#!/usr/bin/env python3
"""
Assemble cross-framework crosswalk raw data from research sources.

Reads CSV mapping files from research agents and inline data to produce
the unified raw/crosswalk_mappings.json consumed by generate_crosswalk.py.

Mapping axes:
  1. ISO 27001:2022 ↔ NIST CSF 2.0          (NIST informative references)
  2. ISO 27001:2022 ↔ NIST SP 800-53 R5     (NIST CSRC crosswalk document)
  3. ISO 27001:2022 ↔ CIS Controls v8       (CIS published mapping)
  4. NIST 800-53 R5 ↔ MITRE ATT&CK v18      (CTID project mappings)
  5. ISO 27001:2022 ↔ Regulatory frameworks  (published compliance mappings)
  6. ISO 27001:2022 ↔ OWASP Top 10:2025     (web security control mapping)

Sources:
  - NIST_CSF2_to_ISO27001_2022_mapping.csv
  - CIS_v8_to_ISO27001_2022_mapping.csv
  - MITRE_ATTaCK_to_NIST80053_mapping.csv
  - Inline: NIST 800-53 R5 → ISO (from sp800-53r5-to-iso-27001-mapping.docx)
  - Inline: Regulatory → ISO (from published compliance mapping guides)
  - Inline: OWASP → ISO (web security to information security controls)
"""

import csv
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RAW_DIR = SCRIPT_DIR.parent / "raw"
OUTPUT_FILE = RAW_DIR / "crosswalk_mappings.json"

# Framework codes matching the generated bundles
ISO = "ISO27001_2022"
CSF = "NIST_CSF_2.0"
NIST = "NIST_800_53_R5"
CIS = "CIS_V8"
MITRE = "MITRE_ATTACK_V18"
OWASP = "OWASP_TOP10_2025"

# Regulatory codes
GDPR = "EU_GDPR"
NDSG = "SWISS_NDSG"
NIS2 = "NIS2"
DORA = "DORA"
PCI = "PCI_DSS_4.0.1"
AIACT = "EU_AI_ACT"


# ============================================================================
# AXIS 1: ISO 27001:2022 ↔ NIST CSF 2.0
# Source: NIST Informative References (official NIST OLIR catalog)
# ============================================================================
def load_csf_mappings() -> list:
    """Read CSF CSV and produce one mapping per ISO control per CSF subcategory."""
    csv_file = SCRIPT_DIR / "NIST_CSF2_to_ISO27001_2022_mapping.csv"
    mappings = []

    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            subcategory = row["csf_subcategory"]
            iso_controls_str = row.get("iso27001_annex_a", "").strip()
            if not iso_controls_str:
                continue

            iso_controls = [c.strip() for c in iso_controls_str.split(";") if c.strip()]
            for iso_ctrl in iso_controls:
                mappings.append({
                    "source_framework": ISO,
                    "source_id": iso_ctrl,
                    "target_framework": CSF,
                    "target_id": subcategory,
                    "mapping_type": "maps-to",
                    "confidence": 0.90,
                    "source_reference": "NIST Informative References (OLIR catalog, referenceId=154)",
                    "notes": row.get("csf_title", "")[:120]
                })

    return mappings


# ============================================================================
# AXIS 2: ISO 27001:2022 ↔ NIST SP 800-53 Rev 5
# Source: NIST CSRC sp800-53r5-to-iso-27001-mapping.docx (Table 2)
# ============================================================================

# The 20 "XX-1" policy controls that map to ISO's overarching policy requirements
ALL_XX1 = [
    "AC-1", "AT-1", "AU-1", "CA-1", "CM-1", "CP-1", "IA-1", "IR-1",
    "MA-1", "MP-1", "PE-1", "PL-1", "PM-1", "PS-1", "PT-1", "RA-1",
    "SA-1", "SC-1", "SI-1", "SR-1"
]

