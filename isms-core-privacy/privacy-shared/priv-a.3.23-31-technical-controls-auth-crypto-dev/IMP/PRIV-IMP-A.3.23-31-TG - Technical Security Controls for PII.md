<!-- ISMS-CORE:IMP:PRIV-IMP-A.3.23-31-TG:privacy:TG:a.3.23-31 -->
**PRIV-IMP-A.3.23-31-TG — Technical Security Controls for PII — Technical Guide**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Technical Security Controls for PII — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | PRIV-IMP-A.3.23-31-TG |
| **Related Policy** | PRIV-POL-A.3.23-31 (Technical Security Controls for PII) |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / DPO | Initial technical guide for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant technical change)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- PRIV-POL-A.3.23-31 (Technical Security Controls for PII — the governing policy)
- PRIV-IMP-A.3.23-31-UG (Technical Security Controls for PII — User Guide)
- ISMS-POL-A.8.24 (Use of Cryptography — master cryptographic standards)
- ISMS-POL-A.8.15-16 (Logging and Monitoring — master logging framework)

---

## Purpose of This Guide

This guide provides the **technical specifications, approved configurations, register schemas, and templates** for PII technical security controls. It covers:

- PII System Inventory schema
- PII System Authentication Register schema
- Approved MFA technologies and authentication thresholds
- Approved cryptographic algorithms and TLS standards
- Key rotation schedule
- PII logging event specification
- PII Application Security Requirements template
- Backup compliance review template
- Test data generation reference

**Audience**: CISO, IT Security Team, Development/DevOps Teams, IT Architecture.

---

## 1. PII System Inventory

The PII System Inventory is the authoritative register of all systems within PIMS scope (those that store, process, or provide access to PII). Maintained by IT Security Team with DPO oversight.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| System ID | Text | Unique identifier (e.g., SYS-001) |
| System Name | Text | Official system name |
| System Type | Enum | Database / Application / API / Infrastructure / Cloud Service / Other |
| PII Classification | Enum | RESTRICTED / CONFIDENTIAL / INTERNAL |
| PII Categories Processed | Multi-select | Ordinary / Financial / Special Category / Sensitive |
| Data Owner | Text | Accountable role/person for this system's PII |
| System Owner (Technical) | Text | IT owner responsible for system configuration |
| Hosting | Enum | On-premises / Cloud (IaaS) / SaaS / Hybrid |
| Cloud Provider | Text | If cloud: provider name and region |
| Authentication Standard Applied | Enum | MFA All Access / MFA Remote + Password Internal / Password Only |
| MFA Technology | Text | Specific MFA implementation (see approved list) |
| Encryption at Rest | Enum | Enabled / Not Enabled / Not Applicable |
| Encryption Algorithm | Text | e.g., AES-256-GCM |
| Encryption in Transit | Enum | TLS 1.3 / TLS 1.2 / Not Enabled |
| Logging Configured | Enum | Full (all required events) / Partial / Not Configured |
| Log Destination | Text | SIEM or log storage location |
| Backup Covered | Boolean | Yes / No |
| Backup Encryption | Enum | Enabled / Not Enabled |
| Last Security Review | Date | Date of last security configuration review |
| In PCAS Scope | Boolean | Yes / No |
| Notes | Text | Open actions, exceptions, audit flags |

---

## 2. PII System Authentication Register

Supplementary to the PII System Inventory — records the specific authentication configuration for each PII system.

### Schema

| Field | Type | Description |
|-------|------|-------------|
| System ID | Text | Reference to PII System Inventory |
| Access Type | Enum | Internal (on-premises) / Remote (VPN) / Internet-facing / Privileged |
| Authentication Method | Text | Password + MFA / Password only / Certificate / Biometric + PIN |
| MFA Technology Used | Text | e.g., Microsoft Authenticator TOTP, hardware FIDO2 key |
| Password Policy Applied | Text | Minimum length, complexity, history settings |
| Lockout Threshold | Number | Number of failed attempts before lockout |
| Lockout Duration | Text | Duration of lockout (e.g., 15 minutes / until admin unlock) |
| Session Timeout | Text | Session expiry for idle sessions |
| Shared Credentials | Boolean | No (prohibited) / Yes — Exception Reference: [ref] |
| Configuration Last Verified | Date | Date IT Security Team last verified the configuration is active |
| Verified By | Text | IT Security Team member |
| Notes | Text | Exceptions, compensating controls |

---

## 3. Approved Authentication Technologies and Thresholds

