#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.31 — Separation of Development, Test and Production Environments Compliance Checklist

Control A.8.31: Separation of Development, Test and Production Environments
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Network Separation (13 reqs)
4. Access Control per Environment (8 reqs)
5. Data Handling Rules (8 reqs)
6. Test Data Management (12 reqs)
7. Code Promotion Process (15 reqs)
8. Configuration Separation (8 reqs)
9. Cloud Environment Separation (8 reqs)
10. Env Sep and Incident Response (1 reqs)
11. Compliance Measurement (2 reqs)

Total: 75 requirements across 9 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.31"
CONTROL_ID = "A.8.31"
CONTROL_NAME = "Separation of Development, Test and Production Environments"
SOURCE_POLICY = "ISMS-OP-POL-A.8.31"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.31
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Network Separation", [
        ("A.8.31-01", "Be Isolated Through Network Segmentation",
         "Environments shall be isolated through network segmentation to prevent unintended cross-environment data flows and access."),
        ("A.8.31-02", "Environment Separation",
         "Where the organisation uses cloud infrastructure, environment separation shall be implemented using the cloud provider's account or subscription boundary model:."),
        ("A.8.31-03", "Be Separated Using",
         "Where the organisation uses container orchestration platforms, environments shall be separated using:."),
        ("A.8.31-04", "Production Workloads",
         "Production workloads shall not share a cluster with development or testing workloads."),
        ("A.8.31-05", "Container Image Registries",
         "Container image registries shall be separated or access-controlled per environment."),
        ("A.8.31-06", "Production Containers",
         "Production containers shall not mount host filesystems except for explicitly approved use cases."),
        ("A.8.31-07", "Production Containers",
         "Production containers shall run as non-root users."),
        ("A.8.31-08", "Production Container Images",
         "Production container images shall be signed and verified before deployment."),
        ("A.8.31-09", "Container Registries",
         "Container registries shall be separated per environment (e.g., prod.registry.example.com vs dev.registry.example.com)."),
        ("A.8.31-10", "Production Clusters",
         "Production clusters shall use separate control planes and node pools."),
        ("A.8.31-11", "Pod Security Standards (Pss)",
         "Pod Security Standards (PSS) shall be enforced at 'Restricted' level for production."),
        ("A.8.31-12", "Network Policies",
         "Network policies shall deny-all by default with explicit allow rules."),
        ("A.8.31-13", "Service Accounts",
         "Service accounts shall be scoped to minimum required permissions."),
    ]),

    ("Access Control per Environment", [
        ("A.8.31-14", "Access To Each Environment",
         "Access to each environment shall follow the principle of least privilege. Access rights shall be defined per role and environment tier."),
        ("A.8.31-15", "Not Have Standing Access To Production",
         "Developers shall not have standing access to production infrastructure, databases, or application consoles."),
        ("A.8.31-16", "Production Access",
         "All production access shall require multi-factor authentication."),
        ("A.8.31-17", "Production Access Sessions",
         "Production access sessions shall be logged, recorded, and monitored."),
        ("A.8.31-18", "Privileged Production Access",
         "Privileged production access shall be managed through a Privileged Access Management (PAM) system ([PAM Tool] — e.g., CyberArk, HashiCorp Boundary, AWS SSM Session Manager, or equivalent)."),
        ("A.8.31-19", "Emergency Developer Access To Production",
         "Emergency developer access to production shall be permitted only during declared incidents where developer expertise is required for resolution. Break-glass access shall:."),
        ("A.8.31-20", "Break-Glass Activations",
         "Break-glass activations shall be reviewed monthly by the Information Security Manager and reported in the quarterly CISO dashboard with trend analysis."),
        ("A.8.31-21", "Terminated Employee Access",
         "Terminated employee access shall be revoked within the same business day across all environments. Automated deprovisioning via the identity management system is preferred."),
    ]),

    ("Data Handling Rules", [
        ("A.8.31-22", "Production Data",
         "Production data shall not be used in development or testing environments. This requirement protects business-critical data from exposure in less-controlled environments and supports nFADP compliance for personal data."),
        ("A.8.31-23", "Production Data",
         "Production data shall not be copied, exported, restored, or replicated to development, testing, or staging environments."),
        ("A.8.31-24", "Production Database Backups",
         "Production database backups shall not be restored in non-production environments."),
        ("A.8.31-25", "Production Credentials, Api Keys,",
         "Production credentials, API keys, connection strings, and secrets shall not be used in non-production environments."),
        ("A.8.31-26", "Log Files",
         "Log files containing production personal data shall not be transferred to non-production environments without anonymisation."),
        ("A.8.31-27", "Confidential And Restricted Data",
         "Confidential and Restricted data classifications shall be prohibited in development and testing environments."),
        ("A.8.31-28", "Automated Scanning",
         "Automated scanning shall be implemented to detect prohibited production data patterns (e.g., real names, national identifiers, financial account numbers) in non-production environments. Scanning shall cover databases, file systems, log files, and container images."),
        ("A.8.31-29", "Be Remediated Within 7 Days Of",
         "Violations shall be remediated within 7 days of detection and reported to the Information Security Manager."),
    ]),

    ("Test Data Management", [
        ("A.8.31-30", "Test Data",
         "Test data shall be managed as a controlled asset throughout the software development lifecycle."),
        ("A.8.31-31", "Synthetic Data",
         "Synthetic data shall be the default and preferred approach for all testing activities."),
        ("A.8.31-32", "Test Data",
         "Test data shall be structurally representative of production data (same schema, data types, relationships, and volume characteristics) without containing real personal or business data."),
        ("A.8.31-33", "Test Data Generation",
         "Test data generation shall be automated where practicable using [Test Data Tool] (e.g., Faker, Mockaroo, Tonic.ai, Delphix, or equivalent)."),
        ("A.8.31-34", "Test Data",
         "Test data shall be versioned and reproducible to support regression testing."),
        ("A.8.31-35", "Test Data",
         "Test data shall be purged from non-production environments within 30 days of project completion or test cycle conclusion."),
        ("A.8.31-36", "The Anonymisation Process",
         "Where anonymised production data is approved for non-production use, the anonymisation process shall be validated before each use:."),
        ("A.8.31-37", "Data Protection Officer",
         "Data Protection Officer shall verify that direct identifiers have been removed or replaced."),
        ("A.8.31-38", "Quasi-Identifier Combinations",
         "Quasi-identifier combinations shall be assessed for re-identification risk."),
        ("A.8.31-39", "Validation Results",
         "Validation results shall be documented and retained for audit purposes."),
        ("A.8.31-40", "Failed Validation",
         "Failed validation shall result in rejection and remediation before data can be used."),
        ("A.8.31-41", "Card Holder Data*: Card Holder Data",
         "Card Holder Data*: Card holder data (PAN, CVV, track data) shall never be used in development or testing environments, regardless of anonymisation status. Synthetic card numbers conforming to test ranges shall be used instead."),
    ]),

    ("Code Promotion Process", [
        ("A.8.31-42", "Follow A Defined Promotion Path From",
         "Changes shall follow a defined promotion path from development to production. Direct deployment to production shall be prohibited except for approved emergency fixes."),
        ("A.8.31-43", "Promotion Step",
         "Each promotion step shall include defined quality and security gates."),
        ("A.8.31-44", "The Developer Who Writes The Code",
         "The developer who writes the code shall not be the same person who approves its promotion to production."),
        ("A.8.31-45", "The Person Who Promotes Code To",
         "The person who promotes code to staging shall not be the same person who promotes it to production, where team size permits."),
        ("A.8.31-46", "Ci/Cd Pipeline Credentials For",
         "CI/CD pipeline credentials for production deployment shall be restricted to the operations team."),
        ("A.8.31-47", "Pipeline Definitions",
         "Pipeline definitions shall be version-controlled and subject to code review."),
        ("A.8.31-48", "Pipeline Credentials And Secrets",
         "Pipeline credentials and secrets shall be stored in the pipeline platform's secret store — not hardcoded in pipeline definitions."),
        ("A.8.31-49", "Have Dedicated Pipeline Credentials With",
         "Each environment shall have dedicated pipeline credentials with minimum required permissions."),
        ("A.8.31-50", "Pipeline Execution Logs",
         "Pipeline execution logs shall be retained for audit purposes (minimum 1 year)."),
        ("A.8.31-51", "Be Built Once And Promoted Through",
         "Artifacts shall be built once and promoted through environments (immutable artifacts) — not rebuilt per environment."),
        ("A.8.31-52", "Previous Versions",
         "Previous versions shall be retained to support rollback."),
        ("A.8.31-53", "Rollback Procedures",
         "Rollback procedures shall be documented and tested at least quarterly."),
        ("A.8.31-54", "The Operations Team",
         "The operations team shall be authorised to execute rollbacks without additional approval during incidents."),
        ("A.8.31-55", "Production Environments",
         "Production environments shall be backed up before each deployment to facilitate rollback."),
        ("A.8.31-56", "Test Data And Development Artefacts",
         "Test data and development artefacts shall be removed before promotion to production."),
    ]),

    ("Configuration Separation", [
        ("A.8.31-57", "Environment Configurations",
         "Environment configurations shall be managed to prevent credential leakage, cross-environment contamination, and configuration drift."),
        ("A.8.31-58", "Staging Environments",
         "Staging environments shall mirror production configuration as closely as possible (same software versions, same infrastructure sizing within budget constraints, same security controls)."),
        ("A.8.31-59", "Configuration Drift Between Staging And",
         "Configuration drift between staging and production shall be detected and reported. Drift detection shall be performed at least weekly."),
        ("A.8.31-60", "Differences Between Staging And",
         "Differences between staging and production shall be documented, justified, and approved by the IT Operations Manager."),
        ("A.8.31-61", "The Following Table",
         "The following table shall be maintained by the IT Operations Manager and reviewed quarterly. Unapproved differences detected through drift detection shall be investigated and resolved."),
        ("A.8.31-62", "Display Clear Visual Identification To",
         "Each environment shall display clear visual identification to prevent accidental operations in the wrong environment."),
        ("A.8.31-63", "Hostname Prefixes, Console Banners,",
         "Hostname prefixes, console banners, browser tab labels, and colour-coded UI elements shall distinguish environment tiers."),
        ("A.8.31-64", "Production Environments",
         "Production environments shall display prominent identification (e.g., red banners, '[PRODUCTION]' labels)."),
    ]),

    ("Cloud Environment Separation", [
        ("A.8.31-65", "Production Workloads",
         "Production workloads shall reside in dedicated cloud accounts, subscriptions, or projects — separate from all non-production workloads."),
        ("A.8.31-66", "Iam Policies",
         "IAM policies shall prevent cross-account access except through explicitly defined, audited roles."),
        ("A.8.31-67", "Service Control Policies (Scps), Azure",
         "Service control policies (SCPs), Azure Policies, or organisation policies shall enforce environment boundaries at the organisational level."),
        ("A.8.31-68", "Be Separated Per Environment To Enable",
         "Billing shall be separated per environment to enable cost attribution and anomaly detection."),
        ("A.8.31-69", "Cloud Resources",
         "All cloud resources shall be tagged with environment identification (e.g., env:production, env:staging, env:development) to support:."),
        ("A.8.31-70", "Infrastructure Definitions",
         "Infrastructure definitions shall be stored in version-controlled repositories."),
        ("A.8.31-71", "Infrastructure Changes",
         "Infrastructure changes shall follow the same promotion workflow as application code (develop, review, test, deploy)."),
        ("A.8.31-72", "Manual Changes To Production",
         "Manual changes to production infrastructure ('ClickOps') shall be prohibited; all changes shall be applied through the CI/CD pipeline."),
    ]),

    ("Env Sep and Incident Response", [
        ("A.8.31-73", "During Incidents Involving Environment",
         "During incidents involving environment boundary violations (unauthorised access across environments, production data discovered in non-production), the Information Security Manager shall:."),
    ]),

    ("Compliance Measurement", [
        ("A.8.31-74", "The Information Security Manager",
         "The Information Security Manager shall generate this dashboard quarterly and present it during the management review:."),
        ("A.8.31-75", "Items Requiring Attention And Recent",
         "Items requiring attention and recent improvements shall be highlighted in the dashboard report."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.31
# =============================================================================
