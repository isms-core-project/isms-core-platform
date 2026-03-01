<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.11.3-TG:framework:TG:a.8.11.3 -->
**ISMS-IMP-A.8.11.3-TG - Environment Coverage Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Environment Coverage Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.11.3-TG |
| **Related Policy** | ISMS-POL-A.8.11 (Data Masking) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.11 (Data Masking) |
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

- ISMS-POL-A.8.11 (Data Masking)
- ISMS-IMP-A.8.11.1 (Data Inventory & Classification Assessment)
- ISMS-IMP-A.8.11.2 (Masking Technique Selection & Requirements)
- ISMS-IMP-A.8.11.4 (Testing & Validation Framework)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a811_3_environment_coverage.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.11.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Environment Inventory |
| 3 | Production Environment |
| 4 | NonProduction Environments |
| 5 | Analytics & Reporting |
| 6 | Backup & Archive |
| 7 | External Sharing |
| 8 | Cloud Environments |
| 9 | Data Flow Mapping |
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
| 1 | User Role/Group |
| 2 | Masked Fields |
| 3 | Unmasked Access Logged? |
| 4 | Access Control Method |
| 5 | Exception Justification |
| 6 | Risk Level |
| 7 | Remediation Target Date |
| 8 | Data Refresh Frequency |
| 9 | Masking Applied During Refresh? |
| 10 | Direct Prod Clone Prevented? |
| 11 | Masking Validation Method |
| 12 | Last Data Refresh Date |
| 13 | Next Planned Refresh |
| 14 | Refresh Process Owner |
| 15 | Analytics Platform Type |
| 16 | Aggregation Level |
| 17 | Re-ID Risk Assessed? |
| 18 | Re-ID Risk Level |
| 19 | Synthetic Data Used? |
| 20 | Data Export Controls |
| 21 | Self-Service BI Masking |
| 22 | Backup Type |
| 23 | Encryption Enabled? |
| 24 | Encryption Method |
| 25 | Access Control |
| 26 | Restoration Process |
| 27 | Masking on Restore? |
| 28 | Backup Retention Period |
| 29 | Recipient Type |
| 30 | Data Sharing Purpose |
| 31 | DPA in Place? |
| 32 | DPA Specifies Masking? |
| 33 | Contractual Exception? |
| 34 | Recipient Security Audit Date |
| 35 | Data Minimization Applied? |
| 36 | Cloud Provider |
| 37 | Cloud Service Type |
| 38 | Region/Geography |
| 39 | Client-Side Masking? |
| 40 | Cloud-Native Masking Tool |
| 41 | Multi-Tenancy Concerns? |
| 42 | Data Residency Compliance |
| 43 | Source Environment |
| 44 | Destination Environment |
| 45 | Data Type |
| 46 | Masking Checkpoint? |
| 47 | Masking Technique |
| 48 | Flow Frequency |
| 49 | Automated Masking? |
| 50 | Masking Tool/Script |
| 51 | Masking Validation |
| 52 | Last Flow Date |
| 53 | Flow Owner |
| 54 | Approval Required? |
| 55 | Approval Status |
| 56 | Compliance Status |
| 57 | Notes/Comments |
| 58 | Evidence ID |
| 59 | Gap ID |
| 60 | Environment/System |
| 61 | Gap Description |
| 62 | Current State |
| 63 | Target State |
| 64 | Impact |
| 65 | Remediation Action |
| 66 | Owner |
| 67 | Target Date |
| 68 | Status |
| 69 | =SUM(B6:B13) |
| 70 | =SUM(C6:C13) |
| 71 | =SUM(D6:D13) |
| 72 | =SUM(E6:E13) |
| 73 | =SUM(F6:F13) |
| 74 | Category |
| 75 | Description |
| 76 | Source/Location |
| 77 | Date Collected |
| 78 | Collected By |
| 79 | Notes |
| 80 | Assessment Area |
| 81 | Total Items |
| 82 | Compliant |
| 83 | Partial |
| 84 | Non-Compliant |
| 85 | N/A |
| 86 | Compliance % |
| 87 | Finding |
| 88 | Recommendation |
| 89 | Priority |

### Data Validation Values

All dropdown/list values used across sheets:

```
Production, Development, Testing, UAT, Staging, Training, Sandbox, Analytics
Cloud, Backup, Archive, External, Sensitive, Confidential, Internal, Public
On-Premises, AWS, Azure, GCP, Hybrid, Other Cloud, PII, Financial, Health
Credentials, Proprietary, Mixed, None, \u2705 Mandatory
\u26A0\uFE0F Conditional, \u274C Not Required, N/A, Yes, No, Partial, Planned
SDM, DDM, Tokenization, Encryption, Redaction, Substitution, Anonymization
\u2705 Compliant, \u26A0\uFE0F Partial, \u274C Non-Compliant, \u2705 Complete
\u274C Missing, High, Medium, Low, Not Started, In Progress, Completed
Blocked, Configuration file, Screenshot, Architecture diagram, Documentation
Audit log, Compliance report, Data flow map, Masking evidence, Other, Verified
Pending verification, Not verified, Requires update, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 13 sheets, 89 columns, 77 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"In the middle of difficulty lies opportunity."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
