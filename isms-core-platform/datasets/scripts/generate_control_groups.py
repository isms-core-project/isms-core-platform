#!/usr/bin/env python3
"""
Generate ISMS CORE control groups dataset bundle from raw data.

Pipeline: raw/control_groups.json → data/control_groups.json

Each control group maps to one or more ISO 27001:2022 Annex A controls.
The bundle includes containment relationships linking groups to ISO controls.
"""

import json
import uuid
import hashlib
from datetime import datetime, timezone
from pathlib import Path

# =============================================================================
# PATHS
# =============================================================================
SCRIPT_DIR = Path(__file__).resolve().parent
RAW_DIR = SCRIPT_DIR.parent / "raw"
DATA_DIR = SCRIPT_DIR.parent / "data"
RAW_FILE = RAW_DIR / "control_groups.json"
ISO_BUNDLE = DATA_DIR / "iso27001_2022.json"
OUTPUT_FILE = DATA_DIR / "control_groups.json"

# =============================================================================
# UUID STRATEGY
# =============================================================================
ISMS_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")


def stable_uuid(key: str) -> str:
    """Generate deterministic UUID5 from a stable key."""
    return str(uuid.uuid5(ISMS_NAMESPACE, key))


def group_uuid(group_code: str) -> str:
    """UUID for a control group entity."""
    return stable_uuid(f"control_group:{group_code}")


def control_uuid(framework_code: str, control_id: str) -> str:
    """UUID for a framework control entity (must match generate_iso27001.py)."""
    return stable_uuid(f"control:{framework_code}:{control_id}")


# =============================================================================
# GENERATOR
# =============================================================================
def generate_bundle() -> dict:
    """Read raw control groups and produce a stable-ID bundle."""

    with open(RAW_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    # Load ISO 27001 bundle for cross-referencing control UUIDs
    iso_controls = {}
    if ISO_BUNDLE.exists():
        with open(ISO_BUNDLE, "r", encoding="utf-8") as f:
            iso_data = json.load(f)
        for obj in iso_data.get("objects", []):
            if obj.get("level") == 1:
                iso_controls[obj["control_id"]] = obj["id"]
        print(f"  Loaded {len(iso_controls)} ISO controls for cross-referencing")

    objects = []
    relationships = []
    sort_counter = 0

    for section in raw["sections"]:
        for group in section["groups"]:
            sort_counter += 1
            gcode = group["group_code"]
            gid = group_uuid(gcode)

            is_stacked = len(group["stacked_control_ids"]) > 1
            all_covered = group["stacked_control_ids"] + group.get("also_covers", [])

            objects.append({
                "type": "control_group",
                "id": gid,
                "group_code": gcode,
                "name": group["name"],
                "section": group["section"],
                "section_name": group["section_name"],
                "folder_name": group["folder_name"],
                "is_stacked": is_stacked,
                "stacked_control_ids": group["stacked_control_ids"],
                "also_covers": group.get("also_covers", []),
                "is_iso_standard": group.get("is_iso_standard", True),
                "has_framework": group.get("has_framework", True),
                "has_operational": group.get("has_operational", True),
                "sort_order": sort_counter,
                "metadata": {
                    "notes": group.get("notes", "")
                }
            })

            # Containment relationships: group → ISO control
            for ctrl_id in all_covered:
                # Try to resolve to ISO bundle UUID, fall back to computed UUID
                ctrl_uuid = iso_controls.get(
                    ctrl_id,
                    control_uuid("ISO27001_2022", ctrl_id)
                )
                rel_type = "contains" if ctrl_id in group["stacked_control_ids"] else "also-covers"
                relationships.append({
                    "type": "containment",
                    "source_id": gid,
                    "target_id": ctrl_uuid,
                    "relationship_type": rel_type,
                    "target_control_id": ctrl_id
                })

    # Compute content hash
    content_str = json.dumps(objects, sort_keys=True)
    content_hash = hashlib.sha256(content_str.encode()).hexdigest()

    bundle = {
        "bundle_id": f"bundle--{stable_uuid(f'bundle:control_groups:{content_hash[:16]}')}",
        "bundle_type": "isms-core-dataset",
        "bundle_version": "1.0",
        "dataset": {
            "name": raw["isms_core"]["name"],
            "description": raw["isms_core"]["description"],
            "version": raw["isms_core"]["version"],
            "total_groups": raw["isms_core"]["total_groups"],
            "iso_groups": raw["isms_core"].get("iso_groups", 53),
            "total_iso_controls_covered": raw["isms_core"]["total_iso_controls_covered"],
            "products": raw["isms_core"]["products"]
        },
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "generate_control_groups.py",
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

    print(f"Generated {OUTPUT_FILE.name}:")
    print(f"  Control groups:  {bundle['objects_count']}")
    print(f"  Relationships:   {bundle['relationships_count']}")
    print(f"  Content hash:    {bundle['content_hash'][:16]}...")
    print(f"  Written to:      {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
