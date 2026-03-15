#!/usr/bin/env python3
"""
Generate cross-framework crosswalk bundle from raw mapping data.

Pipeline: raw/crosswalk_mappings.json → data/crosswalk.json

Creates CrossFrameworkMapping objects linking controls across frameworks.
All source/target UUIDs are deterministic (UUID5) so they match the
individual framework bundles without needing to load them.

Mapping axes:
  - ISO 27001:2022 ↔ NIST CSF 2.0          (official NIST informative references)
  - ISO 27001:2022 ↔ NIST SP 800-53 R5     (NIST/CPRT published mappings)
  - ISO 27001:2022 ↔ CIS Controls v8       (CIS published mappings)
  - NIST 800-53 ↔ MITRE ATT&CK             (CTID project mappings)
  - ISO 27001:2022 ↔ OWASP Top 10:2025     (web security controls)
  - ISO 27001:2022 ↔ Regulatory frameworks  (GDPR, nFADP, NIS2, DORA, PCI DSS, AI Act)
"""

import json
import uuid
import hashlib
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RAW_DIR = SCRIPT_DIR.parent / "raw"
DATA_DIR = SCRIPT_DIR.parent / "data"
RAW_FILE = RAW_DIR / "crosswalk_mappings.json"
OUTPUT_FILE = DATA_DIR / "crosswalk.json"

ISMS_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")

# Regex for zero-padded NIST control numbers: AC-02, SI-08 etc.
import re
_NIST_PADDED = re.compile(r"^([A-Z]{2})-0(\d)$")
# Regex for NIST enhancement parens: AC-17(1), CM-3(7) etc.
_NIST_PARENS = re.compile(r"\((\d+)\)")


def _normalise_control_id(fw_code: str, control_id: str) -> str:
    """Normalise control_id to match the format used in framework bundles."""
    if fw_code == "NIST_800_53_R5":
        # AC-02 → AC-2  (strip leading zeros in base controls)
        m = _NIST_PADDED.match(control_id)
        if m:
            control_id = f"{m.group(1)}-{m.group(2)}"
        # AC-17(1) → AC-17.1  (parens → dot notation for enhancements)
        control_id = _NIST_PARENS.sub(r".\1", control_id)
    elif fw_code == "CIS_V8":
        # 1.1 → CIS 1.1  (add prefix)
        if not control_id.startswith("CIS "):
            control_id = f"CIS {control_id}"
    return control_id


def stable_uuid(key: str) -> str:
    return str(uuid.uuid5(ISMS_NAMESPACE, key))


def control_uuid(fw_code: str, control_id: str) -> str:
    """Generate the same UUID that individual framework generators produce."""
    return stable_uuid(f"control:{fw_code}:{control_id}")


def section_uuid(fw_code: str, section_id: str) -> str:
    """Generate section UUID matching framework generators."""
    return stable_uuid(f"section:{fw_code}:{section_id}")


def mapping_uuid(source_fw: str, source_id: str, target_fw: str, target_id: str, mapping_type: str) -> str:
    """Deterministic UUID for a mapping relationship."""
    source_uuid = control_uuid(source_fw, source_id)
    target_uuid = control_uuid(target_fw, target_id)
    return stable_uuid(f"mapping:{source_uuid}:{target_uuid}:{mapping_type}")


def generate_bundle() -> dict:
    with open(RAW_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    objects = []
    stats = {}
    skipped = 0

    for m in raw["mappings"]:
        src_fw = m["source_framework"]
        src_id = _normalise_control_id(src_fw, m["source_id"])
        tgt_fw = m["target_framework"]
        tgt_id = _normalise_control_id(tgt_fw, m["target_id"])
        mtype = m.get("mapping_type", "maps-to")
        confidence = m.get("confidence", 0.80)
        source_ref = m.get("source_reference", "")
        notes = m.get("notes", "")

        # Resolve UUIDs using the same deterministic strategy as framework generators
        src_uuid = control_uuid(src_fw, src_id)
        tgt_uuid = control_uuid(tgt_fw, tgt_id)
        m_uuid = mapping_uuid(src_fw, src_id, tgt_fw, tgt_id, mtype)

        objects.append({
            "type": "cross_framework_mapping",
            "id": m_uuid,
            "source_control_id": src_uuid,
            "target_control_id": tgt_uuid,
            "source_framework": src_fw,
            "source_control": src_id,
            "target_framework": tgt_fw,
            "target_control": tgt_id,
            "mapping_type": mtype,
            "confidence": confidence,
            "source_reference": source_ref,
            "notes": notes
        })

        # Track stats per mapping axis
        axis = f"{src_fw} → {tgt_fw}"
        stats[axis] = stats.get(axis, 0) + 1

    content_str = json.dumps(objects, sort_keys=True)
    content_hash = hashlib.sha256(content_str.encode()).hexdigest()

    bundle = {
        "bundle_id": f"bundle--{stable_uuid(f'bundle:crosswalk:{content_hash[:16]}')}",
        "bundle_type": "isms-core-dataset",
        "bundle_version": "1.0",
        "dataset": {
            "name": "ISMS CORE Cross-Framework Crosswalk",
            "version": "1.0",
            "description": "Mapping relationships between ISO 27001:2022 and NIST, CIS, MITRE, OWASP, and regulatory frameworks"
        },
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "generate_crosswalk.py",
        "content_hash": content_hash,
        "objects_count": len(objects),
        "mapping_axes": stats,
        "objects": objects
    }

    return bundle


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not RAW_FILE.exists():
        print(f"ERROR: {RAW_FILE} not found. Create crosswalk_mappings.json first.")
        return

    print(f"Reading crosswalk mappings from {RAW_FILE}")
    bundle = generate_bundle()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)

    print(f"\nGenerated {OUTPUT_FILE.name}:")
    print(f"  Total mappings: {bundle['objects_count']}")
    print(f"  Content hash:   {bundle['content_hash'][:16]}...")
    print(f"\n  Mapping axes:")
    for axis, count in sorted(bundle["mapping_axes"].items()):
        print(f"    {axis:45s} {count:4d}")


if __name__ == "__main__":
    main()
