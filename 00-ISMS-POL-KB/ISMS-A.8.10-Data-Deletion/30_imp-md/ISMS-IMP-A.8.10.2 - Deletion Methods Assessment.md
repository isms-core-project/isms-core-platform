# ISMS-IMP-A.8.10.2 - Deletion Methods Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.10.2  
**Assessment Area:** Deletion Methods by Media Type  
**Related Policy:** ISMS-POL-A.8.10-S2.2 (Deletion Methods by Media Type)  
**Purpose:** Assess deletion method effectiveness across different storage media types and validate technical implementation

**Key Principle:** This assessment is **vendor-neutral**. Organizations document THEIR specific deletion tools, methods, and validation procedures. The workbook provides technical structure; customers provide their implementation reality.

---

## Assessment Context

### What This Assessment Covers

This assessment evaluates the organization's approach to:
1. **Physical Media Deletion** - HDD, SSD, tape, removable media, paper destruction
2. **Cloud Storage Deletion** - IaaS, PaaS, SaaS provider deletion capabilities
3. **Database & Application Deletion** - Logical deletion, purging, crypto-erasure
4. **Mobile & Endpoint Deletion** - BYOD, MDM, factory reset procedures
5. **Deletion Method Validation** - Testing, verification, forensic recovery attempts

### What This Assessment Does NOT Cover

- **WHEN** data should be deleted (see ISMS-IMP-A.8.10.1 - Retention Triggers)
- **Third-party coordination** for deletion (see ISMS-IMP-A.8.10.3 - Third-Party Deletion)
- **Evidence collection** post-deletion (see ISMS-IMP-A.8.10.4 - Verification & Evidence)

### Related ISMS Documents

- **ISMS-POL-A.8.10** - Information Deletion Policy (Master)
- **ISMS-POL-A.8.10-S2.2** - Deletion Methods by Media Type Requirements
- **ISMS-POL-A.8.10-S5.A** - Annex A: Deletion Methods Matrix
- **NIST SP 800-88 Rev. 1** - Guidelines for Media Sanitization (reference)
- **ISMS-REF-A.5.23** - Cloud Service Provider Registry (for cloud deletion context)

---

## Workbook Structure

This workbook contains **9 sheets** organized as follows:

### Core Sheets
1. **Instructions & Legend** - How to use this workbook, NIST framework, definitions
2. **2. Physical Media Deletion** - HDD, SSD, tape, removable media, paper
3. **3. Cloud Storage Deletion** - AWS, Azure, GCP, other cloud providers
4. **4. Database & Application Deletion** - Databases, applications, crypto-shredding
5. **5. Mobile & Endpoint Deletion** - Laptops, smartphones, tablets, BYOD
6. **6. Deletion Tool Validation** - Tool testing, forensic verification, effectiveness

### Summary & Administration
7. **Summary Dashboard** - Compliance overview, method effectiveness, critical gaps
8. **Evidence Register** - Links to supporting documentation (100 rows)
9. **Approval Sign-Off** - Three-level approval workflow

---

## Assessment Sheets - Column Definitions

### Standard Column Layout (Columns A-Q, 17 columns)

These columns appear in **Sheets 2-6** with minor variations:

| Column | Header | Width | Type | Validation Options | Purpose |
|--------|--------|-------|------|-------------------|---------|
| A | Media Type / System Name | 30 | Text | Free text | Primary identifier |
| B | Data Classification | 22 | Dropdown | Public, Internal, Confidential, Restricted | Sensitivity level |
| C | Owner / Responsible Party | 18 | Text | Free text | System/media owner |
| D | Deletion Method Used | 25 | Dropdown | See method options below | How data is deleted |
| E | Tool/Vendor Used | 20 | Text | Free text | Customer fills in their tools |
| F | Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Traffic light status |
| G | Implementation Date | 12 | Date | Date picker | When method deployed |
| H | Last Effectiveness Test | 12 | Date | Date picker | Last validation test |
| I | Next Test Date | 12 | Date | Date picker | Scheduled validation |
| J | Gap Identified | 25 | Text | Free text | If not compliant |
| K | Remediation Plan | 25 | Text | Free text | How to fix gap |
| L | Target Completion | 12 | Date | Date picker | Remediation deadline |
| M | Risk Level | 12 | Dropdown | Critical, High, Medium, Low | If gap exists |
| N | Evidence Reference | 20 | Text | Free text | Link to Evidence Register |
| O | Notes / Comments | 25 | Text | Free text | Additional context |
| P | Remediation Owner | 18 | Text | Free text | Who will fix |
| Q | Budget Required | 15 | Dropdown | Yes, No, Unknown | Resource planning |

### Extended Columns (R-U) - Sheet-Specific

**Sheet 2 (Physical Media Deletion):**
- R: **NIST SP 800-88 Method** (Dropdown: Clear, Purge, Destroy, N/A)
- S: **Verification Method** (Dropdown: Software Verification, Visual Inspection, Certificate of Destruction, Forensic Test, None)
- T: **Last Forensic Test Result** (Dropdown: Pass (No Recovery), Fail (Partial Recovery), Fail (Full Recovery), Not Tested)
- U: **Media Disposal Method** (Dropdown: Reuse, Recycle, Shred, Incinerate, Degauss, Other)

**Sheet 3 (Cloud Storage Deletion):**
- R: **Provider Tier** (Dropdown: Tier 1-10 from ISMS-REF-A.5.23)
- S: **Deletion API Available** (Dropdown: Yes - Automated, Yes - Manual, No, Unknown)
- T: **Snapshot/Backup Deletion** (Dropdown: Automatic, Manual, Unknown, N/A)
- U: **Multi-Region Deletion Verified** (Dropdown: Yes, No, N/A, Unknown)

**Sheet 4 (Database & Application Deletion):**
- R: **Deletion Type** (Dropdown: Logical Delete, Hard Delete, Purge, Truncate, Crypto-Shred, Archive then Delete)
- S: **Referential Integrity Handled** (Dropdown: Yes - Cascading, Yes - Manual, No, N/A)
- T: **Backup Purging** (Dropdown: Automatic, Manual, Not Implemented, N/A)
- U: **Crypto-Erasure Key Management** (Dropdown: Yes - Automated, Yes - Manual, No, N/A)

**Sheet 5 (Mobile & Endpoint Deletion):**
- R: **Device Type** (Dropdown: Corporate Laptop, Corporate Mobile, BYOD Laptop, BYOD Mobile, Tablet, Other)
- S: **MDM Solution Used** (Text: customer fills in their MDM)
- T: **Remote Wipe Capability** (Dropdown: Yes - Tested, Yes - Untested, No, N/A)
- U: **Full Disk Encryption** (Dropdown: Yes - BitLocker, Yes - FileVault, Yes - LUKS, Yes - Other, No)

