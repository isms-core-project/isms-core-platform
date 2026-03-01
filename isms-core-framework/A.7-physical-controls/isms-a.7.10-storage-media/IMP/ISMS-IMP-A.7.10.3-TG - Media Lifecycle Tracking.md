<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.10.3-TG:framework:TG:a.7.10.3 -->
**ISMS-IMP-A.7.10.3-TG - Media Lifecycle Tracking Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.10: Storage Media

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Media Lifecycle Tracking |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.10.3-TG |
| **Related Policy** | ISMS-POL-A.7.10 (Storage Media) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.10 (Storage Media) |
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

- ISMS-POL-A.7.10 (Storage Media)
- ISMS-IMP-A.7.10.1 (Storage Media Inventory)
- ISMS-IMP-A.7.10.2 (Media Handling Procedures)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a710_3_media_lifecycle.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.10.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 2. Acquisition & Procurement |
| 3 | 3. Internal Re-use |
| 4 | 4. Disposal Methods |
| 5 | 5. Third-Party Disposal |
| 6 | 6. Paper Document Lifecycle |
| 7 | Evidence Register |
| 8 | Summary Dashboard |
| 9 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #0000FF | Custom |
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
| 1 | Process / Category |
| 2 | Classification Level |
| 3 | Process Owner |
| 4 | Procedure Reference |
| 5 | Last Review Date |
| 6 | Status |
| 7 | Implementation Date |
| 8 | Last Audit Date |
| 9 | Next Review Date |
| 10 | Gap Identified |
| 11 | Remediation Plan |
| 12 | Target Completion |
| 13 | Risk Level |
| 14 | Evidence Reference |
| 15 | Notes / Comments |
| 16 | Remediation Owner |
| 17 | Budget Required |
| 18 | Approved Suppliers |
| 19 | Registration Required |
| 20 | Quality Standards |
| 21 | Erasure Method |
| 22 | Verification Required |
| 23 | Documentation |
| 24 | Destruction Method |
| 25 | Witness Required |
| 26 | Certificate Required |
| 27 | Contract Status |
| 28 | Certifications |
| 29 | Certificate SLA |
| 30 | Shredding Standard |
| 31 | Collection Process |
| 32 | Destruction Frequency |
| 33 | Policy Reference: ISMS-POL-A.7.10 - Storage Media |
| 34 | Assessment Area |
| 35 | Total Items |
| 36 | Compliant |
| 37 | Partial |
| 38 | Non-Compliant |
| 39 | N/A |
| 40 | Compliance % |
| 41 | Evidence ID |
| 42 | Evidence Type |
| 43 | Description |
| 44 | Related Sheet/Item |
| 45 | Collection Date |
| 46 | Collected By |
| 47 | Retention Period |
| 48 | Notes |

### Data Validation Values

All dropdown/list values used across sheets:

```
Public, Internal, Confidential, Restricted, All Classifications, Compliant
Partial, Non-Compliant, N/A, Critical, High, Medium, Low, Yes, No, Unknown
Yes - Automatic (PO), Yes - Manual Entry, No - Track Only
NIST 800-88 Rev. 2 Clear, NIST 800-88 Rev. 2 Purge, Cryptographic Erasure
Factory Reset, Full Format, Quick Format, Physical Destruction
Full Verification, Sample Verification (10%), Log Review Only, None
Erasure Certificate, Asset System Log, Manual Log Entry, None Required
Physical Shredding, Degaussing, Degaussing + Shredding, Incineration
Secure Overwriting, Crushing, Disintegration, Yes - Internal Witness
Yes - External Auditor, Yes - Both, For Certain Classifications
Yes - Individual Certificate, Yes - Batch Certificate, No Certificate
Vendor Report Only, Active Contract, Contract Pending Renewal
Contract Expired, No Contract (Spot Purchase), Under Evaluation
DIN 66399 P-4 (Cross-cut), DIN 66399 P-5 (Fine Cross-cut)
DIN 66399 P-6 (High Security), DIN 66399 P-7 (Super High Security)
Strip Shred, Not Specified, Secure Bins (Locked), Secure Bins (Unlocked)
On-Demand Shredding, Contractor Collection, Centralised Collection Point
Daily, Weekly, Bi-weekly, Monthly, Quarterly, On-Demand, Event-Based
Screenshot, Configuration Export, Log Sample, Report, Document, Photo, Other
Draft, Final, Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 48 columns, 87 validation values, 11 colors

---

**END OF SPECIFICATION**


---

*"Information is the oxygen of the modern age."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-03-01 -->
