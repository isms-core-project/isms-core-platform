**ISMS-IMP-A.5.37.2-TG - Procedure Quality Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.37

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.2-TG |
| **Title** | Procedure Quality Assessment |
| **Control Reference** | ISO/IEC 27001:2022 A.5.37 |
| **Control Name** | Documented Operating Procedures |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |
| **Framework Version** | 1.0 |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Quality Framework](#14-quality-framework)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 Quality Scoring Methodology](#17-quality-scoring-methodology)
   - [1.8 Quality Checklist Elements](#18-quality-checklist-elements)
   - [1.9 Evidence Collection](#19-evidence-collection)
   - [1.10 Common Pitfalls](#110-common-pitfalls)
   - [1.11 Quality Checklist](#111-quality-checklist)
   - [1.12 Review and Approval](#112-review-and-approval)
   - [1.13 Improvement Action Management](#113-improvement-action-management)
   - [1.14 Related Controls](#114-related-controls)
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
| **Filename** | `ISMS-IMP-A.5.37.2_Procedure_Quality_Assessment_YYYYMMDD.xlsx` |
| **Format** | Microsoft Excel Open XML (.xlsx) |
| **Sheets** | 7 |
| **Protected** | Yes (structure and formatting) |
| **Password** | [Organisation standard] |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 2 |
| 2 | Quality_Assessment | Quality scoring | 200+ | 14 |
| 3 | Quality_Checklist | Detailed checks | 500+ | 6 |
| 4 | Improvement_Actions | Action tracking | 100+ | 11 |
| 5 | Trend_Analysis | Historical trends | 20+ | 11 |
| 6 | Evidence_Register | Evidence links | 50+ | 7 |
| 7 | Approval_SignOff | Authorisation | 15 | 3 |

### Workbook Properties

```python
WORKBOOK_PROPERTIES = {
    "title": "ISMS-IMP-A.5.37.2 Procedure Quality Assessment",
    "subject": "Operating Procedure Quality Management",
    "creator": "ISMS Generator",
    "keywords": "ISO27001, A.5.37, Procedures, Quality, Assessment",
    "category": "ISMS Assessment Workbook",
    "company": "[Organisation Name]"
}
```

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

#### Layout

| Row | Column A | Column B |
|-----|----------|----------|
| 1 | **ISMS-IMP-A.5.37.2** | |
| 2 | **Procedure Quality Assessment** | |
| 3 | | |
| 4 | **Document Information** | |
| 5 | Control Reference | ISO/IEC 27001:2022 A.5.37 |
| 6 | Document ID | ISMS-IMP-A.5.37.2 |
| 7 | Generated Date | [Date] |
| 8 | Version | 1.0 |

### Sheet 2: Quality_Assessment

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Procedure_ID | 15 | List | From Inventory |
| B | Procedure_Name | 40 | Formula | Lookup |
| C | Assessment_Date | 15 | Date | DD.MM.YYYY |
| D | Assessor | 25 | Text | Required |
| E | Clarity_Score | 12 | Number | 0-5 |
| F | Completeness_Score | 12 | Number | 0-5 |
| G | Accuracy_Score | 12 | Number | 0-5 |
| H | Usability_Score | 12 | Number | 0-5 |
| I | Maintainability_Score | 12 | Number | 0-5 |
| J | Overall_Score | 12 | Formula | Calculated |
| K | Quality_Rating | 15 | Formula | From thresholds |
| L | Priority_Improvements | 40 | Text | Multi-value |
| M | Findings | 50 | Text | Optional |
| N | Next_Review | 15 | Formula | Based on rating |

### Sheet 3: Quality_Checklist

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Procedure_ID | 15 | List | From Inventory |
| B | Check_Category | 20 | List | Structure/Content/Operations |
| C | Check_Item | 50 | Text | Pre-populated |
| D | Status | 12 | List | Pass/Partial/Fail/N/A |
| E | Finding | 40 | Text | If not Pass |
| F | Recommendation | 40 | Text | If not Pass |

### Sheet 4: Improvement_Actions

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Action_ID | 20 | Text | ACT-A.5.37.2-NNN |
| B | Procedure_ID | 15 | List | From Inventory |
| C | Dimension | 15 | List | Quality dimensions |
| D | Issue_Description | 40 | Text | Required |
| E | Action_Required | 40 | Text | Required |
| F | Owner | 25 | Text | Required |
| G | Priority | 12 | List | Critical/High/Medium/Low |
| H | Target_Date | 15 | Date | DD.MM.YYYY |
| I | Status | 15 | List | Open/In Progress/Completed |
| J | Completion_Date | 15 | Date | DD.MM.YYYY |
| K | Verification | 30 | Text | How verified |

### Sheet 5: Trend_Analysis

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Period | 15 | Text | e.g., Q1 2026 |
| B | Procedures_Assessed | 10 | Number | Count |
| C | Avg_Clarity | 12 | Number | Average |
| D | Avg_Completeness | 12 | Number | Average |
| E | Avg_Accuracy | 12 | Number | Average |
| F | Avg_Usability | 12 | Number | Average |
| G | Avg_Maintainability | 12 | Number | Average |
| H | Overall_Avg | 12 | Number | Average |
| I | Excellent_Count | 10 | Number | Count |
| J | Poor_Count | 10 | Number | Count |
| K | Improvement_Pct | 12 | Number | % change |

### Sheet 6: Evidence_Register

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Evidence_ID | 20 | Text | EVD-A.5.37.2-NNN |
| B | Evidence_Type | 20 | List | See dropdown |
| C | Procedure_ID | 15 | Text | Procedure reference |
| D | Description | 40 | Text | What it demonstrates |
| E | Collection_Date | 15 | Date | DD.MM.YYYY |
| F | Location | 40 | Text | Storage path |
| G | Collected_By | 20 | Text | Name |

### Sheet 7: Approval_SignOff

#### Layout

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 1 | **Assessment Sign-Off** | | |
| 2 | | | |
| 3 | **Assessor Details** | | |
| 4 | Assessor Name | [Input field] | |
| 5 | Role | [Input field] | |
| 6 | Assessment Date | [Input field] | |
| 7 | | | |
| 8 | **Reviewer Sign-Off** | **Signature** | **Date** |
| 9 | ISMS Administrator | | |
| 10 | Information Security Manager | | |

---

## 2.3 Data Validations

### Score Validation

```python
SCORE_VALIDATION = {
    "type": "decimal",
    "minimum": 0,
    "maximum": 5,
    "decimal_places": 1
}
```

### Checklist_Status Dropdown

```python
CHECKLIST_STATUS_LIST = [
    "Pass",
    "Partial",
    "Fail",
    "N/A"
]
```

### Dimension Dropdown

```python
DIMENSION_LIST = [
    "Clarity",
    "Completeness",
    "Accuracy",
    "Usability",
    "Maintainability"
]
```

### Action_Status Dropdown

```python
ACTION_STATUS_LIST = [
    "Open",
    "In Progress",
    "Completed",
    "Cancelled"
]
```

### Priority Dropdown

```python
PRIORITY_LIST = [
    "Critical",
    "High",
    "Medium",
    "Low"
]
```

---

## 2.4 Conditional Formatting

### Quality_Assessment Sheet

#### Overall Score Formatting

| Condition | Fill Colour | Font Colour |
|-----------|-------------|-------------|
| Score < 1.5 | Light Red (#FFC7CE) | Dark Red (#9C0006) |
| Score 1.5-2.49 | Light Orange (#FABF8F) | Dark Orange (#9C5700) |
| Score 2.5-3.49 | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Score 3.5-4.49 | Light Green (#C6EFCE) | Dark Green (#006100) |
| Score ≥ 4.5 | Dark Green (#00B050) | White (#FFFFFF) |

#### Quality Rating Formatting

| Rating | Fill Colour | Font Colour |
|--------|-------------|-------------|
| Poor | Light Red (#FFC7CE) | Dark Red (#9C0006), Bold |
| Needs Improvement | Light Orange (#FABF8F) | Dark Orange (#9C5700) |
| Adequate | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Good | Light Green (#C6EFCE) | Dark Green (#006100) |
| Excellent | Dark Green (#00B050) | White (#FFFFFF), Bold |

### Quality_Checklist Sheet

#### Status Formatting

| Status | Fill Colour | Font Colour |
|--------|-------------|-------------|
| Pass | Light Green (#C6EFCE) | Dark Green (#006100) |
| Partial | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Fail | Light Red (#FFC7CE) | Dark Red (#9C0006) |
| N/A | Light Grey (#D9D9D9) | Dark Grey (#595959) |

### Improvement_Actions Sheet

#### Priority + Status Formatting

| Condition | Fill Colour | Font Colour |
|-----------|-------------|-------------|
| Critical + Open | Light Red (#FFC7CE) | Dark Red (#9C0006), Bold |
| Status = Open + Past Due | Light Red (#FFC7CE) | Dark Red (#9C0006) |
| Status = Completed | Light Green (#C6EFCE) | Dark Green (#006100) |

---

## 2.5 Formula Specifications

### Quality_Assessment Calculated Fields

#### Overall Score

```excel
=(E2+F2+G2+H2+I2)/5
```
*Simple average of five dimension scores*

#### Quality Rating

```excel
=IF(J2>=4.5,"Excellent",IF(J2>=3.5,"Good",IF(J2>=2.5,"Adequate",IF(J2>=1.5,"Needs Improvement","Poor"))))
```

#### Next Review Date

```excel
=IF(K2="Excellent",C2+365,IF(K2="Good",C2+180,IF(K2="Adequate",C2+90,C2+30)))
```
*Review frequency based on quality rating*

### Quality_Checklist Calculated Fields

#### Checklist Pass Rate

```excel
=COUNTIF(D:D,"Pass")/(COUNTIF(D:D,"Pass")+COUNTIF(D:D,"Partial")+COUNTIF(D:D,"Fail"))*100
```

### Trend_Analysis Calculated Fields

#### Improvement Percentage

```excel
=(H2-H1)/H1*100
```
*Percentage change from previous period*

---

## 2.6 Cell Styling Standards

### Colour Palette

| Purpose | Colour Name | Hex Code | RGB |
|---------|-------------|----------|-----|
| Header Background | Theme Blue | #2E75B6 | 46, 117, 182 |
| Header Text | White | #FFFFFF | 255, 255, 255 |
| Excellent | Dark Green | #00B050 | 0, 176, 80 |
| Good | Light Green | #C6EFCE | 198, 239, 206 |
| Adequate | Light Yellow | #FFEB9C | 255, 235, 156 |
| Needs Improvement | Light Orange | #FABF8F | 250, 191, 143 |
| Poor | Light Red | #FFC7CE | 255, 199, 206 |

### Font Standards

| Element | Font | Size | Weight | Colour |
|---------|------|------|--------|--------|
| Sheet Title | Calibri | 16 | Bold | Theme Blue |
| Section Header | Calibri | 12 | Bold | Black |
| Column Header | Calibri | 11 | Bold | White |
| Data Cell | Calibri | 10 | Normal | Black |
| Score Cell | Calibri | 10 | Bold | Varies by value |

---

## 2.7 Generator Script Reference

### Script Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a537_2_procedure_quality.py` |
| **Location** | `10-isms-scr-base/isms-a.5.37-documented-procedures/10_generator-master/` |
| **Language** | Python 3.8+ |
| **Dependencies** | openpyxl, logging, datetime |

### Script Structure

```python
# =============================================================================
# ISMS-IMP-A.5.37.2 Procedure Quality Assessment
# Excel Workbook Generator
# =============================================================================

# Section 1: Imports and Configuration
# Section 2: Constants and Metadata
# Section 3: Style Definitions
# Section 4: Data Validation Lists
# Section 5: Sheet Creation Functions
# Section 6: Formatting Functions
# Section 7: Main Generation Function
# Section 8: Entry Point

# =============================================================================
# QA_VERIFIED: [Date]
# QA_STATUS: PASSED - STANDARDIZATION COMPLETE
# =============================================================================
```

### Key Functions

| Function | Purpose |
|----------|---------|
| `create_instructions_sheet()` | Generates Instructions sheet |
| `create_quality_assessment_sheet()` | Generates Quality_Assessment sheet |
| `create_quality_checklist_sheet()` | Generates Quality_Checklist sheet |
| `create_improvement_actions_sheet()` | Generates Improvement_Actions sheet |
| `create_trend_analysis_sheet()` | Generates Trend_Analysis sheet |
| `create_evidence_register_sheet()` | Generates Evidence_Register sheet |
| `create_approval_signoff_sheet()` | Generates Approval_SignOff sheet |
| `apply_conditional_formatting()` | Applies formatting rules |
| `apply_data_validations()` | Applies dropdown validations |
| `generate_workbook()` | Main orchestration function |

### Output Location

```
10-isms-scr-base/
└── isms-a.5.37-documented-procedures/
    └── 90_workbooks/
        └── ISMS-IMP-A.5.37.2_Procedure_Quality_Assessment_YYYYMMDD.xlsx
```

### Execution

```bash
cd 10-isms-scr-base/isms-a.5.37-documented-procedures/10_generator-master
python3 generate_a537_2_procedure_quality.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"Quality is not an act, it is a habit."*
— Aristotle

<!-- QA_VERIFIED: 2026-02-06 -->