**Sheet 6 (Deletion Tool Validation):**
- R: **Test Frequency** (Dropdown: Monthly, Quarterly, Semi-Annual, Annual, Ad-hoc, Never)
- S: **Forensic Tool Used** (Text: e.g., EnCase, FTK, Autopsy, Custom)
- T: **Pass Rate (Last 12 Months)** (Text: e.g., "12/12 = 100%")
- U: **Independent Testing** (Dropdown: Yes - External, Yes - Internal, No, Planned)

---

## Validation Options - Dropdowns

### Deletion Method Options (Column D)

**Physical Media Methods:**
- Overwrite (1-pass)
- Overwrite (3-pass)
- Overwrite (7-pass DoD 5220.22-M)
- Secure Erase (ATA/NVMe)
- Cryptographic Erasure
- Degaussing
- Physical Destruction (Shred)
- Physical Destruction (Incinerate)
- Physical Destruction (Crush/Pulverize)
- Other (specify in notes)

**Cloud/Digital Methods:**
- Cloud Provider API Delete
- Cloud Lifecycle Policy
- Manual Console Delete
- Crypto-Shred (Key Deletion)
- Account Closure
- Other (specify in notes)

**Database/Application Methods:**
- Logical DELETE (soft delete)
- Hard DELETE (permanent)
- TRUNCATE TABLE
- DROP TABLE/DATABASE
- Purge/Vacuum
- Crypto-Shred
- Archive then Delete
- Other (specify in notes)

### NIST SP 800-88 Method Options (Column R - Sheet 2)
- Clear (logical techniques, prevents simple recovery)
- Purge (physical/crypto techniques, prevents lab recovery)
- Destroy (physical destruction, prevents any recovery)
- N/A (not applicable to this media)

### Data Classification Options (Column B)
- Public
- Internal
- Confidential
- Restricted

### Status Options (Column F)
- ✅ Compliant
- ⚠️ Partial
- ❌ Non-Compliant
- N/A

### Risk Level Options (Column M)
- Critical
- High
- Medium
- Low

### Budget Required (Column Q)
- Yes
- No
- Unknown

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Legend

**Purpose:** Provide complete usage instructions, NIST framework overview, and definitions

**Content Structure:**

**Section 1: Document Information (Rows 1-8)**
- Workbook title and version
- Assessment date and assessor name
- Organization name
- Review period covered
- Related policy references

**Section 2: How to Use This Workbook (Rows 10-25)**
- Step-by-step instructions for completing assessment
- Navigation guidance between sheets
- How to map media types to appropriate deletion methods
- NIST SP 800-88 framework explanation
- How to link to Evidence Register
- Approval workflow instructions

**Section 3: NIST SP 800-88 Framework Overview (Rows 27-45)**

**Clear:**
- **Definition:** Logical techniques applied to sanitization to protect against simple non-invasive data recovery
- **Use Case:** Media will be reused within organization for same or lower classification
- **Examples:** Overwrite (1-3 pass), block erase, cryptographic erase (key deletion)
- **Protection Level:** Prevents keyboard recovery, software file recovery tools

**Purge:**
- **Definition:** Physical or logical techniques that render target data recovery infeasible using state-of-the-art laboratory techniques
- **Use Case:** Media leaving organizational control or being repurposed to higher classification
- **Examples:** Overwrite (cryptographic-strength pattern verification), block erase (all addressable locations), secure erase, degaussing, cryptographic erasure
- **Protection Level:** Prevents laboratory recovery attempts

**Destroy:**
- **Definition:** Physical destruction of media to render it unusable and prevent any data recovery
- **Use Case:** Media contains highly sensitive data or is end-of-life
- **Examples:** Shredding, disintegration, pulverization, incineration, melting
- **Protection Level:** Absolute - media is physically destroyed

**Section 4: Color Coding Legend (Rows 47-55)**
| Color | Meaning | Usage |
|-------|---------|-------|
| Blue header | Column headers | Do not edit |
| Yellow | Data entry cells | Complete these fields |
| Green | Compliant status | Method validated and effective |
| Orange | Partial compliance | Method implemented but not validated |
| Red | Non-compliant | Ineffective or missing method |
| Gray | Reference information | Read-only guidance |
| White | Optional fields | Complete if relevant |

**Section 5: Key Definitions (Rows 57-75)**
- **Deletion Method:** Technical approach to removing data from storage media
- **Clear (NIST):** Logical sanitization protecting against simple recovery
- **Purge (NIST):** Advanced sanitization protecting against laboratory recovery
- **Destroy (NIST):** Physical destruction of media
- **Overwrite:** Writing new data patterns over existing data
- **Secure Erase:** Built-in firmware command for SSDs/HDDs
- **Cryptographic Erasure (Crypto-Shred):** Deletion of encryption keys rendering data unreadable
- **Degaussing:** Using magnetic field to disrupt magnetic media
- **Forensic Verification:** Testing using professional data recovery tools
- **Certificate of Destruction:** Third-party documentation of physical destruction
- **Logical Delete:** Marking data as deleted without immediate removal (soft delete)
- **Hard Delete:** Immediate permanent removal from database
- **Purge/Vacuum:** Database operation to reclaim space from deleted records

**Section 6: Media Type Quick Reference (Rows 77-90)**
| Media Type | Recommended NIST Method | Common Tools/Methods |
|------------|------------------------|---------------------|
| HDD (spinning disk) | Purge or Destroy | Overwrite (7-pass), Degauss, Shred |
| SSD (NAND flash) | Purge or Destroy | Secure Erase (ATA), Crypto-Erase, Shred |
| NVMe SSD | Purge or Destroy | NVMe Secure Erase, Crypto-Erase, Shred |
| Tape (magnetic) | Purge or Destroy | Degauss, Overwrite, Shred |
| USB/SD Cards | Purge or Destroy | Overwrite, Crypto-Erase, Shred |
| Optical Media (CD/DVD) | Destroy | Shred, Incinerate |
| Paper Documents | Destroy | Cross-cut shred, Pulp, Incinerate |
| Cloud Storage | Clear or Purge | API Delete, Crypto-Erase, Account Closure |
| Database Records | Clear | Hard DELETE, TRUNCATE, Purge/Vacuum |
| Mobile Devices | Purge or Destroy | Factory Reset + Encryption, MDM Wipe, Destroy |

