**ISMS-IMP-A.7.10.1-UG - Storage Media Inventory Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.10: Storage Media

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.10.1-UG |
| **Version** | 1.0 |
| **Assessment Area** | Storage Media Inventory & Classification |
| **Related Policy** | ISMS-POL-A.7.10, Section 2.2 (Removable Media Management) |
| **Purpose** | Assess organisational compliance with storage media inventory, registration, and classification requirements across the media lifecycle |
| **Target Audience** | IT Operations, Asset Management, Information Security Officers, Physical Security, Compliance Officers, Auditors |
| **Assessment Type** | Asset Inventory & Operational Compliance |
| **Review Cycle** | Quarterly (minimum) or After Significant Media Acquisitions |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Storage Media Inventory assessment workbook | ISMS Implementation Team |

---

**Audience:** IT Operations, Asset Management, Physical Security Managers, Compliance Officers

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organisation]'s implementation of **storage media inventory and classification** to ensure compliance with ISO/IEC 27001:2022 Control A.7.10 and applicable data protection regulations.

**Scope:** Complete storage media lifecycle inventory across 5 critical areas:

1. **Digital Storage Media Inventory** - HDDs, SSDs, USB drives, SD cards, optical media, backup tapes
2. **Removable Media Registry** - Authorised removable devices with owner assignments
3. **Fixed Storage Assets** - Servers, workstations, network storage systems
4. **Cloud Storage Mapping** - Cloud backup and file storage locations
5. **Physical Documents & Archives** - Paper documents, microfilm, microfiche in secure storage

**Assessment Output:** Excel workbook with ~150-200 data points documenting current storage media inventory, classification status, custodianship, and gap remediation plans.

## Why This Matters

**ISO 27001:2022 Control A.7.10 Requirement:**
> *"Storage media should be managed through their life cycle of acquisition, use, transportation and disposal in accordance with the organisation's classification scheme and handling requirements."*

**Regulatory Context:**

- **EU GDPR (Article 5.1.f):** Integrity and confidentiality principle - appropriate security for processing
- **Swiss nDSG (Article 8):** Technical and organisational measures for data protection
- **PCI DSS v4.0 (Requirement 9.4):** Media protection requirements for cardholder data
- **ISO/IEC 27002:2022:** Control 7.10 implementation guidance

**Business Impact:**

- **Data Breach Risk:** Untracked media increases breach liability and forensic challenges
- **Regulatory Fines:** Inadequate media controls violate GDPR, PCI DSS requirements
- **Operational Efficiency:** Clear inventory enables systematic lifecycle management
- **Audit Readiness:** Documented inventory demonstrates control implementation
- **Chain of Custody:** Media tracking supports legal hold and e-discovery

## Who Should Complete This Assessment

**Primary Responsibility:** IT Operations Manager / Asset Management Lead

**Required Knowledge:**

- [Organisation]'s complete IT asset inventory
- Data classification scheme and handling requirements
- Physical security zones and access controls
- Cloud storage subscriptions and configurations
- Backup and archive systems

**Support Roles:**

- **Physical Security:** For secure storage locations and access logs
- **Procurement:** For media acquisition records and approved suppliers
- **Information Security:** For classification alignment and encryption requirements
- **Business Unit Owners:** For media usage justification
- **Compliance Team:** For regulatory requirement mapping

## Time Estimate

**Total Assessment Time:** 6-10 hours (depending on media inventory size)

**Breakdown:**

- **Digital Media Inventory (2-3 hours):** Document all digital storage devices
- **Removable Media Registry (1-2 hours):** Register and assign authorised removable media
- **Fixed Storage Assessment (1-2 hours):** Inventory servers, NAS, SAN systems
- **Cloud Storage Mapping (1 hour):** Document cloud storage locations
- **Evidence Collection (1-2 hours):** Gather supporting documentation

**Pro Tip:** For organisations with >500 storage media items, consider conducting assessment in phases by media type or business unit.

## Connection to Policy

This assessment implements **ISMS-POL-A.7.10, Section 2.2 (Removable Media Management)** which defines mandatory requirements for:

- **Media Registration:** All removable media registered in asset management system
- **Authorisation:** Line management approval for removable media use
- **Classification Alignment:** Media handling per data classification scheme
- **Encryption Requirements:** Hardware-encrypted devices for CONFIDENTIAL data
- **Inventory Audits:** Periodic reconciliation of media location and status

**Policy Authority:** Chief Information Security Officer (CISO)
**Compliance Status:** Mandatory for all storage media containing organisation information

---

# Prerequisites

## Access Required

Before starting this assessment, ensure you have access to:

**Documentation:**

- [ ] IT asset management system (CMDB)
- [ ] Current storage media inventory (if any)
- [ ] Data classification policy and scheme
- [ ] Approved supplier list for media procurement
- [ ] Physical security zone definitions
- [ ] Encryption deployment records

**Systems:**

- [ ] Asset management platform (e.g., ServiceNow, JIRA Assets, Freshservice)
- [ ] Endpoint management console (e.g., Intune, JAMF, SCCM)
- [ ] Cloud storage administration portals
- [ ] Physical access control system logs
- [ ] Backup system inventory

**Subject Matter Experts:**

- [ ] IT Operations (for media inventory details)
- [ ] Physical Security (for secure storage locations)
- [ ] Procurement (for media acquisition records)
- [ ] Information Security (for encryption requirements)

## Required Knowledge

**Asset Management:**

- IT asset lifecycle management principles
- Media type classifications and specifications
- Serial number and identifier tracking
- Custodianship and assignment workflows

**Security:**

- Data classification scheme in use at [Organisation]
- Encryption standards (AES-256, hardware encryption)
- Physical security zone requirements
- Chain of custody documentation

**Regulatory:**

- GDPR Article 5 and 32 requirements
- Swiss nDSG data protection obligations
- PCI DSS media protection requirements (if applicable)

## Pre-Assessment Checklist

Complete these tasks before beginning the assessment:

- [ ] **Export current IT asset inventory** from CMDB/asset management system
- [ ] **Identify all media types** in use across the organisation
- [ ] **Map physical storage locations** where media is kept
- [ ] **Verify encryption deployment status** for removable media
- [ ] **Collect procurement records** for recent media acquisitions
- [ ] **Schedule walkthrough** of data centre and secure storage areas
- [ ] **Review previous audit findings** related to media management

**Critical:** If [Organisation] has never conducted a formal media inventory, allow additional time (15-25 hours) for initial discovery and registration.

---

# Assessment Workflow

## Workflow Overview

```
Step 1: Digital Storage Media Inventory (Sheet 2)
   |
Step 2: Removable Media Registry (Sheet 3)
   |
Step 3: Fixed Storage Assets (Sheet 4)
   |
Step 4: Cloud Storage Mapping (Sheet 5)
   |
Step 5: Physical Documents Assessment (Sheet 6)
   |
Step 6: Evidence Collection (Sheet 8)
   |
Step 7: Review Summary Dashboard (Sheet 7)
   |
Step 8: Quality Check & Approval (Sheet 9)
```

## Step-by-Step Instructions

### Step 1: Digital Storage Media Inventory (Sheet 2)

**Objective:** Document every digital storage device managed by [Organisation]

**Instructions:**
1. List all digital storage media in Column A (e.g., "USB-001", "HDD-DC1-001", "TAPE-BKP-001")
2. Select Media Type in Column B (HDD, SSD, USB, SD Card, Tape, Optical, Other)
3. Assign Data Classification in Column C based on highest data level stored
4. Document Serial Number / Asset Tag in Column D
5. Identify Assigned Custodian in Column E
6. Record Physical Location in Column R
7. Indicate Encryption Status in Column S
8. Select Status in Column F (Registered / Unregistered / Pending)

**Media Types to Inventory:**

- **Hard Disk Drives (HDD):** Internal, external, portable
- **Solid State Drives (SSD):** SATA, NVMe, portable
- **USB Flash Drives:** Approved, encrypted, personal (flagged for remediation)
- **SD Cards / Memory Cards:** Cameras, mobile devices, IoT
- **Backup Tapes:** LTO, DLT, cartridge media
- **Optical Media:** CD, DVD, Blu-ray (archival)

**Quality Check:**

- Have you captured ALL media types in use?
- Are serial numbers/asset tags recorded for all items?
- Is every item assigned to a custodian?
- Are encryption requirements met for classified data?

### Step 2: Removable Media Registry (Sheet 3)

**Objective:** Register all authorised removable media with approval documentation

**Instructions:**
1. List each authorised removable device in Column A
2. Record Media Type in Column B (USB, External HDD/SSD, Tape, Optical)
3. Document Authorisation Reference in Column R (approval ticket/form number)
4. Record Authorised User(s) in Column S
5. Specify Permitted Use Cases in Column T
6. Document Authorisation Expiry Date in Column I

**Authorisation Requirements:**

- Line management approval for each removable device
- Documented business justification
- Time-limited authorisation (recommend 12 months maximum)
- Renewal process defined

**Common Removable Media Use Cases:**

