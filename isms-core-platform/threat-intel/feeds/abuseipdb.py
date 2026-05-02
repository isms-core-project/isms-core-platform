"""AbuseIPDB feed — two functions:

  run_blacklist(): daily pull of top abusive IPs → ti_iocs + ti-abuseipdb-blacklist
  enrich_ip(ip):  on-demand single-IP check → cached in ti_enrichment_cache (24h TTL)
"""

import logging
import os
from datetime import datetime, timedelta, timezone
from uuid import uuid4

import requests

from feeds import ipinfo, maxmind
from feeds.base import fail_run, finish_run, get_conn, get_os_client, is_cancelled, os_bulk_upsert, start_run

logger = logging.getLogger(__name__)

_API_BASE = "https://api.abuseipdb.com/api/v2"
_OS_INDEX = "ti-abuseipdb-blacklist"

_OS_MAPPING = {
    "mappings": {
        "properties": {
            "ip":               {"type": "ip"},
            "abuse_score":      {"type": "integer"},
            "country_code":     {"type": "keyword"},
            "isp":              {"type": "keyword"},
            "usage_type":       {"type": "keyword"},
            "categories":       {"type": "integer"},
            "total_reports":    {"type": "integer"},
            "last_reported_at": {"type": "date"},
            "indexed_at":       {"type": "date"},
            # MaxMind GeoLite2 enrichment (free tier: country, city, ASN only)
            "geo_country":  {"type": "keyword"},
            "geo_city":     {"type": "keyword"},
            "geo_lat":      {"type": "float"},
            "geo_lon":      {"type": "float"},
            "geo_location": {"type": "geo_point"},
            "geo_asn":      {"type": "integer"},
            "geo_org":      {"type": "keyword"},
            # IPInfo privacy enrichment
            "privacy_label":    {"type": "keyword"},
            "privacy_is_vpn":   {"type": "boolean"},
            "privacy_is_proxy": {"type": "boolean"},
            "privacy_is_tor":   {"type": "boolean"},
            "privacy_is_hosting": {"type": "boolean"},
        }
    }
}


def _api_key() -> str | None:
    return os.environ.get("ABUSEIPDB_API_KEY") or None


def _headers() -> dict:
    return {"Key": _api_key(), "Accept": "application/json"}


