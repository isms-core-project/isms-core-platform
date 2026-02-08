#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
ISMS-OP-CHK-A.8.12 — Data Leakage Prevention Compliance Checklist

Control A.8.12: Data Leakage Prevention
Product: ISMS CORE Operational (SME Compliance Checklist)

Workbook Structure:
1. Executive Summary
2. Dashboard
3. Service Commitments & Customer (2 reqs)
4. Data Classification Integration (3 reqs)
5. Channel Protection (13 reqs)
6. Third-Party DLP Service (4 reqs)
7. Monitoring and Detection (3 reqs)
8. DLP Incident Response (4 reqs)
9. Employee Monitoring Legal Reqs (10 reqs)
10. User Awareness & Acceptable Use (2 reqs)
11. DLP Performance and Tuning (2 reqs)
12. DLP System Avail & Perf Impact (8 reqs)
13. DLP Effectiveness Testing (1 reqs)
14. Mgmt Reporting and Oversight (3 reqs)
15. Exception Management (2 reqs)

Total: 57 requirements across 13 domains
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
DOCUMENT_ID = "ISMS-OP-CHK-A.8.12"
CONTROL_ID = "A.8.12"
CONTROL_NAME = "Data Leakage Prevention"
SOURCE_POLICY = "ISMS-OP-POL-A.8.12"

# =============================================================================
# REQUIREMENTS DATA — extracted from ISMS-OP-POL-A.8.12
# =============================================================================