- Data transfer between air-gapped systems
- Customer data delivery (encrypted)
- Backup media rotation (off-site)
- Field service data collection
- Presentation materials (approved content only)

**Quality Check:**

- Does every removable device have management approval?
- Are business justifications documented?
- Are personal devices flagged and prohibited?
- Is authorisation expiry tracked for renewal?

### Step 3: Fixed Storage Assets (Sheet 4)

**Objective:** Inventory all fixed storage systems (servers, NAS, SAN)

**Instructions:**
1. List each fixed storage system in Column A (e.g., "SRV-DC1-001", "NAS-SHARE-001")
2. Select System Type in Column R (Server, NAS, SAN, Archive System)
3. Document Total Capacity in Column S
4. Record Data Classifications Stored in Column T
5. Verify Encryption at Rest status in Column F

**Fixed Storage Categories:**

- **Servers:** Physical and virtual server storage
- **Network Attached Storage (NAS):** Shared file storage systems
- **Storage Area Networks (SAN):** Enterprise block storage
- **Archive Systems:** Long-term data archival
- **Backup Infrastructure:** Dedicated backup storage

**Quality Check:**

- Are all production storage systems documented?
- Is encryption at rest enabled for classified data?
- Are capacity utilisation and growth trends monitored?
- Are backup storage systems included?

### Step 4: Cloud Storage Mapping (Sheet 5)

**Objective:** Document all cloud storage locations and configurations

**Instructions:**
1. List each cloud storage service in Column A (e.g., "Azure Blob", "AWS S3", "SharePoint Online")
2. Select Cloud Type in Column R (IaaS, PaaS, SaaS, Hybrid)
3. Document Cloud Provider in Column S
4. Record Data Classifications Permitted in Column T
5. Verify Encryption Configuration in Column F

**Cloud Storage Types:**

- **IaaS Storage:** AWS S3, Azure Blob, Google Cloud Storage
- **PaaS Databases:** Azure SQL, AWS RDS, managed databases
- **SaaS File Storage:** SharePoint, OneDrive, Google Drive, Dropbox
- **Backup as a Service:** Cloud backup destinations

**Quality Check:**

- Are all sanctioned cloud storage services documented?
- Is shadow IT cloud storage identified and addressed?
- Are data residency requirements met?
- Are encryption configurations verified?

### Step 5: Physical Documents Assessment (Sheet 6)

**Objective:** Inventory physical document storage containing sensitive information

**Instructions:**
1. List each secure storage location in Column A (e.g., "Cabinet-HR-001", "Safe-Finance-001")
2. Select Document Type in Column R (Paper, Microfilm, Microfiche, Archive Boxes)
3. Document Highest Classification Stored in Column C
4. Record Physical Location in Column S
5. Verify Access Controls in Column T

**Physical Document Storage:**

- **Locked Cabinets:** Department-level secure storage
- **Safes:** High-security document storage
- **Archive Rooms:** Long-term physical archives
- **Secure Disposal Bins:** Pending shredding/destruction

**Quality Check:**

- Are all secure storage locations documented?
- Is access restricted to authorised personnel?
- Are environmental conditions appropriate?
- Is disposal process defined for physical media?

### Step 6: Evidence Collection (Sheet 8)

**Objective:** Link supporting documentation to assessment findings

**Instructions:**
1. For each finding, create evidence entry with unique Evidence ID
2. Document Evidence Type, Location, Retention Period
3. Reference Evidence ID in Column N of assessment sheets

**Evidence Types:**

- **Asset Reports:** CMDB exports, inventory reports
- **Authorisation Records:** Approval forms, tickets
- **Encryption Certificates:** Deployment records, compliance reports
- **Access Logs:** Physical security access records
- **Procurement Records:** Purchase orders, supplier contracts
- **Audit Reports:** Previous media audit findings

### Step 7: Review Summary Dashboard (Sheet 7)

**Objective:** Validate overall inventory completeness and compliance metrics

**The Summary Dashboard auto-calculates:**

- Total media items inventoried by type
- Classification distribution across media
- Encryption compliance percentage
- Unregistered media requiring remediation
- Authorisation status for removable media

### Step 8: Quality Check & Approval (Sheet 9)

**Objective:** Final validation and three-level approval workflow

**Self-Check Before Submitting for Approval:**

- [ ] All media types documented (no major gaps)
- [ ] Every item has serial number or unique identifier
- [ ] Custodians assigned for all media
- [ ] Encryption status verified for classified data
- [ ] Removable media has valid authorisation
- [ ] Evidence register populated

---

# Common Pitfalls

## Incomplete Inventory

**❌ MISTAKE:** Only documenting server-room media, missing end-user devices

