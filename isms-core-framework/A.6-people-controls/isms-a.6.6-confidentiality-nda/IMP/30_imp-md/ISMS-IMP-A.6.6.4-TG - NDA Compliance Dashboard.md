**ISMS-IMP-A.6.6.4-TG - NDA Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.6: Confidentiality or Non-Disclosure Agreements

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.6.6.4-TG |
| **Document Title** | NDA Compliance Dashboard Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.6.6: Confidentiality or Non-Disclosure Agreements |
| **Parent Policy** | ISMS-POL-A.6.6 (Confidentiality and Non-Disclosure Agreements) |
| **Version** | 1.0 |
| **Classification** | Internal |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial implementation specification for ISO 27001:2022 first certification |

---

# Technical Specification


> Auto-generated from `generate_a66_4_nda_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.6.6.4` |
| **Output Filename** | `ISMS-IMP-A.6.6.4_NDA_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | NDA Compliance Dashboard |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #2F5496 | 2F5496 | Dark Blue (Alt Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Workbook

---

## Sheet 2: Instructions

---

## Sheet 3: Executive_Summary

**Data Rows:** 5 (rows 13–17)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Message | 50 |
| B | Priority | 12 |
| C | Owner | 20 |
| D | Action Required | 14 |

---

## Sheet 4: Coverage_Metrics

**Data Rows:** 10 (rows 3–12) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Category | 22 |
| B | Total_Required | 14 |
| C | NDA_Signed | 14 |
| D | Coverage_% | 12 |
| E | Status | 12 |
| F | Missing | 12 |
| G | Expired | 12 |
| H | Notes | 35 |

---

## Sheet 5: Expiration_Status

**Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Time_Period | 20 |
| B | Count | 12 |
| C | Counterparties | 40 |
| D | Renewal_Started | 14 |
| E | Renewal_Complete | 16 |
| F | At_Risk | 12 |
| G | Notes | 30 |

---

## Sheet 6: Compliance_Scorecard

**Data Rows:** 13 (rows 3–15) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Compliance_Area | 35 |
| B | Target | 12 |
| C | Current | 12 |
| D | Status | 12 |
| E | Trend | 12 |
| F | Owner | 20 |
| G | Notes | 30 |

---

## Sheet 7: Kpi_Tracker

**Data Rows:** 13 (rows 3–15) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | KPI_ID | 10 |
| B | KPI_Name | 40 |
| C | Target | 12 |
| D | Current | 12 |
| E | Prior_Period | 14 |
| F | Trend | 12 |
| G | Status | 12 |
| H | Owner | 20 |
| I | Notes | 30 |

---

## Sheet 8: Trend_Analysis

**Data Rows:** 13 (rows 3–15) | **Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Period | 12 |
| B | Total_NDAs | 12 |
| C | New_Signed | 12 |
| D | Renewed | 12 |
| E | Expired | 12 |
| F | Coverage_% | 12 |
| G | Gaps_Open | 12 |
| H | Gaps_Closed | 12 |
| I | Reviews_Done | 12 |
| J | Status | 12 |
| K | Notes | 35 |

---

## Sheet 9: Approval

**Frozen Panes:** A3

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Approval_Type | 25 |
| B | Approver_Role | 25 |
| C | Approver_Name | 25 |
| D | Signature | 20 |
| E | Date | 14 |
| F | Comments | 35 |

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
