**ISMS-POL-A.8.11 — Data Masking**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Data Masking |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.11 |
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
- Secondary: Chief Information Officer (CIO)
- Privacy: Data Protection Officer (DPO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.11.1-UG/TG (Data Inventory & Classification Assessment)
- ISMS-IMP-A.8.11.2-UG/TG (Masking Technique Selection & Requirements)
- ISMS-IMP-A.8.11.3-UG/TG (Environment Coverage Assessment)
- ISMS-IMP-A.8.11.4-UG/TG (Testing & Validation Framework)
- ISMS-IMP-A.8.11.5-UG/TG (Compliance Dashboard)
- ISMS-CTX-A.8.11 (Data Masking Technical Reference - Technical Reference Only)
- ISO/IEC 27001:2022 Control A.8.11

---

## Executive Summary

This policy establishes [Organization]'s requirements for data masking controls to protect sensitive information confidentiality in accordance with ISO/IEC 27001:2022 Control A.8.11.

**Scope**: This policy applies to all sensitive data categories (PII, financial, health, credentials, proprietary) across all environments (production, test, development, analytics, training, backup); all masking techniques (redaction, substitution, tokenization, pseudonymization, anonymization); and all organizational personnel, contractors, and third parties handling sensitive data.

**Purpose**: Define organizational requirements for data masking control implementation and governance. This policy establishes WHAT data requires masking, WHICH techniques are approved, and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8.11 (UG/TG variants).

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (PCI DSS, HIPAA, FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

---

# Control Alignment & Scope

## ISO/IEC 27001:2022 Control A.8.11

**ISO/IEC 27001:2022 Annex A.8.11 - Data Masking**

> *Data masking should be used in accordance with the organization's topic-specific policy on access control and other related topic-specific policies, and business requirements, taking applicable legislation into consideration.*

**Control Objective**: Establish organizational policy for data masking controls protecting sensitive information confidentiality by obscuring data when full visibility is not required for legitimate business purposes.

**This Policy Addresses**:

- Data classification requirements determining what data requires masking
- Approved masking technique standards and selection criteria
- Environment-specific masking coverage requirements (production, non-production)
- Testing and validation requirements ensuring masking effectiveness
- Organizational roles and responsibilities for data masking governance
- Exception and incident management frameworks
- Integration with [Organization]'s risk assessment and treatment processes

## What This Policy Does

This policy:

- **Defines** data masking requirements aligned with data classification and organizational risk appetite
- **Establishes** governance framework for data masking decision-making and accountability
- **Specifies** approved masking techniques and selection criteria
- **References** applicable regulatory requirements per ISMS-POL-00
- **Identifies** organizational roles and responsibilities for masking controls

## What This Policy Does NOT Do

This policy does NOT:

- **Specify masking tool vendors or products** (technology selection based on [Organization]'s risk assessment)
- **Define specific masking configurations** (see ISMS-IMP-A.8.11 Implementation Guides)
- **Provide system-specific procedures** (see ISMS-IMP-A.8.11 Assessment Guides)
- **Replace data classification policy** (masking builds on existing classification scheme per A.5.12)
- **Establish data retention schedules** (covered by data retention policy per A.8.10)
- **Define access control mechanisms** (covered by access control policies per A.5.15, A.8.3)
- **Replace cryptographic controls** (encryption covered by A.8.24 Cryptography Policy)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite evolving masking technologies and tool landscape
- Technical agility for tool updates and technique improvements without policy revision
- Clear distinction between governance (WHAT/WHO) and execution (HOW)
- Focused audit scope (auditors audit policy compliance, not technical implementation details)

## Scope

**This policy applies to**:

- All sensitive data categories:
  - Personally Identifiable Information (PII)
  - Financial data (account numbers, payment card data, transaction details)
  - Health information (medical records, diagnoses, treatment data)
  - Authentication credentials (passwords, tokens, API keys, secrets)
  - Proprietary business information (trade secrets, strategic data, pricing)
  - Any data classified as Confidential or Restricted per [Organization]'s classification scheme
- All environments where sensitive data exists:
  - Production systems (where masking is operationally appropriate)
  - Test and QA environments
  - Development environments
  - Analytics and reporting systems
  - Training and demonstration environments
  - Sandbox and experimental environments
  - Backup and archive systems
  - Data warehouses and data lakes
- All masking use cases:
  - Data provisioning for non-production use
  - Report generation and distribution
  - Data sharing with third parties
  - Application development and testing
  - Machine learning model training
  - User acceptance testing (UAT)
  - Analytics and business intelligence
- All organizational personnel and third parties:
  - Employees handling sensitive data
  - Contractors and consultants
  - Third-party service providers
  - Outsourced development teams
  - Cloud service providers processing organizational data

**Out of Scope**:

- Public information (unclassified data requiring no masking)
- Data classified as "Public" per [Organization]'s classification scheme (masking provides no protection value)
- Encrypted data protection (covered under A.8.24 Cryptography Policy - masking and encryption serve different purposes)
- Data deletion and destruction (covered under A.8.10 Information Deletion)
- Network-level access controls (covered under A.8.20 Networks Security)
- Application-level access controls (covered under A.8.3 Access Restriction)

**Note**: Out-of-scope items do not exempt systems from assessment. Assessment determines applicability; exclusion is documented with business justification.

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**. 

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Data Masking Requirements |
|------------|---------------|-------------------------------|
| **Swiss nDSG** | All Swiss operations | Art. 8 - Data protection by design including data minimization; Art. 25 - Appropriate technical and organizational measures for personal data protection |
| **EU GDPR** | When processing EU personal data | Art. 5(1)(c) - Data minimization principle; Art. 25 - Data protection by design and default; Art. 32 - Security of processing including pseudonymization; Art. 89 - Safeguards for research/statistics including pseudonymization |
| **ISO/IEC 27001:2022** | Certification scope | Control A.8.11 - Documented data masking policy, implemented controls, evidence of effectiveness |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Data Masking Requirements |
|-----------|-------------------|---------------------------|
| **PCI DSS v4.0** | Processing payment card data | Req. 3.4 - PAN rendered unreadable (masking, truncation, hashing, tokenization); Req. 3.5 - Primary Account Number (PAN) masked when displayed (minimum first 6 and last 4 digits); Req. 12.3 - Data usage policies for non-production environments |
| **HIPAA Privacy Rule** | US healthcare data (ePHI) | §164.514(a)-(b) - De-identification standards (Expert Determination or Safe Harbor method); §164.514(c) - Re-identification prohibition; §164.530(c) - Administrative safeguards for de-identified data |
| **FINMA** | Swiss regulated financial institution | Technical and organizational measures per risk assessment; client data protection requirements; outsourcing risk management (FINMA Circular 2018/3) |
| **DORA** | EU financial services entity (ICT risk) | Art. 9 - ICT risk management framework including data protection controls; Art. 28 - ICT third-party risk management including data security |
| **NIS2** | Essential/important entity (EU) | Art. 21 - Cybersecurity risk management measures including data security; Data minimization and pseudonymization for risk reduction |
| **ISO/IEC 27701** | Privacy extension (if implemented) | Control 7.2.2 - Identify basis for PII processing; Control 7.3.2 - Determine PII de-identification and deletion; Control 7.4.5 - PII de-identification and deletion processes |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- NIST SP 800-188 (De-Identifying Government Datasets)
- ISO/IEC 20889:2018 (Privacy Enhancing Data De-identification Terminology and Classification)
- CIS Controls v8 (Control 3.3: Data Protection - Configure data access control lists)
- OWASP Data Security Cheat Sheet
- Cloud Security Alliance (CSA) guidance on cloud data protection

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent requirements apply where multiple regulations overlap. Tier 2 applicability is documented in [Organization]'s regulatory compliance register and reviewed annually.

---

# Data Masking Requirements Framework

## Data Classification and Identification Requirements

[Organization] implements data classification as the foundation for data masking decisions.

**Data Classification Alignment**:

Data masking requirements SHALL align with [Organization]'s information classification policy (per Control A.5.12).

| [Organization] Classification | Masking Requirement | Rationale |
|-------------------------------|---------------------|-----------|
| **Restricted** | Mandatory masking in ALL non-production environments | Highest sensitivity - exposure causes severe harm |
| **Confidential** | Mandatory masking in non-production; risk-based in production | High sensitivity - exposure causes substantial harm |
| **Internal** | Risk-based masking where PII or regulatory requirements apply | Moderate sensitivity - selective masking based on content |
| **Public** | No masking required | No confidentiality requirement |

**Sensitive Data Categories**:

The following data categories SHALL be assessed for masking requirements:

| Category | Description | Examples | Typical Sensitivity |
|----------|-------------|----------|---------------------|
| **Personally Identifiable Information (PII)** | Data identifying individuals directly or indirectly | Name, SSN/AHV, passport, email, phone, address | Restricted/Confidential |
| **Financial Data** | Payment and financial account information | Credit card (PAN), IBAN, account balance, salary, tax ID | Restricted/Confidential |
| **Health Information** | Medical and health data | Medical record number, diagnoses, prescriptions, lab results | Restricted (GDPR Art. 9) |
| **Authentication Credentials** | Access and authentication data | Passwords, API keys, tokens, private keys, connection strings | Restricted |
| **Proprietary Business Data** | Business-sensitive information | Trade secrets, pricing strategies, customer contracts | Confidential |
| **Special Categories** | GDPR Article 9 special category data | Racial/ethnic origin, political opinions, religious beliefs, biometric/genetic data | Restricted |

**Data Discovery Requirements**:

[Organization] SHALL maintain inventory of sensitive data requiring masking:

- Systems and databases containing sensitive data
- Data elements (tables, columns, fields) requiring masking
- Data classification per element
- Data owner responsible for masking decisions
- Applicable regulatory requirements per data category

**Implementation Note**: Data discovery methodology, data inventory procedures, and classification assessment tools are documented in ISMS-IMP-A.8.11-1 (Data Inventory & Classification Assessment). Technical guidance on data discovery techniques is provided in ISMS-CTX-A.8.11 (Technical Reference - NOT ISMS).

**Data Owner Accountability**:

Data Owners SHALL:

- Classify data per [Organization]'s classification scheme
- Determine masking requirements based on data sensitivity and business need
- Approve masking techniques for their data domains
- Review and approve exceptions to masking requirements
- Validate masking effectiveness for their data

## Masking Technique Standards

[Organization] implements approved masking techniques selected based on data type, use case, and regulatory requirements.

**Approved Masking Techniques**:

The following masking technique categories are approved for use:

| Technique Category | Description | Reversibility | Primary Use Cases |
|--------------------|-------------|---------------|-------------------|
| **Static Data Masking (SDM)** | Permanent replacement of data in non-production databases | Irreversible | Non-production environments, external data sharing |
| **Dynamic Data Masking (DDM)** | Real-time masking based on user role at query time | N/A (original data unchanged) | Production role-based access, compliance scenarios |
| **Redaction/Nullification** | Complete removal or placeholder replacement | Irreversible | Reports, exports, screenshots |
| **Substitution** | Replacement with realistic fictitious data | Irreversible | Test data generation, maintaining data utility |
| **Tokenization** | Replacement with tokens; original in secure vault | Reversible with vault | Payment systems, referential integrity requirements |
| **Pseudonymization** | Replacement with pseudonyms; re-identifiable with key | Reversible with key | GDPR compliance, research/analytics |
| **Anonymization** | Irreversible removal of all identifying information | Irreversible | Public data release, statistical analysis |

**Technique Selection Criteria**:

Masking technique selection SHALL consider:

- **Data sensitivity classification**: Higher sensitivity requires stronger masking
- **Regulatory requirements**: GDPR pseudonymization vs. anonymization, PCI DSS masking rules
- **Business use case**: Development/testing vs. analytics vs. external sharing
- **Reversibility requirements**: Legitimate need to recover original data
- **Format preservation**: Maintaining data format for application compatibility
- **Referential integrity**: Cross-table relationships and foreign keys
- **Performance impact**: Real-time vs. batch masking considerations

**Prohibited Practices**:

The following practices are NOT acceptable as masking techniques:

- Simple character substitution without randomization (predictable patterns)
- ROT13 or Caesar cipher (trivially reversible)
- Reversible encoding (Base64, URL encoding) without encryption
- Production data in non-production without any masking (policy violation)
- Self-generated "masking" without validated technique (cargo cult security)

**Technique Approval**:

New masking techniques or significant modifications to approved techniques SHALL:

- Be proposed to Security Team with technical justification
- Undergo security review and testing
- Be approved by CISO before production use
- Be documented in technique inventory (ISMS-IMP-A.8.11-2)

**Implementation Note**: Detailed technique specifications, algorithm parameters, and configuration guidance are provided in ISMS-CTX-A.8.11 (Data Masking Technical Reference - NOT ISMS). Technique selection and implementation assessment is documented in ISMS-IMP-A.8.11-2 (Masking Technique Selection & Requirements Assessment).

## Environment Coverage Requirements

[Organization] implements masking controls to achieve appropriate coverage across all environments processing sensitive data.

**Coverage Principle**: Sensitive data SHALL be masked in environments where full data visibility is not required for legitimate business operations.

**Environment-Specific Requirements**:

| Environment | Masking Requirement | Rationale | Exceptions |
|-------------|---------------------|-----------|------------|
| **Production** | Risk-based; mask where operationally feasible | Business operations require some real data | Document business justification for unmasked data |
| **Test/QA** | Mandatory for Restricted/Confidential data | No business need for real sensitive data | Requires CISO approval with compensating controls |
| **Development** | Mandatory for Restricted/Confidential data | Developers do not need real sensitive data | Requires CISO approval with compensating controls |
| **Analytics/BI** | Mandatory unless aggregated or anonymized | Analytics can function with masked data | Aggregate reporting may not require masking |
| **Training** | Mandatory for ALL sensitive data | Training must use non-sensitive data | No exceptions |
| **Sandbox/Experimental** | Mandatory for ALL sensitive data | Experimental environments are high-risk | No exceptions |
| **Backup/Archive** | Same protection as source environment | Backups mirror source data sensitivity | N/A - follows source requirements |

**Coverage Verification**:

[Organization] SHALL verify masking coverage through:

- Environment inventory documenting all systems with sensitive data access
- Coverage gap analysis identifying unprotected sensitive data
- Technical testing validating masking implementation
- Regular assessment (annual minimum, quarterly for high-risk systems)

**Production Environment Masking**:

In production environments, masking MAY be implemented where:

- Role-based access requires some users see masked data (DDM)
- Reports or exports to external parties require masking
- Compliance requirements mandate masking (e.g., PCI DSS display rules)
- User interfaces display sensitive data to unauthorized personnel

Production masking does NOT replace access controls but provides defense in depth.

**Implementation Note**: Environment coverage assessment methodology, inventory procedures, and gap analysis tools are documented in ISMS-IMP-A.8.11-3 (Environment Coverage Assessment).

## Testing and Validation Requirements

[Organization] validates masking effectiveness to ensure sensitive data protection.

**Testing Requirements**:

Masking implementations SHALL be tested for:

| Test Type | Purpose | Frequency | Success Criteria |
|-----------|---------|-----------|------------------|
| **Effectiveness Testing** | Verify original data is obscured | Before production deployment, after changes | Original data not recoverable, masked data maintains format |
| **Referential Integrity Testing** | Verify cross-table relationships preserved | Before production deployment | Foreign key relationships intact, joins function correctly |
| **Format Validation Testing** | Verify data format and validation rules | Before production deployment | Masked data passes application validation rules |
| **Performance Testing** | Verify acceptable performance impact | Before production deployment for DDM | Masking overhead within acceptable limits (<10% typically) |
| **Re-identification Risk Assessment** | Verify data cannot be re-identified | Annually, or when data structure changes | Anonymization/pseudonymization meets regulatory standards |
| **Regression Testing** | Verify masking after system changes | After masking configuration changes | Masking continues to function correctly |

**Validation Methodology**:

Masking validation SHALL include:

- Sample data inspection (manual review of masked vs. unmasked data)
- Automated pattern detection (searching for unmasked sensitive data patterns)
- Reverse engineering attempts (attempting to recover original data from masked data)
- Statistical analysis (for anonymization - verify k-anonymity, l-diversity as applicable)
- Re-identification testing (for GDPR pseudonymization compliance)

**Acceptance Criteria**:

Masking implementation is acceptable when:

- Original sensitive data values are NOT present in masked datasets
- Data format and structure are preserved appropriately
- Referential integrity is maintained across related data
- Application functionality is not impaired by masked data
- Performance impact is within acceptable limits
- Regulatory requirements are met (GDPR, PCI DSS, etc.)

**Failure Response**:

When masking testing identifies failures:

- Implementation SHALL be corrected before production use
- Root cause SHALL be documented and addressed
- Re-testing SHALL be performed to validate fixes
- Incident SHALL be escalated per severity (exposure of sensitive data)

**Implementation Note**: Testing methodology, validation procedures, test cases, and acceptance criteria are documented in ISMS-IMP-A.8.11-4 (Testing & Validation Framework).

## Logging and Monitoring

[Organization] implements logging of data masking activities to support security monitoring and compliance verification.

**Logging Requirements**:

The following masking-related events SHALL be logged where technically feasible:

- Masking process execution (start, completion, errors)
- Masking configuration changes (technique changes, rule updates)
- Masking exceptions and bypasses (approved or attempted)
- Dynamic masking policy application (who accessed what data with which masking rule)
- Masking failures (processes that failed to complete)
- Re-identification attempts (if detection is implemented)

**Log Retention**:

- Masking process logs: Minimum **90 days**
- Masking configuration changes: Minimum **12 months**
- Exception and bypass events: Minimum **12 months**
- Dynamic masking access logs: Per data classification (minimum 90 days for Confidential+)
- Extended retention applies where regulatory requirements mandate longer periods (per ISMS-POL-00)

**Monitoring Requirements**:

[Organization] monitors for:

- Masking process failures indicating sensitive data exposure risk
- Repeated masking bypass attempts indicating potential misuse
- Configuration changes to masking rules requiring approval verification
- Performance degradation in DDM implementations

**Privacy Compliance**:

Logging SHALL comply with applicable privacy regulations per ISMS-POL-00. Users are informed of monitoring through acceptable use policy. Access to logs is restricted to authorized personnel with legitimate need (security, audit, compliance).

**Implementation Note**: Logging configuration, monitoring procedures, and alert definitions are documented in ISMS-IMP-A.8.11-4 (Testing & Validation Framework).

---

# Roles, Governance & Exception Management

## Roles and Responsibilities

**Executive Management / Board**:

- Accountable for approving data masking policy and strategy
- Ensuring adequate resources and budget for masking implementation
- Accepting residual risks where masking is not technically or operationally feasible
- Supporting data protection program and privacy-by-design initiatives

**Chief Information Security Officer (CISO)**:

- Accountable for overall data masking policy and program effectiveness
- Approving high-risk exceptions and policy changes
- Defining organizational risk appetite for data exposure
- Escalating critical data protection issues to Executive Management
- Annual policy review and approval
- Approving new masking techniques for organizational use

**Data Protection Officer (DPO)**:

- Advising on GDPR/nDSG compliance for masking implementations
- Reviewing pseudonymization and anonymization techniques for regulatory adequacy
- Ensuring data subject rights are respected in masked datasets
- Coordinating with CISO on privacy-by-design implementations
- Monitoring compliance with data protection regulations

**Chief Data Officer (CDO) / Data Governance Team**:

- Defining data classification scheme and categories
- Coordinating data owner assignments and accountability
- Maintaining enterprise data inventory and catalog
- Supporting data discovery and classification initiatives
- Resolving data ownership conflicts

**Data Owners**:

- Responsible for classifying data in their domains
- Determining masking requirements based on data sensitivity and business need
- Approving masking techniques for their data
- Approving or rejecting exception requests for their data domains
- Validating masking effectiveness and data utility
- Annual review of data classification and masking decisions

**Security Team**:

- Responsible for implementing data masking policy requirements
- Evaluating and selecting masking tools and technologies
- Configuring and maintaining masking solutions
- Conducting masking effectiveness testing
- Processing exception requests and conducting risk assessments
- Integrating masking with security monitoring program
- Conducting periodic masking assessments (ISMS-IMP-A.8.11 workbooks)
- Maintaining masking documentation and evidence

**IT Operations / Data Custodians**:

- Responsible for deploying and maintaining masking infrastructure
- Executing masking processes (SDM batch jobs, DDM configuration)
- Monitoring masking process performance and failures
- Providing technical support for masking systems
- Coordinating changes with Security Team and Data Owners
- Maintaining backups of masking configurations

**Development Teams**:

- Responsible for using masked data in non-production environments
- Implementing dynamic masking in applications (where required)
- Reporting masking issues and data utility problems
- Following secure development practices with masked test data
- Prohibited from circumventing masking controls

**Compliance / Audit Teams**:

- Responsible for verifying masking compliance with regulatory requirements
- Conducting periodic masking control audits
- Validating evidence of masking effectiveness
- Reporting compliance gaps and remediation tracking

**Users (All Personnel)**:

- Responsible for complying with data masking policies and acceptable use
- Reporting suspected unmasked sensitive data in non-production
- Using exception process for legitimate business needs
- Prohibited from attempting to bypass masking controls or re-identify masked data

**Detailed RACI Matrix**: Complete roles and responsibilities matrix with RACI assignments documented in ISMS-IMP-A.8.11 Implementation Guides.

## Assessment and Verification

[Organization] verifies data masking control effectiveness through structured assessment.

**Assessment Domains**:

1. **Data Inventory & Classification**: Systems, databases, data elements requiring masking
2. **Masking Technique Selection**: Approved techniques, implementation status, configuration
3. **Environment Coverage**: Masking implementation across all environments
4. **Testing & Validation**: Effectiveness testing, re-identification risk, compliance validation
5. **Compliance Dashboard**: Consolidated metrics, gap analysis, remediation tracking

**Assessment Frequency**:

- **Comprehensive assessment**: **Annually** (aligned with internal audit program, typically Q4)
- **Periodic verification**: **Quarterly** (high-risk systems, recent changes)
- **Triggered assessment**: **Within 30 days** of:
  - Significant security incidents involving data exposure
  - Major system changes affecting sensitive data
  - New data processing activities or data categories
  - Deployment of new masking solutions
  - Audit findings requiring remediation verification
  - Regulatory requirement changes (GDPR, PCI DSS updates)

**Assessment Methodology**:

Assessment conducted using ISMS-IMP-A.8.11 suite:

- Excel-based assessment workbooks with automated compliance calculations
- Evidence registers documenting masking implementations
- Gap analysis identifying unprotected sensitive data
- Remediation tracking for identified gaps
- Dashboard consolidation providing executive visibility

**Assessment Ownership**:

- Security Team conducts assessments with input from Data Owners and IT Operations
- Data Owners validate assessment accuracy for their domains
- CISO reviews assessment results and approves remediation plans
- Compliance Team verifies regulatory compliance claims

**Implementation Note**: Assessment methodology, workbook generation scripts, evidence requirements, and compliance calculation procedures are defined in ISMS-IMP-A.8.11 (Implementation Guidance Suite).

## Exception Management

**Exception Request Requirements**:

Exceptions to data masking policy requirements require:

- **Documented business justification**: Specific reason why masking cannot be implemented
- **Risk assessment**: Likelihood and impact of data exposure without masking
- **Compensating controls**: Alternative protections (access controls, encryption, monitoring)
- **Timeline**: Duration of exception and path to achieving full compliance
- **Data Owner approval**: Owner of affected data must approve exception
- **Formal approval** per authority matrix below

**Approval Authority**:

| Exception Type | Approval Required | Maximum Duration |
|----------------|-------------------|------------------|
| **Single system exception (low sensitivity)** | Security Team Lead + Data Owner | 12 months |
| **Single system exception (high sensitivity)** | CISO + Data Owner | 6 months |
| **Environment-wide exception (Development/Test)** | CISO + CIO + Data Owner | 6 months |
| **Production masking waiver** | CISO + Executive Management | Requires annual re-approval |
| **Regulatory compliance exception** | CISO + DPO + Legal/Compliance | Requires annual re-approval |
| **Technique prohibition override** | NOT PERMITTED | N/A - prohibited techniques cannot be used |

**Exception Documentation**:

All approved exceptions SHALL be documented including:

- Business justification and necessity
- Risk assessment (inherent risk, compensating controls, residual risk)
- Approval signatures and dates
- Exception duration and review schedule
- Monitoring and compliance verification requirements
- Conditions for exception revocation

**Exception Monitoring**:

Active exceptions are:

- Reviewed quarterly for continued validity
- Monitored for compliance with compensating controls
- Revoked if business justification changes or compensating controls fail
- Escalated if risk profile increases
- Automatically expired at end of approved duration (no implicit renewal)

**Exception Template**: ISMS-POL-A.8.11 Annex B provides standardized exception request template and approval workflow.

## Incident Response

**Data Masking Security Incidents** include:

| Incident Type | Severity | Response Priority |
|---------------|----------|-------------------|
| **Unmasked sensitive data in non-production** | High | Immediate - Contain and remediate |
| **Masking process failure exposing sensitive data** | Critical | Immediate - Stop exposure, investigate |
| **Successful re-identification of masked data** | High | Immediate - Assess technique weakness |
| **Masking bypass or circumvention attempt** | High | Immediate - Investigate and prevent recurrence |
| **Unauthorized access to token vault or pseudonymization keys** | Critical | Immediate - Key compromise response |
| **Masking configuration error** | Medium | Urgent - Correct configuration, validate |
| **Data exfiltration from environment with insufficient masking** | Critical | Immediate - Incident response, breach notification |

**Response Process**:

1. **Detection & Reporting**: Incidents detected through monitoring, user reports, or testing
2. **Classification**: Incident severity based on data sensitivity and exposure scope
3. **Containment**: Immediate actions - stop data flow, isolate systems, prevent further exposure
4. **Investigation**: Root cause analysis, scope determination, impact assessment
5. **Remediation**: Fix masking implementation, validate effectiveness, prevent recurrence
6. **Notification**: Internal escalation, external notification per regulatory requirements (GDPR breach notification if applicable)
7. **Post-Incident**: Lessons learned, control improvements, policy updates

**Critical Incidents**:

Unmasked sensitive data exposure in non-production or unauthorized environments is treated as high-priority security incident:

- Immediate containment: Stop data flow, delete exposed data
- Scope assessment: Determine extent of exposure (what data, how long, who accessed)
- Impact analysis: Assess regulatory breach notification requirements
- Remediation: Implement masking, validate effectiveness
- Prevention: Strengthen controls to prevent recurrence

**Regulatory Breach Notification**:

Data exposure incidents SHALL be assessed for breach notification requirements:

- **GDPR**: Notification within 72 hours if risk to rights and freedoms (Art. 33-34)
- **Swiss nDSG**: Notification if high risk to personality or fundamental rights (Art. 24)
- **Sector-specific**: PCI DSS breach notification, HIPAA breach notification (if applicable)

DPO and Legal/Compliance SHALL be involved in breach notification decisions.

**Detailed Procedures**: Data masking incident response procedures, classification criteria, escalation procedures, and coordination with incident response team are documented in ISMS-IMP-A.8.11-4 (Testing & Validation Framework).

## Policy Governance

**Policy Review**:

- **Frequency**: Annual minimum
- **Triggers**: 
  - Regulatory changes (GDPR updates, new sector regulations)
  - Major incidents exposing policy gaps
  - Significant organizational changes (mergers, new data processing)
  - Technology changes (new masking capabilities, tool changes)
  - Audit findings requiring policy updates
  - Data classification scheme changes
- **Reviewers**: CISO, Security Team, DPO, Legal/Compliance, Data Governance Team
- **Approval**: CISO (technical), Executive Management (strategic)

**Implementation Standards Review**:

- **Frequency**: Based on technology evolution (at least semi-annual)
- **Authority**: Security Team proposes updates, CISO approves
- **Note**: Implementation standard updates (ISMS-IMP-A.8.11, ISMS-CTX-A.8.11) do NOT require policy revision
- **Scope**: Masking techniques, tool configurations, assessment procedures

**Policy Updates**:

- **Minor** (clarifications, references, procedural details): CISO approval, communication within 30 days
- **Major** (scope changes, new mandatory requirements, technique prohibitions): Full approval chain, implementation timeline per change management
- **Emergency** (critical vulnerability, regulatory mandate): CISO approval with Executive Management notification, immediate communication and implementation

**Policy Communication**:

Policy published in ISMS document repository. Changes communicated organization-wide:

- Email notification to all affected stakeholders
- Intranet announcement highlighting changes
- Training provided for significant changes affecting roles or responsibilities
- Data Owners briefed on changes affecting their domains
- Exception holders notified of changes affecting their exceptions

**Policy Storage and Access**:

**Primary Repository**:

- Centralized policy repository (SharePoint, Confluence, document management system)
- Access-controlled (Internal classification)
- Version history maintained

**Archive**:

- Previous versions archived (minimum 3 years)
- Read-only access
- Timestamped and integrity-protected

**Access Control**:

| Role | Access Level |
|------|-------------|
| **All Employees** | Read (current version) |
| **Security Team** | Read/Write (current version) |
| **CISO** | Read/Write (all versions) |
| **DPO** | Read (all versions) |
| **Compliance Officer** | Read (all versions) |
| **Internal Audit** | Read (all versions) |
| **External Auditors** | Read (current version, upon request) |

**Training and Awareness**:

**Security Awareness** (All Personnel):

- Annual security awareness training includes data masking overview
- User responsibilities for handling masked data
- Recognizing unmasked sensitive data and reporting procedures
- Prohibition on re-identification attempts

**Technical Training** (IT/Security Staff):

- Data masking technology configuration and maintenance
- Masking technique selection and implementation
- Testing and validation procedures
- Incident response for masking failures

**Data Owner Training** (Data Owners):

- Data classification and masking decision framework
- Exception request evaluation criteria
- Validation of masking effectiveness for their domains

**Developer Training** (Development Teams):

- Using masked data in non-production environments
- Dynamic masking implementation in applications
- Secure development practices with sensitive data

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Data masking controls selected based on [Organization]'s risk assessment
- Data classification determines masking requirements
- Risk treatment plans document data masking control implementation
- Residual risks (where masking not feasible) documented and accepted

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Control A.8.11 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported
- Control effectiveness measured through assessment program

**Related Controls**:

| Control | Relationship to Data Masking |
|---------|------------------------------|
| **A.5.12 (Classification of Information)** | Foundation - data classification drives masking decisions |
| **A.5.15 (Access Control)** | Complementary - masking provides defense in depth beyond access controls |
| **A.8.3 (Management of Privileged Access Rights)** | Integration - privileged users may access unmasked data with monitoring |
| **A.8.10 (Information Deletion)** | Complementary - deletion is separate from masking |
| **A.8.24 (Use of Cryptography)** | Complementary - encryption protects data in transit/at rest; masking obscures in use |
| **A.5.9 (Inventory of Information and Other Associated Assets)** | Foundation - asset inventory identifies systems requiring masking |
| **A.5.23 (Cloud Services)** | Integration - cloud data masking requirements per provider model |
| **A.8.11 (Data Masking)** | This policy |
| **A.5.7 (Threat Intelligence)** | Informative - threat landscape informs masking priority |
| **A.5.24 (Information Security Incident Management Planning and Preparation)** | Integration - masking failures handled as incidents |

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.8.11 Suite):

- **ISMS-IMP-A.8.11-1**: Data Inventory & Classification Assessment
  - Sensitive data inventory methodology
  - Data classification assessment
  - System inventory with sensitive data
  - Data owner assignment
  - Evidence registers

- **ISMS-IMP-A.8.11-2**: Masking Technique Selection & Requirements
  - Approved technique implementation documentation
  - Technique selection decision framework
  - Static vs. dynamic masking comparison
  - Tool capability assessment (vendor-agnostic)
  - Configuration standards

- **ISMS-IMP-A.8.11-3**: Environment Coverage Assessment
  - Environment inventory and classification
  - Coverage gap analysis
  - Masking implementation verification
  - Exception tracking
  - Remediation planning

- **ISMS-IMP-A.8.11-4**: Testing & Validation Framework
  - Testing methodology and procedures
  - Effectiveness validation criteria
  - Re-identification risk assessment
  - Regulatory compliance validation
  - Incident response procedures

- **ISMS-IMP-A.8.11-5**: Compliance Dashboard
  - Consolidated compliance reporting
  - Executive summary metrics
  - Gap analysis and prioritization
  - Remediation tracking
  - Audit evidence compilation

**Technical Reference** (NOT ISMS):

- **ISMS-CTX-A.8.11**: Data Masking Technical Reference
  - Detailed masking technique specifications
  - Data discovery methodology deep-dive
  - Masking tool landscape analysis (vendor-agnostic)
  - Implementation patterns and architectures
  - Quick reference guides for practitioners
  - **Note**: This document is NOT part of ISMS and does NOT establish binding requirements

**Assessment Tools**:

- Excel-based assessment workbooks with automated compliance calculations
- Python generation scripts for assessment workbooks
- Evidence registers and templates
- Gap analysis frameworks
- Remediation tracking tools
- Dashboard consolidation scripts

**Supporting Materials**:

- Exception request procedures and templates (Annex B)
- User communication templates
- Training materials
- Quick reference guides (ISMS-CTX-A.8.11)

## Regulatory Mapping

This policy addresses data masking requirements from:

| Requirement Category | Swiss nDSG | EU GDPR | ISO 27001 | PCI DSS* | HIPAA* | FINMA* | DORA/NIS2* |
|---------------------|-----------|---------|-----------|---------|--------|--------|------------|
| Data minimization | Art. 8, 25 | Art. 5(1)(c) | A.8.11 | Req. 12.3 | §164.514 | Risk-Based | Art. 21 (NIS2) |
| Pseudonymization | Art. 8 | Art. 32(1)(a), Art. 89 | A.8.11 | N/A | §164.514(b) | Risk-Based | Risk-Based |
| Masking in non-production | Art. 8 | Art. 25, 32 | A.8.11 | Req. 3.4, 12.3 | §164.514 | Risk-Based | Risk-Based |
| Testing & validation | Art. 8 | Art. 25, 32 | A.8.11 | Req. 11.3 | §164.308(a)(8) | Risk-Based | Art. 9 (DORA) |
| Access logging | Art. 8 | Art. 32(1)(d) | A.8.16 | Req. 10 | §164.312(b) | Risk-Based | Monitoring |
| Incident response | Art. 24 | Art. 33-34 | A.5.24 | Req. 12.10 | §164.404 | Incident Mgmt | Art. 23 (DORA) |

*Conditional applicability per ISMS-POL-00

**Detailed Regulatory Requirements**: Specific regulatory interpretation, compliance verification procedures, and evidence mapping are documented in ISMS-IMP-A.8.11-5 (Compliance Dashboard).

## Document Relationship

```
Policy Layer (Governance - ISMS Governed)
    │
    └── ISMS-POL-A.8.11 (This Document)
        ├── Annex A: Masking Technique Approval Framework
        └── Annex B: Exception Request Template

Technical Reference Layer (NOT ISMS - Informational Only)
    │
    └── ISMS-CTX-A.8.11 (Data Masking Technical Reference)
        ├── Detailed technique specifications
        ├── Data discovery methodologies
        ├── Tool landscape analysis
        ├── Implementation patterns
        └── Quick reference guides

Implementation Layer (Assessment & Evidence - ISMS Governed)
    │
    └── ISMS-IMP-A.8.11 Suite
        ├── ISMS-IMP-A.8.11-1: Data Inventory & Classification
        ├── ISMS-IMP-A.8.11-2: Masking Technique Selection
        ├── ISMS-IMP-A.8.11-3: Environment Coverage
        ├── ISMS-IMP-A.8.11-4: Testing & Validation
        └── ISMS-IMP-A.8.11-5: Compliance Dashboard
```

---

# Definitions

**Anonymization**: Irreversible process of removing all identifying information from data such that re-identification is not possible even with additional data or effort. Anonymized data is no longer personal data under GDPR.

**Compensating Control**: Alternative security control implemented when primary control (masking) is not technically or operationally feasible, providing equivalent risk reduction.

**Data Classification**: Process of categorizing data based on sensitivity, criticality, and regulatory requirements to determine appropriate protection measures including masking.

**Data Custodian**: IT operations personnel responsible for deploying and maintaining technical infrastructure including masking solutions. Custodians implement requirements defined by Data Owners.

**Data Masking**: Process of obscuring original data with modified content (masked values) to protect sensitive information while maintaining data format and usability for legitimate purposes.

**Data Owner**: Business or functional leader accountable for data within their domain, responsible for data classification, determining masking requirements, and approving exceptions.

**Data Subject**: Individual whose personal data is being processed (GDPR/nDSG terminology).

**Dynamic Data Masking (DDM)**: Real-time masking applied at the point of data access based on user role or context. Original data remains unchanged in storage; masking occurs during query or retrieval.

**Environment**: System context where data is processed (Production, Test, Development, Analytics, Training, Sandbox, Backup, Archive). Different environments have different masking requirements.

**Exception**: Formally approved deviation from policy requirements, documented with business justification, risk assessment, compensating controls, and time limitation.

**Format Preservation**: Maintaining original data format and structure in masked data to ensure application compatibility and data validation rules continue to function.

**Personally Identifiable Information (PII)**: Any information that can identify an individual directly (name, ID number) or indirectly (combination of attributes).

**Pseudonymization**: Replacing direct identifiers with pseudonyms such that data cannot identify individuals without additional information (key or mapping table) held separately. Pseudonymized data remains personal data under GDPR but with reduced risk.

**Redaction**: Complete removal or replacement of sensitive data with placeholder characters (e.g., `****`, `XXXX`, `[REDACTED]`) without providing substitute values.

**Referential Integrity**: Maintaining valid relationships between related data across tables or datasets, ensuring foreign keys and joins continue to function correctly after masking.

**Re-identification**: Process of determining the original identity of a data subject from anonymized or pseudonymized data, either through reverse engineering, linking with external data, or other techniques.

**Sensitive Data**: Any information that, if disclosed, could cause harm to individuals or [Organization], including PII, financial data, health data, credentials, and proprietary information. Typically classified as Confidential or Restricted.

**Static Data Masking (SDM)**: Permanent replacement of sensitive data with masked values in non-production databases or datasets. Original data is irreversibly replaced; masking occurs once during data provisioning.

**Substitution**: Replacement of sensitive data with realistic but fictitious values that maintain data format, structure, and utility for intended use cases (testing, development, analytics).

**Tokenization**: Replacing sensitive data with non-sensitive tokens (surrogate values); original data stored in secure token vault enabling reversibility when authorized.

---

# Annex A: Masking Technique Approval Framework

**Scope**: This annex defines the approval framework and selection criteria for data masking techniques. All approved techniques are listed in policy Section 2.2. Organizations select techniques appropriate to their data types, use cases, and risk profiles.

## A.1 Technique Approval Criteria

New masking techniques or modifications to approved techniques SHALL meet the following criteria before organizational approval:

**Security Effectiveness**:

- Technique SHALL obscure original sensitive data effectively
- Original data SHALL NOT be recoverable without authorized access to keys/vaults (for reversible techniques)
- Technique SHALL resist common re-identification attacks appropriate to data sensitivity
- Technique SHALL be based on proven algorithms or industry-accepted practices

**Regulatory Compliance**:

- Technique SHALL meet regulatory requirements for applicable data types:
  - GDPR pseudonymization requirements (Art. 32(1)(a), Art. 89) if used for GDPR compliance
  - PCI DSS masking requirements (Req. 3.4, 3.5) if used for payment card data
  - HIPAA de-identification standards (§164.514) if used for healthcare data
  - nDSG data protection requirements (Art. 8) for Swiss personal data
- Technique SHALL be validated by appropriate authority (Security Team, DPO, Compliance)

**Operational Feasibility**:

- Technique SHALL be implementable within [Organization]'s technical environment
- Technique SHALL maintain data utility for intended use cases (testing, analytics, reporting)
- Technique SHALL preserve data format and referential integrity where required
- Performance impact SHALL be acceptable for operational requirements
- Technique SHALL be maintainable by [Organization]'s technical staff

**Documentation Requirements**:

- Technique specification documented in ISMS-CTX-A.8.11 (Technical Reference)
- Use cases and selection criteria documented
- Testing and validation procedures defined
- Known limitations and residual risks documented

## A.2 Technique Selection Decision Framework

**Decision Matrix**:

| Use Case | Data Sensitivity | Reversibility Need | Format Preservation | Recommended Technique |
|----------|------------------|--------------------|--------------------|----------------------|
| Non-production testing | Critical/High | No | Yes | Static Data Masking (SDM) with Substitution |
| Non-production development | Critical/High | No | Yes | Static Data Masking (SDM) with Substitution |
| Production role-based access | Critical/High | N/A (original unchanged) | Yes | Dynamic Data Masking (DDM) |
| Analytics/reporting | High | No | Partial | Pseudonymization or Aggregation |
| External data sharing | Critical/High | No | Optional | Anonymization or Strong Pseudonymization |
| Payment card data (non-prod) | Critical | Conditional | Yes | Tokenization or SDM with PCI-compliant masking |
| Research/statistics (GDPR) | High | Conditional | Partial | Pseudonymization per GDPR Art. 89 |
| Training/demonstration | Any Sensitive | No | Optional | Redaction or SDM with Substitution |
| Public data release | Any Sensitive | No | No | Anonymization (k-anonymity, l-diversity) |

**Selection Considerations**:

1. **Start with data classification**: Higher sensitivity requires stronger masking
2. **Consider regulatory requirements**: GDPR, PCI DSS, HIPAA have specific technique requirements
3. **Assess reversibility need**: Legitimate need to recover original data determines technique
4. **Evaluate data utility**: Masked data must be useful for intended purpose
5. **Consider performance**: Real-time (DDM) vs. batch (SDM) performance implications
6. **Validate referential integrity**: Cross-table relationships must remain valid

## A.3 Technique-Specific Requirements

### A.3.1 Static Data Masking (SDM)

**Mandatory Requirements**:

- SDM SHALL be applied BEFORE data leaves production environment
- SDM SHALL maintain referential integrity across related tables
- SDM SHALL preserve data format for application compatibility
- SDM process SHALL be repeatable (same input produces consistent masked output)
- Original data SHALL NOT be recoverable from masked output

**Quality Criteria**:

- Masked data realistic enough for application testing
- Data distribution similar to production (for performance testing)
- Edge cases and validation rules tested with masked data

### A.3.2 Dynamic Data Masking (DDM)

**Mandatory Requirements**:

- DDM SHALL be enforced at database or application layer (not client-side)
- DDM rules SHALL be based on documented user roles and least privilege principle
- DDM SHALL NOT be bypassable by users without appropriate authorization
- DDM SHALL log all access to masked fields for audit purposes
- Performance impact SHALL be assessed and within acceptable limits

**Quality Criteria**:

- Masking rules aligned with business access requirements
- Bypass attempts detected and alerted
- Minimal performance degradation (<10% typical)

### A.3.3 Tokenization

**Mandatory Requirements**:

- Token vault SHALL be secured with access controls and encryption
- Tokens SHALL be format-preserving where required (e.g., credit card format)
- Token-to-value mapping SHALL be one-to-one (deterministic tokenization)
- Token vault SHALL be backed up separately with appropriate security
- De-tokenization SHALL require explicit authorization and be logged

**Quality Criteria**:

- Vault availability meets operational requirements
- Key management for vault encryption follows A.8.24 Cryptography Policy
- Token collision risk minimized through appropriate token space

### A.3.4 Pseudonymization (GDPR Compliance)

**Mandatory Requirements**:

- Pseudonymization keys SHALL be stored separately from pseudonymized data
- Re-identification SHALL require separate authorization beyond data access
- Pseudonymization SHALL meet GDPR requirements (Art. 32(1)(a), Art. 89) when used for GDPR compliance
- Pseudonymization technique SHALL be validated by DPO for GDPR adequacy
- Key management SHALL follow A.8.24 Cryptography Policy

**Quality Criteria**:

- Pseudonyms are consistent across datasets (same person = same pseudonym)
- Re-identification risk assessed annually or when data structure changes
- Appropriate for intended purpose (research, statistics, legitimate interest)

### A.3.5 Anonymization (Irreversible)

**Mandatory Requirements**:

- Anonymization SHALL be irreversible (no keys or mappings retained)
- Re-identification risk SHALL be assessed using appropriate methodology (k-anonymity, l-diversity)
- Direct identifiers SHALL be removed or generalized
- Quasi-identifiers SHALL be assessed for linking risk
- Anonymization SHALL meet regulatory standards when used for compliance (GDPR, HIPAA)

**Quality Criteria**:

- k-anonymity ≥ 5 (minimum) for GDPR-compliant anonymization
- l-diversity considered for sensitive attributes
- Linking risk with external datasets assessed
- Data utility preserved for intended analytical purpose

## A.4 Prohibited Techniques and Anti-Patterns

**The following are NOT acceptable as masking techniques**:

| Prohibited Practice | Reason |
|---------------------|--------|
| **Simple character substitution** (A→1, B→2) | Trivially reversible, predictable pattern |
| **ROT13 or Caesar cipher** | Trivially reversible, not cryptographically secure |
| **Reversible encoding only** (Base64, URL encoding, Hex) | Not masking - just encoding, easily reversed |
| **Self-designed "encryption"** | Unvalidated security, likely weak, not accepted for compliance |
| **Masking client-side only** (JavaScript, UI layer) | Bypassable - data remains unmasked in backend |
| **Leaving production data unmasked in non-production** | Core policy violation |
| **Using same masked dataset indefinitely without refresh** | Stale data, potential circumvention over time |

**Rationale**: These practices provide appearance of security without actual protection, constituting "cargo cult security theater" that fails under scrutiny.

## A.5 Technique Validation and Testing

All masking techniques SHALL be validated for:

1. **Effectiveness**: Original data not recoverable (irreversible techniques) or only with authorized keys (reversible)
2. **Format preservation**: Data format matches original where required
3. **Referential integrity**: Cross-table relationships maintained
4. **Regulatory compliance**: Technique meets requirements for intended use case
5. **Performance**: Acceptable overhead for operational requirements

**Validation Procedures**: Testing methodology documented in ISMS-IMP-A.8.11-4 (Testing & Validation Framework).

**Technical Specifications**: Detailed technique specifications, algorithm parameters, and configuration guidance provided in ISMS-CTX-A.8.11 (Data Masking Technical Reference - NOT ISMS).

---

# Annex B: Exception Request Template

**Purpose**: Standardized format for requesting exceptions to data masking requirements per policy Section 3.3.

## Exception Request Form

**Exception Request ID**: [AUTO-GENERATED: EXC-A811-YYYY-NNN]  
**Request Date**: [DD.MM.YYYY]  
**Requested By**: [Name, Title, Department]  
**Data Owner**: [Name, Title] - Must approve this exception  

---

## Exception Scope

**Systems Affected**:

- [List all systems, databases, applications affected by this exception]

**Data Categories Affected**:

- [List data categories: PII, Financial, Health, Credentials, etc.]
- [Specify data elements: table names, field names, data types]

**Environments**:

- [ ] Production
- [ ] Test/QA
- [ ] Development
- [ ] Analytics/BI
- [ ] Training
- [ ] Other: [Specify]

**Data Sensitivity Classification**:

- [ ] Restricted (Critical)
- [ ] Confidential (High)
- [ ] Internal (Medium)

---

## Business Justification

**Why is masking not feasible?**
[Provide detailed explanation - technical, operational, or business reasons]

**Business Impact if Exception Denied**:
[Describe operational impact, business risk, project delays, etc.]

**Duration of Need**:

- Exception Start Date: [DD.MM.YYYY]
- Exception End Date: [DD.MM.YYYY] (Maximum: 12 months, shorter for high sensitivity)
- Path to Compliance: [Describe plan to achieve full masking compliance]

---

## Risk Assessment

**Inherent Risk (without masking)**:

- Likelihood of Exposure: [ ] Low [ ] Medium [ ] High [ ] Critical
- Impact if Exposed: [ ] Low [ ] Medium [ ] High [ ] Critical
- Inherent Risk Score: [Likelihood × Impact]

**Threat Scenarios**:
[List specific threats enabled by unmasked data in this environment]

**Compliance Impact**:
[Describe regulatory implications: GDPR, PCI DSS, HIPAA, nDSG, etc.]

---

## Compensating Controls

**Alternative Protections Implemented**:
[Describe controls that partially mitigate risk of unmasked data]

Examples:

- [ ] Enhanced access controls (list roles with access)
- [ ] Network segmentation (describe isolation)
- [ ] Enhanced monitoring and alerting (describe logging)
- [ ] Data encryption at rest and in transit
- [ ] Time-limited access (describe duration and justification)
- [ ] Additional audit logging (describe what is logged)
- [ ] User training and acceptable use acknowledgment
- [ ] Data minimization (reduced dataset size/columns)
- [ ] Other: [Specify]

**Compensating Control Effectiveness**:

- Estimated Risk Reduction: [Percentage or qualitative assessment]
- Residual Risk Score: [Reduced risk after compensating controls]

---

## Monitoring and Compliance

**Monitoring Requirements**:
[How will compliance with exception conditions be verified?]

**Review Schedule**:

- [ ] Monthly (for Critical sensitivity)
- [ ] Quarterly (for High sensitivity)
- [ ] Semi-Annual (for Medium sensitivity)

**Revocation Triggers**:
[Under what conditions will this exception be revoked?]

Examples:

- Compensating control failure
- Security incident related to unmasked data
- Business justification no longer valid
- Masking solution becomes available
- Exception duration expires

---

## Approvals

**Data Owner Approval**:

- Name: [Data Owner Name]
- Signature: ________________
- Date: [DD.MM.YYYY]
- Comments: [Optional]

**Security Team Review**:

- Reviewer: [Security Team Lead Name]
- Risk Assessment: [ ] Acceptable [ ] Not Acceptable
- Signature: ________________
- Date: [DD.MM.YYYY]
- Comments/Conditions: [Required if approved]

**CISO Approval** (Required for High/Critical sensitivity):

- Name: [CISO Name]
- [ ] Approved [ ] Denied
- Signature: ________________
- Date: [DD.MM.YYYY]
- Conditions: [Special conditions for approval]

**Executive Management Approval** (Required for production exceptions):

- Name: [Executive Name]
- [ ] Approved [ ] Denied
- Signature: ________________
- Date: [DD.MM.YYYY]

---

## Exception Tracking

**Exception Status**:

- [ ] Pending Approval
- [ ] Approved
- [ ] Denied
- [ ] Expired
- [ ] Revoked

**Exception Review Log**:

| Review Date | Reviewer | Status | Comments | Next Review |
|-------------|----------|--------|----------|-------------|
| | | | | |

**Exception Closure**:

- Closure Date: [DD.MM.YYYY]
- Reason: [ ] Expired [ ] Revoked [ ] Masking Implemented [ ] Other
- Final Comments: [Lessons learned, improvements implemented]

---

**Exception Documentation**: All approved exceptions maintained in exception register (ISMS-IMP-A.8.11-3 Environment Coverage Assessment).

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

---

*This policy establishes requirements. Implementation procedures are documented in ISMS-IMP-A.8.11 (UG/TG). Technical reference information is provided in ISMS-CTX-A.8.11 (NOT ISMS).*

<!-- QA_VERIFIED: 2026-02-02 -->