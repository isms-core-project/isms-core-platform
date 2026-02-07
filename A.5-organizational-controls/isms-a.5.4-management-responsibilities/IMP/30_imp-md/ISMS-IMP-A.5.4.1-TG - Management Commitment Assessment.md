**ISMS-IMP-A.5.4.1-TG - Management Commitment Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.4: Management Responsibilities

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.1-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

# Technical Specification


> Auto-generated from `generate_a54_1_management_commitment.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.4.1` |
| **Output Filename** | `ISMS-IMP-A.5.4.1_Management_Commitment_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Management Commitment Assessment |
| **Total Sheets** | 4 (4 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #D6DCE4 | D6DCE4 | Silver (Neutral) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Manager Inventory

**Data Rows:** 49 (rows 2–50)

### Columns

| Col | Header |
|-----|--------|
| A | Manager_ID |
| B | Name |
| C | Title |
| D | Department |
| E | Management_Level |
| F | Direct_Reports |
| G | Assessment_Date |
| H | Assessor |
| I | Status |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E50 | `level_dv` |
| I | I2:I50 | `status_dv` |

---

## Sheet 3: Commitment Assessment

**Data Rows:** 499 (rows 2–500)

### Columns

| Col | Header |
|-----|--------|
| A | Manager_ID |
| B | Category |
| C | Criterion |
| D | Weight |
| E | Score (0-5) |
| F | Weighted_Score |
| G | Evidence |
| H | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E500 | `score_dv` |

---

## Sheet 4: Summary Scores

**Data Rows:** 48 (rows 3–50)

### Columns

| Col | Header |
|-----|--------|
| A | Manager_ID |
| B | Name |
| C | Management_Level |
| D | Total_Weight |
| E | Achieved_Score |
| F | Percentage |
| G | Status |
| H | Improvement_Areas |

---

**END OF SPECIFICATION**

---

*"The quality of a leader is reflected in the standards they set for themselves."*
— Ray Kroc

<!-- QA_VERIFIED: 2026-02-06 -->
