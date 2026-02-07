**ISMS-OP-POL-A.8.24 — Use of Cryptography**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Use of Cryptography |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.24 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.8.24 — Use of cryptography

**Related Annex A Controls**:

| Control | Relationship to Cryptography |
|---------|------------------------------|
| A.5.12–13 Information classification and labelling | Determines encryption requirements per classification level |
| A.5.14 Information transfer | Encryption requirements for data in transit |
| A.5.23 Information security for cloud services | Encryption at rest and in transit for cloud-hosted data |
| A.5.31 Legal, statutory, regulatory requirements | Export controls, nFADP/GDPR encryption obligations |
| A.8.1 User endpoint devices | Full-disk encryption, device-level cryptographic controls |
| A.8.5 Secure authentication | Cryptographic protection of authentication credentials |
| A.8.10 Information deletion | Cryptographic erasure as a secure deletion method |
| A.8.13 Information backup | Backup encryption requirements |
| A.8.20 Network security | TLS/IPsec for network transport encryption |
| A.8.28 Secure coding | Use of approved cryptographic libraries in development |

**Related Internal Policies**:

- Information Classification and Handling Policy
- Information Transfer Policy
- Access Control Policy
- Backup Policy
- Secure Development Policy

---

# Use of Cryptography Policy

## Purpose

The purpose of this policy is to ensure the proper and effective use of cryptography to protect the confidentiality, integrity, and authenticity of information.

This policy supports Swiss nFADP (revDSG) and the Data Protection Ordinance (DSV) by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data). Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply. Encryption is a key technical measure for demonstrating compliance with data protection obligations under both frameworks.

## Scope

Confidential and personal information processed, stored, or transmitted on or in organisation-owned, managed, and controlled systems and applications deemed in scope by the ISO 27001 scope statement.

All employees and third-party users.

## Principle

Information is protected by cryptographic controls based on classification as set out in the Information Classification and Handling Policy and based on risk assessment.

Only organisation-approved encryption technology and processes shall be used.

The export of encryption technologies or encrypted data may be restricted by regulation, including Swiss export control provisions and the Wassenaar Arrangement. Personnel shall seek guidance from the legal department should export of cryptographic technologies or encrypted data be required.

Cryptographic key management is based on industry-recognised standards including NIST SP 800-57 and OWASP Key Management guidelines. Cryptographic keys are classified as Confidential.

---

## Cryptographic Controls

### Approved Algorithms and Key Lengths

The organisation shall use the following minimum cryptographic standards:

| Use Case | Algorithm | Minimum Requirement |
|----------|-----------|-------------------|
| Symmetric encryption | AES | 256-bit |
| Asymmetric encryption | RSA | 2048-bit minimum; 4096-bit recommended |
| Asymmetric encryption | ECDSA/ECDH | P-256 minimum; P-384 recommended |
| Hash functions | SHA-2 family | SHA-256 minimum; SHA-384/SHA-512 for high-assurance use |
| Digital signatures | RSA | 2048-bit minimum; 4096-bit recommended |
| Digital signatures | ECDSA | P-256 minimum |
| Key derivation | PBKDF2, scrypt, Argon2 | Per current NIST guidance |

**Prohibited algorithms:** MD5, SHA-1, DES, 3DES, RC4, RSA below 2048-bit. These shall not be used for any purpose.

The organisation shall monitor NIST post-quantum cryptography standards (FIPS 203 ML-KEM, FIPS 204 ML-DSA, FIPS 205 SLH-DSA) and plan migration as adoption timelines are established. A crypto-agility assessment shall be conducted to identify systems and data stores requiring PQC migration planning, prioritising long-lived keys and data with retention periods exceeding 10 years.

### Transport Layer Security

All network communications carrying confidential or personal data shall use encrypted transport:

- TLS 1.2 is the minimum acceptable version.
- TLS 1.3 is preferred and shall be used where supported.
- TLS 1.0 and TLS 1.1 shall be disabled on all systems.
- SSL (all versions) shall be disabled on all systems.
- Only cipher suites using AEAD (e.g., AES-GCM) shall be enabled where feasible.