**Why This Fails:**
- USB drives at desks represent significant data leakage risk
- Auditors expect comprehensive coverage
- Policy violations go undetected

**Prevention:**
- Survey end-users for personal device usage
- Use endpoint management to detect connected devices
- Include field service and remote worker devices

## Missing Serial Numbers

**❌ MISTAKE:** Recording media without unique identifiers

**Why This Fails:**
- Cannot verify specific device during audits
- Chain of custody breaks down
- Lost/stolen media unidentifiable

**Prevention:**
- Require serial number or asset tag for all entries
- Use barcode/QR scanning for accuracy
- Reject inventory entries without identifiers

## Unauthorised Removable Media

**❌ MISTAKE:** Allowing personal USB drives without approval

**Why This Fails:**
- GDPR and security policy violation
- Malware introduction risk
- Data exfiltration path

**Prevention:**
- Enforce removable media authorisation policy
- Deploy endpoint protection blocking unauthorised devices
- Regular audits for compliance

## Encryption Gaps

**❌ MISTAKE:** Assuming all media is encrypted without verification

**Why This Fails:**
- CONFIDENTIAL data on unencrypted media is policy violation
- Lost media = potential data breach notification
- Audit finding guaranteed

**Prevention:**
- Verify encryption for every CONFIDENTIAL/INTERNAL item
- Deploy hardware-encrypted USB drives as standard
- Maintain encryption compliance reports

## Cloud Storage Blind Spots

**❌ MISTAKE:** Not including SaaS and shadow IT storage

**Why This Fails:**
- Data may exist in uncontrolled locations
- GDPR data mapping incomplete
- Security controls not applied

**Prevention:**
- Survey users for cloud storage usage
- Review cloud access security broker (CASB) reports
- Include all sanctioned and discovered cloud storage

## Physical Media Omissions

**❌ MISTAKE:** Forgetting paper documents and archive storage

**Why This Fails:**
- A.7.10 explicitly includes physical media
- CONFIDENTIAL documents require secure handling
- Incomplete scope for audit

**Prevention:**
- Walk through all office areas with secure storage
- Interview department heads about archive locations
- Include secure disposal bins in scope

## Custodian Assignments Missing

**❌ MISTAKE:** Media without assigned responsible parties

**Why This Fails:**
- No accountability for media security
- Lost media has no escalation path
- Chain of custody undefined

**Prevention:**
- Require custodian for every inventory entry
- Automate assignment based on department/location
- Review orphaned media quarterly

## Authorisation Expiry Not Tracked

**❌ MISTAKE:** One-time approval without renewal process

**Why This Fails:**
- Business need may have ended
- User may have changed roles
- Perpetual authorisation contradicts least privilege

**Prevention:**
- Set 12-month maximum authorisation periods
- Automate renewal reminders
- Revoke expired authorisations promptly

---

# Quality Checklist

Before submitting assessment for approval, verify:

## Completeness

- [ ] All media types documented (digital, removable, fixed, cloud, physical)
- [ ] All sheets completed (no "TBD" or blank sections)
- [ ] Evidence Register populated with supporting documentation
- [ ] Summary Dashboard reviewed and validated

## Accuracy

- [ ] Serial numbers/asset tags verified against physical labels
- [ ] Custodian assignments confirmed with department heads
- [ ] Encryption status verified (not assumed)
- [ ] Classifications aligned with data stored

## Compliance

- [ ] Every removable device has valid authorisation
- [ ] CONFIDENTIAL media has encryption enabled
- [ ] Physical security zones documented for storage locations
- [ ] Cloud storage configurations reviewed

## Remediation Planning

- [ ] Unregistered media identified with remediation timeline
- [ ] Unauthorised devices flagged for blocking/removal
- [ ] Encryption gaps with deployment plan
- [ ] Expired authorisations scheduled for review

---

# Review & Approval

## Approval Workflow (Sheet 9)

**Level 1: Technical/Operational Approval**

- **Approver:** IT Operations Manager / Asset Management Lead
- **Validates:** Inventory accuracy, completeness, technical details
- **Approval Criteria:** Assessment accurately reflects current media inventory

**Level 2: Management Approval**

- **Approver:** Chief Information Security Officer / IT Director
- **Validates:** Compliance posture, remediation plans, resource allocation
- **Approval Criteria:** Gaps have realistic remediation plans

**Level 3: Executive Approval**

- **Approver:** Chief Operating Officer / Chief Risk Officer
- **Validates:** Overall media management posture, risk acceptance
- **Approval Criteria:** Executive acknowledges inventory status and risks

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
