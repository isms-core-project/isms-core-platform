"""ENISA European Vulnerability Database (EUVD) feed.

Source: https://euvdservices.enisa.europa.eu/api

Fetches:
  - Actively Exploited Vulnerabilities — EU analog of CISA KEV
  - Critical Vulnerabilities           — CVSS 8+ catalog

After upsert to PostgreSQL, immediately:
  1. Indexes all records to OpenSearch 'euvd' index.
  2. Bulk-updates 'nvd-cve' with in_euvd=True for matching CVEs so the
     CVE Explorer reflects EU exploitation status on the same daily cycle.
"""

import json
import logging
import os
import time
from datetime import datetime, timezone
from uuid import uuid4

import requests

from feeds.base import fail_run, finish_run, get_conn, start_run

logger = logging.getLogger(__name__)

_BASE_URL  = "https://euvdservices.enisa.europa.eu/api"
_PAGE_SIZE = 500
_OS_INDEX  = "euvd"
_NVD_INDEX = "nvd-cve"


# ── HTTP helpers ──────────────────────────────────────────────────────────────

def _get(path: str, params: dict | None = None) -> dict | list:
    url = f"{_BASE_URL}/{path}"
    resp = requests.get(url, params=params or {}, timeout=60)
    resp.raise_for_status()
    return resp.json()


def _paginate(endpoint: str) -> list[dict]:
    """Fetch all pages from a paginated EUVD list endpoint."""
    items: list[dict] = []
    page = 1
    while True:
        try:
            data = _get(endpoint, {"page": page, "size": _PAGE_SIZE})
        except Exception as exc:
            logger.warning("EUVD %s page %d failed: %s", endpoint, page, exc)
            break

        batch = data if isinstance(data, list) else (data.get("items") or [])
        items.extend(batch)

        if len(batch) < _PAGE_SIZE:
            break
        page += 1
        time.sleep(0.3)

    return items


# ── Data helpers ──────────────────────────────────────────────────────────────

def _cve_ids(aliases: list) -> list[str]:
    return [a.upper() for a in (aliases or []) if isinstance(a, str) and a.upper().startswith("CVE-")]


def _first_cve(aliases: list) -> str | None:
    ids = _cve_ids(aliases)
    return ids[0] if ids else None


def _parse_dt(s: str | None) -> datetime | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


# ── OpenSearch helpers ────────────────────────────────────────────────────────

def _get_os_client():
    try:
        from opensearchpy import OpenSearch
        url = os.environ.get("OPENSEARCH_URL", "http://opensearch:9200")
        return OpenSearch(hosts=[url], use_ssl=False, verify_certs=False, timeout=30)
    except ImportError:
        return None


def _ensure_euvd_index(client) -> None:
    if client.indices.exists(index=_OS_INDEX):
        return
    client.indices.create(index=_OS_INDEX, body={
        "settings": {"number_of_shards": 1, "number_of_replicas": 0},
        "mappings": {"properties": {
            "euvd_id":             {"type": "keyword"},
            "cve_id":              {"type": "keyword"},
            "cve_ids":             {"type": "keyword"},
            "description":         {"type": "text"},
            "date_published":      {"type": "date"},
            "date_updated":        {"type": "date"},
            "base_score":          {"type": "float"},
            "base_score_version":  {"type": "keyword"},
            "base_score_vector":   {"type": "keyword"},
            "epss_score":          {"type": "float"},
            "assigner":            {"type": "keyword"},
            "is_exploited":        {"type": "boolean"},
            "is_critical":         {"type": "boolean"},
            "aliases":             {"type": "keyword"},
            "vendors":             {"type": "keyword"},
            "products":            {"type": "keyword"},
            "indexed_at":          {"type": "date"},
        }},
    })
    logger.info("Created OpenSearch index: %s", _OS_INDEX)


