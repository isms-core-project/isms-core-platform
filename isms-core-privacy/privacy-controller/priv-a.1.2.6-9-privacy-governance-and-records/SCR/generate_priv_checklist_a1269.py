#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.1.2.6-9 — Privacy Governance and Records Compliance Checklist

Controls A.1.2.6-9: Privacy Impact Assessment, Processor Contracts,
                     Joint Controller Arrangements, Records of Processing
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Controller Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Privacy Impact Assessment (A.1.2.6) — 5 reqs
4. Processor Contracts (A.1.2.7) — 6 reqs
5. Joint Controller Arrangements (A.1.2.8) — 4 reqs
6. Records of Processing Activities (A.1.2.9) — 5 reqs

Total: 20 requirements across 4 domains
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
DOCUMENT_ID = "PRIV-CHK-A.1.2.6-9"
CONTROL_ID = "A.1.2.6-9"
CONTROL_NAME = "Privacy Governance and Records"
SOURCE_POLICY = "PRIV-POL-A.1.2.6-9"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.1.2.6-9
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Privacy Impact Assessment", [
        ("A.1.2.6-01", "DPIA Screening",
         "All new processing activities and material changes to existing activities shall undergo a DPIA screening by the DPO to determine whether a full DPIA is required. Screening decisions shall be documented."),
        ("A.1.2.6-02", "High-Risk Triggers",
         "A full DPIA is mandatory where processing is likely to result in high risk, including: systematic profiling with legal effects; large-scale special category processing; systematic monitoring of public areas; use of new technologies with large PII volumes; and any type on the supervisory authority's DPIA required list."),
        ("A.1.2.6-03", "DPIA Execution",
         "Full DPIAs shall be conducted in accordance with GDPR Article 35, describing processing operations, necessity and proportionality, risks to data subjects, and measures to address those risks."),
        ("A.1.2.6-04", "Residual High Risk",
         "A DPIA that identifies residual high risk after implementing risk-reduction measures requires prior consultation with the competent supervisory authority (GDPR Article 36), Executive Management approval, and documented risk acceptance or processing halt decision."),
        ("A.1.2.6-05", "DPIA Register",
         "DPIA results shall be documented and maintained in the DPIA Register. DPIAs shall be reviewed when processing changes materially or after a significant privacy incident involving the processing activity."),
    ]),

    ("Processor Contracts", [
        ("A.1.2.7-01", "Contract Requirement",
         "The organisation shall have a written contract with every PII processor it uses. No PII shall be transferred to an external processor without a current, signed processor agreement."),
        ("A.1.2.7-02", "Mandatory Contract Content",
         "Processor agreements shall address at minimum the obligations required by GDPR Article 28(3): processing only on documented instructions; personnel confidentiality; appropriate security measures; sub-processor restrictions; data subject rights assistance; security and breach notification assistance; return or deletion of PII at end of service; and cooperation with audits."),
        ("A.1.2.7-03", "ISO 27701 Table A.2 Reference",
         "Processor agreements shall also reference the appropriate controls from ISO/IEC 27701:2025 Table A.2, requiring the processor to implement controls equivalent to those in PRIV-POL-A.2.x."),
        ("A.1.2.7-04", "Sub-processor Controls",
         "The processor agreement shall require that sub-processors are engaged only with the organisation's prior written consent, and that the same data protection obligations as in the primary agreement are imposed on sub-processors."),
        ("A.1.2.7-05", "Processor Agreement Register",
         "The DPO shall maintain a Processor Agreement Register listing all active processor agreements with status, review date, and processor contact. No PII processor engagement commences without a register entry."),
        ("A.1.2.7-06", "Processor Due Diligence",
         "Prior to engaging a PII processor, the organisation shall conduct and document due diligence on the processor's technical and organisational security measures, confirming they are sufficient to meet GDPR Article 28(1) requirements."),
    ]),

    ("Joint Controller Arrangements", [
        ("A.1.2.8-01", "Arrangement Requirement",
         "Where the organisation jointly determines the purposes and means of PII processing with another controller, the organisation shall determine respective roles and responsibilities with that joint controller in a transparent arrangement before processing commences."),
        ("A.1.2.8-02", "Arrangement Content",
         "Joint controller arrangements shall determine: respective responsibilities for GDPR obligations (Article 26(1)); which controller provides privacy notices to data subjects; which controller is primary point of contact for data subject rights; data security responsibilities; and breach notification responsibilities."),
        ("A.1.2.8-03", "Data Subject Information",
         "The essence of the joint controller arrangement (i.e. which controller data subjects should contact and for what) shall be made available to data subjects, directly or by reference in the privacy notice."),
        ("A.1.2.8-04", "Review and Approval",
         "Joint controller arrangements require DPO and Legal/Compliance review before execution. Executed arrangements shall be maintained in the Joint Controller Arrangement Register."),
    ]),

    ("Records of Processing Activities", [
        ("A.1.2.9-01", "RoPA Requirement",
         "The organisation shall determine and securely maintain a Record of Processing Activities (RoPA) in support of its obligations as PII Controller for all processing of PII. The RoPA shall be available to supervisory authorities on request."),
        ("A.1.2.9-02", "RoPA Content",
         "The RoPA shall contain for each processing activity: name and contact details of the controller and DPO; purposes of the processing; categories of data subjects and PII; categories of recipients; third-country transfers and safeguards; retention periods; and description of technical and organisational security measures."),
        ("A.1.2.9-03", "Additional Records",
         "In addition to the RoPA, the organisation shall maintain: DPIA Register; Processor Agreement Register; Joint Controller Arrangement Register; consent records (per PRIV-POL-A.1.2.2-5); and LIA records (per PRIV-POL-A.1.2.2-5)."),
        ("A.1.2.9-04", "RoPA Maintenance",
         "The DPO shall own and maintain the RoPA. It shall be updated whenever a new processing activity commences, an existing activity changes materially, or a processing activity ceases."),
        ("A.1.2.9-05", "Records Protection",
         "All privacy records (RoPA, DPIA Register, Processor Agreement Register, consent records) shall be protected against loss, unauthorised access, and falsification in accordance with PRIV-POL-A.3.13-16."),
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
