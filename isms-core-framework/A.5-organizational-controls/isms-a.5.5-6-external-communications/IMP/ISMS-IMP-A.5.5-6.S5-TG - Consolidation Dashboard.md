<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.5-6.S5-TG:framework:TG:a.5.5-6 -->
**ISMS-IMP-A.5.5-6.S5-TG - External Communications Consolidation Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.5.5 & A.5.6: Executive Consolidation

## Implementation Guide for ISO 27001:2022 Controls A.5.5 & A.5.6: Executive Consolidation

**Document ID:** ISMS-IMP-A.5.5-6.S5-TG
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


> Auto-generated from `generate_a55_6_5_consolidation_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.5-6.S5` |
| **Output Filename** | `ISMS-IMP-A.5.5-6.S5_Consolidation_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Consolidation Dashboard |
| **Total Sheets** | 12 (12 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls A.5.5 & A.5.6: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #002060 | 002060 | Custom |
| #1F4E79 | 1F4E79 | Custom |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #E2EFDA | E2EFDA | Pale Green (Success Background) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Executive_Summary

**Data Rows:** 3 (rows 2–4)

### Columns

| Col | Header |
|-----|--------|
| A | Domain |
| B | Workbook |
| C | Status |
| D | Score % |
| E | Critical Gaps |
| F | Last Updated |

---

## Sheet 3: Domain_Overview

**Data Rows:** 4 (rows 2–5)

### Columns

| Col | Header |
|-----|--------|
| A | Requirement |
| B | Status |
| C | Evidence Ref |
| D | Gap Description |
| E | Remediation |

---

## Sheet 4: Authority_Compliance

**Data Rows:** 8 (rows 2–9)

### Columns

| Col | Header |
|-----|--------|
| A | Authority_Type |
| B | Authority_Name |
| C | Contact_Status |
| D | Last_Verified |
| E | Next_Review |
| F | Compliance_Status |
| G | Gap_Notes |
| H | Action_Required |
| I | Owner |

---

## Sheet 5: SIG_Compliance

**Data Rows:** 8 (rows 2–9)

### Columns

| Col | Header |
|-----|--------|
| A | SIG_Category |
| B | Group_Name |
| C | Membership_Status |
| D | Value_Rating |
| E | Last_Engagement |
| F | Intelligence_Received |
| G | Compliance_Status |
| H | Gap_Notes |
| I | Owner |

---

## Sheet 6: Procedure_Compliance

**Data Rows:** 6 (rows 3–8)

### Columns

| Col | Header |
|-----|--------|
| A | Procedure_Type |
| B | Procedure_Name |
| C | Status |
| D | Last_Reviewed |
| E | Compliance_Status |
| F | Gap_Description |
| G | Remediation_Action |
| H | Owner |

---

## Sheet 7: Cross_Domain_Gaps

**Data Rows:** 15 (rows 4–18)

### Columns

| Col | Header |
|-----|--------|
| A | Gap_ID |
| B | Source_Domain |
| C | Gap_Description |
| D | Risk_Rating |
| E | Priority |
| F | Affected_Controls |
| G | Root_Cause |
| H | Remediation_Action |
| I | Owner |
| J | Target_Date |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B4:B18 | `domain_dv` |
| E | E4:E18 | `priority_dv` |

---

## Sheet 8: Remediation_Tracker

**Data Rows:** 20 (rows 4–23)

### Columns

| Col | Header |
|-----|--------|
| A | Action_ID |
| B | Related_Gap |
| C | Source_Domain |
| D | Action_Description |
| E | Priority |
| F | Owner |
| G | Start_Date |
| H | Target_Date |
| I | Status |
| J | Progress_% |
| K | Notes |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| I | I4:I23 | `status_dv` |

---

## Sheet 9: KPI_Summary

### Columns

| Col | Header |
|-----|--------|
| A | KPI |
| B | Target |
| C | Current |
| D | Previous |
| E | Trend |
| F | Status |

---

## Sheet 10: Evidence_Index

**Data Rows:** 20 (rows 4–23)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence_ID |
| B | Source_Workbook |
| C | Source_Sheet |
| D | Evidence_Type |
| E | Evidence_Description |
| F | Location/Reference |
| G | Date_Captured |
| H | Validation_Status |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B4:B23 | `source_dv` |

---

## Sheet 11: Trend_Dashboard

**Data Rows:** 7 (rows 2–8)

### Columns

| Col | Header |
|-----|--------|
| A | Period |
| B | A.5.5 Authority % |
| C | A.5.6 SIG % |
| D | Procedures % |
| E | Overall % |
| F | Critical Gaps |
| G | Remediation Rate |
| H | Notes |

---

## Sheet 12: Approval_SignOff

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

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `DOMAIN_VALUES` | A.5.5-6.1 Authority Contacts, A.5.5-6.2 SIG Membership, A.5.5-6.3 Procedures, A.5.5-6.4 Dashboard... |
| `PRIORITY_VALUES` | Critical, High, Medium, Low |
| `STATUS_VALUES` | Compliant, Partially Compliant, Non-Compliant, Not Assessed, Not Applicable |

---

**END OF SPECIFICATION**

---

*"The whole is greater than the sum of its parts."*
— Aristotle

<!-- QA_VERIFIED: 2026-02-06 -->
