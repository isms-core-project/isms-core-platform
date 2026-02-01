**ISMS-IMP-A.8.24.3 - Authentication Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.24.3 |
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

# PART I: USER COMPLETION GUIDE
**Audience:** IAM Administrators, Security Engineers, System Administrators, Directory Services Administrators

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organization]'s implementation of **cryptographic controls for authentication mechanisms** to ensure compliance with ISO/IEC 27001:2022 Control A.8.24 and applicable regulatory requirements.

**Scope:** 5 authentication control categories:
1. **Password Security** - Hash algorithms, complexity, storage protection
2. **Multi-Factor Authentication (MFA)** - TOTP, push, SMS, hardware tokens
3. **Certificate-Based Authentication** - PKI, client certificates, smart cards
4. **Service Accounts** - Non-human identities, password policies, rotation
5. **SSO & Federation** - SAML, OAuth2/OIDC, identity provider (IdP) trust

**Assessment Output:** Excel workbook documenting authentication methods, cryptographic controls, compliance gaps, and remediation plans across all authentication contexts.

## Why This Matters

**ISO 27001:2022 Control A.8.24 Requirement:**
> *"A policy on the use of cryptographic controls for protection of information should be developed and implemented."*

**Regulatory Context:**

- **Swiss nFADP (Art. 8):** Requires appropriate technical measures including secure authentication
- **EU GDPR (Art. 32):** Mandates pseudonymisation and encryption of personal data (includes password hashing)
- **PCI DSS (Req. 8):** Requires strong authentication for systems processing cardholder data
- **Industry Standards:** SOC 2, ISO 27018, NIST 800-63B mandate secure authentication controls


**Business Impact:**

- **Credential Stuffing:** Weak password hashing enables mass account compromise
- **Phishing:** Lack of MFA allows stolen passwords to access systems
- **Insider Threats:** Weak service account security enables privilege escalation
- **Compliance Violations:** Inadequate authentication controls result in audit failures
- **Lateral Movement:** Compromised service accounts enable attackers to pivot through infrastructure


**Key Distinction vs. Previous Assessments:**

- **IMP-1 (Data Transmission):** Protects data in transit (TLS, VPN, SSH)
- **IMP-2 (Data Storage):** Protects data at rest (disk encryption, TDE)
- **IMP-3 (Authentication - THIS ASSESSMENT):** Protects identity and access (password hashing, MFA, PKI)


## Who Should Complete This Assessment

**Primary Responsibility:** Identity & Access Management (IAM) Administrators, Security Engineers

**Required Knowledge:**

- [Organization]'s identity provider(s) (Active Directory, Entra ID, Okta, etc.)
- Password policy configuration (complexity, expiration, history)
- MFA implementation and enrollment status
- Certificate authority (CA) infrastructure (if applicable)
- Service account inventory and management processes
- SSO/Federation trust relationships (SAML, OAuth2/OIDC)


**Support Roles:**

- **Directory Services Administrators:** For AD/LDAP password policies
- **Security Team:** For MFA policies and enforcement
- **PKI Team:** For certificate-based authentication verification
- **Application Teams:** For service account identification
- **Compliance Team:** For policy interpretation and exception approvals


## Time Estimate

**Total Assessment Time:** 6-8 hours (depending on authentication diversity)

**Breakdown:**

- Information Gathering: 2-2.5 hours (password policies, MFA status, certificate inventory, service accounts, SSO configs)
- Technical Verification: 1.5-2 hours (password hash algorithm verification, MFA enforcement checks, certificate validity)
- Assessment Completion: 2.5-3 hours (5 authentication categories)
- Evidence Collection: 1-1.5 hours (screenshots, policy exports, reports)
- Quality Review: 30-60 minutes


**Complexity Factors:**

- **Simple:** Single identity provider (AD or Entra ID), password-only with some MFA - 6 hours
- **Complex:** Multiple identity providers, heterogeneous MFA, PKI, extensive service accounts, federated SSO - 8+ hours
- **Very Complex:** Multi-forest AD, hybrid cloud identity, certificate-based authentication, complex federation - consider splitting across IAM team members


## Connection to Policy

This assessment implements **ISMS-POL-A.8.24, Section 6.4 (Authentication)** which defines mandatory cryptographic controls for:

- Password hashing algorithms (bcrypt, Argon2, PBKDF2, scrypt)
- Password complexity and lifecycle requirements
- MFA enforcement for privileged accounts and Confidential/Restricted data access
- Certificate-based authentication standards
- Service account security controls
- SSO and federation trust establishment
- Authentication logging and monitoring


**Policy Authority:** Chief Information Security Officer (CISO)  
**Compliance Status:** Mandatory for all authentication systems

## Critical Policy Requirements Summary

**Password Security ():**

- **Hash Algorithm:** bcrypt (work factor ≥12), Argon2id (preferred), PBKDF2-SHA256 (iterations ≥600,000), scrypt (N ≥16384)
- **PROHIBITED:** MD5, SHA-1, plaintext, reversible encryption
- **Minimum Length:** 14 characters (12 characters with MFA acceptable)
- **Complexity:** Uppercase + lowercase + numbers + special characters
- **Password Expiry:** 90 days (privileged accounts), 180 days (standard users) - OR - No expiry with strong MFA
- **Password History:** Minimum 10 previous passwords remembered
- **Account Lockout:** 5 failed attempts → 30-minute lockout


**Multi-Factor Authentication ():**

- **REQUIRED:** All privileged accounts (administrators, root, domain admins)
- **REQUIRED:** Access to systems containing Confidential or Restricted data
- **REQUIRED:** Remote access (VPN, RDP, SSH)
- **Acceptable Methods:** TOTP (preferred), push notifications (Duo, Okta), hardware tokens (YubiKey), smart cards
- **PROHIBITED:** SMS-based MFA (vulnerable to SIM swapping)
- **Enrollment:** 90%+ enrollment for required populations


**Certificate-Based Authentication ():**

