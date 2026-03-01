<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.15-16-18.S4-TG:framework:TG:a.5.15-16-18 -->
**ISMS-IMP-A.5.15-16-18.S4-TG - Role Definition & SoD Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Role Definition & SoD Compliance Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.15-16-18.S4-TG |
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
- ISMS-IMP-A.5.15-16-18.S3 (Access Review Results Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a515-16-18_4_role_compliance.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.15-16-18.S4`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Role Catalog |
| 2 | Role Assignments |
| 3 | Direct Access Users |
| 4 | SoD Matrix |
| 5 | SoD Violations |
| 6 | RBAC Metrics |
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
| #FF6600 | Custom |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | ROLE CATALOG - RBAC ROLE DEFINITIONS |
| 2 | ROLE ASSIGNMENTS - USER TO ROLE MAPPINGS |
| 3 | DIRECT ACCESS USERS - NON-RBAC ACCESS |
| 4 | SEGREGATION OF DUTIES MATRIX - CONFLICTING ROLE COMBINATIONS |
| 5 | SOD VIOLATIONS - DETECTED CONFLICTING ROLE ASSIGNMENTS |
| 6 | RBAC ADOPTION METRICS & KPIS |
| 7 | Overall RBAC & SoD Compliance Score |
| 8 | GAP ANALYSIS - RBAC & SOD NON-COMPLIANCE |
| 9 | Role ID |
| 10 | Role Name |
| 11 | Department |
| 12 | Description |
| 13 | Systems/Access |
| 14 | User Count |
| 15 | Privileged |
| 16 | Last Review |
| 17 | Owner |
| 18 | Status |
| 19 | User ID |
| 20 | Username |
| 21 | Full Name |
| 22 | Assigned Role |
| 23 | Assignment Date |
| 24 | Assignment Type |
| 25 | Role Appropriate |
| 26 | Verified By |
| 27 | System |
| 28 | Access Level |
| 29 | Granted Date |
| 30 | Justification |
| 31 | Migration Plan |
| 32 | Conflict ID |
| 33 | Role A |
| 34 | Role B |
| 35 | Risk Level |
| 36 | Rationale |
| 37 | Compensating Controls |
| 38 | Violation ID |
| 39 | Detected Date |
| 40 | Remediation Plan |
| 41 | Due Date |
| 42 | Metric |
| 43 | Target |
| 44 | Actual |
| 45 | Gap |
| 46 | Comments |
| 47 | Gap ID |
| 48 | Category |
| 49 | Affected Items |
| 50 | Root Cause |
| 51 | Assessment Area |
| 52 | Total Items |
| 53 | Compliant / Active |
| 54 | Partial / Under Review |
| 55 | Non-Compliant / Inappropriate |
| 56 | N/A |
| 57 | Compliance % |

### Data Validation Values

All dropdown/list values used across sheets:

```
Critical, High, Medium, Low, Open, In Progress, Resolved, Accepted, Active
Archived, Superseded, Pending Review, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 57 columns, 20 validation values, 12 colors

---

**END OF SPECIFICATION**


---

*"It doesn't matter how beautiful your theory is, it doesn't matter how smart you are. If it doesn't agree with experiment, it's wrong."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
