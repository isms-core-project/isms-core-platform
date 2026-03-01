<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.2-3-5.S2-TG:framework:TG:a.8.2-3-5 -->
**ISMS-IMP-A.8.2-3-5.S2-TG - MFA Coverage Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | MFA Coverage |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.2-3-5.S2-TG |
| **Related Policy** | ISMS-POL-A.8.2-3-5 (Authentication Privileged Access) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.2 (Privileged Access Rights) |
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

- ISMS-POL-A.8.2-3-5 (Authentication Privileged Access)
- ISMS-IMP-A.8.2-3-5.S1 (Authentication Inventory)
- ISMS-IMP-A.8.2-3-5.S3 (Privileged Accounts)
- ISMS-IMP-A.8.2-3-5.S4 (Privileged Monitoring)
- ISMS-IMP-A.8.2-3-5.S5 (Access Restrictions)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a8235_2_mfa_coverage.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.2-3-5.S2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | User MFA Enrollment |
| 3 | MFA Coverage By Type |
| 4 | MFA Method Analysis |
| 5 | MFA Gaps Priority |
| 6 | Enrollment Campaign |
| 7 | Backup Method Status |
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
| 1 | Total Critical/High MFA Gaps: |
| 2 | Evidence ID |
| 3 | Control Ref |
| 4 | Evidence Type |
| 5 | Description |
| 6 | Location / Reference |
| 7 | Date Collected |
| 8 | Collected By |
| 9 | Verification Status |
| 10 | Assessment Area |
| 11 | Total Items |
| 12 | Compliant |
| 13 | Partial |
| 14 | Non-Compliant |
| 15 | N/A |
| 16 | Compliance % |
| 17 | KPI |
| 18 | Current Value |
| 19 | Target |
| 20 | Status |
| 21 | Last Updated |
| 22 | Owner |
| 23 | Notes |
| 24 | Finding ID |
| 25 | User / Group |
| 26 | Gap Description |
| 27 | Priority |
| 28 | MFA Required |
| 29 | Target Date |
| 30 | User ID / Email |
| 31 | User Name |
| 32 | User Type |
| 33 | Department |
| 34 | MFA Status |
| 35 | MFA Method |
| 36 | Backup Method |
| 37 | Enrollment Date |
| 38 | Last Verified |
| 39 | Enrollment Deadline |
| 40 | Days Overdue |
| 41 | Compliance Status |
| 42 | User Type Category |
| 43 | Total Users |
| 44 | MFA Enrolled |
| 45 | Not Enrolled |
| 46 | Coverage % |
| 47 | Target % |
| 48 | Gap |
| 49 | Compliance |
| 50 | Users Using |
| 51 | Security Rating |
| 52 | Phishing Resistant |
| 53 | Deployment Date |
| 54 | Replacement Plan |
| 55 | User ID |
| 56 | Risk Level |
| 57 | Remediation Plan |
| 58 | Campaign Phase |
| 59 | Target Group |
| 60 | Start Date |
| 61 | End Date |
| 62 | Users Targeted |
| 63 | Users Enrolled |
| 64 | Completion % |
| 65 | Primary MFA |
| 66 | Backup Method Registered |
| 67 | Backup Method Type |
| 68 | Last Tested |

### Data Validation Values

All dropdown/list values used across sheets:

```
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 68 columns, 8 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Multi-factor authentication is the simplest defence against credential theft."*
— Access security principle

<!-- QA_VERIFIED: 2026-03-01 -->
