"""ISMS CORE Threat Intelligence Scheduler.

Pulls OSINT threat feeds on fixed schedules:
  - CIRCL MISP         : every 6h (00:00, 06:00, 12:00, 18:00 UTC)
  - Botvrij MISP       : every 6h (01:00, 07:00, 13:00, 19:00 UTC — staggered)
  - AbuseIPDB BL       : daily    (02:00 UTC)
  - URLhaus            : daily    (03:00 UTC)
  - ThreatFox          : every 6h (03:00, 09:00, 15:00, 21:00 UTC)
  - SSL Blacklist      : daily    (04:00 UTC)
  - Feodo Tracker      : every 6h (04:30, 10:30, 16:30, 22:30 UTC)
  - Red Flag Domains   : daily    (05:00 UTC)
  - Stopforumspam      : daily    (05:30 UTC)
  - AlienVault OTX     : daily    (04:30 UTC)
  - Malpedia           : weekly   (Sunday 03:00 UTC)
  - MaxMind MMDB       : weekly   (Tuesday 01:00 UTC — MaxMind publishes Tuesdays)

On-demand enrichment (AbuseIPDB check + Shodan) is served by the backend via
POST /api/v1/threat-intel/enrich/ip — not scheduled here.

Each source can be disabled via env vars:
  TI_MISP_CIRCL_ENABLED=true|false         (default: true)
  TI_MISP_BOTVRIJ_ENABLED=true|false       (default: true)
  TI_ABUSEIPDB_ENABLED=true|false          (default: true)
  TI_URLHAUS_ENABLED=true|false            (default: true)
  TI_THREATFOX_ENABLED=true|false          (default: true)
  TI_SSLBL_ENABLED=true|false              (default: true)
  TI_FEODOTRACKER_ENABLED=true|false       (default: true)
  TI_RED_FLAG_DOMAINS_ENABLED=true|false   (default: true)
  TI_STOPFORUMSPAM_ENABLED=true|false      (default: true)
  TI_ALIENVAULT_ENABLED=true|false         (default: true)
  TI_MALPEDIA_ENABLED=true|false           (default: true)

First-run seed logic:
  - If a feed has never had a successful run it runs once on startup.
  - Set TI_RUN_ON_START=true to force-run all feeds on every start.

Date floor for MISP (first run only):
  TI_MISP_IMPORT_FROM_DATE=2024-01-01  (default — full history: 2000-01-01)
"""

import logging
import os
import time

import schedule

