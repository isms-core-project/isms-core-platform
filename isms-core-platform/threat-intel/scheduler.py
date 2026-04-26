"""ISMS CORE Threat Intelligence Scheduler.

Pulls OSINT threat feeds on fixed schedules:
  - CIRCL MISP    : every 6h (00:00, 06:00, 12:00, 18:00 UTC)
  - Botvrij MISP  : every 6h (01:00, 07:00, 13:00, 19:00 UTC — staggered)
  - AbuseIPDB BL  : daily    (02:00 UTC)
  - Malpedia      : weekly   (Sunday 03:00 UTC) — no key needed; MALPEDIA_API_KEY improves rate limits

On-demand enrichment (AbuseIPDB check + Shodan) is served by the backend via
POST /api/v1/threat-intel/enrich/ip — not scheduled here.

Each source can be disabled via env vars:
  TI_MISP_CIRCL_ENABLED=true|false     (default: true)
  TI_MISP_BOTVRIJ_ENABLED=true|false   (default: true)
  TI_ABUSEIPDB_ENABLED=true|false      (default: true)
  TI_MALPEDIA_ENABLED=true|false       (default: true)

First-run seed logic (same as feeds container):
  - If a feed has never had a successful run it runs once on startup.
  - Set TI_RUN_ON_START=true to force-run all feeds on every start.

Date floor for MISP (first run only):
  TI_MISP_IMPORT_FROM_DATE=2024-01-01  (default — full history: 2000-01-01)
"""

import logging
import os
import time

import schedule

from feeds import misp_feed, abuseipdb, malpedia
from feeds.base import has_successful_run
import trigger_server

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s %(message)s",
)
logger = logging.getLogger("ti-scheduler")


def _enabled(var: str) -> bool:
    return os.environ.get(var, "true").lower() == "true"


def _safe(fn, name: str):
    def wrapper():
        logger.info("Starting TI feed: %s", name)
        try:
            fn()
        except Exception as exc:
            logger.error("TI feed %s failed: %s", name, exc, exc_info=True)
    return wrapper


def _clear_stale_runs():
    try:
        from feeds.base import get_conn
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE feed_runs SET status='error', finished_at=NOW(),
                      error_message='Container restarted — run interrupted'
                    WHERE status='running'
                    AND (  feed_name LIKE 'circl_misp%'
                        OR feed_name LIKE 'botvrij_misp%'
                        OR feed_name LIKE 'abuseipdb%'
                        OR feed_name LIKE 'malpedia%'
                        )
                    """
                )
                count = cur.rowcount
        if count:
            logger.info("Cleared %d stale TI feed_run(s) on startup", count)
    except Exception as exc:
        logger.warning("Could not clear stale TI feed runs: %s", exc)


def main():
    # Register on-demand trigger endpoints (matches _TRIGGER_MAP in backend threat_intel.py)
    trigger_server.register("circl_misp",        misp_feed.run_circl)
    trigger_server.register("botvrij_misp",       misp_feed.run_botvrij)
    trigger_server.register("abuseipdb_blacklist", abuseipdb.run_blacklist)
    trigger_server.register("malpedia",           malpedia.run)
    trigger_server.start()

    _clear_stale_runs()

    force_run = os.environ.get("TI_RUN_ON_START", "false").lower() == "true"

    # ── Schedule ─────────────────────────────────────────────────────────────

    if _enabled("TI_MISP_CIRCL_ENABLED"):
        for hour in ("00:00", "06:00", "12:00", "18:00"):
            schedule.every().day.at(hour).do(_safe(misp_feed.run_circl, "CIRCL MISP"))

    if _enabled("TI_MISP_BOTVRIJ_ENABLED"):
        for hour in ("01:00", "07:00", "13:00", "19:00"):
            schedule.every().day.at(hour).do(_safe(misp_feed.run_botvrij, "Botvrij MISP"))

    if _enabled("TI_ABUSEIPDB_ENABLED"):
        schedule.every().day.at("02:00").do(_safe(abuseipdb.run_blacklist, "AbuseIPDB blacklist"))

    if _enabled("TI_MALPEDIA_ENABLED"):
        schedule.every().sunday.at("03:00").do(_safe(malpedia.run, "Malpedia"))

    # ── Startup seed (first-boot or forced) ──────────────────────────────────

    def _should_run(prefix: str) -> bool:
        if force_run:
            return True
        if not has_successful_run(prefix):
            logger.info("First-boot seed: %s has no successful runs — running now", prefix)
            return True
        return False

    if _enabled("TI_MISP_CIRCL_ENABLED") and _should_run("circl_misp"):
        _safe(misp_feed.run_circl, "CIRCL MISP")()
    if _enabled("TI_MISP_BOTVRIJ_ENABLED") and _should_run("botvrij_misp"):
        _safe(misp_feed.run_botvrij, "Botvrij MISP")()
    if _enabled("TI_ABUSEIPDB_ENABLED") and _should_run("abuseipdb"):
        _safe(abuseipdb.run_blacklist, "AbuseIPDB blacklist")()
    if _enabled("TI_MALPEDIA_ENABLED") and _should_run("malpedia"):
        _safe(malpedia.run, "Malpedia")()

    logger.info("TI scheduler running — next jobs: %s", schedule.jobs)

    while True:
        schedule.run_pending()
        time.sleep(30)


if __name__ == "__main__":
    main()
