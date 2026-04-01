#!/usr/bin/env python3
"""
Generate MITRE ATT&CK v19 dataset bundle from structured summary.

Pipeline: raw/mitre_attack_v19.json → data/mitre_attack_v19.json

ATT&CK v19 releases 2026-04-28. Key breaking change vs v18:
  - Defense Evasion (TA0005) tactic RETIRED
  - Replaced by two new tactics:
      - Stealth           (techniques: evasion-focused)
      - Impair Defenses   (techniques: defense-disabling)
  See: https://attack.mitre.org/resources/updates/updates-april-2026/

BEFORE RUNNING:
  1. Download the v19 STIX bundle from MITRE after 2026-04-28:
       https://github.com/mitre-attack/attack-stix-data
  2. Run process_mitre_attack.py against the v19 STIX bundle to produce
     raw/mitre_attack_v19.json (same format as raw/mitre_attack_v18.json)
  3. Run this script: python generate_mitre_attack_v19.py

POST-GENERATION:
  - Update bootstrap/importer to load mitre_attack_v19.json instead of v18
  - Update crosswalk.json notes: replace "Defense Evasion" with
    "Stealth; Impair Defenses" where appropriate (132 hits in notes fields)
  - Run: datasets/scripts/add_mitre_owasp_finma_mappings.py (check for
    any hardcoded defense-evasion references)
"""

import json
import uuid
import hashlib
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RAW_DIR = SCRIPT_DIR.parent / "raw"
DATA_DIR = SCRIPT_DIR.parent / "data"
RAW_FILE = RAW_DIR / "mitre_attack_v19.json"
OUTPUT_FILE = DATA_DIR / "mitre_attack_v19.json"

ISMS_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
FRAMEWORK_CODE = "MITRE_ATTACK_V19"


def stable_uuid(key: str) -> str:
    return str(uuid.uuid5(ISMS_NAMESPACE, key))


def framework_uuid() -> str:
    return stable_uuid(f"framework:{FRAMEWORK_CODE}")


def control_uuid(control_id: str) -> str:
    return stable_uuid(f"control:{FRAMEWORK_CODE}:{control_id}")


