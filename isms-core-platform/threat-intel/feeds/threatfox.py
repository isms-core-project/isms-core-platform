"""Abuse.ch ThreatFox feed — C2 and malware IOCs with family attribution.

Source: https://threatfox-api.abuse.ch/api/v1/
Pull schedule: every 6 hours. No API key required.

Delta logic: first run fetches 30 days; subsequent runs fetch 1 day.
ThreatFox malware field (e.g. "win.cobalt_strike") maps directly to family_slugs.
"""

import json
import logging
import os
import re
from datetime import datetime, timezone
from uuid import uuid4

import requests

from feeds.base import (
    fail_run, finish_run, get_conn, get_os_client, has_successful_run,
    is_cancelled, os_bulk_upsert, start_run,
)

logger = logging.getLogger(__name__)

_API_URL  = "https://threatfox-api.abuse.ch/api/v1/"
_API_KEY  = os.environ.get("TI_THREATFOX_API_KEY", "")
_OS_INDEX = "ti-threatfox"

_OS_MAPPING = {
    "mappings": {
        "properties": {
            "ioc":         {"type": "keyword"},
            "ioc_type":    {"type": "keyword"},
            "threat_type": {"type": "keyword"},
            "malware":     {"type": "keyword"},
            "confidence":  {"type": "integer"},
            "tags":        {"type": "keyword"},
            "first_seen":  {"type": "date"},
            "indexed_at":  {"type": "date"},
        }
    }
}

# ThreatFox ioc_type → our ioc_type
_TYPE_MAP = {
    "ip:port":     "ip",
    "domain":      "domain",
    "url":         "url",
    "md5_hash":    "md5",
    "sha256_hash": "sha256",
}


def run() -> None:
    if not _API_KEY:
        logger.warning("TI_THREATFOX_API_KEY not set — ThreatFox feed disabled")
        run_id = start_run("threatfox")
        finish_run(run_id, 0)
        return

    run_id = start_run("threatfox")
    days = 1 if has_successful_run("threatfox") else 7
    logger.info("ThreatFox pull started (%d-day window)", days)

    try:
        resp = requests.post(
            _API_URL,
            json={"query": "get_iocs", "days": days},
            headers={"Content-Type": "application/json", "Auth-Key": _API_KEY},
            timeout=60,
        )
        if resp.status_code == 401:
            finish_run(run_id, 0)
            logger.warning("ThreatFox: API key rejected (401) — fix TI_THREATFOX_API_KEY at threatfox.abuse.ch then trigger manually")
            return
        resp.raise_for_status()
        data = resp.json()
    except Exception as exc:
        fail_run(run_id, str(exc))
        logger.error("ThreatFox fetch failed: %s", exc)
        return

    if data.get("query_status") != "ok":
        status = data.get("query_status")
        if status == "unauthorized":
            finish_run(run_id, 0)
            logger.warning("ThreatFox: API key rejected — fix TI_THREATFOX_API_KEY at auth.abuse.ch then trigger manually")
            return
        if status == "no_results":
            finish_run(run_id, 0)
            logger.info("ThreatFox: no IOCs for requested window")
            return
        fail_run(run_id, f"ThreatFox API error: {status}")
        return

    iocs = data.get("data") or []
    if not iocs:
        finish_run(run_id, 0)
        logger.info("ThreatFox: no IOCs for %d-day window", days)
        return

    now     = datetime.now(timezone.utc)
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

    with get_conn() as conn:
        with conn.cursor() as cur:
            for entry in iocs:
                if is_cancelled("threatfox"):
                    logger.info("ThreatFox cancelled at %d entries", upserted)
                    fail_run(run_id, "Cancelled by user")
                    return

                tf_type  = entry.get("ioc_type", "")
                our_type = _TYPE_MAP.get(tf_type)
                if not our_type:
                    continue

                raw_ioc = (entry.get("ioc") or "").strip()
                if not raw_ioc:
                    continue

                # ip:port → strip port
                value = raw_ioc.split(":")[0] if tf_type == "ip:port" else raw_ioc
                value = value.strip()[:2000]
                if not value:
                    continue

                confidence  = entry.get("confidence_level") or None
                malware     = (entry.get("malware") or "").strip()   # e.g. "win.cobalt_strike"
                threat_type = (entry.get("threat_type") or "").strip()
                tags        = [t for t in (entry.get("tags") or []) if t]
                first_seen_s = entry.get("first_seen") or ""

                # Pull TIDs from any tag that looks like T1234 or T1234.001
                mitre_tids: list[str] = []
                for t in tags:
                    mitre_tids.extend(re.findall(r"T\d{4}(?:\.\d{3})?", str(t)))
                mitre_tids = list(dict.fromkeys(mitre_tids))

                family_slugs = [malware] if malware else []

                try:
                    fs = first_seen_s.replace(" ", "T").replace("Z", "+00:00")
                    first_seen = datetime.fromisoformat(fs) if fs else now
                    if first_seen.tzinfo is None:
                        first_seen = first_seen.replace(tzinfo=timezone.utc)
                except Exception:
                    first_seen = now

                all_tags = tags + ([threat_type] if threat_type else [])

                cur.execute(
                    """
                    INSERT INTO ti_iocs
                      (id, ioc_type, value, source, confidence, tags, mitre_tids,
                       family_slugs, actor_slugs, event_uuids, first_seen, last_seen, created_at, raw)
                    VALUES (%s,%s,%s,'threatfox',%s,%s,%s,%s,'[]'::jsonb,'[]'::jsonb,%s,%s,%s,%s)
                    ON CONFLICT (ioc_type, value, source) DO UPDATE SET
                      confidence   = EXCLUDED.confidence,
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
                      last_seen    = GREATEST(ti_iocs.last_seen, EXCLUDED.last_seen)
                    """,
                    (
                        str(uuid4()), our_type, value,
                        confidence,
                        json.dumps(all_tags),
                        json.dumps(mitre_tids),
                        json.dumps(family_slugs),
                        first_seen, now, now,
                        json.dumps({"ioc_type": tf_type, "threat_type": threat_type, "malware": malware}),
                    ),
                )
                upserted += 1

                os_docs.append({
                    "ioc":         raw_ioc,
                    "ioc_type":    our_type,
                    "threat_type": threat_type,
                    "malware":     malware,
                    "confidence":  confidence,
                    "tags":        tags,
                    "first_seen":  first_seen.isoformat(),
                    "indexed_at":  now_iso,
                    "_os_id":      f"threatfox:{our_type}:{value[:400]}",
                })

                if len(os_docs) >= 1000 and os_client:
                    os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")
                    os_docs = []

    if os_docs and os_client:
        os_bulk_upsert(os_client, _OS_INDEX, os_docs, "_os_id")

    finish_run(run_id, upserted)
    logger.info("ThreatFox completed: %d IOCs upserted (%d-day window)", upserted, days)
