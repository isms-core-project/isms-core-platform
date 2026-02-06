**ISMS-IMP-A.5.32-33.S3-TG - Retention and Disposal Schedule Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.33: Protection of Records

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.32-33.S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Records Retention Requirements, Disposal Schedule, Secure Destruction Verification |
| **Related Policy** | ISMS-POL-A.5.32-33, Section 2.2 (Retention Requirements, Records Disposal) |
| **Purpose** | Guide users through defining retention periods, managing disposal schedules, and verifying secure destruction |
| **Target Audience** | Records Manager, Legal Counsel, CISO, IT Operations, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Annual or After Regulatory Changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Retention and Disposal assessment workbook | ISMS Implementation Team |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.5.32-33.S3-UG.

---

# Technical Specification

**Audience:** Workbook Developers, Python/Excel Script Maintainers

---

# Workbook Structure

## Generated File

**Filename:** `ISMS-IMP-A.5.32-33.S3_Retention_Disposal_Schedule_[YYYYMMDD].xlsx`

**Generator Script:** `generate_a532_33_3_retention_disposal.py`

## Sheet Overview

| Sheet # | Sheet Name | Purpose | Rows (Est.) |
|---------|------------|---------|-------------|
| 1 | Instructions | Usage guidance | ~50 |
| 2 | Retention_Schedule | Retention periods | 50+ |
| 3 | Regulatory_Mapping | Regulation reference | 30+ |
| 4 | Disposal_Queue | Records for disposal | 50+ |
| 5 | Disposal_Method_Matrix | Methods per classification | ~10 |
| 6 | Destruction_Verification | Destruction evidence | 100+ |
| 7 | Exception_Register | Extensions/early disposal | 30+ |
| 8 | Compliance_Dashboard | Metrics | ~20 |
| 9 | Gap_Analysis | Issues | 30+ |
| 10 | Evidence_Register | Audit evidence | 50+ |
| 11 | Approval_SignOff | Formal approval | ~30 |

---

# Sheet-by-Sheet Specifications

## Sheet 2: Retention_Schedule

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Record Category ID | 18 | - |
| B | Category Name | 30 | - |
| C | Retention Period | 15 | - |
| D | Retention Basis | 20 | List: Regulatory, Contractual, Business, Mixed |
| E | Basis Detail | 35 | - |
| F | Retention Trigger | 20 | List: Creation, Year-End, Contract End, Last Activity, Event-Based |
| G | Grace Period | 12 | - |
| H | Review Cycle | 12 | List: Annual, Biennial, Triennial |
| I | Last Review | 12 | Date |
| J | Next Review | 12 | Date |
| K | Notes | 35 | - |

## Sheet 3: Regulatory_Mapping

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Regulation ID | 12 | - |
| B | Regulation Name | 30 | - |
| C | Section/Article | 15 | - |
| D | Record Types Affected | 35 | - |
| E | Required Retention | 15 | - |
| F | Retention Trigger | 20 | - |
| G | Penalty for Non-Compliance | 30 | - |
| H | Last Review | 12 | Date |
| I | Reviewer | 20 | - |
| J | Notes | 35 | - |

## Sheet 4: Disposal_Queue

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Queue ID | 12 | - |
| B | Record Category | 30 | - |
| C | Retention End Date | 15 | Date |
| D | Volume - Physical | 15 | - |
| E | Volume - Electronic | 15 | - |
| F | Legal Hold Status | 12 | List: Yes, No, Checking |
| G | Disposal Priority | 12 | List: High, Medium, Low |
| H | Target Disposal Date | 15 | Date |
| I | Assigned To | 20 | - |
| J | Status | 15 | List: Pending, In Progress, Complete, On Hold |
| K | Notes | 30 | - |

## Sheet 5: Disposal_Method_Matrix

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Classification | 15 | List: Restricted, Confidential, Internal, Public |
| B | Physical - Paper | 25 | - |
| C | Physical - Media | 25 | - |
| D | Electronic - On-Prem | 25 | - |
| E | Electronic - Cloud | 25 | - |
| F | Verification Required | 20 | - |
| G | Approved Vendors | 25 | - |
| H | Special Handling | 25 | - |