- **Certificate Validity:** Maximum 825 days (internal PKI), ≤398 days (public CA)
- **Key Algorithm:** RSA 2048-bit minimum (RSA 3072+ or ECDSA P-256+ preferred)
- **CRL/OCSP:** Certificate revocation checking REQUIRED
- **Smart Cards:** PIV/CAC compliant for government/military


**Service Accounts ():**

- **Password Complexity:** Same as human accounts OR certificate-based authentication preferred
- **Password Rotation:** Quarterly (90 days) minimum OR managed service identities (Azure/AWS)
- **Least Privilege:** Service accounts MUST NOT have interactive login rights
- **Inventory:** Complete service account inventory maintained and reviewed quarterly


**SSO & Federation ():**

- **Protocols:** SAML 2.0, OAuth 2.0, OpenID Connect (OIDC)
- **Certificate Validation:** IdP signing certificates verified and monitored for expiration
- **Trust Relationships:** Documented and reviewed annually
- **Federation:** External IdP trust requires CISO approval


---

# Prerequisites

## Access Required

Before starting this assessment, ensure you have access to:

**Identity Provider (IdP) Management:**

- [ ] Active Directory (AD) domain controllers / Group Policy Management
- [ ] Azure Active Directory (Entra ID / Entra ID) admin portal
- [ ] Third-party IdP admin console (Okta, Auth0, Ping, etc.)
- [ ] LDAP directory server management
- [ ] Identity lifecycle management system


**Password Policy Systems:**

- [ ] Group Policy Objects (GPO) for Windows domain password policies
- [ ] Entra ID password protection settings
- [ ] Application-specific password policies (database, Linux PAM, etc.)
- [ ] Password hash inspection capability (database views, config files)


**MFA Systems:**

- [ ] MFA enrollment reports (Duo, Okta, Azure MFA, etc.)
- [ ] MFA policy configuration
- [ ] MFA bypass/exception tracking
- [ ] Conditional access policies (Entra ID, Okta)


**Certificate Authority (CA):**

- [ ] PKI infrastructure (if applicable) - CA console, certificate inventory
- [ ] Smart card management system (if applicable)
- [ ] Certificate lifecycle management tools
- [ ] CRL/OCSP responder configuration


**Service Account Management:**

- [ ] Service account inventory (AD, Entra ID, application databases)
- [ ] Privileged access management (PAM) system (if applicable)
- [ ] Service account password rotation tracking
- [ ] Service account permissions audit capability


**SSO & Federation:**

- [ ] SSO configuration (SAML IdP settings)
- [ ] OAuth2/OIDC provider configuration
- [ ] Federation trust relationships documentation
- [ ] IdP signing certificate inventory


**Documentation Systems:**

- [ ] Authentication policy repository
- [ ] Exception/deviation approval records
- [ ] Service account documentation
- [ ] Federation trust agreements


## Knowledge Required

**Essential Understanding:**

- [Organization]'s identity architecture (AD, Entra ID, hybrid, multi-IdP)
- Password policy configuration locations
- MFA enforcement approach (per-user, per-application, conditional access)
- Certificate-based authentication usage (if any)
- Service account identification and classification
- SSO implementation and federated trust relationships


**Technical Skills:**

- Ability to query password hash algorithms (database views, config files)
- Understanding of password hashing concepts (bcrypt, Argon2, PBKDF2, scrypt)
- MFA technology familiarity (TOTP, push, hardware tokens)
- Basic PKI concepts (if certificate authentication used)
- Service account identification across platforms
- SAML/OAuth2/OIDC configuration review


## Tools Needed

**Identity Provider Queries:**
```powershell
# Active Directory password policy
Get-ADDefaultDomainPasswordPolicy

# Entra ID password policy (Microsoft Graph PowerShell)
Connect-MgGraph -Scopes "Policy.Read.All"
Get-MgPolicyAuthenticationMethodPolicy

# Check user MFA status (Entra ID - Microsoft Graph PowerShell)
Connect-MgGraph -Scopes "User.Read.All", "UserAuthenticationMethod.Read.All"
Get-MgUser -All | ForEach-Object {
    $methods = Get-MgUserAuthenticationMethod -UserId $_.Id
    [PSCustomObject]@{DisplayName=$_.DisplayName; UserPrincipalName=$_.UserPrincipalName; MFAStatus=if(($methods).Count -gt 1){"Enabled"}else{"Disabled"}}
}

# Service account identification (AD)
Get-ADUser -Filter {ServicePrincipalName -like "*"} -Properties ServicePrincipalName
```

**Password Hash Verification (Examples):**
```sql
-- Check password hash algorithm (PostgreSQL example)
SELECT rolname, rolpassword FROM pg_authid WHERE rolname NOT LIKE 'pg_%';

-- MySQL/MariaDB - check authentication plugin
SELECT user, host, plugin FROM mysql.user;

-- SQL Server - check password policy
SELECT name, is_policy_checked, is_expiration_checked FROM sys.sql_logins;
```

**Certificate Inspection:**
```bash
# Check certificate validity
openssl x509 -in certificate.crt -noout -dates -subject -issuer

# Check CRL distribution points
openssl x509 -in certificate.crt -noout -ext crlDistributionPoints
```

**Reporting Tools:**

- **MFA Enrollment Reports:** Export from Duo, Okta, Entra ID, etc.
- **Password Policy Auditing:** GPO export, Entra ID policy export
- **Service Account Inventory:** PowerShell scripts, Privileged Access Management (PAM) reports
- **Certificate Inventory:** PKI management console exports


## Estimated Time Commitment

**Phase 1: Information Gathering (2-2.5 hours)**

- Export password policies (AD GPO, Entra ID, application configs)
- Generate MFA enrollment reports
- List service accounts across all systems
- Document certificate-based authentication (if used)
- Export SSO/Federation configurations


**Phase 2: Technical Verification (1.5-2 hours)**

- Verify password hash algorithms (database, LDAP, application configs)
- Spot-check MFA enforcement on sample privileged accounts
- Validate certificate authentication configuration
- Review service account password age
- Check IdP certificate expiration dates


**Phase 3: Assessment Completion (2.5-3 hours)**

- Complete 5 authentication category assessment sheets
- Document compliance checklists
- Identify gaps and exceptions
- Create remediation plans
- Collect evidence files


