"""MISP OSINT feed ingestor — handles CIRCL and Botvrij with the same logic.

First-run behaviour:
  - Fetches the manifest, filters events by TI_MISP_IMPORT_FROM_DATE (default 2024-01-01).
  - Processes only matching UUIDs, records each in ti_misp_state.

Delta runs (every 6h):
  - Fetches manifest, skips any UUID already in ti_misp_state for this source.
  - TI_MISP_IMPORT_FROM_DATE is ignored after first run.

Correlation at ingest:
  - Extracts ip/domain/url/hash IOC attributes from each event.
  - Parses misp-galaxy tags for malpedia slugs, threat-actor names, MITRE TIDs.
  - Stamps family_slugs, actor_slugs, mitre_tids onto each ti_iocs row.
"""

import json
import logging
import os
from datetime import datetime, timezone
from uuid import uuid4

import requests

from feeds.base import fail_run, finish_run, get_conn, get_os_client, is_cancelled, os_bulk_upsert, start_run

logger = logging.getLogger(__name__)

# IOC attribute types we care about, mapped to our ioc_type values
_ATTR_TYPE_MAP = {
    "ip-src":           "ip",
    "ip-dst":           "ip",
    "ip-src|port":      "ip",
    "ip-dst|port":      "ip",
    "domain":           "domain",
    "hostname":         "domain",
    "url":              "url",
    "md5":              "md5",
    "sha1":             "sha1",
    "sha256":           "sha256",
    "filename|md5":     "md5",
    "filename|sha1":    "sha1",
    "filename|sha256":  "sha256",
}

_OS_MAPPING = {
    "mappings": {
        "properties": {
            "ioc_type":    {"type": "keyword"},
            "value":       {"type": "keyword"},
            "source":      {"type": "keyword"},
            "confidence":  {"type": "integer"},
            "tags":        {"type": "keyword"},
            "mitre_tids":  {"type": "keyword"},
            "family_slugs": {"type": "keyword"},
            "actor_slugs": {"type": "keyword"},
            "first_seen":  {"type": "date"},
            "last_seen":   {"type": "date"},
            "indexed_at":  {"type": "date"},
        }
    }
}


def _ensure_os_index(client, index: str) -> None:
    if not client.indices.exists(index=index):
        client.indices.create(index=index, body=_OS_MAPPING)
        logger.info("Created OpenSearch index: %s", index)


def _import_from_date() -> str:
    return os.environ.get("TI_MISP_IMPORT_FROM_DATE", "2024-01-01")


def _processed_uuids(source: str) -> set:
    """Return the set of event UUIDs already processed for this source."""
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT event_uuid FROM ti_misp_state WHERE source = %s",
                    (source,),
                )
                return {row[0] for row in cur.fetchall()}
    except Exception as exc:
        logger.warning("Could not load ti_misp_state for %s: %s", source, exc)
        return set()


def _mark_processed(source: str, uuids: list[str]) -> None:
    if not uuids:
        return
    now = datetime.now(timezone.utc)
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                psycopg2_extras_available = True
                try:
                    import psycopg2.extras
                    psycopg2.extras.execute_values(
                        cur,
                        "INSERT INTO ti_misp_state (source, event_uuid, processed_at) VALUES %s ON CONFLICT DO NOTHING",
                        [(source, u, now) for u in uuids],
                    )
                except ImportError:
                    psycopg2_extras_available = False
                if not psycopg2_extras_available:
                    for u in uuids:
                        cur.execute(
                            "INSERT INTO ti_misp_state (source, event_uuid, processed_at) VALUES (%s,%s,%s) ON CONFLICT DO NOTHING",
                            (source, u, now),
                        )
    except Exception as exc:
        logger.warning("Could not persist ti_misp_state for %s: %s", source, exc)


def _extract_tlp(tags: list) -> str | None:
    """Return normalised TLP level from MISP tags (e.g. 'white', 'green')."""
    for tag in tags:
        name = (tag.get("name", "") if isinstance(tag, dict) else str(tag)).lower()
        if name.startswith("tlp:"):
            level = name.split(":", 1)[1].strip()
            if level in ("white", "green", "amber", "red"):
                return level
    return None


