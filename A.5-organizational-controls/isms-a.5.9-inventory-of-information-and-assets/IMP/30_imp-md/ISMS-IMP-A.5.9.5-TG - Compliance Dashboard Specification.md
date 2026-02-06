**ISMS-IMP-A.5.9.5-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Executive Compliance Dashboard & Consolidated Metrics |
| **Related Policy** | ISMS-POL-A.5.9, Section 3 (Assessment Methodology), Requirement A.5.9-R9 (Reporting) |
| **Purpose** | Consolidate all A.5.9 assessment data into executive dashboard for management reporting and compliance tracking |
| **Target Audience** | CISO, Information Security Manager, Executive Management, Auditors, Board of Directors |
| **Assessment Type** | Consolidation & Executive Reporting |
| **Review Cycle** | Quarterly (after all 4 assessments completed) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial dashboard specification consolidating 4 assessment workbooks | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.9.5-UG.

---

# Technical Specification

**Audience:** Dashboard developers (Python/Excel script maintainers)

---

## Document Overview

### Purpose of Technical Specification

This section provides complete technical specifications for developers creating or maintaining the Python script that consolidates all 4 assessment workbooks into the executive compliance dashboard.

**Python Script**: `generate_assessment_5_compliance_dashboard.py`

**Input Files** (4 CSV exports):

- `A59_1_Discovery_Metrics_YYYYMMDD.csv`
- `A59_2_Maintenance_Metrics_YYYYMMDD.csv`
- `A59_3_Quality_Metrics_YYYYMMDD.csv`
- `A59_4_Accountability_Metrics_YYYYMMDD.csv`

**Generated Workbook**: `ISMS_A_5_9_Compliance_Dashboard_QX_YYYY.xlsx`

**Key Design Principles**:
1. **Automated Consolidation**: CSV import, not manual data entry
2. **Executive Focus**: Dashboard clarity over technical detail
3. **Audit Trail**: Preserve data lineage from assessments to dashboard
4. **Trending Capability**: Support quarter-over-quarter comparison
5. **Error Handling**: Graceful failure if CSVs malformed or missing

---

## Excel Workbook Structure

### Workbook Metadata

**Workbook Properties**:

- **Title**: ISMS A.5.9 Compliance Dashboard
- **Subject**: ISO/IEC 27001:2022 Control A.5.9 - Executive Reporting
- **Author**: [Organization] ISMS Implementation Team
- **Company**: [Organization]
- **Created**: [Generation Date]
- **Version**: 1.0

### Sheet Summary

| Sheet # | Sheet Name | Purpose | Data Source | User Input | Protection |
|---------|-----------|---------|-------------|------------|-----------|
| 1 | Executive Summary | One-page dashboard | Auto-calc from 2-6 | Executive narrative | Partial |
| 2 | Compliance Scorecard | All 4 assessment scores | Auto-calc from 3-6 | Trending manual | Partial |
| 3 | Discovery Metrics | IMP-A.5.9-1 data | CSV import | None | Full |
| 4 | Maintenance Metrics | IMP-A.5.9-2 data | CSV import | None | Full |
| 5 | Quality Metrics | IMP-A.5.9-3 data | CSV import | None | Full |
| 6 | Accountability Metrics | IMP-A.5.9-4 data | CSV import | None | Full |
| 7 | Trending Analysis | Quarter-over-quarter | Manual + auto-calc | Historical data | Partial |
| 8 | Action Register | Remediation priorities | Compiled from 3-6 | Status updates | Partial |

---

## Global Styling Standards

Same as IMP-A.5.9-1/2/3/4 (refer to those documents for color palette).

---

## CSV Import Specifications

### CSV File Format Requirements

**General Requirements**:

- **Encoding**: UTF-8 with BOM
- **Delimiter**: Comma (`,`)
- **Line Ending**: CRLF (`\r\n`) or LF (`\n`)
- **Header Row**: Required (first row)
- **Data Rows**: Starting from row 2

### CSV 1: Discovery Metrics (from IMP-A.5.9-1)

**Filename Pattern**: `A59_1_Discovery_Metrics_YYYYMMDD.csv`

