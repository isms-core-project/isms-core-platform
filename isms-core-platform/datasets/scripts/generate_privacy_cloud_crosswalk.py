#!/usr/bin/env python3
"""
Generate privacy and cloud crosswalk mappings.

Adds new mapping entries to raw/crosswalk_mappings.json covering:
  1. ISO27701 → EU_GDPR          (from crosswalk_indexes.json Annex D inversion)
  2. ISO27701 → ISO27018         (from crosswalk_indexes.json Annex E)
  3. ISO27018 → ISO27701         (from crosswalk_indexes.json Annex E inversion)
  4. ISO27018 → EU_GDPR          (from crosswalk_indexes.json Annex D inversion)
  5. ISO27701 A.3.x → ISO27001   (exact: A.3 controls ARE the 27001 Annex A controls)
  6. ISO27701 A.1.x/A.2.x → ISO27001 (approximate: nearest 27001 controls)
  7. ISO27017 → ISO27001         (from iso27017_cloud.json bundle metadata)
  8. ISO27018 → ISO27001         (from iso27018_pii_cloud.json bundle metadata)

Run after this script:
  python3 datasets/scripts/generate_crosswalk.py
"""

import json
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RAW_DIR = SCRIPT_DIR.parent / "raw"
DATA_DIR = SCRIPT_DIR.parent / "data"

RAW_FILE = RAW_DIR / "crosswalk_mappings.json"
INDEXES_FILE = DATA_DIR / "crosswalk_indexes.json"
ISO27701_FILE = DATA_DIR / "iso27701_privacy.json"
ISO27017_FILE = DATA_DIR / "iso27017_cloud.json"
ISO27018_FILE = DATA_DIR / "iso27018_pii_cloud.json"
EU_GDPR_FILE = DATA_DIR / "eu_gdpr.json"

# GDPR articles present in the EU GDPR dataset (subset of full regulation)
VALID_GDPR_ARTICLES = {
    "Art. 5", "Art. 6", "Art. 24", "Art. 25", "Art. 28",
    "Art. 30", "Art. 32", "Art. 33", "Art. 34", "Art. 35",
    "Art. 36", "Art. 37", "Art. 39", "Art. 44", "Art. 45",
    "Art. 46", "Art. 47", "Art. 48", "Art. 49",
}

# ISO 27701 A.3.x → ISO 27001:2022 Annex A (exact equivalence)
# Source: ISO/IEC 27701:2025 Table A.3 — Security controls for PII controllers and processors
A3_TO_ISO27001 = {
    "A.3.3":  "A.5.1",   # Policies for information security
    "A.3.4":  "A.5.2",   # Information security roles and responsibilities
    "A.3.5":  "A.5.12",  # Classification of information
    "A.3.6":  "A.5.13",  # Labelling of information
    "A.3.7":  "A.5.14",  # Information transfer
    "A.3.8":  "A.5.16",  # Identity management
    "A.3.9":  "A.5.18",  # Access rights
    "A.3.10": "A.5.20",  # Information security in supplier agreements
    "A.3.11": "A.5.24",  # Information security incident management planning
    "A.3.12": "A.5.26",  # Response to information security incidents
    "A.3.13": "A.5.31",  # Legal, statutory, regulatory and contractual requirements
    "A.3.14": "A.5.33",  # Protection of records
    "A.3.15": "A.5.35",  # Independent review of information security
    "A.3.16": "A.5.36",  # Compliance with policies, rules and standards
    "A.3.17": "A.6.3",   # Information security awareness, education and training
    "A.3.18": "A.6.6",   # Confidentiality or non-disclosure agreements
    "A.3.19": "A.7.7",   # Clear desk and clear screen
    "A.3.20": "A.7.10",  # Storage media
    "A.3.21": "A.7.14",  # Secure disposal or re-use of equipment
    "A.3.22": "A.8.1",   # User endpoint devices
    "A.3.23": "A.8.5",   # Secure authentication
    "A.3.24": "A.8.13",  # Information backup
    "A.3.25": "A.8.15",  # Logging
    "A.3.26": "A.8.24",  # Use of cryptography
    "A.3.27": "A.8.25",  # Secure development life cycle
    "A.3.28": "A.8.26",  # Application security requirements
    "A.3.29": "A.8.27",  # Secure system architecture and engineering principles
    "A.3.30": "A.8.30",  # Outsourced development
    "A.3.31": "A.8.33",  # Test information
}

