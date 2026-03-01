<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.27.1-TG:framework:TG:a.8.27.1 -->
**ISMS-IMP-A.8.27.1-TG - Security Architecture Review Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.27: Secure System Architecture and Engineering Principles

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Security Architecture Review Process |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.27.1-TG |
| **Related Policy** | ISMS-POL-A.8.27 (Secure Systems Engineering) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.27 (Secure System Architecture and Engineering Principles) |
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

- ISMS-POL-A.8.27 (Secure Systems Engineering)
- ISMS-IMP-A.8.27.2 (Threat Modelling Methodology)
- ISMS-IMP-A.8.27.3 (Secure Architecture Pattern Catalogue)
- ISMS-IMP-A.8.27.4 (Zero Trust Implementation Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a827_1_architecture_review.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.27.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Governance |
| 2 | D |
| 3 | ✅ Implemented |
| 4 | ⚠️ Partial |
| 5 | ❌ Not Implemented |
| 6 | Process |
| 7 | ✅ Yes |
| 8 | ❌ No |
| 9 | Templates |
| 10 | E |
| 11 | 5 |
| 12 | 3 |
| 13 | 1 |
| 14 | Integration |
| 15 | Metrics |
| 16 | F |
| 17 | Up |
| 18 | Stable |
| 19 | Down |
| 20 | Compliance |
| 21 | Instructions & Legend |
| 22 | Evidence Register |
| 23 | Summary Dashboard |
| 24 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
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
| 1 | Security Team |
| 2 | Overall Compliance Score: |
| 3 | What This Shows |
| 4 | Critical Finding Type |
| 5 | Filter Instructions |
| 6 | Gov-ID |
| 7 | Category |
| 8 | Requirement |
| 9 | Status |
| 10 | Evidence |
| 11 | Gap |
| 12 | Owner |
| 13 | Notes |
| 14 | Proc-ID |
| 15 | Phase |
| 16 | Activity |
| 17 | Documented |
| 18 | Implemented |
| 19 | Effectiveness |
| 20 | Temp-ID |
| 21 | Template |
| 22 | Version |
| 23 | Last Updated |
| 24 | Completeness |
| 25 | Usability |
| 26 | Gaps |
| 27 | Int-ID |
| 28 | Integration |
| 29 | Trigger |
| 30 | Automated |
| 31 | Tracked |
| 32 | Enforced |
| 33 | Met-ID |
| 34 | Metric |
| 35 | Period |
| 36 | Target |
| 37 | Actual |
| 38 | Trend |
| 39 | Action |
| 40 | Comp-ID |
| 41 | Source |
| 42 | Compliant |
| 43 | Score |
| 44 | Assessment Area |
| 45 | Total Items |
| 46 | Partial |
| 47 | Non-Compliant |
| 48 | N/A |
| 49 | Compliance % |
| 50 | Evidence ID |
| 51 | Evidence Type |
| 52 | Description |
| 53 | Location / Path |
| 54 | Date Collected |
| 55 | Collected By |
| 56 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
✅ Implemented, ⚠️ Partial, ❌ Not Implemented, N/A, Policy, Procedures, Roles
Authority, Exceptions, ✅ Yes, ❌ No, 1, 2, 3, 4, 5, Trigger, Planning
Execution, Documentation, Approval, Follow-up, Up, Down, Stable
Policy Document, Process Record, System Screenshot, Configuration Export
Audit Log, Training Record, Test Result, Risk Assessment, Meeting Minutes
Other, ✅ Verified, ⚠️ Pending, ❌ Not Verified, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 24 sheets, 56 columns, 46 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Architecture is the foundation; security architecture is the foundation's foundation."*
— Gene Kim

<!-- QA_VERIFIED: [Date] -->
