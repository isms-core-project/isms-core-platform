**ISMS-IMP-A.5.15-16-18.S1-TG - User Inventory & Lifecycle Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | User Inventory & Identity Lifecycle Compliance |
| **Related Policy** | ISMS-POL-A.5.15-16-18, Section 2.2 (Identity Management Requirements - A.5.16) |
| **Purpose** | Document complete user inventory across all identity systems, assess identity lifecycle compliance (joiner/mover/leaver timeliness), and identify orphaned accounts in a technology-agnostic manner |
| **Target Audience** | IAM Team, HR Team, IT Operations, Security Team, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Monthly (user inventory updates), Quarterly (comprehensive lifecycle assessment) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for User Inventory & Lifecycle assessment workbook | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a515-16-18_1_user_inventory.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.15-16-18.S1` |
| **Output Filename** | `ISMS-IMP-A.5.15-16-18.S1_User_Inventory_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | User Inventory & Lifecycle Compliance Assessment |
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

## Sheet 2: User_Inventory

**Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | User ID | 10 |
| B | Username | 20 |
| C | Full Name | 20 |
| D | Email | 30 |
| E | User Type | 15 |
| F | Department | 15 |
| G | Job Title | 25 |
| H | Manager | 20 |
| I | Hire Date | 12 |
| J | Termination Date | 15 |
| K | Status | 12 |
| L | Last Login | 12 |
| M | Account Created | 12 |
| N | Comments | 30 |

---

## Sheet 3: Employee_Lifecycle

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A7

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | User ID | 10 |
| B | Username | 20 |
| C | Full Name | 20 |
| D | Department | 15 |
| E | Hire Date | 15 |
| F | Provision Date | 18 |
| G | Days to Provision | 15 |
| H | SLA (Days) | 12 |
| I | Compliance Status | 18 |
| J | Notes | 35 |

---

## Sheet 4: Contractor_Lifecycle

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | User ID | 10 |
| B | Username | 22 |
| C | Full Name | 20 |
| D | Department | 15 |
| E | Sponsor | 20 |
| F | Contract Start | 15 |
| G | Contract End | 15 |
| H | Access Expiry | 15 |
| I | Days Remaining | 15 |
| J | Status | 15 |
| K | Compliance | 15 |

---

## Sheet 5: Service_Accounts

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Account ID | 12 |
| B | Account Name | 30 |
| C | Purpose | 25 |
| D | Owner | 20 |
| E | Department | 15 |
| F | Created Date | 15 |
| G | Last Used | 15 |
| H | Privileged | 12 |
| I | Password Rotation | 18 |
| J | Status | 12 |

---

## Sheet 6: Orphaned_Accounts

**Data Rows:** 11 (rows 1–11) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | User ID | 10 |
| B | Username | 20 |
| C | Full Name | 20 |
| D | User Type | 15 |
| E | Department | 15 |
| F | Last Login | 15 |
| G | Status | 12 |
| H | Orphan Reason | 40 |
| I | Detected Date | 15 |
| J | Remediation Status | 18 |
| K | Notes | 30 |

---

## Sheet 7: Lifecycle_Metrics

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

## Sheet 8: Gap_Analysis

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 10 |
| B | Category | 18 |
| C | Description | 40 |
| D | Risk Level | 12 |
| E | Affected Users | 15 |
| F | Root Cause | 30 |
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
| H | Notes | 40 |

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

*"I learned very early the difference between knowing the name of something and knowing something."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
