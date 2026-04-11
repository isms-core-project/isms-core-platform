"""MITRE ATT&CK feed — pulls Enterprise ATT&CK STIX bundle from GitHub.

Ingests all four actor-layer object types:
  attack-pattern  → mitre_techniques  (existing)
  intrusion-set   → mitre_groups      (Phase 28)
  malware / tool  → mitre_software    (Phase 28)
  campaign        → mitre_campaigns   (Phase 28)
  relationship    → mitre_relationships (Phase 28)

Sources:
  v18/v19: https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json
"""

import json
import logging
import os
from datetime import date, datetime, timezone
from uuid import uuid4

import psycopg2.extras
import requests

from feeds.base import fail_run, finish_run, get_conn, start_run

logger = logging.getLogger(__name__)

ATTACK_URL = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"

_SOURCE_LABEL = "attack_v19" if os.environ.get("FEEDS_MITRE_V19", "false").lower() == "true" else "attack_v18"
_RUN_NAME     = "mitre_attack_v19" if _SOURCE_LABEL == "attack_v19" else "mitre_attack_v18"


# ── Parsers ───────────────────────────────────────────────────────────────────

def _ext_ref(obj: dict, source_name: str = "mitre-attack") -> tuple[str, str]:
    """Return (external_id, url) from external_references matching source_name."""
    for ref in obj.get("external_references", []):
        if ref.get("source_name") == source_name:
            return ref.get("external_id", ""), ref.get("url", "")
    return "", ""


def _is_deprecated(obj: dict) -> bool:
    return bool(obj.get("x_mitre_deprecated") or obj.get("revoked"))


def _parse_technique(obj: dict) -> dict | None:
    if obj.get("type") != "attack-pattern":
        return None
    ext_id, url = _ext_ref(obj)
    if not ext_id:
        return None
    tactics = [
        phase["phase_name"]
        for phase in obj.get("kill_chain_phases", [])
        if phase.get("kill_chain_name") == "mitre-attack"
    ]
    return {
        "stix_id":        obj["id"],
        "technique_id":   ext_id,
        "name":           obj.get("name", ""),
        "description":    (obj.get("description") or "")[:8000],
        "tactics":        tactics,
        "platforms":      obj.get("x_mitre_platforms", []),
        "is_subtechnique": bool(obj.get("x_mitre_is_subtechnique", False)),
        "deprecated":     _is_deprecated(obj),
        "url":            url,
    }


def _parse_group(obj: dict) -> dict | None:
    if obj.get("type") != "intrusion-set":
        return None
    ext_id, url = _ext_ref(obj)
    if not ext_id:
        return None
    return {
        "stix_id":     obj["id"],
        "group_id":    ext_id,
        "name":        obj.get("name", ""),
        "description": (obj.get("description") or "")[:8000],
        "aliases":     obj.get("aliases", []),
        "deprecated":  _is_deprecated(obj),
        "url":         url,
    }


def _parse_software(obj: dict) -> dict | None:
    obj_type = obj.get("type")
    if obj_type not in ("malware", "tool"):
        return None
    ext_id, url = _ext_ref(obj)
    if not ext_id:
        return None
    aliases = obj.get("x_mitre_aliases") or obj.get("aliases") or []
    return {
        "stix_id":       obj["id"],
        "software_id":   ext_id,
        "name":          obj.get("name", ""),
        "software_type": obj_type,
        "description":   (obj.get("description") or "")[:8000],
        "aliases":       aliases,
        "platforms":     obj.get("x_mitre_platforms", []),
        "deprecated":    _is_deprecated(obj),
        "url":           url,
    }


