<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.31.2-TG:framework:TG:a.8.31.2 -->
**ISMS-IMP-A.8.31.2-TG - Environment Access Control Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.31: Separation of Development, Test and Production Environments

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Environment Access Control |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.31.2-TG |
| **Related Policy** | ISMS-POL-A.8.31 (Environment Separation) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.31 (Separation of Development, Test and Production Environments) |
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

- ISMS-POL-A.8.31 (Environment Separation)
- ISMS-IMP-A.8.31.1 (Environment Architecture Implementation)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a831_2_environment_access.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.31.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | User Environment Access Matrix |
| 3 | Developer Production Access |
| 4 | Production Credential Audit |
| 5 | Cross Environment Access Log |
| 6 | Break Glass Access Log |
| 7 | MFA Enforcement |
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
| 1 | User ID / Email |
| 2 | Role |
| 3 | Development Access |
| 4 | Testing Access |
| 5 | Staging Access |
| 6 | Production Access |
| 7 | Compliance Status |
| 8 | Notes |
| 9 | Developer ID |
| 10 | Production Account/Sub |
| 11 | Production Access? |
| 12 | Access Type |
| 13 | Justification |
| 14 | Violation Severity |
| 15 | Remediation Action |
| 16 | Credential Type |
| 17 | System/Service |
| 18 | Stored in PAM Vault? |
| 19 | Vault Location |
| 20 | Last Rotated |
| 21 | Rotation Schedule |
| 22 | Compliance |
| 23 | Date/Time |
| 24 | User ID |
| 25 | Source Environment |
| 26 | Target Environment |
| 27 | Attempted Action |
| 28 | Result |
| 29 | Alert Generated? |
| 30 | Investigation Notes |
| 31 | Incident ID |
| 32 | Date/Time Activated |
| 33 | Approved By |
| 34 | Reason/Justification |
| 35 | Duration (hours) |
| 36 | Date/Time Revoked |
| 37 | Post-Incident Review |
| 38 | MFA Enabled? |
| 39 | MFA Type |
| 40 | Last MFA Check |
| 41 | Evidence |
| 42 | N/A - Compliant |
| 43 | PRODUCTION CREDENTIAL AUDIT |
| 44 | CROSS-ENVIRONMENT ACCESS ATTEMPTS LOG |
| 45 | BREAK-GLASS EMERGENCY ACCESS LOG |
| 46 | MFA ENFORCEMENT VERIFICATION |
| 47 | EVIDENCE REGISTER |
| 48 | ASSESSMENT APPROVAL AND SIGN-OFF |
| 49 | ASSESSMENT SUMMARY |
| 50 | FINAL DECISION: |
| 51 | NEXT REVIEW DETAILS |
| 52 | Assessment Area |
| 53 | Total Items |
| 54 | Compliant |
| 55 | Partial |
| 56 | Non-Compliant |
| 57 | N/A |
| 58 | Compliance % |
| 59 | Severity |
| 60 | Production Account |
| 61 | Status |
| 62 | Evidence ID |
| 63 | Evidence Type |
| 64 | Description |
| 65 | Location / Path |
| 66 | Date Collected |
| 67 | Collected By |
| 68 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, ✅ Yes, ❌ No, ➖ N/A, Full (CRUD), Read/Write, Read-only, No Access
Break-Glass Only, Compliant, Non-Compliant, Partial, Not Assessed, Developer
QA Engineer, DevOps Engineer, Operations Engineer, Security Analyst, Manager
Auditor, Other, Development, Testing, Staging, Production, Critical, High
Medium, Low, Configuration file, Screenshot, Log extract, Policy document
Training record, Audit report, Risk assessment, Interview notes, Test results
Verified, Pending Verification, Insufficient, Not Reviewed, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 68 columns, 51 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"We should be careful to get out of an experience only the wisdom that is in it."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
