#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-CHK-A.11 — Information Security Compliance Checklist

Controls A.11.1-A.11.13: Confidentiality, Hardcopy Restriction,
  Backup Restoration Logging, Physical Media, Portable Storage, Encryption,
  Secure Disposal, Unique IDs, ID Management, Authorised User Records,
  Contract Measures, Sub-processor Obligations, Storage Remanence
Product: ISMS CORE Cloud (ISO/IEC 27018:2025 — Annex A)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Personnel, Physical and Media Controls (A.11.1-7) — 7 reqs
4. Access Management and Encryption (A.11.6, A.11.8-10) — 6 reqs
5. Contracts, Sub-processors and Storage (A.11.11-13) — 6 reqs

Total: 19 requirements across 3 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 51-isms-core-privacy/00-checklist-engine/priv_checklist_engine.py
_REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_REPO_ROOT / '51-isms-core-privacy' / '00-checklist-engine'))
from priv_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "CLD-CHK-A.11"
CONTROL_ID = "A.11.1-13"
CONTROL_NAME = "Information Security"
SOURCE_POLICY = "CLD-POL-A.11"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-POL-A.11
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Personnel, Physical and Media Controls", [
        ("A.11.1-01", "Confidentiality Obligations (A.11.1)",
         "All personnel and contractors with access to systems containing PII shall be bound by written confidentiality and non-disclosure obligations that explicitly prohibit secondary use, personal retention, or unauthorised disclosure of PII; survive termination of employment or engagement; and are signed before access to any PII system is granted. NDA coverage shall be verified during onboarding and departure processes."),
        ("A.11.2-01", "Hardcopy Restriction (A.11.2)",
         "Creation of hardcopy (printed) material containing PII is restricted and requires documented business justification and team lead authorisation. Printed PII shall be collected immediately from the printer, not left unattended in shared areas, and handled under clear-desk procedures. Printed PII shall be disposed of per the secure hardcopy disposal standard."),
        ("A.11.3-01", "Backup Restoration Logging (A.11.3)",
         "Restoration of PII from backup or archive is a controlled operation requiring: documented authorisation from the team lead or incident commander; logging of the operator identity, timestamp, backup source, scope of data restored, and authorisation reference; restoration logs protected against tampering (write-once or cryptographically signed); and quarterly review of restoration logs by CISO. Unplanned restoration attempts shall be treated as security events."),
        ("A.11.4-01", "Storage Media Leaving Premises (A.11.4)",
         "Physical storage media containing PII that leaves cloud facilities shall be encrypted using approved full-disk or volume encryption, or physically destroyed to a standard preventing data recovery before departure. Media movement shall be authorised by the CISO or Cloud Security Manager, logged in a media movement register with chain of custody documentation, and tracked to final destination."),
        ("A.11.5-01", "Unencrypted Portable Storage Prohibition (A.11.5)",
         "The use of unencrypted portable storage media and devices for storage or transfer of PII is prohibited. Where portable devices are authorised for PII, full-disk encryption (AES-256 minimum) is mandatory, device encryption status shall be verified before PII access is permitted, and remote wipe capability shall be enabled for mobile devices. Loss or theft of any portable device potentially containing PII shall be reported to the CISO and DPO immediately and treated as a PII security incident."),
        ("A.11.7-01", "Secure Disposal of Hardcopy (A.11.7)",
         "Hardcopy materials containing PII shall be disposed of securely: individual disposal by cross-cut shredding to DIN 66399 Level P-4 or equivalent; bulk disposal via certified destruction services providing a certificate of destruction; and locked, access-controlled disposal bins for PII material in all work areas. Certificates of destruction shall be retained for 3 years."),
        ("A.11.6-01", "Encryption in Transit (A.11.6)",
         "PII transmitted over public networks shall be encrypted using TLS 1.2 minimum (TLS 1.3 preferred for new implementations). HTTPS shall be enforced on all web interfaces and API endpoints handling PII. Unencrypted transmission (plain HTTP, FTP, SMTP without STARTTLS) of PII is prohibited. Cipher suite configurations shall be reviewed annually against current best practice; weak ciphers (RC4, DES, 3DES, SSL 3.0, TLS 1.0, TLS 1.1) shall be disabled."),
    ]),

    ("Access Management and Encryption", [
        ("A.11.8-01", "Unique User IDs (A.11.8)",
         "Each individual with access to PII systems shall be assigned a unique user identifier. Shared, generic, or role-based accounts shall not be used to access systems where PII is processed or stored. Exceptions such as service accounts require CISO approval and enhanced compensating controls including privileged access management and session recording."),
        ("A.11.9-01", "User ID Lifecycle (A.11.9)",
         "User identifiers for PII systems shall be managed through a documented lifecycle: provisioning requires documented authorisation; access reviewed at least quarterly; role changes updated within 1 business day; terminations deactivated within 4 hours of HR-confirmed departure; and dormant accounts (inactive 90 days) reviewed and suspended pending review, then deleted if no business justification confirmed."),
        ("A.11.9-02", "Dormant Account Management",
         "The organisation shall identify and review all PII system accounts inactive for 90 or more days as part of the quarterly access review. Dormant accounts shall be suspended pending business justification review; if no justification is confirmed within 5 business days, the account shall be permanently deactivated. Dormant account review records shall be maintained."),
        ("A.11.10-01", "Authorised User Register (A.11.10)",
         "The organisation shall maintain an Authorised User Register for each PII system recording: individual identity and role; scope of access granted (read, write, admin); authorisation date and authorising manager; and last review date. The register shall be reviewed and attested by system owners at least quarterly, updated within 1 business day of any access change, and made available to any PII controller upon request (restricted to access over their PII)."),
        ("A.11.10-02", "Quarterly Attestation",
         "System owners shall formally attest the Authorised User Register for each PII system at least quarterly, confirming that all listed access entitlements remain current, necessary, and authorised. Attestation records shall be retained for 3 years. Unconfirmed access entitlements (non-response after documented follow-up) shall be suspended."),
        ("A.11.10-03", "Access Change Records",
         "All access changes to PII systems (grants, modifications, revocations) shall be documented with the change date, individual affected, access scope before and after, authorising party, and business reason. Access change records shall be retained for 3 years."),
    ]),

    ("Contracts, Sub-processors and Storage", [
        ("A.11.11-01", "Contract Measures (A.11.11)",
         "Service agreements between the organisation and PII controllers shall include provisions addressing: scope and documented purpose of PII processing; security obligations aligned with GDPR Article 32; breach notification (controller notification within 24 hours per CLD-POL-A.10.1); data subject rights assistance obligations; audit rights for the controller or appointed auditor; sub-processor approval requirements; PII return or deletion upon termination; and applicable law and jurisdiction."),
        ("A.11.11-02", "Agreement Template Review",
         "The standard processor agreement template shall be reviewed by Legal/Compliance when regulatory requirements change materially and at minimum annually. All active controller agreements shall be assessed against the current template and updated where material gaps exist. The Processor Agreement Register shall record review status for each agreement."),
        ("A.11.12-01", "Sub-processor Equivalent Obligations (A.11.12)",
         "The organisation shall impose on all sub-processors via binding contract obligations equivalent to those in CLD-POL-A.11 and the full CLD-POL-A.X suite. Sub-processor contracts shall: mirror data protection obligations from the controller-processor agreement; require prior written consent before any further sub-processing; include audit rights for the organisation; require breach notification to the organisation within 12 hours of detection; and require PII return or disposal upon sub-processor engagement termination."),
        ("A.11.12-02", "Sub-processor Audit Programme",
         "The organisation shall audit sub-processors at least annually (via questionnaire, document review, or on-site audit) and remains fully accountable to PII controllers for sub-processor compliance failures. Sub-processor audit results shall be documented and available to controllers upon request. Sub-processor audit records shall be retained for 5 years."),
        ("A.11.13-01", "Pre-used Storage Space Erasure (A.11.13)",
         "The organisation shall ensure that PII cannot be accessed from storage previously allocated to another customer. Before any storage is reallocated to a new customer workload, all prior data shall be cryptographically erased (encryption key deletion for encrypted volumes) or overwritten to a standard preventing recovery. The erasure shall be documented and the decommissioning record retained."),
        ("A.11.13-02", "Decommissioning Procedures and Testing",
         "Decommissioning procedures shall cover all storage types (block, object, ephemeral instance, database) and all compute layers, and all geographic regions of cloud infrastructure. Procedures shall be tested at least annually by randomly sampling reallocated storage and confirming no residual data. Annual test results shall be documented and retained for 3 years. Any failure shall be treated as a potential PII security incident."),
    ]),
])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 27018:2025"
    ))


# =============================================================================
# QA_VERIFIED: 2026-03-10
# QA_STATUS: PASSED
# QA_TOOL: Claude Code Production Scripts QA Methodology
# CHANGES: Initial generation for Cloud product launch
# =============================================================================
