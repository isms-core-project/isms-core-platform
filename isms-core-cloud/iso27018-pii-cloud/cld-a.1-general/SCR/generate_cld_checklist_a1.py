#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-CHK-A.1 — General (Public Cloud PII Processor) Compliance Checklist

Control A.1: General Applicability and Obligations for Public Cloud PII Processors
Product: ISMS CORE Cloud (ISO/IEC 27018:2025 — Annex A)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. PII Processor Role Obligations (A.1) — 4 reqs
4. Contract and Sub-processor Framework (A.1) — 4 reqs

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
DOCUMENT_ID = "CLD-CHK-A.1"
CONTROL_ID = "A.1"
CONTROL_NAME = "General"
SOURCE_POLICY = "CLD-POL-A.1"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-POL-A.1
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("PII Processor Role Obligations", [
        ("A.1-01", "Processor-Only Role",
         "The organisation shall operate as a PII processor only — processing PII solely on the documented instructions of PII controllers. The organisation shall not determine the purposes or means of PII processing beyond technical service delivery, process PII for its own commercial, analytical, or operational purposes without explicit controller authorisation, or transfer, sell, or otherwise exploit PII processed on behalf of a controller."),
        ("A.1-02", "Instruction Processing",
         "The organisation shall process PII only in accordance with documented, current instructions from the PII controller. Where the organisation is legally required by applicable law to process PII beyond controller instructions, the organisation shall inform the PII controller of that requirement before processing, unless legally prohibited from doing so."),
        ("A.1-03", "Documentation of Controls",
         "The organisation shall document how each applicable control in ISO/IEC 27018:2025 Annex A is addressed within its cloud services. This documentation shall be made available to PII controllers upon request and incorporated into service agreements where contractually required. Documentation shall be reviewed and updated at minimum annually and upon material service changes."),
        ("A.1-04", "Control Implementation Map",
         "The organisation shall maintain a Control Implementation Map linking each CLD-POL-A.X policy to the technical and organisational measures implementing it. The map shall be available to auditors and to PII controllers upon request, demonstrating the completeness of the ISO/IEC 27018:2025 Annex A implementation."),
    ]),

    ("Contract and Sub-processor Framework", [
        ("A.1-05", "Written Contract Requirement",
         "The organisation shall process PII only where a written contract with the PII controller is in place. The contract shall address at minimum: the scope of processing; security obligations; breach notification; sub-processor arrangements; data return or deletion; and audit rights — in accordance with CLD-POL-A.11.11."),
        ("A.1-06", "Processor Agreement Register",
         "The organisation shall maintain a Processor Agreement Register listing all active cloud service agreements under which PII is processed, including: controller identity; processing scope; agreement status and review date; and applicable data residency requirements. No PII processing engagement shall commence without a register entry."),
        ("A.1-07", "Sub-processor Prior Consent",
         "The organisation shall engage sub-processors only with the prior written consent of the PII controller. General authorisation from the controller (covering a class of sub-processors) is acceptable where the service agreement provides for it, subject to the advance notification requirements in CLD-POL-A.8.1."),
        ("A.1-08", "Sub-processor Accountability",
         "The organisation remains fully accountable to PII controllers for the performance of sub-processors' obligations. Sub-processor non-compliance is treated as processor non-compliance for the purposes of the controller agreement. Sub-processor arrangements are governed in detail by CLD-POL-A.11.12."),
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
