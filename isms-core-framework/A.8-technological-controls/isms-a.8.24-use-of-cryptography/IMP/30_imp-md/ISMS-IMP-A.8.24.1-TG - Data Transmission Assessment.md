**ISMS-IMP-A.8.24.1-TG - Data Transmission Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.24.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Data Transmission Cryptographic Controls |
| **Related Policy** | ISMS-POL-A.8.24, Section 3.2 (Data Transmission Encryption Requirements) |
| **Purpose** | Assess implementation of cryptographic controls for data-in-transit across 13 transmission categories (HTTPS/TLS, Email, File Transfer, Remote Access, APIs, Database, Wireless, Cloud) |
| **Target Audience** | Network Engineers, Security Engineers, System Administrators, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Data Transmission assessment workbook | ISMS Implementation Team |

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

# Instructions for Completing This Assessment

## How to Use This Document

This technical specification defines the structure, validation rules, and formulas for the Data Transmission Assessment Excel workbook (`ISMS-IMP-A.8.24.1_Data_Transmission_[DATE].xlsx`).

**Workbook Generation:** Python script `generate_a824_1_data_transmission_assessment.py` creates the workbook based on this specification.

**Assessment Completion Process:**

1. **Read each section** and determine if the technology/service applies to your organization
2. **Check Yes/No/Not Applicable** for each assessment question
3. **If Yes:** Complete the assessment table with your current implementation
4. **Mark Status:** ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant / N/A Not Applicable
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

- Configuration files or screenshots
- Network scan results (SSL Labs, nmap, testssl.sh)
- System documentation
- Vendor specifications
- Certificate inventory
- Audit logs
- Compliance reports

## Certificate Validity Requirements Update (CA/Browser Forum SC-081v3)

**CRITICAL - Updated Standards (Effective 2025):**

The CA/Browser Forum approved Ballot SC-081v3 which progressively reduces maximum certificate validity for publicly-trusted certificates:

| Effective Date | Maximum Validity | DCV Reuse Period | Notes |
|----------------|------------------|------------------|-------|
| **Until 15.03.2026** | **398 days** | 398 days | Current standard (CA/B Forum SC-062) |
| **15.03.2026 onwards** | **200 days** | 200 days | Automation REQUIRED |
| **15.03.2027 onwards** | **100 days** | 100 days | Bi-monthly renewals |
| **15.03.2029 onwards** | **47 days** | 10 days | Final target, automation mandatory |

**Certificate Renewal Automation:**

