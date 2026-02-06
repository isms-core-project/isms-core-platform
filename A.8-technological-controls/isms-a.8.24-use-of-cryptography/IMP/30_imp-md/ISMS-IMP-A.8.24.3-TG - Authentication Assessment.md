**ISMS-IMP-A.8.24.3-TG - Authentication Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.24.3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Authentication Cryptographic Controls |
| **Related Policy** | ISMS-POL-A.8.24, Section 3.4 (Authentication and Digital Signature Requirements) |
| **Purpose** | Assess implementation of cryptographic controls for authentication mechanisms across 5 authentication categories (Password Security, MFA, Certificate-Based Auth, Service Accounts, SSO/Federation) |
| **Target Audience** | Identity & Access Management (IAM) Administrators, Security Engineers, System Administrators, Directory Services Administrators, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational (Authentication Controls) |
| **Review Cycle** | Quarterly or After Major IAM Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Authentication assessment workbook | ISMS Implementation Team |

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

# Instructions for Completing This Assessment

## How to Use This Document

This technical specification defines the structure, validation rules, and formulas for the Authentication Assessment Excel workbook (`ISMS-IMP-A.8.24.3_Authentication_[DATE].xlsx`).

**Workbook Generation:** Python script `generate_a824_3_authentication_assessment.py` creates the workbook based on this specification.

**Assessment Completion Process:**

1. **Read each section** and determine if the authentication method applies to your organization
2. **Check Yes/No/Not Applicable** for each assessment question
3. **If Yes:** Complete the assessment table with current authentication controls
4. **Mark Status:** ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant / N/A
5. **If ⚠️ or ❌:** Complete the Exception/Deviation Documentation section
6. **Provide Evidence:** Document where compliance evidence can be found
7. **Review Compliance Checklist:** Check all items that apply to your implementation

## Status Legend

| Symbol | Meaning | Description |
|--------|---------|-------------|
| **✅** | **Compliant** | Fully meets policy requirements, no gaps identified |
| **⚠️** | **Partial** | Some requirements met, minor gaps exist, remediation planned |
| **❌** | **Non-Compliant** | Does not meet policy requirements, significant gaps |
| **N/A** | **Not Applicable** | This requirement does not apply to your environment |

## Evidence Types

Acceptable evidence includes:

- Password policy documentation
- Active Directory Group Policy Objects (GPO)
- MFA enrollment reports
- Certificate authority configurations
- PKI infrastructure documentation
- SSO/SAML configuration screenshots
- Identity provider (IdP) settings
- Service account inventory
- Authentication logs and audit trails
- Password hash algorithm verification
- Account lockout policy screenshots
- MFA bypass exception approvals
- Federation trust relationships
- Privileged access management (PAM) reports

---

# Common Column Structure (All Assessment Sheets)

All 5 assessment sheets (Password Security through SSO & Federation) use this standard column layout:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | System/Application | 30 | Text | Free text |
| B | Authentication Method | 22 | Dropdown | Password, MFA, Certificate, Token, SSO, Federation, Biometric, API Key, Service Account, N/A |
| C | User Type | 18 | Dropdown | End User, Administrator, Service Account, External User, API Client, N/A |
| D | Data Classification | 18 | Dropdown | Public, Internal, Confidential, Restricted, N/A |
| E | Cryptographic Algorithm | 22 | Dropdown | bcrypt, Argon2, PBKDF2, scrypt, SHA-256, SHA-512, RSA-2048+, ECDSA, None, N/A |
| F | Hash/Encryption Status | 20 | Dropdown | Properly Hashed, Encrypted, Plaintext (Non-compliant), Salted, N/A |
| G | Password Complexity | 20 | Dropdown | Strong (≥14 chars), Adequate (12-13), Weak (<12), N/A |
| H | Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| I | Evidence Location | 28 | Text | Free text (file path or evidence ID) |
| J | Gap Description | 30 | Text | Free text (required if Status = Partial/Non-Compliant) |
| K | Remediation Needed | 14 | Dropdown | Yes, No |
| L | Exception ID | 14 | Text | Free text (if formal exception submitted) |
| M | Risk ID | 14 | Text | Free text (if risk accepted) |
| N | Compensating Controls | 30 | Text | Free text (if applicable) |
| O | Responsible Person | 20 | Text | Free text (name and role) |
| P | Target Date | 14 | Date | Date picker (DD.MM.YYYY) |
| Q | Budget Required | 15 | Dropdown | Yes, No, Unknown |

---

# Password Security

**Policy Requirement:** Passwords MUST be hashed using approved algorithms (bcrypt, Argon2, PBKDF2, scrypt). Minimum 12 characters, complexity requirements enforced 

**Assessment Question:**

