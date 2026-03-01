<!-- ISMS-CORE:POLICY:ISMS-POL-A.7.10:framework:POL:a.7.10 -->
**ISMS-POL-A.7.10 — Storage Media**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Storage Media |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.7.10 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: IT Operations Manager
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.12-13 (Information Classification and Labelling)
- ISMS-POL-A.7.6-7-14 (Secure Areas and Media Handling)
- ISMS-POL-A.8.10 (Information Deletion)
- ISMS-IMP-A.7.10.1-UG/TG (Storage Media Inventory)
- ISMS-IMP-A.7.10.2-UG/TG (Media Handling Procedures)
- ISMS-IMP-A.7.10.3-UG/TG (Media Lifecycle Tracking)
- ISO/IEC 27001:2022 Control A.7.10

---

## Executive Summary

This policy establishes [Organisation]'s requirements for managing storage media throughout its lifecycle, from acquisition through use, transportation, and disposal.

**Scope**: This policy applies to all storage media used by [Organisation], including removable media, fixed storage, cloud storage, and paper documents containing sensitive information.

**Purpose**: Define requirements for secure management of storage media in accordance with the organisation's classification scheme and handling requirements. This policy establishes WHAT storage media requirements apply and WHO is responsible. Implementation procedures (HOW) are documented in ISMS-IMP-A.7.10.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, PCI DSS v4.0.1, DORA) apply where [Organisation]'s business activities trigger applicability.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Control A.7.10**

**ISO/IEC 27001:2022 Annex A.7.10 - Storage Media**

> *Storage media should be managed through their life cycle of acquisition, use, transportation and disposal in accordance with the organisation's classification scheme and handling requirements.*

**Control Objectives**:

- Ensure only authorised disclosure, modification, removal, or destruction of information on storage media
- Protect storage media throughout its lifecycle
- Maintain accountability for media containing sensitive information
- Prevent data leakage through improper media handling

**Control Type**: Preventive
**Control Category**: Physical

**This Policy Addresses**:

- Removable media authorisation and registration
- Media use requirements and encryption
- Transportation and chain of custody
- Storage requirements by classification
- Disposal and re-use procedures

## What This Policy Does

This policy:

- **Defines** storage media management requirements throughout lifecycle
- **Establishes** media handling requirements by information classification
- **Specifies** transportation and chain of custody requirements
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Define information classification scheme** (see ISMS-POL-A.5.12-13)
- **Specify secure disposal methods** (see ISMS-POL-A.7.6-7-14)
- **Detail information deletion procedures** (see ISMS-POL-A.8.10)
- **Provide media procurement specifications** (see ISMS-IMP-A.7.10)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite technology changes
- Flexibility for different media types and vendors
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- Digital storage media: hard drives (HDD/SSD), USB drives, SD cards, optical media (CD/DVD), backup tapes, network storage
- Physical documents: paper documents, microfilm, microfiche
- Cloud storage: cloud backup storage, cloud file storage (managed per A.5.19-23)
- Lifecycle phases: acquisition, use, transportation, storage, disposal
- Personnel: all employees, contractors, and third parties handling storage media

**Out of Scope**:

- Information classification scheme (covered by A.5.12-13)
- Secure disposal methods (covered by A.7.14)
- Third-party cloud storage contracts (covered by A.5.19-23)

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG** | All personal data processing | Article 8 - Technical measures; Article 6 - Data minimisation |
| **ISO/IEC 27001:2022** | Certification scope | Control A.7.10 |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Requirements |
|-----------|-------------------|--------------|
| **EU GDPR** | Processing EU personal data, EU establishment, or offering services to EU | Art. 5(1)(f) integrity/confidentiality; Art. 17 right to erasure |
| **PCI DSS v4.0.1** | Payment card processing | Requirement 9.4 - Media protection |
| **FINMA** | Swiss regulated financial institution | Data protection and retention requirements |
| **DORA** | EU financial services entity | ICT asset management |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- NIST SP 800-88 Rev. 2 (Media Sanitization Guidelines)
- ISO/IEC 27040 (Storage security)
- CIS Controls v8.1 (Control 3 - Data Protection)
- Industry best practices for media management

