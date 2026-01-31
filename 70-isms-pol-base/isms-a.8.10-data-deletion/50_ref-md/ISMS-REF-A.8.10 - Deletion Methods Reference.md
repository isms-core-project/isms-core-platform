# ISMS-REF-A.8.10 — Deletion Methods Reference
## Media Sanitization Standards & Tool Selection (Non-ISMS Technical Reference)

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Deletion Methods Reference |
| **Document Type** | Internal - Technical Reference (Not ISMS) |
| **Document ID** | ISMS-REF-A.8.10 |
| **Document Creator** | Chief Information Security Officer (CISO) |

| **Approved By** | CISO (Technical Reference - No Executive Approval Required) |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / IT Operations | Initial technical reference for ISO 27001:2022 certification |

**Review Cycle**: As needed (technology and tool evolution)  
**Next Review Date**: [Date + 12 months]  
**Approvers**: IT Operations Manager / Security Architecture (technical reference, no ISMS approval required)

**Distribution**: IT Operations, Security Engineering, System Owners (for technical implementation awareness)

---

⚠️ **IMPORTANT – NON-ISMS TECHNICAL SUPPORT DOCUMENT**

This document is provided for informational and awareness purposes only.

- This document is NOT part of the Information Security Management System (ISMS).
- This document does NOT define mandatory deletion controls or requirements.
- This document does NOT establish binding requirements, deadlines, KPIs, or SLAs.
- This document does NOT mandate the use, prohibition, or configuration of specific deletion tools, vendors, or platforms.
- This document does NOT override or extend any ISMS policy.

All binding deletion requirements, obligations, and governance decisions are defined exclusively in **ISMS-POL-A.8.10 (Information Deletion Policy)** and other approved ISMS documentation.

This document serves solely as a technical reference to:
- Describe commonly used deletion methods and media sanitization techniques
- Track industry standards evolution and tool availability
- Support deletion method selection awareness
- Inform technical discussions and future implementation planning
- **This document must not be used as audit evidence of implementation**

Use of this document does not imply implementation, compliance, or operational maturity.

**Critical Positioning Statement**:
This document intentionally provides technical detail beyond what is required for ISO/IEC 27001 policy documentation. Its purpose is technical awareness only. No auditor conclusions shall be drawn from the presence, absence, or classification of any deletion method, tool, or vendor listed herein.

---

## 1. Document Purpose and Scope

### 1.1 Purpose

This document provides a technical overview of deletion methods and media sanitization techniques commonly used for information deletion. It is intended to support:

- Technical awareness of available deletion options
- Understanding of method effectiveness by media type
- Context for deletion method selection during implementation
- Future implementation planning discussions
- Tool evaluation criteria

### 1.2 What This Document Is NOT

This document does NOT:
- Define [Organization]'s approved or prohibited deletion methods
- Establish mandatory implementation requirements
- Create compliance obligations or audit criteria
- Replace ISMS-POL-A.8.10 policy requirements
- Mandate specific tool selection or vendor relationships
- Establish deletion procedures or verification processes

### 1.3 Relationship to ISMS

This document is a **non-binding technical reference**. All deletion control requirements are defined exclusively in ISMS-POL-A.8.10.

Implementation decisions are documented through ISMS-IMP-A.8.10 procedures based on risk assessment, operational context, and regulatory requirements.

### 1.4 Content Organization

This reference organizes deletion methods by:
- Media type (magnetic, solid-state, cloud, paper, optical)
- Sanitization method (Clear, Purge, Destroy)
- Tool and vendor landscape
- Cloud provider deletion capabilities
- Industry standards alignment

---

## 2. NIST SP 800-88 Sanitization Framework

### 2.1 Overview

NIST Special Publication 800-88 Revision 1 ("Guidelines for Media Sanitization") provides authoritative guidance on media sanitization methods. While this is an informational reference (not mandatory unless contractually required), it represents industry best practice.

**Three Sanitization Categories**:

1. **Clear**: Apply logical techniques to sanitize data in all user-addressable storage locations for protection against simple non-invasive data recovery techniques
2. **Purge**: Apply physical or logical techniques to render target data recovery infeasible using state-of-the-art laboratory techniques
3. **Destroy**: Render media unusable and target data recovery infeasible using state-of-the-art laboratory techniques

