**ISMS-IMP-A.5.9.5-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Executive Compliance Dashboard & Consolidated Metrics |
| **Related Policy** | ISMS-POL-A.5.9, Section 3 (Assessment Methodology), Requirement A.5.9-R9 (Reporting) |
| **Purpose** | Consolidate all A.5.9 assessment data into executive dashboard for management reporting and compliance tracking |
| **Target Audience** | CISO, Information Security Manager, Executive Management, Auditors, Board of Directors |
| **Assessment Type** | Consolidation & Executive Reporting |
| **Review Cycle** | Quarterly (after all 4 assessments completed) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial dashboard specification consolidating 4 assessment workbooks | ISMS Implementation Team |


---
# Technical Specification
**Audience:** Dashboard developers (Python/Excel script maintainers)


> Auto-generated from `generate_a59_5_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.9.5` |
| **Output Filename** | `ISMS-IMP-A.5.9.5_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance Dashboard |
| **Total Sheets** | 8 (8 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | header_bg | Dark Blue (Headers) |
| #006100 | green_dark | Dark Green (Pass) |
| #4472C4 | section_bg | Medium Blue (Sub-headers) |
| #9C0006 | red_dark | Dark Red (Error) |
| #9C5700 | yellow_dark | Custom |
| #C6EFCE | green_light | Light Green (Compliant/Pass) |
| #D9D9D9 | gray_light | Light Gray (Column Headers) |
| #FFC7CE | red_light | Light Red (Non-Compliant/Fail) |
| #FFEB9C | yellow_light | Light Yellow/Amber (Partial) |

## Sheet 1: Executive_Summary

**Data Rows:** 3 (rows 27–29)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IF(B{row}>={target},` |  |

---

## Sheet 2: Compliance_Scorecard

**Data Rows:** 4 (rows 6–9)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| DN | `=B{row}*{weight}/100` |  |
| FN | `=B{row}-{target}/100` |  |
| GN | `=IF(B{row}>={target}/100,` |  |
| BN | `=SUM(D6:D9)` |  |
| BN | `=B{overall_row-2}-0.95` |  |
| BN | `=IF(B{overall_row-3}>=0.95,` |  |

---

## Sheet 3: Discovery_Metrics

---

## Sheet 4: Maintenance_Metrics

---

## Sheet 5: Quality_Metrics

---

## Sheet 6: Accountability_Metrics

---

## Sheet 7: Trending_Analysis

### Columns

| Col | Header |
|-----|--------|
| A | Assessment Domain |
| B | Q-4 |
| C | Q-3 |
| D | Q-2 |
| E | Q-1 |
| F | Current |
| G | Trend |
| H | Forecast Q+1 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| GN | `=IF(AND(E{row}<>` |  |

---

## Sheet 8: Action_Register

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Action ID | 15 |
| B | Assessment Domain | 20 |
| C | Gap Description | 40 |
| D | Severity | 12 |
| E | Impact | 12 |
| F | Effort | 12 |
| G | Audit Relevance | 15 |
| H | Priority Score | 15 |
| I | Priority | 15 |
| J | Owner | 20 |
| K | Target Date | 15 |
| L | Status | 15 |
| M | Notes | 30 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| HN | `=IF(OR(D{row}=` |  |
| IN | `=IF(H{row}=` |  |

---

**END OF SPECIFICATION**

---

*"The optimist thinks this is the best of all possible worlds. The pessimist fears it is true."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->
