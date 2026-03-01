<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.23.3-TG:framework:TG:a.8.23.3 -->
**ISMS-IMP-A.8.23.3-TG - Policy Configuration Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.23: Web Filtering

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Policy Configuration Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.23.3-TG |
| **Related Policy** | ISMS-POL-A.8.23 (Web Filtering) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.23 (Web Filtering) |
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

- ISMS-POL-A.8.23 (Web Filtering)
- ISMS-IMP-A.8.23.1 (Filtering Infrastructure Assessment)
- ISMS-IMP-A.8.23.2 (Network Coverage Assessment)
- ISMS-IMP-A.8.23.4 (Monitoring & Response Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a823_3_policy_configuration.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.23.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Threat Protection |
| 3 | Category Management |
| 4 | Custom Lists |
| 5 | Policy Exceptions |
| 6 | User Group Policies |
| 7 | Acceptable Use Alignment |
| 8 | Policy Review Process |
| 9 | Evidence Register |
| 10 | Gap Analysis |
| 11 | Summary Dashboard |
| 12 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #0000FF | Custom |
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
| 1 | Threat Type |
| 2 | Policy Configured? |
| 3 | Blocking Method |
| 4 | Effectiveness |
| 5 | False Positives |
| 6 | Last Tested |
| 7 | Evidence |
| 8 | Category |
| 9 | Policy Action |
| 10 | Applied To |
| 11 | Business Justification |
| 12 | Exceptions? |
| 13 | Exception Count |
| 14 | Last Reviewed |
| 15 | List ID |
| 16 | List Name |
| 17 | List Type |
| 18 | URL Count |
| 19 | Purpose |
| 20 | Maintained By |
| 21 | Last Updated |
| 22 | Review Frequency |
| 23 | Policy ID |
| 24 | Policy Name |
| 25 | User Count |
| 26 | Policy Type |
| 27 | Filtering Level |
| 28 | Categories Blocked |
| 29 | Time Restrictions |
| 30 | HTTPS Inspection |
| 31 | AUP Requirement |
| 32 | Filtering Enforces This? |
| 33 | How Enforced? |
| 34 | Gaps Identified? |
| 35 | Gap Description |
| 36 | Remediation Plan |
| 37 | Review Date |
| 38 | Review Type |
| 39 | Policies Reviewed |
| 40 | Changes Made |
| 41 | Approved By |
| 42 | Next Review |
| 43 | Exception ID |
| 44 | Exception Type |
| 45 | Requested For |
| 46 | URL/Category |
| 47 | Risk Level |
| 48 | Compensating Controls |
| 49 | Requested By |
| 50 | Approval Date |
| 51 | Expiry Date |
| 52 | Status |
| 53 | Gap ID |
| 54 | Policy Area |
| 55 | Impact |
| 56 | Current State |
| 57 | Target State |
| 58 | Owner |
| 59 | Target Date |
| 60 | Evidence ID |
| 61 | Assessment Area |
| 62 | Evidence Type |
| 63 | Description |
| 64 | Location/Path |
| 65 | Date Collected |
| 66 | Collected By |
| 67 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, N/A, \u2705 Configured, \u26A0\uFE0F Partial, \u274C Not Configured
\u27F3 Planned, High, Medium, Low, Unknown, Rare, Occasional, Frequent
Real-time, Hourly, Daily, Weekly, Monthly, Restrictive (Default Deny)
Trust-Based (Threats Only), Hybrid (Balanced), ⛔ Block, ✅ Allow, ⚠️ Warn
○ Monitor Only, All Users, Specific Group, Specific User, Network Segment
Device Type, Block List, Allow List, Exception List, Quarterly, Annually
As-needed, URL Exception, Category Exception, User Exception, Group Exception
Temporary Exception, Permanent Exception, ✅ Active, ❌ Expired, ⛔ Revoked
⏳ Under Review, Critical, Standard, Restrictive, Relaxed, Executive, Guest
Contractor, High (Strict), Medium (Balanced), Low (Permissive), Selective
\u2705 Yes, \u274C No, Full Review, Partial Review, Ad-hoc, Incident-Driven
Regulatory Change, ○ Open, ⟳ In Progress, ✅ Resolved, ⚠️ Accepted Risk
Threat Protection, Category Filtering, Custom Lists, Exceptions, User Policies
AUP Alignment, Review Process, Policy Config Screenshot, Policy Export
Category List, URL List, Exception Approval, AUP Document, Meeting Minutes
Test Results, User Communication, Change Record, Incident Report, Other
Verified, Pending, Not Verified, Draft, Final, Requires Remediation
Re-assessment Required, Approved, Approved with Conditions, Rejected, Approve
Approve with Conditions, Reject, Require Rework, Configuration file
Screenshot, Network scan, Documentation, '
                 'Vendor spec
Certificate inventory, Audit log, Compliance report, ✅ Verified, ⚠️ Pending
❌ Not Verified, Deferred
```

**Extracted:** 12 sheets, 67 columns, 114 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"I later spent times of the order of five to eight months in hospitals in New Jersey, always on an involuntary basis and always attempting a legal argument for release."*
— John Nash

<!-- QA_VERIFIED: 2026-02-06 -->
