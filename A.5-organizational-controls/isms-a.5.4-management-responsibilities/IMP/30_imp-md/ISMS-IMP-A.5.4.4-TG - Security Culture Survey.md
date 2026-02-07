**ISMS-IMP-A.5.4.4-TG - Security Culture Survey**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.4: Management Responsibilities

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.4-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

# Technical Specification


> Auto-generated from `generate_a54_4_security_culture_survey.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.4.4` |
| **Output Filename** | `ISMS-IMP-A.5.4.4_Security_Culture_Survey_YYYYMMDD.xlsx` |
| **Workbook Title** | Security Culture Survey |
| **Total Sheets** | 6 (6 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D6DCE4 | D6DCE4 | Silver (Neutral) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Survey Questions

### Columns

| Col | Header |
|-----|--------|
| A | Question_ID |
| B | Category |
| C | Question_Text |
| D | Response_Scale |

---

## Sheet 3: Response Data

### Columns

| Col | Header |
|-----|--------|
| A | Department |
| B | Respondents |
| C | Response_Rate |

---

## Sheet 4: YoY Trend Analysis

**Data Rows:** 12 (rows 4–15)

### Columns

| Col | Header |
|-----|--------|
| A | Category |
| B | Year-3 |
| C | Year-2 |
| D | Year-1 |
| E | Current |
| F | YoY_Change |
| G | Trend |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| G | G4:G15 | `trend_dv` |

---

## Sheet 5: Action Plan

**Data Rows:** 21 (rows 5–25)

### Columns

| Col | Header |
|-----|--------|
| A | Action_ID |
| B | Category |
| C | Current_Score |
| D | Gap |
| E | Action_Required |
| F | Owner |
| G | Due_Date |
| H | Status |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| H | H5:H25 | `status_dv` |

---

## Sheet 6: Executive Summary

**Data Rows:** 3 (rows 2–4)

### Columns

| Col | Header |
|-----|--------|
| A | Metric |
| B | Value |
| C | Benchmark |

---

**END OF SPECIFICATION**

---

*"Culture eats strategy for breakfast."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