# ISO → NIST 800-53 mapping (from official NIST crosswalk document)
# "XX1" is a placeholder expanded to ALL_XX1 controls
# Asterisk (*) in source = partial mapping (confidence lowered to 0.75)
NIST_800_53_MAP = {
    # A.5 Organisational Controls
    "A.5.1":  "XX1",
    "A.5.2":  "XX1,CM-9,CP-2,PS-7,PS-9,SA-3,SA-9,PM-2,PM-10",
    "A.5.3":  "AC-5",
    "A.5.4":  "XX1,PM-18*",
    "A.5.5":  "IR-6",
    "A.5.6":  "PM-15,SI-5",
    "A.5.7":  "PM-16,PM-16(1),RA-10",
    "A.5.8":  "PL-2,PL-7,PL-8,SA-3,SA-4,SA-9,SA-15",
    "A.5.9":  "CM-8",
    "A.5.10": "MP-2,MP-4,MP-5,MP-6,MP-7,PE-16,PE-18,PE-20,PL-4,SC-8,SC-28",
    "A.5.11": "PS-4,PS-5",
    "A.5.12": "RA-2",
    "A.5.13": "MP-3,PE-22",
    "A.5.14": "AC-4,AC-17,AC-18,AC-19,AC-20,CA-3,PE-17,PS-6,SA-9,SC-7,SC-8,SC-15",
    "A.5.15": "AC-1,AC-3,AC-6",
    "A.5.16": "AC-2,IA-2,IA-4,IA-5,IA-8",
    "A.5.17": "IA-5",
    "A.5.18": "AC-2",
    "A.5.19": "SR-1",
    "A.5.20": "SA-4,SR-3",
    "A.5.21": "SR-3,SR-5",
    "A.5.22": "RA-9,SA-9,SR-6,SR-7",
    "A.5.23": "SA-1,SA-4,SA-9,SA-9(3),SR-5",
    "A.5.24": "IR-8",
    "A.5.25": "AU-6,IR-4",
    "A.5.26": "IR-4",
    "A.5.27": "IR-4",
    "A.5.28": "AU-3,AU-4,AU-9,AU-10(3),AU-11*",
    "A.5.29": "CP-2,CP-4,CP-6,CP-7,CP-8,CP-9,CP-10,CP-11,CP-13",
    "A.5.30": "CP-2(1)*,CP-2(8)*,CP-4*,CP-4(1)*",
    "A.5.31": "XX1,SC-12,SC-13,SC-17",
    "A.5.32": "CM-10*",
    "A.5.33": "AC-3*,AC-23,AU-9,CP-9,SC-8,SC-8(1)*,SC-13,SC-28,SC-28(1)*",
    "A.5.34": "PM-18,PT-1,PT-3,PT-7,CA-9*,CA-3*,PL-2*,PL-8*",
    "A.5.35": "CA-2(1)",
    "A.5.36": "XX1,CA-2",
    "A.5.37": "XX1,SA-5",
    # A.6 People Controls
    "A.6.1":  "PS-3,SA-21",
    "A.6.2":  "PL-4,PS-6",
    "A.6.3":  "AT-2,AT-3,CP-3,IR-2,PM-13",
    "A.6.4":  "PS-8",
    "A.6.5":  "PS-4,PS-5",
    "A.6.6":  "PS-6",
    "A.6.7":  "",  # No NIST mapping
    "A.6.8":  "AU-6,IR-6,SI-2",
    # A.7 Physical Controls
    "A.7.1":  "PE-3*",
    "A.7.2":  "PE-2,PE-3,PE-4,PE-5,PE-16",
    "A.7.3":  "PE-3,PE-5",
    "A.7.4":  "AU-6(6)*,PE-3,PE-3(3),PE-6,PE-6(1),PE-6(4)*",
    "A.7.5":  "CP-6,CP-7,PE-9,PE-13,PE-14,PE-15,PE-18,PE-19,PE-23",
    "A.7.6":  "SC-42*",
    "A.7.7":  "AC-11,MP-2,MP-4",
    "A.7.8":  "PE-9,PE-13,PE-14,PE-15,PE-18,PE-19,PE-23",
    "A.7.9":  "AC-19,AC-20,MP-5,PE-17",
    "A.7.10": "MA-2,MP-2,MP-4,MP-5,MP-6,MP-7,PE-16",
    "A.7.11": "CP-8,PE-9,PE-10,PE-11,PE-12,PE-14,PE-15",
    "A.7.12": "PE-4,PE-9",
    "A.7.13": "MA-2,MA-6",
    "A.7.14": "MP-6",
    # A.8 Technological Controls
    "A.8.1":  "AC-11",
    "A.8.2":  "AC-2,AC-3,AC-6,CM-5",
    "A.8.3":  "AC-3,AC-24",
    "A.8.4":  "AC-3*,AC-3(11),CM-5",
    "A.8.5":  "AC-7,AC-8,AC-9,IA-6",
    "A.8.6":  "AU-4,CP-2(2),SC-5(2)*",
    "A.8.7":  "AT-2,SI-3",
    "A.8.8":  "RA-3,RA-5,SI-2,SI-5",
    "A.8.9":  "CM-1,CM-2,CM-2(3)*,CM-3,CM-3(7),CM-3(8),CM-4,CM-5,CM-6,CM-8,CM-9,CM-9(1)*,SA-10",
    "A.8.10": "AC-4(25)*,AC-7(2)*,MA-2,MA-3(3)*,MA-4(3)*,MP-4,MP-6,MP-6(1)*,SI-21",
    "A.8.11": "AC-4(23),SI-19(4)",
    "A.8.12": "AU-13,PE-3(2)*,PE-19,SC-7(10)*,SI-20",
    "A.8.13": "CP-9",
    "A.8.14": "CP-2,CP-6,CP-7",
    "A.8.15": "AU-3,AU-6,AU-9,AU-11,AU-12,AU-14",
    "A.8.16": "AC-2(12),AC-17(1),AU-13*,IR-4(13)*,MA-4(1)*,PE-6*,PE-6(3)*,SI-4,SI-4(4)*,SI-4(13)*,SI-4(16)*",
    "A.8.17": "AU-8",
    "A.8.18": "AC-3,AC-6",
    "A.8.19": "CM-5,CM-7(4)*,CM-7(5)*,CM-11*",
    "A.8.20": "AC-3,AC-18,AC-20,SC-7,SC-8,SC-10",
    "A.8.21": "CA-3,SA-9",
    "A.8.22": "AC-4,SC-7",
    "A.8.23": "AC-4,SC-7,SC-7(8)",
    "A.8.24": "SC-12,SC-13,SC-17",
    "A.8.25": "SA-3,SA-15,SA-17",
    "A.8.26": "AC-3,SC-8*,SC-13",
    "A.8.27": "SA-8",
    "A.8.28": "SA-4(3)*,SA-8,SA-11(1)*,SA-15(5)*,SI-10",
    "A.8.29": "CA-2,SA-4,SA-11,SR-5(2)*",
    "A.8.30": "SA-4,SA-10,SA-11,SA-15,SR-2,SR-4",
    "A.8.31": "CM-4(1),CM-5*,SA-3*",
    "A.8.32": "CM-3,CM-5,SA-10,SI-2",
    "A.8.33": "SA-3(2)*",
    "A.8.34": "AU-5*",
}


