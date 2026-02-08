#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.37 — Documented Operating Procedures Compliance Checklist

Control A.5.37: Documented Operating Procedures
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Mandatory Documented Procedures (1 reqs)
4. Creating and Updating Procs (2 reqs)
5. Document Storage and Avail (4 reqs)
6. Version Control and Approval (3 reqs)
7. Procedure Review and Maint (3 reqs)
8. Procedure Documentation Metrics (2 reqs)
9. Records Management (6 reqs)
10. Training and Competence (5 reqs)

Total: 26 requirements across 8 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/SCR/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_OP_ROOT / 'SCR'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.5.37"
CONTROL_ID = "A.5.37"
CONTROL_NAME = "Documented Operating Procedures"
SOURCE_POLICY = "ISMS-OP-POL-A.5.37"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.37
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Mandatory Documented Procedures", [
        ("A.5.37-01", "Document Operating Procedures For The",
         "The organisation shall document operating procedures for the following categories:."),
    ]),

    ("Creating and Updating Procs", [
        ("A.5.37-02", "Operating Procedures",
         "All operating procedures shall include the following mandatory elements:."),
        ("A.5.37-03", "Be Created In Electronic Format Using",
         "Procedures shall be created in electronic format using standard, supported office applications or native operational systems. The organisation shall ensure appropriate identification and description (title, date, author, reference number), consistent format (language, software version, graphics), and review and approval for suitability and adequacy."),
    ]),

    ("Document Storage and Avail", [
        ("A.5.37-04", "Be Stored In The Organisation'S Document",
         "Procedures shall be stored in the organisation's document management system: [Specify: SharePoint, Confluence, Notion, or equivalent]."),
        ("A.5.37-05", "For Critical Services, The Organisation",
         "For critical services, the organisation shall maintain an offline pack containing, at minimum:."),
        ("A.5.37-06", "Be Verified Quarterly With A Recorded",
         "Currency shall be verified quarterly with a recorded checklist confirming version alignment with the authoritative repository."),
        ("A.5.37-07", "Annual Audit*: During Annual Internal",
         "Annual audit*: During annual internal audit, the offline pack shall be opened and verified against the authoritative repository (100% version match required)."),
    ]),

    ("Version Control and Approval", [
        ("A.5.37-08", "Only The Latest Approved Version",
         "Only the latest approved version shall be presented to users."),
        ("A.5.37-09", "Previous Versions",
         "Previous versions shall be archived (not deleted) for audit trail."),
        ("A.5.37-10", "Be Notified To Affected Personnel",
         "Updates shall be notified to affected personnel."),
    ]),

    ("Procedure Review and Maint", [
        ("A.5.37-11", "Personnel Using Procedures",
         "Personnel using procedures shall report:."),
        ("A.5.37-12", "Critical Procedures",
         "Critical procedures shall be tested at defined intervals:."),
        ("A.5.37-13", "Be Documented",
         "Testing shall be documented, including: test date and participants, test scenario, results (success/partial/failure), issues identified, and remediation actions."),
    ]),

    ("Procedure Documentation Metrics", [
        ("A.5.37-14", "Track The Following Procedure",
         "The organisation shall track the following procedure documentation metrics:."),
        ("A.5.37-15", "Metrics Breaching Targets",
         "Metrics breaching targets shall be escalated to the CISO and reported at the next Management Review."),
    ]),

    ("Records Management", [
        ("A.5.37-16", "Obsolete Documents And Records",
         "Obsolete documents and records shall be archived in line with data retention requirements:."),
        ("A.5.37-17", "Obsolete Documents And Records That Are",
         "Obsolete documents and records that are not required for audit and/or legal and regulatory purposes shall be securely deleted per the Information Classification and Handling Policy within 90 days of obsolescence determination."),
        ("A.5.37-18", "Documented Information Of External",
         "Documented information of external origin determined by the organisation to be necessary for the planning and operation of the Information Security Management System shall be identified and controlled (e.g., ISO standards, vendor documentation, regulatory guidance)."),
        ("A.5.37-19", "No Editing: External Documents",
         "No editing: External documents shall not be modified; annotations or summaries created as separate internal documents."),
        ("A.5.37-20", "Be Classified In Line With The",
         "Documents shall be classified in line with the Information Classification and Handling Policy."),
        ("A.5.37-21", "Classified Procedures",
         "Classified procedures shall be handled, stored, and transmitted according to their classification level. Confidential procedures shall have restricted access (role-based, need-to-know)."),
    ]),

    ("Training and Competence", [
        ("A.5.37-22", "Be Trained On Relevant Procedures Before",
         "Personnel shall be trained on relevant procedures before performing them independently."),
        ("A.5.37-23", "Training Records",
         "Training records shall be maintained."),
        ("A.5.37-24", "Be Verified Through Observation,",
         "Competence shall be verified through observation, assessment, or supervisor sign-off."),
        ("A.5.37-25", "Refresher Training",
         "Refresher training shall be provided when procedures are significantly updated."),
        ("A.5.37-26", "Cross-Training",
         "Cross-training shall be implemented for critical procedures to avoid single points of failure."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.37
# =============================================================================
