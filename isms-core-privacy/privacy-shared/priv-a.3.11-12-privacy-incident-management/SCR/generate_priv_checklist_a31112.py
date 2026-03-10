#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.3.11-12 — Privacy Incident Management Compliance Checklist

Controls A.3.11-12: Planning and Preparation for Privacy Incident Management,
                    Assessment and Response to Privacy Incidents
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Shared Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Privacy Incident Response Planning (A.3.11) — 5 reqs
4. Privacy Incident Detection and Assessment (A.3.12) — 4 reqs
5. Breach Notification and Reporting (A.3.12) — 5 reqs

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
DOCUMENT_ID = "PRIV-CHK-A.3.11-12"
CONTROL_ID = "A.3.11-12"
CONTROL_NAME = "Privacy Incident Management"
SOURCE_POLICY = "PRIV-POL-A.3.11-12"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.3.11-12
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Privacy Incident Response Planning", [
        ("A.3.11-01", "Privacy Incident Response Plan",
         "The organisation shall maintain a documented Privacy Incident Response Plan (PIRP) that defines: the definition of a privacy incident; roles and responsibilities during an incident; the incident lifecycle (detect, contain, assess, notify, remediate, review); escalation paths; and communication protocols for supervisory authorities and data subjects."),
        ("A.3.11-02", "Severity Classification",
         "The PIRP shall define incident severity tiers. At minimum: Critical (large-scale RESTRICTED PII breach, likely significant harm to data subjects — e.g., medical data of 1,000+ individuals, financial fraud enabling data); High (RESTRICTED PII of any scale or CONFIDENTIAL PII of significant scale, likely harm to individuals); Medium (CONFIDENTIAL PII, limited scope, low individual harm risk); Low (internal breach, no external exposure, negligible individual harm risk). Severity tier determines response timeline and notification obligations."),
        ("A.3.11-03", "Breach Register",
         "The DPO shall maintain a Privacy Breach Register logging all confirmed privacy incidents, regardless of severity. Register entries shall include: incident date, detection date, nature of PII compromised, number of data subjects affected, categories of PII, cause, containment actions, notification status, and remediation outcome. The register shall be retained for minimum 5 years."),
        ("A.3.11-04", "Incident Response Team",
         "A Privacy Incident Response Team (PIRT) shall be designated, comprising at minimum: DPO (incident coordinator), CISO (technical lead), Legal/Compliance (notification and regulatory obligations), Communications (where data subject notification is required). PIRT members shall be familiar with the PIRP and trained in their incident roles."),
        ("A.3.11-05", "Reporting Obligation",
         "All personnel shall be trained and aware of their obligation to report suspected PII incidents immediately to the DPO (or Privacy Champion for first-line escalation). Personnel shall not attempt to independently resolve or conceal a suspected PII incident. Initial reports shall be made without undue delay upon suspicion — the 72-hour regulatory clock starts at the point the organisation becomes aware, not at confirmed breach."),
    ]),

    ("Privacy Incident Detection and Assessment", [
        ("A.3.12-01", "Incident Assessment",
         "Upon receipt of a privacy incident report, the DPO shall conduct an initial assessment within 24 hours to determine: whether a personal data breach (as defined by GDPR Article 4(12)) has occurred; the severity tier per PIRP criteria; whether notification obligations are triggered; and immediate containment actions required. Assessment shall be documented."),
        ("A.3.12-02", "Containment Actions",
         "Immediate containment actions shall be initiated upon confirmation of a privacy incident, proportionate to severity: access revocation for compromised accounts; isolation of affected systems; cessation of the processing activity causing the breach; notification to processors or sub-processors if the incident originates in their systems. Containment actions and timelines shall be documented."),
        ("A.3.12-03", "Root Cause Analysis",
         "Following containment, a root cause analysis (RCA) shall be conducted for all High and Critical incidents, and for any incident resulting in supervisory authority notification. The RCA shall identify the technical and procedural causes and propose remediation measures to prevent recurrence. RCA documentation shall be retained for 5 years."),
        ("A.3.12-04", "Post-Incident Review",
         "A post-incident review shall be conducted after closure of all High and Critical incidents. The review shall assess: effectiveness of the response; adequacy of the PIRP; lessons learned; and whether PIMS controls require updating. Review outcomes shall be presented to Executive Management and shall feed into the PIMS continual improvement programme."),
    ]),

    ("Breach Notification and Reporting", [
        ("A.3.12-05", "Supervisory Authority Notification",
         "Where a personal data breach is likely to result in a risk to the rights and freedoms of natural persons, the supervisory authority shall be notified without undue delay and within 72 hours of the organisation becoming aware of the breach (GDPR Article 33). Notification shall include the information required by Article 33(3): nature of breach, categories and approximate numbers of data subjects and records affected, DPO contact, likely consequences, and measures taken or proposed."),
        ("A.3.12-06", "Late Notification",
         "Where notification to the supervisory authority cannot be made within 72 hours, the notification shall be accompanied by reasons for the delay. The DPO shall document the reason for delay in the Breach Register. Late notification does not avoid the notification obligation — it must still be made as soon as practicable after the 72-hour window."),
        ("A.3.12-07", "Data Subject Notification",
         "Where a personal data breach is likely to result in a high risk to the rights and freedoms of natural persons, affected data subjects shall be notified without undue delay (GDPR Article 34). Notification shall use clear and plain language and shall describe: the nature of the breach; name and contact details of the DPO; likely consequences; and measures taken or proposed to address the breach and mitigate its effects."),
        ("A.3.12-08", "Processor Notification to Controller",
         "Where the organisation acts as a PII processor and becomes aware of a breach involving customer PII, the organisation shall notify the customer (PII controller) without undue delay and in the timeframe required by the processor agreement (typically within 24 hours of confirmed breach). Processor notification obligations do not replace the controller's own regulatory notification obligations."),
        ("A.3.12-09", "Notification Records",
         "All notifications made to supervisory authorities, data subjects, and customers (as controller or processor) shall be documented in the Breach Register, including: notification date and time, content of notification, recipient, and any responses received. Notification records shall be retained for minimum 5 years."),
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
