# ISMS-POL-A.8.10-S1
## Information Deletion — Purpose, Scope, Definitions

---

**Document ID**: ISMS-POL-A.8.10-S1  
**Title**: Information Deletion — Purpose, Scope, Definitions  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial foundational document |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Privacy: Data Protection Officer (DPO)
- Compliance: Legal/Compliance Officer
- Technical: IT Operations Manager

**Distribution**: Security team, IT operations, data governance, legal, DPO office  
**Related Documents**: ISMS-POL-A.8.10 (Master), ISO/IEC 27002:2022 Control 8.10, NIST SP 800-88

---

## 1.1 Purpose

### 1.1.1 Policy Objective

This document establishes the purpose, scope, and key definitions for the organization's Information Deletion policy framework, implementing ISO/IEC 27001:2022 Annex A Control 8.10 (Information Deletion / Löschung von Informationen).

The policy framework aims to:

- **Prevent** unnecessary exposure of sensitive information by ensuring timely deletion
- **Comply** with legal, regulatory, and contractual data deletion obligations
- **Enforce** data retention policies through systematic deletion processes
- **Protect** data subject rights including the right to erasure (GDPR Art. 17, FADP)
- **Verify** deletion through documented evidence and audit trails
- **Manage** third-party and cloud provider deletion obligations

### 1.1.2 Control Alignment

This policy implements ISO/IEC 27001:2022 Annex A.8.10:

> **A.8.10 Information Deletion (Löschung von Informationen)**  
> *Information stored in information systems, devices or in any other storage media should be deleted when no longer required.*

The control recognizes that retained data beyond its useful life creates:
- Increased attack surface for data breaches
- Regulatory non-compliance risk (GDPR, FADP, sector regulations)
- Legal liability from unauthorized disclosure
- Storage cost inefficiency
- Increased scope for legal discovery/e-discovery
- Privacy violations for data subjects

### 1.1.3 Risk Management Context

Information deletion serves as a **preventive control** within the organization's data protection architecture. Effective deletion reduces risk by:

- Eliminating data that could be compromised in a breach
- Reducing regulatory exposure from non-compliant retention
- Honoring data subject rights and organizational commitments
- Limiting legal discovery scope in litigation
- Demonstrating privacy-by-design implementation

The organization recognizes that deletion must balance:
- **Security** — Removing data to reduce exposure
- **Compliance** — Meeting regulatory retention minimums AND maximums
- **Business** — Retaining data needed for legitimate operations
- **Legal** — Preserving data under litigation hold

---

## 1.2 Scope

### 1.2.1 In Scope

This policy framework applies to:

**Data Categories:**
- Personal data (PII) of employees, customers, partners, and other data subjects
- Confidential business information
- Financial and accounting records
- Technical data (logs, configurations, credentials)
- Communications (email, messaging, collaboration content)
- Backup and archive data
- Development and test data containing production information
- Temporary and cache data

**Storage Locations:**
- On-premises data centers and server rooms
- Cloud infrastructure (IaaS, PaaS)
- Cloud applications (SaaS)
- Backup and disaster recovery systems
- Archive and cold storage
- End-user devices (laptops, desktops, mobile)
- Removable media (USB, external drives)
- Paper documents and physical records

**Storage Media Types:**
- Magnetic storage (HDDs, tape)
- Solid-state storage (SSDs, NVMe, flash)
- Optical media (CD, DVD, Blu-ray)
- Paper and microfilm
- Volatile memory (RAM) where persistent data may reside

**Third Parties:**
- Cloud service providers (per ISMS-REF-A.5.23)
- Managed service providers
- Backup and disaster recovery vendors
- Data processing subcontractors
- Physical destruction service providers

**Lifecycle Stages:**
- Retention period expiry
- Data subject erasure requests
- Contract/service termination
- Asset decommissioning
- Legal hold release
- Purpose completion (data no longer needed)

### 1.2.2 Out of Scope

The following are explicitly excluded from this policy:

- **Physical equipment disposal** without data (covered under asset management)
- **Data anonymization/pseudonymization** as alternative to deletion (covered under privacy policy)
- **Data archival** for long-term retention (covered under records management)
- **Encryption key management** except for cryptographic erasure (covered under A.8.24)
- **Incident response data preservation** during active investigations

