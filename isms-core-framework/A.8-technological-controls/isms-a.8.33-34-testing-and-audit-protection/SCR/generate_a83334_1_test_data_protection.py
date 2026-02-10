#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
================================================================================
ISMS-IMP-A.8.33-34.1 - Test Data Protection Assessment
================================================================================

ISO/IEC 27001:2022 Controls A.8.33: Test Information & A.8.34: Protection of
Information Systems During Audit Testing
Assessment Domain 1 of 3: Test Data Governance & Protection

This script generates a comprehensive Excel assessment workbook for managing
test data protection including inventory, masking, anonymization, environment
registry, and compliance verification.
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
DOCUMENT_ID = "ISMS-IMP-A.8.33-34.1"
WORKBOOK_NAME = "Test Data Protection Assessment"
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
        "1. Complete all assessment sheets in order, starting with Test Data Inventory.",
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
        "Test data inventory documentation and authorisation records",
        "Data masking configuration and effectiveness reports",
        "Test environment security assessment results",
        "Data refresh authorisation and governance records",
        "Audit activity authorisation and access control logs",
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

    # Masking Effectiveness Scale
    scale_row = 37
    ws[f"A{scale_row}"] = "Masking Effectiveness Scale"
    ws[f"A{scale_row}"].font = Font(bold=True, size=12)

    scale_items = [
        "5 - Excellent: All PII fully anonymised, irreversible",
        "4 - Good: Strong masking, minimal re-identification risk",
        "3 - Adequate: Reasonable masking, some risk",
        "2 - Poor: Weak masking, significant risk",
        "1 - Inadequate: Minimal/no masking, high risk",
    ]

    for i, item in enumerate(scale_items):
        ws[f"A{scale_row + 1 + i}"] = item

    # Column Widths & Freeze
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 45
    ws.column_dimensions["C"].width = 70
    ws.freeze_panes = "A4"