**Section 7: Important Notes (Rows 92-105)**
- Vendor-neutral approach explanation
- SSD-specific considerations (wear leveling, over-provisioning)
- Cloud provider deletion limitations
- Backup deletion coordination requirement
- Link to related assessments (A.8.10.1, A.8.10.3, A.8.10.4)
- Annual testing requirement for deletion methods
- Escalation procedures for failed forensic tests

---

### Sheet 2: Physical Media Deletion

**Purpose:** Assess deletion methods for physical storage media (HDD, SSD, tape, removable media, paper)

**Assessment Question:**
*"Do we have effective deletion methods for all types of physical media, validated through testing, and aligned with NIST SP 800-88 guidance?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.2, Section 2.2.1 (Physical Media Deletion)

**Column Structure:** A-U (21 columns total)
- Columns A-Q: Standard base columns
- Column R: NIST SP 800-88 Method
- Column S: Verification Method
- Column T: Last Forensic Test Result
- Column U: Media Disposal Method

**Data Entry Rows:** 13 rows (yellow-highlighted, Rows 10-22)

**Compliance Checklist (Rows 25-45):**

1. All physical media types in use are identified and documented
2. Deletion methods are assigned per media type (not one-size-fits-all)
3. HDD deletion uses overwrite (≥3 pass) OR degaussing OR destruction
4. SSD deletion uses Secure Erase OR crypto-erasure OR destruction (NOT simple overwrite)
5. Magnetic tape deletion uses degaussing OR overwrite OR destruction
6. Removable media (USB, SD) deletion methods documented
7. Paper document destruction uses cross-cut shredding (minimum)
8. NIST SP 800-88 method classification assigned (Clear/Purge/Destroy)
9. Deletion tools are approved and maintained
10. Media disposal procedures documented (reuse, recycle, destroy)
11. Certificate of Destruction obtained for outsourced destruction
12. Forensic testing conducted at least annually
13. Failed forensic tests trigger immediate remediation
14. Data classification influences deletion method choice (Restricted → Destroy)
15. End-of-life media destruction procedures exist

**Reference Table 1: HDD vs SSD Deletion Differences (Rows 47-58)**
| Aspect | HDD (Spinning Disk) | SSD (NAND Flash) |
|--------|---------------------|------------------|
| Overwrite Effectiveness | ✅ Effective (7-pass DoD) | ❌ Ineffective (wear leveling) |
| Secure Erase Command | ✅ Effective (ATA Secure Erase) | ✅ Effective (ATA/NVMe Secure Erase) |
| Degaussing | ✅ Effective | ❌ Ineffective (not magnetic) |
| Cryptographic Erasure | ⚠️ Requires FDE | ✅ Highly Effective (built-in encryption) |
| Physical Destruction | ✅ Shred, crush, pulverize | ✅ Shred (flash chips destroyed) |
| NIST Recommendation | Purge: Overwrite or Degauss | Purge: Secure Erase or Crypto-Erase |
| Reuse After Sanitization | ✅ Possible | ✅ Possible (if Secure Erase used) |
| Over-Provisioning Concern | N/A | ⚠️ Hidden areas may retain data |
| Trim/GC Consideration | N/A | ⚠️ May leave data in unmapped blocks |

**Reference Table 2: Physical Destruction Methods (Rows 60-70)**
| Method | Media Types | Effectiveness | Cost | Vendor Options |
|--------|-------------|---------------|------|----------------|
| Cross-Cut Shredding | Paper, Optical, Cards | High | Low-Medium | Iron Mountain, Shred-it, In-house |
| Disintegration/Pulverization | HDD, SSD, Tape | Very High | Medium-High | Specialist vendors |
| Degaussing | HDD, Tape (magnetic only) | High (magnetic media) | Medium | Proton Data Security, VS Security |
| Incineration | All media types | Absolute | High | Specialist waste disposal |
| Melting | Optical media, some plastics | High | Medium | Specialist vendors |
| Crushing/Bending | HDD, Optical | Medium-High | Low-Medium | Manual or hydraulic press |

**Reference Table 3: Common Deletion Tools (Vendor Examples) (Rows 72-85)**
| Tool Category | Example Tools (Non-Exhaustive) | Media Types | NIST Method |
|---------------|-------------------------------|-------------|-------------|
| Overwrite Software | DBAN, Eraser, Blancco, Disk Wipe | HDD, USB | Clear/Purge |
| Secure Erase Utilities | hdparm, nvme-cli, Parted Magic | HDD, SSD | Purge |
| Degaussers | Proton T-4, VS Security PD-5 | HDD, Tape | Purge |
| Crypto-Erase Tools | BitLocker, LUKS, vendor firmware | FDE HDD/SSD | Purge |
| Physical Shredders | Whitaker Brothers, SEM, HSM | HDD, SSD, Paper | Destroy |
| Forensic Verification | EnCase, FTK, Autopsy, PhotoRec | All (testing) | Validation |

**Note:** Tool names provided as examples only. Organizations select tools meeting their requirements.

**Exception/Deviation Block (Rows 88-93):**
- Media types without approved deletion method (document risk)
- Legacy systems with non-standard media
- Outsourced destruction pending vendor qualification

---

### Sheet 3: Cloud Storage Deletion

**Purpose:** Assess deletion capabilities and methods for cloud-based storage (IaaS, PaaS, SaaS)

**Assessment Question:**
*"Can we effectively delete data from cloud storage providers, including all snapshots, backups, and multi-region copies?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.2, Section 2.2.2 (Cloud Storage Deletion)

**Column Structure:** A-U (21 columns total)
- Columns A-Q: Standard base columns
- Column R: Provider Tier (from ISMS-REF-A.5.23)
- Column S: Deletion API Available
- Column T: Snapshot/Backup Deletion
- Column U: Multi-Region Deletion Verified

**Data Entry Rows:** 13 rows (yellow-highlighted)

**Compliance Checklist (Rows 25-45):**

1. All cloud storage providers in use are identified
2. Provider tier classification assigned (Tier 1-10 per ISMS-REF-A.5.23)
3. Deletion method documented per provider (API, console, support ticket)
4. API-based deletion implemented for Tier 1-3 providers (critical)
5. Snapshot deletion procedures documented and tested
6. Backup deletion timeline documented (may differ from active data)
7. Multi-region/multi-zone deletion verified
8. Object versioning deletion addressed (S3, GCS, Azure Blob)
9. Soft-delete/recycle bin behavior documented
10. Deletion confirmation/verification method exists
11. Provider deletion SLA documented (see ISMS-IMP-A.8.10.3)
12. Cryptographic erasure option evaluated (customer-managed keys)
13. Account closure deletion behavior documented
14. Cross-provider data deletion coordinated (if data replicated)
15. Cloud deletion events logged and monitored

