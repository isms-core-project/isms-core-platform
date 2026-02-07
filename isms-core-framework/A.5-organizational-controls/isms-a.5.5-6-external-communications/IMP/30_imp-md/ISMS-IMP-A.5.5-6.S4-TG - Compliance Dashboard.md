**ISMS-IMP-A.5.5-6.S4-TG - External Communications Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.5.5 & A.5.6: Compliance Monitoring

## Implementation Guide for ISO 27001:2022 Controls A.5.5 & A.5.6: Compliance Monitoring

**Document ID:** ISMS-IMP-A.5.5-6.S4-TG
**Version:** 1.0
**Classification:** Internal Use
**Owner:** CISO
**Last Review:** [Date to be set]
**Next Review:** [Date to be set]

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | ISMS Team | Initial release |

---

# Technical Specification


> Auto-generated from `generate_a55_6_4_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.5-6.S4` |
| **Output Filename** | `ISMS-IMP-A.5.5-6.S4_External_Communications_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | External Communications Compliance Dashboard |
| **Total Sheets** | 10 (10 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls A.5.5 & A.5.6: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #1F4E79 | 1F4E79 | Custom |
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Executive_Summary

**Data Rows:** 3 (rows 6–8)

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B6:B8 | `status_dv` |
| D | D6:D8 | `trend_dv` |

---

## Sheet 3: Authority_KPIs

**Data Rows:** 29 (rows 2–30)

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
| J | J2:J30 | `status_dv` |
| K | K2:K30 | `trend_dv` |
| G | G2:G30 | `freq_dv` |

---

## Sheet 4: SIG_KPIs

**Data Rows:** 29 (rows 2–30)

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
| J | J2:J30 | `status_dv` |
| K | K2:K30 | `trend_dv` |

---

## Sheet 5: Compliance_Scorecard

**Data Rows:** 29 (rows 2–30)

### Columns

| Col | Header |
|-----|--------|
| A | Requirement_ID |
| B | Requirement |
| C | Control_Reference |
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
| E | E2:E30 | `evidence_dv` |
| F | F2:F30 | `impl_dv` |
| J | J2:J30 | `remed_dv` |

---

## Sheet 6: Gap_Analysis

**Data Rows:** 49 (rows 2–50)

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
| D | D2:D50 | `risk_dv` |
| I | I2:I50 | `status_dv` |
| J | J2:J50 | `progress_dv` |

---

## Sheet 7: Audit_Readiness

**Data Rows:** 29 (rows 2–30)

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
| E | E2:E30 | `avail_dv` |
| H | H2:H30 | `status_dv` |

---

## Sheet 8: Trend_Analysis

### Columns

| Col | Header |
|-----|--------|
| A | Period |
| B | Authority_Compliance_Score |
| C | SIG_Compliance_Score |
| D | Combined_Score |
| E | Key_Changes |
| F | Notable_Events |
| G | Actions_Taken |

---

## Sheet 9: Evidence_Register

**Data Rows:** 99 (rows 2–100)

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
| B | B2:B100 | `type_dv` |
| J | J2:J100 | `status_dv` |

---

## Sheet 10: Approval_SignOff

**Data Rows:** 19 (rows 2–20)

### Columns

| Col | Header |
|-----|--------|
| A | Approval_ID |
| B | Review_Period |
| C | Review_Date |
| D | Reviewer_Name |
| E | Reviewer_Role |
| F | Dashboard_Complete |
| G | KPIs_Current |
| H | Gaps_Addressed |
| I | Approval_Status |
| J | Signature_Date |
| K | Next_Review_Date |
| L | Comments |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| E | E2:E20 | `role_dv` |
| F | F2:F20 | `yn_dv` |
| G | G2:G20 | `yn_dv` |
| H | H2:H20 | `yn_dv` |
| I | I2:I20 | `status_dv` |

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
