<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.9.3-TG:framework:TG:a.5.9.3 -->
**ISMS-IMP-A.5.9.3-TG - Quality & Compliance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Assessment Specifications |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.9.3-TG |
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
- ISMS-IMP-A.5.9.1 (Asset Identification & Discovery)
- ISMS-IMP-A.5.9.2 (Inventory Structure & Maintenance)
- ISMS-IMP-A.5.9.4 (Owner Accountability Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a59_3_quality_compliance.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.9.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Accuracy Sampling |
| 3 | Completeness Assessment |
| 4 | Currency Assessment |
| 5 | Consistency Checks |
| 6 | Policy Compliance Matrix |
| 7 | Quality Metrics & Scoring |
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
| 1 | Sample ID |
| 2 | Asset Category |
| 3 | Asset ID (Inventory) |
| 4 | Attribute Verified |
| 5 | Inventory Value |
| 6 | Ground Truth Value |
| 7 | Match? |
| 8 | Discrepancy Type |
| 9 | Verification Method |
| 10 | Verified By |
| 11 | Verification Date |
| 12 | Corrected? |
| 13 | Evidence ID |
| 14 | Notes |
| 15 | Mandatory Field |
| 16 | Total Assets |
| 17 | Assets with Field Populated |
| 18 | Completeness % |
| 19 | Target % |
| 20 | Gap |
| 21 | Status |
| 22 | Missing Count |
| 23 | Currency Metric |
| 24 | Assets Meeting Currency Target |
| 25 | Currency % |
| 26 | Stale Assets Count |
| 27 | Consistency Check |
| 28 | System A |
| 29 | System B |
| 30 | Records in A |
| 31 | Records in B |
| 32 | Matches |
| 33 | Consistency % |
| 34 | Policy Requirement |
| 35 | SHALL Requirement |
| 36 | Compliant Assets |
| 37 | Compliance % |
| 38 | Target |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Verified, Not verified, In Review, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 38 columns, 13 validation values, 11 colors

---

**END OF SPECIFICATION**


---

*"When it comes to atoms, language can be used only as in poetry."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
