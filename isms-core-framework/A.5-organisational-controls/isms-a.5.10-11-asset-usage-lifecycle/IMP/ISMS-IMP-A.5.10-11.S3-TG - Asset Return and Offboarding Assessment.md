<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.10-11.S3-TG:framework:TG:a.5.10-11 -->
**ISMS-IMP-A.5.10-11.S3-TG - Asset Return and Offboarding Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.11

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Asset Return and Offboarding Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.10-11.S3-TG |
| **Related Policy** | ISMS-POL-A.5.10-11 (Asset Usage Lifecycle) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.11) |
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

- ISMS-POL-A.5.10-11 (Asset Usage Lifecycle)
- ISMS-IMP-A.5.10-11.S1 (Acceptable Use Policy Assessment)
- ISMS-IMP-A.5.10-11.S2 (Usage Rules Inventory)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a510_11_3_asset_return_offboarding.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.10-11.S3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Return Process |
| 3 | Asset Checklist |
| 4 | Offboarding Tracking |
| 5 | Access Revocation |
| 6 | Evidence Register |
| 7 | Summary Dashboard |
| 8 | Approval Sign-Off |

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
| 1 | Assessment Area |
| 2 | Total Items |
| 3 | Compliant |
| 4 | Partial |
| 5 | Non-Compliant |
| 6 | N/A |
| 7 | Compliance % |
| 8 | Metric |
| 9 | Value |
| 10 | Category |
| 11 | Finding |
| 12 | Count |
| 13 | Severity |
| 14 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, Partial, No, Compliant, Gap Identified, Remediation In Progress, Optional
Verify, N/A, Employee, Contractor, Consultant, Intern, Temp, Resignation
Termination, Contract End, Transfer, Retirement, Other, Complete, In Progress
Pending, Overdue, Network, VPN, Email, Application, Database, Cloud, Physical
Admin, AD Query, System Log, Login Attempt, Screenshot, Attestation
Sign-off Form, AD Export, Email Confirmation, Checklist, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 8 sheets, 14 columns, 49 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
