**ISMS-POL-A.5.34 - Privacy and Protection of PII**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Privacy and Protection of Personally Identifiable Information (PII) |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.34 |
| **Document Creator** | Chief Information Security Officer (CISO) / Data Protection Officer (DPO) |
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
| 1.0 | [Date] | CISO/DPO | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Data Protection Officer (DPO) / Privacy Officer
- Secondary: Chief Information Security Officer (CISO)
- Legal Review: Legal/Compliance Officer (mandatory)
- HR Integration: Chief Human Resources Officer (CHRO) - employee PII aspects
- Final Authority: Executive Management (GL)


**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-CTX-A.5.34 (Privacy Regulatory Landscape Reference)
- ISMS-IMP-A.5.34 (Implementation Guidance Suite)
- ISMS-POL-A.5.9 (Inventory of Information and Assets)
- ISMS-POL-A.5.12 (Classification of Information)
- ISMS-POL-A.5.15-16-18 (Identity and Access Management)
- ISMS-POL-A.5.33 (Protection of Records)
- ISMS-POL-A.8.10 (Information Deletion)
- ISMS-POL-A.8.11 (Data Masking)
- ISMS-POL-A.8.12 (Data Leakage Prevention)
- ISO/IEC 27001:2022 Control A.5.34
- ISO/IEC 27701:2019 (Privacy Information Management System - if implemented)


---

## Executive Summary

This policy establishes [Organization]'s requirements for privacy and protection of personally identifiable information (PII) in accordance with ISO/IEC 27001:2022 Control A.5.34.

**Purpose**: Define WHAT privacy requirements must be met and WHO is accountable for privacy compliance. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.34.

**Scope**: All processing of personal data / PII by [Organization], including data relating to customers, employees, contractors, vendors, and other natural persons, regardless of format or location.

**Regulatory Alignment**: Addresses mandatory compliance requirements per ISMS-POL-00, including Swiss nDSG/FADP, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements apply where business activities trigger applicability.

---

# Control Alignment and Scope

## ISO/IEC 27001:2022 Control A.5.34

**ISO/IEC 27001:2022 Annex A.5.34 - Privacy and Protection of PII**

> *The organization should identify and meet requirements regarding the preservation of privacy and protection of PII in accordance with applicable laws and regulations and contractual requirements.*

**Control Objective**: Ensure [Organization] identifies all applicable privacy requirements and implements appropriate measures to protect PII throughout its lifecycle, respecting data subject rights and meeting regulatory obligations.

**Control Type**: Organizational Control (People Controls - Section 5)

**Information Security Properties**:

- **Confidentiality** - PII protected from unauthorized disclosure
- **Integrity** - PII accuracy maintained, unauthorized modification prevented
- **Availability** - Data subject rights fulfilled within regulatory timeframes


## Policy Scope

**This Policy Establishes**:

- Privacy governance requirements and accountability structure
- PII classification framework aligned with regulatory definitions
- Legal basis requirements for processing personal data
- Data subject rights requirements and response obligations
- Privacy by Design and by Default requirements
- Data Protection Impact Assessment (DPIA) triggers
- Cross-border data transfer requirements
- Data breach notification obligations
- Record of Processing Activities (ROPA) requirements


**This Policy Does NOT Provide**:

- Detailed DSR handling procedures (see ISMS-IMP-A.5.34.3)
- DPIA methodologies or templates (see ISMS-IMP-A.5.34.5)
- Technical PII protection configurations (see ISMS-POL-A.8.11, A.8.24)
- Data retention schedules (see ISMS-POL-A.5.33)


**Geographical Scope**: All [Organization] operations, regardless of location. Specific regulatory requirements triggered based on location of data subjects, processing activities, and data infrastructure.

**Data Scope**: All PII processed by [Organization], including:

- Customers, clients, and prospects
- Employees and contractors
- Vendors and suppliers
- Job applicants
- Website visitors
- Other natural persons whose data [Organization] processes


**Exclusions**: Anonymized data (genuinely anonymized per GDPR Recital 26), deceased persons where regulation excludes them.

---