- **Public CA certificates:** Automated renewal REQUIRED before 15.03.2026
- **Rationale:** Manual processes will NOT scale for <100-day lifecycles
- **Implementation:** ACME protocol (Let's Encrypt, Sectigo, DigiCert, etc.)
- **Internal PKI:** Automation REQUIRED if certificate inventory >50 certificates

**Internal/Private PKI Certificates:**

- Maximum: 825 days (not subject to CA/Browser Forum requirements)
- Recommended: 180-365 days for enhanced security posture

**Reference:** CA/Browser Forum Ballot SC-081v3  
**URL:** https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/

---

# HTTPS/TLS Implementation

## External Web Services

**Policy Requirement:** All externally accessible web services MUST use TLS encryption with valid certificates from trusted Certificate Authorities 

**Assessment Question:**

**Does your organization have external-facing web services or websites?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 1.2
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Service Description | Current TLS Version | Certificate Source (CA) | Certificate Validity | Status | Evidence Location | Gap Description | Remediation Needed |
|---------------------|--------------------|-----------------------|---------------------|---------|-------------------|-----------------|-------------------|
| Example: Public websites, customer portals, APIs | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Number of external web services:** _________
- **Certificate expiration monitoring configured:** [ ] Yes [ ] No
- **Automated certificate renewal:** [ ] Yes [ ] No [ ] Planned
- **Certificate inventory maintained:** [ ] Yes [ ] No
- **Certificate automation status:** [ ] Fully automated [ ] Partially automated [ ] Manual (requires migration) [ ] Not applicable
- **Target automation completion date (if not automated):** _________
- **ACME-enabled CA in use:** [ ] Yes [ ] No [ ] Planned

---

**Compliance Checklist:**

- [ ] TLS 1.3 preferred OR TLS 1.2 minimum
- [ ] Valid certificates from trusted public CA
- [ ] Certificate validity: ≤398d (until 15.03.2026), ≤200d (15.03.2026+), ≤100d (15.03.2027+), ≤47d (15.03.2029+)
- [ ] Automated certificate renewal implemented or planned (REQUIRED for public CAs before 15.03.2026)
- [ ] Infrastructure readiness for short-lived certificates assessed (47-day lifecycle by 2029)
- [ ] Self-signed certificates NOT used in production
- [ ] HTTP automatically redirects to HTTPS
- [ ] HSTS (HTTP Strict Transport Security) header configured
- [ ] Strong cipher suites configured (per Appendix A)
- [ ] Weak/deprecated protocols disabled (TLS 1.1, TLS 1.0, SSL)
- [ ] Perfect Forward Secrecy (PFS) enabled
- [ ] Certificate expiration alerts configured (≥30-day advance, adjusted for shorter validity periods)

**Certificate Automation Readiness Assessment (REQUIRED before 15.03.2026):**

- [ ] ACME protocol support enabled (Let's Encrypt, Sectigo, DigiCert, etc.)
- [ ] Certificate lifecycle fully automated (issuance, installation, renewal, revocation)
- [ ] Alert thresholds adjusted for shorter validity periods (≥30 days for 200-day certs)
- [ ] Monitoring dashboards updated to track 47-day lifecycle readiness
- [ ] Documented process for emergency certificate replacement (<24 hour SLA)
- [ ] Staff trained on automated certificate management systems
- [ ] Runbook for automated renewal failures with escalation procedures

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Network segmentation/firewall restrictions
  - [ ] Enhanced monitoring and alerting
  - [ ] IP whitelisting/access restrictions
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________
- **Budget required:** [ ] Yes [ ] No  Amount: _________

---

## Internal Web Services

**Policy Requirement:** Internal web services containing sensitive data (Confidential or Restricted classification) MUST use TLS 

**Assessment Question:**

**Does your organization have internal web services (intranet, internal portals, internal APIs)?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 2
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Service Description | Data Classification | Current TLS Version | Certificate Type | Status | Evidence Location | Gap Description | Remediation Needed |
|---------------------|--------------------|--------------------|------------------|---------|-------------------|-----------------|-------------------|
| Example: Intranet, internal APIs, admin panels | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Number of internal web services:** _________
- **Data classification(s) handled:** [ ] Public [ ] Internal [ ] Confidential [ ] Restricted
- **Internal CA in use:** [ ] Yes [ ] No
- **Certificate management process documented:** [ ] Yes [ ] No
- **Internal certificate inventory count:** _________
- **Automation status (if >50 certificates):** [ ] Automated [ ] Manual [ ] In progress

---

**Compliance Checklist:**

- [ ] TLS 1.2+ for services with Confidential/Restricted data
- [ ] Valid certificates (internal CA acceptable for internal services)
- [ ] Services with non-sensitive data: Risk assessed and documented (if no TLS)
- [ ] Certificate inventory maintained for internal certificates
- [ ] Certificate expiration monitoring configured (same standards as public CA)
- [ ] Internal PKI certificates: Maximum 825 days validity (not subject to CA/B Forum)
- [ ] Internal TLS certificates: 180-365 days recommended for security posture
- [ ] Automation REQUIRED if certificate inventory >50 certificates
- [ ] Manual renewal exception: <50 certificates with documented CISO approval

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Isolated network segment (no internet access)
  - [ ] Enhanced access controls (authentication required)
  - [ ] Monitoring and logging
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# Email Security

## Email Encryption

**Policy Requirement:** Emails containing classified information (Confidential or Restricted) MUST be encrypted when sent externally 

**Assessment Question:**

**Does your organization send emails containing classified information to external parties?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 2.2
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Email System | Encryption Solution | Encryption Method | User Adoption Rate | Status | Evidence Location | Gap Description | Remediation Needed |
|--------------|--------------------|--------------------|-------------------|---------|-------------------|-----------------|-------------------|
| Example: Exchange, Gmail, other | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Encryption solution in use:** [ ] S/MIME [ ] PGP/GPG [ ] TLS-only [ ] Other: _______
- **PKI infrastructure for email:** [ ] Implemented [ ] Planned [ ] Not implemented
- **User training provided:** [ ] Yes [ ] No
- **Encryption enforced via policy/DLP:** [ ] Yes [ ] No

---

**Compliance Checklist:**

- [ ] S/MIME or PGP/GPG encryption available
- [ ] Users trained on when/how to encrypt sensitive emails
- [ ] PKI infrastructure in place for S/MIME
- [ ] Opportunistic TLS enabled for mail server connections
- [ ] STARTTLS enabled for SMTP

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] DLP blocks sensitive email externally
  - [ ] Secure portal for external file sharing
  - [ ] Policy prohibits emailing Confidential/Restricted externally
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

## Digital Signatures

**Policy Requirement:** Digital signatures RECOMMENDED for all external emails, REQUIRED for legal/financial/official communications 

**Assessment Question:**

**Does your organization use digital signatures for email?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 3
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Use Case | Signature Method | Certificate Source | Status | Evidence Location | Gap Description | Remediation Needed |
|----------|------------------|-------------------|---------|-------------------|-----------------|-------------------|
| Example: Legal docs, financial approvals, all external | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Digital signatures used for:** [ ] All emails [ ] Legal docs only [ ] Executives only [ ] Not used
- **Certificate source:** [ ] Public CA [ ] Internal PKI [ ] Both

---

**Compliance Checklist:**

- [ ] Digital signatures available for required use cases
- [ ] Email certificates issued from trusted CA or internal PKI
- [ ] Certificate validity ≤ 1 year
- [ ] Users trained on digital signature usage

---

# Secure File Transfer

## File Transfer Protocols

**Policy Requirement:** File transfers containing sensitive data MUST use encrypted protocols (SFTP, FTPS, HTTPS). Unencrypted FTP is PROHIBITED 

**Assessment Question:**

**Does your organization transfer files containing sensitive data to/from external parties or between systems?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 4
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Transfer Method/System | Protocol Used | Authentication Method | Data Classification | Status | Evidence Location | Gap Description | Remediation Needed |
|------------------------|---------------|----------------------|---------------------|---------|-------------------|-----------------|-------------------|
| Example: SFTP server, cloud storage, partner portal | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Approved protocols in use:** [ ] SFTP [ ] FTPS [ ] HTTPS [ ] SCP [ ] Other: _______
- **Prohibited protocols detected:** [ ] FTP [ ] TFTP [ ] None
- **Authentication:** [ ] Password [ ] Key-based [ ] MFA [ ] Certificate

---

**Compliance Checklist:**

- [ ] SFTP, FTPS, or HTTPS used for sensitive file transfers
- [ ] Plain FTP NOT used for sensitive data
- [ ] Strong authentication configured (key-based preferred)
- [ ] MFA required for external file transfer
- [ ] File transfer logging enabled
- [ ] SSH keys rotated annually (if SFTP used)

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Isolated network for legacy FTP
  - [ ] File content encryption (in addition to transport)
  - [ ] Access restricted to specific IP addresses
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# Remote Access Protocols

## VPN (Virtual Private Network)

**Policy Requirement:** All remote access to organizational networks MUST use encrypted VPN with approved protocols (IPsec, WireGuard, OpenVPN). MFA REQUIRED 

**Assessment Question:**

**Does your organization provide remote access via VPN?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 4.2
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| VPN Solution | Protocol | Encryption Algorithm | MFA Enabled | Status | Evidence Location | Gap Description | Remediation Needed |
|--------------|----------|---------------------|-------------|---------|-------------------|-----------------|-------------------|
| Example: Cisco AnyConnect, WireGuard, OpenVPN | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **VPN protocol in use:** [ ] IPsec/IKEv2 [ ] WireGuard [ ] OpenVPN [ ] Other: _______
- **Encryption algorithm:** _________
- **Number of VPN users:** _________
- **MFA solution:** [ ] TOTP [ ] Push notification [ ] SMS [ ] Hardware token [ ] None
- **Split-tunneling:** [ ] Disabled [ ] Enabled (with justification)

---

**Compliance Checklist:**

- [ ] Approved VPN protocol (IPsec/IKEv2, WireGuard, OpenVPN with TLS 1.2+)
- [ ] AES-256 or ChaCha20 encryption
- [ ] Perfect Forward Secrecy (PFS) enabled
- [ ] MFA required for all VPN connections
- [ ] Certificate-based authentication (preferred) OR strong pre-shared key
- [ ] VPN session timeout configured (≤30 minutes idle)
- [ ] Split-tunneling disabled (or documented exception)
- [ ] VPN access logs retained and reviewed

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Zero-trust network architecture (no VPN needed)
  - [ ] Additional authentication layer
  - [ ] Network segmentation post-VPN
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

## SSH (Secure Shell)

**Policy Requirement:** SSH REQUIRED for all administrative and remote terminal access. SSH protocol version 2 REQUIRED, password authentication SHOULD be disabled 

**Assessment Question:**

**Does your organization use SSH for remote system administration?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 4.3
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| System/Service | SSH Version | Authentication Method | Key Algorithm | Status | Evidence Location | Gap Description | Remediation Needed |
|----------------|-------------|----------------------|---------------|---------|-------------------|-----------------|-------------------|
| Example: Linux servers, network devices, containers | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **SSH protocol version:** [ ] SSHv2 only [ ] SSHv1 (legacy - prohibited)
- **Authentication method:** [ ] Key-based only [ ] Password allowed [ ] Both
- **SSH key types in use:** [ ] Ed25519 [ ] RSA 3072+ [ ] RSA 2048 [ ] ECDSA [ ] Other
- **Root login via SSH:** [ ] Disabled [ ] Enabled
- **SSH key rotation schedule:** [ ] Annual [ ] On personnel change [ ] No rotation

---

**Compliance Checklist:**

- [ ] SSH protocol version 2 only (SSHv1 disabled)
- [ ] Key-based authentication (password auth disabled preferred)
- [ ] Minimum key length: RSA 2048-bit or Ed25519
- [ ] Root login disabled
- [ ] SSH keys rotated annually
- [ ] Unused SSH keys removed
- [ ] Strong algorithms configured (per Policy Appendix A)
- [ ] Weak algorithms disabled (DSA, MD5, SHA-1)

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] SSH accessible only via VPN or jump host
  - [ ] Enhanced logging and monitoring
  - [ ] Rate limiting on SSH connection attempts
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

