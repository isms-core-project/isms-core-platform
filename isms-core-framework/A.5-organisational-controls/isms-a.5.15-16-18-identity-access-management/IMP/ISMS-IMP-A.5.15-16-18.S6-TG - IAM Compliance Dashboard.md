<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.15-16-18.S6-TG:framework:TG:a.5.15-16-18 -->
**ISMS-IMP-A.5.15-16-18.S6-TG - IAM Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.5.15, A.5.16, A.5.18: Identity and Access Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S6-TG |
| **Version** | 1.0 |
| **Assessment Area** | IAM Governance Compliance Dashboard - Consolidated Metrics |
| **Related Policy** | ISMS-POL-A.5.15-16-18 (All Sections) |
| **Purpose** | Provide consolidated executive dashboard for IAM compliance across all assessment domains (S1-S5), enabling governance oversight, audit readiness, and continuous improvement tracking |
| **Target Audience** | CISO, Security Management, Internal Audit, Executive Leadership, Board/Audit Committee, External Auditors |
| **Assessment Type** | Executive Dashboard & Governance Reporting |
| **Review Cycle** | Monthly (metric refresh), Quarterly (executive review), Annually (comprehensive audit) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for IAM Compliance Dashboard - consolidates S1-S5 metrics | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a515-16-18_6_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.15-16-18.S6` |
| **Output Filename** | `ISMS-IMP-A.5.15-16-18.S6_IAM_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | IAM Compliance Dashboard |
| **Total Sheets** | 9 (9 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #002060 | 002060 | Custom |
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |

## Sheet 1: Instructions & Legend

**Data Rows:** 3 (rows 1–3)

---

## Sheet 2: Executive_Summary

**Data Rows:** 4 (rows 1–4)

### Columns

| Col | Header |
|-----|--------|
| A | Domain |
| B | Score |
| C | Target |
| D | Gap |
| E | Status |

---

## Sheet 3: Domain_Compliance

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Domain ID | 12 |
| B | Domain Name | 30 |
| C | Score | 10 |
| D | Target | 10 |
| E | Gap | 10 |
| F | Status | 15 |
| G | Trend | 12 |
| H | Key Metrics | 50 |
| I | Findings Summary | 50 |

---

## Sheet 4: Gap_Analysis

**Data Rows:** 12 (rows 1–12) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 10 |
| B | Source | 8 |
| C | Category | 18 |
| D | Description | 35 |
| E | Risk Level | 12 |
| F | Affected | 10 |
| G | Root Cause | 30 |
| H | Remediation Plan | 35 |
| I | Owner | 15 |
| J | Due Date | 12 |
| K | Status | 12 |
| L | Notes | 25 |

---

## Sheet 5: KPI_Dashboard

**Data Rows:** 8 (rows 1–8) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | KPI ID | 10 |
| B | KPI Name | 35 |
| C | Target | 12 |
| D | Actual | 12 |
| E | Gap | 10 |
| F | Status | 15 |
| G | Trend | 12 |
| H | Source | 15 |

---

## Sheet 6: Evidence_Summary

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 12 |
| B | Source | 8 |
| C | ISO Requirement | 15 |
| D | Requirement Area | 25 |
| E | Evidence Type | 18 |
| F | Evidence Location | 35 |
| G | Collection Date | 15 |
| H | Completeness | 15 |
| I | Verified By | 18 |

---

## Sheet 7: Trend_Analysis

**Data Rows:** 7 (rows 1–7) | **Frozen Panes:** A6

### Columns

| Col | Header |
|-----|--------|
| A | Period |
| B | Composite |
| C | S1 |
| D | S2 |
| E | S3 |
| F | S4 |
| G | S5 |

---

## Sheet 8: Certification_Readiness

**Data Rows:** 7 (rows 1–7) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Control | 12 |
| B | Control Name | 25 |
| C | Source Assessments | 15 |
| D | Evidence Status | 15 |
| E | Gap Status | 18 |
| F | Readiness | 15 |
| G | Audit Blockers | 35 |

---

## Sheet 9: Approval_Sign_Off

**Data Rows:** 6 (rows 1–6)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Approval Level | 25 |
| B | Role | 20 |
| C | Name | 20 |
| D | Signature | 20 |
| E | Date | 15 |
| F | Status | 15 |

---

**END OF SPECIFICATION**

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
