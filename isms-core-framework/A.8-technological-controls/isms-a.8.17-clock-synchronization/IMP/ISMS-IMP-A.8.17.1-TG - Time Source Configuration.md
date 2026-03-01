<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.17.1-TG:framework:TG:a.8.17-s1 -->
**ISMS-IMP-A.8.17.1-TG - Time Source Configuration & Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Time Source Configuration |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.17.1-TG |
| **Related Policy** | ISMS-POL-A.8.17 (Clock Synchronization) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.17 (Clock Synchronization) |
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

- ISMS-POL-A.8.17 (Clock Synchronization)
- ISMS-IMP-A.8.17.2 (Synchronization Verification Process)
- ISMS-IMP-A.8.17.3 (Exception Management)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a817_1_time_sources.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.17.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Time Sources |
| 3 | Internal NTP Servers |
| 4 | Hierarchy |
| 5 | Summary Dashboard |
| 6 | Evidence Register |
| 7 | Approval Sign-Off |

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
| 1 | EVIDENCE REGISTER |
| 2 | TIME SOURCES |
| 3 | INTERNAL NTP SERVERS |
| 4 | TIME SYNCHRONISATION HIERARCHY |
| 5 | TOTAL Non-Active NTP Servers |
| 6 | Evidence ID |
| 7 | Assessment Area |
| 8 | Evidence Type |
| 9 | Description |
| 10 | Location/Path |
| 11 | Date Collected |
| 12 | Collected By |
| 13 | Verification Status |
| 14 | Total Items |
| 15 | Compliant |
| 16 | Partial |
| 17 | Non-Compliant |
| 18 | N/A |
| 19 | Compliance % |
| 20 | KPI |
| 21 | Current Value |
| 22 | Target |
| 23 | Status |
| 24 | Last Updated |
| 25 | Owner |
| 26 | Notes |
| 27 | Server Name |
| 28 | Status / Issue |
| 29 | Monitoring |

### Data Validation Values

All dropdown/list values used across sheets:

```
Configuration File, Screenshot, Report, Log Extract, Policy Document
Audit Record, Test Result, Other, Verified, Pending Review, Insufficient
Not Submitted, Draft, Final, Requires remediation, Re-assessment required
Approved, Approved with Conditions, Rejected, Deferred, GPS, NIST, NTP Pool
Cloudflare, Google, Regional Government, Atomic Clock, Cloud Provider, 0, 1, 2
3
```

**Extracted:** 7 sheets, 29 columns, 32 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Time is what keeps everything from happening at once."*
— Ray Cummings

<!-- QA_VERIFIED: 2026-02-06 -->
