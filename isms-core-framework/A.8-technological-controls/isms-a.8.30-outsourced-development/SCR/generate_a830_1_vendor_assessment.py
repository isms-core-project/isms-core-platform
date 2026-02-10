#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
================================================================================
ISMS-IMP-A.8.30.1 - Vendor Assessment and Registry
================================================================================

ISO/IEC 27001:2022 Control A.8.30: Outsourced Development
Assessment Domain 1 of 4: Vendor Assessment and Registry

This script generates a comprehensive Excel assessment workbook for managing
vendor security assessments and the approved vendor registry for outsourced
development engagements.
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
DOCUMENT_ID = "ISMS-IMP-A.8.30.1"
WORKBOOK_NAME = "Vendor Assessment and Registry"
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
HEADER_FONT = Font(bold=True, size=11, color="FFFFFF", name="Calibri")
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
        "1. Complete all assessment sheets in order, starting with Vendor Registry.",
        "2. Classify each vendor by risk tier (Critical/High/Standard) in the registry.",
        "3. Complete security assessment records for each vendor.",
        "4. Run through the due diligence checklist for vendor onboarding.",
        "5. Verify development environment security attestations.",
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
        "Vendor security questionnaire responses and risk assessments",
        "Due diligence verification records and checklists",
        "Development environment security attestation documents",
        "Vendor approval records and risk tier classifications",
        "Annual reassessment reports and compliance certificates",
        "Vendor registry updates and status change logs",
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


