<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.24-cryptographic-landscape-reference:framework:CTX:a.8.24 -->
**ISMS-CTX-A.8.24 — Cryptographic Landscape Reference**
**Industry Algorithm and Cipher Suite Overview (Non-ISMS Technical Reference)**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Cryptographic Landscape Reference |
| **Document Type** | Internal - Technical Reference (Not ISMS) |
| **Document ID** | ISMS-CTX-A.8.24 |
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
| 1.0 | [Date] | CISO | Initial policy for ISO 27001:2022 first certification |

**Review Cycle**: As needed (industry standards evolution)  
**Next Review Date**: [Date + 12 months]  
**Approvers**: Security Architecture / Cryptography SME (technical reference, no ISMS approval required)

**Distribution**: Security Engineering, System Architects, Development Teams (for awareness)

---

⚠️ **IMPORTANT – NON-ISMS TECHNICAL SUPPORT DOCUMENT**

This document is provided for informational and awareness purposes only.

- This document is NOT part of the Information Security Management System (ISMS).
- This document does NOT define mandatory cryptographic controls.
- This document does NOT establish binding requirements, deadlines, KPIs, or SLAs.
- This document does NOT mandate the use, prohibition, or configuration of specific cryptographic algorithms, ciphers, protocols, tools, or platforms.
- This document does NOT override or extend any ISMS policy.

All binding cryptographic requirements, obligations, and governance decisions are defined exclusively in **ISMS-POL-A.8.24 (Use of Cryptography)** and other approved ISMS documentation.

This document serves solely as a technical reference to:

- Describe commonly encountered cryptographic algorithms and cipher suites
- Track industry standards evolution and algorithm lifecycle status
- Support cryptographic agility awareness
- Inform technical discussions and future implementation planning
- **This document must not be used as audit evidence of implementation**

Use of this document does not imply implementation, compliance, or operational maturity.

**Critical Positioning Statement**:
This document intentionally exceeds the level of detail required for ISO/IEC 27001 policy documentation. Its purpose is technical awareness only. No auditor conclusions shall be drawn from the presence, absence, or classification of any algorithm, cipher, or parameter listed herein.

---

# Document Purpose and Scope

## Purpose

This document provides a technical overview of the cryptographic algorithm landscape commonly encountered in modern information systems. It is intended to support:

- Technical awareness of cryptographic options
- Understanding of algorithm lifecycle and maturity
- Context for cryptographic decision-making
- Future implementation planning discussions

## What This Document Is NOT

This document does NOT:

- Define [Organization]'s approved or prohibited algorithms
- Establish mandatory implementation requirements
- Create compliance obligations or audit criteria
- Replace ISMS-POL-A.8.24 policy requirements
- Mandate specific cipher suite configurations
- Establish key management procedures

## Relationship to ISMS

This document is a **non-binding technical reference**. All cryptographic control requirements are defined exclusively in ISMS-POL-A.8.24.

Implementation decisions are documented through separate procedures based on risk assessment, operational context, and regulatory requirements.

## Content Organization

This reference organizes cryptographic algorithms by function:

- Symmetric encryption (data confidentiality)
- Asymmetric encryption (key exchange, digital signatures)
- Hash functions (data integrity, authentication)
- TLS/SSL cipher suites (secure communications)
- Key lengths and algorithm maturity status

---

# Symmetric Encryption Algorithms

## Block Ciphers

Symmetric block ciphers commonly encountered in modern systems:

| Algorithm | Block Size | Key Lengths | Status | Common Use Cases |
|-----------|------------|-------------|--------|------------------|
| **AES** (Advanced Encryption Standard) | 128-bit | 128, 192, 256-bit | Modern, widely deployed | Data encryption, TLS, VPN, disk encryption |
| **ChaCha20** | 64-byte stream | 256-bit | Modern, mobile-optimized | TLS (mobile devices), VPN (WireGuard) |
| **3DES** (Triple DES) | 64-bit | 168-bit (effective 112-bit) | Legacy, deprecated | Legacy system support only |
| **DES** (Data Encryption Standard) | 64-bit | 56-bit | Obsolete, broken | Historical reference only |
| **Blowfish** | 64-bit | 32-448 bit | Legacy | Historical reference, replaced by AES |
| **Twofish** | 128-bit | 128, 192, 256-bit | Modern but less common | Alternative to AES |

