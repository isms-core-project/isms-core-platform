**ISMS-IMP-A.5.37.1-TG - Procedure Inventory Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.37

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.1-TG |
| **Title** | Procedure Inventory Assessment |
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
   - [1.4 Procedure Categories](#14-procedure-categories)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 Procedure Identification Methods](#17-procedure-identification-methods)
   - [1.8 Accessibility Requirements](#18-accessibility-requirements)
   - [1.9 Evidence Collection](#19-evidence-collection)
   - [1.10 Common Pitfalls](#110-common-pitfalls)
   - [1.11 Quality Checklist](#111-quality-checklist)
   - [1.12 Review and Approval](#112-review-and-approval)
   - [1.13 Integration with Other Controls](#113-integration-with-other-controls)
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
| **Filename** | `ISMS-IMP-A.5.37.1_Procedure_Inventory_Assessment_YYYYMMDD.xlsx` |
| **Format** | Microsoft Excel Open XML (.xlsx) |
| **Sheets** | 7 |
| **Protected** | Yes (structure and formatting) |
| **Password** | [Organisation standard] |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 2 |
| 2 | Procedure_Inventory | Master catalogue | 200+ | 16 |
| 3 | Required_Procedures | Compliance reference | 50+ | 8 |
| 4 | Accessibility_Matrix | Access mapping | 200+ | 10 |
| 5 | Gap_Analysis | Gap tracking | 50+ | 10 |
| 6 | Evidence_Register | Evidence links | 50+ | 8 |
| 7 | Approval_SignOff | Authorisation | 15 | 3 |

### Workbook Properties

```python
WORKBOOK_PROPERTIES = {
    "title": "ISMS-IMP-A.5.37.1 Procedure Inventory Assessment",
    "subject": "Operating Procedure Inventory Management",
    "creator": "ISMS Generator",
    "keywords": "ISO27001, A.5.37, Procedures, Operating, Inventory",
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
| 1 | **ISMS-IMP-A.5.37.1** | |
| 2 | **Procedure Inventory Assessment** | |
| 3 | | |
| 4 | **Document Information** | |
| 5 | Control Reference | ISO/IEC 27001:2022 A.5.37 |
| 6 | Document ID | ISMS-IMP-A.5.37.1 |
| 7 | Generated Date | [Date] |
| 8 | Version | 1.0 |
| 9 | | |
| 10 | **Purpose** | |
| 11 | [Purpose text spanning both columns] | |
| ... | ... | ... |

#### Column Widths

| Column | Width (characters) |
|--------|-------------------|
| A | 25 |
| B | 80 |

### Sheet 2: Procedure_Inventory

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Procedure_ID | 15 | Text | SOP-XXX-NNN pattern |
| B | Procedure_Name | 40 | Text | Max 100 chars |
| C | Category | 20 | List | See dropdown |
| D | Process_Owner | 25 | Text | Required |
| E | Department | 20 | Text | Required |
| F | Document_Location | 50 | Text | Path/URL |
| G | Last_Review_Date | 15 | Date | DD.MM.YYYY |
| H | Next_Review_Due | 15 | Date | Calculated |
| I | Review_Cycle_Days | 12 | Number | Default 365 |
| J | Version | 10 | Text | X.Y format |
| K | Approval_Status | 15 | List | See dropdown |
| L | Approver | 25 | Text | Conditional |
| M | Approval_Date | 15 | Date | Conditional |
| N | Related_Controls | 25 | Text | Multi-value |
| O | Criticality | 12 | List | See dropdown |
| P | Notes | 50 | Text | Optional |

#### Header Row Format

```python
HEADER_FORMAT = {
    "font": Font(name='Calibri', size=11, bold=True, color='FFFFFF'),
    "fill": PatternFill(start_color='2E75B6', end_color='2E75B6', fill_type='solid'),
    "alignment": Alignment(horizontal='center', vertical='center', wrap_text=True),
    "border": Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
}
```

### Sheet 3: Required_Procedures

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Reference_ID | 15 | Text | Standard reference |
| B | Required_Procedure | 40 | Text | Procedure name |
| C | ISO_Control | 15 | Text | Control reference |
| D | Category | 20 | List | Category dropdown |
| E | Priority | 12 | List | High/Medium/Low |
| F | Current_Status | 15 | List | Exists/Partial/Missing |
| G | Mapped_Procedure_ID | 15 | Text | Link to inventory |
| H | Gap_Notes | 50 | Text | Gap description |

### Sheet 4: Accessibility_Matrix

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Procedure_ID | 15 | List | From Procedure_Inventory |
| B | IT_Operations | 10 | Boolean | Y/N |
| C | Security_Team | 10 | Boolean | Y/N |
| D | Facilities | 10 | Boolean | Y/N |
| E | Help_Desk | 10 | Boolean | Y/N |
| F | Management | 10 | Boolean | Y/N |
| G | Other_Roles | 20 | Text | Additional roles |
| H | Access_Method | 25 | Text | How accessed |
| I | Verified_Date | 15 | Date | Last verification |
| J | Issues | 30 | Text | Access issues |

### Sheet 5: Gap_Analysis

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap_ID | 20 | Text | GAP-A.5.37.1-NNN |
| B | Gap_Type | 15 | List | See dropdown |
| C | Procedure_Reference | 25 | Text | Procedure or description |
| D | Severity | 12 | List | Critical/High/Medium/Low |
| E | Identified_Date | 15 | Date | DD.MM.YYYY |
| F | Remediation_Owner | 20 | Text | Responsible party |
| G | Target_Date | 15 | Date | Deadline |
| H | Status | 15 | List | Open/In Progress/Closed |
| I | Completion_Date | 15 | Date | When resolved |
| J | Evidence | 30 | Text | Evidence reference |

### Sheet 6: Evidence_Register

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Evidence_ID | 20 | Text | EVD-A.5.37.1-NNN |
| B | Evidence_Type | 20 | List | See dropdown |
| C | Description | 40 | Text | What it demonstrates |
| D | Related_Procedure | 15 | Text | Procedure ID |
| E | Collection_Date | 15 | Date | DD.MM.YYYY |
| F | Location | 40 | Text | Storage path |
| G | Collected_By | 20 | Text | Name |
| H | Valid_Until | 15 | Date | Expiry date |

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
| 10 | Department Owner | | |
| 11 | Information Security Manager | | |
| 12 | | | |
| 13 | **Approval Status** | | |
| 14 | Status | [Approved/Pending/Rejected] | |
| 15 | Comments | [Input field spanning columns] | |

---

## 2.3 Data Validations

### Category Dropdown

```python
CATEGORY_LIST = [
    "System Operations",
    "Security Operations",
    "Facility Operations",
    "Change Management",
    "Recovery Operations",
    "User Management",
    "Network Operations",
    "Database Operations",
    "Application Operations",
    "Other"
]
```

### Approval_Status Dropdown

```python
APPROVAL_STATUS_LIST = [
    "Draft",
    "Pending Approval",
    "Approved",
    "Expired",
    "Under Review",
    "Retired"
]
```

### Criticality Dropdown

```python
CRITICALITY_LIST = [
    "Critical",
    "High",
    "Medium",
    "Low"
]
```

### Gap_Type Dropdown

```python
GAP_TYPE_LIST = [
    "Missing",
    "Incomplete",
    "Outdated",
    "Unapproved",
    "Inaccessible",
    "Other"
]
```

### Evidence_Type Dropdown

```python
EVIDENCE_TYPE_LIST = [
    "Document",
    "Screenshot",
    "Export",
    "Attestation",
    "Meeting Minutes",
    "Other"
]
```

### Current_Status Dropdown

```python
CURRENT_STATUS_LIST = [
    "Exists",
    "Partial",
    "Missing"
]
```

---

## 2.4 Conditional Formatting

### Procedure_Inventory Sheet

#### Review Status Formatting

| Condition | Fill Colour | Font Colour |
|-----------|-------------|-------------|
| Next_Review_Due < TODAY() | Light Red (#FFC7CE) | Dark Red (#9C0006) |
| Next_Review_Due < TODAY()+30 | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Within review cycle | No fill | Default |

#### Approval Status Formatting

| Status | Fill Colour | Font Colour |
|--------|-------------|-------------|
| Approved | Light Green (#C6EFCE) | Dark Green (#006100) |
| Draft | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Pending Approval | Light Blue (#BDD7EE) | Dark Blue (#1F4E79) |
| Expired | Light Red (#FFC7CE) | Dark Red (#9C0006) |
| Under Review | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Retired | Light Grey (#D9D9D9) | Dark Grey (#595959) |

### Gap_Analysis Sheet

#### Severity Formatting

| Severity | Fill Colour | Font Colour |
|----------|-------------|-------------|
| Critical + Open | Light Red (#FFC7CE) | Dark Red (#9C0006), Bold |
| High + Open | Light Orange (#FABF8F) | Dark Orange (#9C5700) |
| Medium + Open | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Low + Open | Light Grey (#D9D9D9) | Dark Grey (#595959) |
| Closed | Light Green (#C6EFCE) | Dark Green (#006100) |

### Required_Procedures Sheet

#### Status Formatting

| Status | Fill Colour | Font Colour |
|--------|-------------|-------------|
| Exists | Light Green (#C6EFCE) | Dark Green (#006100) |
| Partial | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Missing | Light Red (#FFC7CE) | Dark Red (#9C0006) |

---

## 2.5 Formula Specifications

### Procedure_Inventory Calculated Fields

#### Next Review Due Date

```excel
=G2+I2
```
*Calculates next review date from last review plus cycle days*

#### Review Status

```excel
=IF(H2<TODAY(),"OVERDUE",IF(H2<TODAY()+30,"DUE SOON","CURRENT"))
```
*Determines review status based on next review date*

### Dashboard Formulas (if implemented)

#### Total Procedures Count

```excel
=COUNTA(Procedure_Inventory!A:A)-1
```

#### Approved Percentage

```excel
=COUNTIF(Procedure_Inventory!K:K,"Approved")/COUNTA(Procedure_Inventory!A:A)-1)*100
```

#### Overdue Review Count

```excel
=COUNTIF(Procedure_Inventory!H:H,"<"&TODAY())
```

#### Critical Open Gaps

```excel
=COUNTIFS(Gap_Analysis!D:D,"Critical",Gap_Analysis!H:H,"Open")
```

---

## 2.6 Cell Styling Standards

### Colour Palette

| Purpose | Colour Name | Hex Code | RGB |
|---------|-------------|----------|-----|
| Header Background | Theme Blue | #2E75B6 | 46, 117, 182 |
| Header Text | White | #FFFFFF | 255, 255, 255 |
| Alternate Row | Light Grey | #F2F2F2 | 242, 242, 242 |
| Input Field | Light Yellow | #FFFFCC | 255, 255, 204 |
| Success/Approved | Light Green | #C6EFCE | 198, 239, 206 |
| Warning | Light Yellow | #FFEB9C | 255, 235, 156 |
| Error/Alert | Light Red | #FFC7CE | 255, 199, 206 |
| Neutral | Light Grey | #D9D9D9 | 217, 217, 217 |

### Font Standards

| Element | Font | Size | Weight | Colour |
|---------|------|------|--------|--------|
| Sheet Title | Calibri | 16 | Bold | Theme Blue |
| Section Header | Calibri | 12 | Bold | Black |
| Column Header | Calibri | 11 | Bold | White |
| Data Cell | Calibri | 10 | Normal | Black |
| Notes/Comments | Calibri | 9 | Italic | Grey |

### Border Standards

| Element | Style | Colour |
|---------|-------|--------|
| Header Row | Thin all sides | Black |
| Data Rows | Thin all sides | Grey |
| Section Divider | Medium bottom | Black |
| Outer Border | Medium | Black |

### Row Heights

| Row Type | Height (points) |
|----------|-----------------|
| Title | 25 |
| Header | 30 |
| Data | 20 |
| Notes | 15 |

---

## 2.7 Generator Script Reference

### Script Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a537_1_procedure_inventory.py` |
| **Location** | `10-isms-scr-base/isms-a.5.37-documented-procedures/10_generator-master/` |
| **Language** | Python 3.8+ |
| **Dependencies** | openpyxl, logging, datetime |

### Script Structure

```python
# =============================================================================
# ISMS-IMP-A.5.37.1 Procedure Inventory Assessment
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
| `create_procedure_inventory_sheet()` | Generates Procedure_Inventory sheet |
| `create_required_procedures_sheet()` | Generates Required_Procedures sheet |
| `create_accessibility_matrix_sheet()` | Generates Accessibility_Matrix sheet |
| `create_gap_analysis_sheet()` | Generates Gap_Analysis sheet |
| `create_evidence_register_sheet()` | Generates Evidence_Register sheet |
| `create_approval_signoff_sheet()` | Generates Approval_SignOff sheet |
| `apply_conditional_formatting()` | Applies conditional formatting rules |
| `apply_data_validations()` | Applies dropdown validations |
| `generate_workbook()` | Main orchestration function |

### Output Location

```
10-isms-scr-base/
└── isms-a.5.37-documented-procedures/
    └── 90_workbooks/
        └── ISMS-IMP-A.5.37.1_Procedure_Inventory_Assessment_YYYYMMDD.xlsx
```

### Execution

```bash
cd 10-isms-scr-base/isms-a.5.37-documented-procedures/10_generator-master
python3 generate_a537_1_procedure_inventory.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"The beginning of wisdom is the definition of terms."*
— Socrates

<!-- QA_VERIFIED: 2026-02-06 -->
