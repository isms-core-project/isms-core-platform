#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.1.3.5-10 — Data Subject Rights Compliance Checklist

Controls A.1.3.5-10: Consent Withdrawal, Right to Object, Access/Correction/Erasure,
                      Informing Third Parties, Copy of PII, Handling Requests
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Controller Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Consent Withdrawal Mechanism (A.1.3.5) — 4 reqs
4. Right to Object (A.1.3.6) — 4 reqs
5. Access, Correction and Erasure (A.1.3.7) — 5 reqs
6. Informing Third Parties (A.1.3.8) — 3 reqs
7. Copy of PII (A.1.3.9) — 2 reqs
8. Handling Requests (A.1.3.10) — 5 reqs

Total: 23 requirements across 6 domains
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
DOCUMENT_ID = "PRIV-CHK-A.1.3.5-10"
CONTROL_ID = "A.1.3.5-10"
CONTROL_NAME = "Data Subject Rights"
SOURCE_POLICY = "PRIV-POL-A.1.3.5-10"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.1.3.5-10
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Consent Withdrawal Mechanism", [
        ("A.1.3.5-01", "Withdrawal Mechanism",
         "The organisation shall provide PII principals with a mechanism to modify or withdraw their consent at any time. The mechanism shall be as easy to use as giving consent, clearly communicated in the privacy notice and at the point of consent, and effective without penalty or detriment."),
        ("A.1.3.5-02", "Processing Cessation",
         "Upon withdrawal of consent, processing based solely on that consent shall cease without undue delay. Where another lawful basis independently supports continued processing, the DPO shall assess applicability and document the basis continuation."),
        ("A.1.3.5-03", "PII Handling After Withdrawal",
         "After consent withdrawal, PII shall be deleted or anonymised unless a lawful basis for continued retention exists. The decision and basis shall be documented."),
        ("A.1.3.5-04", "Third Party Notification",
         "Third parties who received PII under the consent-based processing shall be notified of the consent withdrawal per the obligations in A.1.3.8 below."),
    ]),

    ("Right to Object", [
        ("A.1.3.6-01", "Objection Mechanism",
         "The organisation shall provide PII principals with an accessible mechanism to object to the processing of their PII. The mechanism shall be clearly communicated in the privacy notice and at the latest at the first communication with the data subject."),
        ("A.1.3.6-02", "Legitimate Interests Objection",
         "Where processing is based on legitimate interests or public task, a data subject's objection shall result in cessation of processing unless the organisation can demonstrate compelling legitimate grounds that override the data subject's interests, rights, and freedoms. A DPO assessment of compelling grounds shall be documented."),
        ("A.1.3.6-03", "Direct Marketing Objection",
         "Where PII is processed for direct marketing purposes, a data subject's objection shall result in immediate cessation of direct marketing processing. No compelling grounds assessment is required; the right is absolute."),
        ("A.1.3.6-04", "Objection Outcome Documentation",
         "The outcome of all objection assessments (cessation decision or compelling grounds determination) shall be documented in the Data Subject Rights Register and communicated to the data subject."),
    ]),

    ("Access, Correction and Erasure", [
        ("A.1.3.7-01", "Right of Access",
         "Upon a valid access request, the organisation shall provide: confirmation of whether PII is being processed; a copy of the PII; and supplementary information per GDPR Article 15(1) including purposes, categories, recipients, transfers, retention periods, rights, source, and automated decision-making information."),
        ("A.1.3.7-02", "Right to Rectification",
         "Upon a valid rectification request, the organisation shall correct inaccurate PII without undue delay. Where accuracy is disputed, the data subject may request restriction of processing pending resolution. Corrections shall be documented."),
        ("A.1.3.7-03", "Right to Erasure",
         "Upon a valid erasure request, the organisation shall erase PII where: it is no longer necessary for the purpose; consent is withdrawn and no other lawful basis applies; the data subject objects and there are no overriding grounds; processing was unlawful; or erasure is required by law."),
        ("A.1.3.7-04", "Erasure Refusal",
         "Erasure requests that cannot be fulfilled due to a countervailing legal obligation or other exemption shall receive a documented refusal with explanation and information about the right to complain to the supervisory authority."),
        ("A.1.3.7-05", "Right to Restriction",
         "Upon a valid restriction request (where accuracy is contested, processing is unlawful but deletion not wanted, retention needed for legal claims, or objection pending), the organisation shall restrict processing to storage only until the restriction condition resolves."),
    ]),

    ("Informing Third Parties", [
        ("A.1.3.8-01", "Third Party Notification Obligation",
         "Where PII has been disclosed to third parties and a data subject subsequently withdraws consent, objects, requests rectification, or requests erasure, the organisation shall inform each third party to whom the PII was disclosed of the relevant change or request."),
        ("A.1.3.8-02", "Disproportionate Effort Exception",
         "Where informing third parties proves impossible or involves disproportionate effort, the reason shall be documented. The data subject shall be informed of which third parties have been notified upon request."),
        ("A.1.3.8-03", "Third Party Notification Records",
         "Records of third party notifications shall be maintained for 3 years, including the identity of the third parties notified, the date of notification, and the content communicated."),
    ]),

    ("Copy of PII", [
        ("A.1.3.9-01", "Copy Provision",
         "Upon request, the organisation shall provide the data subject with a copy of their PII in a commonly used, machine-readable format (for portability requests under GDPR Article 20 where applicable) or in a generally accessible format."),
        ("A.1.3.9-02", "Fees",
         "The first copy of PII shall be provided free of charge. A reasonable administrative fee may be charged for subsequent copies, provided the data subject is informed of the fee before it is applied."),
    ]),

    ("Handling Requests", [
        ("A.1.3.10-01", "Request Procedures",
         "The organisation shall define and document policies and procedures for receiving, validating, and responding to all categories of data subject rights requests. These procedures shall be known to all personnel."),
        ("A.1.3.10-02", "Response Timeframes",
         "All data subject rights requests shall be acknowledged and responded to within one month of receipt. Where requests are complex or numerous, the period may be extended by a further two months — with notification to the data subject within the first month, including the reason for extension."),
        ("A.1.3.10-03", "Identity Verification",
         "Before fulfilling a rights request involving disclosure of PII, the organisation shall verify the identity of the requester with reasonable measures proportionate to the sensitivity of the PII. Identity verification shall not be unnecessarily burdensome."),
        ("A.1.3.10-04", "Manifestly Unfounded Requests",
         "Requests that are manifestly unfounded or excessive (including repetitive requests) may be refused. Refusals shall be documented with reasoning, and the data subject shall be informed of their right to complain to the supervisory authority."),
        ("A.1.3.10-05", "Data Subject Rights Register",
         "All rights requests shall be logged in the Data Subject Rights Register, recording: request type, receipt date, identity verification date, response date, outcome, and any extensions or refusals. The register shall be retained for 5 years."),
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
