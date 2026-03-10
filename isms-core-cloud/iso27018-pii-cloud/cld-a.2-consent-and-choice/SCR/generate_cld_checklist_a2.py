#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-CHK-A.2 — Consent and Choice Compliance Checklist

Controls A.2 / A.2.1: Prohibition on Unsanctioned Processing,
                       Co-operation on Data Subject Rights
Product: ISMS CORE Cloud (ISO/IEC 27018:2025 — Annex A)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Prohibition on Unsanctioned Processing (A.2) — 4 reqs
4. Co-operation on Data Subject Rights (A.2.1) — 4 reqs

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
DOCUMENT_ID = "CLD-CHK-A.2"
CONTROL_ID = "A.2 / A.2.1"
CONTROL_NAME = "Consent and Choice"
SOURCE_POLICY = "CLD-POL-A.2"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-POL-A.2
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Prohibition on Unsanctioned Processing", [
        ("A.2-01", "No Processing Beyond Controller Instructions",
         "The organisation shall not process PII for any purpose other than the documented instructions of the PII controller. This prohibition includes: marketing, advertising, or audience profiling using controller-owned PII; data analytics or product improvement using PII beyond agreed service delivery telemetry; sale, licensing, or sharing of PII with third parties for commercial purposes; and training machine learning models on PII without explicit written controller authorisation."),
        ("A.2-02", "Anonymisation Before Secondary Use",
         "Where the organisation wishes to use aggregated or anonymised data derived from PII for service improvement, the organisation shall document the anonymisation methodology and obtain written confirmation from the DPO that the result is genuinely anonymised before proceeding. DPO anonymisation confirmations shall be retained."),
        ("A.2-03", "Legally Compelled Processing",
         "Where applicable law requires the organisation to process PII beyond controller instructions, the organisation shall: inform the PII controller of the requirement before processing, unless legally prohibited; process only the minimum PII required to comply with the legal obligation; document the legal basis; and notify the controller at the earliest opportunity when any prohibition on notification lapses."),
        ("A.2-04", "Legally Compelled Processing Records",
         "All instances of processing beyond controller instructions pursuant to a legal obligation shall be documented, including the legal authority, the PII scope, the date of processing, whether the controller was notified (and if not, why), and the date of subsequent notification. Records shall be retained for 3 years."),
    ]),

    ("Co-operation on Data Subject Rights", [
        ("A.2.1-01", "Technical Capability Requirement",
         "The organisation shall implement and maintain technical capabilities within its cloud services enabling PII controllers to fulfil data subject rights. Required capabilities: access (PII export in machine-readable format); rectification (field-level correction with replication propagation); erasure (confirmed deletion including cached and replicated copies); restriction (isolation from active processing without deletion); portability (structured JSON/CSV export); and objection (suspension of automated processing for specific PII)."),
        ("A.2.1-02", "Response Timeframes",
         "The organisation shall respond to PII controller requests for data subject rights assistance within timeframes enabling statutory compliance. Unless the service agreement specifies shorter timeframes, the organisation shall: acknowledge controller requests within 1 business day; complete data subject rights fulfilment requests within 5 business days; and notify the controller immediately of any technical constraint preventing fulfilment within this period."),
        ("A.2.1-03", "Capability Documentation",
         "The organisation shall maintain and make available to PII controllers documentation describing the data subject rights capabilities available within each cloud service, including how to initiate each rights fulfilment operation, expected completion times, confirmation mechanisms, and the escalation path for requesting assistance where self-service is insufficient. Documentation shall be updated within 30 days of any material capability change."),
        ("A.2.1-04", "Cooperation Records",
         "The organisation shall maintain records of all data subject rights assistance provided to PII controllers, including request receipt date, type of right exercised, controller identifier, fulfilment date, and outcome. Records shall be made available to the controller on request and retained for the duration of the contract plus 3 years."),
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
