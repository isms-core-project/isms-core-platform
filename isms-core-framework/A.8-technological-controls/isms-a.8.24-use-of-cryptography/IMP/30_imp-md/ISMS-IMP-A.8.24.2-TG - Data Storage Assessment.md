**ISMS-IMP-A.8.24.2-TG - Data Storage Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.24.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Data Storage Cryptographic Controls (Data at Rest) |
| **Related Policy** | ISMS-POL-A.8.24, Section 3.3 (Data Storage Encryption Requirements) |
| **Purpose** | Assess implementation of encryption controls for data at rest across 7 storage categories (Mobile Devices, Laptops, Servers, Databases, Cloud Storage, Backups, Removable Media) |
| **Target Audience** | System Administrators, Database Administrators, Storage Engineers, Security Engineers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Data Storage assessment workbook | ISMS Implementation Team |
---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

# Instructions for Completing This Assessment

## How to Use This Document

This technical specification defines the structure, validation rules, and formulas for the Data Storage Assessment Excel workbook (`ISMS-IMP-A.8.24.2_Data_Storage_[DATE].xlsx`).

**Workbook Generation:** Python script `generate_a824_2_data_storage_assessment.py` creates the workbook based on this specification.

**Assessment Completion Process:**

1. **Read each section** and determine if the storage type applies to your organization
2. **Check Yes/No/Not Applicable** for each assessment question
3. **If Yes:** Complete the assessment table with current encryption status
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

- Encryption configuration screenshots
- BitLocker/FileVault/LUKS status reports
- Database TDE (Transparent Data Encryption) configuration
- Cloud encryption settings documentation
- Key management system inventory
- Backup encryption verification reports
- Mobile device management (MDM) compliance reports
- Storage vendor encryption specifications
- Disk encryption audit logs
- Certificate/key rotation logs
- Hardware Security Module (HSM) integration documentation

---

# Common Column Structure (All Assessment Sheets)

All 7 assessment sheets (Mobile Devices through Removable Media) use this standard column layout:

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | Storage System/Device | 30 | Text | Free text |
| B | Data Classification | 18 | Dropdown | Public, Internal, Confidential, Restricted, N/A |
| C | Encryption Status | 18 | Dropdown | Encrypted, Not Encrypted, Partially Encrypted |
| D | Encryption Type | 20 | Dropdown | Full Disk, File-level, Database TDE, Volume, Container, Application-level, Hardware-based, N/A |
| E | Algorithm & Key Size | 18 | Text | Examples: AES-256-XTS, AES-128-GCM, AES-256-CBC |
| F | Key Management Method | 22 | Dropdown | HSM, Cloud KMS, TPM, Software-based, Manual, Vendor-managed, N/A |
| G | Key Rotation Enabled | 16 | Dropdown | Yes, No, N/A |
| H | Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| I | Evidence Location | 28 | Text | Free text (file path or evidence ID) |
| J | Gap Description | 30 | Text | Free text (required if Status = Partial/Non-Compliant) |
| K | Remediation Needed | 14 | Dropdown | Yes, No |
| L | Exception ID | 14 | Text | Free text (if formal exception submitted) |
| M | Risk ID | 14 | Text | Free text (if risk accepted) |
| N | Compensating Controls | 30 | Text | Free text (if applicable) |
| O | Responsible Person | 20 | Text | Free text (name and role) |
| P | Target Date | 14 | Date | Date picker (DD.MM.YYYY) |
| Q | Budget Required | 15 | Dropdown | Yes, No, Unknown |

---

# Mobile Devices

**Policy Requirement:** Mobile devices storing organizational data MUST use full device encryption 

**Assessment Question:**

**Does your organization issue or allow mobile devices (smartphones, tablets) that store organizational data?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 2
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Storage System/Device | Data Classification | Encryption Status | Encryption Type | Algorithm & Key Size | Key Management Method | Key Rotation Enabled | Status | Evidence Location | Gap Description | Remediation Needed |
|----------------------|--------------------|--------------------|-----------------|---------------------|----------------------|---------------------|---------|-------------------|-----------------|-------------------|
| Example: iPhone 13, Samsung Galaxy S23, iPad Pro | | | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Total mobile devices:** _________
- **Platform distribution:** iOS: _____ / Android: _____ / Other: _____
- **MDM solution in use:** _________
- **MDM enforces encryption:** [ ] Yes [ ] No

