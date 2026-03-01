<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.4.1-TG:framework:TG:a.5.4.1 -->
**ISMS-IMP-A.5.4.1-TG - Management Commitment Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.4: Management Responsibilities

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Management Commitment Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.4.1-TG |
| **Related Policy** | ISMS-POL-A.5.4 (Management Responsibilities) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.4 (Management Responsibilities) |
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

- ISMS-POL-A.5.4 (Management Responsibilities)
- ISMS-IMP-A.5.4.2 (Compliance Oversight Tracker)
- ISMS-IMP-A.5.4.3 (Leadership Dashboard)
- ISMS-IMP-A.5.4.4 (Security Culture Survey)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a54_1_management_commitment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.4.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Manager Inventory |
| 3 | Commitment Assessment |
| 4 | Summary Scores |
| 5 | Approval Sign-Off |
| 6 | Evidence Register |
| 7 | Summary Dashboard |

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
| 1 | Manager ID |
| 2 | Name |
| 3 | Title |
| 4 | Department |
| 5 | Management Level |
| 6 | Direct Reports |
| 7 | Assessment Date |
| 8 | Assessor |
| 9 | Status |
| 10 | Category |
| 11 | Criterion |
| 12 | Weight |
| 13 | Score (0-5) |
| 14 | Weighted Score |
| 15 | Evidence |
| 16 | Notes |
| 17 | Total Weight |
| 18 | Achieved Score |
| 19 | Percentage |
| 20 | Improvement Areas |
| 21 | Evidence ID |
| 22 | Evidence Type |
| 23 | Description |
| 24 | Related Sheet |
| 25 | File Name |
| 26 | File Location |
| 27 | Collection Date |
| 28 | Collected By |

### Data Validation Values

All dropdown/list values used across sheets:

```
Executive, Director, Manager, Team Lead, Supervisor, Pending, In Progress
Complete, Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 7 sheets, 28 columns, 16 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The quality of a leader is reflected in the standards they set for themselves."*
— Ray Kroc

<!-- QA_VERIFIED: 2026-02-06 -->
