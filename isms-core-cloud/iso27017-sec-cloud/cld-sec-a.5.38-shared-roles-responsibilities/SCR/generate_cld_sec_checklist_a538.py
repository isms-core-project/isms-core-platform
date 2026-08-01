#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-SEC-CHK-A.5.38 — Shared Roles and Responsibilities Compliance Checklist

Control 5.38: CLD - Shared roles and responsibilities within a cloud computing environment
Product: ISMS CORE Cloud Sec (ISO/IEC 27017:2026, Clause 5.38)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. CSC Obligations — 4 reqs
4. CSP Obligations — 4 reqs

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
DOCUMENT_ID = "CLD-SEC-CHK-A.5.38"
CONTROL_ID = "5.38"
CONTROL_NAME = "Shared Roles and Responsibilities"
SOURCE_POLICY = "CLD-SEC-POL-A.5.38"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-SEC-POL-A.5.38
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("CSC Obligations", [
        ("5.38-01", "Review CSP-Defined Roles",
         "The organisation shall review the information security roles and responsibilities defined by the CSP for each service consumed, and confirm it can fulfil its allocated roles and responsibilities before the service is put into production use."),
        ("5.38-02", "Agreement Statement of Roles",
         "The organisation shall ensure the information security roles and responsibilities of both the organisation and the CSP are stated in a written agreement, not left to the CSP's public documentation alone."),
        ("5.38-03", "Customer Support Relationship",
         "The organisation shall identify and manage its relationship with the CSP's customer support function for information security matters, including a defined point of contact."),
        ("5.38-04", "CSP Capability Information Request",
         "The organisation shall request information from the CSP regarding its information security capabilities — including authentication, cryptography, backup, and logging — and use third-party or independent-body frameworks to complement CSP disclosures where insufficient."),
    ]),

    ("CSP Obligations", [
        ("5.38-05", "Define and Document Allocation",
         "The organisation shall define and document the allocation of information security roles and responsibilities that its CSCs, the organisation itself, and its own suppliers are each expected to implement."),
        ("5.38-06", "Maintain CSC Relationship",
         "The organisation shall establish and maintain the relationship with each CSC regarding information security issues, based on the documented allocation of roles and responsibilities."),
        ("5.38-07", "Provide Capability Information to CSCs",
         "The organisation shall provide CSCs with information regarding its information security capabilities and measures at a level of clarity sufficient for the CSC to understand them adequately, using recognised third-party or independent-body frameworks where useful."),
        ("5.38-08", "Shared Allocation — Custodianship Principle",
         "The organisation shall take into account, when allocating roles and responsibilities in either capacity, the CSC's data and applications for which the organisation (as CSP) is a custodian, or for which the organisation (as CSC) remains accountable notwithstanding the CSP's technical custody."),
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