**Reference Table 1: Major Cloud Provider Deletion Methods (Rows 47-65)**
| Provider | Service | Deletion Method | Snapshots/Backups | Multi-Region | Crypto-Erase |
|----------|---------|----------------|-------------------|--------------|--------------|
| AWS | S3 | DELETE API, Lifecycle Policy | Manual or Lifecycle | ✅ Per region | ✅ CMK deletion |
| AWS | EBS | DeleteVolume API | DeleteSnapshot API | ✅ Per region | ✅ CMK deletion |
| AWS | RDS | DeleteDBInstance | DeleteDBSnapshot | ✅ Per region | ✅ CMK deletion |
| Azure | Blob Storage | Delete API, Lifecycle | Soft delete (90 days) | ✅ Per region | ✅ CMK deletion |
| Azure | Managed Disk | Delete API | Delete Snapshot | ✅ Per region | ✅ CMK deletion |
| Azure | SQL Database | Drop Database | Delete Backup | ✅ Per region | ✅ TDE key deletion |
| GCP | Cloud Storage | DELETE API, Lifecycle | Manual deletion | ✅ Per region/multi-region | ✅ CMEK deletion |
| GCP | Persistent Disk | Delete API | Delete Snapshot | ✅ Per region | ✅ CMEK deletion |
| GCP | Cloud SQL | Delete Instance | Delete Backup | ✅ Per region | ✅ CMEK deletion |

**Reference Table 2: Cloud Deletion Challenges (Rows 67-78)**
| Challenge | Description | Mitigation |
|-----------|-------------|------------|
| Soft Delete / Recycle Bin | Deleted data retained 30-90 days | Purge recycle bin, document timeline |
| Object Versioning | Previous versions retained | Delete all versions explicitly |
| Snapshots / Backups | Persist after source deletion | Lifecycle policy, manual deletion |
| Multi-Region Replication | Data in multiple regions | Region-by-region deletion, verify all |
| Cross-Account Access | Shared data in other accounts | Coordinate deletion with data owner |
| Delayed Deletion | Provider may not delete immediately | Document SLA, obtain confirmation |
| Metadata Retention | Logs, audit trails may persist | Separate retention policy for logs |
| Third-Party Integrations | Data copied to partner services | See ISMS-IMP-A.8.10.3 |

**Reference Table 3: Cloud Crypto-Erasure (Customer-Managed Keys) (Rows 80-90)**
| Provider | Service | CMK/CMEK Support | Key Deletion Effect |
|----------|---------|------------------|---------------------|
| AWS | S3, EBS, RDS | ✅ Yes (KMS CMK) | Data unreadable immediately |
| Azure | Blob, Disk, SQL | ✅ Yes (Key Vault CMK) | Data unreadable immediately |
| GCP | Storage, Disk, SQL | ✅ Yes (Cloud KMS CMEK) | Data unreadable immediately |
| Oracle Cloud | Object/Block Storage | ✅ Yes (Vault) | Data unreadable immediately |
| IBM Cloud | Object Storage | ✅ Yes (Key Protect) | Data unreadable immediately |

**Note:** Crypto-erasure via CMK deletion is NIST "Purge" method IF encryption properly implemented.

**Exception/Deviation Block (Rows 93-98):**
- Cloud providers without API deletion (manual process documented)
- Providers with >90 day soft-delete (GDPR compliance concern)
- Multi-region deletion not verified (remediation plan required)

---

### Sheet 4: Database & Application Deletion

**Purpose:** Assess logical deletion methods in databases and applications

**Assessment Question:**
*"Are database and application deletion methods effective, and do they address referential integrity, backups, and crypto-shredding where applicable?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.2, Section 2.2.3 (Database & Application Deletion)

**Column Structure:** A-U (21 columns total)
- Columns A-Q: Standard base columns
- Column R: Deletion Type
- Column S: Referential Integrity Handled
- Column T: Backup Purging
- Column U: Crypto-Erasure Key Management

**Data Entry Rows:** 13 rows (yellow-highlighted)

**Compliance Checklist (Rows 25-45):**

1. All databases and applications processing sensitive data identified
2. Deletion method documented per system (logical delete, hard delete, purge)
3. Referential integrity constraints addressed (cascading deletes or manual)
4. Soft delete (logical delete) systems have purge procedures
5. Hard delete operations tested and verified
6. Database backup purging procedures exist
7. Archive-then-delete workflows documented (if used)
8. Crypto-shredding evaluated for encrypted databases
9. Application-layer deletion triggers database deletion
10. Deletion operations are logged and auditable
11. Batch deletion procedures exist for large datasets
12. Deletion performance tested (large table truncation)
13. Database vacuuming/purging reclaims storage space
14. Third-party SaaS application deletion verified (see A.8.10.3)
15. Deletion operations do not impact system availability

**Reference Table 1: Database Deletion Methods (Rows 47-60)**
| Method | SQL Example | Effect | Use Case | Storage Reclaimed |
|--------|-------------|--------|----------|-------------------|
| Logical DELETE | UPDATE SET deleted=1 | Marks as deleted | Undo capability, audit trail | ❌ No (until purged) |
| Hard DELETE | DELETE FROM table WHERE | Removes immediately | Permanent deletion | ⚠️ After VACUUM |
| TRUNCATE | TRUNCATE TABLE | Removes all rows | Clear entire table | ✅ Immediate |
| DROP TABLE | DROP TABLE name | Removes table entirely | Decommission table | ✅ Immediate |
| Purge/Vacuum | VACUUM (PostgreSQL) | Reclaims space | After DELETE operations | ✅ Yes |
| Crypto-Shred | DROP ENCRYPTION KEY | Data unreadable | Encrypted DB deletion | ✅ Immediate (crypto) |

**Reference Table 2: Referential Integrity Handling (Rows 62-72)**
| Approach | Implementation | Pros | Cons |
|----------|----------------|------|------|
| CASCADE DELETE | FOREIGN KEY ... ON DELETE CASCADE | Automatic, consistent | Risk of unintended deletion |
| SET NULL | FOREIGN KEY ... ON DELETE SET NULL | Preserves child records | Orphaned records |
| RESTRICT | FOREIGN KEY ... ON DELETE RESTRICT | Prevents accidental deletion | Manual cleanup required |
| Manual Deletion | Application handles order | Full control | Error-prone, complex |
| Soft Delete Propagation | Update deleted flag in children | Reversible | Storage not reclaimed |

