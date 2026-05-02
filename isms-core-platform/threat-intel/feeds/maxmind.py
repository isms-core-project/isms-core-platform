"""MaxMind GeoLite2 MMDB — batch IP geolocation enricher.

Downloads GeoLite2-City, GeoLite2-Country and GeoLite2-ASN MMDB files
from MaxMind on startup (if missing) and on the weekly Tuesday refresh.
Files are stored in _TI_DATA_DIR (/data/ti by default — Docker named volume).

Requires: MAXMIND_ACCOUNT_ID + MAXMIND_LICENSE_KEY (used for authenticated download).
Results cached in ti_enrichment_cache.maxmind (30-day TTL).
"""

import io
import json
import logging
import os
import tarfile
import time
from datetime import datetime, timedelta, timezone

import geoip2.database
import geoip2.errors
import requests

from feeds.base import get_conn

logger = logging.getLogger(__name__)

_TTL_DAYS      = 30
_TI_DATA_DIR   = os.environ.get("TI_DATA_DIR", "/data/ti")
_CITY_MMDB     = os.path.join(_TI_DATA_DIR, "GeoLite2-City.mmdb")
_ASN_MMDB      = os.path.join(_TI_DATA_DIR, "GeoLite2-ASN.mmdb")
_COUNTRY_MMDB  = os.path.join(_TI_DATA_DIR, "GeoLite2-Country.mmdb")
_DOWNLOAD_BASE = "https://download.maxmind.com/geoip/databases/{edition}/download?suffix=tar.gz"

_city_reader:    "geoip2.database.Reader | None" = None
_asn_reader:     "geoip2.database.Reader | None" = None
_country_reader: "geoip2.database.Reader | None" = None


def _account_id() -> int | None:
    val = os.environ.get("MAXMIND_ACCOUNT_ID")
    try:
        return int(val) if val else None
    except ValueError:
        return None


def _license_key() -> str | None:
    return os.environ.get("MAXMIND_LICENSE_KEY") or None


def _download_mmdb(edition: str, dest: str, account_id: int, license_key: str) -> bool:
    """Download one GeoLite2 edition (tar.gz), extract the .mmdb, write atomically."""
    url = _DOWNLOAD_BASE.format(edition=edition)
    try:
        resp = requests.get(
            url, auth=(str(account_id), license_key),
            timeout=180, stream=True,
        )
        resp.raise_for_status()
        buf = io.BytesIO()
        for chunk in resp.iter_content(chunk_size=1024 * 1024):
            buf.write(chunk)
        buf.seek(0)
        with tarfile.open(fileobj=buf, mode="r:gz") as tar:
            for member in tar.getmembers():
                if member.name.endswith(".mmdb"):
                    f = tar.extractfile(member)
                    if f:
                        tmp = dest + ".tmp"
                        with open(tmp, "wb") as out:
                            out.write(f.read())
                        os.replace(tmp, dest)
                        return True
        logger.warning("MaxMind: no .mmdb found in %s tarball", edition)
    except Exception as exc:
        logger.error("MaxMind: download failed for %s: %s", edition, exc)
    return False


def _download_all() -> None:
    account_id = _account_id()
    license_key = _license_key()
    if not account_id or not license_key:
        logger.debug("MaxMind: MMDB download skipped — MAXMIND_ACCOUNT_ID / MAXMIND_LICENSE_KEY not set")
        return
    os.makedirs(_TI_DATA_DIR, exist_ok=True)
    for edition, dest in [
        ("GeoLite2-City",    _CITY_MMDB),
        ("GeoLite2-ASN",     _ASN_MMDB),
        ("GeoLite2-Country", _COUNTRY_MMDB),
    ]:
        if _download_mmdb(edition, dest, account_id, license_key):
            logger.info("MaxMind: downloaded %s → %s", edition, dest)
        else:
            logger.warning("MaxMind: %s download failed — enrichment will be partial", edition)


def _reload_readers() -> None:
    global _city_reader, _asn_reader, _country_reader
    for path, name in ((_CITY_MMDB, "City"), (_ASN_MMDB, "ASN"), (_COUNTRY_MMDB, "Country")):
        if not os.path.exists(path):
            continue
        try:
            reader = geoip2.database.Reader(path)
            if name == "City":
                _city_reader = reader
            elif name == "ASN":
                _asn_reader = reader
            else:
                _country_reader = reader
            logger.info("MaxMind: loaded %s MMDB from %s", name, path)
        except Exception as exc:
            logger.error("MaxMind: failed to open %s MMDB: %s", name, exc)


def ensure_mmdb() -> None:
    """Download MMDB files if missing, then open readers. Called at scheduler startup."""
    missing = not os.path.exists(_CITY_MMDB) or not os.path.exists(_ASN_MMDB)
    if missing:
        logger.info("MaxMind: MMDB files missing — downloading now")
        _download_all()
    else:
        logger.info("MaxMind: MMDB files found at %s", _TI_DATA_DIR)
    _reload_readers()


def refresh_mmdb() -> None:
    """Force-download latest MMDB files. Called weekly by scheduler (Tuesdays)."""
    logger.info("MaxMind: weekly MMDB refresh starting")
    _download_all()
    _reload_readers()


def _fetch_one(ip: str) -> dict:
    result: dict = {}
    if _city_reader:
        try:
            r = _city_reader.city(ip)
            result.update({
                "country_code": r.country.iso_code,
                "country_name": r.country.name,
                "city":         r.city.name,
                "latitude":     r.location.latitude,
                "longitude":    r.location.longitude,
            })
        except geoip2.errors.AddressNotFoundError:
            pass
    if _asn_reader:
        try:
            a = _asn_reader.asn(ip)
            result.update({
                "asn":     a.autonomous_system_number,
                "asn_org": a.autonomous_system_organization,
            })
        except geoip2.errors.AddressNotFoundError:
            pass
    return result


def enrich_batch(ips: list[str]) -> dict[str, dict]:
    """
    Enrich a list of IPs with MaxMind GeoLite2 geo + ASN data.
    Returns {ip: result_dict}. IPs not found return {}.
    """
    if not _city_reader and not _asn_reader:
        logger.debug("MaxMind skipped: no MMDB readers loaded")
        return {}
    if not ips:
        return {}

    now    = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=_TTL_DAYS)
    result: dict[str, dict] = {}
    to_fetch: list[str] = []

    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT ip, maxmind, maxmind_cached_at FROM ti_enrichment_cache WHERE ip = ANY(%s)",
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
        logger.warning("MaxMind cache read failed: %s", exc)
        to_fetch = list(ips)

    if not to_fetch:
        return result

    logger.info("MaxMind: enriching %d IPs (%d from cache)", len(to_fetch), len(result))

    fetched: dict[str, dict] = {}
    for ip in to_fetch:
        data = _fetch_one(ip)
        fetched[ip] = data
        result[ip] = data

    if not fetched:
        return result

    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                for ip, data in fetched.items():
                    cur.execute(
                        """
                        INSERT INTO ti_enrichment_cache (ip, maxmind, maxmind_cached_at, cached_at)
                        VALUES (%s, %s, %s, %s)
                        ON CONFLICT (ip) DO UPDATE
                          SET maxmind           = EXCLUDED.maxmind,
                              maxmind_cached_at = EXCLUDED.maxmind_cached_at
                        """,
                        (ip, json.dumps(data), now, now),
                    )
    except Exception as exc:
        logger.warning("MaxMind cache write failed: %s", exc)

    return result
