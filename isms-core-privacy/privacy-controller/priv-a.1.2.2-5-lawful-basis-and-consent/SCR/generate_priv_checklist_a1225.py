#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.1.2.2-5 — Lawful Basis and Consent Compliance Checklist

Controls A.1.2.2-5: Purpose Identification, Lawful Basis, Consent Process,
                     Consent Obtaining and Recording
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Controller Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Purpose Documentation (A.1.2.2) — 5 reqs
4. Lawful Basis Determination (A.1.2.3) — 6 reqs
5. Consent Process Design (A.1.2.4) — 5 reqs
6. Consent Obtaining and Recording (A.1.2.5) — 6 reqs

Total: 22 requirements across 4 domains
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
DOCUMENT_ID = "PRIV-CHK-A.1.2.2-5"
CONTROL_ID = "A.1.2.2-5"
CONTROL_NAME = "Lawful Basis and Consent"
SOURCE_POLICY = "PRIV-POL-A.1.2.2-5"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.1.2.2-5
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Purpose Documentation", [
        ("A.1.2.2-01", "Purpose Identification",
         "The organisation shall identify and document the specific, explicit, and legitimate purposes for which each category of PII is processed. Vague or generic purposes are not acceptable."),
        ("A.1.2.2-02", "RoPA Entry",
         "Each processing purpose shall be documented in the Record of Processing Activities (RoPA) with sufficient specificity to enable data subjects, lawful basis determination, and supervisory authority assessment."),
        ("A.1.2.2-03", "Purpose Limitation",
         "PII collected for a documented purpose shall not be processed for a different purpose unless fresh consent is obtained, a compatibility assessment confirms compatibility, or a new legal basis exists."),
        ("A.1.2.2-04", "Compatibility Assessment",
         "The DPO shall conduct and document a compatibility assessment before any secondary use of PII. Assessments shall be maintained in the Purpose Register as part of the RoPA."),
        ("A.1.2.2-05", "Purpose Review",
         "Documented purposes shall be reviewed at minimum annually as part of RoPA review, when a processing activity changes materially, and upon DPA guidance that affects how a purpose is interpreted."),
    ]),

    ("Lawful Basis Determination", [
        ("A.1.2.3-01", "Basis Determination",
         "The organisation shall determine, document, and be able to demonstrate the lawful basis for each processing purpose. No PII processing shall commence without a documented lawful basis."),
        ("A.1.2.3-02", "Basis Selection",
         "The lawful basis for each processing activity shall be selected from GDPR Article 6 (ordinary PII) and, where special category PII is involved, an additional condition from GDPR Article 9(2) shall be identified."),
        ("A.1.2.3-03", "Legitimate Interests Assessment",
         "Where legitimate interests (Article 6(1)(f)) is the lawful basis, the organisation shall conduct and document a Legitimate Interests Assessment (LIA) prior to commencing processing."),
        ("A.1.2.3-04", "RoPA Lawful Basis Record",
         "For each processing activity, the RoPA shall record: the primary lawful basis; for special category PII the Article 9(2) condition; for legitimate interests the LIA reference; for legal obligation the specific legal provision; and for consent the consent record reference."),
        ("A.1.2.3-05", "Demonstrability",
         "The organisation shall be able to demonstrate lawful basis compliance at any time. The DPO shall maintain documented evidence of each basis determination, including the reasoning and any supporting assessments."),
        ("A.1.2.3-06", "Basis Review",
         "Documented lawful basis determinations shall be reviewed when processing activities change materially, when legislation changes, or at minimum annually as part of RoPA review."),
    ]),

    ("Consent Process Design", [
        ("A.1.2.4-01", "Process Documentation",
         "Where consent is the lawful basis, the organisation shall determine and document a process by which it can demonstrate if, when, and how consent for the processing of PII was obtained from PII principals."),
        ("A.1.2.4-02", "Consent Validity",
         "Consent shall meet all validity conditions: freely given (no detriment for refusal); specific (separate per distinct purpose); informed (information per PRIV-POL-A.1.3.2-4 provided before consent); and unambiguous (positive opt-in — no pre-ticked boxes, silence, or inactivity)."),
        ("A.1.2.4-03", "Withdrawal Mechanism",
         "Data subjects shall be informed of their right to withdraw consent at any time, and withdrawal shall be as easy as giving consent. The withdrawal mechanism shall be documented as part of the consent process."),
        ("A.1.2.4-04", "Child Consent Process",
         "Where PII of children is processed on a consent basis, the consent process shall require parental or guardian consent, include proportionate age verification measures, and be approved by the DPO before deployment."),
        ("A.1.2.4-05", "Consent Process Review",
         "Documented consent processes shall be reviewed when the processing activity changes, when new consent mechanisms are deployed, and at minimum annually by the DPO."),
    ]),

    ("Consent Obtaining and Recording", [
        ("A.1.2.5-01", "Consent Obtaining",
         "The organisation shall obtain and record consent from PII principals according to the documented consent processes. Consent shall not be assumed or inferred from inaction."),
        ("A.1.2.5-02", "Consent Record Content",
         "For each consent-based processing activity, the consent record shall capture: identity of the PII principal; timestamp of consent; version of the consent statement presented; purposes for which consent was given; and channel or mechanism through which consent was obtained."),
        ("A.1.2.5-03", "Consent Record Protection",
         "Consent records shall be protected against loss and falsification per PRIV-POL-A.3.13-16, retained for the duration of the processing activity plus 3 years minimum, and accessible to the DPO for subject rights fulfilment and supervisory authority requests."),
        ("A.1.2.5-04", "Consent Withdrawal Action",
         "Upon withdrawal of consent, processing based solely on that consent shall cease without undue delay, PII shall be deleted or anonymised unless another lawful basis applies, and third parties shall be notified per PRIV-POL-A.1.3.5-10."),
        ("A.1.2.5-05", "Consent Refresh",
         "Where consent has become invalid (e.g. due to purpose change, long period of inactivity, or regulatory change), the organisation shall seek fresh consent or cease the processing activity."),
        ("A.1.2.5-06", "Supervisory Authority Demonstrability",
         "The organisation shall be able to demonstrate to the supervisory authority, on request, that consent was validly obtained for each consent-based processing activity by producing the consent record and documenting the process followed."),
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
