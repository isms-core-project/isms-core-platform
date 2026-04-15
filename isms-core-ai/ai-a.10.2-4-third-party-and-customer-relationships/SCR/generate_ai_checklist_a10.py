#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
AI-CHK-A.10.2-4 — Third-Party and Customer Relationships Compliance Checklist

Controls A.10.2-4: Responsibility Allocation, AI Suppliers,
                   Customer and Deployer Obligations
Product: ISMS CORE AI (ISO/IEC 42001:2023)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Responsibility Allocation (A.10.2) — 6 reqs
4. AI Suppliers (A.10.3) — 6 reqs
5. Customer and Deployer Obligations (A.10.4) — 5 reqs

Total: 17 requirements across 3 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

_AI_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_AI_ROOT / '00-checklist-engine'))
from ai_checklist_engine import generate_checklist

DOCUMENT_ID   = "AI-CHK-A.10.2-4"
CONTROL_ID    = "A.10.2-4"
CONTROL_NAME  = "Third-Party and Customer Relationships"
SOURCE_POLICY = "AI-POL-A.10.2-4"

REQUIREMENTS = OrderedDict([
    ("Responsibility Allocation", [
        ("A.10.2-01", "Responsibility Matrix",
         "For each AI system involving third-party AI components or deployed to customers, the organisation shall complete a Third-Party Responsibility Matrix per the template in AI-IMP-A.10.2-4-TG, allocating responsibility for all nine AI governance domains across all parties."),
        ("A.10.2-02", "EU AI Act Role Determination",
         "The organisation shall determine and document its EU AI Act role for each in-scope AI system: Provider, Deployer, Distributor, or combination. Role determination shall be reviewed whenever the supply chain or deployment arrangement changes."),
        ("A.10.2-03", "Provider Obligations",
         "Where the organisation acts as an AI Provider (placing an AI system on the market or putting it into service), it shall fulfil all EU AI Act Article 16 provider obligations applicable to the system's risk classification. Obligations shall be documented and monitored."),
        ("A.10.2-04", "Deployer Obligations",
         "Where the organisation acts as an AI Deployer (using an AI system provided by a third party), it shall fulfil all EU AI Act Article 26 deployer obligations — including AISIA, human oversight, operator training, and serious incident reporting."),
        ("A.10.2-05", "Contractual Responsibility",
         "Responsibility allocations documented in the Third-Party Responsibility Matrix shall be reflected in contracts with third-party AI providers and customers. Contracts shall clearly assign each party's obligations and shall not leave responsibility gaps."),
        ("A.10.2-06", "Responsibility Review",
         "The Third-Party Responsibility Matrix shall be reviewed annually and whenever a supply chain change, significant system update, or regulatory change could affect responsibility allocation. Review outcomes shall be documented."),
    ]),

    ("AI Suppliers", [
        ("A.10.3-01", "Supplier Pre-Procurement Assessment",
         "Before procuring an AI system or AI component from a third party, the organisation shall complete a Supplier Pre-Procurement Assessment per the template in AI-IMP-A.10.2-4-TG. No AI supplier shall be engaged without a completed assessment on file."),
        ("A.10.3-02", "Assessment Dimensions",
         "The supplier pre-procurement assessment shall evaluate the supplier across eight dimensions: responsible AI practices, EU AI Act compliance, data governance, information security, incident response, financial and operational resilience, sub-supplier management, and overall assessment outcome."),
        ("A.10.3-03", "Contractual Minimums",
         "Contracts with AI suppliers shall include minimum contractual provisions covering: incident notification obligations, audit rights, data processing terms, AI system change notification, and compliance with applicable AI regulation. Contracts without these provisions shall not be executed without AI Governance Officer approval."),
        ("A.10.3-04", "Supplier Monitoring",
         "The AI Governance Officer shall maintain an AI Supplier Monitoring Register. Registered suppliers shall be monitored against defined KPIs on a schedule proportionate to risk. Monitoring results shall be reviewed at AI governance meetings."),
        ("A.10.3-05", "Supplier Incident Notification",
         "AI supplier contracts shall require the supplier to notify the organisation within a defined timeframe of any incident affecting the AI system or service that could materially affect the organisation's compliance or the system's performance."),
        ("A.10.3-06", "Supplier Concentration Risk",
         "The AI Governance Officer shall assess and document concentration risk from single-vendor dependencies in critical AI systems. Systems with critical third-party AI API dependencies shall have documented contingency plans referenced in business continuity planning."),
    ]),

    ("Customer and Deployer Obligations", [
        ("A.10.4-01", "Customer Information",
         "Where the organisation provides AI systems to customers or deployers, it shall provide all information required for the customer to fulfil their deployer obligations under applicable regulation. The AI Customer Information Register shall track what information has been provided to each customer."),
        ("A.10.4-02", "Required Customer Information",
         "Information provided to AI customers shall include at minimum: system description and intended use, known limitations, human oversight requirements, operator training requirements, incident reporting obligations, and the organisation's contact for AI governance enquiries."),
        ("A.10.4-03", "Deployer Compliance Monitoring",
         "The organisation shall implement a process to monitor whether customers are using the AI system within its intended use scope and in compliance with contractual terms. Material non-compliance shall be escalated and remediated."),
        ("A.10.4-04", "Customer Contract Provisions",
         "Contracts with customers who use or deploy the organisation's AI systems shall include: use restriction clauses, human oversight requirements, incident notification obligations, and prohibition on uses that would engage the organisation's regulatory obligations."),
        ("A.10.4-05", "EU AI Act Article 25 Multi-Party Obligations",
         "Where the supply chain involves multiple parties each contributing to an AI system, the organisation shall document compliance with EU AI Act Article 25 obligations — confirming which obligations are fulfilled by each party and that no obligations are left unassigned."),
    ]),
])

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 42001:2023"
    ))

# QA_VERIFIED: [YYYY-MM-DD]
