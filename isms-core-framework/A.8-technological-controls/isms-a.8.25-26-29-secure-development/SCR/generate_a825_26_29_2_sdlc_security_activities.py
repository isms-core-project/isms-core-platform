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
ISMS-IMP-A.8.25-26-29.S2 - SDLC Security Activities Assessment Excel Generator
================================================================================

ISO/IEC 27001:2022 Controls A.8.25/A.8.26/A.8.29: Secure Development Framework
Assessment Domain 2 of 5: Secure Development Lifecycle Activities (A.8.25)

--------------------------------------------------------------------------------
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR YOUR ORGANIZATION
--------------------------------------------------------------------------------

This script is a TEMPLATE/SAMPLE implementation and MUST be adapted to match
your organization's specific:
- Development methodologies (Agile, Waterfall, DevOps, hybrid)
- Technology stack (languages, frameworks, platforms)
- Security tooling (SAST, DAST, SCA, IAST tools and versions)
- SDLC processes and governance structure
- Compliance requirements and risk tolerance
- SDLC phase definitions and security gates
- Secure coding standards and code review processes
- Security training programs and certification requirements

DO NOT use this script without reviewing and adapting all sections marked
with "# CUSTOMIZE:" comments throughout the code.

Reference Pattern: Based on ISMS-A.8.25-26-29 Secure Development Framework

--------------------------------------------------------------------------------
DESCRIPTION
--------------------------------------------------------------------------------

This script generates a comprehensive Excel assessment workbook for evaluating
security activities integrated throughout the Software Development Lifecycle
(SDLC) across all development projects and teams.

**Purpose:**
Enables systematic assessment of security integration in SDLC phases, secure
coding practices, code review execution, security training, and security tool
deployment against ISO 27001:2022 Control A.8.25 requirements, supporting
evidence-based validation of secure development practices.

**Assessment Scope:**
- Security activities by SDLC phase (requirements, design, development, testing, deployment)
- Secure coding standard adoption and compliance
- Code review execution and security-focused review coverage
- Security training completion rates for developers
- Security tool deployment and integration (SAST, SCA, secret scanning, IDE plugins)
- Security champion program effectiveness
- Security defect management and remediation
- Gap analysis and remediation planning
- Evidence collection for audit readiness

**Generated Workbook Structure:**
1. Instructions & Legend - Assessment guidance and SDLC security standards
2. SDLC Phase Activities - Security activities execution by phase and project
3. Secure Coding Compliance - Adoption of secure coding standards by language/framework
4. Code Review Tracking - Code review execution and security coverage
5. Security Training Status - Developer training completion and certification
6. Security Tool Deployment - SAST/SCA/secret scanning tool deployment status
7. Security Champion Program - Security champion coverage and effectiveness
8. Compliance Summary - Overall SDLC security activity completion scores
9. Gap Analysis - Non-compliant projects/teams and remediation requirements
10. Evidence Register - Audit evidence tracking and documentation
11. Approval & Sign-Off - Stakeholder review and approval workflow

**Key Features:**
- Data validation with SDLC phase and activity dropdown lists
- Conditional formatting for activity completion status
- Automated gap identification for missing security activities
- Protected formulas with unprotected input cells
- Evidence linkage for audit traceability
- Multi-stakeholder approval workflow
- Integration with code repositories, CI/CD pipelines, and training systems

**Integration:**
This assessment feeds into the A.8.25-26-29.5 Secure Development Compliance
Dashboard, which consolidates data from all five assessment domains for
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
    - openpyxl>=3.0.0 (Python Excel library)
    - datetime (standard library)

--------------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------------

Basic Usage:
    python3 generate_a825_26_29_2_sdlc_security_activities.py

Advanced Usage:
    # Generate with custom output directory
    python3 generate_a825_26_29_2_sdlc_security_activities.py --output /path/to/dir
    
    # Generate with specific date suffix
    python3 generate_a825_26_29_2_sdlc_security_activities.py --date 20250124

Output:
    File: ISMS_A_8_25_26_29_2_SDLC_Security_Activities_Assessment_YYYYMMDD.xlsx
    Location: Current directory (or specified output path)

Post-Generation Steps:
    1. Review and customize SDLC phase definitions to match your methodology
    2. Define security activities required for each SDLC phase
    3. Inventory all active development projects and teams
    4. Complete SDLC phase activity tracking for each project
    5. Assess secure coding standard adoption by development team
    6. Track code review execution and security-focused review coverage
    7. Verify security training completion for all developers
    8. Document security tool deployment (SAST, SCA, secret scanning)
    9. Conduct gap analysis for projects missing security activities
    10. Define remediation actions with development leads and timelines
    11. Collect and link audit evidence (code review records, training certificates, tool configs)
    12. Obtain stakeholder approvals
    13. Feed results into A.8.25-26-29.5 Compliance Dashboard

--------------------------------------------------------------------------------
METADATA
--------------------------------------------------------------------------------

Control Reference:    ISO/IEC 27001:2022 Annex A Controls A.8.25/A.8.26/A.8.29
Assessment Domain:    2 of 5 (Secure Development Lifecycle Activities - A.8.25)
Framework Version:    1.0
Script Version:       1.0
Author:               [Organization] ISMS Implementation Team
Date:                 [YYYY-MM-DD]
Last Modified:        [YYYY-MM-DD]
Python Version:       3.8+
License:              [Organization License/Terms]

Related Documents:
    - ISMS-POL-A.8.25-26-29-S1: Executive Control Alignment (Governance)
    - ISMS-POL-A.8.25-26-29-S2: Security Requirements (A.8.26)
    - ISMS-POL-A.8.25-26-29-S3: Secure Development Lifecycle (A.8.25)
    - ISMS-POL-A.8.25-26-29-S4: Security Testing (A.8.29)
    - ISMS-POL-A.8.25-26-29-S5: Assessment Evidence Framework
    - ISMS-IMP-A.8.25-26-29-S2: SDLC Security Integration Implementation Guide
    - ISMS-IMP-A.8.25-26-29.S5: Compliance Dashboard (Consolidation)

