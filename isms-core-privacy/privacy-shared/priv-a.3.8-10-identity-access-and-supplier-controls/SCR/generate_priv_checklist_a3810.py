#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.3.8-10 — Identity, Access and Supplier Controls Compliance Checklist

Controls A.3.8-10: Identity Management (PII), Access Rights (PII),
                   Supplier Agreements (PII)
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Shared Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Identity Lifecycle for PII Access (A.3.8) — 5 reqs
4. Access Rights Review (A.3.9) — 4 reqs
5. Supplier PII Agreements (A.3.10) — 4 reqs

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
DOCUMENT_ID = "PRIV-CHK-A.3.8-10"
CONTROL_ID = "A.3.8-10"
CONTROL_NAME = "Identity, Access and Supplier Controls"
SOURCE_POLICY = "PRIV-POL-A.3.8-10"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.3.8-10
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Identity Lifecycle for PII Access", [
        ("A.3.8-01", "Identity Provisioning",
         "Access identities for PII processing systems shall only be provisioned following formal authorisation by the Data Owner for the relevant PII dataset or the system owner for the relevant PII processing system. Provisioning requests shall document the business purpose, PII datasets to be accessed, and access level required."),
        ("A.3.8-02", "Access Principles",
         "Access to PII shall be granted on the basis of least privilege (minimum access needed for the job function) and need-to-know (processing purpose must be documented and legitimate). Privileged access to PII processing systems (admin, DBA, root) shall require separate privileged credentials and shall be restricted to the minimum number of individuals required."),
        ("A.3.8-03", "Access Modification",
         "Changes to PII access rights (expansion, reduction, role change) shall be formally authorised by the Data Owner and implemented within a documented timeframe. Expansion of access to RESTRICTED PII requires DPO notification in addition to Data Owner approval."),
        ("A.3.8-04", "Access Decommissioning",
         "PII access rights shall be revoked promptly when no longer required: upon termination of employment or contract (within 24 hours of effective date); upon role change where old access is no longer appropriate (within 5 business days); upon Data Owner instruction. Revocation shall be confirmed and documented."),
        ("A.3.8-05", "Identity Records",
         "A record of all identities with access to PII processing systems shall be maintained, including: identity, role, PII datasets/systems accessible, access level, date granted, and authorising Data Owner. Identity records shall be maintained for the duration of access plus 3 years."),
    ]),

    ("Access Rights Review", [
        ("A.3.9-01", "Periodic Access Review",
         "Access rights to PII processing systems shall be reviewed at minimum annually. For RESTRICTED PII systems, access reviews shall occur at minimum every 6 months. Reviews shall confirm that each identity's access remains appropriate, necessary, and authorised by a current Data Owner."),
        ("A.3.9-02", "Review Process",
         "Access reviews shall be conducted with Data Owner participation. Data Owners shall confirm or revoke each access entitlement in their domain. Unconfirmed access entitlements (Data Owner non-response after documented follow-up) shall be suspended as a precautionary measure pending confirmation."),
        ("A.3.9-03", "Review Outcomes",
         "Access review outcomes shall be documented: confirmed entitlements, revocations actioned, and exceptions noted with justification. Revocations identified during review shall be implemented within 5 business days of the review determination. Review records shall be retained for 3 years."),
        ("A.3.9-04", "Trigger-Based Review",
         "In addition to periodic reviews, PII access rights shall be reviewed upon: significant change to a user's role or responsibilities; material change to the PII processing system; privacy incident involving unauthorised PII access; or DPO request. Trigger-based reviews are documented separately from scheduled reviews."),
    ]),

    ("Supplier PII Agreements", [
        ("A.3.10-01", "Supplier Categorisation",
         "Suppliers (third parties providing services to the organisation) shall be categorised according to their PII access level before engagement: PII Processor (direct access to and processing of PII under instruction); PII-Adjacent (access to systems or environments where PII resides, but not direct PII processing); No PII Access. Categorisation determines the required agreement type and due diligence level."),
        ("A.3.10-02", "PII Processor Agreements",
         "Before a PII Processor supplier is engaged, a processor agreement meeting the requirements of GDPR Article 28 and PRIV-POL-A.2.2.2-7 (where the organisation acts as controller) shall be executed. The agreement shall be reviewed by the DPO before signing. No PII Processor supplier shall access PII without an executed agreement."),
        ("A.3.10-03", "PII-Adjacent Supplier Obligations",
         "PII-Adjacent suppliers shall be bound by a confidentiality agreement covering the PII environments they may access (per PRIV-POL-A.3.17-19), minimum security standards consistent with the organisation's PIMS, and an obligation to report any PII incident or suspected PII exposure immediately."),
        ("A.3.10-04", "Supplier Register and Due Diligence",
         "The DPO shall maintain a Supplier Register categorising all suppliers by PII access level. Due diligence appropriate to the supplier category shall be conducted before engagement and at least annually thereafter: security questionnaire and certification review for PII Processors; simplified review for PII-Adjacent. Due diligence records shall be retained for the duration of the engagement plus 3 years."),
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
