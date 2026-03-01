<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.8.3-TG:framework:TG:a.5.8.3 -->
**ISMS-IMP-A.5.8.3-TG - Project Portfolio Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.8: Information Security in Project Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Project Portfolio Dashboard |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.8.3-TG |
| **Related Policy** | ISMS-POL-A.5.8 (Information Security in Project Management) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.8 (Information Security in Project Management) |
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

- ISMS-POL-A.5.8 (Information Security in Project Management)
- ISMS-IMP-A.5.8.1 (Project Lifecycle Security Assessment)
- ISMS-IMP-A.5.8.2 (Security Requirements Register)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a58_3_project_portfolio.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.8.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |

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
| 1 | Portfolio Compliance |
| 2 | Regulatory Compliance |
| 3 | Project Name |
| 4 | Classification |
| 5 | Business Owner |
| 6 | Phase |
| 7 | Compliance % |
| 8 | Initiation % |
| 9 | Planning % |
| 10 | Execution % |
| 11 | Monitoring % |
| 12 | Closure % |
| 13 | Critical Gaps |
| 14 | High Findings |
| 15 | Deploy Date |
| 16 | Last Assessment |
| 17 | Notes |
| 18 | Assessment Area |
| 19 | Questions Answered |
| 20 | No Gap |
| 21 | Gap Identified |
| 22 | N/A |
| 23 | Target |
| 24 | Project |
| 25 | Status |
| 26 | Owner |
| 27 | Gap Category |
| 28 | Description |
| 29 | Frequency |
| 30 | Impact |
| 31 | Recommended Action |
| 32 | Quarter |
| 33 | Total Projects |
| 34 | Avg Compliance % |
| 35 | High Risk Avg |
| 36 | Medium Risk Avg |
| 37 | Low Risk Avg |
| 38 | Priority |
| 39 | Action Required |
| 40 | Lesson Learned |
| 41 | Category |
| 42 | Recommendation |
| 43 | Regulation |
| 44 | Applicable Projects |
| 45 | Compliance Rate |
| 46 | Gaps |
| 47 | Security Budget (CHF) |
| 48 | Actual Spend (CHF) |
| 49 | % of Total Budget |
| 50 | Resource FTE |
| 51 | Role / Function |
| 52 | Name |
| 53 | Signature / Initials |
| 54 | Date (DD.MM.YYYY) |
| 55 | Comments |

### Data Validation Values

All dropdown/list values used across sheets:

```
High, Medium, Low, Classification, Initiation, Planning, Execution, Monitoring
Closure, Closed, Critical, P1, P2, P3, P4, Security Testing, Vendor Management
Requirements Definition, Implementation, Training, Process, Compliant, Partial
Non-Compliant, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 1 sheets, 55 columns, 28 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"A physicist is just an atom's way of looking at itself."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
