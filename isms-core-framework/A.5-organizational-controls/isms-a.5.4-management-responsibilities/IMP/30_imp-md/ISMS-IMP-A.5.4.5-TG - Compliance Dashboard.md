**ISMS-IMP-A.5.4.5-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.4: Management Responsibilities

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.5-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

# Technical Specification


> Auto-generated from `generate_a54_5_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.4.5` |
| **Output Filename** | `ISMS-IMP-A.5.4.5_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance Dashboard |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #1F4E79 | 1F4E79 | Custom |
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #E2EFDA | E2EFDA | Pale Green (Success Background) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Executive_Summary

**Data Rows:** 5 (rows 7–11)

### Columns

| Col | Header |
|-----|--------|
| A | Assessment Domain |
| B | Workbook |
| C | Status |
| D | Score % |
| E | Key Issues |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C7:C11 | `status_dv` |

---

## Sheet 3: Compliance_KPIs

**Data Rows:** 19 (rows 2–20)

### Columns

| Col | Header |
|-----|--------|
| A | KPI_ID |
| B | KPI_Name |
| C | Description |
| D | Target |
| E | Current_Value |
| F | Measurement_Method |
| G | Frequency |
| H | Data_Source |
| I | Owner |
| J | Status |
| K | Trend |
| L | Comments |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| J | J2:J20 | `status_dv` |
| K | K2:K20 | `trend_dv` |
| G | G2:G20 | `freq_dv` |

---

## Sheet 4: Compliance_Scorecard

**Data Rows:** 19 (rows 2–20)

### Columns

| Col | Header |
|-----|--------|
| A | Requirement_ID |
| B | Requirement |
| C | Source |
| D | Weight |
| E | Evidence_Available |
| F | Implementation_Status |
| G | Score |
| H | Max_Score |
| I | Gap_Description |
| J | Remediation_Status |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E20 | `evidence_dv` |
| F | F2:F20 | `impl_dv` |
| J | J2:J20 | `remed_dv` |

---

## Sheet 5: Gap_Analysis

**Data Rows:** 29 (rows 2–30)

### Columns

| Col | Header |
|-----|--------|
| A | Gap_ID |
| B | Requirement_Reference |
| C | Gap_Description |
| D | Risk_Level |
| E | Root_Cause |
| F | Remediation_Action |
| G | Owner |
| H | Target_Date |
| I | Status |
| J | Progress |
| K | Evidence_of_Closure |
| L | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D2:D30 | `risk_dv` |
| I | I2:I30 | `status_dv` |
| J | J2:J30 | `progress_dv` |

---

## Sheet 6: Audit_Readiness

**Data Rows:** 19 (rows 2–20)

### Columns

| Col | Header |
|-----|--------|
| A | Check_ID |
| B | Audit_Requirement |
| C | Evidence_Required |
| D | Evidence_Location |
| E | Evidence_Available |
| F | Last_Reviewed |
| G | Reviewer |
| H | Status |
| I | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E20 | `avail_dv` |
| H | H2:H20 | `status_dv` |

---

## Sheet 7: Trend_Analysis

### Columns

| Col | Header |
|-----|--------|
| A | Period |
| B | Commitment_Score |
| C | Training_Compliance |
| D | Violation_Response |
| E | Access_Review_Rate |
| F | Culture_Score |
| G | Overall_Score |
| H | Key_Changes |
| I | Notes |

---

## Sheet 8: Evidence_Register

**Data Rows:** 49 (rows 2–50)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_ID |
| B | Evidence_Type |
| C | Description |
| D | Related_Requirement |
| E | Date_Created |
| F | Created_By |
| G | Storage_Location |
| H | Retention_Period |
| I | Review_Date |
| J | Status |
| K | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B2:B50 | `type_dv` |
| J | J2:J50 | `status_dv` |

---

## Sheet 9: Approval_SignOff

**Data Rows:** 4 (rows 2–5)

### Columns

| Col | Header |
|-----|--------|
| A | Role |
| B | Name |
| C | Date |
| D | Signature |
| E | Comments |

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
