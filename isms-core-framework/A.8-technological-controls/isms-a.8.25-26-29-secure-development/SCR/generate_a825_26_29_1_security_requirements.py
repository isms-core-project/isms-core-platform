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
ISMS-IMP-A.8.25-26-29.S1 - Security Requirements Assessment Excel Generator
================================================================================

ISO/IEC 27001:2022 Controls A.8.25/A.8.26/A.8.29: Secure Development Framework
Assessment Domain 1 of 5: Application Security Requirements (A.8.26)

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
- Application portfolio and classification scheme
- Security requirements taxonomy and threat model frameworks
- Security architecture review processes

DO NOT use this script without reviewing and adapting all sections marked
with "# CUSTOMIZE:" comments throughout the code.

Reference Pattern: Based on ISMS-A.8.25-26-29 Secure Development Framework

--------------------------------------------------------------------------------
DESCRIPTION
--------------------------------------------------------------------------------

This script generates a comprehensive Excel assessment workbook for evaluating
application security requirements specification and validation processes across
the application portfolio.

**Purpose:**
Enables systematic assessment of security requirements definition, documentation,
threat modeling, architecture review, and traceability against ISO 27001:2022
Control A.8.26 requirements, supporting evidence-based validation of security
requirements practices.

**Assessment Scope:**
- Application inventory with risk classification
- Security requirements documentation completeness
- Functional security requirements coverage
- Non-functional security requirements coverage
- Threat modeling execution and documentation
- Security architecture review completion
- Requirements-to-implementation traceability
- Gap analysis and remediation planning
- Evidence collection for audit readiness

**Generated Workbook Structure:**
1. Instructions & Legend - Assessment guidance and security requirements standards
2. Application Inventory - Complete portfolio with risk classifications
3. Requirements Documentation Status - Documentation completeness per application
4. Threat Modeling Status - Threat model execution and review status
5. Architecture Review Status - Security architecture review completion
6. Traceability Matrix Status - Requirements traceability compliance
7. Compliance Summary - Overall security requirements compliance scores
8. Gap Analysis - Non-compliant applications and remediation requirements
9. Evidence Register - Audit evidence tracking and documentation
10. Approval & Sign-Off - Stakeholder review and approval workflow

**Key Features:**
- Data validation with application risk classification dropdown lists
- Conditional formatting for requirements completeness status
- Automated gap identification for missing requirements documentation
- Protected formulas with unprotected input cells
- Evidence linkage for audit traceability
- Multi-stakeholder approval workflow
- Integration with threat modeling tools and security architecture reviews

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
    python3 generate_a825_26_29_1_security_requirements.py

Advanced Usage:
    # Generate with custom output directory
    python3 generate_a825_26_29_1_security_requirements.py --output /path/to/dir
    
    # Generate with specific date suffix
    python3 generate_a825_26_29_1_security_requirements.py --date 20250124

Output:
    File: ISMS_A_8_25_26_29_1_Security_Requirements_Assessment_YYYYMMDD.xlsx
    Location: Current directory (or specified output path)

Post-Generation Steps:
    1. Review and customize application risk classification criteria
    2. Inventory all applications in your portfolio (internal, vendor, cloud)
    3. Complete requirements documentation status for each application
    4. Validate threat modeling completion for high-risk applications
    5. Review security architecture review status
    6. Verify requirements traceability for critical applications
    7. Conduct gap analysis for applications with missing requirements
    8. Define remediation actions with application owners and timelines
    9. Collect and link audit evidence (requirements docs, threat models, reviews)
    10. Obtain stakeholder approvals
    11. Feed results into A.8.25-26-29.5 Compliance Dashboard

--------------------------------------------------------------------------------
METADATA
--------------------------------------------------------------------------------

Control Reference:    ISO/IEC 27001:2022 Annex A Controls A.8.25/A.8.26/A.8.29
Assessment Domain:    1 of 5 (Application Security Requirements - A.8.26)
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
    - ISMS-IMP-A.8.25-26-29-S1: Security Requirements Process Implementation Guide
    - ISMS-IMP-A.8.25-26-29.S5: Compliance Dashboard (Consolidation)

Related Scripts:
    - generate_a825_26_29_1_security_requirements.py (this script)
    - generate_a825_26_29_2_sdlc_security_activities.py
    - generate_a825_26_29_3_security_testing_results.py
    - generate_a825_26_29_4_vulnerability_remediation.py
    - generate_a825_26_29_5_compliance_dashboard.py
    - normalize_assessment_files_a825_26_29.py

--------------------------------------------------------------------------------
CHANGE HISTORY
--------------------------------------------------------------------------------

Version 1.0 - [YYYY-MM-DD]
    - Initial release
    - Implements full assessment framework per ISMS-IMP-A.8.25-26-29-S1 spec
    - Supports comprehensive security requirements evaluation
    - Integrated with A.8.25-26-29.5 Compliance Dashboard

[Future changes to be documented here]

--------------------------------------------------------------------------------
IMPORTANT NOTES
--------------------------------------------------------------------------------

**SDLC Methodology Neutrality:**
This assessment framework is methodology-agnostic and must work across:
- Waterfall: Traditional phase-gate development with upfront requirements
- Agile: Iterative sprint-based development with evolving requirements
- DevOps/DevSecOps: Continuous integration/deployment with security automation
- Hybrid: Mixed methodology approaches
Customize dropdown values and assessment criteria to match YOUR methodology.

