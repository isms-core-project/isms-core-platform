#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.25-26-29 — Secure Development Lifecycle Compliance Checklist

Controls A.8.25-26-29: Secure Development Lifecycle
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Development Security Toolchain (2 reqs)
4. Environment Segregation (5 reqs)
5. Application Risk Classification (3 reqs)
6. Security Requirements (7 reqs)
7. Secure Coding Guidelines (5 reqs)
8. Code Repositories & Version (8 reqs)
9. Code Review (5 reqs)
10. CI CD Pipeline Security Gates (2 reqs)
11. Security Testing Requirements (16 reqs)
12. Vulnerability Remediation (5 reqs)
13. Test Data Protection (6 reqs)
14. Promoting Code to Production (7 reqs)
15. Outsourced Development (5 reqs)
16. Developer Security Training (5 reqs)

Total: 81 requirements across 14 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.25-26-29"
CONTROL_ID = "A.8.25-26-29"
CONTROL_NAME = "Secure Development Lifecycle"
SOURCE_POLICY = "ISMS-OP-POL-A.8.25-26-29"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.25-26-29
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Development Security Toolchain", [
        ("A.8.25-26-29-01", "Maintain An Approved Security Toolchain",
         "The organisation shall maintain an approved security toolchain integrated into the development lifecycle."),
        ("A.8.25-26-29-02", "The Toolchain",
         "The toolchain shall be reviewed annually by the Development Manager and CISO. Tool changes shall follow the change management process. All tools shall be maintained at current supported versions."),
    ]),

    ("Environment Segregation", [
        ("A.8.25-26-29-03", "Development, Test, And Production",
         "Development, test, and production environments shall be separated and shall not share common components, databases, or storage."),
        ("A.8.25-26-29-04", "Development, Test, And Production",
         "Development, test, and production environments shall be on separate networks or network segments."),
        ("A.8.25-26-29-05", "Be A Segregation Of Administrative",
         "There shall be a segregation of administrative duties between development/test and production environments. Personnel with write access to development repositories shall not have direct administrative access to production systems without separate authorisation."),
        ("A.8.25-26-29-06", "Not Flow From Production To Development",
         "Data shall not flow from production to development or test environments without explicit approval and appropriate sanitisation (see Test Data Protection section)."),
        ("A.8.25-26-29-07", "Configuration Of Environment Segregation",
         "Configuration of environment segregation shall be documented, and compliance shall be verified at least annually."),
    ]),

    ("Application Risk Classification", [
        ("A.8.25-26-29-08", "Be Classified By Risk Level To",
         "All applications shall be classified by risk level to determine the appropriate security requirements."),
        ("A.8.25-26-29-09", "Application Risk Classifications",
         "Application risk classifications shall be reviewed annually by the Development Manager and CISO."),
        ("A.8.25-26-29-10", "The Classification",
         "The classification shall be recorded in the application risk classification register."),
    ]),

    ("Security Requirements", [
        ("A.8.25-26-29-11", "Security Requirements",
         "Security requirements shall be specified for all applications based on risk classification."),
        ("A.8.25-26-29-12", "Recommended For Medium-Risk), The",
         "Where threat modelling is required (mandatory for High-Risk, recommended for Medium-Risk), the following process shall be followed:."),
        ("A.8.25-26-29-13", "Threat Models",
         "Threat models shall be reviewed and updated: at each major release; when the application architecture changes significantly; when new threat intelligence relevant to the application is identified; and at least annually for High-Risk applications."),
        ("A.8.25-26-29-14", "Security Requirements",
         "Security requirements shall address the following areas as a minimum*:."),
        ("A.8.25-26-29-15", "For Applications That Provide",
         "For applications that provide transactional services between the organisation and external parties, additional requirements shall address identity trust levels, integrity of exchanged information, non-repudiation, and confidentiality of transactions."),
        ("A.8.25-26-29-16", "Security Requirements Specifications",
         "Security requirements specifications shall follow a standardised template covering the following sections:."),
        ("A.8.25-26-29-17", "Security Requirements",
         "Security requirements shall be approved by the CISO (High-Risk) or Development Manager (Medium/Low-Risk) before development begins."),
    ]),

    ("Secure Coding Guidelines", [
        ("A.8.25-26-29-18", "Be Designed And Developed Based On",
         "Software shall be designed and developed based on industry-recognised secure coding guidelines, including:."),
        ("A.8.25-26-29-19", "Language-Specific Secure Coding",
         "Language-specific secure coding standards shall be documented and maintained for each programming language in active use. These shall cover, at a minimum:."),
        ("A.8.25-26-29-20", "Example — Python Secure Coding Standard*",
         "Example — Python Secure Coding Standard* (illustrative; each language shall have equivalent documentation):."),
        ("A.8.25-26-29-21", "Language-Specific Standards",
         "Language-specific standards shall be stored in the code repository (e.g., docs/secure-coding/ or equivalent), reviewed annually, and updated when new vulnerabilities or patterns emerge."),
        ("A.8.25-26-29-22", "Complete Secure Coding Training Before",
         "All developers shall complete secure coding training before being granted access to write production code (see Developer Security Training section)."),
    ]),

    ("Code Repositories & Version", [
        ("A.8.25-26-29-23", "Development Code",
         "Development code shall be stored in a secure code repository that enforces and meets the requirements of the Access Control Policy and segregation of duty."),
        ("A.8.25-26-29-24", "Repository Access",
         "Repository access shall follow the principle of least privilege:."),
        ("A.8.25-26-29-25", "Be Granted Based On Project Assignment",
         "Access shall be granted based on project assignment and role."),
        ("A.8.25-26-29-26", "Repository Access",
         "Repository access shall be reviewed at least annually, aligned with identity and access management reviews."),
        ("A.8.25-26-29-27", "Former Team Members",
         "Former team members shall have access revoked within the same business day of departure."),
        ("A.8.25-26-29-28", "Code Repositories",
         "Code repositories shall enforce:."),
        ("A.8.25-26-29-29", "Secret Scanning",
         "Secret scanning shall detect, at a minimum: API keys, access tokens, private keys, database connection strings, cloud provider credentials, and webhook URLs."),
        ("A.8.25-26-29-30", "Hardcoded Secrets In Source Code Are",
         "Hardcoded secrets in source code are prohibited. Secret scanning results shall be reviewed weekly by the Development Manager."),
    ]),

    ("Code Review", [
        ("A.8.25-26-29-31", "Be Reviewed Prior To Release By",
         "All code shall be reviewed prior to release by skilled personnel other than the code author or developer."),
        ("A.8.25-26-29-32", "Be Reviewed Against The Secure Coding",
         "Code shall be reviewed against the secure coding guidelines documented by the organisation."),
        ("A.8.25-26-29-33", "Code Reviews",
         "Code reviews shall employ both manual and automated techniques:."),
        ("A.8.25-26-29-34", "Code Review Findings",
         "Code review findings shall be documented and tracked to resolution before code is approved for promotion."),
        ("A.8.25-26-29-35", "Be Approved Before Being Promoted Into",
         "Code shall be approved before being promoted into test or production environments."),
    ]),

    ("CI CD Pipeline Security Gates", [
        ("A.8.25-26-29-36", "Security Checks",
         "Security checks shall be automated within the CI/CD pipeline at defined gates."),
        ("A.8.25-26-29-37", "Pipeline Security Gate Results",
         "Pipeline security gate results shall be reported to the Development Manager weekly and the CISO monthly."),
    ]),

    ("Security Testing Requirements", [
        ("A.8.25-26-29-38", "Security Testing Processes",
         "Security testing processes shall be defined and implemented in the development lifecycle. Testing shall validate that security requirements have been met before deployment to production."),
        ("A.8.25-26-29-39", "Application Security Testing",
         "All application security testing shall, at a minimum, test for the OWASP Top 10:2025 categories: Broken Access Control, Security Misconfiguration, Software Supply Chain Failures, Cryptographic Failures, Injection, Insecure Design, Authentication Failures, Software or Data Integrity Failures, Security Logging and Alerting Failures, and Mishandling of Exceptional Conditions."),
        ("A.8.25-26-29-40", "Pre-Production Testing",
         "All pre-production testing shall occur in a test environment that mirrors the production environment as closely as possible."),
        ("A.8.25-26-29-41", "Environment Verification*: Environment",
         "Environment verification*: Environment parity shall be verified before major security tests (penetration testing, DAST). Verification shall be documented and signed off by the DevOps / Platform Team."),
        ("A.8.25-26-29-42", "Test Environment Security*: Test",
         "Test environment security*: Test environments shall be subject to the same access controls as production environments. Test environments shall not be accessible from the internet unless required for DAST testing (with time-limited firewall rules)."),
        ("A.8.25-26-29-43", "Penetration Testing",
         "All penetration testing shall be conducted by an external specialist company."),
        ("A.8.25-26-29-44", "Public-Facing Web Applications",
         "All public-facing web applications shall be tested using manual or automated vulnerability security tools at least annually or after a significant change."),
        ("A.8.25-26-29-45", "Testing Standards*: Penetration Tests",
         "Testing standards*: Penetration tests shall follow OWASP Testing Guide v4.2 and/or PTES (Penetration Testing Execution Standard). Test reports shall include: executive summary, methodology, findings with CVSS scoring, evidence (screenshots, request/response), remediation recommendations, and re-test verification."),
        ("A.8.25-26-29-46", "Vendor Selection Criteria*: Penetration",
         "Vendor selection criteria*: Penetration testing vendors shall hold relevant certifications (e.g., CREST, OSCP, CEH) and provide evidence of professional indemnity insurance. Vendor engagements shall include signed rules of engagement and NDA."),
        ("A.8.25-26-29-47", "High-Risk Applications",
         "High-Risk applications shall maintain an SBOM in CycloneDX or SPDX format."),
        ("A.8.25-26-29-48", "Be Generated Automatically During The",
         "SBOMs shall be generated automatically during the build process (every build for High-Risk; weekly for Medium-Risk)."),
        ("A.8.25-26-29-49", "Be Updated Upon Dependency Changes And",
         "SBOMs shall be updated upon dependency changes and reviewed quarterly for known vulnerabilities."),
        ("A.8.25-26-29-50", "Sbom Content Requirements*: Each Sbom",
         "SBOM content requirements*: Each SBOM shall include: component name and version, supplier/author, licence type, dependency relationships (direct and transitive), and known vulnerability status (CVE references where applicable)."),
        ("A.8.25-26-29-51", "Sbom Vulnerability Monitoring*: Sca",
         "SBOM vulnerability monitoring*: SCA tools shall continuously monitor SBOM components against vulnerability databases. New critical/high vulnerabilities affecting SBOM components shall trigger alerts to the Development Manager within 24 hours."),
        ("A.8.25-26-29-52", "Sbom Retention*: Sboms",
         "SBOM retention*: SBOMs shall be retained for the lifecycle of the application plus 3 years."),
        ("A.8.25-26-29-53", "Test Results",
         "Test results, including penetration testing reports, shall be reported to the Management Review Team."),
    ]),

    ("Vulnerability Remediation", [
        ("A.8.25-26-29-54", "Security Vulnerabilities Identified",
         "Security vulnerabilities identified during development and testing shall be remediated within defined timeframes based on severity."),
        ("A.8.25-26-29-55", "Vulnerabilities Identified As Part Of",
         "All vulnerabilities identified as part of the testing phase, including penetration testing, shall be corrected prior to promotion to production or managed via the risk management and exception process."),
        ("A.8.25-26-29-56", "Vulnerabilities Exceeding The",
         "Vulnerabilities exceeding the remediation SLA shall be escalated to the CISO and Application Owner."),
        ("A.8.25-26-29-57", "Critical And High Vulnerabilities",
         "Critical and High vulnerabilities overdue beyond the SLA shall block subsequent deployments until remediated or an exception is approved with compensating controls."),
        ("A.8.25-26-29-58", "Vulnerability Remediation Status",
         "Vulnerability remediation status shall be reviewed monthly and reported quarterly to the Management Review Team."),
    ]),

    ("Test Data Protection", [
        ("A.8.25-26-29-59", "Production Data",
         "Production data shall not be used for testing or development."),
        ("A.8.25-26-29-60", "Personal Data (As Defined By Swiss",
         "Personal data (as defined by Swiss nFADP Art. 5) shall not be used for testing or development."),
        ("A.8.25-26-29-61", "Be",
         "If sensitive information is required as part of the testing process, it shall be:."),
        ("A.8.25-26-29-62", "Synthetic Data* (Artificially Generated",
         "Synthetic data* (artificially generated data with no connection to real individuals) is the preferred approach and shall be used where feasible."),
        ("A.8.25-26-29-63", "The Creation And Use Of Test",
         "The creation and use of test data sets shall be documented and approved by the data owner. Test data sets containing transformed personal data shall be treated as Internal classification at a minimum."),
        ("A.8.25-26-29-64", "Test Data",
         "Test data shall be securely deleted when no longer required."),
    ]),

    ("Promoting Code to Production", [
        ("A.8.25-26-29-65", "Be Promoted To Production By Approved",
         "Code shall be promoted to production by approved personnel only and shall be subject to the documented change management process."),
        ("A.8.25-26-29-66", "Required Security Gates",
         "All required security gates shall be passed (security testing, code review, vulnerability remediation)."),
        ("A.8.25-26-29-67", "The Production Environment",
         "The production environment shall be backed up to facilitate rollback in the event of a failed change."),
        ("A.8.25-26-29-68", "Test Data",
         "Test data shall be removed from the application."),
        ("A.8.25-26-29-69", "No Development Files, Debug",
         "No development files, debug configurations, test accounts, or test data shall be present in the production environment."),
        ("A.8.25-26-29-70", "For High-Risk Applications, The Ciso Or",
         "For High-Risk applications, the CISO or designated security authority shall provide explicit sign-off."),
        ("A.8.25-26-29-71", "Promotion Records",
         "Promotion records shall include the change ticket reference, approver, security gate status, and deployment timestamp."),
    ]),

    ("Outsourced Development", [
        ("A.8.25-26-29-72", "The Organisation'S Secure Development",
         "Where software development is outsourced to third-party contractors or development partners, the organisation's secure development requirements shall apply."),
        ("A.8.25-26-29-73", "Contractual Requirements",
         "Contractual requirements shall include*:."),
        ("A.8.25-26-29-74", "Submit Security Testing Reports",
         "Contractors shall submit security testing reports (SAST/DAST/SCA results, remediation status) at agreed intervals."),
        ("A.8.25-26-29-75", "High-Risk Outsourced Projects",
         "High-Risk outsourced projects shall undergo security review by the organisation's security-qualified personnel at major milestones (design approval, pre-production)."),
        ("A.8.25-26-29-76", "Code Delivered By Contractors",
         "Code delivered by contractors shall undergo the same code review and security testing process as internally developed code before acceptance."),
    ]),

    ("Developer Security Training", [
        ("A.8.25-26-29-77", "Complete Security Training Appropriate",
         "All developers shall complete security training appropriate to their role and responsibilities."),
        ("A.8.25-26-29-78", "Cover, At A Minimum",
         "Training shall cover, at a minimum:."),
        ("A.8.25-26-29-79", "Training Completion",
         "Training completion shall be recorded and verified before granting production code access. Training records shall be retained for the duration of employment plus 3 years."),
        ("A.8.25-26-29-80", "Selection Criteria*: Security Champions",
         "Selection criteria*: Security Champions shall be nominated from development teams based on: demonstrated interest in security, minimum 2 years development experience, willingness to commit approximately 10% of working time to security activities, and team lead endorsement."),
        ("A.8.25-26-29-81", "Incentives*: Security Champion",
         "Incentives*: Security Champion contributions shall be recognised in performance reviews. The organisation should consider conference attendance, certification sponsorship, or similar professional development opportunities."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.25-26-29
# =============================================================================
