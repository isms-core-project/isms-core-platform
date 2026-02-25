#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
================================================================================
A.5.14.3 Transfer Agreements Register Generator
================================================================================

Generates Excel workbook for managing information transfer agreements with
third parties, including data sharing agreements, interconnection security
agreements, and memoranda of understanding per ISO 27001:2022 A.5.14.

Sheets:
    1. Instructions - Completion guidance
    2. Agreement_Register - Master list of transfer agreements
    3. Agreement_Requirements - Standard clauses and requirements
    4. Third_Party_Assessment - Security posture of transfer partners
    5. Review_Schedule - Agreement review and renewal tracking
    6. Evidence_Register - Supporting documentation
    7. Approval_SignOff - Authorization workflow

Usage:
    python3 generate_a514_3_transfer_agreements_register.py

Output:
    ISMS-IMP-A.5.14.3_Transfer_Agreements_Register_YYYYMMDD.xlsx

================================================================================
"""

import logging
import sys
from datetime import datetime
from pathlib import Path

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
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
DOCUMENT_ID = "ISMS-IMP-A.5.14.3"
WORKBOOK_NAME = "Transfer Agreements Register"
CONTROL_ID = "A.5.14"
CONTROL_NAME = "Information Transfer"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

# Timestamps
GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")

# Output filename
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

# =============================================================================
# STYLE DEFINITIONS
# =============================================================================
HEADER_FILL = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
SUBHEADER_FILL = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
INPUT_FILL = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
ACTIVE_FILL = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
EXPIRING_FILL = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
EXPIRED_FILL = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")

HEADER_FONT = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
SUBHEADER_FONT = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
BOLD_FONT = Font(name="Calibri", size=11, bold=True)
NORMAL_FONT = Font(name="Calibri", size=11)

THIN_BORDER = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin")
)

CENTER_ALIGN = Alignment(horizontal="center", vertical="center", wrap_text=True)
LEFT_ALIGN = Alignment(horizontal="left", vertical="center", wrap_text=True)
TOP_LEFT_ALIGN = Alignment(horizontal="left", vertical="top", wrap_text=True)


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================
def set_column_widths(ws, widths: dict):
    """Set column widths from a dictionary."""
    for col, width in widths.items():
        ws.column_dimensions[col].width = width


def create_header_row(ws, row: int, headers: list, fill=SUBHEADER_FILL, font=SUBHEADER_FONT):
    """Create a styled header row."""
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col, value=header)
        cell.font = font
        cell.fill = fill
        cell.alignment = CENTER_ALIGN
        cell.border = THIN_BORDER


def add_data_validation(ws, cell_range: str, formula: str):
    """Add dropdown data validation."""
    dv = DataValidation(type="list", formula1=formula, showDropDown=False, allowBlank=True)
    dv.showInputMessage = True
    ws.add_data_validation(dv)
    dv.add(cell_range)


# =============================================================================
# SHEET CREATORS
# =============================================================================
def create_instructions_sheet(wb: Workbook):
    """Create the Instructions sheet."""
    ws = wb.active
    ws.title = "Instructions"

    # Title
    ws.merge_cells("A1:H1")
    title_cell = ws["A1"]
    title_cell.value = f"{DOCUMENT_ID} - {WORKBOOK_NAME}"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    # Metadata
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

    # Purpose
    row += 1
    ws.cell(row=row, column=1, value="PURPOSE").font = BOLD_FONT
    row += 1
    ws.merge_cells(f"A{row}:H{row}")
    purpose_cell = ws.cell(row=row, column=1)
    purpose_cell.value = (
        "This workbook maintains a register of all information transfer agreements with third parties. "
        "It tracks data sharing agreements, interconnection security agreements (ISAs), memoranda of "
        "understanding (MOUs), and other contractual arrangements governing information exchange. "
        "Use this register to ensure all transfer relationships are documented, reviewed, and compliant."
    )
    purpose_cell.font = NORMAL_FONT
    purpose_cell.alignment = TOP_LEFT_ALIGN
    ws.row_dimensions[row].height = 60

    # Sheet descriptions
    row += 2
    ws.cell(row=row, column=1, value="SHEET DESCRIPTIONS").font = BOLD_FONT
    row += 1

    sheets = [
        ("Agreement_Register", "Master list of all transfer agreements and their status"),
        ("Agreement_Requirements", "Standard clauses and security requirements for agreements"),
        ("Third_Party_Assessment", "Security posture assessment of transfer partners"),
        ("Review_Schedule", "Agreement review and renewal tracking schedule"),
        ("Evidence_Register", "Supporting documentation and evidence"),
        ("Approval_SignOff", "Register approval workflow"),
    ]

    for sheet_name, description in sheets:
        ws.cell(row=row, column=1, value=sheet_name).font = BOLD_FONT
        ws.cell(row=row, column=2, value=description).font = NORMAL_FONT
        row += 1

    # Agreement types
    row += 1
    ws.cell(row=row, column=1, value="AGREEMENT TYPES").font = BOLD_FONT
    row += 1

    types = [
        ("DSA - Data Sharing Agreement", "Governs sharing of specific data sets between parties"),
        ("ISA - Interconnection Security Agreement", "Technical security requirements for system interconnections"),
        ("MOU - Memorandum of Understanding", "High-level agreement on information exchange purposes"),
        ("DPA - Data Processing Agreement", "GDPR-required agreement for data processors"),
        ("SCC - Standard Contractual Clauses", "EU-approved clauses for international data transfers"),
        ("NDA - Non-Disclosure Agreement", "Confidentiality obligations for information exchange"),
    ]

    for type_name, description in types:
        ws.cell(row=row, column=1, value=type_name).font = BOLD_FONT
        ws.cell(row=row, column=2, value=description).font = NORMAL_FONT
        row += 1

    set_column_widths(ws, {"A": 35, "B": 55, "C": 20, "D": 20, "E": 20, "F": 20, "G": 20, "H": 20})
    ws.freeze_panes = "A3"

    logger.info("Created Instructions sheet")


def create_agreement_register_sheet(wb: Workbook):
    """Create the Agreement Register sheet."""
    ws = wb.create_sheet("Agreement_Register")

    # Title
    ws.merge_cells("A1:L1")
    title_cell = ws["A1"]
    title_cell.value = "Information Transfer Agreements Register"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    # Headers
    headers = ["Agreement ID", "Agreement Type", "Third Party", "Purpose/Scope", "Data Classification", "Transfer Direction", "Effective Date", "Expiry Date", "Review Date", "Owner", "Status", "Notes"]
    create_header_row(ws, 3, headers)

    # Sample entries
    agreements = [
        ("AGR-001", "DSA", "Example Partner Ltd", "Customer analytics data sharing", "CONFIDENTIAL", "Bi-directional", "", "", "", "", "Active", ""),
        ("AGR-002", "ISA", "Cloud Provider Inc", "API integration for services", "INTERNAL", "Outbound", "", "", "", "", "Active", ""),
        ("AGR-003", "DPA", "SaaS Vendor GmbH", "HR data processing", "CONFIDENTIAL", "Outbound", "", "", "", "", "Active", ""),
        ("AGR-004", "SCC", "US Subsidiary Corp", "EU-US data transfers", "CONFIDENTIAL", "Outbound", "", "", "", "", "Active", ""),
        ("AGR-005", "MOU", "Research University", "Research collaboration", "INTERNAL", "Bi-directional", "", "", "", "", "Draft", ""),
    ]

    row = 4
    for agr in agreements:
        for col, value in enumerate(agr, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col in [7, 8, 9, 10, 11, 12]:  # Input fields
                cell.fill = INPUT_FILL
        row += 1

    # Add empty rows for new entries
    for i in range(15):
        for col in range(1, 13):
            cell = ws.cell(row=row, column=col, value="")
            cell.border = THIN_BORDER
            cell.fill = INPUT_FILL
        row += 1

    # Data validation
    add_data_validation(ws, f"B4:B{row-1}", '"DSA,ISA,MOU,DPA,SCC,NDA,Other"')
    add_data_validation(ws, f"E4:E{row-1}", '"PUBLIC,INTERNAL,CONFIDENTIAL,RESTRICTED"')
    add_data_validation(ws, f"F4:F{row-1}", '"Inbound,Outbound,Bi-directional"')
    add_data_validation(ws, f"K4:K{row-1}", '"Draft,Under Review,Active,Expiring Soon,Expired,Terminated"')

    set_column_widths(ws, {"A": 14, "B": 16, "C": 22, "D": 30, "E": 18, "F": 16, "G": 14, "H": 14, "I": 14, "J": 18, "K": 14, "L": 25})
    ws.freeze_panes = "A4"

    logger.info("Created Agreement_Register sheet")


def create_agreement_requirements_sheet(wb: Workbook):
    """Create the Agreement Requirements sheet."""
    ws = wb.create_sheet("Agreement_Requirements")

    # Title
    ws.merge_cells("A1:G1")
    title_cell = ws["A1"]
    title_cell.value = "Standard Agreement Requirements and Clauses"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    # Headers
    headers = ["Requirement Category", "Clause/Requirement", "Mandatory For", "Rationale", "Template Reference", "Applicability", "Notes"]
    create_header_row(ws, 3, headers)

    # Requirements
    requirements = [
        ("Data Protection", "Data classification handling requirements", "All agreements", "Ensure appropriate protection levels", "ISMS-TEMP-001 §4.1", "CONFIDENTIAL+", ""),
        ("Data Protection", "Encryption requirements (at rest and in transit)", "DSA, ISA, DPA", "Protect data confidentiality", "ISMS-TEMP-001 §4.2", "INTERNAL+", ""),
        ("Data Protection", "Data retention and deletion obligations", "DSA, DPA", "Minimize data exposure", "ISMS-TEMP-001 §4.3", "All", ""),
        ("Access Control", "Authorised user/system identification", "ISA, DSA", "Limit access to authorised parties", "ISMS-TEMP-001 §5.1", "All", ""),
        ("Access Control", "Authentication requirements", "ISA", "Verify identity of connecting systems", "ISMS-TEMP-001 §5.2", "All", ""),
        ("Access Control", "Access logging and audit trail", "All agreements", "Enable incident investigation", "ISMS-TEMP-001 §5.3", "INTERNAL+", ""),
        ("Incident Response", "Security incident notification requirements", "All agreements", "Timely breach notification", "ISMS-TEMP-001 §6.1", "All", ""),
        ("Incident Response", "Incident response coordination procedures", "ISA, DSA", "Coordinated response", "ISMS-TEMP-001 §6.2", "CONFIDENTIAL+", ""),
        ("Compliance", "Right to audit clause", "DPA, DSA", "Verify compliance", "ISMS-TEMP-001 §7.1", "CONFIDENTIAL+", ""),
        ("Compliance", "Certification requirements (ISO 27001, SOC 2)", "DPA, ISA", "Baseline security assurance", "ISMS-TEMP-001 §7.2", "INTERNAL+", ""),
        ("Compliance", "Regulatory compliance obligations", "DPA, SCC", "Legal compliance", "ISMS-TEMP-001 §7.3", "All", ""),
        ("Liability", "Liability and indemnification clauses", "All agreements", "Risk allocation", "ISMS-TEMP-001 §8.1", "All", ""),
        ("Liability", "Insurance requirements", "DSA, DPA", "Financial protection", "ISMS-TEMP-001 §8.2", "CONFIDENTIAL+", ""),
        ("Termination", "Data return/destruction on termination", "All agreements", "Prevent data retention post-contract", "ISMS-TEMP-001 §9.1", "All", ""),
        ("Termination", "Transition assistance obligations", "DPA, ISA", "Business continuity", "ISMS-TEMP-001 §9.2", "CONFIDENTIAL+", ""),
        ("Sub-Processing", "Sub-processor approval requirements", "DPA", "GDPR compliance", "ISMS-TEMP-001 §10.1", "All", ""),
        ("Sub-Processing", "Sub-processor security requirements", "DPA", "Maintain security chain", "ISMS-TEMP-001 §10.2", "INTERNAL+", ""),
        ("Transfer Mechanisms", "Legal basis for international transfers", "SCC, DSA", "Cross-border compliance", "ISMS-TEMP-001 §11.1", "All", ""),
    ]

    row = 4
    for req in requirements:
        for col, value in enumerate(req, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col == 7:  # Notes input
                cell.fill = INPUT_FILL
        row += 1

    set_column_widths(ws, {"A": 20, "B": 40, "C": 18, "D": 30, "E": 20, "F": 18, "G": 25})
    ws.freeze_panes = "A4"

    logger.info("Created Agreement_Requirements sheet")


def create_third_party_assessment_sheet(wb: Workbook):
    """Create the Third Party Assessment sheet."""
    ws = wb.create_sheet("Third_Party_Assessment")

    # Title
    ws.merge_cells("A1:J1")
    title_cell = ws["A1"]
    title_cell.value = "Third Party Security Assessment"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    # Headers
    headers = ["Third Party", "Agreement ID", "Assessment Date", "ISO 27001 Certified", "SOC 2 Report", "Security Questionnaire", "Penetration Test", "Risk Rating", "Next Assessment", "Notes"]
    create_header_row(ws, 3, headers)

    # Sample entries
    assessments = [
        ("Example Partner Ltd", "AGR-001", "", "", "", "", "", "", "", ""),
        ("Cloud Provider Inc", "AGR-002", "", "", "", "", "", "", "", ""),
        ("SaaS Vendor GmbH", "AGR-003", "", "", "", "", "", "", "", ""),
        ("US Subsidiary Corp", "AGR-004", "", "", "", "", "", "", "", ""),
        ("Research University", "AGR-005", "", "", "", "", "", "", "", ""),
    ]

    row = 4
    for assessment in assessments:
        for col, value in enumerate(assessment, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col >= 3:  # Input fields
                cell.fill = INPUT_FILL
        row += 1

    # Add empty rows
    for i in range(10):
        for col in range(1, 11):
            cell = ws.cell(row=row, column=col, value="")
            cell.border = THIN_BORDER
            cell.fill = INPUT_FILL
        row += 1

    # Data validation
    add_data_validation(ws, f"D4:D{row-1}", '"Yes,No,In Progress,N/A"')
    add_data_validation(ws, f"E4:E{row-1}", '"Type I,Type II,Not Available,N/A"')
    add_data_validation(ws, f"F4:F{row-1}", '"Completed,Pending,Not Required"')
    add_data_validation(ws, f"G4:G{row-1}", '"Current (<12mo),Expired,Not Available,N/A"')
    add_data_validation(ws, f"H4:H{row-1}", '"Low,Medium,High,Critical"')

    set_column_widths(ws, {"A": 22, "B": 14, "C": 16, "D": 18, "E": 15, "F": 20, "G": 18, "H": 14, "I": 16, "J": 25})
    ws.freeze_panes = "A4"

    logger.info("Created Third_Party_Assessment sheet")


def create_review_schedule_sheet(wb: Workbook):
    """Create the Review Schedule sheet."""
    ws = wb.create_sheet("Review_Schedule")

    # Title
    ws.merge_cells("A1:I1")
    title_cell = ws["A1"]
    title_cell.value = "Agreement Review and Renewal Schedule"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    # Headers
    headers = ["Agreement ID", "Third Party", "Last Review Date", "Next Review Date", "Review Type", "Reviewer", "Review Status", "Action Required", "Notes"]
    create_header_row(ws, 3, headers)

    # Sample entries
    reviews = [
        ("AGR-001", "Example Partner Ltd", "", "", "Annual", "", "", "", ""),
        ("AGR-002", "Cloud Provider Inc", "", "", "Annual", "", "", "", ""),
        ("AGR-003", "SaaS Vendor GmbH", "", "", "Annual", "", "", "", ""),
        ("AGR-004", "US Subsidiary Corp", "", "", "Semi-Annual", "", "", "", ""),
        ("AGR-005", "Research University", "", "", "Annual", "", "", "", ""),
    ]

    row = 4
    for review in reviews:
        for col, value in enumerate(review, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col >= 3:  # Input fields
                cell.fill = INPUT_FILL
        row += 1

    # Add empty rows
    for i in range(10):
        for col in range(1, 10):
            cell = ws.cell(row=row, column=col, value="")
            cell.border = THIN_BORDER
            cell.fill = INPUT_FILL
        row += 1

    # Data validation
    add_data_validation(ws, f"E4:E{row-1}", '"Annual,Semi-Annual,Quarterly,Ad-hoc,Renewal"')
    add_data_validation(ws, f"G4:G{row-1}", '"Scheduled,In Progress,Completed,Overdue"')
    add_data_validation(ws, f"H4:H{row-1}", '"None,Update Clauses,Renegotiate,Terminate,Renew"')

    set_column_widths(ws, {"A": 14, "B": 22, "C": 16, "D": 16, "E": 14, "F": 20, "G": 14, "H": 18, "I": 30})
    ws.freeze_panes = "A4"

    logger.info("Created Review_Schedule sheet")


def create_evidence_register_sheet(wb: Workbook):
    """Create the Evidence Register sheet."""
    ws = wb.create_sheet("Evidence_Register")

    # Title
    ws.merge_cells("A1:H1")
    title_cell = ws["A1"]
    title_cell.value = "Evidence Register - Transfer Agreements"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    # Headers
    headers = ["Evidence ID", "Evidence Type", "Description", "Related Agreement", "Location/Link", "Date Collected", "Collected By", "Status"]
    create_header_row(ws, 3, headers)

    # Sample entries
    evidence = [
        ("EV-514-AGR-001", "Signed Agreement", "Executed DSA with Example Partner", "AGR-001", "", "", "", ""),
        ("EV-514-AGR-002", "Security Certificate", "ISO 27001 certificate for Cloud Provider", "AGR-002", "", "", "", ""),
        ("EV-514-AGR-003", "SOC 2 Report", "Type II SOC 2 report for SaaS Vendor", "AGR-003", "", "", "", ""),
        ("EV-514-AGR-004", "Legal Review", "Legal sign-off on SCC terms", "AGR-004", "", "", "", ""),
        ("EV-514-AGR-005", "Review Record", "Annual agreement review documentation", "All", "", "", "", ""),
    ]

    row = 4
    for item in evidence:
        for col, value in enumerate(item, 1):
            cell = ws.cell(row=row, column=col, value=value)
            cell.font = NORMAL_FONT
            cell.border = THIN_BORDER
            cell.alignment = LEFT_ALIGN
            if col in [5, 6, 7, 8]:  # Input fields
                cell.fill = INPUT_FILL
        row += 1

    # Add empty rows
    for i in range(10):
        for col in range(1, 9):
            cell = ws.cell(row=row, column=col, value="")
            cell.border = THIN_BORDER
            cell.fill = INPUT_FILL
        row += 1

    # Data validation
    add_data_validation(ws, f"H4:H{row-1}", '"Pending,Collected,Verified,Expired,N/A"')
    add_data_validation(ws, f"B4:B{row-1}", '"Signed Agreement,Security Certificate,SOC 2 Report,Audit Report,Legal Review,Review Record,Assessment,Other"')

    set_column_widths(ws, {"A": 18, "B": 20, "C": 35, "D": 18, "E": 30, "F": 15, "G": 18, "H": 12})
    ws.freeze_panes = "A4"

    logger.info("Created Evidence_Register sheet")


def create_approval_signoff_sheet(wb: Workbook):
    """Create the Approval and Sign-Off sheet."""
    ws = wb.create_sheet("Approval_SignOff")

    # Title
    ws.merge_cells("A1:F1")
    title_cell = ws["A1"]
    title_cell.value = "Register Approval and Sign-Off"
    title_cell.font = HEADER_FONT
    title_cell.fill = HEADER_FILL
    title_cell.alignment = CENTER_ALIGN

    # Document info
    ws.cell(row=3, column=1, value="Document Information").font = BOLD_FONT
    ws.merge_cells("A3:F3")

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

    # Register summary
    row += 1
    ws.cell(row=row, column=1, value="Register Summary").font = BOLD_FONT
    ws.merge_cells(f"A{row}:F{row}")

    row += 1
    summary_headers = ["Metric", "Count", "", "", "", ""]
    create_header_row(ws, row, summary_headers)

    row += 1
    metrics = [
        ("Total Agreements", ""),
        ("Active Agreements", ""),
        ("Expiring Within 90 Days", ""),
        ("Expired Agreements", ""),
        ("Agreements Requiring Review", ""),
    ]

    for metric, count in metrics:
        ws.cell(row=row, column=1, value=metric).font = NORMAL_FONT
        ws.cell(row=row, column=2, value=count).font = NORMAL_FONT
        ws.cell(row=row, column=2).fill = INPUT_FILL
        ws.cell(row=row, column=1).border = THIN_BORDER
        ws.cell(row=row, column=2).border = THIN_BORDER
        row += 1

    # Approval section
    row += 1
    ws.cell(row=row, column=1, value="Approval Signatures").font = BOLD_FONT
    ws.merge_cells(f"A{row}:F{row}")

    row += 1
    approval_headers = ["Role", "Name", "Signature", "Date", "Status", "Comments"]
    create_header_row(ws, row, approval_headers)

    row += 1
    approvers = [
        ("Register Owner", "", "", "", "", ""),
        ("Legal Representative", "", "", "", "", ""),
        ("Information Security Officer", "", "", "", "", ""),
        ("Data Protection Officer", "", "", "", "", ""),
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

    set_column_widths(ws, {"A": 28, "B": 25, "C": 20, "D": 15, "E": 15, "F": 30})
    ws.freeze_panes = "A4"

    logger.info("Created Approval_SignOff sheet")


# =============================================================================
# MAIN EXECUTION
# =============================================================================
def main():
    """Main execution function."""
    logger.info("=" * 70)
    logger.info(f"{DOCUMENT_ID} {WORKBOOK_NAME} Generator")
    logger.info("=" * 70)

    wb = Workbook()

    create_instructions_sheet(wb)
    create_agreement_register_sheet(wb)
    create_agreement_requirements_sheet(wb)
    create_third_party_assessment_sheet(wb)
    create_review_schedule_sheet(wb)
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
# CHANGES: Initial creation for A.5.14 Information Transfer control
# =============================================================================