def _sync_to_opensearch(entries: list[dict]) -> int:
    """Index EUVD entries to OpenSearch, then cross-enrich nvd-cve."""
    client = _get_os_client()
    if client is None:
        logger.warning("opensearch-py not available — skipping EUVD sync")
        return 0

    try:
        if not client.ping():
            logger.warning("OpenSearch unavailable — skipping EUVD sync")
            return 0
        _ensure_euvd_index(client)
    except Exception as exc:
        logger.warning("OpenSearch unavailable: %s", exc)
        return 0

    from opensearchpy import helpers as os_helpers

    now_iso = datetime.now(timezone.utc).isoformat()
    indexed = 0

    def _index_actions():
        for e in entries:
            yield {"_op_type": "index", "_index": _OS_INDEX, "_id": e["euvd_id"],
                   **e, "indexed_at": now_iso}

    try:
        for ok, info in os_helpers.streaming_bulk(
            client, _index_actions(), raise_on_error=False, chunk_size=500
        ):
            if ok:
                indexed += 1
            else:
                logger.debug("EUVD index error: %s", info)
    except Exception as exc:
        logger.warning("EUVD OpenSearch bulk error: %s", exc)

    logger.info("EUVD → OpenSearch euvd: %d indexed", indexed)

    _enrich_nvd_cve(client, entries)
    return indexed


def _enrich_nvd_cve(client, entries: list[dict]) -> None:
    """Bulk partial-update nvd-cve docs with in_euvd=True + euvd_id."""
    try:
        if not client.indices.exists(index=_NVD_INDEX):
            return
        client.indices.put_mapping(
            index=_NVD_INDEX,
            body={"properties": {
                "in_euvd":  {"type": "boolean"},
                "euvd_id":  {"type": "keyword"},
            }},
        )
    except Exception as exc:
        logger.warning("nvd-cve mapping update failed: %s", exc)
        return

    from opensearchpy import helpers as os_helpers

    # CVE → first EUVD ID mapping
    cve_to_euvd: dict[str, str] = {}
    for e in entries:
        for cve_id in (e.get("cve_ids") or []):
            if cve_id not in cve_to_euvd:
                cve_to_euvd[cve_id] = e["euvd_id"]

    if not cve_to_euvd:
        logger.info("EUVD → nvd-cve: no CVE aliases found, skipping enrichment")
        return

    def _update_actions():
        for cve_id, euvd_id in cve_to_euvd.items():
            yield {"_op_type": "update", "_index": _NVD_INDEX, "_id": cve_id,
                   "doc": {"in_euvd": True, "euvd_id": euvd_id}}

    updated = 0
    errors  = 0
    try:
        for ok, info in os_helpers.streaming_bulk(
            client, _update_actions(),
            raise_on_error=False, chunk_size=500, max_retries=2,
        ):
            if ok:
                updated += 1
            else:
                err = info.get("update", {}).get("error", {})
                if err.get("type") != "document_missing_exception":
                    logger.debug("EUVD → nvd-cve skip: %s", info)
                errors += 1
    except Exception as exc:
        logger.warning("EUVD → nvd-cve bulk error: %s", exc)

    logger.info("EUVD → nvd-cve enrichment: %d updated, %d not-found/skipped", updated, errors)


# ── Main run ──────────────────────────────────────────────────────────────────

