<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.20-22:privacy:POL:a.3.20-22 -->
**PRIV-POL-A.3.20-22 — Physical Media and Endpoint Security**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Physical Media and Endpoint Security |
| **Document Type** | Policy |
| **Document ID** | PRIV-POL-A.3.20-22 |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial policy for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Data Protection Officer (DPO)
- Secondary: Chief Information Security Officer (CISO)
- Legal: Legal/Compliance Officer
- Final Authority: Executive Management

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- PRIV-POL-01 (Privacy Governance and Decision-Making Framework)
- PRIV-IMP-A.3.20-22-UG (Physical Media and Endpoint Security — User Guide)
- PRIV-IMP-A.3.20-22-TG (Physical Media and Endpoint Security — Technical Guide)
- ISMS-POL-A.7.8-10 (Clear Desk, Media and Equipment — ISMS parallel)
- ISMS-POL-A.8.1 (User Endpoint Devices — ISMS parallel)
- PRIV-POL-A.3.5-7 (Information Classification and Transfer — classification scheme applied here)
- ISO/IEC 27701:2025 Controls A.3.20, A.3.21, A.3.22
- ISO/IEC 27701:2025 Annex B (Implementation guidance B.3.20, B.3.21, B.3.22)
- GDPR Article 32 (Security of processing — includes protection of data on endpoints and media)
- CH FADP Article 7 (Technical and organisational measures)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for the lifecycle management of storage media containing PII, secure disposal or re-use of equipment containing PII, and protection of PII on user endpoint devices — in accordance with ISO/IEC 27701:2025 Controls A.3.20, A.3.21, and A.3.22.

**Scope**: All storage media containing PII throughout its lifecycle; all equipment containing storage media with PII at end-of-life or re-assignment; all user endpoint devices on which PII is stored, processed, or accessible.

**Purpose**: Define organisational requirements for:

- PII storage media lifecycle management aligned to the classification scheme (A.3.20)
- Secure verification, erasure, and disposal of equipment with PII storage media (A.3.21)
- Protection of PII on user endpoint devices (A.3.22)

This policy establishes **WHAT** media lifecycle, equipment disposal, and endpoint protection requirements apply to PII, **WHO** is responsible, and **WHEN** controls must be applied. Implementation procedures (**HOW**) are documented in PRIV-IMP-A.3.20-22-UG and PRIV-IMP-A.3.20-22-TG.

**Role Applicability**: This policy applies to the organisation acting as **both PII Controller and PII Processor**. Controls A.3.20, A.3.21, and A.3.22 are shared controls (Table A.3) and apply regardless of processing role.

**Combined Control Rationale**: A.3.20 (storage media), A.3.21 (equipment disposal), and A.3.22 (endpoints) address PII at rest in physical form and on devices. They close the physical exposure window for PII: media lifecycle controls prevent mishandling during active use; disposal controls prevent residual PII exposure after use; endpoint controls protect PII on the devices most likely to be lost, stolen, or misused. Together they form the physical and device layer of PII protection.

---

# Scope and Applicability

## ISO/IEC 27701:2025 Control Statements

**Control A.3.20 — Storage media**
> *Storage media with PII shall be managed through its life cycle of acquisition, use, transportation and disposal in accordance with the organization's classification scheme and handling requirements.*

**Control A.3.21 — Secure disposal or re-use of equipment**
> *Items of equipment containing storage media with PII shall be verified to ensure that any sensitive data and licensed software has been removed or securely overwritten prior to disposal or re-use.*

**Control A.3.22 — User endpoint devices**
> *PII stored on, processed by or accessible via user endpoint devices shall be protected.*

## What This Policy Covers

**Storage Media (A.3.20)**:

- All storage media containing PII in any form: hard drives (internal and external), SSDs, USB drives, optical media, backup tapes, printed documents treated as media, microfilm, and any other medium capable of storing PII
- Lifecycle stages: acquisition, registration, use, transportation, re-use, and disposal

**Equipment Disposal and Re-use (A.3.21)**:

- All items of equipment containing storage media where PII may be present: servers, workstations, laptops, printers with internal storage, mobile devices, network equipment with stored configurations, and any device where PII storage is possible
- Disposal: retirement, sale, donation, recycling, destruction
- Re-use: reassignment within [Organisation] or to third parties

**User Endpoint Devices (A.3.22)**:

- Laptops, desktops, tablets, smartphones, and any other end-user device that stores, processes, or can access PII
- Both corporate-managed and BYOD devices where PII access is permitted

## What This Policy Does NOT Cover

