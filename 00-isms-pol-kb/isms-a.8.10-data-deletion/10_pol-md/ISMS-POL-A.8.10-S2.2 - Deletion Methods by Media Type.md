# ISMS-POL-A.8.10-S2.2
## Information Deletion - Deletion Methods by Media Type

**Document ID**: ISMS-POL-A.8.10-S2.2
**Title**: Information Deletion - Deletion Methods by Media Type  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / IT Operations | Initial deletion methods and media sanitization requirements |

**Review Cycle**: Annually (or upon significant technology changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: IT Infrastructure Manager
- Compliance Review: Data Protection Officer (DPO)

**Distribution**: IT operations, data center staff, asset management, procurement  
**Related Documents**: ISMS-IMP-A.8.10.2 (Deletion Methods Assessment), ISMS-POL-A.8.24 (Cryptography Policy), NIST SP 800-88 Rev. 1 (informational reference)

---

## 2.2.1 Purpose and Scope

This section establishes **mandatory requirements** for deletion methods based on media type and data sensitivity. These requirements ensure data cannot be recovered after deletion while balancing practicality, cost, and environmental considerations.

**In Scope**: Deletion methods for all media types, tool validation, verification procedures  
**Primary Stakeholders**: IT Operations, Data Center Staff, Asset Management  
**Implementation Evidence**: ISMS-IMP-A.8.10.2 (Deletion Methods Assessment)

**Foundational Principle**: "Deletion" means rendering data **practically irrecoverable** with reasonable effort and cost by adversaries with appropriate capability.

---

## 2.2.2 NIST SP 800-88 Sanitization Framework

### 2.2.2.1 Sanitization Levels (Informational Reference)

Organizations **SHOULD** align deletion methods with NIST SP 800-88 Rev. 1 sanitization levels:

| Level | Definition | Use Case | Recoverability |
|-------|------------|----------|----------------|
| **Clear** | Logical overwriting of data | Media remains in organization control, general reuse | Not recoverable with standard tools |
| **Purge** | Physical or cryptographic destruction | Media leaving organization or high-sensitivity reuse | Not recoverable with laboratory techniques |
| **Destroy** | Physical destruction of media | End-of-life, extreme sensitivity | Physically impossible to recover |

**Note**: NIST SP 800-88 is referenced as **best practice guidance** (not mandatory compliance requirement per ISMS-POL-00 regulatory framework).

### 2.2.2.2 Deletion Method Selection Criteria

Organizations **SHALL** select deletion methods based on:

- **Data sensitivity classification** (public, internal, confidential, restricted)
- **Media type** (HDD, SSD, cloud, tape, paper, mobile)
- **Media destination** (reuse internally, external transfer, disposal)
- **Regulatory requirements** (GDPR, FADP, sector-specific)
- **Technical feasibility** (can the method be applied to this media?)
- **Cost and environmental impact** (balance security with sustainability)

**Decision Matrix** (see Annex S5.A for detailed matrix):
- **Low sensitivity + Internal reuse** → Clear (logical deletion)
- **Medium sensitivity + External transfer** → Purge (secure erase)
- **High sensitivity + Any scenario** → Purge or Destroy
- **End-of-life media** → Destroy (physical destruction)

---

## 2.2.3 Hard Disk Drives (HDD)

### 2.2.3.1 Clear Method - Overwrite

For HDDs containing **non-sensitive or low-sensitivity data** being reused internally, organizations **MAY** use:

**Overwrite Method**:
- **DoD 5220.22-M** (3-pass overwrite: random, complement, random) — widely accepted but time-consuming
- **Single-pass overwrite** with zeros or random data — sufficient for modern HDDs per NIST SP 800-88
- **Tool examples**: DBAN (Darik's Boot and Nuke), `shred` (Linux), BitRaser, Blancco

**Requirements**:
- Overwrite **entire addressable space** including remapped sectors
- **Verify completion** through tool logs
- Document **drive serial number**, date, tool used, operator

**Limitation**: Overwrite does NOT work reliably on damaged drives or drives with bad sectors.

### 2.2.3.2 Purge Method - Cryptographic Erase or Secure Erase

For HDDs containing **sensitive data** or leaving organizational control, organizations **SHALL** use:

**Cryptographic Erase** (preferred for encrypted drives):
- **Delete encryption key** from self-encrypting drive (SED)
- **Verify cryptographic erasure** through ATA Secure Erase Enhanced command or vendor tools
- **Requirement**: Drive must support hardware encryption (TCG Opal, AES-256)
- **Fastest method** (seconds vs. hours for overwrite)

**ATA Secure Erase**:
- Use ATA Secure Erase command (overwrites all blocks including remapped sectors)
- **Tool examples**: `hdparm` (Linux), Parted Magic, vendor-specific utilities
- **Verify** with SMART data showing erase completion

**Degaussing** (magnetic field destruction):
- Use **NSA/CSS EPL-listed degausser** for classified environments
- **Renders drive permanently inoperable** (cannot be reused)
- **Document degausser model**, serial number, date, operator
- Not applicable for SSD or flash media (degaussing doesn't affect solid-state)

### 2.2.3.3 Destroy Method - Physical Destruction

For **end-of-life HDDs** or **extremely sensitive data**, organizations **SHALL** use:

**Physical Destruction Methods**:
- **Shredding**: Reduce platters to particles ≤2mm (NSA standard)
- **Disintegration**: Industrial shredder meeting DIN 66399 P-5 or higher
- **Incineration**: Complete combustion at certified facility
- **Crushing/Bending**: Deform platters (least secure, not recommended alone)

**Requirements**:
- **Certificate of Destruction** from certified vendor (ISO 27001, NAID AAA certified)
- **Chain of custody** documentation from removal to destruction
- **Witness destruction** for high-sensitivity drives (video recording or physical presence)
- Destruction facility **audited annually**

---

## 2.2.4 Solid State Drives (SSD) and Flash Media

### 2.2.4.1 SSD-Specific Challenges

**Critical Understanding**: SSDs behave differently than HDDs due to:
- **Wear leveling**: Data blocks moved to prevent cell degradation
- **Over-provisioning**: Hidden storage not visible to OS
- **TRIM command**: OS hints to SSD which blocks are deleted (unreliable for sanitization)
- **Bad block remapping**: Damaged blocks contain old data

**Result**: Traditional overwrite methods are **INEFFECTIVE** for SSDs. Deleted data may persist in over-provisioned areas.

### 2.2.4.2 Clear Method - Not Recommended for SSD

Organizations **SHOULD NOT** rely on file deletion or overwrite for SSD sanitization.

**Exception**: ATA Secure Erase (see Purge below) may be categorized as "Clear" for low-sensitivity internal reuse.

### 2.2.4.3 Purge Method - Cryptographic Erase or Secure Erase

For SSDs, organizations **SHALL** use:

**Cryptographic Erase** (strongly preferred):
- **Self-Encrypting Drive (SED)** with instant erase capability
- **Delete encryption key** → renders all data irrecoverable
- **Verify** through vendor tools or ATA Security Erase Unit command

**ATA Secure Erase** (NVMe Sanitize):
- Use vendor-specific secure erase command
- **NVMe Format** with cryptographic erase or user data erase
- **Warning**: Firmware bugs may cause incomplete erasure — verify with vendor advisories
- Test with data recovery tools if feasible

**Full Drive Encryption + Key Deletion**:
- If SSD lacks SED, use OS-level encryption (BitLocker, LUKS, FileVault)
- Delete encryption key from all locations (TPM, key escrow)
- **Note**: Less reliable than hardware SED due to key recovery risks

### 2.2.4.4 Destroy Method - Physical Destruction

For end-of-life SSDs or when secure erase is unavailable/untrusted:

**Physical Destruction**:
- **Shredding**: Reduce NAND chips to particles ≤2mm
- **Disintegration**: Per DIN 66399 P-5 or higher
- **Do NOT use degaussing** (ineffective against flash memory)

**Note**: SSDs are more difficult to destroy than HDDs due to distributed NAND chips. Ensure destruction method addresses all memory chips.

---

## 2.2.5 Magnetic Tape

### 2.2.5.1 Clear Method - Overwrite

For tapes being reused internally, organizations **MAY** use:

**Overwrite**:
- Write new data to entire tape (replaces old data)
- **Verify** overwrite completion through tape drive logs

**Limitation**: Time-consuming for large capacity tapes (LTO-9 = 18TB native).

### 2.2.5.2 Purge Method - Degaussing

For tapes leaving organizational control, organizations **SHALL** use:

**Degaussing**:
- Use **NSA/CSS EPL-listed degausser** rated for tape technology
- **Verify degauss** with magnetic field strength meter
- Document degausser model, tape serial number, operator, date
- **Renders tape unusable** for future writes

### 2.2.5.3 Destroy Method - Physical Destruction

For end-of-life tapes:

**Physical Destruction**:
- **Shredding**: Cut tape into particles ≤6mm (DIN 66399 P-4)
- **Incineration**: Complete combustion
- Certificate of Destruction required

---

## 2.2.6 Cloud Storage and Virtual Media

### 2.2.6.1 Cloud Storage Deletion Challenges

**Unique Considerations**:
- **No physical access** to storage media
- **Data replication** across multiple locations/regions
- **Shared infrastructure** (multi-tenancy)
- **Backup and snapshot persistence**
- **Vendor deletion processes** (trust but verify)

### 2.2.6.2 Clear Method - Logical Deletion

For cloud storage, organizations **SHALL** use provider deletion APIs:

**Object Storage (S3, Azure Blob, GCS)**:
- Delete objects via API (DELETE request)
- **Verify deletion** through list operations (object no longer exists)
- **Delete all versions** in versioned buckets
- **Empty then delete buckets** to ensure no residual data

**Block Storage (EBS, Azure Disk, Persistent Disk)**:
- Delete volumes via cloud console/API
- **Verify deletion** through volume list (status = deleted)

**File Storage (EFS, Azure Files, Cloud Filestore)**:
- Delete files and file systems
- Verify through file system list

**Limitation**: Logical deletion relies on vendor processes — no direct verification of physical erasure.

### 2.2.6.3 Purge Method - Cryptographic Erasure

For cloud storage, organizations **SHOULD** implement:

**Client-Side Encryption**:
- Encrypt data **before upload** to cloud (customer-managed keys)
- Store encryption keys in separate key management service (KMS)
- **Delete encryption keys** when data deletion is required
- Data in cloud becomes cryptographically irrecoverable

**Provider-Managed Encryption**:
- Use cloud provider KMS (AWS KMS, Azure Key Vault, Cloud KMS)
- **Delete customer-managed keys** after data deletion
- **Verify key deletion** through KMS audit logs

**Requirement**: Encryption keys **MUST** be deleted from all locations (production, backup, escrow).

### 2.2.6.4 Multi-Region and Backup Deletion

Organizations **SHALL**:

- **Delete from all regions** where data is replicated
- **Delete snapshots and backups** according to backup retention policy (ISMS-POL-A.8.10-S2.1)
- **Verify deletion** across all cloud regions and availability zones
- **Document deletion timeline** from cloud provider (see ISMS-POL-A.8.10-S2.4)

**See ISMS-POL-A.8.10-S2.4 for detailed third-party cloud deletion requirements.**

---

## 2.2.7 Databases and Structured Data

### 2.2.7.1 Logical Deletion vs. Physical Deletion

Organizations **SHALL** understand the difference:

| Method | Description | Data Recoverability | Use Case |
|--------|-------------|---------------------|----------|
| **Soft Delete** | Mark record as deleted (flag/timestamp) | Easily recoverable | Temporary deletion, undo functionality |
| **Hard Delete** | DELETE SQL statement | Recoverable from database logs/backups | Standard deletion |
| **Purge/Vacuum** | Reclaim physical space | Not recoverable from database (still in backups) | Permanent deletion |
| **Cryptographic Erase** | Delete row encryption key | Cryptographically irrecoverable | GDPR right to erasure compliance |

### 2.2.7.2 Database Deletion Requirements

For GDPR-compliant deletion, organizations **SHALL**:

**Immediate Deletion**:
- Use **hard delete** (DELETE/DROP statements) for active data
- **VACUUM** database to reclaim space (PostgreSQL) or **OPTIMIZE TABLE** (MySQL)
- **Verify deletion** through query (record no longer exists)

**Transaction Log Considerations**:
- **Truncate transaction logs** after deletion (prevents recovery from logs)
- **Backup deletion**: See backup retention requirements (ISMS-POL-A.8.10-S2.1)

**Row-Level Encryption** (recommended):
- Encrypt individual records with unique keys
- **Delete encryption key** when record is deleted
- Data persists in backups but is cryptographically irrecoverable

### 2.2.7.3 Data Masking vs. Deletion

**Data masking is NOT deletion** but may be acceptable when:
- **Legal requirement** prohibits full deletion (e.g., financial audit trails)
- **Masked data** cannot identify individuals (anonymization, pseudonymization per GDPR Article 4)
- **Documented justification** approved by DPO

**Requirements for masking in lieu of deletion**:
- Masking must be **irreversible** (not simple replacement)
- Masked data must not be **re-identifiable** through combination with other data
- Regular **effectiveness review** of masking techniques

---

## 2.2.8 Mobile Devices and Endpoints

### 2.2.8.1 Mobile Device Deletion

For smartphones, tablets, and laptops, organizations **SHALL**:

**Factory Reset**:
- Perform **full factory reset** through device settings
- **Remove accounts** (iCloud, Google, Microsoft) before reset
- **Verify reset** by attempting data recovery (if feasible)

**Mobile Device Management (MDM)**:
- Use **remote wipe** capability (enterprise wipe or full wipe)
- **Verify wipe** through MDM console (device status = wiped)
- **Unenroll device** from MDM after wipe

**Encryption Requirement**:
- Devices **MUST** be encrypted (BitLocker, FileVault, Android/iOS encryption)
- Factory reset on encrypted device = cryptographic erasure

### 2.2.8.2 Endpoint Computer Deletion

For desktops and laptops, organizations **SHALL**:

**OS Reinstallation**:
- Reinstall operating system (overwrites most data)
- **Not sufficient alone** for sensitive data

**Disk Encryption + Key Deletion**:
- Encrypted disk (BitLocker, FileVault, LUKS)
- Delete encryption key from TPM/keyring
- Perform secure erase on drive (see HDD/SSD sections above)

**Physical Removal and Destruction**:
- Remove storage media from device
- Destroy per HDD/SSD destruction requirements

---

## 2.2.9 Paper and Physical Media

### 2.2.9.1 Paper Document Destruction

For paper documents containing **confidential or personal data**, organizations **SHALL**:

**Shredding Requirements**:
- **Cross-cut shredder**: Minimum DIN 66399 P-4 (particle size ≤160mm²)
- **High security**: DIN 66399 P-5 for highly sensitive documents (particle size ≤30mm²)
- **On-site shredding** preferred for high sensitivity
- **Certificate of Destruction** from certified shredding vendor

**Pulping/Incineration**:
- Acceptable for bulk paper destruction
- Use certified destruction facility
- Certificate of Destruction required

### 2.2.9.2 Other Physical Media

For non-electronic media, organizations **SHALL**:

| Media Type | Destruction Method | Standard |
|------------|-------------------|----------|
| **Microfilm/Microfiche** | Shredding, incineration | DIN 66399 O-4 (optical media) |
| **Photographs** | Shredding, incineration | DIN 66399 P-4 |
| **Printed Circuit Boards** | Shredding, disintegration | Physical destruction of chips |
| **USB/Removable Media** | Physical destruction | Same as SSD/flash |

---

## 2.2.10 Deletion Tool Validation and Approval

### 2.2.10.1 Tool Approval Requirements

Organizations **SHALL** validate deletion tools before operational use:

**Validation Process**:
- **Test deletion effectiveness** on sample media
- **Attempt data recovery** with forensic tools (FTK, EnCase, Autopsy)
- **Verify no data recovery** possible with reasonable effort
- **Document test results** (media tested, tool version, recovery attempts, results)
- **Approve tool** by CISO or Information Security Manager

**Approved Tool List**:
- Maintain list of approved deletion tools (see Annex S5.A)
- Include tool name, version, media types, approval date, limitations
- **Review annually** and when new tools are introduced

### 2.2.10.2 Tool Examples (Informational)

Common deletion tools include:

| Tool | Media Type | Method | Notes |
|------|-----------|--------|-------|
| **DBAN** | HDD | Overwrite | Free, bootable, widely used |
| **Blancco** | HDD, SSD, mobile | Secure erase, reports | Commercial, certificate generation |
| **BitRaser** | HDD, SSD, mobile | Secure erase | Commercial, enterprise management |
| **hdparm** | HDD, SSD | ATA Secure Erase | Linux command-line, free |
| **nvme-cli** | NVMe SSD | NVMe Sanitize | Linux command-line, free |
| **Parted Magic** | HDD, SSD | Secure Erase | Bootable, GUI, commercial |
| **shred** | Files (HDD only) | Overwrite | Linux built-in, NOT for SSD |
| **Cloud APIs** | Cloud storage | Provider deletion | S3 CLI, Azure CLI, gcloud |

**Note**: Tool selection depends on media type, organizational budget, and scale of deletion operations.

---

## 2.2.11 Deletion Verification

### 2.2.11.1 Verification Requirements

Organizations **SHALL** verify deletion through:

**Automated Verification**:
- **Tool logs**: Deletion tool reports success/failure
- **SMART data**: HDD/SSD self-monitoring shows secure erase completion
- **API responses**: Cloud provider confirms object deletion

**Manual Verification** (sampling):
- **Forensic analysis**: Attempt data recovery on 5-10% of sanitized media (random sampling)
- **Visual inspection**: Physical destruction confirmed (media rendered unusable)
- **Certificate review**: Third-party destruction certificates validated

**Continuous Verification**:
- **Monthly audits**: Review deletion logs for completeness
- **Quarterly testing**: Verify tool effectiveness with forensic recovery attempts
- **Annual assessment**: Independent validation of deletion processes

### 2.2.11.2 Verification Documentation

Organizations **SHALL** maintain:

- **Deletion logs**: Media ID, method, tool, date, operator, result
- **Certificates of Destruction**: From third-party vendors
- **Verification test results**: Forensic recovery attempts, outcomes
- **Non-compliance reports**: Failed deletions, remediation actions

**Retention**: Deletion evidence retained for **3 years** minimum (audit requirement).

---

## 2.2.12 Environmental and Sustainability Considerations

### 2.2.12.1 Balance Security and Sustainability

Organizations **SHOULD** consider environmental impact:

**Preference Hierarchy** (security permitting):
1. **Cryptographic erase → Reuse** (zero waste)
2. **Secure erase → Reuse** (extends device life)
3. **Secure erase → Recycle** (responsible disposal)
4. **Physical destruction → Recycle materials** (metal recovery)
5. **Physical destruction → Landfill** (last resort)

**Certified Recyclers**:
- Use **R2 (Responsible Recycling)** or **e-Stewards** certified facilities
- Obtain **Certificate of Recycling** in addition to destruction certificate
- Verify recycler performs data destruction before recycling

### 2.2.12.2 Regulatory Compliance for Disposal

Organizations **SHALL** comply with:
- **WEEE Directive** (EU): Waste Electrical and Electronic Equipment regulations
- **Swiss ORDEA** (Swiss): Electrical and Electronic Equipment Ordinance
- Local e-waste disposal regulations

---

## 2.2.13 Deletion Method Selection Matrix

Organizations **SHALL** use the following decision framework (see Annex S5.A for complete matrix):

| Media Type | Sensitivity | Destination | Recommended Method | Alternative |
|------------|-------------|-------------|-------------------|-------------|
| **HDD** | Low | Internal reuse | Single-pass overwrite | ATA Secure Erase |
| **HDD** | Medium/High | External/disposal | ATA Secure Erase or Degaussing | Physical destruction |
| **HDD** | Any | End-of-life | Physical destruction | Degaussing + recycling |
| **SSD** | Any | Internal reuse | Cryptographic erase (SED) | ATA Secure Erase (verify) |
| **SSD** | Medium/High | External/disposal | Cryptographic erase + physical destruction | Physical destruction alone |
| **SSD** | Any | End-of-life | Physical destruction | N/A |
| **Cloud** | Any | Logical deletion | API deletion + crypto erase (key deletion) | Provider deletion only |
| **Tape** | Low/Medium | Internal reuse | Overwrite | Degaussing |
| **Tape** | High | Disposal | Degaussing | Physical destruction |
| **Mobile** | Any | Reuse/disposal | Factory reset (encrypted device) | MDM remote wipe |
| **Paper** | Confidential | Disposal | Cross-cut shred (P-4) | Secure incineration |
| **Paper** | Highly sensitive | Disposal | Cross-cut shred (P-5) | Pulping + verification |

---

## 2.2.14 Exceptions and Special Cases

### 2.2.14.1 When Standard Methods Fail

If standard deletion methods cannot be applied, organizations **SHALL**:

- **Document reason** for failure (damaged media, technical limitation)
- **Implement compensating controls**:
  - Physical destruction (if media cannot be sanitized)
  - Secure storage until destruction is feasible
  - Enhanced encryption (if data must persist)
- **Escalate to CISO** for high-sensitivity data
- **Record exception** in deletion log

### 2.2.14.2 Forensic and Legal Investigation Data

Data under legal hold or forensic investigation **SHALL**:
- Remain in **secure, isolated storage** (not deleted)
- Apply **access controls** (need-to-know basis)
- **Encrypt at rest** during hold period
- **Delete immediately** upon hold release per normal procedures

---

**END OF DOCUMENT**

*"If you can still read the data after deletion, you didn't actually delete it."* — Feynman (definitely said this while working on Los Alamos data sanitization... probably)