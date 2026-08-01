#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-SEC-CHK-A.8.35 — Segregation in Virtual Computing Environments Compliance Checklist

Control 8.35: CLD - Segregation in virtual computing environments
Product: ISMS CORE Cloud Sec (ISO/IEC 27017:2026, Clause 8.35)

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
DOCUMENT_ID = "CLD-SEC-CHK-A.8.35"
CONTROL_ID = "8.35"
CONTROL_NAME = "Segregation in Virtual Computing Environments"
SOURCE_POLICY = "CLD-SEC-POL-A.8.35"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-SEC-POL-A.8.35
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("CSC Obligations", [
        ("8.35-01", "Define Segregation Requirements",
         "The organisation shall define its requirements for segregating its environment to achieve tenant isolation within the shared virtual environment of any cloud service it uses."),
        ("8.35-02", "Verify CSP Meets Requirements",
         "The organisation shall verify, before and periodically during use of the service, that the CSP meets the organisation's stated segregation requirements."),
        ("8.35-03", "Periodic Re-verification",
         "The organisation shall repeat segregation verification at least annually, and whenever the CSP announces a material change to its virtualization or multi-tenancy architecture."),
        ("8.35-04", "Regulatory Segregation Requirements",
         "Where applicable laws or regulations require the segregation of networks or the isolation of network traffic, the organisation shall ensure its virtual computing segregation controls satisfy those requirements in addition to this policy's baseline."),
    ]),

    ("CSP Obligations", [
        ("8.35-05", "Enforce Logical Segregation by Layer",
         "The organisation shall enforce logical segregation of CSC data, virtualized applications, operating systems, storage, and network resources, to ensure isolation of resources used by different tenants."),
        ("8.35-06", "Risk Assessment of CSC-Supplied Software",
         "The organisation shall assess the risks associated with running CSC-supplied software within its cloud services before permitting such software to run in shared infrastructure."),
        ("8.35-07", "Separate Internal Administration",
         "The organisation shall enforce separation of its own internal administration functions from the resources used by CSCs."),
        ("8.35-08", "Technology-Dependent Segregation Implementation",
         "Where network and storage configurations are virtualized through a software virtualization function, the organisation shall implement segregation using the segregation functions native to that software, in addition to underlying physical or network-level controls."),
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