### 1.2.3 Geographic and Regulatory Scope

This policy applies to:
- All organizational locations regardless of geographic region
- All data regardless of where physically stored
- All applicable legal jurisdictions where data subjects reside

Where local regulations impose additional or different requirements:
- The **most stringent applicable requirement** shall be implemented
- Jurisdiction-specific requirements shall be documented as amendments
- Legal counsel shall resolve conflicting requirements

### 1.2.4 Technology Neutrality

This policy framework is **vendor-agnostic** and **technology-independent**. Requirements are expressed in terms of capabilities and outcomes rather than specific products.

Organizations may choose any technology solution(s) that satisfy requirements. Technology selection should consider:
- Effectiveness for specific media types
- Verification and certification capabilities
- Integration with existing infrastructure
- Compliance with applicable standards (NIST SP 800-88)
- Audit trail and evidence generation

---

## 1.3 Definitions

### 1.3.1 Core Deletion Terminology

**Information Deletion**  
The process of removing data from storage media such that it cannot be recovered through normal or specialized means. Deletion may be logical (removing references) or physical (destroying media).

**Data Sanitization**  
A broader term encompassing all methods of rendering data inaccessible, including clearing, purging, and destroying. Per NIST SP 800-88, sanitization ensures data cannot be retrieved regardless of future technology advances.

**Secure Deletion**  
Deletion methods that prevent data recovery through forensic techniques. Secure deletion goes beyond simple file deletion to overwrite or destroy underlying data.

**Retention Period**  
The defined timeframe during which data must be kept before deletion is permitted or required. Retention periods are driven by legal, regulatory, contractual, or business requirements.

**Deletion Trigger**  
An event or condition that initiates the deletion process, such as retention period expiry, data subject request, contract termination, or legal hold release.

### 1.3.2 Sanitization Methods (NIST SP 800-88 Alignment)

**Clear**  
Logical sanitization that protects data against simple, non-invasive data recovery techniques. Typically involves overwriting with fixed patterns. Suitable for media remaining within organizational control.

**Purge**  
Physical or logical sanitization that protects data against laboratory attack techniques. Renders data recovery infeasible using state-of-the-art techniques. Required for media leaving organizational control.

**Destroy**  
Physical sanitization that renders media unusable and data recovery infeasible. Methods include disintegration, pulverization, melting, and incineration.

**Cryptographic Erasure**  
Sanitization by securely deleting the encryption key for encrypted data, rendering the ciphertext unrecoverable. Effective only if encryption was properly implemented and key management is secure.

### 1.3.3 Media-Specific Terminology

**Magnetic Media**  
Storage devices using magnetic recording (HDDs, tape). Sanitization may require multiple overwrite passes or degaussing.

**Solid-State Media**  
Storage devices using flash memory (SSDs, NVMe, USB drives, mobile devices). Wear-leveling and over-provisioning complicate traditional overwriting; manufacturer secure erase or cryptographic erasure preferred.

**Optical Media**  
Storage using laser-written data (CD, DVD, Blu-ray). Generally write-once; physical destruction required for sanitization.

**Degaussing**  
Exposing magnetic media to a strong magnetic field to erase data. Effective for HDDs and tape; renders media unusable.

**Secure Erase (ATA)**  
Firmware-level command for storage devices that overwrites all user-accessible and inaccessible areas. Manufacturer implementation varies.

**TRIM/UNMAP**  
Commands informing SSDs that data blocks are no longer in use. Does NOT constitute secure deletion — data may persist in spare areas.

### 1.3.4 Regulatory and Legal Terms

**Right to Erasure (Right to be Forgotten)**  
Data subject right under GDPR Article 17 and similar regulations to request deletion of personal data under specified circumstances.

**Data Subject Request (DSR)**  
A formal request from an individual exercising their data protection rights, including erasure requests.

**Legal Hold (Litigation Hold)**  
An instruction to preserve data that may be relevant to pending or anticipated litigation, investigation, or audit. Legal holds suspend normal deletion processes.

