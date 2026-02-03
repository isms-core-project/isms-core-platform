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
- ISMS-IMP-A.7.10 (Implementation Guidance)
- ISO/IEC 27001:2022 Control A.7.10

---

## Executive Summary

This policy establishes [Organisation]'s requirements for managing storage media throughout its lifecycle, from acquisition through use, transportation, and disposal.

**Purpose**: Define requirements for secure management of storage media in accordance with the organisation's classification scheme and handling requirements. This policy establishes WHAT storage media requirements apply and WHO is responsible. Implementation procedures (HOW) are documented in ISMS-IMP-A.7.10.

**Scope**: All storage media used by [Organisation], including removable media, fixed storage, cloud storage, and paper documents containing sensitive information.

---

# Scope & Control Alignment

## ISO/IEC 27001:2022 Control A.7.10

> *Storage media should be managed through their life cycle of acquisition, use, transportation and disposal in accordance with the organisation's classification scheme and handling requirements.*

**Control Objective**: Ensure only authorised disclosure, modification, removal, or destruction of information on storage media.

**Control Type**: Preventive
**Control Category**: Physical

## Policy Scope

**This policy applies to**:

| Category | Scope |
|----------|-------|
| **Digital Storage Media** | Hard drives (HDD/SSD), USB drives, SD cards, optical media (CD/DVD), backup tapes, network storage |
| **Physical Documents** | Paper documents, microfilm, microfiche |
| **Cloud Storage** | Cloud backup storage, cloud file storage (managed per A.5.19-23) |
| **Lifecycle Phases** | Acquisition, use, transportation, storage, disposal |
| **Personnel** | All employees, contractors, and third parties handling storage media |

## Regulatory Applicability

**Tier 1 - Mandatory Compliance** (All operations):

| Regulation | Key Requirements |
|------------|------------------|
| **Swiss nDSG** | Article 8 - Technical measures; Article 6 - Data minimisation |
| **EU GDPR** | Article 5(1)(f) - Integrity and confidentiality; Article 17 - Right to erasure |
| **ISO/IEC 27001:2022** | Control A.7.10 |

**Tier 2 - Conditional Applicability** (Triggered by business activities):

| Regulation | Trigger | Requirement |
|-----------|---------|-------------|
| **PCI DSS v4.0** | Payment card processing | Requirement 9.4 - Media protection |
| **FINMA** | Swiss financial institution | Data protection and retention requirements |
| **DORA** | EU financial services | ICT asset management |

---

# Policy Statements

## Storage Media Policy

[Organisation] should establish and implement suitable procedures, technical controls, and organisation-wide policies regarding the use of storage media according to the organisation's classification scheme and data handling requirements.

**Policy Statement**:
- All storage media containing organisation information should be managed per this policy
- Removable media use should be restricted and controlled
- Media containing sensitive information should be protected during transport
- Disposal should ensure data cannot be recovered

## Removable Media Management

### Authorisation and Registration

**Authorisation Requirements**:
- Use of removable media should be authorised by line management
- Authorisation should specify permitted use cases and data classifications
- Personal removable media should not be used for organisation data
- Organisation-issued media should be registered in the asset management system

**Approved Media**:
- Only organisation-approved and encrypted removable media should be used
- Hardware-encrypted USB devices should be used for CONFIDENTIAL data
- Media should be procured through approved suppliers
- Bring-your-own media should be prohibited for CONFIDENTIAL/INTERNAL data

### Use Requirements

**Data Transfer**:
- Transfer of CONFIDENTIAL data to removable media requires management approval
- Data should be encrypted before transfer to removable media
- Transfer logs should be maintained for CONFIDENTIAL data
- Data should be removed from media when no longer required

**Access Control**:
- Media should be password-protected or encrypted
- Media should not be left unattended
- Media should be stored securely when not in use
- Media contents should be scanned for malware before use

### Media Inventory

**Registration**:
- All removable media should be registered in the asset inventory
- Registration should include: media type, capacity, assigned user, purpose, classification level
- Periodic inventory audits should verify media location and status

## Transportation of Storage Media

### Secure Transportation

**Courier Requirements**:
- CONFIDENTIAL media should use approved secure couriers only
- Chain of custody should be documented
- Recipient should verify and acknowledge receipt
- Tamper-evident packaging should be used

**Personal Transport**:
- Media should be carried in hand luggage during travel (not checked baggage)
- Media should be encrypted
- Media should not be left unattended during transport
- Transport through high-risk areas should be avoided

### Tracking and Accountability

**Chain of Custody**:
- Transfer of media between individuals should be documented
- Documentation should include: date, from, to, media identifier, purpose
- Acknowledgment of receipt should be obtained

## Storage Requirements

### Physical Storage

**Secure Storage**:
- Media containing CONFIDENTIAL information should be stored in locked cabinets or safes
- Storage locations should have appropriate access controls
- Environmental conditions should protect media integrity (temperature, humidity, magnetic fields)
- Media should be stored separately from systems (for backup media)

**Retention Periods**:
- Media should be retained per data retention requirements
- Retention periods should be documented in data retention schedule
- Media should be disposed of when retention period expires

### Protection Requirements by Classification

