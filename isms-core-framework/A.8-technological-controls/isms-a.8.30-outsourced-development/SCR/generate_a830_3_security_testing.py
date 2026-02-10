#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
================================================================================
ISMS-IMP-A.8.30.3 - Security Testing and Acceptance
================================================================================

ISO/IEC 27001:2022 Control A.8.30: Outsourced Development
Assessment Domain 3 of 4: Security Testing and Acceptance

This script generates a comprehensive Excel assessment workbook for tracking
security testing activities and acceptance criteria for outsourced development
deliverables.
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
DOCUMENT_ID = "ISMS-IMP-A.8.30.3"
WORKBOOK_NAME = "Security Testing and Acceptance"
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
TITLE_FONT = Font(bold=True, size=14, color="FFFFFF", name="Calibri")
HEADER_FILL = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
HEADER_ALIGNMENT = Alignment(horizontal="center", vertical="center", wrap_text=True)

SUBHEADER_FILL = PatternFill(start_color="D6DCE4", end_color="D6DCE4", fill_type="solid")
SUBHEADER_FONT = Font(bold=True, size=10)

INPUT_FILL = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
LOCKED_FILL = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")

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
        "1. Complete all assessment sheets in order, starting with Deliverable Inventory.",
        "2. Track code review results for each deliverable in Code Review Tracking.",
        "3. Record SAST, DAST, SCA, and penetration test results in Security Testing.",
        "4. Maintain SBOM records for all deliverables in SBOM Management.",
        "5. Verify acceptance criteria and obtain sign-off in Acceptance Sign-off.",
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
        "SAST and DAST scan reports with finding classifications",
        "Code review records and approval documentation",
        "Software Bill of Materials (SBOM) export files",
        "Penetration test reports for critical projects",
        "Acceptance criteria verification and sign-off records",
        "Remediation tracking reports and retest evidence",
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