**Does your organization use password-based authentication for any systems or applications?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 2
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| System/Application | Authentication Method | User Type | Data Classification | Cryptographic Algorithm | Hash/Encryption Status | Password Complexity | Status | Evidence Location | Gap Description | Remediation Needed |
|-------------------|----------------------|-----------|--------------------|-----------------------|------------------------|--------------------| ---------|-------------------|-----------------|-------------------|
| Example: Active Directory, Entra ID, PostgreSQL database, Linux /etc/shadow | | | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Password-Specific Additional Columns:**

| Column | Header | Width | Validation Options |
|--------|--------|-------|--------------------|
| R | Min Password Length | 16 | ≥14 chars, 12-13 chars, <12 chars (weak), N/A |
| S | Complexity Enforced | 16 | Yes, No, N/A |
| T | Password Expiry | 18 | 90 days, 180 days, 365 days, Never, N/A |
| U | Password History | 16 | ≥10 passwords, 5-9 passwords, <5 passwords, None, N/A |
| V | Account Lockout | 16 | 5 attempts, 10 attempts, None, N/A |
| W | Lockout Duration | 16 | 30 minutes, Until admin unlock, None, N/A |

**Additional Details:**

- **Total systems using passwords:** _________
- **Primary identity provider:** [ ] Active Directory [ ] Entra ID [ ] LDAP [ ] Other: _____
- **Password policy enforcement:** [ ] Centralized (AD/Entra ID) [ ] Per-application [ ] Mixed

---

**PASSWORD SECURITY COMPLIANCE CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| Approved hash algorithm (bcrypt, Argon2, PBKDF2, scrypt) | [ ] Yes [ ] No [ ] N/A | Verify via database query or config file |
| Minimum 12 characters (14 characters preferred) | [ ] Yes [ ] No [ ] N/A | AD: Get-ADDefaultDomainPasswordPolicy |
| Complexity requirements enforced (upper, lower, numbers, special) | [ ] Yes [ ] No [ ] N/A | Prevents simple passwords |
| Password expiration: 90 days (privileged), 180 days (standard), OR no expiry with strong MFA | [ ] Yes [ ] No [ ] N/A | Modern guidance allows no expiry with MFA |
| Password history: Minimum 10 passwords remembered | [ ] Yes [ ] No [ ] N/A | Prevents password recycling |
| Account lockout: 5 failed attempts, 30-minute lockout | [ ] Yes [ ] No [ ] N/A | Prevents brute force attacks |
| Passwords NOT stored in plaintext | [ ] Yes [ ] No [ ] N/A | CRITICAL - plaintext is immediate failure |
| Weak algorithms NOT used (MD5, SHA-1, DES, reversible encryption) | [ ] Yes [ ] No [ ] N/A | Must migrate if found |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Strong MFA enforced (compensates for weaker passwords)
  - [ ] Network segmentation (limits exposure)
  - [ ] Enhanced monitoring (detects anomalies)
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________
- **Budget required:** [ ] Yes [ ] No  Amount: _________

---

# Multi-Factor Authentication (MFA)

**Policy Requirement:** MFA REQUIRED for all privileged accounts, access to Confidential/Restricted data, and all remote access 

**Assessment Question:**

**Does your organization require multi-factor authentication (MFA) for any user accounts or systems?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 3
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| System/Application | Authentication Method | User Type | Data Classification | MFA Method | Enrollment Rate | Status | Evidence Location | Gap Description | Remediation Needed |
|-------------------|----------------------|-----------|--------------------|-----------|-----------------| ---------|-------------------|-----------------|-------------------|
| Example: VPN access, Entra ID, AWS Console, Privileged accounts | | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**MFA-Specific Additional Columns:**

| Column | Header | Width | Validation Options |
|--------|--------|-------|--------------------|
| R | MFA Method | 20 | TOTP (Authenticator), Push (Duo/Okta), Hardware Token, Smart Card, SMS (not recommended), N/A |
| S | Enrollment Rate | 16 | % (e.g., 95%, 80%, 60%) |
| T | Backup MFA | 18 | Backup codes, SMS (fallback), None, N/A |
| U | Bypass Exceptions | 16 | Number (e.g., 0, 5 users, Unknown) |

**Additional Details:**

- **MFA provider:** [ ] Duo [ ] Okta [ ] Azure MFA [ ] Google Authenticator [ ] Other: _____
- **MFA enrollment target:** [ ] 100% (privileged) [ ] 90%+ (all users) [ ] Other: _____
- **Conditional access configured:** [ ] Yes [ ] No

---

