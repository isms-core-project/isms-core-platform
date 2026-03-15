#!/usr/bin/env python3
"""
Generate ISO 27001:2022 dataset bundle from raw controls data.

Pipeline: raw/iso27001_2022_controls.json → data/iso27001_2022.json

Follows OpenCTI datasets pattern: raw source → generator → stable-ID bundle.
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
RAW_FILE = RAW_DIR / "iso27001_2022_controls.json"
OUTPUT_FILE = DATA_DIR / "iso27001_2022.json"

# =============================================================================
# UUID STRATEGY
# =============================================================================
# Deterministic UUID5 using a fixed ISMS CORE namespace
ISMS_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")  # URL namespace


def stable_uuid(key: str) -> str:
    """Generate deterministic UUID5 from a stable key."""
    return str(uuid.uuid5(ISMS_NAMESPACE, key))


def framework_uuid(code: str) -> str:
    """UUID for a framework entity."""
    return stable_uuid(f"framework:{code}")


def control_uuid(framework_code: str, control_id: str) -> str:
    """UUID for a framework control entity."""
    return stable_uuid(f"control:{framework_code}:{control_id}")


def section_uuid(framework_code: str, section_id: str) -> str:
    """UUID for a section (level-0) entity."""
    return stable_uuid(f"section:{framework_code}:{section_id}")


# =============================================================================
# GENERATOR
# =============================================================================
def generate_bundle() -> dict:
    """Read raw ISO 27001 data and produce a stable-ID bundle."""

    with open(RAW_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    framework_info = raw["framework"]
    framework_code = framework_info["code"]
    fw_id = framework_uuid(framework_code)

    objects = []
    relationships = []
    sort_counter = 0

    for section in raw["sections"]:
        section_id = section["id"]
        section_name = section["name"]

        # Create section object (level 0)
        sec_uuid = section_uuid(framework_code, section_id)
        sort_counter += 1
        objects.append({
            "type": "framework_control",
            "id": sec_uuid,
            "framework_id": fw_id,
            "control_id": section_id,
            "title": section_name,
            "level": 0,
            "sort_order": sort_counter * 1000,
            "metadata": {
                "section": section_id,
                "category": section_name,
                "controls_count": section["controls_count"]
            }
        })

        # Create control objects (level 1)
        for i, ctrl in enumerate(section["controls"]):
            ctrl_uuid = control_uuid(framework_code, ctrl["control_id"])
            objects.append({
                "type": "framework_control",
                "id": ctrl_uuid,
                "framework_id": fw_id,
                "parent_id": sec_uuid,
                "control_id": ctrl["control_id"],
                "title": ctrl["title"],
                "level": 1,
                "sort_order": sort_counter * 1000 + (i + 1),
                "control_type": ctrl.get("control_type", []),
                "security_properties": ctrl.get("security_properties", []),
                "metadata": {
                    "section": section_id,
                    "category": section_name,
                    "cybersecurity_concepts": ctrl.get("cybersecurity_concepts", []),
                    "operational_capabilities": ctrl.get("operational_capabilities", []),
                    "security_domains": ctrl.get("security_domains", [])
                }
            })

            # Hierarchy relationship: control → section
            relationships.append({
                "type": "hierarchy",
                "source_id": ctrl_uuid,
                "target_id": sec_uuid,
                "relationship_type": "part-of"
            })

    # Compute content hash for change detection
    content_str = json.dumps(objects, sort_keys=True)
    content_hash = hashlib.sha256(content_str.encode()).hexdigest()

    bundle = {
        "bundle_id": f"bundle--{stable_uuid(f'bundle:iso27001_2022:{content_hash[:16]}')}",
        "bundle_type": "isms-core-dataset",
        "bundle_version": "1.0",
        "framework": {
            "id": fw_id,
            "code": framework_code,
            "name": framework_info["name"],
            "version": framework_info["version"],
            "publisher": framework_info["publisher"],
            "source_url": framework_info["source_url"],
            "description": framework_info["description"]
        },
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "generate_iso27001.py",
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
    print(f"  Objects:       {bundle['objects_count']}")
    print(f"  Relationships: {bundle['relationships_count']}")
    print(f"  Content hash:  {bundle['content_hash'][:16]}...")
    print(f"  Written to:    {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
