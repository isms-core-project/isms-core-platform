#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.35-36 — Independent Review and Compliance Compliance Checklist

Controls A.5.35-36: Independent Review and Compliance
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Audit Programme (11 reqs)
4. Independent Review of Info Sec (20 reqs)
5. Finding Severity Classification (1 reqs)
6. Corrective Action & Remediation (4 reqs)
7. Compliance Verification (5 reqs)
8. Non-Conformity Management (6 reqs)
9. Risk Acceptance (3 reqs)
10. Compl Metrics and Reporting (3 reqs)
11. Improvement Inputs (3 reqs)

Total: 56 requirements across 9 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/SCR/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_OP_ROOT / 'SCR'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.5.35-36"
CONTROL_ID = "A.5.35-36"
CONTROL_NAME = "Independent Review and Compliance"
SOURCE_POLICY = "ISMS-OP-POL-A.5.35-36"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.35-36
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Audit Programme", [
        ("A.5.35-36-01", "Internal Audits",
         "Internal audits shall be conducted to assess the effectiveness of the information security management system and the controls documented in the Statement of Applicability."),
        ("A.5.35-36-02", "Internal Audits",
         "Internal audits shall be planned annually, based on risk and business need, ensuring all ISMS areas are covered over the [specify: 1-year / 3-year] audit cycle."),
        ("A.5.35-36-03", "Annual Audit Programme",
         "Annual audit programme shall prioritise:."),
        ("A.5.35-36-04", "The Annual Audit Plan",
         "The annual audit plan shall be approved by the Management Review Team by [month, e.g., December] for the following year."),
        ("A.5.35-36-05", "Internal Audits",
         "Internal audits shall be conducted by individuals independent of the area being audited (i.e., auditors shall not audit their own work)."),
        ("A.5.35-36-06", "Internal Audit Results",
         "Internal audit results shall be reported to and overseen by the Management Review Team."),
        ("A.5.35-36-07", "External Certification Audits",
         "External certification audits shall be conducted to assess the effectiveness of the information security management system and the controls documented in the Statement of Applicability."),
        ("A.5.35-36-08", "External Certification Audits",
         "External certification audits shall be conducted per the certification body's requirements and schedule."),
        ("A.5.35-36-09", "External Audit Results",
         "External audit results shall be reported to and overseen by the Management Review Team."),
        ("A.5.35-36-10", "Client And Third-Party Audits",
         "Client and third-party audits shall be conducted subject to a contract and/or non-disclosure agreement being in place."),
        ("A.5.35-36-11", "Be Reported To And Overseen By",
         "Results shall be reported to and overseen by the Management Review Team."),
    ]),

    ("Independent Review of Info Sec", [
        ("A.5.35-36-12", "Independent Reviews Of The",
         "Independent reviews of the organisation's approach to managing information security shall be conducted:."),
        ("A.5.35-36-13", "Be Conducted By Persons Independent Of",
         "Reviews shall be conducted by persons independent of the area being reviewed to prevent 'marking your own homework.' Independence may be achieved through:."),
        ("A.5.35-36-14", "Possess Appropriate Competence To",
         "Reviewers shall possess appropriate competence to conduct information security reviews, demonstrated through:."),
        ("A.5.35-36-15", "Reviewer Qualifications",
         "Reviewer qualifications shall be verified and documented before assignment to review activities."),
        ("A.5.35-36-16", "Independent Reviews",
         "Independent reviews shall assess whether the organisation's information security approach:."),
        ("A.5.35-36-17", "Review'S Scope",
         "Each review's scope shall be documented in advance, including: controls and areas to be reviewed, time period covered, review methodology, documentation and evidence requirements, and planned interviews and assessments."),
        ("A.5.35-36-18", "Independent Reviews",
         "Independent reviews shall follow a documented plan covering objectives, criteria, sampling methodology, timeline, resource requirements, and reporting requirements."),
        ("A.5.35-36-19", "Be Evidence-Based. Evidence Collected",
         "Reviews shall be evidence-based. Evidence collected during reviews shall be retained in the ISMS Evidence Library: [Specify: SharePoint site URL, Confluence space, GRC platform, or equivalent]."),
        ("A.5.35-36-20", "Evidence Retained",
         "Evidence retained shall include: documentation reviewed, interview notes, observation records, technical assessment results, and sampling records."),
        ("A.5.35-36-21", "Review Findings",
         "Review findings shall be documented in a formal review report and communicated to appropriate management levels."),
        ("A.5.35-36-22", "Audit And Review Activities",
         "Audit and review activities shall not compromise the security, availability, or integrity of production systems or data (ISO 27001:2022 Control A.8.34)."),
        ("A.5.35-36-23", "Approved Tools Only: Auditors",
         "Approved tools only: Auditors shall use pre-approved security assessment tools and scanning software. Approval list maintained by CISO."),
        ("A.5.35-36-24", "Change Management: Intrusive Testing",
         "Change management: Intrusive testing (penetration testing, vulnerability scanning with exploits) shall follow the change management process with risk assessment and rollback plan."),
        ("A.5.35-36-25", "Non-Production First: Testing",
         "Non-production first: Testing shall be performed in non-production environments where feasible; production testing requires CISO approval and business owner acceptance."),
        ("A.5.35-36-26", "Time Windows: Testing",
         "Time windows: Testing shall be scheduled during approved maintenance windows or low-impact periods."),
        ("A.5.35-36-27", "Backups Verified: Current Backups",
         "Backups verified: Current backups shall be verified before intrusive testing."),
        ("A.5.35-36-28", "Monitoring: Audit Testing",
         "Monitoring: Audit testing shall be logged; security monitoring teams notified to reduce false positive alerts."),
        ("A.5.35-36-29", "Live Production Data",
         "Live production data shall not be exported for audit analysis without Data Protection Officer approval and encryption."),
        ("A.5.35-36-30", "Audit Working Papers",
         "Audit working papers containing personal or confidential data shall be protected per the Information Classification and Handling Policy."),
        ("A.5.35-36-31", "Audit Evidence",
         "Audit evidence shall be securely disposed of after the retention period per this policy."),
    ]),

    ("Finding Severity Classification", [
        ("A.5.35-36-32", "Findings From Independent Reviews,",
         "All findings from independent reviews, compliance assessments, and audits shall be classified by severity:."),
    ]),

    ("Corrective Action & Remediation", [
        ("A.5.35-36-33", "Corrective Actions",
         "When findings are identified, corrective actions shall be planned and implemented within the following timeframes:."),
        ("A.5.35-36-34", "Corrective Actions",
         "All corrective actions shall be tracked in the corrective action register (incident and corrective action log) with:."),
        ("A.5.35-36-35", "Be Tracked And Reported",
         "Progress shall be tracked and reported:."),
        ("A.5.35-36-36", "Corrective Actions",
         "Corrective actions shall not be marked as complete until:."),
    ]),

    ("Compliance Verification", [
        ("A.5.35-36-37", "Compliance With The Organisation'S",
         "Compliance with the organisation's information security policy, topic-specific policies, rules, and standards shall be reviewed through a three-tier approach:."),
        ("A.5.35-36-38", "Be Verified Through Appropriate Methods",
         "Compliance shall be verified through appropriate methods, including:."),
        ("A.5.35-36-39", "Compliance Claims",
         "Compliance claims shall be supported by evidence, including:."),
        ("A.5.35-36-40", "Compliance Evidence",
         "Compliance evidence shall be stored in the ISMS Evidence Library (SharePoint, Confluence, or equivalent) and retained in accordance with the organisation's records retention schedule."),
        ("A.5.35-36-41", "Non-Completion Of Scheduled Assessments",
         "Non-completion of scheduled assessments shall be escalated: 30 days overdue to Department Head, 60 days overdue to CISO, reported at next Management Review."),
    ]),

    ("Non-Conformity Management", [
        ("A.5.35-36-42", "Non-Conformities Not Resolved Within",
         "Non-conformities not resolved within target timeframes shall be escalated:."),
        ("A.5.35-36-43", "Root Cause Analysis (Rca)",
         "Root cause analysis (RCA) shall be conducted for:."),
        ("A.5.35-36-44", "Rca Methodology*: The Organisation",
         "RCA methodology*: The organisation shall use a structured RCA approach such as:."),
        ("A.5.35-36-45", "Rca Documentation*",
         "RCA documentation* shall include: finding description, analysis method used, identified root cause(s), contributing factors, corrective actions, and preventive actions."),
        ("A.5.35-36-46", "The Organisation",
         "When a non-conformity occurs, the organisation shall:."),
        ("A.5.35-36-47", "Non-Conformities",
         "Non-conformities shall be recorded, documented, and tracked in the incident and corrective action log. The effectiveness of corrective and preventive actions shall be reviewed."),
    ]),

    ("Risk Acceptance", [
        ("A.5.35-36-48", "Risk Acceptance Requests",
         "Risk acceptance requests shall include:."),
        ("A.5.35-36-49", "Risk Acceptances",
         "Risk acceptances shall be reviewed:."),
        ("A.5.35-36-50", "The Risk Owner",
         "When a trigger condition occurs, the risk owner shall notify the CISO within 14 days for reassessment."),
    ]),

    ("Compl Metrics and Reporting", [
        ("A.5.35-36-51", "The Following Kpis",
         "The following KPIs shall be tracked to measure the effectiveness of the compliance and review programme:."),
        ("A.5.35-36-52", "Compliance And Review Metrics",
         "Compliance and review metrics shall be tracked over time to identify improvement or degradation trends (quarter-over-quarter, year-over-year), recurring finding patterns, areas requiring focused attention, and the effectiveness of remediation efforts."),
        ("A.5.35-36-53", "Trend Data",
         "Trend data shall be retained for a minimum of 3 years to support long-term analysis and certification audit preparation."),
    ]),

    ("Improvement Inputs", [
        ("A.5.35-36-54", "The Following Sources",
         "The following sources shall be considered as inputs for continual improvement of the ISMS:."),
        ("A.5.35-36-55", "Management Review Team — The Management",
         "Management Review Team — The Management Review Team shall consider opportunities for improvement as a standing agenda item."),
        ("A.5.35-36-56", "Changes To The Information Security",
         "Changes to the information security management system resulting from improvement activities shall be planned, managed, and recorded in the incident and corrective action log or change log, as appropriate."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.35-36
# =============================================================================
