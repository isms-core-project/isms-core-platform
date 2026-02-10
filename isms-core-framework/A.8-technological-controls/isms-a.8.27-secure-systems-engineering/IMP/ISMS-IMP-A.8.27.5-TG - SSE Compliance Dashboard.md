<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.27.5-TG:framework:TG:a.8.27.5 -->
**ISMS-IMP-A.8.27.5-TG - SSE Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Secure Systems Engineering Compliance Dashboard |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.5-TG |
| **Assessment Domain** | Domain 5 - Consolidated Dashboard |
| **Related Policy** | ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Security Architect |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Architect | Initial dashboard specification |

**Review Cycle**: Quarterly (aligned with ISMS reporting)
**Next Review Date**: [Effective Date + 3 months]

**Related Documents**:

- ISMS-POL-A.8.27 (Secure System Architecture and Engineering Principles)
- ISMS-IMP-A.8.27.1 (Security Architecture Review Process)
- ISMS-IMP-A.8.27.2 (Threat Modelling Methodology)
- ISMS-IMP-A.8.27.3 (Secure Architecture Pattern Catalogue)
- ISMS-IMP-A.8.27.4 (Zero Trust Implementation Assessment)

---

# Technical Specification


> Auto-generated from `generate_a827_5_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.27.5` |
| **Output Filename** | `ISMS-IMP-A.8.27.5_SSE_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | SSE Compliance Dashboard |
| **Total Sheets** | 8 (8 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #1F4E79 | header_bg | Custom |
| #2E75B6 | subheader_bg | Custom |
| #2ECC71 | green | Custom |
| #E2EFDA | input_cell | Pale Green (Success Background) |
| #E74C3C | red | Custom |
| #F39C12 | amber | Custom |
| #FFF2CC | formula_cell | Cream (Input Alt) |

## Sheet 1: Instructions

---

## Sheet 2: Executive_Summary

**Data Rows:** 7 (rows 4–10)

### Columns

| Col | Header |
|-----|--------|
| A | Domain |
| B | Name |
| C | Score |
| D | Status |
| E | Gaps |
| F | Trend |

---

## Sheet 3: Domain_Scores

**Data Rows:** 9 (rows 1–9)

### Columns

| Col | Header |
|-----|--------|
| A | Domain |
| B | Name |
| C | Assessment Date |
| D | Compliance Score |
| E | Gap Count |
| F | High Risk |
| G | Status |
| H | Trend |
| I | Next Assessment |

---

## Sheet 4: Zero_Trust_Radar

**Data Rows:** 7 (rows 4–10)

### Columns

| Col | Header |
|-----|--------|
| A | Pillar |
| B | Current Level |
| C | Current Score |
| D | Target Level |
| E | Target Score |
| F | Gap |
| G | Priority |

---

## Sheet 5: Gap_Consolidation

**Data Rows:** 50 (rows 4–53)

### Columns

| Col | Header |
|-----|--------|
| A | Gap-ID |
| B | Source |
| C | Description |
| D | Risk |
| E | Remediation |
| F | Owner |
| G | Due Date |
| H | Status |
| I | Days Open |
| J | Overdue |

---

## Sheet 6: Trend_Analysis

**Data Rows:** 8 (rows 1–8)

### Columns

| Col | Header |
|-----|--------|
| A | Period |
| B | Overall Score |
| C | Domain 1 |
| D | Domain 2 |
| E | Domain 3 |
| F | Domain 4 |
| G | Open Gaps |
| H | High Gaps Closed |

---

## Sheet 7: Audit_Evidence

**Data Rows:** 7 (rows 1–7)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence-ID |
| B | Domain |
| C | Description |
| D | Location |
| E | Date |
| F | Status |
| G | Audit Use |

---

## Sheet 8: Action_Tracker

**Data Rows:** 30 (rows 4–33)

### Columns

| Col | Header |
|-----|--------|
| A | Action-ID |
| B | Gap-ID |
| C | Action |
| D | Owner |
| E | Due Date |
| F | Status |
| G | Completion Date |
| H | Evidence |

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed. What gets reported gets improved."*
— Peter Drucker

<!-- QA_VERIFIED: [Date] -->