---

**MOBILE DEVICE ENCRYPTION CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| iOS devices: FileVault/built-in encryption enabled | [ ] Yes [ ] No [ ] N/A | iOS encrypts automatically when passcode set |
| Android devices: Full device encryption enabled | [ ] Yes [ ] No [ ] N/A | Verify via MDM compliance report |
| MDM policy enforces encryption | [ ] Yes [ ] No [ ] N/A | Policy blocks non-compliant devices |
| Encryption status verified via MDM reporting | [ ] Yes [ ] No [ ] N/A | Quarterly verification minimum |
| PIN/password/biometric required for device unlock | [ ] Yes [ ] No [ ] N/A | Minimum 6 digits/characters |
| Remote wipe capability configured | [ ] Yes [ ] No [ ] N/A | Test annually |
| Recovery keys escrowed to organizational MDM system | [ ] Yes [ ] No [ ] N/A | Business-owned devices only |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Limited data access (email only, no files)
  - [ ] Enhanced monitoring via MDM
  - [ ] Frequent remote wipe tests
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________
- **Budget required:** [ ] Yes [ ] No  Amount: _________

---

# Laptops & Workstations

**Policy Requirement:** All laptops and workstations containing sensitive data (Confidential or Restricted) MUST implement full disk encryption 

**Assessment Question:**

**Does your organization have laptops or workstations that store organizational data?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 3
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Storage System/Device | Data Classification | Encryption Status | Encryption Type | Algorithm & Key Size | Key Management Method | Key Rotation Enabled | Status | Evidence Location | Gap Description | Remediation Needed |
|----------------------|--------------------|--------------------|-----------------|---------------------|----------------------|---------------------|---------|-------------------|-----------------|-------------------|
| Example: Dell Latitude (Windows), MacBook Pro (macOS), ThinkPad (Linux) | | | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Total laptops:** _________
- **Total workstations:** _________
- **Platform distribution:** Windows: _____ / macOS: _____ / Linux: _____
- **Encryption solution(s):** _________

---

**LAPTOP & WORKSTATION ENCRYPTION CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| BitLocker enabled (Windows) with TPM 2.0 or TPM 1.2 minimum | [ ] Yes [ ] No [ ] N/A | Check: `manage-bde -status` |
| FileVault enabled (macOS) | [ ] Yes [ ] No [ ] N/A | Check: `fdesetup status` |
| LUKS enabled (Linux) | [ ] Yes [ ] No [ ] N/A | Check: `cryptsetup status` |
| Recovery keys escrowed to Active Directory, Entra ID, or organizational KMS | [ ] Yes [ ] No [ ] N/A | Critical for business continuity |
| AES-256-XTS encryption algorithm | [ ] Yes [ ] No [ ] N/A | Standard for disk encryption |
| Desktop workstations: Risk assessment documented if not encrypted | [ ] Yes [ ] No [ ] N/A | Exception requires CISO approval |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Workstations in physically secured facility (locked room)
  - [ ] No Confidential/Restricted data on unencrypted devices
  - [ ] Network-based data access only (no local storage)
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# Servers

**Policy Requirement:** Servers storing Confidential or Restricted data MUST implement disk/volume encryption 

**Assessment Question:**

**Does your organization have physical or virtual servers that store organizational data?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 4
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Storage System/Device | Data Classification | Encryption Status | Encryption Type | Algorithm & Key Size | Key Management Method | Key Rotation Enabled | Status | Evidence Location | Gap Description | Remediation Needed |
|----------------------|--------------------|--------------------|-----------------|---------------------|----------------------|---------------------|---------|-------------------|-----------------|-------------------|
| Example: Windows Server 2022, RHEL 8, VMware VM, Hyper-V VM | | | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Total physical servers:** _________
- **Total virtual machines:** _________
- **Virtualization platform:** [ ] VMware [ ] Hyper-V [ ] KVM [ ] Other: _____
- **Encryption approach:** [ ] Guest OS encryption [ ] Hypervisor-level encryption [ ] Both

