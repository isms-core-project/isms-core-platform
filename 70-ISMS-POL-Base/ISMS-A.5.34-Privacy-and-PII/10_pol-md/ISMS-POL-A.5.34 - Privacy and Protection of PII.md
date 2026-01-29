# ISMS-POL-A.5.34 - Privacy and Protection of PII

---

## Document Control

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
| 1.0 | [Date] | CISO/DPO | Initial policy for ISO 27001:2022 certification - Privacy and PII protection requirements |

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
- ISMS-IMP-A.5.34 (Implementation Guidance Suite - 7 documents)
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

This policy establishes [Organization]'s requirements for privacy and protection of personally identifiable information (PII) to ensure compliance with applicable privacy laws, regulations, and contractual obligations in accordance with ISO/IEC 27001:2022 Control A.5.34.

**Scope**: This policy applies to all processing of personal data / personally identifiable information (PII) by [Organization], including data relating to customers, employees, contractors, vendors, and any other natural persons (data subjects). It covers all processing activities regardless of format (electronic, paper, verbal), location (on-premises, cloud, third-party), or technology used.

**Purpose**: Define organizational requirements for privacy governance and PII protection throughout the complete data lifecycle. This policy establishes WHAT privacy requirements must be met and WHO is accountable for privacy compliance. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.34.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS, FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control A.5.34

**ISO/IEC 27001:2022 Annex A.5.34 - Privacy and Protection of PII**

> *The organization should identify and meet requirements regarding the preservation of privacy and protection of PII in accordance with applicable laws and regulations and contractual requirements.*

**Control Objective**: Ensure [Organization] identifies all applicable privacy requirements (legal, regulatory, contractual) and implements appropriate measures to protect personally identifiable information throughout its lifecycle, respecting data subject rights and meeting regulatory obligations.

**This Policy Addresses**:
- Identification of applicable privacy laws and regulations
- PII classification and discovery framework
- Legal basis requirements for processing personal data
- Data subject rights framework
- Privacy by Design and by Default requirements
- Technical and Organizational Measures (TOMs) for PII protection
- Data Protection Impact Assessment (DPIA) requirements
- Cross-border data transfer governance
- Data breach notification obligations
- Record of Processing Activities (ROPA) requirements
- Privacy governance roles and responsibilities
- Accountability and compliance demonstration

**Control Type**: Organizational Control (People Controls - Section 5)

**Information Security Properties**: 
- **Confidentiality** - PII protected from unauthorized disclosure
- **Integrity** - PII accuracy maintained, unauthorized modification prevented
- **Availability** - Data subject rights fulfilled within regulatory timeframes

### 1.2 What This Policy Does

This policy:
- **Defines** [Organization]'s privacy requirements based on GDPR, FADP, and ISO 27001:2022
- **Establishes** PII classification framework aligned with regulatory definitions
- **Specifies** data subject rights requirements and response obligations
- **Assigns** accountability for privacy compliance (DPO, Data Controllers, Processors)
- **References** applicable regulatory requirements per ISMS-POL-00
- **Integrates** privacy requirements with information security controls
- **Provides** framework for Privacy by Design and by Default
- **Defines** DPIA requirements and triggers
- **Establishes** cross-border data transfer requirements
- **Specifies** data breach notification obligations

### 1.3 What This Policy Does NOT Do

This policy does NOT:
- **Provide detailed DSR handling procedures** (see ISMS-IMP-A.5.34.3 Data Subject Rights Management)
- **Specify DPIA methodologies or templates** (see ISMS-IMP-A.5.34.5 DPIA Assessment)
- **Define technical PII protection configurations** (see ISMS-POL-A.8.11 Data Masking, A.8.24 Cryptography)
- **Replace legal advice** (legal interpretation requires qualified counsel)
- **Define data retention schedules** (see ISMS-POL-A.5.33 Protection of Records)
- **Specify DLP technical configurations** (see ISMS-POL-A.8.12 Data Leakage Prevention)
- **Mandate consent management platform selection** (technology selection based on risk assessment)
- **Provide country-by-country adequacy assessments** (see ISMS-CTX-A.5.34 Privacy Regulatory Landscape)
- **Replace risk assessment** (privacy controls selected based on risk treatment decisions)

**Rationale**: Separating policy requirements from implementation procedures enables:
- Policy stability despite evolving privacy technologies and regulatory interpretations
- Technical agility for privacy-enhancing technology adoption
- Clear distinction between governance (policy) and execution (implementation)
- Focused audit scope (auditors verify policy compliance, not tool configurations)
- Flexibility for organizations to adapt to their specific context

### 1.4 Scope

**Geographical Scope**: This policy applies to all [Organization] operations, regardless of location. Specific regulatory requirements (GDPR, FADP) are triggered based on:
- Location of data subjects (GDPR: EU residents, FADP: persons in Switzerland)
- Location of [Organization] processing activities
- Location of data storage and processing infrastructure

**Data Scope**: This policy applies to all personally identifiable information (PII) / personal data processed by [Organization], including:

**Data Subject Categories**:
- **Customers / Clients**: Contact information, transaction history, preferences, financial data, communications
- **Employees**: HR records, payroll, performance data, communications, access logs
- **Contractors / Temporary Workers**: Contract details, deliverables, access credentials, communications
- **Vendors / Suppliers**: Contact persons, business relationship data, contract information
- **Job Applicants**: Application materials, interview notes, assessment results
- **Website Visitors**: IP addresses, cookies, analytics data, form submissions
- **Other Natural Persons**: Any other individuals whose data [Organization] processes

**Processing Activities Scope**:
- Collection, recording, storage, retrieval, consultation, use
- Disclosure by transmission, dissemination, or making available
- Alignment, combination, restriction, erasure, or destruction
- Automated and non-automated processing (including paper records)

**System Scope**:
- All information systems that process, store, or transmit PII (CRM, HR systems, email, collaboration tools, databases)
- Cloud services and SaaS platforms processing PII on behalf of [Organization]
- Third-party processors handling PII under contract
- Development, test, and production environments containing PII

**Exclusions from Scope**:
- **Anonymized Data**: Data that cannot be re-identified is outside privacy regulation scope (but must be genuinely anonymized per GDPR Recital 26)
- **Corporate Contact Information**: Business contact details of employees in their professional capacity may have reduced protection under some regulations
- **Deceased Persons**: Some regulations exclude deceased persons (verify specific requirements per jurisdiction)

**Note on Pseudonymization**: Pseudonymized data (where identification requires additional information kept separately) remains personal data under GDPR/FADP and is within scope of this policy.

### 1.5 Regulatory Applicability Framework

[Organization] complies with privacy requirements defined in ISMS-POL-00 (Regulatory Applicability Framework). The following regulatory structure applies to this control:

#### Tier 1: Mandatory Compliance (Active)

**Swiss Federal Act on Data Protection (FADP / nDSG)**:

**Applicability**: [Organization] is subject to Swiss data protection law.

**Key Requirements**:
- Article 6: Principles of data processing (lawfulness, good faith, proportionality, purpose limitation, data minimization)
- Article 8: Data security requirements
- Article 19-24: Duty to provide information when collecting personal data
- Article 25-32: Data subject rights (access, rectification, erasure, data portability, objection)
- Article 24: Data breach notification to FDPIC (Federal Data Protection and Information Commissioner)
- Article 16-17: Cross-border data disclosure requirements

**Special Categories** (Article 5(c)): 
- Religious, philosophical, political, trade union views
- Health, private sphere, racial/ethnic affiliation
- Genetic data, biometric data for unique identification
- Administrative/criminal proceedings data
- Social assistance data

**Enforcement**: Swiss Federal Data Protection and Information Commissioner (FDPIC)

**Reference**: SR 235.1, effective 01.09.2023

---

**EU General Data Protection Regulation (GDPR)**:

**Applicability**: [Organization] processes personal data of EU residents.

**Key Requirements**:
- Article 5: Principles of processing (lawfulness, fairness, transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity/confidentiality, accountability)
- Article 6: Legal bases for processing (consent, contract, legal obligation, vital interests, public task, legitimate interests)
- Article 7-8: Conditions for consent
- Article 9: Special category data processing restrictions
- Article 12-22: Data subject rights (access, rectification, erasure, restriction, data portability, objection, automated decision-making)
- Article 24-25: Controller responsibilities (accountability, data protection by design and default)
- Article 28: Processor obligations
- Article 30: Records of processing activities (ROPA)
- Article 32: Security of processing
- Article 33-34: Breach notification (72 hours to supervisory authority)
- Article 35: Data Protection Impact Assessment (DPIA)
- Article 37-39: Data Protection Officer (DPO) requirements
- Article 44-49: International data transfers

**Special Category Data** (Article 9):
- Racial or ethnic origin
- Political opinions
- Religious or philosophical beliefs
- Trade union membership
- Genetic data, biometric data for unique identification
- Health data
- Sex life or sexual orientation data

**Enforcement**: EU Data Protection Authorities (DPAs), European Data Protection Board (EDPB)

**Penalties**: Up to €20 million or 4% of annual global turnover (whichever is higher)

**Reference**: Regulation (EU) 2016/679, effective 25.05.2018

---

**ISO/IEC 27001:2022**:

**Applicability**: [Organization] is pursuing/maintaining ISO 27001:2022 certification.

**Key Requirements**:
- Control A.5.34: Privacy and protection of PII (this policy)
- Integration with ISMS risk assessment and treatment
- Privacy controls included in Statement of Applicability (SoA)
- Documented information requirements

**This Policy Supports SoA Entry**:

| Control | Status | Justification | Implementation |
|---------|--------|---------------|----------------|
| **A.5.34 - Privacy and Protection of PII** | ☑ Applicable | [Organization] processes personal data subject to GDPR and FADP | This policy + ISMS-IMP-A.5.34 suite |

**Reference**: ISO/IEC 27001:2022 Annex A

---

#### Tier 2: Conditional Applicability (Under Monitoring)

The following regulations may apply to [Organization] based on specific business activities, industry sector, or contractual obligations. Applicability is assessed per ISMS-POL-00 and reviewed annually:

**FINMA Circulars (Swiss Financial Market Supervisory Authority)**:

**Applicability Determination**: Applies if [Organization] is a FINMA-regulated entity (bank, securities dealer, insurance company, financial infrastructure provider).

**Relevant Requirements**: Data protection requirements for outsourced services, data processing by third parties, data residency requirements.

**Current Status**: [To be determined per ISMS-POL-00 assessment]

---

**DORA (Digital Operational Resilience Act)**:

**Applicability Determination**: Applies if [Organization] is an EU financial entity or designated ICT third-party service provider to financial entities.

