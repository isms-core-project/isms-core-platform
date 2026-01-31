# Control A.8.24: Use of Cryptography
## POLICY REQUIREMENTS - SECTION 2.3
## Cryptographic Controls for Data Storage

---

**Document ID**: ISMS-POL-A.8.24-S2.3  
**Title**: Use of Cryptography - Data Storage  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Data Security Manager | Initial data-at-rest encryption requirements |

**Review Cycle**: Annual (or upon regulatory changes/breach incidents)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Data Security Manager / Database Administrator Lead
- Secondary: Chief Technology Officer (CTO) or IT Director
- Compliance: Legal/Compliance Officer (for data residency/protection laws)
- Risk: Risk Management Officer (for data classification impact)

**Distribution**: Database Administrators, System Administrators, Storage Teams, Development Teams, Data Protection Officers  
**Related Standards**: ISO/IEC 27001:2022 Control A.8.24, NIST SP 800-111 (Storage), BSI TR-02102-1, nFADP Art. 8, GDPR Art. 32, PCI DSS Req. 3 (if applicable)

---

## 2.3 Cryptographic Controls for Data Storage

### Purpose
This section defines mandatory cryptographic requirements for protecting data at rest across all storage media, devices, and systems.

---

### 2.3.1 Mobile Devices

#### Scope
Mobile devices include: smartphones, tablets, laptops used in mobile context, and other portable computing devices containing organizational data.

#### Full Disk Encryption Requirements

**Mandatory Encryption:**
- All mobile devices with access to organizational data MUST implement full disk encryption (FDE)
- Encryption MUST be enabled before device is provisioned for organizational use
- Devices without encryption capability MUST NOT be approved for organizational data access

**Platform-Specific Requirements:**

**iOS Devices:**
- FileVault MUST be enabled (macOS)
- Native iOS encryption enabled by default (passcode required)
- Minimum passcode: 6 digits (alphanumeric preferred)
- Biometric authentication (Touch ID/Face ID) acceptable with strong passcode backup

**Android Devices:**
- Full device encryption MUST be enabled
- Minimum PIN/password: 6 characters
- Biometric authentication acceptable with strong PIN/password backup
- Encryption status MUST be verified via MDM

**Windows Mobile Devices:**
- BitLocker MUST be enabled
- TPM (Trusted Platform Module) REQUIRED where available
- PIN or password authentication REQUIRED

#### Mobile Device Management (MDM)

**Requirements:**
- MDM solution MUST verify encryption status
- MDM MUST enforce encryption policy
- Non-compliant devices MUST be blocked from organizational resources
- Encryption status reporting REQUIRED (quarterly minimum)

#### Key Management for Mobile Devices

**Requirements:**
- Encryption keys MUST be tied to user authentication (passcode/password)
- Recovery keys MUST be escrowed to organizational MDM system
- Lost device recovery procedures MUST be documented
- Remote wipe capability REQUIRED for lost/stolen devices

**Key Recovery:**
- IT department MUST have ability to recover encryption keys for business-owned devices
- Recovery process MUST be documented and tested
- Recovery key access MUST be logged and audited
- Personal devices (BYOD) MAY use user-controlled encryption keys

---

### 2.3.2 Laptops and Workstations

#### Full Disk Encryption Requirements

**Mandatory Encryption:**
- All laptops and workstations containing sensitive data (Confidential or Restricted) MUST implement full disk encryption
- Desktop workstations in secure facilities MAY be exempted with documented risk assessment and CISO approval
- Encryption MUST be enabled before device deployment

#### Platform-Specific Implementation

**Windows Devices:**
- **BitLocker** REQUIRED
- TPM 2.0 REQUIRED (TPM 1.2 minimum for legacy hardware)
- Encryption algorithm: AES-256-XTS
- BitLocker startup authentication: TPM + PIN (RECOMMENDED) or TPM-only (acceptable)
- BitLocker recovery key MUST be escrowed to Active Directory or Azure AD

**macOS Devices:**
- **FileVault** REQUIRED
- Encryption algorithm: AES-256-XTS
- FileVault recovery key MUST be escrowed to organizational key management system
- Institutional recovery key RECOMMENDED for corporate-owned devices

**Linux Devices:**
- **LUKS** (Linux Unified Key Setup) REQUIRED
- Encryption algorithm: AES-256-XTS or AES-256-CBC-ESSIV
- Encryption MUST be configured during OS installation
- Recovery key/passphrase MUST be documented and stored securely

#### Key Escrow and Recovery

**Requirements:**
- Recovery keys for business-owned devices MUST be escrowed centrally
- Escrow system MUST be separate from encrypted device
- Recovery key access MUST require authorization and be logged
- Recovery procedures MUST be tested annually
- Employee termination process MUST include recovery key verification

