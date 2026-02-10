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
ISMS-IMP-A.8.28.1 - SDLC Integration Assessment
================================================================================

ISO/IEC 27001:2022 Control A.8.28: Secure Coding
Assessment Domain 1 of 4: Secure Development Lifecycle Integration

--------------------------------------------------------------------------------
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR YOUR ORGANIZATION
--------------------------------------------------------------------------------

This script is a TEMPLATE/SAMPLE implementation and MUST be adapted to match
your organization's specific development environment, SDLC methodology, and
assessment requirements.

Key customization areas:
1. SDLC methodology and phases (Agile, Waterfall, DevOps - match your process)
2. Security gate criteria and thresholds (adapt to your risk tolerance)
3. Development tools and platforms (specific to your toolchain)
4. Project types and classifications (based on your portfolio structure)
5. Compliance criteria and scoring (aligned with your regulatory requirements)

DO NOT use this script without reviewing and adapting all sections marked
with "# CUSTOMIZE:" comments throughout the code.

Reference Pattern: Based on ISMS-A.8.28 Secure Coding Assessment Framework

--------------------------------------------------------------------------------
DESCRIPTION
--------------------------------------------------------------------------------

This script generates a comprehensive Excel assessment workbook for evaluating
security integration across all phases of the Software Development Lifecycle.

**Purpose:**
Enables systematic assessment of SDLC security integration against ISO 27001:2022
Control A.8.28 requirements, supporting evidence-based validation of secure
development practices from requirements through deployment.

**Assessment Scope:**
- Security requirements definition and threat modeling processes
- Secure design review and architecture security validation
- Security testing integration (SAST, DAST, SCA, penetration testing)
- Security gate implementation and enforcement mechanisms
- Deployment security controls and production hardening
- Post-deployment monitoring and incident response integration
- Developer security training and awareness programs
- Security champion and SME involvement in SDLC
- Gap analysis and remediation planning
- Evidence collection for audit readiness

**Generated Workbook Structure:**
1. Instructions & Legend - Assessment guidance and SDLC security standards
2. Requirements Phase - Security requirements and threat modeling assessment
3. Design Phase - Secure architecture and design review practices
4. Implementation Phase - Coding standards and secure development practices
5. Testing Phase - Security testing integration and coverage
6. Deployment Phase - Production security controls and hardening
7. Maintenance Phase - Patching, monitoring, and incident response
8. Training & Awareness - Developer security competency assessment
9. Security Gates - Gate effectiveness and enforcement evaluation
10. Gap Analysis - Non-compliant SDLC phases and remediation requirements
11. Evidence Register - Audit evidence tracking and documentation
12. Approval & Sign-Off - Stakeholder review and approval workflow

**Key Features:**
- Data validation with SDLC methodology dropdown lists
- Conditional formatting for security gate compliance status
- Automated gap identification for missing security activities
- Protected formulas with unprotected input cells
- Evidence linkage for audit traceability
- Multi-stakeholder approval workflow
- Integration with project management and CI/CD tool outputs

**Integration:**
This assessment feeds into the A.8.28.5 Compliance Dashboard, which
consolidates data from all four assessment domains for executive
oversight and audit readiness.

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
    - openpyxl >= 3.0.0 (Python Excel library)
    - datetime (standard library)

--------------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------------

Basic Usage:
    python3 generate_a828_1_sdlc_assessment.py

Advanced Usage:
    # Generate with custom output directory
    python3 generate_a828_1_sdlc_assessment.py --output /path/to/dir
    
    # Generate with specific date suffix
    python3 generate_a828_1_sdlc_assessment.py --date 20250124

Output:
    File: ISMS_A_8_28_1_SDLC_Assessment_YYYYMMDD.xlsx
    Location: Current directory (or specified output path)

Post-Generation Steps:
    1. Review and customize SDLC security standards to match your methodology
    2. Inventory all active development projects and their SDLC phases
    3. Complete assessments for each project or development stream
    4. Validate security gate effectiveness against defined criteria
    5. Review developer security training completion and competency
    6. Conduct gap analysis for missing or ineffective security activities
    7. Define remediation actions with timelines and ownership
    8. Collect and link audit evidence (gate approvals, test reports, training records)
    9. Obtain stakeholder approvals (Dev Manager, AppSec Lead, CISO)
    10. Feed results into A.8.28.5 Compliance Dashboard

--------------------------------------------------------------------------------
METADATA
--------------------------------------------------------------------------------

Control Reference:    ISO/IEC 27001:2022 Annex A Control A.8.28
Assessment Domain:    1 of 4 (SDLC Integration)
Framework Version:    1.0
Script Version:       1.0
Author:               [Organization] ISMS Implementation Team
Date:                 DD.MM.YYYY
Last Modified:        DD.MM.YYYY
Python Version:       3.8+
License:              [Organization License/Terms]

Related Documents:
    - ISMS-POL-A.8.28: Secure Coding Policy (Governance)
    - ISMS-IMP-A.8.28.1: SDLC Integration Implementation Guide
    - ISMS-IMP-A.8.28.2: Standards & Tools Assessment (Domain 2)
    - ISMS-IMP-A.8.28.3: Code Review & Testing Assessment (Domain 3)
    - ISMS-IMP-A.8.28.4: Third-Party & OSS Assessment (Domain 4)
    - ISMS-IMP-A.8.28.5: Compliance Dashboard (Consolidation)

Related Scripts:
    - generate_a828_2_standards_tools.py
    - generate_a828_3_code_review_testing.py
    - generate_a828_4_third_party_oss.py
    - generate_a828_5_compliance_dashboard.py
    - normalize_assessment_files_a828.py

--------------------------------------------------------------------------------
CHANGE HISTORY
--------------------------------------------------------------------------------

Version 1.0 - DD.MM.YYYY
    - Initial release
    - Implements full assessment framework per ISMS-IMP-A.8.28.1 specification
    - Supports comprehensive SDLC security integration evaluation
    - Integrated with A.8.28.5 Compliance Dashboard

[Future changes to be documented here]

--------------------------------------------------------------------------------
IMPORTANT NOTES
--------------------------------------------------------------------------------

**SDLC Methodology Adaptation:**
This assessment framework is methodology-agnostic by design. Customize phase
names, security activities, and gate criteria to match your organization's
specific SDLC approach (Agile/Scrum, Waterfall, DevOps, DevSecOps, SAFe, etc.).

**Security Gate Philosophy:**
Security gates should be enabling, not blocking. Focus assessment on whether
gates effectively identify and manage risk, not whether they create bottlenecks.
Overly rigid gates that teams bypass are worse than no gates at all.

**Audit Considerations:**
This assessment generates audit evidence per ISO 27001:2022 requirements.
Ensure all fields are completed accurately and evidence is properly linked.
Auditors will expect verification of security gate approvals, testing results,
and training records.

**Data Protection:**
Assessment workbooks contain sensitive development information including:
- Project names, timelines, and architectures
- Vulnerability information and security gaps
- Development team structures and resource allocation
- Security testing results and penetration test findings

Handle in accordance with your organization's data classification policies.

**Maintenance:**
Review and update assessment:
- Quarterly: Check security gate effectiveness and compliance rates
- Semi-annually: Update security activity requirements for new threats
- Annually: Complete reassessment of all active development projects
- Ad-hoc: When SDLC methodology changes or new security requirements emerge

**Quality Assurance:**
Have application security SMEs, development managers, and security champions
validate assessments before using results for compliance reporting or
remediation decisions.

**Regulatory Alignment:**
Ensure SDLC security standards align with applicable regulatory requirements:
- Payment processing: PCI DSS v4.0.1 secure SDLC requirements (Requirement 6)
- Healthcare: HIPAA application security and risk analysis standards
- Finance: Regional banking application security requirements
- Government: Jurisdiction-specific secure development mandates (e.g., NIST SSDF)

Customize assessment criteria to include regulatory-specific requirements.

**Integration with Development Tools:**
Where possible, integrate assessment data with:
- Project management systems (Jira, Azure DevOps, etc.)
- CI/CD pipeline metrics (Jenkins, GitLab, GitHub Actions)
- Security testing tool outputs (SAST, DAST, SCA results)
- Training platforms (completion tracking, competency scores)

Automated tool integration reduces manual effort and improves accuracy.

**Don't Fool Yourself - Feynman Principle:**
Assess actual SDLC practice, not documented procedures. Just because a security
gate exists on paper doesn't mean it's effective. Look for evidence of:
- Actual gate approvals (not rubber-stamping)
- Real security defects found and fixed
- Developers actually trained (not just registered for courses)
- Threat models that influenced design (not checkbox exercises)

If you can't find evidence it's working, it probably isn't.

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
DOCUMENT_ID = "ISMS-IMP-A.8.28.1"
WORKBOOK_NAME = "Secure Development Lifecycle Integration"
CONTROL_ID = "A.8.28"
CONTROL_NAME = "Secure Coding"
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

# Unicode Constants (for cross-platform compatibility)
CHECK_MARK = "\u2705"      # ✅
CROSS_MARK = "\u274C"      # ❌
WARNING = "\u26A0"         # ⚠️
CLIPBOARD = "\u1F4CB"      # 📋
TRIANGLE = "\u25B8"        # ▸
BULLET = "\u2022"          # •

import sys


# ============================================================================
# SECTION 1: WORKBOOK CREATION & STYLE DEFINITIONS
# ============================================================================

