<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.9.5-TG:framework:TG:a.8.9.5 -->
**ISMS-IMP-A.8.9.5-TG - Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.9: Configuration Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.9.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Configuration Management Compliance - Consolidated Maturity Dashboard Across All Four Domains |
| **Related Policy** | ISMS-POL-A.8.9 (All Sections - Baseline, Change Control, Monitoring, Hardening) |
| **Purpose** | Provide consolidated executive dashboard of configuration management maturity across all four domains (baseline, change, monitoring, hardening) with aggregated compliance metrics and trend analysis |
| **Target Audience** | CISO, Configuration Manager, IT Leadership, Executive Management, Risk Management, Compliance Officers, Auditors |
| **Assessment Type** | Executive Dashboard & Compliance Reporting |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Configuration Management Compliance Dashboard | ISMS Implementation Team |

---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a89_5_compliance_dashboard.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.9.5` |
| **Output Filename** | `ISMS-IMP-A.8.9.5_Compliance_Dashboard_YYYYMMDD.xlsx` |
| **Workbook Title** | Compliance Dashboard |
| **Total Sheets** | 10 (10 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #375623 | 375623 | Custom |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #70AD47 | 70AD47 | Medium Green (On Track) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D6EAF8 | D6EAF8 | Custom |
| #D8E4F8 | D8E4F8 | Pale Blue (Sub-section) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #ED7D31 | ED7D31 | Custom |
| #FCE4D6 | FCE4D6 | Peach (Warning Alt) |
| #FFC000 | FFC000 | Custom |
| #FFF2CC | FFF2CC | Cream (Input Alt) |

## Sheet 1: Alls

---

## Sheet 2: External_Reference

---

## Sheet 3: Instructions

---

## Sheet 4: Workbook_Integration_Settings

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Domain | 25 |
| B | Document ID | 20 |
| C | Expected Filename | 30 |
| D | Status | 15 |
| E | Last Modified | 20 |
| F | Link Status | 40 |
| A | Domain | — |
| B | Document ID | — |
| C | Expected Filename | — |
| D | Status | — |
| E | Last Modified | — |
| F | Link Status | — |

---

## Sheet 5: Overall_Compliance_Dashboard

---

## Sheet 6: Asset_Compliance_Summary

**Data Rows:** 100 (rows 2–101)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Asset_ID | 12 |
| B | Asset_Name | 30 |
| C | Asset_Type | 25 |
| D | Asset_Tier | 12 |
| E | Asset_Owner | 25 |
| F | Baseline_Documented | 18 |
| G | Baseline_Current | 16 |
| H | Change_Compliance | 18 |
| I | Emergency_Changes_30d | 20 |
| J | Monitoring_Coverage | 18 |
| K | Critical_Drift | 14 |
| L | Hardening_Compliance | 20 |
| M | High_Risk_Gaps | 16 |
| N | Overall_Compliance | 18 |
| O | Status | 20 |
| P | Critical_Issues | 16 |
| Q | Primary_Gap_Domain | 20 |
| R | Priority | 12 |
| S | Notes | 40 |

---

## Sheet 7: Gap_Prioritization

**Data Rows:** 150 (rows 2–151)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap_ID | 12 |
| B | Priority_Rank | 12 |
| C | Source_Domain | 20 |
| D | Asset_ID | 12 |
| E | Asset_Name | 25 |
| F | Asset_Tier | 12 |
| G | Gap_Category | 20 |
| H | Gap_Description | 50 |
| I | Gap_Risk_Rating | 16 |
| J | Impact | 40 |
| K | Exploitation_Likelihood | 20 |
| L | Risk_Score | 12 |
| M | Owner | 25 |
| N | Strategy | 30 |
| O | Target_Date | 15 |
| P | Days_Until | 12 |
| Q | Status | 18 |
| R | Quick_Win | 12 |
| S | Cross_Domain | 14 |
| T | Notes | 40 |

---

## Sheet 8: Trend_Analysis

**Data Rows:** 20 (rows 1–20)

---

## Sheet 9: Evidence_Register

**Data Rows:** 100 (rows 2–101)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence_ID | 14 |
| B | Source_Domain | 22 |
| C | Source_Document | 20 |
| D | Source_Evidence_ID | 18 |
| E | Evidence_Type | 25 |
| F | Evidence_Description | 50 |
| G | Related_Control_Area | 25 |
| H | Collection_Date | 15 |
| I | Evidence_Location | 40 |
| J | Evidence_Status | 15 |
| K | Verification_Status | 18 |
| L | Audit_Reference | 20 |
| M | Notes | 40 |

---

## Sheet 10: Approval_Sign_Off

**Data Rows:** 5 (rows 12–16)

---

**END OF SPECIFICATION**

---

*"In the new paradigm, the properties of the parts can be understood only from the dynamics of the whole."*
— Fritjof Capra

<!-- QA_VERIFIED: 2026-02-06 -->
