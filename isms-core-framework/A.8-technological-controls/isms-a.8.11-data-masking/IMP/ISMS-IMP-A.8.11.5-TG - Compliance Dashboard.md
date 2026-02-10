<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.11.5-TG:framework:TG:a.8.11.5 -->
**ISMS-IMP-A.8.11.5-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Master Compliance Dashboard & Consolidation |
| **Related Policy** | ISMS-POL-A.8.11 (All Sections) |
| **Purpose** | Consolidate all assessment domains into executive-level compliance dashboard |
| **Target Audience** | CISO, DPO, Security Managers, Compliance Officers |
| **Review Cycle** | Monthly or After Major Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification | ISMS Implementation Team |

---


> Auto-generated from `generate_a811_5_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.11.5` |
| **Output Filename** | `ISMS-IMP-A.8.11.5_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance Dashboard |
| **Total Sheets** | 21 (21 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #0000FF | 0000FF | Custom |
| #002060 | 002060 | Custom |
| #003366 | 003366 | Dark Blue (Headers) |
| #006100 | 006100 | Dark Green (Pass) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #666666 | 666666 | Dark Gray (Secondary Text) |
| #9C0006 | 9C0006 | Dark Red (Error) |
| #9C5700 | 9C5700 | Custom |
| #B4C7E7 | B4C7E7 | Light Blue (Planned/Info) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #F2F2F2 | F2F2F2 | Very Light Gray (Protected/Alternating) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions_Legend

---

## Sheet 2: Executive_Summary

---

## Sheet 3: Domain_1_Summary

---

## Sheet 4: Domain_2_Summary

---

## Sheet 5: Domain_3_Summary

---

## Sheet 6: Domain_4_Summary

---

## Sheet 7: Consolidated_Gap_Analysis

---

## Sheet 8: Risk_Register

---

## Sheet 9: Remediation_Roadmap

---

## Sheet 10: Evidence_Master_Index

---

## Sheet 11: KPI_Dashboard

---

## Sheet 12: CISO_DPO_Approval

---

## Sheet 13: Comprehensive_Instructions

**Frozen Panes:** A3

---

## Sheet 14: Comprehensive_Executive_Summary

**Data Rows:** 6 (rows 7–12) | **Frozen Panes:** A4

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIFS(Risk_Register!$B:$B,\` | Unmasked Environments |

---

## Sheet 15: Comprehensive_Domain_Summary

**Data Rows:** 15 (rows 5–19) | **Frozen Panes:** A6

---

## Sheet 16: Comprehensive_Gap_Analysis

**Frozen Panes:** A4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 12 |
| B | Domain | 15 |
| C | Gap Category | 20 |
| D | Gap Description | 40 |
| E | Current State | 30 |
| F | Target State | 30 |
| G | Risk Level | 12 |
| H | Business Impact | 35 |
| I | Remediation Action | 40 |
| J | Owner | 20 |
| K | Target Date | 15 |
| L | Status | 15 |
| M | Dependencies | 25 |
| N | Evidence ID | 15 |

---

## Sheet 17: Comprehensive_Risk_Register

**Frozen Panes:** A4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Risk ID | 12 |
| B | Risk Category | 22 |
| C | Risk Description | 45 |
| D | Affected Domain | 15 |
| E | Likelihood (1-5) | 14 |
| F | Impact (1-5) | 13 |
| G | Risk Score | 12 |
| H | Risk Level | 12 |
| I | Mitigation Strategy | 45 |
| J | Owner | 20 |
| K | Target Date | 15 |
| L | Status | 15 |
| M | Residual Risk | 15 |
| N | Residual Score | 14 |
| O | Notes | 30 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| GN | `=E{row}*F{row}` |  |
| HN | `=IF(G{row}>=15,` |  |
| GN | `=IF(AND(E{row}<>\` |  |
| HN | `=IF(G{row}=` |  |

---

## Sheet 18: Comprehensive_Remediation_Roadmap

**Frozen Panes:** A4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Action ID | 12 |
| B | Priority | 14 |
| C | Action Description | 45 |
| D | Related Gap/Risk | 18 |
| E | Domain | 12 |
| F | Owner | 20 |
| G | Start Date | 15 |
| H | Target Date | 15 |
| I | Status | 16 |
| J | % Complete | 12 |
| K | Effort (Days) | 12 |
| L | Dependencies | 30 |
| M | Success Criteria | 35 |
| N | Notes | 30 |

---

## Sheet 19: Comprehensive_Evidence_Index

**Data Rows:** 100 (rows 5–104) | **Frozen Panes:** A4

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 15 |
| B | Domain | 15 |
| C | Evidence Type | 22 |
| D | Description | 40 |
| E | Related Assessment | 25 |
| F | Document Name/Link | 35 |
| G | Date Created | 15 |
| H | Owner | 20 |
| I | Retention Period | 18 |
| J | Location | 30 |

---

## Sheet 20: Comprehensive_Kpi_Dashboard

**Frozen Panes:** A6

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTIFS(Domain_3_Summary!$L:$L,\` | Exception Count (Total) |
| — | `=COUNTIF(Consolidated_Gap_Analysis!$G:$G,\` | High-Risk Gaps |
| — | `=COUNTIF(Consolidated_Gap_Analysis!$L:$L,\` | Gaps Remediated % |
| — | `=COUNTIF(Domain_4_Summary!$L:$L,\` | Failed Tests Remediated |
| — | `=COUNTA(Evidence_Master_Index!$A:$A)/100*100` | Evidence Documentation Rate |

---

## Sheet 21: Comprehensive_Approval_Signoff

**Frozen Panes:** A4

---

**END OF SPECIFICATION**

---

*"Logic will get you from A to Z; imagination will get you everywhere."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
