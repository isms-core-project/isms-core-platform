#!/usr/bin/env python3
"""
Auto-generate crosswalk mappings for ISO 27000-family extension standards.

Pipeline:
  raw/iso27017_cloud.json   ─┐
  raw/iso27018_pii_cloud.json ├─► data/crosswalk.json (patched in-place)
  raw/iso27701_privacy.json  ─┘

Each extension control already declares maps_to_iso27001_2022[] in its raw data.
This script harvests those declared mappings and injects them into the crosswalk
bundle — no manual research required.

Mapping direction: ISO 27001:2022 ↔ ISO 2701X/2702X
  source = ISO 27001:2022 control (e.g. A.5.34)
  target = ISO extension control (e.g. ISO27701:6.2.1)

Run from repo root:
  python3 60-isms-core-api/datasets/scripts/generate_iso_extension_crosswalk.py

Or from datasets/ directory:
  python3 scripts/generate_iso_extension_crosswalk.py
"""

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
RAW_DIR = SCRIPT_DIR.parent / "raw"
DATA_DIR = SCRIPT_DIR.parent / "data"

ISMS_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")

# ISO extension frameworks to process — maps raw file → framework code
ISO_EXTENSIONS = [
    ("iso27017_cloud.json", "ISO27017"),
    ("iso27018_pii_cloud.json", "ISO27018"),
    ("iso27701_privacy.json", "ISO27701"),
]

# Confidence levels for declared mappings (taken from standard text, not inferred)
DECLARED_CONFIDENCE = 0.95


def stable_uuid(key: str) -> str:
    return str(uuid.uuid5(ISMS_NAMESPACE, key))


def control_uuid(fw_code: str, control_id: str) -> str:
    return stable_uuid(f"control:{fw_code}:{control_id}")


def mapping_uuid(src_fw: str, src_id: str, tgt_fw: str, tgt_id: str) -> str:
    src_uuid = control_uuid(src_fw, src_id)
    tgt_uuid = control_uuid(tgt_fw, tgt_id)
    return stable_uuid(f"mapping:{src_uuid}:{tgt_uuid}:maps-to")


def load_crosswalk() -> dict:
    cw_path = DATA_DIR / "crosswalk.json"
    with open(cw_path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_crosswalk(bundle: dict) -> None:
    cw_path = DATA_DIR / "crosswalk.json"
    with open(cw_path, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)


def existing_mapping_ids(crosswalk: dict) -> set:
    """Collect all existing object IDs to avoid duplicates."""
    return {obj["id"] for obj in crosswalk.get("objects", [])}


def generate_mappings_for_extension(raw_file: Path, fw_code: str) -> list:
    """
    Read an ISO extension raw JSON and produce crosswalk mapping objects.

    Each control's maps_to_iso27001_2022[] list declares which ISO 27001:2022
    controls it maps to. We emit bidirectional mappings:
      ISO27001_2022 → ISO_EXTENSION  (source = ISO 27001)
    """
    with open(raw_file, "r", encoding="utf-8") as f:
        raw = json.load(f)

    fw_name = raw["framework"]["name"]
    mappings = []

    for ctrl in raw.get("controls", []):
        ext_ctrl_id = ctrl["id"]
        ext_ctrl_title = ctrl["title"]
        iso_refs = ctrl.get("maps_to_iso27001_2022", [])

        if not iso_refs:
            print(f"  NOTE {fw_code}:{ext_ctrl_id} — no maps_to_iso27001_2022")
            continue

        for iso_ref in iso_refs:
            # Normalise: strip leading 'A.' prefix inconsistencies
            iso_id = iso_ref.strip()

            mapping_id = mapping_uuid("ISO27001_2022", iso_id, fw_code, ext_ctrl_id)

            mappings.append({
                "type": "cross_framework_mapping",
                "id": mapping_id,
                "source_framework": "ISO27001_2022",
                "source_control_id": iso_id,
                "source_control_uuid": control_uuid("ISO27001_2022", iso_id),
                "target_framework": fw_code,
                "target_control_id": ext_ctrl_id,
                "target_control_uuid": control_uuid(fw_code, ext_ctrl_id),
                "target_control_title": ext_ctrl_title,
                "mapping_type": "maps-to",
                "confidence": DECLARED_CONFIDENCE,
                "source_reference": f"{fw_name} — declared maps_to_iso27001_2022 in standard text",
                "notes": f"{fw_code} {ext_ctrl_id} ({ext_ctrl_title}) extends ISO 27001:2022 {iso_id}"
            })

    return mappings


def update_crosswalk_axis_count(crosswalk: dict, fw_code: str, count: int) -> None:
    """Update or add the mapping axis count in the crosswalk metadata."""
    axis_key = f"ISO27001_2022 ↔ {fw_code}"
    if "mapping_axes" not in crosswalk:
        crosswalk["mapping_axes"] = {}
    crosswalk["mapping_axes"][axis_key] = count


def main():
    crosswalk = load_crosswalk()
    existing_ids = existing_mapping_ids(crosswalk)

    total_added = 0
    total_skipped = 0

    for raw_filename, fw_code in ISO_EXTENSIONS:
        raw_file = RAW_DIR / raw_filename
        if not raw_file.exists():
            print(f"  SKIP {fw_code}: {raw_filename} not found in {RAW_DIR}")
            continue

        mappings = generate_mappings_for_extension(raw_file, fw_code)
        added = 0
        skipped = 0

        for m in mappings:
            if m["id"] in existing_ids:
                skipped += 1
                continue
            crosswalk["objects"].append(m)
            existing_ids.add(m["id"])
            added += 1

        # Update axis count in metadata
        update_crosswalk_axis_count(crosswalk, fw_code, added + skipped)

        total_added += added
        total_skipped += skipped
        print(f"  {fw_code:15s}: {added:3d} added, {skipped:3d} already existed "
              f"({len(mappings)} total mappings from {raw_filename})")

    # Update bundle metadata
    crosswalk["objects_count"] = len(crosswalk["objects"])
    crosswalk["generated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    crosswalk["generator"] = "generate_iso_extension_crosswalk.py"

    save_crosswalk(crosswalk)

    print(f"\n  TOTAL: {total_added} new mappings added, {total_skipped} already existed")
    print(f"  Crosswalk now has {crosswalk['objects_count']} objects")
    print(f"  Saved → {DATA_DIR / 'crosswalk.json'}")


if __name__ == "__main__":
    main()
