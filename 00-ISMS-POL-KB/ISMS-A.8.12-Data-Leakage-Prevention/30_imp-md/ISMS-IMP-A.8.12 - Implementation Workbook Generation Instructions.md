# ISMS-IMP-A.8.12 - Implementation Workbook Generation Instructions

**Document ID**: ISMS-IMP-A.8.12-INSTRUCTIONS  
**Title**: Python Generator Instructions for DLP Assessment Workbooks  
**Version**: 1.0  
**Date**: [Date] 
**For**: Claude (Future Sessions)  
**Control**: ISO/IEC 27001:2022 Control A.8.12 (Data Leakage Prevention)

---

## 1. Overview

This document provides **complete instructions** for Claude to generate 5 DLP implementation assessment workbooks and their supporting Python generator scripts.

**Context:**  
- **Policy Layer (POL)**: 13 documents COMPLETE ✅ (~6,745 lines)
- **Implementation Layer (IMP)**: 5 workbooks TO BE CREATED 🔜
- **Reference Control**: A.8.11 (Data Masking) - use as template pattern
- **Reference Control**: A.8.23/A.8.24 - secondary pattern reference

---

## 2. Workbook Structure Overview

### 2.1 Complete Workbook Set

| Workbook ID | Title | Sheets | Assessment Items | Python Script |
|-------------|-------|--------|------------------|---------------|
| **ISMS-IMP-A.8.12.1** | DLP Infrastructure Assessment | ~10 | ~80 | `generate_a812_1_dlp_infrastructure.py` |
| **ISMS-IMP-A.8.12.2** | Data Classification Assessment | ~9 | ~70 | `generate_a812_2_data_classification.py` |
| **ISMS-IMP-A.8.12.3** | Channel Coverage Assessment | ~11 | ~90 | `generate_a812_3_channel_coverage.py` |
| **ISMS-IMP-A.8.12.4** | Monitoring & Response Assessment | ~10 | ~70 | `generate_a812_4_monitoring_response.py` |
| **ISMS-IMP-A.8.12.5** | Compliance Summary Dashboard | ~9 | ~25 KPIs | `generate_a812_5_compliance_dashboard.py` |

**Total Implementation Layer Output:** ~49 sheets across 5 workbooks, ~310 assessment items

---

## 3. Domain Mapping (Policy → Implementation)

### 3.1 Domain 1: DLP Infrastructure (IMP-A.8.12.1)

**Policy Source**: ISMS-POL-A.8.12-S2.2 (Channel Protection Requirements)

**Assessment Focus:**
- DLP technology inventory (network, endpoint, cloud, email gateway)
- Deployment architecture (inline, monitor-only, hybrid)
- DLP capabilities (content inspection, pattern matching, ML/AI, fingerprinting)
- Vendor information (licensing, support contracts, EOL tracking)
- Integration status (SIEM, SOC tools, incident management, IAM)

**Sheets Required (~10 sheets):**
1. **Instructions_Legend** - Standard instructions + domain-specific guidance
2. **DLP_Technology_Inventory** - All DLP solutions deployed
3. **Network_DLP** - Network appliances, inline/TAP, protocols covered
4. **Endpoint_DLP** - Agent deployment (Windows, macOS, Linux, VDI)
5. **Email_DLP** - Gateway DLP, M365 Purview, Google Workspace DLP
6. **Cloud_CASB_DLP** - CASB solutions, API-based DLP for SaaS
7. **Web_DLP** - Proxy-based, SSL inspection, URL filtering integration
8. **Database_DAM** - Database Activity Monitoring for DLP
9. **Gap_Analysis** - Infrastructure gaps (40 rows)
10. **Evidence_Register** - Evidence tracking (100 rows)
11. **Summary_Dashboard** - KPIs + infrastructure compliance

**Key Columns (Assessment Sheets):**
- Technology Name
- Deployment Type (Network/Endpoint/Cloud/Email/Web)
- Deployment Architecture (Inline/Monitor/Hybrid)
- Channels Covered (Email/Web/USB/Network/Mobile)
- Capabilities (Content Inspection/Regex/Fingerprint/ML)
- Integration Status (SIEM/SOC/IAM/Ticketing)
- Vendor/Licensing
- Compliance Status (Yes/No/Partial/Planned/N/A)
- Gap Description
- Evidence ID

---

### 3.2 Domain 2: Data Classification (IMP-A.8.12.2)

**Policy Source**: ISMS-POL-A.8.12-S2.1 (Data Classification & Identification)

**Assessment Focus:**
- Data classification schema (Public/Internal/Confidential/Restricted)
- Sensitive data categories (PII, financial, IP, credentials)
- Data location inventory (file servers, databases, endpoints, cloud)
- Data labeling methods (manual, automated, metadata)
- Data owner assignment
- Regulatory mapping (FADP/GDPR requirements)

**Sheets Required (~9 sheets):**
1. **Instructions_Legend**
2. **Classification_Schema** - Org classification levels (4-tier standard)
3. **Sensitive_Data_Inventory** - PII, financial, IP, credentials, business confidential
4. **Data_Location_Mapping** - Where sensitive data resides
5. **Data_Owner_Assignment** - Who owns each data category
6. **Regulatory_Mapping** - FADP/GDPR/PCI-DSS data mapping
7. **Labeling_Methods** - Manual, automated, classification tools
8. **Gap_Analysis** - Classification gaps (40 rows)
9. **Evidence_Register** - Evidence tracking (100 rows)
10. **Summary_Dashboard** - Classification compliance KPIs