### Approved MFA Technologies for PII Systems

| Technology | Type | Acceptable Use |
|-----------|------|----------------|
| Hardware FIDO2 / WebAuthn (YubiKey, etc.) | Hardware token | Preferred; all PII access types |
| Authenticator app — TOTP (Microsoft Authenticator, Google Authenticator) | Software token | Acceptable for all PII access types |
| Push notification (Microsoft Authenticator, Duo) | Software push | Acceptable; requires training on push-phishing awareness |
| SMS one-time code | Software / telco | Acceptable for CONFIDENTIAL PII only; not for RESTRICTED PII |
| Email one-time code | Software / email | Not acceptable for PII system MFA (same channel as primary credential) |

### Authentication Failure Thresholds

| Threshold | Value |
|-----------|-------|
| Failed attempts before lockout | 5 consecutive failures |
| Lockout duration | 15 minutes (automatic unlock); or admin unlock for RESTRICTED PII systems |
| Alert to IT Security Team | On 3+ failures within 5 minutes (potential brute force) |
| Session idle timeout | 15 minutes (CONFIDENTIAL PII systems); 10 minutes (RESTRICTED PII systems) |

---

## 4. Approved Cryptographic Standards for PII

### Encryption Algorithms

| Use Case | Approved Algorithm | Minimum Key Size | Notes |
|----------|--------------------|-----------------|-------|
| Data at rest (databases, files) | AES-GCM | 256-bit | AES-256-GCM preferred |
| Data at rest (full-disk encryption) | AES-XTS | 256-bit | BitLocker / FileVault 2 |
| Data in transit | TLS 1.3 | N/A (protocol-defined) | Preferred |
| Data in transit (minimum) | TLS 1.2 | N/A | TLS 1.0 and 1.1 prohibited |
| Asymmetric (key exchange, signatures) | RSA | 2048-bit minimum; 4096-bit preferred | Or ECDSA P-256 / P-384 |
| Hashing (integrity, token generation) | SHA-256 or SHA-3 | — | MD5 and SHA-1 prohibited |
| Key derivation | PBKDF2 / bcrypt / Argon2 | — | For password-derived keys |

### Prohibited Algorithms (for PII processing systems)

The following algorithms are explicitly prohibited for PII protection: DES, 3DES, RC4, MD5, SHA-1, TLS 1.0, TLS 1.1, export-grade ciphers.

### TLS Cipher Suites (PII APIs and Web Interfaces)

Permitted cipher suites for PII-processing endpoints:
- TLS_AES_256_GCM_SHA384 (TLS 1.3)
- TLS_CHACHA20_POLY1305_SHA256 (TLS 1.3)
- TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (TLS 1.2)
- TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (TLS 1.2)

### Key Rotation Schedule

| Key Type | Maximum Rotation Period | Trigger for Immediate Rotation |
|----------|------------------------|-------------------------------|
| Data-at-rest encryption keys (PII databases) | 24 months | Suspected key compromise; personnel departure with key access |
| TLS certificates (external-facing PII endpoints) | 12 months | Certificate compromise; CA revocation |
| Backup encryption keys | 24 months | Suspected compromise |
| API signing keys | 12 months | Key exposure in code or logs |
| Master key / KEK | 36 months | Suspected compromise only |

---

## 5. PII Logging Event Specification

The following events must be captured in logs for all PII-processing systems. Log format: structured JSON (preferred) or syslog CEF. Timestamps: ISO 8601 with timezone.

| Event Category | Minimum Fields to Log |
|---------------|----------------------|
| **PII Data Store Read** | Timestamp, Identity ID, System ID, Data store/table, Query type, Records affected (count), Source IP |
| **PII Data Store Write/Update** | Timestamp, Identity ID, System ID, Data store/table, Fields modified, Records affected, Source IP |
| **Bulk PII Export** | Timestamp, Identity ID, System ID, Export destination, Format, Record count, Approval reference |
| **PII Deletion / Erasure** | Timestamp, Identity ID, System ID, Records deleted, Deletion method, Approval reference |
| **Failed Authentication** | Timestamp, Identity attempted, System ID, Source IP, Failure reason |
| **Access Rights Change** | Timestamp, Admin Identity ID, Target Identity ID, System ID, Change type (grant/revoke/modify), Approval reference |
| **Privileged Session** | Session ID, Timestamp start/end, Identity ID, System ID, Commands/queries (summary), Data volume accessed |
| **Data Subject Rights Fulfilment** | Timestamp, Right type (access/erasure/restriction/portability), Request reference, Identity processing request, Data subjects affected, Outcome |
| **System/Application Error** | Timestamp, System ID, Error type, Component, Error code, Severity, Data affected (if applicable) |