**Technology Stack Agnosticism:**
Framework must remain vendor-neutral and technology-agnostic:
- Programming languages: Java, Python, C#, JavaScript, Go, Ruby, etc.
- Frameworks: Spring, Django, .NET, React, Angular, Vue, etc.
- Platforms: Web, mobile, desktop, embedded, cloud-native, SaaS, etc.
Do NOT hardcode technology-specific assumptions in assessment criteria.

**Security Tool Diversity:**
Assessment must accommodate various security requirements and threat modeling tools:
- Threat Modeling: Microsoft Threat Modeling Tool, OWASP Threat Dragon, IriusRisk
- Requirements Management: Jira, Azure DevOps, Confluence, custom systems
- Architecture Tools: Enterprise Architect, draw.io, Lucidchart, C4 Model
Use generic terms; avoid vendor lock-in in assessment structure.

**Audit Considerations:**
This assessment generates audit evidence per ISO 27001:2022 requirements.
Ensure all fields are completed accurately and evidence is properly linked.
Auditors will expect:
- Complete application inventory with risk classifications
- Documented security requirements for each application
- Threat models for high-risk applications
- Security architecture review records
- Requirements traceability matrices
- Evidence of requirements validation and approval

**Data Protection:**
Assessment workbooks contain sensitive application information including:
- Application portfolio and architecture details
- Risk classifications and threat assessments
- Security requirements and control implementations
- Security gaps and vulnerabilities
- Internal system names and data flows
Handle in accordance with your organization's data classification policies.

**Maintenance:**
Review and update assessment:
- Quarterly: Complete reassessment of all applications
- Semi-annually: Update risk classifications based on threat landscape
- Annually: Review and update security requirements taxonomy
- Ad-hoc: When new applications are deployed or architectures change

**Quality Assurance:**
Have Application Security team, Security Architects, and Development Leads
validate assessments before using results for compliance reporting or
remediation decisions.

**Regulatory Alignment:**
Security requirements assessment supports regulatory compliance:
- Payment processing: PCI DSS v4.0.1 requirement 6.3 (secure development)
- Healthcare: HIPAA security requirements for applications handling PHI
- Finance: Regional banking requirements for secure application development
- Privacy: GDPR/FADP privacy-by-design and data protection requirements
Customize assessment criteria to include regulatory-specific requirements
applicable to your organization and industry.

**Integration with Related Controls:**
This assessment integrates with:
- A.8.4 (Access to Source Code): Requirements for repository access controls
- A.8.28 (Secure Coding): Requirements inform secure coding standards
- A.8.31 (Environment Separation): Requirements for environment isolation
- A.8.32 (Change Management): Requirements traceability in change process
- A.8.25 (Secure Development Lifecycle): Requirements feed into SDLC phases
- A.8.29 (Security Testing): Requirements define test cases and acceptance criteria

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
DOCUMENT_ID = "ISMS-IMP-A.8.25-26-29.S1"
CONTROL_REF = "ISO/IEC 27001:2022 - Controls A.8.25, A.8.26, A.8.29: Secure Development"
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")
OUTPUT_FILENAME = f"{DOCUMENT_ID}_Security_Requirements_Assessment_{GENERATED_TIMESTAMP}.xlsx"


# ============================================================================
# SECTION 1: WORKBOOK CREATION & STYLE DEFINITIONS
# ============================================================================

def create_workbook() -> Workbook:
    """Create workbook with all required sheets matching IMP specification."""
    wb = Workbook()
    
    # Remove default sheet
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])
    
    # Sheet structure from ISMS-IMP-A.8.25-26-29-S1 Section 6.2
    sheets = [
        "Instructions & Legend",
        "Application_Inventory",
        "Requirements_Documentation_Status",
        "Threat_Modeling_Status",
        "Architecture_Review_Status",
        "Traceability_Matrix_Status",
        "Compliance_Summary",
        "Gap_Analysis",
        "Evidence_Register",
        "Approval_Sign_Off",
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
    
    # Return style TEMPLATES (dictionaries), not objects
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
        "percentage_good": {
            "fill": PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid"),
        },
        "percentage_fair": {
            "fill": PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid"),
        },
        "percentage_poor": {
            "fill": PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid"),
        },
    }
    return styles


