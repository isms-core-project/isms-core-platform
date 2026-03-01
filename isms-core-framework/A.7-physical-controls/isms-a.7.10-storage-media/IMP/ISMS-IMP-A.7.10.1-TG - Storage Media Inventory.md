<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.10.1-TG:framework:TG:a.7.10.1 -->
**ISMS-IMP-A.7.10.1-TG - Storage Media Inventory Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.10: Storage Media

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Storage Media Inventory |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.10.1-TG |
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
- ISMS-IMP-A.7.10.2 (Media Handling Procedures)
- ISMS-IMP-A.7.10.3 (Media Lifecycle Tracking)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a710_1_storage_media_inventory.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.7.10.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 2. Digital Storage Media |
| 3 | 3. Removable Media Registry |
| 4 | 4. Fixed Storage Assets |
| 5 | 5. Cloud Storage Mapping |
| 6 | 6. Physical Documents |
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
| 1 | Media ID / Asset Tag |
| 2 | Media Type |
| 3 | Data Classification |
| 4 | Serial Number |
| 5 | Assigned Custodian |
| 6 | Status |
| 7 | Acquisition Date |
| 8 | Last Audit Date |
| 9 | Next Audit Date |
| 10 | Gap Identified |
| 11 | Remediation Plan |
| 12 | Target Completion |
| 13 | Risk Level |
| 14 | Evidence Reference |
| 15 | Notes / Comments |
| 16 | Remediation Owner |
| 17 | Budget Required |
| 18 | Physical Location |
| 19 | Encryption Status |
| 20 | Capacity (GB) |
| 21 | Authorisation Reference |
| 22 | Authorised User(s) |
| 23 | Permitted Use Cases |
| 24 | System Type |
| 25 | Total Capacity (TB) |
| 26 | Utilisation (%) |
| 27 | Cloud Type |
| 28 | Provider Name |
| 29 | Data Residency |
| 30 | Document Type |
| 31 | Storage Location |
| 32 | Access Control |
| 33 | Assessment Area |
| 34 | Total Items |
| 35 | Registered |
| 36 | Transitional |
| 37 | Unregistered/Lost |
| 38 | N/A |
| 39 | Compliance % |
| 40 | Evidence ID |
| 41 | Evidence Type |
| 42 | Description |
| 43 | Related Sheet/Item |
| 44 | Collection Date |
| 45 | Collected By |
| 46 | Retention Period |
| 47 | Notes |

### Data Validation Values

All dropdown/list values used across sheets:

```
HDD, SSD, USB Flash Drive, SD Card, Backup Tape, Optical Media, Other, Public
Internal, Confidential, Restricted, Registered, Unregistered, Pending Disposal
In Transit, Lost/Stolen, N/A, Critical, High, Medium, Low, Yes, No, Unknown
Encrypted (AES-256), Encrypted (Hardware), Not Encrypted, Physical Server
Virtual Server, NAS, SAN, Archive System, Backup Appliance, IaaS, PaaS, SaaS
Hybrid, Multi-Cloud, Switzerland, EU, US, UK, APAC, Multiple Regions
Paper Documents, Microfilm, Microfiche, Archive Boxes, Mixed Media, Key Lock
Combination Lock, Card Access, Biometric, Multi-Factor, None, Screenshot
Configuration Export, Log Sample, Report, Document, Photo, Draft, Final
Requires remediation, Re-assessment required, Approved
Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 47 columns, 69 validation values, 11 colors

---

**END OF SPECIFICATION**


---

*"The price of reliability is the pursuit of the utmost simplicity."*
- C.A.R. Hoare

<!-- QA_VERIFIED: 2026-03-01 -->
