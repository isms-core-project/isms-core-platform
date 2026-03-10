#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-CHK-A.4 — Collection Limitation Compliance Checklist

Control A.4: Collection Limitation for Public Cloud PII Processors
Product: ISMS CORE Cloud (ISO/IEC 27018:2025 — Annex A)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Minimum Necessary Collection (A.4) — 4 reqs
4. Excess PII and Development Environments (A.4) — 3 reqs

Total: 7 requirements across 2 domains
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
DOCUMENT_ID = "CLD-CHK-A.4"
CONTROL_ID = "A.4"
CONTROL_NAME = "Collection Limitation"
SOURCE_POLICY = "CLD-POL-A.4"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-POL-A.4
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Minimum Necessary Collection", [
        ("A.4-01", "Minimum PII Collection",
         "The organisation shall collect, retain, or otherwise process only the minimum PII necessary to deliver the contracted cloud service. The organisation shall not request or accept PII categories from the PII controller beyond what is required for service delivery; store PII in system components, logs, or operational databases beyond operational necessity; or replicate PII across environments without explicit controller authorisation."),
        ("A.4-02", "Collection Practice Documentation",
         "The organisation shall document PII collection practices for each cloud service, including: categories of PII collected or received during service delivery; the operational justification for each PII category; the system components, logs, and storage locations where PII may be present; and retention periods applicable to each collection type. Documentation shall be reviewed annually and upon material changes to service architecture."),
        ("A.4-03", "Annual Collection Review",
         "Collection practice documentation shall be reviewed and signed off at minimum annually by the CISO or DPO. The review shall confirm that no PII categories are being collected beyond those necessary for contracted service delivery. Review records shall be retained for 3 years."),
        ("A.4-04", "Controller Instruction Primacy",
         "The scope of PII that may be collected or processed is defined by the PII controller's instructions and the service agreement. Where the organisation identifies ambiguity in what PII may be collected, written clarification shall be obtained from the controller before collection commences. Ambiguity does not authorise broader collection."),
    ]),

    ("Excess PII and Development Environments", [
        ("A.4-05", "Excess PII Handling",
         "Where the organisation determines that PII has been collected that exceeds the scope of the contracted service, the organisation shall: notify the PII controller of the excess PII without undue delay; agree with the controller whether the excess PII is to be returned or securely deleted; complete the agreed action within the agreed timeframe; and document the event and outcome. Excess PII event records shall be retained for the duration of the contract plus 3 years."),
        ("A.4-06", "Development and Test Environment Restriction",
         "PII from production environments shall not be used in development, testing, or staging environments without explicit written authorisation from the PII controller. Where controller authorisation is obtained, the minimum necessary PII shall be used and the same security controls applicable in production shall apply. Development/test PII authorisation records shall be retained for the duration of use plus 3 years."),
        ("A.4-07", "Post-Test Deletion",
         "Where PII is used in a development or test environment under controller authorisation, the PII shall be deleted immediately after the specific test or development activity concludes. Deletion shall be confirmed and documented. Authorisation does not constitute permission for indefinite retention of production PII in non-production environments."),
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
