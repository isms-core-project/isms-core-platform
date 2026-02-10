<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.14.4-TG:framework:TG:a.5.14.4 -->
**ISMS-IMP-A.5.14.4-TG - Compliance Monitoring Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.14

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.14.4-TG |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.14 (Information Transfer) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.14 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.14 (Information Transfer Policy)
- ISMS-IMP-A.5.14.1 (Transfer Rules and Procedures)
- ISMS-IMP-A.5.14.2 (Channel Security Assessment)
- ISMS-IMP-A.5.14.3 (Transfer Agreements Register)
- ISMS-POL-A.5.24-28 (Incident Management)

---

# Technical Specification


> Auto-generated from `generate_a514_4_compliance_monitoring_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.14.4` |
| **Output Filename** | `ISMS-IMP-A.5.14.4_Compliance_Monitoring_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance Monitoring Dashboard |
| **Total Sheets** | 10 (10 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9E1F2 | D9E1F2 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

**Frozen Panes:** A3

---

## Sheet 2: Executive_Summary

**Data Rows:** 5 (rows 1–5) | **Frozen Panes:** A3

### Columns

| Col | Header |
|-----|--------|
| A | Channel Type |
| B | Assessed |
| C | Compliant |
| D | Partial |
| E | Non-Compliant |

---

## Sheet 3: Compliance_KPIs

**Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | KPI ID |
| B | KPI Name |
| C | Description |
| D | Target |
| E | Current Value |
| F | Status |
| G | Trend |
| H | Owner |
| I | Notes |

---

## Sheet 4: Transfer_Incidents

**Data Rows:** 12 (rows 1–12) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Incident ID |
| B | Date Detected |
| C | Channel Type |
| D | Incident Type |
| E | Severity |
| F | Classification Affected |
| G | Description |
| H | Root Cause |
| I | Corrective Action |
| J | Status |
| K | Closed Date |
| L | Lessons Learned |

---

## Sheet 5: Audit_Findings

**Data Rows:** 11 (rows 1–11) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Finding ID |
| B | Audit Type |
| C | Audit Date |
| D | Finding Description |
| E | Affected Control |
| F | Severity |
| G | Recommendation |
| H | Owner |
| I | Due Date |
| J | Status |
| K | Closure Notes |

---

## Sheet 6: Remediation_Tracker

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Item ID |
| B | Source |
| C | Gap/Finding Description |
| D | Priority |
| E | Remediation Plan |
| F | Owner |
| G | Start Date |
| H | Target Date |
| I | Status |
| J | Progress Notes |

---

## Sheet 7: Evidence_Register

**Data Rows:** 8 (rows 1–8) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Evidence Type |
| C | Description |
| D | Related Item |
| E | Location/Link |
| F | Date Collected |
| G | Collected By |
| H | Status |

---

## Sheet 8: Approval_SignOff

**Frozen Panes:** A4

---

## Sheet 9: Header_Row

---

## Sheet 10: Metric_Box

---

**END OF SPECIFICATION**

---

*"You can't manage what you can't measure."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