**Required Columns**:
| Column | Type | Description |
|--------|------|-------------|
| Discovery_Domain | Text | Domain name (Info Assets, IT Infra, Apps, Physical, Personnel) |
| Target | Number (%) | Target completeness |
| Actual | Number (%) | Actual completeness |
| Gap | Number (%) | Gap vs. target |
| Status | Text | Compliance status (✅/⚠️/❌) |

**Sample CSV**:
```csv
Discovery_Domain,Target,Actual,Gap,Status
Information Assets,95,94,-1,⚠️
IT Infrastructure,98,98,0,✅
Applications,90,92,+2,✅
Physical Assets,90,91,+1,✅
Personnel Assets,100,100,0,✅
Overall Discovery Score,95,96,+1,✅
```

### CSV 2: Maintenance Metrics (from IMP-A.5.9-2)

**Filename Pattern**: `A59_2_Maintenance_Metrics_YYYYMMDD.csv`

**Required Columns**:
| Column | Type | Description |
|--------|------|-------------|
| Metric_Category | Text | Category (Update Timeliness, Integration Health, Data Quality, Review Compliance) |
| Target | Number (%) | Target |
| Actual | Number (%) | Current achievement |
| Gap | Number (%) | Gap |
| Status | Text | Compliance status |

**Sample CSV**:
```csv
Metric_Category,Target,Actual,Gap,Status
Update Timeliness,95,89,-6,⚠️
Integration Health,98,96,-2,⚠️
Data Quality,95,87,-8,⚠️
Review Compliance,95,73,-22,❌
Overall Maintenance Score,95,88,-7,⚠️
```

### CSV 3: Quality Metrics (from IMP-A.5.9-3)

**Filename Pattern**: `A59_3_Quality_Metrics_YYYYMMDD.csv`

**Required Columns**:
| Column | Type | Description |
|--------|------|-------------|
| Quality_Dimension | Text | Dimension (Accuracy, Completeness, Currency, Consistency, Policy Compliance) |
| Weight | Number (%) | Weighting |
| Target | Number (%) | Target score |
| Actual | Number (%) | Actual score |
| Gap | Number (%) | Gap |
| Status | Text | Compliance status |

**Sample CSV**:
```csv
Quality_Dimension,Weight,Target,Actual,Gap,Status
Accuracy,30,95,96,+1,✅
Completeness,25,100,94,-6,⚠️
Currency,20,100,92,-8,⚠️
Consistency,15,99,98.5,-0.5,✅
Policy Compliance,10,100,89,-11,⚠️
Overall Quality Score,100,97,94.2,-2.8,⚠️
```

### CSV 4: Accountability Metrics (from IMP-A.5.9-4)

**Filename Pattern**: `A59_4_Accountability_Metrics_YYYYMMDD.csv`

**Required Columns**:
| Column | Type | Description |
|--------|------|-------------|
| Accountability_Dimension | Text | Dimension (Coverage, Acknowledgment, Awareness, Performance) |
| Weight | Number (%) | Weighting |
| Target | Number (%) | Target score |
| Actual | Number (%) | Actual score |
| Gap | Number (%) | Gap |
| Status | Text | Compliance status |

**Sample CSV**:
```csv
Accountability_Dimension,Weight,Target,Actual,Gap,Status
Coverage,30,100,98,-2,⚠️
Acknowledgment,25,95,89,-6,⚠️
Awareness,20,100,85,-15,❌
Performance,25,80,76,-4,⚠️
Overall Accountability Score,100,94,88.1,-5.9,⚠️
```

---

## Sheet 1: Executive Summary - Complete Specification

### Purpose

One-page executive dashboard.

### Layout Structure

**Section A: Header & Overall Score** (Rows 1-12)
**Section B: Assessment Breakdown** (Rows 14-22)
**Section C: Top Priorities** (Rows 24-32)
**Section D: Executive Narrative** (Rows 34-45)
**Section E: Key Metrics** (Rows 47-58)
**Section F: Audit Readiness** (Rows 60-68)

### Section A: Header & Overall Score

