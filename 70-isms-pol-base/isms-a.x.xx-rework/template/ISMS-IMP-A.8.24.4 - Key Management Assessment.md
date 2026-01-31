# ISMS-IMP-A.8.24.4 - Key Management Assessment

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.24.4 |
| **Version** | 1.0 |
| **Assessment Area** | Key Management Cryptographic Controls |
| **Related Policy** | ISMS-POL-A.8.24, Section 6.5 (Key Management) |
| **Purpose** | Assess implementation of cryptographic key lifecycle management across 5 key management categories (Key Generation, Key Storage, Key Rotation, Key Backup & Recovery, Certificate Management) |
| **Target Audience** | Security Engineers, PKI Administrators, Key Management System (KMS) Administrators, HSM Administrators, Cloud Security Architects, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational (Cryptographic Key Lifecycle) |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Key Management assessment workbook | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** Security Engineers, PKI Administrators, KMS Administrators, HSM Administrators

---

## 1. Assessment Overview

### 1.1 What This Assessment Measures

This assessment evaluates [Organization]'s implementation of **cryptographic key lifecycle management controls** to ensure compliance with ISO/IEC 27001:2022 Control A.8.24 and applicable regulatory requirements.

**Scope:** 5 key management lifecycle categories:
1. **Key Generation** - Entropy sources, algorithm selection, key strength
2. **Key Storage** - HSM, KMS, software keystores, access controls
3. **Key Rotation** - Rotation frequency, automation, algorithm updates
4. **Key Backup & Recovery** - Escrow, disaster recovery, recovery testing
5. **Certificate Management** - Lifecycle automation, expiration monitoring, revocation

**Assessment Output:** Excel workbook documenting key management practices, cryptographic controls, compliance gaps, and remediation plans across all key lifecycle stages.

### 1.2 Why This Matters

**ISO 27001:2022 Control A.8.24 Requirement:**
> *"A policy on the use of cryptographic controls for protection of information should be developed and implemented."*

**Key Management is the Foundation:**
- **IMP-1 (Data Transmission):** Requires valid certificates → Key Management generates and maintains them
- **IMP-2 (Data Storage):** Requires encryption keys → Key Management generates and protects them
- **IMP-3 (Authentication):** Requires password hashing and MFA → Key Management underpins cryptographic authentication
- **IMP-4 (Key Management - THIS ASSESSMENT):** Protects ALL cryptographic keys used in IMP-1, IMP-2, IMP-3

**Regulatory Context:**
- **Swiss nFADP (Art. 8):** Requires appropriate technical measures including key management
- **EU GDPR (Art. 32):** Mandates encryption with proper key management
- **PCI DSS (Req. 3):** Extensive key management requirements for cardholder data
- **Industry Standards:** SOC 2, ISO 27018, NIST 800-57 mandate cryptographic key management

**Business Impact:**
- **Key Compromise:** Single compromised key can decrypt all protected data
- **Key Loss:** Lost encryption keys make data permanently unrecoverable
- **Weak Key Generation:** Predictable keys enable cryptographic attacks
- **Certificate Expiration:** Expired certificates break services organization-wide
- **Compliance Violations:** Poor key management results in audit failures and regulatory fines

**The Security Hierarchy:**
- **Weakest:** Strong encryption with weak key management = Compromisable
- **Strongest:** Strong encryption + strong key management = Defense-in-depth

### 1.3 Who Should Complete This Assessment

**Primary Responsibility:** Security Engineers, PKI Administrators, Key Management System (KMS) Administrators

**Required Knowledge:**
- [Organization]'s key management infrastructure (HSM, KMS, software keystores)
- PKI architecture (CA hierarchy, certificate lifecycle)
- Key generation methods and entropy sources
- Key storage solutions (hardware vs software)
- Key rotation policies and automation
- Key backup and recovery procedures
- Certificate management systems

**Support Roles:**
- **HSM Administrators:** For hardware security module management
- **Cloud Security Team:** For cloud-based KMS (AWS KMS, Azure Key Vault, GCP KMS)
- **PKI Team:** For certificate authority operations
- **Disaster Recovery Team:** For key backup and recovery procedures
- **Compliance Team:** For regulatory key management requirements

### 1.4 Time Estimate

**Total Assessment Time:** 6-8 hours (depending on key infrastructure complexity)

**Breakdown:**
- Information Gathering: 2-2.5 hours (key inventories, key generation methods, storage systems, rotation policies, backup procedures)
- Technical Verification: 1.5-2 hours (entropy source verification, HSM inspection, rotation verification, recovery testing)
- Assessment Completion: 2.5-3 hours (5 key management categories)
- Evidence Collection: 1-1.5 hours (screenshots, configs, test results)
- Quality Review: 30-60 minutes

**Complexity Factors:**
- **Simple:** Single KMS (cloud provider), certificate automation in place, documented procedures - 6 hours
- **Complex:** On-premise HSM, multiple PKIs, manual certificate management, multiple cloud providers - 8+ hours
- **Very Complex:** Multi-site HSM cluster, complex CA hierarchy, extensive certificate inventory, legacy key management - consider team approach

### 1.5 Connection to Policy

This assessment implements **ISMS-POL-A.8.24, Section 6.5 (Key Management)** which defines mandatory controls for:
- Key generation entropy sources (hardware RNG preferred, /dev/random acceptable)
- Key generation algorithms (RSA 2048+ or ECC P-256+, AES-256)
- Key storage security (HSM for high-value keys, KMS for standard keys)
- Key rotation frequency (annually minimum, quarterly for high-risk)
- Key backup and escrow (dual-control, split-knowledge)
- Key recovery testing (annually minimum)
- Certificate lifecycle management (automation required for <100-day validity)
- Certificate expiration monitoring (90-day advance alerts)

**Policy Authority:** Chief Information Security Officer (CISO)  
**Compliance Status:** Mandatory for all cryptographic key management

### 1.6 Critical Policy Requirements Summary

**Key Generation (Section 3.1):**
- **Entropy Source:** Hardware RNG (TPM, HSM) PREFERRED, /dev/random (Linux) ACCEPTABLE, /dev/urandom discouraged for long-term keys
- **Algorithms:** RSA 2048-bit minimum (3072+ preferred), ECDSA P-256 minimum (P-384 preferred), AES-256 for symmetric
- **Key Strength:** Minimum 128-bit security strength (equivalent)
- **Random Number Testing:** NIST SP 800-22 compliance for custom RNG implementations

**Key Storage (Section 3.2):**
- **High-Value Keys (Restricted data, CA signing keys):** HSM REQUIRED (FIPS 140-2 Level 2+ or Common Criteria EAL4+)
- **Standard Keys (Confidential data):** Cloud KMS (AWS KMS, Azure Key Vault, GCP KMS) or software keystore with strong access controls
- **Prohibited:** Keys stored in plaintext, code repositories, config files, environment variables without secrets management

**Key Rotation (Section 3.3):**
- **Encryption Keys:** Annually minimum (quarterly for high-risk, Restricted data)
- **Signing Keys:** 2-3 years maximum (CA root: 10-20 years with strict controls)
- **TLS Certificates:** ≤398 days (until 15.03.2026), ≤200 days (15.03.2026+), ≤100 days (15.03.2027+), ≤47 days (15.03.2029+) - Automation REQUIRED
- **API Keys:** Quarterly (90 days) minimum
- **Automation:** REQUIRED for certificate validity <100 days (ACME protocol)

**Key Backup & Recovery (Section 3.4):**
- **Backup Frequency:** After key generation, before deployment, after rotation
- **Escrow Requirements:** Dual-control (2 persons required for recovery), split-knowledge (key split across multiple escrow locations)
- **Recovery Testing:** Annually minimum, after DR exercises, after personnel changes
- **Backup Encryption:** Backed-up keys MUST be encrypted with separate key (not self-encrypted)

**Certificate Management (Section 3.5):**
- **Expiration Monitoring:** 90-day advance alerts (60-day for critical systems)
- **Revocation Infrastructure:** CRL/OCSP REQUIRED and tested
- **Certificate Inventory:** Complete inventory maintained and reviewed quarterly
- **Automation:** REQUIRED for public CA certificates (approaching 47-day validity by 2029)
- **Certificate Lifecycle:** Automated issuance, renewal, revocation using ACME or equivalent

---

## 2. Prerequisites

### 2.1 Access Required

Before starting this assessment, ensure you have access to:

