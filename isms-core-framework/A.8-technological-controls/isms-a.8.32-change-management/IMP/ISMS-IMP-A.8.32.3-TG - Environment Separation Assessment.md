<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.32.3-TG:framework:TG:a.8.32.3 -->
**ISMS-IMP-A.8.32.3-TG - Environment Separation Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Environment Separation Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.32.3-TG |
| **Related Policy** | ISMS-POL-A.8.32 (Change Management) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.32 (Change Management) |
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

- ISMS-POL-A.8.32 (Change Management)
- ISMS-IMP-A.8.32.1 (Change Process Assessment)
- ISMS-IMP-A.8.32.2 (Change Types & Categories Assessment)
- ISMS-IMP-A.8.32.4 (Testing & Validation Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a832_3_environment_separation.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.32.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Environment Inventory |
| 3 | Access Controls |
| 4 | Promotion Workflows |
| 5 | Data Protection |
| 6 | Environment Config |
| 7 | Separation Controls |
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
| 1 | Attribute |
| 2 | Value |
| 3 | Compliance |
| 4 | Evidence |
| 5 | Notes |
| 6 | From Environment |
| 7 | To Environment |
| 8 | Method |
| 9 | Approval Required? |
| 10 | Frequency |
| 11 | Control |
| 12 | Dev→Test |
| 13 | Test→QA |
| 14 | QA→Prod |
| 15 | Pipeline Stage |
| 16 | Implemented? |
| 17 | Tool/Method |
| 18 | Automated? |
| 19 | Requirement |
| 20 | Details |
| 21 | System/Application |
| 22 | Contains Prod Data? |
| 23 | Data Type |
| 24 | Anonymized? |
| 25 | Approval Date |
| 26 | Approved By |
| 27 | Review Date |
| 28 | Compliant? |
| 29 | Capability |
| 30 | Available? |
| 31 | Data Types Supported |
| 32 | Usage |
| 33 | Control Type |
| 34 | Description |
| 35 | Environments Covered |
| 36 | Implementation Status |
| 37 | Effectiveness |
| 38 | Last Tested |
| 39 | Owner |
| 40 | Assessment Area |
| 41 | Target |
| 42 | Current Score |
| 43 | Gap |
| 44 | Remediation Required |
| 45 | Target Date |
| 46 | Total Items |
| 47 | Compliant |
| 48 | Partial |
| 49 | Non-Compliant |
| 50 | N/A |
| 51 | Compliance % |
| 52 | Metric |
| 53 | Category |
| 54 | Finding |
| 55 | Count |
| 56 | Severity |
| 57 | Action Required |
| 58 | Evidence ID |
| 59 | Evidence Type |
| 60 | Location / Path |
| 61 | Date Collected |
| 62 | Collected By |
| 63 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Development, Test, QA, UAT, Staging, Pre-Production, Production, DR/Backup
On-Premises, Cloud IaaS, Cloud PaaS, Cloud SaaS, Hybrid, Managed Service
Physical, Network (VLAN), Logical (Namespace/VM), None, VPN, Bastion Host
Direct, Jump Server, API, Web Portal, SSH Key, Other, Monthly, Quarterly
Bi-Annually, Annually, Ad-hoc, Public, Internal, Confidential
Highly Confidential, Personal Data, Masking, Tokenization, Synthetic Data
Subset Only, Encryption, Not Anonymized, Manual Deploy, CI/CD Pipeline
Automated, Release Management Tool, On-Demand, Daily, Weekly, Bi-Weekly
Per Release, Change Request, Policy Document, Process Record
System Screenshot, Configuration Export, Audit Log, Training Record
Test Result, Risk Assessment, Meeting Minutes, N/A, Real-time, Hourly, Draft
Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 63 columns, 72 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"When you have a clever cryptographic scheme, the job is half done. Making it work in practice is the other ninety percent."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