```python
def create_header_section(ws):
    # Title
    ws.merge_cells('A1:P1')
    ws['A1'] = "CONTROL A.5.9 - COMPLIANCE DASHBOARD"
    ws['A1'].font = Font(size=18, bold=True, color='003366')
    ws['A1'].alignment = Alignment(horizontal='center')
    ws.row_dimensions[1].height = 35
    
    # Subtitle
    ws.merge_cells('A2:P2')
    ws['A2'] = "Asset Inventory Management - Executive Summary"
    ws['A2'].font = Font(size=12, color='666666')
    ws['A2'].alignment = Alignment(horizontal='center')
    
    # Assessment Quarter
    ws['A4'] = "Assessment Quarter:"
    ws['B4'] = f"Q{current_quarter} {current_year}"  # User configurable
    ws['A4'].font = Font(bold=True)
    
    ws['A5'] = "Assessment Date:"
    ws['B5'] = datetime.now().strftime('%d.%m.%Y')
    ws['A5'].font = Font(bold=True)
    
    # OVERALL COMPLIANCE SCORE (Large, prominent)
    ws.merge_cells('A7:D10')
    ws['A7'] = "OVERALL COMPLIANCE"
    ws['A7'].font = Font(size=14, bold=True, color='003366')
    ws['A7'].alignment = Alignment(horizontal='center', vertical='top')
    
    ws.merge_cells('A11:D11')
    # Formula: Weighted average of 4 assessments
    ws['A11'] = "=('Discovery Metrics'!B7*0.25)+('Maintenance Metrics'!B6*0.20)+('Quality Metrics'!B8*0.35)+('Accountability Metrics'!B7*0.20)"
    ws['A11'].number_format = '0.0"%"'
    ws['A11'].font = Font(size=36, bold=True)
    ws['A11'].alignment = Alignment(horizontal='center')
    
    # Compliance Status (Conditional)
    ws.merge_cells('A12:D12')
    ws['A12'] = '=IF(A11>=90,"✅ Compliant",IF(A11>=75,"⚠️ At Risk","❌ Non-Compliant"))'
    ws['A12'].font = Font(size=14, bold=True)
    ws['A12'].alignment = Alignment(horizontal='center')
    
    # Conditional formatting for A11 (overall score)
    # Green: ≥90%, Yellow: 75-89%, Red: <75%
    # (add conditional formatting rules)
```

### Section B: Assessment Breakdown

```python
def create_assessment_breakdown(ws, row_start=14):
    # Table header
    ws[f'A{row_start}'] = "ASSESSMENT BREAKDOWN"
    ws[f'A{row_start}'].font = Font(size=12, bold=True, color='003366')
    
    row = row_start + 2
    
    # Column headers
    headers = ['Assessment', 'Weight', 'Target', 'Actual', 'Gap', 'Status']
    for col_num, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_num, value=header)
        cell.font = Font(bold=True, color='FFFFFF')
        cell.fill = PatternFill(start_color='003366', fill_type='solid')
        cell.alignment = Alignment(horizontal='center')
    
    row += 1
    
    # Assessment rows (formulas pull from metric sheets)
    assessments = [
        ('Discovery', 25, '=\'Discovery Metrics\'!B7'),
        ('Maintenance', 20, '=\'Maintenance Metrics\'!B6'),
        ('Quality', 35, '=\'Quality Metrics\'!B8'),
        ('Accountability', 20, '=\'Accountability Metrics\'!B7')
    ]
    
    for assessment, weight, actual_formula in assessments:
        ws[f'A{row}'] = assessment
        ws[f'B{row}'] = weight
        ws[f'B{row}'].number_format = '0"%"'
        
        # Target (pull from respective metric sheet or use config)
        ws[f'C{row}'] = get_target_for_assessment(assessment)  # e.g., 95, 95, 97, 94
        ws[f'C{row}'].number_format = '0"%"'
        
        # Actual (formula to metric sheet)
        ws[f'D{row}'] = actual_formula
        ws[f'D{row}'].number_format = '0.0"%"'
        
        # Gap
        ws[f'E{row}'] = f'=D{row}-C{row}'
        ws[f'E{row}'].number_format = '0.0"%"'
        
        # Status (conditional)
        ws[f'F{row}'] = f'=IF(D{row}>=C{row},"✅",IF(D{row}>=C{row}-10,"⚠️","❌"))'
        ws[f'F{row}'].alignment = Alignment(horizontal='center')
        
        row += 1
    
    # Overall row (bold, larger font)
    ws[f'A{row}'] = "OVERALL"
    ws[f'A{row}'].font = Font(bold=True, size=12)
    ws[f'B{row}'] = 100
    ws[f'B{row}'].number_format = '0"%"'
    ws[f'C{row}'] = 95  # Overall target (configurable)
    ws[f'C{row}'].number_format = '0"%"'
    ws[f'D{row}'] = '=A11'  # Link to overall score
    ws[f'D{row}'].number_format = '0.0"%"'
    ws[f'D{row}'].font = Font(bold=True, size=12)
    ws[f'E{row}'] = f'=D{row}-C{row}'
    ws[f'E{row}'].number_format = '0.0"%"'
    ws[f'E{row}'].font = Font(bold=True)
    ws[f'F{row}'] = '=F12'  # Link to overall status
    ws[f'F{row}'].alignment = Alignment(horizontal='center')
    ws[f'F{row}'].font = Font(bold=True, size=12)
```