**Industry Observations**:

- AES is the dominant standard for symmetric encryption globally
- ChaCha20 gaining adoption in resource-constrained environments
- 3DES deprecated by NIST (disallowed after 2023 in most contexts)
- DES considered cryptographically broken since late 1990s

## Block Cipher Modes of Operation

Common modes for operating block ciphers:

| Mode | Authentication | Parallelizable | Status | Notes |
|------|----------------|----------------|--------|-------|
| **GCM** (Galois/Counter Mode) | Yes (AEAD) | Yes (encryption & decryption) | Modern, recommended | Authenticated encryption, TLS 1.2+ default |
| **CCM** (Counter with CBC-MAC) | Yes (AEAD) | Partial | Modern | Used in constrained environments |
| **CTR** (Counter Mode) | No | Yes | Modern | Requires separate authentication (HMAC) |
| **CBC** (Cipher Block Chaining) | No | Partial | Legacy | Vulnerable to padding oracle attacks |
| **ECB** (Electronic Codebook) | No | Yes | Obsolete | Deterministic, not recommended |
| **XTS** | No | Yes | Modern | Disk encryption (BitLocker, dm-crypt) |

**Industry Observations**:

- AEAD modes (GCM, CCM) strongly preferred for new implementations
- CBC mode requires careful implementation to avoid vulnerabilities
- ECB mode provides insufficient security for most applications

## Stream Ciphers

| Cipher | Key Length | Status | Common Use Cases |
|--------|------------|--------|------------------|
| **ChaCha20-Poly1305** | 256-bit | Modern | TLS 1.3, mobile VPN, modern protocols |
| **RC4** (Rivest Cipher 4) | 40-2048 bit | Obsolete, broken | Historical reference only |
| **Salsa20** | 128, 256-bit | Modern | ChaCha20 predecessor |

**Industry Observations**:

- RC4 formally deprecated across all major protocols (TLS, WPA, etc.)
- ChaCha20 increasingly adopted as AES alternative for performance

---

# Asymmetric Encryption Algorithms

## Public Key Algorithms

Asymmetric algorithms commonly encountered:

| Algorithm | Key Lengths | Status | Primary Use Cases |
|-----------|-------------|--------|-------------------|
| **RSA** (Rivest-Shamir-Adleman) | 2048, 3072, 4096-bit | Modern (≥2048-bit) | TLS certificates, SSH, email encryption, code signing |
| **ECDSA** (Elliptic Curve DSA) | P-256, P-384, P-521 | Modern | TLS certificates, SSH, mobile/IoT, blockchain |
| **EdDSA** (Edwards-curve DSA) | Ed25519 (256-bit equivalent) | Modern | SSH keys, modern protocols, cryptocurrency |
| **DH** (Diffie-Hellman) | 2048, 3072, 4096-bit | Modern (≥2048-bit) | Key exchange (legacy) |
| **ECDH** (Elliptic Curve DH) | P-256, P-384, P-521, X25519 | Modern | TLS 1.2+, key exchange |
| **DSA** (Digital Signature Algorithm) | 2048, 3072-bit | Legacy | Older systems only, replaced by RSA/ECDSA |
| **RSA-1024** | 1024-bit | Obsolete, deprecated | Historical reference only |

**Industry Observations**:

- RSA-2048 minimum for new deployments (NIST, CA/Browser Forum)
- RSA-3072 increasingly adopted for long-term keys (5+ year lifetime)
- ECC (ECDSA, EdDSA) provides equivalent security with smaller key sizes
- Ed25519 gaining adoption for SSH and modern protocols

