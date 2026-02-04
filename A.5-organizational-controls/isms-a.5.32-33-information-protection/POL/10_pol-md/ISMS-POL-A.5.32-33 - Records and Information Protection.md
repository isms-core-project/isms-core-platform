**ISMS-POL-A.5.32-33 — Records and Information Protection**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Records and Information Protection |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.32-33 |
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
- Secondary: Legal Counsel
- Integration: Data Protection Officer (DPO)
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.12-13 (Information Classification and Labelling)
- ISMS-POL-A.5.34 (Privacy and Protection of PII)
- ISMS-POL-A.8.10 (Information Deletion)
- ISMS-POL-A.8.12 (Data Leakage Prevention)
- ISMS-IMP-A.5.32-33 (Implementation Guidance)
- ISO/IEC 27001:2022 Controls A.5.32, A.5.33

---

## Executive Summary

This policy establishes [Organization]'s requirements for protecting intellectual property, proprietary information, and ensuring proper protection of records throughout their lifecycle.

**Scope**: This policy applies to all intellectual property, proprietary information, trade secrets, and records created, processed, stored, or transmitted by [Organization], including both physical and electronic formats.

**Purpose**: Define organisational requirements for intellectual property protection and records management. This policy establishes WHAT protection is required and WHO is responsible. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.32-33.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss CO (Code of Obligations), Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, healthcare regulations) apply where [Organization]'s business activities trigger applicability.

**Combined Control Approach**: Controls A.5.32 (Intellectual Property Rights) and A.5.33 (Protection of Records) are implemented together because they share common governance structures and protection mechanisms.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Controls A.5.32 and A.5.33**

**ISO/IEC 27001:2022 Annex A.5.32 - Intellectual Property Rights**

> *The organisation should implement appropriate procedures to protect intellectual property rights.*

**ISO/IEC 27001:2022 Annex A.5.33 - Protection of Records**

> *Records should be protected from loss, destruction, falsification, unauthorized access and unauthorized release in accordance with legislative, regulatory, contractual and business requirements.*

**Control Objectives**:

- Ensure intellectual property is identified, protected, and legally compliant
- Ensure records are retained, protected, and available for required periods
- Prevent loss, falsification, or unauthorised access to valuable information assets
- Comply with legal and regulatory retention requirements

**Control Type**: Preventive, Detective
**Control Category**: Organisational

**This Policy Addresses**:

- Intellectual property identification and classification
- IP protection controls (technical, administrative, legal)
- Third-party IP compliance
- Records classification and retention requirements
- Records protection and disposal

## What This Policy Does

This policy:

- **Defines** intellectual property categories and protection requirements
- **Establishes** records retention periods and protection controls
- **Specifies** disposal requirements for records and IP materials
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Define personal data protection requirements** (see ISMS-POL-A.5.34)
- **Specify information classification methodology** (see ISMS-POL-A.5.12-13)
- **Detail secure deletion procedures** (see ISMS-POL-A.8.10)
- **Provide DLP technical configurations** (see ISMS-POL-A.8.12)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite technology or process changes
- Flexibility for different records management solutions
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- All intellectual property (patents, copyrights, trademarks, trade secrets, source code)
- All records (business, financial, personnel, technical, operational)
- All formats (physical documents, electronic files, databases, emails)
- All personnel (employees, contractors, third parties with IP or records access)

**Out of Scope**:

- Personal data protection specific requirements (covered by A.5.34)
- Information classification methodology (covered by A.5.12-13)
- Technical deletion procedures (covered by A.8.10)

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss CO Art. 958f** | All Swiss entities | Bookkeeping retention (10 years) |
| **Swiss nDSG** | All personal data processing | Appropriate protection measures |
| **ISO/IEC 27001:2022** | Certification scope | Controls A.5.32, A.5.33 |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Requirements |
|-----------|-------------------|--------------|
| **EU GDPR** | Processing EU/EEA personal data or otherwise within GDPR territorial scope | Retention/disposal must support storage limitation (Art. 5(1)(e)) and erasure requests (Art. 17), subject to overriding legal retention obligations |
| **Swiss Patent Act** | Patent holdings | Protection of patent documentation |
| **Swiss Copyright Act** | Software development | Source code protection |
| **FINMA** | Swiss regulated financial institution | Enhanced record retention (10 years) |
| **Tax authorities** | All entities | Tax record retention (10 years Switzerland) |
| **Healthcare regulations** | Healthcare operations | Medical record retention (20+ years) |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- ISO 15489 (Records Management)
- ARMA International Guidelines
- Open source license compliance frameworks (GPL, Apache, MIT)
- Software Asset Management (SAM) best practices

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent retention requirements apply where multiple regulations overlap.