**Reference Table 3: Crypto-Shredding in Databases (Rows 74-85)**
| Database | Encryption Feature | Key Management | Crypto-Shred Method |
|----------|-------------------|----------------|---------------------|
| Oracle | Transparent Data Encryption (TDE) | Oracle Wallet or HSM | Drop wallet, delete keys |
| SQL Server | Transparent Data Encryption (TDE) | Certificate-based | Drop certificate |
| PostgreSQL | pgcrypto or TDE (EDB) | Key file or KMS | Delete encryption keys |
| MySQL | InnoDB Encryption | Keyring or KMS | Rotate to invalid key |
| MongoDB | Encryption at Rest | KMIP or local key | Delete master key |
| AWS RDS | Storage Encryption | KMS CMK | Delete CMK |

**Note:** Crypto-shredding requires encryption was properly implemented at creation.

**Exception/Deviation Block (Rows 88-93):**
- Systems using only soft delete (hard delete procedure required)
- Legacy databases without referential integrity enforcement
- Backup purging not implemented (GDPR concern)

---

### Sheet 5: Mobile & Endpoint Deletion

**Purpose:** Assess deletion methods for mobile devices, laptops, and endpoints

**Assessment Question:**
*"Can we securely delete data from corporate and BYOD devices, including remote wipe capabilities and full disk encryption support?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.2, Section 2.2.4 (Mobile & Endpoint Deletion)

**Column Structure:** A-U (21 columns total)
- Columns A-Q: Standard base columns
- Column R: Device Type
- Column S: MDM Solution Used
- Column T: Remote Wipe Capability
- Column U: Full Disk Encryption

**Data Entry Rows:** 13 rows (yellow-highlighted)

**Compliance Checklist (Rows 25-45):**

1. All endpoint device types documented (laptops, desktops, mobiles, tablets)
2. Corporate vs BYOD devices identified
3. Mobile Device Management (MDM) solution deployed
4. Remote wipe capability tested and functional
5. Full disk encryption (FDE) enabled on all corporate devices
6. Factory reset procedures documented
7. BYOD partial wipe capability (corporate data only)
8. Device encryption keys managed (BitLocker, FileVault, etc.)
9. Lost/stolen device wipe procedures exist
10. Employee offboarding triggers device wipe
11. BYOD app containerization supports selective wipe
12. Physical device destruction procedures (end-of-life)
13. Deletion verification for returned devices
14. MDM logs capture wipe commands and confirmations
15. Crypto-erasure supported (FDE key deletion)

**Reference Table 1: Device Deletion Methods (Rows 47-60)**
| Device Type | Deletion Method | Effectiveness | Requirements |
|-------------|----------------|---------------|--------------|
| Corporate Laptop (Windows) | BitLocker + Format | High (if FDE enabled) | BitLocker enabled, recovery key |
| Corporate Laptop (macOS) | FileVault + Erase | High (if FDE enabled) | FileVault enabled, recovery key |
| Corporate Laptop (Linux) | LUKS + Wipe | High (if FDE enabled) | LUKS encryption enabled |
| Corporate Mobile (iOS) | MDM Remote Wipe | Very High (FDE always on) | MDM enrollment |
| Corporate Mobile (Android) | MDM Remote Wipe | High (FDE if enabled) | MDM enrollment, FDE enabled |
| BYOD Mobile (iOS) | MDM Selective Wipe | Medium (corporate data only) | MDM enrollment, containerization |
| BYOD Mobile (Android) | MDM Selective Wipe | Medium (corporate data only) | MDM enrollment, work profile |
| Tablet (iOS/Android) | Same as mobile | Same as mobile | Same as mobile |
| Desktop Workstation | Overwrite or Destroy | High | Depends on storage type (HDD/SSD) |

**Reference Table 2: MDM Remote Wipe Capabilities (Rows 62-75)**
| MDM Solution (Examples) | Full Wipe | Selective Wipe | Platforms | Verification |
|------------------------|-----------|----------------|-----------|--------------|
| Microsoft Intune | ✅ Yes | ✅ Yes | Windows, iOS, Android, macOS | Command log + device check-in |
| VMware Workspace ONE | ✅ Yes | ✅ Yes | All major platforms | Command log + status report |
| Jamf Pro | ✅ Yes | ✅ Yes (via profiles) | macOS, iOS, iPadOS | Command history + inventory |
| MobileIron (Ivanti) | ✅ Yes | ✅ Yes | iOS, Android, Windows | Command log + confirmation |
| IBM MaaS360 | ✅ Yes | ✅ Yes | All major platforms | Action log + device status |
| Citrix Endpoint Management | ✅ Yes | ✅ Yes | All major platforms | Audit log + confirmation |

**Note:** Organizations document THEIR specific MDM solution.

**Reference Table 3: Full Disk Encryption (FDE) Support (Rows 77-88)**
| Operating System | FDE Solution | Crypto-Erase Method | Key Management |
|------------------|-------------|---------------------|----------------|
| Windows 10/11 | BitLocker | Delete recovery key | Active Directory, Azure AD, TPM |
| macOS | FileVault 2 | Delete recovery key | iCloud, MDM, local |
| Linux | LUKS (dm-crypt) | Delete LUKS header | Manual key file management |
| iOS | Built-in (always on) | Factory reset (key deleted) | Secure Enclave, Apple ID |
| Android | File-Based Encryption | Factory reset (key deleted) | TEE, user PIN/password |
| ChromeOS | Built-in | Powerwash (key deleted) | Google Account |

**Exception/Deviation Block (Rows 91-96):**
- BYOD devices without MDM enrollment (acceptable use policy required)
- Legacy devices without FDE capability (physical destruction required)
- Devices without remote wipe capability (retrieval procedures required)

---

### Sheet 6: Deletion Tool Validation

**Purpose:** Assess testing and validation procedures for deletion methods and tools

**Assessment Question:**
*"Do we regularly test our deletion methods using forensic tools to verify effectiveness, and do we remediate failed tests?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.2, Section 2.2.5 (Deletion Method Validation)

**Column Structure:** A-U (21 columns total)
- Columns A-Q: Standard base columns
- Column R: Test Frequency
- Column S: Forensic Tool Used
- Column T: Pass Rate (Last 12 Months)
- Column U: Independent Testing

**Data Entry Rows:** 13 rows (yellow-highlighted)

**Compliance Checklist (Rows 25-45):**