def create_vendor_registry_sheet(ws):
    """Create the Vendor Registry sheet."""
    ws.title = "Vendor Registry"

    headers = [
        "Vendor_ID", "Vendor_Name", "Registry_Status", "Risk_Tier",
        "Initial_Assessment_Date", "Last_Assessment_Date", "Next_Assessment_Due",
        "ISO_27001_Certified", "SOC2_Type2", "Primary_Contact",
        "Approved_Project_Types", "Approved_By", "Notes"
    ]

    # Title row
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "VENDOR REGISTRY"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write column headers (row 3)
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Add data validation dropdowns
    status_dv = DataValidation(type="list", formula1='"Approved,Pending,Suspended,Removed"')
    ws.add_data_validation(status_dv)
    status_dv.add(f'C4:C102')

    tier_dv = DataValidation(type="list", formula1='"Critical,High,Standard"')
    ws.add_data_validation(tier_dv)
    tier_dv.add(f'D4:D102')

    cert_dv = DataValidation(type="list", formula1='"Yes,No,In Progress"')
    ws.add_data_validation(cert_dv)
    cert_dv.add(f'H4:H102')
    cert_dv.add(f'I4:I102')

    # Format input rows
    for row in range(4, 23):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Set column widths
    widths = [12, 30, 15, 12, 18, 18, 18, 15, 12, 25, 25, 20, 30]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_security_assessment_sheet(ws):
    """Create the Security Assessment sheet."""
    ws.title = "Security Assessment"

    headers = [
        "Assessment_ID", "Vendor_ID", "Assessment_Date", "Assessment_Type",
        "Assessor", "Security_Certification", "Cert_Expiry_Date",
        "SDLC_Maturity", "Security_Incident_History", "SAST_DAST_Tooling",
        "Personnel_Screening", "Dev_Environment_Security", "Overall_Risk_Rating",
        "Recommendation", "Conditions", "Evidence_Location"
    ]

    # Title row
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "SECURITY ASSESSMENT"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write column headers (row 3)
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    type_dv = DataValidation(type="list", formula1='"Initial,Annual,Triggered"')
    ws.add_data_validation(type_dv)
    type_dv.add('D4:D102')

    cert_dv = DataValidation(type="list", formula1='"ISO 27001,SOC 2,Both,None"')
    ws.add_data_validation(cert_dv)
    cert_dv.add('F4:F102')

    maturity_dv = DataValidation(type="list", formula1='"Mature,Developing,Basic,Unknown"')
    ws.add_data_validation(maturity_dv)
    maturity_dv.add('H4:H102')

    incident_dv = DataValidation(type="list", formula1='"None,Minor,Major"')
    ws.add_data_validation(incident_dv)
    incident_dv.add('I4:I102')

    screening_dv = DataValidation(type="list", formula1='"Verified,Attested,Unknown"')
    ws.add_data_validation(screening_dv)
    screening_dv.add('K4:K102')

    env_dv = DataValidation(type="list", formula1='"Compliant,Partial,Non-Compliant"')
    ws.add_data_validation(env_dv)
    env_dv.add('L4:L102')

    risk_dv = DataValidation(type="list", formula1='"Low,Medium,High,Critical"')
    ws.add_data_validation(risk_dv)
    risk_dv.add('M4:M102')

    rec_dv = DataValidation(type="list", formula1='"Approve,Conditional,Reject"')
    ws.add_data_validation(rec_dv)
    rec_dv.add('N4:N102')

    # Format input rows
    for row in range(4, 23):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Column widths
    widths = [15, 12, 15, 15, 20, 18, 15, 15, 20, 25, 18, 20, 18, 15, 30, 35]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_due_diligence_sheet(ws):
    """Create the Due Diligence Checklist sheet."""
    ws.title = "Due Diligence"

    headers = [
        "Vendor_ID", "Check_Category", "Check_Item", "Status",
        "Evidence_Type", "Evidence_Reference", "Verified_By",
        "Verified_Date", "Notes"
    ]

    # Title row
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "DUE DILIGENCE"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write column headers (row 3)
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Standard checklist items
    checklist_items = [
        ("Security Certification", "Valid ISO 27001 or SOC 2 Type II certification"),
        ("Security Certification", "Certification scope covers development services"),
        ("Secure Development", "Documented SDLC methodology"),
        ("Secure Development", "Security gates defined in SDLC"),
        ("Secure Development", "SAST/DAST/SCA tools in use"),
        ("Incident History", "No major security incidents in 24 months"),
        ("Incident History", "Incident response process documented"),
        ("Technical Capability", "Code review practices established"),
        ("Technical Capability", "Vulnerability management process"),
        ("Personnel Security", "Background checks for developers"),
        ("Personnel Security", "Security awareness training"),
        ("Subcontractor Mgmt", "Subcontractor security policy"),
        ("Business Continuity", "BCP/DR plans documented"),
        ("Reference Check", "Reference 1 contacted and verified"),
        ("Reference Check", "Reference 2 contacted and verified"),
    ]

    row = 4
    for category, item in checklist_items:
        ws.cell(row=row, column=1, value="[Vendor_ID]").fill = INPUT_FILL
        ws.cell(row=row, column=2, value=category)
        ws.cell(row=row, column=3, value=item)
        for col in range(4, 10):
            ws.cell(row=row, column=col).fill = INPUT_FILL
        for col in range(1, 10):
            ws.cell(row=row, column=col).border = THIN_BORDER
        row += 1

    # Data validation
    status_dv = DataValidation(type="list", formula1='"Complete,Pending,N/A"')
    ws.add_data_validation(status_dv)
    status_dv.add('D4:D102')

    evidence_dv = DataValidation(type="list", formula1='"Certificate,Attestation,Document,Interview"')
    ws.add_data_validation(evidence_dv)
    evidence_dv.add('E4:E102')

    # Column widths
    widths = [12, 20, 45, 12, 15, 35, 20, 15, 30]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_environment_security_sheet(ws):
    """Create the Environment Security Assessment sheet."""
    ws.title = "Environment Security"

    headers = [
        "Vendor_ID", "Assessment_Date", "MFA_Enabled", "Network_Isolation",
        "Endpoint_Security", "Code_Repository", "Secret_Scanning",
        "Branch_Protection", "Data_Handling", "Attestation_Received",
        "Attestation_Date", "Compliance_Status"
    ]

    # Title row
    num_cols = len(headers)
    last_col = get_column_letter(num_cols)
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = "ENVIRONMENT SECURITY"
    ws["A1"].font = TITLE_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Write column headers (row 3)
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col, value=header)
        cell.font = Font(name="Calibri", size=11, bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    yn_dv = DataValidation(type="list", formula1='"Yes,No"')
    ws.add_data_validation(yn_dv)
    yn_dv.add('G4:G102')
    yn_dv.add('J4:J102')

    ynp_dv = DataValidation(type="list", formula1='"Yes,Partial,No"')
    ws.add_data_validation(ynp_dv)
    ynp_dv.add('C4:C102')
    ynp_dv.add('H4:H102')

    network_dv = DataValidation(type="list", formula1='"Isolated,Segmented,Shared"')
    ws.add_data_validation(network_dv)
    network_dv.add('D4:D102')

    endpoint_dv = DataValidation(type="list", formula1='"Compliant,Partial,Non-Compliant"')
    ws.add_data_validation(endpoint_dv)
    endpoint_dv.add('E4:E102')

    repo_dv = DataValidation(type="list", formula1='"Secure,Partial,Unsecure"')
    ws.add_data_validation(repo_dv)
    repo_dv.add('F4:F102')

    data_dv = DataValidation(type="list", formula1='"No Prod Data,Masked,Raw"')
    ws.add_data_validation(data_dv)
    data_dv.add('I4:I102')

    compliance_dv = DataValidation(type="list", formula1='"Compliant,Conditional,Non-Compliant"')
    ws.add_data_validation(compliance_dv)
    compliance_dv.add('L4:L102')

    # Format input rows
    for row in range(4, 23):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Column widths
    widths = [12, 15, 12, 15, 15, 15, 15, 15, 15, 18, 15, 18]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_summary_dashboard_sheet(ws):
    """Create standard Summary Dashboard sheet."""
    thin = Side(style="thin")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    ws.title = "Summary Dashboard"
    ws.merge_cells("A1:G1")
    cell = ws.cell(row=1, column=1, value="VENDOR ASSESSMENT - COMPLIANCE SUMMARY")
    cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="003366")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    ws.merge_cells("A2:G2")
    cell = ws.cell(row=2, column=1, value=CONTROL_REF)
    cell.font = Font(name="Calibri", size=10, italic=True, color="003366")

    row = 4
    ws.merge_cells(f"A{row}:G{row}")
    cell = ws.cell(row=row, column=1, value="TABLE 1: COMPLIANCE OVERVIEW")
    cell.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="003366")

    row = 5
    headers = ["Assessment Area", "Total Requirements", "Compliant", "Partially Compliant", "Non-Compliant", "N/A", "Compliance %"]
    for col, h in enumerate(headers, 1):
        c = ws.cell(row=row, column=col, value=h)
        c.font = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="4472C4")
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = border

    areas = ["Vendor Registry", "Security Assessment", "Due Diligence", "Environment Security"]
    for i, area in enumerate(areas):
        r = 6 + i
        ws.cell(row=r, column=1, value=area).font = Font(name="Calibri", size=10)
        ws.cell(row=r, column=1).border = border
        for col in range(2, 8):
            c = ws.cell(row=r, column=col)
            c.fill = PatternFill("solid", fgColor="FFFFCC")
            c.border = border
            c.alignment = Alignment(horizontal="center")

    total_row = 6 + len(areas)
    ws.cell(row=total_row, column=1, value="TOTAL").font = Font(name="Calibri", size=10, bold=True)
    ws.cell(row=total_row, column=1).fill = PatternFill("solid", fgColor="D9D9D9")
    ws.cell(row=total_row, column=1).border = border
    for col_idx in range(2, 7):
        col_letter = chr(64 + col_idx)
        c = ws.cell(row=total_row, column=col_idx)
        c.value = f"=SUM({col_letter}6:{col_letter}{total_row-1})"
        c.font = Font(name="Calibri", size=10, bold=True)
        c.fill = PatternFill("solid", fgColor="D9D9D9")
        c.border = border
        c.alignment = Alignment(horizontal="center")
    c = ws.cell(row=total_row, column=7)
    c.value = f'=IF((B{total_row}-F{total_row})=0,"0%",ROUND(C{total_row}/(B{total_row}-F{total_row})*100,1)&"%")'
    c.font = Font(name="Calibri", size=10, bold=True)
    c.fill = PatternFill("solid", fgColor="D9D9D9")
    c.border = border
    c.alignment = Alignment(horizontal="center")

    # TABLE 2
    row = total_row + 2
    ws.merge_cells(f"A{row}:G{row}")
    c = ws.cell(row=row, column=1, value="TABLE 2: KEY METRICS")
    c.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor="4472C4")
    for i, m in enumerate(["Last Assessment Date", "Next Review Due", "Assessment Owner", "Overall Risk Rating"]):
        r = row + 1 + i
        ws.cell(row=r, column=1, value=m).font = Font(name="Calibri", size=10, bold=True)
        ws.cell(row=r, column=1).border = border
        ws.merge_cells(f"B{r}:G{r}")
        ws.cell(row=r, column=2).fill = PatternFill("solid", fgColor="FFFFCC")
        ws.cell(row=r, column=2).border = border

    # TABLE 3
    row = row + 6
    ws.merge_cells(f"A{row}:G{row}")
    c = ws.cell(row=row, column=1, value="TABLE 3: CRITICAL FINDINGS")
    c.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor="C00000")
    row += 1
    for col, h in enumerate(["#", "Finding", "Severity", "Affected Area", "Recommended Action", "Owner", "Due Date"], 1):
        c = ws.cell(row=row, column=col, value=h)
        c.font = Font(name="Calibri", size=10, bold=True)
        c.fill = PatternFill("solid", fgColor="D9D9D9")
        c.border = border
    for i in range(1, 6):
        r = row + i
        ws.cell(row=r, column=1, value=i).border = border
        for col in range(2, 8):
            ws.cell(row=r, column=col).fill = PatternFill("solid", fgColor="FFFFCC")
            ws.cell(row=r, column=col).border = border

    for col, w in zip("ABCDEFG", [40, 16, 16, 18, 18, 12, 15]):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = "A4"


