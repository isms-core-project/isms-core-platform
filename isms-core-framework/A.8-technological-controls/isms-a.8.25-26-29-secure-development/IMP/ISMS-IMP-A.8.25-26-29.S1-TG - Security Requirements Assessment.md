<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.25-26-29.S1-TG:framework:TG:a.8.25-26-29 -->
**ISMS-IMP-A.8.25-26-29.S1-TG - Security Requirements Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.25: Secure Development Life Cycle

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Security Requirements Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.25-26-29.S1-TG |
| **Related Policy** | ISMS-POL-A.8.25-26-29 (Secure Development) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.25 (Secure Development Life Cycle) |
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

- ISMS-POL-A.8.25-26-29 (Secure Development)
- ISMS-IMP-A.8.25-26-29.S2 (SDLC Security Activities Assessment)
- ISMS-IMP-A.8.25-26-29.S3 (Security Testing Results Assessment)
- ISMS-IMP-A.8.25-26-29.S4 (Vulnerability Remediation Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a825_26_29_1_security_requirements.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.25-26-29.S1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Application Inventory |
| 3 | Requirements Documentation |
| 4 | Threat Modelling |
| 5 | Architecture Review |
| 6 | Traceability Matrix |
| 7 | Evidence Register |
| 8 | Gap Analysis |
| 9 | Summary Dashboard |
| 10 | Approval Sign-Off |

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
| 1 | APPLICATION INVENTORY |
| 2 | COMPLETE INVENTORY OF ALL APPLICATIONS REQUIRING SECURITY REQUIREMENTS ASSESSMENT |
| 3 | SECURITY REQUIREMENTS DOCUMENTATION ASSESSMENT |
| 4 | ASSESS COMPLETENESS OF SECURITY REQUIREMENTS DOCUMENTATION PER APPLICATION |
| 5 | THREAT MODELING STATUS ASSESSMENT |
| 6 | ASSESS THREAT MODELING COMPLETION AND QUALITY PER APPLICATION |
| 7 | SECURITY ARCHITECTURE REVIEW STATUS |
| 8 | ASSESS SECURITY ARCHITECTURE REVIEW COMPLETION AND FINDINGS PER APPLICATION |
| 9 | REQUIREMENTS TRACEABILITY MATRIX STATUS |
| 10 | ASSESS REQUIREMENTS TRACEABILITY COMPLETENESS PER APPLICATION |
| 11 | GAP ANALYSIS & REMEDIATION TRACKING |
| 12 | TRACK SECURITY REQUIREMENTS GAPS AND REMEDIATION ACTIONS PER APPLICATION |
| 13 | Application Name |
| 14 | Application ID |
| 15 | Application Owner |
| 16 | Business Criticality |
| 17 | Risk Classification |
| 18 | Technology Stack |
| 19 | Deployment Model |
| 20 | Regulatory Scope |
| 21 | Internet Facing |
| 22 | Last Assessment Date |
| 23 | App-ID |
| 24 | Requirements Document Exists? |
| 25 | Document Location/Link |
| 26 | Last Updated |
| 27 | Requirements Approved? |
| 28 | Approver Name |
| 29 | Approval Date |
| 30 | Functional Requirements (%) |
| 31 | Non-Functional Requirements (%) |
| 32 | Data Protection Requirements (%) |
| 33 | Completeness Score (%) |
| 34 | Threat Model Exists? |
| 35 | Methodology Used |
| 36 | Threat Model Location/Link |
| 37 | DFD Created? |
| 38 | Threats Documented? |
| 39 | Mitigations Defined? |
| 40 | Approval Status |
| 41 | Review Conducted? |
| 42 | Review Date |
| 43 | Review Report Location/Link |
| 44 | Reviewers |
| 45 | Critical Findings |
| 46 | High Findings |
| 47 | Medium Findings |
| 48 | Low Findings |
| 49 | Open Findings |
| 50 | Traceability Matrix Exists? |
| 51 | Matrix Location/Link |
| 52 | Requirements → Design Traced? |
| 53 | Requirements → Code Traced? |
| 54 | Requirements → Tests Traced? |
| 55 | Traceability Coverage (%) |
| 56 | Quality Score (%) |
| 57 | Assessment Area |
| 58 | Total Assessed |
| 59 | Complete |
| 60 | Partial |
| 61 | Missing |
| 62 | N/A |
| 63 | Completion % |
| 64 | Finding |
| 65 | Count |
| 66 | Severity |
| 67 | Affected Area |
| 68 | Recommended Action |
| 69 | Owner |
| 70 | Gap ID |
| 71 | Gap Category |
| 72 | Gap Description |
| 73 | Risk Level |
| 74 | Remediation Action |
| 75 | Target Date |
| 76 | Status |
| 77 | Notes |
| 78 | Evidence ID |
| 79 | Evidence Type |
| 80 | Description |
| 81 | Location / Path |
| 82 | Date Collected |
| 83 | Collected By |
| 84 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, N/A, Partial, Planned, Scheduled, High Risk, Medium Risk, Low Risk
Approved, Pending, Not Approved, STRIDE, PASTA, LINDDUN, Other, Current
Outdated, Missing, Compliant, ⚠️ Partial Compliance, Non-Compliant
Security requirements doc, Code review report, Test report, Vulnerability scan
Penetration test, Remediation record, SDLC process doc, Screenshot
\u2705 Verified, \u26a0\ufe0f Pending, \u274c Not Verified, Draft, Final
Requires remediation, Re-assessment required, Approved with Conditions
Rejected, Deferred
```

**Extracted:** 10 sheets, 84 columns, 40 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"I remember once going to see him when he was ill at Putney. I had ridden in taxi cab number 1729 and remarked that the number seemed to me rather a dull one."*
— G.H. Hardy, about Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
