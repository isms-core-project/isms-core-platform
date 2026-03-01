<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.17.3-TG:framework:TG:a.5.17.3 -->
**ISMS-IMP-A.5.17.3-TG - Authentication Management Procedures**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.17: Authentication Information

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Authentication Management Procedures |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.17.3-TG |
| **Related Policy** | ISMS-POL-A.5.17 (Authentication Information) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.17 (Authentication Information) |
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

- ISMS-POL-A.5.17 (Authentication Information)
- ISMS-IMP-A.5.17.1 (Password Policy Implementation Guide)
- ISMS-IMP-A.5.17.2 (MFA Deployment Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a517_3_password_system_assessment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.17.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | System Inventory |
| 2 | Security Assessment |
| 3 | Storage Assessment |
| 4 | Integration Assessment |
| 5 | Gap Analysis |
| 6 | Evidence Register |
| 7 | Approval Sign-Off |
| 8 | Summary Dashboard |
| 9 | Instructions & Legend |

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
| 1 | AUTHENTICATION SYSTEM INVENTORY |
| 2 | AUTHENTICATION SYSTEM SECURITY ASSESSMENT |
| 3 | PASSWORD STORAGE SECURITY ASSESSMENT |
| 4 | SSO AND FEDERATION INTEGRATION ASSESSMENT |
| 5 | GAP ANALYSIS AND REMEDIATION TRACKING |
| 6 | System Name |
| 7 | System Type |
| 8 | Vendor |
| 9 | Version |
| 10 | User Count |
| 11 | Auth Method |
| 12 | SSO Integrated |
| 13 | MFA Enabled |
| 14 | Owner |
| 15 | Criticality |
| 16 | Control Area |
| 17 | Requirement |
| 18 | Expected State |
| 19 | Actual State |
| 20 | Status |
| 21 | Gap Description |
| 22 | Priority |
| 23 | Notes |
| 24 | System/Application |
| 25 | Storage Mechanism |
| 26 | Hashing Algorithm |
| 27 | Salting |
| 28 | Key Protection |
| 29 | Encryption at Rest |
| 30 | Application |
| 31 | SSO Protocol |
| 32 | Identity Provider |
| 33 | MFA Pass-through |
| 34 | Session Timeout |
| 35 | Token Encryption |
| 36 | Provisioning |
| 37 | Gap ID |
| 38 | System/Area |
| 39 | Risk Level |
| 40 | Remediation Plan |
| 41 | Target Date |
| 42 | Evidence ID |
| 43 | Assessment Area |
| 44 | Evidence Type |
| 45 | Description |
| 46 | Location / Path |
| 47 | Date Collected |
| 48 | Collected By |
| 49 | Verification Status |
| 50 | Total Items |
| 51 | Compliant |
| 52 | Partial |
| 53 | Non-Compliant |
| 54 | N/A |
| 55 | Compliance % |
| 56 | Metric |
| 57 | Value |
| 58 | Category |
| 59 | Finding |
| 60 | Count |
| 61 | Severity |
| 62 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Policy Document, Process Record, System Screenshot, Configuration Export
Audit Log, Training Record, Test Result, Risk Assessment, Meeting Minutes
Other, ✅ Verified, ⚠️ Pending, ❌ Not Verified, N/A, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 62 columns, 18 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"A chain is only as strong as its weakest link."*
— Thomas Reid

<!-- QA_VERIFIED: 2026-02-06 -->