**Key Columns:**
- Data Category (PII/Financial/IP/Credentials/Business Confidential)
- Classification Level (Public/Internal/Confidential/Restricted)
- Data Location (File Server/Database/Endpoint/Cloud/Email)
- Data Owner (Name, Department, Email)
- Regulatory Requirement (FADP/GDPR/PCI-DSS/None)
- Labeling Method (Manual/Automated/Metadata/None)
- Discovery Status (Discovered/In Progress/Not Started)
- DLP Protection (Yes/No/Partial/Planned)
- Compliance Status
- Evidence ID

---

### 3.3 Domain 3: Channel Coverage (IMP-A.8.12.3)

**Policy Source**: ISMS-POL-A.8.12-S2.2 (Channel Protection Requirements - Sections 3-8)

**Assessment Focus:**
- 6 major egress channels (Email, Web/Cloud, Endpoint, Network, Application, Mobile)
- DLP deployment per channel (Yes/No/Partial/Planned)
- Detection capabilities per channel (Pattern/Keyword/Fingerprint/ML)
- Policy actions per channel (Allow/Alert/Block/Quarantine/Encrypt)
- Coverage percentage (% of traffic inspected)
- Gap identification (unprotected channels, blind spots)

**Sheets Required (~11 sheets):**
1. **Instructions_Legend**
2. **Channel_Coverage_Matrix** - Overview of all 6 channels
3. **Email_Channel** - SMTP, M365, Gmail, attachments, encrypted email
4. **Web_Cloud_Channel** - HTTP/HTTPS, cloud storage, SaaS, code repos
5. **Endpoint_Channel** - USB, print, clipboard, screen capture, Bluetooth
6. **Network_Channel** - SMB, FTP, NFS, SCP, WebDAV
7. **Application_Channel** - Databases, APIs, reporting tools, CRM, ERP
8. **Mobile_Channel** - MDM/MAM, BYOD, corporate mobile
9. **Coverage_Metrics** - Channel coverage % calculations
10. **Gap_Analysis** - Channel gaps (40 rows)
11. **Evidence_Register** - Evidence tracking (100 rows)
12. **Summary_Dashboard** - Channel compliance KPIs

**Key Columns:**
- Channel Name (Email/Web/Endpoint/Network/Application/Mobile)
- Sub-Channel (e.g., Email: SMTP, Webmail, M365)
- DLP Deployed? (Yes/No/Partial/Planned/N/A)
- Detection Method (Pattern/Keyword/Fingerprint/Contextual/ML)
- Policy Action (Allow/Alert/Block/Quarantine/Encrypt)
- Coverage % (% of traffic inspected)
- Traffic Volume (GB/day or transactions/day)
- Exceptions Count
- Compliance Status
- Evidence ID

---

### 3.4 Domain 4: Monitoring & Response (IMP-A.8.12.4)

**Policy Source**: ISMS-POL-A.8.12-S2.3 (Monitoring & Detection) + S2.4 (Incident Response)

**Assessment Focus:**
- DLP logging requirements (what events are logged)
- Alert configuration (severity levels, thresholds)
- SIEM integration (log forwarding, correlation rules)
- False positive management (FP rate, tuning process)
- Incident response procedures (triage, containment, investigation)
- SOC integration (alert workflow, escalation)
- Dashboard and reporting (executive, operational, compliance)

**Sheets Required (~10 sheets):**
1. **Instructions_Legend**
2. **Logging_Requirements** - What events are logged per channel
3. **Alert_Configuration** - Alert rules, severity, thresholds
4. **SIEM_Integration** - Log forwarding, correlation rules, use cases
5. **False_Positive_Management** - FP rate, tuning procedures, metrics
6. **Incident_Response** - Triage, containment, investigation procedures
7. **SOC_Integration** - Alert workflow, escalation matrix, SLAs
8. **Dashboards_Reporting** - Executive, operational, compliance reports
9. **Gap_Analysis** - Monitoring/response gaps (40 rows)
10. **Evidence_Register** - Evidence tracking (100 rows)
11. **Summary_Dashboard** - Monitoring/response compliance KPIs

**Key Columns:**
- Monitoring Area (Logging/Alerting/SIEM/FP Management/IR/SOC/Reporting)
- Requirement (What must be monitored/logged/reported)
- Implemented? (Yes/No/Partial/Planned/N/A)
- Alert Severity (Critical/High/Medium/Low/Info)
- Response SLA (15 min/1 hour/4 hours/24 hours)
- Current Performance (Actual MTTD, MTTR, FP rate)
- Target Performance (Target MTTD, MTTR, FP rate)
- Compliance Status
- Evidence ID

**Key Metrics to Track:**
- Mean Time To Detect (MTTD) - target <5 min for Critical
- Mean Time To Respond (MTTR) - target <15 min for Critical
- False Positive Rate - target <10% after 6 months tuning
- Alert Volume - trend over time
- Incident Response SLA Compliance - target >90%

---

### 3.5 Domain 5: Compliance Dashboard (IMP-A.8.12.5)

**Policy Source**: All ISMS-POL-A.8.12 documents