def _parse_campaign(obj: dict) -> dict | None:
    if obj.get("type") != "campaign":
        return None
    ext_id, url = _ext_ref(obj)
    if not ext_id:
        return None

    def _to_date(val: str | None) -> date | None:
        if not val:
            return None
        try:
            return datetime.fromisoformat(val.replace("Z", "+00:00")).date()
        except Exception:
            return None

    return {
        "stix_id":     obj["id"],
        "campaign_id": ext_id,
        "name":        obj.get("name", ""),
        "description": (obj.get("description") or "")[:8000],
        "aliases":     obj.get("aliases", []),
        "first_seen":  _to_date(obj.get("first_seen")),
        "last_seen":   _to_date(obj.get("last_seen")),
        "deprecated":  _is_deprecated(obj),
        "url":         url,
    }


def _parse_relationship(obj: dict) -> dict | None:
    if obj.get("type") != "relationship":
        return None
    rel_type   = obj.get("relationship_type", "")
    source_ref = obj.get("source_ref", "")
    target_ref = obj.get("target_ref", "")
    if not source_ref or not target_ref:
        return None
    # Derive object type from STIX ID prefix (e.g. "intrusion-set--uuid")
    source_type = source_ref.split("--")[0] if "--" in source_ref else ""
    target_type = target_ref.split("--")[0] if "--" in target_ref else ""
    return {
        "stix_id":           obj["id"],
        "relationship_type": rel_type,
        "source_ref":        source_ref,
        "target_ref":        target_ref,
        "source_type":       source_type,
        "target_type":       target_type,
        "description":       (obj.get("description") or "")[:2000],
    }


# ── Upsert helpers ────────────────────────────────────────────────────────────

def _upsert_techniques(cur, rows: list[dict], now: datetime) -> int:
    for row in rows:
        cur.execute(
            """
            INSERT INTO mitre_techniques
              (id, stix_id, source, technique_id, name, description,
               tactics, platforms, is_subtechnique, deprecated, url, created_at, updated_at)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (stix_id, source) DO UPDATE SET
              name=EXCLUDED.name, description=EXCLUDED.description,
              tactics=EXCLUDED.tactics, platforms=EXCLUDED.platforms,
              is_subtechnique=EXCLUDED.is_subtechnique,
              deprecated=EXCLUDED.deprecated, url=EXCLUDED.url,
              updated_at=EXCLUDED.updated_at
            """,
            (
                str(uuid4()), row["stix_id"], _SOURCE_LABEL,
                row["technique_id"], row["name"], row["description"],
                psycopg2.extras.Json(row["tactics"]),
                psycopg2.extras.Json(row["platforms"]),
                row["is_subtechnique"], row["deprecated"], row["url"],
                now, now,
            ),
        )
    return len(rows)


def _upsert_groups(cur, rows: list[dict], now: datetime) -> int:
    for row in rows:
        cur.execute(
            """
            INSERT INTO mitre_groups
              (id, stix_id, source, group_id, name, description, aliases, deprecated, url, created_at, updated_at)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (stix_id, source) DO UPDATE SET
              name=EXCLUDED.name, description=EXCLUDED.description,
              aliases=EXCLUDED.aliases, deprecated=EXCLUDED.deprecated,
              url=EXCLUDED.url, updated_at=EXCLUDED.updated_at
            """,
            (
                str(uuid4()), row["stix_id"], _SOURCE_LABEL,
                row["group_id"], row["name"], row["description"],
                psycopg2.extras.Json(row["aliases"]),
                row["deprecated"], row["url"], now, now,
            ),
        )
    return len(rows)


def _upsert_software(cur, rows: list[dict], now: datetime) -> int:
    for row in rows:
        cur.execute(
            """
            INSERT INTO mitre_software
              (id, stix_id, source, software_id, name, software_type,
               description, aliases, platforms, deprecated, url, created_at, updated_at)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (stix_id, source) DO UPDATE SET
              name=EXCLUDED.name, software_type=EXCLUDED.software_type,
              description=EXCLUDED.description, aliases=EXCLUDED.aliases,
              platforms=EXCLUDED.platforms, deprecated=EXCLUDED.deprecated,
              url=EXCLUDED.url, updated_at=EXCLUDED.updated_at
            """,
            (
                str(uuid4()), row["stix_id"], _SOURCE_LABEL,
                row["software_id"], row["name"], row["software_type"],
                row["description"],
                psycopg2.extras.Json(row["aliases"]),
                psycopg2.extras.Json(row["platforms"]),
                row["deprecated"], row["url"], now, now,
            ),
        )
    return len(rows)