def load_nist_800_53_mappings() -> list:
    """Expand NIST 800-53 mapping data into individual mapping records."""
    mappings = []

    for iso_ctrl, nist_str in NIST_800_53_MAP.items():
        if not nist_str:
            continue

        tokens = [t.strip() for t in nist_str.split(",") if t.strip()]
        nist_ctrls = []

        for token in tokens:
            if token == "XX1":
                # Expand to all 20 XX-1 policy controls
                for xx1 in ALL_XX1:
                    nist_ctrls.append((xx1, False))
            else:
                partial = token.endswith("*")
                ctrl_id = token.rstrip("*")
                nist_ctrls.append((ctrl_id, partial))

        for nist_ctrl, is_partial in nist_ctrls:
            mappings.append({
                "source_framework": ISO,
                "source_id": iso_ctrl,
                "target_framework": NIST,
                "target_id": nist_ctrl,
                "mapping_type": "partially-maps-to" if is_partial else "maps-to",
                "confidence": 0.75 if is_partial else 0.85,
                "source_reference": "NIST CSRC sp800-53r5-to-iso-27001-mapping.docx (Table 2)",
                "notes": ""
            })

    return mappings


# ============================================================================
# AXIS 3: ISO 27001:2022 ↔ CIS Controls v8
# Source: CIS v8.1 Mapping to ISO/IEC 27001:2022 (CIS published mapping)
# ============================================================================
def load_cis_mappings() -> list:
    """Read CIS CSV and produce one mapping per ISO control per CIS safeguard."""
    csv_file = SCRIPT_DIR / "CIS_v8_to_ISO27001_2022_mapping.csv"
    mappings = []

    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cis_id = row["cis_safeguard"]
            iso_controls_str = row.get("iso_controls", "").strip()
            if not iso_controls_str:
                continue

            iso_controls = [c.strip() for c in iso_controls_str.split(";") if c.strip()]
            for iso_ctrl in iso_controls:
                mappings.append({
                    "source_framework": ISO,
                    "source_id": iso_ctrl,
                    "target_framework": CIS,
                    "target_id": cis_id,
                    "mapping_type": "maps-to",
                    "confidence": 0.85,
                    "source_reference": "CIS Controls v8.1 Mapping to ISO/IEC 27001:2022",
                    "notes": row.get("notes", "")
                })

    return mappings


# ============================================================================
# AXIS 4: NIST SP 800-53 R5 ↔ MITRE ATT&CK v18
# Source: CTID Mappings Explorer (NIST 800-53 Rev 5 to ATT&CK v16.1)
# ============================================================================
def load_mitre_mappings() -> list:
    """Read MITRE CSV and produce one mapping per NIST control per technique."""
    csv_file = SCRIPT_DIR / "MITRE_ATTaCK_to_NIST80053_mapping.csv"
    mappings = []

    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            technique = row["mitre_technique"]
            nist_controls_str = row.get("nist_controls", "").strip()
            if not nist_controls_str:
                continue

            nist_controls = [c.strip() for c in nist_controls_str.split(",") if c.strip()]
            for nist_ctrl in nist_controls:
                mappings.append({
                    "source_framework": NIST,
                    "source_id": nist_ctrl,
                    "target_framework": MITRE,
                    "target_id": technique,
                    "mapping_type": "mitigates",
                    "confidence": 0.80,
                    "source_reference": "CTID Mappings Explorer — NIST 800-53 Rev 5 to ATT&CK",
                    "notes": row.get("tactic", "")
                })

    return mappings


# ============================================================================
# AXIS 5: ISO 27001:2022 ↔ Regulatory Frameworks
# Sources: DataGuard, NQA, Advisera, Ceeyu, ENISA, ISACA published mappings
# ============================================================================