**Assessment Focus:**
- Consolidated metrics from Domains 1-4
- Overall DLP compliance score
- Gap rollup across all domains
- Risk register (DLP-specific risks)
- Remediation roadmap (prioritized action items)
- Executive summary (one-page CISO view)
- CISO/DPO approval sign-off

**Sheets Required (~9 sheets):**
1. **Instructions_Legend** - Formula update instructions (external workbook links)
2. **Executive_Summary** - One-page CISO view (12 KPIs)
3. **Domain_1_Summary** - Infrastructure rollup from IMP-A.8.12.1
4. **Domain_2_Summary** - Classification rollup from IMP-A.8.12.2
5. **Domain_3_Summary** - Channel coverage rollup from IMP-A.8.12.3
6. **Domain_4_Summary** - Monitoring rollup from IMP-A.8.12.4
7. **Consolidated_Gap_Analysis** - All gaps from Domains 1-4 (50 rows)
8. **Risk_Register** - DLP-specific risks (40 rows: 20 pre-defined + 20 custom)
9. **Remediation_Roadmap** - Prioritized actions (50 rows)
10. **Evidence_Master_Index** - All evidence across domains (100 rows)
11. **KPI_Dashboard** - 25 KPIs with traffic lights
12. **CISO_DPO_Approval** - Approval workflow sign-off

**CRITICAL**: This workbook uses **external formulas** to pull data from Domains 1-4.  
Use **placeholder formulas** like `[A812-1]`, `[A812-2]`, `[A812-3]`, `[A812-4]` and provide instructions for users to update via Find & Replace.

**Key KPIs (Executive Summary):**
- Overall DLP Compliance Score (weighted average of Domains 1-4)
- Infrastructure Coverage % (from Domain 1)
- Data Classification Coverage % (from Domain 2)
- Channel Protection Coverage % (from Domain 3)
- Monitoring Effectiveness % (from Domain 4)
- False Positive Rate (from Domain 4)
- Incident Response SLA Compliance % (from Domain 4)
- Total Gaps (Critical/High/Medium/Low)
- Gaps Remediated % (closed / total)
- High-Risk Issues (count of high-risk gaps)
- Evidence Completeness % (documented / required)
- CISO Approval Status (Approved/Pending/Rejected)

---

## 4. Python Script Structure (Based on A.8.11 Pattern)

### 4.1 Script Template Structure