def create_evidence_register_sheet(ws):
    """Create standard Evidence Register sheet."""
    thin = Side(style="thin")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    ws.title = "Evidence Register"

    # Header row 1 - title banner
    ws.merge_cells("A1:H1")
    cell = ws.cell(row=1, column=1, value="EVIDENCE REGISTER")
    cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="003366")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    # Header row 2 - control ref
    ws.merge_cells("A2:H2")
    cell = ws.cell(row=2, column=1, value=CONTROL_REF)
    cell.font = Font(name="Calibri", size=10, italic=True, color="003366")

    # Header row 3 - guidance
    ws.merge_cells("A3:H3")
    cell = ws.cell(row=3, column=1, value="Record all evidence artefacts supporting this assessment. Link to shared drive or attach to audit package.")
    cell.font = Font(name="Calibri", size=9, italic=True, color="666666")

    # Column headers (row 4)
    headers = ["Evidence ID", "Evidence Title", "Evidence Type", "Description",
               "Source / Location", "Date Collected", "Collected By", "Status"]
    for col, h in enumerate(headers, 1):
        c = ws.cell(row=4, column=col, value=h)
        c.font = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="4472C4")
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = border

    # Pre-populate 100 rows with EV-001..EV-100
    evidence_type_dv = DataValidation(
        type="list",
        formula1='"Policy Document,Process Document,Screenshot,Log Extract,Configuration Export,Audit Report,Training Record,Signed Attestation,Tool Output,Other"'
    )
    ws.add_data_validation(evidence_type_dv)

    status_dv = DataValidation(
        type="list",
        formula1='"Collected,Pending,Not Available,Expired"'
    )
    ws.add_data_validation(status_dv)

    for i in range(1, 101):
        r = 4 + i
        # Evidence ID (gray font placeholder)
        c = ws.cell(row=r, column=1, value=f"EV-{i:03d}")
        c.font = Font(name="Calibri", size=10, color="808080")
        c.border = border
        # Cols B-H: yellow input + border
        for col in range(2, 9):
            c = ws.cell(row=r, column=col)
            c.fill = PatternFill("solid", fgColor="FFFFCC")
            c.border = border

    evidence_type_dv.add("C5:C104")
    status_dv.add("H5:H104")

    # Column widths
    for col, w in zip("ABCDEFGH", [15, 25, 22, 40, 45, 16, 20, 22]):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = "A5"


