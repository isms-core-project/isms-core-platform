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
ISMS-IMP-A.8.32.2 - Change Types & Categories Assessment Excel Generator
================================================================================

ISO/IEC 27001:2022 Control A.8.32: Change Management
Assessment Domain 2 of 4: Change Classification & Risk Management

--------------------------------------------------------------------------------
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR YOUR ORGANIZATION
--------------------------------------------------------------------------------

This script is a TEMPLATE/SAMPLE implementation and MUST be adapted to match
your organization's specific change classification schemes and assessment
requirements.

Key customization areas:
1. Standard change catalog (match your pre-approved changes)
2. Change risk classification criteria (adapt to your risk appetite)
3. Emergency change triggers (customize to your business context)
4. Change calendar blackout periods (align with your business cycles)
5. Approval workflows per change type (match your governance)

DO NOT use this script without reviewing and adapting all sections marked
with "# CUSTOMIZE:" comments throughout the code.

Reference Pattern: Based on ISMS-A.8.32 Change Management Assessment Framework

--------------------------------------------------------------------------------
DESCRIPTION
--------------------------------------------------------------------------------

This script generates a comprehensive Excel assessment workbook for evaluating
change classification, risk assessment, and category management against
ISO 27001:2022 Control A.8.32 requirements.

**Purpose:**
Enables systematic assessment of change type definitions, standard change
catalogs, normal change procedures, emergency change processes, risk
classification matrices, and change calendar management.

**Assessment Scope:**
- Standard change catalog and pre-authorization criteria
- Normal change risk assessment and CAB review procedures
- Emergency change triggers and fast-track approvals
- Change risk classification (Impact × Likelihood matrices)
- Change calendar management and blackout periods
- Change type compliance verification
- Gap analysis and remediation planning
- Evidence collection for audit readiness

**Generated Workbook Structure:**
1. Instructions & Legend - Assessment guidance and classification standards
2. Standard Changes Catalog - Pre-approved low-risk changes
3. Normal_Changes_Assessment - CAB-reviewed changes and procedures
4. Emergency_Changes - Fast-track emergency change process
5. Change_Risk_Classification - Risk matrix and scoring
6. Change Calendar Management - Blackout periods and scheduling
7. Summary Dashboard - Compliance metrics and analytics
8. Evidence Register - Audit evidence tracking
9. Approval Sign-Off - Stakeholder approval workflow

**Key Features:**
- Technology-agnostic assessment (works with any ITSM tool)
- Standard change catalog template with customization guidance
- Risk matrix with Impact × Likelihood methodology
- Change calendar integration for blackout period management
- Automated compliance calculations
- Evidence linkage for audit traceability
- Integration with A.8.32.5 Compliance Dashboard

**Integration:**
This assessment feeds into the A.8.32.5 Compliance Dashboard, which
consolidates data from all four change management assessment domains for
executive oversight and audit readiness.

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
    python3 generate_a832_2_change_types.py

Output:
    File: ISMS_A_8_32_2_Change_Types_Categories_Assessment_YYYYMMDD.xlsx
    Location: Current directory

Post-Generation Steps:
    1. Define your organization's standard change catalog
    2. Document normal change risk assessment procedures
    3. Define emergency change triggers specific to your business
    4. Customize risk matrix to your risk appetite
    5. Document change calendar blackout periods
    6. Review Summary Dashboard for compliance metrics
    7. Collect and link audit evidence
    8. Feed results into A.8.32.5 Compliance Dashboard

--------------------------------------------------------------------------------
METADATA
--------------------------------------------------------------------------------

Control Reference:    ISO/IEC 27001:2022 Annex A Control A.8.32
Assessment Domain:    2 of 4 (Change Classification & Risk Management)
Framework Version:    1.0
Script Version:       1.0
Author:               [Organization] ISMS Implementation Team
Date:                 [Date to be set]
Last Modified:        [Date to be set]
Python Version:       3.8+
License:              [Organisation License/Terms]

Related Documents:
    - ISMS-POL-A.8.32: Change Management Policy (Governance)
    - ISMS-IMP-A.8.32.2: Change Types & Categories Implementation Guide
    - ISMS-IMP-A.8.32.1: Change Process Assessment (Domain 1)
    - ISMS-IMP-A.8.32.3: Environment Separation Assessment (Domain 3)
    - ISMS-IMP-A.8.32.4: Testing & Validation Assessment (Domain 4)
    - ISMS-IMP-A.8.32.5: Compliance Dashboard (Consolidation)

--------------------------------------------------------------------------------
CHANGE HISTORY
--------------------------------------------------------------------------------

Version 1.0 - [Date to be set]
    - Initial release
    - Implements full assessment framework per ISMS-IMP-A.8.32.2 specification
    - Supports comprehensive change classification evaluation
    - Integrated with A.8.32.5 Compliance Dashboard

[Future changes to be documented here]

--------------------------------------------------------------------------------
IMPORTANT NOTES
--------------------------------------------------------------------------------

**Standard Change Philosophy:**
Standard changes are pre-approved, low-risk, well-understood changes that follow
a documented procedure. They don't require CAB approval but DO require logging
and monitoring for compliance.

**Risk Classification Flexibility:**
Customize the risk matrix to your organization's risk appetite. A startup might
accept higher risks than a regulated financial institution. The framework is
intentionally flexible.

**Emergency Change Reality:**
Emergency changes will happen. The goal is controlled urgency, not prevention.
Document clear triggers, fast-track approvals, and mandatory post-implementation
reviews.

**Audit Considerations:**
Auditors will verify that change types are clearly defined, risk assessments
are systematic, and emergency changes have proper justification and review.

**Data Protection:**
Assessment workbooks contain sensitive information about change management
practices, risk tolerances, and operational procedures. Handle according to
your data classification policies.

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


from datetime import datetime, timedelta
# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.8.32.2"
WORKBOOK_NAME = "Change Types & Categories Assessment"
CONTROL_ID = "A.8.32"
CONTROL_NAME = "Change Management"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

# Timestamps
GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")      # For display (Swiss format)
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")   # For filenames (sortable)

# Output filename
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"


from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation


# ============================================================================
# SECTION 1: WORKBOOK CREATION & STYLE DEFINITIONS
# ============================================================================


# ============================================================================
# UNICODE SYMBOLS - PROPER UTF-8 ENCODING
# ============================================================================

CHECK = '\u2705'      # ✅ Green checkmark
XMARK = '\u274C'      # ❌ Red X
WARNING = '\u26A0'    # ⚠️  Warning sign
CHART = '\U0001F4CA' # 📊 Chart
TARGET = '\U0001F3AF' # 🎯 Target
SHIELD = '\U0001F6E1' # 🛡️  Shield
LOCK = '\U0001F512'   # 🔒 Lock
CLOCK = '\U0001F552'  # 🕒 Clock
WRENCH = '\U0001F527' # 🔧 Wrench
ROCKET = '\U0001F680' # 🚀 Rocket
GEAR = '\u2699'       # ⚙️  Gear
BULLET = '\u2022'     # • Bullet point
ARROW = '\u2192'      # → Right arrow

def create_workbook() -> Workbook:
    """Create workbook with all required sheets matching IMP-A.8.32.2 spec."""
    wb = Workbook()

    # Remove default sheet
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])

    # Sheet structure matches ISMS-IMP-A.8.32.2 specification (10 sheets)
    sheets = [
        "Instructions & Legend",
        "Standard Changes Catalog",
        "Normal Change Classification",
        "Emergency Change Procedures",
        "Risk Assessment Matrix",
        "Change Calendar Management",
        "Classification Metrics",
        "Evidence Register",
        "Summary Dashboard",
        "Approval Sign-Off",
    ]
    for name in sheets:
        wb.create_sheet(title=name)

    return wb


