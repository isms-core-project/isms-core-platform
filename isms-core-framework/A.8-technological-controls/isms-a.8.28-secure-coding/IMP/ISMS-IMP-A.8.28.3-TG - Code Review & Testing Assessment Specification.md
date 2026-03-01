<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.28.3-TG:framework:TG:a.8.28.3 -->
**ISMS-IMP-A.8.28.3-TG - Code Review & Testing Assessment Specification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Code Review & Testing Assessment Specification |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.28.3-TG |
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
- ISMS-IMP-A.8.28.4 (Third-Party & Open Source Software Assessment Specification)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a828_3_code_review_testing.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.28.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Code Review Process |
| 3 | Security Champion Review |
| 4 | Unit Integration Testing |
| 5 | API Application Testing |
| 6 | External Testing Validation |
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
Partial, Unknown, Excellent, Good, Fair, Poor, Not Assessed, Complete (>95%)
High (80-95%), Medium (60-79%), Low (<60%), Every Change, Daily, Weekly
Monthly, Quarterly, On-Demand, Never, Critical, High, Medium, Low, Negligible
Open, In Progress, Resolved, Closed, Deferred, Review Log, Test Result
Pentest Report, Bug Bounty Submission, Training Record, Policy Document
Tool Output, Screenshot, Other, Peer Review, Security Champion Review
Architecture Review, Design Review, Post-Incident Review, Unit Test
Integration Test, API Test, Security Test, Penetration Test, Regression Test
Smoke Test, Passing, Failing, Flaky, Disabled, Not Run, Fully Automated
Partially Automated, Manual, Not Applicable, Informational, Fixed
Accepted Risk, False Positive, Fully Compliant, Mostly Compliant
Partially Compliant, Non-Compliant, Completed, Not Started, Approved
Approved with Conditions, Rejected, Pending Review, Configuration file
Network scan, Documentation, Vendor spec, Certificate inventory, Audit log
Compliance report, Verified, Pending verification, Not verified
Requires update, Draft, Final, Requires remediation, Re-assessment required
```

**Extracted:** 10 sheets, 28 columns, 93 validation values, 11 colors

---

**END OF SPECIFICATION**


---

*"You can't encrypt your way out of a fundamentally insecure design."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
