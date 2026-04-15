#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
AI-CHK-A.2.2-4 — AI Policy Framework Compliance Checklist

Controls A.2.2-4: Responsible AI Policy, Responsible AI Principles,
                  Processes for AI Policy
Product: ISMS CORE AI (ISO/IEC 42001:2023)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Responsible AI Policy (A.2.2) — 6 reqs
4. Responsible AI Principles (A.2.3) — 6 reqs
5. AI Policy Processes (A.2.4) — 5 reqs

Total: 17 requirements across 3 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

_AI_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_AI_ROOT / '00-checklist-engine'))
from ai_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID  = "AI-CHK-A.2.2-4"
CONTROL_ID   = "A.2.2-4"
CONTROL_NAME = "AI Policy Framework"
SOURCE_POLICY = "AI-POL-A.2.2-4"

# =============================================================================
# REQUIREMENTS — extracted from AI-POL-A.2.2-4
# =============================================================================
REQUIREMENTS = OrderedDict([
    ("Responsible AI Policy", [
        ("A.2.2-01", "Policy Establishment",
         "The organisation shall establish a policy for the responsible development and/or use of AI systems. The policy shall be approved by Executive Management and documented."),
        ("A.2.2-02", "Policy Scope",
         "The AI policy shall define the scope of AI systems covered and identify the organisational activities related to AI systems to which the policy applies."),
        ("A.2.2-03", "Policy Communication",
         "The AI policy shall be communicated to all persons within the organisation whose roles are relevant to AI systems, and made available to interested parties as appropriate."),
        ("A.2.2-04", "Policy Review",
         "The AI policy shall be reviewed at planned intervals and when significant changes occur to ensure its continuing suitability, adequacy, and effectiveness."),
        ("A.2.2-05", "Policy Alignment",
         "The AI policy shall be consistent with applicable laws and regulations and aligned with [Organisation]'s overall information security and data protection policies."),
        ("A.2.2-06", "Policy Authority",
         "The AI policy shall establish clear authority and accountability for AI governance, naming the AI Governance Officer role as responsible for the AIMS."),
    ]),

    ("Responsible AI Principles", [
        ("A.2.3-01", "Principles Establishment",
         "The organisation shall establish and document principles for the responsible development and use of AI systems. Principles shall be approved by Executive Management."),
        ("A.2.3-02", "Human Agency and Oversight",
         "The responsible AI principles shall include a commitment to human agency and oversight — AI systems shall be designed to support human decision-making with meaningful human review for consequential outputs."),
        ("A.2.3-03", "Fairness and Non-Discrimination",
         "The responsible AI principles shall include a commitment to fairness — AI systems shall be assessed for potential bias and discriminatory impact before deployment and in operation."),
        ("A.2.3-04", "Privacy by Design",
         "The responsible AI principles shall include a commitment to privacy — personal data in AI systems shall be governed by documented legal bases and minimisation requirements."),
        ("A.2.3-05", "Robustness and Safety",
         "The responsible AI principles shall include a commitment to robustness, security, and safety — AI systems shall undergo validation before deployment and be monitored in operation."),
        ("A.2.3-06", "Accountability and Transparency",
         "The responsible AI principles shall include a commitment to accountability and transparency — every AI system shall have a named owner accountable for its compliance, and transparency shall be provided to users and affected individuals."),
    ]),

    ("AI Policy Processes", [
        ("A.2.4-01", "Policy Integration",
         "The organisation shall implement processes to ensure that AI policy requirements are integrated into the AI system lifecycle — from specification through deployment and operation."),
        ("A.2.4-02", "Compliance Monitoring",
         "The organisation shall implement a process to monitor compliance with the AI policy. Non-compliance shall be escalated and addressed per defined escalation paths."),
        ("A.2.4-03", "Policy Hierarchy",
         "The organisation shall maintain a documented AI policy hierarchy (foundation policies → control-specific policies → implementation guides) ensuring that lower-tier documents do not contradict higher-tier requirements."),
        ("A.2.4-04", "Awareness and Training",
         "The organisation shall ensure that persons with AI-related roles receive training on the AI policy and relevant responsible AI requirements appropriate to their role."),
        ("A.2.4-05", "Effectiveness Measurement",
         "The organisation shall define and measure indicators of AI policy effectiveness, reporting results to Executive Management at least annually via the AIMS management review."),
    ]),
])


# =============================================================================
# MAIN
# =============================================================================
if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 42001:2023"
    ))


# =============================================================================
# QA_VERIFIED: [YYYY-MM-DD]
# =============================================================================
