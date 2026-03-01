<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.32-33.S1-TG:framework:TG:a.5.32-33 -->
**ISMS-IMP-A.5.32-33.S1-TG - IP Rights Inventory and Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.32: Intellectual Property Rights

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | IP Rights Inventory and Compliance Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.32-33.S1-TG |
| **Related Policy** | ISMS-POL-A.5.32-33 (Information Protection) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.32 (Intellectual Property Rights) |
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
- ISMS-IMP-A.5.32-33.S2 (Records Protection Assessment)
- ISMS-IMP-A.5.32-33.S3 (Retention and Disposal Schedule Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a532_33_1_ip_rights_inventory.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.32-33.S1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | IP Asset Inventory |
| 2 | IP Protection Assessment |
| 3 | Third-Party IP Register |
| 4 | Software License Compliance |
| 5 | Gap Analysis |
| 6 | Evidence Register |
| 7 | Summary Dashboard |
| 8 | Approval Sign-Off |
| 9 | Instructions & Legend |

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
| 1 | IP Asset ID |
| 2 | IP Asset Name |
| 3 | IP Category |
| 4 | Description |
| 5 | IP Owner |
| 6 | Custodian |
| 7 | Legal Protection Status |
| 8 | Business Value |
| 9 | Classification |
| 10 | Creation Date |
| 11 | Last Review |
| 12 | Notes |
| 13 | Access Control |
| 14 | Technical Controls |
| 15 | Administrative Controls |
| 16 | Physical Controls |
| 17 | Legal Protection |
| 18 | Control Effectiveness |
| 19 | Gap Description |
| 20 | Remediation Needed |
| 21 | Status |
| 22 | Third-Party IP ID |
| 23 | Software/Content Name |
| 24 | Vendor |
| 25 | License Type |
| 26 | License Quantity |
| 27 | Deployed Quantity |
| 28 | Compliance Status |
| 29 | Contract Reference |
| 30 | Renewal Date |
| 31 | Open Source License |
| 32 | Software Name |
| 33 | License Model |
| 34 | Entitled |
| 35 | Deployed |
| 36 | Variance |
| 37 | Compliance Risk |
| 38 | Remediation Action |
| 39 | Due Date |
| 40 | Gap ID |
| 41 | Gap Category |
| 42 | Related IP |
| 43 | Risk Rating |
| 44 | Owner |
| 45 | Evidence ID |
| 46 | Evidence Type |
| 47 | Related Item |
| 48 | Storage Location |
| 49 | Collected Date |
| 50 | Collected By |
| 51 | Verification Status |
| 52 | Assessment Area |
| 53 | Total Items |
| 54 | Compliant |
| 55 | Partial |
| 56 | Non-Compliant |
| 57 | N/A |
| 58 | Compliance % |
| 59 | Category |
| 60 | Finding |
| 61 | Count |
| 62 | Severity |
| 63 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Trade Secret, Patent, Copyright, Trademark, Registered, Pending, Unregistered
N/A, High, Medium, Low, Restricted, Confidential, Internal, Public, Effective
Partial, Ineffective, Complete, In Progress, Not Started, Perpetual
Subscription, Open Source, Freeware, Compliant, Over-deployed, Under-utilised
GPL, Apache, MIT, BSD, LGPL, MPL, Other, Named User, Device, Enterprise
Per Core, None, Open, Protection, Compliance, Documentation, Process, Accepted
Document, Screenshot, Report, Configuration, Certificate, Verified
Pending Review, Not Verified, Expired, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 63 columns, 63 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The only thing worse than training employees and losing them is not training them and keeping them."*
-- Zig Ziglar

<!-- QA_VERIFIED: 2026-02-06 -->
