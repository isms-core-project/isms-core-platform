**ISMS-IMP-A.5.37.4-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.37: Documented Operating Procedures

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.4-TG |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.37: Documented Operating Procedures |
| **Parent Policy** | ISMS-POL-A.5.37 Documented Operating Procedures Policy |
| **Related IMPs** | ISMS-IMP-A.5.37.1, ISMS-IMP-A.5.37.2, ISMS-IMP-A.5.37.3 |
| **Version** | 1.0 |
| **Classification** | Internal Use |
| **Owner** | Information Security Manager |
| **Last Review** | [Date to be set] |
| **Framework Version** | 1.0 |
| **Assessment Type** | Management Dashboard and Reporting |

---

## Control Requirement

> "Operating procedures for information processing facilities should be documented and made available to personnel who need them."
>
> — ISO/IEC 27001:2022, Annex A Control 5.37

---

## Table of Contents

### PART I: USER COMPLETION GUIDE
1. [Dashboard Overview](#1-dashboard-overview)
2. [Control Requirements](#2-control-requirements)
3. [Prerequisites](#3-prerequisites)
4. [Dashboard Views](#4-dashboard-views)
5. [Key Performance Indicators](#5-key-performance-indicators)
6. [Workbook Structure](#6-workbook-structure)
7. [Completion Walkthrough](#7-completion-walkthrough)
8. [Data Refresh Process](#8-data-refresh-process)
9. [Reporting and Export](#9-reporting-and-export)
10. [Evidence Collection](#10-evidence-collection)
11. [Common Pitfalls](#11-common-pitfalls)
12. [Quality Checklist](#12-quality-checklist)
13. [Review and Approval](#13-review-and-approval)
14. [Related Controls](#14-related-controls)

### PART II: TECHNICAL SPECIFICATION
15. [Workbook Architecture](#15-workbook-architecture)
16. [Sheet Specifications](#16-sheet-specifications)
17. [Data Validation Rules](#17-data-validation-rules)
18. [Conditional Formatting](#18-conditional-formatting)
19. [Formula Specifications](#19-formula-specifications)
20. [Chart Specifications](#20-chart-specifications)
21. [Cell Styling Standards](#21-cell-styling-standards)
22. [Generator Script Reference](#22-generator-script-reference)

---

# Technical Specification

## 15. Workbook Architecture

### 15.1 Generator Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a537_4_compliance_dashboard.py` |
| **Script Location** | `10-isms-scr-base/isms-a.5.37-documented-procedures/10_generator-master/` |
| **Output Location** | `10-isms-scr-base/isms-a.5.37-documented-procedures/90_workbooks/` |
| **Output Filename** | `ISMS-IMP-A.5.37.4_Compliance_Dashboard_YYYYMMDD.xlsx` |

### 15.2 Technical Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    WORKBOOK ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    HEADER STRUCTURE                       │   │
│  │  Row 1: Dashboard Title Bar (merged A1:H1)               │   │
│  │  Row 2: Report Period                                     │   │
│  │  Row 3: Last Refreshed Date                               │   │
│  │  Row 4: Empty (separator)                                 │   │
│  │  Row 5+: Dashboard Content                                │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │Executive │ │Category  │ │Review    │ │Quality   │          │
│  │Dashboard │ │Analysis  │ │Status    │ │Overview  │          │
│  │ Sheet 1  │ │ Sheet 2  │ │ Sheet 3  │ │ Sheet 4  │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐          │
│  │Gap       │ │Change    │ │Trend     │ │Data      │          │
│  │Tracking  │ │Activity  │ │History   │ │Sources   │          │
│  │ Sheet 5  │ │ Sheet 6  │ │ Sheet 7  │ │ Sheet 8  │          │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘          │
│                                                                 │
│  ┌──────────┐                                                   │
│  │Instruc-  │                                                   │
│  │tions     │                                                   │
│  │ Sheet 9  │                                                   │
│  └──────────┘                                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 16. Sheet Specifications

### Sheet 1: Executive_Dashboard

**Purpose:** High-level KPIs and compliance summary

**Layout:**

| Section | Location | Content |
|---------|----------|---------|
| Title Block | A1:H3 | Dashboard title, period, refresh date |
| Overall Score | B5:C8 | Compliance score gauge |
| KPI Cards | D5:H8 | Individual KPI values with traffic lights |
| Trend Summary | B10:H12 | Sparklines and trend arrows |
| Critical Issues | B14:H20 | List of items requiring attention |
| Period Notes | B22:H25 | Narrative summary |

**Key Cells:**

| Cell | Content | Formula/Value |
|------|---------|---------------|
| C6 | Overall Compliance Score | Composite formula |
| D6 | Approval Rate | From Data_Sources |
| E6 | Review Currency | From Data_Sources |
| F6 | Avg Quality Score | From Data_Sources |
| G6 | Open Gaps | From Data_Sources |
| H6 | Overdue Reviews | From Data_Sources |

### Sheet 2: Category_Analysis

**Purpose:** Performance breakdown by procedure category

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Category | 25 | Text | Procedure category name |
| B | Total_Count | 12 | Number | Total procedures |
| C | Documented | 12 | Number | With documentation |
| D | Approved | 12 | Number | With approval |
| E | Current | 12 | Number | Review current |
| F | Compliance_% | 12 | Percent | Overall compliance |
| G | Avg_Quality | 12 | Number | Average quality score |
| H | Open_Gaps | 12 | Number | Open gaps |
| I | Status | 10 | Text | Traffic light |

### Sheet 3: Review_Status

**Purpose:** Review compliance summary

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Status | 15 | Text | OVERDUE/DUE SOON/CURRENT |
| B | Count | 10 | Number | Procedures in status |
| C | Percentage | 10 | Percent | % of total |
| D | Critical_Count | 12 | Number | Critical procedures |
| E | High_Count | 12 | Number | High criticality |
| F | Medium_Count | 12 | Number | Medium criticality |
| G | Low_Count | 12 | Number | Low criticality |

**Additional Sections:**
- Top 10 Overdue List (rows 15-25)
- Upcoming Reviews 30-Day List (rows 30-45)

### Sheet 4: Quality_Overview

**Purpose:** Quality assessment summary

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Rating | 20 | Text | Excellent/Good/Adequate/Needs Improvement/Poor |
| B | Count | 10 | Number | Procedures with rating |
| C | Percentage | 10 | Percent | % of assessed |
| D | Avg_Clarity | 12 | Number | Clarity dimension |
| E | Avg_Completeness | 12 | Number | Completeness dimension |
| F | Avg_Accuracy | 12 | Number | Accuracy dimension |
| G | Avg_Usability | 12 | Number | Usability dimension |
| H | Avg_Maintainability | 12 | Number | Maintainability dimension |

### Sheet 5: Gap_Tracking

**Purpose:** Gap remediation status

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Severity | 12 | Text | Critical/High/Medium/Low |
| B | Open | 10 | Number | Open gaps |
| C | In_Progress | 10 | Number | Being addressed |
| D | Closed | 10 | Number | Resolved |
| E | Total | 10 | Number | All gaps |
| F | Closure_Rate | 12 | Percent | % closed |
| G | Avg_Days_Open | 12 | Number | Average age |
| H | Overdue | 10 | Number | Past target date |

### Sheet 6: Change_Activity

**Purpose:** Change request metrics

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Period | 12 | Text | Month/Quarter |
| B | Submitted | 10 | Number | CRs submitted |
| C | Approved | 10 | Number | CRs approved |
| D | Rejected | 10 | Number | CRs rejected |
| E | Implemented | 10 | Number | CRs completed |
| F | Approval_Rate | 12 | Percent | % approved |
| G | Avg_Cycle_Time | 12 | Number | Days to implement |
| H | Emergency_Count | 10 | Number | Emergency changes |

### Sheet 7: Trend_History

**Purpose:** Historical trend data for analysis

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Period | 12 | Text | YYYY-MM or YYYY-QN |
| B | Total_Procedures | 12 | Number | Count at period |
| C | Compliance_% | 12 | Percent | Overall compliance |
| D | Avg_Quality | 12 | Number | Quality score |
| E | Open_Gaps | 12 | Number | Gap count |
| F | Overdue_Reviews | 12 | Number | Overdue count |
| G | CR_Volume | 12 | Number | Change requests |
| H | Notes | 40 | Text | Period notes |

### Sheet 8: Data_Sources

**Purpose:** Document and track source workbook links

| Column | Header | Width | Data Type | Description |
|:------:|--------|:-----:|-----------|-------------|
| A | Source_Workbook | 30 | Text | Source file name |
| B | Sheet | 20 | Text | Source sheet |
| C | Data_Range | 20 | Text | Range reference |
| D | Last_Updated | 15 | Date | Last refresh |
| E | Refresh_Method | 15 | Text | Manual/Auto/Link |
| F | Status | 15 | Text | Connected/Error/Stale |

### Sheet 9: Instructions

**Purpose:** User guidance for dashboard

Static content including:
- Dashboard navigation guide
- Metric definitions
- Data refresh procedures
- Troubleshooting guide
- Report distribution list
- Contact information

---

## 17. Data Validation Rules

### 17.1 Dropdown Lists

| Field | Valid Values |
|-------|--------------|
| **Rating** | Excellent, Good, Adequate, Needs Improvement, Poor |
| **Status** | OVERDUE, DUE SOON, CURRENT |
| **Severity** | Critical, High, Medium, Low |
| **Refresh_Method** | Manual, Auto, Link |
| **Connection_Status** | Connected, Error, Stale |

### 17.2 Numeric Constraints

| Field | Constraint |
|-------|------------|
| Counts | ≥0, whole numbers |
| Percentages | 0-100 |
| Quality Scores | 0.0-5.0 |
| Days | ≥0 |

---

## 18. Conditional Formatting

### 18.1 Traffic Light Rules

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| Overall Compliance | ≥95% | 80-94% | <80% |
| Approval Rate | =100% | 90-99% | <90% |
| Review Currency | ≥95% | 80-94% | <80% |
| Quality Score | ≥4.0 | 3.0-3.9 | <3.0 |
| Open Gaps | 0 | 1-5 | >5 |
| Overdue Reviews | 0 | 1-5 | >5 |

### 18.2 Colour Codes

| Condition | Fill Colour | Text Colour |
|-----------|-------------|-------------|
| Target Met (Green) | #90EE90 | #006400 |
| Warning (Yellow) | #FFFF00 | #8B8000 |
| Critical (Red) | #FF0000 | #FFFFFF |
| Neutral | #FFFFFF | #000000 |

### 18.3 Trend Arrow Formatting

| Trend | Symbol | Colour |
|-------|:------:|--------|
| Improving | ↑ | Green (#008000) |
| Stable | → | Black (#000000) |
| Declining | ↓ | Red (#FF0000) |

---

## 19. Formula Specifications

### 19.1 Overall Compliance Score

```excel
=((D6/100)*0.25)+((E6/100)*0.25)+((F6/5)*0.25)+((1-(G6/B6))*0.25)*100
```

Where:
- D6 = Approval Rate %
- E6 = Review Currency %
- F6 = Average Quality Score (0-5)
- G6 = Open Gaps
- B6 = Total Procedures

### 19.2 Category Compliance

```excel
=SUMPRODUCT((Inventory!$C:$C=A2)*(Inventory!$K:$K="Approved")*(Review!$H:$H<>"OVERDUE"))/
 COUNTIF(Inventory!$C:$C,A2)*100
```

### 19.3 Quality Trend Direction

```excel
=IF(Trend_History!D2>Trend_History!D3,"↑",IF(Trend_History!D2<Trend_History!D3,"↓","→"))
```

### 19.4 Gap Closure Rate

```excel
=D2/(B2+C2+D2)*100
```

Where: B2=Open, C2=In Progress, D2=Closed

### 19.5 Average Days Open

```excel
=AVERAGEIFS(Gap_Analysis!J:J,Gap_Analysis!H:H,"Open")
```

### 19.6 Review Currency Rate

```excel
=COUNTIF(Review_Schedule!$H:$H,"CURRENT")/COUNTA(Review_Schedule!$A:$A)*100
```

---

## 20. Chart Specifications

### 20.1 Compliance Gauge Chart (Executive Dashboard)

| Property | Value |
|----------|-------|
| Type | Doughnut chart (half) |
| Data | [Compliance %, 100-Compliance %] |
| Colours | [Traffic light colour, Light grey] |
| Centre Label | Percentage value, 24pt bold |
| Legend | None |
| Size | 200x150 pixels |

### 20.2 Category Performance Bar Chart

| Property | Value |
|----------|-------|
| Type | Clustered horizontal bar |
| Categories | Procedure categories |
| Values | Compliance % |
| Reference Line | 95% target |
| Colours | Traffic light by value |
| Legend | None |
| Size | 400x300 pixels |

### 20.3 Quality Radar Chart

| Property | Value |
|----------|-------|
| Type | Radar (filled) |
| Axes | 5 quality dimensions |
| Series | Current period, Previous period |
| Scale | 0-5 |
| Colours | Blue (current), Grey (previous) |
| Legend | Bottom |
| Size | 300x300 pixels |

### 20.4 Gap Burn-Down Chart

| Property | Value |
|----------|-------|
| Type | Line with area |
| X-Axis | Time periods (12 months) |
| Y-Axis | Open gap count |
| Trend Line | Linear forecast |
| Colours | Blue area, red trend line |
| Legend | None |
| Size | 400x250 pixels |

### 20.5 CR Volume Trend Chart

| Property | Value |
|----------|-------|
| Type | Stacked column |
| X-Axis | Periods (12 months) |
| Y-Axis | CR count |
| Series | Submitted, Approved, Implemented |
| Colours | Blue, Green, Grey |
| Legend | Bottom |
| Size | 400x250 pixels |

---

## 21. Cell Styling Standards

### 21.1 Colour Palette

| Element | Colour | Hex Code | Usage |
|---------|--------|----------|-------|
| Header Background | Dark Blue | #1F4E79 | Dashboard headers |
| Header Text | White | #FFFFFF | Header text |
| KPI Card Background | Light Blue | #DEEBF7 | Metric cards |
| Success | Green | #90EE90 | Target met indicators |
| Warning | Yellow | #FFFF00 | Warning indicators |
| Critical | Red | #FF0000 | Critical indicators |
| Chart Background | White | #FFFFFF | Chart areas |
| Border | Grey | #D0D0D0 | Cell borders |

### 21.2 Font Standards

| Element | Font | Size | Style |
|---------|------|:----:|-------|
| Dashboard Title | Calibri | 20 | Bold |
| KPI Values | Calibri | 24 | Bold |
| KPI Labels | Calibri | 11 | Regular |
| Section Headers | Calibri | 14 | Bold |
| Data Cells | Calibri | 10 | Regular |
| Trend Arrows | Calibri | 14 | Bold |

### 21.3 Number Formats

| Data Type | Format | Example |
|-----------|--------|---------|
| Percentage | 0% | 95% |
| Quality Score | 0.0 | 4.2 |
| Count | 0 | 42 |
| Date | DD.MM.YYYY | 03.02.2026 |
| Period | YYYY-MM | 2026-02 |

---

## 22. Generator Script Reference

### 22.1 Script Structure

```python
# =============================================================================
# ISMS-IMP-A.5.37.4 - Compliance Dashboard Generator
# =============================================================================
# ISO 27001:2022 Control A.5.37: Documented Operating Procedures
# Generates executive dashboard consolidating A.5.37.1-3 metrics
# =============================================================================

# Document Metadata
DOCUMENT_ID = "ISMS-IMP-A.5.37.4"
WORKBOOK_NAME = "Compliance Dashboard"
CONTROL_ID = "A.5.37"
CONTROL_NAME = "Documented Operating Procedures"

# Output Configuration
OUTPUT_FILENAME = f"{DOCUMENT_ID}_Compliance_Dashboard_{GENERATED_TIMESTAMP}.xlsx"
```

### 22.2 Key Functions

| Function | Purpose |
|----------|---------|
| `create_workbook()` | Initialise workbook with standard structure |
| `create_executive_dashboard()` | Generate Sheet 1 with KPIs and charts |
| `create_category_analysis()` | Generate Sheet 2 with category breakdown |
| `create_review_status()` | Generate Sheet 3 with review metrics |
| `create_quality_overview()` | Generate Sheet 4 with quality data |
| `create_gap_tracking()` | Generate Sheet 5 with gap metrics |
| `create_change_activity()` | Generate Sheet 6 with CR metrics |
| `create_trend_history()` | Generate Sheet 7 with trend data |
| `create_data_sources()` | Generate Sheet 8 with source links |
| `create_instructions()` | Generate Sheet 9 with user guide |
| `create_charts()` | Add visual elements to dashboard |
| `apply_conditional_formatting()` | Apply traffic light rules |
| `apply_formulas()` | Add calculated fields |
| `style_workbook()` | Apply consistent styling |

### 22.3 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| openpyxl | ≥3.0.0 | Excel workbook generation |
| openpyxl.chart | ≥3.0.0 | Chart creation |
| datetime | stdlib | Date handling |
| logging | stdlib | Execution logging |

### 22.4 Execution

```bash
cd 10-isms-scr-base/isms-a.5.37-documented-procedures/10_generator-master/
python3 generate_a537_4_compliance_dashboard.py
mv ISMS-IMP-A.5.37.4_*.xlsx ../90_workbooks/
```

### 22.5 Output Verification

After generation, verify:
- [ ] All 9 sheets created
- [ ] Executive Dashboard layout correct
- [ ] Charts render properly
- [ ] Conditional formatting applied
- [ ] Formulas calculate correctly
- [ ] Print area configured for each sheet
- [ ] Headers/footers set for printing

---

**END OF SPECIFICATION**

---

*"You can't manage what you can't measure."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
