"""AlienVault OTX — community threat intelligence pulse feed.

Pulls subscribed pulses modified in the last OTX_IMPORT_DAYS days (first run,
default 90) or last 2 days (delta). Filters TLP WHITE + GREEN only. Extracts
per-indicator IOCs and attaches pulse-level adversary, malware family, and
MITRE ATT&CK technique metadata.

⚠ WARNING: setting OTX_IMPORT_DAYS to a large value (e.g. 365) on first run
   will pull a very large number of pulses and may take hours to complete.

Requires: OTX_API_KEY (free — register at otx.alienvault.com)
Schedule:  daily at 04:30 UTC
"""

import json
import logging
import os
import re
from datetime import datetime, timedelta, timezone
from uuid import uuid4

import requests

from feeds.base import (
    fail_run, finish_run, get_conn, get_os_client, has_successful_run,
    is_cancelled, os_bulk_upsert, start_run,
)

logger = logging.getLogger(__name__)

_API_BASE    = "https://otx.alienvault.com/api/v1"
_API_KEY     = os.environ.get("OTX_API_KEY", "")
_OS_INDEX    = "ti-alienvault"
_PAGE_SIZE   = 50
_IMPORT_DAYS = int(os.environ.get("OTX_IMPORT_DAYS", "90"))  # first-run depth

_OS_MAPPING = {
    "mappings": {
        "properties": {
            "ioc":         {"type": "keyword"},
            "ioc_type":    {"type": "keyword"},
            "pulse_name":  {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
            "adversary":   {"type": "keyword"},
            "industries":  {"type": "keyword"},
            "countries":   {"type": "keyword"},
            "malware":     {"type": "keyword"},
            "mitre_tids":  {"type": "keyword"},
            "tlp":         {"type": "keyword"},
            "first_seen":  {"type": "date"},
            "indexed_at":  {"type": "date"},
        }
    }
}

# OTX indicator type → our ioc_type
_TYPE_MAP = {
    "IPv4":           "ip",
    "IPv6":           "ip",
    "domain":         "domain",
    "hostname":       "domain",
    "URL":            "url",
    "URI":            "url",
    "FileHash-MD5":   "md5",
    "FileHash-SHA1":  "sha1",
    "FileHash-SHA256":"sha256",
    "email":          "email",
}

_SKIP_TLP = {"amber", "red"}

# Confidence proxy: TLP WHITE = lower trust (public, unvetted),
# TLP GREEN = community-verified. Named adversary adds context → +10, cap 75.
_TLP_CONFIDENCE = {"white": 40, "green": 60}


def _session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"X-OTX-API-KEY": _API_KEY, "Accept": "application/json"})
    return s


def _modified_since() -> str:
    """2-day delta on subsequent runs; OTX_IMPORT_DAYS on first run (default 90)."""
    days = 2 if has_successful_run("alienvault") else _IMPORT_DAYS
    if not has_successful_run("alienvault") and _IMPORT_DAYS > 90:
        logger.warning("OTX_IMPORT_DAYS=%d — large first-run window, expect long processing time", _IMPORT_DAYS)
    dt = datetime.now(timezone.utc) - timedelta(days=days)
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def _fetch_pulses(session: requests.Session, since: str) -> list[dict]:
    """Paginate through subscribed pulses modified since `since`."""
    url = f"{_API_BASE}/pulses/subscribed"
    params: dict = {"modified_since": since, "limit": _PAGE_SIZE}
    pulses: list[dict] = []

    while url:
        try:
            resp = session.get(url, params=params, timeout=60)
            if resp.status_code == 403:
                logger.warning("AlienVault OTX: API key rejected (403) — check OTX_API_KEY")
                return pulses
            resp.raise_for_status()
            data = resp.json()
        except Exception as exc:
            logger.error("AlienVault OTX: fetch page failed: %s", exc)
            break

        results = data.get("results") or []
        pulses.extend(results)
        logger.debug("AlienVault OTX: fetched %d pulses (total so far: %d)", len(results), len(pulses))

        next_url = data.get("next")
        url = next_url if next_url else None
        params = {}  # next URL already contains query string

        if not results:
            break

    return pulses