1. Annual forensic testing of deletion methods is scheduled
2. Representative sample of media types tested
3. Forensic recovery tools used (EnCase, FTK, Autopsy, etc.)
4. Pass/fail criteria defined (no data recovery = pass)
5. Failed tests trigger immediate investigation and remediation
6. Testing covers all NIST method types (Clear, Purge, Destroy)
7. Cloud deletion verification performed (where possible)
8. Database deletion verification performed (backup restoration test)
9. Mobile device wipe verification performed (MDM logs + device inspection)
10. Independent testing considered (external forensic firm)
11. Test results documented and linked to Evidence Register
12. Deletion tool vendors provide effectiveness documentation
13. New deletion methods tested before production use
14. Testing includes encrypted media (crypto-erasure validation)
15. Testing results reported to management and DPO

**Reference Table 1: Forensic Testing Approach (Rows 47-60)**
| Media Type | Test Method | Forensic Tool Examples | Pass Criteria |
|------------|-------------|----------------------|---------------|
| HDD (overwritten) | File recovery attempt | EnCase, FTK, PhotoRec | Zero files recovered |
| SSD (secure erased) | File recovery attempt | EnCase, FTK, PhotoRec | Zero files recovered |
| Cloud Storage (deleted) | API verification, backup check | AWS CLI, Azure CLI, manual | No objects found, no snapshots |
| Database (hard deleted) | Backup restoration + query | Database tools, SQL | Zero records recovered |
| Mobile Device (wiped) | Physical inspection + recovery | Cellebrite, Oxygen Forensics | Zero corporate data found |
| Crypto-Erased Media | Key verification, mount attempt | Forensic tools, OS mounting | Data unreadable, mount fails |

**Reference Table 2: Common Forensic Tools (Rows 62-72)**
| Tool | Type | Use Case | Cost |
|------|------|----------|------|
| EnCase Forensic | Commercial | Professional forensic recovery | High (enterprise) |
| FTK (Forensic Toolkit) | Commercial | Professional forensic recovery | High (enterprise) |
| Autopsy | Open Source | File recovery, analysis | Free |
| PhotoRec | Open Source | File carving, recovery | Free |
| Recuva | Freemium | Simple file recovery | Free/Low |
| TestDisk | Open Source | Partition/file recovery | Free |
| Cellebrite | Commercial | Mobile forensics | Very High |
| Oxygen Forensics | Commercial | Mobile forensics | High |

**Reference Table 3: Testing Frequency Recommendations (Rows 74-85)**
| Media Type | Recommended Frequency | Rationale |
|------------|----------------------|-----------|
| Physical Media (HDD/SSD) | Annual | Technology stable, methods validated |
| Cloud Storage | Semi-Annual | Provider changes, API updates |
| Database Deletion | Annual | Logic stable, backup testing |
| Mobile Devices | Quarterly | Frequent OS updates, MDM changes |
| New Deletion Tools | Before Production | Validate before operational use |
| After Failed Test | Immediate Retest | Verify remediation effectiveness |
| Regulatory Requirement | Per Requirement | GDPR, sector-specific regulations |

**Exception/Deviation Block (Rows 88-93):**
- Media types not tested (justify or remediate)
- Failed forensic tests in last 12 months (document remediation)
- Independent testing not performed (cost/benefit justification)

---

### Sheet 7: Summary Dashboard

**Purpose:** Provide executive-level overview of deletion method compliance and effectiveness

**Dashboard Structure:**

**Section 1: Overall Compliance Summary (Rows 3-12)**

| Assessment Area | Total Items | Compliant | Partial | Non-Compliant | Compliance % |
|-----------------|-------------|-----------|---------|---------------|--------------|
| Physical Media Deletion | [COUNT] | [COUNTIF] | [COUNTIF] | [COUNTIF] | [%] |
| Cloud Storage Deletion | [COUNT] | [COUNTIF] | [COUNTIF] | [COUNTIF] | [%] |
| Database & Application Deletion | [COUNT] | [COUNTIF] | [COUNTIF] | [COUNTIF] | [%] |
| Mobile & Endpoint Deletion | [COUNT] | [COUNTIF] | [COUNTIF] | [COUNTIF] | [%] |
| Deletion Tool Validation | [COUNT] | [COUNTIF] | [COUNTIF] | [COUNTIF] | [%] |
| **OVERALL A.8.10.2** | [SUM] | [SUM] | [SUM] | [SUM] | [Overall %] |

**Compliance Thresholds:**
- ≥ 90% Compliant = 🟢 Excellent
- 70-89% Compliant = 🟡 Needs Improvement
- < 70% Compliant = 🔴 Critical Attention Required

**Section 2: Critical Gaps Requiring Immediate Attention (Rows 15-25)**

Auto-populated from all assessment sheets where:
- Status = "❌ Non-Compliant" AND Risk Level = "Critical" OR "High"

| Media Type/System | Gap Description | Risk Level | Target Completion | Owner |
|-------------------|-----------------|------------|-------------------|-------|
| [Auto-populated] | | | | |

**Section 3: NIST Method Distribution (Rows 28-36)**

| NIST SP 800-88 Method | Count of Media Types | % of Total | Status |
|-----------------------|---------------------|-----------|--------|
| Clear | [COUNTIF Sheet2!R:R="Clear"] | [%] | ℹ️ Info |
| Purge | [COUNTIF Sheet2!R:R="Purge"] | [%] | ℹ️ Info |
| Destroy | [COUNTIF Sheet2!R:R="Destroy"] | [%] | ℹ️ Info |
| N/A (Non-Physical) | [COUNTIF Sheet2!R:R="N/A"] | [%] | ℹ️ Info |

**Section 4: Deletion Method Effectiveness (Rows 39-48)**

| Metric | Count/Percentage | Target | Status |
|--------|------------------|--------|--------|
| Media Types with Validated Methods | [Count where Last Test Date exists] | 100% | [Status] |
| Forensic Tests Passed (Last 12 Months) | [Sum of pass rates] | 100% | [Status] |
| Media Types Without Annual Testing | [Count overdue tests] | 0 | [Status] |
| Failed Forensic Tests (Unresolved) | [Count fail + no remediation] | 0 | [Status] |
| SSD Using Overwrite (Ineffective!) | [COUNTIF SSD + Overwrite] | 0 | [Critical if >0] |

**Section 5: Cloud Deletion Readiness (Rows 51-59)**