**Compliance Determination**: [Organisation] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent requirements apply where multiple regulations overlap.

---

# Policy Statements

## Storage Media Policy

[Organisation] SHALL establish and implement suitable procedures, technical controls, and organisation-wide policies regarding the use of storage media according to the organisation's classification scheme and data handling requirements.

**Policy Statement**:

- All storage media containing organisation information SHALL be managed per this policy
- Removable media use SHALL be restricted and controlled
- Media containing sensitive information SHALL be protected during transport
- Disposal SHALL ensure data cannot be recovered

## Removable Media Management

### Authorisation and Registration

**Authorisation Requirements**:

- Use of removable media SHALL be authorised by line management
- Authorisation SHALL specify permitted use cases and data classifications
- Personal removable media SHALL NOT be used for organisation data
- Organisation-issued media SHALL be registered in the asset management system

**Approved Media**:

- Only organisation-approved and encrypted removable media SHALL be used
- Hardware-encrypted USB devices SHALL be used for CONFIDENTIAL data
- Media SHALL be procured through approved suppliers
- Bring-your-own media SHALL be prohibited for CONFIDENTIAL/INTERNAL data

### Use Requirements

**Data Transfer**:

- Transfer of CONFIDENTIAL data to removable media requires management approval
- Data SHALL be encrypted before transfer to removable media
- Transfer logs SHALL be maintained for CONFIDENTIAL data
- Data SHALL be removed from media when no longer required

**Access Control**:

- Media SHALL be password-protected or encrypted
- Media SHALL not be left unattended
- Media SHALL be stored securely when not in use
- Media contents SHALL be scanned for malware before use

### Media Inventory

**Registration**:

- All removable media SHALL be registered in the asset inventory
- Registration SHALL include: media type, capacity, assigned user, purpose, classification level
- Quarterly inventory audits SHALL reconcile 100% of registered removable media items against asset records; reconciliation SHALL verify physical location, encryption status, and assigned user. Mismatches SHALL be escalated within 1 business day per incident response procedures

## Transportation of Storage Media

### Secure Transportation

**Courier Requirements**:

- CONFIDENTIAL media SHALL use approved secure couriers only
- Chain of custody SHALL be documented
- Recipient SHALL verify and acknowledge receipt
- Tamper-evident packaging SHALL be used

**Personal Transport**:

- Media SHALL be carried in hand luggage during travel (not checked baggage)
- Media SHALL be encrypted
- Media SHALL not be left unattended during transport
- Transport through high-risk areas SHALL be avoided

### Tracking and Accountability

**Chain of Custody**:

- Transfer of media between individuals SHALL be documented
- Documentation SHALL include: date, from, to, media identifier, purpose
- Acknowledgment of receipt SHALL be obtained

## Storage Requirements

### Physical Storage

**Secure Storage**:

- Media containing CONFIDENTIAL information SHALL be stored in locked cabinets or safes
- Storage locations SHALL have appropriate access controls
- Environmental conditions SHALL protect media integrity (temperature, humidity, magnetic fields)
- Media SHALL be stored separately from systems (for backup media)

**Retention Periods**:

- Media SHALL be retained per data retention requirements defined in the Retention Schedule (ISMS-REG-RETENTION)
- Retention periods for specific data types and media categories are documented in ISMS-REG-RETENTION
- Media SHALL be disposed of when retention period expires; backup tapes and cloud snapshots SHALL be included in retention schedule coverage with documented disposal/deletion triggers

### Protection Requirements by Classification

