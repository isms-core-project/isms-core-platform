<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.19-23.S1-TG:framework:TG:a.5.19-23 -->
**ISMS-IMP-A.5.19-23.S1-TG - Cloud Service Inventory & Classification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Cloud Service Inventory & Classification |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.19-23.S1-TG |
| **Related Policy** | ISMS-POL-A.5.19-23 (Cloud Services) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.23 (Information Security for Use of Cloud Services) |
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

- ISMS-POL-A.5.19-23 (Cloud Services)
- ISMS-IMP-A.5.19-23.S2 (Vendor Due Diligence & Contracts)
- ISMS-IMP-A.5.19-23.S3 (Secure Configuration & Deployment)
- ISMS-IMP-A.5.19-23.S4 (Ongoing Governance & Risk Management)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a523_1_inventory.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.19-23.S1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 2. SaaS Services |
| 3 | 3. IaaS PaaS Services |
| 4 | 4. Cloud Security Services |
| 5 | 5. Cloud Storage Services |
| 6 | 6. Data Classification |
| 7 | 7. Service Criticality |
| 8 | Evidence Register |
| 9 | Summary Dashboard |
| 10 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #666666 | Dark Gray (Secondary Text) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FF0000 | Red (Critical/Alert) |
| #FFC000 | Custom |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFF00 | Yellow (Warning) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | Service Name |
| 2 | Provider |
| 3 | Service Type |
| 4 | Environment |
| 5 | Business Owner |
| 6 | Technical Owner |
| 7 | Data Classification |
| 8 | Criticality |
| 9 | Users |
| 10 | Cost (Annual CHF) |
| 11 | Contract End Date |
| 12 | Primary Region |
| 13 | Backup Region |
| 14 | Integration Count |
| 15 | API Dependency |
| 16 | Compliance Certs |
| 17 | Current Status |
| 18 | Exit Strategy Type |
| 19 | Alternative Identified |
| 20 | Export Format Available |
| 21 | Export Tested |
| 22 | Data Volume (GB) |
| 23 | Migration Complexity |
| 24 | Lock-In Risk |
| 25 | Hybrid: Workload Segmentation |
| 26 | Hybrid: Data Sync Latency |
| 27 | OnPrem: TCO Analysis Complete |
| 28 | OnPrem: Infrastructure Available |
| 29 | OnPrem: Staffing Plan Documented |
| 30 | Data ID |
| 31 | Data Category |
| 32 | Description |
| 33 | Classification Level |
| 34 | Primary Cloud Service |
| 35 | Storage Location |
| 36 | Data Owner |
| 37 | Retention Period |
| 38 | Personal Data (GDPR) |
| 39 | Cross-Border Transfer |
| 40 | Service ID |
| 41 | Cloud Service Name |
| 42 | Service Category |
| 43 | Business Process Supported |
| 44 | Criticality Level |
| 45 | RTO (Hours) |
| 46 | RPO (Hours) |
| 47 | MTPD (Hours) |
| 48 | Single Point of Failure |
| 49 | Workaround Available |
| 50 | DORA Scope |
| 51 | Exit Priority |
| 52 | Item |
| 53 | Requirement |
| 54 | Status |
| 55 | Evidence |
| 56 | Category |
| 57 | Total |
| 58 | {CHECK} Compliant |
| 59 | {WARNING} Partial |
| 60 | {XMARK} Non-Compliant |
| 61 | N/A |
| 62 | Compliance % |
| 63 | Evidence ID |
| 64 | Assessment Area |
| 65 | Evidence Type |
| 66 | Location/Path |
| 67 | Date Collected |
| 68 | Collected By |
| 69 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
SaaS, IaaS, PaaS, Security, Storage, Collaboration, Other, Critical, High
Medium, Low, Restricted, Confidential, Internal, Public, Mixed, N/A
Switzerland, EU, USA, Global, Unknown, Active, Renewal Due, Expired
Under Negotiation, Trial, Yes, No, High (>$50K), Medium ($10K-$50K)
Low (<$10K), None, Planned, Easy (≤30 days), Medium (31-90 days)
Hard (>90 days), ' + ', '.join(PROVIDER_HQ_JURISDICTION) + '
'.join(CLOUD_ACT_EXPOSURE) + ', '.join(EU_DATA_BOUNDARY_OPTIONS) + '
'.join(YES_NO_NOT_DETERMINED) + ', '.join(AI_RISK_CLASSIFICATION) + '
'.join(CONCENTRATION_RISK_LEVEL) + ', '.join(YES_NO_PARTIAL) + ', Partial
Under Review, Production, Development, Test, Staging, All
'.join(EXIT_STRATEGY_TYPE) + ', '.join(ALTERNATIVE_IDENTIFIED) + '
'.join(EXPORT_FORMAT) + ', '.join(EXPORT_TESTED) + '
'.join(MIGRATION_COMPLEXITY) + ', '.join(LOCK_IN_RISK) + '
'.join(HYBRID_WORKLOAD_SEGMENTATION) + ', '.join(HYBRID_DATA_SYNC_LATENCY) + '
'.join(ONPREM_TCO_ANALYSIS) + ', '.join(ONPREM_INFRASTRUCTURE) + '
'.join(ONPREM_STAFFING_PLAN) + ', Yes - Special Category, Yes - Personal
EEA Only, Adequacy Decision, SCCs, Not Assessed, In-Scope, Out-of-Scope, TBD
P1 - Critical, P2 - High, P3 - Medium, P4 - Low, Contract, Invoice
CMDB Export, Screenshot, Config File, Risk Assessment, Audit Report, Verified
Pending verification, Not verified, Requires update, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 69 columns, 95 validation values, 12 colors

---

**END OF SPECIFICATION**


---

*"What I cannot create, I do not understand."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