---

# Policy Statements

## Intellectual Property Protection (A.5.32)

### IP Identification and Classification

[Organisation] SHALL identify and classify all intellectual property:

**IP Categories**:

| Category | Examples | Protection Level |
|----------|----------|------------------|
| **Trade Secrets** | Algorithms, formulas, processes, client lists | Restricted (highest protection) |
| **Proprietary Software** | Source code, development tools, scripts | Confidential minimum |
| **Business Methods** | Unique processes, methodologies | Confidential |
| **Technical Documentation** | Architecture, designs, specifications | Confidential |
| **Trademarks/Branding** | Logos, brand materials | Internal (usage controlled) |

**IP Registry**:

- All significant IP assets SHALL be inventoried in the IP Register
- Each IP asset SHALL have designated owner and custodian
- IP classification SHALL align with ISMS-POL-A.5.12-13 (Information Classification)
- IP Register reviewed annually by Legal Counsel and CISO

**IP Register (ISMS-REG-IP)**: Owner: Legal Counsel; Custodian: CISO (or Records Manager); System of record: [GRC/SharePoint/equivalent]. Minimum fields: IP asset name, category, business owner, custodian, classification, location/system, access group, third-party sharing allowed (Y/N), legal protection status (patent/copyright/trademark/trade secret), review date, exceptions/holds. Review: annual; evidence: dated export + review sign-off.

### IP Protection Controls

[Organisation] SHALL implement protection controls based on IP type:

**Technical Protection**:

| IP Type | Required Controls |
|---------|-------------------|
| **Source Code** | Access control, version control, code review, export restrictions |
| **Trade Secrets** | Need-to-know access, encryption, DLP monitoring |
| **Designs/Specifications** | Access logging, watermarking, sharing restrictions |
| **Research Data** | Encryption, access control, backup protection |

**Administrative Protection**:

- Confidentiality clauses in employment contracts (per ISMS-POL-A.6.1-2 HR Security)
- Non-disclosure agreements for third-party access (per A.6.6)
- IP ownership clauses in vendor contracts (per A.5.20)
- Exit procedures ensuring IP return/deletion (per A.6.5)

**Legal Protection**:

- Patent applications filed where appropriate
- Copyright notices on protected materials
- Trademark registrations maintained
- Trade secret documentation for legal defence

### Third-Party IP Compliance

[Organisation] SHALL comply with third-party intellectual property rights:

**Software Licensing**:

- All software SHALL be properly licensed
- Software Asset Management (SAM) inventory maintained
- License compliance verified quarterly: verification includes full inventory reconciliation against procurement records, identification of exceptions, exception remediation with documented SLA (30 days critical/90 days standard), and management sign-off; evidence stored per ISMS-IMP-A.5.32-33.1
- Unlicensed software use is PROHIBITED

**Third-Party Content**:

- Copyright verification before use
- Proper attribution and licensing
- Open source license compliance (GPL, Apache, MIT, etc.); open-source use must follow the approved OSS review process including SBOM generation, license scanning, and approval gates as defined in ISMS-IMP-A.5.32-33.1 and Secure Development controls
- Creative commons restrictions honoured

## Records Protection (A.5.33)

### Records Classification

[Organisation] SHALL classify records based on retention requirements and protection needs:

**Record Categories**:

| Category | Retention Period | Protection Requirement | Examples |
|----------|-----------------|----------------------|----------|
| **Legal/Contracts** | Duration + 10 years | Confidential, integrity protected | Contracts, legal agreements |
| **Financial** | 10 years (Swiss CO) | Confidential, tamper-evident | Invoices, ledgers, tax records |
| **Personnel** | Employment + 10 years | Confidential, privacy protected | HR files, payroll, evaluations |
| **Regulatory** | Per regulation | Per classification | Audit reports, compliance evidence |
| **Technical** | System lifecycle + 3 years | Internal minimum | Configurations, change records |
| **Operational** | 3-7 years | Internal | Meeting minutes, project files |
| **Security/Audit** | 2-7 years | Confidential, integrity protected | Access logs, incident records |

### Retention Requirements

[Organisation] SHALL implement record retention controls:

**Retention Schedule**:

- Documented retention schedule maintained by Legal Counsel
- Retention periods based on legal, regulatory, contractual, and business requirements
- Retention schedule reviewed annually
- Exceptions require Legal Counsel and CISO approval

