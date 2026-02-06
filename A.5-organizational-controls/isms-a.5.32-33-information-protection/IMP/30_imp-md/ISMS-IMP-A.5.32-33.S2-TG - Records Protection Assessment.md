**ISMS-IMP-A.5.32-33.S2-TG - Records Protection Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.33: Protection of Records

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.32-33.S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Records Identification, Classification, Protection Controls, and Integrity Verification |
| **Related Policy** | ISMS-POL-A.5.32-33, Section 2.2 (Records Protection) |
| **Purpose** | Guide users through systematic records inventory, classification, protection assessment, and integrity verification |
| **Target Audience** | Records Manager, CISO, Legal Counsel, System Owners, IT Teams, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Annual or After Significant System Changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Records Protection assessment workbook | ISMS Implementation Team |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.32-33.S2-UG.

---

# Technical Specification

**Audience:** Workbook Developers, Python/Excel Script Maintainers

---

# Workbook Structure

## Generated File

**Filename:** `ISMS-IMP-A.5.32-33.S2_Records_Protection_Assessment_[YYYYMMDD].xlsx`

**Generator Script:** `generate_a532_33_2_records_protection.py`

## Sheet Overview

| Sheet # | Sheet Name | Purpose | Rows (Est.) |
|---------|------------|---------|-------------|
| 1 | Instructions | Usage guidance | ~50 |
| 2 | Records_Category_Inventory | Record types | 50+ |
| 3 | Protection_Controls | Controls per category | 50+ |
| 4 | Integrity_Verification | Test results | 30+ |
| 5 | Access_Control_Review | Access assessment | 30+ |
| 6 | Legal_Hold_Register | Active holds | 20+ |
| 7 | Backup_Verification | Backup status | 50+ |
| 8 | Gap_Analysis | Identified gaps | 30+ |
| 9 | Evidence_Register | Audit evidence | 50+ |
| 10 | Approval_SignOff | Formal approval | ~30 |

---

# Sheet-by-Sheet Specifications

## Sheet 2: Records_Category_Inventory

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Record Category ID | 18 | - |
| B | Category Name | 30 | - |
| C | Record Type | 15 | List: Financial, Personnel, Legal, Operational, Technical, Security, Regulatory |
| D | Description | 45 | - |
| E | Custodian Department | 20 | - |
| F | Storage Location | 30 | - |
| G | Format | 12 | List: Physical, Electronic, Both |
| H | Retention Requirement | 30 | - |
| I | Confidentiality | 15 | List: Restricted, Confidential, Internal, Public |
| J | Integrity Requirement | 12 | List: Critical, High, Standard |
| K | Availability Requirement | 18 | List: Mission Critical, Business Critical, Standard |
| L | Notes | 35 | - |

## Sheet 3: Protection_Controls

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Record Category ID | 18 | - |
| B | Category Name | 25 | - |
| C | Confidentiality Controls | 35 | - |
| D | Integrity Controls | 35 | - |
| E | Availability Controls | 35 | - |
| F | Physical Controls | 25 | - |
| G | Control Effectiveness | 15 | List: Effective, Partial, Ineffective |
| H | Gap Description | 35 | - |
| I | Remediation Needed | 35 | - |
| J | Status | 15 | List: Complete, In Progress, Not Started |

## Sheet 4: Integrity_Verification

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Test ID | 10 | - |
| B | Record Category | 25 | - |
| C | Integrity Mechanism | 25 | List: Checksum, Digital Signature, WORM, Audit Log, Database Constraints, Other |
| D | Test Date | 12 | Date |
| E | Test Performed | 35 | - |
| F | Expected Result | 25 | - |
| G | Actual Result | 25 | - |
| H | Status | 10 | List: Pass, Fail, Partial, Not Tested |
| I | Issues | 30 | - |
| J | Remediation | 30 | - |

## Sheet 5: Access_Control_Review

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | System Name | 25 | - |
| B | Record Categories | 30 | - |
| C | Access Control Type | 15 | List: RBAC, DAC, MAC, Mixed |
| D | User Count | 12 | Number |
| E | Privileged Users | 15 | Number |
| F | Last Access Review | 15 | Date |
| G | Access Logging | 12 | List: Yes, No, Partial |
| H | Log Retention | 15 | - |
| I | Issues | 30 | - |
| J | Remediation | 30 | - |
| K | Status | 15 | List: Compliant, Non-Compliant, Partial |

