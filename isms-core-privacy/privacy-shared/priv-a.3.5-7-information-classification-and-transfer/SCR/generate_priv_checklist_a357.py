#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.3.5-7 — Information Classification and Transfer Compliance Checklist

Controls A.3.5-7: Classification of Information (PII), Labelling of Information (PII),
                  Information Transfer (PII)
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Shared Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. PII Classification Requirements (A.3.5) — 4 reqs
4. PII Labelling (A.3.6) — 4 reqs
5. PII Transfer Controls (A.3.7) — 5 reqs

Total: 13 requirements across 3 domains
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
DOCUMENT_ID = "PRIV-CHK-A.3.5-7"
CONTROL_ID = "A.3.5-7"
CONTROL_NAME = "Information Classification and Transfer"
SOURCE_POLICY = "PRIV-POL-A.3.5-7"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.3.5-7
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("PII Classification Requirements", [
        ("A.3.5-01", "Classification Scheme for PII",
         "The organisation shall apply its information classification scheme to all PII, with PII-specific minimum classification floors: ordinary PII (any personal data as defined by GDPR/CH FADP) shall be classified at minimum CONFIDENTIAL; special category PII (health, biometric, racial/ethnic origin, etc.) and legally privileged PII shall be classified at minimum RESTRICTED."),
        ("A.3.5-02", "Classification Assignment",
         "PII shall be classified at the point of collection or creation. Data Owners are responsible for assigning and maintaining the classification of PII within their domain. Where PII is received from external parties, its classification shall be confirmed or assigned upon receipt before further processing."),
        ("A.3.5-03", "Classification Review",
         "PII classification shall be reviewed when the nature, purpose, or risk profile of the processing changes. Downgrading of classification (e.g., from RESTRICTED to CONFIDENTIAL) requires DPO approval and shall be documented. Anonymisation that renders data no longer PII requires DPO confirmation before reclassification."),
        ("A.3.5-04", "Handling Requirements by Classification",
         "Handling requirements (access, storage, transfer, disposal) shall be defined and enforced for each PII classification level. RESTRICTED PII requires the most restrictive handling controls across all lifecycle stages. CONFIDENTIAL PII requires controls that prevent unauthorised access but permits broader internal use with appropriate safeguards."),
    ]),

    ("PII Labelling", [
        ("A.3.6-01", "Labelling Obligation",
         "PII in electronic and physical form shall be labelled in accordance with the classification level assigned. Labels shall be clearly visible to users handling the information so that handling requirements are apparent. Where technical systems prevent explicit labelling, metadata or system-enforced controls shall substitute."),
        ("A.3.6-02", "PII Indicator",
         "In addition to the standard classification label, PII shall bear an indicator that identifies it as personal data subject to privacy obligations. The PII indicator (e.g., 'PII', 'Personal Data', or equivalent) shall be applied to documents, datasets, database fields, and system outputs that contain PII, so that personnel understand the privacy-specific handling obligations."),
        ("A.3.6-03", "Special Category Indicator",
         "Special category PII shall bear a specific indicator distinguishing it from ordinary PII (e.g., 'SPECIAL CATEGORY' or 'SENSITIVE PII'). This indicator shall trigger heightened handling requirements in accordance with the RESTRICTED classification floor."),
        ("A.3.6-04", "Labelling in Transfers",
         "When PII is transferred to third parties (sub-processors, customers, other organisations), the classification and PII indicator shall be communicated as part of the transfer, either via document labelling or transfer agreement terms. Receiving parties shall be notified of the classification and handling requirements."),
    ]),

    ("PII Transfer Controls", [
        ("A.3.7-01", "Internal Transfer Rules",
         "Transfers of PII between internal teams, departments, or systems shall be conducted on a need-to-know basis, limited to the minimum PII necessary for the receiving function's purpose. Internal transfers of RESTRICTED PII shall be logged, including sender, recipient, PII categories, and purpose."),
        ("A.3.7-02", "External Transfer Authorisation",
         "Transfers of PII to external parties shall be authorised. For CONFIDENTIAL PII, authorisation may be via existing processor agreement or documented business need. For RESTRICTED PII, transfer requires explicit Data Owner approval and DPO notification. All external transfers shall be recorded."),
        ("A.3.7-03", "Secure Transfer Methods",
         "The transfer method used for PII shall be commensurate with the classification level. RESTRICTED PII transfers shall use encrypted channels (e.g., TLS-protected API, encrypted secure file transfer, end-to-end encrypted messaging); unencrypted email transfer of RESTRICTED PII is prohibited. CONFIDENTIAL PII transfers shall use minimum TLS-encrypted channels for electronic transfer."),
        ("A.3.7-04", "Cross-Border Transfer Rules",
         "Transfers of PII outside the EEA or Switzerland require a lawful transfer mechanism (adequacy decision, SCCs, BCRs, or other approved mechanism). The transfer basis for each cross-border destination shall be documented in the Transfer Destination Register. No cross-border PII transfer shall commence without a documented and DPO-approved transfer basis."),
        ("A.3.7-05", "Transfer Records",
         "The organisation shall maintain records of external PII transfers sufficient to demonstrate compliance: date, recipient, PII categories transferred, transfer basis, and applicable customer or processing activity. Transfer records shall be maintained for 3 years."),
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
