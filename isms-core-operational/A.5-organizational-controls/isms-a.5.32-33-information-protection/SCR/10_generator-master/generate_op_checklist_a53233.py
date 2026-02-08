#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.32-33 — Information Protection and Records Management Compliance Checklist

Controls A.5.32-33: Information Protection and Records Management
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. IP and Records Mgmt Systems (1 reqs)
4. Intellectual Property Prot (19 reqs)
5. Records Protection (16 reqs)
6. Privacy Prots Records (2 reqs)

Total: 38 requirements across 4 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/SCR/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_OP_ROOT / 'SCR'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.5.32-33"
CONTROL_ID = "A.5.32-33"
CONTROL_NAME = "Information Protection and Records Management"
SOURCE_POLICY = "ISMS-OP-POL-A.5.32-33"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.32-33
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("IP and Records Mgmt Systems", [
        ("A.5.32-33-01", "Use The Following Systems To Manage",
         "The organisation shall use the following systems to manage intellectual property and records:."),
    ]),

    ("Intellectual Property Prot", [
        ("A.5.32-33-02", "Identify And Classify All Intellectual",
         "The organisation shall identify and classify all intellectual property assets:."),
        ("A.5.32-33-03", "An Ip Register",
         "An IP register shall be maintained recording all significant intellectual property assets. The register shall include, at minimum:."),
        ("A.5.32-33-04", "The Ip Register",
         "The IP register shall be reviewed annually by Legal Counsel (or equivalent role) and the CISO."),
        ("A.5.32-33-05", "Protection Controls",
         "Protection controls shall be implemented based on IP type and classification:."),
        ("A.5.32-33-06", "Third Parties (Vendors, Consultants,",
         "All third parties (vendors, consultants, contractors, partners) accessing organisation IP or confidential records shall sign a Non-Disclosure Agreement (NDA) before access is granted."),
        ("A.5.32-33-07", "Renewal: For Ongoing Relationships, Ndas",
         "Renewal: For ongoing relationships, NDAs shall be reviewed and renewed before expiration."),
        ("A.5.32-33-08", "Require Third Party To Return Or",
         "NDA shall require third party to return or certify deletion of all organisation IP upon contract termination."),
        ("A.5.32-33-09", "Business Owner",
         "Business owner shall verify return/deletion and document verification in agreement register."),
        ("A.5.32-33-10", "Nda Register Review: Legal Counsel",
         "NDA Register Review: Legal Counsel shall review NDA register quarterly* to identify expiring NDAs requiring renewal and terminated relationships requiring IP return verification. Target: 100% of active third parties with valid NDAs."),
        ("A.5.32-33-11", "Software Used By The Organisation",
         "All software used by the organisation shall be properly licensed and compliant:."),
        ("A.5.32-33-12", "Be Acquired Through Official Channels",
         "Software shall be acquired through official channels only. Evidence of valid licences shall be retained."),
        ("A.5.32-33-13", "Be Used In Accordance With Licence",
         "Software shall be used in accordance with licence terms."),
        ("A.5.32-33-14", "A Software Asset Management (Sam)",
         "A Software Asset Management (SAM) register shall be maintained recording: software name and version, licence type (commercial, open-source, freeware), person responsible, number of licences purchased vs. in use, licence location (key, certificate, portal), deployment locations, and review dates."),
        ("A.5.32-33-15", "Only Software Supported By The",
         "Only software supported by the manufacturer shall be used in production. End-of-life software shall be identified and migrated per the vulnerability management policy."),
        ("A.5.32-33-16", "Be Installed Only By Authorised",
         "Software shall be installed only by authorised personnel."),
        ("A.5.32-33-17", "Comply With Third-Party Intellectual",
         "The organisation shall comply with third-party intellectual property rights:."),
        ("A.5.32-33-18", "Creative Commons And Other Content",
         "Creative Commons and other content licence restrictions shall be honoured."),
        ("A.5.32-33-19", "Copyleft Obligations*: If Gpl-Licensed",
         "Copyleft Obligations*: If GPL-licensed code triggers copyleft obligations (e.g., distribution of modified binaries), Development Manager shall provide source code to recipients per GPL terms, document compliance in OSS register, and notify Legal Counsel."),
        ("A.5.32-33-20", "Oss Register Review: Development Manager",
         "OSS Register Review: Development Manager shall review OSS register quarterly* to verify all components are properly licensed and documented. Target: 100% OSS components with valid licence approval."),
    ]),

    ("Records Protection", [
        ("A.5.32-33-21", "Classify Records Based On Retention",
         "The organisation shall classify records based on retention requirements and protection needs:."),
        ("A.5.32-33-22", "A Documented Retention Schedule",
         "A documented retention schedule shall be maintained:."),
        ("A.5.32-33-23", "Conflict Resolution: Where Multiple",
         "Conflict resolution: Where multiple regulations apply, the most stringent retention requirement shall prevail. Where a deletion or erasure request conflicts with legal retention obligations, retention takes precedence — the records shall be access-restricted, the decision documented with Legal Counsel approval, and DPO involvement obtained for personal data."),
        ("A.5.32-33-24", "Grace Period*: Records May Be Retained",
         "Grace Period*: Records may be retained up to 12 months beyond the minimum retention period to allow for orderly disposal processes. Records shall not be retained indefinitely without documented justification."),
        ("A.5.32-33-25", "Annual Review*: Legal Counsel",
         "Annual Review*: Legal Counsel shall review the retention schedule annually and update for regulatory changes, new record types, or business needs."),
        ("A.5.32-33-26", "Be Protected Throughout Their Lifecycle",
         "Records shall be protected throughout their lifecycle:."),
        ("A.5.32-33-27", "Backup Restoration Testing",
         "Backup restoration testing shall be performed quarterly for critical records (select 3 sample records from each category, perform test restoration, verify integrity and completeness). Target: 100% successful restoration."),
        ("A.5.32-33-28", "Critical Records",
         "Critical records shall have backups stored in a geographically separate location (minimum 100 km from primary site)."),
        ("A.5.32-33-29", "Backups",
         "Backups containing confidential records shall be encrypted (AES-256 or equivalent)."),
        ("A.5.32-33-30", "Be Disposed Of Securely When The",
         "Records shall be disposed of securely when the retention period expires (and no legal hold applies):."),
        ("A.5.32-33-31", "Disposal Records",
         "Disposal records shall be maintained for the audit trail (minimum 3 years)."),
        ("A.5.32-33-32", "Certificates Of Destruction",
         "Certificates of destruction shall be obtained for confidential and above records."),
        ("A.5.32-33-33", "Third-Party Destruction",
         "Third-party destruction shall be verified through vendor certifications and chain-of-custody documentation."),
        ("A.5.32-33-34", "Disposal Verification*: Internal Audit",
         "Disposal Verification*: Internal Audit shall sample disposal records annually to verify disposal occurred within timeframe, certificates of destruction obtained for confidential records, and legal holds were checked. Target: 100% compliance with disposal procedures."),
        ("A.5.32-33-35", "Custodian Notification (Within 24",
         "Custodian Notification (within 24 hours): Legal Counsel sends hold notice to all identified custodians via email. Custodians acknowledge receipt and understanding within 2 business days. Notice shall state: 'You are hereby instructed to preserve and not delete, modify, or destroy any records related to [matter]. This includes emails, documents, files, and any other information in your possession or control. Normal deletion activities must be suspended. This hold remains in effect until formally released by Legal Counsel.'."),
        ("A.5.32-33-36", "Compliance Verification*: Internal Audit",
         "Compliance Verification*: Internal Audit shall verify legal hold compliance annually (sample custodian acknowledgements, verify IT suspension was implemented)."),
    ]),

    ("Privacy Prots Records", [
        ("A.5.32-33-37", "Security Logs",
         "Security logs containing user activity: access restricted to IT Security Team and Internal Audit; logs shall not be browsed by line managers for employee monitoring."),
        ("A.5.32-33-38", "Retention Minimisation*: Personal Data",
         "Retention Minimisation*: Personal data in records shall not be retained longer than necessary. Annual review: Records Manager and DPO shall review retention schedule to verify personal data retention periods remain justified and comply with nFADP Art. 6 (proportionality)."),
    ]),

])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS
    ))


# =============================================================================
# QA_VERIFIED: 2026-02-08
# QA_STATUS: PASSED - AUTO-GENERATED (Phase 2 Operational Checklist)
# QA_TOOL: meta_generate_op_checklists.py
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.32-33
# =============================================================================
