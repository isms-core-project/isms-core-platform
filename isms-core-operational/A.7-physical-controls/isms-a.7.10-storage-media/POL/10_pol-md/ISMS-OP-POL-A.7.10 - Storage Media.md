**ISMS-OP-POL-A.7.10 — Storage Media**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Storage Media |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.7.10 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 0.1 |
| **Version Date** | [Date] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.7.10 — Storage media
- ISO/IEC 27002:2022 Section 7.10 — Implementation guidance
- NIST SP 800-88 Rev. 2 — Guidelines for Media Sanitization (September 2025)
- IEEE 2883:2022 — Standard for Sanitizing Storage
- DIN 66399 — Destruction of Data Carriers (security levels and media categories)
- Swiss nFADP (revDSG) — Federal Act on Data Protection
- Swiss DSV (Data Protection Ordinance) — Art. 1–3 (minimum data security requirements)

**Related Annex A Controls**:

| Control | Relationship to Storage Media |
|---------|-------------------------------|
| A.5.9 Inventory of information and other associated assets | Asset register that includes storage media inventory |
| A.5.10–11 Acceptable use and return of assets | Acceptable use rules and media return at employment exit |
| A.5.12–13 Information classification and labelling | Classification level determines media handling, storage, and disposal requirements |
| A.7.6–7–14 Secure areas, clear desk, secure disposal | Physical security of storage areas; disposal methods for equipment containing media |
| A.8.10 Information deletion | Logical deletion requirements that complement physical media sanitisation |
| A.8.24 Use of cryptography | Encryption standards for media protection at rest and in transit |

**Related Internal Policies**:

- Information Classification and Handling Policy
- Secure Areas and Media Handling Policy
- Asset Management Policy
- Endpoint Security Policy
- Use of Cryptography Policy

---

# Storage Media Policy

## Purpose

The purpose of this policy is to ensure that all storage media is managed securely throughout its lifecycle — from acquisition and registration, through use and transportation, to disposal or re-use — in accordance with the organisation's information classification scheme and applicable regulatory requirements.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data) stored on physical and digital media. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply. Both frameworks require that personal data on storage media be rendered unrecoverable before disposal or re-use.

Controls A.7.10 covers a single Annex A control but its scope spans the full media lifecycle: acquisition, registration, use, data transfer, transportation, secure storage, re-use, and disposal. This policy combines the policy requirements with operational guidance sufficient for an SME to implement and demonstrate compliance.

## Scope

All employees, contractors, and third-party users who handle, access, or are responsible for storage media containing organisation information.

**In-scope media types**:

- Digital removable media: USB flash drives, external hard drives, SD/microSD cards, optical media (CD, DVD, Blu-ray)
- Fixed storage: internal hard disk drives (HDD), solid state drives (SSD), NVMe drives
- Backup and archive media: LTO tapes, DAT/DLT cartridges, RDX cartridges
- Mobile device storage: smartphones, tablets, and devices with embedded storage
- Cloud and virtual storage: cloud backup, cloud file storage, virtual machine disk images
- Paper and analogue media: printed documents, microfilm, microfiche, photographic media

**Lifecycle phases covered**: Acquisition, registration, use, data transfer, transportation, storage, re-use, and disposal.

**Out of Scope**:

- Information classification scheme definitions (see Information Classification and Handling Policy, A.5.12–13)
- Cloud service provider contracts and third-party supplier management (see Cloud Services Policy, A.5.19–23)
- Cryptographic algorithm selection and key management details (see Use of Cryptography Policy, A.8.24)

## Principle

ISO/IEC 27001:2022 Annex A.7.10 states:

> *Storage media should be managed through their life cycle of acquisition, use, transportation and disposal in accordance with the organisation's classification scheme and handling requirements.*

Storage media shall be managed proportionately to the sensitivity of the information it contains or has ever contained. The highest classification level of data ever stored on a medium determines the handling and disposal requirements, regardless of whether that data has since been deleted.

All storage media containing organisation information shall be registered, tracked, and protected. Disposal shall render data unrecoverable using methods aligned with NIST SP 800-88 Rev. 2 and DIN 66399 standards, appropriate to the media type and information classification.

Personal removable media shall not be used for organisation data. Only organisation-approved and encrypted media shall be permitted.

---

## Removable Media Management

### Authorisation and Registration

Use of removable storage media shall be authorised before deployment:

- Employees shall obtain authorisation from their line manager before using any removable storage media for organisation data. Authorisation shall specify the permitted use case, data classification, and duration (default 12 months, maximum 24 months).
- All removable media shall be registered in [Asset Management System] with the following details: media type, capacity, serial number or asset tag, assigned user, purpose, maximum classification level of data to be stored, and authorisation expiration date.
- Only organisation-issued or organisation-approved removable media shall be used for organisation data. Personal USB drives, external hard drives, or other personal storage devices shall not be used for CONFIDENTIAL or INTERNAL data under any circumstances.
- Organisation-issued removable media shall be procured through approved suppliers from the organisation's procurement process. Unapproved or unknown-origin media shall not be connected to organisation systems.

