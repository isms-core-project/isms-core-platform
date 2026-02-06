**ISMS-IMP-A.5.3.1-TG - SoD Matrix Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.3: Policies for Segregation of Duties

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.3.1-TG |
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
   - [1.6 Evidence Collection](#16-evidence-collection)
   - [1.7 Common Pitfalls](#17-common-pitfalls)
   - [1.8 Quality Checklist](#18-quality-checklist)
   - [1.9 Review and Approval](#19-review-and-approval)
2. [PART II: TECHNICAL SPECIFICATION](#part-ii-technical-specification)
   - [2.1 Workbook Technical Details](#21-workbook-technical-details)
   - [2.2 Sheet Specifications](#22-sheet-specifications)
   - [2.3 Conditional Formatting](#23-conditional-formatting)
   - [2.4 Integration Points](#24-integration-points)
   - [2.5 Related Documents](#25-related-documents)

---

# Technical Specification

---

## 2.1 Workbook Technical Details

### File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.3.1_SoD_Matrix_Assessment_YYYYMMDD.xlsx` |
| Generator | `generate_a53_1_sod_matrix.py` |
| Sheets | 8 |
| Protected | No (input cells unlocked) |
| Format | Microsoft Excel Open XML (.xlsx) |

### Sheet Architecture

| Sheet Index | Sheet Name | Purpose | Rows (est.) | Columns |
|-------------|------------|---------|-------------|---------|
| 1 | Instructions | Guidance | 50 | 8 |
| 2 | Role_Inventory | Master catalogue | 200+ | 9 |
| 3 | Conflict_Matrix | Role conflicts | 200+ | Dynamic |
| 4 | Current_Assignments | Personnel assignments | 500+ | 9 |
| 5 | Gap_Analysis | Identified gaps | 100+ | 9 |
| 6 | Remediation_Tracker | Actions | 100+ | 9 |
| 7 | Exception_Register | Exceptions | 50+ | 10 |
| 8 | Approval_SignOff | Authorisation | 20 | 5 |

---

## 2.2 Sheet Specifications

### Sheet 1: Instructions

| Row | Content | Purpose |
|-----|---------|---------|
| 1 | Title (merged A1:H1) | Document identification |
| 3-10 | Document Information table | Metadata reference |
| 12-25 | Methodology overview | Guidance for assessors |
| 27-40 | Conflict classification reference | Quick reference |
| 42-50 | Evidence requirements | Audit preparation |

### Sheet 2: Role_Inventory

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Role_ID | 15 | Text | None |
| B | Role_Name | 30 | Text | None |
| C | Department | 20 | Text | Dropdown list |
| D | Process_Domain | 20 | List | Financial, IT Operations, HR, Procurement, Security, Change Management, Other |
| E | Risk_Level | 12 | List | Critical, High, Medium, Low |
| F | Description | 40 | Text | None |
| G | Key_Duties | 40 | Text | None |
| H | System_Access | 30 | Text | None |
| I | Active | 10 | List | Yes, No |

### Sheet 3: Conflict_Matrix

Dynamic matrix where:
- Row 1: Role IDs from Role_Inventory
- Column A: Role IDs from Role_Inventory
- Cells: Conflict classification (X, C, M, -)

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Role_ID | 15 | Text | Linked to Role_Inventory |
| B+ | [Dynamic Role IDs] | 12 | List | X, C, M, - |

### Sheet 4: Current_Assignments

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Person_ID | 12 | Text | None |
| B | Name | 25 | Text | None |
| C | Department | 20 | Text | Dropdown |
| D | Primary_Role | 30 | List | From Role_Inventory |
| E | Additional_Roles | 50 | Text | Comma-separated |
| F | Assignment_Date | 15 | Date | None |
| G | Last_Review | 15 | Date | None |
| H | Manager | 25 | Text | None |
| I | Notes | 30 | Text | None |

### Sheet 5: Gap_Analysis

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Gap_ID | 15 | Text | None |
| B | Person_ID | 12 | Text | None |
| C | Name | 25 | Text | None |
| D | Conflicting_Roles | 50 | Text | None |
| E | Conflict_Type | 12 | List | X, C, M |
| F | Risk_Level | 12 | List | Critical, High, Medium, Low |
| G | Identified_Date | 15 | Date | None |
| H | Status | 15 | List | Open, Mitigated, Resolved, Accepted |
| I | Notes | 40 | Text | None |

### Sheet 6: Remediation_Tracker

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Remediation_ID | 15 | Text | None |
| B | Gap_ID | 15 | Text | None |
| C | Action_Type | 18 | List | Role Removal, Role Reassignment, Process Redesign, Compensating Control |
| D | Description | 50 | Text | None |
| E | Owner | 25 | Text | None |
| F | Target_Date | 15 | Date | None |
| G | Status | 15 | List | Not Started, In Progress, Completed, Cancelled |
| H | Completion_Date | 15 | Date | None |
| I | Evidence_Ref | 30 | Text | None |

### Sheet 7: Exception_Register

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Exception_ID | 15 | Text | None |
| B | Gap_ID | 15 | Text | None |
| C | Justification | 50 | Text | None |
| D | Compensating_Controls | 60 | Text | None |
| E | Risk_Acceptance | 25 | Text | None |
| F | Approval_Date | 15 | Date | None |
| G | Expiry_Date | 15 | Date | None |
| H | Review_Frequency | 15 | List | Monthly, Quarterly, Semi-Annual, Annual |
| I | Last_Review | 15 | Date | None |
| J | Status | 12 | List | Active, Expired, Revoked |

### Sheet 8: Approval_SignOff

| Column | Header | Width | Type | Validation |
|:------:|--------|:-----:|------|------------|
| A | Role | 25 | Text | Pre-populated |
| B | Name | 25 | Text | Input |
| C | Date | 15 | Date | Input |
| D | Signature | 20 | Text | Input |
| E | Comments | 50 | Text | Input |

---

## 2.3 Conditional Formatting

| Sheet | Range | Condition | Format |
|-------|-------|-----------|--------|
| Conflict_Matrix | Data cells | ="X" | Red fill (#FFC7CE), Bold |
| Conflict_Matrix | Data cells | ="C" | Orange fill (#FABF8F) |
| Conflict_Matrix | Data cells | ="M" | Yellow fill (#FFEB9C) |
| Gap_Analysis | F:F | ="Critical" | Red fill (#FFC7CE), Bold |
| Gap_Analysis | F:F | ="High" | Orange fill (#FABF8F) |
| Gap_Analysis | H:H | ="Open" | Red fill (#FFC7CE) |
| Gap_Analysis | H:H | ="Resolved" | Green fill (#C6EFCE) |
| Remediation_Tracker | G:G | ="Completed" | Green fill (#C6EFCE) |
| Remediation_Tracker | G:G | ="Not Started" | Red fill (#FFC7CE) |
| Remediation_Tracker | G:G | ="In Progress" | Yellow fill (#FFEB9C) |
| Exception_Register | J:J | ="Active" | Yellow fill (#FFEB9C) |
| Exception_Register | J:J | ="Expired" | Red fill (#FFC7CE) |
| Exception_Register | J:J | ="Revoked" | Green fill (#C6EFCE) |
| Role_Inventory | E:E | ="Critical" | Red fill (#FFC7CE), Bold |
| Role_Inventory | E:E | ="High" | Orange fill (#FABF8F) |

### Styling Standards

| Element | Style |
|---------|-------|
| Title | Bold 14pt, centered, merged |
| Headers | White text (#FFFFFF), Blue fill (#2F5496), Bold, Centered |
| Input cells | Yellow fill (#FFFFCC), thin border |
| Formula cells | Grey fill (#F2F2F2), protected |
| All data cells | Thin black border |
| Conflict markers | Color-coded per classification |

### Colour Palette

| Purpose | Colour Name | Hex Code |
|---------|-------------|----------|
| Header Background | Theme Blue | #2F5496 |
| Header Text | White | #FFFFFF |
| Input Field | Light Yellow | #FFFFCC |
| Critical/Error | Light Red | #FFC7CE |
| Warning | Light Orange | #FABF8F |
| Caution | Light Yellow | #FFEB9C |
| Success | Light Green | #C6EFCE |
| Neutral | Light Grey | #F2F2F2 |

---

## 2.4 Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| IAM/Active Directory | Role assignment export | IAM -> Current_Assignments |
| HR System | Organisation structure, manager hierarchy | HR -> Role_Inventory, Current_Assignments |
| RBAC Configuration | Role definitions, permissions | RBAC -> Role_Inventory |
| GRC Platform | Risk ratings, compliance status | Bidirectional |
| Access Review System | Periodic review results | Access Review -> Gap_Analysis |
| A.5.3.2 Workbook | Conflict analysis detail | This workbook -> A.5.3.2 |
| A.5.3.4 Dashboard | Compliance metrics | This workbook -> Dashboard |
| SIEM | Log monitoring for exceptions | SIEM -> Exception evidence |

---

## 2.5 Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.3 | Segregation of Duties | Parent policy |
| ISMS-IMP-A.5.3.2 | Conflict Analysis | Detailed conflict assessment |
| ISMS-IMP-A.5.3.3 | Role-Function Mapping | Role definition detail |
| ISMS-IMP-A.5.3.4 | Compliance Dashboard | Metrics aggregation |
| ISMS-IMP-A.5.15-16-18 | IAM Assessment | Access management integration |
| ISMS-IMP-A.5.24-28 | Incident Management | SoD violation incidents |

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
