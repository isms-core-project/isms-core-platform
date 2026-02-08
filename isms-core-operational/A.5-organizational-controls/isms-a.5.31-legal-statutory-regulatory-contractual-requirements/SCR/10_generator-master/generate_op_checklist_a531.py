#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.31 — Legal, Statutory, Regulatory and Contractual Requirements Compliance Checklist

Control A.5.31: Legal, Statutory, Regulatory and Contractual Requirements
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Reg Ident and Applicability (9 reqs)
4. Swiss Regulatory Requirements (33 reqs)
5. Contractual Requirements (11 reqs)
6. Compliance Mon and Review (7 reqs)
7. Compliance Measurement (1 reqs)
8. Reg Change Comms (SOC 2 CC2.3) (1 reqs)

Total: 62 requirements across 6 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.31"
CONTROL_ID = "A.5.31"
CONTROL_NAME = "Legal, Statutory, Regulatory and Contractual Requirements"
SOURCE_POLICY = "ISMS-OP-POL-A.5.31"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.31
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Reg Ident and Applicability", [
        ("A.5.31-01", "Maintain A Systematic Process For",
         "The organisation shall maintain a systematic process for identifying legal, statutory, regulatory, and contractual requirements relevant to information security. This process shall be initiated:."),
        ("A.5.31-02", "Annual Comprehensive Review — Full Scan",
         "Annual comprehensive review — full scan of the regulatory landscape and validation of all entries in the Regulatory Register. Performed in Q4 (October–November) to align with the annual Management Review cycle and allow remediation planning for the following year. The review completion date shall be documented in the Regulatory Register."),
        ("A.5.31-03", "Utilise The Following Sources To",
         "The organisation shall utilise the following sources to identify potentially applicable regulations, listed in order of authority:."),
        ("A.5.31-04", "Higher-Authority Sources Take",
         "Where sources conflict, higher-authority sources take precedence. Conflicts between equal-level sources (e.g., nFADP vs. GDPR) shall be resolved by legal counsel."),
        ("A.5.31-05", "For Each Potentially Applicable",
         "For each potentially applicable regulation, the organisation shall assess applicability across three dimensions:."),
        ("A.5.31-06", "Or If Applicability Is Uncertain, It",
         "If a regulation is clearly relevant across any dimension, or if applicability is uncertain, it shall be added to the Regulatory Register with an appropriate tier classification."),
        ("A.5.31-07", "Applicable Regulation",
         "Each applicable regulation shall be classified into one of three tiers:."),
        ("A.5.31-08", "Default Position:* Where Applicability",
         "Default position:* Where applicability is uncertain after assessment, the organisation shall default to a higher tier (Tier 1 over Tier 2, Tier 2 over Tier 3) to reduce the risk of non-compliance."),
        ("A.5.31-09", "Maintain A Regulatory Register",
         "The organisation shall maintain a Regulatory Register documenting all applicable requirements. This register is the authoritative source for regulatory compliance obligations."),
    ]),

    ("Swiss Regulatory Requirements", [
        ("A.5.31-10", "The Swiss Nfadp, Effective 1 September",
         "The Swiss nFADP, effective 1 September 2023, is the primary data protection legislation governing the organisation's processing of personal data. The organisation shall comply with the following key requirements:."),
        ("A.5.31-11", "Personal Data",
         "Personal data shall be:."),
        ("A.5.31-12", "Processed Lawfully And In Good Faith",
         "Processed lawfully and in good faith — Processing shall be conducted transparently, with a clear and documented purpose."),
        ("A.5.31-13", "Collected For Specified Purposes — Data",
         "Collected for specified purposes — Data shall be collected for specific, stated purposes and shall not be further processed in a manner incompatible with those purposes."),
        ("A.5.31-14", "Proportionate — Only Data That Is",
         "Proportionate — Only data that is adequate, relevant, and limited to what is necessary for the stated purpose shall be collected and processed."),
        ("A.5.31-15", "Accurate — Personal Data",
         "Accurate — Personal data shall be accurate, and every reasonable step shall be taken to ensure that inaccurate data is rectified or erased without delay."),
        ("A.5.31-16", "Not Retained Longer Than Necessary —",
         "Not retained longer than necessary — Data shall be retained only for as long as necessary for the processing purpose, or as required by law. It shall then be destroyed or anonymised."),
        ("A.5.31-17", "Processed Securely — Appropriate",
         "Processed securely — Appropriate technical and organisational measures shall be implemented to protect personal data against unauthorised processing, accidental loss, or destruction (Art. 8 nFADP)."),
        ("A.5.31-18", "A Valid Legal Basis Under Gdpr",
         "Where the organisation also processes data of EU/EEA individuals, a valid legal basis under GDPR Article 6 shall be identified and documented for each processing activity."),
        ("A.5.31-19", "Inform Data Subjects At The Time",
         "The organisation shall inform data subjects at the time of data collection. Privacy notices shall include: the identity and contact details of the controller, purposes of processing, categories of data processed, recipients or categories of recipients, whether data is transferred abroad and applicable safeguards, the retention period, and the rights of data subjects."),
        ("A.5.31-20", "Maintain A Data Subject Rights Request",
         "The organisation shall maintain a Data Subject Rights Request Register documenting all requests, responses, and timelines. SLA tracking shall include:."),
        ("A.5.31-21", "Data Security Breaches",
         "Data security breaches shall be reported to the Federal Data Protection and Information Commissioner (FDPIC) as soon as possible where the breach is likely to result in a high risk to the personality or fundamental rights of data subjects. Data subjects shall also be informed where necessary for their protection or where the FDPIC requires it."),
        ("A.5.31-22", "Be Documented In The Breach Register",
         "All breaches shall be documented in the breach register regardless of the notification threshold. Upon discovery of any potential breach, an immediate assessment shall be performed within 4 hours to determine:."),
        ("A.5.31-23", "The Immediate Assessment Outcome",
         "The immediate assessment outcome shall be recorded in the breach register entry and approved by the CISO or Compliance Officer."),
        ("A.5.31-24", "Maintain A Record Of Processing",
         "The organisation shall maintain a Record of Processing Activities (ROPA) documenting all processing operations."),
        ("A.5.31-25", "Sme Exemption (Dsv Art. 4):*",
         "SME exemption (DSV Art. 4):* Organisations with fewer than 250 employees are exempted from maintaining a ROPA unless their processing presents a high risk of violating personality or fundamental rights (e.g., large-scale processing of sensitive data, high-risk profiling). The organisation shall document its assessment of whether the exemption applies, including:."),
        ("A.5.31-26", "Best Practice Recommendation:* Even",
         "Best practice recommendation:* Even where the SME exemption applies, maintaining a simplified ROPA is strongly recommended as it supports accountability, incident response, and audit readiness. The organisation shall reassess the exemption annually and whenever employee headcount approaches 250 or processing activities materially change."),
        ("A.5.31-27", "Art. 1-3 — Data Security Measures",
         "Art. 1-3 — Data security measures: The controller and processor shall implement technical and organisational measures appropriate to the risk. The adequacy of measures depends on the purpose, nature, and extent of data processing and the risk to data subjects. Measures shall be reviewed regularly."),
        ("A.5.31-28", "Art. 4 — Logging Of Automated",
         "Art. 4 — Logging of automated processing: Processing of personal data in automated systems shall be logged to enable retrospective verification that data has not been lost, deleted, destroyed, modified, or disclosed without authorisation. Logs shall be retained for at least one year."),
        ("A.5.31-29", "Art. 8 — Duty To Inform",
         "Art. 8 — Duty to inform on cross-border transfers: Where personal data is transferred abroad, the organisation shall disclose the destination country and applicable safeguards."),
        ("A.5.31-30", "Art. 14 — Dpia Retention: Data",
         "Art. 14 — DPIA retention: Data Protection Impact Assessment documentation shall be retained for at least 2 years after processing ends."),
        ("A.5.31-31", "Data Protection Impact Assessments (Art.",
         "Data Protection Impact Assessments (Art. 22 nFADP):* The organisation shall conduct a DPIA before commencing any processing that is likely to result in a high risk to the personality or fundamental rights of data subjects. High-risk processing includes:."),
        ("A.5.31-32", "The Dpia",
         "The DPIA shall assess the necessity and proportionality of processing, evaluate risks to data subjects, and identify measures to mitigate those risks. Where the DPIA concludes that high risk remains despite mitigation measures, the FDPIC shall be consulted prior to processing (Art. 23 nFADP)."),
        ("A.5.31-33", "Annex 1 — Adequacy List: Countries",
         "Annex 1 — Adequacy list: Countries determined by the Swiss Federal Council to provide adequate data protection for the purposes of cross-border data transfers. The organisation shall maintain a current copy of the DSV Annex 1 adequacy list and verify the adequacy status of each destination country before initiating cross-border transfers. Note: The Swiss and EU adequacy lists differ — a country may be adequate under one framework but not the other (e.g., the US is adequate under the Swiss-U.S. Data Privacy Framework but subject to specific conditions)."),
        ("A.5.31-34", "Art. 328 — Employer Duty Of",
         "Art. 328 — Employer duty of care: The employer shall protect and respect the personality rights of employees, including the protection of their personal data and privacy."),
        ("A.5.31-35", "Art. 957-958F — Record-Keeping",
         "Art. 957-958f — Record-keeping obligations: Legal entities and sole proprietorships with turnover of at least CHF 500,000 shall maintain commercial books and records. Business books, accounting vouchers, business reports, and audit reports shall be retained for 10 years from the end of the business year (Art. 958f CO). Records may be kept on paper, electronically, or in a comparable format provided they can be read at any time."),
        ("A.5.31-36", "Monitoring Behaviour, Or As A Processor",
         "Where the organisation processes personal data of individuals located in the EU/EEA — whether through offering goods or services, monitoring behaviour, or as a processor for EU-based controllers — GDPR shall apply in addition to the nFADP."),
        ("A.5.31-37", "Legal Basis Required — A Valid",
         "Legal basis required — A valid legal basis under Art. 6 GDPR shall be documented for each processing activity (consent, contract, legal obligation, vital interests, public interest, or legitimate interests). The legal basis shall be recorded in the ROPA and, where consent is relied upon, consent records shall be maintained in [GRC Tool / Privacy Management Platform] with evidence of when and how consent was obtained."),
        ("A.5.31-38", "Maintain Clear Documentation Of Which",
         "The organisation shall maintain clear documentation of which processing activities fall under nFADP only, which fall under GDPR, and which fall under both."),
        ("A.5.31-39", "Not Transfer Personal Data To Countries",
         "The organisation shall not transfer personal data to countries outside Switzerland unless adequate safeguards are in place:."),
        ("A.5.31-40", "Transfer Impact Assessments (Tias)*",
         "Transfer Impact Assessments (TIAs)* shall be conducted where the adequacy of the destination country is uncertain or where legal frameworks are subject to change. The TIA methodology shall include:."),
        ("A.5.31-41", "Document And Approve — Record The",
         "Document and approve — Record the assessment, conclusion, and approval. TIAs for Tier 1 transfers shall be approved by the Compliance Officer with legal counsel input."),
        ("A.5.31-42", "Be Aware Of The Enforcement Mechanisms",
         "The organisation shall be aware of the enforcement mechanisms and potential penalties under applicable regulations:."),
    ]),

    ("Contractual Requirements", [
        ("A.5.31-43", "Systematically Review All Customer",
         "The organisation shall systematically review all customer contracts for compliance requirements related to information security. This includes:."),
        ("A.5.31-44", "Contractual Compliance Requirements",
         "Contractual compliance requirements shall be assessed and added to the Regulatory Register with the appropriate tier classification. Where a customer contract explicitly requires compliance with a specific regulation and includes enforcement mechanisms (penalties, termination rights), the requirement shall be classified as Tier 1."),
        ("A.5.31-45", "Pre-Signature Review — Business",
         "Pre-signature review — Business Development shall flag all compliance clauses to the Compliance Officer before contract execution."),
        ("A.5.31-46", "Gap Notification — Where Gaps Exist",
         "Gap notification — Where gaps exist, Business Development shall be informed of the remediation timeline before contract execution. Contracts shall not be signed where Tier 1 compliance gaps cannot be remediated within the contract start date."),
        ("A.5.31-47", "Renewal Review — Compliance Clauses",
         "Renewal review — Compliance clauses shall be reviewed at each contract renewal for changes or new requirements."),
        ("A.5.31-48", "Review Supplier And Subprocessor",
         "The organisation shall review supplier and subprocessor agreements for obligations that flow through to the organisation. This includes:."),
        ("A.5.31-49", "Pass-Through Obligations",
         "Pass-through obligations shall be documented in the Regulatory Register alongside directly applicable regulations."),
        ("A.5.31-50", "The Compliance Requirements Associated",
         "Where the organisation holds or pursues certifications, the compliance requirements associated with those certifications shall be treated as Tier 1 obligations:."),
        ("A.5.31-51", "Certification Requirements",
         "Certification requirements shall be reviewed upon any of the following triggers:."),
        ("A.5.31-52", "Comply With Applicable Laws And",
         "The organisation shall comply with applicable laws and regulations regarding the use of cryptography, including:."),
        ("A.5.31-53", "These Requirements",
         "These requirements shall be documented in the Regulatory Register and reflected in the Use of Cryptography Policy (ISMS-OP-POL-A.8.24)."),
    ]),

    ("Compliance Mon and Review", [
        ("A.5.31-54", "Conduct A Comprehensive Annual Review Of",
         "The organisation shall conduct a comprehensive annual review of all entries in the Regulatory Register:."),
        ("A.5.31-55", "The Annual Review",
         "The annual review shall be performed by the Compliance Officer (or equivalent), with ISMS Manager approval of the review summary."),
        ("A.5.31-56", "In Addition To The Annual Review",
         "In addition to the annual review, the Regulatory Register shall be revisited when triggered by:."),
        ("A.5.31-57", "Reassessments Triggered By Events",
         "Reassessments triggered by events shall be completed within 30 days of the trigger event (within 60 days for mergers and acquisitions due to complexity)."),
        ("A.5.31-58", "Track To Closure — Monitor Progress",
         "Track to closure — Monitor progress. Gaps overdue by more than 30 days shall be escalated to the ISMS Manager; gaps overdue by more than 60 days shall be escalated to executive management."),
        ("A.5.31-59", "The Organisation",
         "Where full remediation is not feasible within the required timeframe, the organisation shall implement compensating controls and document a formal risk acceptance signed by executive management."),
        ("A.5.31-60", "External Dependency Gaps:* Where",
         "External dependency gaps:* Where remediation depends on a third party (e.g., vendor software update, supplier contract amendment, cloud provider feature), the gap owner shall:."),
    ]),

    ("Compliance Measurement", [
        ("A.5.31-61", "The Information Security Management Team",
         "The information security management team shall verify compliance with this policy through various methods, including but not limited to: Regulatory Register audits, compliance gap analysis, internal and external audits, regulatory review records, and feedback to the policy owner."),
    ]),

    ("Reg Change Comms (SOC 2 CC2.3)", [
        ("A.5.31-62", "Acknowledgement — Team Leads",
         "Acknowledgement — Team leads shall acknowledge receipt and confirm understanding within 5 business days."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.31
# =============================================================================