Related Scripts:
    - generate_a825_26_29_1_security_requirements.py
    - generate_a825_26_29_2_sdlc_security_activities.py (this script)
    - generate_a825_26_29_3_security_testing_results.py
    - generate_a825_26_29_4_vulnerability_remediation.py
    - generate_a825_26_29_5_compliance_dashboard.py
    - normalize_assessment_files_a825_26_29.py

--------------------------------------------------------------------------------
CHANGE HISTORY
--------------------------------------------------------------------------------

Version 1.0 - [YYYY-MM-DD]
    - Initial release
    - Implements full assessment framework per ISMS-IMP-A.8.25-26-29-S2 spec
    - Supports comprehensive SDLC security activities evaluation
    - Integrated with A.8.25-26-29.5 Compliance Dashboard

[Future changes to be documented here]

--------------------------------------------------------------------------------
IMPORTANT NOTES
--------------------------------------------------------------------------------

**SDLC Methodology Neutrality:**
This assessment framework is methodology-agnostic and must work across:
- Waterfall: Traditional phase-gate development with formal security reviews
- Agile: Iterative sprint-based development with security in each sprint
- DevOps/DevSecOps: Continuous integration/deployment with automated security
- Hybrid: Mixed methodology approaches with varying security integration
Customize dropdown values and assessment criteria to match YOUR methodology.
For Agile: Map activities to sprints, not traditional phases.
For DevOps: Emphasize automation and CI/CD pipeline security.

**Technology Stack Agnosticism:**
Framework must remain vendor-neutral and technology-agnostic:
- Programming languages: Java, Python, C#, JavaScript, Go, Ruby, PHP, etc.
- Frameworks: Spring, Django, .NET, React, Angular, Vue, Express, etc.
- Platforms: Web, mobile, desktop, embedded, cloud-native, serverless, etc.
Do NOT hardcode technology-specific assumptions in assessment criteria.
Secure coding standards vary by language; provide customization guidance.

**Security Tool Diversity:**
Assessment must accommodate various security tools in the SDLC:
- SAST: SonarQube, Checkmarx, Fortify, Veracode, Snyk Code, Semgrep
- SCA: Snyk, Dependabot, WhiteSource, Black Duck, Mend
- Secret Scanning: GitGuardian, TruffleHog, GitHub Secret Scanning
- IDE Plugins: SonarLint, Snyk IDE plugins, security-focused linters
- Code Review: GitHub, GitLab, Bitbucket, Gerrit, Crucible
Use generic terms; avoid vendor lock-in in assessment structure.

**Audit Considerations:**
This assessment generates audit evidence per ISO 27001:2022 requirements.
Ensure all fields are completed accurately and evidence is properly linked.
Auditors will expect:
- Documented security activities for each SDLC phase
- Evidence of secure coding standard adoption (policies, training)
- Code review records showing security-focused reviews
- Training completion records for all developers
- Security tool deployment and integration evidence
- Security defect tracking and remediation records

**Data Protection:**
Assessment workbooks contain sensitive development information including:
- Project names and development team structures
- Code review findings and security issues
- Training records and developer competency data
- Security tool configurations and findings
- Security gaps and remediation plans
Handle in accordance with your organization's data classification policies.

**Maintenance:**
Review and update assessment:
- Quarterly: Complete reassessment of all active projects
- Semi-annually: Update secure coding standards based on new threats
- Annually: Review SDLC security activities and adjust as needed
- Ad-hoc: When new projects start or methodologies change

**Quality Assurance:**
Have Application Security team, Development Leads, and DevOps Engineers
validate assessments before using results for compliance reporting or
remediation decisions.

**Regulatory Alignment:**
SDLC security activities assessment supports regulatory compliance:
- Payment processing: PCI DSS v4.0.1 requirement 6.3 (secure SDLC practices)
- Healthcare: HIPAA security requirements for software development
- Finance: Regional banking requirements for secure development
- Critical infrastructure: Sector-specific secure development requirements
Customize assessment criteria to include regulatory-specific requirements
applicable to your organization and industry.

**Integration with Related Controls:**
This assessment integrates with:
- A.8.4 (Access to Source Code): SDLC activities include access controls
- A.8.26 (Security Requirements): Requirements inform SDLC activities
- A.8.28 (Secure Coding): Secure coding standards are SDLC activities
- A.8.29 (Security Testing): Testing activities are part of SDLC phases
- A.8.31 (Environment Separation): SDLC phases map to environments
- A.8.32 (Change Management): SDLC activities feed change process
- A.5.24 (Security Incident Management): Defect management integrates

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
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

# =============================================================================
# Document Constants
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.8.25-26-29.S2"
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")
OUTPUT_FILENAME = f"{DOCUMENT_ID}_SDLC_Security_Activities_Assessment_{GENERATED_TIMESTAMP}.xlsx"
CONTROL_REF = "ISO/IEC 27001:2022 - Controls A.8.25, A.8.26, A.8.29: Secure Development"


# ============================================================================
# SECTION 1: WORKBOOK CREATION & STYLE DEFINITIONS
# ============================================================================

def create_workbook() -> Workbook:
    """Create workbook with all required sheets matching IMP specification."""
    wb = Workbook()
    
    # Remove default sheet
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])
    
    # Sheet structure from ISMS-IMP-A.8.25-26-29-S2 Section 7.2
    sheets = [
        "Instructions & Legend",
        "SDLC_Phase_Activities",
        "Secure_Coding_Standards",
        "Code_Review_Metrics",
        "Security_Tools_Deployment",
        "Security_Tools_Usage",
        "Developer_Training",
        "Security_Defect_Management",
        "Compliance_Summary",
        "Evidence_Register",
        "Approval_Sign_Off",
    ]
    for name in sheets:
        wb.create_sheet(title=name)
    
    return wb