**Log retention**: Minimum 12 months hot (immediately accessible); cold archive for minimum 36 months for RESTRICTED PII system logs.

---

## 6. PII Application Security Requirements Template

Complete this template for any application that processes PII — before development commences or before procurement decision.

```
PII APPLICATION SECURITY REQUIREMENTS

Application Name: _____________________________________________
Application Type: [ ] Internal development  [ ] Acquired (vendor: _______)
PII Processing Scope: _____________________________________________
PII Classification: [ ] RESTRICTED  [ ] CONFIDENTIAL  [ ] INTERNAL
Date: _____________________________________________

SECTION 1 — AUTHENTICATION
Requirement 1.1: Authentication method for PII access:
  Required: [ ] MFA all access  [ ] MFA remote + password internal  [ ] Password only
  Specific technology: _____________________________________________
Requirement 1.2: Account lockout after [5] failed attempts

SECTION 2 — ACCESS CONTROL
Requirement 2.1: Role-based access control (RBAC) aligned to defined access roles
Requirement 2.2: Least privilege — each role accesses only required PII fields
Requirement 2.3: Separation of duties for privileged operations on PII

SECTION 3 — ENCRYPTION
Requirement 3.1: Encryption at rest — algorithm: AES-256 (minimum)
Requirement 3.2: Encryption in transit — protocol: TLS 1.2 minimum; TLS 1.3 preferred
Requirement 3.3: Key management — keys stored separately from PII; rotation schedule defined

SECTION 4 — LOGGING
Requirement 4.1: All required PII events logged per PRIV-IMP-A.3.23-31-TG event specification
Requirement 4.2: Logs forwarded to SIEM / central log store within [X] minutes
Requirement 4.3: No PII values in log fields (log record IDs, not PII content)

SECTION 5 — RETENTION AND DELETION
Requirement 5.1: Data retention periods defined and enforced per PRIV-POL-A.1.4.6-10
Requirement 5.2: Automated deletion at end of retention period (or manual process with evidence)
Requirement 5.3: Data subject erasure (Art. 17) triggerable from the application within [X] business days

SECTION 6 — PRIVACY BY DESIGN
Requirement 6.1: Data minimisation — only required PII fields collected; excess fields removed before finalisation
Requirement 6.2: Privacy-by-default settings defined and documented
Requirement 6.3: DPIA trigger assessed: [ ] DPIA not required (rationale: _____)
                                         [ ] DPIA required and completed (DPIA reference: _____)

DPO APPROVAL: _________________________ Date: _____________
CISO APPROVAL: _________________________ Date: _____________
```

---

## 7. Annual PII Backup Compliance Review Template

```
PII BACKUP COMPLIANCE REVIEW

Review Period: [Year]
Date of Review: [Date]
Conducted By (IT Security Team): [Name]
DPO Confirmed: [Name / Date]

1. PII SYSTEM BACKUP COVERAGE
(List all systems from PII System Inventory and confirm backup status)

| System ID | System Name | PII Classification | Backup Coverage | Backup Encryption | Gap |
|-----------|-------------|-------------------|----------------|-------------------|-----|
| | | | Yes / No | Yes / No | |

Total systems with PII: [N]
Systems covered by backup: [N]
Coverage gap: [ ] None  [ ] Yes — systems: [list]

2. RESTORATION TEST
Test Date: [Date]
System Tested: [System ID + Name]
Backup Restored: [Yes / No]
Data Integrity Verified: [Yes / No — method: ___________]
Restoration Time: [Minutes]
Outcome: [ ] Pass  [ ] Fail — details: ___________

3. KEY MANAGEMENT FOR BACKUP ENCRYPTION
Decryption keys accessible and tested: [ ] Yes  [ ] No — see actions
Last key rotation: [Date]

4. OVERALL OUTCOME
[ ] Pass — all PII systems covered; backup tested and restorable
[ ] Partial — gaps identified (see above); remediation actions below
[ ] Fail — escalate to CISO and DPO immediately

Actions Required:
[List gaps and remediation owners/target dates]

IT Security Team Sign-off: _________________________ Date: _____________
CISO Sign-off: _________________________ Date: _____________
DPO Awareness: _________________________ Date: _____________
```

---

<!-- QA_VERIFIED: [Date] -->
