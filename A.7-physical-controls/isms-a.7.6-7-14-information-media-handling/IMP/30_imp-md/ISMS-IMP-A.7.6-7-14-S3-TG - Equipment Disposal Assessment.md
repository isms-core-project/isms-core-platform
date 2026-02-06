**ISMS-IMP-A.7.6-7-14-S3-TG - Secure Equipment Disposal Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.14: Secure Disposal or Re-Use of Equipment

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.6-7-14-S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Secure Disposal and Re-Use of Equipment - Data Sanitisation and Destruction |
| **Related Policy** | ISMS-POL-A.7.6-7-14, Section 2.3 (Secure Disposal or Re-Use of Equipment) |
| **Purpose** | Document disposal procedures, assess data sanitisation practices, track disposal records and certificates |
| **Target Audience** | IT Operations, Asset Management, Procurement, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Procedural |
| **Review Cycle** | Semi-Annual or After Major Disposal Events |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Equipment Disposal assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.6-7-14-S3-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.14.S3_Equipment_Disposal_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a76_3_equipment_disposal.py)

**Sheet Count:** 8 worksheets

**Data Capacity:** 100 data rows per assessment sheet

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type |
|---------|------------|---------|------|
| 1 | Instructions & Legend | Assessment metadata | Read-only Reference |
| 2 | Disposal Requirements | Methods by equipment/classification | Data Entry |
| 3 | Disposal Tools | Approved sanitisation tools | Data Entry |
| 4 | Service Providers | Disposal vendor management | Data Entry |
| 5 | Disposal Log | Equipment disposal tracking | Data Entry |
| 6 | Summary Dashboard | Automated compliance scoring | Formula-driven |
| 7 | Evidence Register | Audit evidence documentation | Data Entry |
| 8 | Approval Sign-Off | Approval workflow | Data Entry |

---

## Sheet-by-Sheet Specifications

### Sheet 2: Disposal Requirements

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Equipment Type | Text | 20 | None |
| B | Storage Type | Dropdown | 15 | HDD / SSD / Flash / Memory / Config |
| C | CONFIDENTIAL Method | Dropdown | 25 | Physical Destruction / Crypto Erase / Secure Overwrite |
| D | INTERNAL Method | Dropdown | 25 | As above + Format |
| E | PUBLIC Method | Dropdown | 20 | As above |
| F | Verification Required | Dropdown | 15 | Yes / No |
| G | Certificate Required | Dropdown | 15 | Yes / No |
| H | Implementation Status | Dropdown | 20 | Implemented / Partial / Not Implemented |
| I | Notes | Text | 40 | None |

### Sheet 3: Disposal Tools

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Tool/Method Name | Text | 30 | None |
| B | Tool Type | Dropdown | 22 | Software - Overwrite / Software - Crypto / Hardware - Degausser / Hardware - Shredder |
| C | Applicable Equipment | Text | 25 | None |
| D | Standard/Method | Text | 25 | None |
| E | Verification Method | Text | 30 | None |
| F | Approved Version | Text | 15 | None |
| G | Last Tested | Date | 15 | Date |
| H | Compliant | Dropdown | 12 | Yes / Partial / No |
| I | Notes | Text | 40 | None |

### Sheet 4: Service Providers

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Provider Name | Text | 30 | None |
| B | Service Type | Dropdown | 22 | On-site / Off-site / Recycling / Certificate Only |
| C | Contract Status | Dropdown | 15 | Active / Expired / Under Review |
| D | Contract Expiry | Date | 15 | Date |
| E | Certificate Provided | Dropdown | 18 | Yes - Per Item / Yes - Per Batch / No |
| F | On-Site Option | Dropdown | 12 | Yes / No |
| G | Chain of Custody | Dropdown | 18 | Documented / Partial / Not Documented |
| H | Last Audit/Review | Date | 15 | Date |
| I | Compliance Status | Formula | 18 | Auto |
| J | Notes | Text | 40 | None |

### Sheet 5: Disposal Log

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Disposal ID | Text | 18 | None |
| B | Date | Date | 12 | Date |
| C | Asset Tag | Text | 15 | None |
| D | Equipment Type | Dropdown | 15 | Laptop / Desktop / Server / Mobile / Printer / Other |
| E | Make/Model | Text | 25 | None |
| F | Serial Number | Text | 20 | None |
| G | Data Classification | Dropdown | 18 | CONFIDENTIAL / INTERNAL / PUBLIC / Unknown |
| H | Disposal Method | Dropdown | 22 | Physical Destruction / Secure Overwrite / Factory Reset / Format |
| I | Destination | Dropdown | 18 | Vendor / Internal Re-Use / Donation / Sale / Recycling |
| J | Certificate Obtained | Dropdown | 15 | Yes / No / N/A |
| K | Certificate Ref | Text | 20 | None |
| L | Verified By | Text | 20 | None |
| M | Asset Updated | Dropdown | 12 | Yes / No |
| N | Compliant | Formula | 12 | Auto |
| O | Notes | Text | 35 | None |

---

## Cell Styling Reference

### Colour Palette

**Headers:**
- Primary: #003366 (Navy blue), #FFFFFF (White text)
- Column: #D9D9D9 (Grey), #000000 (Black text)

**Data Cells:**
- Input: #FFFFCC (Yellow)
- Formula: #FFFFFF (White)

**Status:**
- Compliant: #C6EFCE (Green)
- Partial: #FFEB9C (Amber)
- Non-Compliant: #FFC7CE (Red)

---

## Integration Points

### Policy Integration

| Policy Section | Assessment Sheet |
|----------------|------------------|
| Section 2.3: Pre-Disposal Requirements | Sheet 2 |
| Section 2.3: Disposal Methods | Sheet 2, Sheet 3 |
| Section 2.3: Re-Use Requirements | Sheet 5 (Destination) |
| Section 2.3: Documentation | Sheet 5, Sheet 7 |

### Related Control Integration

- **A.5.10-11** (Asset Lifecycle): Asset record updates in Sheet 5
- **A.7.10** (Storage Media): Removable media disposal in Sheet 5
- **A.8.10** (Information Deletion): Data sanitisation methods in Sheet 3

### Dashboard Integration

Feeds into ISMS-IMP-A.7.6-7-14-S4 Compliance Dashboard:
- Disposal compliance rate
- Certificate collection rate
- Equipment disposed by type
- Gap count

---

**END OF SPECIFICATION**

---

*"The data you don't properly destroy is the data that will come back to haunt you."*
— Unknown

<!-- QA_VERIFIED: 2026-02-06 -->