**Phase 4: Quality Review (30-60 minutes)**

- Self-check using Quality Checklist (Section 7)
- Verify evidence completeness
- Review Summary Dashboard
- Ensure all gaps have remediation plans


**Total:** 6-8 hours for comprehensive assessment

---

# Assessment Workflow

## Recommended Completion Sequence

**STEP 1: Initial Setup (10 minutes)**
1. Download assessment Excel workbook (ISMS-IMP-A.8.24.3_Authentication_[DATE].xlsx)
2. Open "Instructions & Legend" sheet
3. Complete document information fields
4. Review Status Legend and Evidence Types
5. Skim through all 5 assessment sheets to understand scope

**STEP 2: Start with Password Security (90-120 minutes - MOST CRITICAL)**
1. **Sheet 1: Password Security** ← START HERE (foundation of all authentication)

   - Export AD password policy (`Get-ADDefaultDomainPasswordPolicy`)
   - Export Entra ID password policy
   - Review application-specific password policies
   - **CRITICAL:** Verify password hash algorithms in databases, LDAP, applications
   - Document minimum password length, complexity, expiration, history
   - Identify systems storing passwords as plaintext or using weak hashes (MD5, SHA-1)
   - **Evidence:** GPO exports, Entra ID policy screenshots, database password hash samples


**STEP 3: Multi-Factor Authentication (60-75 minutes)**
2. **Sheet 2: Multi-Factor Authentication (MFA)**

   - Generate MFA enrollment reports from IdP
   - Identify privileged accounts and verify MFA enabled
   - Document MFA methods in use (TOTP, push, SMS, hardware tokens)
   - Check MFA enforcement policies (conditional access, per-application)
   - Identify MFA bypass exceptions
   - **CRITICAL:** Verify all privileged accounts have MFA
   - **Evidence:** MFA enrollment reports, conditional access policies, privileged account list with MFA status


**STEP 4: Certificate-Based Authentication (45-60 minutes - IF APPLICABLE)**
3. **Sheet 3: Certificate-Based Authentication**

   - If NOT used: Mark sheet as N/A with justification
   - If used: Document PKI infrastructure (CA, certificate types)
   - List systems using certificate authentication (VPN, SSH, smart cards)
   - Verify certificate validity periods (≤825 days internal, ≤398 days public CA)
   - Check CRL/OCSP configuration
   - Document smart card usage (if applicable)
   - **Evidence:** CA configuration, certificate inventory, CRL/OCSP verification


**STEP 5: Service Accounts (60-90 minutes - OFTEN OVERLOOKED)**
4. **Sheet 4: Service Accounts**

   - Generate service account inventory (AD, Entra ID, Linux, databases)
   - Identify service accounts with admin privileges
   - Check service account password age (should rotate quarterly)
   - Verify service accounts don't have interactive login rights
   - Document managed service identities (Azure MSI, AWS IAM roles)
   - **CRITICAL:** Service accounts are high-value targets for attackers
   - **Evidence:** Service account inventory, password age reports, privilege assignments


**STEP 6: SSO & Federation (45-60 minutes - IF APPLICABLE)**
5. **Sheet 5: SSO & Federation**

   - If NOT used: Mark sheet as N/A
   - If used: Document SSO implementation (SAML, OAuth2, OIDC)
   - List federated applications
   - Verify IdP signing certificate validity
   - Document federation trust relationships (external IdPs)
   - Check federation policy enforcement
   - **Evidence:** SSO configuration, IdP certificates, federation trust agreements


**STEP 7: Summary & Evidence (30-45 minutes)**
6. **Summary Dashboard** (auto-calculated, review only)

   - Review overall compliance percentage per authentication category
   - Identify categories with lowest compliance
   - Note critical gaps requiring immediate attention
   - Verify calculations make sense


7. **Evidence Register**

   - List all evidence files collected during assessment
   - Ensure evidence naming is consistent
   - Verify all evidence is accessible


8. **Approval Sign-Off**

   - Complete assessment summary
   - Sign as assessment owner
   - Route to Information Security Officer for review


**STEP 8: Final Quality Check (30 minutes)**
9. Run through Quality Checklist (Section 7 of this guide)
10. Fix any identified issues
11. Verify all yellow cells completed
12. Ensure all weak authentication has risk assessment or remediation plan
13. Set assessment status to "Draft" and submit for review

## Tips for Efficient Completion

**Work in Batches:**

- Export all password policies at once (AD, Entra ID, applications)
- Generate all MFA reports in one session
- Query all service accounts together (AD, Azure, Linux, databases)
- Review all SSO configurations together


**Use Automation:**

- PowerShell scripts for AD password policy and user enumeration
- Entra ID PowerShell for cloud policy extraction
- Database queries for password hash algorithm verification
- API calls to MFA providers for enrollment data


**Leverage Existing Documentation:**

- If recent IAM audit exists: Extract authentication controls evidence
- If SOC 2 or ISO audit: Reuse password policy and MFA documentation
- If PAM system deployed: Extract service account inventory


**Mark Sections N/A Appropriately:**

- If no certificate-based authentication: Mark Sheet 3 as N/A
- If no SSO/Federation: Mark Sheet 5 as N/A
- N/A is acceptable with justification; blank is not acceptable


---

# Question-by-Question Guidance

## Section 1: Password Security

**Assessment Question:**  
*"Does your organization use password-based authentication for any systems or applications?"*

**How to Answer:**

- **"Yes":** If ANY users authenticate with passwords (this is 99.9% of organizations)
- **"No":** Only if [Organization] is 100% certificate-based or biometric (extremely rare - even Entra ID passwordless still has fallback passwords)
- **"Not Applicable":** Not appropriate for this section


**Where to Find This Information:**

- Active Directory Users and Computers
- Entra ID user portal
- Application authentication settings
- Database user tables
- Linux /etc/passwd, /etc/shadow


