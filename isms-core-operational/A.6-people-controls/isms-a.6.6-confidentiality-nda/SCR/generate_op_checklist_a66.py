#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.6.6 — Confidentiality and Non-Disclosure Agreements Compliance Checklist

Control A.6.6: Confidentiality and Non-Disclosure Agreements
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. NDA Requirements (4 reqs)
4. Template Requirements (4 reqs)
5. Stakeholder-Specific Reqs (8 reqs)
6. Execution and Storage (4 reqs)
7. Periodic Review & Gap (4 reqs)
8. Post-Employment Obligations (4 reqs)
9. Compliance Measurement (1 reqs)

Total: 29 requirements across 7 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/A.0-checklist-engine/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(_OP_ROOT / 'A.0-checklist-engine'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.6.6"
CONTROL_ID = "A.6.6"
CONTROL_NAME = "Confidentiality and Non-Disclosure Agreements"
SOURCE_POLICY = "ISMS-OP-POL-A.6.6"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.6.6
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("NDA Requirements", [
        ("A.6.6-01", "No Person",
         "No person shall be granted access to the organisation's confidential information, systems, or facilities without a valid, signed confidentiality or non-disclosure agreement in place. NDAs shall be executed before access is granted — not retrospectively."),
        ("A.6.6-02", "Coverage Targets*: The Organisation",
         "Coverage targets*: The organisation shall achieve and maintain the following NDA coverage rates:."),
        ("A.6.6-03", "Be Executed According To The Following",
         "NDAs shall be executed according to the following timelines:."),
        ("A.6.6-04", "Be Legally Enforceable In The",
         "All NDAs shall be legally enforceable in the organisation's operating jurisdictions. Legal Counsel shall review and approve all NDA templates. NDAs shall reference:."),
    ]),

    ("Template Requirements", [
        ("A.6.6-05", "Maintain Six Standardised Nda Templates,",
         "The organisation shall maintain six standardised NDA templates, one for each stakeholder category:."),
        ("A.6.6-06", "Nda Templates",
         "All NDA templates shall include the following elements:."),
        ("A.6.6-07", "Nda Templates",
         "NDA templates shall be reviewed:."),
        ("A.6.6-08", "Upon A Trigger Event, Legal Counsel",
         "Upon a trigger event, Legal Counsel shall initiate review within 5 business days and record the review requirement in the NDA Template Register maintained in [Contract Management System]."),
    ]),

    ("Stakeholder-Specific Reqs", [
        ("A.6.6-09", "Employment Ndas",
         "Employment NDAs shall:."),
        ("A.6.6-10", "Contractor Ndas",
         "Contractor NDAs shall:."),
        ("A.6.6-11", "Vendor Ndas",
         "Vendor NDAs shall:."),
        ("A.6.6-12", "Data Processing Agreement (Dpa)",
         "Data Processing Agreement (DPA) requirements*: When a vendor will process personal data on behalf of the organisation, the Vendor NDA template shall include or reference a DPA covering the following elements (per nFADP Art. 9, GDPR Art. 28):."),
        ("A.6.6-13", "Mutual Ndas For Partners",
         "Mutual NDAs for partners shall:."),
        ("A.6.6-14", "Director/Advisor Ndas",
         "Director/Advisor NDAs shall:."),
        ("A.6.6-15", "Conflict Assessment",
         "Conflict assessment shall be performed at Director onboarding and annually thereafter (Chair + Legal Counsel)."),
        ("A.6.6-16", "Visitor Ndas",
         "Visitor NDAs shall:."),
    ]),

    ("Execution and Storage", [
        ("A.6.6-17", "Be",
         "NDAs shall be:."),
        ("A.6.6-18", "Executed Ndas",
         "Executed NDAs shall be:."),
        ("A.6.6-19", "Maintain A Register Of All Active",
         "The organisation shall maintain a register of all active NDAs. The register shall include:."),
        ("A.6.6-20", "The Nda Register",
         "The NDA Register shall be maintained in [Contract Management System] and reconciled quarterly against the personnel directory and active vendor/partner lists."),
    ]),

    ("Periodic Review & Gap", [
        ("A.6.6-21", "Periodic Reviews",
         "Periodic reviews shall assess:."),
        ("A.6.6-22", "Annual Review By Legal Counsel",
         "Annual review by Legal Counsel shall assess each template against the following criteria:."),
        ("A.6.6-23", "The Following Escalation",
         "When remediation timelines cannot be met, the following escalation shall apply:."),
        ("A.6.6-24", "Compensating Controls: If Access Cannot",
         "Compensating controls: If access cannot be immediately suspended pending NDA execution, documented compensating controls shall be implemented within 2 business days* of the deadline and reviewed weekly until the NDA is executed."),
    ]),

    ("Post-Employment Obligations", [
        ("A.6.6-25", "Confidentiality Obligations",
         "Confidentiality obligations shall survive the termination of employment, contract, or business relationship. Post-termination obligations shall be communicated to the departing individual in writing before or on the last working day, as part of the exit process (per A.6.4–5)."),
        ("A.6.6-26", "Maintain A Post-Termination Obligation",
         "The organisation shall maintain a Post-Termination Obligation Register for all departed personnel and ended third-party relationships. The register shall include:."),
        ("A.6.6-27", "The Register",
         "The register shall be:."),
        ("A.6.6-28", "Upon Obligation Expiration, The Record",
         "Upon obligation expiration, the record shall be archived in historical compliance records, retained per document retention policy (minimum 7 years from expiration), and removed from active monitoring."),
    ]),

    ("Compliance Measurement", [
        ("A.6.6-29", "Be Reported To The Ciso Monthly",
         "Metrics shall be reported to the CISO monthly and to the Management Review Team quarterly."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.6.6
# =============================================================================
