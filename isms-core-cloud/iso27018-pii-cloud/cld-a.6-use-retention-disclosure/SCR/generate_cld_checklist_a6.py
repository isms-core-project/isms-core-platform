#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-CHK-A.6 — Use, Retention and Disclosure Limitation Compliance Checklist

Controls A.6.1-A.6.2: PII Disclosure Notification,
                       Recording of PII Disclosures
Product: ISMS CORE Cloud (ISO/IEC 27018:2025 — Annex A)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Retention Limitation and Disclosure Notification (A.6 / A.6.1) — 5 reqs
4. Recording of PII Disclosures (A.6.2) — 4 reqs

Total: 9 requirements across 2 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 51-isms-core-privacy/00-checklist-engine/priv_checklist_engine.py
_REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_REPO_ROOT / '51-isms-core-privacy' / '00-checklist-engine'))
from priv_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "CLD-CHK-A.6"
CONTROL_ID = "A.6.1-2"
CONTROL_NAME = "Use, Retention and Disclosure Limitation"
SOURCE_POLICY = "CLD-POL-A.6"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-POL-A.6
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Retention Limitation and Disclosure Notification", [
        ("A.6-01", "Retention Schedule Adherence",
         "The organisation shall retain PII on behalf of controllers only for the duration specified in the service agreement. Where the service agreement does not specify a retention period, the organisation shall request explicit written instructions from the PII controller before implementing any retention configuration."),
        ("A.6-02", "Automated Retention Enforcement",
         "The organisation shall implement automated retention enforcement (automated deletion or archival) wherever technically feasible. Reliance on manual deletion is acceptable only where automated enforcement is technically not possible, in which case manual deletion shall be scheduled, logged, and reviewed quarterly."),
        ("A.6.1-01", "Prior Notification of Compelled Disclosure",
         "Where the organisation receives a legally binding request from a law enforcement agency, regulatory authority, court, or other governmental body requiring disclosure of PII belonging to a PII controller, the organisation shall notify the relevant PII controller prior to disclosure, including: the identity of the requesting authority (to the extent legally permissible); the categories and scope of PII requested; the legal basis cited; and the requested disclosure deadline. The controller shall be given a reasonable opportunity to seek legal challenge before disclosure where the deadline permits."),
        ("A.6.1-02", "Notification Prohibited by Law",
         "Where applicable law prohibits the organisation from notifying the PII controller of a disclosure request, the organisation shall: document the legal prohibition and the date from which notification is restricted; notify the PII controller at the earliest opportunity after the prohibition lapses; and if permanently prohibited, publish a transparency report or warrant canary to the maximum extent legally permissible."),
        ("A.6.1-03", "Minimum Disclosure Principle",
         "All legally compelled disclosures shall be limited to the minimum PII required to satisfy the legal obligation. The organisation shall not provide broader access or data sets than specifically required by the legal order. Where the scope of a legal order is ambiguous, legal advice shall be sought before responding."),
    ]),

    ("Recording of PII Disclosures", [
        ("A.6.2-01", "PII Disclosure Register",
         "The organisation shall maintain a PII Disclosure Register recording every disclosure of PII to a third party, including legally compelled disclosures. Each entry shall record: date of disclosure; recipient identity; categories of PII disclosed; approximate number of data subjects affected; legal basis or controller instruction authorising the disclosure; whether the PII controller was notified (and if not, reason and date of subsequent notification); and the authorising officer."),
        ("A.6.2-02", "Register Maintenance",
         "The PII Disclosure Register shall be maintained by the DPO, protected against unauthorised modification, and subject to quarterly review. The register shall be retained for minimum 5 years from the date of each recorded disclosure."),
        ("A.6.2-03", "Controller Access",
         "The PII Disclosure Register shall be made available to any PII controller upon request, restricted to records pertaining to that controller's PII. The organisation shall respond to controller register access requests within 5 business days."),
        ("A.6.2-04", "Transparency Reporting",
         "The organisation shall publish an annual transparency report summarising legally compelled disclosure requests received (where legally permissible), including aggregated counts of requests by type and jurisdiction, and the number of notifications issued to PII controllers. Where a warrant canary is maintained, it shall be updated at minimum every 6 months."),
    ]),
])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 27018:2025"
    ))


# =============================================================================
# QA_VERIFIED: 2026-03-10
# QA_STATUS: PASSED
# QA_TOOL: Claude Code Production Scripts QA Methodology
# CHANGES: Initial generation for Cloud product launch
# =============================================================================
