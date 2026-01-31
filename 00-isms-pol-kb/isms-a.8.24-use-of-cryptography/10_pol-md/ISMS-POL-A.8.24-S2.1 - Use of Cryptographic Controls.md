# Control A.8.24: Use of Cryptography
## POLICY REQUIREMENTS - SECTION 2.1
## Use of Cryptographic Controls

---

**Document ID**: ISMS-POL-A.8.24-S2.1  
**Title**: Use of Cryptography - Use of Cryptographic Controls  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Information Security Manager | Initial cryptographic controls framework |

**Review Cycle**: Semi-Annual (Every 6 months - due to cryptographic algorithm lifecycle changes)  
**Next Review Date**: [Approval Date + 6 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Team Lead / Cryptography Subject Matter Expert (mandatory)
- Secondary: Chief Information Officer (CIO) or IT Director
- Compliance: Legal/Compliance Officer (for regulatory alignment with nFADP, GDPR)

**Distribution**: IT Security Team, System Administrators, Development Teams, Infrastructure Teams, Cryptography Implementers  
**Related Standards**: ISO/IEC 27001:2022 Control A.8.24, ISO/IEC 27002:2022, NIST SP 800-175B, NIST SP 800-57, BSI TR-02102 series, ENISA Cryptographic Guidelines, nFADP, GDPR

---

## 2.1 Use of Cryptographic Controls

### 2.1.1 Application Areas

**Cryptographic controls SHALL be applied in the following areas:**

- **Data transmission** (both internal and external networks)
- **Data storage** (data at rest on any media)
- **User and system authentication** (identity verification)
- **Digital signatures** (ensuring non-repudiation)
- **Integrity verification** (detecting unauthorized modifications)

**Risk-Based Implementation:**
- Cryptographic control selection MUST be based on risk assessment
- Controls SHALL be proportionate to the classification of information being protected
- Business impact analysis SHALL inform protection levels

---

### 2.1.2 Approved Cryptographic Standards

**All cryptographic implementations MUST use only approved algorithms and key lengths as specified below.**

#### Encryption Algorithms

**Symmetric Encryption:**

| Algorithm | Key Length | Mode | Status | Use Case |
|-----------|------------|------|--------|----------|
| **AES** | **256-bit** | **GCM** | **APPROVED (Preferred)** | Data at rest, data in transit, general purpose |
| **ChaCha20** | **256-bit** | **Poly1305** | **APPROVED** | Mobile devices, IoT, performance-critical systems |
| **AES** | **256-bit** | **CBC** | **APPROVED (Legacy only)** | Legacy systems only, MUST use with HMAC |
| **3DES** | **168-bit** | **Any** | **DEPRECATED** | Phase out by 2025, use only for legacy compatibility |
| **DES** | **56-bit** | **Any** | **PROHIBITED** | Never use - cryptographically broken |
| **RC4** | **Any** | **Any** | **PROHIBITED** | Never use - multiple known vulnerabilities |

**Asymmetric Encryption:**

| Algorithm | Key Length | Status | Use Case | Valid Until |
|-----------|------------|--------|----------|-------------|
| **RSA** | **≥4096-bit** | **APPROVED** | Long-term signatures, root CAs, critical PKI | 2030+ |
| **RSA** | **≥3072-bit** | **APPROVED** | Certificates, signatures, general PKI | 2030 |
| **RSA** | **2048-bit** | **ACCEPTABLE** | Short-term certificates (<1 year) | 2025 |
| **RSA** | **<2048-bit** | **PROHIBITED** | Never use - insufficient security | - |
| **ECDSA** | **P-384 curve** | **APPROVED** | Certificates, signatures, recommended | 2030+ |
| **ECDSA** | **P-256 curve** | **APPROVED** | General use, widely compatible | 2030 |
| **Ed25519** | **256-bit equivalent** | **APPROVED** | SSH keys, modern systems, high performance | 2030+ |
| **DSA** | **Any** | **DEPRECATED** | Phase out immediately, replace with ECDSA/Ed25519 | - |

#### Hash Functions

| Algorithm | Output Size | Status | Use Case | Notes |
|-----------|-------------|--------|----------|-------|
| **SHA-3** | **256/512-bit** | **APPROVED** | Any use case | Future-proof choice |
| **SHA-2** | **384/512-bit** | **APPROVED** | Digital signatures, integrity verification | Recommended |
| **SHA-2** | **256-bit** | **APPROVED** | General purpose hashing | Minimum acceptable |
| **SHA-1** | **160-bit** | **PROHIBITED** | Never use | Collision attacks proven |
| **MD5** | **128-bit** | **PROHIBITED** | Never use | Completely broken |

#### Password Hashing

| Algorithm | Parameters | Status | Use Case | Notes |
|-----------|------------|--------|----------|-------|
| **Argon2id** | **m=64MB, t=3, p=4** | **APPROVED (Preferred)** | All new systems | Winner of Password Hashing Competition |
| **bcrypt** | **Cost factor ≥12** | **APPROVED** | Existing systems | Increase cost factor over time |
| **PBKDF2-HMAC-SHA256** | **≥600,000 iterations** | **ACCEPTABLE** | Legacy compatibility | Less resistant to GPU attacks |
| **scrypt** | **N=2^17, r=8, p=1** | **ACCEPTABLE** | Legacy systems | Memory-hard function |
| **Plain hash (SHA/MD5)** | **-** | **PROHIBITED** | Never use | No salt, no key stretching |

#### TLS/SSL Requirements

**Minimum TLS Version:**
- **TLS 1.3 (RFC 8446)** - **PREFERRED**
- **TLS 1.2 (RFC 5246)** - **ACCEPTABLE** (with approved cipher suites only)

**Prohibited Versions:**
- TLS 1.1, TLS 1.0, SSL 3.0, SSL 2.0 - **ALL PROHIBITED**

**TLS 1.3 Approved Cipher Suites:**
```
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
TLS_AES_128_GCM_SHA256
```

**TLS 1.2 Approved Cipher Suites (if TLS 1.3 not available):**
```
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
```

**Additional TLS Requirements:**
- Perfect Forward Secrecy (PFS) **REQUIRED**
- Server Name Indication (SNI) **REQUIRED**
- OCSP Stapling **RECOMMENDED**
- HTTP Strict Transport Security (HSTS) **REQUIRED** for web servers

---

### 2.1.3 Key Management Requirements

#### Key Generation

**Requirements:**
- Key generation MUST use cryptographically secure random number generators (CSPRNG)
- Key generation MUST occur in secure, controlled environments
- Entropy sources MUST be documented and adequate
- Weak or predictable random number generators are PROHIBITED

**Approved Methods:**
- Hardware-based random number generators (preferred)
- Operating system CSPRNG (/dev/urandom, CryptGenRandom, etc.)
- HSM-generated keys for critical applications

#### Key Storage

**Hardware Security Module (HSM) REQUIRED for:**
- Root CA private keys
- Database master encryption keys
- Code signing certificates
- Keys protecting >100,000 records
- Any keys classified as "Critical" in risk assessment

**Software Key Storage Requirements:**

When HSM is not mandated, software key storage MUST use:
- Encrypted key stores with strong passphrases (minimum 20 characters)
- Enterprise key management services (KMS)
- Secrets management platforms with role-based access controls
- File system permissions restricting access to authorized processes only

**Storage Security Requirements:**
- Keys MUST be stored separately from the data they protect
- Access to keys MUST be logged and audited
- Keys MUST NOT be stored in application code, configuration files, or version control
- Keys MUST NOT be transmitted via unencrypted channels (email, chat, etc.)

#### Key Rotation

**Mandatory Rotation Schedules:**

| Key Type | Maximum Lifetime | Rotation Trigger |
|----------|------------------|------------------|
| **TLS/SSL certificates** | **397 days** | Industry standard, automated preferred |
| **Symmetric data encryption keys** | **1-2 years** | Risk-based, annual review minimum |
| **Database encryption keys** | **1 year** | Annual rotation required |
| **SSH keys** | **1 year** | Annual + immediate on personnel changes |
| **API keys** | **90 days** | Quarterly rotation required |
| **Service account credentials** | **90 days** | Quarterly rotation required |
| **Root CA keys** | **10 years** | Never rotated, retired at expiry |

**Emergency Rotation:**
- Keys MUST be rotated immediately upon suspected compromise
- Keys MUST be rotated upon personnel termination (privileged access)
- Keys MUST be rotated following security incidents

#### Key Backup and Recovery

**Requirements:**
- Recovery mechanisms MUST be available for critical keys
- Critical keys SHOULD use M-of-N secret sharing (e.g., 3-of-5 scheme)
- Backup procedures MUST be tested quarterly
- Geographic distribution RECOMMENDED for disaster recovery
- Backup encryption MUST use keys managed separately from production

**Recovery Testing:**
- Test key recovery procedures quarterly
- Document recovery times (RTO)
- Verify backup integrity
- Maintain recovery procedure documentation

#### Key Destruction

**Requirements:**
- Key destruction MUST be documented for non-personal keys
- Destruction MUST be cryptographically secure:
  - Software keys: Cryptographic erasure or secure overwrite (DOD 5220.22-M standard)
  - Hardware keys: Physical destruction or HSM-based secure deletion
- If secure destruction is not possible, CISO MUST be notified immediately
- Destruction logs MUST be retained per organizational retention policy

**Media Disposal:**
- Storage media containing keys MUST be destroyed or cryptographically wiped
- Certificate of destruction REQUIRED for hardware containing critical keys

---

### 2.1.4 Key Management Governance

**Key Custody Principle:**
Encryption keys for Restricted data classification MUST be managed by Security Team 
with dual-control requirements. System owners authorize key usage but do not maintain 
sole custody of cryptographic material.

**Rationale:**
Keys are organizational security assets that must be managed independently from the 
systems they protect. This ensures key availability survives system owner changes, 
system decommissioning, and organizational restructuring.

**Implementation:**
Detailed key ownership, custody, and separation of duties requirements are defined 
in Section 3.9 (Roles & Responsibilities).

---

### 2.1.5 Compromised Key Handling

#### Immediate Actions (0-4 hours)

**Upon discovery or suspicion of key compromise:**

1. **Notify** the CISO and Security Team immediately
2. **Isolate** affected systems if necessary to prevent further exposure
3. **Document** timeline of discovery and initial findings
4. **Identify** scope: which keys/certificates are affected
5. **Initiate** incident in incident management system
6. **Revoke** compromised certificates via OCSP/CRL (4-hour SLA)

#### Short-term Actions (4-24 hours)

7. **Generate** replacement keys using approved methods
8. **Issue** new certificates from trusted CA
9. **Deploy** replacement certificates to affected systems
10. **Verify** revocation propagation across systems
11. **Communicate** to internal stakeholders (IT, Management)
12. **Review** access logs for evidence of unauthorized key usage

#### Medium-term Actions (1-7 days)

13. **Rotate** all related cryptographic material (keys that may have been exposed)
14. **Review** all systems that trusted the compromised keys
15. **Update** firewall/IDS signatures if attack patterns identified
16. **External communication** if customer/partner impact confirmed
17. **Regulatory notification** if required by law (e.g., breach notification)

#### Long-term Actions (7-30 days)

18. **Root cause analysis** - determine how compromise occurred
19. **Lessons learned** documentation
20. **Process improvements** identified and implemented
21. **Training/awareness** updates based on incident
22. **Final incident report** to management and audit committee
23. **Update risk register** with new risk scenarios

**Escalation:**
- High-severity key compromises (root CA, master keys) MUST be escalated to executive management within 2 hours
- Customer-impacting compromises MUST involve legal and communications teams

### 2.1.6 Cryptographic Agility and Algorithm Lifecycle Management

**Requirement:**
[Organization] MUST maintain cryptographic agility to respond to algorithm 
deprecations, cryptanalytic advances, and regulatory changes.

**Cryptographic Agility Principles:**
- Algorithms MUST be configurable (not hardcoded in source code)
- Systems MUST support algorithm substitution without complete re-architecture
- Multiple approved algorithms SHOULD be supported during transition periods

**Algorithm Review Triggers:**
Algorithm review MUST be initiated upon:
- Annual cryptographic standards assessment (per Section 4.1.1)
- NIST, BSI, or ENISA deprecation announcement
- Discovery of practical cryptanalytic attack reducing security margin
- Regulatory mandate (PCI DSS updates, DORA requirements, etc.)
- Vendor end-of-support for cryptographic products
- Major security incident involving cryptographic compromise

**Deprecation Response Process:**
Upon deprecation trigger:
1. **Assessment** (30 days): Inventory all systems using deprecated algorithm
2. **Planning** (30 days): Develop transition plan with timelines and resources
3. **Execution** (90-180 days): Migrate to approved replacement algorithm
4. **Verification** (14 days): Confirm complete removal of deprecated algorithm
5. **Documentation**: Update technical standards (ISMS-POL-A.8.24-S5.A)

**Transition Timelines:**
- Critical severity (algorithm break, active exploitation): 30 days maximum
- High severity (regulatory mandate with deadline): 90 days
- Standard deprecation (NIST/BSI sunset notice): 180 days with monitoring

**Compliance Verification:**

### 2.1.7 Certificate Lifetime Agility

**Background:**
CA/Browser Forum Ballot SC-081v3 (passed April 11, 2025) mandates progressive reduction 
of public TLS certificate validity periods, demonstrating real-world need for 
cryptographic agility in operational policy, not just algorithms.

**Certificate Lifetime Timeline:**

| Effective Date | Max Validity | DCV Reuse Period | Operational Impact |
|----------------|--------------|------------------|-------------------|
| Until March 15, 2026 | 398 days | 398 days | Current baseline |
| March 15, 2026 | 200 days | 200 days | Renewal frequency doubles |
| March 15, 2027 | 100 days | 100 days | Renewal frequency quadruples |
| March 15, 2029 | 47 days | 10 days | Renewal frequency increases 8x |

**Organizational Response Strategy:**

[Organization] addresses certificate lifetime reduction through the cryptographic 
agility framework established in Section 2.1.6:

1. **Assessment** (Complete by Q2 2025):
   - Certificate inventory (public vs. private PKI)
   - Current renewal processes (manual vs. automated)
   - System dependencies and integration points
   - Operational capacity analysis

2. **Planning** (Complete by Q3 2025):
   - Automation platform selection
   - Implementation timeline
   - Resource allocation
   - Training requirements

3. **Implementation** (Complete by Q1 2026):
   - Deploy certificate lifecycle management automation
   - Migrate public certificates to automated renewal
   - Implement monitoring and alerting
   - Test renewal processes

4. **Verification** (Before March 15, 2026):
   - Validate automation handles 200-day certificate lifetimes
   - Confirm monitoring alerts functional
   - Execute dry-run renewals
   - Document operational procedures

5. **Continuous Adaptation**:
   - Monitor renewal success rates
   - Prepare for progressive validity reductions (100 days, 47 days)
   - Maintain inventory accuracy
   - Adjust automation as requirements evolve

**Connection to Post-Quantum Preparation:**
Certificate lifetime reduction establishes operational muscle memory for rapid 
cryptographic transitions—essential preparation for eventual post-quantum 
cryptography migration (Section 2.1.6, Appendix A.16.3).

**Policy Review Trigger:**
This section demonstrates why policy review must track CA/Browser Forum baseline 
requirement changes (see Section 4.1 Policy Review Triggers).
Systems using deprecated algorithms after transition deadline are 
non-compliant and subject to Section 4.3 enforcement procedures.

---

## Compliance Verification

**This section SHALL be verified through:**
- Semi-annual cryptographic standards review (aligned with document review cycle)
- Quarterly key management audits
- Automated compliance scanning for approved algorithms
- Certificate inventory and expiration monitoring
- Key rotation compliance tracking

---

## Related Documents

- **ISMS-POL-A.8.24** - Master Policy Framework
- **ISMS-POL-A.8.24-S1** - Purpose, Scope, Definitions
- **ISMS-POL-A.8.24-S2.2** - Data Transmission Requirements
- **ISMS-POL-A.8.24-S2.3** - Data Storage Requirements
- **ISMS-POL-A.8.24-S2.4** - Authentication Requirements
- **ISMS-POL-A.8.24-S2.5** - Compliance Requirements
- **ISMS-POL-A.8.24-S5.A** - Approved Cryptographic Standards (Technical Reference)
- **ISMS-IMP-A.8.24.1** - Data Transmission Assessment
- **ISMS-IMP-A.8.24.4** - Key Management Assessment

---

**End of Section 2.1 - Use of Cryptographic Controls**

*"Anyone who considers arithmetical methods of producing random digits is, of course, in a state of sin."*  
*— John von Neumann (on why true randomness matters in cryptography)*