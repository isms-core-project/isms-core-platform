**ISMS-IMP-A.8.17-S4-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Clock Synchronization Compliance Dashboard |
| **Related Policy** | ISMS-POL-A.8.17 (Clock Synchronization Policy) |
| **Purpose** | Provide executive dashboard aggregating S1-S3 findings, showing overall clock synchronization compliance status and metrics |
| **Target Audience** | CISO, Executive Management, ISMS Officers, Auditors, Risk Managers |
| **Assessment Type** | Executive Reporting & Compliance Tracking |
| **Review Cycle** | Monthly or As Required |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original Date] | Initial technical specification for compliance dashboard | ISMS Officer |


---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, technical implementers


> Auto-generated from `generate_a817_4_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.17.D` |
| **Output Filename** | `ISMS-IMP-A.8.17.D_Time_Synchronization_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Time Synchronization Compliance Dashboard |
| **Total Sheets** | 5 (5 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #006100 | 006100 | Dark Green (Pass) |
| #999999 | 999999 | Medium Gray |
| #9C0006 | 9C0006 | Dark Red (Error) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Executive_Summary

**Data Rows:** 999 (rows 2–1000)

### Columns

| Col | Header |
|-----|--------|
| A | Category |
| B | Metric |
| C | Value |
| D | Status |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| A8 | `=ROUND({countif_ext(WB2, ` |  |
| E8 | `=ROUND({countifs_ext(WB2, ` |  |

---

## Sheet 3: Infrastructure_Health

**Data Rows:** 99 (rows 2–100)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `={count_ext(WB1, ` |  |
| EN | `=IF(B{row}>=2,\` |  |
| BN | `={countif_ext(WB1, ` |  |
| EN | `=IF(B{row}=B{row-1},\` |  |

---

## Sheet 4: System_Compliance

**Data Rows:** 999 (rows 2–1000)

### Columns

| Col | Header |
|-----|--------|
| A | Status |
| B | Count |
| C | Percentage |
| D | Rate |
| E | Status |

---

## Sheet 5: Gaps_Action_Items

**Data Rows:** 999 (rows 2–1000)

### Columns

| Col | Header |
|-----|--------|
| A | Gap Type |
| B | Count |
| C | Severity |
| D | Action Required |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=SUM(B{row-6}:B{row-1})` |  |

---

**END OF SPECIFICATION**

---

*"Time is the wisest counselor of all."*
— Pericles

<!-- QA_VERIFIED: 2026-02-06 -->