Each generator script SHALL follow this structure (based on `generate_a811_1_data_inventory.py`):
```python
#!/usr/bin/env python3
"""
ISMS-IMP-A.8.12.X - [Workbook Title] Excel Generator
ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention

[Description of what this workbook assesses]

Requirements:
    sudo apt install python3-openpyxl
    
Usage:
    python3 generate_a812_X_[workbook_name].py

Author: ISMS Implementation Team
Date: Approval Date
Control: ISO/IEC 27001:2022 - A.8.12 Data Leakage Prevention
"""

from datetime import datetime, timedelta
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation


# ============================================================================
# SECTION 1: CONSTANTS & CONFIGURATION
# ============================================================================

# Document Information
WORKBOOK_VERSION = "1.0"
CONTROL_ID = "A.8.12"
WORKBOOK_ID = "ISMS-IMP-A.8.12.X"
RELATED_POLICY = "ISMS-POL-A.8.12-S2.X"
ASSESSMENT_AREA = "[Assessment Area Name]"

# Color Scheme (CONSISTENT across all A.8.12 workbooks)
COLOR_HEADER = "003366"          # Dark blue
COLOR_SUBHEADER = "4472C4"       # Medium blue
COLOR_COLUMN_HEADER = "D9D9D9"   # Light gray
COLOR_INPUT = "FFFFCC"           # Light yellow (user input)
COLOR_INFO = "E7E6E6"            # Light gray (info/example rows)
COLOR_COMPLETE = "C6EFCE"        # Light green (✅ Yes)
COLOR_PARTIAL = "FFEB9C"         # Light yellow (⚠️ Partial)
COLOR_MISSING = "FFC7CE"         # Light red (❌ No)
COLOR_PLANNED = "B4C7E7"         # Light blue (📋 Planned)

# Standard column widths
WIDTH_NARROW = 12
WIDTH_MEDIUM = 20
WIDTH_WIDE = 25
WIDTH_EXTRA_WIDE = 30
WIDTH_DESCRIPTION = 35


# ============================================================================
# SECTION 2: WORKBOOK CREATION & STYLE DEFINITIONS
# ============================================================================

def create_workbook() -> Workbook:
    """Create workbook with all required sheets."""
    wb = Workbook()
    
    # Remove default sheet
    if "Sheet" in wb.sheetnames:
        wb.remove(wb["Sheet"])
    
    # Create all sheets in order
    sheets = [
        "Instructions_Legend",
        "[Sheet2_Name]",
        "[Sheet3_Name]",
        # ... all sheets for this workbook
        "Gap_Analysis",
        "Evidence_Register",
        "Summary_Dashboard",
    ]
    
    for sheet_name in sheets:
        wb.create_sheet(title=sheet_name)
    
    return wb


def setup_styles():
    """
    Define all cell styles used throughout the workbook.
    Returns style TEMPLATES (dictionaries), not reusable objects.
    
    CRITICAL: Do NOT create shared Font/Fill/Border objects.
    Each cell gets its OWN style instance to avoid openpyxl issues.
    """
    return {
        "header": {
            "font": Font(name="Arial", size=16, bold=True, color="FFFFFF"),
            "fill": PatternFill(start_color=COLOR_HEADER, end_color=COLOR_HEADER, fill_type="solid"),
            "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
            "border": Border(
                left=Side(style="thin"),
                right=Side(style="thin"),
                top=Side(style="thin"),
                bottom=Side(style="thin")
            )
        },
        "subheader": {
            "font": Font(name="Arial", size=12, bold=True, color="FFFFFF"),
            "fill": PatternFill(start_color=COLOR_SUBHEADER, end_color=COLOR_SUBHEADER, fill_type="solid"),
            "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
            "border": Border(
                left=Side(style="thin"),
                right=Side(style="thin"),
                top=Side(style="thin"),
                bottom=Side(style="thin")
            )
        },
        "column_header": {
            "font": Font(name="Arial", size=10, bold=True),
            "fill": PatternFill(start_color=COLOR_COLUMN_HEADER, end_color=COLOR_COLUMN_HEADER, fill_type="solid"),
            "alignment": Alignment(horizontal="center", vertical="center", wrap_text=True),
            "border": Border(
                left=Side(style="thin"),
                right=Side(style="thin"),
                top=Side(style="thin"),
                bottom=Side(style="thin")
            )
        },
        "input_cell": {
            "fill": PatternFill(start_color=COLOR_INPUT, end_color=COLOR_INPUT, fill_type="solid"),
            "alignment": Alignment(horizontal="left", vertical="top", wrap_text=True),
            "border": Border(
                left=Side(style="thin"),
                right=Side(style="thin"),
                top=Side(style="thin"),
                bottom=Side(style="thin")
            )
        },
        "data_cell": {
            "alignment": Alignment(horizontal="left", vertical="top", wrap_text=True),
            "border": Border(
                left=Side(style="thin"),
                right=Side(style="thin"),
                top=Side(style="thin"),
                bottom=Side(style="thin")
            )
        },
    }


def apply_style(cell, style_dict):
    """
    Apply style template to cell by creating NEW instances.
    NEVER reuse Font/Fill/Border objects across cells.
    """
    if "font" in style_dict:
        cell.font = Font(**{k: v for k, v in style_dict["font"].__dict__.items() if not k.startswith('_')})
    if "fill" in style_dict:
        cell.fill = PatternFill(**{k: v for k, v in style_dict["fill"].__dict__.items() if not k.startswith('_')})
    if "alignment" in style_dict:
        cell.alignment = Alignment(**{k: v for k, v in style_dict["alignment"].__dict__.items() if not k.startswith('_')})
    if "border" in style_dict:
        cell.border = Border(**{k: v for k, v in style_dict["border"].__dict__.items() if not k.startswith('_')})


# ============================================================================
# SECTION 3: DATA VALIDATIONS
# ============================================================================

def create_data_validations():
    """
    Create data validation objects.
    MUST be added to worksheet.add_data_validation() and then cells added to validation.
    """
    return {
        "yes_no_partial": DataValidation(
            type="list",
            formula1='"Yes,No,Partial,Planned,N/A"',
            allow_blank=False,
            showDropDown=True,
            showErrorMessage=True,
            error="Invalid value. Select from dropdown.",
            errorTitle="Invalid Entry"
        ),
        "compliance": DataValidation(
            type="list",
            formula1='"Compliant,Non-Compliant,Partial,Planned,N/A"',
            allow_blank=False,
            showDropDown=True
        ),
        "severity": DataValidation(
            type="list",
            formula1='"Critical,High,Medium,Low"',
            allow_blank=False,
            showDropDown=True
        ),
        "risk_level": DataValidation(
            type="list",
            formula1='"Very High,High,Medium,Low,Very Low"',
            allow_blank=False,
            showDropDown=True
        ),
        # ... add more validations as needed per workbook
    }


# ============================================================================
# SECTION 4: SHEET CREATION FUNCTIONS
# ============================================================================

def create_instructions(ws, styles):
    """Create Instructions & Legend sheet."""
    
    # Header
    ws.merge_cells('A1:H1')
    ws['A1'] = f"ISMS Control {WORKBOOK_ID} - {ASSESSMENT_AREA}"
    apply_style(ws['A1'], styles["header"])
    ws.row_dimensions[1].height = 40
    
    # Subheader
    ws.merge_cells('A2:H2')
    ws['A2'] = f"ISO/IEC 27001:2022 Control {CONTROL_ID} - Data Leakage Prevention"
    apply_style(ws['A2'], styles["subheader"])
    
    # Document Info
    info = [
        ("Document ID:", WORKBOOK_ID),
        ("Assessment Area:", ASSESSMENT_AREA),
        ("Related Policy:", RELATED_POLICY),
        ("Version:", WORKBOOK_VERSION),
        ("Assessment Date:", "[USER INPUT]"),
        ("Completed By:", "[USER INPUT]"),
        ("Organization:", "[USER INPUT]"),
        ("Review Cycle:", "Quarterly"),
    ]
    
    row = 4
    for label, value in info:
        ws[f'A{row}'] = label
        ws[f'A{row}'].font = Font(bold=True)
        ws[f'B{row}'] = value
        if "USER INPUT" in value:
            ws[f'B{row}'].fill = PatternFill(start_color=COLOR_INPUT, end_color=COLOR_INPUT, fill_type="solid")
        row += 1
    
    # HOW TO USE THIS WORKBOOK section
    row += 2
    ws[f'A{row}'] = "HOW TO USE THIS WORKBOOK"
    ws[f'A{row}'].font = Font(bold=True, size=12)
    row += 1
    
    instructions = [
        "1. Complete each worksheet tab in sequence",
        "2. Fill ALL yellow-highlighted cells with your organization's information",
        "3. Use dropdown menus where provided (do not type free-form text in dropdown cells)",
        "4. Document all [specific items for this workbook]",
        "5. Provide evidence IDs for all assessments",
        "6. Review Summary Dashboard for overall compliance score",
        "7. Identify gaps and create remediation plans",
        "8. Obtain CISO/DPO approval before finalizing",
        "... [add workbook-specific instructions]",
    ]
    
    for instruction in instructions:
        ws[f'A{row}'] = instruction
        row += 1
    
    # LEGEND section
    row += 2
    ws[f'A{row}'] = "LEGEND - RESPONSE VALUES"
    ws[f'A{row}'].font = Font(bold=True, size=12)
    row += 1
    
    legend = [
        ("Yes", "Fully implemented and documented", COLOR_COMPLETE),
        ("No", "Not implemented", COLOR_MISSING),
        ("Partial", "Partially implemented (explain in notes)", COLOR_PARTIAL),
        ("Planned", "Scheduled for implementation (provide target date)", COLOR_PLANNED),
        ("N/A", "Not applicable (provide justification)", "FFFFFF"),
    ]
    
    for value, description, color in legend:
        ws[f'A{row}'] = value
        ws[f'A{row}'].fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
        ws[f'B{row}'] = description
        row += 1
    
    # Set column widths
    ws.column_dimensions['A'].width = WIDTH_MEDIUM
    ws.column_dimensions['B'].width = WIDTH_EXTRA_WIDE
    
    # Freeze panes at row 3
    ws.freeze_panes = 'A3'


def create_assessment_sheet(ws, styles, sheet_title, columns, row_count, checklist_items=None):
    """
    Generic function to create assessment sheets.
    
    Args:
        ws: Worksheet object
        styles: Style templates dictionary
        sheet_title: Title for the sheet
        columns: Dictionary of column definitions {"col_letter": "Column Header"}
        row_count: Number of data rows to create
        checklist_items: Optional list of pre-populated checklist items
    """
    
    # Header
    ws.merge_cells('A1:' + get_column_letter(len(columns)) + '1')
    ws['A1'] = sheet_title
    apply_style(ws['A1'], styles["header"])
    ws.row_dimensions[1].height = 30
    
    # Subheader with instructions
    ws.merge_cells('A2:' + get_column_letter(len(columns)) + '2')
    ws['A2'] = "[Sheet-specific instructions/guidance]"
    apply_style(ws['A2'], styles["subheader"])
    
    # Column headers (row 3)
    col_idx = 1
    for col_letter, col_header in columns.items():
        cell = ws[f'{col_letter}3']
        cell.value = col_header
        apply_style(cell, styles["column_header"])
        ws.column_dimensions[col_letter].width = WIDTH_MEDIUM  # Adjust per column
        col_idx += 1
    
    # Data rows
    start_row = 4
    end_row = start_row + row_count - 1
    
    for row in range(start_row, end_row + 1):
        # If checklist items provided, pre-populate column A
        if checklist_items and (row - start_row) < len(checklist_items):
            ws[f'A{row}'] = checklist_items[row - start_row]
        
        # Apply input cell styling to user-fillable columns
        for col_letter in columns.keys():
            cell = ws[f'{col_letter}{row}']
            apply_style(cell, styles["input_cell"])
    
    # Freeze panes at row 4 (after column headers)
    ws.freeze_panes = 'A4'


def create_gap_analysis(ws, styles):
    """Create Gap Analysis sheet (standard across all workbooks)."""
    
    columns = {
        'A': 'Gap ID',
        'B': 'Gap Description',
        'C': 'Affected Area',
        'D': 'Risk Level',
        'E': 'Business Impact',
        'F': 'Root Cause',
        'G': 'Remediation Plan',
        'H': 'Owner',
        'I': 'Target Date',
        'J': 'Status',
        'K': 'Evidence ID',
    }
    
    create_assessment_sheet(
        ws, styles,
        "GAP ANALYSIS - IDENTIFIED DEFICIENCIES",
        columns,
        40  # 40 gap rows
    )
    
    # Add data validations
    validations = create_data_validations()
    ws.add_data_validation(validations['risk_level'])
    for row in range(4, 44):
        validations['risk_level'].add(ws[f'D{row}'])
    
    # Add status validation
    status_val = DataValidation(
        type="list",
        formula1='"Open,In Progress,Resolved,Accepted,Closed"',
        allow_blank=False
    )
    ws.add_data_validation(status_val)
    for row in range(4, 44):
        status_val.add(ws[f'J{row}'])


def create_evidence_register(ws, styles):
    """Create Evidence Register sheet (standard across all workbooks)."""
    
    columns = {
        'A': 'Evidence ID',
        'B': 'Evidence Type',
        'C': 'Description',
        'D': 'Location/Link',
        'E': 'Date Collected',
        'F': 'Collected By',
        'G': 'Related Requirement',
        'H': 'Verification Status',
    }
    
    create_assessment_sheet(
        ws, styles,
        "EVIDENCE REGISTER - AUDIT TRAIL",
        columns,
        100  # 100 evidence entries
    )
    
    # Add evidence type validation
    evidence_type_val = DataValidation(
        type="list",
        formula1='"Screenshot,Configuration File,Policy Document,Log Export,Report,Certificate,Email,Meeting Minutes,Other"',
        allow_blank=False
    )
    ws.add_data_validation(evidence_type_val)
    for row in range(4, 104):
        evidence_type_val.add(ws[f'B{row}'])


def create_summary_dashboard(ws, styles):
    """Create Summary Dashboard sheet."""
    
    # Header
    ws.merge_cells('A1:F1')
    ws['A1'] = f"{ASSESSMENT_AREA} - COMPLIANCE DASHBOARD"
    apply_style(ws['A1'], styles["header"])
    ws.row_dimensions[1].height = 35
    
    # KPI Section
    ws.merge_cells('A3:F3')
    ws['A3'] = "KEY PERFORMANCE INDICATORS"
    apply_style(ws['A3'], styles["subheader"])
    
    kpi_headers = ['KPI', 'Current Value', 'Target', 'Status', 'Trend', 'Notes']
    for col_idx, header in enumerate(kpi_headers, start=1):
        cell = ws[f'{get_column_letter(col_idx)}4']
        cell.value = header
        apply_style(cell, styles["column_header"])
    
    # Add KPIs with formulas (adjust per workbook)
    kpis = [
        ("Overall Compliance Score %", "=...", "≥90%"),
        ("[Workbook-specific KPI 1]", "=...", "[target]"),
        ("[Workbook-specific KPI 2]", "=...", "[target]"),
        # ... add all KPIs for this workbook
    ]
    
    row = 5
    for kpi_name, formula, target in kpis:
        ws[f'A{row}'] = kpi_name
        ws[f'B{row}'] = formula
        ws[f'C{row}'] = target
        ws[f'D{row}'] = '=IF(B{}>C{},"✅ Compliant","❌ Non-Compliant")'.format(row, row)
        row += 1
    
    # Gap Summary Section
    row += 2
    ws.merge_cells(f'A{row}:F{row}')
    ws[f'A{row}'] = "GAP SUMMARY"
    apply_style(ws[f'A{row}'], styles["subheader"])
    row += 1
    
    # Gap rollup table
    # ... (add gap summary with formulas from Gap_Analysis sheet)
    
    # Set column widths
    ws.column_dimensions['A'].width = WIDTH_EXTRA_WIDE
    ws.column_dimensions['B'].width = WIDTH_MEDIUM
    ws.column_dimensions['C'].width = WIDTH_MEDIUM
    ws.column_dimensions['D'].width = WIDTH_MEDIUM
    ws.column_dimensions['E'].width = WIDTH_NARROW
    ws.column_dimensions['F'].width = WIDTH_WIDE
    
    # Freeze panes
    ws.freeze_panes = 'A5'


# ============================================================================
# SECTION 5: MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    
    print("=" * 78)
    print(f"{WORKBOOK_ID} - {ASSESSMENT_AREA} Generator")
    print(f"ISO/IEC 27001:2022 Control {CONTROL_ID}")
    print("=" * 78)
    
    wb = create_workbook()
    styles = setup_styles()
    
    print("\n[1/X] Creating Instructions & Legend...")
    create_instructions(wb["Instructions_Legend"], styles)
    
    print("[2/X] Creating [Sheet2]...")
    # create_sheet2(wb["Sheet2"], styles)
    
    # ... create all sheets
    
    print("[X-2/X] Creating Gap Analysis...")
    create_gap_analysis(wb["Gap_Analysis"], styles)
    
    print("[X-1/X] Creating Evidence Register...")
    create_evidence_register(wb["Evidence_Register"], styles)
    
    print("[X/X] Creating Summary Dashboard...")
    create_summary_dashboard(wb["Summary_Dashboard"], styles)
    
    # Save workbook
    filename = f"{WORKBOOK_ID}_{ASSESSMENT_AREA.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.xlsx"
    wb.save(filename)
    
    print(f"\n✅ SUCCESS: {filename}")
    print("\nWorkbook Structure:")
    print("  • Instructions & Legend")
    print("  • [List all sheets]")
    print("  • Gap Analysis (40 rows)")
    print("  • Evidence Register (100 rows)")
    print("  • Summary Dashboard (KPIs + compliance tracking)")
    print("\n" + "=" * 78)


if __name__ == "__main__":
    main()
```

