#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
#
# This file is part of ISMS Core.
#
# ISMS Core is dual-licensed:
#   1. AGPL 3.0 (Open Source) - See LICENSE-AGPL.txt
#   2. Commercial License - Contact vendor for proprietary use
#
# You may use this file under either license, at your option.
# =============================================================================
"""
================================================================================
ISMS-IMP-A.8.23.4 - Monitoring & Response Assessment Excel Generator
================================================================================

ISO/IEC 27001:2022 Control A.8.23: Web Filtering
Assessment Domain 4 of 4: Monitoring, Logging, Alerting & Incident Response

--------------------------------------------------------------------------------
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR YOUR ORGANIZATION
--------------------------------------------------------------------------------

This script is a TEMPLATE/SAMPLE implementation and MUST be adapted to match
your organization's specific monitoring requirements, logging infrastructure,
alerting mechanisms, and incident response procedures.

Key customization areas:
1. Log retention requirements (match your regulatory and policy requirements)
2. Alert thresholds and escalation criteria (adapt to your risk tolerance)
3. SIEM/monitoring tool integration (specific to your security stack)
4. Incident response workflow (match your IR procedures)
5. Reporting requirements (adapt to stakeholder needs)

DO NOT use this script without reviewing and adapting all sections marked
with "# CUSTOMIZE:" comments throughout the code.

Reference Pattern: Based on ISMS-A.8.23 Web Filtering Assessment Framework

--------------------------------------------------------------------------------
DESCRIPTION
--------------------------------------------------------------------------------

This script generates a comprehensive Excel assessment workbook for evaluating
web filtering monitoring, logging, alerting, and incident response capabilities
against ISO 27001:2022 Control A.8.23 requirements.

**Purpose:**
Validates that web filtering controls are supported by adequate monitoring,
logging, alerting, and incident response capabilities to detect, investigate,
and respond to security events and policy violations.

**Assessment Scope:**
- Log generation, collection, and retention adequacy
- Real-time monitoring and alerting configuration
- Event correlation and threat detection capabilities
- Incident detection, triage, and response procedures
- Reporting and metrics for compliance oversight
- Integration with Security Operations Center (SOC)
- SIEM/monitoring tool integration effectiveness
- Evidence collection for monitoring adequacy audit

**Generated Workbook Structure:**
1. Instructions & Legend - Assessment methodology and evaluation criteria
2. Log Management - Generation, collection, retention, and access controls
3. Monitoring Configuration - Real-time monitoring and coverage assessment
4. Alerting Framework - Alert rules, thresholds, and escalation procedures
5. Event Correlation - Multi-source correlation and threat detection
6. Incident Response - Detection, triage, investigation, and remediation
7. SIEM Integration - Security information and event management integration
8. Reporting & Metrics - Compliance reporting and operational metrics
9. SOC Integration - Security operations center workflow integration
10. Gap Analysis - Monitoring and response capability gaps
11. Evidence Register - Audit evidence and configuration documentation
12. Approval & Sign-Off - Security operations and SOC team approval

**Key Features:**
- Log retention compliance verification (regulatory + policy requirements)
- Alert rule effectiveness assessment and tuning recommendations
- Event correlation capability evaluation
- Incident response workflow validation and effectiveness measurement
- SIEM integration assessment and coverage verification
- Reporting adequacy for multiple stakeholder audiences
- Automated gap identification for monitoring deficiencies
- Evidence linking for audit readiness
- Multi-stakeholder approval workflow (SOC, Security Ops, Compliance)

**Integration:**
This assessment completes the four-domain A.8.23 framework, feeding into the
A.8.23.5 Compliance Dashboard alongside Infrastructure (A.8.23.1), Network
Coverage (A.8.23.2), and Policy Configuration (A.8.23.3) assessments for
consolidated compliance oversight and executive reporting.

--------------------------------------------------------------------------------
REQUIREMENTS
--------------------------------------------------------------------------------

System Requirements:
    - Python 3.8 or higher
    - openpyxl library for Excel generation

Installation:
    Ubuntu/Debian:
        sudo apt install python3-openpyxl
    
    Or via pip:
        pip3 install openpyxl

Dependencies:
    - openpyxl (Python Excel library)
    - datetime (standard library)

--------------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------------

Basic Usage:
    python3 generate_a823_4_monitoring_response.py

Advanced Usage:
    # Generate with custom output directory
    python3 generate_a823_4_monitoring_response.py --output /path/to/dir
    
    # Generate with specific date suffix
    python3 generate_a823_4_monitoring_response.py --date 20250115

Output:
    File: ISMS_A_8_23_4_Monitoring_Response_Assessment_YYYYMMDD.xlsx
    Location: Current directory (or specified output path)

Post-Generation Steps:
    1. Document log generation, collection, and retention configurations
    2. Validate monitoring coverage across all filtering infrastructure
    3. Review and tune alerting rules for effectiveness
    4. Assess event correlation and threat detection capabilities
    5. Validate incident response procedures and integration
    6. Verify SIEM integration and data flow
    7. Evaluate reporting adequacy for compliance and operations
    8. Assess SOC integration and workflow effectiveness
    9. Conduct gap analysis and define remediation actions
    10. Collect and link monitoring configuration evidence
    11. Obtain SOC, security operations, and compliance approvals
    12. Feed results into A.8.23.5 Compliance Dashboard

--------------------------------------------------------------------------------
METADATA
--------------------------------------------------------------------------------

Control Reference:    ISO/IEC 27001:2022 Annex A Control A.8.23
Assessment Domain:    4 of 4 (Monitoring, Logging, Alerting & Response)
Framework Version:    1.0
Script Version:       1.0
Author:               [Organization] ISMS Implementation Team
Date:                 [Date to be set]
Last Modified:        [Date to be set]
Python Version:       3.8+
License:              [Organisation License/Terms]

Related Documents:
    - ISMS-POL-A.8.23: Web Filtering Policy (Governance)
    - ISMS-IMP-A.8.23.4: Monitoring & Response Implementation Guide
    - ISMS-POL-A.8.15: Logging Policy
    - ISMS-POL-A.5.24: Information Security Incident Management
    - ISMS-IMP-A.8.23.1: Filtering Infrastructure Assessment (Domain 1)
    - ISMS-IMP-A.8.23.2: Network Coverage Assessment (Domain 2)
    - ISMS-IMP-A.8.23.3: Policy Configuration Assessment (Domain 3)
    - ISMS-IMP-A.8.23.5: Compliance Dashboard (Consolidation)

Related Controls:
    - A.8.15: Logging (Log management requirements)
    - A.8.16: Monitoring Activities (Security monitoring)
    - A.5.24: Information Security Event Management Planning
    - A.5.25: Assessment and Decision on Information Security Events
    - A.5.26: Response to Information Security Incidents
    - A.5.27: Learning from Information Security Incidents

--------------------------------------------------------------------------------
CHANGE HISTORY
--------------------------------------------------------------------------------

Version 1.0 - [Date to be set]
    - Initial release
    - Implements full monitoring and response assessment framework
    - Supports logging, alerting, incident response, and SIEM integration
    - Integrated with A.8.23.5 Compliance Dashboard

[Future changes to be documented here]

--------------------------------------------------------------------------------
IMPORTANT NOTES
--------------------------------------------------------------------------------

**Audit Considerations:**
Monitoring and incident response capabilities are critical audit focus areas:
- Log retention MUST meet regulatory and policy requirements (verify actual)
- Alert rules must be documented, tuned, and evidence false-positive reduction
- Incident response procedures must be documented AND exercised (not just paper)
- SIEM integration must be technically validated (not assumed)
- Reporting must demonstrate actual usage and effectiveness

Auditors will request:
- Sample log extracts demonstrating retention compliance
- Alert rule documentation and tuning history
- Incident response runbooks and exercise records
- SIEM correlation rule configurations
- Compliance reports with actual data (not templates)

**Data Protection:**
Assessment workbooks contain sensitive security operations information including:
- Log retention configurations (may reveal monitoring gaps)
- Alert thresholds (potential bypass information)
- Incident response procedures (operational security)
- SIEM integration details (security architecture)

Handle in accordance with your organization's data classification policies
(typically CONFIDENTIAL or RESTRICTED).

**Maintenance:**
Review and update monitoring assessments:
- Monthly: Alert effectiveness review and tuning
- Quarterly: Incident response procedure validation and exercise
- After significant incidents: Lessons learned integration
- Semi-annually: SIEM integration and correlation effectiveness
- Annually: Complete monitoring framework re-assessment

**Quality Assurance:**
Monitoring assessments should be validated by:
- Security Operations Center (SOC) team (operational accuracy)
- Incident Response team (procedure validation)
- SIEM/monitoring platform administrators (technical verification)
- Compliance team (retention and reporting requirement validation)

**Common Pitfalls:**
- Log retention claims without verification (check actual, not configured)
- Alert fatigue not addressed (high false-positive rates reduce effectiveness)
- Paper-only incident response (no exercises, no evidence of capability)
- SIEM integration assumed but not validated (check data flow)
- Compliance reports generated but not reviewed (checkbox reporting)
- Missing alert tuning documentation (no evidence of optimization)
- No metrics on detection effectiveness (cannot prove value)

**Critical Success Factors:**
- VERIFY actual log retention, don't just document configured retention
- TUNE alerts regularly with documented false-positive reduction metrics
- EXERCISE incident response procedures with documented results
- VALIDATE SIEM integration with actual event flow testing
- DEMONSTRATE reporting effectiveness with stakeholder feedback
- QUANTIFY detection capabilities with metrics and trend analysis

**Monitoring ≠ Compliance Theater:**
This assessment measures ACTUAL monitoring effectiveness, not just the presence
of monitoring tools. Focus on:
- Detection rate (how many incidents are identified)
- Time to detect (how quickly incidents are identified)
- Time to respond (how quickly incidents are contained)
- False positive rate (efficiency of alert rules)
- Coverage verification (blind spots identification)

"Evidence > Theater" - Richard Feynman would approve.

================================================================================
"""

# =============================================================================
# Standard Library Imports
# =============================================================================
import logging
import sys

# =============================================================================
# Logging Configuration
# =============================================================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


from datetime import datetime
# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.8.23.4"
WORKBOOK_NAME = "Monitoring & Response Assessment"
CONTROL_ID = "A.8.23"
CONTROL_NAME = "Web Filtering"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

# Timestamps
GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")      # For display (Swiss format)
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")   # For filenames (sortable)

# Output filename
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

# =============================================================================
# SECTION 1: IMPORTS AND CONFIGURATION
# =============================================================================

import os

from openpyxl import Workbook
from openpyxl.styles import (
    Font, Fill, PatternFill, Alignment, Border, Side, Protection
)
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

# Unicode Constants (for cross-platform compatibility)
CHECK_MARK = "\u2705"      # ✅
CROSS_MARK = "\u274C"      # ❌
WARNING = "\u26A0"         # ⚠️
CLIPBOARD = "\u1F4CB"      # 📋
TRIANGLE = "\u25B8"        # ▸
BULLET = "\u2022"          # •

