<!-- ISMS-CORE:REF:ISMS-REF-NIS2-network-and-information-security-directi:framework:REF:nis2 -->
**ISMS-REF-NIS2 — Network and Information Security Directive 2 Requirements Reference**
**EU Cybersecurity Requirements for Essential and Important Entities (Non-ISMS Technical Reference)**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | NIS2 Requirements Reference |
| **Document Type** | Internal - Technical Reference (Not ISMS) |
| **Document ID** | ISMS-REF-NIS2 |
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
| 1.0 | [Date] | CISO / Legal/Compliance | Initial technical reference for EU entities |

**Review Cycle**: Annual (or upon national transposition law updates)  
**Next Review Date**: [Date + 12 months]  
**Approvers**: Legal/Compliance / CISO (technical reference, no ISMS approval required)

**Distribution**: Compliance team, CISO, Legal counsel (for organisations subject to NIS2)

---

⚠️ **IMPORTANT – NON-ISMS TECHNICAL SUPPORT DOCUMENT**

This document is provided for informational and awareness purposes only.

- This document is NOT part of the Information Security Management System (ISMS).
- This document does NOT define mandatory requirements unless [Organisation] is a NIS2-regulated entity.
- This document does NOT establish binding requirements, deadlines, KPIs, or SLAs for non-regulated entities.
- This document does NOT mandate the adoption of NIS2 requirements for organisations not subject to NIS2.
- This document does NOT override or extend any ISMS policy.

**Applicability Determination**:
NIS2 requirements apply ONLY IF [Organisation]:

- Is an essential or important entity operating in the EU in covered sectors
- Falls within size thresholds (medium/large enterprises typically)
- Provides services categorized under NIS2 Annex I (essential) or Annex II (important)
- Operates in an EU member state that has transposed NIS2 into national law

For all other organisations, this document serves solely as:

- Technical reference for potential NIS2 requirements
- Context for business expansion into EU regulated sectors
- Awareness of EU cybersecurity standards
- **This document must not be used as audit evidence unless [Organisation] is NIS2-regulated**

Use of this document does not imply NIS2 applicability, compliance obligations, or regulatory status.

**Critical Positioning Statement**:
This document intentionally provides regulatory detail beyond what applies to most organisations. Its purpose is awareness only for organisations that MAY become subject to NIS2 as they expand operations, or that provide services to NIS2-regulated entities. No auditor conclusions shall be drawn from the presence, absence, or implementation status of any NIS2 requirement listed herein unless [Organisation] is explicitly NIS2-regulated.

---

# Document Purpose and Scope

## Purpose

This document provides a technical overview of the Network and Information Security Directive 2 (Directive (EU) 2022/2555) requirements for essential and important entities in the EU. It is intended to support:

- Awareness of NIS2 requirements for covered EU sectors
- Understanding of NIS2's cybersecurity risk management framework
- Context for organisations expanding into NIS2-regulated sectors
- Potential future applicability assessment
- Mapping NIS2 requirements to ISO 27001:2022 controls

## What This Document Is NOT

This document does NOT:

- Establish mandatory requirements for non-NIS2-regulated organisations
- Define [Organisation]'s compliance obligations (see POL-00 for regulatory applicability)
- Create audit criteria unless [Organisation] is NIS2-regulated
- Replace legal or compliance counsel interpretation
- Constitute legal advice on NIS2 compliance
- Cover all national transposition variations (NIS2 is a Directive requiring national implementation)
- Establish implementation procedures or verification processes

## Relationship to ISMS

This document is a **non-binding technical reference** UNLESS [Organisation] is subject to NIS2 (as determined in ISMS-POL-00 Section 3.3).

**If [Organisation] IS NIS2-regulated:**

- NIS2 requirements become Tier 1 (Mandatory Compliance) per POL-00
- This document provides implementation guidance
- ISMS controls must demonstrate NIS2 compliance
- Incident reporting and national CSIRT coordination required

**If [Organisation] IS NOT NIS2-regulated:**

- NIS2 remains Tier 3 (Informational Reference) per POL-00
- This document is for awareness only
- No NIS2 compliance obligations exist
- ISMS controls follow ISO 27001:2022 only

## Content Organisation

This reference organizes NIS2 requirements by:

- Scope and applicability (entities, sectors, size thresholds)
- Cybersecurity risk management measures (Article 21)
- Incident reporting obligations (Article 23)
- Supply chain security (Article 21)
- Supervisory framework and penalties
- Mapping to ISO 27001:2022 Annex A controls

---

# NIS2 Overview and Applicability

## What is NIS2?

**Directive (EU) 2022/2555** on measures for a high common level of cybersecurity across the Union, replacing the original NIS Directive (2016/1148).

**Key Dates**:

- **Entry into Force**: January 16, 2023
- **Transposition Deadline**: October 17, 2024 (EU member states must implement into national law)
- **Application**: Varies by member state (typically 6-12 months after national law publication)

**Purpose**:

- Strengthen cybersecurity resilience across EU critical sectors
- Harmonize cybersecurity requirements across member states
- Expand scope beyond original NIS Directive
- Establish incident reporting framework
- Introduce supervisory and enforcement measures

