#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.6.3 — Information Security Awareness and Training Compliance Checklist

Control A.6.3: Information Security Awareness and Training
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Awareness & Training Programme (1 reqs)
4. Training Topics (1 reqs)
5. Training Schedule (5 reqs)
6. Phishing Simulation Programme (7 reqs)
7. Assessment and Acknowledgement (4 reqs)
8. Training Records (3 reqs)
9. Training Content Updates (2 reqs)
10. Training Effectiveness Metrics (1 reqs)
11. Language and Accessibility (4 reqs)

Total: 28 requirements across 9 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/A.0-checklist-engine/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(_OP_ROOT / 'A.0-checklist-engine'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.6.3"
CONTROL_ID = "A.6.3"
CONTROL_NAME = "Information Security Awareness and Training"
SOURCE_POLICY = "ISMS-OP-POL-A.6.3"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.6.3
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Awareness & Training Programme", [
        ("A.6.3-01", "Executive Management",
         "Executive management shall visibly support and promote the information security awareness and training programme. This includes endorsing training requirements, allocating resources, and setting the expectation that all personnel complete required training."),
    ]),

    ("Training Topics", [
        ("A.6.3-02", "The Following Topics",
         "The following topics shall be covered in baseline security awareness training:."),
    ]),

    ("Training Schedule", [
        ("A.6.3-03", "Information Security Awareness Training",
         "Information security awareness training shall be provided to new starters before they are granted access to systems that process, store, or transmit confidential or personal data. Training shall be completed within 5 business days of the start date."),
        ("A.6.3-04", "The Information Security Policy And",
         "The information security policy and acceptable use policy shall be provided to new starters as part of the onboarding process. Acknowledgement of these policies shall be obtained before system access is granted."),
        ("A.6.3-05", "General Information Security Awareness",
         "General information security awareness training shall be conducted for all employees at least annually. Training shall be refreshed to reflect current threats, policy changes, and lessons learned from incidents."),
        ("A.6.3-06", "Information Security Awareness",
         "Information security awareness shall be reinforced throughout the year using a variety of methods:."),
        ("A.6.3-07", "Additional Training",
         "When an employee's role changes significantly or their access to data types changes, additional training shall be provided appropriate to the new role and its associated risks."),
    ]),

    ("Phishing Simulation Programme", [
        ("A.6.3-08", "Conduct A Phishing Simulation Programme",
         "The organisation shall conduct a phishing simulation programme to assess and improve employee resilience to social engineering attacks."),
        ("A.6.3-09", "Use Realistic, Work-Relevant Scenarios",
         "Simulations shall use realistic, work-relevant scenarios (e.g., delivery notifications, meeting invitations, password reset requests) — not deceptive or humiliating content."),
        ("A.6.3-10", "Employees Who Interact With Simulated",
         "Employees who interact with simulated phishing shall receive immediate feedback explaining what was suspicious and how to recognise similar attacks."),
        ("A.6.3-11", "The Programme Is Educational, Not",
         "The programme is educational, not punitive. Simulation results shall be used to identify training needs, not for disciplinary action."),
        ("A.6.3-12", "Employees Who Report Simulated Phishing",
         "Employees who report simulated phishing shall be positively recognised."),
        ("A.6.3-13", "Simulation Difficulty",
         "Simulation difficulty shall be gradually increased over time."),
        ("A.6.3-14", "A Single, Standardised Method For",
         "A single, standardised method for reporting suspected phishing shall be provided to all employees (e.g., a 'Report Phishing' button in the email client). Employees shall be trained to use this reporting mechanism."),
    ]),

    ("Assessment and Acknowledgement", [
        ("A.6.3-15", "Be Assessed On Their Understanding Of",
         "Employees shall be assessed on their understanding of information security at the completion of awareness training. Assessment may include quizzes, scenario-based questions, or practical exercises."),
        ("A.6.3-16", "The Minimum Passing Score For All",
         "The minimum passing score for all assessments shall be 80%. Employees who do not achieve the passing score shall be required to repeat the training within 10 business days. Two consecutive failures shall be escalated to the employee's line manager for additional support."),
        ("A.6.3-17", "Formally Acknowledge That They Have",
         "All employees shall formally acknowledge that they have received training and understand their information security responsibilities. Acknowledgement shall be recorded and retained."),
        ("A.6.3-18", "New Starters",
         "New starters shall acknowledge the information security policy and acceptable use policy during onboarding before system access is granted."),
    ]),

    ("Training Records", [
        ("A.6.3-19", "A Register Of Information Security",
         "A register of information security training and competency shall be maintained for all employees. The register shall record:."),
        ("A.6.3-20", "Training Records",
         "Training records shall be retained for the duration of employment plus 2 years after departure."),
        ("A.6.3-21", "Training Completion Rates",
         "Training completion rates shall be monitored. Non-completion shall be escalated:."),
    ]),

    ("Training Content Updates", [
        ("A.6.3-22", "Training Content",
         "Training content shall be reviewed and updated in response to:."),
        ("A.6.3-23", "Phishing Simulation Results: If Phishing",
         "Phishing simulation results: If phishing metrics breach red thresholds, targeted training content shall be developed within 30 days."),
    ]),

    ("Training Effectiveness Metrics", [
        ("A.6.3-24", "The Information Security Management Team",
         "The information security management team shall measure the effectiveness of the awareness and training programme using the following framework:."),
    ]),

    ("Language and Accessibility", [
        ("A.6.3-25", "Training Materials",
         "Training materials shall be provided in the languages used within the organisation, reflecting Switzerland's multilingual context:."),
        ("A.6.3-26", "Primary Language: Training",
         "Primary language: Training shall be available in the organisation's primary business language."),
        ("A.6.3-27", "Additional Languages: Where The",
         "Additional languages: Where the workforce includes employees whose primary language differs from the business language, key training materials (at minimum: annual awareness, onboarding, and phishing reporting instructions) shall be made available in the relevant additional languages (e.g., German, French, Italian, English)."),
        ("A.6.3-28", "Accessibility: Training Platforms",
         "Accessibility: Training platforms shall support accessibility features (screen readers, subtitles for video content, adjustable text size) where reasonably practicable."),
    ]),

])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS
    ))


# =============================================================================
# QA_VERIFIED: 2026-02-08
# QA_STATUS: PASSED - AUTO-GENERATED (Phase 2 Operational Checklist)
# QA_TOOL: meta_generate_op_checklists.py
# CHANGES: Auto-generated from ISMS-OP-POL-A.6.3
# =============================================================================
