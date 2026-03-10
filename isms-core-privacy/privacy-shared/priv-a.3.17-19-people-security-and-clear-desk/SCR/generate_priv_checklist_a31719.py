#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.3.17-19 — Privacy Awareness, NDAs and Clear Desk Compliance Checklist

Controls A.3.17-19: Information Security Awareness and Training (PII),
                    Confidentiality and Non-Disclosure Agreements (PII),
                    Clear Desk and Clear Screen (PII)
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Shared Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Privacy Awareness and Training (A.3.17) — 5 reqs
4. Confidentiality and NDA Requirements (A.3.18) — 5 reqs
5. Clear Desk and Clear Screen (A.3.19) — 4 reqs

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
DOCUMENT_ID = "PRIV-CHK-A.3.17-19"
CONTROL_ID = "A.3.17-19"
CONTROL_NAME = "Privacy Awareness, NDAs and Clear Desk"
SOURCE_POLICY = "PRIV-POL-A.3.17-19"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.3.17-19
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Privacy Awareness and Training", [
        ("A.3.17-01", "Training Applicability",
         "The organisation shall provide appropriate privacy awareness, education, and training relevant to each personnel category: all personnel receive general privacy awareness annually; personnel with PII access receive PII handling training on engagement plus annual refresher; personnel with elevated PII responsibility receive role-specific training on appointment plus annually; contractors receive minimum general privacy awareness before PII access is granted."),
        ("A.3.17-02", "Privacy Awareness Content",
         "General privacy awareness content shall address at minimum: what PII is and the heightened sensitivity of special categories; the organisation's legal obligations under GDPR and CH FADP; the individual's role in protecting PII; how to recognise a PII incident and how to report it; data subject rights and how to escalate requests; and consequences of PII handling failures (regulatory and disciplinary)."),
        ("A.3.17-03", "Policy Update Notifications",
         "When a PIMS policy is substantially revised or a new policy is issued, affected personnel shall be notified of the change and its content relevant to their role, required to acknowledge the updated policy before its effective date, and provided with summary guidance where the policy change is material. Acknowledgment records shall be maintained per the Personnel Privacy Training and Acknowledgment Register."),
        ("A.3.17-04", "Training Records",
         "Training completion records shall be maintained per individual, including training module and version completed, date of completion, outcome, and next required refresher date. Training records shall be retained for the duration of employment plus 3 years."),
        ("A.3.17-05", "DPO Professional Development",
         "The DPO and privacy function shall receive ongoing professional development, including updates on regulatory developments, supervisory authority guidance, and changes to applicable privacy standards. Professional development activities and attendance shall be documented."),
    ]),

    ("Confidentiality and NDA Requirements", [
        ("A.3.18-01", "Who Must Sign",
         "The following persons and parties shall be bound by a signed confidentiality or non-disclosure obligation covering PII before access to PII is granted: employees (employment contract clause or separate NDA); contractors and consultants (contractor agreement clause or standalone NDA); temporary workers (staffing agency agreement or standalone NDA); PII processors (processor agreement per GDPR Article 28); professional advisors with PII access (engagement letter or NDA)."),
        ("A.3.18-02", "Minimum PII Content in Agreements",
         "Confidentiality or non-disclosure agreements covering PII shall address: the obligation to process PII only for authorised purposes and under instruction; prohibition on disclosure of PII to unauthorised parties; obligation to protect PII using at least the organisation's required security measures; obligation to report suspected PII incidents without undue delay; survival of confidentiality obligations post-engagement; and consequences of breach."),
        ("A.3.18-03", "Confidentiality Agreement Register",
         "The DPO shall maintain a Confidentiality Agreement Register recording: party identity, agreement type, date signed, PII scope covered, and next review date. No PII access shall be granted without a register entry confirming a current, signed agreement is in place."),
        ("A.3.18-04", "Agreement Review",
         "Agreements covering PII shall be reviewed at minimum every 3 years or upon: regulatory change affecting the obligations; significant change to the processing activities covered; material change to an individual's role. Agreements that are out of date shall be refreshed before continued PII access is permitted."),
        ("A.3.18-05", "DPO Professional Secrecy",
         "The DPO is bound by professional secrecy (GDPR Article 38(5)) with respect to the performance of their tasks. This obligation is in addition to and does not replace the general confidentiality obligations applicable to all personnel."),
    ]),

    ("Clear Desk and Clear Screen", [
        ("A.3.19-01", "Clear Desk Rules for PII",
         "PII documents shall not be left unattended on desks or in open areas; they shall be secured (in locked drawers, cabinets, or document safes) when a workspace is unoccupied. Special category PII documents require locked storage when unattended. PII documents awaiting destruction shall be placed in secure cross-cut shredding receptacles immediately upon completion of use — not in standard waste bins. In shared and hot-desk environments, PII documents must be cleared before vacating without exception."),
        ("A.3.19-02", "Clear Screen Rules for PII",
         "Workstations accessing PII shall lock automatically after a maximum idle period (configured per PRIV-IMP-A.3.17-19-TG). Personnel shall manually lock their screen before leaving a workstation unattended, even briefly. Screens displaying PII shall be positioned to minimise visibility to unauthorised persons; privacy screens shall be used in open-plan, public-facing, or shared environments where PII is routinely displayed."),
        ("A.3.19-03", "Meeting Room and Shared Display Controls",
         "PII shall not be projected or displayed in meeting rooms or on shared screens unless all attendees are authorised to view the PII. PII shall be closed or screened before external participants join a meeting. Shared display environments (screens, projectors) shall not cache or retain PII between sessions."),
        ("A.3.19-04", "Remote Working",
         "Clear desk and clear screen rules apply to remote working environments as fully as to office environments. PII documents used in remote working contexts shall be stored securely and not left visible to household members or others not authorised to access the PII. Personnel shall acknowledge remote working clear desk obligations, with acknowledgment records maintained."),
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
