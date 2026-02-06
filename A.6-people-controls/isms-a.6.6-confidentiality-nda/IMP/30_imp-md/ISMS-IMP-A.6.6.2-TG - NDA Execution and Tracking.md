**ISMS-IMP-A.6.6.2-TG - NDA Execution and Tracking**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.6

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.6.2-TG |
| **Title** | NDA Execution and Tracking |
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
   - [1.4 NDA Execution Process](#14-nda-execution-process)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 Signatory Management](#17-signatory-management)
   - [1.8 Expiration and Renewal Management](#18-expiration-and-renewal-management)
   - [1.9 Evidence Collection](#19-evidence-collection)
   - [1.10 Common Pitfalls](#110-common-pitfalls)
   - [1.11 Quality Checklist](#111-quality-checklist)
   - [1.12 Review and Approval](#112-review-and-approval)
   - [1.13 Integration with HR and Procurement](#113-integration-with-hr-and-procurement)
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
| **Filename** | `ISMS-IMP-A.6.6.2_NDA_Execution_and_Tracking_YYYYMMDD.xlsx` |
| **Format** | Microsoft Excel Open XML (.xlsx) |
| **Sheets** | 7 |
| **Protected** | Yes (structure and formatting) |
| **Password** | [Organisation standard] |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 2 |
| 2 | Active_NDAs | Executed NDA registry | 200+ | 18 |
| 3 | Signatory_Register | Individual tracking | 500+ | 15 |
| 4 | Expiration_Monitor | Expiry tracking | 200+ | 9 |
| 5 | Renewal_Tracking | Renewal workflow | 50+ | 14 |
| 6 | Evidence_Register | Evidence tracking | 100+ | 6 |
| 7 | Approval_SignOff | Authorisation | 15 | 3 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

#### Layout

| Row | Column A | Column B |
|-----|----------|----------|
| 1 | **ISMS-IMP-A.6.6.2** | |
| 2 | **NDA Execution and Tracking** | |
| 3 | | |
| 4 | **Document Information** | |
| 5 | Control Reference | ISO/IEC 27001:2022 A.6.6 |
| 6 | Document ID | ISMS-IMP-A.6.6.2 |
| 7 | Generated Date | [Date] |
| 8 | Version | 1.0 |

### Sheet 2: Active_NDAs

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | NDA_ID | 20 | Text | NDA-EXE-YYYY-XXXX |
| B | Template_Ref | 15 | List | From Template Registry |
| C | NDA_Title | 50 | Text | Descriptive |
| D | Counterparty_Name | 35 | Text | Legal name |
| E | Counterparty_Type | 15 | List | See dropdown |
| F | Execution_Date | 12 | Date | DD.MM.YYYY |
| G | Effective_Date | 12 | Date | DD.MM.YYYY |
| H | Expiration_Date | 15 | Date/Text | DD.MM.YYYY or Indefinite |
| I | Term_Years | 10 | Number/Text | Number or Indefinite |
| J | Post_Term_Period | 15 | Number/Text | Years |
| K | Post_Term_Expiry | 15 | Date | Calculated |
| L | Signatories_Count | 12 | Number | Count |
| M | Our_Signatory | 30 | Text | Name and title |
| N | Storage_Location | 50 | Text | Path |
| O | Status | 15 | List | See dropdown |
| P | Renewal_Required | 10 | List | Yes/No/TBD |
| Q | Renewal_Owner | 25 | Text | Name/Dept |
| R | Comments | 50 | Text | Notes |

### Sheet 3: Signatory_Register

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Signatory_ID | 18 | Text | SIG-YYYY-XXXXX |
| B | NDA_Ref | 20 | List | From Active_NDAs |
| C | Signatory_Name | 30 | Text | Full name |
| D | Signatory_Type | 20 | List | See dropdown |
| E | Organisation | 30 | Text | Employer |
| F | Role_Title | 25 | Text | Job title |
| G | Department | 20 | Text | Dept name |
| H | Email | 35 | Text | Email |
| I | Signature_Date | 12 | Date | DD.MM.YYYY |
| J | Signature_Method | 15 | List | See dropdown |
| K | Relationship_Start | 15 | Date | DD.MM.YYYY |
| L | Relationship_End | 15 | Date | DD.MM.YYYY |
| M | Access_Granted_Date | 15 | Date | DD.MM.YYYY |
| N | Status | 15 | List | See dropdown |
| O | Notes | 40 | Text | Comments |

### Sheet 4: Expiration_Monitor

#### Column Definitions

| Column | Header | Width | Type | Source |
|--------|--------|-------|------|--------|
| A | NDA_ID | 20 | Formula | Active_NDAs |
| B | Counterparty | 35 | Formula | Active_NDAs |
| C | Expiration_Date | 15 | Formula | Active_NDAs |
| D | Days_Until_Expiry | 15 | Formula | Calculated |
| E | Alert_Status | 15 | Formula | Conditional |
| F | Renewal_Required | 12 | Formula | Active_NDAs |
| G | Renewal_Owner | 25 | Formula | Active_NDAs |
| H | Renewal_Status | 15 | Formula | Renewal_Tracking |
| I | Action_Required | 40 | Manual | User input |

### Sheet 5: Renewal_Tracking

#### Column Definitions

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Renewal_ID | 18 | Text | RNW-YYYY-XXXX |
| B | Original_NDA | 20 | List | From Active_NDAs |
| C | Counterparty | 35 | Formula | From Active_NDAs |
| D | Original_Expiry | 15 | Formula | From Active_NDAs |
| E | Renewal_Initiated | 12 | Date | DD.MM.YYYY |
| F | Initiated_By | 25 | Text | Name |
| G | New_Terms_Required | 12 | List | Yes/No |
| H | Legal_Review_Status | 15 | List | See dropdown |
| I | Counterparty_Agreed | 15 | List | See dropdown |
| J | New_NDA_ID | 20 | List | From Active_NDAs |
| K | New_Expiry | 12 | Date | DD.MM.YYYY |
| L | Renewal_Completed | 12 | Date | DD.MM.YYYY |
| M | Status | 20 | List | See dropdown |
| N | Notes | 50 | Text | Progress notes |

---

## 2.3 Data Validations

### Counterparty_Type Dropdown

```python
COUNTERPARTY_TYPE_LIST = [
    "Employee",
    "Contractor",
    "Consultant",
    "Vendor",
    "Supplier",
    "Partner",
    "Customer",
    "Board Member",
    "Investor",
    "Visitor",
    "Candidate",
    "Other"
]
```

### NDA_Status Dropdown

```python
NDA_STATUS_LIST = [
    "Active",
    "Expired",
    "Terminated",
    "Renewed",
    "Superseded",
    "Post-Term",
    "Fully Expired"
]
```

### Signatory_Type Dropdown

```python
SIGNATORY_TYPE_LIST = [
    "Employee",
    "Contractor",
    "Consultant",
    "Vendor Representative",
    "Partner Representative",
    "Customer Representative",
    "Board Member",
    "Investor",
    "Visitor",
    "Witness",
    "Authorised Signatory (Our Org)",
    "Other"
]
```

### Signature_Method Dropdown

```python
SIGNATURE_METHOD_LIST = [
    "Wet Signature",
    "Digital Signature",
    "DocuSign",
    "Adobe Sign",
    "Other E-Signature",
    "Click-to-Accept"
]
```

### Signatory_Status Dropdown

```python
SIGNATORY_STATUS_LIST = [
    "Active",
    "Terminated",
    "Post-Term Expired",
    "Suspended"
]
```

### Alert_Status Dropdown

```python
ALERT_STATUS_LIST = [
    "Green (>90 days)",
    "Amber (30-90 days)",
    "Red (<30 days)",
    "Expired"
]
```

### Legal_Review_Status Dropdown

```python
LEGAL_REVIEW_STATUS_LIST = [
    "Not Required",
    "Pending",
    "In Progress",
    "Completed",
    "N/A"
]
```

### Renewal_Status Dropdown

```python
RENEWAL_STATUS_LIST = [
    "Not Started",
    "In Progress",
    "Legal Review",
    "Awaiting Counterparty",
    "Awaiting Signature",
    "Completed",
    "Cancelled - No Longer Required",
    "Failed - Counterparty Declined"
]
```

---

## 2.4 Conditional Formatting

### Active_NDAs Sheet

#### Status Formatting

| Status | Fill Colour | Font Colour |
|--------|-------------|-------------|
| Active | Light Green (#C6EFCE) | Dark Green (#006100) |
| Expired | Light Red (#FFC7CE) | Dark Red (#9C0006) |
| Terminated | Light Grey (#D9D9D9) | Dark Grey (#595959) |
| Renewed | Light Blue (#BDD7EE) | Dark Blue (#1F4E79) |
| Post-Term | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |

### Signatory_Register Sheet

#### Status Formatting

| Status | Fill Colour | Font Colour |
|--------|-------------|-------------|
| Active | Light Green (#C6EFCE) | Dark Green (#006100) |
| Terminated | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Post-Term Expired | Light Grey (#D9D9D9) | Dark Grey (#595959) |
| Suspended | Light Red (#FFC7CE) | Dark Red (#9C0006) |

### Expiration_Monitor Sheet

#### Alert Status Formatting

| Alert | Fill Colour | Font Colour |
|-------|-------------|-------------|
| Green | Light Green (#C6EFCE) | Dark Green (#006100) |
| Amber | Light Yellow (#FFEB9C) | Dark Orange (#9C5700) |
| Red | Light Orange (#FABF8F) | Dark Red (#9C0006) |
| Expired | Light Red (#FFC7CE) | White (#FFFFFF) |

---

## 2.5 Formula Specifications

### Expiration_Monitor Formulas

#### Days Until Expiry

```excel
=IF(C2="Indefinite", "N/A", C2-TODAY())
```

#### Alert Status

```excel
=IF(D2="N/A", "N/A",
 IF(D2<0, "Expired",
 IF(D2<30, "Red (<30 days)",
 IF(D2<90, "Amber (30-90 days)",
 "Green (>90 days)"))))
```

### Active_NDAs Formulas

#### Post-Term Expiry Calculation

```excel
=IF(OR(H2="Indefinite", J2="Indefinite"), "See Terms",
 IF(ISNUMBER(H2), DATE(YEAR(H2)+J2, MONTH(H2), DAY(H2)), ""))
```

### Dashboard Metrics (if implemented)

#### Total Active NDAs

```excel
=COUNTIF(Active_NDAs!O:O, "Active")
```

#### Total Active Signatories

```excel
=COUNTIF(Signatory_Register!N:N, "Active")
```

#### NDAs Expiring in 90 Days

```excel
=COUNTIFS(Active_NDAs!O:O, "Active", Active_NDAs!H:H, "<="&TODAY()+90, Active_NDAs!H:H, ">"&TODAY())
```

---

## 2.6 Cell Styling Standards

### Colour Palette

| Purpose | Colour Name | Hex Code |
|---------|-------------|----------|
| Header Background | Theme Blue | #2E75B6 |
| Header Text | White | #FFFFFF |
| Alternate Row | Light Grey | #F2F2F2 |
| Input Field | Light Yellow | #FFFFCC |
| Success/Active | Light Green | #C6EFCE |
| Warning | Light Yellow | #FFEB9C |
| Error/Alert | Light Red | #FFC7CE |

### Font Standards

| Element | Font | Size | Weight |
|---------|------|------|--------|
| Sheet Title | Calibri | 16 | Bold |
| Column Header | Calibri | 11 | Bold |
| Data Cell | Calibri | 10 | Normal |

---

## 2.7 Generator Script Reference

### Script Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a66_2_nda_execution_tracking.py` |
| **Location** | `10-isms-scr-base/isms-a.6.6-confidentiality-nda/10_generator-master/` |
| **Language** | Python 3.8+ |
| **Dependencies** | openpyxl, logging, datetime |

### Key Functions

| Function | Purpose |
|----------|---------|
| `create_instructions_sheet()` | Generates Instructions sheet |
| `create_active_ndas_sheet()` | Generates Active_NDAs sheet |
| `create_signatory_register_sheet()` | Generates Signatory_Register sheet |
| `create_expiration_monitor_sheet()` | Generates Expiration_Monitor sheet |
| `create_renewal_tracking_sheet()` | Generates Renewal_Tracking sheet |
| `create_evidence_register_sheet()` | Generates Evidence_Register sheet |
| `create_approval_signoff_sheet()` | Generates Approval_SignOff sheet |
| `apply_conditional_formatting()` | Applies formatting rules |
| `apply_data_validations()` | Applies dropdown validations |
| `generate_workbook()` | Main orchestration function |

### Output Location

```
10-isms-scr-base/
└── isms-a.6.6-confidentiality-nda/
    └── 90_workbooks/
        └── ISMS-IMP-A.6.6.2_NDA_Execution_and_Tracking_YYYYMMDD.xlsx
```

### Execution

```bash
cd 10-isms-scr-base/isms-a.6.6-confidentiality-nda/10_generator-master
python3 generate_a66_2_nda_execution_tracking.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"A verbal contract isn't worth the paper it's written on."*
— Samuel Goldwyn

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-02-06 -->
