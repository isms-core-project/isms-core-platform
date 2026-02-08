#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.15-16-18 — Identity and Access Management Compliance Checklist

Controls A.5.15-16-18: Identity and Access Management
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Confidentiality Agreements (1 reqs)
4. Role-Based Access (1 reqs)
5. Unique Identifier (2 reqs)
6. Access Authentication (2 reqs)
7. Access Rights Review (3 reqs)
8. Privileged Accounts (3 reqs)
9. Service Accounts (8 reqs)
10. Passwords (1 reqs)
11. User Account Provisioning (5 reqs)
12. Leavers (3 reqs)
13. Authentication (2 reqs)
14. Remote Access (2 reqs)
15. Third-Party Remote Access (3 reqs)
16. Monitoring and Reporting (1 reqs)

Total: 37 requirements across 14 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.15-16-18"
CONTROL_ID = "A.5.15-16-18"
CONTROL_NAME = "Identity and Access Management"
SOURCE_POLICY = "ISMS-OP-POL-A.5.15-16-18"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.15-16-18
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Confidentiality Agreements", [
        ("A.5.15-16-18-01", "Employees And Contractors Who Are Given",
         "All employees and contractors who are given access to confidential information shall sign a confidentiality or non-disclosure agreement prior to being given access to information processing facilities."),
    ]),

    ("Role-Based Access", [
        ("A.5.15-16-18-02", "Implement Role-Based Access Control",
         "The organisation shall implement role-based access control (RBAC) as the preferred method for assigning access. Roles shall be documented and reviewed annually by business owners."),
    ]),

    ("Unique Identifier", [
        ("A.5.15-16-18-03", "Users Are Assigned A Unique Username",
         "Users are assigned a unique username or identifier on the principle of one user, one ID to ensure individual accountability. Usernames and identifiers shall not be shared between users."),
        ("A.5.15-16-18-04", "Shared Accounts Are Prohibited Except",
         "Shared accounts are prohibited except where technically unavoidable (legacy systems, vendor-required accounts). Any exception requires written CISO approval with documented business justification, compensating controls (individual user logging, quarterly review), and formal risk acceptance. Shared accounts shall be included in the privileged account register."),
    ]),

    ("Access Authentication", [
        ("A.5.15-16-18-05", "Multi-Factor Authentication (Mfa)",
         "Multi-factor authentication (MFA) shall be required for:."),
        ("A.5.15-16-18-06", "Systems Unable To Support Mfa",
         "Systems unable to support MFA shall be documented in the risk register with technical justification, compensating controls (e.g., network segmentation, enhanced monitoring), and CISO-approved risk acceptance reviewed annually."),
    ]),

    ("Access Rights Review", [
        ("A.5.15-16-18-07", "User Access To Systems",
         "User access to systems shall be reviewed periodically to ensure it is still appropriate and relevant:."),
        ("A.5.15-16-18-08", "Inactive And Dormant Accounts",
         "Inactive and dormant accounts shall be investigated. An account is considered inactive if it has not successfully authenticated within the specified period. Accounts inactive for more than 45 days shall be disabled. Accounts inactive for more than 90 days shall be removed unless a documented business justification exists."),
        ("A.5.15-16-18-09", "Service Accounts Are Excluded From",
         "Service accounts are excluded from inactivity-based disablement but shall be reviewed quarterly to verify they remain in active use and are still required. Unused service accounts shall be disabled immediately upon discovery."),
    ]),

    ("Privileged Accounts", [
        ("A.5.15-16-18-10", "Administrator Accounts",
         "Administrator accounts shall not be provided to users for standard tasks, including but not limited to laptops and mobile technology."),
        ("A.5.15-16-18-11", "Privileged And Administrator Users",
         "Where feasible, privileged and administrator users shall be assigned specific privileged accounts in addition to their normal account, for the specific use of completing privileged and administrator tasks."),
        ("A.5.15-16-18-12", "Privileged And Administrator Accounts",
         "Privileged and administrator accounts shall:."),
    ]),

    ("Service Accounts", [
        ("A.5.15-16-18-13", "Service Accounts (Non-Human Accounts",
         "Service accounts (non-human accounts used by applications, scripts, or automated processes) shall be managed according to the following requirements:."),
        ("A.5.15-16-18-14", "Service Account Creation",
         "Service account creation shall be approved by the system owner and CISO."),
        ("A.5.15-16-18-15", "Service Accounts",
         "All service accounts shall be documented with purpose, system/application, owner, and review date."),
        ("A.5.15-16-18-16", "Service Accounts",
         "Service accounts shall be granted only the minimum permissions required for their function."),
        ("A.5.15-16-18-17", "Service Accounts",
         "Service accounts shall not be used for interactive login by personnel."),
        ("A.5.15-16-18-18", "Service Account Credentials",
         "Service account credentials shall be stored in an approved secrets management solution, not hard-coded or stored in plaintext."),
        ("A.5.15-16-18-19", "Service Account Activity",
         "Service account activity shall be logged and monitored for anomalous behaviour."),
        ("A.5.15-16-18-20", "Service Accounts",
         "Service accounts shall be reviewed quarterly per the access review schedule."),
    ]),

    ("Passwords", [
        ("A.5.15-16-18-21", "Access To Systems And Information Is",
         "Access to systems and information is authenticated by passwords. The organisation shall enforce the following password standards:."),
    ]),

    ("User Account Provisioning", [
        ("A.5.15-16-18-22", "Account Creation, Modification, And",
         "Account creation, modification, and deletion shall be performed by authorised personnel and fully documented."),
        ("A.5.15-16-18-23", "Implement A Joiner-Mover-Leaver (Jml)",
         "The organisation shall implement a Joiner-Mover-Leaver (JML) process:."),
        ("A.5.15-16-18-24", "Business, System, Or Information Owners",
         "Business, system, or information owners shall approve access to systems and information. A documented request shall clearly indicate the required access and an authorisation record shall be maintained."),
        ("A.5.15-16-18-25", "Emergency Access (Break-Glass) May Be",
         "Emergency access (break-glass) may be granted by IT with CISO verbal approval and shall be formally documented within 1 business day."),
        ("A.5.15-16-18-26", "Users Requesting Password Resets Or",
         "All users requesting password resets or changes to authentication credentials shall have their identity verified using at least one of the following methods:."),
    ]),

    ("Leavers", [
        ("A.5.15-16-18-27", "Line Managers And Hr",
         "Line managers and HR shall inform the account provisioning team of a user's leave date."),
        ("A.5.15-16-18-28", "All Access",
         "When a user leaves the organisation, all access shall be revoked on the same business day, as a minimum to the main authentication technology, and to all systems and data recorded in the role-based access list."),
        ("A.5.15-16-18-29", "User Ids, Passwords, And Authentication",
         "User IDs, passwords, and authentication credentials of leavers shall not be reused."),
    ]),

    ("Authentication", [
        ("A.5.15-16-18-30", "The Main Access Authentication System",
         "The main access authentication system shall:."),
        ("A.5.15-16-18-31", "Validate The Log-On Information Only On",
         "Validate the log-on information only on completion of all input data. If an error condition arises, the system shall not indicate which part of the data is correct or incorrect."),
    ]),

    ("Remote Access", [
        ("A.5.15-16-18-32", "Remote Connections",
         "Remote connections shall be set to disconnect after a defined period of inactivity."),
        ("A.5.15-16-18-33", "A List Of Users With Remote",
         "A list of users with remote access to internal network systems shall be maintained and reviewed quarterly."),
    ]),

    ("Third-Party Remote Access", [
        ("A.5.15-16-18-34", "Be Granted For A Specific Time",
         "Access shall be granted for a specific time, to a specific system, to a specific individual, and provided on receipt of a formal, valid, authorised access request."),
        ("A.5.15-16-18-35", "Be Removed Immediately On Completion Of",
         "Access shall be removed immediately on completion of the requirement or contract end, whichever comes first."),
        ("A.5.15-16-18-36", "A List Of Third Parties And",
         "A list of third parties and individuals with access shall be maintained and reviewed quarterly."),
    ]),

    ("Monitoring and Reporting", [
        ("A.5.15-16-18-37", "Access To Systems",
         "Access to systems shall be monitored and reported. Actions that directly or indirectly affect or could affect the confidentiality, integrity, or availability of data shall be managed via the Incident Management process."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.15-16-18
# =============================================================================