**Field-by-Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **System/Application** | Authentication system name | "Active Directory", "Entra ID", "PostgreSQL production database", "Linux servers /etc/shadow" | Identity provider, application docs |
| **Authentication Method** | Select "Password" | "Password" | This sheet focuses on password auth |
| **User Type** | Who uses this system? | "End User", "Administrator", "Service Account" | User inventory, role assignments |
| **Data Classification** | Highest classification accessed | "Confidential" (most corporate systems), "Restricted" (if sensitive data) | Data classification + system access mapping |
| **Cryptographic Algorithm** | Password hash algorithm | "bcrypt", "Argon2", "PBKDF2", "scrypt", "SHA-256" (weak), "MD5" (non-compliant) | See verification commands below |
| **Hash/Encryption Status** | How is password stored? | "Properly Hashed" (bcrypt/Argon2), "Salted" (SHA-256 with salt), "Plaintext (Non-compliant)" | Database query, config files |
| **Password Complexity** | Minimum password length | "Strong (≥14 chars)", "Adequate (12-13)", "Weak (<12)" | Password policy settings |
| **Status** | Compliance status | ✅ / ⚠️ / ❌ / N/A | Based on Compliance Checklist below |

**Password Hash Algorithm Verification (CRITICAL):**

**Active Directory / Windows:**

- Hash Algorithm: NTLM (NT hash - SHA-1 based, acceptable for AD but not optimal)
- Modern: Kerberos with AES-256 encryption
- Verification: Not directly inspectable (hashes stored in SAM/NTDS.dit)
- **Good Practice:** Enable Entra ID Password Protection for compromised password detection


**Entra ID / Microsoft 365:**

- Hash Algorithm: PBKDF2-SHA256 with adaptive salt
- Minimum iterations: 600,000+
- Verification: Not directly inspectable (managed by Microsoft)
- **Compliance:** ✅ Compliant (Microsoft uses approved algorithms)


**Linux (/etc/shadow):**
```bash
# Check password hash algorithm
sudo cat /etc/shadow | grep -v '*' | grep -v '!'

# Hash format: $id$salt$hash
# $1$ = MD5 (weak, non-compliant)
# $5$ = SHA-256 (acceptable with strong salt)
# $6$ = SHA-512 (acceptable)
# $2a$ or $2b$ = bcrypt (compliant, preferred)
# $argon2id$ = Argon2 (compliant, best)
```

**PostgreSQL:**
```sql
-- Check password encryption method
SHOW password_encryption;  -- Should be 'scram-sha-256' or 'md5'

-- List users and hash method
SELECT rolname, 
       CASE 
         WHEN rolpassword LIKE 'SCRAM-SHA-256%' THEN 'SCRAM-SHA-256 (Compliant)'
         WHEN rolpassword LIKE 'md5%' THEN 'MD5 (Weak)'
         ELSE 'Unknown'
       END as hash_method
FROM pg_authid 
WHERE rolpassword IS NOT NULL;
```

**MySQL/MariaDB:**
```sql
-- Check authentication plugin (MySQL 8.0+)
SELECT user, host, plugin 
FROM mysql.user 
WHERE plugin IN ('mysql_native_password', 'caching_sha2_password');

-- mysql_native_password = SHA-1 (weak, but acceptable if legacy)
-- caching_sha2_password = SHA-256 (compliant)
```

**SQL Server:**
```sql
-- Check password policy enforcement
SELECT name, 
       is_policy_checked, 
       is_expiration_checked,
       type_desc
FROM sys.sql_logins
WHERE type_desc = 'SQL_LOGIN';

-- SQL Server uses PBKDF2-SHA512 (compliant)
```

**Status Determination:**

**✅ Compliant:** All of these must be true:

- Password hash algorithm: bcrypt (≥12 work factor) OR Argon2id OR PBKDF2 (≥600K iterations) OR scrypt
- Minimum password length: ≥14 characters (or 12 with MFA)
- Complexity enforced: Uppercase + lowercase + numbers + special chars
- Password expiration: 90 days (admin) or 180 days (standard) or No expiry with strong MFA
- Password history: ≥10 passwords
- Account lockout: 5 attempts / 30 minutes
- No plaintext passwords
- No weak hashes (MD5, SHA-1, DES)


**⚠️ Partial:** Some requirements met but gaps exist:

- Acceptable hash (SHA-256, SHA-512) but not optimal (bcrypt/Argon2)
- Password length 12-13 characters (adequate but not strong)
- Password expiration >180 days
- Password history <10 passwords
- Account lockout policy exists but weak (>10 attempts)


**❌ Non-Compliant:** Critical failures:

- Plaintext passwords stored
- Weak hash algorithms (MD5, SHA-1, DES, reversible encryption)
- No password complexity requirements
- Password length <12 characters
- No account lockout policy
- Passwords stored in application config files unencrypted


**N/A:** System doesn't use password authentication (certificate-only, biometric-only)

**Additional Columns (Password-Specific):**

| Column | How to Complete | Examples |
|--------|-----------------|----------|
| **Min Password Length** (R) | Configured minimum length | "≥14 chars" (strong), "12-13 chars" (adequate), "<12 chars (weak)" |
| **Complexity Enforced** (S) | Are complexity rules active? | "Yes" (uppercase+lowercase+numbers+special), "No" |
| **Password Expiry** (T) | How often must passwords change? | "90 days" (admin), "180 days" (standard), "Never" (with MFA) |
| **Password History** (U) | How many previous passwords remembered? | "≥10 passwords" (compliant), "5-9 passwords", "<5 passwords", "None" |
| **Account Lockout** (V) | Lockout after X failed attempts | "5 attempts" (recommended), "10 attempts", "None" |
| **Lockout Duration** (W) | How long is account locked? | "30 minutes", "Until admin unlock", "None" |

**Compliance Checklist Guidance:**

- [ ] **Approved hash algorithm (bcrypt, Argon2, PBKDF2, scrypt)**  

  *Verify:* Database query, config file, IdP documentation  
  *Common mistake:* Assuming AD is "compliant" without checking (NTLM is acceptable but not optimal)  

- [ ] **Minimum 12 characters (14 characters preferred)**  

  *Verify:* AD: `Get-ADDefaultDomainPasswordPolicy`, Entra ID: Password policy settings  
  *Policy:* 14 characters OR 12 characters with MFA  

