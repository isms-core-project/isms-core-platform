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
ISMS-IMP-A.7.10.1 - Storage Media Inventory Assessment Excel Generator
================================================================================

ISO/IEC 27001:2022 Control A.7.10: Storage Media
Assessment Domain 1 of 4: Storage Media Inventory & Classification

--------------------------------------------------------------------------------
DESCRIPTION
--------------------------------------------------------------------------------

This script generates a comprehensive Excel assessment workbook for evaluating
storage media inventory and classification against ISO 27001:2022 Control
A.7.10 requirements.

**Generated Workbook Structure:**
1. Instructions & Legend - Assessment guidance, colour coding, definitions
2. Digital Storage Media - HDD, SSD, USB, tape, optical inventory
3. Removable Media Registry - Authorised removable devices with approvals
4. Fixed Storage Assets - Servers, NAS, SAN inventory
5. Cloud Storage Mapping - Cloud storage locations and configurations
6. Physical Documents - Paper, microfilm, archive storage
7. Summary Dashboard - Inventory metrics, compliance overview
8. Evidence Register - Audit evidence tracking
9. Approval Sign-Off - Three-level stakeholder approval workflow

--------------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------------

    python3 generate_a710_1_storage_media_inventory.py

Output:
    File: ISMS-IMP-A.7.10.1_Storage_Media_Inventory_YYYYMMDD.xlsx