| Classification | Storage Requirement | Encryption | Access Control |
|----------------|-------------------|------------|----------------|
| **CONFIDENTIAL** | Locked safe/cabinet | Mandatory (AES-256) | Named individuals only |
| **INTERNAL** | Locked cabinet | Recommended | Authorised staff |
| **PUBLIC** | Standard storage | Optional | General access |

## Disposal of Storage Media

### Disposal Requirements

Disposal methods should ensure data cannot be recovered, appropriate to the classification level of data ever stored on the media:

**CONFIDENTIAL Data**:
- Physical destruction (shredding, degaussing, incineration)
- Destruction by approved third-party service provider
- Certificate of destruction required
- Witnessed destruction for highly sensitive data

**INTERNAL Data**:
- Secure overwriting (minimum 3 passes) OR physical destruction
- Verification of successful erasure
- Documentation of disposal method

**PUBLIC Data**:
- Standard deletion acceptable
- Format and disposal through appropriate channels

### Internal Re-Use

Before media is re-used within the organisation:
- All sensitive data should be securely erased
- Erasure should be verified
- Media should be inspected for physical integrity
- Asset records should be updated

### External Disposal

Media being disposed of externally should:
- Have all data securely erased or be physically destroyed
- Be disposed of through approved disposal providers
- Have disposal documented with certificates retained
- Never be sold or donated with recoverable data

## Paper Documents and Physical Media

### Handling Requirements

**Paper Documents**:
- Documents should be classified and handled per classification scheme
- CONFIDENTIAL documents should be stored in locked cabinets
- Documents should be collected immediately from printers
- Clean desk policy should be followed

### Disposal

**Secure Destruction**:
- CONFIDENTIAL paper documents should be cross-cut shredded
- INTERNAL paper documents should be shredded
- Shredding should be performed on-site or by approved contractors
- Mass destruction should be witnessed or certified

---

# Roles & Responsibilities

| Role | Accountability |
|------|----------------|
| **Executive Management** | Approve policy, allocate resources for media security |
| **CISO** | Policy ownership, standards, compliance oversight |
| **IT Operations** | Media procurement, encryption deployment, disposal execution |
| **Line Managers** | Authorise media use, ensure team compliance |
| **Asset Management** | Media inventory, tracking, lifecycle management |
| **All Personnel** | Handle media per policy, report losses immediately |

**Escalation Path**:
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

**Governance Metrics (Quarterly Dashboard)**:

| Metric | Target | Measurement |
|--------|--------|-------------|
| Registered media with encryption | 100% | Asset inventory + encryption status |
| Media losses | 0 | Incident records |
| Disposal with certificates | 100% (CONFIDENTIAL) | Disposal records |
| Overdue media returns | <3 | Asset tracking |
| Media audit completion | 100% | Audit records |

## Exception Management

Storage media policy exceptions require:
- Documented business justification
- Risk assessment including data classification impact
- Compensating controls (e.g., enhanced encryption, additional logging)
- CISO approval
- Time-limited approval (maximum 6 months)
- Quarterly review for continued necessity

---

# ISMS Integration

## Statement of Applicability

| Control | Status | Implementation Reference |
|---------|--------|-------------------------|
| **A.7.10 - Storage Media** | Applicable | This policy, ISMS-IMP-A.7.10 |

## Related Controls

| Control | Relationship |
|---------|--------------|
| **A.5.9** | Asset inventory including storage media |
| **A.5.12-13** | Information classification driving media handling requirements |
| **A.7.6-7-14** | Secure areas, clear desk, secure disposal |
| **A.8.10** | Information deletion requirements |
| **A.8.24** | Cryptography for media encryption |

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

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

- ✅ This policy document (ISMS-POL-A.7.10 v1.0)
- ✅ Approval signatures from CISO, IT Operations Manager, Executive Management
- ✅ Removable media requirements documented (Section 2.2)
- ✅ Transportation requirements documented (Section 2.3)
- ✅ Disposal requirements documented (Section 2.5)
- ✅ Roles and responsibilities assigned (Section 3)

**Stage 2 (Operational Effectiveness) Evidence:**

**Evidence Repository and Generation**:

| Evidence Type | Repository Location | Generation Method | Owner | Retention |
|---------------|-------------------|-------------------|-------|-----------|
| Media inventory | [Asset Management System] | Continuous tracking | Asset Management | Active + 1 year |
| Media authorisations | [Service Desk System] | Per request | Line Managers | 3 years |
| Transport chain of custody | [GRC Platform] - Evidence Library | Per transport event | Sender/Receiver | 3 years |
| Disposal records | [Asset Management System] | Per disposal event | IT Operations | 7 years |
| Destruction certificates | [GRC Platform] - Evidence Library | From disposal vendors | IT Operations | 7 years |
| Media audit reports | [GRC Platform] - Compliance Module | Quarterly audits | IT Operations | 3 years |

**Evidence Accessibility**: All evidence SHALL be accessible to auditors upon request within 2 business days.

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

*This policy establishes [Organisation]'s requirements for storage media management. Implementation procedures are documented in ISMS-IMP-A.7.10.*

<!-- QA_VERIFIED: [Date] -->
