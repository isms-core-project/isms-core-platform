<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.6-7-14-S3-TG:framework:TG:a.7.6-7-14-s3 -->
**ISMS-IMP-A.7.6-7-14-S3-TG - Secure Equipment Disposal Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.14: Secure Disposal or Re-Use of Equipment

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Equipment Disposal Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.6-7-14-S3-TG |
| **Related Policy** | ISMS-POL-A.7.6-7-14-S3 (Information Media Handling) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.14 (Secure Disposal or Re-Use of Equipment) |
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

- ISMS-POL-A.7.6-7-14-S3 (Information Media Handling)
- ISMS-IMP-A.7.6-7-14-S1 (Secure Areas Working Assessment)
- ISMS-IMP-A.7.6-7-14-S2 (Clear Desk Screen Compliance)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a76_3_equipment_disposal.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.14.S3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | Disposal Requirements |
| 3 | Disposal Tools |
| 4 | Service Providers |
| 5 | Disposal Log |
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
| 1 | Equipment Type |
| 2 | Storage Type |
| 3 | CONFIDENTIAL Method |
| 4 | INTERNAL Method |
| 5 | PUBLIC Method |
| 6 | Verification Required |
| 7 | Certificate Required |
| 8 | Implementation Status |
| 9 | Notes |
| 10 | Tool/Method Name |
| 11 | Tool Type |
| 12 | Applicable Equipment |
| 13 | Standard/Method |
| 14 | Verification Method |
| 15 | Approved Version |
| 16 | Last Tested |
| 17 | Compliant |
| 18 | Provider Name |
| 19 | Service Type |
| 20 | Contract Status |
| 21 | Contract Expiry |
| 22 | Certificate Provided |
| 23 | On-Site Option |
| 24 | Chain of Custody |
| 25 | Last Audit/Review |
| 26 | Status |
| 27 | Disposal ID |
| 28 | Date |
| 29 | Asset Tag |
| 30 | Make/Model |
| 31 | Serial Number |
| 32 | Data Classification |
| 33 | Disposal Method |
| 34 | Destination |
| 35 | Certificate Obtained |
| 36 | Certificate Ref |
| 37 | Verified By |
| 38 | Asset Updated |
| 39 | Disposal Requirements |
| 40 | Service Providers |
| 41 | Assessment Area |
| 42 | Total Items |
| 43 | Partial |
| 44 | Non-Compliant |
| 45 | N/A |
| 46 | Compliance % |
| 47 | Evidence ID |
| 48 | Evidence Type |
| 49 | Description |
| 50 | Location/Path |
| 51 | Date Collected |
| 52 | Collected By |
| 53 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
HDD, SSD, Flash, Memory, Config, Mixed, Physical Destruction, Crypto Erase
Secure Overwrite, 3-Pass Overwrite, Factory Reset, Format, Config Wipe, N/A
Yes, No, Implemented, Partial, Not Implemented, Software - Overwrite
Software - Crypto Erase, Hardware - Degausser, Hardware - Shredder
Manual Process, On-site Destruction, Off-site Destruction
Recycling with Destruction, Certificate Only, Active, Expired, Under Review
Pending, Yes - Per Item, Yes - Per Batch, Documented, Not Documented, Laptop
Desktop, Server, Mobile, Printer, Network, Storage, USB/Media, Other
CONFIDENTIAL, INTERNAL, PUBLIC, Unknown, Vendor Destruction, Internal Re-Use
Donation, Sale, Recycling, Approved, Approved with Conditions, Rejected
Deferred, Policy document, Procedure document, Screenshot, Photograph
Audit report, Training record, Configuration file, Verified
Pending verification, Not verified, Requires update, Draft, Final
Requires remediation, Re-assessment required
```

**Extracted:** 8 sheets, 53 columns, 73 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"The data you don't properly destroy is the data that will come back to haunt you."*
— Unknown

<!-- QA_VERIFIED: 2026-03-01 -->