# Format: (iso_control, framework_code, regulatory_article, mapping_type, confidence)
REGULATORY_MAPPINGS = [
    # --- EU GDPR (57 mappings) ---
    ("A.5.34", GDPR, "Art. 5", "maps-to", 0.90),
    ("A.5.10", GDPR, "Art. 5", "supports", 0.80),
    ("A.5.12", GDPR, "Art. 5", "supports", 0.80),
    ("A.5.13", GDPR, "Art. 5", "supports", 0.80),
    ("A.5.33", GDPR, "Art. 5", "supports", 0.80),
    ("A.5.1", GDPR, "Art. 24", "supports", 0.80),
    ("A.5.2", GDPR, "Art. 24", "supports", 0.80),
    ("A.5.36", GDPR, "Art. 24", "supports", 0.80),
    ("A.5.1", GDPR, "Art. 25", "supports", 0.80),
    ("A.5.8", GDPR, "Art. 25", "maps-to", 0.85),
    ("A.5.34", GDPR, "Art. 25", "maps-to", 0.90),
    ("A.8.11", GDPR, "Art. 25", "supports", 0.80),
    ("A.8.25", GDPR, "Art. 25", "supports", 0.80),
    ("A.8.26", GDPR, "Art. 25", "supports", 0.80),
    ("A.5.2", GDPR, "Art. 28", "supports", 0.80),
    ("A.5.19", GDPR, "Art. 28", "maps-to", 0.85),
    ("A.5.20", GDPR, "Art. 28", "maps-to", 0.85),
    ("A.5.21", GDPR, "Art. 28", "supports", 0.80),
    ("A.5.22", GDPR, "Art. 28", "supports", 0.80),
    ("A.5.33", GDPR, "Art. 30", "maps-to", 0.85),
    ("A.5.9", GDPR, "Art. 30", "supports", 0.80),
    ("A.5.12", GDPR, "Art. 30", "supports", 0.80),
    ("A.5.1", GDPR, "Art. 32", "maps-to", 0.85),
    ("A.5.15", GDPR, "Art. 32", "maps-to", 0.85),
    ("A.5.17", GDPR, "Art. 32", "supports", 0.85),
    ("A.5.29", GDPR, "Art. 32", "supports", 0.80),
    ("A.5.34", GDPR, "Art. 32", "maps-to", 0.90),
    ("A.8.1", GDPR, "Art. 32", "supports", 0.80),
    ("A.8.2", GDPR, "Art. 32", "supports", 0.80),
    ("A.8.5", GDPR, "Art. 32", "supports", 0.85),
    ("A.8.7", GDPR, "Art. 32", "supports", 0.80),
    ("A.8.9", GDPR, "Art. 32", "supports", 0.80),
    ("A.8.13", GDPR, "Art. 32", "supports", 0.80),
    ("A.8.15", GDPR, "Art. 32", "supports", 0.85),
    ("A.8.20", GDPR, "Art. 32", "supports", 0.80),
    ("A.8.24", GDPR, "Art. 32", "maps-to", 0.90),
    ("A.5.24", GDPR, "Art. 33", "maps-to", 0.90),
    ("A.5.25", GDPR, "Art. 33", "supports", 0.85),
    ("A.5.26", GDPR, "Art. 33", "supports", 0.85),
    ("A.5.27", GDPR, "Art. 33", "supports", 0.80),
    ("A.5.28", GDPR, "Art. 33", "supports", 0.80),
    ("A.6.8", GDPR, "Art. 33", "supports", 0.80),
    ("A.5.24", GDPR, "Art. 34", "supports", 0.80),
    ("A.5.26", GDPR, "Art. 34", "supports", 0.80),
    ("A.5.34", GDPR, "Art. 35", "maps-to", 0.85),
    ("A.5.8", GDPR, "Art. 35", "supports", 0.80),
    ("A.5.1", GDPR, "Art. 35", "supports", 0.75),
    ("A.5.14", GDPR, "Art. 44", "supports", 0.80),
    ("A.5.19", GDPR, "Art. 44", "supports", 0.75),
    ("A.5.31", GDPR, "Art. 44", "supports", 0.80),
    ("A.5.34", GDPR, "Art. 44", "supports", 0.85),
    ("A.5.14", GDPR, "Art. 46", "supports", 0.80),
    ("A.5.31", GDPR, "Art. 46", "supports", 0.80),
    ("A.8.24", GDPR, "Art. 46", "supports", 0.75),
    # Remaining GDPR (deduplicated: 3 more for Art. 37-39 DPO)
    ("A.5.2", GDPR, "Art. 37", "supports", 0.75),
    ("A.5.4", GDPR, "Art. 37", "supports", 0.75),
    ("A.6.3", GDPR, "Art. 39", "supports", 0.75),

    # --- Swiss nFADP (41 mappings) ---
    ("A.5.1", NDSG, "Art. 7", "supports", 0.85),
    ("A.5.2", NDSG, "Art. 7", "supports", 0.80),
    ("A.5.15", NDSG, "Art. 7", "supports", 0.85),
    ("A.5.17", NDSG, "Art. 7", "supports", 0.85),
    ("A.5.29", NDSG, "Art. 7", "supports", 0.80),
    ("A.5.34", NDSG, "Art. 7", "maps-to", 0.90),
    ("A.8.1", NDSG, "Art. 7", "supports", 0.80),
    ("A.8.2", NDSG, "Art. 7", "supports", 0.80),
    ("A.8.3", NDSG, "Art. 7", "supports", 0.80),
    ("A.8.5", NDSG, "Art. 7", "supports", 0.85),
    ("A.8.7", NDSG, "Art. 7", "supports", 0.80),
    ("A.8.9", NDSG, "Art. 7", "supports", 0.80),
    ("A.8.13", NDSG, "Art. 7", "supports", 0.80),
    ("A.8.15", NDSG, "Art. 7", "supports", 0.85),
    ("A.8.20", NDSG, "Art. 7", "supports", 0.80),
    ("A.8.24", NDSG, "Art. 7", "maps-to", 0.90),
    ("A.5.1", NDSG, "Art. 8", "supports", 0.80),
    ("A.5.8", NDSG, "Art. 8", "maps-to", 0.85),
    ("A.5.34", NDSG, "Art. 8", "maps-to", 0.90),
    ("A.8.11", NDSG, "Art. 8", "supports", 0.80),
    ("A.8.12", NDSG, "Art. 8", "supports", 0.80),
    ("A.8.24", NDSG, "Art. 8", "supports", 0.85),
    ("A.8.25", NDSG, "Art. 8", "supports", 0.80),
    ("A.8.26", NDSG, "Art. 8", "supports", 0.80),
    ("A.5.14", NDSG, "Art. 16", "supports", 0.85),
    ("A.5.19", NDSG, "Art. 16", "supports", 0.80),
    ("A.5.20", NDSG, "Art. 16", "supports", 0.80),
    ("A.5.31", NDSG, "Art. 16", "supports", 0.85),
    ("A.5.34", NDSG, "Art. 16", "maps-to", 0.85),
    ("A.8.24", NDSG, "Art. 16", "supports", 0.80),
    ("A.5.14", NDSG, "Art. 17", "supports", 0.75),
    ("A.5.34", NDSG, "Art. 17", "supports", 0.80),
    ("A.5.34", NDSG, "Art. 22", "maps-to", 0.85),
    ("A.5.8", NDSG, "Art. 22", "supports", 0.80),
    ("A.5.1", NDSG, "Art. 22", "supports", 0.75),
    ("A.5.24", NDSG, "Art. 24", "maps-to", 0.90),
    ("A.5.25", NDSG, "Art. 24", "supports", 0.85),
    ("A.5.26", NDSG, "Art. 24", "supports", 0.85),
    ("A.5.27", NDSG, "Art. 24", "supports", 0.80),
    ("A.5.28", NDSG, "Art. 24", "supports", 0.80),
    ("A.6.8", NDSG, "Art. 24", "supports", 0.80),

    # --- NIS2 Directive (54 mappings) ---
    ("A.5.1", NIS2, "Art. 21(2)(a)", "maps-to", 0.90),
    ("A.5.7", NIS2, "Art. 21(2)(a)", "supports", 0.85),
    ("A.5.36", NIS2, "Art. 21(2)(a)", "supports", 0.85),
    ("A.5.24", NIS2, "Art. 21(2)(b)", "maps-to", 0.90),
    ("A.5.25", NIS2, "Art. 21(2)(b)", "maps-to", 0.90),
    ("A.5.26", NIS2, "Art. 21(2)(b)", "maps-to", 0.90),
    ("A.5.27", NIS2, "Art. 21(2)(b)", "supports", 0.85),
    ("A.5.28", NIS2, "Art. 21(2)(b)", "supports", 0.85),
    ("A.6.8", NIS2, "Art. 21(2)(b)", "supports", 0.80),
    ("A.8.15", NIS2, "Art. 21(2)(b)", "supports", 0.85),
    ("A.8.16", NIS2, "Art. 21(2)(b)", "supports", 0.85),
    ("A.8.17", NIS2, "Art. 21(2)(b)", "supports", 0.80),
    ("A.5.29", NIS2, "Art. 21(2)(c)", "maps-to", 0.90),
    ("A.5.30", NIS2, "Art. 21(2)(c)", "maps-to", 0.85),
    ("A.8.13", NIS2, "Art. 21(2)(c)", "maps-to", 0.90),
    ("A.8.14", NIS2, "Art. 21(2)(c)", "supports", 0.85),
    ("A.5.19", NIS2, "Art. 21(2)(d)", "maps-to", 0.90),
    ("A.5.20", NIS2, "Art. 21(2)(d)", "maps-to", 0.90),
    ("A.5.21", NIS2, "Art. 21(2)(d)", "maps-to", 0.85),
    ("A.5.22", NIS2, "Art. 21(2)(d)", "supports", 0.80),
    ("A.8.30", NIS2, "Art. 21(2)(d)", "supports", 0.80),
    ("A.5.23", NIS2, "Art. 21(2)(e)", "supports", 0.85),
    ("A.8.8", NIS2, "Art. 21(2)(e)", "maps-to", 0.90),
    ("A.8.9", NIS2, "Art. 21(2)(e)", "supports", 0.85),
    ("A.8.25", NIS2, "Art. 21(2)(e)", "maps-to", 0.85),
    ("A.8.29", NIS2, "Art. 21(2)(e)", "supports", 0.80),
    ("A.8.31", NIS2, "Art. 21(2)(e)", "maps-to", 0.85),
    ("A.8.32", NIS2, "Art. 21(2)(e)", "supports", 0.85),
    ("A.8.33", NIS2, "Art. 21(2)(e)", "supports", 0.80),
    ("A.8.34", NIS2, "Art. 21(2)(e)", "supports", 0.80),
    ("A.5.35", NIS2, "Art. 21(2)(f)", "maps-to", 0.90),
    ("A.5.36", NIS2, "Art. 21(2)(f)", "maps-to", 0.90),
    ("A.6.3", NIS2, "Art. 21(2)(g)", "maps-to", 0.90),
    ("A.8.7", NIS2, "Art. 21(2)(g)", "supports", 0.80),
    ("A.5.31", NIS2, "Art. 21(2)(h)", "supports", 0.85),
    ("A.8.24", NIS2, "Art. 21(2)(h)", "maps-to", 0.95),
    ("A.5.9", NIS2, "Art. 21(2)(i)", "supports", 0.85),
    ("A.5.15", NIS2, "Art. 21(2)(i)", "maps-to", 0.90),
    ("A.5.16", NIS2, "Art. 21(2)(i)", "supports", 0.85),
    ("A.5.18", NIS2, "Art. 21(2)(i)", "supports", 0.85),
    ("A.6.1", NIS2, "Art. 21(2)(i)", "supports", 0.80),
    ("A.6.2", NIS2, "Art. 21(2)(i)", "supports", 0.80),
    ("A.6.5", NIS2, "Art. 21(2)(i)", "supports", 0.80),
    ("A.8.2", NIS2, "Art. 21(2)(i)", "supports", 0.85),
    ("A.8.3", NIS2, "Art. 21(2)(i)", "supports", 0.85),
    ("A.8.18", NIS2, "Art. 21(2)(i)", "supports", 0.85),
    ("A.5.17", NIS2, "Art. 21(2)(j)", "maps-to", 0.85),
    ("A.8.5", NIS2, "Art. 21(2)(j)", "maps-to", 0.90),
    ("A.8.20", NIS2, "Art. 21(2)(j)", "supports", 0.85),
    ("A.8.21", NIS2, "Art. 21(2)(j)", "supports", 0.80),
    ("A.8.22", NIS2, "Art. 21(2)(j)", "supports", 0.80),
    ("A.8.24", NIS2, "Art. 21(2)(j)", "supports", 0.85),
    ("A.5.24", NIS2, "Art. 23", "maps-to", 0.85),
    ("A.5.25", NIS2, "Art. 23", "supports", 0.80),

    # --- DORA (50 mappings) ---
    ("A.5.1", DORA, "Art. 5", "maps-to", 0.85),
    ("A.5.2", DORA, "Art. 5", "maps-to", 0.85),
    ("A.5.4", DORA, "Art. 5", "supports", 0.80),
    ("A.5.1", DORA, "Art. 6", "maps-to", 0.85),
    ("A.5.7", DORA, "Art. 6", "supports", 0.80),
    ("A.5.36", DORA, "Art. 6", "supports", 0.80),
    ("A.8.1", DORA, "Art. 7", "maps-to", 0.80),
    ("A.8.6", DORA, "Art. 7", "supports", 0.80),
    ("A.8.9", DORA, "Art. 7", "supports", 0.80),
    ("A.8.25", DORA, "Art. 7", "supports", 0.80),
    ("A.5.9", DORA, "Art. 8", "maps-to", 0.90),
    ("A.5.10", DORA, "Art. 8", "supports", 0.80),
    ("A.5.12", DORA, "Art. 8", "supports", 0.85),
    ("A.5.13", DORA, "Art. 8", "supports", 0.85),
    ("A.8.9", DORA, "Art. 8", "supports", 0.80),
    ("A.5.15", DORA, "Art. 9", "maps-to", 0.90),
    ("A.5.16", DORA, "Art. 9", "supports", 0.85),
    ("A.5.17", DORA, "Art. 9", "maps-to", 0.85),
    ("A.6.3", DORA, "Art. 9", "supports", 0.80),
    ("A.8.2", DORA, "Art. 9", "supports", 0.85),
    ("A.8.3", DORA, "Art. 9", "supports", 0.85),
    ("A.8.5", DORA, "Art. 9", "maps-to", 0.85),
    ("A.8.7", DORA, "Art. 9", "supports", 0.80),
    ("A.8.20", DORA, "Art. 9", "supports", 0.85),
    ("A.8.22", DORA, "Art. 9", "supports", 0.80),
    ("A.8.24", DORA, "Art. 9", "maps-to", 0.90),
    ("A.8.15", DORA, "Art. 10", "maps-to", 0.90),
    ("A.8.16", DORA, "Art. 10", "maps-to", 0.90),
    ("A.8.17", DORA, "Art. 10", "supports", 0.80),
    ("A.5.24", DORA, "Art. 11", "maps-to", 0.85),
    ("A.5.26", DORA, "Art. 11", "maps-to", 0.85),
    ("A.5.29", DORA, "Art. 11", "maps-to", 0.90),
    ("A.5.30", DORA, "Art. 11", "maps-to", 0.85),
    ("A.8.13", DORA, "Art. 12", "maps-to", 0.90),
    ("A.8.14", DORA, "Art. 12", "maps-to", 0.85),
    ("A.5.7", DORA, "Art. 13", "maps-to", 0.85),
    ("A.5.27", DORA, "Art. 13", "maps-to", 0.85),
    ("A.6.3", DORA, "Art. 13", "supports", 0.75),
    ("A.8.8", DORA, "Art. 13", "supports", 0.80),
    ("A.5.24", DORA, "Art. 14", "supports", 0.80),
    ("A.5.26", DORA, "Art. 14", "supports", 0.80),
    ("A.5.24", DORA, "Art. 17", "maps-to", 0.90),
    ("A.5.25", DORA, "Art. 17", "maps-to", 0.90),
    ("A.5.26", DORA, "Art. 17", "maps-to", 0.85),
    ("A.5.25", DORA, "Art. 18", "maps-to", 0.85),
    ("A.5.19", DORA, "Art. 28", "maps-to", 0.85),
    ("A.5.20", DORA, "Art. 28", "maps-to", 0.85),
    ("A.5.21", DORA, "Art. 28", "supports", 0.80),
    ("A.5.22", DORA, "Art. 28", "supports", 0.80),
    ("A.5.23", DORA, "Art. 28", "supports", 0.80),

    # --- PCI DSS v4.0.1 (39 mappings) ---
    ("A.8.20", PCI, "Req. 1", "maps-to", 0.85),
    ("A.8.21", PCI, "Req. 1", "supports", 0.80),
    ("A.8.22", PCI, "Req. 1", "maps-to", 0.85),
    ("A.8.9", PCI, "Req. 2", "maps-to", 0.85),
    ("A.8.27", PCI, "Req. 2", "supports", 0.80),
    ("A.8.24", PCI, "Req. 3", "maps-to", 0.80),
    ("A.5.33", PCI, "Req. 3", "supports", 0.75),
    ("A.8.11", PCI, "Req. 3", "supports", 0.75),
    ("A.8.10", PCI, "Req. 3", "supports", 0.70),
    ("A.8.24", PCI, "Req. 4", "maps-to", 0.90),
    ("A.8.20", PCI, "Req. 4", "supports", 0.80),
    ("A.8.7", PCI, "Req. 5", "maps-to", 0.90),
    ("A.5.32", PCI, "Req. 5", "supports", 0.80),
    ("A.8.8", PCI, "Req. 6", "maps-to", 0.85),
    ("A.8.25", PCI, "Req. 6", "maps-to", 0.85),
    ("A.8.26", PCI, "Req. 6", "supports", 0.80),
    ("A.8.28", PCI, "Req. 6", "supports", 0.80),
    ("A.8.31", PCI, "Req. 6", "supports", 0.80),
    ("A.8.32", PCI, "Req. 6", "supports", 0.80),
    ("A.5.15", PCI, "Req. 7", "maps-to", 0.90),
    ("A.8.3", PCI, "Req. 7", "supports", 0.85),
    ("A.5.16", PCI, "Req. 8", "maps-to", 0.85),
    ("A.5.17", PCI, "Req. 8", "maps-to", 0.85),
    ("A.8.2", PCI, "Req. 8", "supports", 0.80),
    ("A.8.5", PCI, "Req. 8", "maps-to", 0.90),
    ("A.7.1", PCI, "Req. 9", "maps-to", 0.85),
    ("A.7.2", PCI, "Req. 9", "maps-to", 0.85),
    ("A.7.3", PCI, "Req. 9", "supports", 0.80),
    ("A.7.4", PCI, "Req. 9", "supports", 0.80),
    ("A.7.10", PCI, "Req. 9", "supports", 0.80),
    ("A.8.15", PCI, "Req. 10", "maps-to", 0.90),
    ("A.8.16", PCI, "Req. 10", "supports", 0.85),
    ("A.8.17", PCI, "Req. 10", "supports", 0.80),
    ("A.8.8", PCI, "Req. 11", "supports", 0.80),
    ("A.8.34", PCI, "Req. 11", "supports", 0.75),
    ("A.5.35", PCI, "Req. 11", "supports", 0.75),
    ("A.5.1", PCI, "Req. 12", "maps-to", 0.85),
    ("A.5.2", PCI, "Req. 12", "supports", 0.80),
    ("A.6.3", PCI, "Req. 12", "supports", 0.80),

    # --- EU AI Act (30 mappings) ---
    ("A.5.1", AIACT, "Art. 8", "supports", 0.75),
    ("A.5.36", AIACT, "Art. 8", "supports", 0.70),
    ("A.5.1", AIACT, "Art. 9", "supports", 0.80),
    ("A.5.7", AIACT, "Art. 9", "supports", 0.75),
    ("A.5.8", AIACT, "Art. 9", "supports", 0.80),
    ("A.5.9", AIACT, "Art. 10", "supports", 0.75),
    ("A.5.10", AIACT, "Art. 10", "supports", 0.70),
    ("A.5.12", AIACT, "Art. 10", "supports", 0.75),
    ("A.5.13", AIACT, "Art. 10", "supports", 0.75),
    ("A.8.11", AIACT, "Art. 10", "supports", 0.70),
    ("A.5.33", AIACT, "Art. 11", "supports", 0.75),
    ("A.5.37", AIACT, "Art. 11", "supports", 0.70),
    ("A.8.15", AIACT, "Art. 12", "maps-to", 0.80),
    ("A.8.17", AIACT, "Art. 12", "supports", 0.75),
    ("A.5.33", AIACT, "Art. 12", "supports", 0.75),
    ("A.5.37", AIACT, "Art. 13", "supports", 0.70),
    ("A.5.10", AIACT, "Art. 13", "supports", 0.65),
    ("A.5.4", AIACT, "Art. 14", "supports", 0.70),
    ("A.5.15", AIACT, "Art. 14", "supports", 0.65),
    ("A.8.2", AIACT, "Art. 14", "supports", 0.65),
    ("A.8.7", AIACT, "Art. 15", "supports", 0.80),
    ("A.8.8", AIACT, "Art. 15", "supports", 0.80),
    ("A.8.9", AIACT, "Art. 15", "supports", 0.75),
    ("A.8.20", AIACT, "Art. 15", "supports", 0.80),
    ("A.8.24", AIACT, "Art. 15", "supports", 0.80),
    ("A.8.25", AIACT, "Art. 15", "maps-to", 0.80),
    ("A.8.28", AIACT, "Art. 15", "supports", 0.75),
    ("A.8.29", AIACT, "Art. 15", "supports", 0.75),
    ("A.5.34", AIACT, "Art. 27", "supports", 0.75),
    ("A.5.8", AIACT, "Art. 27", "supports", 0.70),
]


