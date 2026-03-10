#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
CLD-CHK-A.10 — Accountability Compliance Checklist

Controls A.10.1-A.10.3: Breach Notification, Document Retention,
                         PII Return, Transfer and Disposal
Product: ISMS CORE Cloud (ISO/IEC 27018:2025 — Annex A)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Breach Notification to PII Controllers (A.10.1) — 4 reqs
4. Document Retention (A.10.2) — 3 reqs
5. PII Return, Transfer and Disposal (A.10.3) — 4 reqs

Total: 11 requirements across 3 domains
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
DOCUMENT_ID = "CLD-CHK-A.10"
CONTROL_ID = "A.10.1-3"
CONTROL_NAME = "Accountability"
SOURCE_POLICY = "CLD-POL-A.10"

# =============================================================================
# REQUIREMENTS DATA — extracted from CLD-POL-A.10
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Breach Notification to PII Controllers", [
        ("A.10.1-01", "24-Hour Notification Obligation",
         "The organisation shall notify the relevant PII controller of any confirmed or reasonably suspected PII security incident without undue delay, and in any case within 24 hours of detection. This timeframe ensures the controller has sufficient time to fulfil its own 72-hour GDPR supervisory authority notification obligation under Article 33."),
        ("A.10.1-02", "Notification Content",
         "Breach notifications to PII controllers shall include the following information to the extent available: nature of the breach (type of incident); categories of PII affected; approximate number of data subjects affected; likely consequences for data subjects; measures taken or proposed for containment and remediation; the organisation's internal incident reference number; and DPO or security contact details. Where information is not fully available initially, phased updates shall be provided without undue delay."),
        ("A.10.1-03", "Breach Response Process",
         "The organisation's breach response process shall include: detection (Security Operations or Cloud Engineering identifies potential PII incident); triage within 2 hours (CISO determines PII involvement, activates PII breach response if confirmed or suspected); initial notification within 24 hours of detection (DPO notifies affected PII controller(s)); parallel containment and investigation with phased controller updates; and final incident report provided to controller upon closure."),
        ("A.10.1-04", "Breach Notification Records",
         "All notifications sent to PII controllers shall be documented with timestamps and content. Final post-incident reports for all PII security events shall be retained for 5 years. Where a controller's 72-hour GDPR clock is relevant, the organisation's notification timestamp shall predate any supervisory authority notification deadline for which the controller could be penalised."),
    ]),

    ("Document Retention", [
        ("A.10.2-01", "Retention Schedule",
         "The organisation shall retain the following administrative documentation for the defined minimum periods: CLD-POL-A.X cloud security policies (all versions) — 5 years from version supersession; sub-processor agreements and registers — duration of engagement plus 5 years; PII processing records (records of processing activities) — duration of processing plus 5 years; breach notification records and incident reports — 5 years from incident closure; PII disclosure records — 5 years from disclosure; data return or disposal confirmations — 5 years from completion; security assessment and audit reports — 5 years; controller service agreements — duration of agreement plus 5 years."),
        ("A.10.2-02", "Policy Version History",
         "All CLD-POL-A.X policy documents shall maintain a version history capturing document version, date, author, and summary of changes. Previous versions shall be retained in accordance with the retention schedule. Version history enables retrospective audit and incident investigation where questions arise about the controls in effect at a specific point in time."),
        ("A.10.2-03", "Retention Compliance Verification",
         "The DPO shall verify compliance with the retention schedule at minimum annually, confirming that required documents are accessible and that no documents have been prematurely deleted. Retention compliance verification records shall be maintained for 3 years."),
    ]),

    ("PII Return, Transfer and Disposal", [
        ("A.10.3-01", "End-of-Contract Obligation",
         "Upon termination or expiry of a cloud service agreement under which the organisation processes PII, the organisation shall, as instructed by the PII controller: return all PII in a structured machine-readable format (JSON, CSV, or standard database export as agreed) within 30 calendar days of termination; or securely destroy all PII (including primary stores, backups, replicated copies, and sub-processor copies) using methods that prevent recovery within 30 calendar days, providing a written certificate of destruction."),
        ("A.10.3-02", "Backup and Replicated Copies",
         "Where PII exists in backup or replicated copies at the time of contract termination, the organisation shall include backup copies in the return or disposal process, define in the service agreement the maximum timeframe for backup disposal (accounting for backup rotation cycles), and confirm in writing when backup disposal is complete. The 30-day return or disposal obligation shall be interpreted as complete only when backup copies are also addressed."),
        ("A.10.3-03", "Written Confirmation",
         "The organisation shall provide the PII controller with written confirmation of completed return or disposal, including: date of return delivery or disposal completion; scope of PII returned or disposed of (categories and approximate volume); disposal method (where disposal was chosen); and confirmation that sub-processor PII has also been returned or disposed of. Written confirmations and certificates of destruction shall be retained for 5 years."),
        ("A.10.3-04", "Sub-processor Disposal Coordination",
         "Where sub-processors hold copies of controller PII at contract termination, the organisation shall coordinate sub-processor return or disposal to coincide with the primary disposal process. Sub-processor disposal confirmations shall be obtained and retained. The organisation remains accountable to the controller for sub-processor PII disposal."),
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