## RDP (Remote Desktop Protocol)

**Policy Requirement:** RDP connections MUST be encrypted using TLS. RDP MUST NOT be directly exposed to Internet. Access through VPN, jump host, or zero-trust gateway REQUIRED 

**Assessment Question:**

**Does your organization use RDP for remote Windows system access?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 5
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| System/Environment | RDP Access Method | TLS Encryption | NLA Enabled | Status | Evidence Location | Gap Description | Remediation Needed |
|--------------------|-------------------|----------------|-------------|---------|-------------------|-----------------|-------------------|
| Example: Windows servers, workstations, virtual desktops | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **RDP access method:** [ ] VPN required [ ] Jump host/bastion [ ] Direct (prohibited) [ ] Zero-trust gateway
- **Network Level Authentication (NLA):** [ ] Enabled [ ] Disabled
- **MFA for RDP:** [ ] Required [ ] Optional [ ] Not implemented
- **RDP encryption level:** [ ] High [ ] Client Compatible [ ] Low (prohibited)

---

**Compliance Checklist:**

- [ ] RDP accessed through VPN or jump host (NOT directly exposed)
- [ ] TLS encryption configured
- [ ] Network Level Authentication (NLA) enabled
- [ ] RDP encryption level set to 'High'
- [ ] MFA required for production system access
- [ ] RDP session recording (recommended for privileged access)

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] RDP accessible only from specific IP addresses
  - [ ] Strong password policy enforced
  - [ ] Account lockout after failed attempts
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# API Security

