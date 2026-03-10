#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.1.4.2-5 — Data Minimisation Compliance Checklist

Controls A.1.4.2-5: Limit Collection, Limit Processing, Accuracy and Quality,
                     PII Minimisation Objectives
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Controller Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Limit Collection (A.1.4.2) — 4 reqs
4. Limit Processing (A.1.4.3) — 4 reqs
5. Accuracy and Quality (A.1.4.4) — 5 reqs
6. Minimisation Objectives (A.1.4.5) — 4 reqs

Total: 17 requirements across 4 domains
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
DOCUMENT_ID = "PRIV-CHK-A.1.4.2-5"
CONTROL_ID = "A.1.4.2-5"
CONTROL_NAME = "Data Minimisation"
SOURCE_POLICY = "PRIV-POL-A.1.4.2-5"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.1.4.2-5
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Limit Collection", [
        ("A.1.4.2-01", "Collection Minimisation",
         "The organisation shall limit the collection of PII to the minimum that is relevant, proportional, and necessary for the identified purposes. 'Nice to have' data collection is not a valid justification."),
        ("A.1.4.2-02", "Field Justification",
         "Each data field collected shall be traceable to a specific documented purpose in the RoPA. Fields without a documented purpose shall not be collected."),
        ("A.1.4.2-03", "DPO Review of New Collection",
         "New data collection points (forms, APIs, integrations) require DPO review of the fields to be collected before deployment. Privacy by design (data minimisation as the default at design stage) shall be applied per GDPR Article 25."),
        ("A.1.4.2-04", "Collection Review",
         "Existing data collection points shall be reviewed at minimum annually to confirm that all fields collected remain necessary for documented purposes. Fields no longer necessary shall be removed."),
    ]),

    ("Limit Processing", [
        ("A.1.4.3-01", "Processing Access Restriction",
         "Access to PII for processing shall be restricted to personnel and systems with a documented processing purpose (minimum necessary principle). Role-based access controls shall enforce this restriction."),
        ("A.1.4.3-02", "Secondary Processing Assessment",
         "Secondary processing of PII for a purpose not identified at collection requires a purpose compatibility assessment (per PRIV-POL-A.1.2.2-5) and a new lawful basis where required. No secondary processing shall commence without DPO assessment."),
        ("A.1.4.3-03", "Analytics and Profiling",
         "Aggregation, profiling, or analytics that go beyond the documented purpose require DPO assessment before commencement. The assessment outcome shall be documented."),
        ("A.1.4.3-04", "Pseudonymisation Preference",
         "Where the processing purpose can be fulfilled with pseudonymised or anonymised data, the pseudonymised or anonymised version shall be used in preference to identifiable PII, particularly for testing, analytics, and research."),
    ]),

    ("Accuracy and Quality", [
        ("A.1.4.4-01", "Accuracy Requirement",
         "The organisation shall ensure that PII held and processed is as accurate, complete, and up to date as necessary for the processing purposes, throughout the lifecycle of the PII."),
        ("A.1.4.4-02", "Collection Validation",
         "Collection processes shall include reasonable validation measures to prevent the entry of obviously inaccurate data (e.g. date format validation, email format validation, range checks for numeric fields)."),
        ("A.1.4.4-03", "Update Mechanisms",
         "PII that is known to change over time shall have a defined review or update mechanism. Data subjects shall be given the means to update their own PII where technically feasible."),
        ("A.1.4.4-04", "Inaccuracy Correction",
         "Where inaccurate PII is identified — whether by the organisation or through a data subject rectification request — it shall be corrected without undue delay. The correction shall be documented."),
        ("A.1.4.4-05", "Enhanced Accuracy Controls",
         "PII used for significant decisions (financial, health, legal) shall have enhanced accuracy controls. The organisation shall not retain PII that has become inaccurate for purposes where accuracy is necessary, when the inaccuracy cannot be corrected."),
    ]),

    ("Minimisation Objectives", [
        ("A.1.4.5-01", "Documented Objectives",
         "The organisation shall define and document PII minimisation objectives covering: collection minimisation; processing minimisation; retention minimisation; de-identification for secondary use; and aggregation minimisation."),
        ("A.1.4.5-02", "De-identification Mechanisms",
         "The organisation shall document the de-identification mechanisms used to meet minimisation objectives, including pseudonymisation (reversible, still PII under GDPR) and anonymisation (irreversible, not PII where re-identification is not reasonably possible — confirmed by DPO)."),
        ("A.1.4.5-03", "Objectives Review",
         "PII minimisation objectives and mechanisms shall be reviewed at minimum annually, when new processing activities commence, and when regulatory guidance on minimisation changes."),
        ("A.1.4.5-04", "Objectives Demonstrability",
         "The organisation shall be able to demonstrate that minimisation objectives are being met in practice, through evidence of DPO reviews, RoPA field justifications, de-identification records, and collection point documentation."),
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
