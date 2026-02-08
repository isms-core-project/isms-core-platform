#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.27 — Secure System Architecture and Engineering Principles Compliance Checklist

Control A.8.27: Secure System Architecture and Engineering Principles
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Sec Architecture Documentation (3 reqs)
4. Architecture Review Process (9 reqs)
5. Technology Select Sec Criteria (2 reqs)
6. Security Baselines (4 reqs)
7. Secure Architecture Patterns (4 reqs)
8. Third-Party & Acquired Systems (9 reqs)
9. Compliance Measurement (2 reqs)

Total: 33 requirements across 7 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.27"
CONTROL_ID = "A.8.27"
CONTROL_NAME = "Secure System Architecture and Engineering Principles"
SOURCE_POLICY = "ISMS-OP-POL-A.8.27"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.27
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Sec Architecture Documentation", [
        ("A.8.27-01", "Systems Classified As High-Risk Or",
         "All systems classified as High-Risk or Medium-Risk shall have documented security architecture. Low-Risk systems shall have, at minimum, a completed security checklist."),
        ("A.8.27-02", "Documentation Storage*: Security",
         "Documentation Storage*: Security architecture documentation shall be stored in [Architecture Tool / Confluence / SharePoint] with access restricted to: CISO, Development Manager, System Owner, and personnel with documented need-to-know approved by the CISO. Documentation shall be version-controlled."),
        ("A.8.27-03", "Documentation Currency*: Security",
         "Documentation Currency*: Security architecture documentation shall be reviewed and updated: when significant changes are made to the system, when new threats are identified that affect the system, and at least annually for High-Risk systems."),
    ]),

    ("Architecture Review Process", [
        ("A.8.27-04", "New Systems And Significant Changes To",
         "All new systems and significant changes to existing systems shall undergo security architecture review before implementation."),
        ("A.8.27-05", "Approval Criteria*: Architecture",
         "Approval Criteria*: Architecture shall not be approved if:."),
        ("A.8.27-06", "Incomplete Submissions",
         "Incomplete submissions shall be returned within 3 business days with specific gaps identified. Clock resets upon resubmission of complete documentation."),
        ("A.8.27-07", "Engage External Security Architecture",
         "Organisations shall engage external security architecture specialists when:."),
        ("A.8.27-08", "External Reviewers",
         "External reviewers shall be selected based on: relevant industry certifications (CISSP, CCSP, or equivalent), demonstrated experience with similar architectures, and independence from implementation vendors."),
        ("A.8.27-09", "The Stride Methodology",
         "Where threat modelling is required, the STRIDE methodology shall be used as the primary approach:."),
        ("A.8.27-10", "Threat Models",
         "Threat models shall be retained for:."),
        ("A.8.27-11", "Major Incidents: Threat Models For",
         "Major incidents: Threat models for systems involved in security incidents shall be retained permanently (minimum 7 years)."),
        ("A.8.27-12", "Threat Models",
         "Threat models shall be reviewed and updated: at each major release, when the system architecture changes significantly, when new threat intelligence relevant to the system is identified, and at least annually for High-Risk systems."),
    ]),

    ("Technology Select Sec Criteria", [
        ("A.8.27-13", "Platforms, Frameworks, Or Third-Party",
         "When selecting new technologies, platforms, frameworks, or third-party components, security shall be a selection criterion with equal weight to functional requirements."),
        ("A.8.27-14", "Technology Selection Decisions For",
         "Technology selection decisions for High-Risk systems shall be documented with security assessment evidence and approved by the CISO before procurement."),
    ]),

    ("Security Baselines", [
        ("A.8.27-15", "Maintain Security Baselines For Each",
         "The organisation shall maintain security baselines for each system tier, defining the minimum security controls required."),
        ("A.8.27-16", "System Tier",
         "System tier shall be reviewed and potentially reclassified when:."),
        ("A.8.27-17", "Re-Classification Triggers Updated",
         "Re-classification triggers updated security baseline requirements and architecture review. The System Owner shall request a re-classification review from the CISO when any trigger occurs."),
        ("A.8.27-18", "Security Baselines",
         "Security baselines shall be reviewed annually by the CISO and updated to reflect current threats, technology changes, and regulatory requirements."),
    ]),

    ("Secure Architecture Patterns", [
        ("A.8.27-19", "Maintain A Catalogue Of Approved Secure",
         "The organisation shall maintain a catalogue of approved secure architecture patterns that system designers shall reference when building new systems or modifying existing ones."),
        ("A.8.27-20", "Approved Pattern",
         "Each approved pattern shall document:."),
        ("A.8.27-21", "Approved Patterns",
         "Approved patterns shall be reviewed annually for continued appropriateness."),
        ("A.8.27-22", "New Patterns",
         "New patterns shall be validated through threat modelling before addition to the catalogue."),
    ]),

    ("Third-Party & Acquired Systems", [
        ("A.8.27-23", "Secure Engineering Principles",
         "Secure engineering principles shall apply to third-party developed and acquired systems that are integrated into the organisation's environment."),
        ("A.8.27-24", "Security Architecture Documentation",
         "Security architecture documentation shall be reviewed before procurement approval."),
        ("A.8.27-25", "Vendor Security Assessment",
         "Vendor security assessment shall be conducted per the Supplier and Cloud Services Policy (A.5.19-23)."),
        ("A.8.27-26", "Architecture Compatibility With The",
         "Architecture compatibility with the organisation's security standards shall be verified."),
        ("A.8.27-27", "Third-Party Developers",
         "Third-party developers shall be contractually required to follow the organisation's secure engineering principles."),
        ("A.8.27-28", "Security Architecture Review",
         "Security architecture review shall be required at design milestone."),
        ("A.8.27-29", "Evidence Of Secure Development Practices",
         "Evidence of secure development practices shall be provided."),
        ("A.8.27-30", "Security Testing Results",
         "Security testing results shall be provided before acceptance."),
        ("A.8.27-31", "Vendor Non-Compliance",
         "Vendor non-compliance shall trigger issue escalation per contract terms."),
    ]),

    ("Compliance Measurement", [
        ("A.8.27-32", "The Following Metrics",
         "The following metrics shall be tracked and reported to the CISO quarterly:."),
        ("A.8.27-33", "Metrics Breaching Red Thresholds",
         "Metrics breaching red thresholds shall be escalated to the CISO for immediate attention and reported at the next Management Review."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.27
# =============================================================================
