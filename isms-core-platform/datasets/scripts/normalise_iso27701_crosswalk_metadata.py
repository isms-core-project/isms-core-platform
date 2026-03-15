"""
Fix ISO 27701 crosswalk entries + inject ISMS Copilot framework_mappings metadata.

Problem 1: 53 existing ISO 27701 ↔ ISO 27001 crosswalk entries use string control IDs
           ("A.5.31", "5.2.1") instead of UUIDs. The loader calls uuid.UUID(obj["source_control_id"])
           which fails, causing all 53 entries to be skipped → Coverage shows 0.
Fix:       Swap source_control_uuid → source_control_id and target_control_uuid → target_control_id.

Problem 2: 80 ISMS Copilot mappings (ISO 27701 → ISO 27017/27018/GDPR) cannot be stored as
           CrossFrameworkMapping records because target controls (theme slugs, GDPR articles)
           don't exist as FrameworkControl rows.
Fix:       Store as metadata["framework_mappings"] on each ISO 27701 control in iso27701_privacy.json.
           The bundle loader reads obj.get("metadata", {}) → stored in FrameworkControl.metadata_ JSONB.
"""

import json
import hashlib
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
CROSSWALK_FILE = DATA_DIR / "crosswalk.json"
ISO27701_FILE = DATA_DIR / "iso27701_privacy.json"

