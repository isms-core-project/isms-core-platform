<!-- ISMS-CORE:REF:ISMS-REF-DORA-digital-operational-resilience-act-requi:framework:REF:dora -->
**ISMS-REF-DORA — Digital Operational Resilience Act Requirements Reference**
**EU Financial Sector Digital Resilience Requirements (Non-ISMS Technical Reference)**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | DORA Requirements Reference |
| **Document Type** | Internal - Technical Reference (Not ISMS) |
| **Document ID** | ISMS-REF-DORA |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | CISO (Technical Reference - No Executive Approval Required) |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Legal/Compliance | Initial technical reference for EU financial entities |

**Review Cycle**: Annual (or upon DORA regulatory technical standards updates)  
**Next Review Date**: [Date + 12 months]  
**Approvers**: Legal/Compliance / CISO (technical reference, no ISMS approval required)

**Distribution**: Compliance team, CISO, Legal counsel (for organisations subject to DORA)

---

⚠️ **IMPORTANT – NON-ISMS TECHNICAL SUPPORT DOCUMENT**

This document is provided for informational and awareness purposes only.

- This document is NOT part of the Information Security Management System (ISMS).
- This document does NOT define mandatory requirements unless [Organisation] is a DORA-regulated entity.
- This document does NOT establish binding requirements, deadlines, KPIs, or SLAs for non-regulated entities.
- This document does NOT mandate the adoption of DORA requirements for organisations not subject to DORA.
- This document does NOT override or extend any ISMS policy.

**Applicability Determination**:
DORA requirements apply ONLY IF [Organisation]:

- Is a financial entity operating in the EU (banks, payment institutions, investment firms, crypto-asset service providers, insurance, etc.)
- Is designated as a critical or important ICT third-party service provider to EU financial entities
- Has contractual obligations to meet DORA requirements

For all other organisations, this document serves solely as:

- Technical reference for potential DORA requirements
- Context for service provider relationships with EU financial entities
- Awareness of EU financial sector digital resilience standards
- **This document must not be used as audit evidence unless [Organisation] is DORA-regulated**

Use of this document does not imply DORA applicability, compliance obligations, or regulatory status.

**Critical Positioning Statement**:
This document intentionally provides regulatory detail beyond what applies to most organisations. Its purpose is awareness only for organisations that MAY become subject to DORA, or that provide ICT services to DORA-regulated financial entities. No auditor conclusions shall be drawn from the presence, absence, or implementation status of any DORA requirement listed herein unless [Organisation] is explicitly DORA-regulated.

---

# Document Purpose and Scope

## Purpose

This document provides a technical overview of the Digital Operational Resilience Act (Regulation (EU) 2022/2554) requirements for EU financial sector entities. It is intended to support:

- Awareness of DORA requirements for EU financial entities
- Understanding of DORA's five pillars (ICT risk management, incident reporting, testing, third-party risk, information sharing)
- Context for ICT service providers to EU financial entities
- Potential future applicability assessment
- Mapping DORA requirements to ISO 27001:2022 controls

## What This Document Is NOT

This document does NOT:

- Establish mandatory requirements for non-DORA-regulated organisations
- Define [Organisation]'s compliance obligations (see POL-00 for regulatory applicability)
- Create audit criteria unless [Organisation] is DORA-regulated
- Replace legal or compliance counsel interpretation
- Constitute legal advice on DORA compliance
- Establish implementation procedures or verification processes
- Cover Regulatory Technical Standards (RTS) in exhaustive detail

## Relationship to ISMS

This document is a **non-binding technical reference** UNLESS [Organisation] is subject to DORA (as determined in ISMS-POL-00 Section 3.2).

**If [Organisation] IS DORA-regulated:**

- DORA requirements become Tier 1 (Mandatory Compliance) per POL-00
- This document provides implementation guidance
- ISMS controls must demonstrate DORA compliance
- Compliance attestation required (supervisory reporting)

**If [Organisation] IS NOT DORA-regulated:**

- DORA remains Tier 3 (Informational Reference) per POL-00
- This document is for awareness only
- No DORA compliance obligations exist
- ISMS controls follow ISO 27001:2022 only

**If [Organisation] provides ICT services to DORA financial entities:**

- May be designated as critical or important third-party service provider
- DORA oversight framework may apply (Chapter V, Section II)
- Contractual requirements likely to reference DORA standards
- Consider as Tier 2 (Conditional) pending designation

## Content Organisation

This reference organizes DORA requirements by:

- Five pillar structure (Chapters II-VI of DORA)
- ICT risk management framework (Chapter II)
- Incident reporting (Chapter III)
- Digital operational resilience testing (Chapter IV)
- Third-party risk management (Chapter V)
- Information sharing arrangements (Chapter VI)
- Mapping to ISO 27001:2022 Annex A controls

---

# DORA Overview and Applicability

## What is DORA?

**Regulation (EU) 2022/2554** on digital operational resilience for the financial sector entered into force on January 16, 2023 with application from **January 17, 2025**.

**Purpose**: Establish uniform requirements for digital operational resilience across EU financial sector, addressing:

- Fragmented national approaches to ICT risk
- Increasing cyber threats and ICT disruptions
- Concentration risk in third-party ICT service providers
- Need for harmonized incident reporting
- Importance of threat intelligence sharing

**Legal Basis**: EU Regulation (directly applicable in all member states, no national transposition required)

**Supervisory Authority**: European Supervisory Authorities (ESAs):

