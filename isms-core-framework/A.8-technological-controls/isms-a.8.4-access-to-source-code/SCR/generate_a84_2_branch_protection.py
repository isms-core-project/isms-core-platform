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
ISMS-IMP-A.8.4.2 - Branch Protection Assessment Excel Generator
================================================================================

ISO/IEC 27001:2022 Control A.8.4: Access to Source Code
Assessment Domain 2 of 3: Branch Protection & Code Review

--------------------------------------------------------------------------------
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR YOUR ORGANIZATION
--------------------------------------------------------------------------------

This script is a TEMPLATE/SAMPLE implementation and MUST be adapted to match
your organization's specific branching strategy, code review requirements,
and CI/CD pipeline configuration.

Key customization areas:
1. Branch protection rules (main, release branch requirements)
2. Code review requirements (approver counts, CODEOWNERS)
3. CI/CD gate requirements (build, test, security scans)
4. Merge policies (squash, rebase per your standards)
5. Bypass policies (emergency procedures, audit requirements)

DO NOT use this script without reviewing and adapting all sections marked
with "# CUSTOMIZE:" comments throughout the code.

Reference Pattern: Based on ISMS-A.8.24 Assessment Framework (adapted for source code)

--------------------------------------------------------------------------------
DESCRIPTION
--------------------------------------------------------------------------------

**Purpose:**
Enables systematic assessment of branch protection controls and code review
practices supporting ISO 27001:2022 Control A.8.4 requirements.

**Assessment Scope:**
- Branch protection rule inventory
- Required review configuration
- Status check and CI/CD gate requirements
- Direct push restriction verification
- Force push and deletion protection
- CODEOWNERS configuration
- Bypass policy and audit trail
- Gap analysis and remediation planning
- Evidence collection for audit readiness

**Generated Workbook Structure:**
1. Instructions & Legend - Assessment guidance
2. Branch Protection Rules - Configuration inventory
3. Code Review Requirements - Reviewer configuration
4. CI/CD Gates - Build and test requirements
5. Push Restrictions - Direct commit controls
6. CODEOWNERS - Ownership configuration
7. Bypass Audit - Emergency access tracking
8. Gap Analysis - Protection deficiencies
9. Evidence Register - Audit evidence tracking
10. Approval & Sign-Off - Stakeholder approval

--------------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------------

Basic Usage:
    python3 generate_a84_2_branch_protection.py

Requirements:
    - Python 3.8+
    - openpyxl library: pip install openpyxl

Output:
    ISMS-A84-2-Branch-Protection-Assessment.xlsx
