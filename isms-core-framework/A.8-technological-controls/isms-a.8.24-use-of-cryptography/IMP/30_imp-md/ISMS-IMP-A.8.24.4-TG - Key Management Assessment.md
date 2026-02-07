**ISMS-IMP-A.8.24.4-TG - Key Management Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography

----

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.24.4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Key Management Cryptographic Controls |
| **Related Policy** | ISMS-POL-A.8.24, Section 3.5 (Key Management Requirements) |
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

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

# Instructions for Completing This Assessment

## How to Use This Document

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

## Status Legend

| Symbol | Meaning | Description |
|--------|---------|-------------|
| **✅** | **Compliant** | Fully meets policy requirements, no gaps identified |
| **⚠️** | **Partial** | Some requirements met, minor gaps exist, remediation planned |
| **❌** | **Non-Compliant** | Does not meet policy requirements, significant gaps |
| **N/A** | **Not Applicable** | This requirement does not apply to your environment |

## Evidence Types

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

# Common Column Structure (All Assessment Sheets)

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

# Key Generation

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

# Key Storage

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

# Key Rotation

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

# Key Backup & Recovery

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

# Certificate Management

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

# Overall Key Management Summary

## Compliance Summary

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

## Critical Gaps Identified

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

## Top Remediation Priorities

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

# Evidence Register

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

# Approval and Sign-Off

## Assessment Summary

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

## Assessment Completed By

**Name:** _______________________  
**Role:** _______________________  
**Department:** _______________________  
**Email:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Certification:**
I certify that this assessment was completed with due diligence, all key management information is accurate to the best of my knowledge, entropy sources have been verified (not assumed), NO private keys are included in evidence, and all evidence has been collected and sanitized.

---

## Reviewed By (Information Security Officer)

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

## Approved By (CISO)

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

## Next Review Date

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

## Distribution List

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

# APPENDIX: Technical Notes for Workbook Developers

## A.1 Excel Workbook Structure

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

## A.2 Data Validation Rules

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

## A.3 Conditional Formatting

**Status Column:** Green/Yellow/Red traffic light system
**Storage Security Level:** Red alert for "Plaintext (Non-compliant)"
**Entropy Source:** Green for hardware RNG, yellow for /dev/urandom
**Certificate Validity:** Green for ≤398d, red for >398d

## A.4 Cell Protection

**Protected:** Formulas, headers, checklists
**Unprotected:** Data entry cells (yellow fill), dates, dropdowns

## A.5 Summary Dashboard Formulas

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

## A.6 Evidence Register Auto-Numbering

```excel
="EV-"&TEXT(ROW()-4,"000")
```

## A.7 Python Script Integration Points

**Script:** `generate_a824_4_key_management_assessment.py`

**Key Functions:**

- `create_workbook()`, `setup_styles()`, `get_key_management_columns()`
- `create_key_generation_sheet()` (columns Q-S)
- `create_key_storage_sheet()` (columns Q-S)
- `create_key_rotation_sheet()` (columns Q-T)
- `create_key_backup_sheet()` (columns Q-T)
- `create_certificate_mgmt_sheet()` (columns Q-U)

**QA Script:** `excel_sanity_check_a824_4.py`

## A.8 Version Control

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

**END OF SPECIFICATION**

---

*"The zeros of the Riemann zeta function and the prime numbers are the two most important objects in mathematics."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