- European Banking Authority (EBA)
- European Securities and Markets Authority (ESMA)
- European Insurance and Occupational Pensions Authority (EIOPA)
- Plus national competent authorities

## Who Must Comply with DORA?

**Financial Entities** (Article 2):

| Category | Examples | Supervisory Authority |
|----------|----------|----------------------|
| **Credit institutions** | Banks | EBA + National CA |
| **Payment institutions** | Payment service providers | EBA + National CA |
| **Electronic money institutions** | E-money issuers | EBA + National CA |
| **Investment firms** | Brokers, portfolio managers | ESMA + National CA |
| **Crypto-asset service providers** | Crypto exchanges, custodians | ESMA + National CA |
| **Central securities depositories** | CSDs | ESMA + National CA |
| **Trading venues** | Stock exchanges, MTFs | ESMA + National CA |
| **Trade repositories** | Transaction reporting | ESMA + National CA |
| **Managers of alternative investment funds** | Hedge funds, PE funds | ESMA + National CA |
| **Management companies** | UCITS managers | ESMA + National CA |
| **Data reporting service providers** | Approved publication arrangements | ESMA + National CA |
| **Insurance and reinsurance undertakings** | Insurers, reinsurers | EIOPA + National CA |
| **Insurance intermediaries** | Insurance brokers | EIOPA + National CA |
| **Institutions for occupational retirement provision** | Pension funds | EIOPA + National CA |
| **Credit rating agencies** | Rating agencies | ESMA |
| **Administrators of critical benchmarks** | Benchmark providers | ESMA |
| **Crowdfunding service providers** | Crowdfunding platforms | ESMA + National CA |
| **Securitisation repositories** | Securitisation reporting | ESMA + National CA |

**ICT Third-Party Service Providers** (Chapter V, Section II):

- Cloud computing service providers
- Software providers
- Data analytics providers
- Data center service providers
- **If designated as "critical"**: Subject to DORA oversight framework
- **If designated as "important"**: Enhanced contractual requirements

## Applicability Determination

**DORA applies to [Organisation] IF**:

| Criteria | Status | Evidence |
|----------|--------|----------|
| Financial entity operating in EU | ⬜ Yes ⬜ No | [License type / Country] |
| EU bank or credit institution | ⬜ Yes ⬜ No | [Banking license] |
| EU payment or e-money institution | ⬜ Yes ⬜ No | [Payment license] |
| EU investment firm | ⬜ Yes ⬜ No | [Investment license] |
| EU crypto-asset service provider | ⬜ Yes ⬜ No | [MiCAR license] |
| EU insurance or reinsurance undertaking | ⬜ Yes ⬜ No | [Insurance license] |
| Other financial entity per Article 2 | ⬜ Yes ⬜ No | [Specify type] |
| Critical ICT third-party service provider | ⬜ Yes ⬜ No ⬜ Pending | [Designation letter] |

**If ANY "Yes"**: DORA requirements are **Tier 1 (Mandatory Compliance)** per POL-00 Section 3.2

**If ALL "No"**: DORA requirements remain **Tier 3 (Informational Reference)** per POL-00

**ICT Service Provider Assessment**:
If [Organisation] provides ICT services to EU financial entities:

- Monitor for potential critical third-party service provider designation
- Review customer contracts for DORA-referenced requirements
- Assess if services are "critical or important functions" per DORA Article 3(31)-(32)
- Critical designation triggers DORA oversight framework (Articles 31-44)

---

# DORA Five Pillars Overview

## Pillar Structure

DORA organizes requirements into five pillars:

```
┌─────────────────────────────────────────────────────────────────┐
│                    DORA FIVE PILLARS                            │
├─────────────────────────────────────────────────────────────────┤
│  CHAPTER II:  ICT Risk Management Framework                     │
│               Articles 5-16                                      │
│               - Governance and strategy                          │
│               - ICT risk identification, protection, detection   │
│               - Response and recovery                            │
│               - Learning and evolving                            │
│               - Communication                                    │
├─────────────────────────────────────────────────────────────────┤
│  CHAPTER III: ICT-Related Incident Management & Reporting       │
│               Articles 17-23                                     │
│               - Incident detection and classification            │
│               - Incident response procedures                     │
│               - Reporting to competent authorities               │
├─────────────────────────────────────────────────────────────────┤
│  CHAPTER IV:  Digital Operational Resilience Testing            │
│               Articles 24-27                                     │
│               - Testing programs                                 │
│               - Advanced testing (TLPT)                          │
│               - Proportionality principle                        │
├─────────────────────────────────────────────────────────────────┤
│  CHAPTER V:   ICT Third-Party Risk Management                   │
│               Articles 28-44                                     │
│               - Third-party risk framework                       │
│               - Contractual requirements                         │
│               - Oversight of critical providers                  │
├─────────────────────────────────────────────────────────────────┤
│  CHAPTER VI:  Information Sharing Arrangements                  │
│               Articles 45                                        │
│               - Cyber threat intelligence sharing                │
└─────────────────────────────────────────────────────────────────┘
```

## Proportionality Principle

DORA applies proportionality (Article 4):

- Requirements scaled based on:
  - Size of financial entity
  - Nature, scale, and complexity of activities
  - Overall risk profile
- **Small and non-interconnected investment firms**: Simplified regime
- **Microenterprises**: Further simplifications where justified
- **All financial entities**: Core requirements still apply

---

# Chapter II - ICT Risk Management Framework

## Overview (Articles 5-16)

Financial entities must establish, maintain, and review an ICT risk management framework ensuring resilience, continuity, and security of ICT systems.

