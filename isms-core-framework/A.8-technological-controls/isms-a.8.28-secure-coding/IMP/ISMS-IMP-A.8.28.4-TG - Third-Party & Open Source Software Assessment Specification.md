<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.28.4-TG:framework:TG:a.8.28.4 -->
**ISMS-IMP-A.8.28.4-TG - Third-Party & Open Source Software Assessment Specification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Third-Party & Open Source Software Assessment Specification |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.28.4-TG |
| **Related Policy** | ISMS-POL-A.8.28 (Secure Coding) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.28 (Secure Coding) |
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

- ISMS-POL-A.8.28 (Secure Coding)
- ISMS-IMP-A.8.28.1 (SDLC Assessment Specification)
- ISMS-IMP-A.8.28.2 (Standards & Tools Assessment Specification)
- ISMS-IMP-A.8.28.3 (Code Review & Testing Assessment Specification)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a828_4_third_party_oss.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.28.4`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Summary Dashboard |
| 2 | Evidence Register |
| 3 | Gap Analysis |
| 4 | Approval Sign-Off |
| 5 | Vendor Security Assessment |
| 6 | OSS Management |
| 7 | Dependency Vulnerability Mgmt |
| 8 | Third-Party Code & Integration |
| 9 | License Compliance & Legal Risk |
| 10 | Instructions & Legend |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #666666 | Dark Gray (Secondary Text) |
| #808080 | Gray (Disabled) |
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
| 1 | GAP ANALYSIS & REMEDIATION PLAN |
| 2 | Requirement |
| 3 | Implementation Status |
| 4 | Evidence Reference |
| 5 | Comments |
| 6 | Assessment Area |
| 7 | Total Items |
| 8 | Compliant |
| 9 | Partial |
| 10 | Non-Compliant |
| 11 | N/A |
| 12 | Compliance % |
| 13 | Evidence ID |
| 14 | Evidence Type |
| 15 | Description |
| 16 | Location/Path |
| 17 | Date Collected |
| 18 | Collected By |
| 19 | Verification Status |
| 20 | Gap ID |
| 21 | Domain |
| 22 | Requirement ID |
| 23 | Requirement Description |
| 24 | Current State |
| 25 | Target State |
| 26 | Priority |
| 27 | Owner |
| 28 | Target Date |
| 29 | Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
✅ Implemented, ⚠️ Partially Implemented, ❌ Not Implemented, N/A, Yes, No
Critical, High, Medium, Low, Open, In Progress, Resolved, Closed, Deferred
Document, Screenshot, Report, Configuration, URL, Recording, Database Query
Log File, Other, Pending, Verified, Rejected, Approved
Approved with Conditions, Pending Review, Vendor Security Assessment
OSS Management, Dependency Vulnerability Mgmt, Third-Party Code & Integration
License Compliance & Legal Risk, Configuration file, Network scan
Documentation, Vendor spec, Certificate inventory, Audit log
Compliance report, Pending verification, Not verified, Requires update, Draft
Final, Requires remediation, Re-assessment required
```

**Extracted:** 10 sheets, 29 columns, 49 validation values, 11 colors

---

**END OF SPECIFICATION**


---

*"Complexity is the enemy of security."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