def create_approval_signoff_sheet(ws):
    """Create standard Approval Sign-Off sheet."""
    thin = Side(style="thin")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    ws.title = "Approval Sign-Off"

    # Title banner
    ws.merge_cells("A1:E1")
    cell = ws.cell(row=1, column=1, value="ASSESSMENT APPROVAL AND SIGN-OFF")
    cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="003366")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    ws.merge_cells("A2:E2")
    cell = ws.cell(row=2, column=1, value=CONTROL_REF)
    cell.font = Font(name="Calibri", size=10, italic=True, color="003366")

    # --- ASSESSMENT SUMMARY ---
    row = 3
    ws.merge_cells(f"A{row}:E{row}")
    c = ws.cell(row=row, column=1, value="ASSESSMENT SUMMARY")
    c.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor="4472C4")

    summary_fields = [
        ("Document:", f"{DOCUMENT_ID} - {WORKBOOK_NAME}"),
        ("Assessment Period:", ""),
        ("Overall Compliance:", ""),
        ("Assessment Status:", ""),
        ("Assessed By:", ""),
    ]
    for i, (label, value) in enumerate(summary_fields):
        r = row + 1 + i
        ws.cell(row=r, column=1, value=label).font = Font(name="Calibri", size=10, bold=True)
        ws.merge_cells(f"B{r}:E{r}")
        cell = ws.cell(row=r, column=2, value=value)
        if not value:
            cell.fill = PatternFill("solid", fgColor="FFFFCC")
            cell.border = border

    # Assessment Status dropdown
    status_row = row + 4
    status_dv = DataValidation(
        type="list",
        formula1='"Draft,Final,Requires remediation,Re-assessment required"',
        allow_blank=True,
    )
    ws.add_data_validation(status_dv)
    status_dv.add(f"B{status_row}")

    # --- APPROVER SECTIONS ---
    row = row + 1 + len(summary_fields) + 1

    def _approver_section(start_row, title, fill_color):
        ws.merge_cells(f"A{start_row}:E{start_row}")
        c = ws.cell(row=start_row, column=1, value=title)
        c.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor=fill_color)
        fields = ["Name:", "Title:", "Date:", "Signature:", "Comments:"]
        for idx, field in enumerate(fields):
            r = start_row + 1 + idx
            ws.cell(row=r, column=1, value=field).font = Font(name="Calibri", size=10, bold=True)
            ws.merge_cells(f"B{r}:E{r}")
            c = ws.cell(row=r, column=2)
            c.fill = PatternFill("solid", fgColor="FFFFCC")
            c.border = border
        return start_row + 1 + len(fields) + 1

    row = _approver_section(row, "COMPLETED BY (ASSESSOR)", "4472C4")
    row = _approver_section(row, "REVIEWED BY (INFORMATION SECURITY OFFICER)", "4472C4")
    row = _approver_section(row, "APPROVED BY (CISO)", "003366")

    # --- FINAL DECISION ---
    ws.cell(row=row, column=1, value="FINAL DECISION:").font = Font(name="Calibri", size=11, bold=True)
    ws.merge_cells(f"B{row}:E{row}")
    ws.cell(row=row, column=2).fill = PatternFill("solid", fgColor="FFFFCC")
    ws.cell(row=row, column=2).border = border
    decision_dv = DataValidation(
        type="list",
        formula1='"Approved,Approved with Conditions,Rejected,Deferred"',
        allow_blank=True,
    )
    ws.add_data_validation(decision_dv)
    decision_dv.add(f"B{row}")

    # --- NEXT REVIEW DETAILS ---
    row += 3
    ws.merge_cells(f"A{row}:E{row}")
    c = ws.cell(row=row, column=1, value="NEXT REVIEW DETAILS")
    c.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    c.fill = PatternFill("solid", fgColor="4472C4")

    for i, field in enumerate(["Next Review Date:", "Review Responsible:", "Special Considerations:"]):
        r = row + 1 + i
        ws.cell(row=r, column=1, value=field).font = Font(name="Calibri", size=10, bold=True)
        ws.merge_cells(f"B{r}:E{r}")
        ws.cell(row=r, column=2).fill = PatternFill("solid", fgColor="FFFFCC")
        ws.cell(row=r, column=2).border = border

    # Column widths
    for col, w in zip("ABCDE", [32, 25, 20, 20, 20]):
        ws.column_dimensions[col].width = w
    ws.freeze_panes = "A3"


def generate_workbook():
    """Generate the complete assessment workbook."""
    logger.info(f"Generating {DOCUMENT_ID} - {WORKBOOK_NAME}")

    wb = Workbook()

    # Remove default sheet
    default_sheet = wb.active

    # Create all sheets
    create_instructions_sheet(wb.create_sheet())
    create_vendor_registry_sheet(wb.create_sheet())
    create_security_assessment_sheet(wb.create_sheet())
    create_due_diligence_sheet(wb.create_sheet())
    create_environment_security_sheet(wb.create_sheet())
    create_summary_dashboard_sheet(wb.create_sheet())
    create_evidence_register_sheet(wb.create_sheet())
    create_approval_signoff_sheet(wb.create_sheet())

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
# QA_TOOL: Claude Code Standardization
# CHANGES: Unicode symbols, freeze_panes, Summary Dashboard, Evidence Register,
#          Approval Sign-Off sheets added; QA footer updated
# =============================================================================