**Article 5: Governance and Organisation**

**Requirements**:

- Management body ultimately responsible for ICT risk
- Approval of ICT risk management framework
- Allocation of clear roles and responsibilities
- Sufficient resources for ICT risk management
- Internal reporting lines to management body

**Key Roles**:

- Management body (board-level responsibility)
- ICT risk management function (operational responsibility)
- Control functions (independent oversight)

**ISO 27001:2022 Mapping**:

- Clause 5.1: Leadership and commitment
- Clause 5.3: Organisational roles, responsibilities and authorities
- A.5.1: Policies for information security
- A.5.2: Information security roles and responsibilities

---

**Article 6: ICT Risk Management Framework**

**Requirements**:
Comprehensive framework covering:

- **Strategies, policies, procedures**: Documented ICT risk approach
- **ICT systems and tools**: Inventory and risk assessment
- **ICT security policies**: Protection measures
- **ICT continuity policies**: Business continuity and disaster recovery
- **ICT response and recovery plans**: Incident management
- **ICT testing**: Validation of controls
- **ICT audit**: Independent assurance
- **ICT third-party risk**: Supplier management

**ISO 27001:2022 Mapping**:

- Clause 4-10: Entire ISMS framework
- A.5.1: Policies for information security
- A.5.8: Information security in project management
- A.5.9: Inventory of information and other associated assets
- A.8.13: Information backup
- A.5.29-5.30: Business continuity

---

**Article 8: Identification**

**Requirements**:

- Comprehensive inventory of ICT assets and information assets
- Identification of all sources of ICT risk (internal and external)
- Risk assessment methodology aligned with business criticality
- Documentation of information processing locations and data flows
- Legacy ICT systems identification and risk assessment

**ISO 27001:2022 Mapping**:

- A.5.9: Inventory of information and other associated assets
- A.5.12: Classification of information
- Clause 6.1.2: Information security risk assessment

**DORA-Specific Requirements**:

- **Legacy systems**: Explicit identification and compensating controls
- **Interdependencies**: Mapping of system dependencies
- **Data mapping**: Processing locations and cross-border flows
- **Critical services**: Business impact classification

---

**Article 9: Protection and Prevention**

**Requirements**:
ICT systems protection through:

- **Policies, procedures, protocols**: Security baselines
- **ICT security tools**: Detection and prevention technologies
- **Encryption**: Data protection at rest and in transit
- **Network segmentation**: Isolation of critical functions
- **Access control**: Identity and access management
- **Physical security**: Data center and infrastructure protection
- **Change management**: Controlled system modifications

**ISO 27001:2022 Mapping**:

- A.8.1: User endpoint devices
- A.8.2-8.5: Access control
- A.8.7: Protection against malware
- A.8.9: Configuration management
- A.8.18: Use of privileged utility programs
- A.8.19: Installation of software on operational systems
- A.8.20: Networks security
- A.8.21: Security of network services
- A.8.22: Segregation of networks
- A.8.23: Web filtering
- A.8.24: Use of cryptography
- A.7.4: Physical security monitoring

**DORA Emphasis**:

- **Network segmentation** is explicitly required (not optional)
- **Encryption** mandatory for sensitive data
- **Multi-factor authentication** expected for privileged access
- **Patching and vulnerability management** critical requirements

---

**Article 10: Detection**

**Requirements**:

- Continuous monitoring mechanisms
- Detection of anomalous activities
- Real-time alerting capabilities
- Correlation of security events
- Threat intelligence integration

**ISO 27001:2022 Mapping**:

- A.8.15: Logging
- A.8.16: Monitoring activities
- A.5.24-5.25: Incident management planning
- A.5.7: Threat intelligence

**Technology Examples**:

- SIEM (Security Information and Event Management)
- EDR (Endpoint Detection and Response)
- Network traffic analysis (NTA)
- User and Entity Behavior Analytics (UEBA)
- Threat intelligence platforms (TIP)

---

**Article 11: Response and Recovery**

**Requirements**:

- ICT incident response plans
- Crisis management procedures
- Communication plans (internal and external)
- Business continuity plans (BCP)
- Disaster recovery plans (DRP)
- Recovery time objectives (RTO)
- Recovery point objectives (RPO)

**ISO 27001:2022 Mapping**:

- A.5.24-5.28: Incident management (full cycle)
- A.5.29: Information security during disruption
- A.5.30: ICT readiness for business continuity
- A.8.13: Information backup
- A.8.14: Redundancy of information processing facilities

**DORA Expectations**:

- **RTO for critical functions**: Typically 2-4 hours
- **RPO for critical data**: Near-zero (continuous replication preferred)
- **Crisis communication**: Internal and external stakeholders
- **Lessons learned**: Post-incident review mandatory

---

**Article 12: Learning and Evolving**

**Requirements**:

- Post-incident reviews
- Root cause analysis
- Implementation of corrective actions
- Integration of lessons learned
- Continuous improvement of ICT risk framework
- Monitoring of ICT risk landscape evolution

**ISO 27001:2022 Mapping**:

- A.5.27: Learning from information security incidents
- Clause 10.1-10.2: Continual improvement

---

**Article 13: Communication**

**Requirements**:

- Communication channels for reporting ICT issues
- Escalation procedures to management
- Information sharing with stakeholders
- Coordination with third-party service providers
- External communication during incidents

**ISO 27001:2022 Mapping**:

- A.5.5: Contact with authorities
- A.5.6: Contact with special interest groups
- A.6.8: Information security event reporting

---

**Article 15: ICT Security Awareness and Training**

