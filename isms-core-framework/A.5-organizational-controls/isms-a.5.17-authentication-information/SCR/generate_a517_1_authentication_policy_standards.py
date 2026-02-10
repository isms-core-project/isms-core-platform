#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
================================================================================
A.5.17.1 Authentication Policy and Standards Generator
================================================================================

Generates Excel workbook for documenting authentication policies including
password requirements, MFA standards, and credential management rules
per ISO 27001:2022 A.5.17.

Sheets:
    1. Instructions - Completion guidance
    2. Password_Policy - Password complexity and lifecycle requirements
    3. MFA_Requirements - Multi-factor authentication standards
    4. Credential_Standards - Standards for different credential types
    5. User_Responsibilities - User obligations for authentication info
    6. System_Requirements - Technical requirements for auth systems
    7. Evidence_Register - Supporting documentation
    8. Approval_SignOff - Authorization workflow

Usage:
    python3 generate_a517_1_authentication_policy_standards.py

Output:
    ISMS-IMP-A.5.17.1_Authentication_Policy_and_Standards_YYYYMMDD.xlsx
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
DOCUMENT_ID = "ISMS-IMP-A.5.17.1"
WORKBOOK_NAME = "Authentication Policy and Standards"
CONTROL_ID = "A.5.17"
CONTROL_NAME = "Authentication Information"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

# =============================================================================
# STYLE DEFINITIONS
# =============================================================================
HEADER_FILL = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
SUBHEADER_FILL = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
INPUT_FILL = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
MANDATORY_FILL = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid")

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


