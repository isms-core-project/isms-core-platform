#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.6.4-5 — Disciplinary Process and Employment Exit Compliance Checklist

Controls A.6.4-5: Disciplinary Process and Employment Exit
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Disciplinary Framework (14 reqs)
4. Employment Exit (14 reqs)
5. Compliance Measurement (1 reqs)

Total: 29 requirements across 3 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/A.0-checklist-engine/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_OP_ROOT / 'A.0-checklist-engine'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.6.4-5"
CONTROL_ID = "A.6.4-5"
CONTROL_NAME = "Disciplinary Process and Employment Exit"
SOURCE_POLICY = "ISMS-OP-POL-A.6.4-5"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.6.4-5
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Disciplinary Framework", [
        ("A.6.4-5-01", "The Disciplinary Process",
         "The disciplinary process shall be:."),
        ("A.6.4-5-02", "Proportionate — The Response",
         "Proportionate — the response shall match the severity of the violation and its consequences."),
        ("A.6.4-5-03", "The Following Five-Step Procedure",
         "The following five-step procedure shall be followed for all information security violations:."),
        ("A.6.4-5-04", "Be Collected In A Manner That",
         "Evidence shall be collected in a manner that respects the individual's rights under Swiss CO Art. 328 and nFADP. The chain of custody shall be documented."),
        ("A.6.4-5-05", "Step 4 — Investigation*: A Formal",
         "Step 4 — Investigation*: A formal investigation is conducted, including interviews with the individual concerned, witnesses, and relevant managers. The individual shall be informed of the nature of the allegations and given the opportunity to respond. For serious or gross misconduct cases, Legal Counsel shall be consulted."),
        ("A.6.4-5-06", "The Following Due Process Requirements",
         "The following due process requirements shall be observed in all disciplinary proceedings, in compliance with Swiss CO Art. 328 (employer's duty of care):."),
        ("A.6.4-5-07", "The Individual",
         "The individual shall be informed of the specific allegations in writing before any disciplinary hearing."),
        ("A.6.4-5-08", "The Individual",
         "The individual shall be given a reasonable opportunity to respond to the allegations, including time to prepare."),
        ("A.6.4-5-09", "The Individual",
         "The individual shall have the right to representation at disciplinary meetings (e.g., a colleague, trade union representative, or legal advisor, as permitted under applicable employment law)."),
        ("A.6.4-5-10", "An Appeals Process",
         "An appeals process shall be available:."),
        ("A.6.4-5-11", "Be Maintained Confidentially, With",
         "All documentation shall be maintained confidentially, with access restricted to those with a legitimate need to know."),
        ("A.6.4-5-12", "The Individual'S Personal Data Processed",
         "The individual's personal data processed during the investigation shall be handled in accordance with nFADP and the organisation's Privacy and Protection of PII Policy."),
        ("A.6.4-5-13", "The Information Security Team",
         "The Information Security Team shall be involved in disciplinary matters when:."),
        ("A.6.4-5-14", "Regulatory Notification*: Where A",
         "Regulatory notification*: Where a disciplinary matter involves a confirmed or suspected personal data breach, the organisation shall assess notification obligations:."),
    ]),

    ("Employment Exit", [
        ("A.6.4-5-15", "Be Revoked According To The Following",
         "Access shall be revoked according to the following timelines based on termination type:."),
        ("A.6.4-5-16", "Before Executing Immediate Dismissal,",
         "Before executing immediate dismissal, the following procedural safeguards shall be observed:."),
        ("A.6.4-5-17", "Compensating Controls When Sla Cannot Be",
         "Compensating controls when SLA cannot be met: If full revocation across all systems cannot be completed within the SLA, the following compensating controls shall be applied immediately* while full revocation is completed:."),
        ("A.6.4-5-18", "A Nonconformity Or Exception Record",
         "A nonconformity or exception record shall be created for any SLA breach, with root cause analysis and remediation tracked to closure per the corrective action process."),
        ("A.6.4-5-19", "Access Types",
         "All access types shall be addressed during the offboarding process:."),
        ("A.6.4-5-20", "Follow This Priority Order",
         "Where the departing individual holds privileged access, revocation shall follow this priority order:."),
        ("A.6.4-5-21", "Recover All Organisational Assets Upon",
         "The organisation shall recover all organisational assets upon termination or change of employment."),
        ("A.6.4-5-22", "Continuing Obligations",
         "Continuing obligations shall be communicated to the departing individual in writing before or on the last working day:."),
        ("A.6.4-5-23", "Organisational Information In The",
         "All organisational information in the individual's possession shall be returned or certified as destroyed."),
        ("A.6.4-5-24", "The Individual",
         "The individual shall confirm in writing that no organisational data has been retained on personal devices, personal cloud storage, or personal email accounts."),
        ("A.6.4-5-25", "Verification Of Data Return Or Deletion",
         "Verification of data return or deletion shall use the following lawful, risk-proportionate methods:."),
        ("A.6.4-5-26", "No Forced Inspection Of Personal Devices",
         "No forced inspection of personal devices: The organisation shall not compel inspection of personal devices without the individual's consent. Where consent is refused and risk is assessed as high, Legal Counsel shall advise on available remedies under Swiss law."),
        ("A.6.4-5-27", "A Security-Focused Exit Interview",
         "A security-focused exit interview shall be conducted for all departing personnel. The interview shall cover:."),
        ("A.6.4-5-28", "Exit Interviews",
         "Exit interviews shall be conducted by HR with input from the Information Security Team where the departing individual had access to Confidential or Restricted data, held privileged system access, or is departing under disciplinary circumstances."),
    ]),

    ("Compliance Measurement", [
        ("A.6.4-5-29", "Be Reported To The Ciso Monthly",
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.6.4-5
# =============================================================================
