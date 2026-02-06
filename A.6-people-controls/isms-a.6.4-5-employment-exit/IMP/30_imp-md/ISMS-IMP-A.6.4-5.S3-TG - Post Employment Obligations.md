**ISMS-IMP-A.6.4-5.S3-TG - Post-Employment Obligations**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.4, A.6.5

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.4-5.S3-TG |
| **Title** | Post-Employment Obligations |
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
   - [1.4 Obligation Types](#14-obligation-types)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 NDA Tracking Framework](#17-nda-tracking-framework)
   - [1.8 Enforcement Procedures](#18-enforcement-procedures)
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
| **Filename** | `ISMS-IMP-A.6.4-5.S3_Post_Employment_Obligations_YYYYMMDD.xlsx` |
| **Format** | Microsoft Excel Open XML (.xlsx) |
| **Sheets** | 9 |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows | Columns |
|-------------|------------|---------|------|---------|
| 1 | Instructions | Guidance | 50 | 2 |
| 2 | Obligation_Types | Obligation definitions | 20 | 7 |
| 3 | Former_Personnel | Personnel registry | 500+ | 9 |
| 4 | Active_Obligations | Active tracking | 1000+ | 8 |
| 5 | Expiration_Tracker | Expiration monitoring | 100+ | 8 |
| 6 | Acknowledgement_Log | Exit acknowledgements | 500+ | 8 |
| 7 | Enforcement_Register | Enforcement records | 50+ | 9 |
| 8 | Evidence_Register | Evidence tracking | 50+ | 6 |
| 9 | Approval_SignOff | Authorisation | 15 | 3 |

---

## 2.2 Sheet Specifications

### Sheet 2: Obligation_Types

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Obligation_ID | 14 | Text |
| B | Obligation_Type | 20 | List |
| C | Description | 50 | Text |
| D | Standard_Duration | 20 | Text |
| E | Source_Document | 30 | Text |
| F | Applicable_To | 25 | List |
| G | Enforceability_Notes | 45 | Text |

### Sheet 3: Former_Personnel

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Person_ID | 16 | Text |
| B | Name | 30 | Text |
| C | Exit_Date | 14 | Date |
| D | Exit_Type | 20 | List |
| E | Position_Held | 30 | Text |
| F | Access_Level | 16 | List |
| G | NDA_Reference | 20 | Text |
| H | Obligations_End_Date | 14 | Date |
| I | Status | 18 | List |

### Sheet 4: Active_Obligations

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Obligation_Ref | 18 | Text |
| B | Person_ID | 16 | List |
| C | Obligation_Type | 20 | List |
| D | Start_Date | 14 | Date |
| E | End_Date | 14 | Date/Text |
| F | Specific_Terms | 40 | Text |
| G | Monitoring_Required | 18 | List |
| H | Status | 18 | List |

### Sheet 5: Expiration_Tracker

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Obligation_Ref | 18 | List |
| B | Person_Name | 30 | Text |
| C | Obligation_Type | 20 | Text |
| D | Expiration_Date | 14 | Date |
| E | Days_Until_Expiry | 16 | Formula |
| F | Status | 20 | List |
| G | Action_Required | 35 | Text |
| H | Action_Taken | 35 | Text |

---

## 2.3 Data Validations

### Obligation_Type Dropdown

```python
OBLIGATION_TYPE_LIST = [
    "Confidentiality",
    "Trade Secrets",
    "IP Assignment",
    "Non-Compete",
    "Non-Solicitation (Employee)",
    "Non-Solicitation (Customer)",
    "Data Return"
]
```

### Exit_Type Dropdown

```python
EXIT_TYPE_LIST = [
    "Voluntary Resignation",
    "Involuntary Termination",
    "Contract End",
    "Retirement",
    "Role Change"
]
```

### Access_Level Dropdown

```python
ACCESS_LEVEL_LIST = [
    "Standard",
    "Elevated",
    "Privileged",
    "Executive"
]
```

### Obligation_Status Dropdown

```python
OBLIGATION_STATUS_LIST = [
    "Active",
    "Expired",
    "Waived",
    "Under Enforcement"
]
```

### Personnel_Status Dropdown

```python
PERSONNEL_STATUS_LIST = [
    "Active Obligations",
    "All Expired",
    "Under Enforcement"
]
```

### Expiration_Status Dropdown

```python
EXPIRATION_STATUS_LIST = [
    "Expiring Soon",
    "Expired",
    "Acknowledged",
    "Extended"
]
```

### Enforcement_Status Dropdown

```python
ENFORCEMENT_STATUS_LIST = [
    "Under Investigation",
    "Cease and Desist Sent",
    "Legal Action Initiated",
    "Resolved",
    "No Action Required"
]
```

### Monitoring_Required Dropdown

```python
MONITORING_REQUIRED_LIST = [
    "Yes",
    "No",
    "Periodic"
]
```

### Acknowledgement_Type Dropdown

```python
ACKNOWLEDGEMENT_TYPE_LIST = [
    "Exit Interview",
    "Written Acknowledgement",
    "Email Confirmation",
    "Refused"
]
```

---

## 2.4 Conditional Formatting

### Active_Obligations Sheet

#### Status Formatting

| Value | Fill Colour |
|-------|-------------|
| Active | Light Green (#C6EFCE) |
| Expired | Light Grey (#D9D9D9) |
| Under Enforcement | Light Red (#FFC7CE) |
| Waived | Light Blue (#BDD7EE) |

### Expiration_Tracker Sheet

#### Days Until Expiry Formatting

| Condition | Fill Colour |
|-----------|-------------|
| < 0 (Expired) | Light Red (#FFC7CE) |
| 0-30 days | Light Orange (#FCE4D6) |
| 31-90 days | Light Yellow (#FFEB9C) |
| > 90 days | Light Green (#C6EFCE) |

### Enforcement_Register Sheet

#### Status Formatting

| Value | Fill Colour |
|-------|-------------|
| Under Investigation | Light Yellow (#FFEB9C) |
| Cease and Desist Sent | Light Orange (#FCE4D6) |
| Legal Action Initiated | Light Red (#FFC7CE) |
| Resolved | Light Green (#C6EFCE) |

---

## 2.5 Formula Specifications

### Expiration_Tracker Calculated Fields

#### Days Until Expiry

```excel
=IF(D2="Indefinite", "N/A", D2-TODAY())
```

#### Status Auto-Calculate

```excel
=IF(E2="N/A", "Indefinite", IF(E2<0, "Expired", IF(E2<=90, "Expiring Soon", "Active")))
```

### Former_Personnel Summary

#### Count Active Obligations

```excel
=COUNTIF(Former_Personnel!I:I, "Active Obligations")
```

#### Count Under Enforcement

```excel
=COUNTIF(Former_Personnel!I:I, "Under Enforcement")
```

---

## 2.6 Cell Styling Standards

Standard styling as per ISMS framework.

---

## 2.7 Generator Script Reference

### Script Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a645_3_post_employment.py` |
| **Location** | `10-isms-scr-base/isms-a.6.4-5-employment-exit/10_generator-master/` |
| **Language** | Python 3.8+ |
| **Dependencies** | openpyxl, logging, datetime |

### Execution

```bash
cd 10-isms-scr-base/isms-a.6.4-5-employment-exit/10_generator-master
python3 generate_a645_3_post_employment.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Russian Proverb

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-02-06 -->