**Requirements**:

- Regular ICT security awareness programs
- Role-based training for ICT staff
- Phishing simulations and testing
- Training effectiveness measurement
- Awareness of social engineering threats

**ISO 27001:2022 Mapping**:

- A.6.3: Information security awareness, education and training

**DORA Emphasis**:

- Training programs must be documented and measurable
- Annual mandatory training minimum
- Specialized training for privileged users
- Phishing testing expected as standard practice

---

**Article 16: ICT-Related Policies**

**Requirements**:
Financial entities must establish ICT-related policies covering:

- ICT security
- ICT continuity
- ICT change management
- ICT operations
- ICT project management
- Network security
- Encryption and key management

**Policy Review**: Annual minimum, or upon significant changes

**ISO 27001:2022 Mapping**:

- A.5.1: Policies for information security
- A.5.36: Compliance with policies, rules and standards for information security

---

# Chapter III - ICT-Related Incident Management & Reporting

## Overview (Articles 17-23)

Financial entities must have processes to detect, manage, notify, and report ICT-related incidents.

**Article 17: ICT-Related Incident Management Process**

**Requirements**:

- Early warning indicators
- Incident detection procedures
- Incident classification criteria (major vs. non-major)
- Incident response and recovery procedures
- Root cause analysis
- Escalation procedures
- Communication plans

**Incident Classification** (Article 18):
Financial entities must classify incidents based on:

- **Criticality**: Impact on business operations
- **Duration**: Length of service disruption
- **Data loss**: Volume and sensitivity of data affected
- **Geographic spread**: Number of countries/clients affected
- **Reputational impact**: Public perception and trust

**Major Incident Indicators**:

- Significant disruption to critical functions
- Service unavailability exceeding threshold (e.g., 2 hours)
- Data breach affecting large number of clients
- Significant financial loss
- Potential systemic risk to financial stability

**ISO 27001:2022 Mapping**:

- A.5.24: Information security incident management planning and preparation
- A.5.25: Assessment and decision on information security events
- A.5.26: Response to information security incidents

---

**Article 19: Initial Notification and Intermediate Reports**

**Requirement**: Financial entities must notify competent authorities of **major ICT-related incidents** according to defined timelines.

**Notification Timeline**:

| Phase | Timing | Content |
|-------|--------|---------|
| **Initial notification** | As soon as possible, no later than specified hours (typically 4 hours from detection) | Incident description, time of detection, status, preliminary impact |
| **Intermediate report** | Upon request or significant status change | Updated assessment, actions taken, ongoing response |
| **Final report** | After incident resolution (e.g., within 1 month) | Root cause, impact assessment, remediation, lessons learned |

**Reporting Channels**:

- National competent authority portal
- Standardized reporting templates (per RTS)
- Secure communication channels

**ISO 27001:2022 Mapping**:

- A.5.5: Contact with authorities
- A.5.26: Response to information security incidents

**Cross-Reporting**:
DORA reporting requirements may overlap with:

- GDPR personal data breach notifications (Article 33-34)
- NIS2 incident reporting (if entity also subject to NIS2)
- National incident reporting requirements

Entities should coordinate reporting to avoid duplication and inconsistency.

---

**Article 20: Centralized Reporting**

Financial entities report to single point of contact (national competent authority), which coordinates with:

- European Supervisory Authorities (ESAs)
- European Central Bank (ECB) for systemic risk assessment
- Single Resolution Board (SRB) if relevant
- Other EU authorities as needed

**Purpose**: Ensure EU-wide visibility of ICT incidents with potential systemic impact.

---

**Article 23: Voluntary Notification of Significant Cyber Threats**

Financial entities may voluntarily notify competent authorities of significant cyber threats even without actual incident, to support sector-wide awareness and prevention.

**Examples**:

- Advanced persistent threat (APT) detection
- Zero-day vulnerability discovery
- Ransomware campaign targeting financial sector
- Credential stuffing attacks at scale

---

# Chapter IV - Digital Operational Resilience Testing

## Overview (Articles 24-27)

Financial entities must establish, maintain, and review a sound digital operational resilience testing program.

**Article 24: General Requirements on Testing**

**Testing Program Components**:

- Range of assessments and tests appropriate to entity's ICT risk
- Vulnerability assessments and scans
- Open source analysis
- Network security assessments
- Gap analyses
- Physical security reviews
- Scenario-based testing
- Compatibility testing
- Performance testing
- End-to-end testing

**Testing Frequency**:

- Basic testing: At least annually
- Critical systems: More frequent testing
- After significant changes: Triggered testing

**ISO 27001:2022 Mapping**:

- A.5.30: ICT readiness for business continuity (testing requirement)
- A.8.8: Management of technical vulnerabilities
- A.8.34: Protection of information systems during audit testing

---

**Article 25: Testing of ICT Tools, Systems and Processes**

Financial entities shall implement testing methodologies including:

**1. Vulnerability Assessments**:

- Identification of weaknesses in systems
- Automated scanning tools
- Manual review where appropriate
- Severity-based risk scoring

**2. Scenario-Based Testing**:

- Business continuity and disaster recovery testing
- Crisis management exercises
- Failover and redundancy validation
- Communication plan validation

**3. Compatibility Testing**:

- New system integration testing
- Upgrade and migration testing
- Cross-platform compatibility

**4. Performance Testing**:

- Capacity and load testing
- Stress testing under adverse conditions
- Scalability validation

**Documentation**:

- Testing plans and procedures
- Test results and findings
- Remediation plans and timelines
- Validation of remediation

