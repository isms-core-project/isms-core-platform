<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.12-13.S2-TG:framework:TG:a.7.12-13 -->
**ISMS-IMP-A.7.12-13.S2-TG - Equipment Maintenance Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.13: Equipment Maintenance

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Equipment Maintenance Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.12-13.S2-TG |
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
- ISMS-IMP-A.7.12-13.S3 (Maintenance Schedule Tracking)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a712_2_equipment_maintenance.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.12-13.S2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Equipment Inventory |
| 3 | Maintenance Programme |
| 4 | Personnel & Vendors |
| 5 | Security During Maintenance |
| 6 | Remote Maintenance |
| 7 | Evidence Register |
| 8 | Summary Dashboard |
| 9 | Approval Sign-Off |

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
| 1 | Assessment Question |
| 2 | Status |
| 3 | Evidence Reference |
| 4 | Notes |
| 5 | Assessment Area |
| 6 | Total Items |
| 7 | Compliant |
| 8 | Partial |
| 9 | Non-Compliant |
| 10 | N/A |
| 11 | Compliance % |
| 12 | Evidence ID |
| 13 | Evidence Type |
| 14 | Description |
| 15 | Related Sheet / Item |
| 16 | File Name |
| 17 | File Location |
| 18 | Collection Date |
| 19 | Collected By |

### Data Validation Values

All dropdown/list values used across sheets:

```
Server, Network Device, Storage, UPS, HVAC, Generator, Security System, Other
Tier 1 - Critical, Tier 2 - Standard, Monthly, Quarterly, Semi-annually
Annually, Yes, No, Partial, Internal Staff, Third-Party Vendor, Contractor
Yes - Badge/ID, Yes - Escort, Yes - Always, Yes - Sensitive Equipment, N/A
Vendor Remote Support, Internal Remote Management, Cloud Management Portal
Yes - Pre-approved, Yes - On-demand, Yes - VPN, Yes - Encrypted
Yes - Automated, Yes - Manual, Yes - Real-time, Yes - Recorded, Yes - Usually
Draft, Final, Requires remediation, Re-assessment required
```

**Extracted:** 9 sheets, 19 columns, 41 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Take care of your equipment and your equipment will take care of you."*
— Unknown

<!-- QA_VERIFIED: 2026-03-01 -->
