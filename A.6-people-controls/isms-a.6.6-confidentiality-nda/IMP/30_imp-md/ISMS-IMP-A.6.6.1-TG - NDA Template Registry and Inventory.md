**ISMS-IMP-A.6.6.1-TG - NDA Template Registry and Inventory**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.6

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.6.1-TG |
| **Title** | NDA Template Registry and Inventory |
| **Control Reference** | ISO/IEC 27001:2022 A.6.6 |
| **Control Name** | Confidentiality or Non-Disclosure Agreements |
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
   - [1.4 Stakeholder Categories](#14-stakeholder-categories)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 NDA Template Types](#17-nda-template-types)
   - [1.8 Standard Clause Library](#18-standard-clause-library)
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
| **Filename** | `ISMS-IMP-A.6.6.1_NDA_Template_Registry_and_Inventory_YYYYMMDD.xlsx` |
| **Format** | Microsoft Excel Open XML (.xlsx) |
| **Sheets** | 7 |
| **Protected** | Yes (structure and formatting) |
| **Password** | [Organisation standard] |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 2 |
| 2 | Template_Registry | Template master list | 50+ | 13 |
| 3 | Template_Versions | Version history | 200+ | 9 |
| 4 | Applicability_Matrix | Selection guidance | 30+ | 9 |
| 5 | Clause_Library | Standard clauses | 50+ | 8 |
| 6 | Evidence_Register | Evidence tracking | 50+ | 6 |
| 7 | Approval_SignOff | Authorisation | 15 | 3 |

### Workbook Properties

```python
WORKBOOK_PROPERTIES = {
    "title": "ISMS-IMP-A.6.6.1 NDA Template Registry and Inventory",
    "subject": "NDA Template Management Assessment",
    "creator": "ISMS Generator",
    "keywords": "ISO27001, A.6.6, NDA, Confidentiality, Template",
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
| 1 | **ISMS-IMP-A.6.6.1** | |
| 2 | **NDA Template Registry and Inventory** | |
| 3 | | |
| 4 | **Document Information** | |
| 5 | Control Reference | ISO/IEC 27001:2022 A.6.6 |
| 6 | Document ID | ISMS-IMP-A.6.6.1 |
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

### Sheet 2: Template_Registry

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Template_ID | 15 | Text | NDA-TMP-### pattern |
| B | Template_Name | 40 | Text | Max 100 chars |
| C | Template_Type | 20 | List | See dropdown |
| D | Stakeholder_Category | 25 | List | Multiple allowed |
| E | Current_Version | 10 | Text | #.# pattern |
| F | Effective_Date | 12 | Date | DD.MM.YYYY |
| G | Legal_Review_Date | 15 | Date | DD.MM.YYYY |
| H | Legal_Reviewer | 25 | Text | Name and title |
| I | Next_Review_Date | 15 | Date | DD.MM.YYYY |
| J | Template_Owner | 25 | Text | Department/Name |
| K | Storage_Location | 40 | Text | Path/URL |
| L | Status | 15 | List | See dropdown |
| M | Notes | 50 | Text | Max 500 chars |

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

#### Data Row Format

```python
DATA_FORMAT = {
    "font": Font(name='Calibri', size=10),
    "alignment": Alignment(horizontal='left', vertical='top', wrap_text=True),
    "border": Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
}
```

### Sheet 3: Template_Versions

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Template_ID | 15 | List | From Template_Registry |
| B | Version | 10 | Text | #.# pattern |
| C | Version_Date | 12 | Date | DD.MM.YYYY |
| D | Change_Description | 50 | Text | Required |
| E | Change_Reason | 40 | Text | Required |
| F | Changed_By | 25 | Text | Name |
| G | Legal_Approved | 12 | List | Yes/No/Pending |
| H | Legal_Approver | 25 | Text | Name if approved |
| I | Approval_Date | 12 | Date | DD.MM.YYYY |

### Sheet 4: Applicability_Matrix

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Stakeholder_Category | 20 | List | Standard categories |
| B | Access_Type | 20 | Text | Description |
| C | Information_Classification | 15 | List | Public/Internal/Confidential/Restricted |
| D | Required_Template | 15 | List | From Template_Registry |
| E | Timing | 25 | Text | When required |
| F | Duration | 20 | Text | Agreement term |
| G | Post_Termination_Period | 20 | Text | Survival period |
| H | Mandatory | 12 | List | Yes/No/Conditional |
| I | Conditions | 40 | Text | If conditional |

### Sheet 5: Clause_Library

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Clause_ID | 12 | Text | CL-### pattern |
| B | Clause_Name | 35 | Text | Descriptive name |
| C | Clause_Category | 20 | List | See dropdown |
| D | Clause_Purpose | 40 | Text | Description |
| E | Standard_Text | 80 | Text | Approved wording |
| F | Mandatory | 15 | List | Yes/No/Recommended |
| G | Applicable_Templates | 30 | Text | Template IDs |
| H | Last_Reviewed | 12 | Date | DD.MM.YYYY |

### Sheet 6: Evidence_Register

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Evidence_ID | 20 | Text | EVD-A.6.6.1-### |
| B | Evidence_Description | 50 | Text | What it demonstrates |
| C | Evidence_Type | 20 | List | See dropdown |
| D | Storage_Location | 50 | Text | Path/URL |
| E | Collection_Date | 12 | Date | DD.MM.YYYY |
| F | Collected_By | 25 | Text | Name |

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
| 10 | Legal Counsel | | |
| 11 | Information Security Manager | | |
| 12 | | | |
| 13 | **Approval Status** | | |
| 14 | Status | [Approved/Pending/Rejected] | |
| 15 | Comments | [Input field spanning columns] | |

---

## 2.3 Data Validations

### Template_Type Dropdown

```python
TEMPLATE_TYPE_LIST = [
    "Standard NDA",
    "Mutual NDA",
    "One-Way NDA (Disclosing)",
    "One-Way NDA (Receiving)",
    "Employment Confidentiality",
    "Contractor Agreement",
    "Vendor Agreement",
    "Customer Agreement",
    "Partner Agreement",
    "Investor NDA",
    "Visitor Acknowledgement",
    "Board Member Agreement",
    "Intern Agreement",
    "Research NDA"
]
```

### Stakeholder_Category Dropdown

```python
STAKEHOLDER_CATEGORY_LIST = [
    "Employees",
    "Contractors",
    "Consultants",
    "Vendors",
    "Suppliers",
    "Partners",
    "Customers",
    "Board Members",
    "Investors",
    "Visitors",
    "Interns",
    "Candidates",
    "Researchers",
    "Subcontractors",
    "Auditors"
]
```

### Status Dropdown

```python
STATUS_LIST = [
    "Active",
    "Draft",
    "Under Review",
    "Superseded",
    "Archived"
]
```

### Legal_Approved Dropdown

```python
LEGAL_APPROVED_LIST = [
    "Yes",
    "No",
    "Pending"
]
```

### Information_Classification Dropdown

```python
CLASSIFICATION_LIST = [
    "Public",
    "Internal",
    "Confidential",
    "Restricted"
]
```

### Clause_Category Dropdown

```python
CLAUSE_CATEGORY_LIST = [
    "Definitions",
    "Scope",
    "Obligations",
    "Exceptions",
    "Term and Duration",
    "Termination",
    "Return of Information",
    "Remedies",
    "Intellectual Property",
    "Data Protection",
    "Jurisdiction",
    "General Provisions"
]
```

### Mandatory Dropdown

```python
MANDATORY_LIST = [
    "Yes",
    "No",
    "Recommended",
    "Conditional"
]
```

### Evidence_Type Dropdown

```python
EVIDENCE_TYPE_LIST = [
    "Template Document",
    "Legal Review Record",
    "Approval Email",
    "Meeting Minutes",
    "Version History Log",
    "Sign-Off Form",
    "Other"
]
```

---

## 2.4 Conditional Formatting

### Template_Registry Sheet

#### Legal Review Date Warning

**Condition:** Legal_Review_Date > 12 months ago
**Format:** Yellow fill (#FFEB9C), Red text (#9C0006)
**Purpose:** Highlight templates requiring legal review

```python
# Rule configuration
rule_legal_review = FormulaRule(
    formula=['=G2<TODAY()-365'],
    fill=PatternFill(start_color='FFEB9C', end_color='FFEB9C', fill_type='solid'),
    font=Font(color='9C0006')
)
```

#### Status Formatting

| Status | Fill Colour | Font Colour |
|--------|-------------|-------------|
| Active | Light Green (#C6EFCE) | Dark Green (#006100) |
| Draft | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Under Review | Light Blue (#BDD7EE) | Dark Blue (#1F4E79) |
| Superseded | Light Grey (#D9D9D9) | Dark Grey (#595959) |
| Archived | Light Red (#FFC7CE) | Dark Red (#9C0006) |

### Template_Versions Sheet

#### Legal Approval Status

| Value | Fill Colour | Font Colour |
|-------|-------------|-------------|
| Yes | Light Green (#C6EFCE) | Dark Green (#006100) |
| No | Light Red (#FFC7CE) | Dark Red (#9C0006) |
| Pending | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |

### Applicability_Matrix Sheet

#### Mandatory Formatting

| Value | Fill Colour | Font Colour |
|-------|-------------|-------------|
| Yes | Light Green (#C6EFCE) | Dark Green (#006100) |
| No | Light Grey (#D9D9D9) | Dark Grey (#595959) |
| Conditional | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |

---

## 2.5 Formula Specifications

### Template_Registry Calculated Fields

#### Days Since Legal Review

```excel
=DATEDIF(G2, TODAY(), "d")
```
*Calculates days since last legal review*

#### Review Overdue Flag

```excel
=IF(G2<TODAY()-365, "OVERDUE", "Current")
```
*Flags templates with overdue legal review*

### Template_Versions Calculated Fields

#### Days Since Version

```excel
=DATEDIF(C2, TODAY(), "d")
```
*Calculates days since version was created*

### Dashboard Formulas (if implemented)

#### Total Active Templates

```excel
=COUNTIF(Template_Registry!L:L, "Active")
```

#### Templates Requiring Review

```excel
=COUNTIFS(Template_Registry!L:L, "Active", Template_Registry!G:G, "<" & TODAY()-365)
```

#### Average Version Count

```excel
=COUNTROWS(Template_Versions!A:A) / COUNTIF(Template_Registry!L:L, "Active")
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
| Success/Active | Light Green | #C6EFCE | 198, 239, 206 |
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
| **Script Name** | `generate_a66_1_nda_template_registry.py` |
| **Location** | `10-isms-scr-base/isms-a.6.6-confidentiality-nda/10_generator-master/` |
| **Language** | Python 3.8+ |
| **Dependencies** | openpyxl, logging, datetime |

### Script Structure

```python
# =============================================================================
# ISMS-IMP-A.6.6.1 NDA Template Registry and Inventory
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
| `create_template_registry_sheet()` | Generates Template_Registry sheet |
| `create_template_versions_sheet()` | Generates Template_Versions sheet |
| `create_applicability_matrix_sheet()` | Generates Applicability_Matrix sheet |
| `create_clause_library_sheet()` | Generates Clause_Library sheet |
| `create_evidence_register_sheet()` | Generates Evidence_Register sheet |
| `create_approval_signoff_sheet()` | Generates Approval_SignOff sheet |
| `apply_conditional_formatting()` | Applies conditional formatting rules |
| `apply_data_validations()` | Applies dropdown validations |
| `generate_workbook()` | Main orchestration function |

### Output Location

```
10-isms-scr-base/
└── isms-a.6.6-confidentiality-nda/
    └── 90_workbooks/
        └── ISMS-IMP-A.6.6.1_NDA_Template_Registry_and_Inventory_YYYYMMDD.xlsx
```

### Execution

```bash
cd 10-isms-scr-base/isms-a.6.6-confidentiality-nda/10_generator-master
python3 generate_a66_1_nda_template_registry.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"The only real security that a man can have in this world is a reserve of knowledge, experience, and ability."*
— Henry Ford

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-02-06 -->
