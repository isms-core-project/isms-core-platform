# Control A.8.24: Use of Cryptography
## POLICY REQUIREMENTS - SECTION 2.4
## Cryptographic Controls for Authentication

---

**Document ID**: ISMS-POL-A.8.24-S2.4  
**Title**: Use of Cryptography - Authentication  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Identity & Access Management Lead | Initial authentication cryptography requirements |

**Review Cycle**: Annual (or upon authentication protocol changes/vulnerabilities)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Identity & Access Management (IAM) Lead
- Secondary: Chief Technology Officer (CTO) or IT Director
- Compliance: Legal/Compliance Officer (for identity/privacy regulations)

**Distribution**: IAM Teams, System Administrators, Development Teams, Infrastructure Teams, Security Operations Center (SOC)  
**Related Standards**: ISO/IEC 27001:2022 Controls A.5.17, A.5.18, A.8.5, A.8.24, NIST SP 800-63B (Digital Identity), BSI TR-02102-1, nFADP, GDPR Art. 32

---

## 2.4 Cryptographic Controls for Authentication

### Purpose
This section defines mandatory cryptographic requirements for authentication mechanisms that verify the identity of users, systems, and services.

---

### 2.4.1 Password Security

#### Password Storage Requirements

**Mandatory Cryptographic Protection:**
- Passwords MUST NEVER be stored in plaintext
- Passwords MUST be hashed using approved password hashing algorithms
- Password hashes MUST include cryptographically random salt (minimum 128-bit)
- Salts MUST be unique per password (no shared salts)

#### Approved Password Hashing Algorithms

**Priority Order (highest to lowest):**

| Algorithm | Parameters | Status | Use Case |
|-----------|------------|--------|----------|
| **Argon2id** | **m=64MB (65536 KiB), t=3 iterations, p=4 parallelism** | **APPROVED (Preferred)** | All new implementations |
| **bcrypt** | **Cost factor ≥12** | **APPROVED** | Existing systems, legacy compatibility |
| **PBKDF2-HMAC-SHA256** | **≥600,000 iterations** | **ACCEPTABLE** | When Argon2/bcrypt unavailable |
| **scrypt** | **N=2^17, r=8, p=1** | **ACCEPTABLE** | Memory-hard requirements |

**PROHIBITED:**
- Plain SHA-256, SHA-512, SHA-3 (without key stretching)
- MD5, SHA-1 (completely broken)
- Unsalted hashes of any type
- Reversible encryption of passwords

#### Parameter Guidance

**Argon2id Configuration:**
- Memory (m): Minimum 64 MB, increase as system resources allow
- Time (t): Minimum 3 iterations, adjust to achieve ~500ms hash time
- Parallelism (p): 4 threads (adjust based on server CPU cores)
- Salt length: 16 bytes minimum
- Output length: 32 bytes (256 bits)

**bcrypt Configuration:**
- Cost factor: Minimum 12, increase annually as computing power increases
- Recommendation: Test on production hardware to achieve ~250-500ms hash time
- Cost factor 14-16 recommended for high-security environments

**PBKDF2 Configuration:**
- Minimum 600,000 iterations for HMAC-SHA256
- Minimum 210,000 iterations for HMAC-SHA512
- Salt length: 16 bytes minimum
- Increase iterations annually

#### Password Complexity Requirements

**Minimum Requirements:**
- Standard user accounts: 12 characters minimum
- Privileged accounts: 14 characters minimum
- Service accounts: 20 characters minimum (or use key-based authentication)
- Administrative accounts: 14 characters minimum

