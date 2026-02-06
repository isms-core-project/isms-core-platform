**ISMS-IMP-A.5.3.3-TG - Role-Function Mapping**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.3: Policies for Segregation of Duties

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.3.3-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.3 Segregation of Duties |
| **Parent Policy** | ISMS-POL-A.5.3 - Segregation of Duties |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

## Table of Contents

1. [PART I: USER COMPLETION GUIDE](#part-i-user-completion-guide)
   - [1.1 Assessment Overview](#11-assessment-overview)
   - [1.2 Control Requirements](#12-control-requirements)
   - [1.3 Prerequisites](#13-prerequisites)
   - [1.4 Workbook Structure](#14-workbook-structure)
   - [1.5 Completion Walkthrough](#15-completion-walkthrough)
   - [1.6 Function-Level Conflict Analysis](#16-function-level-conflict-analysis)
   - [1.7 Evidence Collection](#17-evidence-collection)
   - [1.8 Common Pitfalls](#18-common-pitfalls)
   - [1.9 Quality Checklist](#19-quality-checklist)
   - [1.10 Review and Approval](#110-review-and-approval)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Technical Details](#21-workbook-technical-details)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Conditional Formatting](#23-conditional-formatting)
   - [2.4 Formulas](#24-formulas)
   - [2.5 Integration Points](#25-integration-points)
   - [2.6 Related Documents](#26-related-documents)

---

# Technical Specification

---

## 2.1 Workbook Technical Details

### File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.3.3_Role_Function_Mapping_YYYYMMDD.xlsx` |
| Generator | `generate_a53_3_role_function_mapping.py` |
| Sheets | 9 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 8 |
| 2 | Business_Roles | Org roles | 100+ | 8 |
| 3 | Application_Roles | System roles | 200+ | 8 |
| 4 | Functions | Capabilities | 300+ | 8 |
| 5 | Permissions | Technical | 500+ | 8 |
| 6 | Role_Function_Map | Mappings | 1000+ | 8 |
| 7 | Function_Conflicts | Conflicts | 100+ | 7 |
| 8 | Validation_Status | Validation | 200+ | 9 |
| 9 | Change_Log | History | 500+ | 8 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

| Row | Content | Purpose |
|-----|---------|---------|
| 1 | Title (merged A1:H1) | Document identification |
| 3-10 | Document Information table | Metadata reference |
| 12-35 | Methodology overview | Guidance for mapping |
| 37-50 | Function categories | Classification reference |

### Sheet 2: Business_Roles

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Business_Role_ID | 18 | Text | None |
| B | Role_Name | 30 | Text | None |
| C | Department | 20 | Text | Dropdown |
| D | Process_Domain | 20 | List | Financial, IT Operations, HR, Procurement, Security, Change Management, Other |
| E | Role_Owner | 25 | Text | None |
| F | Description | 50 | Text | None |
| G | Risk_Level | 12 | List | Critical, High, Medium, Low |
| H | Last_Reviewed | 15 | Date | None |

### Sheet 3: Application_Roles

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | App_Role_ID | 18 | Text | None |
| B | Application | 20 | Text | None |
| C | Role_Name | 30 | Text | None |
| D | Role_Type | 15 | List | Composite, Single, Derived |
| E | Description | 40 | Text | None |
| F | Business_Roles | 35 | Text | Comma-separated |
| G | Criticality | 12 | List | Critical, High, Medium, Low |
| H | Review_Frequency | 15 | List | Monthly, Quarterly, Semi-Annual, Annual |

### Sheet 4: Functions

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Function_ID | 18 | Text | None |
| B | Function_Name | 30 | Text | None |
| C | Category | 12 | List | Create, Read, Update, Delete, Approve, Execute, Admin |
| D | Application | 20 | Text | None |
| E | Process | 25 | Text | None |
| F | Description | 45 | Text | None |
| G | Risk_Level | 12 | List | Critical, High, Medium, Low |
| H | SoD_Sensitive | 12 | List | Yes, No |

### Sheet 5: Permissions

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Permission_ID | 18 | Text | None |
| B | Function_ID | 18 | Text | None |
| C | Application | 20 | Text | None |
| D | Permission_Name | 25 | Text | None |
| E | Permission_Type | 15 | List | Transaction, Report, API, Config, Data |
| F | Description | 40 | Text | None |
| G | Data_Scope | 25 | Text | None |
| H | Special_Conditions | 35 | Text | None |

### Sheet 6: Role_Function_Map

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Mapping_ID | 15 | Text | None |
| B | Business_Role_ID | 18 | Text | From Business_Roles |
| C | App_Role_ID | 18 | Text | From Application_Roles |
| D | Function_ID | 18 | Text | From Functions |
| E | Grant_Type | 12 | List | Direct, Inherited, Delegated, Emergency |
| F | Justification | 40 | Text | None |
| G | Effective_Date | 15 | Date | None |
| H | Expiry_Date | 15 | Date | None (blank = permanent) |

### Sheet 7: Function_Conflicts

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Conflict_ID | 15 | Text | None |
| B | Function_A | 18 | Text | From Functions |
| C | Function_B | 18 | Text | From Functions |
| D | Conflict_Type | 12 | List | X, C, M |
| E | Risk_Level | 12 | List | Critical, High, Medium, Low |
| F | Justification | 50 | Text | None |
| G | Mitigation | 40 | Text | None |

### Sheet 8: Validation_Status

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Validation_ID | 15 | Text | None |
| B | Role_ID | 18 | Text | None |
| C | Validation_Date | 15 | Date | None |
| D | Validator | 25 | Text | None |
| E | Documented_Functions | 20 | Number | >=0 |
| F | Actual_Functions | 18 | Number | >=0 |
| G | Discrepancies | 15 | Number | Formula |
| H | Status | 20 | List | Validated, Requires Investigation, Remediated, Deferred |
| I | Resolution | 40 | Text | None |

### Sheet 9: Change_Log

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Change_ID | 15 | Text | None |
| B | Change_Date | 15 | Date | None |
| C | Role_ID | 18 | Text | None |
| D | Change_Type | 15 | List | Permission Added, Permission Removed, Function Modified, Role Created, Role Deleted |
| E | Description | 50 | Text | None |
| F | Requested_By | 25 | Text | None |
| G | Approved_By | 25 | Text | None |
| H | Ticket_Reference | 20 | Text | None |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Business_Roles | G:G | ="Critical" | Red fill (#FFC7CE), Bold |
| Business_Roles | G:G | ="High" | Orange fill (#FABF8F) |
| Functions | G:G | ="Critical" | Red fill (#FFC7CE), Bold |
| Functions | G:G | ="High" | Orange fill (#FABF8F) |
| Functions | H:H | ="Yes" | Orange fill (#FABF8F) |
| Function_Conflicts | D:D | ="X" | Red fill (#FFC7CE), Bold |
| Function_Conflicts | D:D | ="C" | Orange fill (#FABF8F) |
| Function_Conflicts | D:D | ="M" | Yellow fill (#FFEB9C) |
| Validation_Status | H:H | ="Requires Investigation" | Red fill (#FFC7CE) |
| Validation_Status | H:H | ="Validated" | Green fill (#C6EFCE) |
| Validation_Status | H:H | ="Remediated" | Light green fill (#C6EFCE) |
| Validation_Status | H:H | ="Deferred" | Yellow fill (#FFEB9C) |
| Change_Log | D:D | ="Permission Added" | Light blue fill (#BDD7EE) |
| Change_Log | D:D | ="Permission Removed" | Light green fill (#C6EFCE) |

---

## 2.4 Formulas

**Discrepancies (Validation_Status, Column G):**
```
=ABS(E{row}-F{row})
```

**Validation Status Auto (Validation_Status, Column H):**
```
=IF(G{row}=0,"Validated",IF(G{row}>0,"Requires Investigation",""))
```

---

## 2.5 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| IAM/Directory | Role definitions, memberships | IAM -> Application_Roles |
| HR System | Business role assignments | HR -> Business_Roles |
| Application Admin | Role configurations | Apps -> Permissions |
| ISMS-IMP-A.5.3.1 | Conflict definitions | Bidirectional |
| ISMS-IMP-A.5.3.2 | Conflict analysis | This -> A.5.3.2 |
| Access Review | Certification support | This -> Access Review |

---

## 2.6 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.3 | Segregation of Duties | Parent policy |
| ISMS-IMP-A.5.3.1 | SoD Matrix Assessment | Role-level conflicts |
| ISMS-IMP-A.5.3.2 | Conflict Analysis | Detailed analysis |
| ISMS-IMP-A.5.3.4 | Compliance Dashboard | Reporting |
| ISMS-IMP-A.5.15-16-18 | IAM Assessment | Access management |

---

**END OF SPECIFICATION**

---

*"The devil is in the details."*
— Ludwig Mies van der Rohe

<!-- QA_VERIFIED: 2026-02-06 -->
