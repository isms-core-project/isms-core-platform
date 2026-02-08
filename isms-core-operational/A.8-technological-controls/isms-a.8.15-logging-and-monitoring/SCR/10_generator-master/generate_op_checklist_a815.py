#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.15 — Logging and Monitoring Compliance Checklist

Control A.8.15: Logging and Monitoring
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Event Logging (2 reqs)
4. Event Logging Access Control (3 reqs)
5. Protection of Event Log Info (4 reqs)
6. Centralised Logging (4 reqs)
7. Administrator and Operator Logs (4 reqs)
8. Clock Synchronisation (7 reqs)
9. Event Log Monitoring (3 reqs)
10. Event Log Retention (3 reqs)
11. Swiss nFADP — DSV Article 4 (2 reqs)
12. Personal Privacy (7 reqs)

Total: 39 requirements across 10 domains
"""

import sys
from pathlib import Path
from collections import OrderedDict

# Engine: 10-isms-core-operational/A.0-checklist-engine/op_checklist_engine.py
_OP_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(_OP_ROOT / 'A.0-checklist-engine'))
from op_checklist_engine import generate_checklist

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-OP-CHK-A.8.15"
CONTROL_ID = "A.8.15"
CONTROL_NAME = "Logging and Monitoring"
SOURCE_POLICY = "ISMS-OP-POL-A.8.15"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.15
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Event Logging", [
        ("A.8.15-01", "Event Logs Recording User Activities,",
         "Event logs recording user activities, exceptions, faults, and information security events shall be produced, kept, and regularly reviewed. The following events shall be logged:."),
        ("A.8.15-02", "Log Entry",
         "Each log entry shall include, at minimum:."),
    ]),

    ("Event Logging Access Control", [
        ("A.8.15-03", "Event Logging And Monitoring",
         "Event logging and monitoring shall be performed by authorised personnel only."),
        ("A.8.15-04", "Event Logs And Monitoring Systems",
         "Event logs and monitoring systems shall be protected and access restricted in line with the Access Control Policy. Access to raw logs shall be limited to the information security management team and authorised IT personnel."),
        ("A.8.15-05", "System Administrators",
         "System administrators shall not have permission to erase or deactivate logs of their own activities. Where this is not technically enforceable, compensating controls shall be implemented (e.g., forwarding logs to a central system outside the administrator's control, periodic review of administrator activity by a separate role)."),
    ]),

    ("Protection of Event Log Info", [
        ("A.8.15-06", "Logging Facilities And Log Information",
         "Logging facilities and log information shall be protected against tampering and unauthorised access."),
        ("A.8.15-07", "Protect Against",
         "Controls shall protect against:."),
        ("A.8.15-08", "Storage Exhaustion Causing Loss Of Log",
         "Storage exhaustion causing loss of log data (logs shall fail open — alert when storage reaches 80% capacity rather than silently overwriting). Log storage capacity shall be monitored continuously, with automated alerts at 80% and 90% thresholds. When 90% capacity is reached, archived logs shall be offloaded to long-term storage and the platform team shall assess whether additional capacity is required."),
        ("A.8.15-09", "Log Protection",
         "Log protection shall be achieved through:."),
    ]),

    ("Centralised Logging", [
        ("A.8.15-10", "The Centralised Logging Platform",
         "The centralised logging platform shall meet the following requirements:."),
        ("A.8.15-11", "Logs From All Critical Systems",
         "Logs from all critical systems shall be forwarded to the centralised logging platform. The platform shall be:."),
        ("A.8.15-12", "Separate From The Systems Generating The",
         "Separate from the systems generating the logs (source system administrators shall not have administrative access to the central log store)."),
        ("A.8.15-13", "Manual Log Collection And Review",
         "Where automated centralised logging is not feasible for a specific system, manual log collection and review shall be performed at a defined frequency with documented justification."),
    ]),

    ("Administrator and Operator Logs", [
        ("A.8.15-14", "System Administrator And System Operator",
         "System administrator and system operator activities shall be logged, and the logs protected and regularly reviewed."),
        ("A.8.15-15", "Administrator Actions",
         "Administrator actions shall be forwarded to the centralised logging system in real-time or near-real-time."),
        ("A.8.15-16", "A Periodic Review Of Privileged User",
         "A periodic review of privileged user activity shall be conducted (at least quarterly)."),
        ("A.8.15-17", "Anomalous Privileged Activity (E.G.,",
         "Anomalous privileged activity (e.g., after-hours access, bulk data operations, security configuration changes) shall generate alerts."),
    ]),

    ("Clock Synchronisation", [
        ("A.8.15-18", "The Clocks Of All Information Processing",
         "The clocks of all information processing systems within the organisation shall be synchronised to a single, consistent reference time source."),
        ("A.8.15-19", "An Internal Ntp Server (Or The",
         "An internal NTP server (or the primary domain controller) shall be designated as the organisation's reference time source."),
        ("A.8.15-20", "The Internal Reference",
         "The internal reference shall synchronise to at least two independent external Stratum 1 or Stratum 2 NTP servers (e.g., ch.pool.ntp.org, ntp.metas.ch)."),
        ("A.8.15-21", "Organisation Systems (Servers,",
         "All organisation systems (servers, workstations, network devices, cloud services) shall synchronise to the internal reference."),
        ("A.8.15-22", "Clock Drift Exceeding 1 Second On",
         "Clock drift exceeding 1 second on any critical system shall generate an alert."),
        ("A.8.15-23", "Log Timestamps",
         "Log timestamps shall be recorded in UTC or with a defined timezone offset to enable correlation across systems in different locations."),
        ("A.8.15-24", "Time Synchronisation Settings",
         "Time synchronisation settings shall be documented and protected from unauthorised modification."),
    ]),

    ("Event Log Monitoring", [
        ("A.8.15-25", "Be Assigned For The Analysis And",
         "Responsibilities shall be assigned for the analysis and monitoring of security events."),
        ("A.8.15-26", "The Following Events",
         "The following events shall trigger immediate automated alerts and be escalated to the incident management process:."),
        ("A.8.15-27", "The Following Escalation Process",
         "When a high-risk event is detected, the following escalation process shall be followed:."),
    ]),

    ("Event Log Retention", [
        ("A.8.15-28", "Archived Logs",
         "Archived logs shall be encrypted, stored in a secure location, and retrievable within the following timeframes:."),
        ("A.8.15-29", "Retrieval Procedures",
         "Retrieval procedures shall be tested at least annually to verify that archived logs are accessible and intact."),
        ("A.8.15-30", "Not Be Retained Longer Than Necessary",
         "Logs shall not be retained longer than necessary. When retention periods expire, logs shall be securely deleted in line with the Information Classification and Handling Policy."),
    ]),

    ("Swiss nFADP — DSV Article 4", [
        ("A.8.15-31", "Log Storage: Logs Of Sensitive Personal",
         "Log storage: Logs of sensitive personal data processing shall be stored separately from the processing system, retained for a minimum of 1 year*, and access restricted to verifying data security compliance and ensuring confidentiality, integrity, availability, and traceability."),
        ("A.8.15-32", "Determine Whether Dsv Art. 4 Applies",
         "The organisation shall determine whether DSV Art. 4 applies by assessing the following criteria:."),
    ]),

    ("Personal Privacy", [
        ("A.8.15-33", "The Privacy Of Employees And Customers",
         "The privacy of employees and customers shall be respected in line with Swiss nFADP and applicable legal requirements when implementing logging and monitoring."),
        ("A.8.15-34", "Logging Systems",
         "Logging systems shall serve legitimate security purposes (detecting threats, investigating incidents, verifying compliance) — not primarily for monitoring employee behaviour."),
        ("A.8.15-35", "Be Informed In Advance That Logging",
         "Employees shall be informed in advance that logging takes place, what is logged, and why, through the information security awareness programme and employment documentation."),
        ("A.8.15-36", "Only The Minimum Necessary Data",
         "Only the minimum necessary data shall be collected and retained (data minimisation)."),
        ("A.8.15-37", "Access To Logs",
         "Access to logs containing employee data shall be restricted to authorised security and compliance personnel only — not line managers for general browsing."),
        ("A.8.15-38", "Keystroke Logging And Continuous",
         "Keystroke logging and continuous individual activity surveillance are disproportionate and shall not be implemented."),
        ("A.8.15-39", "Vendors For Troubleshooting), Personal",
         "Where logs containing personal data are shared with external parties (e.g., vendors for troubleshooting), personal identifiers shall be masked or anonymised."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.15
# =============================================================================
