# Control A.8.24: Use of Cryptography
## SECTION 1
## Purpose, Scope, Definitions

---

**Document ID**: ISMS-POL-A.8.24-S1  
**Title**: Use of Cryptography - Purpose, Scope, Definitions  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Information Security Manager | Initial draft - foundation document |

**Review Cycle**: Annual (or upon significant regulatory/organizational changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO) or IT Director
- Compliance: Legal/Compliance Officer (for regulatory definitions and scope)
- Technical Review: Security Team Lead (for technical accuracy)

**Distribution**: All employees, IT management, security team, compliance officers  
**Related Standards**: ISO/IEC 27001:2022 Control A.8.24, ISO/IEC 27002:2022, nFADP, GDPR

---

## 1.1 Purpose

### 1.1.1 Policy Objectives

This policy establishes the organization's framework for the use of cryptographic controls to protect the confidentiality, integrity, authenticity, and non-repudiation of information assets.

**Primary Objectives:**

1. **Confidentiality Protection**: Ensure that sensitive information remains accessible only to authorized parties through appropriate encryption mechanisms
2. **Integrity Assurance**: Guarantee that information has not been altered or tampered with during storage or transmission
3. **Authentication**: Verify the identity of users, systems, and data sources through cryptographic mechanisms
4. **Non-Repudiation**: Provide proof of origin and delivery of information to prevent denial of actions
5. **Regulatory Compliance**: Meet legal, statutory, and contractual obligations related to data protection and cryptography
6. **Risk Management**: Implement cryptographic controls proportionate to identified information security risks

### 1.1.2 Business Drivers

**This policy supports the organization's business objectives by:**

- **Customer Trust**: Demonstrating commitment to protecting customer and partner data
- **Competitive Advantage**: Enabling secure digital business operations and services
- **Regulatory Compliance**: Meeting Swiss nFADP, EU GDPR, and industry-specific requirements
- **Business Continuity**: Protecting critical business information from unauthorized access or disclosure
- **Legal Protection**: Reducing liability through appropriate technical and organizational measures
- **Market Access**: Enabling business with clients requiring specific security certifications (ISO 27001, SOC 2, etc.)

### 1.1.3 Alignment with Information Security Management System (ISMS)

This cryptography policy is a component of the organization's Information Security Management System (ISMS) and:

- Implements ISO/IEC 27001:2022 Control A.8.24 (Use of Cryptography)
- Supports risk treatment plans identified through the organization's risk assessment process
- Integrates with complementary controls including access control (A.5.15-5.18), physical security (A.7.1-7.14), and operations security (A.8.1-8.34)
- Follows the Plan-Do-Check-Act (PDCA) continuous improvement cycle
- Is subject to periodic review, internal audit, and management review

---

## 1.2 Scope

### 1.2.1 Organizational Scope

**This policy applies to:**

- **All organizational entities**: Including parent company, subsidiaries, and affiliates under common ownership or control
- **All employees**: Full-time, part-time, temporary, and contracted personnel
- **All information assets**: Regardless of format (electronic or physical), location (on-premises, cloud, mobile), or classification level
- **All information systems**: Including but not limited to servers, workstations, mobile devices, network infrastructure, cloud services, and embedded systems
- **Third-party service providers**: Contractors, vendors, consultants, and partners who process, store, or transmit organizational information

**Geographic Coverage:**
- Primary operations in Switzerland (subject to Swiss Federal Act on Data Protection - nFADP)
- European operations subject to EU General Data Protection Regulation (GDPR)
- Global operations where local regulations impose additional cryptographic requirements

### 1.2.2 Technical Scope

**This policy covers cryptographic controls for:**

1. **Data in Transit**:
   - Network communications (TLS/SSL, IPsec, VPN)
   - Email transmission (S/MIME, PGP)
   - File transfers (SFTP, HTTPS)
   - API communications
   - Wireless communications (WPA3, 802.1X)

2. **Data at Rest**:
   - Database encryption (Transparent Data Encryption, column-level)
   - File system encryption (BitLocker, FileVault, LUKS)
   - Storage encryption (SAN, NAS, cloud storage)
   - Backup encryption
   - Archive encryption
   - Removable media encryption (USB drives, external disks)

3. **Authentication**:
   - User authentication (password hashing, multi-factor authentication)
   - System authentication (certificates, API keys)
   - Digital signatures
   - Public Key Infrastructure (PKI)
   - Certificate management

4. **Key Management**:
   - Cryptographic key generation
   - Key storage and protection
   - Key distribution and escrow
   - Key rotation and lifecycle management
   - Key destruction

### 1.2.3 Information Classification Scope

