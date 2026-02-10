#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
================================================================================
ISMS-IMP-A.8.30.2 - Contract Compliance
================================================================================

ISO/IEC 27001:2022 Control A.8.30: Outsourced Development
Assessment Domain 2 of 4: Contract Compliance

This script generates a comprehensive Excel assessment workbook for tracking
security clause inclusion in outsourced development contracts and monitoring
ongoing contract compliance.
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
DOCUMENT_ID = "ISMS-IMP-A.8.30.2"
WORKBOOK_NAME = "Contract Compliance"
CONTROL_ID = "A.8.30"
CONTROL_NAME = "Outsourced Development"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

# Timestamps
GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")

# Output filename
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

# =============================================================================
# UNICODE SYMBOLS
# =============================================================================
CHECK = "\u2705"
WARNING = "\u26a0\ufe0f"
XMARK = "\u274c"
DASH = "\u2014"

# =============================================================================
# STYLING CONSTANTS
# =============================================================================
HEADER_FONT = Font(bold=True, size=11, color="FFFFFF")
HEADER_FILL = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
HEADER_ALIGNMENT = Alignment(horizontal="center", vertical="center", wrap_text=True)
TITLE_FONT = Font(bold=True, size=14, color="FFFFFF", name="Calibri")

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
# WORKBOOK GENERATION FUNCTIONS
# =============================================================================

def create_instructions_sheet(ws):
    """Create the Instructions and Legend sheet."""
    ws.title = "Instructions"

    thin = Side(style="thin")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    # Header (Row 1) -- two-line merged header
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
        ("Related Policy:", "ISMS-POL-A.8.30"),
        ("Version:", "1.0"),
        ("Assessment Date:", ""),
        ("Completed By:", ""),
        ("Organisation:", ""),
        ("Review Cycle:", "Annually"),
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
        "1. Complete all assessment sheets in order, starting with Contract Inventory.",
        "2. For each contract, verify security clause inclusion in Security Clauses sheet.",
        "3. Track vulnerability remediation SLA compliance in SLA Compliance sheet.",
        "4. Record subcontractor authorisation requests in Subcontractor Approvals sheet.",
        "5. Complete termination checklist at contract closure.",
        "6. Record all supporting evidence in the Evidence Register sheet.",
        "7. Use the Summary Dashboard to track overall compliance status.",
        "8. All user-input cells are highlighted in yellow.",
        "9. Submit the completed workbook for review and approval via the Approval Sign-Off sheet.",
        "10. Retain this workbook as part of the ISMS evidence library.",
    ]

    for i, text in enumerate(instructions):
        ws[f"A{14 + i}"] = text

    # Acceptable Evidence
    ws["A25"] = "ACCEPTABLE EVIDENCE (examples)"
    ws["A25"].font = Font(bold=True, size=12)

    evidence_items = [
        "Executed outsourced development contracts with security clauses",
        "Security clause compliance checklists and review records",
        "Vulnerability remediation SLA tracking reports",
        "Subcontractor approval records and flow-down verification",
        "Contract termination security verification records",
        "Vendor security assessment reports",
    ]

    for i, item in enumerate(evidence_items):
        ws[f"A{26 + i}"] = f"{DASH} {item}"

    # Status Legend (Table Format)
    legend_row = 33
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

    # Column Widths & Freeze
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 45
    ws.column_dimensions["C"].width = 70
    ws.freeze_panes = "A4"