## API Authentication and Encryption

**Policy Requirement:** All API endpoints MUST use HTTPS with TLS 1.2+. API authentication MUST use approved methods (OAuth2, API keys with 256-bit entropy, mTLS). API keys MUST rotate quarterly 

**Assessment Question:**

**Does your organization have APIs (internal or external)?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 6
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| API Name/Service | Authentication Method | TLS Version | API Key Management | Token Expiry | Status | Evidence Location | Gap Description | Remediation Needed |
|------------------|----------------------|-------------|-------------------|--------------|---------|-------------------|-----------------|-------------------|
| Example: REST API, GraphQL, SOAP services | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **API authentication methods:** [ ] OAuth2/JWT [ ] API keys [ ] mTLS [ ] Basic Auth (HTTPS only)
- **API key storage:** [ ] Secrets manager [ ] Environment variables [ ] Hardcoded (prohibited)
- **API gateway in use:** [ ] Yes [ ] No
- **Rate limiting implemented:** [ ] Yes [ ] No

---

**Compliance Checklist:**

- [ ] All API endpoints use HTTPS with TLS 1.2+ (TLS 1.3 preferred)
- [ ] API endpoints NOT accessible over HTTP
- [ ] OAuth 2.0 with JWT tokens (preferred) OR API keys (256-bit entropy minimum)
- [ ] API keys stored in secrets manager (NOT in code/config files)
- [ ] API keys rotated quarterly (90-day maximum)
- [ ] Access tokens expire within 1 hour (for OAuth2)
- [ ] Refresh tokens expire within 24 hours
- [ ] Rate limiting implemented per API key or client
- [ ] API keys NOT passed in URL query parameters

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] API only accessible via internal network
  - [ ] IP whitelisting for API access
  - [ ] API gateway with additional security controls
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# Network Protocols

