"""
Add missing cross-framework mappings:
  - ISO 27001 → MITRE ATT&CK (direct tactic/technique mappings)
  - ISO 27001 → OWASP ASVS 4.0 (chapter-level)
  - ISO 27001 → FINMA (all three circulars)

Run from datasets/ directory:
  python3 scripts/add_mitre_owasp_finma_mappings.py
"""
import json
import uuid
from pathlib import Path

DATA = Path(__file__).parent.parent / "data"

# ---------------------------------------------------------------------------
# Load existing datasets
# ---------------------------------------------------------------------------

def load(name):
    with open(DATA / name) as f:
        return json.load(f)

iso_data    = load("iso27001_2022.json")
mitre_data  = load("mitre_attack_v18.json")
owasp_data  = load("owasp.json")
finma_data  = load("finma.json")
crosswalk   = load("crosswalk.json")

# Build lookup: control_id → object_id
def id_map(dataset):
    return {o["control_id"]: o["id"] for o in dataset.get("objects", []) if "control_id" in o}

iso_ids   = id_map(iso_data)
mitre_ids = id_map(mitre_data)
owasp_ids = id_map(owasp_data)
finma_ids = id_map(finma_data)

print(f"ISO controls:   {len(iso_ids)}")
print(f"MITRE entries:  {len(mitre_ids)}")
print(f"OWASP entries:  {len(owasp_ids)}")
print(f"FINMA entries:  {len(finma_ids)}")

# ---------------------------------------------------------------------------
# Dedup: collect existing (source, target) pairs
# ---------------------------------------------------------------------------
existing_pairs = set()
for o in crosswalk["objects"]:
    existing_pairs.add((o["source_control_id"], o["target_control_id"]))

new_mappings = []
skipped = 0

def add(src_iso, tgt_fw_id, tgt_id_str, tgt_fw_code, src_fw_code, mapping_type, confidence, notes):
    global skipped
    src_id = iso_ids.get(src_iso)
    tgt_id = tgt_fw_id.get(tgt_id_str)
    if not src_id:
        print(f"  WARN: ISO control not found: {src_iso}")
        return
    if not tgt_id:
        print(f"  WARN: Target control not found: {tgt_id_str}")
        return
    if (src_id, tgt_id) in existing_pairs:
        skipped += 1
        return
    existing_pairs.add((src_id, tgt_id))
    new_mappings.append({
        "type": "cross_framework_mapping",
        "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{src_id}:{tgt_id}")),
        "source_control_id": src_id,
        "target_control_id": tgt_id,
        "source_framework": src_fw_code,
        "source_control": src_iso,
        "target_framework": tgt_fw_code,
        "target_control": tgt_id_str,
        "mapping_type": mapping_type,
        "confidence": confidence,
        "source_reference": "ISMS CORE mapping — see add_mitre_owasp_finma_mappings.py",
        "notes": notes,
    })

# ===========================================================================
# 1. ISO 27001 → MITRE ATT&CK (direct tactic + key technique mappings)
#    Reference: MITRE ATT&CK Mappings to Security Controls (CTID project),
#               NIST 800-53 ↔ ATT&CK mappings, ISO/IEC 27001:2022 Annex A
# ===========================================================================
print("\n--- ISO 27001 → MITRE ATT&CK ---")

M = mitre_ids  # shorthand

# A.5.7 Threat intelligence
# TTI directly covers adversary reconnaissance and resource development TTPs
add("A.5.7", M, "TA0043", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.90,
    "Threat intelligence informs defence against Reconnaissance tactics")
add("A.5.7", M, "TA0042", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "Threat intelligence covers adversary Resource Development tradecraft")

# A.8.8 Management of technical vulnerabilities
# Patching closes the exploitation surface exploited in these techniques
add("A.8.8", M, "TA0001", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "Timely patching reduces Initial Access via known vulnerabilities")
add("A.8.8", M, "T1190", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.95,
    "Patch management directly mitigates Exploit Public-Facing Application (T1190)")
add("A.8.8", M, "T1203", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "Patching client software mitigates Exploitation for Client Execution (T1203)")
add("A.8.8", M, "T1068", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "Privilege escalation via exploitation is mitigated by OS/software patching")

# A.8.16 Monitoring activities
# Monitoring detects adversary activity across multiple tactics
add("A.8.16", M, "TA0005", "MITRE_ATTACK_V18", "ISO27001_2022", "detects", 0.85,
    "Monitoring detects Defense Evasion techniques (log tampering, obfuscation)")
