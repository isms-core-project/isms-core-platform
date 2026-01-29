# Control A.8.24: Use of Cryptography
## POLICY REQUIREMENTS - SECTION 2.2
## Cryptographic Controls for Data Transmission

---

**Document ID**: ISMS-POL-A.8.24-S2.2  
**Title**: Use of Cryptography - Data Transmission  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Network Security Manager | Initial transmission security requirements |

**Review Cycle**: Annual (or upon protocol deprecation/vulnerability disclosure)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Network Security Manager / Infrastructure Lead
- Secondary: Chief Technology Officer (CTO) or IT Director
- Compliance: Legal/Compliance Officer (for data protection regulations)

**Distribution**: Network Administrators, System Administrators, Development Teams, Cloud/Infrastructure Teams, Data Protection Officers  
**Related Standards**: ISO/IEC 27001:2022 Control A.8.24, NIST SP 800-52 (TLS), BSI TR-02102-2 (TLS), BSI TR-02102-3 (IPsec), nFADP Art. 8, GDPR Art. 32

---

## 2.2 Cryptographic Controls for Data Transmission

### Purpose
This section defines mandatory cryptographic requirements for protecting data during transmission across networks, whether internal, external, public, or private.

---

### 2.2.1 HTTPS and TLS

#### External Web Services

**Requirements:**
- All externally accessible web services MUST use TLS encryption
- Valid certificates from trusted Certificate Authorities (CA) REQUIRED
- Self-signed certificates are PROHIBITED for production external services
- TLS version and cipher suite requirements per Section 2.1 (4.1.2) MUST be followed

**Configuration Standards:**
- TLS 1.3 PREFERRED
- TLS 1.2 ACCEPTABLE (minimum)
- TLS 1.1 and below PROHIBITED
- Perfect Forward Secrecy (PFS) REQUIRED
- HSTS (HTTP Strict Transport Security) header REQUIRED for all HTTPS sites

**HTTP to HTTPS Redirection:**
- All HTTP traffic MUST automatically redirect to HTTPS
- HSTS preload list inclusion RECOMMENDED for public-facing services

#### Internal Web Services

**Requirements:**
- Internal web services containing sensitive data (Confidential or Restricted classification) MUST use TLS
- Internal web services MAY use organizationally-issued certificates from internal CA
- Self-signed certificates acceptable ONLY for development/testing environments
- Production internal services SHOULD use certificates from trusted internal or public CA

**Risk-Based Exceptions:**
- Internal services with NO sensitive data and operating on isolated networks MAY operate without TLS
- Such exceptions MUST be documented with risk assessment and approved by CISO
- Compensating controls REQUIRED (network segmentation, access controls)

#### Certificate Management

**Certificate Inventory:**
- All TLS/SSL certificates MUST be maintained in a centralized inventory
- Inventory MUST include: certificate subject, issuer, expiration date, system location
- Inventory MUST be reviewed quarterly

**Expiration Monitoring:**
- Certificate expiration monitoring with automated alerts REQUIRED
- Alerts MUST trigger 30 days before expiration (minimum)
- Secondary alert at 14 days before expiration RECOMMENDED
- Expired certificates constitute a security incident

**Certificate Validity Periods:**

Public TLS Certificates (Internet-accessible servers):
- Current (until March 15, 2026): Maximum 398 days (CA/B Forum SC-062)
- **March 15, 2026 onwards**: Maximum 200 days (CA/B Forum Ballot SC-081v3)
- **March 15, 2027 onwards**: Maximum 100 days
- **March 15, 2029 onwards**: Maximum 47 days
- Domain Control Validation (DCV) reuse: Reduces from 398 days to 10 days by 2029

Private/Internal PKI Certificates:
- Maximum 825 days (not subject to CA/Browser Forum requirements)
- [Organization] may implement shorter lifetimes for enhanced security posture

