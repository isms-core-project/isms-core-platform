<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.24.3-TG:framework:TG:a.8.24.3 -->
**ISMS-IMP-A.8.24.3-TG - Authentication Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Authentication Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.24.3-TG |
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
- ISMS-IMP-A.8.24.4 (Key Management Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a824_3_authentication_assessment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.24.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 1. Password Security |
| 3 | 2. Multi-Factor Authentication |
| 4 | 3. Certificate-Based Auth |
| 5 | 4. Service Accounts |
| 6 | 5. SSO & Federation |
| 7 | Evidence Register |
| 8 | Summary Dashboard |
| 9 | Approval Sign-Off |

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
| 1 | Min Password Length |
| 2 | Complexity Enforced |
| 3 | Password Expiry |
| 4 | Password History |
| 5 | Account Lockout |
| 6 | Password Strength Meter |
| 7 | Default Passwords |
| 8 | MFA Factor Type |
| 9 | MFA Enrollment Rate |
| 10 | MFA Enforcement |
| 11 | Backup MFA Method |
| 12 | MFA Bypass Allowed |
| 13 | Passwordless Option |
| 14 | Certificate Type |
| 15 | Issuing CA |
| 16 | Key Algorithm |
| 17 | Certificate Validity |
| 18 | CRL/OCSP Configured |
| 19 | Smart Card Required |
| 20 | PIV/CAC Compliant |
| 21 | Service Account Type |
| 22 | Auth Method |
| 23 | Password Rotation |
| 24 | Privileged Account |
| 25 | Account Monitoring |
| 26 | Interactive Login |
| 27 | Least Privilege |
| 28 | SSO Protocol |
| 29 | Identity Provider |
| 30 | MFA at IdP |
| 31 | Just-In-Time Provisioning |
| 32 | Session Timeout |
| 33 | Certificate Validation |
| 34 | Token Encryption |
| 35 | Password |
| 36 | MFA |
| 37 | Properly Hashed |
| 38 | Plaintext (Non-compliant) |
| 39 | Metric (Auto-computed) |
| 40 | Value |
| 41 | Notes |
| 42 | Authentication Domain |
| 43 | Non-Compliant |
| 44 | Partial |
| 45 | Compliant |
| 46 | N/A |
| 47 | Total Items |
| 48 | Compliance % |
| 49 | Evidence ID |
| 50 | Assessment Area |
| 51 | Evidence Type |
| 52 | Description |
| 53 | Location/Path |
| 54 | Date Collected |
| 55 | Collected By |
| 56 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Password, MFA, Certificate, Token, SSO, Federation, Biometric, API Key
Service Account, N/A, End User, Administrator, External User, API Client
Public, Internal, Confidential, Restricted, bcrypt, Argon2, PBKDF2, scrypt
SHA-256, SHA-512, RSA-2048+, ECDSA, None, Properly Hashed, Encrypted
Plaintext (Non-compliant), Salted, Strong (≥14 chars), Adequate (12-13)
Weak (<12), ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, ✅ Yes, ❌ No, ⚠️ Unknown
⚠️ Not Applicable, ≥14 chars, 12-13 chars, <12 chars (weak), 90 days, 180 days
365 days, Never, ≥10 passwords, 5-9 passwords, <5 passwords, Changed
Not Changed (Non-compliant), TOTP (Authenticator App), Push Notification
SMS (Deprecated), Hardware Token, 100%, 90-99%, 75-89%, <75%, Required
Optional, Not Configured, With Approval, Emergency Only
Always (Non-compliant), Client Certificate, Smart Card, Machine/Device
Code Signing, Email, User, ≤1 year, 1-2 years, >2 years, Expired, RSA-4096
RSA-3072, RSA-2048, ECDSA P-256, ECDSA P-384, Ed25519, Database Service
Application Service, API Service, Scheduled Task, Integration
Long Password (≥20 chars), Managed Identity, Secret, Never (Monitored)
On Change Only, Disabled, Enabled (Non-compliant), SAML 2.0, OAuth 2.0, OIDC
WS-Federation, Kerberos, LDAP, ≤1 hour, 1-8 hours, >8 hours, No timeout
Implemented, Planned, Not Implemented, \u2705 On Target, \u26a0\ufe0f At Risk
\u274c Below Target, Password policy, GPO screenshot, MFA enrollment report
Certificate config, PKI documentation, SAML configuration, IdP settings
Service account inventory, Authentication logs, Audit trail, Policy document
Security assessment, Penetration test, Compliance scan, Other, ✅ Verified
⚠️ Pending, ❌ Not Verified, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 9 sheets, 56 columns, 137 validation values, 12 colors

---

**END OF SPECIFICATION**


---

*"Authentication without strong cryptography is a handshake with an impostor."*
— Cryptography principle

<!-- QA_VERIFIED: 2026-03-01 -->