---

## 5. Critical Implementation Rules

### 5.1 Style Object Handling (CRITICAL!)

**NEVER create shared style objects across cells!**

❌ **WRONG (causes openpyxl errors):**
```python
header_font = Font(name="Arial", size=16, bold=True, color="FFFFFF")
ws['A1'].font = header_font
ws['B1'].font = header_font  # REUSING SAME OBJECT - BREAKS!
```

✅ **CORRECT (each cell gets own instance):**
```python
def apply_style(cell, style_dict):
    if "font" in style_dict:
        cell.font = Font(**{k: v for k, v in style_dict["font"].__dict__.items() if not k.startswith('_')})
```

**Use style TEMPLATES (dictionaries) not objects!**

### 5.2 Data Validation Handling

**Data validations must be:**
1. Created as DataValidation objects
2. Added to worksheet via `ws.add_data_validation(validation)`
3. Cells added to validation via `validation.add(cell)`
```python
# Create validation
val = DataValidation(type="list", formula1='"Yes,No,Partial"')

# Add to worksheet
ws.add_data_validation(val)

# Add cells to validation
for row in range(4, 44):
    val.add(ws[f'C{row}'])
```

### 5.3 Formula Handling

**Internal formulas (within workbook):**
```python
ws['B5'] = '=COUNTIF(Data_Sheet!$D$4:$D$43,"Yes")'
```