## Database Connections

**Policy Requirement:** Database connections MUST use encrypted protocols (TLS for PostgreSQL/MySQL, encrypted connections for MSSQL) 

**Assessment Question:**

**Does your organization have applications connecting to databases?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 6.2
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Database System | Connection Encryption | Certificate Validation | Status | Evidence Location | Gap Description | Remediation Needed |
|-----------------|----------------------|------------------------|---------|-------------------|-----------------|-------------------|
| Example: PostgreSQL, MySQL, MSSQL, Oracle | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Database types in use:** [ ] PostgreSQL [ ] MySQL/MariaDB [ ] MSSQL [ ] Oracle [ ] MongoDB [ ] Other: _______
- **Encryption enabled:** [ ] Yes [ ] No [ ] Partial
- **Certificate validation:** [ ] Enabled [ ] Disabled [ ] Not applicable

---

**Compliance Checklist:**

- [ ] Database connections encrypted (TLS/SSL)
- [ ] Certificate validation enabled (not "trust any certificate")
- [ ] Self-signed certificates only for internal databases (with proper CA)
- [ ] Unencrypted connections disabled or documented exception

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Database on isolated network segment
  - [ ] No sensitive data in database
  - [ ] Application-level encryption of sensitive fields
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

## Wireless Networks

**Policy Requirement:** Wireless networks MUST use WPA3-Enterprise or WPA2-Enterprise minimum. WEP and WPA (original) PROHIBITED 

**Assessment Question:**

**Does your organization have wireless networks?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 7
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Network SSID | Encryption Standard | Authentication Method | Status | Evidence Location | Gap Description | Remediation Needed |
|--------------|--------------------|-----------------------|---------|-------------------|-----------------|-------------------|
| Example: Corporate WiFi, Guest WiFi | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Corporate WiFi encryption:** [ ] WPA3-Enterprise [ ] WPA2-Enterprise [ ] WPA2-Personal [ ] Other
- **Guest WiFi:** [ ] Isolated network [ ] Captive portal [ ] Open (no encryption)
- **802.1X authentication:** [ ] Implemented [ ] Planned [ ] Not implemented
- **WiFi password strength (if PSK):** [ ] ≥20 characters [ ] <20 characters

---

**Compliance Checklist:**

- [ ] WPA3-Enterprise or WPA2-Enterprise for corporate networks
- [ ] 802.1X with EAP-TLS (certificate-based) preferred
- [ ] WPA2-Personal only with strong passphrase (≥20 characters)
- [ ] WEP and WPA (original) NOT used
- [ ] Guest wireless isolated from corporate network
- [ ] WiFi passwords rotated quarterly (for PSK networks)

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Network segmentation (guest WiFi only)
  - [ ] Strong WPA2-Personal passphrase (≥20 characters)
  - [ ] Network access control (NAC)
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# Cloud Data Transmission

## Cloud Provider Connections

**Policy Requirement:** Connections to cloud provider APIs MUST use TLS 1.2+. Private connectivity options (PrivateLink, Private Link, Private Service Connect) RECOMMENDED for high-volume or sensitive data 

**Assessment Question:**

