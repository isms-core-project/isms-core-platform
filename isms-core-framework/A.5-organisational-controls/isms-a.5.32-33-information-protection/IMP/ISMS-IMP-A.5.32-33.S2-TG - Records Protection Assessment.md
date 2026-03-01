<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.32-33.S2-TG:framework:TG:a.5.32-33 -->
**ISMS-IMP-A.5.32-33.S2-TG - Records Protection Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.33: Protection of Records

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Records Protection Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.32-33.S2-TG |
| **Related Policy** | ISMS-POL-A.5.32-33 (Information Protection) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.33 (Protection of Records) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.5.32-33 (Information Protection)
- ISMS-IMP-A.5.32-33.S1 (IP Rights Inventory and Compliance Assessment)
- ISMS-IMP-A.5.32-33.S3 (Retention and Disposal Schedule Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a532_33_2_records_protection.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.32-33.S2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Records Category Inventory |
| 2 | Protection Controls |
| 3 | Integrity Verification |
| 4 | Access Control Review |
| 5 | Legal Hold Register |
| 6 | Backup Verification |
| 7 | Gap Analysis |
| 8 | Evidence Register |
| 9 | Summary Dashboard |
| 10 | Approval Sign-Off |
| 11 | Instructions & Legend |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #C00000 | Dark Red (Blocked) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | Record Category ID |
| 2 | Category Name |
| 3 | Record Type |
| 4 | Description |
| 5 | Custodian Department |
| 6 | Storage Location |
| 7 | Format |
| 8 | Retention Requirement |
| 9 | Confidentiality |
| 10 | Integrity Requirement |
| 11 | Availability Requirement |
| 12 | Notes |
| 13 | Confidentiality Controls |
| 14 | Integrity Controls |
| 15 | Availability Controls |
| 16 | Physical Controls |
| 17 | Control Effectiveness |
| 18 | Gap Description |
| 19 | Remediation Needed |
| 20 | Status |
| 21 | Test ID |
| 22 | Record Category |
| 23 | Integrity Mechanism |
| 24 | Test Date |
| 25 | Test Performed |
| 26 | Expected Result |
| 27 | Actual Result |
| 28 | Issues |
| 29 | Remediation |
| 30 | System Name |
| 31 | Record Categories |
| 32 | Access Control Type |
| 33 | User Count |
| 34 | Privileged Users |
| 35 | Last Access Review |
| 36 | Access Logging |
| 37 | Log Retention |
| 38 | Hold ID |
| 39 | Matter Name |
| 40 | Legal Counsel |
| 41 | Effective Date |
| 42 | Custodians Notified |
| 43 | Notification Date |
| 44 | Release Date |
| 45 | Backup System |
| 46 | Backup Frequency |
| 47 | Backup Location |
| 48 | Last Backup Date |
| 49 | Last Verification |
| 50 | Last Recovery Test |
| 51 | RTO Target |
| 52 | RTO Achieved |
| 53 | RPO Target |
| 54 | RPO Achieved |
| 55 | Gap ID |
| 56 | Gap Category |
| 57 | Related Record Category |
| 58 | Risk Rating |
| 59 | Remediation Action |
| 60 | Owner |
| 61 | Due Date |
| 62 | Evidence ID |
| 63 | Evidence Type |
| 64 | Related Item |
| 65 | Collected Date |
| 66 | Collected By |
| 67 | Verification Status |
| 68 | Assessment Area |
| 69 | Total Items |
| 70 | Compliant |
| 71 | Partial |
| 72 | Non-Compliant |
| 73 | N/A |
| 74 | Compliance % |
| 75 | Category |
| 76 | Finding |
| 77 | Count |
| 78 | Severity |
| 79 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Financial, Personnel, Legal, Operational, Technical, Security, Regulatory
Physical, Electronic, Both, Restricted, Confidential, Internal, Public
Critical, High, Standard, Mission Critical, Business Critical, Effective
Partial, Ineffective, Complete, In Progress, Not Started, Checksum
Digital Signature, WORM, Audit Log, Database Constraints, Other, Pass, Fail
Not Tested, RBAC, DAC, MAC, Mixed, Yes, No, Compliant, Non-Compliant, Active
Released, Pending, Real-time, Hourly, Daily, Weekly, Monthly, Confidentiality
Integrity, Availability, Process, Medium, Low, Open, Accepted, Document
Screenshot, Report, Log, Configuration, Verified, Pending Review, Not Verified
Expired, Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 79 columns, 75 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Records management is not just about what you keep, but how you keep it."*
-- Anonymous

<!-- QA_VERIFIED: 2026-02-06 -->
