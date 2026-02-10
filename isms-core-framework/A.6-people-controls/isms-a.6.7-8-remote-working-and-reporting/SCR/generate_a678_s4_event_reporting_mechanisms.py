#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
================================================================================
ISMS-IMP-A.6.7-8.S4 - Event Reporting Mechanisms Assessment Excel Generator
================================================================================

ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Event Reporting)
Assessment Domain S4 of S5: Event Reporting Mechanisms Assessment

Reference Pattern: Based on ISMS-IMP-A.6.7-8.S4 specification
================================================================================
"""

import logging
import sys
from datetime import datetime

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.6.7-8.S4"
WORKBOOK_NAME = "Event Reporting Mechanisms Assessment"
CONTROL_ID = "A.6.7-8"
CONTROL_NAME = "Remote Working and Security Event Reporting"
CONTROL_REF = f"ISO/IEC 27001:2022 - Controls {CONTROL_ID}: {CONTROL_NAME}"

GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

# =============================================================================
# STYLE DEFINITIONS
# =============================================================================
def setup_styles():
    thin = Side(style="thin")
    border_thin = Border(left=thin, right=thin, top=thin, bottom=thin)
    return {
        "header": {"font": Font(name="Calibri", size=14, bold=True, color="FFFFFF"),
                   "fill": PatternFill(start_color="003366", end_color="003366", fill_type="solid"),
                   "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True)},
        "column_header": {"font": Font(name="Calibri", size=10, bold=True),
                          "fill": PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid"),
                          "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
                          "border": border_thin},
        "input_cell": {"fill": PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid"),
                       "alignment": Alignment(horizontal="left", vertical="center", wrap_text=True),
                       "border": border_thin},
        "border": border_thin,
    }

# =============================================================================
# PRE-POPULATED DATA
# =============================================================================
REPORTING_CHANNELS = [
    ("Security Email", "Dedicated email for security event reports", "Mandatory", "24/7"),
    ("Phone/Hotline", "Contact number for urgent security matters", "Mandatory", "24/7"),
    ("Ticketing System", "Formal ticket submission for events", "Mandatory", "Business Hours"),
    ("Anonymous Option", "Anonymous reporting mechanism", "Recommended", "24/7"),
    ("Chat/IM", "Secure instant messaging for urgent reports", "Optional", "Business Hours"),
]

CHANNEL_REQUIREMENTS = [
    ("Multiple Channels", "At least two distinct reporting channels available", "Mandatory"),
    ("24/7 Availability", "At least one channel available outside business hours", "Mandatory"),
    ("Remote Accessibility", "All channels accessible from remote locations", "Mandatory"),
    ("Clear Contact Info", "Reporting contacts prominently published", "Mandatory"),
    ("Acknowledgment", "All reports acknowledged within defined timeframes", "Mandatory"),
]

EVENT_CATEGORIES = [
    ("Phishing/Social Engineering", "Suspicious emails, calls, or manipulation attempts"),
    ("Malware/System Compromise", "Unexpected behaviour, pop-ups, ransomware indicators"),
    ("Unauthorised Access", "Unknown login attempts, unexpected account changes"),
    ("Data Breach/Leakage", "Misdirected emails, unauthorised data exposure"),
    ("Physical Security", "Lost/stolen devices, tailgating, missing equipment"),
    ("Policy Violations", "Observed circumvention of security controls"),
    ("Remote Work Specific", "Home network compromise, VPN issues, suspicious activity"),
    ("System Alterations", "Changes not via change control (ISO 27002:2022)"),
]

RESPONSE_TIMEFRAMES = [
    ("Acknowledgment", "Within 4 business hours"),
    ("Initial Assessment", "Within 24 hours"),
    ("Status Update", "Within 72 hours"),
    ("Closure Notification", "Upon resolution"),
]

NON_BLAME_PRINCIPLES = [
    ("Good Faith Protection", "Reporters SHALL NOT face consequences for good faith reporting"),
    ("Honest Mistake Handling", "Honest mistakes handled constructively"),
    ("No Retaliation", "Retaliation against reporters is prohibited"),
    ("Confidentiality", "Reporter identity protected to extent possible"),
]


def create_workbook() -> Workbook:
    wb = Workbook()
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])
    sheets = ["Instructions", "Channel_Assessment", "Channel_Availability", "Event_Categories",
              "Response_Timeframes", "NonBlame_Culture", "Awareness_Training", "Sample_Events",
              "Gap_Analysis", "Evidence_Register", "Dashboard", "Approval_Sign_Off"]
    for name in sheets:
        wb.create_sheet(title=name)
    return wb


def create_instructions_sheet(ws, styles):
    ws.merge_cells("A1:G1")
    ws["A1"] = f"{DOCUMENT_ID} - {WORKBOOK_NAME}\n{CONTROL_REF}"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]
    ws.row_dimensions[1].height = 40

    doc_info = [("Document ID", DOCUMENT_ID),
                ("Assessment Area", "Reporting Channels, Event Categories, Response Procedures"),
                ("Related Policy", "ISMS-POL-A.6.7-8, Section 3 (Event Reporting)"),
                ("Version", "1.0"), ("Assessment Date", ""), ("Completed By", "")]
    row = 4
    for label, value in doc_info:
        ws[f"A{row}"] = label
        ws[f"A{row}"].font = Font(bold=True)
        ws[f"B{row}"] = value
        if value == "":
            ws[f"B{row}"].fill = styles["input_cell"]["fill"]
            ws[f"B{row}"].border = styles["border"]
        row += 1
    ws.column_dimensions["A"].width = 30
    ws.column_dimensions["B"].width = 55


def create_channel_assessment_sheet(ws, styles):
    ws.merge_cells("A1:I1")
    ws["A1"] = "Reporting Channel Assessment"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]

    headers = ["Channel", "Description", "Requirement", "Availability", "Implemented",
               "Contact Info", "Remote Access", "Evidence", "Notes"]
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.border = styles["column_header"]["border"]

    row = 4
    for channel, desc, req, avail in REPORTING_CHANNELS:
        ws.cell(row=row, column=1, value=channel).border = styles["border"]
        ws.cell(row=row, column=2, value=desc).border = styles["border"]
        ws.cell(row=row, column=3, value=req).border = styles["border"]
        ws.cell(row=row, column=4, value=avail).border = styles["border"]
        for col in range(5, 10):
            cell = ws.cell(row=row, column=col, value="")
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
        row += 1

    yn_dv = DataValidation(type="list", formula1='"Yes,No,Partial"', allow_blank=True)
    ws.add_data_validation(yn_dv)
    yn_dv.add(f"E4:G{row-1}")

    ws.column_dimensions["A"].width = 18
    ws.column_dimensions["B"].width = 40
    for col in range(3, 10):
        ws.column_dimensions[get_column_letter(col)].width = 14


def create_channel_availability_sheet(ws, styles):
    ws.merge_cells("A1:H1")
    ws["A1"] = "Channel Availability Testing"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]

    headers = ["Channel", "Test Date", "Test Type", "Business Hours", "After Hours",
               "Weekend", "Result", "Next Test"]
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.border = styles["column_header"]["border"]

    for data_row in range(4, 14):
        for col in range(1, 9):
            cell = ws.cell(row=data_row, column=col, value="")
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]

    result_dv = DataValidation(type="list", formula1='"Pass,Fail,Partial"', allow_blank=True)
    ws.add_data_validation(result_dv)
    result_dv.add("G4:G13")

    avail_dv = DataValidation(type="list", formula1='"Available,Unavailable,Not Tested"', allow_blank=True)
    ws.add_data_validation(avail_dv)
    avail_dv.add("D4:F13")

    for col in range(1, 9):
        ws.column_dimensions[get_column_letter(col)].width = 15


def create_event_categories_sheet(ws, styles):
    ws.merge_cells("A1:H1")
    ws["A1"] = "Event Categories Assessment"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]

    headers = ["Category", "Description", "Documented", "Examples Provided", "In Training",
               "Personnel Aware", "Reports Received", "Notes"]
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.border = styles["column_header"]["border"]

    row = 4
    for category, description in EVENT_CATEGORIES:
        ws.cell(row=row, column=1, value=category).border = styles["border"]
        ws.cell(row=row, column=2, value=description).border = styles["border"]
        for col in range(3, 9):
            cell = ws.cell(row=row, column=col, value="")
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
        row += 1

    yn_dv = DataValidation(type="list", formula1='"Yes,No,Partial"', allow_blank=True)
    ws.add_data_validation(yn_dv)
    yn_dv.add(f"C4:F{row-1}")

    ws.column_dimensions["A"].width = 25
    ws.column_dimensions["B"].width = 45
    for col in range(3, 9):
        ws.column_dimensions[get_column_letter(col)].width = 15


def create_response_timeframes_sheet(ws, styles):
    ws.merge_cells("A1:H1")
    ws["A1"] = "Response Timeframe Compliance"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]

    headers = ["Response Type", "SLA", "Documented", "Measured", "Compliance Rate",
               "Verification Method", "Last Reviewed", "Notes"]
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.border = styles["column_header"]["border"]

    row = 4
    for response_type, sla in RESPONSE_TIMEFRAMES:
        ws.cell(row=row, column=1, value=response_type).border = styles["border"]
        ws.cell(row=row, column=2, value=sla).border = styles["border"]
        for col in range(3, 9):
            cell = ws.cell(row=row, column=col, value="")
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
        row += 1

    yn_dv = DataValidation(type="list", formula1='"Yes,No"', allow_blank=True)
    ws.add_data_validation(yn_dv)
    yn_dv.add(f"C4:D{row-1}")

    ws.column_dimensions["A"].width = 22
    ws.column_dimensions["B"].width = 25
    for col in range(3, 9):
        ws.column_dimensions[get_column_letter(col)].width = 16


def create_nonblame_culture_sheet(ws, styles):
    ws.merge_cells("A1:H1")
    ws["A1"] = "Non-Blame Culture Assessment"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]

    headers = ["Principle", "Description", "Documented", "Communicated", "Training",
               "Effectiveness Measure", "Evidence", "Notes"]
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.border = styles["column_header"]["border"]

    row = 4
    for principle, description in NON_BLAME_PRINCIPLES:
        ws.cell(row=row, column=1, value=principle).border = styles["border"]
        ws.cell(row=row, column=2, value=description).border = styles["border"]
        for col in range(3, 9):
            cell = ws.cell(row=row, column=col, value="")
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
        row += 1

    # Metrics section
    row += 2
    ws[f"A{row}"] = "Culture Effectiveness Metrics"
    ws[f"A{row}"].font = Font(bold=True, size=11)

    row += 1
    metrics = [("Reporting Volume Trend", ""), ("Time-to-Report Average", ""),
               ("Anonymous vs Identified Ratio", ""), ("Personnel Survey Score", ""),
               ("Repeat Reporter Rate", "")]
    for metric, value in metrics:
        ws[f"A{row}"] = metric
        ws[f"A{row}"].border = styles["border"]
        cell = ws[f"B{row}"]
        cell.fill = styles["input_cell"]["fill"]
        cell.border = styles["border"]
        row += 1

    ws.column_dimensions["A"].width = 25
    ws.column_dimensions["B"].width = 45
    for col in range(3, 9):
        ws.column_dimensions[get_column_letter(col)].width = 16


def create_awareness_training_sheet(ws, styles):
    ws.merge_cells("A1:G1")
    ws["A1"] = "Event Reporting Awareness & Training"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]

    headers = ["Training Element", "Included in Training", "Last Updated", "Completion Rate",
               "Effectiveness Measured", "Evidence", "Notes"]
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.border = styles["column_header"]["border"]

    elements = ["Reporting channels overview", "What to report (event categories)",
                "How to report (procedures)", "Response expectations", "Non-blame culture",
                "Evidence preservation", "Remote work specific scenarios"]
    row = 4
    for element in elements:
        ws.cell(row=row, column=1, value=element).border = styles["border"]
        for col in range(2, 8):
            cell = ws.cell(row=row, column=col, value="")
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
        row += 1

    ws.column_dimensions["A"].width = 35
    for col in range(2, 8):
        ws.column_dimensions[get_column_letter(col)].width = 18


def create_sample_events_sheet(ws, styles):
    ws.merge_cells("A1:I1")
    ws["A1"] = "Sample Event Reports (Last 12 Months)"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]

    headers = ["Event ID", "Date Reported", "Category", "Channel Used", "Acknowledged",
               "Ack Time", "Resolution Time", "Escalated", "Notes"]
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.border = styles["column_header"]["border"]

    for data_row in range(4, 19):
        ws.cell(row=data_row, column=1, value=f"EVT-{data_row-3:04d}").border = styles["border"]
        for col in range(2, 10):
            cell = ws.cell(row=data_row, column=col, value="")
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]

    for col in range(1, 10):
        ws.column_dimensions[get_column_letter(col)].width = 15


def create_gap_analysis_sheet(ws, styles):
    ws.merge_cells("A1:I1")
    ws["A1"] = "Event Reporting Gap Analysis"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]

    headers = ["Gap ID", "Area", "Description", "Impact", "Risk", "Remediation", "Owner", "Target", "Status"]
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.border = styles["column_header"]["border"]

    for data_row in range(4, 19):
        ws.cell(row=data_row, column=1, value=f"GAP-ER-{data_row-3:03d}").border = styles["border"]
        for col in range(2, 10):
            cell = ws.cell(row=data_row, column=col, value="")
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]

    area_dv = DataValidation(type="list", formula1='"Channels,Categories,Response,Culture,Training"', allow_blank=True)
    ws.add_data_validation(area_dv)
    area_dv.add("B4:B18")

    risk_dv = DataValidation(type="list", formula1='"Critical,High,Medium,Low"', allow_blank=True)
    ws.add_data_validation(risk_dv)
    risk_dv.add("E4:E18")

    status_dv = DataValidation(type="list", formula1='"Open,In Progress,Resolved,Accepted"', allow_blank=True)
    ws.add_data_validation(status_dv)
    status_dv.add("I4:I18")

    for col in range(1, 10):
        ws.column_dimensions[get_column_letter(col)].width = 15


def create_evidence_register_sheet(ws, styles):
    ws.merge_cells("A1:H1")
    ws["A1"] = "Evidence Register"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]

    headers = ["Evidence ID", "Type", "Description", "Source", "Date", "Retention", "Location", "Status"]
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.border = styles["column_header"]["border"]

    evidence = [("EVD-ER-001", "Channel Documentation", "Reporting channel procedures", "Intranet"),
                ("EVD-ER-002", "Availability Tests", "Channel availability test records", "IT Ops"),
                ("EVD-ER-003", "Training Materials", "Event reporting training content", "LMS"),
                ("EVD-ER-004", "Response Metrics", "SLA compliance dashboards", "Ticketing"),
                ("EVD-ER-005", "Sample Reports", "Sample event reports with responses", "SIEM"),
                ("EVD-ER-006", "Survey Results", "Non-blame culture survey results", "HR")]
    row = 4
    for evd_id, evd_type, desc, source in evidence:
        ws.cell(row=row, column=1, value=evd_id).border = styles["border"]
        ws.cell(row=row, column=2, value=evd_type).border = styles["border"]
        ws.cell(row=row, column=3, value=desc).border = styles["border"]
        ws.cell(row=row, column=4, value=source).border = styles["border"]
        for col in range(5, 9):
            cell = ws.cell(row=row, column=col, value="")
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
        row += 1

    for col in range(1, 9):
        ws.column_dimensions[get_column_letter(col)].width = 18


def create_dashboard_sheet(ws, styles):
    ws.merge_cells("A1:D1")
    ws["A1"] = "Event Reporting Dashboard"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]

    metrics = [("Channels Fully Operational", ""), ("24/7 Channel Available", ""),
               ("Event Categories Documented", ""), ("Acknowledgment SLA Compliance", ""),
               ("Non-Blame Culture Survey Score", ""), ("Training Completion Rate", ""),
               ("Events Reported (Last 12 mo)", ""), ("Open Gaps", "")]
    row = 4
    for metric, value in metrics:
        ws[f"A{row}"] = metric
        ws[f"A{row}"].font = Font(bold=True)
        ws[f"A{row}"].border = styles["border"]
        cell = ws[f"B{row}"]
        cell.fill = styles["input_cell"]["fill"]
        cell.border = styles["border"]
        row += 1

    ws.column_dimensions["A"].width = 35
    ws.column_dimensions["B"].width = 20


def create_approval_sheet(ws, styles):
    ws.merge_cells("A1:E1")
    ws["A1"] = "Assessment Approval and Sign-Off"
    ws["A1"].font = styles["header"]["font"]
    ws["A1"].fill = styles["header"]["fill"]
    ws["A1"].alignment = styles["header"]["alignment"]

    headers = ["Role", "Name", "Signature", "Date", "Comments"]
    row = 3
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.font = styles["column_header"]["font"]
        cell.fill = styles["column_header"]["fill"]
        cell.border = styles["column_header"]["border"]

    approvers = ["IT Security Manager", "Service Desk Manager", "HR Manager", "CISO"]
    row = 4
    for approver in approvers:
        ws.cell(row=row, column=1, value=approver).border = styles["border"]
        for col in range(2, 6):
            cell = ws.cell(row=row, column=col, value="")
            cell.fill = styles["input_cell"]["fill"]
            cell.border = styles["border"]
        row += 1

    ws.column_dimensions["A"].width = 25
    ws.column_dimensions["B"].width = 25
    ws.column_dimensions["C"].width = 25
    ws.column_dimensions["D"].width = 15
    ws.column_dimensions["E"].width = 40


def main():
    logger.info(f"Starting generation of {DOCUMENT_ID} - {WORKBOOK_NAME}")
    logger.info(f"Output file: {OUTPUT_FILENAME}")

    try:
        styles = setup_styles()
        wb = create_workbook()

        logger.info("Creating sheets...")
        create_instructions_sheet(wb["Instructions"], styles)
        create_channel_assessment_sheet(wb["Channel_Assessment"], styles)
        create_channel_availability_sheet(wb["Channel_Availability"], styles)
        create_event_categories_sheet(wb["Event_Categories"], styles)
        create_response_timeframes_sheet(wb["Response_Timeframes"], styles)
        create_nonblame_culture_sheet(wb["NonBlame_Culture"], styles)
        create_awareness_training_sheet(wb["Awareness_Training"], styles)
        create_sample_events_sheet(wb["Sample_Events"], styles)
        create_gap_analysis_sheet(wb["Gap_Analysis"], styles)
        create_evidence_register_sheet(wb["Evidence_Register"], styles)
        create_dashboard_sheet(wb["Dashboard"], styles)
        create_approval_sheet(wb["Approval_Sign_Off"], styles)

        wb.save(OUTPUT_FILENAME)
        logger.info(f"Workbook saved successfully: {OUTPUT_FILENAME}")

    except Exception as e:
        logger.error(f"Error generating workbook: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

# =============================================================================
# QA_VERIFIED: 2026-01-31
# QA_STATUS: PASSED - STANDARDIZATION COMPLETE (Phase 1-3)
# QA_TOOL: Claude Code Standardization
# CHANGES: Initial creation, constants, metadata headers, v1.0 versioning, logger output
# =============================================================================
