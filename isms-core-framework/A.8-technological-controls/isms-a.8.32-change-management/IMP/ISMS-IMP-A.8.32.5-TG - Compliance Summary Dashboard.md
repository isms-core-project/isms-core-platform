<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.32.5-TG:framework:TG:a.8.32.5 -->
**ISMS-IMP-A.8.32.5-TG - Compliance Summary Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.32.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Compliance Dashboard & Consolidation |
| **Related Policy** | ISMS-POL-A.8.32 (All Sections) |
| **Purpose** | Consolidate all domain assessments into executive compliance view with scoring, gap analysis, and audit readiness certification |
| **Target Audience** | CISO, Executive Management, Board of Directors, Internal/External Auditors, ISO 27001 Certification Bodies, Workbook Developers |
| **Assessment Type** | Executive Dashboard & Consolidation |
| **Review Cycle** | Quarterly (synchronized with domain assessments) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial technical specification for Change Management Compliance Dashboard workbook | ISMS Implementation Team |


---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a832_5_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.32.5` |
| **Output Filename** | `ISMS-IMP-A.8.32.5_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance Dashboard |
| **Total Sheets** | 13 (13 visible) |
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

## Sheet 1: Executive_Dashboard

---

## Sheet 2: Gap_Analysis

---

## Sheet 3: Risk_Register

---

## Sheet 4: Remediation_Roadmap

---

## Sheet 5: KPIs_Metrics

---

## Sheet 6: Evidence_Register

---

## Sheet 7: Audit_Readiness

---

## Sheet 8: CISO_Certification

---

## Sheet 9: Kpis_Metrics

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

## Sheet 10: Ciso_Certification

---

## Sheet 11: Action_Items

**Data Rows:** 200 (rows 20–219)

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

---

## Sheet 12: Audit_Log

**Data Rows:** 100 (rows 20–119)

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

---

## Sheet 13: Approval_Signoff

---

**END OF SPECIFICATION**

---

*"Zero-knowledge proofs are perhaps the most powerful tool we have in cryptography."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