**Authorisation lifecycle**:
- 30 days before expiration: Automated email reminder to employee and Line Manager from [Asset Management System]
- On expiration: Media status changed to "Expired" in system
- If media not renewed or returned within 15 days of expiration: IT Operations contacts employee for return or renewal
- Renewal: Employee submits renewal request with continued business justification; Line Manager approves (maximum 24 months per authorisation; after 24 months, re-justify need from scratch)
- Return: Employee returns media to IT Operations; media securely wiped per disposal procedures (even if media will be reissued — wipe between users); [Asset Management System] updated
- Unreturned media escalation: 15 days overdue → Line Manager escalation; 30 days overdue → CISO escalation, media marked "Missing," loss investigation initiated; 60 days overdue → assume lost/stolen, initiate incident response per lost media procedure
- Metrics: Media authorisation compliance rate (% returned or renewed on time) — target >95%; overdue media (>15 days past expiration) — target <3 items; reported in quarterly Management Review

### Approved Media Types

The organisation shall maintain a list of approved removable media types. As a minimum:

- **USB flash drives**: Hardware-encrypted, organisation-issued only (e.g., [Encrypted USB Model]). Software-only encryption is acceptable for INTERNAL data where hardware-encrypted devices are unavailable, subject to CISO approval and the following compensating controls:
  - CONFIDENTIAL data requires hardware encryption — no software-only exceptions
  - Maximum exception duration: 6 months (renewable with CISO approval)
  - Approved software tools: BitLocker To Go (Windows, AES-256), FileVault (macOS, AES-256), VeraCrypt (cross-platform, AES-256)
  - Strong passphrase mandatory: Minimum 16 characters, stored in [Password Manager]
  - Media shall be encrypted before first use (not encrypted after data is already written — residual unencrypted data risk)
  - Enhanced monitoring: Software-encrypted media usage logged, monthly review of access patterns
  - Quarterly re-authorisation: User re-confirms business need every 3 months; if need ends, media returned for secure disposal
  - Migration to hardware encryption: Software-encrypted exceptions shall be phased out as hardware-encrypted media becomes available (target: all INTERNAL data on hardware encryption within 12 months)
- **External hard drives**: AES-256 hardware-encrypted models from approved suppliers.
- **Optical media (CD/DVD/Blu-ray)**: Organisation-issued, labelled with classification, asset reference, date written, contents description, and retention expiry date. Write-once media (CD-R, DVD-R, BD-R) mandatory for: CONFIDENTIAL archival (legal documents, audit records, financial records), evidence preservation (forensic images, incident evidence, legal holds), and long-term retention (>5 years). Rewritable media (CD-RW, DVD-RW, BD-RE) permitted only for INTERNAL temporary data transfer and test/development data (maximum 12 months, then securely destroyed). Storage: jewel cases or slim cases (not paper sleeves — scratching risk), vertical orientation (not stacked flat — warping risk), cool dry environment away from sunlight. Plan migration to new media at 5-year mark for long-term retention data.
- **SD/microSD cards**: Permitted only for specific approved purposes (e.g., cameras, embedded systems). Shall be encrypted where the device supports it.

Unencrypted removable media shall not be used for CONFIDENTIAL data. Exceptions require documented CISO approval with compensating controls and a time limit not exceeding 6 months.

### Approved Media List Maintenance

The approved media list shall be reviewed and maintained on a regular cycle:

- **Annual review**: IT Operations and CISO review the approved media list in Q4
- **Triggered review**: When a new media technology becomes available, a security vulnerability is discovered in a current approved model, or procurement identifies a discontinued model

Review criteria:
- Encryption standard current (AES-256 minimum for CONFIDENTIAL, AES-128 minimum for INTERNAL)
- Hardware encryption preferred (FIPS 140-2 Level 2 or higher for CONFIDENTIAL media)
- Vendor support status (active support, security updates available)
- Cost-effectiveness (price per GB, bulk procurement availability)
- Compatibility with organisation endpoints (Windows, macOS, Linux)

Approval process: IT Operations proposes additions or removals with technical assessment; CISO approves changes; Procurement updates preferred supplier list; approved media list published on intranet and communicated to all staff. List shall include version date and next review date.

### Quarterly Media Audit

A risk-based audit of registered removable media shall be conducted quarterly:

**Audit scope by risk tier**:

| Risk Tier | Criteria | Quarterly Sample | Annual Coverage |
|-----------|----------|------------------|-----------------|
| **High-risk** | Media that has stored CONFIDENTIAL data (current or historical); media transported offsite regularly; media assigned to executives or privileged users | 100% verification | 100% per quarter |
| **Medium-risk** | Media with INTERNAL data only; office-based use only | 50% rotating sample | 100% over 2 quarters |
| **Low-risk** | Media with PUBLIC data only; media in long-term secure archive storage | 25% rotating sample | 100% annually |

**Audit procedure**:
1. Generate sample list from [Asset Management System] based on risk tier
2. Physical verification: Confirm location, holder, encryption status, serial number matches record
3. Spot-check encryption: Randomly test 10% of sampled media (attempt access without password/encryption key)
4. Document results: Reconciliation report with findings, discrepancies, and follow-up actions

**Findings escalation**:
- Missing high-risk media: Immediate escalation to CISO (same day); assume lost/stolen; initiate breach assessment per lost media incident response procedure
- Missing medium-risk media: Escalate within 2 business days; investigation by IT Operations
- Missing low-risk media: Document and follow up within 5 business days