add("A.8.16", M, "TA0007", "MITRE_ATTACK_V18", "ISO27001_2022", "detects", 0.80,
    "Monitoring detects unusual Discovery/enumeration activity")
add("A.8.16", M, "TA0008", "MITRE_ATTACK_V18", "ISO27001_2022", "detects", 0.80,
    "Network monitoring detects Lateral Movement patterns")
add("A.8.16", M, "TA0011", "MITRE_ATTACK_V18", "ISO27001_2022", "detects", 0.85,
    "Network monitoring detects Command and Control communication")

# A.8.7 Protection against malware
add("A.8.7", M, "TA0002", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.90,
    "Anti-malware controls mitigate malicious Execution tactics")
add("A.8.7", M, "T1566", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.90,
    "Anti-malware scanning mitigates Phishing (T1566) payloads")
add("A.8.7", M, "T1059", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.80,
    "Script/execution controls limit Command and Scripting Interpreter abuse")
add("A.8.7", M, "T1486", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "Anti-malware mitigates Data Encrypted for Impact (ransomware)")

# A.8.20 Networks security
add("A.8.20", M, "TA0008", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "Network segmentation limits Lateral Movement")
add("A.8.20", M, "TA0011", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "Network controls block Command and Control channels")
add("A.8.20", M, "TA0010", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.80,
    "Network controls limit Exfiltration pathways")
add("A.8.20", M, "T1048", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.80,
    "Egress filtering mitigates Exfiltration Over Alternative Protocol")

# A.8.23 Web filtering
add("A.8.23", M, "TA0001", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.80,
    "Web filtering blocks malicious Initial Access vectors")
add("A.8.23", M, "T1566", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "Web filtering blocks Phishing URLs and malicious attachments")
add("A.8.23", M, "TA0011", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.80,
    "Web filtering blocks known C2 domains and infrastructure")

# A.8.12 Data leakage prevention
add("A.8.12", M, "TA0010", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.90,
    "DLP directly mitigates Exfiltration tactics")
add("A.8.12", M, "T1048", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "DLP mitigates Exfiltration Over Alternative Protocol (T1048)")
add("A.8.12", M, "T1041", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "DLP mitigates Exfiltration Over C2 Channel (T1041)")

# A.5.15 Access control
add("A.5.15", M, "TA0003", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "Access control limits attacker ability to establish Persistence")
add("A.5.15", M, "TA0004", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "Least-privilege access control mitigates Privilege Escalation")
add("A.5.15", M, "T1078", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "Access control and account hygiene mitigates Valid Accounts (T1078)")

# A.8.5 Secure authentication
add("A.8.5", M, "TA0006", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.90,
    "Strong authentication controls mitigate Credential Access tactics")
add("A.8.5", M, "T1110", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.90,
    "MFA and account lockout mitigates Brute Force (T1110)")
add("A.8.5", M, "T1558", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.75,
    "Strong Kerberos configuration mitigates Steal or Forge Kerberos Tickets")

# A.8.2 Privileged access rights
add("A.8.2", M, "TA0004", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.90,
    "Privileged access management directly mitigates Privilege Escalation")
add("A.8.2", M, "T1068", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.85,
    "PAM reduces impact of Exploitation for Privilege Escalation")

# A.8.13 Information backup
add("A.8.13", M, "TA0040", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.90,
    "Backups mitigate destructive Impact tactics (ransomware, wipers)")
add("A.8.13", M, "T1486", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.95,
    "Immutable backups are the primary mitigation for Data Encrypted for Impact")

# A.5.29 Business continuity during disruption
add("A.5.29", M, "TA0040", "MITRE_ATTACK_V18", "ISO27001_2022", "mitigates", 0.80,
    "BC planning mitigates operational Impact from destructive attacks")

# A.8.15 Logging
add("A.8.15", M, "TA0005", "MITRE_ATTACK_V18", "ISO27001_2022", "detects", 0.85,
    "Audit logging detects Defense Evasion attempts including log tampering")

print(f"  MITRE mappings prepared: {len(new_mappings)}")
mitre_count = len(new_mappings)

# ===========================================================================
# 2. ISO 27001 → OWASP ASVS 4.0 (chapter level)
#    Reference: OWASP ASVS 4.0 Appendix C — ISO 27001 mapping
# ===========================================================================
print("\n--- ISO 27001 → OWASP ASVS ---")
before = len(new_mappings)

O = owasp_ids

# V1 Architecture, Design and Threat Modeling
add("A.8.25", O, "V1", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.85,
    "Secure development lifecycle requirements align with ASVS Architecture chapter")