### Mobile, Laptop, and Removable Media Encryption

Mobile devices, laptops, and removable media shall have full-disk encryption enabled at the hardware or operating system level.

- Device encryption shall not be disabled.
- Access to encrypted storage shall be protected by a password, passphrase, PIN, or biometric authentication.
- Only organisation-owned and managed removable media may be used to store confidential data.

### Email Encryption

Email shall not be used to transfer confidential or personal data in an unencrypted format, in line with the Information Transfer Policy.

Where confidential data must be sent via email, an encrypted attachment shall be used with a key length that meets the approved algorithm requirements above.

The organisation shall evaluate and approve an email encryption solution appropriate to its needs. Until a solution is deployed, encrypted file attachments with out-of-band key exchange shall be used as an interim measure.

### Web and Cloud Services Encryption

Web and cloud services that process, store, or transmit confidential or personal data shall implement TLS 1.2 at a minimum to protect data in transit.

All servers shall have a valid certificate issued by a recognised Certificate Authority. System owners are responsible for certificate renewal and ensuring systems are updated before expiry.

### Wireless Encryption

- WEP shall not be used.
- WPA3 is preferred for all wireless networks.
- WPA2 Enterprise mode with 802.1X authentication and AES encryption is the minimum acceptable standard.
- WPA2 Personal mode may be used for non-production networks with a minimum 16-character random passphrase and AES encryption.

### Backup Encryption

Backups containing confidential or personal data shall be encrypted using organisation-approved encryption technology meeting the minimum algorithm requirements above.

Backup encryption shall not rely solely on vendor-proprietary mechanisms without documented assurance of the encryption standard used.

### Database Encryption

Databases containing confidential information or personal data shall be encrypted at rest at either the database application layer or the disk/volume layer.

Where full-disk or volume encryption is used, cryptographic erasure (destruction of the encryption key) may be used as a valid secure deletion method, provided the risk is assessed and the approach is documented and approved.

### Data in Motion Encryption

The transfer of confidential and personal information shall use encrypted channels. Encryption is required for:

- Transport of sensitive files (SFTP, SCP, or equivalent encrypted transfer).
- All network traffic for remote access (VPN or equivalent).
- Database queries or web service calls transmitting sensitive data.
- Privileged access to network or server equipment (SSH; Telnet is prohibited).

### Bluetooth

Bluetooth shall not be used as a communication method for unencrypted confidential, personal, or otherwise sensitive data. See the Information Transfer Policy.

---

## Cryptographic Key Management

### Key Generation

Cryptographic keys shall be generated within cryptographic modules with at least FIPS 140-2 or FIPS 140-3 compliance, or equivalent validated assurance.

Any random values required for key generation shall be generated within the cryptographic module using a validated random bit generator.

Hardware cryptographic modules (HSMs) are preferred over software modules for protection of high-value keys.

### Key Distribution

Keys shall be transported using secure channels. Key material shall not be transmitted in plaintext over any network.

### Key Storage

- Keys shall never be stored in plaintext format.
- Keys shall be stored in a cryptographic vault, HSM, or cloud key management service (KMS).
- Keys shall not be hard-coded in source code, stored in configuration files in plaintext, or shared via email or messaging. This extends to API keys, tokens, service credentials, and other secrets — these shall be managed through a dedicated secrets management solution (e.g., AWS KMS, Azure Key Vault, HashiCorp Vault, or equivalent). Secrets do not require the same encryption-at-rest standards as data encryption keys but shall never be stored in plaintext and shall be rotated according to the key rotation periods above.
- Key encryption keys (KEKs) used to wrap stored keys shall be at least as strong as the keys they protect.
- Keys shall have integrity protections applied while in storage.

### Key Access Control

Access to cryptographic keys shall follow the principle of least privilege.