## Sheet 6: Destruction_Verification

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Destruction ID | 18 | - |
| B | Record Category | 25 | - |
| C | Volume | 15 | - |
| D | Destruction Date | 15 | Date |
| E | Method Used | 25 | - |
| F | Performed By | 20 | - |
| G | Witness | 20 | - |
| H | Certificate Reference | 20 | - |
| I | Storage Location | 30 | - |
| J | Verification Status | 15 | List: Verified, Pending, Not Verified |

## Sheet 7: Exception_Register

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Exception ID | 15 | - |
| B | Exception Type | 15 | List: Extension, Early Disposal |
| C | Record Category | 25 | - |
| D | Original Retention | 15 | - |
| E | New Retention | 15 | - |
| F | Reason | 35 | - |
| G | Requested By | 20 | - |
| H | Approved By | 20 | - |
| I | Approval Date | 12 | Date |
| J | Expiration | 15 | - |
| K | Status | 12 | List: Active, Expired, Cancelled |

## Sheet 8: Compliance_Dashboard

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Metric ID | 10 | - |
| B | Metric Name | 25 | - |
| C | Description | 40 | - |
| D | Target | 12 | - |
| E | Current Value | 12 | - |
| F | Trend | 12 | List: Improving, Stable, Declining, New |
| G | Status | 15 | List: On Target, At Risk, Below Target |
| H | Owner | 20 | - |
| I | Last Updated | 12 | Date |

## Sheet 9: Gap_Analysis

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Gap ID | 10 | - |
| B | Gap Category | 18 | List: Retention, Disposal, Verification, Process |
| C | Description | 45 | - |
| D | Related Item | 20 | - |
| E | Risk Rating | 12 | List: High, Medium, Low |
| F | Remediation Action | 40 | - |
| G | Owner | 20 | - |
| H | Due Date | 12 | Date |
| I | Status | 15 | List: Open, In Progress, Complete |

## Sheet 10: Evidence_Register

### Column Structure

| Column | Header | Width | Data Validation |
|--------|--------|-------|-----------------|
| A | Evidence ID | 12 | - |
| B | Description | 40 | - |
| C | Evidence Type | 18 | List: Certificate, Log, Approval, Report, Other |
| D | Related Item | 20 | - |
| E | Storage Location | 35 | - |
| F | Collected Date | 12 | Date |
| G | Collected By | 20 | - |
| H | Verification Status | 18 | List: Verified, Pending, Expired |

## Sheet 11: Approval_SignOff

### Approver Roles
1. Records Manager
2. Legal Counsel
3. Chief Information Security Officer
4. IT Operations Manager
5. Compliance Officer

---

# Cell Styling Reference

## Colour Palette

| Style Name | Hex Code | Usage |
|------------|----------|-------|
| Header Fill | #1F4E79 | Sheet headers |
| Subheader Fill | #2E75B6 | Secondary headers |
| Column Header | #D6DCE4 | Table headers |
| Input Cell | #FFFFCC | User input cells |
| High Priority | #FF6B6B | Overdue/high risk |
| Medium Priority | #FFA94D | Approaching deadline |
| Low Priority | #69DB7C | On track |
| Compliant | #C6EFCE | Compliant status |
| Warning | #FFEB9C | Attention needed |
| Non-Compliant | #FFC7CE | Non-compliant |

---

# Integration Points

## Related Workbooks

| Workbook | Integration Type | Data Exchange |
|----------|-----------------|---------------|
| ISMS-IMP-A.5.32-33.S2 | Record categories | Uses protection classification |
| ISMS-IMP-A.5.32-33.S4 | Dashboard | Retention metrics feed dashboard |
| ISMS-IMP-A.8.10 | Secure deletion | Deletion methods alignment |

---

**END OF SPECIFICATION**

---

*"The cost of storage is not just dollars - it is also risk."*
-- Anonymous Records Manager

<!-- QA_VERIFIED: 2026-02-06 -->
