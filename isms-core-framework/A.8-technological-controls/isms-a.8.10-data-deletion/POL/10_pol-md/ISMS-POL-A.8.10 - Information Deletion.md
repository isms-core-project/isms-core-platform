**ISMS-POL-A.8.10 - Information Deletion Policy**

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

---

# Executive Summary

This policy establishes [Organization]'s requirements for secure deletion of information when no longer required, in accordance with ISO/IEC 27001:2022 Control A.8.10.

**Purpose**: Define organizational requirements for information deletion control implementation and governance. This policy establishes WHAT deletion protection is required, WHEN deletion must occur, and WHO is accountable.

**Scope**: This policy applies to:

- All information assets regardless of storage location (on-premises, cloud, third-party)
- All storage media types (magnetic, solid-state, optical, paper, mobile devices)
- All personnel (employees, contractors) and third parties processing organizational data
- All lifecycle stages requiring deletion (retention expiry, data subject requests, contract termination, asset decommissioning, legal hold release)

**Regulatory Alignment**: This policy addresses mandatory compliance requirements including:

- **Swiss nDSG** - Data minimization and data subject rights
- **EU GDPR Article 17** - Right to erasure
- **ISO/IEC 27001:2022 Control A.8.10** - Information deletion requirements

---

# Scope

## In Scope

**Information Assets**:

- All data categories (personal data, confidential business information, financial records, technical data, communications, logs)
- All classification levels per [Organization]'s classification scheme
- All formats (structured databases, unstructured files, email, backups, system logs)
- All lifecycle stages (active use, archival, backup, disaster recovery, development/test)

**Storage Locations**:

- On-premises infrastructure (data centers, server rooms, local storage)
- Cloud infrastructure (IaaS, PaaS, SaaS across all providers)
- Third-party processing locations (managed service providers, subcontractors)
- Backup and disaster recovery systems
- End-user devices (laptops, desktops, mobile devices, removable media)

**Organizational Coverage**:

- All employees (permanent, temporary, contractors)
- All third-party service providers processing organizational data
- All cloud service providers storing organizational information
- All business units and geographic locations

## Out of Scope

- Physical equipment disposal without data considerations (covered under asset management)
- Data anonymization or pseudonymization as alternatives to deletion (covered under privacy policies)
- Data archival for long-term retention within retention periods (covered under records management)
- Encryption key management except for cryptographic erasure (covered under ISMS-POL-A.8.24)

---

# Policy Statements

## Retention and Deletion Triggers

**POL-8.10-01**: [Organization] SHALL maintain a comprehensive inventory of data categories processed, including data type, classification level, business purpose, storage location, and data owner. Inventory completeness SHALL be verified through: (a) automated discovery tools for IT systems; (b) annual attestation from system owners confirming all data categories are registered; (c) quarterly reconciliation of inventory against IT asset register (per ISMS-POL-A.5.9) and cloud service registry (ISMS-REF-A.5.23).

**POL-8.10-02**: [Organization] SHALL establish retention schedules for all data categories based on legal requirements, regulatory requirements, contractual obligations, and documented business needs.

**POL-8.10-03**: Deletion SHALL be triggered by one of the following events:

- Retention period expiry
- Data subject erasure request (GDPR Article 17 / Swiss nDSG)
- Contract or service agreement termination
- Processing purpose completion
- Legal hold release
- Asset decommissioning
- Consent withdrawal

**POL-8.10-04**: Where multiple retention requirements apply, the LONGEST applicable retention period SHALL be implemented unless legal counsel determines otherwise.

**POL-8.10-05**: [Organization] SHOULD implement automated deletion processes where technically feasible, including safeguards against premature deletion (legal hold checks, business owner approval for high-value data).

**POL-8.10-05a**: Technical feasibility assessment for automated deletion SHALL consider: (a) system API capabilities for deletion and verification; (b) data structure complexity (structured vs. unstructured); (c) deletion trigger availability (retention metadata, lifecycle policies); (d) risk of premature deletion (legal hold integration, business-critical data safeguards); (e) cost-benefit analysis (development effort vs. manual process risk). Feasibility assessments SHALL be documented by System Owners during system onboarding and reviewed annually. Where automation is deemed infeasible, manual deletion procedures SHALL be documented with defined verification checkpoints.

## Deletion Method Requirements

**POL-8.10-06**: [Organization] SHALL select deletion methods appropriate for:

- Media type (magnetic, solid-state, optical, paper, cloud storage)
- Data classification level
- Media destination (internal reuse, external transfer, disposal/destruction)
- Recovery risk assessment

**POL-8.10-07**: Deletion methods SHALL align with recognized sanitization standards (NIST SP 800-88 Rev. 2 or equivalent) providing appropriate protection levels:

- **Clear**: For media remaining in organizational control with lower sensitivity data
- **Purge**: For media leaving organizational control or containing sensitive data
- **Destroy**: For end-of-life media or highest sensitivity data

**POL-8.10-08**: Deletion in production systems SHALL extend to ALL backup copies, including incremental/differential backups, snapshots, and disaster recovery replicas.

**POL-8.10-08a**: Backup deletion verification SHALL account for backup technology architecture, including: (a) full/incremental/differential backup dependencies; (b) snapshot-based backups with retention policies; (c) cloud-native backup services with independent retention; (d) application-level backups (database dumps, VM exports) with separate retention. Verification methods include: retention policy enforcement logs, backup catalog queries confirming absence of deleted data identifiers, or documented backup rotation schedules guaranteeing deletion by date certain. Where immediate backup deletion is not technically feasible, maximum retention SHALL be documented and approved by CISO + Data Owner.

**POL-8.10-09**: Where technically feasible, [Organization] SHOULD leverage cryptographic erasure for high-efficiency deletion, with appropriate encryption key management per ISMS-POL-A.8.24 (key lifecycle) and verified key destruction. For cryptographic erasure to constitute deletion per this policy, [Organization] SHALL: (a) document data-to-key mapping enabling identification of encryption keys protecting specific data categories; (b) implement key destruction procedures meeting NIST SP 800-88 Rev. 2 'Purge' level (e.g., cryptographic erase of key storage, HSM key zeroization); (c) verify key destruction through key management system audit logs or HSM certificates; (d) retain key destruction evidence per POL-8.10-14 (3+ years).

## Third-Party and Cloud Deletion

**POL-8.10-10**: [Organization] SHALL include deletion obligations in all contracts with third parties processing organizational data, including:

- Maximum deletion timeline after contract termination or upon request
- Sanitization standards appropriate for data sensitivity
- Deletion scope covering all copies including backups
- Requirement to provide deletion certificate or attestation
- Flow-down of deletion requirements to sub-processors

**POL-8.10-11**: [Organization] SHALL assess cloud service provider deletion capabilities before engagement, including API deletion support, deletion verification mechanisms, multi-tenant isolation, and geographic deletion coverage.

**POL-8.10-12**: [Organization] SHALL obtain verification of deletion from third parties through:

(a) **Certificates of destruction** (for physical media destruction): Must include media serial numbers or asset identifiers, destruction method referencing NIST SP 800-88 Rev. 2 level (Clear/Purge/Destroy), destruction date and location, certificate issuer name and accreditation (if applicable)

(b) **Audit reports** (for service provider logical deletion): SOC 2 Type II report with deletion control testing, OR independent audit report verifying deletion procedures, OR ISO 27001 certification with Annex A.8.10 in scope

(c) **API response logging** (for cloud/SaaS deletion): API call timestamp and authenticated user, resource identifier, HTTP success response (200/204), confirmation of backup/snapshot deletion where provider offers this capability

**For High/Critical classification data**: Certificates from accredited destruction vendors (e.g., NAID AAA, ISO 21964) OR independent audit reports are REQUIRED (API logs alone insufficient).

## Verification and Evidence

**POL-8.10-13**: [Organization] SHALL maintain comprehensive deletion audit trails including deletion timestamp, data category, deletion method, media identifier, deletion trigger, responsible party, and verification result.

**POL-8.10-14**: Deletion logs SHALL be retained for a minimum of 3 years or per applicable regulatory requirements (whichever is longer).

**POL-8.10-15**: [Organization] SHALL generate or obtain deletion certificates for sensitive data, with external certificates required for third-party destruction services.

**POL-8.10-16**: [Organization] SHALL implement verification procedures to confirm deletion effectiveness, including automated confirmation, periodic sampling, and attestations.

## Evidence Requirements

**POL-8.10-16a**: [Organization] SHALL maintain the following evidence types to demonstrate deletion control effectiveness:

| Evidence Type | Purpose | Owner | Retention |
|---------------|---------|-------|-----------|
| **Deletion execution logs** | Prove deletions occurred per schedule | IT Ops | 3 years |
| **Retention schedule** | Define required retention by data category | Records Mgr | Current + superseded versions (7 years) |
| **Third-party certificates** | Verify third-party deletion compliance | IT Ops | 3 years from deletion date |
| **GDPR request log** | Demonstrate data subject rights compliance | DPO | 3 years from request closure |
| **Legal hold register** | Justify deletion suspension | Legal | 3 years from hold release |
| **Exception approvals** | Document approved deviations | CISO | Life of exception + 3 years |
| **Quarterly compliance reports** | Aggregate deletion metrics, gap analysis | CISO | 3 years |
| **Data inventory** | Establish deletion scope | Records Mgr | Current + quarterly snapshots (3 years) |

