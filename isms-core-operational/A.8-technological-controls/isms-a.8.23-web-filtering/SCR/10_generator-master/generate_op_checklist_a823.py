#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.23 — Web Filtering Compliance Checklist

Control A.8.23: Web Filtering
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Web Filtering Architecture (11 reqs)
4. URL Categorisation & Filtering (5 reqs)
5. TLS Inspection (5 reqs)
6. Threat Intelligence Integration (4 reqs)
7. Exception and Override Process (5 reqs)
8. Remote Worker & BYOD (5 reqs)
9. Employee Privacy & Web (7 reqs)
10. Testing & Validation (2 reqs)
11. Metrics & Mgmt Reporting (1 reqs)

Total: 45 requirements across 9 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.23"
CONTROL_ID = "A.8.23"
CONTROL_NAME = "Web Filtering"
SOURCE_POLICY = "ISMS-OP-POL-A.8.23"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.23
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Web Filtering Architecture", [
        ("A.8.23-01", "Implement Web Filtering Using One Or",
         "The organisation shall implement web filtering using one or more of the following technologies:."),
        ("A.8.23-02", "Dns Filtering",
         "DNS filtering shall be enforced on all managed devices as the baseline. Direct DNS queries to external resolvers (including DNS over HTTPS (DoH) and DNS over TLS (DoT) to non-approved resolvers) shall be blocked at the firewall to prevent filter bypass."),
        ("A.8.23-03", "The Web Filtering Platform",
         "The web filtering platform shall meet the following service level objectives:."),
        ("A.8.23-04", "It Operations",
         "If the filtering platform experiences sustained degradation exceeding SLO thresholds, IT Operations shall implement the documented incident response procedure. Fail-open (allowing unfiltered traffic) is permitted only as a temporary measure during platform failure and shall be logged, reported to the CISO, and remediated within 4 hours."),
        ("A.8.23-05", "Changes To Web Filtering Configuration",
         "Changes to web filtering configuration (category policies, block/allow lists, TLS inspection settings, deployment architecture) shall follow the organisation's change management process:."),
        ("A.8.23-06", "Emergency Changes (E.G., Blocking An",
         "Emergency changes (e.g., blocking an active phishing campaign) may bypass standard approval but shall be retrospectively documented within 24 hours."),
        ("A.8.23-07", "The Vendor",
         "The vendor shall be included in the organisation's vendor risk management programme."),
        ("A.8.23-08", "Soc 2 Type Ii Report Or",
         "SOC 2 Type II report or ISO 27001 certification shall be reviewed annually."),
        ("A.8.23-09", "Sla Compliance (Availability, Latency,",
         "SLA compliance (availability, latency, threat detection rate, support response time) shall be monitored against contractual thresholds."),
        ("A.8.23-10", "Data Processing Agreements",
         "Data processing agreements shall address: employee browsing data handling, data residency, retention periods, and incident notification."),
        ("A.8.23-11", "Vendor Lock-In Risk",
         "Vendor lock-in risk shall be assessed; the organisation shall maintain the ability to migrate to an alternative provider within a reasonable timeframe."),
    ]),

    ("URL Categorisation & Filtering", [
        ("A.8.23-12", "The Following Categories",
         "The following categories shall be blocked for all users without exception:."),
        ("A.8.23-13", "The Following Categories",
         "The following categories shall be blocked unless an approved exception exists:."),
        ("A.8.23-14", "The Following Categories",
         "The following categories shall not be filtered or restricted:."),
        ("A.8.23-15", "Websites Not Categorised By The",
         "Websites not categorised by the filtering solution shall be handled as follows:."),
        ("A.8.23-16", "Access To Uncategorised Sites",
         "All access to uncategorised sites shall be logged for security review."),
    ]),

    ("TLS Inspection", [
        ("A.8.23-17", "The Following Categories",
         "The following categories shall be excluded from TLS inspection to protect privacy and avoid technical issues:."),
        ("A.8.23-18", "Be Informed In Advance That Encrypted",
         "Employees shall be informed in advance that encrypted web traffic may be decrypted and inspected for security purposes."),
        ("A.8.23-19", "The Acceptable Use Policy",
         "The acceptable use policy shall document TLS inspection and its purpose."),
        ("A.8.23-20", "Tls Inspection Data",
         "TLS inspection data shall be processed only for security purposes (malware detection, data leakage prevention, policy enforcement) — not for behavioural monitoring."),
        ("A.8.23-21", "Byod And Guest Network Traffic",
         "BYOD and guest network traffic shall not be subject to TLS inspection."),
    ]),

    ("Threat Intelligence Integration", [
        ("A.8.23-22", "Web Filtering Block Lists",
         "Web filtering block lists shall be updated using threat intelligence from multiple sources:."),
        ("A.8.23-23", "Employee-Reported Phishing Urls",
         "Employee-reported phishing URLs shall be assessed and added to the block list within 4 hours during business hours."),
        ("A.8.23-24", "Phishing Simulation Urls",
         "Phishing simulation URLs shall be excluded from web filtering during testing campaigns (coordinated between Information Security and IT Operations)."),
        ("A.8.23-25", "Web Filtering Events",
         "Web filtering events shall be integrated with the organisation's incident management process (A.5.24-28). The following thresholds shall trigger incident creation:."),
    ]),

    ("Exception and Override Process", [
        ("A.8.23-26", "Be Reviewed Quarterly By It Security",
         "All exceptions shall be reviewed quarterly by IT Security."),
        ("A.8.23-27", "Expired Exceptions",
         "Expired exceptions shall be automatically revoked."),
        ("A.8.23-28", "Unused Exceptions (No Access Recorded In",
         "Unused exceptions (no access recorded in 90 days) shall be removed."),
        ("A.8.23-29", "The Total Number Of Active Exceptions",
         "The total number of active exceptions shall be reported to the CISO quarterly."),
        ("A.8.23-30", "Be The Minimum Scope Needed: Specific",
         "Exceptions shall be the minimum scope needed: specific URL preferred over full domain; domain preferred over entire category."),
    ]),

    ("Remote Worker & BYOD", [
        ("A.8.23-31", "Cloud-Delivered Swg Or Dns Filtering",
         "Cloud-delivered SWG or DNS filtering agent shall be installed on all managed endpoints."),
        ("A.8.23-32", "Web Filtering Policies",
         "Web filtering policies shall apply consistently whether the user is on the corporate network, home Wi-Fi, mobile hotspot, or public network."),
        ("A.8.23-33", "Split Tunnelling (Vpn)",
         "Split tunnelling (VPN) shall not bypass web filtering; web traffic shall be routed through the filtering solution regardless of VPN configuration."),
        ("A.8.23-34", "Tls Inspection",
         "TLS inspection shall not be performed on personal devices (privacy and legal constraints)."),
        ("A.8.23-35", "Separate, Less Intrusive Filtering",
         "Separate, less intrusive filtering policies shall apply to BYOD compared to corporate-managed devices."),
    ]),

    ("Employee Privacy & Web", [
        ("A.8.23-36", "Web Filtering That Processes Employee",
         "Web filtering that processes employee browsing data shall comply with Swiss employment law:."),
        ("A.8.23-37", "Argv3 Art. 26: Web Filtering Systems",
         "ArGV3 Art. 26: Web filtering systems shall not be used primarily to monitor employee behaviour. Their purpose is security (malware prevention, data leakage prevention, policy enforcement)."),
        ("A.8.23-38", "Co Art. 328B: Processing Of Employee",
         "CO Art. 328b: Processing of employee web browsing data shall be proportional and limited to security purposes."),
        ("A.8.23-39", "Transparency: Employees",
         "Transparency: Employees shall be informed that web filtering is in place, what categories are filtered, and that access to blocked sites is logged. This information shall be included in the acceptable use policy and employment documentation."),
        ("A.8.23-40", "Non-Personalised Monitoring By Default:",
         "Non-personalised monitoring by default: Web filtering logs shall be reviewed in aggregate for security monitoring (e.g., total blocked requests by category, top blocked domains). Individual user browsing activity shall not be reviewed unless:."),
        ("A.8.23-41", "Purpose Limitation: Web Filtering Data",
         "Purpose limitation: Web filtering data shall not be used for HR performance evaluation, disciplinary action for non-security matters, or general behavioural profiling."),
        ("A.8.23-42", "Data Minimisation: Web Filtering Logs",
         "Data minimisation: Web filtering logs shall be retained only as long as necessary for security purposes (per log retention schedule in the Logging and Monitoring Policy, A.8.15)."),
    ]),

    ("Testing & Validation", [
        ("A.8.23-43", "The Effectiveness Of Web Filtering",
         "The effectiveness of web filtering controls shall be tested on a regular basis:."),
        ("A.8.23-44", "Test Results",
         "Test results shall be documented and remediation actions tracked for any identified weaknesses."),
    ]),

    ("Metrics & Mgmt Reporting", [
        ("A.8.23-45", "The Following Metrics",
         "The following metrics shall be reported:."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.23
# =============================================================================