### Section C: Top Priorities

```python
def create_top_priorities(ws, row_start=24):
    ws[f'A{row_start}'] = "TOP 3 PRIORITIES THIS QUARTER"
    ws[f'A{row_start}'].font = Font(size=12, bold=True, color='003366')
    
    row = row_start + 2
    
    # Headers
    headers = ['Priority', 'Gap Description', 'Severity', 'Owner', 'Target Date', 'Status']
    for col_num, header in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_num, value=header)
        cell.font = Font(bold=True)
    
    row += 1
    
    # Priority 1-3 rows (user fills these, or pulled from Action Register sheet)
    # These can be manually entered or auto-populated from top of Action Register
    for priority_num in range(1, 4):
        ws[f'A{row}'] = priority_num
        ws[f'A{row}'].alignment = Alignment(horizontal='center')
        ws[f'A{row}'].font = Font(bold=True)
        
        # Gap description - user enters or formula from Action Register
        ws[f'B{row}'] = f'=IF(\'Action Register\'!B{priority_num+2}<>"",\'Action Register\'!B{priority_num+2},"[To be determined]")'
        ws[f'B{row}'].alignment = Alignment(horizontal='left', wrap_text=True)
        
        # Severity
        ws[f'C{row}'] = f'=IF(\'Action Register\'!D{priority_num+2}<>"",\'Action Register\'!D{priority_num+2},"")'
        
        # Owner
        ws[f'D{row}'] = f'=IF(\'Action Register\'!H{priority_num+2}<>"",\'Action Register\'!H{priority_num+2},"")'
        
        # Target Date
        ws[f'E{row}'] = f'=IF(\'Action Register\'!I{priority_num+2}<>"",\'Action Register\'!I{priority_num+2},"")'
        ws[f'E{row}'].number_format = 'DD.MM.YYYY'
        
        # Status
        ws[f'F{row}'] = f'=IF(\'Action Register\'!J{priority_num+2}<>"",\'Action Register\'!J{priority_num+2},"")'
        
        row += 1
```

### Section D: Executive Narrative

```python
def create_executive_narrative_section(ws, row_start=34):
    ws[f'A{row_start}'] = "EXECUTIVE NARRATIVE"
    ws[f'A{row_start}'].font = Font(size=12, bold=True, color='003366')
    
    row = row_start + 2
    
    # Merged cell for narrative (user enters 2-3 paragraphs)
    ws.merge_cells(f'A{row}:P{row+8}')
    ws[f'A{row}'] = """[User enters executive narrative here - 2-3 paragraphs]

Template:

- Paragraph 1: Current state summary (overall score, comparison to target)
- Paragraph 2: Key achievements this quarter (specific accomplishments, quantified improvements)
- Paragraph 3: Critical gaps and recommended actions (specific gaps, proposed remediation, resource needs)

"""
    ws[f'A{row}'].alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
    ws[f'A{row}'].font = Font(size=11)
    ws.row_dimensions[row].height = 150
    
    # User replaces template with actual narrative
    ws[f'A{row}'].protection = Protection(locked=False)  # Unlocked for editing
```

### Section E: Key Metrics

