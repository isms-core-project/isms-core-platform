<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.24.4-TG:framework:TG:a.8.24.4 -->
**ISMS-IMP-A.8.24.4-TG - Key Management Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Key Management Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.24.4-TG |
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
- ISMS-IMP-A.8.24.2 (Data Storage Assessment)
- ISMS-IMP-A.8.24.3 (Authentication Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a824_4_key_management_assessment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.24.4`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 1. Key Generation |
| 3 | 2. Key Storage |
| 4 | 3. Key Rotation |
| 5 | 4. Key Backup & Recovery |
| 6 | 5. Certificate Management |
| 7 | 6. Key Destruction |
| 8 | Evidence Register |
| 9 | Summary Dashboard |
| 10 | Approval Sign-Off |

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
| 1 | Random Number Generator |
| 2 | Generation Location |
| 3 | Key Ceremony Performed |
| 4 | Entropy Source Verified |
| 5 | Generation Audit Log |
| 6 | HSM/KMS Model |
| 7 | FIPS 140 Level |
| 8 | Access Control Method |
| 9 | Encryption at Rest |
| 10 | Physical Security |
| 11 | Key Backup Exists |
| 12 | Rotation Schedule |
| 13 | Last Rotation Date |
| 14 | Next Rotation Due |
| 15 | Automated Rotation |
| 16 | Rotation Tested |
| 17 | Re-encryption Required |
| 18 | Backup Method |
| 19 | Backup Encryption |
| 20 | Backup Location |
| 21 | Recovery Tested |
| 22 | Last Recovery Test |
| 23 | RTO (Recovery Time) |
| 24 | Escrow Agreement |
| 25 | Certificate Type |
| 26 | Issuing CA |
| 27 | Certificate Validity |
| 28 | Expiration Date |
| 29 | Auto-Renewal |
| 30 | Revocation Method |
| 31 | Monitoring Enabled |
| 32 | AES-256 |
| 33 | RSA-4096 |
| 34 | RSA-3072 |
| 35 | Other |
| 36 | Active |
| 37 | Archived |
| 38 | Destroyed |
| 39 | Pending Rotation |
| 40 | Metric (Auto-computed) |
| 41 | Value |
| 42 | Notes |
| 43 | Key Management Domain |
| 44 | Non-Compliant |
| 45 | Partial |
| 46 | Compliant |
| 47 | N/A |
| 48 | Total Items |
| 49 | Compliance % |
| 50 | Evidence ID |
| 51 | Assessment Area |
| 52 | Evidence Type |
| 53 | Description |
| 54 | Location/Path |
| 55 | Date Collected |
| 56 | Collected By |
| 57 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Encryption Key, Signing Key, Authentication Key, Certificate, Master Key
Data Encryption Key, Key Encryption Key, Session Key, N/A, AES-256, AES-128
RSA-4096, RSA-3072, RSA-2048, Ed25519, ECDSA P-256, ECDSA P-384, ChaCha20
Other, 256, 384, 512, 2048, 3072, 4096, 8192, HSM, Cloud KMS, TPM
Software Keystore, File-based, Database, Smart Card, Vault, Public, Internal
Confidential, Restricted, Active, Suspended, Archived, Destroyed
Pending Rotation, ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, ✅ Yes, ❌ No
⚠️ Unknown, ⚠️ Not Applicable, Hardware RNG, OS Crypto RNG, HSM RNG, TPM RNG
FIPS 140-2 Validated, NIST SP 800-90A, Non-compliant, KMS, Local System
Cloud Service, Level 1, Level 2, Level 3, Level 4, Not Validated, Role-based
Certificate-based, MFA Required, PIN/Password, Dual Control
Locked Data Center, Secure Room, Tamper-evident, Cloud Provider, Inadequate
Hourly, Daily, Weekly, Monthly, Quarterly, Annually, Biennially, On Compromise
Never, ⏳ In Progress, HSM Backup, KMS Backup, Encrypted File, Key Escrow
Split Knowledge, Cloud Backup, No Backup, ⏳ Scheduled, TLS/SSL Server
TLS/SSL Client, Code Signing, Email (S/MIME), User Authentication
CA Certificate, Wildcard, SAN, Self-signed, ≤90 days, 91-180 days
181-365 days, 366-397 days, >397 days (non-compliant), Expired, CRL, OCSP
OCSP Stapling, Not Configured, Yes, No, Partially, Hardware Shredding
Crypto-erasure, Physical Destruction, Vendor-managed, Degaussing
Overwrite (multi-pass), \u2705 Destroyed, \u23f3 Pending, \u274c Overdue
\u2705 Yes, \u274c No, \u2705 On Target, \u26a0\ufe0f At Risk
\u274c Below Target, Key generation log, HSM configuration, KMS architecture
Rotation log, Backup procedure, Recovery test, Certificate inventory
CA audit report, FIPS certificate, Key ceremony record, Access log
Destruction record, Algorithm verification, Third-party audit, ✅ Verified
⚠️ Pending, ❌ Not Verified, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 10 sheets, 57 columns, 154 validation values, 12 colors

---

**END OF SPECIFICATION**


---

*"The zeros of the Riemann zeta function and the prime numbers are the two most important objects in mathematics."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
