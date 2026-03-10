#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.2.3.2 — PII Principal Obligations (Processor) Compliance Checklist

Control A.2.3.2: Providing Customers with Means to Comply with PII Principal Obligations
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Processor Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Rights Fulfilment Capabilities — 5 reqs
4. Request Handling and Notification — 4 reqs
5. Evidence and Demonstrability — 3 reqs

Total: 12 requirements across 3 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 51-isms-core-privacy/00-checklist-engine/priv_checklist_engine.py
_PRIV_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(_PRIV_ROOT / '00-checklist-engine'))
from priv_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "PRIV-CHK-A.2.3.2"
CONTROL_ID = "A.2.3.2"
CONTROL_NAME = "PII Principal Obligations (Processor)"
SOURCE_POLICY = "PRIV-POL-A.2.3.2"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.2.3.2
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Rights Fulfilment Capabilities", [
        ("A.2.3.2-01", "Proactive Capability Obligation",
         "The organisation shall provide customers with the means to comply with their obligations to PII principals (data subjects). This obligation is proactive — the organisation has a duty to ensure the means are available regardless of whether the customer explicitly requests assistance."),
        ("A.2.3.2-02", "Access and Portability",
         "The organisation shall make available the capability to retrieve all PII held for a specific data subject in a structured, commonly used, and machine-readable format upon customer instruction, to support customer fulfilment of access and portability rights."),
        ("A.2.3.2-03", "Rectification and Erasure",
         "The organisation shall make available the capability to: update or correct PII for a specific data subject (rectification) upon customer instruction; and delete all PII for a specific data subject across all systems (including backups, within the agreed timeframe) upon customer instruction."),
        ("A.2.3.2-04", "Restriction and Objection",
         "The organisation shall make available the capability to: mark specific data subjects' PII as restricted, ensuring no further processing occurs (storage only), upon customer instruction; and cease processing specific data subjects' PII for specified purposes upon customer instruction."),
        ("A.2.3.2-05", "Capability Timeframes",
         "Rights fulfilment capabilities shall be available within the timeframe required for the customer to meet their regulatory obligations — typically within the applicable response window less reasonable lead time. Capability response times shall be defined in the processor agreement."),
    ]),

    ("Request Handling and Notification", [
        ("A.2.3.2-06", "Capability Documentation",
         "The means to fulfil data subject rights shall be documented in PRIV-IMP-A.2.3.2-TG, specifying how each capability is accessed and invoked by the customer. The documentation shall be kept current and made available to customers on request."),
        ("A.2.3.2-07", "Contractual Commitment",
         "Data subject rights assistance capabilities shall be maintained as a contractual commitment in processor agreements per PRIV-POL-A.2.2.2-7. The processor agreement shall specify response timeframes for each rights fulfilment type."),
        ("A.2.3.2-08", "Forwarding Direct Requests",
         "The organisation shall forward to the customer, without undue delay, any data subject rights requests received directly (e.g. a data subject contacting the organisation directly). The organisation shall not respond directly to data subject rights requests without explicit customer authorisation."),
        ("A.2.3.2-09", "Customer Request Log",
         "All customer instructions for data subject rights fulfilment shall be logged with: customer identity; request type; date received; fulfilment date; and outcome. The log shall be retained for 5 years."),
    ]),

    ("Evidence and Demonstrability", [
        ("A.2.3.2-10", "Technical Capability Evidence",
         "The organisation shall maintain technical documentation demonstrating that access, rectification, erasure, restriction, and objection capabilities are operational and tested. Documentation shall be current and reflect the actual state of capabilities."),
        ("A.2.3.2-11", "Agreement Clauses",
         "Processor agreements shall contain the Article 28(3)(e) assistance commitment. The DPO shall verify this commitment is present in all agreements before execution and flag any gaps for remediation."),
        ("A.2.3.2-12", "Capability Review",
         "Data subject rights fulfilment capabilities shall be reviewed and tested at minimum annually and whenever material changes are made to systems processing customer PII, to confirm capabilities remain operational and within required timeframes."),
    ]),
])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 27701:2025"
    ))


# =============================================================================
# QA_VERIFIED: 2026-03-10
# QA_STATUS: PASSED
# QA_TOOL: Claude Code Production Scripts QA Methodology
# CHANGES: Initial generation for Privacy product launch
# =============================================================================
