"""CISA Known Exploited Vulnerabilities feed.

Source: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json

After upserting to PostgreSQL, bulk-indexes entries to the OpenSearch `cisa-kev` index
so OSD dashboards and cross-enrichment can query KEV data directly.
"""

import logging
import os
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


_OS_INDEX = "cisa-kev"

_OS_MAPPING = {
    "mappings": {
        "properties": {
            "cve_id":             {"type": "keyword"},
            "vendor_project":     {"type": "keyword"},
            "product":            {"type": "keyword"},
            "vulnerability_name": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 512}}},
            "date_added":         {"type": "date", "format": "yyyy-MM-dd||strict_date_optional_time"},
            "short_description":  {"type": "text"},
            "required_action":    {"type": "text"},
            "due_date":           {"type": "date", "format": "yyyy-MM-dd||strict_date_optional_time"},
            "known_ransomware":   {"type": "boolean"},
            "notes":              {"type": "text"},
            "indexed_at":         {"type": "date"},
        }
    }
}


def _sync_to_opensearch(vulns: list[dict]) -> int:
    """Bulk-upsert KEV entries to the `cisa-kev` OpenSearch index."""
    try:
        from opensearchpy import OpenSearch
        from opensearchpy import helpers as os_helpers
    except ImportError:
        logger.warning("opensearch-py not available — skipping KEV → OpenSearch sync")
        return 0

    url = os.environ.get("OPENSEARCH_URL", "http://opensearch:9200")
    try:
        client = OpenSearch(hosts=[url], use_ssl=False, verify_certs=False, timeout=30)
        if not client.ping():
            logger.warning("OpenSearch not reachable — skipping KEV sync")
            return 0
        if not client.indices.exists(index=_OS_INDEX):
            client.indices.create(index=_OS_INDEX, body=_OS_MAPPING)
            logger.info("Created OpenSearch index: %s", _OS_INDEX)
    except Exception as exc:
        logger.warning("OpenSearch unavailable for KEV sync: %s", exc)
        return 0

    now_iso = datetime.now(timezone.utc).isoformat()

    def _actions():
        for v in vulns:
            yield {
                "_op_type": "index",
                "_index":   _OS_INDEX,
                "_id":      v["cve_id"],
                "_source":  {**v, "indexed_at": now_iso},
            }

    indexed = 0
    try:
        for ok, _ in os_helpers.streaming_bulk(
            client, _actions(), raise_on_error=False, chunk_size=500
        ):
            if ok:
                indexed += 1
    except Exception as exc:
        logger.warning("KEV → OpenSearch bulk error: %s", exc)

    logger.info("KEV → OpenSearch sync: %d indexed", indexed)
    return indexed


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
    os_docs: list[dict] = []

    with get_conn() as conn:
        with conn.cursor() as cur:
            for v in vulns:
                cve_id = v.get("cveID") or ""
                if not cve_id:
                    continue

                ransomware_str = (v.get("knownRansomwareCampaignUse") or "").lower()
                known_ransomware = ransomware_str in ("known", "yes", "true")
                vendor  = (v.get("vendorProject") or "")[:255]
                product = (v.get("product") or "")[:255]
                name    = (v.get("vulnerabilityName") or "")[:512]
                added   = _parse_date(v.get("dateAdded"))
                desc    = (v.get("shortDescription") or "")[:4000]
                action  = (v.get("requiredAction") or "")[:2000]
                due     = _parse_date(v.get("dueDate"))
                notes   = (v.get("notes") or "")[:2000] or None

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
                    (str(uuid4()), cve_id, vendor, product, name, added,
                     desc, action, due, known_ransomware, notes, now, now),
                )
                upserted += 1
                os_docs.append({
                    "cve_id":             cve_id,
                    "vendor_project":     vendor,
                    "product":            product,
                    "vulnerability_name": name,
                    "date_added":         added.isoformat() if added else None,
                    "short_description":  desc,
                    "required_action":    action,
                    "due_date":           due.isoformat() if due else None,
                    "known_ransomware":   known_ransomware,
                    "notes":              notes,
                })

    _sync_to_opensearch(os_docs)

    finish_run(run_id, upserted)
    logger.info("CISA KEV completed: %d entries upserted", upserted)
