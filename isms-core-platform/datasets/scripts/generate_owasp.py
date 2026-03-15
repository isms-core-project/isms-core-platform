#!/usr/bin/env python3
"""
Generate OWASP dataset bundle from raw Top 10 and ASVS data.

Pipeline:
  raw/owasp_top10_2025.json + raw/owasp_asvs_4.0.3.json → data/owasp.json

Two sub-frameworks in one bundle:
  - OWASP Top 10:2025 (10 categories with CWE mappings and statistics)
  - OWASP ASVS 4.0.3 (14 chapters, ~278 active requirements)
"""

import json
import uuid
import hashlib
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RAW_DIR = SCRIPT_DIR.parent / "raw"
DATA_DIR = SCRIPT_DIR.parent / "data"
TOP10_FILE = RAW_DIR / "owasp_top10_2025.json"
ASVS_FILE = RAW_DIR / "owasp_asvs_4.0.3.json"
OUTPUT_FILE = DATA_DIR / "owasp.json"

ISMS_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")


def stable_uuid(key: str) -> str:
    return str(uuid.uuid5(ISMS_NAMESPACE, key))


def control_uuid(fw_code: str, control_id: str) -> str:
    return stable_uuid(f"control:{fw_code}:{control_id}")


def generate_bundle() -> dict:
    objects = []
    relationships = []

    # =========================================================================
    # OWASP TOP 10:2025
    # =========================================================================
    top10_fw_code = "OWASP_TOP10_2025"
    top10_fw_id = stable_uuid(f"framework:{top10_fw_code}")

    with open(TOP10_FILE, "r", encoding="utf-8") as f:
        top10_raw = json.load(f)

    for i, cat in enumerate(top10_raw["categories"]):
        cat_id = cat["id"]
        cat_uuid = control_uuid(top10_fw_code, cat_id)

        objects.append({
            "type": "framework_control",
            "id": cat_uuid,
            "framework_id": top10_fw_id,
            "control_id": cat_id,
            "title": cat["name"],
            "description": cat["description"],
            "level": 0,
            "sort_order": (i + 1) * 100,
            "metadata": {
                "sub_framework": "top10",
                "cwes_mapped": cat.get("cwes_mapped", 0),
                "notable_cwes": cat.get("notable_cwes", []),
                "total_occurrences": cat.get("total_occurrences"),
                "total_cves": cat.get("total_cves"),
                "max_incidence_rate": cat.get("max_incidence_rate"),
                "avg_incidence_rate": cat.get("avg_incidence_rate"),
                "previous": cat.get("previous")
            }
        })

    print(f"  Top 10: {len(top10_raw['categories'])} categories")

    # =========================================================================
    # OWASP ASVS 4.0.3
    # =========================================================================
    asvs_fw_code = "OWASP_ASVS_4.0"
    asvs_fw_id = stable_uuid(f"framework:{asvs_fw_code}")

    if ASVS_FILE.exists():
        with open(ASVS_FILE, "r", encoding="utf-8") as f:
            asvs_raw = json.load(f)

        # ASVS JSON structure: {Requirements: [{Shortcode: "V1", Items: [{Shortcode: "V1.1", Items: [{...}]}]}]}
        asvs_chapters = asvs_raw.get("Requirements", [])
        total_reqs = 0

        for i, chapter in enumerate(asvs_chapters):
            chap_id = chapter["Shortcode"]
            chap_name = chapter.get("Name", chap_id)
            chap_uuid = control_uuid(asvs_fw_code, chap_id)

            # Flatten all requirements from nested sections
            flat_reqs = []
            for section in chapter.get("Items", []):
                for req in section.get("Items", []):
                    desc = req.get("Description", "")
                    if "DELETED" in desc or "DUPLICATE" in desc:
                        continue
                    flat_reqs.append(req)

            objects.append({
                "type": "framework_control",
                "id": chap_uuid,
                "framework_id": asvs_fw_id,
                "control_id": chap_id,
                "title": chap_name,
                "level": 0,
                "sort_order": 10000 + (i + 1) * 1000,
                "metadata": {
                    "sub_framework": "asvs",
                    "requirements_count": len(flat_reqs)
                }
            })

            for j, req in enumerate(flat_reqs):
                req_id = req.get("Shortcode", "")
                req_uuid = control_uuid(asvs_fw_code, req_id)
                desc = req.get("Description", "")

                l1 = req.get("L1", {})
                l2 = req.get("L2", {})
                l3 = req.get("L3", {})

                levels = []
                if _is_required(l1.get("Required") if isinstance(l1, dict) else l1):
                    levels.append("L1")
                if _is_required(l2.get("Required") if isinstance(l2, dict) else l2):
                    levels.append("L2")
                if _is_required(l3.get("Required") if isinstance(l3, dict) else l3):
                    levels.append("L3")

                cwe_val = req.get("CWE", [])
                if isinstance(cwe_val, list):
                    cwes = [int(c) for c in cwe_val if str(c).isdigit()]
                else:
                    cwe_str = str(cwe_val)
                    cwes = [int(c.strip()) for c in cwe_str.split(",") if c.strip().isdigit()]

                nist_val = req.get("NIST", "")

                objects.append({
                    "type": "framework_control",
                    "id": req_uuid,
                    "framework_id": asvs_fw_id,
                    "parent_id": chap_uuid,
                    "control_id": req_id,
                    "title": desc[:200] if desc else req_id,
                    "description": desc,
                    "level": 1,
                    "sort_order": 10000 + (i + 1) * 1000 + (j + 1),
                    "metadata": {
                        "sub_framework": "asvs",
                        "verification_levels": levels,
                        "cwes": cwes,
                        "nist_mapping": nist_val
                    }
                })

                relationships.append({
                    "type": "hierarchy",
                    "source_id": req_uuid,
                    "target_id": chap_uuid,
                    "relationship_type": "part-of"
                })

            total_reqs += len(flat_reqs)

        print(f"  ASVS: {len(asvs_chapters)} chapters, {total_reqs} requirements")
    else:
        print(f"  WARNING: ASVS file not found at {ASVS_FILE}")

    # =========================================================================
    # BUNDLE
    # =========================================================================
    content_str = json.dumps(objects, sort_keys=True)
    content_hash = hashlib.sha256(content_str.encode()).hexdigest()

    top10_count = len([o for o in objects if o.get("metadata", {}).get("sub_framework") == "top10"])
    asvs_count = len([o for o in objects if o.get("metadata", {}).get("sub_framework") == "asvs"])

    bundle = {
        "bundle_id": f"bundle--{stable_uuid(f'bundle:owasp:{content_hash[:16]}')}",
        "bundle_type": "isms-core-dataset",
        "bundle_version": "1.0",
        "frameworks": [
            {
                "id": top10_fw_id,
                "code": top10_fw_code,
                "name": "OWASP Top 10:2025",
                "version": "2025",
                "publisher": "OWASP Foundation",
                "source_url": "https://owasp.org/Top10/2025/",
                "description": "Top 10 Web Application Security Risks (2025 edition)"
            },
            {
                "id": asvs_fw_id,
                "code": asvs_fw_code,
                "name": "OWASP ASVS",
                "version": "4.0.3",
                "publisher": "OWASP Foundation",
                "source_url": "https://owasp.org/www-project-application-security-verification-standard/",
                "description": "Application Security Verification Standard"
            }
        ],
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "generate_owasp.py",
        "content_hash": content_hash,
        "top10_objects": top10_count,
        "asvs_objects": asvs_count,
        "objects_count": len(objects),
        "relationships_count": len(relationships),
        "objects": objects,
        "relationships": relationships
    }

    return bundle


def _is_required(val) -> bool:
    """Check if an ASVS level marker indicates required."""
    if isinstance(val, bool):
        return val
    s = str(val).strip().upper()
    return s in ("X", "✓", "TRUE", "1", "YES", "REQUIRED")


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Reading raw data from {TOP10_FILE} and {ASVS_FILE}")
    bundle = generate_bundle()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)

    print(f"Generated {OUTPUT_FILE.name}:")
    print(f"  Top 10 objects: {bundle['top10_objects']}")
    print(f"  ASVS objects:   {bundle['asvs_objects']}")
    print(f"  Total objects:  {bundle['objects_count']}")
    print(f"  Relationships:  {bundle['relationships_count']}")
    print(f"  Content hash:   {bundle['content_hash'][:16]}...")


if __name__ == "__main__":
    main()
