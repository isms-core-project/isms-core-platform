#!/usr/bin/env python3
"""
Generate CIS Controls v8.1 dataset bundle from raw data.

Pipeline: raw/cis_controls_v8.json → data/cis_controls_v8.json

18 Controls + 153 Safeguards with Implementation Group classification.
"""

import json
import uuid
import hashlib
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RAW_DIR = SCRIPT_DIR.parent / "raw"
DATA_DIR = SCRIPT_DIR.parent / "data"
RAW_FILE = RAW_DIR / "cis_controls_v8.json"
OUTPUT_FILE = DATA_DIR / "cis_controls_v8.json"

ISMS_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
FRAMEWORK_CODE = "CIS_V8"


def stable_uuid(key: str) -> str:
    return str(uuid.uuid5(ISMS_NAMESPACE, key))


def framework_uuid() -> str:
    return stable_uuid(f"framework:{FRAMEWORK_CODE}")


def control_uuid(control_id: str) -> str:
    return stable_uuid(f"control:{FRAMEWORK_CODE}:{control_id}")


def generate_bundle() -> dict:
    with open(RAW_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    meta = raw["metadata"]
    fw_id = framework_uuid()

    objects = []
    relationships = []

    for ctrl in raw["controls"]:
        ctrl_num = str(ctrl["control_id"])
        ctrl_label = f"CIS {ctrl_num}"
        ctrl_uuid = control_uuid(ctrl_label)

        # Control (level 0)
        objects.append({
            "type": "framework_control",
            "id": ctrl_uuid,
            "framework_id": fw_id,
            "control_id": ctrl_label,
            "title": ctrl["control_name"],
            "description": ctrl.get("description", ""),
            "level": 0,
            "sort_order": int(ctrl_num) * 1000,
            "metadata": {
                "control_number": int(ctrl_num),
                "safeguard_count": len(ctrl.get("safeguards", []))
            }
        })

        for sg in ctrl.get("safeguards", []):
            sg_id = sg["safeguard_id"]
            sg_full_id = f"CIS {sg_id}"
            sg_uuid = control_uuid(sg_full_id)

            objects.append({
                "type": "framework_control",
                "id": sg_uuid,
                "framework_id": fw_id,
                "parent_id": ctrl_uuid,
                "control_id": sg_full_id,
                "title": sg["title"],
                "description": sg.get("description", ""),
                "level": 1,
                "sort_order": int(sg_id.replace(".", "").ljust(4, "0")),
                "metadata": {
                    "safeguard_id": sg_id,
                    "asset_type": sg.get("asset_type", ""),
                    "security_function": sg.get("security_function", ""),
                    "implementation_groups": sg.get("implementation_groups", [])
                }
            })

            relationships.append({
                "type": "hierarchy",
                "source_id": sg_uuid,
                "target_id": ctrl_uuid,
                "relationship_type": "part-of"
            })

    content_str = json.dumps(objects, sort_keys=True)
    content_hash = hashlib.sha256(content_str.encode()).hexdigest()

    bundle = {
        "bundle_id": f"bundle--{stable_uuid(f'bundle:cis_v8:{content_hash[:16]}')}",
        "bundle_type": "isms-core-dataset",
        "bundle_version": "1.0",
        "framework": {
            "id": fw_id,
            "code": FRAMEWORK_CODE,
            "name": meta["framework"],
            "version": meta["version"],
            "publisher": "CIS",
            "source_url": meta.get("url", "https://www.cisecurity.org/controls"),
            "description": "CIS Critical Security Controls — prioritised set of actions for cyber defence"
        },
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "generate_cis_v8.py",
        "content_hash": content_hash,
        "objects_count": len(objects),
        "relationships_count": len(relationships),
        "objects": objects,
        "relationships": relationships
    }

    return bundle


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Reading raw data from {RAW_FILE}")
    bundle = generate_bundle()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)

    controls = len([o for o in bundle["objects"] if o["level"] == 0])
    safeguards = len([o for o in bundle["objects"] if o["level"] == 1])
    print(f"Generated {OUTPUT_FILE.name}:")
    print(f"  Controls:     {controls}")
    print(f"  Safeguards:   {safeguards}")
    print(f"  Total:        {bundle['objects_count']}")
    print(f"  Relationships:{bundle['relationships_count']}")
    print(f"  Content hash: {bundle['content_hash'][:16]}...")


if __name__ == "__main__":
    main()