def _parse_galaxy_tags(tags: list) -> tuple[list, list, list]:
    """
    Returns (family_slugs, actor_slugs, mitre_tids) extracted from MISP galaxy tags.
    Tag format examples:
      misp-galaxy:malpedia="win.emotet"
      misp-galaxy:threat-actor="APT28"
      misp-galaxy:mitre-attack-pattern="Process Injection - T1055"
    """
    if not tags:
        return [], [], []
    family_slugs, actor_slugs, mitre_tids = [], [], []
    for tag in tags:
        name = tag.get("name", "") if isinstance(tag, dict) else str(tag)
        if name.startswith('misp-galaxy:malpedia="'):
            slug = name.split('"')[1]
            family_slugs.append(slug)
        elif name.startswith('misp-galaxy:threat-actor="'):
            actor = name.split('"')[1]
            actor_slugs.append(actor)
        elif "mitre-attack-pattern" in name:
            # Extract TID like T1055 or T1055.001 from the value string
            import re
            tids = re.findall(r"T\d{4}(?:\.\d{3})?", name)
            mitre_tids.extend(tids)
    return (
        list(dict.fromkeys(family_slugs)),
        list(dict.fromkeys(actor_slugs)),
        list(dict.fromkeys(mitre_tids)),
    )


def _extract_iocs_from_event(event_data: dict, source: str, event_uuid: str) -> list[dict]:
    """Parse a MISP event JSON and return a list of IOC dicts ready for DB upsert."""
    event = event_data.get("Event", event_data)
    now = datetime.now(timezone.utc)

    # Event-level tags → galaxy slugs + TIDs + TLP
    tags = event.get("Tag", [])
    family_slugs, actor_slugs, mitre_tids = _parse_galaxy_tags(tags)
    tlp = _extract_tlp(tags)

    # Event date
    event_date_str = event.get("date") or event.get("timestamp")
    try:
        event_dt = datetime.fromisoformat(event_date_str) if event_date_str else now
    except (ValueError, TypeError):
        event_dt = now

    iocs = []
    for attr in event.get("Attribute", []):
        attr_type = attr.get("type", "")
        ioc_type = _ATTR_TYPE_MAP.get(attr_type)
        if not ioc_type:
            continue

        value = attr.get("value", "")
        if not value:
            continue

        # For combined types like "ip-src|port", take only the IP part
        if "|" in attr_type and "|" not in ioc_type:
            value = value.split("|")[0]

        value = value.strip()
        if not value:
            continue

        # Attribute-level tags can add more context
        attr_tags = attr.get("Tag", [])
        a_family, a_actor, a_tids = _parse_galaxy_tags(attr_tags)

        iocs.append({
            "ioc_type":    ioc_type,
            "value":       value[:2000],
            "source":      source,
            "confidence":  None,
            "tlp":         tlp,
            "tags":        [t.get("name", t) if isinstance(t, dict) else t for t in tags + attr_tags],
            "mitre_tids":  list(dict.fromkeys(mitre_tids + a_tids)),
            "family_slugs": list(dict.fromkeys(family_slugs + a_family)),
            "actor_slugs":  list(dict.fromkeys(actor_slugs + a_actor)),
            "event_uuids": [event_uuid],
            "first_seen":  event_dt,
            "last_seen":   event_dt,
            "created_at":  now,
        })

    return iocs


def _upsert_iocs(iocs: list[dict]) -> int:
    if not iocs:
        return 0
    import json as _json
    now = datetime.now(timezone.utc)
    upserted = 0
    with get_conn() as conn:
        with conn.cursor() as cur:
            for ioc in iocs:
                cur.execute(
                    """
                    INSERT INTO ti_iocs
                      (id, ioc_type, value, source, confidence, tlp, tags, mitre_tids,
                       family_slugs, actor_slugs, event_uuids, first_seen, last_seen, created_at)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (ioc_type, value, source) DO UPDATE SET
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
                      event_uuids  = COALESCE((
                          SELECT jsonb_agg(DISTINCT elem)
                          FROM jsonb_array_elements(ti_iocs.event_uuids || EXCLUDED.event_uuids) elem
                      ), '[]'::jsonb),
                      last_seen    = GREATEST(ti_iocs.last_seen, EXCLUDED.last_seen)
                    """,
                    (
                        str(uuid4()),
                        ioc["ioc_type"], ioc["value"], ioc["source"],
                        ioc["confidence"],
                        ioc.get("tlp"),
                        _json.dumps(ioc.get("tags") or []),
                        _json.dumps(ioc.get("mitre_tids") or []),
                        _json.dumps(ioc.get("family_slugs") or []),
                        _json.dumps(ioc.get("actor_slugs") or []),
                        _json.dumps(ioc.get("event_uuids") or []),
                        ioc["first_seen"], ioc["last_seen"], ioc["created_at"],
                    ),
                )
                upserted += 1
    return upserted