def setup_styles():
    """
    Define all cell styles used throughout the workbook.
    
    CRITICAL: Each style object must be created NEW for each cell to avoid
    Excel repair warnings from shared Border/Font/Fill objects.
    This function returns TEMPLATES, not reusable objects.
    """
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
        "section_header": {
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
        "calculated_cell": {
            "fill": PatternFill(start_color="E0E0E0", end_color="E0E0E0", fill_type="solid"),
            "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
            "border": border_thin,
        },
        "border": border_thin,
        "risk_low": {
            "fill": PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
        },
        "risk_medium": {
            "fill": PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
        },
        "risk_high": {
            "fill": PatternFill(start_color="FFD966", end_color="FFD966", fill_type="solid")
        },
        "risk_critical": {
            "fill": PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
        },
    }
    return styles


def apply_style(cell, style_dict):
    """Apply style dictionary to a cell. Creates NEW style objects."""
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
# SECTION 2: DATA VALIDATIONS & DROPDOWN DEFINITIONS
# ============================================================================

def create_base_validations(ws):
    """
    Create data validation objects for standard dropdowns.
    CUSTOMIZE: Adapt dropdown values for change classification context.
    """
    validations = {
        'yes_no': DataValidation(
            type="list",
            formula1='"Yes,No"',
            allow_blank=False
        ),
        'yes_no_na': DataValidation(
            type="list",
            formula1='"Yes,No,N/A"',
            allow_blank=False
        ),
        'definition_status': DataValidation(
            type="list",
            formula1=f'"{CHECK} Defined,⚠️ Partial,❌ Not Defined,📋 Planned,N/A"',
            allow_blank=False
        ),
        'change_category': DataValidation(
            type="list",
            formula1='"Infrastructure,Application,Security,Data,Network,Cloud,User Access,Configuration,Other"',
            allow_blank=False
        ),
        'frequency': DataValidation(
            type="list",
            formula1='"Daily,Weekly,Monthly,Quarterly,Annual,On-Demand,Rare"',
            allow_blank=False
        ),
        'risk_level': DataValidation(
            type="list",
            formula1='"Low,Medium,High,Critical"',
            allow_blank=False
        ),
        'std_change_risk': DataValidation(
            type="list",
            formula1='"Low,Medium"',
            allow_blank=False
        ),
        'std_change_status': DataValidation(
            type="list",
            formula1=f'"{CHECK} Active,⚠️ Under Review,❌ Retired,📋 Proposed"',
            allow_blank=False
        ),
        'cab_requirement': DataValidation(
            type="list",
            formula1='"Mandatory,Recommended,Optional,Not Required"',
            allow_blank=False
        ),
        'approval_authority': DataValidation(
            type="list",
            formula1='"Change Manager,CAB,Service Owner,CISO,CIO,Multiple Required,Other"',
            allow_blank=False
        ),
        'implementation_level': DataValidation(
            type="list",
            formula1=f'"{CHECK} Always,⚠️ Sometimes,❌ Never,📋 Planned"',
            allow_blank=False
        ),
        'exceptions_allowed': DataValidation(
            type="list",
            formula1=f'"{CHECK} Yes,❌ No,⚠️ Case-by-Case,N/A"',
            allow_blank=False
        ),
        'compliance_status': DataValidation(
            type="list",
            formula1=f'"{CHECK} Yes,⚠️ Partial,❌ No"',
            allow_blank=False
        ),
        'emergency_criteria_definition': DataValidation(
            type="list",
            formula1=f'"{CHECK} Clearly Defined,⚠️ Partially,❌ Not Defined"',
            allow_blank=False
        ),
        'user_count': DataValidation(
            type="list",
            formula1='"<10 users,10-50,50-100,100-1000,>1000 users,All users,Business-critical,Other"',
            allow_blank=False
        ),
        'downtime_potential': DataValidation(
            type="list",
            formula1='"<15 min,15-60 min,1-2 hours,2-8 hours,>8 hours,Irreversible,Business-critical,Other"',
            allow_blank=False
        ),
        'data_loss_risk': DataValidation(
            type="list",
            formula1='"None,Minimal,Moderate,High"',
            allow_blank=False
        ),
        'complexity': DataValidation(
            type="list",
            formula1='"Simple,Moderate,Complex,Very Complex"',
            allow_blank=False
        ),
        'testing_maturity': DataValidation(
            type="list",
            formula1='"Extensively Tested,Well Tested,Limited Testing,Untested"',
            allow_blank=False
        ),
        'convening_method': DataValidation(
            type="list",
            formula1='"Conference Call,Video,IM Group,Emergency Hotline,Other"',
            allow_blank=False
        ),
        'applicable_changes': DataValidation(
            type="list",
            formula1='"All,Standard Only,Normal Only,Emergency Only,Custom"',
            allow_blank=False
        ),
        'blackout_reason': DataValidation(
            type="list",
            formula1='"Financial Close,Holiday Period,Peak Business,Audit,Other"',
            allow_blank=False
        ),
        'conflict_detection': DataValidation(
            type="list",
            formula1='"Automated,Manual,None"',
            allow_blank=False
        ),
        'evidence_type': DataValidation(
            type="list",
            formula1='"Catalog,Procedure,Criteria Doc,Risk Matrix,Calendar,Meeting Minutes,Metrics Report,Approval Record,Training Material,Other"',
            allow_blank=False
        ),
        'verification_status': DataValidation(
            type="list",
            formula1=f'"{CHECK} Verified,⚠️ Pending,❌ Not Verified"',
            allow_blank=False
        ),
        'assessment_status': DataValidation(
            type="list",
            formula1=f'"{CHECK} Final,⚠️ Requires Remediation,📋 Draft,❌ Re-assessment Required"',
            allow_blank=False
        ),
        'review_recommendation': DataValidation(
            type="list",
            formula1=f'"{CHECK} Approve,⚠️ Approve with Conditions,❌ Reject,📋 Require Rework"',
            allow_blank=False
        ),
        'approval_decision': DataValidation(
            type="list",
            formula1=f'"{CHECK} Approved,⚠️ Approved with Conditions,❌ Rejected"',
            allow_blank=False
        ),
        'regulatory_review': DataValidation(
            type="list",
            formula1='"Yes,No,To Be Determined"',
            allow_blank=False
        ),
    }

    # NOTE: Do NOT add validations here. They are added per-sheet via
    # finalize_validations() AFTER cells are assigned, to avoid empty
    # sqref entries that trigger Excel "Repaired" warnings.

    return validations


def finalize_validations(ws, validations):
    """Add only data validations that have cells assigned to avoid Excel repair."""
    for dv in validations.values():
        if dv.sqref:
            ws.add_data_validation(dv)


# ============================================================================
# SECTION 3: INSTRUCTIONS & LEGEND SHEET
# ============================================================================

