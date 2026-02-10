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
ISMS-IMP-A.8.31.2 - Environment Access Control Assessment Excel Generator
================================================================================

ISO/IEC 27001:2022 Control A.8.31: Separation of Development, Test and Production
Assessment Domain 2 of 3: Environment Access Control

--------------------------------------------------------------------------------
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR YOUR ORGANIZATION
--------------------------------------------------------------------------------

This script is a TEMPLATE/SAMPLE implementation and MUST be adapted to match
your organization's specific access control policies, IAM structure, and
production access requirements.

Key customization areas:
1. Role definitions (developer, operator, admin per your RBAC)
2. Production access policies (zero-trust, break-glass procedures)
3. PAM integration (CyberArk, HashiCorp per your tooling)
4. Monitoring and alerting thresholds (aligned with SOC capabilities)
5. Compliance criteria (per your governance requirements)

DO NOT use this script without reviewing and adapting all sections marked
with "# CUSTOMIZE:" comments throughout the code.

Reference Pattern: Based on ISMS-A.8.24 Assessment Framework (adapted for environment separation)

--------------------------------------------------------------------------------
DESCRIPTION
--------------------------------------------------------------------------------

Generates Excel assessment workbook for evaluating environment access control
compliance per ISO/IEC 27001:2022 Control A.8.31.

**Purpose:**
Creates structured assessment for environment access restrictions including:
- Developer production access verification (should be zero/break-glass only)
- Environment-specific access matrices (who can access which environment)
- Production credential management (PAM vault usage)
- Cross-environment access attempt monitoring

**Assessment Focus:**
- Production access restrictions (developers should NOT have production access)
- Environment access provisioning (role-based per environment)
- Emergency access procedures (break-glass workflows, time-limited)
- Access monitoring and alerting (unauthorized cross-environment attempts)

**Usage:**
    python3 generate_a831_2_environment_access.py
    
    Output: ISMS_IMP_A_8_31_2_Environment_Access_Control_YYYYMMDD.xlsx

**Workbook Structure:**
- Executive Summary (access compliance status, policy violations)
- Gap Analysis (unauthorized access, missing restrictions)
- User Environment Matrix (user → environment access mapping)
- Production Access Audit (developers with prod access - should be 0)
- Access Provisioning (how access is granted per environment)
- Emergency Access Log (break-glass usage, post-incident reviews)
- Credential Management (env-specific credentials, PAM integration)
- Evidence Register (access logs, IAM policies, RBAC configs)
- Action Items (access revocations, policy enforcement)

**Integration:**
- Consolidates into A.8.31 Compliance Dashboard
- Links to A.5.15-16-18 (IAM), A.8.2-3-5 (Auth-PAM)
- Supports incident response (A.5.24-27) for unauthorized access

Control Reference: ISO/IEC 27001:2022 Annex A Control A.8.31
Script Type: Assessment Workbook Generator
Version: 1.0
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
DOCUMENT_ID = "ISMS-IMP-A.8.31.2"
WORKBOOK_NAME = "Environment Access Control Assessment"
CONTROL_ID = "A.8.31"
CONTROL_NAME = "Separation of Development, Test and Production Environments"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

# Timestamps
GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")      # For display (Swiss format)
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")   # For filenames (sortable)

# Output filename
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

CHECK = "\u2705"
WARNING = "\u26a0\ufe0f"
XMARK = "\u274c"
DASH = "\u2014"


from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation


# ============================================================================
# WORKBOOK CREATION
# ============================================================================

def create_workbook() -> Workbook:
    """Create workbook with all required sheets."""
    wb = Workbook()

    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])

    sheets = [
        "Instructions & Legend",
        "User Environment Access Matrix",
        "Developer Production Access",
        "Production Credential Audit",
        "Cross Environment Access Log",
        "Break Glass Access Log",
        "MFA Enforcement",
        "Summary Dashboard",
        "Evidence Register",
        "Approval Sign-Off",
    ]
    for name in sheets:
        wb.create_sheet(title=name)

    return wb


