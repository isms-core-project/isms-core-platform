#!/usr/bin/env python3
"""
Generate BSI IT-Grundschutz Kompendium framework bundle.

Pipeline: this script → data/bsi_it_grundschutz.json
Then run generate_crosswalk.py to rebuild data/crosswalk.json.

BSI IT-Grundschutz Kompendium is the modular control catalog of building blocks
(Bausteine) organized in 10 layers. BSI publishes an official Zuordnungstabelle
linking these to ISO 27001:2022 — the basis for dual certification.

Note: BSI 200-3 G-codes (G 0.x) are threats/risks, NOT controls.
They belong in the risk calculator, not here.
"""

import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_DIR = SCRIPT_DIR.parent / "data"
OUTPUT_FILE = DATA_DIR / "bsi_it_grundschutz.json"

ISMS_NAMESPACE = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")


def stable_uuid(key: str) -> str:
    return str(uuid.uuid5(ISMS_NAMESPACE, key))


def control_uuid(baustein_id: str) -> str:
    return stable_uuid(f"control:BSI_IT_GRUNDSCHUTZ:{baustein_id}")


FRAMEWORK_ID = stable_uuid("framework:BSI_IT_GRUNDSCHUTZ")

FRAMEWORK = {
    "id": FRAMEWORK_ID,
    "code": "BSI_IT_GRUNDSCHUTZ",
    "name": "BSI IT-Grundschutz Kompendium",
    "version": "2023",
    "publisher": "Bundesamt fuer Sicherheit in der Informationstechnik (BSI)",
    "source_url": "https://www.bsi.bund.de/grundschutz",
    "jurisdiction": "DE",
    "description": (
        "BSI IT-Grundschutz Kompendium — modular security building blocks (Bausteine) "
        "for information security management. Basis for IT-Grundschutz certification "
        "recognised as equivalent to ISO 27001 by BSI. Organised in 10 layers."
    ),
}

# ---------------------------------------------------------------------------
# Layer definitions: (layer_code, layer_title, layer_description, sort_order)
# ---------------------------------------------------------------------------

LAYERS = [
    ("ISMS", "Security Management",
     "Information security management system requirements, strategy, and governance.",
     1000),
    ("ORP", "Organisation and Personnel",
     "Organisational structures, roles, responsibilities, and personnel security.",
     2000),
    ("CON", "Concepts and Approaches",
     "Security concepts including cryptography, data backup, and software development.",
     3000),
    ("OPS", "Operation",
     "Operational security: IT administration, patch management, malware protection, logging.",
     4000),
    ("DER", "Detection and Reaction",
     "Detection of security incidents and reactive measures including forensics and BCM.",
     5000),
    ("INF", "Infrastructure",
     "Physical and environmental security: buildings, data centres, cabling.",
     6000),
    ("NET", "Networks",
     "Network architecture, management, wireless, firewall, and VPN.",
     7000),
    ("SYS", "IT Systems",
     "Secure operation of servers, clients, mobile devices, and storage media.",
     8000),
    ("APP", "Applications",
     "Security requirements for applications, web services, and software.",
     9000),
    ("IND", "Industrial IT",
     "Security for industrial control systems (ICS) and process environments.",
     10000),
]

# ---------------------------------------------------------------------------
# Bausteine: (baustein_id, title, description, layer_code, sort_order)
# ---------------------------------------------------------------------------