## Key Length Equivalence

Approximate security equivalence between algorithm families:

| Symmetric | RSA/DH | ECC | Hash | Security Bits |
|-----------|--------|-----|------|---------------|
| 3DES (2-key) | 1024 | 160 | SHA-1 | ~80 bits (deprecated) |
| AES-128 | 3072 | 256 (P-256) | SHA-256 | ~128 bits |
| AES-192 | 7680 | 384 (P-384) | SHA-384 | ~192 bits |
| AES-256 | 15360 | 521 (P-521) | SHA-512 | ~256 bits |

**Source**: NIST SP 800-57 Part 1 Rev. 5

---

# Hash Functions and Message Authentication

## Cryptographic Hash Functions

Hash functions commonly encountered:

| Algorithm | Output Size | Status | Common Use Cases |
|-----------|-------------|--------|------------------|
| **SHA-256** | 256-bit | Modern | Digital signatures, certificates, password storage (with KDF), blockchain |
| **SHA-384** | 384-bit | Modern | High-security applications, long-term signatures |
| **SHA-512** | 512-bit | Modern | High-security applications, password hashing (with KDF) |
| **SHA-3** (Keccak) | 224, 256, 384, 512-bit | Modern | Alternative to SHA-2, blockchain |
| **BLAKE2** | 256, 512-bit | Modern | High-performance hashing, password storage |
| **SHA-1** | 160-bit | Obsolete, broken | Historical reference only, deprecated 2017 |
| **MD5** | 128-bit | Obsolete, broken | Historical reference only, deprecated 2004 |

**Industry Observations**:

- SHA-256 minimum for new implementations (certificates, signatures)
- SHA-1 deprecated for certificates (2017), git migration ongoing
- MD5 considered cryptographically broken, suitable only for non-security use (checksums)

## Message Authentication Codes (MAC)

| Algorithm | Based On | Output Size | Status |
|-----------|----------|-------------|--------|
| **HMAC-SHA256** | SHA-256 | 256-bit | Modern |
| **HMAC-SHA384** | SHA-384 | 384-bit | Modern |
| **HMAC-SHA512** | SHA-512 | 512-bit | Modern |
| **Poly1305** | ChaCha20 | 128-bit | Modern (with ChaCha20) |
| **HMAC-SHA1** | SHA-1 | 160-bit | Legacy, being phased out |
| **HMAC-MD5** | MD5 | 128-bit | Obsolete |

## Password Hashing Functions

Specialized functions for password storage:

| Function | Type | Status | Notes |
|----------|------|--------|-------|
| **Argon2** (Argon2id) | Password KDF | Modern, recommended | Winner of Password Hashing Competition 2015 |
| **bcrypt** | Password KDF | Modern | Widely deployed, automatic work factor |
| **scrypt** | Password KDF | Modern | Memory-hard function |
| **PBKDF2-HMAC-SHA256** | Password KDF | Modern | NIST approved, lower cost factor |
| **SHA-256 (raw)** | General hash | Inappropriate | Too fast for password storage |
| **MD5 (raw)** | General hash | Obsolete | Unsuitable for passwords |

**Industry Observations**:

- Password hashing requires key derivation functions (KDFs) with work factor
- Raw hash functions (SHA-256, MD5) unsuitable for password storage
- Argon2id recommended for new implementations (OWASP)

---

# TLS/SSL Cipher Suites

**Important Note on Cipher Suite Listings**:
The TLS cipher suite examples below are illustrative and non-exhaustive. They are provided to explain common industry constructions and naming conventions only. They do not represent approved, required, or expected configurations within [Organization].

## TLS 1.3 Cipher Suites

TLS 1.3 simplified cipher suite design (5 standardized suites):

