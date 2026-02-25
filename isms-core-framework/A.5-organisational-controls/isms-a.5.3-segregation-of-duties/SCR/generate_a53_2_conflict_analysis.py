#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
# =============================================================================
"""
================================================================================
ISMS-IMP-A.5.3.2 - Conflict Analysis
================================================================================

ISO/IEC 27001:2022 Control A.5.3: Segregation of Duties
Assessment Workbook 2 of 4: Conflict Analysis

This script generates an Excel workbook for detailed analysis of segregation
of duties conflicts including impact assessment, exploitation scenarios,
and control mapping.
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
DOCUMENT_ID = "ISMS-IMP-A.5.3.2"
WORKBOOK_NAME = "Conflict Analysis"
CONTROL_ID = "A.5.3"
CONTROL_NAME = "Segregation of Duties"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

# Timestamps
GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")

# Output filename
OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME.replace(' ', '_')}_{GENERATED_TIMESTAMP}.xlsx"

# =============================================================================
# STYLING CONSTANTS
# =============================================================================
HEADER_FONT = Font(bold=True, size=11, color="FFFFFF")
HEADER_FILL = PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid")
HEADER_ALIGNMENT = Alignment(horizontal="center", vertical="center", wrap_text=True)

TITLE_FONT = Font(bold=True, size=14, color="FFFFFF")
TITLE_FILL = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")

INPUT_FILL = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")

# Impact level colors
CRITICAL_FILL = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
HIGH_FILL = PatternFill(start_color="FABF8F", end_color="FABF8F", fill_type="solid")
MEDIUM_FILL = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
LOW_FILL = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")

THIN_BORDER = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

# =============================================================================
# DATA CONSTANTS
# =============================================================================
CONFLICT_CATEGORIES = [
    "Maker-Checker",
    "Requestor-Approver",
    "Developer-Deployer",
    "Administrator-Auditor",
    "Creator-Reconciler",
    "Custodian-Owner",
    "Other"
]

CONFLICT_TYPES = ["X", "C", "M"]

IMPACT_LEVELS = ["1", "2", "3", "4", "5"]

RISK_LEVELS = ["Critical", "High", "Medium", "Low"]

ANALYSIS_STATUSES = ["Pending", "In Progress", "Complete"]

THREAT_ACTORS = [
    "Insider-Malicious",
    "Insider-Negligent",
    "External-Attacker",
    "Colluding-Parties"
]

DETECTION_DIFFICULTY = ["Very High", "High", "Medium", "Low", "Very Low"]

CONTROL_TYPES = ["Preventive", "Detective", "Corrective", "Compensating"]

CONTROL_EFFECTIVENESS = ["High", "Medium", "Low"]

IMPLEMENTATION_STATUS = ["Implemented", "Partial", "Planned", "Not Implemented"]

PRIORITY_LEVELS = ["Critical", "High", "Medium", "Low"]

EVIDENCE_TYPES = [
    "Analysis Document",
    "System Export",
    "Interview Notes",
    "Historical Incident",
    "Control Evidence"
]


# =============================================================================
# WORKBOOK GENERATION FUNCTIONS
# =============================================================================

def apply_header_style(cell):
    """Apply standard header styling to a cell."""
    cell.font = HEADER_FONT
    cell.fill = HEADER_FILL
    cell.alignment = HEADER_ALIGNMENT
    cell.border = THIN_BORDER


def apply_input_style(cell):
    """Apply input cell styling."""
    cell.fill = INPUT_FILL
    cell.border = THIN_BORDER


def create_instructions_sheet(ws):
    """Create the Instructions sheet."""
    ws.title = "Instructions"

    instructions = [
        [f"{DOCUMENT_ID} - {WORKBOOK_NAME}"],
        [""],
        ["PURPOSE"],
        ["This workbook provides detailed analysis of segregation of duties conflicts."],
        ["It examines WHY conflicts are problematic and HOW they create risk."],
        [""],
        ["SHEETS"],
        ["1. Instructions - This guidance sheet"],
        ["2. Conflict_Register - Master list of all conflicts from A.5.3.1"],
        ["3. Impact_Assessment - Detailed impact scoring"],
        ["4. Exploitation_Scenarios - How conflicts could be exploited"],
        ["5. Control_Mapping - Controls mitigating each conflict"],
        ["6. Trend_Analysis - Historical conflict patterns"],
        ["7. Prioritisation_Matrix - Risk-based ranking"],
        ["8. Evidence_Register - Supporting documentation"],
        [""],
        ["IMPACT SCORING (1-5)"],
        ["1 = Minimal impact (e.g., <CHF 10K loss, minor disruption)"],
        ["2 = Low impact (e.g., CHF 10-50K loss, limited disruption)"],
        ["3 = Moderate impact (e.g., CHF 50-250K loss, significant disruption)"],
        ["4 = High impact (e.g., CHF 250K-1M loss, major disruption)"],
        ["5 = Critical impact (e.g., >CHF 1M loss, severe/existential impact)"],
        [""],
        ["PRIORITY CALCULATION"],
        ["Priority Score = Impact x Likelihood x (1 - Control Effectiveness)"],
        ["Critical: 15-25 | High: 10-14 | Medium: 5-9 | Low: 1-4"],
        [""],
        [f"Generated: {GENERATED_DATE}"],
        [f"Control Reference: {CONTROL_REF}"],
    ]

    for row_num, row_data in enumerate(instructions, 1):
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row_num, column=col_num, value=value)
            if row_num == 1:
                cell.font = TITLE_FONT
                cell.fill = TITLE_FILL
            elif value in ["PURPOSE", "SHEETS", "IMPACT SCORING (1-5)", "PRIORITY CALCULATION"]:
                cell.font = Font(bold=True, size=11)

    ws.column_dimensions['A'].width = 80


def create_conflict_register_sheet(ws):
    """Create the Conflict Register sheet."""
    ws.title = "Conflict_Register"

    headers = [
        "Conflict_ID", "Gap_ID", "Conflict_Category", "Role_A", "Role_B",
        "Process", "Conflict_Type", "Persons_Affected", "Analysis_Status"
    ]

    widths = [15, 15, 20, 25, 25, 25, 12, 15, 15]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        apply_header_style(cell)
        ws.column_dimensions[get_column_letter(col)].width = widths[col - 1]

    # Data validations
    category_dv = DataValidation(type="list", formula1=f'"{",".join(CONFLICT_CATEGORIES)}"')
    ws.add_data_validation(category_dv)
    category_dv.add('C2:C200')

    type_dv = DataValidation(type="list", formula1=f'"{",".join(CONFLICT_TYPES)}"')
    ws.add_data_validation(type_dv)
    type_dv.add('G2:G200')

    status_dv = DataValidation(type="list", formula1=f'"{",".join(ANALYSIS_STATUSES)}"')
    ws.add_data_validation(status_dv)
    status_dv.add('I2:I200')

    # Format input rows
    for row in range(2, 51):
        for col in range(1, len(headers) + 1):
            apply_input_style(ws.cell(row=row, column=col))

    # Sample data
    sample_conflicts = [
        ("CON-2026-001", "GAP-2026-001", "Maker-Checker", "AP Clerk", "Treasurer",
         "Accounts Payable", "X", 2, "Complete"),
        ("CON-2026-002", "GAP-2026-002", "Developer-Deployer", "Developer", "Release Manager",
         "Software Development", "X", 1, "In Progress"),
    ]

    for row_idx, conflict in enumerate(sample_conflicts, 2):
        for col_idx, value in enumerate(conflict, 1):
            ws.cell(row=row_idx, column=col_idx, value=value)


def create_impact_assessment_sheet(ws):
    """Create the Impact Assessment sheet."""
    ws.title = "Impact_Assessment"

    headers = [
        "Conflict_ID", "Financial_Impact", "Operational_Impact", "Reputational_Impact",
        "Compliance_Impact", "Data_Impact", "Overall_Impact", "Justification",
        "Assessor", "Assessment_Date"
    ]

    widths = [15, 15, 18, 18, 18, 15, 15, 50, 20, 15]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        apply_header_style(cell)
        ws.column_dimensions[get_column_letter(col)].width = widths[col - 1]

    # Data validations for impact levels
    impact_dv = DataValidation(type="list", formula1=f'"{",".join(IMPACT_LEVELS)}"')
    ws.add_data_validation(impact_dv)
    impact_dv.add('B2:F200')

    # Format input rows and add formulas
    for row in range(2, 51):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            if col == 7:  # Overall_Impact formula
                cell.value = f"=MAX(B{row}:F{row})"
                cell.fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
            else:
                apply_input_style(cell)
            cell.border = THIN_BORDER


def create_exploitation_scenarios_sheet(ws):
    """Create the Exploitation Scenarios sheet."""
    ws.title = "Exploitation_Scenarios"

    headers = [
        "Scenario_ID", "Conflict_ID", "Scenario_Name", "Threat_Actor",
        "Motivation", "Method", "Detection_Difficulty", "Historical_Precedent", "Reference"
    ]

    widths = [15, 15, 30, 20, 25, 60, 18, 15, 40]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        apply_header_style(cell)
        ws.column_dimensions[get_column_letter(col)].width = widths[col - 1]

    # Data validations
    actor_dv = DataValidation(type="list", formula1=f'"{",".join(THREAT_ACTORS)}"')
    ws.add_data_validation(actor_dv)
    actor_dv.add('D2:D200')

    detection_dv = DataValidation(type="list", formula1=f'"{",".join(DETECTION_DIFFICULTY)}"')
    ws.add_data_validation(detection_dv)
    detection_dv.add('G2:G200')

    precedent_dv = DataValidation(type="list", formula1='"Yes,No,Unknown"')
    ws.add_data_validation(precedent_dv)
    precedent_dv.add('H2:H200')

    # Format input rows
    for row in range(2, 51):
        for col in range(1, len(headers) + 1):
            apply_input_style(ws.cell(row=row, column=col))

    # Sample scenario
    ws.cell(row=2, column=1, value="SCN-2026-001")
    ws.cell(row=2, column=2, value="CON-2026-001")
    ws.cell(row=2, column=3, value="Fictitious Vendor Fraud")
    ws.cell(row=2, column=4, value="Insider-Malicious")
    ws.cell(row=2, column=5, value="Financial gain")
    ws.cell(row=2, column=6, value="Create fake vendor, submit invoices, approve own payments")
    ws.cell(row=2, column=7, value="High")
    ws.cell(row=2, column=8, value="Yes")


def create_control_mapping_sheet(ws):
    """Create the Control Mapping sheet."""
    ws.title = "Control_Mapping"

    headers = [
        "Mapping_ID", "Conflict_ID", "Control_ID", "Control_Name",
        "Control_Type", "Effectiveness", "Implementation_Status", "Gap_Notes"
    ]

    widths = [15, 15, 15, 35, 15, 12, 18, 50]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        apply_header_style(cell)
        ws.column_dimensions[get_column_letter(col)].width = widths[col - 1]

    # Data validations
    type_dv = DataValidation(type="list", formula1=f'"{",".join(CONTROL_TYPES)}"')
    ws.add_data_validation(type_dv)
    type_dv.add('E2:E200')

    eff_dv = DataValidation(type="list", formula1=f'"{",".join(CONTROL_EFFECTIVENESS)}"')
    ws.add_data_validation(eff_dv)
    eff_dv.add('F2:F200')

    status_dv = DataValidation(type="list", formula1=f'"{",".join(IMPLEMENTATION_STATUS)}"')
    ws.add_data_validation(status_dv)
    status_dv.add('G2:G200')

    # Format input rows
    for row in range(2, 51):
        for col in range(1, len(headers) + 1):
            apply_input_style(ws.cell(row=row, column=col))


def create_trend_analysis_sheet(ws):
    """Create the Trend Analysis sheet."""
    ws.title = "Trend_Analysis"

    headers = [
        "Period", "Total_Conflicts", "Critical_Conflicts", "High_Conflicts",
        "Resolved_Count", "New_Conflicts", "Resolution_Rate", "Trend_Notes"
    ]

    widths = [12, 15, 18, 15, 15, 15, 15, 50]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        apply_header_style(cell)
        ws.column_dimensions[get_column_letter(col)].width = widths[col - 1]

    # Format input rows and add formulas
    for row in range(2, 21):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            if col == 7:  # Resolution_Rate formula
                cell.value = f"=IF(B{row}>0,E{row}/B{row}*100,0)"
                cell.fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
            else:
                apply_input_style(cell)
            cell.border = THIN_BORDER

    # Sample periods
    periods = ["2025-Q1", "2025-Q2", "2025-Q3", "2025-Q4", "2026-Q1"]
    for idx, period in enumerate(periods, 2):
        ws.cell(row=idx, column=1, value=period)


def create_prioritisation_matrix_sheet(ws):
    """Create the Prioritisation Matrix sheet."""
    ws.title = "Prioritisation_Matrix"

    headers = [
        "Conflict_ID", "Impact_Score", "Likelihood_Score", "Control_Effectiveness",
        "Priority_Score", "Priority_Level", "Action_Timeline", "Assigned_To"
    ]

    widths = [15, 12, 15, 20, 15, 15, 25, 25]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        apply_header_style(cell)
        ws.column_dimensions[get_column_letter(col)].width = widths[col - 1]

    # Data validations
    likelihood_dv = DataValidation(type="list", formula1=f'"{",".join(IMPACT_LEVELS)}"')
    ws.add_data_validation(likelihood_dv)
    likelihood_dv.add('C2:C200')

    # Format input rows and add formulas
    for row in range(2, 51):
        for col in range(1, len(headers) + 1):
            cell = ws.cell(row=row, column=col)
            if col == 5:  # Priority_Score formula
                cell.value = f"=IF(AND(B{row}<>\"\",C{row}<>\"\"),B{row}*C{row}*(1-D{row}),\"\")"
                cell.fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
            elif col == 6:  # Priority_Level formula
                cell.value = f'=IF(E{row}="","",IF(E{row}>=15,"Critical",IF(E{row}>=10,"High",IF(E{row}>=5,"Medium","Low"))))'
                cell.fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
            elif col == 7:  # Action_Timeline formula
                cell.value = f'=IF(F{row}="","",IF(F{row}="Critical","Immediate (<7 days)",IF(F{row}="High","Short-term (<30 days)",IF(F{row}="Medium","Medium-term (<90 days)","Long-term (<180 days)"))))'
                cell.fill = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
            else:
                apply_input_style(cell)
            cell.border = THIN_BORDER


def create_evidence_register_sheet(ws):
    """Create the Evidence Register sheet."""
    ws.title = "Evidence_Register"

    headers = [
        "Evidence_ID", "Conflict_ID", "Evidence_Type", "Description",
        "Location", "Date_Collected", "Collected_By"
    ]

    widths = [15, 15, 20, 40, 50, 15, 25]

    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        apply_header_style(cell)
        ws.column_dimensions[get_column_letter(col)].width = widths[col - 1]

    # Data validations
    type_dv = DataValidation(type="list", formula1=f'"{",".join(EVIDENCE_TYPES)}"')
    ws.add_data_validation(type_dv)
    type_dv.add('C2:C200')

    # Format input rows
    for row in range(2, 51):
        for col in range(1, len(headers) + 1):
            apply_input_style(ws.cell(row=row, column=col))


def generate_workbook():
    """Generate the complete assessment workbook."""
    logger.info(f"Generating {DOCUMENT_ID} - {WORKBOOK_NAME}")

    wb = Workbook()

    # Remove default sheet
    default_sheet = wb.active

    # Create all sheets
    create_instructions_sheet(wb.create_sheet())
    create_conflict_register_sheet(wb.create_sheet())
    create_impact_assessment_sheet(wb.create_sheet())
    create_exploitation_scenarios_sheet(wb.create_sheet())
    create_control_mapping_sheet(wb.create_sheet())
    create_trend_analysis_sheet(wb.create_sheet())
    create_prioritisation_matrix_sheet(wb.create_sheet())
    create_evidence_register_sheet(wb.create_sheet())

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
# QA_VERIFIED: 2026-02-03
# QA_STATUS: PASSED - INITIAL CREATION
# QA_TOOL: Claude Code
# CHANGES: Initial creation for A.5.3 Segregation of Duties control
# =============================================================================
