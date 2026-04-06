"""ISMS CORE Feeds Scheduler.

Pulls threat intelligence and vulnerability data on fixed schedules:
  - NVD CVE full   : weekly   (Sunday 01:00 UTC)
  - NVD CPE Opt-B  : weekly   (Sunday 01:30 UTC — only if FEEDS_CPE_FULL=true)
  - MITRE ATT&CK   : weekly   (Sunday 02:00 UTC)
  - MITRE ATLAS    : weekly   (Sunday 02:30 UTC)
  - CISA KEV       : daily    (03:00 UTC)
  - NVD CVE delta  : daily    (03:00 UTC — runs alongside KEV, both are fast)
  - FIRST EPSS     : daily    (03:30 UTC)

Each feed can be disabled via env vars:
  FEEDS_MITRE_ENABLED=true|false
  FEEDS_ATLAS_ENABLED=true|false
  FEEDS_KEV_ENABLED=true|false
  FEEDS_EPSS_ENABLED=true|false
  FEEDS_CVE_ENABLED=true|false
  FEEDS_CPE_ENABLED=true|false  (Option A always runs as part of CVE pull)
  FEEDS_CPE_FULL=false          (Option B KEV-vendor CPE — default off)

Set FEEDS_RUN_ON_START=true to run all enabled feeds immediately on container start.

Environment:
  DATABASE_URL          — PostgreSQL DSN
  OPENSEARCH_URL        — OpenSearch host (default: http://opensearch:9200)
  NIST_API_KEY          — optional, raises NVD rate limit from 5→50 req/30s
  FEEDS_RUN_ON_START    — run all feeds immediately (default: true)
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

from feeds import cisa_kev, epss, mitre_atlas, mitre_attack, nist_cpe, nist_cve

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


def main():
    run_on_start = os.environ.get("FEEDS_RUN_ON_START", "true").lower() == "true"

    # ── Schedule ────────────────────────────────────────────────────────────────

    # NVD CVE: full weekly + daily delta
    if _enabled("FEEDS_CVE_ENABLED"):
        schedule.every().sunday.at("01:00").do(_safe(nist_cve.run_full, "NVD CVE (full)"))
        schedule.every().day.at("03:00").do(_safe(nist_cve.run_delta, "NVD CVE (delta)"))
        if run_on_start:
            _safe(nist_cve.run_full, "NVD CVE (full)")()

    # NVD CPE Option B: weekly after CVE full (only if FEEDS_CPE_FULL=true)
    if _enabled("FEEDS_CVE_ENABLED") and os.environ.get("FEEDS_CPE_FULL", "false").lower() == "true":
        schedule.every().sunday.at("01:30").do(_safe(nist_cpe.run, "NVD CPE (Option B)"))
        if run_on_start:
            _safe(nist_cpe.run, "NVD CPE (Option B)")()

    if _enabled("FEEDS_MITRE_ENABLED"):
        schedule.every().sunday.at("02:00").do(_safe(mitre_attack.run, "MITRE ATT&CK"))
        if run_on_start:
            _safe(mitre_attack.run, "MITRE ATT&CK")()

    if _enabled("FEEDS_ATLAS_ENABLED"):
        schedule.every().sunday.at("02:30").do(_safe(mitre_atlas.run, "MITRE ATLAS"))
        if run_on_start:
            _safe(mitre_atlas.run, "MITRE ATLAS")()

    if _enabled("FEEDS_KEV_ENABLED"):
        schedule.every().day.at("03:00").do(_safe(cisa_kev.run, "CISA KEV"))
        if run_on_start:
            _safe(cisa_kev.run, "CISA KEV")()

    if _enabled("FEEDS_EPSS_ENABLED"):
        schedule.every().day.at("03:30").do(_safe(epss.run, "FIRST EPSS"))
        if run_on_start:
            _safe(epss.run, "FIRST EPSS")()

    logger.info("Scheduler running — next jobs: %s", schedule.jobs)

    while True:
        schedule.run_pending()
        time.sleep(30)


if __name__ == "__main__":
    main()
