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
ISMS-IMP-A.5.10-11.S2 - Usage Rules Inventory Excel Generator
================================================================================

ISO/IEC 27001:2022 Control A.5.10: Acceptable Use of Information and Other
Associated Assets

Assessment Domain 2 of 4: Usage Rules Inventory

--------------------------------------------------------------------------------
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR YOUR ORGANIZATION
--------------------------------------------------------------------------------

This script generates a comprehensive Excel assessment workbook for documenting
specific usage rules by asset category, including permitted activities,
prohibited activities, and handling requirements.

**Generated Workbook Structure:**
1. Instructions - Assessment guidance and methodology
2. Usage_Rules - Master inventory of usage rules by category
3. Permitted_Activities - Detailed permitted use documentation
4. Prohibited_Activities - Explicit prohibited actions
5. Handling_Requirements - Asset handling specifications
6. Evidence_Register - Audit evidence tracking
7. Approval_SignOff - Stakeholder review and approval

================================================================================
"""

# =============================================================================
# IMPORTS - Standard Library
# =============================================================================
import logging
import sys
from datetime import datetime

# =============================================================================
# IMPORTS - Third Party
# =============================================================================
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
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
DOCUMENT_ID = "ISMS-IMP-A.5.10-11.S2"
WORKBOOK_NAME = "Usage Rules Inventory"
CONTROL_ID = "A.5.10"
CONTROL_NAME = "Acceptable Use of Information and Other Associated Assets"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

# Timestamps
GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")

# Output filename
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

# =============================================================================
# STYLE DEFINITIONS
# =============================================================================
def setup_styles():
    """Define all cell styles used throughout the workbook."""
    thin = Side(style="thin")
    border_thin = Border(left=thin, right=thin, top=thin, bottom=thin)

    styles = {
        "header": {
            "font": Font(name="Calibri", size=14, bold=True, color="FFFFFF"),
            "fill": PatternFill(start_color="003366", end_color="003366", fill_type="solid"),
            "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
        },
        "subheader": {
            "font": Font(name="Calibri", size=11, bold=True, color="FFFFFF"),
            "fill": PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid"),
            "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
        },
        "column_header": {
            "font": Font(name="Calibri", size=10, bold=True),
            "fill": PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid"),
            "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
            "border": border_thin,
        },
        "input_cell": {
            "fill": PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid"),
            "alignment": Alignment(horizontal="left", vertical="center", wrap_text=True),
            "border": border_thin,
        },
        "border": border_thin,
        "permitted": {"fill": PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")},
        "prohibited": {"fill": PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")},
        "conditional": {"fill": PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")},
    }
    return styles


# =============================================================================
# WORKBOOK CREATION
# =============================================================================
def create_workbook() -> Workbook:
    """Create workbook with all required sheets."""
    wb = Workbook()

    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])

    sheets = [
        "Instructions",
        "Usage_Rules",
        "Permitted_Activities",
        "Prohibited_Activities",
        "Handling_Requirements",
        "Evidence_Register",
        "Approval_SignOff",
    ]
    for name in sheets:
        wb.create_sheet(title=name)

    return wb


# =============================================================================
# INSTRUCTIONS SHEET
# =============================================================================
def create_instructions_sheet(ws, styles):
    """Create the Instructions sheet with assessment guidance."""
    ws.merge_cells("A1:G1")
    ws["A1"] = f"{DOCUMENT_ID} - {WORKBOOK_NAME}\n{CONTROL_REF}"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 40

    ws["A3"] = "Document Information"
    ws["A3"].font = Font(bold=True, size=12)

    doc_info = [
        ("Document ID", DOCUMENT_ID),
        ("Assessment Area", "Usage Rules Inventory by Asset Category"),
        ("Control Reference", CONTROL_ID),
        ("Version", "1.0"),
        ("Assessment Date", ""),
        ("Completed By", ""),
        ("Organisation", ""),
        ("Review Cycle", "Annual"),
    ]

    row = 4
    for label, value in doc_info:
        ws[f"A{row}"] = label
        ws[f"A{row}"].font = Font(bold=True)
        ws[f"B{row}"] = value
        if value == "":
            ws[f"B{row}"].fill = styles["input_cell"]["fill"]
            ws[f"B{row}"].border = styles["border"]
        row += 1

    row += 1
    ws[f"A{row}"] = "PURPOSE"
    ws[f"A{row}"].font = Font(bold=True, size=12)
    row += 1
    ws[f"A{row}"] = (
        "This workbook documents specific usage rules for each asset category, "
        "providing a detailed inventory of permitted activities, prohibited "
        "activities, and handling requirements to support the Acceptable Use Policy."
    )
    ws.merge_cells(f"A{row}:G{row}")

    row += 2
    ws[f"A{row}"] = "HOW TO USE THIS WORKBOOK"
    ws[f"A{row}"].font = Font(bold=True, size=12)

    instructions = [
        "1. Review Usage_Rules for master list of rules by category",
        "2. Document permitted activities in Permitted_Activities",
        "3. Document prohibited activities in Prohibited_Activities",
        "4. Define handling requirements in Handling_Requirements",
        "5. Link supporting evidence in Evidence_Register",
        "6. Obtain approvals in Approval_SignOff sheet",
    ]

    row += 1
    for line in instructions:
        ws[f"A{row}"] = line
        row += 1

    row += 1
    ws[f"A{row}"] = "ACTIVITY CLASSIFICATIONS"
    ws[f"A{row}"].font = Font(bold=True, size=12)

    classifications = [
        ("Permitted", "Activity is explicitly allowed", "Green"),
        ("Permitted with Conditions", "Allowed under specific circumstances", "Yellow"),
        ("Prohibited", "Activity is explicitly forbidden", "Red"),
        ("Not Applicable", "Rule does not apply to this category", "Grey"),
    ]

    row += 1
    for classification, desc, color in classifications:
        ws[f"A{row}"] = classification
        ws[f"A{row}"].font = Font(bold=True)
        ws[f"B{row}"] = desc
        ws[f"C{row}"] = color
        row += 1

    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 50
    ws.column_dimensions["C"].width = 15
    ws.freeze_panes = "A4"


# =============================================================================
# USAGE RULES SHEET
# =============================================================================
def create_usage_rules_sheet(ws, styles):
    """Create the Usage_Rules sheet - master inventory."""
    ws.merge_cells("A1:L1")
    ws["A1"] = "USAGE RULES INVENTORY"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30

    columns = [
        ("Rule_ID", 14),
        ("Asset_Category", 25),
        ("Rule_Description", 50),
        ("Classification", 20),
        ("Applies_To", 22),
        ("Enforcement_Method", 22),
        ("Monitoring_Required", 16),
        ("Exception_Process", 18),
        ("Policy_Reference", 20),
        ("Last_Updated", 14),
        ("Owner", 22),
        ("Notes", 30),
    ]

    for col_idx, (col_name, col_width) in enumerate(columns, start=1):
        cell = ws.cell(row=3, column=col_idx, value=col_name)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.alignment = styles["column_header"]["alignment"]
        cell.border = styles["column_header"]["border"]
        ws.column_dimensions[get_column_letter(col_idx)].width = col_width

    # Pre-populate common usage rules
    usage_rules = [
        ("UR-001", "Email", "Business email for work communications only", "Permitted with Conditions"),
        ("UR-002", "Email", "No forwarding of confidential data to personal accounts", "Prohibited"),
        ("UR-003", "Internet", "Web browsing for business research permitted", "Permitted"),
        ("UR-004", "Internet", "No access to prohibited website categories", "Prohibited"),
        ("UR-005", "Software", "Only approved software may be installed", "Permitted with Conditions"),
        ("UR-006", "Software", "No pirated or unlicensed software", "Prohibited"),
        ("UR-007", "Mobile Devices", "Corporate mobile devices for business use", "Permitted"),
        ("UR-008", "Mobile Devices", "No jailbreaking or rooting devices", "Prohibited"),
        ("UR-009", "Cloud Services", "Approved cloud services only", "Permitted with Conditions"),
        ("UR-010", "Cloud Services", "No storage of classified data in unapproved clouds", "Prohibited"),
        ("UR-011", "USB/Removable Media", "Encrypted USB drives for data transfer", "Permitted with Conditions"),
        ("UR-012", "USB/Removable Media", "No personal USB devices on corporate systems", "Prohibited"),
        ("UR-013", "Printing", "Secure printing for confidential documents", "Permitted with Conditions"),
        ("UR-014", "Remote Access", "VPN required for remote work", "Permitted with Conditions"),
        ("UR-015", "Social Media", "Personal social media on break times only", "Permitted with Conditions"),
    ]

    dv_classification = DataValidation(
        type="list",
        formula1='"Permitted,Permitted with Conditions,Prohibited,Not Applicable"',
        allow_blank=False
    )
    ws.add_data_validation(dv_classification)

    dv_monitoring = DataValidation(
        type="list",
        formula1='"Yes,No"',
        allow_blank=False
    )
    ws.add_data_validation(dv_monitoring)

    for row_idx, (rule_id, category, description, classification) in enumerate(usage_rules, start=4):
        ws.cell(row=row_idx, column=1, value=rule_id)
        ws.cell(row=row_idx, column=2, value=category)
        ws.cell(row=row_idx, column=3, value=description)
        ws.cell(row=row_idx, column=4, value=classification)

        # Color code classification
        if classification == "Permitted":
            ws.cell(row=row_idx, column=4).fill = styles["permitted"]["fill"]
        elif classification == "Prohibited":
            ws.cell(row=row_idx, column=4).fill = styles["prohibited"]["fill"]
        elif classification == "Permitted with Conditions":
            ws.cell(row=row_idx, column=4).fill = styles["conditional"]["fill"]

        for c in range(5, 13):
            cell = ws.cell(row=row_idx, column=c)
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
            cell.alignment = styles["input_cell"]["alignment"]

        dv_classification.add(ws.cell(row=row_idx, column=4))
        dv_monitoring.add(ws.cell(row=row_idx, column=7))

    # Additional blank rows
    for r in range(len(usage_rules) + 4, len(usage_rules) + 54):
        ws.cell(row=r, column=1, value=f"UR-{r-3:03d}").font = Font(color="808080")
        for c in range(2, 13):
            cell = ws.cell(row=r, column=c)
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
            cell.alignment = styles["input_cell"]["alignment"]
        dv_classification.add(ws.cell(row=r, column=4))
        dv_monitoring.add(ws.cell(row=r, column=7))

    ws.freeze_panes = "D4"


# =============================================================================
# PERMITTED ACTIVITIES SHEET
# =============================================================================
def create_permitted_activities_sheet(ws, styles):
    """Create the Permitted_Activities sheet."""
    ws.merge_cells("A1:J1")
    ws["A1"] = "PERMITTED ACTIVITIES"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30

    columns = [
        ("Activity_ID", 14),
        ("Asset_Category", 22),
        ("Permitted_Activity", 45),
        ("Conditions", 35),
        ("Approval_Required", 16),
        ("Approver_Role", 22),
        ("Time_Restrictions", 20),
        ("Location_Restrictions", 22),
        ("Documentation_Required", 20),
        ("Notes", 30),
    ]

    for col_idx, (col_name, col_width) in enumerate(columns, start=1):
        cell = ws.cell(row=3, column=col_idx, value=col_name)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.alignment = styles["column_header"]["alignment"]
        cell.border = styles["column_header"]["border"]
        ws.column_dimensions[get_column_letter(col_idx)].width = col_width

    dv_approval = DataValidation(
        type="list",
        formula1='"Yes,No"',
        allow_blank=False
    )
    ws.add_data_validation(dv_approval)

    for r in range(4, 104):
        ws.cell(row=r, column=1, value=f"PA-{r-3:03d}").font = Font(color="808080")
        for c in range(2, 11):
            cell = ws.cell(row=r, column=c)
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
            cell.alignment = styles["input_cell"]["alignment"]
        dv_approval.add(ws.cell(row=r, column=5))
        dv_approval.add(ws.cell(row=r, column=9))

    ws.freeze_panes = "C4"


# =============================================================================
# PROHIBITED ACTIVITIES SHEET
# =============================================================================
def create_prohibited_activities_sheet(ws, styles):
    """Create the Prohibited_Activities sheet."""
    ws.merge_cells("A1:J1")
    ws["A1"] = "PROHIBITED ACTIVITIES"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30

    columns = [
        ("Prohibition_ID", 14),
        ("Asset_Category", 22),
        ("Prohibited_Activity", 45),
        ("Reason", 35),
        ("Risk_Level", 14),
        ("Detection_Method", 25),
        ("Consequence", 25),
        ("Exception_Possible", 16),
        ("Related_Control", 18),
        ("Notes", 30),
    ]

    for col_idx, (col_name, col_width) in enumerate(columns, start=1):
        cell = ws.cell(row=3, column=col_idx, value=col_name)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.alignment = styles["column_header"]["alignment"]
        cell.border = styles["column_header"]["border"]
        ws.column_dimensions[get_column_letter(col_idx)].width = col_width

    # Pre-populate common prohibitions
    prohibitions = [
        ("PH-001", "All Assets", "Sharing credentials with others", "Security breach risk", "Critical"),
        ("PH-002", "All Assets", "Disabling security controls", "Compliance violation", "Critical"),
        ("PH-003", "Email", "Sending unencrypted sensitive data externally", "Data breach risk", "High"),
        ("PH-004", "Software", "Installing unauthorised software", "Malware risk", "High"),
        ("PH-005", "Internet", "Accessing illegal or inappropriate content", "Legal/HR risk", "High"),
        ("PH-006", "Data", "Storing classified data on personal devices", "Data loss risk", "Critical"),
        ("PH-007", "Network", "Connecting unauthorised devices to network", "Security risk", "High"),
        ("PH-008", "Cloud", "Using unapproved cloud storage services", "Data governance", "High"),
    ]

    dv_risk = DataValidation(
        type="list",
        formula1='"Critical,High,Medium,Low"',
        allow_blank=False
    )
    ws.add_data_validation(dv_risk)

    dv_exception = DataValidation(
        type="list",
        formula1='"Yes,No"',
        allow_blank=False
    )
    ws.add_data_validation(dv_exception)

    for row_idx, (p_id, category, activity, reason, risk) in enumerate(prohibitions, start=4):
        ws.cell(row=row_idx, column=1, value=p_id)
        ws.cell(row=row_idx, column=2, value=category)
        ws.cell(row=row_idx, column=3, value=activity)
        ws.cell(row=row_idx, column=4, value=reason)
        ws.cell(row=row_idx, column=5, value=risk)

        for c in range(6, 11):
            cell = ws.cell(row=row_idx, column=c)
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
            cell.alignment = styles["input_cell"]["alignment"]

        dv_risk.add(ws.cell(row=row_idx, column=5))
        dv_exception.add(ws.cell(row=row_idx, column=8))

    for r in range(len(prohibitions) + 4, len(prohibitions) + 54):
        ws.cell(row=r, column=1, value=f"PH-{r-3:03d}").font = Font(color="808080")
        for c in range(2, 11):
            cell = ws.cell(row=r, column=c)
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
            cell.alignment = styles["input_cell"]["alignment"]
        dv_risk.add(ws.cell(row=r, column=5))
        dv_exception.add(ws.cell(row=r, column=8))

    ws.freeze_panes = "C4"


# =============================================================================
# HANDLING REQUIREMENTS SHEET
# =============================================================================
def create_handling_requirements_sheet(ws, styles):
    """Create the Handling_Requirements sheet."""
    ws.merge_cells("A1:K1")
    ws["A1"] = "ASSET HANDLING REQUIREMENTS"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30

    columns = [
        ("Handling_ID", 14),
        ("Asset_Category", 22),
        ("Data_Classification", 18),
        ("Storage_Requirement", 30),
        ("Transmission_Requirement", 30),
        ("Disposal_Requirement", 30),
        ("Access_Restriction", 25),
        ("Labelling_Required", 16),
        ("Encryption_Required", 16),
        ("Retention_Period", 18),
        ("Notes", 30),
    ]

    for col_idx, (col_name, col_width) in enumerate(columns, start=1):
        cell = ws.cell(row=3, column=col_idx, value=col_name)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.alignment = styles["column_header"]["alignment"]
        cell.border = styles["column_header"]["border"]
        ws.column_dimensions[get_column_letter(col_idx)].width = col_width

    dv_classification = DataValidation(
        type="list",
        formula1='"Public,Internal,Confidential,Restricted"',
        allow_blank=False
    )
    ws.add_data_validation(dv_classification)

    dv_yesno = DataValidation(
        type="list",
        formula1='"Yes,No"',
        allow_blank=False
    )
    ws.add_data_validation(dv_yesno)

    for r in range(4, 54):
        ws.cell(row=r, column=1, value=f"HR-{r-3:03d}").font = Font(color="808080")
        for c in range(2, 12):
            cell = ws.cell(row=r, column=c)
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
            cell.alignment = styles["input_cell"]["alignment"]
        dv_classification.add(ws.cell(row=r, column=3))
        dv_yesno.add(ws.cell(row=r, column=8))
        dv_yesno.add(ws.cell(row=r, column=9))

    ws.freeze_panes = "C4"


# =============================================================================
# EVIDENCE REGISTER SHEET
# =============================================================================
def create_evidence_register_sheet(ws, styles):
    """Create the Evidence_Register sheet."""
    ws.merge_cells("A1:H1")
    ws["A1"] = "EVIDENCE REGISTER"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30

    columns = [
        ("Evidence_ID", 15),
        ("Evidence_Type", 22),
        ("Description", 45),
        ("Related_Rule", 20),
        ("Collection_Date", 16),
        ("Location", 40),
        ("Collected_By", 25),
        ("Valid_Until", 16),
    ]

    for col_idx, (col_name, col_width) in enumerate(columns, start=1):
        cell = ws.cell(row=3, column=col_idx, value=col_name)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.alignment = styles["column_header"]["alignment"]
        cell.border = styles["column_header"]["border"]
        ws.column_dimensions[get_column_letter(col_idx)].width = col_width

    dv_type = DataValidation(
        type="list",
        formula1='"Policy Document,Configuration,Screenshot,Export,Training Record,Attestation"',
        allow_blank=False
    )
    ws.add_data_validation(dv_type)

    for r in range(4, 54):
        ws.cell(row=r, column=1, value=f"EV-{r-3:03d}").font = Font(color="808080")
        for c in range(2, 9):
            cell = ws.cell(row=r, column=c)
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
            cell.alignment = styles["input_cell"]["alignment"]
        dv_type.add(ws.cell(row=r, column=2))

    ws.freeze_panes = "C4"


# =============================================================================
# APPROVAL SIGN-OFF SHEET
# =============================================================================
def create_approval_signoff_sheet(ws, styles):
    """Create the Approval_SignOff sheet."""
    ws.merge_cells("A1:E1")
    ws["A1"] = "ASSESSMENT APPROVAL AND SIGN-OFF"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 30

    row = 3
    ws[f"A{row}"] = "Assessment Summary"
    ws[f"A{row}"].font = Font(bold=True, size=12)

    summary_fields = [
        ("Assessment Document", f"{DOCUMENT_ID} - {WORKBOOK_NAME}"),
        ("Assessment Period", ""),
        ("Total Usage Rules Documented", "=COUNTA(Usage_Rules!A4:A68)-COUNTBLANK(Usage_Rules!B4:B68)"),
        ("Permitted Activities Documented", "=COUNTA(Permitted_Activities!A4:A103)-COUNTBLANK(Permitted_Activities!B4:B103)"),
        ("Prohibited Activities Documented", "=COUNTA(Prohibited_Activities!A4:A61)-COUNTBLANK(Prohibited_Activities!B4:B61)"),
        ("Handling Requirements Defined", "=COUNTA(Handling_Requirements!A4:A53)-COUNTBLANK(Handling_Requirements!B4:B53)"),
        ("Assessment Status", ""),
    ]

    row += 1
    for label, value in summary_fields:
        ws[f"A{row}"] = label
        ws[f"A{row}"].font = Font(bold=True)
        ws[f"B{row}"] = value
        if value == "" or (isinstance(value, str) and not value.startswith("=")):
            ws[f"B{row}"].fill = styles["input_cell"]["fill"]
            ws[f"B{row}"].border = styles["border"]
        row += 1

    row += 2
    ws.merge_cells(f"A{row}:E{row}")
    ws[f"A{row}"] = "ASSESSMENT COMPLETED BY"
    ws[f"A{row}"].font = Font(bold=True, size=11, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")

    completion_fields = ["Name", "Role/Title", "Department", "Email", "Date"]
    row += 1
    for field in completion_fields:
        ws[f"A{row}"] = field + ":"
        ws[f"A{row}"].font = Font(bold=True)
        ws.merge_cells(f"B{row}:E{row}")
        ws[f"B{row}"].fill = styles["input_cell"]["fill"]
        ws[f"B{row}"].border = styles["border"]
        row += 1

    row += 2
    ws.merge_cells(f"A{row}:E{row}")
    ws[f"A{row}"] = "REVIEWED BY (Information Security Manager)"
    ws[f"A{row}"].font = Font(bold=True, size=11, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")

    row += 1
    for field in ["Name", "Date", "Signature"]:
        ws[f"A{row}"] = field + ":"
        ws[f"A{row}"].font = Font(bold=True)
        ws.merge_cells(f"B{row}:E{row}")
        ws[f"B{row}"].fill = styles["input_cell"]["fill"]
        ws[f"B{row}"].border = styles["border"]
        row += 1

    row += 2
    ws.merge_cells(f"A{row}:E{row}")
    ws[f"A{row}"] = "APPROVED BY (CISO)"
    ws[f"A{row}"].font = Font(bold=True, size=11, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")

    row += 1
    for field in ["Name", "Date", "Approval Decision", "Signature"]:
        ws[f"A{row}"] = field + ":"
        ws[f"A{row}"].font = Font(bold=True)
        ws.merge_cells(f"B{row}:E{row}")
        ws[f"B{row}"].fill = styles["input_cell"]["fill"]
        ws[f"B{row}"].border = styles["border"]
        row += 1

    dv_decision = DataValidation(
        type="list",
        formula1='"Approved,Approved with conditions,Rejected"',
        allow_blank=False
    )
    ws.add_data_validation(dv_decision)
    dv_decision.add(ws[f"B{row-2}"])

    ws.column_dimensions["A"].width = 35
    ws.column_dimensions["B"].width = 35
    ws.freeze_panes = "A3"


# =============================================================================
# MAIN EXECUTION
# =============================================================================
def main() -> int:
    """Main execution function."""
    logger.info("=" * 78)
    logger.info(f"{DOCUMENT_ID} - {WORKBOOK_NAME} Generator")
    logger.info(CONTROL_REF)
    logger.info("=" * 78)

    try:
        wb = create_workbook()
        styles = setup_styles()

        logger.info("[1/7] Creating Instructions sheet...")
        create_instructions_sheet(wb["Instructions"], styles)

        logger.info("[2/7] Creating Usage_Rules sheet...")
        create_usage_rules_sheet(wb["Usage_Rules"], styles)

        logger.info("[3/7] Creating Permitted_Activities sheet...")
        create_permitted_activities_sheet(wb["Permitted_Activities"], styles)

        logger.info("[4/7] Creating Prohibited_Activities sheet...")
        create_prohibited_activities_sheet(wb["Prohibited_Activities"], styles)

        logger.info("[5/7] Creating Handling_Requirements sheet...")
        create_handling_requirements_sheet(wb["Handling_Requirements"], styles)

        logger.info("[6/7] Creating Evidence_Register sheet...")
        create_evidence_register_sheet(wb["Evidence_Register"], styles)

        logger.info("[7/7] Creating Approval_SignOff sheet...")
        create_approval_signoff_sheet(wb["Approval_SignOff"], styles)

        wb.save(OUTPUT_FILENAME)

        logger.info("SUCCESS: %s", OUTPUT_FILENAME)
        logger.info("=" * 78)
        return 0

    except ImportError as e:
        logger.error("Missing dependency: %s", e)
        return 1
    except PermissionError as e:
        logger.error("Permission denied: %s", e)
        return 1
    except Exception as e:
        logger.error("Unexpected error: %s", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())


# =============================================================================
# END OF SCRIPT
# =============================================================================
# =============================================================================
# QA_VERIFIED: 2026-02-01
# QA_STATUS: PASSED
# QA_TOOL: Claude Code
# CHANGES: Initial creation per ISMS-IMP-A.5.10-11.S2 specification
# =============================================================================