**Legal Nature**: 

- Directive (not Regulation), so member states must transpose into national law
- National variations may exist in implementation details
- Core requirements remain consistent across EU

**Supervisory Authorities**:

- National competent authorities (designated by each member state)
- Computer Security Incident Response Teams (CSIRTs)
- Single Points of Contact (SPOCs)

## Scope and Covered Sectors

NIS2 establishes two categories of entities:

**Essential Entities** (Annex I - Higher impact, stricter requirements):

| Sector | Sub-Sectors |
|--------|-------------|
| **Energy** | Electricity, district heating/cooling, oil, gas, hydrogen |
| **Transport** | Air, rail, water, road transport |
| **Banking** | Credit institutions |
| **Financial Market Infrastructures** | Trading venues, central counterparties, central securities depositories |
| **Health** | Healthcare providers, EU reference laboratories, pharmaceutical manufacturers for critical medicines |
| **Drinking Water** | Suppliers and distributors of drinking water |
| **Wastewater** | Wastewater management and collection |
| **Digital Infrastructure** | Internet exchange points, DNS service providers (excluding root name servers), TLD name registries, cloud computing service providers, data center service providers, content delivery networks, trust service providers, public electronic communications networks, publicly available electronic communications services |
| **ICT Service Management** | Managed service providers, managed security service providers |
| **Public Administration** | Central government entities |
| **Space** | Operators of ground-based infrastructure supporting space services |

**Important Entities** (Annex II - Medium impact, proportionate requirements):

| Sector | Sub-Sectors |
|--------|-------------|
| **Postal and Courier Services** | Postal and courier service providers |
| **Waste Management** | Waste collection, treatment, disposal |
| **Manufacture, Production, Distribution of Chemicals** | Chemical substances and mixtures |
| **Food Production, Processing, Distribution** | Food operators (large scale) |
| **Manufacturing** | Medical devices, computer/electronic/optical products, electrical equipment, machinery, motor vehicles/trailers, other transport equipment |
| **Digital Providers** | Online marketplaces, online search engines, social networking services platforms |
| **Research** | Research organisations |

## Size and Scope Criteria

**Size Thresholds** (Article 2):

| Enterprise Size | Employees | Annual Turnover OR Balance Sheet | NIS2 Applicability |
|-----------------|-----------|-----------------------------------|-------------------|
| **Large** | ≥ 250 | > €50M turnover OR > €43M balance sheet | In scope (if in covered sector) |
| **Medium** | 50-249 | ≤ €50M turnover AND ≤ €43M balance sheet | In scope (if in covered sector) |
| **Small** | 10-49 | ≤ €10M turnover AND ≤ €10M balance sheet | Generally out of scope |
| **Micro** | < 10 | ≤ €2M turnover AND ≤ €2M balance sheet | Out of scope |

**Exceptions**:

- **Sole providers**: Even if small, may be in scope if only provider of essential service
- **Public administration**: Size thresholds do not apply
- **Critical infrastructure**: Member states may include additional entities

## Applicability Determination

**NIS2 applies to [Organisation] IF**:

| Criteria | Status | Evidence |
|----------|--------|----------|
| Operates in EU member state | ⬜ Yes ⬜ No | [Country] |
| Falls within covered sector (Annex I or II) | ⬜ Yes ⬜ No | [Sector] |
| Meets size thresholds (medium or large) | ⬜ Yes ⬜ No | [Employees / Turnover] |
| Designated by national authority | ⬜ Yes ⬜ No ⬜ Unknown | [Designation letter if applicable] |
| Member state transposed NIS2 into national law | ⬜ Yes ⬜ No ⬜ Pending | [National law reference] |

**If Criteria Met**: NIS2 requirements are **Tier 1 (Mandatory Compliance)** per POL-00 Section 3.3

**If Criteria Not Met**: NIS2 requirements remain **Tier 3 (Informational Reference)** per POL-00

**Note on National Transposition**:
Each EU member state implements NIS2 through national legislation. Organisations must consult their national cybersecurity authority for specific requirements, as implementation details may vary.

---

# Article 21 - Cybersecurity Risk Management Measures

## Overview

Article 21 establishes **minimum cybersecurity risk management measures** that essential and important entities must implement.

**Legal Obligation** (Article 21(1)):
Member states shall ensure entities take "appropriate and proportionate" technical, operational, and organisational measures to manage cybersecurity risks and minimize impact of incidents.

**Proportionality Principle**:
Measures must be appropriate to:

- Nature and scope of entity's activities
- Size of entity
- Likelihood and severity of incidents
- State of the art in cybersecurity

## Ten Minimum Measures (Article 21(2))

**1. Risk Analysis and Information System Security Policies**

**Requirement**:

- Policies on risk analysis and information system security
- Comprehensive risk assessment methodology
- Regular risk reviews and updates
- Documentation of risk treatment decisions

**ISO 27001:2022 Mapping**:

- Clause 6.1.2: Information security risk assessment
- Clause 6.1.3: Information security risk treatment
- A.5.1: Policies for information security