def load_regulatory_mappings() -> list:
    """Convert inline regulatory mapping tuples to mapping records."""
    mappings = []
    source_refs = {
        GDPR: "NQA GDPR v ISO 27001 Mapping Table; IsecT ISO 27002 GDPR controls",
        NDSG: "Swiss nFADP structural alignment with GDPR Art. 32 equivalent (Art. 7)",
        NIS2: "DataGuard NIS2 to ISO 27001:2022 Mapping; ENISA Technical Guidance (2025)",
        DORA: "Ceeyu/Copla DORA-ISO 27001 Mapping Guide",
        PCI: "ISACA PCI DSS and ISO 27001 Comparison (2016, updated for v4.0.1)",
        AIACT: "ISACA ISO 42001 and EU AI Act Pairing; VibyLabs Alignment Guide",
    }

    for iso_ctrl, reg_fw, reg_article, mtype, confidence in REGULATORY_MAPPINGS:
        mappings.append({
            "source_framework": ISO,
            "source_id": iso_ctrl,
            "target_framework": reg_fw,
            "target_id": reg_article,
            "mapping_type": mtype,
            "confidence": confidence,
            "source_reference": source_refs.get(reg_fw, ""),
            "notes": ""
        })

    return mappings


# ============================================================================
# AXIS 6: ISO 27001:2022 ↔ OWASP Top 10:2025
# Source: OWASP mapping to ISO controls (web security focus)
# ============================================================================

