**ISMS-IMP-A.5.34.7-TG - Privacy Compliance Dashboard (Consolidation)**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.34.7-TG |
| **Version** | 1.0 |
| **Assessment Area** | Privacy Compliance Dashboard - Consolidated Privacy Program Oversight |
| **Related Policy** | ISMS-POL-A.5.34, Section 2.7 (Privacy Program Oversight and Accountability) |
| **Purpose** | Guide users through consolidation of all privacy assessments (A.5.34.1-6) into executive dashboard for GDPR Article 24 accountability and ISO 27001 compliance demonstration |
| **Target Audience** | DPO/Privacy Officers, CISO, Legal Counsel, Privacy Committee, Board of Directors, Executive Leadership, Auditors |
| **Assessment Type** | Consolidation & Executive Reporting |
| **Review Cycle** | Quarterly (synchronized with privacy assessment cycles) |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Privacy Compliance Dashboard | ISMS Implementation Team |

---

## Purpose and Scope

### Purpose

This implementation guide provides comprehensive procedures for consolidating privacy assessment data from all six A.5.34 domain assessments into a unified Privacy Compliance Dashboard for executive oversight, audit readiness, and continuous privacy program monitoring.

### Consolidation Objectives

1. **Unified Metrics**: Aggregate privacy compliance metrics across all 7 domains
2. **Executive Visibility**: Provide C-level dashboard for privacy program oversight
3. **Audit Readiness**: Centralize evidence and compliance status for ISO 27001/GDPR audits
4. **Gap Prioritization**: Consolidate gaps from all domains for risk-based remediation
5. **Trend Analysis**: Track privacy compliance improvements over time
6. **Regulatory Reporting**: Support GDPR Article 24 accountability obligations

### Scope

**In Scope:**

- Consolidation of 6 privacy assessment workbooks (A.5.34.1 through A.5.34.6)
- Master dashboard with domain-by-domain compliance scores
- Aggregated gap analysis across all privacy domains
- Risk heat map for privacy program
- Evidence completeness tracking
- Executive summary for Privacy Committee/Board
- Quarterly trend tracking

**Out of Scope:**

- Individual domain re-assessment (handled in respective A.5.34.1-6 assessments)
- Detailed gap remediation tracking (managed in individual domain workbooks)
- Real-time monitoring (dashboard updated quarterly or on-demand)
- Integration with GRC platforms (future enhancement)

### Architecture Overview

**Three-Layer Assessment Architecture:**

**Layer 1: Domain Assessments (A.5.34.1 through A.5.34.6)**

- Individual Excel workbooks with local dashboards
- Excel formula-based calculations within each workbook
- Manual completion by business owners, DPO, Legal

**Layer 2: BIG DASHBOARD (A.5.34.7) - THIS LAYER**

- Python script reads all 6 workbooks using `openpyxl` library
- Extracts metrics from each domain's dashboard sheet
- Generates consolidated master dashboard workbook
- Creates executive summary and trend charts

**Layer 3: Optional Consolidation Scripts**

- Risk registry consolidation (merges gaps from all domains)
- Evidence repository consolidation
- Normalization scripts for data quality

---

# Technical Specification

---

## Consolidation Architecture

### Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│  SOURCE WORKBOOKS (6 Domain Assessments - Layer 1)        │
├─────────────────────────────────────────────────────────────┤
│  A.5.34.1: PII Identification (Dashboard sheet)           │
│  A.5.34.2: Legal Basis (Dashboard sheet)                  │
│  A.5.34.3: DSR Management (Dashboard sheet)               │
│  A.5.34.4: TOMs (Dashboard sheet)                         │
│  A.5.34.5: DPIA (Dashboard sheet)                         │
│  A.5.34.6: Cross-Border Transfer (Dashboard sheet)        │
└────────────────┬────────────────────────────────────────────┘
                 │
                 │ Python Script: generate_a5347_compliance_dashboard.py
                 │ - Opens each workbook with openpyxl
                 │ - Extracts metrics from dashboard sheets
                 │ - Reads gap analysis sheets
                 │ - Aggregates evidence counts
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  OUTPUT WORKBOOK (Master Dashboard - Layer 2)             │
├─────────────────────────────────────────────────────────────┤
│  Sheet 1: Executive Dashboard (metrics, charts)            │
│  Sheet 2: Consolidated Gap Registry (all domains)          │
│  Sheet 3: Risk Heat Map (visual matrix)                    │
│  Sheet 4: Evidence Completeness (by domain)                │
│  Sheet 5: Executive Summary (2-page report)                │
│  Sheet 6: Quarterly Trends (historical comparison)         │
└─────────────────────────────────────────────────────────────┘
```

### Python Data Extraction Pattern

```python
from openpyxl import load_workbook

# Open source workbook (read-only, formulas evaluated)
wb = load_workbook('ISMS_A_5_34_1_PII_Identification_Assessment_20250130.xlsx',
                   data_only=True, read_only=True)

# Navigate to dashboard sheet
ws = wb['Dashboard']  # or 'Summary' or 'Compliance Dashboard' - varies by domain

# Extract metrics (cell references must match domain workbook structure)
total_systems = ws['B6'].value         # Total PII systems
ropa_entries = ws['B8'].value          # ROPA entries
compliance_score = ws['B14'].value     # Overall compliance %
critical_gaps = ws['B26'].value        # Critical gaps count
high_gaps = ws['B27'].value            # High gaps count

# Close workbook
wb.close()

# Store in dictionary for master dashboard
domain_data['A.5.34.1'] = {
    'total_systems': total_systems,
    'ropa_entries': ropa_entries,
    'compliance_score': compliance_score,
    'critical_gaps': critical_gaps,
    'high_gaps': high_gaps,
}
```

**Key Principle:** Master dashboard contains **NO user input fields** - all data is extracted programmatically from source workbooks.

---

## Sheet 1: Executive Dashboard

### Purpose
Provide C-level overview of privacy program health with key metrics, domain scorecard, and visualizations.

### Structure

**Section 1: Title Block (A1:L3)**

- Merge cells A1:L3
- Title: "Privacy Compliance Dashboard - Executive Overview"
- Subtitle: "ISO/IEC 27001:2022 Control A.5.34 - Privacy and Protection of PII"
- Quarter: "Q1 2025" (auto-populated from consolidation date)
- Font: Arial 18pt Bold, White text
- Background: Dark Blue (#1F4E78)

**Section 2: Overall Metrics (A5:L15)**

| Row | Metric Label (Column A) | Value (Column B) | Target (Column C) | Status (Column D) | Data Source |
|-----|------------------------|------------------|-------------------|-------------------|-------------|
| 6 | **Overall Privacy Compliance Score** | 85% | ≥80% | 🟢 Good | Weighted average of 6 domain scores |
| 7 | **Domains at Target (≥80%)** | 5/6 | 6/6 | 🟡 | Count domains where score ≥80% |
| 8 | **Critical Gaps (All Domains)** | 0 | 0 | 🟢 | Sum of critical gaps from all 6 domains |
| 9 | **High Gaps (All Domains)** | 6 | <5 | 🟡 | Sum of high gaps from all 6 domains |
| 10 | **Medium Gaps (All Domains)** | 12 | <15 | 🟢 | Sum of medium gaps |
| 11 | **Average Gap Age (Days)** | 42 | <60 | 🟢 | Weighted average across domains |
| 12 | **Evidence Completeness** | 90% | 100% | 🟡 | % of required evidence collected |
| 13 | **DPO Approval Rate** | 100% | 100% | 🟢 | % of domains with DPO sign-off |
| 14 | **Last Updated** | 2025-01-30 | - | - | Consolidation run date |

**Cell Formulas (Python-generated, NOT Excel formulas):**

```python
# Overall Compliance Score (weighted average)
weights = {'A.5.34.1': 0.20, 'A.5.34.2': 0.20, 'A.5.34.3': 0.15,
           'A.5.34.4': 0.20, 'A.5.34.5': 0.10, 'A.5.34.6': 0.15}

