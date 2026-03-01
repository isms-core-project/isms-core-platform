<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.31.1-TG:framework:TG:a.8.31.1 -->
**ISMS-IMP-A.8.31.1-TG - Environment Architecture Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.31: Separation of Development, Test and Production Environments

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Environment Architecture Implementation |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.31.1-TG |
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
- ISMS-IMP-A.8.31.2 (Environment Access Control)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a831_1_environment_architecture.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.31.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Environment Inventory |
| 3 | Network Separation |
| 4 | Infrastructure Separation |
| 5 | Data Separation |
| 6 | Credential Separation |
| 7 | Configuration Consistency |
| 8 | Evidence Register |
| 9 | Gap Analysis |
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
| 1 | Environment Name |
| 2 | Environment Type |
| 3 | Purpose |
| 4 | Infrastructure Type |
| 5 | Primary Users |
| 6 | Data Type Allowed |
| 7 | Availability Target |
| 8 | Change Control Level |
| 9 | Notes |
| 10 | Environment Pair |
| 11 | Network Segment (VLAN/VPC) |
| 12 | Firewall Rules |
| 13 | Cross-Environment Traffic |
| 14 | Separation Status |
| 15 | Test Result |
| 16 | Compliance |
| 17 | Notes/Evidence |
| 18 | Environment |
| 19 | Compute Resources |
| 20 | Database Instances |
| 21 | Storage/Buckets |
| 22 | Cloud Account/Sub |
| 23 | Shared Resources? |
| 24 | Evidence |
| 25 | Data Type Used |
| 26 | Production Data Present? |
| 27 | Anonymization Applied? |
| 28 | Synthetic Data Used? |
| 29 | Data Source |
| 30 | Evidence/Notes |
| 31 | Credential Type |
| 32 | Development |
| 33 | Testing |
| 34 | Production |
| 35 | Shared Credentials? |
| 36 | Prod in PAM Vault? |
| 37 | Configuration Item |
| 38 | Staging Config |
| 39 | Production Config |
| 40 | Match? |
| 41 | Drift % |
| 42 | Gap ID |
| 43 | Area |
| 44 | Gap Description |
| 45 | Risk Severity |
| 46 | Current State |
| 47 | Target State |
| 48 | Remediation Action |
| 49 | Owner |
| 50 | Target Date |
| 51 | ENVIRONMENT INVENTORY |
| 52 | NETWORK SEPARATION ASSESSMENT |
| 53 | INFRASTRUCTURE SEPARATION ASSESSMENT |
| 54 | DATA SEPARATION ASSESSMENT |
| 55 | CREDENTIAL & SECRETS SEPARATION ASSESSMENT |
| 56 | CONFIGURATION CONSISTENCY CHECK |
| 57 | GAP ANALYSIS & REMEDIATION PLAN |
| 58 | Network Separation |
| 59 | Cloud Architect |
| 60 | EVIDENCE REGISTER |
| 61 | ASSESSMENT APPROVAL AND SIGN-OFF |
| 62 | ASSESSMENT SUMMARY |
| 63 | FINAL DECISION: |
| 64 | NEXT REVIEW DETAILS |
| 65 | Assessment Area |
| 66 | Total Items |
| 67 | Compliant |
| 68 | Partial |
| 69 | Non-Compliant |
| 70 | N/A |
| 71 | Compliance % |
| 72 | Severity |
| 73 | Affected Area |
| 74 | Due Date |
| 75 | Evidence ID |
| 76 | Evidence Type |
| 77 | Description |
| 78 | Location / Path |
| 79 | Date Collected |
| 80 | Collected By |
| 81 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, ✅ Yes, ❌ No, ⚠️ Partial, ❓ Unknown, Compliant, Non-Compliant, Partial
Not Assessed, N/A, Development, Testing/QA, Staging, Production, Sandbox
DR/Backup, Training, Other, On-Premises, AWS, Azure, GCP, Hybrid, Multi-Cloud
Kubernetes, Complete, None, Critical, High, Medium, Low, Informational
Configuration file, Screenshot, Log extract, Policy document, Training record
Audit report, Risk assessment, Interview notes, Test results, Verified
Pending Verification, Insufficient, Not Reviewed, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 81 columns, 54 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The security of a cryptographic system lies entirely in the key."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
