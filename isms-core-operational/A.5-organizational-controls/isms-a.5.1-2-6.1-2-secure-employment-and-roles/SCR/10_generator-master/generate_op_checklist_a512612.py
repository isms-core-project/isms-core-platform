#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.1-2-6.1-2 — ISMS Governance and Secure Employment Compliance Checklist

Controls A.5.1-2-6.1-2: ISMS Governance and Secure Employment
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Info Security Policy Framework (16 reqs)
4. Personnel Screening (11 reqs)
5. Terms and Conditions of Employ (6 reqs)
6. Monitoring (1 reqs)
7. Legal and Reg Obligations (1 reqs)

Total: 35 requirements across 5 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.1-2-6.1-2"
CONTROL_ID = "A.5.1-2-6.1-2"
CONTROL_NAME = "ISMS Governance and Secure Employment"
SOURCE_POLICY = "ISMS-OP-POL-A.5.1-2-6.1-2"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.1-2-6.1-2
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Info Security Policy Framework", [
        ("A.5.1-2-6.1-2-01", "Higher-Tier Policies Set Requirements;",
         "Higher-tier policies set requirements; lower-tier documents provide operational detail. Lower-tier documents shall not contradict higher-tier policies."),
        ("A.5.1-2-6.1-2-02", "Information Security Policies",
         "Information security policies shall be managed through defined lifecycle stages:."),
        ("A.5.1-2-6.1-2-03", "Creation*: Policies",
         "Creation*: Policies shall be developed using the organisational template, with input from stakeholders including Legal, HR, IT, and affected business units."),
        ("A.5.1-2-6.1-2-04", "Approval*: Policies",
         "Approval*: Policies shall be approved by the appropriate authority per tier before publication. Policy approval shall be performed by a different individual than the policy author. Tier 2 policies authored by the Security Team shall be approved by the CISO. The Master Policy authored by the CISO shall be approved by the CEO."),
        ("A.5.1-2-6.1-2-05", "Publication*: Approved Policies",
         "Publication*: Approved policies shall be published to the organisational policy repository (e.g., SharePoint, Confluence, or equivalent) with version control."),
        ("A.5.1-2-6.1-2-06", "Communication*: Policies",
         "Communication*: Policies shall be communicated to all affected personnel. Supplemental training shall be provided when: (a) >30% of users are affected, (b) a new technical control requires user action (e.g., MFA enrolment), or (c) a regulatory deadline is <90 days. Training formats: webinar, e-learning module, or annotated policy guide."),
        ("A.5.1-2-6.1-2-07", "Acknowledgment*: Critical Policies",
         "Acknowledgment*: Critical policies (Master Information Security Policy, Acceptable Use Policy, Code of Conduct) shall require formal acknowledgment from all personnel annually. Acknowledgments shall be collected via [electronic signature portal / HR system attestation] and tracked in the Personnel Training and Acknowledgment Register maintained by HR."),
        ("A.5.1-2-6.1-2-08", "Review*: Policies",
         "Review*: Policies shall be reviewed at planned intervals (minimum annually) and upon:."),
        ("A.5.1-2-6.1-2-09", "Change Management*: Policy Changes",
         "Change management*: Policy changes shall follow the change management process: change request logged in [GRC Tool / Change Management System], impact assessment performed (affected systems, users, controls), approval obtained per policy tier, change communicated to affected personnel, change implementation tracked (old version archived, new version published), and post-implementation review within 30 days to verify acknowledgments collected and no unintended impacts."),
        ("A.5.1-2-6.1-2-10", "Retirement*: Retired Policies",
         "Retirement*: Retired policies shall be archived with audit trail retained for a minimum of 3 years."),
        ("A.5.1-2-6.1-2-11", "Topic-Specific Policies (Tier 2)",
         "All topic-specific policies (Tier 2) shall include:."),
        ("A.5.1-2-6.1-2-12", "Exceptions To Any Information Security",
         "Exceptions to any information security policy shall be:."),
        ("A.5.1-2-6.1-2-13", "The Exception Register",
         "The exception register shall record: exception ID, affected control or policy, description, requestor, business justification, risk assessment, compensating controls, approval authority, approval date, expiry date, and review status."),
        ("A.5.1-2-6.1-2-14", "Be Reviewed Quarterly By The Isms",
         "Exceptions shall be reviewed quarterly by the ISMS Committee and reported in Management Review. Expired exceptions shall be re-assessed or closed within 30 days."),
        ("A.5.1-2-6.1-2-15", "Policy Violations",
         "Policy violations shall be classified by severity:."),
        ("A.5.1-2-6.1-2-16", "Violations (Critical, High, Medium)",
         "All violations (Critical, High, Medium) shall be logged in the Security Incident Register with investigation findings, remediation actions, and closure date. Violations shall be analysed quarterly for trends and policy effectiveness improvement."),
    ]),

    ("Personnel Screening", [
        ("A.5.1-2-6.1-2-17", "Conduct Background Verification Checks",
         "The organisation shall conduct background verification checks based on:."),
        ("A.5.1-2-6.1-2-18", "Proportionality*: Screening Intensity",
         "Proportionality*: Screening intensity shall be proportional to the sensitivity of information accessed, the criticality of the role, the level of system access and privileges, and regulatory requirements."),
        ("A.5.1-2-6.1-2-19", "Legality*: All Screening",
         "Legality*: All screening shall comply with Swiss Code of Obligations (OR) Art. 328 and 328b, Swiss nFADP (revDSG), and local employment law. Under Swiss law, employers may only collect information relevant to the role. Written consent from the candidate shall be obtained before conducting background checks. Criminal record checks may cover up to seven years in Switzerland."),
        ("A.5.1-2-6.1-2-20", "Fairness*: Screening",
         "Fairness*: Screening shall be conducted transparently. Candidates shall be informed before screening is conducted, consent shall be obtained where required, criteria shall be non-discriminatory and job-relevant, and candidates shall have the opportunity to clarify adverse findings."),
        ("A.5.1-2-6.1-2-21", "Confidentiality*: Screening Results",
         "Confidentiality*: Screening results shall be accessed only by HR and authorised hiring personnel, stored securely in [HR System] with access controls, retained for the duration of employment plus 2 years (for defence of employment decisions), and securely destroyed per the data deletion procedure thereafter."),
        ("A.5.1-2-6.1-2-22", "Classify Roles By Sensitivity And Apply",
         "The organisation shall classify roles by sensitivity and apply appropriate screening:."),
        ("A.5.1-2-6.1-2-23", "The Role-To-Screening-Level Mapping",
         "The role-to-screening-level mapping shall be documented and maintained by HR in consultation with the CISO. Assignments shall be reviewed annually and upon organisational restructure. Changes require CISO approval and HR execution."),
        ("A.5.1-2-6.1-2-24", "Pre-Employment*: Screening",
         "Pre-employment*: Screening shall be completed before granting organisational access."),
        ("A.5.1-2-6.1-2-25", "Re-Screening",
         "Re-screening shall be conducted only where: (a) contractually agreed in employment terms, (b) required by regulation (e.g., FINMA for financial sector roles), or (c) triggered by security incident or role change requiring elevated access."),
        ("A.5.1-2-6.1-2-26", "Adverse Findings",
         "Adverse findings shall be discussed with the candidate to allow clarification, assessed for relevance, recency, and severity, documented with a decision rationale, and handled consistently and non-discriminatorily."),
        ("A.5.1-2-6.1-2-27", "Third-Party Personnel Screening",
         "Third-party personnel screening shall be specified in contracts (minimum screening requirements equivalent to the access granted), attested by the vendor, and spot-checked by the organisation (sample verification per the third-party spot-checking process)."),
    ]),

    ("Terms and Conditions of Employ", [
        ("A.5.1-2-6.1-2-28", "Information Security Obligations",
         "Information security obligations shall be included in all employment-related contracts:."),
        ("A.5.1-2-6.1-2-29", "Employment Contracts",
         "All employment contracts shall include the following information security clauses:."),
        ("A.5.1-2-6.1-2-30", "New Hire Training",
         "New hire training shall cover: Acceptable Use Policy key requirements (authorised use, prohibited activities), information classification and handling rules, incident identification and reporting procedure, password and authentication requirements, physical security (badge use, visitor management, clean desk), and data protection obligations (confidentiality, nFADP/GDPR basics). Training delivered via [LMS platform] with completion tracked by HR. Certification required to provision system access."),
        ("A.5.1-2-6.1-2-31", "Upon Employee Termination (Voluntary Or",
         "Upon employee termination (voluntary or involuntary), the Line Manager shall initiate the termination workflow in [HR System] immediately. HR notifies IT Service Desk on the same business day. IT Service Desk:."),
        ("A.5.1-2-6.1-2-32", "Be Signed Before Access Is Granted",
         "Contracts shall be signed before access is granted:."),
        ("A.5.1-2-6.1-2-33", "Acknowledgments (Nda, Aup, Training",
         "All acknowledgments (NDA, AUP, training completion) shall be collected with signature (physical or electronic), tracked in [HR System], and re-collected annually for critical policies. Acknowledgment compliance shall be reported quarterly to the ISMS Committee. Personnel who do not acknowledge critical policies within 30 days of communication shall have system access suspended until acknowledgment is completed. Line managers shall be notified at 21 days."),
    ]),

    ("Monitoring", [
        ("A.5.1-2-6.1-2-34", "Compliance With The Policies And",
         "Compliance with the policies and procedures of the information security management system shall be monitored via the Management Review Team, together with independent reviews by both internal and external audit on a periodic basis."),
    ]),

    ("Legal and Reg Obligations", [
        ("A.5.1-2-6.1-2-35", "The Organisation Takes Its Legal And",
         "The organisation takes its legal and regulatory obligations seriously. Requirements arising from Swiss nFADP (revDSG), the Swiss Code of Obligations, and other applicable regulations are recorded in the Legal and Contractual Requirements Register. This register shall be reviewed at least annually and updated when new regulations apply or existing regulations change materially."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.1-2-6.1-2
# =============================================================================
