<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.17-S3-TG:framework:TG:a.8.17-s3 -->
**ISMS-IMP-A.8.17-S3-TG - Exception Management**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Clock Synchronization Exception Management |
| **Related Policy** | ISMS-POL-A.8.17 (Clock Synchronization Policy - Section 3.3) |
| **Purpose** | Document and manage systems that cannot meet clock synchronization requirements, including air-gapped systems, legacy equipment, and special use cases |
| **Target Audience** | System Administrators, Network Engineers, Security Engineers, ISMS Officers, Risk Managers, Auditors |
| **Assessment Type** | Operational & Risk Management |
| **Review Cycle** | Quarterly or When Exceptions Change |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original Date] | Initial technical specification for exception management | ISMS Officer |


---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, technical implementers


> Auto-generated from `generate_a817_3_exception_register.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.17.3` |
| **Output Filename** | `ISMS-IMP-A.8.17.3_Exception_Register_YYYYMMDD.xlsx` |
| **Total Sheets** | 5 (5 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.17: Clock Synchronization |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #0000FF | 0000FF | Custom |
| #003366 | 003366 | Dark Blue (Headers) |
| #808080 | 808080 | Gray (Disabled) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Exception_Requests

**Data Rows:** 50 (rows 4–53) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Exception ID [*] |
| B | Submitted Date [*] |
| C | System/Asset Name [*] |
| D | Requirement Exempted [*] |
| E | Exception Type [*] |
| F | Business Justification [*] |
| G | Risk Assessment [*] |
| H | Compensating Controls [*] |
| I | Requested Duration [*] |
| J | Submitted By [*] |
| K | Approval Authority [*] |
| L | Approval Status |
| M | Notes |

---

## Sheet 3: Active_Exceptions

**Data Rows:** 50 (rows 4–53) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Exception ID [*] |
| B | System/Asset Name [*] |
| C | Requirement Exempted [*] |
| D | Exception Type [*] |
| E | Approved By [*] |
| F | Approval Date [*] |
| G | Expiry Date [*] |
| H | Days Until Expiry |
| I | Compensating Controls [*] |
| J | Last Quarterly Review |
| K | Next Review Due |
| L | Reassessment Required |
| M | Status |
| N | Review Notes |
| O | Actions Required |

---

## Sheet 4: Expired_Exceptions

**Data Rows:** 100 (rows 4–103) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Exception ID |
| B | System/Asset Name |
| C | Requirement Exempted |
| D | Exception Type |
| E | Approved By |
| F | Approval Date |
| G | Expiry Date |
| H | Closure Date |
| I | Closure Reason |
| J | Total Duration (Days) |
| K | Final Status |
| L | Lessons Learned |

---

## Sheet 5: Summary_Dashboard

**Data Rows:** 100 (rows 4–103)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(Exception_Requests!A4:A53)` | Pending Approval |
| — | `=COUNTA(Active_Exceptions!A4:A53)` | Active Exceptions |
| — | `=COUNTA(Expired_Exceptions!A4:A103)` | Expired/Revoked (Total) |
| — | `=COUNTIF(Active_Exceptions!H4:H53,\` | Expiring Within 30 Days |
| — | `=COUNTIF(Active_Exceptions!L4:L53,\` | Requiring Reassessment (90-day rule) |

---

**END OF SPECIFICATION**

---

*"Lost time is never found again."*
— Benjamin Franklin

<!-- QA_VERIFIED: 2026-02-06 -->
