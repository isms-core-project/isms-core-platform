#!/usr/bin/env python3
"""
Generate NIST CSF 2.0 dataset bundle from raw data.

Pipeline: raw/nist_csf_2.0.json → data/nist_csf_2.0.json

NIST Cybersecurity Framework 2.0: 6 functions, 22 categories, 106 subcategories.
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
RAW_FILE = RAW_DIR / "nist_csf_2.0.json"
OUTPUT_FILE = DATA_DIR / "nist_csf_2.0.json"

# =============================================================================
# UUID STRATEGY
# =============================================================================
ISMS_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
FRAMEWORK_CODE = "NIST_CSF_2.0"


def stable_uuid(key: str) -> str:
    return str(uuid.uuid5(ISMS_NAMESPACE, key))


def framework_uuid() -> str:
    return stable_uuid(f"framework:{FRAMEWORK_CODE}")


def control_uuid(control_id: str) -> str:
    return stable_uuid(f"control:{FRAMEWORK_CODE}:{control_id}")


# =============================================================================
# GENERATOR
# =============================================================================
def generate_bundle() -> dict:
    with open(RAW_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    fw_info = raw["framework"]
    fw_id = framework_uuid()

    objects = []
    relationships = []
    sort_counter = 0

    for func in raw["functions"]:
        func_id = func["id"]
        func_uuid = control_uuid(func_id)
        sort_counter += 1

        # Function (level 0)
        objects.append({
            "type": "framework_control",
            "id": func_uuid,
            "framework_id": fw_id,
            "control_id": func_id,
            "title": func["name"],
            "description": func["description"],
            "level": 0,
            "sort_order": sort_counter * 10000,
            "metadata": {
                "function": func_id,
                "function_name": func["name"]
            }
        })

        for cat in func["categories"]:
            cat_id = cat["id"]
            cat_uuid = control_uuid(cat_id)
            sort_counter += 1

            # Category (level 1)
            objects.append({
                "type": "framework_control",
                "id": cat_uuid,
                "framework_id": fw_id,
                "parent_id": func_uuid,
                "control_id": cat_id,
                "title": cat["name"],
                "description": cat["description"],
                "level": 1,
                "sort_order": sort_counter * 100,
                "metadata": {
                    "function": func_id,
                    "category": cat_id,
                    "category_name": cat["name"]
                }
            })

            relationships.append({
                "type": "hierarchy",
                "source_id": cat_uuid,
                "target_id": func_uuid,
                "relationship_type": "part-of"
            })

            for subcat in cat["subcategories"]:
                subcat_id = subcat["id"]
                subcat_uuid = control_uuid(subcat_id)
                sort_counter += 1

                # Subcategory (level 2)
                objects.append({
                    "type": "framework_control",
                    "id": subcat_uuid,
                    "framework_id": fw_id,
                    "parent_id": cat_uuid,
                    "control_id": subcat_id,
                    "title": subcat["description"],
                    "level": 2,
                    "sort_order": sort_counter,
                    "metadata": {
                        "function": func_id,
                        "category": cat_id
                    }
                })

                relationships.append({
                    "type": "hierarchy",
                    "source_id": subcat_uuid,
                    "target_id": cat_uuid,
                    "relationship_type": "part-of"
                })

    content_str = json.dumps(objects, sort_keys=True)
    content_hash = hashlib.sha256(content_str.encode()).hexdigest()

    bundle = {
        "bundle_id": f"bundle--{stable_uuid(f'bundle:nist_csf_2.0:{content_hash[:16]}')}",
        "bundle_type": "isms-core-dataset",
        "bundle_version": "1.0",
        "framework": {
            "id": fw_id,
            "code": FRAMEWORK_CODE,
            "name": fw_info["name"],
            "version": fw_info["version"],
            "publisher": "NIST",
            "source_url": fw_info.get("url", "https://www.nist.gov/cyberframework"),
            "description": "NIST Cybersecurity Framework 2.0 — Functions, Categories, and Subcategories"
        },
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "generate_nist_csf.py",
        "content_hash": content_hash,
        "statistics": fw_info.get("statistics", {}),
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

    # Count by level
    funcs = len([o for o in bundle["objects"] if o["level"] == 0])
    cats = len([o for o in bundle["objects"] if o["level"] == 1])
    subcats = len([o for o in bundle["objects"] if o["level"] == 2])

    print(f"Generated {OUTPUT_FILE.name}:")
    print(f"  Functions:      {funcs}")
    print(f"  Categories:     {cats}")
    print(f"  Subcategories:  {subcats}")
    print(f"  Total objects:  {bundle['objects_count']}")
    print(f"  Relationships:  {bundle['relationships_count']}")
    print(f"  Content hash:   {bundle['content_hash'][:16]}...")


if __name__ == "__main__":
    main()