**MFA COMPLIANCE CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| MFA enforced for ALL privileged accounts (100% enrollment) | [ ] Yes [ ] No [ ] N/A | Domain Admins, root, AWS admin, etc. |
| MFA enforced for access to Confidential/Restricted data | [ ] Yes [ ] No [ ] N/A | Conditional access policies |
| MFA enforced for ALL remote access (VPN, RDP, SSH) | [ ] Yes [ ] No [ ] N/A | Highest-risk attack vector |
| Approved MFA methods (TOTP preferred, push/hardware acceptable) | [ ] Yes [ ] No [ ] N/A | Avoid SMS for high-value accounts |
| SMS-based MFA NOT used for privileged accounts | [ ] Yes [ ] No [ ] N/A | SMS vulnerable to SIM swapping |
| MFA bypass exceptions documented and approved by CISO | [ ] Yes [ ] No [ ] N/A | Use ISMS-POL-A.8.24-S5.B Exception Form |
| MFA enrollment ≥90% for required populations | [ ] Yes [ ] No [ ] N/A | Target: 95%+ enrollment |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Restricted network access (VPN-only, IP whitelist)
  - [ ] Enhanced monitoring and alerting
  - [ ] Shorter password expiry (compensating control)
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# Certificate-Based Authentication

**Policy Requirement:** Certificate-based authentication MUST use RSA 2048-bit minimum (RSA 3072+ or ECDSA P-256+ preferred). CRL/OCSP revocation checking REQUIRED 

**Assessment Question:**

**Does your organization use certificate-based authentication (PKI, client certificates, smart cards)?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 4
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| System/Application | Authentication Method | User Type | Data Classification | Certificate Type | Key Algorithm | Certificate Validity | Status | Evidence Location | Gap Description | Remediation Needed |
|-------------------|----------------------|-----------|--------------------|-----------------|--------------|--------------------|---------|-------------------|-----------------|-------------------|
| Example: VPN client certificates, SSH certificates, Smart cards (PIV/CAC), TLS mutual auth | | | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Certificate-Specific Additional Columns:**

| Column | Header | Width | Validation Options |
|--------|--------|-------|--------------------|
| R | Certificate Type | 20 | Client Certificate, Smart Card (PIV/CAC), SSH Certificate, Code Signing, N/A |
| S | Key Algorithm | 18 | RSA-2048, RSA-3072, RSA-4096, ECDSA P-256, ECDSA P-384, N/A |
| T | Certificate Validity | 18 | ≤825 days (internal), ≤398 days (public CA), >825 days (non-compliant) |
| U | CRL/OCSP Enabled | 16 | Yes, No, N/A |
| V | CA Type | 16 | Internal PKI, Public CA, Both, N/A |

**Additional Details:**

- **PKI infrastructure:** [ ] Internal CA (Microsoft CA, OpenSSL) [ ] Public CA [ ] Both [ ] None
- **Certificate usage:** [ ] VPN [ ] SSH [ ] Smart cards [ ] TLS mutual auth [ ] Code signing [ ] Other: _____
- **Certificate lifecycle management:** [ ] Automated [ ] Manual [ ] Mixed

---

**CERTIFICATE AUTHENTICATION COMPLIANCE CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| RSA 2048-bit minimum (RSA 3072+ or ECDSA P-256+ preferred) | [ ] Yes [ ] No [ ] N/A | Verify certificate properties |
| Certificate validity: ≤825 days (internal PKI), ≤398 days (public CA) | [ ] Yes [ ] No [ ] N/A | Internal PKI not subject to CA/B Forum |
| CRL/OCSP revocation checking REQUIRED | [ ] Yes [ ] No [ ] N/A | Test with revoked certificate |
| Smart cards: PIV/CAC compliant (if applicable) | [ ] Yes [ ] No [ ] N/A | Government/military requirement |
| Certificate expiration monitoring configured | [ ] Yes [ ] No [ ] N/A | 90-day advance alerts |
| Certificate enrollment automated (if >50 certificates) | [ ] Yes [ ] No [ ] N/A | Manual not scalable |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Certificate pinning (prevents MITM)
  - [ ] Enhanced logging of certificate usage
  - [ ] Restricted certificate usage (specific IPs only)
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# Service Accounts

**Policy Requirement:** Service accounts MUST use strong passwords (same complexity as human accounts) OR certificate-based authentication. Password rotation quarterly (90 days) minimum OR managed service identities. Service accounts MUST NOT have interactive login rights 

**Assessment Question:**

**Does your organization use service accounts (non-human identities for applications, scripts, scheduled tasks)?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 5
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| System/Application | Authentication Method | User Type | Data Classification | Account Name | Password Age | Privileges | Status | Evidence Location | Gap Description | Remediation Needed |
|-------------------|----------------------|-----------|--------------------|--------------|--------------|-----------| ---------|-------------------|-----------------|-------------------|
| Example: SQL Server service account, Linux cron job, Entra ID application, AWS IAM service account | | | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Service Account-Specific Additional Columns:**