**Acceptable Escrow Solutions:**
- Active Directory BitLocker Recovery
- Azure AD BitLocker Recovery
- Enterprise key management system
- Secure password vault with access controls

#### Pre-Boot Authentication

**Requirements:**
- Pre-boot authentication RECOMMENDED for high-security environments
- Pre-boot PIN/password SHOULD be different from Windows/macOS login
- Smart card or hardware token authentication ACCEPTABLE
- Biometric pre-boot authentication NOT RECOMMENDED (availability concerns)

---

### 2.3.3 Servers

#### Encryption Requirements by Environment

**Physical Servers:**
- Physical servers containing sensitive data MUST implement encryption:
  - **Full disk encryption (FDE)**, OR
  - **Volume-level encryption**, OR
  - **Application-level encryption**
- Servers in physically secure data centers MAY use volume-level or application-level encryption
- Servers in less secure locations MUST use full disk encryption

**Virtual Machines:**
- Virtual machines MAY rely on hypervisor-level encryption if:
  - Hypervisor provides AES-256 or equivalent
  - Encryption keys are managed separately from VMs
  - VM administrator cannot access encryption keys
- Guest-level encryption RECOMMENDED for highly sensitive workloads
- VM disk encryption (VMDK encryption) ACCEPTABLE for VMware environments

**Containerized Workloads:**
- Container persistent volumes containing sensitive data MUST be encrypted
- Encryption at storage layer (CSI driver encryption) ACCEPTABLE
- Application-level encryption RECOMMENDED for defense in depth
- Container image encryption RECOMMENDED for proprietary applications

#### Key Management for Servers

**Requirements:**
- Encryption keys MUST be stored separately from encrypted data
- Keys MUST NOT reside on the same server/system being encrypted
- Hardware Security Module (HSM) REQUIRED for critical servers protecting:
  - Payment card data
  - Cryptographic keys
  - Authentication databases
  - >100,000 sensitive records

**Automated Key Management:**
- Enterprise key management system (KMS) RECOMMENDED
- Key rotation automation REQUIRED for database encryption keys
- Key versioning MUST be supported to enable rollback if needed

#### Boot Process Security

**Requirements:**
- Secure boot MUST be enabled where supported
- Boot authentication mechanism MUST be documented
- Automatic decryption on boot ACCEPTABLE if:
  - Server is in physically secure data center, AND
  - Network-based key server provides keys (keys not stored locally), AND
  - Boot process is logged and monitored

---

### 2.3.4 Databases

#### Database Encryption Requirements

**Mandatory Encryption:**
- Databases containing sensitive data (Confidential or Restricted) MUST implement encryption
- Encryption MUST use one of:
  - **Transparent Data Encryption (TDE)** - PREFERRED
  - **Column-level encryption** for specific sensitive fields - ACCEPTABLE
  - **Application-level encryption** before database storage - ACCEPTABLE

#### Transparent Data Encryption (TDE)

**Implementation Requirements:**
- TDE MUST encrypt all data files, log files, and backups
- Encryption algorithm: AES-256 minimum
- TDE master key MUST be stored in separate key management system
- TDE certificate/keys MUST be backed up separately from database backups

**Platform-Specific TDE:**

**Microsoft SQL Server:**
- TDE MUST be enabled for sensitive databases
- Master key MUST be protected by certificate in master database
- Certificate MUST be backed up separately
- Backup encryption MUST be verified

**Oracle Database:**
- TDE with AES-256 required
- Oracle Wallet or HSM for key storage
- Wallet auto-login NOT RECOMMENDED for production

**PostgreSQL:**
- pgcrypto extension or native encryption (PostgreSQL 15+)
- Key management via external KMS recommended
- pg_tde extension ACCEPTABLE for older versions

**MySQL/MariaDB:**
- InnoDB table encryption REQUIRED
- Key ring plugin for key management
- File-per-table tablespace encryption

#### Column-Level Encryption

**Use Cases:**
- Legacy databases without TDE support
- Specific highly sensitive fields (SSN, credit cards, health records)
- Fine-grained encryption control requirements

**Requirements:**
- Encryption MUST occur at application layer before database insert
- AES-256-GCM REQUIRED for column encryption
- Encryption keys MUST NOT be stored in database
- Key versioning REQUIRED to support key rotation without data re-encryption

#### Database Connection Encryption

**Requirements:**
- Database connections MUST use encrypted protocols:
  - PostgreSQL: SSL/TLS connections required
  - MySQL: SSL connections required
  - MSSQL: Encrypted connections required
  - MongoDB: TLS required
- Self-signed certificates ACCEPTABLE for internal databases
- Certificate validation SHOULD be enabled (prevent MITM attacks)

#### Key Management for Databases

