<!-- ISMS-CORE:POLICY:AI-POL-00:ai:POL:00 -->
**AI-POL-00 — AIMS Regulatory Applicability Framework**
**Authoritative Reference for AI Management System Compliance Obligations**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AIMS Regulatory Applicability Framework |
| **Document Type** | Policy |
| **Document ID** | AI-POL-00 |
| **Document Creator** | AI Governance Officer / Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |
| **AIMS Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [Date - 8 weeks] | AI Governance Officer | Initial draft — three-tier framework, EU AI Act + ISO 42001 scope |
| 0.2 | [Date - 6 weeks] | AI Governance Officer + Legal | Added sector-specific obligations, ISO 42005:2025 tier placement |
| 0.3 | [Date - 4 weeks] | CISO | Aligned with ISMS-POL-00 methodology; added Swiss AI strategy context |
| 0.4 | [Date - 2 weeks] | AI Governance Officer / Legal / CISO | Incorporated stakeholder feedback; forthcoming legislation monitoring section |
| 1.0 | [Date] | AI Governance Officer / Legal / CISO | Initial approved release |

**Review Cycle**: Annual (or upon significant AI regulatory changes, new standard publications, or certification scope changes)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: AI Governance Officer (or designated CISO where no dedicated AI governance role exists)
- Secondary: Chief Information Security Officer (CISO)
- Compliance: Legal / Compliance Officer
- Final Authority: Executive Management

**Related Documents**:

- AI-POL-01 — AIMS Governance and Decision-Making Framework
- ISMS-POL-00 — Regulatory Applicability Framework (ISMS base — mandatory co-reference)
- ISO/IEC 42001:2023 Clause 4.2 (Understanding the needs and expectations of interested parties)
- ISO/IEC 42001:2023 Clause 4.3 (Determining the scope of the AI management system)
- All AIMS policy documents (mandatory reference)

**Distribution**: All AIMS stakeholders, AI governance officers, policy authors, AI system owners, legal/compliance, auditors
**Referenced By**: All AIMS policy documents (AI-POL-01, all AI-POL-A.x.x control group policies)

**Language Strategy**: Where technical or regulatory terms are internationally established (e.g., EU AI Act, GPAI, ISO/IEC, AISIA, NIST AI RMF), English terminology is retained to preserve precision and facilitate cross-border regulatory reference.

---

## Executive Summary

This document provides the **authoritative reference** for interpreting AI regulatory and framework applicability across the entire AI Management System (AIMS).

**Purpose**: Eliminate ambiguity and inconsistency in how AI laws, regulations, and standards are referenced across AIMS policies, procedures, and controls.

**Scope**: All references to AI laws, AI regulations, and AI governance frameworks within AIMS documentation.

