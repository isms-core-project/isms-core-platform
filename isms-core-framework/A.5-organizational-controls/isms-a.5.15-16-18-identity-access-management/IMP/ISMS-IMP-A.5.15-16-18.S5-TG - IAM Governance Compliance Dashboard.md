<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.15-16-18.S5-TG:framework:TG:a.5.15-16-18 -->
**ISMS-IMP-A.5.15-16-18.S5-TG - Lifecycle Compliance Detailed Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.16: Identity Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Lifecycle Compliance Detailed Assessment - Joiner/Mover/Leaver Analysis |
| **Related Policy** | ISMS-POL-A.5.15-16-18 (All Sections) |
| **Purpose** | Detailed analysis of identity lifecycle compliance across joiner/mover/leaver events with SLA tracking and HR integration status |
| **Target Audience** | IAM Team, HR Operations, IT Operations, Security Operations, Internal Audit |
| **Assessment Type** | Lifecycle Event Analysis |
| **Review Cycle** | Monthly (Lifecycle Review), Quarterly (Process Review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Lifecycle Compliance Detailed Assessment | ISMS Implementation Team |

---
# Technical Specification


> Auto-generated from `generate_a515-16-18_5_lifecycle_compliance.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.15-16-18.S5` |
| **Output Filename** | `ISMS-IMP-A.5.15-16-18.S5_Lifecycle_Compliance_Detailed_YYYYMMDD.xlsx` |
| **Workbook Title** | Lifecycle Compliance Detailed Assessment |
| **Total Sheets** | 10 (10 visible) |

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

---

## Sheet 2: Joiner_Events

**Data Rows:** 12 (rows 1–12) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Event ID | 12 |
| B | User ID | 10 |
| C | Username | 18 |
| D | Full Name | 20 |
| E | Department | 15 |
| F | Job Title | 18 |
| G | Hire Date | 12 |
| H | Provision Date | 15 |
| I | Days to Provision | 15 |
| J | SLA | 8 |
| K | Compliance | 15 |
| L | Notes | 30 |

---

## Sheet 3: Mover_Events

**Data Rows:** 12 (rows 1–12) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Event ID | 12 |
| B | User ID | 10 |
| C | Username | 18 |
| D | Full Name | 20 |
| E | Change Type | 20 |
| F | From Dept | 15 |
| G | To Dept | 15 |
| H | Effective Date | 15 |
| I | Access Updated | 15 |
| J | Days to Update | 15 |
| K | Compliance | 15 |
| L | Notes | 35 |

---

## Sheet 4: Leaver_Events

**Data Rows:** 12 (rows 1–12) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Event ID | 12 |
| B | User ID | 10 |
| C | Username | 18 |
| D | Full Name | 20 |
| E | Department | 15 |
| F | Termination Date | 15 |
| G | Account Disabled | 18 |
| H | Hours to Disable | 15 |
| I | SLA | 8 |
| J | Compliance | 15 |
| K | Security Risk | 15 |
| L | Notes | 50 |

---

## Sheet 5: Contractor_Lifecycle

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Contractor ID | 12 |
| B | Username | 22 |
| C | Full Name | 20 |
| D | Sponsor | 20 |
| E | Department | 15 |
| F | Contract Start | 15 |
| G | Contract End | 15 |
| H | Days Remaining | 15 |
| I | Expiration Status | 18 |
| J | Extension Approved | 18 |
| K | Compliance | 15 |

---

## Sheet 6: Orphaned_Remediation

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Account ID | 10 |
| B | Username | 18 |
| C | Account Type | 15 |
| D | Last Login | 15 |
| E | Detection Date | 15 |
| F | Orphan Reason | 45 |
| G | Assigned To | 20 |
| H | Remediation Action | 22 |
| I | Completion Date | 15 |
| J | Days to Remediate | 18 |
| K | Status | 15 |

---

## Sheet 7: Timeliness_Metrics

**Data Rows:** 6 (rows 1–6)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Metric | 35 |
| B | Target | 15 |
| C | Actual | 15 |
| D | Status | 18 |
| E | Gap | 10 |
| F | Comments | 50 |

---

## Sheet 8: HR_Integration

**Data Rows:** 7 (rows 1–7)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Component | 35 |
| B | Status | 18 |
| C | Integration Method | 20 |
| D | Frequency | 15 |
| E | Last Sync | 18 |
| F | Issues | 20 |
| G | Notes | 35 |

---

## Sheet 9: Gap_Analysis

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 10 |
| B | Category | 18 |
| C | Description | 35 |
| D | Risk Level | 12 |
| E | Affected Items | 15 |
| F | Root Cause | 35 |
| G | Remediation Plan | 45 |
| H | Owner | 18 |
| I | Due Date | 12 |
| J | Status | 15 |

---

## Sheet 10: Evidence_Register

**Data Rows:** 8 (rows 1–8) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 12 |
| B | Requirement | 25 |
| C | Evidence Type | 20 |
| D | Evidence Location | 35 |
| E | Collection Date | 18 |
| F | Completeness | 15 |
| G | Reviewed By | 20 |
| H | Notes | 45 |

---

**END OF SPECIFICATION**

---

*"The sum of an infinite series of fractions whose denominators are the squares of the natural numbers is equal to π²/6."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