**Retention Schedule**  
A documented matrix specifying retention periods for different data categories based on legal, regulatory, and business requirements.

**Data Minimization**  
The principle that personal data should be adequate, relevant, and limited to what is necessary. Deletion supports data minimization by removing unnecessary data.

### 1.3.5 Verification and Evidence Terms

**Deletion Certificate**  
Formal documentation confirming deletion occurred, typically including date, method, media identifiers, and responsible party.

**Certificate of Destruction (CoD)**  
Third-party attestation that physical media was destroyed, typically provided by certified destruction vendors.

**Chain of Custody**  
Documentation tracking who had possession of media from identification through destruction, ensuring accountability.

**Audit Trail**  
Chronological record of deletion activities including who, what, when, and how. Supports compliance verification.

**Verification**  
Process of confirming deletion was successful, through technical validation (attempting recovery) or procedural confirmation (certificates, logs).

### 1.3.6 Third-Party and Cloud Terms

**Data Processing Agreement (DPA)**  
Contract between data controller and processor specifying data handling requirements, including deletion obligations.

**Sub-processor**  
Third party engaged by a data processor to process data on behalf of the controller. Deletion requirements flow down to sub-processors.

**Service Level Agreement (SLA)**  
Contract terms specifying deletion timelines and methods for cloud/third-party services.

**Tenant Isolation**  
Separation of customer data in multi-tenant cloud environments. Deletion must ensure no data leakage between tenants.

**Data Remanence**  
Residual data remaining after deletion attempts. A key concern in cloud and shared infrastructure environments.

### 1.3.7 Organizational Terms

**Data Owner**  
Individual or team accountable for data throughout its lifecycle, including retention and deletion decisions.

**Data Custodian**  
Individual or team responsible for technical management of data, including executing deletion procedures.

**System Owner**  
Individual or team responsible for a system containing data, accountable for implementing deletion within that system.

**Records Manager**  
Individual responsible for organizational records management, including retention schedules and destruction coordination.

---

## 1.4 Sanitization Decision Matrix

### 1.4.1 Method Selection by Media Type

| Media Type | Clear | Purge | Destroy | Crypto Erase | Notes |
|------------|-------|-------|---------|--------------|-------|
| **HDD (Magnetic)** | Overwrite (1+ pass) | Secure Erase, Degauss | Shred, Disintegrate | If encrypted | Degaussing renders unusable |
| **SSD/NVMe** | Not Recommended | Manufacturer Secure Erase | Shred, Disintegrate | **Preferred** | Wear-leveling complicates overwriting |
| **USB Flash** | Not Recommended | Secure Erase (if supported) | Shred | If encrypted | Physical destruction often most practical |
| **Tape (Magnetic)** | Overwrite | Degauss | Incinerate, Shred | If encrypted | Degaussing preferred for tapes |
| **Optical (CD/DVD)** | N/A | N/A | Shred, Incinerate | N/A | Write-once media requires destruction |
| **Mobile Devices** | Factory Reset + Verify | Crypto Erase | Shred | **Required** | Verify encryption was enabled |
| **Paper** | N/A | N/A | Cross-cut Shred (DIN 66399) | N/A | P-4 minimum for confidential |
| **Cloud Storage** | API Delete + Verify | Crypto Erase | N/A (provider) | **Preferred** | Verify with provider |
| **Virtual Machines** | Secure Wipe | Crypto Erase | N/A | **Preferred** | Include snapshots |
| **Databases** | DELETE + Vacuum | Crypto Erase | Disk sanitization | If TDE enabled | Include transaction logs |

### 1.4.2 Method Selection by Data Classification

| Classification | Minimum Method | Recommended Method | Evidence Required |
|---------------|----------------|-------------------|-------------------|
| **Public** | Clear | Clear | Log entry |
| **Internal** | Clear | Purge | Deletion log |
| **Confidential** | Purge | Purge + Verify | Certificate |
| **Restricted** | Destroy or Crypto Erase | Destroy | Certificate of Destruction |
| **PII (GDPR/FADP)** | Purge | Purge + Verify | Certificate + Audit Trail |

---

## 1.5 References

### 1.5.1 ISO/IEC Standards