**Implementation Guidance**:

- Annual risk assessment minimum
- Risk-based approach aligned with business impact
- Board-level risk reporting
- Integration with enterprise risk management

---

**2. Incident Handling**

**Requirement**:

- Policies and procedures for incident handling
- Incident detection, classification, response, and recovery
- Communication plans (internal and external)
- Lessons learned and continuous improvement

**ISO 27001:2022 Mapping**:

- A.5.24: Information security incident management planning and preparation
- A.5.25: Assessment and decision on information security events
- A.5.26: Response to information security incidents
- A.5.27: Learning from information security incidents

**NIS2-Specific**:

- Incident reporting to national authorities (Article 23)
- Coordination with national CSIRT
- Communication with customers and stakeholders

---

**3. Business Continuity and Crisis Management**

**Requirement**:

- Business continuity plans (BCP)
- Disaster recovery plans (DRP)
- Crisis management procedures
- Backup and recovery capabilities
- Testing and validation

**ISO 27001:2022 Mapping**:

- A.5.29: Information security during disruption
- A.5.30: ICT readiness for business continuity
- A.8.13: Information backup
- A.8.14: Redundancy of information processing facilities

**NIS2 Emphasis**:

- Focus on continuity of essential services
- Recovery time objectives (RTO) for critical functions
- Regular testing (at least annually)

---

**4. Supply Chain Security**

**Requirement**:

- Measures to secure supply chain
- Assessment of supplier cybersecurity practices
- Contractual security requirements
- Monitoring of supplier security posture
- Risk-based approach to supplier relationships

**ISO 27001:2022 Mapping**:

- A.5.19: Information security in supplier relationships
- A.5.20: Addressing information security within supplier agreements
- A.5.21: Managing information security in the ICT supply chain
- A.5.22: Monitoring, review and change management of supplier services

**NIS2-Specific**:

- Explicit focus on cybersecurity aspects of supply chain
- Includes both direct suppliers and supply chain dependencies
- Vulnerability disclosure and coordination with suppliers

---

**5. Security in Network and Information Systems Acquisition, Development and Maintenance**

**Requirement**:

- Secure development lifecycle
- Security requirements in procurement
- Security testing before deployment
- Maintenance and patching procedures
- Change management controls

**ISO 27001:2022 Mapping**:

- A.8.4: Access to source code
- A.8.8: Management of technical vulnerabilities
- A.8.9: Configuration management
- A.8.25: Secure development life cycle
- A.8.26: Application security requirements
- A.8.27: Secure system architecture and engineering principles
- A.8.28: Secure coding
- A.8.29: Security testing in development and acceptance
- A.8.30: Outsourced development

**Implementation**:

- Security by design principles
- Vulnerability management program
- Patch management with defined SLAs
- Secure configuration baselines

---

**6. Policies and Procedures to Assess Effectiveness of Cybersecurity Risk Management Measures**

**Requirement**:

- Regular assessment of security control effectiveness
- Internal audits
- Security metrics and KPIs
- Continuous monitoring and improvement

**ISO 27001:2022 Mapping**:

- Clause 9.1: Monitoring, measurement, analysis and evaluation
- Clause 9.2: Internal audit
- Clause 9.3: Management review
- Clause 10.1-10.2: Continual improvement

**Assessment Methods**:

- Internal security assessments
- Vulnerability assessments
- Penetration testing
- Third-party audits
- Compliance reviews

---

**7. Basic Cyber Hygiene Practices and Cybersecurity Training**

**Requirement**:

- User awareness and training programs
- Basic cyber hygiene measures
- Role-based security training
- Regular security awareness campaigns
- Training effectiveness measurement

**ISO 27001:2022 Mapping**:

- A.6.3: Information security awareness, education and training
- A.6.4: Disciplinary process (accountability)

**Cyber Hygiene Measures**:

- Strong password policies
- Multi-factor authentication (MFA)
- Phishing awareness and testing
- Secure remote working guidance
- BYOD and mobile device security
- Email and web security

**Training Requirements**:

- Annual mandatory training for all personnel
- Specialized training for IT and security staff
- Phishing simulation testing
- Training completion tracking

---

**8. Cryptography and Encryption**

**Requirement**:

- Use of cryptography to protect data
- Encryption of sensitive data at rest and in transit
- Cryptographic key management
- Alignment with current encryption standards

**ISO 27001:2022 Mapping**:

- A.8.24: Use of cryptography

**Implementation Standards**:

- TLS 1.2 minimum (TLS 1.3 preferred) for data in transit
- AES-256 for data at rest
- PKI and certificate management
- No use of deprecated algorithms (DES, 3DES, MD5, SHA-1)
- Hardware Security Modules (HSM) for high-value keys

---

**9. Human Resources Security, Access Control Policies and Asset Management**

**Requirements**:

**Human Resources Security**:

- Background checks for sensitive positions
- Security responsibilities in employment contracts
- Termination procedures (access revocation)

**Access Control**:

- User identification and authentication
- Least privilege principle
- Regular access reviews
- Privileged access management

**Asset Management**:

- Inventory of information assets
- Asset classification and handling
- Acceptable use policies
- Asset disposal procedures

**ISO 27001:2022 Mapping**:

- A.5.9: Inventory of information and other associated assets
- A.5.10: Acceptable use of information and other associated assets
- A.5.12: Classification of information
- A.5.15: Access control
- A.5.16: Identity management
- A.5.17: Authentication information
- A.5.18: Access rights
- A.6.1: Screening
- A.6.2: Terms and conditions of employment
- A.6.4: Disciplinary process
- A.6.5: Responsibilities after termination or change of employment
- A.8.2: Privileged access rights
- A.8.3: Information access restriction
- A.8.10: Information deletion

---

**10. Multi-Factor Authentication, Secured Voice/Video/Text Communications, and Emergency Communication**

**Requirements**:

**Multi-Factor Authentication (MFA)**:

- MFA for remote access
- MFA for privileged accounts
- MFA for access to sensitive systems/data
- Risk-based authentication where appropriate

**Secured Communications**:

- Encryption for voice, video, and text communications
- Secure collaboration platforms
- End-to-end encryption for sensitive communications
- VPN for remote access

**Emergency Communication Systems**:

- Out-of-band communication channels for incidents
- Emergency contact lists
- Alternative communication methods (SMS, phone, secure messaging)
- Crisis communication procedures

**ISO 27001:2022 Mapping**:

- A.5.14: Information transfer
- A.8.5: Secure authentication
- A.8.20: Networks security
- A.8.23: Web filtering (communication security)

**NIS2-Specific**:
This is one of the most prescriptive requirements in NIS2, explicitly mandating MFA and secured communications - more specific than typical ISO 27001 implementations.

---

## Management Body Responsibility (Article 21(3))

**Leadership Accountability**:
Member states shall ensure that management body:

- **Approves** cybersecurity risk management measures
- **Oversees** implementation
- Can be **held liable** for non-compliance

**Liability Provisions** (Article 21(5)):

- Management body can be held liable for infringements
- Member states may provide for direct liability
- Training required for management body members

**ISO 27001:2022 Mapping**:

- Clause 5.1: Leadership and commitment
- Clause 5.2: Policy
- Clause 9.3: Management review

**NIS2 Enhancement**:
Explicit management liability is unique to NIS2 and not present in ISO 27001.

---

# Article 23 - Incident Reporting

## Overview

Entities must notify the national CSIRT or competent authority of significant incidents.

**Legal Obligation**:

- **Without undue delay**: Initial notification
- **Three-stage process**: Early warning, incident notification, final report

## Reporting Timeline

| Stage | Timing | Content |
|-------|--------|---------|
| **Early Warning** | Without undue delay (≤ 24 hours from awareness) | Awareness of significant incident, initial indication of possible cross-border impact |
| **Incident Notification** | Without undue delay (≤ 72 hours from awareness) | Initial assessment (impact, severity, indicators of compromise), preliminary technical details |
| **Final Report** | ≤ 1 month from incident notification | Detailed description, severity, impact, root cause, applied/ongoing mitigation measures |
| **Intermediate Reports** | Upon request by CSIRT/authority OR significant change in handling | Updated status and information |

## Significant Incident Criteria

Incidents are considered **significant** if:

- Caused or likely to cause severe operational disruption
- Caused or likely to cause considerable financial loss
- Affected or likely to affect other natural/legal persons (customers, partners)

**Assessment Factors** (Annex I to Directive - Implementing Act):

- Number of affected users/entities
- Duration of incident
- Geographical spread
- Severity of disruption of services
- Extent of impact on economic and societal activities

## Reporting Content

**Early Warning** (24 hours):

- Indication that significant incident occurred
- Whether incident suspected to be result of unlawful/malicious act
- Whether incident likely to have cross-border impact

**Incident Notification** (72 hours):

- Description of incident (type, scope, timeline)
- Indicators of compromise (IOCs) if available
- Initial assessment of severity and impact
- Type of threat or root cause (if known)
- Applied mitigation measures

**Final Report** (1 month):

- Detailed incident description
- Type of incident and root cause analysis
- Severity assessment with justification
- Impact on service provision and customers
- Mitigation and remediation measures
- Cross-border impact assessment (if applicable)
- Lessons learned

## Reporting Exemptions

Entities **may choose not to report** if:

- Incident is covered by other sector-specific reporting (e.g., GDPR, DORA for financial entities)
- Provided the information reaches the CSIRT or competent authority

**Coordination**:

- NIS2 incident reports may overlap with GDPR personal data breach reporting
- DORA reporting for financial entities may satisfy NIS2 requirements
- Member states may establish single reporting portal

**ISO 27001:2022 Mapping**:

- A.5.26: Response to information security incidents (internal reporting)
- A.5.5: Contact with authorities (external notification)

**NIS2 vs. ISO 27001**:
ISO 27001 does not mandate external regulatory reporting timelines - this is NIS2-specific.

---

# Supply Chain Security (Article 21(2)(d) and Recitals)

## Overview

NIS2 explicitly requires entities to address cybersecurity risks in their supply chain.

