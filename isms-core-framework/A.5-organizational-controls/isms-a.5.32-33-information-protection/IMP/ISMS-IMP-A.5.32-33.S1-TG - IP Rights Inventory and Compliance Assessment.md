<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.32-33.S1-TG:framework:TG:a.5.32-33 -->
**ISMS-IMP-A.5.32-33.S1-TG - IP Rights Inventory and Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.32: Intellectual Property Rights

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.32-33.S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Intellectual Property Identification, Classification, Protection, and Compliance |
| **Related Policy** | ISMS-POL-A.5.32-33, Section 2.1 (IP Identification and Classification) |
| **Purpose** | Guide users through systematic IP discovery, classification, protection assessment, and third-party IP compliance verification |
| **Target Audience** | Legal Counsel, CISO, IP Owners, System Owners, IT Teams, Compliance Officers, Auditors, Workbook Developers |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Annual or After Significant IP Changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for IP Rights Inventory assessment workbook | ISMS Implementation Team |

---


---
# Technical Specification
**Audience:** Workbook Developers, Python/Excel Script Maintainers


> Auto-generated from `generate_a532_33_1_ip_rights_inventory.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.5.32-33.S1` |
| **Output Filename** | `ISMS-IMP-A.5.32-33.S1_IP_Rights_Inventory_YYYYMMDD.xlsx` |
| **Workbook Title** | IP Rights Inventory |
| **Total Sheets** | 8 (8 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control {...}: {...} |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #1F4E79 | 1F4E79 | Custom |
| #2E75B6 | 2E75B6 | Custom |
| #69DB7C | 69DB7C | Custom |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D6DCE4 | D6DCE4 | Silver (Neutral) |
| #FF6B6B | FF6B6B | Custom |
| #FFA94D | FFA94D | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions

---

## Sheet 2: Ip_Asset_Inventory

**Data Rows:** 46 (rows 5–50)

### Columns

| Col | Header |
|-----|--------|
| A | IP Asset ID |
| B | IP Asset Name |
| C | IP Category |
| D | Description |
| E | IP Owner |
| F | Custodian |
| G | Legal Protection Status |
| H | Business Value |
| I | Classification |
| J | Creation Date |
| K | Last Review |
| L | Notes |

---

## Sheet 3: Ip_Protection_Assessment

**Data Rows:** 46 (rows 5–50)

### Columns

| Col | Header |
|-----|--------|
| A | IP Asset ID |
| B | IP Asset Name |
| C | Access Control |
| D | Technical Controls |
| E | Administrative Controls |
| F | Physical Controls |
| G | Legal Protection |
| H | Control Effectiveness |
| I | Gap Description |
| J | Remediation Needed |
| K | Status |

---

## Sheet 4: Third_Party_Ip_Register

**Data Rows:** 56 (rows 5–60)

### Columns

| Col | Header |
|-----|--------|
| A | Third-Party IP ID |
| B | Software/Content Name |
| C | Vendor |
| D | License Type |
| E | License Quantity |
| F | Deployed Quantity |
| G | Compliance Status |
| H | Contract Reference |
| I | Renewal Date |
| J | Open Source License |
| K | Notes |

---

## Sheet 5: Software_License_Compliance

**Data Rows:** 46 (rows 5–50)

### Columns

| Col | Header |
|-----|--------|
| A | Software Name |
| B | Vendor |
| C | License Model |
| D | Entitled |
| E | Deployed |
| F | Variance |
| G | Compliance Risk |
| H | Remediation Action |
| I | Due Date |
| J | Status |

---

## Sheet 6: Gap_Analysis

**Data Rows:** 46 (rows 5–50)

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | Gap Category |
| C | Description |
| D | Related IP |
| E | Risk Rating |
| F | Remediation Action |
| G | Owner |
| H | Due Date |
| I | Status |
| J | Notes |

---

## Sheet 7: Evidence_Register

**Data Rows:** 46 (rows 5–50)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Description |
| C | Evidence Type |
| D | Related Item |
| E | Storage Location |
| F | Collected Date |
| G | Collected By |
| H | Verification Status |

---

## Sheet 8: Approval

**Data Rows:** 8 (rows 13–20)

---

**END OF SPECIFICATION**

---

*"The only thing worse than training employees and losing them is not training them and keeping them."*
-- Zig Ziglar

<!-- QA_VERIFIED: 2026-02-06 -->
