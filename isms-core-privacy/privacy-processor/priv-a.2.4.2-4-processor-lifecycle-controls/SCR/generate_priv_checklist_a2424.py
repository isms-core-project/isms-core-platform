#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
PRIV-CHK-A.2.4.2-4 — Processor Lifecycle Controls Compliance Checklist

Controls A.2.4.2-4: Temporary Files (Processor), Return/Transfer/Disposal of
                     Customer PII, PII Transmission Controls (Processor)
Product: ISMS CORE Privacy (ISO/IEC 27701:2025 — Processor Controls)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Temporary Files — Processor (A.2.4.2) — 4 reqs
4. Return, Transfer or Disposal (A.2.4.3) — 5 reqs
5. Transmission Controls — Processor (A.2.4.4) — 4 reqs

Total: 13 requirements across 3 domains
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
DOCUMENT_ID = "PRIV-CHK-A.2.4.2-4"
CONTROL_ID = "A.2.4.2-4"
CONTROL_NAME = "Processor Lifecycle Controls"
SOURCE_POLICY = "PRIV-POL-A.2.4.2-4"

# =============================================================================
# REQUIREMENTS DATA — extracted from PRIV-POL-A.2.4.2-4
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Temporary Files — Processor", [
        ("A.2.4.2-01", "Documented Disposal Periods",
         "Temporary files created as a result of processing customer PII shall be disposed of within documented, specified periods. A schedule of temporary file types and maximum retention periods shall be maintained and made available to customers."),
        ("A.2.4.2-02", "Disposal Periods",
         "Processing cache and staging files shall be disposed within 48 hours of processing completion. Error/exception logs containing customer PII shall be disposed within 30 days (automated rotation). Export files generated for customer delivery shall be disposed within 72 hours after confirmed delivery."),
        ("A.2.4.2-03", "Automated Purge",
         "Automated purge mechanisms are preferred over manual deletion for customer PII temporary files. Where automated purge is not technically feasible, manual deletion shall be scheduled, logged, and confirmed."),
        ("A.2.4.2-04", "Purge Confirmation",
         "Purge confirmation records (automated or manual) for customer PII temporary files shall be maintained for 3 years, sufficient to demonstrate compliance to customers and supervisory authorities."),
    ]),

    ("Return, Transfer or Disposal", [
        ("A.2.4.3-01", "End-of-Service Capability",
         "When a customer contract ends or a customer requests return or deletion of their PII, the organisation shall be able to return the PII in an agreed format, transfer it to another processor designated by the customer, or dispose of it securely using approved erasure methods — at the customer's instruction."),
        ("A.2.4.3-02", "Customer Instruction",
         "The organisation shall follow the customer's documented instruction for end-of-service PII handling. In the absence of a specific customer instruction, the organisation shall request instructions and follow the default specified in the processor agreement."),
        ("A.2.4.3-03", "Disposal Standards",
         "Disposal of customer PII at contract end shall use approved methods: database records via SQL DELETE or cryptographic erasure; file system via cryptographic erasure or approved overwrite; backup media aligned to backup retention schedule with confirmed deletion. Methods are consistent with PRIV-POL-A.1.4.6-10 (A.1.4.9)."),
        ("A.2.4.3-04", "Disposal Confirmation",
         "Disposal shall be confirmed in writing to the customer within the timeframe specified in the processor agreement (typically within 30 days of service end). Written disposal confirmation records shall be retained for 5 years."),
        ("A.2.4.3-05", "Policy Availability",
         "The organisation's return, transfer, and disposal policy shall be made available to customers on request and, where contractually required, as part of the processor agreement documentation."),
    ]),

    ("Transmission Controls — Processor", [
        ("A.2.4.4-01", "Encryption in Transit",
         "All customer PII transmitted over networks shall be encrypted in transit using current TLS standards (minimum TLS 1.2; TLS 1.3 preferred). Unencrypted transmission of CONFIDENTIAL or RESTRICTED customer PII over public networks is prohibited."),
        ("A.2.4.4-02", "Approved Transfer Methods",
         "CONFIDENTIAL and RESTRICTED customer PII transmissions shall use approved secure transfer methods consistent with PRIV-POL-A.3.5-7. The organisation shall ensure that data reaches its intended destination and is not interceptable or diverted."),
        ("A.2.4.4-03", "Delivery Confirmation",
         "Delivery confirmation or receipt acknowledgment shall be obtained for RESTRICTED PII transmissions to third parties (including sub-processors and customers). Confirmation records shall be maintained."),
        ("A.2.4.4-04", "Transmission Logging",
         "Transmission logs for customer PII carried over networks shall be maintained per PRIV-POL-A.3.23-31 logging requirements, sufficient to identify what was transmitted, to whom, and when."),
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