**Cryptographic requirements apply based on information classification:**

| Classification Level | Encryption Required | Strength Requirements |
|---------------------|--------------------|-----------------------|
| **Public** | Optional | N/A - low business impact |
| **Internal** | Recommended for transmission | Standard algorithms acceptable |
| **Confidential** | **REQUIRED** for storage and transmission | Strong algorithms (AES-256, RSA-3072+) |
| **Restricted** | **REQUIRED** with enhanced controls | Strongest algorithms (AES-256-GCM, RSA-4096+, HSM storage) |

*Note: Information classification is defined in ISMS-POL-A.5.12 (Classification of Information)*

### 1.2.4 Regulatory and Compliance Scope

**This policy addresses cryptographic requirements from:**

**Swiss Regulations:**
- Federal Act on Data Protection (nFADP - Bundesgesetz über den Datenschutz)
- Swiss Code of Obligations (Art. 328b - employer data protection obligations)

**European Union Regulations:**
- General Data Protection Regulation (GDPR) - Article 32 (Security of Processing)
- NIS2 Directive (Network and Information Security)

**Conditional Industry Requirements** (when applicable based on client contracts):
- Payment Card Industry Data Security Standard (PCI DSS) - Requirement 3 (Protect Stored Account Data)
- Swiss Financial Market Supervisory Authority (FINMA) requirements
- Health Insurance Portability and Accountability Act (HIPAA) - for U.S. healthcare data
- SOC 2 Type II requirements

**International Standards:**
- ISO/IEC 27001:2022 - Annex A Control 8.24
- ISO/IEC 27002:2022 - Information Security Controls
- NIST Cybersecurity Framework
- CIS Critical Security Controls

### 1.2.5 Exclusions

**The following are explicitly OUT OF SCOPE for this policy:**

- **Export-controlled cryptography**: Cryptographic implementations subject to export control regulations require separate legal review and approval
- **National security systems**: Systems designated for national security purposes (none currently in organizational scope)
- **Research and development**: Experimental or proof-of-concept cryptographic implementations in isolated lab environments (covered under separate R&D security policy)
- **Personal devices**: Employee-owned devices not used for organizational business purposes

---

## 1.3 Definitions

### 1.3.1 Cryptographic Terms

**Advanced Encryption Standard (AES)**  
A symmetric block cipher standardized by NIST (FIPS 197) using 128-bit, 192-bit, or 256-bit keys. Currently the most widely used encryption algorithm for protecting sensitive data.

**Asymmetric Cryptography** (Public Key Cryptography)  
Cryptographic system using paired keys: a public key for encryption/verification and a private key for decryption/signing. Examples: RSA, ECDSA, Ed25519.

**Authentication**  
The process of verifying the identity of a user, system, or entity using cryptographic mechanisms such as passwords, certificates, or digital signatures.

**Certificate Authority (CA)**  
A trusted entity that issues digital certificates used to verify the identity of certificate holders in a Public Key Infrastructure (PKI).

**Cipher**  
An algorithm for performing encryption or decryption. Modern ciphers include AES (symmetric) and RSA (asymmetric).

**Cipher Suite**  
A set of cryptographic algorithms used together in protocols like TLS, typically including key exchange, encryption, and message authentication algorithms.

**Cryptanalysis**  
The study of analyzing and breaking cryptographic systems to find weaknesses or vulnerabilities.

**Cryptographic Hash Function**  
A mathematical function that takes arbitrary input and produces a fixed-size output (hash/digest) in a way that is computationally infeasible to reverse. Examples: SHA-256, SHA-3.

**Cryptographic Key**  
A piece of information (parameter) that determines the output of a cryptographic algorithm. Keys must be kept secret (private/symmetric keys) or protected (public keys).

**Cryptographic Strength**  
A measure of the resistance of a cryptographic algorithm or key to cryptanalysis, typically expressed in bits of security (e.g., 128-bit, 256-bit).

**Decryption**  
The process of converting ciphertext (encrypted data) back to plaintext (readable data) using a cryptographic key.

**Deprecated Algorithm**  
A cryptographic algorithm that is no longer recommended for new implementations due to known weaknesses but may be temporarily permitted for legacy system compatibility. Examples: 3DES, SHA-1.

**Digital Signature**  
A cryptographic mechanism that provides authentication, integrity, and non-repudiation by creating a unique signature using the sender's private key that can be verified using their public key.

**Elliptic Curve Cryptography (ECC)**  
A public-key cryptography approach based on elliptic curve mathematics, offering equivalent security to RSA with smaller key sizes. Examples: ECDSA, Ed25519.