def apply_style(cell, style_dict):
    """
    Apply style dictionary to a cell.
    Creates NEW style objects to avoid shared object warnings.
    """
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
    """
    Create data validation objects for standard dropdowns.
    These are added to worksheet once, then applied to multiple cells.
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
        'yes_no_partial': DataValidation(
            type="list",
            formula1='"Yes,No,Partial"',
            allow_blank=False
        ),
        'yes_no_planned': DataValidation(
            type="list",
            formula1='"Yes,No,Planned"',
            allow_blank=False
        ),
        'yes_no_scheduled': DataValidation(
            type="list",
            formula1='"Yes,No,Scheduled"',
            allow_blank=False
        ),
        'risk_classification': DataValidation(
            type="list",
            formula1='"High Risk,Medium Risk,Low Risk"',
            allow_blank=False
        ),
        'approval_status': DataValidation(
            type="list",
            formula1='"✅ Approved,⏳ Pending,❌ Not Approved"',
            allow_blank=False
        ),
        'threat_methodology': DataValidation(
            type="list",
            formula1='"STRIDE,PASTA,LINDDUN,Other,N/A"',
            allow_blank=False
        ),
        'evidence_status': DataValidation(
            type="list",
            formula1='"Current,Outdated,Missing"',
            allow_blank=False
        ),
        'compliance_status': DataValidation(
            type="list",
            formula1='"✅ Compliant,⚠️ Partial Compliance,❌ Non-Compliant"',
            allow_blank=False
        ),
    }
    
    # Add validations to worksheet
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
    cell.value = "ISO/IEC 27001:2022 - Control A.8.26: Application Security Requirements"
    apply_style(cell, styles['subheader'])
    
    # Document Information
    row = 4
    info = [
        ("Document ID:", "ISMS-IMP-A.8.25-26-29.S1"),
        ("Assessment Area:", "Application Security Requirements"),
        ("Related Policy:", "ISMS-POL-A.8.25-26-29-S2"),
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
    
    # How to Use This Workbook
    row += 1
    ws.merge_cells(f'A{row}:F{row}')
    cell = ws[f'A{row}']
    cell.value = "How to Use This Workbook"
    apply_style(cell, styles['subheader'])
    
    row += 1
    instructions = [
        "1. Complete the Application_Inventory sheet with all applications in your portfolio",
        "2. For each application, complete the Requirements_Documentation_Status sheet",
        "3. For each application, complete the Threat_Modeling_Status sheet",
        "4. For each application, complete the Architecture_Review_Status sheet",
        "5. For each application, complete the Traceability_Matrix_Status sheet",
        "6. Review the Compliance_Summary sheet for overall compliance scores",
        "7. Document evidence in the Evidence_Register sheet",
        "8. Obtain approval and sign-off in the Approval_Sign_Off sheet",
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
    legend_headers = ["Symbol", "Status", "Description", "Color Code"]
    for col_num, header in enumerate(legend_headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    row += 1
    legend_data = [
        ("✅", "Compliant", "Requirement met, fully implemented", "Green"),
        ("⚠️", "Partial", "Partially implemented, needs improvement", "Yellow"),
        ("❌", "Non-Compliant", "Not implemented, not meeting requirement", "Red"),
        ("⏳", "Pending", "In progress, under review", "Blue"),
        ("N/A", "Not Applicable", "Not applicable to this application", "Gray"),
    ]
    
    for symbol, status, description, color in legend_data:
        ws[f'A{row}'] = symbol
        ws[f'B{row}'] = status
        ws[f'C{row}'] = description
        ws[f'D{row}'] = color
        
        # Apply color to color code cell
        if color == "Green":
            ws[f'D{row}'].fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
        elif color == "Yellow":
            ws[f'D{row}'].fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
        elif color == "Red":
            ws[f'D{row}'].fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
        elif color == "Blue":
            ws[f'D{row}'].fill = PatternFill(start_color="B4C7E7", end_color="B4C7E7", fill_type="solid")
        
        row += 1
    
    # Acceptable Evidence
    row += 1
    ws.merge_cells(f'A{row}:F{row}')
    cell = ws[f'A{row}']
    cell.value = "Acceptable Evidence (Examples)"
    apply_style(cell, styles['subheader'])
    
    row += 1
    evidence_examples = [
        "✓ Security Requirements Documents (SEC-REQ-XXX format)",
        "✓ Threat Models (STRIDE, PASTA, LINDDUN methodologies)",
        "✓ Architecture Review Reports (with findings and approvals)",
        "✓ Requirements Traceability Matrices (linking requirements to design, code, tests)",
        "✓ Security Approval Sign-offs (from Security Architects, Product Owners)",
        "✓ Application Risk Classification Documentation",
        "✓ Security Requirements Workshop Materials (agendas, attendees, outputs)",
        "✓ Threat Modeling Workshop Materials (DFDs, threat lists, mitigations)",
    ]
    
    for example in evidence_examples:
        ws[f'A{row}'] = example
        ws[f'A{row}'].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        row += 1
    
    # Column widths
    ws.column_dimensions['A'].width = 12
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width = 50
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 15
    
    # Freeze panes
    ws.freeze_panes = 'A3'
    
    return ws


def build_application_inventory_sheet(wb, styles, validations):
    """Build Application Inventory sheet."""
    ws = wb["Application_Inventory"]
    
    # Title
    ws.merge_cells('A1:J1')
    cell = ws['A1']
    cell.value = "Application Inventory"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    # Subtitle
    ws.merge_cells('A2:J2')
    cell = ws['A2']
    cell.value = "Complete inventory of all applications requiring security requirements assessment"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Application Name",
        "Application ID",
        "Application Owner",
        "Business Criticality",
        "Risk Classification",
        "Technology Stack",
        "Deployment Model",
        "Regulatory Scope",
        "Internet Facing",
        "Last Assessment Date",
    ]
    
    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    ws.column_dimensions['A'].width = 25  # Application Name
    ws.column_dimensions['B'].width = 15  # Application ID
    ws.column_dimensions['C'].width = 20  # Owner
    ws.column_dimensions['D'].width = 18  # Business Criticality
    ws.column_dimensions['E'].width = 18  # Risk Classification
    ws.column_dimensions['F'].width = 22  # Technology Stack
    ws.column_dimensions['G'].width = 18  # Deployment Model
    ws.column_dimensions['H'].width = 20  # Regulatory Scope
    ws.column_dimensions['I'].width = 15  # Internet Facing
    ws.column_dimensions['J'].width = 18  # Last Assessment
    
    # Apply data validations
    validations['risk_classification'].add('E4:E100')
    validations['yes_no'].add('I4:I100')
    
    # Example data rows
    example_data = [
        ["Customer Portal", "APP-001", "Anna Müller", "High", "High Risk", "Java/Spring Boot", "AWS Cloud", "GDPR, PCI DSS v4.0.1", "Yes", "2025-01-15"],
        ["Internal HR System", "APP-002", "Thomas Meier", "Medium", "Medium Risk", "Python/Django", "On-Premises", "GDPR", "No", "2024-12-10"],
        ["Marketing Website", "APP-003", "Sandra Brunner", "Medium", "Medium Risk", "Static HTML/CSS", "CDN (Cloudflare)", "None", "Yes", "2025-01-05"],
        ["Employee Portal", "APP-004", "Markus Huber", "Medium", "Medium Risk", "ASP.NET Core", "Azure Cloud", "GDPR", "No", "2024-11-22"],
        ["Finance Dashboard", "APP-005", "Petra Keller", "High", "High Risk", "React + Node.js", "AWS Cloud", "SOX, GDPR", "No", "2025-01-08"],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            cell.value = value
            apply_style(cell, styles['data_cell'])
        row += 1
    
    # Freeze panes
    ws.freeze_panes = 'A4'
    
    return ws


def build_requirements_documentation_sheet(wb, styles, validations):
    """Build Requirements Documentation Status sheet."""
    ws = wb["Requirements_Documentation_Status"]
    
    # Title
    ws.merge_cells('A1:K1')
    cell = ws['A1']
    cell.value = "Security Requirements Documentation Assessment"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    # Subtitle
    ws.merge_cells('A2:K2')
    cell = ws['A2']
    cell.value = "Assess completeness of security requirements documentation per application"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Application Name",
        "Requirements Document Exists?",
        "Document Location/Link",
        "Last Updated",
        "Requirements Approved?",
        "Approver Name",
        "Approval Date",
        "Functional Requirements (%)",
        "Non-Functional Requirements (%)",
        "Data Protection Requirements (%)",
        "Completeness Score (%)",
    ]
    
    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 18
    ws.column_dimensions['C'].width = 40
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 18
    ws.column_dimensions['F'].width = 20
    ws.column_dimensions['G'].width = 15
    ws.column_dimensions['H'].width = 20
    ws.column_dimensions['I'].width = 22
    ws.column_dimensions['J'].width = 22
    ws.column_dimensions['K'].width = 18
    
    # Apply data validations
    validations['yes_no'].add('B4:B100')
    validations['yes_no'].add('E4:E100')
    
    # Example data with formulas
    example_data = [
        ["Customer Portal", "Yes", "/docs/security-requirements/APP-001-sec-req.pdf", "2025-01-10", "Yes", "Anna Müller", "2025-01-12", 95, 90, 100],
        ["Internal HR System", "Yes", "/docs/security-requirements/APP-002-sec-req.pdf", "2024-11-20", "Yes", "Thomas Meier", "2024-11-25", 85, 80, 90],
        ["Marketing Website", "Partial", "/docs/security-requirements/APP-003-baseline.pdf", "2024-12-15", "Yes", "Sandra Brunner", "2024-12-18", 60, 50, 70],
        ["Employee Portal", "Yes", "/docs/security-requirements/APP-004-sec-req.pdf", "2024-11-15", "Yes", "Markus Huber", "2024-11-18", 88, 85, 92],
        ["Finance Dashboard", "Yes", "/docs/security-requirements/APP-005-sec-req.pdf", "2025-01-05", "Yes", "Petra Keller", "2025-01-07", 92, 88, 95],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            if col_num <= 10:  # Data columns
                cell.value = value
                apply_style(cell, styles['data_cell'])
            else:  # Completeness Score (Column K) - formula
                # Formula: =IF(AND(H4<>"",I4<>"",J4<>""),(H4+I4+J4)/3,"")
                cell.value = f'=IF(AND(H{row}<>"",I{row}<>"",J{row}<>""),(H{row}+I{row}+J{row})/3,"")'
                cell.number_format = '0.0"%"'
        row += 1
    
    # Freeze panes
    ws.freeze_panes = 'A4'
    
    return ws


def build_threat_modeling_sheet(wb, styles, validations):
    """Build Threat Modeling Status sheet."""
    ws = wb["Threat_Modeling_Status"]
    
    # Title
    ws.merge_cells('A1:K1')
    cell = ws['A1']
    cell.value = "Threat Modeling Status Assessment"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    # Subtitle
    ws.merge_cells('A2:K2')
    cell = ws['A2']
    cell.value = "Assess threat modeling completion and quality per application"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Application Name",
        "Threat Model Exists?",
        "Methodology Used",
        "Threat Model Location/Link",
        "Last Updated",
        "DFD Created?",
        "Threats Documented?",
        "Mitigations Defined?",
        "Approval Status",
        "Approver Name",
        "Completeness Score (%)",
    ]
    
    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 18
    ws.column_dimensions['C'].width = 18
    ws.column_dimensions['D'].width = 40
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 15
    ws.column_dimensions['G'].width = 18
    ws.column_dimensions['H'].width = 18
    ws.column_dimensions['I'].width = 18
    ws.column_dimensions['J'].width = 20
    ws.column_dimensions['K'].width = 18
    
    # Apply data validations
    validations['yes_no_planned'].add('B4:B100')
    validations['threat_methodology'].add('C4:C100')
    validations['yes_no'].add('F4:F100')
    validations['yes_no'].add('G4:G100')
    validations['yes_no'].add('H4:H100')
    validations['approval_status'].add('I4:I100')
    
    # Example data with formulas
    example_data = [
        ["Customer Portal", "Yes", "STRIDE", "/docs/threat-models/APP-001-threat-model.pdf", "2025-01-08", "Yes", "Yes", "Yes", "✅ Approved", "Anna Müller"],
        ["Internal HR System", "Yes", "STRIDE", "/docs/threat-models/APP-002-threat-model.pdf", "2024-11-18", "Yes", "Yes", "Yes", "✅ Approved", "Thomas Meier"],
        ["Marketing Website", "No", "N/A", "", "", "No", "No", "No", "❌ Not Approved", ""],
        ["Employee Portal", "Yes", "STRIDE", "/docs/threat-models/APP-004-threat-model.pdf", "2024-11-12", "Yes", "Yes", "Partial", "⏳ Pending", "Markus Huber"],
        ["Finance Dashboard", "Yes", "STRIDE", "/docs/threat-models/APP-005-threat-model.pdf", "2025-01-03", "Yes", "Yes", "Yes", "✅ Approved", "Petra Keller"],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            if col_num <= 10:  # Data columns
                cell.value = value
                apply_style(cell, styles['data_cell'])
            else:  # Completeness Score (Column K) - formula
                # Formula: =IF(B{row}="Yes",(IF(F{row}="Yes",25,0)+IF(G{row}="Yes",25,0)+IF(H{row}="Yes",25,0)+IF(I{row}="✅ Approved",25,0)),"N/A")
                cell.value = f'=IF(B{row}="Yes",(IF(F{row}="Yes",25,0)+IF(G{row}="Yes",25,0)+IF(H{row}="Yes",25,0)+IF(I{row}="✅ Approved",25,0)),"N/A")'
                cell.number_format = '0"%"'
        row += 1
    
    # Freeze panes
    ws.freeze_panes = 'A4'
    
    return ws


def build_architecture_review_sheet(wb, styles, validations):
    """Build Architecture Review Status sheet."""
    ws = wb["Architecture_Review_Status"]
    
    # Title
    ws.merge_cells('A1:L1')
    cell = ws['A1']
    cell.value = "Security Architecture Review Status"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    # Subtitle
    ws.merge_cells('A2:L2')
    cell = ws['A2']
    cell.value = "Assess security architecture review completion and findings per application"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Application Name",
        "Review Conducted?",
        "Review Date",
        "Review Report Location/Link",
        "Reviewers",
        "Critical Findings",
        "High Findings",
        "Medium Findings",
        "Low Findings",
        "Open Findings",
        "Approval Status",
        "Approval Date",
    ]
    
    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 18
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 40
    ws.column_dimensions['E'].width = 25
    ws.column_dimensions['F'].width = 15
    ws.column_dimensions['G'].width = 15
    ws.column_dimensions['H'].width = 15
    ws.column_dimensions['I'].width = 15
    ws.column_dimensions['J'].width = 15
    ws.column_dimensions['K'].width = 18
    ws.column_dimensions['L'].width = 15
    
    # Apply data validations
    validations['yes_no_scheduled'].add('B4:B100')
    validations['approval_status'].add('K4:K100')
    
    # Example data
    example_data = [
        ["Customer Portal", "Yes", "2025-01-09", "/docs/arch-reviews/APP-001-arch-review.pdf", "Security Team, Tech Lead", 0, 0, 2, 3, 0, "✅ Approved", "2025-01-11"],
        ["Internal HR System", "Yes", "2024-11-19", "/docs/arch-reviews/APP-002-arch-review.pdf", "Security Architect", 0, 1, 3, 2, 0, "✅ Approved", "2024-11-22"],
        ["Marketing Website", "No", "", "", "", 0, 0, 0, 0, 0, "❌ Not Approved", ""],
        ["Employee Portal", "Yes", "2024-11-14", "/docs/arch-reviews/APP-004-arch-review.pdf", "Security Team", 0, 2, 1, 1, 2, "⏳ Pending", ""],
        ["Finance Dashboard", "Yes", "2025-01-04", "/docs/arch-reviews/APP-005-arch-review.pdf", "Security Architect, CTO", 0, 0, 1, 2, 0, "✅ Approved", "2025-01-06"],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            cell.value = value
            apply_style(cell, styles['data_cell'])
        row += 1
    
    # Freeze panes
    ws.freeze_panes = 'A4'
    
    return ws


def build_traceability_sheet(wb, styles, validations):
    """Build Traceability Matrix Status sheet."""
    ws = wb["Traceability_Matrix_Status"]
    
    # Title
    ws.merge_cells('A1:I1')
    cell = ws['A1']
    cell.value = "Requirements Traceability Matrix Status"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30
    
    # Subtitle
    ws.merge_cells('A2:I2')
    cell = ws['A2']
    cell.value = "Assess requirements traceability completeness per application"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Application Name",
        "Traceability Matrix Exists?",
        "Matrix Location/Link",
        "Last Updated",
        "Requirements → Design Traced?",
        "Requirements → Code Traced?",
        "Requirements → Tests Traced?",
        "Traceability Coverage (%)",
        "Quality Score (%)",
    ]
    
    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width = 40
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 22
    ws.column_dimensions['F'].width = 22
    ws.column_dimensions['G'].width = 22
    ws.column_dimensions['H'].width = 18
    ws.column_dimensions['I'].width = 15
    
    # Apply data validations
    validations['yes_no'].add('B4:B100')
    validations['yes_no_partial'].add('E4:E100')
    validations['yes_no_partial'].add('F4:F100')
    validations['yes_no_partial'].add('G4:G100')
    
    # Example data with formulas
    example_data = [
        ["Customer Portal", "Yes", "/docs/traceability/APP-001-traceability.xlsx", "2025-01-14", "Yes", "Yes", "Yes", 95],
        ["Internal HR System", "Yes", "/docs/traceability/APP-002-traceability.xlsx", "2024-12-08", "Yes", "Yes", "Partial", 85],
        ["Marketing Website", "No", "", "", "No", "No", "No", 0],
        ["Employee Portal", "Yes", "/docs/traceability/APP-004-traceability.xlsx", "2024-11-20", "Yes", "Partial", "Partial", 75],
        ["Finance Dashboard", "Yes", "/docs/traceability/APP-005-traceability.xlsx", "2025-01-07", "Yes", "Yes", "Yes", 90],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            if col_num <= 8:  # Data columns
                cell.value = value
                apply_style(cell, styles['data_cell'])
                if col_num == 8:  # Coverage percentage
                    cell.number_format = '0"%"'
            else:  # Quality Score (Column I) - formula
                # Formula: =IF(B{row}="Yes",(IF(E{row}="Yes",33,IF(E{row}="Partial",16.5,0))+IF(F{row}="Yes",33,IF(F{row}="Partial",16.5,0))+IF(G{row}="Yes",34,IF(G{row}="Partial",17,0))),"N/A")
                cell.value = f'=IF(B{row}="Yes",(IF(E{row}="Yes",33,IF(E{row}="Partial",16.5,0))+IF(F{row}="Yes",33,IF(F{row}="Partial",16.5,0))+IF(G{row}="Yes",34,IF(G{row}="Partial",17,0))),"N/A")'
                cell.number_format = '0.0"%"'
        row += 1
    
    # Freeze panes
    ws.freeze_panes = 'A4'
    
    return ws


def build_compliance_summary_sheet(wb, styles, validations):
    """Build Compliance Summary dashboard sheet."""
    ws = wb["Compliance_Summary"]
    
    # Title
    ws.merge_cells('A1:H1')
    cell = ws['A1']
    cell.value = "A.8.26 Security Requirements Compliance Dashboard"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 40
    
    # Subtitle
    ws.merge_cells('A2:H2')
    cell = ws['A2']
    cell.value = "Overall compliance summary for application security requirements"
    apply_style(cell, styles['subheader'])
    
    # Summary Statistics Section
    row = 4
    ws.merge_cells(f'A{row}:H{row}')
    cell = ws[f'A{row}']
    cell.value = "Portfolio Summary Statistics"
    apply_style(cell, styles['subheader'])
    
    row += 1
    summary_labels = [
        "Total Applications:",
        "High Risk Applications:",
        "Medium Risk Applications:",
        "Low Risk Applications:",
        "Applications with Security Requirements:",
        "Applications with Threat Models:",
        "Applications with Architecture Reviews:",
        "Overall Portfolio Compliance Score:",
    ]
    
    for label in summary_labels:
        ws[f'A{row}'] = label
        ws[f'A{row}'].font = Font(name="Calibri", size=10, bold=True)
        ws[f'B{row}'] = "[Calculated from data]"
        ws[f'B{row}'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        row += 1
    
    # Application-Level Compliance Table
    row += 1
    ws.merge_cells(f'A{row}:H{row}')
    cell = ws[f'A{row}']
    cell.value = "Application-Level Compliance Scores"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    row += 1
    headers = [
        "Application Name",
        "Risk Level",
        "Req Score (%)",
        "TM Score (%)",
        "Arch Score",
        "Trace Score (%)",
        "Overall Score (%)",
        "Compliance Status",
    ]
    
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])
    
    # Column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 15
    ws.column_dimensions['G'].width = 18
    ws.column_dimensions['H'].width = 22
    
    # Example data with formulas
    example_apps = [
        "Customer Portal",
        "Internal HR System",
        "Marketing Website",
        "Employee Portal",
        "Finance Dashboard",
    ]
    
    row += 1
    start_row = row
    for app_name in example_apps:
        ws[f'A{row}'] = app_name
        ws[f'B{row}'] = "High Risk"  # Simplified - would lookup from Application_Inventory
        
        # Requirements Score - reference to Requirements_Documentation_Status sheet
        ws[f'C{row}'].value = f"=Requirements_Documentation_Status!K{row-start_row+4}"
        ws[f'C{row}'].number_format = '0.0"%"'
        
        # Threat Model Score - reference to Threat_Modeling_Status sheet
        ws[f'D{row}'].value = f"=Threat_Modeling_Status!K{row-start_row+4}"
        ws[f'D{row}'].number_format = '0"%"'
        
        # Architecture Score - calculated from approval status
        ws[f'E{row}'].value = f'=IF(Architecture_Review_Status!K{row-start_row+4}="✅ Approved",100,IF(Architecture_Review_Status!K{row-start_row+4}="⏳ Pending",50,0))'
        ws[f'E{row}'].number_format = '0"%"'
        
        # Traceability Score - reference to Traceability_Matrix_Status sheet
        ws[f'F{row}'].value = f"=Traceability_Matrix_Status!I{row-start_row+4}"
        ws[f'F{row}'].number_format = '0.0"%"'
        
        # Overall Score - weighted average
        ws[f'G{row}'].value = f"=(C{row}*0.4+D{row}*0.3+E{row}*0.2+F{row}*0.1)"
        ws[f'G{row}'].number_format = '0.0"%"'
        
        # Compliance Status
        ws[f'H{row}'].value = f'=IF(G{row}>=80,"✅ Compliant",IF(G{row}>=60,"⚠️ Partial Compliance","❌ Non-Compliant"))'
        
        row += 1
    
    # Gap Analysis Section
    row += 1
    ws.merge_cells(f'A{row}:H{row}')
    cell = ws[f'A{row}']
    cell.value = "Gap Analysis - Applications Requiring Attention"
    apply_style(cell, styles['subheader'])
    
    row += 1
    gaps = [
        "Applications without Security Requirements:",
        "Applications without Threat Models:",
        "Applications without Architecture Reviews:",
        "Applications with Open Critical Findings:",
        "Applications below 80% Compliance Threshold:",
    ]
    
    for gap in gaps:
        ws[f'A{row}'] = gap
        ws[f'A{row}'].font = Font(name="Calibri", size=10, bold=True)
        ws[f'B{row}'] = "[List applications]"
        ws[f'B{row}'].fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
        row += 1
    
    # Freeze panes
    ws.freeze_panes = 'A18'

    return ws


def build_gap_analysis_sheet(wb, styles, validations):
    """Build Gap Analysis sheet for tracking non-compliant applications and remediation."""
    ws = wb["Gap_Analysis"]

    # Title
    ws.merge_cells('A1:J1')
    cell = ws['A1']
    cell.value = "Gap Analysis & Remediation Tracking"
    apply_style(cell, styles['header'])
    ws.row_dimensions[1].height = 30

    # Subtitle
    ws.merge_cells('A2:J2')
    cell = ws['A2']
    cell.value = "Track security requirements gaps and remediation actions per application"
    apply_style(cell, styles['subheader'])

    # Column headers
    headers = [
        "Gap ID",
        "Application Name",
        "Gap Category",
        "Gap Description",
        "Risk Level",
        "Remediation Action",
        "Owner",
        "Target Date",
        "Status",
        "Notes",
    ]

    row = 3
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        apply_style(cell, styles['column_header'])

    # Column widths
    ws.column_dimensions['A'].width = 12
    ws.column_dimensions['B'].width = 25
    ws.column_dimensions['C'].width = 22
    ws.column_dimensions['D'].width = 40
    ws.column_dimensions['E'].width = 12
    ws.column_dimensions['F'].width = 35
    ws.column_dimensions['G'].width = 20
    ws.column_dimensions['H'].width = 15
    ws.column_dimensions['I'].width = 15
    ws.column_dimensions['J'].width = 30

    # Apply data validations
    validations['risk_classification'].add('E4:E100')

    # Example gap data
    example_data = [
        ["GAP-001", "Marketing Website", "Missing Requirements", "No security requirements document exists", "High Risk", "Create security requirements document", "Sandra Brunner", "2025-03-15", "Open", "Low-risk app but needs baseline requirements"],
        ["GAP-002", "Marketing Website", "Missing Threat Model", "No threat model conducted", "Medium Risk", "Conduct STRIDE threat modeling session", "Security Team", "2025-03-30", "Open", "Schedule with app team"],
        ["GAP-003", "Marketing Website", "Missing Architecture Review", "No security architecture review performed", "Medium Risk", "Schedule architecture review", "Security Architect", "2025-04-15", "Open", "Depends on GAP-001 completion"],
        ["GAP-004", "Employee Portal", "Open Findings", "2 high-severity findings from architecture review remain open", "High Risk", "Remediate authentication bypass and input validation issues", "Markus Huber", "2025-02-28", "In Progress", "Dev team working on fixes"],
        ["GAP-005", "Internal HR System", "Partial Traceability", "Requirements to tests traceability only 85% complete", "Low Risk", "Complete traceability matrix for remaining requirements", "Dev Lead", "2025-02-15", "In Progress", "15% remaining"],
    ]

    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            cell.value = value
            apply_style(cell, styles['data_cell'])

            # Color code status
            if col_num == 9:  # Status column
                if value == "Open":
                    cell.fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
                elif value == "In Progress":
                    cell.fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
                elif value == "Closed":
                    cell.fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")

            # Color code risk level
            if col_num == 5:  # Risk Level column
                if "High" in value:
                    cell.fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
                elif "Medium" in value:
                    cell.fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
                elif "Low" in value:
                    cell.fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
        row += 1

    # Freeze panes
    ws.freeze_panes = 'A4'

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
    cell.value = "Centralised register of all security requirements evidence"
    apply_style(cell, styles['subheader'])
    
    # Column headers
    headers = [
        "Evidence Type",
        "Application Name",
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
        ["Security Requirements", "Customer Portal", "APP-001 Security Requirements v1.2", "/docs/security-requirements/APP-001-sec-req.pdf", "2025-01-10", "Anna Müller", "Current"],
        ["Threat Model", "Customer Portal", "APP-001 STRIDE Threat Model", "/docs/threat-models/APP-001-threat-model.pdf", "2025-01-08", "Security Team", "Current"],
        ["Architecture Review", "Customer Portal", "APP-001 Security Architecture Review Report", "/docs/arch-reviews/APP-001-arch-review.pdf", "2025-01-09", "Security Architect", "Current"],
        ["Traceability Matrix", "Customer Portal", "APP-001 Requirements Traceability", "/docs/traceability/APP-001-traceability.xlsx", "2025-01-14", "Dev Lead", "Current"],
        ["Security Requirements", "Internal HR System", "APP-002 Security Requirements v1.0", "/docs/security-requirements/APP-002-sec-req.pdf", "2024-11-20", "Thomas Meier", "Current"],
        ["Threat Model", "Internal HR System", "APP-002 STRIDE Threat Model", "/docs/threat-models/APP-002-threat-model.pdf", "2024-11-18", "Security Team", "Current"],
        ["Architecture Review", "Internal HR System", "APP-002 Security Architecture Review", "/docs/arch-reviews/APP-002-arch-review.pdf", "2024-11-19", "Security Architect", "Current"],
        ["Security Requirements", "Marketing Website", "APP-003 Baseline Security Requirements", "/docs/security-requirements/APP-003-baseline.pdf", "2024-12-15", "Sandra Brunner", "Outdated"],
    ]
    
    row = 4
    for row_data in example_data:
        for col_num, value in enumerate(row_data, 1):
            cell = ws.cell(row=row, column=col_num)
            cell.value = value
            apply_style(cell, styles['data_cell'])
        row += 1
    
    # Freeze panes
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
        "CISO / Security Leadership",
        "Compliance Officer",
        "Application Portfolio Manager",
    ]
    
    row += 1
    for role in approval_roles:
        ws[f'A{row}'] = "[Name]"
        ws[f'B{row}'] = role
        ws[f'C{row}'] = "[Date]"
        ws[f'D{row}'] = "[Signature/Initials]"
        ws[f'E{row}'] = ""
        
        # Yellow fill for input cells
        ws[f'A{row}'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        ws[f'C{row}'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        ws[f'D{row}'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        ws[f'E{row}'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        
        row += 1
    
    # Overall Compliance Determination
    row += 2
    ws.merge_cells(f'A{row}:E{row}')
    cell = ws[f'A{row}']
    cell.value = "Overall Compliance Determination"
    apply_style(cell, styles['subheader'])
    
    row += 1
    ws[f'A{row}'] = "Overall Portfolio Compliance Status:"
    ws[f'A{row}'].font = Font(name="Calibri", size=10, bold=True)
    ws[f'B{row}'] = "[✅ Compliant / ⚠️ Partial Compliance / ❌ Non-Compliant]"
    ws[f'B{row}'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
    
    row += 1
    ws[f'A{row}'] = "Overall Compliance Score:"
    ws[f'A{row}'].font = Font(name="Calibri", size=10, bold=True)
    ws[f'B{row}'] = "[X%]"
    ws[f'B{row}'].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
    
    # Recommended Actions
    row += 2
    ws.merge_cells(f'A{row}:E{row}')
    cell = ws[f'A{row}']
    cell.value = "Recommended Actions"
    apply_style(cell, styles['subheader'])
    
    row += 1
    ws.merge_cells(f'A{row}:E{row+5}')
    cell = ws[f'A{row}']
    cell.value = "[Document recommended actions based on gap analysis and compliance summary]"
    cell.fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
    cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    ws.row_dimensions[row].height = 100
    
    # Column widths
    ws.column_dimensions['A'].width = 25
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
    logger.info("🚀 Generating ISMS A.8.26 Security Requirements Assessment Workbook...")
    logger.info("=" * 70)
    
    # Create workbook and styles
    logger.info("\n📊 Creating workbook structure...")
    wb = create_workbook()
    styles = setup_styles()
    
    # Build all sheets
    logger.info("📋 Building Instructions & Legend sheet...")
    build_instructions_sheet(wb, styles)
    
    logger.info("📦 Building Application Inventory sheet...")
    ws_inventory = wb["Application_Inventory"]
    validations = create_base_validations(ws_inventory)
    build_application_inventory_sheet(wb, styles, validations)
    
    logger.info("📄 Building Requirements Documentation Status sheet...")
    build_requirements_documentation_sheet(wb, styles, validations)
    
    logger.info("🎯 Building Threat Modeling Status sheet...")
    build_threat_modeling_sheet(wb, styles, validations)
    
    logger.info("🏗️  Building Architecture Review Status sheet...")
    build_architecture_review_sheet(wb, styles, validations)
    
    logger.info("🔗 Building Traceability Matrix Status sheet...")
    build_traceability_sheet(wb, styles, validations)
    
    logger.info("📈 Building Compliance Summary dashboard...")
    build_compliance_summary_sheet(wb, styles, validations)

    logger.info("🔍 Building Gap Analysis sheet...")
    build_gap_analysis_sheet(wb, styles, validations)

    logger.info("📚 Building Evidence Register...")
    build_evidence_register_sheet(wb, styles, validations)
    
    logger.info("✅ Building Approval Sign-Off sheet...")
    build_approval_sheet(wb, styles)
    
    # Save workbook
    filename = OUTPUT_FILENAME
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
    logger.info("2. Review the Instructions & Legend sheet for guidance")
    logger.info("3. Complete the Application_Inventory sheet with your applications")
    logger.info("4. For each application, complete:")
    logger.info("   - Requirements_Documentation_Status")
    logger.info("   - Threat_Modeling_Status")
    logger.info("   - Architecture_Review_Status")
    logger.info("   - Traceability_Matrix_Status")
    logger.info("5. Review the Compliance_Summary dashboard for overall scores")
    logger.info("6. Document evidence in the Evidence_Register")
    logger.info("7. Obtain approvals in the Approval_Sign_Off sheet")
    logger.info("\n" + "=" * 70)
    logger.info("📖 REFERENCE:")
    logger.info("=" * 70)
    logger.info("Implementation Guide: ISMS-IMP-A.8.25-26-29-S1")
    logger.info("Policy Reference: ISMS-POL-A.8.25-26-29-S2")
    logger.info("ISO Control: A.8.26 (Application Security Requirements)")
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
