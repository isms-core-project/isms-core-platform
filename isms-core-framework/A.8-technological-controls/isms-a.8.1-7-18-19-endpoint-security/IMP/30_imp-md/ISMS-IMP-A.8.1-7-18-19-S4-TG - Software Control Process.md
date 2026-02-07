**ISMS-IMP-A.8.1-7-18-19-S4-TG - Software Control Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.1: User Endpoint Devices

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Software Installation Controls and Application Whitelisting |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19, Section 2.4 (Software Installation Controls) |
| **Purpose** | Document approved software list, assess unauthorized software, verify application control effectiveness across endpoint landscape |
| **Target Audience** | IT Operations, Security Engineers, Change Management, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Monthly (unauthorized software), Quarterly (full assessment) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guide for software control assessment | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a81-7-18-19_4_privileged_utilities.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.1-7-18-19.4` |
| **Output Filename** | `ISMS-IMP-A.8.1-7-18-19.S4_Privileged_Utilities_YYYYMMDD.xlsx` |
| **Total Sheets** | 23 (23 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls A.8.1, A.8.7, A.8.18, A.8.19: Endpoint Security |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #44546A | 44546A | Custom |
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #ED7D31 | ED7D31 | Custom |
| #FF6666 | FF6666 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFF2CC | FFF2CC | Cream (Input Alt) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: Utility_Inventory

---

## Sheet 3: Access_Controls

---

## Sheet 4: Approval_Workflow

---

## Sheet 5: Usage_Audit

---

## Sheet 6: MFA_Compliance

---

## Sheet 7: Quarterly_Reviews

---

## Sheet 8: Capability_Requirements

---

## Sheet 9: Evidence_Register

---

## Sheet 10: Gap_Analysis

---

## Sheet 11: Approval_Sign_Off

---

## Sheet 12: Base_Validations

---

## Sheet 13: Instructions

---

## Sheet 14: Utility_Inventory

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Utility ID |
| B | Utility Name |
| C | Platform |
| D | Category |
| E | Risk Level |
| F | Business Justification |
| G | Authorized Roles |
| H | Access Control Method |
| I | MFA Required |
| J | Logging Enabled |
| K | Notes |

---

## Sheet 15: Access_Controls

**Data Rows:** 9 (rows 2–10)

### Columns

| Col | Header |
|-----|--------|
| A | Utility ID |
| B | Utility Name |
| C | File Permissions Set |
| D | AD Group Restriction |
| E | AppLocker Rule |
| F | Control Status |
| G | Last Verified |
| H | Verified By |
| I | Issues |
| J | Notes |

---

## Sheet 16: Approval_Workflow

**Data Rows:** 10 (rows 2–11)

### Columns

| Col | Header |
|-----|--------|
| A | Request ID |
| B | Request Date |
| C | Requester |
| D | Utility |
| E | Access Type |
| F | Duration |
| G | Justification |
| H | Manager Approval |
| I | Security Approval |
| J | Status |
| K | Notes |

---

## Sheet 17: Usage_Audit

**Data Rows:** 9 (rows 2–10)

### Columns

| Col | Header |
|-----|--------|
| A | Log ID |
| B | Timestamp |
| C | User |
| D | Utility |
| E | Device |
| F | Action |
| G | Duration |
| H | Authorized |
| I | Flagged |
| J | Notes |

---

## Sheet 18: Mfa_Compliance

**Data Rows:** 8 (rows 1–8)

### Columns

| Col | Header |
|-----|--------|
| A | User |
| B | Role |
| C | Utility Access |
| D | MFA Technology |
| E | MFA Status |
| F | Last MFA Setup |
| G | Compliance |
| H | Notes |

---

## Sheet 19: Quarterly_Reviews

**Data Rows:** 10 (rows 1–10)

### Columns

| Col | Header |
|-----|--------|
| A | Review Quarter |
| B | User |
| C | Utility Access |
| D | Last Used |
| E | Manager Review |
| F | Decision |
| G | Action Taken |
| H | Completion Date |
| I | Reviewer |
| J | Notes |

---

## Sheet 20: Capability_Requirements

**Data Rows:** 4 (rows 3–6)

### Columns

| Col | Header |
|-----|--------|
| A | Req ID |
| B | Policy Requirement |
| C | Implemented |
| D | Evidence Reference |
| E | Notes |
| F | Status |

---

## Sheet 21: Evidence_Register

**Data Rows:** 9 (rows 2–10)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Type |
| C | Description |
| D | Related Requirement |
| E | Worksheet |
| F | Location |
| G | Date |
| H | Collected By |
| I | Status |
| J | Notes |

---

## Sheet 22: Gap_Analysis

**Data Rows:** 11 (rows 2–12)

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | Description |
| C | Affected Utilities |
| D | Requirement |
| E | Severity |
| F | Risk |
| G | Root Cause |
| H | Remediation |
| I | Owner |
| J | Due Date |
| K | Status |
| L | Notes |

---

## Sheet 23: Approval_Signoff

---

**END OF SPECIFICATION**

---

*"There are children playing in the streets who could solve some of my top problems in physics, because they have modes of sensory perception that I lost long ago."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->
