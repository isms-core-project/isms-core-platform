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

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.3.3-UG.

---

# Technical Specification


> Auto-generated from `generate_a53_3_role_function_mapping.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.3.3` |
| **Output Filename** | `ISMS-IMP-A.5.3.3_Role_Function_Mapping_YYYYMMDD.xlsx` |
| **Workbook Title** | Role Function Mapping |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #1F4E79 | 1F4E79 | Custom |
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FABF8F | FABF8F | Custom |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Business_Roles

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Business_Role_ID |
| B | Role_Name |
| C | Department |
| D | Process_Domain |
| E | Role_Owner |
| F | Description |
| G | Risk_Level |
| H | Last_Reviewed |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C200 | `dept_dv` |
| D | D2:D200 | `domain_dv` |
| G | G2:G200 | `risk_dv` |

---

## Sheet 3: Application_Roles

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | App_Role_ID |
| B | Application |
| C | Role_Name |
| D | Role_Type |
| E | Description |
| F | Business_Roles |
| G | Criticality |
| H | Review_Frequency |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D2:D200 | `type_dv` |
| G | G2:G200 | `crit_dv` |
| H | H2:H200 | `freq_dv` |

---

## Sheet 4: Functions

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Function_ID |
| B | Function_Name |
| C | Category |
| D | Application |
| E | Process |
| F | Description |
| G | Risk_Level |
| H | SoD_Sensitive |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C200 | `cat_dv` |
| G | G2:G200 | `risk_dv` |
| H | H2:H200 | `sod_dv` |

---

## Sheet 5: Permissions

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Permission_ID |
| B | Function_ID |
| C | Application |
| D | Permission_Name |
| E | Permission_Type |
| F | Description |
| G | Data_Scope |
| H | Special_Conditions |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E200 | `type_dv` |

---

## Sheet 6: Role_Function_Map

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Mapping_ID |
| B | Business_Role_ID |
| C | App_Role_ID |
| D | Function_ID |
| E | Grant_Type |
| F | Justification |
| G | Effective_Date |
| H | Expiry_Date |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E200 | `grant_dv` |

---

## Sheet 7: Function_Conflicts

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Conflict_ID |
| B | Function_A |
| C | Function_B |
| D | Conflict_Type |
| E | Risk_Level |
| F | Justification |
| G | Mitigation |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D2:D200 | `type_dv` |
| E | E2:E200 | `risk_dv` |

---

## Sheet 8: Validation_Status

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Validation_ID |
| B | Role_ID |
| C | Validation_Date |
| D | Validator |
| E | Documented_Functions |
| F | Actual_Functions |
| G | Discrepancies |
| H | Status |
| I | Resolution |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| H | H2:H200 | `status_dv` |

---

## Sheet 9: Change_Log

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Change_ID |
| B | Change_Date |
| C | Role_ID |
| D | Change_Type |
| E | Description |
| F | Requested_By |
| G | Approved_By |
| H | Ticket_Reference |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D2:D200 | `type_dv` |

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `CHANGE_TYPES` | Permission Added, Permission Removed, Function Modified, Role Created, Role Deleted |
| `CONFLICT_TYPES` | X, C, M |
| `DEPARTMENTS` | Executive, Finance, IT, Operations, HR, Legal, Sales, Marketing, Engineering, Support, Procuremen... |
| `FUNCTION_CATEGORIES` | Create, Read, Update, Delete, Approve, Execute, Admin |
| `GRANT_TYPES` | Direct, Inherited, Delegated, Emergency |
| `PERMISSION_TYPES` | Transaction, Report, API, Config, Data |
| `PROCESS_DOMAINS` | Financial, IT Operations, HR, Procurement, Security, Change Management, Other |
| `REVIEW_FREQUENCIES` | Monthly, Quarterly, Semi-Annual, Annual |
| `RISK_LEVELS` | Critical, High, Medium, Low |
| `ROLE_TYPES` | Composite, Single |
| `VALIDATION_STATUSES` | Validated, Requires Investigation, Remediated, Deferred |

---

**END OF SPECIFICATION**

---

*"The devil is in the details."*
— Ludwig Mies van der Rohe

<!-- QA_VERIFIED: 2026-02-06 -->