| Cipher Suite | Key Exchange | Bulk Cipher | Status |
|--------------|--------------|-------------|--------|
| **TLS_AES_256_GCM_SHA384** | ECDHE | AES-256-GCM | Modern, recommended |
| **TLS_AES_128_GCM_SHA256** | ECDHE | AES-128-GCM | Modern, recommended |
| **TLS_CHACHA20_POLY1305_SHA256** | ECDHE | ChaCha20-Poly1305 | Modern, mobile-optimized |
| **TLS_AES_128_CCM_SHA256** | ECDHE | AES-128-CCM | Modern, IoT/constrained |
| **TLS_AES_128_CCM_8_SHA256** | ECDHE | AES-128-CCM (8-byte tag) | Modern, constrained devices |

**Industry Observations**:

- TLS 1.3 removes cipher suite negotiation complexity
- All TLS 1.3 suites provide forward secrecy (ECDHE mandatory)
- All TLS 1.3 suites provide authenticated encryption (AEAD)

## TLS 1.2 Cipher Suites (Selected Common Examples)

TLS 1.2 cipher suite examples (non-exhaustive, descriptive only):

| Cipher Suite | Key Exchange | Authentication | Bulk Cipher | MAC | Status |
|--------------|--------------|----------------|-------------|-----|--------|
| **TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384** | ECDHE | RSA | AES-256-GCM | (AEAD) | Modern, widely deployed |
| **TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256** | ECDHE | RSA | AES-128-GCM | (AEAD) | Modern, widely deployed |
| **TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256** | ECDHE | RSA | ChaCha20-Poly1305 | (AEAD) | Modern, mobile |
| **TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384** | ECDHE | ECDSA | AES-256-GCM | (AEAD) | Modern, ECC certificates |
| **TLS_RSA_WITH_AES_256_GCM_SHA384** | RSA | RSA | AES-256-GCM | (AEAD) | Legacy, no forward secrecy |
| **TLS_RSA_WITH_AES_128_CBC_SHA256** | RSA | RSA | AES-128-CBC | SHA-256 | Legacy, padding oracle risk |
| **TLS_RSA_WITH_3DES_EDE_CBC_SHA** | RSA | RSA | 3DES-CBC | SHA-1 | Obsolete, deprecated |
| **TLS_RSA_WITH_RC4_128_SHA** | RSA | RSA | RC4 | SHA-1 | Obsolete, broken |

**Industry Observations**:

- ECDHE provides forward secrecy (recommended)
- AEAD modes (GCM, Poly1305) preferred over CBC + HMAC
- RSA key exchange (no ECDHE) lacks forward secrecy
- CBC mode vulnerable to padding oracle attacks if not carefully implemented

## Deprecated/Obsolete Protocols and Cipher Suites

| Protocol/Cipher | Deprecated | Reason |
|-----------------|------------|--------|
| **SSL v2** | 2011 | Multiple cryptographic flaws |
| **SSL v3** | 2015 | POODLE attack, weak encryption |
| **TLS 1.0** | 2020 | Outdated cryptography, BEAST attack |
| **TLS 1.1** | 2020 | Outdated cryptography |
| **RC4 cipher** | 2015 | Biases in keystream, practical attacks |
| **3DES cipher** | 2023 | Sweet32 attack, 64-bit block size |
| **Export-grade ciphers** | 1990s-2015 | Intentionally weakened (40-56 bit), broken |
| **NULL encryption** | Always | No encryption, authentication only |
| **Anonymous DH (ADH)** | Always | No authentication, MITM vulnerable |

---

# Key Lengths and Algorithm Lifecycle

## Commonly Referenced Key Lengths in Industry Guidance

Commonly referenced key lengths in industry guidance (NIST, BSI, ENISA):