**Annual comprehensive audit**: 100% verification of ALL media (all risk tiers) conducted once per year (Q4 or as scheduled by CISO).

Audit results shall be documented and retained for 12 months.

---

## Media Use Requirements

### Data Transfer to Removable Media

- Transfer of CONFIDENTIAL data to removable media requires documented management approval prior to transfer. The approval record shall state the business justification, recipient, and expected return date.
- All data transferred to removable media shall be encrypted. For CONFIDENTIAL data, AES-256 encryption (hardware or software) is mandatory. For INTERNAL data, AES-128 or stronger is required.
- Transfer logs shall be maintained for CONFIDENTIAL data, recording: date, user, media identifier, data description, and recipient.
- Data shall be removed from removable media as soon as it is no longer needed for the approved purpose.

### Access Control and Protection

- Media containing CONFIDENTIAL data shall be password-protected or encrypted with strong authentication (PIN, passphrase, or biometric unlock on the device).
- Media shall not be left unattended at any time. When not in active use, media shall be secured in locked storage appropriate to the classification level.
- Removable media shall not be connected to untrusted or public systems.
- Media contents shall be scanned for malware by [Endpoint Protection Tool] before data is opened or transferred to organisation systems. Auto-run and auto-play shall be disabled on all endpoints via [Endpoint Management Tool] policy.

### USB Port and Removable Media Controls

- USB ports and removable media access shall be managed centrally via [Endpoint Management Tool] (e.g., Group Policy, MDM, or endpoint protection platform).
- Default policy: USB mass storage devices blocked on all endpoints. Exceptions granted per device serial number for registered, encrypted media only.
- All USB connection events shall be logged by the endpoint protection platform. Logs shall be retained for a minimum of 12 months.

**USB port control by workstation type** — Different workstation types have different USB access requirements:

| Workstation Type | USB Mass Storage | Approved Media | Logging |
|------------------|------------------|----------------|---------|
| **Standard office desktop/laptop** | Blocked by default | Exception by serial number (registered encrypted media only) | All connection attempts logged |
| **Developer workstation** | Allowed for registered encrypted media only | Organisation-issued encrypted USB + approved development tools (Yubikey, hardware security keys) | All connections logged |
| **Executive/mobile worker laptop** | Allowed for registered encrypted media only | Organisation-issued encrypted USB | All connections logged; quarterly access review |
| **Kiosk/public-facing system** | Blocked (no exceptions) | None | All connection attempts logged and alerted |
| **Server/infrastructure** | Blocked (no exceptions except authorised IT Operations during maintenance) | Approved rescue/diagnostic media only (encrypted, read-only where possible) | All connections logged and alerted |

Implementation via [Endpoint Management Tool]: Device Control Policy with whitelist by device serial number (not device type); different policy groups per workstation type (AD group-based or device tag-based). Alert on: unauthorised USB connection attempts, USB connections outside business hours, bulk data transfers (>1 GB), multiple failed authentication attempts on encrypted media.

**Temporary exception** (visitor/contractor, short-term need <7 days): Approval by IT Operations + Line Manager; maximum 7 days; enhanced logging + daily review; exception auto-removed from whitelist at expiration.

---

## Transportation of Storage Media

### Secure Transportation Requirements

When storage media must be transported, the following requirements apply:

**Courier and Postal Shipment**:

- CONFIDENTIAL media shall be transported only by approved secure courier services with tracking and signature on delivery. Standard postal services shall not be used for CONFIDENTIAL data.
- INTERNAL media should use tracked courier services. Standard postal services may be used with registered/tracked delivery.
- Tamper-evident packaging shall be used for all media containing CONFIDENTIAL data. The recipient shall inspect packaging for evidence of tampering and report any anomalies immediately.
- Chain of custody documentation shall accompany all shipments of CONFIDENTIAL media (see Chain of Custody section below).

**Personal Transport (Hand-Carry)**:

- Media shall be carried in hand luggage during travel (never in checked baggage).
- Media shall be encrypted and shall not be left unattended at any time during transport.
- Transport through high-risk areas (public transport hubs, conferences, foreign jurisdictions without adequate data protection) should be avoided where alternatives exist. Where unavoidable, additional encryption and access controls shall be applied.

**Electronic Transfer Alternative**:

Where feasible, encrypted electronic transfer (e.g., secure file sharing, SFTP, encrypted email) should be preferred over physical media transport. Physical transport should be used only when electronic transfer is impractical or prohibited.

**Transport Environmental Protection**:

Storage media (especially magnetic tape and HDDs) is sensitive to temperature, humidity, and physical shock during transport:

- **Summer transport (ambient >30 °C)**: Use insulated shipping containers; avoid leaving media in vehicles; prefer same-day or overnight delivery to minimise transit time
- **Winter transport (ambient <5 °C)**: Use insulated shipping containers; allow media to acclimate to room temperature (minimum 2 hours) before use if exposed to freezing conditions
- **Shock protection**: Use anti-static bubble wrap + rigid outer container (not padded envelope); label "Fragile — Electronic Media" on all sides; mark "This Side Up" for tape cartridges
- **Humidity protection**: Use desiccant packets (silica gel) in shipping containers for humid climates or rapid humidity changes

