**ISMS-IMP-A.5.4.2-TG - Compliance Oversight Tracker**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.4: Management Responsibilities

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.2-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

# Technical Specification


> Auto-generated from `generate_a54_2_compliance_oversight.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.4.2` |
| **Output Filename** | `ISMS-IMP-A.5.4.2_Compliance_Oversight_Tracker_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance Oversight Tracker |
| **Total Sheets** | 6 (6 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Training Oversight

**Data Rows:** 49 (rows 2–50)

### Columns

| Col | Header |
|-----|--------|
| A | Manager_ID |
| B | Manager_Name |
| C | Department |
| D | Team_Size |
| E | Training_Required |
| F | Training_Completed |
| G | Completion_Rate |
| H | Overdue_Count |
| I | Follow_Up_Actions |
| J | Last_Review_Date |

---

## Sheet 3: Policy Violations

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Violation_ID |
| B | Date_Reported |
| C | Manager_ID |
| D | Manager_Name |
| E | Employee_ID |
| F | Violation_Type |
| G | Severity |
| H | Manager_Response |
| I | Response_Date |
| J | Resolution |
| K | Lessons_Learned |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| G | G2:G100 | `severity_dv` |
| H | H2:H100 | `response_dv` |
| J | J2:J100 | `resolution_dv` |

---

## Sheet 4: Access Reviews

**Data Rows:** 99 (rows 2–100)

### Columns

| Col | Header |
|-----|--------|
| A | Review_ID |
| B | Review_Period |
| C | Manager_ID |
| D | Manager_Name |
| E | System_Scope |
| F | Accounts_Reviewed |
| G | Changes_Requested |
| H | Review_Completed |
| I | Completion_Date |
| J | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| H | H2:H100 | `completed_dv` |

---

## Sheet 5: Escalation Triggers

### Columns

| Col | Header |
|-----|--------|
| A | Metric |
| B | Threshold |
| C | Condition |
| D | Escalation Action |

---

## Sheet 6: Quarterly Summary

**Data Rows:** 199 (rows 2–200)

### Columns

| Col | Header |
|-----|--------|
| A | Manager_ID |
| B | Manager_Name |
| C | Quarter |
| D | Training_Compliance_Rate |
| E | Violations_Handled |
| F | Avg_Response_Days |
| G | Access_Reviews_Completed |
| H | Overall_Rating |
| I | Comments |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C2:C200 | `quarter_dv` |
| H | H2:H200 | `rating_dv` |

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Russian proverb (popularised by Ronald Reagan)

<!-- QA_VERIFIED: 2026-02-06 -->