- Physical security of premises and server rooms (see ISMS-POL-A.7.1-6)
- Information transfer procedures (see PRIV-POL-A.3.5-7)
- Logging and monitoring of endpoint activity (see PRIV-POL-A.3.23-31)
- Software asset management unrelated to PII (see ISMS-POL-A.8.8)

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 32 (appropriate technical measures for PII at rest — including media and endpoints); Article 5(1)(f) (integrity and confidentiality)
- **CH FADP**: Article 7 (technical measures — physical media protection and secure disposal)
- **ISO/IEC 27701:2025**: Controls A.3.20, A.3.21, A.3.22 (normative)

**Tier 3: Informational Reference** (per PRIV-POL-00):

- **ISO/IEC 27002:2022**: Implementation guidance for media handling (7.10), equipment disposal (7.14), and endpoint devices (8.1)
- **ISO/IEC 27701:2025 Annex B**: B.3.20, B.3.21, B.3.22

For complete regulatory categorisation, refer to PRIV-POL-00.

---

# Policy Statements: Storage Media Lifecycle for PII (A.3.20)

## Storage Media Requirements

[Organisation] SHALL manage storage media containing PII through its full lifecycle in accordance with the classification scheme defined in PRIV-POL-A.3.5-7 and the handling requirements below.

### Media Acquisition and Registration

- All removable storage media that will or may contain PII SHALL be registered in the Media Register upon acquisition
- Each registered media item SHALL have an assigned owner (accountable individual or team)
- Media classification SHALL be assigned at first use based on the PII content stored

### Media in Use

- Storage media containing PII SHALL be handled in accordance with the classification level assigned (per PRIV-POL-A.3.5-7 handling requirements)
- Media containing RESTRICTED PII (special category) SHALL be encrypted at all times
- Media containing CONFIDENTIAL PII SHALL be encrypted when transported outside secure premises
- Unattended media containing PII SHALL be secured (in locked storage or locked equipment) — consistent with clear desk requirements in PRIV-POL-A.3.17-19

### Media Transportation

- Transportation of media containing PII outside secure premises SHALL be logged, including destination, purpose, and return date
- Media containing CONFIDENTIAL PII transported externally SHALL use approved encrypted media or approved secure courier
- Loss of media during transport SHALL be reported immediately as a PII incident per PRIV-POL-A.3.11-12

### Media Disposal

- Storage media containing PII SHALL NOT be disposed of through standard waste streams
- Before disposal, PII SHALL be irreversibly removed by cryptographic erasure (for encrypted media) or secure overwrite (DoD 5220.22-M or equivalent standard), or physical destruction
- Disposal method SHALL be documented in the Media Register, including method used, date, and responsible person
- Third-party media destruction service disposal SHALL produce a certificate of destruction, retained as evidence

---

# Policy Statements: Secure Disposal and Re-use of Equipment with PII (A.3.21)

## Equipment Disposal and Re-use Requirements

Before any item of equipment containing storage media is disposed of or re-used (within or outside [Organisation]), [Organisation] SHALL verify that any PII has been removed or securely overwritten.

### Pre-Disposal Verification

All equipment scheduled for disposal or re-assignment SHALL undergo:

1. **Inventory check**: Confirm whether PII was or may have been stored on the device's storage media
2. **Data erasure**: Overwrite all storage using an approved erasure standard (per PRIV-IMP-A.3.20-22-TG), or physically destroy the storage media if erasure is not technically feasible
3. **Verification**: Confirm erasure was successful (post-erasure verification scan)
4. **Documentation**: Record the device asset ID, PII status (PII present/not confirmed), erasure method, verification outcome, date, and responsible person in the Disposal Register

### Erasure Standards

