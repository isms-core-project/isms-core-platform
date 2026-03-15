#!/usr/bin/env python3
"""
Generate NIST SP 800-53 Rev 5 dataset bundle from structured OSCAL extract.

Pipeline: raw/nist_sp800_53r5.json → data/nist_sp800_53r5.json

1,196 controls across 20 families with baseline classification.
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
RAW_FILE = RAW_DIR / "nist_sp800_53r5.json"
OUTPUT_FILE = DATA_DIR / "nist_sp800_53r5.json"

# =============================================================================
# UUID STRATEGY
# =============================================================================
ISMS_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
FRAMEWORK_CODE = "NIST_800_53_R5"


def stable_uuid(key: str) -> str:
    return str(uuid.uuid5(ISMS_NAMESPACE, key))


def framework_uuid() -> str:
    return stable_uuid(f"framework:{FRAMEWORK_CODE}")


def control_uuid(control_id: str) -> str:
    return stable_uuid(f"control:{FRAMEWORK_CODE}:{control_id}")


def family_uuid(family_id: str) -> str:
    return stable_uuid(f"section:{FRAMEWORK_CODE}:{family_id}")


# =============================================================================
# GENERATOR
# =============================================================================
def generate_bundle() -> dict:
    with open(RAW_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    fw_id = framework_uuid()
    summary = raw["summary"]

    objects = []
    relationships = []

    # Build family lookup
    family_map = {}
    for i, fam in enumerate(raw["families"]):
        fam_id = fam["family_id"]
        fam_uuid = family_uuid(fam_id)
        family_map[fam_id] = fam_uuid

        objects.append({
            "type": "framework_control",
            "id": fam_uuid,
            "framework_id": fw_id,
            "control_id": fam_id,
            "title": fam["family_title"],
            "level": 0,
            "sort_order": (i + 1) * 10000,
            "metadata": {
                "family": fam_id,
                "family_title": fam["family_title"],
                "base_control_count": fam["base_control_count"],
                "enhancement_count": fam["enhancement_count"],
                "total_count": fam["total_count"]
            }
        })

    # Process controls
    for ctrl in raw["controls"]:
        ctrl_id = ctrl["control_id"]
        ctrl_uuid_val = control_uuid(ctrl_id)
        fam_id = ctrl["family_id"]
        is_enhancement = ctrl.get("is_enhancement", False)
        parent_ctrl = ctrl.get("parent_control")

        # Determine parent
        if is_enhancement and parent_ctrl:
            parent_id = control_uuid(parent_ctrl)
        else:
            parent_id = family_map.get(fam_id)

        level = 2 if is_enhancement else 1

        # Parse sort_id for ordering
        sort_id = ctrl.get("sort_id", ctrl_id.lower())

        objects.append({
            "type": "framework_control",
            "id": ctrl_uuid_val,
            "framework_id": fw_id,
            "parent_id": parent_id,
            "control_id": ctrl_id,
            "title": ctrl["title"],
            "level": level,
            "sort_order": _sort_key(sort_id),
            "metadata": {
                "family": fam_id,
                "is_enhancement": is_enhancement,
                "parent_control": parent_ctrl,
                "baseline_low": ctrl.get("baseline_low", False),
                "baseline_moderate": ctrl.get("baseline_moderate", False),
                "baseline_high": ctrl.get("baseline_high", False),
                "label": ctrl.get("label", ctrl_id),
                "sort_id": sort_id
            }
        })

        # Hierarchy relationship
        if parent_id:
            relationships.append({
                "type": "hierarchy",
                "source_id": ctrl_uuid_val,
                "target_id": parent_id,
                "relationship_type": "part-of"
            })

    content_str = json.dumps(objects, sort_keys=True)
    content_hash = hashlib.sha256(content_str.encode()).hexdigest()

    bundle = {
        "bundle_id": f"bundle--{stable_uuid(f'bundle:nist_800_53:{content_hash[:16]}')}",
        "bundle_type": "isms-core-dataset",
        "bundle_version": "1.0",
        "framework": {
            "id": fw_id,
            "code": FRAMEWORK_CODE,
            "name": "NIST SP 800-53 Rev 5",
            "version": raw.get("version", "5.2.0"),
            "publisher": "NIST",
            "source_url": "https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final",
            "description": "Security and Privacy Controls for Information Systems and Organizations"
        },
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "generate_nist_800_53.py",
        "content_hash": content_hash,
        "summary": summary,
        "objects_count": len(objects),
        "relationships_count": len(relationships),
        "objects": objects,
        "relationships": relationships
    }

    return bundle


def _sort_key(sort_id: str) -> int:
    """Convert sort_id like 'ac-02.01' to numeric sort key."""
    parts = sort_id.replace(".", "-").split("-")
    result = 0
    for i, part in enumerate(parts):
        try:
            result = result * 100 + int(part)
        except ValueError:
            result = result * 100 + sum(ord(c) for c in part) % 100
    return result


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Reading raw data from {RAW_FILE}")
    bundle = generate_bundle()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)

    families = len([o for o in bundle["objects"] if o["level"] == 0])
    controls = len([o for o in bundle["objects"] if o["level"] == 1])
    enhancements = len([o for o in bundle["objects"] if o["level"] == 2])

    print(f"Generated {OUTPUT_FILE.name}:")
    print(f"  Families:       {families}")
    print(f"  Controls:       {controls}")
    print(f"  Enhancements:   {enhancements}")
    print(f"  Total objects:  {bundle['objects_count']}")
    print(f"  Relationships:  {bundle['relationships_count']}")
    print(f"  Content hash:   {bundle['content_hash'][:16]}...")


if __name__ == "__main__":
    main()