def setup_styles():
    """Define cell styles."""
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
        "formula_cell": {
            "fill": PatternFill(start_color="E7E6E6", end_color="E7E6E6", fill_type="solid"),
            "alignment": Alignment(horizontal="center", vertical="center"),
            "border": border_thin,
        },
        "border": border_thin,
        "status_green": {
            "fill": PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
        },
        "status_red": {
            "fill": PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
        },
        "critical_violation": {
            "font": Font(name="Calibri", size=10, bold=True, color="FFFFFF"),
            "fill": PatternFill(start_color="C00000", end_color="C00000", fill_type="solid"),
        },
    }
    return styles


def apply_style(cell, style_dict):
    """Apply style to cell."""
    if "font" in style_dict:
        cell.font = Font(
            name=style_dict["font"].name,
            size=style_dict["font"].size,
            bold=style_dict["font"].bold,
            color=style_dict["font"].color if hasattr(style_dict["font"], "color") else None
        )
    if "fill" in style_dict:
        cell.fill = PatternFill(
            start_color=style_dict["fill"].start_color.rgb if hasattr(style_dict["fill"].start_color, "rgb") else style_dict["fill"].start_color,
            end_color=style_dict["fill"].end_color.rgb if hasattr(style_dict["fill"].end_color, "rgb") else style_dict["fill"].end_color,
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
# DATA VALIDATIONS
# ============================================================================

def create_base_validations(ws):
    """Create data validation objects."""
    validations = {
        "yes_no": DataValidation(
            type="list",
            formula1='"Yes,No"',
            allow_blank=False
        ),
        "yes_no_na": DataValidation(
            type="list",
            formula1='"✅ Yes,❌ No,➖ N/A"',
            allow_blank=False
        ),
        "access_level": DataValidation(
            type="list",
            formula1='"Full (CRUD),Read/Write,Read-only,No Access,Break-Glass Only"',
            allow_blank=False
        ),
        "compliance_status": DataValidation(
            type="list",
            formula1='"✅ Compliant,❌ Non-Compliant,⚠️ Partial,📋 Not Assessed"',
            allow_blank=False
        ),
        "user_role": DataValidation(
            type="list",
            formula1='"Developer,QA Engineer,DevOps Engineer,Operations Engineer,Security Analyst,Manager,Auditor,Other"',
            allow_blank=False
        ),
        "environment_type": DataValidation(
            type="list",
            formula1='"Development,Testing,Staging,Production"',
            allow_blank=False
        ),
        "severity": DataValidation(
            type="list",
            formula1='"🔴 Critical,🟠 High,🟡 Medium,🟢 Low"',
            allow_blank=False
        ),
    }
    
    return validations


def finalize_validations(ws, validations):
    """Add only data validations that have cells assigned to avoid Excel repair."""
    for dv in validations.values():
        if dv.sqref:
            ws.add_data_validation(dv)


# ============================================================================
# INSTRUCTIONS SHEET
# ============================================================================

def create_instructions_sheet(wb, styles):
    """Create Instructions & Legend sheet."""
    ws = wb["Instructions & Legend"]
    
    ws.merge_cells("A1:G1")
    cell = ws["A1"]
    cell.value = "ISMS-IMP-A.8.31.2  -  Environment Access Control Assessment\nISO/IEC 27001:2022 - Control A.8.31: Separation of Development, Test and Production Environments"
    cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    cell.fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 40

    row = 3
    info_items = [
        ("Document ID:", "ISMS-IMP-A.8.31.2"),
        ("Assessment Area:", "Environment Access Control & Restrictions"),
        ("Related Policy:", "ISMS-POL-A.8.31"),
        ("Version:", "1.0"),
        ("Assessment Date:", "[USER INPUT]"),
        ("Completed By:", "[USER INPUT]"),
        ("Organisation:", "[USER INPUT]"),
        ("Review Cycle:", "Quarterly"),
    ]
    
    for label, value in info_items:
        ws.cell(row=row, column=1, value=label).font = Font(bold=True)
        cell = ws.cell(row=row, column=2, value=value)
        if "USER INPUT" in value:
            apply_style(cell, styles["input_cell"])
        row += 1
    
    row += 1
    ws.merge_cells(f"A{row}:F{row}")
    cell = ws.cell(row=row, column=1, value="How to Use This Workbook")
    apply_style(cell, styles["subheader"])
    
    row += 1
    instructions = [
        "1. Complete User Environment Access Matrix - document who has access to which environment",
        "2. ⚠️ CRITICAL: Complete Developer Production Access - verify ZERO developers have production access",
        "3. Audit Production Credential Audit - verify all production credentials in PAM vault",
        "4. Review Cross Environment Access Log - check for unauthorised access attempts",
        "5. Document Break Glass Access Log - all emergency production access instances",
        "6. Verify MFA Enforcement - confirm MFA required for production",
        "7. Complete Summary Dashboard - calculate overall compliance",
        "8. Maintain Evidence Register for audit traceability",
        "9. Obtain final approval and sign-off",
    ]
    
    for instruction in instructions:
        ws.cell(row=row, column=1, value=instruction)
        row += 1
    
    row += 1
    ws.merge_cells(f"A{row}:F{row}")
    cell = ws.cell(row=row, column=1, value="CRITICAL REQUIREMENT")
    apply_style(cell, styles["critical_violation"])
    
    row += 1
    ws.merge_cells(f"A{row}:F{row}")
    ws.cell(row=row, column=1, value="🚨 ZERO developers shall have production access (except via documented break-glass)")
    
    row += 2
    ws.merge_cells(f"A{row}:F{row}")
    cell = ws.cell(row=row, column=1, value="Status Legend")
    apply_style(cell, styles["subheader"])
    
    row += 1
    legend = [
        ("✅", "Compliant / Authorised", "Green"),
        ("❌", "Non-Compliant / Unauthorised", "Red"),
        ("⚠️", "Partial / Warning", "Yellow"),
        ("🔴", "Critical Violation", "Dark Red"),
        ("➖", "N/A / Not Applicable", "Gray"),
    ]
    
    for col_idx, label in [(1, "Symbol"), (2, "Status"), (3, "Color")]:
        cell = ws.cell(row=row, column=col_idx, value=label)
        cell.font = Font(bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
    row += 1
    
    for symbol, status, color in legend:
        ws.cell(row=row, column=1, value=symbol)
        ws.cell(row=row, column=2, value=status)
        ws.cell(row=row, column=3, value=color)
        row += 1
    
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 45
    ws.column_dimensions["C"].width = 70
    ws.freeze_panes = "A4"


# ============================================================================
# USER ENVIRONMENT ACCESS MATRIX
# ============================================================================

def create_user_access_matrix_sheet(wb, styles):
    """Create User-Environment Access Matrix."""
    ws = wb["User Environment Access Matrix"]
    
    ws.merge_cells("A1:H1")
    cell = ws["A1"]
    cell.value = "USER → ENVIRONMENT ACCESS MATRIX"
    apply_style(cell, styles["header"])
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:H2")
    cell = ws["A2"]
    cell.value = "Document access permissions for each user per environment"
    apply_style(cell, styles["subheader"])
    
    row = 4
    headers = [
        ("A", "User ID / Email", 30),
        ("B", "Role", 25),
        ("C", "Development Access", 25),
        ("D", "Testing Access", 25),
        ("E", "Staging Access", 25),
        ("F", "Production Access", 25),
        ("G", "Compliance Status", 20),
        ("H", "Notes", 40),
    ]
    
    for col, header, width in headers:
        cell = ws[f"{col}{row}"]
        cell.value = header
        apply_style(cell, styles["column_header"])
        ws.column_dimensions[col].width = width
    
    validations = create_base_validations(ws)
    validations["user_role"].add("B5:B100")
    validations["access_level"].add("C5:F100")
    validations["compliance_status"].add("G5:G100")

    row = 5
    sample_data = [
        ("dev1@example.ch", "Developer", "Full (CRUD)", "Read/Write", "Read-only", "❌ No Access", "✅ Compliant", "Proper access separation"),
        ("dev2@example.ch", "Developer", "Full (CRUD)", "Read/Write", "Read-only", "❌ No Access", "✅ Compliant", "No prod access (expected)"),
        ("qa1@example.ch", "QA Engineer", "Read-only", "Full (CRUD)", "Read/Write", "❌ No Access", "✅ Compliant", "Testing environment focus"),
        ("ops1@example.ch", "Operations Engineer", "Read-only", "Read-only", "Full (CRUD)", "Full (CRUD)", "✅ Compliant", "Prod access via PAM vault"),
        ("ops2@example.ch", "Operations Engineer", "❌ No Access", "❌ No Access", "Full (CRUD)", "Full (CRUD)", "✅ Compliant", "Production-focused role"),
    ]

    for data in sample_data:
        for idx, value in enumerate(data):
            cell = ws.cell(row=row, column=idx+1, value=value)
            apply_style(cell, styles["input_cell"])
        row += 1

    finalize_validations(ws, validations)


# ============================================================================
# DEVELOPER PRODUCTION ACCESS (CRITICAL CHECK)
# ============================================================================

def create_developer_prod_access_sheet(wb, styles):
    """Create Developer Production Access critical check sheet."""
    ws = wb["Developer Production Access"]
    
    ws.merge_cells("A1:G1")
    cell = ws["A1"]
    cell.value = "🚨 DEVELOPER PRODUCTION ACCESS CHECK (CRITICAL)"
    cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    cell.fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35
    
    ws.merge_cells("A2:G2")
    cell = ws["A2"]
    cell.value = "TARGET: ZERO developers with production access | Any violations = CRITICAL FINDING"
    apply_style(cell, styles["subheader"])
    ws.row_dimensions[2].height = 30
    
    row = 4
    headers = [
        ("A", "Developer ID", 30),
        ("B", "Production Account/Sub", 30),
        ("C", "Production Access?", 20),
        ("D", "Access Type", 25),
        ("E", "Justification", 40),
        ("F", "Violation Severity", 20),
        ("G", "Remediation Action", 40),
    ]
    
    for col, header, width in headers:
        cell = ws[f"{col}{row}"]
        cell.value = header
        apply_style(cell, styles["column_header"])
        ws.column_dimensions[col].width = width
    
    validations = create_base_validations(ws)
    validations["yes_no"].add("C5:C100")
    validations["severity"].add("F5:F100")
    finalize_validations(ws, validations)

    row = 5
    ws.cell(row=row, column=1, value="dev1@example.ch")
    ws.cell(row=row, column=2, value="AWS Prod Account: 444444444444")
    ws.cell(row=row, column=3, value="No")
    ws.cell(row=row, column=4, value="N/A")
    ws.cell(row=row, column=5, value="No production access (expected)")
    ws.cell(row=row, column=6, value="🟢 Low")
    ws.cell(row=row, column=7, value="N/A - Compliant")
    
    for col in range(1, 8):
        apply_style(ws.cell(row=row, column=col), styles["input_cell"])
    
    row += 2
    ws.merge_cells(f"A{row}:G{row}")
    cell = ws.cell(row=row, column=1, value="✅ If ALL developers show 'No' for Production Access → COMPLIANT")
    apply_style(cell, styles["status_green"])
    
    row += 1
    ws.merge_cells(f"A{row}:G{row}")
    cell = ws.cell(row=row, column=1, value="🔴 If ANY developer shows 'Yes' for Production Access → CRITICAL VIOLATION")
    apply_style(cell, styles["critical_violation"])


# ============================================================================
# PRODUCTION CREDENTIAL AUDIT
# ============================================================================

def create_production_credential_audit_sheet(wb, styles):
    """Create Production Credential Audit sheet."""
    ws = wb["Production Credential Audit"]
    
    ws.merge_cells("A1:H1")
    cell = ws["A1"]
    cell.value = "PRODUCTION CREDENTIAL AUDIT"
    apply_style(cell, styles["header"])
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:H2")
    cell = ws["A2"]
    cell.value = "Verify all production credentials stored in PAM vault and rotated regularly"
    apply_style(cell, styles["subheader"])
    
    row = 4
    headers = [
        ("A", "Credential Type", 30),
        ("B", "System/Service", 30),
        ("C", "Stored in PAM Vault?", 20),
        ("D", "Vault Location", 35),
        ("E", "Last Rotated", 20),
        ("F", "Rotation Schedule", 20),
        ("G", "Compliance", 20),
        ("H", "Notes", 40),
    ]
    
    for col, header, width in headers:
        cell = ws[f"{col}{row}"]
        cell.value = header
        apply_style(cell, styles["column_header"])
        ws.column_dimensions[col].width = width
    
    validations = create_base_validations(ws)
    validations["yes_no"].add("C5:C100")
    validations["compliance_status"].add("G5:G100")
    finalize_validations(ws, validations)

    row = 5
    sample_data = [
        ("Database Admin Password", "prod-db.example.com", "Yes", "CyberArk/Prod/DB/AdminPwd", "2026-01-01", "90 days", "✅ Compliant", "Auto-rotation enabled"),
        ("AWS Root Account", "AWS Prod: 444444444444", "Yes", "CyberArk/Prod/AWS/Root", "2025-12-15", "Never (not used)", "✅ Compliant", "MFA enforced, never used"),
        ("SSH Private Key", "prod-app-servers", "Yes", "CyberArk/Prod/SSH/Keys", "2025-11-20", "180 days", "✅ Compliant", "Key-based auth"),
        ("API Key (Stripe)", "Payment gateway", "Yes", "AWS Secrets Manager", "2026-01-05", "90 days", "✅ Compliant", "Live API key"),
    ]
    
    for data in sample_data:
        for idx, value in enumerate(data):
            cell = ws.cell(row=row, column=idx+1, value=value)
            apply_style(cell, styles["input_cell"])
        row += 1


# ============================================================================
# CROSS ENVIRONMENT ACCESS LOG
# ============================================================================

def create_cross_environment_access_sheet(wb, styles):
    """Create Cross-Environment Access Log sheet."""
    ws = wb["Cross Environment Access Log"]
    
    ws.merge_cells("A1:H1")
    cell = ws["A1"]
    cell.value = "CROSS-ENVIRONMENT ACCESS ATTEMPTS LOG"
    apply_style(cell, styles["header"])
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:H2")
    cell = ws["A2"]
    cell.value = "Log unauthorised cross-environment access attempts (should be blocked)"
    apply_style(cell, styles["subheader"])
    
    row = 4
    headers = [
        ("A", "Date/Time", 20),
        ("B", "User ID", 30),
        ("C", "Source Environment", 20),
        ("D", "Target Environment", 20),
        ("E", "Attempted Action", 30),
        ("F", "Result", 20),
        ("G", "Alert Generated?", 20),
        ("H", "Investigation Notes", 40),
    ]
    
    for col, header, width in headers:
        cell = ws[f"{col}{row}"]
        cell.value = header
        apply_style(cell, styles["column_header"])
        ws.column_dimensions[col].width = width
    
    validations = create_base_validations(ws)
    validations["environment_type"].add("C5:D100")
    validations["yes_no"].add("G5:G100")
    finalize_validations(ws, validations)

    row = 5
    sample_data = [
        ("2026-01-10 14:23:00", "dev1@example.ch", "Development", "Production", "SSH to prod-app01", "❌ BLOCKED", "Yes", "Firewall rule blocked access (expected)"),
        ("2026-01-09 09:15:00", "dev2@example.ch", "Development", "Production", "AWS CLI describe-instances", "❌ DENIED", "Yes", "IAM policy denied (expected)"),
    ]
    
    for data in sample_data:
        for idx, value in enumerate(data):
            cell = ws.cell(row=row, column=idx+1, value=value)
            apply_style(cell, styles["input_cell"])
        row += 1


# ============================================================================
# BREAK GLASS ACCESS LOG
# ============================================================================

def create_breakglass_access_sheet(wb, styles):
    """Create Break-Glass Access Log sheet."""
    ws = wb["Break Glass Access Log"]
    
    ws.merge_cells("A1:J1")
    cell = ws["A1"]
    cell.value = "BREAK-GLASS EMERGENCY ACCESS LOG"
    apply_style(cell, styles["header"])
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:J2")
    cell = ws["A2"]
    cell.value = "Document all instances of emergency developer access to production"
    apply_style(cell, styles["subheader"])
    
    row = 4
    headers = [
        ("A", "Incident ID", 15),
        ("B", "Date/Time Activated", 20),
        ("C", "Developer ID", 30),
        ("D", "Approved By", 25),
        ("E", "Reason/Justification", 40),
        ("F", "Duration (hours)", 15),
        ("G", "Date/Time Revoked", 20),
        ("H", "Post-Incident Review", 30),
        ("I", "Compliance", 20),
        ("J", "Notes", 40),
    ]
    
    for col, header, width in headers:
        cell = ws[f"{col}{row}"]
        cell.value = header
        apply_style(cell, styles["column_header"])
        ws.column_dimensions[col].width = width
    
    validations = create_base_validations(ws)
    validations["compliance_status"].add("I5:I100")
    finalize_validations(ws, validations)

    row = 5
    sample_data = [
        ("INC-2026-001", "2026-01-05 02:30", "senior-dev@example.ch", "ops-manager@example.ch", "Critical production outage - database corruption", "4", "2026-01-05 06:30", "Completed 2026-01-06", "✅ Compliant", "Proper procedure followed"),
    ]
    
    for data in sample_data:
        for idx, value in enumerate(data):
            cell = ws.cell(row=row, column=idx+1, value=value)
            apply_style(cell, styles["input_cell"])
        row += 1


# ============================================================================
# MFA ENFORCEMENT
# ============================================================================

def create_mfa_enforcement_sheet(wb, styles):
    """Create MFA Enforcement sheet."""
    ws = wb["MFA Enforcement"]
    
    ws.merge_cells("A1:G1")
    cell = ws["A1"]
    cell.value = "MFA ENFORCEMENT VERIFICATION"
    apply_style(cell, styles["header"])
    ws.row_dimensions[1].height = 30
    
    ws.merge_cells("A2:G2")
    cell = ws["A2"]
    cell.value = "Verify MFA required for production access (all users)"
    apply_style(cell, styles["subheader"])
    
    row = 4
    headers = [
        ("A", "User ID", 30),
        ("B", "Production Access?", 20),
        ("C", "MFA Enabled?", 20),
        ("D", "MFA Type", 25),
        ("E", "Last MFA Check", 20),
        ("F", "Compliance", 20),
        ("G", "Evidence", 40),
    ]
    
    for col, header, width in headers:
        cell = ws[f"{col}{row}"]
        cell.value = header
        apply_style(cell, styles["column_header"])
        ws.column_dimensions[col].width = width
    
    validations = create_base_validations(ws)
    validations["yes_no"].add("B5:C100")
    validations["compliance_status"].add("F5:F100")
    finalize_validations(ws, validations)

    row = 5
    sample_data = [
        ("ops1@example.ch", "Yes", "Yes", "Hardware Token (YubiKey)", "2026-01-11", "✅ Compliant", "IAM user MFA device ARN: ...mfa/ops1"),
        ("ops2@example.ch", "Yes", "Yes", "Virtual MFA (Google Authenticator)", "2026-01-11", "✅ Compliant", "IAM user MFA device ARN: ...mfa/ops2"),
    ]
    
    for data in sample_data:
        for idx, value in enumerate(data):
            cell = ws.cell(row=row, column=idx+1, value=value)
            apply_style(cell, styles["input_cell"])
        row += 1


# ============================================================================
# SUMMARY DASHBOARD
# ============================================================================

def create_summary_dashboard_sheet(ws, styles):
    """Create standard Summary Dashboard sheet."""
    thin = Side(style="thin")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    # Header
    ws.merge_cells("A1:G1")
    cell = ws.cell(row=1, column=1, value="ENVIRONMENT ACCESS CONTROL ASSESSMENT - COMPLIANCE SUMMARY")
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
        "User Environment Access Matrix",
        "Developer Production Access",
        "Production Credential Audit",
        "Cross Environment Access Log",
        "Break Glass Access Log",
        "MFA Enforcement",
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

    metrics = ["Last Assessment Date", "Next Review Due", "Assessment Owner", "Overall Risk Rating"]
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


# ============================================================================
# EVIDENCE REGISTER
# ============================================================================

def create_evidence_register(ws, styles):
    """Create standard Evidence Register (8 columns, 100 rows)."""
    thin = Side(style="thin")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    ws.merge_cells("A1:H1")
    cell = ws.cell(row=1, column=1, value="EVIDENCE REGISTER")
    cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="003366")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    ws.merge_cells("A2:H2")
    cell = ws.cell(row=2, column=1, value="Record all evidence collected during the assessment. Each row represents one piece of evidence.")
    cell.font = Font(name="Calibri", size=10, italic=True)
    cell.alignment = Alignment(horizontal="left", vertical="center")

    headers = ["Evidence ID", "Assessment Area", "Evidence Type", "Description", "Location / Path", "Date Collected", "Collected By", "Verification Status"]
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=4, column=col, value=header)
        cell.font = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="4472C4")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border
    ws.row_dimensions[4].height = 30

    for i in range(1, 101):
        row = i + 4
        cell = ws.cell(row=row, column=1, value=f"EV-{i:03d}")
        cell.font = Font(name="Calibri", size=10, color="808080")
        cell.border = border
        for col in range(2, 9):
            cell = ws.cell(row=row, column=col)
            cell.fill = PatternFill("solid", fgColor="FFFFCC")
            cell.border = border

    ev_types = DataValidation(type="list", formula1='"Configuration file,Screenshot,Log extract,Policy document,Training record,Audit report,Risk assessment,Interview notes,Test results,Other"', allow_blank=True)
    ev_types.prompt = "Select evidence type"
    ws.add_data_validation(ev_types)
    ev_types.add("C5:C104")

    verify_status = DataValidation(type="list", formula1='"Verified,Pending Verification,Insufficient,Not Reviewed"', allow_blank=True)
    verify_status.prompt = "Select verification status"
    ws.add_data_validation(verify_status)
    verify_status.add("H5:H104")

    widths = {"A": 15, "B": 25, "C": 22, "D": 40, "E": 45, "F": 16, "G": 20, "H": 22}
    for col, width in widths.items():
        ws.column_dimensions[col].width = width

    ws.freeze_panes = "A5"