def run(source_name: str, feed_url: str, os_index: str) -> None:
    """
    Pull a MISP OSINT feed.

    Args:
        source_name: 'circl_misp' or 'botvrij_misp' — used as DB source tag + ti_misp_state key
        feed_url:    base URL of the MISP feed (must end without trailing slash)
        os_index:    OpenSearch index to write IOCs to
    """
    run_id = start_run(source_name)
    logger.info("MISP feed pull started: %s (%s)", source_name, feed_url)

    # ── 1. Fetch manifest ────────────────────────────────────────────────────
    try:
        resp = requests.get(f"{feed_url}/manifest.json", timeout=60)
        resp.raise_for_status()
        manifest: dict = resp.json()
    except Exception as exc:
        fail_run(run_id, f"Manifest fetch failed: {exc}")
        logger.error("MISP manifest fetch failed for %s: %s", source_name, exc)
        return

    # ── 2. Determine which UUIDs to process ─────────────────────────────────
    already_processed = _processed_uuids(source_name)
    import_from = _import_from_date()

    new_uuids = []
    for uuid, meta in manifest.items():
        if uuid in already_processed:
            continue
        event_date = (meta.get("date") or "")[:10]
        if event_date and event_date < import_from:
            continue
        new_uuids.append(uuid)

    if not new_uuids:
        finish_run(run_id, 0)
        logger.info("MISP %s: no new events since last run", source_name)
        return

    logger.info("MISP %s: %d new events to process (from %s)", source_name, len(new_uuids), import_from)

    # ── 3. OpenSearch setup ──────────────────────────────────────────────────
    os_client = get_os_client()
    if os_client:
        try:
            _ensure_os_index(os_client, os_index)
        except Exception as exc:
            logger.warning("OpenSearch index setup failed: %s", exc)
            os_client = None

    # ── 4. Fetch + ingest each event ─────────────────────────────────────────
    total_iocs = 0
    processed_uuids_this_run: list[str] = []
    os_docs: list[dict] = []
    now_iso = datetime.now(timezone.utc).isoformat()

    for i, event_uuid in enumerate(new_uuids):
        if is_cancelled(source_name):
            logger.info("MISP %s cancelled at event %d/%d", source_name, i, len(new_uuids))
            _mark_processed(source_name, processed_uuids_this_run)
            fail_run(run_id, "Cancelled by user")
            return
        try:
            resp = requests.get(f"{feed_url}/{event_uuid}.json", timeout=30)
            resp.raise_for_status()
            event_data = resp.json()
        except Exception as exc:
            logger.warning("MISP %s: failed to fetch event %s: %s", source_name, event_uuid, exc)
            continue

        iocs = _extract_iocs_from_event(event_data, source_name, event_uuid)
        if iocs:
            upserted = _upsert_iocs(iocs)
            total_iocs += upserted

            if os_client:
                for ioc in iocs:
                    os_docs.append({
                        "ioc_type":    ioc["ioc_type"],
                        "value":       ioc["value"],
                        "source":      ioc["source"],
                        "confidence":  ioc["confidence"],
                        "tags":        ioc["tags"],
                        "mitre_tids":  ioc["mitre_tids"],
                        "family_slugs": ioc["family_slugs"],
                        "actor_slugs": ioc["actor_slugs"],
                        "first_seen":  ioc["first_seen"].isoformat() if ioc["first_seen"] else None,
                        "last_seen":   ioc["last_seen"].isoformat() if ioc["last_seen"] else None,
                        "indexed_at":  now_iso,
                        "_os_id":      f"{source_name}:{ioc['ioc_type']}:{ioc['value']}",
                    })

        processed_uuids_this_run.append(event_uuid)

        # Flush OS every 1000 docs and persist state every 200 events
        if len(os_docs) >= 1000 and os_client:
            os_bulk_upsert(os_client, os_index, os_docs, "_os_id")
            os_docs = []
        if len(processed_uuids_this_run) % 200 == 0:
            _mark_processed(source_name, processed_uuids_this_run[-200:])

        if (i + 1) % 100 == 0:
            logger.info("MISP %s: processed %d/%d events, %d IOCs so far",
                        source_name, i + 1, len(new_uuids), total_iocs)

    # Final flush
    if os_docs and os_client:
        os_bulk_upsert(os_client, os_index, os_docs, "_os_id")
    _mark_processed(source_name, processed_uuids_this_run)

    finish_run(run_id, total_iocs)
    logger.info("MISP %s completed: %d events → %d IOCs upserted", source_name, len(processed_uuids_this_run), total_iocs)


def run_circl() -> None:
    run("circl_misp", "https://www.circl.lu/doc/misp/feed-osint", "ti-misp-circl")


def run_botvrij() -> None:
    run("botvrij_misp", "https://www.botvrij.eu/data/feed-osint", "ti-misp-botvrij")