---

**Article 26: Advanced Testing of ICT Tools, Systems and Processes (TLPT)**

**Threat-Led Penetration Testing (TLPT)**:
Selected financial entities must conduct advanced testing based on **Threat-Led Penetration Testing** at least every **3 years**.

**TLPT Applicability**:

- Designated by competent authorities
- Typically large, interconnected financial entities
- High-impact institutions for financial stability
- Criteria: size, systemic importance, interconnectedness

**TLPT Requirements** (per Article 26 and RTS):

**Threat Intelligence**:

- Real-world threat scenarios
- Advanced Persistent Threat (APT) simulation
- Based on TIBER-EU or equivalent frameworks

**Red Team Testing**:

- Simulated attacks on critical functions
- Physical and digital attack vectors
- Social engineering elements
- Testing of detective and response capabilities

**Controls Testing**:

- Purple team exercises (red team + blue team collaboration)
- Testing of monitoring, detection, and response
- Validation of incident response procedures
- Communication and escalation testing

**Closure and Remediation**:

- Detailed findings report
- Remediation plan with timelines
- Management and board reporting
- Supervisory authority notification

**ISO 27001:2022 Mapping**:

- No direct ISO 27001 mapping (TLPT is DORA-specific advanced requirement)
- Related to: A.8.34 (audit testing), A.5.7 (threat intelligence)

**TLPT Framework References**:

- **TIBER-EU**: European framework for threat intelligence-based ethical red teaming
- **CBEST** (UK), **TIBER-NL** (Netherlands), **iCAST** (Ireland): National frameworks

---

**Article 27: Requirements for Testers for TLPT**

TLPT must be conducted by:

- Independent external testers
- Internal testers with independence safeguards
- Competent authorities may establish pool of approved testers

**Tester Qualifications**:

- Technical expertise in threat intelligence and penetration testing
- Understanding of financial sector operations
- Certification requirements (e.g., CREST, OSCP, OSCE, or equivalent)
- Non-disclosure and confidentiality agreements

---

# Chapter V - ICT Third-Party Risk Management

## Overview (Articles 28-44)

Financial entities must manage ICT third-party risk through comprehensive framework and oversight.

**Article 28: General Principles**

**Third-Party Risk Management Framework**:

- Strategy, policies, and procedures
- Maintenance of ICT third-party service provider register
- Pre-contractual due diligence
- Contractual arrangements
- Ongoing monitoring and oversight
- Exit strategies

**ISO 27001:2022 Mapping**:

- A.5.19: Information security in supplier relationships
- A.5.20: Addressing information security within supplier agreements
- A.5.21: Managing information security in the ICT supply chain
- A.5.22: Monitoring, review and change management of supplier services
- A.5.23: Information security for use of cloud services

---

**Article 29: Preliminary Assessment of ICT Concentration Risk**

Financial entities must:

- Identify concentration risk in ICT third-party service providers
- Assess potential single points of failure
- Consider alternative providers or mitigation strategies
- Report significant concentration risks to competent authority

**Concentration Risk Factors**:

- Use of same provider for multiple critical functions
- Limited alternative providers available
- Geographic concentration (single region/country)
- Dependency chains (provider depends on sub-provider)

**DORA-Specific**:
This is an explicit requirement not typically detailed in ISO 27001.

---

**Article 30: Key Contractual Provisions**

**Mandatory Contract Elements** for ICT services supporting critical or important functions:

**1. Service Descriptions**:

- Clear definition of services provided
- Service level agreements (SLAs)
- Locations of data processing
- Support for financial entity's compliance obligations

**2. Security Requirements**:

- Data protection and confidentiality measures
- Security incident notification timelines
- Sub-contracting restrictions and approvals
- Data return and deletion procedures

**3. Access and Audit Rights**:

- Financial entity's right to audit
- Competent authority's right to access and audit
- On-site inspection rights
- Information access for supervisory purposes

**4. Termination and Exit**:

- Exit strategies with sufficient transition period
- Data portability and migration support
- Service continuity during transition
- Return or deletion of data

**5. Jurisdiction and Dispute Resolution**:

- Governing law (EU member state law)
- Dispute resolution mechanisms
- Regulatory cooperation obligations

**ISO 27001:2022 Mapping**:

- A.5.20: Addressing information security within supplier agreements
- A.5.23: Information security for use of cloud services (exit strategies)

**DORA Enhancement**:
DORA provides much more prescriptive contractual requirements than ISO 27001, particularly around:

- Access and audit rights for authorities
- Mandatory exit strategies
- Sub-contracting governance
- Data localization and portability

---

**Article 31: ICT Third-Party Service Provider Register**

Financial entities must maintain and update register of all ICT third-party service providers, including:

- Provider identification
- Services provided
- Criticality classification (critical, important, non-critical)
- Contract dates and renewal
- Country of establishment and data processing locations
- Sub-contractors used

**Reporting**: Annual submission to competent authority (or more frequently if requested)

**ISO 27001:2022 Mapping**:

- A.5.19 (requires supplier register, though less prescriptive than DORA)

---

**Articles 32-44: Oversight Framework for Critical ICT Third-Party Service Providers**

**Critical Provider Designation**:
European Supervisory Authorities (ESAs) may designate ICT third-party service providers as "critical" based on:

- Systemic impact on financial stability
- Number and nature of financial entities served
- Complexity and criticality of services
- Substitutability and concentration risk

**Designation Process** (Article 33):

