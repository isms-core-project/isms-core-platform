**ISMS-IMP-A.6.4-5.S2-TG - Employment Exit Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.4, A.6.5

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.4-5.S2-TG |
| **Title** | Employment Exit Assessment |
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
   - [1.4 Exit Scenarios](#14-exit-scenarios)
   - [1.5 Workbook Structure](#15-workbook-structure)
   - [1.6 Completion Walkthrough](#16-completion-walkthrough)
   - [1.7 Access Revocation Framework](#17-access-revocation-framework)
   - [1.8 Asset Recovery Process](#18-asset-recovery-process)
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
| **Filename** | `ISMS-IMP-A.6.4-5.S2_Employment_Exit_Assessment_YYYYMMDD.xlsx` |
| **Format** | Microsoft Excel Open XML (.xlsx) |
| **Sheets** | 8 |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows | Columns |
|-------------|------------|---------|------|---------|
| 1 | Instructions | Guidance | 50 | 2 |
| 2 | Exit_Procedures | Exit process by type | 20 | 8 |
| 3 | Access_Revocation | Revocation requirements | 30 | 8 |
| 4 | Asset_Recovery | Asset return tracking | 30 | 7 |
| 5 | Exit_Tracker | Individual exit tracking | 200+ | 10 |
| 6 | Leaver_Reconciliation | Monthly reconciliation | 24+ | 8 |
| 7 | Evidence_Register | Evidence tracking | 50+ | 6 |
| 8 | Approval_SignOff | Authorisation | 15 | 3 |

---

## 2.2 Sheet Specifications

### Sheet 2: Exit_Procedures

#### Column Definitions

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Exit_Type | 25 | List |
| B | Notification_Trigger | 35 | Text |
| C | HR_Actions | 40 | Text |
| D | IT_Actions | 40 | Text |
| E | Manager_Actions | 40 | Text |
| F | Security_Actions | 35 | Text |
| G | Timeline | 25 | Text |
| H | Documentation_Required | 35 | Text |

### Sheet 3: Access_Revocation

#### Column Definitions

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Access_Type | 22 | List |
| B | System_Examples | 35 | Text |
| C | Revocation_Method | 40 | Text |
| D | Timeline_Standard | 20 | Text |
| E | Timeline_Immediate | 20 | Text |
| F | Verification_Method | 35 | Text |
| G | Responsible_Party | 20 | Text |
| H | Dependencies | 35 | Text |

### Sheet 5: Exit_Tracker

#### Column Definitions

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Exit_ID | 18 | Text |
| B | Employee_ID | 15 | Text |
| C | Exit_Type | 22 | List |
| D | Last_Working_Day | 14 | Date |
| E | Access_Revoked_Date | 14 | Date |
| F | Assets_Returned_Date | 14 | Date |
| G | Exit_Interview_Date | 14 | Date |
| H | Checklist_Complete | 15 | List |
| I | Status | 18 | List |
| J | Notes | 40 | Text |

---

## 2.3 Data Validations

### Exit_Type Dropdown

```python
EXIT_TYPE_LIST = [
    "Voluntary Resignation",
    "Involuntary Termination",
    "Immediate Dismissal",
    "Retirement",
    "Contract End",
    "Role Change"
]
```

### Access_Type Dropdown

```python
ACCESS_TYPE_LIST = [
    "Physical Access",
    "AD/Directory",
    "Email",
    "VPN",
    "Applications",
    "Cloud Services",
    "Third-Party Systems",
    "Shared Accounts",
    "API Keys",
    "Privileged Access"
]
```

### Exit_Status Dropdown

```python
EXIT_STATUS_LIST = [
    "Initiated",
    "In Progress",
    "Pending Asset Return",
    "Pending Verification",
    "Complete",
    "Issues Outstanding"
]
```

### Checklist_Complete Dropdown

```python
CHECKLIST_COMPLETE_LIST = [
    "Yes",
    "Partial",
    "No"
]
```

---

## 2.4 Conditional Formatting

### Exit_Tracker Sheet

#### Status Formatting

| Value | Fill Colour |
|-------|-------------|
| Initiated | Light Blue (#BDD7EE) |
| In Progress | Light Yellow (#FFEB9C) |
| Pending Asset Return | Light Orange (#FCE4D6) |
| Complete | Light Green (#C6EFCE) |
| Issues Outstanding | Light Red (#FFC7CE) |

#### Overdue Highlighting

**Condition:** Last_Working_Day < TODAY() AND Status <> "Complete"
**Format:** Red border, yellow fill

---

## 2.5 Formula Specifications

### Exit_Tracker Calculated Fields

#### Days Since Exit

```excel
=IF(D2<>"", TODAY()-D2, "")
```

#### SLA Breach Flag

```excel
=IF(AND(E2="", D2<TODAY()), "ACCESS OVERDUE", "")
```

### Leaver_Reconciliation Calculated Fields

#### Discrepancy Count

```excel
=B2-C2
```

#### Compliance Rate

```excel
=IF(B2>0, C2/B2*100, "N/A")
```

---

## 2.6 Cell Styling Standards

Standard styling as per ISMS framework - see Section 2.6 of ISMS-IMP-A.6.4-5.S1.

---

## 2.7 Generator Script Reference

### Script Information

| Attribute | Value |
|-----------|-------|
| **Script Name** | `generate_a645_2_employment_exit.py` |
| **Location** | `10-isms-scr-base/isms-a.6.4-5-employment-exit/10_generator-master/` |
| **Language** | Python 3.8+ |
| **Dependencies** | openpyxl, logging, datetime |

### Execution

```bash
cd 10-isms-scr-base/isms-a.6.4-5-employment-exit/10_generator-master
python3 generate_a645_2_employment_exit.py
mv *.xlsx ../90_workbooks/
```

---

**END OF SPECIFICATION**

---

*"The way to get started is to quit talking and begin doing."*
— Walt Disney

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-02-06 -->
