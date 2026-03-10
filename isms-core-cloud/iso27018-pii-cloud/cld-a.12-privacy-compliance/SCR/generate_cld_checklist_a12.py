#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-CHK-A.12 — Privacy Compliance Checklist

Controls A.12.1-A.12.2: Geographical Location of PII,
                         Intended Destination of PII
Product: ISMS CORE Cloud (ISO/IEC 27018:2025 — Annex A)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Geographical Location of PII (A.12.1) — 5 reqs
4. Transfer Destinations and Mechanisms (A.12.2) — 4 reqs

Total: 9 requirements across 2 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 51-isms-core-privacy/00-checklist-engine/priv_checklist_engine.py
_REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_REPO_ROOT / '51-isms-core-privacy' / '00-checklist-engine'))
from priv_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "CLD-CHK-A.12"
CONTROL_ID = "A.12.1-2"
CONTROL_NAME = "Privacy Compliance"
SOURCE_POLICY = "CLD-POL-A.12"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-POL-A.12
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Geographical Location of PII", [
        ("A.12.1-01", "PII Processing Locations Register",
         "The organisation shall maintain a PII Processing Locations Register documenting all countries and regions in which PII is stored, processed, or transits as part of cloud service delivery. The register shall cover: primary storage locations (data centres and cloud regions where PII at rest resides); processing locations (compute regions where PII is actively processed); transit routes (regions through which PII may pass during replication, backup, or delivery); and sub-processor locations (all geographic locations of engaged sub-processors)."),
        ("A.12.1-02", "Register Availability",
         "The PII Processing Locations Register shall be made available to PII controllers upon request and shall be publicly accessible for controllers operating under general authorisation (e.g., linked from the organisation's trust portal or DPA annex). The register shall be consistent with the Sub-Processor Register maintained under CLD-POL-A.8.1."),
        ("A.12.1-03", "Data Residency Enforcement",
         "Where a PII controller specifies data residency requirements in the service agreement (e.g., 'EU-only storage', 'Switzerland only'), the organisation shall technically enforce the residency constraint through infrastructure configuration (regional restrictions, geo-fencing, storage policy rules); document the technical mechanism used and make this documentation available to the controller upon request; and audit residency compliance at least annually and upon significant infrastructure changes, confirming that no PII has been stored or processed outside the agreed regions."),
        ("A.12.1-04", "Location Change Notification",
         "Before changing the geographic location of PII processing — including opening a new service region, adding a sub-processor in a new jurisdiction, or relocating backup storage — the organisation shall notify the relevant PII controller a minimum of 30 days in advance (unless the service agreement specifies a longer period); identify the new location and explain the operational reason; obtain prior consent from controllers whose agreements require specific consent for location changes; and update the PII Processing Locations Register within 5 business days of the change taking effect."),
        ("A.12.1-05", "Emergency Location Changes",
         "Emergency location changes (e.g., due to data centre failure or force majeure) shall be notified to affected PII controllers without undue delay, with retroactive documentation of the change and its justification. Emergency changes shall be formally recorded in the PII Processing Locations Register within 5 business days of the change. Records of location change notifications shall be retained for 5 years."),
    ]),

    ("Transfer Destinations and Mechanisms", [
        ("A.12.2-01", "Transfer Destination Documentation",
         "The organisation shall maintain documented records of all intended destinations to which PII may be transferred as part of cloud service delivery, including cross-border flows to sub-processors, backup and disaster recovery sites in third countries, cloud infrastructure in jurisdictions outside the controller's home country, and support or operations personnel accessing PII remotely from outside the processing region. For each destination the organisation shall document: the destination country or region; transfer purpose; applicable transfer mechanism and legal basis; safeguards in place; and controller notification status."),
        ("A.12.2-02", "Approved Transfer Mechanisms",
         "For transfers of PII to countries outside the EEA or Switzerland that lack an adequacy decision, the organisation shall implement one of the following approved transfer mechanisms: EC-approved Standard Contractual Clauses (2021 set); UK International Data Transfer Agreement (IDTA) for transfers to or from the United Kingdom; Swiss Standard Data Protection Clauses for transfers subject to CH FADP; adequacy decision (where in force at the time of transfer); or Binding Corporate Rules (where applicable for intra-group transfers). The organisation shall not transfer PII to a third country without a documented, applicable mechanism."),
        ("A.12.2-03", "Adequacy Status Monitoring",
         "The organisation shall monitor the adequacy status of all destination countries to which PII is transferred. Where the adequacy status of a destination country changes (e.g., adequacy decision revoked or suspended), the organisation shall review affected transfers and implement alternative transfer mechanisms within 30 days of the change taking effect, and notify affected PII controllers of the change and the alternative mechanism adopted."),
        ("A.12.2-04", "Controller Transfer Information",
         "The organisation shall provide PII controllers with transfer documentation upon request to support the controller's own Article 30 RoPA obligations or transfer impact assessments. Documentation shall include: the complete list of transfer destinations for the controller's PII; the transfer mechanism and relevant legal instrument reference for each destination; and a summary of supplementary technical safeguards applied for transfers to high-risk jurisdictions. Transfer mechanism instruments (SCCs, IDTAs, BCRs, adequacy decision citations) shall be retained for the duration of the engagement plus 5 years."),
    ]),
])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 27018:2025"
    ))


# =============================================================================
# QA_VERIFIED: 2026-03-10
# QA_STATUS: PASSED
# QA_TOOL: Claude Code Production Scripts QA Methodology
# CHANGES: Initial generation for Cloud product launch
# =============================================================================
