#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.30 — Outsourced Development Compliance Checklist

Control A.8.30: Outsourced Development
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Vendor Security Assessment (5 reqs)
4. Contractual Security Reqs (1 reqs)
5. Secure Dev Reqs for Vendors (8 reqs)
6. Code Review and Sec Testing (7 reqs)
7. Acceptance Criteria (2 reqs)
8. IP Property and Code Escrow (5 reqs)
9. Ongoing Monitoring (2 reqs)
10. Vendor Sec Incident Response (1 reqs)
11. Data Protection Requirements (11 reqs)

Total: 42 requirements across 9 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/A.0-checklist-engine/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_OP_ROOT / 'A.0-checklist-engine'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.8.30"
CONTROL_ID = "A.8.30"
CONTROL_NAME = "Outsourced Development"
SOURCE_POLICY = "ISMS-OP-POL-A.8.30"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.30
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Vendor Security Assessment", [
        ("A.8.30-01", "Before Engaging An External Development",
         "Before engaging an external development partner, the organisation shall conduct a security assessment to confirm the vendor's ability to meet information security requirements."),
        ("A.8.30-02", "Be Classified Based On The Highest",
         "Vendors shall be classified based on the highest risk factor present:."),
        ("A.8.30-03", "Tier Determination",
         "Tier determination shall be documented in the vendor security assessment record and reviewed upon scope changes."),
        ("A.8.30-04", "Assessment Results",
         "Assessment results shall be documented and retained for the duration of the vendor relationship plus 3 years."),
        ("A.8.30-05", "Vendors That Fail The Security",
         "Vendors that fail the security assessment shall not be engaged until identified deficiencies are remediated and verified."),
    ]),

    ("Contractual Security Reqs", [
        ("A.8.30-06", "Outsourced Development Agreements",
         "All outsourced development agreements shall include security requirements as contractual obligations."),
    ]),

    ("Secure Dev Reqs for Vendors", [
        ("A.8.30-07", "The Organisation'S Secure Development",
         "The organisation's secure development standards shall be communicated to vendors at the start of every engagement."),
        ("A.8.30-08", "Provide Each Vendor With",
         "The organisation shall provide each vendor with:."),
        ("A.8.30-09", "Implement Controls To Mitigate Software",
         "Vendors shall implement controls to mitigate software supply chain risks in accordance with OWASP Top 10:2025 A03 (Software Supply Chain Failures):."),
        ("A.8.30-10", "Third-Party Dependencies",
         "All third-party dependencies shall be inventoried and tracked in an SBOM (CycloneDX or SPDX format)."),
        ("A.8.30-11", "Be Pinned To Specific Versions And",
         "Dependencies shall be pinned to specific versions and sourced from trusted registries."),
        ("A.8.30-12", "Transitive Dependencies",
         "Transitive dependencies shall be included in vulnerability scanning."),
        ("A.8.30-13", "Monitor Dependencies Against",
         "Vendors shall monitor dependencies against vulnerability databases (NVD, OSV, GitHub Advisory Database) and remediate identified vulnerabilities within the agreed SLAs."),
        ("A.8.30-14", "Use Of Unmaintained Or End-Of-Life",
         "Use of unmaintained or end-of-life components shall require documented risk acceptance from the organisation."),
    ]),

    ("Code Review and Sec Testing", [
        ("A.8.30-15", "Outsourced Code",
         "All outsourced code shall undergo independent security validation by the organisation before acceptance."),
        ("A.8.30-16", "Vendor-Side Test Results",
         "Vendor-side test results shall be shared with the organisation at agreed intervals (minimum: per milestone or sprint delivery)."),
        ("A.8.30-17", "Minimum Testing Baseline*: All Security",
         "Minimum testing baseline*: All security testing shall, at a minimum, cover the OWASP Top 10:2025 categories."),
        ("A.8.30-18", "Penetration Testing",
         "All penetration testing shall be conducted by an independent external specialist company meeting at least one of:."),
        ("A.8.30-19", "Penetration Test Provider",
         "Penetration test provider shall not be the same entity as the development vendor to ensure independence."),
        ("A.8.30-20", "Vulnerabilities Identified During",
         "Vulnerabilities identified during testing shall be remediated by the vendor at the vendor's cost before the organisation accepts the deliverable. Critical and High vulnerabilities shall block acceptance."),
        ("A.8.30-21", "Vulnerabilities Identified In Vendor",
         "All vulnerabilities identified in vendor deliverables shall be tracked through resolution:."),
    ]),

    ("Acceptance Criteria", [
        ("A.8.30-22", "Outsourced Deliverables",
         "Outsourced deliverables shall not be accepted or deployed to production until all acceptance criteria are satisfied."),
        ("A.8.30-23", "Acceptance Records",
         "Acceptance records shall be retained for the duration of the application lifecycle plus 3 years."),
    ]),

    ("IP Property and Code Escrow", [
        ("A.8.30-24", "The Development Agreement",
         "The development agreement shall clearly define ownership of all work products, including source code, documentation, designs, and related intellectual property."),
        ("A.8.30-25", "The Default Position",
         "Where the organisation commissions bespoke development, the default position shall be that the organisation owns all intellectual property rights in the deliverables upon final payment or upon delivery if payment-on-delivery, whichever occurs first. Any deviation from full ownership shall be documented, approved by Legal and the CISO, and justified by business need."),
        ("A.8.30-26", "Vendor Retains Rights To Pre-Existing",
         "Where full ownership transfer is not possible (e.g., vendor retains rights to pre-existing components or frameworks), the agreement shall specify:."),
        ("A.8.30-27", "For Tier 1 Vendor Engagements Where",
         "For Tier 1 vendor engagements where the organisation does not hold the source code directly, the organisation shall establish a code escrow arrangement with an independent escrow agent (e.g., Escode, Codekeeper, or equivalent)."),
        ("A.8.30-28", "Code Escrow Is Not Required, But",
         "Where the organisation holds source code directly in its own repositories, code escrow is not required, but the organisation shall maintain its own verified backups."),
    ]),

    ("Ongoing Monitoring", [
        ("A.8.30-29", "Continuously Monitor Outsourced",
         "The organisation shall continuously monitor outsourced development activities throughout the engagement lifecycle."),
        ("A.8.30-30", "Vendor Performance Scorecard",
         "Vendor performance scorecard shall be maintained quarterly, tracking: security testing compliance, SLA adherence, incident count, and audit findings. Results shall be reported to management annually."),
    ]),

    ("Vendor Sec Incident Response", [
        ("A.8.30-31", "Notify Executive Management Within 24",
         "CISO shall notify Executive Management within 24 hours of any vendor incident affecting organisational data or systems."),
    ]),

    ("Data Protection Requirements", [
        ("A.8.30-32", "Additional Data Protection Requirements",
         "Where outsourced development involves access to personal data or systems processing personal data, additional data protection requirements shall apply."),
        ("A.8.30-33", "In Accordance With Swiss Nfadp Art",
         "In accordance with Swiss nFADP Art. 9, the organisation shall execute a DPA with the development vendor that addresses:."),
        ("A.8.30-34", "A Transfer Impact Assessment",
         "A transfer impact assessment shall be completed per Swiss nFADP requirements."),
        ("A.8.30-35", "Appropriate Safeguards",
         "Appropriate safeguards shall be in place (e.g., Standard Contractual Clauses, adequacy decisions by the Federal Council, or binding corporate rules)."),
        ("A.8.30-36", "Gdpr Chapter V Transfer Requirements",
         "Where the vendor processes data of EU/EEA individuals, GDPR Chapter V transfer requirements shall also be met."),
        ("A.8.30-37", "Not Receive Production Personal Data For",
         "Vendors shall not receive production personal data for development or testing purposes."),
        ("A.8.30-38", "Sanitised, Anonymised, Or Pseudonymised",
         "Where realistic data is required, sanitised, anonymised, or pseudonymised data shall be used."),
        ("A.8.30-39", "Any Use Of Transformed Personal Data",
         "Any use of transformed personal data shall be documented and approved by the Data Protection Officer or CISO."),
        ("A.8.30-40", "Rare Edge Cases), Data",
         "Where absolutely necessary to use production data (complex data relationships, rare edge cases), data shall be:."),
        ("A.8.30-41", "The Organisation",
         "Where a vendor security incident results in high risk to data subjects (nFADP Art. 24), the organisation shall notify the FDPIC without undue delay. High risk indicators include:."),
        ("A.8.30-42", "Vendor Dpa",
         "Vendor DPA shall require vendor to provide all information necessary for FDPIC notification within 48 hours of incident discovery."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.30
# =============================================================================
