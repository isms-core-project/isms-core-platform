<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.9.1-TG:framework:TG:a.5.9.1 -->
**ISMS-IMP-A.5.9.1-TG - Asset Identification & Discovery**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Asset Identification & Discovery |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.9.1-TG |
| **Related Policy** | ISMS-POL-A.5.9 (Inventory of Information and Assets) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.9 (Inventory of Information and Other Associated Assets) |
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

- ISMS-POL-A.5.9 (Inventory of Information and Assets)
- ISMS-IMP-A.5.9.2 (Inventory Structure & Maintenance)
- ISMS-IMP-A.5.9.3 (Assessment Specifications)
- ISMS-IMP-A.5.9.4 (Owner Accountability Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a59_1_asset_discovery.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.9.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Information Assets Discovery |
| 3 | IT Infrastructure Discovery |
| 4 | Applications Discovery |
| 5 | Physical Assets Discovery |
| 6 | Personnel Assets Discovery |
| 7 | Discovery Metrics & Summary |
| 8 | Evidence Register |
| 9 | Summary Dashboard |
| 10 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #808080 | Gray (Disabled) |
| #9C0006 | Dark Red (Error) |
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
| 1 | Asset Subcategory |
| 2 | Discovery Method |
| 3 | Expected Count |
| 4 | Discovered Count |
| 5 | Completeness % |
| 6 | Compliance Status |
| 7 | Gaps Identified |
| 8 | Discovery Evidence |
| 9 | Next Discovery Actions |
| 10 | Responsible Party |
| 11 | Target Date |
| 12 | Evidence ID |
| 13 | Notes |
| 14 | Asset Category |
| 15 | Target % |
| 16 | Gap vs. Target |
| 17 | Priority |
| 18 | Key Gaps |
| 19 | Next Actions |

### Data Validation Values

All dropdown/list values used across sheets:

```
Verified, Not verified, In Review, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 19 columns, 11 validation values, 11 colors

---

**END OF SPECIFICATION**


---

*"No, no, you're not thinking; you're just being logical."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
