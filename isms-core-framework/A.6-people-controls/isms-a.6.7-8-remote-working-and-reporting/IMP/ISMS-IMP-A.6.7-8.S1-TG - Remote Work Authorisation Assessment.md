<!-- ISMS-CORE:IMP:ISMS-IMP-A.6.7-8.S1-TG:framework:TG:a.6.7-8 -->
**ISMS-IMP-A.6.7-8.S1-TG - Remote Work Authorisation Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Remote Work Authorisation Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.6.7-8.S1-TG |
| **Related Policy** | ISMS-POL-A.6.7-8 (Remote Working and Reporting) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting) |
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

- ISMS-POL-A.6.7-8 (Remote Working and Reporting)
- ISMS-IMP-A.6.7-8.S2 (Technical Controls Assessment)
- ISMS-IMP-A.6.7-8.S3 (Endpoint and Physical Security Assessment)
- ISMS-IMP-A.6.7-8.S4 (Event Reporting Mechanisms Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a678_s1_remote_work_authorisation.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.6.7-8.S1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Eligibility Criteria |
| 3 | Authorisation Register |
| 4 | Risk Assessment |
| 5 | Physical Security |
| 6 | Acknowledgments |
| 7 | Gap Analysis |
| 8 | Evidence Register |
| 9 | Summary Dashboard |
| 10 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #666666 | Dark Gray (Secondary Text) |
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
| 1 | Criterion |
| 2 | Description |
| 3 | Importance |
| 4 | Documented |
| 5 | Evidence |
| 6 | Notes |
| 7 | Auth ID |
| 8 | Employee Name |
| 9 | Department |
| 10 | Role |
| 11 | Remote Type |
| 12 | Request Date |
| 13 | Risk Assessment |
| 14 | Physical Assessment |
| 15 | Acknowledgment |
| 16 | Status |
| 17 | Approval Date |
| 18 | Review Date |
| 19 | Scoring Guide |
| 20 | Max Score |
| 21 | Employee |
| 22 | Data Class |
| 23 | Physical |
| 24 | Network |
| 25 | Device |
| 26 | Regulatory |
| 27 | Total |
| 28 | Risk Level |
| 29 | Requirement |
| 30 | Requirement Level |
| 31 | Verification Method |
| 32 | Assessment Date |
| 33 | All Mandatory Met |
| 34 | Conditional Items |
| 35 | Overall Status |
| 36 | Next Review |
| 37 | Policy Version |
| 38 | Acknowledgment Date |
| 39 | Method |
| 40 | Expiry Date |
| 41 | Evidence Reference |
| 42 | Gap ID |
| 43 | Source Area |
| 44 | Gap Description |
| 45 | Affected Scope |
| 46 | Remediation Action |
| 47 | Owner |
| 48 | Target Date |
| 49 | Evidence ID |
| 50 | Evidence Type |
| 51 | Source / Owner |
| 52 | Date Collected |
| 53 | Retention Period |
| 54 | Storage Location |
| 55 | Assessment Area |
| 56 | Total Items |
| 57 | Compliant |
| 58 | Partial |
| 59 | Non-Compliant |
| 60 | N/A |
| 61 | Compliance % |
| 62 | Category |
| 63 | Finding |
| 64 | Count |
| 65 | Severity |
| 66 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Partial, Full-Time, Part-Time, Occasional, Travel Only, Complete
Pending, N/A, Low, Medium, High, Critical, Compliant, Non-Compliant
Pending Review, Electronic Signature, Physical Signature, LMS Completion
Email Confirmation, Current, Expired, Eligibility, Authorisation
Risk Assessment, Physical Security, Acknowledgment, Open, In Progress
Resolved, Accepted, Collected, Not Available, Superseded, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 66 columns, 43 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"The only truly secure system is one that is powered off, cast in a block of concrete, and sealed in a lead-lined room with armed guards."*
— Gene Spafford

<!-- QA_VERIFIED: 2026-03-01 -->