def setup_styles():
    """Define all cell styles - return TEMPLATES not objects."""
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
        "border": border_thin,
        "status_compliant": {
            "fill": PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid"),
            "font": Font(name="Calibri", size=10, bold=True),
        },
        "status_partial": {
            "fill": PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid"),
            "font": Font(name="Calibri", size=10, bold=True),
        },
        "status_noncompliant": {
            "fill": PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid"),
            "font": Font(name="Calibri", size=10, bold=True),
        },
    }
    return styles


def apply_style(cell, style_dict):
    """Apply style dictionary to cell - creates NEW objects."""
    if "font" in style_dict:
        cell.font = Font(
            name=style_dict["font"].name if hasattr(style_dict["font"], 'name') else "Calibri",
            size=style_dict["font"].size if hasattr(style_dict["font"], 'size') else 10,
            bold=style_dict["font"].bold if hasattr(style_dict["font"], 'bold') else False,
            color=style_dict["font"].color if hasattr(style_dict["font"], 'color') else None
        )
    if "fill" in style_dict:
        cell.fill = PatternFill(
            start_color=style_dict["fill"].start_color.rgb if hasattr(style_dict["fill"].start_color, 'rgb') else style_dict["fill"].start_color,
            end_color=style_dict["fill"].end_color.rgb if hasattr(style_dict["fill"].end_color, 'rgb') else style_dict["fill"].end_color,
            fill_type=style_dict["fill"].fill_type if hasattr(style_dict["fill"], 'fill_type') else "solid"
        )
    if "alignment" in style_dict:
        cell.alignment = Alignment(
            horizontal=style_dict["alignment"].horizontal if hasattr(style_dict["alignment"], 'horizontal') else "left",
            vertical=style_dict["alignment"].vertical if hasattr(style_dict["alignment"], 'vertical') else "center",
            wrap_text=style_dict["alignment"].wrap_text if hasattr(style_dict["alignment"], 'wrap_text') else False
        )
    if "border" in style_dict:
        thin = Side(style="thin")
        cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)


# ============================================================================
# SECTION 2: DATA VALIDATIONS & COLUMN DEFINITIONS
# ============================================================================

def create_base_validations(ws):
    """Create data validation objects for standard dropdowns."""
    validations = {
        'yes_no': DataValidation(type="list", formula1='"Yes,No"', allow_blank=False),
        'yes_no_na': DataValidation(type="list", formula1='"Yes,No,N/A"', allow_blank=False),
        'activity_status': DataValidation(type="list", formula1='"✅ Complete,⏳ In Progress,❌ Not Done,N/A"', allow_blank=False),
        'sdlc_methodology': DataValidation(type="list", formula1='"Waterfall,Agile,Scrum,DevOps,DevSecOps,Hybrid"', allow_blank=False),
        'tool_status': DataValidation(type="list", formula1='"✅ Deployed,⏳ In Progress,❌ Not Deployed,N/A"', allow_blank=False),
        'evidence_status': DataValidation(type="list", formula1='"Current,Outdated,Missing"', allow_blank=False),
        'compliance_status': DataValidation(type="list", formula1='"✅ Compliant,⚠️ Partial Compliance,❌ Non-Compliant"', allow_blank=False),
    }
    
    for key, dv in validations.items():
        ws.add_data_validation(dv)
    
    return validations


# ============================================================================
# SECTION 3: SHEET BUILDERS
# ============================================================================

