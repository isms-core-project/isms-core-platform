#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.2.5.7-9 — Sub-processor Management Compliance Checklist

Controls A.2.5.7-9: Disclosure of Sub-processors, Engaging Sub-processors,
                     Sub-processor Change Management
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Processor Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Sub-processor Disclosure (A.2.5.7) — 4 reqs
4. Sub-processor Engagement (A.2.5.8) — 5 reqs
5. Sub-processor Changes (A.2.5.9) — 4 reqs

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
DOCUMENT_ID = "PRIV-CHK-A.2.5.7-9"
CONTROL_ID = "A.2.5.7-9"
CONTROL_NAME = "Sub-processor Management"
SOURCE_POLICY = "PRIV-POL-A.2.5.7-9"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.2.5.7-9
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Sub-processor Disclosure", [
        ("A.2.5.7-01", "Pre-Engagement Disclosure",
         "Before commencing processing on behalf of a customer, the organisation shall disclose to the customer whether any sub-processors are used to process that customer's PII. No customer processing shall begin without this disclosure."),
        ("A.2.5.7-02", "Sub-processor Register",
         "The DPO shall maintain a Sub-processor Register listing all sub-processors engaged in PII processing on behalf of customers, including: name and contact details; location (country/jurisdiction); nature of processing; categories of PII processed; and applicable customers or services."),
        ("A.2.5.7-03", "Register Availability",
         "The Sub-processor Register shall be made available to customers as part of the processor agreement or as a publicly accessible list. Customers shall be notified of updates per A.2.5.9."),
        ("A.2.5.7-04", "Disclosure Documentation",
         "Disclosure of sub-processor use to customers shall be documented, including the date of disclosure, the sub-processors disclosed, and customer acknowledgment where applicable."),
    ]),

    ("Sub-processor Engagement", [
        ("A.2.5.8-01", "Customer Authorisation",
         "The organisation shall only engage a sub-processor to process customer PII in accordance with the customer contract — i.e., with the customer's specific or general written authorisation. No sub-processor shall be engaged without documented customer authorisation."),
        ("A.2.5.8-02", "Sub-processor Agreement Requirements",
         "Before engaging any sub-processor with access to customer PII, a sub-processor agreement shall be executed imposing the same data protection obligations as those in the organisation's processor agreement with the customer, including: processing only on instruction; appropriate security measures; confidentiality; breach notification; return or deletion of PII; and cooperation with audits."),
        ("A.2.5.8-03", "Due Diligence",
         "A security due diligence assessment of the sub-processor shall be conducted before engagement and periodically thereafter. Due diligence records shall be maintained for the duration of the engagement plus 3 years."),
        ("A.2.5.8-04", "Sub-sub-processor Restrictions",
         "Sub-processor agreements shall restrict the sub-processor from engaging further sub-sub-processors without the organisation's prior written consent, which in turn requires customer authorisation."),
        ("A.2.5.8-05", "Processor Liability",
         "The organisation remains fully liable to customers for the performance of sub-processors' obligations. Sub-processor non-compliance is treated as the organisation's non-compliance for the purposes of the customer contract."),
    ]),

    ("Sub-processor Changes", [
        ("A.2.5.9-01", "Change Notification Obligation",
         "Where the customer contract includes a general written authorisation for sub-processor engagement, the organisation shall notify customers of any intended addition or replacement of sub-processors in advance of the effective date, giving customers the opportunity to object."),
        ("A.2.5.9-02", "Notification Period",
         "The advance notification period for sub-processor changes shall be as specified in the processor agreement (typically minimum 30 days). The notification shall include the identity of the new or replacement sub-processor and the nature of processing to be performed."),
        ("A.2.5.9-03", "Objection Handling",
         "The organisation shall have a documented process for handling customer objections to sub-processor changes, which may include implementing alternative technical measures or allowing the customer to terminate the service without penalty. Objections and their outcomes shall be documented."),
        ("A.2.5.9-04", "Change Records",
         "All sub-processor changes and associated customer notifications, customer responses (objection or no-objection), and outcomes shall be maintained in the Sub-processor Change Register for 3 years."),
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