# ISO 27701 A.1.x (controller) → ISO 27001:2022 approximate mappings
# Confidence: 0.75 — nearest relevant controls, not official 1:1 equivalence
A1_TO_ISO27001 = {
    "A.1.2.2":  ["A.5.34"],             # Identify and document purpose
    "A.1.2.3":  ["A.5.34", "A.5.31"],   # Identify lawful basis
    "A.1.2.4":  ["A.5.34"],             # Determine when and how consent is obtained
    "A.1.2.5":  ["A.5.34", "A.5.36"],   # Obtain and record consent
    "A.1.2.6":  ["A.5.34"],             # Privacy risk assessment (DPIA)
    "A.1.2.7":  ["A.5.19", "A.5.20"],   # Contracts with PII processors
    "A.1.2.8":  ["A.5.19"],             # Joint controllers
    "A.1.2.9":  ["A.5.33", "A.5.34"],   # Records related to processing PII
    "A.1.3.2":  ["A.5.34"],             # Obligations to PII principals
    "A.1.3.3":  ["A.5.34"],             # Determining information for PII principals
    "A.1.3.4":  ["A.5.34"],             # Providing information to PII principals
    "A.1.3.5":  ["A.5.34"],             # Mechanism to modify or withdraw consent
    "A.1.3.6":  ["A.5.34"],             # Mechanism to object to PII processing
    "A.1.3.7":  ["A.5.34"],             # Access, correction or erasure
    "A.1.3.8":  ["A.5.34"],             # Inform third parties of corrections
    "A.1.3.9":  ["A.5.34"],             # Providing copy of PII processed
    "A.1.3.10": ["A.5.34"],             # Handling requests
    "A.1.3.11": ["A.5.34"],             # Automated decision-making
    "A.1.4.2":  ["A.5.34"],             # Limit collection
    "A.1.4.3":  ["A.5.34"],             # Limit processing
    "A.1.4.4":  ["A.5.34"],             # Accuracy and quality
    "A.1.4.5":  ["A.5.34"],             # PII minimisation objectives
    "A.1.4.6":  ["A.8.10"],             # PII de-identification and deletion
    "A.1.4.7":  ["A.8.10"],             # Temporary files
    "A.1.4.8":  ["A.5.33", "A.5.34"],   # Retention
    "A.1.4.9":  ["A.8.10"],             # Disposal
    "A.1.4.10": ["A.8.24", "A.5.14"],   # PII transmission controls
    "A.1.5.2":  ["A.5.31"],             # Identify basis for PII transfer between jurisdictions
    "A.1.5.3":  ["A.5.31"],             # Countries and international organisations
    "A.1.5.4":  ["A.5.33", "A.5.36"],   # Records of transfer of PII
    "A.1.5.5":  ["A.5.31", "A.5.33"],   # Records of PII disclosures to third parties
}

# ISO 27701 A.2.x (processor) → ISO 27001:2022 approximate mappings
# Confidence: 0.75 — nearest relevant controls, not official 1:1 equivalence
A2_TO_ISO27001 = {
    "A.2.2.2":  ["A.5.19", "A.5.20"],   # Customer agreement
    "A.2.2.3":  ["A.5.19"],             # Organisation's purposes
    "A.2.2.4":  ["A.5.34"],             # Marketing and advertising use
    "A.2.2.5":  ["A.5.31"],             # Infringing instruction
    "A.2.2.6":  ["A.5.19", "A.5.20"],   # Customer obligations
    "A.2.2.7":  ["A.5.33", "A.5.36"],   # Records related to processing PII
    "A.2.3.2":  ["A.5.34"],             # Comply with obligations to PII principals
    "A.2.4.2":  ["A.8.10"],             # Temporary files
    "A.2.4.3":  ["A.8.10"],             # Return, transfer or disposal of PII
    "A.2.4.4":  ["A.8.24", "A.5.14"],   # PII transmission controls
    "A.2.5.2":  ["A.5.31"],             # Basis for PII transfer between jurisdictions
    "A.2.5.3":  ["A.5.31"],             # Countries and international organisations
    "A.2.5.4":  ["A.5.33", "A.5.36"],   # Records of PII disclosures to third parties
    "A.2.5.5":  ["A.5.31"],             # Notification of PII disclosure requests
    "A.2.5.6":  ["A.5.31"],             # Legally binding PII disclosures
    "A.2.5.7":  ["A.5.21"],             # Disclosure of subcontractors
    "A.2.5.8":  ["A.5.21"],             # Engagement of a subcontractor
    "A.2.5.9":  ["A.5.21"],             # Change of subcontractor
}


def normalise_gdpr_article(raw: str) -> str | None:
    """Normalise 'Art. 5(1)(a)' → 'Art. 5'. Returns None if not in dataset."""
    m = re.match(r"^(Art\.\s*\d+)", raw)
    if not m:
        return None
    base = m.group(1)
    return base if base in VALID_GDPR_ARTICLES else None


def make_mapping(source_fw, source_id, target_fw, target_id, mapping_type,
                 confidence, source_reference, notes=""):
    return {
        "source_framework": source_fw,
        "source_id": source_id,
        "target_framework": target_fw,
        "target_id": target_id,
        "mapping_type": mapping_type,
        "confidence": confidence,
        "source_reference": source_reference,
        "notes": notes,
    }