- ESA recommendation to financial entity clients
- Criteria assessment (Articles 31(1) factors)
- ICT provider has opportunity to provide information
- Lead Oversight Authority (LOA) designation

**Oversight Activities** (Articles 35-40):

- General investigations and on-site inspections
- Requests for information and documentation
- Recommendations for remediation
- Penalties for non-compliance

**ICT Provider Obligations** (Articles 37-41):

- Cooperation with Lead Oversight Authority
- Provision of information and documentation
- Facilitation of inspections
- Implementation of recommendations

**This is DORA-unique**: ISO 27001 has no equivalent regulatory oversight framework for service providers.

---

# Chapter VI - Information Sharing Arrangements

## Article 45: Information Sharing

Financial entities may participate in information sharing arrangements to enhance cyber threat intelligence and defensive capabilities.

**Permitted Information Sharing**:

- Cyber threat information and intelligence
- Indicators of compromise (IOCs)
- Tactics, techniques, and procedures (TTPs)
- Vulnerabilities and security advisories
- Effective security practices

**Conditions**:

- Voluntary participation
- Protection of confidentiality and sensitive information
- Compliance with data protection law (GDPR)
- No exchange of competitively sensitive information
- No restriction on reporting obligations to authorities

**ISO 27001:2022 Mapping**:

- A.5.7: Threat intelligence

**Information Sharing Platforms**:

- Financial Services Information Sharing and Analysis Center (FS-ISAC)
- European Financial ISAC (EU FS-ISAC)
- National CERTs and CSIRTs
- Sector-specific sharing groups

---

# ISO 27001:2022 to DORA Mapping

## Control Mapping Matrix

| DORA Requirement | DORA Article | ISO 27001:2022 Control | Gap Analysis |
|------------------|--------------|------------------------|--------------|
| ICT Risk Governance | Art. 5 | Clause 5.1, 5.3, A.5.1, A.5.2 | DORA: Management body accountability explicit |
| ICT Risk Framework | Art. 6 | Clause 4-10 (entire ISMS) | DORA: More prescriptive framework elements |
| Asset Identification | Art. 8 | A.5.9, A.5.12 | DORA: Legacy systems explicit, data mapping required |
| Protection & Prevention | Art. 9 | A.8.1-8.24, A.7.4 | DORA: Network segmentation mandatory |
| Detection | Art. 10 | A.8.15, A.8.16, A.5.7 | DORA: Real-time monitoring expected |
| Response & Recovery | Art. 11 | A.5.24-5.30, A.8.13-8.14 | DORA: RTO/RPO for critical functions |
| Learning & Evolving | Art. 12 | A.5.27, Clause 10 | Aligned |
| Awareness & Training | Art. 15 | A.6.3 | DORA: Measurable training programs |
| Incident Classification | Art. 18 | A.5.25 | DORA: Specific classification criteria (major incident) |
| Incident Reporting | Art. 19-20 | A.5.5, A.5.26 | **DORA-specific**: Regulatory reporting timelines |
| Testing Program | Art. 24-25 | A.5.30, A.8.8 | DORA: More comprehensive testing requirements |
| TLPT | Art. 26-27 | No equivalent | **DORA-unique**: Threat-led penetration testing |
| Third-Party Register | Art. 31 | A.5.19 | DORA: Prescriptive register and reporting |
| Third-Party Contracts | Art. 30 | A.5.20, A.5.23 | **DORA-specific**: Mandatory contract provisions |
| Concentration Risk | Art. 29 | No direct mapping | **DORA-unique**: Explicit concentration risk assessment |
| Critical Provider Oversight | Art. 32-44 | No equivalent | **DORA-unique**: Regulatory oversight framework |
| Information Sharing | Art. 45 | A.5.7 | Aligned |

## Key Gaps Between ISO 27001:2022 and DORA

**Gap 1: Regulatory Incident Reporting**

- ISO 27001: Internal incident management
- DORA: Mandatory reporting to competent authorities with timelines

**Gap 2: Threat-Led Penetration Testing (TLPT)**

- ISO 27001: No equivalent
- DORA: Required for designated financial entities every 3 years

**Gap 3: Third-Party Contract Provisions**

- ISO 27001: General supplier agreement guidance
- DORA: Specific mandatory contractual clauses

**Gap 4: Critical Provider Oversight**

- ISO 27001: No regulatory oversight concept
- DORA: ESA oversight framework for critical ICT providers

**Gap 5: Concentration Risk**

- ISO 27001: Indirectly addressed through risk assessment
- DORA: Explicit assessment and reporting requirement

---

# Implementation Considerations

## DORA Compliance Timeline

**If [Organisation] is DORA-regulated financial entity**:

**January 2025 (Effective Date)**:

- DORA becomes applicable
- Competent authorities may conduct supervisory assessments

**Recommended Preparation Timeline**:

**6-12 Months Before (Jul 2024 - Dec 2024)**:

- Gap assessment against DORA requirements
- ICT risk management framework enhancements
- Incident reporting process establishment
- Third-party risk management review
- Contract renegotiations with critical ICT providers

**0-6 Months After (Jan 2025 - Jun 2025)**:

- Incident reporting capability testing
- Digital operational resilience testing program launch
- Third-party register establishment
- Information sharing participation
- Regulatory technical standards (RTS) implementation as adopted

**Ongoing (Post-Jun 2025)**:

- Annual testing and continuous improvement
- Quarterly incident reporting (as incidents occur)
- Annual third-party register submission
- 3-year TLPT cycle (if designated)

## Resource Requirements

**Personnel**:

- ICT risk management function (dedicated)
- Incident response team with 24/7 capability
- Third-party risk management specialists
- Testing and audit resources (internal or external)
- Compliance and regulatory reporting function

**Technology**:

- Enhanced SIEM and SOC capabilities
- Testing tools (vulnerability scanners, penetration testing platforms)
- Third-party risk management platform
- Incident reporting portal integration
- Backup and disaster recovery infrastructure

**External Support**:

- Legal counsel with DORA expertise
- External auditors and penetration testers
- Managed Security Service Providers (MSSP) if needed
- Threat intelligence services

## Cost Implications

DORA compliance typically requires:

- Enhanced ICT risk management framework
- Advanced testing capabilities (TLPT)
- Expanded third-party oversight
- Incident reporting infrastructure
- Training and awareness programs

Estimated additional cost: 20-35% increase over base ISO 27001 compliance for medium-sized financial entities.

---

# Common Pitfalls and Lessons Learned

## Common DORA Compliance Challenges

**Challenge 1: Underestimating Regulatory Reporting Complexity**

- Incident reporting timelines are tight (initial report within hours)
- Classification criteria require judgment and consistency
- Reporting infrastructure must be tested before incidents occur

**Challenge 2: Third-Party Contract Renegotiation**

- Major cloud providers may resist DORA-specific contract terms
- Negotiation timelines can extend 6-12 months
- Some providers may not accept audit rights for authorities

**Challenge 3: TLPT Readiness**

- Organisations not used to red team exercises may struggle
- Requires mature detection and response capabilities
- Blue team readiness critical for realistic testing

**Challenge 4: Concentration Risk Assessment**

- Difficult to quantify concentration risk
- Limited alternative providers in some service categories
- Mitigation strategies may be costly (multi-cloud, vendor diversification)

**Challenge 5: Legacy System Challenges**

- Older systems may lack logging and monitoring
- Patching and upgrades may be infeasible
- Compensating controls required but may not fully mitigate risk

## Best Practices

**Practice 1**: Engage competent authority early for guidance
**Practice 2**: Leverage ISO 27001 as foundation, augment with DORA-specific requirements
**Practice 3**: Establish incident reporting process and test quarterly
**Practice 4**: Prioritize critical ICT service provider relationships
**Practice 5**: Conduct internal TLPT preparation even if not yet designated
**Practice 6**: Participate in sector information sharing arrangements

---

# References and Resources

## DORA Legal Texts

**Primary Regulation**:

- Regulation (EU) 2022/2554 (DORA) - Official Journal of the EU

**Regulatory Technical Standards (RTS)**:

- Commission Delegated Regulation on ICT risk management (expected adoption 2024)
- Commission Delegated Regulation on incident reporting (expected adoption 2024)
- Commission Delegated Regulation on digital operational resilience testing (expected adoption 2024)
- Commission Delegated Regulation on third-party risk oversight (expected adoption 2024)

**ESA Websites**:

- European Banking Authority (EBA): https://www.eba.europa.eu/
- European Securities and Markets Authority (ESMA): https://www.esma.europa.eu/
- European Insurance and Occupational Pensions Authority (EIOPA): https://www.eiopa.europa.eu/

## Related Standards and Frameworks

**ISO Standards**:

- ISO/IEC 27001:2022: Information Security Management
- ISO/IEC 27002:2022: Information Security Controls
- ISO/IEC 27005:2022: Information Security Risk Management
- ISO 22301:2019: Business Continuity Management

**TLPT Frameworks**:

- **TIBER-EU**: Threat Intelligence-Based Ethical Red Teaming (ECB framework)
- CBEST: UK threat-led penetration testing framework
- TIBER-NL: Netherlands TLPT framework
- iCAST: Ireland TLPT framework

**NIST Publications** (informational reference):

- NIST Cybersecurity Framework (CSF)
- NIST SP 800-53: Security and Privacy Controls
- NIST SP 800-61: Computer Security Incident Handling Guide

## Industry Guidance

**Financial Sector**:

- FS-ISAC: Financial Services Information Sharing and Analysis Center
- SWIFT Customer Security Programme (CSP)
- PCI DSS: Payment Card Industry Data Security Standard (where applicable)

**Compliance Consulting**:
Organisations subject to DORA should engage:

- Legal counsel with EU financial regulatory expertise
- Auditors experienced with DORA compliance
- Cybersecurity consultants familiar with TIBER-EU and TLPT

---

# Appendix A: DORA Compliance Self-Assessment Checklist

## ICT Risk Management Framework (Chapter II)

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| Management body approval of ICT risk framework | ⬜ Yes ⬜ No ⬜ Partial | | |
| ICT risk management function established | ⬜ Yes ⬜ No | | |
| Comprehensive ICT asset inventory | ⬜ Yes ⬜ No ⬜ Partial | | |
| Legacy systems identified and risk-assessed | ⬜ Yes ⬜ No | | |
| Network segmentation implemented | ⬜ Yes ⬜ No ⬜ Partial | | |
| Encryption for sensitive data (rest and transit) | ⬜ Yes ⬜ No ⬜ Partial | | |
| Continuous monitoring and detection | ⬜ Yes ⬜ No ⬜ Partial | | |
| Business continuity and disaster recovery plans | ⬜ Yes ⬜ No ⬜ Partial | | |
| RTO/RPO defined for critical functions | ⬜ Yes ⬜ No | | |
| Post-incident reviews and lessons learned | ⬜ Yes ⬜ No | | |
| Annual ICT security awareness training | ⬜ Yes ⬜ No | | |

