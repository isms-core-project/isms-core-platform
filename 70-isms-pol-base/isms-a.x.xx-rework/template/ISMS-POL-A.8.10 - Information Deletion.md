# ISMS-POL-A.8.10 — Information Deletion

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Information Deletion |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.10 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Secondary: Data Protection Officer (DPO)
- Compliance: Legal/Compliance Officer
- Technical: Chief Information Officer (CIO)
- Final Authority: Executive Management (GL)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.10 (Implementation Guidance Suite)
- ISMS-REF-A.8.10 (Deletion Methods Reference - Technical Reference)
- ISMS-REF-A.5.23 (Cloud Service Provider Registry)
- ISMS-FORM-A.8.10-GDPR (Operational Forms and Templates)
- ISO/IEC 27001:2022 Control A.8.10

---

## Executive Summary

This policy establishes [Organization]'s requirements for secure deletion of information when no longer required, in accordance with ISO/IEC 27001:2022 Control A.8.10.

**Scope**: This policy applies to all information assets regardless of storage location (on-premises, cloud, third-party), all storage media types (magnetic, solid-state, optical, paper, mobile devices), all organizational personnel and third parties processing organizational data, and all lifecycle stages requiring deletion (retention expiry, data subject requests, contract termination, asset decommissioning, legal hold release).

**Purpose**: Define organizational requirements for information deletion control implementation and governance. This policy establishes WHAT deletion protection is required, WHEN deletion must occur, and WHO is accountable. Implementation procedures (HOW deletion is performed) are documented separately in ISMS-IMP-A.8.10.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG (data minimization and data subject rights), EU GDPR Article 17 (right to erasure), and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS, HIPAA, FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.10

**ISO/IEC 27001:2022 Annex A.8.10 - Information Deletion**

> *Information stored in information systems, devices or in any other storage media shall be deleted when no longer required.*

**Control Objective**: Establish organizational policy for secure deletion of information throughout its lifecycle to prevent unnecessary exposure, ensure compliance with legal and regulatory obligations, and honor data subject rights.

**This Policy Addresses**:
- Retention period determination and deletion trigger events
- Deletion methods appropriate for storage media types and data sensitivity
- Third-party and cloud service provider deletion obligations
- Verification and evidence requirements for demonstrating deletion effectiveness
- Data subject erasure request handling (GDPR Article 17, Swiss nDSG)
- Legal hold management and suspension of deletion processes
- Organizational roles and responsibilities for deletion governance
- Exception and incident management frameworks
- Integration with [Organization]'s risk assessment and treatment processes

### 1.2 What This Policy Does

This policy:
- **Defines** information deletion control requirements aligned with data classification, regulatory obligations, and organizational risk appetite
- **Establishes** governance framework for deletion decision-making and accountability
- **Specifies** mandatory deletion triggers based on retention periods, data subject requests, and lifecycle events
- **References** applicable regulatory requirements per ISMS-POL-00
- **Identifies** organizational roles and responsibilities for deletion controls
- **Provides** framework for managing exceptions and legal holds

### 1.3 What This Policy Does NOT Do

