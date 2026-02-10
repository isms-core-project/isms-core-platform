#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.10 — Information Deletion Compliance Checklist

Control A.8.10: Information Deletion
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Retention Schedules & Deletion (5 reqs)
4. Deletion Methods (9 reqs)
5. Third-Party and Cloud Deletion (3 reqs)
6. Data Subject Erasure Requests (2 reqs)
7. Legal Hold Management (7 reqs)
8. Exception Management (3 reqs)
9. Compliance Measurement (1 reqs)

Total: 30 requirements across 7 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.10"
CONTROL_ID = "A.8.10"
CONTROL_NAME = "Information Deletion"
SOURCE_POLICY = "ISMS-OP-POL-A.8.10"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.10
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Retention Schedules & Deletion", [
        ("A.8.10-01", "Maintain A Retention Schedule Defining",
         "The organisation shall maintain a retention schedule defining retention periods for all data categories. Retention periods shall be based on the longest applicable requirement from:."),
        ("A.8.10-02", "The Longest Applicable Retention Period",
         "Where multiple requirements apply to the same data, the longest applicable retention period shall govern unless Legal Counsel determines otherwise."),
        ("A.8.10-03", "This Table Provides Minimum Reference",
         "This table provides minimum reference periods. The Records Manager shall maintain the authoritative retention schedule, which shall be reviewed annually by Legal Counsel and approved by Executive Management."),
        ("A.8.10-04", "Be Initiated When Any Of The",
         "Deletion shall be initiated when any of the following events occurs:."),
        ("A.8.10-05", "It Should Be Implemented With Safeguards",
         "Where automated deletion is technically feasible, it should be implemented with safeguards against premature deletion (legal hold checks, business owner notification). Where automation is not feasible, manual deletion procedures shall be documented with defined verification checkpoints."),
    ]),

    ("Deletion Methods", [
        ("A.8.10-06", "Deletion Methods",
         "Deletion methods shall align with NIST SP 800-88 Rev. 2 (Guidelines for Media Sanitization, September 2025), which defines three sanitisation levels, and IEEE 2883 for media-specific sanitisation techniques."),
        ("A.8.10-07", "Target Data",
         "All target data shall have been encrypted before storage (encryption applied retroactively does not qualify)."),
        ("A.8.10-08", "The Encryption Algorithm",
         "The encryption algorithm shall meet approved minimum standards (AES-256 or equivalent)."),
        ("A.8.10-09", "A Documented Data-To-Key Mapping",
         "A documented data-to-key mapping shall exist, enabling identification of which encryption keys protect which data."),
        ("A.8.10-10", "Key Destruction",
         "Key destruction shall be performed through a verified process (HSM key zeroisation, KMS key deletion with audit log, or equivalent)."),
        ("A.8.10-11", "Key Destruction Evidence",
         "Key destruction evidence shall be retained (audit logs, HSM certificates) for a minimum of 3 years."),
        ("A.8.10-12", "Backup Copies Of The Encryption Key",
         "Backup copies of the encryption key shall also be destroyed — if key backup, escrow, or external storage exists and cannot be verified as destroyed, cryptographic erasure shall not be accepted as the sole deletion method."),
        ("A.8.10-13", "Deletion In Production Systems",
         "Deletion in production systems shall extend to all backup copies containing the deleted data, including:."),
        ("A.8.10-14", "Immutable Backup Tapes, Retention-Locked",
         "Where immediate deletion from backups is not technically feasible (e.g., immutable backup tapes, retention-locked cloud backups), the organisation shall:."),
    ]),

    ("Third-Party and Cloud Deletion", [
        ("A.8.10-15", "Contracts With Third Parties That",
         "All contracts with third parties that process organisational data shall include deletion obligations specifying:."),
        ("A.8.10-16", "Before Engaging A Cloud Service Provider",
         "Before engaging a cloud service provider, the organisation shall assess deletion capabilities including:."),
        ("A.8.10-17", "Obtain Verification Of Deletion From",
         "The organisation shall obtain verification of deletion from third parties through one or more of the following methods:."),
    ]),

    ("Data Subject Erasure Requests", [
        ("A.8.10-18", "Accept And Process Data Subject Erasure",
         "The organisation shall accept and process data subject erasure requests in compliance with Swiss nFADP Art. 6(4) and, where applicable, GDPR Art. 17 (right to erasure / right to be forgotten)."),
        ("A.8.10-19", "The Organisation",
         "Where personal data subject to an erasure request was disclosed to third parties, the organisation shall notify those third parties of the erasure request per GDPR Art. 19 and nFADP obligations, unless doing so proves impossible or involves disproportionate effort."),
    ]),

    ("Legal Hold Management", [
        ("A.8.10-20", "Be Suspended When Data Is Subject",
         "Deletion shall be suspended when data is subject to a legal hold for any of the following reasons:."),
        ("A.8.10-21", "Affected Custodians Are Notified Within",
         "Affected custodians are notified within 24 hours and shall acknowledge receipt within 2 business days."),
        ("A.8.10-22", "Legal Holds",
         "Legal holds shall be reviewed at least quarterly by Legal Counsel. Each review shall produce a documented assessment including:."),
        ("A.8.10-23", "Data Held Beyond Normal Retention Solely",
         "Data held beyond normal retention solely due to the legal hold shall be deleted within 90 days of hold release, unless an approved business justification exists."),
        ("A.8.10-24", "Restriction Of Processing",
         "Restriction of processing shall be applied (data preserved but not actively used)."),
        ("A.8.10-25", "Execute Within 30 Days Of Hold",
         "Deletion shall execute within 30 days of hold release."),
        ("A.8.10-26", "The Data Subject",
         "The data subject shall be informed that the request has been noted but cannot currently be fulfilled, citing the applicable legal exception, without disclosing details that could prejudice legal proceedings."),
    ]),

    ("Exception Management", [
        ("A.8.10-27", "Proposed Expiry Date (Exceptions",
         "Proposed expiry date (exceptions shall not be indefinite)."),
        ("A.8.10-28", "The Following Exceptions",
         "The following exceptions shall not be granted:."),
        ("A.8.10-29", "Approved Exceptions",
         "All approved exceptions shall be recorded in the exception register with owner, approval date, expiry date, compensating controls, and review schedule. Exceptions shall be reviewed quarterly and auto-expire unless renewed through the approval process."),
    ]),

    ("Compliance Measurement", [
        ("A.8.10-30", "Metrics Breaching Targets",
         "Metrics breaching targets shall be escalated to the CISO for immediate attention and reported at the next Management Review."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.10
# =============================================================================
