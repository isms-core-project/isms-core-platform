#!/usr/bin/env python3
"""
Generate regulatory framework dataset bundles from raw data.

Pipeline: raw/{framework}.json → data/{framework}.json

Processes all Tier 3 regulatory frameworks:
  - Swiss nFADP (nDSG) — 11 articles
  - EU GDPR — 16 articles
  - FINMA (3 circulars) — 21 sections
  - NIS2 Directive — 14 articles
  - DORA — 4 chapters, 26 articles
  - PCI DSS v4.0.1 — 6 objectives, 12 requirements
  - EU AI Act — 9 articles
  - US CLOUD Act — 5 provisions (info/awareness only)

ISO 27000-family extensions (sections → controls hierarchy):
  - ISO 27017:2015 — Cloud Services Security (12 controls)
  - ISO 27018:2019 — PII Protection in Public Cloud (16 controls)
  - ISO 27701:2019 — Privacy Information Management (18 controls)
"""

import json
import uuid
import hashlib
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RAW_DIR = SCRIPT_DIR.parent / "raw"
DATA_DIR = SCRIPT_DIR.parent / "data"

ISMS_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")


def stable_uuid(key: str) -> str:
    return str(uuid.uuid5(ISMS_NAMESPACE, key))


def control_uuid(fw_code: str, control_id: str) -> str:
    return stable_uuid(f"control:{fw_code}:{control_id}")


def section_uuid(fw_code: str, section_id: str) -> str:
    return stable_uuid(f"section:{fw_code}:{section_id}")


def make_bundle(fw_code: str, fw_meta: dict, objects: list, relationships: list,
                generator_name: str = "generate_regulatory.py") -> dict:
    content_str = json.dumps(objects, sort_keys=True)
    content_hash = hashlib.sha256(content_str.encode()).hexdigest()

    return {
        "bundle_id": f"bundle--{stable_uuid(f'bundle:{fw_code}:{content_hash[:16]}')}",
        "bundle_type": "isms-core-dataset",
        "bundle_version": "1.0",
        "framework": {
            "id": stable_uuid(f"framework:{fw_code}"),
            **fw_meta
        },
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": generator_name,
        "content_hash": content_hash,
        "objects_count": len(objects),
        "relationships_count": len(relationships),
        "objects": objects,
        "relationships": relationships
    }


# =============================================================================
# FLAT ARTICLE FRAMEWORKS (Swiss nFADP, EU GDPR, NIS2, EU AI Act, CLOUD Act)
# =============================================================================
def generate_flat_articles(raw_file: Path, fw_code: str, articles_key: str = "articles") -> dict:
    """Generate bundle from a framework with a flat list of articles/provisions."""
    with open(raw_file, "r", encoding="utf-8") as f:
        raw = json.load(f)

    fw_info = raw["framework"]
    fw_id = stable_uuid(f"framework:{fw_code}")
    objects = []

    items = raw.get(articles_key, [])
    for i, item in enumerate(items):
        item_id = item["id"]
        item_uuid = control_uuid(fw_code, item_id)

        obj = {
            "type": "framework_control",
            "id": item_uuid,
            "framework_id": fw_id,
            "control_id": item_id,
            "title": item["title"],
            "description": item["description"],
            "level": 0,
            "sort_order": (i + 1) * 100
        }

        # Preserve extra metadata fields
        extra = {}
        for key in item:
            if key not in ("id", "title", "description"):
                extra[key] = item[key]
        if extra:
            obj["metadata"] = extra

        objects.append(obj)

    return make_bundle(
        fw_code,
        {
            "code": fw_code,
            "name": fw_info["name"],
            "version": fw_info["version"],
            "publisher": fw_info["publisher"],
            "source_url": fw_info.get("source_url", ""),
            "jurisdiction": fw_info.get("jurisdiction", ""),
            "description": fw_info.get("description", fw_info["name"])
        },
        objects,
        []  # flat structure = no hierarchy relationships
    )