```python
def create_key_metrics(ws, row_start=47):
    ws[f'A{row_start}'] = "KEY METRICS AT A GLANCE"
    ws[f'A{row_start}'].font = Font(size=12, bold=True, color='003366')
    
    row = row_start + 2
    
    metrics = [
        ('Total Assets Inventoried', '=\'Discovery Metrics\'!B2', 'From Discovery'),
        ('Asset Categories Covered', '5 of 5', 'Fixed'),
        ('Ownership Coverage', '=\'Accountability Metrics\'!D3', 'From Accountability'),
        ('Data Quality Score', '=\'Quality Metrics\'!D8', 'From Quality'),
        ('Critical Assets at Risk', '[Manual Entry]', 'From assessments'),
        ('High Priority Gaps', '=COUNTIF(\'Action Register\'!D:D,"Critical")+COUNTIF(\'Action Register\'!D:D,"High")', 'From Action Register')
    ]
    
    for metric_name, formula_or_value, source in metrics:
        ws[f'A{row}'] = metric_name
        ws[f'A{row}'].font = Font(bold=True)
        
        if formula_or_value.startswith('='):
            ws[f'B{row}'] = formula_or_value
        else:
            ws[f'B{row}'] = formula_or_value
        
        ws[f'B{row}'].font = Font(size=11)
        row += 1
```

### Section F: Audit Readiness

```python
def create_audit_readiness(ws, row_start=60):
    ws[f'A{row_start}'] = "AUDIT READINESS"
    ws[f'A{row_start}'].font = Font(size=12, bold=True, color='003366')
    
    row = row_start + 2
    
    # ISO Control Status
    ws[f'A{row}'] = "ISO/IEC 27001:2022 Control A.5.9:"
    ws[f'A{row}'].font = Font(bold=True)
    ws[f'B{row}'] = '=F12'  # Link to overall compliance status
    ws[f'B{row}'].alignment = Alignment(horizontal='center')
    ws[f'B{row}'].font = Font(bold=True, size=12)
    row += 1
    
    # Evidence Completeness
    ws[f'A{row}'] = "Evidence Completeness:"
    ws[f'A{row}'].font = Font(bold=True)
    ws[f'B{row}'] = '[Manual: % of evidence collected]'  # User enters
    ws[f'B{row}'].protection = Protection(locked=False)
    row += 1
    
    # Last Audit Finding
    ws[f'A{row}'] = "Last Audit Findings:"
    ws[f'A{row}'].font = Font(bold=True)
    ws[f'B{row}'] = '[Manual: Open/Closed/N/A]'
    ws[f'B{row}'].protection = Protection(locked=False)
    row += 1
    
    # Next Audit Preparation
    ws[f'A{row}'] = "Next Audit Preparation:"
    ws[f'A{row}'].font = Font(bold=True)
    ws[f'B{row}'] = '[Manual: On Track/At Risk/Behind]'
    ws[f'B{row}'].protection = Protection(locked=False)
```

---

## Sheet 2: Compliance Scorecard - Complete Specification

### Purpose

Detailed breakdown of all 4 assessments.

### Table Structure

**Table 1: Assessment Summary** (Rows 3-12)

Columns: Assessment | Weight | Target | Actual | Gap | Status | Trend

**Table 2: Dimension Details** (Rows 15+)

For each assessment, show sub-dimensions:

```python
def create_scorecard_sheet(ws):
    # Table 1: Assessment Summary
    create_assessment_summary_table(ws, row_start=3)
    
    # Table 2: Discovery Breakdown
    create_discovery_breakdown(ws, row_start=15)
    
    # Table 3: Maintenance Breakdown
    create_maintenance_breakdown(ws, row_start=25)
    
    # Table 4: Quality Breakdown
    create_quality_breakdown(ws, row_start=35)
    
    # Table 5: Accountability Breakdown
    create_accountability_breakdown(ws, row_start=50)
    
    # Traffic Light Summary
    create_traffic_light_summary(ws, row_start=65)
```

Formulas pull directly from Sheets 3-6 (imported CSV data).

---

## Sheets 3-6: CSV Import Sheets - Specification

### Sheet 3: Discovery Metrics

**Import Source**: `A59_1_Discovery_Metrics_YYYYMMDD.csv`

**Layout**:

- Row 1: Headers
- Rows 2+: Data from CSV