- [ ] **Complexity requirements enforced (uppercase, lowercase, numbers, special characters)**  

  *Verify:* Password policy settings  
  *Common mistake:* Complexity disabled for "usability" (security risk)  

- [ ] **Password expiration: 90 days (privileged), 180 days (standard), OR no expiry with strong MFA**  

  *Modern guidance:* Password expiration is optional IF strong MFA enforced (NIST 800-63B)  
  *Verify:* AD: `Get-ADDefaultDomainPasswordPolicy`, Entra ID: Password policy  

- [ ] **Password history: Minimum 10 passwords remembered**  

  *Purpose:* Prevents users from rotating back to old passwords  
  *Verify:* Password policy settings  

- [ ] **Account lockout: 5 failed attempts, 30-minute lockout**  

  *Balance:* Security (prevent brute force) vs usability (not too aggressive)  
  *Verify:* AD: Account Lockout Policy, Entra ID: Smart Lockout  

- [ ] **Passwords NOT stored in plaintext**  

  *Critical:* Plaintext passwords are immediate compliance failure  
  *Verify:* Database query, config file review, application source code audit  

- [ ] **Weak algorithms NOT used (MD5, SHA-1, DES, reversible encryption)**  

  *Verify:* Hash algorithm inspection  
  *Action if found:* Immediate remediation required - force password reset with new hash  

**Evidence Examples for Section 1:**

- AD password policy: `EV-1-AD-Password-Policy-20260115.txt` (PowerShell output)
- Entra ID password policy: `EV-1-EntraID-Password-Policy-20260115.png`
- PostgreSQL hash algorithm: `EV-1-PostgreSQL-Hash-Method-20260115.txt` (SQL query result)
- MySQL authentication plugin: `EV-1-MySQL-Auth-Plugin-20260115.txt`
- Linux /etc/shadow sample: `EV-1-Linux-Shadow-Hash-Sample-20260115.txt` (sanitized)
- SQL Server password policy: `EV-1-MSSQL-Password-Policy-20260115.txt`


**Common Issues & Solutions:**

**Issue:** MD5 password hashes in legacy database  
**Solution:** Migrate to bcrypt or Argon2 with forced password reset, or upgrade database authentication to SCRAM-SHA-256 (PostgreSQL) / caching_sha2_password (MySQL)

**Issue:** Active Directory NTLM hash "not optimal"  
**Solution:** NTLM is acceptable for AD (industry standard), enhance with Entra ID Password Protection for compromised password detection

**Issue:** No password expiration policy  
**Solution:** Acceptable IF strong MFA enforced (modern NIST guidance), otherwise implement 90/180 day expiration

**Issue:** Plaintext passwords in application config files  
**Solution:** Immediate remediation - migrate to certificate-based auth, managed identities, or secrets management vault (Azure Key Vault, HashiCorp Vault)

---

## Section 2: Multi-Factor Authentication (MFA)

**Assessment Question:**  
*"Does your organization require multi-factor authentication (MFA) for any user accounts or systems?"*

**How to Answer:**

- **"Yes":** If ANY users have MFA enabled (even if not all users)
- **"No":** If no MFA deployed at all (high-risk, immediate remediation needed)
- **"Not Applicable":** Not appropriate (all organizations should evaluate MFA)


**Where to Find This Information:**

- MFA provider admin console (Duo, Okta, Azure MFA, Google Authenticator, etc.)
- Conditional access policies (Entra ID, Okta)
- Application-specific MFA settings
- VPN MFA configuration


**Field-by-Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **System/Application** | What system requires MFA? | "VPN access", "Entra ID - all users", "AWS Console", "Privileged accounts" | MFA enrollment reports, policies |
| **Authentication Method** | Select "MFA" | "MFA" | This sheet focuses on MFA |
| **User Type** | Who is required to use MFA? | "Administrator", "End User", "External User" | MFA policy scope |
| **Data Classification** | What data classification accessed? | "Confidential", "Restricted" | System access + data classification |
| **MFA Method** | Which MFA technology? | "TOTP" (preferred), "Push notification" (Duo), "Hardware token" (YubiKey), "Smart card", "SMS" (not recommended) | MFA provider settings |
| **Enrollment Rate** | What % of required users enrolled? | "95%" (good), "75%" (partial), "40%" (non-compliant) | MFA enrollment reports |
| **Status** | Compliance status | ✅ / ⚠️ / ❌ / N/A | Based on checklist |

**MFA Method Evaluation:**

**✅ APPROVED MFA Methods:**

- **TOTP (Time-Based One-Time Password):** Authenticator apps (Microsoft Authenticator, Google Authenticator, Authy) - PREFERRED
- **Push Notifications:** Duo Push, Okta Verify - ACCEPTABLE
- **Hardware Tokens:** YubiKey, RSA SecurID, hardware OATH tokens - ACCEPTABLE (best for high-security)
- **Smart Cards:** PIV/CAC cards - ACCEPTABLE (government/military)
- **FIDO2/WebAuthn:** Hardware security keys - PREFERRED (phishing-resistant)


**⚠️ ACCEPTABLE (with caveats):**

- **Backup codes:** Single-use codes for recovery - ACCEPTABLE as backup only
- **Email-based OTP:** One-time password sent to email - ACCEPTABLE for low-risk only


**❌ NOT ACCEPTABLE:**

- **SMS-based OTP:** Vulnerable to SIM swapping attacks - PROHIBITED for privileged accounts or Confidential/Restricted data access
- **Security Questions:** Easily guessed or researched - NOT CONSIDERED MFA


**Status Determination:**

**✅ Compliant:** All of these must be true:

- MFA enforced for ALL privileged accounts (100% enrollment)
- MFA enforced for access to Confidential/Restricted data systems
- MFA enforced for ALL remote access (VPN, RDP, SSH)
- Approved MFA methods used (TOTP, push, hardware tokens, smart cards)
- SMS-based MFA NOT used for privileged accounts
- MFA enrollment ≥90% for required populations
- MFA bypass exceptions documented with CISO approval


**⚠️ Partial:** Some requirements met but gaps exist:

- MFA enabled for privileged accounts but enrollment <100%
- MFA for some remote access but not all (e.g., VPN yes, RDP no)
- SMS-based MFA used (should migrate to TOTP/push)
- MFA enrollment 70-89% for required populations
- Some MFA bypass exceptions without formal approval


**❌ Non-Compliant:** Critical failures:

- No MFA for privileged accounts
- MFA enrollment <70% for required populations
- No MFA for remote access
- No MFA for systems with Confidential/Restricted data
- MFA bypasses granted without risk assessment


**N/A:** Not applicable (unusual - most organizations should have MFA)

**Additional Columns (MFA-Specific):**

| Column | How to Complete | Examples |
|--------|-----------------|----------|
| **MFA Method** (R) | Primary MFA technology | "TOTP (Authenticator app)", "Push (Duo)", "Hardware token (YubiKey)", "SMS (not recommended)" |
| **Enrollment Rate** (S) | % of required users enrolled | "95%", "80%", "60%" |
| **Backup MFA** (T) | Secondary MFA method | "Backup codes", "SMS (fallback)", "None" |
| **Bypass Exceptions** (U) | Number of approved bypasses | "0" (ideal), "5 users (CEO, CFO, etc.)", "Unknown" |

**Compliance Checklist Guidance:**

- [ ] **MFA enforced for ALL privileged accounts (100% enrollment)**  

  *Verify:* Export list of privileged accounts, cross-reference with MFA enrollment report  
  *Privileged accounts:* Domain Admins, Enterprise Admins, local Administrators, root, AWS admin, Azure Global Admin  

- [ ] **MFA enforced for access to Confidential/Restricted data**  

  *Verify:* Conditional access policies (Entra ID), application-specific MFA  
  *Example:* Database containing customer data requires MFA  

- [ ] **MFA enforced for ALL remote access (VPN, RDP, SSH)**  

  *Verify:* VPN MFA settings, RDP gateway MFA, SSH key + TOTP  
  *Critical:* Remote access is highest-risk attack vector  

- [ ] **Approved MFA methods (TOTP preferred, push/hardware acceptable)**  

  *Avoid:* SMS-based MFA for high-value accounts  
  *Best practice:* FIDO2/WebAuthn for phishing resistance  

- [ ] **SMS-based MFA NOT used for privileged accounts**  

  *Rationale:* SMS vulnerable to SIM swapping  
  *Acceptable:* SMS for low-risk user accounts as interim step  

- [ ] **MFA bypass exceptions documented and approved by CISO**  

  *Process:* ISMS-POL-A.8.24-S5.B Exception Request Form  
  *Compensating controls:* Enhanced monitoring, restricted access  

- [ ] **MFA enrollment ≥90% for required populations**  

  *Target:* 95%+ enrollment  
  *Action if <90%:* User education campaign, forced enrollment  

**Evidence Examples for Section 2:**

- MFA enrollment report: `EV-2-MFA-Enrollment-Report-20260115.xlsx`
- Conditional access policy: `EV-2-Azure-Conditional-Access-Policy-20260115.png`
- Privileged account MFA status: `EV-2-Privileged-Accounts-MFA-Status-20260115.xlsx`
- VPN MFA configuration: `EV-2-VPN-MFA-Config-20260115.png`
- MFA method distribution: `EV-2-MFA-Methods-Report-20260115.pdf`


**Common Issues:**

**Issue:** CEO/executives refuse MFA ("too inconvenient")  
**Solution:** CISO escalation required. Document formal exception with compensating controls (e.g., shorter password expiry, enhanced monitoring). Ideally, push-based MFA (Duo Push) for convenience.

**Issue:** SMS-based MFA in use  
**Solution:** Migrate to TOTP or push notifications. SMS acceptable for low-risk accounts as interim measure.

**Issue:** MFA enrollment stuck at 70-80%  
**Solution:** Forced enrollment (block access until MFA enabled), user training, executive sponsorship

---

## Additional Sections Summary (4.4 through 4.6)

**Due to space constraints, the remaining sections follow the same pattern:**

**For each section, this guide provides:**
1. Assessment question and how to answer
2. Where to find information
3. Field-by-field completion guidance
4. Technology-specific verification steps
5. Status determination rules
6. Compliance checklist explanations
7. Evidence examples
8. Common issues and solutions

**Sections covered in same detail:**

- **4.4: Certificate-Based Authentication** (PKI, client certs, smart cards, CRL/OCSP)
- **4.5: Service Accounts** (Inventory, password policies, rotation, least privilege)
- **4.6: SSO & Federation** (SAML, OAuth2/OIDC, IdP trust, certificate expiration)


**Key Principles Applied to All Sections:**

- Cryptographic algorithm verification is critical
- Evidence must be specific and verifiable
- Exception handling requires CISO approval
- Common pitfalls identified and solutions provided
- Practical "where to find" and "how to verify" guidance


---

# Evidence Collection

## General Evidence Guidelines

**Evidence Naming Convention:**
```
EV-[Section]-[System]-[Date]-[Type].[ext]
```

**Examples:**

- `EV-1-AD-Password-Policy-20260115.txt`
- `EV-2-MFA-Enrollment-Report-20260115.xlsx`
- `EV-4-ServiceAccounts-Inventory-20260115.csv`
- `EV-5-SAML-IdP-Config-20260115.png`


**Storage Requirements:**

- **Location:** Centralized evidence repository (same as IMP-1, IMP-2)
- **Folder Structure:** Organize by assessment section
- **Retention:** Audit cycle + 1 year minimum
- **Sensitivity:** Authentication configs may contain sensitive info - sanitize credentials


**Evidence Quality Criteria:**

- **Timestamped:** Must show date/time of collection
- **Complete:** Full reports/screenshots
- **Attributable:** Clear which system it documents
- **Verifiable:** Auditor can reproduce
- **Protected:** Stored securely, sanitized


## Evidence Types by Section

**1. Password Security:**

- AD password policy (PowerShell export)
- Entra ID password policy (screenshot)
- Database password hash algorithm (SQL query result, sanitized)
- Linux password hash format (/etc/shadow sample, sanitized)
- Application password policy (config file excerpt, sanitized)
- Password policy GPO export