| Column | Header | Width | Validation Options |
|--------|--------|-------|--------------------|
| R | Account Name | 20 | Free text (e.g., svc_backup, app_service) |
| S | Password Age (Days) | 18 | <90 days, 90-180 days, >180 days (non-compliant), Managed Identity (N/A) |
| T | Privileges | 20 | Standard User, Local Admin, Domain Admin, Database Owner, Root, N/A |
| U | Interactive Login | 16 | Allowed (non-compliant), Denied (compliant), N/A |
| V | Managed Identity | 16 | Yes (Azure MSI/AWS IAM), No, N/A |

**Additional Details:**

- **Total service accounts:** _________
- **Service accounts with admin privileges:** _________
- **Service accounts using managed identities:** _________
- **Password rotation process:** [ ] Automated [ ] Manual [ ] None

---

**SERVICE ACCOUNT COMPLIANCE CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| Service account inventory maintained and reviewed quarterly | [ ] Yes [ ] No [ ] N/A | Complete inventory required |
| Service account passwords rotated quarterly (90 days) OR managed identities used | [ ] Yes [ ] No [ ] N/A | Managed identities preferred |
| Service accounts use strong passwords (same complexity as human accounts) | [ ] Yes [ ] No [ ] N/A | Unless certificate-based |
| Service accounts do NOT have interactive login rights | [ ] Yes [ ] No [ ] N/A | "Deny log on locally" GPO setting |
| Service accounts follow least privilege principle | [ ] Yes [ ] No [ ] N/A | No unnecessary admin rights |
| Service account usage monitored and logged | [ ] Yes [ ] No [ ] N/A | Detect anomalous usage |
| Managed service identities used where available (Azure MSI, AWS IAM roles) | [ ] Yes [ ] No [ ] N/A | Eliminates password management |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Service account usage restricted to specific IPs/subnets
  - [ ] Enhanced monitoring and alerting
  - [ ] Service account isolated to specific systems
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# SSO & Federation

**Policy Requirement:** SSO/Federation MUST use SAML 2.0, OAuth 2.0, or OpenID Connect (OIDC). IdP signing certificates MUST be valid and monitored for expiration. Federation trust relationships MUST be documented and reviewed annually 

**Assessment Question:**

**Does your organization use Single Sign-On (SSO) or federated authentication with external identity providers?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 6
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| System/Application | Authentication Method | User Type | Data Classification | SSO Protocol | IdP | Certificate Expiry | Status | Evidence Location | Gap Description | Remediation Needed |
|-------------------|----------------------|-----------|--------------------|--------------|----|-------------------| ---------|-------------------|-----------------|-------------------|
| Example: Office 365, Salesforce, AWS SSO, Internal apps via Entra ID SAML | | | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**SSO/Federation-Specific Additional Columns:**

| Column | Header | Width | Validation Options |
|--------|--------|-------|--------------------|
| R | SSO Protocol | 20 | SAML 2.0, OAuth 2.0, OIDC, WS-Federation, Legacy (non-compliant) |
| S | Identity Provider (IdP) | 20 | Entra ID, Okta, Auth0, Google, Internal, Other |
| T | IdP Certificate Expiry | 18 | <90 days (urgent), 90-180 days, >180 days, N/A |
| U | Federation Trust Type | 18 | Internal (same org), External (partner), Public (SaaS) |
| V | Trust Documentation | 16 | Yes (documented), No, N/A |

**Additional Details:**

- **SSO solution:** [ ] Entra ID [ ] Okta [ ] Auth0 [ ] Google Workspace [ ] Other: _____
- **Federated applications:** _________
- **External IdP trusts:** [ ] Yes (count: _____) [ ] No
- **IdP certificate monitoring:** [ ] Automated [ ] Manual [ ] None

---

**SSO & FEDERATION COMPLIANCE CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| Approved protocols (SAML 2.0, OAuth 2.0, OIDC) | [ ] Yes [ ] No [ ] N/A | Legacy protocols non-compliant |
| IdP signing certificates valid and monitored | [ ] Yes [ ] No [ ] N/A | 90-day advance alerts required |
| Certificate expiration >90 days from now | [ ] Yes [ ] No [ ] N/A | Urgent action if <90 days |
| Federation trust relationships documented | [ ] Yes [ ] No [ ] N/A | Trust agreements, scope, SLA |
| Federation trusts reviewed annually | [ ] Yes [ ] No [ ] N/A | CISO approval for external trusts |
| SSO conditional access policies configured | [ ] Yes [ ] No [ ] N/A | MFA, location-based, device compliance |
| SSO session timeout configured (≤8 hours for high-risk, ≤24 hours standard) | [ ] Yes [ ] No [ ] N/A | Prevents indefinite sessions |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Enhanced monitoring of federation events
  - [ ] Restricted federation scope (specific apps only)
  - [ ] Additional authentication factors for federated access
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# Overall Authentication Summary

## Compliance Summary

**Total Assessment Areas:** _______