def run() -> None:
    run_id = start_run("euvd")
    logger.info("ENISA EUVD pull started")

    logger.info("Fetching exploited vulnerabilities...")
    exploited = _paginate("exploitedvulnerabilities")
    logger.info("  → %d exploited entries", len(exploited))

    logger.info("Fetching critical vulnerabilities...")
    critical = _paginate("criticalvulnerabilities")
    logger.info("  → %d critical entries", len(critical))

    # Deduplicate on EUVD id, preserving both flags
    merged: dict[str, dict] = {}
    for item in exploited:
        eid = item.get("id") or ""
        if eid:
            merged[eid] = {**item, "_is_exploited": True, "_is_critical": False}
    for item in critical:
        eid = item.get("id") or ""
        if not eid:
            continue
        if eid in merged:
            merged[eid]["_is_critical"] = True
        else:
            merged[eid] = {**item, "_is_exploited": False, "_is_critical": True}

    if not merged:
        fail_run(run_id, "No EUVD entries fetched")
        return

    now      = datetime.now(timezone.utc)
    upserted = 0
    os_docs  = []

    with get_conn() as conn:
        with conn.cursor() as cur:
            for eid, item in merged.items():
                aliases      = item.get("aliases") or []
                cve_id       = _first_cve(aliases)
                all_cve_ids  = _cve_ids(aliases)
                description  = (item.get("description") or "")[:8000] or None
                date_pub     = _parse_dt(item.get("datePublished"))
                date_upd     = _parse_dt(item.get("dateUpdated"))
                base_score   = item.get("baseScore")
                base_ver     = (item.get("baseScoreVersion") or "")[:20] or None
                base_vec     = (item.get("baseScoreVector") or "")[:200] or None
                epss         = item.get("epss")
                assigner     = (item.get("assigner") or "")[:200] or None
                is_exploited = bool(item.get("_is_exploited"))
                is_critical  = bool(item.get("_is_critical"))
                vendors      = [v.get("name", "") for v in (item.get("enisaIdVendor") or []) if v.get("name")]
                products     = [p.get("name", "") for p in (item.get("enisaIdProduct") or []) if p.get("name")]

                cur.execute(
                    """
                    INSERT INTO euvd_vulnerabilities
                      (id, euvd_id, cve_id, description,
                       date_published, date_updated,
                       base_score, base_score_version, base_score_vector,
                       epss_score, assigner,
                       is_exploited, is_critical,
                       aliases, cve_ids, vendors, products,
                       created_at, updated_at)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                            %s::jsonb,%s::jsonb,%s::jsonb,%s::jsonb,
                            %s,%s)
                    ON CONFLICT (euvd_id) DO UPDATE SET
                      cve_id             = EXCLUDED.cve_id,
                      description        = EXCLUDED.description,
                      date_updated       = EXCLUDED.date_updated,
                      base_score         = EXCLUDED.base_score,
                      base_score_version = EXCLUDED.base_score_version,
                      base_score_vector  = EXCLUDED.base_score_vector,
                      epss_score         = EXCLUDED.epss_score,
                      assigner           = EXCLUDED.assigner,
                      is_exploited       = EXCLUDED.is_exploited OR euvd_vulnerabilities.is_exploited,
                      is_critical        = EXCLUDED.is_critical OR euvd_vulnerabilities.is_critical,
                      aliases            = EXCLUDED.aliases,
                      cve_ids            = EXCLUDED.cve_ids,
                      vendors            = EXCLUDED.vendors,
                      products           = EXCLUDED.products,
                      updated_at         = EXCLUDED.updated_at
                    """,
                    (
                        str(uuid4()), eid, cve_id, description,
                        date_pub, date_upd,
                        base_score, base_ver, base_vec,
                        epss, assigner,
                        is_exploited, is_critical,
                        json.dumps(aliases), json.dumps(all_cve_ids),
                        json.dumps(vendors), json.dumps(products),
                        now, now,
                    ),
                )
                upserted += 1

                os_docs.append({
                    "euvd_id":            eid,
                    "cve_id":             cve_id,
                    "cve_ids":            all_cve_ids,
                    "description":        description,
                    "date_published":     date_pub.isoformat() if date_pub else None,
                    "date_updated":       date_upd.isoformat() if date_upd else None,
                    "base_score":         base_score,
                    "base_score_version": base_ver,
                    "base_score_vector":  base_vec,
                    "epss_score":         epss,
                    "assigner":           assigner,
                    "is_exploited":       is_exploited,
                    "is_critical":        is_critical,
                    "aliases":            aliases,
                    "vendors":            vendors,
                    "products":           products,
                })

    _sync_to_opensearch(os_docs)

    finish_run(run_id, upserted)
    logger.info("ENISA EUVD completed: %d entries upserted", upserted)
