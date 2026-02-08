#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.16 — Monitoring Activities Compliance Checklist

Control A.8.16: Monitoring Activities
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. What to Monitor (2 reqs)
4. Behavioural Baselines (5 reqs)
5. Monitoring Architecture (8 reqs)
6. Alert Management (9 reqs)
7. Key Performance Indicators (1 reqs)
8. Employee Privacy and Monitoring (9 reqs)

Total: 34 requirements across 6 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.16"
CONTROL_ID = "A.8.16"
CONTROL_NAME = "Monitoring Activities"
SOURCE_POLICY = "ISMS-OP-POL-A.8.16"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.16
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("What to Monitor", [
        ("A.8.16-01", "The Following",
         "The following shall be monitored for anomalous behaviour and security events:."),
        ("A.8.16-02", "Be Prioritised For Monitoring Based On",
         "Systems shall be prioritised for monitoring based on risk:."),
    ]),

    ("Behavioural Baselines", [
        ("A.8.16-03", "Before Anomaly Detection Is Effective,",
         "Before anomaly detection is effective, the organisation shall establish baselines of normal behaviour. Initial baselines shall be established within 30 days of monitoring deployment for each system or system group. During the baseline establishment period, monitoring shall operate in 'learning mode' — alerts shall be generated but reviewed with increased tolerance for false positives until baselines are validated."),
        ("A.8.16-04", "Document",
         "Baselines shall document:."),
        ("A.8.16-05", "Be Reviewed And Updated",
         "Baselines shall be reviewed and updated:."),
        ("A.8.16-06", "Monitoring Systems",
         "Monitoring systems shall be configured to detect deviations from established baselines, including:."),
        ("A.8.16-07", "User Behaviour Anomalies: Access Outside",
         "User behaviour anomalies: access outside normal working hours, access to resources not previously accessed, impossible travel between geographic locations. Impossible travel is defined as authentication events from two geographic locations within a timeframe that makes physical travel between them implausible (e.g., logins from Zurich and Tokyo within 2 hours). The organisation shall define impossible travel parameters based on: maximum plausible travel speed, VPN/proxy exclusions for known corporate exit points, and tolerance for mobile device location inaccuracy."),
    ]),

    ("Monitoring Architecture", [
        ("A.8.16-08", "Deploy A Centralised Monitoring Platform",
         "The organisation shall deploy a centralised monitoring platform capable of:."),
        ("A.8.16-09", "A Layered Monitoring Approach",
         "A layered monitoring approach shall be implemented:."),
        ("A.8.16-10", "Cloud Audit Logs (Aws Cloudtrail, Azure",
         "Cloud audit logs (AWS CloudTrail, Azure Activity Log, GCP Cloud Audit Logs) shall be forwarded to the centralised monitoring platform."),
        ("A.8.16-11", "Cloud Security Posture Changes (E.G.,",
         "Cloud security posture changes (e.g., public S3 bucket creation, security group modification, IAM policy changes) shall generate immediate alerts."),
        ("A.8.16-12", "Saas Administrative Actions (M365 Admin",
         "SaaS administrative actions (M365 admin portal, Google Workspace admin, Salesforce setup changes) shall be monitored for unauthorised configuration changes."),
        ("A.8.16-13", "Cloud Api Activity",
         "Cloud API activity shall be monitored for unusual volumes, access from unexpected locations, and use of deprecated or high-risk API endpoints."),
        ("A.8.16-14", "The Monitoring Infrastructure Itself",
         "The monitoring infrastructure itself shall be monitored to ensure continuous availability:."),
        ("A.8.16-15", "Monthly Health Report: It Operations",
         "Monthly health report: IT Operations shall produce a monthly monitoring platform health report covering uptime, ingestion rates, agent coverage, and capacity projections."),
    ]),

    ("Alert Management", [
        ("A.8.16-16", "Be Classified By Severity To Drive",
         "Alerts shall be classified by severity to drive response timelines:."),
        ("A.8.16-17", "Alert Response Staffing Model*: The",
         "Alert response staffing model*: The organisation shall define its alert response staffing approach:."),
        ("A.8.16-18", "The Chosen Model",
         "The chosen model shall be documented and approved by the CISO. After-hours response capability shall be tested quarterly."),
        ("A.8.16-19", "Detection Rules",
         "Detection rules shall be reviewed and tuned monthly to reduce false positive rates."),
        ("A.8.16-20", "Suppression Rules",
         "Suppression rules shall be documented with justification and reviewed quarterly."),
        ("A.8.16-21", "New Detection Rules",
         "New detection rules shall be added when: threat intelligence identifies new attack patterns, incidents reveal detection gaps, or new systems/applications are deployed."),
        ("A.8.16-22", "Detection Rule Change Control: All",
         "Detection rule change control: All changes to detection rules (new rules, modifications, suppressions, deletions) shall follow a documented process: change request with justification, peer review by a second analyst, testing in a non-production/staging environment where feasible, approval by the Information Security lead, and deployment with rollback capability. Emergency rule changes (e.g., in response to an active threat) may bypass peer review but shall be retrospectively reviewed within 48 hours."),
        ("A.8.16-23", "Alert Volumes And False Positive Rates",
         "Alert volumes and false positive rates shall be tracked as key performance indicators."),
        ("A.8.16-24", "False Positive Management Process: When",
         "False positive management process: When a false positive is identified, the analyst shall: (a) document the root cause (misconfigured rule, legitimate business process, environmental noise), (b) determine the appropriate action (tune rule, add exception, suppress with expiry, accept), (c) implement the change through the detection rule change control process, and (d) verify the tuning does not suppress true positives. Persistent false positive sources (>10 occurrences per week from the same rule) shall be prioritised for tuning within 5 business days."),
    ]),

    ("Key Performance Indicators", [
        ("A.8.16-25", "The Following Metrics",
         "The following metrics shall be tracked to measure monitoring effectiveness:."),
    ]),

    ("Employee Privacy and Monitoring", [
        ("A.8.16-26", "Monitoring Activities",
         "Monitoring activities shall comply with Swiss employment law:."),
        ("A.8.16-27", "The Following Safeguards",
         "The following safeguards shall be applied:."),
        ("A.8.16-28", "Serve Legitimate Security Purposes",
         "Monitoring shall serve legitimate security purposes (threat detection, incident investigation, compliance verification) — not behavioural surveillance or performance management."),
        ("A.8.16-29", "Be Informed In Advance That Monitoring",
         "Employees shall be informed in advance that monitoring takes place, what is monitored, and why, through the acceptable use policy and employment documentation."),
        ("A.8.16-30", "Only The Minimum Necessary Data",
         "Only the minimum necessary data shall be collected and retained (data minimisation)."),
        ("A.8.16-31", "Monitoring Data",
         "Monitoring data shall not be used for HR performance evaluation, disciplinary action for non-security matters, or general behavioural profiling."),
        ("A.8.16-32", "Personalised Analysis (Identifying",
         "Personalised analysis (identifying individual users) shall only occur when: (a) an alert indicates a potential security incident or policy violation, and (b) the investigation is documented with justification."),
        ("A.8.16-33", "Mdr Providers, Forensic Investigators),",
         "Where monitoring data is shared with external parties (e.g., MDR providers, forensic investigators), personal identifiers shall be minimised or anonymised where feasible."),
        ("A.8.16-34", "A Data Protection Impact Assessment",
         "A Data Protection Impact Assessment (DPIA) under nFADP Art. 22 shall be conducted before deployment of monitoring that meets any of the following criteria:."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.16
# =============================================================================