# =============================================================================
# FINMA (3 sub-frameworks in one file)
# =============================================================================
def generate_finma(raw_file: Path) -> dict:
    fw_code = "FINMA"
    with open(raw_file, "r", encoding="utf-8") as f:
        raw = json.load(f)

    fw_id = stable_uuid(f"framework:{fw_code}")
    objects = []
    relationships = []
    sort_counter = 0

    for sub_fw in raw["frameworks"]:
        sub_code = sub_fw["code"]
        sub_uuid = section_uuid(fw_code, sub_code)
        sort_counter += 1

        # Sub-framework as level 0 container
        objects.append({
            "type": "framework_control",
            "id": sub_uuid,
            "framework_id": fw_id,
            "control_id": sub_code,
            "title": sub_fw["name"],
            "description": f"{sub_fw['name']} ({sub_fw['version']})",
            "level": 0,
            "sort_order": sort_counter * 10000,
            "metadata": {
                "sub_framework": sub_code,
                "version": sub_fw["version"],
                "effective_date": sub_fw.get("effective_date", ""),
                "source_url": sub_fw.get("source_url", "")
            }
        })

        # Sections/principles as level 1
        items_key = None
        for key in ("requirements", "principles", "sections"):
            if key in sub_fw:
                items_key = key
                break

        if items_key:
            for j, item in enumerate(sub_fw[items_key]):
                item_id = item["id"]
                item_uuid = control_uuid(fw_code, f"{sub_code}:{item_id}")
                sort_counter += 1

                objects.append({
                    "type": "framework_control",
                    "id": item_uuid,
                    "framework_id": fw_id,
                    "parent_id": sub_uuid,
                    "control_id": item_id,
                    "title": item["title"],
                    "description": item["description"],
                    "level": 1,
                    "sort_order": sort_counter * 100,
                    "metadata": {
                        "sub_framework": sub_code
                    }
                })

                relationships.append({
                    "type": "hierarchy",
                    "source_id": item_uuid,
                    "target_id": sub_uuid,
                    "relationship_type": "part-of"
                })

    return make_bundle(
        fw_code,
        {
            "code": fw_code,
            "name": "FINMA Regulatory Requirements",
            "version": "2024",
            "publisher": "Swiss Financial Market Supervisory Authority (FINMA)",
            "source_url": "https://www.finma.ch/en/documentation/",
            "jurisdiction": "CH",
            "description": "FINMA circulars and guidance for operational resilience, outsourcing, and cyber risks"
        },
        objects,
        relationships
    )


# =============================================================================
# DORA (chapters → articles hierarchy)
# =============================================================================
def generate_dora(raw_file: Path) -> dict:
    fw_code = "DORA"
    with open(raw_file, "r", encoding="utf-8") as f:
        raw = json.load(f)

    fw_info = raw["framework"]
    fw_id = stable_uuid(f"framework:{fw_code}")
    objects = []
    relationships = []
    sort_counter = 0

    for chapter in raw["chapters"]:
        chap_id = chapter["id"]
        chap_uuid = section_uuid(fw_code, chap_id)
        sort_counter += 1

        # Chapter (level 0)
        objects.append({
            "type": "framework_control",
            "id": chap_uuid,
            "framework_id": fw_id,
            "control_id": chap_id,
            "title": chapter["title"],
            "description": f"DORA {chap_id}: {chapter['title']}",
            "level": 0,
            "sort_order": sort_counter * 10000
        })

        # Articles (level 1)
        for j, art in enumerate(chapter["articles"]):
            art_id = art["id"]
            art_uuid = control_uuid(fw_code, art_id)
            sort_counter += 1

            objects.append({
                "type": "framework_control",
                "id": art_uuid,
                "framework_id": fw_id,
                "parent_id": chap_uuid,
                "control_id": art_id,
                "title": art["title"],
                "description": art["description"],
                "level": 1,
                "sort_order": sort_counter * 100
            })

            relationships.append({
                "type": "hierarchy",
                "source_id": art_uuid,
                "target_id": chap_uuid,
                "relationship_type": "part-of"
            })

    return make_bundle(
        fw_code,
        {
            "code": fw_code,
            "name": fw_info["name"],
            "version": fw_info["version"],
            "publisher": fw_info["publisher"],
            "source_url": fw_info.get("source_url", ""),
            "jurisdiction": fw_info.get("jurisdiction", "EU"),
            "description": "Digital Operational Resilience Act — ICT risk management for financial entities"
        },
        objects,
        relationships
    )