**Requirement**:

- Security measures to address vulnerabilities specific to each direct supplier
- Overall quality of products and services
- Cybersecurity practices of suppliers

## Supplier Assessment

**Pre-Contract Assessment**:

- Supplier cybersecurity posture evaluation
- Security certifications (ISO 27001, SOC 2, etc.)
- Incident history and response capabilities
- Data handling and protection practices
- Subcontractor risk assessment

**Ongoing Monitoring**:

- Regular security reviews (annual minimum)
- Continuous monitoring where appropriate
- Incident notification requirements
- Security audit rights
- Performance against security SLAs

## Contractual Requirements

Contracts with suppliers should include:

- Security obligations and standards
- Incident notification requirements
- Audit and assessment rights
- Data protection and confidentiality
- Subcontracting restrictions
- Liability and indemnification
- Termination rights for security breaches

**ISO 27001:2022 Mapping**:

- A.5.19: Information security in supplier relationships
- A.5.20: Addressing information security within supplier agreements
- A.5.21: Managing information security in the ICT supply chain

## Supply Chain Risk Management

**Risk-Based Approach**:

- Criticality assessment (impact if supplier fails)
- Concentration risk (single supplier dependencies)
- Geographic risk (location of suppliers/data)
- Substitutability (availability of alternatives)

**Mitigation Strategies**:

- Vendor diversification
- Contractual protections
- Escrow arrangements for critical software
- Business continuity clauses
- Exit strategies

---

# Supervisory and Enforcement Framework

## National Competent Authorities

Each member state designates:

- **Competent authority**: Responsible for NIS2 supervision
- **CSIRT (Computer Security Incident Response Team)**: Technical incident response
- **Single Point of Contact (SPOC)**: Liaison function for cross-border cooperation

**Supervisory Powers** (Article 32):

- On-site and remote inspections
- Security audits by qualified auditors
- Requests for information
- Requests for evidence of implementation
- Access to data, documents, facilities

## Enforcement Measures (Article 34)

**Administrative Sanctions**:

- Binding instructions
- Warnings
- Orders to comply
- Temporary prohibition of management body members
- **Fines** (see Section 6.3)
- Public disclosure of non-compliance

**Urgency Measures**:
If serious and immediate risk, authorities may:

- Order immediate implementation of security measures
- Restrict or prohibit use of compromised systems
- Temporarily suspend services

## Penalties (Article 34)

**Essential Entities** (Annex I):

- Up to **€10,000,000** OR
- **2% of total worldwide annual turnover** (whichever is higher)

**Important Entities** (Annex II):

- Up to **€7,000,000** OR
- **1.4% of total worldwide annual turnover** (whichever is higher)

**Factors Considered**:

- Gravity and duration of infringement
- Intentional or negligent character
- Actions taken to mitigate damage
- Previous infringements
- Financial benefits gained or losses avoided
- Cooperation with authority

**Management Liability** (Article 21(5)):

- Member states may hold management body members personally liable
- Temporary prohibition from management positions possible

---

# ISO 27001:2022 to NIS2 Mapping

## Control Mapping Matrix

| NIS2 Requirement | NIS2 Article | ISO 27001:2022 Control | Gap Analysis |
|------------------|--------------|------------------------|--------------|
| Risk analysis and security policies | Art. 21(2)(a) | Clause 6.1.2-6.1.3, A.5.1 | Aligned |
| Incident handling | Art. 21(2)(b) | A.5.24-5.27 | NIS2: Adds external reporting |
| Business continuity & crisis management | Art. 21(2)(c) | A.5.29-5.30, A.8.13-8.14 | Aligned |
| Supply chain security | Art. 21(2)(d) | A.5.19-5.22 | NIS2: More explicit focus |
| Secure acquisition, development, maintenance | Art. 21(2)(e) | A.8.4, A.8.8-8.9, A.8.25-8.30 | Aligned |
| Effectiveness assessment | Art. 21(2)(f) | Clause 9.1-9.3, 10.1-10.2 | Aligned |
| Basic cyber hygiene and training | Art. 21(2)(g) | A.6.3 | Aligned |
| Cryptography and encryption | Art. 21(2)(h) | A.8.24 | Aligned |
| HR security, access control, asset mgmt | Art. 21(2)(i) | A.5.9-5.18, A.6.1-6.5, A.8.2-8.3 | Aligned |
| MFA and secured communications | Art. 21(2)(j) | A.5.14, A.8.5, A.8.20 | **NIS2-specific**: Prescriptive MFA requirement |
| Incident reporting to authorities | Art. 23 | A.5.5, A.5.26 | **NIS2-specific**: Mandated timelines |
| Management body responsibility | Art. 21(3) | Clause 5.1-5.2 | **NIS2-specific**: Personal liability |

## Key Gaps Between ISO 27001:2022 and NIS2

**Gap 1: Regulatory Incident Reporting with Timelines**

- ISO 27001: Internal incident management, optional authority contact
- NIS2: Mandatory reporting to national CSIRT/authority within 24/72 hours

**Gap 2: Prescriptive MFA Requirement**