---

**SERVER ENCRYPTION CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| Physical servers: Disk encryption enabled for data volumes | [ ] Yes [ ] No [ ] N/A | BitLocker, LUKS, hardware encryption |
| Virtual machines: VM encryption or guest OS encryption enabled | [ ] Yes [ ] No [ ] N/A | vSphere Encryption, Hyper-V encryption, or in-guest |
| Linux servers: LUKS encryption for data volumes | [ ] Yes [ ] No [ ] N/A | Check: `cryptsetup status /dev/mapper/*` |
| Windows Servers: BitLocker enabled for data volumes | [ ] Yes [ ] No [ ] N/A | Check: `manage-bde -status` |
| Encryption keys managed via KMS or HSM | [ ] Yes [ ] No [ ] N/A | Centralized key management required |
| Encryption applied at appropriate layer (hypervisor vs guest) | [ ] Yes [ ] No [ ] N/A | Document decision rationale |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Servers in highly secured data center (badge + biometric)
  - [ ] Application-level encryption for sensitive data
  - [ ] Network segmentation isolates servers
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# Databases

**Policy Requirement:** Databases containing Confidential or Restricted data MUST implement Transparent Data Encryption (TDE) or equivalent 

**Assessment Question:**

**Does your organization have databases that store organizational data?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 5
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Storage System/Device | Data Classification | Encryption Status | Encryption Type | Algorithm & Key Size | Key Management Method | Key Rotation Enabled | Status | Evidence Location | Gap Description | Remediation Needed |
|----------------------|--------------------|--------------------|-----------------|---------------------|----------------------|---------------------|---------|-------------------|-----------------|-------------------|
| Example: SQL Server 2019, Oracle 19c, PostgreSQL 14, MySQL 8.0, MongoDB 6.0 | | | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Total databases:** _________
- **Database platforms:** [ ] SQL Server [ ] Oracle [ ] PostgreSQL [ ] MySQL [ ] MongoDB [ ] Other: _____
- **TDE implementation:** [ ] All databases [ ] Confidential/Restricted only [ ] None

---

**DATABASE ENCRYPTION CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| SQL Server: TDE enabled for Confidential/Restricted databases | [ ] Yes [ ] No [ ] N/A | Query: `SELECT name, is_encrypted FROM sys.databases` |
| Oracle: TDE or tablespace encryption enabled | [ ] Yes [ ] No [ ] N/A | Check: `SELECT * FROM v$encrypted_tablespaces` |
| PostgreSQL: pgcrypto or disk-level encryption | [ ] Yes [ ] No [ ] N/A | pgcrypto extension or LUKS on data volume |
| MySQL/MariaDB: InnoDB encryption enabled | [ ] Yes [ ] No [ ] N/A | Check: `SHOW VARIABLES LIKE '%innodb_encrypt%'` |
| MongoDB: Encryption at rest enabled | [ ] Yes [ ] No [ ] N/A | Check: `db.adminCommand({getParameter: 1, encryptionCipherMode: 1})` |
| Database encryption keys managed via KMS or HSM | [ ] Yes [ ] No [ ] N/A | Not stored in database itself |
| Column-level encryption for highly sensitive fields (if applicable) | [ ] Yes [ ] No [ ] N/A | Credit cards, SSNs, passwords |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Disk-level encryption (server LUKS/BitLocker)
  - [ ] Application-level field encryption
  - [ ] Database contains only Public/Internal data
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

**END OF PART II, FILE 1 of 2**

**CONTINUATION:** Part II, File 2 contains:

- Section 5: Cloud Storage
- Section 6: Backups
- Section 7: Removable Media
- Section 8: Overall Storage Summary
- Section 9: Evidence Register
- Section 10: Approval and Sign-Off
- Appendix: Technical Notes for Workbook Developers

# Cloud Storage

**Policy Requirement:** Cloud storage containing Confidential or Restricted data MUST use encryption with customer-managed keys (CMEK) preferred over cloud-service-managed keys (CSEK) 

**Assessment Question:**