**Python Implementation**:

```python
def import_discovery_metrics(ws, csv_filepath):
    """Import Discovery CSV into Sheet 3"""
    import csv
    
    with open(csv_filepath, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row_num, row_data in enumerate(reader, start=1):
            for col_num, cell_value in enumerate(row_data, start=1):
                cell = ws.cell(row=row_num, column=col_num)
                
                # Try to convert to number if possible
                try:
                    cell.value = float(cell_value)
                except ValueError:
                    cell.value = cell_value
                
                # Header formatting
                if row_num == 1:
                    cell.font = Font(bold=True, color='FFFFFF')
                    cell.fill = PatternFill(start_color='003366', fill_type='solid')
                    cell.alignment = Alignment(horizontal='center')
    
    # Protect sheet (read-only, imported data)
    ws.protection.sheet = True
```

### Sheets 4-6: Same Pattern

Same CSV import logic for Maintenance, Quality, and Accountability metrics.

---

## Sheet 7: Trending Analysis - Specification

### Purpose

Quarter-over-quarter comparison.

### Table Structure

**Historical Data Table** (manual entry for past quarters):

| Quarter | Overall | Discovery | Maintenance | Quality | Accountability |
|---------|---------|-----------|-------------|---------|----------------|
| Q4 2025 | 89.1% | 93% | 84% | 91% | 85% |
| Q1 2026 | 92.8% (formula) | 96% (formula) | 89% (formula) | 94.2% (formula) | 88.1% (formula) |
| Q2 2026 | (future) | (future) | (future) | (future) | (future) |

**Formulas for Current Quarter**:
```python
# Overall Score for current quarter
ws['B5'] = '=\'Executive Summary\'!A11'

# Discovery Score for current quarter
ws['C5'] = '=\'Discovery Metrics\'!B7'

# etc.
```

**Trend Calculation**:
```python
# Improvement Rate
ws['G5'] = '=(B5-B4)/B4*100'  # % change vs. previous quarter
ws['G5'].number_format = '0.0"%"'

# Trend Direction
ws['H5'] = '=IF(G5>1,"↗️ Improved",IF(G5<-1,"↘️ Degraded","→ Stable"))'
```

**Forecast** (simple linear projection):
```python
# Projected Q+1
ws['B6'] = '=B5+(B5-B4)'  # Linear: Current + (Current - Previous)
```

---

## Sheet 8: Action Register - Specification

### Purpose

Consolidated gaps from all 4 assessments with prioritization.

### Column Structure

| Col | Header | Width | Source |
|-----|--------|-------|--------|
| A | Priority | 10 | Auto-ranked |
| B | Gap Description | 50 | From assessments |
| C | Source Assessment | 20 | Discovery/Maintenance/Quality/Accountability |
| D | Severity | 15 | From assessment |
| E | Impact | 15 | Manual entry |
| F | Effort | 15 | Manual entry |
| G | Priority Score | 12 | Auto-calculated |
| H | Owner | 25 | From assessment or assigned |
| I | Target Date | 15 | From assessment or set |
| J | Status | 15 | Dropdown |
| K | % Complete | 10 | Manual |
| L | Evidence | 30 | Link |
| M | Notes | 30 | Free text |

### Priority Calculation

```python
def calculate_priority_score(severity, impact, effort):
    """
    Priority Score = (Severity_Points + Impact_Points) × (Effort_Inverse) + Audit_Relevance
    
    Severity: Critical=10, High=7, Medium=4, Low=2
    Impact: High=8, Medium=5, Low=2
    Effort: High=3/10, Medium=5/10, Low=8/10 (inverse: lower effort = higher priority)
    Audit_Relevance: +8 for SHALL requirements, +3 for SHOULD, 0 for operational
    """
    
    severity_points = {'Critical': 10, 'High': 7, 'Medium': 4, 'Low': 2}
    impact_points = {'High': 8, 'Medium': 5, 'Low': 2}
    effort_inverse = {'High': 3, 'Medium': 5, 'Low': 8}
    
    score = (severity_points[severity] + impact_points[impact]) * (effort_inverse[effort] / 10)
    
    # Add audit relevance (heuristic: if severity is Critical or High, likely audit-relevant)
    if severity in ['Critical', 'High']:
        score += 8
    
    return score

# In Excel formula:
ws['G3'] = '''=
  (IF(D3="Critical",10,IF(D3="High",7,IF(D3="Medium",4,2))) +
   IF(E3="High",8,IF(E3="Medium",5,2))) *
  (IF(F3="High",0.3,IF(F3="Medium",0.5,0.8))) +
  IF(OR(D3="Critical",D3="High"),8,0)
'''
```

