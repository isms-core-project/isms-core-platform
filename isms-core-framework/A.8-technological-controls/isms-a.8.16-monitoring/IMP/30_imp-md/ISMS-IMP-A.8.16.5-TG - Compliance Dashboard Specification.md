**ISMS-IMP-A.8.16.5-TG - Compliance Dashboard Specification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.16.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Compliance Dashboard, Metrics Consolidation, Executive Reporting |
| **Related Policy** | ISMS-POL-A.8.16, All Sections |
| **Purpose** | Consolidate metrics from A.8.16.1-4 assessments into executive dashboard with compliance scoring |
| **Target Audience** | Security Management, CISO, Compliance Officers, Executive Leadership, Auditors |
| **Assessment Type** | Data Consolidation & Reporting |
| **Review Cycle** | Monthly (dashboard updates), Quarterly (full review) |
| **Date** | 22.01.2026 |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original] | Initial technical specification | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a816_5_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.16.5` |
| **Output Filename** | `ISMS-IMP-A.8.16.5_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance Dashboard |
| **Total Sheets** | 14 (14 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #0000FF | 0000FF | Custom |
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D8E4F8 | D8E4F8 | Pale Blue (Sub-section) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: Executive Summary

---

## Sheet 3: Compliance Matrix

---

## Sheet 4: KPIs

---

## Sheet 5: Gap Remediation Tracker

---

## Sheet 6: Trend Analysis

---

## Sheet 7: Evidence & Approvals

---

## Sheet 8: Instructions_Legend

**Frozen Panes:** A4

---

## Sheet 9: Executive_Summary

**Data Rows:** 5 (rows 1–5) | **Frozen Panes:** A4

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIFS(` | Critical Gaps |
| CN | `=AVERAGE(C17:C20)` |  |
| DN | `=IF(C21>=95,\` |  |

---

## Sheet 10: Compliance_Matrix

**Data Rows:** 105 (rows 1–105) | **Frozen Panes:** A4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Policy Reference | 25 |
| B | Requirement | 40 |
| C | Control Type | 18 |
| D | Assessment Sheet | 22 |
| E | Evidence Location | 30 |
| F | Implementation Status | 20 |
| G | Compliance Status | 20 |
| H | Gap Description | 35 |
| I | Risk Level | 15 |
| J | Remediation Owner | 20 |
| K | Target Date | 14 |
| L | Notes | 25 |

---

## Sheet 11: Kpis

**Frozen Panes:** A4

---

## Sheet 12: Gap_Remediation_Tracker

**Data Rows:** 60 (rows 1–60) | **Frozen Panes:** A4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 12 |
| B | Source Assessment | 18 |
| C | Gap Category | 20 |
| D | Description | 35 |
| E | Risk | 12 |
| F | Impact | 15 |
| G | Remediation Plan | 30 |
| H | Owner | 20 |
| I | Target Date | 14 |
| J | Budget | 15 |
| K | Status | 15 |
| L | % Complete | 12 |
| M | Last Updated | 14 |

---

## Sheet 13: Trend_Analysis

**Frozen Panes:** A5

---

## Sheet 14: Evidence_Approvals

**Data Rows:** 100 (rows 1–100) | **Frozen Panes:** A4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 15 |
| B | Evidence Type | 20 |
| C | Description | 35 |
| D | Related Requirement | 22 |
| E | Source Assessment | 20 |
| F | Date Collected | 16 |
| G | Collected By | 20 |
| H | Location/Link | 30 |
| I | Verification Status | 20 |
| J | Verified By | 20 |
| K | Verification Date | 16 |
| L | Notes | 25 |

---

**END OF SPECIFICATION**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