def create_header_row(ws, row: int, headers: list, fill=SUBHEADER_FILL, font=SUBHEADER_FONT):
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col, value=header)
        cell.font = font
        cell.fill = fill
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
    title_cell = ws["A1"]
    title_cell.value = f"{DOCUMENT_ID} - {WORKBOOK_NAME}"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    metadata = [
        ("Document ID:", DOCUMENT_ID),
        ("Control Reference:", CONTROL_REF),
        ("Generated Date:", GENERATED_DATE),
        ("Version:", "1.0"),
        ("Classification:", "INTERNAL"),
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
    purpose_cell = ws.cell(row=row, column=1)
    purpose_cell.value = (
        "This workbook documents authentication policies and standards per ISO 27001:2022 A.5.17. "
        "It defines password requirements, multi-factor authentication standards, and user responsibilities "
        "for handling authentication information. Use this to establish and maintain secure credential management."
    )
    purpose_cell.font = NORMAL_FONT
    purpose_cell.alignment = TOP_LEFT_ALIGN
    ws.row_dimensions[row].height = 50

    row += 2
    ws.cell(row=row, column=1, value="SHEET DESCRIPTIONS").font = BOLD_FONT
    row += 1

    sheets = [
        ("Password_Policy", "Password complexity, length, and lifecycle requirements"),
        ("MFA_Requirements", "Multi-factor authentication standards and applicability"),
        ("Credential_Standards", "Standards for passwords, tokens, certificates, biometrics"),
        ("User_Responsibilities", "User obligations for credential handling"),
        ("System_Requirements", "Technical requirements for authentication systems"),
        ("Evidence_Register", "Supporting documentation and evidence"),
        ("Approval_SignOff", "Policy approval workflow"),
    ]

    for sheet_name, description in sheets:
        ws.cell(row=row, column=1, value=sheet_name).font = BOLD_FONT
        ws.cell(row=row, column=2, value=description).font = NORMAL_FONT
        row += 1

    set_column_widths(ws, {"A": 25, "B": 55, "C": 20, "D": 20, "E": 20, "F": 20, "G": 20, "H": 20})
    ws.freeze_panes = "A3"
    logger.info("Created Instructions sheet")


def create_password_policy_sheet(wb: Workbook):
    ws = wb.create_sheet("Password_Policy")

    ws.merge_cells("A1:G1")
    title_cell = ws["A1"]
    title_cell.value = "Password Policy Requirements"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    headers = ["Requirement Category", "Policy Requirement", "Standard Value", "Current Setting", "Compliant", "Implementation Notes", "Exception Process"]
    create_header_row(ws, 3, headers)

    requirements = [
        ("Minimum Length", "Minimum password length", "≥12 characters", "", "", "", ""),
        ("Maximum Length", "Maximum password length (no artificial limit)", "≥128 characters", "", "", "", ""),
        ("Complexity - Uppercase", "Require uppercase letters", "Yes", "", "", "", ""),
        ("Complexity - Lowercase", "Require lowercase letters", "Yes", "", "", "", ""),
        ("Complexity - Numbers", "Require numeric characters", "Yes", "", "", "", ""),
        ("Complexity - Special", "Require special characters", "Yes", "", "", "", ""),
        ("Password History", "Number of previous passwords prevented", "≥12 passwords", "", "", "", ""),
        ("Maximum Age", "Maximum password age before mandatory change", "≤365 days", "", "", "", ""),
        ("Minimum Age", "Minimum age before password can be changed", "≥1 day", "", "", "", ""),
        ("Initial Password", "Temporary password requirements", "Force change on first login", "", "", "", ""),
        ("Common Passwords", "Block commonly used/breached passwords", "Yes - use blocklist", "", "", "", ""),
        ("Sequential Characters", "Block sequential characters (abc, 123)", "Yes", "", "", "", ""),
        ("Username in Password", "Block username or variations in password", "Yes", "", "", "", ""),
        ("Dictionary Words", "Block dictionary words", "Recommended", "", "", "", ""),
        ("Password Hints", "Disable password hints", "Yes", "", "", "", ""),
        ("Account Lockout Threshold", "Failed attempts before lockout", "5-10 attempts", "", "", "", ""),
        ("Lockout Duration", "Account lockout duration", "≥15 minutes", "", "", "", ""),
        ("Password Storage", "Secure storage algorithm", "bcrypt/Argon2/PBKDF2", "", "", "", ""),
        ("Transmission Security", "Password transmission encryption", "TLS 1.2+ required", "", "", "", ""),
    ]

    row = 4
    for req in requirements:
        for col, value in enumerate(req, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col in [4, 5, 6, 7]:
                cell.fill = INPUT_FILL
        row += 1

    add_data_validation(ws, f"E4:E{row+5}", '"Yes,No,Partial,N/A"')

    set_column_widths(ws, {"A": 22, "B": 40, "C": 22, "D": 20, "E": 12, "F": 30, "G": 25})
    ws.freeze_panes = "A4"
    logger.info("Created Password_Policy sheet")


def create_mfa_requirements_sheet(wb: Workbook):
    ws = wb.create_sheet("MFA_Requirements")

    ws.merge_cells("A1:H1")
    title_cell = ws["A1"]
    title_cell.value = "Multi-Factor Authentication Requirements"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    headers = ["System/Access Type", "MFA Required", "Approved Methods", "Fallback Method", "Current Status", "Implementation Date", "Owner", "Notes"]
    create_header_row(ws, 3, headers)

    systems = [
        ("VPN Remote Access", "MANDATORY", "TOTP, Push Notification, FIDO2", "SMS (emergency only)", "", "", "", ""),
        ("Cloud Applications (M365, etc.)", "MANDATORY", "Authenticator App, FIDO2", "Phone call", "", "", "", ""),
        ("Privileged Access (Admin)", "MANDATORY", "Hardware Token, FIDO2", "Authenticator App", "", "", "", ""),
        ("Email (External Access)", "MANDATORY", "TOTP, Push Notification", "SMS", "", "", "", ""),
        ("Internal Applications (Sensitive)", "MANDATORY", "Authenticator App, FIDO2", "SMS", "", "", "", ""),
        ("Internal Applications (Standard)", "RECOMMENDED", "Authenticator App", "N/A", "", "", "", ""),
        ("Database Access (Production)", "MANDATORY", "Hardware Token, Certificate", "TOTP", "", "", "", ""),
        ("Source Code Repository", "MANDATORY", "TOTP, FIDO2", "Authenticator App", "", "", "", ""),
        ("CI/CD Pipeline", "MANDATORY", "Service Account + Certificate", "Hardware Token", "", "", "", ""),
        ("Customer Portal (Admin)", "MANDATORY", "TOTP, Push Notification", "SMS", "", "", "", ""),
        ("Customer Portal (Users)", "RECOMMENDED", "TOTP, Email OTP", "Security Questions", "", "", "", ""),
        ("Workstation Login", "CONDITIONAL", "Windows Hello, Smart Card", "Password only", "", "", "", ""),
        ("Server Console Access", "MANDATORY", "Hardware Token, Certificate", "TOTP", "", "", "", ""),
        ("Cloud Infrastructure (AWS/Azure)", "MANDATORY", "FIDO2, Hardware Token", "Authenticator App", "", "", "", ""),
    ]

    row = 4
    for system in systems:
        for col, value in enumerate(system, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col in [5, 6, 7, 8]:
                cell.fill = INPUT_FILL
            if value == "MANDATORY":
                cell.fill = MANDATORY_FILL
                cell.font = BOLD_FONT
        row += 1

    add_data_validation(ws, f"B4:B{row+5}", '"MANDATORY,RECOMMENDED,CONDITIONAL,NOT REQUIRED"')
    add_data_validation(ws, f"E4:E{row+5}", '"Implemented,In Progress,Planned,Not Started,Exception"')

    set_column_widths(ws, {"A": 30, "B": 14, "C": 32, "D": 22, "E": 16, "F": 18, "G": 18, "H": 25})
    ws.freeze_panes = "A4"
    logger.info("Created MFA_Requirements sheet")


def create_credential_standards_sheet(wb: Workbook):
    ws = wb.create_sheet("Credential_Standards")

    ws.merge_cells("A1:H1")
    title_cell = ws["A1"]
    title_cell.value = "Credential Type Standards"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    headers = ["Credential Type", "Use Cases", "Security Requirements", "Storage Requirements", "Rotation Policy", "Revocation Process", "Approved Products", "Notes"]
    create_header_row(ws, 3, headers)

    credentials = [
        ("User Passwords", "End-user authentication", "Min 12 chars, complexity", "bcrypt/Argon2, salted", "Annual or incident", "Immediate on termination", "N/A", ""),
        ("Service Account Passwords", "Application-to-application", "Min 24 chars, random", "Secrets manager (Vault)", "Quarterly", "Change on compromise", "HashiCorp Vault, Azure Key Vault", ""),
        ("API Keys", "API authentication", "Min 32 chars, random", "Secrets manager", "Quarterly", "Immediate revocation", "HashiCorp Vault, AWS Secrets Manager", ""),
        ("SSH Keys", "Server/system access", "RSA 4096-bit or Ed25519", "Encrypted key store", "Annual", "Remove from authorized_keys", "OpenSSH", ""),
        ("SSL/TLS Certificates", "Server authentication", "RSA 2048+ or ECC P-256+", "HSM or secure store", "Annual (max 1 year)", "CRL/OCSP update", "DigiCert, Let's Encrypt", ""),
        ("Client Certificates", "User/device authentication", "RSA 2048+ or ECC P-256+", "Smart card or TPM", "Annual", "CRL/OCSP update", "Internal PKI", ""),
        ("TOTP Seeds", "MFA time-based codes", "Min 160-bit secret", "Encrypted in auth system", "On device change", "Remove from account", "Microsoft Authenticator, Google Auth", ""),
        ("FIDO2/WebAuthn", "Passwordless MFA", "Platform authenticator", "Device TPM/Secure Element", "N/A (hardware bound)", "Remove registration", "YubiKey, Windows Hello", ""),
        ("Hardware Tokens", "High-security MFA", "FIPS 140-2 Level 2+", "Physical custody", "5 years or damage", "Return and deactivate", "YubiKey, RSA SecurID", ""),
        ("Biometric Data", "Local device auth", "On-device processing only", "Never stored centrally", "N/A", "Device wipe", "Windows Hello, Touch ID", ""),
        ("Recovery Codes", "MFA backup", "Random 8-digit codes", "User-managed secure storage", "On use or annually", "Regenerate", "N/A", ""),
    ]

    row = 4
    for cred in credentials:
        for col, value in enumerate(cred, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col == 8:
                cell.fill = INPUT_FILL
        row += 1

    set_column_widths(ws, {"A": 22, "B": 25, "C": 28, "D": 28, "E": 20, "F": 25, "G": 30, "H": 25})
    ws.freeze_panes = "A4"
    logger.info("Created Credential_Standards sheet")


def create_user_responsibilities_sheet(wb: Workbook):
    ws = wb.create_sheet("User_Responsibilities")

    ws.merge_cells("A1:F1")
    title_cell = ws["A1"]
    title_cell.value = "User Responsibilities for Authentication Information"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    headers = ["Responsibility", "Description", "Requirement Level", "Enforcement Method", "Training Required", "Notes"]
    create_header_row(ws, 3, headers)

    responsibilities = [
        ("Password Confidentiality", "Never share passwords with anyone including IT staff", "MANDATORY", "Policy acknowledgment, monitoring", "Yes", ""),
        ("Unique Passwords", "Use unique passwords for each system/service", "MANDATORY", "Password manager provided", "Yes", ""),
        ("Password Strength", "Create passwords meeting complexity requirements", "MANDATORY", "Technical enforcement", "Yes", ""),
        ("Secure Storage", "Never write down passwords or store in plain text", "MANDATORY", "Approved password manager", "Yes", ""),
        ("Compromise Reporting", "Immediately report suspected credential compromise", "MANDATORY", "Incident reporting process", "Yes", ""),
        ("MFA Device Security", "Protect MFA devices (phones, tokens) from unauthorised access", "MANDATORY", "Device management policy", "Yes", ""),
        ("Phishing Awareness", "Verify authenticity before entering credentials", "MANDATORY", "Security awareness training", "Yes", ""),
        ("Session Security", "Lock workstation when away, log out of shared systems", "MANDATORY", "Auto-lock policies", "Yes", ""),
        ("Personal Device MFA", "Secure personal devices used for MFA", "CONDITIONAL", "MDM for BYOD", "Yes", ""),
        ("Recovery Code Storage", "Store MFA recovery codes securely offline", "MANDATORY", "User guidance provided", "Yes", ""),
        ("Credential Sharing Prohibition", "Never use shared accounts for individual actions", "MANDATORY", "Audit logging", "Yes", ""),
        ("Employment Contract", "Acknowledge password responsibilities in contract", "MANDATORY", "HR onboarding process", "No", ""),
    ]

    row = 4
    for resp in responsibilities:
        for col, value in enumerate(resp, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col == 6:
                cell.fill = INPUT_FILL
        row += 1

    add_data_validation(ws, f"C4:C{row+5}", '"MANDATORY,RECOMMENDED,CONDITIONAL"')
    add_data_validation(ws, f"E4:E{row+5}", '"Yes,No,Completed"')

    set_column_widths(ws, {"A": 28, "B": 45, "C": 18, "D": 30, "E": 16, "F": 25})
    ws.freeze_panes = "A4"
    logger.info("Created User_Responsibilities sheet")


def create_system_requirements_sheet(wb: Workbook):
    ws = wb.create_sheet("System_Requirements")

    ws.merge_cells("A1:G1")
    title_cell = ws["A1"]
    title_cell.value = "Authentication System Technical Requirements"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    headers = ["Requirement Area", "Technical Requirement", "Standard/Protocol", "Implementation", "Status", "Evidence", "Notes"]
    create_header_row(ws, 3, headers)

    requirements = [
        ("Password Hashing", "Use approved password hashing algorithms", "bcrypt (cost≥12), Argon2id, PBKDF2", "", "", "", ""),
        ("Salt Generation", "Unique cryptographic salt per password", "Min 128-bit random salt", "", "", "", ""),
        ("Transmission Security", "Encrypt credentials in transit", "TLS 1.2+ only", "", "", "", ""),
        ("Session Management", "Secure session token handling", "HttpOnly, Secure, SameSite cookies", "", "", "", ""),
        ("Account Lockout", "Implement progressive lockout", "5-10 attempts, 15+ min lockout", "", "", "", ""),
        ("Brute Force Protection", "Rate limiting on authentication", "Max 5 attempts/minute per IP", "", "", "", ""),
        ("Audit Logging", "Log all authentication events", "Success, failure, lockout, unlock", "", "", "", ""),
        ("Secure Recovery", "Secure password reset process", "Email verification, time-limited tokens", "", "", "", ""),
        ("MFA Integration", "Support for MFA protocols", "TOTP, WebAuthn/FIDO2, Push", "", "", "", ""),
        ("SSO Support", "Support for single sign-on", "SAML 2.0, OIDC, OAuth 2.0", "", "", "", ""),
        ("Password Exposure Check", "Check against breached password databases", "HIBP API integration", "", "", "", ""),
        ("Credential Isolation", "Separate credential stores by environment", "Prod/dev/test separation", "", "", "", ""),
        ("Secrets Management", "Centralised secrets management", "HashiCorp Vault, Azure Key Vault", "", "", "", ""),
        ("Certificate Management", "Automated certificate lifecycle", "ACME, internal PKI", "", "", "", ""),
    ]

    row = 4
    for req in requirements:
        for col, value in enumerate(req, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col in [4, 5, 6, 7]:
                cell.fill = INPUT_FILL
        row += 1

    add_data_validation(ws, f"E4:E{row+5}", '"Implemented,In Progress,Planned,Not Started,N/A"')

    set_column_widths(ws, {"A": 22, "B": 35, "C": 32, "D": 25, "E": 14, "F": 20, "G": 25})
    ws.freeze_panes = "A4"
    logger.info("Created System_Requirements sheet")


def create_evidence_register_sheet(wb: Workbook):
    ws = wb.create_sheet("Evidence_Register")

    ws.merge_cells("A1:H1")
    title_cell = ws["A1"]
    title_cell.value = "Evidence Register - Authentication Policy"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    headers = ["Evidence ID", "Evidence Type", "Description", "Related Section", "Location/Link", "Date Collected", "Collected By", "Status"]
    create_header_row(ws, 3, headers)

    evidence = [
        ("EV-517-001", "Policy Document", "Approved Authentication Policy", "Password_Policy", "", "", "", ""),
        ("EV-517-002", "Configuration Export", "Password policy settings from AD/Microsoft Entra ID (formerly Azure AD)", "Password_Policy", "", "", "", ""),
        ("EV-517-003", "Configuration Export", "MFA configuration settings", "MFA_Requirements", "", "", "", ""),
        ("EV-517-004", "Training Record", "User security awareness completion", "User_Responsibilities", "", "", "", ""),
        ("EV-517-005", "Audit Report", "Authentication controls assessment", "System_Requirements", "", "", "", ""),
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

    set_column_widths(ws, {"A": 15, "B": 20, "C": 35, "D": 20, "E": 30, "F": 15, "G": 18, "H": 12})
    ws.freeze_panes = "A4"
    logger.info("Created Evidence_Register sheet")


def create_approval_signoff_sheet(wb: Workbook):
    ws = wb.create_sheet("Approval_SignOff")

    ws.merge_cells("A1:F1")
    title_cell = ws["A1"]
    title_cell.value = "Policy Approval and Sign-Off"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

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
    ws.cell(row=row, column=1, value="Approval Signatures").font = BOLD_FONT

    row += 1
    approval_headers = ["Role", "Name", "Signature", "Date", "Status", "Comments"]
    create_header_row(ws, row, approval_headers)

    row += 1
    approvers = [
        ("Policy Owner", "", "", "", "", ""),
        ("IT Security Manager", "", "", "", "", ""),
        ("Information Security Officer", "", "", "", "", ""),
        ("CISO", "", "", "", "", ""),
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

    add_data_validation(ws, f"E{row-4}:E{row-1}", '"Pending,Approved,Rejected,Deferred"')

    set_column_widths(ws, {"A": 25, "B": 25, "C": 20, "D": 15, "E": 15, "F": 30})
    ws.freeze_panes = "A4"
    logger.info("Created Approval_SignOff sheet")


def main():
    logger.info("=" * 70)
    logger.info(f"{DOCUMENT_ID} {WORKBOOK_NAME} Generator")
    logger.info("=" * 70)

    wb = Workbook()

    create_instructions_sheet(wb)
    create_password_policy_sheet(wb)
    create_mfa_requirements_sheet(wb)
    create_credential_standards_sheet(wb)
    create_user_responsibilities_sheet(wb)
    create_system_requirements_sheet(wb)
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
