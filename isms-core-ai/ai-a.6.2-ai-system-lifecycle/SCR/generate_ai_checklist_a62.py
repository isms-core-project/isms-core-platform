#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
AI-CHK-A.6.2 — AI System Lifecycle Compliance Checklist

Controls A.6.2: AI System Specification, Operation,
                Monitoring, Change Management, Decommissioning
Product: ISMS CORE AI (ISO/IEC 42001:2023)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. AI System Specification (A.6.2.1) — 5 reqs
4. Operation (A.6.2.2) — 5 reqs
5. Monitoring (A.6.2.3) — 5 reqs
6. Change Management (A.6.2.4) — 4 reqs
7. Decommissioning (A.6.2.5) — 4 reqs

Total: 23 requirements across 5 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

_AI_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_AI_ROOT / '00-checklist-engine'))
from ai_checklist_engine import generate_checklist

DOCUMENT_ID   = "AI-CHK-A.6.2"
CONTROL_ID    = "A.6.2"
CONTROL_NAME  = "AI System Lifecycle"
SOURCE_POLICY = "AI-POL-A.6.2"

REQUIREMENTS = OrderedDict([
    ("AI System Specification", [
        ("A.6.2.1-01", "System Specification Document",
         "Every in-scope AI system shall have a current system specification document covering: system purpose, intended use, use restrictions, input and output definitions, performance requirements, and human oversight mechanism. The specification shall be approved before development commences."),
        ("A.6.2.1-02", "Technical Documentation",
         "Technical documentation shall be maintained for every AI system, structured per the requirements in AI-IMP-A.6.2-TG. Technical documentation shall be sufficient to enable evaluation of the system's compliance with applicable requirements."),
        ("A.6.2.1-03", "Specification Scope",
         "The system specification shall define: the populations affected, the geographic scope of deployment, the languages supported, and the environmental conditions under which the system is designed to operate."),
        ("A.6.2.1-04", "Pre-Operational Checklist",
         "Before a new AI system enters operational use, the AI System Owner shall complete a pre-operational checklist confirming: AISIA approved, V&V complete, user training complete, monitoring in place, and operational procedures documented."),
        ("A.6.2.1-05", "Specification Currency",
         "The system specification shall be updated whenever a material change is made to the AI system. Outdated specifications shall not remain as the current version; superseded versions shall be preserved in version control."),
    ]),

    ("Operation", [
        ("A.6.2.2-01", "Operational Procedures",
         "The organisation shall document operational procedures for each AI system covering: normal operation, escalation of AI outputs for human review, override procedures, and incident first response. Procedures shall be accessible to all operators."),
        ("A.6.2.2-02", "Operator Training",
         "All persons operating an AI system shall have completed the required training before the system enters operational use. The AI System Owner shall maintain training completion records and refresh training when the system changes materially."),
        ("A.6.2.2-03", "Intended Use Enforcement",
         "The AI System Owner shall implement controls to prevent operational use of the AI system for purposes outside its documented intended use. Where misuse is detected, the AI System Owner shall escalate per the process in AI-POL-A.9.2-4."),
        ("A.6.2.2-04", "Output Review for High-Impact Systems",
         "For AI systems classified as High impact, the organisation shall implement a process for human review of AI outputs before those outputs are acted upon in consequential decisions. The review process shall be documented and auditable."),
        ("A.6.2.2-05", "Operational Logging",
         "AI systems shall generate operational logs meeting the minimum logging requirements in AI-IMP-A.6.2-TG. Logs shall be retained per the retention schedule proportionate to the system's impact classification."),
    ]),

    ("Monitoring", [
        ("A.6.2.3-01", "Monitoring Plan",
         "The AI System Owner shall maintain a monitoring plan for each AI system, defining: KPIs monitored, monitoring frequency, alert thresholds, and escalation paths. The monitoring plan shall be proportionate to the system's impact classification."),
        ("A.6.2.3-02", "Performance Monitoring",
         "The organisation shall monitor AI system performance against defined KPIs in operation. Performance results shall be recorded. Degradation below defined thresholds shall trigger escalation."),
        ("A.6.2.3-03", "Distributional Shift Detection",
         "The AI System Owner shall implement monitoring for distributional shift — changes in input data distributions that may degrade model performance or introduce bias. Detected shifts shall be assessed and reported to the AI Governance Officer."),
        ("A.6.2.3-04", "Incident Trigger",
         "The monitoring plan shall define the thresholds at which a monitoring alert escalates to a formal AI incident under AI-POL-A.6.2. Escalation criteria shall be documented and communicated to all operators."),
        ("A.6.2.3-05", "Monitoring Review",
         "Monitoring results shall be reviewed by the AI System Owner at minimum quarterly for High-impact systems, semi-annually for Medium-impact, and annually for Low-impact. Review findings shall feed into the periodic AISIA review."),
    ]),

    ("Change Management", [
        ("A.6.2.4-01", "Change Classification",
         "The AI System Owner shall classify all proposed changes to an AI system as material or minor per the criteria in AI-POL-A.6.2. Material changes shall require a new or updated AISIA and re-validation before deployment."),
        ("A.6.2.4-02", "Change Approval",
         "Material changes shall be approved by the AI Governance Officer before implementation. Minor changes shall be approved by the AI System Owner. All changes shall be logged with classification, approval record, and effective date."),
        ("A.6.2.4-03", "Emergency Change Procedure",
         "The organisation shall define an emergency change procedure for urgent fixes to AI systems in production. Emergency changes shall still require post-deployment review and retrospective AISIA update where the change has impact implications."),
        ("A.6.2.4-04", "Version Management",
         "All AI system versions deployed to production shall be recorded in the model registry with: version identifier, deployment date, key change summary, V&V Record reference, and AISIA version applicable at time of deployment."),
    ]),

    ("Decommissioning", [
        ("A.6.2.5-01", "Decommissioning Plan",
         "Before decommissioning an AI system, the AI System Owner shall prepare a decommissioning plan covering: user notification, data deletion or transfer, downstream system impacts, handover to replacement system if applicable, and record retention."),
        ("A.6.2.5-02", "User Notification",
         "Users and affected parties shall be notified of AI system decommissioning with adequate notice proportionate to the system's impact classification. Notification content and distribution shall be documented."),
        ("A.6.2.5-03", "Data Deletion",
         "Upon decommissioning, the organisation shall implement data deletion per the AI system's data retention schedule. Deletion of personal data shall comply with GDPR Article 17 requirements. Deletion shall be confirmed and documented."),
        ("A.6.2.5-04", "Record Retention",
         "Following decommissioning, AISIA records, V&V Records, incident records, and audit logs for the AI system shall be retained for a minimum of 5 years. The AI Governance Officer shall confirm record retention is in place before system shutdown."),
    ]),
])

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 42001:2023"
    ))

# QA_VERIFIED: [YYYY-MM-DD]