from feeds import alienvault, abuseipdb, feodotracker, malwarebazaar, malpedia, maxmind, misp_feed, red_flag_domains, sslbl, stopforumspam, threatfox, urlhaus, virustotal
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
    """Delete any feed_run rows left in 'running' state from a previous container session.
    Deleting (not marking error) avoids false health alerts — an interrupted run
    caused by container restart is not a real failure."""
    try:
        from feeds.base import get_conn
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM feed_runs
                    WHERE (
                        status = 'running'
                        OR (status = 'error' AND error_message = 'Container restarted — run interrupted')
                    )
                    AND (  feed_name LIKE 'circl_misp%'
                        OR feed_name LIKE 'botvrij_misp%'
                        OR feed_name LIKE 'abuseipdb%'
                        OR feed_name LIKE 'malpedia%'
                        OR feed_name LIKE 'urlhaus%'
                        OR feed_name LIKE 'threatfox%'
                        OR feed_name LIKE 'sslbl%'
                        OR feed_name LIKE 'red_flag_domains%'
                        OR feed_name LIKE 'stopforumspam%'
                        OR feed_name LIKE 'malwarebazaar%'
                        OR feed_name LIKE 'feodotracker%'
                        OR feed_name LIKE 'alienvault%'
                        OR feed_name LIKE 'virustotal%'
                        )
                    """
                )
                count = cur.rowcount
        if count:
            logger.info("Removed %d interrupted TI feed_run(s) from previous container session", count)
    except Exception as exc:
        logger.warning("Could not clear stale TI feed runs: %s", exc)


def main():
    # Register on-demand trigger endpoints (must match _TRIGGER_MAP in backend threat_intel.py)
    trigger_server.register("circl_misp",        misp_feed.run_circl)
    trigger_server.register("botvrij_misp",       misp_feed.run_botvrij)
    trigger_server.register("abuseipdb_blacklist", abuseipdb.run_blacklist)
    trigger_server.register("malpedia",           malpedia.run)
    trigger_server.register("urlhaus",            urlhaus.run)
    trigger_server.register("threatfox",          threatfox.run)
    trigger_server.register("sslbl",              sslbl.run)
    trigger_server.register("red_flag_domains",   red_flag_domains.run)
    trigger_server.register("stopforumspam",      stopforumspam.run)
    trigger_server.register("malwarebazaar",      malwarebazaar.run)
    trigger_server.register("feodotracker",       feodotracker.run)
    trigger_server.register("alienvault",          alienvault.run)
    trigger_server.register("virustotal",          virustotal.run)
    trigger_server.start()

    _clear_stale_runs()

    # Download GeoLite2 MMDB files on startup if not already on the volume
    _safe(maxmind.ensure_mmdb, "MaxMind MMDB init")()

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

    if _enabled("TI_URLHAUS_ENABLED"):
        schedule.every().day.at("03:00").do(_safe(urlhaus.run, "URLhaus"))

    if _enabled("TI_THREATFOX_ENABLED"):
        for hour in ("03:00", "09:00", "15:00", "21:00"):
            schedule.every().day.at(hour).do(_safe(threatfox.run, "ThreatFox"))

    if _enabled("TI_SSLBL_ENABLED"):
        schedule.every().day.at("04:00").do(_safe(sslbl.run, "SSL Blacklist"))

    if _enabled("TI_FEODOTRACKER_ENABLED"):
        for hour in ("04:30", "10:30", "16:30", "22:30"):
            schedule.every().day.at(hour).do(_safe(feodotracker.run, "Feodo Tracker"))

    if _enabled("TI_RED_FLAG_DOMAINS_ENABLED"):
        schedule.every().day.at("05:00").do(_safe(red_flag_domains.run, "Red Flag Domains"))

    if _enabled("TI_STOPFORUMSPAM_ENABLED"):
        schedule.every().day.at("05:30").do(_safe(stopforumspam.run, "Stopforumspam"))

    if _enabled("TI_ALIENVAULT_ENABLED"):
        schedule.every().day.at("04:30").do(_safe(alienvault.run, "AlienVault OTX"))

        if _enabled("TI_VIRUSTOTAL_ENABLED"):
            schedule.every().day.at("07:00").do(_safe(virustotal.run, "VirusTotal enrichment"))

    if _enabled("TI_MALWAREBAZAAR_ENABLED"):
        for hour in ("02:00", "08:00", "14:00", "20:00"):
            schedule.every().day.at(hour).do(_safe(malwarebazaar.run, "MalwareBazaar"))

    if _enabled("TI_MALPEDIA_ENABLED"):
        schedule.every().sunday.at("03:00").do(_safe(malpedia.run, "Malpedia"))

    # MaxMind publishes updated GeoLite2 databases every Tuesday
    schedule.every().tuesday.at("01:00").do(_safe(maxmind.refresh_mmdb, "MaxMind MMDB refresh"))

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
    if _enabled("TI_URLHAUS_ENABLED") and _should_run("urlhaus"):
        _safe(urlhaus.run, "URLhaus")()
    if _enabled("TI_THREATFOX_ENABLED") and _should_run("threatfox"):
        _safe(threatfox.run, "ThreatFox")()
    if _enabled("TI_SSLBL_ENABLED") and _should_run("sslbl"):
        _safe(sslbl.run, "SSL Blacklist")()
    if _enabled("TI_FEODOTRACKER_ENABLED") and _should_run("feodotracker"):
        _safe(feodotracker.run, "Feodo Tracker")()
    if _enabled("TI_RED_FLAG_DOMAINS_ENABLED") and _should_run("red_flag_domains"):
        _safe(red_flag_domains.run, "Red Flag Domains")()
    if _enabled("TI_STOPFORUMSPAM_ENABLED") and _should_run("stopforumspam"):
        _safe(stopforumspam.run, "Stopforumspam")()
    if _enabled("TI_ALIENVAULT_ENABLED") and _should_run("alienvault"):
        _safe(alienvault.run, "AlienVault OTX")()
    if _enabled("TI_MALWAREBAZAAR_ENABLED") and _should_run("malwarebazaar"):
        _safe(malwarebazaar.run, "MalwareBazaar")()
    if _enabled("TI_MALPEDIA_ENABLED") and _should_run("malpedia"):
        _safe(malpedia.run, "Malpedia")()

    logger.info("TI scheduler running — next jobs: %s", schedule.jobs)

    while True:
        schedule.run_pending()
        time.sleep(30)


if __name__ == "__main__":
    main()
