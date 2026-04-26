"""ISMS CORE Feeds Scheduler.

Pulls threat intelligence and vulnerability data on fixed schedules:
  - NVD CVE full   : weekly   (Sunday 01:00 UTC)
  - NVD CPE Opt-B  : weekly   (Sunday 01:30 UTC — only if FEEDS_CPE_FULL=true)
  - MITRE ATT&CK   : weekly   (Sunday 02:00 UTC)
  - MITRE ATLAS    : weekly   (Sunday 02:30 UTC)
  - CISA KEV       : daily    (03:00 UTC)
  - NVD CVE delta  : daily    (03:00 UTC — runs alongside KEV, both are fast)
  - FIRST EPSS     : daily    (03:30 UTC)
  - ENISA EUVD full : weekly  (Sunday 02:45 UTC)
  - ENISA EUVD delta: daily   (04:00 UTC)

Each feed can be disabled via env vars:
  FEEDS_MITRE_ENABLED=true|false
  FEEDS_ATLAS_ENABLED=true|false
  FEEDS_KEV_ENABLED=true|false
  FEEDS_EPSS_ENABLED=true|false
  FEEDS_CVE_ENABLED=true|false
  FEEDS_CPE_ENABLED=true|false  (Option A always runs as part of CVE pull)
  FEEDS_CPE_FULL=false          (Option B KEV-vendor CPE — default off)
  FEEDS_EUVD_ENABLED=true|false (default: true)
  FEEDS_RUN_ON_START=false      (force-run all feeds on every start — default: false)

Startup behaviour:
  - By default feeds do NOT run on container start — they wait for their scheduled window.
  - Exception: if a feed has never had a successful run (first deployment), it runs once
    automatically so the platform has data on day 1.
  - Set FEEDS_RUN_ON_START=true to force-run all enabled feeds on every start (admin override).

Environment:
  DATABASE_URL          — PostgreSQL DSN
  OPENSEARCH_URL        — OpenSearch host (default: http://opensearch:9200)
  NIST_API_KEY          — optional, raises NVD rate limit from 5→50 req/30s
  FEEDS_RUN_ON_START    — force-run all feeds on start regardless of DB state (default: false)
  FEEDS_MITRE_ENABLED   — (default: true)
  FEEDS_ATLAS_ENABLED   — (default: true)
  FEEDS_KEV_ENABLED     — (default: true)
  FEEDS_EPSS_ENABLED    — (default: true)
  FEEDS_CVE_ENABLED     — (default: false)
  FEEDS_CPE_FULL        — enable Option B KEV-vendor CPE pull (default: false)
"""

import logging
import os
import time

import schedule

from feeds import cisa_kev, epss, euvd, mitre_atlas, mitre_attack, nist_cpe, nist_cve, trigger_server
from feeds.base import has_successful_run

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s %(message)s",
)
logger = logging.getLogger("scheduler")


def _enabled(var: str) -> bool:
    return os.environ.get(var, "true").lower() == "true"


def _safe(fn, name: str):
    def wrapper():
        logger.info("Starting feed: %s", name)
        try:
            fn()
        except Exception as exc:
            logger.error("Feed %s failed: %s", name, exc, exc_info=True)
    return wrapper


def _clear_stale_runs():
    """Mark any feed_runs still in 'running' state as failed — left over from a previous container crash."""
    try:
        from feeds.base import get_conn
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    UPDATE feed_runs SET status='error', finished_at=NOW(),
                      error_message='Container restarted — run interrupted'
                    WHERE status='running'
                    """
                )
                count = cur.rowcount
        if count:
            logger.info("Cleared %d stale running feed_run(s) on startup", count)
    except Exception as exc:
        logger.warning("Could not clear stale feed runs: %s", exc)


def main():
    _clear_stale_runs()
    trigger_server.start()

    # FEEDS_RUN_ON_START=true → force-run all feeds now (admin override, old behaviour)
    # FEEDS_RUN_ON_START=false (default) → only seed feeds that have never run successfully
    force_run = os.environ.get("FEEDS_RUN_ON_START", "false").lower() == "true"

    # ── Schedule ────────────────────────────────────────────────────────────────

    if _enabled("FEEDS_MITRE_ENABLED"):
        schedule.every().sunday.at("02:00").do(_safe(mitre_attack.run, "MITRE ATT&CK"))
    if _enabled("FEEDS_ATLAS_ENABLED"):
        schedule.every().sunday.at("02:30").do(_safe(mitre_atlas.run, "MITRE ATLAS"))
    if _enabled("FEEDS_KEV_ENABLED"):
        schedule.every().day.at("03:00").do(_safe(cisa_kev.run, "CISA KEV"))
    if _enabled("FEEDS_EPSS_ENABLED"):
        schedule.every().day.at("03:30").do(_safe(epss.run, "FIRST EPSS"))
    if _enabled("FEEDS_CVE_ENABLED"):
        schedule.every().sunday.at("01:00").do(_safe(nist_cve.run_full, "NVD CVE (full)"))
        schedule.every().day.at("03:00").do(_safe(nist_cve.run_delta, "NVD CVE (delta)"))
        schedule.every().sunday.at("01:30").do(_safe(nist_cpe.run, "NVD CPE (Option B)"))
    if _enabled("FEEDS_EUVD_ENABLED"):
        schedule.every().sunday.at("02:45").do(_safe(euvd.run_full, "ENISA EUVD (full)"))
        schedule.every().day.at("04:00").do(_safe(euvd.run_delta, "ENISA EUVD (delta)"))

    # ── Startup runs ─────────────────────────────────────────────────────────────
    # Fast feeds first (<5s each), heavy full-pulls last.
    # Each feed only runs if force_run=True OR it has never had a successful run (first deploy).

    def _should_run(feed_name_prefix: str) -> bool:
        if force_run:
            return True
        if not has_successful_run(feed_name_prefix):
            logger.info("First-boot seed: %s has no successful runs — running now", feed_name_prefix)
            return True
        return False

    if _enabled("FEEDS_MITRE_ENABLED") and _should_run("mitre_attack"):
        _safe(mitre_attack.run, "MITRE ATT&CK")()
    if _enabled("FEEDS_ATLAS_ENABLED") and _should_run("mitre_atlas"):
        _safe(mitre_atlas.run, "MITRE ATLAS")()
    if _enabled("FEEDS_KEV_ENABLED") and _should_run("cisa_kev"):
        _safe(cisa_kev.run, "CISA KEV")()
    if _enabled("FEEDS_EPSS_ENABLED") and _should_run("epss"):
        _safe(epss.run, "FIRST EPSS")()
    if _enabled("FEEDS_CVE_ENABLED") and _should_run("nist_cve"):
        _safe(nist_cve.run_full, "NVD CVE (full)")()
    if _enabled("FEEDS_CVE_ENABLED") and _should_run("nist_cpe"):
        _safe(nist_cpe.run, "NVD CPE (Option B)")()
    if _enabled("FEEDS_EUVD_ENABLED") and _should_run("euvd"):
        _safe(euvd.run_full, "ENISA EUVD (full)")()

    logger.info("Scheduler running — next jobs: %s", schedule.jobs)

    while True:
        schedule.run_pending()
        time.sleep(30)


if __name__ == "__main__":
    main()