**Does your organization use cloud storage services (AWS S3, Azure Blob, GCP Cloud Storage, etc.)?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 6
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Storage System/Device | Data Classification | Encryption Status | Encryption Type | Algorithm & Key Size | Key Management Method | Key Rotation Enabled | Status | Evidence Location | Gap Description | Remediation Needed |
|----------------------|--------------------|--------------------|-----------------|---------------------|----------------------|---------------------|---------|-------------------|-----------------|-------------------|
| Example: S3 bucket, Azure Blob container, GCS bucket | | | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Cloud provider(s):** [ ] AWS [ ] Azure [ ] GCP [ ] Other: _____
- **Total storage buckets/containers:** _________
- **Encryption method:** [ ] CMEK (Customer-Managed) [ ] CSEK (Cloud-Managed) [ ] Default
- **KMS in use:** _________

---

**CLOUD STORAGE ENCRYPTION CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| All buckets/containers have encryption enabled | [ ] Yes [ ] No [ ] N/A | Verify per bucket/container |
| CMEK (Customer-Managed Encryption Keys) used for Confidential/Restricted data | [ ] Yes [ ] No [ ] N/A | AWS KMS, Azure Key Vault, GCP KMS |
| CSEK (Cloud-Service-Managed Keys) acceptable for Internal data only | [ ] Yes [ ] No [ ] N/A | Less control over keys |
| KMS key rotation enabled (annual minimum) | [ ] Yes [ ] No [ ] N/A | Automatic rotation preferred |
| Cloud provider encryption audit logs enabled | [ ] Yes [ ] No [ ] N/A | CloudTrail, Azure Monitor, GCP Audit Logs |
| Encryption-at-rest verified for all storage services | [ ] Yes [ ] No [ ] N/A | S3, EBS, RDS, etc. |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Cloud provider native encryption (CSEK) with documented acceptance
  - [ ] Application-level encryption before cloud upload
  - [ ] Cloud storage contains only Public/Internal data
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# Backups

**Policy Requirement:** Backups containing Confidential or Restricted data MUST be encrypted using AES-256 minimum 

**Assessment Question:**

**Does your organization perform backups of organizational data?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 7
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Storage System/Device | Data Classification | Encryption Status | Encryption Type | Algorithm & Key Size | Key Management Method | Key Rotation Enabled | Status | Evidence Location | Gap Description | Remediation Needed |
|----------------------|--------------------|--------------------|-----------------|---------------------|----------------------|---------------------|---------|-------------------|-----------------|-------------------|
| Example: Veeam backups, Commvault, tape backups, cloud backups | | | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Backup solution:** _________
- **Backup types:** [ ] Full [ ] Incremental [ ] Differential [ ] Continuous
- **Backup locations:** [ ] On-site [ ] Off-site [ ] Cloud [ ] Tape
- **Encryption enabled:** [ ] All backups [ ] Off-site only [ ] None

---

**BACKUP ENCRYPTION CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| Backup encryption enabled in backup software | [ ] Yes [ ] No [ ] N/A | Check backup software configuration |
| AES-256 encryption algorithm | [ ] Yes [ ] No [ ] N/A | Minimum requirement |
| Backup encryption keys stored separately from backup data | [ ] Yes [ ] No [ ] N/A | Protect against ransomware |
| Backup restore tested with encrypted backups (annually) | [ ] Yes [ ] No [ ] N/A | Verify encryption doesn't prevent restore |
| Off-site/cloud backups encrypted | [ ] Yes [ ] No [ ] N/A | Critical for data leaving premises |
| Tape backups encrypted (if applicable) | [ ] Yes [ ] No [ ] N/A | Hardware or software encryption |
| Backup encryption keys documented and accessible for recovery | [ ] Yes [ ] No [ ] N/A | DR plan includes key recovery |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Backups stored in highly secure facility (limited access)
  - [ ] Source data encrypted (database TDE, disk encryption)
  - [ ] Backups contain only Public/Internal data
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# Removable Media

**Policy Requirement:** Removable media (USB drives, external disks) containing organizational data MUST be encrypted 

**Assessment Question:**

**Does your organization allow use of removable media (USB drives, external disks) for organizational data?**