**Encryption**  
The process of converting plaintext (readable data) into ciphertext (unreadable data) using a cryptographic algorithm and key.

**End-to-End Encryption (E2E)**  
Encryption where data is encrypted on the sender's device and only decrypted on the recipient's device, with no intermediate parties able to access plaintext.

**Hash-based Message Authentication Code (HMAC)**  
A mechanism for message authentication using a cryptographic hash function combined with a secret key.

**Hardware Security Module (HSM)**  
A physical device that provides secure cryptographic key generation, storage, and operations in a tamper-resistant environment.

**Integrity**  
The property that data has not been altered or tampered with. Cryptographic hash functions and message authentication codes provide integrity verification.

**Key Derivation Function (KDF)**  
A cryptographic function that derives one or more secret keys from a secret value (such as a password or master key). Example: PBKDF2.

**Key Exchange**  
The process of securely establishing a shared cryptographic key between parties over an insecure channel. Examples: Diffie-Hellman, ECDH.

**Key Management**  
The set of processes and procedures for generating, distributing, storing, rotating, and destroying cryptographic keys throughout their lifecycle.

**Key Rotation**  
The process of replacing cryptographic keys at regular intervals or after specific events to limit the impact of potential key compromise.

**Key Strength** (Key Length)  
The size of a cryptographic key measured in bits. Larger keys generally provide stronger security. Examples: AES-256 (256-bit), RSA-4096 (4096-bit).

**Message Authentication Code (MAC)**  
A short piece of information used to authenticate a message and confirm its integrity. HMACs are a common type of MAC.

**Non-Repudiation**  
The assurance that someone cannot deny the authenticity or origin of a message or action. Digital signatures provide non-repudiation.

**Perfect Forward Secrecy (PFS)**  
A property of key exchange protocols ensuring that session keys are not compromised even if long-term private keys are later compromised. Required for TLS configurations.

**Plaintext**  
Unencrypted, readable data before encryption or after decryption.

**Prohibited Algorithm**  
A cryptographic algorithm that MUST NOT be used under any circumstances due to critical security weaknesses. Examples: DES, MD5, RC4, SSL 3.0.

**Public Key Infrastructure (PKI)**  
A framework of policies, procedures, hardware, and software for creating, managing, distributing, and revoking digital certificates and public keys.

**Quantum-Safe Cryptography** (Post-Quantum Cryptography)  
Cryptographic algorithms designed to be secure against attacks by quantum computers. Current subject of NIST standardization.

**RSA (Rivest-Shamir-Adleman)**  
A widely used asymmetric cryptographic algorithm for encryption and digital signatures. Requires minimum 2048-bit keys (3072-bit or 4096-bit recommended).

**Salt**  
Random data added to passwords before hashing to defend against rainbow table attacks and ensure unique hashes for identical passwords.

**Secure Sockets Layer (SSL)**  
Deprecated predecessor to TLS. All versions (SSL 2.0, 3.0) are PROHIBITED.

**Symmetric Cryptography** (Secret Key Cryptography)  
Cryptographic system where the same key is used for both encryption and decryption. Examples: AES, ChaCha20.

**Transport Layer Security (TLS)**  
Cryptographic protocol providing secure communications over networks. TLS 1.3 preferred, TLS 1.2 acceptable minimum.

**X.509 Certificate**  
A standard format for public key certificates used in TLS/SSL and other protocols, containing identity information and public key.

### 1.3.2 Organizational Roles

**Chief Information Security Officer (CISO)**  
Executive responsible for the organization's information security strategy and overall accountability for cryptography policy.

**Information Security Officer (ISO) / Security Manager**  
Operational lead responsible for day-to-day enforcement and monitoring of cryptography policy compliance.

**Cryptography Subject Matter Expert (SME)**  
Technical specialist responsible for evaluating cryptographic algorithms, reviewing implementations, and providing technical guidance.

**Key Management Administrator**  
Personnel responsible for the operational management of cryptographic keys and key management systems.

**System Owner**  
Individual accountable for a specific system or application, responsible for ensuring cryptographic controls are properly implemented.

---

## 1.4 Policy Framework Structure

### 1.4.1 Document Hierarchy

This policy is structured as a modular framework consisting of:

**Section 1 - Purpose, Scope, Definitions** (This Document)  
Foundation document establishing objectives, applicability, and terminology.

**Section 2 - Policy Requirements**  
- **Section 2.1**: Use of Cryptographic Controls (general requirements)
- **Section 2.2**: Data Transmission (network encryption, TLS, VPN)
- **Section 2.3**: Data Storage (encryption at rest, backups)
- **Section 2.4**: Authentication (password hashing, PKI, digital signatures)
- **Section 2.5**: Compliance Requirements (regulatory obligations)

