#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.17 — Clock Synchronisation Compliance Checklist

Control A.8.17: Clock Synchronisation
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Authoritative Time Sources (3 reqs)
4. Synchronisation Protocol (3 reqs)
5. Timestamp Format (4 reqs)
6. Clock Drift Tolerances (4 reqs)
7. Cloud Service Time (1 reqs)
8. Leap Second Handling (1 reqs)
9. NTP Security (4 reqs)

Total: 20 requirements across 7 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.17"
CONTROL_ID = "A.8.17"
CONTROL_NAME = "Clock Synchronisation"
SOURCE_POLICY = "ISMS-OP-POL-A.8.17"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.17
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Authoritative Time Sources", [
        ("A.8.17-01", "Designate A Primary Authoritative Time",
         "The organisation shall designate a primary authoritative time source:."),
        ("A.8.17-02", "Deploy Internal Ntp Servers In A",
         "The organisation shall deploy internal NTP servers in a tiered architecture:."),
        ("A.8.17-03", "Air-Gapped Networks), These",
         "Where the organisation operates GPS-disciplined oscillators (GPSDOs) for Stratum 0/1 independence (e.g., air-gapped networks), these shall be documented and maintained per manufacturer specifications."),
    ]),

    ("Synchronisation Protocol", [
        ("A.8.17-04", "Network Time Protocol (Ntp)",
         "Network Time Protocol (NTP) shall be used for time synchronisation across all standard enterprise systems."),
        ("A.8.17-05", "Financial Trading, Industrial Control,",
         "Where sub-microsecond accuracy is required (e.g., financial trading, industrial control, high-frequency data processing), IEEE 1588 Precision Time Protocol (PTPv2) shall be deployed:."),
        ("A.8.17-06", "A Ptp Grandmaster Clock",
         "A PTP grandmaster clock (GPS-disciplined) shall be deployed."),
    ]),

    ("Timestamp Format", [
        ("A.8.17-07", "Record Timestamps In One Of The",
         "All systems shall record timestamps in one of the following formats:."),
        ("A.8.17-08", "Iso 8601 / Rfc 3339 Format",
         "ISO 8601 / RFC 3339 format shall be used for all machine-generated timestamps."),
        ("A.8.17-09", "Named Timezone Abbreviations",
         "Named timezone abbreviations shall not be used in log timestamps."),
        ("A.8.17-10", "Use Utc Or Explicit Offset To",
         "All systems shall use UTC or explicit offset to prevent DST-related timestamp ambiguity."),
    ]),

    ("Clock Drift Tolerances", [
        ("A.8.17-11", "Maintain Clock Accuracy Within The",
         "Systems shall maintain clock accuracy within the following tolerances:."),
        ("A.8.17-12", "Clock Drift",
         "Clock drift shall be monitored continuously using system monitoring tools (e.g., Prometheus, Nagios, CloudWatch, or equivalent):."),
        ("A.8.17-13", "Ntp Offset, Jitter, And Stratum Metrics",
         "NTP offset, jitter, and stratum metrics shall be collected from all monitored systems."),
        ("A.8.17-14", "Clock Drift Alerts",
         "Clock drift alerts shall be forwarded to the centralised monitoring platform."),
    ]),

    ("Cloud Service Time", [
        ("A.8.17-15", "The Provider'S Time Synchronisation",
         "Where systems run in cloud environments, the provider's time synchronisation service shall be used:."),
    ]),

    ("Leap Second Handling", [
        ("A.8.17-16", "Adopt A Single, Consistent Leap Second",
         "The organisation shall adopt a single, consistent leap second handling strategy across all environments:."),
    ]),

    ("NTP Security", [
        ("A.8.17-17", "Ntp Infrastructure",
         "NTP infrastructure shall be protected against spoofing, replay, and denial-of-service attacks:."),
        ("A.8.17-18", "Ntp Configuration Files",
         "NTP configuration files shall be protected from unauthorised modification (file permissions, integrity monitoring)."),
        ("A.8.17-19", "Changes To Ntp Configuration",
         "Changes to NTP configuration shall follow the change management process."),
        ("A.8.17-20", "Ntp Service Status",
         "NTP service status shall be monitored; service failure shall generate an alert."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.17
# =============================================================================