**Certificate Renewal Requirements:**
- **Public CA certificates**: Automated renewal **REQUIRED** (manual renewal operationally infeasible at <100-day lifetimes)
- **Automation deadline**: Must be deployed before March 15, 2026
- Internal PKI automation: REQUIRED when certificate inventory >50 certificates
- Manual renewal exception: Internal PKI <50 certificates with documented CISO approval
- Minimum renewal lead time: 30 days before expiration
- Automated certificate renewal (e.g., ACME protocol, Let's Encrypt) RECOMMENDED

**Certificate Storage:**
- Private keys MUST be stored securely with restricted file system permissions
- Private keys MUST NOT be stored in version control systems
- Private keys MUST be protected with encryption at rest where possible
- Access to private keys MUST be logged and audited

**Certificate Revocation:**
- Compromised certificates MUST be revoked within 4 hours of discovery
- Revocation MUST be published via CRL and/or OCSP
- Certificate revocation testing MUST be performed during incident response drills

---

### 2.2.2 Email Security

#### Email Encryption

**Requirements:**
- Emails containing classified information (Confidential or Restricted) MUST be encrypted when sent externally
- Email encryption MUST use S/MIME or PGP/GPG standards
- Encryption MUST be applied before transmission (end-to-end encryption preferred)

**Approved Technologies:**
- S/MIME (Secure/Multipurpose Internet Mail Extensions) - PREFERRED
- PGP/GPG (Pretty Good Privacy / GNU Privacy Guard) - ACCEPTABLE
- Transport-only encryption (TLS for SMTP) - ACCEPTABLE for Internal classification only

**Internal Email:**
- Internal emails (within organizational domain) SHOULD use opportunistic TLS
- SMTP over TLS (STARTTLS) MUST be enabled on mail servers
- Unencrypted SMTP (port 25 without TLS) PROHIBITED for external connections

#### Digital Signatures

**Requirements:**
- Digital signatures RECOMMENDED for all outgoing external emails
- Digital signatures REQUIRED for:
  - Legal documents and contracts
  - Financial transactions and approvals
  - Official organizational announcements
  - Communications requiring non-repudiation

**S/MIME Implementation:**
- Email certificates MUST be issued from trusted CA or internal PKI
- Email certificates MUST use minimum RSA 2048-bit or ECDSA P-256
- Certificate validity MUST NOT exceed 1 year

#### Email Gateway Security

**Mail Server Requirements:**
- TLS MUST be enforced for connections to external mail servers where supported
- SPF (Sender Policy Framework) records MUST be published
- DKIM (DomainKeys Identified Mail) signing MUST be implemented
- DMARC (Domain-based Message Authentication, Reporting & Conformance) policy MUST be published

---

### 2.2.3 Secure File Transfer

#### Approved Protocols

**REQUIRED protocols for file transfer containing sensitive data:**
- **SFTP** (SSH File Transfer Protocol) - PREFERRED
- **FTPS** (FTP over TLS) - ACCEPTABLE
- **HTTPS** (HTTP over TLS) - ACCEPTABLE for web-based file transfer
- **SCP** (Secure Copy Protocol) - ACCEPTABLE

**PROHIBITED protocols:**
- **FTP** (File Transfer Protocol) without encryption - PROHIBITED
- **TFTP** (Trivial File Transfer Protocol) - PROHIBITED for sensitive data
- **Unencrypted HTTP** for file upload/download - PROHIBITED

#### Authentication Requirements

**File transfer systems MUST implement:**
- Strong authentication (password + key-based preferred)
- Multi-factor authentication (MFA) REQUIRED for external file transfer
- Service accounts MUST use key-based authentication (no passwords)
- Password authentication (if used) MUST meet organizational password policy

**Key Management for File Transfer:**
- SSH keys MUST be minimum 2048-bit RSA or Ed25519
- SSH keys MUST be rotated annually
- SSH keys MUST be rotated immediately upon personnel termination
- Private keys MUST be protected with passphrase encryption

#### File Transfer Security

**Requirements:**
- File transfer logs MUST be maintained for audit purposes
- Failed authentication attempts MUST trigger alerts after threshold
- File integrity verification (checksums/hashes) RECOMMENDED for critical transfers
- Large file transfers SHOULD use resume capability to prevent re-transmission

**External File Sharing:**
- External file sharing platforms MUST use end-to-end encryption
- File expiration and access controls MUST be configurable
- Download tracking and audit logging REQUIRED
- Password protection and link expiration RECOMMENDED for sensitive files

---

### 2.2.4 Remote Access

#### VPN (Virtual Private Network)

**Requirements:**
- All remote access to organizational networks MUST use encrypted VPN
- VPN MUST use approved encryption protocols:
  - **IPsec** with IKEv2 - APPROVED
  - **WireGuard** - APPROVED
  - **OpenVPN** with TLS 1.2+ - ACCEPTABLE
  - **PPTP, L2TP without IPsec** - PROHIBITED

**VPN Configuration:**
- Encryption: AES-256 or ChaCha20 REQUIRED
- Authentication: Certificate-based preferred, pre-shared keys acceptable with strong entropy
- Perfect Forward Secrecy (PFS) REQUIRED
- Split-tunneling SHOULD be disabled for accessing business systems
- VPN idle timeout MUST be configured (maximum 30 minutes)

**VPN Authentication:**
- Multi-factor authentication (MFA) REQUIRED for all VPN access
- Device certificates RECOMMENDED for additional security layer
- VPN access logs MUST be retained and reviewed

#### SSH (Secure Shell)

**Requirements:**
- SSH REQUIRED for all administrative and remote terminal access
- SSH protocol version 2 REQUIRED (SSH-1 PROHIBITED)
- Password authentication SHOULD be disabled (key-based preferred)
- Root login via SSH MUST be disabled

**SSH Configuration Standards:**
- Minimum key length: RSA 2048-bit or Ed25519
- Weak algorithms MUST be disabled (DSA, ECDSA with weak curves)
- SSH session timeout MUST be configured (maximum 15 minutes idle)
- SSH login attempts MUST be rate-limited

**SSH Key Management:**
- SSH keys MUST be rotated annually
- Authorized_keys files MUST be audited quarterly
- Unused SSH keys MUST be removed
- SSH keys for service accounts MUST be managed centrally

#### RDP (Remote Desktop Protocol)

**Requirements:**
- RDP connections MUST be encrypted using TLS
- RDP MUST NOT be directly exposed to the Internet
- RDP access MUST occur through:
  - VPN tunnel (PREFERRED), OR
  - Jump host/bastion server with MFA, OR
  - Zero-trust network access (ZTNA) solution

**RDP Security:**
- Network Level Authentication (NLA) REQUIRED
- RDP encryption level set to "High"
- MFA REQUIRED for RDP access to production systems
- RDP session recording RECOMMENDED for privileged access

---

### 2.2.5 API Security

#### API Authentication

**Requirements:**
- API authentication MUST use one of the following approved methods:
  - **OAuth 2.0** with JWT tokens - PREFERRED
  - **API keys** with minimum 256-bit entropy - ACCEPTABLE
  - **Mutual TLS (mTLS)** - ACCEPTABLE for service-to-service
  - **Basic Authentication over HTTPS** - ACCEPTABLE for internal APIs only

**PROHIBITED:**
- Unencrypted API authentication
- API keys in URL query parameters
- Long-lived credentials without rotation

#### API Key Management

**Requirements:**
- API keys MUST have minimum 256-bit entropy (cryptographically random)
- API keys MUST be treated as secrets (encrypted storage, no version control)
- API keys MUST have expiration periods:
  - User API keys: Maximum 90 days
  - Service account API keys: Maximum 90 days with automated rotation
- API keys MUST be scoped to minimum necessary permissions

**Key Rotation:**
- API keys MUST rotate quarterly (90-day maximum)
- Rotation process MUST allow grace period for client updates
- Deprecated keys MUST be revoked after grace period
- Key rotation MUST be logged and auditable

#### Token Management (OAuth/JWT)

**Requirements:**
- Access tokens MUST have short expiration (1 hour maximum)
- Refresh tokens MUST have reasonable expiration (24 hours maximum for user sessions)
- Tokens MUST be transmitted only over HTTPS
- Tokens MUST be stored securely (encrypted storage, HTTPOnly cookies for web)

**JWT Requirements:**
- JWT MUST be signed (HMAC-SHA256 minimum, RS256 preferred)
- JWT signature verification REQUIRED on all API endpoints
- Sensitive data SHOULD NOT be included in JWT payload (or encrypt payload)
- JWT "aud" (audience) and "iss" (issuer) claims MUST be validated

#### API Transport Security

**Requirements:**
- All API endpoints MUST use HTTPS with TLS 1.2+ (TLS 1.3 preferred)
- API endpoints MUST NOT be accessible over HTTP
- API Gateway or reverse proxy SHOULD enforce TLS and authentication
- Rate limiting MUST be implemented per API key or client

#### API Documentation

**Security Requirements:**
- API documentation MUST specify encryption requirements
- API authentication methods MUST be documented
- Security contact information MUST be provided (responsible disclosure)

---

### 2.2.6 Network Protocols

#### General Requirements

**Encrypted Protocols REQUIRED for:**
- Database connections (TLS for PostgreSQL/MySQL, encrypted connections for MSSQL)
- Message queues (AMQPS for RabbitMQ, SSL for Kafka)
- Service mesh communication (mTLS for Kubernetes service mesh)
- Inter-service communication containing sensitive data

**Protocol Migration:**
- Organizations MUST maintain inventory of unencrypted protocols in use
- Migration plan REQUIRED to replace unencrypted protocols
- Unencrypted protocols MUST be justified with risk assessment and compensating controls

#### Wireless Networks

**Requirements:**
- Wireless networks MUST use WPA3-Enterprise (802.1X authentication)
- WPA3-Personal acceptable for small offices (minimum WPA2-Personal)
- WEP and WPA (original) PROHIBITED
- Guest wireless networks MUST be isolated from organizational networks
- Wireless encryption keys MUST be rotated annually

---

### 2.2.7 Data in Transit - Cloud Environments

#### Cloud Provider Connections

**Requirements:**
- Connections to cloud provider APIs MUST use TLS 1.2+
- Cloud storage transfers MUST use encrypted protocols (HTTPS, SFTP)
- Private connectivity options RECOMMENDED (AWS PrivateLink, Azure Private Link, GCP Private Service Connect)
- VPN or dedicated circuits RECOMMENDED for high-volume or sensitive data transfers

#### Inter-Region and Cross-Cloud

**Requirements:**
- Data replication between cloud regions MUST be encrypted in transit
- Multi-cloud data transfers MUST be encrypted
- Cloud provider native encryption ACCEPTABLE if meeting organizational standards
- Customer-managed encryption keys (CMEK) PREFERRED for maximum control

---

## Compliance Verification

**This section SHALL be verified through:**
- Quarterly TLS/SSL configuration scanning
- Annual penetration testing of remote access solutions
- Bi-annual API security assessments
- Certificate inventory and expiration monitoring
- Network protocol audits

---

## Related Documents

- **ISMS-POL-A.8.24-S1** - Section 1: Purpose, Scope, Definitions
- **ISMS-POL-A.8.24-S2.1** - Use of Cryptographic Controls
- **ISMS-POL-A.8.24-S2.3** - Data Storage Requirements
- **ISMS-POL-A.8.24-S2.4** - Authentication Requirements
- **ISMS-POL-A.8.24-S2.5** - Compliance Requirements
- **ISMS-IMP-A.8.24** - Implementation & Compliance Status

---

**End of Section 2.2 - Cryptographic Controls for Data Transmission**

*"On the Internet, nobody knows you're a dog. Unless you're not using TLS."*  
*— Modified Peter Steiner cartoon wisdom*