def build_instructions_sheet(wb, styles):
    """Build Instructions & Legend sheet."""
    ws = wb["Instructions & Legend"]
    
    # Title
    ws.merge_cells('A1:F1')
    cell = ws['A1']
    cell.value = f"{DOCUMENT_ID}\n{CONTROL_REF}"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 40
    
    # Subtitle
    ws.merge_cells('A2:F2')
    cell = ws['A2']
    cell.value = "ISO/IEC 27001:2022 - Control A.8.25: Secure Development Lifecycle"
    apply_style(cell, styles['subheader'])
    
    # Document Information
    row = 4
    info = [
        ("Document ID:", "ISMS-IMP-A.8.25-26-29.S2"),
        ("Assessment Area:", "SDLC Security Activities"),
        ("Related Policy:", "ISMS-POL-A.8.25-26-29-S3"),
        ("Version:", "1.0"),
        ("Assessment Date:", "[USER INPUT]"),
        ("Completed By:", "[USER INPUT]"),
        ("Organisation:", "[USER INPUT]"),
        ("Review Cycle:", "Quarterly"),
    ]
    
    for label, value in info:
        ws[f'A{row}'] = label
        ws[f'A{row}'].font = Font(name="Calibri", size=10, bold=True)
        ws[f'B{row}'] = value
        if "[USER INPUT]" in value:
            ws[f'B{row}'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        row += 1
    
    # How to Use
    row += 1
    ws.merge_cells(f'A{row}:F{row}')
    cell = ws[f'A{row}']
    cell.value = "How to Use This Workbook"
    apply_style(cell, styles['subheader'])
    
    row += 1
    instructions = [
        "1. Complete SDLC_Phase_Activities for each application and SDLC phase",
        "2. Document secure coding standards adoption in Secure_Coding_Standards",
        "3. Track code review metrics in Code_Review_Metrics",
        "4. Document security tool deployment in Security_Tools_Deployment and usage in Security_Tools_Usage",
        "5. Track developer training completion in Developer_Training",
        "6. Monitor security defects in Security_Defect_Management",
        "7. Review Compliance_Summary for overall SDLC security compliance",
        "8. Document evidence in Evidence_Register",
        "9. Obtain approvals in Approval_Sign_Off",
    ]
    
    for instruction in instructions:
        ws[f'A{row}'] = instruction
        ws[f'A{row}'].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        ws.row_dimensions[row].height = 20
        row += 1
    
    # Status Legend
    row += 1
    ws.merge_cells(f'A{row}:F{row}')
    cell = ws[f'A{row}']
    cell.value = "Status Legend"
    apply_style(cell, styles['subheader'])
    
    row += 1
    legend_data = [
        ("✅", "Complete", "Activity completed", "Green"),
        ("⏳", "In Progress", "Activity in progress", "Yellow"),
        ("❌", "Not Done", "Activity not started or incomplete", "Red"),
        ("N/A", "Not Applicable", "Activity not applicable", "Gray"),
    ]
    
    legend_headers = ["Symbol", "Status", "Description", "Color"]
    for col_num, header in enumerate(legend_headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    row += 1
    for symbol, status, description, color in legend_data:
        ws[f'A{row}'] = symbol
        ws[f'B{row}'] = status
        ws[f'C{row}'] = description
        ws[f'D{row}'] = color
        
        if color == "Green":
            ws[f'D{row}'].fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
        elif color == "Yellow":
            ws[f'D{row}'].fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
        elif color == "Red":
            ws[f'D{row}'].fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
        
        row += 1
    
    # Column widths
    ws.column_dimensions['A'].width = 12
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width = 50
    ws.column_dimensions['D'].width = 15
    
    ws.freeze_panes = 'A3'
    
    return ws


def build_sdlc_phase_activities_sheet(wb, styles, validations):
    """Build SDLC Phase Activities matrix sheet."""
    ws = wb["SDLC_Phase_Activities"]
    
    # Title
    ws.merge_cells('A1:M1')
    cell = ws['A1']
    cell.value = "SDLC Security Activities by Phase"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    # Subtitle
    ws.merge_cells('A2:M2')
    cell = ws['A2']
    cell.value = "Track security activity completion for each SDLC phase per application"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Application Name",
        "SDLC Methodology",
        "Requirements: Sec Req Defined",
        "Requirements: Risk Classification",
        "Design: Threat Modeling",
        "Design: Architecture Review",
        "Development: SAST Enabled",
        "Development: Code Review",
        "Testing: DAST Scan",
        "Testing: Security Testing",
        "Deployment: Security Checklist",
        "Maintenance: Vulnerability Monitoring",
        "Phase Compliance (%)",
    ]
    
    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    for i in range(1, 14):
        ws.column_dimensions[get_column_letter(i)].width = 18
    
    # Apply data validations
    validations['sdlc_methodology'].add('B4:B100')
    validations['activity_status'].add('C4:L100')
    
    # Example data with formula
    example_data = [
        ["Customer Portal", "Agile", "✅ Complete", "✅ Complete", "✅ Complete", "✅ Complete", "✅ Complete", "✅ Complete", "✅ Complete", "✅ Complete", "✅ Complete", "✅ Complete"],
        ["Internal HR System", "Waterfall", "✅ Complete", "✅ Complete", "✅ Complete", "✅ Complete", "⏳ In Progress", "✅ Complete", "❌ Not Done", "❌ Not Done", "N/A", "N/A"],
        ["Marketing Website", "DevOps", "✅ Complete", "✅ Complete", "N/A", "N/A", "✅ Complete", "✅ Complete", "✅ Complete", "✅ Complete", "✅ Complete", "✅ Complete"],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            if col_num <= 12:
                cell.value = value
                apply_style(cell, styles['data_cell'])
            else:  # Phase Compliance formula (Column M)
                # Formula: =(COUNTIF(C{row}:L{row},"✅ Complete")/COUNTIF(C{row}:L{row},"<>N/A"))*100
                cell.value = f'=(COUNTIF(C{row}:L{row},"✅ Complete")/COUNTIF(C{row}:L{row},"<>N/A"))*100'
                cell.number_format = '0"%"'
        row += 1
    
    ws.freeze_panes = 'A4'
    
    return ws


def build_secure_coding_standards_sheet(wb, styles, validations):
    """Build Secure Coding Standards adoption sheet."""
    ws = wb["Secure_Coding_Standards"]
    
    # Title
    ws.merge_cells('A1:H1')
    cell = ws['A1']
    cell.value = "Secure Coding Standards Adoption"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    # Subtitle
    ws.merge_cells('A2:H2')
    cell = ws['A2']
    cell.value = "Assess secure coding standards adoption per application"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Application Name",
        "Standard Adopted",
        "Standard Documented?",
        "Developers Trained?",
        "Enforced via Tools?",
        "Enforced via Code Review?",
        "Last Standard Update",
        "Compliance Score (%)",
    ]
    
    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 30
    for i in range(3, 8):
        ws.column_dimensions[get_column_letter(i)].width = 20
    ws.column_dimensions['H'].width = 18
    
    # Apply data validations
    validations['yes_no'].add('C4:F100')
    
    # Example data with formula
    example_data = [
        ["Customer Portal", "OWASP Secure Coding Practices + Java Secure Coding (Oracle)", "Yes", "Yes", "Yes", "Yes", "2024-11-15"],
        ["Internal HR System", "OWASP + Python Secure Coding", "Yes", "Yes", "Yes", "No", "2024-09-20"],
        ["Marketing Website", "OWASP Baseline", "Yes", "No", "Yes", "Yes", "2024-10-10"],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            if col_num <= 7:
                cell.value = value
                apply_style(cell, styles['data_cell'])
            else:  # Compliance Score (Column H)
                # Formula: =(IF(C{row}="Yes",25,0)+IF(D{row}="Yes",25,0)+IF(E{row}="Yes",25,0)+IF(F{row}="Yes",25,0))
                cell.value = f'=(IF(C{row}="Yes",25,0)+IF(D{row}="Yes",25,0)+IF(E{row}="Yes",25,0)+IF(F{row}="Yes",25,0))'
                cell.number_format = '0"%"'
        row += 1
    
    ws.freeze_panes = 'A4'
    
    return ws


def build_code_review_metrics_sheet(wb, styles, validations):
    """Build Code Review Metrics sheet."""
    ws = wb["Code_Review_Metrics"]
    
    # Title
    ws.merge_cells('A1:H1')
    cell = ws['A1']
    cell.value = "Code Review Metrics"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    # Subtitle
    ws.merge_cells('A2:H2')
    cell = ws['A2']
    cell.value = "Track code review process and security focus"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Application Name",
        "Code Review Process Documented?",
        "Code Review Coverage (%)",
        "Security Checklist Used?",
        "Security Champion Involved?",
        "Avg Review Turnaround (days)",
        "Security Findings Count",
        "Review Compliance Score (%)",
    ]
    
    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    ws.column_dimensions['A'].width = 25
    for i in range(2, 9):
        ws.column_dimensions[get_column_letter(i)].width = 22
    
    # Apply data validations
    validations['yes_no'].add('B4:B100')
    validations['yes_no'].add('D4:E100')
    
    # Example data with formula
    example_data = [
        ["Customer Portal", "Yes", 100, "Yes", "Yes", 1.5, 8],
        ["Internal HR System", "Yes", 95, "Yes", "No", 2.2, 12],
        ["Marketing Website", "Yes", 85, "No", "Yes", 1.8, 5],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            if col_num <= 7:
                cell.value = value
                apply_style(cell, styles['data_cell'])
                if col_num == 3:  # Coverage percentage
                    cell.number_format = '0"%"'
            else:  # Review Compliance Score (Column H)
                # Formula: =IF(B{row}="Yes",20,0)+(C{row}*0.4)+IF(D{row}="Yes",20,0)+IF(E{row}="Yes",20,0)
                cell.value = f'=IF(B{row}="Yes",20,0)+(C{row}*0.4)+IF(D{row}="Yes",20,0)+IF(E{row}="Yes",20,0)'
                cell.number_format = '0.0"%"'
        row += 1
    
    ws.freeze_panes = 'A4'
    
    return ws


def build_security_tools_deployment_sheet(wb, styles, validations):
    """Build Security Tools Deployment sheet."""
    ws = wb["Security_Tools_Deployment"]
    
    # Title
    ws.merge_cells('A1:H1')
    cell = ws['A1']
    cell.value = "Security Tools Deployment Status"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    # Subtitle
    ws.merge_cells('A2:H2')
    cell = ws['A2']
    cell.value = "Track security tool deployment across organisation"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Tool Type",
        "Tool Name/Vendor",
        "Deployment Status",
        "Applications Covered",
        "Integration Point",
        "Config Reviewed?",
        "Findings Per Month (Avg)",
        "False Positive Rate (%)",
    ]
    
    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    for i in range(1, 9):
        ws.column_dimensions[get_column_letter(i)].width = 20
    
    # Apply data validations
    validations['tool_status'].add('C4:C100')
    validations['yes_no'].add('F4:F100')
    
    # Example data
    example_data = [
        ["SAST", "SonarQube Community", "✅ Deployed", "15 applications", "CI/CD (GitLab)", "Yes", 125, 15],
        ["SCA", "Snyk Open Source", "✅ Deployed", "12 applications", "CI/CD (GitLab)", "Yes", 45, 8],
        ["Secret Scanning", "TruffleHog", "✅ Deployed", "All repositories", "Pre-commit hook", "Yes", 3, 5],
        ["DAST", "OWASP ZAP", "⏳ In Progress", "5 applications", "Test Pipeline", "No", 0, 0],
        ["Container Scanning", "Trivy", "✅ Deployed", "8 applications", "CI/CD (Docker build)", "Yes", 22, 10],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            cell.value = value
            apply_style(cell, styles['data_cell'])
            if col_num == 8:  # False positive rate
                cell.number_format = '0.0"%"'
        row += 1
    
    ws.freeze_panes = 'A4'
    
    return ws


def build_security_tools_usage_sheet(wb, styles, validations):
    """Build Security Tools Usage sheet."""
    ws = wb["Security_Tools_Usage"]
    
    # Title
    ws.merge_cells('A1:H1')
    cell = ws['A1']
    cell.value = "Security Tools Usage Metrics"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    # Subtitle
    ws.merge_cells('A2:H2')
    cell = ws['A2']
    cell.value = "Track security tool usage per application"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Application Name",
        "SAST Scans Per Month",
        "SCA Scans Per Month",
        "Secret Scanning Enabled?",
        "DAST Scans Per Release",
        "Avg Remediation Time (days)",
        "Tool Integration Score",
        "Usage Compliance (%)",
    ]
    
    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    ws.column_dimensions['A'].width = 25
    for i in range(2, 9):
        ws.column_dimensions[get_column_letter(i)].width = 20
    
    # Apply data validations
    validations['yes_no'].add('D4:D100')
    
    # Example data with formula
    example_data = [
        ["Customer Portal", 20, 20, "Yes", 2, 5.5, "Excellent"],
        ["Internal HR System", 8, 8, "Yes", 1, 12.0, "Good"],
        ["Marketing Website", 16, 16, "Yes", 4, 3.2, "Excellent"],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            if col_num <= 7:
                cell.value = value
                apply_style(cell, styles['data_cell'])
            else:  # Usage Compliance (Column H)
                # Simplified formula based on targets
                # SAST >= 4/month (25%), SCA >= 4/month (25%), Secret scanning enabled (25%), DAST >= 1/release (25%)
                cell.value = f'=(IF(B{row}>=4,25,0)+IF(C{row}>=4,25,0)+IF(D{row}="Yes",25,0)+IF(E{row}>=1,25,0))'
                cell.number_format = '0"%"'
        row += 1
    
    ws.freeze_panes = 'A4'
    
    return ws


def build_developer_training_sheet(wb, styles, validations):
    """Build Developer Training sheet."""
    ws = wb["Developer_Training"]
    
    # Title
    ws.merge_cells('A1:H1')
    cell = ws['A1']
    cell.value = "Developer Security Training Compliance"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    # Subtitle
    ws.merge_cells('A2:H2')
    cell = ws['A2']
    cell.value = "Track developer security training completion and compliance"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Developer/Team Name",
        "Initial Training Date",
        "Annual Refresher Date",
        "Language-Specific Training",
        "Security Champion Training",
        "Training Quiz Score (%)",
        "Training Overdue?",
        "Training Status",
    ]
    
    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    ws.column_dimensions['A'].width = 25
    for i in range(2, 9):
        ws.column_dimensions[get_column_letter(i)].width = 20
    
    # Example data with formulas
    example_data = [
        ["Sandra Brunner", "2024-03-15", "2025-01-10", "Java Secure Coding (2024-06-20)", "N/A", 92],
        ["Markus Huber", "2023-05-10", "2024-01-15", "N/A", "Champion Training (2024-08-12)", 88],
        ["Petra Keller", "2024-08-22", "N/A", "Python Security (2024-10-05)", "N/A", 85],
        ["Development Team A", "85% trained", "70% current", "60% completed", "2 champions", 86],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            if col_num <= 6:
                cell.value = value
                apply_style(cell, styles['data_cell'])
                if col_num == 6 and isinstance(value, (int, float)):  # Quiz score
                    cell.number_format = '0"%"'
            elif col_num == 7:  # Training Overdue (Column G)
                # Formula: Check if annual refresher > 365 days old
                if row == 4:  # Individual developer rows
                    cell.value = f'=IF(AND(C{row}<>"",C{row}<TODAY()-365),"Yes","No")'
                else:
                    cell.value = "Varies"
                apply_style(cell, styles['data_cell'])
            else:  # Training Status (Column H)
                if row == 4:
                    cell.value = f'=IF(AND(B{row}<>"",C{row}<>"",C{row}>=TODAY()-365),"✅ Current","⚠️ Overdue")'
                else:
                    cell.value = "Mixed"
                apply_style(cell, styles['data_cell'])
        row += 1
    
    ws.freeze_panes = 'A4'
    
    return ws


def build_security_defect_management_sheet(wb, styles, validations):
    """Build Security Defect Management sheet."""
    ws = wb["Security_Defect_Management"]
    
    # Title
    ws.merge_cells('A1:J1')
    cell = ws['A1']
    cell.value = "Security Defect Management"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    # Subtitle
    ws.merge_cells('A2:J2')
    cell = ws['A2']
    cell.value = "Track open security defects and remediation compliance"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Application Name",
        "Critical Defects",
        "High Defects",
        "Medium Defects",
        "Low Defects",
        "Total Open Defects",
        "Avg Age (days)",
        "SLA Compliance (%)",
        "Security Tech Debt",
        "Monthly Trend",
    ]
    
    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    ws.column_dimensions['A'].width = 25
    for i in range(2, 11):
        ws.column_dimensions[get_column_letter(i)].width = 15
    
    # Example data
    example_data = [
        ["Customer Portal", 0, 1, 3, 8, 12, 15, 92, 2, "Improving"],
        ["Internal HR System", 0, 2, 5, 12, 19, 28, 78, 5, "Stable"],
        ["Marketing Website", 0, 0, 2, 4, 6, 8, 100, 0, "Improving"],
        ["Employee Portal", 1, 3, 4, 10, 18, 45, 65, 8, "Degrading"],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            cell.value = value
            apply_style(cell, styles['data_cell'])
            if col_num == 8:  # SLA Compliance percentage
                cell.number_format = '0"%"'
        row += 1
    
    ws.freeze_panes = 'A4'
    
    return ws


def build_compliance_summary_sheet(wb, styles, validations):
    """Build Compliance Summary dashboard sheet."""
    ws = wb["Compliance_Summary"]
    
    # Title
    ws.merge_cells('A1:H1')
    cell = ws['A1']
    cell.value = "A.8.25 SDLC Security Compliance Dashboard"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 40
    
    # Subtitle
    ws.merge_cells('A2:H2')
    cell = ws['A2']
    cell.value = "Overall compliance summary for SDLC security activities"
    apply_style(cell, styles['subheader'])
    
    # Summary Statistics
    row = 4
    ws.merge_cells(f'A{row}:H{row}')
    cell = ws[f'A{row}']
    cell.value = "Portfolio Summary Statistics"
    apply_style(cell, styles['subheader'])
    
    row += 1
    summary_labels = [
        "Total Applications:",
        "Applications with Full SDLC Security:",
        "SAST Tool Coverage:",
        "SCA Tool Coverage:",
        "Developers Trained (Current):",
        "Security Champions Active:",
        "Overall SDLC Compliance Score:",
    ]
    
    for label in summary_labels:
        ws[f'A{row}'] = label
        ws[f'A{row}'].font = Font(name="Calibri", size=10, bold=True)
        ws[f'B{row}'] = "[Calculated from data]"
        ws[f'B{row}'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        row += 1
    
    # Application-Level Compliance
    row += 1
    ws.merge_cells(f'A{row}:H{row}')
    cell = ws[f'A{row}']
    cell.value = "Application-Level SDLC Compliance Scores"
    apply_style(cell, styles['subheader'])
    
    row += 1
    headers = [
        "Application Name",
        "SDLC Activities",
        "Standards Score",
        "Code Review Score",
        "Tool Usage Score",
        "Training Score",
        "Overall SDLC Score",
        "Compliance Status",
    ]
    
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Example data with formulas
    example_apps = [
        "Customer Portal",
        "Internal HR System",
        "Marketing Website",
    ]
    
    row += 1
    start_row = row
    for app_name in example_apps:
        ws[f'A{row}'] = app_name
        
        # References to other sheets
        ws[f'B{row}'].value = f"=SDLC_Phase_Activities!M{row-start_row+4}"
        ws[f'B{row}'].number_format = '0"%"'
        
        ws[f'C{row}'].value = f"=Secure_Coding_Standards!H{row-start_row+4}"
        ws[f'C{row}'].number_format = '0"%"'
        
        ws[f'D{row}'].value = f"=Code_Review_Metrics!H{row-start_row+4}"
        ws[f'D{row}'].number_format = '0.0"%"'
        
        ws[f'E{row}'].value = f"=Security_Tools_Usage!H{row-start_row+4}"
        ws[f'E{row}'].number_format = '0"%"'
        
        # Training score - placeholder (would calculate from Developer_Training sheet)
        ws[f'F{row}'].value = 85
        ws[f'F{row}'].number_format = '0"%"'
        
        # Overall SDLC Score - weighted average
        ws[f'G{row}'].value = f"=(B{row}*0.3+C{row}*0.15+D{row}*0.15+E{row}*0.2+F{row}*0.2)"
        ws[f'G{row}'].number_format = '0.0"%"'
        
        # Compliance Status
        ws[f'H{row}'].value = f'=IF(G{row}>=80,"✅ Compliant",IF(G{row}>=60,"⚠️ Partial Compliance","❌ Non-Compliant"))'
        
        row += 1
    
    # Column widths
    for i in range(1, 9):
        ws.column_dimensions[get_column_letter(i)].width = 20
    
    ws.freeze_panes = 'A14'
    
    return ws


def build_evidence_register_sheet(wb, styles, validations):
    """Build Evidence Register sheet."""
    ws = wb["Evidence_Register"]
    
    # Title
    ws.merge_cells('A1:G1')
    cell = ws['A1']
    cell.value = "Evidence Register"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    # Subtitle
    ws.merge_cells('A2:G2')
    cell = ws['A2']
    cell.value = "Centralised register of all SDLC security evidence"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Evidence Type",
        "Application/Team Name",
        "Document Title/Description",
        "Document Location/Link",
        "Last Updated",
        "Owner",
        "Status",
    ]
    
    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 25
    ws.column_dimensions['C'].width = 35
    ws.column_dimensions['D'].width = 45
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 20
    ws.column_dimensions['G'].width = 15
    
    # Apply data validations
    validations['evidence_status'].add('G4:G100')
    
    # Example data
    example_data = [
        ["SDLC Checklist", "Customer Portal", "Sprint Security Activities Checklist", "/docs/sdlc/APP-001-sprint-checklist.xlsx", "2025-01-14", "Dev Lead", "Current"],
        ["Code Review Record", "Customer Portal", "Code Review Dashboard (GitLab)", "https://gitlab.com/app-001/merge_requests", "2025-01-15", "Dev Team", "Current"],
        ["SAST Report", "Customer Portal", "SonarQube Security Report Dec 2024", "/reports/sast/APP-001-202412.pdf", "2024-12-31", "Security Team", "Current"],
        ["Training Certificate", "Development Team A", "Secure Coding Training Completion", "/training/team-a-completion-2024.pdf", "2024-11-30", "Training Lead", "Current"],
        ["Security Champion Meeting", "All Teams", "Security Champion Q4 2024 Meeting Minutes", "/docs/security-champions/2024-q4-minutes.pdf", "2024-12-15", "Security Lead", "Current"],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            cell.value = value
            apply_style(cell, styles['data_cell'])
        row += 1
    
    ws.freeze_panes = 'A4'
    
    return ws


def build_approval_sheet(wb, styles):
    """Build Approval/Sign-Off sheet."""
    ws = wb["Approval_Sign_Off"]
    
    # Title
    ws.merge_cells('A1:E1')
    cell = ws['A1']
    cell.value = "Assessment Approval and Sign-Off"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 40
    
    # Assessment Information
    row = 3
    ws.merge_cells(f'A{row}:E{row}')
    cell = ws[f'A{row}']
    cell.value = "Assessment Information"
    apply_style(cell, styles['subheader'])
    
    row += 1
    info = [
        ("Assessment Date:", "[USER INPUT]"),
        ("Assessed By:", "[USER INPUT]"),
        ("Organisation:", "[USER INPUT]"),
        ("Assessment Period:", "[USER INPUT - e.g., Q1 2025]"),
        ("Total Applications Assessed:", "[Auto-calculated or USER INPUT]"),
    ]
    
    for label, value in info:
        ws[f'A{row}'] = label
        ws[f'A{row}'].font = Font(name="Calibri", size=10, bold=True)
        ws[f'B{row}'] = value
        if "[USER INPUT]" in value or "[Auto-calculated" in value:
            ws[f'B{row}'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        row += 1
    
    # Approval Table
    row += 2
    ws.merge_cells(f'A{row}:E{row}')
    cell = ws[f'A{row}']
    cell.value = "Approval Sign-Off"
    apply_style(cell, styles['subheader'])
    
    row += 1
    approval_headers = ["Approver Name", "Role/Title", "Date", "Signature", "Comments"]
    for col_num, header in enumerate(approval_headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Approval rows
    approval_roles = [
        "Security Architect",
        "Development Manager",
        "DevOps Lead",
        "CISO / Security Leadership",
    ]
    
    row += 1
    for role in approval_roles:
        ws[f'A{row}'] = "[Name]"
        ws[f'B{row}'] = role
        ws[f'C{row}'] = "[Date]"
        ws[f'D{row}'] = "[Signature/Initials]"
        ws[f'E{row}'] = ""
        
        # Yellow fill for input cells
        for col in ['A', 'C', 'D', 'E']:
            ws[f'{col}{row}'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        row += 1
    
    # Overall Compliance
    row += 2
    ws.merge_cells(f'A{row}:E{row}')
    cell = ws[f'A{row}']
    cell.value = "Overall Compliance Determination"
    apply_style(cell, styles['subheader'])
    
    row += 1
    ws[f'A{row}'] = "Overall SDLC Compliance Status:"
    ws[f'A{row}'].font = Font(name="Calibri", size=10, bold=True)
    ws[f'B{row}'] = "[✅ Compliant / ⚠️ Partial Compliance / ❌ Non-Compliant]"
    ws[f'B{row}'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
    
    row += 1
    ws[f'A{row}'] = "Overall Compliance Score:"
    ws[f'A{row}'].font = Font(name="Calibri", size=10, bold=True)
    ws[f'B{row}'] = "[X%]"
    ws[f'B{row}'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
    
    # Column widths
    ws.column_dimensions['A'].width = 30
    ws.column_dimensions['B'].width = 30
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 25
    ws.column_dimensions['E'].width = 40
    
    return ws


# ============================================================================
# SECTION 4: MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    logger.info("🚀 Generating ISMS A.8.25 SDLC Security Activities Assessment Workbook...")
    logger.info("=" * 70)
    
    # Create workbook and styles
    logger.info("\n📊 Creating workbook structure...")
    wb = create_workbook()
    styles = setup_styles()
    
    # Build all sheets
    logger.info("📋 Building Instructions & Legend sheet...")
    build_instructions_sheet(wb, styles)
    
    logger.info("📦 Building SDLC Phase Activities sheet...")
    ws_sdlc = wb["SDLC_Phase_Activities"]
    validations = create_base_validations(ws_sdlc)
    build_sdlc_phase_activities_sheet(wb, styles, validations)
    
    logger.info("📄 Building Secure Coding Standards sheet...")
    build_secure_coding_standards_sheet(wb, styles, validations)
    
    logger.info("🔍 Building Code Review Metrics sheet...")
    build_code_review_metrics_sheet(wb, styles, validations)
    
    logger.info("🛠️  Building Security Tools Deployment sheet...")
    build_security_tools_deployment_sheet(wb, styles, validations)
    
    logger.info("📊 Building Security Tools Usage sheet...")
    build_security_tools_usage_sheet(wb, styles, validations)
    
    logger.info("🎓 Building Developer Training sheet...")
    build_developer_training_sheet(wb, styles, validations)
    
    logger.info("🐛 Building Security Defect Management sheet...")
    build_security_defect_management_sheet(wb, styles, validations)
    
    logger.info("📈 Building Compliance Summary dashboard...")
    build_compliance_summary_sheet(wb, styles, validations)
    
    logger.info("📚 Building Evidence Register...")
    build_evidence_register_sheet(wb, styles, validations)
    
    logger.info("✅ Building Approval Sign-Off sheet...")
    build_approval_sheet(wb, styles)
    
    # Save workbook
    filename = f"ISMS-IMP-A.8.25-26-29.S2_SDLC_Security_Activities_Assessment_{datetime.now().strftime('%Y%m%d')}.xlsx"
    logger.info(f"\n💾 Saving workbook: {filename}")
    wb.save(filename)
    
    logger.info("\n" + "=" * 70)
    logger.info("✅ Workbook generated successfully!")
    logger.info("=" * 70)
    logger.info(f"\n📊 File: {filename}")
    logger.info(f"📝 Sheets: {len(wb.sheetnames)}")
    logger.info("\nSheet List:")
    for i, sheet_name in enumerate(wb.sheetnames, 1):
        logger.info(f"  {i}. {sheet_name}")
    
    logger.info("\n" + "=" * 70)
    logger.info("💡 NEXT STEPS:")
    logger.info("=" * 70)
    logger.info("1. Open the workbook in Excel or LibreOffice Calc")
    logger.info("2. Review the Instructions & Legend sheet")
    logger.info("3. Complete SDLC_Phase_Activities for each application")
    logger.info("4. Document secure coding standards adoption")
    logger.info("5. Track code review metrics")
    logger.info("6. Document security tool deployment and usage")
    logger.info("7. Track developer training compliance")
    logger.info("8. Monitor security defect management")
    logger.info("9. Review Compliance_Summary for overall scores")
    logger.info("10. Obtain approvals in Approval_Sign_Off")
    logger.info("\n" + "=" * 70)
    logger.info("📖 REFERENCE:")
    logger.info("=" * 70)
    logger.info("Implementation Guide: ISMS-IMP-A.8.25-26-29-S2")
    logger.info("Policy Reference: ISMS-POL-A.8.25-26-29-S3")
    logger.info("ISO Control: A.8.25 (Secure Development Lifecycle)")
    logger.info("=" * 70)
    
    return filename


if __name__ == "__main__":
    try:
        filename = main()
        logger.info(f"\n✅ SUCCESS: {filename} created successfully\n")
    except Exception as e:
        logger.error(f"\n❌ ERROR: {str(e)}\n")
        import traceback
        traceback.print_exc()
        exit(1)

# =============================================================================
# QA_VERIFIED: 2026-01-31
# QA_STATUS: PASSED - STANDARDIZATION COMPLETE (Phase 1-3)
# QA_TOOL: Claude Code Standardization
# CHANGES: constants, metadata headers, v1.0 versioning, logger output
# =============================================================================
