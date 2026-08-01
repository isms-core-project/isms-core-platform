#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-SEC-CHK-A.5.39 — Agreement on Cloud Service Partner Roles Compliance Checklist

Control 5.39: CLD - Agreement on the roles and responsibilities of the cloud service partner
Product: ISMS CORE Cloud Sec (ISO/IEC 27017:2026, Clause 5.39)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Defining and Agreeing CSN Roles — 4 reqs
4. Governance and Oversight — 4 reqs

Total: 8 requirements across 2 domains
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
DOCUMENT_ID = "CLD-SEC-CHK-A.5.39"
CONTROL_ID = "5.39"
CONTROL_NAME = "Agreement on Cloud Service Partner Roles"
SOURCE_POLICY = "CLD-SEC-POL-A.5.39"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-SEC-POL-A.5.39
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Defining and Agreeing CSN Roles", [
        ("5.39-01", "Classify CSN Sub-Role",
         "The organisation shall classify each prospective cloud service partner (CSN) against the ISO/IEC 22123-3 sub-roles (cloud service developer, cloud auditor, cloud service broker) before engagement."),
        ("5.39-02", "Written Agreement Before Work Begins",
         "The organisation shall reach written agreement with the CSN on its roles and responsibilities before the CSN begins any activity affecting a cloud service the organisation consumes or delivers."),
        ("5.39-03", "Consistency with Shared Responsibility Allocation",
         "The organisation shall verify that the agreement with the CSN is consistent with the shared roles and responsibilities already established between the organisation and its CSC or CSP counterparty under CLD-SEC-POL-A.5.38."),
        ("5.39-04", "Contractual Requirements",
         "Every cloud service partner engagement shall be governed by a written agreement, negotiated per ISMS-POL-A.5.19-23-S2, that identifies the CSN's sub-role(s) and states the specific information security responsibilities assigned."),
    ]),

    ("Governance and Oversight", [
        ("5.39-05", "Recognise Dual CSN/CSP Role",
         "Where a cloud service partner also independently delivers a cloud service to the organisation, the organisation shall apply CLD-SEC-POL-A.5.38 to that CSP relationship in addition to CSN-specific requirements."),
        ("5.39-06", "CSN Role Register",
         "The organisation shall maintain a CSN Role Register listing all active cloud service partners with assigned sub-role(s), scope, and agreement reference."),
        ("5.39-07", "Annual Review",
         "The organisation shall review the CSN Role Register at least annually, confirming each active CSN's classification, agreed responsibilities, and continued consistency with the relevant Shared Responsibility Matrix."),
        ("5.39-08", "Escalation of Scope Conflicts",
         "The organisation shall escalate to the Cloud Security Manager, and where unresolved to the CISO, any instance where a CSN's actual activity exceeds its agreed scope or conflicts with the CSC/CSP shared responsibility allocation."),
    ]),
])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 27017:2026"
    ))


# =============================================================================
# QA_VERIFIED: 2026-08-01
# QA_STATUS: PASSED
# QA_TOOL: Claude Code Production Scripts QA Methodology
# CHANGES: Initial generation for Cloud Sec product launch
# =============================================================================