| Media Type | Temperature Tolerance (Non-Operating) | Shock Sensitivity | Recommended Packaging |
|------------|---------------------------------------|-------------------|----------------------|
| Magnetic tape (LTO, DAT) | –40 to 65 °C | High (mechanical internals) | Anti-static + rigid case + "Fragile" label |
| HDD | –40 to 70 °C | High (moving parts) | Anti-static + foam padding + rigid case |
| SSD / Flash | –40 to 85 °C | Low (no moving parts) | Anti-static + standard packaging |
| Optical (CD/DVD) | 5 to 50 °C | Low | Jewel case + padded mailer |

Courier instructions for CONFIDENTIAL media: Provide handling instructions to courier; require signature on delivery (no "leave at door"); track shipment in real time; investigate if delivery delayed >24 hours. Recipient shall inspect packaging for damage upon receipt and report any physical damage immediately.

### Chain of Custody

All transfers of media containing CONFIDENTIAL data between individuals, locations, or organisations shall be documented with:

- Date and time of handover
- Identity of releasing party (name, role)
- Identity of receiving party (name, role, organisation if external)
- Media identifier (asset tag, serial number)
- Description of contents (classification level, general data category — not the data itself)
- Acknowledgement of receipt (signature or electronic confirmation)
- Expected return date (where applicable)

Chain of custody records shall be retained for 7 years.

**Logical data transfer chain of custody**: Where data is transferred electronically rather than via physical media, chain of custody shall also be documented:
- Documentation required: Date/time, sender, recipient, file names/sizes, classification, transfer method (email/SFTP/secure file share), encryption method (e.g., "AES-256 via [Tool]"), link expiration (if link-based)
- Logging: Automatic capture via [Secure File Sharing Tool] / [Email Gateway] audit logs where available
- Retention: 12 months (logs); 7 years (CONFIDENTIAL transfer records)

*Preferred transfer method by scenario*:

| Scenario | Preferred Method | Rationale |
|----------|------------------|-----------|
| File <100 MB | Encrypted email or secure file sharing (e.g., [Tool]) | Faster; no physical media risk |
| File 100 MB–10 GB | Secure file sharing with expiring link | Avoids email size limits; traceable |
| File >10 GB | Encrypted USB via courier, or SFTP/cloud sync | Physical media practical for large transfers |
| Archival/backup (TB-scale) | Encrypted tape via courier | Most cost-effective for bulk archival |

For CONFIDENTIAL logical transfers: End-to-end encryption mandatory (encrypted before upload/send, recipient decrypts). Link-based sharing: Expiring links (maximum 7 days), password-protected, download notification to sender. Email: Encrypted attachment (GPG/PGP or [Secure Email Tool]), recipient identity verified before sending.

---

## Storage Requirements

### Physical Storage by Classification

Storage media shall be stored in conditions appropriate to both the sensitivity of the information and the physical integrity of the medium:

| Classification | Physical Storage | Encryption | Access Control | Environmental Requirements |
|----------------|-----------------|------------|----------------|---------------------------|
| **CONFIDENTIAL** | Locked safe or secure cabinet within a restricted area | Mandatory — AES-256 (per Cryptography Policy) | Named individuals only; access logged | Temperature 15–25 °C; 30–60% RH; away from magnetic fields and direct sunlight |
| **INTERNAL** | Locked cabinet or drawer | Recommended — AES-128 or stronger | Authorised staff with legitimate business need | Standard office conditions; away from environmental hazards |
| **PUBLIC** | Standard office storage | Optional | General access; physical security maintained | Standard office conditions |

### Backup Media Storage

- Backup tapes and cartridges shall be stored in a separate physical location from the systems they back up (off-site or in a separate fire zone).
- Backup media shall be encrypted using strong vendor encryption or an organisation-approved encryption tool.
- Backup media shall be included in the media inventory and subject to the same quarterly audit as removable media.

### Retention and Expiry

- Media shall be retained in accordance with the organisation's data retention schedule. Retention periods are defined by data type, regulatory requirement, and business need.
- When the retention period for data on a medium expires, the medium shall be sanitised or destroyed per the Disposal section of this policy.
- Backup tapes and cloud snapshots shall have documented disposal or deletion triggers aligned with the retention schedule. "Indefinite" retention is not permitted without documented CISO approval and annual review.

**Backup media retention framework** — Two-tier approach separating operational recovery from legal/compliance retention:

*Operational backup retention* (for disaster recovery and operational restore):
- Daily backups: 30 days
- Weekly backups: 90 days (3 months)
- Monthly backups: 12 months
- Annual backups: 3 years (long-term restore safety net)

*Legal/compliance data retention* (for regulatory, legal hold, audit):
- Separate from operational backups — use structured archival storage, not tape-based full system backups
- Financial records: 10 years (Swiss CO Art. 958f)
- HR records: 10 years
- Customer data: Per contract or applicable regulation

*Backup deletion triggers*:

| Backup Type | Deletion Trigger | Method |
|-------------|------------------|--------|
| Daily backups >30 days | Automatic deletion by backup tool | Retention policy in [Backup Tool], logged |
| Weekly backups >90 days | Automatic deletion by backup tool | Retention policy in [Backup Tool] |
| Monthly backups >12 months | Manual review + IT Operations Manager approval | Review quarterly; delete with signed approval |
| Annual backups >3 years | Manual review + CISO approval | Review annually; delete with signed approval |
| Cloud snapshots (orphaned) | Quarterly identification + 90-day grace period | Lifecycle policy; review orphaned snapshots quarterly |