**Does your organization use cloud services (AWS, Azure, GCP, SaaS)?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 8
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Cloud Provider/Service | Connection Method | Encryption | Status | Evidence Location | Gap Description | Remediation Needed |
|------------------------|-------------------|------------|---------|-------------------|-----------------|-------------------|
| Example: AWS, Azure, GCP, Office 365, Salesforce | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Connection type:** [ ] Public internet (TLS) [ ] VPN [ ] Private Link/PrivateLink [ ] Direct Connect/ExpressRoute
- **Data classification transmitted:** [ ] Public [ ] Internal [ ] Confidential [ ] Restricted

---

**Compliance Checklist:**

- [ ] TLS 1.2+ for all cloud API connections
- [ ] Private connectivity for Confidential/Restricted data (preferred)
- [ ] Cloud provider native encryption enabled
- [ ] Data encrypted in transit to/from cloud

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] VPN for cloud access
  - [ ] Application-level encryption before cloud transmission
  - [ ] Data classification does not require private connectivity
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# Overall Data Transmission Summary

## Compliance Summary

**Total Assessment Areas:** _______

| Status | Count | Percentage |
|--------|-------|------------|
| ✅ Compliant | | |
| ⚠️ Partial | | |
| ❌ Non-Compliant | | |
| N/A Not Applicable | | |

**Instructions for Completion:**

- Count the number of each status across all 13 assessment sections
- Calculate percentage: (Count / Total Assessment Areas) × 100
- Exclude N/A items from total when calculating compliance percentage
- Target: ≥90% Compliant for mature ISMS

## Critical Gaps Identified

List the most critical gaps that require immediate attention:

1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________

**Guidance:**

- Critical gaps typically include:
  - ❌ Non-Compliant items with Confidential/Restricted data exposure
  - Expired or soon-to-expire certificates (<30 days)
  - Prohibited protocols in active use (FTP, WEP, TLS 1.0/1.1)
  - Missing MFA on critical systems (VPN, production RDP)
  - Lack of certificate automation approaching March 2026 deadline
  - Self-signed certificates on production external services

## Top Remediation Priorities

| Priority | Gap Description | Target Date | Responsible Person |
|----------|-----------------|-------------|-------------------|
| **High** | | | |
| **High** | | | |
| **Medium** | | | |

**Priority Definitions:**

- **High:** Security risk, compliance violation, or operational failure imminent
- **Medium:** Compliance gap with planned remediation, low immediate risk
- **Low:** Best practice improvement, no compliance impact

---

# Evidence Register

**List all evidence files/documents referenced in this assessment:**

| Evidence ID | Description | Location | Date Collected |
|-------------|-------------|----------|----------------|
| EV-1.1-001 | SSL Labs report for www.example.com | /evidence/a824_1/ | DD.MM.YYYY |
| EV-1.1-002 | Certificate export for www.example.com | /evidence/a824_1/ | DD.MM.YYYY |
| | | | |
| | | | |

**Evidence Naming Convention:**
```
EV-[Section]-[System]-[Date]-[Type].[ext]
```

**Examples:**

- `EV-1.1-PublicWebsite-20260115-SSLLabsReport.pdf`
- `EV-4.2-SSHServers-20260115-KeyAlgorithms.txt`
- `EV-6.2-CorporateWiFi-20260115-ControllerConfig.png`

**Evidence Types:**

- Configuration files (sanitized)
- Screenshots (timestamped)
- Scan results (SSL Labs, testssl.sh, nmap)
- Certificate exports (.pem, .cer)
- Policy documents
- Risk assessments
- Compliance reports
- Audit logs (sample extracts)

**Evidence Storage:**

