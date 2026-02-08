#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.28 — Secure Coding Compliance Checklist

Control A.8.28: Secure Coding
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Secure Coding Standards (4 reqs)
4. Common Vulnerability Prevention (8 reqs)
5. Dependency and Library Mgmt (8 reqs)
6. Code Review Requirements (14 reqs)
7. Static App Sec Testing (SAST) (10 reqs)
8. Secure Coding Training (4 reqs)
9. Insecure Coding Practices (5 reqs)
10. Outsourced Development (12 reqs)
11. Sec Champion Programme (1 reqs)
12. Exception Management (3 reqs)

Total: 69 requirements across 10 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.28"
CONTROL_ID = "A.8.28"
CONTROL_NAME = "Secure Coding"
SOURCE_POLICY = "ISMS-OP-POL-A.8.28"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.28
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Secure Coding Standards", [
        ("A.8.28-01", "Establish And Maintain Documented Secure",
         "The organisation shall establish and maintain documented secure coding standards applicable to each programming language and framework in active use."),
        ("A.8.28-02", "The Development Manager",
         "The Development Manager shall maintain a register of approved languages and their associated secure coding references. At minimum:."),
        ("A.8.28-03", "The Development Manager",
         "Where a language is used that has no entry in this register, the Development Manager shall document the applicable secure coding reference before the language enters production use."),
        ("A.8.28-04", "Coding Standards Review*: Secure Coding",
         "Coding Standards Review*: Secure coding standards shall be reviewed annually, or when a new language or framework is adopted, or when a significant vulnerability class emerges that requires additional guidance."),
    ]),

    ("Common Vulnerability Prevention", [
        ("A.8.28-05", "Write Code That Prevents The",
         "Developers shall write code that prevents the vulnerability classes identified by the OWASP Top 10 and CWE/SANS Top 25. The following sections define mandatory coding practices for the most prevalent vulnerability categories."),
        ("A.8.28-06", "Input From External Sources",
         "All input from external sources shall be treated as untrusted and validated before processing."),
        ("A.8.28-07", "Output Rendered To Users Or External",
         "All output rendered to users or external systems shall be encoded to prevent injection attacks."),
        ("A.8.28-08", "Application Code Implementing",
         "Application code implementing authentication and session handling shall follow established secure patterns."),
        ("A.8.28-09", "Generate Session Identifiers Using",
         "Generate session identifiers using cryptographically secure random number generators. Session IDs shall be of sufficient length (minimum 128 bits of entropy)."),
        ("A.8.28-10", "Application Error Handling",
         "Application error handling shall prevent information disclosure and support security monitoring."),
        ("A.8.28-11", "Application Code That Implements Or Uses",
         "Application code that implements or uses cryptography shall follow the organisation's cryptographic policy."),
        ("A.8.28-12", "Application Code",
         "Application code shall enforce authorisation consistently."),
    ]),

    ("Dependency and Library Mgmt", [
        ("A.8.28-13", "Third-Party Libraries, Frameworks, And",
         "Third-party libraries, frameworks, and open source components introduce supply chain risk and shall be managed throughout their lifecycle."),
        ("A.8.28-14", "Maintain A Dependency Inventory For Each",
         "Maintain a dependency inventory for each application. All production applications shall maintain a Software Bill of Materials (SBOM) in CycloneDX or SPDX format, generated automatically via the build pipeline."),
        ("A.8.28-15", "Sca Scanning",
         "SCA scanning shall run on every build (CI/CD pipeline integration). Builds shall fail if critical or high-severity dependency vulnerabilities are detected and unresolved."),
        ("A.8.28-16", "Evaluate New Dependencies Before",
         "Evaluate new dependencies before adoption: check maintenance status, known vulnerabilities, licence compatibility, and community activity. Abandoned or unmaintained libraries shall not be introduced."),
        ("A.8.28-17", "Sbom Generation",
         "SBOM generation shall be standard practice for all applications, not limited to high-risk applications."),
        ("A.8.28-18", "Storage And Access: Sboms Stored In",
         "Storage and access: SBOMs stored in [Artifact Repository / Dependency Track / SBOM Platform], accessible to the Development Team, Security Team, Legal (for licence compliance), and Incident Response team. Each SBOM shall be tagged with the corresponding application version (1:1 relationship)."),
        ("A.8.28-19", "Timeline: All Production Applications",
         "Timeline: All production applications shall generate SBOMs by [Date — suggest 6 months from policy effective date]. Phased rollout: critical applications first (Month 1–3), then all production (Month 4–6)."),
        ("A.8.28-20", "Pinning Dependency Versions Ensures",
         "Pinning dependency versions ensures reproducible builds but creates staleness risk if versions are never updated. The organisation shall maintain a dependency update cadence to balance stability with security."),
    ]),

    ("Code Review Requirements", [
        ("A.8.28-21", "Code Changes",
         "All code changes shall be reviewed before merging to protected branches."),
        ("A.8.28-22", "The Number Of Reviewers And Their",
         "The number of reviewers and their qualifications shall be determined by the risk classification of the code change:."),
        ("A.8.28-23", "Qualifications: Security Champion",
         "Qualifications: Security Champion shall have completed Security Champion training."),
        ("A.8.28-24", "Approval: Both Reviewers",
         "Approval: Both reviewers shall approve before merge."),
        ("A.8.28-25", "Qualifications: Reviewer",
         "Qualifications: Reviewer shall understand infrastructure implications."),
        ("A.8.28-26", "Testing",
         "Testing: Shall include automated security tests (SAST passed, integration tests passed)."),
        ("A.8.28-27", "Security Champions",
         "Security Champions shall have dedicated time allocation for security reviews (10% of work time)."),
        ("A.8.28-28", "If Security Champion Unavailable:",
         "If Security Champion unavailable: Security Team shall provide review within 48 hours."),
        ("A.8.28-29", "Documentation: Pr Description",
         "Documentation: PR description shall state the review type required based on code classification (standard, security-critical, high-risk). CI/CD checks shall verify that the review approval count matches the requirement."),
        ("A.8.28-30", "The Code Author",
         "The code author shall not approve their own code (separation of duties)."),
        ("A.8.28-31", "Verify Adherence To The Organisation'S",
         "Reviewers shall verify adherence to the organisation's secure coding standards."),
        ("A.8.28-32", "Check For: Hard-Coded Secrets, Insecure",
         "Reviewers shall check for: hard-coded secrets, insecure coding patterns, missing input validation, missing output encoding, excessive permissions, inadequate error handling, and missing logging."),
        ("A.8.28-33", "Pull Requests",
         "Pull requests shall include a description of changes, link to the related issue or ticket, and evidence of testing."),
        ("A.8.28-34", "Be Completed Before The Code Is",
         "Reviews shall be completed before the code is merged to a protected branch."),
    ]),

    ("Static App Sec Testing (SAST)", [
        ("A.8.28-35", "Automated Static Analysis",
         "Automated static analysis shall be integrated into the development workflow to detect security defects before deployment."),
        ("A.8.28-36", "Deploy A Sast Tool ([Sast Tool]",
         "The organisation shall deploy a SAST tool ([SAST Tool] — e.g., SonarQube, Semgrep, CodeQL, Checkmarx, or equivalent) integrated into the CI/CD pipeline."),
        ("A.8.28-37", "Sast Scans",
         "SAST scans shall run on every pull request or merge request to a protected branch."),
        ("A.8.28-38", "Sast Results",
         "SAST results shall be reviewed before merging. Critical and high-severity findings shall block the merge until resolved or explicitly accepted as false positives with documented justification."),
        ("A.8.28-39", "Sast Rule Sets",
         "SAST rule sets shall cover, at minimum, the OWASP Top 10 and CWE/SANS Top 25 vulnerability classes."),
        ("A.8.28-40", "False Positives",
         "False positives shall be documented and suppressed following the suppression procedure below. Suppression without justification and peer review is prohibited."),
        ("A.8.28-41", "Sast Tool Configuration And Rule Sets",
         "SAST tool configuration and rule sets shall be reviewed annually by the Development Manager and Security Team."),
        ("A.8.28-42", "Peer Review Required: Another Developer",
         "Peer review required: Another developer OR Security Champion shall review the suppression request."),
        ("A.8.28-43", "Security Team Approval (For",
         "Security Team approval (for Critical/High findings): The Security Team shall approve suppression of Critical/High severity findings. Medium/Low findings may be approved by a peer reviewer."),
        ("A.8.28-44", "Quarterly Review: Security Team",
         "Quarterly review: Security Team shall sample 20% of suppressed findings."),
    ]),

    ("Secure Coding Training", [
        ("A.8.28-45", "Receive Training To Write Secure Code",
         "Developers shall receive training to write secure code effectively."),
        ("A.8.28-46", "Training Content*",
         "Training Content* shall cover, at minimum:."),
        ("A.8.28-47", "Training Evidence*: Completion Records",
         "Training Evidence*: Completion records shall be maintained in [HR System / LMS] and reviewed by the Development Manager quarterly."),
        ("A.8.28-48", "Training Requirements",
         "Training requirements shall be enforced through escalating consequences for non-compliance:."),
    ]),

    ("Insecure Coding Practices", [
        ("A.8.28-49", "The Prohibition On Hard-Coded Secrets In",
         "The prohibition on hard-coded secrets in the table above shall be enforced through automated detection at multiple layers."),
        ("A.8.28-50", "Blocks Commit If Secrets Detected",
         "Blocks commit if secrets detected (developer shall remove before re-commit)."),
        ("A.8.28-51", "Onboarding: All Developers",
         "Onboarding: All developers shall be instructed to install the pre-commit hook during onboarding."),
        ("A.8.28-52", "Fail If Secrets Are Detected (No",
         "Builds shall fail if secrets are detected (no merge until remediated)."),
        ("A.8.28-53", "Documentation: Secrets Detection Tool",
         "Documentation: Secrets detection tool configuration shall be maintained in [CI/CD Config Repository] and reviewed quarterly by the Security Team."),
    ]),

    ("Outsourced Development", [
        ("A.8.28-54", "Code Produced By External Contractors",
         "Code produced by external contractors and outsourced development teams shall meet the same secure coding standards as internally developed code."),
        ("A.8.28-55", "Require Adherence To The Organisation'S",
         "Contracts shall require adherence to the organisation's secure coding standards and this policy."),
        ("A.8.28-56", "Provide Evidence Of Secure Coding",
         "Contractors shall provide evidence of secure coding training for their developers."),
        ("A.8.28-57", "Contractor-Produced Code",
         "All contractor-produced code shall undergo the same code review and SAST scanning as internal code."),
        ("A.8.28-58", "Remediate Security Findings Within The",
         "Contractors shall remediate security findings within the organisation's defined SLAs."),
        ("A.8.28-59", "Contractor Code",
         "Contractor code shall be reviewed by an internal developer before merging."),
        ("A.8.28-60", "Sast And Sca Results For",
         "SAST and SCA results for contractor-produced code shall be visible to the organisation's Security Team."),
        ("A.8.28-61", "High-Risk Code Produced By Contractors",
         "High-risk code produced by contractors (authentication, authorisation, cryptography, data protection) shall receive a security-focused code review by a Security Champion or Security Architect."),
        ("A.8.28-62", "In Addition To Ongoing Code Review",
         "In addition to ongoing code review and scanning, the organisation shall conduct periodic audits of contractor-produced code to verify sustained quality and compliance."),
        ("A.8.28-63", "Poor Performance: 3 Consecutive Quarters",
         "Poor performance: 3 consecutive quarters below threshold shall trigger contract review and possible termination."),
        ("A.8.28-64", "Action: Contractors",
         "Action: Contractors shall address Critical/High recommendations within 90 days."),
        ("A.8.28-65", "Documentation: Contractor Audit Reports",
         "Documentation: Contractor audit reports shall be retained for contract duration + 3 years."),
    ]),

    ("Sec Champion Programme", [
        ("A.8.28-66", "Documentation: Security Champion",
         "Documentation: Security Champion Register shall be maintained in [HR System / Wiki] with names, teams, appointment dates, and training completion."),
    ]),

    ("Exception Management", [
        ("A.8.28-67", "Exceptions To This Policy",
         "Exceptions to this policy shall be requested in writing and shall include:."),
        ("A.8.28-68", "Be Approved By The Development Manager",
         "Exceptions shall be approved by the Development Manager and Information Security Manager (mandatory), plus the CISO for production application exceptions. All active exceptions shall be reviewed quarterly."),
        ("A.8.28-69", "Legacy Code Base That Cannot Be",
         "Where technically infeasible to meet a requirement (e.g., legacy code base that cannot be refactored immediately), compensating controls shall be implemented, documented, verified by the Information Security Manager, and reviewed annually."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.28
# =============================================================================