def create_deliverable_inventory_sheet(ws):
    """Create the Deliverable Inventory sheet."""
    ws.title = "Deliverable Inventory"

    headers = [
        "Deliverable_ID", "Contract_ID", "Vendor_ID", "Deliverable_Name",
        "Deliverable_Type", "Project_Classification", "Planned_Delivery",
        "Actual_Delivery", "Code_Review_Status", "Security_Test_Status",
        "SBOM_Received", "Acceptance_Status", "Acceptance_Date", "Accepted_By"
    ]

    # Title row
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "DELIVERABLE INVENTORY"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write headers in row 3
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    type_dv = DataValidation(type="list", formula1='"Application,Module,Component,Library,API"')
    ws.add_data_validation(type_dv)
    type_dv.add('E4:E102')

    class_dv = DataValidation(type="list", formula1='"Critical,High,Standard"')
    ws.add_data_validation(class_dv)
    class_dv.add('F4:F102')

    review_dv = DataValidation(type="list", formula1='"Pending,In Progress,Complete,N/A"')
    ws.add_data_validation(review_dv)
    review_dv.add('I4:I102')

    test_dv = DataValidation(type="list", formula1='"Pending,In Progress,Complete"')
    ws.add_data_validation(test_dv)
    test_dv.add('J4:J102')

    sbom_dv = DataValidation(type="list", formula1='"Yes,No,N/A"')
    ws.add_data_validation(sbom_dv)
    sbom_dv.add('K4:K102')

    accept_dv = DataValidation(type="list", formula1='"Pending,Accepted,Rejected,Conditional"')
    ws.add_data_validation(accept_dv)
    accept_dv.add('L4:L102')

    # Format input rows
    for row in range(4, 53):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Set column widths
    widths = [15, 12, 12, 35, 15, 18, 15, 15, 18, 18, 15, 15, 15, 20]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_code_review_sheet(ws):
    """Create the Code Review Tracking sheet."""
    ws.title = "Code Review Tracking"

    headers = [
        "Review_ID", "Deliverable_ID", "Review_Type", "Review_Date",
        "Reviewer", "Reviewer_Role", "Files_Reviewed", "Security_Findings",
        "Critical_Findings", "High_Findings", "Medium_Findings", "Low_Findings",
        "Review_Result", "Findings_Reference", "Notes"
    ]

    # Title row
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "CODE REVIEW TRACKING"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write headers in row 3
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    type_dv = DataValidation(type="list", formula1='"Peer Review,Security Review,Architecture Review"')
    ws.add_data_validation(type_dv)
    type_dv.add('C4:C102')

    role_dv = DataValidation(type="list", formula1='"Developer,Security Team,Security Architect"')
    ws.add_data_validation(role_dv)
    role_dv.add('F4:F102')

    result_dv = DataValidation(type="list", formula1='"Approved,Approved with Findings,Rejected"')
    ws.add_data_validation(result_dv)
    result_dv.add('M4:M102')

    # Format input rows
    for row in range(4, 53):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Column widths
    widths = [12, 15, 18, 12, 20, 18, 15, 15, 15, 12, 15, 12, 20, 35, 30]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_security_testing_sheet(ws):
    """Create the Security Testing Results sheet."""
    ws.title = "Security Testing"

    headers = [
        "Test_ID", "Deliverable_ID", "Test_Type", "Test_Tool", "Test_Date",
        "Tester", "Scope", "Total_Findings", "Critical_Findings", "High_Findings",
        "Medium_Findings", "Low_Findings", "False_Positives", "Findings_Remediated",
        "Findings_Outstanding", "Report_Reference", "Retest_Required",
        "Retest_Date", "Retest_Status"
    ]

    # Title row
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "SECURITY TESTING"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write headers in row 3
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    type_dv = DataValidation(type="list", formula1='"SAST,DAST,SCA,Penetration Test,Manual Review"')
    ws.add_data_validation(type_dv)
    type_dv.add('C4:C102')

    retest_dv = DataValidation(type="list", formula1='"Yes,No"')
    ws.add_data_validation(retest_dv)
    retest_dv.add('Q4:Q102')

    retest_status_dv = DataValidation(type="list", formula1='"Pending,Passed,Failed,N/A"')
    ws.add_data_validation(retest_status_dv)
    retest_status_dv.add('S4:S102')

    # Format input rows
    for row in range(4, 53):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Column widths
    widths = [10, 15, 15, 20, 12, 20, 30, 12, 12, 12, 12, 10, 12, 15, 15, 35, 12, 12, 12]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_sbom_management_sheet(ws):
    """Create the SBOM Management sheet."""
    ws.title = "SBOM Management"

    headers = [
        "SBOM_ID", "Deliverable_ID", "SBOM_Format", "SBOM_Date",
        "Total_Components", "Direct_Dependencies", "Transitive_Dependencies",
        "Known_Vulnerabilities", "Critical_Vulns", "High_Vulns",
        "License_Issues", "Outdated_Components", "Review_Status",
        "Reviewed_By", "Review_Date", "SBOM_Reference", "Action_Plan"
    ]

    # Title row
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "SBOM MANAGEMENT"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write headers in row 3
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    format_dv = DataValidation(type="list", formula1='"CycloneDX,SPDX,Spreadsheet,Other"')
    ws.add_data_validation(format_dv)
    format_dv.add('C4:C102')

    status_dv = DataValidation(type="list", formula1='"Pending,Reviewed,Accepted,Rejected"')
    ws.add_data_validation(status_dv)
    status_dv.add('M4:M102')

    # Format input rows
    for row in range(4, 53):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Column widths
    widths = [12, 15, 12, 12, 15, 18, 20, 18, 12, 12, 12, 18, 12, 20, 12, 35, 40]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_acceptance_signoff_sheet(ws):
    """Create the Acceptance Sign-off domain sheet."""
    ws.title = "Acceptance Sign-off"

    headers = [
        "Acceptance_ID", "Deliverable_ID", "Criteria_Category", "Acceptance_Criteria",
        "Status", "Evidence_Reference", "Verified_By", "Verification_Date",
        "Waiver_Reason", "Waiver_Approver"
    ]

    # Title row
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "ACCEPTANCE SIGN-OFF"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write headers in row 3
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Standard acceptance criteria
    criteria = [
        ("Security", "Code review completed with no unresolved Critical/High findings"),
        ("Security", "SAST scan completed with no unresolved Critical/High findings"),
        ("Security", "SCA scan completed with no Critical/High vulnerable dependencies"),
        ("Security", "DAST scan completed (for web applications)"),
        ("Security", "Penetration test passed (for Critical projects)"),
        ("Security", "SBOM received and reviewed"),
        ("Security", "No secrets detected in codebase"),
        ("Documentation", "Security documentation complete"),
        ("Compliance", "Vulnerability remediation SLAs met"),
        ("Compliance", "Security training completed by all developers"),
    ]

    row = 4
    for category, criterion in criteria:
        ws.cell(row=row, column=1, value=f"ACC-{row-3:04d}").fill = INPUT_FILL
        ws.cell(row=row, column=2, value="[Deliverable_ID]").fill = INPUT_FILL
        ws.cell(row=row, column=3, value=category)
        ws.cell(row=row, column=4, value=criterion)
        for col in range(5, 11):
            ws.cell(row=row, column=col).fill = INPUT_FILL
        for col in range(1, 11):
            ws.cell(row=row, column=col).border = THIN_BORDER
        row += 1

    # Data validation
    category_dv = DataValidation(type="list", formula1='"Functional,Security,Performance,Documentation,Compliance"')
    ws.add_data_validation(category_dv)
    category_dv.add('C4:C102')

    status_dv = DataValidation(type="list", formula1='"Met,Not Met,Waived,N/A"')
    ws.add_data_validation(status_dv)
    status_dv.add('E4:E102')

    # Column widths
    widths = [12, 15, 18, 55, 10, 35, 20, 15, 35, 25]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_summary_dashboard_sheet(ws):
    """Create standard Summary Dashboard sheet."""
    ws.title = "Summary Dashboard"
    border = THIN_BORDER

    # Header
    ws.merge_cells("A1:G1")
    cell = ws.cell(row=1, column=1, value="SECURITY TESTING ASSESSMENT - COMPLIANCE SUMMARY")
    cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="003366")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Subtitle
    ws.merge_cells("A2:G2")
    cell = ws.cell(row=2, column=1, value=CONTROL_REF)
    cell.font = Font(name="Calibri", size=10, italic=True, color="003366")
    cell.alignment = Alignment(horizontal="left", vertical="center")

    # TABLE 1 banner
    row = 4
    ws.merge_cells(f"A{row}:G{row}")
    cell = ws.cell(row=row, column=1, value="TABLE 1: COMPLIANCE OVERVIEW")
    cell.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="003366")
    cell.alignment = Alignment(horizontal="left", vertical="center")

    # Column headers
    row = 5
    headers = ["Assessment Area", "Total Requirements", "Compliant", "Partially Compliant", "Non-Compliant", "N/A", "Compliance %"]
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col, value=header)
        cell.font = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="4472C4")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border
    ws.row_dimensions[row].height = 30

    # Assessment areas (based on domain sheets)
    areas = [
        "Deliverable Inventory",
        "Code Review Tracking",
        "Security Testing",
        "SBOM Management",
        "Acceptance Sign-off",
    ]

    for i, area in enumerate(areas):
        r = row + 1 + i
        ws.cell(row=r, column=1, value=area).font = Font(name="Calibri", size=10)
        ws.cell(row=r, column=1).border = border
        for col in range(2, 8):
            cell = ws.cell(row=r, column=col)
            cell.fill = PatternFill("solid", fgColor="FFFFCC")
            cell.border = border
            cell.alignment = Alignment(horizontal="center")

    # TOTAL row
    total_row = row + 1 + len(areas)
    ws.cell(row=total_row, column=1, value="TOTAL").font = Font(name="Calibri", size=10, bold=True)
    ws.cell(row=total_row, column=1).fill = PatternFill("solid", fgColor="D9D9D9")
    ws.cell(row=total_row, column=1).border = border

    data_start = row + 1
    data_end = total_row - 1
    for col_idx in range(2, 7):
        col_letter = chr(64 + col_idx)
        cell = ws.cell(row=total_row, column=col_idx)
        cell.value = f"=SUM({col_letter}{data_start}:{col_letter}{data_end})"
        cell.font = Font(name="Calibri", size=10, bold=True)
        cell.fill = PatternFill("solid", fgColor="D9D9D9")
        cell.border = border
        cell.alignment = Alignment(horizontal="center")

    # Compliance % formula
    cell = ws.cell(row=total_row, column=7)
    cell.value = f'=IF((B{total_row}-F{total_row})=0,"0%",ROUND(C{total_row}/(B{total_row}-F{total_row})*100,1)&"%")'
    cell.font = Font(name="Calibri", size=10, bold=True)
    cell.fill = PatternFill("solid", fgColor="D9D9D9")
    cell.border = border
    cell.alignment = Alignment(horizontal="center")

    # TABLE 2: KEY METRICS
    row = total_row + 2
    ws.merge_cells(f"A{row}:G{row}")
    cell = ws.cell(row=row, column=1, value="TABLE 2: KEY METRICS")
    cell.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="4472C4")
    cell.alignment = Alignment(horizontal="left", vertical="center")

    metrics = [
        "Last Assessment Date",
        "Next Review Due",
        "Assessment Owner",
        "Overall Risk Rating",
    ]
    for i, metric in enumerate(metrics):
        r = row + 1 + i
        ws.cell(row=r, column=1, value=metric).font = Font(name="Calibri", size=10, bold=True)
        ws.cell(row=r, column=1).border = border
        ws.merge_cells(f"B{r}:G{r}")
        cell = ws.cell(row=r, column=2)
        cell.fill = PatternFill("solid", fgColor="FFFFCC")
        cell.border = border

    # TABLE 3: CRITICAL FINDINGS
    row = row + 1 + len(metrics) + 1
    ws.merge_cells(f"A{row}:G{row}")
    cell = ws.cell(row=row, column=1, value="TABLE 3: CRITICAL FINDINGS")
    cell.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="C00000")
    cell.alignment = Alignment(horizontal="left", vertical="center")

    finding_headers = ["#", "Finding", "Severity", "Affected Area", "Recommended Action", "Owner", "Due Date"]
    row += 1
    for col, header in enumerate(finding_headers, 1):
        cell = ws.cell(row=row, column=col, value=header)
        cell.font = Font(name="Calibri", size=10, bold=True)
        cell.fill = PatternFill("solid", fgColor="D9D9D9")
        cell.border = border
        cell.alignment = Alignment(horizontal="center", wrap_text=True)

    for i in range(1, 6):
        r = row + i
        ws.cell(row=r, column=1, value=i).border = border
        ws.cell(row=r, column=1).alignment = Alignment(horizontal="center")
        for col in range(2, 8):
            cell = ws.cell(row=r, column=col)
            cell.fill = PatternFill("solid", fgColor="FFFFCC")
            cell.border = border

    # Column widths
    ws.column_dimensions["A"].width = 40
    ws.column_dimensions["B"].width = 16
    ws.column_dimensions["C"].width = 16
    ws.column_dimensions["D"].width = 18
    ws.column_dimensions["E"].width = 18
    ws.column_dimensions["F"].width = 12
    ws.column_dimensions["G"].width = 15

    ws.freeze_panes = "A4"