### 2.2 Method Selection Decision Factors

**Media Destination**:
- Remaining in organization control → Clear may be sufficient (depending on classification)
- Leaving organization control → Purge minimum
- Disposal / end-of-life → Destroy recommended for sensitive data

**Data Classification**:
- Public data → Clear sufficient
- Internal data → Clear or Purge
- Confidential data → Purge minimum
- Restricted data → Destroy or Purge with verification

**Media Reuse Intent**:
- Reuse within organization → Clear or Purge
- External sale/donation → Purge or Destroy
- Disposal → Destroy

---

## 3. Magnetic Media Deletion (HDDs, Tape)

### 3.1 Hard Disk Drives (HDD)

**Media Characteristics**:
- Data stored magnetically on rotating platters
- Standard file deletion only removes file system pointers, not actual data
- Data remains recoverable until overwritten
- Well-established sanitization methods

**3.1.1 Clear Methods**

**Single-Pass Overwrite**:
- Write pattern over all addressable locations
- NIST SP 800-88: Single pass sufficient for modern drives
- Legacy multi-pass methods (DoD 5220.22-M 7-pass) no longer necessary per NIST
- Tools: `shred` (Linux), `sdelete` (Windows), `dd` (Unix/Linux)
- Effectiveness: Adequate for non-sensitive data, internal reuse
- Limitations: Does not address bad sectors or firmware-reserved areas

**3.1.2 Purge Methods**

**ATA Secure Erase**:
- Built-in drive command that overwrites all addressable locations including remapped sectors
- Manufacturer-implemented, leverages drive controller knowledge of all storage areas
- Single command, fast execution (typically 1-4 hours for modern drives)
- Tools: `hdparm` (Linux), Parted Magic, manufacturer utilities
- Effectiveness: Highly effective for HDDs, recommended method
- Verification: Check SMART data or ATA command completion status

**Degaussing**:
- Expose drive to powerful magnetic field to disrupt magnetic domains
- Renders drive permanently inoperable (cannot be reused)
- Requires NSA Evaluated Products List (EPL) degausser for classified data
- Effectiveness: Very high for magnetic media
- Limitations: Drive unusable after degaussing, expensive equipment required
- Use Case: High-security environments, classified data disposal

**3.1.3 Destroy Methods**

**Physical Disintegration**:
- Shred drive into small particles (≤2mm recommended per DIN 66399)
- Incineration at high temperature
- Pulverization
- Melting
- Vendor Services: NAID AAA certified destruction vendors
- Effectiveness: Highest level, data recovery infeasible
- Use Case: Highest sensitivity data, end-of-life disposal

**3.1.4 Cryptographic Erasure**

**Self-Encrypting Drives (SED)**:
- Hardware-based full disk encryption
- Data encrypted with Data Encryption Key (DEK)
- DEK encrypted with Authentication Key (AK)
- Sanitization: Destroy cryptographic keys
- Tools: Manufacturer SED management utilities, sedutil
- Effectiveness: Very high IF encryption was enabled from deployment
- Limitations: Only effective if drive was encrypted; verify encryption status before relying on crypto erase

### 3.2 Magnetic Tape

**Media Characteristics**:
- Sequential access media
- Common for backup and archival
- Multiple read/write passes over same media

**3.2.1 Clear Method**

**Full Tape Overwrite**:
- Write pattern over entire tape length
- Time-consuming (hours per tape)
- Tools: Tape drive native overwrite commands
- Effectiveness: Adequate for internal reuse
- Limitation: Very slow, does not address damaged tape segments

**3.2.2 Purge Method**

**Degaussing**:
- Preferred method for tape media
- Fast (seconds per tape)
- Renders tape unusable for future use
- Requires NSA EPL degausser for sensitive data
- Effectiveness: Very high
- Use Case: Sensitive backup tape disposal, decommissioning

**3.2.3 Destroy Method**

**Physical Destruction**:
- Shredding
- Incineration
- Pulverization
- Effectiveness: Highest
- Use Case: End-of-life, highest sensitivity

---

## 4. Solid-State Media Deletion (SSD, NVMe, Flash)

### 4.1 Solid-State Characteristics

