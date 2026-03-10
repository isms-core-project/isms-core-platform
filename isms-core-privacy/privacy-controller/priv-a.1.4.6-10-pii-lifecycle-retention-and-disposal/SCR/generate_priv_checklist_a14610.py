#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.1.4.6-10 — PII Lifecycle, Retention and Disposal Compliance Checklist

Controls A.1.4.6-10: De-identification/Deletion at End of Processing, Temporary
                      Files, Retention, Disposal, PII Transmission Controls
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Controller Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. De-identification and Deletion (A.1.4.6) — 4 reqs
4. Temporary Files (A.1.4.7) — 3 reqs
5. Retention Management (A.1.4.8) — 5 reqs
6. Disposal Procedures (A.1.4.9) — 4 reqs
7. Transmission Controls (A.1.4.10) — 4 reqs

Total: 20 requirements across 5 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 51-isms-core-privacy/00-checklist-engine/priv_checklist_engine.py
_PRIV_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(_PRIV_ROOT / '00-checklist-engine'))
from priv_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "PRIV-CHK-A.1.4.6-10"
CONTROL_ID = "A.1.4.6-10"
CONTROL_NAME = "PII Lifecycle, Retention and Disposal"
SOURCE_POLICY = "PRIV-POL-A.1.4.6-10"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.1.4.6-10
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("De-identification and Deletion", [
        ("A.1.4.6-01", "End-of-Purpose Obligation",
         "When PII is no longer necessary for the identified processing purpose(s), the organisation shall either delete the PII (irreversible destruction) or de-identify it to a form that does not permit identification or re-identification of PII principals. This obligation applies as soon as the purpose is no longer served."),
        ("A.1.4.6-02", "All Copies",
         "The deletion or de-identification obligation applies to all copies of PII: primary databases, backups, archives, processing logs, and temporary copies. A single primary deletion is not sufficient if copies persist in secondary locations."),
        ("A.1.4.6-03", "Legal Hold Retention",
         "Where a legal obligation requires retention beyond the processing purpose (e.g. tax records, employment records, legal hold), retention shall be limited to the legally required period, restricted to the minimum scope, and clearly recorded in the Retention Schedule with the legal provision reference."),
        ("A.1.4.6-04", "Anonymisation Confirmation",
         "Where de-identification is used in lieu of deletion, the DPO shall confirm in writing that the de-identification method constitutes true anonymisation such that re-identification is not reasonably possible. Pseudonymised data (re-identifiable with a key) does not satisfy this requirement."),
    ]),

    ("Temporary Files", [
        ("A.1.4.7-01", "Temporary File Procedures",
         "The organisation shall ensure that temporary files created as a result of PII processing are disposed of following documented procedures within a specified, documented period. A schedule of temporary file types and maximum retention periods shall be maintained."),
        ("A.1.4.7-02", "Automated Purge",
         "Automated purge mechanisms are preferred over manual deletion for temporary PII files. Where automated purge is not technically feasible, manual deletion shall be scheduled and logged. Processing cache files shall be purged within 24 hours; export files within 72 hours of transmission."),
        ("A.1.4.7-03", "Development Copies",
         "Temporary development copies containing real PII shall be subject to immediate deletion after use. DPO approval is required for any development use of real PII, and deletion confirmation shall be documented."),
    ]),

    ("Retention Management", [
        ("A.1.4.8-01", "Retention Schedule",
         "The DPO shall maintain a PII Retention Schedule specifying: PII category or processing activity; retention period with trigger date; legal or regulatory basis where applicable; and disposal method upon expiry. The schedule forms part of the RoPA."),
        ("A.1.4.8-02", "No Unnecessary Retention",
         "The organisation shall not retain PII for longer than is necessary for the purposes for which it is processed. Retention periods shall be based on documented need — not on the principle of 'keeping just in case'."),
        ("A.1.4.8-03", "Conflicting Retention Obligations",
         "Where multiple regulatory obligations create different retention requirements for the same data, the longest mandatory period applies for the legally required scope; data not required by the longer obligation shall be deleted at the earliest applicable period."),
        ("A.1.4.8-04", "Backup Retention Alignment",
         "Backups containing PII shall be subject to the same retention limits as primary data. Backup retention schedules shall align with PII retention periods or have a documented exception with compensating controls."),
        ("A.1.4.8-05", "Retention Schedule Review",
         "The PII Retention Schedule shall be reviewed at minimum annually, upon changes to regulatory requirements, and when processing activities change materially. Review evidence shall be documented."),
    ]),

    ("Disposal Procedures", [
        ("A.1.4.9-01", "Disposal Requirements",
         "PII disposal shall be irreversible (not recoverable by routine technical means), documented (disposal action logged with date, scope, method), verified where technically feasible, and compliant with the classification level per PRIV-POL-A.3.20-22."),
        ("A.1.4.9-02", "Disposal Methods",
         "Disposal methods shall be appropriate to the data location: database records — SQL DELETE or approved in-place anonymisation; electronic files — cryptographic erasure or approved overwrite; physical documents — cross-cut shredding (CONFIDENTIAL) or cross-cut plus witness (RESTRICTED); cloud storage — deletion via approved API with provider confirmation."),
        ("A.1.4.9-03", "Disposal Triggers",
         "PII disposal shall be triggered by: expiry of the retention period; cessation of the processing purpose; data subject erasure request; consent withdrawal for consent-based processing where no other basis applies; and end of contract or employment for applicable PII categories."),
        ("A.1.4.9-04", "Disposal Logs",
         "Disposal logs shall record each disposal action with: date; PII category and scope disposed; disposal method; identity of person who performed or confirmed disposal. Disposal logs shall be retained for 5 years."),
    ]),

    ("Transmission Controls", [
        ("A.1.4.10-01", "Encryption in Transit",
         "All PII transmitted over networks shall be encrypted in transit using current TLS standards (minimum TLS 1.2; TLS 1.3 preferred). Unencrypted transmission of CONFIDENTIAL or RESTRICTED PII over public networks is prohibited."),
        ("A.1.4.10-02", "Approved Transfer Methods",
         "PII transmitted to external parties shall use approved secure transfer methods per PRIV-POL-A.3.5-7. Transfer mechanisms shall ensure that PII reaches its intended destination and not be interceptable or diverted."),
        ("A.1.4.10-03", "Restricted PII Delivery Confirmation",
         "Delivery confirmation or receipt acknowledgment shall be obtained for transfers of RESTRICTED PII (special category). Confirmation records shall be maintained and cross-referenced with the Disclosure Register."),
        ("A.1.4.10-04", "Transmission Logging",
         "Transmission logs shall be maintained for CONFIDENTIAL and RESTRICTED PII transfers per PRIV-POL-A.3.23-31 logging requirements. Logs shall be sufficient to identify what was transmitted, to whom, and when."),
    ]),
])


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    sys.exit(generate_checklist(
        DOCUMENT_ID, CONTROL_ID, CONTROL_NAME, SOURCE_POLICY, REQUIREMENTS,
        iso_standard="ISO/IEC 27701:2025"
    ))


# =============================================================================
# QA_VERIFIED: 2026-03-10
# QA_STATUS: PASSED
# QA_TOOL: Claude Code Production Scripts QA Methodology
# CHANGES: Initial generation for Privacy product launch
# =============================================================================
