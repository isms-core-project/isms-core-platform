"""VirusTotal IOC enrichment — updates confidence scores using VT detection ratios.

This is an enrichment feed, not a collection feed. It does NOT add new IOCs;
it queries existing ti_iocs entries against the VirusTotal v3 API and updates
their confidence score based on how many AV engines flagged them as malicious.

  confidence = round((malicious + suspicious) / total_engines × 100)

Supported types: ip, domain, url, md5, sha1, sha256

Rate limits (free tier): 4 req/min, ~500 req/day.
This feed sleeps 15 s between requests and caps at 450 IOCs per run.
IOCs are prioritised: NULL confidence first, then oldest VT check.
IOCs are re-enriched every 30 days.

Requires: VT_API_KEY (free registration at virustotal.com)
Schedule:  daily at 07:00 UTC (runs after collection feeds have populated IOCs)
"""

import base64
import logging
import os
import time
from datetime import datetime, timedelta, timezone

import requests

from feeds.base import fail_run, finish_run, get_conn, is_cancelled, start_run

logger = logging.getLogger(__name__)

_API_BASE     = "https://www.virustotal.com/api/v3"
_API_KEY      = os.environ.get("VT_API_KEY", "")
_DAILY_LIMIT  = int(os.environ.get("VT_DAILY_LIMIT", "450"))  # stay under 500 free-tier cap
_RATE_SLEEP   = 15.0   # seconds between requests → ~4/min
_RECHECK_DAYS = 30     # re-enrich IOCs older than this many days

# VT v3 endpoint per IOC type
_ENDPOINTS = {
    "ip":     "/ip_addresses/{v}",
    "domain": "/domains/{v}",
    "md5":    "/files/{v}",
    "sha1":   "/files/{v}",
    "sha256": "/files/{v}",
    "url":    "/urls/{v}",   # {v} = base64url-encoded URL (no padding)
}


def _url_id(url: str) -> str:
    """VT v3 URL identifier: base64url without padding."""
    return base64.urlsafe_b64encode(url.encode()).rstrip(b"=").decode()


def _score(stats: dict) -> int | None:
    malicious  = stats.get("malicious", 0)
    suspicious = stats.get("suspicious", 0)
    harmless   = stats.get("harmless", 0)
    undetected = stats.get("undetected", 0)
    timeout    = stats.get("timeout", 0)
    total      = malicious + suspicious + harmless + undetected + timeout
    if total == 0:
        return None
    return round((malicious + suspicious) / total * 100)


def _query(session: requests.Session, ioc_type: str, value: str) -> int | None:
    tpl = _ENDPOINTS.get(ioc_type)
    if not tpl:
        return None
    v   = _url_id(value) if ioc_type == "url" else value
    url = f"{_API_BASE}{tpl.format(v=v)}"
    try:
        resp = session.get(url, timeout=30)
        if resp.status_code == 404:
            return None
        if resp.status_code == 429:
            logger.warning("VirusTotal: rate limit hit — sleeping 60 s")
            time.sleep(60)
            return None
        resp.raise_for_status()
        stats = resp.json().get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        return _score(stats)
    except Exception as exc:
        logger.warning("VirusTotal: query error %s %s: %s", ioc_type, value[:60], exc)
        return None


def run() -> None:
    if not _API_KEY:
        logger.warning("VT_API_KEY not set — VirusTotal enrichment disabled")
        run_id = start_run("virustotal")
        finish_run(run_id, 0)
        return

    run_id = start_run("virustotal")
    stale  = datetime.now(timezone.utc) - timedelta(days=_RECHECK_DAYS)
    logger.info("VirusTotal enrichment started (limit=%d, recheck_days=%d)", _DAILY_LIMIT, _RECHECK_DAYS)

    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, ioc_type, value
                FROM   ti_iocs
                WHERE  ioc_type IN ('ip', 'domain', 'url', 'md5', 'sha1', 'sha256')
                  AND  (vt_checked_at IS NULL OR vt_checked_at < %s)
                ORDER BY
                    (confidence IS NULL) DESC,
                    last_seen DESC
                LIMIT %s
            """, (stale, _DAILY_LIMIT))
            rows = cur.fetchall()

    if not rows:
        finish_run(run_id, 0)
        logger.info("VirusTotal: no IOCs need enrichment")
        return

    logger.info("VirusTotal: enriching %d IOCs", len(rows))

    session = requests.Session()
    session.headers.update({"x-apikey": _API_KEY, "Accept": "application/json"})

    now      = datetime.now(timezone.utc)
    enriched = 0
    updated  = 0

    with get_conn() as conn:
        with conn.cursor() as cur:
            for ioc_id, ioc_type, value in rows:
                if is_cancelled("virustotal"):
                    logger.info("VirusTotal: cancelled at %d enriched", enriched)
                    fail_run(run_id, "Cancelled by user")
                    return

                vt_score = _query(session, ioc_type, value)
                time.sleep(_RATE_SLEEP)

                # Update vt_checked_at always; update confidence only when VT
                # returns a score AND it is higher than the current value.
                cur.execute("""
                    UPDATE ti_iocs
                    SET    vt_checked_at = %s,
                           confidence    = CASE
                               WHEN %s IS NOT NULL
                                AND (confidence IS NULL OR %s > confidence)
                               THEN %s
                               ELSE confidence
                           END
                    WHERE  id = %s
                """, (now, vt_score, vt_score, vt_score, ioc_id))

                enriched += 1
                if vt_score is not None:
                    updated += 1
                    logger.debug("VT %s %s → %d%%", ioc_type, value[:60], vt_score)

    finish_run(run_id, enriched)
    logger.info(
        "VirusTotal enrichment complete: %d checked, %d scores updated",
        enriched, updated,
    )