**Key Management Systems:**
- [ ] Hardware Security Modules (HSM) management console
- [ ] Cloud KMS (AWS KMS, Azure Key Vault, GCP KMS) admin portal
- [ ] Software keystores (Java KeyStore, PKCS#12 files, OpenSSL directories)
- [ ] Secrets management systems (HashiCorp Vault, CyberArk, etc.)

**Certificate Authority (CA):**
- [ ] CA management console (Microsoft CA, OpenSSL CA, Let's Encrypt)
- [ ] Certificate inventory system
- [ ] Certificate lifecycle management tools
- [ ] CRL/OCSP responder configuration

**Key Generation Systems:**
- [ ] Entropy source verification (TPM, HSM, /dev/random)
- [ ] Key generation documentation
- [ ] Random number generator (RNG) test results (if custom implementation)

**Key Backup Systems:**
- [ ] Key escrow system
- [ ] Backup storage (offline, encrypted)
- [ ] Recovery procedures documentation
- [ ] DR runbooks

**Monitoring & Logging:**
- [ ] Certificate expiration monitoring system
- [ ] Key usage logs
- [ ] Key lifecycle audit trails
- [ ] Security information and event management (SIEM) for key events

### 2.2 Knowledge Required

**Essential Understanding:**
- [Organization]'s key management architecture (HSM, KMS, software)
- Cryptographic algorithms in use (RSA, ECDSA, AES)
- Key lifecycle policies (generation, rotation, retirement)
- Certificate management processes (issuance, renewal, revocation)
- Key backup and recovery procedures
- Entropy sources and random number generation

**Technical Skills:**
- Ability to inspect HSM or KMS key inventories
- Understanding of key strength requirements (bit length, security level)
- Certificate lifecycle management concepts
- Key escrow and split-knowledge principles
- DR testing procedures for key recovery

### 2.3 Tools Needed

**Key Inventory Queries:**
```bash
# AWS KMS - List keys
aws kms list-keys

# Azure Key Vault - List keys
az keyvault key list --vault-name <vault-name>

# GCP KMS - List keys
gcloud kms keys list --location=global --keyring=<keyring-name>

# OpenSSL - Check key in file
openssl rsa -in key.pem -check -noout

# Check key bit length
openssl rsa -in key.pem -text -noout | grep "Private-Key"
```

**Entropy Source Verification:**
```bash
# Linux - Check available entropy
cat /proc/sys/kernel/random/entropy_avail

# Linux - Verify hardware RNG
cat /sys/class/misc/hw_random/rng_available

# Check TPM status
tpm2_getcap properties-fixed
```

**Certificate Lifecycle:**
```bash
# Check certificate expiration
openssl x509 -in certificate.crt -noout -dates

# Check certificate key size
openssl x509 -in certificate.crt -noout -text | grep "Public-Key"

# List certificates expiring in 90 days
find /etc/ssl/certs -name "*.crt" -exec openssl x509 -checkend 7776000 -noout -in {} \; -print
```

**Reporting Tools:**
- **Key Inventory Reports:** Export from HSM/KMS management consoles
- **Certificate Expiration Reports:** Certificate lifecycle management tools
- **Key Usage Audit Logs:** SIEM queries for key access events

### 2.4 Estimated Time Commitment

**Phase 1: Information Gathering (2-2.5 hours)**
- Inventory all cryptographic keys (HSM, KMS, software keystores)
- Document key generation methods and entropy sources
- Export certificate inventory
- Review key rotation schedules
- Collect key backup and recovery documentation

**Phase 2: Technical Verification (1.5-2 hours)**
- Verify entropy source (hardware RNG, /dev/random)
- Inspect key bit lengths and algorithms
- Test certificate expiration monitoring
- Verify key backup encryption
- Test key recovery procedure (if possible)

**Phase 3: Assessment Completion (2.5-3 hours)**
- Complete 5 key management category assessment sheets
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

## 3. Assessment Workflow

### 3.1 Recommended Completion Sequence

**STEP 1: Initial Setup (10 minutes)**
1. Download assessment Excel workbook (ISMS-IMP-A.8.24.4_Key_Management_[DATE].xlsx)
2. Open "Instructions & Legend" sheet
3. Complete document information fields
4. Review Status Legend and Evidence Types
5. Skim through all 5 assessment sheets to understand scope

**STEP 2: Start with Key Generation (60-75 minutes - FOUNDATION)**
1. **Sheet 1: Key Generation** ← START HERE (foundation of all key security)
   - Document entropy sources (TPM, HSM, /dev/random, /dev/urandom)
   - Verify key generation algorithms (RSA 2048+, ECDSA P-256+, AES-256)
   - Check key strength (minimum 128-bit security equivalent)
   - Document key generation procedures
   - **CRITICAL:** Weak key generation undermines all other controls
   - **Evidence:** Entropy source verification, key generation logs, algorithm documentation

**STEP 3: Key Storage (60-75 minutes - PROTECTION)**
2. **Sheet 2: Key Storage**
   - Inventory key storage locations (HSM, KMS, software keystores)
   - Classify keys by sensitivity (CA signing keys, encryption keys, TLS keys, API keys)
   - Verify storage security level (HSM for high-value, KMS for standard)
   - Check access controls (who can access keys, how is access logged?)
   - Identify plaintext keys (immediate remediation required)
   - **CRITICAL:** HSM required for CA signing keys and Restricted data encryption keys
   - **Evidence:** HSM inventory, KMS key list, access control policies, audit logs

**STEP 4: Key Rotation (45-60 minutes)**
3. **Sheet 3: Key Rotation**
   - Document rotation policies per key type
   - Verify encryption keys rotated annually minimum
   - Check TLS certificate validity aligns with CA/B Forum SC-081v3 timeline
   - Identify keys never rotated (legacy risk)
   - Verify rotation automation (REQUIRED for <100-day certificate validity)
   - **CRITICAL:** Certificate automation REQUIRED before 15.03.2026 for public CAs
   - **Evidence:** Rotation schedule, certificate validity reports, automation configuration

**STEP 5: Key Backup & Recovery (60-90 minutes - BUSINESS CONTINUITY)**
4. **Sheet 4: Key Backup & Recovery**
   - Document key backup procedures (frequency, method, storage)
   - Verify dual-control and split-knowledge for key recovery
   - Check backup encryption (backed-up keys encrypted with separate key)
   - Review recovery testing schedule (annually minimum)
   - Test key recovery procedure (if safe to do so)
   - **CRITICAL:** Key loss = permanent data loss, recovery MUST be tested
   - **Evidence:** Backup procedures, escrow documentation, recovery test results

**STEP 6: Certificate Management (60-90 minutes - LIFECYCLE)**
5. **Sheet 5: Certificate Management**
   - Export complete certificate inventory
   - Verify expiration monitoring (90-day advance alerts)
   - Check CRL/OCSP configuration and testing
   - Document certificate lifecycle automation (ACME protocol)
   - Identify certificates expiring within 90 days (urgent action)
   - Verify certificate revocation capability
   - **CRITICAL:** Certificate expiration breaks services, automation essential
   - **Evidence:** Certificate inventory, expiration monitoring config, ACME setup, CRL/OCSP tests

**STEP 7: Summary & Evidence (30-45 minutes)**
6. **Summary Dashboard** (auto-calculated, review only)
   - Review overall compliance percentage per key management category
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
12. Ensure all weak key management has risk assessment or remediation plan
13. Set assessment status to "Draft" and submit for review

### 3.2 Tips for Efficient Completion

**Work in Batches:**
- Export all key inventories at once (HSM, AWS KMS, Azure Key Vault, GCP KMS)
- Generate all certificate expiration reports together
- Review all key rotation schedules in one session
- Test key recovery procedures together (if multiple keys)

**Use Automation:**
- Cloud CLI tools for key inventory (aws kms, az keyvault, gcloud kms)
- Certificate lifecycle management tools for expiration reports
- SIEM queries for key usage and access logs
- Automated entropy testing tools

**Leverage Existing Documentation:**
- If recent SOC 2 or ISO audit: Extract key management evidence
- If PKI infrastructure documented: Reuse certificate lifecycle documentation
- If DR testing performed: Extract key recovery test results

**Mark Sections N/A Appropriately:**
- If no HSM: Mark HSM rows as N/A (but note if HSM should be used)
- If no on-premise CA: Mark internal CA rows as N/A
- N/A is acceptable with justification; blank is not acceptable

---

## 4. Question-by-Question Guidance

### 4.1 Section 1: Key Generation

**Assessment Question:**  
*"Does your organization generate cryptographic keys for any purpose (encryption, signing, authentication, TLS certificates)?"*

**How to Answer:**
- **"Yes":** If ANY cryptographic keys are generated (this is 99.9% of organizations)
- **"No":** Only if [Organization] uses exclusively pre-shared keys from vendors (extremely rare)
- **"Not Applicable":** Not appropriate for this section

**Where to Find This Information:**
- HSM management console (key generation logs)
- KMS key creation records (AWS KMS, Azure Key Vault, GCP KMS)
- Certificate authority key generation logs
- Entropy source documentation (/proc/sys/kernel/random/entropy_avail)
- Key generation procedures documentation

**Field-by-Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Key Type** | What is the key used for? | "TLS Certificate", "Database Encryption", "Code Signing", "CA Root Key" | Key inventory, certificate purpose field |
| **Generation Method** | How was key generated? | "HSM", "AWS KMS", "OpenSSL", "Let's Encrypt ACME" | Key generation logs, procedures |
| **Algorithm** | Cryptographic algorithm | "RSA-2048", "RSA-3072", "ECDSA P-256", "AES-256" | Key properties, certificate details |
| **Entropy Source** | Source of randomness | "Hardware RNG (TPM)", "HSM TRNG", "/dev/random", "/dev/urandom" | System documentation, entropy verification |
| **Key Strength (bits)** | Security strength | "2048", "3072", "256", "128-bit equivalent" | Key properties, algorithm documentation |
| **Status** | Compliance status | ✅ / ⚠️ / ❌ / N/A | Based on Compliance Checklist below |

**Entropy Source Verification (CRITICAL):**

**Hardware RNG (PREFERRED):**
```bash
# Check if hardware RNG available (Linux)
cat /sys/class/misc/hw_random/rng_available
# Output: tpm-rng-0 (TPM available)

# Check hardware RNG current
cat /sys/class/misc/hw_random/rng_current

# Verify TPM functionality
tpm2_getcap properties-fixed
```

**Software RNG:**
```bash
# Check available entropy (Linux)
cat /proc/sys/kernel/random/entropy_avail
# Healthy: >1000, Low: <200

# /dev/random - Blocks when entropy depleted (ACCEPTABLE for long-term keys)
# /dev/urandom - Never blocks, refills from PRNG (DISCOURAGED for long-term keys)
```

**HSM TRNG (BEST):**
- Hardware Security Module True Random Number Generator
- FIPS 140-2 or Common Criteria certified
- Best entropy source for high-value keys

**Status Determination:**

**✅ Compliant:** All of these must be true:
- Entropy source: Hardware RNG (TPM, HSM TRNG) OR /dev/random (Linux)
- Algorithm: RSA 2048-bit minimum (3072+ preferred) OR ECDSA P-256 minimum (P-384 preferred) OR AES-256 for symmetric
- Key strength: ≥128-bit security equivalent
- Key generation documented and auditable
- No predictable keys (sequential, timestamp-based, weak seeds)

**⚠️ Partial:** Some requirements met but gaps exist:
- Entropy source: /dev/urandom used for long-term keys (should use /dev/random or hardware RNG)
- Algorithm: RSA 2048-bit (acceptable but 3072+ preferred)
- Key strength: 128-bit equivalent (acceptable but 256-bit preferred)
- Key generation not fully documented

**❌ Non-Compliant:** Critical failures:
- Weak algorithms (RSA 1024-bit, DES, 3DES, MD5-based key derivation)
- Predictable entropy source (timestamp, sequential, weak PRNG)
- No documentation of key generation procedures
- Keys generated on insecure systems (developer laptops without TPM)

**N/A:** Keys not generated by organization (all keys provided by external vendors)

**Compliance Checklist Guidance:**

- [ ] **Hardware RNG (TPM, HSM) OR /dev/random used for long-term keys**  
  *Verify:* Check entropy source in key generation logs or system config  
  *Best:* HSM TRNG for CA root keys and high-value keys  
  *Acceptable:* /dev/random for standard keys  
  *Discouraged:* /dev/urandom for long-term keys (acceptable for session keys)  

- [ ] **RSA 2048-bit minimum (3072+ preferred) OR ECDSA P-256 minimum**  
  *Verify:* `openssl rsa -in key.pem -text -noout | grep "Private-Key"`  
  *Modern trend:* ECDSA P-256 provides equivalent security to RSA-3072 with smaller keys  

- [ ] **AES-256 for symmetric encryption keys**  
  *Verify:* Check KMS key configuration or encryption configuration  
  *Note:* AES-128 acceptable for performance-critical applications with risk acceptance  

- [ ] **Minimum 128-bit security strength (equivalent)**  
  *Examples:* RSA 2048-bit ≈ 112-bit strength, RSA 3072-bit ≈ 128-bit strength, ECDSA P-256 ≈ 128-bit strength  
  *Target:* 128-bit strength minimum, 256-bit preferred  

- [ ] **Key generation procedures documented**  
  *Required:* Who can generate keys, approval process, entropy source verification  
  *Purpose:* Auditability and repeatability  

- [ ] **No predictable key generation (weak seeds, timestamps)**  
  *Common mistake:* Using current timestamp as seed for random number generator  
  *Test:* Review key generation code or procedures for weak entropy sources  

**Evidence Examples for Section 1:**
- Entropy source verification: `EV-1-Entropy-Source-20260115.txt` (cat /proc/sys/kernel/random/entropy_avail)
- Hardware RNG status: `EV-1-Hardware-RNG-20260115.txt` (cat /sys/class/misc/hw_random/rng_available)
- Key bit length verification: `EV-1-Key-Bitlength-20260115.txt` (openssl rsa -text output)
- HSM key generation log: `EV-1-HSM-KeyGen-Log-20260115.pdf`
- Key generation procedures: `EV-1-KeyGen-Procedures-20260115.pdf`

**Common Issues:**

**Issue:** /dev/urandom used for CA root key generation  
**Solution:** Regenerate CA root key using /dev/random or HSM TRNG (major undertaking - plan carefully)

**Issue:** RSA 1024-bit keys still in use  
**Solution:** Immediate migration to RSA 2048+ or ECDSA P-256+, force certificate reissuance

**Issue:** Low entropy available (<200) during key generation  
**Solution:** Install hardware RNG (rng-tools, haveged) or wait for entropy to accumulate before generating keys

---

### 4.2 Section 2: Key Storage

**Assessment Question:**  
*"Where does your organization store cryptographic keys (HSM, KMS, software keystores, config files)?"*

**How to Answer:**
- **"Yes":** If ANY cryptographic keys are stored (this is 100% of organizations using crypto)
- **"No":** Not possible if organization generates or uses keys
- **"Not Applicable":** Not appropriate

**Where to Find This Information:**
- HSM inventory reports
- Cloud KMS key lists (AWS KMS, Azure Key Vault, GCP KMS)
- Software keystore locations (Java KeyStore, PKCS#12 files, OpenSSL directories)
- Secrets management systems (HashiCorp Vault, CyberArk)
- Code repositories (check for hardcoded keys - PROHIBITED)

**Key Storage Security Hierarchy (Best to Worst):**

1. **Hardware Security Module (HSM) - BEST**
   - FIPS 140-2 Level 2+ or Common Criteria EAL4+
   - Physical tamper resistance
   - Keys never leave HSM in plaintext
   - **Use for:** CA signing keys, Restricted data encryption keys, payment processing keys

2. **Cloud KMS (Key Management Service) - GOOD**
   - AWS KMS, Azure Key Vault, GCP KMS
   - Hardware-backed (HSMs behind the scenes)
   - Strong access controls and audit logging
   - **Use for:** Confidential data encryption keys, standard TLS keys, database encryption keys

3. **Software Keystore - ACCEPTABLE (with strong access controls)**
   - Java KeyStore (JKS), PKCS#12 files, OpenSSL key files
   - Protected by file system permissions and encryption
   - **Use for:** Internal data encryption keys, development/test keys

4. **Secrets Management - ACCEPTABLE**
   - HashiCorp Vault, CyberArk, AWS Secrets Manager
   - Centralized secrets storage with access controls
   - **Use for:** Application secrets, API keys, service account credentials

5. **Config Files (encrypted) - POOR (but better than plaintext)**
   - Configuration files with encrypted keys
   - Requires separate key to decrypt (key-encryption-key)
   - **Use for:** Low-sensitivity keys only, temporary keys

6. **Config Files (plaintext), Code Repositories - PROHIBITED**
   - Plaintext keys in files, hardcoded in code, committed to git
   - **IMMEDIATE REMEDIATION REQUIRED**

**Field-by-Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Key Type** | What is the key used for? | "CA Root Key", "TLS Private Key", "Database Master Key", "API Key" | Key inventory |
| **Storage Location** | Where is key stored? | "HSM (Thales Luna)", "AWS KMS", "File: /etc/ssl/private/", "Azure Key Vault" | Key storage inventory |
| **Storage Security Level** | Security classification | "HSM (FIPS 140-2 L3)", "Cloud KMS", "Software Keystore", "Plaintext (non-compliant)" | Storage system specs |
| **Access Controls** | Who can access key? | "2 HSM operators (dual-control)", "IAM role: KMS_Admin", "File permissions: 600 root" | Access control policies |
| **Audit Logging** | Is key access logged? | "Yes (HSM audit log)", "Yes (CloudTrail)", "No" | Logging configuration |
| **Status** | Compliance status | ✅ / ⚠️ / ❌ / N/A | Based on checklist |

**Status Determination:**

**✅ Compliant:**
- High-value keys (CA signing, Restricted data) stored in HSM (FIPS 140-2 L2+ or CC EAL4+)
- Standard keys stored in Cloud KMS or software keystore with strong access controls
- All key access logged and auditable
- No plaintext keys in config files or code repositories

**⚠️ Partial:**
- High-value keys in Cloud KMS (should be in HSM)
- Software keystore without strong access controls
- Some key access not logged
- Key storage locations not fully documented

**❌ Non-Compliant:**
- Plaintext keys in config files or code repositories
- No access controls on key files
- CA signing keys not in HSM
- No audit logging of key access

**Compliance Checklist:**

- [ ] **High-value keys stored in HSM (FIPS 140-2 Level 2+ or CC EAL4+)**  
  *High-value:* CA signing keys, Restricted data encryption, payment processing  
  *Verify:* HSM inventory shows these keys present  

- [ ] **Standard keys stored in Cloud KMS or secure software keystore**  
  *Standard:* Confidential data encryption, TLS keys, database keys  
  *Cloud KMS:* AWS KMS, Azure Key Vault, GCP KMS  

- [ ] **No plaintext keys in config files, code repositories, or environment variables**  
  *Check:* grep -r "BEGIN.*PRIVATE KEY" in code repos, config directories  
  *Immediate remediation required if found*  

- [ ] **Strong access controls on all key storage locations**  
  *HSM:* Dual-control, M-of-N authentication  
  *Cloud KMS:* IAM policies, least privilege  
  *File system:* 600 permissions (owner read/write only), root ownership  

- [ ] **All key access logged and monitored**  
  *HSM:* HSM audit logs  
  *Cloud KMS:* CloudTrail (AWS), Azure Monitor, GCP Audit Logs  
  *File system:* auditd or equivalent  

- [ ] **Key backup encrypted with separate key (not self-encrypted)**  
  *Purpose:* If encryption key compromised, backup not also compromised  
  *Method:* Key-encryption-key (KEK) or HSM master key  

**Evidence Examples:**
- HSM inventory: `EV-2-HSM-Key-Inventory-20260115.pdf`
- Cloud KMS key list: `EV-2-AWS-KMS-Keys-20260115.txt`
- File system key permissions: `EV-2-File-Permissions-20260115.txt` (ls -la /etc/ssl/private)
- Access control policies: `EV-2-IAM-KMS-Policies-20260115.json`
- Audit log sample: `EV-2-HSM-Audit-Log-Sample-20260115.pdf`

**Common Issues:**

**Issue:** CA signing key in software keystore (not HSM)  
**Solution:** Migrate CA signing key to HSM, plan CA re-keying

**Issue:** Plaintext private keys found in /etc/config/app.conf  
**Solution:** Immediate rotation, migrate to secrets management (Vault, Key Vault)

**Issue:** No audit logging for key access  
**Solution:** Enable CloudTrail (AWS), Azure Monitor, or auditd depending on platform

---

### 4.3 Additional Sections Summary (4.4 through 4.6)

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
- **4.4: Key Rotation** (Rotation frequency, automation, algorithm updates, certificate validity timeline SC-081v3)
- **4.5: Key Backup & Recovery** (Escrow, dual-control, split-knowledge, recovery testing)
- **4.6: Certificate Management** (Lifecycle automation, expiration monitoring, CRL/OCSP, ACME protocol)

**Key Principles Applied to All Sections:**
- Key lifecycle management is continuous, not one-time
- Automation essential for short-lived certificates (<100 days)
- Recovery testing must be performed (not just documented)
- Evidence must be specific and verifiable
- Common pitfalls identified and solutions provided

---

## 5. Evidence Collection

### 5.1 General Evidence Guidelines

**Evidence Naming Convention:**
```
EV-[Section]-[System]-[Date]-[Type].[ext]
```

**Examples:**
- `EV-1-Entropy-Source-20260115.txt`
- `EV-2-HSM-Key-Inventory-20260115.pdf`
- `EV-3-Certificate-Rotation-Schedule-20260115.xlsx`
- `EV-4-Key-Recovery-Test-20260115.pdf`
- `EV-5-Certificate-Expiration-Report-20260115.xlsx`

**Storage Requirements:**
- **Location:** Centralized evidence repository (same as IMP-1, IMP-2, IMP-3)
- **Folder Structure:** Organize by assessment section
- **Retention:** Audit cycle + 1 year minimum
- **Sensitivity:** Key management documentation is highly sensitive - strict access controls

**Evidence Quality Criteria:**
- **Timestamped:** Must show date/time of collection
- **Complete:** Full reports/screenshots (no partial data)
- **Attributable:** Clear which system/key it documents
- **Verifiable:** Auditor can reproduce
- **Protected:** Stored securely, NO private keys in evidence

### 5.2 Evidence Types by Section

**1. Key Generation:**
- Entropy source verification (cat /proc/sys/kernel/random/entropy_avail)
- Hardware RNG status (TPM, HSM TRNG availability)
- Key bit length verification (openssl rsa -text output, sanitized)
- Key generation logs (HSM, KMS, CA logs - sanitized)
- Key generation procedures documentation

**2. Key Storage:**
- HSM inventory report (key count, types, FIPS level)
- Cloud KMS key list (AWS CLI, Azure CLI, gcloud output)
- File system key permissions (ls -la /etc/ssl/private)
- Access control policies (IAM policies, file ACLs)
- Audit log samples (HSM audit log, CloudTrail, Azure Monitor)

**3. Key Rotation:**
- Key rotation schedule documentation
- Certificate validity reports (expiring certificates list)
- Rotation automation configuration (ACME setup, automated scripts)
- Historical rotation evidence (key retirement logs)

**4. Key Backup & Recovery:**
- Key backup procedures documentation
- Escrow configuration (dual-control, split-knowledge)
- Recovery test results (most recent test)
- Backup encryption verification

**5. Certificate Management:**
- Complete certificate inventory (all active certificates)
- Certificate expiration monitoring configuration (90-day alerts)
- CRL/OCSP configuration and test results
- ACME protocol setup (Let's Encrypt, Sectigo, DigiCert)
- Certificate lifecycle automation documentation

### 5.3 Tools for Evidence Collection

**Key Inventory:**
```bash
# AWS KMS - List keys
aws kms list-keys --output table

# Azure Key Vault - List keys
az keyvault key list --vault-name <vault-name> --output table

# GCP KMS - List keys
gcloud kms keys list --location=global --keyring=<keyring-name>

# OpenSSL - List certificates in directory
for cert in /etc/ssl/certs/*.crt; do 
  echo "=== $cert ==="
  openssl x509 -in $cert -noout -subject -dates
done
```

**Entropy Verification:**
```bash
# Available entropy
cat /proc/sys/kernel/random/entropy_avail > EV-1-Entropy-Available-$(date +%Y%m%d).txt

# Hardware RNG
cat /sys/class/misc/hw_random/rng_available > EV-1-Hardware-RNG-$(date +%Y%m%d).txt
```

**Certificate Expiration:**
```bash
# Certificates expiring within 90 days
find /etc/ssl/certs -name "*.crt" -exec openssl x509 -checkend 7776000 -noout -in {} \; -print > EV-5-Expiring-Certs-$(date +%Y%m%d).txt
```

### 5.4 Evidence Sanitization

**CRITICAL:** Remove sensitive information:

**Must Sanitize (NEVER include in evidence):**
- Private keys (ANY form - PEM, DER, PKCS#12)
- HSM PIN codes or authentication credentials
- Key encryption keys (KEK)
- Backup passphrases
- HSM administrator passwords

**Safe to Include:**
- Public keys and public certificates
- Key algorithms and bit lengths (RSA-2048, ECDSA P-256)
- Key identifiers (key IDs, key aliases - NOT the key material)
- Certificate expiration dates
- Key rotation schedules
- Entropy source specifications
- Access control policies (redact credentials)

---

## 6. Common Pitfalls

### ❌ MISTAKE #1: Assuming HSM = Secure (Without Proper Configuration)

**Problem:** "We have an HSM, so our keys are secure"  
**Why Wrong:** Misconfigured HSM with weak access controls or single-person recovery negates security benefits  
**Correct Approach:** Verify HSM configuration (dual-control, M-of-N, audit logging enabled)  
**Impact:** False sense of security, HSM compromise possible

---

### ❌ MISTAKE #2: /dev/urandom for Long-Term Keys

**Problem:** Using /dev/urandom for CA root key or long-term encryption keys  
**Why Wrong:** /dev/urandom uses PRNG when entropy depleted (predictable if attacked)  
**Correct Approach:** Use /dev/random (blocks until entropy available) or hardware RNG for long-term keys  
**Impact:** Potentially predictable keys if generated during low-entropy conditions

---

### ❌ MISTAKE #3: No Key Recovery Testing ("We Have Backups")

**Problem:** Key backups documented but never tested  
**Why Wrong:** Discovery of non-recoverable backups during actual disaster = data loss  
**Correct Approach:** Annual recovery testing minimum, test after DR exercises  
**Impact:** Permanent data loss when keys needed for recovery

---

### ❌ MISTAKE #4: Certificate Automation "Coming Soon" (15.03.2026 Approaching)

**Problem:** Manual certificate management with automation "planned" but not implemented  
**Why Wrong:** CA/B Forum reduces certificate validity to 47 days by 2029, manual processes won't scale  
**Correct Approach:** Implement ACME automation NOW (before 15.03.2026 deadline for 200-day certificates)  
**Impact:** Certificate management crisis, service outages from expired certificates

---

### ❌ MISTAKE #5: Keys in Config Files "Just for Dev"

**Problem:** Private keys in config files marked "development only"  
**Why Wrong:** Dev configs propagate to production, developers commit to git repos  
**Correct Approach:** Zero plaintext keys anywhere - use secrets management (Vault, Key Vault) for dev AND prod  
**Impact:** Key compromise from git history or accidentally deployed configs

---

### ❌ MISTAKE #6: No Monitoring for Certificate Expiration

**Problem:** Certificates expire without advance warning  
**Why Wrong:** Certificate expiration causes service outages, often organization-wide  
**Correct Approach:** 90-day advance alerts minimum (60-day for critical), automated monitoring  
**Impact:** Unexpected service outages, emergency certificate renewals

---

### ❌ MISTAKE #7: Single-Person Key Recovery (No Dual-Control)

**Problem:** One person can recover all keys from escrow  
**Why Wrong:** Insider threat, no accountability, single point of failure if person unavailable  
**Correct Approach:** Dual-control (2 persons required) or M-of-N split-knowledge  
**Impact:** Insider key theft, key recovery impossible if sole person unavailable

---

### ❌ MISTAKE #8: RSA 1024-bit "Good Enough for Internal"

**Problem:** Using RSA 1024-bit keys for internal systems ("not exposed to internet")  
**Why Wrong:** RSA 1024-bit factorization feasible with modern computing, insiders have access  
**Correct Approach:** RSA 2048-bit minimum for ALL keys (internal and external)  
**Impact:** Cryptographic compromise via factorization or quantum computing

---

### ❌ MISTAKE #9: Key Rotation "When We Remember"

**Problem:** No formal key rotation schedule, rotation done ad-hoc  
**Why Wrong:** Keys never rotated, long-lived keys accumulate risk  
**Correct Approach:** Annual rotation minimum (quarterly for high-risk), calendar reminders  
**Impact:** Long-lived keys (>5 years) exposed to increased cryptanalytic attacks

---

### ❌ MISTAKE #10: CRL/OCSP "Configured" But Never Tested

**Problem:** Certificate revocation configured but never verified it works  
**Why Wrong:** Revoked certificates still accepted = compromised keys still valid  
**Correct Approach:** Test revocation with actual revoked certificate, verify client rejects  
**Impact:** Compromised certificates remain valid despite revocation

---

## 7. Quality Checklist

**Complete this checklist before submitting assessment for review:**

### Completeness Checks
- [ ] All 5 assessment sections completed (or marked N/A with justification)
- [ ] Every yellow data entry cell filled in
- [ ] Status dropdown selected for every applicable item
- [ ] Evidence location documented for every key management control
- [ ] Gap descriptions completed for all Partial/Non-Compliant items
- [ ] Entropy sources verified (not assumed)
- [ ] Key storage locations documented (HSM, KMS, software)
- [ ] Remediation plans with dates for all gaps
- [ ] Compliance checklists completed for all sections
- [ ] Summary Dashboard reviewed and totals make sense
- [ ] Evidence Register populated
- [ ] All evidence files exist and are accessible (NO PRIVATE KEYS)

### Accuracy Checks
- [ ] Entropy sources verified (hardware RNG, /dev/random, /dev/urandom)
- [ ] Key bit lengths verified (not assumed - checked with openssl or equivalent)
- [ ] Key storage security levels accurate (HSM FIPS level, Cloud KMS, software)
- [ ] Key rotation frequencies documented from actual schedules
- [ ] Certificate expiration dates verified (not estimated)
- [ ] Recovery testing dates documented (actual test results)
- [ ] No plaintext keys anywhere (config files, code repos checked)

### Policy Alignment Checks
- [ ] High-value keys in HSM (CA signing, Restricted data encryption)
- [ ] Standard keys in Cloud KMS or secure software keystore
- [ ] Key generation uses approved algorithms (RSA 2048+, ECDSA P-256+, AES-256)
- [ ] Entropy sources: Hardware RNG or /dev/random for long-term keys
- [ ] Key rotation: Annually minimum (quarterly for high-risk)
- [ ] Certificate validity aligns with CA/B Forum SC-081v3 timeline
- [ ] Certificate automation implemented or planned (deadline: 15.03.2026)
- [ ] Key backup uses dual-control or split-knowledge
- [ ] Recovery testing performed annually minimum
- [ ] Certificate expiration monitoring: 90-day advance alerts

### Audit Readiness Checks
- [ ] Evidence is verifiable (auditor could reproduce)
- [ ] Evidence is timestamped and attributable
- [ ] NO private keys in evidence (public keys and certificates only)
- [ ] Evidence organized logically and consistently named
- [ ] Assessment tells clear story from beginning to end
- [ ] Key management practices not "assumed" - all verified with evidence

### Red Flags to Address BEFORE Submission
- [ ] No plaintext private keys in config files or code repositories
- [ ] No weak algorithms (RSA 1024, DES, 3DES, MD5)
- [ ] No CA signing keys outside HSM
- [ ] No certificates expiring within 90 days without renewal plan
- [ ] No keys never rotated (check for >3 year old keys)
- [ ] No untested key recovery procedures
- [ ] Overall compliance rate >80% (if <80%, indicates systemic issue)

### Final Sanity Checks
- [ ] Summary Dashboard totals match manual count
- [ ] Assessment owner name and role completed
- [ ] Assessment date correct
- [ ] Organization name filled in
- [ ] Next Review Date set (quarterly)
- [ ] Assessment status set to "Draft"

**If ANY checkbox above is unchecked: STOP. Complete missing item before submitting.**

---

## 8. Review & Approval

### 8.1 Review Process

**Step 1: Self-Review** (Assessment Owner)
- Run through Quality Checklist (Section 7)
- Fix identified issues
- Verify all evidence accessible (and sanitized - no private keys!)
- Set status to "Draft"
- Submit to Information Security Officer

**Step 2: Technical Review** (Information Security Officer)
- Verify entropy sources documented
- Validate key storage security levels appropriate
- Assess key rotation schedules realistic
- Check certificate automation plan (15.03.2026 deadline)
- Verify recovery testing performed
- Provide feedback

**Step 3: Remediation (if needed)** (Assessment Owner)
- Address review feedback
- Update assessment
- Re-submit if significant changes

**Step 4: Final Approval** (CISO)
- Review overall key management posture
- Approve remediation timelines
- Accept documented risks
- Sign off assessment
- Set Next Review Date

### 8.2 Approval Timeline

**Typical Timeline:**
- Assessment completion: 6-8 hours (owner)
- Self-review: 30-60 minutes (owner)
- Technical review: 2-3 business days (ISO)
- Remediation: 1-2 hours (owner)
- Final approval: 1-2 business days (CISO)
- **Total:** 1-2 weeks start to finish

### 8.3 After Approval

**Immediate Actions:**
1. File approved assessment in ISMS repository
2. Distribute to relevant stakeholders
3. Track remediation items in project system
4. Schedule follow-up reviews

**Ongoing Monitoring:**
- Certificate expiration monitoring (continuous, 90-day alerts)
- Key rotation schedule tracking (quarterly reviews)
- HSM audit log reviews (quarterly)
- Key backup testing (annually)
- Entropy source health checks (quarterly)

**Triggers for Immediate Re-Assessment:**
- Key compromise or suspected compromise
- HSM failure or maintenance
- Certificate expiration incident (service outage)
- Discovery of plaintext keys
- CA/B Forum ballot changes (certificate validity)
- Failed audit findings on key management
- Major infrastructure changes (new HSM, KMS migration)

### 8.4 Continuous Improvement

**Use Assessment Results to Improve:**
- Pattern of weak entropy? → Implement hardware RNG (TPM, HSM)
- Keys in config files? → Migrate to secrets management (Vault, Key Vault)
- Certificate expiration incidents? → Implement ACME automation
- No recovery testing? → Schedule annual recovery drills
- CA signing key not in HSM? → Plan HSM procurement and CA migration

**Feedback Loop:**
- Assessment owner provides feedback on this guide
- ISO reviews common questions/issues
- Update guide for next assessment cycle

---

## PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

## Instructions for Completing This Assessment

### How to Use This Document

This technical specification defines the structure, validation rules, and formulas for the Key Management Assessment Excel workbook (`ISMS-IMP-A.8.24.4_Key_Management_[DATE].xlsx`).

**Workbook Generation:** Python script `generate_a824_4_key_management_assessment.py` creates the workbook based on this specification.

**Assessment Completion Process:**

1. **Read each section** and determine if the key management practice applies to your organization
2. **Check Yes/No/Not Applicable** for each assessment question
3. **If Yes:** Complete the assessment table with current key management controls
4. **Mark Status:** ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant / N/A
5. **If ⚠️ or ❌:** Complete the Exception/Deviation Documentation section
6. **Provide Evidence:** Document where compliance evidence can be found
7. **Review Compliance Checklist:** Check all items that apply to your implementation

### Status Legend

| Symbol | Meaning | Description |
|--------|---------|-------------|
| **✅** | **Compliant** | Fully meets policy requirements, no gaps identified |
| **⚠️** | **Partial** | Some requirements met, minor gaps exist, remediation planned |
| **❌** | **Non-Compliant** | Does not meet policy requirements, significant gaps |
| **N/A** | **Not Applicable** | This requirement does not apply to your environment |

### Evidence Types

Acceptable evidence includes:
- HSM inventory reports and configuration documentation
- Cloud KMS key lists and access policies
- Key generation procedures and entropy source verification
- Key rotation schedules and automation configuration
- Key backup and recovery procedures
- Recovery test results
- Certificate inventory and expiration monitoring
- ACME protocol configuration (Let's Encrypt, etc.)
- Audit logs (HSM logs, CloudTrail, Azure Monitor)

---

## Common Column Structure (All Assessment Sheets)

All 5 assessment sheets use this standard column layout:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | Key Type / Purpose | 30 | Text | Free text |
| B | Generation Method | 22 | Dropdown | HSM, AWS KMS, Azure Key Vault, GCP KMS, OpenSSL, Let's Encrypt ACME, Manual, N/A |
| C | Algorithm | 20 | Dropdown | RSA-2048, RSA-3072, RSA-4096, ECDSA P-256, ECDSA P-384, AES-256, AES-128, N/A |
| D | Key Strength (bits) | 18 | Dropdown | 256, 192, 128, 2048, 3072, 4096, N/A |
| E | Storage Location | 25 | Dropdown | HSM, AWS KMS, Azure Key Vault, GCP KMS, Software Keystore, Config File, N/A |
| F | Storage Security Level | 20 | Dropdown | HSM (FIPS 140-2 L2+), Cloud KMS, Software Keystore, Plaintext (Non-compliant), N/A |
| G | Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| H | Evidence Location | 28 | Text | Free text (file path or evidence ID) |
| I | Gap Description | 30 | Text | Free text (required if Status = Partial/Non-Compliant) |
| J | Remediation Needed | 14 | Dropdown | Yes, No |
| K | Exception ID | 14 | Text | Free text (if formal exception submitted) |
| L | Risk ID | 14 | Text | Free text (if risk accepted) |
| M | Compensating Controls | 30 | Text | Free text (if applicable) |
| N | Responsible Person | 20 | Text | Free text (name and role) |
| O | Target Date | 14 | Date | Date picker (DD.MM.YYYY) |
| P | Budget Required | 15 | Dropdown | Yes, No, Unknown |

---

## 1. Key Generation

**Policy Requirement:** Cryptographic keys MUST be generated using approved algorithms (RSA 2048+, ECDSA P-256+, AES-256) with sufficient entropy from hardware RNG (preferred) or /dev/random (acceptable) (Policy Section 3.1)

**Assessment Question:**

**Does your organization generate cryptographic keys for any purpose (encryption, signing, authentication, TLS certificates)?**
- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 2
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Key Type / Purpose | Generation Method | Algorithm | Key Strength (bits) | Entropy Source | Status | Evidence Location | Gap Description | Remediation Needed |
|-------------------|-------------------|-----------|--------------------|-----------------| ---------|-------------------|-----------------|-------------------|
| Example: TLS Certificate, Database Encryption Key, CA Root Key, Code Signing Key | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Key Generation-Specific Additional Columns:**

| Column | Header | Width | Validation Options |
|--------|--------|-------|--------------------|
| Q | Entropy Source | 22 | Hardware RNG (TPM/HSM), /dev/random, /dev/urandom, Other, N/A |
| R | Security Strength | 18 | 256-bit, 192-bit, 128-bit, <128-bit (weak), N/A |
| S | NIST SP 800-22 Tested | 16 | Yes, No, N/A |

**Additional Details:**
- **Total keys generated annually:** _________
- **Primary key generation system:** [ ] HSM [ ] Cloud KMS [ ] OpenSSL [ ] Let's Encrypt [ ] Other: _____
- **Entropy source health monitoring:** [ ] Continuous [ ] Periodic [ ] None

---

**KEY GENERATION COMPLIANCE CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| Hardware RNG (TPM, HSM) OR /dev/random used for long-term keys | [ ] Yes [ ] No [ ] N/A | /dev/urandom discouraged for long-term |
| RSA 2048-bit minimum (3072+ preferred) OR ECDSA P-256 minimum | [ ] Yes [ ] No [ ] N/A | Verify: openssl rsa -text -noout |
| AES-256 for symmetric encryption keys | [ ] Yes [ ] No [ ] N/A | AES-128 acceptable with risk acceptance |
| Minimum 128-bit security strength (equivalent) | [ ] Yes [ ] No [ ] N/A | RSA 2048 ≈ 112-bit, RSA 3072 ≈ 128-bit |
| Key generation procedures documented | [ ] Yes [ ] No [ ] N/A | Who, what, when, how, why |
| No predictable key generation (weak seeds, timestamps) | [ ] Yes [ ] No [ ] N/A | Review key generation code |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**
- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Enhanced monitoring of key usage
  - [ ] Restricted key scope (limited use cases)
  - [ ] Key rotation more frequent than policy minimum
  - [ ] Other: _______________________________

**Remediation Plan:**
- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________
- **Budget required:** [ ] Yes [ ] No  Amount: _________

---

## 2. Key Storage

**Policy Requirement:** High-value keys (CA signing keys, Restricted data encryption) MUST be stored in HSM (FIPS 140-2 Level 2+ or CC EAL4+). Standard keys MUST use Cloud KMS or secure software keystore with strong access controls. Plaintext keys in config files or code repositories PROHIBITED (Policy Section 3.2)

**Assessment Question:**

**Where does your organization store cryptographic keys (HSM, KMS, software keystores, config files)?**
- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 3
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Key Type / Purpose | Storage Location | Storage Security Level | Access Controls | Audit Logging | Status | Evidence Location | Gap Description | Remediation Needed |
|-------------------|------------------|----------------------|-----------------|---------------| ---------|-------------------|-----------------|-------------------|
| Example: CA Root Key, TLS Private Key, Database Master Key, API Key | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Key Storage-Specific Additional Columns:**

| Column | Header | Width | Validation Options |
|--------|--------|-------|--------------------|
| Q | HSM FIPS Level | 18 | FIPS 140-2 L3, FIPS 140-2 L2, FIPS 140-2 L1, N/A (not HSM) |
| R | Access Control Method | 22 | Dual-control (M-of-N), IAM Policy, File Permissions, None, N/A |
| S | Audit Logging Enabled | 16 | Yes (HSM log), Yes (CloudTrail), Yes (auditd), No |

**Additional Details:**
- **Total keys stored:** _________
- **Storage systems in use:** [ ] HSM [ ] AWS KMS [ ] Azure Key Vault [ ] GCP KMS [ ] Software Keystore [ ] Other: _____
- **Plaintext keys found:** [ ] Yes (immediate remediation) [ ] No

---

**KEY STORAGE COMPLIANCE CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| High-value keys stored in HSM (FIPS 140-2 Level 2+ or CC EAL4+) | [ ] Yes [ ] No [ ] N/A | CA signing, Restricted data encryption |
| Standard keys stored in Cloud KMS or secure software keystore | [ ] Yes [ ] No [ ] N/A | Confidential data encryption, TLS keys |
| No plaintext keys in config files, code repositories, or environment variables | [ ] Yes [ ] No [ ] N/A | CRITICAL - check git history |
| Strong access controls on all key storage locations | [ ] Yes [ ] No [ ] N/A | HSM: dual-control, Cloud: IAM, File: 600 perms |
| All key access logged and monitored | [ ] Yes [ ] No [ ] N/A | HSM audit log, CloudTrail, auditd |
| Key backup encrypted with separate key (not self-encrypted) | [ ] Yes [ ] No [ ] N/A | KEK or HSM master key |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**
- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Key usage restricted to specific systems/IPs
  - [ ] Enhanced monitoring and alerting
  - [ ] Key isolated to specific environment
  - [ ] Other: _______________________________

**Remediation Plan:**
- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

## 3. Key Rotation

**Policy Requirement:** Encryption keys MUST be rotated annually minimum (quarterly for high-risk, Restricted data). TLS certificates MUST follow CA/Browser Forum SC-081v3 timeline: ≤398d (until 15.03.2026), ≤200d (15.03.2026+), ≤100d (15.03.2027+), ≤47d (15.03.2029+). Automation REQUIRED for certificate validity <100 days (Policy Section 3.3)

**Assessment Question:**

**Does your organization rotate cryptographic keys and certificates according to policy requirements?**
- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 4
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Key Type / Purpose | Current Rotation Frequency | Last Rotation Date | Automation Status | Status | Evidence Location | Gap Description | Remediation Needed |
|-------------------|---------------------------|-------------------|------------------| ---------|-------------------|-----------------|-------------------|
| Example: Encryption Keys, TLS Certificates, API Keys, Signing Keys | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Key Rotation-Specific Additional Columns:**

| Column | Header | Width | Validation Options |
|--------|--------|-------|--------------------|
| Q | Policy Rotation Frequency | 20 | Quarterly (90d), Semi-annual (180d), Annual (365d), 2-3 years, Other |
| R | Certificate Validity (if applicable) | 18 | ≤398d, ≤200d, ≤100d, ≤47d, >398d (non-compliant), N/A |
| S | Automation Method | 22 | ACME (Let's Encrypt), Automated Script, Manual, N/A |
| T | Next Rotation Date | 18 | Date (DD.MM.YYYY) |

**Additional Details:**
- **Total keys requiring rotation:** _________
- **Keys overdue for rotation:** _________
- **Certificate automation status:** [ ] Fully automated [ ] Partially automated [ ] Manual (requires migration) [ ] N/A
- **ACME protocol in use:** [ ] Yes [ ] No [ ] Planned

---

**KEY ROTATION COMPLIANCE CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| Encryption keys rotated annually minimum (quarterly for high-risk) | [ ] Yes [ ] No [ ] N/A | Check last rotation date |
| TLS certificates: ≤398d (until 15.03.2026), progressive reduction thereafter | [ ] Yes [ ] No [ ] N/A | CA/B Forum SC-081v3 timeline |
| Certificate automation implemented or planned (deadline: 15.03.2026) | [ ] Yes [ ] No [ ] N/A | ACME protocol preferred |
| Signing keys rotated per policy (2-3 years max, CA root: 10-20 years) | [ ] Yes [ ] No [ ] N/A | Document CA root key age |
| API keys rotated quarterly (90 days) minimum | [ ] Yes [ ] No [ ] N/A | Check API key age |
| Rotation automation for <100-day certificate validity | [ ] Yes [ ] No [ ] N/A | REQUIRED by policy |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**
- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Enhanced monitoring during manual rotation
  - [ ] Rotation calendar with advance alerts
  - [ ] Automation implementation in progress (target date: ________)
  - [ ] Other: _______________________________

**Remediation Plan:**
- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

## 4. Key Backup & Recovery

**Policy Requirement:** Keys MUST be backed up after generation, before deployment, and after rotation. Key escrow MUST use dual-control (2 persons) or split-knowledge (M-of-N). Recovery testing MUST be performed annually minimum. Backed-up keys MUST be encrypted with separate key (not self-encrypted) (Policy Section 3.4)

**Assessment Question:**

**Does your organization back up cryptographic keys and test recovery procedures?**
- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 5
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Key Type / Purpose | Backup Frequency | Backup Location | Backup Encryption | Recovery Testing | Status | Evidence Location | Gap Description | Remediation Needed |
|-------------------|------------------|-----------------|-------------------|------------------| ---------|-------------------|-----------------|-------------------|
| Example: CA Root Key, Database Master Key, TLS Keys, Encryption Keys | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Key Backup & Recovery-Specific Additional Columns:**

| Column | Header | Width | Validation Options |
|--------|--------|-------|--------------------|
| Q | Backup Method | 22 | HSM backup, Key escrow, Offline storage, Cloud backup, None, N/A |
| R | Dual-Control / Split-Knowledge | 20 | Dual-control (2 persons), M-of-N split, Single-person (non-compliant), N/A |
| S | Last Recovery Test Date | 18 | Date (DD.MM.YYYY) |
| T | Recovery Test Result | 18 | Successful, Failed, Not tested, N/A |

**Additional Details:**
- **Total keys backed up:** _________
- **Keys without backup:** _________ (HIGH RISK - data loss if key lost)
- **Last recovery test date:** _________
- **Recovery testing frequency:** [ ] Annually [ ] After DR exercises [ ] Never (non-compliant)

---

**KEY BACKUP & RECOVERY COMPLIANCE CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| Keys backed up after generation, before deployment, after rotation | [ ] Yes [ ] No [ ] N/A | Backup frequency documented |
| Key escrow uses dual-control (2 persons) or split-knowledge (M-of-N) | [ ] Yes [ ] No [ ] N/A | Prevents single-person recovery |
| Backed-up keys encrypted with separate key (KEK or HSM master key) | [ ] Yes [ ] No [ ] N/A | Not self-encrypted |
| Recovery testing performed annually minimum | [ ] Yes [ ] No [ ] N/A | Test results documented |
| Backup stored separately from production keys | [ ] Yes [ ] No [ ] N/A | Offline or separate cloud account |
| Recovery procedures documented and accessible | [ ] Yes [ ] No [ ] N/A | DR runbooks, step-by-step |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**
- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Keys regenerable from source (ephemeral keys)
  - [ ] Redundant key generation capability
  - [ ] Recovery testing scheduled (target date: ________)
  - [ ] Other: _______________________________

**Remediation Plan:**
- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

## 5. Certificate Management

**Policy Requirement:** Certificate expiration monitoring MUST provide 90-day advance alerts (60-day for critical systems). CRL/OCSP revocation checking REQUIRED and tested. Certificate lifecycle automation REQUIRED for validity <100 days (ACME protocol). Complete certificate inventory maintained and reviewed quarterly (Policy Section 3.5)

**Assessment Question:**

**Does your organization manage TLS/SSL certificates and other PKI certificates?**
- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 6
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Certificate Purpose | Certificate Authority | Validity Period | Expiration Date | Monitoring Status | Status | Evidence Location | Gap Description | Remediation Needed |
|--------------------|-----------------------|-----------------|-----------------|-------------------| ---------|-------------------|-----------------|-------------------|
| Example: Web server TLS, VPN certificates, Code signing, Email signing (S/MIME) | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Certificate Management-Specific Additional Columns:**

| Column | Header | Width | Validation Options |
|--------|--------|-------|--------------------|
| Q | Certificate Authority Type | 22 | Public CA (Let's Encrypt), Public CA (Commercial), Internal CA, Self-signed, N/A |
| R | Lifecycle Automation | 20 | ACME (Let's Encrypt), Automated script, Manual, N/A |
| S | Expiration Alert Threshold | 18 | 90 days, 60 days, 30 days, None (non-compliant) |
| T | CRL/OCSP Configured | 18 | Yes (tested), Yes (not tested), No |
| U | Next Renewal Date | 16 | Date (DD.MM.YYYY) |

**Additional Details:**
- **Total certificates managed:** _________
- **Certificates expiring within 90 days:** _________ (URGENT if >0)
- **Certificate automation status:** [ ] Fully automated (ACME) [ ] Partially automated [ ] Manual
- **CRL/OCSP testing date:** _________

---

**CERTIFICATE MANAGEMENT COMPLIANCE CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| Certificate expiration monitoring: 90-day advance alerts (60-day for critical) | [ ] Yes [ ] No [ ] N/A | Automated alerts configured |
| Certificate inventory complete and reviewed quarterly | [ ] Yes [ ] No [ ] N/A | All certificates documented |
| CRL/OCSP revocation checking REQUIRED and tested | [ ] Yes [ ] No [ ] N/A | Test with revoked certificate |
| Certificate validity aligns with CA/B Forum SC-081v3 timeline | [ ] Yes [ ] No [ ] N/A | ≤398d until 15.03.2026, progressive reduction |
| Certificate lifecycle automation for <100-day validity | [ ] Yes [ ] No [ ] N/A | ACME protocol or equivalent |
| No certificates expiring within 90 days without renewal plan | [ ] Yes [ ] No [ ] N/A | Check expiration report |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**
- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Manual monitoring with calendar reminders
  - [ ] Automation implementation in progress (target: ________)
  - [ ] Certificates renewed proactively (>90 days in advance)
  - [ ] Other: _______________________________

**Remediation Plan:**
- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

## 6. Overall Key Management Summary

### 6.1 Compliance Summary

**Total Assessment Areas:** _______

| Key Management Category | Status | Percentage |
|------------------------|--------|------------|
| Key Generation | | |
| Key Storage | | |
| Key Rotation | | |
| Key Backup & Recovery | | |
| Certificate Management | | |
| **Overall** | | |

**Instructions for Completion:**
- Count the number of each status (✅ / ⚠️ / ❌) per category
- Calculate percentage: (Compliant Count / Total Items) × 100
- Exclude N/A items from total when calculating compliance percentage
- Target: ≥90% Compliant for mature ISMS

### 6.2 Critical Gaps Identified

List the most critical gaps that require immediate attention:

1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________

**Guidance:**
- Critical gaps typically include:
  - ❌ Weak key generation (weak entropy, RSA 1024-bit)
  - ❌ Plaintext keys in config files or code repositories
  - ❌ CA signing keys not in HSM
  - ❌ Keys never rotated (>3 years old)
  - ❌ No key backup or untested recovery
  - ❌ Certificates expiring within 90 days
  - ❌ No certificate automation with <100-day validity approaching
  - ❌ CRL/OCSP not configured or not tested

### 6.3 Top Remediation Priorities

| Priority | Gap Description | Target Date | Responsible Person |
|----------|-----------------|-------------|-------------------|
| **High** | | | |
| **High** | | | |
| **Medium** | | | |

**Priority Definitions:**
- **High:** Key compromise risk, data loss risk, compliance violation, or operational failure imminent
- **Medium:** Compliance gap with planned remediation, low immediate risk
- **Low:** Best practice improvement, no compliance impact

---

## 7. Evidence Register

**List all evidence files/documents referenced in this assessment:**

| Evidence ID | Description | Location | Date Collected |
|-------------|-------------|----------|----------------|
| EV-1-001 | Entropy source verification | /evidence/a824_4/ | DD.MM.YYYY |
| EV-2-001 | HSM key inventory | /evidence/a824_4/ | DD.MM.YYYY |
| | | | |
| | | | |

**Evidence Naming Convention:**
```
EV-[Section]-[System]-[Date]-[Type].[ext]
```

**Examples:**
- `EV-1-Entropy-Source-20260115.txt`
- `EV-2-HSM-Key-Inventory-20260115.pdf`
- `EV-3-Certificate-Rotation-Schedule-20260115.xlsx`
- `EV-4-Key-Recovery-Test-20260115.pdf`
- `EV-5-Certificate-Expiration-Report-20260115.xlsx`

**Evidence Types:**
- Entropy source verification
- Hardware RNG status
- Key generation logs (SANITIZED)
- Key storage inventories
- Key rotation schedules
- Key backup procedures
- Recovery test results
- Certificate inventory
- Certificate expiration monitoring
- ACME protocol setup
- CRL/OCSP tests

**Evidence Storage:**
- **Location:** [Organization's evidence repository path]
- **Retention:** Audit cycle + 1 year minimum
- **Access Control:** Restricted to security team and auditors
- **Sensitivity:** CRITICAL - NO PRIVATE KEYS IN EVIDENCE

---

## 8. Approval and Sign-Off

### 8.1 Assessment Summary

**Assessment Document:** ISMS-IMP-A.8.24.4 - Key Management Assessment  
**Assessment Period:** From __________ To __________  
**Overall Compliance Rate:** _______ % (from Summary Dashboard Section 6.1)  
**Assessment Status:** [ ] Draft [ ] Final [ ] Requires remediation [ ] Re-assessment required

**Key Findings:**
- Key management controls assessed: _______
- Compliant controls: _______
- Controls requiring remediation: _______
- Critical gaps identified: _______
- High-priority remediation items: _______

---

### 8.2 Assessment Completed By

**Name:** _______________________  
**Role:** _______________________  
**Department:** _______________________  
**Email:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Certification:**
I certify that this assessment was completed with due diligence, all key management information is accurate to the best of my knowledge, entropy sources have been verified (not assumed), NO private keys are included in evidence, and all evidence has been collected and sanitized.

---

### 8.3 Reviewed By (Information Security Officer)

**Name:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Review Comments:**
_________________________________________________________________

**Review Outcome:**
- [ ] Approved - Assessment complete and accurate
- [ ] Approved with minor corrections - Specific items to address: _______
- [ ] Requires revision - Significant issues identified, re-submit required

---

### 8.4 Approved By (CISO)

**Name:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Approval Decision:**
- [ ] Approved - Key management posture acceptable, remediation plans approved
- [ ] Approved with conditions - Remediation must be completed by: _______
- [ ] Rejected - Re-assessment required due to: _______

**Risk Acceptance:**
For any documented exceptions/deviations, I accept the residual risk based on:
- Documented risk assessment
- Approved compensating controls
- Business justification
- Compliance with exception approval process (ISMS-POL-A.8.24-S5.B)

---

### 8.5 Next Review Date

**Next Scheduled Assessment:** _______________________

**Review Cycle:** Quarterly (every 3 months) or upon:
- Key compromise or suspected compromise
- HSM failure or major maintenance
- Certificate expiration incident
- Discovery of plaintext keys
- CA/Browser Forum ballot changes
- Failed audit findings on key management
- Major infrastructure changes

**Interim Monitoring:**
- Certificate expiration: Continuous (90-day alerts)
- Key rotation schedule: Monthly reviews
- HSM audit logs: Quarterly
- Entropy source health: Quarterly
- Key backup testing: Annually
- Remediation progress: Monthly

---

### 8.6 Distribution List

This assessment shall be distributed to:
- [ ] Chief Information Security Officer (CISO)
- [ ] Information Security Officer (ISO)
- [ ] PKI Administrators
- [ ] HSM Administrators
- [ ] Cloud Security team
- [ ] Security Operations team
- [ ] Compliance team
- [ ] Internal Audit
- [ ] IT Management
- [ ] Other: _______________________

**Storage Location:**
- **ISMS Repository:** `ISMS/Controls/A.8.24_Use_of_Cryptography/Assessments/`
- **Filename:** `ISMS-IMP-A.8.24.4_Key_Management_[DATE]_APPROVED.xlsx`

---

## APPENDIX: Technical Notes for Workbook Developers

### A.1 Excel Workbook Structure

**Sheet Names (9 sheets total):**
1. Instructions & Legend
2. 1. Key Generation
3. 2. Key Storage
4. 3. Key Rotation
5. 4. Key Backup & Recovery
6. 5. Certificate Management
7. Summary Dashboard
8. Evidence Register
9. Approval Sign-Off

### A.2 Data Validation Rules

**Status Dropdown:**
- Formula: `"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"`
- Applied to: Column G (Status) in all assessment sheets

**Generation Method Dropdown:**
- Formula: `"HSM,AWS KMS,Azure Key Vault,GCP KMS,OpenSSL,Let's Encrypt ACME,Manual,N/A"`

**Algorithm Dropdown:**
- Formula: `"RSA-2048,RSA-3072,RSA-4096,ECDSA P-256,ECDSA P-384,AES-256,AES-128,N/A"`

**Storage Location Dropdown:**
- Formula: `"HSM,AWS KMS,Azure Key Vault,GCP KMS,Software Keystore,Config File,N/A"`

**Storage Security Level Dropdown:**
- Formula: `"HSM (FIPS 140-2 L2+),Cloud KMS,Software Keystore,Plaintext (Non-compliant),N/A"`

### A.3 Conditional Formatting

**Status Column:** Green/Yellow/Red traffic light system
**Storage Security Level:** Red alert for "Plaintext (Non-compliant)"
**Entropy Source:** Green for hardware RNG, yellow for /dev/urandom
**Certificate Validity:** Green for ≤398d, red for >398d

### A.4 Cell Protection

**Protected:** Formulas, headers, checklists
**Unprotected:** Data entry cells (yellow fill), dates, dropdowns

### A.5 Summary Dashboard Formulas

**Compliance Percentage:**
```excel
=COUNTIF('1. Key Generation'!G:G,"✅ Compliant")/COUNTA('1. Key Generation'!G:G)*100
```

**Critical Gaps:**
```excel
=COUNTIF('2. Key Storage'!F:F,"Plaintext (Non-compliant)")
```

**Certificates Expiring Within 90 Days:**
```excel
=COUNTIF('5. Certificate Management'!U:U,"<="&TODAY()+90)
```

### A.6 Evidence Register Auto-Numbering

```excel
="EV-"&TEXT(ROW()-4,"000")
```

### A.7 Python Script Integration Points

**Script:** `generate_a824_4_key_management_assessment.py`

**Key Functions:**
- `create_workbook()`, `setup_styles()`, `get_key_management_columns()`
- `create_key_generation_sheet()` (columns Q-S)
- `create_key_storage_sheet()` (columns Q-S)
- `create_key_rotation_sheet()` (columns Q-T)
- `create_key_backup_sheet()` (columns Q-T)
- `create_certificate_mgmt_sheet()` (columns Q-U)

**QA Script:** `excel_sanity_check_a824_4.py`

### A.8 Version Control

- Filename: `ISMS-IMP-A.8.24.4_Key_Management_YYYYMMDD.xlsx`
- v2.0: Added User Guide, entropy guidance, SC-081v3 timeline

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

**Quality Checks Before Finalizing:**
- [ ] All merge instructions removed
- [ ] Document Control version shows 2.0
- [ ] Dates in DD.MM.YYYY format
- [ ] Cross-references accurate
- [ ] Entropy source guidance clear (hardware RNG or /dev/random)
- [ ] Certificate automation deadline (15.03.2026) prominent
- [ ] NO PRIVATE KEYS IN EVIDENCE (repeated throughout)

---

**End of Technical Specification**