def create_contract_inventory_sheet(ws):
    """Create the Contract Inventory sheet."""
    ws.title = "Contract Inventory"

    headers = [
        "Contract_ID", "Vendor_ID", "Contract_Name", "Contract_Type",
        "Start_Date", "End_Date", "Project_Classification", "Contract_Value_CHF",
        "Primary_Contact", "Legal_Review_Date", "Security_Review_Date", "Status"
    ]

    # Title row (Row 1)
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "CONTRACT INVENTORY"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write column headers (Row 3)
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Add data validation dropdowns
    type_dv = DataValidation(type="list", formula1='"Fixed-price,T&M,Staff Aug,Managed Service"')
    ws.add_data_validation(type_dv)
    type_dv.add('D4:D102')

    class_dv = DataValidation(type="list", formula1='"Critical,High,Standard"')
    ws.add_data_validation(class_dv)
    class_dv.add('G4:G102')

    status_dv = DataValidation(type="list", formula1='"Active,Completed,Terminated"')
    ws.add_data_validation(status_dv)
    status_dv.add('L4:L102')

    # Format input rows
    for row in range(4, 23):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Set column widths
    widths = [12, 12, 35, 18, 12, 12, 18, 15, 25, 15, 18, 12]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_security_clauses_sheet(ws):
    """Create the Security Clauses Checklist sheet."""
    ws.title = "Security Clauses"

    headers = [
        "Contract_ID", "Clause_Category", "Clause_Description", "Included",
        "Clause_Reference", "Modification_Notes", "Reviewed_By", "Review_Date"
    ]

    # Title row (Row 1)
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "SECURITY CLAUSES CHECKLIST"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write column headers (Row 3)
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Standard security clauses
    clauses = [
        ("Secure Coding Standards", "Compliance with secure coding standards per ISMS-POL-A.8.28"),
        ("Security Policy Compliance", "Adherence to [Organisation] security policies"),
        ("Vulnerability Remediation SLAs", "Critical: 7 days, High: 30 days, Medium: 90 days, Low: 180 days"),
        ("Security Testing Rights", "Right to perform security testing on deliverables"),
        ("Audit Rights", "Right to audit vendor security practices"),
        ("Incident Notification", "24-hour notification requirement for security incidents"),
        ("Data Protection", "Confidentiality and data protection requirements"),
        ("Subcontractor Restrictions", "Prior written approval for subcontractors"),
        ("IP/Code Ownership", "Intellectual property and code ownership terms"),
        ("Source Code Escrow", "Escrow arrangement for critical applications"),
        ("Personnel Security", "Background checks and security training requirements"),
        ("Termination Security", "Data return/destruction and access revocation"),
        ("Insurance Requirements", "Cyber liability insurance minimums"),
        ("Liability Provisions", "Liability caps and indemnification"),
    ]

    row = 4
    for category, description in clauses:
        ws.cell(row=row, column=1, value="[Contract_ID]").fill = INPUT_FILL
        ws.cell(row=row, column=2, value=category)
        ws.cell(row=row, column=3, value=description)
        for col in range(4, 9):
            ws.cell(row=row, column=col).fill = INPUT_FILL
        for col in range(1, 9):
            ws.cell(row=row, column=col).border = THIN_BORDER
        row += 1

    # Data validation
    included_dv = DataValidation(type="list", formula1='"Yes,No,N/A,Modified"')
    ws.add_data_validation(included_dv)
    included_dv.add('D4:D102')

    # Column widths
    widths = [12, 25, 55, 12, 18, 35, 20, 12]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_sla_compliance_sheet(ws):
    """Create the SLA Compliance Tracking sheet."""
    ws.title = "SLA Compliance"

    headers = [
        "SLA_ID", "Contract_ID", "Vulnerability_ID", "Severity",
        "Discovery_Date", "SLA_Days", "SLA_Due_Date", "Remediation_Date",
        "SLA_Met", "Exception_Approved", "Exception_Approver", "Notes"
    ]

    # Title row (Row 1)
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "SLA COMPLIANCE TRACKING"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write column headers (Row 3)
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    severity_dv = DataValidation(type="list", formula1='"Critical,High,Medium,Low"')
    ws.add_data_validation(severity_dv)
    severity_dv.add('D4:D102')

    sla_days_dv = DataValidation(type="list", formula1='"7,30,90,180"')
    ws.add_data_validation(sla_days_dv)
    sla_days_dv.add('F4:F102')

    met_dv = DataValidation(type="list", formula1='"Met,Missed,Pending,Exception"')
    ws.add_data_validation(met_dv)
    met_dv.add('I4:I102')

    exception_dv = DataValidation(type="list", formula1='"Yes,No,N/A"')
    ws.add_data_validation(exception_dv)
    exception_dv.add('J4:J102')

    # Format input rows
    for row in range(4, 53):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Column widths
    widths = [12, 12, 18, 10, 15, 10, 15, 15, 12, 15, 25, 30]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_subcontractor_approvals_sheet(ws):
    """Create the Subcontractor Approvals sheet."""
    ws.title = "Subcontractor Approvals"

    headers = [
        "Approval_ID", "Contract_ID", "Primary_Vendor_ID", "Subcontractor_Name",
        "Subcontractor_Scope", "Access_Level", "Assessment_Level", "Risk_Classification",
        "Approval_Status", "Approved_By", "Approval_Date", "Expiry_Date",
        "Flow_Down_Verified", "Notes"
    ]

    # Title row (Row 1)
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "SUBCONTRACTOR APPROVALS"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write column headers (Row 3)
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    access_dv = DataValidation(type="list", formula1='"Direct,Via Vendor,None"')
    ws.add_data_validation(access_dv)
    access_dv.add('F4:F102')

    assess_dv = DataValidation(type="list", formula1='"Full,Abbreviated,Vendor Attested"')
    ws.add_data_validation(assess_dv)
    assess_dv.add('G4:G102')

    risk_dv = DataValidation(type="list", formula1='"High,Medium,Low"')
    ws.add_data_validation(risk_dv)
    risk_dv.add('H4:H102')

    status_dv = DataValidation(type="list", formula1='"Approved,Pending,Rejected"')
    ws.add_data_validation(status_dv)
    status_dv.add('I4:I102')

    yn_dv = DataValidation(type="list", formula1='"Yes,No"')
    ws.add_data_validation(yn_dv)
    yn_dv.add('M4:M102')

    # Format input rows
    for row in range(4, 23):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Column widths
    widths = [12, 12, 15, 30, 35, 12, 18, 18, 15, 20, 12, 12, 15, 30]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_termination_checklist_sheet(ws):
    """Create the Termination Checklist sheet."""
    ws.title = "Termination Checklist"

    headers = [
        "Contract_ID", "Termination_Type", "Termination_Date", "Check_Item",
        "Status", "Completion_Date", "Verified_By", "Evidence_Reference"
    ]

    # Title row (Row 1)
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "TERMINATION CHECKLIST"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write column headers (Row 3)
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Standard termination checklist items
    checklist_items = [
        "All access credentials revoked (within 24 hours)",
        "[Organisation] data returned or destroyed",
        "Destruction certificate received",
        "Source code transferred (if applicable)",
        "Documentation transferred",
        "Escrow arrangements verified",
        "Outstanding vulnerabilities addressed or risk accepted",
        "Final security review completed",
        "Lessons learned documented",
        "Vendor removed from active registry",
    ]

    row = 4
    for item in checklist_items:
        ws.cell(row=row, column=1, value="[Contract_ID]").fill = INPUT_FILL
        ws.cell(row=row, column=2).fill = INPUT_FILL
        ws.cell(row=row, column=3).fill = INPUT_FILL
        ws.cell(row=row, column=4, value=item)
        for col in range(5, 9):
            ws.cell(row=row, column=col).fill = INPUT_FILL
        for col in range(1, 9):
            ws.cell(row=row, column=col).border = THIN_BORDER
        row += 1

    # Data validation
    type_dv = DataValidation(type="list", formula1='"Completion,Early,Breach"')
    ws.add_data_validation(type_dv)
    type_dv.add('B4:B102')

    status_dv = DataValidation(type="list", formula1='"Complete,Pending,N/A"')
    ws.add_data_validation(status_dv)
    status_dv.add('E4:E102')

    # Column widths
    widths = [12, 15, 15, 50, 12, 15, 20, 35]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_summary_dashboard_sheet(ws):
    """Create the Summary Dashboard sheet."""
    ws.title = "Summary Dashboard"

    # Header (Row 1)
    ws.merge_cells("A1:G1")
    ws["A1"] = "CONTRACT COMPLIANCE - COMPLIANCE SUMMARY"
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
        cell.font = Font(bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.border = THIN_BORDER
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # Data rows -- one per assessment sheet
    areas = [
        "Contract Inventory",
        "Security Clauses",
        "SLA Compliance",
        "Subcontractor Approvals",
        "Termination Checklist",
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
    ws[f"A{metrics_start}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")

    metric_headers = ["Metric", "Value", "Target", "Status"]
    for col, header in enumerate(metric_headers, 1):
        cell = ws.cell(row=metrics_start + 1, column=col, value=header)
        cell.font = Font(bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.border = THIN_BORDER
        cell.alignment = Alignment(horizontal="center")

    metrics = [
        ("Security Clause Coverage", "[%]", "100%"),
        ("SLA Compliance Rate", "[%]", "95%"),
        ("Subcontractor Approval Rate", "[%]", "100%"),
        ("Termination Checklist Completion", "[%]", "100%"),
        ("Contract Review Timeliness", "[%]", "100%"),
        ("Flow-Down Clause Verification", "[%]", "100%"),
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
        cell.font = Font(bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.border = THIN_BORDER
        cell.alignment = Alignment(horizontal="center")

    findings = [
        ("Missing Security Clauses", "Contracts without mandatory clauses", "[#]", "Critical", "Immediate"),
        ("SLA Breaches", "Vulnerabilities exceeding remediation SLA", "[#]", "Critical", "Immediate"),
        ("Unapproved Subcontractors", "Subcontractors without prior approval", "[#]", "High", "Urgent"),
        ("Expired Contracts", "Active work on expired contracts", "[#]", "High", "Urgent"),
        ("Incomplete Terminations", "Contracts closed without full checklist", "[#]", "High", "Priority"),
        ("Missing Security Reviews", "Contracts without security review", "[#]", "Medium", "Plan"),
        ("Overdue Contract Reviews", "Reviews past due date", "[#]", "Medium", "Plan"),
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
    """Create the Evidence Register sheet -- standard 8-column format."""
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
    """Create the Approval Sign-Off sheet -- standard pattern."""
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
    create_contract_inventory_sheet(wb.create_sheet())
    create_security_clauses_sheet(wb.create_sheet())
    create_sla_compliance_sheet(wb.create_sheet())
    create_subcontractor_approvals_sheet(wb.create_sheet())
    create_termination_checklist_sheet(wb.create_sheet())
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
# QA_STATUS: PASSED - STANDARDISATION COMPLETE
# QA_TOOL: Claude Code Standardisation
# CHANGES: Unicode symbols added, Instructions sheet rewrite (two-line header,
#          doc info, legend table, freeze A4), Summary Dashboard (standard 3-table
#          pattern with 003366/4472C4/C00000 banners, TOTAL row, freeze A4),
#          Evidence Register (standard 8-col, EV-001..EV-100, gray 808080,
#          FFFFCC+border B-H, dropdowns C+H, freeze A5), Approval Sign-Off
#          (3-section standard, FINAL DECISION dropdown, NEXT REVIEW, freeze A3),
#          HEADER_FILL corrected 2F5496 -> 003366, traffic light fills added,
#          British English (organisation, authorisation)
# =============================================================================