# Regulatory Framework

## Tier 1: Mandatory Compliance

**Swiss Federal Act on Data Protection (FADP / nDSG)**

[Organization] SHALL comply with FADP requirements including:

- Article 6: Principles of data processing (lawfulness, good faith, proportionality, purpose limitation, data minimization)
- Article 8: Data security requirements
- Articles 19-24: Duty to provide information when collecting personal data
- Articles 25-32: Data subject rights
- Article 24: Data breach notification to FDPIC
- Articles 16-17: Cross-border data disclosure requirements


**Enforcement**: Swiss Federal Data Protection and Information Commissioner (FDPIC)

---

**EU General Data Protection Regulation (GDPR)**

[Organization] SHALL comply with GDPR requirements including:

- Article 5: Principles of processing
- Article 6: Legal bases for processing
- Articles 7-8: Conditions for consent
- Article 9: Special category data processing restrictions
- Articles 12-22: Data subject rights
- Articles 24-25: Controller responsibilities (accountability, Privacy by Design)
- Article 28: Processor obligations
- Article 30: Records of processing activities
- Article 32: Security of processing
- Articles 33-34: Breach notification (72 hours to supervisory authority)
- Article 35: Data Protection Impact Assessment
- Articles 37-39: DPO requirements
- Articles 44-49: International data transfers


**Penalties**: Up to EUR 20 million or 4% of annual global turnover

---

**ISO/IEC 27001:2022**

[Organization] maintains ISO 27001:2022 certification with Control A.5.34 implemented per this policy.

## Tier 2: Conditional Applicability

The following regulations apply based on specific business activities, assessed per ISMS-POL-00:

- **FINMA Circulars**: If [Organization] is a FINMA-regulated entity
- **DORA (Digital Operational Resilience Act)**: If [Organization] is an EU financial entity or designated critical ICT third-party service provider. Article 28 ICT third-party risk assessment of data processing arrangements satisfies GDPR Article 28 processor obligations when both apply
- **NIS2 Directive**: If [Organization] is designated as essential or important entity. Article 21(2) risk management measures (including human resources security, access control) involve PII processing. GDPR/nDSG compliance satisfies NIS2 PII protection requirements. NIS2-specific incident reporting (Art. 23) integrates with ISMS-POL-A.5.24-28 without creating additional privacy requirements
- **PCI DSS**: If [Organization] processes payment cardholder data. Cardholder data is PII subject to both GDPR/nDSG and PCI DSS. Where requirements conflict, [Organization] applies the stricter requirement. PCI DSS compliance does not automatically satisfy GDPR - separate legal basis and data subject rights mechanisms required
- **Health Data Regulations**: Based on products, services, and processing activities. If processing health data (GDPR Art. 9 special category), additional sectoral requirements may apply. Health data processing requires documented legal basis per ISMS-IMP-A.5.34.2 and enhanced security measures per ISMS-POL-A.8.24

**Applicability Determination**: Legal/Compliance Officer and DPO jointly determine Tier 2 applicability annually. Applicability decisions documented in ISMS-POL-00 Regulatory Applicability Matrix. Material business changes (new markets, data categories, regulated clients) trigger immediate reassessment.

## Tier 3: Best Practice Reference

The following frameworks inform practices but are not mandatory unless contractually required:

- ISO/IEC 27701:2019 (Privacy Information Management System)
- ISO/IEC 29100:2011 (Privacy Framework)
- NIST Privacy Framework
- ISO/IEC 27002:2022 (Implementation guidance)


---

# Privacy Policy Statements

## PII Classification

[Organization] SHALL classify PII into the following categories:

**Category 1: Basic PII** - Standard personal data requiring baseline protection measures (identification data, contact information, financial data, professional data, electronic identifiers, behavioral data, communications data).

**Category 2: Sensitive PII** - Special category data requiring enhanced protection (GDPR Article 9: racial/ethnic origin, political opinions, religious beliefs, trade union membership, genetic data, biometric data, health data, sex life/sexual orientation; FADP Article 5(c): similar categories plus administrative/criminal proceedings data).

