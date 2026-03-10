#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.2.5.2-6 — Transfer and Disclosure (Processor) Compliance Checklist

Controls A.2.5.2-6: Informing Customers of Transfer Basis, Transfer Destinations,
                     Disclosure Records, Disclosure Request Notification,
                     Legally Binding Disclosures
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Processor Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Transfer Basis Notification (A.2.5.2) — 4 reqs
4. Transfer Destinations (A.2.5.3) — 3 reqs
5. Disclosure Records (A.2.5.4) — 3 reqs
6. Disclosure Request Handling (A.2.5.5-6) — 5 reqs

Total: 15 requirements across 4 domains
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
DOCUMENT_ID = "PRIV-CHK-A.2.5.2-6"
CONTROL_ID = "A.2.5.2-6"
CONTROL_NAME = "Transfer and Disclosure (Processor)"
SOURCE_POLICY = "PRIV-POL-A.2.5.2-6"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.2.5.2-6
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Transfer Basis Notification", [
        ("A.2.5.2-01", "Customer Notification",
         "The organisation shall inform each customer in a timely manner of the legal basis for any PII transfers between jurisdictions carried out on their behalf. The transfer basis (adequacy, SCCs, BCRs) for each transfer destination shall be documented and provided in the processor agreement or associated data processing schedule."),
        ("A.2.5.2-02", "Change Notification",
         "Where the organisation intends to change a transfer basis or add a new transfer destination, customers shall be notified in advance with sufficient time to object or terminate the contract. The notification period shall be as specified in the processor agreement (typically minimum 30 days for non-urgent changes)."),
        ("A.2.5.2-03", "Change Notification Records",
         "Records of customer notifications for transfer basis changes shall be maintained for 3 years, including the nature of the change, date of notification, and customer response (objection or no-objection)."),
        ("A.2.5.2-04", "Objection Handling",
         "Where a customer objects to a proposed transfer basis change or new destination, the organisation shall have a documented process for handling objections, including implementing alternative measures or allowing termination without penalty."),
    ]),

    ("Transfer Destinations", [
        ("A.2.5.3-01", "Transfer Destination Register",
         "The DPO shall maintain a Transfer Destination Register listing all countries and international organisations to which customer PII may be transferred in the course of service delivery, including transfer mechanism, legal basis, and applicable PII categories."),
        ("A.2.5.3-02", "Customer Availability",
         "The Transfer Destination Register shall be made available to customers in the processor agreement or data processing schedule. Updates to the register require customer notification per A.2.5.2."),
        ("A.2.5.3-03", "Register Currency",
         "The Transfer Destination Register shall be updated when new sub-processors or infrastructure require new transfer destinations, when adequacy status changes, and at minimum annually. Customers shall be notified of changes that affect their processing."),
    ]),

    ("Disclosure Records", [
        ("A.2.5.4-01", "Processor Disclosure Register",
         "The organisation shall maintain a Processor Disclosure Register logging each disclosure of customer PII to third parties: date, third party identity, PII categories disclosed, and basis (customer instruction, legal obligation, or contractual obligation). Records shall be retained for minimum 3 years."),
        ("A.2.5.4-02", "Customer Availability",
         "Disclosure records shall be made available to customers upon request to support customer demonstrability obligations and data subject access requests (which require identification of PII recipients)."),
        ("A.2.5.4-03", "Sub-processor Disclosures",
         "Disclosures to sub-processors shall be documented separately per PRIV-POL-A.2.5.7-9 (Sub-processor Register). Sub-processor disclosures are covered by the customer's general sub-processor authorisation."),
    ]),

    ("Disclosure Request Handling", [
        ("A.2.5.5-01", "Legally Binding Request Notification",
         "When the organisation receives a legally binding request for disclosure of customer PII (from law enforcement, court, regulator, or tax authority), it shall notify the customer without undue delay, unless prohibited by law. Notification shall include the nature of the request, PII categories requested, and legal authority cited — to the extent legally permissible."),
        ("A.2.5.5-02", "Notification Prohibition Handling",
         "Where notification to the customer is legally prohibited (e.g. by a non-disclosure order), the organisation shall document this constraint, seek legal advice on challenging the prohibition, and notify the customer as soon as the prohibition is lifted."),
        ("A.2.5.6-01", "Non-Legally-Binding Request Refusal",
         "The organisation shall reject any requests for disclosure of customer PII that are not legally binding. If uncertain whether a request is legally binding, legal advice shall be sought before responding. Refusals shall be documented."),
        ("A.2.5.6-02", "Legally Binding Disclosure Process",
         "The organisation shall consult with the customer before making any disclosure pursuant to a legally binding request — except where law prohibits notification. Where disclosure proceeds, it shall be limited to the minimum PII necessary to comply with the legal obligation. The disclosure shall be documented in the Processor Disclosure Register."),
        ("A.2.5.6-03", "Contractually Authorised Disclosures",
         "The organisation may accept and act upon contractually agreed requests for PII disclosures explicitly authorised by the customer (e.g. reporting to specified regulators, sharing with auditors under customer instruction). All such disclosures shall be recorded."),
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