Evidence generation and aggregation procedures are defined in ISMS-IMP-A.8.10.5 (Compliance Dashboard Consolidation).

## Data Subject Erasure Requests

**POL-8.10-17**: [Organization] SHALL accept and process data subject erasure requests in compliance with GDPR Article 17 and Swiss nDSG, including:

- Accepting requests via multiple channels
- Logging all requests within 24 hours
- Verifying data subject identity before processing
- Responding within 30 days (GDPR deadline)

**POL-8.10-18**: The DPO SHALL assess whether erasure obligation applies or legal exceptions exist (legal obligation, public interest, legal claims, archiving in public interest).

**POL-8.10-19**: Where erasure is denied based on legal exception, [Organization] SHALL document the specific legal basis and provide written explanation to the data subject including complaint rights.

**POL-8.10-20**: Where personal data was disclosed to third parties, [Organization] SHALL notify them of the erasure request per GDPR Article 19.

## Legal Hold Management

**POL-8.10-21**: [Organization] SHALL suspend deletion when required by legal holds for:

- Litigation (filed, threatened, or reasonably anticipated)
- Government investigation or regulatory examination
- Internal investigation requiring forensic preservation
- External audit requiring specific data preservation

**POL-8.10-22**: ONLY the Legal/Compliance Officer may initiate or release legal holds.

**POL-8.10-23**: Legal holds SHALL be reviewed at least quarterly to assess continued necessity. Reviews SHALL produce documented assessment including: (a) hold identifier and initiation date; (b) current litigation/investigation status; (c) continued necessity determination with legal basis; (d) scope adjustment if applicable (narrowing to specific data categories); (e) anticipated hold release date or trigger condition; (f) reviewer name and review date. Reviews SHALL be signed by Legal/Compliance Officer.

**POL-8.10-24**: Data held beyond normal retention period due to legal hold SHALL be deleted within 90 days of hold release unless approved business justification exists.

**POL-8.10-25**: When data subject erasure request conflicts with legal hold, restriction of processing SHALL be applied, and deletion SHALL execute immediately upon hold release.

## Exception Management

**POL-8.10-26**: Exceptions to standard deletion procedures require documented request including data category, business justification, risk assessment, compensating controls, and proposed expiry date.

**POL-8.10-27**: Exception approval authority is determined by data sensitivity and duration:

- Low-sensitivity data, <12 months: System Owner + CISO
- Medium-sensitivity data, <6 months: CISO + DPO
- High-sensitivity data, any extension: CISO + DPO + Legal + Executive Management

**POL-8.10-28**: The following exceptions are PROHIBITED:

- Indefinite retention without specific end date
- Exceptions to avoid legitimate data subject erasure requests
- Exceptions to circumvent regulatory retention requirements
- Blanket exceptions for entire data categories without specific justification

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Primary Accountabilities |
|------|-------------------------|
| **CISO** | Policy framework, deletion method approval, exception approval, compliance monitoring |
| **DPO** | Data subject request handling, privacy compliance, retention schedule review |
| **Legal/Compliance Officer** | Legal hold management, third-party contract terms, regulatory interpretation |
| **CIO/IT Director** | Deletion technology implementation, IT operations oversight |
| **IT Operations** | Deletion execution, logging, verification, tool maintenance |
| **System Owners** | System-specific deletion implementation, coordination with IT |
| **Data Owners** | Retention period definition, business-critical data approval |
| **Records Manager** | Organizational retention schedule maintenance |

## Escalation

**Escalation Triggers**:

- Deletion failure affecting high-sensitivity data
- Data subject request approaching 30-day deadline
- Third-party refusal to provide deletion verification
- Legal hold conflicting with erasure request
- Discovery of retained data exceeding retention period by >90 days

**Escalation Path**: IT Operations -> System Owner -> CIO/CISO -> DPO (privacy) / Legal (holds) -> Executive Management

**Third-Party Deletion Failure Escalation**:
- **T+0 days**: IT Operations logs failure in gap register, initiates follow-up with third-party contact
- **T+15 days**: System Owner escalates to third-party account manager, CCs CISO + DPO
- **T+30 days**: CISO escalates to third-party executive contact, initiates contract review with Legal
- **T+45 days**: Executive Management reviews contractual remedies (service credits, termination for material breach), considers data migration to compliant provider
- **For high-sensitivity data**: Escalation accelerated (T+7, T+15, T+21 days)

---

# Compliance and Exceptions

## Regulatory Framework

