"""Red Flag Domains feed — newly registered suspicious domains.

Source: https://red.flag.domains/posts/{YYYY-MM-DD}.txt (daily plain-text)
Pull schedule: daily (05:00 UTC). No API key required.

Tries today's list first; falls back to yesterday if not yet published.
"""

import logging
from datetime import datetime, timedelta, timezone
from uuid import uuid4

import requests

from feeds.base import (
    fail_run, finish_run, get_conn, get_os_client, is_cancelled, os_bulk_upsert, start_run,
)

logger = logging.getLogger(__name__)

_BASE_URL = "https://dl.red.flag.domains/daily"
_OS_INDEX = "ti-red-flag-domains"

_OS_MAPPING = {
    "mappings": {
        "properties": {
            "domain":     {"type": "keyword"},
            "date_added": {"type": "date"},
            "indexed_at": {"type": "date"},
        }
    }
}


def run() -> None:
    run_id  = start_run("red_flag_domains")
    now     = datetime.now(timezone.utc)
    now_iso = now.isoformat()
    today   = now.date()

    # Always fetch yesterday's list (today's may not be published yet)
    # Falls back to two days ago in case yesterday is also missing
    domains: list[str] = []
    date_used = None
    for attempt_date in (today - timedelta(days=1), today - timedelta(days=2)):
        url = f"{_BASE_URL}/{attempt_date}.txt"
        try:
            resp = requests.get(url, timeout=30)
            if resp.status_code == 404:
                continue
            resp.raise_for_status()
            lines = [l.strip() for l in resp.text.splitlines() if l.strip() and not l.startswith("#")]
            if lines:
                domains = lines
                date_used = attempt_date
                break
        except Exception as exc:
            logger.warning("Red Flag Domains fetch failed for %s: %s", attempt_date, exc)

    if not domains:
        # Not an error — list may not be published yet or for this date
        logger.info("Red Flag Domains: no list available for today or yesterday — skipping")
        finish_run(run_id, 0)
        return

    logger.info("Red Flag Domains: %d domains from %s", len(domains), date_used)

    os_client = get_os_client()
    if os_client:
        try:
            if not os_client.indices.exists(index=_OS_INDEX):
                os_client.indices.create(index=_OS_INDEX, body=_OS_MAPPING)
                logger.info("Created OpenSearch index: %s", _OS_INDEX)
        except Exception as exc:
            logger.warning("OpenSearch index setup failed: %s", exc)
            os_client = None

    date_dt  = datetime(date_used.year, date_used.month, date_used.day, tzinfo=timezone.utc)
    upserted = 0
    os_docs: list[dict] = []

    with get_conn() as conn:
        with conn.cursor() as cur:
            for domain in domains:
                if is_cancelled("red_flag_domains"):
                    logger.info("Red Flag Domains cancelled at %d entries", upserted)
                    fail_run(run_id, "Cancelled by user")
                    return

                domain = domain.lower()
                if not domain or len(domain) > 253:
                    continue

                cur.execute(
                    """
                    INSERT INTO ti_iocs
                      (id, ioc_type, value, source, confidence, tags, mitre_tids,
                       family_slugs, actor_slugs, event_uuids, first_seen, last_seen, created_at)
                    VALUES (%s,'domain',%s,'red_flag_domains',50,
                            '["newly-registered"]'::jsonb,'[]'::jsonb,
                            '[]'::jsonb,'[]'::jsonb,'[]'::jsonb,%s,%s,%s)
                    ON CONFLICT (ioc_type, value, source) DO UPDATE SET
                      last_seen = GREATEST(ti_iocs.last_seen, EXCLUDED.last_seen)
                    """,
                    (str(uuid4()), domain, date_dt, now, now),
                )
                upserted += 1

                os_docs.append({
                    "domain":     domain,
                    "date_added": date_dt.isoformat(),
                    "indexed_at": now_iso,
                    "_os_id":     f"rfd:{domain}",
                })

                if len(os_docs) >= 2000 and os_client:
                    os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")
                    os_docs = []

    if os_docs and os_client:
        os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")

    finish_run(run_id, upserted)
    logger.info("Red Flag Domains completed: %d domains upserted", upserted)
