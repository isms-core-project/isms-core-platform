**ISMS-IMP-A.5.35-36.S4-TG - Compliance and Review Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.35-36

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.35-36.S4-TG |
| **Title** | Compliance and Review Dashboard |
| **Control Reference** | ISO/IEC 27001:2022 A.5.35-36 |
| **Control Name** | Compliance and Review |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

# Technical Specification


> Auto-generated from `generate_a535_36_4_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.35-36.S4` |
| **Output Filename** | `ISMS-IMP-A.5.35-36.S4_Compliance_and_Review_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance and Review Dashboard |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E2EFDA | E2EFDA | Pale Green (Success Background) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Workbook

---

## Sheet 2: Instructions

**Frozen Panes:** A4

---

## Sheet 3: Executive_Summary

**Data Rows:** 4 (rows 1–4)

### Columns

| Col | Header |
|-----|--------|
| A | Metric |
| B | Current Value |
| C | Target |
| D | Status |

---

## Sheet 4: Review_Status

**Data Rows:** 20 (rows 4–23) | **Frozen Panes:** C4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Review_ID | 16 |
| B | Review_Type | 22 |
| C | Scope | 35 |
| D | Planned_Date | 14 |
| E | Actual_Date | 14 |
| F | Status | 16 |
| G | Lead_Reviewer | 22 |
| H | Findings_Count | 14 |
| I | Report_Status | 16 |
| J | Notes | 30 |

---

## Sheet 5: Compliance_Status

**Data Rows:** 7 (rows 2–8) | **Frozen Panes:** B4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Area | 30 |
| B | Policies_Total | 14 |
| C | Policies_Compliant | 16 |
| D | Compliance_% | 14 |
| E | Controls_Total | 14 |
| F | Controls_Implemented | 18 |
| G | Implementation_% | 16 |
| H | RAG_Status | 14 |

---

## Sheet 6: Findings_Overview

**Data Rows:** 4 (rows 2–5)

---

## Sheet 7: Kpi_Scorecard

**Data Rows:** 8 (rows 1–8) | **Frozen Panes:** C4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | KPI_ID | 12 |
| B | KPI_Name | 40 |
| C | Category | 20 |
| D | Current_Value | 16 |
| E | Target | 14 |
| F | Threshold_Amber | 16 |
| G | Threshold_Red | 14 |
| H | Status | 14 |

---

## Sheet 8: Trend_Analysis

**Data Rows:** 8 (rows 2–9) | **Frozen Panes:** B4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Period | 14 |
| B | Policy_Compliance_% | 18 |
| C | Control_Implementation_% | 20 |
| D | Reviews_Completed | 16 |
| E | Open_Findings | 14 |
| F | Closed_Findings | 14 |
| G | Avg_Closure_Days | 16 |
| H | Overall_Score | 14 |
| I | Notes | 35 |

---

## Sheet 9: Approval_Signoff

**Frozen Panes:** A3

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