from openpyxl.formatting.rule import FormulaRule
from openpyxl.comments import Comment

# -----------------------------------------------------------------------------
# Color Palette (Consistent with A.8.23 Framework)
# -----------------------------------------------------------------------------
COLORS = {
    "header_dark": "003366",      # Dark blue - main headers
    "header_medium": "4472C4",    # Medium blue - subheaders
    "header_light": "8FAADC",     # Light blue - section headers
    "input_yellow": "FFFFCC",     # Yellow - user input cells
    "status_green": "C6EFCE",     # Green - Implemented/Compliant
    "status_yellow": "FFEB9C",    # Yellow/Amber - Partial
    "status_red": "FFC7CE",       # Red - Not Implemented
    "status_blue": "BDD7EE",      # Blue - Planned
    "status_gray": "D9D9D9",      # Gray - N/A
    "white": "FFFFFF",
    "black": "000000",
    "light_gray": "F2F2F2",
}

# -----------------------------------------------------------------------------
# Style Definitions
# -----------------------------------------------------------------------------
def create_styles():
    """Create reusable style dictionaries."""
    return {
        "header": {
            "font": Font(bold=True, color=COLORS["white"], size=14),
            "fill": PatternFill(start_color=COLORS["header_dark"],
                               end_color=COLORS["header_dark"],
                               fill_type="solid"),
            "alignment": Alignment(horizontal="center", vertical="center",
                                  wrap_text=True),
        },
        "subheader": {
            "font": Font(bold=True, color=COLORS["white"], size=11),
            "fill": PatternFill(start_color=COLORS["header_medium"],
                               end_color=COLORS["header_medium"],
                               fill_type="solid"),
            "alignment": Alignment(horizontal="center", vertical="center",
                                  wrap_text=True),
        },
        "section": {
            "font": Font(bold=True, color=COLORS["black"], size=11),
            "fill": PatternFill(start_color=COLORS["header_light"],
                               end_color=COLORS["header_light"],
                               fill_type="solid"),
            "alignment": Alignment(horizontal="left", vertical="center"),
        },
        "label": {
            "font": Font(bold=True, size=10),
            "alignment": Alignment(horizontal="left", vertical="center"),
        },
        "input": {
            "fill": PatternFill(start_color=COLORS["input_yellow"],
                               end_color=COLORS["input_yellow"],
                               fill_type="solid"),
            "alignment": Alignment(horizontal="left", vertical="center",
                                  wrap_text=True),
        },
        "normal": {
            "font": Font(size=10),
            "alignment": Alignment(horizontal="left", vertical="center",
                                  wrap_text=True),
        },
    }

def get_border(style="thin"):
    """Create border object."""
    side = Side(style=style, color=COLORS["black"])
    return Border(left=side, right=side, top=side, bottom=side)

# -----------------------------------------------------------------------------
# Dropdown Validation Lists
# -----------------------------------------------------------------------------
DROPDOWNS = {
    "status": "Implemented,Partial,Planned,Not_Implemented,N/A",
    "yes_no": "Yes,No",
    "yes_no_partial": "Yes,No,Partial",
    "priority": "Critical,High,Medium,Low",
    "severity": "Critical,High,Medium,Low,Informational",
    "log_type": "Blocked_Requests,Allowed_Requests,Bypass_Attempts,Policy_Violations,Authentication,Configuration_Changes,System_Events",
    "collection_method": "Syslog,API,Agent,File_Transfer,Direct_Query,SNMP,Other",
    "destination": "SIEM,Log_Server,Cloud_SIEM,Local_Storage,Archive,Multiple",
    "format": "CEF,JSON,Syslog,CSV,Proprietary,XML,Other",
    "alert_category": "Threat_Detection,Policy_Violation,System_Health,Threshold_Breach,Anomaly,Compliance",
    "notification_method": "Email,SMS,SIEM_Alert,Ticket,Dashboard,Webhook,PagerDuty,Teams,Slack",
    "dashboard_platform": "SIEM,Filtering_Console,Custom,PowerBI,Grafana,Splunk,Cloud_Native,Excel,Other",
    "audience": "SOC,Management,IT_Ops,Compliance,CISO,All,Security_Team",
    "update_frequency": "Real-Time,Hourly,Daily,Weekly,Monthly",
    "kpi_category": "Volume,Security,Performance,Compliance,Operational",
    "kpi_status": "Met,Not_Met,At_Risk,New",
    "trend": "Improving,Stable,Degrading,New,Increasing,Decreasing",
    "report_type": "Operational,Compliance,Executive,Incident,Trend,Audit,Ad-hoc",
    "frequency": "Daily,Weekly,Monthly,Quarterly,Annual,Ad-hoc",
    "generation_method": "Automated,Manual,Semi-Automated",
    "delivery_method": "Email,Portal,Dashboard,File_Share,Meeting,API",
    "gap_category": "Logging,Alerting,Monitoring,Incident_Response,Reporting,Integration,Retention,Process",
    "gap_status": "Open,In_Progress,Resolved,Accepted,Deferred",
    "fp_result": "Confirmed_FP,True_Positive,Inconclusive,Pending",
    "fp_resolution": "Whitelist,Policy_Tuning,Category_Update,No_Action,Escalated,Vendor_Update",
    "fp_recurrence": "First_Time,Recurring,Chronic",
    "fp_status": "Open,Resolved,Escalated,Pending",
    "evidence_type": "Screenshot,Configuration_Export,Log_Sample,Report,Procedure_Document,Email_Confirmation,Audit_Report,Test_Results,Policy_Document,Meeting_Minutes,Other",
    "verification_status": "Verified,Pending,Not_Verified,Expired",
}

def add_dropdown(ws, cell_range, dropdown_key):
    """Add data validation dropdown to a cell range."""
    if dropdown_key not in DROPDOWNS:
        return
    dv = DataValidation(
        type="list",
        formula1=f'"{DROPDOWNS[dropdown_key]}"',
        allow_blank=True
    )
    dv.error = "Please select from dropdown"
    dv.errorTitle = "Invalid Entry"
    dv.prompt = "Select from list"
    dv.promptTitle = "Available Options"
    ws.add_data_validation(dv)
    dv.add(cell_range)


# =============================================================================
# SECTION 2: SHEET 1 - INSTRUCTIONS & LEGEND
# =============================================================================

def create_sheet_instructions(wb, styles):
    """Create Instructions & Legend sheet."""
    ws = wb.active
    ws.title = "Instructions_Legend"
    
    # Column widths
    ws.column_dimensions["A"].width = 25
    ws.column_dimensions["B"].width = 40
    ws.column_dimensions["C"].width = 20
    ws.column_dimensions["D"].width = 50
    
    # --- Header ---
    ws.merge_cells("A1:D1")
    ws["A1"] = "ISMS-IMP-A.8.23.4 – Monitoring & Response Assessment"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:D2")
    ws["A2"] = "ISO/IEC 27001:2022 - Control A.8.23: Web Filtering"
    ws["A2"].font = Font(bold=True, size=11, color=COLORS["header_dark"])
    ws["A2"].alignment = Alignment(horizontal="center")
    
    # --- Document Information ---
    ws["A4"] = "DOCUMENT INFORMATION"
    ws["A4"].font = styles["section"]["font"]
    ws["A4"].fill = styles["section"]["fill"]
    ws.merge_cells("A4:D4")
    
    doc_info = [
        ("Document ID:", "ISMS-IMP-A.8.23.4"),
        ("Assessment Area:", "Monitoring, Logging & Incident Response"),
        ("Related Policy:", "ISMS-POL-A.8.23-S2.3, S5.C"),
        ("Version:", "1.0"),
        ("Assessment Date:", ""),
        ("Completed By:", ""),
        ("Organisation:", ""),
        ("Review Cycle:", "Quarterly"),
    ]
    
    row = 5
    for label, value in doc_info:
        ws[f"A{row}"] = label
        ws[f"A{row}"].font = styles["label"]["font"]
        ws[f"B{row}"] = value
        if value == "":
            ws[f"B{row}"].fill = styles["input"]["fill"]
            ws[f"B{row}"].border = get_border()
        row += 1
    
    # --- How to Use ---
    row += 1
    ws[f"A{row}"] = "HOW TO USE THIS WORKBOOK"
    ws[f"A{row}"].font = styles["section"]["font"]
    ws[f"A{row}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row}:D{row}")
    
    instructions = [
        "1. Navigate through each worksheet tab to assess monitoring & response capabilities",
        "2. Use dropdown menus for standardised entries (Status, Severity, Priority, etc.)",
        "3. Fill in yellow-highlighted cells with your organisation-specific information",
        "4. Document all log sources, alert rules, dashboards, and incident procedures",
        "5. Track false positives and analyze blocked event trends",
        "6. Identify gaps in Sheet 9 (Gap_Analysis) with remediation plans",
        "7. Link evidence in the Evidence_Register for audit traceability",
        "8. Obtain required approvals in Sheet 11 (Approval_Sign_Off)",
        "9. Review quarterly or after significant changes to monitoring infrastructure",
    ]
    
    row += 1
    for instr in instructions:
        ws[f"A{row}"] = instr
        ws[f"A{row}"].font = styles["normal"]["font"]
        ws[f"A{row}"].alignment = styles["normal"]["alignment"]
        ws.merge_cells(f"A{row}:D{row}")
        row += 1
    
    # --- Status Legend ---
    row += 1
    ws[f"A{row}"] = "STATUS LEGEND"
    ws[f"A{row}"].font = styles["section"]["font"]
    ws[f"A{row}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row}:D{row}")
    
    status_legend = [
        ("Implemented", COLORS["status_green"], "Fully operational and documented"),
        ("Partial", COLORS["status_yellow"], "Partially implemented, gaps exist"),
        ("Planned", COLORS["status_blue"], "Scheduled for implementation"),
        ("Not_Implemented", COLORS["status_red"], "Not in place"),
        ("N/A", COLORS["status_gray"], "Not applicable to this environment"),
    ]
    
    row += 1
    ws[f"A{row}"] = "Status"
    ws[f"B{row}"] = "Color"
    ws[f"C{row}"] = "Meaning"
    for col in ["A", "B", "C"]:
        ws[f"{col}{row}"].font = styles["subheader"]["font"]
        ws[f"{col}{row}"].fill = styles["subheader"]["fill"]
    
    row += 1
    for status, color, meaning in status_legend:
        ws[f"A{row}"] = status
        ws[f"B{row}"] = ""
        ws[f"B{row}"].fill = PatternFill(start_color=color, end_color=color,
                                         fill_type="solid")
        ws[f"C{row}"] = meaning
        row += 1
    
    # --- Priority Legend ---
    row += 1
    ws[f"A{row}"] = "PRIORITY LEGEND (for Gaps/Actions)"
    ws[f"A{row}"].font = styles["section"]["font"]
    ws[f"A{row}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row}:D{row}")
    
    priority_legend = [
        ("Critical", "Must address within 30 days"),
        ("High", "Address within 90 days"),
        ("Medium", "Address within 180 days"),
        ("Low", "Address within 12 months"),
    ]
    
    row += 1
    for priority, timeframe in priority_legend:
        ws[f"A{row}"] = priority
        ws[f"B{row}"] = timeframe
        row += 1
    
    # --- Sheet Overview ---
    row += 1
    ws[f"A{row}"] = "WORKBOOK CONTENTS"
    ws[f"A{row}"].font = styles["section"]["font"]
    ws[f"A{row}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row}:D{row}")
    
    sheets_info = [
        ("Sheet 2: Log_Collection", "Document log sources, storage, and retention"),
        ("Sheet 3: Alert_Configuration", "Alert rules, thresholds, and notifications"),
        ("Sheet 4: Monitoring_Dashboard", "Dashboards, KPIs, and review frequency"),
        ("Sheet 5: Incident_Response", "Incident handling procedures and SLAs"),
        ("Sheet 6: Blocked_Events_Analysis", "Trend analysis of blocked events"),
        ("Sheet 7: False_Positive_Mgmt", "False positive tracking and tuning"),
        ("Sheet 8: Reporting_Schedule", "Regular reports and distribution"),
        ("Sheet 9: Gap_Analysis", "Identified gaps with remediation plans"),
        ("Sheet 10: Evidence_Register", "Evidence catalog for audit"),
        ("Sheet 11: Approval_Sign_Off", "Assessment approval workflow"),
    ]
    
    row += 1
    for sheet, desc in sheets_info:
        ws[f"A{row}"] = sheet
        ws[f"A{row}"].font = Font(bold=True, size=10)
        ws[f"B{row}"] = desc
        row += 1
    
    # --- Feynman Quote (Easter Egg) ---
    row += 2
    ws[f"A{row}"] = "💡 Remember:"
    ws[f"A{row}"].font = Font(bold=True, italic=True, size=10)
    row += 1
    ws[f"A{row}"] = '"The first principle is that you must not fool yourself — and you are the easiest person to fool."'
    ws.merge_cells(f"A{row}:D{row}")
    ws[f"A{row}"].font = Font(italic=True, size=9)
    row += 1
    ws[f"A{row}"] = "— Richard Feynman (applies to monitoring dashboards that nobody looks at)"
    ws[f"A{row}"].font = Font(italic=True, size=9, color="666666")
    
    # Freeze panes
    ws.freeze_panes = "A4"
    
    return ws

