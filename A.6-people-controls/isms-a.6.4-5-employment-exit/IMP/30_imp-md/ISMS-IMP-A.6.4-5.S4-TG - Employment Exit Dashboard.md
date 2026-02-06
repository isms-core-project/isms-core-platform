**ISMS-IMP-A.6.4-5.S4-TG - Employment Exit Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.4, A.6.5

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.4-5.S4-TG |
| **Title** | Employment Exit Compliance Dashboard |
| **Control Reference** | ISO/IEC 27001:2022 A.6.4, A.6.5 |
| **Control Name** | Disciplinary Process / Responsibilities After Termination |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Chief Information Security Officer (CISO) |
| **Classification** | Internal |
| **Framework Version** | 1.0 |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Dashboard Metrics](#14-dashboard-metrics)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 KPI Definitions](#17-kpi-definitions)
   - [1.8 Trend Analysis](#18-trend-analysis)
   - [1.9 Evidence Collection](#19-evidence-collection)
   - [1.10 Common Pitfalls](#110-common-pitfalls)
   - [1.11 Quality Checklist](#111-quality-checklist)
   - [1.12 Review and Approval](#112-review-and-approval)
   - [1.13 Related Controls](#113-related-controls)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Architecture](#21-workbook-architecture)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Data Validations](#23-data-validations)
   - [2.4 Conditional Formatting](#24-conditional-formatting)
   - [2.5 Formula Specifications](#25-formula-specifications)
   - [2.6 Cell Styling Standards](#26-cell-styling-standards)
   - [2.7 Generator Script Reference](#27-generator-script-reference)

---

# Technical Specification

---

## 2.1 Workbook Architecture

### File Details

| Attribute | Value |
|-----------|-------|
| **Filename** | `ISMS-IMP-A.6.4-5.S4_Employment_Exit_Dashboard_YYYYMMDD.xlsx` |
| **Format** | Microsoft Excel Open XML (.xlsx) |
| **Sheets** | 9 |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows | Columns |
|-------------|------------|---------|------|---------|
| 1 | Executive_Dashboard | KPI summary | 30 | 6 |
| 2 | Exit_Metrics | Exit statistics | 24+ | 8 |
| 3 | Access_Revocation_Metrics | Revocation compliance | 24+ | 8 |
| 4 | Asset_Metrics | Asset recovery | 24+ | 7 |
| 5 | Disciplinary_Metrics | Case statistics | 24+ | 7 |
| 6 | Obligation_Metrics | Post-employment | 24+ | 7 |
| 7 | Trend_Analysis | Historical trends | 24+ | 10 |
| 8 | Data_Sources | Source references | 10 | 6 |
| 9 | Instructions | Guidance | 50 | 2 |

---

## 2.2 Sheet Specifications

### Sheet 1: Executive_Dashboard

#### Layout

| Row | Content |
|-----|---------|
| 1 | Title: Employment Exit Compliance Dashboard |
| 2 | Reporting Period |
| 3 | Blank |
| 4-5 | Header: Key Performance Indicators |
| 6-15 | KPI Table (Metric, Target, Actual, Status, Trend) |
| 16-17 | Blank |
| 18-19 | Header: Highlights and Issues |
| 20-25 | Summary insights and action items |
| 26-27 | Blank |
| 28-30 | Sign-off section |

#### KPI Table Structure

| Column A | Column B | Column C | Column D | Column E |
|----------|----------|----------|----------|----------|
| KPI Name | Target | Actual | Status | Trend |
| Exit Completion Rate | 100% | [Formula] | [RAG] | [Arrow] |
| Access Revocation SLA | 100% | [Formula] | [RAG] | [Arrow] |
| Asset Recovery Rate | >95% | [Formula] | [RAG] | [Arrow] |
| Orphaned Accounts | 0 | [Formula] | [RAG] | [Arrow] |
| Exit Interview Rate | 100% | [Formula] | [RAG] | [Arrow] |
| Acknowledgement Rate | 100% | [Formula] | [RAG] | [Arrow] |
| Case Closure <30d | >90% | [Formula] | [RAG] | [Arrow] |

### Sheet 2: Exit_Metrics

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Period | 12 | Text |
| B | Total_Exits | 14 | Number |
| C | Voluntary | 12 | Number |
| D | Involuntary | 14 | Number |
| E | Contractors | 14 | Number |
| F | Fully_Complete | 16 | Number |
| G | Completion_Rate | 16 | Percentage |
| H | Outstanding_Items | 18 | Number |

### Sheet 3: Access_Revocation_Metrics

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Period | 12 | Text |
| B | Total_Revocations | 18 | Number |
| C | Within_SLA | 14 | Number |
| D | SLA_Compliance | 16 | Percentage |
| E | Avg_Revocation_Hours | 20 | Number |
| F | Same_Day_Rate | 16 | Percentage |
| G | Privileged_Compliance | 20 | Percentage |
| H | Third_Party_Notified | 20 | Percentage |

### Sheet 7: Trend_Analysis

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Period | 12 | Text |
| B | Exit_Completion | 16 | Percentage |
| C | SLA_Compliance | 16 | Percentage |
| D | Asset_Recovery | 16 | Percentage |
| E | Orphaned_Accounts | 18 | Number |
| F | Disciplinary_Cases | 18 | Number |
| G | Avg_Case_Duration | 18 | Number |
| H | Active_Obligations | 18 | Number |
| I | Enforcement_Cases | 18 | Number |
| J | Rolling_3M_Completion | 20 | Percentage |

---

## 2.3 Data Validations

### Period Dropdown

```python
PERIOD_LIST = [
    "2026-01", "2026-02", "2026-03", "2026-04",
    "2026-05", "2026-06", "2026-07", "2026-08",
    "2026-09", "2026-10", "2026-11", "2026-12"
]
```

### RAG_Status Dropdown

```python
RAG_STATUS_LIST = [
    "Green",
    "Amber",
    "Red"
]
```

### Update_Method Dropdown

```python
UPDATE_METHOD_LIST = [
    "Manual",
    "Linked",
    "Automated"
]
```

---

## 2.4 Conditional Formatting

### Executive_Dashboard RAG Status

| Value | Fill Colour | Font Colour |
|-------|-------------|-------------|
| Green | Light Green (#C6EFCE) | Dark Green (#006100) |
| Amber | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Red | Light Red (#FFC7CE) | Dark Red (#9C0006) |

### Trend Arrows

| Trend | Symbol | Colour |
|-------|--------|--------|
| Improving | ▲ | Green |
| Stable | ► | Yellow |
| Declining | ▼ | Red |

### Metric Thresholds

**Exit Completion Rate:**
- Green: ≥98%
- Amber: 90-97%
- Red: <90%

**SLA Compliance:**
- Green: 100%
- Amber: 95-99%
- Red: <95%

**Asset Recovery:**
- Green: ≥95%
- Amber: 85-94%
- Red: <85%

**Orphaned Accounts:**
- Green: 0
- Amber: 1-2
- Red: >2

---

## 2.5 Formula Specifications

### Executive_Dashboard Formulas

#### Exit Completion Rate

```excel
=SUMPRODUCT((Exit_Metrics!A:A=Dashboard_Period)*(Exit_Metrics!G:G))
```

#### SLA Compliance

```excel
=SUMPRODUCT((Access_Revocation_Metrics!A:A=Dashboard_Period)*(Access_Revocation_Metrics!D:D))
```

#### Asset Recovery Rate

```excel
=SUMPRODUCT((Asset_Metrics!A:A=Dashboard_Period)*(Asset_Metrics!D:D))
```

#### RAG Status (Exit Completion)

```excel
=IF(C6>=0.98, "Green", IF(C6>=0.9, "Amber", "Red"))
```

#### Trend Arrow (Exit Completion)

```excel
=IF(CurrentMonth-PreviousMonth>0.01, "▲", IF(CurrentMonth-PreviousMonth<-0.01, "▼", "►"))
```

### Trend_Analysis Formulas

#### 3-Month Rolling Average

```excel
=AVERAGE(B2:B4)
```

#### Month-over-Month Change

```excel
=(B2-B3)/B3
```

#### Year-over-Year Comparison

```excel
=B2-B14
```

---

## 2.6 Cell Styling Standards

### Dashboard Styling

| Element | Font | Size | Style |
|---------|------|------|-------|
| Title | Calibri | 18 | Bold |
| Section Header | Calibri | 14 | Bold |
| KPI Labels | Calibri | 11 | Normal |
| KPI Values | Calibri | 12 | Bold |
| Status Indicators | Calibri | 11 | Bold, Centered |

### Colour Palette

| Purpose | Hex Code |
|---------|----------|
| Dashboard Title | #003366 |
| Section Header | #4472C4 |
| Green Status | #C6EFCE |
| Amber Status | #FFEB9C |
| Red Status | #FFC7CE |

---

## 2.7 Generator Script Reference

### Script Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a645_4_dashboard.py` |
| **Location** | `10-isms-scr-base/isms-a.6.4-5-employment-exit/10_generator-master/` |
| **Language** | Python 3.8+ |
| **Dependencies** | openpyxl, logging, datetime |

### Execution

```bash
cd 10-isms-scr-base/isms-a.6.4-5-employment-exit/10_generator-master
python3 generate_a645_4_dashboard.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-02-06 -->
