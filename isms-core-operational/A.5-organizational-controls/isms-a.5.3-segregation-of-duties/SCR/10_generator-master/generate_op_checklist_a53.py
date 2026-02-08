#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.3 — Segregation of Duties Compliance Checklist

Control A.5.3: Segregation of Duties
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Conflicting Duties Ident (7 reqs)
4. Small Team & SME Comp Controls (9 reqs)
5. Technical Segregation Controls (12 reqs)
6. Exception Management (6 reqs)
7. SoD Matrix Maintenance (3 reqs)
8. Compliance Measurement (2 reqs)

Total: 39 requirements across 6 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.3"
CONTROL_ID = "A.5.3"
CONTROL_NAME = "Segregation of Duties"
SOURCE_POLICY = "ISMS-OP-POL-A.5.3"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.3
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Conflicting Duties Ident", [
        ("A.5.3-01", "Maintain A Documented Sod Matrix",
         "The organisation shall maintain a documented SoD matrix identifying duty combinations that require segregation. The following categories provide the baseline:."),
        ("A.5.3-02", "The Following Duty Combinations",
         "The following duty combinations shall be segregated:."),
        ("A.5.3-03", "The Following Duty Combinations",
         "The following duty combinations shall be segregated:."),
        ("A.5.3-04", "The Following Duty Combinations",
         "The following duty combinations shall be segregated:."),
        ("A.5.3-05", "The Following Duty Combinations",
         "The following duty combinations shall be segregated:."),
        ("A.5.3-06", "Department Heads",
         "Department heads shall review the SoD matrix annually for their area and report any newly identified conflicts to the CISO. The CISO shall maintain the consolidated organisational SoD matrix in [GRC Tool] or equivalent register."),
        ("A.5.3-07", "> Where A Dedicated Grc Tool",
         "> Where a dedicated GRC tool is not yet deployed, the organisation shall maintain registers in controlled shared storage with version control, access logging, and quarterly integrity verification by the CISO."),
    ]),

    ("Small Team & SME Comp Controls", [
        ("A.5.3-08", "Where Segregation Cannot Be Fully",
         "Where segregation cannot be fully achieved due to limited personnel — a common situation in small and medium-sized organisations — compensating controls shall be implemented to provide equivalent risk mitigation."),
        ("A.5.3-09", "All Five Of The Following Compensating",
         "When full duty segregation is not feasible, all five of the following compensating controls shall be implemented for each identified conflict:."),
        ("A.5.3-10", "An Independent Party",
         "An independent party shall review the process quarterly at minimum. The review shall include:."),
        ("A.5.3-11", "Review Documentation*: Each Quarterly",
         "Review documentation*: Each quarterly review shall produce a written report documenting scope, findings, issues identified, and recommendations. Reports retained for 3 years."),
        ("A.5.3-12", "Issue Escalation*: Issues Identified",
         "Issue escalation*: Issues identified during independent review shall be escalated to the CISO within 5 business days and resolved within 30 calendar days."),
        ("A.5.3-13", "Compensating Control Arrangement",
         "Each compensating control arrangement shall be formally documented with:."),
        ("A.5.3-14", "Compensating Control Documentation",
         "Compensating control documentation shall be maintained in [GRC Tool] or an equivalent register accessible to the CISO and Internal Audit."),
        ("A.5.3-15", "Compensating Control Arrangements",
         "Compensating control arrangements shall be re-evaluated when:."),
        ("A.5.3-16", "The Effectiveness Of Compensating",
         "The effectiveness of compensating controls shall be verified through:."),
    ]),

    ("Technical Segregation Controls", [
        ("A.5.3-17", "Information Systems Supporting",
         "Information systems supporting segregated processes shall implement the following technical controls:."),
        ("A.5.3-18", "Role-Based Access Control (Rbac): Roles",
         "Role-based access control (RBAC): Roles shall be defined in the identity provider or application to enforce duty separation. Conflicting roles shall be documented as mutually exclusive."),
        ("A.5.3-19", "Mutual Exclusion Constraints: The Access",
         "Mutual exclusion constraints: The access control system ([Identity Provider / ERP / HR System]) shall prevent a single user from holding conflicting roles simultaneously. Where the system does not natively support mutual exclusion, a manual review shall be conducted at every access provisioning event."),
        ("A.5.3-20", "Workflow Controls: Multi-Step Business",
         "Workflow controls: Multi-step business processes shall require different authorised individuals at each approval stage. Self-approval shall be technically blocked where feasible and prohibited by policy in all cases."),
        ("A.5.3-21", "Privileged Access Management: Privileged",
         "Privileged access management: Privileged accounts shall be separate from standard accounts. No individual shall approve their own elevated access requests."),
        ("A.5.3-22", "Automated Systems: Mutual Exclusion",
         "Automated systems: Mutual exclusion constraints shall be tested annually by attempting to assign conflicting roles to a test user and verifying the system blocks the assignment. Test results documented."),
        ("A.5.3-23", "Manual Review Systems: Access",
         "Manual review systems: Access provisioning checklists shall include SoD conflict check with documented verification before access grant. Provisioner shall reference SoD matrix and confirm no conflicts."),
        ("A.5.3-24", "Quarterly Access Review: All User Role",
         "Quarterly access review: All user role assignments shall be compared against SoD matrix to detect any conflicts that bypassed provisioning controls. Findings resolved within 30 calendar days."),
        ("A.5.3-25", "Immutable Logging: All Activities In",
         "Immutable logging: All activities in segregated processes shall be logged to a centralised logging platform ([SIEM] or equivalent) that the process participants cannot modify or delete."),
        ("A.5.3-26", "Actor Identification: Logs",
         "Actor identification: Logs shall clearly identify the individual performing each action at every stage of the process."),
        ("A.5.3-27", "Timestamp And Action Recording: All",
         "Timestamp and action recording: All approvals, modifications, and process completions shall be recorded with accurate timestamps."),
        ("A.5.3-28", "Log Protection: Audit Logs",
         "Log protection: Audit logs shall be protected against modification or deletion per the Logging Policy. Acceptable implementations include write-once storage, restricted administrator access with separate log reviewer, retention locks, or centralised log aggregation with integrity verification."),
    ]),

    ("Exception Management", [
        ("A.5.3-29", "Exceptions To Segregation Requirements",
         "Exceptions to segregation requirements shall be managed through a formal process. Self-approval of segregation exceptions is never permitted."),
        ("A.5.3-30", "Full Review Within 24 Hours Of",
         "Full review within 24 hours of exception end — the CISO or delegate shall verify that compensating controls were effective and no irregularities occurred. Review sign-off documented."),
        ("A.5.3-31", "Emergency Exception Log*: All Emergency",
         "Emergency exception log*: All emergency exceptions shall be logged in the Exception Register with 'Emergency' flag."),
        ("A.5.3-32", "The Following Exceptions",
         "The following exceptions shall not be granted under any circumstances:."),
        ("A.5.3-33", "Be Recorded In The Exception Register",
         "All exceptions shall be recorded in the Exception Register maintained in [GRC Tool] or equivalent. Each record shall include:."),
        ("A.5.3-34", "The Ciso",
         "The CISO shall review the Exception Register monthly and report active exceptions to Executive Management quarterly."),
    ]),

    ("SoD Matrix Maintenance", [
        ("A.5.3-35", "The Organisational Sod Matrix",
         "The organisational SoD matrix shall be reviewed and updated annually. The review shall:."),
        ("A.5.3-36", "It Operations",
         "IT Operations shall generate access reports quarterly from the identity provider and application access systems. The CISO shall compare these reports against the SoD matrix to verify:."),
        ("A.5.3-37", "Be Documented And Conflicts Resolved",
         "Findings shall be documented and conflicts resolved within 30 calendar days of discovery."),
    ]),

    ("Compliance Measurement", [
        ("A.5.3-38", "The Following Metrics",
         "The following metrics shall be tracked and reported to the CISO quarterly:."),
        ("A.5.3-39", "Metrics Breaching Red Thresholds",
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.3
# =============================================================================