**Relevant Requirements**: ICT risk management framework (includes data protection aspects), third-party service provider risk management.

**Current Status**: [To be determined per ISMS-POL-00 assessment]

---

**NIS2 (Network and Information Security Directive)**:

**Applicability Determination**: Applies if [Organization] is designated as essential or important entity in EU member states.

**Relevant Requirements**: Cybersecurity risk management measures (includes data protection), reporting obligations (may include data breaches).

**Current Status**: [To be determined per ISMS-POL-00 assessment]

---

**Health Data Regulations (Where Applicable)**:

**Examples**: HIPAA (US), Swiss Medical Device Regulations, EU Medical Device Regulation (MDR)

**Applicability**: Determined based on [Organization]'s products, services, and data processing activities.

**Current Status**: [To be determined per ISMS-POL-00 assessment]

---

**PCI DSS (Payment Card Industry Data Security Standard)**:

**Applicability Determination**: Applies if [Organization] stores, processes, or transmits payment cardholder data.

**Privacy-Relevant Requirements**: Protect stored cardholder data (encryption, masking, retention/disposal), restrict physical access to cardholder data.

**Current Status**: [To be determined per ISMS-POL-00 assessment]

---

**Compliance Determination**: Legal/Compliance Officer and DPO jointly determine applicability of Tier 2 regulations based on [Organization]'s business activities. Assessment documented in ISMS-POL-00 and reviewed annually.

---

#### Tier 3: Informational Reference / Best Practice Alignment

The following frameworks inform [Organization]'s privacy practices but do not constitute mandatory compliance unless contractually required:

**ISO/IEC 27701:2019** (Privacy Information Management System): Extension to ISO/IEC 27001 for privacy management, additional controls for PII controllers and processors, GDPR mapping provided in standard.

**ISO/IEC 29100:2011** (Privacy Framework): Privacy principles and terminology, informational reference for privacy program design.

**NIST Privacy Framework**: US-focused privacy risk management framework, voluntary framework for privacy program structure.

**OECD Privacy Principles**: International privacy guidelines, historical foundation for many national privacy laws.

**ISO/IEC 27002:2022**: Detailed guidance for Control A.5.34 implementation, technical and organizational measure recommendations.

**United States Federal Requirements**: References to US federal frameworks (FISMA, FedRAMP privacy requirements) apply only where [Organization] has explicit US federal contractual obligations, as defined in ISMS-POL-00.

---

## 2. Privacy and PII Protection Requirements

### 2.1 PII Classification and Identification

[Organization] SHALL implement systematic PII identification and classification to enable appropriate protection measures throughout the data lifecycle.

#### 2.1.1 PII Definition and Categories

**Personal Data / PII Definition** (aligned with GDPR Art. 4(1), FADP Art. 5(a)):

Personal data / personally identifiable information (PII) means **any information relating to an identified or identifiable natural person** (data subject). An identifiable person is one who can be identified, directly or indirectly, by reference to:
- Name, identification number, location data, online identifier (IP address, cookie ID)
- One or more factors specific to physical, physiological, genetic, mental, economic, cultural, or social identity

**Key Principle**: Information is PII if it can identify an individual when combined with other information reasonably available to [Organization] or third parties.

**PII Categories**:

[Organization] classifies PII into three categories aligned with regulatory requirements:

**Category 1: Basic PII** (Standard Personal Data)

Personal data requiring standard protection measures under GDPR/FADP:

| Data Type | Regulatory Basis | Common Processing Context |
|-----------|-----------------|---------------------------|
| **Identification Data** | GDPR Art. 4(1), FADP Art. 5(a) | Customer accounts, employee records, vendor contacts |
| **Contact Information** | GDPR Art. 4(1), FADP Art. 5(a) | Communications, service delivery, marketing |
| **Financial Data** | GDPR Art. 4(1), FADP Art. 5(a) | Payment processing, invoicing, expense management |
| **Professional Data** | GDPR Art. 4(1), FADP Art. 5(a) | B2B relationships, HR records, recruitment |
| **Electronic Identifiers** | GDPR Art. 4(1), FADP Art. 5(a) | Website analytics, system access logs, security monitoring |
| **Geographic Data** | GDPR Art. 4(1), FADP Art. 5(a) | Location-based services, logistics, expense tracking |
| **Behavioral Data** | GDPR Art. 4(1), FADP Art. 5(a) | Customer analytics, product recommendations, usage reporting |
| **Communications Data** | GDPR Art. 4(1), FADP Art. 5(a) | Business communications, customer support, collaboration |

**Protection Requirements**: Standard security controls per ISMS baseline (access control, encryption in transit/rest, audit logging, retention limits).

---

**Category 2: Sensitive PII** (Special Category Data)

Personal data requiring enhanced protection due to higher risk to data subjects' rights and freedoms.

**GDPR Article 9 Special Categories**:

| Data Type | Processing Restrictions | Regulatory Basis |
|-----------|------------------------|------------------|
| **Racial/Ethnic Origin** | Explicit consent OR specific Art. 9(2) exemption required | GDPR Art. 9(1) |
| **Political Opinions** | Explicit consent OR specific Art. 9(2) exemption required | GDPR Art. 9(1) |
| **Religious/Philosophical Beliefs** | Explicit consent OR specific Art. 9(2) exemption required | GDPR Art. 9(1) |
| **Trade Union Membership** | Explicit consent OR specific Art. 9(2) exemption required | GDPR Art. 9(1) |
| **Genetic Data** | Explicit consent OR specific Art. 9(2) exemption required | GDPR Art. 9(1) |
| **Biometric Data (for unique identification)** | Explicit consent OR specific Art. 9(2) exemption required | GDPR Art. 9(1) |
| **Health Data** | Explicit consent OR specific Art. 9(2) exemption required | GDPR Art. 9(1) |
| **Sex Life / Sexual Orientation** | Explicit consent OR specific Art. 9(2) exemption required | GDPR Art. 9(1) |

**FADP Special Categories** (Article 5(c) - similar to GDPR):
- Religious, philosophical, political, trade union views
- Health, private sphere, racial/ethnic affiliation
- Genetic data, biometric data
- Administrative/criminal proceedings data
- Social assistance data

**Protection Requirements**: 
- **Legal Basis**: GDPR Art. 6 legal basis PLUS Art. 9(2) specific condition (document justification)
- **Enhanced Security**: Encryption at rest and in transit (mandatory), strict access controls, enhanced audit logging
- **Data Minimization**: Process only when strictly necessary, pseudonymize where possible
- **DPIA**: Data Protection Impact Assessment mandatory for special category processing (GDPR Art. 35)
- **Retention**: Minimize retention period, automated deletion where feasible
- **Training**: Personnel handling special category data receive additional privacy training

---

**Category 3: Criminal Offense Data**

Personal data relating to criminal convictions, offenses, or related security measures (GDPR Art. 10, FADP Art. 5(c)5).

| Data Type | Processing Authority | Regulatory Basis |
|-----------|---------------------|------------------|
| **Criminal Convictions** | Official authority control OR specific legal basis + safeguards | GDPR Art. 10, FADP Art. 5(c) |
| **Criminal Offenses** | Official authority control OR specific legal basis + safeguards | GDPR Art. 10, FADP Art. 5(c) |
| **Security Measures** | Official authority control OR specific legal basis + safeguards | GDPR Art. 10, FADP Art. 5(c) |

**Processing Restrictions**:
- GDPR: Processing only under control of official authority OR authorized by EU/Member State law with appropriate safeguards
- FADP: Sensitive data category requiring appropriate legal basis and safeguards
- [Organization] does NOT routinely process criminal offense data except where legally authorized

**Protection Requirements**: Same as Special Category Data plus legal authorization verification.

---

#### 2.1.2 PII Discovery and Data Mapping Requirements

[Organization] SHALL maintain current knowledge of all PII processing activities through systematic discovery and data mapping.

**PII Discovery Requirements**:

[Organization] SHALL conduct PII discovery using combination of automated and manual methods:
- Automated scanning tools (DLP, database scanners, file system scanners, CASB for SaaS)
- Manual discovery (departmental questionnaires, new system assessments, vendor contract reviews, business process mapping)

**Discovery Frequency**:
- **Comprehensive scan**: Annually (minimum)
- **New systems**: Before production deployment
- **Changed processes**: Within 30 days of material change
- **Incident-driven**: After data breach or near-miss

**Data Mapping Requirements**:

[Organization] SHALL document PII flows including:
1. Data source and collection method
2. Processing purpose and legal basis
3. PII categories and data subjects
4. Storage locations and access controls
5. Sharing/disclosure recipients
6. Cross-border transfers and mechanisms
7. Retention period and deletion method

**Data Flow Diagrams**: [Organization] SHALL create visual data flow diagrams showing PII movement through systems and across organizational boundaries. Diagrams updated annually or upon material changes.

**Implementation Reference**: ISMS-IMP-A.5.34.1 (PII Identification and Classification Assessment) provides detailed discovery and mapping procedures.

---

#### 2.1.3 Record of Processing Activities (ROPA)

**GDPR Article 30 / FADP Requirement**:

[Organization] SHALL maintain a **Record of Processing Activities** (ROPA) documenting all personal data processing operations.

**ROPA Minimum Content**:

**For [Organization] as Data Controller** (GDPR Art. 30(1)):
1. Name and contact details of controller, representative (if applicable), DPO
2. Purposes of processing
3. Categories of data subjects
4. Categories of personal data
5. Categories of recipients
6. Transfers to third countries (countries, safeguards)
7. Retention periods (or criteria)
8. General description of technical and organizational security measures

**For [Organization] as Data Processor** (GDPR Art. 30(2), if applicable):
1. Name and contact details of processor, controllers, DPO
2. Categories of processing carried out on behalf of each controller
3. Transfers to third countries (countries, safeguards)
4. General description of technical and organizational security measures

**ROPA Maintenance**:
- **Review Frequency**: Quarterly (minimum), or upon material changes
- **Update Triggers**: New processing activities, changed purposes, new data categories, changed retention, new third-party sharing, changed transfer mechanisms
- **Ownership**: DPO/Privacy Officer maintains ROPA with input from business units
- **Validation**: Annual validation by Legal and CISO

**ROPA Integration**: 
- Links to Data Protection Impact Assessments (DPIAs)
- Links to processor agreements (GDPR Art. 28 contracts)
- Links to legitimate interest assessments (LIAs)
- Cross-referenced with asset inventory (ISMS-POL-A.5.9)

**Small Organization Exemption**: GDPR Art. 30(5) exempts organizations with <250 employees UNLESS processing likely to result in risk to data subjects, processing is not occasional, or processing includes special category data.