| Metric | Value | Notes |
|--------|-------|-------|
| Cloud Providers in Use | [COUNT Sheet3] | From ISMS-REF-A.5.23 |
| Providers with API Deletion | [COUNTIF API=Yes] | Tier 1-3 should have API |
| Providers with Snapshot Auto-Delete | [COUNTIF Snapshot=Automatic] | Reduces manual effort |
| Multi-Region Deletion Verified | [COUNTIF Multi-Region=Yes] | GDPR compliance |
| Crypto-Erasure Available | [COUNTIF Crypto-Erase supported] | CMK/CMEK usage |

**Section 6: Database Deletion Maturity (Rows 62-70)**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Databases with Hard Delete | [COUNT Hard Delete] | N/A | ℹ️ Info |
| Databases with Crypto-Shred | [COUNT Crypto-Shred] | Encrypted DBs | [Status] |
| Databases with Backup Purging | [COUNTIF Backup Purging implemented] | 100% | [Status] |
| Referential Integrity Handled | [COUNTIF RI = Yes] | 100% | [Status] |

**Section 7: Mobile & Endpoint Coverage (Rows 73-81)**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Endpoints | [COUNT Sheet5] | N/A | ℹ️ Info |
| Endpoints with FDE | [COUNTIF FDE = Yes] | 100% (corporate) | [Status] |
| Endpoints with Remote Wipe | [COUNTIF Remote Wipe = Yes] | 100% (corporate) | [Status] |
| BYOD Devices with Selective Wipe | [COUNTIF BYOD + Selective] | 100% (if BYOD allowed) | [Status] |
| MDM Enrollment Rate | [Calculated %] | 100% (corporate) | [Status] |

**Section 8: Risk Summary (Rows 84-92)**

| Risk Level | Count of Open Gaps | % of Total Gaps | Priority Action |
|------------|-------------------|-----------------|-----------------|
| Critical | [COUNTIF Critical] | [%] | Immediate escalation |
| High | [COUNTIF High] | [%] | Executive attention |
| Medium | [COUNTIF Medium] | [%] | Planned remediation |
| Low | [COUNTIF Low] | [%] | Monitor |

**Section 9: Executive Summary & Recommendations (Rows 95-110)**

**Text block (manually updated by assessor):**

**Overall A.8.10.2 Maturity Level:** [Emerging / Developing / Established / Optimized]

**Key Strengths:**
1. [Example: 100% of physical media use NIST Purge or Destroy methods]
2. [Example: All cloud providers support API-based deletion]
3. [Example: Annual forensic testing program with 100% pass rate]

**Critical Improvement Areas:**
1. [Example: 5 SSDs using ineffective overwrite method instead of Secure Erase]
2. [Example: 30% of databases lack backup purging procedures]
3. [Example: No independent forensic testing performed]

**Top 3 Recommendations:**
1. [Priority 1 action with timeline]
2. [Priority 2 action with timeline]
3. [Priority 3 action with timeline]

**Next Review Date:** [Date, typically annual]

---

### Sheet 8: Evidence Register

**Purpose:** Central repository for linking evidence to assessment findings

**Structure:** 100 pre-formatted rows for evidence tracking

**Column Layout:**

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Evidence ID | 12 | Text | Unique identifier (e.g., A810.2-001) |
| B | Assessment Sheet | 20 | Dropdown | Which sheet references this evidence |
| C | Related Media/System | 30 | Text | What this evidence supports |
| D | Evidence Type | 20 | Dropdown | Document, Screenshot, Log, Test Result, Certificate, Other |
| E | Evidence Title/Description | 35 | Text | Brief description |
| F | File Location/Link | 40 | Text | Network path, URL, or physical location |
| G | Date Created/Collected | 12 | Date | When evidence was generated |
| H | Retention Period | 15 | Dropdown | How long to keep evidence |
| I | Next Review Date | 12 | Date | When to re-validate |
| J | Owner/Custodian | 20 | Text | Person responsible |
| K | Notes | 30 | Text | Additional context |

**Evidence Type Dropdown Options:**
- Deletion Tool Documentation
- Forensic Test Report
- Screenshot/Print Screen
- System Log Export
- Configuration File
- Certificate of Destruction
- Vendor Documentation
- NIST SP 800-88 Compliance Memo
- Test Result (Pass/Fail)
- Third-Party Audit Report
- Other

**Assessment Sheet Dropdown Options:**
- Sheet 2: Physical Media Deletion
- Sheet 3: Cloud Storage Deletion
- Sheet 4: Database & Application Deletion
- Sheet 5: Mobile & Endpoint Deletion
- Sheet 6: Deletion Tool Validation

**Retention Period Options:**
- 3 years
- 5 years
- 7 years
- 10 years
- Duration of media lifecycle + 1 year
- Permanent

**Pre-populated Examples (Rows 10-15):**

| Evidence ID | Sheet | Item | Type | Description |
|-------------|-------|------|------|-------------|
| A810.2-001 | Sheet 2 | Corporate HDDs | Test Result | Forensic test report - 0 files recovered post-DBAN |
| A810.2-002 | Sheet 3 | AWS S3 Buckets | Screenshot | AWS Console showing bucket deletion confirmation |
| A810.2-003 | Sheet 4 | Customer DB | Configuration File | PostgreSQL VACUUM schedule and purge procedures |
| A810.2-004 | Sheet 5 | Corporate iPhones | System Log Export | Intune MDM wipe command log and device confirmation |
| A810.2-005 | Sheet 6 | SSD Testing | Third-Party Audit Report | External forensic firm validation of Secure Erase |

---

### Sheet 9: Approval Sign-Off

**Purpose:** Three-level approval workflow for assessment completion

**Structure:**

**Section 1: Document Control (Rows 3-10)**
- Assessment Period: [Date Range]
- Workbook Version: [e.g., 1.0]
- Total Assessment Sheets Completed: [5]
- Overall Compliance %: [Link to Summary Dashboard]
- Critical Gaps Identified: [Count from Summary]
- Assessment Completed By: [Name, Date]

**Section 2: Level 1 Approval - Technical/Operational (Rows 13-22)**
**Role:** IT Security Manager / Systems Administrator / Data Security Engineer

**Approval Statement:**
*"I confirm that this assessment accurately reflects our current deletion methods across all media types as of [Date]. All deletion tools have been documented, effectiveness testing is current, and remediation plans exist for identified gaps."*

| Field | Value |
|-------|-------|
| Approver Name | [Text entry] |
| Title/Role | [Text entry] |
| Email | [Text entry] |
| Review Date | [Date picker] |
| Approval Status | [Dropdown: ✅ Approved, ⚠️ Approved with Conditions, ❌ Rejected] |
| Conditions/Comments | [Text area] |
| Signature | [Text: "Electronically signed"] |