# ---------------------------------------------------------------------------
# ISMS Copilot mapping data (all 5 parts merged)
# ---------------------------------------------------------------------------
COPILOT_MAPPINGS = [
    # Part 1 — clauses 4.1 through 7.5.3
    {"control_id": "4.1", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 24", "Art. 28"]}},
    {"control_id": "4.2", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 24", "Art. 37"]}},
    {"control_id": "4.3", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["records-audit"], "gdpr": ["Art. 24", "Art. 30"]}},
    {"control_id": "4.4", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 24", "Art. 25(1)"]}},
    {"control_id": "5.1", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 24"]}},
    {"control_id": "5.2", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["transparency-disclosure", "use-limitation"], "gdpr": ["Art. 5(1)(a)", "Art. 24"]}},
    {"control_id": "5.3", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["records-audit"], "gdpr": ["Art. 24", "Art. 37", "Art. 38", "Art. 39"]}},
    {"control_id": "6.1.1", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 24", "Art. 25(1)", "Art. 32(2)"]}},
    {"control_id": "6.1.2", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 32(2)", "Art. 35(1)", "Art. 35(7)"]}},
    {"control_id": "6.1.3", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 25(1)", "Art. 32(1)", "Art. 35(7)"]}},
    {"control_id": "6.2", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 24", "Art. 25(1)"]}},
    {"control_id": "6.3", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 25(1)"]}},
    {"control_id": "7.1", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 24"]}},
    {"control_id": "7.2", "framework_mappings": {"iso_27017": [], "iso_27018": ["staff-confidentiality"], "gdpr": ["Art. 24", "Art. 29"]}},
    {"control_id": "7.3", "framework_mappings": {"iso_27017": [], "iso_27018": ["staff-confidentiality"], "gdpr": ["Art. 24", "Art. 29"]}},
    {"control_id": "7.4", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 24", "Art. 31"]}},
    {"control_id": "7.5.1", "framework_mappings": {"iso_27017": ["records-audit"], "iso_27018": ["records-audit"], "gdpr": ["Art. 5(1)(a)", "Art. 24", "Art. 30"]}},
    {"control_id": "7.5.2", "framework_mappings": {"iso_27017": [], "iso_27018": ["records-audit"], "gdpr": ["Art. 24", "Art. 30"]}},
    {"control_id": "7.5.3", "framework_mappings": {"iso_27017": [], "iso_27018": ["records-audit"], "gdpr": ["Art. 24", "Art. 30"]}},
    # Part 2 — clauses 8.1 through A.1.2.9
    {"control_id": "8.1", "framework_mappings": {"iso_27017": ["cloud-operations-security"], "iso_27018": ["use-limitation", "records-audit"], "gdpr": ["Art. 24", "Art. 25(1)", "Art. 32(1)"]}},
    {"control_id": "8.2", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 32(2)", "Art. 35(1)", "Art. 35(7)"]}},
    {"control_id": "8.3", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 25(1)", "Art. 32(1)", "Art. 35(7)"]}},
    {"control_id": "9.1", "framework_mappings": {"iso_27017": ["cloud-logging-monitoring"], "iso_27018": ["records-audit"], "gdpr": ["Art. 24", "Art. 32(1)(d)"]}},
    {"control_id": "9.2.1", "framework_mappings": {"iso_27017": [], "iso_27018": ["records-audit"], "gdpr": ["Art. 24", "Art. 32(1)(d)"]}},
    {"control_id": "9.2.2", "framework_mappings": {"iso_27017": [], "iso_27018": ["records-audit"], "gdpr": ["Art. 24", "Art. 32(1)(d)"]}},
    {"control_id": "9.3.1", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 24"]}},
    {"control_id": "9.3.2", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 24", "Art. 32(1)(d)"]}},
    {"control_id": "9.3.3", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 24"]}},
    {"control_id": "10.1", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 24", "Art. 25(1)"]}},
    {"control_id": "10.2", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 24", "Art. 33(5)"]}},
    {"control_id": "A.1.2.2", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["use-limitation", "transparency-disclosure"], "gdpr": ["Art. 5(1)(a)", "Art. 6", "Art. 13", "Art. 14"]}},
    {"control_id": "A.1.2.3", "framework_mappings": {"iso_27017": [], "iso_27018": ["use-limitation"], "gdpr": ["Art. 6", "Art. 7", "Art. 9(2)"]}},
    {"control_id": "A.1.2.4", "framework_mappings": {"iso_27017": [], "iso_27018": ["consent-management"], "gdpr": ["Art. 7", "Art. 8"]}},
    {"control_id": "A.1.2.5", "framework_mappings": {"iso_27017": [], "iso_27018": ["consent-management", "records-audit"], "gdpr": ["Art. 7", "Art. 9(2)(a)"]}},
    {"control_id": "A.1.2.6", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 35(1)", "Art. 35(7)", "Art. 36"]}},
    {"control_id": "A.1.2.7", "framework_mappings": {"iso_27017": ["cloud-supplier-relationships"], "iso_27018": ["sub-processor-management"], "gdpr": ["Art. 28", "Art. 28(3)"]}},
    {"control_id": "A.1.2.8", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": [], "gdpr": ["Art. 26"]}},
    {"control_id": "A.1.2.9", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["records-audit"], "gdpr": ["Art. 30", "Art. 30(1)"]}},
    # Part 3 — A.1.3 and A.1.4
    {"control_id": "A.1.3.2", "framework_mappings": {"iso_27017": [], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 12(3)", "Art. 13", "Art. 14"]}},
    {"control_id": "A.1.3.3", "framework_mappings": {"iso_27017": [], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 13", "Art. 14"]}},
    {"control_id": "A.1.3.4", "framework_mappings": {"iso_27017": [], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 13", "Art. 14"]}},
    {"control_id": "A.1.3.5", "framework_mappings": {"iso_27017": [], "iso_27018": ["consent-management"], "gdpr": ["Art. 7", "Art. 17", "Art. 21"]}},
    {"control_id": "A.1.3.6", "framework_mappings": {"iso_27017": [], "iso_27018": ["use-limitation"], "gdpr": ["Art. 18", "Art. 21"]}},
    {"control_id": "A.1.3.7", "framework_mappings": {"iso_27017": ["cloud-data-deletion-return"], "iso_27018": ["data-return-deletion"], "gdpr": ["Art. 15", "Art. 16", "Art. 17"]}},
    {"control_id": "A.1.3.8", "framework_mappings": {"iso_27017": [], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 17", "Art. 19"]}},
    {"control_id": "A.1.3.9", "framework_mappings": {"iso_27017": [], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 15", "Art. 20"]}},
    {"control_id": "A.1.3.10", "framework_mappings": {"iso_27017": [], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 12(3)", "Art. 15", "Art. 16", "Art. 17", "Art. 18", "Art. 19", "Art. 20", "Art. 21"]}},
    {"control_id": "A.1.3.11", "framework_mappings": {"iso_27017": [], "iso_27018": [], "gdpr": ["Art. 22"]}},
    {"control_id": "A.1.4.2", "framework_mappings": {"iso_27017": ["cloud-asset-management"], "iso_27018": ["data-minimization"], "gdpr": ["Art. 5(1)(c)", "Art. 25(2)"]}},
    {"control_id": "A.1.4.3", "framework_mappings": {"iso_27017": ["cloud-operations-security"], "iso_27018": ["use-limitation"], "gdpr": ["Art. 5(1)(c)", "Art. 25(1)", "Art. 25(2)"]}},
    {"control_id": "A.1.4.4", "framework_mappings": {"iso_27017": [], "iso_27018": ["data-minimization"], "gdpr": ["Art. 5(1)(c)", "Art. 16"]}},
    {"control_id": "A.1.4.5", "framework_mappings": {"iso_27017": ["cloud-asset-management"], "iso_27018": ["data-minimization"], "gdpr": ["Art. 5(1)(c)", "Art. 25(1)", "Art. 25(2)"]}},
    {"control_id": "A.1.4.6", "framework_mappings": {"iso_27017": ["cloud-data-deletion-return"], "iso_27018": ["data-return-deletion"], "gdpr": ["Art. 5(1)(e)", "Art. 17"]}},
    {"control_id": "A.1.4.7", "framework_mappings": {"iso_27017": ["cloud-operations-security"], "iso_27018": ["data-minimization"], "gdpr": ["Art. 5(1)(e)", "Art. 32(1)"]}},
    {"control_id": "A.1.4.8", "framework_mappings": {"iso_27017": ["cloud-asset-management"], "iso_27018": ["data-return-deletion"], "gdpr": ["Art. 5(1)(e)"]}},
    {"control_id": "A.1.4.9", "framework_mappings": {"iso_27017": ["cloud-data-deletion-return"], "iso_27018": ["data-return-deletion"], "gdpr": ["Art. 5(1)(e)", "Art. 17"]}},
    {"control_id": "A.1.4.10", "framework_mappings": {"iso_27017": ["cloud-network-security"], "iso_27018": ["encryption-transmission"], "gdpr": ["Art. 32(1)(a)", "Art. 32(1)(b)"]}},
    # Part 4 — A.1.5 and full A.2
    {"control_id": "A.1.5.2", "framework_mappings": {"iso_27017": ["cloud-compliance"], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 44", "Art. 45", "Art. 46", "Art. 49"]}},
    {"control_id": "A.1.5.3", "framework_mappings": {"iso_27017": ["cloud-compliance"], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 44", "Art. 45", "Art. 46", "Art. 47"]}},
    {"control_id": "A.1.5.4", "framework_mappings": {"iso_27017": [], "iso_27018": ["records-audit"], "gdpr": ["Art. 30", "Art. 44", "Art. 46"]}},
    {"control_id": "A.1.5.5", "framework_mappings": {"iso_27017": [], "iso_27018": ["records-audit", "government-disclosure"], "gdpr": ["Art. 30", "Art. 48"]}},
    {"control_id": "A.2.2.2", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities", "cloud-supplier-relationships"], "iso_27018": ["use-limitation", "records-audit"], "gdpr": ["Art. 28", "Art. 28(3)", "Art. 29"]}},
    {"control_id": "A.2.2.3", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["use-limitation"], "gdpr": ["Art. 28", "Art. 29"]}},
    {"control_id": "A.2.2.4", "framework_mappings": {"iso_27017": [], "iso_27018": ["consent-management", "use-limitation"], "gdpr": ["Art. 28", "Art. 6", "Art. 7"]}},
    {"control_id": "A.2.2.5", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["use-limitation"], "gdpr": ["Art. 28", "Art. 29"]}},
    {"control_id": "A.2.2.6", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 28", "Art. 28(3)"]}},
    {"control_id": "A.2.2.7", "framework_mappings": {"iso_27017": [], "iso_27018": ["records-audit"], "gdpr": ["Art. 30", "Art. 28(3)"]}},
    {"control_id": "A.2.3.2", "framework_mappings": {"iso_27017": [], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 28", "Art. 12(3)", "Art. 15", "Art. 16", "Art. 17"]}},
    {"control_id": "A.2.4.2", "framework_mappings": {"iso_27017": ["cloud-operations-security"], "iso_27018": ["data-minimization"], "gdpr": ["Art. 5(1)(e)", "Art. 32(1)"]}},
    {"control_id": "A.2.4.3", "framework_mappings": {"iso_27017": ["cloud-data-deletion-return"], "iso_27018": ["data-return-deletion"], "gdpr": ["Art. 17", "Art. 28(3)"]}},
    {"control_id": "A.2.4.4", "framework_mappings": {"iso_27017": ["cloud-network-security"], "iso_27018": ["encryption-transmission"], "gdpr": ["Art. 32(1)(a)", "Art. 32(1)(b)"]}},
    {"control_id": "A.2.5.2", "framework_mappings": {"iso_27017": ["cloud-compliance"], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 44", "Art. 46", "Art. 28(3)"]}},
    {"control_id": "A.2.5.3", "framework_mappings": {"iso_27017": ["cloud-compliance"], "iso_27018": ["transparency-disclosure"], "gdpr": ["Art. 44", "Art. 45", "Art. 46"]}},
    {"control_id": "A.2.5.4", "framework_mappings": {"iso_27017": [], "iso_27018": ["records-audit", "government-disclosure"], "gdpr": ["Art. 30", "Art. 48"]}},
    {"control_id": "A.2.5.5", "framework_mappings": {"iso_27017": [], "iso_27018": ["government-disclosure", "transparency-disclosure"], "gdpr": ["Art. 48"]}},
    {"control_id": "A.2.5.6", "framework_mappings": {"iso_27017": [], "iso_27018": ["government-disclosure"], "gdpr": ["Art. 48"]}},
    {"control_id": "A.2.5.7", "framework_mappings": {"iso_27017": ["cloud-supplier-relationships"], "iso_27018": ["sub-processor-management", "transparency-disclosure"], "gdpr": ["Art. 28", "Art. 28(3)"]}},
    {"control_id": "A.2.5.8", "framework_mappings": {"iso_27017": ["cloud-supplier-relationships"], "iso_27018": ["sub-processor-management"], "gdpr": ["Art. 28", "Art. 28(3)"]}},
    {"control_id": "A.2.5.9", "framework_mappings": {"iso_27017": ["cloud-supplier-relationships"], "iso_27018": ["sub-processor-management", "transparency-disclosure"], "gdpr": ["Art. 28", "Art. 28(3)"]}},
    # Part 5 — Annex A.3
    {"control_id": "A.3.3", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["use-limitation"], "gdpr": ["Art. 24", "Art. 32(1)"]}},
    {"control_id": "A.3.4", "framework_mappings": {"iso_27017": ["cloud-roles-responsibilities"], "iso_27018": ["staff-confidentiality"], "gdpr": ["Art. 24", "Art. 29"]}},
    {"control_id": "A.3.5", "framework_mappings": {"iso_27017": ["cloud-asset-management"], "iso_27018": ["data-minimization"], "gdpr": ["Art. 5(1)(f)", "Art. 32(1)"]}},
    {"control_id": "A.3.6", "framework_mappings": {"iso_27017": ["cloud-asset-management"], "iso_27018": ["data-minimization"], "gdpr": ["Art. 5(1)(f)", "Art. 32(1)"]}},
    {"control_id": "A.3.7", "framework_mappings": {"iso_27017": ["cloud-network-security"], "iso_27018": ["encryption-transmission"], "gdpr": ["Art. 32(1)(a)", "Art. 32(1)(b)"]}},
    {"control_id": "A.3.8", "framework_mappings": {"iso_27017": ["cloud-access-control"], "iso_27018": ["access-restriction"], "gdpr": ["Art. 32(1)(b)"]}},
    {"control_id": "A.3.9", "framework_mappings": {"iso_27017": ["cloud-access-control"], "iso_27018": ["access-restriction"], "gdpr": ["Art. 25(1)", "Art. 32(1)(b)"]}},
    {"control_id": "A.3.10", "framework_mappings": {"iso_27017": ["cloud-supplier-relationships"], "iso_27018": ["sub-processor-management"], "gdpr": ["Art. 28", "Art. 28(1)"]}},
    {"control_id": "A.3.11", "framework_mappings": {"iso_27017": ["cloud-incident-management"], "iso_27018": ["breach-notification"], "gdpr": ["Art. 33", "Art. 34"]}},
    {"control_id": "A.3.12", "framework_mappings": {"iso_27017": ["cloud-incident-management"], "iso_27018": ["breach-notification"], "gdpr": ["Art. 33", "Art. 33(1)", "Art. 33(3)", "Art. 34"]}},
    {"control_id": "A.3.13", "framework_mappings": {"iso_27017": ["cloud-compliance"], "iso_27018": ["records-audit"], "gdpr": ["Art. 24", "Art. 44", "Art. 48"]}},
    {"control_id": "A.3.14", "framework_mappings": {"iso_27017": ["cloud-operations-security"], "iso_27018": ["records-audit"], "gdpr": ["Art. 5(1)(f)", "Art. 30", "Art. 32(1)"]}},
    {"control_id": "A.3.15", "framework_mappings": {"iso_27017": ["cloud-compliance"], "iso_27018": ["records-audit"], "gdpr": ["Art. 24", "Art. 32(1)(d)"]}},
    {"control_id": "A.3.16", "framework_mappings": {"iso_27017": ["cloud-compliance"], "iso_27018": ["records-audit"], "gdpr": ["Art. 24", "Art. 32(1)(d)"]}},
    {"control_id": "A.3.17", "framework_mappings": {"iso_27017": [], "iso_27018": ["staff-confidentiality"], "gdpr": ["Art. 24", "Art. 29", "Art. 32(4)"]}},
    {"control_id": "A.3.18", "framework_mappings": {"iso_27017": [], "iso_27018": ["staff-confidentiality"], "gdpr": ["Art. 28(3)", "Art. 29", "Art. 32(4)"]}},
    {"control_id": "A.3.19", "framework_mappings": {"iso_27017": ["cloud-operations-security"], "iso_27018": ["access-restriction"], "gdpr": ["Art. 32(1)(b)"]}},
    {"control_id": "A.3.20", "framework_mappings": {"iso_27017": ["cloud-asset-management"], "iso_27018": ["data-return-deletion"], "gdpr": ["Art. 5(1)(f)", "Art. 32(1)"]}},
    {"control_id": "A.3.21", "framework_mappings": {"iso_27017": ["cloud-asset-management", "cloud-data-deletion-return"], "iso_27018": ["data-return-deletion"], "gdpr": ["Art. 5(1)(f)", "Art. 17", "Art. 32(1)"]}},
    {"control_id": "A.3.22", "framework_mappings": {"iso_27017": ["cloud-access-control"], "iso_27018": ["access-restriction"], "gdpr": ["Art. 32(1)(b)"]}},
    {"control_id": "A.3.23", "framework_mappings": {"iso_27017": ["cloud-access-control"], "iso_27018": ["access-restriction"], "gdpr": ["Art. 25(1)", "Art. 32(1)(b)"]}},
    {"control_id": "A.3.24", "framework_mappings": {"iso_27017": ["cloud-operations-security"], "iso_27018": [], "gdpr": ["Art. 32(1)(b)", "Art. 32(1)(c)"]}},
    {"control_id": "A.3.25", "framework_mappings": {"iso_27017": ["cloud-logging-monitoring"], "iso_27018": ["records-audit"], "gdpr": ["Art. 32(1)(b)", "Art. 32(1)(d)"]}},
    {"control_id": "A.3.26", "framework_mappings": {"iso_27017": ["cloud-cryptography"], "iso_27018": ["encryption-transmission"], "gdpr": ["Art. 32(1)(a)"]}},
    {"control_id": "A.3.27", "framework_mappings": {"iso_27017": ["cloud-virtual-environment"], "iso_27018": [], "gdpr": ["Art. 25(1)", "Art. 32(1)"]}},
    {"control_id": "A.3.28", "framework_mappings": {"iso_27017": ["cloud-virtual-environment"], "iso_27018": [], "gdpr": ["Art. 25(1)", "Art. 32(1)"]}},
    {"control_id": "A.3.29", "framework_mappings": {"iso_27017": ["cloud-virtual-environment"], "iso_27018": [], "gdpr": ["Art. 25(1)", "Art. 32(1)"]}},
    {"control_id": "A.3.30", "framework_mappings": {"iso_27017": ["cloud-supplier-relationships"], "iso_27018": ["sub-processor-management"], "gdpr": ["Art. 28", "Art. 32(1)"]}},
    {"control_id": "A.3.31", "framework_mappings": {"iso_27017": ["cloud-operations-security"], "iso_27018": ["data-minimization"], "gdpr": ["Art. 5(1)(c)", "Art. 32(1)"]}},
]

# ---------------------------------------------------------------------------
# Fix 1 — crosswalk.json: swap string IDs to UUIDs for ISO 27701 entries
# ---------------------------------------------------------------------------
print("=== Fix 1: crosswalk.json — ISO 27701 UUID correction ===")
xw = json.loads(CROSSWALK_FILE.read_text())
fixed = 0
skipped = 0
for obj in xw["objects"]:
    if obj.get("type") != "cross_framework_mapping":
        continue
    if "ISO27701" not in (obj.get("source_framework", "") + obj.get("target_framework", "")):
        continue

    src_uuid = obj.get("source_control_uuid")
    tgt_uuid = obj.get("target_control_uuid")
    if src_uuid and tgt_uuid:
        obj["source_control_id"] = src_uuid
        obj["target_control_id"] = tgt_uuid
        fixed += 1
    else:
        skipped += 1

print(f"  Fixed: {fixed} entries   Skipped (no uuid fields): {skipped}")

# Recompute content hash
controls_json = json.dumps(xw["objects"], sort_keys=True).encode()
xw["content_hash"] = hashlib.sha1(controls_json).hexdigest()
CROSSWALK_FILE.write_text(json.dumps(xw, indent=2, ensure_ascii=False))
print(f"  ✓  crosswalk.json written ({len(xw['objects'])} total objects)")

# ---------------------------------------------------------------------------
# Fix 2 — iso27701_privacy.json: inject framework_mappings into metadata
# ---------------------------------------------------------------------------
print("\n=== Fix 2: iso27701_privacy.json — inject framework_mappings metadata ===")
fw = json.loads(ISO27701_FILE.read_text())

# Build lookup: control_id → mapping entry
mapping_lookup = {m["control_id"]: m["framework_mappings"] for m in COPILOT_MAPPINGS}

injected = 0
not_found = []
for ctrl in fw["controls"]:
    cid = ctrl["control_id"]
    if cid in mapping_lookup:
        if "metadata" not in ctrl:
            ctrl["metadata"] = {}
        ctrl["metadata"]["framework_mappings"] = mapping_lookup[cid]
        injected += 1

# Controls in dataset but not in mapping data (expected: management system clauses
# that don't appear in the Copilot mapping, e.g. 5.2.1, 5.2.2, etc.)
mapped_ids = set(mapping_lookup.keys())
dataset_ids = {c["control_id"] for c in fw["controls"]}
missing_from_mapping = dataset_ids - mapped_ids
not_in_dataset = mapped_ids - dataset_ids

print(f"  Injected: {injected} controls")
if missing_from_mapping:
    print(f"  Controls in dataset with no Copilot mapping ({len(missing_from_mapping)}): "
          f"{sorted(missing_from_mapping)[:10]}{'...' if len(missing_from_mapping) > 10 else ''}")
if not_in_dataset:
    print(f"  WARNING — Copilot control IDs not found in dataset ({len(not_in_dataset)}): "
          f"{sorted(not_in_dataset)}")

# Recompute content hash
controls_json_bytes = json.dumps(fw["controls"], sort_keys=True).encode()
fw["content_hash"] = hashlib.sha1(controls_json_bytes).hexdigest()
ISO27701_FILE.write_text(json.dumps(fw, indent=2, ensure_ascii=False))
print(f"  ✓  iso27701_privacy.json written ({len(fw['controls'])} controls)")

print("\nDone. Re-run 'Load Reference Frameworks' in WebUI to push changes to DB.")
