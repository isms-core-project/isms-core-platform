#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.5.9 — Asset Management Compliance Checklist

Control A.5.9: Asset Management
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Asset Categories (2 reqs)
4. Inventory Hardware & IT Infra (1 reqs)
5. Inventory Software & Licence (3 reqs)
6. Inventory Cloud & SaaS Services (4 reqs)
7. Inventory of Data & Info Assets (1 reqs)
8. Ownership of Assets (8 reqs)
9. Asset Lifecycle (8 reqs)
10. Acceptable Use of Assets (2 reqs)
11. Return of Assets (4 reqs)
12. Asset Review (2 reqs)

Total: 35 requirements across 10 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.5.9"
CONTROL_ID = "A.5.9"
CONTROL_NAME = "Asset Management"
SOURCE_POLICY = "ISMS-OP-POL-A.5.9"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.5.9
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Asset Categories", [
        ("A.5.9-01", "The Following Categories Of Assets",
         "The following categories of assets shall be inventoried:."),
        ("A.5.9-02", "Personnel Competencies: The Register",
         "Personnel competencies: The register documents roles and competencies*, not individual person records. Example: 'Database Administrator competency (2 qualified staff)' — not individual names. Where a critical function is dependent on a single individual (single point of failure), this shall be flagged and a succession or knowledge transfer plan documented to mitigate the risk."),
    ]),

    ("Inventory Hardware & IT Infra", [
        ("A.5.9-03", "Hardware And It Infrastructure Assets",
         "All hardware and IT infrastructure assets shall be registered in the asset inventory. For each asset, the following attributes shall be recorded:."),
    ]),

    ("Inventory Software & Licence", [
        ("A.5.9-04", "Software And Software Licences",
         "Software and software licences shall be registered in the asset inventory. For each software asset, the following attributes shall be recorded:."),
        ("A.5.9-05", "Only Organisation-Approved And Licensed",
         "Only organisation-approved and licensed software shall be deployed. Unauthorised software discovered during inventory reviews shall be reported to the information security management team for assessment and removal."),
        ("A.5.9-06", "Software That Has Reached End Of",
         "Software that has reached end of life or end of support shall be flagged and prioritised for upgrade or replacement. Where unsupported software cannot be immediately replaced, the risk shall be documented in the risk register with compensating controls."),
    ]),

    ("Inventory Cloud & SaaS Services", [
        ("A.5.9-07", "Cloud Services (Iaas, Paas, Saas)",
         "Cloud services (IaaS, PaaS, SaaS) shall be registered in the asset inventory alongside traditional software. For each cloud service, the following additional attributes shall be recorded:."),
        ("A.5.9-08", "Cloud Services",
         "Cloud services shall be classified as:."),
        ("A.5.9-09", "New Cloud Services",
         "New cloud services shall be registered in the asset inventory before organisation data is processed in the service (or within 5 business days for emergency deployments with CISO approval)."),
        ("A.5.9-10", "Unsanctioned Cloud Services (Shadow It)",
         "Unsanctioned cloud services (shadow IT) shall be identified through periodic reviews of expense reports, SSO logs, and network traffic. Newly discovered services shall be assessed for security and data protection compliance before being sanctioned."),
    ]),

    ("Inventory of Data & Info Assets", [
        ("A.5.9-11", "Data And Information Assets",
         "Data and information assets shall be identified, and an inventory drawn up and maintained. For each data asset, the following attributes shall be recorded:."),
    ]),

    ("Ownership of Assets", [
        ("A.5.9-12", "An Owner",
         "An owner shall be assigned to every inventoried asset. Ownership shall not be left blank."),
        ("A.5.9-13", "Asset Owners",
         "Asset owners shall:."),
        ("A.5.9-14", "New Assets",
         "New assets shall have an owner assigned at the time of registration."),
        ("A.5.9-15", "The Information Security Management Team",
         "Where ownership is unclear, the information security management team shall escalate to the appropriate manager for determination within 30 calendar days."),
        ("A.5.9-16", "Assets Without An Assigned Owner Beyond",
         "Assets without an assigned owner beyond 30 days shall be escalated to the CISO with documented justification."),
        ("A.5.9-17", "Ownership Changes (E.G., Employee",
         "Ownership changes (e.g., employee departure, role change) shall be updated in the register within 5 business days."),
        ("A.5.9-18", "Discovered Unregistered Assets: Assets",
         "Discovered unregistered assets: Assets found in use but not in the inventory shall be immediately registered with a temporary owner (the discoverer's manager or IT), investigated within 14 business days* to determine the business owner and purpose, and either formally assigned to a permanent owner or decommissioned."),
        ("A.5.9-19", "Owner Departure: When An Asset Owner",
         "Owner departure: When an asset owner leaves the organisation, ownership shall be reassigned to the departing employee's manager or designated successor within 10 business days* of departure. Assets without reassigned ownership after 30 days shall be escalated to the CISO."),
    ]),

    ("Asset Lifecycle", [
        ("A.5.9-20", "Be Registered In The Asset Inventory",
         "All assets shall be registered in the asset inventory within 5 business days of acquisition or deployment. Assets shall not be connected to the network or used to process organisation data until registered."),
        ("A.5.9-21", "Any Change To An Asset'S Owner",
         "Any change to an asset's owner, location, classification, or status shall be reflected in the register within 5 business days of the change."),
        ("A.5.9-22", "Be Securely Erased Or Destroyed In",
         "Data shall be securely erased or destroyed in line with the Information Classification and Handling Policy, using methods compliant with NIST SP 800-88 (Guidelines for Media Sanitization): Clear (logical overwrite) for INTERNAL data, Purge (cryptographic erasure or degauss) for CONFIDENTIAL data, or Destroy (physical destruction) where required."),
        ("A.5.9-23", "Software Licences",
         "Software licences shall be reclaimed or deactivated."),
        ("A.5.9-24", "The Asset Register",
         "The asset register shall be updated to reflect the disposal, including the date and method of disposal."),
        ("A.5.9-25", "For Assets That Stored Confidential Or",
         "For assets that stored confidential or personal data, evidence of data sanitisation shall be retained (e.g., certificate of destruction, wipe confirmation log)."),
        ("A.5.9-26", "Personally-Owned Devices Used To Access",
         "Where BYOD is permitted, personally-owned devices used to access organisation data shall be registered in the asset inventory with a flag indicating personal ownership. Minimum BYOD registration attributes:."),
        ("A.5.9-27", "Upon Termination Or Contract End,",
         "Upon termination or contract end, organisation data shall be wiped from the personal device, and the BYOD record shall be updated."),
    ]),

    ("Acceptable Use of Assets", [
        ("A.5.9-28", "Acceptable Use Of Assets",
         "Acceptable use of assets shall be in line with the Acceptable Use Policy."),
        ("A.5.9-29", "Not Install Unauthorised Software,",
         "Users shall not install unauthorised software, connect unapproved devices to the network, or use organisation assets for purposes outside the scope of their role."),
    ]),

    ("Return of Assets", [
        ("A.5.9-30", "Employees And Third-Party Users",
         "All employees and third-party users shall return all organisation assets in their possession upon termination of their employment, contract, or agreement."),
        ("A.5.9-31", "Ensure That All Organisation Information",
         "Where an employee or third-party user has used their own personal equipment (BYOD), procedures shall ensure that all organisation information is transferred to the organisation and securely erased from the personal device."),
        ("A.5.9-32", "During Notice Periods, The Organisation",
         "During notice periods, the organisation shall take reasonable measures to prevent unauthorised copying of organisation information by departing employees or third-party users."),
        ("A.5.9-33", "The Asset Register",
         "The asset register shall be updated to reflect all returned, reassigned, or disposed assets."),
    ]),

    ("Asset Review", [
        ("A.5.9-34", "The Asset Inventory",
         "The asset inventory shall be reviewed at the following intervals:."),
        ("A.5.9-35", "Department Heads",
         "Department heads shall confirm their asset lists are current during the annual review. Discrepancies shall be investigated and resolved within 30 days."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.5.9
# =============================================================================
