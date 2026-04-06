"""ISMS CORE Feeds Scheduler.

Pulls threat intelligence and vulnerability data on fixed schedules:
  - MITRE ATT&CK   : weekly   (Sunday 02:00 UTC)
  - MITRE ATLAS    : weekly   (Sunday 02:30 UTC)
  - CISA KEV       : daily    (03:00 UTC)
  - FIRST EPSS     : daily    (03:30 UTC)

Each feed can be disabled via env vars:
  FEEDS_MITRE_ENABLED=true|false
  FEEDS_ATLAS_ENABLED=true|false
  FEEDS_KEV_ENABLED=true|false
  FEEDS_EPSS_ENABLED=true|false

Set FEEDS_RUN_ON_START=true to run all enabled feeds immediately on container start
(useful on first deployment to seed the DB before scheduled runs kick in).

Environment:
  DATABASE_URL          — PostgreSQL DSN
  FEEDS_RUN_ON_START    — run all feeds immediately (default: true)
  FEEDS_MITRE_ENABLED   — (default: true)
  FEEDS_ATLAS_ENABLED   — (default: true)
  FEEDS_KEV_ENABLED     — (default: true)
  FEEDS_EPSS_ENABLED    — (default: true)
"""

import logging
import os
import time

import schedule

from feeds import cisa_kev, epss, mitre_atlas, mitre_attack

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
