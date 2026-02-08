#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.24-28 — Incident Management Compliance Checklist

Controls A.5.24-28: Incident Management
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Incident Reporting (4 reqs)
4. Event Assessment and Triage (4 reqs)
5. Incident Classification (1 reqs)
6. Incident Response (10 reqs)
7. Significant Incidents (2 reqs)
8. Data Breach Notification (5 reqs)
9. Lessons Learned (8 reqs)
10. Incident Response Testing (2 reqs)

Total: 36 requirements across 8 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/A.0-checklist-engine/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_OP_ROOT / 'A.0-checklist-engine'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.5.24-28"
CONTROL_ID = "A.5.24-28"
CONTROL_NAME = "Incident Management"
SOURCE_POLICY = "ISMS-OP-POL-A.5.24-28"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.24-28
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Incident Reporting", [
        ("A.5.24-28-01", "Employees And Third-Party Users",
         "All employees and third-party users shall report security events immediately upon discovery to the information security management team through the designated reporting channels:."),
        ("A.5.24-28-02", "Reporting Channels",
         "Reporting channels shall be communicated during onboarding and annual awareness training, and published on the organisation intranet."),
        ("A.5.24-28-03", "Include, Where Known",
         "Reports shall include, where known:."),
        ("A.5.24-28-04", "Not Attempt To Investigate Or Resolve",
         "Employees shall not attempt to investigate or resolve suspected incidents themselves. Preservation of evidence takes priority over curiosity."),
    ]),

    ("Event Assessment and Triage", [
        ("A.5.24-28-05", "The Information Security Management Team",
         "The information security management team shall assess all reported security events to determine whether they constitute a security incident."),
        ("A.5.24-28-06", "Consider",
         "Assessment shall consider:."),
        ("A.5.24-28-07", "Events That Do Not Meet The",
         "Events that do not meet the threshold for an incident shall be logged, and trends shall be monitored."),
        ("A.5.24-28-08", "Reported Security Events And Confirmed",
         "All reported security events and confirmed incidents shall be recorded in the incident register with the following minimum fields:."),
    ]),

    ("Incident Classification", [
        ("A.5.24-28-09", "Confirmed Incidents",
         "Confirmed incidents shall be classified by severity to determine response priority, escalation, and communication requirements:."),
    ]),

    ("Incident Response", [
        ("A.5.24-28-10", "Be Managed Through The Following Phases",
         "Incidents shall be managed through the following phases, aligned with NIST SP 800-61:."),
        ("A.5.24-28-11", "Containment — Limit The Impact And",
         "Containment — Limit the impact and prevent further damage. Short-term containment actions (e.g., isolating affected systems, disabling compromised accounts) shall be taken immediately. Long-term containment strategies shall be planned where eradication cannot be immediate."),
        ("A.5.24-28-12", "Recovery — Restore Systems And Services",
         "Recovery — Restore systems and services to normal operations. Recovery shall be verified through testing before returning systems to production. Monitoring shall be enhanced during the recovery period to detect recurrence."),
        ("A.5.24-28-13", "Incident Response Actions",
         "All incident response actions shall be documented with timestamps, actions taken, and personnel involved."),
        ("A.5.24-28-14", "The Following Roles",
         "The following roles shall be assigned within the incident response capability:."),
        ("A.5.24-28-15", "Role Assignments",
         "Role assignments shall be documented, communicated to all team members, and reviewed annually. Deputies shall be assigned for each role to ensure availability."),
        ("A.5.24-28-16", "The Incident Response Team Leader",
         "The incident response team leader shall escalate incidents to senior management when:."),
        ("A.5.24-28-17", "Incident Information",
         "Incident information shall be shared on a strict need-to-know basis. Communication during an active incident shall be coordinated through the incident response team leader."),
        ("A.5.24-28-18", "Internal Status Updates",
         "Internal status updates shall be provided at regular intervals for Critical and High incidents."),
        ("A.5.24-28-19", "External Communication (Media,",
         "External communication (media, customers, partners) shall be approved by senior management and reviewed by legal counsel before release."),
    ]),

    ("Significant Incidents", [
        ("A.5.24-28-20", "In All Instances Where A Situation",
         "In all instances where a situation may lead to an external investigation or legal proceedings, specialist external resources shall be engaged."),
        ("A.5.24-28-21", "At The Earliest Opportunity, All Work",
         "At the earliest opportunity, all work on, access to, modification of, or tampering with affected systems, documents, locations, files, databases, applications, or other in-scope entities shall stop. The only exceptions are the preservation of life, health, and safety, or the bare minimum actions required to triage and make safe."),
    ]),

    ("Data Breach Notification", [
        ("A.5.24-28-22", "The Organisation",
         "Where both nFADP and GDPR apply, the organisation shall meet the stricter timeline (72 hours)."),
        ("A.5.24-28-23", "Breach Notifications To Supervisory",
         "Breach notifications to supervisory authorities shall include, at minimum:."),
        ("A.5.24-28-24", "Be Provided In Phases Without Undue",
         "Where full information is not available at the time of notification, it shall be provided in phases without undue delay."),
        ("A.5.24-28-25", "Not All Security Incidents Involving",
         "Not all security incidents involving personal data require notification. The incident response team shall assess:."),
        ("A.5.24-28-26", "The Assessment And Decision (Including",
         "The assessment and decision (including the rationale for not notifying, if applicable) shall be documented."),
    ]),

    ("Lessons Learned", [
        ("A.5.24-28-27", "A Post-Incident Review",
         "A post-incident review shall be conducted for all Critical and High severity incidents, and optionally for Medium incidents where useful lessons may be derived."),
        ("A.5.24-28-28", "The Review",
         "The review shall be held within 5 business days of incident resolution, while details are still fresh. The review shall include all personnel who contributed to the response."),
        ("A.5.24-28-29", "The Review",
         "The review shall document:."),
        ("A.5.24-28-30", "Action Items",
         "Action items shall be tracked to completion."),
        ("A.5.24-28-31", "Lessons Learned",
         "Lessons learned shall be communicated to relevant personnel."),
        ("A.5.24-28-32", "The Incident Response Plan",
         "The incident response plan shall be updated where findings indicate gaps."),
        ("A.5.24-28-33", "Trends Across Incidents",
         "Trends across incidents shall be reviewed quarterly to identify systemic issues."),
        ("A.5.24-28-34", "Be Conducted In A Blame-Free Manner",
         "Reviews shall be conducted in a blame-free manner, focusing on system and process improvement rather than individual fault."),
    ]),

    ("Incident Response Testing", [
        ("A.5.24-28-35", "The Incident Response Plan",
         "The incident response plan shall be tested at least annually through tabletop exercises or simulations to verify that:."),
        ("A.5.24-28-36", "Test Results And Improvements",
         "Test results and improvements shall be documented, including participants, scenario details, observed gaps, and corrective actions with owners and deadlines."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.24-28
# =============================================================================
