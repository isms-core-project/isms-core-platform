**ISMS-IMP-A.5.7.4-TG - Threat Intelligence Effectiveness Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Program Effectiveness Dashboard with Automated Data Refresh |
| **Related Policy** | ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements), Section 3.2 (Exception Management), Section 3.4 (Policy Governance) |
| **Purpose** | Provide executive and management-level visibility into threat intelligence program effectiveness by aggregating data from all A.5.7 workbooks |
| **Target Audience** | CISO, Security Managers, Executive Management, Board, Auditors |
| **Assessment Type** | Aggregated Dashboard |
| **Review Cycle** | Monthly (data refresh), Quarterly (full review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification (12 sheets) | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a57_4_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.7.4` |
| **Output Filename** | `ISMS-IMP-A.5.7.4_Threat_Intelligence_Effectiveness_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Threat Intelligence Effectiveness Dashboard |
| **Total Sheets** | 13 (13 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #0000FF | 0000FF | Custom |
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #5B9BD5 | 5B9BD5 | Custom |
| #70AD47 | 70AD47 | Medium Green (On Track) |
| #8FAADC | 8FAADC | Custom |
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #DEEBF7 | DEEBF7 | Custom |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFF2CC | FFF2CC | Cream (Input Alt) |
| #FFFF00 | FFFF00 | Yellow (Warning) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Executive_Summary

---

## Sheet 2: Program_KPIs

---

## Sheet 3: Source_Portfolio

---

## Sheet 4: Intelligence_Operations

---

## Sheet 5: Integration_Status

---

## Sheet 6: Stakeholder_Engagement

---

## Sheet 7: Trend_Analysis

---

## Sheet 8: Risk_Indicators

---

## Sheet 9: Compliance_Evidence

---

## Sheet 10: Monthly_Report

---

## Sheet 11: Quarterly_Report

---

## Sheet 12: Metadata

---

## Sheet 13: Program_Kpis

**Data Rows:** 36 (rows 5–40) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | KPI_ID |
| B | KPI_Category |
| C | KPI_Name |
| D | Description |
| E | Unit |
| F | Measurement_Frequency |
| G | Data_Source |
| H | Target_Value |
| I | Warning_Threshold |
| J | Critical_Threshold |
| K | Current_Value |
| L | Last_Month_Value |
| M | Performance_vs_Target |
| N | Status |
| O | Trend |
| P | Owner |
| Q | Last_Updated |
| R | Notes |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| N5:N40 | equal  | Fill: #C6EFCE (Light Green (Compliant/Pass)) |
| KN:NN | greaterThan 0 | Fill: #FF0000 (Red (Critical/Alert)) |
| N5:N40 | equal  | Fill: #FFEB9C (Light Yellow/Amber (Partial)) |
| N5:N40 | equal  | Fill: #FFC7CE (Light Red (Non-Compliant/Fail)) |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| MN | `=IF(OR(K{row}=` |  |
| NN | `=IF(A{row}=` | Special handling for emergency indicator |
| NN | `=IF(K{row}=` |  |
| — | `=COUNTA(A5:A30)` | Total KPIs Tracked: |
| — | `=COUNTIF(N5:N30,` | On Track: |
| — | `=COUNTIF(O5:O30,` | Improving Trends: |

---

**END OF SPECIFICATION**

---

*"Every great and deep difficulty bears in itself its own solution."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
