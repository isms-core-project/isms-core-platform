<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.15-16-18.S1-TG:framework:TG:a.5.15-16-18 -->
**ISMS-IMP-A.5.15-16-18.S1-TG - User Inventory & Lifecycle Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | User Inventory & Lifecycle Compliance Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.15-16-18.S1-TG |
| **Related Policy** | ISMS-POL-A.5.15-16-18 (Identity Access Management) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.15 (Access Annex) |
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

- ISMS-POL-A.5.15-16-18 (Identity Access Management)
- ISMS-IMP-A.5.15-16-18.S2 (Access Rights Matrix Assessment)
- ISMS-IMP-A.5.15-16-18.S3 (Access Review Results Assessment)
- ISMS-IMP-A.5.15-16-18.S4 (Role Definition & SoD Compliance Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a515-16-18_1_user_inventory.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.15-16-18.S1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | User Inventory |
| 2 | Employee Lifecycle |
| 3 | Contractor Lifecycle |
| 4 | Service Accounts |
| 5 | Orphaned Accounts |
| 6 | Lifecycle Metrics |
| 7 | Gap Analysis |
| 8 | Summary Dashboard |
| 9 | Evidence Register |
| 10 | Approval Sign-Off |
| 11 | Instructions & Legend |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #808080 | Gray (Disabled) |
| #C00000 | Dark Red (Blocked) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FF0000 | Red (Critical/Alert) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | USER INVENTORY - ALL IDENTITY SYSTEMS |
| 2 | EMPLOYEE LIFECYCLE COMPLIANCE - JOINER & LEAVER EVENTS |
| 3 | JOINER EVENTS - Provisioning Compliance |
| 4 | LEAVER EVENTS - Deprovisioning Compliance |
| 5 | CONTRACTOR LIFECYCLE - TIME-BOUND ACCESS COMPLIANCE |
| 6 | SERVICE ACCOUNT INVENTORY - NON-HUMAN ACCOUNTS |
| 7 | ORPHANED ACCOUNT DETECTION & REMEDIATION |
| 8 | IDENTITY LIFECYCLE COMPLIANCE METRICS - A.5.16 |
| 9 | Overall A.5.16 Compliance Score |
| 10 | GAP ANALYSIS - NON-COMPLIANCE FINDINGS |
| 11 | User ID |
| 12 | Username |
| 13 | Full Name |
| 14 | Email |
| 15 | User Type |
| 16 | Department |
| 17 | Job Title |
| 18 | Manager |
| 19 | Hire Date |
| 20 | Termination Date |
| 21 | Status |
| 22 | Last Login |
| 23 | Account Created |
| 24 | Comments |
| 25 | Provision Date |
| 26 | Days to Provision |
| 27 | SLA (Days) |
| 28 | Compliance Status |
| 29 | Notes |
| 30 | Disable Date |
| 31 | Hours to Disable |
| 32 | SLA (Hours) |
| 33 | Sponsor |
| 34 | Contract Start |
| 35 | Contract End |
| 36 | Access Expiry |
| 37 | Days Remaining |
| 38 | Compliance |
| 39 | Account ID |
| 40 | Account Name |
| 41 | Purpose |
| 42 | Owner |
| 43 | Created Date |
| 44 | Last Used |
| 45 | Privileged |
| 46 | Password Rotation |
| 47 | Orphan Reason |
| 48 | Detected Date |
| 49 | Remediation Status |
| 50 | Metric |
| 51 | Target |
| 52 | Actual |
| 53 | Gap |
| 54 | Gap ID |
| 55 | Category |
| 56 | Description |
| 57 | Risk Level |
| 58 | Affected Users |
| 59 | Root Cause |
| 60 | Remediation Plan |
| 61 | Due Date |
| 62 | Assessment Area |
| 63 | Total Items |
| 64 | Compliant |
| 65 | Partial / Warning |
| 66 | Non-Compliant |
| 67 | N/A |
| 68 | Compliance % |

### Data Validation Values

All dropdown/list values used across sheets:

```
Critical, High, Medium, Low, Open, In Progress, Resolved, Accepted, Active
Archived, Superseded, Pending Review, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 68 columns, 20 validation values, 11 colors

---

**END OF SPECIFICATION**


---

*"I learned very early the difference between knowing the name of something and knowing something."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