[Organization] maintains ROPA regardless of size as best practice for accountability and ISO 27001:2022 certification support.

**Implementation Reference**: ISMS-IMP-A.5.34.1 provides ROPA template, maintenance procedures, and assessment workbook.

---

### 2.2 Legal Basis and Lawful Processing

[Organization] SHALL process personal data only when there is a valid legal basis under applicable privacy regulations.

#### 2.2.1 Legal Bases for Processing

**GDPR Article 6 - Legal Bases**:

Processing is lawful ONLY if at least one of the following applies:

**1. Consent (Article 6(1)(a))**:
- Data subject has given clear, affirmative consent to processing for specific purposes
- Requirements: Freely given, specific, informed, unambiguous, withdrawable
- Use Cases: Marketing communications, optional service features, non-essential cookies

**2. Contract Performance (Article 6(1)(b))**:
- Processing is necessary for performance of a contract with data subject
- Requirements: Contract must exist, processing must be genuinely necessary
- Use Cases: Processing customer orders, employee HR data, service provisioning

**3. Legal Obligation (Article 6(1)(c))**:
- Processing is necessary for compliance with legal obligation
- Requirements: Specific legal obligation under EU or Member State law
- Use Cases: Tax reporting, statutory accounting, AML/KYC compliance, lawful court orders

**4. Vital Interests (Article 6(1)(d))**:
- Processing is necessary to protect vital interests of data subject or another person
- Requirements: Genuine emergency, life-or-death situations, last resort
- Use Cases: Medical emergencies, natural disaster response, child protection emergencies

**5. Public Task (Article 6(1)(e))**:
- Processing is necessary for performance of task in public interest
- Requirements: Public interest task set out in law, controller is public authority
- Applicability: Typically NOT applicable to private organizations

**6. Legitimate Interests (Article 6(1)(f))**:
- Processing is necessary for legitimate interests pursued by controller or third party
- Requirements: Identify legitimate interest, demonstrate necessity, balance against data subject rights
- Use Cases: Fraud prevention, network security, internal admin, B2B marketing
- **Balancing Test Required**: Conduct Legitimate Interest Assessment (LIA)
- Limitations: Cannot use for special category data without additional basis

**FADP Processing Principles** (Article 6):
- Lawfulness: Processing must comply with law
- Good Faith: Processing must be fair and non-deceptive
- Proportionality: Processing must be proportionate to purpose
- Purpose Limitation: Processing only for specified purposes
- Data Minimization: Only necessary data processed

---

#### 2.2.2 Legal Basis Determination Requirements

**Legal Basis Selection**:

[Organization] SHALL determine and document the legal basis for each processing activity **before processing begins**.

**Documentation Requirements**:

[Organization] SHALL document in ROPA for each processing activity:
- **Legal Basis**: Which Article 6(1) or FADP principle applies
- **Justification**: Why this legal basis is appropriate
- **Evidence**: Supporting documentation (consent records, LIA, contract template, legal provision)
- **Special Category Basis**: If applicable, Article 9(2) condition

**Special Category Data**: MUST have Article 6 legal basis PLUS Article 9(2) specific condition.

**Legal Basis Immutability**: Legal basis cannot be changed retroactively. If original legal basis fails, processing must stop UNLESS new independent legal basis exists.

**Implementation Reference**: ISMS-IMP-A.5.34.2 (Legal Basis and Lawful Processing Assessment) provides legal basis assessment procedures, LIA template, consent management requirements.

---

#### 2.2.3 Consent Management Requirements

When **Consent** is the legal basis for processing, [Organization] SHALL implement compliant consent management.

**Valid Consent Requirements** (GDPR Article 7, Article 4(11)):

**Consent Must Be**:
1. **Freely Given**: No coercion, no service denial for non-essential processing, no bundled consent
2. **Specific**: Granular consent for each purpose, separate consent for separate purposes
3. **Informed**: Identity of controller, purpose, data types, right to withdraw, consequences
4. **Unambiguous**: Clear affirmative action required (no pre-ticked boxes, silence, inactivity)
5. **Withdrawable**: Data subject can withdraw consent at any time, withdrawal as easy as giving consent

**Consent for Children** (GDPR Article 8):
- Information society services require parental consent for children under age 16 (Member States may lower to 13)
- Controller must make reasonable efforts to verify parental consent

**Consent Records**:

[Organization] SHALL maintain records demonstrating:
- Who gave consent
- When consent was given
- What they were told
- How consent was obtained
- Evidence of consent
- If applicable: When consent was withdrawn

**Consent Refresh**: 
- No mandated expiration under GDPR, but best practice: refresh every 24-36 months for ongoing marketing
- Must refresh if processing purpose changes materially, new data categories collected, new third-party sharing introduced, material change in controller identity

**Implementation Reference**: ISMS-IMP-A.5.34.2 provides consent management platform requirements, consent record structure, withdrawal processing procedures.

---

#### 2.2.4 Legitimate Interest Assessments (LIA)

When **Legitimate Interests** (GDPR Art. 6(1)(f)) is the legal basis, [Organization] SHALL conduct and document a **Legitimate Interest Assessment** (LIA) before processing begins.

**LIA Three-Part Test**:

**Part 1: Purpose Test** - Is there a legitimate interest?
- Identify business interest, third-party interest, or societal interest
- Must be lawful, clear, specific, real and present

**Part 2: Necessity Test** - Is processing necessary for that interest?
- Assess whether interest could be achieved without processing personal data
- Assess whether less intrusive processing could achieve same outcome
- Processing must be proportionate to interest

**Part 3: Balancing Test** - Do data subject rights override the legitimate interest?
- Consider nature of data, reasonable expectations, impact on data subject, relationship, safeguards, vulnerable groups
- If legitimate interest clearly outweighs data subject rights → Processing justified
- If balance uncertain or rights likely impacted → Use different legal basis

**LIA Documentation**:

[Organization] SHALL document LIAs including:
- Processing activity description
- Legitimate interest identified
- Necessity justification
- Data subject impact assessment
- Safeguards implemented
- Balancing test conclusion
- Date of assessment, assessor name

**LIA Review**: Annually or when processing changes materially.

**Implementation Reference**: ISMS-IMP-A.5.34.2 provides LIA template, assessment procedures, balancing test guidance.

---

### 2.3 Data Subject Rights Framework

[Organization] SHALL enable data subjects to exercise their rights under GDPR (Articles 12-22) and FADP (Articles 25-32).

#### 2.3.1 Right of Access (GDPR Article 15, FADP Article 25)

**Right**: Data subject has right to obtain confirmation whether [Organization] processes their personal data, and if so, access to copy of personal data and information about processing.

**[Organization] Obligations**:

[Organization] SHALL:
- Receive and verify access requests via designated channels
- Respond within timeframe: GDPR 1 month (extendable to 3 months if complex), FADP "reasonable time"
- Provide confirmation of processing (yes/no)
- Provide copy of personal data (first copy free, further copies: reasonable fee)
- Provide information per Article 15(1): purposes, categories, recipients, retention period, data subject rights, source of data, existence of automated decision-making
- Deliver response in commonly intelligible form, structured, machine-readable format if electronic
- No fee for first request (subsequent repetitive requests: reasonable administrative fee)

**Exceptions**: May refuse if manifestly unfounded/excessive, affects other people's rights, discloses confidential business information, or involves legal professional privilege. Refusal must be justified.

**Implementation Reference**: ISMS-IMP-A.5.34.3 provides detailed request handling procedures.

---

#### 2.3.2 Right to Rectification (GDPR Article 16, FADP Article 32)

**Right**: Data subject has right to obtain rectification of inaccurate personal data and completion of incomplete personal data.

**[Organization] Obligations**:

[Organization] SHALL:
- Receive and verify rectification requests
- Respond within timeframe: GDPR 1 month (extendable to 3 months if complex), FADP "without undue delay"
- Correct inaccurate data in all systems (production, backups, archives - where feasible)
- Complete incomplete data if relevant to processing purpose
- Notify recipients of rectification (if feasible and not disproportionate)
- Confirm completion to data subject
- No fee

**Proactive Obligation**: [Organization] has duty to keep personal data accurate (GDPR Art. 5(1)(d), FADP Art. 6(4)).

**Implementation Reference**: ISMS-IMP-A.5.34.3 provides rectification procedures.

---

#### 2.3.3 Right to Erasure / "Right to be Forgotten" (GDPR Article 17, FADP Article 32)

**Right**: Data subject has right to obtain erasure of their personal data when specific grounds apply.

**Erasure Grounds** (GDPR Art. 17(1)):
1. No longer necessary for purposes
2. Consent withdrawn AND no other legal basis exists
3. Data subject objects AND no overriding legitimate grounds exist
4. Unlawful processing
5. Legal obligation requires erasure
6. Children's data collected for information society services

**[Organization] Obligations**:

[Organization] SHALL:
- Receive and verify erasure requests
- Assess whether erasure grounds exist
- Respond within timeframe: GDPR 1 month (extendable to 3 months if complex), FADP "without undue delay"
- If granted: Delete personal data from all systems (production, test, development, backups - see limitations)
- Notify recipients of erasure (if feasible and not disproportionate)
- If personal data made public, take reasonable steps to inform other controllers to erase links/copies
- No fee

**Exceptions / Refusal Grounds** (GDPR Art. 17(3)):

[Organization] MAY refuse erasure when processing is necessary for:
1. Freedom of expression/information
2. Legal obligation requiring processing
3. Public interest task or official authority
4. Public health
5. Archiving in public interest, scientific/historical research, statistical purposes
6. Establishment, exercise, or defense of legal claims

**Common Refusal Scenarios**:
- Tax/accounting records during statutory retention period
- Ongoing contract requiring data
- Fraud investigation data
- Legitimate interest processing where balancing test still favors controller

**Backup Limitations**: 
- Immediate erasure from production systems required
- Backup tapes/images: Best-effort erasure on next backup cycle
- Archived backups: May retain until backup expiry IF isolated and not accessible

**Implementation Reference**: ISMS-IMP-A.5.34.3 provides erasure procedures. Integration with ISMS-POL-A.8.10 (Information Deletion) for secure deletion methods.

---

#### 2.3.4 Right to Data Portability (GDPR Article 20)

**Right**: Data subject has right to receive personal data in structured, commonly used, machine-readable format and right to transmit to another controller.

**Applicability Conditions** (All must be met):
1. Processing based on consent (Art. 6(1)(a), Art. 9(2)(a)) OR contract (Art. 6(1)(b))
2. Processing carried out by automated means

**[Organization] Obligations**:

[Organization] SHALL:
- Receive and verify portability requests
- Assess whether applicability conditions met
- Respond within timeframe: GDPR 1 month (extendable to 3 months if complex)
- Provide data in structured, commonly used, machine-readable format (JSON, CSV, XML)
- Include personal data provided by data subject (not inferred/derived data)
- Where technically feasible and requested, transmit directly to another controller
- No fee

**Scope Limitations**:
- Only data "provided by" data subject (actively submitted OR generated through use of service)
- Only automated processing (excludes paper records, manual notes)
- No third-party data (redact if providing would affect others' rights)

**Not Applicable**:
- Processing based on legitimate interest, legal obligation, or public interest task
- Paper/manual records

**FADP**: No explicit data portability right (GDPR-specific).

**Implementation Reference**: ISMS-IMP-A.5.34.3 provides portability procedures and data export format specifications.

---

#### 2.3.5 Right to Object (GDPR Article 21)

**Right**: Data subject has right to object to processing of their personal data.

**Two Types of Objection**:

**1. Objection to Legitimate Interest Processing (Article 21(1))**:

Data subject may object to processing based on legitimate interests (Art. 6(1)(f)) or public interest task (Art. 6(1)(e)).

**[Organization] Response**:
- **MUST stop processing** UNLESS [Organization] demonstrates compelling legitimate grounds that override data subject interests, rights, freedoms OR processing is for legal claims
- Burden of proof on [Organization]

**Practical Effect**: Objection usually succeeds unless strong justification.

---

**2. Objection to Direct Marketing (Article 21(2-3))**:

Data subject has **absolute right** to object to processing for direct marketing purposes, including profiling related to direct marketing.

**[Organization] Response**:
- **MUST stop processing** for direct marketing (no exceptions, no overriding grounds)
- Implement objection immediately (unsubscribe within 24 hours)

**Proactive Obligation**:
- Data subjects must be explicitly informed of right to object at first communication and in every subsequent communication
- Right to object presented clearly and separately from other information
- Objection mechanism must be easy (one-click unsubscribe)

---

**[Organization] Obligations**:

[Organization] SHALL:
- Receive objection via any channel
- No identity verification required for marketing objections (honor all unsubscribe requests)
- Identity verification for legitimate interest objections (if necessary)
- Respond within timeframe: Direct marketing immediate (24-48 hours), Legitimate interest 1 month
- For direct marketing: Stop processing immediately, maintain suppression list
- For legitimate interest: Assess overriding grounds, stop processing if no compelling justification
- No fee

**Suppression Lists**: 
- Maintain "do not contact" suppression lists for marketing objections
- Minimal data retention (email/ID only) to prevent re-adding
- Suppression list maintenance is lawful processing (legitimate interest in complying with objection)

**FADP Objection**: Similar right exists under FADP principles.

**Implementation Reference**: ISMS-IMP-A.5.34.3 provides objection handling procedures and suppression list management.

---

#### 2.3.6 Right to Restriction of Processing (GDPR Article 18)

**Right**: Data subject has right to obtain restriction of processing (processing paused, data retained) when specific grounds apply.

**Restriction Grounds**:
1. Data subject contests accuracy (restrict during verification)
2. Processing unlawful, but data subject opposes erasure and requests restriction
3. [Organization] no longer needs data, but data subject requires it for legal claims
4. Data subject objected (Art. 21(1)), pending verification of overriding grounds

**Effect of Restriction**:

When processing restricted, [Organization] may:
- **Store** personal data (retention allowed)
- **NOT process** (no use, modification, disclosure) EXCEPT with data subject consent, for legal claims, for protection of rights of another person, or for important public interest

**[Organization] Obligations**:

[Organization] SHALL:
- Receive and verify restriction requests
- Assess whether restriction grounds exist
- Respond within timeframe: GDPR 1 month (extendable to 3 months if complex)
- Implement restriction (flag records, limit processing)
- Notify recipients of restriction (if feasible)
- Inform data subject when restriction will be lifted
- No fee

**Lifting Restriction**: Data subject must be informed before restriction lifted.

**FADP**: No explicit restriction right (GDPR-specific), but similar outcome achievable through FADP objection right.

**Implementation Reference**: ISMS-IMP-A.5.34.3 provides restriction procedures and system flagging requirements.

---

#### 2.3.7 Rights Request Handling Framework

**Centralized Request Management**:

[Organization] SHALL implement systematic data subject rights request management.

**Request Receipt Channels**:
- Designated email address (e.g., privacy@[organization].com, dpo@[organization].com)
- Web form on privacy policy page
- Postal mail to DPO/Privacy Officer address
- In-person requests (for employees, contractors)

**Request Processing Requirements**:
- Identity verification (proportionate to risk)
- Request logging and tracking
- Response timeframes per regulation
- Communication with data subject throughout process
- Documentation of decisions and actions taken

**Response Standards**:
- Clear, plain language
- Concise, transparent, intelligible form
- Free of charge (except repetitive/manifestly unfounded requests)
- Electronic format where feasible

**Refusal Requirements**:
- Inform data subject of reasons for refusal
- Inform of right to complain to supervisory authority
- Inform of right to judicial remedy
- Document justification for refusal

**Implementation Reference**: ISMS-IMP-A.5.34.3 (Data Subject Rights Management Assessment) provides comprehensive request handling procedures, verification methods, response templates, escalation workflows, tracking mechanisms.

---

### 2.4 Privacy by Design and by Default

[Organization] SHALL implement Privacy by Design and by Default principles (GDPR Article 25, FADP principles) throughout the data lifecycle.

#### 2.4.1 Privacy by Design Requirements

**Privacy by Design** (GDPR Article 25(1)):

[Organization] SHALL implement appropriate technical and organizational measures designed to implement data protection principles effectively and integrate necessary safeguards into processing.

**Implementation Requirements**:

[Organization] SHALL consider at the time of determination of means of processing and at the time of processing itself:
- State of the art
- Cost of implementation
- Nature, scope, context, and purposes of processing
- Risks to data subject rights and freedoms

**Privacy by Design Principles**:

[Organization] SHALL apply Privacy by Design principles throughout system development and processing design:

1. **Proactive not Reactive**: Anticipate and prevent privacy risks before they materialize
2. **Privacy as Default Setting**: Ensure maximum privacy protection without user action required
3. **Privacy Embedded into Design**: Integrated into IT systems, business practices, physical infrastructure
4. **Full Functionality**: Positive-sum not zero-sum (privacy AND functionality)
5. **End-to-End Security**: Secure lifecycle management from collection to deletion
6. **Visibility and Transparency**: Keep systems visible and transparent to users and providers
7. **Respect for User Privacy**: Keep it user-centric with strong privacy defaults

**Technical Measures**:

[Organization] SHALL consider implementing:
- Pseudonymization and anonymization where feasible
- Encryption at rest and in transit for sensitive PII
- Access controls based on least privilege and need-to-know
- Automated data minimization (collect only necessary data)
- Privacy-enhancing technologies (PETs)
- Secure data deletion mechanisms
- Privacy-preserving analytics methods

**Organizational Measures**:

[Organization] SHALL consider implementing:
- Privacy requirements in system design specifications
- Privacy review in change management process
- Privacy testing in software development lifecycle
- Privacy training for developers and system owners
- Privacy impact considerations in vendor selection
- Data protection clauses in contracts
- Privacy governance oversight

**Implementation Reference**: ISMS-IMP-A.5.34.4 (Technical and Organizational Measures Assessment) provides detailed Privacy by Design implementation checklist, design patterns, technical control specifications.

---

#### 2.4.2 Privacy by Default Requirements

**Privacy by Default** (GDPR Article 25(2)):

[Organization] SHALL implement appropriate technical and organizational measures to ensure that, by default, only personal data necessary for each specific purpose of processing are processed.

**Default Configuration Requirements**:

[Organization] SHALL ensure by default:
- **Data Minimization**: Only necessary personal data collected and processed
- **Limited Processing Scope**: Data processed only for specified purposes
- **Limited Storage Period**: Data retained only as long as necessary
- **Limited Accessibility**: Data not made accessible to indefinite number of persons without individual's intervention

**Examples of Privacy by Default**:

[Organization] SHALL implement configurations such as:
- Default cookie settings: Only essential cookies enabled, analytics/marketing require opt-in
- Default account visibility: User profiles private by default, public sharing requires opt-in
- Default data sharing: Third-party data sharing disabled by default, requires opt-in
- Default retention: Shortest reasonable retention period configured by default
- Default access: Minimum necessary access granted by default, elevated access requires justification

**User Control Requirements**:

[Organization] SHALL provide users with:
- Easy-to-access privacy settings and controls
- Granular control over data processing purposes
- Clear explanation of implications of privacy choices
- Ability to modify settings at any time

**Implementation Reference**: ISMS-IMP-A.5.34.4 provides Privacy by Default configuration checklist, default settings specifications, user control implementation guidance.

---

**[END OF PART 1]**

**Continue to Part 2 for**:
- Section 2.5: Data Protection Impact Assessments (DPIA)
- Section 2.6: Cross-Border Data Transfers
- Section 2.7: Data Breach Notification
- Section 2.8: Technical and Organizational Measures (TOMs)
- Section 3: Roles and Responsibilities
- Section 4: Governance, Review, and Documentation
- Section 5: Integration with Other Controls
- Annex A: Data Subject Rights Request Decision Matrix
- Annex B: DPIA Trigger Assessment

---

### 2.5 Data Protection Impact Assessments (DPIA)

[Organization] SHALL conduct Data Protection Impact Assessments for processing operations likely to result in high risk to data subject rights and freedoms.

#### 2.5.1 DPIA Requirements (GDPR Article 35)

**When DPIA is Required**:

[Organization] SHALL conduct a DPIA before processing when the processing is likely to result in high risk to data subject rights and freedoms, in particular when using new technologies.

**GDPR Article 35(3) - DPIA is Required for**:
1. **Systematic and extensive evaluation** of personal aspects relating to natural persons based on automated processing, including profiling, on which decisions are based that produce legal effects or similarly significantly affect the natural person
2. **Processing on a large scale of special categories of data** (Art. 9) or personal data relating to criminal convictions and offenses (Art. 10)
3. **Systematic monitoring of a publicly accessible area on a large scale** (e.g., CCTV surveillance)

**Additional DPIA Triggers**:

[Organization] SHALL also conduct DPIA when processing involves:
- Use of new technologies
- Large-scale processing of personal data
- Processing that prevents data subjects from exercising a right or using a service
- Automated decision-making with legal or similarly significant effects
- Data matching or combining datasets from different sources
- Processing of vulnerable data subjects (children, employees, patients, elderly)
- Innovative use or application of technological or organizational solutions
- Processing involving cross-border data transfers outside adequate jurisdictions without appropriate safeguards

**DPIA Not Required**:
- Processing not likely to result in high risk to data subjects
- Processing is similar to previously assessed processing (may reference earlier DPIA)
- Processing has legal basis in EU or Member State law regulating the specific processing operation

**Consultation with Supervisory Authority** (GDPR Article 36):

If DPIA indicates high risk AND [Organization] cannot implement sufficient measures to mitigate risk, [Organization] SHALL consult with the supervisory authority (FDPIC for Switzerland, relevant DPA for GDPR) **before** commencing processing.

#### 2.5.2 DPIA Content Requirements

[Organization] SHALL document in the DPIA at minimum (GDPR Art. 35(7)):
1. **Systematic description** of envisaged processing operations and purposes of processing, including legitimate interest where applicable
2. **Assessment of necessity and proportionality** of processing operations in relation to purposes
3. **Assessment of risks** to data subject rights and freedoms
4. **Measures envisaged** to address risks, including safeguards, security measures, mechanisms to ensure protection of personal data and demonstrate compliance

**Risk Assessment Framework**:

[Organization] SHALL assess:
- **Likelihood** of risk materialization (low, medium, high)
- **Severity** of impact on data subjects (low, medium, high)
- **Overall risk level** (likelihood × severity)
- **Residual risk** after mitigating measures

**DPIA Methodology**:

[Organization] SHALL use structured DPIA methodology considering:
- Data subject perspective and reasonable expectations
- Potential for discrimination or unfair treatment
- Potential for reputational damage to data subjects
- Potential for financial loss to data subjects
- Potential for physical harm to data subjects
- Potential for loss of confidentiality
- Potential for loss of availability
- Potential for loss of control over personal data

#### 2.5.3 DPIA Responsibilities and Review

**DPIA Responsibilities**:
- **DPO**: Must be consulted on DPIA (GDPR Art. 35(2))
- **Processing Owner**: Responsible for conducting DPIA
- **Security Team**: Provides technical risk assessment input
- **Legal**: Provides regulatory compliance assessment
- **Data Subjects** (or representatives): Should be consulted where appropriate and feasible

**DPIA Review**:
- **Initial**: Before commencing high-risk processing
- **Ongoing**: When circumstances change (technology, purpose, data categories, risk landscape)
- **Periodic**: Minimum every 24 months for ongoing high-risk processing

**DPIA Register**:

[Organization] SHALL maintain a register of completed DPIAs including:
- Processing activity name and description
- DPIA completion date
- DPIA outcome (approved, approved with conditions, rejected, requires supervisory authority consultation)
- Risk rating (low, medium, high, residual)
- Review date
- DPO consultation confirmation

**Implementation Reference**: ISMS-IMP-A.5.34.5 (Data Protection Impact Assessment) provides DPIA methodology, templates, risk assessment framework, consultation procedures, DPIA register.

---

### 2.6 Cross-Border Data Transfers

[Organization] SHALL ensure lawful mechanisms are in place for transfers of personal data to third countries or international organizations.

#### 2.6.1 Transfer Requirements (GDPR Chapter V, FADP Articles 16-17)

**General Principle**:

Personal data SHALL NOT be transferred to third countries (countries outside the EU/EEA for GDPR, outside Switzerland for FADP) unless appropriate safeguards are in place.

**Third Country Definition**:
- **GDPR**: Countries outside European Union / European Economic Area
- **FADP**: Countries outside Switzerland

**Transfer Includes**:
- Storage of personal data in third country
- Access to personal data by entities in third country
- Processing by third-party service providers in third country
- Remote access to EU/CH-based systems from third country

#### 2.6.2 Transfer Mechanisms (GDPR Articles 45-46, FADP Articles 16-17)

**Mechanism 1: Adequacy Decision** (GDPR Art. 45, FADP Art. 16(1)):

Transfer is permitted if European Commission (for GDPR) or Swiss Federal Council (for FADP) has determined that third country ensures adequate level of data protection.

**GDPR Adequate Countries** (as of policy date - verify current list):
- Andorra, Argentina, Canada (commercial organizations), Faroe Islands, Guernsey, Israel, Isle of Man, Japan, Jersey, New Zealand, Republic of Korea, Switzerland, United Kingdom, Uruguay
- Note: United States under EU-U.S. Data Privacy Framework (limited to certified organizations)

**FADP Adequate Countries** (verify current FDPIC list):
- EU/EEA countries, United Kingdom, and others as determined by Swiss Federal Council

**No additional safeguards required** for transfers to adequate countries.

---

**Mechanism 2: Appropriate Safeguards** (GDPR Art. 46, FADP Art. 16(2)):

If adequacy decision does not exist, transfer is permitted if appropriate safeguards are in place:

**Standard Contractual Clauses (SCCs)** (GDPR Art. 46(2)(c), FADP Art. 16(2)(d)):
- Use of European Commission approved Standard Contractual Clauses (GDPR)
- Use of Swiss Federal Data Protection and Information Commissioner approved contractual clauses (FADP)
- **Most common mechanism** for commercial transfers
- Requires: Signed SCCs, documented transfer impact assessment (Schrems II compliance)

**Binding Corporate Rules (BCRs)** (GDPR Art. 46(2)(b), FADP Art. 16(2)(e)):
- Approved by supervisory authority
- Internal rules for multinational group of undertakings
- Binding privacy rules for intra-group transfers
- Requires: DPA approval, legally binding rules, third-party beneficiary rights

**Approved Codes of Conduct** (GDPR Art. 46(2)(e)):
- Code of conduct approved by supervisory authority
- Binding commitment by controller/processor in third country

**Approved Certification Mechanisms** (GDPR Art. 46(2)(f)):
- Certification mechanism approved by supervisory authority
- Binding commitment by controller/processor in third country

**Ad Hoc Contractual Clauses** (GDPR Art. 46(3)(a), FADP Art. 16(2)(a)):
- Contractual clauses authorized by supervisory authority
- Tailored contracts for specific transfer scenarios
- Requires: DPA authorization

---

**Mechanism 3: Derogations for Specific Situations** (GDPR Art. 49, FADP Art. 17):

In absence of adequacy decision or appropriate safeguards, transfer is permitted ONLY in specific situations:

**GDPR Article 49 Derogations** (use as last resort, cannot be routine):
1. **Explicit consent**: Data subject has explicitly consented to proposed transfer after being informed of risks
2. **Contract performance**: Transfer necessary for performance of contract between data subject and controller
3. **Contract in data subject's interest**: Transfer necessary for conclusion/performance of contract between controller and another person in interest of data subject
4. **Important public interest**: Transfer necessary for important reasons of public interest
5. **Legal claims**: Transfer necessary for establishment, exercise, or defense of legal claims
6. **Vital interests**: Transfer necessary to protect vital interests where data subject incapable of giving consent
7. **Public register**: Transfer from public register
8. **Legitimate interests** (Art. 49(1) second subparagraph): Limited to occasional, non-repetitive transfers, limited number of data subjects, necessary for compelling legitimate interests not overridden by data subject interests

**FADP Article 17 Derogations**:
- Consent with information about inadequate protection
- Necessary for contract performance
- Necessary to protect overriding public interest
- Necessary to establish, exercise, or enforce legal rights
- Necessary to protect data subject's vital interests
- Transfer from publicly accessible register

**Limitations on Derogations**:
- Cannot be used for routine, repetitive, or structural transfers
- Cannot be relied upon as permanent transfer mechanism
- Must be documented with justification each time used
- Must inform data subject of risks where required

#### 2.6.3 Transfer Governance Requirements

**Transfer Assessment**:

[Organization] SHALL assess and document for each transfer:
1. **Destination country** (identify third country receiving data)
2. **Transfer mechanism** (adequacy, SCCs, BCR, derogation)
3. **Data categories** (what personal data is transferred)
4. **Purpose** (why transfer is necessary)
5. **Frequency** (one-time, occasional, systematic)
6. **Recipients** (who receives data in third country)
7. **Safeguards** (technical and organizational measures)
8. **Risks** (assessment of risks to data subjects in third country context)

**Transfer Impact Assessment** (Schrems II Requirement):

For transfers not based on adequacy decision, [Organization] SHALL assess:
- Laws and practices in third country that may impact data protection
- Supplementary measures needed beyond SCCs to ensure adequate protection
- Whether effective protection can be ensured
- If not, whether to suspend or terminate transfer

**Transfer Documentation**:

[Organization] SHALL maintain:
- Register of all cross-border data transfers
- Copies of SCCs, BCRs, or other transfer mechanisms
- Transfer impact assessments
- Derogation justifications (where applicable)

**Transfer Review**:
- Annual review of all systematic transfers
- Review upon changes in third country law or practice
- Review upon changes in processing activities

**Implementation Reference**: ISMS-IMP-A.5.34.6 (Cross-Border Transfer Assessment) provides transfer assessment methodology, SCC templates, transfer impact assessment guidance, transfer register.

---

### 2.7 Data Breach Notification

[Organization] SHALL implement data breach notification procedures to comply with GDPR Article 33-34 and FADP Article 24.

#### 2.7.1 Data Breach Definition

**Personal Data Breach** (GDPR Art. 4(12)):

A breach of security leading to accidental or unlawful:
- **Destruction** of personal data
- **Loss** of personal data
- **Alteration** of personal data
- **Unauthorized disclosure** of personal data
- **Unauthorized access** to personal data

**Breach Types**:
1. **Confidentiality Breach**: Unauthorized or accidental disclosure or access to personal data
2. **Availability Breach**: Accidental or unauthorized loss of access to, or destruction of, personal data
3. **Integrity Breach**: Unauthorized or accidental alteration of personal data

#### 2.7.2 Breach Notification to Supervisory Authority

**GDPR Article 33 - Notification to Supervisory Authority**:

[Organization] SHALL notify the supervisory authority **without undue delay and, where feasible, not later than 72 hours** after becoming aware of a personal data breach, UNLESS the breach is unlikely to result in a risk to data subject rights and freedoms.

**"Becoming Aware"**: When [Organization] has reasonable degree of certainty that a security incident has occurred that resulted in personal data being compromised.

**FADP Article 24 - Notification to FDPIC**:

[Organization] SHALL inform the FDPIC **as quickly as possible** of data breach if breach is likely to result in a high risk to the personality or fundamental rights of the data subject.

**Notification Content** (GDPR Art. 33(3)):

Notification to supervisory authority SHALL include:
1. **Nature of breach**: Categories and approximate number of data subjects affected, categories and approximate number of personal data records concerned
2. **DPO contact**: Name and contact details of DPO or other contact point
3. **Likely consequences**: Description of likely consequences of breach
4. **Measures taken**: Description of measures taken or proposed to address breach and mitigate adverse effects

**Phased Notification**: If information cannot be provided simultaneously, it may be provided in phases without undue further delay.

**Documentation Requirement**: [Organization] SHALL document all personal data breaches (even those not notified), including facts, effects, and remedial action taken. Documentation must be available for supervisory authority verification.

#### 2.7.3 Breach Communication to Data Subjects

**GDPR Article 34 - Communication to Data Subjects**:

[Organization] SHALL communicate breach to affected data subjects **without undue delay** when breach is likely to result in **high risk** to rights and freedoms of data subjects.

**High Risk Indicators**:
- Special category data compromised
- Large-scale breach affecting many data subjects
- Vulnerable data subjects affected (children, employees under duress)
- Breach enables identity theft or fraud
- Financial loss to data subjects likely
- Reputational damage to data subjects likely
- Loss of confidentiality of professional secrets

**Communication Content** (GDPR Art. 34(2)):

Communication to data subjects SHALL:
- Describe nature of breach in clear and plain language
- Provide name and contact details of DPO or other contact point
- Describe likely consequences of breach
- Describe measures taken or proposed to address breach and mitigate adverse effects

**Exceptions to Data Subject Notification** (GDPR Art. 34(3)):

Communication to data subjects NOT required if:
1. **Protective measures**: [Organization] had implemented appropriate technical and organizational measures (e.g., encryption, pseudonymization) rendering data unintelligible to unauthorized persons
2. **Subsequent measures**: [Organization] has taken subsequent measures ensuring high risk is no longer likely to materialize
3. **Disproportionate effort**: Would require disproportionate effort (public communication or similar measure may be used instead)

**FADP**: No explicit data subject notification requirement, but may be required under duty to inform or as part of mitigating harm.

#### 2.7.4 Breach Response Requirements

**Breach Detection and Assessment**:

[Organization] SHALL:
- Implement monitoring to detect potential breaches
- Assess incidents to determine if personal data breach occurred
- Assess likelihood and severity of risk to data subjects
- Document assessment and decision-making process

**Breach Containment and Remediation**:

[Organization] SHALL:
- Contain breach to prevent further unauthorized access/disclosure
- Recover compromised data where possible
- Implement remedial measures to prevent recurrence
- Document all actions taken

**Breach Notification Decision**:

[Organization] SHALL determine:
- **Supervisory authority notification required?** (GDPR: risk to data subjects, FADP: high risk)
- **Data subject notification required?** (GDPR: high risk to data subjects)
- **Notification timeline**: Within 72 hours for supervisory authority (GDPR), as quickly as possible (FADP)

**Breach Register**:

[Organization] SHALL maintain register of all data breaches including:
- Date and time of breach discovery
- Description of breach (nature, scope, affected data categories)
- Number of affected data subjects and records
- Assessment of risk to data subjects
- Notification decisions (authority, data subjects)
- Remedial actions taken
- Lessons learned and preventive measures implemented

**Integration with Incident Management**: Breach notification integrates with ISMS-POL-A.5.24-28 (Information Security Incident Management Framework).

**Implementation Reference**: ISMS-IMP-A.5.34.4 (Technical and Organizational Measures Assessment) includes breach detection, response, and notification procedures. ISMS-IMP-A.5.34.3 includes breach notification templates and communication procedures.

---

### 2.8 Technical and Organizational Measures (TOMs)

[Organization] SHALL implement appropriate technical and organizational measures to ensure level of security appropriate to the risk (GDPR Article 32, FADP Article 8).

#### 2.8.1 Security Measures Requirements

**Risk-Based Approach**:

[Organization] SHALL implement measures taking into account:
- State of the art
- Costs of implementation
- Nature, scope, context, and purposes of processing
- Risk of varying likelihood and severity to data subject rights and freedoms

**Technical Measures** (Examples - GDPR Art. 32(1)):

[Organization] SHALL consider implementing as appropriate:
1. **Pseudonymization and encryption** of personal data
2. **Confidentiality**: Ability to ensure ongoing confidentiality of processing systems and services
3. **Integrity**: Ability to ensure ongoing integrity of processing systems and services
4. **Availability**: Ability to ensure ongoing availability of processing systems and services
5. **Resilience**: Ability to ensure resilience of processing systems and services
6. **Recovery**: Process for regularly testing, assessing, and evaluating effectiveness of technical and organizational measures
7. **Restoration**: Ability to restore availability and access to personal data in timely manner after physical or technical incident

**Organizational Measures** (Examples):

[Organization] SHALL consider implementing as appropriate:
- Access controls and authorization procedures
- Data protection policies and procedures
- Staff training and awareness programs
- Vendor management and processor oversight
- Privacy impact assessments
- Data breach response procedures
- Data protection by design and by default
- Records of processing activities (ROPA)
- Regular audits and reviews

**Measures by Data Category**:

[Organization] SHALL implement enhanced measures for:
- **Special category data**: Encryption mandatory, strict access controls, enhanced logging, DPIA required
- **Criminal offense data**: Legal authorization verification, strict access controls, enhanced logging
- **Children's data**: Age verification mechanisms, parental consent management, child-appropriate communication

**Implementation Reference**: ISMS-IMP-A.5.34.4 (Technical and Organizational Measures Assessment) provides detailed checklist of security measures, implementation guidance, risk-based selection criteria.

Integration with existing ISMS controls:
- ISMS-POL-A.8.24 (Cryptography): Encryption requirements for PII
- ISMS-POL-A.5.15-16-18 (IAM): Access controls for PII
- ISMS-POL-A.8.10 (Information Deletion): Secure PII deletion
- ISMS-POL-A.8.11 (Data Masking): Pseudonymization techniques
- ISMS-POL-A.8.12 (DLP): PII leakage prevention

---

## 3. Roles and Responsibilities

### 3.1 Data Protection Officer (DPO) / Privacy Officer

**Role**: Independent privacy governance function responsible for monitoring privacy compliance, advising on data protection, and serving as contact point for supervisory authorities and data subjects.

**DPO Designation Requirement**:

**GDPR Article 37 - Mandatory DPO**:
- Processing carried out by public authority or body (except courts)
- Core activities require regular and systematic monitoring of data subjects on large scale
- Core activities consist of processing special categories (Art. 9) or criminal offense data (Art. 10) on large scale

**FADP**: No mandatory DPO requirement, but recommended best practice.

[Organization] determines DPO requirement based on GDPR applicability and organizational risk assessment.

**DPO Responsibilities** (GDPR Art. 39):
- Inform and advise controller, processor, and employees on GDPR/FADP obligations
- Monitor compliance with GDPR/FADP and [Organization] privacy policies
- Provide advice regarding Data Protection Impact Assessments (DPIAs)
- Cooperate with supervisory authorities
- Act as contact point for supervisory authorities and data subjects
- Maintain independence (no instructions regarding duties, no dismissal for performing duties)

**Privacy Officer** (if DPO not mandatory):
- Similar responsibilities to DPO but may have less regulatory protection for independence
- Serves as internal privacy governance lead

**Reporting Line**: DPO/Privacy Officer reports directly to highest management level. Must not receive any instructions regarding exercise of duties.

---

### 3.2 Data Controllers and Processors

**Data Controller** (GDPR Art. 4(7), FADP Art. 5(j)):

Natural or legal person, public authority, agency, or other body which, alone or jointly with others, **determines the purposes and means of processing** personal data.

**Controller Responsibilities**:
- Determine legal basis for processing
- Ensure compliance with data protection principles (GDPR Art. 5, FADP Art. 6)
- Implement Privacy by Design and by Default
- Conduct DPIAs where required
- Notify breaches to supervisory authority and data subjects
- Maintain ROPA
- Respond to data subject rights requests
- Select and oversee processors (GDPR Art. 28 agreements)
- Demonstrate accountability

---

**Data Processor** (GDPR Art. 4(8), FADP Art. 5(k)):

Natural or legal person, public authority, agency, or other body which **processes personal data on behalf of the controller**.

**Processor Responsibilities** (GDPR Art. 28):
- Process personal data only on documented instructions from controller
- Ensure persons authorized to process personal data are under confidentiality obligation
- Implement appropriate technical and organizational security measures
- Engage sub-processors only with controller authorization
- Assist controller in responding to data subject rights requests
- Assist controller in ensuring compliance with security, breach notification, DPIA obligations
- Delete or return personal data after end of provision of services (at controller's choice)
- Make available to controller all information necessary to demonstrate compliance
- Notify controller without undue delay after becoming aware of personal data breach

---

**Joint Controllers** (GDPR Art. 26):

When two or more controllers jointly determine purposes and means of processing, they are joint controllers.

**Requirements**:
- Transparent arrangement determining respective responsibilities for GDPR compliance
- Arrangement reflects respective roles and relationships with data subjects
- Data subjects can exercise rights against each controller

**Applicability**: [Organization] assesses whether arrangements with partners/affiliates constitute joint controllership and documents accordingly.

---

### 3.3 Data Owners and Stewards

**Data Owner**:

Business unit or function with accountability for a specific category of personal data or processing activity.

**Responsibilities**:
- Define purpose and legal basis for processing
- Classify data according to sensitivity
- Determine retention requirements
- Authorize access to data
- Ensure compliance with this policy for their data domain
- Coordinate with DPO on privacy assessments

**Data Steward**:

Operational role responsible for day-to-day data management and quality.

**Responsibilities**:
- Maintain data accuracy and completeness
- Execute data subject rights requests
- Monitor data quality and integrity
- Report issues to Data Owner and DPO
- Implement data protection controls

---

### 3.4 Chief Information Security Officer (CISO)

**CISO Responsibilities** (Privacy-Related):
- Implement technical security controls for PII protection
- Conduct security risk assessments for processing activities
- Provide technical input to DPIAs
- Lead data breach response (technical containment and remediation)
- Oversee access controls and encryption for PII
- Coordinate with DPO on security aspects of privacy compliance

---

### 3.5 Legal / Compliance Officer

**Legal/Compliance Responsibilities**:
- Provide legal interpretation of GDPR, FADP, and other privacy regulations
- Review and approve processor agreements (GDPR Art. 28 contracts)
- Review and approve cross-border transfer mechanisms (SCCs, BCRs)
- Assess regulatory applicability per ISMS-POL-00
- Support DPO in regulatory interactions
- Provide guidance on data subject rights requests with legal complexity

---

### 3.6 Human Resources (HR)

**HR Responsibilities** (Employee PII):
- Ensure lawful basis for processing employee personal data (typically contract + legal obligation)
- Provide employee privacy notices
- Manage employee data subject rights requests
- Coordinate with Works Council / employee representatives on privacy matters (where applicable)
- Ensure employment contracts include data protection clauses
- Manage employee training on privacy compliance

---

### 3.7 All Personnel

**Universal Responsibilities**:
- Comply with this policy and related privacy procedures
- Complete mandatory privacy training
- Handle personal data only for authorized purposes
- Report suspected data breaches or privacy violations immediately
- Respect data subject privacy rights
- Maintain confidentiality of personal data

---

## 4. Governance, Review, and Documentation

### 4.1 Privacy Governance Framework

**Privacy Governance Structure**:

[Organization] establishes privacy governance through:
- **Executive Sponsor**: Executive Management (CEO or designated C-level)
- **Privacy Officer / DPO**: Independent privacy governance lead
- **Privacy Steering Committee**: Cross-functional committee (DPO, CISO, Legal, HR, IT, Business Representatives) meeting quarterly
- **Data Owners**: Business unit accountability for specific data domains
- **Implementation Teams**: Operational teams executing privacy controls

**Governance Activities**:
- **Quarterly**: Privacy Steering Committee meetings, review of privacy metrics, DSR volume and timeliness, breach incidents
- **Annual**: Privacy program review, policy updates, ROPA validation, training effectiveness assessment
- **Ad Hoc**: DPIA reviews, processor assessments, incident response, regulatory change impact assessments

---

### 4.2 Privacy Metrics and Reporting

**Key Privacy Indicators**:

[Organization] tracks and reports:
- **Data Subject Rights Requests**: Volume, type, response time, completion rate
- **Data Breaches**: Number of breaches, severity, notification compliance, remediation status
- **DPIAs**: Number completed, high-risk findings, mitigation status
- **Consent Management**: Consent rates, withdrawal rates, consent refresh completions
- **Training Compliance**: Completion rates, assessment scores
- **Audit Findings**: Number of findings, remediation status, overdue findings
- **Processor Compliance**: Number of processors, Art. 28 contract coverage, assessment completion

**Reporting Frequency**:
- **Monthly**: DSR volume, breach incidents (to Privacy Steering Committee)
- **Quarterly**: Comprehensive privacy metrics dashboard (to Executive Management)
- **Annual**: Privacy program maturity assessment, regulatory compliance status (to Board / Executive Management)

**Escalation Thresholds**:
- Data breach with high risk to data subjects → Immediate escalation to Executive Management
- Supervisory authority inquiry or investigation → Immediate escalation to Executive Management and Legal
- Systemic non-compliance identified → Escalation to Privacy Steering Committee within 48 hours

---

### 4.3 Policy Review and Updates

**Review Cycle**: Annual (minimum)

**Review Triggers**:
- Regulatory changes (GDPR amendments, FADP updates, new sector-specific regulations)
- Significant changes in processing activities (new products/services, M&A, major system implementations)
- Data breaches revealing policy gaps
- Supervisory authority guidance or enforcement actions
- Internal audit findings
- Technological changes affecting privacy (new privacy-enhancing technologies, new threats)

**Review Process**:
1. DPO initiates review (scheduled annual OR triggered by event)
2. Cross-functional review (DPO, Legal, CISO, HR, Data Owners)
3. Stakeholder consultation (employee representatives, customer advisory board - where appropriate)
4. Draft updates prepared with tracked changes
5. Legal/DPO review and approval
6. Executive Management approval
7. Communication and training on changes
8. Version control and distribution

**Version Control**:
- Major policy changes: Version increment (e.g., 1.0 → 2.0)
- Minor updates or clarifications: Sub-version increment (e.g., 1.0 → 1.1)
- Version history maintained in Document Control section

---

### 4.4 Training and Awareness

**Mandatory Privacy Training**:

[Organization] SHALL provide privacy training to:
- **All Employees**: Annual general privacy awareness training (GDPR/FADP principles, data subject rights, breach reporting, acceptable use of PII)
- **Employees Handling PII Regularly**: Role-specific training (DSR handling, consent management, data minimization, security practices)
- **Employees Handling Special Category Data**: Enhanced training (legal basis requirements, security obligations, breach sensitivity)
- **New Hires**: Privacy training during onboarding (within 30 days of hire)
- **Developers and System Owners**: Privacy by Design training (technical controls, privacy-enhancing technologies, DPIA process)
- **Managers**: Privacy governance training (accountability, oversight responsibilities, escalation procedures)

**Training Content**:
- Applicable privacy regulations (GDPR, FADP, sector-specific)
- [Organization] privacy policies and procedures
- Data subject rights and request handling
- Breach identification and reporting
- Secure handling of PII (access controls, encryption, data minimization)
- Consent management and legal basis requirements
- Cross-border transfer restrictions
- Vendor and processor management
- Consequences of non-compliance

**Training Delivery**:
- E-learning modules (annual refresh for all employees)
- In-person workshops (for high-risk roles)
- On-demand resources (intranet, knowledge base)
- Awareness campaigns (privacy week, breach awareness month)

**Training Tracking**:
- Completion tracked in learning management system
- Compliance reported to Privacy Steering Committee quarterly
- Non-completion escalated to management

---

### 4.5 Audits and Assessments

**Internal Audits**:

[Organization] SHALL conduct internal privacy audits:
- **Frequency**: Annual (minimum) or as required by risk assessment
- **Scope**: Compliance with this policy, GDPR/FADP requirements, effectiveness of privacy controls
- **Audit Activities**: ROPA accuracy review, DSR handling review, consent record verification, processor agreement review, DPIA completion verification, breach notification testing

**External Audits**:
- ISO/IEC 27001:2022 certification audits (Control A.5.34)
- ISO/IEC 27701:2019 certification audits (if pursued)
- Regulatory audits (supervisory authority inspections)
- Third-party privacy assessments (customer/partner requirements)

**Assessment Framework**:

[Organization] assesses privacy compliance through:
- ISMS-IMP-A.5.34 assessment workbook suite (7 workbooks covering all privacy domains)
- Privacy maturity model assessment (annually)
- Gap analysis against regulatory requirements (GDPR, FADP, sector-specific)
- Control effectiveness testing (quarterly for high-risk controls)

**Audit Findings Management**:
- Findings logged in ISMS corrective action tracking system
- Risk-rated (critical, high, medium, low)
- Assigned to responsible owner with remediation deadline
- Tracked to closure through Privacy Steering Committee
- Overdue critical/high findings escalated to Executive Management

---

### 4.6 Documentation Requirements

**Required Documentation** (GDPR Art. 5(2) Accountability Principle):

[Organization] SHALL maintain documented information including:
- **This Policy** (ISMS-POL-A.5.34)
- **Implementation Procedures** (ISMS-IMP-A.5.34.1-.7)
- **Record of Processing Activities** (ROPA)
- **Data Protection Impact Assessments** (DPIAs)
- **Legitimate Interest Assessments** (LIAs)
- **Processor Agreements** (GDPR Art. 28 contracts)
- **Standard Contractual Clauses** (cross-border transfers)
- **Transfer Impact Assessments** (Schrems II compliance)
- **Consent Records** (consent text, consents given, withdrawals)
- **Data Subject Rights Requests** (requests, responses, decisions)
- **Data Breach Register** (all breaches, notifications, remedial actions)
- **Privacy Training Records** (completion, assessments, attendance)
- **Privacy Audit Reports** (internal/external audits, findings, remediation)
- **Privacy Notices** (customer, employee, website, app)
- **Data Flow Diagrams** (PII movement through systems)

**Documentation Retention**:
- Retain privacy documentation for duration of processing PLUS applicable statutory retention period
- Minimum retention: 3 years after cessation of processing (GDPR statute of limitations)
- Longer retention may be required by sector-specific regulations or legal hold

**Documentation Access**:
- Available to supervisory authorities upon request
- Available to data subjects exercising access rights (where applicable)
- Restricted access for confidentiality and security (not public disclosure)

---

### 4.7 Integration with ISMS

**This Policy Integrates with ISMS**:

**Risk Assessment** (ISO 27001 Clause 6.1):
- Privacy controls selected based on [Organization]'s risk assessment identifying PII processing risks
- Risk treatment plans document privacy control implementation, residual risks, and acceptance
- Privacy risks incorporated into organizational risk register

**Statement of Applicability** (ISO 27001 Clause 6.1.3):
- Control A.5.34 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported
- Control effectiveness measured through assessment workbooks

**Related ISMS Policies and Controls**:

See Section 5 (Integration with Other Controls) for detailed integration points.

---

## 5. Integration with Other Controls

This policy integrates with the following ISMS controls:

### 5.1 Organizational Controls (Section 5)

**A.5.7 (Threat Intelligence)**:
- **Integration**: Privacy threat monitoring (tracking emerging privacy attack vectors, data broker activities, dark web monitoring for leaked PII)
- **Reference**: Threat intelligence feeds include privacy-specific threats

**A.5.9 (Inventory of Information and Assets)**:
- **Integration**: PII-containing assets identified in asset inventory, cross-referenced with ROPA
- **Reference**: Asset classification includes PII category identification

**A.5.10 (Acceptable Use of Information and Other Associated Assets)**:
- **Integration**: AUP includes PII handling requirements (authorized use only, no personal use of work data, no unauthorized sharing)
- **Reference**: AUP violations involving PII escalated as privacy incidents

**A.5.12 (Classification of Information)**:
- **Integration**: Information classification scheme includes PII categories (Basic PII, Sensitive PII, Criminal Offense Data), classification drives protection requirements
- **Reference**: Section 2.1 PII classification aligns with A.5.12

**A.5.15-16-18 (Identity and Access Management)**:
- **Integration**: Access controls enforce least privilege for PII access, access reviews verify PII access appropriateness, joiner/mover/leaver processes ensure timely PII access removal
- **Reference**: Access control requirements for PII defined in this policy Section 2.8

**A.5.19-23 (Information Security in Supplier Relationships)**:
- **Integration**: Processor agreements (GDPR Art. 28) required for all vendors processing PII, vendor risk assessments include privacy evaluation, vendor security requirements include PII protection
- **Reference**: Processor selection criteria include privacy compliance verification

**A.5.24-28 (Information Security Incident Management)**:
- **Integration**: Data breach response procedures integrated with incident management framework, breach notification timelines tracked through incident system, privacy incidents escalated to DPO
- **Reference**: Section 2.7 breach notification procedures integrate with A.5.24-28

**A.5.33 (Protection of Records)**:
- **Integration**: Retention schedules consider data minimization and storage limitation principles, deletion schedules enforce GDPR/FADP retention limits
- **Reference**: Retention policies must comply with privacy storage limitation principle

---

### 5.2 People Controls (Section 6)

**A.6.1 (Screening)**:
- **Integration**: Background checks for employees with PII access (proportionate to risk and privacy-compliant)
- **Reference**: Screening procedures respect privacy of candidates

**A.6.2 (Terms and Conditions of Employment)**:
- **Integration**: Employment contracts include confidentiality clauses covering PII, data protection obligations, consequences of privacy violations
- **Reference**: Employee handbook includes privacy responsibilities

**A.6.3 (Information Security Awareness, Education and Training)**:
- **Integration**: Privacy training mandatory for all employees, role-specific training for PII handlers
- **Reference**: Section 4.4 training requirements

**A.6.4 (Disciplinary Process)**:
- **Integration**: Privacy violations subject to disciplinary action up to and including termination
- **Reference**: Consequences proportionate to severity and intentionality

**A.6.6 (Confidentiality or Non-Disclosure Agreements)**:
- **Integration**: NDAs with employees, contractors, vendors include PII protection obligations
- **Reference**: Confidentiality extends beyond employment/engagement termination

---

### 5.3 Physical Controls (Section 7)

**A.7.14 (Secure Disposal or Re-use of Equipment)**:
- **Integration**: Equipment containing PII securely sanitized before disposal or re-use
- **Reference**: Sanitization standards appropriate for PII sensitivity (enhanced for special category data)

---

### 5.4 Technological Controls (Section 8)

**A.8.2 (Privileged Access Rights)**:
- **Integration**: Privileged access to PII databases strictly controlled, enhanced logging and monitoring
- **Reference**: Privileged users with PII access subject to additional training and oversight

**A.8.3 (Information Access Restriction)**:
- **Integration**: Access to PII restricted based on business need-to-know, technical enforcement (network segmentation, database access controls, application-level authorization)
- **Reference**: Access restrictions implement least privilege for PII

**A.8.5 (Secure Authentication)**:
- **Integration**: Strong authentication required for systems processing PII, MFA required for remote access to PII systems
- **Reference**: Authentication strength commensurate with PII sensitivity

**A.8.10 (Information Deletion)**:
- **Integration**: Secure deletion methods for PII implement right to erasure, deletion verification procedures ensure compliance
- **Reference**: Section 2.3.3 right to erasure integrates with A.8.10 deletion procedures

**A.8.11 (Data Masking)**:
- **Integration**: Pseudonymization and anonymization techniques protect PII in non-production environments, masking protects PII in test data, analytics, reporting
- **Reference**: Section 2.4 Privacy by Design references data masking as protective measure

**A.8.12 (Data Leakage Prevention)**:
- **Integration**: DLP policies detect and prevent unauthorized PII disclosure, DLP monitors PII in emails, file transfers, cloud uploads
- **Reference**: DLP rules based on PII classification (Section 2.1)

**A.8.16 (Monitoring Activities)**:
- **Integration**: Monitoring detects unauthorized PII access or suspicious activity, audit logs support breach detection and DSR fulfillment
- **Reference**: Monitoring respects employee privacy (proportionate, transparent, compliant with local law)

**A.8.23 (Web Filtering)**:
- **Integration**: Web filtering prevents access to malicious sites that could compromise PII
- **Reference**: Filtering logs may contain user activity data (subject to privacy analysis)

**A.8.24 (Use of Cryptography)**:
- **Integration**: Encryption at rest and in transit mandatory for sensitive PII, encryption renders PII unintelligible if breached (reduces breach impact)
- **Reference**: Section 2.8 TOMs require encryption for special category data

**A.8.25-26-29 (Secure Development)**:
- **Integration**: Privacy by Design integrated into SDLC, privacy requirements in design specifications, privacy testing in QA
- **Reference**: Section 2.4 Privacy by Design applies to all system development

---

## Annex A: Data Subject Rights Request Decision Matrix

**Purpose**: Provide decision framework for assessing and responding to data subject rights requests.

**Usage**: Use this matrix to determine appropriate response to DSR. Consult ISMS-IMP-A.5.34.3 for detailed procedures.

| Right | Legal Basis | Exceptions | Response Timeline | Key Considerations |
|-------|-------------|------------|-------------------|-------------------|
| **Access (Art. 15)** | Unconditional right | Manifestly unfounded/excessive, affects others' rights | GDPR: 1 month (extendable to 3), FADP: Reasonable time | Verify identity, provide machine-readable format if electronic, first copy free |
| **Rectification (Art. 16)** | Unconditional right | None (but may challenge accuracy claim) | GDPR: 1 month (extendable to 3), FADP: Without undue delay | Correct in all systems, notify recipients, burden on data subject to prove inaccuracy |
| **Erasure (Art. 17)** | Conditional (grounds must exist) | Legal obligation, legal claims, freedom of expression, public interest, archiving | GDPR: 1 month (extendable to 3), FADP: Without undue delay | Assess grounds, check exceptions, immediate production deletion, best-effort backup deletion |
| **Portability (Art. 20)** | Only for consent or contract + automated processing | Not applicable to other legal bases, paper records | GDPR: 1 month (extendable to 3), N/A for FADP | Structured format (JSON/CSV/XML), only "provided by" data, no derived/inferred data |
| **Object (Art. 21(1))** | Only for legitimate interest or public task | Compelling legitimate grounds override, legal claims | GDPR: 1 month (extendable to 3), Similar under FADP | Stop processing unless can demonstrate compelling grounds, burden on controller |
| **Object - Marketing (Art. 21(2))** | Unconditional (absolute right) | None | Immediate (24-48 hours) | Must stop all direct marketing, maintain suppression list, no justification can override |
| **Restriction (Art. 18)** | Conditional (grounds must exist) | None if grounds met | GDPR: 1 month (extendable to 3), N/A explicitly for FADP | Flag records, storage allowed but no processing except with consent or for legal claims |

**Notes**:
- **Manifestly Unfounded/Excessive**: Repetitive requests, clearly frivolous, intended to harass. Must justify refusal.
- **Identity Verification**: Proportionate to risk. Higher verification for sensitive data access/erasure.
- **Fee**: Only for repetitive requests or additional copies. First access request always free.
- **Extendable Timeline**: Inform data subject within 1 month if extending, explain reason, cannot extend beyond 3 months total.

---

## Annex B: DPIA Trigger Assessment

**Purpose**: Determine whether Data Protection Impact Assessment (DPIA) is required for a processing activity.

**Usage**: Answer questions below. If answer is "YES" to any question in Mandatory Triggers section, DPIA is required. If answer is "YES" to 2+ questions in Risk Indicators section, DPIA is strongly recommended.

**Mandatory DPIA Triggers** (GDPR Art. 35(3)):

| # | Trigger Question | Details |
|---|-----------------|---------|
| 1 | Does processing involve **systematic and extensive evaluation** of personal aspects based on **automated processing** (including profiling) on which decisions are based that produce **legal effects** or **similarly significantly affect** the individual? | Examples: Credit scoring, automated loan decisions, employee performance evaluation algorithms, automated insurance underwriting, algorithmic pricing affecting individuals |
| 2 | Does processing involve **large-scale processing** of **special category data** (GDPR Art. 9) or **criminal offense data** (GDPR Art. 10)? | Special categories: racial/ethnic origin, political opinions, religious beliefs, trade union membership, genetic data, biometric data (for unique identification), health data, sex life/sexual orientation data. Large-scale: Significant number of data subjects OR significant volume of data OR extensive geographical area |
| 3 | Does processing involve **systematic monitoring of a publicly accessible area on a large scale**? | Examples: CCTV surveillance of public streets, facial recognition in public spaces, large-scale location tracking |

**If "YES" to any above → DPIA is MANDATORY**

---

**High-Risk Indicators** (2+ "YES" → DPIA strongly recommended):

| # | Risk Indicator | Details |
|---|---------------|---------|
| 4 | Does processing involve **evaluation or scoring** of individuals (including profiling and predicting aspects)? | Examples: Creditworthiness, work performance, health status, reliability, behavior, location |
| 5 | Does processing involve **automated decision-making with legal or similarly significant effects**? | Automated decisions without human review that significantly affect individuals |
| 6 | Does processing involve **systematic monitoring** of individuals? | Tracking, observing, monitoring, surveillance |
| 7 | Does processing involve **sensitive data** or data of highly personal nature? | Beyond Art. 9 special categories: financial data, location data, communications content |
| 8 | Does processing involve data of **vulnerable data subjects**? | Children, employees, elderly, patients, asylum seekers (imbalance of power) |
| 9 | Does processing involve **large-scale processing**? | Processing affecting large number of data subjects, large volume of data, or wide geographical area |
| 10 | Does processing involve **matching or combining datasets** from different sources? | Combining datasets in ways unexpected by data subjects |
| 11 | Does processing involve data concerning **individuals who have not provided data directly**? | Data obtained from data brokers, scraped from public sources, inferred from other data |
| 12 | Does processing involve **tracking of individuals' location or behavior**? | GPS tracking, online behavioral tracking, movement monitoring |
| 13 | Does processing prevent individuals from **exercising a right, using a service, or performing a contract**? | Data subjects have no genuine choice, cannot opt out without detriment |
| 14 | Does processing involve **innovative use or application** of new technological or organizational solutions? | New technology, new use of existing technology, or novel processing method |
| 15 | Does processing involve **cross-border data transfers** outside of adequate jurisdictions without appropriate safeguards? | Transfers to third countries without adequacy decision or SCCs |

**If "YES" to 2 or more indicators (4-15) → DPIA is STRONGLY RECOMMENDED**

---

**DPIA Decision**:

- **Mandatory Triggers** (Questions 1-3): Any "YES" → Conduct DPIA before processing
- **High-Risk Indicators** (Questions 4-15): 2+ "YES" → Strongly recommend DPIA
- **Low Risk**: All "NO" or only 1 "YES" in indicators → DPIA not required (document assessment)

**Exception**: If processing is similar to previously assessed processing with DPIA already completed, may reference existing DPIA instead of conducting new one (verify processing characteristics are truly similar).

**Next Steps**:
- If DPIA required: Follow ISMS-IMP-A.5.34.5 (DPIA Assessment) procedures
- If DPIA not required: Document assessment and retain in privacy assessment records

---

**END OF POLICY DOCUMENT**

---

*This policy establishes privacy and PII protection requirements. Implementation procedures are documented in ISMS-IMP-A.5.34 suite. Regulatory context is available in ISMS-CTX-A.5.34.*