**Why SSDs Are Different**:
- Wear-leveling algorithms distribute writes across all cells
- Over-provisioning reserves storage cells not visible to OS
- Garbage collection moves data blocks
- TRIM command manages deleted blocks
- Result: Standard overwriting does NOT reliably sanitize SSDs

**Sanitization Challenges**:
- Cannot guarantee all physical storage locations overwritten
- Firmware controls actual data placement
- Hidden areas (over-provisioning, bad block remapping)

### 4.2 SSD / NVMe Sanitization Methods

**4.2.1 Purge Methods**

**ATA Secure Erase / NVMe Sanitize**:
- Manufacturer-implemented command
- SSD: ATA Security Erase command
- NVMe: NVMe Sanitize (Crypto Erase or Block Erase)
- Leverages firmware knowledge of all storage cells
- Tools: `nvme-cli` (NVMe), `hdparm` (SATA SSD), Parted Magic
- Effectiveness: High (if properly implemented by manufacturer)
- Verification: Tool completion status, attempt data recovery sampling
- Caution: Implementation quality varies by manufacturer

**Cryptographic Erasure**:
- Self-Encrypting Drives (SED) or software-based FDE
- Destroy encryption key to render data inaccessible
- Very fast (seconds)
- Tools: Manufacturer SED utilities, OS FDE tools (BitLocker, FileVault, LUKS)
- Effectiveness: Very high IF drive was encrypted from deployment
- **Critical Requirement**: Verify encryption was enabled; post-deployment encryption less effective
- Preferred method for SSDs where encryption enabled

**4.2.2 Destroy Method**

**Physical Destruction**:
- Shred to ≤2mm particles
- Disintegration
- Pulverization
- Incineration
- Effectiveness: Highest, data recovery infeasible
- Use Case: High-sensitivity data, when Secure Erase not verified effective
- Note: Expensive for large volumes

**4.2.3 NOT Recommended for SSDs**

❌ **Standard Overwriting**: Ineffective due to wear-leveling and over-provisioning
❌ **Single-File Deletion Tools**: Do not sanitize deleted space on SSDs
❌ **Multi-Pass Overwrite**: No additional benefit over single pass, wastes write cycles

### 4.3 USB Flash Drives / SD Cards

**Sanitization**:
- Similar challenges to SSDs (flash memory, wear-leveling)
- Secure Erase: If supported (rare in consumer USB drives)
- Cryptographic Erasure: If encrypted (BitLocker To Go, hardware-encrypted drives)
- **Practical Approach**: Physical destruction often most reliable method
- Shred or incinerate for sensitive data
- Low-cost media makes destruction economically viable

---

## 5. Cloud Storage Deletion

### 5.1 Cloud Deletion Challenges

**Multi-Tenancy**:
- Customer data logically separated but physically co-located
- Risk of data remanence or cross-tenant leakage
- Reliance on provider isolation controls

**Data Distribution**:
- Data replicated across multiple geographic locations
- Multiple availability zones and regions
- Backup copies managed by provider

**Limited Control**:
- No physical access to storage media
- Reliance on provider deletion APIs and procedures
- Trust in provider implementation

### 5.2 Cloud Deletion Methods

**5.2.1 Logical Deletion (Clear)**

**API-Based Deletion**:
- Use cloud provider API to delete objects, volumes, databases
- Examples: AWS S3 DeleteObject, Azure Blob Delete, GCP Storage Delete
- Verification: API response codes (200/204 success)
- Effectiveness: Removes logical access, provider purges physical storage per their schedule
- Limitation: Trust provider to physically sanitize storage

**5.2.2 Cryptographic Erasure (Purge - Preferred)**

**Customer-Managed Encryption Keys**:
- Encrypt data with customer-managed keys (CMK)
- AWS: KMS Customer Managed Keys, S3 SSE-C
- Azure: Customer Managed Keys (CMK), Azure Key Vault
- GCP: Customer-Managed Encryption Keys (CMEK)
- Deletion: Destroy encryption keys, rendering data inaccessible
- Verification: Confirm key deletion in key management service
- Effectiveness: Very high, data cryptographically irrecoverable
- **Recommended Approach**: Combine API deletion + key destruction