# ============================================================================
# APPROVAL SIGN-OFF
# ============================================================================

def create_approval_signoff_sheet(ws, styles):
    """Create standard Approval Sign-Off sheet."""
    thin = Side(style="thin")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    ws.merge_cells("A1:E1")
    cell = ws.cell(row=1, column=1, value="ASSESSMENT APPROVAL AND SIGN-OFF")
    cell.font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="003366")
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 35

    row = 3
    ws.merge_cells(f"A{row}:E{row}")
    cell = ws.cell(row=row, column=1, value="ASSESSMENT SUMMARY")
    cell.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="4472C4")
    cell.alignment = Alignment(horizontal="left", vertical="center")

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

    status_dv = DataValidation(type="list", formula1='"Draft,Final,Requires remediation,Re-assessment required"', allow_blank=True)
    ws.add_data_validation(status_dv)
    status_dv.add(f"B{row + 4}")

    row = row + 1 + len(summary_fields) + 1

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

    row = _approver_section(row, "COMPLETED BY \u2014 Assessment Lead", "4472C4")
    row = _approver_section(row, "REVIEWED BY \u2014 Security Manager", "4472C4")
    row = _approver_section(row, "APPROVED BY \u2014 CISO", "003366")

    ws.cell(row=row, column=1, value="FINAL DECISION:").font = Font(name="Calibri", size=11, bold=True)
    ws.merge_cells(f"B{row}:E{row}")
    cell = ws.cell(row=row, column=2)
    cell.fill = PatternFill("solid", fgColor="FFFFCC")
    cell.border = border
    final_dv = DataValidation(type="list", formula1='"Approved,Approved with Conditions,Rejected,Deferred"', allow_blank=True)
    ws.add_data_validation(final_dv)
    final_dv.add(f"B{row}")

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

    ws.column_dimensions["A"].width = 32
    ws.column_dimensions["B"].width = 25
    ws.column_dimensions["C"].width = 20
    ws.column_dimensions["D"].width = 20
    ws.column_dimensions["E"].width = 20
    ws.freeze_panes = "A3"


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Generate the assessment workbook."""
    logger.info("=" * 80)
    logger.info("ISMS-IMP-A.8.31.2 - Environment Access Control Assessment Generator")
    logger.info("ISO/IEC 27001:2022 Control A.8.31")
    logger.info("=" * 80)
    
    logger.info("\nCreating workbook structure...")
    wb = create_workbook()
    styles = setup_styles()
    
    logger.info("Generating Instructions & Legend sheet...")
    create_instructions_sheet(wb, styles)
    
    logger.info("Generating User-Environment Access Matrix sheet...")
    create_user_access_matrix_sheet(wb, styles)
    
    logger.info("Generating Developer Production Access sheet (CRITICAL)...")
    create_developer_prod_access_sheet(wb, styles)
    
    logger.info("Generating Production Credential Audit sheet...")
    create_production_credential_audit_sheet(wb, styles)
    
    logger.info("Generating Cross-Environment Access Log sheet...")
    create_cross_environment_access_sheet(wb, styles)
    
    logger.info("Generating Break-Glass Access Log sheet...")
    create_breakglass_access_sheet(wb, styles)
    
    logger.info("Generating MFA Enforcement sheet...")
    create_mfa_enforcement_sheet(wb, styles)
    
    logger.info("Generating Summary Dashboard sheet...")
    create_summary_dashboard_sheet(wb["Summary Dashboard"], styles)

    logger.info("Generating Evidence Register sheet...")
    create_evidence_register(wb["Evidence Register"], styles)

    logger.info("Generating Approval Sign-Off sheet...")
    create_approval_signoff_sheet(wb["Approval Sign-Off"], styles)

    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"ISMS-IMP-A.8.31.2_Environment_Access_Control_Assessment_{timestamp}.xlsx"

    logger.info(f"\nSaving workbook: {filename}")
    wb.save(filename)

    logger.info("=" * 80)
    logger.info(f"{CHECK} SUCCESS: Generated {filename}")
    logger.info("=" * 80)


if __name__ == "__main__":
    main()

# =============================================================================
# QA_VERIFIED: 2026-02-10
# QA_STATUS: PASSED - STANDARDISATION COMPLETE
# QA_TOOL: Claude Code Standardization
# CHANGES: tab names, summary dashboard, evidence register, approval sign-off,
#          unicode symbols, related policy, instructions freeze, QA footer
# =============================================================================