**Category 3: Criminal Offense Data** - Data relating to criminal convictions, offenses, or security measures requiring specific legal authorization.

## PII Discovery and Data Mapping

[Organization] SHALL:

- Conduct PII discovery through automated and manual methods
- Perform comprehensive discovery annually and for new systems before deployment
- Maintain data mapping documenting data sources, purposes, legal basis, storage locations, sharing recipients, transfers, and retention
- Create and maintain visual data flow diagrams for PII movement


## Record of Processing Activities (ROPA)

[Organization] SHALL maintain a ROPA documenting all personal data processing operations per GDPR Article 30 and FADP requirements.

**ROPA SHALL include**: Controller/processor details, processing purposes, data subject categories, personal data categories, recipients, international transfers, retention periods, security measures description.

**ROPA SHALL be**: Reviewed quarterly, updated upon material changes, validated annually by Legal and CISO.

## Legal Basis for Processing

[Organization] SHALL:

- Determine and document a valid legal basis for each processing activity before processing begins
- Process personal data only under one of the following GDPR Article 6 bases: consent, contract performance, legal obligation, vital interests, public task, or legitimate interests
- Document legal basis justification and supporting evidence in ROPA
- For special category data, document both Article 6 legal basis AND Article 9(2) specific condition


## Consent Management

When consent is the legal basis, [Organization] SHALL ensure consent is:

- Freely given, specific, informed, and unambiguous
- Obtained through clear affirmative action
- Withdrawable at any time with withdrawal as easy as giving consent
- Documented with records of who, when, what, and how


## Legitimate Interest Assessments

When legitimate interests is the legal basis, [Organization] SHALL:

- Conduct and document a Legitimate Interest Assessment (LIA) before processing using standardized template in ISMS-IMP-A.5.34.2
- Apply the three-part test: purpose test (is there a legitimate purpose?), necessity test (are less intrusive alternatives available?), and balancing test (organization interests vs. data subject rights, considering expectations, relationship, and data sensitivity)
- Obtain Legal/DPO approval before processing begins
- Review LIAs annually or when processing changes materially


## Data Subject Rights

[Organization] SHALL enable data subjects to exercise their rights under GDPR and FADP:

| Right | Requirement |
|-------|-------------|
| **Access** | Provide confirmation of processing and copy of personal data within regulatory timeframes |
| **Rectification** | Correct inaccurate data and complete incomplete data |
| **Erasure** | Delete personal data when erasure grounds exist and no exceptions apply |
| **Data Portability** | Provide data in structured, machine-readable format when applicable |
| **Object** | Cease processing upon objection unless compelling grounds exist; absolute right for marketing |
| **Restriction** | Restrict processing when grounds exist |

**Response Timeframes**: [Organization] SHALL respond to data subject requests within **1 month of receipt** (GDPR Art. 12(3), FADP Art. 25(4)).

**DSR Deadline Extensions**: If request complexity or volume requires extension, [Organization] SHALL:

1. Notify data subject within initial 1-month period of reason for delay and expected completion date (maximum 3 months total per GDPR Art. 12(3))
2. Document justification in DSR tracking system
3. Obtain DPO approval for extension

Systematic DSR delays SHALL be investigated as potential process failure and reported to Privacy Steering Committee.

**DSR Evidence**: DSR tracking system records request receipt date, response date, completion status, and extension justifications. Monthly DSR metrics reported to DPO for trend analysis.

## Privacy by Design and by Default

[Organization] SHALL:

- Implement data protection principles throughout system development and processing design
- Consider state of the art, implementation costs, processing nature, and risks to data subjects
- Configure systems with privacy-protective defaults (data minimization, limited processing scope, limited retention, limited accessibility)
- Provide users with accessible privacy controls


## Data Protection Impact Assessments

[Organization] SHALL conduct DPIAs before processing when:

- Processing is likely to result in high risk to data subject rights and freedoms
- Processing involves systematic/extensive automated evaluation with legal effects
- Processing involves large-scale special category or criminal offense data
- Processing involves systematic monitoring of publicly accessible areas