**Complexity:**
- At least one uppercase letter (A-Z)
- At least one lowercase letter (a-z)
- At least one digit (0-9)
- At least one special character (!@#$%^&* etc.)

**Prohibited:**
- Dictionary words (single language or common substitutions)
- Common passwords (must check against breach databases)
- Passwords containing username or email
- Repeated or sequential characters (e.g., "aaa", "123", "abc")
- Company name or variations

#### Password Lifecycle

**Password Rotation:**
- Standard accounts: Minimum 90 days, maximum 365 days
- Privileged accounts: Minimum 60 days, maximum 90 days
- Service accounts: 90 days maximum (or migrate to key-based authentication)
- Immediate rotation required upon:
  - Suspected compromise
  - Employee termination (shared accounts)
  - Security incident
  - Departure of anyone who knew the password

**Password History:**
- Minimum 12 previous passwords must be remembered
- Prevent password reuse within 1 year
- Password history MUST be stored with same security as current passwords

#### Account Lockout and Brute-Force Protection

**Requirements:**
- Account lockout REQUIRED after failed authentication attempts
- Maximum failed attempts: 5-10 (configurable based on risk assessment)
- Lockout duration: Minimum 15 minutes (or manual unlock by administrator)
- CAPTCHA or similar challenge RECOMMENDED after 3 failed attempts
- Rate limiting REQUIRED on authentication endpoints
- Failed authentication attempts MUST be logged

---

### 2.4.2 Multi-Factor Authentication (MFA)

#### MFA Scope - Mandatory Requirements

**MFA REQUIRED for:**
- All remote access (VPN, remote desktop, SSH from external networks)
- All privileged/administrative accounts
- Access to systems containing Confidential or Restricted data
- Cloud service administration (AWS, Azure, GCP, SaaS admin panels)
- Financial systems and approval workflows
- Access to customer data
- Password reset and account recovery processes

**MFA RECOMMENDED for:**
- All user accounts accessing organizational resources
- Internal system access for sensitive applications
- Developer access to production environments
- Database administrator access

#### Approved MFA Methods

**Tier 1 - Phishing-Resistant (Preferred):**
- **FIDO2/WebAuthn hardware security keys** (YubiKey, Google Titan, etc.)
- **Smart cards with PKI certificates**
- **Platform authenticators** (Windows Hello, Touch ID with secure enclave)
- **Mutual TLS (mTLS) certificate authentication**

**Tier 2 - Strong MFA (Acceptable):**
- **TOTP (Time-based One-Time Password)** via authenticator apps
  - Google Authenticator, Microsoft Authenticator, Authy
  - 30-second time step, SHA-1/SHA-256
  - 6-digit codes minimum
- **Push notifications with number matching**
  - Microsoft Authenticator with number matching
  - Duo Push with approval prompts
- **HOTP (HMAC-based One-Time Password)** for hardware tokens

**Tier 3 - Acceptable with Limitations:**
- **SMS-based OTP** - ONLY acceptable where no other method available
  - Must acknowledge weakness to SMS interception (SIM swapping, SS7 attacks)
  - MUST NOT be used for privileged accounts
  - MUST NOT be used for financial transactions
- **Email-based OTP** - ONLY for low-risk scenarios
  - Email account MUST have MFA enabled
  - Not acceptable for privileged access

**PROHIBITED:**
- Security questions as second factor (knowledge-based authentication alone)
- Voice calls for OTP delivery (vulnerable to social engineering)

#### MFA Implementation Requirements

**Enrollment:**
- Users MUST enroll at least one primary MFA method
- Backup MFA method REQUIRED (in case of device loss)
- Backup codes MUST be provided (one-time use codes)
- MFA enrollment status MUST be tracked and reported

**Backup Authentication:**
- Backup authentication methods MUST be available
- Backup codes (one-time use): Minimum 10 codes, each ≥10 characters
- Multiple enrolled devices RECOMMENDED
- Admin-assisted recovery process MUST be documented and require identity verification

**MFA Bypass Procedures:**
- MFA bypass MUST be exceptional and time-limited
- Bypass requests MUST be approved by manager and security team
- Bypass MUST be logged and audited
- Temporary bypass maximum duration: 24 hours

#### MFA Session Management

**Requirements:**
- MFA prompt frequency based on risk:
  - High-risk: Every session (no remember device)
  - Medium-risk: Every 30 days per device
  - Low-risk: Every 90 days per device
- Device trust MUST be re-evaluated periodically
- IP address change SHOULD trigger MFA re-authentication
- Unusual login patterns SHOULD trigger MFA prompt

---

### 2.4.3 Certificate-Based Authentication

#### Use Cases for Certificate Authentication

**Primary Use Cases:**
- VPN client authentication
- Wireless network authentication (802.1X)
- Web service API authentication (mutual TLS)
- User authentication to web applications
- Smart card authentication for workstation login
- Code signing
- Email signing and encryption (S/MIME)

#### Certificate Requirements

**Certificate Standards:**
- Certificates MUST follow approved algorithm requirements (see Section 2.1)
- Minimum key length:
  - RSA: 2048-bit (3072-bit preferred)
  - ECDSA: P-256 (P-384 preferred)
  - Ed25519: 256-bit equivalent
- Certificate validity MUST NOT exceed 1 year for user/device certificates
- Certificate validity MUST NOT exceed 397 days for TLS server certificates

#### Certificate Issuance and Management

**Certificate Authority (CA):**
- Certificates MUST be issued by trusted CA:
  - Internal organizational CA (preferred for internal use)
  - Public trusted CA (required for external-facing services)
- Self-signed certificates PROHIBITED for production authentication
- Self-signed certificates ACCEPTABLE for development/testing only

**Certificate Request Process:**
- Certificate requests MUST be authenticated and authorized
- Identity verification REQUIRED before certificate issuance
- Certificate requests for service accounts MUST be approved by system owner
- Privileged account certificates MUST have additional approval

**Certificate Lifecycle:**
- Certificate inventory MUST be maintained
- Certificate expiration monitoring REQUIRED (30-day advance notice)
- Expired certificates MUST be removed from systems
- Certificate renewal MUST begin 30 days before expiration

#### Private Key Protection

**Requirements:**
- Private keys MUST be generated and stored securely
- Private keys MUST NOT be transmitted over unencrypted channels
- Private keys MUST NOT be shared between users or systems

**Storage Requirements:**
- **Hardware tokens/smart cards** (preferred for users)
  - FIPS 140-2 Level 2 or higher recommended
  - PIN protection REQUIRED
  - Tamper-resistant hardware
- **Trusted Platform Module (TPM)** for device certificates
  - TPM 2.0 preferred
  - TPM storage for private keys where available
- **Operating system key stores** (acceptable alternative)
  - Windows: Certificate Store with private key protection
  - macOS: Keychain with access control lists
  - Linux: PKCS#11 tokens or encrypted file systems
- **Hardware Security Module (HSM)** for service certificates
  - Required for critical services and code signing

**Private Key Access Control:**
- Private key access MUST require authentication (password, PIN, biometric)
- Private key access MUST be logged where technically feasible
- Private key export SHOULD be disabled or restricted

#### Certificate Revocation

**Revocation Requirements:**
- Certificate revocation capability MUST be available
- Certificates MUST be revoked within 24 hours when:
  - Private key is compromised or suspected compromised
  - User employment is terminated
  - Device is decommissioned or lost
  - Certificate information changes

**Revocation Mechanisms:**
- Online Certificate Status Protocol (OCSP) REQUIRED for high-value transactions
- Certificate Revocation List (CRL) REQUIRED as fallback
- OCSP Stapling RECOMMENDED for web servers
- CRL distribution points MUST be accessible
- CRL MUST be published regularly (daily minimum)

---

### 2.4.4 Service Accounts

#### Service Account Authentication

**Prohibited:**
- Shared passwords for service accounts
- Interactive login with service account credentials
- Service accounts with standard user password rotation

**Required:**
- Service accounts MUST use certificate-based or key-based authentication
- API keys or tokens with automated rotation
- Managed service identities (cloud environments)

#### Approved Authentication Methods for Service Accounts

**Priority Order:**

**1. Managed/System Identities (Highest Preference):**
- AWS IAM Roles for EC2/ECS/Lambda
- Azure Managed Identity
- GCP Service Accounts with Workload Identity
- Kubernetes Service Accounts with projected tokens

**2. Certificate-Based Authentication:**
- X.509 client certificates
- Mutual TLS (mTLS) for service-to-service
- Certificate stored in HSM or secure key store

**3. API Keys/Tokens:**
- Cryptographically random tokens (minimum 256-bit entropy)
- Stored in secrets management system
- Scoped to minimum required permissions

**4. Temporary Credentials (where applicable):**
- AWS STS AssumeRole credentials
- Azure AD service principal with certificate
- OAuth 2.0 client credentials flow

#### Service Account Key Management

**Key Generation:**
- Keys MUST be generated using CSPRNG
- Minimum key length: 256 bits for symmetric, 2048 bits for RSA
- Keys MUST be unique per service account

**Key Storage:**
- Keys MUST be stored in secrets management system:
  - HashiCorp Vault
  - AWS Secrets Manager
  - Azure Key Vault
  - GCP Secret Manager
  - CyberArk, Thycotic, or similar
- Keys MUST NOT be stored in:
  - Application code
  - Configuration files
  - Environment variables (except in secure runtime environments)
  - Version control systems

**Key Rotation:**
- Service account credentials MUST rotate every 90 days maximum
- Automated rotation REQUIRED where technically feasible
- Grace period for credential overlap RECOMMENDED (old key valid during transition)
- Rotation MUST be tested in non-production environment

**Key Access Control:**
- Service account key access MUST be restricted to:
  - The service/application using the key
  - Authorized operations personnel (break-glass access)
- Key access MUST be logged and audited
- Unused keys MUST be revoked immediately

#### Service Account Lifecycle

**Provisioning:**
- Service account creation MUST be approved
- Service account purpose MUST be documented
- Service account permissions MUST follow least privilege
- Service account credentials MUST be delivered securely

**Monitoring:**
- Service account usage MUST be monitored
- Anomalous activity MUST trigger alerts
- Unused service accounts MUST be identified quarterly
- Service account inventory MUST be maintained

**Decommissioning:**
- Service accounts MUST be disabled when no longer needed
- Credentials MUST be revoked upon decommissioning
- Service account removal MUST be documented
- Associated keys/certificates MUST be destroyed

---

### 2.4.5 Single Sign-On (SSO) and Federated Authentication

#### SSO Requirements

**Mandatory SSO Implementation:**
- SSO REQUIRED for all cloud SaaS applications where supported
- SSO PREFERRED for internal web applications
- Centralized identity provider (IdP) REQUIRED

**Approved SSO Protocols:**
- **SAML 2.0** (Security Assertion Markup Language) - APPROVED
- **OAuth 2.0 with OpenID Connect** - APPROVED
- **WS-Federation** - ACCEPTABLE for Microsoft environments
- **Kerberos** - ACCEPTABLE for internal Active Directory environments

**PROHIBITED:**
- Legacy SSO mechanisms without strong cryptographic protection
- Custom SSO implementations without security review

#### Identity Provider (IdP) Requirements

**Approved Identity Providers:**
- **Enterprise Solutions:**
  - Azure Active Directory / Entra ID
  - Okta
  - Ping Identity
  - Active Directory Federation Services (ADFS)
  - Google Workspace Identity
  - OneLogin
- **Self-hosted:**
  - Keycloak (with proper security hardening)
  - Shibboleth (for academic environments)

**IdP Security Requirements:**
- IdP MUST enforce MFA for all user authentications
- IdP MUST use HTTPS/TLS for all communications
- IdP MUST support strong cryptographic algorithms (see Section 2.1)
- IdP session timeout MUST be configured (maximum 8 hours for standard users, 1 hour for privileged)

#### SAML Configuration

**SAML Security Requirements:**
- SAML assertions MUST be signed (XML digital signatures)
- SAML assertion encryption RECOMMENDED for sensitive attributes
- SAML Response signing REQUIRED
- Assertion validity period MUST be limited (maximum 5 minutes)
- Replay protection MUST be enabled (assertion ID tracking)

**Certificate Management for SAML:**
- SAML signing certificates MUST use minimum RSA 2048-bit or ECDSA P-256
- SAML certificates MUST be rotated annually
- Certificate expiration monitoring REQUIRED
- Metadata exchange MUST use secure channels

#### OAuth 2.0 and OpenID Connect

**OAuth/OIDC Security Requirements:**
- Authorization code flow with PKCE (Proof Key for Code Exchange) REQUIRED for public clients
- Client credentials flow ACCEPTABLE for server-to-server authentication
- Implicit flow PROHIBITED (deprecated due to security issues)
- State parameter REQUIRED to prevent CSRF attacks
- Nonce parameter REQUIRED in OIDC ID tokens

**Token Security:**
- Access tokens: Maximum lifetime 1 hour
- Refresh tokens: Maximum lifetime 24 hours for user sessions
- Refresh tokens: Rotation on use RECOMMENDED
- Tokens MUST be transmitted only over HTTPS
- Token storage MUST be secure (HTTPOnly cookies, secure storage APIs)

**Client Authentication:**
- Confidential clients MUST authenticate (client secret or certificate)
- Client secrets MUST be minimum 256-bit entropy
- Client certificates PREFERRED over client secrets for high-security applications

#### Federation Trust

**Federation Requirements:**
- Federation partners MUST be approved by security team
- Trust relationships MUST be documented
- Federation metadata MUST be validated
- Certificate trust chains MUST be verified

**Federation Metadata:**
- Metadata MUST be obtained through secure channels
- Metadata signatures MUST be verified
- Metadata SHOULD be refreshed periodically (daily recommended)
- Metadata expiration monitoring REQUIRED

---

### 2.4.6 Biometric Authentication

#### Biometric Use Cases

**Acceptable Use:**
- Device unlock (mobile phones, laptops)
- Physical access control (building entry)
- MFA component (in combination with other factors)

**Requirements:**
- Biometric authentication MUST be combined with other factor (PIN/password)
- Biometric authentication alone INSUFFICIENT for high-security access
- Fallback authentication method REQUIRED

#### Biometric Data Protection

**Storage Requirements:**
- Biometric templates MUST be stored in secure enclave/TPM
- Raw biometric data MUST NOT be stored (only templates/hashes)
- Biometric data MUST NOT be transmitted over network
- On-device processing REQUIRED (local biometric verification)

**Privacy Requirements:**
- Biometric data collection MUST have user consent
- Biometric data MUST be deletable by user
- Biometric data MUST NOT be used for purposes beyond authentication
- Compliance with biometric privacy laws REQUIRED (GDPR, BIPA, etc.)

---

## Compliance Verification

**This section SHALL be verified through:**
- Quarterly password policy compliance audit
- Annual MFA adoption rate reporting
- Certificate inventory and expiration monitoring
- Service account credential audit (quarterly)
- SSO integration security review (annual)
- Failed authentication attempt monitoring
- Privileged account MFA enforcement verification

---

## Related Documents

- **ISMS-POL-A.8.24-S1** - Section 1: Purpose, Scope, Definitions
- **ISMS-POL-A.8.24-S2.1** - Use of Cryptographic Controls
- **ISMS-POL-A.8.24-S2.2** - Data Transmission Requirements
- **ISMS-POL-A.8.24-S2.3** - Data Storage Requirements
- **ISMS-POL-A.8.24-S2.5** - Compliance Requirements
- **ISMS-POL-A.5.17** - Password and Authentication Policy
- **ISMS-IMP-A.8.24** - Implementation & Compliance Status

---

**End of Section 2.4 - Cryptographic Controls for Authentication**

*"Passwords are like underwear: don't let people see it, change it regularly, and don't share it with strangers."*  
*— Chris Pirillo (adapted for cryptographic authentication)*
