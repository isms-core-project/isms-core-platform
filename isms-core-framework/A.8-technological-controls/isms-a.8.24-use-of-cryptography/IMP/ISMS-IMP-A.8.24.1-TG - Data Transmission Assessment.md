<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.24.1-TG:framework:TG:a.8.24.1 -->
**ISMS-IMP-A.8.24.1-TG - Data Transmission Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Data Transmission Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.24.1-TG |
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
- ISMS-IMP-A.8.24.2 (Data Storage Assessment)
- ISMS-IMP-A.8.24.3 (Authentication Assessment)
- ISMS-IMP-A.8.24.4 (Key Management Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a824_1_data_transmission_assessment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.24.1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 1.1 External HTTPS-TLS |
| 3 | 1.2 Internal HTTPS-TLS |
| 4 | 2.1 Email Encryption |
| 5 | 2.2 Digital Signatures |
| 6 | 3.1 File Transfer Protocols |
| 7 | 4.1 VPN |
| 8 | 4.2 SSH |
| 9 | 4.3 RDP |
| 10 | 5.1 API Security |
| 11 | 6.1 Database Connections |
| 12 | 6.2 Wireless Networks |
| 13 | 7.1 Cloud Transmission |
| 14 | Evidence Register |
| 15 | Summary Dashboard |
| 16 | Approval Sign-Off |

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
| 1 | Service Description |
| 2 | Current TLS Version |
| 3 | Certificate Source (CA) |
| 4 | Certificate Validity |
| 5 | Status |
| 6 | Evidence Location |
| 7 | Gap Description |
| 8 | Remediation Needed |
| 9 | Data Classification |
| 10 | Certificate Type |
| 11 | Email System |
| 12 | Encryption Solution |
| 13 | Encryption Method |
| 14 | User Adoption Rate |
| 15 | Use Case |
| 16 | Signature Method |
| 17 | Certificate Source |
| 18 | Transfer Method/System |
| 19 | Protocol Used |
| 20 | Authentication Method |
| 21 | VPN Solution |
| 22 | Protocol |
| 23 | Encryption Algorithm |
| 24 | MFA Enabled |
| 25 | System/Service |
| 26 | SSH Version |
| 27 | Key Algorithm |
| 28 | System/Environment |
| 29 | RDP Access Method |
| 30 | TLS Encryption |
| 31 | NLA Enabled |
| 32 | API Name/Service |
| 33 | TLS Version |
| 34 | API Key Management |
| 35 | Token Expiry |
| 36 | Database System |
| 37 | Connection Encryption |
| 38 | Certificate Validation |
| 39 | Network SSID |
| 40 | Encryption Standard |
| 41 | Cloud Provider/Service |
| 42 | Connection Method |
| 43 | Encryption |
| 44 | Transmission Domain |
| 45 | Non-Compliant |
| 46 | Partial |
| 47 | Compliant |
| 48 | N/A |
| 49 | Total Items |
| 50 | Compliance % |
| 51 | Evidence ID |
| 52 | Assessment Area |
| 53 | Evidence Type |
| 54 | Description |
| 55 | Location/Path |
| 56 | Date Collected |
| 57 | Collected By |
| 58 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
✅ Yes, ❌ No, ⚠️ Not Applicable, ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A
\u2705 On Target, \u26a0\ufe0f At Risk, \u274c Below Target
Configuration file, Screenshot, Network scan, Documentation, Vendor spec
Certificate inventory, Audit log, Compliance report, Other, ✅ Verified
⚠️ Pending, ❌ Not Verified, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 16 sheets, 58 columns, 30 validation values, 12 colors

---

**END OF SPECIFICATION**


---

*"Encryption in transit is the lock on the front door of your data."*
— Cryptography principle

<!-- QA_VERIFIED: 2026-03-01 -->
