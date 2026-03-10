#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.1.3.2-4 — Transparency and Information Provision Compliance Checklist

Controls A.1.3.2-4: Determining Obligations, Determining Information,
                     Providing Information to PII Principals
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Controller Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Obligations Identification (A.1.3.2) — 4 reqs
4. Information Content Determination (A.1.3.3) — 5 reqs
5. Information Provision (A.1.3.4) — 5 reqs

Total: 14 requirements across 3 domains
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
DOCUMENT_ID = "PRIV-CHK-A.1.3.2-4"
CONTROL_ID = "A.1.3.2-4"
CONTROL_NAME = "Transparency and Information Provision"
SOURCE_POLICY = "PRIV-POL-A.1.3.2-4"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.1.3.2-4
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Obligations Identification", [
        ("A.1.3.2-01", "Obligation Documentation",
         "The organisation shall determine and document its legal, regulatory, and business obligations to PII principals for each processing activity, including transparency obligations, rights obligations, breach notification obligations, and jurisdiction-specific obligations."),
        ("A.1.3.2-02", "Obligations Register",
         "The DPO shall maintain a PII Principal Obligations Register (part of the PLRR per PRIV-POL-A.3.13-16) that maps each applicable obligation to the relevant processing activities and describes how the organisation meets each obligation."),
        ("A.1.3.2-03", "Means to Meet Obligations",
         "The organisation shall provide the means to meet its obligations to PII principals, including operational processes for responding to data subject rights requests and providing required information at the point of collection."),
        ("A.1.3.2-04", "Obligations Review",
         "The PII Principal Obligations Register shall be reviewed at minimum annually, upon regulatory change, and when new processing activities commence, to ensure all applicable obligations are captured and met."),
    ]),

    ("Information Content Determination", [
        ("A.1.3.3-01", "Mandatory Information Elements — Direct Collection",
         "For PII collected directly from data subjects (GDPR Article 13), the organisation shall determine and document the mandatory elements to be provided at or before the time of collection, including: controller identity; DPO contact; purposes and legal basis; legitimate interests; recipients; third-country transfers and safeguards; retention period; data subject rights; right to withdraw consent; right to lodge a complaint; and automated decision-making information."),
        ("A.1.3.3-02", "Mandatory Information Elements — Indirect Collection",
         "For PII obtained indirectly (GDPR Article 14), the organisation shall determine the same information elements as direct collection, plus the source of the PII and whether it came from publicly available sources. This information shall be provided within 1 month of obtaining the PII, or at first communication with the data subject, or at time of disclosure — whichever is earliest."),
        ("A.1.3.3-03", "Timing Documentation",
         "The timing of information provision for each processing activity shall be documented. The organisation shall demonstrate that information is provided before or at the point of collection for direct collection activities."),
        ("A.1.3.3-04", "Content Review",
         "Privacy notice content shall be reviewed at minimum annually, when a processing activity changes, upon regulatory change affecting required information elements, and when supervisory authority guidance materially changes expectations."),
        ("A.1.3.3-05", "Version Control",
         "Privacy notices shall be version-controlled with effective dates maintained. Previous versions shall be retained for 3 years after version retirement to support demonstrability obligations."),
    ]),

    ("Information Provision", [
        ("A.1.3.4-01", "Format Requirements",
         "Information provided to PII principals shall be concise, transparent, intelligible, and easily accessible. It shall be provided free of charge and in plain language appropriate to the audience, including simpler language for children's processing."),
        ("A.1.3.4-02", "Accessibility",
         "Privacy information shall be published where data subjects will reasonably find it: privacy notice link on the website; in-app privacy information; and printed notice with physical collection. The full privacy notice shall be accessible at all times."),
        ("A.1.3.4-03", "Layered Notice",
         "The organisation shall maintain a full privacy notice accessible at all times (via website and on request), supplemented by shorter contextual notices at key data collection points that direct users to the full notice for complete details."),
        ("A.1.3.4-04", "Timing of Provision",
         "For online/digital direct collection, privacy information shall be provided at or before the point of collection. For physical collection, at time of collection. For employee PII, at commencement of employment. For indirect collection, within 1 month of obtaining the PII or at first communication — whichever is earliest."),
        ("A.1.3.4-05", "Collection Point Evidence",
         "The organisation shall maintain evidence of where and how privacy information is provided at each collection point, demonstrating timely provision to supervisory authorities on request."),
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
