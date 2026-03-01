<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.2-3-5.S5-TG:framework:TG:a.8.2-3-5 -->
**ISMS-IMP-A.8.2-3-5.S5-TG - Access Restrictions Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Access Restrictions |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.2-3-5.S5-TG |
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
- ISMS-IMP-A.8.2-3-5.S3 (Privileged Accounts)
- ISMS-IMP-A.8.2-3-5.S4 (Privileged Monitoring)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a8235_5_access_restrictions.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.2-3-5.S5`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | File System Permissions |
| 3 | Database Access Controls |
| 4 | Application RBAC |
| 5 | API Access Controls |
| 6 | Cloud IAM Policies |
| 7 | Encryption Status |
| 8 | Network Segmentation |
| 9 | Penetration Test Results |
| 10 | Gap Analysis |
| 11 | Evidence Register |
| 12 | Summary Dashboard |
| 13 | Approval Sign-Off |

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
| 1 | Total Critical/High Gaps: |
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
| 25 | Control Area |
| 26 | Gap Description |
| 27 | Risk Level |
| 28 | Due Date |
| 29 | System |
| 30 | Path / Share |
| 31 | Data Classification |
| 32 | Permission Type |
| 33 | Default Deny |
| 34 | Last Audit Date |
| 35 | Findings |
| 36 | Compliance |
| 37 | Database |
| 38 | Account / Role |
| 39 | Granted Privileges |
| 40 | Least Privilege |
| 41 | Row/Column Security |
| 42 | Audit Date |
| 43 | Application |
| 44 | Role Name |
| 45 | Permissions Granted |
| 46 | Users Assigned |
| 47 | Last Review |
| 48 | API / Service |
| 49 | Auth Method |
| 50 | OAuth Scopes |
| 51 | Rate Limiting |
| 52 | API Key Rotation |
| 53 | Cloud Platform |
| 54 | Identity / Role |
| 55 | Permissions / Scope |
| 56 | Resource Scope |
| 57 | Data Store / System |
| 58 | Encryption at Rest |
| 59 | Algorithm / Standard |
| 60 | Key Management |
| 61 | Segment / VLAN |
| 62 | Systems in Segment |
| 63 | Default Deny Rule |
| 64 | Allowed Traffic |
| 65 | Last Firewall Review |
| 66 | Penetration Tested |
| 67 | Test Date |
| 68 | Test Scope |
| 69 | Severity |
| 70 | Systems Affected |
| 71 | Remediation |
| 72 | Gap ID |
| 73 | System / Area |
| 74 | Impact |
| 75 | Remediation Plan |
| 76 | Target Date |

### Data Validation Values

All dropdown/list values used across sheets:

```
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred, NTFS ACL, Linux ACL
POSIX Permissions, Share Permissions, Both NTFS+Share, Yes, No, Partial
OAuth 2.0, OAuth 2.0 + JWT, API Key, mTLS, Basic Auth (Legacy), None
Microsoft Azure, AWS, Google Cloud Platform, Oracle Cloud, Multi-Cloud
```

**Extracted:** 13 sheets, 76 columns, 27 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"If a machine is expected to be infallible, it cannot also be intelligent."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