**5.2.3 Provider Deletion Certificates**

Some cloud providers offer deletion attestations:
- AWS: Deletion confirmation via CloudTrail logs
- Azure: Audit logs
- GCP: Cloud Audit Logs
- Third-Party Certification: SOC 2 Type II reports covering deletion controls
- Use Case: Contractual evidence of deletion, regulatory compliance

### 5.3 Cloud Provider Deletion by Service Type

**IaaS (Compute, Storage)**:
- Virtual machines: Terminate instance + delete EBS volumes/managed disks
- Object storage: API delete objects + delete bucket + destroy CMK
- Block storage: Delete volumes + snapshots + backups
- Verification: API responses, service console confirmation

**PaaS (Databases, Applications)**:
- Databases: Delete database instance + automated backups + manual snapshots
- Application services: Delete application + data stores + logs
- Verification: Service-specific deletion confirmations

**SaaS (Applications)**:
- Application-level deletion (e.g., delete user account in SaaS app)
- Request data export before deletion (GDPR portability)
- Obtain deletion confirmation from SaaS provider
- Limitation: Minimal control, full reliance on provider procedures

---

## 6. Mobile Devices

### 6.1 Smartphones and Tablets

**Sanitization Approach**:

**Encrypted Devices** (Modern iOS, Android with encryption enabled):
1. Mobile Device Management (MDM) remote wipe
2. Factory reset
3. Encryption key destruction
4. Verification: MDM console confirmation, attempt device access
5. Effectiveness: High for properly encrypted devices

**Non-Encrypted or Unknown Encryption Status**:
1. Physical destruction of storage component (remove and shred)
2. Use Case: High-sensitivity data on older devices
3. Effectiveness: Highest

**Tools**:
- MDM Solutions: Microsoft Intune, Jamf Pro, VMware Workspace ONE, MobileIron
- Native: iOS "Erase All Content and Settings", Android Factory Reset
- Verification: MDM check-in attempt after wipe

### 6.2 Laptops and Desktops

**Sanitization**:
- Magnetic HDD: ATA Secure Erase or physical destruction
- SSD: Cryptographic erasure (BitLocker, FileVault) or physical destruction
- Hybrid (HDD + SSD cache): Sanitize both components
- Approach: Remove storage media, sanitize separately using media-specific methods

---

## 7. Paper and Optical Media

### 7.1 Paper Documents

**Shredding Standards** (DIN 66399):

| Security Level | Particle Size | Use Case |
|---------------|---------------|----------|
| P-1 | <12mm strips | General waste, no confidentiality |
| P-2 | <6mm strips | Internal documents, low sensitivity |
| P-3 | <2mm strips or 320mm² particles | Confidential business documents |
| **P-4** | <2mm strips or 160mm² particles | **Confidential data, PII (recommended minimum)** |
| **P-5** | <0.8mm strips or 30mm² particles | **Highly sensitive PII, Restricted data** |
| P-6 | <1mm strips or 10mm² particles | Classified government data |
| P-7 | <≤5mm² particles | Top secret data |

**Methods**:
- Cross-cut shredding (P-4 or P-5 minimum for sensitive data)
- Large volumes: Contracted destruction service (NAID AAA certified vendor)
- Certificate of Destruction required for confidential/restricted documents

**On-Site vs. Off-Site**:
- On-site shredding: Immediate destruction, chain of custody maintained
- Off-site shredding: Locked bins, scheduled pickup, certificate provided
- High-sensitivity: On-site witnessed destruction preferred

### 7.2 Optical Media (CD, DVD, Blu-ray)

**Characteristics**:
- Write-once media (cannot be overwritten)
- Physical destruction required

**Methods**:
- Physical shredding (small particles)
- Incineration
- Disintegration
- NOT ACCEPTABLE: Scratching, breaking (data often recoverable)

---

## 8. Virtual Environments

### 8.1 Virtual Machines

**Deletion Scope**:
- Virtual disk files (VMDK, VHD, VHDX, qcow2)
- Snapshots (all snapshot files)
- Templates (VM templates created from this VM)
- Configuration files
- Swap files

