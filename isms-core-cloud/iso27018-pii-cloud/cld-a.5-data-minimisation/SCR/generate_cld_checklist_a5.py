#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-CHK-A.5 — Data Minimisation Compliance Checklist

Controls A.5 / A.5.1: Data Minimisation Principle,
                       Secure Erasure of Temporary Files
Product: ISMS CORE Cloud (ISO/IEC 27018:2025 — Annex A)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Data Minimisation — Pseudonymisation and Anonymisation (A.5) — 3 reqs
4. Secure Erasure of Temporary Files (A.5.1) — 5 reqs

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
DOCUMENT_ID = "CLD-CHK-A.5"
CONTROL_ID = "A.5 / A.5.1"
CONTROL_NAME = "Data Minimisation"
SOURCE_POLICY = "CLD-POL-A.5"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-POL-A.5
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Data Minimisation and Pseudonymisation", [
        ("A.5-01", "Pseudonymisation and Anonymisation by Design",
         "Where the processing purpose can be fulfilled without direct identification of data subjects, the organisation shall implement pseudonymisation or anonymisation as part of service design. Analytics and reporting functions shall use pseudonymised or aggregated data where technically feasible. Logging and telemetry systems shall minimise PII capture to the operationally necessary minimum. Test and development environments shall use synthetic data or anonymised data sets wherever possible."),
        ("A.5-02", "DPO Review of Anonymisation Techniques",
         "Anonymisation techniques applied to controller PII shall be documented and subject to DPO review prior to implementation to confirm the result is genuinely anonymised. DPO review records shall be retained for the duration of use plus 3 years."),
        ("A.5-03", "Log Minimisation",
         "Application and infrastructure logs that capture PII shall be subject to: minimum capture (log configurations reviewed to ensure PII in payloads, headers, or parameters is masked or excluded unless operationally essential); retention limits (no longer than the operational period required or the maximum in the service agreement); and automated deletion (log retention policies implemented as automated rules, not manual processes)."),
    ]),

    ("Secure Erasure of Temporary Files", [
        ("A.5.1-01", "Temporary File Types in Scope",
         "The organisation shall identify and document all categories of temporary storage generated during PII processing that are subject to secure erasure, including: cache files; swap and paging files; work files and scratch space; application log files that may capture PII in payloads or error traces; and ephemeral compute storage attached to instances during job execution."),
        ("A.5.1-02", "Erasure Requirement",
         "The organisation shall implement secure erasure of all temporary storage containing PII once the processing operation for which it was created is complete. Erasure shall be performed using methods that prevent data recovery: cryptographic erasure (encryption key deletion for encrypted volumes); multi-pass overwrite for persistent storage where cryptographic erasure is not applicable; or secure memory zeroing for in-memory PII after use."),
        ("A.5.1-03", "Automated Erasure",
         "The erasure mechanism shall be automated within the service pipeline wherever technically feasible to eliminate reliance on manual procedures. Where automated erasure is not technically feasible, manual deletion shall be scheduled, logged, and confirmed. Automated erasure configuration records shall be maintained as evidence."),
        ("A.5.1-04", "Multi-Tenant Storage Isolation",
         "In multi-tenant environments, temporary storage allocated to a PII controller's processing shall be isolated from other tenants during active processing and securely erased before reallocation to any other tenant or workload. Reallocation events shall be logged and available for inspection. Any failure to isolate or erase shall be treated as a potential PII security incident."),
        ("A.5.1-05", "Procedure Coverage",
         "Temporary file erasure procedures shall explicitly cover: both persistent storage (SSD, HDD, NVMe) and ephemeral storage (instance store, container ephemeral); all compute layers (bare metal, virtual machine, container, serverless function); and all geographic regions in which the organisation operates cloud infrastructure. Procedure completeness shall be verified annually."),
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
