**ISMS-IMP-A.5.17.4-TG - Compliance and Audit Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.17

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.17.4-TG |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.17 (Authentication Information) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.17 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.17 (Authentication Information Policy)
- ISMS-IMP-A.5.17.1 (Password Policy Implementation Guide)
- ISMS-IMP-A.5.17.2 (MFA Deployment Assessment)
- ISMS-IMP-A.5.17.3 (Authentication Management Procedures)
- ISMS-POL-A.5.24-28 (Incident Management)

---

# Technical Specification


> Auto-generated from `generate_a517_4_compliance_audit_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.17.4` |
| **Output Filename** | `ISMS-IMP-A.5.17.4_Compliance_and_Audit_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance and Audit Dashboard |
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
| A | Control Area |
| B | Total Requirements |
| C | Compliant |
| D | Non-Compliant |
| E | % Compliant |

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
| E | Current |
| F | Status |
| G | Trend |
| H | Owner |
| I | Notes |

---

## Sheet 4: Authentication_Events

**Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Event Category |
| B | This Period |
| C | Previous Period |
| D | Change |
| E | Threshold |
| F | Alert Status |
| G | Investigation |
| H | Notes |

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
| E | Affected Area |
| F | Severity |
| G | Recommendation |
| H | Owner |
| I | Due Date |
| J | Status |
| K | Notes |

---

## Sheet 6: Remediation_Tracker

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Item ID |
| B | Source |
| C | Description |
| D | Priority |
| E | Remediation Plan |
| F | Owner |
| G | Start Date |
| H | Target Date |
| I | Status |
| J | Notes |

---

## Sheet 7: Evidence_Register

**Data Rows:** 8 (rows 1–8) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Evidence Type |
| C | Description |
| D | Related Section |
| E | Location/Link |
| F | Date |
| G | Collected By |
| H | Status |

---

## Sheet 8: Approval_SignOff

**Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Role |
| B | Name |
| C | Signature |
| D | Date |
| E | Status |
| F | Comments |

---

## Sheet 9: Header_Row

---

## Sheet 10: Metric_Box

---

**END OF SPECIFICATION**

---

*"The only secure password is one you can't remember."*
— Troy Hunt

<!-- QA_VERIFIED: 2026-02-06 -->