BAUSTEINE = [
    # ISMS layer
    ("ISMS.1", "Security Management",
     "Establishment and operation of an information security management system. "
     "Covers ISMS scope, security policy, roles, management review, and continual improvement.",
     "ISMS", 1010),
    ("ISMS.2", "Information Security Strategy",
     "Development and maintenance of an information security strategy aligned to "
     "organisational objectives and risk appetite.",
     "ISMS", 1020),

    # ORP layer
    ("ORP.1", "Organisation",
     "Organisational framework for information security: roles, responsibilities, "
     "authority, and coordination with internal and external stakeholders.",
     "ORP", 2010),
    ("ORP.2", "Personnel",
     "Personnel security covering pre-employment screening, employment terms, "
     "disciplinary processes, and termination of employment.",
     "ORP", 2020),
    ("ORP.3", "Sensitisation and Training",
     "Awareness, education, and training programmes to build information security "
     "competence across the organisation.",
     "ORP", 2030),
    ("ORP.4", "Identity and Permission Management",
     "Management of user identities, access rights, and privilege administration "
     "including provisioning and deprovisioning.",
     "ORP", 2040),

    # CON layer
    ("CON.1", "Cryptography",
     "Policy and technical controls for cryptographic mechanisms: key management, "
     "algorithm selection, certificate lifecycle.",
     "CON", 3010),
    ("CON.2", "Data Backup Concept",
     "Conceptual requirements for data backup: objectives, responsibilities, "
     "backup classes, and recovery targets.",
     "CON", 3020),
    ("CON.3", "Data Backup Policy",
     "Operational data backup policy: schedules, media, retention periods, "
     "off-site storage, and restore testing.",
     "CON", 3030),
    ("CON.6", "Delete and Destroy",
     "Secure deletion and physical destruction of data carriers and information "
     "to prevent unauthorised recovery.",
     "CON", 3060),
    ("CON.8", "Software Development",
     "Security requirements for in-house and commissioned software development "
     "across the full SDLC.",
     "CON", 3080),
    ("CON.10", "Development of Web Applications",
     "Specific security requirements for the development and operation of "
     "web applications and web services.",
     "CON", 3100),
    ("CON.11.1", "Quantum Cryptography",
     "Post-quantum cryptographic algorithms and migration planning to ensure "
     "long-term confidentiality.",
     "CON", 3110),

    # OPS layer
    ("OPS.1.1.1", "General IT Operations",
     "Baseline operational procedures: change management, operational documentation, "
     "monitoring, and standard operating processes.",
     "OPS", 4010),
    ("OPS.1.1.2", "IT Administration",
     "Privileged account management, administrative access controls, separation of "
     "administrative and user functions.",
     "OPS", 4020),
    ("OPS.1.1.3", "Patch and Change Management",
     "Systematic identification, evaluation, testing, and deployment of patches "
     "and software updates across all systems.",
     "OPS", 4030),
    ("OPS.1.1.4", "Protection against Malware",
     "Anti-malware controls including detection software, scanning policies, "
     "update mechanisms, and incident response for malware.",
     "OPS", 4040),
    ("OPS.1.1.5", "Logging",
     "Security and system logging: log generation, protection, retention, "
     "and review to support incident detection and forensics.",
     "OPS", 4050),
    ("OPS.1.1.6", "Software Tests and Approvals",
     "Testing and formal approval of software before production deployment "
     "including security and functional acceptance criteria.",
     "OPS", 4060),
    ("OPS.1.2.2", "Archiving",
     "Long-term preservation of records and information: archiving procedures, "
     "media management, integrity checks, and access controls.",
     "OPS", 4070),
    ("OPS.1.2.5", "Remote Maintenance",
     "Controls for remote access used in system maintenance: authentication, "
     "encryption, session monitoring, and approval processes.",
     "OPS", 4080),
    ("OPS.2.2", "Cloud Usage",
     "Governance and security requirements when using cloud services: provider "
     "assessment, contractual requirements, and data protection.",
     "OPS", 4090),
    ("OPS.2.3", "Outsourcing to Third Parties",
     "Security requirements for outsourced services: risk assessment, contractual "
     "obligations, monitoring, and exit planning.",
     "OPS", 4100),
    ("OPS.3.2", "Outsourcing Provider",
     "Security obligations for organisations acting as outsourcing providers: "
     "service delivery, client data protection, and audit rights.",
     "OPS", 4110),

    # DER layer
    ("DER.1", "Detecting Security Events",
     "Detection controls for security events: monitoring, alerting, intrusion "
     "detection, and log analysis capabilities.",
     "DER", 5010),
    ("DER.2.1", "Incident Handling",
     "Security incident management process: detection, reporting, classification, "
     "response, containment, and post-incident review.",
     "DER", 5020),
    ("DER.2.2", "IT Forensics",
     "Forensic investigation procedures: evidence preservation, chain of custody, "
     "forensic analysis, and reporting.",
     "DER", 5030),
    ("DER.2.3", "Cleanup after Incidents",
     "Recovery and cleanup procedures following security incidents: system "
     "restoration, verification, and lessons learned.",
     "DER", 5040),
    ("DER.3.1", "Audits and Revision",
     "Internal and external audit planning, execution, reporting, and follow-up "
     "to verify security control effectiveness.",
     "DER", 5050),
    ("DER.4", "Emergency Management (BCM)",
     "Business continuity management: BIA, BCP, emergency plans, crisis communication, "
     "testing, and exercises.",
     "DER", 5060),

    # INF layer
    ("INF.1", "General Building",
     "Physical security of buildings: perimeter, access controls, visitor management, "
     "security zones, and environmental protection.",
     "INF", 6010),
    ("INF.2", "Data Centre and Server Room",
     "Physical and environmental controls for data centres and server rooms: "
     "access, power, cooling, fire suppression, and monitoring.",
     "INF", 6020),
    ("INF.5", "Room and Cabinet Protection",
     "Security measures for technical rooms and equipment cabinets: locking, "
     "access logging, environmental monitoring.",
     "INF", 6050),
    ("INF.6", "Storage Media Archives",
     "Secure storage of data carriers and archives: physical protection, "
     "climate control, access restrictions, and inventory management.",
     "INF", 6060),
    ("INF.7", "Office Environments",
     "Security measures for office spaces including clean desk policy, "
     "remote working, and visitor access.",
     "INF", 6070),

    # NET layer
    ("NET.1.1", "Network Architecture and Design",
     "Secure network architecture principles: segmentation, DMZ design, "
     "routing, and network documentation.",
     "NET", 7010),
    ("NET.1.2", "Network Management",
     "Network management security: privileged access, configuration management, "
     "monitoring, and change control for network components.",
     "NET", 7020),
    ("NET.2.2", "WLAN Usage",
     "Security requirements for wireless LAN usage: authentication, encryption, "
     "rogue AP detection, and guest network segregation.",
     "NET", 7030),
    ("NET.3.2", "Firewall",
     "Firewall policy, rule management, zone separation, logging, and regular "
     "rule-set review for perimeter and internal firewalls.",
     "NET", 7040),
    ("NET.3.3", "VPN",
     "VPN security: authentication, encryption standards, client configuration, "
     "split tunnelling policy, and monitoring.",
     "NET", 7050),

    # SYS layer
    ("SYS.1.1", "General Server",
     "Baseline hardening and secure operation of servers: OS hardening, "
     "service minimisation, patch management, and monitoring.",
     "SYS", 8010),
    ("SYS.1.3", "Linux and Unix Server",
     "Linux/Unix-specific hardening: user and group management, PAM, "
     "mandatory access controls, and secure boot.",
     "SYS", 8020),
    ("SYS.1.6", "Containerisation",
     "Security requirements for container deployments: image management, "
     "runtime isolation, network policies, and secrets management.",
     "SYS", 8030),
    ("SYS.2.1", "General Clients",
     "Secure configuration and operation of client systems: OS hardening, "
     "application whitelisting, endpoint protection.",
     "SYS", 8040),
    ("SYS.3.2.1", "Smartphones and Tablets",
     "Mobile device management: MDM/UEM, remote wipe, application controls, "
     "encryption, and BYOD policy.",
     "SYS", 8050),
    ("SYS.4.1", "Printers and Multifunction Devices",
     "Security for printers and MFDs: network isolation, access controls, "
     "secure print release, and data remanence.",
     "SYS", 8060),
    ("SYS.4.5", "Removable Storage Media",
     "Controls for removable storage media: authorised media list, encryption "
     "requirements, scanning, and disposal.",
     "SYS", 8070),

    # APP layer
    ("APP.1.1", "Office Products",
     "Security configuration of office productivity suites: macro controls, "
     "auto-update, protected view, and document security.",
     "APP", 9010),
    ("APP.2.1", "General Directory Services",
     "Security requirements for directory services (LDAP/AD): authentication, "
     "replication, privileged group management, and auditing.",
     "APP", 9020),
    ("APP.3.1", "Web Applications and Services",
     "Security controls for web applications and APIs: authentication, "
     "authorisation, input validation, and session management.",
     "APP", 9030),
    ("APP.3.2", "Web Server",
     "Secure configuration and hardening of web servers: TLS, HTTP security "
     "headers, directory listings, and access logging.",
     "APP", 9040),
    ("APP.3.3", "File Server",
     "Security for file servers: access controls, quotas, antivirus, "
     "auditing, and backup integration.",
     "APP", 9050),
    ("APP.5.3", "General Email Clients and Server",
     "Email security: anti-spam, anti-phishing, S/MIME or PGP, DKIM/DMARC/SPF, "
     "and secure client configuration.",
     "APP", 9060),
    ("APP.6", "General Software",
     "Lifecycle security for commercial and open-source software: procurement, "
     "testing, deployment, and end-of-life management.",
     "APP", 9070),
    ("APP.7", "Development and Ops (DevOps)",
     "Security integration in DevOps pipelines: SAST/DAST, dependency scanning, "
     "secrets management, and secure CI/CD.",
     "APP", 9080),

    # IND layer
    ("IND.1", "Process Control Systems",
     "Security governance for industrial control systems: ICS security policy, "
     "risk management, and zone model.",
     "IND", 10010),
    ("IND.2.1", "General ICS Components",
     "Baseline security for ICS components: hardening, patch management, "
     "remote access controls, and network separation.",
     "IND", 10020),
    ("IND.3.2", "Remote Access for ICS",
     "Secure remote access to industrial systems: authentication, encrypted "
     "tunnels, session monitoring, and vendor access controls.",
     "IND", 10030),
]