- ISO 27001: Secure authentication (method flexible)
- NIS2: Explicit multi-factor authentication requirement

**Gap 3: Management Liability**

- ISO 27001: No legal liability provisions
- NIS2: Management body can be held liable, including personal penalties

**Gap 4: Enforcement and Penalties**

- ISO 27001: Certification suspension/withdrawal
- NIS2: Significant financial penalties (up to €10M or 2% turnover)

## NIS2 Compliance with ISO 27001 Foundation

**Key Insight**:
ISO 27001:2022 certification provides strong foundation for NIS2 compliance. Main gaps are:
1. Incident reporting process and timelines
2. MFA implementation validation
3. Management body oversight and liability framework
4. National registration and supervision

Organisations with ISO 27001 typically require **10-20% additional effort** to achieve NIS2 compliance, primarily in incident reporting infrastructure and management governance.

---

# Implementation Considerations

## NIS2 Compliance Timeline

**If [Organisation] is NIS2-regulated entity**:

**Pre-Application (Before national law takes effect)**:

- Confirm NIS2 applicability status
- Gap assessment against Article 21 measures
- Incident reporting process establishment
- Management body briefing and approval

**0-6 Months (Initial compliance period)**:

- Implement mandatory cybersecurity measures
- Establish incident reporting capability
- Register with national competent authority (if required)
- Supply chain security assessments

**6-12 Months (Maturity phase)**:

- Testing and validation of all measures
- Management body oversight mechanisms
- Incident reporting testing
- First annual review and assessment

**Ongoing**:

- Continuous monitoring and improvement
- Annual assessment of effectiveness
- Incident reporting (as incidents occur)
- Management reviews and board reporting

## Resource Requirements

**Personnel**:

- Cybersecurity function with defined responsibilities
- Incident response team
- Supply chain security specialists
- Compliance and reporting function
- Management body engagement (training and oversight)

**Technology**:

- MFA infrastructure (enterprise-wide)
- Incident detection and response tools (SIEM, EDR)
- Backup and disaster recovery infrastructure
- Encrypted communication platforms
- Vulnerability management tools

**External Support**:

- Legal counsel with NIS2 expertise (member state-specific)
- External auditors for effectiveness assessment
- Incident response retainer (DFIR services)
- Managed Security Service Provider (MSSP) if needed

## Cost Implications

NIS2 compliance typically requires:

- Enhanced technical controls (MFA, encryption, monitoring)
- Incident reporting infrastructure
- Supply chain security program
- Management oversight framework
- Training and awareness programs

Estimated additional cost: **10-25% increase** over base ISO 27001 compliance for medium-sized entities.

**Penalty Risk**:
Non-compliance penalties can be severe (€7-10M or 1.4-2% turnover), making compliance investment cost-effective risk mitigation.

---

# Common Pitfalls and Lessons Learned

## Common NIS2 Compliance Challenges

**Challenge 1: Determining Applicability**

- Entity classification (essential vs. important) can be ambiguous
- Size thresholds at group vs. subsidiary level
- National transposition variations across member states
- Sole provider determinations

**Challenge 2: Incident Reporting Process**

- 24-hour early warning is very tight timeline
- Incident classification criteria require judgment
- Coordination with existing reporting (GDPR, sector-specific)
- Testing reporting process before real incidents

**Challenge 3: Management Body Engagement**

- Board members may lack cybersecurity expertise
- Liability concerns require clear governance framework
- Training and awareness for non-technical executives
- Balancing oversight with operational delegation

**Challenge 4: Supply Chain Complexity**

- Large number of suppliers to assess
- Limited leverage with major suppliers (e.g., cloud providers)
- Subcontractor visibility challenges
- Balancing security with operational efficiency

**Challenge 5: MFA Implementation at Scale**

- Legacy systems may not support MFA
- User experience and adoption challenges
- Cost of MFA infrastructure for all users
- Exceptions and compensating controls for technical constraints

## Best Practices

**Practice 1**: Engage national competent authority early for guidance on applicability
**Practice 2**: Leverage ISO 27001 as foundation, augment with NIS2-specific requirements
**Practice 3**: Establish incident reporting infrastructure and test quarterly
**Practice 4**: Implement MFA enterprise-wide (not just for NIS2 compliance)
**Practice 5**: Integrate NIS2 into existing ERM and compliance programs
**Practice 6**: Provide board-level cybersecurity training and regular reporting
**Practice 7**: Document proportionality justifications for risk-based decisions

---

# References and Resources

## NIS2 Legal Texts

**Primary Directive**:

- Directive (EU) 2022/2555 (NIS2 Directive) - Official Journal of the EU

**Implementing Acts and Guidelines**:

- Commission Implementing Regulation on incident reporting (expected 2024-2025)
- ENISA guidelines on NIS2 implementation
- National transposition laws (vary by member state)

**EU Agencies**:

- **ENISA** (European Union Agency for Cybersecurity): https://www.enisa.europa.eu/
- NIS2 dedicated pages and implementation support

## National Competent Authorities

Organisations must consult their **national cybersecurity authority** for:

