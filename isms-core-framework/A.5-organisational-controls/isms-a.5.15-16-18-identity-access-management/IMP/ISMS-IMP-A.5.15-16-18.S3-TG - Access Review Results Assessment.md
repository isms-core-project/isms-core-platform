<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.15-16-18.S3-TG:framework:TG:a.5.15-16-18 -->
**ISMS-IMP-A.5.15-16-18.S3-TG - Access Review Results Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Access Review Results Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.15-16-18.S3-TG |
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
- ISMS-IMP-A.5.15-16-18.S1 (User Inventory & Lifecycle Compliance Assessment)
- ISMS-IMP-A.5.15-16-18.S2 (Access Rights Matrix Assessment)
- ISMS-IMP-A.5.15-16-18.S4 (Role Definition & SoD Compliance Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a515-16-18_3_access_review_results.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.15-16-18.S3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Review Schedule |
| 2 | Review Completion |
| 3 | Review Findings |
| 4 | Overdue Reviews |
| 5 | Reviewer Performance |
| 6 | Review Metrics |
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
| 1 | REVIEW COMPLETION TRACKING - EXECUTION STATUS |
| 2 | REVIEW FINDINGS - DETAILED ACTIONS |
| 3 | OVERDUE REVIEWS - ESCALATION REQUIRED |
| 4 | REVIEWER PERFORMANCE METRICS - RESPONSIVENESS |
| 5 | ACCESS REVIEW COMPLIANCE METRICS - KPIS |
| 6 | Overall Access Review Compliance Score |
| 7 | GAP ANALYSIS - REVIEW PROCESS NON-COMPLIANCE |
| 8 | Review ID |
| 9 | System/Application |
| 10 | Criticality |
| 11 | Review Period |
| 12 | Frequency |
| 13 | Reviewer |
| 14 | Reviewer Role |
| 15 | Due Date |
| 16 | Est. Users |
| 17 | Status |
| 18 | System |
| 19 | Start Date |
| 20 | Completion Date |
| 21 | Days to Complete |
| 22 | Users Reviewed |
| 23 | Access Confirmed |
| 24 | Access Removed |
| 25 | Finding ID |
| 26 | Username |
| 27 | Access Level |
| 28 | Action |
| 29 | Reason |
| 30 | Priority |
| 31 | Days to Remediate |
| 32 | Days Overdue |
| 33 | Escalation Level |
| 34 | Escalation Date |
| 35 | Escalated To |
| 36 | Reviewer Name |
| 37 | Role |
| 38 | Department |
| 39 | Total Reviews |
| 40 | Completed |
| 41 | Overdue |
| 42 | Completion Rate |
| 43 | Avg Days to Complete |
| 44 | Performance |
| 45 | Metric |
| 46 | Target |
| 47 | Actual |
| 48 | Gap |
| 49 | Comments |
| 50 | Gap ID |
| 51 | Category |
| 52 | Description |
| 53 | Risk Level |
| 54 | Affected Items |
| 55 | Root Cause |
| 56 | Remediation Plan |
| 57 | Owner |
| 58 | Assessment Area |
| 59 | Total Items |
| 60 | Compliant / Completed |
| 61 | Partial / Scheduled |
| 62 | Non-Compliant / Overdue |
| 63 | N/A |
| 64 | Compliance % |

### Data Validation Values

All dropdown/list values used across sheets:

```
Critical, High, Medium, Low, Open, In Progress, Resolved, Accepted, Active
Archived, Superseded, Pending Review, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 64 columns, 20 validation values, 11 colors

---

**END OF SPECIFICATION**


---

*"Study hard what interests you the most in the most undisciplined, irreverent and original manner possible."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