overall_score = sum(domain_data[domain]['compliance_score'] * weights[domain]
                    for domain in domain_data.keys())

# Write to cell B6
ws['B6'] = overall_score
ws['B6'].number_format = '0%'

# Conditional formatting for status
if overall_score >= 0.90:
    ws['D6'] = '🟢 Excellent'
    ws['D6'].fill = PatternFill(start_color='FFC6EFCE', fill_type='solid')
elif overall_score >= 0.80:
    ws['D6'] = '🟢 Good'
    ws['D6'].fill = PatternFill(start_color='FFC6EFCE', fill_type='solid')
elif overall_score >= 0.60:
    ws['D6'] = '🟡 Needs Improvement'
    ws['D6'].fill = PatternFill(start_color='FFFFEB9C', fill_type='solid')
else:
    ws['D6'] = '🔴 Critical'
    ws['D6'].fill = PatternFill(start_color='FFFFC7CE', fill_type='solid')
```

**Section 3: Domain Scorecard (A17:L30)**

**Headers (Row 17):**
| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| Domain | Compliance Score | Status | Critical Gaps | High Gaps | Med Gaps | Last Updated | Trend (vs Q4) |

**Data Rows (18-23):**

| Domain | Score | Status | Critical | High | Medium | Last Updated | Trend |
|--------|-------|--------|----------|------|--------|--------------|-------|
| A.5.34.1 - PII Identification | 85% | 🟢 Good | 0 | 2 | 3 | 2025-01-30 | ↗ +5% |
| A.5.34.2 - Legal Basis | 92% | 🟢 Excellent | 0 | 0 | 1 | 2025-01-30 | ↗ +8% |
| A.5.34.3 - DSR Management | 78% | 🟡 Needs Improvement | 0 | 3 | 4 | 2025-01-30 | → 0% |
| A.5.34.4 - TOMs | 88% | 🟢 Good | 0 | 1 | 2 | 2025-01-30 | ↗ +12% |
| A.5.34.5 - DPIA | 75% | 🟡 Needs Improvement | 0 | 0 | 2 | 2025-01-30 | ↘ -3% |
| A.5.34.6 - Cross-Border Transfer | 82% | 🟢 Good | 0 | 0 | 0 | 2025-01-30 | ↗ +15% |

**Python Population:**

```python
domain_names = {
    'A.5.34.1': 'PII Identification',
    'A.5.34.2': 'Legal Basis',
    'A.5.34.3': 'DSR Management',
    'A.5.34.4': 'TOMs',
    'A.5.34.5': 'DPIA',
    'A.5.34.6': 'Cross-Border Transfer',
}

row = 18
for domain_id, domain_name in domain_names.items():
    ws[f'A{row}'] = f"{domain_id} - {domain_name}"
    ws[f'B{row}'] = domain_data[domain_id]['compliance_score']
    ws[f'B{row}'].number_format = '0%'
    
    # Status with color coding
    score = domain_data[domain_id]['compliance_score']
    if score >= 0.80:
        ws[f'C{row}'] = '🟢 Good' if score < 0.90 else '🟢 Excellent'
        ws[f'C{row}'].fill = PatternFill(start_color='FFC6EFCE', fill_type='solid')
    else:
        ws[f'C{row}'] = '🟡 Needs Improvement'
        ws[f'C{row}'].fill = PatternFill(start_color='FFFFEB9C', fill_type='solid')
    
    ws[f'D{row}'] = domain_data[domain_id]['critical_gaps']
    ws[f'E{row}'] = domain_data[domain_id]['high_gaps']
    ws[f'F{row}'] = domain_data[domain_id]['medium_gaps']
    ws[f'G{row}'] = domain_data[domain_id]['last_updated']
    
    # Trend calculation (requires previous quarter data)
    trend = domain_data[domain_id].get('trend_vs_prev_quarter', 0)
    if trend > 0:
        ws[f'H{row}'] = f"↗ +{trend}%"
        ws[f'H{row}'].font = Font(color='FF006100')  # Dark green
    elif trend < 0:
        ws[f'H{row}'] = f"↘ {trend}%"
        ws[f'H{row}'].font = Font(color='FF9C0006')  # Dark red
    else:
        ws[f'H{row}'] = "→ 0%"
        ws[f'H{row}'].font = Font(color='FF7F7F7F')  # Gray
    
    row += 1