def create_workbook() -> Workbook:
    """Create workbook with all required sheets matching IMP specification."""
    wb = Workbook()

    # Remove default sheet
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])

    # Sheet structure matches ISMS-IMP-A.8.28.1 specification
    # 10 sheets total: Instructions + 5 assessment domains + 4 supporting sheets
    sheets = [
        "Instructions",
        "Security Requirements Design",
        "Development Environment",
        "Build Deployment Pipeline",
        "Security Testing Integration",
        "Release Change Management",
        "Summary Dashboard",
        "Evidence Register",
        "Gap Analysis",
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
    
    Following Feynman's principle: "The first principle is that you must not 
    fool yourself—and you are the easiest person to fool." We don't fool Excel
    with shared style objects that cause repair warnings.
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
        "section_header": {
            "font": Font(name="Calibri", size=11, bold=True, color="FFFFFF"),
            "fill": PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid"),
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
            "alignment": Alignment(horizontal="left", vertical="top", wrap_text=True),
            "border": border_thin,
        },
        "data_cell": {
            "alignment": Alignment(horizontal="left", vertical="top", wrap_text=True),
            "border": border_thin,
        },
        "border": border_thin,
        "status_implemented": {
            "fill": PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
        },
        "status_partial": {
            "fill": PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
        },
        "status_notimplemented": {
            "fill": PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
        },
        "status_na": {
            "fill": PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        },
        "priority_critical": {
            "font": Font(name="Calibri", size=10, bold=True, color="FFFFFF"),
            "fill": PatternFill(start_color="C00000", end_color="C00000", fill_type="solid"),
        },
        "priority_high": {
            "fill": PatternFill(start_color="FF6666", end_color="FF6666", fill_type="solid"),
        },
        "priority_medium": {
            "fill": PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid"),
        },
        "priority_low": {
            "fill": PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid"),
        },
    }
    return styles