| Authentication Category | Status | Percentage |
|------------------------|--------|------------|
| Password Security | | |
| Multi-Factor Authentication | | |
| Certificate-Based Authentication | | |
| Service Accounts | | |
| SSO & Federation | | |
| **Overall** | | |

**Instructions for Completion:**

- Count the number of each status (✅ / ⚠️ / ❌) per category
- Calculate percentage: (Compliant Count / Total Items) × 100
- Exclude N/A items from total when calculating compliance percentage
- Target: ≥90% Compliant for mature ISMS

## Critical Gaps Identified

List the most critical gaps that require immediate attention:

1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________

**Guidance:**

- Critical gaps typically include:
  - ❌ Plaintext passwords stored anywhere
  - ❌ Weak hash algorithms (MD5, SHA-1) in use
  - ❌ Privileged accounts without MFA
  - ❌ Service accounts with admin rights and never-rotated passwords
  - ❌ IdP signing certificates expiring within 90 days
  - ❌ SMS-based MFA for privileged accounts
  - ❌ No service account inventory

## Top Remediation Priorities

| Priority | Gap Description | Target Date | Responsible Person |
|----------|-----------------|-------------|-------------------|
| **High** | | | |
| **High** | | | |
| **Medium** | | | |

**Priority Definitions:**

- **High:** Authentication compromise risk, compliance violation, or operational failure imminent
- **Medium:** Compliance gap with planned remediation, low immediate risk
- **Low:** Best practice improvement, no compliance impact

---

# Evidence Register

**List all evidence files/documents referenced in this assessment:**

| Evidence ID | Description | Location | Date Collected |
|-------------|-------------|----------|----------------|
| EV-1-001 | AD password policy export | /evidence/a824_3/ | DD.MM.YYYY |
| EV-2-001 | MFA enrollment report | /evidence/a824_3/ | DD.MM.YYYY |
| | | | |
| | | | |

**Evidence Naming Convention:**
```
EV-[Section]-[System]-[Date]-[Type].[ext]
```

**Examples:**

- `EV-1-AD-Password-Policy-20260115.txt`
- `EV-2-MFA-Enrollment-Report-20260115.xlsx`
- `EV-4-ServiceAccounts-Inventory-20260115.csv`
- `EV-5-SAML-IdP-Config-20260115.png`

**Evidence Types:**

- Password policy exports (GPO, Entra ID, application configs)
- Password hash algorithm verification (database queries, sanitized)
- MFA enrollment reports
- Conditional access policies
- Certificate inventories
- PKI configuration
- Service account inventories
- SSO/Federation configuration
- IdP signing certificates

**Evidence Storage:**

