#!/usr/bin/env python3
"""
Generate ISO 27001 intra-control dependency bundle from raw dependency data.

Pipeline: raw/control_dependencies.json → data/control_dependencies.json

Creates CrossFrameworkMapping objects linking ISO 27001 controls to each other
(intra-framework dependencies). Reuses the same cross_framework_mapping object
type so the bundle loader handles them identically to crosswalk mappings.

Relationship types (all intra-ISO-27001):
  - depends-on    Hard requirement — source cannot function without target
  - enables       Source provides a capability the target consumes
  - feeds-into    Output of source is input to target
  - supports      Source reinforces or supplements target
  - implements    Source is the technical realisation of target policy control
"""

import json
import uuid
import hashlib
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RAW_DIR = SCRIPT_DIR.parent / "raw"
DATA_DIR = SCRIPT_DIR.parent / "data"
RAW_FILE = RAW_DIR / "control_dependencies.json"
OUTPUT_FILE = DATA_DIR / "control_dependencies.json"

ISMS_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")

ISO27001_CODE = "ISO27001_2022"


def stable_uuid(key: str) -> str:
    return str(uuid.uuid5(ISMS_NAMESPACE, key))


def control_uuid(fw_code: str, control_id: str) -> str:
    """Generate the same UUID that individual framework generators produce."""
    return stable_uuid(f"control:{fw_code}:{control_id}")


def mapping_uuid(source_fw: str, source_id: str, target_fw: str, target_id: str, mapping_type: str) -> str:
    """Deterministic UUID for a mapping relationship."""
    source_uuid = control_uuid(source_fw, source_id)
    target_uuid = control_uuid(target_fw, target_id)
    return stable_uuid(f"mapping:{source_uuid}:{target_uuid}:{mapping_type}")


# Map strength labels to confidence scores
STRENGTH_CONFIDENCE = {
    "strong": 0.90,
    "moderate": 0.70,
    "weak": 0.50,
}


def generate_bundle() -> dict:
    with open(RAW_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    objects = []
    stats = {}

    for dep in raw["dependencies"]:
        src_id = dep["source"]
        tgt_id = dep["target"]
        dep_type = dep["type"]
        strength = dep.get("strength", "moderate")
        confidence = STRENGTH_CONFIDENCE.get(strength, 0.70)
        description = dep.get("description", "")

        # Both source and target are ISO 27001 controls
        src_uuid = control_uuid(ISO27001_CODE, src_id)
        tgt_uuid = control_uuid(ISO27001_CODE, tgt_id)
        m_uuid = mapping_uuid(ISO27001_CODE, src_id, ISO27001_CODE, tgt_id, dep_type)

        objects.append({
            "type": "cross_framework_mapping",
            "id": m_uuid,
            "source_control_id": src_uuid,
            "target_control_id": tgt_uuid,
            "source_framework": ISO27001_CODE,
            "source_control": src_id,
            "target_framework": ISO27001_CODE,
            "target_control": tgt_id,
            "mapping_type": dep_type,
            "confidence": confidence,
            "source_reference": "ISO/IEC 27002:2022 implementation guidance",
            "notes": description,
        })

        # Track stats per dependency type
        stats[dep_type] = stats.get(dep_type, 0) + 1

    content_str = json.dumps(objects, sort_keys=True)
    content_hash = hashlib.sha256(content_str.encode()).hexdigest()

    bundle = {
        "bundle_id": f"bundle--{stable_uuid(f'bundle:control_dependencies:{content_hash[:16]}')}",
        "bundle_type": "isms-core-dataset",
        "bundle_version": "1.0",
        "dataset": {
            "name": "ISMS CORE ISO 27001 Control Dependencies",
            "version": "1.0",
            "description": "Intra-framework dependency relationships between ISO 27001:2022 Annex A controls",
        },
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "generate_control_dependencies.py",
        "content_hash": content_hash,
        "objects_count": len(objects),
        "dependency_types": stats,
        "objects": objects,
    }

    return bundle


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not RAW_FILE.exists():
        print(f"ERROR: {RAW_FILE} not found. Create control_dependencies.json first.")
        return

    print(f"Reading control dependencies from {RAW_FILE}")
    bundle = generate_bundle()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)

    print(f"\nGenerated {OUTPUT_FILE.name}:")
    print(f"  Total dependencies: {bundle['objects_count']}")
    print(f"  Content hash:       {bundle['content_hash'][:16]}...")
    print(f"\n  Dependency types:")
    for dep_type, count in sorted(bundle["dependency_types"].items()):
        print(f"    {dep_type:20s} {count:4d}")


if __name__ == "__main__":
    main()