- **Software erasure**: Industry-standard overwrite (minimum DoD 5220.22-M single pass; NIST SP 800-88 Guidelines for Media Sanitisation provides authoritative guidance)
- **Cryptographic erasure**: Destruction of encryption keys for fully encrypted media (acceptable where full-disk encryption is confirmed active throughout the media's life)
- **Physical destruction**: Shredding or degaussing of storage media for RESTRICTED PII or where software erasure is technically impractical; destruction must be documented

### Re-use Within [Organisation]

Before reassignment of equipment to another user within [Organisation]:

- All PII from the previous user's profile SHALL be removed
- Device SHALL be imaged or reset to baseline configuration
- A new user access record SHALL be created; the previous user's access revoked per PRIV-POL-A.3.8-10

### Third-Party Disposal

Where equipment is disposed of through a third-party service (recycler, reseller, charity):

- Third party SHALL provide a certificate of data destruction before equipment leaves [Organisation]'s custody
- For equipment containing RESTRICTED PII, physical destruction of storage media is required (sale or donation not permitted without confirmed destruction)
- Certificate of destruction SHALL be retained in the Disposal Register for minimum 5 years

---

# Policy Statements: Protection of PII on User Endpoint Devices (A.3.22)

## Endpoint Device Requirements for PII

[Organisation] SHALL ensure that PII stored on, processed by, or accessible via user endpoint devices is protected.

### Minimum Endpoint Controls for PII

All corporate endpoint devices that store, process, or access PII SHALL be configured with:

- **Full-disk encryption**: Active and enforced; encryption key management per cryptography standards (PRIV-POL-A.3.23-31)
- **Screen lock**: Automatic lock after maximum idle period (configured per PRIV-IMP-A.3.20-22-TG)
- **Remote wipe capability**: Remote wipe or lock capability registered for the device; wipe capability tested at minimum annually
- **Device management enrolment**: Enrolled in corporate Mobile Device Management (MDM) or Unified Endpoint Management (UEM) solution where technically feasible
- **Up-to-date patching**: Operating system and security patches applied within the timeframes defined in ISMS-POL-A.8.8

### PII Storage Restrictions on Endpoints

- Bulk download or storage of PII on endpoint devices SHALL be limited to what is necessary for the job function
- Copying or storing large volumes of PII (bulk export from databases or applications) on local endpoints requires Data Owner approval
- RESTRICTED PII (special category) SHALL NOT be stored locally on endpoints except where operationally necessary with DPO notification; where stored locally, it shall be in an encrypted container with access controls separate from general file system access

### BYOD (Bring Your Own Device)

Where personal devices are permitted to access PII (BYOD policy applicable):

- BYOD devices SHALL be enrolled in MDM/containerisation solution that creates a managed PII workspace segregated from personal data
- Minimum controls (encryption, screen lock, remote wipe) SHALL apply to the managed workspace
- Organisation's right to remote wipe the managed workspace SHALL be agreed in writing before PII access is granted
- PII SHALL NOT be stored outside the managed workspace on BYOD devices

### Lost or Stolen Endpoint Devices

Loss or theft of an endpoint device containing or with access to PII SHALL be:

- Reported immediately to IT Security Team and DPO
- Treated as a suspected PII incident and managed per PRIV-POL-A.3.11-12
- Remote wipe initiated for the device within 4 hours of confirmed loss (or as soon as practical)

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Responsibilities for A.3.20–A.3.22 |
|------|-------------------------------------|
| **Data Protection Officer (DPO)** | Defines PII-specific media and endpoint requirements; notified of RESTRICTED PII on endpoints; reviews Disposal Register for adequacy; informed of lost/stolen devices |
| **CISO** | Sets technical standards for erasure, encryption, and endpoint management; configures MDM/UEM; maintains Disposal Register; investigates lost/stolen devices |
| **IT Security Team** | Implements encryption and MDM; executes media disposal and erasure; maintains Media Register and Disposal Register; initiates remote wipe on lost devices |
| **Data Owner** | Approves bulk PII download to endpoints; notified of PII-containing media disposal in their domain |
| **All Personnel** | Report lost or stolen devices immediately; comply with clear screen requirements; restrict PII to minimum necessary on endpoints |

---

# Evidence Requirements

The following evidence demonstrates operation of this policy:

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Media Register | Inventory of removable media with PII, owner, classification, and status | Current + 3 years |
| Media Transportation Log | Records of PII media transported outside secure premises | 3 years |
| Disposal Register | Equipment disposal records with PII status, erasure method, verification, and date | 5 years |
| Certificates of Destruction | Third-party destruction certificates for equipment containing PII | 5 years |
| Endpoint Encryption Status | Configuration reports confirming full-disk encryption on corporate devices | Current + 3 years |
| MDM/UEM Enrolment Records | Devices enrolled in endpoint management, including BYOD managed workspaces | Current + 3 years |
| Lost/Stolen Device Reports | Records of device loss/theft, remote wipe actions, and PII incident assessments | 3 years |

---

# Audit Considerations

Auditors verifying compliance with A.3.20, A.3.21, and A.3.22 should expect to find:

**For A.3.20 (Storage media)**:
- Media Register with PII media inventory
- Evidence that media containing PII is encrypted (especially RESTRICTED PII)
- Transportation log for media moved outside secure premises
- Disposal records including erasure method and verification

**For A.3.21 (Equipment disposal)**:
- Disposal Register with pre-disposal PII status checks
- Evidence of approved erasure method applied
- Certificates of destruction from third-party disposal services
- No disposal of RESTRICTED PII equipment without confirmed physical destruction

**For A.3.22 (Endpoint devices)**:
- Full-disk encryption configuration reports
- MDM/UEM enrolment records
- Remote wipe test evidence
- BYOD written agreements where personal devices access PII
- Lost/stolen device response records with remote wipe confirmation

---

<!-- QA_VERIFIED: [Date] -->