- **Location:** [Organization's evidence repository path]
- **Retention:** Audit cycle + 1 year minimum
- **Access Control:** Restricted to security team and auditors
- **Sensitivity:** Mark according to data classification

**Quality Criteria:**

- Timestamped (date/time visible)
- Complete (not cropped unless sensitive)
- Attributable (clear which system)
- Verifiable (auditor can reproduce)
- Protected (stored securely, sanitized if needed)

---

# Approval and Sign-Off

## Assessment Summary

**Assessment Document:** ISMS-IMP-A.8.24.1 - Data Transmission Assessment  
**Assessment Period:** From __________ To __________  
**Overall Compliance Rate:** _______ % (from Summary Dashboard Section 8.1)  
**Assessment Status:** [ ] Draft [ ] Final [ ] Requires remediation [ ] Re-assessment required

**Key Findings:**

- Number of systems assessed: _______
- Compliant systems: _______
- Systems requiring remediation: _______
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
I certify that this assessment was completed with due diligence, all information is accurate to the best of my knowledge, and all evidence has been collected and verified.

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

- [ ] Approved - Compliance posture acceptable, remediation plans approved
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

- Major infrastructure changes
- Security incidents involving encryption
- Policy updates
- Regulatory changes
- Failed audit findings
- Certificate automation deadline approaching (15.03.2026)

**Interim Monitoring:**

- Certificate expiration monitoring: Continuous (automated alerts)
- Configuration changes: Documented and verified
- New systems: Assessed before production deployment
- Remediation progress: Tracked monthly

---

## Distribution List

This assessment shall be distributed to:

- [ ] Chief Information Security Officer (CISO)
- [ ] Information Security Officer (ISO)
- [ ] Network Engineering team
- [ ] System Administration team
- [ ] Compliance team
- [ ] Internal Audit
- [ ] IT Management
- [ ] Other: _______________________

**Storage Location:**

- **ISMS Repository:** `ISMS/Controls/A.8.24_Use_of_Cryptography/Assessments/`
- **Filename:** `ISMS-IMP-A.8.24.1_Data_Transmission_[DATE]_APPROVED.xlsx`

---

# APPENDIX: Technical Notes for Workbook Developers

## A.1 Excel Workbook Structure

**Sheet Names (16 sheets total):**
1. Instructions & Legend
2. 1.1 External HTTPS-TLS
3. 1.2 Internal HTTPS-TLS
4. 2.1 Email Encryption
5. 2.2 Digital Signatures
6. 3.1 File Transfer Protocols
7. 4.1 VPN
8. 4.2 SSH
9. 4.3 RDP
10. 5.1 API Security
11. 6.1 Database Connections
12. 6.2 Wireless Networks
13. 7.1 Cloud Transmission
14. Summary Dashboard
15. Evidence Register
16. Approval Sign-Off

## A.2 Data Validation Rules

**Status Dropdown:**

- Formula: `"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"`
- Applied to: Status column in all assessment sheets
- Allow blank: No

**Remediation Needed Dropdown:**

- Formula: `"Yes,No"`
- Applied to: Remediation Needed column in all assessment sheets
- Allow blank: No

**Response Dropdown (Assessment Question):**

- Formula: `"Yes,No,Not Applicable"`
- Applied to: Response field for each section's assessment question
- Allow blank: No

**Certificate Automation Status (Section 1.1):**

- Formula: `"Fully automated,Partially automated,Manual (requires migration),Not applicable (internal only)"`
- Applied to: Certificate automation status field
- Allow blank: No

**Checklist Items:**

- Formula: `"Yes,No,N/A"`
- Applied to: All compliance checklist Status columns
- Allow blank: No

## A.3 Conditional Formatting

**Status Column:**

- ✅ Compliant: Green fill (RGB: 198, 239, 206)
- ⚠️ Partial: Yellow fill (RGB: 255, 235, 156)
- ❌ Non-Compliant: Red fill (RGB: 255, 199, 206)
- N/A: No special formatting

**Certificate Validity Cells (Section 1.1):**

- If value >398 and date <15.03.2026: Yellow fill (warning - approaching deadline)
- If value >398 and date ≥15.03.2026: Red fill (non-compliant with SC-081v3)
- If value >200 and date ≥15.03.2026: Red fill
- If value >100 and date ≥15.03.2027: Red fill
- If value >47 and date ≥15.03.2029: Red fill

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

- Assessment data entry tables (yellow fill)
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

**Compliance Percentage Calculation:**
```excel
=COUNTIF(DataRange,"✅ Compliant")/COUNTA(DataRange)*100
```

**Critical Gaps Count:**
```excel
=COUNTIF(DataRange,"❌ Non-Compliant")
```

**Sections Requiring Attention:**
```excel
=COUNTIFS(DataRange,"⚠️ Partial")+COUNTIFS(DataRange,"❌ Non-Compliant")
```

**Certificate Automation Status (Section 1.1):**
```excel
=IF(OR('1.1 External HTTPS-TLS'!AutomationStatus="Manual",'1.1 External HTTPS-TLS'!AutomationStatus="Partially automated"),"ACTION REQUIRED before 15.03.2026","Compliant")
```

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

**Workbook Generation Script:** `generate_a824_1_data_transmission_assessment.py`

**Key Functions:**

- `create_workbook()`: Initialize workbook and sheets
- `setup_styles()`: Define cell styles, fonts, fills
- `get_column_definitions(section_key)`: Return column widths per section
- `create_assessment_sheet()`: Generic sheet generator with validation
- `create_summary_dashboard()`: Compliance calculations
- `create_evidence_register()`: Evidence tracking
- `create_approval_signoff()`: Approval workflow

**Customization Points (marked with `# CUSTOMIZE:` in script):**

- Sheet names (if organizational naming differs)
- Dropdown options (if additional statuses needed)
- Data validation rules (if custom compliance criteria)
- Conditional formatting thresholds (if different color coding)

**Quality Assurance Script:** `excel_sanity_check_a824_1.py`

- Validates sheet structure matches specification
- Checks data validation rules are applied correctly
- Verifies conditional formatting ranges
- Tests formula accuracy
- Reports any discrepancies between script and specification

## A.8 Version Control

**Workbook Versioning:**

- Filename format: `ISMS-IMP-A.8.24.1_Data_Transmission_YYYYMMDD.xlsx`
- Version tracking in Instructions & Legend sheet
- Document Control section updated with each revision

**Change Log:**

- v1.0: Initial workbook structure
- v2.0: Updated certificate validity requirements (SC-081v3), added automation readiness assessment, added internal PKI distinction

**Backward Compatibility:**

- v2.0 workbooks can be opened in Excel 2016+
- v1.0 workbooks should be migrated to v2.0 to reflect updated certificate standards
- Migration script available: `normalize_assessment_files_a824.py`

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Document Assembly Instructions

**To create the complete ISMS-IMP-A.8.24.1 v1.0 document:**

1. **Document Control** (from PART I file, lines 1-30)
2. **PART I: USER COMPLETION GUIDE** (from PART I file, lines 31-440)
3. **PART II: TECHNICAL SPECIFICATION - File 1** (this file, all content)
4. **PART II: TECHNICAL SPECIFICATION - File 2** (next file, all content)

**Final Document Structure:**
```
ISMS-IMP-A.8.24.1 - Data Transmission Assessment v1.0

├── Document Control (Metadata, Version History)
│
├── PART I: USER COMPLETION GUIDE (~440 lines)
│   ├── 1. Assessment Overview
│   ├── 2. Prerequisites
│   ├── 3. Assessment Workflow
│   ├── 4. Question-by-Question Guidance
│   ├── 5. Evidence Collection
│   ├── 6. Common Pitfalls
│   ├── 7. Quality Checklist
│   └── 8. Review & Approval
│
└── PART II: TECHNICAL SPECIFICATION (~750 lines)
    ├── Instructions (with SC-081v3 update notice)
    ├── 1. HTTPS/TLS Implementation
    │   ├── 1.1 External Web Services (UPDATED - SC-081v3)
    │   └── 1.2 Internal Web Services (UPDATED - Internal PKI)
    ├── 2. Email Security
    ├── 3. Secure File Transfer
    ├── 4. Remote Access Protocols
    ├── 5. API Security
    ├── 6. Network Protocols
    ├── 7. Cloud Data Transmission
    ├── 8. Overall Summary
    ├── 9. Evidence Register
    ├── 10. Approval and Sign-Off
    └── Appendix: Technical Notes for Developers
```

**Quality Checks Before Finalizing:**

- [ ] All merge instructions removed
- [ ] Document Control version shows 2.0
- [ ] Version History documents v1.0 → v2.0 changes
- [ ] Certificate validity references SC-081v3 timeline throughout
- [ ] All dates in DD.MM.YYYY format
- [ ] Cross-references accurate (section numbers, policy references)
- [ ] No placeholder text remains (all [Organization] appropriate)
- [ ] Technical appendix matches Python script version

---

**END OF SPECIFICATION**

---

*"While asleep, I had an unusual experience. There was a red screen formed by flowing blood, and I was observing it. Suddenly a hand began to write on the screen."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
