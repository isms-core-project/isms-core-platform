<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.32-33.S3-TG:framework:TG:a.5.32-33 -->
**ISMS-IMP-A.5.32-33.S3-TG - Retention and Disposal Schedule Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.33: Protection of Records

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Retention and Disposal Schedule Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.32-33.S3-TG |
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
- ISMS-IMP-A.5.32-33.S2 (Records Protection Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a532_33_3_retention_disposal.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.32-33.S3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Retention Schedule |
| 2 | Regulatory Mapping |
| 3 | Disposal Queue |
| 4 | Disposal Method Matrix |
| 5 | Destruction Verification |
| 6 | Exception Register |
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
| 3 | Retention Period |
| 4 | Retention Basis |
| 5 | Basis Detail |
| 6 | Retention Trigger |
| 7 | Grace Period |
| 8 | Review Cycle |
| 9 | Last Review |
| 10 | Next Review |
| 11 | Notes |
| 12 | Regulation ID |
| 13 | Regulation Name |
| 14 | Section/Article |
| 15 | Record Types Affected |
| 16 | Required Retention |
| 17 | Penalty for Non-Compliance |
| 18 | Reviewer |
| 19 | Queue ID |
| 20 | Record Category |
| 21 | Retention End Date |
| 22 | Volume - Physical |
| 23 | Volume - Electronic |
| 24 | Legal Hold Status |
| 25 | Disposal Priority |
| 26 | Target Disposal Date |
| 27 | Assigned To |
| 28 | Status |
| 29 | Classification |
| 30 | Physical - Paper |
| 31 | Physical - Media |
| 32 | Electronic - On-Prem |
| 33 | Electronic - Cloud |
| 34 | Verification Required |
| 35 | Approved Vendors |
| 36 | Special Handling |
| 37 | Destruction ID |
| 38 | Volume |
| 39 | Destruction Date |
| 40 | Method Used |
| 41 | Performed By |
| 42 | Witness |
| 43 | Certificate Reference |
| 44 | Storage Location |
| 45 | Verification Status |
| 46 | Exception ID |
| 47 | Exception Type |
| 48 | Original Retention |
| 49 | New Retention |
| 50 | Reason |
| 51 | Requested By |
| 52 | Approved By |
| 53 | Approval Date |
| 54 | Expiration |
| 55 | Gap ID |
| 56 | Gap Category |
| 57 | Description |
| 58 | Related Item |
| 59 | Risk Rating |
| 60 | Remediation Action |
| 61 | Owner |
| 62 | Due Date |
| 63 | Evidence ID |
| 64 | Evidence Type |
| 65 | Collected Date |
| 66 | Collected By |
| 67 | Assessment Area |
| 68 | Total Items |
| 69 | Compliant |
| 70 | Partial |
| 71 | Non-Compliant |
| 72 | N/A |
| 73 | Compliance % |
| 74 | Category |
| 75 | Finding |
| 76 | Count |
| 77 | Severity |
| 78 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Regulatory, Contractual, Business, Mixed, Creation, Year-End, Contract End
Last Activity, Event-Based, Annual, Biennial, Triennial, Yes, No, Checking
High, Medium, Low, Pending, In Progress, Complete, On Hold, Verified
Not Verified, Extension, Early Disposal, Active, Expired, Cancelled, Retention
Disposal, Verification, Process, Open, Certificate, Log, Approval, Report
Other, Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 78 columns, 47 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The cost of storage is not just dollars - it is also risk."*
-- Anonymous Records Manager

<!-- QA_VERIFIED: 2026-02-06 -->