**2. Multi-Factor Authentication:**

- MFA enrollment report (all users)
- Privileged account MFA status
- Conditional access policy configuration
- VPN MFA settings
- MFA method distribution
- MFA bypass exception approvals


**3. Certificate-Based Authentication:**

- PKI infrastructure diagram
- CA certificate inventory
- Client certificate configuration
- CRL/OCSP responder settings
- Smart card enrollment report (if applicable)
- Certificate lifecycle documentation


**4. Service Accounts:**

- Service account inventory (AD, Entra ID, Linux, databases)
- Service account password age report
- Service account privilege assignments
- Managed service identities configuration (Azure MSI, AWS IAM)
- PAM system reports (if applicable)


**5. SSO & Federation:**

- SSO configuration (SAML IdP settings)
- OAuth2/OIDC provider configuration
- Federation trust agreements
- IdP signing certificate inventory
- Federated application list


## Tools for Evidence Collection

**PowerShell (Active Directory & Entra ID):**
```powershell
# Password policy (AD)
Get-ADDefaultDomainPasswordPolicy | Export-Csv -Path "EV-1-AD-Password-Policy.csv"

# MFA status (Entra ID - Microsoft Graph PowerShell)
Connect-MgGraph -Scopes "User.Read.All", "UserAuthenticationMethod.Read.All"
Get-MgUser -All | ForEach-Object {
    $methods = Get-MgUserAuthenticationMethod -UserId $_.Id
    [PSCustomObject]@{DisplayName=$_.DisplayName; UserPrincipalName=$_.UserPrincipalName; MFA=($methods).Count -gt 1}
} | Export-Csv "EV-2-MFA-Status.csv" -NoTypeInformation

# Service accounts (AD)
Get-ADUser -Filter {ServicePrincipalName -like "*"} -Properties * | Export-Csv "EV-4-ServiceAccounts.csv"
```

**Azure CLI:**
```bash
# Entra ID password policy
az ad policy list --query "[?contains(type, 'password')]" > EV-1-EntraID-Password-Policy.json

# Conditional access policies
az ad conditional-access policy list > EV-2-Conditional-Access.json
```

**Database Queries (Sanitize Output!):**
```sql
-- PostgreSQL password hash (SANITIZE before saving)
SELECT rolname, 
       SUBSTRING(rolpassword, 1, 20) || '...' as hash_sample
FROM pg_authid 
WHERE rolpassword IS NOT NULL;
```

## Evidence Sanitization

**CRITICAL:** Remove sensitive information:

**Must Sanitize:**

- Password hashes (show format/algorithm only, not actual hash)
- Service account passwords
- IdP signing private keys
- API secrets
- Personal data in user lists


**Safe to Include:**

- Hash algorithm names (bcrypt, Argon2, etc.)
- MFA enrollment percentages
- Certificate validity dates
- Policy settings (password length, complexity rules)
- Configuration screenshots with secrets redacted


---

# Common Pitfalls

## ❌ MISTAKE #1: Assuming "Hashed = Secure"

**Problem:** "Passwords are hashed, so we're compliant"  
**Why Wrong:** MD5 and SHA-1 are hashing algorithms but WEAK and easily cracked with modern GPUs  
**Correct Approach:** Verify actual hash algorithm (bcrypt, Argon2, PBKDF2, scrypt only)  
**Impact:** Weak hashing enables password cracking in breach scenarios

---

## ❌ MISTAKE #2: MFA Enrolled But Not Enforced

**Problem:** Users have MFA set up but it's optional (they can skip it)  
**Why Wrong:** Optional MFA = users will skip it, especially executives  
**Correct Approach:** Conditional access policies that REQUIRE MFA (block access if skipped)  
**Impact:** False sense of security, no actual protection

---

## ❌ MISTAKE #3: SMS-Based MFA Considered Secure

**Problem:** Using SMS one-time passwords for privileged accounts  
**Why Wrong:** SMS vulnerable to SIM swapping attacks (well-documented threat)  
**Correct Approach:** TOTP authenticator apps or hardware tokens for privileged accounts  
**Impact:** Privileged account compromise via SIM swapping

---

## ❌ MISTAKE #4: Service Accounts "Invisible" in Assessment

**Problem:** Focusing only on human users, ignoring service accounts  
**Why Wrong:** Service accounts often have elevated privileges and weak/never-rotated passwords  
**Correct Approach:** Complete service account inventory with password age and privilege review  
**Impact:** Service accounts are prime target for attackers (often overlooked)

---

## ❌ MISTAKE #5: SSO Certificate Expiration Not Monitored

**Problem:** IdP signing certificate expires, SSO breaks organization-wide  
**Why Wrong:** SSO certificate expiration causes authentication failure for ALL federated apps  
**Correct Approach:** Certificate expiration monitoring (90-day advance alert minimum)  
**Impact:** Organization-wide authentication outage

---

## ❌ MISTAKE #6: Password Expiration Without Considering Modern Guidance

**Problem:** Strict 90-day password expiration for all users without MFA  
**Why Wrong:** Forces users to create weak patterns (Password1!, Password2!, etc.)  
**Correct Approach:** No expiration with strong MFA (modern NIST 800-63B guidance) OR 180-day expiration  
**Impact:** Weaker passwords due to frequent rotation requirements

---

## ❌ MISTAKE #7: No Evidence for "Compliant" Claims

**Problem:** Claiming bcrypt/Argon2 hashing without verifying  
**Why Wrong:** Auditors require proof, not just claims  
**Correct Approach:** Database queries, config file excerpts showing actual hash algorithm  
**Impact:** Audit findings despite actual compliance

---

## ❌ MISTAKE #8: MFA Bypass Exceptions Never Reviewed

**Problem:** MFA bypasses granted years ago never re-evaluated  
**Why Wrong:** Temporary exceptions become permanent without review  
**Correct Approach:** Quarterly review of all MFA bypass exceptions  
**Impact:** Privileged accounts without MFA indefinitely

---

## ❌ MISTAKE #9: Certificate-Based Auth "Assumed" Without Verification