**Section 3: Level 2 Approval - Management (Rows 25-34)**
**Role:** Chief Information Security Officer / IT Director / Compliance Manager

**Approval Statement:**
*"I acknowledge the findings of this A.8.10.2 assessment and approve the proposed remediation plans. Budget and resources will be allocated to address critical gaps, particularly SSD deletion methods and forensic testing programs."*

| Field | Value |
|-------|-------|
| Approver Name | [Text entry] |
| Title/Role | [Text entry] |
| Email | [Text entry] |
| Review Date | [Date picker] |
| Approval Status | [Dropdown: ✅ Approved, ⚠️ Approved with Conditions, ❌ Rejected] |
| Conditions/Comments | [Text area] |
| Signature | [Text: "Electronically signed"] |

**Section 4: Level 3 Approval - Executive (Rows 37-46)**
**Role:** Chief Information Officer / Chief Risk Officer / Board Delegate

**Approval Statement:**
*"This assessment has been reviewed at the executive level. The organization's deletion method effectiveness is [Acceptable/Needs Improvement/Unacceptable]. The Board/Executive Team has been briefed on critical gaps related to SSD deletion, cloud provider dependencies, and forensic testing results."*

| Field | Value |
|-------|-------|
| Approver Name | [Text entry] |
| Title/Role | [Text entry] |
| Email | [Text entry] |
| Review Date | [Date picker] |
| Approval Status | [Dropdown: ✅ Approved, ⚠️ Approved with Conditions, ❌ Rejected] |
| Executive Summary | [Text area for key points communicated to Board] |
| Signature | [Text: "Electronically signed"] |

**Section 5: Next Steps (Rows 49-58)**

| Action Item | Responsible Party | Due Date | Status |
|-------------|-------------------|----------|--------|
| Replace SSD overwrite with Secure Erase methods | [Name] | [Date] | [Pending/In Progress/Complete] |
| Implement cloud snapshot auto-deletion | [Name] | [Date] | [Pending] |
| Engage external forensic testing firm | [Name] | [Date] | [Pending] |
| Annual re-assessment of A.8.10.2 | [Name] | [Date + 1 year] | [Scheduled] |
| Update deletion method documentation | [Name] | [Date] | [Pending] |

**Section 6: Audit Trail (Rows 61-70)**

| Date | Version | Change Description | Changed By |
|------|---------|-------------------|------------|
| [Auto] | 1.0 | Initial assessment completed | [Auto-populate] |
| [Entry] | 1.1 | [Example: Updated Sheet 2 with new HDD deletion tool] | [Name] |
| [Entry] | 1.2 | [Example: Added forensic test results for SSDs] | [Name] |

---

## Summary Dashboard - Calculation Notes

### Formula Guidelines

**Compliance Percentage Calculation:**
```
= COUNTIF(SheetX!F:F,"✅ Compliant") / (COUNTA(SheetX!F:F) - 9)
```

**NIST Method Distribution:**
```
= COUNTIF(Sheet2!R:R,"Purge") / COUNTA(Sheet2!R:R)
```

**SSD Overwrite Detection (Critical Issue):**
```
= COUNTIFS(Sheet2!A:A,"*SSD*", Sheet2!D:D,"Overwrite*")
```
*If this count > 0, flag as CRITICAL GAP (overwrite ineffective for SSDs)*

---

## Workbook Metadata

**File Naming Convention:**
`ISMS-IMP-A.8.10.2_Deletion_Methods_Assessment_YYYYMMDD.xlsx`

**Sheet Tab Colors:**
- Instructions: Blue (#4472C4)
- Assessment Sheets (2-6): Green (#70AD47)
- Summary Dashboard: Orange (#FFC000)
- Evidence Register: Gray (#A6A6A6)
- Approval Sign-Off: Purple (#7030A0)

**Default Sheet Protections:**
- Headers (Rows 1-9): Protected, locked
- Data entry cells (Yellow): Unprotected, editable
- Formula cells: Protected, locked
- Evidence Register: Fully editable
- Approval Sign-Off: Fully editable

---

## Implementation Notes

### For Script Generator (generate_a810_2_deletion_methods.py)

**Key Parameters:**
- Total Sheets: 9
- Data Entry Rows per Assessment Sheet: 13 (yellow-highlighted)
- Evidence Register Rows: 100
- Base Columns: A-Q (17 columns)
- Extended Columns: R-U (4 additional columns per sheet)

**Reusable Components from A.8.10.1:**
- Style definitions (header, subheader, input_cell, status colors)
- Data validation creator
- Evidence Register generator (identical structure)
- Approval Sign-Off generator (identical structure)
- Freeze panes logic

**A.8.10.2-Specific Components:**
- NIST SP 800-88 method dropdowns (Clear, Purge, Destroy)
- Media type specific validations
- HDD vs SSD deletion method distinctions
- Cloud provider tier integration (from ISMS-REF-A.5.23)
- Forensic testing result tracking
- MDM solution documentation (customer fills in)

**Critical Validation:**
- Flag if SSD + Overwrite method selected (ineffective!)
- Warn if no forensic testing date within 365 days
- Alert if cloud provider lacks API deletion

---

## Quality Assurance Checklist

**Before Delivery:**
- [ ] All 9 sheets present and correctly named
- [ ] NIST SP 800-88 framework explained in Instructions
- [ ] HDD vs SSD deletion differences documented
- [ ] Cloud provider tier dropdown references ISMS-REF-A.5.23
- [ ] Data validations working (test all dropdowns)
- [ ] Formulas in Summary Dashboard calculating correctly
- [ ] Yellow highlighting on all data entry cells
- [ ] Freeze panes active on assessment sheets
- [ ] Evidence Register has 100 rows
- [ ] Approval Sign-Off has 3-level workflow
- [ ] SSD overwrite detection formula working (critical!)
- [ ] File size < 5 MB
- [ ] No vendor-specific references (vendor-neutral confirmed)

---

**END OF SPECIFICATION**

**Related Documents:**
- ISMS-POL-A.8.10-S2.2 (Deletion Methods by Media Type Policy)
- ISMS-IMP-A.8.10.1 (Retention & Deletion Triggers) - Completed
- ISMS-IMP-A.8.10.3 (Third-Party & Cloud Deletion) - Next in sequence
- ISMS-REF-A.5.23 (Cloud Service Provider Registry)
- NIST SP 800-88 Rev. 1 (Guidelines for Media Sanitization)

**Version:** 1.0  
**Date:** [Approval Date] 
**Status:** Ready for Python Generator Implementation