**ISMS-IMP-A.8.15.5-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Compliance Dashboard & Gap Prioritization |
| **Related Policy** | ISMS-POL-A.8.15 (All Sections) |
| **Purpose** | Consolidate assessments A.8.15.1, .2, .3, .4 into executive dashboard; track overall compliance; prioritize cross-domain gaps; monitor trends |
| **Target Audience** | CISO, Senior Management, Board of Directors, Information Security Manager, Compliance Team, Internal Audit, External Auditors, Workbook Developers |
| **Assessment Type** | Consolidation & Executive Reporting |
| **Review Cycle** | Quarterly (consolidation after all sub-assessments complete), Annual (formal presentation to Board) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial dashboard specification | ISMS Implementation Team |


---
# Technical Specification
**Audience:** Workbook Developers (Python/Excel script maintainers)


> Auto-generated from `generate_a815_5_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.15.5` |
| **Output Filename** | `ISMS-IMP-A.8.15.5_Logging_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Logging Compliance Dashboard |
| **Total Sheets** | 18 (18 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #9C0006 | color | Dark Red (Error) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | end_color | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |

## Sheet 1: Instructions & Data Sources

---

## Sheet 2: Compliance Overview

---

## Sheet 3: Consolidated Gap Register

---

## Sheet 4: Trend Analysis

---

## Sheet 5: Regulatory Mapping

---

## Sheet 6: Action Plan & Roadmap

---

## Sheet 7: Evidence Summary

---

## Sheet 8: Management Report

---

## Sheet 9: Approval & Sign-Off

---

## Sheet 10: Instructions

**Purpose:** "If you can't measure it, you can't manage it." - Peter Drucker

---

## Sheet 11: Compliance_Overview

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=(B9+B10+B11+B12)/4` | Average of 4 IMPs |
| FN | `=IF(B6>=0.95,` |  |
| DN | `=IF(B{row}=` |  |
| DN | `=IF(B` |  |

---

## Sheet 12: Consolidated_Gap_Register

**Data Rows:** 200 (rows 9–208) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 12 |
| B | Source IMP | 15 |
| C | Category | 25 |
| D | Description | 50 |
| E | Impact | 30 |
| F | Priority | 12 |
| G | Remediation Action | 50 |
| H | Owner | 25 |
| I | Budget Required | 15 |
| J | Target Date | 15 |
| K | Status | 15 |
| L | % Complete | 12 |
| M | Days Overdue | 12 |
| N | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B9:B208 | `imp_dv` |
| F | F9:F208 | `priority_dv` |
| I | I9:I208 | `budget_dv` |
| K | K9:K208 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| MN | `=IF(AND(J{data_row}<>` |  |
| — | `=COUNTA(A9:A208)` | Total Gaps: |
| — | `=COUNTIF(F9:F208,\` | Critical Priority: |
| — | `=COUNTIF(K9:K208,\` | Open Status: |
| — | `=COUNTIF(M9:M208,\` | Overdue Gaps: |
| — | `=COUNTIF(I9:I208,\` | Budget Required Count: |

---

## Sheet 13: Trend_Analysis

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| HN | `=IF(AND(F{row}<>` |  |

---

## Sheet 14: Regulatory_Mapping

**Data Rows:** 150 (rows 10–159) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Regulation / Standard | 25 |
| B | Requirement ID | 20 |
| C | Requirement Description | 50 |
| D | Policy Section | 20 |
| E | IMP Coverage | 25 |
| F | Applicable Systems | 30 |
| G | Compliance Status | 18 |
| H | Evidence Location | 40 |
| I | Last Verified | 15 |
| J | Next Verification | 15 |
| K | Gaps | 40 |
| L | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| A | A10:A159 | `regulation_dv` |
| G | G10:G159 | `compliance_dv` |

---

## Sheet 15: Action_Plan_Roadmap

**Data Rows:** 42 (rows 9–50) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Initiative ID | 15 |
| B | Initiative Name | 30 |
| C | Description | 50 |
| D | Strategic Goal | 30 |
| E | Related Gaps | 25 |
| F | Priority | 15 |
| G | Start Date | 15 |
| H | Target End Date | 15 |
| I | Status | 15 |
| J | % Complete | 12 |
| K | Budget ($) | 15 |
| L | Owner | 25 |
| M | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| D | D9:D50 | `goal_dv` |
| F | F9:F50 | `priority_dv` |
| I | I9:I50 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{data_row}<>` |  |

---

## Sheet 16: Evidence_Summary

**Data Rows:** 52 (rows 9–60) | **Frozen Panes:** A9

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 12 |
| B | Assessment Domain | 20 |
| C | Evidence Type | 18 |
| D | Description | 35 |
| E | Source Location | 25 |
| F | Date Collected | 14 |
| G | Status | 12 |
| H | Audit Ready | 12 |
| I | Retention | 12 |
| J | Notes | 25 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| G | G9:G60 | `status_dv` |
| H | H9:H60 | `audit_dv` |
| B | B9:B60 | `domain_dv` |

---

## Sheet 17: Management_Report

---

## Sheet 18: Approval_Signoff

---

**END OF SPECIFICATION**

---

*"Sometimes it is the people no one imagines anything of who do the things that no one can imagine."*
- Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
