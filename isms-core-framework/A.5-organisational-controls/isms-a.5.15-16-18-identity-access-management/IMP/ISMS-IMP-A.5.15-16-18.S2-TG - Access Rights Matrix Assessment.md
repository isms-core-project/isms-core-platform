<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.15-16-18.S2-TG:framework:TG:a.5.15-16-18 -->
**ISMS-IMP-A.5.15-16-18.S2-TG - Access Rights Matrix Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Access Rights Matrix & Documentation |
| **Related Policy** | ISMS-POL-A.5.15-16-18, Section 2.3 (Access Rights Management Requirements - A.5.18) |
| **Purpose** | Document complete access rights matrix mapping users to systems/applications/data, assess access documentation completeness, and verify business justification in a technology-agnostic manner |
| **Target Audience** | IAM Team, System Owners, IT Operations, Security Team, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Monthly (access rights updates), Quarterly (comprehensive access audit) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Access Rights Matrix assessment workbook | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a515-16-18_2_access_rights_matrix.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.15-16-18.S2` |
| **Output Filename** | `ISMS-IMP-A.5.15-16-18.S2_Access_Rights_Matrix_YYYYMMDD.xlsx` |
| **Workbook Title** | Access Rights Matrix Assessment |
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

## Sheet 2: Access_Matrix

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | User ID | 10 |
| B | Username | 18 |
| C | Full Name | 20 |
| D | Department | 15 |
| E | System/Application | 30 |
| F | Access Level | 15 |
| G | Access Type | 15 |
| H | Granted Date | 12 |
| I | Granted By | 18 |
| J | Last Used | 12 |
| K | Status | 15 |

---

## Sheet 3: Role_Assignments

**Data Rows:** 7 (rows 1–7) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | User ID | 10 |
| B | Username | 18 |
| C | Full Name | 20 |
| D | Department | 15 |
| E | Assigned Role | 25 |
| F | Assignment Date | 15 |
| G | Assignment Type | 18 |
| H | Status | 12 |

---

## Sheet 4: Group_Memberships

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Group Name | 35 |
| B | Group Type | 15 |
| C | Purpose | 40 |
| D | Owner | 18 |
| E | Member Count | 15 |
| F | Created Date | 15 |
| G | Last Modified | 15 |
| H | Nested Groups | 15 |
| I | Review Frequency | 18 |
| J | Status | 12 |

---

## Sheet 5: Privileged_Access

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | User ID | 10 |
| B | Username | 18 |
| C | Full Name | 20 |
| D | Department | 15 |
| E | System | 25 |
| F | Privilege Level | 20 |
| G | Granted Date | 12 |
| H | Business Justification | 35 |
| I | Approved By | 18 |
| J | Last Review | 12 |
| K | Status | 18 |

---

## Sheet 6: Access_Documentation

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Access ID | 12 |
| B | Username | 18 |
| C | System | 30 |
| D | Access Level | 15 |
| E | Granted Date | 12 |
| F | Business Justification | 50 |
| G | Approver | 18 |
| H | Approval Date | 15 |
| I | Documentation Quality | 20 |
| J | Status | 15 |

---

## Sheet 7: Coverage_Analysis

**Data Rows:** 8 (rows 1–8) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | System/Application | 30 |
| B | Criticality | 15 |
| C | Total Users | 12 |
| D | Read Access | 15 |
| E | Write Access | 15 |
| F | Admin Access | 15 |
| G | RBAC Adoption | 18 |
| H | Review Frequency | 18 |

---

## Sheet 8: Gap_Analysis

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A5

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 10 |
| B | Category | 18 |
| C | Description | 45 |
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

*"For a successful technology, reality must take precedence over public relations, for Nature cannot be fooled."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
