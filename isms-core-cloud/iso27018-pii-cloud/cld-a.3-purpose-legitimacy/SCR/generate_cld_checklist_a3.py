#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-CHK-A.3 — Purpose Legitimacy and Specification Compliance Checklist

Controls A.3.1-A.3.2: Public Cloud PII Processor's Purpose,
                       Commercial Use Prohibition
Product: ISMS CORE Cloud (ISO/IEC 27018:2025 — Annex A)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Purpose Restriction (A.3.1) — 4 reqs
4. Commercial Use Prohibition (A.3.2) — 4 reqs

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
DOCUMENT_ID = "CLD-CHK-A.3"
CONTROL_ID = "A.3.1-2"
CONTROL_NAME = "Purpose Legitimacy and Specification"
SOURCE_POLICY = "CLD-POL-A.3"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-POL-A.3
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Purpose Restriction", [
        ("A.3.1-01", "Processing Restricted to Agreed Purposes",
         "The organisation shall process PII only for the purposes explicitly documented in the service agreement or written processing instructions received from the PII controller. Processing shall not be extended to new purposes without prior written controller authorisation."),
        ("A.3.1-02", "Processing Description in Agreements",
         "All cloud service agreements with PII controllers shall include a processing description specifying: the categories of PII to be processed; the purposes of processing; the processing operations to be performed; the duration of processing; and any permitted sub-processing arrangements."),
        ("A.3.1-03", "New Purpose Authorisation",
         "Where the organisation identifies an operational need to process PII for a purpose not covered by the current agreement, the organisation shall: document the proposed new purpose in writing; obtain written controller authorisation before processing begins; record the authorisation in the Processor Agreement Register; and cease the additional processing if authorisation is withheld or withdrawn."),
        ("A.3.1-04", "Operational Telemetry",
         "Service telemetry and operational metadata that incidentally contains PII shall be treated as PII subject to this policy. Telemetry PII retention shall be limited to the minimum period necessary for operational purposes and shall not be used for analytics, product improvement, or commercial purposes without controller authorisation."),
    ]),

    ("Commercial Use Prohibition", [
        ("A.3.2-01", "Absolute Commercial Use Prohibition",
         "The organisation shall not use PII processed on behalf of a PII controller for any of the organisation's own commercial purposes, including: targeted advertising or ad profiling; sale or licensing of PII or derived datasets to third parties; training or improving machine learning models using PII; competitive intelligence gathering; or market research or customer analytics not directly supporting the contracted service. This prohibition applies regardless of aggregation or pseudonymisation unless DPO has confirmed genuine anonymisation in writing."),
        ("A.3.2-02", "Contractual Commitment",
         "Service agreements shall include an explicit clause confirming the commercial use prohibition. Any proposed commercial use arrangement (including arrangements involving genuinely anonymised data) shall be proposed to and agreed by the PII controller in writing before implementation, disclosed in the service agreement, and reviewed by the DPO and Legal/Compliance before execution."),
        ("A.3.2-03", "Technical Separation",
         "The organisation shall implement technical access controls separating controller PII from the organisation's internal product and analytics systems. The organisation's marketing and commercial teams shall be prohibited from accessing controller PII without DPO authorisation. The commercial use prohibition shall be included in employee training and confidentiality agreements."),
        ("A.3.2-04", "DPO Anonymisation Confirmation",
         "Where the organisation proposes to use data derived from controller PII on the basis that it is genuinely anonymised, a written DPO confirmation that the anonymisation is irreversible and meets the applicable regulatory standard shall be obtained before use. DPO confirmations shall be retained for the duration of use plus 3 years."),
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
