#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.4 — Access to Source Code Compliance Checklist

Control A.8.4: Access to Source Code
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Repository Classification (5 reqs)
4. Role-Based Access Control (2 reqs)
5. Access Request and Approval (3 reqs)
6. Access Review & Deprovisioning (3 reqs)
7. Branch Prot and Code Review (7 reqs)
8. Secret Management (6 reqs)
9. Auth and Multi-Factor Auth (4 reqs)
10. Audit Logging and Monitoring (5 reqs)
11. Backup and Recovery (3 reqs)
12. Third-Party Access Management (4 reqs)
13. Exception Management (3 reqs)

Total: 45 requirements across 11 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.4"
CONTROL_ID = "A.8.4"
CONTROL_NAME = "Access to Source Code"
SOURCE_POLICY = "ISMS-OP-POL-A.8.4"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.4
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Repository Classification", [
        ("A.8.4-01", "Source Code Repositories",
         "All source code repositories shall be classified to determine appropriate protection levels."),
        ("A.8.4-02", "Repository Classification",
         "Repository classification shall be assigned by the repository owner during creation and reviewed annually. Classification shall be updated when the repository purpose changes."),
        ("A.8.4-03", "Inherited And Dormant Repositories*:",
         "Inherited and Dormant Repositories*: Repositories that are inherited (e.g., through acquisition, team restructuring, or developer departure) or dormant (no commits >12 months) shall be handled as follows:."),
        ("A.8.4-04", "Inherited Repositories: The Receiving",
         "Inherited repositories: The receiving team lead shall be assigned as interim repository owner within 5 business days. The repository shall be reviewed for classification accuracy, access permissions, and secret scanning compliance within 30 days."),
        ("A.8.4-05", "Dormant Repositories: Repositories With",
         "Dormant repositories: Repositories with no commit activity for 12 months shall be flagged for review. The repository owner shall confirm: (a) the repository is still needed (retain with current classification), (b) the repository should be archived (move to Archived classification, restrict to read-only), or (c) the repository should be deleted (follow data retention policy). Non-response after 30 days shall result in automatic archival with notification to the Development Manager."),
    ]),

    ("Role-Based Access Control", [
        ("A.8.4-06", "Repository Access",
         "Repository access shall be granted based on defined roles with the minimum permissions required."),
        ("A.8.4-07", "Admin Or Owner Access",
         "Admin or owner access shall not be granted to external contractors except in documented exceptional cases with CISO approval."),
    ]),

    ("Access Request and Approval", [
        ("A.8.4-08", "Repository Access Requests",
         "All repository access requests shall include:."),
        ("A.8.4-09", "Be Provisioned Within 24 Hours Of",
         "Access shall be provisioned within 24 hours of approval during business hours. Emergency access requests shall follow an expedited approval process with post-facto review within 48 hours."),
        ("A.8.4-10", "Access Requests And Approvals",
         "All access requests and approvals shall be documented and retained for a minimum of 3 years."),
    ]),

    ("Access Review & Deprovisioning", [
        ("A.8.4-11", "Repository Access",
         "Repository access shall be reviewed quarterly to confirm continued business justification."),
        ("A.8.4-12", "Repository Access",
         "Repository access shall be revoked within the same business day of employment termination, role change that removes the access need, or contract expiration."),
        ("A.8.4-13", "Be Verified Within 24 Hours Of",
         "Deprovisioning shall be verified within 24 hours of the trigger event."),
    ]),

    ("Branch Prot and Code Review", [
        ("A.8.4-14", "The Main Branch (Main/Master/Trunk) Of",
         "The main branch (main/master/trunk) of Production and Internal Tools repositories shall be protected."),
        ("A.8.4-15", "Release Branches (Release/, Hotfix/)",
         "Release branches (release/, hotfix/) shall have the same protection as the main branch."),
        ("A.8.4-16", "Only Repository Administrators",
         "Only repository administrators shall be able to modify branch protection rules. Temporary branch protection removal shall require documented justification, CISO approval, and automatic re-enablement after the specified period."),
        ("A.8.4-17", "Code Changes To Protected Branches",
         "All code changes to protected branches shall be submitted via pull requests."),
        ("A.8.4-18", "Pull Requests",
         "Pull requests shall not be approved by the code author (separation of duties)."),
        ("A.8.4-19", "Pull Requests",
         "Pull requests shall include a clear description of changes, link to related issue or ticket where applicable, and evidence of testing."),
        ("A.8.4-20", "Security-Relevant Changes",
         "Security-relevant changes shall include a security impact assessment."),
    ]),

    ("Secret Management", [
        ("A.8.4-21", "Source Code Repositories",
         "Source code repositories shall not contain passwords, API keys, tokens, private keys, database connection strings with embedded credentials, SSH private keys, encryption keys, or any other sensitive authentication material."),
        ("A.8.4-22", "Have Automated Secret Scanning Enabled",
         "All repositories shall have automated secret scanning enabled using [Secret Scanning Tool] (e.g., GitLeaks, TruffleHog, GitHub Secret Scanning, or equivalent)."),
        ("A.8.4-23", "Production Repositories",
         "Production repositories shall have pre-commit secret scanning enabled (blocking mode)."),
        ("A.8.4-24", "Secret Scanning",
         "Secret scanning shall detect generic secrets (regex-based patterns), provider-specific secrets (AWS keys, GitHub tokens, Azure credentials), and custom patterns defined by the security team."),
        ("A.8.4-25", "Include: (1) Immediate Rotation Of",
         "Remediation shall include: (1) immediate rotation of exposed secret, (2) removal from repository history if committed, (3) impact assessment (was the secret accessed by unauthorised parties?), and (4) incident reporting if required."),
        ("A.8.4-26", "Be Trained On Secret Management Best",
         "Developers shall be trained on secret management best practices, including use of environment variables, secrets management systems, and pre-commit hooks."),
    ]),

    ("Auth and Multi-Factor Auth", [
        ("A.8.4-27", "Access To Source Code Repositories",
         "Access to source code repositories shall be authenticated using approved methods: username/password (with MFA), SSH public key authentication, personal access tokens (with expiration), certificate-based authentication, or single sign-on (SSO) via the organisational identity provider."),
        ("A.8.4-28", "Multi-Factor Authentication",
         "Multi-factor authentication shall be required for:."),
        ("A.8.4-29", "Accepted Mfa Methods: Authenticator",
         "Accepted MFA methods: authenticator applications (e.g., Google Authenticator, Microsoft Authenticator, Authy), hardware security keys (e.g., YubiKey), or push notification to registered device. SMS-based codes are the least preferred method and shall only be used if other methods are unavailable."),
        ("A.8.4-30", "Service Accounts*: Service Accounts",
         "Service Accounts*: Service accounts cannot perform interactive MFA. Compensating controls shall include: tokens issued with minimum required scopes, token expiration enforced (maximum 1 year; 90 days recommended for high-privilege accounts), activity logged and monitored for anomalies, and quarterly review for continued need."),
    ]),

    ("Audit Logging and Monitoring", [
        ("A.8.4-31", "Repository Platforms",
         "Repository platforms shall log the following events:."),
        ("A.8.4-32", "Include: Timestamp (Utc), User Identity,",
         "Logs shall include: timestamp (UTC), user identity, source IP address, action performed, repository affected, and success or failure status."),
        ("A.8.4-33", "Be Tamper-Evident And Protected From",
         "Logs shall be tamper-evident and protected from unauthorised modification or deletion."),
        ("A.8.4-34", "Repository Access Logs",
         "Repository access logs shall be monitored for: multiple failed authentication attempts, access from unusual geographic locations, access outside normal business hours, bulk download operations, permission elevation attempts, force pushes to protected branches, and secret scanning alerts."),
        ("A.8.4-35", "Security Alerts",
         "Security alerts shall be generated and delivered to the security operations team within 15 minutes of detection. Critical events (confirmed unauthorised access, mass permission changes) shall trigger immediate incident response per the organisation's incident management process. Confirmed security incidents involving source code (unauthorised access, code tampering, intellectual property theft) shall be escalated to the CISO within 1 hour of confirmation. Where the incident involves customer data or production systems, the incident management process (A.5.24-28) shall be activated immediately."),
    ]),

    ("Backup and Recovery", [
        ("A.8.4-36", "Source Code Repositories",
         "All source code repositories shall be backed up to enable recovery from data loss, corruption, or platform failure."),
        ("A.8.4-37", "Include Source Code (All Branches,",
         "Backups shall include source code (all branches, commits, full history), repository metadata (permissions, settings, configurations), pull request history, and issue tracking data if integrated."),
        ("A.8.4-38", "Recovery Testing",
         "Recovery testing shall verify: repository restoration within RTO, data integrity (all commits, branches, history intact), permission restoration, and functionality of restored repository. Testing shall use a representative sample of repositories (minimum 3 Production repositories per quarter, rotating to cover all annually). Results shall be documented."),
    ]),

    ("Third-Party Access Management", [
        ("A.8.4-39", "Third-Party Developers, Contractors, And",
         "Third-party developers, contractors, and offshore development teams shall meet the following requirements before receiving repository access:."),
        ("A.8.4-40", "Code Contributions From Third Parties",
         "All code contributions from third parties shall require review by an internal developer (minimum one reviewer) and security review for security-relevant changes."),
        ("A.8.4-41", "Third-Party Access",
         "Third-party access shall be immediately revoked upon contract expiration, contract termination, security incident involving the third party, or repository owner request."),
        ("A.8.4-42", "Third-Party Access",
         "Third-party access shall be documented in a third-party access register with: contracting company, individual names, repositories accessed, contract dates, and project manager accountability."),
    ]),

    ("Exception Management", [
        ("A.8.4-43", "Exceptions To This Policy",
         "Exceptions to this policy shall be requested in writing and shall include:."),
        ("A.8.4-44", "Be Approved By The Repository Owner",
         "Exceptions shall be approved by the repository owner and Information Security Manager (mandatory), plus the CISO for Production repository exceptions. All active exceptions shall be reviewed quarterly."),
        ("A.8.4-45", "Compensating Controls",
         "Where technically infeasible to meet a requirement, compensating controls shall be implemented to achieve equivalent risk reduction, documented, verified by the Information Security Manager, and reviewed annually."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.4
# =============================================================================