"""

# =============================================================================
# Standard Library Imports
# =============================================================================
import logging
import sys
from datetime import datetime, timedelta
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

# =============================================================================
# Logging Configuration
# =============================================================================
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)







# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.8.4.2"
WORKBOOK_NAME = "Branch Protection Assessment"
CONTROL_ID = "A.8.4"
CONTROL_NAME = "Access to Source Code"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

# Timestamps
GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")      # For display (Swiss format)
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")   # For filenames (sortable)

# Output filename
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

# ============================================================================
# UNICODE SYMBOLS - PROPER UTF-8 ENCODING
# ============================================================================

CHECK = '\u2705'      # f"{CHECK}" Green checkmark
XMARK = '\u274C'      # f"{XMARK}" Red X
WARNING = '\u26A0'    # f"{WARNING}"  Warning sign
HOURGLASS = '\u23F3'  # f"{HOURGLASS}" Hourglass
BULLET = '\u2022'     # • Bullet point
ARROW = '\u2192'      # → Right arrow
QUESTION = '\u2753'   # f"{QUESTION}" Question mark
CALENDAR = '\u1F4C5' # f"{CALENDAR}" Calendar
CHECKMARK = '\u2714'  # f"{CHECKMARK}"  Check mark
MINUS = '\u2796'      # f"{MINUS}" Minus
CHART = '\U0001F4CA' # f"{CHART}" Chart
TARGET = '\U0001F3AF' # f"{TARGET}" Target

# ============================================================================
# SECTION 1: WORKBOOK CREATION & STYLE DEFINITIONS
# ============================================================================

def create_workbook() -> Workbook:
    """Create workbook with all required sheets."""
    wb = Workbook()

    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])

    sheets = [
        "Instructions & Legend",
        "Repository_Branch_Inventory",
        "Branch_Protection_Details",
        "Pull_Request_Configuration",
        "Status_Check_Verification",
        "Signed_Commits_Audit",
        "Exception_Management",
        "Compliance_Scoring",
        "Gap_Analysis",
        "Evidence_Register",
        "Approval_Sign_Off",
    ]
    for name in sheets:
        wb.create_sheet(title=name)

    return wb


def setup_styles():
    """Define all cell styles."""
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
        "data_cell": {
            "alignment": Alignment(horizontal="left", vertical="center", wrap_text=True),
            "border": border_thin,
        },
    }
    return styles


def apply_style(cell, style_dict):
    """Apply style dictionary to a cell."""
    if "font" in style_dict:
        cell.font = Font(
            name=style_dict["font"].name,
            size=style_dict["font"].size,
            bold=style_dict["font"].bold,
            color=style_dict["font"].color if hasattr(style_dict["font"], 'color') else None
        )
    if "fill" in style_dict:
        cell.fill = PatternFill(
            start_color=style_dict["fill"].start_color.rgb if hasattr(style_dict["fill"].start_color, 'rgb') else style_dict["fill"].start_color,
            end_color=style_dict["fill"].end_color.rgb if hasattr(style_dict["fill"].end_color, 'rgb') else style_dict["fill"].end_color,
            fill_type=style_dict["fill"].fill_type
        )
    if "alignment" in style_dict:
        cell.alignment = Alignment(
            horizontal=style_dict["alignment"].horizontal,
            vertical=style_dict["alignment"].vertical,
            wrap_text=style_dict["alignment"].wrap_text
        )
    if "border" in style_dict:
        thin = Side(style="thin")
        cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)


# ============================================================================
# SECTION 2: DATA VALIDATIONS
# ============================================================================

def create_base_validations(ws):
    """Create data validation objects for standard dropdowns."""
    
    validations = {
        'platform': DataValidation(
            type="list",
            formula1='"GitHub,GitLab,Bitbucket,Azure DevOps,Self-Hosted,Other"',
            allow_blank=False
        ),
        'classification': DataValidation(
            type="list",
            formula1='"Production Code,Internal Tools,Open Source,Archived"',
            allow_blank=False
        ),
        'branch_type': DataValidation(
            type="list",
            formula1='"Main,Release,Development,Feature,Hotfix"',
            allow_blank=False
        ),
        'yesno': DataValidation(
            type="list",
            formula1=f'"{CHECK} Yes,❌ No,⚠️ Partial,➖ N/A"',
            allow_blank=False
        ),
        'compliance': DataValidation(
            type="list",
            formula1=f'"{CHECK} Compliant,⚠️ Partial,❌ Non-Compliant"',
            allow_blank=False
        ),
        'status': DataValidation(
            type="list",
            formula1='"🟢 Active,🔴 Expired,⚪ Revoked"',
            allow_blank=False
        ),
        'implementation': DataValidation(
            type="list",
            formula1=f'"{CHECK} Implemented,⚠️ Partial,❌ Missing,➖ N/A"',
            allow_blank=False
        ),
        'training': DataValidation(
            type="list",
            formula1=f'"{CHECK} Completed,⚠️ In Progress,❌ Not Started"',
            allow_blank=False
        ),
    }
    
    return validations


# ============================================================================
# SECTION 3: SHEET 1 - INSTRUCTIONS & LEGEND
# ============================================================================

def create_instructions_sheet(wb, styles):
    """Create the Instructions & Legend sheet."""
    ws = wb["Instructions & Legend"]
    
    ws.merge_cells('A1:F1')
    cell = ws['A1']
    cell.value = "ISMS-IMP-A.8.4.2 – Branch Protection Assessment"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 40
    
    ws.merge_cells('A2:F2')
    cell = ws['A2']
    cell.value = "ISO/IEC 27001:2022 - Control A.8.4: Access to Source Code"
    apply_style(cell, styles['subheader'])
    ws.row_dimensions[2].height = 25
    
    row = 4
    doc_info = [
        ("Document ID:", "ISMS-IMP-A.8.4.2"),
        ("Assessment Area:", "Branch Protection Compliance"),
        ("Related Policy:", "ISMS-POL-A.8.4-S2.4"),
        ("Version:", "1.0"),
        ("Assessment Date:", "[ENTER DATE]"),
        ("Completed By:", "[ENTER NAME]"),
        ("Organisation:", "[ENTER ORGANIZATION]"),
        ("Review Cycle:", "Quarterly"),
    ]
    
    for label, value in doc_info:
        ws[f'A{row}'] = label
        ws[f'B{row}'] = value
        ws[f'A{row}'].font = Font(bold=True)
        if value.startswith("["):
            apply_style(ws[f'B{row}'], styles['input_cell'])
        row += 1
    
    row += 2
    ws.merge_cells(f'A{row}:F{row}')
    cell = ws[f'A{row}']
    cell.value = "HOW TO USE THIS WORKBOOK"
    cell.font = Font(name="Calibri", size=12, bold=True, color="FFFFFF")
    cell.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    
    row += 1
    instructions = [
        "1. Complete Repository_Branch_Inventory for all branches requiring protection",
        "2. Document protection rules in Branch_Protection_Details",
        "3. Assess pull request configuration in Pull_Request_Configuration",
        "4. Verify status checks in Status_Check_Verification",
        "5. Track signed commits in Signed_Commits_Audit",
        "6. Document exceptions in Exception_Management",
        "7. Review Compliance_Scoring for automated metrics",
        "8. Identify gaps in Gap_Analysis and create remediation plans",
    ]
    for instruction in instructions:
        ws[f'A{row}'] = instruction
        ws[f'A{row}'].alignment = Alignment(wrap_text=True)
        row += 1
    
    row += 2
    ws.merge_cells(f'A{row}:F{row}')
    cell = ws[f'A{row}']
    cell.value = "STATUS LEGEND"
    cell.font = Font(name="Calibri", size=12, bold=True, color="FFFFFF")
    cell.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    
    row += 1
    ws[f'A{row}'] = "Symbol"
    ws[f'B{row}'] = "Status"
    ws[f'C{row}'] = "Description"
    for col in ['A', 'B', 'C']:
        ws[f'{col}{row}'].font = Font(bold=True)
        ws[f'{col}{row}'].fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
    
    row += 1
    legend_data = [
        ("{CHECK}", "Compliant", "Protection correctly configured"),
        ("{WARNING}", "Partial", "Some protection rules missing"),
        ("{XMARK}", "Non-Compliant", "Protection not configured"),
        (f"{MINUS}", "N/A", "Not applicable to this repository"),
    ]
    for symbol, status, description in legend_data:
        ws[f'A{row}'] = symbol
        ws[f'A{row}'].alignment = Alignment(horizontal="center")
        ws[f'B{row}'] = status
        ws[f'C{row}'] = description
        row += 1
    
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 30
    ws.column_dimensions['C'].width = 50


# ============================================================================
# SECTION 4: SHEET 2 - REPOSITORY BRANCH INVENTORY
# ============================================================================

def create_branch_inventory_sheet(wb, styles, validations):
    """Create Repository_Branch_Inventory sheet."""
    ws = wb["Repository_Branch_Inventory"]
    
    ws.merge_cells('A1:H1')
    cell = ws['A1']
    cell.value = "REPOSITORY BRANCH INVENTORY"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells('A2:H2')
    cell = ws['A2']
    cell.value = "Document all branches requiring protection"
    apply_style(cell, styles['subheader'])
    
    headers = [
        "Repository Name",
        "Repository Platform",
        "Repository Classification",
        "Branch Name",
        "Branch Type",
        "Protection Required",
        "Protection Configured",
        "Status",
    ]
    
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    widths = [30, 20, 25, 25, 18, 20, 22, 18]
    for idx, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = width
    
    ws.add_data_validation(validations['platform'])
    validations['platform'].add('B5:B500')
    
    ws.add_data_validation(validations['classification'])
    validations['classification'].add('C5:C500')
    
    ws.add_data_validation(validations['branch_type'])
    validations['branch_type'].add('E5:E500')
    
    ws.add_data_validation(validations['yesno'])
    validations['yesno'].add('F5:F500')
    validations['yesno'].add('G5:G500')
    
    ws.add_data_validation(validations['compliance'])
    validations['compliance'].add('H5:H500')
    
    row = 4
    ws[f'A{row}'] = "[Example: customer-portal]"
    ws[f'B{row}'] = "GitHub"
    ws[f'C{row}'] = "Production Code"
    ws[f'D{row}'] = "main"
    ws[f'E{row}'] = "Main"
    ws[f'F{row}'] = f"{CHECK} Yes"
    ws[f'G{row}'] = f"{CHECK} Yes"
    ws[f'H{row}'] = f"{CHECK} Compliant"
    
    for col in range(1, 9):
        apply_style(ws.cell(row=row, column=col), styles['input_cell'])


# ============================================================================
# SECTION 5: SHEET 3 - BRANCH PROTECTION DETAILS
# ============================================================================

def create_protection_details_sheet(wb, styles, validations):
    """Create Branch_Protection_Details sheet."""
    ws = wb["Branch_Protection_Details"]
    
    ws.merge_cells('A1:M1')
    cell = ws['A1']
    cell.value = "BRANCH PROTECTION DETAILS"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells('A2:M2')
    cell = ws['A2']
    cell.value = "Document specific protection rules for each branch"
    apply_style(cell, styles['subheader'])
    
    headers = [
        "Repository Name",
        "Branch Name",
        "Direct Commits Blocked",
        "Pull Request Required",
        "Required Approvals",
        "Dismiss Stale Reviews",
        "Code Owner Review",
        "Status Checks Required",
        "Status Check List",
        "Signed Commits Required",
        "Linear History",
        "Compliance Score (%)",
        "Status",
    ]
    
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    widths = [25, 20, 22, 22, 18, 22, 22, 22, 35, 25, 18, 20, 18]
    for idx, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = width
    
    ws.add_data_validation(validations['yesno'])
    for col in ['C', 'D', 'F', 'G', 'H', 'J', 'K']:
        validations['yesno'].add(f'{col}5:{col}500')
    
    ws.add_data_validation(validations['compliance'])
    validations['compliance'].add('M5:M500')
    
    row = 4
    ws[f'A{row}'] = "[Example: customer-portal]"
    ws[f'B{row}'] = "main"
    ws[f'C{row}'] = f"{CHECK} Yes"
    ws[f'D{row}'] = f"{CHECK} Yes"
    ws[f'E{row}'] = "2"
    ws[f'F{row}'] = f"{CHECK} Yes"
    ws[f'G{row}'] = f"{CHECK} Yes"
    ws[f'H{row}'] = f"{CHECK} Yes"
    ws[f'I{row}'] = "[Example: build, test, security-scan]"
    ws[f'J{row}'] = f"{CHECK} Yes"
    ws[f'K{row}'] = f"{CHECK} Yes"
    ws[f'L{row}'] = f'=((COUNTIF(C{row}:K{row},"{CHECK} Yes")/9)*100)'
    ws[f'L{row}'].number_format = '0.0"%"'
    ws[f'M{row}'] = f"{CHECK} Compliant"
    
    for col in range(1, 14):
        apply_style(ws.cell(row=row, column=col), styles['input_cell'])


# ============================================================================
# SECTION 6: SHEET 4 - PULL REQUEST CONFIGURATION
# ============================================================================

def create_pr_configuration_sheet(wb, styles, validations):
    """Create Pull_Request_Configuration sheet."""
    ws = wb["Pull_Request_Configuration"]
    
    ws.merge_cells('A1:H1')
    cell = ws['A1']
    cell.value = "PULL REQUEST CONFIGURATION"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells('A2:H2')
    cell = ws['A2']
    cell.value = "Assess pull request workflow configuration"
    apply_style(cell, styles['subheader'])
    
    headers = [
        "Repository Name",
        "Minimum Reviewers",
        "Code Owner Review",
        "Dismiss Stale Approvals",
        "Restrict Dismiss",
        "Conversation Resolution",
        "Self-Approval Blocked",
        "Compliance Status",
    ]
    
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    widths = [30, 18, 22, 25, 20, 25, 25, 20]
    for idx, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = width
    
    dv_codeowner = DataValidation(
        type="list",
        formula1=f'"{CHECK} Required,⚠️ Optional,❌ No"',
        allow_blank=False
    )
    ws.add_data_validation(dv_codeowner)
    dv_codeowner.add('C5:C500')
    
    ws.add_data_validation(validations['yesno'])
    for col in ['D', 'E', 'F', 'G']:
        validations['yesno'].add(f'{col}5:{col}500')
    
    ws.add_data_validation(validations['compliance'])
    validations['compliance'].add('H5:H500')
    
    row = 4
    ws[f'A{row}'] = "[Example: customer-portal]"
    ws[f'B{row}'] = "2"
    ws[f'C{row}'] = f"{CHECK} Required"
    ws[f'D{row}'] = f"{CHECK} Yes"
    ws[f'E{row}'] = f"{CHECK} Yes"
    ws[f'F{row}'] = f"{CHECK} Yes"
    ws[f'G{row}'] = f"{CHECK} Yes"
    ws[f'H{row}'] = f"{CHECK} Compliant"
    
    for col in range(1, 9):
        apply_style(ws.cell(row=row, column=col), styles['input_cell'])


# ============================================================================
# SECTION 7: SHEET 5 - STATUS CHECK VERIFICATION
# ============================================================================

def create_status_check_sheet(wb, styles, validations):
    """Create Status_Check_Verification sheet."""
    ws = wb["Status_Check_Verification"]
    
    ws.merge_cells('A1:I1')
    cell = ws['A1']
    cell.value = "STATUS CHECK VERIFICATION"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells('A2:I2')
    cell = ws['A2']
    cell.value = "Document CI/CD status checks"
    apply_style(cell, styles['subheader'])
    
    headers = [
        "Repository Name",
        "Status Checks Configured",
        "Build Check",
        "Test Check",
        "Lint Check",
        "Security Check",
        "All Checks Must Pass",
        "Up-to-Date Before Merge",
        "Compliance Status",
    ]
    
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    widths = [30, 23, 18, 18, 18, 18, 22, 25, 20]
    for idx, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = width
    
    dv_configured = DataValidation(
        type="list",
        formula1=f'"{CHECK} Configured,❌ Missing,➖ N/A"',
        allow_blank=False
    )
    ws.add_data_validation(dv_configured)
    for col in ['C', 'D', 'E', 'F']:
        dv_configured.add(f'{col}5:{col}500')
    
    ws.add_data_validation(validations['yesno'])
    validations['yesno'].add('B5:B500')
    validations['yesno'].add('G5:G500')
    validations['yesno'].add('H5:H500')
    
    ws.add_data_validation(validations['compliance'])
    validations['compliance'].add('I5:I500')
    
    row = 4
    ws[f'A{row}'] = "[Example: customer-portal]"
    ws[f'B{row}'] = f"{CHECK} Yes"
    ws[f'C{row}'] = f"{CHECK} Configured"
    ws[f'D{row}'] = f"{CHECK} Configured"
    ws[f'E{row}'] = f"{CHECK} Configured"
    ws[f'F{row}'] = f"{CHECK} Configured"
    ws[f'G{row}'] = f"{CHECK} Yes"
    ws[f'H{row}'] = f"{CHECK} Yes"
    ws[f'I{row}'] = f"{CHECK} Compliant"
    
    for col in range(1, 10):
        apply_style(ws.cell(row=row, column=col), styles['input_cell'])


# ============================================================================
# SECTION 8: SHEET 6 - SIGNED COMMITS AUDIT
# ============================================================================

def create_signed_commits_sheet(wb, styles, validations):
    """Create Signed_Commits_Audit sheet."""
    ws = wb["Signed_Commits_Audit"]
    
    ws.merge_cells('A1:F1')
    cell = ws['A1']
    cell.value = "SIGNED COMMITS AUDIT"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells('A2:F2')
    cell = ws['A2']
    cell.value = "Track signed commit adoption"
    apply_style(cell, styles['subheader'])
    
    headers = [
        "Repository Name",
        "Signed Commits Required",
        "% Commits Signed (30 days)",
        "GPG Infrastructure",
        "Developer Training",
        "Compliance Status",
    ]
    
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    widths = [30, 25, 25, 25, 25, 20]
    for idx, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = width
    
    ws.add_data_validation(validations['yesno'])
    validations['yesno'].add('B5:B500')
    
    ws.add_data_validation(validations['implementation'])
    validations['implementation'].add('D5:D500')
    
    ws.add_data_validation(validations['training'])
    validations['training'].add('E5:E500')
    
    ws.add_data_validation(validations['compliance'])
    validations['compliance'].add('F5:F500')
    
    row = 4
    ws[f'A{row}'] = "[Example: customer-portal]"
    ws[f'B{row}'] = f"{CHECK} Yes"
    ws[f'C{row}'] = "85"
    ws[f'C{row}'].number_format = '0"%"'
    ws[f'D{row}'] = f"{CHECK} Implemented"
    ws[f'E{row}'] = f"{CHECK} Completed"
    ws[f'F{row}'] = f"{CHECK} Compliant"
    
    for col in range(1, 7):
        apply_style(ws.cell(row=row, column=col), styles['input_cell'])


# ============================================================================
# SECTION 9: SHEET 7 - EXCEPTION MANAGEMENT
# ============================================================================

def create_exception_management_sheet(wb, styles, validations):
    """Create Exception_Management sheet."""
    ws = wb["Exception_Management"]
    
    ws.merge_cells('A1:H1')
    cell = ws['A1']
    cell.value = "EXCEPTION MANAGEMENT"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells('A2:H2')
    cell = ws['A2']
    cell.value = "Track branch protection exceptions"
    apply_style(cell, styles['subheader'])
    
    headers = [
        "Exception ID",
        "Repository/Branch",
        "Exception Reason",
        "Granted By",
        "Grant Date",
        "Expiration Date",
        "Review Date",
        "Status",
    ]
    
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    widths = [15, 30, 40, 25, 15, 18, 15, 15]
    for idx, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = width
    
    ws.add_data_validation(validations['status'])
    validations['status'].add('H5:H500')
    
    row = 4
    ws[f'A{row}'] = "EXC-001"
    ws[f'B{row}'] = "[Example: legacy-app/main]"
    ws[f'C{row}'] = "[Example: Repository in decommission process]"
    ws[f'D{row}'] = "[Example: CISO]"
    ws[f'E{row}'] = datetime.now().strftime("%d.%m.%Y")
    ws[f'F{row}'] = (datetime.now() + timedelta(days=90)).strftime("%d.%m.%Y")
    ws[f'G{row}'] = (datetime.now() + timedelta(days=30)).strftime("%d.%m.%Y")
    ws[f'H{row}'] = "🟢 Active"
    
    for col in range(1, 9):
        apply_style(ws.cell(row=row, column=col), styles['input_cell'])


# ============================================================================
# SECTION 10: SHEET 8 - COMPLIANCE SCORING
# ============================================================================

def create_compliance_scoring_sheet(wb, styles):
    """Create Compliance_Scoring sheet."""
    ws = wb["Compliance_Scoring"]
    
    ws.merge_cells('A1:E1')
    cell = ws['A1']
    cell.value = "BRANCH PROTECTION COMPLIANCE SCORING"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 40
    
    ws.merge_cells('A2:E2')
    cell = ws['A2']
    cell.value = "Automated metrics based on assessment data"
    apply_style(cell, styles['subheader'])
    
    row = 4
    ws.merge_cells(f'A{row}:E{row}')
    cell = ws[f'A{row}']
    cell.value = "COMPLIANCE METRICS"
    cell.font = Font(name="Calibri", size=12, bold=True, color="FFFFFF")
    cell.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    cell.alignment = Alignment(horizontal="center")
    
    row += 1
    headers = ["Metric", "Current Score", "Target", "Status", "Weight"]
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    row += 1
    metrics = [
        ("Branch Protection Configuration Rate",
         f'=COUNTIFS(Branch_Protection_Details!M:M,"{CHECK} Compliant")/COUNTA(Branch_Protection_Details!M:M)*100',
         "100%", "", "40%"),
        ("Pull Request Enforcement Rate",
         f'=COUNTIFS(Pull_Request_Configuration!H:H,"{CHECK} Compliant")/COUNTA(Pull_Request_Configuration!H:H)*100',
         "≥95%", "", "30%"),
        ("Status Check Compliance Rate",
         f'=COUNTIFS(Status_Check_Verification!I:I,"{CHECK} Compliant")/COUNTA(Status_Check_Verification!I:I)*100',
         "100%", "", "20%"),
        ("Signed Commit Adoption Rate",
         "=AVERAGE(Signed_Commits_Audit!C:C)",
         "≥80%", "", "10%"),
    ]
    
    for metric, formula, target, status, weight in metrics:
        ws[f'A{row}'] = metric
        ws[f'B{row}'] = formula
        ws[f'C{row}'] = target
        ws[f'D{row}'] = ""
        ws[f'E{row}'] = weight
        ws[f'B{row}'].number_format = '0.0"%"'
        row += 1
    
    row += 1
    ws[f'A{row}'] = "OVERALL BRANCH PROTECTION SCORE"
    ws[f'A{row}'].font = Font(bold=True, size=12)
    ws[f'B{row}'] = "=B6*0.40+B7*0.30+B8*0.20+B9*0.10"
    ws[f'B{row}'].font = Font(bold=True, size=12)
    ws[f'B{row}'].number_format = '0.0"%"'
    ws[f'C{row}'] = "≥85%"
    ws[f'C{row}'].font = Font(bold=True)
    
    ws.column_dimensions['A'].width = 40
    ws.column_dimensions['B'].width = 18
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 12


# ============================================================================
# SECTION 11: REMAINING SHEETS (Gap Analysis, Evidence, Approval)
# ============================================================================

def create_gap_analysis_sheet(wb, styles):
    """Create Gap_Analysis sheet."""
    ws = wb["Gap_Analysis"]
    
    ws.merge_cells('A1:H1')
    cell = ws['A1']
    cell.value = "GAP ANALYSIS"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    headers = [
        "Gap ID", "Gap Description", "Affected Repositories",
        "Remediation Plan", "Responsible Party",
        "Target Date", "Status", "Notes"
    ]
    
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    widths = [12, 40, 30, 40, 25, 18, 18, 30]
    for idx, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = width


def create_evidence_register_sheet(wb, styles):
    """Create Evidence_Register sheet."""
    ws = wb["Evidence_Register"]
    
    ws.merge_cells('A1:H1')
    cell = ws['A1']
    cell.value = "EVIDENCE REGISTER"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    headers = [
        "Evidence ID", "Evidence Type", "Description",
        "File Name", "File Location", "Collection Date",
        "Retention End Date", "Notes"
    ]
    
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    widths = [12, 25, 40, 30, 30, 18, 18, 30]
    for idx, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(idx)].width = width


def create_approval_signoff_sheet(wb, styles):
    """Create Approval_Sign_Off sheet."""
    ws = wb["Approval_Sign_Off"]
    
    ws.merge_cells('A1:E1')
    cell = ws['A1']
    cell.value = "ASSESSMENT COMPLETION CERTIFICATION"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 40
    
    row = 3
    ws.merge_cells(f'A{row}:E{row+3}')
    cell = ws[f'A{row}']
    cell.value = """Branch Protection Assessment Certification

