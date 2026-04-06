"""MITRE ATLAS feed — pulls ML-focused adversarial tactic/technique data.

Source: https://raw.githubusercontent.com/mitre-atlas/atlas-data/main/dist/ATLAS.yaml
"""

import logging
from datetime import datetime, timezone
from uuid import uuid4

import psycopg2.extras
import requests
import yaml

from feeds.base import fail_run, finish_run, get_conn, start_run

logger = logging.getLogger(__name__)

ATLAS_URL = "https://raw.githubusercontent.com/mitre-atlas/atlas-data/main/dist/ATLAS.yaml"


def run() -> None:
    run_id = start_run("mitre_atlas")
    logger.info("MITRE ATLAS pull started")

    try:
        resp = requests.get(ATLAS_URL, timeout=60)
        resp.raise_for_status()
        data = yaml.safe_load(resp.text)
    except Exception as exc:
        fail_run(run_id, str(exc))
        logger.error("MITRE ATLAS download failed: %s", exc)
        return

    now = datetime.now(timezone.utc)

    # ATLAS YAML structure:
    # matrices[0].tactics[].id/.name
    # matrices[0].techniques[].id/.name/.description/.tactics[]/...
    matrix = (data.get("matrices") or [{}])[0]
    techniques_raw = matrix.get("techniques") or []

    # Build tactic id -> name map
    tactic_map: dict[str, str] = {
        t["id"]: t.get("name", t["id"])
        for t in (matrix.get("tactics") or [])
    }

    rows: list[dict] = []
    for tech in techniques_raw:
        tech_id = tech.get("id", "")
        if not tech_id:
            continue

        # tactics may be a list of tactic IDs or objects
        raw_tactics = tech.get("tactics") or []
        tactic_names: list[str] = []
        for t in raw_tactics:
            if isinstance(t, str):
                tactic_names.append(tactic_map.get(t, t))
            elif isinstance(t, dict):
                tname = t.get("name") or tactic_map.get(t.get("id", ""), "")
                if tname:
                    tactic_names.append(tname)

        subtechs = tech.get("subtechniques") or []
        # Store parent technique
        rows.append({
            "stix_id": f"atlas--{tech_id}",
            "technique_id": tech_id,
            "name": tech.get("name", ""),
            "description": (tech.get("description") or "")[:8000],
            "tactics": tactic_names,
            "platforms": [],
            "is_subtechnique": False,
        })
        # Store sub-techniques
        for sub in subtechs:
            sub_id = sub.get("id", "")
            if not sub_id:
                continue
            rows.append({
                "stix_id": f"atlas--{sub_id}",
                "technique_id": sub_id,
                "name": sub.get("name", ""),
                "description": (sub.get("description") or "")[:8000],
                "tactics": tactic_names,
                "platforms": [],
                "is_subtechnique": True,
            })

    if not rows:
        fail_run(run_id, "No techniques found in ATLAS YAML")
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
                    VALUES (%s,%s,'atlas',%s,%s,%s,%s,%s,%s,false,NULL,%s,%s)
                    ON CONFLICT (stix_id, source) DO UPDATE SET
                      name            = EXCLUDED.name,
                      description     = EXCLUDED.description,
                      tactics         = EXCLUDED.tactics,
                      is_subtechnique = EXCLUDED.is_subtechnique,
                      updated_at      = EXCLUDED.updated_at
                    """,
                    (
                        str(uuid4()), row["stix_id"],
                        row["technique_id"], row["name"], row["description"],
                        psycopg2.extras.Json(row["tactics"]),
                        psycopg2.extras.Json(row["platforms"]),
                        row["is_subtechnique"],
                        now, now,
                    ),
                )
                upserted += 1

    finish_run(run_id, upserted)
    logger.info("MITRE ATLAS completed: %d techniques upserted", upserted)
