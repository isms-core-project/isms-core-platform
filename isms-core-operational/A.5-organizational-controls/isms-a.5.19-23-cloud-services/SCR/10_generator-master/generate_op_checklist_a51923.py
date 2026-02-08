#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.19-23 — Cloud Services and Supplier Security Compliance Checklist

Controls A.5.19-23: Cloud Services and Supplier Security
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Supplier & Cloud Service (5 reqs)
4. Info Security Requirements (1 reqs)
5. Audit and Review (2 reqs)
6. Risk Management (3 reqs)
7. Supplier & Cloud Service Select (2 reqs)
8. Contracts, Agreements & Data (9 reqs)
9. Security Incident Management (7 reqs)
10. End of Contract (2 reqs)
11. Changes Cloud Service Supplier (4 reqs)

Total: 35 requirements across 9 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.19-23"
CONTROL_ID = "A.5.19-23"
CONTROL_NAME = "Cloud Services and Supplier Security"
SOURCE_POLICY = "ISMS-OP-POL-A.5.19-23"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.19-23
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Supplier & Cloud Service", [
        ("A.5.19-23-01", "Third-Party Suppliers And Cloud Services",
         "All third-party suppliers and cloud services shall be registered and recorded in the Supplier and Cloud Service Register."),
        ("A.5.19-23-02", "Update Frequency: The Register",
         "Update frequency: The register shall be reviewed and updated at least quarterly* or upon any new supplier engagement, contract change, or supplier exit."),
        ("A.5.19-23-03", "Suppliers And Cloud Services",
         "Suppliers and cloud services shall be assessed for criticality to the business."),
        ("A.5.19-23-04", "Suppliers And Cloud Services",
         "Suppliers and cloud services shall be classified based on the data processed, stored, or transmitted and their criticality to business operations:."),
        ("A.5.19-23-05", "In Addition, The Following",
         "In addition, the following shall be captured as a minimum:."),
    ]),

    ("Info Security Requirements", [
        ("A.5.19-23-06", "The Organisation",
         "Where a supplier cannot provide recognised certification, the organisation shall conduct a documented risk assessment and, if the supplier is engaged, implement compensating controls and obtain risk acceptance from the Information Security Manager and risk owner."),
    ]),

    ("Audit and Review", [
        ("A.5.19-23-07", "Obtain And Review The Most Current",
         "The organisation shall obtain and review the most current independent audit reports (within 12 months) for each Critical cloud service annually."),
        ("A.5.19-23-08", "The Service",
         "Where a cloud provider does not provide independent third-party reports, the service shall not be used for Confidential or Restricted data without CISO approval and documented residual risk acceptance."),
    ]),

    ("Risk Management", [
        ("A.5.19-23-09", "Every Supplier Handling Confidential Or",
         "Every supplier handling confidential or personal data shall be entered onto the Risk Register and managed via the organisation's risk management process."),
        ("A.5.19-23-10", "Cloud Service Risks",
         "Cloud service risks shall include assessment of:."),
        ("A.5.19-23-11", "Concentration Risk (Dependency On A",
         "Concentration risk (dependency on a single provider for critical services) — where a single provider hosts more than 50% of critical services or more than 75% of Confidential data, this shall be flagged in the risk register with a mitigation plan or accepted residual risk. Mitigation options include multi-provider diversification, multi-region deployment within the same provider, and validated exit strategy."),
    ]),

    ("Supplier & Cloud Service Select", [
        ("A.5.19-23-12", "Suppliers And Cloud Services",
         "Suppliers and cloud services shall be selected based on their ability to meet the needs of the business."),
        ("A.5.19-23-13", "Before Engaging A Supplier Or Cloud",
         "Before engaging a supplier or cloud service provider, data security due diligence shall be carried out that includes:."),
    ]),

    ("Contracts, Agreements & Data", [
        ("A.5.19-23-14", "An Appropriate Contract, Agreement,",
         "An appropriate contract, agreement, and/or Data Processing Agreement shall be in place and enforceable before engaging any supplier or cloud service provider to process, store, or transmit confidential or personal information."),
        ("A.5.19-23-15", "Contracts And Agreements",
         "Contracts and agreements shall address, at a minimum:."),
        ("A.5.19-23-16", "The Use By Suppliers Of Sub-Contractors",
         "The use by suppliers of sub-contractors or sub-processors shall be approved by the Information Security Manager. Sub-contractors and sub-processors are subject to the same terms and security requirements as the supplier."),
        ("A.5.19-23-17", "Cloud Service Providers",
         "Cloud service providers shall disclose their sub-processor list. The organisation shall be notified of changes to sub-processors at least 30 days in advance and shall retain the right to object where contractually achievable. Where objection rights cannot be obtained (as is common with major cloud providers), this limitation shall be documented in the risk register as residual risk with compensating controls (encryption, access monitoring)."),
        ("A.5.19-23-18", "Suppliers Processing Personal Data On",
         "All suppliers processing personal data on behalf of the organisation shall have a Data Processing Agreement in place that meets the requirements of Swiss nFADP (revDSG) Art. 9 and, where applicable, GDPR Art. 28."),
        ("A.5.19-23-19", "The Data Processing Agreement",
         "The Data Processing Agreement shall address:."),
        ("A.5.19-23-20", "The Organisation",
         "Where suppliers or cloud service providers process or store personal data outside Switzerland, the organisation shall verify that adequate data protection exists in the destination country per the Swiss Federal Council's adequacy list (Annex 1 to the Data Protection Ordinance)."),
        ("A.5.19-23-21", "For Transfers To Countries Not On",
         "For transfers to countries not on the adequacy list, appropriate safeguards shall be in place:."),
        ("A.5.19-23-22", "For Transfers To The United States",
         "For transfers to the United States, the organisation shall verify that the receiving organisation is certified under the Swiss-U.S. Data Privacy Framework. Where the provider is US-headquartered and subject to the US CLOUD Act, a jurisdictional risk assessment shall be documented, including encryption and key management arrangements and the provider's legal challenge commitments."),
    ]),

    ("Security Incident Management", [
        ("A.5.19-23-23", "Suppliers And Cloud Service Providers",
         "Suppliers and cloud service providers shall have a security incident management process in place."),
        ("A.5.19-23-24", "Supplier And Cloud Service Security",
         "Supplier and cloud service security incidents that impact confidential or personal information shall be reported to the organisation within the following timelines:."),
        ("A.5.19-23-25", "Be Documented As A Residual Risk",
         "Where a supplier cannot commit to the 12-hour timeline, this shall be documented as a residual risk with compensating controls (more frequent supplier reviews, enhanced monitoring, backup provider)."),
        ("A.5.19-23-26", "The Notification",
         "The notification shall include, at a minimum:."),
        ("A.5.19-23-27", "Supplier And Cloud Service Security",
         "Supplier and cloud service security incidents shall be managed as part of the organisation's incident management process, in accordance with the Incident Management Policy."),
        ("A.5.19-23-28", "The Organisation",
         "Where a supplier incident involves a personal data breach, the organisation shall assess notification obligations under nFADP (notification to the FDPIC as soon as possible) and, where applicable, GDPR Art. 33 (notification to the supervisory authority within 72 hours)."),
        ("A.5.19-23-29", "The Supplier'S Incident Management",
         "Where appropriate, the supplier's incident management process shall be followed in coordination with the organisation's own procedures."),
    ]),

    ("End of Contract", [
        ("A.5.19-23-30", "At The End Of The Contract",
         "At the end of the contract, the supplier or cloud service provider shall confirm in writing that it has met its contractual and legal obligations for the destruction of organisation confidential and personal information."),
        ("A.5.19-23-31", "Practicable, And Relevant (Acknowledging",
         "Where appropriate, practicable, and relevant (acknowledging limitations with cloud services), the following shall be completed:."),
    ]),

    ("Changes Cloud Service Supplier", [
        ("A.5.19-23-32", "Follow The Change Management Policy And",
         "Changes shall follow the Change Management Policy and change management process."),
        ("A.5.19-23-33", "Changes To Cloud Suppliers Are",
         "Changes to cloud suppliers are significant changes and shall not be taken lightly. Such changes shall be treated as a project with appropriate resources, risk management, project management, and stakeholder communication."),
        ("A.5.19-23-34", "Maintain An Exit Strategy For Each",
         "The organisation shall maintain an exit strategy for each Critical cloud service to ensure that a transition or exit can be executed in a controlled manner if required."),
        ("A.5.19-23-35", "Exit Strategies",
         "Exit strategies shall be reviewed annually or upon contract renewal."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.19-23
# =============================================================================