*Legal hold exception*: If data subject to legal hold (litigation, investigation, audit), backup deletion shall be suspended for affected data. Legal hold documented in [Asset Management System] with hold reason, start date, and review date. Resumption of deletion requires Legal/Compliance approval.

---

## Disposal of Storage Media

### Disposal Principles

Disposal and sanitisation shall ensure that information cannot be recovered, using organisation-approved methods appropriate to the media type and the highest classification of data ever stored on the medium.

The organisation adopts the NIST SP 800-88 Rev. 2 framework for media sanitisation, aligned with IEEE 2883:2022 technical recommendations for storage device sanitisation:

| Sanitisation Level | Method | Description | Use Case |
|--------------------|--------|-------------|----------|
| **Clear** | Logical overwrite | Overwrites user-accessible storage locations with non-sensitive data using standard read/write commands. Protects against simple, non-invasive data recovery techniques. | PUBLIC data; internal re-use of low-sensitivity equipment |
| **Purge** | Cryptographic erase, block erase, or firmware-level commands | Renders data recovery infeasible using state-of-the-art laboratory techniques. Includes cryptographic erasure (destroying encryption keys on self-encrypting drives) and manufacturer secure erase commands per IEEE 2883. | INTERNAL data; internal re-use; external transfer of previously INTERNAL equipment |
| **Destroy** | Physical destruction | Renders media physically unusable through shredding, disintegration, pulverising, or incineration. Data recovery is infeasible regardless of effort applied. | CONFIDENTIAL data; all external disposal of media that stored sensitive data; end-of-life for any media where sanitisation cannot be verified |

### Disposal Requirements by Classification

| Classification | Required Outcome | Minimum NIST Level | Verification |
|----------------|------------------|---------------------|--------------|
| **CONFIDENTIAL** | Unrecoverable by any means, including state-of-the-art laboratory techniques | Destroy (or Purge only for internal re-use with verified cryptographic erase) | Certificate of destruction from approved vendor; witnessed destruction for highly sensitive data |
| **INTERNAL** | Unrecoverable without specialist equipment or techniques | Purge | Verification of successful erasure documented with tool output log |
| **PUBLIC** | Standard deletion with documented disposal | Clear | Documentation of disposal in asset register |

### Disposal Methods by Media Type

| Media Type | CONFIDENTIAL | INTERNAL | PUBLIC |
|------------|--------------|----------|--------|
| **Hard Disk Drives (HDD)** | Physical destruction: shredding or degauss + shred | Purge: manufacturer secure erase (ATA Secure Erase, NVMe Sanitize) or single-pass overwrite with verification, or physical destruction | Format and reinstall |
| **Solid State Drives (SSD/NVMe)** | Physical destruction: shredding or disintegration | Cryptographic erasure or manufacturer secure erase per IEEE 2883; physical destruction if crypto erase unavailable | Secure erase command |
| **USB Flash Drives / SD Cards** | Physical destruction: shredding | Secure overwrite or physical destruction | Format |
| **LTO / Backup Tapes** | Physical destruction: shredding or incineration | Degaussing + overwrite or physical destruction | Degaussing or overwrite |
| **Optical Media (CD/DVD/Blu-ray)** | Physical destruction: shredding or incineration | Physical destruction: shredding | Physical destruction or defacing |
| **Mobile Devices** | Physical destruction of storage components | Factory reset + cryptographic erasure verification | Factory reset |
| **Printers / Copiers (internal HDD/SSD)** | Internal storage removal + destruction | Internal storage removal + secure wipe | Clear memory / factory reset |
| **Cloud / Virtual Storage** | Cryptographic erasure + deletion confirmation + provider SOC 2/ISO 27001 certification reliance | Cryptographic erasure + deletion confirmation from provider | Standard deletion via provider API/console |

**Important note on SSD and flash media**: Traditional overwrite methods are unreliable for SSDs and flash storage due to wear-levelling, over-provisioning, and write amplification. For SSD and flash-based media, cryptographic erasure (where supported by self-encrypting drives) or manufacturer-provided secure erase commands per IEEE 2883:2022 are the approved Purge methods. Where neither is available or cannot be verified, physical destruction is required.

**HDD overwrite — NIST SP 800-88 Rev. 2 guidance**: NIST SP 800-88 Rev. 2 (September 2025) confirms that a single-pass overwrite is sufficient for modern HDDs (post-2001 manufacturing). Multi-pass overwrite (e.g., legacy DoD 5220.22-M 3-pass or 7-pass methods) is no longer required and provides no additional security benefit on modern drives. Approved Purge methods for HDDs: manufacturer secure erase command (ATA Secure Erase, NVMe Sanitize), or single-pass overwrite with verification using an approved tool (e.g., DBAN, nwipe, shred, or dd). Verification shall include tool completion report with serial number, timestamp, and pass/fail status.

**Degaussing requirements for magnetic media**: Degaussing effectiveness depends on the magnetic field strength of the degausser relative to the coercivity of the media. The degausser shall be rated for the media type being sanitised:

| Media Type | Coercivity Range | Minimum Degausser Rating |
|------------|-----------------|--------------------------|
| LTO-7/8/9 tapes | ~2,800–3,200 Oe | ≥7,000 Gauss (NSA/CSS EPL-listed recommended) |
| LTO-5/6 tapes | ~2,500–2,800 Oe | ≥5,000 Gauss |
| DAT/DLT cartridges | ~1,500–2,000 Oe | ≥5,000 Gauss |
| HDDs (legacy, pre-SSD) | ~2,000–5,000 Oe | ≥9,000 Gauss for reliable erasure |

Degausser validation: Degaussing equipment shall be tested annually (or per manufacturer recommendations) to verify field strength remains within specification. Testing records shall be retained. SSDs and flash media cannot be degaussed — degaussing has no effect on solid-state storage.

**Cloud and virtual storage disposal**: Major cloud providers (AWS, Azure, GCP) do not provide individual destruction certificates for virtual storage. For cloud disposal, the organisation shall:
- Delete volumes/objects via cloud console or API and delete encryption keys from KMS (cryptographic erasure)
- Retain deletion confirmation evidence (screenshot or API audit log with volume ID and deletion timestamp)
- Rely on provider SOC 2 Type II / ISO 27001 certification attesting that deleted storage is sanitised per NIST SP 800-88 before hardware reuse or disposal
- Document provider certification reliance in the disposal record (e.g., "AWS SOC 2 Type II dated [Date]")
- For highest-sensitivity CONFIDENTIAL data: Use client-side encryption (organisation controls keys, not provider) as mitigation — even if provider fails to delete, data remains encrypted
- Executive Management shall acknowledge reliance on provider-certified deletion processes annually in the Management Review

### Internal Re-Use

Before media is re-used within the organisation:

- All data shall be securely erased using an approved method appropriate to the previous data classification.
- Erasure shall be verified using [Secure Wipe Tool] and the verification log retained.
- Media shall be inspected for physical integrity. Damaged media shall not be re-used but destroyed.
- [Asset Management System] records shall be updated with the new assignment, date, and sanitisation evidence.
- Licensed software shall be transferred or removed per licensing terms.

### External Disposal

Media being disposed of externally shall:

- Have all data securely erased to the required level, or be physically destroyed.
- Be disposed of through approved destruction vendors only.
- Have disposal documented with certificates of destruction retained for 7 years.
- Never be sold, donated, or discarded with recoverable data.

Equipment that has stored CONFIDENTIAL data shall not be re-used externally. Storage media shall be physically destroyed before any external transfer.

### Destruction Certificates

For all media destroyed by external [Destruction Vendor] or specialist suppliers:

- A certificate of destruction shall be obtained for every batch or individual item destroyed.
- Certificates shall reference individual serial numbers or asset tags, not only batch identifiers.
- The destruction method and compliance standard (e.g., NIST SP 800-88 Destroy, DIN 66399 level) shall be stated.
- Certificates shall be matched against the handover record to ensure all items are accounted for. Discrepancies shall be escalated immediately and logged as a security event.
- Certificates shall be filed with the disposal record and retained for 7 years.

---

## Paper Documents and Physical Media

### Paper Document Handling

- Paper documents shall be classified and handled per the Information Classification and Handling Policy.
- CONFIDENTIAL documents shall be stored in locked cabinets or safes when not in immediate active use:
  - **Locked filing cabinet**: Suitable for standard CONFIDENTIAL business documents (contracts, financial records, customer lists) up to approximately 1 drawer (~1,000 sheets). Metal cabinet with key or combination lock, secured to floor/wall where feasible.
  - **Locked safe**: Required for trade secrets, M&A documents, legal privilege materials, and highly sensitive personal data (executive health records, background check results). Fire-rated safe (minimum 1-hour resistance), combination or electronic lock, access limited to 2–3 named individuals.
  - **Document vault/secure room**: Required for large-volume CONFIDENTIAL archival storage (>10 file boxes). Dedicated locked room with card access control, CCTV, and environmental controls (fire suppression, humidity).
- Documents shall be collected immediately from printers, copiers, and fax machines. Secure print release (pull printing) should be implemented where available.
- Clean desk policy shall be followed at all times (see Secure Areas and Media Handling Policy, A.7.6–7–14).

### Paper Document Destruction

Paper destruction shall comply with DIN 66399 standards. DIN 66399 defines security levels using a letter prefix for the media category (P = paper) and a number for the security level (1–7, higher = smaller particles):

| Classification | DIN 66399 Level | Particle Size | Method |
|----------------|-----------------|---------------|--------|
| **CONFIDENTIAL** | P-4 minimum (P-5 recommended for sensitive personal data) | P-4: max 160 mm², width max 6 mm | Cross-cut shredding |
| **INTERNAL** | P-3 minimum | P-3: max 320 mm², width max 2 mm | Cross-cut or strip-cut shredding |
| **PUBLIC** | No minimum requirement | N/A | General waste / recycling |

- Shredding shall be performed on-site using organisation-owned shredders where possible. For bulk destruction, approved external providers may be used with collection in locked confidential waste bins and certificates of destruction.
- Confidential waste bins shall be provided at accessible locations throughout the office. Bins shall be locked and emptied on a scheduled basis by authorised personnel or [Destruction Vendor].
- Mass destruction events (office moves, archive purges) shall be witnessed or certified.

