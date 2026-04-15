<!-- ISMS-CORE:POLICY:AI-POL-A.8.2-5:ai:POL:a.8.2-5 -->
**AI-POL-A.8.2-5 — Information for Interested Parties**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Information for Interested Parties |
| **Document Type** | Policy |
| **Document ID** | AI-POL-A.8.2-5 |
| **Document Creator** | AI Governance Officer / Communications Officer |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **AIMS Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | AI Governance Officer / Communications Officer | Initial policy for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual (or upon significant change to AI system portfolio or external communication obligations)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: AI Governance Officer
- Secondary: Legal / Communications Officer
- Compliance: Chief Information Security Officer (CISO)
- Final Authority: Executive Management

**Related Documents**:

- AI-POL-00 (AIMS Regulatory Applicability Framework)
- AI-POL-01 (AIMS Governance and Decision-Making Framework)
- AI-POL-A.6.2 (AI System Lifecycle — technical documentation A.6.2.7)
- AI-IMP-A.8.2-5-UG (Information for Interested Parties — User Guide)
- AI-IMP-A.8.2-5-TG (Information for Interested Parties — Technical Guide)
- PRIV-POL-00 (Privacy Regulatory Applicability — where AI incidents involve personal data)
- ISO/IEC 42001:2023 Controls A.8.2, A.8.3, A.8.4, A.8.5
- ISO/IEC 42001:2023 Annex B.8 (Implementation guidance — Information for interested parties)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for providing information to interested parties about AI systems — covering documentation for AI system users (A.8.2), external reporting on AI systems (A.8.3), communication of AI incidents and near-misses to interested parties (A.8.4), and the overarching framework for determining what information must be provided and to whom (A.8.5) — in accordance with ISO/IEC 42001:2023 Controls A.8.2 through A.8.5.

**Scope**: All AI systems within the AIMS scope; all information and communication obligations towards internal users, external parties, affected individuals, regulators, and the public.

**Purpose**: Define WHAT information must be provided about AI systems, to WHOM, WHEN, and in WHAT form. Implementation detail in AI-IMP-A.8.2-5-UG and AI-IMP-A.8.2-5-TG.

**Combined Control Rationale**: A.8.2 through A.8.5 form the transparency and communication framework for the AIMS. A.8.5 sets the overarching obligation to determine appropriate information for each interested party category; A.8.2 addresses documentation for users specifically; A.8.3 addresses external reporting; A.8.4 addresses incident communication. Together these controls operationalise the AI transparency principle.

---

## Scope and Applicability

### ISO/IEC 42001:2023 Control Statements

**Control A.8.2 — AI system documentation and information for users**
The organisation shall provide information and documentation about the AI system to the users of the AI system.

**Control A.8.3 — External reporting**
The organisation shall determine and implement a process to report externally on its AI systems to relevant parties and in response to requests for information.

**Control A.8.4 — Communication of incidents and near-misses**
The organisation shall communicate about AI incidents and near-misses to relevant parties in an appropriate manner.

**Control A.8.5 — Information for interested parties**
The organisation shall determine and provide information about its AI systems to the interested parties to the extent that is appropriate.

### What This Policy Covers

- Documentation and information requirements for AI system users (A.8.2)
- External reporting obligations and processes (A.8.3)
- AI incident and near-miss communication requirements (A.8.4)
- Interested party information framework — who gets what, when, and how (A.8.5)

### What This Policy Does NOT Cover

- Internal AI incident response and investigation procedures (addressed in AI-POL-A.8.2-5 IMP and ISMS incident management)
- AI system technical documentation for governance purposes (addressed in AI-POL-A.6.2 — A.6.2.7)
- GDPR data subject rights communication obligations (addressed in PRIV-POL-00)

### Regulatory Framework

**Tier 1: Mandatory Compliance** (per AI-POL-00):

- **EU AI Act (Regulation 2024/1689)**: Article 13 — transparency obligations for high-risk AI systems; providers must ensure systems are sufficiently transparent; Article 50 — transparency obligations for AI systems interacting with natural persons (AI-generated content, emotion recognition, deep fakes); Article 73 — notifiable serious incidents for high-risk AI
- **GDPR**: Article 13–14 (information obligations for personal data processing); Article 33–34 (personal data breach notification — applies where AI incidents involve personal data breaches)

**Tier 2: Conditional** (per AI-POL-00):

- **ISO/IEC 42001:2023**: Controls A.8.2–A.8.5 — applies where AIMS certification is in scope or contractually required
- **Sector-specific reporting obligations**: Financial services AI incident reporting (EBA, FINMA); critical infrastructure AI incident reporting (NIS2 Article 23 for in-scope operators) — applicable where [Organisation]'s AI systems fall within regulated sectors

**Tier 3: Informational** (per AI-POL-00):

- NIST AI RMF: GOVERN 5.x — organisational policies for AI transparency; RESPOND 2.x — incident communication practices
- OECD AI Principles: Principle 1.3 — transparency and explainability

---

## Policy Statements: AI System Documentation for Users (A.8.2)

