**ISMS-IMP-A.8.31.2-TG - Environment Access Control Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.31: Separation of Development, Test and Production Environments

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.31.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Environment Access Control & Production Access Restrictions |
| **Related Policy** | ISMS-POL-A.8.31, Section 2.2 (Environment Access Control Requirements) |
| **Purpose** | Document access control implementation, verify production access restrictions (zero developer access), and assess compliance with environment-specific access requirements |
| **Target Audience** | IAM Administrators, IT Operations, Security Engineers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Access Control Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Environment Access Control assessment workbook | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a831_2_environment_access.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.31.2` |
| **Output Filename** | `ISMS-IMP-A.8.31.2_Environment_Access_Control_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Environment Access Control Assessment |
| **Total Sheets** | 19 (19 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions_Legend

---

## Sheet 2: User_Environment_Access_Matrix

---

## Sheet 3: Developer_Production_Access

---

## Sheet 4: Production_Credential_Audit

---

## Sheet 5: Cross_Environment_Access_Log

---

## Sheet 6: Break_Glass_Access_Log

---

## Sheet 7: MFA_Enforcement

---

## Sheet 8: Access_Compliance_Scorecard

---

## Sheet 9: Evidence_Register

---

## Sheet 10: Approval_Sign_Off

---

## Sheet 11: Instructions

---

## Sheet 12: User_Access_Matrix

**Data Rows:** 96 (rows 5–100)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | User ID / Email | 30 |
| B | Role | 25 |
| C | Development Access | 25 |
| D | Testing Access | 25 |
| E | Staging Access | 25 |
| F | Production Access | 25 |
| G | Compliance Status | 20 |
| H | Notes | 40 |

---

## Sheet 13: Developer_Prod_Access

**Data Rows:** 96 (rows 5–100)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Developer ID | 30 |
| B | Production Account/Sub | 30 |
| C | Production Access? | 20 |
| D | Access Type | 25 |
| E | Justification | 40 |
| F | Violation Severity | 20 |
| G | Remediation Action | 40 |

---

## Sheet 14: Cross_Environment_Access

**Data Rows:** 96 (rows 5–100)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Date/Time | 20 |
| B | User ID | 30 |
| C | Source Environment | 20 |
| D | Target Environment | 20 |
| E | Attempted Action | 30 |
| F | Result | 20 |
| G | Alert Generated? | 20 |
| H | Investigation Notes | 40 |

---

## Sheet 15: Breakglass_Access

**Data Rows:** 96 (rows 5–100)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Incident ID | 15 |
| B | Date/Time Activated | 20 |
| C | Developer ID | 30 |
| D | Approved By | 25 |
| E | Reason/Justification | 40 |
| F | Duration (hours) | 15 |
| G | Date/Time Revoked | 20 |
| H | Post-Incident Review | 30 |
| I | Compliance | 20 |
| J | Notes | 40 |

---

## Sheet 16: Mfa_Enforcement

**Data Rows:** 96 (rows 5–100)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | User ID | 30 |
| B | Production Access? | 20 |
| C | MFA Enabled? | 20 |
| D | MFA Type | 25 |
| E | Last MFA Check | 20 |
| F | Compliance | 20 |
| G | Evidence | 40 |

---

## Sheet 17: Compliance_Scorecard

**Data Rows:** 5 (rows 1–5)

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Metric | 40 |
| B | Current Value | 20 |
| C | Target Value | 20 |
| D | Status | 20 |
| E | Notes | 40 |

---

## Sheet 18: Approval_Signoff

**Data Rows:** 5 (rows 1–5)

### Columns

| Col | Header |
|-----|--------|
| A | Role |
| B | Name |
| C | Signature |
| D | Date |
| E | Comments |

---

## Sheet 19: Base_Validations

---

**END OF SPECIFICATION**

---

*"We should be careful to get out of an experience only the wisdom that is in it."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
