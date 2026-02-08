#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.34 — Privacy and Protection of PII Compliance Checklist

Control A.5.34: Privacy and Protection of PII
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Data Prot Policy Statement (1 reqs)
4. Legal Basis for Processing (2 reqs)
5. Lawfulness and Good Faith (8 reqs)
6. Accuracy (1 reqs)
7. Storage Period Limitation (1 reqs)
8. Security of Processing (11 reqs)
9. Cross-Border Data Transfers (5 reqs)
10. The Right of Access (2 reqs)
11. The Right to Rectification (1 reqs)
12. Agreement of Retention Periods (1 reqs)
13. Expiry of Retention Period (1 reqs)
14. Suspension Record Disposal (1 reqs)
15. Children's Data (4 reqs)
16. Optional Data Prot Advisor (1 reqs)

Total: 40 requirements across 14 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.34"
CONTROL_ID = "A.5.34"
CONTROL_NAME = "Privacy and Protection of PII"
SOURCE_POLICY = "ISMS-OP-POL-A.5.34"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.34
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Data Prot Policy Statement", [
        ("A.5.34-01", "Determine Its Role As Data Controller",
         "The organisation shall determine its role as Data Controller, Data Processor, or Joint Controller for each processing activity based on the context of its processing activities under the Swiss Federal Act on Data Protection (nFADP/revDSG). This determination shall be documented in the Record of Processing Activities (ROPA) and reflected in contractual arrangements with third parties. This policy confirms our commitment to protect the privacy of the personal information of our customers, clients, employees, and other interested parties. We have engaged in a programme of Information Security Management aligned to the international standard ISO 27001 to ensure that the processing of personal information is conducted using best practice processes."),
    ]),

    ("Legal Basis for Processing", [
        ("A.5.34-02", "A Valid Legal Basis Under Gdpr",
         "Where the organisation processes data of EU/EEA individuals, a valid legal basis under GDPR Article 6 shall be identified and documented for each processing activity in the Record of Processing Activities."),
        ("A.5.34-03", "Article 6 Of The Nfadp Requires",
         "Article 6 of the nFADP requires that personal data shall be:."),
    ]),

    ("Lawfulness and Good Faith", [
        ("A.5.34-04", "Inform Data Subjects At The Time",
         "The organisation shall inform data subjects at the time of data collection (Art. 19 nFADP). Privacy notices shall be provided covering:."),
        ("A.5.34-05", "Privacy Notices",
         "Privacy notices shall be concise, transparent, and written in plain language. They shall be made available at the point of data collection (e.g., on websites, in application forms, in employment contracts, at reception for visitors)."),
        ("A.5.34-06", "Be Freely Given, Specific, Informed, And",
         "Consent shall be freely given, specific, informed, and unambiguous (Art. 6(6)–(7) nFADP)."),
        ("A.5.34-07", "Consent For Sensitive Personal Data Or",
         "Consent for sensitive personal data or high-risk profiling shall be explicit (Art. 6(7) nFADP)."),
        ("A.5.34-08", "Be Recorded With The Date, Method",
         "Consent shall be recorded with the date, method, and scope of consent granted."),
        ("A.5.34-09", "Withdrawal Of Consent",
         "Withdrawal of consent shall be as easy as giving consent, and the process shall be communicated to data subjects."),
        ("A.5.34-10", "Be Capable Of Recording And Actioning",
         "Systems shall be capable of recording and actioning consent withdrawal without undue delay."),
        ("A.5.34-11", "Consent Records",
         "Consent records shall be retained for the duration of processing plus the applicable limitation period."),
    ]),

    ("Accuracy", [
        ("A.5.34-12", "Accurate And, Where Necessary, Kept Up",
         "Accurate and, where necessary, kept up to date; every reasonable step shall be taken to ensure that personal data that are inaccurate, having regard to the purposes for which they are processed, are erased or rectified without delay."),
    ]),

    ("Storage Period Limitation", [
        ("A.5.34-13", "The Organisation Has Implemented A Data",
         "The organisation has implemented a data retention policy and data retention schedule in line with legal, regulatory, and business needs. Personal data shall be destroyed or anonymised once it is no longer needed for the stated processing purpose (Art. 6(4) nFADP)."),
    ]),

    ("Security of Processing", [
        ("A.5.34-14", "Maintain A Record Of Processing",
         "The organisation shall maintain a Record of Processing Activities documenting all processing operations (DSV Art. 4–5)."),
        ("A.5.34-15", "Sme Exemption (Dsv Art. 4):*",
         "SME exemption (DSV Art. 4):* Organisations with fewer than 250 employees are exempted from maintaining a ROPA unless they process sensitive personal data on a large scale or conduct high-risk profiling. The organisation shall document its assessment of whether the exemption applies."),
        ("A.5.34-16", "Include: Purposes Of Processing,",
         "Where a ROPA is maintained, it shall include: purposes of processing, categories of data subjects and personal data, recipients, cross-border transfers, retention periods, and a description of technical and organisational security measures."),
        ("A.5.34-17", "The Ropa",
         "The ROPA shall be reviewed and updated annually, or whenever new processing activities commence, and made available to the FDPIC upon request."),
        ("A.5.34-18", "Conduct A Dpia Before Beginning",
         "The organisation shall conduct a DPIA before beginning processing activities that are likely to result in a high risk to the rights of data subjects (Art. 22 nFADP, Art. 35 GDPR where applicable)."),
        ("A.5.34-19", "Document: A Description Of The",
         "Each DPIA shall document: a description of the processing and its purposes, an assessment of necessity and proportionality, an assessment of risks to data subjects, and measures to address those risks."),
        ("A.5.34-20", "They May Approve The Dpia In",
         "Where a qualified Data Protection Advisor has been appointed, they may approve the DPIA in place of consulting the FDPIC (Art. 23(4) nFADP). Where residual risk remains high and no Data Protection Advisor is appointed, the FDPIC shall be consulted."),
        ("A.5.34-21", "Dpia Documentation",
         "DPIA documentation shall be retained for at least 2 years after processing ends (DSV Art. 14)."),
        ("A.5.34-22", "Retention Periods",
         "Retention periods shall be agreed by the relevant data owners in line with legal, regulatory, and business requirements:."),
        ("A.5.34-23", "The Information",
         "When the retention target is reached, the information shall be reviewed by the relevant data owner to confirm whether the information is to be further retained or destroyed. It shall be destroyed in line with the Information Classification and Handling Policy if there is no further business, statutory, or historical reason to retain it."),
        ("A.5.34-24", "Personal Data Is Transferred In Line",
         "Personal data is transferred in line with the Information Transfer Policy. Employees shall ensure the appropriate level of security in line with the policy and organisation processes."),
    ]),

    ("Cross-Border Data Transfers", [
        ("A.5.34-25", "Not Transfer Personal Data To Countries",
         "The organisation shall not transfer personal data to countries outside Switzerland unless:."),
        ("A.5.34-26", "European Commission Adequacy Decisions",
         "Where the organisation also processes EU/EEA data, European Commission adequacy decisions and GDPR transfer mechanisms (Art. 44–49) shall be applied as appropriate."),
        ("A.5.34-27", "Inform Their Line Manager And/Or A",
         "In the event of a breach of the data protection principles, employees shall inform their line manager and/or a member of the Management Review Team and invoke the Incident Management Process."),
        ("A.5.34-28", "Be Reported As Follows",
         "Breaches shall be reported as follows:."),
        ("A.5.34-29", "Maintain A Breach Register",
         "The organisation shall maintain a breach register documenting the facts, effects, and remedial actions for all breaches."),
    ]),

    ("The Right of Access", [
        ("A.5.34-30", "Provide Information On The Purpose,",
         "The organisation shall provide information on the purpose, categories of data, recipients, retention period, and source."),
        ("A.5.34-31", "Be Provided In Writing, Free Of",
         "Information shall be provided in writing, free of charge, within 30 days (Art. 25 nFADP). This period may be extended by a further 30 days where necessary due to complexity, with notification to the data subject."),
    ]),

    ("The Right to Rectification", [
        ("A.5.34-32", "Respond Within 30 Days",
         "The organisation shall respond within 30 days."),
    ]),

    ("Agreement of Retention Periods", [
        ("A.5.34-33", "The Relevant Owners Of The Documentation",
         "The relevant owners of the documentation as detailed in the asset register are responsible for agreeing the data retention periods in line with legal, regulatory, and business requirements. Data retention periods shall be approved by legal counsel."),
    ]),

    ("Expiry of Retention Period", [
        ("A.5.34-34", "The Information",
         "When the retention target is reached, the information shall be reviewed by the relevant owners to confirm that the information is to be further retained or destroyed. It shall be destroyed in line with the Information Classification and Handling Policy if there is no further business, statutory, or historical reason to retain it."),
    ]),

    ("Suspension Record Disposal", [
        ("A.5.34-35", "Or The Commencement Of Any Litigation",
         "In the event any employee of the organisation reasonably anticipates or becomes aware of a governmental investigation or audit, or the commencement of any litigation, all further disposal of documents shall be suspended until management, with the advice of legal counsel, determines otherwise. Management shall take such steps as are necessary to promptly inform affected staff of any suspension in the disposal or destruction of documents."),
    ]),

    ("Children's Data", [
        ("A.5.34-36", "Additional Care",
         "Additional care shall be taken to ensure privacy notices are understandable by the child or their legal representative."),
        ("A.5.34-37", "Consent For Online Services Directed At",
         "Consent for online services directed at children shall be obtained from the holder of parental authority where the child is under the applicable age threshold."),
        ("A.5.34-38", "Be Limited To What Is Strictly",
         "Processing shall be limited to what is strictly necessary and proportionate."),
        ("A.5.34-39", "Be Documented. If Children'S Data Is",
         "Where the organisation does not intentionally process children's data, this shall be documented. If children's data is discovered, it shall be assessed for compliance with applicable requirements."),
    ]),

    ("Optional Data Prot Advisor", [
        ("A.5.34-40", "They",
         "If a Data Protection Advisor is appointed, they shall:."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.34
# =============================================================================