def create_test_data_inventory_sheet(ws):
    """Create the Test Data Inventory sheet."""
    ws.title = "Test Data Inventory"

    # Title
    ws.merge_cells('A1:T1')
    title_cell = ws.cell(row=1, column=1, value="TEST DATA INVENTORY")
    title_cell.font = TITLE_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = HEADER_ALIGNMENT
    ws.row_dimensions[1].height = 35

    ws.cell(row=2, column=1, value="Registry of all production data copied to test environments")

    headers = [
        "Data_Set_ID", "Data_Set_Name", "Source_System", "Target_Environment",
        "Data_Classification", "Contains_PII", "PII_Categories", "Data_Volume",
        "Authorization_Status", "Data_Owner", "Authorizer", "Authorization_Date",
        "Last_Copy_Date", "Refresh_Frequency", "Masking_Required", "Masking_Status",
        "Business_Justification", "Expiration_Date", "Evidence_Reference", "Notes"
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
    classification_dv.add('E5:E104')

    pii_dv = DataValidation(type="list", formula1='"Yes,No"')
    ws.add_data_validation(pii_dv)
    pii_dv.add('F5:F104')
    pii_dv.add('O5:O104')

    auth_status_dv = DataValidation(type="list", formula1='"Authorised,Pending,Unauthorised"')
    ws.add_data_validation(auth_status_dv)
    auth_status_dv.add('I5:I104')

    refresh_dv = DataValidation(type="list", formula1='"Daily,Weekly,Monthly,Quarterly,Ad-Hoc,One-Time"')
    ws.add_data_validation(refresh_dv)
    refresh_dv.add('N5:N104')

    masking_dv = DataValidation(type="list", formula1='"Fully Masked,Partially Masked,Not Masked,N/A"')
    ws.add_data_validation(masking_dv)
    masking_dv.add('P5:P104')

    # Format input rows
    for row in range(5, 105):
        ws.cell(row=row, column=1, value=f"TDI-{str(row-4).zfill(3)}")
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Summary Statistics section
    ws.cell(row=107, column=1, value="SUMMARY STATISTICS").font = Font(bold=True, size=12)

    summary_items = [
        ("Total Data Sets", "=COUNTA(B5:B104)"),
        ("Authorised Data Sets", '=COUNTIF(I5:I104,"Authorised")'),
        ("Pending Authorization", '=COUNTIF(I5:I104,"Pending")'),
        ("Unauthorised Data Sets", '=COUNTIF(I5:I104,"Unauthorised")'),
        ("Data Sets with PII", '=COUNTIF(F5:F104,"Yes")'),
        ("Fully Masked PII Sets", '=COUNTIFS(F5:F104,"Yes",P5:P104,"Fully Masked")'),
        ("Partially Masked PII Sets", '=COUNTIFS(F5:F104,"Yes",P5:P104,"Partially Masked")'),
        ("Unmasked PII Sets", '=COUNTIFS(F5:F104,"Yes",P5:P104,"Not Masked")'),
    ]

    row = 109
    for label, formula in summary_items:
        ws.cell(row=row, column=1, value=label).border = THIN_BORDER
        ws.cell(row=row, column=2, value=formula).border = THIN_BORDER
        row += 1

    # Column widths
    widths = [15, 30, 25, 25, 18, 12, 30, 15, 18, 25, 25, 15, 15, 18, 12, 18, 40, 15, 20, 30]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_data_masking_assessment_sheet(ws):
    """Create the Data Masking Assessment sheet."""
    ws.title = "Data Masking Assessment"

    ws.merge_cells('A1:U1')
    title_cell = ws.cell(row=1, column=1, value="DATA MASKING ASSESSMENT")
    title_cell.font = TITLE_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = HEADER_ALIGNMENT
    ws.row_dimensions[1].height = 35

    ws.cell(row=2, column=1, value="Evaluation of data masking and anonymization effectiveness")

    headers = [
        "Data_Set_ID", "Data_Set_Name", "Target_Environment", "Contains_PII",
        "Masking_Status", "Primary_Masking_Technique", "Masking_Tool",
        "Masking_Effectiveness_Score", "PII_Fields_Identified", "PII_Fields_Masked",
        "PII_Fields_Unmasked", "Masking_Verification_Date", "Verification_Method",
        "Re_identification_Risk", "Masking_Gap_Severity", "Remediation_Owner",
        "Remediation_Target_Date", "Remediation_Status", "Exception_Approved",
        "Exception_Justification", "Evidence_Reference"
    ]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    pii_dv = DataValidation(type="list", formula1='"Yes,No"')
    ws.add_data_validation(pii_dv)
    pii_dv.add('D5:D104')
    pii_dv.add('S5:S104')

    masking_dv = DataValidation(type="list", formula1='"Fully Masked,Partially Masked,Not Masked,N/A"')
    ws.add_data_validation(masking_dv)
    masking_dv.add('E5:E104')

    technique_dv = DataValidation(type="list", formula1='"Substitution,Shuffling,Tokenization,Encryption,Synthetic,Anonymization,None"')
    ws.add_data_validation(technique_dv)
    technique_dv.add('F5:F104')

    score_dv = DataValidation(type="list", formula1='"1,2,3,4,5"')
    ws.add_data_validation(score_dv)
    score_dv.add('H5:H104')

    verify_dv = DataValidation(type="list", formula1='"Automated,Manual Sampling,None"')
    ws.add_data_validation(verify_dv)
    verify_dv.add('M5:M104')

    risk_dv = DataValidation(type="list", formula1='"High,Medium,Low,None"')
    ws.add_data_validation(risk_dv)
    risk_dv.add('N5:N104')

    severity_dv = DataValidation(type="list", formula1='"Critical,High,Medium,Low"')
    ws.add_data_validation(severity_dv)
    severity_dv.add('O5:O104')

    status_dv = DataValidation(type="list", formula1='"Not Started,In Progress,Completed"')
    ws.add_data_validation(status_dv)
    status_dv.add('R5:R104')

    # Format input rows
    for row in range(5, 105):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Summary Statistics
    ws.cell(row=107, column=1, value="MASKING TECHNIQUE SUMMARY").font = Font(bold=True, size=12)

    techniques = ["Substitution", "Shuffling", "Tokenization", "Encryption", "Synthetic", "Anonymization", "None"]
    row = 109
    for tech in techniques:
        ws.cell(row=row, column=1, value=tech).border = THIN_BORDER
        ws.cell(row=row, column=2, value=f'=COUNTIF(F5:F104,"{tech}")').border = THIN_BORDER
        row += 1

    ws.cell(row=row + 1, column=1, value="EFFECTIVENESS SUMMARY").font = Font(bold=True, size=12)
    row += 3
    ws.cell(row=row, column=1, value="Average Effectiveness Score").border = THIN_BORDER
    ws.cell(row=row, column=2, value="=AVERAGE(H5:H104)").border = THIN_BORDER
    row += 1
    ws.cell(row=row, column=1, value="High Re-identification Risk").border = THIN_BORDER
    ws.cell(row=row, column=2, value='=COUNTIF(N5:N104,"High")').border = THIN_BORDER
    row += 1
    ws.cell(row=row, column=1, value="Critical Masking Gaps").border = THIN_BORDER
    ws.cell(row=row, column=2, value='=COUNTIF(O5:O104,"Critical")').border = THIN_BORDER

    # Column widths
    widths = [15, 30, 25, 12, 18, 25, 25, 12, 40, 40, 40, 15, 25, 18, 18, 25, 15, 18, 12, 40, 20]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_test_environment_registry_sheet(ws):
    """Create the Test Environment Registry sheet."""
    ws.title = "Test Environment Registry"

    ws.merge_cells('A1:U1')
    title_cell = ws.cell(row=1, column=1, value="TEST ENVIRONMENT REGISTRY")
    title_cell.font = TITLE_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = HEADER_ALIGNMENT
    ws.row_dimensions[1].height = 35

    ws.cell(row=2, column=1, value="Inventory of all test environments with security posture assessment")

    headers = [
        "Environment_ID", "Environment_Name", "Environment_Type", "Infrastructure_Type",
        "Environment_Owner", "Business_Unit", "Highest_Data_Classification",
        "Contains_Production_Data", "Access_Control_Type", "Network_Isolation",
        "Encryption_at_Rest", "Encryption_in_Transit", "Logging_Enabled",
        "Patch_Management", "Security_Control_Status", "Last_Security_Review",
        "Next_Review_Due", "Data_Masking_Enforced", "Environment_URL_Location",
        "Support_Contact", "Evidence_Reference"
    ]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    env_type_dv = DataValidation(type="list", formula1='"Development,QA,Staging,UAT,Performance,Training,DR-Test,Sandbox"')
    ws.add_data_validation(env_type_dv)
    env_type_dv.add('C5:C54')

    infra_type_dv = DataValidation(type="list", formula1='"On-Premise,Cloud-AWS,Cloud-Azure,Cloud-GCP,Hybrid,Container,Local"')
    ws.add_data_validation(infra_type_dv)
    infra_type_dv.add('D5:D54')

    classification_dv = DataValidation(type="list", formula1='"Public,Internal,Confidential,Restricted"')
    ws.add_data_validation(classification_dv)
    classification_dv.add('G5:G54')

    yn_dv = DataValidation(type="list", formula1='"Yes,No"')
    ws.add_data_validation(yn_dv)
    yn_dv.add('H5:H54')

    access_dv = DataValidation(type="list", formula1='"RBAC,AD/LDAP,SSO,Local Accounts,None"')
    ws.add_data_validation(access_dv)
    access_dv.add('I5:I54')

    isolation_dv = DataValidation(type="list", formula1='"Full,Partial,None"')
    ws.add_data_validation(isolation_dv)
    isolation_dv.add('J5:J54')

    ynp_dv = DataValidation(type="list", formula1='"Yes,Partial,No"')
    ws.add_data_validation(ynp_dv)
    ynp_dv.add('K5:K54')
    ynp_dv.add('L5:L54')
    ynp_dv.add('M5:M54')
    ynp_dv.add('R5:R54')

    patch_dv = DataValidation(type="list", formula1='"Automated,Manual-Current,Manual-Delayed,None"')
    ws.add_data_validation(patch_dv)
    patch_dv.add('N5:N54')

    status_dv = DataValidation(type="list", formula1='"Compliant,Partial,Non-Compliant"')
    ws.add_data_validation(status_dv)
    status_dv.add('O5:O54')

    # Format input rows
    for row in range(5, 55):
        ws.cell(row=row, column=1, value=f"ENV-{str(row-4).zfill(3)}")
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Summary Statistics
    ws.cell(row=57, column=1, value="ENVIRONMENT STATISTICS").font = Font(bold=True, size=12)

    summary_items = [
        ("Total Environments", "=COUNTA(B5:B54)"),
        ("Development Environments", '=COUNTIF(C5:C54,"Development")'),
        ("QA Environments", '=COUNTIF(C5:C54,"QA")'),
        ("UAT Environments", '=COUNTIF(C5:C54,"UAT")'),
        ("Environments with Prod Data", '=COUNTIF(H5:H54,"Yes")'),
        ("Security Compliant", '=COUNTIF(O5:O54,"Compliant")'),
        ("Security Partial", '=COUNTIF(O5:O54,"Partial")'),
        ("Security Non-Compliant", '=COUNTIF(O5:O54,"Non-Compliant")'),
        ("Full Network Isolation", '=COUNTIF(J5:J54,"Full")'),
        ("No Network Isolation", '=COUNTIF(J5:J54,"None")'),
    ]

    row = 59
    for label, formula in summary_items:
        ws.cell(row=row, column=1, value=label).border = THIN_BORDER
        ws.cell(row=row, column=2, value=formula).border = THIN_BORDER
        row += 1

    # Column widths
    widths = [15, 30, 20, 20, 25, 25, 18, 12, 25, 18, 12, 12, 12, 18, 18, 15, 15, 12, 40, 25, 20]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_data_refresh_schedule_sheet(ws):
    """Create the Data Refresh Schedule sheet."""
    ws.title = "Data Refresh Schedule"

    ws.merge_cells('A1:T1')
    title_cell = ws.cell(row=1, column=1, value="DATA REFRESH SCHEDULE")
    title_cell.font = TITLE_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = HEADER_ALIGNMENT
    ws.row_dimensions[1].height = 35

    ws.cell(row=2, column=1, value="Governance of test data refresh cycles and authorisations")

    headers = [
        "Refresh_ID", "Target_Environment", "Data_Sources", "Refresh_Frequency",
        "Refresh_Method", "Last_Refresh_Date", "Next_Scheduled_Refresh",
        "Authorization_Status", "Authorizer", "Authorization_Date",
        "Masking_Applied_at_Refresh", "Masking_Tool", "Data_Volume",
        "Refresh_Duration", "Refresh_Window", "Retention_Period",
        "Auto_Purge_Enabled", "Refresh_Owner", "Refresh_Log_Location", "Evidence_Reference"
    ]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    freq_dv = DataValidation(type="list", formula1='"Daily,Weekly,Bi-Weekly,Monthly,Quarterly,Ad-Hoc"')
    ws.add_data_validation(freq_dv)
    freq_dv.add('D5:D54')

    method_dv = DataValidation(type="list", formula1='"Full Copy,Incremental,Subset,Synthetic,Clone"')
    ws.add_data_validation(method_dv)
    method_dv.add('E5:E54')

    auth_dv = DataValidation(type="list", formula1='"Authorised,Pending,Unauthorised"')
    ws.add_data_validation(auth_dv)
    auth_dv.add('H5:H54')

    masking_dv = DataValidation(type="list", formula1='"Yes - Automated,Yes - Manual,Partial,No"')
    ws.add_data_validation(masking_dv)
    masking_dv.add('K5:K54')

    yn_dv = DataValidation(type="list", formula1='"Yes,No"')
    ws.add_data_validation(yn_dv)
    yn_dv.add('Q5:Q54')

    # Format input rows
    for row in range(5, 55):
        ws.cell(row=row, column=1, value=f"REF-{str(row-4).zfill(3)}")
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Summary Statistics
    ws.cell(row=57, column=1, value="REFRESH STATISTICS").font = Font(bold=True, size=12)

    summary_items = [
        ("Total Refresh Schedules", "=COUNTA(B5:B54)"),
        ("Authorised Refreshes", '=COUNTIF(H5:H54,"Authorised")'),
        ("Unauthorised Refreshes", '=COUNTIF(H5:H54,"Unauthorised")'),
        ("Daily Refreshes", '=COUNTIF(D5:D54,"Daily")'),
        ("Weekly Refreshes", '=COUNTIF(D5:D54,"Weekly")'),
        ("Masking Automated", '=COUNTIF(K5:K54,"Yes - Automated")'),
        ("No Masking at Refresh", '=COUNTIF(K5:K54,"No")'),
        ("Auto-Purge Enabled", '=COUNTIF(Q5:Q54,"Yes")'),
    ]

    row = 59
    for label, formula in summary_items:
        ws.cell(row=row, column=1, value=label).border = THIN_BORDER
        ws.cell(row=row, column=2, value=formula).border = THIN_BORDER
        row += 1

    # Column widths
    widths = [15, 25, 40, 18, 25, 15, 15, 18, 25, 15, 18, 25, 15, 15, 20, 18, 12, 25, 30, 20]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_compliance_verification_sheet(ws):
    """Create the Compliance Verification sheet."""
    ws.title = "Compliance Verification"

    ws.merge_cells('A1:R1')
    title_cell = ws.cell(row=1, column=1, value="COMPLIANCE VERIFICATION")
    title_cell.font = TITLE_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = HEADER_ALIGNMENT
    ws.row_dimensions[1].height = 35

    ws.cell(row=2, column=1, value="Documentation of compliance status and verification activities")

    headers = [
        "Requirement_ID", "Requirement_Source", "Requirement_Reference",
        "Requirement_Description", "Applicable_Data_Sets", "Applicable_Environments",
        "Compliance_Status", "Last_Verification_Date", "Verification_Method",
        "Verifier", "Findings", "Finding_Severity", "Remediation_Required",
        "Remediation_Owner", "Remediation_Target_Date", "Remediation_Status",
        "Next_Verification_Due", "Evidence_Reference"
    ]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = HEADER_ALIGNMENT
        cell.border = THIN_BORDER

    # Data validations
    source_dv = DataValidation(type="list", formula1='"GDPR,ISO 27001,FADP,Internal Policy,Industry Standard"')
    ws.add_data_validation(source_dv)
    source_dv.add('B5:B54')

    status_dv = DataValidation(type="list", formula1='"Compliant,Partial,Non-Compliant,Not Assessed"')
    ws.add_data_validation(status_dv)
    status_dv.add('G5:G54')

    method_dv = DataValidation(type="list", formula1='"Automated Check,Manual Audit,Self-Assessment,Third-Party Audit"')
    ws.add_data_validation(method_dv)
    method_dv.add('I5:I54')

    severity_dv = DataValidation(type="list", formula1='"Critical,High,Medium,Low"')
    ws.add_data_validation(severity_dv)
    severity_dv.add('L5:L54')

    yn_dv = DataValidation(type="list", formula1='"Yes,No"')
    ws.add_data_validation(yn_dv)
    yn_dv.add('M5:M54')

    rem_status_dv = DataValidation(type="list", formula1='"Not Started,In Progress,Completed"')
    ws.add_data_validation(rem_status_dv)
    rem_status_dv.add('P5:P54')

    # Pre-populate standard requirements
    requirements = [
        ("REQ-001", "GDPR", "Article 25", "Data protection by design - pseudonymization"),
        ("REQ-002", "GDPR", "Article 32", "Security of processing - technical measures"),
        ("REQ-003", "ISO 27001", "A.8.33", "Test information appropriately protected"),
        ("REQ-004", "ISO 27001", "A.8.34", "Audit testing planned and agreed"),
        ("REQ-005", "Internal Policy", "POL-2.1", "All production data copies authorised"),
        ("REQ-006", "Internal Policy", "POL-2.2", "PII must be masked in test environments"),
        ("REQ-007", "Internal Policy", "POL-2.3", "Test environments must have security controls"),
        ("REQ-008", "Internal Policy", "POL-2.4", "Data refresh must be authorised"),
        ("REQ-009", "FADP", "Article 8", "Data security requirements"),
        ("REQ-010", "Industry Standard", "PCI-DSS 6.4", "Test data security (if applicable)"),
    ]

    for row_idx, (req_id, source, ref, desc) in enumerate(requirements, 5):
        ws.cell(row=row_idx, column=1, value=req_id)
        ws.cell(row=row_idx, column=2, value=source)
        ws.cell(row=row_idx, column=3, value=ref)
        ws.cell(row=row_idx, column=4, value=desc)
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row_idx, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Additional empty rows
    for row in range(15, 55):
        ws.cell(row=row, column=1, value=f"REQ-{str(row-4).zfill(3)}")
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            cell.fill = INPUT_FILL
            cell.border = THIN_BORDER

    # Summary Statistics
    ws.cell(row=57, column=1, value="COMPLIANCE STATISTICS").font = Font(bold=True, size=12)

    summary_items = [
        ("Total Requirements", "=COUNTA(B5:B54)"),
        ("Compliant", '=COUNTIF(G5:G54,"Compliant")'),
        ("Partial", '=COUNTIF(G5:G54,"Partial")'),
        ("Non-Compliant", '=COUNTIF(G5:G54,"Non-Compliant")'),
        ("Not Assessed", '=COUNTIF(G5:G54,"Not Assessed")'),
        ("Critical Findings", '=COUNTIF(L5:L54,"Critical")'),
        ("High Findings", '=COUNTIF(L5:L54,"High")'),
    ]

    row = 59
    for label, formula in summary_items:
        ws.cell(row=row, column=1, value=label).border = THIN_BORDER
        ws.cell(row=row, column=2, value=formula).border = THIN_BORDER
        row += 1

    # Column widths
    widths = [15, 25, 25, 50, 40, 40, 18, 15, 25, 25, 50, 18, 12, 25, 15, 18, 15, 20]
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def create_summary_dashboard_sheet(ws):
    """Create the Summary Dashboard sheet."""
    ws.title = "Summary Dashboard"

    # Header (Row 1)
    ws.merge_cells("A1:G1")
    ws["A1"] = "TEST DATA PROTECTION - COMPLIANCE SUMMARY"
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
        "Test Data Inventory",
        "Data Masking Assessment",
        "Test Environment Registry",
        "Data Refresh Schedule",
        "Compliance Verification",
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
        ("Data Set Authorisation Rate", "[%]", "100%"),
        ("PII Masking Coverage", "[%]", "100%"),
        ("Average Masking Effectiveness", "[Score]", ">=4.0"),
        ("Environment Security Compliance", "[%]", ">=90%"),
        ("Refresh Authorisation Rate", "[%]", "100%"),
        ("Regulatory Compliance Rate", "[%]", "100%"),
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
        ("Unauthorised Data", "Data sets without authorisation", "[#]", "Critical", "Immediate"),
        ("Unmasked PII", "PII data without masking", "[#]", "Critical", "Urgent"),
        ("Non-Compliant Environments", "Environments failing security", "[#]", "High", "Priority"),
        ("Unauthorised Refresh", "Refresh without approval", "[#]", "High", "Priority"),
        ("Overdue Reviews", "Security reviews past due", "[#]", "Medium", "Plan"),
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
    create_test_data_inventory_sheet(wb.create_sheet())
    create_data_masking_assessment_sheet(wb.create_sheet())
    create_test_environment_registry_sheet(wb.create_sheet())
    create_data_refresh_schedule_sheet(wb.create_sheet())
    create_compliance_verification_sheet(wb.create_sheet())
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