Assessment Completion Date: [Date]
Overall Compliance Score: [See Compliance_Scoring]

I certify that this assessment has been completed according to ISMS-POL-A.8.4 requirements."""
    cell.alignment = Alignment(wrap_text=True, vertical="top")
    
    ws.column_dimensions['A'].width = 30


# ============================================================================
# SECTION 12: MAIN FUNCTION
# ============================================================================

def main():
    """Main function to generate the Excel workbook."""
    logger.info("Starting ISMS-A84-2 Branch Protection Assessment Workbook Generation...")
    
    wb = create_workbook()
    styles = setup_styles()
    
    first_sheet = wb["Instructions & Legend"]
    validations = create_base_validations(first_sheet)
    
    logger.info("Creating Instructions & Legend sheet...")
    create_instructions_sheet(wb, styles)
    
    logger.info("Creating Repository_Branch_Inventory sheet...")
    create_branch_inventory_sheet(wb, styles, validations)
    
    logger.info("Creating Branch_Protection_Details sheet...")
    create_protection_details_sheet(wb, styles, validations)
    
    logger.info("Creating Pull_Request_Configuration sheet...")
    create_pr_configuration_sheet(wb, styles, validations)
    
    logger.info("Creating Status_Check_Verification sheet...")
    create_status_check_sheet(wb, styles, validations)
    
    logger.info("Creating Signed_Commits_Audit sheet...")
    create_signed_commits_sheet(wb, styles, validations)
    
    logger.info("Creating Exception_Management sheet...")
    create_exception_management_sheet(wb, styles, validations)
    
    logger.info("Creating Compliance_Scoring sheet...")
    create_compliance_scoring_sheet(wb, styles)
    
    logger.info("Creating Gap_Analysis sheet...")
    create_gap_analysis_sheet(wb, styles)
    
    logger.info("Creating Evidence_Register sheet...")
    create_evidence_register_sheet(wb, styles)
    
    logger.info("Creating Approval_Sign_Off sheet...")
    create_approval_signoff_sheet(wb, styles)
    
    output_filename = f"ISMS-IMP-A.8.4.2_Branch_Protection_{datetime.now().strftime('%Y%m%d')}.xlsx"
    wb.save(output_filename)
    logger.info(f"\n✅ Workbook generated successfully: {output_filename}")
    logger.info(f"{CHART} Sheets created: {len(wb.sheetnames)}")
    logger.info("\nWorkbook ready for branch protection compliance assessment!")


if __name__ == "__main__":
    main()

# =============================================================================
# QA_VERIFIED: 2026-01-31
# QA_STATUS: PASSED - STANDARDIZATION COMPLETE (Phase 1-3)
# QA_TOOL: Claude Code Standardization
# CHANGES: constants, metadata headers, v1.0 versioning, logger output
# =============================================================================
