#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.3.3-4 — Privacy Policy and Roles Compliance Checklist

Controls A.3.3-4: Information Security Policies for PII,
                  Information Security Roles and Responsibilities (PII)
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Shared Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. PIMS Policy Framework (A.3.3) — 5 reqs
4. Privacy Roles — Appointment and Accountability (A.3.4) — 6 reqs
5. Segregation and Independence (A.3.4) — 4 reqs

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
DOCUMENT_ID = "PRIV-CHK-A.3.3-4"
CONTROL_ID = "A.3.3-4"
CONTROL_NAME = "Privacy Policy and Roles"
SOURCE_POLICY = "PRIV-POL-A.3.3-4"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.3.3-4
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("PIMS Policy Framework", [
        ("A.3.3-01", "PIMS Policy Suite",
         "The organisation shall maintain a suite of information security policies covering all aspects of PII processing. The PIMS policy suite shall address all 21 control groups within the PIMS scope and shall be approved by Executive Management."),
        ("A.3.3-02", "Policy Owner and Review",
         "Each PIMS policy shall have a designated owner (the DPO for privacy-specific policies) and shall be reviewed at minimum annually and upon significant regulatory or organisational change. Out-of-date policies (unreviewd for more than 12 months) shall be treated as a compliance gap."),
        ("A.3.3-03", "Policy Communication",
         "All PIMS policies shall be communicated to all personnel and relevant interested parties. Personnel shall be required to acknowledge policies applicable to their role before accessing PII. Acknowledgment records shall be maintained per PRIV-POL-A.3.17-19."),
        ("A.3.3-04", "Policy Hierarchy",
         "The PIMS policy framework shall operate within a defined hierarchy: PRIV-POL-00 (Regulatory Applicability Framework) and PRIV-POL-01 (Governance Framework) sit above control-specific policies (PRIV-POL-A.x.x). Where policies conflict, the more restrictive requirement shall prevail."),
        ("A.3.3-05", "Privacy Registers",
         "The DPO shall maintain the core PIMS registers required to demonstrate compliance: Privacy Legal Requirements Register (PLRR), Confidentiality Agreement Register, Personnel Privacy Training and Acknowledgment Register, and any registers required by individual PIMS policies. Register templates and maintenance procedures are defined in PRIV-IMP-A.3.3-4-UG."),
    ]),

    ("Privacy Roles — Appointment and Accountability", [
        ("A.3.4-01", "DPO Appointment",
         "The organisation shall appoint a Data Protection Officer (DPO) with sufficient authority, resources, and independence to fulfil the role. The DPO appointment shall be documented and communicated internally and, where required by GDPR Article 37, notified to the supervisory authority. The DPO shall report directly to Executive Management."),
        ("A.3.4-02", "DPO Responsibilities",
         "The DPO shall be responsible for: informing and advising on data protection obligations; monitoring PIMS policy compliance; conducting privacy impact assessments; cooperating with supervisory authorities; and acting as first contact for data subjects and supervisory authorities. DPO responsibilities shall not create a conflict of interest with any other role held."),
        ("A.3.4-03", "Privacy Champions",
         "The organisation shall appoint Privacy Champions in each material business unit or function that processes PII. Privacy Champions serve as the DPO's operational contact point within their unit, assist with PIMS awareness, identify PII risks, and escalate privacy concerns to the DPO. Privacy Champion appointments shall be documented."),
        ("A.3.4-04", "Data Owners",
         "A Data Owner shall be assigned for each PII dataset or processing activity in the Record of Processing Activities (RoPA). Data Owners are accountable for the PII within their domain: defining access rights, approving PII use cases, and ensuring the dataset remains within policy bounds. Data Owner assignments shall be documented and reviewed at minimum annually."),
        ("A.3.4-05", "PIMS Internal Auditor",
         "The organisation shall designate a PIMS Internal Auditor role responsible for conducting independent reviews of PIMS implementation per PRIV-POL-A.3.13-16. The PIMS Internal Auditor shall be independent of the operational functions they audit and shall have sufficient competence to assess privacy controls."),
        ("A.3.4-06", "Security Roles with PII Responsibility",
         "The CISO and IT Security Team hold information security responsibilities that include PII-specific obligations. These roles shall implement and maintain technical controls for PII processing environments as specified in this policy series. Their PII responsibilities shall be documented in role descriptions and included in the PIMS governance framework."),
    ]),

    ("Segregation and Independence", [
        ("A.3.4-07", "DPO Independence",
         "The DPO shall not receive instructions from the organisation regarding the exercise of their data protection tasks. The DPO shall not be dismissed or penalised for performing their duties. Roles that would create a conflict of interest (such as determining purposes and means of PII processing) shall not be held concurrently with the DPO role."),
        ("A.3.4-08", "Segregation of Duties",
         "The organisation shall apply segregation of duties for sensitive PII processing operations, including: authorisation of new processing activities, approval of access rights, conduct of privacy impact assessments, and handling of data subject rights requests. No single individual shall be able to authorise and execute a sensitive PII operation without a second authorised party."),
        ("A.3.4-09", "Role Reviews",
         "All privacy role assignments (DPO, Privacy Champions, Data Owners, PIMS Internal Auditor) shall be reviewed at minimum annually to confirm: the role holder remains competent; the scope of the role remains current; no new conflicts of interest have arisen. Reviews shall be documented."),
        ("A.3.4-10", "Succession and Continuity",
         "The organisation shall have documented succession arrangements for the DPO role to ensure continuity of privacy governance in the event of absence or role change. At minimum, a named deputy DPO or temporary arrangement shall be identified and approved by Executive Management."),
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