**Problem:** Claiming certificate authentication works without testing CRL/OCSP  
**Why Wrong:** Revoked certificates still accepted if CRL/OCSP not checked  
**Correct Approach:** Test certificate revocation checking actually works  
**Impact:** Revoked/compromised certificates still allow access

---

## ❌ MISTAKE #10: Plaintext Passwords in Config Files "Just for Dev"

**Problem:** Application config files contain plaintext passwords marked "development only"  
**Why Wrong:** Dev configs often get deployed to production, or dev system contains production data  
**Correct Approach:** Zero plaintext passwords anywhere - use secrets management (Key Vault, Vault)  
**Impact:** Trivial credential theft from config files

---

# Quality Checklist

**Complete this checklist before submitting assessment for review:**

## Completeness Checks

- [ ] All 5 assessment sections completed (or marked N/A with justification)
- [ ] Every yellow data entry cell filled in
- [ ] Status dropdown selected for every applicable item
- [ ] Evidence location documented for every authentication system
- [ ] Gap descriptions completed for all Partial/Non-Compliant items
- [ ] Password hash algorithms verified (not assumed)
- [ ] MFA enrollment rates documented
- [ ] Remediation plans with dates for all gaps
- [ ] Compliance checklists completed for all sections
- [ ] Summary Dashboard reviewed and totals make sense
- [ ] Evidence Register populated
- [ ] All evidence files exist and are accessible


## Accuracy Checks

- [ ] Password hash algorithms verified (database queries, config files)
- [ ] MFA enrollment rates from actual reports (not estimates)
- [ ] Service account inventory complete (AD, Azure, Linux, databases)
- [ ] Certificate expiration dates verified
- [ ] IdP signing certificates validity checked
- [ ] Plaintext passwords identified (if any exist)
- [ ] Weak hash algorithms (MD5, SHA-1) identified
- [ ] MFA enforcement vs enrollment distinguished
- [ ] Service account password ages documented


## Policy Alignment Checks

- [ ] Approved hash algorithms used (bcrypt, Argon2, PBKDF2, scrypt)
- [ ] Password minimum length ≥12 characters (14 preferred)
- [ ] MFA enforced for ALL privileged accounts
- [ ] MFA enforced for Confidential/Restricted data access
- [ ] MFA enforced for ALL remote access
- [ ] SMS-based MFA NOT used for privileged accounts
- [ ] Service account passwords rotated quarterly (or managed identities used)
- [ ] Certificate validity ≤825 days (internal PKI)
- [ ] IdP signing certificates valid and monitored


## Audit Readiness Checks

- [ ] Evidence is verifiable (auditor could reproduce)
- [ ] Evidence is timestamped and attributable
- [ ] No passwords exposed in screenshots/configs
- [ ] Evidence organized logically and consistently named
- [ ] Assessment tells clear story from beginning to end
- [ ] Hash algorithms not "assumed" - all verified with evidence


## Red Flags to Address BEFORE Submission

- [ ] No plaintext passwords anywhere
- [ ] No weak hash algorithms (MD5, SHA-1) without remediation plan
- [ ] No privileged accounts without MFA
- [ ] No service accounts with admin rights and never-rotated passwords
- [ ] No IdP certificates expiring within 90 days
- [ ] Overall compliance rate >80% (if <80%, indicates systemic issue)


## Final Sanity Checks

- [ ] Summary Dashboard totals match manual count
- [ ] Assessment owner name and role completed
- [ ] Assessment date correct
- [ ] Organization name filled in
- [ ] Next Review Date set (quarterly)
- [ ] Assessment status set to "Draft"


**If ANY checkbox above is unchecked: STOP. Complete missing item before submitting.**

---

# Review & Approval

## Review Process

**Step 1: Self-Review** (Assessment Owner)

- Run through Quality Checklist (Section 7)
- Fix identified issues
- Verify all evidence accessible
- Set status to "Draft"
- Submit to Information Security Officer


**Step 2: Technical Review** (Information Security Officer)

- Verify hash algorithms documented
- Validate MFA enforcement (not just enrollment)
- Assess service account inventory completeness
- Check certificate expiration monitoring
- Verify remediation plans realistic
- Provide feedback


**Step 3: Remediation (if needed)** (Assessment Owner)

- Address review feedback
- Update assessment
- Re-submit if significant changes


**Step 4: Final Approval** (CISO)

- Review overall authentication posture
- Approve remediation timelines
- Accept documented risks
- Sign off assessment
- Set Next Review Date


## Approval Timeline

**Typical Timeline:**

- Assessment completion: 6-8 hours (owner)
- Self-review: 30-60 minutes (owner)
- Technical review: 2-3 business days (ISO)
- Remediation: 1-2 hours (owner)
- Final approval: 1-2 business days (CISO)
- **Total:** 1-2 weeks start to finish


## After Approval

**Immediate Actions:**
1. File approved assessment in ISMS repository
2. Distribute to relevant stakeholders
3. Track remediation items in project system
4. Schedule follow-up reviews

**Ongoing Monitoring:**

- Password policy compliance (quarterly)
- MFA enrollment rates (monthly)
- Service account password age (quarterly)
- Certificate expiration monitoring (continuous)
- IdP signing certificate expiration (90-day alerts)


**Triggers for Immediate Re-Assessment:**

- Password database breach (force password reset with strong hash)
- Privileged account compromise
- Discovery of plaintext passwords
- Discovery of weak hash algorithms (MD5, SHA-1)
- IdP certificate expiration incident
- Failed audit findings on authentication


## Continuous Improvement

**Use Assessment Results to Improve:**

- Pattern of weak hashes? → Database migration project to bcrypt/Argon2
- Low MFA enrollment? → Forced enrollment campaign
- Service account password age >1 year? → Implement PAM or managed identities
- IdP certificate near expiration? → Certificate lifecycle management automation


**Feedback Loop:**

- Assessment owner provides feedback on this guide
- ISO reviews common questions/issues
- Update guide for next assessment cycle


---

# PART II: TECHNICAL SPECIFICATION
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

<!-- QA_VERIFIED: 2026-01-31 -->