## Sheet 6: Legal_Hold_Register

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Hold ID | 15 | - |
| B | Matter Name | 30 | - |
| C | Legal Counsel | 25 | - |
| D | Effective Date | 12 | Date |
| E | Record Categories | 35 | - |
| F | Custodians Notified | 30 | - |
| G | Notification Date | 15 | Date |
| H | Release Date | 12 | Date |
| I | Status | 12 | List: Active, Released, Pending |
| J | Notes | 35 | - |

## Sheet 7: Backup_Verification

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Record Category | 25 | - |
| B | Backup System | 20 | - |
| C | Backup Frequency | 20 | List: Real-time, Hourly, Daily, Weekly, Monthly |
| D | Backup Location | 25 | - |
| E | Last Backup Date | 15 | Date |
| F | Last Verification | 15 | Date |
| G | Last Recovery Test | 15 | Date |
| H | RTO Target | 12 | - |
| I | RTO Achieved | 12 | - |
| J | RPO Target | 12 | - |
| K | RPO Achieved | 12 | - |
| L | Status | 15 | List: Compliant, Non-Compliant |
| M | Issues | 30 | - |

## Sheet 8: Gap_Analysis

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Gap ID | 10 | - |
| B | Gap Category | 15 | List: Confidentiality, Integrity, Availability, Process |
| C | Description | 45 | - |
| D | Related Record Category | 20 | - |
| E | Risk Rating | 12 | List: High, Medium, Low |
| F | Remediation Action | 40 | - |
| G | Owner | 20 | - |
| H | Due Date | 12 | Date |
| I | Status | 15 | List: Open, In Progress, Complete, Accepted |
| J | Notes | 30 | - |

## Sheet 9: Evidence_Register

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Evidence ID | 12 | - |
| B | Description | 40 | - |
| C | Evidence Type | 18 | List: Document, Screenshot, Report, Log, Configuration, Other |
| D | Related Item | 20 | - |
| E | Storage Location | 35 | - |
| F | Collected Date | 12 | Date |
| G | Collected By | 20 | - |
| H | Verification Status | 18 | List: Verified, Pending Review, Not Verified, Expired |

## Sheet 10: Approval_SignOff

### Layout
- Rows 1-2: Headers
- Rows 4-8: Assessment metadata
- Row 10: Approval section header
- Row 12: Approval table headers
- Rows 13+: Approver rows

### Approver Roles
1. Records Manager
2. Chief Information Security Officer
3. Legal Counsel
4. IT Operations Manager
5. Internal Audit Representative

---

# Cell Styling Reference

## Colour Palette

| Style Name | Hex Code | Usage |
|------------|----------|-------|
| Header Fill | #1F4E79 | Sheet headers |
| Subheader Fill | #2E75B6 | Secondary headers |
| Column Header | #D6DCE4 | Table headers |
| Input Cell | #FFFFCC | User input cells |
| High Risk | #FF6B6B | High priority items |
| Medium Risk | #FFA94D | Medium priority |
| Low Risk | #69DB7C | Low priority |
| Compliant | #C6EFCE | Compliant status |
| Warning | #FFEB9C | Attention needed |
| Non-Compliant | #FFC7CE | Non-compliant |

---

# Integration Points

## Related Workbooks

| Workbook | Integration Type | Data Exchange |
|----------|-----------------|---------------|
| ISMS-IMP-A.5.32-33.S1 | IP classification | IP records protection requirements |
| ISMS-IMP-A.5.32-33.S3 | Retention schedule | Protection informs disposal |
| ISMS-IMP-A.5.32-33.S4 | Dashboard | Metrics feed dashboard |
| ISMS-IMP-A.8.13 | Backup integration | Backup control alignment |
| ISMS-IMP-A.8.10 | Deletion | Secure disposal alignment |

---

**END OF SPECIFICATION**

---

*"Records management is not just about what you keep, but how you keep it."*
-- Anonymous

<!-- QA_VERIFIED: 2026-02-06 -->
