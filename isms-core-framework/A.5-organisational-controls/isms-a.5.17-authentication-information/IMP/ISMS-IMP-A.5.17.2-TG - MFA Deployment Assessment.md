<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.17.2-TG:framework:TG:a.5.17.2 -->
**ISMS-IMP-A.5.17.2-TG - MFA Deployment Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.17: Authentication Information

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | MFA Deployment Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.17.2-TG |
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
- ISMS-IMP-A.5.17.3 (Authentication Management Procedures)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a517_2_credential_lifecycle_management.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.17.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Allocation Process |
| 2 | Change Management |
| 3 | Recovery Process |
| 4 | Revocation Process |
| 5 | Audit Log Requirements |
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
| 1 | CREDENTIAL ALLOCATION PROCESS |
| 2 | CREDENTIAL CHANGE MANAGEMENT |
| 3 | CREDENTIAL RECOVERY PROCESSES |
| 4 | CREDENTIAL REVOCATION PROCESS |
| 5 | AUTHENTICATION AUDIT LOG REQUIREMENTS |
| 6 | Process Step |
| 7 | Description |
| 8 | Responsible Role |
| 9 | Verification Required |
| 10 | SLA |
| 11 | System/Tool |
| 12 | Status |
| 13 | Notes |
| 14 | Change Type |
| 15 | Trigger |
| 16 | Process Steps |
| 17 | Verification |
| 18 | Notification |
| 19 | Recovery Method |
| 20 | Use Case |
| 21 | Identity Verification |
| 22 | Security Controls |
| 23 | Revocation Trigger |
| 24 | SLA Requirement |
| 25 | Actions Required |
| 26 | Systems Affected |
| 27 | Responsible |
| 28 | Event Type |
| 29 | Details to Log |
| 30 | Retention Period |
| 31 | Alerting Required |
| 32 | Review Frequency |
| 33 | Evidence ID |
| 34 | Assessment Area |
| 35 | Evidence Type |
| 36 | Location / Path |
| 37 | Date Collected |
| 38 | Collected By |
| 39 | Verification Status |
| 40 | Total Items |
| 41 | Compliant |
| 42 | Partial |
| 43 | Non-Compliant |
| 44 | N/A |
| 45 | Compliance % |
| 46 | Metric |
| 47 | Value |
| 48 | Category |
| 49 | Finding |
| 50 | Count |
| 51 | Severity |
| 52 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
Policy Document, Process Record, System Screenshot, Configuration Export
Audit Log, Training Record, Test Result, Risk Assessment, Meeting Minutes
Other, ✅ Verified, ⚠️ Pending, ❌ Not Verified, N/A, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 52 columns, 18 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"There are only two types of companies: those that have been hacked, and those that will be."*
— Robert Mueller

<!-- QA_VERIFIED: 2026-02-06 -->