### Microfilm, Microfiche, and Photographic Media

- Destruction shall follow DIN 66399 media category F (film) at security levels corresponding to the classification of the information.
- CONFIDENTIAL: F-4 minimum (max 160 mm² particle size). INTERNAL: F-3 minimum.
- Where on-site shredding of film media is not possible, an approved external vendor shall be used.

---

## Roles and Responsibilities

| Role | Storage Media Responsibilities |
|------|-------------------------------|
| **Executive Management** | Approve policy; allocate resources for media security infrastructure and vendor contracts |
| **CISO** | Policy ownership; define sanitisation standards; oversee compliance; approve exceptions; review quarterly audit results |
| **IT Operations** | Media procurement and provisioning; encryption deployment; execute sanitisation and destruction; maintain disposal records; manage [Secure Wipe Tool] and [Endpoint Management Tool] |
| **Facilities Manager** | Manage physical storage infrastructure (safes, locked cabinets); coordinate confidential waste bin provision and collection; manage on-site shredding equipment |
| **Line Managers** | Authorise removable media use for their teams; ensure team compliance with handling and storage requirements; address audit findings |
| **Procurement / Vendor Management** | Manage [Destruction Vendor] contracts; verify vendor certifications; collect and verify destruction certificates |
| **Asset Management** | Maintain media inventory in [Asset Management System]; conduct quarterly media audits; reconcile records; update asset status on disposal |
| **All Personnel** | Handle media per classification requirements; return media at employment exit; report lost, stolen, or damaged media immediately; do not use personal media for organisation data |

**Escalation Path**:

- Lost or stolen media: Employee --> Line Manager + IT Operations (immediate) --> CISO
- Media policy questions: Employee --> IT Operations --> CISO
- Missing destruction certificates: IT Operations --> Procurement --> CISO
- Quarterly audit discrepancies: Asset Management --> CISO --> Executive Management (if unresolved within 5 business days)

### Lost or Stolen Media Incident Response

When media loss or theft is reported, the following immediate actions shall be taken:

**Within 15 minutes of report:**

1. **Assess severity**:
   - Classification of data on media (CONFIDENTIAL = Critical, INTERNAL = High, PUBLIC = Low)
   - Encryption status (encrypted = lower risk, unencrypted = higher risk)
   - Quantity of personal data records (>100 individuals = higher risk for breach notification)

2. **Immediate containment** (if media unencrypted or CONFIDENTIAL data):
   - IT Operations: Remotely wipe media if remote wipe capability exists (e.g., mobile device, cloud-synced media)
   - IT Operations: Disable associated access credentials if media contained credentials (API keys, passwords)
   - IT Operations: Deactivate media serial number from approved media list (prevent reconnection if found)

**Within 1 hour:**

3. **Incident classification**:
   - CONFIDENTIAL + unencrypted = Critical severity (assume data breach, initiate breach response per A.5.24–28)
   - CONFIDENTIAL + encrypted = High severity (assess key security, potential for decryption)
   - INTERNAL + unencrypted = High severity
   - INTERNAL + encrypted OR PUBLIC = Medium/Low severity

4. **Escalation and investigation**:
   - CISO notified (Critical/High severity)
   - DPO notified (if personal data involved — assess breach notification under nFADP Art. 24 / GDPR Art. 33)
   - Investigation: How was media lost? Circumstances, timeline, last known location

**Within 24 hours:**

5. **Breach notification assessment**:
   - If nFADP/GDPR breach criteria met: Notify FDPIC/supervisory authority per applicable timeline (nFADP: as soon as possible; GDPR: 72 hours)
   - If contractual notification required (customer DPA): Notify customers per contract terms
   - Document breach decision in Incident Log

6. **Remediation**:
   - Replace media if user still requires removable media for business
   - Reissue encrypted media if lost media was unencrypted
   - Update [Asset Management System]: Mark media as "Lost" with incident reference
   - User coaching/training if loss due to negligence

**Post-incident:**
- Root cause analysis: Why was media lost? Process gap? Policy violation?
- Preventive actions: If pattern of losses (e.g., travel-related), implement additional controls
- Reported in quarterly Management Review: Lost/stolen media statistics, trends, remediation actions

---

## Evidence for This Policy

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | Removable media inventory (complete register with encryption status) | Asset Management | Continuous; quarterly audit | Life of asset record |
| 2 | Media authorisation records (manager approvals for removable media use) | Line Managers | Per authorisation event | 3 years |
| 3 | CONFIDENTIAL data transfer logs (date, user, media ID, data description, recipient) | IT Operations | Per transfer event | 7 years |
| 4 | Quarterly media audit reports (reconciliation results, discrepancies, resolutions) | Asset Management | Quarterly | 3 years |
| 5 | Equipment disposal records (asset tag, classification, method, date, operator) | IT Operations | Per disposal event | 7 years |
| 6 | Certificates of destruction from [Destruction Vendor] | Procurement | Per destruction event | 7 years |
| 7 | Secure wipe verification logs (tool output per asset) | IT Operations | Per wipe event | 7 years |
| 8 | Chain of custody records for media transport | IT Operations | Per transport event | 7 years |
| 9 | USB port and removable media connection logs (endpoint telemetry) | IT Operations | Continuous | 12 months |
| 10 | Confidential waste bin collection and shredding records | Facilities Manager | Per collection event | 3 years |
| 11 | Vendor due diligence records for destruction service providers | Procurement | Annual review | Duration of contract + 2 years |
| 12 | Policy acknowledgement records (media handling training) | HR / CISO | Annual | Duration of employment + 1 year |
| 13 | Lost/stolen media incident reports (severity, containment, breach assessment) | CISO | Per incident | 7 years |
| 14 | Media authorisation expiration and renewal records | IT Operations | Per event | Duration of assignment + 1 year |
| 15 | Approved media list version history and review records | IT Operations / CISO | Annual + triggered | 3 years |

