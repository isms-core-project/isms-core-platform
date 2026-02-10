<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.15-16-18.S4-TG:framework:TG:a.5.15-16-18 -->
**ISMS-IMP-A.5.15-16-18.S4-TG - Role Definition & SoD Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Role-Based Access Control (RBAC) Maturity & Segregation of Duties (SoD) Compliance |
| **Related Policy** | ISMS-POL-A.5.15-16-18, Section 2.3 (Role Definition & RBAC - A.5.18), Section 2.1.4 (Segregation of Duties - A.5.15) |
| **Purpose** | Assess RBAC adoption, verify role-based access implementation, detect segregation of duties violations, and identify role governance gaps |
| **Target Audience** | IAM Team, Security Operations, Access Control Administrators, Internal Audit, Compliance Officers |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Quarterly (Critical Roles), Semi-Annual (All Roles), Annual (Comprehensive Role Governance Review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Role Definition & SoD Compliance assessment workbook | ISMS Implementation Team |

---
# Technical Specification


> Auto-generated from `generate_a515-16-18_4_role_compliance.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.15-16-18.S4` |
| **Output Filename** | `ISMS-IMP-A.5.15-16-18.S4_Role_Compliance_SoD_YYYYMMDD.xlsx` |
| **Workbook Title** | Role Compliance & Segregation of Duties Assessment |
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
| #FF6600 | FF6600 | Custom |
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

## Sheet 2: Role_Catalog

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Role ID | 12 |
| B | Role Name | 25 |
| C | Department | 15 |
| D | Description | 40 |
| E | Systems/Access | 40 |
| F | User Count | 12 |
| G | Privileged | 12 |
| H | Last Review | 12 |
| I | Owner | 20 |
| J | Status | 12 |

---

## Sheet 3: Role_Assignments

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A6

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
| H | Role Appropriate | 18 |
| I | Verified By | 20 |
| J | Status | 12 |

---

## Sheet 4: Direct_Access_Users

**Data Rows:** 9 (rows 1–9) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | User ID | 10 |
| B | Username | 18 |
| C | Full Name | 20 |
| D | Department | 15 |
| E | System | 20 |
| F | Access Level | 15 |
| G | Granted Date | 12 |
| H | Justification | 40 |
| I | Migration Plan | 35 |
| J | Status | 18 |

---

## Sheet 5: SoD_Matrix

**Data Rows:** 7 (rows 1–7) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Conflict ID | 12 |
| B | Role A | 22 |
| C | Role B | 22 |
| D | Risk Level | 12 |
| E | Description | 45 |
| F | Rationale | 45 |
| G | Compensating Controls | 50 |
| H | Status | 12 |

---

## Sheet 6: SoD_Violations

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Violation ID | 12 |
| B | User ID | 10 |
| C | Username | 18 |
| D | Conflict ID | 12 |
| E | Role A | 22 |
| F | Role B | 22 |
| G | Risk Level | 12 |
| H | Detected Date | 15 |
| I | Remediation Plan | 45 |
| J | Due Date | 12 |
| K | Status | 22 |

---

## Sheet 7: RBAC_Metrics

**Data Rows:** 6 (rows 1–6)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Metric | 30 |
| B | Target | 15 |
| C | Actual | 15 |
| D | Status | 18 |
| E | Gap | 10 |
| F | Comments | 55 |

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
| E | Affected Items | 15 |
| F | Root Cause | 40 |
| G | Remediation Plan | 50 |
| H | Owner | 20 |
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
| C | Evidence Type | 22 |
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

*"It doesn't matter how beautiful your theory is, it doesn't matter how smart you are. If it doesn't agree with experiment, it's wrong."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
