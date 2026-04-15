#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
AI-CHK-A.8.2-5 — Information for Interested Parties Compliance Checklist

Controls A.8.2-5: User Documentation, Transparency to Affected Parties,
                  External Reporting, Incident Communication
Product: ISMS CORE AI (ISO/IEC 42001:2023)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. User Documentation (A.8.2) — 5 reqs
4. Transparency to Affected Parties (A.8.3) — 5 reqs
5. External Reporting (A.8.4) — 4 reqs
6. Incident Communication (A.8.5) — 4 reqs

Total: 18 requirements across 4 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

_AI_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_AI_ROOT / '00-checklist-engine'))
from ai_checklist_engine import generate_checklist

DOCUMENT_ID   = "AI-CHK-A.8.2-5"
CONTROL_ID    = "A.8.2-5"
CONTROL_NAME  = "Information for Interested Parties"
SOURCE_POLICY = "AI-POL-A.8.2-5"

REQUIREMENTS = OrderedDict([
    ("User Documentation", [
        ("A.8.2-01", "User Documentation Existence",
         "Every in-scope AI system made available to users shall have current user documentation per the template in AI-IMP-A.8.2-5-TG. Documentation shall be available before or at the point of system access, not retrospectively."),
        ("A.8.2-02", "Required Documentation Content",
         "User documentation shall include at minimum: system description and purpose; intended use and use restrictions; inputs required and outputs produced; human oversight and override instructions; known limitations; support and escalation contacts."),
        ("A.8.2-03", "Accuracy of Claimed Capabilities",
         "User documentation shall accurately represent the AI system's capabilities and limitations. Claims of accuracy, reliability, or fairness shall be supported by V&V evidence. No documentation shall overstate system capabilities."),
        ("A.8.2-04", "Documentation Accessibility",
         "User documentation shall be written in plain language accessible to the intended audience. Where the AI system is deployed in multiple languages, documentation shall be available in all languages supported by the system."),
        ("A.8.2-05", "Documentation Currency",
         "User documentation shall be updated whenever a material change is made to the AI system. Outdated documentation shall not remain current. The AI System Owner is responsible for documentation currency."),
    ]),

    ("Transparency to Affected Parties", [
        ("A.8.3-01", "AI Disclosure to Users",
         "The organisation shall disclose to users that they are interacting with an AI system, unless the context makes this self-evident. Disclosure shall be clear, prominent, and provided before the first substantive AI interaction."),
        ("A.8.3-02", "Transparency Notice",
         "For AI systems that process personal data or make or support consequential decisions affecting individuals, the organisation shall publish a Transparency Notice per the template in AI-IMP-A.8.2-5-TG covering: AI system identity, purpose, data used, and recourse options."),
        ("A.8.3-03", "Recourse Information",
         "Where an AI system produces outputs that affect individuals' rights or interests, the organisation shall provide information on how affected individuals can seek human review, raise objections, or access support."),
        ("A.8.3-04", "EU AI Act Article 50 Compliance",
         "For AI systems in scope of EU AI Act Article 50 transparency requirements (deepfakes, emotion recognition, biometric categorisation, chatbots), the organisation shall implement the applicable disclosure obligations and document compliance."),
        ("A.8.3-05", "Transparency Register",
         "The AI Governance Officer shall maintain an Interested Party Information Register tracking what information has been provided to which categories of interested party, through which channels, and when."),
    ]),

    ("External Reporting", [
        ("A.8.4-01", "Regulatory Reporting Obligations",
         "The organisation shall identify all regulatory reporting obligations applicable to its AI systems — including EU AI Act Article 73 serious incident reporting, national AI regulatory requirements, and sector-specific obligations. Obligations shall be documented."),
        ("A.8.4-02", "Serious Incident Definition",
         "The organisation shall define what constitutes a serious incident for reporting purposes, aligned with EU AI Act Article 3(49) definition: risk to health/safety, fundamental rights violation, or significant disruption to critical services."),
        ("A.8.4-03", "External Reporting Process",
         "The organisation shall implement a documented process for external incident reporting, covering: detection and classification, decision on reportability, notification to regulatory authority within required timeframe, and documentation of report and response."),
        ("A.8.4-04", "Market Surveillance Cooperation",
         "The organisation shall implement a process for cooperating with market surveillance authorities — providing information, access, and documentation on request within required timeframes. The process shall be owned by the AI Governance Officer with Legal involvement."),
    ]),

    ("Incident Communication", [
        ("A.8.5-01", "Internal Incident Communication",
         "When an AI incident is declared, the AI System Owner shall notify the AI Governance Officer within 24 hours. Notification shall include: system affected, nature of incident, initial impact assessment, and immediate containment actions taken."),
        ("A.8.5-02", "Affected Party Notification",
         "Where an AI incident directly affects individuals' rights or interests, the organisation shall notify affected parties of the incident, the impact on them, and the remediation actions taken, within a timeframe proportionate to severity."),
        ("A.8.5-03", "Notification Template",
         "External incident notifications shall use the template in AI-IMP-A.8.2-5-TG. Notifications shall be reviewed by Legal before transmission to regulatory authorities or large-scale affected populations."),
        ("A.8.5-04", "Communication Record",
         "All incident communications — internal notifications, external reports, and affected party notifications — shall be logged in the AI Incident Register with timestamps, recipients, and content. Communication records shall be retained for a minimum of 5 years."),
    ]),
])

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 42001:2023"
    ))

# QA_VERIFIED: [YYYY-MM-DD]
