#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
AI-CHK-A.5.2-5 — AI System Impact Assessment Compliance Checklist

Controls A.5.2-5: AISIA Process, AISIA Documentation,
                  Individual Impact Assessment, Societal Impact Assessment
Product: ISMS CORE AI (ISO/IEC 42001:2023)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. AISIA Process (A.5.2) — 7 reqs
4. AISIA Documentation (A.5.3) — 5 reqs
5. Individual Impact Assessment (A.5.4) — 6 reqs
6. Societal Impact Assessment (A.5.5) — 5 reqs

Total: 23 requirements across 4 domains

NOTE: The AISIA template itself is in AI-IMP-A.5.2-5-TG. This checklist
      verifies that the AISIA process is in place and being followed — not
      the content of individual AISIA records.
"""

import sys
from pathlib import Path
from collections import OrderedDict

_AI_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_AI_ROOT / '00-checklist-engine'))
from ai_checklist_engine import generate_checklist

DOCUMENT_ID   = "AI-CHK-A.5.2-5"
CONTROL_ID    = "A.5.2-5"
CONTROL_NAME  = "AI System Impact Assessment"
SOURCE_POLICY = "AI-POL-A.5.2-5"

REQUIREMENTS = OrderedDict([
    ("AISIA Process", [
        ("A.5.2-01", "Process Establishment",
         "The organisation shall establish, document, and implement a process for AI System Impact Assessment (AISIA) that is applied to every in-scope AI system. The process shall follow ISO/IEC 42005:2025 methodology."),
        ("A.5.2-02", "Deployment Gate",
         "No AI system shall be deployed in an operational context without a completed and approved AISIA. The AI Governance Officer shall approve the AISIA before deployment authorisation is issued."),
        ("A.5.2-03", "Material Change Trigger",
         "A new or updated AISIA shall be completed before any material change to an AI system is deployed — including new use cases, new affected populations, changed deployment context, and significant model updates."),
        ("A.5.2-04", "Review Schedule",
         "AISIAs shall be reviewed on a schedule proportionate to impact classification: High-impact every 6 months; Medium-impact annually; Low-impact every 3 years. Overdue AISIAs shall be flagged and escalated."),
        ("A.5.2-05", "Post-Incident Review",
         "Following any AI incident where the system's impact on individuals was material, the AISIA for the affected system shall be reviewed and updated if the incident reveals new or underestimated harms."),
        ("A.5.2-06", "AISIA Register",
         "The AI Governance Officer shall maintain an AISIA Register listing all in-scope AI systems with their current AISIA version, classification, approval date, and next review date."),
        ("A.5.2-07", "FRIA and DPIA Alignment",
         "Where EU AI Act Fundamental Rights Impact Assessments (FRIA) or GDPR Data Protection Impact Assessments (DPIA) are required, the AISIA shall serve as the analytical foundation, with cross-references documented."),
    ]),

    ("AISIA Documentation", [
        ("A.5.3-01", "Structured Record",
         "Each completed AISIA shall be documented as a structured record following the template in AI-IMP-A.5.2-5-TG (built against ISO/IEC 42005:2025 Annex E). Free-form assessments are not acceptable."),
        ("A.5.3-02", "Required Content",
         "Every AISIA record shall include: AI system identification; intended and foreseeable uses; technical information; deployment environment; interested party identification; benefits and harms analysis; AI system failures; reasonably foreseeable misuse; impact classification; and approval record."),
        ("A.5.3-03", "Approval Record",
         "Every AISIA shall include a signed approval record by the AI Governance Officer with approval date. Deployment authorisation shall not be issued without a signed approval record."),
        ("A.5.3-04", "Retention",
         "AISIA records shall be retained for the duration of the AI system's operational life plus 5 years after decommissioning, and shall be available to auditors and regulatory authorities on request."),
        ("A.5.3-05", "Version Control",
         "AISIAs shall be version-controlled. Updated AISIAs shall preserve prior versions. The current approved version shall be clearly identified in the AISIA Register."),
    ]),

    ("Individual Impact Assessment", [
        ("A.5.4-01", "Individual Impact Scope",
         "For each AI system, the organisation shall identify all categories of individuals whose interests could be affected by AI outputs — including direct users, affected individuals who are not users, and vulnerable groups."),
        ("A.5.4-02", "Harm Assessment Dimensions",
         "The individual impact assessment shall evaluate reasonably foreseeable harms and benefits across all required dimensions: Accountability, Transparency, Fairness and discrimination, Privacy, Reliability, Safety, Explainability, and Environmental impact."),
        ("A.5.4-03", "Harm Severity Rating",
         "For each identified harm, the organisation shall document severity (Negligible / Minor / Moderate / Serious / Critical), breadth (individual / group / population), and reversibility."),
        ("A.5.4-04", "Vulnerable Groups",
         "The individual impact assessment shall specifically identify and assess impacts on vulnerable groups — including children, elderly individuals, persons with disabilities, minority groups, and parties in power-asymmetric relationships."),
        ("A.5.4-05", "Human Oversight Assessment",
         "The individual impact assessment shall assess the adequacy of human oversight mechanisms — whether affected individuals have meaningful recourse, and whether human reviewers can exercise independent judgment."),
        ("A.5.4-06", "Impact Classification",
         "Based on the individual impact assessment, the AI system shall be assigned an overall impact classification: Low / Medium / High. The classification shall determine control requirements and review frequency."),
    ]),

    ("Societal Impact Assessment", [
        ("A.5.5-01", "Societal Impact Scope",
         "For each AI system, the organisation shall assess potential societal impacts — the macro-level effects of AI system deployment on communities, sectors, and society at large — as a distinct assessment from individual impact."),
        ("A.5.5-02", "Societal Dimensions",
         "The societal impact assessment shall address: systemic bias at scale, labour and employment impacts, misinformation risk, democratic and civic process impacts, concentration of power, and dependency/resilience risks."),
        ("A.5.5-03", "Environmental Impact",
         "The societal impact assessment shall include an assessment of the AI system's environmental impact — energy consumption, carbon footprint, and whether these are proportionate to the value delivered."),
        ("A.5.5-04", "Scale Consideration",
         "The societal impact assessment shall explicitly address how individual-level effects aggregate at scale — an AI system with low individual impact may have significant societal impact when deployed broadly."),
        ("A.5.5-05", "Mitigation Measures",
         "Where societal impacts are identified, the organisation shall document what measures it can take to mitigate its contribution to those impacts, even where the impact is beyond its direct control."),
    ]),
])

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 42001:2023"
    ))

# QA_VERIFIED: [YYYY-MM-DD]