- [ ] Yes → Complete assessment below
- [ ] No → Skip to Section 8
- [ ] Not Applicable

---

**If Yes, complete the assessment:**

| Storage System/Device | Data Classification | Encryption Status | Encryption Type | Algorithm & Key Size | Key Management Method | Key Rotation Enabled | Status | Evidence Location | Gap Description | Remediation Needed |
|----------------------|--------------------|--------------------|-----------------|---------------------|----------------------|---------------------|---------|-------------------|-----------------|-------------------|
| Example: USB flash drives, external hard drives, SD cards | | | | | | | [ ] ✅ [ ] ⚠️ [ ] ❌ [ ] N/A | | | [ ] Yes [ ] No |

**Additional Details:**

- **Removable media policy:** [ ] Allowed with encryption [ ] Corporate-issued only [ ] Prohibited [ ] No formal policy
- **Encryption solution:** [ ] BitLocker To Go [ ] VeraCrypt [ ] Hardware-encrypted devices [ ] Other: _____
- **Device control/DLP:** [ ] Blocks unencrypted USB [ ] Allows all USB [ ] Not configured

---

**REMOVABLE MEDIA ENCRYPTION CHECKLIST:**

| Requirement | Status | Notes |
|-------------|--------|-------|
| USB encryption policy documented and communicated | [ ] Yes [ ] No [ ] N/A | Users aware of encryption requirement |
| BitLocker To Go or equivalent encryption required | [ ] Yes [ ] No [ ] N/A | Windows native solution |
| Device control/DLP blocks unencrypted USB drives | [ ] Yes [ ] No [ ] N/A | Technical enforcement preferred |
| Corporate-issued encrypted USB devices available | [ ] Yes [ ] No [ ] N/A | IronKey, encrypted drives |
| Unencrypted USB drives prohibited for Confidential/Restricted data | [ ] Yes [ ] No [ ] N/A | Policy enforcement |
| User training on USB encryption requirement | [ ] Yes [ ] No [ ] N/A | Annual security awareness training |

---

**If Status = ⚠️ or ❌, complete Exception/Deviation Documentation:**

**Exception/Deviation Details:**

- [ ] Formal exception request submitted (Exception ID: __________)
- [ ] Risk acceptance documented (Risk ID: __________)
- [ ] Compensating controls implemented:
  - [ ] Removable media prohibited (policy and device control)
  - [ ] Cloud file sharing used instead of USB drives
  - [ ] No Confidential/Restricted data on removable media
  - [ ] Other: _______________________________

**Remediation Plan:**

- **Remediation actions required:** _________________________________
- **Responsible person:** _________________________________
- **Target completion date:** _________________________________

---

# Overall Storage Summary

## Compliance Summary

**Total Assessment Areas:** _______

| Storage Category | Status | Percentage |
|-----------------|--------|------------|
| Mobile Devices | | |
| Laptops & Workstations | | |
| Servers | | |
| Databases | | |
| Cloud Storage | | |
| Backups | | |
| Removable Media | | |
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
  - ❌ Unencrypted mobile devices with Confidential/Restricted data
  - ❌ Laptops without encryption and no recovery key escrow
  - ❌ Databases with TDE requirement but TDE disabled
  - ❌ Cloud storage without CMEK for Confidential/Restricted data
  - ❌ Unencrypted backups leaving premises
  - ❌ No removable media encryption policy or enforcement

## Top Remediation Priorities

| Priority | Gap Description | Target Date | Responsible Person |
|----------|-----------------|-------------|-------------------|
| **High** | | | |
| **High** | | | |
| **Medium** | | | |

**Priority Definitions:**

- **High:** Data exposure risk, compliance violation, or operational failure imminent
- **Medium:** Compliance gap with planned remediation, low immediate risk
- **Low:** Best practice improvement, no compliance impact

---

# Evidence Register

**List all evidence files/documents referenced in this assessment:**

| Evidence ID | Description | Location | Date Collected |
|-------------|-------------|----------|----------------|
| EV-1-001 | MDM compliance report (all mobile devices) | /evidence/a824_2/ | DD.MM.YYYY |
| EV-2-001 | BitLocker status report (all Windows devices) | /evidence/a824_2/ | DD.MM.YYYY |
| | | | |
| | | | |