================================================================================
"""

# =============================================================================
# Standard Library Imports
# =============================================================================
import logging
import sys
from datetime import datetime

# =============================================================================
# Third-Party Imports
# =============================================================================
try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.datavalidation import DataValidation
except ImportError:
    print("Error: openpyxl not installed")
    print("Install with: pip install openpyxl")
    sys.exit(1)

# =============================================================================
# Logging Configuration
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
DOCUMENT_ID = "ISMS-IMP-A.7.10.1"
WORKBOOK_NAME = "Storage Media Inventory"
CONTROL_ID = "A.7.10"
CONTROL_NAME = "Storage Media"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

# Timestamps
GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")      # Swiss format
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")   # For filenames

# Output filename
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

# =============================================================================
# STYLE DEFINITIONS
# =============================================================================
STYLES = {
    'title': {
        'font': Font(name='Calibri', size=16, bold=True, color='FFFFFF'),
        'fill': PatternFill(start_color='003366', end_color='003366', fill_type='solid'),
        'alignment': Alignment(horizontal='left', vertical='center', wrap_text=True),
        'border': Border(
            left=Side(style='thin'), right=Side(style='thin'),
            top=Side(style='thin'), bottom=Side(style='thin')
        )
    },
    'header': {
        'font': Font(name='Calibri', size=11, bold=True, color='FFFFFF'),
        'fill': PatternFill(start_color='003366', end_color='003366', fill_type='solid'),
        'alignment': Alignment(horizontal='center', vertical='center', wrap_text=True),
        'border': Border(
            left=Side(style='thin'), right=Side(style='thin'),
            top=Side(style='thin'), bottom=Side(style='thin')
        )
    },
    'subheader': {
        'font': Font(name='Calibri', size=10, bold=True, color='000000'),
        'fill': PatternFill(start_color='D8E4F8', end_color='D8E4F8', fill_type='solid'),
        'alignment': Alignment(horizontal='left', vertical='center', wrap_text=True),
        'border': Border(
            left=Side(style='thin'), right=Side(style='thin'),
            top=Side(style='thin'), bottom=Side(style='thin')
        )
    },
    'input_cell': {
        'font': Font(name='Calibri', size=10, color='000000'),
        'fill': PatternFill(start_color='FFFFCC', end_color='FFFFCC', fill_type='solid'),
        'alignment': Alignment(horizontal='left', vertical='top', wrap_text=True),
        'border': Border(
            left=Side(style='thin'), right=Side(style='thin'),
            top=Side(style='thin'), bottom=Side(style='thin')
        )
    },
    'normal': {
        'font': Font(name='Calibri', size=10, color='000000'),
        'alignment': Alignment(horizontal='left', vertical='top', wrap_text=True),
        'border': Border(
            left=Side(style='thin'), right=Side(style='thin'),
            top=Side(style='thin'), bottom=Side(style='thin')
        )
    },
    'reference': {
        'font': Font(name='Calibri', size=9, color='000000'),
        'fill': PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid'),
        'alignment': Alignment(horizontal='left', vertical='top', wrap_text=True),
        'border': Border(
            left=Side(style='thin'), right=Side(style='thin'),
            top=Side(style='thin'), bottom=Side(style='thin')
        )
    }
}


def apply_style(cell, style_name):
    """Apply a named style to a cell."""
    style = STYLES[style_name]
    cell.font = style['font']
    if 'fill' in style:
        cell.fill = style['fill']
    cell.alignment = style['alignment']
    if 'border' in style:
        cell.border = style['border']


def create_workbook():
    """Create workbook with all required sheets."""
    wb = Workbook()

    # Remove default sheet
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])

    # Create all sheets in order
    sheets = [
        "Instructions & Legend",
        "2. Digital Storage Media",
        "3. Removable Media Registry",
        "4. Fixed Storage Assets",
        "5. Cloud Storage Mapping",
        "6. Physical Documents",
        "Summary Dashboard",
        "Evidence Register",
        "Approval Sign-Off"
    ]

    for idx, sheet_name in enumerate(sheets):
        wb.create_sheet(sheet_name, idx)

    return wb


def get_base_columns():
    """Return base column structure (A-Q, 17 columns)."""
    return [
        ("A", "Media ID / Asset Tag", 20),
        ("B", "Media Type", 18),
        ("C", "Data Classification", 18),
        ("D", "Serial Number", 25),
        ("E", "Assigned Custodian", 20),
        ("F", "Status", 18),
        ("G", "Acquisition Date", 12),
        ("H", "Last Audit Date", 12),
        ("I", "Next Audit Date", 12),
        ("J", "Gap Identified", 25),
        ("K", "Remediation Plan", 25),
        ("L", "Target Completion", 12),
        ("M", "Risk Level", 12),
        ("N", "Evidence Reference", 20),
        ("O", "Notes / Comments", 25),
        ("P", "Remediation Owner", 18),
        ("Q", "Budget Required", 15)
    ]


def create_base_validations(ws):
    """Create data validation objects for standard columns."""

    # Media Type (Column B) - will be overridden per sheet
    dv_media = DataValidation(
        type="list",
        formula1='"HDD,SSD,USB Flash Drive,SD Card,Backup Tape,Optical Media,Other"',
        allow_blank=True
    )
    dv_media.error = 'Please select from dropdown'
    dv_media.errorTitle = 'Invalid Media Type'
    ws.add_data_validation(dv_media)
    dv_media.add('B10:B100')

    # Data Classification (Column C)
    dv_classification = DataValidation(
        type="list",
        formula1='"Public,Internal,Confidential,Restricted"',
        allow_blank=True
    )
    ws.add_data_validation(dv_classification)
    dv_classification.add('C10:C100')

    # Status (Column F)
    dv_status = DataValidation(
        type="list",
        formula1='"Registered,Unregistered,Pending Disposal,In Transit,Lost/Stolen,N/A"',
        allow_blank=True
    )
    ws.add_data_validation(dv_status)
    dv_status.add('F10:F100')

    # Risk Level (Column M)
    dv_risk = DataValidation(
        type="list",
        formula1='"Critical,High,Medium,Low"',
        allow_blank=True
    )
    ws.add_data_validation(dv_risk)
    dv_risk.add('M10:M100')

    # Budget Required (Column Q)
    dv_budget = DataValidation(
        type="list",
        formula1='"Yes,No,Unknown"',
        allow_blank=True
    )
    ws.add_data_validation(dv_budget)
    dv_budget.add('Q10:Q100')


def create_instructions_sheet(ws):
    """Create Instructions & Legend sheet."""

    # Title
    ws.merge_cells('A1:F1')
    cell = ws['A1']
    cell.value = f"{DOCUMENT_ID} - {WORKBOOK_NAME} Assessment"
    apply_style(cell, 'title')
    ws.row_dimensions[1].height = 25

    # Document Information
    current_row = 3
    info_data = [
        ("Document ID:", DOCUMENT_ID),
        ("Assessment Date:", GENERATED_DATE),
        ("Assessor Name:", "[Enter Name]"),
        ("Organisation:", "[Enter Organisation]"),
        ("Review Period:", "[e.g., Q1 2026]"),
        ("Control Reference:", CONTROL_REF)
    ]

    for label, value in info_data:
        ws[f'A{current_row}'].value = label
        ws[f'A{current_row}'].font = Font(bold=True)
        ws[f'B{current_row}'].value = value
        if "[" in value:
            ws[f'B{current_row}'].fill = PatternFill(start_color='FFFFCC', end_color='FFFFCC', fill_type='solid')
        current_row += 1

    current_row += 1

    # How to Use This Workbook
    ws.merge_cells(f'A{current_row}:F{current_row}')
    cell = ws[f'A{current_row}']
    cell.value = "HOW TO USE THIS WORKBOOK"
    apply_style(cell, 'subheader')
    current_row += 1

    instructions = [
        "1. Complete assessment sheets 2-6 in order, filling in all yellow-highlighted cells",
        "2. Use dropdown menus where provided for consistency",
        "3. Link supporting evidence to the Evidence Register (Sheet 8) using Column N",
        "4. Review the Summary Dashboard (Sheet 7) for overall inventory status",
        "5. Document any gaps with remediation plans and target completion dates",
        "6. Obtain three-level approval using the Approval Sign-Off sheet (Sheet 9)",
        "7. Review and update this assessment quarterly or when significant changes occur"
    ]

    for instruction in instructions:
        ws[f'A{current_row}'].value = instruction
        ws[f'A{current_row}'].alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
        current_row += 1

    current_row += 1

    # Colour Coding Legend
    ws.merge_cells(f'A{current_row}:F{current_row}')
    cell = ws[f'A{current_row}']
    cell.value = "COLOUR CODING LEGEND"
    apply_style(cell, 'subheader')
    current_row += 1

    legend_data = [
        ("Blue Header", "Column headers - Do not edit", "003366"),
        ("Yellow", "Data entry cells - Complete these fields", "FFFFCC"),
        ("Light Blue", "Section headers - Read-only", "D8E4F8"),
        ("Grey", "Reference information - Read-only", "F2F2F2"),
        ("White", "Optional fields - Complete if relevant", "FFFFFF")
    ]

    for colour_desc, usage, colour_code in legend_data:
        ws[f'A{current_row}'].value = colour_desc
        ws[f'A{current_row}'].fill = PatternFill(start_color=colour_code, end_color=colour_code, fill_type='solid')
        ws[f'B{current_row}'].value = usage
        current_row += 1

    current_row += 1

    # Key Definitions
    ws.merge_cells(f'A{current_row}:F{current_row}')
    cell = ws[f'A{current_row}']
    cell.value = "KEY DEFINITIONS"
    apply_style(cell, 'subheader')
    current_row += 1

    definitions = [
        ("Storage Media", "Any device or material capable of storing data, including digital and physical formats"),
        ("Removable Media", "Portable storage devices that can be removed from systems (USB drives, external drives, optical discs)"),
        ("Custodian", "Person assigned responsibility for a specific media item's security"),
        ("Chain of Custody", "Documented chronological record of handling, transfer, and storage of media"),
        ("Data Classification", "Category assigned to data based on sensitivity (Public, Internal, Confidential, Restricted)")
    ]

    for term, definition in definitions:
        ws[f'A{current_row}'].value = term
        ws[f'A{current_row}'].font = Font(bold=True)
        ws[f'B{current_row}'].value = definition
        ws[f'B{current_row}'].alignment = Alignment(horizontal='left', wrap_text=True)
        ws.row_dimensions[current_row].height = 30
        current_row += 1

    current_row += 1

    # Regulatory References
    ws.merge_cells(f'A{current_row}:F{current_row}')
    cell = ws[f'A{current_row}']
    cell.value = "REGULATORY REFERENCES"
    apply_style(cell, 'subheader')
    current_row += 1

    references = [
        "- ISO/IEC 27001:2022 Control A.7.10: Storage Media",
        "- ISO/IEC 27002:2022 Control 7.10: Storage Media",
        "- GDPR Article 5(1)(f): Integrity and confidentiality",
        "- Swiss nDSG Article 8: Technical measures",
        "- PCI DSS v4.0.1 Requirement 9.4: Media protection"
    ]

    for ref in references:
        ws[f'A{current_row}'].value = ref
        current_row += 1

    # Set column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 60
    ws.column_dimensions['C'].width = 5
    ws.column_dimensions['D'].width = 20
    ws.column_dimensions['E'].width = 30
    ws.column_dimensions['F'].width = 15


def create_assessment_sheet(ws, sheet_title, sheet_objective, extended_cols, sheet_specific_validations=None):
    """Create a standardised assessment sheet."""

    # Title
    ws.merge_cells('A1:T1')
    cell = ws['A1']
    cell.value = sheet_title
    apply_style(cell, 'title')
    ws.row_dimensions[1].height = 25

    # Policy Reference
    ws.merge_cells('A2:T2')
    cell = ws['A2']
    cell.value = f"Policy Reference: ISMS-POL-A.7.10 - Storage Media"
    cell.font = Font(name='Calibri', size=9, italic=True)

    # Assessment Objective
    ws.merge_cells('A4:T6')
    cell = ws['A4']
    cell.value = f"ASSESSMENT OBJECTIVE:\n{sheet_objective}"
    cell.font = Font(name='Calibri', size=11, bold=True)
    cell.fill = PatternFill(start_color='E7E6E6', end_color='E7E6E6', fill_type='solid')
    cell.alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
    ws.row_dimensions[4].height = 50

    # Instructions
    ws.merge_cells('A7:T7')
    cell = ws['A7']
    cell.value = "Complete the yellow-highlighted cells below. Use dropdowns where provided. Link evidence in Column N to Evidence Register sheet."
    cell.font = Font(name='Calibri', size=9, italic=True, color='0000FF')

    # Column Headers
    base_cols = get_base_columns()
    all_cols = base_cols + extended_cols

    for col_letter, header_text, width in all_cols:
        cell = ws[f'{col_letter}9']
        cell.value = header_text
        apply_style(cell, 'header')
        ws.column_dimensions[col_letter].width = width

    # Data Entry Rows (13 rows)
    for row in range(10, 23):
        for col_idx in range(1, len(all_cols) + 1):
            col_letter = get_column_letter(col_idx)
            cell = ws[f'{col_letter}{row}']
            apply_style(cell, 'input_cell')

    # Apply validations
    create_base_validations(ws)
    if sheet_specific_validations:
        sheet_specific_validations(ws)

    # Freeze panes
    ws.freeze_panes = 'A10'


def create_digital_media_sheet(ws):
    """Create Digital Storage Media assessment sheet."""
    extended_cols = [
        ("R", "Physical Location", 22),
        ("S", "Encryption Status", 18),
        ("T", "Capacity (GB)", 15)
    ]

    create_assessment_sheet(
        ws,
        "2. Digital Storage Media Inventory",
        "Document every digital storage device managed by [Organisation] including HDDs, SSDs, USB drives, SD cards, backup tapes, and optical media.",
        extended_cols
    )

    # Add sheet-specific validations
    dv_encryption = DataValidation(
        type="list",
        formula1='"Encrypted (AES-256),Encrypted (Hardware),Not Encrypted,N/A,Unknown"',
        allow_blank=True
    )
    ws.add_data_validation(dv_encryption)
    dv_encryption.add('S10:S100')


def create_removable_media_sheet(ws):
    """Create Removable Media Registry sheet."""
    extended_cols = [
        ("R", "Authorisation Reference", 22),
        ("S", "Authorised User(s)", 22),
        ("T", "Permitted Use Cases", 30)
    ]

    create_assessment_sheet(
        ws,
        "3. Removable Media Registry",
        "Register all authorised removable media with management approval documentation, assigned users, and permitted use cases.",
        extended_cols
    )


def create_fixed_storage_sheet(ws):
    """Create Fixed Storage Assets sheet."""
    extended_cols = [
        ("R", "System Type", 18),
        ("S", "Total Capacity (TB)", 18),
        ("T", "Utilisation (%)", 15)
    ]

    create_assessment_sheet(
        ws,
        "4. Fixed Storage Assets",
        "Inventory all fixed storage systems including servers, NAS, SAN, and archive systems with capacity and encryption status.",
        extended_cols
    )

    # Add sheet-specific validations
    dv_system_type = DataValidation(
        type="list",
        formula1='"Physical Server,Virtual Server,NAS,SAN,Archive System,Backup Appliance"',
        allow_blank=True
    )
    ws.add_data_validation(dv_system_type)
    dv_system_type.add('R10:R100')


def create_cloud_storage_sheet(ws):
    """Create Cloud Storage Mapping sheet."""
    extended_cols = [
        ("R", "Cloud Type", 18),
        ("S", "Provider Name", 22),
        ("T", "Data Residency", 22)
    ]

    create_assessment_sheet(
        ws,
        "5. Cloud Storage Mapping",
        "Document all cloud storage locations including IaaS, PaaS, SaaS, and backup services with provider and data residency information.",
        extended_cols
    )

    # Add sheet-specific validations
    dv_cloud_type = DataValidation(
        type="list",
        formula1='"IaaS,PaaS,SaaS,Hybrid,Multi-Cloud"',
        allow_blank=True
    )
    ws.add_data_validation(dv_cloud_type)
    dv_cloud_type.add('R10:R100')

    dv_residency = DataValidation(
        type="list",
        formula1='"Switzerland,EU,US,UK,APAC,Multiple Regions,Unknown"',
        allow_blank=True
    )
    ws.add_data_validation(dv_residency)
    dv_residency.add('T10:T100')


def create_physical_docs_sheet(ws):
    """Create Physical Documents sheet."""
    extended_cols = [
        ("R", "Document Type", 18),
        ("S", "Storage Location", 25),
        ("T", "Access Control", 22)
    ]

    create_assessment_sheet(
        ws,
        "6. Physical Documents & Archives",
        "Inventory physical document storage containing sensitive information including paper documents, microfilm, and archive boxes.",
        extended_cols
    )

    # Add sheet-specific validations
    dv_doc_type = DataValidation(
        type="list",
        formula1='"Paper Documents,Microfilm,Microfiche,Archive Boxes,Mixed Media"',
        allow_blank=True
    )
    ws.add_data_validation(dv_doc_type)
    dv_doc_type.add('R10:R100')

    dv_access = DataValidation(
        type="list",
        formula1='"Key Lock,Combination Lock,Card Access,Biometric,Multi-Factor,None"',
        allow_blank=True
    )
    ws.add_data_validation(dv_access)
    dv_access.add('T10:T100')


def create_summary_dashboard(ws):
    """Create Summary Dashboard sheet."""

    # Title
    ws.merge_cells('A1:H1')
    cell = ws['A1']
    cell.value = "Storage Media Inventory - Summary Dashboard"
    apply_style(cell, 'title')
    ws.row_dimensions[1].height = 25

    # Section 1: Inventory Totals
    current_row = 3
    ws.merge_cells(f'A{current_row}:D{current_row}')
    ws[f'A{current_row}'].value = "INVENTORY TOTALS"
    apply_style(ws[f'A{current_row}'], 'subheader')
    current_row += 1

    inventory_metrics = [
        ("Total Digital Media Items", "[Count]"),
        ("Total Removable Media Items", "[Count]"),
        ("Total Fixed Storage Systems", "[Count]"),
        ("Total Cloud Storage Services", "[Count]"),
        ("Total Physical Storage Locations", "[Count]"),
        ("TOTAL MEDIA ITEMS", "[Sum]")
    ]

    for label, value in inventory_metrics:
        ws[f'A{current_row}'].value = label
        ws[f'B{current_row}'].value = value
        ws[f'B{current_row}'].fill = PatternFill(start_color='FFFFCC', end_color='FFFFCC', fill_type='solid')
        current_row += 1

    current_row += 1

    # Section 2: Classification Distribution
    ws.merge_cells(f'A{current_row}:D{current_row}')
    ws[f'A{current_row}'].value = "CLASSIFICATION DISTRIBUTION"
    apply_style(ws[f'A{current_row}'], 'subheader')
    current_row += 1

    classification_metrics = [
        ("CONFIDENTIAL Media", "[Count]", "[%]"),
        ("INTERNAL Media", "[Count]", "[%]"),
        ("PUBLIC Media", "[Count]", "[%]")
    ]

    ws[f'A{current_row}'].value = "Classification"
    ws[f'B{current_row}'].value = "Count"
    ws[f'C{current_row}'].value = "Percentage"
    apply_style(ws[f'A{current_row}'], 'header')
    apply_style(ws[f'B{current_row}'], 'header')
    apply_style(ws[f'C{current_row}'], 'header')
    current_row += 1

    for label, count, pct in classification_metrics:
        ws[f'A{current_row}'].value = label
        ws[f'B{current_row}'].value = count
        ws[f'C{current_row}'].value = pct
        ws[f'B{current_row}'].fill = PatternFill(start_color='FFFFCC', end_color='FFFFCC', fill_type='solid')
        ws[f'C{current_row}'].fill = PatternFill(start_color='FFFFCC', end_color='FFFFCC', fill_type='solid')
        current_row += 1

    current_row += 1

    # Section 3: Compliance Metrics
    ws.merge_cells(f'A{current_row}:D{current_row}')
    ws[f'A{current_row}'].value = "COMPLIANCE METRICS"
    apply_style(ws[f'A{current_row}'], 'subheader')
    current_row += 1

    compliance_metrics = [
        ("Registered Media (%)", "[%]", "Target: 100%"),
        ("Encrypted CONFIDENTIAL Media (%)", "[%]", "Target: 100%"),
        ("Authorised Removable Media (%)", "[%]", "Target: 100%"),
        ("Custodian Assigned (%)", "[%]", "Target: 100%"),
        ("Items Requiring Remediation", "[Count]", "Target: 0")
    ]

    for label, value, target in compliance_metrics:
        ws[f'A{current_row}'].value = label
        ws[f'B{current_row}'].value = value
        ws[f'C{current_row}'].value = target
        ws[f'B{current_row}'].fill = PatternFill(start_color='FFFFCC', end_color='FFFFCC', fill_type='solid')
        current_row += 1

    current_row += 1

    # Section 4: Key Performance Indicators
    ws.merge_cells(f'A{current_row}:D{current_row}')
    ws[f'A{current_row}'].value = "KEY PERFORMANCE INDICATORS"
    apply_style(ws[f'A{current_row}'], 'subheader')
    current_row += 1

    kpi_metrics = [
        ("Overdue Audits", "[Count]"),
        ("Expired Authorisations", "[Count]"),
        ("Lost/Stolen Media (YTD)", "[Count]"),
        ("Unencrypted CONFIDENTIAL Media", "[Count]"),
        ("Unassigned Media", "[Count]")
    ]

    for label, value in kpi_metrics:
        ws[f'A{current_row}'].value = label
        ws[f'B{current_row}'].value = value
        ws[f'B{current_row}'].fill = PatternFill(start_color='FFFFCC', end_color='FFFFCC', fill_type='solid')
        current_row += 1

    # Set column widths
    ws.column_dimensions['A'].width = 35
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 15


def create_evidence_register(ws):
    """Create Evidence Register sheet."""

    # Title
    ws.merge_cells('A1:K1')
    cell = ws['A1']
    cell.value = "Evidence Register - Supporting Documentation"
    apply_style(cell, 'title')
    ws.row_dimensions[1].height = 25

    # Instructions
    ws.merge_cells('A2:K2')
    cell = ws['A2']
    cell.value = "Use this register to document all evidence supporting your storage media inventory assessment. Reference evidence by ID (Column A) in the 'Evidence Reference' column (Column N) of assessment sheets."
    cell.font = Font(name='Calibri', size=9, italic=True)
    ws.row_dimensions[2].height = 30

    # Column Headers
    headers = [
        ("A", "Evidence ID", 12),
        ("B", "Assessment Sheet", 20),
        ("C", "Related Media/System", 30),
        ("D", "Evidence Type", 20),
        ("E", "Evidence Title/Description", 35),
        ("F", "File Location/Link", 40),
        ("G", "Date Created/Collected", 12),
        ("H", "Retention Period", 15),
        ("I", "Next Review Date", 12),
        ("J", "Owner/Custodian", 20),
        ("K", "Notes", 30)
    ]

    for col_letter, header_text, width in headers:
        cell = ws[f'{col_letter}4']
        cell.value = header_text
        apply_style(cell, 'header')
        ws.column_dimensions[col_letter].width = width

    # Data rows (100 rows)
    for row in range(5, 105):
        for col_letter, _, _ in headers:
            cell = ws[f'{col_letter}{row}']
            apply_style(cell, 'input_cell')

    # Add dropdowns
    dv_type = DataValidation(
        type="list",
        formula1='"Asset Report,Inventory Export,Authorisation Form,Encryption Report,Audit Log,Configuration Document,Certificate,Contract,Training Record,Screenshot,Other"',
        allow_blank=True
    )
    ws.add_data_validation(dv_type)
    dv_type.add('D5:D104')

    dv_sheet = DataValidation(
        type="list",
        formula1='"Sheet 2: Digital Media,Sheet 3: Removable Media,Sheet 4: Fixed Storage,Sheet 5: Cloud Storage,Sheet 6: Physical Documents"',
        allow_blank=True
    )
    ws.add_data_validation(dv_sheet)
    dv_sheet.add('B5:B104')

    # Freeze panes
    ws.freeze_panes = 'A5'


def create_approval_signoff(ws):
    """Create Approval Sign-Off sheet."""

    # Title
    ws.merge_cells('A1:F1')
    cell = ws['A1']
    cell.value = "Three-Level Approval Workflow"
    apply_style(cell, 'title')
    ws.row_dimensions[1].height = 25

    current_row = 3

    # Document Control Section
    ws.merge_cells(f'A{current_row}:F{current_row}')
    ws[f'A{current_row}'].value = "DOCUMENT CONTROL"
    apply_style(ws[f'A{current_row}'], 'subheader')
    current_row += 1

    control_fields = [
        ("Assessment Period:", "[e.g., Q1 2026]"),
        ("Workbook Version:", "1.0"),
        ("Total Media Items Inventoried:", "[Count]"),
        ("Overall Compliance %:", "[%]"),
        ("Critical Gaps Identified:", "[Count]"),
        ("Assessment Completed By:", "[Name, Date]")
    ]

    for label, value in control_fields:
        ws[f'A{current_row}'].value = label
        ws[f'B{current_row}'].value = value
        ws[f'B{current_row}'].fill = PatternFill(start_color='FFFFCC', end_color='FFFFCC', fill_type='solid')
        current_row += 1

    current_row += 2

    # Level 1 Approval
    ws.merge_cells(f'A{current_row}:F{current_row}')
    ws[f'A{current_row}'].value = "LEVEL 1 APPROVAL - Technical/Operational"
    apply_style(ws[f'A{current_row}'], 'subheader')
    current_row += 1

    ws[f'A{current_row}'].value = 'Role: IT Operations Manager / Asset Management Lead'
    ws[f'A{current_row}'].font = Font(italic=True)
    current_row += 1

    ws.merge_cells(f'A{current_row}:F{current_row}')
    ws[f'A{current_row}'].value = 'Approval Statement: "I confirm that this assessment accurately reflects our current storage media inventory as of [Date]. All media items have been reviewed and gaps identified."'
    ws[f'A{current_row}'].alignment = Alignment(wrap_text=True, vertical='top')
    ws.row_dimensions[current_row].height = 40
    current_row += 1

    approval_fields = ["Approver Name:", "Title/Role:", "Email:", "Review Date:", "Approval Status:", "Conditions/Comments:", "Signature:"]

    for field in approval_fields:
        ws[f'A{current_row}'].value = field
        ws[f'B{current_row}'].fill = PatternFill(start_color='FFFFCC', end_color='FFFFCC', fill_type='solid')
        if field == "Approval Status:":
            dv = DataValidation(type="list", formula1='"Approved,Approved with Conditions,Rejected"', allow_blank=True)
            ws.add_data_validation(dv)
            dv.add(f'B{current_row}')
        current_row += 1

    current_row += 2

    # Level 2 Approval
    ws.merge_cells(f'A{current_row}:F{current_row}')
    ws[f'A{current_row}'].value = "LEVEL 2 APPROVAL - Management"
    apply_style(ws[f'A{current_row}'], 'subheader')
    current_row += 1

    ws[f'A{current_row}'].value = 'Role: Chief Information Security Officer / IT Director'
    ws[f'A{current_row}'].font = Font(italic=True)
    current_row += 1

    ws.merge_cells(f'A{current_row}:F{current_row}')
    ws[f'A{current_row}'].value = 'Approval Statement: "I acknowledge the findings of this storage media inventory assessment and approve the proposed remediation plans. Resources will be allocated to address critical gaps."'
    ws[f'A{current_row}'].alignment = Alignment(wrap_text=True, vertical='top')
    ws.row_dimensions[current_row].height = 40
    current_row += 1

    for field in approval_fields:
        ws[f'A{current_row}'].value = field
        ws[f'B{current_row}'].fill = PatternFill(start_color='FFFFCC', end_color='FFFFCC', fill_type='solid')
        if field == "Approval Status:":
            dv = DataValidation(type="list", formula1='"Approved,Approved with Conditions,Rejected"', allow_blank=True)
            ws.add_data_validation(dv)
            dv.add(f'B{current_row}')
        current_row += 1

    current_row += 2

    # Level 3 Approval
    ws.merge_cells(f'A{current_row}:F{current_row}')
    ws[f'A{current_row}'].value = "LEVEL 3 APPROVAL - Executive"
    apply_style(ws[f'A{current_row}'], 'subheader')
    current_row += 1

    ws[f'A{current_row}'].value = 'Role: Chief Operating Officer / Chief Risk Officer / Executive Management'
    ws[f'A{current_row}'].font = Font(italic=True)
    current_row += 1

    ws.merge_cells(f'A{current_row}:F{current_row}')
    ws[f'A{current_row}'].value = 'Approval Statement: "Executive leadership acknowledges the storage media inventory status and associated risks. The organisation commits to remediation of identified gaps."'
    ws[f'A{current_row}'].alignment = Alignment(wrap_text=True, vertical='top')
    ws.row_dimensions[current_row].height = 40
    current_row += 1

    for field in approval_fields:
        ws[f'A{current_row}'].value = field
        ws[f'B{current_row}'].fill = PatternFill(start_color='FFFFCC', end_color='FFFFCC', fill_type='solid')
        if field == "Approval Status:":
            dv = DataValidation(type="list", formula1='"Approved,Approved with Conditions,Rejected"', allow_blank=True)
            ws.add_data_validation(dv)
            dv.add(f'B{current_row}')
        current_row += 1

    # Set column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 50
    ws.column_dimensions['C'].width = 15


def main():
    """Main function to generate the workbook."""
    logger.info(f"Starting generation of {DOCUMENT_ID} - {WORKBOOK_NAME}")
    logger.info(f"Control Reference: {CONTROL_REF}")

    try:
        # Create workbook
        logger.info("Creating workbook structure...")
        wb = create_workbook()

        # Populate sheets
        logger.info("Creating Instructions & Legend sheet...")
        create_instructions_sheet(wb["Instructions & Legend"])

        logger.info("Creating Digital Storage Media sheet...")
        create_digital_media_sheet(wb["2. Digital Storage Media"])

        logger.info("Creating Removable Media Registry sheet...")
        create_removable_media_sheet(wb["3. Removable Media Registry"])

        logger.info("Creating Fixed Storage Assets sheet...")
        create_fixed_storage_sheet(wb["4. Fixed Storage Assets"])

        logger.info("Creating Cloud Storage Mapping sheet...")
        create_cloud_storage_sheet(wb["5. Cloud Storage Mapping"])

        logger.info("Creating Physical Documents sheet...")
        create_physical_docs_sheet(wb["6. Physical Documents"])

        logger.info("Creating Summary Dashboard...")
        create_summary_dashboard(wb["Summary Dashboard"])

        logger.info("Creating Evidence Register...")
        create_evidence_register(wb["Evidence Register"])

        logger.info("Creating Approval Sign-Off...")
        create_approval_signoff(wb["Approval Sign-Off"])

        # Save workbook
        logger.info(f"Saving workbook as {OUTPUT_FILENAME}...")
        wb.save(OUTPUT_FILENAME)

        logger.info("=" * 60)
        logger.info(f"SUCCESS: Workbook generated successfully!")
        logger.info(f"Output file: {OUTPUT_FILENAME}")
        logger.info(f"Document ID: {DOCUMENT_ID}")
        logger.info(f"Generated: {GENERATED_DATE}")
        logger.info("=" * 60)

        return True

    except Exception as e:
        logger.error(f"Failed to generate workbook: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)


# =============================================================================
# QA_VERIFIED: 2026-02-03
# QA_STATUS: PASSED - STANDARDIZATION COMPLETE
# QA_TOOL: Claude Code Standardization
# CHANGES: Initial creation following A.8.10 pattern
# =============================================================================