OWASP_MAPPINGS = [
    # A01:2025 Broken Access Control
    ("A.5.15", "A01:2025", "maps-to", 0.90, "Access control policy"),
    ("A.8.2", "A01:2025", "maps-to", 0.85, "Privileged access rights"),
    ("A.8.3", "A01:2025", "maps-to", 0.85, "Information access restriction"),
    ("A.8.5", "A01:2025", "supports", 0.80, "Secure authentication"),
    ("A.5.16", "A01:2025", "supports", 0.80, "Identity management"),
    # A02:2025 Security Misconfiguration
    ("A.8.9", "A02:2025", "maps-to", 0.90, "Configuration management"),
    ("A.8.19", "A02:2025", "supports", 0.80, "Software installation controls"),
    ("A.8.27", "A02:2025", "supports", 0.80, "Secure system architecture"),
    # A03:2025 Software Supply Chain Failures
    ("A.5.19", "A03:2025", "maps-to", 0.85, "Supplier relationships"),
    ("A.5.21", "A03:2025", "maps-to", 0.85, "ICT supply chain security"),
    ("A.8.25", "A03:2025", "supports", 0.80, "Secure development lifecycle"),
    ("A.8.30", "A03:2025", "supports", 0.80, "Outsourced development"),
    # A04:2025 Injection
    ("A.8.28", "A04:2025", "maps-to", 0.90, "Secure coding"),
    ("A.8.26", "A04:2025", "maps-to", 0.85, "Application security requirements"),
    ("A.8.29", "A04:2025", "supports", 0.80, "Security testing"),
    # A05:2025 Cryptographic Failures
    ("A.8.24", "A05:2025", "maps-to", 0.95, "Use of cryptography"),
    ("A.5.14", "A05:2025", "supports", 0.80, "Information transfer"),
    # A06:2025 Identification and Authentication Failures
    ("A.5.17", "A06:2025", "maps-to", 0.90, "Authentication information"),
    ("A.8.5", "A06:2025", "maps-to", 0.90, "Secure authentication"),
    ("A.5.16", "A06:2025", "supports", 0.85, "Identity management"),
    # A07:2025 Cross-Site Scripting (XSS)
    ("A.8.28", "A07:2025", "maps-to", 0.85, "Secure coding — output encoding"),
    ("A.8.26", "A07:2025", "supports", 0.80, "Application security requirements"),
    # A08:2025 Insecure Design
    ("A.8.25", "A08:2025", "maps-to", 0.90, "Secure development lifecycle"),
    ("A.8.27", "A08:2025", "maps-to", 0.85, "Secure system architecture"),
    ("A.5.8", "A08:2025", "supports", 0.80, "Security in project management"),
    # A09:2025 Security Logging and Monitoring Failures
    ("A.8.15", "A09:2025", "maps-to", 0.90, "Logging"),
    ("A.8.16", "A09:2025", "maps-to", 0.90, "Monitoring activities"),
    ("A.8.17", "A09:2025", "supports", 0.80, "Clock synchronisation"),
    # A10:2025 Mishandling of Exceptional Conditions
    ("A.8.28", "A10:2025", "maps-to", 0.85, "Secure coding — error handling"),
    ("A.8.25", "A10:2025", "supports", 0.80, "Secure development lifecycle"),
    ("A.8.29", "A10:2025", "supports", 0.80, "Security testing"),
]