def _extract_iocs(pulse: dict) -> list[dict]:
    """Return list of normalised IOC dicts from a pulse."""
    tlp = (pulse.get("tlp") or "white").lower()
    if tlp in _SKIP_TLP:
        return []

    adversary   = (pulse.get("adversary") or "").strip()
    pulse_name  = (pulse.get("name") or "").strip()
    industries  = [i for i in (pulse.get("industries") or []) if i]
    countries   = [c for c in (pulse.get("targeted_countries") or []) if c]
    tlp_val     = tlp

    # Malware families — OTX returns either plain strings or {"display_name": ...} dicts
    family_slugs = []
    for mf in (pulse.get("malware_families") or []):
        name = mf if isinstance(mf, str) else (mf.get("display_name") or mf.get("id") or "") if isinstance(mf, dict) else ""
        name = name.strip()
        if name:
            family_slugs.append(re.sub(r"[^\w.-]", "_", name.lower()))

    # MITRE ATT&CK TIDs — OTX returns either {"id": "T1234"} dicts or plain strings
    mitre_tids = []
    for a in (pulse.get("attack_ids") or []):
        tid = a if isinstance(a, str) else (a.get("id") or "") if isinstance(a, dict) else ""
        if re.match(r"T\d{4}(?:\.\d{3})?$", str(tid)):
            mitre_tids.append(str(tid))

    actor_slugs = [re.sub(r"[^\w.-]", "_", adversary.lower())] if adversary else []

    # Confidence: TLP WHITE=40, GREEN=60; named adversary attribution adds +10 (cap 75)
    confidence = _TLP_CONFIDENCE.get(tlp, 40)
    if adversary:
        confidence = min(confidence + 10, 75)

    tags = []
    if adversary:
        tags.append(adversary)
    tags.extend(industries[:5])

    iocs = []
    for ind in (pulse.get("indicators") or []):
        our_type = _TYPE_MAP.get(ind.get("type", ""))
        if not our_type:
            continue
        value = (ind.get("indicator") or "").strip()[:2000]
        if not value:
            continue

        # Per-indicator expiration check
        exp = ind.get("expiration")
        if exp:
            try:
                exp_dt = datetime.fromisoformat(exp.replace("Z", "+00:00"))
                if exp_dt < datetime.now(timezone.utc):
                    continue
            except Exception:
                pass

        ind_created = ind.get("created") or ""
        try:
            fs = ind_created.replace("Z", "+00:00")
            first_seen = datetime.fromisoformat(fs) if fs else datetime.now(timezone.utc)
            if first_seen.tzinfo is None:
                first_seen = first_seen.replace(tzinfo=timezone.utc)
        except Exception:
            first_seen = datetime.now(timezone.utc)

        iocs.append({
            "ioc_type":     our_type,
            "value":        value,
            "first_seen":   first_seen,
            "confidence":   confidence,
            "tlp":          tlp_val,
            "tags":         tags,
            "mitre_tids":   mitre_tids,
            "family_slugs": family_slugs,
            "actor_slugs":  actor_slugs,
            "pulse_name":   pulse_name,
            "adversary":    adversary,
            "industries":   industries,
            "countries":    countries,
        })

    return iocs