| Algorithm Family | Minimum Key Length | Use Through | Notes |
|------------------|-------------------|-------------|-------|
| **RSA (signing, key exchange)** | 2048-bit | ~2030 | 3072-bit for keys >2030 |
| **RSA (long-term keys)** | 3072-bit | Beyond 2030 | Root CAs, code signing |
| **Diffie-Hellman** | 2048-bit | ~2030 | 3072-bit for future use |
| **ECDSA/ECDH** | P-256 (256-bit) | Beyond 2030 | P-384 for high-security |
| **AES** | 128-bit | Beyond 2030 | 256-bit for high-security |
| **Hash functions** | SHA-256 | Beyond 2030 | SHA-384 for high-security |

**Source**: NIST SP 800-57 Part 1 Rev. 5, BSI TR-02102-1

## Algorithm Lifecycle Status

Classification of algorithm maturity and adoption status:

| Status | Definition | Examples |
|--------|------------|----------|
| **Modern** | Current best practice, actively deployed | AES, RSA-2048+, ECDSA P-256+, SHA-256, TLS 1.3 |
| **Widely Used** | Mature, stable, broad deployment | TLS 1.2, RSA-2048, SHA-256, ChaCha20 |
| **Legacy** | Aging, being replaced, limited new deployment | 3DES, DSA, SHA-1 (non-certificate), TLS 1.1 |
| **Deprecated** | No longer recommended, phase-out in progress | SSL v3, TLS 1.0, RC4, MD5 signatures |
| **Obsolete** | Cryptographically broken or severely weakened | DES, MD5 (security use), RC4, SHA-1 (certificates) |
| **Emerging** | Standardized but limited deployment | Post-quantum algorithms (ML-KEM, ML-DSA) |

## Post-Quantum Cryptography Status

NIST Post-Quantum Cryptography (PQC) standardization:

| Algorithm | Type | Status (2024-2025) | Notes |
|-----------|------|-------------------|-------|
| **ML-KEM** (Kyber) | Key Encapsulation | FIPS 203 published 2024 | Key exchange, hybrid mode with ECDH |
| **ML-DSA** (Dilithium) | Digital Signature | FIPS 204 published 2024 | Signatures, hybrid mode with ECDSA/RSA |
| **SLH-DSA** (SPHINCS+) | Digital Signature | FIPS 205 published 2024 | Stateless hash-based signatures |
| **FN-DSA** (Falcon) | Digital Signature | Under consideration | Lattice-based, compact signatures |

**Industry Observations**:

- Post-quantum algorithms being standardized but not yet widely deployed
- Hybrid modes (PQC + classical) expected during transition period
- TLS 1.3 hybrid key exchange (X25519 + ML-KEM) under development
- Certificate authorities beginning PQC trial issuance

---

# Certificate Validity and Lifecycle Trends

## Historical Certificate Validity Evolution

Public TLS certificate maximum validity periods:

| Period | Maximum Validity | Authority |
|--------|------------------|-----------|
| Pre-2011 | No defined limit | Vendor discretion |
| 2011-2015 | 60 months (5 years) | CA/Browser Forum |
| 2015-2017 | 39 months (~3 years) | CA/Browser Forum Ballot 193 |
| 2017-2020 | 825 days (~27 months) | CA/Browser Forum Ballot 193 |
| 2020-present | 398 days (~13 months) | CA/Browser Forum Ballot SC-31 |

## Future Certificate Validity (Ballot SC-081v3)

CA/Browser Forum Ballot SC-081v3 (passed April 2025):

| Effective Date | Maximum Validity | DCV Reuse Period |
|----------------|------------------|------------------|
| March 15, 2026 | 200 days | 200 days |
| March 15, 2027 | 100 days | 100 days |
| March 15, 2029 | 47 days | 10 days |

**Industry Observations**:

- Certificate lifetimes reducing to improve security and agility
- Shorter lifetimes increase importance of automated lifecycle management
- Private/internal PKI not subject to CA/Browser Forum requirements

**Note on Internal PKI**: Internal certificate policies are determined by risk assessment and operational context and are not derived automatically from public-trust requirements. Organizations may choose shorter or longer lifetimes based on their specific security posture and operational needs.

