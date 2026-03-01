<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.24.2-TG:framework:TG:a.8.24.2 -->
**ISMS-IMP-A.8.24.2-TG - Data Storage Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Data Storage Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.24.2-TG |
| **Related Policy** | ISMS-POL-A.8.24 (Use of Cryptography) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.24 (Use of Cryptography) |
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

- ISMS-POL-A.8.24 (Use of Cryptography)
- ISMS-IMP-A.8.24.1 (Data Transmission Assessment)
- ISMS-IMP-A.8.24.3 (Authentication Assessment)
- ISMS-IMP-A.8.24.4 (Key Management Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a824_2_data_storage_assessment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.24.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 1. Mobile Devices |
| 3 | 2. Laptops & Workstations |
| 4 | 3. Servers |
| 5 | 4. Databases |
| 6 | 5. Cloud Storage |
| 7 | 6. Backups |
| 8 | 7. Removable Media |
| 9 | Evidence Register |
| 10 | Summary Dashboard |
| 11 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #0000FF | Custom |
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #555555 | Custom |
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
| 1 | Not Encrypted |
| 2 | Partially Encrypted |
| 3 | ❌ No |
| 4 | HSM |
| 5 | Cloud KMS |
| 6 | Metric (Auto-computed) |
| 7 | Value |
| 8 | Notes |
| 9 | Storage Domain |
| 10 | Key Rotation Off |
| 11 | HSM in Use |
| 12 | Non-Compliant |
| 13 | Total Items |
| 14 | Compliance % |
| 15 | Evidence ID |
| 16 | Assessment Area |
| 17 | Evidence Type |
| 18 | Description |
| 19 | Location/Path |
| 20 | Date Collected |
| 21 | Collected By |
| 22 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Public, Internal, Confidential, Restricted, N/A, Encrypted, Not Encrypted
Partially Encrypted, Full Disk, File-level, Database TDE, Volume, Container
Application-level, Hardware-based, HSM, Cloud KMS, TPM, Software-based, Manual
Vendor-managed, ✅ Yes, ❌ No, ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant
⚠️ Unknown, ⚠️ Not Applicable, \u2705 On Target, \u26a0\ufe0f At Risk
\u274c Below Target, Configuration file, Screenshot, Encryption report
MDM report, Audit log, Key management record, Backup verification
Vendor documentation, Compliance certificate, Other, ✅ Verified, ⚠️ Pending
❌ Not Verified, Draft, Final, Requires remediation, Re-assessment required
Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 22 columns, 52 validation values, 12 colors

---

**END OF SPECIFICATION**


---

*"Data at rest without encryption is data at risk."*
— Storage security principle

<!-- QA_VERIFIED: 2026-03-01 -->