This policy does NOT:
- **Specify technical deletion procedures** (see ISMS-IMP-A.8.10 Implementation Guides)
- **Define specific retention periods for all data types** (see ISMS-IMP-A.8.10.1 Retention Schedule Assessment - organizations define based on regulatory requirements and business needs)
- **List approved deletion tools or vendors** (see ISMS-REF-A.8.10 Deletion Methods Reference)
- **Provide step-by-step sanitization instructions** (see ISMS-IMP-A.8.10.2 Deletion Methods Assessment)
- **Select specific deletion technologies** (technology selection based on [Organization]'s risk assessment, media types, and technical environment)
- **Replace data classification policy** (deletion requirements depend on [Organization]'s data classification scheme)
- **Define detailed incident response procedures** (see ISMS-IMP-A.8.10.4 Verification & Evidence Assessment)

**Rationale**: Separating policy requirements from implementation guidance enables:
- Policy stability despite evolving storage technologies and sanitization standards
- Technical agility for new deletion methods and tools without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Focused audit scope (auditors verify policy compliance, not specific tool configurations)
- Adaptability for different organizational contexts, industries, and risk profiles

### 1.4 Scope

**This policy applies to**:

**Information Assets**:
- All data categories (personal data, confidential business information, financial records, technical data, communications, logs)
- All classification levels (Internal, Confidential, Restricted per [Organization]'s classification scheme)
- All formats (structured databases, unstructured files, email, backups, system logs, configuration data)
- All lifecycle stages (active use, archival, backup, disaster recovery, development/test environments)

**Storage Locations**:
- On-premises infrastructure (data centers, server rooms, local storage)
- Cloud infrastructure (IaaS, PaaS, SaaS across all cloud service providers)
- Third-party processing locations (managed service providers, subcontractors)
- Backup and disaster recovery systems (tape libraries, cloud backup, replicas)
- End-user devices (laptops, desktops, mobile devices, removable media)
- Archive and cold storage (long-term retention systems)

**Media Types**:
- Magnetic storage (HDDs, tape media)
- Solid-state storage (SSDs, NVMe, flash drives, SD cards)
- Optical media (CD, DVD, Blu-ray)
- Paper documents and physical records
- Virtual storage (VMs, containers, cloud volumes, snapshots)

**Organizational Coverage**:
- All employees (permanent, temporary, contractors)
- All third-party service providers processing organizational data
- All cloud service providers storing organizational information
- All business units and geographic locations
- All operational and non-operational environments (production, development, testing, training)

**Out of Scope**:
- Physical equipment disposal without data considerations (covered under asset management policies)
- Data anonymization or pseudonymization as alternatives to deletion (covered under privacy policies)
- Data archival for long-term retention within retention periods (covered under records management)
- Encryption key management except for cryptographic erasure (covered under ISMS-POL-A.8.24)
- Data preservation during active investigations or litigation (handled through legal hold procedures)

### 1.5 Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**. 

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Deletion Requirements |
|------------|---------------|---------------------------|
| **Swiss nDSG** | All Swiss operations | Art. 6 - Data minimization and purpose limitation principles; Art. 19 - Data subject rights including right to request erasure; Art. 7 - Appropriate technical and organizational measures for secure deletion |
| **EU GDPR** | When processing EU personal data | Art. 17 - Right to erasure ("right to be forgotten"); Art. 5(1)(e) - Storage limitation principle requiring deletion when no longer necessary; Art. 32 - Security measures including secure disposal |
| **ISO/IEC 27001:2022** | Certification scope | Control A.8.10 - Documented information deletion policy, implemented deletion procedures, evidence of effectiveness |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Deletion Requirements |
|-----------|-------------------|----------------------|
| **PCI DSS v4.0** | Processing payment card data | Req. 3.1 - Data retention and disposal procedures for cardholder data; Req. 12.10.7 - Quarterly hard copy materials destruction procedures; Req. 9.8.2 - Secure destruction of media containing cardholder data |
| **HIPAA Security Rule** | US healthcare data processing | §164.310(d)(2)(i) - Disposal standard requiring proper media disposal and data destruction; §164.530(j) - Record retention and availability requirements |
| **FINMA** | Swiss regulated financial institution | Data retention obligations per financial regulations; Secure deletion requirements for client data; Technical and organizational measures per risk assessment |
| **DORA** | EU financial services entity | ICT risk management including data lifecycle controls; Secure data disposal as operational resilience measure; Third-party deletion verification for critical services |
| **NIS2** | Essential/important entity (EU) | Security measures for information lifecycle management; Secure disposal procedures; Incident reporting for improper data disposal |
| **SOX** | Publicly traded companies | Record retention requirements (7 years for audit documents); Secure disposal after retention period; Prevention of premature deletion of financial records |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- NIST SP 800-88 Rev. 1 (Guidelines for Media Sanitization - authoritative technical reference)
- ISO/IEC 27040 (Storage Security - sanitization guidance)
- ISO/IEC 27555 (Guidelines on PII Deletion)
- ISO/IEC 27017 (Cloud Services Security - deletion in cloud environments)
- DIN 66399 (Document Destruction Standards - paper shredding security levels)
- IEEE 2883-2022 (Standard for Sanitizing Storage)
- NIST SP 800-53 (Security Controls - Media Protection family)

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment documented in risk assessments and compliance registers. The most stringent requirements apply where multiple regulations overlap. Regulatory applicability is reviewed annually and when significant business changes occur (new markets, services, or data processing activities).

---

## 2. Information Deletion Requirements Framework

### 2.1 Retention & Deletion Triggers (Mandatory)

**Objective**: Ensure information is retained for appropriate periods and deleted when no longer required.

**Requirements**:

**2.1.1 Data Category Inventory**

[Organization] SHALL maintain a comprehensive inventory of data categories processed, including:
- Data type and classification level
- Business purpose and legal basis for processing
- Primary storage location and backup systems
- Data owner and custodian identification
- Volume or record count (approximate)

**Implementation**: ISMS-IMP-A.8.10.1 (Retention & Deletion Triggers Assessment) provides structured workbook for documenting data categories.

**2.1.2 Retention Schedule Definition**

[Organization] SHALL establish retention schedules for all data categories based on:
- **Legal requirements**: Statutory retention minimums (tax records, employment records, financial documents)
- **Regulatory requirements**: Sector-specific retention obligations (healthcare, financial services, telecommunications)
- **Contractual obligations**: Customer or partner agreements requiring specific retention periods
- **Business requirements**: Operational needs, analytics, historical reference (justified and documented)
- **Risk assessment**: Litigation risk, regulatory examination, audit trails

**Retention Period Calculation**:
- **Fixed Period**: Specific timeframe from creation/collection date (e.g., "7 years from invoice date")
- **Event-Based**: Deletion triggered by specific event (e.g., "30 days after contract termination")
- **Hybrid**: Combination of fixed and event-based (e.g., "3 years after employment termination or 7 years from creation, whichever is longer")

**Retention Conflicts**: Where multiple retention requirements apply, the LONGEST applicable retention period SHALL be implemented unless legal counsel determines otherwise.

**2.1.3 Deletion Triggers**

Deletion SHALL be triggered by one of the following events:

| Trigger Type | Description | Verification Required |
|-------------|-------------|----------------------|
| **Retention Expiry** | Predetermined retention period has elapsed | Automated calendar check or manual review |
| **Data Subject Request** | GDPR Article 17 / FADP erasure request received | Identity verification, legal basis review, exception assessment |
| **Contract Termination** | Service agreement or customer relationship ended | Contract end date confirmation, retention obligation review |
| **Purpose Completion** | Processing purpose no longer applies | Business owner confirmation, legal basis review |
| **Legal Hold Release** | Litigation, investigation, or audit hold lifted | Legal counsel authorization, formal hold release notification |
| **Asset Decommissioning** | Storage media or system end-of-life | Asset inventory update, data migration verification |
| **Consent Withdrawal** | Data subject withdraws processing consent | Consent management system update, processing basis review |

**2.1.4 Automated Deletion Processes**

[Organization] SHOULD implement automated deletion processes where technically feasible:
- Database record deletion based on timestamp fields
- Cloud storage lifecycle policies (S3 lifecycle, Azure blob lifecycle)
- Log rotation and purging (system logs, application logs, access logs)
- Backup tape rotation and purging
- Email retention policies (Exchange, Google Workspace, Office 365)

**Manual Review Required**: Automated deletion MUST include safeguards against premature deletion:
- Legal hold checks before deletion execution
- Business owner approval for high-value data categories
- Exception register review
- Audit trail generation

**2.1.5 Legal Hold Management**

[Organization] SHALL implement procedures to suspend deletion when required by law:

**Legal Hold Triggers**:
- Litigation (filed, threatened, or reasonably anticipated)
- Government investigation or regulatory examination
- Internal investigation (fraud, misconduct, security incident)
- Audit (external, internal, regulatory)

**Legal Hold Process**:
1. Legal counsel issues formal hold notification
2. Data custodians identify affected systems and data
3. Automated deletion processes suspended for held data
4. Hold register updated with scope, reason, responsible party
5. Periodic hold review (at least quarterly) to assess continued necessity
6. Formal hold release authorization when no longer required
7. Deletion proceeds per standard retention schedule after release

**Implementation**: ISMS-IMP-A.8.10.1 provides legal hold tracking and management procedures.

### 2.2 Deletion Methods Requirements (Mandatory)

**Objective**: Ensure deletion methods are appropriate for storage media types and data sensitivity.

**Requirements**:

**2.2.1 Sanitization Method Selection**

[Organization] SHALL select deletion methods aligned with:
- **Media type**: Magnetic, solid-state, optical, paper, cloud storage
- **Data classification**: Public, Internal, Confidential, Restricted
- **Media destination**: Internal reuse, external transfer, disposal/destruction
- **Recovery risk**: Likelihood and impact of data recovery by adversary

**Sanitization Categories** (per NIST SP 800-88 informational reference):

| Method | Protection Level | Use Case | Examples |
|--------|-----------------|----------|----------|
| **Clear** | Simple non-invasive recovery protection | Media remaining in organizational control, low-sensitivity data | Single-pass overwrite, quick format, standard deletion |
| **Purge** | Laboratory attack resistance | Media leaving organizational control, medium-to-high sensitivity data | ATA Secure Erase, cryptographic erasure, degaussing, multi-pass overwrite |
| **Destroy** | Media unusable, data recovery infeasible | End-of-life media disposal, highest sensitivity data | Physical disintegration, pulverization, incineration, shredding |

**2.2.2 Media-Specific Requirements**

[Organization] SHALL apply appropriate deletion methods per media type:

**Magnetic Storage (HDD, Tape)**:
- **Internal Reuse**: ATA Secure Erase OR single-pass overwrite minimum
- **External Transfer/Disposal**: ATA Secure Erase OR degaussing OR physical destruction
- **Confidential/Restricted Data**: Degaussing OR physical destruction (shred to ≤2mm particles)

**Solid-State Storage (SSD, NVMe, Flash)**:
- **Internal Reuse**: Manufacturer Secure Erase (ATA/NVMe Sanitize) OR cryptographic erasure
- **External Transfer/Disposal**: Cryptographic erasure + verification OR physical destruction
- **High-Sensitivity Data**: Physical destruction (shred to ≤2mm particles)
- **Note**: Standard overwriting NOT RECOMMENDED due to wear-leveling and over-provisioning

**Cloud Storage (IaaS/PaaS/SaaS)**:
- **Logical Deletion**: API-based deletion with verification response
- **Enhanced Deletion**: Customer-managed encryption key deletion (cryptographic erasure)
- **Provider Verification**: Deletion certificate or attestation from cloud service provider
- **Multi-Tenant Awareness**: Verify tenant isolation and no data remanence

**Mobile Devices**:
- **Encrypted Devices**: Factory reset + MDM remote wipe + encryption key destruction
- **Non-Encrypted Devices**: Physical destruction of storage component
- **Verification**: MDM console confirmation + device check-in attempt

**Paper Documents**:
- **Internal/Confidential**: Cross-cut shredding (DIN 66399 Security Level P-4 minimum)
- **Restricted/PII**: Cross-cut shredding (DIN 66399 Security Level P-5 or P-6)
- **Large Volume**: Contracted destruction service with certificate of destruction

**Virtual Environments**:
- **Virtual Machines**: Secure wipe of virtual disk files + snapshot deletion + template removal
- **Containers**: Image deletion + volume destruction + registry cleanup
- **Databases**: DROP TABLE + VACUUM + transaction log purging (or cryptographic erasure if TDE enabled)

**Technical Reference**: ISMS-REF-A.8.10 (Deletion Methods Reference) provides detailed media-specific procedures and approved tool lists.

**2.2.3 Cryptographic Erasure**

Where technically feasible, [Organization] SHOULD leverage cryptographic erasure for high-efficiency deletion:

**Requirements**:
- Encryption MUST be enabled from initial deployment (post-deployment encryption less effective)
- Encryption keys MUST be protected with appropriate access controls
- Key deletion MUST be irreversible and verified
- Key management system MUST log destruction events
- Verification MUST confirm key inaccessibility

**Applicable Scenarios**:
- Self-encrypting drives (SED) with hardware encryption
- Full-disk encryption (BitLocker, FileVault, LUKS)
- Database transparent data encryption (TDE)
- Cloud provider encryption (customer-managed keys)
- File-level encryption systems

**Limitations**: Cryptographic erasure relies on encryption being properly implemented. [Organization] MUST verify encryption status before relying on key deletion as sole deletion method.

**2.2.4 Backup Deletion Alignment**

**CRITICAL REQUIREMENT**: Deletion in production systems MUST extend to ALL backup copies.

[Organization] SHALL ensure:
- Backup retention periods align with production data retention schedules
- Backup deletion occurs when production retention expires
- Incremental/differential backups containing deleted data are purged
- Snapshot-based backups (VM snapshots, storage snapshots) are identified and deleted
- Cloud backup services (AWS Backup, Azure Backup, Veeam Cloud) are included in deletion scope
- Disaster recovery replicas are synchronized with production deletion

**Backup Paradox Prevention**: Organizations commonly delete production data while forgetting backup tapes, DR sites, and cloud backup retention policies. This policy explicitly requires backup deletion verification.

**Implementation**: ISMS-IMP-A.8.10.2 (Deletion Methods Assessment) includes backup deletion checklist and verification procedures.

### 2.3 Third-Party & Cloud Deletion (Mandatory)

**Objective**: Ensure third parties and cloud service providers delete organizational data upon request or contract termination.

**Requirements**:

**2.3.1 Contractual Obligations**

[Organization] SHALL include deletion obligations in all contracts with third parties processing organizational data:

**Required Contract Terms**:
- **Deletion timeline**: Maximum timeframe for deletion after contract termination or upon request (e.g., "30 days")
- **Deletion method**: Sanitization standards appropriate for data sensitivity (reference to NIST SP 800-88 or equivalent)
- **Deletion scope**: All data copies including backups, logs, replicas, disaster recovery copies
- **Verification**: Requirement to provide deletion certificate or attestation
- **Sub-processor obligations**: Deletion requirements flow down to all sub-processors
- **Audit rights**: [Organization] right to verify deletion or obtain third-party audit report

**GDPR Article 28 Alignment**: Data processing agreements (DPAs) with processors MUST comply with GDPR Article 28(3)(g) requiring data deletion or return at controller's choice.

**2.3.2 Cloud Service Provider Deletion**

[Organization] SHALL assess cloud service provider deletion capabilities per ISMS-REF-A.5.23 (Cloud Service Provider Registry):

**Assessment Criteria**:
- **API deletion support**: Programmatic deletion capabilities (REST API, CLI)
- **Deletion verification**: Response codes, deletion receipts, audit logs
- **Multi-tenant isolation**: Assurance that deleted data not accessible to other tenants
- **Data remanence**: Provider controls to prevent data remnants
- **Geographic deletion**: Deletion across all regions/availability zones
- **Backup deletion**: Provider backup retention policies and deletion procedures
- **Certification**: Provider adherence to ISO 27001, SOC 2 Type II, or equivalent with deletion controls

**Cloud Service Tiers** (per ISMS-REF-A.5.23):
- **Tier 1-3 Providers** (Hyperscalers): Documented deletion procedures, API support, certifications required
- **Tier 4-6 Providers** (Specialized): Deletion SLA verification, certificate of deletion required
- **Tier 7-10 Providers** (Niche/Emerging): Enhanced verification, potential data retrieval before deletion, migration planning

**2.3.3 Deletion Verification from Third Parties**

[Organization] SHALL obtain verification of deletion from third parties:

**Verification Methods**:
- **Certificate of Destruction**: Signed attestation from authorized third-party representative
- **Audit Report**: SOC 2 Type II report covering deletion controls (if available)
- **API Response**: Cloud provider deletion confirmation via API response logging
- **On-Site Verification**: Physical inspection of destruction (for high-sensitivity data at high-risk providers)

**Required Certificate Elements**:
- Date of deletion
- Scope of deletion (data categories, systems, volumes)
- Method of deletion (sanitization technique)
- Confirmation that all copies deleted (including backups)
- Authorized signatory name and title
- Attestation of compliance with contract terms

**Implementation**: ISMS-IMP-A.8.10.3 (Third-Party & Cloud Deletion Assessment) provides provider evaluation criteria, contract clause templates, and verification tracking.

### 2.4 Verification & Evidence Requirements (Mandatory)

**Objective**: Ensure deletion activities are documented, verifiable, and audit-ready.

**Requirements**:

**2.4.1 Deletion Logging**

[Organization] SHALL maintain comprehensive deletion audit trails:

**Required Log Elements**:
- Deletion timestamp (date and time)
- Data category or system identifier
- Deletion method applied
- Media type and identifier (serial number, asset tag, cloud resource ID)
- Deletion trigger (retention expiry, data subject request, decommissioning, etc.)
- Responsible party (individual or system performing deletion)
- Verification method and result
- Any exceptions or errors encountered

**Log Retention**: Deletion logs SHALL be retained for minimum of 3 years or per applicable regulatory requirements (whichever is longer) to demonstrate compliance during audits.

**2.4.2 Deletion Certificates**

[Organization] SHALL generate or obtain certificates for deletion of sensitive data:

**Internal Certificates**: For on-premises deletion, internal IT operations SHALL generate certificates including:
- Asset or media identifiers
- Data classification level
- Deletion date and method
- Responsible party signature
- Verification outcome

**External Certificates**: For third-party destruction services, [Organization] SHALL obtain certificates of destruction meeting requirements in Section 2.3.3.

**2.4.3 Data Subject Request Tracking**

[Organization] SHALL maintain comprehensive records of data subject erasure requests:

**Required Documentation** (per GDPR Article 17 and Swiss nDSG):
- Request receipt date and method
- Identity verification process and outcome
- Request scope (data categories, systems affected)
- Legal basis assessment (erasure applicable or exception applies)
- Deletion execution date and systems
- Third-party notification (where data was disclosed to third parties)
- Response to data subject (within 30 days per GDPR)
- Evidence of deletion (logs, certificates, confirmations)

**Exception Documentation**: Where erasure request is denied (legal obligation, public interest, legal claims), [Organization] SHALL document:
- Specific exception basis (GDPR Article 17(3) provisions)
- Legal analysis supporting denial
- Alternative measures offered (restriction of processing, data portability)
- Communication to data subject explaining denial and rights

**Implementation**: ISMS-FORM-A.8.10-GDPR provides standardized Data Subject Erasure Request Form and tracking procedures.

**2.4.4 Verification Procedures**

[Organization] SHALL implement verification to confirm deletion effectiveness:

**Verification Methods**:
- **Automated**: Deletion confirmation receipts from systems (API responses, application logs)
- **Sampling**: Periodic sampling of deleted media with forensic tools to verify data irrecoverability
- **Attestation**: Third-party certificates for physical destruction or cloud provider deletion
- **Audit Trail Review**: Periodic review of deletion logs for completeness and accuracy

**Verification Frequency**:
- **Real-time**: Automated deletion processes with immediate verification logging
- **Quarterly**: Sample verification of manual deletion procedures (select 5-10% of deletion events)
- **Annual**: Comprehensive review of all high-sensitivity data deletion activities

**2.4.5 Evidence Register**

[Organization] SHALL maintain an Evidence Register documenting:
- All deletion certificates (internal and external)
- Data subject request logs and responses
- Legal hold notifications and releases
- Deletion exception approvals
- Verification reports and sampling results
- Annual compliance assessment summaries

**Evidence Accessibility**: Evidence SHALL be readily accessible for internal audits, external audits, regulatory examinations, and data subject inquiries.

**Implementation**: ISMS-IMP-A.8.10.4 (Verification & Evidence Assessment) provides evidence management procedures and register template.

---

## 3. Governance & Operations

### 3.1 Roles & Responsibilities

[Organization] establishes clear accountability for information deletion controls through defined roles and responsibilities.

**3.1.1 RACI Matrix**

| Activity | CISO | DPO | Legal | CIO/IT Director | IT Ops | System Owners | Data Owners | Records Manager |
|----------|------|-----|-------|----------------|--------|---------------|-------------|-----------------|
| **Policy Development** | A | C | C | C | I | I | I | C |
| **Policy Approval** | R | C | C | R | I | I | I | I |
| **Retention Schedule Definition** | C | C | A | C | I | R | R | A |
| **Deletion Method Selection** | A | C | C | R | R | C | I | I |
| **Automated Deletion Configuration** | C | I | I | A | R | R | C | I |
| **Manual Deletion Execution** | I | I | I | C | R | R | C | I |
| **Data Subject Request Handling** | C | A | C | I | I | R | C | I |
| **Legal Hold Management** | C | C | A | C | I | C | C | I |
| **Deletion Verification** | A | C | I | R | R | C | I | I |
| **Evidence Collection** | C | C | I | R | R | R | C | C |
| **Third-Party Deletion Verification** | C | C | A | R | I | C | C | I |
| **Exception Approval** | A | A | C | C | I | C | C | C |
| **Compliance Monitoring** | A | R | C | C | I | I | I | C |
| **Annual Policy Review** | A | R | R | R | C | C | C | R |

**Legend**: R = Responsible (does the work), A = Accountable (final authority), C = Consulted (input requested), I = Informed (kept updated)

**3.1.2 Role Descriptions**

**Chief Information Security Officer (CISO)**:
- Accountable for information deletion policy framework and overall compliance
- Approves deletion methods and tools
- Reviews and approves deletion-related exceptions
- Oversees compliance monitoring and reporting
- Escalates significant deletion failures to executive management

**Data Protection Officer (DPO)**:
- Accountable for data subject erasure request handling (GDPR Article 17, Swiss nDSG)
- Accountable for retention schedule compliance with privacy regulations
- Reviews deletion procedures for privacy impact
- Monitors and reports on data subject request response times
- Advises on retention periods for personal data categories
- Coordinates with supervisory authorities on deletion matters

**Legal/Compliance Officer**:
- Accountable for legal hold management (litigation, investigation, audit)
- Accountable for third-party deletion contract terms and verification
- Advises on retention periods for legal and regulatory compliance
- Reviews deletion exceptions for legal risk
- Provides legal analysis for data subject request denials
- Ensures deletion practices comply with applicable laws and regulations

**Chief Information Officer (CIO) / IT Director**:
- Accountable for deletion technology implementation and operational effectiveness
- Approves IT budget for deletion tools and services
- Ensures IT operations team trained on deletion procedures
- Reviews technical deletion capabilities during technology procurement
- Escalates deletion technology limitations or failures

**IT Operations**:
- Responsible for executing deletion procedures (automated and manual)
- Responsible for deletion logging and evidence collection
- Responsible for deletion verification and sampling
- Maintains deletion tools and systems
- Coordinates with system owners on deletion activities
- Reports deletion failures or anomalies

**System Owners**:
- Responsible for implementing deletion within their assigned systems
- Responsible for coordinating with IT operations on deletion procedures
- Identifies data categories and retention requirements for their systems
- Tests deletion procedures during system changes or upgrades
- Participates in deletion verification activities
- Reports system-specific deletion challenges

**Data Owners**:
- Responsible for defining retention periods for their data categories
- Approves deletion of business-critical data
- Identifies business requirements affecting retention
- Reviews deletion logs for their data categories
- Participates in exception approval process
- Coordinates with records manager on retention schedules

**Records Manager**:
- Accountable for organizational retention schedule maintenance
- Responsible for coordinating retention period updates across departments
- Tracks regulatory and legal retention requirement changes
- Publishes updated retention schedules
- Advises data owners on retention best practices
- Coordinates with archives and long-term storage

**3.1.3 Delegation and Escalation**

**Delegation**: Roles may delegate specific tasks but accountability remains with the designated role. Delegation MUST be documented and communicated.

**Escalation Triggers**:
- Deletion failure affecting high-sensitivity data (Confidential, Restricted)
- Data subject request response time approaching GDPR 30-day deadline
- Third-party refusal to provide deletion verification
- Legal hold conflicting with data subject erasure request
- Deletion tool failure or unavailability
- Discovery of retained data exceeding retention period by >90 days

**Escalation Path**: IT Operations → System Owner → CIO/CISO → DPO (privacy matters) / Legal (legal holds) → Executive Management (significant compliance failures)

### 3.2 Data Subject Erasure Requests (GDPR Article 17 / Swiss nDSG)

**Objective**: Ensure timely and compliant handling of data subject rights to erasure.

**Requirements**:

**3.2.1 Request Receipt and Logging**

[Organization] SHALL:
- Accept erasure requests via multiple channels (email, web portal, phone, written mail)
- Log all requests within 24 hours of receipt
- Assign unique request identifier (e.g., ESR-2026-0001)
- Calculate GDPR 30-day response deadline from receipt date
- Notify relevant stakeholders (DPO, IT operations, system owners)

**3.2.2 Identity Verification**

Before processing erasure requests, [Organization] SHALL verify data subject identity:

**Verification Methods**:
- Account authentication (login credentials)
- Email confirmation (verification link to registered email)
- Knowledge-based authentication (security questions, account details)
- Document verification (copy of ID document for high-risk requests)
- In-person verification (for walk-in requests)

**Verification Standard**: Identity verification MUST provide reasonable assurance that the requester is the data subject or authorized representative. Insufficient verification results in request suspension pending proper verification.

**3.2.3 Legal Basis Assessment**

DPO SHALL assess whether erasure obligation applies or exceptions exist:

**Erasure Applies When** (GDPR Article 17(1), Swiss nDSG):
- Data no longer necessary for original purpose
- Data subject withdraws consent (consent-based processing)
- Data subject objects and no overriding legitimate grounds exist
- Data processed unlawfully
- Legal obligation requires erasure
- Data collected for child online services (GDPR Article 8)

**Erasure DOES NOT Apply When** (GDPR Article 17(3) exceptions):
- Legal obligation requires retention (tax records, employment records)
- Public interest task (statistical, research, public health)
- Legal claims (establishment, exercise, or defense)
- Archiving in public interest (historical research, scientific purposes)
- Freedom of expression and information rights

**Exception Documentation**: When erasure denied, DPO SHALL document specific legal basis, provide written explanation to data subject, and inform of complaint rights to supervisory authority.

**3.2.4 Deletion Execution**

Upon confirming erasure obligation, [Organization] SHALL:

1. **Identify Scope**: Determine all systems, backups, and third parties holding data subject's personal data
2. **Execute Deletion**: Apply appropriate deletion methods per Section 2.2
3. **Verify Deletion**: Confirm deletion across all identified systems and backups
4. **Notify Third Parties**: Where personal data disclosed to third parties (processors, recipients), notify them of erasure request per GDPR Article 19
5. **Document Evidence**: Collect deletion logs, certificates, third-party confirmations

**Timeline**: Deletion execution SHOULD commence within 5 business days of confirming erasure obligation to allow buffer for verification and response.

**3.2.5 Response to Data Subject**

[Organization] SHALL respond to data subject within 30 days (GDPR deadline) or 30 days (Swiss nDSG) with:

**If Erasure Completed**:
- Confirmation that personal data erased
- Systems and data categories affected
- Date of deletion execution
- Third parties notified (if applicable)
- Retention period for deletion evidence

**If Erasure Denied**:
- Specific legal exception basis (reference to GDPR Article 17(3) provision)
- Explanation in clear, plain language
- Alternative measures offered (restriction of processing, data portability if applicable)
- Right to complain to supervisory authority (contact details)
- Right to judicial remedy

**Extension**: If deletion scope is complex and 30-day deadline insufficient, [Organization] may extend by 2 months with written notification to data subject explaining delay reasons (GDPR Article 12(3)).

**Implementation**: ISMS-FORM-A.8.10-GDPR provides standardized Data Subject Erasure Request Form and response templates.

### 3.3 Legal Hold Management

**Objective**: Ensure deletion is suspended when legal, regulatory, or investigative obligations require data preservation.

**Requirements**:

**3.3.1 Legal Hold Triggers**

Legal holds SHALL be initiated when:
- Litigation filed or reasonably anticipated
- Government investigation, subpoena, or regulatory examination
- Internal investigation (fraud, misconduct, security incident requiring forensic preservation)
- External audit requiring specific data preservation
- Contractual obligation to preserve data (customer request, insurance claim)

**Authority**: ONLY Legal/Compliance Officer may initiate legal holds. No other role has authority to suspend deletion processes.

**3.3.2 Hold Notification Process**

Legal/Compliance Officer SHALL:

1. **Issue Hold Notice**: Formal written notification to affected stakeholders (IT operations, system owners, data custodians)
2. **Define Scope**: Specific data categories, date ranges, custodians, systems affected
3. **Specify Duration**: Expected hold duration (if known) or "indefinite pending legal resolution"
4. **Suspend Deletion**: IT operations configures systems to exclude held data from automated deletion
5. **Update Hold Register**: Document hold ID, reason, scope, responsible party, notification date

**Hold Notice Elements**:
- Hold identifier and reason
- Data categories and systems in scope
- Custodians and affected personnel
- Deletion suspension confirmation required
- Contact for questions (Legal officer)
- Prohibition on destruction or alteration

**3.3.3 Hold Duration and Review**

[Organization] SHALL:
- Review active holds QUARTERLY to assess continued necessity
- Legal counsel provides status update on litigation/investigation
- Remove hold when legal obligation resolved
- Document hold duration and justification for extended holds

**Extended Holds**: Holds exceeding 12 months require executive management awareness and annual justification review.

**3.3.4 Hold Release and Deletion Resumption**

Upon hold release, Legal/Compliance Officer SHALL:

1. **Issue Release Notice**: Formal written notification that hold lifted
2. **Confirm Scope**: Specify which data categories and systems released
3. **Resume Deletion**: IT operations re-enables automated deletion for released data
4. **Immediate Deletion Assessment**: Determine if released data now exceeds retention period and requires immediate deletion
5. **Update Hold Register**: Document release date, reason, and deletion actions taken

**Deletion After Release**: Data held beyond normal retention period due to legal hold SHALL be deleted within 90 days of hold release unless business justification approved by CISO and DPO.

**3.3.5 Conflicts with Data Subject Requests**

When data subject erasure request conflicts with legal hold:

**Resolution**:
- Legal/Compliance Officer and DPO jointly assess
- GDPR Article 17(3)(e) exception typically applies (data needed for legal claims)
- Response to data subject explains legal hold situation
- Alternative measures: Restriction of processing (GDPR Article 18) - data retained but not actively processed
- Hold register annotated with data subject request reference
- Deletion executed immediately upon hold release (unless other retention basis exists)

### 3.4 Exception Management

**Objective**: Manage deviations from standard deletion procedures with appropriate risk assessment and approval.

**Requirements**:

**3.4.1 Exception Categories**

Exceptions may be requested for:
- **Extended Retention**: Retain data beyond standard retention period for specific business justification
- **Alternative Deletion Method**: Use deletion method different from policy requirements (e.g., logical deletion instead of secure erase)
- **Delayed Deletion**: Postpone deletion beyond scheduled deletion date
- **Deletion Deferral**: Temporarily suspend deletion for specific operational reason

**3.4.2 Exception Request Process**

Exception requests SHALL include:

**Required Information**:
- Data category and classification
- Standard retention period and requested exception duration
- Business justification (detailed and specific)
- Risk assessment (exposure from extended retention, regulatory non-compliance)
- Compensating controls (encryption, access restriction, monitoring)
- Approval requested from (CISO, DPO, Legal as applicable)
- Proposed exception expiry date

**Submission**: Exceptions submitted via ISMS-FORM-A.8.10-GDPR (Exception Request Form) to CISO office.

**3.4.3 Exception Approval Authority**

| Exception Type | Approval Authority | Maximum Duration |
|---------------|-------------------|------------------|
| **Low-sensitivity data (Internal), <12 months extension** | System Owner + CISO | 12 months |
| **Medium-sensitivity data (Confidential), <6 months extension** | CISO + DPO | 6 months |
| **High-sensitivity data (Restricted), any extension** | CISO + DPO + Legal + Executive Mgmt | 3 months (renewable) |
| **Personal data retention extension** | DPO + CISO | Case-by-case (GDPR compliance assessment) |
| **Alternative deletion method** | CISO + IT Director | Permanent (if justified) or until technology change |

**Approval Timeline**: Exception requests SHALL be processed within 10 business days. Urgent requests (operational impact) may be expedited with CISO approval.

**Denial**: If exception denied, requester notified with reason. Data deletion proceeds per standard schedule.

**3.4.4 Exception Monitoring**

[Organization] SHALL:
- Maintain Exception Register with all active and historical exceptions
- Review exceptions QUARTERLY for continued necessity
- Auto-expire exceptions at expiration date unless renewal requested
- Track exception trends and report to CISO quarterly
- Include exception summary in annual compliance assessment

**Exception Renewal**: Exceptions approaching expiration require renewal request 30 days before expiry. Renewal subject to same approval process.

**3.4.5 Exception Restrictions**

The following exceptions are PROHIBITED:
- ❌ Indefinite retention without specific end date
- ❌ Exceptions to avoid data subject erasure requests (unless legal exception applies per Section 3.2.3)
- ❌ Exceptions to circumvent regulatory retention requirements (must comply with legal minimums AND maximums)
- ❌ Blanket exceptions for entire data categories without specific justification
- ❌ Exceptions based solely on "might need someday" rationale

### 3.5 Policy Governance

**3.5.1 Policy Review**

**Annual Review**: Full policy review by CISO, DPO, and Legal/Compliance within 12 months of last approval.

**Review Participants**:
- CISO (policy owner, compliance assessment)
- DPO (privacy and data subject rights)
- Legal/Compliance Officer (regulatory requirements)
- CIO/IT Director (technical implementation feasibility)
- Records Manager (retention schedule alignment)
- Representatives from IT Operations, System Owners (operational feedback)

**Review Criteria**:
- Regulatory changes (GDPR amendments, new Swiss FADP guidance, sector regulations)
- Organizational changes (new business lines, M&A, geographic expansion)
- Technology changes (new storage technologies, cloud services, deletion tools)
- Incident lessons learned (deletion failures, data subject complaints, audit findings)
- Effectiveness metrics (deletion timeliness, verification coverage, exception volume)

**3.5.2 Triggered Reviews**

Policy review SHALL be triggered by:
- Significant regulatory changes (new data protection laws, regulatory guidance)
- Major organizational changes (mergers, acquisitions, new business lines)
- Significant incidents (deletion failure affecting >10,000 records, regulatory investigation)
- External audit findings (ISO 27001 certification audit, GDPR supervisory authority)
- Technology platform changes (cloud migration, new backup system)

**Triggered Review Timeline**: Initiated within 30 days of trigger event. Completed within 90 days.

**3.5.3 Policy Updates**

Policy changes categorized as:

**Minor Updates** (clarifications, references, formatting):
- CISO approval sufficient
- Communication to affected personnel within 30 days
- No formal training required
- Version increment: X.Y (e.g., 1.1, 1.2)

**Major Updates** (scope changes, new requirements, role changes):
- Full approval chain required (CISO → DPO → Legal → CIO → Executive Management)
- Organization-wide communication
- Training provided for personnel with deletion responsibilities
- Implementation timeline per change management process
- Version increment: X.0 (e.g., 2.0, 3.0)

**Emergency Updates** (critical threats, urgent regulatory compliance):
- CISO approval with retrospective executive management ratification
- Immediate implementation and communication
- Temporary measures documented with follow-up permanent policy revision

**3.5.4 Implementation Standard Updates**

Updates to implementation guidance (ISMS-IMP-A.8.10.x) and technical references (ISMS-REF-A.8.10):

**Authority**: CISO approves implementation updates without requiring full policy revision.

**Frequency**: As needed based on technology evolution, tool changes, or lessons learned.

**Communication**: Implementation updates communicated to IT operations, system owners, and affected personnel.

**Rationale**: Separation of policy (stable governance) from implementation (evolving technical procedures) enables technical agility without constant policy revision overhead.

**3.5.5 Communication and Training**

**Policy Publication**:
- Published in ISMS document repository
- Accessible to all personnel via intranet
- Version control maintained (current + previous versions)
- Change summary provided for each version

**Training Requirements**:

| Audience | Training Content | Frequency |
|----------|-----------------|-----------|
| **All Personnel** | Deletion policy awareness, data handling responsibilities | Annual (general security awareness) |
| **IT Operations** | Deletion procedures, tools, verification, logging | Initial + annual refresher + when procedures change |
| **System Owners** | System-specific deletion implementation, legal holds | Initial + annual refresher |
| **Data Owners** | Retention schedule definition, exception management | Initial + annual refresher |
| **DPO Office** | Data subject request handling, GDPR compliance | Initial + when regulations change |
| **Management** | Deletion governance, approval responsibilities, compliance reporting | Initial + annual briefing |

**Training Delivery**: Combination of e-learning modules, instructor-led sessions, procedure documentation, quick reference guides.

**Training Verification**: Training completion tracked in learning management system. Annual compliance reporting includes training completion metrics.

---

## 4. Implementation & References

### 4.1 Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):
- Deletion controls selected based on [Organization]'s risk assessment
- Data retention and exposure risk assessment determines deletion priorities
- Risk treatment plans document deletion control implementation
- Residual risks from incomplete deletion tracked in risk register

**Statement of Applicability** (ISO 27001 Clause 6.1.3):
- Control A.8.10 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported
- Control effectiveness measured through compliance assessments

**Related Controls**:
- **A.5.9** (Inventory of Information and Other Associated Assets): Asset inventory identifies systems and media requiring deletion
- **A.5.12** (Classification of Information): Data classification determines deletion method requirements
- **A.5.33** (Protection of Records): Records retention schedules define retention periods
- **A.5.34** (Privacy and Protection of PII): Privacy requirements drive retention limits and erasure obligations
- **A.7.14** (Secure Disposal or Re-use of Equipment): Physical equipment disposal procedures include data sanitization
- **A.8.11** (Data Masking): Alternative to deletion for test/development environments
- **A.8.24** (Use of Cryptography): Cryptographic erasure as deletion method
- **A.5.24** (Information Security Incident Management): Deletion failures handled as security incidents

**Information Flow**:
- **Asset Management** → Deletion: Asset decommissioning triggers media deletion
- **Data Classification** → Deletion: Classification level determines deletion method
- **Records Management** → Deletion: Retention expiry triggers deletion process
- **Privacy Management** → Deletion: Data subject requests trigger erasure
- **Contract Management** → Deletion: Contract termination triggers third-party deletion
- **Legal** → Deletion: Legal holds suspend deletion, releases resume deletion

### 4.2 Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.8.10 Suite):

The following implementation documents provide detailed procedures, assessment tools, and evidence collection:

- **ISMS-IMP-A.8.10.1**: Retention & Deletion Triggers Assessment
  - Data category inventory and classification
  - Retention schedule definition and documentation
  - Deletion trigger configuration (automated and manual)
  - Legal hold procedures and tracking
  - Excel workbook: Retention Schedule Assessment
  
- **ISMS-IMP-A.8.10.2**: Deletion Methods Assessment
  - Media-specific deletion procedure selection
  - Tool evaluation and approval process
  - Verification procedures and sampling
  - Backup deletion alignment
  - Excel workbook: Deletion Methods Inventory
  
- **ISMS-IMP-A.8.10.3**: Third-Party & Cloud Deletion Assessment
  - Cloud service provider deletion capability evaluation
  - Contract clause templates for deletion obligations
  - Third-party verification procedures
  - Provider deletion tracking and certificate management
  - Excel workbook: Third-Party Deletion Register
  
- **ISMS-IMP-A.8.10.4**: Verification & Evidence Assessment
  - Deletion logging and audit trail requirements
  - Evidence collection and retention procedures
  - Data subject request tracking
  - Compliance reporting and dashboards
  - Excel workbook: Evidence Register and Compliance Dashboard
  
- **ISMS-IMP-A.8.10.5**: Compliance Dashboard Consolidation
  - Executive summary reporting
  - KPI tracking and trending
  - Gap analysis and remediation tracking
  - Annual compliance assessment
  - Excel workbook: Executive Compliance Dashboard

**Technical Reference**:
- **ISMS-REF-A.8.10**: Deletion Methods Reference (detailed media-specific procedures, approved tools, industry standards alignment)

**Operational Forms**:
- **ISMS-FORM-A.8.10-GDPR**: Data Subject Erasure Request Form, deletion verification checklists, exception request forms, deletion log templates

**Cloud Provider Reference**:
- **ISMS-REF-A.5.23**: Cloud Service Provider Registry (deletion capabilities by provider tier)

### 4.3 Regulatory Mapping

This policy addresses deletion requirements from multiple regulatory frameworks:

| Requirement Category | Swiss nDSG | EU GDPR | ISO 27001 | PCI DSS* | HIPAA* | FINMA* | DORA/NIS2* |
|---------------------|-----------|---------|-----------|---------|--------|--------|------------|
| **Data Retention Limits** | Art. 6 | Art. 5(1)(e) | A.8.10 | Req. 3.1 | §164.316(b)(2) | Risk-Based | ICT Risk Mgmt |
| **Deletion Methods** | Art. 7 | Art. 32 | A.8.10 | Req. 9.8.2 | §164.310(d)(2)(i) | Risk-Based | Secure Disposal |
| **Data Subject Rights** | Art. 19 | Art. 17 | A.8.10 | N/A | N/A | Client Rights | N/A |
| **Third-Party Deletion** | Art. 8 | Art. 28(3)(g) | A.8.10 | Req. 12.10 | §164.308(b)(1) | Outsourcing | Critical Services |
| **Verification** | Art. 7 | Art. 5(2) | A.8.10 | Req. 12.10.7 | §164.530(i) | Audit Trail | Evidence |
| **Legal Holds** | OR 730a | Art. 17(3)(e) | A.8.10 | N/A | §164.530(j) | Legal Req | Legal Obligation |

*Conditional applicability per ISMS-POL-00

**Note**: Specific regulatory interpretation and compliance verification procedures are documented in ISMS-IMP-A.8.10.5 (Compliance Dashboard).

### 4.4 Training & Awareness

**Security Awareness** (All Personnel):
- Annual training module on data handling and deletion responsibilities
- User responsibilities for local data deletion (desktop, downloads, personal folders)
- Recognizing retention requirements and avoiding premature deletion
- Reporting deletion-related issues or questions

**Technical Training** (IT Operations, System Owners):
- Deletion tool configuration and operation
- Media-specific deletion procedures
- Verification and logging procedures
- Legal hold implementation
- Exception request evaluation
- Incident response for deletion failures

**Privacy Training** (DPO Office, Customer Service):
- Data subject erasure request handling
- GDPR Article 17 and Swiss nDSG compliance
- Identity verification procedures
- Legal basis assessment for erasure exceptions
- Third-party notification requirements

**Management Training** (Data Owners, System Owners, Management):
- Retention schedule definition and governance
- Exception approval decision-making
- Deletion risk assessment
- Compliance reporting interpretation

---

## 5. Definitions

**Information Deletion**: The process of removing data from storage media such that it cannot be recovered through normal or specialized means. Deletion may be logical (removing references) or physical (destroying media).

**Data Sanitization**: All methods of rendering data inaccessible, including clearing, purging, and destroying. Per NIST SP 800-88, sanitization ensures data cannot be retrieved regardless of future technology advances.

**Clear**: Logical sanitization that protects data against simple, non-invasive data recovery techniques. Suitable for media remaining within organizational control.

**Purge**: Physical or logical sanitization that protects data against laboratory attack techniques. Required for media leaving organizational control.

**Destroy**: Physical sanitization that renders media unusable and data recovery infeasible (disintegration, pulverization, melting, incineration).

**Cryptographic Erasure**: Deletion method that renders encrypted data irrecoverable by destroying or making inaccessible the encryption keys. Only effective if encryption was enabled from deployment.

**Retention Period**: The defined timeframe during which data must be kept before deletion is permitted or required. Driven by legal, regulatory, contractual, or business requirements.

**Deletion Trigger**: An event or condition that initiates the deletion process (retention period expiry, data subject request, contract termination, legal hold release, asset decommissioning).

**Legal Hold**: Suspension of deletion processes to preserve data required for litigation, investigation, or audit. Only Legal/Compliance Officer may initiate or release legal holds.

**Data Subject Erasure Request**: Request from data subject exercising right to erasure under GDPR Article 17 or Swiss nDSG. Requires identity verification, legal basis assessment, and 30-day response timeline.

**Certificate of Destruction (CoD)**: Third-party attestation that physical media was destroyed according to specified standards, typically provided by certified destruction vendors.

**Data Remanence**: Residual data remaining after deletion attempts. A key concern in cloud and shared infrastructure environments.

**Storage Limitation Principle**: GDPR Article 5(1)(e) requirement that personal data be kept only as long as necessary for processing purposes. Core privacy principle requiring timely deletion.

**Data Minimization**: Principle that personal data should be adequate, relevant, and limited to what is necessary. Deletion supports data minimization by removing unnecessary data.

**Chain of Custody**: Documentation tracking who had possession of media from identification through destruction, ensuring accountability.

**Verification**: Process of confirming deletion was successful, through technical validation (attempting recovery) or procedural confirmation (certificates, logs).

---

## Annex A: Deletion Decision Matrix (Quick Reference)

### Decision Flowchart

```
1. What is the data classification?
   ├─ Public → Use Clear method, log deletion
   ├─ Internal → Use Clear or Purge method, maintain deletion log
   ├─ Confidential → Use Purge method, obtain certificate
   └─ Restricted → Use Destroy or Crypto Erase, obtain certificate + verification

2. What is the media type?
   ├─ HDD (Magnetic) → ATA Secure Erase (reuse) OR Degauss/Destroy (disposal)
   ├─ SSD/NVMe → Crypto Erase OR Manufacturer Secure Erase OR Destroy
   ├─ Cloud Storage → API Delete + Crypto Erase (customer-managed keys)
   ├─ Mobile Device → Factory Reset + MDM Wipe + Crypto Erase
   ├─ Paper → Cross-Cut Shred (DIN 66399 P-4 or P-5)
   └─ Tape → Degauss OR Destroy (incinerate/shred)

3. Is media leaving organizational control?
   ├─ YES → Use Purge or Destroy method minimum
   └─ NO (internal reuse) → Use Clear or Purge based on classification

4. Are backups included?
   ├─ NO → STOP: Deletion incomplete, include backups
   └─ YES → Proceed

5. Is verification required?
   ├─ Public/Internal → Deletion log sufficient
   ├─ Confidential → Certificate + log required
   └─ Restricted → Certificate + verification + audit trail

6. Is legal hold active?
   ├─ YES → STOP: Deletion suspended pending hold release
   └─ NO → Proceed with deletion

7. Is this a data subject request?
   ├─ YES → Follow ISMS-FORM-A.8.10-GDPR procedure (30-day timeline)
   └─ NO → Follow standard retention schedule

8. Is third-party deletion needed?
   ├─ YES → Obtain Certificate of Deletion from provider
   └─ NO → Internal deletion only
```

### Media-Specific Quick Reference

| Media Type | Internal Reuse | External/Disposal | Verification |
|-----------|----------------|-------------------|--------------|
| **HDD** | ATA Secure Erase | Degauss OR Shred (≤2mm) | Certificate required for disposal |
| **SSD/Flash** | Crypto Erase OR Secure Erase | Crypto Erase + Shred (≤2mm) | Certificate required for disposal |
| **Cloud** | API Delete | API Delete + Key Destruction | API response + certificate |
| **Mobile** | MDM Wipe + Factory Reset | MDM Wipe + Destroy | MDM console log |
| **Paper** | Shred (P-4) | Shred (P-4 or P-5) | Certificate for large volumes |
| **Tape** | Overwrite | Degauss OR Incinerate | Certificate required |

### Retention Period Examples (Organization-Specific)

Note: Organizations define specific retention periods based on applicable regulations and business requirements. Examples below are illustrative only.

| Data Category | Typical Retention | Legal Basis | Deletion Trigger |
|--------------|-------------------|-------------|------------------|
| Tax Records | 10 years | Swiss Tax Law | Retention expiry |
| Employment Records | 10 years after termination | Swiss OR Art. 730a | Retention expiry |
| Customer Contracts | 10 years after termination | Swiss OR Art. 730a | Retention expiry |
| Marketing Consents | Until withdrawal | GDPR Consent | Consent withdrawal |
| Application Logs | 90 days | Internal policy | Automated purge |
| Backup Tapes | Aligned with production | Internal policy | Production deletion + backup purge |
| PII (no legal basis) | Delete immediately | GDPR Art. 17 | Data subject request OR purpose completion |

---

## Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Data Protection Officer (DPO)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements. Implementation procedures are documented in ISMS-IMP-A.8.10.*