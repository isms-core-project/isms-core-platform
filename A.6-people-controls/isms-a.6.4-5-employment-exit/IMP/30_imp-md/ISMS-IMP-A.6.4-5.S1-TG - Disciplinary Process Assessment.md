**ISMS-IMP-A.6.4-5.S1-TG - Disciplinary Process Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.4, A.6.5

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.4-5.S1-TG |
| **Title** | Disciplinary Process Assessment |
| **Control Reference** | ISO/IEC 27001:2022 A.6.4, A.6.5 |
| **Control Name** | Disciplinary Process / Responsibilities After Termination |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Chief Human Resources Officer (CHRO) |
| **Classification** | Internal |
| **Framework Version** | 1.0 |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Violation Categories](#14-violation-categories)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 Investigation Framework](#17-investigation-framework)
   - [1.8 Due Process Requirements](#18-due-process-requirements)
   - [1.9 Evidence Collection](#19-evidence-collection)
   - [1.10 Common Pitfalls](#110-common-pitfalls)
   - [1.11 Quality Checklist](#111-quality-checklist)
   - [1.12 Review and Approval](#112-review-and-approval)
   - [1.13 Regulatory Compliance](#113-regulatory-compliance)
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
| **Filename** | `ISMS-IMP-A.6.4-5.S1_Disciplinary_Process_Assessment_YYYYMMDD.xlsx` |
| **Format** | Microsoft Excel Open XML (.xlsx) |
| **Sheets** | 7 |
| **Protected** | Yes (structure and formatting) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 2 |
| 2 | Violation_Categories | Violation classification | 50+ | 8 |
| 3 | Response_Matrix | Response mapping | 20 | 7 |
| 4 | Investigation_Process | Procedure documentation | 30 | 6 |
| 5 | Case_Tracker | Case tracking | 100+ | 8 |
| 6 | Evidence_Register | Evidence tracking | 50+ | 6 |
| 7 | Approval_SignOff | Authorisation | 15 | 3 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

#### Layout

| Row | Column A | Column B |
|-----|----------|----------|
| 1 | **ISMS-IMP-A.6.4-5.S1** | |
| 2 | **Disciplinary Process Assessment** | |
| 3 | | |
| 4 | **Document Information** | |
| 5 | Control Reference | ISO/IEC 27001:2022 A.6.4, A.6.5 |
| 6 | Document ID | ISMS-IMP-A.6.4-5.S1 |
| 7 | Generated Date | [Date] |
| 8 | Version | 1.0 |

#### Column Widths

| Column | Width (characters) |
|--------|-------------------|
| A | 28 |
| B | 70 |

### Sheet 2: Violation_Categories

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Category_ID | 15 | Text | VIOL-### |
| B | Category_Name | 35 | Text | Required |
| C | Severity_Level | 18 | List | Dropdown |
| D | Description | 50 | Text | Required |
| E | Examples | 45 | Text | Required |
| F | Investigation_Required | 12 | List | Yes/No |
| G | Security_Team_Involvement | 15 | List | Yes/No/Conditional |
| H | Related_Policy | 30 | Text | Policy reference |

### Sheet 3: Response_Matrix

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Severity_Level | 18 | List | From categories |
| B | First_Occurrence | 35 | Text | Response description |
| C | Second_Occurrence | 35 | Text | Response description |
| D | Third_Occurrence | 35 | Text | Response description |
| E | Immediate_Actions | 35 | Text | Immediate response |
| F | Mitigating_Factors | 40 | Text | Factors reducing response |
| G | Aggravating_Factors | 40 | Text | Factors increasing response |

### Sheet 4: Investigation_Process

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Phase | 20 | List | Investigation phases |
| B | Activities | 50 | Text | Detailed activities |
| C | Timeline | 20 | Text | Expected duration |
| D | Responsible_Party | 25 | Text | Role(s) responsible |
| E | Outputs | 35 | Text | Required outputs |
| F | Documentation_Required | 35 | Text | Required documentation |

### Sheet 5: Case_Tracker

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Case_ID | 18 | Text | DISC-YYYY-### |
| B | Date_Reported | 14 | Date | DD.MM.YYYY |
| C | Violation_Category | 20 | List | From categories |
| D | Status | 18 | List | Status options |
| E | Investigation_Lead | 25 | Text | Name |
| F | Date_Closed | 14 | Date | DD.MM.YYYY |
| G | Outcome | 40 | Text | Summary |
| H | Notes | 35 | Text | Additional info |

### Sheet 6: Evidence_Register

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Evidence_ID | 20 | Text | EVD-A.6.4.1-### |
| B | Evidence_Description | 50 | Text | Description |
| C | Evidence_Type | 20 | List | Type dropdown |
| D | Storage_Location | 50 | Text | Path/URL |
| E | Collection_Date | 14 | Date | DD.MM.YYYY |
| F | Collected_By | 25 | Text | Name |

### Sheet 7: Approval_SignOff

#### Layout

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 1 | **Assessment Sign-Off** | | |
| 3 | **Assessor Details** | | |
| 4 | Assessor Name | [Input] | |
| 5 | Role | [Input] | |
| 6 | Assessment Date | [Input] | |
| 8 | **Reviewer Sign-Off** | **Signature** | **Date** |
| 9 | HR Director | | |
| 10 | Legal Counsel | | |
| 11 | CISO | | |

---

## 2.3 Data Validations

### Severity_Level Dropdown

```python
SEVERITY_LEVEL_LIST = [
    "Minor",
    "Moderate",
    "Serious",
    "Gross Misconduct"
]
```

### Investigation_Required Dropdown

```python
INVESTIGATION_REQUIRED_LIST = [
    "Yes",
    "No"
]
```

### Security_Team_Involvement Dropdown

```python
SECURITY_INVOLVEMENT_LIST = [
    "Yes",
    "No",
    "Conditional"
]
```

### Case_Status Dropdown

```python
CASE_STATUS_LIST = [
    "Reported",
    "Under Investigation",
    "Pending Decision",
    "Action Taken",
    "Closed",
    "Appealed",
    "Appeal Resolved"
]
```

### Investigation_Phase Dropdown

```python
INVESTIGATION_PHASE_LIST = [
    "Discovery",
    "Assessment",
    "Planning",
    "Evidence Collection",
    "Analysis",
    "Decision",
    "Action",
    "Follow-up",
    "Closure"
]
```

### Evidence_Type Dropdown

```python
EVIDENCE_TYPE_LIST = [
    "Policy Document",
    "Procedure",
    "Case Record",
    "Training Record",
    "Communication",
    "Form/Template",
    "Other"
]
```

---

## 2.4 Conditional Formatting

### Violation_Categories Sheet

#### Severity Level Formatting

| Value | Fill Colour | Font Colour |
|-------|-------------|-------------|
| Minor | Light Blue (#BDD7EE) | Dark Blue (#1F4E79) |
| Moderate | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Serious | Light Orange (#FCE4D6) | Dark Red (#9C0006) |
| Gross Misconduct | Light Red (#FFC7CE) | Dark Red (#9C0006) |

### Case_Tracker Sheet

#### Status Formatting

| Value | Fill Colour | Font Colour |
|-------|-------------|-------------|
| Reported | Light Blue (#BDD7EE) | Dark Blue (#1F4E79) |
| Under Investigation | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Pending Decision | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Action Taken | Light Green (#C6EFCE) | Dark Green (#006100) |
| Closed | Light Grey (#D9D9D9) | Dark Grey (#595959) |
| Appealed | Light Orange (#FCE4D6) | Dark Red (#9C0006) |
| Appeal Resolved | Light Green (#C6EFCE) | Dark Green (#006100) |

---

## 2.5 Formula Specifications

### Case_Tracker Calculated Fields

#### Days Open

```excel
=IF(F2="", TODAY()-B2, F2-B2)
```
*Calculates days between report date and closure (or today if open)*

#### Overdue Flag

```excel
=IF(AND(D2<>"Closed", TODAY()-B2>30), "OVERDUE", "")
```
*Flags cases open more than 30 days*

### Approval_SignOff Summary Formulas

#### Total Categories Defined

```excel
=COUNTA(Violation_Categories!A4:A53)-COUNTBLANK(Violation_Categories!B4:B53)
```

#### Active Cases Count

```excel
=COUNTIF(Case_Tracker!D4:D103,"<>Closed")-COUNTIF(Case_Tracker!D4:D103,"")
```

---

## 2.6 Cell Styling Standards

### Colour Palette

| Purpose | Colour Name | Hex Code |
|---------|-------------|----------|
| Header Background | Navy Blue | #003366 |
| Header Text | White | #FFFFFF |
| Subheader Background | Medium Blue | #4472C4 |
| Column Header | Light Grey | #D9D9D9 |
| Input Field | Light Yellow | #FFFFCC |
| Success/Complete | Light Green | #C6EFCE |
| Warning | Light Yellow | #FFEB9C |
| Alert/Error | Light Red | #FFC7CE |

### Font Standards

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Sheet Title | Calibri | 14 | Bold |
| Section Header | Calibri | 12 | Bold |
| Column Header | Calibri | 10 | Bold |
| Data Cell | Calibri | 10 | Normal |

### Border Standards

| Element | Style |
|---------|-------|
| Header Row | Thin all sides |
| Data Rows | Thin all sides |
| Section Divider | Medium bottom |

---

## 2.7 Generator Script Reference

### Script Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a645_1_disciplinary_process.py` |
| **Location** | `10-isms-scr-base/isms-a.6.4-5-employment-exit/10_generator-master/` |
| **Language** | Python 3.8+ |
| **Dependencies** | openpyxl, logging, datetime |

### Key Functions

| Function | Purpose |
|----------|---------|
| `create_instructions_sheet()` | Generates Instructions sheet |
| `create_violation_categories_sheet()` | Generates Violation_Categories sheet |
| `create_response_matrix_sheet()` | Generates Response_Matrix sheet |
| `create_investigation_process_sheet()` | Generates Investigation_Process sheet |
| `create_case_tracker_sheet()` | Generates Case_Tracker sheet |
| `create_evidence_register_sheet()` | Generates Evidence_Register sheet |
| `create_approval_signoff_sheet()` | Generates Approval_SignOff sheet |

### Output Location

```
10-isms-scr-base/
└── isms-a.6.4-5-employment-exit/
    └── 90_workbooks/
        └── ISMS-IMP-A.6.4-5.S1_Disciplinary_Process_Assessment_YYYYMMDD.xlsx
```

### Execution

```bash
cd 10-isms-scr-base/isms-a.6.4-5-employment-exit/10_generator-master
python3 generate_a645_1_disciplinary_process.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"The art of leadership is saying no, not yes. It is very easy to say yes."*
— Tony Blair

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-02-06 -->