def create_evidence_register_sheet(ws):
    """Create standard Evidence Register (8 columns, 100 rows)."""
    ws.title = "Evidence Register"
    border = THIN_BORDER

    # Header
    ws.merge_cells("A1:H1")
    cell = ws.cell(row=1, column=1, value="EVIDENCE REGISTER")
    cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="003366")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Subtitle
    ws.merge_cells("A2:H2")
    cell = ws.cell(row=2, column=1, value="Record all evidence collected during the assessment. Each row represents one piece of evidence.")
    cell.font = Font(name="Calibri", size=10, italic=True)
    cell.alignment = Alignment(horizontal="left", vertical="center")

    # Column headers row 4
    headers = ["Evidence ID", "Assessment Area", "Evidence Type", "Description", "Location / Path", "Date Collected", "Collected By", "Verification Status"]
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col, value=header)
        cell.font = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="4472C4")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border
    ws.row_dimensions[4].height = 30

    # 100 data rows (5-104)
    for i in range(1, 101):
        row = i + 4
        # Evidence ID (gray font, no yellow fill)
        cell = ws.cell(row=row, column=1, value=f"EV-{i:03d}")
        cell.font = Font(name="Calibri", size=10, color="808080")
        cell.border = border

        # Cols B-H: yellow fill + border
        for col in range(2, 9):
            cell = ws.cell(row=row, column=col)
            cell.fill = PatternFill("solid", fgColor="FFFFCC")
            cell.border = border

    # Dropdowns
    ev_types = DataValidation(type="list", formula1='"Configuration file,Screenshot,Log extract,Policy document,Training record,Audit report,Risk assessment,Interview notes,Test results,Other"', allow_blank=True)
    ev_types.prompt = "Select evidence type"
    ws.add_data_validation(ev_types)
    ev_types.add("C5:C104")

    verify_status = DataValidation(type="list", formula1='"Verified,Pending Verification,Insufficient,Not Reviewed"', allow_blank=True)
    verify_status.prompt = "Select verification status"
    ws.add_data_validation(verify_status)
    verify_status.add("H5:H104")

    # Column widths
    ws.column_dimensions["A"].width = 15
    ws.column_dimensions["B"].width = 25
    ws.column_dimensions["C"].width = 22
    ws.column_dimensions["D"].width = 40
    ws.column_dimensions["E"].width = 45
    ws.column_dimensions["F"].width = 16
    ws.column_dimensions["G"].width = 20
    ws.column_dimensions["H"].width = 22

    ws.freeze_panes = "A5"