def _upsert_campaigns(cur, rows: list[dict], now: datetime) -> int:
    for row in rows:
        cur.execute(
            """
            INSERT INTO mitre_campaigns
              (id, stix_id, source, campaign_id, name, description,
               aliases, first_seen, last_seen, deprecated, url, created_at, updated_at)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (stix_id, source) DO UPDATE SET
              name=EXCLUDED.name, description=EXCLUDED.description,
              aliases=EXCLUDED.aliases, first_seen=EXCLUDED.first_seen,
              last_seen=EXCLUDED.last_seen, deprecated=EXCLUDED.deprecated,
              url=EXCLUDED.url, updated_at=EXCLUDED.updated_at
            """,
            (
                str(uuid4()), row["stix_id"], _SOURCE_LABEL,
                row["campaign_id"], row["name"], row["description"],
                psycopg2.extras.Json(row["aliases"]),
                row["first_seen"], row["last_seen"],
                row["deprecated"], row["url"], now, now,
            ),
        )
    return len(rows)


def _upsert_relationships(cur, rows: list[dict], now: datetime) -> int:
    for row in rows:
        cur.execute(
            """
            INSERT INTO mitre_relationships
              (id, stix_id, source, relationship_type,
               source_ref, target_ref, source_type, target_type, description,
               created_at, updated_at)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (stix_id, source) DO UPDATE SET
              relationship_type=EXCLUDED.relationship_type,
              source_ref=EXCLUDED.source_ref, target_ref=EXCLUDED.target_ref,
              source_type=EXCLUDED.source_type, target_type=EXCLUDED.target_type,
              description=EXCLUDED.description, updated_at=EXCLUDED.updated_at
            """,
            (
                str(uuid4()), row["stix_id"], _SOURCE_LABEL,
                row["relationship_type"],
                row["source_ref"], row["target_ref"],
                row["source_type"], row["target_type"],
                row["description"], now, now,
            ),
        )
    return len(rows)


# ── Main ──────────────────────────────────────────────────────────────────────

def run() -> None:
    run_id = start_run(_RUN_NAME)
    logger.info("MITRE ATT&CK pull started (source=%s)", _SOURCE_LABEL)

    try:
        resp = requests.get(ATTACK_URL, timeout=120)
        resp.raise_for_status()
        bundle = resp.json()
    except Exception as exc:
        fail_run(run_id, str(exc))
        logger.error("MITRE ATT&CK download failed: %s", exc)
        return

    objects = bundle.get("objects", [])
    now     = datetime.now(timezone.utc)

    techniques:    list[dict] = []
    groups:        list[dict] = []
    software:      list[dict] = []
    campaigns:     list[dict] = []
    relationships: list[dict] = []

    for obj in objects:
        if (r := _parse_technique(obj)):    techniques.append(r)
        elif (r := _parse_group(obj)):      groups.append(r)
        elif (r := _parse_software(obj)):   software.append(r)
        elif (r := _parse_campaign(obj)):   campaigns.append(r)
        elif (r := _parse_relationship(obj)): relationships.append(r)

    if not techniques:
        fail_run(run_id, "No attack-pattern objects found in bundle")
        return

    total = 0
    with get_conn() as conn:
        with conn.cursor() as cur:
            total += _upsert_techniques(cur, techniques, now)
            total += _upsert_groups(cur, groups, now)
            total += _upsert_software(cur, software, now)
            total += _upsert_campaigns(cur, campaigns, now)
            total += _upsert_relationships(cur, relationships, now)

    finish_run(run_id, total)
    logger.info(
        "MITRE ATT&CK completed: %d techniques, %d groups, %d software, %d campaigns, %d relationships",
        len(techniques), len(groups), len(software), len(campaigns), len(relationships),
    )