**Mandatory Compliance (Tier 1)**:

| Regulation | Key Deletion Requirements |
|------------|--------------------------|
| **Swiss nDSG** | Art. 6 - Data minimization; Art. 19 - Data subject erasure rights; Art. 7 - Technical measures |
| **EU GDPR** | Art. 17 - Right to erasure; Art. 5(1)(e) - Storage limitation; Art. 32 - Security measures |
| **ISO 27001:2022** | Control A.8.10 - Documented deletion policy, implemented procedures, evidence of effectiveness |

**Conditional Compliance (Tier 2)**:
Apply where business activities trigger applicability (per ISMS-POL-00):

- PCI DSS v4.0.1 (payment card data processing)
- HIPAA Security Rule (US healthcare data)
- FINMA (Swiss financial services)
- DORA/NIS2 (EU financial services, critical infrastructure)

## Non-Compliance

Violations of this policy may result in:

- Disciplinary action up to and including termination
- Civil or criminal penalties under applicable law
- Regulatory sanctions and fines
- Reputational damage to [Organization]

## Exception Process

All exceptions must be submitted via the designated exception request form and approved per Section 3.7 authority requirements. Exceptions are reviewed quarterly and auto-expire unless renewed.

---

# Policy Governance

## Review Schedule

**Annual Review**: Full policy review by CISO, DPO, and Legal/Compliance within 12 months of last approval.

**Triggered Reviews**: Policy review initiated within 30 days of:

- Significant regulatory changes
- Major organizational changes (mergers, acquisitions, new business lines)
- Significant deletion-related incidents
- External audit findings
- Technology platform changes

## Training Requirements

| Audience | Content | Frequency |
|----------|---------|-----------|
| All Personnel | Deletion awareness, data handling | Annual |
| IT Operations | Deletion procedures, tools, verification | Initial + annual |
| System Owners | System-specific implementation | Initial + annual |
| DPO Office | Data subject request handling | Initial + regulatory changes |
| Management | Governance, approval responsibilities | Initial + annual |

---

# Related Documents

| Document ID | Document Title |
|-------------|---------------|
| ISMS-POL-00 | Regulatory Applicability Framework |
| ISMS-IMP-A.8.10.1-UG/TG | Retention and Deletion Triggers Assessment |
| ISMS-IMP-A.8.10.2-UG/TG | Deletion Methods Assessment |
| ISMS-IMP-A.8.10.3-UG/TG | Third-Party and Cloud Deletion Assessment |
| ISMS-IMP-A.8.10.4-UG/TG | Verification and Evidence Assessment |
| ISMS-IMP-A.8.10.5-UG/TG | Compliance Dashboard Consolidation |
| ISMS-REF-A.8.10 | Deletion Methods Reference |
| ISMS-REF-A.5.23 | Cloud Service Provider Registry |
| ISMS-FORM-A.8.10-GDPR | Information Deletion Forms and Templates |
| ISO/IEC 27001:2022 | Control A.8.10 - Information Deletion |

---

# Definitions

| Term | Definition |
|------|------------|
| **Information Deletion** | The process of removing data from storage media such that it cannot be recovered through normal or specialized means |
| **Data Sanitization** | All methods of rendering data inaccessible, including clearing, purging, and destroying |
| **Clear** | Logical sanitization protecting against simple, non-invasive recovery techniques |
| **Purge** | Physical or logical sanitization protecting against laboratory attack techniques |
| **Destroy** | Physical sanitization rendering media unusable and data recovery infeasible |
| **Cryptographic Erasure** | Deletion method rendering encrypted data irrecoverable by destroying encryption keys |
| **Retention Period** | Defined timeframe during which data must be kept before deletion is permitted or required |
| **Deletion Trigger** | Event or condition initiating the deletion process |
| **Legal Hold** | Suspension of deletion to preserve data for litigation, investigation, or audit |
| **Data Subject Erasure Request** | Request exercising right to erasure under GDPR Article 17 or Swiss nDSG |
| **Certificate of Destruction** | Third-party attestation that physical media was destroyed according to specified standards |
| **Data Remanence** | Residual data remaining after deletion attempts |

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

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Chief Information Security Officer (CISO)** | [Name] | | [Date] |
| **Data Protection Officer (DPO)** | [Name] | | [Date] |
| **Legal/Compliance Officer** | [Name] | | [Date] |
| **Chief Information Officer (CIO)** | [Name] | | [Date] |
| **Executive Management (GL)** | [Name] | | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for information deletion. Implementation procedures are documented in ISMS-IMP-A.8.10 (UG/TG).1 through A.8.10.5.*

<!-- QA_VERIFIED: 2026-02-02 -->