def create_approval_signoff_sheet(ws):
    """Create standard Approval Sign-Off sheet."""
    ws.title = "Approval Sign-Off"
    border = THIN_BORDER

    # Header
    ws.merge_cells("A1:E1")
    cell = ws.cell(row=1, column=1, value="ASSESSMENT APPROVAL AND SIGN-OFF")
    cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="003366")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # ASSESSMENT SUMMARY banner
    row = 3
    ws.merge_cells(f"A{row}:E{row}")
    cell = ws.cell(row=row, column=1, value="ASSESSMENT SUMMARY")
    cell.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="4472C4")
    cell.alignment = Alignment(horizontal="left", vertical="center")

    # Summary fields
    summary_fields = [
        ("Document:", DOCUMENT_ID),
        ("Assessment Period:", ""),
        ("Overall Compliance Rating:", ""),
        ("Assessment Status:", ""),
        ("Assessed By:", ""),
    ]
    for i, (label, value) in enumerate(summary_fields):
        r = row + 1 + i
        ws.cell(row=r, column=1, value=label).font = Font(name="Calibri", size=10, bold=True)
        ws.merge_cells(f"B{r}:E{r}")
        cell = ws.cell(row=r, column=2, value=value)
        cell.border = border
        if label in ("Assessment Status:", "Overall Compliance Rating:"):
            cell.fill = PatternFill("solid", fgColor="FFFFCC")

    # Assessment Status dropdown
    status_dv = DataValidation(type="list", formula1='"Draft,Final,Requires remediation,Re-assessment required"', allow_blank=True)
    ws.add_data_validation(status_dv)
    status_dv.add(f"B{row + 4}")

    row = row + 1 + len(summary_fields) + 1

    # Helper for approver sections
    def _approver_section(start_row, title, fill_color):
        ws.merge_cells(f"A{start_row}:E{start_row}")
        cell = ws.cell(row=start_row, column=1, value=title)
        cell.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor=fill_color)
        cell.alignment = Alignment(horizontal="left", vertical="center")

        fields = ["Name:", "Title:", "Date:", "Signature:", "Comments:"]
        for i, field in enumerate(fields):
            r = start_row + 1 + i
            ws.cell(row=r, column=1, value=field).font = Font(name="Calibri", size=10, bold=True)
            ws.merge_cells(f"B{r}:E{r}")
            cell = ws.cell(row=r, column=2)
            cell.fill = PatternFill("solid", fgColor="FFFFCC")
            cell.border = border
        return start_row + 1 + len(fields) + 1

    row = _approver_section(row, f"COMPLETED BY {DASH} Assessment Lead", "4472C4")
    row = _approver_section(row, f"REVIEWED BY {DASH} Security Manager", "4472C4")
    row = _approver_section(row, f"APPROVED BY {DASH} CISO", "003366")

    # FINAL DECISION
    ws.cell(row=row, column=1, value="FINAL DECISION:").font = Font(name="Calibri", size=11, bold=True)
    ws.merge_cells(f"B{row}:E{row}")
    cell = ws.cell(row=row, column=2)
    cell.fill = PatternFill("solid", fgColor="FFFFCC")
    cell.border = border

    final_dv = DataValidation(type="list", formula1='"Approved,Approved with Conditions,Rejected,Deferred"', allow_blank=True)
    ws.add_data_validation(final_dv)
    final_dv.add(f"B{row}")

    # NEXT REVIEW DETAILS
    row += 3
    ws.merge_cells(f"A{row}:E{row}")
    cell = ws.cell(row=row, column=1, value="NEXT REVIEW DETAILS")
    cell.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="4472C4")
    cell.alignment = Alignment(horizontal="left", vertical="center")

    review_fields = ["Next Review Date:", "Review Frequency:", "Scheduled Reviewer:"]
    for i, field in enumerate(review_fields):
        r = row + 1 + i
        ws.cell(row=r, column=1, value=field).font = Font(name="Calibri", size=10, bold=True)
        ws.merge_cells(f"B{r}:E{r}")
        cell = ws.cell(row=r, column=2)
        cell.fill = PatternFill("solid", fgColor="FFFFCC")
        cell.border = border

    # Column widths
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

    # Create domain sheets
    create_instructions_sheet(wb.create_sheet())
    create_deliverable_inventory_sheet(wb.create_sheet())
    create_code_review_sheet(wb.create_sheet())
    create_security_testing_sheet(wb.create_sheet())
    create_sbom_management_sheet(wb.create_sheet())
    create_acceptance_signoff_sheet(wb.create_sheet())

    # Create standard sheets
    create_summary_dashboard_sheet(wb.create_sheet())
    create_evidence_register_sheet(wb.create_sheet())
    create_approval_signoff_sheet(wb.create_sheet())

    # Remove default sheet
    wb.remove(default_sheet)

    # Save workbook
    wb.save(OUTPUT_FILENAME)
    logger.info(f"Workbook saved: {OUTPUT_FILENAME}")
    logger.info(f"{CHECK} SUCCESS: Generated {OUTPUT_FILENAME}")

    return OUTPUT_FILENAME


# =============================================================================
# MAIN EXECUTION
# =============================================================================
if __name__ == "__main__":
    generate_workbook()

# =============================================================================
# QA_VERIFIED: 2026-02-10
# QA_STATUS: PASSED - STANDARDISATION COMPLETE
# QA_TOOL: Claude Code Standardization
# CHANGES: unicode symbols, freeze panes, summary dashboard, evidence register,
#          approval sign-off, updated instructions sheet list, logger output
# =============================================================================
