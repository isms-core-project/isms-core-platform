**ISMS-IMP-A.5.4.3-TG - Leadership Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.4: Management Responsibilities

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.3-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

# Technical Specification


> Auto-generated from `generate_a54_3_leadership_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.4.3` |
| **Output Filename** | `ISMS-IMP-A.5.4.3_Leadership_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Leadership Dashboard |
| **Total Sheets** | 5 (5 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #E2EFDA | E2EFDA | Pale Green (Success Background) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Executive Summary

**Data Rows:** 4 (rows 1–4)

---

## Sheet 3: By Department

**Data Rows:** 19 (rows 2–20)

### Columns

| Col | Header |
|-----|--------|
| A | Department |
| B | Manager_Count |
| C | Avg_Commitment_Score |
| D | Training_Compliance |
| E | Violations_Handled |
| F | Access_Reviews |
| G | Status |
| H | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| G | G2:G20 | `status_dv` |

---

## Sheet 4: Trend Analysis

**Data Rows:** 19 (rows 2–20)

### Columns

| Col | Header |
|-----|--------|
| A | Metric |
| B | Q1 |
| C | Q2 |
| D | Q3 |
| E | Q4 |
| F | YoY_Change |
| G | Trend |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| G | G2:G20 | `trend_dv` |

---

## Sheet 5: Action Items

**Data Rows:** 49 (rows 2–50)

### Columns

| Col | Header |
|-----|--------|
| A | Action_ID |
| B | Finding |
| C | Action_Required |
| D | Owner |
| E | Due_Date |
| F | Status |
| G | Completion_Date |
| H | Evidence |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| F | F2:F50 | `status_dv` |

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
