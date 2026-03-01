<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.9.4-TG:framework:TG:a.5.9.4 -->
**ISMS-IMP-A.5.9.4-TG - Owner Accountability Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Owner Accountability Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.9.4-TG |
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
- ISMS-IMP-A.5.9.3 (Assessment Specifications)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a59_4_owner_accountability.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.9.4`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Ownership Coverage |
| 3 | Owner Acknowledgment |
| 4 | Owner Awareness |
| 5 | Owner Performance |
| 6 | Accountability Metrics |
| 7 | Evidence Register |
| 8 | Summary Dashboard |
| 9 | Approval Sign-Off |

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
| 1 | Asset Category |
| 2 | Total Assets |
| 3 | Assets with Owner |
| 4 | Assets without Owner |
| 5 | Coverage % |
| 6 | Target % |
| 7 | Gap |
| 8 | Status |
| 9 | Unique Owners Count |
| 10 | Avg Assets per Owner |
| 11 | Evidence ID |
| 12 | Notes |
| 13 | Owner Name |
| 14 | Owner Email |
| 15 | Department |
| 16 | Assets Count |
| 17 | Email Sent Date |
| 18 | Reminder 1 (Day 7) |
| 19 | Reminder 2 (Day 14) |
| 20 | Reminder 3 (Day 21) |
| 21 | Escalation (Day 28) |
| 22 | Response Date |
| 23 | Days to Respond |
| 24 | Attestation Status |
| 25 | Next Action |
| 26 | Assets Assigned |
| 27 | Assets Identified by Owner |
| 28 | Awareness % |
| 29 | Verification Method |
| 30 | Verification Date |
| 31 | Reviews Due |
| 32 | Reviews Completed |
| 33 | Review Compliance % |
| 34 | Avg Response Time (Days) |
| 35 | Target Response (Days) |
| 36 | Responsiveness % |
| 37 | Performance Score |
| 38 | Target |

### Data Validation Values

All dropdown/list values used across sheets:

```
Verified, Not verified, In Review, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 38 columns, 11 validation values, 11 colors

---

**END OF SPECIFICATION**


---

*"We are all agreed that your theory is crazy. The question which divides us is whether it is crazy enough."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-02-06 -->
