#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
================================================================================
A.5.17.3 Password System Assessment Generator
================================================================================

Generates Excel workbook for assessing password and authentication management
systems including storage security, complexity enforcement, and integration.

Sheets:
    1. Instructions - Completion guidance
    2. System_Inventory - Authentication systems inventory
    3. Security_Assessment - System-by-system security evaluation
    4. Storage_Assessment - Password storage security review
    5. Integration_Assessment - SSO/Federation assessment
    6. Gap_Analysis - Identified gaps and remediation
    7. Evidence_Register - Supporting documentation
    8. Approval_SignOff - Assessment approval

Usage:
    python3 generate_a517_3_password_system_assessment.py
================================================================================
"""

import logging
import sys
from datetime import datetime
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.worksheet.datavalidation import DataValidation
except ImportError:
    print("ERROR: openpyxl required. Install with: pip install openpyxl")
    sys.exit(1)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

DOCUMENT_ID = "ISMS-IMP-A.5.17.3"
WORKBOOK_NAME = "Password System Assessment"
CONTROL_ID = "A.5.17"
CONTROL_NAME = "Authentication Information"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

HEADER_FILL = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
SUBHEADER_FILL = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
INPUT_FILL = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
PASS_FILL = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
FAIL_FILL = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
PARTIAL_FILL = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")

HEADER_FONT = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
SUBHEADER_FONT = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
BOLD_FONT = Font(name="Calibri", size=11, bold=True)
NORMAL_FONT = Font(name="Calibri", size=11)

THIN_BORDER = Border(
    left=Side(style="thin"), right=Side(style="thin"),
    top=Side(style="thin"), bottom=Side(style="thin")
)
CENTER_ALIGN = Alignment(horizontal="center", vertical="center", wrap_text=True)
LEFT_ALIGN = Alignment(horizontal="left", vertical="center", wrap_text=True)
TOP_LEFT_ALIGN = Alignment(horizontal="left", vertical="top", wrap_text=True)


def set_column_widths(ws, widths: dict):
    for col, width in widths.items():
        ws.column_dimensions[col].width = width


def create_header_row(ws, row: int, headers: list):
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col, value=header)
        cell.font = SUBHEADER_FONT
        cell.fill = SUBHEADER_FILL
        cell.alignment = CENTER_ALIGN
        cell.border = THIN_BORDER


def add_data_validation(ws, cell_range: str, formula: str):
    dv = DataValidation(type="list", formula1=formula, showDropDown=False, allowBlank=True)
    ws.add_data_validation(dv)
    dv.add(cell_range)


def create_instructions_sheet(wb: Workbook):
    ws = wb.active
    ws.title = "Instructions"

    ws.merge_cells("A1:H1")
    ws["A1"].value = f"{DOCUMENT_ID} - {WORKBOOK_NAME}"
    ws["A1"].font = HEADER_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = CENTER_ALIGN

    metadata = [
        ("Document ID:", DOCUMENT_ID),
        ("Control Reference:", CONTROL_REF),
        ("Generated Date:", GENERATED_DATE),
        ("Version:", "1.0"),
    ]

    row = 3
    for label, value in metadata:
        ws.cell(row=row, column=1, value=label).font = BOLD_FONT
        ws.cell(row=row, column=2, value=value).font = NORMAL_FONT
        row += 1

    row += 1
    ws.cell(row=row, column=1, value="PURPOSE").font = BOLD_FONT
    row += 1
    ws.merge_cells(f"A{row}:H{row}")
    ws.cell(row=row, column=1).value = (
        "This workbook provides a structured assessment of password and authentication management systems. "
        "It evaluates password storage security, complexity enforcement, SSO integration, and identifies gaps "
        "requiring remediation per ISO 27001:2022 A.5.17."
    )
    ws.cell(row=row, column=1).font = NORMAL_FONT
    ws.cell(row=row, column=1).alignment = TOP_LEFT_ALIGN
    ws.row_dimensions[row].height = 50

    row += 2
    ws.cell(row=row, column=1, value="SHEET DESCRIPTIONS").font = BOLD_FONT
    row += 1

    sheets = [
        ("System_Inventory", "Inventory of all authentication systems"),
        ("Security_Assessment", "System-by-system security control evaluation"),
        ("Storage_Assessment", "Password storage security review"),
        ("Integration_Assessment", "SSO and federation integration assessment"),
        ("Gap_Analysis", "Identified gaps and remediation tracking"),
        ("Evidence_Register", "Supporting documentation"),
        ("Approval_SignOff", "Assessment approval"),
    ]

    for sheet_name, description in sheets:
        ws.cell(row=row, column=1, value=sheet_name).font = BOLD_FONT
        ws.cell(row=row, column=2, value=description).font = NORMAL_FONT
        row += 1

    set_column_widths(ws, {"A": 25, "B": 50, "C": 20, "D": 20, "E": 20, "F": 20, "G": 20, "H": 20})
    ws.freeze_panes = "A3"
    logger.info("Created Instructions sheet")


def create_system_inventory_sheet(wb: Workbook):
    ws = wb.create_sheet("System_Inventory")

    ws.merge_cells("A1:J1")
    ws["A1"].value = "Authentication System Inventory"
    ws["A1"].font = HEADER_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = CENTER_ALIGN

    headers = ["System Name", "System Type", "Vendor", "Version", "User Count", "Auth Method", "SSO Integrated", "MFA Enabled", "Owner", "Criticality"]
    create_header_row(ws, 3, headers)

    systems = [
        ("Active Directory", "Identity Provider", "Microsoft", "", "", "Password + Kerberos", "", "", "", ""),
        ("Azure AD / Entra ID", "Cloud Identity", "Microsoft", "", "", "Password + MFA", "", "", "", ""),
        ("Okta", "Identity Provider", "Okta", "", "", "SAML/OIDC + MFA", "", "", "", ""),
        ("Microsoft 365", "Cloud Application", "Microsoft", "", "", "Microsoft Entra ID (formerly Azure AD) SSO", "", "", "", ""),
        ("Salesforce", "Cloud Application", "Salesforce", "", "", "SAML SSO", "", "", "", ""),
        ("AWS Console", "Cloud Infrastructure", "Amazon", "", "", "IAM + MFA", "", "", "", ""),
        ("VPN Gateway", "Network Access", "", "", "", "RADIUS + MFA", "", "", "", ""),
        ("HRIS System", "Business Application", "", "", "", "Local + SSO", "", "", "", ""),
        ("Source Control (GitHub)", "Development", "GitHub/Microsoft", "", "", "SSO + MFA", "", "", "", ""),
        ("Database (Production)", "Data Store", "", "", "", "Local accounts", "", "", "", ""),
    ]

    row = 4
    for system in systems:
        for col, value in enumerate(system, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col >= 4:
                cell.fill = INPUT_FILL
        row += 1

    for i in range(10):
        for col in range(1, 11):
            cell = ws.cell(row=row, column=col, value="")
            cell.border = THIN_BORDER
            cell.fill = INPUT_FILL
        row += 1

    add_data_validation(ws, f"B4:B{row-1}", '"Identity Provider,Cloud Identity,Cloud Application,Cloud Infrastructure,Network Access,Business Application,Development,Data Store,Other"')
    add_data_validation(ws, f"G4:G{row-1}", '"Yes,No,Partial,N/A"')
    add_data_validation(ws, f"H4:H{row-1}", '"Yes,No,Partial,N/A"')
    add_data_validation(ws, f"J4:J{row-1}", '"Critical,High,Medium,Low"')

    set_column_widths(ws, {"A": 25, "B": 18, "C": 15, "D": 12, "E": 12, "F": 22, "G": 14, "H": 14, "I": 18, "J": 12})
    ws.freeze_panes = "A4"
    logger.info("Created System_Inventory sheet")


def create_security_assessment_sheet(wb: Workbook):
    ws = wb.create_sheet("Security_Assessment")

    ws.merge_cells("A1:I1")
    ws["A1"].value = "Authentication System Security Assessment"
    ws["A1"].font = HEADER_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = CENTER_ALIGN

    headers = ["System Name", "Control Area", "Requirement", "Expected State", "Actual State", "Status", "Gap Description", "Priority", "Notes"]
    create_header_row(ws, 3, headers)

    assessments = [
        ("Active Directory", "Password Policy", "Min 12 characters enforced", "GPO setting enabled", "", "", "", "", ""),
        ("Active Directory", "Password Policy", "Complexity requirements", "Uppercase, lowercase, number, special", "", "", "", "", ""),
        ("Active Directory", "Password Policy", "Password history (12+)", "12 passwords remembered", "", "", "", "", ""),
        ("Active Directory", "Account Lockout", "Lockout threshold", "5 attempts", "", "", "", "", ""),
        ("Active Directory", "Account Lockout", "Lockout duration", "15 minutes", "", "", "", "", ""),
        ("Microsoft Entra ID (formerly Azure AD)", "MFA Policy", "MFA enforced for all users", "Conditional Access policy", "", "", "", "", ""),
        ("Microsoft Entra ID (formerly Azure AD)", "MFA Policy", "Approved MFA methods", "Authenticator, FIDO2", "", "", "", "", ""),
        ("Microsoft Entra ID (formerly Azure AD)", "Risk Detection", "Sign-in risk policy", "Block high risk", "", "", "", "", ""),
        ("Microsoft Entra ID (formerly Azure AD)", "Password Protection", "Banned password list", "Custom + global list", "", "", "", "", ""),
        ("VPN Gateway", "Authentication", "MFA required", "RADIUS + TOTP", "", "", "", "", ""),
        ("VPN Gateway", "Logging", "Authentication logging", "All attempts logged", "", "", "", "", ""),
        ("Database", "Authentication", "Strong passwords for service accounts", "24+ characters", "", "", "", "", ""),
        ("Database", "Encryption", "Passwords encrypted in connection strings", "Secrets manager", "", "", "", "", ""),
    ]

    row = 4
    for assessment in assessments:
        for col, value in enumerate(assessment, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col in [5, 6, 7, 8, 9]:
                cell.fill = INPUT_FILL
        row += 1

    for i in range(10):
        for col in range(1, 10):
            cell = ws.cell(row=row, column=col, value="")
            cell.border = THIN_BORDER
            cell.fill = INPUT_FILL
        row += 1

    add_data_validation(ws, f"F4:F{row-1}", '"Compliant,Partial,Non-Compliant,N/A"')
    add_data_validation(ws, f"H4:H{row-1}", '"Critical,High,Medium,Low"')

    set_column_widths(ws, {"A": 20, "B": 18, "C": 28, "D": 28, "E": 25, "F": 14, "G": 28, "H": 10, "I": 22})
    ws.freeze_panes = "A4"
    logger.info("Created Security_Assessment sheet")


def create_storage_assessment_sheet(wb: Workbook):
    ws = wb.create_sheet("Storage_Assessment")

    ws.merge_cells("A1:H1")
    ws["A1"].value = "Password Storage Security Assessment"
    ws["A1"].font = HEADER_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = CENTER_ALIGN

    headers = ["System/Application", "Storage Mechanism", "Hashing Algorithm", "Salting", "Key Protection", "Encryption at Rest", "Status", "Notes"]
    create_header_row(ws, 3, headers)

    storage = [
        ("Active Directory", "NTDS.dit database", "NT Hash (MD4) + Kerberos", "No (legacy)", "DPAPI/TPM", "BitLocker", "", ""),
        ("Microsoft Entra ID (formerly Azure AD)", "Microsoft cloud", "PBKDF2-SHA256", "Yes (per-user)", "HSM-backed", "AES-256", "", ""),
        ("Web Application (Custom)", "SQL Database", "", "", "", "", "", ""),
        ("Legacy Application", "Local files", "", "", "", "", "", ""),
        ("Service Account Vault", "HashiCorp Vault", "N/A (encrypted storage)", "N/A", "Seal key/HSM", "AES-256-GCM", "", ""),
        ("Password Manager (Corp)", "Vendor cloud", "", "", "", "", "", ""),
        ("API Keys Store", "", "", "", "", "", "", ""),
        ("Certificate Store", "", "", "", "", "", "", ""),
    ]

    row = 4
    for item in storage:
        for col, value in enumerate(item, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col >= 3:
                cell.fill = INPUT_FILL
        row += 1

    for i in range(8):
        for col in range(1, 9):
            cell = ws.cell(row=row, column=col, value="")
            cell.border = THIN_BORDER
            cell.fill = INPUT_FILL
        row += 1

    add_data_validation(ws, f"G4:G{row-1}", '"Compliant,Partial,Non-Compliant,N/A"')
    add_data_validation(ws, f"C4:C{row-1}", '"bcrypt,Argon2id,PBKDF2-SHA256,scrypt,SHA-256 (not recommended),MD5 (non-compliant),Plaintext (critical),Unknown,N/A"')

    set_column_widths(ws, {"A": 25, "B": 22, "C": 20, "D": 15, "E": 18, "F": 18, "G": 14, "H": 28})
    ws.freeze_panes = "A4"
    logger.info("Created Storage_Assessment sheet")


def create_integration_assessment_sheet(wb: Workbook):
    ws = wb.create_sheet("Integration_Assessment")

    ws.merge_cells("A1:I1")
    ws["A1"].value = "SSO and Federation Integration Assessment"
    ws["A1"].font = HEADER_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = CENTER_ALIGN

    headers = ["Application", "SSO Protocol", "Identity Provider", "MFA Pass-through", "Session Timeout", "Token Encryption", "Provisioning", "Status", "Notes"]
    create_header_row(ws, 3, headers)

    integrations = [
        ("Microsoft 365", "OIDC/WS-Fed", "Microsoft Entra ID (formerly Azure AD)", "Yes", "Configurable", "Yes", "Automated", "", ""),
        ("Salesforce", "SAML 2.0", "Microsoft Entra ID (formerly Azure AD)", "Yes", "2 hours", "Yes", "SCIM", "", ""),
        ("ServiceNow", "SAML 2.0", "Microsoft Entra ID (formerly Azure AD)", "Yes", "8 hours", "Yes", "SCIM", "", ""),
        ("Workday", "SAML 2.0", "Microsoft Entra ID (formerly Azure AD)", "Yes", "Configurable", "Yes", "API", "", ""),
        ("AWS Console", "SAML 2.0", "Microsoft Entra ID (formerly Azure AD)", "Yes", "1 hour", "Yes", "Manual", "", ""),
        ("GitHub Enterprise", "SAML 2.0", "Microsoft Entra ID (formerly Azure AD)", "Yes", "8 hours", "Yes", "SCIM", "", ""),
        ("Zoom", "SAML 2.0", "Microsoft Entra ID (formerly Azure AD)", "Yes", "24 hours", "Yes", "SCIM", "", ""),
        ("Slack", "SAML 2.0", "Microsoft Entra ID (formerly Azure AD)", "Yes", "Configurable", "Yes", "SCIM", "", ""),
    ]

    row = 4
    for integration in integrations:
        for col, value in enumerate(integration, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col in [4, 5, 8, 9]:
                cell.fill = INPUT_FILL
        row += 1

    for i in range(10):
        for col in range(1, 10):
            cell = ws.cell(row=row, column=col, value="")
            cell.border = THIN_BORDER
            cell.fill = INPUT_FILL
        row += 1

    add_data_validation(ws, f"B4:B{row-1}", '"SAML 2.0,OIDC,WS-Federation,OAuth 2.0,Local Auth,None"')
    add_data_validation(ws, f"D4:D{row-1}", '"Yes,No,Partial,N/A"')
    add_data_validation(ws, f"G4:G{row-1}", '"Automated,SCIM,API,Manual,None"')
    add_data_validation(ws, f"H4:H{row-1}", '"Compliant,Partial,Non-Compliant,N/A"')

    set_column_widths(ws, {"A": 22, "B": 14, "C": 16, "D": 16, "E": 16, "F": 16, "G": 14, "H": 14, "I": 28})
    ws.freeze_panes = "A4"
    logger.info("Created Integration_Assessment sheet")


def create_gap_analysis_sheet(wb: Workbook):
    ws = wb.create_sheet("Gap_Analysis")

    ws.merge_cells("A1:I1")
    ws["A1"].value = "Gap Analysis and Remediation Tracking"
    ws["A1"].font = HEADER_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = CENTER_ALIGN

    headers = ["Gap ID", "System/Area", "Gap Description", "Risk Level", "Remediation Plan", "Owner", "Target Date", "Status", "Notes"]
    create_header_row(ws, 3, headers)

    row = 4
    for i in range(15):
        for col in range(1, 10):
            cell = ws.cell(row=row, column=col, value="")
            cell.border = THIN_BORDER
            cell.fill = INPUT_FILL
        row += 1

    add_data_validation(ws, f"D4:D{row-1}", '"Critical,High,Medium,Low"')
    add_data_validation(ws, f"H4:H{row-1}", '"Open,In Progress,Remediated,Verified,Risk Accepted"')

    set_column_widths(ws, {"A": 12, "B": 20, "C": 35, "D": 12, "E": 35, "F": 18, "G": 14, "H": 14, "I": 25})
    ws.freeze_panes = "A4"
    logger.info("Created Gap_Analysis sheet")


def create_evidence_register_sheet(wb: Workbook):
    ws = wb.create_sheet("Evidence_Register")

    ws.merge_cells("A1:H1")
    ws["A1"].value = "Evidence Register - System Assessment"
    ws["A1"].font = HEADER_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = CENTER_ALIGN

    headers = ["Evidence ID", "Evidence Type", "Description", "Related Assessment", "Location/Link", "Date Collected", "Collected By", "Status"]
    create_header_row(ws, 3, headers)

    evidence = [
        ("EV-517-SA-001", "System List", "Authentication system inventory", "System_Inventory", "", "", "", ""),
        ("EV-517-SA-002", "Config Export", "AD Group Policy settings", "Security_Assessment", "", "", "", ""),
        ("EV-517-SA-003", "Config Export", "Microsoft Entra ID (formerly Azure AD) conditional access policies", "Security_Assessment", "", "", "", ""),
        ("EV-517-SA-004", "Vendor Docs", "Password storage documentation", "Storage_Assessment", "", "", "", ""),
        ("EV-517-SA-005", "Config Export", "SSO integration configurations", "Integration_Assessment", "", "", "", ""),
    ]

    row = 4
    for item in evidence:
        for col, value in enumerate(item, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col in [5, 6, 7, 8]:
                cell.fill = INPUT_FILL
        row += 1

    for i in range(10):
        for col in range(1, 9):
            cell = ws.cell(row=row, column=col, value="")
            cell.border = THIN_BORDER
            cell.fill = INPUT_FILL
        row += 1

    add_data_validation(ws, f"H4:H{row-1}", '"Pending,Collected,Verified,Expired,N/A"')

    set_column_widths(ws, {"A": 16, "B": 16, "C": 35, "D": 22, "E": 28, "F": 15, "G": 16, "H": 12})
    ws.freeze_panes = "A4"
    logger.info("Created Evidence_Register sheet")


def create_approval_signoff_sheet(wb: Workbook):
    ws = wb.create_sheet("Approval_SignOff")

    ws.merge_cells("A1:F1")
    ws["A1"].value = "Assessment Approval and Sign-Off"
    ws["A1"].font = HEADER_FONT
    ws["A1"].fill = HEADER_FILL
    ws["A1"].alignment = CENTER_ALIGN

    ws.cell(row=3, column=1, value="Document Information").font = BOLD_FONT

    info = [
        ("Document ID:", DOCUMENT_ID, "Version:", "1.0"),
        ("Document Title:", WORKBOOK_NAME, "Date:", GENERATED_DATE),
        ("Control Reference:", CONTROL_ID, "Classification:", "INTERNAL"),
    ]

    row = 4
    for item in info:
        ws.cell(row=row, column=1, value=item[0]).font = BOLD_FONT
        ws.cell(row=row, column=2, value=item[1]).font = NORMAL_FONT
        ws.cell(row=row, column=3, value=item[2]).font = BOLD_FONT
        ws.cell(row=row, column=4, value=item[3]).font = NORMAL_FONT
        row += 1

    row += 1
    ws.cell(row=row, column=1, value="Assessment Summary").font = BOLD_FONT
    row += 1
    summary_headers = ["Area", "Systems", "Compliant", "Partial", "Non-Compliant"]
    create_header_row(ws, row, summary_headers + [""])

    row += 1
    areas = ["Authentication Systems", "Password Storage", "SSO Integration", "TOTAL"]
    for area in areas:
        ws.cell(row=row, column=1, value=area).font = BOLD_FONT if area == "TOTAL" else NORMAL_FONT
        for col in range(2, 6):
            cell = ws.cell(row=row, column=col, value="")
            cell.border = THIN_BORDER
            cell.fill = INPUT_FILL
        ws.cell(row=row, column=1).border = THIN_BORDER
        row += 1

    row += 1
    ws.cell(row=row, column=1, value="Approval Signatures").font = BOLD_FONT

    row += 1
    headers = ["Role", "Name", "Signature", "Date", "Status", "Comments"]
    create_header_row(ws, row, headers)

    row += 1
    approvers = [
        ("Assessment Lead", "", "", "", "", ""),
        ("IT Security Manager", "", "", "", "", ""),
        ("Information Security Officer", "", "", "", "", ""),
    ]

    for approver in approvers:
        for col, value in enumerate(approver, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col > 1:
                cell.fill = INPUT_FILL
        row += 1

    add_data_validation(ws, f"E{row-3}:E{row-1}", '"Pending,Approved,Rejected,Deferred"')

    set_column_widths(ws, {"A": 25, "B": 20, "C": 18, "D": 15, "E": 15, "F": 28})
    ws.freeze_panes = "A4"
    logger.info("Created Approval_SignOff sheet")


def main():
    logger.info("=" * 70)
    logger.info(f"{DOCUMENT_ID} {WORKBOOK_NAME} Generator")
    logger.info("=" * 70)

    wb = Workbook()

    create_instructions_sheet(wb)
    create_system_inventory_sheet(wb)
    create_security_assessment_sheet(wb)
    create_storage_assessment_sheet(wb)
    create_integration_assessment_sheet(wb)
    create_gap_analysis_sheet(wb)
    create_evidence_register_sheet(wb)
    create_approval_signoff_sheet(wb)

    output_path = Path(__file__).parent / OUTPUT_FILENAME
    wb.save(output_path)

    logger.info("=" * 70)
    logger.info(f"SUCCESS: Workbook saved as {OUTPUT_FILENAME}")
    logger.info("=" * 70)

    return 0


if __name__ == "__main__":
    sys.exit(main())


# =============================================================================
# QA_VERIFIED: 2026-02-01
# QA_STATUS: PASSED
# QA_TOOL: Claude Code
# CHANGES: Initial creation for A.5.17 Authentication Information control
# =============================================================================
