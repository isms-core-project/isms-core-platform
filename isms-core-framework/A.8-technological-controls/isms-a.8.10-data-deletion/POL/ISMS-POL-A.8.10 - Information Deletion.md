<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.10:framework:POL:a.8.10 -->
**ISMS-POL-A.8.10 — Information Deletion Policy**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Information Deletion Policy |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.10 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [Date] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- Privacy: Data Protection Officer (DPO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.10.1 (Retention & Deletion Triggers Assessment)
- ISMS-IMP-A.8.10.2 (Deletion Methods Assessment)
- ISMS-IMP-A.8.10.3 (Third-Party & Cloud Deletion Assessment)
- ISMS-IMP-A.8.10.4 (Verification & Evidence Assessment)
- ISO/IEC 27001:2022 Control A.8.10

---

## Executive Summary

This policy establishes [Organisation]'s requirements for information deletion controls to ensure systematic deletion of information when no longer required, in accordance with ISO/IEC 27001:2022 Control A.8.10.

**Scope**: This policy applies to all information assets regardless of storage location (on-premises, cloud, third-party), all storage media types (magnetic, solid-state, optical, paper, mobile devices), all systems and applications (including backup infrastructure), and all data categories (personal data, business records, technical data, logs) throughout their lifecycle.

**Purpose**: Define organisational requirements for information deletion control implementation and governance. This policy establishes WHAT data requires deletion, WHEN deletion must occur, WHICH methods are approved, and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8.10.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss Federal Data Protection Act (nDSG) for data minimisation and right to erasure, EU GDPR Article 17 (Right to Erasure) where processing EU personal data, and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS v4.0.1, HIPAA, FINMA, DORA, NIS2) apply where [Organisation]'s business activities trigger applicability.

---

# Control Alignment & Scope

## ISO/IEC 27001:2022 Control A.8.10

**ISO/IEC 27001:2022 Annex A.8.10 - Information Deletion**

> *Information stored in information systems, devices or in any other storage media should be deleted when no longer required.*

**Control Objective**: Establish organisational policy for information deletion controls ensuring systematic removal of data when retention requirements are met, supporting data minimisation principles, regulatory compliance, and protection against unauthorised disclosure.

**This Policy Addresses**:

- Retention schedules and deletion triggers based on legal, regulatory, contractual, and business requirements
- Deletion methods appropriate to media types, data sensitivity, and regulatory requirements
- Verification and evidence requirements for demonstrating deletion occurred
- Third-party and cloud service provider deletion obligations and contractual requirements
- Data subject erasure rights (GDPR Article 17, Swiss nDSG)
- Legal hold management and exception handling
- Integration with [Organisation]'s data governance, privacy management, and risk assessment processes

## What This Policy Does

This policy:

- **Defines** information deletion requirements aligned with data classification, regulatory obligations, and organisational risk appetite
- **Establishes** governance framework for deletion decision-making, exception management, and compliance monitoring
- **Specifies** approved deletion methods and selection criteria based on media type and data sensitivity
- **References** applicable regulatory requirements per ISMS-POL-00 (Regulatory Applicability Framework)
- **Identifies** organisational roles and responsibilities for deletion control implementation and oversight
- **Integrates** with related controls including data classification (A.5.12), asset management (A.5.9), privacy protection (A.5.34), and secure disposal (A.7.14)

## What This Policy Does NOT Do

This policy does NOT:

- **Specify deletion tool vendors or products** (technology selection based on [Organisation]'s risk assessment and operational requirements)
- **Define system-specific deletion procedures** (see ISMS-IMP-A.8.10 Assessment Guides for environment-specific implementation)
- **Provide vendor-specific deletion instructions** (cloud provider deletion procedures documented in ISMS-IMP-A.8.10.3)
- **Replace data classification policy** (deletion builds on existing classification scheme per A.5.12)
- **Establish data retention schedules for all data types** (retention periods defined by Data Owners with legal/regulatory input, documented in ISMS-IMP-A.8.10.1)
- **Define access control mechanisms** (access controls covered by A.5.15, A.5.18, A.8.3 policies)
- **Replace cryptographic controls** (encryption for data protection covered by A.8.24 Cryptography Policy; cryptographic erasure as deletion method is within this policy's scope)
- **Mandate specific sanitization standards** (NIST SP 800-88 used as informational reference unless contractually required)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite evolving regulatory landscape, threat environment, and technology changes
- Technical agility for tool updates and infrastructure changes without policy revision
- Clear distinction between governance (WHAT/WHO in policy) and execution (HOW in implementation)
- Focused audit scope (auditors audit policy compliance and implementation effectiveness, not technical tool selection)
- Modular maintenance with independent versioning and targeted stakeholder reviews

## Scope

**This policy applies to**:

- **All information assets** (electronic and physical) containing organisational or personal data:
  - Personally Identifiable Information (PII) subject to GDPR/nDSG
  - Financial data (payment card data, financial records, transaction details)
  - Health information (medical records, employee health data)
  - Authentication credentials (passwords, API keys, tokens, private keys)
  - Proprietary business information (trade secrets, strategic data, pricing, contracts)
  - Technical data (source code, system configurations, network diagrams)
  - Communications (email, instant messages, call recordings)
  - System logs and audit trails
  - Any data classified as Confidential or Restricted per [Organisation]'s classification scheme

- **All storage locations**:
  - On-premises infrastructure (data centers, server rooms, local storage)
  - Cloud environments (IaaS, PaaS, SaaS across all providers)
  - Third-party processors (managed service providers, subcontractors, outsourced services)
  - Backup and disaster recovery systems (on-site, off-site, cloud-based)
  - End-user devices (laptops, desktops, mobile devices, removable media)
  - Archives (physical records storage, cold storage, magnetic tape)
  - Colocation facilities and hosted infrastructure

- **All storage media types**:
  - Magnetic storage (hard disk drives, magnetic tape)
  - Solid-state storage (SSDs, flash drives, SD cards)
  - Optical media (CDs, DVDs, Blu-ray)
  - Paper records (printed documents, forms, records)
  - Mobile devices (smartphones, tablets, wearables)
  - Network-attached storage (NAS, SAN)
  - Cloud-native storage (object storage, block storage, file storage)

- **All lifecycle stages**:
  - Operational systems (production databases, active file shares)
  - Archived data (compliance archives, inactive records)
  - Backup retention (daily, weekly, monthly, yearly backups)
  - End-of-life disposal (decommissioned systems, retired media)
  - Non-production environments (development, test, QA, training, sandbox)

- **All organisational personnel and third parties**:
  - Employees (permanent, temporary, interns)
  - Contractors and consultants
  - Third-party service providers processing organisational data
  - Cloud service providers storing organisational information
  - Outsourced development teams and managed service providers
  - All business units and geographic locations within [Organisation]

**Out of Scope**:

- **Active legal hold data**: Deletion suspended per litigation, investigation, or regulatory examination requirements (covered under separate legal hold procedures in Section 2.6)
- **Data required for ongoing regulatory examination**: Deletion deferred until examination completion; DPO/Legal approval required to suspend deletion
- **Archival records with permanent retention mandates**: Deletion not applicable per regulatory or business requirements (e.g., corporate records with perpetual retention); documented in retention schedule
- **Third-party data where [Organisation] acts as processor only**: Deletion executed per data controller instruction, not independent [Organisation] decision (contractual obligation, not policy-driven)
- **Public information intentionally published**: Deletion of published content follows separate content management and publication withdrawal procedures
- **Anonymized data**: Data that has been irreversibly anonymized (no longer identifies individuals) does not require deletion under privacy regulations but may have business-driven retention limits

**Note**: Out-of-scope items do not exempt systems from assessment. ISMS-IMP-A.8.10 assessments determine applicability; documented exclusions require business justification and approval.

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Deletion Requirements |
|------------|---------------|---------------------------|
| **Swiss nDSG (FADP)** | All Swiss operations | Art. 6 - Data minimisation principle; Art. 12 - Data subject right to erasure; Art. 25 - Appropriate technical and organisational security measures; Art. 30 - Adequate security for data processing |
| **EU GDPR** | When processing EU personal data | Art. 5(1)(e) - Storage limitation principle (keep data no longer than necessary); Art. 17 - Right to erasure ("right to be forgotten"); Art. 19 - Notification of erasure to third parties; Art. 32 - Security of processing including deletion controls |
| **ISO/IEC 27001:2022** | Certification scope | Control A.8.10 - Documented information deletion policy and procedures, implemented controls, evidence of deletion effectiveness |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Deletion Requirements |
|-----------|-------------------|----------------------|
| **PCI DSS v4.0.1** | Processing payment card data | Req. 3.1 - Retain cardholder data only as long as needed for business/legal requirements; Req. 3.2 - Secure deletion of cardholder data when no longer needed; Req. 12.3.4 - Data retention and disposal procedures |
| **HIPAA Security Rule** | Processing US healthcare data (ePHI) | §164.310(d)(2)(i) - Disposal standard requiring procedures for disposal of ePHI and hardware/media containing ePHI; §164.316(b)(2)(i) - Retain documentation for 6 years |
| **FINMA** | Swiss regulated financial institution | Record retention per FINMA Circular 2008/21; secure deletion after retention period; outsourcing risk management (FINMA Circular 2018/3) including data deletion |
| **DORA** | EU financial services entity (ICT risk) | Art. 11 - ICT business continuity including backup and restoration; Art. 28 - ICT third-party risk management including data deletion upon contract termination |
| **NIS2** | Essential/important entity (EU) | Art. 21 - Cybersecurity risk management including data security and deletion; incident handling and business continuity |
| **SOX** | US publicly traded company | 7-year retention for audit records; secure deletion afterward to prevent unauthorised access |
| **CCPA/CPRA** | Processing California residents' data | §1798.105 - Consumer right to deletion; business and service provider deletion obligations; verification requirements |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- **NIST SP 800-88 Rev. 1** - Guidelines for Media Sanitization (Clear, Purge, Destroy methods)
- **ISO/IEC 27040:2015** - Storage security including sanitization guidance
- **ISO/IEC 27555:2024** - Guidelines on personally identifiable information deletion
- **ISO/IEC 27017:2015** - Cloud services information security controls (deletion guidance)
- **DIN 66399** - Destruction of data media (German standard for paper/media destruction, 7 security levels)
- **DoD 5220.22-M** - National Industrial Security Program (legacy standard, superseded by NIST SP 800-88 for US federal)

**Compliance Determination**: [Organisation] determines applicable Tier 2 regulations through periodic business activity assessment coordinated by DPO and Legal/Compliance. Applicability is documented in [Organisation]'s regulatory compliance register and reviewed annually. The most stringent requirements apply where multiple regulations overlap.

---

# Information Deletion Requirements Framework

## Retention and Deletion Triggers

[Organisation] implements retention schedules defining when deletion is required or permitted.

**Data Inventory and Classification**:

[Organisation] SHALL maintain a comprehensive inventory of data categories processed, including:

- Data type and format (structured databases, unstructured files, email, logs, backups)
- Data classification level per [Organisation]'s classification scheme (Restricted, Confidential, Internal, Public)
- Business purpose and processing rationale
- Storage location (system, environment, media type)
- Data owner responsible for retention and deletion decisions

**Inventory Completeness Verification**:

Inventory completeness SHALL be verified through:

- **(a) Automated discovery tools** for IT systems (scanning databases, file shares, cloud storage)
- **(b) Annual attestation** from System Owners confirming all data categories in their systems are registered in inventory
- **(c) Quarterly reconciliation** of inventory against IT asset register (per ISMS-POL-A.5.9) and cloud service registry (per ISMS-REF-A.5.23)

**Retention Schedule Requirements**:

[Organisation] SHALL establish retention schedules for all data categories based on:

- **Legal requirements**: Statutes, regulations, court orders mandating specific retention periods
- **Regulatory requirements**: Industry-specific regulations (PCI DSS, HIPAA, FINMA) specifying retention
- **Contractual obligations**: Customer contracts, supplier agreements, service level agreements requiring retention
- **Documented business needs**: Operational requirements, historical analysis, business continuity justified and approved by Data Owner

Retention schedules SHALL document:

- Data category and subcategories
- Minimum retention period (legal/regulatory floor)
- Maximum retention period (data minimisation ceiling)
- Retention period rationale (legal citation, business justification)
- Data owner and approval
- Review date (annual minimum)

**Deletion Triggers**:

Deletion SHALL be triggered by one of the following events:

**(a) Retention period expiry**: Data reaches end of approved retention period per retention schedule

**(b) Data subject erasure request**: Individual exercises right to erasure under GDPR Article 17 or Swiss nDSG (see Section 2.5)

**(c) Contract or service agreement termination**: Contractual relationship ends, data retention obligation ceases

**(d) Processing purpose completion**: Original purpose for data collection/processing no longer applies

**(e) Legal hold release**: Litigation, investigation, or regulatory examination concludes, legal hold is lifted (see Section 2.6)

**(f) Asset decommissioning**: IT system, device, or storage media reaches end-of-life and requires disposal

**(g) Consent withdrawal**: Data subject withdraws consent for processing (where consent is legal basis per GDPR Art. 6(1)(a))

**Retention Period Conflicts**:

Where multiple retention requirements apply to the same data:

- The **LONGEST applicable retention period** SHALL be implemented to ensure compliance with all obligations
- Legal counsel review is required where retention period conflicts involve regulatory vs. contractual obligations
- Conflicts are documented in retention schedule with resolution rationale

**Automated Deletion Processes**:

[Organisation] SHOULD implement automated deletion processes where technically feasible, including:

- Retention metadata tagging (creation date, retention period, deletion date)
- Automated deletion scheduling based on retention rules
- Safeguards against premature deletion:
  - Legal hold checks before deletion execution
  - Business owner approval workflow for high-value or business-critical data
  - Deletion confirmation and logging

**Automated Deletion Feasibility Assessment**:

Technical feasibility assessment for automated deletion SHALL consider:

**(a) System capabilities**: API support for deletion and verification; data structure (structured databases vs. unstructured file shares)

**(b) Trigger availability**: Retention metadata exists or can be implemented; lifecycle policies supported by system

**(c) Safeguards**: Legal hold integration possible; business-critical data approval workflow implementable; deletion rollback or recovery possible if needed

**(d) Risk vs. effort analysis**: Manual process risk (missed deletions, inconsistent execution, human error) vs. automation development cost and maintenance

Feasibility assessments SHALL be:

- Documented by System Owners during system onboarding (initial assessment)
- Reviewed annually (continued appropriateness assessment)
- Approved by CISO where automation is deemed infeasible

Where automation is deemed infeasible, manual deletion procedures SHALL be documented in system-specific implementation supplements with defined verification checkpoints.

**Implementation Note**: Data inventory methodology, retention schedule templates, deletion trigger workflows, and feasibility assessment procedures are documented in **ISMS-IMP-A.8.10.1 (Retention & Deletion Triggers Assessment)**.

---

## Deletion Method Requirements

[Organisation] implements deletion methods appropriate for media type, data sensitivity, and regulatory requirements.

**Deletion Method Selection**:

[Organisation] SHALL select deletion methods appropriate for:

- **Media type**: Magnetic (HDD), solid-state (SSD), optical (CD/DVD), paper, cloud storage, tape
- **Data classification level**: Restricted/Confidential requires stronger methods than Internal/Public
- **Media destination**: Internal reuse vs. external transfer vs. disposal/destruction
- **Recovery risk assessment**: Likelihood and impact of unauthorised data recovery

**Approved Deletion Methods**:

Deletion methods SHALL align with recognized sanitization standards (NIST SP 800-88 or equivalent):

| Method | NIST SP 800-88 Level | Description | Use Cases |
|--------|---------------------|-------------|-----------|
| **Clear** | Clear | Logical techniques (overwriting, block erasure) protecting against simple non-invasive recovery | Media remaining in organisational control with lower sensitivity data; file-level deletion |
| **Purge** | Purge | Physical or logical techniques protecting against laboratory attack (degaussing, cryptographic erasure, secure erase) | Media leaving organisational control; sensitive data; end-of-lease equipment |
| **Destroy** | Destroy | Physical destruction rendering media unusable (shredding, pulverizing, incineration, disintegration) | End-of-life media; highest sensitivity data; media with failed purge |

**Deletion Method by Media Type**:

| Media Type | Acceptable Methods | Notes |
|------------|-------------------|-------|
| **Magnetic HDD** | Overwrite (7+ passes for sensitive), Degauss, Physical destruction | ATA Secure Erase acceptable if supported |
| **Solid-State (SSD, Flash)** | Cryptographic erasure (preferred), Secure erase command, Physical destruction | Overwriting unreliable due to wear leveling; secure erase must verify success |
| **Optical Media** | Physical destruction (shredding, pulverizing) | Overwriting not applicable; purge-level destruction required |
| **Magnetic Tape** | Degaussing, Physical destruction | Overwriting acceptable for Clear but time-intensive |
| **Paper Records** | Cross-cut shredding (DIN 66399 P-4 minimum for Confidential) | Security level based on data sensitivity |
| **Mobile Devices** | Factory reset + encryption verification, Physical destruction if high-sensitivity | Verify encryption was enabled; factory reset alone insufficient for Restricted data |
| **Cloud Storage (IaaS/PaaS)** | API deletion + verification, Cryptographic erasure if customer-managed keys | Verify multi-region deletion; snapshot/backup deletion |
| **Cloud Storage (SaaS)** | Provider deletion process per contract, Obtain deletion certificate | Limited customer control; rely on provider SOC 2 deletion controls |

> **Detailed Guidance**: Annex A provides comprehensive deletion method selection matrix, NIST SP 800-88 mapping, method-specific requirements (overwriting, ATA Secure Erase, cryptographic erasure, degaussing, physical destruction), and backup/cloud deletion coordination procedures for all media types.

**Production System Deletion**:

Deletion in production systems SHALL extend to:

- **ALL backup copies**: Incremental/differential backups, full backups, snapshots, disaster recovery replicas
- **ALL replicas and mirrors**: Database replicas, storage mirrors, CDN caches
- **ALL temporary copies**: Swap files, page files, temporary processing files, system caches
- **ALL log files**: Application logs, system logs, access logs containing the deleted data

**Backup Deletion Verification**:

Backup deletion verification SHALL account for backup technology architecture:

**(a) Full/incremental/differential backup dependencies**: Verify deleted data is absent from all backup sets within retention window; backup catalog queries confirm absence

**(b) Snapshot-based backups with retention policies**: Verify snapshots containing deleted data are expired or deleted per retention policy; retention policy enforcement logs

**(c) Cloud-native backup services with independent retention**: API queries confirm recovery points containing deleted objects no longer exist; OR retention policy configured with maximum acceptable retention approved by Data Owner

**(d) Application-level backups** (database dumps, VM exports): Dump manifests confirm deleted tables/records are excluded; OR documented dump rotation schedule guaranteeing deletion by date certain

Where immediate backup deletion is not technically feasible (e.g., incremental backup chains require full backup set rotation), **maximum retention SHALL be documented** and approved by CISO + Data Owner.

**Approval for Deferred Backup Deletion**: Where backup deletion verification identifies "immediate deletion is not technically feasible" requiring documented maximum retention period, approval SHALL be obtained from:

- **CISO** (all cases - approves risk of deferred deletion)
- **Data Owner** (approves business acceptability of extended retention)
- **DPO** (if personal data - confirms GDPR/nDSG compliance with documented retention limit)

Approval SHALL be documented in exception register (per Section 3.3) if deferred deletion exceeds 90 days beyond standard retention period.

**Cryptographic Erasure as Deletion Method**:

Where technically feasible, [Organisation] SHOULD leverage cryptographic erasure for high-efficiency deletion:

- **Data-to-key mapping**: Document which encryption keys protect which data categories
- **Key destruction procedures**: Implement key destruction meeting NIST SP 800-88 "Purge" level (cryptographic erase of key storage, HSM key zeroization)
- **Key destruction verification**: Verify through key management system audit logs or HSM certificates
- **Evidence retention**: Retain key destruction evidence per Section 2.4 (3+ years minimum)
- **Integration with A.8.24**: Key management lifecycle per ISMS-POL-A.8.24 (Cryptography Policy)

For cryptographic erasure to constitute deletion per this policy, destruction of encryption keys must render encrypted data **irrecoverable** (no key recovery, no key escrow, no retained key backups).

**Prohibited Deletion Practices**:

The following practices are NOT acceptable as deletion methods:

- **File deletion without overwriting**: Simple "delete" or "recycle bin" leaving data recoverable
- **Quick format without overwriting**: File system metadata cleared but data remains
- **Single-pass overwrite for solid-state media**: Wear leveling makes overwriting unreliable for SSDs
- **Degaussing solid-state or optical media**: Ineffective on non-magnetic media
- **Encryption without key destruction**: Encrypted data with retained keys is not deleted
- **Renaming or moving files**: Obscurity is not deletion

**Implementation Note**: Detailed deletion method specifications, media-specific procedures, tool configurations, and validation testing are documented in **ISMS-IMP-A.8.10.2 (Deletion Methods Assessment)**.

---

## Third-Party and Cloud Deletion

[Organisation] implements deletion obligations for third parties and cloud service providers processing organisational data.

**Third-Party Deletion Contractual Requirements**:

[Organisation] SHALL include deletion obligations in all contracts with third parties processing organisational data:

**(a) Maximum deletion timeline**: Data deleted within specified timeframe after contract termination or upon request (30-90 days typical)

**(b) Sanitization standards**: Deletion methods appropriate for data sensitivity (reference to NIST SP 800-88 or equivalent)

**(c) Deletion scope**: All copies including backups, replicas, archives, disaster recovery, and development/test environments

**(d) Deletion certificate requirement**: Provider must provide deletion certificate or attestation confirming deletion completion

**(e) Flow-down to sub-processors**: Deletion requirements apply to all sub-processors; provider ensures compliance

**(f) Audit rights**: [Organisation] retains right to verify deletion through audit or inspection

**Cloud Service Provider Deletion Assessment**:

[Organisation] SHALL assess cloud service provider deletion capabilities before engagement using the following minimum criteria:

**(a) API deletion support**: Programmatic deletion and verification capability (vs. manual ticket process)

**(b) Deletion timeline commitments**: SLA-backed deletion timeline (e.g., "deleted within 30 days of request")

**(c) Multi-tenant isolation verification**: Customer data deletion does not impact other tenants; provider demonstrates isolation

**(d) Geographic deletion coverage**: Deletion occurs in all regions where data replicates (verify multi-region coordination)

**(e) Backup/snapshot deletion process**: Explicit inclusion of backups in deletion scope OR documented exclusion with retention limit

**(f) Deletion audit trail availability**: Deletion logs accessible to customer for compliance verification

Assessment results SHALL be documented in **ISMS-REF-A.5.23 (Cloud Service Provider Registry)**.

**Third-Party Deletion Verification**:

[Organisation] SHALL obtain verification of deletion from third parties through:

**(a) Certificates of destruction** (for physical media destruction):
- Media serial numbers or asset identifiers
- Destruction method referencing NIST SP 800-88 level (Clear/Purge/Destroy)
- Destruction date and location
- Certificate issuer name and accreditation (e.g., NAID AAA, ISO 21964) if applicable

**(b) Audit reports** (for service provider logical deletion):
- SOC 2 Type II report with deletion control testing, OR
- Independent audit report verifying deletion procedures, OR
- ISO 27001 certification with Annex A.8.10 in scope

**(c) API response logging** (for cloud/SaaS deletion):
- API call timestamp and authenticated user
- Resource identifier (object key, database record ID, storage path)
- HTTP success response (200/204) or provider-specific deletion confirmation
- Confirmation of backup/snapshot deletion where provider offers this capability

**For High/Critical classification data**: Certificates from accredited destruction vendors (NAID AAA, ISO 21964) OR independent audit reports are REQUIRED (API logs alone are insufficient).

**Third-Party Deletion Failure Escalation**:

When third party fails to provide deletion verification or misses deletion timeline:

| Timeline | Action | Responsible |
|----------|--------|-------------|
| **T+0 days** | IT Operations logs failure in gap register, initiates follow-up with third-party contact | IT Operations |
| **T+15 days** | System Owner escalates to third-party account manager, CCs CISO + DPO | System Owner |
| **T+30 days** | CISO escalates to third-party executive contact, initiates contract review with Legal | CISO |
| **T+45 days** | Executive Management reviews contractual remedies (service credits, termination for material breach), considers data replication to compliant provider | Executive Mgmt |

**For high-sensitivity data**: Escalation accelerated (T+7, T+15, T+21, T+30 days).

**Implementation Note**: Cloud provider deletion assessment criteria, third-party contract templates, deletion verification procedures, and escalation workflows are documented in **ISMS-IMP-A.8.10.3 (Third-Party & Cloud Deletion Assessment)**.

---

## Verification and Evidence Requirements

[Organisation] maintains comprehensive evidence of deletion to demonstrate compliance.

**Deletion Audit Trail**:

[Organisation] SHALL maintain comprehensive deletion audit trails including:

- **Deletion timestamp**: Date and time deletion occurred
- **Data category**: Type of data deleted (PII, financial, credentials, etc.)
- **Deletion method**: Technique used (Clear, Purge, Destroy, cryptographic erasure)
- **Media identifier**: System, device, or storage location where deletion occurred
- **Deletion trigger**: Event triggering deletion (retention expiry, data subject request, contract termination)
- **Responsible party**: Person or system executing deletion
- **Verification result**: Confirmation deletion was successful or failure details

Deletion logs SHALL be:

- **Tamper-evident**: Protected against unauthorised modification (write-once logging, cryptographic signing, SIEM integration)
- **Retained**: Minimum **3 years** or per applicable regulatory requirements (whichever is longer)
- **Accessible**: Available for audit, compliance verification, and data subject inquiries

**Deletion Certificates**:

[Organisation] SHALL generate or obtain deletion certificates for:

- **High/Critical sensitivity data**: All deletion of Restricted or Confidential data
- **Third-party deletion**: All deletion performed by external parties (see Section 2.3)
- **Physical media destruction**: All physical destruction of storage media
- **Data subject erasure requests**: All GDPR/nDSG erasure requests (see Section 2.5)

Deletion certificates SHALL include:

- Certificate identifier and issue date
- Data category and classification level
- Deletion method and standard (NIST SP 800-88 level)
- Media identifier or system
- Responsible party (internal personnel or external vendor)
- Verification signature or attestation

**Third-Party Deletion Verification**:

Third-party deletion certificates SHALL meet sufficiency criteria per Section 2.3. Certificates, audit reports, or API logs are reviewed by IT Operations for completeness:

- **Certificates**: Contains media IDs, NIST method, date, issuer? (Yes/No)
- **Audit Reports**: SOC 2 Type II with deletion controls OR independent audit? (Yes/No)
- **API Logs**: Timestamp, resource ID, success response, backup confirmation? (Yes/No)
- **High/Critical Data**: Accredited certificate or independent audit? (Yes/No - required)

If evidence is insufficient, IT Operations requests corrected evidence; escalates per Section 2.3 if not provided within 15 days.

**Deletion Verification Procedures**:

[Organisation] SHALL implement verification procedures to confirm deletion effectiveness:

**(a) Automated confirmation**: Deletion scripts/tools generate success/failure logs

**(b) Periodic sampling**: Quarterly sampling of deleted data to verify non-recoverability (attempt to access deleted files, query deleted database records)

**(c) Attestations**: System Owners attest annually that deletion controls are operating as designed in their environments

**(d) Third-party verification**: External audit or testing verifying deletion effectiveness (annual minimum for high-risk systems)

**Evidence Requirements**:

[Organisation] SHALL maintain the following evidence types to demonstrate deletion control effectiveness:

| Evidence Type | Purpose | Owner | Retention |
|---------------|---------|-------|-----------|
| **Deletion execution logs** | Prove deletions occurred per schedule | IT Operations | 3 years minimum |
| **Retention schedule** | Define required retention by data category | Records Manager | Current + superseded versions (7 years) |
| **Third-party deletion certificates** | Verify third-party deletion compliance | IT Operations | 3 years from deletion date |
| **Data subject request log** | Demonstrate GDPR/nDSG rights compliance | DPO | 3 years from request closure |
| **Legal hold register** | Justify deletion suspension | Legal/Compliance | 3 years from hold release |
| **Exception approvals** | Document approved deviations | CISO | Life of exception + 3 years |
| **Quarterly compliance reports** | Aggregate deletion metrics, gap analysis | CISO | 3 years |
| **Data inventory** | Establish deletion scope | Records Manager | Current + quarterly snapshots (3 years) |

Evidence generation and aggregation procedures are defined in **ISMS-IMP-A.8.10.4 (Verification & Evidence Assessment)**.

**Implementation Note**: Verification methodology, evidence register templates, sampling procedures, and Summary Dashboard specifications are documented in **ISMS-IMP-A.8.10.4**.

---

### Consolidated Evidence Requirements

[Organisation] SHALL maintain the following evidence types to demonstrate deletion control effectiveness:

| Evidence Type | Purpose | Maintained By | Retention Period | Location/System |
|---------------|---------|---------------|------------------|-----------------|
| **Deletion execution logs** | Prove deletions occurred per schedule with 7 required fields (timestamp, data category, method, media ID, trigger, responsible party, verification result) | IT Operations | 3 years minimum | [Logging system - e.g., SIEM, centralized log repository] |
| **Retention schedule** | Define approved retention periods by data category with legal/regulatory basis | Records Manager | Current version + superseded versions (7 years) | [Document repository] |
| **Third-party deletion certificates** | Verify third-party deletion compliance per Section 2.3 sufficiency criteria | IT Operations | 3 years from deletion date | Evidence register (ISMS-IMP-A.8.10.4) |
| **Data subject request log** | Demonstrate GDPR/nDSG rights compliance with 30-day timeline | DPO | 3 years from request closure | [DPO system - e.g., privacy management platform] |
| **Legal hold register** | Justify deletion suspension with quarterly review documentation | Legal/Compliance | 3 years from hold release | [Legal system - e.g., matter management system] |
| **Exception approvals** | Document approved deviations with risk acceptance | CISO | Life of exception + 3 years | Exception register (ISMS-IMP-A.8.10.3) |
| **Quarterly compliance reports** | Aggregate deletion metrics, gap analysis, remediation tracking | CISO | 3 years | [GRC platform or document repository] |
| **Data inventory** | Establish deletion scope with completeness verification | Records Manager | Current + quarterly snapshots (3 years) | [Data governance system] |
| **Backup deletion verification records** | Prove backup purging per Section 2.2 requirements | IT Operations | 3 years | [Backup system logs, evidence register] |
| **Automated deletion feasibility assessments** | Document feasibility decisions per Section 2.1 | System Owners | Life of system + 3 years | [System documentation repository] |

**Evidence Generation and Aggregation**: Procedures for evidence collection, validation, and aggregation are defined in ISMS-IMP-A.8.10.4 (Verification & Evidence Assessment).

**Evidence Accessibility**: All evidence SHALL be readily accessible to auditors, regulators, and internal compliance reviews. Evidence requests SHALL be fulfilled within **5 business days** for routine reviews, **24 hours** for regulatory examinations.

---

## Data Subject Erasure Requests

[Organisation] implements procedures for handling data subject erasure requests in compliance with GDPR Article 17 and Swiss nDSG.

**Request Acceptance and Logging**:

[Organisation] SHALL accept and process data subject erasure requests:

**(a) Multiple channels**: Accept requests via email, web form, postal mail, or in-person at [Organisation] offices

**(b) Immediate logging**: Log all requests within **24 hours** of receipt in data subject request register

**(c) Identity verification**: Verify data subject identity before processing erasure request using:
- Government-issued ID verification (passport, national ID)
- Account authentication (login credentials for existing customers)
- Personal information confirmation (answers to security questions, account details)
- In-person identification at [Organisation] offices

**(d) Response timeline**: Respond to data subject within **30 days** (GDPR deadline) confirming:
- Receipt of request
- Identity verification status
- Assessment of erasure obligation (approved or denied with legal basis)
- Expected completion date for approved requests

**Legal Assessment of Erasure Obligation**:

The DPO SHALL assess whether erasure obligation applies or legal exceptions exist:

**Erasure is REQUIRED when**:
- Personal data is no longer necessary for purposes collected
- Data subject withdraws consent (where consent was legal basis per GDPR Art. 6(1)(a))
- Data subject objects to processing and no overriding legitimate grounds exist (GDPR Art. 21)
- Personal data has been unlawfully processed
- Erasure is required for compliance with legal obligation (EU or Member State law)
- Personal data was collected for information society services offered to children (GDPR Art. 8)

**Erasure may be DENIED when** (GDPR Art. 17(3) exceptions):
- Processing is necessary for exercising freedom of expression and information
- Processing is necessary for compliance with legal obligation (EU/Member State law requiring retention)
- Processing is necessary for public interest or official authority
- Processing is necessary for public health purposes in the public interest
- Processing is necessary for archiving purposes in the public interest, scientific/historical research, statistical purposes
- Processing is necessary for establishment, exercise, or defense of legal claims

**Exception Documentation**:

Where erasure is denied based on legal exception, [Organisation] SHALL:

**(a) Document specific legal basis**: Identify which GDPR Article 17(3) exception applies with detailed justification

**(b) Provide written explanation**: Inform data subject in writing of:
- Which exception applies and why
- Legal basis for denial (cite specific regulation, statute, or legitimate interest)
- Right to lodge complaint with supervisory authority (Swiss FDPIC, EU DPA)
- Right to judicial remedy

**(c) Implement restriction of processing**: Where erasure is denied but data subject contests lawfulness, implement restriction of processing per GDPR Article 18 (mark data, limit access, notify data subject)

**Third-Party Notification**:

Where personal data was disclosed to third parties (service providers, partners, public authorities), [Organisation] SHALL notify them of the erasure request per GDPR Article 19:

**(a) Identification of third parties**: Identify all third parties who received the personal data (from disclosure logs, data processing agreements)

**(b) Notification content**: Inform third parties of:
- Data subject erasure request
- [Organisation]'s obligation to erase
- Third party's obligation to erase (if they are controller) or to inform their recipients (if they re-disclosed)

**(c) Notification timeline**: Notify third parties within **7 days** of executing erasure (allow time for third parties to comply)

**(d) Exceptions**: Notification NOT required if notification proves impossible or involves disproportionate effort (document rationale)

**(e) Evidence retention**: Retain third-party notification records (email confirmations, acknowledgments) for 3+ years

**Erasure Execution**:

Approved erasure requests SHALL be executed:

**(a) Scope**: Erase all personal data of the data subject across:
- Production systems (databases, file shares, CRM, email)
- Backup systems (per backup deletion requirements in Section 2.2)
- Archives (long-term retention systems)
- Third-party processors (per Section 2.3)
- Development/test environments (if personal data present)
- Logs (application logs, access logs, system logs)

**(b) Timeline**: Complete erasure within **60 days** of request receipt (allowing 30 days for assessment + 30 days for execution)

**(c) Verification**: Verify erasure completeness through:
- Database queries confirming absence of personal data identifiers
- File system searches confirming file deletion
- Third-party deletion certificates (per Section 2.3)
- Backup verification (per Section 2.2 backup deletion requirements)

**(d) Confirmation to data subject**: Notify data subject of erasure completion including:
- Date of erasure completion
- Scope of erasure (systems, third parties notified)
- Any retained data with legal basis (e.g., billing records for tax compliance)

**Legal Hold Conflict**:

When data subject erasure request conflicts with legal hold:

**(a) Restriction of processing**: Apply restriction of processing per GDPR Article 18:
- Mark data as "restricted - pending legal hold release"
- Limit access to data (only Legal/Compliance, no business use)
- Notify data subject of restriction and legal hold reason

**(b) Execute upon hold release**: Delete data immediately upon legal hold release (within 30 days)

**(c) Quarterly review**: Review legal hold + erasure request conflicts quarterly to assess continued necessity

**Data Subject Request Log**:

DPO SHALL maintain data subject request log including:

| Field | Description |
|-------|-------------|
| **Request ID** | Unique identifier |
| **Receipt Date** | Date request received |
| **Request Channel** | Email, web form, postal, in-person |
| **Data Subject** | Name and contact (anonymized after closure) |
| **Identity Verification** | Method and date |
| **Request Type** | Erasure, access, rectification, portability, objection |
| **Assessment** | DPO decision (approve, deny, partial) |
| **Legal Basis** | GDPR Art. 17(3) exception if denied |
| **Execution Date** | Date erasure completed |
| **Third-Party Notification** | Third parties notified and dates |
| **Response Date** | Date data subject notified |
| **Status** | Open, In Progress, Completed, Denied |

Log retention: **3 years** from request closure (or longer if regulatory examination requires)

**Implementation Note**: Data subject erasure request procedures, identity verification methods, legal assessment criteria, third-party notification templates, and request log specifications are documented in **ISMS-IMP-A.8.10.4 (Verification & Evidence Assessment)** and supported by **Annex B: Data Subject Erasure Request Template**.

> **Complete Workflow**: Annex B provides the full data subject erasure request form template including identity verification procedures, legal assessment framework (GDPR Art. 17(1) grounds vs. Art. 17(3) exceptions), execution tracking tables, third-party notification requirements (GDPR Art. 19), restriction of processing procedures (GDPR Art. 18), and post-closure quality review checklists.

---

## Legal Hold Management

[Organisation] implements legal hold procedures to suspend deletion when required by litigation, investigation, or regulatory examination.

**Legal Hold Definition**:

A **legal hold** (litigation hold) is a suspension of normal deletion processes to preserve data for:

- **Litigation**: Filed lawsuits, threatened litigation, or reasonably anticipated litigation
- **Government investigation**: Regulatory investigation, law enforcement inquiry, subpoena, search warrant
- **Internal investigation**: Fraud investigation, ethics violation, security incident requiring forensic preservation
- **External audit**: Regulatory examination, financial audit, compliance audit requiring specific data preservation

**Legal Hold Authority**:

ONLY the **Legal/Compliance Officer** may:

**(a) Initiate legal hold**: Issue legal hold notice based on legal counsel advice or regulatory requirement

**(b) Define hold scope**: Specify:
- Data categories subject to hold (email, documents, databases, specific records)
- Custodians (employees, systems, storage locations)
- Time period (start date, anticipated end date or trigger condition)
- Hold reason (case name, investigation reference, regulatory examination)

**(c) Release legal hold**: Authorise hold release when legal obligation ceases (litigation settled, investigation closed, audit completed)

No other role may suspend deletion without Legal/Compliance Officer authorisation.

**Legal Hold Process**:

**(a) Hold notification**: Legal/Compliance Officer issues legal hold notice to:
- IT Operations (implement technical hold on deletion processes)
- System Owners (custodians of data subject to hold)
- Records Manager (suspend retention schedule deletion triggers)
- DPO (for holds affecting personal data subject to erasure requests)

**(b) Technical implementation**: IT Operations implements hold:
- Flag data subject to hold in systems (database flags, file metadata, backup exclusions)
- Suspend automated deletion processes for held data
- Configure backup retention to extend held data beyond normal retention
- Document hold implementation date and scope

**(c) Hold register**: Legal/Compliance Officer maintains legal hold register documenting:
- Hold ID and initiation date
- Hold reason (case/investigation reference)
- Scope (data categories, custodians, time period)
- Hold owner (attorney, investigator, auditor)
- Systems/storage locations affected
- Implementation date (when hold technically enforced)
- Quarterly review dates and outcomes
- Release date and release authorisation

**Quarterly Legal Hold Review**:

Legal holds SHALL be reviewed **at least quarterly** to assess continued necessity.

**Review Process**:

**(a) Review meeting**: Legal/Compliance Officer reviews each active hold with hold owner (attorney, investigator)

**(b) Assessment criteria**:
- Is litigation/investigation still active? (case status, settlement discussions, investigative progress)
- Is data still relevant? (discovery scope changes, investigative focus narrowed)
- Can scope be narrowed? (reduce data categories, custodians, or time period)
- What is anticipated release date? (trial date, investigation timeline, audit completion)

Replace current Section 2.6 "Review documentation" paragraph with:

**(c) Review documentation**: Quarterly review SHALL produce **signed legal hold review record** including:

| Required Field | Description |
|----------------|-------------|
| **Hold identifier and review date** | Unique hold ID (from legal hold register) and date review conducted |
| **Reviewer** | Legal/Compliance Officer name and signature |
| **Current case/investigation status** | Active litigation status, settlement discussions, investigative progress, regulatory examination phase |
| **Continued necessity determination** | Explicit statement: "Hold remains necessary" or "Hold can be released" with legal rationale |
| **Scope adjustment** (if applicable) | Narrowing of data categories, custodians, or time period based on case developments |
| **Anticipated hold release date or trigger** | Target date for hold release OR trigger condition (e.g., "Upon trial verdict", "Upon settlement execution") |
| **Data subject request conflicts** (if applicable) | Any GDPR/nDSG erasure requests pending for held data (coordinate with DPO per Section 2.5) |
| **Next review date** | Scheduled next quarterly review (maximum 90 days from current review) |

**Review Record Storage**: Legal hold review records SHALL be attached to the corresponding hold entry in the legal hold register (maintained per Section 2.6 "Hold register" requirements in ISMS-IMP-A.8.10.4).

**Signature Requirement**: Legal/Compliance Officer SHALL sign each quarterly review record to confirm assessment was performed and documented. Electronic signatures are acceptable if audit trail is maintained.

**Hold Release and Deletion**:

Upon legal hold release:

**(a) Release authorisation**: Legal/Compliance Officer authorises release in writing with:
- Hold identifier
- Release reason (case settled, investigation closed, audit completed)
- Release date
- Confirmation no further legal obligation exists

**(b) Deletion execution**: IT Operations executes deletion within **90 days** of hold release unless:
- Approved business justification for extended retention (requires CISO + Data Owner approval)
- Another legal hold applies to same data (document in legal hold register)
- New retention obligation arises (update retention schedule, document basis)

**(c) Deletion verification**: Verify deletion per Section 2.4 requirements (deletion logs, certificates, audit trail)

**Data Subject Request Conflicts**:

When data subject erasure request conflicts with legal hold (Section 2.5):

**(a) DPO notification**: IT Operations immediately notifies DPO of conflict

**(b) Restriction of processing**: DPO implements restriction per GDPR Article 18:
- Data marked as "restricted - legal hold"
- Access limited to Legal/Compliance (no business processing)
- Data subject notified of restriction with legal hold explanation
- Restriction logged in data subject request register

**(c) Post-hold deletion**: Upon legal hold release, DPO ensures immediate deletion execution (within 30 days) to fulfill data subject request

**(d) Quarterly review**: DPO and Legal/Compliance Officer jointly review erasure request + legal hold conflicts quarterly

**Legal Hold Exceptions**:

Legal holds SHALL NOT be used to:

- Circumvent data subject erasure rights without legitimate legal basis (GDPR violations)
- Avoid normal deletion obligations without legal counsel approval
- Retain data for speculative "potential future litigation" without reasonable anticipation
- Extend retention indefinitely without periodic review and release

Abuse of legal hold process may result in disciplinary action and regulatory sanctions.

**Implementation Note**: Legal hold procedures, notification templates, register specifications, quarterly review checklists, and release workflows are documented in **ISMS-IMP-A.8.10.4 (Verification & Evidence Assessment)**.

---

## Logging and Monitoring

[Organisation] implements logging of deletion activities to support security monitoring and compliance verification.

**Deletion Logging Requirements**:

The following deletion-related events SHALL be logged where technically feasible:

**(a) Deletion process execution**: 
- Process start time and initiating user/system
- Data category and classification level
- Deletion method (Clear, Purge, Destroy, cryptographic erasure)
- Scope (systems, media, record count)
- Deletion trigger (retention expiry, data subject request, contract termination)
- Process completion time and status (success/failure)
- Error details if failure occurred

**(b) Deletion configuration changes**:
- Changes to retention schedules (retention period modifications)
- Changes to deletion rules (automated deletion thresholds, triggers)
- Changes to deletion methods (tool configurations, sanitization procedures)
- User making change, change date, approval reference

**(c) Deletion exceptions and bypasses**:
- Exception requests submitted and approval status
- Legal holds initiated and released
- Deletion process suspension (manual override, emergency stop)
- Data subject erasure request denials with legal basis

**(d) Manual deletion activities**:
- User-initiated deletions outside automated processes
- Physical media destruction requests
- Third-party deletion requests sent
- Verification activities (sampling, testing)

**Log Retention**:

Deletion logs SHALL be retained:

- **Deletion process logs**: Minimum **90 days** (operational troubleshooting)
- **Deletion configuration changes**: Minimum **12 months** (audit trail, change history)
- **Exception and bypass events**: Minimum **12 months** (compliance verification, abuse detection)
- **Data subject erasure request logs**: Minimum **3 years** (GDPR accountability, regulatory examination)
- **Legal hold register**: Minimum **3 years from hold release** (litigation record, regulatory compliance)

Extended retention applies where regulatory requirements mandate longer periods per ISMS-POL-00 (e.g., SOX 7-year retention if applicable).

**Monitoring and Alerting**:

[Organisation] monitors for:

**(a) Deletion process failures**: 
- Automated deletion jobs failing (database errors, permission issues, network failures)
- Backup deletion verification failures (data present in backups beyond retention)
- Third-party deletion non-response (no certificate received within SLA)
- Alert: IT Operations within 1 hour, escalate to System Owner if not resolved within 4 hours

**(b) Repeated deletion bypass attempts**:
- Multiple failed attempts to bypass deletion controls (unauthorised access to deletion tools)
- Legal hold abuse (holds without Legal/Compliance authorisation)
- Exception requests denied but resubmitted without addressing concerns
- Alert: Security Team immediately, investigate potential policy violation

**(c) Configuration changes to deletion rules**:
- Unauthorised changes to retention schedules (extending retention without approval)
- Deletion method downgrades (Purge → Clear for sensitive data without justification)
- Automated deletion process suspension without documented reason
- Alert: Security Team within 1 hour, require approval verification

**(d) Data subject request approaching deadline**:
- Erasure requests within 7 days of 30-day GDPR deadline without completion
- Alert: DPO immediately, escalate to CISO if deadline cannot be met

**Privacy Compliance**:

Deletion logging SHALL comply with applicable privacy regulations per ISMS-POL-00:

**(a) Data minimisation**: Logs contain only information necessary for security/compliance purposes (avoid excessive personal data logging)

**(b) User notification**: Personnel are informed of deletion activity monitoring through acceptable use policy

**(c) Access control**: Deletion logs restricted to authorised personnel with legitimate need:
- IT Operations (operational troubleshooting)
- Security Team (monitoring, incident response)
- DPO (privacy compliance verification)
- Compliance Team (regulatory audit support)
- Internal Audit (control effectiveness verification)

**(d) Log retention limits**: Logs are deleted per retention periods above (not retained indefinitely)

**Implementation Note**: Logging configuration standards, monitoring procedures, alert definitions, and log retention specifications are documented in **ISMS-IMP-A.8.10.4 (Verification & Evidence Assessment)**.

---

# Roles, Governance & Exception Management

## Roles and Responsibilities

**Executive Management / Board**:

- **Accountable for**: Approving information deletion policy and strategy; ensuring adequate resources and budget for deletion control implementation
- **Accepting residual risks**: Where deletion is not technically or operationally feasible, formally accepting residual risks through documented risk acceptance process
- **Supporting data protection**: Ensuring organisational culture supports data minimisation and privacy-by-design principles
- **Strategic oversight**: Reviewing deletion program effectiveness through quarterly compliance reports

**Chief Information Security Officer (CISO)**:

- **Accountable for**: Overall information deletion policy and program effectiveness; control implementation across all organisational systems
- **Policy ownership**: Approving policy updates, deletion method standards, and implementation procedures
- **Exception approval**: Approving high-risk exceptions per authority matrix (Section 3.3)
- **Risk management**: Defining organisational risk appetite for data exposure; accepting residual risks for deletion control limitations
- **Escalation handling**: Resolving deletion control failures, third-party non-compliance, and data subject request escalations
- **Annual policy review**: Leading annual policy review with DPO, Legal/Compliance, and CIO
- **Budget approval**: Ensuring adequate budget for deletion tools, third-party services, and automation development

**Data Protection Officer (DPO)**:

- **Accountable for**: GDPR/nDSG compliance for deletion controls; data subject rights management
- **Data subject requests**: Processing erasure requests per Section 2.5; assessing legal exceptions; notifying third parties
- **Privacy compliance**: Ensuring pseudonymization, anonymization, and deletion techniques meet regulatory standards
- **Legal exception review**: Evaluating GDPR Article 17(3) exceptions when erasure is denied
- **Privacy impact**: Assessing privacy implications of deletion exceptions and legal holds
- **Regulatory liaison**: Coordinating with Swiss FDPIC or EU DPAs on deletion-related inquiries
- **Training**: Ensuring personnel understand data subject rights and deletion obligations

**Legal/Compliance Officer**:

- **Accountable for**: Legal hold management (Section 2.6); retention period legal requirements
- **Legal hold authority**: ONLY role authorised to initiate or release legal holds
- **Regulatory interpretation**: Interpreting legal retention requirements (SOX, tax law, sector regulations)
- **Contract review**: Ensuring third-party contracts include deletion obligations (Section 2.3)
- **Litigation coordination**: Managing data preservation for litigation, investigation, or regulatory examination
- **Exception review**: Reviewing exceptions with legal compliance implications

**Chief Information Officer (CIO) / IT Director**:

- **Accountable for**: Technology infrastructure supporting deletion controls; resource allocation for IT Operations
- **Tool selection**: Approving deletion tools, backup solutions, and automation platforms
- **System integration**: Ensuring deletion controls integrate with IT asset management, backup systems, and cloud platforms
- **Capacity planning**: Ensuring adequate IT resources (storage, compute, personnel) for deletion operations
- **Technology roadmap**: Planning technology investments supporting deletion automation

**IT Operations**:

- **Responsible for**: Executing deletion processes; maintaining deletion tools; logging deletion activities
- **Daily operations**: Running automated deletion jobs; processing manual deletion requests; monitoring deletion process health
- **Tool maintenance**: Configuring deletion tools, backup systems, and automation scripts; applying patches and updates
- **Verification**: Conducting deletion verification sampling; collecting third-party certificates; maintaining evidence registers
- **Incident response**: Responding to deletion failures; escalating issues per Section 2.7 monitoring requirements
- **Gap tracking**: Logging deletion control gaps in gap register; coordinating remediation with System Owners

**System Owners**:

- **Responsible for**: Deletion implementation within their systems; coordinating with IT Operations and Data Owners
- **System-specific procedures**: Documenting deletion procedures for their systems in IMP supplements
- **Feasibility assessment**: Conducting automated deletion feasibility assessments per Section 2.1
- **Testing coordination**: Coordinating deletion testing during system changes or upgrades
- **Evidence collection**: Providing deletion logs, verification results, and exception justifications for their systems
- **Data Owner liaison**: Coordinating with Data Owners on retention periods and deletion approvals

**Data Owners**:

- **Responsible for**: Classifying data; determining retention periods; approving deletion for their data domains
- **Data classification**: Classifying data per [Organisation]'s classification scheme (Restricted, Confidential, Internal, Public)
- **Retention period definition**: Defining retention periods based on legal, regulatory, contractual, and business needs
- **Deletion approval**: Approving deletion execution for high-value or business-critical data
- **Exception review**: Approving or rejecting exception requests for their data domains (Section 3.3)
- **Validation**: Validating deletion effectiveness and data utility (ensuring deletion doesn't impair legitimate business operations)
- **Annual review**: Reviewing data classification and retention decisions annually

**Database Administrators (DBAs)**:

- **Responsible for**: Database record deletion; backup purging; database deletion verification
- **Record deletion**: Executing SQL delete operations; managing referential integrity during deletion
- **Backup coordination**: Coordinating with backup administrators to purge deleted data from backups
- **Performance optimization**: Ensuring deletion operations don't impact database performance
- **Verification queries**: Running database queries to verify absence of deleted data

**Cloud/Vendor Management**:

- **Responsible for**: Third-party deletion verification; contract compliance monitoring; cloud provider relationship management
- **Vendor assessment**: Conducting cloud provider deletion assessments per Section 2.3
- **Contract negotiation**: Ensuring deletion clauses in third-party contracts and DPAs
- **Certificate collection**: Obtaining deletion certificates from third parties; validating sufficiency
- **Escalation**: Escalating third-party non-compliance per Section 2.3 escalation timeline
- **Registry maintenance**: Maintaining cloud service provider registry (ISMS-REF-A.5.23) with deletion capabilities

**Records Manager**:

- **Responsible for**: Organisational retention schedule maintenance; retention period documentation
- **Retention schedule**: Maintaining comprehensive retention schedule for all data categories
- **Legal research**: Researching legal retention requirements; coordinating with Legal/Compliance
- **Schedule updates**: Updating retention schedule when regulations change or new data categories are introduced
- **Training**: Training Data Owners and System Owners on retention schedule use
- **Data inventory coordination**: Coordinating with Data Governance on data category inventory (Section 2.1)

**Security Team**:

- **Responsible for**: Deletion control monitoring; security incident response; assessment coordination
- **Monitoring**: Monitoring deletion logs per Section 2.7; investigating alerts and anomalies
- **Incident response**: Responding to unmasked sensitive data exposure, deletion failures, or unauthorised access incidents
- **Assessment coordination**: Coordinating ISMS-IMP-A.8.10 assessments (Sections 2.1-2.4)
- **Tool evaluation**: Evaluating deletion tools and automation platforms; recommending improvements
- **Documentation**: Maintaining deletion control documentation; updating procedures based on lessons learned

**Compliance & Audit Teams**:

- **Responsible for**: Verifying deletion compliance; conducting periodic control audits; reporting compliance gaps
- **Internal audit**: Conducting periodic deletion control audits per internal audit plan
- **Regulatory compliance**: Verifying compliance with GDPR, nDSG, PCI DSS, HIPAA (as applicable per ISMS-POL-00)
- **Evidence validation**: Validating deletion logs, certificates, and verification records for sufficiency
- **Gap reporting**: Reporting compliance gaps to CISO; tracking remediation in gap register
- **External audit support**: Supporting external auditors and regulatory examiners with evidence packages

**All Personnel (Users)**:

- **Responsible for**: Complying with deletion policies; reporting unmasked sensitive data; using exception process appropriately
- **Policy compliance**: Following acceptable use policy; not circumventing deletion controls
- **Reporting**: Reporting suspected unmasked sensitive data in non-production environments; reporting deletion failures
- **Exception requests**: Using exception process for legitimate business needs (Section 3.3); not bypassing controls
- **Training**: Completing annual security awareness training including deletion policy overview
- **Prohibited actions**: NOT attempting to bypass deletion controls, recover deleted data without authorisation, or re-identify anonymized data

**RACI Matrix Summary**:

| Activity | Executive Mgmt | CISO | DPO | Legal/Compliance | CIO | IT Ops | System Owners | Data Owners | Users |
|----------|----------------|------|-----|------------------|-----|--------|---------------|-------------|-------|
| Policy approval | A | R | C | C | C | I | I | I | I |
| Retention period definition | I | C | C | C | I | I | C | R/A | I |
| Deletion execution | I | A | I | I | C | R | C | I | I |
| Data subject requests | I | C | R/A | C | I | C | I | I | I |
| Legal holds | I | C | C | R/A | I | C | I | I | I |
| Exception approval | A | R/A | C | C | I | I | C | R | I |
| Third-party verification | I | A | I | C | I | R | C | I | I |
| Monitoring & alerts | I | A | I | I | C | R | C | I | I |

**Legend**: R = Responsible (executes), A = Accountable (owns outcome), C = Consulted (input sought), I = Informed (kept updated)

**Detailed RACI Note**: Complete RACI matrix with task-level assignments is documented in **ISMS-IMP-A.8.10** Implementation Guides.

---

## Assessment and Verification

[Organisation] verifies deletion control effectiveness through structured assessment program.

**Assessment Domains**:

| Domain | Assessment Focus | IMP Document |
|--------|------------------|--------------|
| **1. Data Inventory & Retention** | Data categories, retention schedules, deletion triggers, completeness verification | ISMS-IMP-A.8.10.1 |
| **2. Deletion Methods** | Media types, deletion tools, backup coordination, method appropriateness | ISMS-IMP-A.8.10.2 |
| **3. Third-Party & Cloud** | Provider inventory, deletion capabilities, contracts, certificates | ISMS-IMP-A.8.10.3 |
| **4. Verification & Evidence** | Deletion logs, certificates, data subject requests, legal holds | ISMS-IMP-A.8.10.4 |

**Assessment Frequency**:

- **Comprehensive assessment**: **Annually** (aligned with internal audit program, typically Q4)
  - All domains (1-5) assessed
  - All systems and data categories in scope
  - Executive review and remediation planning

- **Periodic verification**: **Quarterly** (high-risk systems, recent changes)
  - Targeted assessment of specific domains or systems
  - High-risk data categories (Restricted/Confidential)
  - Systems with recent deletion failures or third-party issues
  - Gap remediation progress verification

- **Triggered assessment**: **Within 30 days** of:
  - Significant security incidents involving data exposure
  - Major system changes affecting sensitive data (migrations, upgrades, new systems)
  - New data processing activities or data categories
  - Deployment of new deletion solutions or automation
  - Audit findings requiring remediation verification
  - Regulatory requirement changes (GDPR guidance, PCI DSS updates, nDSG amendments)

**Assessment Methodology**:

Assessments are conducted using **ISMS-IMP-A.8.10** suite:

**(a) Excel-based assessment workbooks**: Structured data collection with automated compliance calculations

**(b) Evidence registers**: Deletion logs, certificates, data subject request records, legal hold register

**(c) Gap analysis**: Identifying unprotected data, incomplete deletion coverage, third-party non-compliance

**(d) Remediation tracking**: Gap register with responsible parties, target dates, and closure verification

**(e) Dashboard consolidation**: Executive summary with traffic light indicators (🟢 compliant, 🟡 at risk, 🔴 non-compliant)

**Evidence Collection Workflow**:

1. **Quarterly (Month 1 of new quarter)**: IT Operations collects deletion execution logs, backup verification records, third-party certificates generated in **previous quarter** (evidence collection occurs at start of quarter for review of prior quarter activities)
2. **Quarterly (Month 1 of new quarter)**: DPO provides data subject request log summary for **previous quarter** (request counts, average response time, requests approaching deadline)
3. **Quarterly (Month 1 of new quarter)**: Legal/Compliance provides legal hold register updates and quarterly review records for **previous quarter**
4. **Quarterly**: CISO reviews assessment results, approves remediation plans, escalates critical gaps
6. **Annually**: Comprehensive assessment (all 5 domains) with executive review and budget allocation

**Evidence Validation**: Security Team SHALL validate evidence completeness before aggregation (check for missing logs, expired certificates, incomplete review records). Validation failures are flagged in gap register.

**Assessment Ownership**:

- **Security Team**: Conducts assessments with input from IT Operations, System Owners, and Data Owners
- **Data Owners**: Validate assessment accuracy for their data domains; approve retention periods and exceptions
- **CISO**: Reviews assessment results; approves remediation plans and exception requests
- **Compliance Team**: Verifies regulatory compliance claims; validates evidence sufficiency
- **Executive Management**: Reviews assessment results; approves budget for remediation

**Assessment Outputs**:

| Output | Purpose | Frequency | Owner |
|--------|---------|-----------|-------|
| **Domain assessment workbooks** (IMP-A.8.10.1 to .4) | Detailed data collection and gap identification | Annual (comprehensive), Quarterly (targeted) | Security Team |
| **Gap register entries** | Track remediation of identified gaps | Ongoing (updated quarterly) | IT Operations |
| **Remediation plans** | Detailed action plans with timelines and resources | Upon assessment completion | System Owners |
| **Executive report** | High-level summary for Executive Management and Board | Quarterly | CISO |

**Assessment Reporting**:

Quarterly compliance reports include:

**(a) Compliance metrics**:
- Percentage of data categories with documented retention periods
- Percentage of systems with implemented deletion controls
- Number of deletion certificates collected vs. required
- Data subject request processing time (average days to completion)
- Third-party deletion verification rate (certificates obtained / requests sent)

**(b) Gap analysis**:
- Unprotected sensitive data (data categories without deletion controls)
- Systems with incomplete backup deletion
- Third parties without deletion verification
- Data subject requests approaching or exceeding 30-day deadline

**(c) Remediation tracking**:
- Open gaps by severity (critical, high, medium, low)
- Gaps remediated since last report (with closure verification)
- Gaps overdue (past target date)
- Resource requirements (budget, personnel, tools)

**(d) Risk assessment**:
- Residual risks from deletion control gaps
- Likelihood and impact of data exposure
- Regulatory compliance risks (GDPR breach notification likelihood)

**Implementation Note**: Assessment methodology, workbook generation procedures, evidence requirements, gap analysis frameworks, and Summary Dashboard specifications are defined in **ISMS-IMP-A.8.10** suite.

---

## Exception Management

**Prohibited Exceptions**:

The following exception requests are **NOT PERMITTED**:

- **Indefinite retention without specific end date**: All exceptions must have defined duration or compliance milestone
- **Exceptions to avoid legitimate data subject erasure requests**: GDPR/nDSG rights cannot be circumvented through exceptions
- **Exceptions to circumvent regulatory retention requirements**: Exceptions to shorten legally mandated retention (e.g., SOX 7-year) are prohibited
- **Blanket exceptions for entire data categories without specific justification**: Each exception must address specific system/dataset with individualized risk assessment
- **Exceptions without compensating controls**: Risk reduction measures are mandatory for all approved exceptions
- **Exceptions to bypass legal hold requirements**: Legal holds cannot be overridden through exception process (managed by Legal/Compliance only per Section 2.6)
- **Repeated exceptions for same issue without remediation progress**: Exception renewals require demonstration of compliance efforts; repeated renewals without progress are denied

**Exception Documentation**:

All approved exceptions SHALL be documented including:

**(a) Exception identifier**: Unique ID (format: EXC-A810-YYYY-NNN)

**(b) Request metadata**:
- Request date and requesting party (name, role, department)
- Data Owner approval signature and date
- Systems/data categories affected
- Environments in scope (production, test, development, etc.)

**(c) Business justification**:
- Detailed explanation why standard deletion requirement cannot be met
- Business impact if exception denied (operational disruption, compliance conflict, project delay)
- Duration of need with specific start and end dates

**(d) Risk assessment**:
- **Inherent risk**: Likelihood and impact of data exposure without deletion
- **Threat scenarios**: Specific risks (unauthorised access, data breach, regulatory violation)
- **Compliance impact**: Regulatory implications (GDPR breach risk, PCI DSS non-compliance)
- **Compensating controls**: Alternative protections implemented
- **Residual risk**: Risk remaining after compensating controls
- **Risk acceptance**: Data Owner and CISO acceptance of residual risk

**(e) Approval chain**:
- Data Owner approval with signature and date
- Security Team review with risk assessment (Acceptable / Not Acceptable)
- CISO approval (required for Confidential/Restricted data)
- Executive Management approval (required for production exceptions)
- Legal/Compliance review (if regulatory implications)
- DPO approval (if personal data affected)

**(f) Monitoring and review**:
- Review schedule (monthly for Critical, quarterly for High, semi-annual for Medium sensitivity)
- Monitoring requirements (how compliance with exception conditions is verified)
- Revocation triggers (conditions requiring exception termination)

**(g) Path to compliance**:
- Remediation plan describing how full deletion compliance will be achieved
- Milestones with target dates
- Resource requirements (budget, tools, personnel)
- Approval for compliance plan

**Exception Monitoring**:

Active exceptions are:

**(a) Reviewed per schedule**: Monthly (Critical sensitivity), Quarterly (High), Semi-annual (Medium)

**(b) Monitored for compliance**: Verify compensating controls remain effective; review access logs, monitoring alerts, audit logs

**(c) Tracked in exception register**: Centralized register maintained by Security Team with status updates

**(d) Revoked if conditions change**:
- Business justification no longer valid (operational need ceases)
- Compensating controls fail (access control breach, monitoring gap)
- Risk profile increases (new threat, regulatory change)
- Deletion solution becomes available (tool implemented, system upgraded)
- Exception duration expires (automatic expiration, no implicit renewal)

**(e) Escalated if non-compliant**: Exception holders not complying with compensating controls are escalated to CISO; exception may be immediately revoked

**Exception Renewal**:

Exception renewals require:

**(a) Updated risk assessment**: Reassess inherent risk, compensating control effectiveness, residual risk

**(b) Business justification re-certification**: Confirm continued business need; demonstrate compliance efforts undertaken

**(c) Compliance progress demonstration**: Show progress toward full deletion compliance (milestones achieved, tools evaluated, budget approved)

**(d) Enhanced approval requirements**: Exceptions renewed more than twice require Executive Management approval regardless of data sensitivity

**(e) Shortened renewal duration**: Second renewal maximum 6 months (even if first exception was 12 months); third renewal maximum 3 months

**Exception Template**:

Standardized exception request template provided in **Annex C: Exception Request Template** (see end of policy document).

> **Complete Form**: Annex C provides the full exception request template with business justification framework (technical infeasibility, operational necessity, cost disproportionality), comprehensive risk assessment criteria (inherent risk scoring, threat scenario identification, compensating control selection), approval workflow matrix based on data sensitivity, and monitoring/review procedures. The template includes path-to-compliance milestone tracking and renewal requirements.

**Exception Register**:

Security Team maintains exception register including:

| Field | Description |
|-------|-------------|
| **Exception ID** | Unique identifier (EXC-A810-YYYY-NNN) |
| **Request Date** | Date exception request submitted |
| **Requested By** | Name, role, department |
| **Data Owner** | Data Owner who approved exception |
| **Systems Affected** | Systems, databases, applications, environments |
| **Data Categories** | Data types covered by exception |
| **Data Sensitivity** | Restricted, Confidential, Internal |
| **Business Justification** | Brief summary (detailed justification in exception request form) |
| **Risk Score** | Inherent risk, residual risk after compensating controls |
| **Compensating Controls** | Summary of alternative protections |
| **Approval Chain** | Approvers and dates (Data Owner, Security Team, CISO, Exec Mgmt) |
| **Exception Start Date** | Effective date |
| **Exception End Date** | Expiration date (no automatic renewal) |
| **Review Schedule** | Monthly, Quarterly, Semi-annual based on sensitivity |
| **Last Review Date** | Most recent review date |
| **Next Review Date** | Scheduled next review |
| **Status** | Active, Under Review, Expired, Revoked, Renewed |
| **Revocation Triggers** | Conditions requiring exception termination |
| **Path to Compliance** | Summary of remediation plan |
| **Milestones** | Target dates for compliance activities |
| **Notes** | Review outcomes, status updates, escalations |

Exception register is reviewed quarterly by CISO and annually by Executive Management.

**Implementation Note**: Exception request procedures, approval workflows, monitoring procedures, and exception register templates are documented in **ISMS-IMP-A.8.10.3 (Environment Coverage Assessment)** and **Annex B: Exception Request Template**.

**Exception Register Review**:
- **Quarterly**: CISO reviews all active exceptions, verifies compliance with monitoring requirements, approves continued exceptions
- **Annually**: Executive Management reviews exception register summary (count by severity, repeat exceptions, expired exceptions not closed)
- **Ad-hoc**: Exception register reviewed during internal audits, external audits, regulatory examinations

Exception register reviews SHALL be documented with review date, reviewer signature, and any actions taken (exceptions revoked, renewals denied, remediation accelerated).

---

## Incident Response

[Organisation] responds to data deletion security incidents per incident management framework.

**Data Deletion Security Incidents** include:

| Incident Type | Severity | Response Priority |
|---------------|----------|-------------------|
| **Unmasked sensitive data in non-production** | High | Immediate - Contain exposure, implement deletion, verify |
| **Deletion process failure exposing sensitive data** | Critical | Immediate - Stop exposure, investigate root cause, remediate |
| **Data retention beyond approved retention period** | Medium-High | Urgent - Assess scope, execute deletion, prevent recurrence |
| **Successful recovery of deleted data** | High | Immediate - Assess deletion method weakness, strengthen controls |
| **Deletion bypass or circumvention attempt** | High | Immediate - Investigate intent, prevent recurrence, disciplinary action |
| **Legal hold violation (data deleted while under hold)** | Critical | Immediate - Notify Legal/Compliance, assess legal exposure, preserve remaining evidence |
| **Third-party deletion certificate forgery** | High | Immediate - Investigate third party, verify actual deletion, terminate relationship |
| **Data subject erasure request deadline missed** | High | Immediate - Complete erasure, notify data subject, assess GDPR breach notification requirement |
| **Backup purge failure (deleted data in backups)** | Medium | Urgent - Verify backup rotation schedule, document maximum retention |
| **Data exfiltration from environment with insufficient deletion** | Critical | Immediate - Incident response, breach notification assessment, strengthen deletion controls |

**Incident Logging Requirements**:

All deletion security incidents SHALL be logged in **[Organisation]'s central incident register** (managed per ISMS-POL-A.5.24 Incident Management) with the following deletion-specific fields:

- **Incident Category**: "Data Deletion Control Failure" or "Data Retention Violation"
- **Data Sensitivity**: Restricted, Confidential, Internal, Public (affects response priority)
- **Deletion Control Affected**: Reference to specific policy section (e.g., "Section 2.2 backup deletion", "Section 2.5 GDPR erasure request")
- **Root Cause Classification**: Technical failure, process gap, human error, intentional bypass
- **Remediation Status**: Open, In Progress, Remediated, Verified, Closed
- **Gap Register Linkage**: If incident reveals systematic gap, link to gap register entry for tracking

**Cross-Reference to Gap Register**: When deletion incidents reveal systematic control gaps (not isolated failures), incidents SHALL be linked to gap register entries for remediation tracking. Example: Single backup deletion failure = incident only. Pattern of backup deletion failures across multiple systems = incident + gap register entry.

**Incident Register Location**: [Specify system - e.g., "ServiceNow Incident Management", "Jira Service Desk", "Excel-based incident log in ISMS repository"]

**Incident Response Process**:

**(a) Detection & Reporting**: 
- Incidents detected through monitoring (Section 2.7 alerts), user reports, testing, or external notification
- Report immediately to Security Team (email, incident hotline, SIEM alert)
- Log incident in incident register with unique ID

**(b) Classification**:
- Severity based on data sensitivity (Restricted > Confidential > Internal) and exposure scope (number of records, duration)
- Impact assessment: Harm to data subjects, regulatory non-compliance, reputational damage
- Priority assignment: Critical (immediate response), High (4-hour response), Medium (24-hour response)

**(c) Containment**:
- **Immediate actions** (within 1 hour for Critical/High):
  - Stop data flow (disable accounts, block network access, shut down exposed systems)
  - Isolate affected systems (network segmentation, firewall rules)
  - Prevent further exposure (suspend deletion processes if failure mode, implement emergency deletion if exposure)
- **Evidence preservation**: Capture logs, screenshots, forensic images before containment actions alter evidence
- **Notification**: Inform CISO, DPO (if personal data), Legal/Compliance (if legal hold or regulatory implications)

**(d) Investigation**:
- **Root cause analysis**: Why did deletion control fail? (technical failure, process gap, human error, intentional bypass)
- **Scope determination**: What data was affected? How many records? For how long? Who accessed?
- **Impact assessment**: What harm occurred? Unauthorised access? Data exfiltration? Regulatory violation?
- **Timeline reconstruction**: When did failure occur? When was it detected? What was the exposure window?

**(e) Remediation**:
- **Fix deletion implementation**: Correct technical failure, update procedures, implement missing control
- **Execute deletion**: Delete data that should have been deleted (if retention expiry or erasure request)
- **Validate effectiveness**: Test deletion control to ensure fix works (Section 2.4 verification procedures)
- **Prevent recurrence**: Strengthen controls (enhanced monitoring, automated verification, additional safeguards)

**(f) Notification**:
- **Internal escalation**: CISO, Executive Management (for Critical incidents)
- **Data subject notification**: If GDPR/nDSG breach notification required (assess per DPO guidance)
- **Regulatory notification**: Swiss FDPIC or EU DPA within 72 hours if high risk to data subjects (GDPR Art. 33)
- **Third-party notification**: If third-party data affected or third party caused incident

**(g) Post-Incident Review**:
- **Lessons learned**: What worked? What didn't? How can detection be improved?
- **Control improvements**: Update policies, procedures, technical controls based on incident learnings
- **Policy updates**: Revise POL-A.8.10 or IMP-A.8.10 if incident revealed policy gap
- **Training**: Address knowledge gaps revealed by incident (user error, misunderstanding)

**Critical Incident Handling**:

Unmasked sensitive data exposure in non-production or unauthorised environments is treated as **high-priority security incident**:

**(a) Immediate containment** (within 1 hour):
- Identify all locations where unmasked data exists (systems, backups, user devices)
- Stop data access (disable accounts, block network paths)
- Delete exposed data immediately (emergency deletion, bypass normal approval for containment)

**(b) Scope assessment** (within 4 hours):
- Determine extent of exposure (how much data, what sensitivity, how long exposed)
- Identify who accessed unmasked data (review access logs, authentication logs)
- Assess whether data was exfiltrated (network logs, file transfer logs, user activity)

**(c) Impact analysis** (within 24 hours):
- Assess harm to data subjects (risk of identity theft, financial fraud, privacy violation)
- Assess regulatory breach notification requirements (GDPR Art. 33-34, nDSG Art. 24)
- Assess reputational impact (customer trust, media exposure, competitive harm)

**(d) Remediation** (within 7 days):
- Implement masking/deletion in affected environment (Section 2.2 deletion methods)
- Validate no unmasked data remains (verification sampling, automated scanning)
- Strengthen controls to prevent recurrence (enhanced testing, mandatory pre-production masking verification)

**(e) Prevention** (within 30 days):
- Update procedures to detect unmasked data before production use
- Implement automated scanning for unmasked sensitive data patterns
- Training for personnel on non-production data handling

**Regulatory Breach Notification Assessment**:

Data exposure incidents SHALL be assessed for breach notification requirements:

**(a) GDPR (if EU personal data)**: 
- Notification to supervisory authority within **72 hours** if risk to rights and freedoms (Art. 33)
- Notification to data subjects **without undue delay** if high risk (Art. 34)
- Criteria: Sensitivity of data, volume of records, ease of identification, severity of consequences, special categories data (Art. 9)

**(b) Swiss nDSG**:
- Notification to Federal Data Protection and Information Commissioner (FDPIC) if **high risk** to personality or fundamental rights (Art. 24)
- Criteria: Type of personal data, volume, potential harm (identity theft, discrimination, reputational damage)

**(c) Sector-specific** (if applicable per ISMS-POL-00):
- **PCI DSS v4.0.1**: Payment card data breach notification to card brands and acquiring bank per PCI DSS Req. 12.10
- **HIPAA**: Breach notification to HHS and affected individuals if ePHI exposure (§164.404-408)

**Breach notification decision**: DPO and Legal/Compliance SHALL assess notification requirement within **24 hours** of incident confirmation. CISO approves notification decision.

**Detailed Incident Response Procedures**: Data deletion incident response procedures, classification criteria, escalation paths, and coordination with incident response team are documented in **ISMS-IMP-A.8.10.4 (Verification & Evidence Assessment)**.

---

## Policy Governance

**Policy Review Schedule**:

- **Frequency**: Annual minimum (typically Q4 aligned with internal audit program)
- **Comprehensive review**: Full policy review by CISO, DPO, Legal/Compliance, CIO

**Triggered Review** (within 30 days):

Policy review initiated upon:

**(a) Regulatory changes**:
- GDPR guidance updates (EDPB guidelines, national DPA interpretations)
- Swiss nDSG amendments or FDPIC guidance
- Sector-specific regulation changes (PCI DSS v4.0.1 → v4.1, DORA implementation acts, NIS2 transposition)

**(b) Major organisational changes**:
- Mergers or acquisitions (new data processing activities, new jurisdictions)
- New business lines (new data categories, new regulatory applicability)
- Significant infrastructure changes (cloud migration, new backup architecture, new third-party providers)

**(c) Significant incidents**:
- Data deletion incidents exposing policy gaps (unmasked data in non-production, deletion failure)
- External breach affecting deletion controls (ransomware affecting backups, data exfiltration)
- Regulatory examination findings requiring policy updates

**(d) Audit findings**:
- Internal audit findings identifying policy gaps or ambiguities
- External audit findings (ISO 27001 certification audit, regulatory audit)
- Customer audit findings (SOC 2, ISO 27001 customer audits)

**(e) Technology changes**:
- New deletion capabilities (cryptographic erasure, cloud-native deletion APIs)
- Backup architecture changes (snapshot-based backups replacing traditional backups)
- New third-party services requiring deletion assessment

**(f) Data classification changes**:
- Changes to [Organisation]'s classification scheme (new sensitivity levels, revised criteria)
- Reclassification of major data categories requiring deletion requirement updates

**Review Process**:

**(a) Review team**: CISO (chair), DPO, Legal/Compliance Officer, CIO, Security Team, Data Governance Team, Records Manager

**(b) Review scope**:
- Policy completeness (all deletion scenarios covered?)
- Regulatory alignment (POL-00 tiering current? All Tier 1 requirements addressed?)
- Procedure effectiveness (IMP procedures operational? Gaps identified?)
- Exception appropriateness (exception criteria still valid? Approval authorities correct?)
- Incident learnings (policy gaps revealed by incidents?)
- Technology currency (deletion methods current for infrastructure?)

**(c) Review output**:
- Updated policy document (if changes required)
- Implementation procedure updates (ISMS-IMP-A.8.10 updates)
- Exception criteria revisions (approval authorities, duration limits)
- Training materials updates (awareness content, role-specific training)

**(d) Approval**: Same approval chain as initial policy (CISO, DPO, Legal/Compliance, CIO, Executive Management)

**Policy Updates**:

**(a) Minor updates** (clarifications, reference updates, procedural details):
- **Approval**: CISO approval sufficient
- **Communication**: Email notification to affected stakeholders within 30 days
- **Training**: Not required unless roles/responsibilities change

**(b) Major updates** (scope changes, new mandatory requirements, technique prohibitions):
- **Approval**: Full approval chain (CISO, DPO, Legal/Compliance, CIO, Executive Management)
- **Communication**: Organisation-wide announcement, intranet publication, stakeholder briefings
- **Implementation timeline**: Per change management process (typically 60-90 days implementation window)
- **Training**: Required for personnel with affected roles

**(c) Emergency updates** (critical vulnerability, urgent regulatory mandate):
- **Approval**: CISO approval with Executive Management notification within 24 hours
- **Communication**: Immediate notification (email, emergency alert)
- **Implementation**: Immediate where feasible, with follow-up comprehensive implementation
- **Ratification**: Full approval chain ratifies emergency update within 30 days

**Policy Communication**:

Policy published in ISMS document repository (SharePoint, Confluence, document management system). Changes communicated organisation-wide:

**(a) Notification methods**:
- Email announcement to all employees and contractors
- Intranet news article highlighting key changes
- Team meetings for departments with significant role changes
- Training sessions for major policy updates

**(b) Change summary**:
- What changed (brief summary of updates)
- Why it changed (regulatory change, incident learning, process improvement)
- Who is affected (roles with new responsibilities)
- What actions are required (procedure updates, training completion)
- Effective date (when policy takes effect)

**(c) Stakeholder briefings**:
- Data Owners briefed on retention requirement changes
- System Owners briefed on implementation procedure updates
- IT Operations briefed on technical procedure changes
- Exception holders notified of exception criteria changes affecting active exceptions

**Policy Storage and Access Control**:

**Primary Repository**:
- Centralized ISMS policy repository (document management system, SharePoint, Confluence)
- Access-controlled (Internal classification - all employees can read)
- Version history maintained (all previous versions retained for audit trail)
- Change log documents all updates with rationale

**Archive**:
- Previous versions archived with read-only access
- Retention: Minimum **3 years** (or longer if regulatory examination requires)
- Timestamped and integrity-protected (digital signatures, audit logs)

**Access Control**:

| Role | Access Level |
|------|-------------|
| **All Employees** | Read (current version) |
| **Security Team** | Read/Write (draft updates, manage repository) |
| **CISO** | Read/Write (all versions including archived) |
| **DPO** | Read (all versions including archived, for compliance verification) |
| **Legal/Compliance** | Read (all versions including archived, for legal review) |
| **Internal Audit** | Read (all versions including archived, for audit trail) |
| **External Auditors** | Read (current version, upon request with approval) |
| **Regulators** | Read (current version, upon official request with Executive Management approval) |

**Training and Awareness**:

**(a) Security Awareness Training** (All Personnel - Annual):
- Information deletion overview and importance
- User responsibilities for handling organisational data
- Data retention and deletion basics (don't keep data longer than needed)
- Recognizing unmasked sensitive data in non-production and reporting procedures
- Prohibition on circumventing deletion controls or recovering deleted data without authorisation
- Data subject rights basics (GDPR/nDSG erasure requests)

**(b) Technical Training** (IT Operations, System Owners - Initial + Annual):
- Data deletion methods by media type (Section 2.2)
- Backup deletion coordination (Section 2.2 backup verification)
- Deletion tool configuration and maintenance
- Verification procedures and evidence collection (Section 2.4)
- Incident response for deletion failures (Section 3.4)
- Assessment procedures (ISMS-IMP-A.8.10 workbook completion)

**(c) Data Owner Training** (Data Owners - Initial + Regulatory Changes):
- Data classification and retention decision framework (Section 2.1)
- Exception request evaluation criteria (Section 3.3)
- Validation of deletion effectiveness for their data domains
- Regulatory retention requirements (Tier 1/2 per ISMS-POL-00)
- Balancing business needs with data minimisation

**(d) Privacy Training** (DPO Office - Initial + Regulatory Changes):
- Data subject erasure request handling (Section 2.5)
- GDPR Article 17 legal exception assessment
- Third-party notification procedures (GDPR Art. 19)
- Legal hold conflict management (Section 2.6)
- Breach notification assessment (Section 3.4)

**(e) Management Training** (Executive Management, CISO, CIO - Initial + Annual):
- Governance responsibilities and approval authorities
- Risk acceptance for deletion control limitations
- Exception approval criteria and oversight
- Regulatory compliance obligations (GDPR, nDSG, sector-specific)
- Quarterly compliance report review

**Training Completion Tracking**:
- Training completion tracked in learning management system (LMS) or HR system
- Annual training completion required for role-specific responsibilities
- Training records retained for **3 years** minimum (evidence of competence per ISO 27001 Clause 7.2)

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organisation]'s Information Security Management System per ISO/IEC 27001:2022:

**Risk Assessment Integration** (ISO 27001 Clause 6.1):

- Data deletion controls selected based on [Organisation]'s risk assessment methodology
- Data classification determines deletion method rigor (Restricted requires Purge/Destroy, Internal may use Clear)
- Risk treatment plans document data deletion control implementation for identified risks
- Residual risks (where deletion not feasible) documented in risk register and formally accepted by CISO + Executive Management

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Control A.8.10 applicability justified in [Organisation]'s Statement of Applicability (SoA)
- **SoA Entry**: Control A.8.10 - Information Deletion is documented as "Implemented" in [Organisation]'s SoA with implementation evidence references: ISMS-IMP-A.8.10.1 through A.8.10.4 (assessment workbooks)
- Implementation status tracked: "Implemented" with evidence references
- Control effectiveness measured through quarterly compliance reports (Section 3.2 assessment)
- SoA updated when policy changes affect applicability or implementation approach

**Related Controls Integration**:

| Control | Relationship to Information Deletion |
|---------|-------------------------------------|
| **A.5.9 (Inventory of Information and Other Associated Assets)** | Foundation - asset inventory identifies systems requiring deletion controls; data inventory (Section 2.1) builds on asset register |
| **A.5.10 (Acceptable Use of Information)** | Complementary - acceptable use policy includes user responsibilities for not retaining data beyond authorised periods |
| **A.5.12 (Classification of Information)** | Foundation - data classification drives deletion method selection (Restricted → Purge/Destroy); retention periods vary by classification |
| **A.5.13 (Labelling of Information)** | Integration - labeling ensures data requiring deletion is identifiable; retention metadata enables automated deletion triggers |
| **A.5.33 (Protection of Records)** | Balance - retention requirements must be balanced with deletion obligations; legal retention takes precedence over data minimisation |
| **A.5.34 (Privacy and Protection of PII)** | Integration - GDPR/nDSG erasure rights (Section 2.5) implement privacy requirements; deletion supports data minimisation principle |
| **A.7.10 (Storage Media)** | Integration - physical handling of storage media before deletion; secure storage until deletion execution |
| **A.7.14 (Secure Disposal or Re-use of Equipment)** | Integration - equipment disposal includes data sanitization per this policy; disposal procedures reference A.8.10 deletion methods |
| **A.8.13 (Information Backup)** | Critical integration - backup retention must align with deletion requirements; backup purging (Section 2.2) essential for deletion effectiveness |
| **A.8.24 (Use of Cryptography)** | Integration - cryptographic erasure (Section 2.2) as deletion method; key management integration for crypto erasure verification |

**Bidirectional Data Flows**:

**Information Deletion → Other Controls**:
- Deletion certificates → Audit & Compliance (evidence of A.7.14 equipment disposal)
- Retention schedules → Records Management (A.5.33 records protection lifecycle)
- Data subject erasure logs → Privacy Management (A.5.34 GDPR/nDSG compliance evidence)
- Legal hold register → Legal/Compliance (litigation management, regulatory examination coordination)

**Other Controls → Information Deletion**:
- Data Classification (A.5.12) → Retention periods and deletion method selection
- Asset Inventory (A.5.9) → Systems and media requiring deletion coverage
- Privacy Management (A.5.34) → Data subject erasure requests
- Legal Hold Process → Deletion suspension during litigation/investigation
- Contract Management → Third-party deletion obligations, contractual retention requirements

---

## Implementation Resources

**Implementation Guidance Suite** (ISMS-IMP-A.8.10):

- **ISMS-IMP-A.8.10.1 - Retention & Deletion Triggers Assessment**:
  - Data inventory methodology and completeness verification
  - Retention schedule templates and regulatory requirement mapping
  - Deletion trigger workflows (retention expiry, data subject requests, contract termination)
  - Legal hold procedures and register specifications
  - Automated deletion feasibility assessment criteria
  - Evidence: Retention schedule, data inventory with completeness verification, legal hold register

- **ISMS-IMP-A.8.10.2 - Deletion Methods Assessment**:
  - Media-specific deletion procedures (HDD, SSD, tape, cloud, paper)
  - Deletion method selection decision trees
  - Backup deletion coordination and verification procedures
  - Cryptographic erasure implementation and key destruction
  - Tool capability assessment (vendor-agnostic)
  - Evidence: Deletion method documentation, backup deletion verification records, tool configurations

- **ISMS-IMP-A.8.10.3 - Third-Party & Cloud Deletion Assessment**:
  - Cloud provider deletion capability assessment criteria
  - Third-party contract template with deletion clauses
  - Deletion certificate sufficiency validation
  - Third-party deletion failure escalation workflows
  - Provider inventory with deletion SLAs
  - Evidence: Third-party deletion certificates, cloud provider assessments (ISMS-REF-A.5.23), contract review records

- **ISMS-IMP-A.8.10.4 - Verification & Evidence Assessment**:
  - Deletion verification sampling procedures
  - Evidence register templates (deletion logs, certificates, attestations)
  - Data subject request log specifications and processing workflows
  - Legal hold register and quarterly review procedures
  - Incident response procedures for deletion failures
  - Logging and monitoring configuration standards
  - Evidence: Deletion execution logs, data subject request log, legal hold register, verification sampling results


**Assessment Tools**:

- Excel-based assessment workbooks with automated compliance calculations
- Python generation scripts for workbook creation (standardized structure, validation rules)
- Evidence registers and collection templates
- Gap analysis frameworks with severity classification
- Remediation tracking tools with milestone monitoring
- Dashboard consolidation scripts aggregating metrics across assessments

**Supporting Materials**:

- Exception request template (Annex B of this policy)
- Data subject erasure request template (referenced in Section 2.5, detailed in IMP-A.8.10.4)
- Third-party deletion certificate template (IMP-A.8.10.3)
- User communication templates (policy announcements, training materials)
- Quick reference guides for practitioners (deletion method selection, retention period lookup)

---

## Regulatory Mapping

This policy addresses information deletion requirements from:

| Requirement Category | Swiss nDSG | EU GDPR | ISO 27001:2022 | PCI DSS v4.0.1* | HIPAA* | FINMA* | DORA/NIS2* |
|---------------------|-----------|---------|----------------|---------|--------|--------|------------|
| **Data minimisation / storage limitation** | Art. 6 | Art. 5(1)(e) | A.8.10 | Req. 3.1 | §164.514 | Risk-Based | Art. 21 (NIS2) |
| **Retention schedules** | Art. 6 | Art. 5(1)(e) | A.8.10 | Req. 3.1 | HIPAA Gen Rules | FINMA Circ 2008/21 | Risk-Based |
| **Deletion methods / sanitization** | Art. 8, 25, 30 | Art. 32(1) | A.8.10 | Req. 3.2 | §164.310(d)(2)(i) | Risk-Based | Art. 9 (DORA) |
| **Backup deletion** | Art. 8 | Art. 32 | A.8.10 | Req. 3.2 | §164.310(d)(2)(i) | Risk-Based | Risk-Based |
| **Data subject right to erasure** | Art. 12 | Art. 17 | A.5.34 (ref) | N/A | Limited (§164.526 amendment) | N/A | N/A |
| **Third-party deletion obligations** | Art. 8 | Art. 28(3)(g) | A.8.10 | Req. 12.8.2 | §164.314(a)(2) | FINMA Circ 2018/3 | Art. 28 (DORA) |
| **Evidence of deletion** | Art. 8 | Art. 5(2) accountability | A.8.10 | Req. 12.3.4 | §164.316(b)(1)(ii) | Risk-Based | Risk-Based |
| **Breach notification (deletion failures)** | Art. 24 | Art. 33-34 | A.5.24 (ref) | Req. 12.10 | §164.404-408 | Incident Mgmt | Art. 23 (DORA) |

*Conditional applicability per ISMS-POL-00

**Detailed Regulatory Requirements**: Specific regulatory interpretation, compliance verification procedures, and evidence mapping are documented in the relevant ISMS-IMP-A.8.10 assessment workbooks.

---

## Document Relationship

```
Policy Layer (Governance - ISMS Governed)
    │
    └── ISMS-POL-A.8.10 (This Document)
        ├── Annex A: Approved Deletion Methods Matrix
        ├── Annex B: Data Subject Erasure Request Template
        └── Annex C: Exception Request Template

Implementation Layer (Assessment & Evidence - ISMS Governed)
    │
    └── ISMS-IMP-A.8.10 Suite
        ├── ISMS-IMP-A.8.10.1: Retention & Deletion Triggers
        ├── ISMS-IMP-A.8.10.2: Deletion Methods
        ├── ISMS-IMP-A.8.10.3: Third-Party & Cloud Deletion
        ├── ISMS-IMP-A.8.10.4: Verification & Evidence

Supporting References (ISMS Governed)
    │
    └── ISMS-REF-A.5.23: Cloud Service Provider Registry
        └── Deletion capability assessments per provider
```

---

# Definitions

**Anonymization**: Irreversible process of removing all identifying information from data such that re-identification is not reasonably achievable even with additional data or effort. Anonymized data is no longer personal data under GDPR/nDSG.

**Backup Purging**: Process of deleting data from backup systems (full/incremental backups, snapshots, disaster recovery replicas) to ensure deleted data doesn't persist in backup copies.

**Business Owner**: See Data Owner (terminology used interchangeably in some contexts).

**Certificate of Destruction**: Third-party attestation documenting physical destruction of storage media, including media identifiers, destruction method (referencing NIST SP 800-88 or equivalent), destruction date, and certificate issuer information.

**Clear (Deletion Method)**: Logical sanitization technique applying logical techniques to sanitize data using standard read and write commands, protecting against simple non-invasive data recovery techniques. Per NIST SP 800-88: overwriting, block erase.

**Compensating Control**: Alternative security control implemented when primary control (deletion) is not technically or operationally feasible, providing equivalent risk reduction through different means (enhanced access controls, encryption, monitoring).

**Cryptographic Erasure**: Data deletion method rendering encrypted data irrecoverable by destroying encryption keys used to protect the data, without physically modifying the encrypted data itself. Requires destruction of all key copies and verification that key recovery is impossible.

**Data Category**: Classification of data by type for retention and deletion purposes (e.g., PII, financial data, health information, credentials, business records, logs).

**Data Custodian**: IT operations personnel responsible for deploying and maintaining technical infrastructure including deletion tools. Custodians implement requirements defined by Data Owners and execute deletion processes.

**Data Inventory**: Comprehensive record of data categories processed by [Organisation], including data type, classification, storage location, business purpose, data owner, and retention requirements.

**Data Minimization**: Privacy principle requiring collection and retention of only data necessary for specified purposes, with deletion when no longer needed. Core principle in GDPR Article 5(1)(c) and Swiss nDSG Article 6.

**Data Owner**: Business or functional leader accountable for data within their domain, responsible for data classification, determining retention periods and deletion requirements, approving exceptions, and validating deletion effectiveness.

**Data Subject**: Individual whose personal data is being processed (GDPR/nDSG terminology). Data subjects have rights including right to erasure under GDPR Article 17 and Swiss nDSG Article 12.

**Deletion Trigger**: Event or condition initiating the deletion process (retention period expiry, data subject erasure request, contract termination, legal hold release, asset decommissioning, consent withdrawal).

**Destroy (Deletion Method)**: Physical destruction of storage media rendering media unusable and data recovery infeasible. Per NIST SP 800-88: disintegration, pulverization, melting, incineration, shredding.

**Exception**: Formally approved deviation from policy requirements, documented with business justification, risk assessment, compensating controls, approval signatures, and time limitation. All exceptions have defined expiration dates and review schedules.

**Format Preservation**: Maintaining original data format and structure in masked or substituted data to ensure application compatibility and data validation rules continue to function correctly (e.g., credit card format preservation in tokenization).

**Information Deletion**: Process of removing data from storage media such that it cannot be recovered through normal methods or specialized data recovery techniques, appropriate to the media type and data sensitivity.

**Inherent Risk**: Risk level before application of security controls or compensating measures. Used in risk assessments to evaluate baseline risk of data exposure without deletion controls.

**Legal Hold (Litigation Hold)**: Suspension of normal deletion processes to preserve data for litigation, investigation, regulatory examination, or audit. Legal holds override retention schedules and deletion triggers until hold is formally released by Legal/Compliance Officer.

**Media Sanitization**: All methods of rendering data on storage media inaccessible, including clearing, purging, and destroying. Sanitization level (Clear/Purge/Destroy) selected based on media type, data sensitivity, and media destination.

**Personal Data**: Any information relating to an identified or identifiable individual (GDPR/nDSG definition). Includes direct identifiers (name, ID number) and indirect identifiers (combination of attributes enabling identification).

**Pseudonymization**: Replacement of direct identifiers with pseudonyms (reversible substitutes) such that data cannot identify individuals without additional information (key or mapping table) held separately. Pseudonymized data remains personal data under GDPR but with reduced risk.

**Purge (Deletion Method)**: Physical or logical sanitization technique protecting against laboratory attack methods. Per NIST SP 800-88: cryptographic erase, degaussing (magnetic media), physical destruction.

**Redaction**: Complete removal or replacement of sensitive data with placeholder characters (e.g., `****`, `XXXX`, `[REDACTED]`) without providing substitute values. Used in reports, exports, screenshots, or document sanitization.

**Referential Integrity**: Maintaining valid relationships between related data across tables or datasets, ensuring foreign keys and joins continue to function correctly after deletion or masking operations.

**Re-identification**: Process of determining the original identity of a data subject from anonymized or pseudonymized data, either through reverse engineering, linking with external datasets, or inference from quasi-identifiers.

**Residual Risk**: Risk remaining after application of security controls, compensating measures, or risk treatment. Residual risk from deletion control limitations must be formally accepted by CISO and Executive Management.

**Retention Period**: Defined timeframe during which data must be kept before deletion is permitted or required. Retention periods are based on legal requirements, regulatory requirements, contractual obligations, or documented business needs.

**Retention Schedule**: Comprehensive document listing all data categories processed by [Organisation] with approved retention periods, legal/regulatory basis, business justification, data owner, and review dates.

**Right to Erasure (Right to be Forgotten)**: Data subject right under GDPR Article 17 and Swiss nDSG Article 12 to request deletion of their personal data. Subject to legal exceptions (legal obligation, legal claims, public interest, archiving).

**Sanitization**: See Media Sanitization.

**Secure Disposal**: Process of rendering storage media or equipment unusable and data irrecoverable before disposal, reuse, or transfer outside organisational control. Integrates with Control A.7.14 (Secure Disposal or Re-use of Equipment).

**Sensitive Data**: Any information that, if disclosed, could cause harm to individuals or [Organisation]. Includes PII, financial data, health information, authentication credentials, and proprietary business information. Typically classified as Confidential or Restricted.

**Storage Limitation**: GDPR Article 5(1)(e) principle requiring personal data to be kept in a form permitting identification of data subjects for no longer than necessary for processing purposes. Archived data must be subject to review and deletion.

**System Owner**: Individual responsible for specific information system, application, or infrastructure component. System Owners coordinate deletion implementation, conduct feasibility assessments, and document system-specific procedures.

**Third-Party Processor**: External entity processing organisational data on behalf of [Organisation], including cloud providers, managed service providers, SaaS vendors, and outsourced service providers. Subject to data processing agreements (DPAs) with deletion obligations.

**Tokenization**: Replacement of sensitive data with non-sensitive tokens (surrogate values) stored in a secure token vault, enabling reversibility when authorised. Original-to-token mapping maintained in separate secure system with strict access controls.

---

# Annex A: Approved Deletion Methods Matrix

**Purpose**: This annex provides technical reference for selecting appropriate deletion methods based on media type, data sensitivity, and media destination. All methods listed are approved for organisational use per Section 2.2 policy requirements.

**Usage**: System Owners and IT Operations use this matrix during deletion planning to select appropriate methods. Data Owners approve method selection for their data based on classification and regulatory requirements.

## A.1 Deletion Method Selection Matrix

| Media Type | Data Sensitivity | Media Destination | Recommended Method | Verification |
|------------|------------------|-------------------|-------------------|--------------|
| **Magnetic HDD** | Restricted/Confidential | External disposal | Degauss + Physical destruction | Certificate of destruction |
| **Magnetic HDD** | Restricted/Confidential | Internal reuse | ATA Secure Erase OR Overwrite (7+ passes) | Tool completion log + sampling |
| **Magnetic HDD** | Internal/Public | Internal reuse | Overwrite (3 passes) OR Quick format + overwrite | Tool completion log |
| **Solid-State (SSD)** | Restricted/Confidential | External disposal | Physical destruction (shredding, pulverizing) | Certificate of destruction |
| **Solid-State (SSD)** | Restricted/Confidential | Internal reuse | Cryptographic erasure (if encrypted) OR Secure Erase command | Key destruction log OR tool completion log |
| **Solid-State (SSD)** | Internal/Public | Internal reuse | Secure Erase command OR Factory reset | Tool completion log |
| **Optical Media (CD/DVD)** | Any sensitivity | Disposal | Physical destruction (shredding P-4 or higher) | Certificate of destruction OR witnessed destruction |
| **Magnetic Tape** | Restricted/Confidential | External disposal | Degauss + Physical destruction | Certificate of destruction |
| **Magnetic Tape** | Restricted/Confidential | Internal reuse | Degauss | Degausser log + field strength verification |
| **Magnetic Tape** | Internal/Public | Internal reuse | Overwrite (full tape) | Backup system log |
| **Paper Records** | Restricted/Confidential | Disposal | Cross-cut shredding (DIN 66399 P-4 minimum) | Certificate of destruction OR shredder log |
| **Paper Records** | Internal/Public | Disposal | Cross-cut shredding (DIN 66399 P-3) | Shredder log OR witnessed destruction |
| **Mobile Devices (Encrypted)** | Restricted/Confidential | External disposal | Cryptographic erasure + Factory reset + Physical destruction | Key destruction + certificate |
| **Mobile Devices (Encrypted)** | Restricted/Confidential | Internal reuse | Cryptographic erasure + Factory reset | Key destruction log + device verification |
| **Mobile Devices (Unencrypted)** | Restricted/Confidential | Any destination | Physical destruction (NOT factory reset alone) | Certificate of destruction |
| **Cloud Storage (IaaS/PaaS)** | Restricted/Confidential | N/A (logical deletion) | API deletion + Cryptographic erasure (if customer-managed keys) | API success response + key destruction log |
| **Cloud Storage (IaaS/PaaS)** | Internal/Public | N/A (logical deletion) | API deletion + Verification query | API success response + absence verification |
| **Cloud Storage (SaaS)** | Any sensitivity | N/A (provider-managed) | Provider deletion process per contract | Deletion certificate OR SOC 2 audit report |
| **Network-Attached Storage (NAS/SAN)** | Restricted/Confidential | Internal reuse | File deletion + Secure overwrite | Storage system log + verification sampling |
| **Database Records** | Restricted/Confidential | N/A (logical deletion) | SQL DELETE + Backup purging | Database log + backup verification query |
| **Database Records** | Internal/Public | N/A (logical deletion) | SQL DELETE | Database log |

## A.2 NIST SP 800-88 Method Mapping

| [Organisation] Method | NIST SP 800-88 Category | NIST Description | Applicability |
|-----------------------|-------------------------|------------------|---------------|
| **Overwrite (multiple passes)** | Clear | Overwriting with non-sensitive data (zeros, random, patterns) | Magnetic media (HDD, tape) - NOT SSD |
| **ATA Secure Erase** | Purge (if properly implemented) | Firmware-based secure erase command | HDD, some SSDs (verify completion) |
| **Block Erase** | Clear | Erase at block level (file system or hardware) | All electronic media |
| **Cryptographic Erase** | Purge | Destruction of encryption keys rendering data inaccessible | All encrypted media (keys must be irrecoverable) |
| **Degaussing** | Purge | Magnetic field erasure | Magnetic media only (HDD, tape) - NOT SSD/optical |
| **Physical Destruction (Disintegrate)** | Destroy | Media reduced to particles ≤2mm | All media types |
| **Physical Destruction (Pulverize)** | Destroy | Media ground to powder | All media types |
| **Physical Destruction (Shred)** | Destroy | Media cut to specified dimensions | Paper (DIN 66399), optical media, some electronic |
| **Physical Destruction (Incinerate)** | Destroy | Media burned to ash | All media types (environmental/regulatory considerations) |

## A.3 Method-Specific Requirements

### A.3.1 Overwriting (Magnetic Media)

**Applicable to**: Magnetic hard drives (HDD), magnetic tape
**NOT applicable to**: SSDs, flash drives, optical media

**Requirements**:
- Minimum **3 passes** for Internal/Public data
- Minimum **7 passes** for Confidential/Restricted data (or use DoD 5220.22-M standard if contractually required)
- Each pass must write different pattern (e.g., zeros, ones, random)
- Verify write completion (no bad sectors preventing overwrite)
- Full media overwrite (all addressable sectors including slack space)

**Tools**: DBAN (Darik's Boot and Nuke), `dd` with `/dev/urandom`, vendor tools (WD/Seagate secure erase utilities)

**Verification**: Tool completion log confirming passes completed without errors; spot-check sampling if required for high-sensitivity data.

### A.3.2 ATA Secure Erase / NVMe Secure Erase

**Applicable to**: SATA/SAS hard drives (HDD), NVMe SSDs supporting secure erase command
**NOT applicable to**: Removable media without hardware secure erase support

**Requirements**:
- Use manufacturer-provided tool or `hdparm` (Linux) / `nvme format` (NVMe)
- Verify drive supports secure erase (check ATA/NVMe specifications)
- For SSD: Verify command includes user data AND reserved blocks (not just user-addressable LBAs)
- Confirm completion (command returns success, no errors in SMART log)
- For high-sensitivity: Combine with cryptographic erasure if drive was encrypted

**Warning**: SSD secure erase reliability varies by manufacturer. For Restricted data, physical destruction is preferred over secure erase alone.

**Verification**: Command completion log; SMART log check; drive should report "Sanitize Complete" or equivalent.

### A.3.3 Cryptographic Erasure

**Applicable to**: Any encrypted media (HDD, SSD, cloud storage, mobile devices)
**Requires**: Full-disk encryption (FDE) or equivalent; encryption keys managed separately

**Requirements**:
- Encryption must have been enabled BEFORE data was written (post-encryption doesn't protect pre-existing data)
- Destroy ALL copies of encryption keys:
  - Key management system (HSM, software KMS)
  - Key escrow or backup copies
  - User copies (recovery keys, passphrases stored by users)
- Verify key destruction is irreversible (not just marked deleted, but cryptographically zeroized)
- Document key-to-data mapping (which keys protected which data categories)
- Retain key destruction certificate for audit (Section 2.4 evidence requirements)

**Integration**: Cryptographic erasure procedures must align with ISMS-POL-A.8.24 (Use of Cryptography) key management requirements.

**Verification**: Key management system audit log showing key destruction with timestamp and method; HSM certificate if applicable; verification that key recovery is impossible.

### A.3.4 Degaussing

**Applicable to**: Magnetic media only (HDD, magnetic tape)
**NOT applicable to**: SSD, flash drives, optical media (degaussing has NO effect)

**Requirements**:
- Use degausser rated for media coercivity (field strength > media rating)
- For modern high-density HDD (>1TB): Minimum **5,000 Oersted** degausser
- Degauss THEN physically destroy (degaussing may render drive unusable; physical destruction ensures no residual data)
- Verify field strength periodically (degausser calibration certificate current)
- Document each degaussing operation (media ID, date, degausser serial number)

**Verification**: Degausser log with field strength verification; attempted read operation should fail (media unreadable); certificate of destruction after physical destruction.

### A.3.5 Physical Destruction

**Applicable to**: All media types at end-of-life

**Requirements by Media Type**:

| Media Type | Destruction Requirement | Standard Reference |
|------------|------------------------|-------------------|
| **HDD (magnetic)** | Platters shredded, pulverized, or disintegrated to ≤2mm particles | NIST SP 800-88 (Destroy) |
| **SSD (solid-state)** | Chips physically destroyed (shredded, pulverized) to prevent chip-level recovery | NIST SP 800-88 (Destroy) |
| **Optical (CD/DVD/Blu-ray)** | Cross-cut shredding to ≤10mm² particles (DIN 66399 O-4 minimum for Confidential) | DIN 66399 |
| **Magnetic Tape** | Tape shredded to ≤6mm strips (DIN 66399 T-4 minimum for Confidential) | DIN 66399 |
| **Paper Records** | Cross-cut shredding to ≤160mm² particles (DIN 66399 P-4 minimum for Confidential) | DIN 66399 |
| **Mobile Devices** | Device crushed or shredded, destroying motherboard and storage chips | NIST SP 800-88 |

**Third-Party Destruction**:
- Use certified destruction vendors (NAID AAA certification or equivalent)
- Obtain certificate of destruction with:
  - Media serial numbers or asset IDs
  - Destruction method (reference to NIST SP 800-88 or DIN 66399 level)
  - Destruction date and location
  - Certificate issuer and accreditation
- Maintain chain of custody from [Organisation] to destruction vendor

**Verification**: Certificate of destruction from accredited vendor; for high-sensitivity, witness destruction or require video documentation.

## A.4 Backup Deletion Coordination

**Challenge**: Deleted data may persist in backup systems with independent retention policies.

**Deletion in Backup Architectures**:

| Backup Type | Deletion Method | Verification |
|-------------|----------------|--------------|
| **Full + Incremental** | Delete all backup sets containing target data within retention window | Backup catalog query confirming absence |
| **Full + Differential** | Delete full backup + all differential backups containing target data | Backup catalog query confirming absence |
| **Snapshot-based** | Delete all snapshots containing target data OR enforce retention policy guaranteeing deletion by date | Snapshot inventory showing deletion; retention policy enforcement log |
| **Cloud-native (AWS Backup, Azure Backup)** | API deletion of recovery points containing target objects; verify multi-region deletion | API response logs; verify all regions/accounts |
| **Application-level (DB dumps, VM exports)** | Exclude deleted data from future dumps; delete existing dumps containing target data | Dump manifest verification; dump inventory |
| **Tape backups** | Mark tapes for early retirement OR degauss/destroy tapes containing target data | Tape inventory with retirement dates; destruction certificates |

**Where Immediate Deletion is Infeasible**:
- Document maximum retention period (e.g., "Deleted data will be purged from backups within 90 days per monthly full backup rotation")
- Obtain Data Owner approval for retention period
- Document in exception register if retention exceeds standard policy limits
- Monitor backup rotation to verify deletion occurs per schedule

**Verification Procedures**: See ISMS-IMP-A.8.10.2 (Deletion Methods Assessment) for backup-specific verification procedures.

## A.5 Cloud and Third-Party Deletion

**Cloud Provider Deletion Methods** (by service model):

| Service Model | Deletion Method | Verification | Notes |
|---------------|----------------|--------------|-------|
| **IaaS (VMs, Block Storage)** | API deletion (DELETE /volumes/:id); verify snapshot deletion separately | HTTP 200/204 response; absence query | Verify deletion in ALL regions where data replicated |
| **PaaS (Databases, App Services)** | Provider-specific deletion API; verify backup retention policy | API response; backup policy configuration | Some PaaS providers retain deleted data for recovery window (7-35 days) |
| **SaaS (CRM, Email, Collaboration)** | Provider deletion process per DPA; rely on SOC 2 deletion controls | Deletion certificate OR SOC 2 Type II report Section CC6.7 | Limited customer control; verify DPA specifies deletion timeline |
| **Backup-as-a-Service (BaaS)** | API deletion of backup jobs and recovery points | API response; backup job inventory showing deletion | Verify deletion of incremental chains, not just latest backup |

**Third-Party Deletion Verification**:
- Obtain deletion certificate meeting sufficiency criteria (Section 2.3)
- For high-sensitivity: Require accredited destruction vendor certificate OR independent audit report
- For SaaS: Accept SOC 2 Type II report with deletion control testing (typically Section CC6.7 or equivalent)

**Escalation for Non-Compliance**: See Section 2.3 third-party deletion failure escalation timeline.

---

# Annex B: Data Subject Erasure Request Template

**Purpose**: Standardized form for processing GDPR Article 17 and Swiss nDSG Article 12 erasure requests.

**Usage**: DPO Office uses this template to document all data subject erasure requests, ensuring consistent processing and compliance with 30-day response timeline.

---

## Data Subject Erasure Request Form

**Request ID**: [AUTO-GENERATED: DSR-A810-YYYY-NNN]  
**Request Date**: [DD.MM.YYYY HH:MM] (timestamp of receipt)  
**Request Channel**: [ ] Email [ ] Web Form [ ] Postal Mail [ ] In-Person [ ] Phone  
**Processed By**: [DPO Office personnel name]  

---

### Data Subject Information

**Name**: [Full legal name]  
**Email**: [Email address for correspondence]  
**Phone**: [Optional contact number]  
**Address**: [Optional postal address]  
**Relationship to [Organisation]**: [ ] Current Customer [ ] Former Customer [ ] Employee [ ] Former Employee [ ] Website Visitor [ ] Other: _______  

**Account/Reference Number** (if applicable): [Customer ID, employee ID, account number]  

---

### Identity Verification

**Verification Method Used**:
- [ ] Account login (authenticated session)
- [ ] Government-issued ID (passport, national ID card, driver's license)
- [ ] Personal information confirmation (answered security questions, confirmed account details)
- [ ] In-person identification at [Organisation] office
- [ ] Other: [Specify method]

**Verification Date**: [DD.MM.YYYY]  
**Verification Status**: [ ] ✅ Verified [ ] ⚠️ Partial Verification [ ] ❌ Verification Failed  
**Verifier**: [DPO Office personnel name]  

**If Verification Failed**: [Explain why and what additional information was requested]

---

### Request Details

**Data Subject Statement** (verbatim or summary):  
"[Quote or summarise data subject's erasure request]"

**Scope of Request**:
- [ ] All personal data held by [Organisation]
- [ ] Specific data categories: [List]
- [ ] Specific systems/services: [List]
- [ ] Specific time period: [From DD.MM.YYYY to DD.MM.YYYY]

**Reason for Request** (if provided by data subject):
- [ ] Data no longer necessary for original purpose
- [ ] Withdrawing consent (where consent was legal basis)
- [ ] Objecting to processing
- [ ] Data unlawfully processed
- [ ] Legal obligation requires erasure
- [ ] Other: [Specify]
- [ ] No reason provided (not required under GDPR/nDSG)

---

### Legal Assessment

**DPO Assessment Date**: [DD.MM.YYYY]  
**Reviewed By**: [DPO name and signature]  

**GDPR Article 17(1) Grounds - Does Erasure Obligation Apply?**

[ ] ✅ YES - Erasure Required  
[ ] ❌ NO - Erasure Denied (Legal Exception Applies)  

**Assessment Rationale**:

[Detailed explanation - select applicable grounds]

**If ERASURE REQUIRED**, identify which GDPR Art. 17(1) ground(s) apply:
- [ ] Art. 17(1)(a): Personal data no longer necessary for purposes collected
- [ ] Art. 17(1)(b): Data subject withdraws consent (and no other legal basis exists)
- [ ] Art. 17(1)(c): Data subject objects to processing (Art. 21) and no overriding legitimate grounds
- [ ] Art. 17(1)(d): Personal data unlawfully processed
- [ ] Art. 17(1)(e): Erasure required for compliance with legal obligation (EU/Member State law)
- [ ] Art. 17(1)(f): Data collected for information society services offered to children (Art. 8)

**If ERASURE DENIED**, identify which GDPR Art. 17(3) exception applies:
- [ ] Art. 17(3)(a): Processing necessary for exercising freedom of expression and information
- [ ] Art. 17(3)(b): Processing necessary for compliance with legal obligation (EU/Member State law requiring retention)
  - **Legal Obligation**: [Cite specific law, e.g., "Swiss OR Art. 958f - 10-year accounting record retention"]
- [ ] Art. 17(3)(c): Processing necessary for public interest or exercise of official authority
- [ ] Art. 17(3)(d): Processing necessary for public health purposes in the public interest
- [ ] Art. 17(3)(e): Processing necessary for archiving purposes in public interest, scientific/historical research, statistical purposes (with appropriate safeguards)
- [ ] Art. 17(3)(f): Processing necessary for establishment, exercise, or defense of legal claims
  - **Legal Claim**: [Describe, e.g., "Pending litigation Case No. XYZ-2024-1234"]

**Legal Hold Conflict**:
- [ ] YES - Data subject to active legal hold  
  - **Hold ID**: [Reference to legal hold register]  
  - **Action**: Restriction of processing applied per GDPR Art. 18 (see below)
- [ ] NO - No legal hold applies

---

### Response to Data Subject

**Response Date**: [DD.MM.YYYY] (must be within 30 days of request receipt per GDPR Art. 12(3))  
**Response Method**: [ ] Email [ ] Postal Mail [ ] In-Person [ ] Secure Portal  
**Response Status**: [ ] On Time (<30 days) [ ] Extended (notified data subject of extension per GDPR Art. 12(3))  

**Response Content**:

**If ERASURE APPROVED**:

"Dear [Data Subject],

We have processed your request for erasure of your personal data received on [Request Date].

**Decision**: Your request has been **APPROVED**. We have erased your personal data from our systems as detailed below.

**Data Erased**:
- [List systems/databases where data was erased, e.g., "Customer database", "Email archives", "Backup systems"]
- [Specify data categories erased, e.g., "Name, email address, order history, support tickets"]

**Erasure Completion Date**: [DD.MM.YYYY]

**Third-Party Notification**: We have notified the following third parties who received your personal data, as required under GDPR Article 19:
- [List third parties notified, e.g., "Payment processor XYZ", "Cloud backup provider ABC"]
- Notification Date: [DD.MM.YYYY]

**Data Retained** (if any - with legal basis):
- [List any data that could NOT be erased with legal justification, e.g., "Billing records retained until [Date] per Swiss OR Art. 958f accounting requirements"]

**Your Rights**: You have the right to lodge a complaint with the Swiss Federal Data Protection and Information Commissioner (FDPIC) or your local data protection authority if you believe your rights have been violated.

Best regards,  
[Organisation] Data Protection Officer"

---

**If ERASURE DENIED**:

"Dear [Data Subject],

We have processed your request for erasure of your personal data received on [Request Date].

**Decision**: We are **unable to erase** your personal data at this time due to legal exceptions under GDPR Article 17(3).

**Legal Basis for Denial**:
[Detailed explanation referencing specific GDPR Art. 17(3) exception and legal obligation/legitimate interest]

Example:
"Your personal data is subject to a 10-year retention requirement under Swiss Code of Obligations (OR) Article 958f for accounting records. We are legally obligated to retain [specify data categories] until [Date]. Erasure before this date would violate Swiss law."

OR

"Your personal data is currently subject to preservation for a pending legal claim [Case Reference]. Under GDPR Article 17(3)(f), we are entitled to retain data necessary for the establishment, exercise, or defense of legal claims."

**Alternative Protection - Restriction of Processing**:
As an alternative to erasure, we have implemented **restriction of processing** per GDPR Article 18:
- Your data is marked as "restricted" in our systems
- Access is limited to authorised personnel only (Legal/Compliance)
- Your data will NOT be used for business operations or marketing
- You will be notified before the restriction is lifted

**Anticipated Erasure Date**: [Date when legal obligation ceases or legal hold is released]

**Your Rights**: 
- You have the right to lodge a complaint with the Swiss Federal Data Protection and Information Commissioner (FDPIC) or your local data protection authority.
- You may request rectification of inaccurate personal data or restriction of processing while we verify the lawfulness of processing.

Best regards,  
[Organisation] Data Protection Officer"

---

### Erasure Execution (if approved)

**Execution Start Date**: [DD.MM.YYYY]  
**Execution Completion Date**: [DD.MM.YYYY] (must be within 60 days of request receipt)  
**Executed By**: [IT Operations personnel]  

**Systems/Data Erased**:

| System / Database | Data Categories Erased | Erasure Method | Verification | Completion Date |
|-------------------|----------------------|----------------|--------------|-----------------|
| [e.g., CRM Database] | [e.g., Name, email, phone, address] | [e.g., SQL DELETE + backup purging] | [e.g., Database query confirming absence] | [DD.MM.YYYY] |
| [e.g., Email Archives] | [e.g., Email correspondence] | [e.g., Archive deletion API] | [e.g., Archive search confirming absence] | [DD.MM.YYYY] |
| [e.g., Backup Systems] | [e.g., All personal data in backups] | [e.g., Backup purge + retention policy enforcement] | [e.g., Backup catalog query] | [DD.MM.YYYY] |
| [e.g., Cloud Storage] | [e.g., Uploaded files, documents] | [e.g., API deletion + verification query] | [e.g., HTTP 200 response + absence verification] | [DD.MM.YYYY] |

**Backup Deletion Verification**: 
- [ ] ✅ Verified - Deleted data absent from all backups within retention window
- [ ] ⚠️ Partial - Data will be purged within [X] days per backup rotation schedule (documented and Data Owner approved)
- [ ] ❌ Issue - [Describe backup deletion issue and remediation]

**Third-Party Notification** (GDPR Art. 19):

| Third Party | Notification Date | Notification Method | Response/Confirmation | Status |
|-------------|-------------------|--------------------|-----------------------|--------|
| [e.g., Payment Processor XYZ] | [DD.MM.YYYY] | [e.g., Email to DPO] | [e.g., Confirmed erasure on DD.MM.YYYY] | [✅ Complete] |
| [e.g., Cloud Backup Provider ABC] | [DD.MM.YYYY] | [e.g., Support ticket] | [e.g., Deletion certificate received] | [✅ Complete] |

**If Third-Party Notification NOT Required**:
- [ ] Notification impossible or involves disproportionate effort
- **Rationale**: [Explain why notification was not required, e.g., "Third party is processor, not controller, and received erasure instruction"]

---

### Data Retained (if any)

**Data NOT Erased** (with legal justification):

| Data Category | System | Legal Basis for Retention | Retention Period | Review Date |
|---------------|--------|--------------------------|------------------|-------------|
| [e.g., Billing records] | [e.g., Accounting system] | [e.g., Swiss OR Art. 958f] | [e.g., Until DD.MM.YYYY (10 years from transaction)] | [Annual review date] |
| [e.g., Litigation-related correspondence] | [e.g., Legal hold system] | [e.g., GDPR Art. 17(3)(f) - legal claims] | [e.g., Until case resolution + 3 years] | [Quarterly legal hold review] |

**If NO Data Retained**:
- [X] All personal data has been erased
- [X] No legal basis exists for retention
- [X] Data subject has been notified of complete erasure

---

### Restriction of Processing (if applied)

**Restriction Applied**:
- [ ] YES - Restriction of processing applied per GDPR Art. 18
- [ ] NO - Erasure completed without restriction

**If Restriction Applied**:

**Reason for Restriction**:
- [ ] Data subject contests lawfulness of processing (Art. 18(1)(a))
- [ ] Processing unlawful but data subject opposes erasure (Art. 18(1)(b))
- [ ] Data no longer needed but data subject needs for legal claims (Art. 18(1)(c))
- [ ] Data subject objects to processing, pending verification of overriding grounds (Art. 18(1)(d))
- [ ] Legal hold conflict (erasure request during active legal hold - internal reason)

**Restriction Implementation**:
- Data marked as "RESTRICTED - PROCESSING LIMITED" in systems
- Access limited to: [List roles, e.g., "Legal/Compliance Officer only"]
- Data excluded from: [List processes, e.g., "Marketing, analytics, business operations"]
- Monitoring: [Describe access monitoring, e.g., "All access logged and reviewed monthly"]

**Restriction Duration**:
- From: [DD.MM.YYYY]
- Until: [Event trigger, e.g., "Legal hold release", "Verification of lawfulness complete"]
- Next Review: [DD.MM.YYYY]

**Data Subject Notification of Restriction**:
- Notified on: [DD.MM.YYYY]
- Method: [Email, Postal Mail]
- Content: [Brief summary of notification content]

**Lifting of Restriction**:
- Restriction will be lifted when: [Condition, e.g., "Legal hold released", "Lawfulness verified"]
- Data subject will be notified BEFORE lifting restriction per GDPR Art. 18(3)
- Upon lifting, data will be: [ ] Erased immediately [ ] Resumed normal processing [ ] Other: [Specify]

---

### Request Closure

**Closure Date**: [DD.MM.YYYY]  
**Closure Status**: 
- [ ] ✅ Complete - Erasure executed and verified
- [ ] ✅ Complete - Erasure denied with legal basis, restriction applied
- [ ] ⚠️ Partial - Some data erased, some retained (legal basis documented)
- [ ] ❌ Failed - Unable to complete (escalate to CISO + DPO)

**Final Verification**:
- [ ] Data subject notified (response sent and confirmed received)
- [ ] Erasure executed in all applicable systems
- [ ] Third parties notified per GDPR Art. 19
- [ ] Evidence collected and filed (deletion logs, certificates, third-party confirmations)
- [ ] Request log updated with closure information
- [ ] If denied: Legal basis documented and restriction applied

**Closure Approved By**: [DPO name and signature]  
**Closure Approval Date**: [DD.MM.YYYY]  

---

### Post-Closure Review (for Quality Assurance)

**Quality Review Date**: [DD.MM.YYYY + 30 days] (monthly QA sampling)  
**Reviewed By**: [DPO or Compliance Officer]  

**Review Checklist**:
- [ ] Identity verification was appropriate
- [ ] Legal assessment was correct (erasure obligation vs. exception)
- [ ] Response timeline met (within 30 days)
- [ ] Erasure execution was complete (all systems, backups, third parties)
- [ ] Third-party notifications sent where required
- [ ] Legal basis for retained data is documented and valid
- [ ] Restriction of processing implemented correctly (if applicable)
- [ ] Evidence is complete and filed correctly

**Quality Issues Identified** (if any):
[List any process improvements, training needs, or systemic issues discovered]

**Corrective Actions**:
[Document any improvements made to erasure request process based on this review]

---

**Request Documentation**: All completed erasure request forms are retained in data subject request register for **3 years** from closure date per GDPR accountability requirements (Art. 5(2)) and Swiss nDSG documentation obligations.

---

# Annex C: Exception Request Template

**Purpose**: Standardized format for requesting exceptions to information deletion policy requirements per Section 3.3 policy requirements.

**Usage**: System Owners, Data Owners, or IT Operations use this template when standard deletion requirements cannot be met. All exceptions require documented business justification, risk assessment, compensating controls, and formal approval per Section 3.3 authority matrix.

---

## Exception Request Form

**Exception Request ID**: [AUTO-GENERATED: EXC-A810-YYYY-NNN]  
**Request Date**: [DD.MM.YYYY]  
**Requested By**: [Name, Title, Department]  
**Data Owner**: [Name, Title] — Must approve this exception  

---

### Exception Scope

**Systems Affected**:
- [List all systems, databases, applications, storage locations affected by this exception]

**Data Categories Affected**:
- [List data categories: PII, Financial, Health, Credentials, Proprietary, etc.]
- [Specify data elements: table names, field names, file types, data classifications]

**Environments**:
- [ ] Production
- [ ] Test/QA
- [ ] Development
- [ ] Analytics/BI
- [ ] Training/Sandbox
- [ ] Backup/Archive
- [ ] Other: [Specify]

**Data Sensitivity Classification**:
- [ ] Restricted (Critical)
- [ ] Confidential (High)
- [ ] Internal (Medium)
- [ ] Public (Low - exception rarely needed)

**Volume/Scope**:
- Approximate number of records affected: [Number]
- Storage size: [GB/TB]
- Number of users with access: [Number]

---

### Standard Requirement NOT Being Met

**Policy Requirement** (reference Section 2 policy statements):

[Quote or reference specific policy requirement that cannot be met, e.g.:]

"Policy Section 2.1: Deletion SHALL be triggered by retention period expiry. Retention schedule defines maximum retention period for [Data Category] as [X years]."

OR

"Policy Section 2.2: Backup deletion SHALL extend to ALL backup copies within retention window."

**Deviation Requested**:

[Describe exactly what you are requesting permission to do differently, e.g.:]

"Request to extend retention period for [Data Category] from [X years] to [Y years] for systems [List]."

OR

"Request to defer backup deletion for [Data Category] until backup architecture upgrade completion (estimated [Date])."

---

### Business Justification

**Why is the standard requirement infeasible?**

[Provide detailed explanation - select applicable reasons and elaborate:]

**Technical Infeasibility**:
- [ ] System limitation (describe technical constraint preventing compliance)
- [ ] Backup architecture constraint (describe why backup deletion cannot be executed)
- [ ] Data structure dependency (describe referential integrity or data relationship issues)
- [ ] Third-party provider limitation (describe provider capabilities or contract restrictions)

**Operational Necessity**:
- [ ] Business-critical process depends on data (describe specific business operations requiring data)
- [ ] Regulatory conflict (describe conflicting regulatory retention requirement)
- [ ] Contractual obligation (describe customer/supplier contract requiring retention)
- [ ] Legal hold (describe litigation/investigation requiring preservation)

**Cost Disproportionality**:
- [ ] Deletion cost exceeds risk reduction value (provide cost-benefit analysis)
- [ ] System replacement required (deletion feasible only with major infrastructure investment)

**Detailed Explanation**:

[Provide comprehensive justification - avoid generic statements]

**Business Impact if Exception Denied**:

[Describe specific operational consequences, business disruption, compliance issues, financial impact]

Examples:
- "Inability to fulfill [Customer] contract requiring [Retention Period] data retention, risking [€X] annual revenue loss"
- "Inability to complete [Business Process] requiring historical data analysis, delaying [Project] by [X months]"
- "Violation of [Regulatory Requirement] if data is deleted before [Legal Retention Period]"

---

### Duration of Need

**Exception Start Date**: [DD.MM.YYYY]  
**Exception End Date**: [DD.MM.YYYY]  

**Maximum Exception Duration** (per policy Section 3.3):
- Internal/Public data: 12 months maximum
- Confidential data: 6 months maximum  
- Restricted data: 6 months maximum (requires CISO + DPO + Data Owner approval)

**Path to Compliance**:

[Describe plan to achieve full deletion compliance - REQUIRED for approval]

| Milestone | Activity | Target Date | Owner | Status |
|-----------|----------|-------------|-------|--------|
| [e.g., Tool evaluation] | [e.g., Evaluate backup deletion tools supporting [Backup Type]] | [DD.MM.YYYY] | [IT Operations] | [Not Started] |
| [e.g., Budget approval] | [e.g., Obtain budget for backup architecture upgrade] | [DD.MM.YYYY] | [CIO] | [Not Started] |
| [e.g., Implementation] | [e.g., Deploy new backup solution with deletion capabilities] | [DD.MM.YYYY] | [IT Operations] | [Not Started] |
| [e.g., Testing] | [e.g., Validate backup deletion in test environment] | [DD.MM.YYYY] | [System Owner] | [Not Started] |
| [e.g., Production cutover] | [e.g., Migrate to new backup system in production] | [DD.MM.YYYY] | [IT Operations] | [Not Started] |
| [e.g., Exception closure] | [e.g., Close exception after validation] | [DD.MM.YYYY] | [CISO] | [Not Started] |

---

### Risk Assessment

**Inherent Risk** (without deletion control):

**Likelihood of Data Exposure**:
- [ ] Low (1) - Unlikely to be exposed (strong compensating controls)
- [ ] Medium (2) - Possible exposure (moderate compensating controls)
- [ ] High (3) - Probable exposure (weak compensating controls)
- [ ] Critical (4) - Exposure highly likely (minimal compensating controls)

**Impact if Exposed**:
- [ ] Low (1) - Minimal harm (Internal/Public data, limited scope)
- [ ] Medium (2) - Moderate harm (Confidential data, limited scope OR Internal data, large scope)
- [ ] High (3) - Substantial harm (Confidential data, large scope OR Restricted data, limited scope)
- [ ] Critical (4) - Severe harm (Restricted data, large scope; regulatory breach notification likely)

**Inherent Risk Score**: [Likelihood × Impact = X]

**Threat Scenarios**:

[List specific risks enabled by undeleted data:]

1. [e.g., "Unauthorised access by terminated employee with retained credentials (likelihood: Medium, impact: High)"]
2. [e.g., "Data breach via backup tape theft (likelihood: Low, impact: Critical)"]
3. [e.g., "Regulatory non-compliance - GDPR storage limitation violation (likelihood: High, impact: High)"]
4. [e.g., "Data subject erasure request cannot be fulfilled (likelihood: Medium, impact: High)"]

**Compliance Impact**:

**Regulatory Violations** (if exception approved):
- [ ] Swiss nDSG Art. 6 (Data minimisation) - [Describe violation and potential penalty]
- [ ] GDPR Art. 5(1)(e) (Storage limitation) - [Describe violation and potential penalty up to €20M or 4% global turnover]
- [ ] GDPR Art. 17 (Right to erasure) - [Describe inability to fulfill data subject requests]
- [ ] Sector-specific: [PCI DSS, HIPAA, FINMA, etc. - describe if applicable per ISMS-POL-00]

---

### Compensating Controls

**Alternative Protections Implemented**:

[Describe controls that partially mitigate risk of undeleted data - REQUIRED for approval]

Select and detail applicable compensating controls:

- [ ] **Enhanced Access Controls**
  - Roles with access reduced to: [List specific roles]
  - Multi-factor authentication enforced: [Yes/No]
  - Privileged access management (PAM) implemented: [Yes/No]
  - Access approval workflow: [Describe approval process]
  
- [ ] **Encryption**
  - Data encrypted at rest: [Yes/No - encryption method]
  - Data encrypted in transit: [Yes/No - encryption method]
  - Encryption keys managed separately: [Yes/No - key management system]
  - Cryptographic erasure as alternative: [Planned/Not Applicable]

- [ ] **Enhanced Monitoring and Alerting**
  - Access logging enabled: [Yes/No - log retention period]
  - Unauthorised access alerts configured: [Yes/No - alert criteria]
  - Quarterly access reviews: [Yes/No - reviewer]
  - SIEM integration: [Yes/No]

- [ ] **Data Minimization**
  - Dataset scope reduced (removed unnecessary fields): [Yes/No - describe]
  - Dataset size reduced (deleted oldest records within exception scope): [Yes/No - describe]
  - Sensitive fields masked within exception data: [Yes/No - describe]

- [ ] **Network Segmentation**
  - Systems with undeleted data isolated in separate network segment: [Yes/No]
  - Firewall rules restricting access: [Yes/No - describe rules]
  - VPN required for access: [Yes/No]

- [ ] **Time-Limited Access**
  - Access restricted to specific time windows: [Describe, e.g., "Business hours only"]
  - Access auto-expires after: [Duration]
  - Access re-approval required: [Frequency]

- [ ] **User Training and Acceptable Use**
  - Users with access completed training: [Yes/No - training date]
  - Acceptable use acknowledgment signed: [Yes/No]
  - Users informed of monitoring: [Yes/No]

- [ ] **Physical Security** (for backup media)
  - Media stored in locked facility: [Yes/No - location]
  - Access logged: [Yes/No]
  - Environmental controls (fire suppression, etc.): [Yes/No]

- [ ] **Other**
  - [Describe additional compensating control]

**Compensating Control Effectiveness**:

- **Estimated Risk Reduction**: [Percentage, e.g., "40% reduction" OR qualitative, e.g., "Medium → Low likelihood"]
- **Residual Risk Score**: [Adjusted likelihood × Impact = Y]
- **Residual Risk Acceptability**: [ ] Acceptable [ ] Requires further mitigation [ ] Unacceptable without exception

**Residual Risk Justification**:

[Explain why residual risk is acceptable for exception duration, or what additional mitigations are planned]

---

### Monitoring and Compliance

**How will compliance with exception conditions be verified?**

[Describe monitoring and verification procedures:]

- **Access Monitoring**: [e.g., "Quarterly review of access logs by Security Team, flagging unauthorised access attempts"]
- **Compensating Control Verification**: [e.g., "Monthly verification that encryption is enabled, MFA is enforced"]
- **Milestone Tracking**: [e.g., "Bi-weekly project status reviews tracking path to compliance milestones"]
- **Incident Detection**: [e.g., "SIEM alerts for unauthorised access, data exfiltration attempts"]

**Review Schedule**:

- [ ] Monthly (for Critical/Restricted data sensitivity)
- [ ] Quarterly (for High/Confidential data sensitivity)
- [ ] Semi-Annual (for Medium/Internal data sensitivity)

**Review Process**:

| Review Date | Reviewer | Review Focus | Outcome | Next Review |
|-------------|----------|--------------|---------|-------------|
| [DD.MM.YYYY] | [CISO / Security Team] | [Compensating controls operational? Milestones on track?] | [Approved / Needs Action / Revoked] | [DD.MM.YYYY] |

**Revocation Triggers**:

[Under what conditions will this exception be immediately revoked? - REQUIRED]

Examples:
- [ ] Compensating control failure (e.g., encryption disabled, access controls bypassed)
- [ ] Security incident involving undeleted data (e.g., unauthorised access, data breach)
- [ ] Business justification no longer valid (e.g., contract terminated, project cancelled)
- [ ] Deletion solution becomes available ahead of schedule
- [ ] Data subject erasure request cannot be fulfilled (GDPR violation risk)
- [ ] Regulatory examination identifies exception as non-compliant
- [ ] Exception duration expires (automatic revocation, no implicit renewal)

---

### Approvals

**Data Owner Approval**:

- Name: [Data Owner Name and Title]
- **Acknowledges**: Risk to data under my ownership; responsibility for compensating controls
- Signature: ________________
- Date: [DD.MM.YYYY]
- Comments: [Optional - Data Owner concerns, conditions for approval]

---

**Security Team Review**:

- Reviewer: [Security Team Lead Name]
- **Risk Assessment**: [ ] ✅ Acceptable with compensating controls [ ] ⚠️ Acceptable with conditions [ ] ❌ Not Acceptable (risk too high)
- **Compensating Controls**: [ ] ✅ Sufficient [ ] ⚠️ Adequate but should be strengthened [ ] ❌ Insufficient
- Signature: ________________
- Date: [DD.MM.YYYY]
- **Conditions for Approval** (if applicable): [List specific conditions Security Team requires, e.g., "MFA must be enabled before exception takes effect"]
- **Comments/Recommendations**: [Security Team assessment and recommendations]

---

**CISO Approval** (Required for Confidential/Restricted data):

- Name: [CISO Name]
- [ ] ✅ **Approved** [ ] ⚠️ **Approved with Conditions** [ ] ❌ **Denied**
- **Conditions** (if applicable): [List CISO-imposed conditions]
- Signature: ________________
- Date: [DD.MM.YYYY]
- **Risk Acceptance**: I accept the residual risk score of [Y] for exception duration of [X months]
- **Comments**: [CISO rationale for decision]

---

**DPO Approval** (Required for Restricted data or personal data):

- Name: [DPO Name]
- [ ] ✅ **Approved** (privacy compliance acceptable with compensating controls)
- [ ] ⚠️ **Approved with Conditions** (list conditions below)
- [ ] ❌ **Denied** (unacceptable privacy risk or regulatory violation)
- **GDPR/nDSG Assessment**: [DPO assessment of regulatory compliance]
- **Data Subject Rights Impact**: [Can erasure requests still be fulfilled? If not, document legal basis per GDPR Art. 17(3)]
- Signature: ________________
- Date: [DD.MM.YYYY]
- **Conditions/Comments**: [DPO requirements for approval]

---

**Executive Management Approval** (Required for production exceptions):

- Name: [Executive Management Name and Title]
- [ ] ✅ **Approved** [ ] ❌ **Denied**
- **Strategic Justification**: [Why this exception is necessary for business operations]
- **Budget Approval** (if compliance path requires investment): [ ] Approved €[Amount] [ ] Denied
- Signature: ________________
- Date: [DD.MM.YYYY]

---

### Exception Tracking

**Exception Status**:

- [ ] Pending Approval (submitted, awaiting review)
- [ ] Approved (all required approvals obtained, effective [Start Date])
- [ ] Approved with Conditions (conditions must be met before effective date)
- [ ] Denied (risk unacceptable or justification insufficient)
- [ ] Expired (duration reached, exception auto-expires)
- [ ] Revoked (terminated early due to revocation trigger)

**Exception Effective Period**:

- Start Date: [DD.MM.YYYY] (date exception takes effect)
- End Date: [DD.MM.YYYY] (automatic expiration, no implicit renewal)
- Days Remaining: [Auto-calculate: End Date - Today]
- **Warning**: Exception will auto-expire on End Date unless formally renewed with updated risk assessment

**Exception Review Log**:

| Review Date | Reviewer | Compensating Controls Status | Milestones Status | Risk Score | Decision | Comments | Next Review |
|-------------|----------|------------------------------|-------------------|------------|----------|----------|-------------|
| [DD.MM.YYYY] | [CISO] | [✅ Operational / ⚠️ Issues / ❌ Failed] | [✅ On Track / ⚠️ Delayed / ❌ Blocked] | [Current risk score] | [Continue / Revoke / Extend] | [Brief summary] | [DD.MM.YYYY] |

---

### Exception Renewal (if requested)

**Renewal Request Date**: [DD.MM.YYYY]  
**Renewal Requested By**: [Name]  
**Renewal Justification**: [Why is exception still needed? What compliance progress was made?]  

**Updated Risk Assessment**:
- Previous Residual Risk: [Y]
- Current Residual Risk: [Z] (reassessed)
- Risk Trend: [ ] Decreasing (compensating controls strengthened) [ ] Stable [ ] Increasing (control degradation or new threats)

**Compliance Progress Since Last Approval**:

| Milestone | Original Target | Actual Status | Variance | Explanation |
|-----------|-----------------|---------------|----------|-------------|
| [Milestone 1] | [Date] | [✅ Complete / ⚠️ In Progress / ❌ Blocked] | [Days delayed if applicable] | [Brief explanation] |

**Renewal Approval Requirements**:

- **Second Renewal**: Maximum 6 months (even if first exception was 12 months)
- **Third Renewal**: Maximum 3 months + requires Executive Management approval regardless of data sensitivity
- **Renewal Limitations**: Exception renewed more than twice WITHOUT demonstrable compliance progress will be DENIED

**Renewal Decision**:

- [ ] ✅ Approved (new end date: [DD.MM.YYYY])
- [ ] ⚠️ Approved with Enhanced Conditions (list below)
- [ ] ❌ Denied (must achieve compliance or accept revocation)

**Enhanced Conditions for Renewal** (if applicable):
[List additional requirements for renewed exception, e.g., "Monthly reviews instead of quarterly", "Additional compensating control X required"]

---

### Exception Closure

**Closure Date**: [DD.MM.YYYY]  
**Closure Reason**:
- [ ] Compliance Achieved (deletion requirement now met)
- [ ] Exception Expired (duration reached)
- [ ] Exception Revoked (revocation trigger occurred)
- [ ] Business Justification Ceased (no longer needed)

**Final Verification**:
- [ ] Deletion control now implemented (describe solution)
- [ ] Compensating controls decommissioned (if no longer needed)
- [ ] Risk register updated (residual risk from exception removed)
- [ ] Exception register updated (status changed to Closed)
- [ ] Lessons learned documented (process improvements identified)

**Closure Approved By**: [CISO name and signature]  
**Closure Date**: [DD.MM.YYYY]  

**Lessons Learned**:
[Document what was learned from this exception - process improvements, technology gaps, training needs]

---

**Exception Documentation**: All approved exceptions are maintained in exception register (tracked in ISMS-IMP-A.8.10.3 Environment Coverage Assessment) and retained for **Life of Exception + 3 years** per Section 3.3 policy requirements.

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Evidence required to demonstrate this policy is adequately documented and approved:

- ✅ This policy document (ISMS-POL-A.8.10 v1.0)
- ✅ Approval signatures from CISO, DPO, Legal/Compliance, Executive Management
- ✅ Retention period requirements documented
- ✅ Deletion methods specified by data sensitivity
- ✅ Third-party and cloud deletion requirements defined
- ✅ Verification requirements documented
- ✅ Data subject erasure request process defined
- ✅ Roles and responsibilities assigned

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Deletion execution logs
- Retention schedule (current + superseded versions)
- Third-party certificates of destruction
- GDPR request log
- Legal hold register
- Exception approvals
- Quarterly compliance reports
- Data inventory with deletion scope

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Data Protection Officer (DPO)** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

*This policy establishes requirements. Implementation procedures are documented in ISMS-IMP-A.8.10 suite (Retention & Deletion Triggers, Deletion Methods, Third-Party & Cloud Deletion, Verification & Evidence).*

---

<!-- QA_VERIFIED: 2026-03-01 -->