### User Documentation Requirement

[Organisation] SHALL provide documentation and information about each AI system to the persons and organisations that use it. User documentation shall be provided before or at the point of deployment and kept current throughout the system's operational life.

### Mandatory User Documentation Content

For each in-scope AI system, user documentation shall include:

| Documentation Element | Content Required |
|----------------------|----------------|
| **System description** | What the AI system does; the technology type; how it reaches its outputs |
| **Intended use** | The specific purposes and contexts for which the system is designed and validated |
| **Out-of-scope uses** | Uses for which the system has not been designed or validated; uses that are explicitly prohibited |
| **Inputs and outputs** | What inputs the system takes; what outputs or decisions it produces; interpretation guidance |
| **Performance characteristics** | Known accuracy, error rates, or performance metrics relevant to users; conditions under which performance may degrade |
| **Limitations** | Known limitations of the AI system; situations in which outputs should not be relied upon; edge cases |
| **Human oversight requirements** | Where and how human review is required before acting on AI outputs; override mechanisms available |
| **How to use responsibly** | Instructions for responsible use consistent with the intended use specification |
| **How to report concerns** | Process for users to report AI system errors, unexpected outputs, or concerns (links to A.3.3 reporting channel) |
| **Contact information** | Who to contact for support, questions, or incident reports |

### EU AI Act Transparency Notice

For AI systems that interact with natural persons (including end-users, customers, or members of the public), [Organisation] SHALL ensure that:

- Persons are informed when they are interacting with an AI system (unless this is obvious from context)
- Persons are informed when AI is used to generate content that could be mistaken for human-generated content
- Where emotion recognition or biometric categorisation is used, persons are informed before interaction

These disclosures shall be made in clear, plain language appropriate to the audience.

### Documentation Format and Accessibility

User documentation shall be:

- Written in plain language appropriate to the intended user audience — not primarily technical
- Available in the language(s) used by the intended user population
- Accessible — not buried in terms of service or technical annexes
- Version-controlled and linked to the AI system version it describes

---

## Policy Statements: External Reporting (A.8.3)

### External Reporting Requirement

[Organisation] SHALL define and implement a process for reporting externally on its AI systems to relevant parties, including in response to requests for information.

### Proactive External Reporting

[Organisation] SHALL maintain and publish information about its AI systems appropriate to each external audience:

| External Audience | Information Provided |
|------------------|---------------------|
| **Regulatory authorities** | Information required by applicable regulations (EU AI Act technical documentation; conformity assessment documentation; FRIA summaries where required); provided on request or as mandated |
| **Customers and clients** | AI system capabilities; intended use; limitations; how AI affects services provided; how to raise concerns |
| **Partners and suppliers** | AI systems that interact with partner systems or data; relevant interface specifications; responsibility boundaries |
| **Public / affected individuals** | Where [Organisation]'s AI systems affect individuals who are not direct users, appropriate transparency information shall be provided through accessible channels (website, notices, etc.) |

### Responding to Information Requests

[Organisation] SHALL have a documented process for responding to external requests for AI system information:

- Designated contact point for AI-related external enquiries
- Response timeframes defined (standard: within 10 business days; regulatory requests: per applicable deadline)
- Escalation path: AI System Owner → AI Governance Officer → Legal
- Record of enquiries and responses retained

### AI Act Notifiable Information

For AI systems classified as high-risk under the EU AI Act, [Organisation] shall maintain, and provide to market surveillance authorities upon request:

- Technical documentation (Article 11 content)
- EU declaration of conformity
- Logs and records as required by Article 12
- Post-market monitoring data relevant to serious incidents (Article 72)

---

## Policy Statements: Communication of AI Incidents and Near-Misses (A.8.4)

### Incident Communication Requirement

[Organisation] SHALL communicate about AI incidents and near-misses to relevant parties in an appropriate manner and in accordance with applicable legal obligations.

### AI Incident Definitions

For the purpose of this policy:

| Term | Definition |
|------|-----------|
| **AI incident** | An occurrence where an AI system caused or contributed to harm, an unexpected outcome, a safety event, or a material deviation from intended behaviour in a way that affected or could have affected an individual, group, organisation, or society |
| **Near-miss** | An event where an AI system's behaviour had the potential to cause harm but did not, either through intervention or chance — sufficiently significant to warrant documentation and learning |
| **Serious incident** | An AI incident that results in: death or serious injury; significant disruption to critical services; breach of fundamental rights; or other harm meeting thresholds under the EU AI Act Article 3(49) |

### Internal Incident Communication

AI incidents and near-misses shall be communicated internally per the AIMS incident management process:

- AI System Owner notified immediately upon detection
- AI Governance Officer notified within 24 hours for material incidents; within 3 business days for near-misses
- CISO notified where incident has information security dimensions
- DPO / Privacy Officer notified where incident involves personal data processing

### External Incident Communication