REQUIREMENTS = OrderedDict([
    ("Service Commitments & Customer", [
        ("A.8.12-01", "Customer Data Processed By The",
         "Customer data processed by the organisation shall receive DLP protection commensurate with contractual commitments:."),
        ("A.8.12-02", "Customer-Specific Requirements*: Where",
         "Customer-specific requirements*: Where customers have negotiated custom notification timelines, incident severity thresholds, or reporting requirements, these shall be documented in the customer contract register and integrated into DLP alert routing and incident response workflows."),
    ]),

    ("Data Classification Integration", [
        ("A.8.12-03", "Dlp Controls",
         "DLP controls shall be applied based on the organisation's data classification scheme. Classification determines the enforcement mode, channel coverage, and response priority for each data category."),
        ("A.8.12-04", "Implement Multiple Identification",
         "The organisation shall implement multiple identification methods to detect sensitive information in transit:."),
        ("A.8.12-05", "Maintain An Inventory Of Sensitive Data",
         "The organisation shall maintain an inventory of sensitive data requiring DLP protection, reconciled quarterly against the asset inventory (A.5.9). Specific detection patterns, regex rules, and classification labels shall be documented and maintained by the Security Team."),
    ]),

    ("Channel Protection", [
        ("A.8.12-06", "Implement Dlp Controls Across All Data",
         "The organisation shall implement DLP controls across all data egress channels to prevent unauthorised information disclosure. Channel coverage shall be verified through technical testing at least quarterly."),
        ("A.8.12-07", "Outbound Email (Smtp And Webmail)",
         "All outbound email (SMTP and webmail) shall be subject to DLP content inspection:."),
        ("A.8.12-08", "Web-Based Data Egress Channels",
         "Web-based data egress channels shall be monitored and controlled:."),
        ("A.8.12-09", "Web Uploads: Monitor And Control File",
         "Web uploads: Monitor and control file uploads to cloud storage services (e.g., Dropbox, Google Drive, personal OneDrive accounts). Approved corporate cloud storage [Cloud Storage Platform] shall be distinguished from personal or unapproved services."),
        ("A.8.12-10", "Tls Inspection: Where Legally",
         "TLS inspection: Where legally permissible and technically feasible, inspect encrypted web traffic at the internet gateway to detect sensitive content in HTTPS uploads. TLS inspection shall comply with privacy requirements and be documented in the organisation's privacy notice."),
        ("A.8.12-11", "Endpoint Dlp Controls",
         "Endpoint DLP controls shall be deployed on all managed devices:."),
        ("A.8.12-12", "Removable Media: Monitor And Control",
         "Removable media: Monitor and control file transfers to USB drives, external hard drives, SD cards, and other removable storage. Block unauthorised removable media usage for Restricted and Confidential data. Approved removable media (e.g., encrypted corporate USB devices) shall be documented."),
        ("A.8.12-13", "Printing: Monitor Print Jobs For",
         "Printing: Monitor print jobs for Restricted data. Print-to-PDF and virtual printer activity shall be included in monitoring scope."),
        ("A.8.12-14", "Screenshots And Clipboard (Risk-Based):",
         "Screenshots and clipboard (risk-based): Where the risk assessment justifies it, monitor screen capture tools and clipboard operations for Restricted data. This control shall be applied only to specific high-risk roles or data sets, not organisation-wide."),
        ("A.8.12-15", "Offline Enforcement: Endpoint Dlp Agents",
         "Offline enforcement: Endpoint DLP agents shall enforce policies when the device is disconnected from the corporate network."),
        ("A.8.12-16", "Network-Level Dlp Controls",
         "Network-level DLP controls shall monitor data flows at egress points:."),
        ("A.8.12-17", "Corporate Data On Mobile Devices",
         "Corporate data on mobile devices shall be protected:."),
        ("A.8.12-18", "Verify Dlp Channel Coverage Through",
         "The organisation shall verify DLP channel coverage through technical testing at least quarterly. Coverage gaps shall be documented with:."),
    ]),

    ("Third-Party DLP Service", [
        ("A.8.12-19", "Dlp Service Providers",
         "DLP service providers shall be evaluated against:."),
        ("A.8.12-20", "Cloud Dlp Vendor Contracts",
         "Cloud DLP vendor contracts shall include:."),
        ("A.8.12-21", "Cloud Dlp Vendors",
         "Cloud DLP vendors shall receive an annual review covering:."),
        ("A.8.12-22", "Immediate Notification: Vendor",
         "Immediate notification: Vendor shall notify organisation within 24 hours (per contract)."),
    ]),

    ("Monitoring and Detection", [
        ("A.8.12-23", "Implement Continuous Monitoring To",
         "The organisation shall implement continuous monitoring to detect data leakage attempts and policy violations."),
        ("A.8.12-24", "Dlp Events",
         "All DLP events shall be logged with the following information:."),
        ("A.8.12-25", "Behavioural Analytics* (Recommended):",
         "Behavioural Analytics* (recommended): Where the organisation deploys user and entity behaviour analytics (UEBA), DLP data shall be correlated with baseline user activity to detect anomalous transfer patterns (e.g., unusual volume, unusual destination, unusual time). Behavioural analytics shall comply with the employee monitoring legal requirements defined in this policy."),
    ]),

    ("DLP Incident Response", [
        ("A.8.12-26", "Dlp Security Incidents",
         "DLP security incidents shall follow the organisation's incident management process (A.5.24-28) with the following DLP-specific requirements."),
        ("A.8.12-27", "The Organisation",
         "Where DLP incidents constitute personal data breaches, the organisation shall follow notification requirements:."),
        ("A.8.12-28", "The Data Protection Officer (Dpo) Or",
         "The Data Protection Officer (DPO) or designated privacy lead shall be consulted for all DLP incidents involving personal data to determine breach notification obligations."),
        ("A.8.12-29", "Dlp-To-Incident-Management Integration*:",
         "DLP-to-Incident-Management Integration*: Critical and High severity DLP events shall automatically create incident tickets in [ITSM Platform] (e.g., ServiceNow, Jira Service Management, or equivalent). Tickets not acknowledged within the response SLA shall auto-escalate per incident management procedures."),
    ]),

    ("Employee Monitoring Legal Reqs", [
        ("A.8.12-30", "Dlp Monitoring Constitutes A Form Of",
         "DLP monitoring constitutes a form of employee monitoring under Swiss law. The organisation shall comply with the following legal requirements before deploying and operating DLP controls."),
        ("A.8.12-31", "Art. 26 Argv 3 (Ordinance 3",
         "Art. 26 ArGV 3 (Ordinance 3 to the Employment Act)*: Monitoring and surveillance systems shall not be used if their sole or primary purpose is to monitor employee behaviour. DLP systems are permissible because their primary purpose is protecting organisational data from unauthorised disclosure — not monitoring individual employee conduct. However, DLP implementation must demonstrably serve a data protection objective, and any incidental monitoring of employee behaviour must be proportionate."),
        ("A.8.12-32", "Art. 328B Co (Swiss Code Of",
         "Art. 328b CO (Swiss Code of Obligations)*: The employer may process data concerning employees only insofar as it relates to the employee's suitability for the employment relationship or is necessary for the performance of the employment contract. DLP monitoring data shall be processed only for information security purposes. DLP data shall not be used for:."),
        ("A.8.12-33", "Proportionality: Monitoring Scope",
         "Proportionality: Monitoring scope shall be limited to what is necessary for data protection. The organisation shall not monitor more broadly than required."),
        ("A.8.12-34", "Purpose Limitation: Data Collected",
         "Purpose limitation: Data collected through DLP shall be used only for security purposes, not repurposed for other objectives."),
        ("A.8.12-35", "Transparency: Employees",
         "Transparency: Employees shall be informed about DLP monitoring before it is activated."),
        ("A.8.12-36", "Conduct A Proportionality Assessment",
         "The organisation shall conduct a proportionality assessment before deploying DLP controls. The assessment shall verify that:."),
        ("A.8.12-37", "Inform All Employees About Dlp",
         "The organisation shall inform all employees about DLP monitoring through:."),
        ("A.8.12-38", "Works Council Consultation (Where",
         "Works council consultation (where applicable): In jurisdictions requiring co-determination, the works council shall be consulted before deploying DLP monitoring."),
        ("A.8.12-39", "Critical*: Failure To Provide",
         "Critical*: Failure to provide transparency may render DLP monitoring unlawful. DLP monitoring shall not be activated until employee notification has been completed and documented. The organisation shall retain evidence of employee notification (signed acknowledgments, training completion records, privacy notice distribution records)."),
    ]),

    ("User Awareness & Acceptable Use", [
        ("A.8.12-40", "Be Informed Of Dlp Controls And",
         "All personnel shall be informed of DLP controls and their responsibilities."),
        ("A.8.12-41", "Violations Of Dlp Policy",
         "Violations of DLP policy shall be subject to disciplinary action in accordance with HR policy. Deliberate or repeated attempts to circumvent DLP controls may result in termination of employment."),
    ]),

    ("DLP Performance and Tuning", [
        ("A.8.12-42", "Track Dlp Effectiveness Through Key",
         "The organisation shall track DLP effectiveness through key performance indicators and continuously tune DLP rules to reduce false positives while maintaining detection coverage."),
        ("A.8.12-43", "Below-Target Response*: If Metrics Fall",
         "Below-Target Response*: If metrics fall below the acceptable range for two consecutive measurement periods, the CISO shall conduct a root cause analysis within 30 days, implement a corrective action plan, and report remediation status to Executive Management."),
    ]),

    ("DLP System Avail & Perf Impact", [
        ("A.8.12-44", "Dlp Systems",
         "DLP systems shall be configured with explicit fail-safe behaviour to prevent service disruption:."),
        ("A.8.12-45", "Dlp System Performance",
         "DLP system performance shall be monitored to prevent service degradation:."),
        ("A.8.12-46", "Dlp Systems",
         "DLP systems shall be sized to handle peak traffic with 30% headroom."),
        ("A.8.12-47", "Annual Capacity Review",
         "Annual capacity review shall project growth and identify scaling needs."),
        ("A.8.12-48", "Customer Notification*: If Dlp",
         "Customer notification*: If DLP containment actions impact customer-facing services, customers shall be notified per the incident communication procedures (typically within 1 hour for customer-impacting incidents)."),
        ("A.8.12-49", "Dlp Controls",
         "DLP controls shall support the organisation's business continuity and disaster recovery objectives:."),
        ("A.8.12-50", "Dlp Systems",
         "DLP systems shall be included in disaster recovery planning with defined recovery priorities:."),
        ("A.8.12-51", "Dlp Systems",
         "DLP systems shall be included in annual disaster recovery testing:."),
    ]),

    ("DLP Effectiveness Testing", [
        ("A.8.12-52", "Conduct Structured Testing To Validate",
         "The organisation shall conduct structured testing to validate that DLP controls detect and prevent unauthorised data disclosure as designed."),
    ]),

    ("Mgmt Reporting and Oversight", [
        ("A.8.12-53", "Dlp Programme Effectiveness And",
         "DLP programme effectiveness and compliance shall be reported to executive management to demonstrate governance and oversight."),
        ("A.8.12-54", "The Ciso",
         "The CISO shall provide a quarterly DLP programme summary to executive management covering:."),
        ("A.8.12-55", "As Part Of The Iso 27001",
         "As part of the ISO 27001 Management Review (Clause 9.3), the CISO shall present an annual DLP programme review covering:."),
    ]),

    ("Exception Management", [
        ("A.8.12-56", "Exceptions To Dlp Policy Requirements",
         "Exceptions to DLP policy requirements shall be requested in writing and shall include:."),
        ("A.8.12-57", "Active Exceptions",
         "All active exceptions shall be recorded in the DLP Exception Register (format: DLP-EX-YYYY-NNN), reviewed at least quarterly, and revoked when the business justification no longer applies or the risk profile changes."),
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
# CHANGES: Auto-generated from ISMS-OP-POL-A.8.12
# =============================================================================