**External formulas (Domain 5 dashboard linking to Domains 1-4):**
```python
# Use placeholders
ws['B5'] = '=[A812-1]Summary_Dashboard!$B$5'

# Provide instructions for user to Find & Replace:
# Find: [A812-1]
# Replace: [ISMS-IMP-A.8.12.1_DLP_Infrastructure_20250104.xlsx]
```

### 5.4 Freeze Panes

**Standard freeze panes:**
- **Instructions sheet**: `ws.freeze_panes = 'A3'` (after document info)
- **Assessment sheets**: `ws.freeze_panes = 'A4'` (after column headers)
- **Dashboard sheets**: `ws.freeze_panes = 'A5'` (after KPI headers)

### 5.5 Column Widths

Use consistent widths:
- **Narrow**: 12 (IDs, status icons)
- **Medium**: 20 (names, dates)
- **Wide**: 25 (descriptions)
- **Extra Wide**: 30 (long text, instructions)
- **Description**: 35 (detailed explanations)

### 5.6 Row Heights

- **Headers**: 35-40 (merged cell titles)
- **Subheaders**: 25-30
- **Data rows**: Default (15) or auto-adjust

---

## 6. Workbook-Specific Requirements

### 6.1 Domain 1 (Infrastructure) Specific Requirements

**Pre-Populate Technology Examples:**
- Forcepoint DLP (Network, Endpoint, Email)
- Symantec DLP (Network, Endpoint, Email, Cloud)
- Microsoft Purview DLP (M365, Endpoint)
- Google Workspace DLP (Gmail, Drive)
- Netskope CASB (Cloud Apps)
- Zscaler (Web, Cloud)