- **ISO/IEC 27001:2022** — Information Security Management Systems
- **ISO/IEC 27002:2022** — Control 8.10: Information Deletion
- **ISO/IEC 27040:2015** — Storage Security (sanitization guidance)
- **ISO/IEC 27555:2021** — Guidelines on PII Deletion
- **ISO/IEC 27017:2015** — Cloud Services Security (deletion in cloud)

### 1.5.2 Media Sanitization Standards

- **NIST SP 800-88 Rev. 1** — Guidelines for Media Sanitization (authoritative reference)
- **DoD 5220.22-M** — National Industrial Security Program (legacy, superseded by NIST)
- **DIN 66399** — Destruction of Data Media (paper shredding levels)
- **IEEE 2883-2022** — Standard for Sanitizing Storage

### 1.5.3 Regulatory References

- **EU GDPR** — Article 17 (Right to Erasure), Article 5(1)(e) (Storage Limitation)
- **Swiss FADP (nDSG)** — Data minimization, deletion obligations
- **Sector-specific** — As applicable per ISMS-POL-00

### 1.5.4 Related ISMS Documents

- **ISMS-POL-A.8.10** — Master Policy (parent document)
- **ISMS-POL-00** — Regulatory Applicability Framework
- **ISMS-REF-A.5.23** — Cloud Service Provider Registry
- **ISMS-POL-A.5.12** — Classification of Information
- **ISMS-POL-A.5.33** — Protection of Records
- **ISMS-POL-A.7.14** — Secure Disposal of Equipment
- **ISMS-POL-A.8.24** — Use of Cryptography

---

## 1.6 Policy Framework Structure

This document (S1) is part of a modular policy framework. The complete framework:

| Document | Title | Purpose |
|----------|-------|---------|
| **ISMS-POL-A.8.10** | Master Framework | Index and overview |
| **ISMS-POL-A.8.10-S1** | Purpose, Scope, Definitions | This document |
| **ISMS-POL-A.8.10-S2** | Deletion Requirements | Requirements overview |
| **ISMS-POL-A.8.10-S2.1** | Retention & Deletion Triggers | When to delete |
| **ISMS-POL-A.8.10-S2.2** | Deletion Methods by Media | How to delete |
| **ISMS-POL-A.8.10-S2.3** | Verification & Evidence | Proving deletion |
| **ISMS-POL-A.8.10-S2.4** | Third-Party & Cloud | External providers |
| **ISMS-POL-A.8.10-S3** | Roles & Responsibilities | Accountability |
| **ISMS-POL-A.8.10-S4** | Policy Governance | Management |
| **ISMS-POL-A.8.10-S5.A-D** | Annexes | Supporting materials |

---

## 1.7 Document Maintenance

### 1.7.1 Review Triggers

This document shall be reviewed:
- **Annually** as part of ISMS policy review cycle
- **Upon regulatory changes** affecting deletion requirements
- **Upon technology changes** affecting sanitization methods
- **Following incidents** involving data retention/deletion failures
- **Upon significant organizational changes** affecting data landscape

### 1.7.2 Change Management

Changes require:
- Proposal with justification
- Impact assessment
- Stakeholder review (IT, Legal, DPO)
- CISO approval
- Communication to affected personnel

---

## 1.8 Compliance and Enforcement

### 1.8.1 Policy Violations

Violations may include:
- Failure to delete data per retention schedule
- Unauthorized retention of personal data
- Failure to respond to data subject erasure requests
- Improper disposal of media (e.g., discarding without sanitization)
- Failure to obtain deletion verification from third parties
- Circumventing legal holds

### 1.8.2 Consequences

Violations are subject to:
- Mandatory remediation with timeline
- Escalation to management
- Disciplinary action
- Regulatory notification (if required)
- Legal liability (for serious violations)

### 1.8.3 Monitoring

The organization monitors deletion compliance through:
- Retention schedule audits
- Data subject request tracking
- Third-party deletion verification
- System deletion log review
- Periodic compliance assessments

---

**END OF DOCUMENT**

*"What gets measured gets managed. What gets deleted gets... well, that's exactly the problem."*  
— The Deletion Paradox
