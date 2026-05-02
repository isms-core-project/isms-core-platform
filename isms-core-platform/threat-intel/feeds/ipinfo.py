"""IPInfo — batch IP privacy enricher.

Returns per IP: privacy flags (vpn/proxy/tor/relay/hosting) and a single label.
Cached in ti_enrichment_cache.ipinfo (30-day TTL, per-enricher timestamp).
"""

import json
import logging
import os
import time
from datetime import datetime, timedelta, timezone

import requests

from feeds.base import get_conn

logger = logging.getLogger(__name__)

_TTL_DAYS = 30
_MAX_WALL_SECONDS = 120  # hard time budget per enrichment call
_session: requests.Session | None = None


def _api_key() -> str | None:
    return os.environ.get("IPINFO_API_KEY") or None


def _get_session() -> requests.Session:
    global _session
    if _session is None:
        _session = requests.Session()
    return _session


def _privacy_label(p: dict) -> str:
    """Single most-significant privacy classification for pie charts."""
    if p.get("tor"):     return "Tor"
    if p.get("vpn"):     return "VPN"
    if p.get("proxy"):   return "Proxy"
    if p.get("relay"):   return "Relay"
    if p.get("hosting"): return "Hosting"
    return "Clean"


def _fetch_one(ip: str, api_key: str) -> dict:
    resp = _get_session().get(
        f"https://ipinfo.io/{ip}/json",
        params={"token": api_key},
        timeout=10,
    )
    if resp.status_code == 404:
        return {"privacy_label": "Clean", "is_vpn": False, "is_proxy": False, "is_tor": False, "is_hosting": False}
    resp.raise_for_status()
    data = resp.json()
    p = data.get("privacy") or {}
    return {
        "privacy_label": _privacy_label(p),
        "is_vpn":        bool(p.get("vpn")),
        "is_proxy":      bool(p.get("proxy")),
        "is_tor":        bool(p.get("tor")),
        "is_relay":      bool(p.get("relay")),
        "is_hosting":    bool(p.get("hosting")),
        "service":       p.get("service") or "",
    }


def enrich_batch(ips: list[str]) -> dict[str, dict]:
    """
    Enrich a list of IPs with IPInfo privacy data.
    Returns {ip: result_dict}. IPs that error are omitted from the result.
    """
    api_key = _api_key()
    if not api_key or not ips:
        if not api_key:
            logger.debug("IPInfo skipped: IPINFO_API_KEY not set")
        return {}

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=_TTL_DAYS)
    result: dict[str, dict] = {}
    to_fetch: list[str] = []

    # Load cache for all IPs in one query
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT ip, ipinfo, ipinfo_cached_at FROM ti_enrichment_cache WHERE ip = ANY(%s)",
                    (ips,),
                )
                cached_ips: set[str] = set()
                for ip, data, cached_at in cur.fetchall():
                    cached_ips.add(ip)
                    if data is not None and cached_at and cached_at > cutoff:
                        result[ip] = data
                    else:
                        to_fetch.append(ip)
                for ip in ips:
                    if ip not in cached_ips:
                        to_fetch.append(ip)
    except Exception as exc:
        logger.warning("IPInfo cache read failed: %s", exc)
        to_fetch = list(ips)

    if not to_fetch:
        return result

    logger.info("IPInfo: fetching %d IPs (%d from cache)", len(to_fetch), len(result))

    fetched: dict[str, dict] = {}
    deadline = time.monotonic() + _MAX_WALL_SECONDS
    skipped = 0
    for ip in to_fetch:
        if time.monotonic() > deadline:
            skipped += 1
            continue
        try:
            fetched[ip] = _fetch_one(ip, api_key)
            result[ip] = fetched[ip]
        except Exception as exc:
            logger.debug("IPInfo fetch failed for %s: %s", ip, exc)

    if skipped:
        logger.info("IPInfo: time budget (%ds) reached — skipped %d IPs (will retry on next run)",
                    _MAX_WALL_SECONDS, skipped)

    if not fetched:
        return result

    # Batch update cache — only touch ipinfo + ipinfo_cached_at, leave other enrichers untouched
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                for ip, data in fetched.items():
                    cur.execute(
                        """
                        INSERT INTO ti_enrichment_cache (ip, ipinfo, ipinfo_cached_at, cached_at)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (ip) DO UPDATE
                          SET ipinfo           = EXCLUDED.ipinfo,
                              ipinfo_cached_at = EXCLUDED.ipinfo_cached_at
                        """,
                        (ip, json.dumps(data), now, now),
                    )
    except Exception as exc:
        logger.warning("IPInfo cache write failed: %s", exc)

    return result
