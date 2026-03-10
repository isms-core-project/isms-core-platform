#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-CHK-A.8 — Openness, Transparency and Notice Compliance Checklist

Controls A.8 / A.8.1: Sub-processor Disclosure,
                       Advance Notice and Objection Rights
Product: ISMS CORE Cloud (ISO/IEC 27018:2025 — Annex A)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Sub-processor Register and Disclosure (A.8.1) — 4 reqs
4. Change Management and Objection Handling (A.8.1) — 5 reqs

Total: 9 requirements across 2 domains
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
DOCUMENT_ID = "CLD-CHK-A.8"
CONTROL_ID = "A.8 / A.8.1"
CONTROL_NAME = "Openness, Transparency and Notice"
SOURCE_POLICY = "CLD-POL-A.8"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-POL-A.8
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Sub-processor Register and Disclosure", [
        ("A.8.1-01", "Sub-processor Register",
         "The organisation shall maintain a Sub-processor Register listing all sub-processors engaged to process PII on the organisation's behalf. For each sub-processor the register shall include: legal entity name; services provided (specific processing operations); PII categories accessed; processing location(s) by country or region; contract reference; controller consent status with date; and date added and last reviewed."),
        ("A.8.1-02", "Register Availability",
         "The Sub-processor Register shall be maintained by the DPO and made available to all PII controllers upon request. The organisation shall also publish a current Sub-Processor List on its website or trust portal for controllers operating under general authorisation. The published list shall be consistent with the internal register."),
        ("A.8.1-03", "Controller Consent Status",
         "Before any sub-processor is engaged to process PII, documented controller consent shall be obtained — either specific written consent for the individual sub-processor or a general authorisation from the controller to engage sub-processors of the type described, subject to advance notice. No sub-processor shall process PII without a documented consent record in the Sub-processor Register."),
        ("A.8.1-04", "Register Currency",
         "The Sub-processor Register shall be updated within 5 business days of any sub-processor change (addition, replacement, material scope change, or termination). Previous versions of the register shall be retained for 5 years to support retrospective audit."),
    ]),

    ("Change Management and Objection Handling", [
        ("A.8.1-05", "Advance Notice of Sub-processor Changes",
         "The organisation shall provide advance notice to PII controllers before implementing any intended change to sub-processor arrangements, including engagement of a new sub-processor, replacement of an existing sub-processor, or material change to the scope or location of an existing sub-processor's processing. Unless a service agreement specifies a longer period, the minimum advance notice period is 30 days."),
        ("A.8.1-06", "Notice Delivery",
         "Sub-processor change notices shall be delivered via the notification channel specified in the service agreement (e.g., email to the designated data protection contact, trust portal notification, or published change log with subscriber alerts). The notice shall include the identity of the new or changed sub-processor, the nature of processing, and the effective date."),
        ("A.8.1-07", "Controller Objection Right",
         "PII controllers operating under general sub-processor authorisation shall have the right to object to any intended sub-processor change during the advance notice period. The organisation's objection handling procedure shall include: acknowledging the objection within 3 business days; engaging with the controller on the grounds; and if the objection cannot be accommodated, allowing contract termination on reasonable terms without penalty."),
        ("A.8.1-08", "Emergency Sub-processor Changes",
         "Where the organisation must engage a replacement sub-processor urgently (e.g., due to sub-processor insolvency or security incident), the organisation shall notify affected PII controllers without undue delay, provide written justification for the emergency change, implement equivalent security and privacy controls on the replacement before PII transfer, and formally update the Sub-processor Register within 5 business days."),
        ("A.8.1-09", "Objection and Change Records",
         "All controller advance notices, controller objections received, and resolution outcomes shall be documented and retained for 5 years. Timestamped copies of the publicly available sub-processor list at each version shall also be retained for 5 years."),
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
