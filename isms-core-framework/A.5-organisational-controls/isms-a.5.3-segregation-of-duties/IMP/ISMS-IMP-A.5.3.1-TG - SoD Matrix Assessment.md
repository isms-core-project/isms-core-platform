<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.3.1-TG:framework:TG:a.5.3.1 -->
**ISMS-IMP-A.5.3.1-TG - SoD Matrix Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.3: Policies for Segregation of Duties

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | SoD Matrix Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.3.1-TG |
| **Related Policy** | ISMS-POL-A.5.3 (Segregation of Duties) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.3 (Policies for Segregation of Duties) |
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

- ISMS-POL-A.5.3 (Segregation of Duties)
- ISMS-IMP-A.5.3.2 (Conflict Analysis)
- ISMS-IMP-A.5.3.3 (Role-Function Mapping)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a53_1_sod_matrix.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.3.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Role Inventory |
| 3 | Conflict Matrix |
| 4 | Current Assignments |
| 5 | Gap Analysis |
| 6 | Remediation Tracker |
| 7 | Exception Register |
| 8 | Approval Sign-Off |
| 9 | Summary Dashboard |

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
| 1 | Jane Smith |
| 2 | AP Clerk |
| 3 | J. Manager |
| 4 | ROLE-FIN-001, ROLE-FIN-003 |
| 5 | Role Removal |
| 6 | IT Manager |
| 7 | In Progress |
| 8 | FINAL DECISION: |
| 9 | Role ID |
| 10 | Role Name |
| 11 | Department |
| 12 | Process Domain |
| 13 | Risk Level |
| 14 | Description |
| 15 | Key Duties |
| 16 | System Access |
| 17 | Active |
| 18 | Person ID |
| 19 | Name |
| 20 | Primary Role |
| 21 | Additional Roles |
| 22 | Assignment Date |
| 23 | Last Review |
| 24 | Manager |
| 25 | Notes |
| 26 | Gap ID |
| 27 | Conflicting Roles |
| 28 | Conflict Type |
| 29 | Identified Date |
| 30 | Status |
| 31 | Remediation ID |
| 32 | Action Type |
| 33 | Owner |
| 34 | Target Date |
| 35 | Completion Date |
| 36 | Evidence Ref |
| 37 | Exception ID |
| 38 | Justification |
| 39 | Compensating Controls |
| 40 | Risk Acceptance |
| 41 | Approval Date |
| 42 | Expiry Date |
| 43 | Review Frequency |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, X, C, M, Draft, Final, Requires remediation, Re-assessment required
Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 43 columns, 13 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-06 -->