DPIA SHALL include: Systematic description of processing, assessment of necessity and proportionality, assessment of risks to data subjects, and measures to address risks.

DPO SHALL be consulted on all DPIAs. Supervisory authority consultation required if high risk cannot be mitigated.

## Cross-Border Data Transfers

[Organization] SHALL NOT transfer personal data to third countries unless:

- Adequacy decision exists (European Commission or Swiss Federal Council)
- Appropriate safeguards are in place (Standard Contractual Clauses, Binding Corporate Rules, approved codes/certifications)
- Specific derogation applies (explicit consent, contract necessity, legal claims, vital interests)


Transfer impact assessments SHALL be conducted for transfers not based on adequacy decisions.

## Data Breach Notification

[Organization] SHALL:

- Notify supervisory authority without undue delay (GDPR: within 72 hours, FADP: as quickly as possible) of breaches likely to result in risk to data subjects
- Communicate breach to data subjects without undue delay when breach is likely to result in high risk
- Document all breaches including facts, effects, and remedial actions
- Maintain a breach register


## Technical and Organizational Measures

[Organization] SHALL implement appropriate security measures taking into account state of the art, implementation costs, processing nature, and risks, including:

- Pseudonymization and encryption of personal data
- Measures to ensure ongoing confidentiality, integrity, availability, and resilience
- Process for regularly testing and evaluating control effectiveness
- Ability to restore data availability after incidents


Enhanced measures SHALL be implemented for special category data, criminal offense data, and children's data.

---

# Roles and Responsibilities

## Data Protection Officer (DPO) / Privacy Officer

**Accountability**: Independent privacy governance function

**Responsibilities**:

- Inform and advise on GDPR/FADP obligations
- Monitor privacy compliance
- Provide advice on DPIAs
- Cooperate with supervisory authorities
- Serve as contact point for authorities and data subjects
- Maintain ROPA with input from business units


**Reporting**: Reports directly to highest management level without instructions regarding duties.

**DPO Independence Safeguards**:

1. DPO does not perform tasks resulting in conflict of interest (annual self-assessment reviewed by Executive Management)
2. DPO reports directly to CEO, not to CISO or operational management
3. DPO has autonomous budget for external counsel and privacy tools
4. DPO termination or significant responsibility changes require Executive Management approval with documented justification
5. DPO independence reviewed annually during ISO 27001 internal audits

## Chief Executive Officer (CEO) / Executive Management

**Accountability**: Overall accountability for privacy compliance

**Responsibilities**:

- Approve privacy policy and significant changes
- Allocate resources for privacy program
- Review privacy metrics and breach reports
- Ensure organizational commitment to privacy


## Chief Information Security Officer (CISO)

**Accountability**: Technical security controls for PII protection

**Responsibilities**:

- Implement technical security controls
- Conduct security risk assessments for processing activities
- Provide technical input to DPIAs
- Lead data breach response (technical containment)
- Oversee access controls and encryption for PII


## Legal / Compliance Officer

**Accountability**: Legal interpretation and regulatory assessment

**Responsibilities**:

- Provide legal interpretation of privacy regulations
- Review processor agreements and transfer mechanisms
- Assess regulatory applicability per ISMS-POL-00
- Support DPO in regulatory interactions


## Data Owners

**Accountability**: Business unit accountability for specific data domains

**Responsibilities**:

- Define purpose and legal basis for processing
- Classify data according to sensitivity
- Determine retention requirements
- Authorize access to data
- Ensure policy compliance for their data domain


## Human Resources (HR)

**Accountability**: Employee PII processing

**Responsibilities**:

- Ensure lawful basis for employee data processing
- Provide employee privacy notices
- Manage employee DSR requests
- Coordinate with employee representatives on privacy matters
- Manage employee privacy training


## All Personnel

**Universal Responsibilities**:

- Comply with this policy and privacy procedures
- Complete mandatory privacy training
- Handle personal data only for authorized purposes
- Report suspected data breaches or privacy violations immediately
- Maintain confidentiality of personal data


---

# Governance and Review

## Privacy Governance Structure

