#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
AI-CHK-A.4.2-6 — AI System Resources Compliance Checklist

Controls A.4.2-6: Computing Resources, Data Resources, Tooling,
                  System Architecture, Human Resources
Product: ISMS CORE AI (ISO/IEC 42001:2023)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Computing Resources (A.4.2) — 5 reqs
4. Data Resources (A.4.3) — 4 reqs
5. Tooling (A.4.4) — 4 reqs
6. System Architecture (A.4.5) — 4 reqs
7. Human Resources (A.4.6) — 4 reqs

Total: 21 requirements across 5 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

_AI_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_AI_ROOT / '00-checklist-engine'))
from ai_checklist_engine import generate_checklist

DOCUMENT_ID   = "AI-CHK-A.4.2-6"
CONTROL_ID    = "A.4.2-6"
CONTROL_NAME  = "AI System Resources"
SOURCE_POLICY = "AI-POL-A.4.2-6"

REQUIREMENTS = OrderedDict([
    ("Computing Resources", [
        ("A.4.2-01", "Resource Register",
         "The organisation shall maintain an AI System Resource Register documenting all in-scope AI systems and their associated resources. The Register shall be current and reviewed at minimum annually."),
        ("A.4.2-02", "Infrastructure Documentation",
         "For each AI system, the organisation shall document the computing infrastructure on which the system runs, including infrastructure type, provider, and geographic location of data processing."),
        ("A.4.2-03", "Supplier Dependencies",
         "The organisation shall identify and document single-vendor dependencies in AI system infrastructure. Systems with critical third-party AI API dependencies shall be assessed for supply chain risk."),
        ("A.4.2-04", "Continuity Planning",
         "Computing resource dependencies shall be referenced in business continuity and disaster recovery plans for AI systems rated as critical or High-impact."),
        ("A.4.2-05", "Register Currency",
         "The AI System Resource Register shall be updated when any new AI system enters the AIMS scope, when material changes occur, and when systems are decommissioned."),
    ]),

    ("Data Resources", [
        ("A.4.3-01", "Data Resource Documentation",
         "The organisation shall document, for each AI system, the training datasets used and the operational data processed at inference time, including source category and data governance record references."),
        ("A.4.3-02", "Personal Data Flag",
         "For each AI system's data resources, the organisation shall document whether personal data is involved in training or operational use and shall confirm that a documented legal basis exists where personal data is processed."),
        ("A.4.3-03", "Data Records Linkage",
         "Data resource entries in the AI System Resource Register shall link to the full data governance records maintained per AI-POL-A.7.2-6 (Data for AI Systems)."),
        ("A.4.3-04", "Prohibited Data",
         "The organisation shall document and enforce prohibitions on data sources that may not be used without explicit approval — including data with unknown provenance, unlicensed data, and personal data without a legal basis."),
    ]),

    ("Tooling", [
        ("A.4.4-01", "Tooling Documentation",
         "The organisation shall document, for each AI system, the key tooling used in development and operation — including MLOps platforms, model registries, monitoring tools, and logging infrastructure."),
        ("A.4.4-02", "Foundation Model Documentation",
         "Where AI systems use third-party foundation models or AI APIs, these shall be documented in the AI System Resource Register including provider, model name, and version."),
        ("A.4.4-03", "Open Source Licences",
         "Open-source AI libraries and pre-trained models used in AI systems shall have their licence reviewed by Legal before use in commercial or customer-facing applications."),
        ("A.4.4-04", "Vulnerability Management",
         "The organisation shall implement a process for tracking and addressing CVEs in AI-specific libraries and dependencies used in production AI systems."),
    ]),

    ("System Architecture", [
        ("A.4.5-01", "Architecture Documentation",
         "The organisation shall maintain architecture documentation for each AI system showing key components, data flows, integration points, and the human oversight mechanism."),
        ("A.4.5-02", "Integration Dependencies",
         "The organisation shall document all systems that provide input to or receive output from each AI system, enabling accurate impact assessment and incident response."),
        ("A.4.5-03", "Version Control",
         "Model artefacts, training code, inference code, and deployment configuration for each AI system shall be stored in version-controlled repositories with linkage between code versions and model versions."),
        ("A.4.5-04", "Model Registry",
         "The organisation shall maintain a model registry recording all deployed model versions with metadata including training dataset, V&V record reference, AISIA reference, and deployment status."),
    ]),

    ("Human Resources", [
        ("A.4.6-01", "Competency Documentation",
         "For each AI system, the AI System Owner shall document the competency requirements for persons operating or using the system, including required domain expertise and AI governance knowledge."),
        ("A.4.6-02", "Training Completion",
         "The organisation shall maintain records of training completion for all persons operating AI systems, and shall ensure training is refreshed when systems change materially."),
        ("A.4.6-03", "Competency Gaps",
         "Where competency gaps are identified for AI system operators, the AI System Owner shall document and escalate the gap and shall implement a remediation plan."),
        ("A.4.6-04", "New System Onboarding",
         "Before a new AI system enters operational use, all users shall have completed the required training and the AI System Owner shall confirm training completion as part of the deployment gate."),
    ]),
])

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 42001:2023"
    ))

# QA_VERIFIED: [YYYY-MM-DD]
