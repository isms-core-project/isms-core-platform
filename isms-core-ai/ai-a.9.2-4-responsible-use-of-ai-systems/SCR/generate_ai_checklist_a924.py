#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
AI-CHK-A.9.2-4 — Responsible Use of AI Systems Compliance Checklist

Controls A.9.2-4: Responsible Use Processes, Responsible Use Objectives,
                  Intended Use Compliance
Product: ISMS CORE AI (ISO/IEC 42001:2023)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Responsible Use Processes (A.9.2) — 6 reqs
4. Responsible Use Objectives (A.9.3) — 5 reqs
5. Intended Use Compliance (A.9.4) — 5 reqs

Total: 16 requirements across 3 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

_AI_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_AI_ROOT / '00-checklist-engine'))
from ai_checklist_engine import generate_checklist

DOCUMENT_ID   = "AI-CHK-A.9.2-4"
CONTROL_ID    = "A.9.2-4"
CONTROL_NAME  = "Responsible Use of AI Systems"
SOURCE_POLICY = "AI-POL-A.9.2-4"

REQUIREMENTS = OrderedDict([
    ("Responsible Use Processes", [
        ("A.9.2-01", "Responsible Use Framework",
         "The organisation shall establish and implement a responsible use framework for AI systems in operation. The framework shall define: what constitutes responsible use, the obligations on operators, the process for escalating concerns, and consequences of misuse."),
        ("A.9.2-02", "Pre-Use Verification",
         "Before deploying an AI system to a new operational context or user population, the AI System Owner shall complete a pre-use verification confirming: intended use alignment, operator training, human oversight in place, and monitoring active."),
        ("A.9.2-03", "Misuse Detection",
         "The AI System Owner shall implement controls to detect when an AI system is being used outside its intended use scope — including monitoring of use patterns, user queries, and downstream decisions. Detected misuse shall be escalated."),
        ("A.9.2-04", "Misuse Response",
         "The organisation shall implement a documented misuse response process covering: initial containment, impact assessment, affected party notification if applicable, root cause analysis, and remediation. Response shall be proportionate to misuse severity."),
        ("A.9.2-05", "Serious Misuse Escalation",
         "Misuse that results in harm to individuals, breach of applicable law, or reputational risk shall be escalated to the AI Governance Officer and Legal within 24 hours. Where EU AI Act serious incident thresholds are met, regulatory reporting obligations shall be assessed."),
        ("A.9.2-06", "Misuse Register",
         "The AI Governance Officer shall maintain a Misuse Event Register. Misuse events shall be recorded, reviewed at AI governance meetings, and used to improve use controls, training, and system design as appropriate."),
    ]),

    ("Responsible Use Objectives", [
        ("A.9.3-01", "Responsible Use Record",
         "For each AI system, the AI System Owner shall maintain a Responsible Use Record per the template in AI-IMP-A.9.2-4-TG, documenting how the six responsible use properties (human agency, fairness, privacy, reliability, safety, accountability) are operationalised in practice."),
        ("A.9.3-02", "Human Agency in Practice",
         "The AI System Owner shall document and maintain the mechanism through which human agency is preserved in practice — including how operators can override or escalate AI outputs, and how affected individuals can seek human review."),
        ("A.9.3-03", "Fairness in Operation",
         "The AI System Owner shall implement operational fairness monitoring — tracking whether AI outputs show disparate impact across protected groups in operation, not only at V&V. Monitoring results shall be reviewed at minimum annually."),
        ("A.9.3-04", "Safety and Reliability",
         "The AI System Owner shall define operational safety thresholds — the performance levels below which the system shall be suspended or require human review of all outputs — and shall monitor against these thresholds."),
        ("A.9.3-05", "Accountability Trail",
         "The organisation shall maintain an accountability trail for consequential AI-assisted decisions — recording the AI output, the human decision made, and the identity of the human decision-maker. The trail shall be auditable and retained per the impact classification retention schedule."),
    ]),

    ("Intended Use Compliance", [
        ("A.9.4-01", "Intended Use Specification",
         "Every in-scope AI system shall have a documented Intended Use Specification per the template in AI-IMP-A.9.2-4-TG, defining: permitted use cases, geographic scope, user roles, input types, output interpretation guidance, and explicitly prohibited uses."),
        ("A.9.4-02", "Use Restriction Communication",
         "Use restrictions from the Intended Use Specification shall be communicated to all AI system operators before first use, and reinforced through user documentation and system interface notices where technically feasible."),
        ("A.9.4-03", "Scope Creep Prevention",
         "The AI System Owner shall implement a process to identify and respond to scope creep — the gradual expansion of an AI system's use beyond its intended scope. Scope creep shall be treated as a proposed material change requiring AISIA update and re-validation."),
        ("A.9.4-04", "High-Risk Use Prohibition",
         "The organisation shall maintain a list of use cases for which AI system use is prohibited or requires specific additional controls — including uses that would constitute prohibited practices under EU AI Act Article 5. This list shall be communicated to all relevant staff."),
        ("A.9.4-05", "Intended Use Review",
         "The Intended Use Specification shall be reviewed when: the system's operational context changes materially; new user populations are onboarded; or the AISIA is updated. Reviews shall be documented with outcome and approval record."),
    ]),
])

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 42001:2023"
    ))

# QA_VERIFIED: [YYYY-MM-DD]