```

**Section 4: Charts (A32:L60)**

**Chart 1: Overall Compliance Score (Gauge Chart Simulation)**

- Location: A32:F45
- Type: Pie chart with single slice showing percentage filled
- Data: Overall score (85%) vs. remaining to 100% (15%)
- Colors: Green slice (85%), Gray slice (15%)
- Center Label: "85%"

**Chart 2: Domain Compliance Scores (Bar Chart)**

- Location: A47:F60
- Type: Horizontal bar chart
- X-axis: Compliance Score (0-100%)
- Y-axis: 6 Domains
- Bars: Color-coded (Green ≥80%, Yellow 60-79%, Red <60%)
- Target Line: 80% threshold

**Chart 3: Gap Distribution (Stacked Bar Chart)**

- Location: H32:L45
- Type: Stacked horizontal bar chart
- Y-axis: 6 Domains
- X-axis: Count
- Stack segments: Critical (Red), High (Orange), Medium (Yellow), Low (Green)

**Chart 4: Quarterly Trend (Line Chart)**

- Location: H47:L60
- Type: Line chart
- X-axis: Quarters (Q1 2024, Q2 2024, Q3 2024, Q4 2024, Q1 2025)
- Y-axis: Overall Compliance Score (0-100%)
- Line: Overall score over time
- Target Line: 80% threshold

---

## Sheet 2: Consolidated Gap Registry

### Purpose
Aggregate all gaps from 6 domain assessments for centralized remediation tracking.

### Data Extraction Logic

```python
# For each domain workbook
for domain_id, workbook_path in domain_workbooks.items():
    wb = load_workbook(workbook_path, data_only=True, read_only=True)
    
    # Navigate to Gap Analysis sheet (sheet name varies by domain)
    gap_sheet_names = ['Gap Analysis', 'Gaps', 'Remediation Plan']
    ws_gap = None
    for sheet_name in gap_sheet_names:
        if sheet_name in wb.sheetnames:
            ws_gap = wb[sheet_name]
            break
    
    if not ws_gap:
        continue  # Skip if no gap sheet found
    
    # Extract gaps (assuming headers in row 1, data starts row 2)
    for row_num in range(2, ws_gap.max_row + 1):
        gap_id = ws_gap[f'A{row_num}'].value
        if not gap_id:
            break  # Stop at first empty row
        
        gap = {
            'source_domain': domain_id,
            'gap_id': f"{domain_id}-{gap_id}",  # Prefix with domain
            'gap_type': ws_gap[f'C{row_num}'].value,
            'description': ws_gap[f'D{row_num}'].value,
            'risk_level': ws_gap[f'G{row_num}'].value,
            'affected_systems': ws_gap[f'E{row_num}'].value,
            'affected_data_subjects': ws_gap[f'F{row_num}'].value,
            'discovery_date': ws_gap[f'M{row_num}'].value,
            'remediation_action': ws_gap[f'N{row_num}'].value,
            'owner': ws_gap[f'O{row_num}'].value,
            'target_date': ws_gap[f'Q{row_num}'].value,
            'status': ws_gap[f'S{row_num}'].value,
        }
        
        consolidated_gaps.append(gap)
    
    wb.close()

