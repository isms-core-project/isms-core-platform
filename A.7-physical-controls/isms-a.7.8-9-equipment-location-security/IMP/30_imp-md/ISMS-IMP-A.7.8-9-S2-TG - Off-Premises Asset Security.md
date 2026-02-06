**ISMS-IMP-A.7.8-9-S2-TG - Off-Premises Asset Security Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.9: Security of Assets Off-Premises

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.8-9-S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Off-Premises Assets - Authorisation, Tracking, Protection Measures, Remote Working, Permanent Installations |
| **Related Policy** | ISMS-POL-A.7.8-9, Section 2.2 (Security of Assets Off-Premises) |
| **Purpose** | Document equipment used off-premises, assess protection measures, track authorisations, and identify gaps |
| **Target Audience** | IT Operations, Security Operations, Line Managers, Remote Workers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Semi-Annual or After Significant Policy Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Off-Premises Asset Security assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.8-9-S2-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.9.S2_Off_Premises_Assets_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a78_2_offpremises_assets.py)

**Sheet Count:** 10 worksheets

**Data Capacity:** 100 data rows per assessment sheet

**Styling:** Navy blue headers, yellow input cells, conditional formatting

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Metadata and status legend | Reference | ~30 rows |
| 2 | Equipment Inventory | Equipment categories for off-premises use | Data Entry | 50 rows |
| 3 | Authorisation & Tracking | Removal authorisation processes | Data Entry | 50 rows |
| 4 | Protection Measures | Security controls for off-premises equipment | Data Entry | 50 rows |
| 5 | Remote Working | Remote work scenario security | Data Entry | 50 rows |
| 6 | Permanent Off-Site | Fixed off-premises installations | Data Entry | 50 rows |
| 7 | Incidents | Equipment security incidents | Data Entry | 100 rows |
| 8 | Evidence Register | Supporting documentation | Data Entry | 100 rows |
| 9 | Summary Dashboard | Automated compliance scoring | Formula-driven | ~40 rows |
| 10 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

---

## Sheet-by-Sheet Specifications

### Sheet 2: Equipment Inventory

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Category ID | Text | 12 | None |
| B | Equipment Category | Text | 25 | None |
| C | Equipment Type | Dropdown | 18 | List |
| D | Total Count | Number | 12 | Integer |
| E | Off-Premises Count | Number | 15 | Integer |
| F | Primary Use Case | Text | 25 | None |
| G | MDM Managed | Dropdown | 18 | List |
| H | Encryption Enabled | Dropdown | 18 | List |
| I | Remote Wipe Capable | Dropdown | 18 | List |
| J | GPS Tracking | Dropdown | 20 | List |
| K | Last Compliance Check | Date | 15 | Date |
| L | Compliance Status | Formula | 18 | Yes |
| M | Notes | Text | 50 | None |

### Sheet 3: Authorisation & Tracking

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Category ID | Text | 12 | None |
| B | Equipment Category | Text | 25 | None |
| C | Authorisation Required | Dropdown | 22 | List |
| D | Authorisation Method | Text | 25 | None |
| E | Tracking System | Text | 20 | None |
| F | Chain of Custody | Dropdown | 20 | List |
| G | Return Verification | Dropdown | 22 | List |
| H | Overdue Alert | Dropdown | 20 | List |
| I | Current Overdue Count | Number | 15 | Integer |
| J | Last Process Review | Date | 15 | Date |
| K | Compliance Status | Formula | 18 | Yes |
| L | Notes | Text | 50 | None |

### Sheet 4: Protection Measures

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Category ID | Text | 12 | None |
| B | Equipment Category | Text | 25 | None |
| C | Physical Security | Dropdown | 22 | List |
| D | Transport Guidelines | Dropdown | 22 | List |
| E | Public Place Rules | Dropdown | 22 | List |
| F | Storage When Not In Use | Dropdown | 25 | List |
| G | Environmental Protection | Dropdown | 22 | List |
| H | Privacy Screen Required | Dropdown | 22 | List |
| I | VPN Required | Dropdown | 22 | List |
| J | Screen Lock Timeout | Text | 15 | None |
| K | Compliance Status | Formula | 18 | Yes |
| L | Notes | Text | 50 | None |

