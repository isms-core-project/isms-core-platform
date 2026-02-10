#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.9 — Configuration Management Compliance Checklist

Control A.8.9: Configuration Management
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Configuration Baselines (11 reqs)
4. Standard Builds & Golden Images (3 reqs)
5. Configuration Change Control (6 reqs)
6. Config Drift Detection and Mon (8 reqs)
7. Security Hardening Standards (10 reqs)
8. Configuration Audit (3 reqs)
9. Emergency Configuration Changes (5 reqs)

Total: 46 requirements across 7 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.9"
CONTROL_ID = "A.8.9"
CONTROL_NAME = "Configuration Management"
SOURCE_POLICY = "ISMS-OP-POL-A.8.9"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.9
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Configuration Baselines", [
        ("A.8.9-01", "Define And Maintain Secure Configuration",
         "The organisation shall define and maintain secure configuration baselines at the asset-type level (e.g., 'Windows Server 2022 — Domain Controller', 'Ubuntu 24.04 — Application Server', 'Cisco IOS-XE — Core Switch'), not at the individual asset level."),
        ("A.8.9-02", "Be Defined For All Asset Types",
         "Baselines shall be defined for all asset types in active production use."),
        ("A.8.9-03", "Be Measured By",
         "Coverage shall be measured by:."),
        ("A.8.9-04", "Tier 1/2 Assets Without Baselines:",
         "Tier 1/2 assets without baselines: Deployment to production shall be blocked until a baseline is created (enforced via change approval)."),
        ("A.8.9-05", "Document",
         "Each baseline shall document:."),
        ("A.8.9-06", "New Baselines And Baseline Updates",
         "New baselines and baseline updates shall follow a defined approval workflow:."),
        ("A.8.9-07", "Be Reviewed And Updated",
         "Baselines shall be reviewed and updated:."),
        ("A.8.9-08", "The Baseline",
         "The baseline shall be marked 'DEPRECATED' with an effective date."),
        ("A.8.9-09", "The Baseline",
         "The baseline shall be retained in the repository for 3 years for historical reference."),
        ("A.8.9-10", "The Baseline",
         "The baseline shall be removed from active compliance monitoring."),
        ("A.8.9-11", "A Replacement Baseline (If Applicable)",
         "A replacement baseline (if applicable) shall be linked in the repository."),
    ]),

    ("Standard Builds & Golden Images", [
        ("A.8.9-12", "Golden Images",
         "Golden images shall:."),
        ("A.8.9-13", "Image Age Tracking*: [Asset Management",
         "Image age tracking*: [Asset Management System] shall record image creation date per deployed instance; report monthly on 'stale deployments' (instances from images older than 30 days)."),
        ("A.8.9-14", "Golden Image Creation",
         "Golden image creation shall be restricted to authorised personnel (system administrators or DevOps engineers). New or updated golden images shall be validated by the security team before approval."),
    ]),

    ("Configuration Change Control", [
        ("A.8.9-15", "Changes To System Configurations",
         "All changes to system configurations shall follow the organisation's change management process (see Change Management Policy — A.8.32). This section addresses configuration-specific requirements that complement change management."),
        ("A.8.9-16", "Configuration Changes",
         "Configuration changes shall be classified according to risk and impact:."),
        ("A.8.9-17", "Documentation: Standard Change Catalogue",
         "Documentation: Standard change catalogue shall be maintained in [Change Management System] with pre-approved procedures and risk assessments."),
        ("A.8.9-18", "Following Any Approved Configuration",
         "Following any approved configuration change, the following shall be updated within 5 business days:."),
        ("A.8.9-19", "Configuration Changes Made Outside The",
         "Configuration changes made outside the approved change management process shall be treated as security events:."),
        ("A.8.9-20", "The Affected System",
         "The affected system shall be remediated to the approved baseline or a new baseline formally approved through the standard process."),
    ]),

    ("Config Drift Detection and Mon", [
        ("A.8.9-21", "Implement Configuration Monitoring To",
         "The organisation shall implement configuration monitoring to detect deviations from approved baselines."),
        ("A.8.9-22", "Monitoring Tools",
         "Monitoring tools shall:."),
        ("A.8.9-23", "Tool Selection*: The Organisation",
         "Tool selection*: The organisation shall select configuration monitoring tools appropriate to its technical environment. Tools shall support baseline comparison and drift detection. Examples include: file integrity monitoring (FIM) tools, cloud configuration assessment tools (e.g., AWS Config, Azure Policy, GCP Security Command Center), endpoint management platforms, and configuration compliance scanners."),
        ("A.8.9-24", "Asset Types Not Yet Under Automated",
         "Asset types not yet under automated monitoring shall be documented with a planned deployment date and interim manual controls (e.g., quarterly manual audits). Coverage gaps shall be risk-accepted by the CISO and recorded in the risk register."),
        ("A.8.9-25", "Risk Acceptance Does Not Waive Interim",
         "Risk acceptance does not waive interim controls — manual audits shall continue."),
        ("A.8.9-26", "Be Classified By Severity And Responded",
         "When configuration drift is detected, it shall be classified by severity and responded to within defined timelines:."),
        ("A.8.9-27", "Drift Remediation",
         "Drift remediation shall follow a structured workflow:."),
        ("A.8.9-28", "Recurring Drift On The Same System",
         "Recurring drift on the same system or asset type shall trigger a root cause analysis. If the root cause is a baseline that is impractical to maintain, the baseline shall be reviewed and updated through the standard approval process rather than repeatedly accepting exceptions."),
    ]),

    ("Security Hardening Standards", [
        ("A.8.9-29", "Select And Apply Recognised Security",
         "The organisation shall select and apply recognised security hardening standards for all production asset types."),
        ("A.8.9-30", "The Organisation",
         "Where multiple standards exist for an asset type, the organisation shall select the standard most appropriate to its risk profile and document the selection rationale."),
        ("A.8.9-31", "Production Systems",
         "All production systems shall be hardened before deployment. Hardening shall include, at minimum:."),
        ("A.8.9-32", "Hardening Compliance",
         "Hardening compliance shall be verified through periodic scanning:."),
        ("A.8.9-33", "Scan Results And Compliance Reports",
         "Scan results and compliance reports shall be retained for a minimum of 3 years for audit purposes."),
        ("A.8.9-34", "Hardening Gaps Identified Through",
         "Hardening gaps identified through verification shall be remediated according to risk:."),
        ("A.8.9-35", "Gaps That Cannot Be Remediated Due",
         "Gaps that cannot be remediated due to technical constraints or business requirements shall be documented as exceptions with compensating controls (see Exception Management below)."),
        ("A.8.9-36", "Reduce Risk To An Acceptable Level",
         "Controls shall reduce risk to an acceptable level (CISO determination)."),
        ("A.8.9-37", "Be Verifiable And Auditable (Not Merely",
         "Controls shall be verifiable and auditable (not merely 'we will be careful')."),
        ("A.8.9-38", "Expiry: 12 Months Maximum",
         "Expiry: 12 months maximum; shall be re-justified if still needed."),
    ]),

    ("Configuration Audit", [
        ("A.8.9-39", "Conduct Periodic Configuration Audits To",
         "The organisation shall conduct periodic configuration audits to verify that:."),
        ("A.8.9-40", "Configuration Audits",
         "Configuration audits shall produce documented evidence including:."),
        ("A.8.9-41", "Audit Results",
         "Audit results shall be reported to the CISO and included in the management review process."),
    ]),

    ("Emergency Configuration Changes", [
        ("A.8.9-42", "The System",
         "The system shall be restored to a documented, known-good configuration state as quickly as possible."),
        ("A.8.9-43", "The Baseline",
         "If the emergency change results in a new configuration state (not a return to baseline), the baseline shall be updated through the standard approval process within 5 business days."),
        ("A.8.9-44", "Emergency Configuration Changes",
         "All emergency configuration changes shall be logged with: the specific configuration parameters changed, the previous values, the new values, the person who made the change, and the business justification."),
        ("A.8.9-45", "Retrospective Review By The Ciso Or",
         "Retrospective review by the CISO or delegate shall occur within 48 hours."),
        ("A.8.9-46", "Emergency Configuration Changes",
         "Emergency configuration changes shall not exceed 10% of all configuration changes in any calendar month. Exceeding this threshold triggers a process review."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.9
# =============================================================================
