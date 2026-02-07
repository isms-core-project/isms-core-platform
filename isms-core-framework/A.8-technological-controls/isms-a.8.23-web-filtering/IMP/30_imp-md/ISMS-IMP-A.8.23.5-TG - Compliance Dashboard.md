**ISMS-IMP-A.8.23.5-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.23: Web Filtering

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.23.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Compliance Dashboard & Consolidation |
| **Related Policy** | ISMS-POL-A.8.23 (All Sections) |
| **Purpose** | Consolidate all domain assessments into executive compliance view with scoring, gap analysis, and audit readiness certification |
| **Target Audience** | CISO, Executive Management, Board of Directors, Internal/External Auditors, ISO 27001 Certification Bodies |
| **Assessment Type** | Executive Dashboard & Consolidation |
| **Review Cycle** | Quarterly (synchronized with domain assessments) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Web Filtering Compliance Dashboard workbook | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a823_5_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.23.5` |
| **Output Filename** | `ISMS-IMP-A.8.23.5_Compliance_Summary_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance Summary Dashboard |
| **Total Sheets** | 18 (18 visible) |
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
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Executive Dashboard

---

## Sheet 2: Gap Analysis

---

## Sheet 3: Risk Register

---

## Sheet 4: Remediation Roadmap

---

## Sheet 5: KPIs & Metrics

---

## Sheet 6: Evidence Register

---

## Sheet 7: Action Items & Follow-up

---

## Sheet 8: Audit & Compliance Log

---

## Sheet 9: Approval Sign-Off

---

## Sheet 10: Executive_Dashboard

**Data Rows:** 200 (rows 8–207) | **Frozen Panes:** A4

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIFS(` | Critical Gaps |
| — | `=COUNTIF(` | Remediation Progress |

---

## Sheet 11: Gap_Analysis

**Data Rows:** 19 (rows 1–19) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | Source Assessment |
| C | Gap Category |
| D | Gap Description |
| E | Current State |
| F | Target State |
| G | Impact |
| H | Likelihood |
| I | Risk Score |
| J | Priority |
| K | Remediation Action |
| L | Owner |
| M | Target Date |
| N | Status |
| O | Progress % |
| P | Cost Estimate |
| Q | Dependencies |
| R | Verification Method |
| S | Status Notes |

---

## Sheet 12: Risk_Register

**Data Rows:** 17 (rows 1–17) | **Frozen Panes:** A20

### Columns

| Col | Header |
|-----|--------|
| A | Risk ID |
| B | Source |
| C | Risk Category |
| D | Risk Description |
| E | Threat Source |
| F | Vulnerability |
| G | Impact |
| H | Likelihood |
| I | Inherent Risk |
| J | Controls |
| K | Control Effectiveness |
| L | Residual Impact |
| M | Residual Likelihood |
| N | Residual Risk |
| O | Treatment |
| P | Owner |
| Q | Status |

---

## Sheet 13: Remediation_Roadmap

**Data Rows:** 200 (rows 37–236) | **Frozen Panes:** A37

### Columns

| Col | Header |
|-----|--------|
| A | Action ID |
| B | Phase |
| C | Related Gap/Risk |
| D | Action Description |
| E | Target Date |
| F | Assigned Owner |
| G | Department |
| H | Status |
| I | Progress % |
| J | Actual Completion |
| K | Budget |
| L | Dependencies |
| M | Success Criteria |
| N | Verification |
| O | Notes |
| P | Last Updated |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(A37:A236)` | Total Action Items |
| — | `=COUNTIF(H37:H236,\` | Completed |
| — | `=COUNTIFS(H37:H236,\` | Overdue |

---

## Sheet 14: Kpis_Metrics

**Data Rows:** 97 (rows 4–100) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | KPI Name |
| B | Unit |
| C | Current Value |
| D | Target |
| E | Status |
| F | Trend |
| G | Last Month |
| H | YTD Average |
| I | Data Source |
| J | Update Frequency |
| K | Owner |
| L | Collection Method |
| M | Notes |

---

## Sheet 15: Evidence_Register

**Data Rows:** 500 (rows 20–519) | **Frozen Panes:** A20

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Source Assessment |
| C | Related Requirement |
| D | Category |
| E | Evidence Type |
| F | Description |
| G | File Location |
| H | Collection Date |
| I | Collected By |
| J | Retention Period |
| K | Expiry Date |
| L | Verification Status |
| M | Verified By |
| N | Verification Date |
| O | Notes |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(A20:A519)` | Total Evidence Items |
| — | `=COUNTIF(L21:L519,\` | Verified |
| BN | `=COUNTIF(D21:D519,` |  |
| CN | `=COUNTIFS(D21:D519,` |  |
| DN | `=C{row}/B{row}` |  |

---

## Sheet 16: Action_Items

**Data Rows:** 200 (rows 20–219) | **Frozen Panes:** A20

### Columns

| Col | Header |
|-----|--------|
| A | Action ID |
| B | Source |
| C | Related Gap/Risk |
| D | Action Description |
| E | Priority |
| F | Due Date |
| G | Status |
| H | Completion Date |
| I | Assigned To |
| J | Department |
| K | Progress Notes |
| L | Blocker |
| M | Next Steps |
| N | Last Updated |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(A20:A219)` | Total Actions |
| — | `=COUNTIFS(F20:F219,\` | Overdue |
| — | `=COUNTIFS(G20:G219,\` | Completed This Month |
| — | `=COUNTIF(G20:G219,\` | Completion Rate |
| BN | `=COUNTIF(E20:E219,` |  |
| CN | `=COUNTIFS(E20:E219,` |  |

---

## Sheet 17: Audit_Log

**Data Rows:** 100 (rows 20–119) | **Frozen Panes:** A20

### Columns

| Col | Header |
|-----|--------|
| A | Finding ID |
| B | Audit Date |
| C | Audit Type |
| D | Auditor/Source |
| E | Finding Category |
| F | Finding Description |
| G | Severity |
| H | Affected Area |
| I | Status |
| J | Resolution Days |
| K | Resolution Date |
| L | Remediation Action |
| M | Notes |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(A20:A119)` | Total Findings (All Time) |
| — | `=COUNTIF(I21:I119,\` | Open Findings |
| BN | `=COUNTIF(G21:G119,` |  |
| CN | `=COUNTIFS(G21:G119,` |  |
| EN | `=D{row}/B{row}` |  |

---

## Sheet 18: Approval_Signoff

**Frozen Panes:** A3

---

**END OF SPECIFICATION**

---

*"An equation means nothing to me unless it expresses a thought of God."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
