#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.6 — Capacity Management Compliance Checklist

Control A.8.6: Capacity Management
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Resource Monitoring (4 reqs)
4. Threshold Framework & Alerting (5 reqs)
5. Capacity Forecasting (4 reqs)
6. Auto-Scaling Policies (7 reqs)
7. Capacity and Cost Optimisation (3 reqs)
8. Capacity & Service Level (2 reqs)
9. Capacity Reporting (2 reqs)
10. Storage Capacity Management (9 reqs)
11. Licence Capacity Management (2 reqs)
12. Capacity Incident Response (3 reqs)
13. Denial-of-Service Resilience (2 reqs)
14. Capacity Planning Committee (3 reqs)

Total: 46 requirements across 12 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.6"
CONTROL_ID = "A.8.6"
CONTROL_NAME = "Capacity Management"
SOURCE_POLICY = "ISMS-OP-POL-A.8.6"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.6
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Resource Monitoring", [
        ("A.8.6-01", "Production Systems And Services",
         "All production systems and services shall have capacity monitoring enabled. Monitoring shall cover, at minimum, the resource categories listed in the Scope section above."),
        ("A.8.6-02", "Be Implemented Using [Monitoring",
         "Monitoring shall be implemented using [Monitoring Platform] (e.g., Prometheus, Zabbix, Datadog, Azure Monitor, CloudWatch, or equivalent). The platform shall be documented in the asset inventory with its hosting model, data residency, and administrative access controls."),
        ("A.8.6-03", "The Following Metrics",
         "The following metrics shall be collected for each applicable resource type:."),
        ("A.8.6-04", "Metric Data",
         "Metric data shall be protected from unauthorised modification or deletion. Where metrics feed security monitoring (A.8.16), log integrity requirements from the Logging Policy (A.8.15) also apply."),
    ]),

    ("Threshold Framework & Alerting", [
        ("A.8.6-05", "Monitored Resources",
         "All monitored resources shall have defined capacity thresholds at three levels:."),
        ("A.8.6-06", "Exact Threshold Values",
         "Exact threshold values shall be defined per resource type and system classification, documented in the monitoring platform, and reviewed quarterly. Thresholds shall be tuned based on false positive rates, workload patterns, and near-miss incidents."),
        ("A.8.6-07", "Storage-Specific Thresholds*",
         "Storage-specific thresholds* shall also account for growth rate: if storage is projected to reach 95% within 30 days at the current consumption rate, a warning alert shall be generated regardless of current percentage."),
        ("A.8.6-08", "Capacity Threshold Alerts",
         "Capacity threshold alerts shall be configured with:."),
        ("A.8.6-09", "Integration: Critical And Maximum Alerts",
         "Integration: Critical and maximum alerts shall create incidents automatically in [ITSM Tool] (e.g., ServiceNow, Jira Service Management, or equivalent)."),
    ]),

    ("Capacity Forecasting", [
        ("A.8.6-10", "Develop And Maintain Capacity Forecasts",
         "The organisation shall develop and maintain capacity forecasts at three horizons:."),
        ("A.8.6-11", "Be Based On",
         "Forecasts shall be based on:."),
        ("A.8.6-12", "Conservative Estimates",
         "Where historical data is insufficient (new systems or services), conservative estimates shall be used with more frequent review during the first 6 months of operation."),
        ("A.8.6-13", "Target Accuracy: Forecasts",
         "Target accuracy: Forecasts shall be within +/-15% of actual utilisation (measured quarterly)."),
    ]),

    ("Auto-Scaling Policies", [
        ("A.8.6-14", "Auto-Scaling",
         "Where the organisation operates cloud infrastructure, auto-scaling shall be configured for workloads with variable demand patterns."),
        ("A.8.6-15", "Auto-Scaling Configurations",
         "Auto-scaling configurations shall be documented and version-controlled."),
        ("A.8.6-16", "Changes To Auto-Scaling Policies For",
         "Changes to auto-scaling policies for production workloads shall follow the change management process (A.8.32)."),
        ("A.8.6-17", "Maximum Instance Limits",
         "Maximum instance limits shall be reviewed quarterly and aligned with approved budgets."),
        ("A.8.6-18", "Auto-Scaling Events",
         "Auto-scaling events shall be logged and reviewed monthly for optimisation opportunities."),
        ("A.8.6-19", "Cost Guardrails: Maximum Monthly Spend",
         "Cost guardrails: Maximum monthly spend limits shall be configured at the cloud account or subscription level. Auto-scaling that would breach the spend limit shall trigger an alert to the Infrastructure Manager and CFO delegate."),
        ("A.8.6-20", "Fixed-Capacity Services), Manual",
         "Where auto-scaling is not available or not appropriate (on-premises infrastructure, fixed-capacity services), manual capacity expansion procedures shall be documented with defined procurement and deployment lead times."),
    ]),

    ("Capacity and Cost Optimisation", [
        ("A.8.6-21", "Capacity Management",
         "Capacity management shall balance availability, performance, and cost. Over-provisioning wastes budget; under-provisioning creates risk. The organisation shall actively optimise resource allocation based on measured utilisation data."),
        ("A.8.6-22", "The Infrastructure Manager",
         "The Infrastructure Manager shall conduct a quarterly cost review that includes:."),
        ("A.8.6-23", "Cost Optimisation Findings",
         "Cost optimisation findings shall be included in the quarterly capacity review report presented to the CIO, CISO, and CFO delegate."),
    ]),

    ("Capacity & Service Level", [
        ("A.8.6-24", "Capacity Thresholds",
         "Capacity thresholds shall be aligned with service level objectives (SLOs) to ensure that capacity constraints do not degrade service quality below agreed levels. The connection between resource utilisation and service performance shall be documented for each critical service."),
        ("A.8.6-25", "Capacity Thresholds",
         "Where measured resource utilisation approaches levels that would degrade SLO performance, capacity thresholds shall be adjusted downward to trigger earlier intervention. SLO alignment shall be reviewed quarterly as part of the capacity review process."),
    ]),

    ("Capacity Reporting", [
        ("A.8.6-26", "Monthly And Quarterly Reports",
         "Monthly and quarterly reports shall include:."),
        ("A.8.6-27", "Be Generated From [Monitoring Platform]",
         "Reports shall be generated from [Monitoring Platform] data. The annual capacity plan shall be approved by the CIO and included in the management review per ISO 27001 Clause 9.3."),
    ]),

    ("Storage Capacity Management", [
        ("A.8.6-28", "Log Storage Capacity",
         "Log storage capacity shall be planned in coordination with the Logging Policy (A.8.15) to ensure retention requirements can be met without storage exhaustion."),
        ("A.8.6-29", "Log Storage",
         "Log storage shall have a dedicated warning threshold at 70% and critical threshold at 85%."),
        ("A.8.6-30", "Automated Log Rotation Or Archival",
         "If log storage reaches critical threshold, automated log rotation or archival shall be triggered before data loss occurs."),
        ("A.8.6-31", "Log Storage Growth Rate",
         "Log storage growth rate shall be tracked and projected monthly."),
        ("A.8.6-32", "Database Storage Growth",
         "Database storage growth shall be monitored and forecast separately from file storage."),
        ("A.8.6-33", "Database Maintenance Activities",
         "Database maintenance activities (vacuuming, index rebuilds, archival) shall be factored into capacity planning."),
        ("A.8.6-34", "Database Storage Thresholds",
         "Database storage thresholds shall account for operational overhead (temporary tables, transaction logs, replication lag)."),
        ("A.8.6-35", "Backup Storage Capacity",
         "Backup storage capacity shall be planned to accommodate full backup sets for the required retention period per the backup policy (A.5.30–8.13–14)."),
        ("A.8.6-36", "Growth In Backup Storage",
         "Growth in backup storage shall be forecast based on production data growth and retention policy changes."),
    ]),

    ("Licence Capacity Management", [
        ("A.8.6-37", "Software Licence Capacity",
         "Software licence capacity shall be monitored to prevent compliance violations and service interruptions caused by licence exhaustion."),
        ("A.8.6-38", "Licence Renewals",
         "Licence renewals shall be tracked with a minimum 90-day lead time before expiry. Licence capacity requirements shall be included in the medium-term (6–12 month) capacity forecast and aligned with budget planning cycles."),
    ]),

    ("Capacity Incident Response", [
        ("A.8.6-39", "The Organisation'S Incident Management",
         "When capacity exhaustion causes or threatens to cause service impact, the organisation's incident management process (A.5.24–28) shall be invoked."),
        ("A.8.6-40", "Capacity-Related Incidents Classified",
         "All capacity-related incidents classified Priority 1 or Priority 2 shall undergo post-incident review within 5 business days. The review shall determine:."),
        ("A.8.6-41", "Be Tracked In The Capacity Improvement",
         "Findings shall be tracked in the capacity improvement register until remediation is complete."),
    ]),

    ("Denial-of-Service Resilience", [
        ("A.8.6-42", "Capacity Planning",
         "Capacity planning shall incorporate resilience against denial-of-service (DoS/DDoS) conditions. Capacity should not be planned solely for average or expected peak loads — headroom shall be maintained to absorb unexpected demand spikes, including those caused by malicious activity."),
        ("A.8.6-43", "Additional Mitigation Measures (Cdn,",
         "Where external-facing services are exposed to DDoS risk, additional mitigation measures (CDN, DDoS protection services, rate limiting) shall be implemented in coordination with the Network Security Policy (A.8.20–22)."),
    ]),

    ("Capacity Planning Committee", [
        ("A.8.6-44", "The Capacity Planning Committee",
         "The Capacity Planning Committee shall meet quarterly. The agenda shall include:."),
        ("A.8.6-45", "Meeting Minutes",
         "Meeting minutes shall be retained as evidence of governance (Evidence #10)."),
        ("A.8.6-46", "The Quarterly Capacity Review Meeting",
         "Where the organisation is too small to justify a formal committee, the quarterly capacity review meeting between the Infrastructure Manager and CIO shall fulfil this governance function."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.6
# =============================================================================