**Privacy Steering Committee**: Cross-functional committee (DPO, CISO, Legal, HR, IT, Business Representatives) meeting quarterly to review privacy metrics, DSR volume, breach incidents, and program effectiveness.

**Governance Activities**:

- **Quarterly**: Privacy Steering Committee meetings, metrics review
- **Annual**: Privacy program review, policy updates, ROPA validation, training assessment
- **Ad Hoc**: DPIA reviews, processor assessments, incident response


## Privacy Metrics

[Organization] SHALL track and report:

- Data subject rights requests (volume, type, response time, completion rate)
- Data breaches (number, severity, notification compliance)
- DPIAs (number completed, findings, mitigation status)
- Training compliance (completion rates)
- Processor compliance (contract coverage, assessment completion)

**Privacy Metrics Dashboard**: Privacy metrics integrated into [Organization] ISMS dashboard (see ISMS-POL-A.9.1 Monitoring), providing real-time visibility to DPO and quarterly rollup reports to Privacy Steering Committee. Metrics tracked via:

- DSR tracking system (request volume, type, response time, completion rate)
- Breach register (incident count, severity classification, notification compliance)
- DPIA tracking database (number completed, high-risk findings, mitigation status)
- Training LMS (completion rates by role, assessment scores)

Dashboard reviewed monthly by DPO for trend analysis and early warning of compliance issues.

**Escalation**: High-risk breaches, supervisory authority inquiries, and systemic non-compliance escalated immediately to Executive Management.

## Policy Review

**Review Cycle**: Annual minimum

**Review Triggers**: Regulatory changes, significant processing changes, breaches revealing gaps, supervisory authority guidance, audit findings, technological changes.

**Approval**: Policy changes approved by Legal/DPO and Executive Management.

## Training Requirements

[Organization] SHALL provide:

- **All Employees**: Annual general privacy awareness training
- **PII Handlers**: Role-specific training on DSR handling, consent, data minimization
- **Special Category Data Handlers**: Enhanced training on legal basis and security
- **New Hires**: Privacy training within 30 days of hire
- **Developers/System Owners**: Privacy by Design training

**Training Effectiveness**: Privacy training requirements integrate with ISMS-POL-A.7.2 (Competence) framework. Training effectiveness measured via:

1. Post-training assessments (minimum 80% pass rate required)
2. Role-specific competence verification (e.g., DSR handlers demonstrate procedure knowledge before authorization)
3. Annual simulations for breach response team

Training records maintained per A.7.2 requirements and reviewed during Privacy Steering Committee meetings.


## Audits and Assessments

**Internal Audits**: Annual minimum, covering policy compliance, GDPR/FADP requirements, control effectiveness.

**External Audits**: ISO 27001:2022 certification audits, ISO 27701 audits (if pursued), regulatory inspections.

**Assessment Framework**: ISMS-IMP-A.5.34 assessment workbook suite.

---

# Documentation Requirements

[Organization] SHALL maintain documented information including:

- This Policy (ISMS-POL-A.5.34)
- Implementation Procedures (ISMS-IMP-A.5.34 suite)
- Record of Processing Activities (ROPA)
- Data Protection Impact Assessments
- Legitimate Interest Assessments
- Processor Agreements (GDPR Art. 28 contracts)
- Standard Contractual Clauses and Transfer Impact Assessments
- Consent Records
- Data Subject Rights Request Records
- Data Breach Register
- Privacy Training Records
- Privacy Audit Reports
- Privacy Notices


**Retention**: Privacy documentation retained for duration of processing plus applicable statutory retention period (minimum 3 years after cessation).

## Evidence and Verification Framework

**Evidence Generation**: ISMS-IMP-A.5.34 suite generates the following evidence artifacts:

| Evidence Type | Source | Verification |
|---------------|--------|--------------|
| ROPA | ISMS-IMP-A.5.34.1; maintained in [GRC Platform/Tool] | Quarterly update by DPO; annual validation by Legal and CISO |
| DSR Records | DSR tracking system; ISMS-IMP-A.5.34.3 | Monthly metrics review by DPO |
| Legal Basis Documentation | ISMS-IMP-A.5.34.2 | Audit sampling annually |
| DPIA Records | ISMS-IMP-A.5.34.5 | DPO review and approval per DPIA |
| Transfer Impact Assessments | ISMS-IMP-A.5.34.6 | Legal review before transfer |
| Breach Register | CISO with ISMS-IMP-A.5.34.4 | Quarterly review by Privacy Steering Committee |
| Consent Records | Consent management system | Annual audit sampling |
| Processor Agreements | Legal department | Annual contract review |

**Evidence Verification**: DPO responsible for ensuring evidence mechanisms are operational and auditable. Quarterly evidence sampling conducted as part of Privacy Steering Committee review.

---

# Integration with Other Controls

This policy integrates with:

| Control | Integration |
|---------|-------------|
| A.5.9 (Asset Inventory) | PII assets identified and cross-referenced with ROPA |
| A.5.12 (Classification) | Classification scheme includes PII categories |
| A.5.15-16-18 (IAM) | Access controls enforce least privilege for PII |
| A.5.19-23 (Supplier Relationships) | Processor agreements required for vendors processing PII |
| A.5.24-28 (Incident Management) | Data breaches involving PII trigger both privacy-specific notification requirements (GDPR Art. 33-34, nDSG Art. 24) and general incident response procedures. Incident classification includes privacy impact assessment (PII volume, sensitivity, affected data subjects). CISO leads technical containment; DPO determines supervisory authority and data subject notification requirements per ISMS-IMP-A.5.34.4. Breach register maintained by CISO with quarterly review by Privacy Steering Committee |
| A.5.33 (Records) | Retention schedules comply with data minimization |
| A.6.3 (Training) | Privacy training mandatory for all employees |
| A.8.10 (Deletion) | Secure deletion implements right to erasure |
| A.8.11 (Masking) | Pseudonymization protects PII |
| A.8.12 (DLP) | DLP detects unauthorized PII disclosure |
| A.8.24 (Cryptography) | Encryption mandatory for sensitive PII |

---

# Compliance and Exceptions

## Compliance

All personnel are required to comply with this policy. Non-compliance may result in disciplinary action up to and including termination.

## Exceptions

Exceptions to this policy require:

- Written request with business justification and risk assessment
- DPO review and recommendation
- Legal review for regulatory implications
- Executive Management approval
- Documented compensating controls
- Time-limited duration with review date


Exceptions SHALL NOT be granted for mandatory regulatory requirements (GDPR, FADP).

## Enforcement

Suspected violations SHALL be reported to DPO and investigated. Privacy violations involving PII may also trigger data breach notification requirements.

---

# Related Documents

| Document ID | Document Title |
|-------------|---------------|
| ISMS-POL-00 | Regulatory Applicability Framework |
| ISMS-CTX-A.5.34 | Privacy Regulatory Landscape Reference |
| ISMS-IMP-A.5.34.1 | PII Identification and Classification Assessment |
| ISMS-IMP-A.5.34.2 | Legal Basis and Lawful Processing Assessment |
| ISMS-IMP-A.5.34.3 | Data Subject Rights Management |
| ISMS-IMP-A.5.34.4 | Technical and Organizational Measures Assessment |
| ISMS-IMP-A.5.34.5 | Data Protection Impact Assessment |
| ISMS-IMP-A.5.34.6 | Cross-Border Transfer Assessment |
| ISMS-POL-A.5.33 | Protection of Records |
| ISMS-POL-A.8.10 | Information Deletion |
| ISMS-POL-A.8.11 | Data Masking |
| ISMS-POL-A.8.12 | Data Leakage Prevention |
| ISMS-POL-A.8.24 | Use of Cryptography |

---

# Approval Record

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Data Protection Officer | [Name] | | |
| Chief Information Security Officer | [Name] | | |
| Legal/Compliance Officer | [Name] | | |
| Chief Executive Officer | [Name] | | |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for privacy and protection of personally identifiable information. Implementation procedures are documented in ISMS-IMP-A.5.34.1 through A.5.34.6.*

<!-- QA_VERIFIED: 2026-02-02 -->