**Methods**:
- **Standard**: Delete VM + all associated files via hypervisor
- **Secure**: Secure wipe of virtual disk files before VM deletion
- **Crypto Erase**: If virtual disk encrypted, destroy encryption key
- Tools: Hypervisor management (vSphere, Hyper-V, KVM), `shred` for disk files

### 8.2 Containers and Container Images

**Deletion Scope**:
- Container instances
- Container images (local and registry)
- Persistent volumes
- Secrets and configuration

**Methods**:
- Stop and remove containers: `docker rm`, `kubectl delete pod`
- Delete images: `docker rmi`, registry deletion
- Delete volumes: `docker volume rm`, `kubectl delete pvc`
- Registry cleanup: Remove images from container registry

### 8.3 Databases

**Deletion Methods**:

**Logical Deletion**:
- `DELETE FROM table WHERE ...` (removes rows)
- `DROP TABLE` (removes table structure and data)
- `DROP DATABASE` (removes entire database)
- Follow-up: `VACUUM` (PostgreSQL), `OPTIMIZE TABLE` (MySQL) to reclaim space
- Limitation: Data may persist in transaction logs, temporary files

**Cryptographic Erasure** (Transparent Data Encryption enabled):
- Drop encrypted database
- Destroy encryption key
- Effectiveness: High for TDE-enabled databases
- Examples: SQL Server TDE, Oracle TDE, PostgreSQL pgcrypto

**Physical Deletion**:
- Delete database files after logical deletion
- Secure wipe underlying storage media
- Include transaction logs, backup files, temporary files

**Backup Deletion**:
- Critical: Delete database backups when production database deleted
- Includes full backups, differential, transaction logs, snapshots

---

## 9. Approved Tool Examples (Informational)

**Note**: This is NOT an approved vendor list. Organizations select tools based on their environment, risk assessment, and validation testing.

### 9.1 Open-Source / Built-In Tools

**Overwriting**:
- `shred` (Linux) - file and drive overwriting
- `dd` (Unix/Linux) - disk writing and wiping
- `sdelete` (Windows Sysinternals) - secure deletion
- `wipe` (Linux) - secure file deletion

**Secure Erase**:
- `hdparm` (Linux) - ATA Secure Erase for HDDs/SSDs
- `nvme-cli` (Linux) - NVMe Sanitize commands
- Parted Magic (Linux bootable) - drive sanitization suite

**Encryption**:
- BitLocker (Windows) - full disk encryption
- FileVault (macOS) - full disk encryption
- LUKS (Linux) - disk encryption
- VeraCrypt - cross-platform encryption

### 9.2 Commercial Tools