**Requirements:**
- Database encryption keys MUST be stored in separate key management system
- Keys MUST NOT be stored in:
  - Database configuration files
  - Application code
  - Version control systems
- Hardware Security Module (HSM) REQUIRED for:
  - Production databases with >100,000 sensitive records
  - Databases containing payment card data (PCI DSS compliance)
  - Databases containing authentication credentials

**Key Rotation:**
- Database master encryption keys MUST rotate annually
- Key rotation process MUST NOT require downtime (online key rotation preferred)
- Old keys MUST be retained for decryption of historical backups
- Key rotation MUST be tested in non-production environment first

---

### 2.3.5 Cloud Storage

#### Cloud Storage Encryption

**Mandatory Requirements:**
- All sensitive data in cloud environments MUST be encrypted at rest
- Cloud provider default encryption ACCEPTABLE for Internal classification data
- Customer-managed encryption keys (CMEK) REQUIRED for Confidential/Restricted data

**Platform-Specific Requirements:**

**AWS (Amazon Web Services):**
- S3 bucket encryption REQUIRED (SSE-S3, SSE-KMS, or SSE-C)
- SSE-KMS (AWS KMS customer-managed keys) PREFERRED for sensitive data
- EBS volume encryption REQUIRED for EC2 instances with sensitive data
- RDS encryption at rest REQUIRED for databases with sensitive data

**Azure (Microsoft Azure):**
- Storage Service Encryption (SSE) REQUIRED for all storage accounts
- Azure Key Vault with customer-managed keys PREFERRED for sensitive data
- Disk encryption REQUIRED for virtual machines with sensitive data
- Transparent Data Encryption REQUIRED for Azure SQL Database

**GCP (Google Cloud Platform):**
- Default encryption at rest ACCEPTABLE for Internal data
- Cloud KMS with customer-managed encryption keys (CMEK) REQUIRED for sensitive data
- Persistent disk encryption REQUIRED
- Cloud SQL encryption REQUIRED for sensitive databases

#### Client-Side Encryption

**Requirements:**
- Client-side encryption (encryption before upload) REQUIRED for highly sensitive data in cloud storage
- Client-side encryption RECOMMENDED as defense-in-depth measure
- Client-side encryption keys MUST be managed separately from cloud provider

**Use Cases for Client-Side Encryption:**
- Restricted classification data
- Regulated data with strict control requirements (HIPAA, PCI DSS)
- Zero-trust cloud deployments
- Multi-cloud redundancy scenarios

#### Cloud Storage Key Management

**Requirements:**
- Customer-managed encryption keys (CMEK) PREFERRED over provider-managed keys
- Key rotation MUST be automated where possible
- Cloud provider key management service ACCEPTABLE if:
  - Customer controls key lifecycle
  - Cloud provider cannot access keys without customer authorization
  - Key access is logged and auditable

**Key Storage Options (in preference order):**
1. **On-premises HSM** (highest control, most complex)
2. **Cloud HSM service** (AWS CloudHSM, Azure Dedicated HSM, GCP Cloud HSM)
3. **Cloud KMS with CMEK** (AWS KMS, Azure Key Vault, GCP Cloud KMS)
4. **Provider-managed keys** (acceptable for Internal classification only)

---

### 2.3.6 Backup Storage

#### Backup Encryption Requirements

**Mandatory Encryption:**
- All backup media MUST be encrypted
- Encryption MUST occur before backup data leaves production environment
- Backup encryption keys MUST be stored separately from backup media

**Backup Types:**

**Full Backups:**
- Full encryption of backup archive REQUIRED
- AES-256 minimum encryption standard
- Backup software native encryption ACCEPTABLE if meeting standards

**Incremental/Differential Backups:**
- Same encryption requirements as full backups
- Consistent encryption across all backup types REQUIRED

**Database Backups:**
- Database dump/export files MUST be encrypted
- TDE-encrypted database backups automatically encrypted
- Non-TDE backups MUST use backup software encryption or manual encryption

#### Backup Media Encryption

**Disk-Based Backups:**
- Backup target volumes MUST be encrypted (full disk or volume encryption)
- Network-attached storage (NAS) used for backups MUST have encryption enabled
- Deduplication appliances MUST encrypt deduplicated data

**Tape Backups:**
- LTO-4 and higher: hardware encryption REQUIRED (AES-256)
- Legacy tape: software encryption REQUIRED if hardware encryption unavailable
- Tape encryption keys MUST be managed via key management system

**Cloud Backup Storage:**
- Cloud backup targets MUST use provider encryption or client-side encryption
- Customer-managed keys PREFERRED for cloud backups
- Backup in transit to cloud MUST use encrypted protocols (TLS 1.2+)

#### Backup Key Management