**Retention Schedule (ISMS-REG-RET)**: Owner: Legal Counsel; Approved by: Executive Management; System of record: [GRC/SharePoint/equivalent]. Minimum fields: record category, description, systems in scope, retention period, retention basis (law/contract/business), legal hold applicability, disposal method, record owner, last review date. Review: annual; evidence: dated export + approval record.

**Retention Controls**:

| Control | Requirement |
|---------|-------------|
| **Minimum Retention** | Records SHALL NOT be deleted before retention period expires |
| **Maximum Retention** | Records SHOULD be deleted after retention + grace period (GDPR storage limitation) |
| **Legal Hold** | Litigation hold overrides normal deletion (indefinite until released) |
| **Integrity Protection** | Critical records SHALL have integrity verification (checksums, digital signatures) |

**Retention vs Erasure Conflict Resolution**: When a deletion or anonymization request conflicts with legal retention obligations, retention takes precedence. Records under retention are access-restricted, the decision basis is documented (Legal Counsel approval required), and DPO involvement is mandatory for personal data. Decision records are retained in ISMS-REG-EXCEPTIONS.

**Legal Hold Register (ISMS-REG-HOLD)**: Owner: Legal Counsel; System of record: [GRC/SharePoint/equivalent]. Minimum fields: hold ID, matter description, hold scope (systems/records/custodians), start date, release date, Legal Counsel authorisation, evidence of system enforcement (deletion suspended), and release verification. Active holds reviewed monthly; release requires Legal Counsel sign-off.

**Critical Records Definition**: For the purposes of integrity protection requirements, "critical records" include: regulatory and audit evidence, financial ledgers and tax documentation, security and access logs, signed contracts and legal agreements, HR master records, incident investigation records, and any records subject to legal hold.

### Records Protection Controls

[Organisation] SHALL protect records throughout their lifecycle:

**Integrity Protection**:

- Critical records stored with integrity verification
- Audit logs tamper-protected (write-once or cryptographic)
- Version control for records requiring change tracking
- Digital signatures for records requiring authenticity

**Availability Protection**:

- Backup according to criticality (per ISMS-POL-A.8.13)
- Geographic redundancy for critical records
- Media refresh before degradation (migration plan)
- Readable format maintenance (format migration when needed)

**Confidentiality Protection**:

- Access control based on need-to-know
- Encryption for confidential records
- Physical protection for paper records
- Secure disposal per retention schedule

### Records Disposal

[Organisation] SHALL dispose of records securely when retention period expires:

**Disposal Requirements**:

| Record Type | Disposal Method |
|-------------|-----------------|
| **Paper (Confidential+)** | Cross-cut shredding (P-4 minimum) or witnessed incineration |
| **Paper (Internal)** | Standard shredding (P-3 minimum) |
| **Electronic (Confidential+)** | Secure deletion per ISMS-POL-A.8.10 |
| **Electronic (Internal)** | Standard deletion with verification |
| **Media (HDDs, tapes)** | Degaussing, physical destruction, or certified destruction |

**Disposal Documentation**:

- Disposal records maintained for audit trail
- Certificates of destruction for confidential+ records
- Third-party destruction verified (vendor certifications)

---

# Roles and Responsibilities

## Accountability Matrix

| Role | IP and Records Responsibilities |
|------|--------------------------------|
| **Executive Management** | IP strategy approval, record retention policy approval |
| **CISO** | IP protection controls, records security requirements |
| **Legal Counsel** | IP registration, retention schedule, legal compliance |
| **DPO** | Personal data in records, GDPR storage limitation |
| **Records Manager** | Retention schedule maintenance, disposal oversight |
| **Information Owners** | Classification, retention decisions for owned records |
| **IT Operations** | Technical controls, backup, disposal execution |
| **All Personnel** | Handle IP and records per policy, report violations |

## Escalation Path

- IP protection concerns: Employee → Manager → Legal Counsel → CISO
- Records retention questions: Employee → Records Manager → Legal Counsel
- Disposal approval: Records Manager → Information Owner → Legal Counsel (if uncertain)

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| IP Register Review | Annual | Legal Counsel | Updated register, ownership confirmation |
| Software License Audit | Quarterly | IT Operations | SAM report, license reconciliation |
| Retention Schedule Review | Annual | Legal Counsel | Updated schedule, regulatory alignment |
| Records Disposal Audit | Annual | Internal Audit | Disposal records, certificate sampling |
| Records Integrity Check | Annual | IT Operations | Backup verification, integrity test results |