**Enterprise Deletion Software**:
- Blancco Drive Eraser - certified data erasure, certificate generation
- White Canyon WipeDrive - multi-platform drive wiping
- DBAN (Darik's Boot and Nuke) - free HDD wiping (legacy, not maintained)
- Ontrack Eraser - certified erasure solution

**Physical Destruction Equipment**:
- Degaussers: Garner, Proton Data Security, VS Security Products
- Shredders: HSM, Whitaker Brothers, SEM, MBM

**MDM Solutions**:
- Microsoft Intune
- Jamf Pro (Apple devices)
- VMware Workspace ONE
- MobileIron / Ivanti

### 9.3 Cloud-Native Tools

**AWS**:
- AWS CLI (delete operations)
- AWS KMS (key management and destruction)
- AWS Backup (backup deletion)

**Azure**:
- Azure CLI / PowerShell (delete operations)
- Azure Key Vault (key management)
- Azure Backup (backup deletion)

**GCP**:
- gcloud CLI (delete operations)
- Cloud KMS (key management)
- Cloud Backup (backup deletion)

---

## 10. Cloud Provider Deletion Capabilities

### 10.1 Hyperscale Providers (Tier 1)

**Amazon Web Services (AWS)**:
- Deletion APIs: S3 DeleteObject, EC2 TerminateInstances, RDS DeleteDBInstance
- Encryption: KMS customer-managed keys (CMK)
- Verification: CloudTrail logs, API responses
- Certifications: SOC 2 Type II, ISO 27001, ISO 27017, ISO 27018
- Documentation: AWS Well-Architected Framework, security whitepapers

**Microsoft Azure**:
- Deletion APIs: Storage Delete, VM Delete, SQL Database Delete
- Encryption: Customer-Managed Keys (CMK) via Azure Key Vault
- Verification: Azure Monitor logs, Activity logs
- Certifications: SOC 2 Type II, ISO 27001, ISO 27017, ISO 27018

**Google Cloud Platform (GCP)**:
- Deletion APIs: Storage Delete, Compute Instance Delete, Cloud SQL Delete
- Encryption: Customer-Managed Encryption Keys (CMEK)
- Verification: Cloud Audit Logs, Stackdriver logging
- Certifications: SOC 2 Type II, ISO 27001, ISO 27017, ISO 27018

**Common Capabilities**:
- API-based programmatic deletion
- Customer-managed encryption keys
- Audit logging of deletion operations
- Multi-region deletion support
- Certifications covering deletion controls

### 10.2 Other Cloud Providers

For Tier 2-10 providers per ISMS-REF-A.5.23:
- Assess deletion capabilities during vendor evaluation
- Request deletion SLA in contract
- Obtain deletion certificates or attestations
- Verify multi-tenant isolation procedures
- Review SOC 2 Type II reports for deletion controls

---

## 11. Verification and Validation

### 11.1 Verification Methods

**Automated Verification**:
- Tool completion status (exit codes, logs)
- API response codes (HTTP 200/204 for successful deletion)
- MDM console confirmation (mobile device wipes)
- Key management system logs (encryption key destruction)

**Manual Verification**:
- Sampling: Select random media, attempt data recovery
- Forensic validation: Use recovery tools on sanitized media
- Visual inspection: Physical destruction verification
- Certificate review: Third-party destruction certificates

**Third-Party Verification**:
- Certificates of Destruction from certified vendors
- SOC 2 Type II audit reports (deletion control verification)
- Cloud provider deletion attestations

### 11.2 Sampling Guidelines

For large-scale deletion operations:
- Sample 5-10% of deletion events
- Higher sampling (10-20%) for high-sensitivity data
- Focus sampling on new deletion methods or tools
- Document sampling results and any failures

### 11.3 Failure Handling

If verification fails:
- Stop using the deletion method immediately
- Quarantine media for re-sanitization
- Escalate to IT security team
- Use more robust deletion method (e.g., physical destruction)
- Document failure for lessons learned

---

## 12. Industry Standards Reference

**NIST Special Publications**:
- **NIST SP 800-88 Rev. 1**: Guidelines for Media Sanitization (primary reference)
- NIST SP 800-53 Rev. 5: Security Controls (MP family - Media Protection)
- NIST SP 800-171: Protecting CUI (media sanitization requirements)

**ISO Standards**:
- ISO/IEC 27040:2015: Storage Security (sanitization guidance)
- ISO/IEC 27555:2021: Guidelines on PII Deletion
- ISO/IEC 27017:2015: Cloud Services Security (deletion requirements)

**Industry Standards**:
- **DIN 66399**: Destruction of Data Media (paper shredding levels)
- IEEE 2883-2022: Standard for Sanitizing Storage
- ANSI/NAID AAA: Secure Destruction Standards (service providers)

**Legacy References** (superseded but may appear in contracts):
- DoD 5220.22-M: Data sanitization (superseded by NIST SP 800-88)
- NSA/CSS Manual 130-2: Data Sanitization (classified data, superseded)

---

## Appendix A: Deletion Method Selection Worksheet

Organizations can use this worksheet during implementation to document deletion method decisions:

**Data Category**: _______________________  
**Classification Level**: ⬜ Public ⬜ Internal ⬜ Confidential ⬜ Restricted

**Media Type**: _______________________  
**Media Destination**: ⬜ Internal Reuse ⬜ External Transfer ⬜ Disposal

**Recommended Method** (based on NIST SP 800-88 and data classification):
- Clear: _______________________
- Purge: _______________________
- Destroy: _______________________

**Selected Method**: _______________________  
**Justification**: _______________________

**Tool/Vendor**: _______________________  
**Verification Method**: _______________________

**Approved By**: _______________________  
**Date**: _______________________

---

**END OF TECHNICAL REFERENCE**

---

*This technical reference supports implementation of ISMS-POL-A.8.10. All binding requirements are defined in the policy document.*