def run_blacklist() -> None:
    key = _api_key()
    if not key:
        logger.warning("AbuseIPDB blacklist skipped: ABUSEIPDB_API_KEY not set")
        return

    run_id = start_run("abuseipdb_blacklist")
    logger.info("AbuseIPDB blacklist pull started")

    try:
        resp = requests.get(
            f"{_API_BASE}/blacklist",
            headers=_headers(),
            params={"confidenceMinimum": 100, "limit": 10000},
            timeout=120,
        )
        if resp.status_code == 429:
            # Free tier allows one blacklist pull per 24h — skip gracefully
            finish_run(run_id, 0)
            logger.warning("AbuseIPDB blacklist rate-limited (429) — daily limit reached, will retry at next scheduled run")
            return
        resp.raise_for_status()
        data = resp.json()
    except Exception as exc:
        fail_run(run_id, str(exc))
        logger.error("AbuseIPDB blacklist download failed: %s", exc)
        return

    entries = data.get("data") or []
    if not entries:
        fail_run(run_id, "Empty blacklist response")
        return

    now = datetime.now(timezone.utc)
    now_iso = now.isoformat()
    upserted = 0
    os_docs: list[dict] = []

    os_client = get_os_client()
    if os_client:
        try:
            if not os_client.indices.exists(index=_OS_INDEX):
                os_client.indices.create(index=_OS_INDEX, body=_OS_MAPPING)
                logger.info("Created OpenSearch index: %s", _OS_INDEX)
        except Exception as exc:
            logger.warning("OpenSearch index setup failed: %s", exc)
            os_client = None

    # ── Step 1: write IOCs to Postgres immediately — does NOT depend on enrichment ──
    import json as _json
    with get_conn() as conn:
        with conn.cursor() as cur:
            for entry in entries:
                if is_cancelled("abuseipdb_blacklist"):
                    logger.info("AbuseIPDB blacklist cancelled at %d entries", upserted)
                    fail_run(run_id, "Cancelled by user")
                    return
                ip = (entry.get("ipAddress") or "").strip()
                if not ip:
                    continue
                score = entry.get("abuseConfidenceScore") or 0
                country = (entry.get("countryCode") or "")[:5]
                isp = (entry.get("isp") or "")[:255]

                cur.execute(
                    """
                    INSERT INTO ti_iocs
                      (id, ioc_type, value, source, confidence, tags, mitre_tids,
                       family_slugs, actor_slugs, event_uuids, first_seen, last_seen, created_at,
                       raw)
                    VALUES (%s,'ip',%s,'abuseipdb',%s,'[]'::jsonb,'[]'::jsonb,'[]'::jsonb,'[]'::jsonb,'[]'::jsonb,%s,%s,%s,%s)
                    ON CONFLICT (ioc_type, value, source) DO UPDATE SET
                      confidence = EXCLUDED.confidence,
                      last_seen  = EXCLUDED.last_seen,
                      raw        = EXCLUDED.raw
                    """,
                    (
                        str(uuid4()), ip, score,
                        now, now, now,
                        _json.dumps({
                            "country": country, "isp": isp,
                            "totalReports": entry.get("totalReports"),
                            "lastReportedAt": entry.get("lastReportedAt"),
                        }),
                    ),
                )
                upserted += 1
                os_docs.append({
                    "ip":               ip,
                    "abuse_score":      score,
                    "country_code":     country,
                    "isp":              isp,
                    "usage_type":       entry.get("usageType"),
                    "categories":       entry.get("categories", []),
                    "total_reports":    entry.get("totalReports"),
                    "last_reported_at": entry.get("lastReportedAt"),
                    "indexed_at":       now_iso,
                    "_os_id":           f"abuseipdb:{ip}",
                })

    # Postgres data is safe — mark the run complete now so a slow enrichment
    # cannot waste the AbuseIPDB daily blacklist pull if it hangs.
    finish_run(run_id, upserted)
    logger.info("AbuseIPDB blacklist completed: %d IPs upserted", upserted)

    # ── Step 2: best-effort geo + privacy enrichment → OpenSearch only ──────────
    # Enrichment is a separate concern; failures here do not affect Postgres IOCs.
    if os_docs and os_client:
        all_ips = [doc["ip"] for doc in os_docs]
        geo_data     = maxmind.enrich_batch(all_ips)
        privacy_data = ipinfo.enrich_batch(all_ips)

        for doc in os_docs:
            ip      = doc["ip"]
            geo     = geo_data.get(ip) or {}
            privacy = privacy_data.get(ip) or {}
            doc.update({
                "geo_country":  geo.get("country_code"),
                "geo_city":     geo.get("city"),
                "geo_lat":      geo.get("latitude"),
                "geo_lon":      geo.get("longitude"),
                "geo_location": (
                    {"lat": geo["latitude"], "lon": geo["longitude"]}
                    if geo.get("latitude") is not None and geo.get("longitude") is not None
                    else None
                ),
                "geo_asn":      geo.get("asn"),
                "geo_org":      geo.get("asn_org"),
                "privacy_label":      privacy.get("privacy_label"),
                "privacy_is_vpn":     privacy.get("is_vpn"),
                "privacy_is_proxy":   privacy.get("is_proxy"),
                "privacy_is_tor":     privacy.get("is_tor"),
                "privacy_is_hosting": privacy.get("is_hosting"),
            })

        os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")


def enrich_ip(ip: str) -> dict | None:
    """
    Look up a single IP via AbuseIPDB Check endpoint.
    Returns cached result if < 24h old. Returns None if API key missing or error.
    """
    key = _api_key()
    if not key:
        return None

    # Check cache first
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT abuseipdb, cached_at FROM ti_enrichment_cache WHERE ip = %s",
                    (ip,),
                )
                row = cur.fetchone()
                if row and row[0]:
                    cached_at = row[1]
                    if cached_at and (datetime.now(timezone.utc) - cached_at) < timedelta(hours=24):
                        return row[0]
    except Exception as exc:
        logger.warning("Cache read failed for %s: %s", ip, exc)

    # Fetch from API
    try:
        resp = requests.get(
            f"{_API_BASE}/check",
            headers=_headers(),
            params={"ipAddress": ip, "maxAgeInDays": 90, "verbose": True},
            timeout=15,
        )
        resp.raise_for_status()
        result = resp.json().get("data") or {}
    except Exception as exc:
        logger.warning("AbuseIPDB check failed for %s: %s", ip, exc)
        return None

    # Store in cache
    now = datetime.now(timezone.utc)
    try:
        import json
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO ti_enrichment_cache (ip, abuseipdb, cached_at)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (ip) DO UPDATE SET abuseipdb = EXCLUDED.abuseipdb, cached_at = EXCLUDED.cached_at
                    """,
                    (ip, json.dumps(result), now),
                )
    except Exception as exc:
        logger.warning("Cache write failed for %s: %s", ip, exc)

    return result