def build_objects() -> list[dict]:
    objects = []

    # Build a quick lookup: layer_code → layer object ID
    layer_ids: dict[str, str] = {}
    for layer_code, layer_title, layer_desc, sort_order in LAYERS:
        layer_id = stable_uuid(f"layer:BSI_IT_GRUNDSCHUTZ:{layer_code}")
        layer_ids[layer_code] = layer_id
        objects.append({
            "type": "framework_control",
            "id": layer_id,
            "framework_id": FRAMEWORK_ID,
            "control_id": layer_code,
            "title": layer_title,
            "level": 0,
            "sort_order": sort_order,
            "description": layer_desc,
        })

    # Bausteine
    for baustein_id, title, description, layer_code, sort_order in BAUSTEINE:
        objects.append({
            "type": "framework_control",
            "id": control_uuid(baustein_id),
            "framework_id": FRAMEWORK_ID,
            "parent_id": layer_ids[layer_code],
            "control_id": baustein_id,
            "title": title,
            "level": 1,
            "sort_order": sort_order,
            "description": description,
        })

    return objects


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    objects = build_objects()

    content_str = json.dumps(objects, sort_keys=True)
    content_hash = hashlib.sha256(content_str.encode()).hexdigest()

    bundle_key = stable_uuid(f"bundle:BSI_IT_GRUNDSCHUTZ:{content_hash[:16]}")
    bundle = {
        "bundle_id": f"bundle--{bundle_key}",
        "bundle_type": "isms-core-dataset",
        "bundle_version": "1.0",
        "framework": FRAMEWORK,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "generator": "generate_bsi_grundschutz.py",
        "content_hash": content_hash,
        "objects_count": len(objects),
        "objects": objects,
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)

    layers = sum(1 for o in objects if o["level"] == 0)
    bausteine = sum(1 for o in objects if o["level"] == 1)
    print(f"Generated {OUTPUT_FILE.name}:")
    print(f"  Layers:    {layers}")
    print(f"  Bausteine: {bausteine}")
    print(f"  Total objects: {len(objects)}")
    print(f"  Content hash:  {content_hash[:16]}...")


if __name__ == "__main__":
    main()
