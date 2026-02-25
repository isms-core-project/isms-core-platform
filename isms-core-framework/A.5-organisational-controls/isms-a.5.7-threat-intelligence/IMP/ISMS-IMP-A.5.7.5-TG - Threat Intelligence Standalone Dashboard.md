<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.7.5-TG:framework:TG:a.5.7.5 -->
**ISMS-IMP-A.5.7.5-TG - Threat Intelligence Standalone Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Standalone Executive Dashboard (Manual Entry, No Dependencies) |
| **Related Policy** | ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements), Section 3.4 (Policy Governance) |
| **Purpose** | Provide standalone, self-contained executive dashboard for TI program visibility without dependencies on detailed assessment workbooks |
| **Target Audience** | C-Suite Executives, Board Members, External Stakeholders, CISO, Auditors |
| **Assessment Type** | Executive Summary Dashboard |
| **Review Cycle** | Monthly (data entry), Quarterly (executive review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial specification (9 sheets) | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a57_5_compliance_dashboard_standalone.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.7.5` |
| **Output Filename** | `ISMS-IMP-A.5.7.5_Threat_Intelligence_Standalone_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Threat Intelligence Standalone Compliance Dashboard |
| **Total Sheets** | 10 (10 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #2E75B5 | 2E75B5 | Custom |
| #70AD47 | 70AD47 | Medium Green (On Track) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #D8E4F8 | D8E4F8 | Pale Blue (Sub-section) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FFC000 | FFC000 | Custom |

## Sheet 1: Instructions

### Columns

| Col | Header |
|-----|--------|
| A | Feature |
| B | 5.7.4 Comprehensive |
| C | 5.7.5 Standalone (This) |

---

## Sheet 2: Monthly_Data_Entry

### Columns

| Col | Header |
|-----|--------|
| A | Field |
| B | Value |
| C | Instructions |
| D | Example |

---

## Sheet 3: Executive_Dashboard

### Columns

| Col | Header |
|-----|--------|
| A | Metric |
| B | Target |
| C | Last Month |
| D | This Month |
| E | Status |
| F | Trend |

---

## Sheet 4: Trend_History

### Columns

| Col | Header |
|-----|--------|
| A | Period |
| B | Entry_Date |
| C | Active_Sources |
| D | Avg_Quality |
| E | Coverage_Gaps |
| F | Products_Published |
| G | Satisfaction |
| H | IOCs_Deployed |
| I | Hit_Rate_% |
| J | False_Positive_% |
| K | CVSS_4.0_% |
| L | CVSS_Accuracy_% |
| M | High_CVSS_Open |
| N | Prevented |
| O | Cost_Avoid_CHF |
| P | Program_Health |
| Q | Notes |

---

## Sheet 5: Critical_Actions

### Columns

| Col | Header |
|-----|--------|
| A | Action_ID |
| B | Action_Type |
| C | Description |
| D | Owner |
| E | Priority |
| F | Due_Date |
| G | Status |
| H | Resolution |
| I | Created_Date |
| J | Completed_Date |

---

## Sheet 6: Quarterly_Summary

### Columns

| Col | Header |
|-----|--------|
| A | Metric |
| B | Q-4 |
| C | Q-3 |
| D | Q-2 |
| E | Q-1 (Current) |
| F | QoQ Change |
| G | YoY Change |

---

## Sheet 7: Risk_Summary

### Columns

| Col | Header |
|-----|--------|
| A | Risk_ID |
| B | Risk_Category |
| C | Risk_Description |
| D | Likelihood |
| E | Impact |
| F | Risk_Score |
| G | Mitigation_Status |
| H | Mitigation_Plan |
| I | Owner |
| J | Review_Date |
| K | Status |

---

## Sheet 8: ROI_Summary

### Columns

| Col | Header |
|-----|--------|
| A | Cost Category |
| B | This Year (CHF) |
| C | Last Year (CHF) |
| D | Change (CHF) |
| E | Change (%) |
| F | Notes |

---

## Sheet 9: Metadata

---

## Sheet 10: Roi_Summary

### Columns

| Col | Header |
|-----|--------|
| A | Cost Category |
| B | This Year (CHF) |
| C | Last Year (CHF) |
| D | Change (CHF) |
| E | Change (%) |
| F | Notes |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=SUM(B{start_row}:B{row-1})` |  |
| CN | `=SUM(C{start_row}:C{row-1})` |  |
| DN | `=B{row}-C{row}` |  |
| EN | `=(B{row}-C{row})/C{row}*100` |  |
| BN | `=SUM(B{start_row_value}:B{row-1})` |  |
| CN | `=SUM(C{start_row_value}:C{row-1})` |  |
| BN | `=SUM(B{start_cvss}:B{row-1})` |  |
| CN | `=AVERAGE(C{start_cvss}:C{row-1})` |  |
| DN | `=SUM(D{start_cvss}:D{row-1})` |  |
| EN | `=D{r}/D${row}*100` |  |

---

**END OF SPECIFICATION**

---

*"If quantum mechanics hasn't profoundly shocked you, you haven't understood it yet."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
