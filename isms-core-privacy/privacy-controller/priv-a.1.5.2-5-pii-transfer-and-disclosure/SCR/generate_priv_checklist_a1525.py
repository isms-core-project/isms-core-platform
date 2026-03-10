#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.1.5.2-5 — PII Transfer and Disclosure Compliance Checklist

Controls A.1.5.2-5: Identify Basis for Cross-Border Transfer, Countries/Organisations,
                     Records of Transfer, Records of Disclosure to Third Parties
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Controller Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Transfer Basis Identification (A.1.5.2) — 4 reqs
4. Transfer Destinations (A.1.5.3) — 3 reqs
5. Transfer Records (A.1.5.4) — 4 reqs
6. Disclosure Records (A.1.5.5) — 3 reqs

Total: 14 requirements across 4 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 51-isms-core-privacy/00-checklist-engine/priv_checklist_engine.py
_PRIV_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(_PRIV_ROOT / '00-checklist-engine'))
from priv_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "PRIV-CHK-A.1.5.2-5"
CONTROL_ID = "A.1.5.2-5"
CONTROL_NAME = "PII Transfer and Disclosure"
SOURCE_POLICY = "PRIV-POL-A.1.5.2-5"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.1.5.2-5
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Transfer Basis Identification", [
        ("A.1.5.2-01", "Legal Basis Identification",
         "The organisation shall identify and document the legal basis for each transfer of PII to a third country or international organisation. No PII shall be transferred to a third country without a documented legal basis."),
        ("A.1.5.2-02", "Transfer Mechanisms",
         "Transfers shall be made under one of the approved mechanisms: adequacy decision (EU Commission or Swiss FDPIC); Standard Contractual Clauses (EU SCCs 2021 or Swiss FDPIC-approved SCCs); Binding Corporate Rules (DPA-approved BCRs for intra-group transfers); or Article 49 derogations for exceptional non-systematic cases."),
        ("A.1.5.2-03", "Transfer Impact Assessment",
         "Where SCCs or other contractual mechanisms are used, the DPO shall conduct a Transfer Impact Assessment (TIA) evaluating whether the destination country's legal framework provides essentially equivalent protection. TIA records shall be maintained in the International Transfer Register."),
        ("A.1.5.2-04", "Transfer Basis Review",
         "Transfer bases shall be reviewed when adequacy status changes, when SCCs are updated by the regulatory authority, and at minimum annually. Transfers that lose their legal basis shall cease until an alternative mechanism is established."),
    ]),

    ("Transfer Destinations", [
        ("A.1.5.3-01", "Transfer Country Register",
         "The DPO shall maintain a Transfer Country Register (as part of the RoPA) listing: country or international organisation; transfer mechanism and legal basis; categories of PII that may be transferred; relevant processing activities; and adequacy status or safeguard reference."),
        ("A.1.5.3-02", "Register Currency",
         "The Transfer Country Register shall be updated when new transfer destinations are identified, when adequacy status changes, and at minimum annually. Transfers to countries not listed in the register require DPO approval before commencement."),
        ("A.1.5.3-03", "RoPA Transfer Section",
         "The RoPA shall include for each processing activity the transfer destinations, transfer mechanisms, and safeguards. This is a mandatory RoPA element per GDPR Article 30(1)(e) and shall be maintained alongside the Transfer Country Register."),
    ]),

    ("Transfer Records", [
        ("A.1.5.4-01", "Transfer Record Content",
         "For each transfer of PII to or from a third party, the organisation shall record: date and time; identity of sending and receiving party; categories of PII transferred and approximate volume; legal basis; transfer mechanism (for cross-border transfers); and reference to the governing agreement."),
        ("A.1.5.4-02", "Third Party Cooperation Requirement",
         "The organisation shall require in its agreements with third parties that they cooperate with data subject rights requests involving PII that has been transferred, to the extent necessary to fulfil the organisation's obligations as controller."),
        ("A.1.5.4-03", "Transfer Record Retention",
         "Transfer records shall be retained for a minimum of 3 years and be accessible to the DPO for data subject rights fulfilment and supervisory authority requests."),
        ("A.1.5.4-04", "Rights Support",
         "Transfer records shall enable the organisation to: respond to data subject access requests with information on recipients; notify third parties of erasure or rectification obligations per PRIV-POL-A.1.3.5-10 (A.1.3.8); and demonstrate accountability to supervisory authorities."),
    ]),

    ("Disclosure Records", [
        ("A.1.5.5-01", "Disclosure Register",
         "The organisation shall maintain a Disclosure Register recording all disclosures of PII to third parties — including which PII was disclosed, to whom, and when. The Disclosure Register forms part of the broader RoPA. Records shall be retained for minimum 3 years."),
        ("A.1.5.5-02", "Disclosure Scope",
         "Disclosure records shall cover all communications of PII to third parties: routine disclosures under ongoing processor or supplier relationships; one-time disclosures (e.g. to advisors, auditors, regulators); and mandatory disclosures under legal obligation (e.g. to law enforcement, tax authorities)."),
        ("A.1.5.5-03", "Data Subject Rights Support",
         "Disclosure records shall support data subject access requests, as data subjects have the right to know the recipients or categories of recipients of their PII. The DPO shall be able to retrieve disclosure records for any individual data subject upon request."),
    ]),
])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 27701:2025"
    ))


# =============================================================================
# QA_VERIFIED: 2026-03-10
# QA_STATUS: PASSED
# QA_TOOL: Claude Code Production Scripts QA Methodology
# CHANGES: Initial generation for Privacy product launch
# =============================================================================
