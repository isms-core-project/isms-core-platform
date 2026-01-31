# Control A.8.24: Use of Cryptography
## APPENDIX A
## Approved Cryptographic Standards (Technical Reference)

---

**Document ID**: ISMS-POL-A.8.24-S5.A  
**Title**: Use of Cryptography - Approved Cryptographic Standards (Technical Reference)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Security Team Lead | Initial technical reference framework |

**Review Cycle**: Semi-Annual (Every 6 months)  
**Next Review Date**: [Approval Date + 6 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Team Lead / Cryptography Subject Matter Expert (mandatory)
- Secondary: Chief Technology Officer (CTO) or IT Director
- Compliance: Legal/Compliance Officer (for regulatory alignment with nFADP, GDPR)

**Distribution**: IT Security Team, System Administrators, Development Teams, Infrastructure Teams, Architecture Review Board  
**Related Standards**: ISO/IEC 27001:2022 Control A.8.24, NIST SP 800-175B, NIST SP 800-57, BSI TR-02102 series, ENISA Cryptographic Guidelines, FIPS 140-2/3

**Technical Review Notes**:
- This document contains time-sensitive cryptographic standards
- Deprecated algorithms must be tracked and communicated immediately
- Post-quantum cryptography readiness requires ongoing monitoring
- BSI TR-02102 and NIST publications reviewed at each cycle
---

## Purpose of This Appendix

This appendix provides detailed technical specifications for approved cryptographic algorithms, key lengths, protocols, and configurations. This is the authoritative reference for technical implementation of cryptographic controls.

**Important Notes:**
- This appendix is reviewed **semi-annually** (every 6 months) to keep pace with cryptographic standards evolution
- Changes to this appendix may not require full policy approval (minor version updates)
- Technical teams MUST reference this appendix when implementing cryptographic controls
- When in doubt, consult Security Team for interpretation

---

## Table of Contents

**A.1 Symmetric Encryption Algorithms**
**A.2 Asymmetric Encryption Algorithms**
**A.3 Hash Functions**
**A.4 Password Hashing Algorithms**
**A.5 TLS/SSL Configuration Standards**
**A.6 Key Lifecycle Management Matrix**
**A.7 Certificate Standards**
**A.8 Cryptographic Protocol Versions**
**A.9 Wireless Security Standards**
**A.10 VPN Encryption Standards**
**A.11 Database Encryption Standards**
**A.12 SSH Configuration Standards**
**A.13 API Security Standards**
**A.14 Cryptographic Random Number Generation**
**A.15 Digital Signature Standards**
**A.16 Deprecated and Prohibited Algorithms (Sunset Schedule)**

---

## A.1 Symmetric Encryption Algorithms

### A.1.1 Block Ciphers

| Algorithm | Key Length | Block Size | Mode of Operation | Status | Use Cases | Notes |
|-----------|------------|------------|-------------------|--------|-----------|-------|
| **AES (Advanced Encryption Standard)** | **256-bit** | 128-bit | **GCM** | **APPROVED (Preferred)** | Data at rest, data in transit, general purpose | NIST FIPS 197, authenticated encryption |
| **AES** | **256-bit** | 128-bit | **CCM** | **APPROVED** | Constrained environments, IoT | Alternative AEAD mode |
| **AES** | **256-bit** | 128-bit | **CBC** | **APPROVED (with HMAC)** | Legacy systems only | MUST use HMAC-SHA256 for authentication |
| **AES** | **256-bit** | 128-bit | **CTR** | **APPROVED (with HMAC)** | High-performance systems | MUST use HMAC for authentication |
| **AES** | **256-bit** | 128-bit | **XTS** | **APPROVED** | Disk encryption (BitLocker, LUKS) | IEEE P1619, sector-based encryption |
| **AES** | **192-bit** | 128-bit | **GCM/CCM** | **APPROVED** | Where 256-bit not supported | Less preferred than 256-bit |
| **AES** | **128-bit** | 128-bit | **GCM** | **ACCEPTABLE** | Performance-critical, low-security data | Minimum acceptable for Internal data |
| **3DES (Triple DES)** | **168-bit** | 64-bit | **CBC** | **DEPRECATED** | Phase out by 2025 | NIST SP 800-131A, use only for legacy |
| **DES** | **56-bit** | 64-bit | Any | **PROHIBITED** | Never use | Cryptographically broken |
| **RC4** | Any | Stream | N/A | **PROHIBITED** | Never use | Multiple vulnerabilities, RFC 7465 |
| **Blowfish** | Any | 64-bit | Any | **DEPRECATED** | Replace with AES | Small block size vulnerability |

### A.1.2 Stream Ciphers

| Algorithm | Key Length | Status | Use Cases | Notes |
|-----------|------------|--------|-----------|-------|
| **ChaCha20-Poly1305** | **256-bit** | **APPROVED** | Mobile, IoT, TLS alternative to AES-GCM | RFC 8439, AEAD cipher |
| **ChaCha20** | **256-bit** | **APPROVED (with Poly1305)** | Performance-critical systems | MUST use with Poly1305 MAC |
| **Salsa20** | **256-bit** | **ACCEPTABLE** | Legacy systems, specialized use | Predecessor to ChaCha20 |
| **RC4** | Any | **PROHIBITED** | Never use | Biases in keystream, RFC 7465 |

### A.1.3 Mode of Operation Requirements

**AEAD (Authenticated Encryption with Associated Data) - PREFERRED:**
- AES-GCM (Galois/Counter Mode)
- ChaCha20-Poly1305
- AES-CCM (Counter with CBC-MAC)

**Non-AEAD Modes - Require Separate Authentication:**
- If using CBC, CTR, or other non-AEAD modes, MUST combine with:
  - HMAC-SHA256 (minimum)
  - HMAC-SHA384 or HMAC-SHA512 (preferred)
- Encrypt-then-MAC construction REQUIRED (NOT MAC-then-encrypt)

**Prohibited Modes:**
- ECB (Electronic Codebook) - PROHIBITED for all uses (no confidentiality)
- Unauthenticated CBC without HMAC - PROHIBITED

---

## A.2 Asymmetric Encryption Algorithms

### A.2.1 RSA (Rivest-Shamir-Adleman)

| Key Length | Status | Use Cases | Valid Until | Security Level | Notes |
|------------|--------|-----------|-------------|----------------|-------|
| **≥4096-bit** | **APPROVED** | Root CA, long-term signatures, critical PKI | **2030+** | ~152-bit | Best for 20+ year lifetime |
| **≥3072-bit** | **APPROVED (Preferred)** | Certificates, signatures, general PKI | **2030** | ~128-bit | Standard for most uses |
| **2048-bit** | **ACCEPTABLE** | Short-term certificates (<1 year) | **2025** | ~112-bit | Phase out preferred |
| **<2048-bit** | **PROHIBITED** | Never use | **N/A** | Insufficient | Factorization advances |

**RSA Usage Guidelines:**
- **Encryption:** Use OAEP (Optimal Asymmetric Encryption Padding) with SHA-256
- **Signatures:** Use PSS (Probabilistic Signature Scheme) with SHA-256 or higher
- **Legacy compatibility:** PKCS#1 v1.5 acceptable but not recommended
- **Padding:** Never use "no padding" or weak padding schemes

### A.2.2 Elliptic Curve Cryptography (ECC)

#### ECDSA (Elliptic Curve Digital Signature Algorithm)

| Curve | Key Size | Security Level | Status | Use Cases | Notes |
|-------|----------|----------------|--------|-----------|-------|
| **P-521** | 521-bit | ~260-bit | **APPROVED** | High-security signatures | NIST curve, highest security |
| **P-384** | 384-bit | ~192-bit | **APPROVED (Preferred)** | Certificates, signatures | NIST curve, recommended |
| **P-256 (secp256r1)** | 256-bit | ~128-bit | **APPROVED** | General use, widely compatible | NIST curve, most common |
| **P-224** | 224-bit | ~112-bit | **ACCEPTABLE** | Legacy compatibility only | Phase out preferred |
| **P-192** | 192-bit | ~96-bit | **PROHIBITED** | Never use | Insufficient security |
| **secp256k1** | 256-bit | ~128-bit | **ACCEPTABLE** | Cryptocurrency, specialized use | Bitcoin curve, not NIST |

#### EdDSA (Edwards-curve Digital Signature Algorithm)

| Curve | Key Size | Security Level | Status | Use Cases | Notes |
|-------|----------|----------------|--------|-----------|-------|
| **Ed25519** | 256-bit equiv | ~128-bit | **APPROVED (Preferred)** | SSH keys, modern systems | RFC 8032, high performance |
| **Ed448** | 448-bit equiv | ~224-bit | **APPROVED** | High-security applications | RFC 8032, quantum-resistant |

#### ECDH (Elliptic Curve Diffie-Hellman)

| Curve | Status | Use Cases | Notes |
|-------|--------|-----------|-------|
| **Curve25519 (X25519)** | **APPROVED (Preferred)** | Key exchange, TLS, VPN | RFC 7748, modern standard |
| **Curve448 (X448)** | **APPROVED** | High-security key exchange | RFC 7748 |
| **P-384** | **APPROVED** | TLS, VPN, general key exchange | NIST curve |
| **P-256** | **APPROVED** | Wide compatibility needed | NIST curve |

**ECC General Notes:**
- ECC offers equivalent security to RSA with shorter keys
- 256-bit ECC ≈ 3072-bit RSA in security strength
- Preferred over RSA for new implementations (performance, key size)
- NIST curves (P-256, P-384, P-521) widely supported in standards
- Curve25519/Ed25519 preferred for modern protocols (SSH, TLS 1.3)

### A.2.3 Diffie-Hellman (DH)

| Key Length | Status | Use Cases | Notes |
|------------|--------|-----------|-------|
| **≥3072-bit** | **APPROVED** | TLS, VPN, key exchange | Equivalent to 128-bit security |
| **2048-bit** | **ACCEPTABLE** | Legacy systems, short-term | Phase out by 2025 |
| **<2048-bit** | **PROHIBITED** | Never use | Vulnerable to attacks |

**DH Requirements:**
- Use safe primes (Sophie Germain primes)
- Validate public keys (avoid small subgroup attacks)
- Prefer ECDH (Elliptic Curve DH) over traditional DH

### A.2.4 DSA (Digital Signature Algorithm)

| Key Length | Status | Use Cases | Notes |
|------------|--------|-----------|-------|
| **Any** | **DEPRECATED** | Phase out immediately | Replace with ECDSA or Ed25519 |

**Reason for Deprecation:** DSA has security weaknesses, poor random number generation leads to key recovery

---

## A.3 Hash Functions

### A.3.1 Cryptographic Hash Functions

| Algorithm | Output Size | Status | Use Cases | Security Level | Notes |
|-----------|-------------|--------|-----------|----------------|-------|
| **SHA-3 (Keccak)** | **512-bit** | **APPROVED** | Any use case, future-proofing | ~256-bit | NIST FIPS 202 |
| **SHA-3** | **384-bit** | **APPROVED** | Signatures, integrity | ~192-bit | NIST FIPS 202 |
| **SHA-3** | **256-bit** | **APPROVED** | General purpose | ~128-bit | NIST FIPS 202 |
| **SHA-2 (SHA-512)** | **512-bit** | **APPROVED (Preferred)** | Digital signatures, certificates | ~256-bit | NIST FIPS 180-4 |
| **SHA-2 (SHA-384)** | **384-bit** | **APPROVED** | Signatures, high security | ~192-bit | Truncated SHA-512 |
| **SHA-2 (SHA-256)** | **256-bit** | **APPROVED** | General use, widely compatible | ~128-bit | Most common, minimum |
| **SHA-2 (SHA-224)** | **224-bit** | **ACCEPTABLE** | Legacy compatibility | ~112-bit | Less common |
| **SHA-1** | **160-bit** | **PROHIBITED** | Never use | Broken | Collision attacks (SHAttered) |
| **MD5** | **128-bit** | **PROHIBITED** | Never use | Broken | Completely compromised |
| **MD4** | **128-bit** | **PROHIBITED** | Never use | Broken | Completely compromised |

### A.3.2 Hash Function Selection Guide

| Use Case | Recommended Algorithm | Rationale |
|----------|----------------------|-----------|
| **Digital signatures** | SHA-512, SHA-384, SHA-3-512 | Maximum security for long-term validation |
| **TLS/SSL certificates** | SHA-256 minimum, SHA-384 preferred | Industry standard, CA/Browser Forum requirement |
| **File integrity** | SHA-256, SHA-512 | Balance of security and performance |
| **HMAC** | SHA-256, SHA-384, SHA-512 | Used with encryption for authentication |
| **General hashing** | SHA-256 | Widely supported, good security |
| **Checksums (non-security)** | CRC32, SHA-256 | CRC32 for error detection only, SHA-256 if security needed |

**Hash Function Requirements:**
- Collision resistance REQUIRED for digital signatures and certificates
- Preimage resistance REQUIRED for password hashing and integrity
- Second preimage resistance REQUIRED for all security uses

---

## A.4 Password Hashing Algorithms

### A.4.1 Password Hashing Functions (PHFs)

| Algorithm | Parameters | Status | Use Cases | Resistance To | Notes |
|-----------|------------|--------|-----------|---------------|-------|
| **Argon2id** | **m=64MB, t=3, p=4** | **APPROVED (Preferred)** | All new systems | GPU, ASIC, side-channel | PHC winner 2015 |
| **Argon2i** | **m=64MB, t=3, p=4** | **APPROVED** | Side-channel resistant contexts | Side-channel attacks | Memory-hard, cache-timing resistant |
| **Argon2d** | **m=64MB, t=3, p=4** | **APPROVED** | GPU resistance priority | GPU, ASIC | Not side-channel resistant |
| **bcrypt** | **Cost ≥12** | **APPROVED** | Existing systems, wide compatibility | GPU attacks | Increase cost factor over time |
| **scrypt** | **N=2^17, r=8, p=1** | **ACCEPTABLE** | Legacy systems | Memory-hard | Predecessor to Argon2 |
| **PBKDF2-HMAC-SHA256** | **≥600,000 iterations** | **ACCEPTABLE** | Regulatory requirement (NIST) | Brute-force | Less GPU-resistant than Argon2/bcrypt |
| **PBKDF2-HMAC-SHA512** | **≥210,000 iterations** | **ACCEPTABLE** | Legacy systems | Brute-force | Larger output than SHA256 version |
| **Plain Hash (SHA-2/SHA-3)** | N/A | **PROHIBITED** | Never use | None | No key stretching, no salt |
| **MD5/SHA-1** | Any | **PROHIBITED** | Never use | None | Broken algorithms |

### A.4.2 Argon2 Configuration Guidance

**Argon2id (Recommended for most uses):**
```
Memory (m): 64 MB (65536 KiB) minimum
  - Increase to 128 MB or 256 MB if resources allow
  - Server environments: 256 MB - 1 GB acceptable
Time (t): 3 iterations minimum
  - Target: 250-500ms per hash on production hardware
  - Adjust time if memory cannot be increased
Parallelism (p): 4 threads
  - Match to server CPU core count (4-16 typical)
Salt: 16 bytes (128 bits) minimum, cryptographically random
Output: 32 bytes (256 bits)
```

**Tuning Argon2:**
1. Start with recommended parameters
2. Benchmark on production hardware
3. Adjust memory and time to achieve 250-500ms hash time
4. Prioritize memory increase over time increase (better security)
5. Document final parameters in system configuration

### A.4.3 bcrypt Configuration Guidance

**Cost Factor Selection:**
```
Cost Factor 12: ~250ms (minimum acceptable)
Cost Factor 13: ~500ms (recommended for standard accounts)
Cost Factor 14: ~1 second (recommended for privileged accounts)
Cost Factor 15: ~2 seconds (high-security environments)
Cost Factor 16: ~4 seconds (maximum practical for user-facing)
```

**Cost Factor Evolution:**
- Start with cost factor 12-13
- Increase cost factor annually as computing power increases
- Moore's Law approximation: increase cost by 1 every ~18-24 months
- Test on production hardware before deploying cost increase

### A.4.4 Password Hashing Requirements

**Universal Requirements:**
- MUST use cryptographically random salt (minimum 128 bits)
- Salt MUST be unique per password (no salt reuse)
- Salt MUST be stored alongside hash
- Pepper (application-wide secret) RECOMMENDED as additional defense layer
- Timing attacks MUST be prevented (constant-time comparison)

**Storage Format Example:**
```
$argon2id$v=19$m=65536,t=3,p=4$<salt_base64>$<hash_base64>
$2b$12$<salt+hash_base64>  # bcrypt format
```

---

## A.5 TLS/SSL Configuration Standards

### A.5.1 TLS Protocol Versions

| Version | Status | Valid Until | Notes |
|---------|--------|-------------|-------|
| **TLS 1.3** | **APPROVED (Preferred)** | Current standard | RFC 8446, best security and performance |
| **TLS 1.2** | **APPROVED** | 2025+ | RFC 5246, acceptable minimum |
| **TLS 1.1** | **PROHIBITED** | Deprecated 2020 | RFC 4346, no longer secure |
| **TLS 1.0** | **PROHIBITED** | Deprecated 2020 | RFC 2246, no longer secure |
| **SSL 3.0** | **PROHIBITED** | Deprecated 2015 | RFC 6101, POODLE vulnerability |
| **SSL 2.0** | **PROHIBITED** | Deprecated 2011 | Multiple critical vulnerabilities |

### A.5.2 TLS 1.3 Cipher Suites (Preferred)

**All TLS 1.3 cipher suites provide Perfect Forward Secrecy (PFS) and AEAD:**

```
TLS_AES_256_GCM_SHA384           # Preferred, highest security
TLS_CHACHA20_POLY1305_SHA256     # Preferred, best performance on mobile
TLS_AES_128_GCM_SHA256           # Acceptable, widely compatible
```

**TLS 1.3 Configuration Notes:**
- Only 5 cipher suites defined in TLS 1.3 (simplified from TLS 1.2)
- All provide excellent security
- Cipher suite negotiation is server-driven
- 0-RTT (Zero Round Trip Time) SHOULD be disabled (replay attack risk)

### A.5.3 TLS 1.2 Cipher Suites (If TLS 1.3 Not Available)

**Recommended Cipher Suite Order (highest to lowest priority):**

```
# ECDHE with AES-GCM (Best - PFS + AEAD)
TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

# ECDHE with ChaCha20-Poly1305 (Best for mobile)
TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256

# DHE with AES-GCM (Acceptable - PFS + AEAD, slower than ECDHE)
TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
TLS_DHE_RSA_WITH_AES_128_GCM_SHA256

# ECDHE with AES-CBC (Acceptable - PFS, no AEAD)
TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
```

**PROHIBITED TLS 1.2 Cipher Suites:**
```
# No Perfect Forward Secrecy (static RSA key exchange)
TLS_RSA_WITH_AES_*

# Weak/broken ciphers
TLS_*_WITH_3DES_*
TLS_*_WITH_RC4_*
TLS_*_WITH_DES_*
TLS_*_WITH_NULL_*
TLS_*_EXPORT_*

# Anonymous key exchange (no authentication)
TLS_DH_anon_*
TLS_ECDH_anon_*
```

### A.5.4 TLS Configuration Parameters

**Required TLS Settings:**

| Parameter | Requirement | Rationale |
|-----------|-------------|-----------|
| **Perfect Forward Secrecy** | REQUIRED | Protects past sessions if long-term keys compromised |
| **Server Name Indication (SNI)** | REQUIRED | Virtual hosting, correct certificate selection |
| **Certificate Transparency (CT)** | RECOMMENDED | Detect mis-issued certificates |
| **OCSP Stapling** | RECOMMENDED | Efficient certificate revocation checking |
| **Session Resumption** | PERMITTED | Performance improvement, use with caution |
| **TLS Compression** | PROHIBITED | CRIME attack vulnerability |
| **TLS Renegotiation** | SECURE ONLY | Secure renegotiation (RFC 5746) required |

**HSTS (HTTP Strict Transport Security):**
```
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```
- REQUIRED for all HTTPS websites
- max-age: 1 year minimum (31536000 seconds)
- includeSubDomains: Recommended
- preload: Recommended for public-facing sites

### A.5.5 TLS Testing and Validation

**Tools for TLS Configuration Verification:**
- SSL Labs Server Test: https://www.ssllabs.com/ssltest/
- testssl.sh: Command-line TLS scanner
- nmap with ssl-enum-ciphers script
- Mozilla Observatory: https://observatory.mozilla.org/

**Target Rating:**
- SSL Labs Grade A or A+ REQUIRED for external services
- Grade B acceptable only with documented compensating controls
- Grade C or below PROHIBITED

---

## A.6 Key Lifecycle Management Matrix

| Key Type | Generation Method | Min Length | Max Validity | Rotation Frequency | Storage | Backup Required | Destruction Method |
|----------|-------------------|------------|--------------|-------------------|---------|-----------------|-------------------|
| **Root CA Private Key** | HSM/Offline ceremony | RSA 4096 / EC P-384 | 10-20 years | Never (retire at expiry) | HSM, air-gapped | Yes (M-of-N split) | HSM secure delete + physical destruction |
| **Intermediate CA** | HSM/Secure | RSA 3072 / EC P-384 | 5-10 years | N/A | HSM | Yes (encrypted backup) | HSM secure delete |
| **TLS Server Certificate** | Automated (ACME) / Manual CSR | RSA 2048 / EC P-256 | 397 days | Annual (90-day recommended) | Server filesystem | No | File deletion |
| **Code Signing Certificate** | HSM/Secure workstation | RSA 3072 / EC P-384 | 1-3 years | Annual | HSM or hardware token | Yes (secure escrow) | HSM secure delete |
| **User Certificate (S/MIME)** | PKI server | RSA 2048 / EC P-256 | 1 year | Annual | Smart card / user keystore | Optional | Card destruction / keystore delete |
| **Database Master Encryption Key** | KMS/HSM | AES-256 | 1-2 years | Annual | HSM or KMS | Yes (encrypted, separate location) | Cryptographic erasure |
| **Database Column Encryption Key** | KMS | AES-256 | 1 year | Annual | KMS | Yes | Cryptographic erasure |
| **Disk Encryption Key (BitLocker/LUKS)** | OS CSPRNG | AES-256 | N/A (tied to device) | On device retirement | TPM / Key escrow system | Yes (recovery key) | TPM reset / secure disk wipe |
| **SSH User Key** | ssh-keygen | RSA 2048 / Ed25519 | No expiry (managed) | Annual + on personnel change | User home directory | Optional | File deletion (shred) |
| **SSH Host Key** | ssh-keygen | RSA 3072 / Ed25519 | No expiry | On OS reinstall | /etc/ssh/ | Yes (config management) | File deletion |
| **API Key (User)** | CSPRNG (256-bit) | 256-bit entropy | 90 days | Quarterly | Secrets manager | No | Database deletion |
| **API Key (Service Account)** | CSPRNG (256-bit) | 256-bit entropy | 90 days | Quarterly (automated) | Secrets manager | Yes (for DR) | Database deletion |
| **OAuth Access Token** | CSPRNG | 256-bit entropy | 1 hour | Per session | Memory / Redis | No | Memory clear / TTL expiry |
| **OAuth Refresh Token** | CSPRNG | 256-bit entropy | 24 hours | Per session | Database (encrypted) | No | Database deletion |
| **JWT Signing Key** | CSPRNG / RSA | RSA 3072 / HMAC-SHA256 (256-bit) | 30-90 days | Monthly-Quarterly | Secrets manager | Yes | Secure deletion |
| **VPN Pre-Shared Key** | CSPRNG | 256-bit | 90 days | Quarterly | VPN server config (encrypted) | Yes (encrypted backup) | Config overwrite |
| **Backup Encryption Key** | KMS/HSM | AES-256 | Indefinite (for old backups) | N/A (versioned) | HSM / Offline secure storage | Yes (geographically distributed) | Per retention policy |

**Key Storage Legend:**
- **HSM**: Hardware Security Module (FIPS 140-2 Level 2+)
- **KMS**: Key Management Service (cloud or on-premises)
- **TPM**: Trusted Platform Module
- **Secrets Manager**: HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, etc.

---

## A.7 Certificate Standards

### A.7.1 Certificate Validity Periods

**Public TLS Certificates** (CA/Browser Forum Baseline Requirements):

| Effective Date | Max Validity | DCV Reuse | Authority | Status |
|----------------|--------------|-----------|-----------|--------|
| Current | 398 days | 398 days | CA/B Forum SC-062 (2020) | Active until 15.03.2026 |
| **15.03.2026** | **200 days** | **200 days** | **CA/B Forum SC-081v3 (2025)** | **Automation required** |
| **15.03.2027** | **100 days** | **100 days** | **CA/B Forum SC-081v3 (2025)** | Bi-monthly renewals |
| **15.03.2029** | **47 days** | **10 days** | **CA/B Forum SC-081v3 (2025)** | Final target |

**Private/Internal PKI Certificates** ([Organization] Policy):

| Certificate Type | Max Validity | Recommended Validity | Notes |
|------------------|--------------|---------------------|-------|
| Internal TLS | 825 days | 180-365 days | Not subject to CA/B Forum; align with industry practice |
| Internal authentication | 398 days | 365 days | Annual re-issuance recommended |
| Test/development | 90 days | 90 days | Encourages automation testing |

**Other Certificate Types:**

| Certificate Type | Maximum Validity | Recommended Validity | Notes |
|------------------|------------------|---------------------|-------|
| **Code Signing** | 825 days (3 years) | 365 days (1 year) | CA/B Forum Code Signing Requirements |
| **Email (S/MIME)** | 825 days (2 years) | 365 days (1 year) | Shorter for high-turnover organizations |
| **Client Authentication** | 365 days (1 year) | 365 days (1 year) | Re-issue on role change |
| **Root CA** | 20 years | 10-15 years | Long-lived, infrequent rotation |
| **Intermediate CA** | 10 years | 5-7 years | Balance security and operational stability |

**Reference**: CA/Browser Forum Ballot SC-081v3  
**URL**: https://cabforum.org/2025/04/11/ballot-sc081v3-introduce-schedule-of-reducing-validity-and-data-reuse-periods/

### A.7.2 Certificate Subject Naming Convention

**Standard Format:**
```
CN=<Common Name>, OU=<Organizational Unit>, O=<Organization>, L=<Locality>, ST=<State/Province>, C=<Country>
```

**Examples:**
- **Web Server:** `CN=www.example.com, OU=IT Department, O=Example Corp, L=Zurich, ST=Zurich, C=CH`
- **User:** `CN=John Doe, OU=Engineering, O=Example Corp, L=Zurich, ST=Zurich, C=CH`
- **Service:** `CN=api.internal.example.com, OU=Infrastructure, O=Example Corp, L=Zurich, ST=Zurich, C=CH`

**Subject Alternative Name (SAN):**
- TLS certificates MUST include SAN extension
- Common Name (CN) alone is deprecated
- SAN can include: DNS names, IP addresses, email addresses
- Example SAN: `DNS:www.example.com, DNS:example.com, DNS:*.example.com`

### A.7.3 Certificate Key Usage Extensions

| Extension | Use Case | Values |
|-----------|----------|--------|
| **Key Usage** | Define cryptographic operations | digitalSignature, keyEncipherment, dataEncipherment, keyAgreement, keyCertSign, cRLSign |
| **Extended Key Usage** | Define certificate purpose | serverAuth, clientAuth, codeSigning, emailProtection, timeStamping |
| **Basic Constraints** | CA vs. end-entity | CA:TRUE for CAs, CA:FALSE for end-entity certificates |
| **Subject Alternative Name** | Additional identities | DNS, IP Address, email, URI |

**Certificate Profile Examples:**

**TLS Server Certificate:**
```
Key Usage: digitalSignature, keyEncipherment
Extended Key Usage: serverAuth
Basic Constraints: CA:FALSE
Subject Alternative Name: DNS:www.example.com, DNS:example.com
```

**Code Signing Certificate:**
```
Key Usage: digitalSignature
Extended Key Usage: codeSigning
Basic Constraints: CA:FALSE
```

**Email Certificate (S/MIME):**
```
Key Usage: digitalSignature, keyEncipherment, dataEncipherment
Extended Key Usage: emailProtection
Subject Alternative Name: email:user@example.com
```

---

## A.8 Cryptographic Protocol Versions

### A.8.1 Secure Shell (SSH)

| Parameter | Requirement | Notes |
|-----------|-------------|-------|
| **SSH Protocol Version** | SSHv2 only | SSHv1 PROHIBITED (RFC 4253) |
| **Host Key Algorithms** | ssh-ed25519, ecdsa-sha2-nistp256, rsa-sha2-512, rsa-sha2-256 | Prefer Ed25519, avoid ssh-rsa (SHA-1) |
| **Key Exchange Algorithms** | curve25519-sha256, diffie-hellman-group-exchange-sha256 | Minimum 2048-bit DH group |
| **Encryption Algorithms** | chacha20-poly1305@openssh.com, aes256-gcm@openssh.com, aes128-gcm@openssh.com, aes256-ctr, aes128-ctr | AEAD preferred |
| **MAC Algorithms** | hmac-sha2-512-etm@openssh.com, hmac-sha2-256-etm@openssh.com | ETM (Encrypt-then-MAC) required |

**Prohibited SSH Algorithms:**
```
# Weak host keys
ssh-dss (DSA)
ssh-rsa with SHA-1

# Weak ciphers
3des-cbc
aes128-cbc, aes256-cbc (without ETM)
arcfour, arcfour128, arcfour256
blowfish-cbc
cast128-cbc

# Weak MACs
hmac-md5
hmac-sha1
umac-64
```

**SSH Configuration Example (OpenSSH):**
```
# /etc/ssh/sshd_config
Protocol 2
HostKey /etc/ssh/ssh_host_ed25519_key
HostKey /etc/ssh/ssh_host_rsa_key
KexAlgorithms curve25519-sha256,diffie-hellman-group-exchange-sha256
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
```

---

## A.9 Wireless Security Standards

| Standard | Status | Use Case | Encryption | Authentication | Notes |
|----------|--------|----------|------------|----------------|-------|
| **WPA3-Enterprise** | **APPROVED (Preferred)** | Corporate networks | AES-256-GCM or AES-128-GCM | 802.1X (EAP-TLS preferred) | Latest standard, best security |
| **WPA3-Personal** | **APPROVED** | Small offices, home offices | AES-128-GCM | SAE (Simultaneous Authentication of Equals) | Better than WPA2, no PSK weaknesses |
| **WPA2-Enterprise** | **APPROVED** | Legacy devices, corporate networks | AES-128-CCMP | 802.1X (EAP-TLS, EAP-TTLS) | Acceptable, transition to WPA3 |
| **WPA2-Personal** | **ACCEPTABLE** | Small offices (with strong passphrase) | AES-128-CCMP | Pre-shared key (PSK) | Minimum 20-character random PSK required |
| **WPA (original)** | **PROHIBITED** | Never use | TKIP | Weak | Broken, use WPA2 minimum |
| **WEP** | **PROHIBITED** | Never use | RC4 | Weak | Completely broken |
| **Open (No encryption)** | **PROHIBITED** | Never use (except guest with captive portal) | None | None | Use only for isolated guest networks |

**WPA3-Enterprise Configuration:**
- EAP Method: EAP-TLS (certificate-based) PREFERRED
- Alternative: EAP-TTLS with strong inner authentication
- RADIUS server with TLS 1.2+ for backend communication
- Certificate validation REQUIRED (no "accept any certificate")

**WPA2/WPA3-Personal Passphrase Requirements:**
- Minimum 20 characters (WPA3 mitigates offline attacks, but strong passphrase still recommended)
- Cryptographically random generation preferred
- Change quarterly for high-security environments
- Unique per SSID (no passphrase reuse)

---

## A.10 VPN Encryption Standards

### A.10.1 IPsec Configuration

| Parameter | Requirement | Notes |
|-----------|-------------|-------|
| **IKE Version** | IKEv2 | RFC 7296, preferred over IKEv1 |
| **Phase 1 (IKE) Encryption** | AES-256-GCM, AES-256-CBC, ChaCha20-Poly1305 | AEAD preferred |
| **Phase 1 Integrity** | SHA-384, SHA-512 (if not using AEAD) | SHA-256 minimum |
| **Phase 1 DH Group** | Group 19 (P-384), Group 20 (P-521), Group 14 (2048-bit) | Avoid Group 1, 2, 5 (weak) |
| **Phase 2 (ESP) Encryption** | AES-256-GCM, AES-256-CBC, ChaCha20-Poly1305 | AEAD preferred |
| **Phase 2 Integrity** | SHA-384, SHA-512 (if not using AEAD) | SHA-256 minimum |
| **Phase 2 PFS Group** | Same as Phase 1 DH Group | Perfect Forward Secrecy REQUIRED |
| **Authentication** | Certificate-based (preferred), Pre-shared key (acceptable with strong entropy) | Avoid weak PSKs |

**Example IPsec Proposal (strongSwan):**
```
conn corporate-vpn
    ike=aes256gcm128-sha384-ecp384!
    esp=aes256gcm128-sha384-ecp384!
    keyexchange=ikev2
    authby=pubkey
```

### A.10.2 OpenVPN Configuration

| Parameter | Requirement | Notes |
|-----------|-------------|-------|
| **TLS Version** | TLS 1.2+ | TLS 1.3 preferred |
| **Cipher** | AES-256-GCM, ChaCha20-Poly1305 | AEAD required |
| **Authentication** | SHA-384, SHA-512 | SHA-256 minimum |
| **TLS Cipher Suite** | Same as TLS 1.2/1.3 standards (A.5) | Follow TLS best practices |
| **Certificate Key Size** | RSA 3072-bit or EC P-256 minimum | RSA 4096 or EC P-384 preferred |
| **TLS Authentication** | tls-auth or tls-crypt | tls-crypt preferred (encrypts handshake) |

**Example OpenVPN Configuration:**
```
cipher AES-256-GCM
auth SHA384
tls-version-min 1.2
tls-cipher TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384:TLS-ECDHE-ECDSA-WITH-AES-256-GCM-SHA384
dh none  # Use ECDHE instead of static DH
```

### A.10.3 WireGuard Configuration

| Parameter | Requirement | Notes |
|-----------|-------------|-------|
| **Encryption** | ChaCha20-Poly1305 | Built-in, cannot be changed |
| **Key Exchange** | Curve25519 | Built-in, cannot be changed |
| **Hashing** | BLAKE2s | Built-in, cannot be changed |
| **Key Size** | 256-bit | Built-in, cannot be changed |

**WireGuard Notes:**
- Modern, lightweight VPN protocol
- Fixed cryptographic suite (no configuration needed)
- All algorithms are secure and modern
- Automatic key rotation not built-in (requires external tooling)

---

## A.11 Database Encryption Standards

### A.11.1 Transparent Data Encryption (TDE)

| Database | TDE Feature | Encryption Algorithm | Key Management |
|----------|-------------|---------------------|----------------|
| **Microsoft SQL Server** | TDE | AES-128, AES-192, AES-256 | Database Master Key (DMK) in master database, or EKM with HSM |
| **Oracle Database** | TDE | AES-256, AES-192, AES-128 | Oracle Wallet or HSM (PKCS#11) |
| **PostgreSQL** | pgcrypto / pg_tde extension | AES-256-GCM (pgcrypto), AES-128-XTS (pg_tde) | External KMS recommended |
| **MySQL/MariaDB** | InnoDB Encryption | AES-256-CBC (MariaDB), AES-256-ECB (MySQL) | Key ring plugins (file, KMS) |
| **MongoDB** | Encrypted Storage Engine | AES-256-GCM | KMIP-compatible KMS or local key file |

**TDE Configuration Requirements:**
- AES-256 PREFERRED for all databases
- Key rotation MUST be supported (annual rotation required)
- Keys MUST be stored separately from database files
- HSM or enterprise KMS REQUIRED for >100,000 sensitive records

### A.11.2 Database Connection Encryption

| Database | Protocol | Encryption | Certificate Validation |
|----------|----------|------------|------------------------|
| **PostgreSQL** | SSL/TLS | ssl=on, ssl_ciphers (same as TLS 1.2+ standards) | sslmode=verify-full (certificate validation) |
| **MySQL** | SSL/TLS | require_secure_transport=ON | ssl-mode=VERIFY_IDENTITY |
| **SQL Server** | TLS | Encrypt=yes, TrustServerCertificate=false | Certificate validation required |
| **Oracle** | Oracle Native Encryption | TCPS (TLS) | Cipher suites per TLS standards |
| **MongoDB** | TLS | net.tls.mode=requireTLS | Certificate validation required |

**Connection Encryption Requirements:**
- TLS 1.2+ REQUIRED for all database connections
- Certificate validation REQUIRED (not "trust any certificate")
- Self-signed certificates acceptable for internal databases (with proper CA)

---

## A.12 SSH Configuration Standards

**Covered in Section A.8.1**

---

## A.13 API Security Standards

### A.13.1 API Authentication Methods

| Method | Status | Use Case | Token/Key Requirements |
|--------|--------|----------|------------------------|
| **OAuth 2.0 (Authorization Code + PKCE)** | **APPROVED (Preferred)** | User-facing APIs, delegated access | Access token: 1 hour max, Refresh token: 24 hours max |
| **OAuth 2.0 (Client Credentials)** | **APPROVED** | Service-to-service | Client secret: 256-bit entropy minimum |
| **API Key** | **APPROVED** | Simple APIs, rate-limited access | 256-bit entropy, 90-day rotation |
| **Mutual TLS (mTLS)** | **APPROVED** | High-security service-to-service | Client certificate: RSA 2048 or EC P-256 minimum |
| **JWT (JSON Web Token)** | **APPROVED** | Stateless authentication | Signed with RS256/RS384/ES256, short expiry |
| **Basic Authentication over HTTPS** | **ACCEPTABLE** | Internal APIs only, legacy | Strong password, rate-limited |
| **API Key in URL** | **PROHIBITED** | Never use | Logged in web server logs, exposed in browser history |

### A.13.2 JWT (JSON Web Token) Standards

| Parameter | Requirement | Notes |
|-----------|-------------|-------|
| **Signing Algorithm** | RS256, RS384, RS512, ES256, ES384, ES512 | Asymmetric algorithms preferred |
| **Symmetric Signing** | HS256, HS384, HS512 (if asymmetric not possible) | Requires 256-bit+ shared secret |
| **Prohibited Algorithms** | none, HS256 with weak secret | "none" algorithm MUST be disabled |
| **Expiration (exp)** | 1 hour maximum | Shorter for high-security |
| **Claims Validation** | iss, aud, exp, nbf MUST be validated | Prevent token reuse across services |
| **Token Storage** | HTTPOnly cookies (web), Secure storage APIs (mobile) | Never localStorage for sensitive tokens |

**JWT Header Example:**
```json
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "key-id-2024"
}
```

**JWT Payload Example:**
```json
{
  "iss": "https://auth.example.com",
  "sub": "user123",
  "aud": "https://api.example.com",
  "exp": 1234567890,
  "iat": 1234564290,
  "scope": "read write"
}
```

---

## A.14 Cryptographic Random Number Generation

### A.14.1 Approved CSPRNG (Cryptographically Secure Pseudo-Random Number Generators)

| Platform | CSPRNG | Function/API | Notes |
|----------|--------|--------------|-------|
| **Linux** | /dev/urandom | Read from /dev/urandom | Preferred over /dev/random (non-blocking) |
| **Windows** | CryptoAPI | CryptGenRandom(), BCryptGenRandom() | Use BCryptGenRandom for modern apps |
| **macOS** | /dev/urandom | Read from /dev/urandom, or SecRandomCopyBytes() | SecRandomCopyBytes is Apple's API |
| **Java** | SecureRandom | java.security.SecureRandom | Automatically seeds from OS CSPRNG |
| **Python** | secrets module | secrets.token_bytes(), secrets.token_hex() | Preferred over random module |
| **Node.js** | crypto module | crypto.randomBytes() | Uses OS CSPRNG |
| **.NET** | RNGCryptoServiceProvider | RNGCryptoServiceProvider.GetBytes() | Or RandomNumberGenerator in .NET Core |
| **Go** | crypto/rand | rand.Read() | Uses OS CSPRNG |
| **PHP** | random_bytes() | random_bytes(length) | PHP 7+, CSPRNG |
| **OpenSSL** | RAND_bytes() | RAND_bytes(buf, num) | OpenSSL library CSPRNG |

### A.14.2 Prohibited Random Number Sources

**NEVER use for cryptographic purposes:**
- `rand()` / `srand()` (C/C++)
- `random` module (Python) - use `secrets` instead
- `Math.random()` (JavaScript) - use `crypto.getRandomValues()`
- `java.util.Random` (Java) - use `java.security.SecureRandom`
- Timestamp-based seeds
- Sequential or predictable values

### A.14.3 Entropy Requirements

| Use Case | Minimum Entropy | Recommendation |
|----------|-----------------|----------------|
| **Symmetric Keys** | Key length (e.g., 256 bits for AES-256) | Generate full key length from CSPRNG |
| **API Keys / Tokens** | 256 bits | 32 bytes (256 bits) random data |
| **Session IDs** | 128 bits | 16 bytes minimum, 32 bytes preferred |
| **Salts (password hashing)** | 128 bits | 16 bytes minimum |
| **IVs (Initialization Vectors)** | Block size (128 bits for AES) | Must be unique per encryption |
| **Nonces** | Depends on algorithm | Must be unique, size per protocol spec |

---

## A.15 Digital Signature Standards

### A.15.1 Signature Algorithms

| Algorithm | Key Size | Hash Function | Status | Use Case |
|-----------|----------|---------------|--------|----------|
| **RSA-PSS** | ≥3072-bit | SHA-256, SHA-384, SHA-512 | **APPROVED (Preferred)** | Documents, certificates, code signing |
| **RSA-PKCS#1 v1.5** | ≥3072-bit | SHA-256, SHA-384, SHA-512 | **APPROVED** | Legacy compatibility |
| **ECDSA (P-384)** | 384-bit | SHA-384 | **APPROVED (Preferred)** | Certificates, documents |
| **ECDSA (P-256)** | 256-bit | SHA-256 | **APPROVED** | General use |
| **Ed25519** | 256-bit equiv | SHA-512 (internal) | **APPROVED (Preferred)** | Modern systems, SSH |
| **Ed448** | 448-bit equiv | SHAKE256 (internal) | **APPROVED** | High security |
| **DSA** | Any | Any | **DEPRECATED** | Replace with ECDSA/Ed25519 |
| **RSA with SHA-1** | Any | SHA-1 | **PROHIBITED** | SHA-1 collisions proven |

### A.15.2 XML Digital Signatures (XMLDSig)

**Approved Canonicalization Methods:**
- Exclusive XML Canonicalization (exc-c14n#)
- Canonical XML 1.1 (c14n11#)

**Approved Signature Methods:**
- http://www.w3.org/2001/04/xmldsig-more#rsa-sha256 (RSA-SHA256)
- http://www.w3.org/2001/04/xmldsig-more#rsa-sha384 (RSA-SHA384)
- http://www.w3.org/2001/04/xmldsig-more#rsa-sha512 (RSA-SHA512)
- http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256 (ECDSA-SHA256)

**Prohibited:**
- RSA-SHA1
- DSA-SHA1

---

## A.16 Deprecated and Prohibited Algorithms (Sunset Schedule)

### A.16.1 Currently Prohibited (Never Use)

| Algorithm/Protocol | Reason | Prohibited Since |
|--------------------|--------|------------------|
| **DES, 3DES** | Small key size, block size | 2024 (planned NIST deprecation) |
| **RC4** | Biases in keystream | 2015 (RFC 7465) |
| **MD5** | Collision attacks | 2008 |
| **SHA-1** | Collision attacks (SHAttered) | 2017 (most uses), 2020 (certificates) |
| **SSL 2.0, SSL 3.0** | Multiple vulnerabilities (POODLE) | 2015 |
| **TLS 1.0, TLS 1.1** | Weak cipher suites, attacks (BEAST) | 2020 (PCI DSS requirement) |
| **SSHv1** | Cryptographic weaknesses | 2006 |
| **DSA** | Weak random number generation risks | 2024 (phase-out) |
| **RSA < 2048-bit** | Factorization advances | 2014 |
| **Plaintext protocols** | No encryption (FTP, Telnet, HTTP for sensitive data) | Always prohibited |

### A.16.2 Deprecated (Phase Out By Target Date)

| Algorithm/Protocol | Phase Out By | Replacement | Reason |
|--------------------|--------------|-------------|--------|
| **3DES** | 2025 | AES-256 | NIST deprecation, small block size |
| **RSA 2048-bit** | 2025 | RSA 3072-bit or ECDSA P-256 | Advancing computational power |
| **TLS 1.2 (without PFS)** | 2026 | TLS 1.3 or TLS 1.2 with ECDHE/DHE | No forward secrecy |
| **bcrypt cost < 12** | 2025 | bcrypt cost ≥ 12 or Argon2id | Computational advances |
| **PBKDF2 < 600k iterations** | 2025 | PBKDF2 ≥ 600k iterations or Argon2id | Computational advances |
| **WPA2-Personal (PSK)** | 2026 | WPA3-Personal | SAE protocol improvements |

### A.16.3 Under Review (Future Deprecation Possible)

| Algorithm/Protocol | Concern | Review Date |
|--------------------|---------|-------------|
| **SHA-256** | Quantum computing threat (distant) | 2030+ |
| **RSA (all key sizes)** | Quantum computing (Shor's algorithm) | 2030-2035 |
| **ECDSA (NIST curves)** | Quantum computing threat | 2030-2035 |
| **AES-128** | Quantum computing (Grover's algorithm reduces to 64-bit security) | 2030+ |

**Post-Quantum Cryptography (PQC) Readiness:**
- NIST PQC standards finalized in 2024
- Begin pilot implementations of PQC algorithms (CRYSTALS-Kyber, CRYSTALS-Dilithium) by 2026
- Hybrid classical-PQC approach recommended during transition
- Full migration timeline TBD based on threat landscape

---

## References and Standards

**NIST (National Institute of Standards and Technology):**
- FIPS 140-2/140-3: Security Requirements for Cryptographic Modules
- FIPS 180-4: Secure Hash Standard (SHS)
- FIPS 186-5: Digital Signature Standard (DSS)
- FIPS 197: Advanced Encryption Standard (AES)
- SP 800-52: Guidelines for TLS Implementations
- SP 800-57: Recommendation for Key Management
- SP 800-63B: Digital Identity Guidelines (Authentication)
- SP 800-131A: Transitioning the Use of Cryptographic Algorithms
- SP 800-175B: Guideline for Using Cryptographic Standards

**IETF (Internet Engineering Task Force) RFCs:**
- RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3
- RFC 5246: The Transport Layer Security (TLS) Protocol Version 1.2
- RFC 8439: ChaCha20 and Poly1305
- RFC 7748: Elliptic Curves for Security (Curve25519, Curve448)
- RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA)
- RFC 4253: The Secure Shell (SSH) Protocol
- RFC 7465: Prohibiting RC4 Cipher Suites

**Industry Standards:**
- CA/Browser Forum Baseline Requirements
- PCI DSS (Payment Card Industry Data Security Standard)
- BSI TR-02102: Cryptographic Mechanisms (German Federal Office for Information Security)
- ENISA: Algorithms, Key Size and Protocols Report

**Last Updated:** DD.MM.YYYY
**Next Review:** DD.MM.YYYY (6 months from last update)

---

**End of Appendix A - Approved Cryptographic Standards**

*"Don't roll your own crypto. Unless you're Ron Rivest, Adi Shamir, or Leonard Adleman. And even then, think twice."*  
*— Every Security Professional Who Has Seen Homegrown Encryption*