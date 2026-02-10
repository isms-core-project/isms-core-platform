#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.32 — Change Management Compliance Checklist

Control A.8.32: Change Management
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Change Classification (2 reqs)
4. Change Request Process (5 reqs)
5. Change Advisory Board (CAB) (2 reqs)
6. Standard Change Catalogue (3 reqs)
7. Testing and Validation (11 reqs)
8. Implementation and Rollback (6 reqs)
9. Communication (1 reqs)
10. Emergency Changes (4 reqs)
11. Post-Impl Review (PIR) (1 reqs)
12. Change Freeze Periods (1 reqs)
13. Record Keeping & Documentation (3 reqs)
14. Configuration Mgmt Integration (3 reqs)
15. Unauthorised Changes (1 reqs)
16. Change-Incident Correlation (2 reqs)
17. Change Management Metrics (2 reqs)

Total: 47 requirements across 15 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/A.0-checklist-engine/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(_OP_ROOT / 'A.0-checklist-engine'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.8.32"
CONTROL_ID = "A.8.32"
CONTROL_NAME = "Change Management"
SOURCE_POLICY = "ISMS-OP-POL-A.8.32"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.32
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Change Classification", [
        ("A.8.32-01", "Be Classified Into One Of Three",
         "All changes shall be classified into one of three categories:."),
        ("A.8.32-02", "Changes That Fall Into Grey Areas",
         "Changes that fall into grey areas shall be escalated to the Change Manager for classification."),
    ]),

    ("Change Request Process", [
        ("A.8.32-03", "In-Scope Changes",
         "All in-scope changes shall be submitted as formal change requests in the change management system: [Specify: ServiceNow, Jira Service Management, Azure DevOps, or 'In selection; interim: ticketing system/spreadsheet']."),
        ("A.8.32-04", "Change Request",
         "Each change request shall include, at minimum:."),
        ("A.8.32-05", "Be Assessed For Impact Before",
         "All changes shall be assessed for impact before implementation:."),
        ("A.8.32-06", "Security Impact: Confidentiality,",
         "Security impact: Confidentiality, integrity, availability risks. Changes affecting systems that process personal data shall include an assessment of data protection impact."),
        ("A.8.32-07", "Approval Authority",
         "Approval authority shall be based on change risk level:."),
    ]),

    ("Change Advisory Board (CAB)", [
        ("A.8.32-08", "Establish A Change Advisory Board For",
         "The organisation shall establish a Change Advisory Board for review of normal and emergency changes."),
        ("A.8.32-09", "Records: Meeting Minutes",
         "Records: Meeting minutes shall be maintained for all CAB meetings, documenting date, attendees, changes reviewed, decisions, rationale, and action items. Minutes retained for 3 years."),
    ]),

    ("Standard Change Catalogue", [
        ("A.8.32-10", "Maintain A Standard Change Catalogue",
         "The organisation shall maintain a Standard Change Catalogue containing pre-approved, low-risk, routine changes."),
        ("A.8.32-11", "Catalogue Entry",
         "Each catalogue entry shall include:."),
        ("A.8.32-12", "Standard Changes",
         "Standard changes shall still be logged in the change management system for audit trail and incident correlation, even though CAB review is not required."),
    ]),

    ("Testing and Validation", [
        ("A.8.32-13", "Be Tested Before Deployment To",
         "Changes shall be tested before deployment to production:."),
        ("A.8.32-14", "Be Tested In Non-Production Environments",
         "Changes shall be tested in non-production environments (development, test/QA, staging) before production deployment."),
        ("A.8.32-15", "Non-Production Environments",
         "Non-production environments shall be logically or physically separated from production with separate credentials and access controls."),
        ("A.8.32-16", "Production Data",
         "Production data shall not be used in test environments without masking or anonymisation per the Information Classification and Handling Policy."),
        ("A.8.32-17", "Promotion From Test To Production",
         "Promotion from test to production shall require formal sign-off and verified test results."),
        ("A.8.32-18", "Production Changes",
         "Production changes shall be executed only by authorised personnel with the following controls:."),
        ("A.8.32-19", "Separation Of Duties: Developers",
         "Separation of duties: Developers shall not deploy their own changes to production without independent review and approval from a designated release manager, operations team member, or CAB."),
        ("A.8.32-20", "Multi-Factor Authentication",
         "Multi-factor authentication shall be required for production access."),
        ("A.8.32-21", "Privileged Access Management: Production",
         "Privileged access management: Production deployment accounts shall be separate from development accounts."),
        ("A.8.32-22", "Production Changes",
         "All production changes shall be audit-logged with user identity, timestamp, and change content."),
        ("A.8.32-23", "Exception*: In Organisations With Fewer",
         "Exception*: In organisations with fewer than 5 IT staff where full separation is not feasible, compensating controls shall include enhanced logging, CISO review of all production changes monthly, and peer review post-implementation."),
    ]),

    ("Implementation and Rollback", [
        ("A.8.32-24", "Be Implemented Following The Approved",
         "Changes shall be implemented following the approved implementation plan with:."),
        ("A.8.32-25", "Establish Preferred Change Windows To",
         "The organisation shall establish preferred change windows to minimise business disruption:."),
        ("A.8.32-26", "A Rollback Procedure",
         "A rollback procedure shall be agreed upon before implementing changes to production systems. Rollback shall be executed when:."),
        ("A.8.32-27", "For High And Critical Risk Changes",
         "For High and Critical risk changes, rollback procedures shall be:."),
        ("A.8.32-28", "Rollback Testing",
         "Rollback testing shall verify:."),
        ("A.8.32-29", "Destructive Changes), A Forward-Fix Plan",
         "Where rollback testing is not feasible (one-way migrations, destructive changes), a forward-fix plan shall be documented as an alternative to rollback."),
    ]),

    ("Communication", [
        ("A.8.32-30", "Affected Stakeholders",
         "Affected stakeholders shall be notified of changes, including:."),
    ]),

    ("Emergency Changes", [
        ("A.8.32-31", "Be Classified As Emergency Only When",
         "Changes shall be classified as emergency only when:."),
        ("A.8.32-32", "Emergency Classification",
         "Emergency classification shall not be used for convenience, poor planning, routine work, or desired features."),
        ("A.8.32-33", "Emergency Change Percentage",
         "Emergency change percentage shall be tracked monthly. Target: <5% of all changes."),
        ("A.8.32-34", "Emergency Change Abuse*: Using Emergency",
         "Emergency change abuse*: Using emergency classification inappropriately (convenience, poor planning) constitutes policy non-compliance and shall be escalated to the CISO."),
    ]),

    ("Post-Impl Review (PIR)", [
        ("A.8.32-35", "Post-Implementation Reviews",
         "Post-implementation reviews shall be conducted for:."),
    ]),

    ("Change Freeze Periods", [
        ("A.8.32-36", "Change Freeze Periods",
         "Change freeze periods shall be:."),
    ]),

    ("Record Keeping & Documentation", [
        ("A.8.32-37", "Complete Change Records",
         "Complete change records shall be maintained including:."),
        ("A.8.32-38", "Change Records",
         "Change records shall be retained for a minimum of 3 years for operational reference and 7 years for audit evidence."),
        ("A.8.32-39", "Following System Changes, The Following",
         "Following system changes, the following documentation shall be updated within 5 business days:."),
    ]),

    ("Configuration Mgmt Integration", [
        ("A.8.32-40", "Configuration Baselines",
         "Configuration baselines shall be updated following approved changes."),
        ("A.8.32-41", "Configuration Drift Detection (Actual",
         "Configuration drift detection (actual vs. baseline) shall trigger investigation and a corrective change request."),
        ("A.8.32-42", "The Configuration Management Database",
         "The configuration management database (CMDB) or equivalent inventory shall be the authoritative source for impact assessment (what systems are affected)."),
    ]),

    ("Unauthorised Changes", [
        ("A.8.32-43", "Unauthorised Changes — Changes Made",
         "Unauthorised changes — changes made without following the change management process — shall be:."),
    ]),

    ("Change-Incident Correlation", [
        ("A.8.32-44", "The Change Manager",
         "When a security incident or service outage occurs, the Change Manager shall:."),
        ("A.8.32-45", "The Catalogue Entry",
         "If the change was in the Standard Change Catalogue, the catalogue entry shall be reviewed and potentially reclassified or removed."),
    ]),

    ("Change Management Metrics", [
        ("A.8.32-46", "The Information Security Management Team",
         "The information security management team shall report change management metrics to the CISO at least quarterly:."),
        ("A.8.32-47", "Metrics Breaching Red Thresholds",
         "Metrics breaching red thresholds shall be escalated to the CISO for immediate attention and reported at the next Management Review."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.32
# =============================================================================
