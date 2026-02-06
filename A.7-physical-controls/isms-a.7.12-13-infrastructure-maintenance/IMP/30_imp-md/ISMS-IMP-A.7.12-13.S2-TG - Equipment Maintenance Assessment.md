**ISMS-IMP-A.7.12-13.S2-TG - Equipment Maintenance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.13: Equipment Maintenance

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.12-13.S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Equipment Maintenance - Maintenance Programme, Personnel, Security During Maintenance, Remote Maintenance, Records |
| **Related Policy** | ISMS-POL-A.7.12-13, Section 2.2 (Equipment Maintenance) |
| **Purpose** | Document equipment maintenance practices, assess compliance against policy requirements, and identify gaps |
| **Target Audience** | IT Operations, Facilities Management, System Administrators, Vendor Managers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Maintenance Events |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Equipment Maintenance assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.12-13.S2-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.12-13.S2_Equipment_Maintenance_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a712_2_equipment_maintenance.py)

**Sheet Count:** 9 worksheets

**Styling:** Navy blue headers, yellow input cells, conditional formatting

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Metadata and legend | Reference | ~30 rows |
| 2 | Equipment Inventory | Equipment in maintenance programme | Data Entry | 100 rows |
| 3 | Maintenance Programme | Programme compliance | Data Entry | ~30 rows |
| 4 | Personnel & Vendors | Authorised personnel | Data Entry | 50 rows |
| 5 | Security During Maintenance | Security controls | Data Entry | ~30 rows |
| 6 | Remote Maintenance | Remote access controls | Data Entry | 50 rows |
| 7 | Summary Dashboard | Compliance scoring | Formula-driven | ~40 rows |
| 8 | Evidence Register | Supporting evidence | Data Entry | 100 rows |
| 9 | Approval Sign-Off | Approval workflow | Data Entry | ~20 rows |

---

## Sheet-by-Sheet Specifications

### Sheet 2: Equipment Inventory

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Equipment ID | Text | 15 | None |
| B | Equipment Type | Dropdown | 18 | Server, Network Device, Storage, UPS, HVAC, Security System, Other |
| C | Equipment Description | Text | 35 | None |
| D | Location | Text | 25 | None |
| E | Criticality | Dropdown | 18 | Tier 1 - Critical, Tier 2 - Standard |
| F | Manufacturer | Text | 20 | None |
| G | Manufacturer Requirement | Text | 35 | None |
| H | Maintenance Frequency | Dropdown | 15 | Annually, Semi-annually, Quarterly, Monthly |
| I | Frequency Compliant | Dropdown | 12 | Yes, No |
| J | In Maintenance Programme | Dropdown | 12 | Yes, No, Partial |
| K | Last Maintenance | Date | 15 | Date |
| L | Next Scheduled | Date | 15 | Date |
| M | Compliance Status | Formula | 18 | Auto |
| N | Notes | Text | 40 | None |

### Sheet 4: Personnel & Vendors

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Personnel/Vendor ID | Text | 15 | None |
| B | Name | Text | 30 | None |
| C | Type | Dropdown | 18 | Internal Staff, Third-Party Vendor, Contractor |
| D | Equipment Types Authorised | Text | 30 | None |
| E | Verification Required | Dropdown | 18 | Yes - Badge/ID, Yes - Escort, No |
| F | Supervision Required | Dropdown | 20 | Yes - Always, Yes - Sensitive Equipment, No |
| G | Contract/Agreement | Text | 20 | None |
| H | NDA in Place | Dropdown | 10 | Yes, No, N/A |
| I | Background Check | Dropdown | 10 | Yes, No, N/A |
| J | Last Verified | Date | 15 | Date |
| K | Compliance Status | Formula | 18 | Auto |
| L | Notes | Text | 40 | None |

### Sheet 6: Remote Maintenance

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Access ID | Text | 12 | None |
| B | Access Type | Dropdown | 25 | Vendor Remote Support, Internal Remote Management, Cloud Management Portal |
| C | Provider/System | Text | 25 | None |
| D | Equipment Types | Text | 25 | None |
| E | Authorised | Dropdown | 18 | Yes - Pre-approved, Yes - On-demand, No |
| F | Secure Connection | Dropdown | 15 | Yes - VPN, Yes - Encrypted, No |
| G | Session Logged | Dropdown | 15 | Yes - Automated, Yes - Manual, No |
| H | Session Monitored | Dropdown | 15 | Yes - Real-time, Yes - Recorded, No |
| I | Access Disabled When Not Required | Dropdown | 18 | Yes - Always, Yes - Usually, No |
| J | Last Access Review | Date | 15 | Date |
| K | Compliance Status | Formula | 18 | Auto |
| L | Notes | Text | 40 | None |

---

## Cell Styling Reference

### Colour Palette

- Primary Header: #003366 (Navy blue)
- Column Header: #D9D9D9 (Light grey)
- Input Cell: #FFFFCC (Light yellow)
- Compliant: #C6EFCE (Light green)
- Partial: #FFEB9C (Light amber)
- Non-Compliant: #FFC7CE (Light red)

---

## Integration Points

### Integration with Policy

| Policy Section | Assessment Sheet |
|----------------|------------------|
| Section 2.2.1: Maintenance Programme | Sheet 2, Sheet 3 |
| Section 2.2.2: Maintenance Personnel | Sheet 4 |
| Section 2.2.3: Security During Maintenance | Sheet 5 |
| Section 2.2.4: Remote Maintenance | Sheet 6 |
| Section 2.2.5: Equipment Removal | Sheet 5 |
| Section 2.2.6: Maintenance Records | Sheet 3 |

### Integration with Other Assessments

- Feeds into: ISMS-IMP-A.7.12-13.S3 (Schedule), ISMS-IMP-A.7.12-13.S4 (Dashboard)
- Related to: Asset Management (A.5.9), Change Management (A.8.32)

---

**END OF SPECIFICATION**

---

*"Take care of your equipment and your equipment will take care of you."*
— Unknown

<!-- QA_VERIFIED: 2026-02-06 -->