### Auto-Ranking

```python
# Sort Action Register by Priority Score (descending)
# Column A (Priority) is rank after sort
# This can be done manually via Excel sort, or programmatically
```

---

## Python Consolidation Script - Complete Template

```python
"""
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR YOUR ORGANIZATION

Compliance Dashboard Consolidation Script
ISO/IEC 27001:2022 Control A.5.9

This script consolidates 4 assessment CSVs into executive dashboard workbook.

IMPORTANT: This is a SAMPLE script. Customize for your organization:
1. CSV file paths (adjust to your directory structure)
2. Assessment weights (verify 25%/20%/35%/20% is correct for you)
3. Target scores (verify 95%/95%/97%/94% matches your policy)
4. Action prioritization logic (adjust severity/impact/effort scoring)

Author: ISMS Implementation Team
Date: [Date]
Version: 1.0
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, Protection
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from datetime import datetime
import csv
import os
import sys

# CUSTOMIZE: Configuration
CONFIG = {
    'input_dir': './csv-exports/',
    'output_dir': './dashboards/',
    'workbook_name': f'ISMS_A_5_9_Compliance_Dashboard_Q1_{datetime.now().year}.xlsx',
    
    # Assessment weights (must sum to 100%)
    'weights': {
        'Discovery': 25,
        'Maintenance': 20,
        'Quality': 35,
        'Accountability': 20
    },
    
    # Target scores
    'targets': {
        'Discovery': 95,
        'Maintenance': 95,
        'Quality': 97,
        'Accountability': 94,
        'Overall': 95
    },
    
    # CSV filenames (adjust YYYYMMDD to your generation dates)
    'csv_files': {
        'Discovery': 'A59_1_Discovery_Metrics_20260115.csv',
        'Maintenance': 'A59_2_Maintenance_Metrics_20260118.csv',
        'Quality': 'A59_3_Quality_Metrics_20260120.csv',
        'Accountability': 'A59_4_Accountability_Metrics_20260122.csv'
    },
    
    'sheets': [
        'Executive Summary',
        'Compliance Scorecard',
        'Discovery Metrics',
        'Maintenance Metrics',
        'Quality Metrics',
        'Accountability Metrics',
        'Trending Analysis',
        'Action Register'
    ]
}

def main():
    """Main execution function"""
    
    print("=" * 70)
    print("ISMS A.5.9 COMPLIANCE DASHBOARD CONSOLIDATION")
    print("=" * 70)
    print()
    
    # Step 1: Validate all CSV files exist
    print("[1/6] Validating CSV files...")
    csv_paths = validate_csv_files()
    if not csv_paths:
        print("❌ ERROR: Missing CSV files. Cannot proceed.")
        sys.exit(1)
    print("  ✓ All 4 CSV files found")
    print()
    
    # Step 2: Create workbook structure
    print("[2/6] Creating dashboard workbook...")
    wb = create_workbook_structure()
    print("  ✓ Workbook created with 8 sheets")
    print()
    
    # Step 3: Import CSV data into sheets 3-6
    print("[3/6] Importing assessment data...")
    import_assessment_data(wb, csv_paths)
    print("  ✓ All assessment data imported")
    print()
    
    # Step 4: Generate executive summary
    print("[4/6] Generating Executive Summary...")
    create_executive_summary(wb['Executive Summary'])
    print("  ✓ Executive Summary generated")
    print()
    
    # Step 5: Generate scorecard
    print("[5/6] Generating Compliance Scorecard...")
    create_compliance_scorecard(wb['Compliance Scorecard'])
    print("  ✓ Scorecard generated")
    print()
    
    # Step 6: Generate action register template
    print("[6/6] Creating Action Register template...")
    create_action_register(wb['Action Register'])
    print("  ✓ Action Register created")
    print()
    
    # Save workbook
    output_path = os.path.join(CONFIG['output_dir'], CONFIG['workbook_name'])
    os.makedirs(CONFIG['output_dir'], exist_ok=True)
    wb.save(output_path)
    
    print("=" * 70)
    print(f"✓ DASHBOARD GENERATED SUCCESSFULLY!")
    print(f"  Location: {output_path}")
    print(f"  Size: {os.path.getsize(output_path) / 1024:.1f} KB")
    print()
    print("NEXT STEPS:")
    print("  1. Review imported data in Sheets 3-6")
    print("  2. Complete Executive Narrative in Sheet 1")
    print("  3. Populate Action Register in Sheet 8")
    print("  4. Review with CISO and distribute")
    print("=" * 70)

def validate_csv_files():
    """Validate all required CSV files exist"""
    csv_paths = {}
    all_exist = True
    
    for assessment, filename in CONFIG['csv_files'].items():
        filepath = os.path.join(CONFIG['input_dir'], filename)
        if os.path.exists(filepath):
            csv_paths[assessment] = filepath
            print(f"  ✓ {assessment}: {filename}")
        else:
            print(f"  ❌ {assessment}: {filename} NOT FOUND")
            all_exist = False
    
    return csv_paths if all_exist else None

def create_workbook_structure():
    """Create workbook with all sheets"""
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    
    for sheet_name in CONFIG['sheets']:
        wb.create_sheet(title=sheet_name)
    
    # Set workbook properties
    wb.properties.title = "ISMS A.5.9 Compliance Dashboard"
    wb.properties.subject = "ISO/IEC 27001:2022 Control A.5.9"
    wb.properties.creator = "[Organization] ISMS Team"
    wb.properties.created = datetime.now()
    
    return wb

def import_assessment_data(wb, csv_paths):
    """Import CSV data into sheets 3-6"""
    
    sheet_mapping = {
        'Discovery': 'Discovery Metrics',
        'Maintenance': 'Maintenance Metrics',
        'Quality': 'Quality Metrics',
        'Accountability': 'Accountability Metrics'
    }
    
    for assessment, sheet_name in sheet_mapping.items():
        ws = wb[sheet_name]
        csv_path = csv_paths[assessment]
        
        with open(csv_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            for row_num, row_data in enumerate(reader, start=1):
                for col_num, cell_value in enumerate(row_data, start=1):
                    cell = ws.cell(row=row_num, column=col_num)
                    
                    # Try numeric conversion
                    try:
                        if cell_value.endswith('%'):
                            cell.value = float(cell_value.rstrip('%')) / 100
                            cell.number_format = '0.0"%"'
                        else:
                            cell.value = float(cell_value)
                    except (ValueError, AttributeError):
                        cell.value = cell_value
                    
                    # Header formatting
                    if row_num == 1:
                        cell.font = Font(bold=True, color='FFFFFF')
                        cell.fill = PatternFill(start_color='003366', fill_type='solid')
                        cell.alignment = Alignment(horizontal='center')
        
        # Protect sheet
        ws.protection.sheet = True
        print(f"  ✓ Imported {assessment} metrics")

def create_executive_summary(ws):
    """Generate Executive Summary sheet"""
    # Implementation as per specification above
    # (create_header_section, create_assessment_breakdown, etc.)
    pass

def create_compliance_scorecard(ws):
    """Generate Compliance Scorecard sheet"""
    # Implementation as per specification
    pass

def create_action_register(ws):
    """Create Action Register template"""
    # Implementation as per specification
    pass

if __name__ == '__main__':
    main()
```

---

## Integration Testing

### Test Procedure

1. **Generate Test CSVs** from sample assessment workbooks
2. **Run consolidation script**
3. **Verify imported data** matches source CSVs
4. **Check formulas** calculate correctly
5. **Test conditional formatting** (traffic lights work)
6. **Manual review** executive summary for completeness

### Expected Outputs

- Dashboard workbook generated without errors
- All 4 CSV files imported successfully
- Overall compliance score calculated correctly
- Traffic light indicators display properly
- Action register populated with sample data

---

**END OF SPECIFICATION**

---

*"The optimist thinks this is the best of all possible worlds. The pessimist fears it is true."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->
