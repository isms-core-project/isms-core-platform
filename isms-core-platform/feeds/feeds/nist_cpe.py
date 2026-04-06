"""Phase 27 — NVD CPE feed (Option B — KEV-vendor driven).

Queries the NVD CPE API for each unique vendor/product pair in CISA KEV entries,
indexing results into OpenSearch `nvd-cpe` with source=kev_vendor.

Only runs when FEEDS_CPE_FULL=true.
Merges with Option A CPEs (from nist_cve.py) — deduplicated by CPE URI.

Schedule: Sunday 01:30 UTC (after CVE full pull at 01:00)

Env:
  NIST_API_KEY      — optional, raises rate limit from 5→50 req/30s
  FEEDS_CPE_FULL    — must be true to run (default: false)
  OPENSEARCH_URL    — OpenSearch host (default: http://opensearch:9200)
"""

import logging
import os
import time
from datetime import datetime, timezone

import requests

from feeds.base import fail_run, finish_run, get_conn, start_run

logger = logging.getLogger(__name__)

NVD_CPE_URL = "https://services.nvd.nist.gov/rest/json/cpes/2.0"
_RUN_NAME   = "nist_cpe"

_SLEEP_NO_KEY = 0.65
_SLEEP_KEY    = 0.12


def _headers() -> dict:
    key = os.environ.get("NIST_API_KEY", "").strip()
    return {"apiKey": key} if key else {}


def _sleep():
    key = os.environ.get("NIST_API_KEY", "").strip()
    time.sleep(_SLEEP_KEY if key else _SLEEP_NO_KEY)


def _get_os_client():
    from opensearchpy import OpenSearch
    url = os.environ.get("OPENSEARCH_URL", "http://opensearch:9200")
    return OpenSearch(hosts=[url], use_ssl=False, verify_certs=False, timeout=30)


def _get_kev_vendors() -> list[tuple[str, str]]:
    """Return unique (vendor_project, product) pairs from KEV entries."""
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT DISTINCT vendor_project, product
                    FROM cisa_kev_entries
                    WHERE vendor_project IS NOT NULL AND product IS NOT NULL
                    ORDER BY vendor_project, product
                    """
                )
                return [(r[0], r[1]) for r in cur.fetchall()]
    except Exception as e:
        logger.warning("Could not load KEV vendors: %s", e)
        return []


def _get_kev_cve_ids() -> set[str]:
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT cve_id FROM cisa_kev_entries")
                return {r[0] for r in cur.fetchall()}
    except Exception:
        return set()


def run() -> None:
    if os.environ.get("FEEDS_CPE_FULL", "false").lower() != "true":
        logger.info("FEEDS_CPE_FULL not enabled — skipping CPE Option B pull")
        return

    run_id = start_run(_RUN_NAME)
    logger.info("NVD CPE (Option B — KEV-vendor) pull started")

    try:
        os_client = _get_os_client()
    except Exception as exc:
        fail_run(run_id, f"OpenSearch init failed: {exc}")
        return

    vendors      = _get_kev_vendors()
    kev_ids      = _get_kev_cve_ids()
    now_iso      = datetime.now(timezone.utc).isoformat()
    indexed      = 0
    skipped      = 0

    logger.info("Querying NVD CPE API for %d vendor/product pairs", len(vendors))

    for vendor, product in vendors:
        # Build a keyword search: "vendor product"
        keyword = f"{vendor} {product}"[:100]
        _sleep()
        try:
            resp = requests.get(
                NVD_CPE_URL,
                headers=_headers(),
                params={"keywordSearch": keyword, "resultsPerPage": 100},
                timeout=30,
            )
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logger.warning("CPE query failed for '%s': %s", keyword, e)
            skipped += 1
            continue

        for item in data.get("products") or []:
            cpe = item.get("cpe") or {}
            uri = cpe.get("cpeName") or ""
            if not uri:
                continue

            parts   = uri.split(":")
            part    = parts[2] if len(parts) > 2 else ""
            v       = parts[3] if len(parts) > 3 else ""
            p       = parts[4] if len(parts) > 4 else ""
            version = parts[5] if len(parts) > 5 else ""

            # Title: prefer English deprecation title, else build from parts
            title = ""
            for t in cpe.get("titles") or []:
                if t.get("lang") == "en":
                    title = t.get("title", "")
                    break
            if not title:
                title = f"{v} {p} {version}".strip()

            try:
                os_client.index(
                    index="nvd-cpe",
                    id=uri,
                    body={
                        "cpe_uri":    uri,
                        "part":       part,
                        "vendor":     v,
                        "product":    p,
                        "version":    version,
                        "title":      title,
                        "in_kev":     True,   # all of these are KEV-vendor matched
                        "source":     "kev_vendor",
                        "indexed_at": now_iso,
                    },
                )
                indexed += 1
            except Exception as e:
                logger.warning("Failed to index CPE %s: %s", uri, e)

    finish_run(run_id, indexed)
    logger.info("NVD CPE Option B complete: %d CPEs indexed, %d vendor queries skipped", indexed, skipped)