add("A.8.27", O, "V1", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.85,
    "Secure system architecture principles align with ASVS V1")

# V2 Authentication
add("A.5.16", O, "V2", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.90,
    "Identity management requirements align with ASVS Authentication chapter")
add("A.5.17", O, "V2", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.90,
    "Authentication information controls align with ASVS V2")
add("A.8.5", O, "V2", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.90,
    "Secure authentication controls align directly with ASVS V2")

# V3 Session Management
add("A.5.17", O, "V3", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.80,
    "Authentication information controls include session credential protection")
add("A.8.5", O, "V3", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.80,
    "Secure authentication includes session management")

# V4 Access Control
add("A.5.15", O, "V4", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.95,
    "Access control policy directly aligns with ASVS V4 Access Control")
add("A.8.2", O, "V4", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.85,
    "Privileged access rights management aligns with ASVS V4")

# V5 Validation, Sanitization and Encoding
add("A.8.25", O, "V5", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.80,
    "Secure SDLC requires input validation per ASVS V5")
add("A.8.27", O, "V5", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.80,
    "Secure architecture principles include input validation requirements")

# V6 Stored Cryptography
add("A.8.24", O, "V6", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.95,
    "Use of cryptography directly aligns with ASVS V6 Stored Cryptography")

# V7 Error Handling and Logging
add("A.8.15", O, "V7", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.90,
    "Logging controls align directly with ASVS V7 Error Handling and Logging")
add("A.8.16", O, "V7", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.80,
    "Monitoring activities require comprehensive logging per ASVS V7")

# V8 Data Protection
add("A.8.12", O, "V8", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.90,
    "Data leakage prevention aligns with ASVS V8 Data Protection")
add("A.5.12", O, "V8", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.80,
    "Classification of information aligns with ASVS V8 data sensitivity handling")

# V9 Communication Security
add("A.8.20", O, "V9", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.85,
    "Network security controls align with ASVS V9 Communication requirements")
add("A.8.24", O, "V9", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.85,
    "Cryptography controls include TLS/transport security per ASVS V9")

# V10 Malicious Code
add("A.8.7", O, "V10", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.90,
    "Protection against malware aligns with ASVS V10 Malicious Code chapter")

# V13 API and Web Service
add("A.8.27", O, "V13", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.80,
    "Secure architecture includes secure API design per ASVS V13")
add("A.8.20", O, "V13", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.75,
    "Network security includes API security controls per ASVS V13")

# V14 Configuration
add("A.8.9", O, "V14", "OWASP_ASVS_4.0", "ISO27001_2022", "maps-to", 0.95,
    "Configuration management directly aligns with ASVS V14 Configuration")

asvs_count = len(new_mappings) - mitre_count
print(f"  OWASP ASVS mappings prepared: {asvs_count}")

# ===========================================================================
# 3. ISO 27001 → FINMA
#    Reference: FINMA Circular 2023/1, 2018/3, Guidance 03/2024
#               Published at finma.ch; mapped against ISO 27001:2022 Annex A
# ===========================================================================
print("\n--- ISO 27001 → FINMA ---")
before_finma = len(new_mappings)

F = finma_ids

# FINMA 2023/1 — P1 Operational Risk Management
for iso in ["A.5.29", "A.5.30", "A.8.16", "A.8.15"]:
    add(iso, F, "P1", "FINMA", "ISO27001_2022", "maps-to", 0.80,
        f"{iso} supports FINMA 2023/1 P1 Operational Risk Management requirements")

# FINMA 2023/1 — P2 ICT Risk Management
for iso in ["A.8.8", "A.8.9", "A.8.20", "A.8.16", "A.5.15", "A.8.5"]:
    add(iso, F, "P2", "FINMA", "ISO27001_2022", "maps-to", 0.85,
        f"{iso} satisfies FINMA 2023/1 P2 ICT Risk Management requirements")

# FINMA 2023/1 — P3 Cyber Risk Management
for iso in ["A.8.7", "A.8.8", "A.8.16", "A.8.23", "A.5.7", "A.8.12"]:
    add(iso, F, "P3", "FINMA", "ISO27001_2022", "maps-to", 0.90,
        f"{iso} satisfies FINMA 2023/1 P3 Cyber Risk Management requirements")

# FINMA 2023/1 — P4 Critical Data Risk Management
for iso in ["A.5.9", "A.5.10", "A.5.12", "A.8.12", "A.8.24"]:
    add(iso, F, "P4", "FINMA", "ISO27001_2022", "maps-to", 0.85,
        f"{iso} satisfies FINMA 2023/1 P4 Critical Data Risk Management requirements")

