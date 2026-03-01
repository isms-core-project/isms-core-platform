<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.30-8.13-14-S1-TG:framework:TG:a.5.30-8.13-14-s1 -->
**ISMS-IMP-A.5.30-8.13-14-S1-TG - BIA and RPO/RTO Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.13: Information Backup

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | BIA and RPO:RTO Process |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.30-8.13-14-S1-TG |
| **Related Policy** | ISMS-POL-A.5.30-8.13-14-S1 (Business Continuity Dr) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.13 (Information Backup) |
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

- ISMS-POL-A.5.30-8.13-14-S1 (Business Continuity Dr)
- ISMS-IMP-A.5.30-8.13-14-S2 (Backup Implementation)
- ISMS-IMP-A.5.30-8.13-14-S3 (Redundancy Implementation)
- ISMS-IMP-A.5.30-8.13-14-S4 (Recovery Testing Process)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a530_1_backup_inventory.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.5.30.S1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Backup Inventory |
| 2 | RPO Compliance |
| 3 | 3-2-1-1-0 Compliance |
| 4 | Summary Dashboard |
| 5 | Evidence Register |
| 6 | Approval Sign-Off |
| 7 | Instructions & Legend |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | System Name |
| 2 | Criticality Tier |
| 3 | Backup Status |
| 4 | Backup Solution |
| 5 | Backup Frequency |
| 6 | Last Backup Date |
| 7 | Offsite Backup |
| 8 | Immutable Backup |
| 9 | Last Test Date |
| 10 | Test Result |
| 11 | Notes |
| 12 | RPO Requirement (hours) |
| 13 | Backup Frequency (hours) |
| 14 | RPO Compliant |
| 15 | Gap (hours) |
| 16 | Criticality |
| 17 | 3 Copies |
| 18 | 2 Media Types |
| 19 | 1 Offsite |
| 20 | 1 Immutable |
| 21 | 0 Errors (Tested) |
| 22 | Total Score (0-5) |
| 23 | Compliance Status |
| 24 | Evidence ID |
| 25 | Assessment Area |
| 26 | Evidence Type |
| 27 | Description |
| 28 | Location / Path |
| 29 | Date Collected |
| 30 | Collected By |
| 31 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Tier 1 - Critical, Tier 2 - Important, Tier 3 - Standard, Tier 4 - Low
Continuous, Every 15 min, Hourly, Every 4 hours, Daily, Weekly, Monthly, Other
Config File, Screenshot, Report, Log File, Test Result, Policy Document
Contract, License, Diagram, Draft, Under Review, Final, Requires Remediation
Approved, Approved with Conditions, Rejected, Requires Rework, Approve
Approve with Conditions, Reject, Require Rework, Re-assessment required
Deferred
```

**Extracted:** 7 sheets, 31 columns, 35 validation values, 8 colors

---

**END OF SPECIFICATION**


---

*"The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
