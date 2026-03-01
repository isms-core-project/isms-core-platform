<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.15-16-18.S2-TG:framework:TG:a.5.15-16-18 -->
**ISMS-IMP-A.5.15-16-18.S2-TG - Access Rights Matrix Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Access Rights Matrix Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.15-16-18.S2-TG |
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
- ISMS-IMP-A.5.15-16-18.S3 (Access Review Results Assessment)
- ISMS-IMP-A.5.15-16-18.S4 (Role Definition & SoD Compliance Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a515-16-18_2_access_rights_matrix.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.15-16-18.S2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Access Matrix |
| 2 | Role Assignments |
| 3 | Group Memberships |
| 4 | Privileged Access |
| 5 | Access Documentation |
| 6 | Coverage Analysis |
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
| 1 | ACCESS RIGHTS MATRIX - USER X SYSTEM MAPPING |
| 2 | ROLE ASSIGNMENTS - RBAC IMPLEMENTATION |
| 3 | GROUP MEMBERSHIP DETAILS |
| 4 | PRIVILEGED ACCESS TRACKING - ADMIN & ELEVATED RIGHTS |
| 5 | ACCESS DOCUMENTATION COMPLETENESS - BUSINESS JUSTIFICATION |
| 6 | COVERAGE ANALYSIS - SYSTEM-LEVEL ACCESS STATISTICS |
| 7 | GAP ANALYSIS - ACCESS RIGHTS NON-COMPLIANCE |
| 8 | User ID |
| 9 | Username |
| 10 | Full Name |
| 11 | Department |
| 12 | System/Application |
| 13 | Access Level |
| 14 | Access Type |
| 15 | Granted Date |
| 16 | Granted By |
| 17 | Last Used |
| 18 | Status |
| 19 | Assigned Role |
| 20 | Assignment Date |
| 21 | Assignment Type |
| 22 | Group Name |
| 23 | Group Type |
| 24 | Purpose |
| 25 | Owner |
| 26 | Member Count |
| 27 | Created Date |
| 28 | Last Modified |
| 29 | Nested Groups |
| 30 | Review Frequency |
| 31 | System |
| 32 | Privilege Level |
| 33 | Business Justification |
| 34 | Approved By |
| 35 | Last Review |
| 36 | Access ID |
| 37 | Approver |
| 38 | Approval Date |
| 39 | Documentation Quality |
| 40 | Criticality |
| 41 | Total Users |
| 42 | Read Access |
| 43 | Write Access |
| 44 | Admin Access |
| 45 | RBAC Adoption |
| 46 | Gap ID |
| 47 | Category |
| 48 | Description |
| 49 | Risk Level |
| 50 | Affected Items |
| 51 | Root Cause |
| 52 | Remediation Plan |
| 53 | Due Date |
| 54 | Assessment Area |
| 55 | Total Items |
| 56 | Compliant |
| 57 | Partial / Warning |
| 58 | Non-Compliant |
| 59 | N/A |
| 60 | Compliance % |

### Data Validation Values

All dropdown/list values used across sheets:

```
Critical, High, Medium, Low, Open, In Progress, Resolved, Accepted, Active
Archived, Superseded, Pending Review, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 60 columns, 20 validation values, 11 colors

---

**END OF SPECIFICATION**


---

*"For a successful technology, reality must take precedence over public relations, for Nature cannot be fooled."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
