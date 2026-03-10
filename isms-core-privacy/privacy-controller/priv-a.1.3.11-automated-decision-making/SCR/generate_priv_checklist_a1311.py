#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.1.3.11 — Automated Decision Making Compliance Checklist

Control A.1.3.11: Identifying and Addressing Obligations for Automated
                  Decision Making Based Solely on PII Processing
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Controller Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. ADM Identification (A.1.3.11) — 4 reqs
4. Obligations and Safeguards — 5 reqs
5. Transparency and Demonstrability — 4 reqs

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
DOCUMENT_ID = "PRIV-CHK-A.1.3.11"
CONTROL_ID = "A.1.3.11"
CONTROL_NAME = "Automated Decision Making"
SOURCE_POLICY = "PRIV-POL-A.1.3.11"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.1.3.11
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("ADM Identification", [
        ("A.1.3.11-01", "ADM Scope Identification",
         "The organisation shall identify and document all processing activities where decisions are made based solely on automated processing of PII (without meaningful human involvement) AND those decisions produce legal effects or similarly significant effects on data subjects."),
        ("A.1.3.11-02", "ADM Register",
         "The DPO shall maintain an ADM Register listing all in-scope automated decision-making activities. The register shall be updated whenever new ADM activities are deployed or existing ones are materially changed."),
        ("A.1.3.11-03", "DPO Approval for New ADM",
         "New ADM activities shall be notified to and approved by the DPO before deployment. Development and product teams shall flag ADM activities during product design, not after deployment."),
        ("A.1.3.11-04", "Special Category PII in ADM",
         "ADM activities that process special category PII require an Article 9(2) condition in addition to an Article 22 exception, explicit DPO approval, and in most cases a DPIA (per PRIV-POL-A.1.2.6-9)."),
    ]),

    ("Obligations and Safeguards", [
        ("A.1.3.11-05", "Obligations Identification",
         "For each ADM activity, the organisation shall identify and document: the right not to be subject to the decision (Article 22(1)); the applicable Article 22 exception (contract, law, or explicit consent); and safeguards required where an exception is invoked."),
        ("A.1.3.11-06", "Article 22 Exception Documentation",
         "Where an exception to Article 22 is invoked, the specific exception (necessary for contract, authorised by law, or explicit consent) shall be documented in the ADM Register with supporting evidence of the applicable exception."),
        ("A.1.3.11-07", "Human Review Right",
         "Where ADM produces significant effects and an Article 22 exception is invoked, a mechanism for data subjects to request human intervention shall be implemented — meaning a named person reviews the automated output before the decision is finalised or reconsidered."),
        ("A.1.3.11-08", "Point of View and Contestation",
         "Where ADM produces significant effects and an Article 22 exception is invoked, mechanisms for data subjects to express their point of view about the decision and to contest the automated decision shall be implemented and communicated to data subjects."),
        ("A.1.3.11-09", "Safeguards Communication",
         "Safeguards (human review, point of view, contestation) shall be communicated to data subjects in the privacy notice and upon the automated decision being communicated to them."),
    ]),

    ("Transparency and Demonstrability", [
        ("A.1.3.11-10", "Transparency Information",
         "For each ADM activity in scope, the transparency information provided to data subjects shall include: the existence of automated decision-making; meaningful information about the logic involved (at a level data subjects can understand); and the significance and envisaged consequences of such processing."),
        ("A.1.3.11-11", "Privacy Notice Coverage",
         "The organisation's privacy notice shall include ADM transparency information covering all in-scope ADM activities. The information shall be updated whenever the ADM activities or their logic changes materially."),
        ("A.1.3.11-12", "Demonstrability",
         "The organisation shall be able to demonstrate how it addresses its obligations for each ADM activity at any time, to supervisory authorities, data subjects, and certification auditors. The ADM Register and associated documentation (including DPIAs where conducted) are the primary demonstrability evidence."),
        ("A.1.3.11-13", "ADM Review",
         "ADM activities and their associated obligations documentation shall be reviewed at minimum annually, when the underlying processing or algorithm changes materially, and following any supervisory authority guidance on automated decision-making."),
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
