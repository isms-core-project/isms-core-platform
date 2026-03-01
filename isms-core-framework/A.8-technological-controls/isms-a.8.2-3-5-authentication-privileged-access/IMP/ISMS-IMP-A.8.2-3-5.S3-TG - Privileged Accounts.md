<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.2-3-5.S3-TG:framework:TG:a.8.2-3-5 -->
**ISMS-IMP-A.8.2-3-5.S3-TG - Privileged Account Inventory**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Privileged Accounts |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.2-3-5.S3-TG |
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
- ISMS-IMP-A.8.2-3-5.S2 (MFA Coverage)
- ISMS-IMP-A.8.2-3-5.S4 (Privileged Monitoring)
- ISMS-IMP-A.8.2-3-5.S5 (Access Restrictions)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a8235_3_privileged_accounts.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.2-3-5.S3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Privileged Account Inventory |
| 3 | Admin Tiering Matrix |
| 4 | Privileged User Roster |
| 5 | PAM Vault Coverage |
| 6 | MFA Hardware Tokens |
| 7 | Credential Rotation Status |
| 8 | Access Review Results |
| 9 | Tier Isolation Compliance |
| 10 | Evidence Register |
| 11 | Summary Dashboard |
| 12 | Approval Sign-Off |

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
| 1 | Total Non-Compliant Accounts: |
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
| 24 | Account ID |
| 25 | Account Name |
| 26 | Admin Tier |
| 27 | Compliance Status |
| 28 | MFA Status |
| 29 | PAM Status |
| 30 | Account Owner |
| 31 | Account Type |
| 32 | Privileged Role |
| 33 | System / Platform |
| 34 | Owner / Responsible |
| 35 | MFA Method |
| 36 | PAM Vaulted |
| 37 | Last Password Change |
| 38 | Password Rotation Freq |
| 39 | Last Access Review |
| 40 | System / Infrastructure |
| 41 | Tier Classification |
| 42 | Criticality |
| 43 | Security Requirements |
| 44 | User Name |
| 45 | User ID |
| 46 | Privileged Accounts Owned |
| 47 | Tier 0 Access |
| 48 | Tier 1 Access |
| 49 | Tier 2 Access |
| 50 | Business Justification |
| 51 | Last Review Date |
| 52 | Vault Date |
| 53 | JIT Enabled |
| 54 | Session Recording |
| 55 | Auto Rotation |
| 56 | Compliance |
| 57 | Tier 0 Account |
| 58 | Primary Token Serial |
| 59 | Backup Token Serial |
| 60 | Enrollment Date |
| 61 | Last Tested |
| 62 | Last Rotation |
| 63 | Rotation Frequency |
| 64 | Next Due |
| 65 | Days Until Due |
| 66 | Rotation Method |
| 67 | Review Period |
| 68 | User |
| 69 | Privileged Account |
| 70 | Access Confirmed |
| 71 | Access Removed |
| 72 | Reviewer |
| 73 | Review Date |
| 74 | Date |
| 75 | Account |
| 76 | Account Tier |
| 77 | System Accessed |
| 78 | System Tier |
| 79 | Violation Type |
| 80 | Investigation Status |
| 81 | Remediation |

### Data Validation Values

All dropdown/list values used across sheets:

```
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 12 sheets, 81 columns, 8 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Privilege is a liability. Grant least, review often."*
— Privileged access principle

<!-- QA_VERIFIED: 2026-03-01 -->
