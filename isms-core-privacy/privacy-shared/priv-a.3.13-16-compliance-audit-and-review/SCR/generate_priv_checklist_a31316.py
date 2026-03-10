#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.3.13-16 — Compliance, Audit and Review Compliance Checklist

Controls A.3.13-16: Legal and Regulatory Requirements (PII), Protection of Records (PII),
                    Independent Review of PIMS, Compliance Review
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Shared Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Legal Requirements and Records (A.3.13-14) — 6 reqs
4. Independent Review of PIMS (A.3.15) — 5 reqs
5. Ongoing Compliance Review (A.3.16) — 4 reqs

Total: 15 requirements across 3 domains
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
DOCUMENT_ID = "PRIV-CHK-A.3.13-16"
CONTROL_ID = "A.3.13-16"
CONTROL_NAME = "Compliance, Audit and Review"
SOURCE_POLICY = "PRIV-POL-A.3.13-16"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.3.13-16
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Legal Requirements and Records", [
        ("A.3.13-01", "Privacy Legal Requirements Register",
         "The organisation shall maintain a Privacy Legal Requirements Register (PLRR) documenting all legal, statutory, regulatory, and contractual requirements applicable to PII processing, the organisation's approach to meeting each requirement, current compliance status, and review dates. The PLRR is maintained by the DPO and classified CONFIDENTIAL."),
        ("A.3.13-02", "PLRR Currency",
         "The PLRR shall be reviewed at minimum annually and updated upon: enactment or amendment of applicable privacy legislation; new or material contract obligations involving PII; new processing activities that bring new regulatory obligations into scope; and DPA guidance or enforcement decisions that materially clarify obligations. Stale entries (unreviewd for more than 12 months) shall be treated as a compliance gap."),
        ("A.3.14-01", "Mandatory PII Processing Records",
         "The organisation shall create and maintain the following mandatory PII processing records: Record of Processing Activities (RoPA); consent records; DPIA documentation; DPO appointment records; supervisory authority notifications; data subject rights response records; processor agreements; International Transfer Register; Privacy Breach Register; training and acknowledgment records; PIMS internal audit reports; and PIMS management review records."),
        ("A.3.14-02", "Records Protection",
         "PII processing records shall be protected against loss or destruction (backups, defined retention periods); falsification (audit trails with identity and timestamp, prior version retention, DPO authorisation required for deletion); unauthorised access (classification controls per PRIV-POL-A.3.5-7); and unauthorised release (confidentiality controls). Records with regulatory significance shall be stored in systems that log all modifications."),
        ("A.3.14-03", "Record Retention Periods",
         "Mandatory retention periods shall be observed for all PII processing records. Minimum periods: RoPA, consent records, DPIA, transfer register — duration of processing plus 3 years; breach register, supervisory authority notifications — 5 years; DPO appointment record — duration of appointment plus 3 years; audit and management review records — 3 years."),
        ("A.3.14-04", "Supervisory Authority Access",
         "PII processing records shall be maintained in a secure manner and made available to supervisory authorities on request within the timeframe required by applicable law (GDPR Article 58; CH FADP Article 49). A process for responding to supervisory authority records requests shall be documented in the PIRP."),
    ]),

    ("Independent Review of PIMS", [
        ("A.3.15-01", "Independent Review Requirement",
         "The organisation shall conduct independent reviews of its PIMS — covering people, processes, and technologies related to PII processing — at planned intervals and when significant changes occur. The DPO may not conduct the independent review for PIMS functions they directly manage."),
        ("A.3.15-02", "Review Frequency",
         "Independent PIMS reviews shall occur at minimum annually (planned interval) and upon: major new processing activity; material change to organisational structure or processing infrastructure; significant regulatory change; or material privacy incident."),
        ("A.3.15-03", "Independence Requirement",
         "Independent reviews shall be conducted by reviewers who are independent of the operational functions responsible for PIMS implementation, have no conflict of interest in the review outcome, and have sufficient competence to assess PIMS controls and regulatory requirements. Acceptable approaches include: internal PIMS audit by the designated PIMS Internal Auditor; external audit by a third-party privacy auditor; or ISO/IEC 27701:2025 certification body audit."),
        ("A.3.15-04", "Review Scope",
         "Each independent review shall cover at minimum: policy and documentation completeness and currency; role assignments and competence evidence; evidence of PIMS operation (records per A.3.14); technical controls for PII processing; regulatory compliance status against the PLRR; and status of findings from previous reviews."),
        ("A.3.15-05", "Review Outputs",
         "Independent review outputs shall include a review report with findings, non-conformities, observations, and recommendations; formal presentation of findings to Executive Management; DPO response with remediation plan and timelines; and tracking of remediation to closure. Review reports are classified CONFIDENTIAL and retained for minimum 3 years."),
    ]),

    ("Ongoing Compliance Review", [
        ("A.3.16-01", "Compliance Review Programme",
         "The DPO shall maintain an ongoing compliance review programme covering: all 21 PIMS control group policies; the RoPA (currency and accuracy); processor agreement compliance; technical security control compliance for PII processing environments; and training and awareness completion rates."),
        ("A.3.16-02", "Review Frequency by Subject",
         "Minimum compliance review frequencies: RoPA accuracy — quarterly; processor agreement inventory — annually; technical controls compliance for PII systems — annually or upon significant system change; training and acknowledgment records — annually; PIMS policy compliance self-assessment per control group — annually."),
        ("A.3.16-03", "Compliance Review Outputs",
         "Compliance reviews shall produce: a written compliance assessment per review subject; a list of identified non-conformities or gaps; remediation actions with owner and target date; escalation to DPO for material compliance gaps; and reporting to Executive Management for systemic compliance issues. Compliance review records are retained for minimum 3 years."),
        ("A.3.16-04", "Non-Conformity Management",
         "Non-conformities identified through compliance review shall be documented, assigned an owner, and tracked to closure. Material non-conformities (those presenting significant regulatory risk or risk of harm to data subjects) shall be escalated to Executive Management and, where required, to the relevant supervisory authority as part of the organisation's accountability obligations."),
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