**Key Formulas:**
- Technology count by deployment type
- Coverage % = (Protected channels / Total channels) × 100
- Integration score = (Integrated systems / Required systems) × 100

### 6.2 Domain 2 (Classification) Specific Requirements

**Pre-Populate Data Categories:**
- PII (FADP/GDPR Article 6)
- Special Categories PII (GDPR Article 9)
- Financial Data (PCI DSS, bank accounts, credit cards)
- Intellectual Property (patents, source code, trade secrets)
- Credentials (passwords, API keys, SSH keys, certificates)
- Business Confidential (contracts, M&A, strategies)

**Regulatory Mapping:**
- FADP Article 4 (Personal Data definition)
- FADP Article 5 (Special Categories)
- GDPR Article 4(1) (Personal Data)
- GDPR Article 9 (Special Categories)
- PCI DSS (Payment Card Data)

### 6.3 Domain 3 (Channel Coverage) Specific Requirements

**Pre-Populate Channels:**
1. **Email**: SMTP, Webmail, M365, Gmail, Encrypted Email
2. **Web/Cloud**: HTTP/HTTPS, Dropbox, Box, OneDrive, Google Drive, GitHub, SaaS
3. **Endpoint**: USB, Print, Clipboard, Screen Capture, Bluetooth, Sync Apps
4. **Network**: SMB, FTP, SFTP, NFS, SCP, WebDAV
5. **Application**: Databases, APIs, Reporting (Crystal, Tableau, Power BI), CRM, ERP
6. **Mobile**: MDM, MAM, BYOD, Mobile Email, Mobile Cloud

**Coverage Calculation:**
```
Channel Coverage % = (Protected sub-channels / Total sub-channels) × 100
Overall Coverage % = Weighted average of all 6 channels
```

### 6.4 Domain 4 (Monitoring) Specific Requirements

**Pre-Populate Alert Rules:**
- Credentials detected outbound (Severity: Critical, SLA: 15 min)
- Mass exfiltration (>100 files or >1GB in <10 min) (Severity: Critical, SLA: 15 min)
- PII to external recipient (Severity: High, SLA: 1 hour)
- Repeated blocking same user (>5 in 1 hour) (Severity: High, SLA: 1 hour)
- Confidential data to unapproved destination (Severity: Medium, SLA: 4 hours)

**KPIs to Track:**
- MTTD (Mean Time To Detect) - target <5 min for Critical
- MTTR (Mean Time To Respond) - target <15 min for Critical
- False Positive Rate - target <10% after 6 months
- SLA Compliance % - target >90%
- Incident Recurrence Rate - target <5%

### 6.5 Domain 5 (Dashboard) Specific Requirements

