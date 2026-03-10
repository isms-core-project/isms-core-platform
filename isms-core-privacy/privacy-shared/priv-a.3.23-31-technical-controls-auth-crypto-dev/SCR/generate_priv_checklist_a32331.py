#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.3.23-31 — Technical Security Controls for PII Compliance Checklist

Controls A.3.23-31: Secure Authentication, Backup, Logging, Cryptography,
                    Secure Development Lifecycle, Application Security Requirements,
                    Secure Architecture Principles, Outsourced Development,
                    Test Information
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Shared Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Authentication, Backup and Logging (A.3.23-25) — 9 reqs
4. Cryptography and Secure Development (A.3.26-29) — 9 reqs
5. Outsourced Development and Test Information (A.3.30-31) — 6 reqs

Total: 24 requirements across 3 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 51-isms-core-privacy/00-checklist-engine/priv_checklist_engine.py
_PRIV_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(_PRIV_ROOT / '00-checklist-engine'))
from priv_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "PRIV-CHK-A.3.23-31"
CONTROL_ID = "A.3.23-31"
CONTROL_NAME = "Technical Security Controls for PII"
SOURCE_POLICY = "PRIV-POL-A.3.23-31"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.3.23-31
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Authentication, Backup and Logging", [
        ("A.3.23-01", "Authentication Standards for PII Systems",
         "Secure authentication shall be implemented for access to PII processing systems based on access restrictions. Minimum requirements by PII sensitivity: CONFIDENTIAL PII — MFA for remote access, strong password policy for internal access; RESTRICTED PII — MFA required for all access (internal and remote); administrative and privileged access to PII — MFA required with separate privileged credentials."),
        ("A.3.23-02", "Authentication Procedure Requirements",
         "Authentication procedures for PII systems shall enforce access restrictions aligned to the access rights defined in PRIV-POL-A.3.8-10. Failed authentication attempts to PII systems shall be logged and trigger account lockout per defined thresholds. Authentication credentials for PII systems shall be unique per individual — shared credentials for PII system access are prohibited."),
        ("A.3.24-01", "PII Backup Requirements",
         "All PII processed by the organisation shall be covered by a backup regime with documented recovery point objectives aligned to PII processing criticality and regulatory requirements. Backups containing PII shall be subject to the same classification and access controls as primary PII (CONFIDENTIAL or RESTRICTED as applicable) and shall be encrypted with the same standard as the primary data."),
        ("A.3.24-02", "Backup Testing",
         "Backup restoration shall be tested at minimum annually to confirm that PII is recoverable and complete. Test restoration outcomes shall be documented, including data integrity verification. Restoration test failures involving PII shall be treated as a risk event and escalated to the CISO and DPO."),
        ("A.3.25-01", "PII Logging Requirements",
         "The following events relating to PII processing shall be logged: access to PII data stores (read, write, export) by authenticated users; failed access attempts to PII systems; bulk data operations involving PII; changes to access rights for PII systems; privileged operations on PII processing systems; data subject rights fulfilment operations; and system errors or exceptions in PII processing components."),
        ("A.3.25-02", "Log Protection",
         "Logs containing PII processing activity shall be: protected against modification and deletion (tamper-evident storage); classified at minimum CONFIDENTIAL; accessible only to authorised personnel (IT Security Team, CISO, DPO for privacy investigation purposes); and retained for minimum 12 months or longer where required by applicable regulation or contract."),
        ("A.3.25-03", "Log Analysis",
         "Logs shall be reviewed on an exception basis (alerts for anomalous PII access patterns), as part of periodic compliance review per PRIV-POL-A.3.13-16, in response to a privacy incident per PRIV-POL-A.3.11-12, and as part of access rights review per PRIV-POL-A.3.8-10. Log analysis standards and tools are defined in PRIV-IMP-A.3.23-31-TG."),
        ("A.3.25-04", "Offsite and Cloud Backup Security",
         "Offsite or cloud backup copies containing PII shall be subject to equivalent security controls to primary storage, including access restrictions and encryption in transit and at rest. Cloud backup providers shall be subject to the supplier controls in PRIV-POL-A.3.8-10 and, where they process PII, shall be categorised as PII Processor suppliers with a compliant processor agreement."),
        ("A.3.23-03", "Credential Management",
         "Privileged access credentials for PII processing systems shall be managed separately from standard user credentials. Privileged credentials shall be rotated at intervals defined in PRIV-IMP-A.3.23-31-TG. Dormant privileged accounts shall be identified and disabled in access reviews per PRIV-POL-A.3.8-10."),
    ]),

    ("Cryptography and Secure Development", [
        ("A.3.26-01", "Encryption at Rest",
         "All CONFIDENTIAL and RESTRICTED PII stored in databases, files, or on media shall be encrypted at rest using an approved algorithm (minimum AES-256 or equivalent per ISMS-POL-A.8.24). Encryption at rest is a baseline requirement — its absence for CONFIDENTIAL or RESTRICTED PII requires DPO-approved risk acceptance."),
        ("A.3.26-02", "Encryption in Transit",
         "All PII transmitted across networks shall be encrypted in transit using current TLS standards (minimum TLS 1.2; TLS 1.3 preferred). Unencrypted transmission of CONFIDENTIAL or RESTRICTED PII over public networks is prohibited. Internal network transmission of RESTRICTED PII shall also be encrypted."),
        ("A.3.26-03", "Pseudonymisation and Anonymisation",
         "Where PII is used for analytics, testing, research, or secondary purposes, pseudonymisation shall be applied to reduce re-identification risk where technically feasible. Anonymisation (where re-identification is not reasonably possible) removes data from the scope of PII — anonymisation decisions require DPO confirmation before reclassification."),
        ("A.3.26-04", "Key Management",
         "Cryptographic keys protecting PII shall be managed separately from the PII they protect. Key access shall be restricted to authorised personnel with documented operational need. Key rotation shall occur at defined intervals. Key compromise or loss involving PII-protecting keys shall be treated as a PII security incident per PRIV-POL-A.3.11-12."),
        ("A.3.27-01", "Privacy by Design and by Default",
         "Privacy and PII protection requirements shall be considered from the earliest design stage of any system intended to process PII (Privacy by Design). System defaults shall minimise PII collection and processing — the most privacy-protective settings shall be the default (Privacy by Default). Systems shall be designed to collect and process only the minimum PII necessary for the stated purpose."),
        ("A.3.27-02", "GDPR Article 25 Compliance",
         "Systems involving PII processing shall be documented as privacy-by-design compliant before production deployment. The DPIA process (PRIV-POL-A.1.3.2-4) shall be triggered for high-risk processing systems during the design phase. Retrofitting privacy controls after production deployment is not an acceptable approach."),
        ("A.3.28-01", "PII Security Requirements in Development and Acquisition",
         "PII security requirements shall be documented before development begins or before procurement decision for any application that processes PII. Requirements shall address at minimum: authentication, access control, encryption at rest and in transit, logging, and data retention and deletion. Requirements shall be approved by the DPO (privacy requirements) and CISO (security requirements) before commencement."),
        ("A.3.28-02", "Security Requirements Review",
         "PII application security requirements shall be reviewed at each major version release or significant change; upon changes to applicable regulatory requirements; and following a security incident involving the application. For acquired applications, security requirements shall be included in procurement specifications and vendor security assessment."),
        ("A.3.29-01", "PII Architecture Principles",
         "The following principles shall be applied to system architecture involving PII: minimum exposure (PII flows through minimum system components); least privilege in architecture (service-to-service PII access scoped and authenticated); data segregation (PII logically segregated by purpose where feasible); auditability (systems designed to produce logs per A.3.25); restorability (architecture supports backup and recovery per A.3.24); and pseudonymisation pathways for secondary use cases."),
    ]),

    ("Outsourced Development and Test Information", [
        ("A.3.30-01", "Outsourced Development Requirements",
         "Where development of systems processing PII is outsourced: the development partner shall be categorised as a PII Processor or PII-Adjacent supplier per PRIV-POL-A.3.8-10; an agreement covering PII security obligations shall be in place before development access to PII is granted; PII security requirements (A.3.28) shall be communicated and agreed before development commences; and security and privacy requirements shall be included in acceptance testing."),
        ("A.3.30-02", "Oversight of Outsourced Development",
         "The organisation shall direct, monitor, and review outsourced PII system development activities. The organisation shall retain the right to review development artefacts (code, design documents) for PII compliance. The development partner shall report any PII incident discovered during development immediately. Security and privacy review shall be a formal gate in the acceptance process before production deployment."),
        ("A.3.30-03", "PII in Outsourced Development Environments",
         "Development partners shall not use real PII in development or test environments without explicit DPO approval. Where real PII must be used (e.g., for reproducible defect investigation), approval shall be time-limited and documented; the PII shall be deleted after the specific investigation concludes, with deletion confirmed and documented."),
        ("A.3.31-01", "Prohibition on Real PII in Test Environments",
         "Real PII shall not be used in test environments as a default practice. Test environments shall use synthetically generated data that resembles PII in structure but contains no real personal data, or irreversibly anonymised data from real PII datasets (DPO confirmation of anonymisation required before use in testing)."),
        ("A.3.31-02", "Exception: Use of Real PII in Testing",
         "Where use of real PII in testing is operationally necessary, the following shall apply: written approval from the DPO before real PII is copied to the test environment; scope limited to the minimum PII needed for the minimum duration required; test environment shall apply the same access controls and encryption as production; real PII shall be deleted immediately after the specific test concludes with deletion confirmed and documented; and all access to real PII in the test environment shall be logged."),
        ("A.3.31-03", "Test Data Management",
         "Synthetic and anonymised test data sets used for PII processing system testing shall be: documented in a test data inventory (owner, format, currency, purpose); protected against accidental replacement with real PII; and reviewed periodically to ensure they remain representative for testing purposes."),
    ]),
])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 27701:2025"
    ))


# =============================================================================
# QA_VERIFIED: 2026-03-10
# QA_STATUS: PASSED
# QA_TOOL: Claude Code Production Scripts QA Methodology
# CHANGES: Initial generation for Privacy product launch
# =============================================================================