**Section 3 - Roles & Responsibilities**  
Definition of accountability and responsibilities for cryptographic controls.

**Section 4 - Policy Governance**  
Lifecycle management, review processes, exceptions, and enforcement.

**Section 5 - Technical Annexes**  
- **Appendix A**: Approved Cryptographic Standards (technical reference)
- **Appendix B**: Exception Request Form Template
- **Appendix C**: Incident Response for Cryptographic Events
- **Appendix D**: Quick Reference Guide

### 1.4.2 Related Policies and Documents

This cryptography policy operates in conjunction with:

- **ISMS-POL-A.5.1**: Information Security Policy (master policy)
- **ISMS-POL-A.5.10**: Acceptable Use Policy
- **ISMS-POL-A.5.12**: Information Classification Policy
- **ISMS-POL-A.5.15-5.18**: Access Control Policies
- **ISMS-POL-A.5.23**: Information Security for Cloud Services
- **ISMS-POL-A.8.1-8.34**: Technological Controls
- **ISMS-IMP-A.8.24**: Use of Cryptography Implementation Assessment Suite

---

## 1.5 Policy Statement

### 1.5.1 Organizational Commitment

The organization is committed to:

1. **Protecting Information Assets**: Implementing appropriate cryptographic controls to protect the confidentiality, integrity, and availability of information assets
2. **Risk-Based Approach**: Selecting cryptographic controls proportionate to identified risks and information classification levels
3. **Regulatory Compliance**: Meeting all applicable legal, statutory, and contractual obligations related to data protection and cryptography
4. **Industry Best Practices**: Following recognized international standards and guidance from NIST, BSI, ENISA, and other authoritative sources
5. **Continuous Improvement**: Regularly reviewing and updating cryptographic standards to address emerging threats and technological evolution
6. **Transparency and Accountability**: Maintaining clear roles, responsibilities, and audit trails for cryptographic control implementation

### 1.5.2 Mandatory Requirements

All personnel and systems MUST:

1. Use **ONLY approved cryptographic algorithms** and key strengths as specified in Section 2 and Appendix A
2. **Encrypt Confidential and Restricted information** during transmission and storage
3. Implement **appropriate key management** practices including secure generation, storage, rotation, and destruction
4. Follow **certificate management** procedures for TLS/SSL certificates
5. **Report cryptographic incidents** including compromised keys, certificate expirations, or algorithm vulnerabilities
6. **Request exceptions** through the formal exception process for any deviation from this policy
7. Participate in required **security awareness training** on cryptographic controls

### 1.5.3 Prohibited Actions

The following are **STRICTLY PROHIBITED**:

1. Use of **cryptographically broken or deprecated algorithms** (DES, MD5, RC4, SHA-1, SSL 2.0/3.0, TLS 1.0/1.1)
2. Storing cryptographic keys in **plaintext or unprotected locations**
3. **Sharing or disclosing** private keys or symmetric encryption keys
4. Implementing **custom or proprietary cryptographic algorithms** without explicit CISO approval and external cryptographic review
5. **Circumventing or disabling** cryptographic controls on production systems
6. Using **weak or predictable** cryptographic keys (dictionary words, sequential numbers, default keys)
7. **Exporting cryptographic technology** without proper legal review and export control compliance

---

## 1.6 Governance and Compliance

### 1.6.1 Policy Ownership and Approval

- **Policy Owner**: Chief Information Security Officer (CISO)
- **Approval Authority**: CISO, CIO/IT Director, Legal/Compliance Officer
- **Review Cycle**: Annual or upon significant changes

### 1.6.2 Compliance Monitoring

Compliance with this policy will be verified through:

- **Automated configuration scanning** (quarterly)
- **Internal audits** (annual)
- **External audits** (as required for certifications)
- **Penetration testing** (annual)
- **Vulnerability assessments** (quarterly)

### 1.6.3 Non-Compliance Consequences

Violations of this policy may result in:

- Disciplinary action up to and including termination of employment
- Termination of contractor or vendor agreements
- Legal action if violations result in data breaches or regulatory penalties
- Mandatory remediation and additional security training

### 1.6.4 Exception Process

Exceptions to this policy must follow the formal exception request process defined in Section 4 (Policy Governance) and use the Exception Request Form (Appendix B).

---

## Document End

*For technical implementation details, refer to Section 2 (Policy Requirements) and Appendix A (Approved Cryptographic Standards).*

---

**Document Footer**  
ISMS-POL-A.8.24-S1 | Version 1.0 | [Approval Date] | Page {page} of {total_pages}