- Administrative and operational access to keys shall be separated where possible.
- Multi-factor authentication shall be required for key custodians.
- A register of individuals with access to key material shall be maintained.

### Key Rotation

Key rotation periods shall be defined based on key type, risk, and regulatory requirements.

Keys shall be rotated immediately upon suspected or confirmed compromise, regardless of scheduled rotation.

**Minimum key rotation periods:**

| Key Type | Maximum Lifetime |
|----------|------------------|
| TLS/SSL certificates | 398 days (per CA/Browser Forum baseline) |
| Symmetric data encryption keys (AES) | 2 years (or per NIST SP 800-57 cryptoperiod limits) |
| Asymmetric key pairs (RSA/ECDSA) | 3 years |
| API keys and service tokens | 90 days (extendable to 1 year with documented risk acceptance) |
| Database encryption keys | 1 year |

Shorter rotation periods may be required based on risk assessment or regulatory requirements.

### Key Escrow and Backup

Key material shall be backed up to enable recovery of encrypted data.

- Backup key storage shall be encrypted using at least the same assurance level as the operational keys.
- Signing keys shall not be escrowed.
- Encryption keys may be escrowed where business requirements justify it.

### Key Compromise and Recovery

A key compromise recovery plan shall be documented, tested annually, and maintained as a referenced procedure. The plan shall include:

- Contact information of personnel to notify and those responsible for recovery actions.
- The re-keying method and procedures.
- An inventory of all cryptographic keys and their usage.
- Identification of all data or other keys protected by the compromised key.
- Monitoring of re-keying operations to confirm completion.

### Trust Stores

Trust stores shall be protected against injection of unauthorised root certificates. Access controls shall be managed and enforced per entity and application.

A secure process for updating the trust store shall be implemented.

### Cryptographic Libraries

Only reputable cryptographic libraries shall be used that are actively maintained, regularly updated, and validated by third-party organisations (e.g., NIST/FIPS, Common Criteria).

Custom cryptographic implementations shall not be developed unless specifically approved by the CISO with documented justification.

---

## Optional: Payment Card Data Controls (PCI DSS)

*Applicable only if payment card data is processed and PCI scope exists.*

If PCI scope exists, the following additional requirements apply:

- Secret and private keys used to encrypt/decrypt cardholder data shall be stored encrypted with a key-encrypting key at least as strong as the data-encrypting key, stored separately from the data-encrypting key, or within a PTS-approved device or HSM.
- Cardholder data environment encryption shall meet PCI DSS requirements in addition to this policy.

---

## Evidence

The following evidence demonstrates compliance with this policy:

- **Cryptographic inventory** (algorithms, key lengths, protocols in use across systems) — *maintained quarterly by IT Security*
- **TLS configuration scan results** (e.g., SSL Labs, testssl.sh) — *monthly automated scans*
- **Certificate inventory and expiry monitoring records** — *automated monitoring, reviewed monthly*
- **KMS access logs and key usage audit trails** — *retained for 12 months, reviewed quarterly*
- **Key rotation records** — *logged in KMS, audited semi-annually*
- **Encryption configuration documentation** for databases, backups, endpoints — *reviewed annually*
- **Key compromise recovery plan** (documented and tested annually)

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, technical configuration audits, TLS/certificate scanning, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to cryptographic standards, emerging threats (including post-quantum cryptography developments), regulatory changes, and lessons learned from incidents.

---

# Areas of the ISO 27001 Standard Addressed

Use of Cryptography Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | 8.1 User endpoint devices |
| | **8.24 Use of cryptography** |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures for data protection |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 32 — Security of processing (encryption as appropriate measure) |
| ISO/IEC 27001:2022 | Annex A Control 8.24 — Use of cryptography |
| ISO/IEC 27002:2022 | Section 8.24 — Implementation guidance for cryptographic controls |
| NIST SP 800-57 | Key management recommendations |

---

<!-- QA_VERIFIED: 2026-02-07 -->