def run() -> None:
    if not _API_KEY:
        logger.warning("OTX_API_KEY not set — AlienVault OTX feed disabled")
        run_id = start_run("alienvault")
        finish_run(run_id, 0)
        return

    run_id = start_run("alienvault")
    since  = _modified_since()
    logger.info("AlienVault OTX pull started (modified_since=%s)", since)

    session = _session()
    try:
        pulses = _fetch_pulses(session, since)
    except Exception as exc:
        fail_run(run_id, str(exc))
        logger.error("AlienVault OTX: pulse fetch failed: %s", exc)
        return

    if not pulses:
        finish_run(run_id, 0)
        logger.info("AlienVault OTX: no pulses in window")
        return

    logger.info("AlienVault OTX: processing %d pulses", len(pulses))

    now      = datetime.now(timezone.utc)
    now_iso  = now.isoformat()
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

    with get_conn() as conn:
        with conn.cursor() as cur:
            for pulse in pulses:
                if is_cancelled("alienvault"):
                    logger.info("AlienVault OTX cancelled at %d IOCs", upserted)
                    fail_run(run_id, "Cancelled by user")
                    return

                for ioc in _extract_iocs(pulse):
                    cur.execute(
                        """
                        INSERT INTO ti_iocs
                          (id, ioc_type, value, source, confidence, tlp, tags, mitre_tids,
                           family_slugs, actor_slugs, event_uuids, first_seen, last_seen, created_at, raw)
                        VALUES (%s,%s,%s,'alienvault',%s,%s,%s,%s,%s,%s,'[]'::jsonb,%s,%s,%s,%s)
                        ON CONFLICT (ioc_type, value, source) DO UPDATE SET
                          confidence   = EXCLUDED.confidence,
                          tlp          = COALESCE(ti_iocs.tlp, EXCLUDED.tlp),
                          tags         = COALESCE((
                              SELECT jsonb_agg(DISTINCT elem)
                              FROM jsonb_array_elements(ti_iocs.tags || EXCLUDED.tags) elem
                          ), '[]'::jsonb),
                          mitre_tids   = COALESCE((
                              SELECT jsonb_agg(DISTINCT elem)
                              FROM jsonb_array_elements(ti_iocs.mitre_tids || EXCLUDED.mitre_tids) elem
                          ), '[]'::jsonb),
                          family_slugs = COALESCE((
                              SELECT jsonb_agg(DISTINCT elem)
                              FROM jsonb_array_elements(ti_iocs.family_slugs || EXCLUDED.family_slugs) elem
                          ), '[]'::jsonb),
                          actor_slugs  = COALESCE((
                              SELECT jsonb_agg(DISTINCT elem)
                              FROM jsonb_array_elements(ti_iocs.actor_slugs || EXCLUDED.actor_slugs) elem
                          ), '[]'::jsonb),
                          last_seen    = GREATEST(ti_iocs.last_seen, EXCLUDED.last_seen)
                        """,
                        (
                            str(uuid4()),
                            ioc["ioc_type"], ioc["value"],
                            ioc["confidence"],
                            ioc["tlp"],
                            json.dumps(ioc["tags"]),
                            json.dumps(ioc["mitre_tids"]),
                            json.dumps(ioc["family_slugs"]),
                            json.dumps(ioc["actor_slugs"]),
                            ioc["first_seen"], now, now,
                            json.dumps({
                                "pulse_name": ioc["pulse_name"],
                                "adversary":  ioc["adversary"],
                            }),
                        ),
                    )
                    upserted += 1

                    os_docs.append({
                        "ioc":        ioc["value"],
                        "ioc_type":   ioc["ioc_type"],
                        "pulse_name": ioc["pulse_name"],
                        "adversary":  ioc["adversary"],
                        "industries": ioc["industries"],
                        "countries":  ioc["countries"],
                        "malware":    ioc["family_slugs"],
                        "mitre_tids": ioc["mitre_tids"],
                        "tlp":        ioc["tlp"],
                        "first_seen": ioc["first_seen"].isoformat(),
                        "indexed_at": now_iso,
                        "_os_id":     f"alienvault:{ioc['ioc_type']}:{ioc['value'][:400]}",
                    })

                    if len(os_docs) >= 1000 and os_client:
                        os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")
                        os_docs = []

    if os_docs and os_client:
        os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")

    finish_run(run_id, upserted)
    logger.info("AlienVault OTX completed: %d IOCs upserted (%d pulses)", upserted, len(pulses))
