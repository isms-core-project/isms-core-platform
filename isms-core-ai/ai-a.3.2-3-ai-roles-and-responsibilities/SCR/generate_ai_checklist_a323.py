#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
AI-CHK-A.3.2-3 — AI Roles and Responsibilities Compliance Checklist

Controls A.3.2-3: AI Governance Roles, Concerns Reporting Channel
Product: ISMS CORE AI (ISO/IEC 42001:2023)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. AI Governance Roles (A.3.2) — 7 reqs
4. Concerns Reporting Channel (A.3.3) — 5 reqs

Total: 12 requirements across 2 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

_AI_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_AI_ROOT / '00-checklist-engine'))
from ai_checklist_engine import generate_checklist

DOCUMENT_ID   = "AI-CHK-A.3.2-3"
CONTROL_ID    = "A.3.2-3"
CONTROL_NAME  = "AI Roles and Responsibilities"
SOURCE_POLICY = "AI-POL-A.3.2-3"

REQUIREMENTS = OrderedDict([
    ("AI Governance Roles", [
        ("A.3.2-01", "Role Assignment",
         "The organisation shall assign and document AI governance roles and responsibilities. All named roles shall be held by identified individuals with formal appointments."),
        ("A.3.2-02", "AI Governance Officer",
         "The organisation shall designate an AI Governance Officer responsible for owning the AIMS policy suite, approving AISIAs, and overseeing AI governance reviews. This role shall be named and current at all times."),
        ("A.3.2-03", "AI Risk Owner",
         "For each in-scope AI system, the organisation shall designate an AI Risk Owner who is accountable for the risk profile of the system and who accepts residual impact classifications from AISIAs."),
        ("A.3.2-04", "AI System Owner",
         "Every in-scope AI system shall have exactly one named AI System Owner who is responsible for maintaining AISIA currency, monitoring system performance, managing incidents, and maintaining user documentation for that system."),
        ("A.3.2-05", "Role Continuity",
         "The organisation shall ensure continuity of all AI governance roles — no in-scope AI system shall be without a named AI System Owner at any time. Role transitions shall follow a documented handover process."),
        ("A.3.2-06", "Competency Requirements",
         "The organisation shall define and document competency requirements for each AI governance role and ensure that role holders meet those requirements through training or experience."),
        ("A.3.2-07", "Role Register",
         "The organisation shall maintain an AI Role Assignment Register documenting all current AI governance role holders, assigned AI systems, training status, and contact information."),
    ]),

    ("Concerns Reporting Channel", [
        ("A.3.3-01", "Channel Establishment",
         "The organisation shall establish and maintain a channel through which any person can report concerns about AI systems, including unexpected behaviour, potential misuse, discriminatory outputs, and safety concerns."),
        ("A.3.3-02", "Channel Accessibility",
         "The AI concerns reporting channel shall be accessible to all staff who use or are affected by AI systems, with clear guidance on how to use it and what types of concerns to raise."),
        ("A.3.3-03", "Non-Retaliation",
         "The organisation shall implement and communicate a non-retaliation policy: persons who raise AI concerns in good faith shall not face negative consequences. This protection applies to both internal reports and reports to regulatory authorities."),
        ("A.3.3-04", "Concern Handling",
         "Concerns raised through the channel shall be logged, acknowledged within a defined timeframe, investigated, and responded to. The AI Governance Officer shall oversee concern handling and maintain a concerns register."),
        ("A.3.3-05", "Awareness of Channel",
         "All staff who use AI systems shall be informed of the concerns reporting channel as part of their AI system training and in accessible AI governance communications."),
    ]),
])

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 42001:2023"
    ))

# QA_VERIFIED: [YYYY-MM-DD]