## Incident Management & Reporting (Chapter III)

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| Incident classification criteria established | ⬜ Yes ⬜ No ⬜ Partial | | |
| Major incident definition documented | ⬜ Yes ⬜ No | | |
| Incident reporting process to competent authority | ⬜ Yes ⬜ No ⬜ N/A | | |
| Initial notification capability (within hours) | ⬜ Yes ⬜ No | | |
| Incident reporting testing conducted | ⬜ Yes ⬜ No | | |

## Digital Operational Resilience Testing (Chapter IV)

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| Annual testing program established | ⬜ Yes ⬜ No ⬜ Partial | | |
| Vulnerability assessments conducted regularly | ⬜ Yes ⬜ No | | |
| Scenario-based BCP/DR testing | ⬜ Yes ⬜ No | | |
| TLPT conducted (if designated) | ⬜ Yes ⬜ No ⬜ N/A ⬜ Pending | | |
| Testing results documented and remediated | ⬜ Yes ⬜ No ⬜ Partial | | |

## Third-Party Risk Management (Chapter V)

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| Third-party risk management framework | ⬜ Yes ⬜ No ⬜ Partial | | |
| ICT third-party service provider register | ⬜ Yes ⬜ No ⬜ Partial | | |
| Pre-contractual due diligence process | ⬜ Yes ⬜ No ⬜ Partial | | |
| DORA-compliant contracts for critical providers | ⬜ Yes ⬜ No ⬜ Partial | | |
| Exit strategies for critical ICT services | ⬜ Yes ⬜ No ⬜ Partial | | |
| Concentration risk assessment conducted | ⬜ Yes ⬜ No | | |
| Annual register submission to authority | ⬜ Yes ⬜ No ⬜ N/A | | |

## Information Sharing (Chapter VI)

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| Participation in threat intelligence sharing | ⬜ Yes ⬜ No ⬜ Planned | | |
| Membership in FS-ISAC or similar | ⬜ Yes ⬜ No ⬜ Planned | | |

---

# Appendix B: Major Incident Notification Template

**DORA Major ICT-Related Incident - Initial Notification**

**To**: [National Competent Authority - Single Point of Contact]  
**From**: [Financial Entity Name]  
**Contact**: [Incident Response Manager Name, Phone, Email]  
**Date/Time**: [ISO 8601 format]  
**LEI (Legal Entity Identifier)**: [LEI]  
**Notification Type**: ⬜ Initial ⬜ Intermediate ⬜ Final

---

**SECTION 1: INCIDENT SUMMARY**

**Incident ID**: [Internal reference number]  
**Detection Date/Time**: [ISO 8601]  
**Incident Start Date/Time** (estimated): [ISO 8601]  
**Current Status**: ⬜ Ongoing ⬜ Contained ⬜ Resolved

**Incident Type**:
⬜ Cyberattack (specify: ransomware, DDoS, malware, phishing, etc.)
⬜ System failure (specify: hardware, software, network)
⬜ Data breach / Data loss
⬜ Third-party provider outage
⬜ Natural disaster impact
⬜ Other (specify): _____________

---

**SECTION 2: IMPACT ASSESSMENT**

**Critical or Important Functions Affected**:

- [Function 1]: [Impact description]
- [Function 2]: [Impact description]

**Service Disruption**:

- **Duration**: [Hours/minutes of disruption]
- **Clients Affected**: [Number and type]
- **Geographic Scope**: [Countries affected]
- **Service Unavailability**: [Which services are down]

**Data Impact**:
⬜ No data affected
⬜ Data potentially compromised: [Type, volume, sensitivity]
⬜ Data confirmed compromised: [Details]

**Financial Impact** (preliminary):
⬜ Not yet determined
⬜ Estimated: [Amount and basis]

**Reputational Impact**:
⬜ Low ⬜ Medium ⬜ High
[Brief description]

---

**SECTION 3: ROOT CAUSE** (preliminary)

[Brief description of suspected or confirmed root cause]

---

**SECTION 4: RESPONSE ACTIONS**

**Actions Taken**:
1. [Action 1 - timestamp]
2. [Action 2 - timestamp]
3. [Action 3 - timestamp]

**Current Response Status**:
[Brief description of ongoing response]

**Ongoing Actions**:

- [Action with expected completion]

---

**SECTION 5: EXTERNAL COORDINATION**

**Third-Party Providers Involved**:

- [Provider 1]: [Involvement]
- [Provider 2]: [Involvement]

**External Notifications**:

- **Clients**: ⬜ Yes ⬜ No ⬜ Planned [Date/time]
- **GDPR Data Protection Authority**: ⬜ Yes ⬜ No ⬜ N/A
- **Other Authorities**: [Specify]

---

**SECTION 6: NEXT UPDATE**

**Next Report Due**: [Date/time]  
**Report Type**: ⬜ Intermediate ⬜ Final

---

**DECLARATION**

I confirm that the information provided in this notification is accurate to the best of my knowledge as of [Date/Time].

**Name**: [Senior Management Representative]  
**Title**: [Title]  
**Signature**: [Digital signature if applicable]

---

**END OF TECHNICAL REFERENCE**

---

*This technical reference supports potential DORA compliance requirements as determined in ISMS-POL-00. All regulatory applicability determinations and binding requirements are defined in ISMS-POL-00 and approved ISMS policy documents.*

*For organisations NOT subject to DORA, this document is for informational awareness only and does NOT create compliance obligations.*

<!-- QA_VERIFIED: 2026-02-01 -->