def generate_bundle() -> dict:
    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"{RAW_FILE} not found.\n"
            "Download v19 STIX data from https://github.com/mitre-attack/attack-stix-data "
            "after 2026-04-28 and run process_mitre_attack.py first."
        )

    with open(RAW_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    meta = raw["_metadata"]
    counts = raw["counts"]
    fw_id = framework_uuid()

    objects = []
    relationships = []
    tactic_map = {}

    # Tactics (level 0)
    for i, tactic in enumerate(raw["tactics"]):
        t_id = tactic["id"]
        t_uuid = control_uuid(t_id)
        tactic_map[tactic["shortname"]] = t_uuid
        tactic_map[t_id] = t_uuid

        objects.append({
            "type": "framework_control",
            "id": t_uuid,
            "framework_id": fw_id,
            "control_id": t_id,
            "title": tactic["name"],
            "level": 0,
            "sort_order": (i + 1) * 10000,
            "metadata": {
                "shortname": tactic["shortname"],
                "stix_id": tactic.get("stix_id", "")
            }
        })

    # Techniques and sub-techniques (level 1 and 2)
    all_techniques = raw.get("techniques", []) + raw.get("subtechniques", [])

    technique_map = {}
    for tech in all_techniques:
        t_id = tech["id"]
        technique_map[t_id] = control_uuid(t_id)

    for tech in all_techniques:
        t_id = tech["id"]
        t_uuid = control_uuid(t_id)
        is_sub = tech.get("is_subtechnique", False)

        if is_sub:
            parent_base = t_id.split(".")[0]
            parent_id = technique_map.get(parent_base)
            level = 2
        else:
            tactic_ids = tech.get("tactic_ids", tech.get("tactics", []))
            parent_id = None
            for tid in tactic_ids:
                if tid in tactic_map:
                    parent_id = tactic_map[tid]
                    break
            level = 1

        objects.append({
            "type": "framework_control",
            "id": t_uuid,
            "framework_id": fw_id,
            "parent_id": parent_id,
            "control_id": t_id,
            "title": tech["name"],
            "level": level,
            "sort_order": _technique_sort(t_id),
            "metadata": {
                "is_subtechnique": is_sub,
                "tactics": tech.get("tactics", tech.get("tactic_ids", [])),
                "platforms": tech.get("platforms", [])
            }
        })

        tactic_ids = tech.get("tactic_ids", tech.get("tactics", []))
        for tid in tactic_ids:
            tac_uuid = tactic_map.get(tid)
            if tac_uuid:
                relationships.append({
                    "type": "tactic-technique",
                    "source_id": t_uuid,
                    "target_id": tac_uuid,
                    "relationship_type": "uses-tactic"
                })

        if is_sub and parent_id:
            relationships.append({
                "type": "hierarchy",
                "source_id": t_uuid,
                "target_id": parent_id,
                "relationship_type": "part-of"
            })

    # Mitigations (separate type)
    for mit in raw.get("mitigations", []):
        m_id = mit["id"]
        m_uuid = control_uuid(m_id)

        objects.append({
            "type": "framework_control",
            "id": m_uuid,
            "framework_id": fw_id,
            "control_id": m_id,
            "title": mit["name"],
            "level": 0,
            "sort_order": 90000 + int(m_id.replace("M", "").replace(".", "")),
            "metadata": {
                "object_type": "mitigation",
                "stix_id": mit.get("stix_id", "")
            }
        })

    content_str = json.dumps(objects, sort_keys=True)
    content_hash = hashlib.sha256(content_str.encode()).hexdigest()

    bundle = {
        "bundle_id": f"bundle--{stable_uuid(f'bundle:mitre_attack:{content_hash[:16]}')}",
        "bundle_type": "isms-core-dataset",
        "bundle_version": "1.0",
        "framework": {
            "id": fw_id,
            "code": FRAMEWORK_CODE,
            "name": "MITRE ATT&CK Enterprise",
            "version": meta.get("attack_version", "19.0"),
            "publisher": "MITRE",
            "source_url": "https://attack.mitre.org/",
            "description": "Adversarial Tactics, Techniques, and Common Knowledge — Enterprise matrix"
        },
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "generate_mitre_attack_v19.py",
        "content_hash": content_hash,
        "counts": counts,
        "objects_count": len(objects),
        "relationships_count": len(relationships),
        "objects": objects,
        "relationships": relationships
    }

    return bundle


def _technique_sort(t_id: str) -> int:
    """Convert T1059.001 to numeric sort key."""
    parts = t_id.replace("T", "").split(".")
    try:
        base = int(parts[0])
        sub = int(parts[1]) if len(parts) > 1 else 0
        return base * 1000 + sub
    except ValueError:
        return 0


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Reading raw data from {RAW_FILE}")
    bundle = generate_bundle()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)

    tactics = len([o for o in bundle["objects"] if o["level"] == 0 and o["metadata"].get("object_type") != "mitigation"])
    mitigations = len([o for o in bundle["objects"] if o["metadata"].get("object_type") == "mitigation"])
    techniques = len([o for o in bundle["objects"] if o["level"] == 1])
    subtechniques = len([o for o in bundle["objects"] if o["level"] == 2])

    print(f"Generated {OUTPUT_FILE.name}:")
    print(f"  Tactics:        {tactics}")
    print(f"  Techniques:     {techniques}")
    print(f"  Sub-techniques: {subtechniques}")
    print(f"  Mitigations:    {mitigations}")
    print(f"  Total objects:  {bundle['objects_count']}")
    print(f"  Relationships:  {bundle['relationships_count']}")
    print(f"  Content hash:   {bundle['content_hash'][:16]}...")
    print()
    print("NOTE: Defense Evasion (TA0005) is retired in v19.")
    print("  → Update crosswalk.json notes (132 'Defense Evasion' references)")
    print("  → New tactics: Stealth, Impair Defenses")


if __name__ == "__main__":
    main()

# QA_VERIFIED: 2026-04-02