**Relationship to ISMS**: This policy is an AI-specific companion to **ISMS-POL-00** (Regulatory Applicability Framework). ISMS-POL-00 governs information security obligations. AI-POL-00 governs AI management and governance obligations. Where obligations overlap (e.g., GDPR Article 22 — automated decision-making, or the EU AI Act's security requirements for high-risk AI), ISMS-POL-00 takes precedence for the information security dimension; AI-POL-00 governs the AI governance dimension. Privacy obligations arising from AI processing personal data are addressed in conjunction with PRIV-POL-00.

**Key Principle**: **AI regulatory applicability must be explicit, not assumed.** References to AI regulations and frameworks fall into three categories:

1. **Mandatory Compliance** — Legal obligations that apply to the organisation
2. **Conditional Applicability** — Requirements that apply only under specific circumstances
3. **Informational Reference** — Best practices and technical guidance

**Usage**: All AIMS policies shall include a "Regulatory Framework" section referencing this document, identifying which tier each cited regulation or standard belongs to.

**Key Terms**: Definitions for terms used throughout this policy are provided in the **Glossary** at the end of this document.

---

## Policy Authority and Boundaries

### Purpose and Scope of This Policy

This policy defines the **identification and applicability** of legal, statutory, regulatory, and contractual requirements for the organisation's AI Management System.

**This policy establishes:**

- Which AI laws and standards apply to the organisation
- Categorisation of AI obligations (Mandatory, Conditional, Informational)
- Assessment methodology for determining applicability based on organisational AI role
- Review and update processes for changes in the AI regulatory landscape

**This policy does NOT establish:**

- AI risk treatment decisions (addressed in AIMS risk management)
- Control implementation requirements (addressed in control group policies and IMPs)
- Compliance status or verification (addressed in compliance monitoring processes)
- Information security obligations (addressed in ISMS-POL-00)
- Privacy obligations for AI processing personal data (addressed in PRIV-POL-00)

**Boundary Principle**: This policy establishes AI regulatory applicability. Implementation, enforcement, and verification are handled through separate AIMS processes and control group policies.

**Integration with ISO/IEC 42001:2023:**

- **Clause 4.2 (Interested Parties)**: AI regulatory requirements constitute the primary interested party obligations. This policy identifies them explicitly.
- **Clause 4.3 (Scope)**: Scope determination is informed by which Tier 1 obligations apply and the organisation's AI role (provider, deployer, or both).
- **Clause 6 (Risk Assessment)**: Regulatory obligations feed into the AI risk register. Tier 1 = High priority, Tier 2 conditional = Medium priority, Tier 3 = Informational input.

**Integration with ISMS-POL-00 and PRIV-POL-00:**

This policy operates alongside ISMS-POL-00 and PRIV-POL-00. Where an AI regulation has information security dimensions (e.g., EU AI Act Article 15 — accuracy, robustness and cybersecurity), ISMS-POL-00 governs the security interpretation. Where an AI regulation has privacy dimensions (e.g., GDPR Article 22 — automated individual decision-making), PRIV-POL-00 governs the data protection interpretation. AI-POL-00 governs the AI management and governance interpretation.

---

## Organisational AI Role Determination

**This step must be completed before applying the regulatory framework.** AI regulatory obligations differ significantly based on the organisation's role in the AI value chain.

### Roles Defined by EU AI Act (Regulation 2024/1689)

| Role | Definition | Obligations |
|------|-----------|-------------|
| **AI Provider** | Develops an AI system or general-purpose AI model with intent to place on the market or put into service under own name or trademark, including by download | Highest obligation level — conformity assessment, technical documentation, post-market monitoring |
| **AI Deployer** | Uses an AI system under own authority for professional purposes | Implement provider instructions, conduct FRIA for high-risk AI, maintain logs, ensure human oversight |
| **AI Importer** | Places on EU market an AI system bearing the name of an entity established outside EU | Verify conformity, retain documentation, report to authorities |
| **AI Distributor** | Makes AI system available on EU market, other than provider or importer | Verify CE marking, documentation, registration |

### Roles Defined by ISO/IEC 42001:2023

| Role | Definition |
|------|-----------|
| **AI Provider** | Develops, trains, deploys, or maintains AI systems (for internal or external use) |
| **AI User / Deployer** | Integrates or uses AI systems developed by third parties |
| **Both** | Most enterprise organisations — develops some AI capabilities internally while using third-party AI tools |

**Assessment action required**: The organisation shall document its role(s) in the AI system inventory (AI-POL-01) for each AI system in scope. Roles may differ per AI system.

---

## Regulatory Applicability Categories

**Mandatory Compliance**
Legal or contractual AI obligations that the organisation MUST comply with. Non-compliance results in legal liability, regulatory fines, supervisory authority investigations, or certification loss.

**Characteristics**:

- Enforceable by a regulatory authority or court
- Non-compliance has legal or financial consequences (fines, enforcement orders, market access restrictions)
- Requires documented evidence of compliance (conformity assessments, technical documentation, incident records)
- Subject to regulatory audits, inspections, and supervisory authority powers

**Conditional Applicability**
AI requirements that apply only when specific conditions are met (e.g., specific AI system types, geographic market exposure, certification sought, customer contracts, regulated sectors).

**Characteristics**:

- Applicability depends on AI system characteristics, deployment context, or market geography
- May become mandatory based on business activities or contractual requirements
- Requires periodic re-assessment as business activities and AI systems evolve

**Informational Reference / Best Practice Alignment**
Frameworks and standards used for technical and organisational guidance, benchmarking, or voluntary alignment. These inform AI governance practices but do not constitute mandatory compliance requirements.

**Characteristics**:

- Voluntary adoption for best practices
- No direct legal enforcement mechanism
- Used for responsible AI implementation guidance
- May become mandatory if referenced in contracts or certification requirements

---

## Compliance Hierarchy

```
┌─────────────────────────────────────────────────────────────────────┐
│                  AI COMPLIANCE HIERARCHY                            │
├─────────────────────────────────────────────────────────────────────┤
│  TIER 1: MANDATORY (Legal / Contractual)                            │
│  • EU AI Act (Regulation 2024/1689) — where placing AI on EU        │
│    market or putting AI into service in the EU                      │
│  • Sector-specific AI obligations (DORA, MiFID II, MDR, etc.)       │
│  • GDPR Article 22 — where AI makes automated decisions about       │
│    individuals with legal or significant effects                    │
│                                                                     │
│  TIER 2: CONDITIONAL (Context-Dependent)                            │
│  • ISO/IEC 42001:2023 — where certification sought or               │
│    contractually required                                           │
│  • ISO/IEC 42005:2025 — AISIA methodology (companion to 42001,      │
│    applies where 42001 certification is in scope)                   │
│  • EU AI Act high-risk conformity assessment obligations            │
│    (where AI system classified as high-risk under Annex III)        │
│  • National AI Acts in markets where organisation operates          │
│                                                                     │
│  TIER 3: INFORMATIONAL (Best Practice / Technical Guidance)         │
│  • NIST AI Risk Management Framework 1.0 (NIST AI RMF)             │
│  • ISO/IEC 23894:2023 (AI risk management guidance)                 │
│  • ISO/IEC 38507:2022 (Governance of AI)                            │
│  • OECD AI Principles (2019, revised 2024)                          │
│  • UNESCO Recommendation on the Ethics of AI (2021)                 │
│  • Swiss Federal Council AI Strategy (2023)                         │
│                                                                     │
│  FORTHCOMING (Monitor — Adopt on Publication / Enactment)           │
│  • Swiss national AI legislation (anticipated)                      │
│  • ISO/IEC 42006 — AIMS internal audit guidance (under dev.)        │
│  • EU AI Liability Directive (under development)                    │
└─────────────────────────────────────────────────────────────────────┘
```

> *If box-drawing characters do not render correctly, refer to the sections below for tier definitions.*

---

# Mandatory Compliance (Tier 1)

> **Note on ISO/IEC 42001:2023 classification**: ISO/IEC 42001:2023 is classified as **Tier 2 (Conditional)** in this framework. It is not a legally enforceable regulation. It becomes obligatory for [Organisation] where certification is actively sought or where a customer contract explicitly requires AIMS compliance. Where neither condition applies, it functions as a voluntary best-practice framework. See the ISO/IEC 42001:2023 section under Tier 2 for full details.

## EU Artificial Intelligence Act (Regulation 2024/1689)

**Applicability**: When placing an AI system on the EU market, putting an AI system into service in the EU, or where AI system outputs are used in the EU — regardless of where the organisation is established. Applies in full from 2 August 2026 (with prohibited AI provisions in force from 2 February 2025, GPAI provisions from 2 August 2025).

**Risk Classification Framework**:

The EU AI Act applies a risk-based approach. Every AI system must be classified:

| Risk Level | Definition | Obligations |
|-----------|-----------|-------------|
| **Unacceptable risk** (Prohibited) | AI systems posing clear threat to fundamental rights or safety | Absolute prohibition — cannot be placed on market. Examples: subliminal manipulation, social scoring, real-time remote biometric identification in public spaces (except narrow law enforcement exceptions), exploitation of vulnerabilities based on age/disability |
| **High-risk** (Annex III) | AI systems in regulated sectors or with significant impact on fundamental rights | Full conformity obligations — see below |
| **Limited risk** | AI systems with specific transparency obligations | Disclose AI interaction to users (chatbots, deepfakes) |
| **Minimal risk** | All other AI systems | No mandatory requirements; voluntary codes of practice |
| **General Purpose AI (GPAI)** | AI models with general capabilities (e.g., LLMs) | Transparency, copyright compliance; systemic risk models have additional obligations |

**High-Risk AI System Categories (Annex III)**:

- Biometric identification and categorisation
- Management and operation of critical infrastructure
- Education and vocational training (access, assessment)
- Employment, workers management and access to self-employment
- Access to and enjoyment of essential private and public services and benefits
- Law enforcement
- Migration, asylum and border control management
- Administration of justice and democratic processes

**Key Requirements for High-Risk AI Providers**:

- Article 9: Quality management system (QMS) including risk management
- Article 10: Training, validation and testing data requirements
- Article 11: Technical documentation (before placing on market)
- Article 12: Record-keeping (logging throughout operational lifetime)
- Article 13: Transparency and provision of information to deployers
- Article 14: Human oversight measures
- Article 15: Accuracy, robustness and cybersecurity requirements
- Article 16: Obligations of providers (registration, CE marking, post-market monitoring)
- Article 26: Obligations of deployers (fundamental rights impact assessment for public bodies and certain private deployers)

**Key Requirements for GPAI Model Providers**:

- Article 53: Transparency and copyright compliance (technical documentation, training data summary)
- Article 55: Systemic risk models (adversarial testing, incident reporting, cybersecurity measures)

**AIMS Impact**:

- AI system inventory must classify each system by EU AI Act risk category
- High-risk systems require conformity assessment before EU market placement
- Technical documentation maintained per Article 11 requirements
- AISIA (A.5.2–A.5.5) aligned with Fundamental Rights Impact Assessment (FRIA) for high-risk AI
- A.6.2.6 (operation and monitoring) must address post-market monitoring obligations
- A.8.4 (communication of incidents) must address EU AI Act serious incident reporting timelines

**Supervisory Authority**: National market surveillance authority of each EU Member State; European AI Office (European Commission) for GPAI models

**Reference**: Regulation (EU) 2024/1689, Official Journal of the EU, 12 July 2024. Application dates: prohibited AI from 2 February 2025; GPAI provisions from 2 August 2025; full application from 2 August 2026.

---

## GDPR Article 22 — Automated Decision-Making

**Applicability**: When the organisation uses AI systems to make **solely automated decisions** that produce **legal effects** or **significantly affect** individuals (e.g., automated credit scoring, automated recruitment screening, automated benefits eligibility, automated fraud detection resulting in account restriction).

**Key Requirements**:

- Right not to be subject to solely automated decisions with legal or significant effects (Article 22(1))
- Exceptions: explicit consent, contractual necessity, or authorised by Union or Member State law — all require safeguards
- Where exceptions apply: inform individuals, implement meaningful human oversight, provide right to contest decision and obtain human review
- DPIAs required for systematic automated processing likely to result in high risk (Article 35)

**AIMS Impact**:

- AI systems making consequential automated decisions must be identified in the AI system inventory
- Mandatory human oversight controls (A.6.2.6) for AI-driven decisions affecting individuals
- Transparency disclosures (A.8.2, A.8.5) must address GDPR Article 22 information obligations
- Link to PRIV-POL-00 and PRIV-POL-A.1.3.11 (Automated Decision-Making) for full data protection obligations

**Supervisory Authority**: Competent EU/EEA data protection authority (DPA)

**Reference**: Regulation (EU) 2016/679 Article 22; Guidelines 05/2020 on automated individual decision-making and profiling (EDPB)

---

## Sector-Specific AI Obligations

Certain regulated sectors impose AI-specific obligations in addition to the EU AI Act. Applicability depends on the organisation's sector and activities.

**Financial Services — DORA (Regulation 2022/2554)**:

- Article 28–30: ICT third-party risk management applies to AI tools and AI service providers
- DORA classifies AI tools used in critical functions as ICT third-party dependencies subject to full TPRM obligations
- AI systems used in trading, risk management, or customer services in scope for ICT incident reporting
- **Applicability trigger**: Organisation is a DORA-regulated entity (financial institution, investment firm, insurance undertaking, crypto-asset service provider, etc.)

**Medical Devices — MDR (Regulation 2017/745) and IVDR (Regulation 2017/746)**:

- AI-powered medical devices and in vitro diagnostic medical devices are subject to MDR/IVDR conformity assessment
- AI medical device software (SaMD) may be classified as high-risk under both MDR and EU AI Act — dual conformity assessment may apply
- **Applicability trigger**: Organisation develops or places on market AI-powered medical devices or diagnostic software

**Aviation, Automotive, Rail, Maritime (CE marking regimes)**:

- AI systems embedded in safety-critical products regulated under existing product safety legislation may require dual conformity under both EU AI Act and sector-specific regulation
- **Applicability trigger**: Organisation develops AI systems integrated into safety-critical products in these sectors

**Assessment action required**: Legal/Compliance shall assess sector-specific AI obligations annually and document applicability findings in the regulatory register.

---

# Conditional Applicability (Tier 2)

These regulations and standards apply **only when specific conditions are met**.

## ISO/IEC 42001:2023 — AI Management System

**Standard**: ISO/IEC 42001:2023 (First Edition) — Information technology — Artificial intelligence — Management system

**Applicability Triggers**:

- The organisation **seeks ISO/IEC 42001:2023 certification** (either standalone or combined with ISO 27001 certification)
- A customer contract **explicitly requires** AIMS compliance with this standard
- The organisation **voluntarily adopts** ISO 42001 as its AI governance framework (in which case treat as operationally binding)

**Classification Note**: ISO/IEC 42001:2023 is classified Tier 2 (Conditional) in this framework. It is not a legally enforceable regulation. It does not become mandatory simply because the organisation develops or uses AI systems — the EU AI Act fulfils that role for EU market exposure. Where certification is sought or contractually required, it is treated as a binding operational commitment equivalent to Tier 1 for the duration of certification.

**Key Requirements**:

- Clause 4: Context of the organisation (understanding context, interested parties, AIMS scope)
- Clause 5: Leadership (AI policy, roles and responsibilities, top management commitment)
- Clause 6: Planning (AI risk assessment, AI system impact assessment, AI objectives)
- Clause 7: Support (resources, competence, awareness, communication, documented information)
- Clause 8: Operation (operational planning, AI risk assessment execution, risk treatment, AISIA execution)
- Clause 9: Performance evaluation (monitoring, internal audit, management review)
- Clause 10: Improvement (nonconformity, corrective action, continual improvement)
- Annex A (normative): 36 controls across 9 domains (A.2–A.10)
- Annex B (normative): Implementation guidance for all Annex A controls

**AIMS Delivery**: The full ISO 42001 Annex A control set is delivered through the AI-POL-A.x.x control group policies in `53-isms-core-ai/`. The organisation's Statement of Applicability (SoA) shall reference these policies.

**Integration with ISO 27001**: ISO 42001 uses the same High-Level Structure (HLS/Annex SL) as ISO 27001:2022. Organisations holding ISO 27001 certification can integrate or combine AIMS and ISMS processes under a shared management system. Shared clause areas (7, 9, 10) can reuse existing ISMS infrastructure.

**Reference**: ISO/IEC 42001:2023, Information technology — Artificial intelligence — Management system, December 2023

---

## ISO/IEC 42005:2025 — AI System Impact Assessment

**Standard**: ISO/IEC 42005:2025 (First Edition) — Information technology — Artificial intelligence — AI system impact assessment

**Applicability Triggers**:

- ISO/IEC 42001:2023 is in scope (Tier 2 trigger above applies) — ISO 42005:2025 provides the methodology for ISO 42001 Clause 6.1.4 (AI system impact assessment) and Annex A controls A.5.2–A.5.5
- The organisation formally adopts AISIA as part of its AI governance programme
- Customer contracts or regulatory obligations (e.g., EU AI Act FRIA requirements) require documented AI impact assessment methodology

**What ISO 42005:2025 Covers**:

- Clause 5: Developing and implementing the AISIA process (scope, thresholds, sensitive uses, restricted uses, impact scales, responsibilities, approval, monitoring and review)
- Clause 6: Documenting the AI system impact assessment (AI system description, functionalities and capabilities, intended use, data information and quality, algorithm and model information, deployment environment, relevant interested parties, actual and reasonably foreseeable impacts, benefits and harms, measures to address harms)
- Annex A (informative): Guidance for use with ISO/IEC 42001
- Annex B (informative): Guidance for use with ISO/IEC 23894 (AI risk management)

**AIMS Impact**:

- All AISIA templates in 53-isms-core-ai/ shall be built against ISO 42005:2025 Clause 6 documentation requirements
- AISIA methodology in AIMS documents must reference ISO 42005:2025, not general guidance
- ISO 42005:2025 AISIA aligns with EU AI Act Fundamental Rights Impact Assessment (FRIA) — organisations subject to both should document the cross-reference

**Reference**: ISO/IEC 42005:2025, Information technology — Artificial intelligence — AI system impact assessment, May 2025

---

## EU AI Act High-Risk Conformity Assessment

**Applicability Trigger**: Organisation acts as AI provider or deployer for an AI system classified as **high-risk** under EU AI Act Annex III.

**Additional Obligations Triggered**:

- Conformity assessment procedure (Article 43) — either internal control or third-party assessment (notified body) depending on AI system category
- Registration in EU AI Act database (Article 49) before market placement
- CE marking and declaration of conformity
- Post-market monitoring system (Article 72)
- Serious incident reporting to national authority (Article 73) within defined timelines

**Assessment action required**: For each AI system in scope for EU market, classify under EU AI Act risk categories and document in AI system inventory. High-risk classification triggers conformity assessment planning.

---

# Informational Reference (Tier 3)

These frameworks inform AI governance practices but do not constitute mandatory compliance requirements. They are used for guidance, benchmarking, and best practice implementation.

## NIST AI Risk Management Framework 1.0 (NIST AI RMF)

**Published**: January 2023 — National Institute of Standards and Technology (US)

**Relevance**: Provides a voluntary framework for managing AI risks across four core functions: GOVERN, MAP, MEASURE, MANAGE. Internationally recognised as a practical AI risk management reference even outside the US.

**How used in AIMS**:

- AI risk register structure informed by NIST AI RMF risk taxonomy (GOVERN, MAP, MEASURE, MANAGE)
- NIST AI RMF Profile concept supports organisation-specific AI risk prioritisation
- Crosswalk: NIST AI RMF ↔ ISO 42001 mappings assist dual-framework organisations

**Reference**: NIST AI RMF 1.0, NIST AI 100-1, January 2023

---

## ISO/IEC 23894:2023 — AI Risk Management

**Published**: February 2023

**Relevance**: Provides guidance on how organisations can manage risks specifically related to AI. Extends ISO 31000 (risk management) with AI-specific considerations. Referenced by ISO 42001 Annex B and ISO 42005 Annex B.

**How used in AIMS**:

- AI risk assessment methodology informed by ISO 23894 risk identification and analysis guidance
- AI risk taxonomy informed by ISO 23894 categories (technical, operational, societal)

**Reference**: ISO/IEC 23894:2023, Information technology — Artificial intelligence — Guidance on risk management

---

## ISO/IEC 38507:2022 — Governance of AI for Organisations

**Published**: April 2022

**Relevance**: Provides guidance on the governance implications of using AI by organisations. Addresses how governing body members can enable, extend and evolve AI governance. Referenced in ISO 42001 Annex B.2.3.

**How used in AIMS**:

- Governance structure for AI (A.3.2) informed by ISO 38507 board-level AI governance guidance
- Top management accountability framework aligned with ISO 38507 principles

**Reference**: ISO/IEC 38507:2022, Information technology — Artificial intelligence — Governance implications of the use of AI by organizations

---

## OECD AI Principles (2019, revised 2024)

**Published**: May 2019 (revised June 2024) — Organisation for Economic Co-operation and Development

**Relevance**: International reference for responsible AI. Adopted by G20. Widely referenced in national AI legislation including the EU AI Act. Five principles: inclusive growth and well-being; human-centred values and fairness; transparency and explainability; robustness and safety; accountability.

**How used in AIMS**:

- Responsible AI principles in AI-POL-01 aligned with OECD AI Principles
- EU AI Act Recitals reference OECD Principles — alignment reduces interpretative gaps

**Reference**: OECD AI Principles, OECD/LEGAL/0449, adopted 22 May 2019, revised 2024

---

## Swiss Federal Council AI Strategy (2023)

**Published**: December 2023 — Swiss Federal Council

**Relevance**: Switzerland's government AI strategy outlines responsible AI principles for public administration and signals direction for future Swiss AI legislation. Not legally binding for private sector as of 2026.

**Swiss Context**: Switzerland has not enacted a standalone national AI Act as of April 2026. Swiss AI governance for private sector organisations is primarily addressed through:

- Swiss nDSG (Federal Act on Data Protection, SR 235.1) — applies to AI processing personal data
- Swiss ISG (Federal Act on Information Security, SR 128) — applies to AI systems in critical national infrastructure
- Swiss Federal Council AI Strategy — voluntary principles
- EU AI Act — applies to Swiss organisations placing AI on the EU market

**Monitor**: Swiss national AI legislation is anticipated to follow EU AI Act framework. Assign responsibility for monitoring to Legal/Compliance.

---

# Forthcoming (Monitor — Adopt on Publication or Enactment)

These instruments are under development or anticipated. [Organisation] shall monitor and adopt when published or enacted.

| Instrument | Status | Expected Impact |
|-----------|--------|----------------|
| **Swiss national AI legislation** | Anticipated — no draft published as of April 2026 | Likely to mirror EU AI Act for CH-market AI systems; AIMS already aligned |
| **ISO/IEC 42006** — Requirements for auditing AI management systems | Under development (ISO/IEC JTC 1/SC 42) | Will define internal/external AIMS audit requirements — update AIMS audit programme on publication |
| **EU AI Liability Directive** | Under development | May impose civil liability for AI system harms; triggers AIMS risk register updates |
| **EU AI Act delegated acts** | Expected 2025–2026 | Technical details for conformity assessment, standardisation mandates, GPAI model thresholds |
| **NIST AI RMF 2.0 / sector profiles** | Expected periodically | Update NIST AI RMF Tier 3 reference on publication |

**Monitoring responsibility**: Legal/Compliance Officer, with support from AI Governance Officer. Review cycle: quarterly scan, annual policy update if triggered.

---

# Assessment and Review Process

## Determining Applicability

For each new AI system developed or acquired, and at each annual review cycle, the AI Governance Officer and Legal/Compliance shall:

1. **Identify the organisation's AI role** for the system (provider, deployer, both) per the role definitions above
2. **Assess Tier 1 applicability** — EU AI Act risk classification; GDPR Article 22 trigger; sector-specific triggers
3. **Assess Tier 2 triggers** — Is ISO 42001 certification sought or contractually required? Is the system high-risk under EU AI Act requiring conformity assessment?
4. **Review Tier 3 relevance** — Document which informational frameworks inform implementation for the system
5. **Update the AI system inventory** (AI-POL-01) with regulatory classification findings
6. **Update the AIMS SoA** if new obligations affect control selection

## Annual Review

This policy shall be reviewed annually by the AI Governance Officer and Legal/Compliance. Triggers for out-of-cycle review:

- New AI regulation enacted in a jurisdiction where the organisation operates
- New AI standard published that affects the AIMS control framework
- Significant change in the organisation's AI portfolio (new AI system in high-risk category)
- Regulatory enforcement action against a peer organisation that reveals a new obligation interpretation

---

# Glossary

| Term | Definition |
|------|-----------|
| **AI Act** | EU Artificial Intelligence Act — Regulation (EU) 2024/1689 on artificial intelligence |
| **AI Deployer** | Natural or legal person using an AI system under their own authority for professional purposes (EU AI Act definition) |
| **AI Provider** | Person or entity developing an AI system or GPAI model with intent to place on the EU market (EU AI Act definition) |
| **AI System** | A machine-based system designed to operate with varying levels of autonomy that may exhibit adaptiveness, and that — for explicit or implicit objectives — infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions (ISO/IEC 42001:2023 definition, aligned with EU AI Act Article 3) |
| **AIMS** | AI Management System — management system for the responsible development, deployment and use of AI systems |
| **AISIA** | AI System Impact Assessment — formal assessment of potential consequences of an AI system for individuals and societies (ISO/IEC 42001:2023 Clause 6.1.4; detailed in ISO/IEC 42005:2025) |
| **FRIA** | Fundamental Rights Impact Assessment — required under EU AI Act Article 26 for deployers of certain high-risk AI systems affecting natural persons |
| **GPAI** | General Purpose AI — AI model trained on broad data, capable of serving multiple tasks (e.g., large language models); subject to specific obligations under EU AI Act Title V |
| **High-Risk AI** | AI system falling within EU AI Act Annex III categories, subject to full conformity obligations before EU market placement |
| **Mandatory** | Tier 1 — legally or contractually enforceable obligation with consequences for non-compliance |
| **Conditional** | Tier 2 — obligation that becomes applicable when specific triggers are met |
| **Informational** | Tier 3 — voluntary best practice framework informing AIMS implementation without direct enforcement |
| **SoA** | Statement of Applicability — document listing all 36 ISO 42001 Annex A controls with applicability decisions and justifications |
| **Systemic Risk** | Risk associated with GPAI models with very high training computation (≥10^25 FLOPs) posing adverse effects at EU scale |

---

<!-- QA_VERIFIED: 2026-04-15 -->
