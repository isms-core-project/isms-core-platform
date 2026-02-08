#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.4 — Management Responsibilities Compliance Checklist

Control A.5.4: Management Responsibilities
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Mgmt Commitment Requirements (7 reqs)
4. Security Culture Leadership (4 reqs)
5. Personnel Compl Accountability (6 reqs)
6. Management Review Participation (6 reqs)
7. Mgmt Commitment Assessment (2 reqs)
8. Escalation Path (1 reqs)

Total: 26 requirements across 6 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.4"
CONTROL_ID = "A.5.4"
CONTROL_NAME = "Management Responsibilities"
SOURCE_POLICY = "ISMS-OP-POL-A.5.4"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.4
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Mgmt Commitment Requirements", [
        ("A.5.4-01", "Management Personnel",
         "All management personnel shall demonstrate active commitment to information security through:."),
        ("A.5.4-02", "Ensure Adequate Resources Are Available",
         "Management shall ensure adequate resources are available for information security:."),
        ("A.5.4-03", "Adequacy Criteria* For Resource",
         "Adequacy criteria* for resource allocation decisions shall consider:."),
        ("A.5.4-04", "Resource Requests For Approved Security",
         "Resource requests for approved security initiatives shall be processed within 30 calendar days. Disputes over resource adequacy shall be escalated per the escalation path defined in this policy."),
        ("A.5.4-05", "Ensure Their Teams Understand And Comply",
         "Management shall ensure their teams understand and comply with applicable security policies:."),
        ("A.5.4-06", "Management Commitment",
         "Management commitment shall be assessed annually using objective criteria:."),
        ("A.5.4-07", "Assessment Results",
         "Assessment results shall be documented and reviewed by Executive Management. Scores below 70% trigger a mandatory remediation plan (see Remediation for Non-Compliance)."),
    ]),

    ("Security Culture Leadership", [
        ("A.5.4-08", "Foster A Positive Security Culture",
         "Management shall foster a positive security culture across the organisation through deliberate action and consistent example."),
        ("A.5.4-09", "Create An Environment Where Personnel",
         "Management shall create an environment where personnel feel safe reporting security issues:."),
        ("A.5.4-10", "Implement A Structured Recognition",
         "Management shall implement a structured recognition programme for security-conscious behaviour:."),
        ("A.5.4-11", "An Annual Security Culture Survey",
         "An annual Security Culture Survey shall be conducted to measure the effectiveness of management's security leadership and the organisation's overall security awareness posture."),
    ]),

    ("Personnel Compl Accountability", [
        ("A.5.4-12", "Ensure All Personnel Under Their",
         "Management shall ensure all personnel under their authority comply with information security requirements throughout the employment lifecycle."),
        ("A.5.4-13", "Verify That New Personnel Complete All",
         "Management shall verify that new personnel complete all security onboarding requirements before being granted system access."),
        ("A.5.4-14", "Access Gate*: System Access (Beyond",
         "Access gate*: System access (beyond basic email and intranet) shall not be provisioned until items 1-4 are confirmed complete. [Identity Provider] group assignment conditional on [LMS] training completion status."),
        ("A.5.4-15", "Maintain Continuous Oversight Of",
         "Management shall maintain continuous oversight of personnel compliance:."),
        ("A.5.4-16", "Important*: Security Performance",
         "Important*: Security performance criteria shall be communicated to personnel at the start of each review period. No individual shall be evaluated against criteria they were not informed of in advance."),
        ("A.5.4-17", "Ensure Timely And Complete Security",
         "Management shall ensure timely and complete security offboarding for departing personnel."),
    ]),

    ("Management Review Participation", [
        ("A.5.4-18", "Actively Participate In Isms Management",
         "Management shall actively participate in ISMS management review activities as required by ISO 27001:2022 Clause 9.3."),
        ("A.5.4-19", "Active Participation Means More Than",
         "Active participation means more than attendance. Management personnel shall:."),
        ("A.5.4-20", "Quarterly Management Review",
         "Each quarterly management review shall follow a standardised agenda to ensure consistent coverage and efficient use of executive time:."),
        ("A.5.4-21", "Provide The Following Inputs To Isms",
         "Management shall provide the following inputs to ISMS management reviews:."),
        ("A.5.4-22", "Within Management Reviews, Management",
         "Within management reviews, management personnel shall exercise their authority to:."),
        ("A.5.4-23", "Be Tracked And Reported As Part",
         "Participation shall be tracked and reported as part of the annual management commitment assessment."),
    ]),

    ("Mgmt Commitment Assessment", [
        ("A.5.4-24", "An Annual Management Commitment",
         "An annual Management Commitment Assessment shall be conducted by the CISO to evaluate management's fulfilment of their information security responsibilities. The assessment shall cover:."),
        ("A.5.4-25", "Management Responsibility Gaps",
         "All management responsibility gaps shall be recorded in the central ISMS Gap Register maintained in [GRC Tool / SharePoint / Confluence]. The Gap Register is the single source of truth for tracking management commitment findings across all assessment cycles."),
    ]),

    ("Escalation Path", [
        ("A.5.4-26", "The Following Escalation Paths",
         "The following escalation paths shall be used for security-related matters:."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.4
# =============================================================================