**Critical Requirements:**
- Backup encryption keys MUST be stored separately from backup media
- Keys MUST NOT be stored on backup server or media
- Key recovery process MUST be documented and tested
- Key escrow RECOMMENDED for long-term archive backups

**Key Storage Best Practices:**
- Primary key storage: Enterprise key management system or HSM
- Secondary key backup: Physically separate secure location
- Geographic distribution RECOMMENDED for disaster recovery
- M-of-N secret sharing for critical backup keys (e.g., 3-of-5 scheme)

#### Backup Recovery Testing

**Requirements:**
- Backup decryption and recovery MUST be tested quarterly
- Test MUST include key retrieval from escrow/backup system
- Recovery time objective (RTO) MUST be measured and documented
- Failed decryption tests MUST trigger incident response

**Offsite Backup Security:**
- Offsite backups MUST maintain encryption in transit and at rest
- Physical transport of backup media MUST use locked containers
- Chain of custody MUST be documented for physical media transport
- Cloud-based offsite backups MUST use encrypted transmission (TLS 1.2+)

---

### 2.3.7 Removable Media and Portable Storage

#### Encryption Requirements

**Mandatory Encryption:**
- All removable media containing organizational data MUST be encrypted
- Encryption MUST be enabled before data is written to media

**Removable Media Types:**
- USB flash drives
- External hard drives
- SD cards and other flash memory
- Optical media (CD, DVD, Blu-ray) for sensitive data

**Approved Encryption Methods:**
- BitLocker To Go (Windows)
- FileVault (macOS external drives)
- LUKS (Linux external drives)
- Hardware-encrypted USB drives (FIPS 140-2 compliant preferred)

#### Hardware-Encrypted Drives

**Requirements for High-Security Environments:**
- Hardware-encrypted USB drives REQUIRED for Restricted classification data
- FIPS 140-2 Level 2 or higher certification REQUIRED
- Self-destruct mechanisms for multiple failed authentication attempts RECOMMENDED
- Approved vendor list MUST be maintained

#### Removable Media Policy

**General Requirements:**
- Use of unapproved removable media PROHIBITED
- Removable media MUST be inventoried and tracked
- Data retention limits MUST be enforced on removable media
- Removable media MUST be securely erased/destroyed when no longer needed

---

### 2.3.8 Data Disposal and Secure Erasure

#### Cryptographic Erasure

**Preferred Method:**
- Cryptographic erasure (crypto-shredding) PREFERRED for encrypted storage
- Process: Securely destroy encryption keys to render data unrecoverable
- Applicable when: Data was encrypted with unique key that can be destroyed
- Verification: Confirm keys are destroyed and data cannot be decrypted

#### Physical Destruction

**Requirements for Physical Media:**
- Hard drives: Physical destruction (shredding, degaussing, incineration)
- SSDs: Physical destruction (shredding, incineration) - degaussing NOT effective
- Magnetic tape: Degaussing or physical shredding
- Optical media: Physical shredding or incineration

**Certification Requirements:**
- Certificate of destruction REQUIRED for media containing Confidential/Restricted data
- Destruction MUST be performed by approved vendor or in-house with documented procedures
- Destruction logs MUST be retained per organizational retention policy

#### Software-Based Secure Erasure

**Requirements:**
- Software erasure acceptable for non-critical or Internal classification data
- Minimum standard: DoD 5220.22-M (3-pass overwrite)
- SSD secure erase: Use ATA Secure Erase command (single pass acceptable due to wear leveling)
- Verification MUST be performed after software erasure

#### Data Disposal Documentation

**Requirements:**
- All data disposal activities MUST be documented
- Documentation MUST include: date, method, media identifier, responsible person
- Records MUST be retained per organizational retention policy
- Annual audit of disposal records REQUIRED

---

## Compliance Verification

**This section SHALL be verified through:**
- Quarterly endpoint encryption compliance reporting (via MDM/endpoint management)
- Annual server and database encryption audit
- Bi-annual backup recovery testing including encryption verification
- Annual review of cloud storage encryption configuration
- Data disposal audit trail review

---

## Related Documents

- **ISMS-POL-A.8.24-S1** - Section 1: Purpose, Scope, Definitions
- **ISMS-POL-A.8.24-S2.1** - Use of Cryptographic Controls
- **ISMS-POL-A.8.24-S2.2** - Data Transmission Requirements
- **ISMS-POL-A.8.24-S2.4** - Authentication Requirements
- **ISMS-POL-A.8.24-S2.5** - Compliance Requirements
- **ISMS-IMP-A.8.24** - Implementation & Compliance Status

---

**End of Section 2.3 - Cryptographic Controls for Data Storage**

*"Data at rest is data under attack. It just doesn't know it yet."*  
*— The Wisdom of Defense in Depth*