### Sheet 5: Remote Working

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Scenario ID | Text | 12 | None |
| B | Work Scenario | Text | 30 | None |
| C | Data Sensitivity | Dropdown | 22 | List |
| D | VPN Requirement | Dropdown | 22 | List |
| E | Privacy Screen | Dropdown | 18 | List |
| F | WiFi Security | Dropdown | 22 | List |
| G | Physical Security | Dropdown | 22 | List |
| H | Visitor Access | Dropdown | 22 | List |
| I | Bluetooth/Wireless | Dropdown | 22 | List |
| J | Worker Count | Number | 12 | Integer |
| K | Last Review | Date | 15 | Date |
| L | Compliance Status | Formula | 18 | Yes |
| M | Notes | Text | 50 | None |

### Sheet 6: Permanent Off-Site

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Installation ID | Text | 12 | None |
| B | Installation Name | Text | 25 | None |
| C | Installation Type | Dropdown | 20 | List |
| D | Location Count | Number | 12 | Integer |
| E | Physical Security | Dropdown | 22 | List |
| F | Environmental Monitoring | Dropdown | 22 | List |
| G | Remote Management | Dropdown | 20 | List |
| H | Inspection Schedule | Dropdown | 18 | List |
| I | Last Inspection | Date | 15 | Date |
| J | Incident Response | Dropdown | 20 | List |
| K | Compliance Status | Formula | 18 | Yes |
| L | Notes | Text | 50 | None |

### Sheet 7: Incidents

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Incident ID | Text | 12 | None |
| B | Incident Date | Date | 12 | Date |
| C | Equipment Category | Text | 20 | None |
| D | Incident Type | Dropdown | 15 | List |
| E | Location | Text | 20 | None |
| F | Data at Risk | Dropdown | 22 | List |
| G | Remote Wipe Executed | Dropdown | 22 | List |
| H | Time to Report (hours) | Number | 18 | Integer |
| I | Recovery Status | Dropdown | 18 | List |
| J | Root Cause | Text | 25 | None |
| K | Corrective Action | Text | 30 | None |
| L | Notes | Text | 50 | None |

### Sheet 8: Evidence Register

Standard evidence register format (see Sheet 7 in S1 specification).

### Sheet 9: Summary Dashboard

**Metrics:**

- Overall Off-Premises Security Score
- Equipment Inventory Compliance (%)
- Authorisation Process Compliance (%)
- Protection Measures Compliance (%)
- Remote Working Compliance (%)
- Permanent Installation Compliance (%)
- Incident Rate (losses per 1000 devices)
- Recovery Rate (%)
- Gap Summary

### Sheet 10: Approval Sign-Off

Standard four-level approval format.

---

## Cell Styling Reference

Same as S1 specification:

- Headers: #003366 (Navy blue)
- Input cells: #FFFFCC (Light yellow)
- Compliant: #C6EFCE (Light green)
- Partial: #FFEB9C (Light amber)
- Non-Compliant: #FFC7CE (Light red)

---

## Integration Points

### Integration with Policy (ISMS-POL-A.7.8-9)

| Policy Section | Assessment Sheet |
|----------------|------------------|
| Section 2.2.1: Authorisation and Tracking | Sheet 3 |
| Section 2.2.2: Off-Premises Protection | Sheet 4 |
| Section 2.2.3: Working Remotely | Sheet 5 |
| Section 2.2.4: Permanently Off-Site | Sheet 6 |

### Integration with Other Assessments

**Feeds into:**

- ISMS-IMP-A.7.8-9-S3 (Compliance Dashboard)
- ISMS-IMP-A.6.7 (Remote Working)

**Related Controls:**

- A.8.1 User Endpoint Devices
- A.6.7 Remote Working
- A.7.4 Physical Security Monitoring

---

**END OF SPECIFICATION**

---

*"The price of freedom is eternal vigilance."*
-- Thomas Jefferson

<!-- QA_VERIFIED: 2026-02-06 -->