**External Formula Placeholders:**
```python
# Domain 1 rollup
ws['B5'] = '=[A812-1]Summary_Dashboard!$B$10'  # Infrastructure compliance score

# Domain 2 rollup
ws['B6'] = '=[A812-2]Summary_Dashboard!$B$10'  # Classification compliance score

# Domain 3 rollup
ws['B7'] = '=[A812-3]Summary_Dashboard!$B$10'  # Channel coverage score

# Domain 4 rollup
ws['B8'] = '=[A812-4]Summary_Dashboard!$B$10'  # Monitoring effectiveness score

# Overall score
ws['B10'] = '=AVERAGE(B5:B8)'  # Weighted average of all domains
```

**Pre-Defined Risks (Risk Register):**
1. Insufficient DLP coverage on email channel
2. Endpoint DLP agents not deployed to all devices
3. False positive rate >20% causing alert fatigue
4. No DLP monitoring on cloud applications
5. MTTD exceeds 15 minutes for Critical incidents
6. Data classification schema not applied consistently
7. PII transfer to external parties without encryption
8. No automated blocking for credentials
9. Incident response procedures not documented
10. SIEM integration incomplete (logs not forwarded)
11. Mobile devices (BYOD) not protected by DLP
12. Database exports not monitored for bulk exfiltration
13. No breach notification process defined
14. DLP policy exceptions not tracked/reviewed
15. Training completion rate <80%
16. Works council not consulted (if required)
17. DPO not involved in DLP deployment (privacy impact)
18. Vendor support contracts expiring within 90 days
19. DLP solution EOL/deprecated (replacement needed)
20. Budget insufficient for full channel coverage

---

## 7. Testing and Validation

### 7.1 Post-Generation Testing

After generating each workbook:

1. **Open in Excel/LibreOffice** - verify no corruption
2. **Test dropdowns** - all validations working
3. **Test formulas** - calculations correct
4. **Check styling** - consistent colors, no style errors
5. **Verify freeze panes** - correct rows frozen
6. **Test save/re-open** - no data loss

### 7.2 Validation Scripts (from A.8.11 pattern)

**Generic Validation:**
```bash
python3 excel_sanity_check.py ISMS-IMP-A.8.12.1_DLP_Infrastructure_20250104.xlsx
```

**Specialized Validation:**
```bash
python3 excel_sanity_check_a812_1.py ISMS-IMP-A.8.12.1_DLP_Infrastructure_20250104.xlsx
```

**Style Object Detection:**
```bash
python3 style_object_checker.py ISMS-IMP-A.8.12.1_DLP_Infrastructure_20250104.xlsx
```

**Auto-Fix Style Issues:**
```bash
python3 style_object_patcher.py ISMS-IMP-A.8.12.1_DLP_Infrastructure_20250104.xlsx
```

---

## 8. File Naming Conventions

**Generated Workbooks:**
```
ISMS-IMP-A.8.12.1_DLP_Infrastructure_20250104.xlsx
ISMS-IMP-A.8.12.2_Data_Classification_20250104.xlsx
ISMS-IMP-A.8.12.3_Channel_Coverage_20250104.xlsx
ISMS-IMP-A.8.12.4_Monitoring_Response_20250104.xlsx
ISMS-IMP-A.8.12.5_Compliance_Dashboard_20250104.xlsx
```

**Python Scripts:**
```
generate_a812_1_dlp_infrastructure.py
generate_a812_2_data_classification.py
generate_a812_3_channel_coverage.py
generate_a812_4_monitoring_response.py
generate_a812_5_compliance_dashboard.py
```

**Validation Scripts:**
```
excel_sanity_check_a812_1.py
excel_sanity_check_a812_2.py
excel_sanity_check_a812_3.py
excel_sanity_check_a812_4.py
excel_sanity_check_a812_5.py
```

---

## 9. Success Criteria

### 9.1 Per-Workbook Success

✅ **Each workbook generator SHALL:**
- Generate without errors
- Create all specified sheets
- Apply consistent styling (colors, fonts, borders)
- Include all data validations (dropdowns working)
- Contain all required formulas (calculations correct)
- Freeze panes at correct positions
- Save without corruption
- Re-open without errors
- Pass validation scripts

### 9.2 Overall Framework Success

✅ **Complete framework SHALL:**
- 5 Python generators created
- 5 Excel workbooks generated
- All ~49 sheets functional
- ~310 assessment items present
- Consistent styling across all workbooks
- External formulas in Dashboard (Domain 5) linking to Domains 1-4
- Gap Analysis (40 rows) in all workbooks
- Evidence Register (100 rows) in all workbooks
- Summary Dashboard in all workbooks
- Instructions clear and comprehensive

---

## 10. Next Steps After Generation

1. **Execute all 5 generators** - create workbooks
2. **Run validation scripts** - check for errors
3. **Test in Excel** - verify functionality
4. **Create sample data** - test with realistic entries
5. **Document any issues** - for iterative improvement
6. **Create user guide** - how to complete assessments
7. **Train assessors** - Security/IT teams who will complete workbooks

---

**END OF INSTRUCTIONS**

*"These instructions are your blueprint. Follow them precisely, and you'll generate audit-ready DLP assessment workbooks that would make any CISO proud."* 🎯

**Token Status Check:** ~133K used / 190K total = ~57K remaining  
**Estimated Tokens Needed:** ~30-40K for full implementation generation  
**Verdict:** ✅ **SUFFICIENT TOKENS TO COMPLETE!**

Ready to generate the IMP layer when you return! 🚀