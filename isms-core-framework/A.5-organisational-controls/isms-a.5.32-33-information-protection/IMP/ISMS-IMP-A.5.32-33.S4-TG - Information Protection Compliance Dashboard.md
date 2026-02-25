<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.32-33.S4-TG:framework:TG:a.5.32-33 -->
**ISMS-IMP-A.5.32-33.S4-TG - Information Protection Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.5.32-33: Intellectual Property Rights & Protection of Records

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.32-33.S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Compliance Monitoring for IP Rights and Records Protection |
| **Related Policy** | ISMS-POL-A.5.32-33 (Full Policy) |
| **Purpose** | Provide executive-level visibility into IP protection, records protection, and retention compliance |
| **Target Audience** | CISO, Legal Counsel, Records Manager, Executive Management, Internal Audit, Compliance Officers |
| **Assessment Type** | Executive Reporting & Compliance Monitoring |
| **Review Cycle** | Quarterly or After Significant Changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Information Protection Compliance Dashboard | ISMS Implementation Team |

---


---
# Technical Specification
**Audience:** Workbook Developers, Python/Excel Script Maintainers


> Auto-generated from `generate_a532_33_4_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.32-33.S4` |
| **Output Filename** | `ISMS-IMP-A.5.32-33.S4_Information_Protection_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Information Protection Compliance Dashboard |
| **Total Sheets** | 10 (10 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #1F4E79 | 1F4E79 | Custom |
| #2E75B6 | 2E75B6 | Custom |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D6DCE4 | D6DCE4 | Silver (Neutral) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Executive_Summary

**Data Rows:** 6 (rows 19–24)

---

## Sheet 3: Compliance_Metrics

**Data Rows:** 31 (rows 5–35)

### Columns

| Col | Header |
|-----|--------|
| A | Metric ID |
| B | Category |
| C | Metric Name |
| D | Description |
| E | Target |
| F | Current Value |
| G | Previous Value |
| H | Trend |
| I | Status |
| J | Owner |
| K | Notes |

---

## Sheet 4: Control_Assessment

**Data Rows:** 9 (rows 17–25)

### Columns

| Col | Header |
|-----|--------|
| A | Requirement |
| B | Implementation |
| C | Evidence |
| D | Gap |
| E | Score |
| F | Status |

---

## Sheet 5: Maturity_Assessment

**Data Rows:** 10 (rows 15–24)

---

## Sheet 6: Risk_Register

**Data Rows:** 26 (rows 5–30)

### Columns

| Col | Header |
|-----|--------|
| A | Risk ID |
| B | Risk Description |
| C | Risk Category |
| D | Likelihood |
| E | Impact |
| F | Risk Score |
| G | Current Mitigation |
| H | Residual Risk |
| I | Owner |
| J | Status |
| K | Review Date |

---

## Sheet 7: Remediation_Tracker

**Data Rows:** 46 (rows 5–50)

### Columns

| Col | Header |
|-----|--------|
| A | Action ID |
| B | Source |
| C | Description |
| D | Priority |
| E | Owner |
| F | Due Date |
| G | Progress |
| H | Status |
| I | Blocker |
| J | Notes |

---

## Sheet 8: Trend_Analysis

**Data Rows:** 16 (rows 5–20)

### Columns

| Col | Header |
|-----|--------|
| A | Metric |
| B | Q1 |
| C | Q2 |
| D | Q3 |
| E | Q4 |
| F | YoY Change |
| G | Trend |
| H | Target |
| I | On Track |

---

## Sheet 9: Evidence_Register

**Data Rows:** 46 (rows 5–50)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Description |
| C | Evidence Type |
| D | Related Item |
| E | Storage Location |
| F | Collected Date |
| G | Collected By |
| H | Verification Status |

---

## Sheet 10: Approval

**Data Rows:** 9 (rows 14–22)

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
-- Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