def load_owasp_mappings() -> list:
    """Convert inline OWASP mapping tuples to mapping records."""
    mappings = []
    for iso_ctrl, owasp_id, mtype, confidence, notes in OWASP_MAPPINGS:
        mappings.append({
            "source_framework": ISO,
            "source_id": iso_ctrl,
            "target_framework": OWASP,
            "target_id": owasp_id,
            "mapping_type": mtype,
            "confidence": confidence,
            "source_reference": "OWASP Top 10:2025 to ISO 27001:2022 control mapping",
            "notes": notes
        })
    return mappings


# ============================================================================
# MAIN ASSEMBLER
# ============================================================================
def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    print("Assembling cross-framework crosswalk raw data...\n")

    # Load all mapping axes
    csf = load_csf_mappings()
    print(f"  Axis 1: ISO ↔ NIST CSF 2.0         {len(csf):5d} mappings")

    nist_53 = load_nist_800_53_mappings()
    print(f"  Axis 2: ISO ↔ NIST 800-53 R5        {len(nist_53):5d} mappings")

    cis = load_cis_mappings()
    print(f"  Axis 3: ISO ↔ CIS Controls v8        {len(cis):5d} mappings")

    mitre = load_mitre_mappings()
    print(f"  Axis 4: NIST 800-53 ↔ MITRE ATT&CK   {len(mitre):5d} mappings")

    regulatory = load_regulatory_mappings()
    print(f"  Axis 5: ISO ↔ Regulatory              {len(regulatory):5d} mappings")

    owasp = load_owasp_mappings()
    print(f"  Axis 6: ISO ↔ OWASP Top 10:2025       {len(owasp):5d} mappings")

    all_mappings = csf + nist_53 + cis + mitre + regulatory + owasp

    print(f"\n  TOTAL: {len(all_mappings)} mapping relationships")

    # Build the raw crosswalk file
    raw_data = {
        "description": "Cross-framework crosswalk mapping data for ISMS CORE Platform",
        "version": "1.0",
        "generated_by": "assemble_crosswalk_raw.py",
        "sources": {
            "nist_csf": "NIST Informative References (OLIR catalog, referenceId=154)",
            "nist_800_53": "NIST CSRC sp800-53r5-to-iso-27001-mapping.docx (Table 2)",
            "cis_v8": "CIS Controls v8.1 Mapping to ISO/IEC 27001:2022",
            "mitre_attack": "CTID Mappings Explorer — NIST 800-53 Rev 5 to ATT&CK",
            "regulatory": "DataGuard, NQA, ENISA, Ceeyu, ISACA published mapping guides",
            "owasp": "OWASP Top 10:2025 to ISO 27001:2022 control mapping"
        },
        "mapping_axes": {
            f"{ISO} ↔ {CSF}": len(csf),
            f"{ISO} ↔ {NIST}": len(nist_53),
            f"{ISO} ↔ {CIS}": len(cis),
            f"{NIST} ↔ {MITRE}": len(mitre),
            f"{ISO} ↔ Regulatory": len(regulatory),
            f"{ISO} ↔ {OWASP}": len(owasp),
        },
        "mappings": all_mappings
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(raw_data, f, indent=2, ensure_ascii=False)

    print(f"\n  Output: {OUTPUT_FILE}")
    print(f"  Size:   {OUTPUT_FILE.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
