"""Shodan enrichment — two paths:

  enrich_ip_paid(ip):    Shodan Host API (requires SHODAN_API_KEY)
  enrich_ip_internetdb(ip): Shodan InternetDB (free, no key)

The enrichment endpoint in the backend calls enrich_ip() which tries paid first,
falls back to InternetDB if no key is configured. Results are cached 24h in
ti_enrichment_cache.shodan.
"""

import json
import logging
import os
from datetime import datetime, timedelta, timezone

import requests

from feeds.base import get_conn

logger = logging.getLogger(__name__)

_SHODAN_HOST_URL = "https://api.shodan.io/shodan/host/{ip}?key={key}"
_INTERNETDB_URL  = "https://internetdb.shodan.io/{ip}"


def _api_key() -> str | None:
    return os.environ.get("SHODAN_API_KEY") or None


def _get_cache(ip: str) -> dict | None:
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT shodan, cached_at FROM ti_enrichment_cache WHERE ip = %s",
                    (ip,),
                )
                row = cur.fetchone()
                if row and row[0]:
                    cached_at = row[1]
                    if cached_at and (datetime.now(timezone.utc) - cached_at) < timedelta(hours=24):
                        return row[0]
    except Exception as exc:
        logger.warning("Shodan cache read failed for %s: %s", ip, exc)
    return None


def _set_cache(ip: str, data: dict) -> None:
    now = datetime.now(timezone.utc)
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO ti_enrichment_cache (ip, shodan, cached_at)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (ip) DO UPDATE SET shodan = EXCLUDED.shodan, cached_at = EXCLUDED.cached_at
                    """,
                    (ip, json.dumps(data), now),
                )
    except Exception as exc:
        logger.warning("Shodan cache write failed for %s: %s", ip, exc)


def enrich_ip_paid(ip: str) -> dict | None:
    key = _api_key()
    if not key:
        return None
    try:
        resp = requests.get(
            _SHODAN_HOST_URL.format(ip=ip, key=key),
            timeout=15,
        )
        if resp.status_code == 404:
            return {}   # IP not in Shodan — valid empty result
        resp.raise_for_status()
        raw = resp.json()
        return {
            "source":    "shodan_api",
            "ip":        ip,
            "ports":     raw.get("ports", []),
            "hostnames": raw.get("hostnames", []),
            "org":       raw.get("org"),
            "asn":       raw.get("asn"),
            "country":   raw.get("country_code"),
            "cves":      list(raw.get("vulns", {}).keys()),
            "last_update": raw.get("last_update"),
            "tags":      raw.get("tags", []),
        }
    except Exception as exc:
        logger.warning("Shodan API enrichment failed for %s: %s", ip, exc)
        return None


def enrich_ip_internetdb(ip: str) -> dict | None:
    """InternetDB returns ports, hostnames, CPEs, tags, and CVE list — no key needed."""
    try:
        resp = requests.get(_INTERNETDB_URL.format(ip=ip), timeout=10)
        if resp.status_code == 404:
            return {}
        resp.raise_for_status()
        raw = resp.json()
        return {
            "source":    "shodan_internetdb",
            "ip":        ip,
            "ports":     raw.get("ports", []),
            "hostnames": raw.get("hostnames", []),
            "cpes":      raw.get("cpes", []),
            "cves":      raw.get("vulns", []),
            "tags":      raw.get("tags", []),
        }
    except Exception as exc:
        logger.warning("Shodan InternetDB failed for %s: %s", ip, exc)
        return None


def enrich_ip(ip: str) -> dict | None:
    """
    Returns Shodan enrichment for ip.
    Tries paid API first (if SHODAN_API_KEY set), falls back to InternetDB.
    Result cached 24h. Returns None on total failure.
    """
    cached = _get_cache(ip)
    if cached is not None:
        return cached

    result = enrich_ip_paid(ip)
    if result is None:
        result = enrich_ip_internetdb(ip)

    if result is not None:
        _set_cache(ip, result)

    return result
