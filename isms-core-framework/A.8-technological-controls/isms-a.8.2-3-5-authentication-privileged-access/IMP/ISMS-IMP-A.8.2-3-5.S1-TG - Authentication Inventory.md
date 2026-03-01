<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.2-3-5.S1-TG:framework:TG:a.8.2-3-5 -->
**ISMS-IMP-A.8.2-3-5.S1-TG - Authentication Inventory & Methods**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Authentication Inventory |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.2-3-5.S1-TG |
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
- ISMS-IMP-A.8.2-3-5.S2 (MFA Coverage)
- ISMS-IMP-A.8.2-3-5.S3 (Privileged Accounts)
- ISMS-IMP-A.8.2-3-5.S4 (Privileged Monitoring)
- ISMS-IMP-A.8.2-3-5.S5 (Access Restrictions)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a8235_1_authentication_inventory.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.2-3-5.S1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Authentication Inventory |
| 3 | Protocol Analysis |
| 4 | SSO Integration Status |
| 5 | Password Policy |
| 6 | MFA Availability |
| 7 | Legacy Authentication |
| 8 | Gap Analysis |
| 9 | Evidence Register |
| 10 | Summary Dashboard |
| 11 | Approval Sign-Off |

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
| 1 | Total Critical/High Findings: |
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
| 25 | Affected Area |
| 26 | Severity |
| 27 | Due Date |
| 28 | System / Application |
| 29 | System Type |
| 30 | Environment |
| 31 | Primary Auth Method |
| 32 | Auth Protocol |
| 33 | Identity Provider |
| 34 | SSO Integrated |
| 35 | MFA Available |
| 36 | MFA Method |
| 37 | Password Policy |
| 38 | Security Rating |
| 39 | Compliance Status |
| 40 | Notes / Gaps |
| 41 | Protocol Name |
| 42 | Systems Using |
| 43 | Security Level |
| 44 | TLS Required |
| 45 | TLS Version |
| 46 | Deprecation Status |
| 47 | Compliance Rating |
| 48 | Remediation Plan |
| 49 | Target Date |
| 50 | Application Name |
| 51 | Application Type |
| 52 | User Count |
| 53 | SSO Status |
| 54 | SSO Protocol |
| 55 | Integration Date |
| 56 | SSO Platform |
| 57 | Integration Effort |
| 58 | Business Priority |
| 59 | System / Platform |
| 60 | Policy Enforced |
| 61 | Min Length |
| 62 | Complexity Req |
| 63 | Password Expiry |
| 64 | History Count |
| 65 | Breach Detection |
| 66 | Lockout Threshold |
| 67 | Compliance Score |
| 68 | Gaps Identified |

### Data Validation Values

All dropdown/list values used across sheets:

```
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred, Yes, No, In Progress
Not Supported, Planned, Compliant, Partial, Non-Compliant, N/A (Certificate)
Strong, Adequate, Weak, Legacy/Insecure, N/A, TLS 1.3, TLS 1.2
TLS 1.1 (Deprecated), TLS 1.0 (Insecure), No TLS, Active - Recommended
Active - Acceptable, Deprecated - Migrate, Prohibited - Block, SaaS
On-Premises Web App, Cloud Service, Internal Portal, Database, Legacy, Other
Integrated, Password Vaulting, Not Assessed, SAML 2.0, OAuth 2.0
OpenID Connect, WS-Federation, Low (Pre-built), Medium (Custom Config)
High (Development), Not Possible, Never (Recommended), 90 Days, 60 Days
30 Days, Custom
```

**Extracted:** 11 sheets, 68 columns, 54 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Identity is the new perimeter."*
— Zero Trust principle

<!-- QA_VERIFIED: 2026-03-01 -->