def main():
    # Load raw mappings
    with open(RAW_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    existing = raw["mappings"]
    # Build dedup key set: (src_fw, src_id, tgt_fw, tgt_id)
    seen = {
        (m["source_framework"], m["source_id"], m["target_framework"], m["target_id"])
        for m in existing
    }

    new_mappings = []
    stats: dict[str, int] = {}

    def add(m: dict) -> None:
        key = (m["source_framework"], m["source_id"], m["target_framework"], m["target_id"])
        if key not in seen:
            seen.add(key)
            new_mappings.append(m)
            axis = f"{m['source_framework']} → {m['target_framework']}"
            stats[axis] = stats.get(axis, 0) + 1

    # ------------------------------------------------------------------
    # Load source data
    # ------------------------------------------------------------------
    with open(INDEXES_FILE, "r", encoding="utf-8") as f:
        indexes = json.load(f)

    with open(ISO27017_FILE, "r", encoding="utf-8") as f:
        iso27017 = json.load(f)

    with open(ISO27018_FILE, "r", encoding="utf-8") as f:
        iso27018 = json.load(f)

    gdpr_entries = indexes["indexes"]["gdpr_to_iso_27701_and_27018"]["entries"]
    idx_27701_to_27018 = indexes["indexes"]["iso_27701_to_iso_27018"]["entries"]
    idx_27018_to_27701 = indexes["indexes"]["iso_27018_to_iso_27701"]["entries"]

    # ------------------------------------------------------------------
    # 1. ISO27701 → EU_GDPR  (invert GDPR→27701 index, normalize article)
    # ------------------------------------------------------------------
    # Also 2b. ISO27018 → EU_GDPR (invert GDPR→27018 index)
    ref_gdpr_annex = "ISO/IEC 27701:2025 Annex D — GDPR mapping"
    ref_27018_gdpr = "ISO/IEC 27018:2025 — GDPR alignment (derived from ISO 27701:2025 Annex D)"

    for entry in gdpr_entries:
        art_raw = entry["gdpr_article"]
        art = normalise_gdpr_article(art_raw)
        if art is None:
            continue

        for ctrl in entry.get("mapped_iso_27701", []):
            add(make_mapping(
                "ISO27701", ctrl, "EU_GDPR", art,
                "maps-to", 0.90, ref_gdpr_annex,
                f"ISO 27701 control {ctrl} addresses {art_raw} requirements",
            ))

        for ctrl in entry.get("mapped_iso_27018_2025", []):
            add(make_mapping(
                "ISO27018", ctrl, "EU_GDPR", art,
                "maps-to", 0.85, ref_27018_gdpr,
                f"ISO 27018 control {ctrl} supports {art_raw} requirements",
            ))

    # ------------------------------------------------------------------
    # 2a. ISO27701 → ISO27018  (from iso_27701_to_iso_27018 index)
    # ------------------------------------------------------------------
    ref_annex_e = "ISO/IEC 27701:2025 Annex E — ISO 27018/29151 mapping"

    for ctrl_27701, data in idx_27701_to_27018.items():
        for ctrl_27018 in data.get("iso_27018_2025", []):
            add(make_mapping(
                "ISO27701", ctrl_27701, "ISO27018", ctrl_27018,
                "maps-to", 0.90, ref_annex_e,
                f"ISO 27701 {ctrl_27701} ({data.get('title','')}) extends ISO 27018 {ctrl_27018}",
            ))

    # ------------------------------------------------------------------
    # 3. ISO27018 → ISO27701  (from iso_27018_to_iso_27701 index)
    # ------------------------------------------------------------------
    for ctrl_27018, data in idx_27018_to_27701.items():
        for ctrl_27701 in data.get("iso_27701", []):
            add(make_mapping(
                "ISO27018", ctrl_27018, "ISO27701", ctrl_27701,
                "maps-to", 0.90, ref_annex_e,
                f"ISO 27018 {ctrl_27018} ({data.get('title','')}) maps to ISO 27701 {ctrl_27701}",
            ))

    # ------------------------------------------------------------------
    # 4. ISO27701 A.3.x → ISO27001_2022  (exact equivalence)
    # ------------------------------------------------------------------
    ref_a3 = "ISO/IEC 27701:2025 Table A.3 — Security controls for PII controllers and processors (ISO 27001:2022 Annex A)"

    for ctrl_27701, ctrl_27001 in A3_TO_ISO27001.items():
        add(make_mapping(
            "ISO27701", ctrl_27701, "ISO27001_2022", ctrl_27001,
            "maps-to", 1.00, ref_a3,
            f"ISO 27701 A.3 control is the ISO 27001:2022 {ctrl_27001} control applied in a PIMS context",
        ))

    # ------------------------------------------------------------------
    # 5. ISO27701 A.1.x → ISO27001_2022  (approximate)
    # ------------------------------------------------------------------
    ref_a1 = "ISO/IEC 27701:2025 — derived mapping to nearest ISO/IEC 27001:2022 Annex A controls (controller obligations)"

    for ctrl_27701, iso27001_list in A1_TO_ISO27001.items():
        for ctrl_27001 in iso27001_list:
            add(make_mapping(
                "ISO27701", ctrl_27701, "ISO27001_2022", ctrl_27001,
                "maps-to", 0.75, ref_a1,
                f"ISO 27701 controller control {ctrl_27701} is supported by ISO 27001:2022 {ctrl_27001}",
            ))

    # ------------------------------------------------------------------
    # 6. ISO27701 A.2.x → ISO27001_2022  (approximate)
    # ------------------------------------------------------------------
    ref_a2 = "ISO/IEC 27701:2025 — derived mapping to nearest ISO/IEC 27001:2022 Annex A controls (processor obligations)"

    for ctrl_27701, iso27001_list in A2_TO_ISO27001.items():
        for ctrl_27001 in iso27001_list:
            add(make_mapping(
                "ISO27701", ctrl_27701, "ISO27001_2022", ctrl_27001,
                "maps-to", 0.75, ref_a2,
                f"ISO 27701 processor control {ctrl_27701} is supported by ISO 27001:2022 {ctrl_27001}",
            ))

    # ------------------------------------------------------------------
    # 7. ISO27017 → ISO27001_2022  (from bundle metadata)
    # ------------------------------------------------------------------
    ref_27017 = "ISO/IEC 27017:2015 — cloud extension controls mapped to ISO/IEC 27001:2022 Annex A"

    for obj in iso27017["objects"]:
        ctrl_27017 = obj.get("control_id", "")
        meta = obj.get("metadata", {})
        iso27001_list = meta.get("maps_to_iso27001_2022", [])
        if not iso27001_list or ctrl_27017 in ("CLD", "CSP", "CSC"):
            continue
        for ctrl_27001 in iso27001_list:
            add(make_mapping(
                "ISO27017", ctrl_27017, "ISO27001_2022", ctrl_27001,
                "maps-to", 0.90, ref_27017,
                f"ISO 27017 cloud control {ctrl_27017} extends ISO 27001:2022 {ctrl_27001}",
            ))

    # ------------------------------------------------------------------
    # 8. ISO27018 → ISO27001_2022  (from bundle metadata)
    # ------------------------------------------------------------------
    ref_27018 = "ISO/IEC 27018:2025 — PII processor cloud controls mapped to ISO/IEC 27001:2022 Annex A"

    for obj in iso27018["objects"]:
        ctrl_27018 = obj.get("control_id", "")
        meta = obj.get("metadata", {})
        iso27001_list = meta.get("maps_to_iso27001_2022", [])
        # Skip parent headers without real content (top-level Annex A header)
        if not iso27001_list or ctrl_27018 in ("A",):
            continue
        # Only leaf controls (those with a dot in the ID, or 1-2 char section like A.2, A.6)
        for ctrl_27001 in iso27001_list:
            add(make_mapping(
                "ISO27018", ctrl_27018, "ISO27001_2022", ctrl_27001,
                "maps-to", 0.90, ref_27018,
                f"ISO 27018 PII cloud control {ctrl_27018} extends ISO 27001:2022 {ctrl_27001}",
            ))

    # ------------------------------------------------------------------
    # Write updated raw file
    # ------------------------------------------------------------------
    raw["mappings"] = existing + new_mappings

    # Update mapping_axes count in header
    axis_counts = {}
    for m in raw["mappings"]:
        axis = f"{m['source_framework']} ↔ {m['target_framework']}"
        axis_counts[axis] = axis_counts.get(axis, 0) + 1
    raw["mapping_axes"] = axis_counts

    # Update version
    raw["version"] = "2.0"
    raw["generated_by"] = "assemble_crosswalk_raw.py + generate_privacy_cloud_crosswalk.py"

    with open(RAW_FILE, "w", encoding="utf-8") as f:
        json.dump(raw, f, indent=2, ensure_ascii=False)

    print(f"Updated {RAW_FILE.name}")
    print(f"  Existing mappings:  {len(existing):4d}")
    print(f"  New mappings added: {len(new_mappings):4d}")
    print(f"  Total mappings:     {len(existing) + len(new_mappings):4d}")
    print()
    print("New mapping axes:")
    for axis, count in sorted(stats.items()):
        print(f"  {axis:<45s} {count:4d}")

    print()
    print("Next step: regenerate crosswalk bundle:")
    print("  python3 datasets/scripts/generate_crosswalk.py")


if __name__ == "__main__":
    main()