# =============================================================================
# PCI DSS (control objectives → requirements hierarchy)
# =============================================================================
def generate_pci_dss(raw_file: Path) -> dict:
    fw_code = "PCI_DSS_4.0.1"
    with open(raw_file, "r", encoding="utf-8") as f:
        raw = json.load(f)

    fw_info = raw["framework"]
    fw_id = stable_uuid(f"framework:{fw_code}")
    objects = []
    relationships = []
    sort_counter = 0

    # Build objective lookup for parent linkage
    objective_uuids = {}
    for co in raw["control_objectives"]:
        co_id = co["id"]
        co_uuid = section_uuid(fw_code, co_id)
        objective_uuids[co_id] = co_uuid
        sort_counter += 1

        objects.append({
            "type": "framework_control",
            "id": co_uuid,
            "framework_id": fw_id,
            "control_id": co_id,
            "title": co["name"],
            "description": f"PCI DSS Control Objective: {co['name']}",
            "level": 0,
            "sort_order": sort_counter * 10000,
            "metadata": {
                "requirements": co["requirements"]
            }
        })

    # Map requirement numbers to their parent objectives
    req_to_objective = {}
    for co in raw["control_objectives"]:
        for req_num in co["requirements"]:
            req_to_objective[req_num] = co["id"]

    for req in raw["requirements"]:
        req_id = req["id"]
        req_uuid = control_uuid(fw_code, req_id)
        sort_counter += 1

        # Find parent objective
        req_num = req_id.replace("Req. ", "")
        parent_co_id = req_to_objective.get(req_num)
        parent_uuid = objective_uuids.get(parent_co_id) if parent_co_id else None

        obj = {
            "type": "framework_control",
            "id": req_uuid,
            "framework_id": fw_id,
            "control_id": req_id,
            "title": req["title"],
            "description": req["description"],
            "level": 1,
            "sort_order": sort_counter * 100,
            "metadata": {
                "sub_requirements": req.get("sub_requirements", [])
            }
        }
        if parent_uuid:
            obj["parent_id"] = parent_uuid

        objects.append(obj)

        if parent_uuid:
            relationships.append({
                "type": "hierarchy",
                "source_id": req_uuid,
                "target_id": parent_uuid,
                "relationship_type": "part-of"
            })

    return make_bundle(
        fw_code,
        {
            "code": fw_code,
            "name": fw_info["name"],
            "version": fw_info["version"],
            "publisher": fw_info["publisher"],
            "source_url": fw_info.get("source_url", ""),
            "jurisdiction": "Global",
            "description": "Payment Card Industry Data Security Standard v4.0.1"
        },
        objects,
        relationships
    )


# =============================================================================
# ISO 27000-FAMILY EXTENSIONS (sections → controls hierarchy)
# =============================================================================
def generate_iso_extension(raw_file: Path, fw_code: str) -> dict:
    """Generate bundle from ISO 27000-family extension standards.

    Structure: sections (level 0) → controls (level 1).
    Controls carry maps_to_iso27001_2022, gdpr_ref, keywords in metadata.
    """
    with open(raw_file, "r", encoding="utf-8") as f:
        raw = json.load(f)

    fw_info = raw["framework"]
    fw_id = stable_uuid(f"framework:{fw_code}")
    objects = []
    relationships = []
    sort_counter = 0

    # Build section UUID lookup
    section_uuids = {}
    for sec in raw.get("sections", []):
        sec_id = sec["id"]
        sec_uuid = section_uuid(fw_code, sec_id)
        section_uuids[sec_id] = sec_uuid
        sort_counter += 1

        objects.append({
            "type": "framework_control",
            "id": sec_uuid,
            "framework_id": fw_id,
            "control_id": sec_id,
            "title": sec["title"],
            "description": sec.get("description", sec["title"]),
            "level": 0,
            "sort_order": sort_counter * 10000
        })

    # Controls as level 1 under their section
    for ctrl in raw.get("controls", []):
        ctrl_id = ctrl["id"]
        ctrl_uuid = control_uuid(fw_code, ctrl_id)
        parent_sec_id = str(ctrl.get("section", ""))
        parent_uuid = section_uuids.get(parent_sec_id)
        sort_counter += 1

        obj = {
            "type": "framework_control",
            "id": ctrl_uuid,
            "framework_id": fw_id,
            "control_id": ctrl_id,
            "title": ctrl["title"],
            "description": ctrl["description"],
            "level": 1,
            "sort_order": sort_counter * 100,
            "metadata": {}
        }
        if parent_uuid:
            obj["parent_id"] = parent_uuid

        # Preserve extension-specific fields
        for key in ("maps_to_iso27001_2022", "gdpr_ref", "keywords", "applicability"):
            if key in ctrl:
                obj["metadata"][key] = ctrl[key]

        objects.append(obj)

        if parent_uuid:
            relationships.append({
                "type": "hierarchy",
                "source_id": ctrl_uuid,
                "target_id": parent_uuid,
                "relationship_type": "part-of"
            })

    return make_bundle(
        fw_code,
        {
            "code": fw_code,
            "name": fw_info["name"],
            "version": fw_info["version"],
            "publisher": fw_info["publisher"],
            "source_url": fw_info.get("source_url", ""),
            "jurisdiction": None if fw_info.get("jurisdiction", "").lower() in ("international", "global") else fw_info.get("jurisdiction"),
            "description": fw_info.get("notes", fw_info["name"])
        },
        objects,
        relationships
    )


