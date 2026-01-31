# ISMS-POL-A.8.2-3-5-S2
## Secure Authentication Requirements (A.8.5)

**Document ID**: ISMS-POL-A.8.2-3-5-S2  
**Title**: Secure Authentication Requirements (ISO/IEC 27001:2022 Control A.8.5)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | IAM Security Lead | Initial secure authentication requirements (A.8.5) |

**Review Cycle**: Annual (aligned with authentication infrastructure changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Identity & Access Management Lead
- Operational Review: IT Operations Manager

**Distribution**: IAM team, security team, IT operations, application owners, auditors  
**Related Documents**: 
- ISMS-POL-A.8.2-3-5-S1 (Executive Summary)
- ISMS-IMP-A.8.2-3-5-S1 (Authentication Implementation)
- ISMS-IMP-A.8.2-3-5-S2 (MFA Deployment)

---

## 1. Control Objective and Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.5

**Official Control Text**:

> *Secure authentication technologies and procedures should be implemented based on information access restrictions and the topic-specific policy on access control.*

**Control Purpose**: Ensure users prove their identity using secure mechanisms appropriate to the sensitivity of information and systems being accessed, with stronger authentication for privileged access and sensitive data.

**Why This Matters**:

Authentication is the **gateway to all systems**. Every security control depends on knowing WHO is accessing systems. Weak authentication means:

- **81% of breaches involve stolen credentials** (Verizon DBIR)
- **Password-only authentication** is trivially compromised (phishing, credential stuffing, brute force)
- **Shared credentials** eliminate accountability (cannot determine who did what)
- **Weak passwords** are cracked instantly (password123, Summer2024!)

Strong authentication provides:
- **99.9% reduction in account compromise** with MFA (Microsoft Security)
- **Phishing resistance** with FIDO2 hardware tokens
- **User convenience** with Single Sign-On (SSO)
- **Audit trail** of authentication events

### 1.2 Scope of A.8.5 Requirements

This section defines mandatory requirements for:

1. **Authentication Mechanism Requirements** - Supported authentication methods
2. **Multi-Factor Authentication (MFA) Requirements** - MFA coverage and deployment
3. **Password Policy Requirements** - Password complexity, expiration, strength
4. **Single Sign-On (SSO) Requirements** - SSO deployment and integration
5. **Authentication Protocols** - SAML, OAuth, OpenID Connect, Kerberos, RADIUS
6. **Certificate-Based Authentication** - PKI for systems and services
7. **Biometric Authentication** - Fingerprint, facial recognition requirements
8. **Authentication Logging** - Authentication event logging and monitoring
9. **Credential Compromise Response** - Detection and response procedures

---

## 2. Authentication Mechanism Requirements

### 2.1 Requirement: Supported Authentication Methods

**REQ-A85-001**: [Organization] **MUST** support multiple authentication mechanisms appropriate to use cases.

**Supported Authentication Methods**:

| Method | Use Case | Security Level | Deployment Status |
|--------|----------|----------------|-------------------|
| **Password + MFA** | Standard user access | High | Mandatory for all users |
| **Single Sign-On (SSO)** | Application access | High (with MFA) | Deploy for all SaaS/web apps |
| **Certificate-based** | System-to-system, API | Very High | Deploy for APIs and services |
| **Biometric** | Mobile devices, physical access | High (with liveness detection) | Optional, user choice |
| **Hardware tokens** | High-security access | Very High | Deploy for Tier 0 admins |

**Authentication Method Selection Criteria**:

1. **User Type**:
   - **Standard users**: Password + MFA (authenticator app or push)
   - **Privileged users**: Password + MFA (hardware token preferred) + session recording
   - **Remote users**: VPN with MFA mandatory
   - **Contractors/vendors**: Time-limited access, MFA required

2. **System Criticality**:
   - **Critical systems** (Tier 0): Hardware MFA tokens (FIDO2) required
   - **High criticality** (Tier 1): MFA mandatory (authenticator app minimum)
   - **Medium criticality** (Tier 2): MFA recommended
   - **Low criticality**: Password acceptable (internal non-sensitive systems)

3. **Data Sensitivity**:
   - **Restricted data access**: MFA + certificate-based authentication
   - **Confidential data access**: MFA mandatory
   - **Internal data access**: MFA recommended
   - **Public data access**: Password acceptable

**Technology-Agnostic Approach**:

[Organization] may use any of the following authentication platforms:
- Microsoft Active Directory (on-premises)
- Azure Active Directory / Microsoft Entra ID (cloud)
- Okta
- Google Workspace
- Auth0
- Other enterprise identity providers

Requirements apply regardless of platform choice.

**Audit Evidence**: Authentication mechanism inventory, platform documentation

---

## 3. Multi-Factor Authentication (MFA) Requirements

### 3.1 Requirement: MFA Coverage Requirements

**REQ-A85-002**: [Organization] **MUST** deploy multi-factor authentication (MFA) according to coverage requirements.

**MFA Coverage Tiers**:

**Tier 1 - MANDATORY MFA (Non-negotiable)**:
- ✅ **ALL privileged users** (system admins, DBAs, security admins, cloud admins)
- ✅ **ALL remote access** (VPN, external access)
- ✅ **ALL access to restricted/confidential data**
- ✅ **ALL access to financial systems**
- ✅ **ALL access to production environments**
- ✅ **NIS2 compliance**: Essential/important entities MUST have MFA per Article 21(2)(e)

**Tier 2 - RECOMMENDED MFA (Strong recommendation)**:
- ⚠️ **ALL standard users** (phishing protection for everyone)
- ⚠️ **ALL SaaS application access** (Office 365, Salesforce, etc.)
- ⚠️ **ALL cloud platform access** (AWS, Azure, GCP consoles)

**Tier 3 - OPTIONAL MFA**:
- ℹ️ **Internal-only, non-sensitive systems** (MFA not required but available)
- ℹ️ **Service accounts** (use certificate-based authentication instead)

**Target MFA Coverage Metrics**:
- **Privileged users with MFA**: 100% (mandatory)
- **Remote access users with MFA**: 100% (mandatory)
- **Standard users with MFA**: Target 95%+ within 12 months
- **Overall MFA coverage**: Target 90%+ within 24 months

**Audit Evidence**: MFA enrollment data (Workbook 2), coverage metrics by user type

### 3.2 Requirement: MFA Methods Supported

**REQ-A85-003**: [Organization] **MUST** support multiple MFA methods with varying security levels.

**Supported MFA Methods** (ranked by security level):

1. **Hardware Tokens (FIDO2, YubiKey)** - HIGHEST SECURITY
   - **Security**: Phishing-resistant, cryptographic authentication
   - **Use case**: Tier 0 administrators, high-value accounts, executives
   - **Platforms**: Works with Azure AD, Okta, Google Workspace, web applications
   - **Cost**: ~$50 per token, one-time expense
   - **User experience**: Excellent (tap token)

2. **Authenticator Apps (TOTP)** - HIGH SECURITY
   - **Security**: Time-based one-time passwords, offline capable
   - **Use case**: Standard users, privileged users (if hardware tokens unavailable)
   - **Platforms**: Microsoft Authenticator, Google Authenticator, Authy, Duo Mobile
   - **Cost**: Free
   - **User experience**: Good (type 6-digit code or approve push)

3. **Push Notifications** - HIGH SECURITY
   - **Security**: Real-time approval, user confirms authentication attempt
   - **Use case**: Standard users, convenient for frequent logins
   - **Platforms**: Microsoft Authenticator, Okta Verify, Duo Mobile
   - **Cost**: Free (requires internet connection)
   - **User experience**: Excellent (tap "Approve")
   - **Risk**: Vulnerable to MFA fatigue attacks (approve notification without checking)

4. **Biometric Authentication** - MEDIUM-HIGH SECURITY
   - **Security**: Fingerprint, facial recognition (with liveness detection)
   - **Use case**: Mobile devices, physical access
   - **Platforms**: Windows Hello, Face ID, Touch ID
   - **Cost**: Free (if device supports)
   - **User experience**: Excellent
   - **Risk**: Biometric data compromise is permanent (cannot change fingerprint)

5. **SMS/Voice** - LOW SECURITY (DISCOURAGED)
   - **Security**: Vulnerable to SIM swapping, interception
   - **Use case**: ONLY as last-resort backup method
   - **Status**: **Discouraged** - do not use as primary MFA
   - **Rationale**: NIST SP 800-63B discourages SMS due to vulnerabilities

**MFA Method Selection Guidelines**:
- **Tier 0 administrators**: Hardware tokens (FIDO2) required
- **Privileged users**: Authenticator app minimum, hardware token recommended
- **Standard users**: Authenticator app or push notifications
- **Mobile-only users**: Platform biometrics (Windows Hello, Face ID) acceptable
- **Backup MFA method**: Required for all users (in case primary method unavailable)

**Prohibited MFA Methods**:
- ❌ SMS as primary MFA method (only allowed as backup)
- ❌ Email-based OTP (email compromise = MFA bypass)
- ❌ Single-factor authentication for privileged access

**Audit Evidence**: MFA method inventory, user enrollment by method type

### 3.3 Requirement: MFA Enrollment Procedures

**REQ-A85-004**: MFA enrollment **MUST** be mandatory with defined timelines and verification.

**Mandatory Enrollment Requirements**:

1. **Privileged Users**:
   - **Enrollment deadline**: Within 7 days of privileged access grant
   - **Verification**: IT Security team verifies enrollment before activating privileged access
   - **Non-compliance**: Privileged access revoked if MFA not enrolled

2. **Remote Access Users**:
   - **Enrollment deadline**: Before VPN access granted
   - **Verification**: VPN access requires MFA enrollment first
   - **Non-compliance**: VPN access denied until MFA enrolled

3. **Standard Users**:
   - **Enrollment deadline**: Phased rollout over 12 months
   - **Verification**: Self-service enrollment, IT support available
   - **Non-compliance**: Escalation to management, eventual account restriction

**Enrollment Procedures**:

1. **User receives enrollment notification** (email with instructions)
2. **User installs authenticator app** (Microsoft Authenticator, Google Authenticator, etc.)
3. **User scans QR code** or enters setup key to register account
4. **User verifies MFA works** by authenticating once
5. **User registers backup MFA method** (second device or backup codes)
6. **System confirms enrollment** (user added to "MFA Enrolled" group)

**Backup MFA Method Registration**:
- **Required**: All users must register backup method
- **Options**: Second authenticator device, hardware token, backup codes
- **Purpose**: Prevent lockout if primary MFA device lost/stolen

**Audit Evidence**: MFA enrollment logs, enrollment completion rates, verification records

### 3.4 Requirement: MFA Recovery Procedures

**REQ-A85-005**: MFA recovery procedures **MUST** balance security with usability.

**MFA Recovery Scenarios**:

1. **Lost MFA Device** (phone lost/stolen):
   - User contacts IT support helpdesk
   - Identity verification required (employee ID, manager confirmation, security questions)
   - IT admin resets MFA registration
   - User re-enrolls MFA immediately (temporary access may be granted)

2. **Broken MFA Device** (phone damaged, app not working):
   - User uses backup MFA method (if registered)
   - If no backup: Same process as lost device

3. **MFA App Accidentally Deleted**:
   - User re-installs app
   - Uses backup codes or backup device to authenticate
   - Re-registers primary device if needed

**MFA Reset Verification Requirements**:
- **Identity proofing**: Multi-factor identity verification before MFA reset
  - Employee ID + manager email confirmation
  - OR in-person verification with ID badge
  - OR security questions + callback to registered phone number
- **Audit logging**: All MFA resets logged and reviewed monthly
- **Alert on suspicious resets**: Multiple reset attempts trigger security review

**Break-Glass MFA Bypass**:
- **Emergency accounts** (break-glass) may bypass MFA temporarily
- **Requires**: Executive approval (CISO or CIO)
- **Triggers**: Critical incident, all MFA methods unavailable
- **Audit**: Full investigation after use, re-enable MFA immediately

**Audit Evidence**: MFA reset logs, identity verification records, break-glass usage logs

---

## 4. Password Policy Requirements

### 4.1 Requirement: Password Complexity and Length

**REQ-A85-006**: Password policies **MUST** follow modern best practices emphasizing length over complexity.

**Modern Password Policy** (aligned with NIST SP 800-63B):

**Password Length** (MOST IMPORTANT):
- **Minimum length**: 12 characters (passwords)
- **Recommended length**: 15+ characters (passphrases)
- **Rationale**: Length provides far more entropy than complexity rules
  - 12-character password = 10^14 combinations (with basic complexity)
  - 15-character passphrase = 10^18 combinations

**Password Complexity** (LESS IMPORTANT):
- **Required**: At least 3 of 4 character types:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special characters (!@#$%^&*)
- **Rationale**: Some complexity reduces dictionary attacks, but length matters more

**Passphrase Encouragement**:
- **Example**: "CoffeeTable!Morning92" (22 chars, easy to remember, very strong)
- **Better than**: "P@ssw0rd!" (9 chars, meets complexity, but weak)

**Password Strength Validation**:
- **Dictionary word detection**: Reject common passwords (password, 123456, qwerty, etc.)
- **Breach detection**: Check against known breached password lists (Have I Been Pwned API)
- **Sequential/repeated character detection**: Reject passwords like "aaaabbbb" or "12345678"

**Modern Best Practice Changes**:
- ✅ **Favor length over complexity** (15-char simple phrase beats 8-char complex password)
- ✅ **Allow spaces in passwords** (enables passphrases: "my dog has fleas 2024")
- ✅ **Allow copy-paste** (encourages password manager use)
- ❌ **No forced complexity** if password is 15+ characters
- ❌ **No character substitution requirements** (P@ssw0rd patterns are well-known to attackers)

**Audit Evidence**: Password policy configuration, password strength distribution analysis

### 4.2 Requirement: Password Expiration

**REQ-A85-007**: Password expiration **SHOULD** be disabled unless specific risk requires it.

**Modern Guidance on Password Expiration**:

**NIST SP 800-63B (2020)** recommends:
- **NO forced periodic password expiration** unless compromise suspected
- **Rationale**: Forced expiration leads to weaker passwords (Password1, Password2, Password3)
- **Better approach**: Continuous monitoring for compromised credentials

**[Organization] Password Expiration Policy**:

**Default: NO PASSWORD EXPIRATION**
- **Applies to**: Standard user accounts with MFA enabled
- **Rationale**: MFA provides strong security, forced expiration degrades password quality
- **Monitoring**: Passwords checked against breach databases continuously

**Exceptions Requiring Password Expiration**:

1. **Accounts WITHOUT MFA** (if any exist):
   - **Expiration**: 90 days
   - **Rationale**: Password-only access needs rotation as compensating control
   - **Goal**: Eliminate password-only access, then remove expiration

2. **Shared/Service Accounts**:
   - **Expiration**: 90 days (or automated rotation via PAM)
   - **Rationale**: Shared credentials have higher compromise risk

3. **Privileged Accounts in PAM Vault**:
   - **Rotation**: Automatic after each use (PAM-managed)
   - **Alternative**: JIT access with temporary passwords

4. **Suspected Compromise**:
   - **Immediate**: Force password reset if compromise suspected
   - **Notification**: User notified of security concern

**Audit Evidence**: Password expiration settings, accounts with/without MFA, password age distribution

### 4.3 Requirement: Password History and Reuse Prevention

**REQ-A85-008**: Password history **MUST** prevent reuse of recent passwords.

**Password History Requirements**:
- **History length**: Remember last 5 passwords
- **Reuse prevention**: Cannot reuse any of last 5 passwords
- **Rationale**: Prevents cycling through Password1, Password2, Password3
- **Exception**: Emergency password resets (if absolutely necessary, log and review)

**Audit Evidence**: Password history configuration, password reuse attempt logs

### 4.4 Requirement: Password Breach Detection

**REQ-A85-009**: Passwords **MUST** be checked against known breached password databases.

**Breach Detection Implementation**:

1. **At Password Creation/Change**:
   - Check password against Have I Been Pwned API (pwned passwords)
   - Reject password if found in breach database
   - User notification: "This password has been compromised in a data breach - please choose a different password"

2. **Continuous Monitoring**:
   - **Azure AD Password Protection**: Continuously monitors and alerts on compromised passwords
   - **Okta Compromised Credential Detection**: Automatically detects known breached credentials
   - **Force reset**: If user's password found in new breach, force immediate reset

**Breach Detection Platforms**:
- **Azure AD Password Protection**: Built-in for Azure AD
- **Okta Compromised Credential Detection**: Built-in for Okta
- **Have I Been Pwned API**: Can be integrated into custom authentication systems
- **Enzoic**: Commercial breach detection service

**Audit Evidence**: Breach detection configuration, compromised password detection logs, forced resets

---

## 5. Single Sign-On (SSO) Requirements

### 5.1 Requirement: SSO Deployment

**REQ-A85-010**: Single Sign-On (SSO) **MUST** be deployed for all supported applications.

**SSO Benefits**:
- **Reduced password fatigue**: Users remember one strong password instead of dozens
- **Improved security**: Centralized authentication with MFA
- **Better user experience**: Seamless access to applications
- **Centralized logging**: All authentication events in one place
- **Faster onboarding/offboarding**: Disable one account = disable all access

**SSO Coverage Requirements**:

**Tier 1 - Mandatory SSO**:
- ✅ All SaaS applications (Office 365, Salesforce, Slack, etc.)
- ✅ All web-based applications (internal portals, intranet)
- ✅ All cloud platform consoles (AWS, Azure, GCP management consoles)

**Tier 2 - Recommended SSO**:
- ⚠️ Legacy applications (if technically feasible)
- ⚠️ On-premises applications (if SAML/OAuth support available)

**Tier 3 - Excluded from SSO**:
- ℹ️ Applications without SSO support (document exception)
- ℹ️ Air-gapped systems (no network connection)
- ℹ️ Infrastructure devices (use device-specific authentication)

**SSO Adoption Metrics**:
- **Applications with SSO**: Target 90%+ of SaaS applications
- **Users accessing apps via SSO**: Target 95%+ of authentication events

**Audit Evidence**: SSO integration status (Workbook 1), application inventory with SSO status

### 5.2 Requirement: SSO Platform Requirements

**REQ-A85-011**: SSO platform **MUST** support modern authentication protocols and MFA integration.

**Required SSO Capabilities**:

1. **Protocol Support**:
   - **SAML 2.0**: Enterprise SSO (preferred for SaaS applications)
   - **OAuth 2.0 / OpenID Connect (OIDC)**: Modern authentication (preferred for APIs)
   - **WS-Federation**: Legacy enterprise SSO (if needed for older apps)

2. **MFA Integration**:
   - Native MFA support (built into SSO platform)
   - MFA prompt during SSO authentication
   - Adaptive authentication (risk-based MFA prompts)

3. **Application Catalog**:
   - Pre-built integrations for common SaaS apps (Office 365, Salesforce, etc.)
   - Custom app integration support (SAML/OAuth configuration)
   - Application gallery with 1000+ pre-configured integrations

4. **User Provisioning (SCIM)**:
   - Automatic user account creation in applications (via SCIM protocol)
   - User attribute synchronization (email, name, department, etc.)
   - Automatic deprovisioning when user leaves organization

5. **Session Management**:
   - Configurable session timeout
   - Global logout capability (logout from SSO = logout from all apps)
   - Session monitoring and analytics

**SSO Platform Options** (technology-agnostic):
- Azure Active Directory (Microsoft Entra ID)
- Okta
- Google Workspace
- Auth0
- Ping Identity
- ForgeRock

**Audit Evidence**: SSO platform capabilities documentation, protocol support matrix

### 5.3 Requirement: SSO Session Management

**REQ-A85-012**: SSO sessions **MUST** have appropriate timeout and logout procedures.

**Session Timeout Requirements**:

| Access Type | Idle Timeout | Max Session Duration | Rationale |
|-------------|--------------|---------------------|-----------|
| **Standard users** | 8 hours | 12 hours | Balance security and usability |
| **Privileged users** | 1 hour | 4 hours | Higher risk requires shorter sessions |
| **Sensitive data access** | 30 minutes | 2 hours | Extra protection for confidential data |
| **Public workstations** | 15 minutes | 1 hour | Shared computer risk |

**Session Security**:
- **Session tokens**: Cryptographically secure, random
- **Token storage**: HTTP-only, secure cookies (no JavaScript access)
- **Token revocation**: Immediate logout revokes all application sessions
- **Session hijacking protection**: Bind session to IP address and user agent

**Global Logout**:
- **User-initiated logout**: Logout from SSO portal logs out from all applications
- **Admin-initiated logout**: IT can force logout for user (security incident response)
- **Automatic logout**: After max session duration reached

**Audit Evidence**: Session timeout configuration, global logout functionality, session logs

---

## 6. Authentication Protocols and Standards

### 6.1 Requirement: Supported Authentication Protocols

**REQ-A85-013**: [Organization] **MUST** support modern authentication protocols and deprecate insecure legacy protocols.

**Supported Authentication Protocols**:

1. **SAML 2.0** (Security Assertion Markup Language):
   - **Use case**: Enterprise SSO for web applications
   - **Common for**: SaaS applications (Salesforce, ServiceNow, etc.)
   - **Security**: Strong (XML signatures, assertions)
   - **Status**: ✅ Supported, widely deployed

2. **OAuth 2.0** (Authorization Framework):
   - **Use case**: API authorization (delegated access)
   - **Common for**: Mobile apps, APIs, third-party integrations
   - **Security**: Strong (token-based, scoped access)
   - **Status**: ✅ Supported, preferred for APIs

3. **OpenID Connect (OIDC)** (built on OAuth 2.0):
   - **Use case**: Modern authentication and SSO
   - **Common for**: Web applications, mobile apps
   - **Security**: Strong (JWT tokens, identity layer on OAuth)
   - **Status**: ✅ Supported, preferred for new applications

4. **Kerberos**:
   - **Use case**: On-premises Active Directory authentication
   - **Common for**: Windows domain environments
   - **Security**: Strong (encrypted tickets)
   - **Status**: ✅ Supported for on-premises AD

5. **RADIUS** (Remote Authentication Dial-In User Service):
   - **Use case**: Network device authentication (802.1X, VPN)
   - **Common for**: Wireless networks, network equipment
   - **Security**: Moderate (shared secret-based, can be strengthened with EAP-TLS)
   - **Status**: ✅ Supported for network authentication

6. **LDAP/LDAPS** (Lightweight Directory Access Protocol):
   - **Use case**: Directory authentication queries
   - **Common for**: Legacy applications, directory lookups
   - **Security**: LDAP weak (plaintext), LDAPS strong (TLS-encrypted)
   - **Status**: ⚠️ LDAPS supported, plaintext LDAP deprecated

**Deprecated/Prohibited Protocols**:
- ❌ **Basic Authentication (HTTP Basic Auth)**: Credentials in Base64 (not encrypted)
- ❌ **NTLM** (NT LAN Manager): Legacy Windows authentication (Kerberos preferred)
- ❌ **Plaintext LDAP**: Credentials sent unencrypted

**Audit Evidence**: Protocol usage logs, legacy protocol deprecation status

### 6.2 Requirement: Secure Protocol Configuration

**REQ-A85-014**: Authentication protocols **MUST** be configured securely.

**SAML Configuration Requirements**:
- **Signature validation**: Always validate SAML assertions signatures
- **Certificate expiration monitoring**: Alert 30 days before certificate expires
- **Secure bindings**: Use HTTP-POST binding (avoid HTTP-Redirect for sensitive data)

**OAuth 2.0 / OIDC Configuration Requirements**:
- **PKCE required**: Use Proof Key for Code Exchange (PKCE) for public clients
- **State parameter**: Always use state parameter (CSRF protection)
- **Token encryption**: Store tokens securely (encrypted storage)
- **Scope limitation**: Grant minimum necessary OAuth scopes

**Kerberos Configuration Requirements**:
- **Encryption types**: Use AES256 or AES128 (disable DES, RC4)
- **Ticket lifetime**: Max 10 hours
- **Clock skew**: Max 5 minutes (time sync critical)

**RADIUS Configuration Requirements**:
- **Shared secret strength**: 32+ character random string
- **EAP methods**: Use EAP-TLS (certificate-based) or PEAP-MSCHAPv2
- **Avoid**: PAP, CHAP (weak authentication)

**Audit Evidence**: Protocol configuration audits, security settings documentation

---

## 7. Certificate-Based Authentication

### 7.1 Requirement: PKI for System-to-System Authentication

**REQ-A85-015**: Certificate-based authentication **MUST** be used for system-to-system and API authentication.

**Certificate Authentication Use Cases**:

1. **API Authentication**:
   - Client certificates for API access (mutual TLS)
   - Stronger than API keys (cryptographic authentication)
   - Use case: High-security APIs, financial transactions

2. **Service-to-Service Authentication**:
   - Certificates for service accounts (no passwords)
   - Automated certificate rotation
   - Use case: Microservices, cloud-native applications

3. **Device Authentication**:
   - Certificates for devices accessing network (802.1X with EAP-TLS)
   - Device identity tied to certificate (not password)
   - Use case: Corporate laptops, IoT devices

4. **VPN Authentication**:
   - Certificate-based VPN (in addition to username/password + MFA)
   - Device trust validation
   - Use case: Remote access VPN

**PKI Requirements**:
- **Certificate Authority (CA)**: Internal CA or trusted third-party CA
- **Certificate lifecycle**: Issuance, renewal (30 days before expiry), revocation (CRL/OCSP)
- **Key length**: RSA 2048-bit minimum, RSA 4096-bit or ECC P-256 recommended
- **Certificate validity**: Max 2 years (13 months for public trust)

**Audit Evidence**: Certificate inventory, certificate expiration monitoring, PKI documentation

### 7.2 Requirement: Certificate Management

**REQ-A85-016**: Certificates **MUST** be managed through defined lifecycle procedures.

**Certificate Lifecycle**:

1. **Issuance**:
   - Certificate requests approved by designated authority
   - Certificate subject matches intended use (CN, SAN fields)
   - Private key generated securely (on device, never transmitted)

2. **Renewal**:
   - Automated renewal 30 days before expiration
   - Alert if renewal fails
   - Monitor certificate inventory for approaching expiration

3. **Revocation**:
   - Revoke certificate immediately if:
     - Private key compromised
     - System decommissioned
     - Certificate misused
   - CRL (Certificate Revocation List) or OCSP (Online Certificate Status Protocol) published

4. **Storage**:
   - Private keys stored securely (hardware security module or encrypted storage)
   - Never store private keys in code repositories or configuration files
   - Access to private keys restricted to authorized systems/personnel

**Audit Evidence**: Certificate inventory with expiration dates, renewal logs, revocation logs

---

## 8. Biometric Authentication

### 8.1 Requirement: Biometric Authentication Standards

**REQ-A85-017**: Biometric authentication **MAY** be used with appropriate security controls.

**Supported Biometric Methods**:

1. **Fingerprint Recognition**:
   - **Devices**: Touch ID (Apple), Windows Hello (fingerprint)
   - **Use case**: Mobile device unlock, workstation login
   - **Security**: Liveness detection required (reject photos, molds)

2. **Facial Recognition**:
   - **Devices**: Face ID (Apple), Windows Hello (facial)
   - **Use case**: Mobile device unlock, workstation login
   - **Security**: 3D depth sensing required (reject photos)

3. **Iris/Retinal Scanning**:
   - **Devices**: Specialized readers
   - **Use case**: Physical access control
   - **Security**: Very high accuracy

**Biometric Security Requirements**:

1. **Liveness Detection**: MANDATORY
   - Detect and reject spoofing attempts (photos, videos, masks)
   - Active liveness (user performs action) or passive liveness (AI detection)

2. **Biometric Template Protection**:
   - **Never store raw biometric data** (fingerprint image, face image)
   - Store only biometric templates (mathematical representation)
   - Encrypt biometric templates at rest
   - Templates stored in secure enclave (iPhone Secure Enclave, TPM)

3. **Fallback Authentication**:
   - Always provide fallback to password/PIN
   - Biometric failure does not lock user out permanently
   - Max biometric attempts: 5, then require password

4. **Privacy Considerations**:
   - Biometric enrollment is user choice (not mandatory)
   - User can delete biometric templates anytime
   - Biometric data not shared with third parties

**Biometric Use Cases**:
- ✅ **Acceptable**: Device unlock (laptop, mobile), physical access
- ⚠️ **Caution**: High-security systems (biometrics not phishing-resistant like FIDO2)
- ❌ **Prohibited**: Biometric-only for privileged access (combine with password/token)

**Audit Evidence**: Biometric enrollment status, biometric authentication logs

---

## 9. Authentication Logging and Monitoring

### 9.1 Requirement: Authentication Event Logging

**REQ-A85-018**: All authentication events **MUST** be logged for security monitoring and forensic investigation.

**Required Authentication Logs**:

1. **Successful Authentication**:
   - Username, timestamp, source IP, user agent
   - Authentication method (password, MFA, SSO, certificate)
   - Application/system accessed

2. **Failed Authentication**:
   - Username (attempted), timestamp, source IP, user agent
   - Failure reason (invalid password, invalid MFA, account locked, etc.)
   - Number of consecutive failures

3. **MFA Events**:
   - MFA enrollment (user, timestamp, method)
   - MFA authentication (success/failure, method used)
   - MFA reset requests (user, admin, timestamp)

4. **SSO Events**:
   - SSO login (user, timestamp, source IP)
   - Application accessed via SSO (application name, timestamp)
   - SSO logout (user, timestamp, applications logged out)

5. **Account Lockout Events**:
   - Account lockout (username, timestamp, reason)
   - Account unlock (username, timestamp, admin who unlocked)

**Log Retention**:
- **Minimum retention**: 90 days online, 1 year archived
- **Extended retention**: 7 years for financial systems (regulatory requirement)
- **Compliance**: GDPR Article 5(1)(e) limits data retention (review retention period)

**Log Protection**:
- **Centralized logging**: Forward authentication logs to SIEM (Security Information and Event Management)
- **Tamper-proof**: Logs write-once (cannot be modified after creation)
- **Access control**: Only security team can access authentication logs

**Audit Evidence**: Authentication log samples, log retention configuration, SIEM integration

### 9.2 Requirement: Authentication Monitoring and Alerting

**REQ-A85-019**: Authentication events **MUST** be monitored for anomalies and security incidents.

**Critical Authentication Alerts**:

| Alert | Threshold | Priority | Response Time |
|-------|-----------|----------|---------------|
| **Brute force attack** | 10 failed logins in 5 minutes | High | 15 minutes |
| **Impossible travel** | Login from 2 locations >500km apart in <1 hour | High | 30 minutes |
| **Privileged account login** | Admin login from unusual location/time | Medium | 1 hour |
| **MFA bypass attempt** | Multiple MFA failures followed by success | High | 15 minutes |
| **Account lockout spike** | >5 accounts locked in 10 minutes | High | 15 minutes |
| **New device/location** | User login from never-before-seen device/IP | Low | 24 hours |

**Automated Responses**:
- **Account lockout**: After 5 failed password attempts (30-minute lockout)
- **IP blocking**: Block source IP after 20 failed attempts from that IP (1-hour block)
- **MFA challenge**: Require MFA for logins from new locations/devices
- **Session termination**: Terminate active sessions if account compromised

**Integration with SIEM**:
- Forward authentication logs to SIEM (A.8.16)
- Correlation with other security events (malware, network anomalies, etc.)
- Automated incident ticket creation for critical alerts

**Audit Evidence**: Alert rules configuration, alert response logs, SIEM integration documentation

---

## 10. Credential Compromise Response

### 10.1 Requirement: Compromised Credential Detection

**REQ-A85-020**: [Organization] **MUST** detect and respond to compromised credentials.

**Compromise Detection Methods**:

1. **Password Breach Detection**:
   - Continuous monitoring against Have I Been Pwned database
   - Azure AD Password Protection / Okta Compromised Credential Detection
   - Alert and force reset if user password found in breach

2. **Impossible Travel Detection**:
   - User logs in from New York, then Tokyo 1 hour later = impossible
   - Automated MFA challenge or session termination
   - Alert security team for investigation

3. **Anomalous Behavior Detection**:
   - User logs in at 3 AM (normally 9 AM - 5 PM) = suspicious
   - User accesses systems never accessed before = suspicious
   - Machine learning-based anomaly detection (Azure AD Identity Protection, Okta ThreatInsight)

4. **Dark Web Monitoring**:
   - Monitor dark web forums for [Organization] credentials
   - Third-party services (SpyCloud, Flare, Have I Been Pwned Domain Search)
   - Alert if credentials posted for sale

**Compromise Indicators**:
- ⚠️ Password found in public breach database
- ⚠️ Impossible travel (geographically impossible logins)
- ⚠️ Login from Tor exit node or known proxy
- ⚠️ Unusual time of access (outside business hours)
- ⚠️ Unusual systems accessed (never accessed before)
- ⚠️ Suspicious activity after authentication (data exfiltration, privilege escalation)

**Audit Evidence**: Compromise detection alerts, dark web monitoring reports

### 10.2 Requirement: Compromised Credential Response

**REQ-A85-021**: Compromised credentials **MUST** trigger immediate response procedures.

**Response Procedures**:

**Severity Level 1 - Confirmed Compromise** (Password in breach, active attacker):
1. **Immediate actions** (within 15 minutes):
   - Force password reset for affected user(s)
   - Terminate all active sessions
   - Disable account temporarily (until investigation complete)
   - Alert security team and user

2. **Investigation** (within 1 hour):
   - Review authentication logs (what was accessed?)
   - Review audit logs (what actions were performed?)
   - Determine scope of compromise (one user or multiple?)
   - Identify any data accessed or exfiltrated

3. **Remediation** (within 24 hours):
   - User enrolls new password (in person or verified identity)
   - User re-enrolls MFA (new device if old device compromised)
   - Review and revoke unnecessary access rights
   - Monitor account for 30 days for suspicious activity

4. **Lessons learned** (within 1 week):
   - Incident report documenting timeline, impact, remediation
   - Identify root cause (how was credential compromised?)
   - Implement preventive measures (MFA enforcement, user training, etc.)

**Severity Level 2 - Suspected Compromise** (Suspicious activity, no confirmation):
1. **Immediate actions** (within 1 hour):
   - Challenge user with MFA (if not already required)
   - Alert security team for monitoring
   - Flag account for enhanced logging

2. **Investigation** (within 4 hours):
   - Contact user to verify activity was legitimate
   - Review recent authentication and activity logs
   - If suspicious confirmed, escalate to Level 1 response

**Severity Level 3 - Anomaly Detection** (Unusual but possibly legitimate):
1. **Automated response**:
   - Challenge with MFA
   - Email notification to user ("Did you just log in from X location?")
   - Log event for future correlation

2. **User self-service response**:
   - User confirms legitimate or reports suspicious
   - If suspicious, user initiates password reset

**Breach Notification**:
- **Internal**: Notify affected users immediately
- **Regulatory**: Notify regulators if personal data compromised (GDPR 72-hour rule)
- **Customer**: Notify customers if customer data compromised

**Audit Evidence**: Compromise response logs, incident reports, user notifications, remediation status

---

## 11. Measurable Requirements and Audit Verification

### 11.1 Authentication Security Metrics

**Measurable requirements for audit verification**:

| Requirement | Metric | Target | Verification Method |
|-------------|--------|--------|---------------------|
| **MFA coverage - privileged** | % privileged users with MFA | 100% | Workbook 2 |
| **MFA coverage - remote access** | % remote users with MFA | 100% | VPN logs + MFA data |
| **MFA coverage - overall** | % all users with MFA | 90%+ | Workbook 2 |
| **Password strength** | % passwords meeting minimum length | 95%+ | Password policy audit |
| **Password breaches** | Passwords in breach database | 0 | Breach detection logs |
| **SSO adoption** | % apps integrated with SSO | 90%+ | Workbook 1 |
| **Legacy protocol usage** | Authentications via insecure protocols | <5% | Protocol usage logs |
| **Authentication failures** | Failed auth rate | <1% | Authentication logs |
| **MFA enrollment time** | Days to enroll MFA (privileged) | <7 days | Enrollment logs |

### 11.2 Audit Evidence Requirements

**For ISO 27001:2022 A.8.5 audit**:

1. **Policy and procedures**: This document (ISMS-POL-A.8.2-3-5-S2)
2. **Authentication inventory**: Workbook 1 (authentication mechanisms by system)
3. **MFA coverage**: Workbook 2 (MFA enrollment by user type, coverage metrics)
4. **Password policy**: Configuration screenshots, policy documentation
5. **SSO integration**: Application catalog with SSO status
6. **Authentication logs**: Sample logs showing successful/failed authentication events
7. **Breach detection**: Compromised password detection logs, forced resets
8. **Incident response**: Compromise response logs, incident reports

---

**END OF SECTION 2 (SECURE AUTHENTICATION REQUIREMENTS - A.8.5)**

**Next Section**: ISMS-POL-A.8.2-3-5-S3 (Privileged Access Requirements - A.8.2)

---

**VERSION HISTORY**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | IAM Security Lead | Initial secure authentication requirements (A.8.5) |

---

**APPROVAL STATUS: DRAFT - AWAITING REVIEW**
