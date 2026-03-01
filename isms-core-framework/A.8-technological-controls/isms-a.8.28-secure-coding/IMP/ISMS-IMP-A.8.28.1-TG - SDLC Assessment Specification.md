<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.28.1-TG:framework:TG:a.8.28.1 -->
**ISMS-IMP-A.8.28.1-TG - SDLC Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | SDLC Assessment Specification |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.28.1-TG |
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
- ISMS-IMP-A.8.28.2 (Standards & Tools Assessment Specification)
- ISMS-IMP-A.8.28.3 (Code Review & Testing Assessment Specification)
- ISMS-IMP-A.8.28.4 (Third-Party & Open Source Software Assessment Specification)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a828_1_sdlc_assessment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.28.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Security Requirements Design |
| 3 | Development Environment |
| 4 | Build Deployment Pipeline |
| 5 | Security Testing Integration |
| 6 | Release Change Management |
| 7 | Evidence Register |
| 8 | Gap Analysis |
| 9 | Summary Dashboard |
| 10 | Approval Sign-Off |

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
| 1 | Requirement |
| 2 | Implementation Status |
| 3 | Evidence Reference |
| 4 | Comments |
| 5 | Assessment Area |
| 6 | Total Items |
| 7 | Compliant |
| 8 | Partial |
| 9 | Non-Compliant |
| 10 | N/A |
| 11 | Compliance % |
| 12 | Evidence ID |
| 13 | Evidence Type |
| 14 | Description |
| 15 | Location/Path |
| 16 | Date Collected |
| 17 | Collected By |
| 18 | Verification Status |
| 19 | Gap ID |
| 20 | Domain |
| 21 | Requirement ID |
| 22 | Requirement Description |
| 23 | Current State |
| 24 | Target State |
| 25 | Priority |
| 26 | Owner |
| 27 | Target Date |
| 28 | Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
✅ Implemented, ⚠️ Partially Implemented, ❌ Not Implemented, N/A, Yes, No
Partial, Unknown, Planned, Critical, High, Medium, Low, Negligible, Open
In Progress, Resolved, Closed, Deferred, Document, Screenshot, Report
Configuration, URL, Log File, Diagram, Policy, Procedure, Test Result
Scan Result, Other, Verified, Pending, Not Verified, Approved
Approved with Conditions, Rejected, Pending Review, Requirements, Design
Development, Testing, Deployment, Maintenance, SAST, SCA, DAST, Secret Scanner
Container Scanner, IaC Scanner, IDE Plugin, Unit, Integration, API, Security
Penetration, Performance, Regression, Continuous, Daily, Weekly, Monthly
Quarterly, On-Demand, Initial, Repeatable, Defined, Managed, Optimizing
Completed, Not Started, Staging, Production, All, Fully Automated
Partially Automated, Manual, Not Applicable, Fully Compliant, Mostly Compliant
Partially Compliant, Non-Compliant, Configuration file, Network scan
Documentation, Vendor spec, Certificate inventory, Audit log
Compliance report, Pending verification, Requires update, Draft, Final
Requires remediation, Re-assessment required
```

**Extracted:** 10 sheets, 28 columns, 95 validation values, 11 colors

---

**END OF SPECIFICATION**


---

*"Security is a process, not a product. It's also not a destination but a journey."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