---

# Standards and Reference Sources

## Authoritative Standards Bodies

| Organization | Focus Area | Key Publications |
|--------------|------------|------------------|
| **NIST** (National Institute of Standards and Technology) | Cryptographic standards (US) | FIPS 140-2/3, SP 800-series |
| **BSI** (Bundesamt für Sicherheit in der Informationstechnik) | Cryptographic standards (Germany) | TR-02102-1 through TR-02102-4 |
| **ENISA** (European Union Agency for Cybersecurity) | Cryptographic recommendations (EU) | Algorithm reports, guidelines |
| **IETF** (Internet Engineering Task Force) | Protocol standards | RFCs (TLS, SSH, IPsec) |
| **CA/Browser Forum** | Certificate authority standards | Baseline Requirements, ballots |
| **ISO/IEC JTC 1/SC 27** | Information security standards | ISO/IEC 18033 (encryption algorithms) |

## Key Reference Documents

**NIST Publications**:

- FIPS 140-2/140-3: Security Requirements for Cryptographic Modules
- NIST SP 800-52 Rev. 2: Guidelines for TLS Implementations
- NIST SP 800-57 Part 1 Rev. 5: Key Management Recommendations
- NIST SP 800-131A Rev. 2: Transitioning the Use of Cryptographic Algorithms
- NIST SP 800-175B Rev. 1: Guideline for Using Cryptographic Standards

**BSI Publications**:

- TR-02102-1: Cryptographic Mechanisms - Recommendations and Key Lengths
- TR-02102-2: Use of TLS
- TR-02102-3: Suitable Cryptographic Algorithms
- TR-02102-4: Use of Secure Shell (SSH)

**IETF RFCs**:

- RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3
- RFC 5246: The Transport Layer Security (TLS) Protocol Version 1.2
- RFC 8017: PKCS #1: RSA Cryptography Specifications Version 2.2
- RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA)

**CA/Browser Forum**:

- Baseline Requirements for TLS Certificates
- Extended Validation Guidelines
- Code Signing Requirements
- S/MIME Requirements

## Algorithm Deprecation Tracking

Organizations commonly monitor algorithm status through:

- NIST Cryptographic Algorithm Validation Program (CAVP)
- NIST Deprecated Algorithm List
- Browser vendor security policies (Chrome, Firefox, Safari, Edge root programs)
- CA/Browser Forum ballot tracking
- Vendor security bulletins (OpenSSL, Microsoft, Apple, etc.)

---

# Document Maintenance

## Update Triggers

This reference document may be updated when:

- Major algorithm standardization occurs (NIST, IETF RFCs)
- Significant algorithm deprecations announced
- TLS/SSL protocol updates published
- Post-quantum cryptography deployment milestones reached
- CA/Browser Forum baseline requirement changes

## Responsibility

**Document Owner**: Security Architecture / Cryptography SME  
**Review Frequency**: Annual or as needed  
**Update Authority**: Technical update (no ISMS approval process)

---

# Relationship to ISMS-POL-A.8.24

This document provides **technical context** that may inform:

- Cryptographic agility awareness (ISMS-POL-A.8.24 Section 2.6)
- Algorithm selection discussions during implementation planning
- Risk assessment of legacy cryptographic systems
- Understanding of industry standards evolution

This document does NOT:

- Override or extend ISMS-POL-A.8.24 requirements
- Establish mandatory algorithm selections
- Create compliance obligations
- Define approved/prohibited algorithms for [Organization]

All cryptographic control requirements are defined exclusively in ISMS-POL-A.8.24 and implemented through separate procedures based on risk assessment and operational context.

---

**END OF DOCUMENT**

*This is a technical reference document for awareness purposes only. It does not establish ISMS requirements or create compliance obligations.*

<!-- QA_VERIFIED: 2026-01-31 -->