def apply_style(cell, style_dict):
    """
    Apply style dictionary to a cell.
    Creates NEW style objects to avoid shared object warnings.
    
    This is cargo cult done right: we follow the ritual of creating new objects
    not because we worship Excel's quirks, but because we understand why
    shared style objects cause corruption.
    """
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
    These are added to worksheet once, then applied to multiple cells.
    
    Data validations ensure consistency and reduce user error - this is
    not cargo cult, it's user interface design.
    """
    validations = {
        # Implementation status dropdowns
        'implementation_status': DataValidation(
            type="list",
            formula1='"Implemented,Partially Implemented,Not Implemented,N/A"',
            allow_blank=False
        ),
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
            formula1='"Yes,No,Partial,Unknown"',
            allow_blank=False
        ),
        'yes_no_planned': DataValidation(
            type="list",
            formula1='"Yes,No,Planned,N/A"',
            allow_blank=False
        ),
        
        # Priority and risk levels
        'priority': DataValidation(
            type="list",
            formula1='"Critical,High,Medium,Low"',
            allow_blank=False
        ),
        'risk_level': DataValidation(
            type="list",
            formula1='"Critical,High,Medium,Low,Negligible"',
            allow_blank=False
        ),
        
        # Gap analysis statuses
        'gap_status': DataValidation(
            type="list",
            formula1='"Open,In Progress,Resolved,Closed,Deferred"',
            allow_blank=False
        ),
        
        # Evidence types
        'evidence_type': DataValidation(
            type="list",
            formula1='"Document,Screenshot,Report,Configuration,URL,Log File,Diagram,Policy,Procedure,Test Result,Scan Result,Other"',
            allow_blank=False
        ),
        
        # Verification status
        'verification_status': DataValidation(
            type="list",
            formula1='"Verified,Pending,Not Verified,N/A"',
            allow_blank=False
        ),
        
        # Approval decision
        'approval_decision': DataValidation(
            type="list",
            formula1='"Approved,Approved with Conditions,Rejected,Pending Review"',
            allow_blank=False
        ),
        
        # SDLC phase
        'sdlc_phase': DataValidation(
            type="list",
            formula1='"Requirements,Design,Development,Testing,Deployment,Maintenance"',
            allow_blank=False
        ),
        
        # Tool category
        'tool_category': DataValidation(
            type="list",
            formula1='"SAST,SCA,DAST,Secret Scanner,Container Scanner,IaC Scanner,IDE Plugin,Other"',
            allow_blank=False
        ),
        
        # Testing type
        'testing_type': DataValidation(
            type="list",
            formula1='"Unit,Integration,API,Security,Penetration,Performance,Regression"',
            allow_blank=False
        ),
        
        # Frequency
        'frequency': DataValidation(
            type="list",
            formula1='"Continuous,Daily,Weekly,Monthly,Quarterly,On-Demand"',
            allow_blank=False
        ),
        
        # Maturity level
        'maturity_level': DataValidation(
            type="list",
            formula1='"Initial,Repeatable,Defined,Managed,Optimizing"',
            allow_blank=False
        ),
        
        # Training status
        'training_status': DataValidation(
            type="list",
            formula1='"Completed,In Progress,Not Started,N/A"',
            allow_blank=False
        ),
        
        # Deployment environment
        'environment': DataValidation(
            type="list",
            formula1='"Development,Testing,Staging,Production,All"',
            allow_blank=False
        ),
        
        # Automation level
        'automation_level': DataValidation(
            type="list",
            formula1='"Fully Automated,Partially Automated,Manual,Not Applicable"',
            allow_blank=False
        ),
        
        # Compliance level
        'compliance_level': DataValidation(
            type="list",
            formula1='"Fully Compliant,Mostly Compliant,Partially Compliant,Non-Compliant,N/A"',
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
# SECTION 3: ASSESSMENT DOMAIN DATA DEFINITIONS
# ============================================================================

def get_domain1_requirements():
    """
    Domain 1: Security Requirements & Design
    
    This domain assesses whether security is "baked in" from the start,
    not bolted on later. As Feynman might say: "If you can't specify 
    security requirements upfront, you're just fooling yourself about 
    having a secure development process."
    """
    return [
        {
            "id": "1.1",
            "requirement": "Security requirements are documented for all new development projects",
            "evidence": "Requirements documents, user stories with security acceptance criteria, requirements management system records",
            "category": "Requirements Definition"
        },
        {
            "id": "1.2",
            "requirement": "Threat modeling is performed for high-risk applications before implementation",
            "evidence": "Threat model documents, STRIDE analysis, attack trees, threat modeling session notes",
            "category": "Requirements Definition"
        },
        {
            "id": "1.3",
            "requirement": "Security design reviews are conducted before implementation begins",
            "evidence": "Architecture review meeting notes, approved design documents, security sign-off records",
            "category": "Design Review"
        },
        {
            "id": "1.4",
            "requirement": "Authentication and authorization requirements are defined upfront for all applications",
            "evidence": "Security specifications, access control matrices, identity management requirements",
            "category": "Requirements Definition"
        },
        {
            "id": "1.5",
            "requirement": "Data classification is performed for all data handled by applications",
            "evidence": "Data classification register, data flow diagrams, data handling requirements",
            "category": "Requirements Definition"
        },
        {
            "id": "1.6",
            "requirement": "Cryptographic requirements are specified when sensitive data is involved",
            "evidence": "Crypto standards documentation, algorithm approval records, key management specs",
            "category": "Requirements Definition"
        },
        {
            "id": "1.7",
            "requirement": "Security requirements are tracked throughout the entire SDLC",
            "evidence": "Requirement traceability matrix, ticket system reports, requirements coverage metrics",
            "category": "Requirements Management"
        },
        {
            "id": "1.8",
            "requirement": "Privacy requirements (GDPR, CCPA, etc.) are incorporated into design phase",
            "evidence": "Privacy impact assessments, data protection by design documentation, consent mechanisms",
            "category": "Requirements Definition"
        },
        {
            "id": "1.9",
            "requirement": "Secure coding standards are referenced in all project documentation",
            "evidence": "Project wikis, coding guidelines links, onboarding documentation",
            "category": "Design Review"
        },
        {
            "id": "1.10",
            "requirement": "Security acceptance criteria are defined for all user stories and features",
            "evidence": "JIRA/Azure DevOps stories with security DoD, acceptance criteria templates",
            "category": "Requirements Definition"
        },
        {
            "id": "1.11",
            "requirement": "API security requirements are documented for all APIs (internal and external)",
            "evidence": "API security specifications, OpenAPI security schemes, API gateway policies",
            "category": "Requirements Definition"
        },
        {
            "id": "1.12",
            "requirement": "Third-party integration security is assessed during design phase",
            "evidence": "Vendor security assessments, integration security reviews, API security analysis",
            "category": "Design Review"
        },
        {
            "id": "1.13",
            "requirement": "Error handling and logging requirements are specified in design",
            "evidence": "Logging standards, error handling patterns documentation, log retention policies",
            "category": "Design Review"
        },
        {
            "id": "1.14",
            "requirement": "Security testing requirements are defined before development starts",
            "evidence": "Test plans, security test case specifications, testing strategy documents",
            "category": "Requirements Definition"
        },
        {
            "id": "1.15",
            "requirement": "Compliance requirements are mapped to technical controls in design",
            "evidence": "Compliance mapping documents, control implementation matrix, regulatory requirements docs",
            "category": "Requirements Definition"
        },
        {
            "id": "1.16",
            "requirement": "Security Champions are involved in requirements and design review",
            "evidence": "Review meeting attendance, Security Champion feedback records, design review checklists",
            "category": "Design Review"
        },
        {
            "id": "1.17",
            "requirement": "Secure design patterns are documented and promoted for common scenarios",
            "evidence": "Design pattern library, secure architecture templates, reference architectures",
            "category": "Design Review"
        },
        {
            "id": "1.18",
            "requirement": "Security requirements are risk-based and proportional to data sensitivity",
            "evidence": "Risk assessment documentation, security control selection justification",
            "category": "Requirements Definition"
        },
    ]


def get_domain2_requirements():
    """
    Domain 2: Development Environment & Tooling
    
    The development environment is where vulnerabilities are often introduced.
    Proper tooling and configuration prevents many security issues before
    they reach production.
    """
    return [
        {
            "id": "2.1",
            "requirement": "Development environments are logically isolated from production systems",
            "evidence": "Network diagrams, firewall rules, network segmentation documentation",
            "category": "Environment Security"
        },
        {
            "id": "2.2",
            "requirement": "Developer workstations have mandatory security tooling installed (EDR, DLP, etc.)",
            "evidence": "EDR deployment reports, endpoint security compliance dashboards, security agent status",
            "category": "Workstation Security"
        },
        {
            "id": "2.3",
            "requirement": "IDE security plugins are available and promoted to all developers",
            "evidence": "IDE plugin catalog, installation instructions, adoption metrics",
            "category": "Development Tools"
        },
        {
            "id": "2.4",
            "requirement": "Pre-commit hooks prevent secret commits to version control",
            "evidence": "Git hooks configuration, secret scanner setup (git-secrets, detect-secrets), violation reports",
            "category": "Development Tools"
        },
        {
            "id": "2.5",
            "requirement": "Code repositories require authentication and authorization (SSO/MFA)",
            "evidence": "GitHub/GitLab access logs, SSO configuration, MFA enforcement policies",
            "category": "Repository Security"
        },
        {
            "id": "2.6",
            "requirement": "Branch protection rules enforce mandatory peer review for production branches",
            "evidence": "Repository settings screenshots, branch protection rules configuration, merge policies",
            "category": "Repository Security"
        },
        {
            "id": "2.7",
            "requirement": "Development and testing use anonymized or synthetic data (not production data)",
            "evidence": "Data masking procedures, test data generation tools, data usage policies",
            "category": "Environment Security"
        },
        {
            "id": "2.8",
            "requirement": "Secrets management solution is available and documented for developers",
            "evidence": "Vault/secrets manager documentation, developer usage guidelines, secrets rotation policies",
            "category": "Development Tools"
        },
        {
            "id": "2.9",
            "requirement": "Local development environments use HTTPS/TLS where applicable",
            "evidence": "Development proxy configs, local cert management, TLS enforcement policies",
            "category": "Environment Security"
        },
        {
            "id": "2.10",
            "requirement": "Dependency management tools scan for vulnerabilities in developer environments",
            "evidence": "npm audit, pip-audit, Dependabot integration, vulnerability scan results",
            "category": "Development Tools"
        },
        {
            "id": "2.11",
            "requirement": "Development environment hardening guidelines exist and are enforced",
            "evidence": "Developer workstation security baseline, configuration management records",
            "category": "Workstation Security"
        },
        {
            "id": "2.12",
            "requirement": "Multi-factor authentication (MFA) is enforced for all code repository access",
            "evidence": "MFA enforcement policies, authentication logs, MFA adoption metrics",
            "category": "Repository Security"
        },
        {
            "id": "2.13",
            "requirement": "Development tools and IDEs are kept up-to-date with security patches",
            "evidence": "Tool version inventory, patch management records, software update policies",
            "category": "Development Tools"
        },
        {
            "id": "2.14",
            "requirement": "Secure coding training resources are accessible to all developers",
            "evidence": "Training portal links, OWASP resources, internal wiki, training completion records",
            "category": "Training & Awareness"
        },
        {
            "id": "2.15",
            "requirement": "Development containers/VMs use secure, hardened base images",
            "evidence": "Approved image catalog, image scanning results, base image security standards",
            "category": "Environment Security"
        },
        {
            "id": "2.16",
            "requirement": "Code repository activity is logged and monitored for anomalies",
            "evidence": "Repository audit logs, SIEM integration, anomaly detection alerts",
            "category": "Repository Security"
        },
        {
            "id": "2.17",
            "requirement": "Personal access tokens and API keys have expiration policies",
            "evidence": "Token lifecycle policies, key rotation procedures, token expiration reports",
            "category": "Development Tools"
        },
        {
            "id": "2.18",
            "requirement": "Developers have access to security documentation and secure code examples",
            "evidence": "Internal security wiki, code example repository, secure coding cheat sheets",
            "category": "Training & Awareness"
        },
    ]


def get_domain3_requirements():
    """
    Domain 3: Build & Deployment Pipeline
    
    The CI/CD pipeline is the assembly line where security checks happen
    automatically. If it's not in the pipeline, it doesn't happen consistently.
    """
    return [
        {
            "id": "3.1",
            "requirement": "CI/CD pipelines enforce automated security checks on every build",
            "evidence": "Pipeline configuration files (Jenkinsfile, .gitlab-ci.yml), build logs showing security scans",
            "category": "Pipeline Security"
        },
        {
            "id": "3.2",
            "requirement": "SAST (Static Application Security Testing) tools are integrated into build pipeline",
            "evidence": "SAST scan results, tool integration config (SonarQube, Semgrep, Checkmarx)",
            "category": "Security Scanning"
        },
        {
            "id": "3.3",
            "requirement": "SCA (Software Composition Analysis) tools scan dependencies during every build",
            "evidence": "SCA scan reports (Snyk, WhiteSource, Dependency-Check), vulnerability alerts",
            "category": "Security Scanning"
        },
        {
            "id": "3.4",
            "requirement": "Secret scanning runs automatically on every commit",
            "evidence": "Secret scanner logs (TruffleHog, GitGuardian), detected secret alerts, remediation records",
            "category": "Security Scanning"
        },
        {
            "id": "3.5",
            "requirement": "Build artifacts are signed and signature verification is enforced",
            "evidence": "Code signing certificates, artifact signatures, signature verification logs",
            "category": "Artifact Security"
        },
        {
            "id": "3.6",
            "requirement": "Container images are scanned for vulnerabilities before deployment",
            "evidence": "Trivy/Clair/Anchore scan results, image vulnerability reports, scan policies",
            "category": "Security Scanning"
        },
        {
            "id": "3.7",
            "requirement": "Infrastructure-as-Code (IaC) is scanned for security misconfigurations",
            "evidence": "Checkov/tfsec/Terrascan results, IaC security scan reports, policy violations",
            "category": "Security Scanning"
        },
        {
            "id": "3.8",
            "requirement": "Build pipelines fail on critical or high severity vulnerabilities",
            "evidence": "Pipeline failure logs, quality gate configuration, vulnerability threshold policies",
            "category": "Pipeline Security"
        },
        {
            "id": "3.9",
            "requirement": "Deployment to production requires explicit approval",
            "evidence": "Approval workflows, deployment gate records, approval audit logs",
            "category": "Deployment Controls"
        },
        {
            "id": "3.10",
            "requirement": "Pipeline service accounts use least-privilege access principles",
            "evidence": "Service account permissions, IAM policies, privilege reviews",
            "category": "Pipeline Security"
        },
        {
            "id": "3.11",
            "requirement": "Build environments are ephemeral and disposable (not persistent)",
            "evidence": "Build agent lifecycle documentation, container/VM configs, environment refresh logs",
            "category": "Pipeline Security"
        },
        {
            "id": "3.12",
            "requirement": "Pipeline configurations are version-controlled and peer-reviewed",
            "evidence": "CI/CD config files in git, change history, pipeline review records",
            "category": "Pipeline Security"
        },
        {
            "id": "3.13",
            "requirement": "Security scan results are archived and historically trackable",
            "evidence": "Scan result storage, historical trend reports, vulnerability tracking database",
            "category": "Security Scanning"
        },
        {
            "id": "3.14",
            "requirement": "Rollback procedures are tested and documented",
            "evidence": "Rollback runbooks, rollback test results, disaster recovery procedures",
            "category": "Deployment Controls"
        },
        {
            "id": "3.15",
            "requirement": "Deployment logs are sent to centralised logging/SIEM",
            "evidence": "SIEM integration, deployment audit logs, log retention policies",
            "category": "Deployment Controls"
        },
        {
            "id": "3.16",
            "requirement": "Pipeline secrets are managed securely (not hardcoded in configs)",
            "evidence": "Secrets management integration, vault usage, secret rotation logs",
            "category": "Pipeline Security"
        },
        {
            "id": "3.17",
            "requirement": "Build reproducibility is ensured (deterministic builds where possible)",
            "evidence": "Build reproducibility documentation, dependency pinning, lockfiles",
            "category": "Artifact Security"
        },
        {
            "id": "3.18",
            "requirement": "Failed security scans trigger notifications to security team",
            "evidence": "Alert configuration, notification logs, incident escalation procedures",
            "category": "Security Scanning"
        },
    ]


def get_domain4_requirements():
    """
    Domain 4: Security Testing Integration
    
    Testing is where we validate that our security controls actually work.
    Without testing, security is just wishful thinking.
    """
    return [
        {
            "id": "4.1",
            "requirement": "Security test cases are written for all critical functionality",
            "evidence": "Security test suite, test case repository, test coverage reports",
            "category": "Test Planning"
        },
        {
            "id": "4.2",
            "requirement": "Unit tests include security-focused test cases (input validation, etc.)",
            "evidence": "Unit test suites with security tests, code coverage reports",
            "category": "Unit Testing"
        },
        {
            "id": "4.3",
            "requirement": "Integration tests validate authentication and authorization mechanisms",
            "evidence": "Integration test suites, auth test results, test scenarios",
            "category": "Integration Testing"
        },
        {
            "id": "4.4",
            "requirement": "DAST (Dynamic Application Security Testing) runs against staging environments",
            "evidence": "DAST scan reports (OWASP ZAP, Burp Suite, Acunetix), vulnerability findings",
            "category": "Dynamic Testing"
        },
        {
            "id": "4.5",
            "requirement": "API security testing is performed (fuzzing, schema validation, injection tests)",
            "evidence": "API test results, fuzzing reports, Postman/REST Assured test suites",
            "category": "API Testing"
        },
        {
            "id": "4.6",
            "requirement": "Penetration testing is conducted for high-risk applications annually",
            "evidence": "Pentest reports, findings tracking, remediation validation",
            "category": "Penetration Testing"
        },
        {
            "id": "4.7",
            "requirement": "Security regression tests prevent reintroduction of known vulnerabilities",
            "evidence": "Regression test suite, vulnerability fix validation tests",
            "category": "Regression Testing"
        },
        {
            "id": "4.8",
            "requirement": "Test environments mirror production security configurations",
            "evidence": "Environment parity documentation, configuration comparisons",
            "category": "Test Environment"
        },
        {
            "id": "4.9",
            "requirement": "Automated security tests run in CI/CD pipeline on every build",
            "evidence": "Pipeline test execution logs, automated test results",
            "category": "Test Automation"
        },
        {
            "id": "4.10",
            "requirement": "Security testing results are reviewed before release approval",
            "evidence": "Release gate checklists, security sign-off records, test result reviews",
            "category": "Test Planning"
        },
        {
            "id": "4.11",
            "requirement": "Performance testing includes assessment of security control overhead",
            "evidence": "Load test results with security controls enabled, performance baselines",
            "category": "Performance Testing"
        },
        {
            "id": "4.12",
            "requirement": "Bug bounty or responsible disclosure program provides external testing",
            "evidence": "Bug bounty platform reports (HackerOne, Bugcrowd), vulnerability submissions",
            "category": "External Testing"
        },
        {
            "id": "4.13",
            "requirement": "Security Champions participate in test planning and review",
            "evidence": "Test planning meeting notes, Security Champion involvement records",
            "category": "Test Planning"
        },
        {
            "id": "4.14",
            "requirement": "Failed security tests block deployment to production",
            "evidence": "Quality gate configuration, blocked deployment logs, override procedures",
            "category": "Test Automation"
        },
        {
            "id": "4.15",
            "requirement": "Security test coverage is measured and tracked over time",
            "evidence": "Coverage metrics, security test inventory, trend analysis",
            "category": "Test Planning"
        },
        {
            "id": "4.16",
            "requirement": "Authentication and session management are thoroughly tested",
            "evidence": "Auth test scenarios, session security tests, credential handling tests",
            "category": "Integration Testing"
        },
        {
            "id": "4.17",
            "requirement": "Input validation testing covers all user input vectors",
            "evidence": "Input validation test cases, injection testing results, fuzzing outputs",
            "category": "API Testing"
        },
        {
            "id": "4.18",
            "requirement": "Security test data is maintained separately from production data",
            "evidence": "Test data management procedures, synthetic data generation tools",
            "category": "Test Environment"
        },
    ]


def get_domain5_requirements():
    """
    Domain 5: Release & Change Management
    
    The final gate before production. This is where we ensure that all
    security checks have passed and changes are controlled.
    """
    return [
        {
            "id": "5.1",
            "requirement": "Security review is mandatory for all production releases",
            "evidence": "Release checklists with security sign-off, security review records",
            "category": "Release Process"
        },
        {
            "id": "5.2",
            "requirement": "Release notes document all security-relevant changes",
            "evidence": "Release notes, change logs with security tags, security update notifications",
            "category": "Release Documentation"
        },
        {
            "id": "5.3",
            "requirement": "Emergency hotfix process includes security assessment",
            "evidence": "Hotfix procedures, emergency change records, security review logs",
            "category": "Change Management"
        },
        {
            "id": "5.4",
            "requirement": "Rollback plans are prepared and tested for all production releases",
            "evidence": "Rollback procedures, rollback test results, disaster recovery plans",
            "category": "Release Process"
        },
        {
            "id": "5.5",
            "requirement": "Post-deployment verification includes security checks",
            "evidence": "Smoke test results, security validation logs, post-deployment checklists",
            "category": "Release Process"
        },
        {
            "id": "5.6",
            "requirement": "Security patches are prioritised and tracked with defined SLAs",
            "evidence": "Security patch SLA, vulnerability remediation tracker, patching metrics",
            "category": "Patch Management"
        },
        {
            "id": "5.7",
            "requirement": "Configuration changes follow formal change management process",
            "evidence": "Change requests, CAB approval records, configuration change logs",
            "category": "Change Management"
        },
        {
            "id": "5.8",
            "requirement": "Production access is logged, monitored, and reviewed",
            "evidence": "Production access logs, privileged access monitoring, access reviews",
            "category": "Access Control"
        },
        {
            "id": "5.9",
            "requirement": "Feature flags enable controlled rollout of security features",
            "evidence": "Feature flag configurations, gradual rollout plans, feature toggle logs",
            "category": "Release Process"
        },
        {
            "id": "5.10",
            "requirement": "Security metrics are collected and reviewed post-release",
            "evidence": "Post-release security reports, incident metrics, security KPI dashboards",
            "category": "Release Documentation"
        },
        {
            "id": "5.11",
            "requirement": "Communication plan exists for security-relevant releases",
            "evidence": "Communication templates, stakeholder notification logs, security bulletins",
            "category": "Release Documentation"
        },
        {
            "id": "5.12",
            "requirement": "Release frequency balances security needs with business velocity",
            "evidence": "Release calendar, security vs. feature delivery metrics, deployment frequency",
            "category": "Release Process"
        },
        {
            "id": "5.13",
            "requirement": "Post-incident releases are tracked and undergo enhanced scrutiny",
            "evidence": "Incident-driven release logs, security fix tracking, post-incident reviews",
            "category": "Patch Management"
        },
        {
            "id": "5.14",
            "requirement": "Compliance artifacts are updated with each relevant release",
            "evidence": "Compliance documentation updates, attestation records, audit trail",
            "category": "Release Documentation"
        },
        {
            "id": "5.15",
            "requirement": "Lessons learned from security issues feed into process improvements",
            "evidence": "Retrospective notes, security improvement backlog, process change records",
            "category": "Continuous Improvement"
        },
        {
            "id": "5.16",
            "requirement": "Release approvals require sign-off from security stakeholders",
            "evidence": "Approval workflow records, security sign-off documentation",
            "category": "Release Process"
        },
        {
            "id": "5.17",
            "requirement": "Version control and release tags are properly maintained",
            "evidence": "Git tags, release versioning records, artifact version tracking",
            "category": "Release Documentation"
        },
        {
            "id": "5.18",
            "requirement": "Security scan results are archived with release artifacts",
            "evidence": "Scan result archives, release documentation bundles, compliance packages",
            "category": "Release Documentation"
        },
    ]

# ============================================================================
# SECTION 4: INSTRUCTIONS SHEET CREATION
# ============================================================================

def create_instructions_sheet(ws, styles):
    """
    Create comprehensive Instructions sheet with guidance, legend, and examples.
    
    This is the user's first interaction with the workbook - make it count.
    Clear instructions prevent confusion and reduce the "cargo cult" effect
    of people just filling in boxes without understanding why.
    """
    
    # Header
    ws.merge_cells("A1:F1")
    ws["A1"] = "ISMS-IMP-A.8.28.1 – SDLC Assessment"
    apply_style(ws["A1"], styles["header"])
    ws.row_dimensions[1].height = 30

    ws.merge_cells("A2:F2")
    ws["A2"] = "ISO/IEC 27001:2022 - Control A.8.28: Secure Coding (SDLC)"
    apply_style(ws["A2"], styles["subheader"])
    ws.row_dimensions[2].height = 20

    # Document Information Block
    row = 4
    ws[f"A{row}"] = "DOCUMENT INFORMATION"
    ws[f"A{row}"].font = Font(bold=True, size=11, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    ws.merge_cells(f"A{row}:F{row}")
    
    doc_info = [
        ("Document ID:", "ISMS-IMP-A.8.28.1"),
        ("Assessment Area:", "Secure Software Development Lifecycle"),
        ("Related Policy:", "ISMS-POL-A.8.28-S2.1 (SDLC Requirements)"),
        ("Version:", "1.0"),
        ("Assessment Date:", "[USER INPUT - Enter assessment date]"),
        ("Completed By:", "[USER INPUT - Enter assessor name]"),
        ("Organisation:", "[USER INPUT - Enter organisation name]"),
        ("Review Cycle:", "Quarterly or when SDLC processes change"),
    ]
    
    row += 1
    for label, value in doc_info:
        ws[f"A{row}"] = label
        ws[f"A{row}"].font = Font(bold=True, size=10)
        ws[f"B{row}"] = value
        if "USER INPUT" in value:
            ws[f"B{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
            ws[f"B{row}"].font = Font(italic=True, size=10)
        ws.merge_cells(f"B{row}:F{row}")
        row += 1

    # How to Use This Workbook
    row += 2
    ws.merge_cells(f"A{row}:F{row}")
    ws[f"A{row}"] = "HOW TO USE THIS WORKBOOK"
    ws[f"A{row}"].font = Font(bold=True, size=12, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[row].height = 25

    instructions = [
        "1. Complete each assessment domain sheet sequentially (Security Requirements → Development Environment → Build Pipeline → Security Testing → Release Management)",
        "2. For each requirement, select Implementation Status from dropdown menu",
        "3. Provide Evidence Reference - document WHERE the evidence can be found (URL, file path, system name)",
        "4. Add Comments explaining implementation details, exceptions, or context",
        "5. Review the Summary Dashboard to see overall compliance metrics",
        "6. Document all gaps in the Gap Analysis sheet with remediation plans",
        "7. Maintain the Evidence Register for comprehensive audit trail",
        "8. Obtain required approvals on the Approval Sign-Off sheet",
        "",
        "\u26A0\uFE0F  IMPORTANT: This is a TECHNICAL assessment. Focus on what is ACTUALLY implemented, not what is planned or documented.",
        "   As Feynman said: 'The first principle is that you must not fool yourself—and you are the easiest person to fool.'",
    ]

    row += 1
    for instruction in instructions:
        ws[f"A{row}"] = instruction
        ws[f"A{row}"].alignment = Alignment(wrap_text=True, vertical="top")
        ws.merge_cells(f"A{row}:F{row}")
        if instruction.startswith("\u26A0\uFE0F"):
            ws[f"A{row}"].font = Font(bold=True, size=10, color="C00000")
        ws.row_dimensions[row].height = 30 if len(instruction) > 100 else 20
        row += 1

    # Assessment Domains Overview
    row += 2
    ws.merge_cells(f"A{row}:F{row}")
    ws[f"A{row}"] = "ASSESSMENT DOMAINS"
    ws[f"A{row}"].font = Font(bold=True, size=12, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")

    row += 1
    ws[f"A{row}"] = "Domain"
    ws[f"B{row}"] = "Focus Area"
    ws[f"C{row}"] = "Requirements"
    for col in ["A", "B", "C"]:
        ws[f"{col}{row}"].font = Font(bold=True)
        ws[f"{col}{row}"].fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")

    domain_overview = [
        ("1. Security Requirements & Design", "Threat modeling, security requirements, design reviews", "18"),
        ("2. Development Environment & Tooling", "Developer workstations, IDE plugins, repository security", "18"),
        ("3. Build & Deployment Pipeline", "CI/CD security, SAST/SCA/DAST, artifact signing", "18"),
        ("4. Security Testing Integration", "Unit/integration/API testing, pentest, bug bounty", "18"),
        ("5. Release & Change Management", "Release approval, patching, post-deployment verification", "18"),
    ]

    row += 1
    for domain, focus, req_count in domain_overview:
        ws[f"A{row}"] = domain
        ws[f"B{row}"] = focus
        ws[f"C{row}"] = req_count
        ws[f"C{row}"].alignment = Alignment(horizontal="center")
        ws.merge_cells(f"B{row}:F{row}")
        row += 1

    ws[f"C{row}"] = "90 Total"
    ws[f"C{row}"].font = Font(bold=True)
    ws[f"C{row}"].alignment = Alignment(horizontal="center")

    # Implementation Status Legend
    row += 3
    ws.merge_cells(f"A{row}:F{row}")
    ws[f"A{row}"] = "IMPLEMENTATION STATUS LEGEND"
    ws[f"A{row}"].font = Font(bold=True, size=12, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")

    row += 1
    legend_headers = ["Status", "Symbol", "Description", "When to Use"]
    for col_idx, header in enumerate(legend_headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=header)
        cell.font = Font(bold=True)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")

    legend_data = [
        ("Implemented", "\u2705", "Requirement fully implemented and operational", "When the control is working as intended with evidence"),
        ("Partially Implemented", "\u26A0\uFE0F", "Requirement partially met or limited coverage", "When control exists but has gaps or incomplete coverage"),
        ("Not Implemented", "\u274C", "Requirement not implemented", "When control does not exist or is not functional"),
        ("N/A", "N/A", "Not applicable to this environment", "When requirement genuinely does not apply (rare - be cautious)"),
    ]

    row += 1
    for status, symbol, desc, when_use in legend_data:
        ws[f"A{row}"] = status
        ws[f"A{row}"].font = Font(bold=True)
        ws[f"B{row}"] = symbol
        ws[f"C{row}"] = desc
        ws[f"D{row}"] = when_use
        
        # Apply color coding to status cell
        if status == "Implemented":
            ws[f"A{row}"].fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
        elif status == "Partially Implemented":
            ws[f"A{row}"].fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
        elif status == "Not Implemented":
            ws[f"A{row}"].fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
        elif status == "N/A":
            ws[f"A{row}"].fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        
        ws.merge_cells(f"C{row}:F{row}")
        ws[f"C{row}"].alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[row].height = 30
        row += 1

    # Acceptable Evidence Examples
    row += 2
    ws.merge_cells(f"A{row}:F{row}")
    ws[f"A{row}"] = "ACCEPTABLE EVIDENCE (Examples)"
    ws[f"A{row}"].font = Font(bold=True, size=12, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")

    evidence_examples = [
        "✓ SDLC documentation (process flows, procedures, developer guides)",
        "✓ Tool configurations (CI/CD pipelines, security scanner settings)",
        "✓ Scan results (SAST/SCA/DAST reports with timestamps)",
        "✓ Code repository settings (branch protection rules, access controls)",
        "✓ Training records (security training completion, attendance logs)",
        "✓ Architecture diagrams (threat models, security design reviews)",
        "✓ Meeting notes (design review meetings, security champion sessions)",
        "✓ Policy documents (secure coding standards, security policies)",
        "✓ Audit logs (access logs, deployment logs, security events)",
        "✓ Test results (security test execution, penetration test reports)",
        "✓ Approval records (release approvals, security sign-offs)",
        "✓ Incident reports (security incidents, lessons learned)",
        "✓ Metrics dashboards (vulnerability trends, security KPIs)",
        "✓ Configuration files (git hooks, IDE plugins, tool configs)",
        "✓ Screenshots (tool outputs, dashboard views, configurations)",
    ]

    row += 1
    for evidence in evidence_examples:
        ws[f"A{row}"] = evidence
        ws[f"A{row}"].alignment = Alignment(wrap_text=True)
        ws.merge_cells(f"A{row}:F{row}")
        row += 1

    # Common Pitfalls to Avoid
    row += 2
    ws.merge_cells(f"A{row}:F{row}")
    ws[f"A{row}"] = "COMMON PITFALLS TO AVOID"
    ws[f"A{row}"].font = Font(bold=True, size=12, color="FFFFFF")
    ws[f"A{row}"].fill = PatternFill(start_color="C00000", end_color="C00000", fill_type="solid")
    ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")

    pitfalls = [
        "\u274C Marking something 'Implemented' because it's documented - documentation ≠ implementation",
        "\u274C Using 'N/A' as a way to avoid difficult assessments - be honest about gaps",
        "\u274C Providing vague evidence like 'in our wiki' - give specific links or locations",
        "\u274C Confusing 'we plan to do this' with 'we do this' - plans don't count",
        "\u274C Rating based on what the tool CAN do vs. what is ACTUALLY configured",
        "\u274C Assuming developers follow guidelines without evidence of enforcement",
        "\u274C Marking 'Implemented' for tools that exist but aren't actually used",
        "\u274C Ignoring technical debt - 'we know it's bad but...' means Not Implemented",
    ]

    row += 1
    for pitfall in pitfalls:
        ws[f"A{row}"] = pitfall
        ws[f"A{row}"].font = Font(size=10, color="C00000")
        ws[f"A{row}"].alignment = Alignment(wrap_text=True)
        ws.merge_cells(f"A{row}:F{row}")
        ws.row_dimensions[row].height = 25
        row += 1

    # Column widths
    ws.column_dimensions["A"].width = 25
    ws.column_dimensions["B"].width = 25
    ws.column_dimensions["C"].width = 35
    ws.column_dimensions["D"].width = 35
    ws.column_dimensions["E"].width = 20
    ws.column_dimensions["F"].width = 20

    ws.freeze_panes = "A4"


# ============================================================================
# SECTION 5: DOMAIN ASSESSMENT SHEET CREATION
# ============================================================================

def create_domain_sheet(ws, domain_name, requirements, styles):
    """
    Create a standardized assessment domain sheet.
    
    Each domain sheet follows the same structure:
    - Header row with column names
    - Assessment items with ID, Requirement, Status dropdown, Evidence, Comments
    - Compliance indicator (auto-calculated based on status)
    
    Args:
        ws: Worksheet object
        domain_name: Display name for the domain
        requirements: List of requirement dictionaries
        styles: Style templates dictionary
    """
    validations = create_base_validations(ws)
    
    # Header
    ws.merge_cells("A1:F1")
    ws["A1"] = f"SDLC Assessment: {domain_name}"
    apply_style(ws["A1"], styles["header"])
    ws.row_dimensions[1].height = 30

    # Column headers
    headers = [
        "ID",
        "Requirement",
        "Implementation Status",
        "Evidence Reference",
        "Comments",
        "Compliance"
    ]
    
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=2, column=col_num, value=header)
        apply_style(cell, styles["column_header"])
    
    ws.row_dimensions[2].height = 30

    # Column widths
    ws.column_dimensions["A"].width = 8
    ws.column_dimensions["B"].width = 55
    ws.column_dimensions["C"].width = 22
    ws.column_dimensions["D"].width = 35
    ws.column_dimensions["E"].width = 40
    ws.column_dimensions["F"].width = 12

    # Requirements data
    current_category = None
    row = 3
    
    for req in requirements:
        # Insert category header if new category
        if "category" in req and req["category"] != current_category:
            ws.merge_cells(f"A{row}:F{row}")
            ws[f"A{row}"] = f"▶ {req['category']}"
            ws[f"A{row}"].font = Font(bold=True, size=11, color="4472C4")
            ws[f"A{row}"].fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
            ws[f"A{row}"].alignment = Alignment(horizontal="left", vertical="center")
            ws.row_dimensions[row].height = 20
            row += 1
            current_category = req["category"]
        
        # ID column
        ws[f"A{row}"] = req["id"]
        ws[f"A{row}"].alignment = Alignment(horizontal="center", vertical="center")
        ws[f"A{row}"].font = Font(bold=True, size=9)
        
        # Requirement column
        ws[f"B{row}"] = req["requirement"]
        ws[f"B{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        thin = Side(style="thin")
        ws[f"B{row}"].border = Border(left=thin, right=thin, top=thin, bottom=thin)
        
        # Implementation Status (dropdown - yellow input cell)
        ws[f"C{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        ws[f"C{row}"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        ws[f"C{row}"].border = Border(left=thin, right=thin, top=thin, bottom=thin)
        validations["implementation_status"].add(ws[f"C{row}"])
        
        # Evidence Reference (yellow input cell)
        ws[f"D{row}"] = req.get("evidence", "")
        ws[f"D{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        ws[f"D{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        ws[f"D{row}"].border = Border(left=thin, right=thin, top=thin, bottom=thin)
        ws[f"D{row}"].font = Font(size=9, italic=True, color="666666")
        
        # Comments (yellow input cell)
        ws[f"E{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        ws[f"E{row}"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        ws[f"E{row}"].border = Border(left=thin, right=thin, top=thin, bottom=thin)
        
        # Compliance indicator (formula-driven)
        ws[f"F{row}"] = f'=IF(C{row}="Implemented","\u2705",IF(C{row}="Partially Implemented","\u26A0\uFE0F",IF(C{row}="Not Implemented","\u274C",IF(C{row}="N/A","N/A",""))))'
        ws[f"F{row}"].alignment = Alignment(horizontal="center", vertical="center")
        ws[f"F{row}"].border = Border(left=thin, right=thin, top=thin, bottom=thin)
        
        ws.row_dimensions[row].height = 45
        row += 1

    # Freeze header rows
    ws.freeze_panes = "A3"
    finalize_validations(ws, validations)

    return ws


# ============================================================================
# SECTION 6: SUMMARY DASHBOARD CREATION
# ============================================================================

def create_summary_dashboard(ws, styles):
    """
    Create Summary Dashboard with overall compliance metrics.
    
    This sheet provides executive-level visibility into SDLC security posture.
    Uses formulas to aggregate data from all domain sheets.
    """
    
    # Title
    ws.merge_cells("A1:E1")
    ws["A1"] = "SDLC Assessment - Summary Dashboard"
    apply_style(ws["A1"], styles["header"])
    ws.row_dimensions[1].height = 30

    # Assessment metadata
    ws["A3"] = "Assessment Date:"
    ws["B3"] = "=Instructions!B8"
    ws["A4"] = "Assessor:"
    ws["B4"] = "=Instructions!B9"
    ws["A5"] = "Organisation:"
    ws["B5"] = "=Instructions!B10"
    
    for r in [3, 4, 5]:
        ws[f"A{r}"].font = Font(bold=True)

    # Overall Compliance Score
    ws["A7"] = "Overall SDLC Compliance Score:"
    ws["A7"].font = Font(bold=True, size=13)
    ws.merge_cells("A7:B7")
    
    # Complex formula to calculate overall compliance across all domains
    # Counts "Implemented" divided by total non-header, non-N/A items
    ws["C7"] = """=(COUNTIF('Security Requirements Design'!C:C,"Implemented")+
COUNTIF('Development Environment'!C:C,"Implemented")+
COUNTIF('Build Deployment Pipeline'!C:C,"Implemented")+
COUNTIF('Security Testing Integration'!C:C,"Implemented")+
COUNTIF('Release Change Management'!C:C,"Implemented"))/
(COUNTA('Security Requirements Design'!C:C)+
COUNTA('Development Environment'!C:C)+
COUNTA('Build Deployment Pipeline'!C:C)+
COUNTA('Security Testing Integration'!C:C)+
COUNTA('Release Change Management'!C:C)-5-
COUNTIF('Security Requirements Design'!C:C,"N/A")-
COUNTIF('Development Environment'!C:C,"N/A")-
COUNTIF('Build Deployment Pipeline'!C:C,"N/A")-
COUNTIF('Security Testing Integration'!C:C,"N/A")-
COUNTIF('Release Change Management'!C:C,"N/A"))"""
    
    ws["C7"].number_format = "0%"
    ws["C7"].font = Font(bold=True, size=14)
    ws["C7"].alignment = Alignment(horizontal="center")
    
    # Status indicator
    ws["D7"] = '=IF(C7>=0.8,"🟢 Compliant",IF(C7>=0.6,"🟡 Needs Improvement","🔴 Non-Compliant"))'
    ws["D7"].font = Font(bold=True, size=12)
    ws["D7"].alignment = Alignment(horizontal="center")
    ws.merge_cells("D7:E7")

    # Domain-by-Domain Compliance
    ws["A10"] = "Domain Compliance Breakdown"
    ws["A10"].font = Font(bold=True, size=12, color="FFFFFF")
    ws["A10"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws.merge_cells("A10:E10")
    ws["A10"].alignment = Alignment(horizontal="center")

    # Domain headers
    domain_headers = ["Domain", "Compliance %", "Status", "Not Implemented", "Partially Implemented"]
    for col_num, header in enumerate(domain_headers, 1):
        cell = ws.cell(row=11, column=col_num, value=header)
        apply_style(cell, styles["column_header"])

    # Domain data
    domains = [
        ("Security Requirements Design", "1. Security Requirements & Design"),
        ("Development Environment", "2. Development Environment & Tooling"),
        ("Build Deployment Pipeline", "3. Build & Deployment Pipeline"),
        ("Security Testing Integration", "4. Security Testing Integration"),
        ("Release Change Management", "5. Release & Change Management"),
    ]

    row = 12
    for sheet_name, display_name in domains:
        ws[f"A{row}"] = display_name
        
        # Compliance % formula
        ws[f"B{row}"] = f"=COUNTIF('{sheet_name}'!C:C,\"Implemented\")/(COUNTA('{sheet_name}'!C:C)-1-COUNTIF('{sheet_name}'!C:C,\"N/A\"))"
        ws[f"B{row}"].number_format = "0%"
        ws[f"B{row}"].alignment = Alignment(horizontal="center")
        
        # Status indicator
        ws[f"C{row}"] = f'=IF(B{row}>=0.8,"🟢",IF(B{row}>=0.6,"🟡","🔴"))'
        ws[f"C{row}"].alignment = Alignment(horizontal="center")
        
        # Not Implemented count
        ws[f"D{row}"] = f"=COUNTIF('{sheet_name}'!C:C,\"Not Implemented\")"
        ws[f"D{row}"].alignment = Alignment(horizontal="center")
        
        # Partially Implemented count
        ws[f"E{row}"] = f"=COUNTIF('{sheet_name}'!C:C,\"Partially Implemented\")"
        ws[f"E{row}"].alignment = Alignment(horizontal="center")
        
        row += 1

    # Summary Statistics
    ws["A18"] = "Summary Statistics"
    ws["A18"].font = Font(bold=True, size=12, color="FFFFFF")
    ws["A18"].fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    ws.merge_cells("A18:E18")
    ws["A18"].alignment = Alignment(horizontal="center")

    stats = [
        ("Total Requirements Assessed:", "=COUNTA('Security Requirements Design'!C:C)+COUNTA('Development Environment'!C:C)+COUNTA('Build Deployment Pipeline'!C:C)+COUNTA('Security Testing Integration'!C:C)+COUNTA('Release Change Management'!C:C)-5"),
        ("Implemented:", "=COUNTIF('Security Requirements Design'!C:C,\"Implemented\")+COUNTIF('Development Environment'!C:C,\"Implemented\")+COUNTIF('Build Deployment Pipeline'!C:C,\"Implemented\")+COUNTIF('Security Testing Integration'!C:C,\"Implemented\")+COUNTIF('Release Change Management'!C:C,\"Implemented\")"),
        ("Partially Implemented:", "=COUNTIF('Security Requirements Design'!C:C,\"Partially Implemented\")+COUNTIF('Development Environment'!C:C,\"Partially Implemented\")+COUNTIF('Build Deployment Pipeline'!C:C,\"Partially Implemented\")+COUNTIF('Security Testing Integration'!C:C,\"Partially Implemented\")+COUNTIF('Release Change Management'!C:C,\"Partially Implemented\")"),
        ("Not Implemented:", "=COUNTIF('Security Requirements Design'!C:C,\"Not Implemented\")+COUNTIF('Development Environment'!C:C,\"Not Implemented\")+COUNTIF('Build Deployment Pipeline'!C:C,\"Not Implemented\")+COUNTIF('Security Testing Integration'!C:C,\"Not Implemented\")+COUNTIF('Release Change Management'!C:C,\"Not Implemented\")"),
        ("Not Applicable (N/A):", "=COUNTIF('Security Requirements Design'!C:C,\"N/A\")+COUNTIF('Development Environment'!C:C,\"N/A\")+COUNTIF('Build Deployment Pipeline'!C:C,\"N/A\")+COUNTIF('Security Testing Integration'!C:C,\"N/A\")+COUNTIF('Release Change Management'!C:C,\"N/A\")"),
    ]

    row = 19
    for label, formula in stats:
        ws[f"A{row}"] = label
        ws[f"A{row}"].font = Font(bold=True)
        ws[f"B{row}"] = formula
        ws[f"B{row}"].alignment = Alignment(horizontal="center")
        ws[f"B{row}"].font = Font(bold=True, size=11)
        row += 1

    # Recommendations
    ws["A25"] = "Recommendations"
    ws["A25"].font = Font(bold=True, size=12, color="FFFFFF")
    ws["A25"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws.merge_cells("A25:E25")
    ws["A25"].alignment = Alignment(horizontal="center")

    recommendations = [
        "\u2022 Focus remediation efforts on 'Not Implemented' items first, then 'Partially Implemented'",
        "\u2022 Prioritize gaps in Build & Deployment Pipeline - these provide automated security controls",
        "\u2022 Document all evidence thoroughly - lack of evidence ≠ lack of implementation",
        "\u2022 Review 'N/A' items carefully - are they genuinely not applicable or just difficult?",
        "\u2022 Set target dates for all gaps in the Gap Analysis sheet",
        "\u2022 Schedule quarterly re-assessments to track improvement",
    ]

    row = 26
    for rec in recommendations:
        ws[f"A{row}"] = rec
        ws[f"A{row}"].alignment = Alignment(wrap_text=True)
        ws.merge_cells(f"A{row}:E{row}")
        ws.row_dimensions[row].height = 25
        row += 1

    # Column widths
    ws.column_dimensions["A"].width = 40
    ws.column_dimensions["B"].width = 18
    ws.column_dimensions["C"].width = 15
    ws.column_dimensions["D"].width = 20
    ws.column_dimensions["E"].width = 25

    return ws


# ============================================================================
# SECTION 7: EVIDENCE REGISTER CREATION
# ============================================================================

def create_evidence_register(ws, styles):
    """
    Create Evidence Register for tracking supporting documentation.
    
    Evidence is what separates real compliance from security theater.
    Every claim needs proof.
    """
    validations = create_base_validations(ws)
    
    # Title
    ws.merge_cells("A1:G1")
    ws["A1"] = "Evidence Register"
    apply_style(ws["A1"], styles["header"])
    ws.row_dimensions[1].height = 25

    # Instructions
    ws["A2"] = "Document all evidence supporting your SDLC assessment. Each requirement should have traceable evidence."
    ws.merge_cells("A2:G2")
    ws["A2"].font = Font(italic=True, size=10)
    ws["A2"].alignment = Alignment(wrap_text=True)
    ws.row_dimensions[2].height = 30

    # Column headers
    headers = [
        "Evidence ID",
        "Related Requirement",
        "Evidence Type",
        "Description",
        "Location/Link",
        "Collection Date",
        "Collected By",
    ]
    
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col_num, value=header)
        apply_style(cell, styles["column_header"])

    # Column widths
    widths = {"A": 12, "B": 25, "C": 18, "D": 40, "E": 35, "F": 15, "G": 20}
    for col, width in widths.items():
        ws.column_dimensions[col].width = width

    # Evidence type dropdown
    validations["evidence_type"].add(f"C4:C200")

    # Example rows (first few pre-filled as templates)
    examples = [
        ("E001", "1.1 - Security Requirements", "Document", "SDLC Process Documentation", "https://wiki.company.com/sdlc", "01.01.2025", "Security Team"),
        ("E002", "3.2 - SAST Integration", "Screenshot", "SonarQube Pipeline Configuration", "file://evidence/sonarqube_config.png", "05.01.2025", "DevOps Lead"),
        ("E003", "4.4 - DAST Scanning", "Report", "OWASP ZAP Scan Results", "https://security-portal.company.com/reports/zap/", "06.01.2025", "Security Analyst"),
    ]

    row = 4
    for eid, req, etype, desc, loc, date, by in examples:
        ws[f"A{row}"] = eid
        ws[f"B{row}"] = req
        ws[f"C{row}"] = etype
        ws[f"D{row}"] = desc
        ws[f"E{row}"] = loc
        ws[f"F{row}"] = date
        ws[f"G{row}"] = by
        
        # Style example rows as input cells
        for col in ["A", "B", "C", "D", "E", "F", "G"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
            ws[f"{col}{row}"].font = Font(italic=True, size=9, color="666666")
        
        row += 1

    ws.freeze_panes = "A4"
    finalize_validations(ws, validations)
    return ws

# ============================================================================
# SECTION 8: GAP ANALYSIS SHEET CREATION
# ============================================================================

def create_gap_analysis_sheet(ws, styles):
    """
    Create Gap Analysis sheet for tracking remediation efforts.
    
    Identifying gaps is easy. Fixing them requires planning, ownership, and tracking.
    This sheet turns assessment findings into actionable remediation plans.
    """
    validations = create_base_validations(ws)
    
    # Title
    ws.merge_cells("A1:J1")
    ws["A1"] = "Gap Analysis & Remediation Plan"
    apply_style(ws["A1"], styles["header"])
    ws.row_dimensions[1].height = 25

    # Instructions
    ws["A2"] = "Document all 'Not Implemented' and 'Partially Implemented' requirements. Assign owners, set target dates, and track remediation progress."
    ws.merge_cells("A2:J2")
    ws["A2"].font = Font(italic=True, size=10)
    ws["A2"].alignment = Alignment(wrap_text=True)
    ws.row_dimensions[2].height = 30

    # Column headers
    headers = [
        "Gap ID",
        "Domain",
        "Requirement ID",
        "Requirement Description",
        "Current State",
        "Target State",
        "Priority",
        "Owner",
        "Target Date",
        "Status",
    ]
    
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=3, column=col_num, value=header)
        apply_style(cell, styles["column_header"])

    # Column widths
    widths = {
        "A": 10,
        "B": 22,
        "C": 12,
        "D": 35,
        "E": 25,
        "F": 25,
        "G": 12,
        "H": 20,
        "I": 12,
        "J": 15,
    }
    for col, width in widths.items():
        ws.column_dimensions[col].width = width

    # Add dropdowns
    validations["priority"].add("G4:G200")
    validations["gap_status"].add("J4:J200")

    # Example gaps (pre-filled as templates)
    example_gaps = [
        (
            "GAP-001",
            "Development Environment",
            "2.4",
            "Pre-commit hooks prevent secret commits",
            "No pre-commit hooks configured",
            "Git-secrets installed on all dev workstations",
            "High",
            "DevOps Lead",
            "31.01.2025",
            "In Progress"
        ),
        (
            "GAP-002",
            "Build Pipeline",
            "3.2",
            "SAST tools integrated into build pipeline",
            "SAST runs manually, not in pipeline",
            "SonarQube integrated with automated quality gates",
            "Critical",
            "CI/CD Engineer",
            "15.02.2025",
            "Open"
        ),
        (
            "GAP-003",
            "Security Testing",
            "4.4",
            "DAST runs against staging",
            "No DAST scanning performed",
            "OWASP ZAP automated scans before production",
            "High",
            "Security Team",
            "28.02.2025",
            "Open"
        ),
    ]

    row = 4
    for gap_data in example_gaps:
        for col_num, value in enumerate(gap_data, 1):
            cell = ws.cell(row=row, column=col_num, value=value)
            cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
            cell.font = Font(italic=True, size=9, color="666666")
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            thin = Side(style="thin")
            cell.border = Border(left=thin, right=thin, top=thin, bottom=thin)
        
        ws.row_dimensions[row].height = 40
        row += 1

    # Add conditional formatting guidance below examples
    row += 1
    ws[f"A{row}"] = "Priority Guidance:"
    ws[f"A{row}"].font = Font(bold=True)
    ws.merge_cells(f"A{row}:J{row}")
    
    row += 1
    priority_guide = [
        "Critical: Exploitable vulnerability or compliance blocker - fix immediately",
        "High: Significant security risk or major compliance gap - fix within 30 days",
        "Medium: Moderate security risk or minor compliance gap - fix within 90 days",
        "Low: Low security risk or improvement opportunity - fix when resources available",
    ]
    
    for guide in priority_guide:
        ws[f"A{row}"] = guide
        ws[f"A{row}"].alignment = Alignment(wrap_text=True)
        ws.merge_cells(f"A{row}:J{row}")
        
        # Color code based on priority
        if "Critical" in guide:
            ws[f"A{row}"].fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
        elif "High" in guide:
            ws[f"A{row}"].fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
        elif "Medium" in guide:
            ws[f"A{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
        elif "Low" in guide:
            ws[f"A{row}"].fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
        
        ws.row_dimensions[row].height = 20
        row += 1

    ws.freeze_panes = "A4"
    finalize_validations(ws, validations)
    return ws


# ============================================================================
# SECTION 9: APPROVAL SIGN-OFF SHEET CREATION
# ============================================================================

def create_approval_sheet(ws, styles):
    """
    Create Approval Sign-Off sheet for formal assessment approval.
    
    Assessment isn't complete until it's reviewed and approved.
    This provides audit trail and accountability.
    """
    
    # Title
    ws.merge_cells("A1:D1")
    ws["A1"] = "SDLC Assessment - Approval Sign-Off"
    apply_style(ws["A1"], styles["header"])
    ws.row_dimensions[1].height = 30

    # Subtitle
    ws.merge_cells("A2:D2")
    ws["A2"] = "Formal approval workflow for assessment completion"
    apply_style(ws["A2"], styles["subheader"])
    ws.row_dimensions[2].height = 20

    # Assessment Summary Section
    ws["A4"] = "ASSESSMENT SUMMARY"
    ws["A4"].font = Font(bold=True, size=11, color="FFFFFF")
    ws["A4"].fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    ws.merge_cells("A4:D4")
    ws["A4"].alignment = Alignment(horizontal="center")

    # Assessment details
    ws["A6"] = "Assessment Date:"
    ws["B6"] = "=Instructions!B8"
    ws["B6"].font = Font(bold=True)
    
    ws["A7"] = "Assessor Name:"
    ws["B7"] = "=Instructions!B9"
    ws["B7"].font = Font(bold=True)
    
    ws["A8"] = "Organisation:"
    ws["B8"] = "=Instructions!B10"
    ws["B8"].font = Font(bold=True)
    
    ws["A9"] = "Overall Compliance Score:"
    ws["B9"] = "='Summary Dashboard'!C7"
    ws["B9"].number_format = "0%"
    ws["B9"].font = Font(bold=True, size=12, color="C00000")
    
    ws["A10"] = "Compliance Status:"
    ws["B10"] = "='Summary Dashboard'!D7"
    ws["B10"].font = Font(bold=True, size=11)

    for r in range(6, 11):
        ws[f"A{r}"].font = Font(bold=True)

    # Key Findings Section
    ws["A13"] = "KEY FINDINGS"
    ws["A13"].font = Font(bold=True, size=11, color="FFFFFF")
    ws["A13"].fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    ws.merge_cells("A13:D13")
    ws["A13"].alignment = Alignment(horizontal="center")

    ws["A15"] = "Total Requirements:"
    ws["B15"] = "='Summary Dashboard'!B19"
    ws["B15"].font = Font(bold=True)
    
    ws["A16"] = "Implemented:"
    ws["B16"] = "='Summary Dashboard'!B20"
    ws["B16"].fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    ws["B16"].font = Font(bold=True)
    
    ws["A17"] = "Partially Implemented:"
    ws["B17"] = "='Summary Dashboard'!B21"
    ws["B17"].fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
    ws["B17"].font = Font(bold=True)
    
    ws["A18"] = "Not Implemented:"
    ws["B18"] = "='Summary Dashboard'!B22"
    ws["B18"].fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    ws["B18"].font = Font(bold=True)
    
    ws["A19"] = "Not Applicable:"
    ws["B19"] = "='Summary Dashboard'!B23"
    ws["B19"].fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")

    for r in range(15, 20):
        ws[f"A{r}"].font = Font(bold=True)
        ws[f"B{r}"].alignment = Alignment(horizontal="center")

    # Approval Workflow Section
    ws["A22"] = "APPROVAL WORKFLOW"
    ws["A22"].font = Font(bold=True, size=11, color="FFFFFF")
    ws["A22"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws.merge_cells("A22:D22")
    ws["A22"].alignment = Alignment(horizontal="center")

    # Approval table headers
    approval_headers = ["Role", "Name", "Signature", "Date"]
    for col_num, header in enumerate(approval_headers, 1):
        cell = ws.cell(row=23, column=col_num, value=header)
        cell.font = Font(bold=True, size=10)
        cell.fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center")

    # Approval roles
    approval_roles = [
        "Assessment Completer",
        "Application Security Lead",
        "Development Manager / Engineering Lead",
        "CISO / Security Director",
    ]

    row = 24
    for role in approval_roles:
        ws[f"A{row}"] = role
        ws[f"A{row}"].font = Font(bold=True, size=10)
        
        # Input cells for signature
        for col in ["B", "C", "D"]:
            ws[f"{col}{row}"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
            thin = Side(style="thin")
            ws[f"{col}{row}"].border = Border(left=thin, right=thin, top=thin, bottom=thin)
        
        ws.row_dimensions[row].height = 25
        row += 1

    # Approval Notes Section
    ws["A29"] = "APPROVAL NOTES / CONDITIONS"
    ws["A29"].font = Font(bold=True, size=11, color="FFFFFF")
    ws["A29"].fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    ws.merge_cells("A29:D29")
    ws["A29"].alignment = Alignment(horizontal="center")

    ws.merge_cells("A30:D35")
    ws["A30"].fill = PatternFill(start_color="FFFFCC", end_color="FFFFCC", fill_type="solid")
    ws["A30"].alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
    thin = Side(style="thin")
    ws["A30"].border = Border(left=thin, right=thin, top=thin, bottom=thin)
    ws["A30"] = "Enter any conditions, exceptions, or notes related to this approval:\n\n"
    ws["A30"].font = Font(italic=True, size=9)

    # Approval Criteria
    ws["A37"] = "APPROVAL CRITERIA"
    ws["A37"].font = Font(bold=True, size=11, color="FFFFFF")
    ws["A37"].fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    ws.merge_cells("A37:D37")
    ws["A37"].alignment = Alignment(horizontal="center")

    approval_criteria = [
        "✓ All assessment domains have been completed",
        "✓ Evidence references are provided for all 'Implemented' claims",
        "✓ Gap Analysis sheet documents all 'Not Implemented' items",
        "✓ Remediation plans include owners and target dates",
        "✓ Assessment findings are accurate and verifiable",
        "✓ Summary Dashboard reflects true compliance posture",
    ]

    row = 38
    for criteria in approval_criteria:
        ws[f"A{row}"] = criteria
        ws[f"A{row}"].alignment = Alignment(wrap_text=True)
        ws.merge_cells(f"A{row}:D{row}")
        ws.row_dimensions[row].height = 20
        row += 1

    # Column widths
    ws.column_dimensions["A"].width = 35
    ws.column_dimensions["B"].width = 25
    ws.column_dimensions["C"].width = 25
    ws.column_dimensions["D"].width = 15

    return ws


# ============================================================================
# SECTION 10: MAIN EXECUTION
# ============================================================================

def main():
    """
    Main execution function - generates complete SDLC Assessment workbook.
    
    As Feynman taught us: "What I cannot create, I do not understand."
    This script creates a complete, functional assessment workbook that
    actually helps organizations understand their SDLC security posture.
    """
    logger.info("=" * 80)
    logger.info(" " * 20 + "ISMS Control 8.28.1 - SDLC Assessment Generator")
    logger.info("=" * 80)
    logger.info("")
    logger.info("Generating comprehensive SDLC security assessment workbook...")
    logger.info("")
    
    try:
        # Create workbook structure
        logger.info("📁 [1/10] Creating workbook structure...")
        wb = create_workbook()
        styles = setup_styles()
        logger.info("     \u2705 Workbook initialized with 10 sheets")

        # Create Instructions sheet
        logger.info("📄 [2/10] Creating Instructions sheet...")
        ws_instructions = wb["Instructions"]
        create_instructions_sheet(ws_instructions, styles)
        logger.info("     \u2705 Instructions sheet complete (guidance, legend, examples)")

        # Create assessment domain sheets
        logger.info("📊 [3/10] Creating Domain 1: Security Requirements & Design...")
        ws_domain1 = wb["Security Requirements Design"]
        create_domain_sheet(
            ws_domain1,
            "Security Requirements & Design",
            get_domain1_requirements(),
            styles
        )
        logger.info("     \u2705 18 requirements (Requirements Definition, Design Review)")

        logger.info("📊 [4/10] Creating Domain 2: Development Environment & Tooling...")
        ws_domain2 = wb["Development Environment"]
        create_domain_sheet(
            ws_domain2,
            "Development Environment & Tooling",
            get_domain2_requirements(),
            styles
        )
        logger.info("     \u2705 18 requirements (Workstation Security, Repository Security, Tools)")

        logger.info("📊 [5/10] Creating Domain 3: Build & Deployment Pipeline...")
        ws_domain3 = wb["Build Deployment Pipeline"]
        create_domain_sheet(
            ws_domain3,
            "Build & Deployment Pipeline",
            get_domain3_requirements(),
            styles
        )
        logger.info("     \u2705 18 requirements (Pipeline Security, Security Scanning, Deployment)")

        logger.info("📊 [6/10] Creating Domain 4: Security Testing Integration...")
        ws_domain4 = wb["Security Testing Integration"]
        create_domain_sheet(
            ws_domain4,
            "Security Testing Integration",
            get_domain4_requirements(),
            styles
        )
        logger.info("     \u2705 18 requirements (Unit/Integration/API/DAST/Pentest)")

        logger.info("📊 [7/10] Creating Domain 5: Release & Change Management...")
        ws_domain5 = wb["Release Change Management"]
        create_domain_sheet(
            ws_domain5,
            "Release & Change Management",
            get_domain5_requirements(),
            styles
        )
        logger.info("     \u2705 18 requirements (Release Process, Patch Management, Approval)")

        logger.info("📈 [8/10] Creating Summary Dashboard...")
        ws_summary = wb["Summary Dashboard"]
        create_summary_dashboard(ws_summary, styles)
        logger.info("     \u2705 Executive summary with compliance metrics and traffic lights")

        logger.info("🔎 [9/10] Creating Evidence Register...")
        ws_evidence = wb["Evidence Register"]
        create_evidence_register(ws_evidence, styles)
        logger.info("     \u2705 Evidence tracking with examples and templates")

        logger.info("\u26A0\uFE0F  [10/10] Creating Gap Analysis & Approval sheets...")
        ws_gap = wb["Gap Analysis"]
        create_gap_analysis_sheet(ws_gap, styles)
        
        ws_approval = wb["Approval Sign-Off"]
        create_approval_sheet(ws_approval, styles)
        logger.info("     \u2705 Gap remediation tracking and formal approval workflow")

        # Save workbook
        logger.info("")
        logger.info("💾 Saving workbook...")
        timestamp = datetime.now().strftime("%Y%m%d")
        filename = f"ISMS-IMP-A.8.28.1_SDLC_Assessment_{datetime.now().strftime('%Y%m%d')}.xlsx"
        wb.save(filename)

        # Success summary
        logger.info("")
        logger.info("=" * 80)
        logger.info("\u2705 SUCCESS: SDLC Assessment workbook generated successfully!")
        logger.info("=" * 80)
        logger.info("")
        logger.info(f"📁 File: {filename}")
        logger.info(f"📊 Sheets: {len(wb.sheetnames)}")
        logger.info(f"\u1F4CB Total Requirements: 90 (18 per domain × 5 domains)")
        logger.info("")
        logger.info("📌 Assessment Domains:")
        logger.info("   1. Security Requirements & Design        (18 requirements)")
        logger.info("   2. Development Environment & Tooling     (18 requirements)")
        logger.info("   3. Build & Deployment Pipeline           (18 requirements)")
        logger.info("   4. Security Testing Integration          (18 requirements)")
        logger.info("   5. Release & Change Management           (18 requirements)")
        logger.info("")
        logger.info("📌 Supporting Sheets:")
        logger.info("   \u2022 Instructions (comprehensive guidance)")
        logger.info("   \u2022 Summary Dashboard (executive overview)")
        logger.info("   \u2022 Evidence Register (audit trail)")
        logger.info("   \u2022 Gap Analysis (remediation tracking)")
        logger.info("   \u2022 Approval Sign-Off (formal approval)")
        logger.info("")
        logger.info("🎯 Next Steps:")
        logger.info("   1. Open the workbook and review the Instructions sheet")
        logger.info("   2. Complete each assessment domain systematically")
        logger.info("   3. Provide evidence references for all 'Implemented' items")
        logger.info("   4. Document gaps and create remediation plans")
        logger.info("   5. Review Summary Dashboard for compliance metrics")
        logger.info("   6. Obtain stakeholder approvals")
        logger.info("")
        logger.info("💡 Remember: Security is not cargo cult. Focus on what is ACTUALLY")
        logger.info("   implemented and working, not just what exists on paper.")
        logger.info("")
        logger.info("=" * 80)
        
        return 0

    except Exception as e:
        logger.info("")
        logger.info("=" * 80)
        logger.error("\u274C ERROR: Failed to generate workbook")
        logger.info("=" * 80)
        logger.error(f"Error Details: {str(e)}")
        logger.info("")
        import traceback
        traceback.print_exc()
        logger.info("")
        logger.error("Please report this error to the ISMS implementation team.")
        logger.info("=" * 80)
        return 1


if __name__ == "__main__":
    sys.exit(main())

# =============================================================================
# QA_VERIFIED: 2026-01-31
# QA_STATUS: PASSED - STANDARDIZATION COMPLETE (Phase 1-3)
# QA_TOOL: Claude Code Standardization
# CHANGES: constants, metadata headers, v1.0 versioning, logger output
# =============================================================================