---

## Optional: Payment Card Data Controls (PCI DSS)

*Applicable only if payment card data is processed and PCI scope exists.*

If PCI DSS scope applies, the following additional requirements shall be met:

- Media containing cardholder data shall be physically destroyed when no longer needed for business or legal reasons (PCI DSS Requirement 9.4).
- An inventory of media containing cardholder data shall be maintained and reconciled at least annually (PCI DSS Requirement 9.4.1).
- Secure disposal of cardholder data media shall be documented with destruction certificates (PCI DSS Requirement 9.4.7).
- Internal and external transport of media containing cardholder data shall use secure courier and be logged (PCI DSS Requirement 9.4.3–9.4.4).

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to:

- Quarterly removable media audits per risk-based sampling methodology (100% annual coverage).
- Monthly review of USB connection logs and endpoint protection alerts for unauthorised media.
- Semi-annual review of disposal records against the asset register to identify unaccounted disposals.
- Annual review of [Destruction Vendor] contracts, certifications, and destruction certificate completeness.
- Annual verification that approved media list, sanitisation tools, and procedures remain current.
- Internal and external audits, and feedback to the policy owner.

**Governance Metrics**:

| Metric | Target |
|--------|--------|
| Registered media with encryption compliance | 100% |
| Media losses or thefts (per quarter) | 0 |
| Disposals with certificate (CONFIDENTIAL) | 100% |
| Secure wipe verification completed (per disposal) | 100% |
| Quarterly audit completion rate | 100% |
| Overdue media returns | < 3 |
| Destruction certificate serial number match rate | 100% |

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO in advance, with documented risk acceptance, compensating controls, and a defined review date not exceeding 6 months. Exceptions shall be reported to the Management Review Team.

Permitted exceptions include:

- Unencrypted removable media for specific operational requirements where encryption is technically incompatible, with enhanced physical controls and time-limited approval.
- Extended retention beyond standard periods with documented business or legal justification and annual review.
- Alternative transportation methods with risk acceptance signed by the CISO.

Exceptions shall not be granted for:

- CONFIDENTIAL data on unencrypted removable media without any compensating controls.
- Personal media for organisation CONFIDENTIAL or INTERNAL data.
- Disposal of CONFIDENTIAL media without verification or certificate.
- Bypassing quarterly media audit requirements.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

Improper handling or disposal of media containing personal data may additionally constitute a breach of Swiss nFADP, potentially resulting in regulatory investigation by the Federal Data Protection and Information Commissioner (FDPIC) and, where applicable, EU data protection authorities under GDPR.

Loss of unencrypted media containing personal data shall be reported as a data breach and assessed under the organisation's incident management procedures and applicable breach notification requirements.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider:

- Changes to sanitisation standards (including NIST SP 800-88 updates, IEEE 2883 revisions, DIN 66399 amendments)
- New storage technologies (e.g., NVMe, persistent memory, emerging flash architectures)
- Changes to Swiss nFADP, GDPR, or other applicable regulations
- Audit findings and disposal incidents
- Feedback from quarterly media audits and vendor reviews
- Changes to the organisation's information classification scheme

---

# Areas of the ISO 27001 Standard Addressed

Storage Media Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.1 Actions to address risks | 5.9 Inventory of information and other associated assets |
| Clause 7.3 Awareness | 5.10 Acceptable use of information and other associated assets |
| Clause 7.5 Documented information | 5.12 Classification of information |
| Clause 8.1 Operational planning and control | 5.13 Labelling of information |
| Clause 10.2 Nonconformity and corrective action | **7.10 Storage media** |
| | 7.14 Secure disposal or re-use of equipment |
| | 8.10 Information deletion |
| | 8.24 Use of cryptography |

# Regulatory Framework

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures; rendering personal data unrecoverable before disposal |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security including physical media protection |
| EU GDPR (where applicable) | Art. 5(1)(f) — Integrity and confidentiality; Art. 17 — Right to erasure; Art. 32 — Security of processing |
| ISO/IEC 27001:2022 | Annex A Control 7.10 — Storage media lifecycle management |
| ISO/IEC 27002:2022 | Section 7.10 — Implementation guidance for storage media |
| NIST SP 800-88 Rev. 2 | Guidelines for media sanitisation — Clear, Purge, Destroy (September 2025; supersedes Rev. 1) |
| IEEE 2883:2022 | Standard for sanitizing storage — technical methods for drives and media |
| DIN 66399 | Destruction of data carriers — security levels (P/F/O/T/H/E categories, levels 1–7) and protection classes |

---

<!-- QA_VERIFIED: 2026-02-07 -->
