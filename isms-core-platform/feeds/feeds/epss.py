"""FIRST EPSS (Exploit Prediction Scoring System) feed.

Source: https://api.first.org/data/v1/epss?limit=10000&order=!epss

Fetches the top 10,000 CVEs by EPSS score (covers all meaningful exploitation
probability — anything outside top 10K has EPSS < ~0.001).

After upserting to PostgreSQL, immediately bulk-updates the nvd-cve OpenSearch
index so that EPSS scores are fresh in the UI on the same daily cycle, even for
CVEs whose NVD records have not been modified (and would not be re-indexed by the
daily CVE delta run).
"""

import logging
import os
from datetime import date, datetime, timezone
from uuid import uuid4

import requests

from feeds.base import fail_run, finish_run, get_conn, start_run

logger = logging.getLogger(__name__)

EPSS_URL = "https://api.first.org/data/v1/epss?limit=10000&order=!epss"
_OS_INDEX = "nvd-cve"


def _sync_to_opensearch(scores: dict[str, float]) -> int:
    """Bulk partial-update epss_score on existing nvd-cve documents.

    Only updates documents that already exist — does not create new ones.
    CVEs not yet indexed by the NVD feed are silently skipped.
    """
    try:
        from opensearchpy import OpenSearch
        from opensearchpy import helpers as os_helpers
    except ImportError:
        logger.warning("opensearch-py not available — skipping EPSS → OpenSearch sync")
        return 0

    url = os.environ.get("OPENSEARCH_URL", "http://opensearch:9200")
    try:
        client = OpenSearch(hosts=[url], use_ssl=False, verify_certs=False, timeout=30)
        if not client.indices.exists(index=_OS_INDEX):
            logger.info("nvd-cve index does not exist yet — skipping EPSS sync")
            return 0
    except Exception as exc:
        logger.warning("OpenSearch unavailable for EPSS sync: %s", exc)
        return 0

    def _actions():
        for cve_id, score in scores.items():
            yield {
                "_op_type": "update",
                "_index":   _OS_INDEX,
                "_id":      cve_id,
                "doc":      {"epss_score": score},
            }

    updated = 0
    errors  = 0
    try:
        for ok, info in os_helpers.streaming_bulk(
            client,
            _actions(),
            raise_on_error=False,
            chunk_size=1000,
            max_retries=2,
        ):
            if ok:
                updated += 1
            else:
                # 404 = CVE not yet in index (normal for new CVEs); log others
                err = info.get("update", {}).get("error", {})
                if err.get("type") != "document_missing_exception":
                    logger.debug("EPSS sync skip: %s", info)
                errors += 1
    except Exception as exc:
        logger.warning("EPSS → OpenSearch bulk error: %s", exc)

    logger.info("EPSS → OpenSearch sync: %d updated, %d not-found/skipped", updated, errors)
    return updated


def run() -> None:
    run_id = start_run("epss")
    logger.info("FIRST EPSS pull started")

    try:
        resp = requests.get(EPSS_URL, timeout=60)
        resp.raise_for_status()
        payload = resp.json()
    except Exception as exc:
        fail_run(run_id, str(exc))
        logger.error("EPSS download failed: %s", exc)
        return

    items = (payload.get("data") or [])
    if not items:
        fail_run(run_id, "Empty data in EPSS response")
        return

    # Date of the score set (from API timestamp field)
    score_date: date | None = None
    try:
        ts = payload.get("timestamp")
        if ts:
            score_date = datetime.fromisoformat(ts[:10]).date()
    except Exception:
        score_date = date.today()

    now = datetime.now(timezone.utc)
    upserted = 0
    scores: dict[str, float] = {}

    with get_conn() as conn:
        with conn.cursor() as cur:
            for item in items:
                cve_id = item.get("cve") or ""
                if not cve_id:
                    continue
                try:
                    score      = float(item.get("epss", 0))
                    percentile = float(item.get("percentile", 0))
                except (ValueError, TypeError):
                    continue

                cur.execute(
                    """
                    INSERT INTO epss_scores
                      (id, cve_id, score, percentile, score_date, created_at, updated_at)
                    VALUES (%s,%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (cve_id) DO UPDATE SET
                      score      = EXCLUDED.score,
                      percentile = EXCLUDED.percentile,
                      score_date = EXCLUDED.score_date,
                      updated_at = EXCLUDED.updated_at
                    """,
                    (str(uuid4()), cve_id, score, percentile, score_date, now, now),
                )
                scores[cve_id] = score
                upserted += 1

    # Push fresh scores to OpenSearch immediately so the CVE Explorer
    # reflects today's EPSS without waiting for the next full NVD pull.
    _sync_to_opensearch(scores)

    finish_run(run_id, upserted)
    logger.info("FIRST EPSS completed: %d scores upserted", upserted)
