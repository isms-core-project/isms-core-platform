#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-CHK-A.7 — Accuracy and Quality Compliance Checklist

Control A.7: Accuracy and Quality for Public Cloud PII Processors
Product: ISMS CORE Cloud (ISO/IEC 27018:2025 — Annex A)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Data Integrity Preservation (A.7) — 4 reqs
4. Controller Correction Mechanisms and Quality Checks (A.7) — 4 reqs

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
DOCUMENT_ID = "CLD-CHK-A.7"
CONTROL_ID = "A.7"
CONTROL_NAME = "Accuracy and Quality"
SOURCE_POLICY = "CLD-POL-A.7"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-POL-A.7
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Data Integrity Preservation", [
        ("A.7-01", "Integrity Controls",
         "The organisation shall implement technical controls ensuring that PII stored in cloud systems is not degraded, corrupted, or altered through processing operations except as authorised by the PII controller. Storage systems shall implement integrity checking (e.g., checksums, cryptographic hashes) for PII data stores to detect unauthorised or accidental modification."),
        ("A.7-02", "Transformation Logging",
         "Transformation operations performed on PII during processing shall be reversible or logged, ensuring the original data can be verified or restored. Backup and replication operations shall preserve PII accuracy and completeness without data loss."),
        ("A.7-03", "Processing-Induced Inaccuracy",
         "Where the organisation performs data transformation, enrichment, or processing operations on PII on behalf of a controller, the organisation shall: document the transformation logic and its effect on PII accuracy; obtain controller authorisation for any transformation that modifies PII attributes; and alert the controller if a processing operation produces results that indicate potential inaccuracy in the source data."),
        ("A.7-04", "Integrity Check Configuration Records",
         "Technical documentation of integrity checking mechanisms implemented for PII data stores shall be maintained as evidence, including the mechanism type, scope of data stores covered, and verification frequency. Records shall be retained for the duration of the service plus 3 years."),
    ]),

    ("Controller Correction Mechanisms and Quality Checks", [
        ("A.7-05", "Controller Correction Capabilities",
         "The organisation shall provide PII controllers with technical capabilities to correct, update, and delete PII within cloud storage. These mechanisms shall allow field-level correction or full record update for structured PII data stores, and shall propagate corrections to replicated copies (backups, read replicas, caches) within a reasonable timeframe enabling the controller to fulfil data subject rights obligations."),
        ("A.7-06", "Correction Confirmation Records",
         "The organisation shall generate a confirmation record when PII corrections are completed, including which records were modified and the timestamp. Correction confirmation records shall be provided to the controller on request and retained for the duration of the service plus 3 years."),
        ("A.7-07", "Quality Checks",
         "The organisation shall implement the following quality controls for PII data stores: data completeness checks (identify and flag records with missing mandatory fields that may indicate data corruption or incomplete transfer); data consistency checks (verify PII consistency across replicated or distributed data stores to detect replication errors); and backup integrity verification (periodically restore and verify backup PII data to confirm backup integrity)."),
        ("A.7-08", "Quality Check Review and Reporting",
         "Quality check results shall be logged and reviewed quarterly by the Cloud Engineering team. Material data quality issues shall be reported to the PII controller without undue delay. Data quality incident records shall be retained for the duration of the service plus 3 years."),
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
