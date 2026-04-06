"""MITRE ATT&CK feed — pulls Enterprise ATT&CK STIX bundle from GitHub.

Sources:
  v18: https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json
  v19: Same URL (updated in-place when v19 releases). We store as attack_v18 until
       the bundle header confirms v19, then store as attack_v19 and keep v18.
"""

import json
import logging
import os
from datetime import datetime, timezone
from uuid import uuid4

import psycopg2.extras
import requests

from feeds.base import fail_run, finish_run, get_conn, start_run

logger = logging.getLogger(__name__)

ATTACK_URL = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"

# We always label what we pull as "attack_v18" until ATT&CK v19 is officially
# released and the STIX bundle version header changes.  When v19 lands, set
# FEEDS_MITRE_V19=true in .env and the source label will switch.
_SOURCE_LABEL = "attack_v19" if os.environ.get("FEEDS_MITRE_V19", "false").lower() == "true" else "attack_v18"


def _parse_technique(obj: dict) -> dict | None:
    """Extract fields from a STIX attack-pattern object.  Returns None to skip."""
    if obj.get("type") != "attack-pattern":
        return None
    if obj.get("x_mitre_is_subtechnique") and not obj.get("x_mitre_is_subtechnique") in (True, False):
        return None

    # External references — first one with source_name == 'mitre-attack' has the T-code
    technique_id = ""
    url = ""
    for ref in obj.get("external_references", []):
        if ref.get("source_name") == "mitre-attack":
            technique_id = ref.get("external_id", "")
            url = ref.get("url", "")
            break

    if not technique_id:
        return None

    tactics = [
        phase["phase_name"]
        for phase in obj.get("kill_chain_phases", [])
        if phase.get("kill_chain_name") == "mitre-attack"
    ]
    platforms = obj.get("x_mitre_platforms", [])

    return {
        "stix_id": obj["id"],
        "technique_id": technique_id,
        "name": obj.get("name", ""),
        "description": (obj.get("description") or "")[:8000],
        "tactics": tactics,
        "platforms": platforms,
        "is_subtechnique": bool(obj.get("x_mitre_is_subtechnique", False)),
        "deprecated": bool(obj.get("x_mitre_deprecated", False) or obj.get("revoked", False)),
        "url": url,
    }


def run() -> None:
    run_id = start_run(_SOURCE_LABEL)
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
    now = datetime.now(timezone.utc)

    rows: list[dict] = []
    for obj in objects:
        parsed = _parse_technique(obj)
        if parsed:
            rows.append(parsed)

    if not rows:
        fail_run(run_id, "No attack-pattern objects found in bundle")
        return

    upserted = 0
    with get_conn() as conn:
        with conn.cursor() as cur:
            for row in rows:
                cur.execute(
                    """
                    INSERT INTO mitre_techniques
                      (id, stix_id, source, technique_id, name, description,
                       tactics, platforms, is_subtechnique, deprecated, url,
                       created_at, updated_at)
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (stix_id, source) DO UPDATE SET
                      name           = EXCLUDED.name,
                      description    = EXCLUDED.description,
                      tactics        = EXCLUDED.tactics,
                      platforms      = EXCLUDED.platforms,
                      is_subtechnique= EXCLUDED.is_subtechnique,
                      deprecated     = EXCLUDED.deprecated,
                      url            = EXCLUDED.url,
                      updated_at     = EXCLUDED.updated_at
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
                upserted += 1

    finish_run(run_id, upserted)
    logger.info("MITRE ATT&CK completed: %d techniques upserted", upserted)