- **Location:** [Organization's evidence repository path]
- **Retention:** Audit cycle + 1 year minimum
- **Access Control:** Restricted to security team and auditors
- **Sensitivity:** Sanitize password hashes, credentials, private keys

---

# Approval and Sign-Off

## Assessment Summary

**Assessment Document:** ISMS-IMP-A.8.24.3 - Authentication Assessment  
**Assessment Period:** From __________ To __________  
**Overall Compliance Rate:** _______ % (from Summary Dashboard Section 6.1)  
**Assessment Status:** [ ] Draft [ ] Final [ ] Requires remediation [ ] Re-assessment required

**Key Findings:**

- Authentication systems assessed: _______
- Compliant authentication controls: _______
- Controls requiring remediation: _______
- Critical gaps identified: _______
- High-priority remediation items: _______

---

## Assessment Completed By

**Name:** _______________________  
**Role:** _______________________  
**Department:** _______________________  
**Email:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Certification:**
I certify that this assessment was completed with due diligence, all authentication control information is accurate to the best of my knowledge, password hash algorithms have been verified (not assumed), and all evidence has been collected and verified.

---

## Reviewed By (Information Security Officer)

**Name:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Review Comments:**
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

**Review Outcome:**

- [ ] Approved - Assessment complete and accurate
- [ ] Approved with minor corrections - Specific items to address: _______
- [ ] Requires revision - Significant issues identified, re-submit required

---

## Approved By (CISO)

**Name:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Approval Decision:**

- [ ] Approved - Authentication posture acceptable, remediation plans approved
- [ ] Approved with conditions - Remediation must be completed by: _______
- [ ] Rejected - Re-assessment required due to: _______

**Risk Acceptance:**
For any documented exceptions/deviations, I accept the residual risk based on:

- Documented risk assessment
- Approved compensating controls
- Business justification
- Compliance with exception approval process (ISMS-POL-A.8.24-S5.B)

**Budget Approval:**
Remediation budget requirement: _______

- [ ] Approved
- [ ] Requires further justification
- [ ] Deferred to next budget cycle

---

## Next Review Date

**Next Scheduled Assessment:** _______________________

**Review Cycle:** Quarterly (every 3 months) or upon:

- Password database breach or compromise
- Discovery of plaintext passwords
- Discovery of weak hash algorithms (MD5, SHA-1)
- Privileged account compromise
- IdP certificate expiration incident
- Failed audit findings on authentication
- Major IAM system changes

**Interim Monitoring:**

- Password policy compliance: Quarterly reviews
- MFA enrollment rates: Monthly tracking
- Service account password age: Quarterly audits
- Certificate expiration monitoring: Continuous (90-day alerts)
- IdP signing certificate expiration: 90-day alerts
- Remediation progress: Tracked monthly

---

## Distribution List

This assessment shall be distributed to:

- [ ] Chief Information Security Officer (CISO)
- [ ] Information Security Officer (ISO)
- [ ] Identity & Access Management (IAM) team
- [ ] Directory Services Administrators
- [ ] Security Operations team
- [ ] Compliance team
- [ ] Internal Audit
- [ ] IT Management
- [ ] Other: _______________________

**Storage Location:**

- **ISMS Repository:** `ISMS/Controls/A.8.24_Use_of_Cryptography/Assessments/`
- **Filename:** `ISMS-IMP-A.8.24.3_Authentication_[DATE]_APPROVED.xlsx`

---

# APPENDIX: Technical Notes for Workbook Developers

## A.1 Excel Workbook Structure

**Sheet Names (9 sheets total):**
1. Instructions & Legend
2. 1. Password Security
3. 2. Multi-Factor Authentication (MFA)
4. 3. Certificate-Based Authentication
5. 4. Service Accounts
6. 5. SSO & Federation
7. Summary Dashboard
8. Evidence Register
9. Approval Sign-Off

## A.2 Data Validation Rules

**Status Dropdown:**

- Formula: `"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"`
- Applied to: Column H (Status) in all assessment sheets
- Allow blank: No

**Authentication Method Dropdown:**

- Formula: `"Password,MFA,Certificate,Token,SSO,Federation,Biometric,API Key,Service Account,N/A"`
- Applied to: Column B in all assessment sheets
- Allow blank: No

**User Type Dropdown:**

- Formula: `"End User,Administrator,Service Account,External User,API Client,N/A"`
- Applied to: Column C in all assessment sheets
- Allow blank: No

**Data Classification Dropdown:**

- Formula: `"Public,Internal,Confidential,Restricted,N/A"`
- Applied to: Column D in all assessment sheets
- Allow blank: No

**Cryptographic Algorithm Dropdown:**

- Formula: `"bcrypt,Argon2,PBKDF2,scrypt,SHA-256,SHA-512,RSA-2048+,ECDSA,None,N/A"`
- Applied to: Column E in all assessment sheets
- Allow blank: No

**Hash/Encryption Status Dropdown:**

- Formula: `"Properly Hashed,Encrypted,Plaintext (Non-compliant),Salted,N/A"`
- Applied to: Column F in all assessment sheets
- Allow blank: No

**Password Complexity Dropdown:**

- Formula: `"Strong (≥14 chars),Adequate (12-13),Weak (<12),N/A"`
- Applied to: Column G in all assessment sheets
- Allow blank: No

**Remediation Needed Dropdown:**

- Formula: `"Yes,No"`
- Applied to: Column K in all assessment sheets
- Allow blank: No

**Budget Required Dropdown:**

- Formula: `"Yes,No,Unknown"`
- Applied to: Column Q in all assessment sheets
- Allow blank: No

**Response Dropdown (Assessment Question):**

- Formula: `"Yes,No,Not Applicable"`
- Applied to: Response field for each section's assessment question
- Allow blank: No

**Checklist Items:**

- Formula: `"Yes,No,N/A"`
- Applied to: All compliance checklist Status columns
- Allow blank: No

**Password Security-Specific Dropdowns:**

- **Min Password Length (R):** `"≥14 chars,12-13 chars,<12 chars (weak),N/A"`
- **Complexity Enforced (S):** `"Yes,No,N/A"`
- **Password Expiry (T):** `"90 days,180 days,365 days,Never,N/A"`
- **Password History (U):** `"≥10 passwords,5-9 passwords,<5 passwords,None,N/A"`
- **Account Lockout (V):** `"5 attempts,10 attempts,None,N/A"`
- **Lockout Duration (W):** `"30 minutes,Until admin unlock,None,N/A"`

**MFA-Specific Dropdowns:**

- **MFA Method (R):** `"TOTP (Authenticator),Push (Duo/Okta),Hardware Token,Smart Card,SMS (not recommended),N/A"`
- **Backup MFA (T):** `"Backup codes,SMS (fallback),None,N/A"`

**Certificate-Specific Dropdowns:**

- **Certificate Type (R):** `"Client Certificate,Smart Card (PIV/CAC),SSH Certificate,Code Signing,N/A"`
- **Key Algorithm (S):** `"RSA-2048,RSA-3072,RSA-4096,ECDSA P-256,ECDSA P-384,N/A"`
- **Certificate Validity (T):** `"≤825 days (internal),≤398 days (public CA),>825 days (non-compliant)"`
- **CRL/OCSP Enabled (U):** `"Yes,No,N/A"`
- **CA Type (V):** `"Internal PKI,Public CA,Both,N/A"`

**Service Account-Specific Dropdowns:**

- **Password Age (S):** `"<90 days,90-180 days,>180 days (non-compliant),Managed Identity (N/A)"`
- **Privileges (T):** `"Standard User,Local Admin,Domain Admin,Database Owner,Root,N/A"`
- **Interactive Login (U):** `"Allowed (non-compliant),Denied (compliant),N/A"`
- **Managed Identity (V):** `"Yes (Azure MSI/AWS IAM),No,N/A"`

**SSO/Federation-Specific Dropdowns:**

- **SSO Protocol (R):** `"SAML 2.0,OAuth 2.0,OIDC,WS-Federation,Legacy (non-compliant)"`
- **IdP Certificate Expiry (T):** `"<90 days (urgent),90-180 days,>180 days,N/A"`
- **Federation Trust Type (U):** `"Internal (same org),External (partner),Public (SaaS)"`
- **Trust Documentation (V):** `"Yes (documented),No,N/A"`

## A.3 Conditional Formatting

**Status Column (Column H):**

- ✅ Compliant: Green fill (RGB: 198, 239, 206)
- ⚠️ Partial: Yellow fill (RGB: 255, 235, 156)
- ❌ Non-Compliant: Red fill (RGB: 255, 199, 206)
- N/A: No special formatting

**Hash/Encryption Status (Column F) - Critical highlighting:**

- "Plaintext (Non-compliant)": Red fill (RGB: 255, 199, 206), bold red text
- "Properly Hashed": Green fill (RGB: 198, 239, 206)
- "Salted": Yellow fill (RGB: 255, 235, 156)

**Password Complexity (Column G):**

- "Weak (<12)": Red fill (RGB: 255, 199, 206)
- "Adequate (12-13)": Yellow fill (RGB: 255, 235, 156)
- "Strong (≥14 chars)": Green fill (RGB: 198, 239, 206)

**Service Account Password Age (Column S in Sheet 4):**

- "<90 days": Green fill
- "90-180 days": Yellow fill
- ">180 days (non-compliant)": Red fill

**IdP Certificate Expiry (Column T in Sheet 5):**

- "<90 days (urgent)": Red fill, bold red text
- "90-180 days": Yellow fill
- ">180 days": Green fill

**Overall Compliance Percentage (Summary Dashboard):**

- ≥90%: Green fill
- 80-89%: Yellow fill
- <80%: Red fill

## A.4 Cell Protection

**Protected Cells (Formula/Static):**

- Column headers
- Instructions text
- Compliance checklist labels
- Status legend
- Summary Dashboard calculations
- Evidence Register ID auto-generation

**Unprotected Cells (User Input):**

- Assessment data entry tables (yellow fill, columns A-Q rows 8-20)
- Additional section-specific columns (R-W)
- Compliance checklist status columns
- Additional Details fields
- Exception/Deviation documentation fields
- Evidence Register descriptions
- Approval Sign-Off fields

**Sheet Protection:**

- Password: [Set during workbook generation]
- Allow: Format cells, Insert rows, Sort, Filter
- Disallow: Delete rows, Modify formulas, Unprotect sheet

## A.5 Summary Dashboard Formulas

**Compliance Percentage by Category:**
```excel
=COUNTIF('1. Password Security'!H:H,"✅ Compliant")/COUNTA('1. Password Security'!H:H)*100
```

**Critical Gaps Count:**
```excel
=COUNTIF('1. Password Security'!H:H,"❌ Non-Compliant")+
 COUNTIF('2. Multi-Factor Authentication'!H:H,"❌ Non-Compliant")+
 COUNTIF('3. Certificate-Based Authentication'!H:H,"❌ Non-Compliant")+
 COUNTIF('4. Service Accounts'!H:H,"❌ Non-Compliant")+
 COUNTIF('5. SSO & Federation'!H:H,"❌ Non-Compliant")
```

**Overall Compliance Rate:**
```excel
=(Total Compliant Items / Total Applicable Items) * 100
```
Where Total Applicable Items excludes N/A items.

**Plaintext Password Detection (Critical Alert):**
```excel
=COUNTIF('1. Password Security'!F:F,"Plaintext (Non-compliant)")
```
If >0: Display critical alert in dashboard

## A.6 Evidence Register Auto-Numbering

**Evidence ID Format:**
```excel
="EV-"&TEXT(ROW()-4,"000")
```

**Date Format:**
```excel
=TEXT(TODAY(),"DD.MM.YYYY")
```

## A.7 Python Script Integration Points

**Workbook Generation Script:** `generate_a824_3_authentication_assessment.py`

**Key Functions:**

- `create_workbook()`: Initialize workbook and sheets
- `setup_styles()`: Define cell styles, fonts, fills
- `get_authentication_columns()`: Return standard column definitions (A-Q)
- `create_assessment_sheet()`: Generic sheet generator with validation
- `create_password_security_sheet()`: Specialized for password assessment (columns R-W)
- `create_mfa_sheet()`: Specialized for MFA assessment (columns R-U)
- `create_certificate_sheet()`: Specialized for certificate assessment (columns R-V)
- `create_service_account_sheet()`: Specialized for service account assessment (columns R-V)
- `create_sso_federation_sheet()`: Specialized for SSO assessment (columns R-V)
- `create_checklist_section()`: Compliance checklist builder
- `create_summary_dashboard()`: Compliance calculations
- `create_evidence_register()`: Evidence tracking
- `create_approval_signoff()`: Approval workflow

**Customization Points (marked with `# CUSTOMIZE:` in script):**

- Sheet names (if organizational naming differs)
- Dropdown options (if additional authentication methods)
- Data validation rules (if custom compliance criteria)
- Conditional formatting thresholds (if different color coding)
- Checklist items (if organization-specific requirements)

**Quality Assurance Script:** `excel_sanity_check_a824_3.py`

- Validates sheet structure matches specification
- Checks data validation rules applied correctly
- Verifies conditional formatting ranges
- Tests formula accuracy
- Reports discrepancies between script and specification

## A.8 Version Control

**Workbook Versioning:**

- Filename format: `ISMS-IMP-A.8.24.3_Authentication_YYYYMMDD.xlsx`
- Version tracking in Instructions & Legend sheet
- Document Control section updated with each revision

**Change Log:**

- v1.0: Initial workbook structure
- v2.0: Added comprehensive User Completion Guide, enhanced hash algorithm guidance, clarified MFA enforcement vs enrollment distinction, added service account lifecycle management

**Backward Compatibility:**

- v2.0 workbooks can be opened in Excel 2016+
- v1.0 workbooks should be migrated to v2.0 for updated guidance
- Migration script available: `normalize_assessment_files_a824.py`

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Document Assembly Instructions

**To create the complete ISMS-IMP-A.8.24.3 v1.0 document:**

1. **Document Control** (from PART I file, lines 1-30)
2. **PART I: USER COMPLETION GUIDE** (from PART I file, lines 31-~440)
3. **PART II: TECHNICAL SPECIFICATION - File 1** (this file, all content)
4. **PART II: TECHNICAL SPECIFICATION - File 2** (next file, all content)

**Final Document Structure:**
```
ISMS-IMP-A.8.24.3 - Authentication Assessment v1.0

├── Document Control (Metadata, Version History)
│
├── PART I: USER COMPLETION GUIDE (~440 lines)
│   ├── 1. Assessment Overview
│   ├── 2. Prerequisites
│   ├── 3. Assessment Workflow
│   ├── 4. Question-by-Question Guidance (Sections 1-2 detailed, 3-5 outlined)
│   ├── 5. Evidence Collection
│   ├── 6. Common Pitfalls (10 mistakes)
│   ├── 7. Quality Checklist (50+ items)
│   └── 8. Review & Approval
│
└── PART II: TECHNICAL SPECIFICATION (~750 lines)
    ├── Instructions
    ├── Common Column Structure
    ├── 1. Password Security (columns A-W, 23 total)
    ├── 2. Multi-Factor Authentication (columns A-U, 21 total)
    ├── 3. Certificate-Based Authentication (columns A-V, 22 total)
    ├── 4. Service Accounts (columns A-V, 22 total)
    ├── 5. SSO & Federation (columns A-V, 22 total)
    ├── 6. Overall Summary
    ├── 7. Evidence Register
    ├── 8. Approval and Sign-Off
    └── Appendix: Technical Notes for Developers
```

**Quality Checks Before Finalizing:**

- [ ] All merge instructions removed
- [ ] Document Control version shows 2.0
- [ ] Version History documents v1.0 → v2.0 changes
- [ ] All dates in DD.MM.YYYY format
- [ ] Cross-references accurate (section numbers, policy references)
- [ ] No placeholder text remains
- [ ] Technical appendix matches Python script version
- [ ] Hash algorithm guidance emphasizes bcrypt/Argon2/PBKDF2/scrypt

---

**END OF SPECIFICATION**

---

*"No, it is a very interesting number; it is the smallest number expressible as the sum of two cubes in two different ways."*
— Srinivasa Ramanujan, on 1729

<!-- QA_VERIFIED: 2026-02-06 -->
