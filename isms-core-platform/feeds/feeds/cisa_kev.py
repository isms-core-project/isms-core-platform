"""CISA Known Exploited Vulnerabilities feed.

Source: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
"""

import logging
from datetime import date, datetime, timezone
from uuid import uuid4

import requests

from feeds.base import fail_run, finish_run, get_conn, start_run

logger = logging.getLogger(__name__)

KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"


def _parse_date(s: str | None) -> date | None:
    if not s:
        return None
    try:
        return date.fromisoformat(s)
    except ValueError:
        return None


def run() -> None:
    run_id = start_run("cisa_kev")
    logger.info("CISA KEV pull started")

    try:
        resp = requests.get(KEV_URL, timeout=60)
        resp.raise_for_status()
        data = resp.json()
    except Exception as exc:
        fail_run(run_id, str(exc))
        logger.error("CISA KEV download failed: %s", exc)
        return

    vulns = data.get("vulnerabilities") or []
    if not vulns:
        fail_run(run_id, "No vulnerabilities in response")
        return

    now = datetime.now(timezone.utc)
    upserted = 0

    with get_conn() as conn:
        with conn.cursor() as cur:
            for v in vulns:
                cve_id = v.get("cveID") or ""
                if not cve_id:
                    continue

                ransomware_str = (v.get("knownRansomwareCampaignUse") or "").lower()
                known_ransomware = ransomware_str in ("known", "yes", "true")

                cur.execute(
                    """
                    INSERT INTO cisa_kev_entries
                      (id, cve_id, vendor_project, product, vulnerability_name,
                       date_added, short_description, required_action, due_date,
                       known_ransomware, notes, created_at, updated_at)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (cve_id) DO UPDATE SET
                      vendor_project     = EXCLUDED.vendor_project,
                      product            = EXCLUDED.product,
                      vulnerability_name = EXCLUDED.vulnerability_name,
                      date_added         = EXCLUDED.date_added,
                      short_description  = EXCLUDED.short_description,
                      required_action    = EXCLUDED.required_action,
                      due_date           = EXCLUDED.due_date,
                      known_ransomware   = EXCLUDED.known_ransomware,
                      notes              = EXCLUDED.notes,
                      updated_at         = EXCLUDED.updated_at
                    """,
                    (
                        str(uuid4()),
                        cve_id,
                        (v.get("vendorProject") or "")[:255],
                        (v.get("product") or "")[:255],
                        (v.get("vulnerabilityName") or "")[:512],
                        _parse_date(v.get("dateAdded")),
                        (v.get("shortDescription") or "")[:4000],
                        (v.get("requiredAction") or "")[:2000],
                        _parse_date(v.get("dueDate")),
                        known_ransomware,
                        (v.get("notes") or "")[:2000] or None,
                        now, now,
                    ),
                )
                upserted += 1

    finish_run(run_id, upserted)
    logger.info("CISA KEV completed: %d entries upserted", upserted)
