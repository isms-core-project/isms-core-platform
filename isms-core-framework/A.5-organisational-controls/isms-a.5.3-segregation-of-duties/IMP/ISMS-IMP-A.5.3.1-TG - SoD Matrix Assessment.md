<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.3.1-TG:framework:TG:a.5.3.1 -->
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

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.3.1-UG.

---

# Technical Specification


> Auto-generated from `generate_a53_1_sod_matrix.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.3.1` |
| **Output Filename** | `ISMS-IMP-A.5.3.1_SoD_Matrix_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | SoD Matrix Assessment |
| **Total Sheets** | 8 (8 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #1F4E79 | 1F4E79 | Custom |
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #D6DCE4 | D6DCE4 | Silver (Neutral) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FABF8F | FABF8F | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Role_Inventory

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Role_ID |
| B | Role_Name |
| C | Department |
| D | Process_Domain |
| E | Risk_Level |
| F | Description |
| G | Key_Duties |
| H | System_Access |
| I | Active |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C200 | `dept_dv` |
| D | D2:D200 | `domain_dv` |
| E | E2:E200 | `risk_dv` |
| I | I2:I200 | `active_dv` |

---

## Sheet 3: Conflict_Matrix

**Data Rows:** 199 (rows 2–200)

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B2:Z200 | `conflict_dv` |

---

## Sheet 4: Current_Assignments

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Person_ID |
| B | Name |
| C | Department |
| D | Primary_Role |
| E | Additional_Roles |
| F | Assignment_Date |
| G | Last_Review |
| H | Manager |
| I | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C200 | `dept_dv` |

---

## Sheet 5: Gap_Analysis

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Gap_ID |
| B | Person_ID |
| C | Name |
| D | Conflicting_Roles |
| E | Conflict_Type |
| F | Risk_Level |
| G | Identified_Date |
| H | Status |
| I | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E200 | `conflict_type_dv` |
| F | F2:F200 | `risk_dv` |
| H | H2:H200 | `status_dv` |

---

## Sheet 6: Remediation_Tracker

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Remediation_ID |
| B | Gap_ID |
| C | Action_Type |
| D | Description |
| E | Owner |
| F | Target_Date |
| G | Status |
| H | Completion_Date |
| I | Evidence_Ref |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C200 | `type_dv` |
| G | G2:G200 | `status_dv` |

---

## Sheet 7: Exception_Register

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Exception_ID |
| B | Gap_ID |
| C | Justification |
| D | Compensating_Controls |
| E | Risk_Acceptance |
| F | Approval_Date |
| G | Expiry_Date |
| H | Review_Frequency |
| I | Last_Review |
| J | Status |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| H | H2:H200 | `freq_dv` |
| J | J2:J200 | `status_dv` |

---

## Sheet 8: Approval_SignOff

**Data Rows:** 5 (rows 1–5)

### Columns

| Col | Header |
|-----|--------|
| A | Role |
| B | Name |
| C | Date |
| D | Signature |
| E | Comments |

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `CONFLICT_TYPES` | X, C, M, - |
| `DEPARTMENTS` | Executive, Finance, IT, Operations, HR, Legal, Sales, Marketing, Engineering, Support, Procuremen... |
| `EXCEPTION_STATUSES` | Active, Expired, Revoked |
| `GAP_STATUSES` | Open, Mitigated, Resolved, Accepted |
| `PROCESS_DOMAINS` | Financial, IT Operations, HR, Procurement, Security, Change Management, Other |
| `REMEDIATION_STATUSES` | Not Started, In Progress, Completed, Cancelled |
| `REMEDIATION_TYPES` | Role Removal, Role Reassignment, Process Redesign, Compensating Control |
| `REVIEW_FREQUENCIES` | Monthly, Quarterly, Semi-Annual, Annual |
| `RISK_LEVELS` | Critical, High, Medium, Low |

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
