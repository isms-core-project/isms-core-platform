#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
AI-CHK-A.6.1 — AI Development Governance Compliance Checklist

Controls A.6.1: Responsible Design, Data Engineering for AI,
                Bias Assessment, Validation and Verification,
                Human Oversight in Development
Product: ISMS CORE AI (ISO/IEC 42001:2023)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Responsible Design (A.6.1.1) — 5 reqs
4. Data Engineering for AI (A.6.1.2) — 5 reqs
5. Bias Assessment (A.6.1.3) — 5 reqs
6. Validation and Verification (A.6.1.4) — 5 reqs
7. Human Oversight in Development (A.6.1.5) — 4 reqs

Total: 24 requirements across 5 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

_AI_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_AI_ROOT / '00-checklist-engine'))
from ai_checklist_engine import generate_checklist

DOCUMENT_ID   = "AI-CHK-A.6.1"
CONTROL_ID    = "A.6.1"
CONTROL_NAME  = "AI Development Governance"
SOURCE_POLICY = "AI-POL-A.6.1"

REQUIREMENTS = OrderedDict([
    ("Responsible Design", [
        ("A.6.1.1-01", "AISIA as Design Input",
         "The AI System Impact Assessment (AISIA) shall be completed or initiated before or during the design phase and shall serve as a formal input to design decisions. Designers shall document how AISIA findings have influenced system design."),
        ("A.6.1.1-02", "Responsible Design Review",
         "Before design is finalised, the AI System Owner shall conduct a responsible design review addressing: intended use scope, use-case restrictions, human oversight mechanism design, transparency to end users, and explainability requirements proportionate to impact classification."),
        ("A.6.1.1-03", "Explainability by Design",
         "For AI systems classified as Medium or High impact, the design shall incorporate an explainability mechanism enabling human reviewers to understand the basis for individual AI outputs. The mechanism shall be documented in the system architecture."),
        ("A.6.1.1-04", "Prohibited Design Patterns",
         "The organisation shall document and enforce a list of prohibited design patterns — including systems designed to be deceptive to users, systems that exploit cognitive biases, and systems implementing subliminal manipulation."),
        ("A.6.1.1-05", "Design Documentation",
         "The design phase shall produce a system specification document covering intended use, use restrictions, input and output definitions, human oversight design, and references to the AISIA and applicable fairness requirements."),
    ]),

    ("Data Engineering for AI", [
        ("A.6.1.2-01", "Data Governance Gate",
         "No AI system shall enter the model development phase until all training datasets have passed the data quality gate defined in AI-POL-A.7.2-6 and have documented Data Quality Records on file."),
        ("A.6.1.2-02", "Personal Data Controls",
         "Where training data contains personal data, the development team shall confirm a documented legal basis before use, apply data minimisation techniques, and ensure that the Data Acquisition Record references the legal basis and data governance controls applied."),
        ("A.6.1.2-03", "Prohibited Data Enforcement",
         "The development team shall verify that no prohibited data sources (as defined in AI-POL-A.7.2-6) are used in training or fine-tuning without explicit written approval from the AI Governance Officer."),
        ("A.6.1.2-04", "Data Preparation Documentation",
         "All data preparation steps — including cleaning, transformation, augmentation, feature engineering, and train/test splits — shall be documented in a Data Preparation Documentation record per the template in AI-IMP-A.7.2-6-TG."),
        ("A.6.1.2-05", "Reproducibility",
         "Training data pipelines shall be version-controlled and reproducible. The exact dataset version, preprocessing steps, and random seeds used for each model training run shall be recorded in the model registry entry for that run."),
    ]),

    ("Bias Assessment", [
        ("A.6.1.3-01", "Mandatory Bias Assessment",
         "Every AI system that produces outputs affecting individuals shall undergo a bias assessment before deployment. The assessment shall be documented and linked from the AISIA and V&V Record."),
        ("A.6.1.3-02", "Protected Characteristics",
         "The bias assessment shall evaluate system performance across all applicable protected characteristics under relevant law — including but not limited to: age, sex, race/ethnicity, disability, and religion. The characteristics assessed shall be documented."),
        ("A.6.1.3-03", "Fairness Metrics",
         "The bias assessment shall apply quantitative fairness metrics appropriate to the system's output type. The selected metrics, their definitions, computed values, and pass/fail thresholds shall be documented in the V&V Record."),
        ("A.6.1.3-04", "Bias Remediation",
         "Where bias assessment identifies unacceptable disparate impact, the development team shall implement remediation measures — including resampling, re-weighting, adversarial debiasing, or post-processing calibration — and re-run the assessment to confirm remediation effectiveness."),
        ("A.6.1.3-05", "Ongoing Bias Monitoring",
         "For deployed AI systems, the AI System Owner shall implement ongoing monitoring for distributional shift that could introduce or amplify bias. Monitoring results shall feed into the periodic AISIA review."),
    ]),

    ("Validation and Verification", [
        ("A.6.1.4-01", "V&V Requirement",
         "Every AI system shall undergo formal Validation and Verification (V&V) before deployment. V&V shall produce a documented V&V Record per the template in AI-IMP-A.6.1-TG. Systems without a signed V&V Record shall not be deployed."),
        ("A.6.1.4-02", "V&V Scope",
         "The V&V process shall cover: functional correctness against specification, performance against defined thresholds, bias assessment results, security testing (adversarial inputs, prompt injection where applicable), and human oversight mechanism effectiveness."),
        ("A.6.1.4-03", "V&V Independence",
         "For AI systems classified as High impact, V&V shall include independent review by a person other than the primary developer. The independent reviewer's sign-off shall be recorded in the V&V Record."),
        ("A.6.1.4-04", "Deployment Gate Criteria",
         "The V&V Record shall document whether the system meets the deployment gate: AISIA approved, all V&V tests passed or waivers documented, legal review complete where required, AI System Owner sign-off obtained. No deployment shall proceed without a closed deployment gate."),
        ("A.6.1.4-05", "Re-Validation on Material Change",
         "Any material change to a deployed AI system shall trigger re-validation covering the affected components. The scope of re-validation shall be proportionate to the nature of the change and shall be approved by the AI Governance Officer."),
    ]),

    ("Human Oversight in Development", [
        ("A.6.1.5-01", "Oversight Mechanism Design",
         "Every AI system shall have a defined human oversight mechanism that enables a human to review, override, or halt AI outputs. The mechanism shall be specified in the system design and tested as part of V&V."),
        ("A.6.1.5-02", "Override Capability",
         "AI systems whose outputs are acted upon automatically shall provide an effective mechanism for authorised personnel to override or suspend AI-driven actions. The override mechanism shall be documented and accessible without specialist knowledge."),
        ("A.6.1.5-03", "Human Review Enablement",
         "For AI systems classified as Medium or High impact, the system design shall provide human reviewers with the information needed to exercise independent judgement — including the AI's output, the confidence level or uncertainty, and the key inputs that drove the output."),
        ("A.6.1.5-04", "Automation Bias Mitigation",
         "Where human reviewers are present, the design shall include measures to mitigate automation bias — the tendency for humans to defer to AI outputs without exercising independent judgement. Measures shall be documented in the User Documentation."),
    ]),
])

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 42001:2023"
    ))

# QA_VERIFIED: [YYYY-MM-DD]
