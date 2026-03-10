#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-CHK-A.9 — Individual Participation and Access Compliance Checklist

Control A.9: Individual Participation and Access for Public Cloud PII Processors
Product: ISMS CORE Cloud (ISO/IEC 27018:2025 — Annex A)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Rights Fulfilment Capabilities (A.9) — 4 reqs
4. Capability Testing, Timeframes and Documentation (A.9) — 4 reqs

Total: 8 requirements across 2 domains
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
DOCUMENT_ID = "CLD-CHK-A.9"
CONTROL_ID = "A.9"
CONTROL_NAME = "Individual Participation and Access"
SOURCE_POLICY = "CLD-POL-A.9"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-POL-A.9
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Rights Fulfilment Capabilities", [
        ("A.9-01", "Processor Support Obligation",
         "The organisation shall provide PII controllers with technical capabilities and operational procedures enabling controllers to fulfil data subject rights requests. The support obligation covers: access (export of all PII for a data subject in structured, readable format); rectification (update or correct PII records with replication propagation); erasure (confirmed deletion including backups and replicated copies within defined timeframe); restriction (isolate PII from active processing without deletion); portability (PII export in machine-readable format such as JSON or CSV); and objection (flag and suspend automated processing involving specific PII)."),
        ("A.9-02", "Capability Completeness",
         "Rights fulfilment capabilities shall be available for each cloud service category that stores or processes PII. Where a capability cannot be provided for a specific service, the organisation shall document the limitation, notify affected PII controllers, and implement alternative arrangements enabling the controller to fulfil the right by other means."),
        ("A.9-03", "Backup and Replication Propagation",
         "Erasure and restriction operations shall propagate correctly to backup copies and replicated data stores. The organisation shall define and document the maximum timeframe for complete propagation to backups, including any period during which PII exists in backup copies pending rotation. This timeframe shall be included in controller-facing capability documentation."),
        ("A.9-04", "Controller Assistance Records",
         "All controller requests for data subject rights assistance shall be logged with: controller identity; right type exercised; date of request; date of completion; and outcome. Records shall be made available to the controller on request and retained for the duration of the service plus 3 years."),
    ]),

    ("Capability Testing, Timeframes and Documentation", [
        ("A.9-05", "Annual Capability Testing",
         "The organisation shall test data subject rights fulfilment capabilities at minimum annually and upon any material change to service architecture. Testing shall cover each right type for each service category; verify that export, deletion, and restriction operations complete within the defined response timeframes; and confirm that deletions propagate correctly to backup copies and replicated data stores. Test results shall be documented."),
        ("A.9-06", "Gap Remediation",
         "Material gaps identified during capability testing shall be tracked as remediation items and reported to affected PII controllers if capability is reduced below contracted service levels. Remediation tracking records shall be retained until the gap is resolved plus 3 years."),
        ("A.9-07", "Response Timeframes",
         "The organisation's service capabilities shall support controller fulfilment of data subject rights responses within the following timeframes: acknowledge controller DSAR-related requests within 1 business day; complete data access exports and rectification requests within 5 business days; complete erasure requests (including propagation to backups) within 15 business days; complete restriction requests within 1 business day (functional) and 5 business days (full propagation). Service agreement timeframes prevail where shorter."),
        ("A.9-08", "Controller Capability Documentation",
         "The organisation shall provide PII controllers with documentation describing the data subject rights capabilities available within each cloud service, including how to initiate each operation, expected completion times and confirmation mechanisms, any limitations on rights fulfilment, and the escalation path for requesting assistance. Documentation shall be current and updated within 30 days of any material capability change."),
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
