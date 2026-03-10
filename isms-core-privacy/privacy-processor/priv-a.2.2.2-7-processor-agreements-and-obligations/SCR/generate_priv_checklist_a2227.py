#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.2.2.2-7 — Processor Agreements and Obligations Compliance Checklist

Controls A.2.2.2-7: Customer Agreement, Processing on Instructions, Marketing
                     Prohibition, Infringing Instruction, Customer Compliance
                     Support, Processor Records
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Processor Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Customer Agreement Content (A.2.2.2) — 4 reqs
4. Processing on Instructions (A.2.2.3) — 4 reqs
5. Marketing and Advertising (A.2.2.4) — 3 reqs
6. Infringing Instructions (A.2.2.5) — 4 reqs
7. Customer Compliance Support (A.2.2.6) — 3 reqs
8. Processor Records (A.2.2.7) — 4 reqs

Total: 22 requirements across 6 domains
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
DOCUMENT_ID = "PRIV-CHK-A.2.2.2-7"
CONTROL_ID = "A.2.2.2-7"
CONTROL_NAME = "Processor Agreements and Obligations"
SOURCE_POLICY = "PRIV-POL-A.2.2.2-7"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.2.2.2-7
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Customer Agreement Content", [
        ("A.2.2.2-01", "Agreement Content Review",
         "All processor agreements (where the organisation acts as processor) shall be reviewed by the DPO before execution to confirm that obligations relating to assisting with the customer's data protection duties are adequately addressed, taking into account the nature of processing."),
        ("A.2.2.2-02", "Assistance Obligations",
         "Processor agreements shall address the organisation's role in: implementing appropriate security measures (Article 32); assisting with data subject rights obligations; assisting with security, breach notification, DPIA, and prior consultation; providing information for customer compliance demonstration; and cooperating with customer or supervisory authority audits."),
        ("A.2.2.2-03", "Return or Deletion at End",
         "Processor agreements shall include the obligation to return or delete all customer PII upon service termination, per PRIV-POL-A.2.4.2-4. The default action (return or deletion) shall be specified in the agreement."),
        ("A.2.2.2-04", "Processor Agreement Register",
         "The DPO shall maintain a Processor Agreement Register listing all active customer processor agreements with status, review date, and customer contact. No new processor engagement commences without a register entry."),
    ]),

    ("Processing on Instructions", [
        ("A.2.2.3-01", "Instruction-Only Processing",
         "PII processed on behalf of customers shall be processed only for the purposes expressed in the customer's documented instructions. Processing for the organisation's own purposes is prohibited unless explicitly authorised by the customer in writing."),
        ("A.2.2.3-02", "Instruction Traceability",
         "All processing operations applied to customer PII must be traceable to a customer instruction (contract, SLA, or written instruction). Processing operations without a traceable instruction shall not commence."),
        ("A.2.2.3-03", "Personnel Instruction Compliance",
         "All personnel processing customer PII shall understand and be able to demonstrate that they are acting on customer instructions only. Unauthorised use of customer PII for internal purposes shall be treated as a security incident."),
        ("A.2.2.3-04", "Escalation Requirement",
         "Where personnel seek to use customer PII for a purpose not covered by the contract, they shall escalate to the DPO for assessment before proceeding. The DPO assessment and outcome shall be documented."),
    ]),

    ("Marketing and Advertising", [
        ("A.2.2.4-01", "Marketing Prohibition",
         "The organisation shall not use PII processed under a customer contract for marketing or advertising purposes (the organisation's own marketing to the customer's data subjects) unless prior consent from the PII principal has been separately obtained."),
        ("A.2.2.4-02", "Consent Requirements",
         "Marketing consent from PII principals shall be separately obtained and not bundled with the service agreement. Providing consent for marketing shall not be a condition of receiving the service."),
        ("A.2.2.4-03", "Consent Records",
         "The organisation shall maintain records of any marketing consent obtained from data subjects in the context of processor activities and shall not send marketing to individuals who have not consented."),
    ]),

    ("Infringing Instructions", [
        ("A.2.2.5-01", "Notification Obligation",
         "If the organisation considers that a customer's processing instruction infringes applicable legal requirements (GDPR, CH FADP, or other applicable law), the organisation shall inform the customer in writing without undue delay."),
        ("A.2.2.5-02", "Escalation Process",
         "Processing personnel who identify a potentially infringing instruction shall escalate to the DPO immediately. The DPO shall assess the instruction (with Legal/Compliance input where uncertain), document the assessment, and communicate the concern to the customer in writing."),
        ("A.2.2.5-03", "Non-Execution Pending Resolution",
         "The organisation shall not execute an instruction identified as potentially infringing pending resolution with the customer. If the customer insists on proceeding after notification, the organisation shall document its position and may exercise its contractual right to suspend or terminate the engagement."),
        ("A.2.2.5-04", "Infringing Instruction Register",
         "All infringing instruction notifications and customer responses shall be documented in the Infringing Instruction Register and retained for 5 years."),
    ]),

    ("Customer Compliance Support", [
        ("A.2.2.6-01", "Compliance Information Provision",
         "The organisation shall provide customers with the information necessary to enable them to demonstrate compliance with their obligations as PII Controller. This includes: security documentation (certificates, audit reports, SOC 2); sub-processor lists; and evidence of implemented security measures."),
        ("A.2.2.6-02", "Audit Cooperation",
         "The organisation shall cooperate with customer audits and supervisory authority inspections relating to the processing of customer PII, as required by GDPR Article 28(3)(h). The scope and conditions of such cooperation shall be defined in the processor agreement."),
        ("A.2.2.6-03", "Customer Compliance Support Register",
         "The DPO shall maintain a Customer Compliance Support Register tracking what security and compliance documentation has been provided to each customer and when."),
    ]),

    ("Processor Records", [
        ("A.2.2.7-01", "Processor RoPA",
         "The organisation shall maintain a processor-side Record of Processing Activities (RoPA) per GDPR Article 30(2), including for each customer processing activity: name and contact details of the processor and DPO; categories of processing carried out per customer; transfers to third countries and safeguards; and general description of security measures."),
        ("A.2.2.7-02", "Supporting Registers",
         "In addition to the processor RoPA, the organisation shall maintain: Processor Agreement Register; Sub-processor Register; Infringing Instruction Register; and Customer Compliance Support Register."),
        ("A.2.2.7-03", "Record Availability",
         "Processor records shall be maintained in a secure manner and made available to supervisory authorities on request within the timeframe required by applicable law."),
        ("A.2.2.7-04", "Record Review",
         "Processor records shall be reviewed and updated at minimum annually, when new customer engagements commence, when processing activities change materially, and when engagements end."),
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