| Party | Trigger | Requirement |
|-------|---------|------------|
| **Regulatory authority** | Serious incident involving high-risk AI (EU AI Act Article 73); personal data breach (GDPR Article 33); sector-specific incident (per applicable regulation) | Report within required timeframe per applicable obligation; report content per regulatory template |
| **Affected individuals** | AI incident that results in harm to identified individuals; personal data breach with high risk to individuals (GDPR Article 34) | Notification without undue delay; plain language description of incident, consequences, and remediation |
| **Customers / business partners** | AI incident that materially affects services provided to customers; incident involving customer data | Notification as required by contractual obligations and applicable regulation |
| **Market surveillance authority (EU AI Act)** | Serious incident for high-risk AI systems | Immediate notification (Article 73); content per Article 73(1) |

### Notification Content Requirements

External incident notifications shall include, as appropriate:

- Description of the AI system and the incident
- Date, time, and duration of the incident
- Nature and scale of impact on affected parties
- Immediate steps taken to contain or mitigate the incident
- Ongoing investigation status
- Contact point for affected parties

### Non-Retaliation for Reporting

Individuals who report AI incidents or near-misses in good faith, including through the A.3.3 concerns reporting channel, shall not face retaliation. This principle applies to reports made both internally and, where applicable, to regulatory authorities.

---

## Policy Statements: Information for Interested Parties (A.8.5)

### Interested Party Information Requirement

[Organisation] SHALL determine, for each in-scope AI system, what information about the system is appropriate to provide to each category of interested party, and shall provide that information.

### Interested Party Categories and Information Mapping

| Interested Party Category | Information Appropriate to Provide |
|--------------------------|-----------------------------------|
| **Direct users** (persons operating or using the AI system) | Full user documentation per A.8.2; performance characteristics; limitations; responsible use guidance; reporting channel |
| **Affected individuals** (persons whose interests are affected by AI outputs even if not direct users) | Transparency notice; nature and purpose of AI use; whether AI influences decisions about them; recourse options; contact for enquiries |
| **Customers and clients** (organisations purchasing AI-enabled services) | Service description including AI components; intended use boundaries; incident notification obligations; liability allocation (per A.10.4) |
| **Suppliers and third parties** (organisations providing components to AI systems) | Interface and integration requirements; data handling requirements; incident reporting obligations to [Organisation] |
| **Regulatory authorities** | Technical documentation; conformity evidence; incident reports; information as required by applicable regulation |
| **Certification / audit bodies** | Full AIMS documentation set; AISIA records; SoA; evidence of control implementation |
| **General public** | Where AI systems affect the public: high-level description of AI use; transparency notice; contact point for concerns |

### Information Appropriateness Assessment

When determining what information to provide, the AI Governance Officer shall consider:

- **Relevance**: Does this party have a legitimate interest in this information?
- **Proportionality**: Is the level of detail proportionate to the party's role and the system's impact level?
- **Sensitivity**: Does the information contain commercially sensitive or security-sensitive details that should not be disclosed?
- **Legal obligation**: Is disclosure required by applicable law, regulation, or contract?
- **Privacy**: Does the information contain or reveal personal data?

Where disclosure would reveal security vulnerabilities or commercially sensitive information, the AI Governance Officer may approve a summary or redacted version provided the substance of the transparency obligation is met.

### Transparency as a Principle

[Organisation]'s approach to AI transparency shall be governed by the principle that **affected parties should have sufficient information to understand how AI is being used in matters that concern them, and to exercise meaningful oversight or recourse**. Transparency is not merely compliance with minimum disclosure obligations; it is a means of building justified trust in AI systems.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|----------------|
| **AI Governance Officer** | Own the information for interested parties framework; approve external reporting; approve external incident communications; determine information appropriateness per A.8.5 |
| **AI System Owner** | Maintain user documentation for owned AI systems; report incidents per A.8.4 obligations; maintain contact information for user enquiries |
| **Legal / Communications Officer** | Draft external communications; advise on regulatory notification obligations; manage regulatory authority enquiries |
| **DPO / Privacy Officer** | Advise on GDPR-related notification obligations; review external communications involving personal data |
| **CISO** | Coordinate incident communication where incident has information security dimensions; ensure security-sensitive information is not inappropriately disclosed |

---

## Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| User documentation | Per-AI-system user documentation with version history | Duration of system + 3 years |
| External reporting records | Records of proactive disclosures and responses to information requests | 5 years |
| Incident communication records | Records of external incident notifications, content, and recipients | Duration of system + 5 years (longer where regulatory obligation requires) |
| Interested party information register | Documentation of what information has been determined appropriate for each interested party category | Current + 3 years |
| Transparency notices | Records of transparency disclosures made to affected individuals | Duration of AI system + 5 years |

---

## Audit Considerations

Auditors verifying compliance with A.8.2–A.8.5 should expect to find:

- User documentation available for all in-scope AI systems, linked to system version
- Evidence that transparency notices are provided where AI systems interact with natural persons
- A documented process for external reporting including handling of information requests
- Incident communication procedures defining who is notified, when, and with what content
- Evidence that incident communications were issued following material AI incidents
- An interested party information mapping showing what information is provided to each category and why

---

<!-- QA_VERIFIED: 2026-04-15 -->