**Evidence Naming Convention:**
```
EV-[Section]-[System]-[Date]-[Type].[ext]
```

**Examples:**

- `EV-1-MDM-Compliance-20260115.pdf`
- `EV-2-BitLocker-Status-20260115.xlsx`
- `EV-4-MSSQL-TDE-Status-20260115.txt`
- `EV-5-S3-Encryption-Config-20260115.png`

**Evidence Types:**

- MDM compliance reports
- Encryption configuration screenshots
- Database query results (TDE status)
- Cloud console screenshots
- Backup configuration exports
- Key management documentation
- Encryption algorithm verification
- Recovery key escrow verification

**Evidence Storage:**

- **Location:** [Organization's evidence repository path]
- **Retention:** Audit cycle + 1 year minimum
- **Access Control:** Restricted to security team and auditors
- **Sensitivity:** Sanitize encryption keys and credentials

---

# Approval and Sign-Off

## Assessment Summary

**Assessment Document:** ISMS-IMP-A.8.24.2 - Data Storage Assessment  
**Assessment Period:** From __________ To __________  
**Overall Compliance Rate:** _______ % (from Summary Dashboard Section 8.1)  
**Assessment Status:** [ ] Draft [ ] Final [ ] Requires remediation [ ] Re-assessment required

**Key Findings:**

- Storage systems assessed: _______
- Encrypted systems: _______
- Systems requiring remediation: _______
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
I certify that this assessment was completed with due diligence, all encryption status information is accurate to the best of my knowledge, and all evidence has been collected and verified.

---

## Reviewed By (Information Security Officer)

**Name:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Review Comments:**
_________________________________________________________________
_________________________________________________________________
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

- [ ] Approved - Encryption posture acceptable, remediation plans approved
- [ ] Approved with conditions - Remediation must be completed by: _______
- [ ] Rejected - Re-assessment required due to: _______

**Risk Acceptance:**
For any documented exceptions/deviations, I accept the residual risk based on:

- Documented risk assessment
- Approved compensating controls
- Business justification
- Compliance with exception approval process (ISMS-POL-A.8.24-S5.B)

**Budget Approval:**
Remediation budget requirement: _______

- [ ] Approved
- [ ] Requires further justification
- [ ] Deferred to next budget cycle

---

## Next Review Date

**Next Scheduled Assessment:** _______________________

**Review Cycle:** Quarterly (every 3 months) or upon:

- Major infrastructure changes (new servers, cloud migration)
- Security incidents involving unencrypted device
- Policy updates (encryption algorithm changes)
- Regulatory changes
- Failed audit findings
- New storage systems deployed

**Interim Monitoring:**

- MDM compliance monitoring: Continuous (automated alerts)
- Endpoint encryption status: Quarterly spot-checks
- Database TDE status: Quarterly verification
- Cloud storage encryption: Monthly reviews
- Backup encryption: Test restores quarterly
- Remediation progress: Tracked monthly

---

## Distribution List

This assessment shall be distributed to:

- [ ] Chief Information Security Officer (CISO)
- [ ] Information Security Officer (ISO)
- [ ] System Administrators (endpoint, server, database teams)
- [ ] Storage team
- [ ] Cloud team
- [ ] Compliance team
- [ ] Internal Audit
- [ ] IT Management
- [ ] Other: _______________________

**Storage Location:**

- **ISMS Repository:** `ISMS/Controls/A.8.24_Use_of_Cryptography/Assessments/`
- **Filename:** `ISMS-IMP-A.8.24.2_Data_Storage_[DATE]_APPROVED.xlsx`

---

# APPENDIX: Technical Notes for Workbook Developers

## A.1 Excel Workbook Structure

**Sheet Names (11 sheets total):**
1. Instructions & Legend
2. 1. Mobile Devices
3. 2. Laptops & Workstations
4. 3. Servers
5. 4. Databases
6. 5. Cloud Storage
7. 6. Backups
8. 7. Removable Media
9. Summary Dashboard
10. Evidence Register
11. Approval Sign-Off

## A.2 Data Validation Rules

**Status Dropdown:**

- Formula: `"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"`
- Applied to: Column H (Status) in all assessment sheets
- Allow blank: No

**Data Classification Dropdown:**

- Formula: `"Public,Internal,Confidential,Restricted,N/A"`
- Applied to: Column B in all assessment sheets
- Allow blank: No

**Encryption Status Dropdown:**

- Formula: `"Encrypted,Not Encrypted,Partially Encrypted"`
- Applied to: Column C in all assessment sheets
- Allow blank: No

**Encryption Type Dropdown:**

- Formula: `"Full Disk,File-level,Database TDE,Volume,Container,Application-level,Hardware-based,N/A"`
- Applied to: Column D in all assessment sheets
- Allow blank: No

**Key Management Method Dropdown:**

- Formula: `"HSM,Cloud KMS,TPM,Software-based,Manual,Vendor-managed,N/A"`
- Applied to: Column F in all assessment sheets
- Allow blank: No

**Key Rotation Enabled Dropdown:**

- Formula: `"Yes,No,N/A"`
- Applied to: Column G in all assessment sheets
- Allow blank: No

**Remediation Needed Dropdown:**

- Formula: `"Yes,No"`
- Applied to: Column K in all assessment sheets
- Allow blank: No

**Budget Required Dropdown:**

- Formula: `"Yes,No,Unknown"`
- Applied to: Column Q in all assessment sheets
- Allow blank: No

**Response Dropdown (Assessment Question):**

- Formula: `"Yes,No,Not Applicable"`
- Applied to: Response field for each section's assessment question
- Allow blank: No

**Checklist Items:**

- Formula: `"Yes,No,N/A"`
- Applied to: All compliance checklist Status columns
- Allow blank: No

## A.3 Conditional Formatting

**Status Column (Column H):**

- ✅ Compliant: Green fill (RGB: 198, 239, 206)
- ⚠️ Partial: Yellow fill (RGB: 255, 235, 156)
- ❌ Non-Compliant: Red fill (RGB: 255, 199, 206)
- N/A: No special formatting

**Overall Compliance Percentage (Summary Dashboard):**

- ≥90%: Green fill
- 80-89%: Yellow fill
- <80%: Red fill

**Data Classification (Column B) - Risk-based coloring:**

- Restricted: Red fill (RGB: 255, 199, 206)
- Confidential: Yellow fill (RGB: 255, 235, 156)
- Internal: No fill
- Public: No fill

## A.4 Cell Protection

**Protected Cells (Formula/Static):**

- Column headers
- Instructions text
- Compliance checklist labels
- Status legend
- Summary Dashboard calculations
- Evidence Register ID auto-generation

**Unprotected Cells (User Input):**

- Assessment data entry tables (yellow fill, columns A-Q rows 8-20)
- Compliance checklist status columns
- Additional Details fields
- Exception/Deviation documentation fields
- Evidence Register descriptions
- Approval Sign-Off fields

**Sheet Protection:**

- Password: [Set during workbook generation]
- Allow: Format cells, Insert rows, Sort, Filter
- Disallow: Delete rows, Modify formulas, Unprotect sheet

## A.5 Summary Dashboard Formulas

**Compliance Percentage by Category:**
```excel
=COUNTIF('1. Mobile Devices'!H:H,"✅ Compliant")/COUNTA('1. Mobile Devices'!H:H)*100
```

**Critical Gaps Count:**
```excel
=COUNTIF('1. Mobile Devices'!H:H,"❌ Non-Compliant")+
 COUNTIF('2. Laptops & Workstations'!H:H,"❌ Non-Compliant")+
 COUNTIF('3. Servers'!H:H,"❌ Non-Compliant")+
 COUNTIF('4. Databases'!H:H,"❌ Non-Compliant")+
 COUNTIF('5. Cloud Storage'!H:H,"❌ Non-Compliant")+
 COUNTIF('6. Backups'!H:H,"❌ Non-Compliant")+
 COUNTIF('7. Removable Media'!H:H,"❌ Non-Compliant")
```

**Overall Compliance Rate:**
```excel
=(Total Compliant Items / Total Applicable Items) * 100
```
Where Total Applicable Items excludes N/A items.

## A.6 Evidence Register Auto-Numbering

**Evidence ID Format:**
```excel
="EV-"&TEXT(ROW()-4,"000")
```

**Date Format:**
```excel
=TEXT(TODAY(),"DD.MM.YYYY")
```

## A.7 Python Script Integration Points

**Workbook Generation Script:** `generate_a824_2_data_storage_assessment.py`

**Key Functions:**

- `create_workbook()`: Initialize workbook and sheets
- `setup_styles()`: Define cell styles, fonts, fills
- `get_storage_columns()`: Return standard column definitions (A-Q)
- `create_assessment_sheet()`: Generic sheet generator with validation
- `create_checklist_section()`: Compliance checklist builder
- `create_summary_dashboard()`: Compliance calculations
- `create_evidence_register()`: Evidence tracking
- `create_approval_signoff()`: Approval workflow

**Customization Points (marked with `# CUSTOMIZE:` in script):**

- Sheet names (if organizational naming differs)
- Dropdown options (if additional statuses needed)
- Data validation rules (if custom compliance criteria)
- Conditional formatting thresholds (if different color coding)
- Checklist items (if organization-specific requirements)

**Quality Assurance Script:** `excel_sanity_check_a824_2.py`

- Validates sheet structure matches specification
- Checks data validation rules applied correctly
- Verifies conditional formatting ranges
- Tests formula accuracy
- Reports discrepancies between script and specification

## A.8 Version Control

**Workbook Versioning:**

- Filename format: `ISMS-IMP-A.8.24.2_Data_Storage_YYYYMMDD.xlsx`
- Version tracking in Instructions & Legend sheet
- Document Control section updated with each revision

**Change Log:**

- v1.0: Initial workbook structure
- v2.0: Added comprehensive User Completion Guide, enhanced checklists, improved evidence guidance

**Backward Compatibility:**

- v2.0 workbooks can be opened in Excel 2016+
- v1.0 workbooks should be migrated to v2.0 for updated guidance
- Migration script available: `normalize_assessment_files_a824.py`

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Document Assembly Instructions

**To create the complete ISMS-IMP-A.8.24.2 v1.0 document:**

1. **Document Control** (from PART I file, lines 1-30)
2. **PART I: USER COMPLETION GUIDE** (from PART I file, lines 31-~440)
3. **PART II: TECHNICAL SPECIFICATION - File 1** (this file, all content)
4. **PART II: TECHNICAL SPECIFICATION - File 2** (next file, all content)

**Final Document Structure:**
```
ISMS-IMP-A.8.24.2 - Data Storage Assessment v1.0

├── Document Control (Metadata, Version History)
│
├── PART I: USER COMPLETION GUIDE (~440 lines)
│   ├── 1. Assessment Overview
│   ├── 2. Prerequisites
│   ├── 3. Assessment Workflow
│   ├── 4. Question-by-Question Guidance (Sections 1-2 detailed, 3-7 outlined)
│   ├── 5. Evidence Collection
│   ├── 6. Common Pitfalls (10 mistakes)
│   ├── 7. Quality Checklist (50+ items)
│   └── 8. Review & Approval
│
└── PART II: TECHNICAL SPECIFICATION (~750 lines)
    ├── Instructions
    ├── Common Column Structure
    ├── 1. Mobile Devices
    ├── 2. Laptops & Workstations
    ├── 3. Servers
    ├── 4. Databases
    ├── 5. Cloud Storage
    ├── 6. Backups
    ├── 7. Removable Media
    ├── 8. Overall Summary
    ├── 9. Evidence Register
    ├── 10. Approval and Sign-Off
    └── Appendix: Technical Notes for Developers
```

**Quality Checks Before Finalizing:**

- [ ] All merge instructions removed
- [ ] Document Control version shows 2.0
- [ ] Version History documents v1.0 → v2.0 changes
- [ ] All dates in DD.MM.YYYY format
- [ ] Cross-references accurate (section numbers, policy references)
- [ ] No placeholder text remains
- [ ] Technical appendix matches Python script version

---

**END OF SPECIFICATION**

---

*"I have not trodden through a conventional university course, but I am striking out a new path for myself."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-06 -->