# =============================================================================
# SECTION 3: SHEET 2 - LOG COLLECTION
# =============================================================================

def create_sheet_log_collection(wb, styles):
    """Create Log Collection assessment sheet."""
    ws = wb.create_sheet("Log_Collection")
    
    # Column widths
    col_widths = {
        "A": 14, "B": 28, "C": 22, "D": 25, "E": 20,
        "F": 22, "G": 14, "H": 16, "I": 18, "J": 18,
        "K": 14, "L": 18, "M": 35
    }
    for col, width in col_widths.items():
        ws.column_dimensions[col].width = width
    
    # --- Header ---
    ws.merge_cells("A1:M1")
    ws["A1"] = "LOG COLLECTION ASSESSMENT"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:M2")
    ws["A2"] = "Document all web filtering log sources, collection methods, storage, and retention compliance"
    ws["A2"].font = Font(italic=True, size=10)
    ws["A2"].alignment = Alignment(horizontal="center")
    
    # --- Section A: Log Source Inventory ---
    ws["A4"] = "SECTION A: LOG SOURCE INVENTORY"
    ws["A4"].font = styles["section"]["font"]
    ws["A4"].fill = styles["section"]["fill"]
    ws.merge_cells("A4:M4")
    
    # Column headers
    headers_a = [
        "Log_Source_ID", "Log_Source_Name", "Log_Type", "Source_System",
        "Collection_Method", "Destination", "Format", "Retention_Days",
        "Retention_Compliant", "Volume_Daily", "Status", "Evidence_Ref", "Notes"
    ]
    
    for col_num, header in enumerate(headers_a, 1):
        cell = ws.cell(row=5, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.alignment = styles["subheader"]["alignment"]
        cell.border = get_border()
    
    # Data rows (30 log sources)
    for i in range(30):
        row = 6 + i
        ws[f"A{row}"] = f"LOG-{i+1:03d}"
        ws[f"A{row}"].font = Font(bold=True)
        
        # Apply input styling and borders
        for col in range(2, 14):
            cell = ws.cell(row=row, column=col)
            cell.fill = styles["input"]["fill"]
            cell.border = get_border()
            cell.alignment = styles["normal"]["alignment"]
    
    # Add dropdowns for log source inventory
    add_dropdown(ws, "C6:C35", "log_type")
    add_dropdown(ws, "E6:E35", "collection_method")
    add_dropdown(ws, "F6:F35", "destination")
    add_dropdown(ws, "G6:G35", "format")
    add_dropdown(ws, "I6:I35", "yes_no_partial")
    add_dropdown(ws, "K6:K35", "status")
    
    # --- Section B: Retention Requirements ---
    row_b = 38
    ws[f"A{row_b}"] = "SECTION B: RETENTION REQUIREMENTS"
    ws[f"A{row_b}"].font = styles["section"]["font"]
    ws[f"A{row_b}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_b}:G{row_b}")
    
    headers_b = [
        "Requirement_ID", "Requirement_Source", "Log_Type_Affected",
        "Min_Retention_Days", "Current_Retention", "Compliant", "Notes"
    ]
    
    row_b += 1
    for col_num, header in enumerate(headers_b, 1):
        cell = ws.cell(row=row_b, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.alignment = styles["subheader"]["alignment"]
        cell.border = get_border()
    
    # Retention requirement rows (10 requirements)
    req_sources = ["Regulatory", "Policy", "Contractual", "Best_Practice"]
    for i in range(10):
        row = row_b + 1 + i
        ws[f"A{row}"] = f"RET-{i+1:03d}"
        ws[f"A{row}"].font = Font(bold=True)
        
        for col in range(2, 8):
            cell = ws.cell(row=row, column=col)
            cell.fill = styles["input"]["fill"]
            cell.border = get_border()
    
    # Dropdown for requirement source
    dv_req = DataValidation(type="list", 
                            formula1='"Regulatory,Policy,Contractual,Best_Practice"',
                            allow_blank=True)
    ws.add_data_validation(dv_req)
    dv_req.add(f"B{row_b+1}:B{row_b+10}")
    
    add_dropdown(ws, f"F{row_b+1}:F{row_b+10}", "yes_no_partial")
    
    # --- Section C: Summary Metrics ---
    row_c = 52
    ws[f"A{row_c}"] = "SECTION C: SUMMARY METRICS"
    ws[f"A{row_c}"].font = styles["section"]["font"]
    ws[f"A{row_c}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_c}:D{row_c}")
    
    metrics = [
        ("Total log sources configured:", '=COUNTA(B6:B35)'),
        ("Blocked request log sources:", '=COUNTIF(C6:C35,"Blocked_Requests")'),
        ("Sources meeting retention:", '=COUNTIF(I6:I35,"Yes")'),
        ("Retention compliance rate:", '=IF(COUNTA(I6:I35)>0,COUNTIF(I6:I35,"Yes")/COUNTA(I6:I35),0)'),
        ("Implemented sources:", '=COUNTIF(K6:K35,"Implemented")'),
        ("Sources needing attention:", '=COUNTIF(K6:K35,"Partial")+COUNTIF(K6:K35,"Not_Implemented")'),
    ]
    
    row_c += 1
    for label, formula in metrics:
        ws[f"A{row_c}"] = label
        ws[f"A{row_c}"].font = styles["label"]["font"]
        ws[f"B{row_c}"] = formula
        ws[f"B{row_c}"].border = get_border()
        if "rate" in label.lower():
            ws[f"B{row_c}"].number_format = "0.0%"
        row_c += 1
    
    # Freeze panes
    ws.freeze_panes = "A6"
    
    return ws


# =============================================================================
# SECTION 4: SHEET 3 - ALERT CONFIGURATION
# =============================================================================

def create_sheet_alert_configuration(wb, styles):
    """Create Alert Configuration assessment sheet."""
    ws = wb.create_sheet("Alert_Configuration")
    
    # Column widths
    col_widths = {
        "A": 12, "B": 32, "C": 20, "D": 38, "E": 18,
        "F": 14, "G": 22, "H": 25, "I": 20, "J": 25,
        "K": 15, "L": 14, "M": 14, "N": 15
    }
    for col, width in col_widths.items():
        ws.column_dimensions[col].width = width
    
    # --- Header ---
    ws.merge_cells("A1:N1")
    ws["A1"] = "ALERT CONFIGURATION ASSESSMENT"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:N2")
    ws["A2"] = "Document alerting rules, thresholds, notification methods, and escalation paths"
    ws["A2"].font = Font(italic=True, size=10)
    ws["A2"].alignment = Alignment(horizontal="center")
    
    # --- Section A: Alert Rules Inventory ---
    ws["A4"] = "SECTION A: ALERT RULES INVENTORY"
    ws["A4"].font = styles["section"]["font"]
    ws["A4"].fill = styles["section"]["fill"]
    ws.merge_cells("A4:N4")
    
    headers_a = [
        "Alert_ID", "Alert_Name", "Alert_Category", "Trigger_Condition",
        "Threshold_Value", "Severity", "Notification_Method", "Recipients",
        "Response_SLA_Min", "Escalation_Path", "Auto_Response", "Status",
        "Last_Triggered", "Evidence_Ref"
    ]
    
    for col_num, header in enumerate(headers_a, 1):
        cell = ws.cell(row=5, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.alignment = styles["subheader"]["alignment"]
        cell.border = get_border()
    
    # Data rows (40 alert rules)
    for i in range(40):
        row = 6 + i
        ws[f"A{row}"] = f"ALR-{i+1:03d}"
        ws[f"A{row}"].font = Font(bold=True)
        
        for col in range(2, 15):
            cell = ws.cell(row=row, column=col)
            cell.fill = styles["input"]["fill"]
            cell.border = get_border()
            cell.alignment = styles["normal"]["alignment"]
    
    # Add dropdowns
    add_dropdown(ws, "C6:C45", "alert_category")
    add_dropdown(ws, "F6:F45", "severity")
    add_dropdown(ws, "G6:G45", "notification_method")
    add_dropdown(ws, "K6:K45", "yes_no_partial")
    add_dropdown(ws, "L6:L45", "status")
    
    # --- Section B: Alert Categories Summary ---
    row_b = 48
    ws[f"A{row_b}"] = "SECTION B: ALERT CATEGORIES SUMMARY"
    ws[f"A{row_b}"].font = styles["section"]["font"]
    ws[f"A{row_b}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_b}:E{row_b}")
    
    cat_headers = ["Category", "Count", "Active", "Critical_Count", "Notes"]
    row_b += 1
    for col_num, header in enumerate(cat_headers, 1):
        cell = ws.cell(row=row_b, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.border = get_border()
    
    categories = [
        "Threat_Detection", "Policy_Violation", "System_Health",
        "Threshold_Breach", "Anomaly", "Compliance"
    ]
    
    row_b += 1
    for cat in categories:
        ws[f"A{row_b}"] = cat
        ws[f"B{row_b}"] = f'=COUNTIF(C6:C45,"{cat}")'
        ws[f"C{row_b}"] = f'=COUNTIFS(C6:C45,"{cat}",L6:L45,"Implemented")'
        ws[f"D{row_b}"] = f'=COUNTIFS(C6:C45,"{cat}",F6:F45,"Critical")'
        ws[f"E{row_b}"].fill = styles["input"]["fill"]
        for col in ["A", "B", "C", "D", "E"]:
            ws[f"{col}{row_b}"].border = get_border()
        row_b += 1
    
    # --- Section C: Summary Metrics ---
    row_c = row_b + 2
    ws[f"A{row_c}"] = "SECTION C: SUMMARY METRICS"
    ws[f"A{row_c}"].font = styles["section"]["font"]
    ws[f"A{row_c}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_c}:D{row_c}")
    
    metrics = [
        ("Total alert rules configured:", '=COUNTA(B6:B45)'),
        ("Implemented alerts:", '=COUNTIF(L6:L45,"Implemented")'),
        ("Critical severity alerts:", '=COUNTIF(F6:F45,"Critical")'),
        ("High severity alerts:", '=COUNTIF(F6:F45,"High")'),
        ("Alerts with auto-response:", '=COUNTIF(K6:K45,"Yes")'),
        ("Alert coverage score:", '=IF(COUNTA(B6:B45)>0,COUNTIF(L6:L45,"Implemented")/COUNTA(B6:B45),0)'),
    ]
    
    row_c += 1
    for label, formula in metrics:
        ws[f"A{row_c}"] = label
        ws[f"A{row_c}"].font = styles["label"]["font"]
        ws[f"B{row_c}"] = formula
        ws[f"B{row_c}"].border = get_border()
        if "score" in label.lower():
            ws[f"B{row_c}"].number_format = "0.0%"
        row_c += 1
    
    # Freeze panes
    ws.freeze_panes = "A6"
    
    return ws

# =============================================================================
# SECTION 5: SHEET 4 - MONITORING DASHBOARD
# =============================================================================

def create_sheet_monitoring_dashboard(wb, styles):
    """Create Monitoring Dashboard assessment sheet."""
    ws = wb.create_sheet("Monitoring_Dashboard")
    
    # Column widths
    col_widths = {
        "A": 14, "B": 32, "C": 20, "D": 20, "E": 18,
        "F": 18, "G": 45, "H": 18, "I": 14, "J": 18
    }
    for col, width in col_widths.items():
        ws.column_dimensions[col].width = width
    
    # --- Header ---
    ws.merge_cells("A1:J1")
    ws["A1"] = "MONITORING DASHBOARD ASSESSMENT"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:J2")
    ws["A2"] = "Document monitoring dashboards, KPIs tracked, and review frequency"
    ws["A2"].font = Font(italic=True, size=10)
    ws["A2"].alignment = Alignment(horizontal="center")
    
    # --- Section A: Dashboard Inventory ---
    ws["A4"] = "SECTION A: DASHBOARD INVENTORY"
    ws["A4"].font = styles["section"]["font"]
    ws["A4"].fill = styles["section"]["fill"]
    ws.merge_cells("A4:J4")
    
    headers_a = [
        "Dashboard_ID", "Dashboard_Name", "Platform", "Primary_Audience",
        "Update_Frequency", "Review_Frequency", "Key_Metrics_Displayed",
        "Alerting_Integrated", "Status", "Evidence_Ref"
    ]
    
    for col_num, header in enumerate(headers_a, 1):
        cell = ws.cell(row=5, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.alignment = styles["subheader"]["alignment"]
        cell.border = get_border()
    
    # Data rows (20 dashboards)
    for i in range(20):
        row = 6 + i
        ws[f"A{row}"] = f"DSH-{i+1:03d}"
        ws[f"A{row}"].font = Font(bold=True)
        
        for col in range(2, 11):
            cell = ws.cell(row=row, column=col)
            cell.fill = styles["input"]["fill"]
            cell.border = get_border()
            cell.alignment = styles["normal"]["alignment"]
    
    # Add dropdowns
    add_dropdown(ws, "C6:C25", "dashboard_platform")
    add_dropdown(ws, "D6:D25", "audience")
    add_dropdown(ws, "E6:E25", "update_frequency")
    add_dropdown(ws, "F6:F25", "update_frequency")  # Same options for review
    add_dropdown(ws, "H6:H25", "yes_no")
    add_dropdown(ws, "I6:I25", "status")
    
    # --- Section B: Key Performance Indicators ---
    row_b = 28
    ws[f"A{row_b}"] = "SECTION B: KEY PERFORMANCE INDICATORS (KPIs)"
    ws[f"A{row_b}"].font = styles["section"]["font"]
    ws[f"A{row_b}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_b}:J{row_b}")
    
    kpi_headers = [
        "KPI_ID", "KPI_Name", "Category", "Measurement_Unit",
        "Target_Value", "Current_Value", "Trend", "Review_Freq",
        "Owner_Role", "Status"
    ]
    
    row_b += 1
    for col_num, header in enumerate(kpi_headers, 1):
        cell = ws.cell(row=row_b, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.alignment = styles["subheader"]["alignment"]
        cell.border = get_border()
    
    # Pre-populated KPIs (20 KPIs with suggested names)
    suggested_kpis = [
        ("Total blocked requests (daily)", "Volume", "Count"),
        ("Block rate percentage", "Security", "Percentage"),
        ("Malware blocks (daily)", "Security", "Count"),
        ("Phishing blocks (daily)", "Security", "Count"),
        ("Policy violation blocks", "Compliance", "Count"),
        ("Bypass attempts detected", "Security", "Count"),
        ("False positive rate", "Operational", "Percentage"),
        ("False positive resolution time", "Operational", "Hours"),
        ("Alert response time (avg)", "Performance", "Minutes"),
        ("Critical incident response time", "Performance", "Minutes"),
        ("User complaints (weekly)", "Operational", "Count"),
        ("Exception requests (monthly)", "Compliance", "Count"),
        ("Log collection uptime", "Performance", "Percentage"),
        ("Dashboard availability", "Performance", "Percentage"),
        ("Report delivery on-time rate", "Operational", "Percentage"),
        ("SLA compliance rate", "Compliance", "Percentage"),
        ("Unique users blocked (daily)", "Volume", "Count"),
        ("Top category blocks", "Volume", "Category"),
        ("Threat intelligence hits", "Security", "Count"),
        ("Configuration change count", "Operational", "Count"),
    ]
    
    row_b += 1
    for i, (kpi_name, category, unit) in enumerate(suggested_kpis):
        row = row_b + i
        ws[f"A{row}"] = f"KPI-{i+1:03d}"
        ws[f"A{row}"].font = Font(bold=True)
        ws[f"B{row}"] = kpi_name
        ws[f"C{row}"] = category
        ws[f"D{row}"] = unit
        
        for col in range(2, 11):
            cell = ws.cell(row=row, column=col)
            if col > 4:  # Only highlight input columns
                cell.fill = styles["input"]["fill"]
            cell.border = get_border()
            cell.alignment = styles["normal"]["alignment"]
    
    # Add dropdowns for KPIs
    add_dropdown(ws, f"C{row_b}:C{row_b+19}", "kpi_category")
    add_dropdown(ws, f"G{row_b}:G{row_b+19}", "trend")
    add_dropdown(ws, f"H{row_b}:H{row_b+19}", "frequency")
    add_dropdown(ws, f"J{row_b}:J{row_b+19}", "kpi_status")
    
    # --- Section C: Summary Metrics ---
    row_c = row_b + 22
    ws[f"A{row_c}"] = "SECTION C: SUMMARY METRICS"
    ws[f"A{row_c}"].font = styles["section"]["font"]
    ws[f"A{row_c}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_c}:D{row_c}")
    
    metrics = [
        ("Total dashboards configured:", '=COUNTA(B6:B25)'),
        ("Dashboards with alerting:", '=COUNTIF(H6:H25,"Yes")'),
        ("Real-time dashboards:", '=COUNTIF(E6:E25,"Real-Time")'),
        ("KPIs defined:", '=COUNTA(B30:B49)'),
        ("KPIs meeting target:", f'=COUNTIF(J{row_b}:J{row_b+19},"Met")'),
        ("KPIs at risk:", f'=COUNTIF(J{row_b}:J{row_b+19},"At_Risk")+COUNTIF(J{row_b}:J{row_b+19},"Not_Met")'),
    ]
    
    row_c += 1
    for label, formula in metrics:
        ws[f"A{row_c}"] = label
        ws[f"A{row_c}"].font = styles["label"]["font"]
        ws[f"B{row_c}"] = formula
        ws[f"B{row_c}"].border = get_border()
        row_c += 1
    
    # Freeze panes
    ws.freeze_panes = "A6"
    
    return ws


# =============================================================================
# SECTION 6: SHEET 5 - INCIDENT RESPONSE
# =============================================================================

def create_sheet_incident_response(wb, styles):
    """Create Incident Response assessment sheet."""
    ws = wb.create_sheet("Incident_Response")
    
    # Column widths
    col_widths = {
        "A": 14, "B": 32, "C": 16, "D": 20, "E": 20,
        "F": 20, "G": 30, "H": 20, "I": 14, "J": 20
    }
    for col, width in col_widths.items():
        ws.column_dimensions[col].width = width
    
    # --- Header ---
    ws.merge_cells("A1:J1")
    ws["A1"] = "INCIDENT RESPONSE ASSESSMENT"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:J2")
    ws["A2"] = "Document incident categories, SLAs, response procedures, and performance metrics"
    ws["A2"].font = Font(italic=True, size=10)
    ws["A2"].alignment = Alignment(horizontal="center")
    
    # --- Section A: Incident Categories ---
    ws["A4"] = "SECTION A: INCIDENT CATEGORIES & SLAs"
    ws["A4"].font = styles["section"]["font"]
    ws["A4"].fill = styles["section"]["fill"]
    ws.merge_cells("A4:I4")
    
    headers_a = [
        "Category_ID", "Incident_Category", "Default_Severity",
        "Response_SLA_Min", "Resolution_SLA_Hrs", "Escalation_Threshold",
        "Response_Procedure", "Owner_Role", "Status"
    ]
    
    for col_num, header in enumerate(headers_a, 1):
        cell = ws.cell(row=5, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.alignment = styles["subheader"]["alignment"]
        cell.border = get_border()
    
    # Pre-populated incident categories
    incident_cats = [
        ("Malware delivery attempt", "Critical", 15, 4),
        ("Phishing site access", "Critical", 15, 4),
        ("Command & Control communication", "Critical", 15, 2),
        ("Data exfiltration attempt", "Critical", 15, 4),
        ("Exploit kit encounter", "High", 30, 8),
        ("Policy violation - gambling", "Medium", 60, 24),
        ("Policy violation - adult content", "Medium", 60, 24),
        ("Unauthorised bypass attempt", "High", 30, 8),
        ("Web filter system failure", "Critical", 15, 4),
        ("Log collection failure", "High", 30, 8),
        ("False positive - business impact", "Medium", 60, 24),
        ("User access exception request", "Low", 240, 72),
        ("Suspicious URL reported", "Medium", 60, 24),
        ("Category misclassification", "Low", 240, 72),
        ("Performance degradation", "Medium", 60, 24),
    ]
    
    for i, (cat_name, severity, response_sla, resolution_sla) in enumerate(incident_cats):
        row = 6 + i
        ws[f"A{row}"] = f"CAT-{i+1:03d}"
        ws[f"A{row}"].font = Font(bold=True)
        ws[f"B{row}"] = cat_name
        ws[f"C{row}"] = severity
        ws[f"D{row}"] = response_sla
        ws[f"E{row}"] = resolution_sla
        
        for col in range(2, 10):
            cell = ws.cell(row=row, column=col)
            if col > 5:  # Only highlight non-prepopulated columns
                cell.fill = styles["input"]["fill"]
            cell.border = get_border()
            cell.alignment = styles["normal"]["alignment"]
    
    add_dropdown(ws, "C6:C20", "severity")
    add_dropdown(ws, "I6:I20", "status")
    
    # --- Section B: SLA Performance ---
    row_b = 24
    ws[f"A{row_b}"] = "SECTION B: SLA PERFORMANCE (Last 90 Days)"
    ws[f"A{row_b}"].font = styles["section"]["font"]
    ws[f"A{row_b}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_b}:E{row_b}")
    
    sla_headers = ["Metric", "Target", "Actual", "Status", "Notes"]
    row_b += 1
    for col_num, header in enumerate(sla_headers, 1):
        cell = ws.cell(row=row_b, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.border = get_border()
    
    sla_metrics = [
        ("Critical incident response time", "<15 min"),
        ("High incident response time", "<30 min"),
        ("Medium incident response time", "<60 min"),
        ("Low incident response time", "<4 hours"),
        ("Critical resolution time", "<4 hours"),
        ("High resolution time", "<8 hours"),
        ("Medium resolution time", "<24 hours"),
        ("Overall SLA compliance rate", ">95%"),
        ("Mean time to detect (MTTD)", "<5 min"),
        ("Mean time to respond (MTTR)", "<30 min"),
    ]
    
    row_b += 1
    for metric, target in sla_metrics:
        ws[f"A{row_b}"] = metric
        ws[f"B{row_b}"] = target
        ws[f"C{row_b}"].fill = styles["input"]["fill"]
        ws[f"D{row_b}"].fill = styles["input"]["fill"]
        ws[f"E{row_b}"].fill = styles["input"]["fill"]
        for col in ["A", "B", "C", "D", "E"]:
            ws[f"{col}{row_b}"].border = get_border()
        row_b += 1
    
    add_dropdown(ws, f"D{row_b-10}:D{row_b-1}", "kpi_status")
    
    # --- Section C: Recent Incident Summary ---
    row_c = row_b + 2
    ws[f"A{row_c}"] = "SECTION C: RECENT INCIDENT SUMMARY (Last 20 Incidents)"
    ws[f"A{row_c}"].font = styles["section"]["font"]
    ws[f"A{row_c}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_c}:J{row_c}")
    
    inc_headers = [
        "Incident_ID", "Date_Detected", "Category", "Severity",
        "Response_Time_Min", "Resolution_Time_Hrs", "SLA_Met",
        "Root_Cause", "Lessons_Learned", "Evidence_Ref"
    ]
    
    row_c += 1
    for col_num, header in enumerate(inc_headers, 1):
        cell = ws.cell(row=row_c, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.alignment = styles["subheader"]["alignment"]
        cell.border = get_border()
    
    # Incident log rows (20 incidents)
    row_c += 1
    for i in range(20):
        row = row_c + i
        ws[f"A{row}"] = f"INC-{i+1:03d}"
        ws[f"A{row}"].font = Font(bold=True)
        
        for col in range(2, 11):
            cell = ws.cell(row=row, column=col)
            cell.fill = styles["input"]["fill"]
            cell.border = get_border()
            cell.alignment = styles["normal"]["alignment"]
    
    add_dropdown(ws, f"D{row_c}:D{row_c+19}", "severity")
    add_dropdown(ws, f"G{row_c}:G{row_c+19}", "yes_no")
    
    # Freeze panes
    ws.freeze_panes = "A6"
    
    return ws

# =============================================================================
# SECTION 7: SHEET 6 - BLOCKED EVENTS ANALYSIS
# =============================================================================

def create_sheet_blocked_events(wb, styles):
    """Create Blocked Events Analysis sheet."""
    ws = wb.create_sheet("Blocked_Events_Analysis")
    
    # Column widths
    col_widths = {
        "A": 14, "B": 30, "C": 20, "D": 20, "E": 16,
        "F": 25, "G": 14, "H": 16, "I": 35
    }
    for col, width in col_widths.items():
        ws.column_dimensions[col].width = width
    
    # --- Header ---
    ws.merge_cells("A1:I1")
    ws["A1"] = "BLOCKED EVENTS ANALYSIS"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:I2")
    ws["A2"] = "Analyze patterns, trends, and categories of blocked web filtering events"
    ws["A2"].font = Font(italic=True, size=10)
    ws["A2"].alignment = Alignment(horizontal="center")
    
    # --- Section A: Blocked Event Categories ---
    ws["A4"] = "SECTION A: BLOCKED EVENT CATEGORIES"
    ws["A4"].font = styles["section"]["font"]
    ws["A4"].fill = styles["section"]["fill"]
    ws.merge_cells("A4:I4")
    
    headers_a = [
        "Category_ID", "Block_Category", "Events_30_Days", "Events_90_Days",
        "Trend", "Top_Source", "Risk_Level", "Action_Required", "Notes"
    ]
    
    for col_num, header in enumerate(headers_a, 1):
        cell = ws.cell(row=5, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.alignment = styles["subheader"]["alignment"]
        cell.border = get_border()
    
    # Pre-populated block categories
    block_categories = [
        "Malware",
        "Phishing",
        "Command & Control",
        "Exploit Kits",
        "Ransomware",
        "Cryptomining",
        "Spam URLs",
        "Adult Content",
        "Gambling",
        "Social Media (if blocked)",
        "Streaming Media (if blocked)",
        "File Sharing",
        "Proxy/Anonymizer",
        "Hacking Tools",
        "Policy Violations - Other",
        "Uncategorized High-Risk",
        "User-Reported Blocks",
        "Geo-Blocked Content",
        "Bandwidth Abuse",
        "Other",
    ]
    
    for i, category in enumerate(block_categories):
        row = 6 + i
        ws[f"A{row}"] = f"BLK-{i+1:03d}"
        ws[f"A{row}"].font = Font(bold=True)
        ws[f"B{row}"] = category
        
        for col in range(2, 10):
            cell = ws.cell(row=row, column=col)
            if col > 2:  # Only highlight input columns
                cell.fill = styles["input"]["fill"]
            cell.border = get_border()
            cell.alignment = styles["normal"]["alignment"]
    
    add_dropdown(ws, "E6:E25", "trend")
    add_dropdown(ws, "G6:G25", "priority")  # Risk level uses priority values
    add_dropdown(ws, "H6:H25", "yes_no")
    
    # --- Section B: Top Blocked Threats ---
    row_b = 28
    ws[f"A{row_b}"] = "SECTION B: TOP 10 BLOCKED THREATS (Last 30 Days)"
    ws[f"A{row_b}"].font = styles["section"]["font"]
    ws[f"A{row_b}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_b}:F{row_b}")
    
    top_headers = ["Rank", "Threat_Type/URL", "Count_30_Days", "Percentage", 
                   "Mitigation_Status", "Notes"]
    row_b += 1
    for col_num, header in enumerate(top_headers, 1):
        cell = ws.cell(row=row_b, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.border = get_border()
    
    row_b += 1
    for i in range(10):
        ws[f"A{row_b + i}"] = i + 1
        ws[f"A{row_b + i}"].font = Font(bold=True)
        ws[f"A{row_b + i}"].alignment = Alignment(horizontal="center")
        for col in range(2, 7):
            cell = ws.cell(row=row_b + i, column=col)
            cell.fill = styles["input"]["fill"]
            cell.border = get_border()
    
    add_dropdown(ws, f"E{row_b}:E{row_b+9}", "status")
    
    # --- Section C: 6-Month Trend Analysis ---
    row_c = row_b + 12
    ws[f"A{row_c}"] = "SECTION C: 6-MONTH TREND ANALYSIS"
    ws[f"A{row_c}"].font = styles["section"]["font"]
    ws[f"A{row_c}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_c}:G{row_c}")
    
    trend_headers = ["Month", "Total_Blocked", "Malware", "Phishing", 
                     "Policy_Violation", "Other", "Notes"]
    row_c += 1
    for col_num, header in enumerate(trend_headers, 1):
        cell = ws.cell(row=row_c, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.border = get_border()
    
    # 6 months of trend data
    row_c += 1
    months = ["Month-6", "Month-5", "Month-4", "Month-3", "Month-2", "Current"]
    for i, month in enumerate(months):
        ws[f"A{row_c + i}"] = month
        ws[f"A{row_c + i}"].font = Font(bold=True)
        for col in range(2, 8):
            cell = ws.cell(row=row_c + i, column=col)
            cell.fill = styles["input"]["fill"]
            cell.border = get_border()
    
    # --- Section D: Summary Metrics ---
    row_d = row_c + 8
    ws[f"A{row_d}"] = "SECTION D: SUMMARY METRICS"
    ws[f"A{row_d}"].font = styles["section"]["font"]
    ws[f"A{row_d}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_d}:D{row_d}")
    
    metrics = [
        ("Categories tracked:", '=COUNTA(B6:B25)'),
        ("Categories requiring action:", '=COUNTIF(H6:H25,"Yes")'),
        ("High-risk categories:", '=COUNTIF(G6:G25,"Critical")+COUNTIF(G6:G25,"High")'),
        ("Categories with increasing trend:", '=COUNTIF(E6:E25,"Increasing")'),
    ]
    
    row_d += 1
    for label, formula in metrics:
        ws[f"A{row_d}"] = label
        ws[f"A{row_d}"].font = styles["label"]["font"]
        ws[f"B{row_d}"] = formula
        ws[f"B{row_d}"].border = get_border()
        row_d += 1
    
    # Freeze panes
    ws.freeze_panes = "A6"
    
    return ws


# =============================================================================
# SECTION 8: SHEET 7 - FALSE POSITIVE MANAGEMENT
# =============================================================================

def create_sheet_false_positive(wb, styles):
    """Create False Positive Management sheet."""
    ws = wb.create_sheet("False_Positive_Mgmt")
    
    # Column widths
    col_widths = {
        "A": 12, "B": 14, "C": 20, "D": 28, "E": 35,
        "F": 20, "G": 22, "H": 14, "I": 20, "J": 14,
        "K": 14, "L": 15
    }
    for col, width in col_widths.items():
        ws.column_dimensions[col].width = width
    
    # --- Header ---
    ws.merge_cells("A1:L1")
    ws["A1"] = "FALSE POSITIVE MANAGEMENT"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:L2")
    ws["A2"] = "Track false positives, tuning actions, and resolution effectiveness"
    ws["A2"].font = Font(italic=True, size=10)
    ws["A2"].alignment = Alignment(horizontal="center")
    
    # --- Section A: False Positive Log ---
    ws["A4"] = "SECTION A: FALSE POSITIVE LOG"
    ws["A4"].font = styles["section"]["font"]
    ws["A4"].fill = styles["section"]["fill"]
    ws.merge_cells("A4:L4")
    
    headers_a = [
        "FP_ID", "Date_Reported", "Reported_By", "Blocked_URL_Category",
        "Business_Justification", "Investigation_Result", "Resolution_Action",
        "Resolution_Date", "Resolution_Time_Hrs", "Recurrence", "Status", "Evidence_Ref"
    ]
    
    for col_num, header in enumerate(headers_a, 1):
        cell = ws.cell(row=5, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.alignment = styles["subheader"]["alignment"]
        cell.border = get_border()
    
    # Data rows (50 FP entries)
    for i in range(50):
        row = 6 + i
        ws[f"A{row}"] = f"FP-{i+1:03d}"
        ws[f"A{row}"].font = Font(bold=True)
        
        for col in range(2, 13):
            cell = ws.cell(row=row, column=col)
            cell.fill = styles["input"]["fill"]
            cell.border = get_border()
            cell.alignment = styles["normal"]["alignment"]
    
    # Add dropdowns
    add_dropdown(ws, "F6:F55", "fp_result")
    add_dropdown(ws, "G6:G55", "fp_resolution")
    add_dropdown(ws, "J6:J55", "fp_recurrence")
    add_dropdown(ws, "K6:K55", "fp_status")
    
    # --- Section B: False Positive Metrics ---
    row_b = 58
    ws[f"A{row_b}"] = "SECTION B: FALSE POSITIVE METRICS"
    ws[f"A{row_b}"].font = styles["section"]["font"]
    ws[f"A{row_b}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_b}:E{row_b}")
    
    metric_headers = ["Metric", "Value", "Target", "Status", "Notes"]
    row_b += 1
    for col_num, header in enumerate(metric_headers, 1):
        cell = ws.cell(row=row_b, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.border = get_border()
    
    fp_metrics = [
        ("Total FPs reported (last 90 days)", '=COUNTA(B6:B55)', "<50"),
        ("Average resolution time (hours)", '=IFERROR(AVERAGE(I6:I55),"N/A")', "<24"),
        ("Open FPs", '=COUNTIF(K6:K55,"Open")', "<10"),
        ("Confirmed FP rate", '=IFERROR(COUNTIF(F6:F55,"Confirmed_FP")/COUNTA(F6:F55),"N/A")', ">80%"),
        ("Recurring FP percentage", '=IFERROR((COUNTIF(J6:J55,"Recurring")+COUNTIF(J6:J55,"Chronic"))/COUNTA(J6:J55),"N/A")', "<10%"),
        ("FPs escalated", '=COUNTIF(K6:K55,"Escalated")', "<5"),
        ("FPs resolved via whitelist", '=COUNTIF(G6:G55,"Whitelist")', "Monitor"),
        ("FPs resolved via tuning", '=COUNTIF(G6:G55,"Policy_Tuning")', "Monitor"),
    ]
    
    row_b += 1
    for metric, formula, target in fp_metrics:
        ws[f"A{row_b}"] = metric
        ws[f"A{row_b}"].font = styles["label"]["font"]
        ws[f"B{row_b}"] = formula
        ws[f"C{row_b}"] = target
        ws[f"D{row_b}"].fill = styles["input"]["fill"]
        ws[f"E{row_b}"].fill = styles["input"]["fill"]
        for col in ["A", "B", "C", "D", "E"]:
            ws[f"{col}{row_b}"].border = get_border()
        row_b += 1
    
    add_dropdown(ws, f"D{row_b-8}:D{row_b-1}", "kpi_status")
    
    # Freeze panes
    ws.freeze_panes = "A6"
    
    return ws


# =============================================================================
# SECTION 9: SHEET 8 - REPORTING SCHEDULE
# =============================================================================

def create_sheet_reporting_schedule(wb, styles):
    """Create Reporting Schedule sheet."""
    ws = wb.create_sheet("Reporting_Schedule")
    
    # Column widths
    col_widths = {
        "A": 12, "B": 32, "C": 18, "D": 14, "E": 18,
        "F": 28, "G": 18, "H": 40, "I": 14, "J": 14, "K": 15
    }
    for col, width in col_widths.items():
        ws.column_dimensions[col].width = width
    
    # --- Header ---
    ws.merge_cells("A1:K1")
    ws["A1"] = "REPORTING SCHEDULE"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:K2")
    ws["A2"] = "Document regular reports generated for web filtering operations"
    ws["A2"].font = Font(italic=True, size=10)
    ws["A2"].alignment = Alignment(horizontal="center")
    
    # --- Section A: Report Inventory ---
    ws["A4"] = "SECTION A: REPORT INVENTORY"
    ws["A4"].font = styles["section"]["font"]
    ws["A4"].fill = styles["section"]["fill"]
    ws.merge_cells("A4:K4")
    
    headers_a = [
        "Report_ID", "Report_Name", "Report_Type", "Frequency",
        "Generation_Method", "Distribution_List", "Delivery_Method",
        "Content_Summary", "Last_Generated", "Status", "Evidence_Ref"
    ]
    
    for col_num, header in enumerate(headers_a, 1):
        cell = ws.cell(row=5, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.alignment = styles["subheader"]["alignment"]
        cell.border = get_border()
    
    # Pre-populated report types (20 reports)
    suggested_reports = [
        ("Daily Threat Summary", "Operational", "Daily"),
        ("Weekly Block Statistics", "Operational", "Weekly"),
        ("Monthly Executive Dashboard", "Executive", "Monthly"),
        ("Quarterly Compliance Report", "Compliance", "Quarterly"),
        ("Annual Security Review", "Audit", "Annual"),
        ("Incident Summary Report", "Incident", "Weekly"),
        ("False Positive Analysis", "Operational", "Monthly"),
        ("User Activity Report", "Compliance", "Monthly"),
        ("Policy Exception Report", "Compliance", "Monthly"),
        ("Top Blocked Sites Report", "Trend", "Weekly"),
        ("Bandwidth Usage Report", "Operational", "Weekly"),
        ("SLA Performance Report", "Operational", "Monthly"),
        ("Category Statistics", "Trend", "Monthly"),
        ("Alert Summary Report", "Operational", "Daily"),
        ("System Health Report", "Operational", "Daily"),
        ("Audit Trail Report", "Audit", "Monthly"),
        ("User Training Status", "Compliance", "Quarterly"),
        ("Risk Assessment Update", "Executive", "Quarterly"),
        ("Vendor Update Summary", "Operational", "Monthly"),
        ("Custom Ad-hoc Report", "Ad-hoc", "Ad-hoc"),
    ]
    
    for i, (report_name, report_type, frequency) in enumerate(suggested_reports):
        row = 6 + i
        ws[f"A{row}"] = f"RPT-{i+1:03d}"
        ws[f"A{row}"].font = Font(bold=True)
        ws[f"B{row}"] = report_name
        ws[f"C{row}"] = report_type
        ws[f"D{row}"] = frequency
        
        for col in range(2, 12):
            cell = ws.cell(row=row, column=col)
            if col > 4:  # Only highlight non-prepopulated columns
                cell.fill = styles["input"]["fill"]
            cell.border = get_border()
            cell.alignment = styles["normal"]["alignment"]
    
    # Add dropdowns
    add_dropdown(ws, "C6:C25", "report_type")
    add_dropdown(ws, "D6:D25", "frequency")
    add_dropdown(ws, "E6:E25", "generation_method")
    add_dropdown(ws, "G6:G25", "delivery_method")
    add_dropdown(ws, "J6:J25", "status")
    
    # --- Section B: Stakeholder Coverage ---
    row_b = 28
    ws[f"A{row_b}"] = "SECTION B: STAKEHOLDER REPORTING COVERAGE"
    ws[f"A{row_b}"].font = styles["section"]["font"]
    ws[f"A{row_b}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_b}:E{row_b}")
    
    coverage_headers = ["Stakeholder", "Required_Reports", "Reports_Received", 
                        "Coverage_%", "Notes"]
    row_b += 1
    for col_num, header in enumerate(coverage_headers, 1):
        cell = ws.cell(row=row_b, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.border = get_border()
    
    stakeholders = ["CISO", "IT Management", "Compliance Team", "SOC", 
                    "Internal Audit", "External Auditors", "HR", "Legal"]
    
    row_b += 1
    for stakeholder in stakeholders:
        ws[f"A{row_b}"] = stakeholder
        ws[f"A{row_b}"].font = Font(bold=True)
        ws[f"B{row_b}"].fill = styles["input"]["fill"]
        ws[f"C{row_b}"].fill = styles["input"]["fill"]
        ws[f"D{row_b}"] = '=IFERROR(C{0}/B{0},0)'.format(row_b)
        ws[f"D{row_b}"].number_format = "0%"
        ws[f"E{row_b}"].fill = styles["input"]["fill"]
        for col in ["A", "B", "C", "D", "E"]:
            ws[f"{col}{row_b}"].border = get_border()
        row_b += 1
    
    # --- Section C: Summary Metrics ---
    row_c = row_b + 2
    ws[f"A{row_c}"] = "SECTION C: SUMMARY METRICS"
    ws[f"A{row_c}"].font = styles["section"]["font"]
    ws[f"A{row_c}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_c}:D{row_c}")
    
    metrics = [
        ("Total reports configured:", '=COUNTA(B6:B25)'),
        ("Automated reports:", '=COUNTIF(E6:E25,"Automated")'),
        ("Reports implemented:", '=COUNTIF(J6:J25,"Implemented")'),
        ("Daily reports:", '=COUNTIF(D6:D25,"Daily")'),
        ("Stakeholders with full coverage:", '=COUNTIF(D30:D37,">=100%")'),
    ]
    
    row_c += 1
    for label, formula in metrics:
        ws[f"A{row_c}"] = label
        ws[f"A{row_c}"].font = styles["label"]["font"]
        ws[f"B{row_c}"] = formula
        ws[f"B{row_c}"].border = get_border()
        row_c += 1
    
    # Freeze panes
    ws.freeze_panes = "A6"
    
    return ws

# =============================================================================
# SECTION 10: SHEET 9 - GAP ANALYSIS
# =============================================================================

def create_sheet_gap_analysis(wb, styles):
    """Create Gap Analysis sheet."""
    ws = wb.create_sheet("Gap_Analysis")
    
    # Column widths
    col_widths = {
        "A": 14, "B": 18, "C": 40, "D": 30, "E": 30,
        "F": 14, "G": 25, "H": 35, "I": 20, "J": 14,
        "K": 15, "L": 12, "M": 15
    }
    for col, width in col_widths.items():
        ws.column_dimensions[col].width = width
    
    # --- Header ---
    ws.merge_cells("A1:M1")
    ws["A1"] = "GAP ANALYSIS - MONITORING & RESPONSE"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:M2")
    ws["A2"] = "Identify and prioritize monitoring and incident response gaps for remediation"
    ws["A2"].font = Font(italic=True, size=10)
    ws["A2"].alignment = Alignment(horizontal="center")
    
    # --- Gap Register ---
    ws["A4"] = "GAP REGISTER"
    ws["A4"].font = styles["section"]["font"]
    ws["A4"].fill = styles["section"]["fill"]
    ws.merge_cells("A4:M4")
    
    headers = [
        "Gap_ID", "Gap_Category", "Gap_Description", "Current_State",
        "Target_State", "Risk_Impact", "Affected_Systems", "Remediation_Action",
        "Owner", "Target_Date", "Status", "Priority", "Evidence_Ref"
    ]
    
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=5, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.alignment = styles["subheader"]["alignment"]
        cell.border = get_border()
    
    # Gap rows (30 gaps)
    for i in range(30):
        row = 6 + i
        ws[f"A{row}"] = f"GAP4-{i+1:03d}"
        ws[f"A{row}"].font = Font(bold=True)
        
        for col in range(2, 14):
            cell = ws.cell(row=row, column=col)
            cell.fill = styles["input"]["fill"]
            cell.border = get_border()
            cell.alignment = styles["normal"]["alignment"]
    
    # Add dropdowns
    add_dropdown(ws, "B6:B35", "gap_category")
    add_dropdown(ws, "F6:F35", "priority")  # Risk impact uses priority values
    add_dropdown(ws, "K6:K35", "gap_status")
    add_dropdown(ws, "L6:L35", "priority")
    
    # --- Summary Metrics ---
    row_sum = 38
    ws[f"A{row_sum}"] = "SUMMARY METRICS"
    ws[f"A{row_sum}"].font = styles["section"]["font"]
    ws[f"A{row_sum}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_sum}:D{row_sum}")
    
    metrics = [
        ("Total gaps identified:", '=COUNTA(C6:C35)'),
        ("Critical gaps:", '=COUNTIF(F6:F35,"Critical")'),
        ("High gaps:", '=COUNTIF(F6:F35,"High")'),
        ("Open gaps:", '=COUNTIF(K6:K35,"Open")'),
        ("In Progress gaps:", '=COUNTIF(K6:K35,"In_Progress")'),
        ("Resolved gaps:", '=COUNTIF(K6:K35,"Resolved")'),
        ("Gaps past target date:", '=COUNTIFS(K6:K35,"<>Resolved",J6:J35,"<"&TODAY())'),
    ]
    
    row_sum += 1
    for label, formula in metrics:
        ws[f"A{row_sum}"] = label
        ws[f"A{row_sum}"].font = styles["label"]["font"]
        ws[f"B{row_sum}"] = formula
        ws[f"B{row_sum}"].border = get_border()
        row_sum += 1
    
    # --- Gap Categories Breakdown ---
    row_cat = row_sum + 2
    ws[f"A{row_cat}"] = "GAP CATEGORIES BREAKDOWN"
    ws[f"A{row_cat}"].font = styles["section"]["font"]
    ws[f"A{row_cat}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_cat}:D{row_cat}")
    
    gap_cats = ["Logging", "Alerting", "Monitoring", "Incident_Response", 
                "Reporting", "Integration", "Retention", "Process"]
    
    row_cat += 1
    cat_headers = ["Category", "Count", "Open", "Critical/High"]
    for col_num, header in enumerate(cat_headers, 1):
        cell = ws.cell(row=row_cat, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.border = get_border()
    
    row_cat += 1
    for cat in gap_cats:
        ws[f"A{row_cat}"] = cat
        ws[f"B{row_cat}"] = f'=COUNTIF(B6:B35,"{cat}")'
        ws[f"C{row_cat}"] = f'=COUNTIFS(B6:B35,"{cat}",K6:K35,"Open")'
        ws[f"D{row_cat}"] = f'=COUNTIFS(B6:B35,"{cat}",F6:F35,"Critical")+COUNTIFS(B6:B35,"{cat}",F6:F35,"High")'
        for col in ["A", "B", "C", "D"]:
            ws[f"{col}{row_cat}"].border = get_border()
        row_cat += 1
    
    # Freeze panes
    ws.freeze_panes = "A6"
    
    return ws


# =============================================================================
# SECTION 11: SHEET 10 - EVIDENCE REGISTER
# =============================================================================

def create_sheet_evidence_register(wb, styles):
    """Create Evidence Register sheet with 100 rows."""
    ws = wb.create_sheet("Evidence_Register")
    
    # Column widths
    col_widths = {
        "A": 14, "B": 35, "C": 22, "D": 20, "E": 16,
        "F": 14, "G": 18, "H": 40, "I": 14, "J": 18, "K": 30
    }
    for col, width in col_widths.items():
        ws.column_dimensions[col].width = width
    
    # --- Header ---
    ws.merge_cells("A1:K1")
    ws["A1"] = "EVIDENCE REGISTER - MONITORING & RESPONSE"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:K2")
    ws["A2"] = "Catalog all evidence supporting monitoring and incident response assessment claims"
    ws["A2"].font = Font(italic=True, size=10)
    ws["A2"].alignment = Alignment(horizontal="center")
    
    # --- Evidence Catalog ---
    ws["A4"] = "EVIDENCE CATALOG"
    ws["A4"].font = styles["section"]["font"]
    ws["A4"].fill = styles["section"]["fill"]
    ws.merge_cells("A4:K4")
    
    headers = [
        "Evidence_ID", "Evidence_Title", "Evidence_Type", "Related_Sheet",
        "Related_Item_ID", "Date_Collected", "Collected_By", "Storage_Location",
        "Retention_Until", "Verification_Status", "Notes"
    ]
    
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=5, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.alignment = styles["subheader"]["alignment"]
        cell.border = get_border()
    
    # Evidence rows (100 rows)
    related_sheets = [
        "Log_Collection", "Alert_Configuration", "Monitoring_Dashboard",
        "Incident_Response", "Blocked_Events_Analysis", "False_Positive_Mgmt",
        "Reporting_Schedule", "Gap_Analysis"
    ]
    
    for i in range(100):
        row = 6 + i
        ws[f"A{row}"] = f"EV4-{i+1:03d}"
        ws[f"A{row}"].font = Font(bold=True)
        
        for col in range(2, 12):
            cell = ws.cell(row=row, column=col)
            cell.fill = styles["input"]["fill"]
            cell.border = get_border()
            cell.alignment = styles["normal"]["alignment"]
    
    # Add dropdowns
    add_dropdown(ws, "C6:C105", "evidence_type")
    
    # Related sheet dropdown
    dv_sheet = DataValidation(
        type="list",
        formula1=f'"{",".join(related_sheets)}"',
        allow_blank=True
    )
    ws.add_data_validation(dv_sheet)
    dv_sheet.add("D6:D105")
    
    add_dropdown(ws, "J6:J105", "verification_status")
    
    # --- Summary Metrics ---
    row_sum = 108
    ws[f"A{row_sum}"] = "EVIDENCE SUMMARY"
    ws[f"A{row_sum}"].font = styles["section"]["font"]
    ws[f"A{row_sum}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row_sum}:D{row_sum}")
    
    metrics = [
        ("Total evidence items:", '=COUNTA(B6:B105)'),
        ("Verified evidence:", '=COUNTIF(J6:J105,"Verified")'),
        ("Pending verification:", '=COUNTIF(J6:J105,"Pending")'),
        ("Evidence by Log_Collection:", '=COUNTIF(D6:D105,"Log_Collection")'),
        ("Evidence by Alert_Configuration:", '=COUNTIF(D6:D105,"Alert_Configuration")'),
        ("Evidence by Incident_Response:", '=COUNTIF(D6:D105,"Incident_Response")'),
    ]
    
    row_sum += 1
    for label, formula in metrics:
        ws[f"A{row_sum}"] = label
        ws[f"A{row_sum}"].font = styles["label"]["font"]
        ws[f"B{row_sum}"] = formula
        ws[f"B{row_sum}"].border = get_border()
        row_sum += 1
    
    # Freeze panes
    ws.freeze_panes = "A6"
    
    return ws


# =============================================================================
# SECTION 12: SHEET 11 - APPROVAL SIGN-OFF
# =============================================================================

def create_sheet_approval(wb, styles):
    """Create Approval Sign-Off sheet."""
    ws = wb.create_sheet("Approval_Sign_Off")
    
    # Column widths
    ws.column_dimensions["A"].width = 25
    ws.column_dimensions["B"].width = 30
    ws.column_dimensions["C"].width = 15
    ws.column_dimensions["D"].width = 25
    ws.column_dimensions["E"].width = 40
    
    # --- Header ---
    ws.merge_cells("A1:E1")
    ws["A1"] = "ASSESSMENT APPROVAL - MONITORING & RESPONSE"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:E2")
    ws["A2"] = "ISMS-IMP-A.8.23.4 - ISO/IEC 27001:2022 Control A.8.23"
    ws["A2"].font = Font(bold=True, size=11, color=COLORS["header_dark"])
    ws["A2"].alignment = Alignment(horizontal="center")
    
    # --- Assessment Summary ---
    ws["A4"] = "ASSESSMENT SUMMARY"
    ws["A4"].font = styles["section"]["font"]
    ws["A4"].fill = styles["section"]["fill"]
    ws.merge_cells("A4:E4")
    
    summary_items = [
        ("Assessment Date:", "=Instructions_Legend!B9"),
        ("Completed By:", "=Instructions_Legend!B10"),
        ("Organisation:", "=Instructions_Legend!B11"),
        ("Total Log Sources:", "=Log_Collection!B53"),
        ("Total Alert Rules:", "=Alert_Configuration!B64"),
        ("Total KPIs Tracked:", "=Monitoring_Dashboard!B73"),
        ("Open Incidents:", '=COUNTIF(Incident_Response!G40:G59,"No")'),
        ("Open False Positives:", "='False_Positive_Mgmt'!B63"),
        ("Open Gaps:", "=Gap_Analysis!B40"),
        ("Evidence Items:", "=Evidence_Register!B109"),
    ]
    
    row = 5
    for label, formula in summary_items:
        ws[f"A{row}"] = label
        ws[f"A{row}"].font = styles["label"]["font"]
        ws[f"B{row}"] = formula
        ws[f"B{row}"].border = get_border()
        row += 1
    
    # --- Approval Workflow ---
    row += 1
    ws[f"A{row}"] = "APPROVAL WORKFLOW"
    ws[f"A{row}"].font = styles["section"]["font"]
    ws[f"A{row}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row}:E{row}")
    
    approval_headers = ["Role", "Name", "Date", "Signature", "Comments"]
    row += 1
    for col_num, header in enumerate(approval_headers, 1):
        cell = ws.cell(row=row, column=col_num, value=header)
        cell.font = styles["subheader"]["font"]
        cell.fill = styles["subheader"]["fill"]
        cell.alignment = styles["subheader"]["alignment"]
        cell.border = get_border()
    
    approval_roles = [
        "Completed By (Assessor)",
        "Reviewed By (Security Manager)",
        "Approved By (CISO)",
    ]
    
    row += 1
    for role in approval_roles:
        ws[f"A{row}"] = role
        ws[f"A{row}"].font = Font(bold=True)
        for col in ["A", "B", "C", "D", "E"]:
            ws[f"{col}{row}"].border = get_border()
            if col != "A":
                ws[f"{col}{row}"].fill = styles["input"]["fill"]
        row += 1
    
    # --- Certification Statement ---
    row += 1
    ws[f"A{row}"] = "CERTIFICATION STATEMENT"
    ws[f"A{row}"].font = styles["section"]["font"]
    ws[f"A{row}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row}:E{row}")
    
    row += 1
    certification = (
        "This assessment accurately reflects the current state of web filtering "
        "monitoring, logging, alerting, and incident response capabilities. "
        "All findings have been verified against actual system configurations "
        "and operational evidence. Identified gaps have been documented with "
        "remediation plans and assigned to responsible owners."
    )
    ws.merge_cells(f"A{row}:E{row}")
    ws[f"A{row}"] = certification
    ws[f"A{row}"].alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[row].height = 60
    
    # --- Next Review ---
    row += 2
    ws[f"A{row}"] = "NEXT REVIEW"
    ws[f"A{row}"].font = styles["section"]["font"]
    ws[f"A{row}"].fill = styles["section"]["fill"]
    ws.merge_cells(f"A{row}:E{row}")
    
    row += 1
    ws[f"A{row}"] = "Scheduled Review Date:"
    ws[f"A{row}"].font = styles["label"]["font"]
    ws[f"B{row}"].fill = styles["input"]["fill"]
    ws[f"B{row}"].border = get_border()
    
    row += 1
    ws[f"A{row}"] = "Review Frequency:"
    ws[f"A{row}"].font = styles["label"]["font"]
    ws[f"B{row}"] = "Quarterly"
    ws[f"B{row}"].border = get_border()
    
    # --- Footer Quote ---
    row += 3
    ws[f"A{row}"] = "💡 Assessment Philosophy:"
    ws[f"A{row}"].font = Font(bold=True, italic=True, size=10)
    row += 1
    ws.merge_cells(f"A{row}:E{row}")
    ws[f"A{row}"] = '"Theater says \'we monitor.\' Engineering says \'we detected 47,392 blocked threats last quarter with 0.3% false positive rate and 15-minute average response time.\'"'
    ws[f"A{row}"].font = Font(italic=True, size=9)
    
    # Freeze panes
    ws.freeze_panes = "A4"
    
    return ws

# =============================================================================
# SECTION 13: MAIN FUNCTION AND EXECUTION
# =============================================================================

def generate_workbook():
    """
    Main function to generate the ISMS-IMP-A.8.23.4 workbook.
    
    Returns:
        str: Path to the generated workbook
    """
    logger.info("=" * 70)
    logger.info("ISMS-IMP-A.8.23.4 - Monitoring & Response Assessment Generator")
    logger.info("ISO/IEC 27001:2022 - Control A.8.23: Web Filtering")
    logger.info("=" * 70)
    logger.info("")
    
    # Create workbook
    logger.info("[1/12] Creating workbook...")
    wb = Workbook()
    styles = create_styles()
    
    # Generate sheets
    logger.info("[2/12] Creating Instructions & Legend sheet...")
    create_sheet_instructions(wb, styles)
    
    logger.info("[3/12] Creating Log Collection sheet...")
    create_sheet_log_collection(wb, styles)
    
    logger.info("[4/12] Creating Alert Configuration sheet...")
    create_sheet_alert_configuration(wb, styles)
    
    logger.info("[5/12] Creating Monitoring Dashboard sheet...")
    create_sheet_monitoring_dashboard(wb, styles)
    
    logger.info("[6/12] Creating Incident Response sheet...")
    create_sheet_incident_response(wb, styles)
    
    logger.info("[7/12] Creating Blocked Events Analysis sheet...")
    create_sheet_blocked_events(wb, styles)
    
    logger.info("[8/12] Creating False Positive Management sheet...")
    create_sheet_false_positive(wb, styles)
    
    logger.info("[9/12] Creating Reporting Schedule sheet...")
    create_sheet_reporting_schedule(wb, styles)
    
    logger.info("[10/12] Creating Gap Analysis sheet...")
    create_sheet_gap_analysis(wb, styles)
    
    logger.info("[11/12] Creating Evidence Register sheet...")
    create_sheet_evidence_register(wb, styles)
    
    logger.info("[12/12] Creating Approval Sign-Off sheet...")
    create_sheet_approval(wb, styles)
    
    # Generate filename with date
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"ISMS-IMP-A.8.23.4_Monitoring_Response_{date_str}.xlsx"
    
    # Save workbook
    logger.info("")
    logger.info(f"Saving workbook as: {filename}")
    wb.save(filename)
    
    # Print summary
    logger.info("")
    logger.info("=" * 70)
    logger.info("GENERATION COMPLETE")
    logger.info("=" * 70)
    logger.info("")
    logger.info(f"Output file: {filename}")
    logger.info(f"Total sheets: {len(wb.sheetnames)}")
    logger.info("")
    logger.info("Sheet Summary:")
    logger.info("-" * 40)
    for i, sheet in enumerate(wb.sheetnames, 1):
        logger.info(f"  {i:2}. {sheet}")
    logger.info("")
    logger.info("Key Capacities:")
    logger.info("-" * 40)
    logger.info("  \u2022 Log Sources: 30 rows")
    logger.info("  \u2022 Alert Rules: 40 rows")
    logger.info("  \u2022 Dashboards: 20 rows")
    logger.info("  \u2022 KPIs: 20 rows")
    logger.info("  \u2022 Incident Categories: 15 rows")
    logger.info("  \u2022 Recent Incidents: 20 rows")
    logger.info("  \u2022 Blocked Event Categories: 20 rows")
    logger.info("  \u2022 False Positives: 50 rows")
    logger.info("  \u2022 Reports: 20 rows")
    logger.info("  \u2022 Gaps: 30 rows")
    logger.info("  \u2022 Evidence: 100 rows")
    logger.info("")
    logger.info("Next Steps:")
    logger.info("-" * 40)
    logger.info("  1. Open the workbook in Excel")
    logger.info("  2. Complete each assessment sheet")
    logger.info("  3. Use dropdown menus for consistency")
    logger.info("  4. Document evidence for each item")
    logger.info("  5. Identify gaps and remediation plans")
    logger.info("  6. Obtain required approvals")
    logger.info("")
    logger.info("Remember: Evidence > Theater")
    logger.info("         'We monitor' means nothing without metrics.")
    logger.info("")
    
    return filename


def validate_workbook(filename):
    """
    Basic validation of generated workbook.
    
    Args:
        filename: Path to the workbook to validate
        
    Returns:
        bool: True if validation passes
    """
    from openpyxl import load_workbook
    
    logger.info("")
    logger.info("Running basic validation...")
    logger.info("-" * 40)
    
    try:
        wb = load_workbook(filename)
        
        expected_sheets = [
            "Instructions_Legend",
            "Log_Collection",
            "Alert_Configuration",
            "Monitoring_Dashboard",
            "Incident_Response",
            "Blocked_Events_Analysis",
            "False_Positive_Mgmt",
            "Reporting_Schedule",
            "Gap_Analysis",
            "Evidence_Register",
            "Approval_Sign_Off",
        ]
        
        # Check sheet count
        if len(wb.sheetnames) != 11:
            logger.info(f"  \u274C Expected 11 sheets, found {len(wb.sheetnames)}")
            return False
        logger.info(f"  \u2705 Sheet count: {len(wb.sheetnames)}")
        
        # Check sheet names
        for sheet in expected_sheets:
            if sheet in wb.sheetnames:
                logger.info(f"  \u2705 Found: {sheet}")
            else:
                logger.info(f"  \u274C Missing: {sheet}")
                return False
        
        # Check Evidence Register has 100 rows
        ev_sheet = wb["Evidence_Register"]
        ev_count = 0
        for row in range(6, 106):
            if ev_sheet[f"A{row}"].value:
                ev_count += 1
        
        if ev_count == 100:
            logger.info(f"  \u2705 Evidence Register: {ev_count} rows")
        else:
            logger.info(f"  \u26A0\uFE0F Evidence Register: {ev_count} rows (expected 100)")
        
        logger.info("")
        logger.info("Validation Result: \u2705 PASSED")
        logger.info("")
        
        wb.close()
        return True
        
    except Exception as e:
        logger.error(f"  \u274C Validation error: {str(e)}")
        return False


# =============================================================================
# SECTION 14: ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    """
    Entry point for script execution.
    
    Usage:
        python generate_a823_4_monitoring_response.py
        
    This will generate the assessment workbook in the current directory.
    """
    import sys
    
    logger.info("")
    logger.info("╔════════════════════════════════════════════════════════════════════╗")
    logger.info("║  ISMS Control A.8.23 - Web Filtering                               ║")
    logger.info("║  Domain 4: Monitoring & Response Assessment                        ║")
    logger.info("║                                                                    ║")
    logger.info("║  'The first principle is that you must not fool yourself'          ║")
    logger.info("║                                        - Richard Feynman           ║")
    logger.info("╚════════════════════════════════════════════════════════════════════╝")
    logger.info("")
    
    try:
        # Generate the workbook
        output_file = generate_workbook()
        
        # Validate the output
        if validate_workbook(output_file):
            logger.info(f"Successfully generated: {output_file}")
            sys.exit(0)
        else:
            logger.error("Validation failed - please check the output")
            sys.exit(1)
            
    except ImportError as e:
        logger.info("")
        logger.error("ERROR: Missing required library")
        logger.info("-" * 40)
        logger.info(f"  {str(e)}")
        logger.info("")
        logger.info("Please install openpyxl:")
        logger.info("  pip install openpyxl")
        logger.info("")
        sys.exit(1)
        
    except Exception as e:
        logger.info("")
        logger.error("ERROR: Generation failed")
        logger.info("-" * 40)
        logger.info(f"  {str(e)}")
        logger.info("")
        import traceback
        traceback.print_exc()
        sys.exit(1)


# =============================================================================
# END OF GENERATOR SCRIPT
# =============================================================================
#
# Document Control:
#   Version: 1.0
#   Created: 2025-01-01
#
# Change History:
#   1.0 - Initial version
#       - 11 sheets for monitoring & response assessment
#       - 100-row evidence register
#       - 3-level approval workflow
#       - Pre-populated incident categories, KPIs, and reports
#       - Comprehensive dropdown validations
#
# Dependencies:
#   - Python 3.7+
#   - openpyxl >= 3.0.0
#
# Output:
#   ISMS-IMP-A.8.23.4_Monitoring_Response_YYYYMMDD.xlsx
#

# =============================================================================
# QA_VERIFIED: 2026-01-31
# QA_STATUS: PASSED - STANDARDIZATION COMPLETE (Phase 1-3)
# QA_TOOL: Claude Code Standardization
# CHANGES: constants, metadata headers, v1.0 versioning, logger output
# =============================================================================
