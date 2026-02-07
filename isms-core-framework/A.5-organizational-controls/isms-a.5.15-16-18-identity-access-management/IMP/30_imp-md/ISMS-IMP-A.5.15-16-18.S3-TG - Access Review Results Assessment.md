**ISMS-IMP-A.5.15-16-18.S3-TG - Access Review Results Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Access Review Results & Recertification Compliance |
| **Related Policy** | ISMS-POL-A.5.15-16-18, Section 2.3.4 (Access Review and Recertification Requirements) |
| **Purpose** | Document access review execution, track review completion rates, assess reviewer accountability, and verify access removal for findings in a technology-agnostic manner |
| **Target Audience** | Managers, System Owners, Security Team, IAM Team, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Quarterly (review cycle completion), Monthly (tracking progress) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Access Review Results assessment workbook | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a515-16-18_3_access_review_results.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.15-16-18.S3` |
| **Output Filename** | `ISMS-IMP-A.5.15-16-18.S3_Access_Review_Results_YYYYMMDD.xlsx` |
| **Workbook Title** | Access Review Results Assessment |
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

**Data Rows:** 3 (rows 1–3)

### Columns

| Col | Header |
|-----|--------|
| A | Sheet |
| B | Purpose |
| C | Key Metrics |

---

## Sheet 2: Review_Schedule

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Review ID | 12 |
| B | System/Application | 30 |
| C | Criticality | 12 |
| D | Review Period | 15 |
| E | Frequency | 15 |
| F | Reviewer | 20 |
| G | Reviewer Role | 22 |
| H | Due Date | 12 |
| I | Est. Users | 12 |
| J | Status | 15 |

---

## Sheet 3: Review_Completion

**Data Rows:** 11 (rows 1–11) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Review ID | 12 |
| B | System | 28 |
| C | Review Period | 15 |
| D | Reviewer | 20 |
| E | Due Date | 12 |
| F | Start Date | 12 |
| G | Completion Date | 15 |
| H | Days to Complete | 15 |
| I | Users Reviewed | 15 |
| J | Access Confirmed | 15 |
| K | Access Removed | 15 |
| L | Status | 15 |

---

## Sheet 4: Review_Findings

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Finding ID | 12 |
| B | Review ID | 12 |
| C | System | 20 |
| D | Username | 15 |
| E | Access Level | 15 |
| F | Action | 20 |
| G | Reason | 45 |
| H | Priority | 10 |
| I | Completion Date | 15 |
| J | Days to Remediate | 18 |
| K | Status | 15 |

---

## Sheet 5: Overdue_Reviews

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Review ID | 12 |
| B | System | 28 |
| C | Criticality | 12 |
| D | Reviewer | 20 |
| E | Due Date | 12 |
| F | Days Overdue | 15 |
| G | Escalation Level | 20 |
| H | Escalation Date | 15 |
| I | Escalated To | 30 |
| J | Status | 12 |

---

## Sheet 6: Reviewer_Performance

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Reviewer Name | 20 |
| B | Role | 22 |
| C | Department | 15 |
| D | Total Reviews | 15 |
| E | Completed | 12 |
| F | Overdue | 12 |
| G | Completion Rate | 18 |
| H | Avg Days to Complete | 20 |
| I | Performance | 20 |
| J | Status | 15 |

---

## Sheet 7: Review_Metrics

**Data Rows:** 6 (rows 1–6)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Metric | 30 |
| B | Target | 15 |
| C | Actual | 15 |
| D | Status | 18 |
| E | Gap | 10 |
| F | Comments | 50 |

---

## Sheet 8: Gap_Analysis

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 10 |
| B | Category | 20 |
| C | Description | 40 |
| D | Risk Level | 12 |
| E | Affected Items | 15 |
| F | Root Cause | 40 |
| G | Remediation Plan | 40 |
| H | Owner | 18 |
| I | Due Date | 12 |
| J | Status | 15 |

---

## Sheet 9: Evidence_Register

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

## Sheet 10: Approval_Sign_Off

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Approval Level | 25 |
| B | Role | 20 |
| C | Name | 25 |
| D | Signature | 20 |
| E | Date | 15 |
| F | Status | 15 |

---

**END OF SPECIFICATION**

---

*"Study hard what interests you the most in the most undisciplined, irreverent and original manner possible."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