# =============================================================================
# MAIN
# =============================================================================
FRAMEWORKS = [
    {
        "name": "Swiss nFADP",
        "raw_file": "swiss_ndsg.json",
        "output_file": "swiss_ndsg.json",
        "fw_code": "SWISS_NDSG",
        "generator": "flat",
        "articles_key": "articles"
    },
    {
        "name": "EU GDPR",
        "raw_file": "eu_gdpr.json",
        "output_file": "eu_gdpr.json",
        "fw_code": "EU_GDPR",
        "generator": "flat",
        "articles_key": "articles"
    },
    {
        "name": "NIS2",
        "raw_file": "nis2.json",
        "output_file": "nis2.json",
        "fw_code": "NIS2",
        "generator": "flat",
        "articles_key": "articles"
    },
    {
        "name": "EU AI Act",
        "raw_file": "eu_ai_act.json",
        "output_file": "eu_ai_act.json",
        "fw_code": "EU_AI_ACT",
        "generator": "flat",
        "articles_key": "articles"
    },
    {
        "name": "US CLOUD Act",
        "raw_file": "us_cloud_act.json",
        "output_file": "us_cloud_act.json",
        "fw_code": "US_CLOUD_ACT",
        "generator": "flat",
        "articles_key": "provisions"
    },
    {
        "name": "FINMA",
        "raw_file": "finma.json",
        "output_file": "finma.json",
        "fw_code": "FINMA",
        "generator": "finma"
    },
    {
        "name": "DORA",
        "raw_file": "dora.json",
        "output_file": "dora.json",
        "fw_code": "DORA",
        "generator": "dora"
    },
    {
        "name": "PCI DSS v4.0.1",
        "raw_file": "pci_dss_v4.json",
        "output_file": "pci_dss_v4.json",
        "fw_code": "PCI_DSS_4.0.1",
        "generator": "pci_dss"
    },
    {
        "name": "ISO 27017 Cloud Security",
        "raw_file": "iso27017_cloud.json",
        "output_file": "iso27017_cloud.json",
        "fw_code": "ISO27017",
        "generator": "iso_extension"
    },
    {
        "name": "ISO 27018 PII in Public Cloud",
        "raw_file": "iso27018_pii_cloud.json",
        "output_file": "iso27018_pii_cloud.json",
        "fw_code": "ISO27018",
        "generator": "iso_extension"
    },
    {
        "name": "ISO 27701 Privacy Management",
        "raw_file": "iso27701_privacy.json",
        "output_file": "iso27701_privacy.json",
        "fw_code": "ISO27701",
        "generator": "iso_extension"
    }
]


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    total_objects = 0
    total_rels = 0

    for fw in FRAMEWORKS:
        raw_file = RAW_DIR / fw["raw_file"]
        output_file = DATA_DIR / fw["output_file"]

        if not raw_file.exists():
            print(f"  SKIP {fw['name']}: {raw_file.name} not found")
            continue

        gen_type = fw["generator"]
        if gen_type == "flat":
            bundle = generate_flat_articles(raw_file, fw["fw_code"], fw.get("articles_key", "articles"))
        elif gen_type == "finma":
            bundle = generate_finma(raw_file)
        elif gen_type == "dora":
            bundle = generate_dora(raw_file)
        elif gen_type == "pci_dss":
            bundle = generate_pci_dss(raw_file)
        elif gen_type == "iso_extension":
            bundle = generate_iso_extension(raw_file, fw["fw_code"])
        else:
            print(f"  SKIP {fw['name']}: unknown generator type '{gen_type}'")
            continue

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(bundle, f, indent=2, ensure_ascii=False)

        obj_count = bundle["objects_count"]
        rel_count = bundle["relationships_count"]
        total_objects += obj_count
        total_rels += rel_count

        print(f"  {fw['name']:20s} → {output_file.name:25s}  {obj_count:4d} objects, {rel_count:4d} relationships")

    print(f"\n  TOTAL: {total_objects} objects, {total_rels} relationships across {len(FRAMEWORKS)} frameworks")


if __name__ == "__main__":
    main()
