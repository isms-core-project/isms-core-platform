<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.12-13.S3-TG:framework:TG:a.7.12-13 -->
**ISMS-IMP-A.7.12-13.S3-TG - Maintenance Schedule Tracking**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.13: Equipment Maintenance

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Maintenance Schedule Tracking |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.12-13.S3-TG |
| **Related Policy** | ISMS-POL-A.7.12-13 (Infrastructure Maintenance) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.13 (Equipment Maintenance) |
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

- ISMS-POL-A.7.12-13 (Infrastructure Maintenance)
- ISMS-IMP-A.7.12-13.S1 (Cabling Security Assessment)
- ISMS-IMP-A.7.12-13.S2 (Equipment Maintenance Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a712_3_maintenance_schedule.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.12-13.S3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Equipment Schedule |
| 3 | Overdue Tracking |
| 4 | Upcoming Maintenance |
| 5 | Maintenance Log |
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
| 1 | Equipment Schedule |
| 2 | Assessment Area |
| 3 | Total Items |
| 4 | Compliant |
| 5 | Partial |
| 6 | Non-Compliant |
| 7 | N/A |
| 8 | Compliance % |
| 9 | Evidence ID |
| 10 | Evidence Type |
| 11 | Description |
| 12 | Related Sheet / Item |
| 13 | File Name |
| 14 | File Location |
| 15 | Collection Date |
| 16 | Collected By |

### Data Validation Values

All dropdown/list values used across sheets:

```
Server, Network Device, Storage, UPS, HVAC, Generator, Security System, Other
Tier 1 - Critical, Tier 2 - Standard, Firmware Update, Inspection
Battery Check, Filter Replacement, Calibration, Full Service, Monthly
Quarterly, Semi-annually, Annually, Internal - IT, Internal - Facilities
Vendor, Manufacturer, Parts on Order, Vendor Scheduling, Resource Unavailable
Budget Hold, Yes, No, N/A, Draft, Final, Requires remediation
Re-assessment required
```

**Extracted:** 8 sheets, 16 columns, 35 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"An ounce of prevention is worth a pound of cure."*
— Benjamin Franklin

<!-- QA_VERIFIED: 2026-03-01 -->