**Governance Metrics**:

- IP assets with designated owners (target: 100%)
- Software license compliance rate (target: 100%)
- Records with assigned retention periods (target: 100%)
- Records disposed per schedule (target: >95%)
- Records integrity check pass rate (target: 100%)

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Regulatory changes, legal requirements, audit findings, business changes
- **Reviewers**: CISO, Legal Counsel, DPO, Records Manager
- **Approval**: Executive Management

## Exception Management

**Permitted Exceptions**:

- Retention extension due to legal hold or documented business requirement
- Early disposal with risk assessment and Legal Counsel approval
- Third-party access to IP with NDA and CISO approval

**Exception Process**:

1. Document business justification
2. Risk assessment of exception impact
3. Legal Counsel review (for retention exceptions)
4. CISO approval (for IP access exceptions)
5. Time-limited approval with review date

**Not Permissible**:

- Disposal of records under legal hold
- IP sharing without confidentiality agreement
- Unlicensed software use

All exceptions SHALL be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

## Corrective Action Linkage

Nonconformities related to this policy (e.g., unlicensed software, premature disposal, IP leakage, missing retention periods) SHALL be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- IP assets included in risk assessment
- Records loss/falsification risks identified and treated
- Risk treatment plans document IP and records protection controls

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Controls A.5.32 and A.5.33 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported

**Related Controls**:

| Control | Relationship |
|---------|--------------|
| **A.5.12-13** | Classification - IP and records classified per scheme |
| **A.5.34** | Privacy - Personal data records subject to privacy requirements |
| **A.6.6** | NDAs - Third-party IP access requires confidentiality agreements |
| **A.8.10** | Deletion - Secure disposal of records |
| **A.8.12** | DLP - Prevention of IP exfiltration |
| **A.8.13** | Backup - Records availability protection |

**Stacked Control Integration**:

A.5.32-33 (IP and Records Protection) stacks with related controls:

| Stacked Control | Integration Point | A.5.32-33 Contribution |
|-----------------|-------------------|------------------------|
| **A.5.12-13** (Classification) | Information handling | A.5.32-33 defines IP/records categories; A.5.12-13 provides classification framework |
| **A.8.10** (Deletion) | Records disposal | A.5.32-33 defines retention periods; A.8.10 defines deletion procedures |
| **A.8.12** (DLP) | IP protection | A.5.32-33 identifies IP to protect; A.8.12 prevents exfiltration |

Assessment of A.5.32-33 should reference stacked control assessments for complete coverage.

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.5.32-33 Suite):

| Document ID | Title | Purpose |
|-------------|-------|---------|
| **ISMS-IMP-A.5.32-33.1** | IP Protection Implementation Guide | IP registration, protection controls, compliance procedures |
| **ISMS-IMP-A.5.32-33.2** | Records Management Implementation Guide | Retention schedule, disposal procedures, integrity controls |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Required Stage 1 evidence includes:

- This policy document (ISMS-POL-A.5.32-33 v1.0)
- Recorded approval by CISO, Legal Counsel, DPO, Executive Management
- Evidence of communication to relevant roles
- IP categories and protection requirements defined (Intellectual Property Protection)
- Records categories and retention periods defined (Records Protection)
- Disposal requirements specified (Records Disposal)
- Roles and responsibilities assigned (Roles and Responsibilities)

Evidence presence and status is tracked in the ISMS Evidence Register.

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- IP Register with ownership and classification
- Software Asset Management reports showing license compliance
- Documented retention schedule with regulatory alignment
- Disposal records and certificates of destruction
- Integrity verification results for critical records
- Legal hold register with active holds
- Third-party IP agreements and NDAs
- Training records for IP and records handling

---

# Definitions

| Term | Definition |
|------|------------|
| **Intellectual Property (IP)** | Creations of the mind: inventions, literary/artistic works, symbols, designs |
| **Trade Secret** | Confidential business information providing competitive advantage |
| **Record** | Information created, received, and maintained as evidence of business activity |
| **Retention Period** | Required duration for keeping a record before disposal |
| **Legal Hold** | Preservation requirement due to litigation or investigation |
| **Software Asset Management (SAM)** | Processes for managing software licenses and usage |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Legal Counsel** | [Name] | [Date to be set] |
| **Data Protection Officer (DPO)** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for intellectual property and records protection. Implementation procedures are documented in ISMS-IMP-A.5.32-33.*

<!-- QA_VERIFIED: 2026-02-04 -->