def create_instructions_sheet(ws, styles):
    """Create Instructions & Legend sheet with usage guidance."""
    
    # Header
    ws.merge_cells("A1:G1")
    ws["A1"] = "ISMS-IMP-A.8.32.2  -  Change Types & Categories Assessment\nISO/IEC 27001:2022 - Control A.8.32: Change Management"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 40

    # Document Information Block
    row = 4
    ws[f"A{row}"] = "DOCUMENT INFORMATION"
    ws[f"A{row}"].font = Font(bold=True, size=11)
    
    doc_info = [
        ("Document ID:", "ISMS-IMP-A.8.32.2"),
        ("Assessment Area:", "Change Types & Categories"),
        ("Related Policy:", "ISMS-POL-A.8.32"),
        ("Version:", "1.0"),
        ("Assessment Date:", "[USER INPUT]"),
        ("Completed By:", "[USER INPUT]"),
        ("Organisation:", "[Organisation]"),
        ("Review Cycle:", "Quarterly"),
    ]
    
    row += 1
    for label, value in doc_info:
        ws[f"A{row}"] = label
        ws[f"A{row}"].font = Font(bold=True)
        ws[f"B{row}"] = value
        if "USER INPUT" in value:
            ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        row += 1

    # How to Use This Workbook
    row += 2
    ws.merge_cells(f"A{row}:F{row}")
    ws[f"A{row}"] = "HOW TO USE THIS WORKBOOK"
    ws[f"A{row}"].font = Font(bold=True, size=12, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")

    instructions = [
        "1. Complete the Standard Changes Catalog with YOUR pre-approved changes",
        "2. Document YOUR normal change assessment criteria",
        "3. Define YOUR emergency change triggers and procedures",
        "4. Configure YOUR change risk classification matrix",
        "5. Document YOUR change calendar management approach",
        "6. Review the Summary Dashboard for compliance metrics",
        "7. Maintain the Evidence Register for audit traceability",
        "8. Obtain final approval and sign-off",
    ]

    row += 1
    for instruction in instructions:
        ws[f"A{row}"] = instruction
        ws[f"A{row}"].alignment = Alignment(wrap_text=True)
        ws.row_dimensions[row].height = 30
        row += 1

    # Status Legend
    row += 2
    ws.merge_cells(f"A{row}:F{row}")
    ws[f"A{row}"] = "STATUS LEGEND"
    ws[f"A{row}"].font = Font(bold=True, size=12, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")

    row += 1
    legend_headers = ["Symbol", "Status", "Description", "Color Code"]
    for col_idx, header in enumerate(legend_headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.font = Font(bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")

    legend_data = [
        ("{CHECK}", "Defined", "Criteria/process clearly defined and documented", "Green"),
        ("{WARNING}", "Partial", "Partially defined or inconsistent application", "Yellow"),
        ("{XMARK}", "Not Defined", "Not defined or not documented", "Red"),
        ("📋", "Planned", "Definition planned with target date", "Blue"),
        ("N/A", "Not Applicable", "Not applicable to this environment", "Gray"),
    ]

    row += 1
    for symbol, status, desc, color in legend_data:
        ws[f"A{row}"] = symbol
        ws[f"B{row}"] = status
        ws[f"C{row}"] = desc
        ws[f"D{row}"] = color
        
        # Apply color coding
        if color == "Green":
            ws[f"D{row}"].fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
        elif color == "Yellow":
            ws[f"D{row}"].fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
        elif color == "Red":
            ws[f"D{row}"].fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
        elif color == "Blue":
            ws[f"D{row}"].fill = PatternFill(start_color="B4C7E7", end_color="B4C7E7", fill_type="solid")
        
        row += 1

    # Change Type Decision Tree
    row += 2
    ws.merge_cells(f"A{row}:F{row}")
    ws[f"A{row}"] = "CHANGE TYPE DECISION TREE"
    ws[f"A{row}"].font = Font(bold=True, size=12, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")

    decision_tree = [
        "Is this change:",
        "├─ Pre-approved, low-risk, well-documented? → STANDARD CHANGE",
        "├─ Requires assessment and approval? → NORMAL CHANGE",
        "│   ├─ Low Risk + Low Impact → Expedited Normal Change",
        "│   ├─ Medium Risk/Impact → Standard Normal Change",
        "│   └─ High/Critical Risk/Impact → High-Priority Normal Change",
        "└─ Urgent, meets emergency criteria? → EMERGENCY CHANGE",
        "    ├─ Critical system outage?",
        "    ├─ Security incident?",
        "    ├─ Data loss prevention?",
        "    └─ Regulatory deadline?",
    ]

    row += 1
    for line in decision_tree:
        ws[f"A{row}"] = line
        ws[f"A{row}"].font = Font(name="Calibri", size=9)
        row += 1

    # Acceptable Evidence
    row += 2
    ws.merge_cells(f"A{row}:F{row}")
    ws[f"A{row}"] = "ACCEPTABLE EVIDENCE (Examples)"
    ws[f"A{row}"].font = Font(bold=True, size=12, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")

    evidence_examples = [
        "✓ Standard changes catalog/library",
        "✓ Change classification decision trees",
        "✓ Risk assessment matrices",
        "✓ Emergency change criteria documentation",
        "✓ Change calendar procedures",
        "✓ CAB meeting records (classification decisions)",
        "✓ Change metrics (by type and category)",
        "✓ Training materials on change classification",
        "✓ Audit reports on classification accuracy",
        "✓ Exception/deviation records",
        "✓ Change type definitions document",
        "✓ Historical change data (by type)",
    ]

    row += 1
    for evidence in evidence_examples:
        ws[f"A{row}"] = evidence
        row += 1

    # Column widths
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 45
    ws.column_dimensions["C"].width = 70

    ws.freeze_panes = "A4"


# ============================================================================
# SECTION 4: STANDARD CHANGES CATALOG SHEET
# ============================================================================

def create_standard_changes_catalog(ws, styles):
    """Create Standard Changes Catalog sheet with 50 pre-formatted entries."""
    validations = create_base_validations(ws)
    
    # Header
    ws.merge_cells("A1:M1")
    ws["A1"] = "STANDARD CHANGES CATALOG"
    apply_style(ws["A1"], styles["header"])
    ws.row_dimensions[1].height = 30

    ws.merge_cells("A2:M2")
    ws["A2"] = "Pre-approved, low-risk changes with documented procedures"
    apply_style(ws["A2"], styles["subheader"])

    # Column headers
    row = 4
    headers = ["Change ID", "Change Title", "Description", "Category", "Frequency", "Pre-requisites", 
               "Procedure Location", "Owner", "Approval Date", "Review Date", "Risk Level", "Status", "Evidence"]
    
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_style(cell, styles["column_header"])

    # Create 50 standard change rows
    row += 1
    for i in range(1, 51):
        # Change ID - suggested format
        ws[f"A{row}"] = f"STD-{i:03d}"
        ws[f"A{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Change Title, Description, Pre-requisites, Procedure Location, Owner, Evidence - text
        for col in ["B", "C", "F", "G", "H", "M"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Category dropdown
        validations['change_category'].add(ws[f"D{row}"])
        ws[f"D{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Frequency dropdown
        validations['frequency'].add(ws[f"E{row}"])
        ws[f"E{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Approval Date and Review Date
        for col in ["I", "J"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
            ws[f"{col}{row}"].number_format = 'DD.MM.YYYY'
        
        # Risk Level (Low/Medium only for standard changes)
        validations['std_change_risk'].add(ws[f"K{row}"])
        ws[f"K{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Status dropdown
        validations['std_change_status'].add(ws[f"L{row}"])
        ws[f"L{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Alternating row colors for readability
        if i % 2 == 0:
            for col in range(1, 14):
                cell = ws.cell(row=row, column=col)
                if cell.fill.start_color.rgb != "FFFFCC":
                    cell.fill = PatternFill(start_color="F5F5F5", end_color="F5F5F5", fill_type="solid")
        
        row += 1

    # Summary Metrics
    row += 2
    ws.merge_cells(f"A{row}:C{row}")
    ws[f"A{row}"] = "STANDARD CHANGE SUMMARY METRICS"
    apply_style(ws[f"A{row}"], styles["section_header"])

    row += 1
    metric_headers = ["Metric", "Value", "Notes"]
    for col_idx, header in enumerate(metric_headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_style(cell, styles["column_header"])

    metrics = [
        "Total Standard Changes Defined",
        "Active Standard Changes",
        "Standard Changes Under Review",
        "Standard Changes Requiring Annual Review",
        "Most Common Category",
        "Average Age of Standard Changes",
    ]

    row += 1
    for metric in metrics:
        ws[f"A{row}"] = metric
        ws[f"B{row}"].fill = PatternFill(start_color="E0E0E0", end_color="E0E0E0", fill_type="solid")
        ws[f"B{row}"].value = "[FORMULA]"
        ws[f"C{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        row += 1

    # Column widths
    ws.column_dimensions["A"].width = 12
    ws.column_dimensions["B"].width = 30
    ws.column_dimensions["C"].width = 40
    ws.column_dimensions["D"].width = 18
    ws.column_dimensions["E"].width = 15
    ws.column_dimensions["F"].width = 30
    ws.column_dimensions["G"].width = 30
    ws.column_dimensions["H"].width = 20
    ws.column_dimensions["I"].width = 15
    ws.column_dimensions["J"].width = 15
    ws.column_dimensions["K"].width = 15
    ws.column_dimensions["L"].width = 18
    ws.column_dimensions["M"].width = 25

    ws.freeze_panes = "A5"
    finalize_validations(ws, validations)


# ============================================================================
# SECTION 5: NORMAL CHANGES ASSESSMENT SHEET
# ============================================================================

def create_normal_changes_assessment(ws, styles):
    """Create Normal_Changes_Assessment sheet."""
    validations = create_base_validations(ws)
    
    # Header
    ws.merge_cells("A1:G1")
    ws["A1"] = "NORMAL CHANGES ASSESSMENT"
    apply_style(ws["A1"], styles["header"])
    ws.row_dimensions[1].height = 30

    ws.merge_cells("A2:G2")
    ws["A2"] = "Changes requiring risk assessment, approval, and CAB review"
    apply_style(ws["A2"], styles["subheader"])

    # ==================== NORMAL CHANGE CRITERIA ====================
    row = 4
    ws.merge_cells(f"A{row}:G{row}")
    ws[f"A{row}"] = "NORMAL CHANGE CRITERIA"
    apply_style(ws[f"A{row}"], styles["section_header"])

    row += 1
    criteria_headers = ["Criterion", "Defined", "Documentation Reference", "Assessment Method", "Responsible Role", "Compliance", "Evidence"]
    for col_idx, header in enumerate(criteria_headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_style(cell, styles["column_header"])

    criteria = [
        "Change does not meet Standard criteria",
        "Change is not an emergency",
        "Risk assessment required",
        "Impact assessment required",
        "CAB review required (based on risk)",
        "Business justification required",
        "Implementation plan required",
        "Test plan required",
        "Rollback plan required",
        "Communication plan required",
        "PIR (Post-Implementation Review) required",
        "Change window scheduling required",
    ]

    row += 1
    for criterion in criteria:
        ws[f"A{row}"] = criterion
        
        # Editable cells
        for col in ["C", "D", "E", "G"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Dropdowns
        validations['definition_status'].add(ws[f"B{row}"])
        ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        validations['compliance_status'].add(ws[f"F{row}"])
        ws[f"F{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        row += 1

    # ==================== RISK-BASED APPROVAL PATHS ====================
    row += 2
    ws.merge_cells(f"A{row}:H{row}")
    ws[f"A{row}"] = "RISK-BASED APPROVAL PATHS"
    apply_style(ws[f"A{row}"], styles["section_header"])

    row += 1
    approval_headers = ["Risk Category", "Impact Category", "Approval Authority", "CAB Review", "Typical Timeline", "Success Rate", "Documented", "Evidence"]
    for col_idx, header in enumerate(approval_headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_style(cell, styles["column_header"])

    risk_combinations = [
        ("Low", "Low"), ("Low", "Medium"), ("Low", "High"),
        ("Medium", "Low"), ("Medium", "Medium"), ("Medium", "High"),
        ("High", "Low"), ("High", "Medium"), ("High", "High"),
        ("Critical", "Any"),
    ]

    row += 1
    for risk, impact in risk_combinations:
        ws[f"A{row}"] = risk
        ws[f"B{row}"] = impact
        
        # Editable cells
        for col in ["E", "F", "H"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Dropdowns
        validations['approval_authority'].add(ws[f"C{row}"])
        ws[f"C{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        validations['cab_requirement'].add(ws[f"D{row}"])
        ws[f"D{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        validations['definition_status'].add(ws[f"G{row}"])
        ws[f"G{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        row += 1

    # Column widths
    ws.column_dimensions["A"].width = 35
    ws.column_dimensions["B"].width = 18
    ws.column_dimensions["C"].width = 25
    ws.column_dimensions["D"].width = 20
    ws.column_dimensions["E"].width = 18
    ws.column_dimensions["F"].width = 15
    ws.column_dimensions["G"].width = 18
    ws.column_dimensions["H"].width = 25

    ws.freeze_panes = "A6"
    finalize_validations(ws, validations)


# ============================================================================
# SECTION 6: EMERGENCY CHANGES SHEET
# ============================================================================

def create_emergency_changes(ws, styles):
    """Create Emergency_Changes sheet."""
    validations = create_base_validations(ws)
    
    # Header
    ws.merge_cells("A1:G1")
    ws["A1"] = "EMERGENCY CHANGES"
    apply_style(ws["A1"], styles["header"])
    ws.row_dimensions[1].height = 30

    ws.merge_cells("A2:G2")
    ws["A2"] = "Urgent changes meeting specific emergency criteria with E-CAB approval"
    apply_style(ws["A2"], styles["subheader"])

    # ==================== EMERGENCY CRITERIA DEFINITION ====================
    row = 4
    ws.merge_cells(f"A{row}:F{row}")
    ws[f"A{row}"] = "EMERGENCY CRITERIA DEFINITION"
    apply_style(ws[f"A{row}"], styles["section_header"])

    row += 1
    criteria_headers = ["Emergency Criterion", "Defined", "Specific Triggers", "Escalation Path", "Response Time SLA", "Documented", "Evidence"]
    # Adjust to 7 columns
    for col_idx, header in enumerate(criteria_headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_style(cell, styles["column_header"])

    emergency_criteria = [
        "System Outage (Critical Services)",
        "Security Incident Response",
        "Data Loss Prevention",
        "Regulatory Compliance Deadline",
        "Health & Safety Risk",
        "Business Continuity Threat",
        "[Custom Criterion 1]",
        "[Custom Criterion 2]",
    ]

    row += 1
    for criterion in emergency_criteria:
        ws[f"A{row}"] = criterion
        
        # Editable cells
        for col in ["C", "D", "E", "G"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Dropdowns
        validations['emergency_criteria_definition'].add(ws[f"B{row}"])
        ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        validations['definition_status'].add(ws[f"F{row}"])
        ws[f"F{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        row += 1

    # ==================== EMERGENCY CHANGE PROCESS REQUIREMENTS ====================
    row += 2
    ws.merge_cells(f"A{row}:F{row}")
    ws[f"A{row}"] = "EMERGENCY CHANGE PROCESS REQUIREMENTS"
    apply_style(ws[f"A{row}"], styles["section_header"])

    row += 1
    req_headers = ["Requirement", "Implemented", "Process Description", "Responsible Role", "Exceptions Allowed", "Compliance", "Evidence"]
    for col_idx, header in enumerate(req_headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_style(cell, styles["column_header"])

    requirements = [
        "Emergency criteria must be met",
        "E-CAB convened",
        "Minimum E-CAB members defined",
        "Emergency approval documented",
        "Risk acceptance explicit",
        "Communication immediate",
        "Implementation window immediate",
        "Rollback plan prepared (where feasible)",
        "Incident ticket linked",
        "Mandatory PIR within 2 business days",
        "Retrospective CAB review",
        "Emergency change metrics tracked",
    ]

    row += 1
    for requirement in requirements:
        ws[f"A{row}"] = requirement
        
        # Editable cells
        for col in ["C", "D", "G"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Dropdowns
        validations['implementation_level'].add(ws[f"B{row}"])
        ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        validations['exceptions_allowed'].add(ws[f"E{row}"])
        ws[f"E{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        validations['compliance_status'].add(ws[f"F{row}"])
        ws[f"F{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        row += 1

    # ==================== EMERGENCY CHANGE METRICS ====================
    row += 2
    ws.merge_cells(f"A{row}:E{row}")
    ws[f"A{row}"] = "EMERGENCY CHANGE METRICS"
    apply_style(ws[f"A{row}"], styles["section_header"])

    row += 1
    metric_headers = ["Metric", "Target", "Current (Last Quarter)", "Status", "Notes"]
    for col_idx, header in enumerate(metric_headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_style(cell, styles["column_header"])

    metrics = [
        "Emergency changes as % of total changes",
        "Average E-CAB response time",
        "Emergency changes with PIR completed",
        "Emergency changes leading to incidents",
        "Retrospective CAB review completion",
        "False emergency declarations",
        "Emergency change success rate",
    ]

    row += 1
    for metric in metrics:
        ws[f"A{row}"] = metric
        
        # Target and Notes - editable
        for col in ["B", "E"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Current - formula (editable for now)
        ws[f"C{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Status - calculated
        ws[f"D{row}"].fill = PatternFill(start_color="E0E0E0", end_color="E0E0E0", fill_type="solid")
        ws[f"D{row}"].value = "[FORMULA]"
        
        row += 1

    # Column widths
    ws.column_dimensions["A"].width = 35
    ws.column_dimensions["B"].width = 20
    ws.column_dimensions["C"].width = 25
    ws.column_dimensions["D"].width = 25
    ws.column_dimensions["E"].width = 20
    ws.column_dimensions["F"].width = 18
    ws.column_dimensions["G"].width = 25

    ws.freeze_panes = "A6"
    finalize_validations(ws, validations)


# ============================================================================
# SECTION 7: CHANGE RISK CLASSIFICATION SHEET
# ============================================================================

def create_change_risk_classification(ws, styles):
    """Create Change_Risk_Classification sheet with risk matrix."""
    validations = create_base_validations(ws)
    
    # Header
    ws.merge_cells("A1:H1")
    ws["A1"] = "CHANGE RISK CLASSIFICATION MATRIX"
    apply_style(ws["A1"], styles["header"])
    ws.row_dimensions[1].height = 30

    ws.merge_cells("A2:H2")
    ws["A2"] = "Risk = Impact × Likelihood methodology"
    apply_style(ws["A2"], styles["subheader"])

    # ==================== IMPACT LEVEL DEFINITIONS ====================
    row = 4
    ws.merge_cells(f"A{row}:H{row}")
    ws[f"A{row}"] = "IMPACT LEVEL DEFINITIONS"
    apply_style(ws[f"A{row}"], styles["section_header"])

    row += 1
    impact_headers = ["Impact Level", "User Count Affected", "Service Downtime Potential", "Recovery Time", "Data Loss Risk", "Financial Impact", "Documented", "Evidence"]
    for col_idx, header in enumerate(impact_headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_style(cell, styles["column_header"])

    impact_levels = ["Low", "Medium", "High", "Critical"]

    row += 1
    for level in impact_levels:
        ws[f"A{row}"] = level
        
        # Editable cells
        for col in ["D", "F", "H"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Dropdowns
        validations['user_count'].add(ws[f"B{row}"])
        ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        validations['downtime_potential'].add(ws[f"C{row}"])
        ws[f"C{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        validations['data_loss_risk'].add(ws[f"E{row}"])
        ws[f"E{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        validations['definition_status'].add(ws[f"G{row}"])
        ws[f"G{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        row += 1

    # ==================== LIKELIHOOD LEVEL DEFINITIONS ====================
    row += 2
    ws.merge_cells(f"A{row}:H{row}")
    ws[f"A{row}"] = "LIKELIHOOD LEVEL DEFINITIONS"
    apply_style(ws[f"A{row}"], styles["section_header"])

    row += 1
    likelihood_headers = ["Likelihood Level", "Failure Probability", "Complexity", "Dependencies", "Testing Maturity", "Historical Success Rate", "Documented", "Evidence"]
    for col_idx, header in enumerate(likelihood_headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_style(cell, styles["column_header"])

    likelihood_levels = ["Low", "Medium", "High"]

    row += 1
    for level in likelihood_levels:
        ws[f"A{row}"] = level
        
        # Editable cells
        for col in ["B", "D", "F", "H"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Dropdowns
        validations['complexity'].add(ws[f"C{row}"])
        ws[f"C{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        validations['testing_maturity'].add(ws[f"E{row}"])
        ws[f"E{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        validations['definition_status'].add(ws[f"G{row}"])
        ws[f"G{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        row += 1

    # ==================== RISK MATRIX ====================
    row += 2
    ws.merge_cells(f"A{row}:E{row}")
    ws[f"A{row}"] = "RISK MATRIX (Impact × Likelihood)"
    apply_style(ws[f"A{row}"], styles["section_header"])

    row += 1
    # Risk matrix headers
    ws[f"A{row}"] = ""
    ws[f"B{row}"] = "Low Impact"
    ws[f"C{row}"] = "Medium Impact"
    ws[f"D{row}"] = "High Impact"
    ws[f"E{row}"] = "Critical Impact"
    for col in ["A", "B", "C", "D", "E"]:
        ws[f"{col}{row}"].font = Font(bold=True)
        ws[f"{col}{row}"].fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")

    # Risk matrix data with color coding
    risk_matrix = [
        ("Low Likelihood", "LOW RISK", "LOW RISK", "MEDIUM RISK", "HIGH RISK"),
        ("Medium Likelihood", "LOW RISK", "MEDIUM RISK", "HIGH RISK", "CRITICAL RISK"),
        ("High Likelihood", "MEDIUM RISK", "HIGH RISK", "CRITICAL RISK", "CRITICAL RISK"),
    ]

    row += 1
    for likelihood, low, medium, high, critical in risk_matrix:
        ws[f"A{row}"] = likelihood
        ws[f"A{row}"].font = Font(bold=True)
        
        ws[f"B{row}"] = low
        ws[f"C{row}"] = medium
        ws[f"D{row}"] = high
        ws[f"E{row}"] = critical
        
        # Apply risk color coding
        for col, value in [("B", low), ("C", medium), ("D", high), ("E", critical)]:
            if "LOW" in value:
                ws[f"{col}{row}"].fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
            elif "MEDIUM" in value:
                ws[f"{col}{row}"].fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
            elif "HIGH" in value:
                ws[f"{col}{row}"].fill = PatternFill(start_color="FFD966", end_color="FFD966", fill_type="solid")
            elif "CRITICAL" in value:
                ws[f"{col}{row}"].fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
            
            ws[f"{col}{row}"].alignment = Alignment(horizontal="center", vertical="center")
            ws[f"{col}{row}"].font = Font(bold=True)
        
        row += 1

    # Column widths
    ws.column_dimensions["A"].width = 25
    ws.column_dimensions["B"].width = 22
    ws.column_dimensions["C"].width = 22
    ws.column_dimensions["D"].width = 22
    ws.column_dimensions["E"].width = 22
    ws.column_dimensions["F"].width = 20
    ws.column_dimensions["G"].width = 18
    ws.column_dimensions["H"].width = 25

    ws.freeze_panes = "A6"
    finalize_validations(ws, validations)


# ============================================================================
# SECTION 8: CHANGE CALENDAR MANAGEMENT SHEET
# ============================================================================

def create_change_calendar_management(ws, styles):
    """Create Change Calendar Management sheet."""
    validations = create_base_validations(ws)
    
    # Header
    ws.merge_cells("A1:G1")
    ws["A1"] = "CHANGE CALENDAR MANAGEMENT"
    apply_style(ws["A1"], styles["header"])
    ws.row_dimensions[1].height = 30

    ws.merge_cells("A2:G2")
    ws["A2"] = "Scheduling, blackout windows, and conflict detection"
    apply_style(ws["A2"], styles["subheader"])

    # ==================== CHANGE WINDOW DEFINITIONS ====================
    row = 4
    ws.merge_cells(f"A{row}:G{row}")
    ws[f"A{row}"] = "CHANGE WINDOW DEFINITIONS"
    apply_style(ws[f"A{row}"], styles["section_header"])

    row += 1
    window_headers = ["Change Window", "Days/Times", "Applicable Change Types", "Approval Required", "Advance Notice", "Documented", "Evidence"]
    for col_idx, header in enumerate(window_headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_style(cell, styles["column_header"])

    change_windows = [
        "Standard Maintenance Window",
        "Business Hours (Restricted)",
        "After-Hours Window",
        "Emergency Window",
        "[Custom Window 1]",
        "[Custom Window 2]",
    ]

    row += 1
    for window in change_windows:
        ws[f"A{row}"] = window
        
        # Editable cells
        for col in ["B", "E", "G"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Dropdowns
        validations['applicable_changes'].add(ws[f"C{row}"])
        ws[f"C{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        validations['yes_no'].add(ws[f"D{row}"])
        ws[f"D{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        validations['definition_status'].add(ws[f"F{row}"])
        ws[f"F{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        row += 1

    # ==================== BLACKOUT PERIODS ====================
    row += 2
    ws.merge_cells(f"A{row}:H{row}")
    ws[f"A{row}"] = "BLACKOUT PERIODS"
    apply_style(ws[f"A{row}"], styles["section_header"])

    row += 1
    blackout_headers = ["Blackout Period", "Start Date", "End Date", "Reason", "Affected Systems/Services", "Exceptions Allowed", "Exception Approver", "Documented", "Evidence"]
    # Adjust to 9 columns
    for col_idx, header in enumerate(blackout_headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_style(cell, styles["column_header"])

    row += 1
    # 12 rows for blackout periods
    for i in range(12):
        # Blackout Period name - editable
        ws[f"A{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Start and End Date
        for col in ["B", "C"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
            ws[f"{col}{row}"].number_format = 'DD.MM.YYYY'
        
        # Affected Systems, Exception Approver, Evidence - editable
        for col in ["E", "G", "I"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Reason dropdown
        validations['blackout_reason'].add(ws[f"D{row}"])
        ws[f"D{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Exceptions Allowed dropdown
        validations['exceptions_allowed'].add(ws[f"F{row}"])
        ws[f"F{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        # Documented dropdown
        validations['definition_status'].add(ws[f"H{row}"])
        ws[f"H{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        row += 1

    # Column widths
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 15
    ws.column_dimensions["C"].width = 15
    ws.column_dimensions["D"].width = 20
    ws.column_dimensions["E"].width = 30
    ws.column_dimensions["F"].width = 18
    ws.column_dimensions["G"].width = 20
    ws.column_dimensions["H"].width = 18
    ws.column_dimensions["I"].width = 25

    ws.freeze_panes = "A6"
    finalize_validations(ws, validations)


# ============================================================================
# SECTION 8.5: CLASSIFICATION METRICS SHEET
# ============================================================================

def create_classification_metrics(ws, styles):
    """Create Classification Metrics sheet tracking change classification metrics."""
    validations = create_base_validations(ws)

    # Header
    ws.merge_cells("A1:H1")
    ws["A1"] = "CHANGE CLASSIFICATION METRICS"
    apply_style(ws["A1"], styles["header"])
    ws.row_dimensions[1].height = 30

    ws.merge_cells("A2:H2")
    ws["A2"] = "Track metrics related to change type distribution and classification accuracy"
    apply_style(ws["A2"], styles["subheader"])

    # ==================== CLASSIFICATION METRICS ====================
    row = 4
    ws.merge_cells(f"A{row}:H{row}")
    ws[f"A{row}"] = "CHANGE TYPE DISTRIBUTION METRICS"
    apply_style(ws[f"A{row}"], styles["section_header"])
    row += 1

    headers = ["Metric", "Target", "Current", "Period", "Trend", "Status", "Owner", "Notes"]
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_style(cell, styles["column_header"])
    row += 1

    metrics = [
        ("Standard Changes %", ">60%", "", "Monthly", "", "", "", ""),
        ("Normal Changes %", "25-35%", "", "Monthly", "", "", "", ""),
        ("Emergency Changes %", "<5%", "", "Monthly", "", "", "", ""),
        ("Classification Accuracy", ">95%", "", "Monthly", "", "", "", ""),
        ("Re-Classification Rate", "<2%", "", "Monthly", "", "", "", ""),
        ("Standard Catalog Utilization", ">80%", "", "Monthly", "", "", "", ""),
    ]

    for metric_data in metrics:
        for col_idx, value in enumerate(metric_data, 1):
            cell = ws.cell(row=row, column=col_idx, value=value)
            if col_idx > 2:
                apply_style(cell, styles["input_cell"])
        row += 1

    row += 2

    # ==================== CLASSIFICATION ACCURACY ====================
    ws.merge_cells(f"A{row}:H{row}")
    ws[f"A{row}"] = "CLASSIFICATION ACCURACY TRACKING"
    apply_style(ws[f"A{row}"], styles["section_header"])
    row += 1

    accuracy_headers = ["Period", "Total Changes", "Correctly Classified", "Misclassified", "Accuracy %", "Review Date", "Reviewer"]
    for col_idx, header in enumerate(accuracy_headers, 1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        apply_style(cell, styles["column_header"])
    row += 1

    for _ in range(6):
        for col_idx in range(1, 8):
            cell = ws.cell(row=row, column=col_idx, value="")
            apply_style(cell, styles["input_cell"])
        row += 1

    # Column widths
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 15
    ws.column_dimensions["C"].width = 15
    ws.column_dimensions["D"].width = 15
    ws.column_dimensions["E"].width = 15
    ws.column_dimensions["F"].width = 15
    ws.column_dimensions["G"].width = 18
    ws.column_dimensions["H"].width = 25

    ws.freeze_panes = "A6"
    finalize_validations(ws, validations)


# ============================================================================
# SECTION 9: SUMMARY DASHBOARD SHEET
# ============================================================================

def create_summary_dashboard(ws, styles):
    """Create Summary Dashboard with standard compliance table and metrics."""
    thin = Side(style="thin")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    # Header
    ws.merge_cells("A1:G1")
    ws["A1"] = "CHANGE TYPES ASSESSMENT - COMPLIANCE SUMMARY"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 35

    ws.merge_cells("A2:G2")
    ws["A2"] = "ISO/IEC 27001:2022 \u2014 Control A.8.32: Change Management"
    ws["A2"].font = Font(name="Calibri", size=11, italic=True)
    ws["A2"].alignment = Alignment(horizontal="left", vertical="center")

    # --- TABLE 1: COMPLIANCE OVERVIEW ---
    row = 3
    ws.merge_cells(f"A{row}:G{row}")
    ws[f"A{row}"] = "TABLE 1: COMPLIANCE OVERVIEW"
    ws[f"A{row}"].font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="left", vertical="center")

    headers = ["Assessment Area", "Total Requirements", "Compliant", "Partially Compliant", "Non-Compliant", "N/A", "Compliance %"]
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=4, column=col_idx, value=header)
        cell.font = Font(name="Calibri", size=10, bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border

    assessment_areas = [
        "Standard Changes Catalog",
        "Normal Change Classification",
        "Emergency Change Procedures",
        "Risk Assessment Matrix",
        "Change Calendar Management",
    ]

    for i, area in enumerate(assessment_areas):
        r = 5 + i
        ws[f"A{r}"] = area
        ws[f"A{r}"].font = Font(name="Calibri", size=10)
        ws[f"A{r}"].border = border
        for col in "BCDEF":
            cell = ws[f"{col}{r}"]
            cell.fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
            cell.border = border
            cell.alignment = Alignment(horizontal="center", vertical="center")
        ws[f"G{r}"].border = border
        ws[f"G{r}"].alignment = Alignment(horizontal="center", vertical="center")

    # TOTAL row with SUM formulas
    total_row = 5 + len(assessment_areas)
    ws[f"A{total_row}"] = "TOTAL"
    ws[f"A{total_row}"].font = Font(name="Calibri", size=10, bold=True)
    ws[f"A{total_row}"].fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
    ws[f"A{total_row}"].border = border
    for col_letter in "BCDEF":
        cell = ws[f"{col_letter}{total_row}"]
        cell.value = f"=SUM({col_letter}5:{col_letter}{total_row - 1})"
        cell.font = Font(name="Calibri", size=10, bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.border = border
        cell.alignment = Alignment(horizontal="center", vertical="center")
    ws[f"G{total_row}"] = f'=IF((B{total_row}-F{total_row})=0,"0%",ROUND(C{total_row}/(B{total_row}-F{total_row})*100,1)&"%")'
    ws[f"G{total_row}"].font = Font(name="Calibri", size=10, bold=True)
    ws[f"G{total_row}"].fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
    ws[f"G{total_row}"].border = border
    ws[f"G{total_row}"].alignment = Alignment(horizontal="center", vertical="center")

    # --- TABLE 2: KEY METRICS ---
    met_row = total_row + 2
    ws.merge_cells(f"A{met_row}:G{met_row}")
    ws[f"A{met_row}"] = "TABLE 2: KEY METRICS"
    ws[f"A{met_row}"].font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    ws[f"A{met_row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws[f"A{met_row}"].alignment = Alignment(horizontal="left", vertical="center")

    metrics = [
        ("Standard Change Utilisation Rate", "[enter %]"),
        ("Emergency Change Rate", "[enter %]"),
        ("Classification Accuracy", "[enter %]"),
        ("Risk Matrix Coverage", "[enter %]"),
    ]
    for i, (metric, placeholder) in enumerate(metrics):
        r = met_row + 1 + i
        ws[f"A{r}"] = metric
        ws[f"A{r}"].font = Font(name="Calibri", size=10, bold=True)
        ws[f"A{r}"].border = border
        ws.merge_cells(f"B{r}:G{r}")
        ws[f"B{r}"] = placeholder
        ws[f"B{r}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        ws[f"B{r}"].border = border

    # --- TABLE 3: CRITICAL FINDINGS ---
    crit_row = met_row + 1 + len(metrics) + 1
    ws.merge_cells(f"A{crit_row}:G{crit_row}")
    ws[f"A{crit_row}"] = "TABLE 3: CRITICAL FINDINGS"
    ws[f"A{crit_row}"].font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    ws[f"A{crit_row}"].fill = PatternFill(start_color="C00000", end_color="C00000", fill_type="solid")
    ws[f"A{crit_row}"].alignment = Alignment(horizontal="left", vertical="center")

    find_headers = ["Finding", "Severity", "Owner", "Due Date", "Status"]
    for col_idx, h in enumerate(find_headers, start=1):
        cell = ws.cell(row=crit_row + 1, column=col_idx, value=h)
        cell.font = Font(name="Calibri", size=10, bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.border = border
        cell.alignment = Alignment(horizontal="center", vertical="center")
    for i in range(5):
        r = crit_row + 2 + i
        for col in range(1, 6):
            cell = ws.cell(row=r, column=col)
            cell.fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
            cell.border = border

    # Column widths (standard)
    for col, w in [("A", 40), ("B", 16), ("C", 16), ("D", 18), ("E", 18), ("F", 12), ("G", 15)]:
        ws.column_dimensions[col].width = w

    ws.freeze_panes = "A4"


# ============================================================================
# SECTION 10: EVIDENCE REGISTER SHEET
# ============================================================================

def create_evidence_register(ws, styles):
    """Create standard 8-column Evidence Register with 100 rows."""
    thin = Side(style="thin")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    # Header
    ws.merge_cells("A1:H1")
    ws["A1"] = "EVIDENCE REGISTER"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 35

    # Subtitle
    ws.merge_cells("A2:H2")
    ws["A2"] = "Document all evidence collected during this assessment"
    ws["A2"].font = Font(name="Calibri", size=11, italic=True)
    ws["A2"].alignment = Alignment(horizontal="left", vertical="center")

    # Column headers (row 4)
    headers = [
        "Evidence ID", "Assessment Area", "Evidence Type", "Description",
        "Location / Path", "Date Collected", "Collected By", "Verification Status",
    ]
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=4, column=col_idx, value=header)
        cell.font = Font(name="Calibri", size=10, bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border

    # Evidence type dropdown
    ev_type_dv = DataValidation(
        type="list",
        formula1='"Policy Document,Process Record,System Screenshot,Configuration Export,Audit Log,Training Record,Test Result,Risk Assessment,Meeting Minutes,Other"',
        allow_blank=True,
    )
    ev_type_dv.error = "Please select a valid evidence type"
    ev_type_dv.errorTitle = "Invalid Evidence Type"
    ws.add_data_validation(ev_type_dv)

    # Verification status dropdown
    ver_status_dv = DataValidation(
        type="list",
        formula1=f'"{CHECK} Verified,{WARNING} Pending,{XMARK} Not Verified,N/A"',
        allow_blank=True,
    )
    ver_status_dv.error = "Please select a valid status"
    ver_status_dv.errorTitle = "Invalid Status"
    ws.add_data_validation(ver_status_dv)

    # 100 data rows (5-104)
    for i in range(1, 101):
        row = 4 + i
        # Evidence ID (gray font, no fill)
        ws[f"A{row}"] = f"EV-{i:03d}"
        ws[f"A{row}"].font = Font(name="Calibri", size=10, color="808080")
        ws[f"A{row}"].border = border
        ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")
        # Cols B-H: yellow fill + border
        for col in range(2, 9):
            cell = ws.cell(row=row, column=col)
            cell.fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
            cell.border = border
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        # Dropdowns
        ev_type_dv.add(ws[f"C{row}"])
        ver_status_dv.add(ws[f"H{row}"])

    # Column widths
    for col, w in [("A", 15), ("B", 25), ("C", 22), ("D", 40), ("E", 45), ("F", 16), ("G", 20), ("H", 22)]:
        ws.column_dimensions[col].width = w

    ws.freeze_panes = "A5"


# ============================================================================
# SECTION 11: APPROVAL SIGN-OFF SHEET
# ============================================================================

def create_approval_signoff(ws, styles):
    """Create standard Approval Sign-Off with 3-section approval workflow."""
    thin = Side(style="thin")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    # Header
    ws.merge_cells("A1:E1")
    ws["A1"] = "ASSESSMENT APPROVAL AND SIGN-OFF"
    ws["A1"].font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    ws["A1"].fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 35

    # --- ASSESSMENT SUMMARY ---
    row = 3
    ws.merge_cells(f"A{row}:E{row}")
    ws[f"A{row}"] = "ASSESSMENT SUMMARY"
    ws[f"A{row}"].font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="left", vertical="center")

    # Assessment Status dropdown
    status_dv = DataValidation(
        type="list",
        formula1='"Draft,Final,Requires remediation,Re-assessment required"',
        allow_blank=True,
    )
    ws.add_data_validation(status_dv)

    summary_fields = [
        ("Assessment Document:", "ISMS-IMP-A.8.32.2 \u2014 Change Types & Categories Assessment", False),
        ("Assessment Period:", "", True),
        ("Assessment Scope:", "", True),
        ("Overall Compliance:", "", True),
        ("Assessment Status:", "", "dropdown"),
    ]
    row = 4
    for label, value, editable in summary_fields:
        ws[f"A{row}"] = label
        ws[f"A{row}"].font = Font(name="Calibri", size=10, bold=True)
        ws.merge_cells(f"B{row}:E{row}")
        ws[f"B{row}"] = value
        if editable == "dropdown":
            status_dv.add(ws[f"B{row}"])
            ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        elif editable:
            ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        row += 1

    # --- Helper for approver sections ---
    def _approver_section(start_row, title, fill_color):
        ws.merge_cells(f"A{start_row}:E{start_row}")
        ws[f"A{start_row}"] = title
        ws[f"A{start_row}"].font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
        ws[f"A{start_row}"].fill = PatternFill(start_color=fill_color, end_color=fill_color, fill_type="solid")
        ws[f"A{start_row}"].alignment = Alignment(horizontal="left", vertical="center")
        r = start_row + 1
        for field in ["Name:", "Title:", "Date:", "Signature:", "Comments:"]:
            ws[f"A{r}"] = field
            ws[f"A{r}"].font = Font(name="Calibri", size=10, bold=True)
            ws.merge_cells(f"B{r}:E{r}")
            ws[f"B{r}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
            ws[f"B{r}"].border = border
            r += 1
        return r

    # COMPLETED BY
    row += 1
    row = _approver_section(row, "COMPLETED BY", "4472C4")

    # REVIEWED BY
    row += 1
    row = _approver_section(row, "REVIEWED BY", "4472C4")

    # APPROVED BY — CISO
    row += 1
    row = _approver_section(row, "APPROVED BY \u2014 CISO", "003366")

    # --- FINAL DECISION ---
    ws[f"A{row}"] = "FINAL DECISION:"
    ws[f"A{row}"].font = Font(name="Calibri", size=10, bold=True)
    ws.merge_cells(f"B{row}:E{row}")
    ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
    ws[f"B{row}"].border = border
    decision_dv = DataValidation(
        type="list",
        formula1='"Approved,Approved with Conditions,Rejected,Deferred"',
        allow_blank=True,
    )
    ws.add_data_validation(decision_dv)
    decision_dv.add(ws[f"B{row}"])

    # --- NEXT REVIEW DETAILS ---
    row += 3
    ws.merge_cells(f"A{row}:E{row}")
    ws[f"A{row}"] = "NEXT REVIEW DETAILS"
    ws[f"A{row}"].font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="left", vertical="center")

    for field in ["Next Review Date:", "Review Frequency:", "Scheduled Reviewer:"]:
        row += 1
        ws[f"A{row}"] = field
        ws[f"A{row}"].font = Font(name="Calibri", size=10, bold=True)
        ws.merge_cells(f"B{row}:E{row}")
        ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        ws[f"B{row}"].border = border

    # Column widths
    for col, w in [("A", 32), ("B", 25), ("C", 20), ("D", 20), ("E", 20)]:
        ws.column_dimensions[col].width = w

    ws.freeze_panes = "A3"


# ============================================================================
# SECTION 12: MAIN EXECUTION FUNCTION
# ============================================================================

def main():
    """
    Main execution function - orchestrates workbook creation.
    
    Philosophy: Create evidence-based assessment tools for change classification,
    not checkbox compliance theater.
    """
    logger.info("=" * 78)
    logger.info("ISMS-IMP-A.8.32.2 - Change Types & Categories Assessment Generator")
    logger.info("ISO/IEC 27001:2022 Control A.8.32: Change Management")
    logger.info("=" * 78)
    logger.info("\n🎯 Systems Engineering Approach: Evidence-Based Compliance")
    logger.info(f"{CHART} Technology-Agnostic: Works with ANY change classification approach")
    logger.info(f"{LOCK} Audit-Ready: Comprehensive evidence collection")
    logger.info("\n" + "─" * 78)

    # Create workbook and setup styles
    logger.info("\n[Phase 1] Initializing workbook structure...")
    wb = create_workbook()
    styles = setup_styles()
    logger.info("{CHECK} Workbook created with 9 sheets")

    # Create all sheets
    logger.info("\n[Phase 2] Generating assessment sheets...")

    logger.info("  [1/10] Creating Instructions & Legend...")
    create_instructions_sheet(wb["Instructions & Legend"], styles)
    logger.info("  ✅ Instructions complete")

    logger.info("  [2/10] Creating Standard Changes Catalog...")
    create_standard_changes_catalog(wb["Standard Changes Catalog"], styles)
    logger.info("  ✅ Standard changes catalog complete (50 entries)")

    logger.info("  [3/10] Creating Normal Change Classification...")
    create_normal_changes_assessment(wb["Normal Change Classification"], styles)
    logger.info("  ✅ Normal change classification complete")

    logger.info("  [4/10] Creating Emergency Change Procedures...")
    create_emergency_changes(wb["Emergency Change Procedures"], styles)
    logger.info("  ✅ Emergency change procedures complete")

    logger.info("  [5/10] Creating Risk Assessment Matrix...")
    create_change_risk_classification(wb["Risk Assessment Matrix"], styles)
    logger.info("  ✅ Risk assessment matrix complete")

    logger.info("  [6/10] Creating Change Calendar Management...")
    create_change_calendar_management(wb["Change Calendar Management"], styles)
    logger.info("  ✅ Change calendar and blackout periods complete")

    logger.info("  [7/10] Creating Classification Metrics...")
    create_classification_metrics(wb["Classification Metrics"], styles)
    logger.info("  ✅ Classification metrics complete")

    logger.info("  [8/10] Creating Evidence Register...")
    create_evidence_register(wb["Evidence Register"], styles)
    logger.info("  ✅ Evidence register complete (100 evidence rows)")

    logger.info("  [9/10] Creating Summary Dashboard...")
    create_summary_dashboard(wb["Summary Dashboard"], styles)
    logger.info("  ✅ Dashboard complete (compliance metrics)")

    logger.info("  [10/10] Creating Approval Sign-Off...")
    create_approval_signoff(wb["Approval Sign-Off"], styles)
    logger.info("  ✅ Approval workflow complete (3-level sign-off)")

    # Save workbook
    logger.info("\n[Phase 3] Finalizing and saving workbook...")
    filename = f"ISMS-IMP-A.8.32.2_Change_Types_Categories_Assessment_{datetime.now().strftime('%Y%m%d')}.xlsx"
    
    try:
        wb.save(filename)
        logger.info(f"{CHECK} SUCCESS: {filename}")
    except Exception as e:
        logger.error(f"{XMARK} ERROR saving workbook: {e}")
        return 1

    # Summary
    logger.info("\n" + "=" * 78)
    logger.info("📋 WORKBOOK STRUCTURE SUMMARY")
    logger.info("=" * 78)
    logger.info("\n📄 Assessment Sheets (10 per IMP specification):")
    logger.info("  • Instructions & Legend (usage guidance)")
    logger.info("  • Standard Changes Catalog (50 pre-approved changes)")
    logger.info("  • Normal Change Classification (risk-based approval paths)")
    logger.info("  • Emergency Change Procedures (E-CAB procedures, <5% target)")
    logger.info("  • Risk Assessment Matrix (Impact x Likelihood matrix)")
    logger.info("  • Change Calendar Management (blackout periods)")
    logger.info("  • Classification Metrics (distribution and accuracy)")
    logger.info("\n📊 Analysis & Governance:")
    logger.info("  • Evidence Register (100 evidence entries)")
    logger.info("  • Summary Dashboard (compliance metrics)")
    logger.info("  • Approval Sign-Off (3-level approval workflow)")
    logger.info("\n" + "─" * 78)
    logger.info("📈 ASSESSMENT CAPABILITIES:")
    logger.info("  • 50 standard changes catalog entries")
    logger.info("  • Risk matrix (4 impact × 3 likelihood levels)")
    logger.info("  • Emergency change metrics (<5% target)")
    logger.info("  • Change calendar with blackout periods")
    logger.info("  • 12 policy requirements mapped")
    logger.info("  • 100 evidence documentation entries")
    logger.info("  • Automated compliance calculations")
    logger.info("\n" + "─" * 78)
    logger.info(f"{TARGET} KEY FEATURES:")
    logger.info("  ✅ Technology-agnostic (works with ANY change management approach)")
    logger.info("  ✅ Standard/Normal/Emergency change types defined")
    logger.info("  ✅ Risk-based classification methodology")
    logger.info("  ✅ E-CAB procedures documented")
    logger.info("  ✅ Comprehensive evidence collection")
    logger.info("  ✅ Audit readiness assessment")
    logger.info("  ✅ Quarterly review cycle support")
    logger.info("\n" + "=" * 78)
    logger.info(f"{ROCKET} NEXT STEPS:")
    logger.info("  1. Open the generated workbook")
    logger.info("  2. Review Instructions & Legend sheet first")
    logger.info("  3. Populate Standard Changes Catalog with YOUR pre-approved changes")
    logger.info("  4. Document YOUR normal change criteria")
    logger.info("  5. Define YOUR emergency change triggers")
    logger.info("  6. Configure YOUR risk classification matrix")
    logger.info("  7. Document YOUR change calendar and blackout periods")
    logger.info("  8. Review Summary Dashboard for compliance status")
    logger.info("  9. Document evidence in Evidence Register")
    logger.info("  10. Obtain final approval via Approval Sign-Off")
    logger.info("\n💡 PRO TIP:")
    logger.info("  If your emergency changes consistently stay below 5% of total changes")
    logger.info("  and your risk classifications accurately predict change outcomes,")
    logger.info("  you've moved beyond checkbox compliance to operational excellence.")
    logger.info("\n" + "=" * 78)
    logger.info('\n"The first principle is that you must not fool yourself')
    logger.info('— and you are the easiest person to fool." - Richard Feynman')
    logger.info("\n🎭 This is not cargo cult ISMS. This is evidence-based compliance.")
    logger.info("=" * 78 + "\n")

    return 0


if __name__ == "__main__":
    exit(main())

# =============================================================================
# QA_VERIFIED: 2026-02-10
# QA_STATUS: PASSED - STANDARDISATION COMPLETE
# QA_TOOL: Claude Code Standardisation
# CHANGES: Tab names (underscores->spaces), Dashboard (real SUM formulas, TABLE banners,
#          standard widths), Evidence Register (9->8 cols, gray font EV IDs),
#          Approval Sign-Off (standard 3-section), Related Policy fixed, British English
# =============================================================================
