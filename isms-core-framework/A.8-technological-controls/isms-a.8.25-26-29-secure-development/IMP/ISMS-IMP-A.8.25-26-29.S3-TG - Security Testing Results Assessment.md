<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.25-26-29.S3-TG:framework:TG:a.8.25-26-29 -->
**ISMS-IMP-A.8.25-26-29.S3-TG - Security Testing Results Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.25: Secure Development Life Cycle

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Security Testing Results Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.25-26-29.S3-TG |
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
- ISMS-IMP-A.8.25-26-29.S1 (Security Requirements Assessment)
- ISMS-IMP-A.8.25-26-29.S2 (SDLC Security Activities Assessment)
- ISMS-IMP-A.8.25-26-29.S4 (Vulnerability Remediation Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a825_26_29_3_security_testing_results.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.25-26-29.S3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Security Testing Coverage |
| 3 | SAST Scan Results |
| 4 | DAST Scan Results |
| 5 | SCA Scan Results |
| 6 | Penetration Testing Results |
| 7 | Security Acceptance Testing |
| 8 | Evidence Register |
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
| 1 | SECURITY TESTING COVERAGE OVERVIEW |
| 2 | TRACK SECURITY TESTING COVERAGE ACROSS ALL TESTING TYPES PER APPLICATION |
| 3 | TRACK SAST SCAN FINDINGS BY SEVERITY AND REMEDIATION STATUS |
| 4 | TRACK DAST SCAN FINDINGS BY SEVERITY AND SCAN TYPE |
| 5 | TRACK VULNERABLE DEPENDENCIES AND LICENSE COMPLIANCE |
| 6 | PENETRATION TESTING RESULTS |
| 7 | TRACK PENETRATION TESTING FINDINGS AND REMEDIATION |
| 8 | SECURITY ACCEPTANCE TESTING |
| 9 | TRACK SECURITY TEST CASE EXECUTION AND PASS RATES |
| 10 | Application Name |
| 11 | SAST Enabled? |
| 12 | Last SAST Scan |
| 13 | DAST Enabled? |
| 14 | Last DAST Scan |
| 15 | SCA Enabled? |
| 16 | Last SCA Scan |
| 17 | Pentest Status |
| 18 | Last Pentest Date |
| 19 | Coverage Score (%) |
| 20 | Last Scan Date |
| 21 | Critical Findings |
| 22 | High Findings |
| 23 | Medium Findings |
| 24 | Low Findings |
| 25 | Total Findings |
| 26 | Findings Remediated |
| 27 | Remediation Rate (%) |
| 28 | Trend vs. Previous |
| 29 | Scan Type |
| 30 | Remediation Status |
| 31 | Next Scan Date |
| 32 | Critical Vulns |
| 33 | High Vulns |
| 34 | Medium Vulns |
| 35 | Low Vulns |
| 36 | Total Vulns |
| 37 | License Issues |
| 38 | Outdated Deps |
| 39 | Pentest Date |
| 40 | Pentester |
| 41 | Retest Date |
| 42 | Findings Resolved |
| 43 | Closure Rate (%) |
| 44 | App-ID |
| 45 | Release Version |
| 46 | Test Cases Total |
| 47 | Test Cases Passed |
| 48 | Test Cases Failed |
| 49 | Test Cases N/A |
| 50 | Pass Rate (%) |
| 51 | Security Sign-Off |
| 52 | Assessment Area |
| 53 | Total Assessed |
| 54 | Complete |
| 55 | Partial |
| 56 | Missing |
| 57 | N/A |
| 58 | Completion % |
| 59 | Finding |
| 60 | Count |
| 61 | Severity |
| 62 | Affected Area |
| 63 | Recommended Action |
| 64 | Owner |
| 65 | Evidence ID |
| 66 | Evidence Type |
| 67 | Description |
| 68 | Location / Path |
| 69 | Date Collected |
| 70 | Collected By |
| 71 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, N/A, Baseline, Full, API, Authenticated, Internal, External, Both
Passed, Failed, In Progress, Approved, Pending, Rejected, Current, Outdated
Missing, Compliant, ⚠️ Partial Compliance, Non-Compliant, Test report
SAST report, DAST report, SCA report, Penetration test, Vulnerability scan
Code review report, Screenshot, Other, \u2705 Verified, \u26a0\ufe0f Pending
\u274c Not Verified, Draft, Final, Requires remediation
Re-assessment required, Approved with Conditions, Deferred
```

**Extracted:** 10 sheets, 71 columns, 40 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"My brain is open to mathematics. When I'm not working, I'm not really living."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
