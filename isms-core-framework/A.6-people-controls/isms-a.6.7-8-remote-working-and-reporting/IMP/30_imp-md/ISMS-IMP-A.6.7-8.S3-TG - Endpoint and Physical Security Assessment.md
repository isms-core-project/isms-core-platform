**ISMS-IMP-A.6.7-8.S3-TG - Endpoint and Physical Security Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Device Security, Encryption, Endpoint Protection, Physical Security |
| **Related Policy** | ISMS-POL-A.6.7-8, Sections 2.2 (Physical Security) & 2.5 (Device Security) |
| **Purpose** | Guide users through assessment of endpoint security controls and physical security for remote work |
| **Target Audience** | IT Security Team, Endpoint Management Team, Desktop Support, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly (technical), Annual (physical) |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for endpoint and physical security assessment | ISMS Implementation Team |

---


---
# Technical Specification


> Auto-generated from `generate_a678_s3_endpoint_physical_security.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.6.7-8.S3` |
| **Output Filename** | `ISMS-IMP-A.6.7-8.S3_Endpoint_and_Physical_Security_Assessment_YYYYMMDD.xlsx` |
| **Workbook Title** | Endpoint and Physical Security Assessment |
| **Total Sheets** | 15 (15 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #003366 | 003366 | Dark Blue (Headers) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Device_Inventory

---

## Sheet 3: Encryption_Status

---

## Sheet 4: Endpoint_Protection

---

## Sheet 5: Patch_Compliance

---

## Sheet 6: BYOD_Assessment

---

## Sheet 7: Physical_Security

---

## Sheet 8: Lost_Stolen_Procedures

---

## Sheet 9: Gap_Analysis

---

## Sheet 10: Evidence_Register

---

## Sheet 11: Dashboard

---

## Sheet 12: Approval_Sign_Off

---

## Sheet 13: Byod_Assessment

**Data Rows:** 15 (rows 4–18)

### Columns

| Col | Header |
|-----|--------|
| A | Device ID |
| B | Device Type |
| C | Owner |
| D | OS/Version |
| E | Min OS Met |
| F | MDM Enrolled |
| G | Container |
| H | Encrypted |
| I | Remote Wipe |
| J | Agreement Signed |
| K | Compliant |
| L | Notes |

---

## Sheet 14: Lost_Stolen

**Data Rows:** 7 (rows 3–9)

### Columns

| Col | Header |
|-----|--------|
| A | Procedure Element |
| B | Requirement |
| C | SLA |
| D | Implemented |
| E | Documentation |
| F | Last Tested |
| G | Responsible |
| H | Evidence |
| I | Compliant |

---

## Sheet 15: Approval

**Data Rows:** 4 (rows 2–5)

### Columns

| Col | Header |
|-----|--------|
| A | Role |
| B | Name |
| C | Signature |
| D | Date |
| E | Comments |

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `DEVICE_TYPES` | Laptop, Desktop, Tablet, Mobile, Other |
| `ENCRYPTION_TYPES` | BitLocker, FileVault, LUKS, Other, None |
| `OWNERSHIP_TYPES` | Corporate, BYOD, Contractor |

---

**END OF SPECIFICATION**

---

*"Physical security is the foundation upon which all other security measures are built."*
— ASIS International

<!-- QA_VERIFIED: 2026-02-06 -->
