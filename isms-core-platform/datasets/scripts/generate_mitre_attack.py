#!/usr/bin/env python3
"""
Generate MITRE ATT&CK v18 dataset bundle from structured summary.

Pipeline: raw/mitre_attack_v18.json → data/mitre_attack_v18.json

14 Tactics, 691 Techniques/Sub-techniques, 44 Mitigations.
"""

import json
import uuid
import hashlib
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RAW_DIR = SCRIPT_DIR.parent / "raw"
DATA_DIR = SCRIPT_DIR.parent / "data"
RAW_FILE = RAW_DIR / "mitre_attack_v18.json"
OUTPUT_FILE = DATA_DIR / "mitre_attack_v18.json"

ISMS_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
FRAMEWORK_CODE = "MITRE_ATTACK_V18"


def stable_uuid(key: str) -> str:
    return str(uuid.uuid5(ISMS_NAMESPACE, key))


def framework_uuid() -> str:
    return stable_uuid(f"framework:{FRAMEWORK_CODE}")


def control_uuid(control_id: str) -> str:
    return stable_uuid(f"control:{FRAMEWORK_CODE}:{control_id}")


def generate_bundle() -> dict:
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
    # Combine techniques and subtechniques into one list
    all_techniques = raw.get("techniques", []) + raw.get("subtechniques", [])

    # Build parent technique map for sub-techniques
    technique_map = {}
    for tech in all_techniques:
        t_id = tech["id"]
        technique_map[t_id] = control_uuid(t_id)

    for tech in all_techniques:
        t_id = tech["id"]
        t_uuid = control_uuid(t_id)
        is_sub = tech.get("is_subtechnique", False)

        if is_sub:
            # Parent is the base technique ID (e.g., T1059 from T1059.001)
            parent_base = t_id.split(".")[0]
            parent_id = technique_map.get(parent_base)
            level = 2
        else:
            # Parent is first tactic
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

        # Relationships to all tactics
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

        # Sub-technique hierarchy
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
            "version": meta.get("attack_version", "18.1"),
            "publisher": "MITRE",
            "source_url": "https://attack.mitre.org/",
            "description": "Adversarial Tactics, Techniques, and Common Knowledge — Enterprise matrix"
        },
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "generate_mitre_attack.py",
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


if __name__ == "__main__":
    main()