- National transposition law specifics
- Registration requirements
- Incident reporting procedures
- Supervisory expectations

**Examples of National Authorities**:

- **Germany**: BSI (Bundesamt für Sicherheit in der Informationstechnik)
- **France**: ANSSI (Agence nationale de la sécurité des systèmes d'information)
- **Netherlands**: NCSC (National Cyber Security Centrum)
- **Italy**: ACN (Agenzia per la Cybersicurezza Nazionale)
- **Spain**: CCN-CERT (Centro Criptológico Nacional)
- **Poland**: NASK (Naukowa i Akademicka Sieć Komputerowa)

## Related Standards and Frameworks

**ISO Standards**:

- ISO/IEC 27001:2022: Information Security Management
- ISO/IEC 27002:2022: Information Security Controls
- ISO/IEC 27005:2022: Information Security Risk Management
- ISO 22301:2019: Business Continuity Management

**NIST Publications** (informational reference):

- NIST Cybersecurity Framework (CSF)
- NIST SP 800-53: Security and Privacy Controls

**Industry Guidance**:

- ENISA NIS2 Guidelines and Best Practices
- National CSIRT incident handling guides
- Sector-specific guidance (varies by industry)

## Compliance Resources

Organisations subject to NIS2 should engage:

- Legal counsel with EU cybersecurity regulatory expertise
- Auditors experienced with NIS2 compliance
- Cybersecurity consultants familiar with national transposition
- National competent authority for clarifications

---

# Appendix A: NIS2 Compliance Self-Assessment Checklist

## Applicability Determination

| Criteria | Status | Notes |
|----------|--------|-------|
| Entity operates in EU member state | ⬜ Yes ⬜ No | [Specify country/countries] |
| Entity falls within Annex I or II sectors | ⬜ Yes (Annex I) ⬜ Yes (Annex II) ⬜ No | [Specify sector] |
| Entity meets size thresholds (≥50 employees) | ⬜ Yes ⬜ No | [Employees: ___ / Turnover: ___] |
| Entity designated by national authority | ⬜ Yes ⬜ No ⬜ Unknown | |
| National transposition law in effect | ⬜ Yes ⬜ No ⬜ Pending | [National law reference] |

**Overall NIS2 Applicability**: ⬜ Essential Entity ⬜ Important Entity ⬜ Not Applicable

---

## Article 21(2) - Cybersecurity Risk Management Measures

| Measure | Status | Evidence Location | Notes |
|---------|--------|-------------------|-------|
| (a) Risk analysis and security policies | ⬜ Yes ⬜ No ⬜ Partial | | |
| (b) Incident handling procedures | ⬜ Yes ⬜ No ⬜ Partial | | |
| (c) Business continuity and crisis management | ⬜ Yes ⬜ No ⬜ Partial | | |
| (d) Supply chain security measures | ⬜ Yes ⬜ No ⬜ Partial | | |
| (e) Security in acquisition, development, maintenance | ⬜ Yes ⬜ No ⬜ Partial | | |
| (f) Effectiveness assessment procedures | ⬜ Yes ⬜ No ⬜ Partial | | |
| (g) Basic cyber hygiene and training | ⬜ Yes ⬜ No ⬜ Partial | | |
| (h) Cryptography and encryption | ⬜ Yes ⬜ No ⬜ Partial | | |
| (i) HR security, access control, asset management | ⬜ Yes ⬜ No ⬜ Partial | | |
| (j) MFA, secured communications, emergency comms | ⬜ Yes ⬜ No ⬜ Partial | | |

---

## Article 21(3) - Management Body Responsibility

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| Management body approval of risk management measures | ⬜ Yes ⬜ No | | |
| Management body oversight of implementation | ⬜ Yes ⬜ No ⬜ Partial | | |
| Cybersecurity training for management body | ⬜ Yes ⬜ No ⬜ Planned | | |
| Regular cybersecurity reporting to management body | ⬜ Yes ⬜ No | | |

---

## Article 23 - Incident Reporting

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| Incident classification criteria defined | ⬜ Yes ⬜ No ⬜ Partial | | |
| Incident reporting process to CSIRT/authority | ⬜ Yes ⬜ No | | |
| Early warning capability (24 hours) | ⬜ Yes ⬜ No | | |
| Incident notification capability (72 hours) | ⬜ Yes ⬜ No | | |
| Final report capability (1 month) | ⬜ Yes ⬜ No | | |
| Incident reporting testing conducted | ⬜ Yes ⬜ No ⬜ Planned | | |
| CSIRT/authority contact established | ⬜ Yes ⬜ No | | |

---

## Registration and Supervision

| Requirement | Status | Evidence Location | Notes |
|-------------|--------|-------------------|-------|
| Registered with national competent authority (if required) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Point of contact designated | ⬜ Yes ⬜ No | | |
| Prepared for supervisory inspections | ⬜ Yes ⬜ No ⬜ Partial | | |

---

# Appendix B: Incident Notification Template (NIS2)

**NIS2 Significant Incident Notification**

**To**: [National CSIRT / Competent Authority]  
**From**: [Entity Name]  
**Contact**: [Incident Response Manager Name, Phone, Email]  
**Date/Time**: [ISO 8601 format]  
**Entity Classification**: ⬜ Essential (Annex I) ⬜ Important (Annex II)  
**Sector**: [Specify sector per Annex I or II]  
**Notification Type**: ⬜ Early Warning ⬜ Incident Notification ⬜ Final Report ⬜ Intermediate Report

---

## SECTION 1: INCIDENT SUMMARY

**Incident ID**: [Internal reference number]  
**Awareness Date/Time**: [When entity became aware - ISO 8601]  
**Incident Start Date/Time** (estimated): [ISO 8601]  
**Current Status**: ⬜ Ongoing ⬜ Contained ⬜ Resolved

**Incident Type**:
⬜ Cyberattack (specify: ransomware, DDoS, malware, phishing, data breach, etc.)
⬜ System failure (specify: hardware, software, network, power)
⬜ Third-party provider issue
⬜ Natural disaster
⬜ Human error
⬜ Other (specify): _____________

---

## SECTION 2: SIGNIFICANCE ASSESSMENT

**Why is this incident significant?** (Check all that apply):
⬜ Caused/likely to cause severe operational disruption of essential service
⬜ Caused/likely to cause considerable financial loss
⬜ Affected/likely to affect other natural or legal persons (customers, partners, public)

**Service Impact**:

- **Duration of disruption**: [Hours/minutes]
- **Number of users/customers affected**: [Estimate]
- **Geographic scope**: [Countries/regions affected]
- **Essential services affected**: [List]

---

## SECTION 3: CROSS-BORDER IMPACT

**Is cross-border impact suspected?**
⬜ Yes ⬜ No ⬜ Unknown

**If Yes**:

- **Affected countries**: [List]
- **Nature of cross-border impact**: [Description]

---

## SECTION 4: MALICIOUS ACT ASSESSMENT

**Is incident suspected to be result of unlawful or malicious act?**
⬜ Yes ⬜ No ⬜ Unknown

**If Yes**:

- **Type of threat**: [e.g., ransomware, APT, insider threat]
- **Indicators of compromise (IOCs)**: [List if available]

---

## SECTION 5: TECHNICAL DETAILS (For Incident Notification & Final Report)

**Root Cause** (if known):
[Description]

**Attack Vector** (if applicable):
⬜ Phishing/Social Engineering
⬜ Vulnerability exploitation
⬜ Brute force / Credential stuffing
⬜ Supply chain compromise
⬜ Insider threat
⬜ Other: _____________

**Affected Systems**:

- [System 1]: [Impact]
- [System 2]: [Impact]

---

## SECTION 6: RESPONSE ACTIONS

**Mitigation Measures Taken**:
1. [Action 1 - timestamp]
2. [Action 2 - timestamp]
3. [Action 3 - timestamp]

**Ongoing Response**:
[Description of current response activities]

**Estimated Recovery Time**: [If known]

---

## SECTION 7: IMPACT ASSESSMENT (For Final Report)

**Operational Impact**:

- **Service downtime**: [Total hours]
- **Degraded service period**: [Hours]
- **Number of affected users**: [Final count]

**Financial Impact**:
⬜ Not yet quantified
⬜ Estimated: [Amount and basis]
⬜ No significant financial impact

**Data Impact**:
⬜ No data affected
⬜ Data potentially compromised: [Type, volume]
⬜ Data confirmed compromised: [Details]

**Reputational Impact**:
⬜ Low ⬜ Medium ⬜ High
[Description]

---

## SECTION 8: LESSONS LEARNED (For Final Report)

**Root Cause Analysis Summary**:
[Detailed root cause]

**Contributing Factors**:
[Factors that enabled or exacerbated incident]

**Remediation Actions**:
1. [Action to prevent recurrence]
2. [Action to improve detection]
3. [Action to enhance response]

**Timeline for Remediation**: [Completion dates]

---

## SECTION 9: EXTERNAL COORDINATION

**Other Authorities Notified**:
⬜ Data Protection Authority (GDPR breach): [Date]
⬜ Law Enforcement: [Which agency, date]
⬜ Other regulatory authorities: [Specify]

**Public Communication**:
⬜ Yes ⬜ No ⬜ Planned
[If yes, describe scope and timing]

---

## SECTION 10: NEXT STEPS

**Next Report Type**: ⬜ Intermediate ⬜ Final ⬜ None expected  
**Next Report Due**: [Date/time if applicable]

---

**DECLARATION**

I confirm that the information provided in this notification is accurate to the best of my knowledge as of [Date/Time].

**Name**: [Authorized Representative]  
**Title**: [Title]  
**Signature**: [Digital signature if applicable]

---

**END OF TECHNICAL REFERENCE**

---

*This technical reference supports potential NIS2 compliance requirements as determined in ISMS-POL-00. All regulatory applicability determinations and binding requirements are defined in ISMS-POL-00 and approved ISMS policy documents.*

*For organisations NOT subject to NIS2, this document is for informational awareness only and does NOT create compliance obligations.*

<!-- QA_VERIFIED: 2026-02-01 -->