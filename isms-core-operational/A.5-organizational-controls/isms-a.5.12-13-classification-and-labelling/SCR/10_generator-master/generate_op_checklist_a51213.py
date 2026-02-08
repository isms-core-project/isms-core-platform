#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.12-13 — Information Classification and Handling Compliance Checklist

Controls A.5.12-13: Information Classification and Handling
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Classification Scheme (6 reqs)
4. Information Labelling (2 reqs)
5. Information Handling (13 reqs)
6. Information Destruction (5 reqs)
7. Reclassification (2 reqs)

Total: 28 requirements across 5 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.12-13"
CONTROL_ID = "A.5.12-13"
CONTROL_NAME = "Information Classification and Handling"
SOURCE_POLICY = "ISMS-OP-POL-A.5.12-13"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.12-13
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Classification Scheme", [
        ("A.5.12-13-01", "Be Classified Into One Of Three",
         "Information shall be classified into one of three levels:."),
        ("A.5.12-13-02", "Default Classification: Information That",
         "Default classification: Information that has not been explicitly classified shall be treated as INTERNAL* until classified by its owner."),
        ("A.5.12-13-03", "Be Assigned When Information Is Created",
         "Classification shall be assigned when information is created or received."),
        ("A.5.12-13-04", "Be Reviewed When Information Is",
         "Classification shall be reviewed when information is significantly modified, shared with new parties, or when business circumstances change."),
        ("A.5.12-13-05", "Over-Classification",
         "Over-classification shall be avoided — classifying everything as CONFIDENTIAL dilutes the meaning and wastes resources."),
        ("A.5.12-13-06", "Aggregation Risk: Information That Is",
         "Aggregation risk: Information that is individually classified as INTERNAL may require reclassification to CONFIDENTIAL when combined with other datasets, if the aggregation creates a materially higher risk of harm (e.g., combining names with health conditions, or combining individual salary records into a department-wide compensation report). Information owners shall consider aggregation risk when classifying datasets."),
    ]),

    ("Information Labelling", [
        ("A.5.12-13-07", "Be Labelled According To Its",
         "All information shall be labelled according to its classification level:."),
        ("A.5.12-13-08", "Unmarked Information",
         "Unmarked information shall be treated as INTERNAL* by default."),
    ]),

    ("Information Handling", [
        ("A.5.12-13-09", "Organisation Information",
         "Organisation information shall not be stored on personal equipment, personal email accounts, or personal cloud storage unless approved by the CISO and recorded in an approved register."),
        ("A.5.12-13-10", "Organisation Information",
         "Organisation information shall be protected by access controls as defined in the Access Control Policy."),
        ("A.5.12-13-11", "Confidential Information",
         "Confidential information shall be encrypted at rest and in transit when stored on or transmitted through any system, in line with the Use of Cryptography Policy."),
        ("A.5.12-13-12", "Confidential And Internal Information",
         "Confidential and internal information shall not be stored or processed in development or test environments unless the data has been masked, anonymised, or pseudonymised. Where production data must be used in non-production environments, approval from the information owner and the CISO is required, and the data shall be handled at the same classification level as in production."),
        ("A.5.12-13-13", "Dlp Policies",
         "Where the organisation deploys Data Leakage Prevention (DLP) tools, DLP policies shall be aligned with the classification scheme to detect and prevent unauthorised transfer or disclosure of CONFIDENTIAL information (e.g., blocking external email of files labelled CONFIDENTIAL, preventing upload to unsanctioned cloud services)."),
        ("A.5.12-13-14", "Confidential Information Discussed",
         "Confidential information discussed verbally (in meetings, phone calls, or conversations) shall be handled with appropriate care:."),
        ("A.5.12-13-15", "Discussions Of Confidential Information",
         "Discussions of confidential information shall take place in private settings (closed offices, meeting rooms with closed doors) — not in open-plan areas, public spaces, or on public transport."),
        ("A.5.12-13-16", "Virtual Meetings Discussing Confidential",
         "Virtual meetings discussing confidential information shall use encrypted platforms with access restricted to authorised participants."),
        ("A.5.12-13-17", "Be Reminded Of The Confidential Nature",
         "Participants shall be reminded of the confidential nature of the discussion at the start of the meeting."),
        ("A.5.12-13-18", "Notes Or Minutes Of Confidential",
         "Notes or minutes of confidential discussions shall be classified and handled accordingly."),
        ("A.5.12-13-19", "Electronic And Paper Media",
         "All electronic and paper media containing confidential information shall be physically secured from unauthorised access by securing in locked drawers, cabinets, or restricted rooms."),
        ("A.5.12-13-20", "Removable Media (Usb Drives, External",
         "Removable media (USB drives, external drives, backup tapes) containing confidential data shall be encrypted and registered in the asset inventory, in line with the Asset Management Policy."),
        ("A.5.12-13-21", "Organisation Information",
         "Organisation information shall be backed up, retained, and tested in line with the backup schedule. Backups shall be encrypted using strong encryption. All backups shall be stored in secure locations with access restricted to authorised personnel."),
    ]),

    ("Information Destruction", [
        ("A.5.12-13-22", "Be Destroyed Securely According To Its",
         "When information is no longer required and its retention period has expired, it shall be destroyed securely according to its classification level."),
        ("A.5.12-13-23", "Logs Of The Wipe",
         "Logs of the wipe shall be maintained where the sanitisation tool supports it."),
        ("A.5.12-13-24", "Electronic Media And Devices That Have",
         "Electronic media and devices that have stored confidential or internal information shall be destroyed by approved methods when no longer required:."),
        ("A.5.12-13-25", "Destruction Of Confidential Media",
         "Destruction of confidential media shall be performed by approved specialist third-party suppliers where in-house destruction is not feasible. Certificates of destruction shall be obtained and retained as evidence."),
        ("A.5.12-13-26", "An Inventory Of Devices",
         "An inventory of devices, including those destroyed, shall be maintained in line with the Asset Management Policy."),
    ]),

    ("Reclassification", [
        ("A.5.12-13-27", "Information Classification Is Not",
         "Information classification is not permanent. Information shall be reclassified when:."),
        ("A.5.12-13-28", "Be Performed By The Information Owner",
         "Reclassification shall be performed by the information owner and the labelling updated accordingly."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.12-13
# =============================================================================
