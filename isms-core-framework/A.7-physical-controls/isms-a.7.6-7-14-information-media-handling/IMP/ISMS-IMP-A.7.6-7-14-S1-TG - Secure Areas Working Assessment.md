<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.6-7-14-S1-TG:framework:TG:a.7.6-7-14-s1 -->
**ISMS-IMP-A.7.6-7-14-S1-TG - Secure Areas Working Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.6: Working in Secure Areas

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Secure Areas Working Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.6-7-14-S1-TG |
| **Related Policy** | ISMS-POL-A.7.6-7-14-S1 (Information Media Handling) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.6 (Working in Secure Areas) |
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

- ISMS-POL-A.7.6-7-14-S1 (Information Media Handling)
- ISMS-IMP-A.7.6-7-14-S2 (Clear Desk Screen Compliance)
- ISMS-IMP-A.7.6-7-14-S3 (Equipment Disposal Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a76_1_secure_areas.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.6.S1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Secure Area Register |
| 3 | Working Procedures |
| 4 | Third-Party Access |
| 5 | Incidents |
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
| 1 | Secure Area ID |
| 2 | Secure Area Name |
| 3 | Location |
| 4 | Classification |
| 5 | Access Control Type |
| 6 | Authorised Personnel |
| 7 | Last Access Review |
| 8 | Emergency Procedures |
| 9 | Recording Controls |
| 10 | Unsupervised Working |
| 11 | Status |
| 12 | Notes |
| 13 | Requirement ID |
| 14 | Requirement Description |
| 15 | Implementation Status |
| 16 | Evidence |
| 17 | Access Period |
| 18 | Secure Area |
| 19 | Visitor/Contractor Count |
| 20 | Escort Compliance % |
| 21 | NDA Status |
| 22 | Time Limit Compliance |
| 23 | Equipment Inspected |
| 24 | Incident ID |
| 25 | Date |
| 26 | Incident Type |
| 27 | Severity |
| 28 | Description |
| 29 | Response Time (min) |
| 30 | Resolution Status |
| 31 | Corrective Action |
| 32 | Assessment Area |
| 33 | Total Items |
| 34 | Compliant |
| 35 | Partial |
| 36 | Non-Compliant |
| 37 | N/A |
| 38 | Compliance % |
| 39 | Evidence ID |
| 40 | Evidence Type |
| 41 | Location/Path |
| 42 | Date Collected |
| 43 | Collected By |
| 44 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Tier 1 - Critical, Tier 2 - Standard, Badge + PIN, Biometric, Badge Only
Mantrap, Key Lock, Yes, No, Prohibited, Authorised Only, No Restriction
Restricted, Allowed, Implemented, Partial, Not Implemented, N/A
Unauthorised Access, Procedure Violation, Tailgating
Equipment Policy Violation, Recording Violation, Other, Critical, High, Medium
Low, Resolved, In Progress, Escalated, Approved, Approved with Conditions
Rejected, Deferred, Policy document, Procedure document, Screenshot
Photograph, Audit report, Training record, Configuration file, Verified
Pending verification, Not verified, Requires update, Draft, Final
Requires remediation, Re-assessment required
```

**Extracted:** 8 sheets, 44 columns, 50 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Security is not a product, but a process."*
— Bruce Schneier

<!-- QA_VERIFIED: 2026-03-01 -->