# FINMA 2023/1 — P5 Business Continuity Management
for iso in ["A.5.29", "A.5.30", "A.8.13", "A.8.14"]:
    add(iso, F, "P5", "FINMA", "ISO27001_2022", "maps-to", 0.90,
        f"{iso} satisfies FINMA 2023/1 P5 Business Continuity requirements")

# FINMA 2023/1 — P7 Operational Resilience
for iso in ["A.5.29", "A.5.30", "A.8.13", "A.8.14", "A.8.16"]:
    add(iso, F, "P7", "FINMA", "ISO27001_2022", "maps-to", 0.85,
        f"{iso} contributes to FINMA 2023/1 P7 Operational Resilience")

# FINMA 2018/3 — Outsourcing (DEF, V.A-V.H)
for iso in ["A.5.19", "A.5.20", "A.5.21"]:
    add(iso, F, "DEF", "FINMA", "ISO27001_2022", "maps-to", 0.80,
        f"{iso} aligns with FINMA 2018/3 outsourcing definition scope")
    add(iso, F, "V.A", "FINMA", "ISO27001_2022", "maps-to", 0.85,
        f"{iso} aligns with FINMA 2018/3 V.A inventory of outsourced functions")
    add(iso, F, "V.B", "FINMA", "ISO27001_2022", "maps-to", 0.85,
        f"{iso} aligns with FINMA 2018/3 V.B selection and monitoring requirements")
    add(iso, F, "V.D", "FINMA", "ISO27001_2022", "maps-to", 0.80,
        f"{iso} aligns with FINMA 2018/3 V.D responsibility requirements")
    add(iso, F, "V.H", "FINMA", "ISO27001_2022", "maps-to", 0.80,
        f"{iso} aligns with FINMA 2018/3 V.H agreement requirements")

add("A.8.20", F, "V.E", "FINMA", "ISO27001_2022", "maps-to", 0.85,
    "Network security requirements align with FINMA 2018/3 V.E Security")
add("A.8.5", F, "V.E", "FINMA", "ISO27001_2022", "maps-to", 0.80,
    "Secure authentication requirements align with FINMA 2018/3 V.E Security")

# FINMA Guidance 03/2024 — Cyber Risks
# G1 Governance
for iso in ["A.5.7", "A.8.16"]:
    add(iso, F, "G1", "FINMA", "ISO27001_2022", "maps-to", 0.85,
        f"{iso} supports FINMA Guidance 03/2024 G1 Cyber Governance requirements")

# G2 Protective measures
for iso in ["A.8.7", "A.8.8", "A.8.9", "A.8.20", "A.8.23", "A.8.5", "A.5.15"]:
    add(iso, F, "G2", "FINMA", "ISO27001_2022", "maps-to", 0.85,
        f"{iso} satisfies FINMA Guidance 03/2024 G2 Protective Measures")

# G3 Detection, response, and recovery
for iso in ["A.8.16", "A.8.15", "A.5.29", "A.8.13"]:
    add(iso, F, "G3", "FINMA", "ISO27001_2022", "maps-to", 0.90,
        f"{iso} satisfies FINMA Guidance 03/2024 G3 Detection, Response and Recovery")

finma_count = len(new_mappings) - mitre_count - asvs_count
print(f"  FINMA mappings prepared: {finma_count}")

# ===========================================================================
# Summary + write
# ===========================================================================
print(f"\nTotal new mappings: {len(new_mappings)}  (skipped {skipped} duplicates)")

if not new_mappings:
    print("Nothing to add.")
    exit(0)

# Update bundle
crosswalk["objects"].extend(new_mappings)
crosswalk["objects_count"] = len(crosswalk["objects"])

# Update mapping_axes counts
axes = {}
for o in crosswalk["objects"]:
    k = f"{o['source_framework']} → {o['target_framework']}"
    axes[k] = axes.get(k, 0) + 1
crosswalk["mapping_axes"] = axes

output = DATA / "crosswalk.json"
with open(output, "w") as f:
    json.dump(crosswalk, f, indent=2)

print(f"\nSaved → {output}")
print("\nUpdated mapping_axes:")
for k, v in sorted(axes.items()):
    print(f"  {k}: {v}")

print("\nNext step: re-import the crosswalk into the DB:")
print("  POST /api/v1/sync/crosswalk  (or use the Admin → re-import button)")