| Classification | Storage Requirement | Encryption | Access Control |
|----------------|-------------------|------------|----------------|
| **CONFIDENTIAL** | Locked safe/cabinet | Mandatory (per ISMS-POL-A.8.24) | Named individuals only |
| **INTERNAL** | Locked cabinet | Recommended (per ISMS-POL-A.8.24) | Authorised staff |
| **PUBLIC** | Standard storage | Optional | General access |

**Encryption Implementation**: Platform-specific encryption mechanisms (BitLocker/FileVault for endpoints, LUKS for Linux, S3 SSE-KMS for cloud object storage, storage-array encryption, tape encryption) are defined in ISMS-IMP-A.7.10.2 and SHALL comply with cryptographic standards in ISMS-POL-A.8.24.

## Disposal of Storage Media

### Disposal Requirements

Disposal and sanitisation SHALL ensure information cannot be recovered, using organisation-approved sanitisation/destruction methods appropriate to the media type and information classification level of data ever stored on the media.

**Disposal Outcome Requirements by Classification**:

| Classification | Required Outcome | Verification |
|----------------|------------------|--------------|
| **CONFIDENTIAL** | Unrecoverable by any means | Certificate of destruction from approved provider; witnessed destruction for highly sensitive data |
| **INTERNAL** | Unrecoverable without specialist equipment | Verification of successful erasure documented |
| **PUBLIC** | Standard deletion acceptable | Documentation of disposal |

**Approved Methods**: Specific sanitisation and destruction methods per media type (HDD, SSD, tape, optical, mobile devices) are defined in ISMS-IMP-A.7.10.3, aligned with NIST SP 800-88 Rev. 2 principles. Physical disposal requirements are addressed in ISMS-POL-A.7.6-7-14.

### Internal Re-Use

Before media is re-used within the organisation:

- All sensitive data SHALL be securely erased
- Erasure SHALL be verified
- Media SHALL be inspected for physical integrity
- Asset records SHALL be updated

### External Disposal

Media being disposed of externally SHALL:

- Have all data securely erased or be physically destroyed
- Be disposed of through approved disposal providers
- Have disposal documented with certificates retained
- Never be sold or donated with recoverable data

## Paper Documents and Physical Media

### Handling Requirements

**Paper Documents**:

- Documents SHALL be classified and handled per classification scheme
- CONFIDENTIAL documents SHALL be stored in locked cabinets
- Documents SHALL be collected immediately from printers
- Clean desk policy SHALL be followed

### Disposal

**Secure Destruction**:

- CONFIDENTIAL paper documents SHALL be cross-cut shredded
- INTERNAL paper documents SHALL be shredded
- Shredding SHALL be performed on-site or by approved contractors
- Mass destruction SHALL be witnessed or certified

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Storage Media Responsibilities |
|------|--------------------------------|
| **Executive Management** | Approve policy, allocate resources for media security |
| **CISO** | Policy ownership, standards, compliance oversight |
| **IT Operations** | Media procurement, encryption deployment, disposal execution |
| **Line Managers** | Authorise media use, ensure team compliance |
| **Asset Management** | Media inventory, tracking, lifecycle management |
| **All Personnel** | Handle media per policy, report losses immediately |

## Escalation Path

- Media loss/theft: Employee → Line Manager + IT Operations (immediate) → CISO
- Media policy questions: Employee → IT Operations → CISO

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| Removable media audit | Quarterly | IT Operations | Inventory reconciliation |
| Media encryption compliance | Monthly | IT Security | Endpoint management reports |
| Disposal process audit | Semi-annual | Internal Audit | Disposal records, certificates |
| Transportation security review | Annual | CISO | Process review |

**Governance Metrics**:

- Registered media with encryption (target: 100%)
- Media losses (target: 0)
- Disposal with certificates (target: 100% for CONFIDENTIAL)
- Overdue media returns (target: <3)
- Media audit completion (target: 100%)

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Media incidents, technology changes, audit findings, regulatory updates
- **Reviewers**: CISO, IT Operations, Asset Management
- **Approval**: Executive Management

## Exception Management

**Permitted Exceptions**:

- Unencrypted media for specific operational requirements (with enhanced controls)
- Extended retention beyond standard periods (with documented justification)
- Alternative transportation methods (with risk acceptance)

**Exception Process**:

1. Document business justification
2. Risk assessment including data classification impact
3. CISO approval with compensating controls
4. Time-limited approval (maximum 6 months)
5. Documentation in exception register

**Not Permissible**:

- CONFIDENTIAL data on unencrypted removable media without compensating controls
- Personal media for organisation CONFIDENTIAL data
- Disposal without verification for CONFIDENTIAL media

All exceptions SHALL be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

## Corrective Action Linkage

Nonconformities related to this policy (e.g., lost media, unregistered media, improper disposal, missing encryption) SHALL be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organisation]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Media loss and theft risks inform handling requirements
- Data leakage risks addressed through encryption and controls
- Risk treatment plans document media protection controls

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Control A.7.10 applicability justified in [Organisation]'s SoA
- Implementation status tracked and reported

**Related Controls**:

| Control | Relationship |
|---------|--------------|
| **A.5.9** | Asset inventory including storage media |
| **A.5.12-13** | Information classification driving media handling requirements |
| **A.7.6-7-14** | Secure areas, clear desk, secure disposal |
| **A.8.10** | Information deletion requirements |
| **A.8.24** | Cryptography for media encryption |

**Stacked Control Integration**:

A.7.10 (Storage Media) stacks with related controls:

| Stacked Control | Integration Point | A.7.10 Contribution |
|-----------------|-------------------|---------------------|
| **A.5.12-13** (Classification) | Handling requirements | Classification drives A.7.10 protection levels |
| **A.7.6-7-14** (Secure Areas/Disposal) | End-of-life | A.7.10 manages lifecycle; A.7.14 handles disposal |
| **A.8.24** (Cryptography) | Encryption | A.7.10 mandates encryption; A.8.24 specifies standards |

Assessment of A.7.10 should reference stacked control assessments for complete coverage.

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.7.10 Suite):

| Document ID | Title | Purpose |
|-------------|-------|---------|
| **ISMS-IMP-A.7.10.1-UG/TG** | Media Inventory Procedures | Registration and tracking procedures |
| **ISMS-IMP-A.7.10.2-UG/TG** | Media Handling Procedures | Use and transportation procedures |
| **ISMS-IMP-A.7.10.3-UG/TG** | Media Disposal Procedures | Disposal and destruction procedures |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Required Stage 1 evidence includes:

- This policy document (ISMS-POL-A.7.10 v1.0)
- Recorded approval by CISO, IT Operations Manager, Executive Management
- Evidence of communication to relevant roles
- Removable media requirements documented (Removable Media Management)
- Transportation requirements documented (Transportation of Storage Media)
- Disposal requirements documented (Disposal of Storage Media)
- Roles and responsibilities assigned (Roles and Responsibilities)

Evidence presence and status is tracked in the ISMS Evidence Register.

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Media inventory with encryption status
- Media authorisation records
- Transportation chain of custody records
- Disposal records with certificates
- Media audit reports with reconciliation
- Incident reports for lost/stolen media
- Training records for media handling

---

# Definitions

| Term | Definition |
|------|------------|
| **Storage Media** | Any device or material capable of storing data, including digital and physical formats |
| **Removable Media** | Portable storage devices that can be removed from systems (USB drives, external drives, optical discs) |
| **Secure Overwriting** | Process of writing patterns over stored data to prevent recovery |
| **Degaussing** | Using powerful magnetic fields to erase data from magnetic storage media |
| **Chain of Custody** | Documented chronological record of handling, transfer, and storage of media |
| **Certificate of Destruction** | Written confirmation from an approved provider that media has been destroyed |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **IT Operations Manager** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for storage media management. Implementation procedures are documented in ISMS-IMP-A.7.10 (UG/TG).*

<!-- QA_VERIFIED: 2026-03-01 -->
