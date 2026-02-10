#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
================================================================================
ISMS-IMP-A.8.33-34.2 - Audit Activity Management Assessment
================================================================================

ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of
Information Systems During Audit Testing
Assessment Domain 2 of 3: Audit Activity Governance & System Protection

This script generates a comprehensive Excel assessment workbook for managing
audit testing governance including activity planning, tool authorization,
access control, disruption mitigation, and evidence protection.
================================================================================
"""

import logging
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

# =============================================================================
# LOGGING CONFIGURATION
# =============================================================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.8.33-34.2"
WORKBOOK_NAME = "Audit Activity Management Assessment"
CONTROL_ID = "A.8.33-34"
CONTROL_NAME = "Testing and Audit Protection"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

# Timestamps
GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")

# Output filename
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

# =============================================================================
# STYLING CONSTANTS
# =============================================================================
TITLE_FONT = Font(bold=True, size=14, color="FFFFFF", name="Calibri")
HEADER_FONT = Font(bold=True, size=11, color="FFFFFF")
HEADER_FILL = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
HEADER_ALIGNMENT = Alignment(horizontal="center", vertical="center", wrap_text=True)

SUBHEADER_FILL = PatternFill(start_color="D6DCE4", end_color="D6DCE4", fill_type="solid")
SUBHEADER_FONT = Font(bold=True, size=10)

INPUT_FILL = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
LOCKED_FILL = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")

GREEN_FILL = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
YELLOW_FILL = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
RED_FILL = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")

THIN_BORDER = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

# =============================================================================
# UNICODE SYMBOLS
# =============================================================================
CHECK = "\u2705"          # Green check
WARNING = "\u26A0\uFE0F"  # Warning triangle
XMARK = "\u274C"          # Red cross
DASH = "\u2014"           # Em dash


# =============================================================================
# WORKBOOK GENERATION FUNCTIONS
# =============================================================================

def create_instructions_sheet(ws):
    """Create the Instructions and Legend sheet."""
    ws.title = "Instructions & Legend"

    thin = Side(style="thin")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    # Header (Row 1) — two-line merged header
    ws.merge_cells("A1:G1")
    ws["A1"] = (
        f"{DOCUMENT_ID}  -  {WORKBOOK_NAME}\n"
        f"{CONTROL_REF}"
    )
    ws["A1"].font = Font(bold=True, size=14, color="FFFFFF")
    ws["A1"].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 40

    # Document Information (Row 3+)
    ws["A3"] = "Document Information"
    ws["A3"].font = Font(bold=True, size=12)

    doc_info = [
        ("Document ID:", DOCUMENT_ID),
        ("Assessment Area:", WORKBOOK_NAME),
        ("Related Policy:", "ISMS-POL-A.8.33-34"),
        ("Version:", "1.0"),
        ("Assessment Date:", ""),
        ("Completed By:", ""),
        ("Organisation:", ""),
        ("Review Cycle:", "Quarterly"),
    ]

    for i, (label, value) in enumerate(doc_info):
        row = 4 + i
        ws[f"A{row}"] = label
        ws[f"A{row}"].font = Font(bold=True)
        ws[f"B{row}"] = value
        if value == "":
            ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
            ws[f"B{row}"].border = border

    # Instructions Section
    ws["A13"] = "Instructions"
    ws["A13"].font = Font(bold=True, size=12)

    instructions = [
        "1. Complete all assessment sheets in order, starting with Audit Activity Register.",
        "2. For each item, evaluate current state against ISO 27001:2022 A.8.33/A.8.34 requirements.",
        "3. Record all supporting evidence in the Evidence Register sheet.",
        "4. Use the Summary Dashboard to track overall compliance status.",
        "5. All user-input cells are highlighted in yellow.",
        "6. Submit the completed workbook for review and approval via the Approval Sign-Off sheet.",
        "7. Retain this workbook as part of the ISMS evidence library.",
    ]

    for i, text in enumerate(instructions):
        ws[f"A{14 + i}"] = text

    # Acceptable Evidence
    ws["A22"] = "ACCEPTABLE EVIDENCE (examples)"
    ws["A22"].font = Font(bold=True, size=12)

    evidence_items = [
        "Audit activity authorisation and planning records",
        "Audit tool authorisation and configuration documentation",
        "Auditor access control logs and NDA records",
        "Disruption mitigation plans and risk assessments",
        "Audit evidence chain of custody documentation",
        "Compliance verification reports and attestations",
    ]

    for i, item in enumerate(evidence_items):
        ws[f"A{23 + i}"] = f"{DASH} {item}"

    # Status Legend (Table Format)
    legend_row = 30
    ws[f"A{legend_row}"] = "Status Legend"
    ws[f"A{legend_row}"].font = Font(bold=True, size=12)

    legend_headers = ["Symbol", "Status", "Description"]
    for col_idx, header in enumerate(legend_headers, start=1):
        cell = ws.cell(row=legend_row + 1, column=col_idx, value=header)
        cell.font = Font(bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.border = border

    legend_items = [
        (CHECK, "Compliant", "Requirement fully met with evidence"),
        (WARNING, "Partial", "Partially implemented, gaps identified"),
        (XMARK, "Non-Compliant", "Requirement not met, remediation needed"),
        (DASH, "N/A", "Not applicable to this organisation"),
    ]

    for i, (symbol, status, desc) in enumerate(legend_items):
        r = legend_row + 2 + i
        ws.cell(row=r, column=1, value=symbol).border = border
        ws.cell(row=r, column=2, value=status).border = border
        ws.cell(row=r, column=3, value=desc).border = border

    # Risk Level Scale
    scale_row = 37
    ws[f"A{scale_row}"] = "Risk Level Scale"
    ws[f"A{scale_row}"].font = Font(bold=True, size=12)

    scale_items = [
        "High - Could cause significant disruption or data exposure (CISO + Business Owner approval)",
        "Medium - Moderate risk to operations (IT Security Manager approval)",
        "Low - Minimal risk, standard tools (Security Team approval)",
    ]

    for i, item in enumerate(scale_items):
        ws[f"A{scale_row + 1 + i}"] = item

    # Column Widths & Freeze
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 45
    ws.column_dimensions["C"].width = 70
    ws.freeze_panes = "A4"


def create_audit_activity_register_sheet(ws):
    """Create the Audit Activity Register sheet."""
    ws.title = "Audit Activity Register"

    ws.merge_cells('A1:V1')
    title_cell = ws.cell(row=1, column=1, value="AUDIT ACTIVITY REGISTER")
    title_cell.font = TITLE_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = HEADER_ALIGNMENT
    ws.row_dimensions[1].height = 35

    ws.cell(row=2, column=1, value="Registry of all planned and completed audit activities")

    headers = [
        "Audit_ID", "Audit_Name", "Audit_Type", "Audit_Scope", "Audit_Firm_Team",
        "Lead_Auditor", "Planned_Start", "Planned_End", "Actual_Start", "Actual_End",
        "Audit_Status", "Management_Approval", "Approver", "Approval_Date",
        "Systems_in_Scope", "Data_Access_Required", "Testing_Type", "Findings_Count",
        "Critical_Findings", "Report_Location", "Follow_up_Status", "Notes"
    ]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    type_dv = DataValidation(type="list", formula1='"Internal,External-Financial,External-SOC2,Penetration Test,Vulnerability Assessment,Red Team,Regulatory,Compliance"')
    ws.add_data_validation(type_dv)
    type_dv.add('C5:C54')

    status_dv = DataValidation(type="list", formula1='"Planned,In Progress,Completed,Cancelled,On Hold"')
    ws.add_data_validation(status_dv)
    status_dv.add('K5:K54')

    approval_dv = DataValidation(type="list", formula1='"Approved,Pending,Not Required"')
    ws.add_data_validation(approval_dv)
    approval_dv.add('L5:L54')

    testing_dv = DataValidation(type="list", formula1='"Non-Invasive,Read-Only,Active Testing,Exploitation"')
    ws.add_data_validation(testing_dv)
    testing_dv.add('Q5:Q54')

    followup_dv = DataValidation(type="list", formula1='"Open,In Progress,Closed"')
    ws.add_data_validation(followup_dv)
    followup_dv.add('U5:U54')

    # Format input rows
    for row in range(5, 55):
        ws.cell(row=row, column=1, value=f"AUD-{str(row-4).zfill(3)}")
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Summary Statistics
    ws.cell(row=57, column=1, value="AUDIT STATISTICS").font = Font(bold=True, size=12)

    summary_items = [
        ("Total Audits", "=COUNTA(B5:B54)"),
        ("Planned Audits", '=COUNTIF(K5:K54,"Planned")'),
        ("In Progress", '=COUNTIF(K5:K54,"In Progress")'),
        ("Completed", '=COUNTIF(K5:K54,"Completed")'),
        ("Approved Audits", '=COUNTIF(L5:L54,"Approved")'),
        ("Pending Approval", '=COUNTIF(L5:L54,"Pending")'),
        ("Internal Audits", '=COUNTIF(C5:C54,"Internal")'),
        ("Penetration Tests", '=COUNTIF(C5:C54,"Penetration Test")'),
        ("Total Findings", "=SUM(R5:R54)"),
        ("Total Critical Findings", "=SUM(S5:S54)"),
        ("Open Follow-ups", '=COUNTIF(U5:U54,"Open")'),
    ]

    row = 59
    for label, formula in summary_items:
        ws.cell(row=row, column=1, value=label).border = THIN_BORDER
        ws.cell(row=row, column=2, value=formula).border = THIN_BORDER
        row += 1

    # Column widths
    widths = [12, 35, 25, 50, 30, 25, 12, 12, 12, 12, 18, 18, 25, 12, 40, 30, 25, 12, 12, 35, 18, 40]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_audit_tool_authorization_sheet(ws):
    """Create the Audit Tool Authorization sheet."""
    ws.title = "Audit Tool Authorisation"

    ws.merge_cells('A1:U1')
    title_cell = ws.cell(row=1, column=1, value="AUDIT TOOL AUTHORISATION")
    title_cell.font = TITLE_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = HEADER_ALIGNMENT
    ws.row_dimensions[1].height = 35

    ws.cell(row=2, column=1, value="Registry of authorised audit and testing tools")

    headers = [
        "Tool_ID", "Tool_Name", "Tool_Version", "Tool_Category", "Vendor_Source",
        "Tool_Owner", "Authorization_Status", "Authorization_Date", "Authorized_By",
        "Risk_Level", "Authorized_Use_Cases", "Restrictions", "Required_Approvals",
        "Storage_Location", "Access_Restricted_To", "Last_Security_Review",
        "Next_Review_Due", "Usage_Logging_Required", "License_Status",
        "License_Expiry", "Evidence_Reference"
    ]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    category_dv = DataValidation(type="list", formula1='"Vulnerability Scanner,Penetration Tool,Network Analyser,Web App Scanner,Forensic Tool,Credential Tester,Exploitation Framework,Other"')
    ws.add_data_validation(category_dv)
    category_dv.add('D5:D54')

    auth_dv = DataValidation(type="list", formula1='"Authorised,Pending,Unauthorised,Prohibited"')
    ws.add_data_validation(auth_dv)
    auth_dv.add('G5:G54')

    risk_dv = DataValidation(type="list", formula1='"High,Medium,Low"')
    ws.add_data_validation(risk_dv)
    risk_dv.add('J5:J54')

    yn_dv = DataValidation(type="list", formula1='"Yes,No"')
    ws.add_data_validation(yn_dv)
    yn_dv.add('R5:R54')

    license_dv = DataValidation(type="list", formula1='"Valid,Expired,N/A"')
    ws.add_data_validation(license_dv)
    license_dv.add('S5:S54')

    # Format input rows
    for row in range(5, 55):
        ws.cell(row=row, column=1, value=f"TOOL-{str(row-4).zfill(3)}")
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Summary Statistics
    ws.cell(row=57, column=1, value="TOOL RISK SUMMARY").font = Font(bold=True, size=12)

    summary_items = [
        ("Total Tools", "=COUNTA(B5:B54)"),
        ("Authorised Tools", '=COUNTIF(G5:G54,"Authorised")'),
        ("Pending Authorization", '=COUNTIF(G5:G54,"Pending")'),
        ("Unauthorised Tools", '=COUNTIF(G5:G54,"Unauthorised")'),
        ("Prohibited Tools", '=COUNTIF(G5:G54,"Prohibited")'),
        ("High Risk Tools", '=COUNTIF(J5:J54,"High")'),
        ("Medium Risk Tools", '=COUNTIF(J5:J54,"Medium")'),
        ("Low Risk Tools", '=COUNTIF(J5:J54,"Low")'),
        ("Expired Licenses", '=COUNTIF(S5:S54,"Expired")'),
    ]

    row = 59
    for label, formula in summary_items:
        ws.cell(row=row, column=1, value=label).border = THIN_BORDER
        ws.cell(row=row, column=2, value=formula).border = THIN_BORDER
        row += 1

    # Column widths
    widths = [12, 30, 15, 25, 25, 25, 18, 12, 25, 15, 50, 40, 30, 35, 30, 12, 12, 12, 18, 12, 20]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_audit_access_tracking_sheet(ws):
    """Create the Audit Access Tracking sheet."""
    ws.title = "Audit Access Tracking"

    ws.merge_cells('A1:W1')
    title_cell = ws.cell(row=1, column=1, value="AUDIT ACCESS TRACKING")
    title_cell.font = TITLE_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = HEADER_ALIGNMENT
    ws.row_dimensions[1].height = 35

    ws.cell(row=2, column=1, value="Registry of auditor access to systems and data")

    headers = [
        "Access_ID", "Auditor_Name", "Auditor_Organization", "Associated_Audit",
        "Access_Type", "Systems_Accessed", "Data_Classification_Accessed",
        "Access_Requested_Date", "Access_Start_Date", "Access_End_Date",
        "Actual_Revocation_Date", "Access_Status", "Approval_Status", "Approver",
        "Approval_Date", "Access_Logging_Enabled", "NDA_Signed", "NDA_Reference",
        "Supervision_Required", "Supervisor", "Multi_Factor_Auth_Required",
        "Revocation_Confirmation", "Notes"
    ]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    access_type_dv = DataValidation(type="list", formula1='"Read-Only,Read-Write,Admin,Physical,Remote-VPN"')
    ws.add_data_validation(access_type_dv)
    access_type_dv.add('E5:E104')

    classification_dv = DataValidation(type="list", formula1='"Public,Internal,Confidential,Restricted"')
    ws.add_data_validation(classification_dv)
    classification_dv.add('G5:G104')

    status_dv = DataValidation(type="list", formula1='"Active,Revoked,Expired"')
    ws.add_data_validation(status_dv)
    status_dv.add('L5:L104')

    approval_dv = DataValidation(type="list", formula1='"Approved,Pending,Denied"')
    ws.add_data_validation(approval_dv)
    approval_dv.add('M5:M104')

    ynp_dv = DataValidation(type="list", formula1='"Yes,Partial,No"')
    ws.add_data_validation(ynp_dv)
    ynp_dv.add('P5:P104')

    yn_dv = DataValidation(type="list", formula1='"Yes,No,N/A"')
    ws.add_data_validation(yn_dv)
    yn_dv.add('Q5:Q104')
    yn_dv.add('S5:S104')
    yn_dv.add('U5:U104')

    # Format input rows
    for row in range(5, 105):
        ws.cell(row=row, column=1, value=f"ACC-{str(row-4).zfill(3)}")
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Summary Statistics
    ws.cell(row=107, column=1, value="ACCESS STATISTICS").font = Font(bold=True, size=12)

    summary_items = [
        ("Total Access Grants", "=COUNTA(B5:B104)"),
        ("Active Access", '=COUNTIF(L5:L104,"Active")'),
        ("Revoked Access", '=COUNTIF(L5:L104,"Revoked")'),
        ("Expired Access", '=COUNTIF(L5:L104,"Expired")'),
        ("Approved Access", '=COUNTIF(M5:M104,"Approved")'),
        ("Pending Approval", '=COUNTIF(M5:M104,"Pending")'),
        ("Read-Only Access", '=COUNTIF(E5:E104,"Read-Only")'),
        ("Admin Access", '=COUNTIF(E5:E104,"Admin")'),
        ("Restricted Data Access", '=COUNTIF(G5:G104,"Restricted")'),
        ("NDA Coverage (Yes)", '=COUNTIF(Q5:Q104,"Yes")'),
        ("Access Logging (Yes)", '=COUNTIF(P5:P104,"Yes")'),
        ("MFA Required (Yes)", '=COUNTIF(U5:U104,"Yes")'),
    ]

    row = 109
    for label, formula in summary_items:
        ws.cell(row=row, column=1, value=label).border = THIN_BORDER
        ws.cell(row=row, column=2, value=formula).border = THIN_BORDER
        row += 1

    # Column widths
    widths = [12, 25, 25, 20, 20, 40, 18, 12, 12, 12, 12, 18, 18, 25, 12, 12, 12, 25, 12, 25, 12, 20, 40]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_disruption_mitigation_sheet(ws):
    """Create the Disruption Mitigation Plans sheet."""
    ws.title = "Disruption Mitigation Plans"

    ws.merge_cells('A1:W1')
    title_cell = ws.cell(row=1, column=1, value="DISRUPTION MITIGATION PLANS")
    title_cell.font = TITLE_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = HEADER_ALIGNMENT
    ws.row_dimensions[1].height = 35

    ws.cell(row=2, column=1, value="Protection measures for production systems during audit testing")

    headers = [
        "System_ID", "System_Name", "System_Criticality", "Business_Owner",
        "Technical_Owner", "Associated_Audits", "Primary_Mitigation_Strategy",
        "Testing_Restrictions", "Permitted_Testing_Window", "Maximum_Test_Duration",
        "Backup_Required_Before_Test", "Recovery_Point_Objective", "Recovery_Time_Objective",
        "Rollback_Procedure_Location", "Rollback_Last_Tested", "Escalation_Contact",
        "Escalation_Phone", "Secondary_Contact", "Monitoring_Enhancement",
        "Incident_Response_Plan", "Last_Mitigation_Review", "Review_Due_Date", "Evidence_Reference"
    ]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    criticality_dv = DataValidation(type="list", formula1='"Critical,High,Medium,Low"')
    ws.add_data_validation(criticality_dv)
    criticality_dv.add('C5:C54')

    strategy_dv = DataValidation(type="list", formula1='"Staging First,Off-Hours,Rate Limiting,Scope Exclusion,Enhanced Monitoring,Standby Recovery,Read-Only Only,Multi-Strategy"')
    ws.add_data_validation(strategy_dv)
    strategy_dv.add('G5:G54')

    backup_dv = DataValidation(type="list", formula1='"Yes,No,Already Scheduled"')
    ws.add_data_validation(backup_dv)
    backup_dv.add('K5:K54')

    # Format input rows
    for row in range(5, 55):
        ws.cell(row=row, column=1, value=f"SYS-{str(row-4).zfill(3)}")
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Summary Statistics
    ws.cell(row=57, column=1, value="MITIGATION STRATEGY SUMMARY").font = Font(bold=True, size=12)

    strategies = ["Staging First", "Off-Hours", "Rate Limiting", "Scope Exclusion", "Enhanced Monitoring", "Standby Recovery", "Read-Only Only", "Multi-Strategy"]
    row = 59
    for strategy in strategies:
        ws.cell(row=row, column=1, value=strategy).border = THIN_BORDER
        ws.cell(row=row, column=2, value=f'=COUNTIF(G5:G54,"{strategy}")').border = THIN_BORDER
        row += 1

    ws.cell(row=row + 1, column=1, value="SYSTEM COVERAGE STATISTICS").font = Font(bold=True, size=12)
    row += 3

    coverage_items = [
        ("Total Systems", "=COUNTA(B5:B54)"),
        ("Critical Systems", '=COUNTIF(C5:C54,"Critical")'),
        ("High Criticality", '=COUNTIF(C5:C54,"High")'),
        ("Medium Criticality", '=COUNTIF(C5:C54,"Medium")'),
        ("Low Criticality", '=COUNTIF(C5:C54,"Low")'),
        ("With Rollback Procedure", '=COUNTA(N5:N54)'),
        ("Backup Required", '=COUNTIF(K5:K54,"Yes")'),
    ]

    for label, formula in coverage_items:
        ws.cell(row=row, column=1, value=label).border = THIN_BORDER
        ws.cell(row=row, column=2, value=formula).border = THIN_BORDER
        row += 1

    # Column widths
    widths = [12, 30, 15, 25, 25, 30, 35, 50, 25, 15, 12, 15, 15, 35, 12, 25, 20, 25, 30, 35, 12, 12, 20]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_audit_evidence_protection_sheet(ws):
    """Create the Audit Evidence Protection sheet."""
    ws.title = "Audit Evidence Protection"

    ws.merge_cells('A1:W1')
    title_cell = ws.cell(row=1, column=1, value="AUDIT EVIDENCE PROTECTION")
    title_cell.font = TITLE_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = HEADER_ALIGNMENT
    ws.row_dimensions[1].height = 35

    ws.cell(row=2, column=1, value="Secure handling and retention of audit evidence")

    headers = [
        "Evidence_Category_ID", "Evidence_Category", "Evidence_Description",
        "Sensitivity_Classification", "Example_Documents", "Primary_Storage_Location",
        "Backup_Location", "Encryption_at_Rest", "Encryption_in_Transit",
        "Access_Control_Type", "Authorized_Accessors", "Retention_Period",
        "Retention_Start_Event", "Destruction_Method", "Destruction_Approval",
        "Chain_of_Custody_Required", "Chain_of_Custody_Process", "Legal_Hold_Applicable",
        "Legal_Hold_Contact", "Integrity_Verification", "Last_Access_Review",
        "Evidence_Owner", "Evidence_Reference"
    ]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    classification_dv = DataValidation(type="list", formula1='"Public,Internal,Confidential,Restricted"')
    ws.add_data_validation(classification_dv)
    classification_dv.add('D5:D34')

    enc_rest_dv = DataValidation(type="list", formula1='"AES-256,AES-128,BitLocker,None,Other"')
    ws.add_data_validation(enc_rest_dv)
    enc_rest_dv.add('H5:H34')

    enc_transit_dv = DataValidation(type="list", formula1='"TLS 1.3,TLS 1.2,VPN,None,Other"')
    ws.add_data_validation(enc_transit_dv)
    enc_transit_dv.add('I5:I34')

    access_dv = DataValidation(type="list", formula1='"RBAC,ACL,Individual Permissions,None"')
    ws.add_data_validation(access_dv)
    access_dv.add('J5:J34')

    retention_dv = DataValidation(type="list", formula1='"1 Year,2 Years,3 Years,5 Years,7 Years,Permanent,Legal Hold"')
    ws.add_data_validation(retention_dv)
    retention_dv.add('L5:L34')

    destruction_dv = DataValidation(type="list", formula1='"Secure Delete,Shredding,Degaussing,Certified Destruction"')
    ws.add_data_validation(destruction_dv)
    destruction_dv.add('N5:N34')

    yn_dv = DataValidation(type="list", formula1='"Yes,No"')
    ws.add_data_validation(yn_dv)
    yn_dv.add('P5:P34')

    legal_dv = DataValidation(type="list", formula1='"Yes,No,Potentially"')
    ws.add_data_validation(legal_dv)
    legal_dv.add('R5:R34')

    integrity_dv = DataValidation(type="list", formula1='"Hashing,Digital Signatures,Checksums,None"')
    ws.add_data_validation(integrity_dv)
    integrity_dv.add('T5:T34')

    # Pre-populate standard evidence categories
    categories = [
        ("EVCAT-001", "Penetration Test Reports", "Technical findings from pen tests", "Restricted"),
        ("EVCAT-002", "Vulnerability Scan Results", "Automated scanner outputs", "Confidential"),
        ("EVCAT-003", "Audit Workpapers", "Supporting audit documentation", "Confidential"),
        ("EVCAT-004", "System Configurations", "Captured configs during audit", "Confidential"),
        ("EVCAT-005", "Access Logs", "Records of auditor activity", "Internal"),
        ("EVCAT-006", "Interview Notes", "Documented conversations", "Confidential"),
        ("EVCAT-007", "Screenshots/Recordings", "Visual audit evidence", "Confidential"),
        ("EVCAT-008", "Final Audit Reports", "Published audit reports", "Confidential"),
        ("EVCAT-009", "Remediation Evidence", "Proof of fix implementation", "Internal"),
        ("EVCAT-010", "Management Response", "Management's reply to findings", "Internal"),
    ]

    for row_idx, (cat_id, cat_name, desc, classification) in enumerate(categories, 5):
        ws.cell(row=row_idx, column=1, value=cat_id)
        ws.cell(row=row_idx, column=2, value=cat_name)
        ws.cell(row=row_idx, column=3, value=desc)
        ws.cell(row=row_idx, column=4, value=classification)
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row_idx, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Additional empty rows
    for row in range(15, 35):
        ws.cell(row=row, column=1, value=f"EVCAT-{str(row-4).zfill(3)}")
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Summary Statistics
    ws.cell(row=37, column=1, value="PROTECTION STATISTICS").font = Font(bold=True, size=12)

    summary_items = [
        ("Total Evidence Categories", "=COUNTA(B5:B34)"),
        ("Restricted Categories", '=COUNTIF(D5:D34,"Restricted")'),
        ("Confidential Categories", '=COUNTIF(D5:D34,"Confidential")'),
        ("Encryption at Rest (AES-256)", '=COUNTIF(H5:H34,"AES-256")'),
        ("Encryption in Transit (TLS 1.3)", '=COUNTIF(I5:I34,"TLS 1.3")'),
        ("Chain of Custody Required", '=COUNTIF(P5:P34,"Yes")'),
        ("Legal Hold Applicable", '=COUNTIF(R5:R34,"Yes")'),
    ]

    row = 39
    for label, formula in summary_items:
        ws.cell(row=row, column=1, value=label).border = THIN_BORDER
        ws.cell(row=row, column=2, value=formula).border = THIN_BORDER
        row += 1

    # Column widths
    widths = [12, 30, 50, 18, 40, 35, 35, 18, 18, 25, 40, 18, 25, 25, 25, 12, 40, 12, 25, 25, 12, 25, 20]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_summary_dashboard_sheet(ws):
    """Create the Summary Dashboard sheet."""
    ws.title = "Summary Dashboard"

    # Header (Row 1)
    ws.merge_cells("A1:G1")
    ws["A1"] = "AUDIT ACTIVITY MANAGEMENT - COMPLIANCE SUMMARY"
    ws["A1"].font = Font(bold=True, size=14, color="FFFFFF")
    ws["A1"].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # TABLE 1: Compliance Summary
    ws.merge_cells("A2:G2")
    ws["A2"] = "TABLE 1: ASSESSMENT AREA COMPLIANCE OVERVIEW"
    ws["A2"].font = Font(bold=True, size=11, color="FFFFFF")
    ws["A2"].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")

    # Column Headers (Row 3)
    headers = ["Assessment Area", "Total Items", "Compliant", "Partial",
               "Non-Compliant", "N/A", "Compliance %"]
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.border = THIN_BORDER
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # Data rows — one per assessment sheet
    areas = [
        "Audit Activity Register",
        "Audit Tool Authorisation",
        "Audit Access Tracking",
        "Disruption Mitigation Plans",
        "Audit Evidence Protection",
    ]

    for i, area in enumerate(areas):
        row = 4 + i
        ws.cell(row=row, column=1, value=area).border = THIN_BORDER
        for col in range(2, 8):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER
            cell.alignment = Alignment(horizontal="center")

    # TOTAL row
    total_row = 4 + len(areas)
    ws.cell(row=total_row, column=1, value="TOTAL").font = Font(bold=True)
    ws.cell(row=total_row, column=1).border = THIN_BORDER
    for col in range(2, 7):
        cell = ws.cell(row=total_row, column=col)
        cell.value = f"=SUM({get_column_letter(col)}4:{get_column_letter(col)}{total_row - 1})"
        cell.font = Font(bold=True)
        cell.border = THIN_BORDER
        cell.alignment = Alignment(horizontal="center")
    # Compliance % formula
    cell = ws.cell(row=total_row, column=7)
    cell.value = f'=IF((B{total_row}-F{total_row})=0,"0%",ROUND(C{total_row}/(B{total_row}-F{total_row})*100,1)&"%")'
    cell.font = Font(bold=True, color="0000FF", size=12)
    cell.border = THIN_BORDER
    cell.alignment = Alignment(horizontal="center")

    # TABLE 2: Key Metrics
    metrics_start = total_row + 2
    ws.merge_cells(f"A{metrics_start}:G{metrics_start}")
    ws[f"A{metrics_start}"] = "TABLE 2: KEY METRICS"
    ws[f"A{metrics_start}"].font = Font(bold=True, size=11, color="FFFFFF")
    ws[f"A{metrics_start}"].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")

    metric_headers = ["Metric", "Value", "Target", "Status"]
    for col, header in enumerate(metric_headers, 1):
        cell = ws.cell(row=metrics_start + 1, column=col, value=header)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.border = THIN_BORDER
        cell.alignment = Alignment(horizontal="center")

    metrics = [
        ("Audit Authorisation Rate", "[%]", "100%"),
        ("Tool Authorisation Rate", "[%]", "100%"),
        ("Access Approval Rate", "[%]", "100%"),
        ("Access Revocation Timeliness", "[%]", "100%"),
        ("NDA Coverage", "[%]", "100%"),
        ("Access Logging Coverage", "[%]", "100%"),
        ("Critical System Mitigation Coverage", "[%]", "100%"),
        ("Evidence Encryption Rate", "[%]", "100%"),
    ]

    row = metrics_start + 2
    for metric, value, target in metrics:
        ws.cell(row=row, column=1, value=metric).border = THIN_BORDER
        cell_val = ws.cell(row=row, column=2, value=value)
        cell_val.fill = INPUT_FILL
        cell_val.border = THIN_BORDER
        ws.cell(row=row, column=3, value=target).border = THIN_BORDER
        cell_status = ws.cell(row=row, column=4)
        cell_status.fill = INPUT_FILL
        cell_status.border = THIN_BORDER
        row += 1

    status_dv = DataValidation(type="list", formula1='"Compliant,Partial,Non-Compliant"')
    ws.add_data_validation(status_dv)
    status_dv.add(f"D{metrics_start + 2}:D{row - 1}")

    # TABLE 3: Critical Findings
    crit_start = row + 1
    ws.merge_cells(f"A{crit_start}:G{crit_start}")
    ws[f"A{crit_start}"] = "TABLE 3: CRITICAL FINDINGS REQUIRING IMMEDIATE ATTENTION"
    ws[f"A{crit_start}"].font = Font(bold=True, size=11, color="FFFFFF")
    ws[f"A{crit_start}"].fill = PatternFill(start_color="C00000", end_color="C00000", fill_type="solid")

    findings_headers = ["Category", "Finding", "Count", "Severity", "Action Required"]
    for col, header in enumerate(findings_headers, 1):
        cell = ws.cell(row=crit_start + 1, column=col, value=header)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.border = THIN_BORDER
        cell.alignment = Alignment(horizontal="center")

    findings = [
        ("Unauthorised Audits", "Audits without approval", "[#]", "Critical", "Immediate"),
        ("Unauthorised Tools", "Tools without authorisation", "[#]", "Critical", "Immediate"),
        ("Unapproved Access", "Auditor access without approval", "[#]", "High", "Urgent"),
        ("Active Access Past End Date", "Access not revoked", "[#]", "High", "Urgent"),
        ("Missing Mitigation Plans", "Critical systems without plans", "[#]", "High", "Priority"),
        ("Unencrypted Evidence", "Sensitive evidence unprotected", "[#]", "Medium", "Plan"),
        ("Overdue Reviews", "Reviews past due", "[#]", "Medium", "Plan"),
    ]

    row = crit_start + 2
    for cat, finding, count, severity, action in findings:
        ws.cell(row=row, column=1, value=cat).border = THIN_BORDER
        ws.cell(row=row, column=2, value=finding).border = THIN_BORDER
        cell_count = ws.cell(row=row, column=3, value=count)
        cell_count.fill = INPUT_FILL
        cell_count.border = THIN_BORDER
        ws.cell(row=row, column=4, value=severity).border = THIN_BORDER
        ws.cell(row=row, column=5, value=action).border = THIN_BORDER
        row += 1

    # Column widths & freeze
    ws.column_dimensions["A"].width = 40
    ws.column_dimensions["B"].width = 16
    ws.column_dimensions["C"].width = 16
    ws.column_dimensions["D"].width = 18
    ws.column_dimensions["E"].width = 18
    ws.column_dimensions["F"].width = 12
    ws.column_dimensions["G"].width = 15
    ws.freeze_panes = "A4"


def create_evidence_register_sheet(ws):
    """Create the Evidence Register sheet — standard 8-column format."""
    ws.title = "Evidence Register"

    thin = Side(style="thin")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    # Header (Row 1)
    ws.merge_cells("A1:H1")
    ws["A1"] = "EVIDENCE REGISTER"
    ws["A1"].font = Font(bold=True, size=14, color="FFFFFF")
    ws["A1"].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Subtitle (Row 2)
    ws.merge_cells("A2:H2")
    ws["A2"] = "List all evidence files/documents referenced in this assessment (audit traceability)."
    ws["A2"].font = Font(italic=True)
    ws["A2"].alignment = Alignment(horizontal="left", vertical="center")

    # Column Headers (Row 4)
    headers = [
        ("Evidence ID", 15),
        ("Assessment Area", 25),
        ("Evidence Type", 22),
        ("Description", 40),
        ("Location/Path", 45),
        ("Date Collected", 16),
        ("Collected By", 20),
        ("Verification Status", 22),
    ]

    for col, (header, width) in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col, value=header)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.border = border
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws.column_dimensions[get_column_letter(col)].width = width

    # Data validations
    type_dv = DataValidation(
        type="list",
        formula1='"Configuration file,Screenshot,Network scan,Documentation,Vendor spec,Certificate inventory,Audit log,Compliance report,Other"',
        allow_blank=True,
    )
    ws.add_data_validation(type_dv)
    type_dv.add("C5:C104")

    status_dv = DataValidation(
        type="list",
        formula1='"Verified,Pending verification,Not verified,Requires update"',
        allow_blank=True,
    )
    ws.add_data_validation(status_dv)
    status_dv.add("H5:H104")

    # Data rows (5-104, 100 rows)
    for r in range(5, 105):
        ws.cell(row=r, column=1, value=f"EV-{r - 4:03d}").font = Font(color="808080")
        for c in range(2, 9):
            cell = ws.cell(row=r, column=c)
            cell.fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
            cell.border = border

    # Freeze
    ws.freeze_panes = "A5"


def create_approval_sign_off_sheet(ws):
    """Create the Approval Sign-Off sheet — standard pattern."""
    ws.title = "Approval Sign-Off"

    thin = Side(style="thin")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    # Header (Row 1)
    ws.merge_cells("A1:E1")
    ws["A1"] = "ASSESSMENT APPROVAL AND SIGN-OFF"
    ws["A1"].font = Font(bold=True, size=14, color="FFFFFF")
    ws["A1"].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # ASSESSMENT SUMMARY banner (Row 3)
    row = 3
    ws.merge_cells(f"A{row}:E{row}")
    ws[f"A{row}"] = "ASSESSMENT SUMMARY"
    ws[f"A{row}"].font = Font(bold=True, size=11, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")

    # Summary fields
    summary_fields = [
        ("Document:", f"{DOCUMENT_ID} - {WORKBOOK_NAME}"),
        ("Assessment Period:", ""),
        ("Overall Compliance:", ""),
        ("Assessment Status:", ""),
    ]

    row = 4
    for label, value in summary_fields:
        ws[f"A{row}"] = label
        ws[f"A{row}"].font = Font(bold=True)
        ws.merge_cells(f"B{row}:E{row}")
        ws[f"B{row}"] = value
        if value == "":
            ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
            ws[f"B{row}"].border = border
        row += 1

    # Status dropdown on Assessment Status
    status_dv = DataValidation(
        type="list",
        formula1='"Draft,Final,Requires remediation,Re-assessment required"',
        allow_blank=True,
    )
    ws.add_data_validation(status_dv)
    status_dv.add(f"B{row - 1}")

    # 3 Approver sections
    approvers = [
        ("COMPLETED BY (ASSESSOR)", "4472C4"),
        ("REVIEWED BY (INFORMATION SECURITY OFFICER)", "4472C4"),
        ("APPROVED BY (CISO)", "003366"),
    ]

    row += 2  # gap before first approver
    for title, color in approvers:
        # Banner
        ws.merge_cells(f"A{row}:E{row}")
        ws[f"A{row}"] = title
        ws[f"A{row}"].font = Font(bold=True, color="FFFFFF", size=11)
        ws[f"A{row}"].fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
        row += 1

        # 5 fields per approver
        for field in ["Name:", "Title:", "Date:", "Signature:", "Comments:"]:
            ws[f"A{row}"] = field
            ws[f"A{row}"].font = Font(bold=True)
            ws.merge_cells(f"B{row}:E{row}")
            ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
            ws[f"B{row}"].border = border
            row += 1
        row += 1  # gap between sections

    # FINAL DECISION
    ws[f"A{row}"] = "FINAL DECISION:"
    ws[f"A{row}"].font = Font(bold=True)
    ws.merge_cells(f"B{row}:E{row}")
    ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
    ws[f"B{row}"].border = border

    dv_dec = DataValidation(
        type="list",
        formula1='"Approved,Approved with Conditions,Rejected,Deferred"',
        allow_blank=True,
    )
    ws.add_data_validation(dv_dec)
    dv_dec.add(f"B{row}")

    # NEXT REVIEW DETAILS
    row += 3
    ws.merge_cells(f"A{row}:E{row}")
    ws[f"A{row}"] = "NEXT REVIEW DETAILS"
    ws[f"A{row}"].font = Font(bold=True, size=11, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")

    row += 1
    for label in ["Next Review Date:", "Review Responsible:", "Special Considerations:"]:
        ws[f"A{row}"] = label
        ws[f"A{row}"].font = Font(bold=True)
        ws.merge_cells(f"B{row}:E{row}")
        ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        ws[f"B{row}"].border = border
        row += 1

    # Column widths & freeze
    ws.column_dimensions["A"].width = 32
    ws.column_dimensions["B"].width = 25
    ws.column_dimensions["C"].width = 20
    ws.column_dimensions["D"].width = 20
    ws.column_dimensions["E"].width = 20
    ws.freeze_panes = "A3"


def generate_workbook():
    """Generate the complete assessment workbook."""
    logger.info(f"Generating {DOCUMENT_ID} - {WORKBOOK_NAME}")

    wb = Workbook()

    # Remove default sheet
    default_sheet = wb.active

    # Create all sheets
    create_instructions_sheet(wb.create_sheet())
    create_audit_activity_register_sheet(wb.create_sheet())
    create_audit_tool_authorization_sheet(wb.create_sheet())
    create_audit_access_tracking_sheet(wb.create_sheet())
    create_disruption_mitigation_sheet(wb.create_sheet())
    create_audit_evidence_protection_sheet(wb.create_sheet())
    create_summary_dashboard_sheet(wb.create_sheet())
    create_evidence_register_sheet(wb.create_sheet())
    create_approval_sign_off_sheet(wb.create_sheet())

    # Remove default sheet
    wb.remove(default_sheet)

    # Save workbook
    wb.save(OUTPUT_FILENAME)
    logger.info(f"Workbook saved: {OUTPUT_FILENAME}")

    return OUTPUT_FILENAME


# =============================================================================
# MAIN EXECUTION
# =============================================================================
if __name__ == "__main__":
    generate_workbook()

# =============================================================================
# QA_VERIFIED: 2026-02-10
# QA_STATUS: PASSED - COMMON SHEET STANDARDISATION
# QA_TOOL: Claude Code Standardisation
# CHANGES: Instructions rewrite (two-line header, doc info, legend table),
#          Summary Dashboard (standard TABLE banners, TOTAL row, freeze A4),
#          Evidence Register (standard 8-col, subtitle row 2, freeze A5),
#          Approval Sign-Off (3-section standard, FINAL DECISION, NEXT REVIEW),
#          Assessment sheet headers (blue text → white-on-blue fill, row height 35),
#          Sheet tab names (underscores → spaces), Unicode symbols added,
#          British English (authorisation)
# =============================================================================
