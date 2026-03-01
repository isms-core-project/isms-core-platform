<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.24-28.S2-TG:framework:TG:a.5.24-28 -->
**ISMS-IMP-A.5.24-28.S2-TG - Incident Detection & Classification Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.24: Information Security Incident Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Detection Classification Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S2-TG |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.24 (Information Security Incident Management) |
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

- ISMS-POL-A.5.24-28 (Incident Management Lifecycle)
- ISMS-IMP-A.5.24-28.S1 (Incident Management Framework Assessment)
- ISMS-IMP-A.5.24-28.S3 (Response Capabilities Assessment)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment)
- ISMS-IMP-A.5.24-28.S5 (Learning & Continuous Improvement Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a524_28_s2_detection_classification.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.24-28.S2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Detection Mechanisms |
| 3 | Alert Handling |
| 4 | Classification & Severity |
| 5 | Detection Effectiveness |
| 6 | Gap Analysis |
| 7 | Evidence Register |
| 8 | Summary Dashboard |
| 9 | Approval Sign-Off |

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
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | Detection Mechanisms |
| 2 | Alert Handling |
| 3 | Classification & Severity |
| 4 | Detection Effectiveness |
| 5 | Question ID |
| 6 | Section |
| 7 | Question |
| 8 | Answer |
| 9 | Evidence Reference |
| 10 | Comments |
| 11 | Gap Identified |
| 12 | Gap ID |
| 13 | Gap Description |
| 14 | Risk Level |
| 15 | Current State |
| 16 | Target State |
| 17 | Remediation |
| 18 | Owner |
| 19 | Target Date |
| 20 | Status |
| 21 | Assessment Area |
| 22 | Questions Answered |
| 23 | No Gap |
| 24 | N/A |
| 25 | Target |
| 26 | Compliance % |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Partial, Never, In-Progress, N/A, Informal, Worsening, Improving
Stable, Active, Archived, Superseded, Pending Review, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 26 columns, 22 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"The first principle is that you must not fool yourself — and you are the easiest person to fool."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-06 -->
