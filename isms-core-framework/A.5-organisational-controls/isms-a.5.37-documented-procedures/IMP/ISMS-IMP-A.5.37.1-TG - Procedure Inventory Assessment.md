<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.37.1-TG:framework:TG:a.5.37.1 -->
**ISMS-IMP-A.5.37.1-TG - Procedure Inventory Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.37

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Procedure Inventory Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.37.1-TG |
| **Related Policy** | ISMS-POL-A.5.37 (Documented Procedures) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.37) |
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

- ISMS-POL-A.5.37 (Documented Procedures)
- ISMS-IMP-A.5.37.2 (Procedure Quality Assessment)
- ISMS-IMP-A.5.37.3 (Procedure Review and Update Tracking)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a537_1_procedure_inventory.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.37.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Procedure Inventory |
| 3 | Required Procedures |
| 4 | Accessibility Matrix |
| 5 | Gap Analysis |
| 6 | Evidence Register |
| 7 | Summary Dashboard |
| 8 | Approval Sign-Off |

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
| 1 | Evidence ID |
| 2 | Assessment Area |
| 3 | Evidence Type |
| 4 | Description |
| 5 | Location / Path |
| 6 | Date Collected |
| 7 | Collected By |
| 8 | Verification Status |
| 9 | Total Items |
| 10 | Compliant |
| 11 | Partial |
| 12 | Non-Compliant |
| 13 | N/A |
| 14 | Compliance % |
| 15 | Category |
| 16 | Finding |
| 17 | Count |
| 18 | Severity |
| 19 | Action Required |

### Data Validation Values

All dropdown/list values used across sheets:

```
System Operations, Security Operations, Facility Operations, Change Management
Recovery Operations, User Management, Other, Draft, Pending Approval, Approved
Expired, Under Review, Critical, High, Medium, Low, Exists, Partial, Missing
Yes, No, Incomplete, Outdated, Unapproved, Open, In Progress, Closed
Policy Document, Process Record, System Screenshot, Configuration Export
Audit Log, Training Record, Test Result, Risk Assessment, Meeting Minutes
Verified, Pending verification, Not verified, N/A, Approved with Conditions
Rejected, Deferred
```

**Extracted:** 8 sheets, 19 columns, 43 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The beginning of wisdom is the definition of terms."*
— Socrates

<!-- QA_VERIFIED: 2026-02-06 -->