# Sort consolidated gaps by priority
consolidated_gaps.sort(key=lambda x: (
    {'Critical': 0, 'High': 1, 'Medium': 2, 'Low': 3}.get(x['risk_level'], 4),
    (datetime.now() - x['target_date']).days if x['target_date'] else 0  # Days overdue
), reverse=False)
```

### Column Definitions

| Col | Column Name | Data Type | Width | Source | Notes |
|-----|------------|-----------|-------|--------|-------|
| A | Gap ID | Text | 15 | `domain-original_gap_id` | E.g., "A.5.34.1-GAP-0003" |
| B | Source Domain | Text | 12 | Domain ID | A.5.34.1, A.5.34.2, etc. |
| C | Gap Type | Text | 25 | From domain Gap Analysis sheet | E.g., "Missing Legal Basis" |
| D | Description | Text | 50 | From domain | Full gap description |
| E | Risk Level | Text | 12 | Critical/High/Medium/Low | As assessed in domain |
| F | Affected Systems | Text | 30 | From domain | System names |
| G | Affected Data Subjects | Text | 25 | From domain | Count or description |
| H | Discovery Date | Date | 12 | From domain | When identified |
| I | Remediation Action | Text | 50 | From domain | What needs to be done |
| J | Owner | Text | 20 | From domain | Responsible person/team |
| K | Target Date | Date | 12 | From domain | Deadline |
| L | Actual Completion Date | Date | 12 | From domain | When completed (if applicable) |
| M | Status | Text | 15 | From domain | Open/In Progress/Completed/Blocked |
| N | Days Overdue | Formula | 12 | Calculated | `=IF(TODAY()>K2, TODAY()-K2, 0)` |
| O | Priority | Formula | 12 | Calculated | Risk + Overdue ranking |

### Conditional Formatting

**Rule 1: Critical Gaps**
```
Applies to: E2:E1000
Condition: ="Critical"
Format: Red fill (#FFC7CE), Red text, Bold
```

**Rule 2: High Gaps**
```
Applies to: E2:E1000
Condition: ="High"
Format: Orange fill (#FFD966), Dark Orange text
```

**Rule 3: Overdue Gaps**
```
Applies to: N2:N1000
Condition: >0
Format: Red text, Bold
```

**Rule 4: Status Color-Coding**
```
Applies to: M2:M1000
Condition: ="Completed" → Light Green
Condition: ="In Progress" → Light Yellow
Condition: ="Open" → Light Red
Condition: ="Blocked" → Gray
```

### Sorting and Filtering

**Default Sort:**
1. Risk Level (Critical → High → Medium → Low)
2. Days Overdue (descending)
3. Affected Data Subjects (descending)

**AutoFilter:** Enabled on row 1 for all columns

---

## Sheet 3: Risk Heat Map

### Purpose
Visualize privacy risks across domains and risk categories.

### Structure

**Heat Map Matrix (A1:H10)**

**Rows:** Privacy Domains (A.5.34.1 through A.5.34.6)  
**Columns:** Risk Categories

| | A | B | C | D | E | F | G | H |
|-|---|---|---|---|---|---|---|---|
| 1 | **Domain** | **Data Governance** | **Legal Compliance** | **Security Controls** | **Cross-Border** | **Subject Rights** | **High-Risk Processing** | **Overall Risk** |
| 2 | A.5.34.1 | 🟢 Low | 🟢 Low | 🟡 Medium | 🟢 Low | N/A | N/A | 🟢 Low |
| 3 | A.5.34.2 | 🟢 Low | 🟢 Low | N/A | N/A | N/A | N/A | 🟢 Low |
| 4 | A.5.34.3 | N/A | 🟡 Medium | 🟢 Low | N/A | 🟡 Medium | N/A | 🟡 Medium |
| 5 | A.5.34.4 | 🟢 Low | 🟢 Low | 🟡 Medium | N/A | N/A | N/A | 🟢 Low |
| 6 | A.5.34.5 | 🟡 Medium | 🟡 Medium | 🟢 Low | 🟡 Medium | N/A | 🟡 Medium | 🟡 Medium |
| 7 | A.5.34.6 | 🟢 Low | 🟡 Medium | 🟢 Low | 🟡 Medium | N/A | N/A | 🟡 Medium |
| 8 | | | | | | | | |
| 9 | **Overall** | 🟢 Low | 🟡 Medium | 🟡 Medium | 🟡 Medium | 🟡 Medium | 🟡 Medium | 🟡 Medium |

### Risk Calculation Logic

```python
def calculate_risk_level(domain_id, category):
    """
    Calculate risk level for domain + category combination.
    
    Risk Levels:

    - Critical: Any Critical gap in this category
    - High: 3+ High gaps in this category
    - Medium: 1-2 High gaps OR 5+ Medium gaps
    - Low: <5 Medium gaps, no High/Critical gaps

    """
    # Filter gaps for this domain + category
    category_gaps = [g for g in consolidated_gaps 
                     if g['source_domain'] == domain_id 
                     and g['category'] == category]
    
    critical_count = sum(1 for g in category_gaps if g['risk_level'] == 'Critical')
    high_count = sum(1 for g in category_gaps if g['risk_level'] == 'High')
    medium_count = sum(1 for g in category_gaps if g['risk_level'] == 'Medium')
    
    if critical_count > 0:
        return '🔴 Critical', 'FFFF0000'  # Red
    elif high_count >= 3:
        return '🔴 High', 'FFFFA500'  # Orange
    elif high_count >= 1 or medium_count >= 5:
        return '🟡 Medium', 'FFFFFF00'  # Yellow
    else:
        return '🟢 Low', 'FF00FF00'  # Green

# Populate heat map
for row_num, domain_id in enumerate(domain_names.keys(), start=2):
    ws[f'A{row_num}'] = domain_id
    
    categories = {
        'B': 'Data Governance',
        'C': 'Legal Compliance',
        'D': 'Security Controls',
        'E': 'Cross-Border',
        'F': 'Subject Rights',
        'G': 'High-Risk Processing',
    }
    
    for col, category in categories.items():
        risk_text, risk_color = calculate_risk_level(domain_id, category)
        cell = ws[f'{col}{row_num}']
        cell.value = risk_text
        cell.fill = PatternFill(start_color=risk_color, fill_type='solid')
        cell.alignment = Alignment(horizontal='center', vertical='center')
```

### Visualization

**Heat Map Color Gradient:**

- 🔴 Critical/High: Dark Red → Orange
- 🟡 Medium: Yellow
- 🟢 Low: Light Green

**Overall Risk Row (Row 9):**

- Aggregate risk across all domains per category
- Calculated as highest risk level across all domains for that category

---

**END OF PART II: Technical Specifications (Sheets 1-3)**

## PART III: Technical Specifications (Sheets 4-6) + Python Implementation

---

## Sheet 4: Evidence Completeness

### Purpose
Track audit evidence collection status across all privacy domains for ISO 27001/GDPR audit readiness.

### Data Extraction Logic

```python
def extract_evidence_metrics(domain_id, workbook_path):
    """Extract evidence metrics from domain workbook."""
    wb = load_workbook(workbook_path, data_only=True, read_only=True)
    
    # Find Evidence Repository sheet
    evidence_sheet_names = ['Evidence Repository', 'Evidence', 'Evidence Register']
    ws_evidence = None
    for sheet_name in evidence_sheet_names:
        if sheet_name in wb.sheetnames:
            ws_evidence = wb[sheet_name]
            break
    
    if not ws_evidence:
        return {'collected': 0, 'required': 0, 'completeness': 0}
    
    # Count evidence items (rows 2 onwards, stop at first empty)
    evidence_collected = 0
    evidence_required = 0
    
    for row_num in range(2, ws_evidence.max_row + 1):
        evidence_id = ws_evidence[f'A{row_num}'].value
        if not evidence_id:
            break
        
        evidence_required += 1
        
        # Check if evidence is current (not expired or missing)
        status = ws_evidence[f'M{row_num}'].value  # Assuming column M = Status
        if status and status.lower() in ['current', 'valid', 'active']:
            evidence_collected += 1
    
    completeness = (evidence_collected / evidence_required * 100) if evidence_required > 0 else 0
    
    wb.close()
    
    return {
        'collected': evidence_collected,
        'required': evidence_required,
        'completeness': completeness,
    }
```

### Column Definitions

| Col | Column Name | Data Type | Width | Source | Notes |
|-----|------------|-----------|-------|--------|-------|
| A | Domain | Text | 25 | Domain name | E.g., "A.5.34.1 - PII Identification" |
| B | Required Evidence Types | Text | 50 | Domain-specific | List of evidence categories |
| C | Evidence Collected | Number | 12 | Count from Evidence sheet | # of current evidence items |
| D | Evidence Required | Number | 12 | Count from Evidence sheet | Total evidence items |
| E | Completeness % | Percentage | 12 | Calculated | `=C/D` |
| F | Missing Evidence Items | Number | 12 | Calculated | `=D-C` |
| G | Evidence Status | Text | 15 | Conditional | Good/Partial/Poor based on % |
| H | Last Evidence Update | Date | 15 | Latest evidence date | From Evidence sheet max(Upload Date) |
| I | Next Evidence Review | Date | 15 | Calculated | Last Update + 90 days |

### Example Data

| Domain | Required Types | Collected | Required | % | Missing | Status | Last Update | Next Review |
|--------|---------------|-----------|----------|---|---------|--------|-------------|-------------|
| A.5.34.1 | ROPA, data flows, classifications | 45 | 50 | 90% | 5 | 🟢 Good | 2025-01-25 | 2025-04-25 |
| A.5.34.2 | Legal assessments, consents, LIAs | 82 | 90 | 91% | 8 | 🟢 Good | 2025-01-28 | 2025-04-28 |
| A.5.34.3 | DSR logs, verifications, responses | 120 | 125 | 96% | 5 | 🟢 Good | 2025-01-30 | 2025-04-30 |
| A.5.34.4 | TOMs docs, configs, audits, tests | 38 | 45 | 84% | 7 | 🟢 Good | 2025-01-28 | 2025-04-28 |
| A.5.34.5 | DPIAs, DPO consults, SA consults | 12 | 15 | 80% | 3 | 🟢 Good | 2025-01-29 | 2025-04-29 |
| A.5.34.6 | SCCs, TIAs, DPAs, DPF certs | 28 | 35 | 80% | 7 | 🟢 Good | 2025-01-30 | 2025-04-30 |
| **TOTAL** | | **325** | **360** | **90%** | **35** | 🟢 | | |

### Conditional Formatting

**Rule 1: Evidence Completeness Percentage**
```
Applies to: E2:E10
Condition: >=95% → Dark Green fill, White text
Condition: >=80% → Light Green fill
Condition: >=60% → Light Yellow fill
Condition: <60% → Light Red fill
```

**Rule 2: Missing Evidence Count**
```
Applies to: F2:F10
Condition: >10 → Orange fill, Dark Orange text (many items missing)
Condition: >0 → Light Yellow fill
Condition: =0 → Light Green fill
```

**Rule 3: Evidence Status**
```
G2:G10 populated based on % in column E:

- ≥95%: "🟢 Excellent"
- ≥80%: "🟢 Good"
- ≥60%: "🟡 Partial"
- <60%: "🔴 Poor"

```

### Charts

**Chart 1: Evidence Completeness by Domain (Bar Chart)**

- Location: J2:O15
- Type: Horizontal bar chart
- X-axis: Completeness % (0-100%)
- Y-axis: 6 Domains
- Bars: Color-coded (Green ≥80%, Yellow 60-79%, Red <60%)
- Target Line: 80% threshold

**Chart 2: Missing Evidence Breakdown (Pie Chart)**

- Location: J17:O30
- Type: Pie chart
- Slices: 6 domains showing proportion of missing evidence
- Labels: Domain name + count (e.g., "A.5.34.1 - 5 items")

---

## Sheet 5: Executive Summary

### Purpose
Generate 2-page executive report for Privacy Committee/Board presentation.

### Structure

**PAGE 1: Privacy Program Health (Rows 1-50)**

**Section 1: Header (A1:L5)**
```
Organization: [Company Name]
Report: Privacy Compliance Executive Summary
Period: Q1 2025 (January 1 - March 31, 2025)
Prepared By: Data Protection Officer
Date: January 30, 2025
```

**Section 2: Executive Summary (A7:L20)**
```
OVERALL STATUS: 🟢 GOOD (85% Compliance)

The privacy program demonstrates strong compliance with ISO/IEC 27001:2022 
Control A.5.34 and GDPR requirements. Significant improvements achieved in 
Q1 2025 with elimination of all Critical gaps and substantial reduction in 
High-priority gaps.

KEY HIGHLIGHTS:
✅ Overall privacy compliance score: 85% (target: ≥80%)
✅ Zero Critical gaps (down from 3 in Q4 2024)
✅ Legal basis coverage at 92% (GDPR Art. 6 compliance excellent)
✅ DSR SLA compliance at 95% (meeting 30-day GDPR requirement)
✅ Cross-border transfer compliance improved 15% quarter-over-quarter

AREAS REQUIRING ATTENTION:
⚠️ DPIA completion at 75% (below 80% target) - 3 DPIAs pending for new systems
⚠️ Cross-border TIAs needed for 7 US processors (Schrems II requirement)
⚠️ DSR request backlog increasing (15 pending vs. 8 last quarter)
```

**Section 3: Domain Performance Table (A22:L35)**

| Domain | Score | Status | Change vs Q4 | Key Achievement | Key Gap |
|--------|-------|--------|--------------|-----------------|---------|
| PII Identification | 85% | 🟢 | +5% | ROPA updated for 12 new systems | 5 data flow diagrams pending |
| Legal Basis | 92% | 🟢 | +8% | 100% processing activities have legal basis | 8 LIAs need annual refresh |
| DSR Management | 78% | 🟡 | 0% | 95% SLA compliance maintained | Backlog growing, need +1 FTE |
| TOMs | 88% | 🟢 | +12% | Backup encryption deployed | 1 legacy system TOM upgrade |
| DPIA | 75% | 🟡 | -3% | 12 DPIAs completed | 3 new profiling systems need DPIA |
| Cross-Border | 82% | 🟢 | +15% | All SCCs updated to 2021 version | 7 TIAs required for US processors |

**PAGE 2: Remediation Plan & Resources (Rows 36-80)**

**Section 4: Top 5 Priority Gaps (A37:L50)**

| Priority | Gap | Risk | Deadline | Owner | Status | Impact if Unresolved |
|----------|-----|------|----------|-------|--------|---------------------|
| 1 | Missing TIAs for 7 US processors | High | Mar 31 | Legal | In Progress | Unlawful transfers (GDPR Chapter V) |
| 2 | 3 DPIAs pending for profiling | High | Feb 28 | DPO | Open | GDPR Art. 35 violation |
| 3 | DSR backlog (15 requests) | Medium | Feb 15 | Privacy Team | In Progress | Art. 12(3) SLA breach risk |
| 4 | 8 LIA annual refreshes overdue | Medium | Mar 15 | Legal | Open | Legitimate interest basis validity |
| 5 | Legacy system TOM upgrade | Medium | Apr 30 | IT Security | Planning | GDPR Art. 32 security gap |

**Section 5: Q2 2025 Remediation Plan (A52:L65)**

```
QUARTER 2 PRIORITIES:

1. Complete Outstanding DPIAs (Owner: DPO, Deadline: Feb 28)

   - DPIA for customer profiling system (10,000 users)
   - DPIA for employee monitoring tool (500 employees)
   - DPIA for automated decision-making (credit scoring)

   Action: DPO conducting DPIAs with business owners this month

2. Execute Schrems II TIAs for US Processors (Owner: Legal, Deadline: Mar 31)

   - 7 TIAs required for processors without EU-US DPF certification
   - External legal counsel engaged for complex TIAs (FISA 702 risk assessment)

   Budget: €15,000 for legal counsel
   Action: TIA template developed, processors prioritized by data sensitivity

3. Reduce DSR Request Backlog (Owner: Privacy Team, Deadline: Feb 15)

   - Current backlog: 15 requests (target: <5)
   - Root cause: Increased DSR volume (20% Q-over-Q growth) + resource constraints

   Resource Request: +1 FTE Privacy Analyst (€70,000 annual cost)
   Action: Hiring requisition submitted to HR, interim contractor engaged
```

**Section 6: Resource Requirements (A67:L75)**

```
BUDGET REQUEST FOR Q2 2025:

• External legal counsel (TIAs): €15,000
• Privacy Analyst headcount: €70,000 annually (€17,500 for Q2)
• DPIA training for business owners: €5,000
• Privacy program tooling (DPIA/TIA software): €10,000
TOTAL Q2 REQUEST: €47,500

ROI JUSTIFICATION:

- Avoided GDPR penalties (estimated €2M+ exposure from Critical gaps)
- Audit readiness (prevent ISO 27001 certification findings)
- Business enablement (faster product launches with streamlined DPIA process)

```

**Section 7: Next Steps (A77:L80)**

```
GOVERNANCE & OVERSIGHT:

✓ Privacy Committee Review: February 15, 2025
✓ Board Update: March 1, 2025 (included in CISO quarterly report)
✓ Next Consolidation: April 30, 2025 (Q2 2025 assessment)
✓ External Privacy Audit: October 2025 (pre-ISO 27001 recertification)
```

### Python Generation Logic

```python
def generate_executive_summary(ws, domain_data, gaps, evidence):
    """
    Generate executive summary sheet with dynamic content.
    
    Inputs:

    - domain_data: Dict with all domain metrics
    - gaps: List of all gaps from consolidated registry
    - evidence: Dict with evidence metrics
    
    Outputs:

    - Populated Sheet 5 with formatted executive summary

    """
    
    # Header
    ws['A1'] = "Organization:"
    ws['B1'] = "[Company Name]"  # User fills in
    ws['A2'] = "Report:"
    ws['B2'] = "Privacy Compliance Executive Summary"
    ws['A3'] = "Period:"
    ws['B3'] = f"Q1 2025 ({datetime.now().strftime('%B %d, %Y')})"
    ws['A4'] = "Prepared By:"
    ws['B4'] = "Data Protection Officer"
    ws['A5'] = "Date:"
    ws['B5'] = datetime.now().strftime('%Y-%m-%d')
    
    # Format header
    for row in range(1, 6):
        ws[f'A{row}'].font = Font(bold=True)
    
    # Overall Status
    overall_score = calculate_overall_score(domain_data)
    
    row = 7
    ws[f'A{row}'] = "OVERALL STATUS:"
    if overall_score >= 0.80:
        ws[f'B{row}'] = f"🟢 GOOD ({overall_score:.0%} Compliance)"
        ws[f'B{row}'].fill = PatternFill(start_color='FFC6EFCE', fill_type='solid')
    else:
        ws[f'B{row}'] = f"🟡 NEEDS IMPROVEMENT ({overall_score:.0%} Compliance)"
        ws[f'B{row}'].fill = PatternFill(start_color='FFFFEB9C', fill_type='solid')
    
    ws[f'A{row}'].font = Font(size=14, bold=True)
    ws[f'B{row}'].font = Font(size=14, bold=True)
    
    # Key Highlights (auto-generate based on data)
    row = 10
    ws[f'A{row}'] = "KEY HIGHLIGHTS:"
    ws[f'A{row}'].font = Font(bold=True)
    row += 1
    
    critical_gaps = sum(1 for g in gaps if g['risk_level'] == 'Critical')
    high_gaps = sum(1 for g in gaps if g['risk_level'] == 'High')
    
    highlights = [
        f"✅ Overall privacy compliance score: {overall_score:.0%} (target: ≥80%)",
        f"✅ Zero Critical gaps" if critical_gaps == 0 else f"⚠️ {critical_gaps} Critical gaps require immediate action",
        f"✅ High gaps reduced to {high_gaps}" if high_gaps < 5 else f"⚠️ {high_gaps} High gaps need remediation",
    ]
    
    for highlight in highlights:
        ws[f'A{row}'] = highlight
        ws[f'A{row}'].alignment = Alignment(wrap_text=True)
        row += 1
    
    # Domain Performance Table
    row += 2
    ws[f'A{row}'] = "DOMAIN PERFORMANCE:"
    ws[f'A{row}'].font = Font(bold=True)
    row += 1
    
    # Headers
    headers = ['Domain', 'Score', 'Status', 'Change vs Q4', 'Key Gap']
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=row, column=col_num)
        cell.value = header
        cell.font = Font(bold=True)
        cell.fill = PatternFill(start_color='FF1F4E78', fill_type='solid')
        cell.font = Font(bold=True, color='FFFFFFFF')
    
    row += 1
    
    # Domain data rows
    for domain_id, data in domain_data.items():
        ws[f'A{row}'] = domain_names[domain_id]
        ws[f'B{row}'] = data['compliance_score']
        ws[f'B{row}'].number_format = '0%'
        
        if data['compliance_score'] >= 0.80:
            ws[f'C{row}'] = '🟢 Good'
        else:
            ws[f'C{row}'] = '🟡 Needs Improvement'
        
        ws[f'D{row}'] = data.get('trend', '→ 0%')
        ws[f'E{row}'] = data.get('key_gap', 'None identified')
        
        row += 1
    
    # ... (continue with remediation plan, resources, etc.)
```

---

## Sheet 6: Quarterly Trends

### Purpose
Track privacy compliance metrics over time to demonstrate continuous improvement and identify negative trends.

### Data Requirements

**Historical Data Storage:**

- Maintain archive of past quarter consolidated dashboards
- File naming: `ISMS_A_5_34_7_Privacy_Compliance_Dashboard_YYYYMMDD.xlsx`
- Retention: Minimum 4 quarters (12 months), recommend 8 quarters (24 months)

**Python Loading Historical Data:**

```python
def load_historical_dashboards(archive_dir, quarters=4):
    """
    Load metrics from previous quarters for trend analysis.
    
    Args:
        archive_dir: Path to directory with historical dashboards
        quarters: Number of past quarters to load (default 4)
    
    Returns:
        List of dicts with quarterly metrics
    """
    historical_data = []
    
    # Expected file pattern: ISMS_A_5_34_7_Privacy_Compliance_Dashboard_YYYYMMDD.xlsx
    dashboard_files = sorted([f for f in os.listdir(archive_dir) 
                              if f.startswith('ISMS_A_5_34_7_Privacy_Compliance_Dashboard_')
                              and f.endswith('.xlsx')],
                             reverse=True)[:quarters]
    
    for filename in dashboard_files:
        wb = load_workbook(os.path.join(archive_dir, filename), data_only=True, read_only=True)
        ws = wb['Executive Dashboard']
        
        # Extract key metrics
        quarter_data = {
            'date': filename.split('_')[-1].replace('.xlsx', ''),
            'overall_score': ws['B6'].value,
            'domains_at_target': ws['B7'].value,
            'critical_gaps': ws['B8'].value,
            'high_gaps': ws['B9'].value,
            'medium_gaps': ws['B10'].value,
            'avg_gap_age': ws['B11'].value,
            'evidence_completeness': ws['B12'].value,
        }
        
        historical_data.append(quarter_data)
        wb.close()
    
    return historical_data
```

### Column Definitions

| Col | Column Name | Data Type | Width | Source | Notes |
|-----|------------|-----------|-------|--------|-------|
| A | Quarter | Text | 12 | Historical file dates | E.g., "Q1 2024", "Q2 2024" |
| B | Date | Date | 12 | From filename | Consolidation run date |
| C | Overall Score | Percentage | 12 | Historical Sheet 1, Cell B6 | Overall compliance % |
| D | Domains ≥80% | Text | 15 | Historical | E.g., "4/6" |
| E | Critical Gaps | Number | 12 | Historical | Count |
| F | High Gaps | Number | 12 | Historical | Count |
| G | Medium Gaps | Number | 12 | Historical | Count |
| H | Avg Gap Age (Days) | Number | 12 | Historical | Average |
| I | Evidence Completeness | Percentage | 12 | Historical | % |
| J | DPO Sign-Off | Text | 12 | Historical | "6/6" or similar |

### Example Data

| Quarter | Date | Overall Score | Domains ≥80% | Critical | High | Medium | Avg Gap Age | Evidence % | DPO Sign-Off |
|---------|------|---------------|--------------|----------|------|--------|-------------|------------|--------------|
| Q1 2024 | 2024-01-31 | 68% | 2/6 | 5 | 24 | 35 | 85 | 75% | 4/6 |
| Q2 2024 | 2024-04-30 | 72% | 3/6 | 3 | 20 | 30 | 78 | 80% | 5/6 |
| Q3 2024 | 2024-07-31 | 75% | 4/6 | 2 | 15 | 25 | 68 | 83% | 6/6 |
| Q4 2024 | 2024-10-31 | 78% | 4/6 | 3 | 18 | 22 | 62 | 85% | 6/6 |
| **Q1 2025** | **2025-01-30** | **85%** | **5/6** | **0** | **6** | **12** | **42** | **90%** | **6/6** |

### Trend Calculations

**Quarter-over-Quarter Change:**
```python
current_score = 0.85
previous_score = 0.78
qoq_change = current_score - previous_score  # +0.07 = +7%
```

**Year-over-Year Change:**
```python
current_score = 0.85
yoy_score = 0.68  # Q1 2024
yoy_change = current_score - yoy_score  # +0.17 = +17%
```

### Charts

**Chart 1: Overall Compliance Trend (Line Chart)**

- Location: A25:L40
- Type: Line chart with markers
- X-axis: Quarters
- Y-axis: Overall Score (0-100%)
- Line: Blue with markers
- Target Line: 80% threshold (green dashed line)
- Annotations: Major improvements highlighted

**Chart 2: Gap Count Trends (Stacked Area Chart)**

- Location: A42:L57
- Type: Stacked area chart
- X-axis: Quarters
- Y-axis: Count
- Layers: Critical (Red), High (Orange), Medium (Yellow)
- Shows gap reduction over time

**Chart 3: Domain Score Evolution (Multi-Line Chart)**

- Location: A59:L74
- Type: Multi-line chart
- X-axis: Quarters
- Y-axis: Score (0-100%)
- Lines: 6 domains (different colors)
- Target Line: 80%

---

## Python Script Implementation Architecture

### Script Name
```
generate_a5347_compliance_dashboard.py
```

### Command-Line Usage

**Explicit File Specification:**
```bash
python3 generate_a5347_compliance_dashboard.py \
    --pii ISMS_A_5_34_1_PII_Identification_Assessment_20250130.xlsx \
    --legal ISMS_A_5_34_2_Legal_Basis_Assessment_20250130.xlsx \
    --dsr ISMS_A_5_34_3_DSR_Management_Assessment_20250130.xlsx \
    --toms ISMS_A_5_34_4_TOMs_Assessment_20250130.xlsx \
    --dpia ISMS_A_5_34_5_DPIA_Assessment_20250130.xlsx \
    --xfer ISMS_A_5_34_6_Cross_Border_Transfer_Assessment_20250130.xlsx \
    --output ./
```

**Auto-Detection (Date-Based):**
```bash
python3 generate_a5347_compliance_dashboard.py \
    --date 20250130 \
    --dir /privacy-assessments/2025-Q1/
```

**Historical Trend Analysis:**
```bash
python3 generate_a5347_compliance_dashboard.py \
    --date 20250130 \
    --dir /privacy-assessments/2025-Q1/ \
    --history /privacy-assessments/ \
    --quarters 4
```

### Script Structure

#### 1. Header (Lines 1-250)
**REFERENCE QUALITY HEADER** per A.8.24/A.5.34.1 standard (255 lines)

#### 2. Imports (Lines 252-265)
```python
import argparse
import os
from datetime import datetime, timedelta
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import LineChart, BarChart, PieChart, Reference
from openpyxl.utils import get_column_letter
```

#### 3. Configuration (Lines 267-300)
```python
# Color palette
COLORS = {
    'header_blue': 'FF1F4E78',
    'light_green': 'FFC6EFCE',
    'light_yellow': 'FFFFEB9C',
    'light_red': 'FFFFC7CE',
    'dark_green': 'FF006100',
    'dark_orange': 'FF9C5700',
    'dark_red': 'FF9C0006',
}

# Domain names mapping
DOMAIN_NAMES = {
    'A.5.34.1': 'PII Identification',
    'A.5.34.2': 'Legal Basis',
    'A.5.34.3': 'DSR Management',
    'A.5.34.4': 'TOMs',
    'A.5.34.5': 'DPIA',
    'A.5.34.6': 'Cross-Border Transfer',
}

# Domain weights for overall score
DOMAIN_WEIGHTS = {
    'A.5.34.1': 0.20,
    'A.5.34.2': 0.20,
    'A.5.34.3': 0.15,
    'A.5.34.4': 0.20,
    'A.5.34.5': 0.10,
    'A.5.34.6': 0.15,
}

# Output filename
FILE_PREFIX = "ISMS_A_5_34_7_Privacy_Compliance_Dashboard"
```

#### 4. Data Extraction Functions (Lines 302-500)

```python
def extract_domain_metrics(domain_id, workbook_path):
    """
    Extract metrics from domain assessment workbook.
    
    Returns dict with:

    - compliance_score
    - critical_gaps
    - high_gaps
    - medium_gaps
    - low_gaps
    - last_updated
    - evidence_collected
    - evidence_required

    """
    wb = load_workbook(workbook_path, data_only=True, read_only=True)
    
    # Find dashboard sheet (name varies by domain)
    dashboard_names = ['Dashboard', 'Summary', 'Compliance Dashboard']
    ws_dashboard = None
    for sheet_name in dashboard_names:
        if sheet_name in wb.sheetnames:
            ws_dashboard = wb[sheet_name]
            break
    
    if not ws_dashboard:
        raise ValueError(f"Dashboard sheet not found in {workbook_path}")
    
    # Extract metrics (cell references must match domain workbook structure)
    # NOTE: These cell references are ASSUMPTIONS - verify against actual workbooks
    metrics = {
        'compliance_score': ws_dashboard['B14'].value,  # Assuming % compliant metric
        'critical_gaps': ws_dashboard['B26'].value,
        'high_gaps': ws_dashboard['B27'].value,
        'medium_gaps': ws_dashboard['B28'].value,
        'low_gaps': ws_dashboard['B29'].value,
        'last_updated': ws_dashboard['B36'].value or datetime.now(),
    }
    
    wb.close()
    return metrics

def extract_all_gaps(domain_id, workbook_path):
    """Extract gap registry from domain workbook."""
    gaps = []
    
    wb = load_workbook(workbook_path, data_only=True, read_only=True)
    
    # Find gap analysis sheet
    gap_sheet_names = ['Gap Analysis', 'Gaps', 'Remediation']
    ws_gap = None
    for sheet_name in gap_sheet_names:
        if sheet_name in wb.sheetnames:
            ws_gap = wb[sheet_name]
            break
    
    if not ws_gap:
        wb.close()
        return gaps
    
    # Extract gaps (row 2 onwards)
    for row_num in range(2, ws_gap.max_row + 1):
        gap_id = ws_gap[f'A{row_num}'].value
        if not gap_id:
            break
        
        gap = {
            'source_domain': domain_id,
            'gap_id': f"{domain_id}-{gap_id}",
            'gap_type': ws_gap[f'C{row_num}'].value,
            'description': ws_gap[f'D{row_num}'].value,
            'risk_level': ws_gap[f'G{row_num}'].value,
            'owner': ws_gap[f'O{row_num}'].value,
            'target_date': ws_gap[f'Q{row_num}'].value,
            'status': ws_gap[f'S{row_num}'].value,
        }
        
        gaps.append(gap)
    
    wb.close()
    return gaps

def extract_evidence_metrics(domain_id, workbook_path):
    """Extract evidence completeness from domain workbook."""
    # (Implementation as shown in Sheet 4 section above)
    pass

def load_historical_data(archive_dir, quarters=4):
    """Load historical dashboard data for trend analysis."""
    # (Implementation as shown in Sheet 6 section above)
    pass
```

#### 5. Dashboard Generation Functions (Lines 502-1200)

```python
def create_executive_dashboard(wb, domain_data, gaps):
    """Create Sheet 1: Executive Dashboard."""
    # (Implementation as shown in Sheet 1 section)
    pass

def create_consolidated_gap_registry(wb, all_gaps):
    """Create Sheet 2: Consolidated Gap Registry."""
    # (Implementation as shown in Sheet 2 section)
    pass

def create_risk_heat_map(wb, domain_data, all_gaps):
    """Create Sheet 3: Risk Heat Map."""
    # (Implementation as shown in Sheet 3 section)
    pass

def create_evidence_completeness(wb, evidence_data):
    """Create Sheet 4: Evidence Completeness."""
    # (Implementation as shown in Sheet 4 section)
    pass

def create_executive_summary(wb, domain_data, gaps, evidence):
    """Create Sheet 5: Executive Summary."""
    # (Implementation as shown in Sheet 5 section)
    pass

def create_quarterly_trends(wb, domain_data, historical_data):
    """Create Sheet 6: Quarterly Trends."""
    # (Implementation as shown in Sheet 6 section)
    pass
```

#### 6. Main Function (Lines 1202-1350)

```python
def main():
    """Generate Privacy Compliance Dashboard."""
    # Parse arguments
    parser = argparse.ArgumentParser(
        description='Generate ISMS A.5.34.7 Privacy Compliance Dashboard'
    )
    parser.add_argument('--pii', type=str, help='A.5.34.1 workbook path')
    parser.add_argument('--legal', type=str, help='A.5.34.2 workbook path')
    parser.add_argument('--dsr', type=str, help='A.5.34.3 workbook path')
    parser.add_argument('--toms', type=str, help='A.5.34.4 workbook path')
    parser.add_argument('--dpia', type=str, help='A.5.34.5 workbook path')
    parser.add_argument('--xfer', type=str, help='A.5.34.6 workbook path')
    parser.add_argument('--date', type=str, help='Date suffix for auto-detection')
    parser.add_argument('--dir', type=str, default='.', help='Directory with workbooks')
    parser.add_argument('--history', type=str, help='Directory with historical dashboards')
    parser.add_argument('--quarters', type=int, default=4, help='Quarters of history to load')
    parser.add_argument('--output', type=str, default='.', help='Output directory')
    args = parser.parse_args()
    
    # Determine workbook paths (explicit or auto-detect)
    if args.date:
        # Auto-detect based on date suffix
        workbook_paths = {
            'A.5.34.1': os.path.join(args.dir, f'ISMS_A_5_34_1_PII_Identification_Assessment_{args.date}.xlsx'),
            'A.5.34.2': os.path.join(args.dir, f'ISMS_A_5_34_2_Legal_Basis_Assessment_{args.date}.xlsx'),
            'A.5.34.3': os.path.join(args.dir, f'ISMS_A_5_34_3_DSR_Management_Assessment_{args.date}.xlsx'),
            'A.5.34.4': os.path.join(args.dir, f'ISMS_A_5_34_4_TOMs_Assessment_{args.date}.xlsx'),
            'A.5.34.5': os.path.join(args.dir, f'ISMS_A_5_34_5_DPIA_Assessment_{args.date}.xlsx'),
            'A.5.34.6': os.path.join(args.dir, f'ISMS_A_5_34_6_Cross_Border_Transfer_Assessment_{args.date}.xlsx'),
        }
    else:
        # Explicit paths
        workbook_paths = {
            'A.5.34.1': args.pii,
            'A.5.34.2': args.legal,
            'A.5.34.3': args.dsr,
            'A.5.34.4': args.toms,
            'A.5.34.5': args.dpia,
            'A.5.34.6': args.xfer,
        }
    
    # Extract data from all domain workbooks
    print("Extracting data from domain assessments...")
    domain_data = {}
    all_gaps = []
    evidence_data = {}
    
    for domain_id, workbook_path in workbook_paths.items():
        print(f"  Loading {domain_id}: {workbook_path}")
        
        if not os.path.exists(workbook_path):
            print(f"  WARNING: {workbook_path} not found, skipping")
            continue
        
        domain_data[domain_id] = extract_domain_metrics(domain_id, workbook_path)
        all_gaps.extend(extract_all_gaps(domain_id, workbook_path))
        evidence_data[domain_id] = extract_evidence_metrics(domain_id, workbook_path)
    
    # Load historical data if requested
    historical_data = []
    if args.history:
        print(f"Loading {args.quarters} quarters of historical data...")
        historical_data = load_historical_data(args.history, args.quarters)
    
    # Create consolidated workbook
    print("Creating consolidated dashboard...")
    wb = Workbook()
    wb.remove(wb.active)
    
    print("  Creating Sheet 1: Executive Dashboard...")
    create_executive_dashboard(wb, domain_data, all_gaps)
    
    print("  Creating Sheet 2: Consolidated Gap Registry...")
    create_consolidated_gap_registry(wb, all_gaps)
    
    print("  Creating Sheet 3: Risk Heat Map...")
    create_risk_heat_map(wb, domain_data, all_gaps)
    
    print("  Creating Sheet 4: Evidence Completeness...")
    create_evidence_completeness(wb, evidence_data)
    
    print("  Creating Sheet 5: Executive Summary...")
    create_executive_summary(wb, domain_data, all_gaps, evidence_data)
    
    print("  Creating Sheet 6: Quarterly Trends...")
    create_quarterly_trends(wb, domain_data, historical_data)
    
    # Save consolidated dashboard
    date_suffix = args.date if args.date else datetime.now().strftime('%Y%m%d')
    filename = f"{FILE_PREFIX}_{date_suffix}.xlsx"
    output_path = os.path.join(args.output, filename)
    
    print(f"\nSaving consolidated dashboard to {output_path}...")
    wb.save(output_path)
    
    print(f"\nSuccess! Privacy Compliance Dashboard created: {output_path}")
    print("\nNext steps:")
    print("1. Review Executive Dashboard (Sheet 1) for overall privacy compliance status")
    print("2. Prioritize gaps in Consolidated Gap Registry (Sheet 2)")
    print("3. Analyze Risk Heat Map (Sheet 3) for cross-domain risk patterns")
    print("4. Verify Evidence Completeness (Sheet 4) for audit readiness")
    print("5. Present Executive Summary (Sheet 5) to Privacy Committee/Board")
    print("6. Track Quarterly Trends (Sheet 6) for continuous improvement")

if __name__ == '__main__':
    main()
```

---

**END OF PART III: Technical Specifications (Sheets 4-6) + Python Implementation**

**END OF ISMS-IMP-A.5.34.7**

---

**END OF SPECIFICATION**

---

*"Prediction is very difficult, especially about the future."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
