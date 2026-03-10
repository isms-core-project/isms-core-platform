<!-- ISMS-CORE:POLICY:PRIV-POL-00:privacy:POL:00 -->
**PRIV-POL-00 — Privacy Regulatory Applicability Framework**
**Authoritative Reference for PIMS Compliance Obligations**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Privacy Regulatory Applicability Framework |
| **Document Type** | Policy |
| **Document ID** | PRIV-POL-00 |
| **Document Creator** | Data Protection Officer (DPO) |
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
| 0.1 | [Date - 8 weeks] | DPO | Initial draft — three-tier framework structure, GDPR + FADP scope |
| 0.2 | [Date - 6 weeks] | DPO + Legal | Added ISO 27701:2025 and ISO 27018:2025 tiers; international scope conditions |
| 0.3 | [Date - 4 weeks] | CISO | Aligned with ISMS-POL-00 methodology; added cloud and cloud security references |
| 0.4 | [Date - 2 weeks] | DPO/Legal/CISO | Incorporated stakeholder feedback; added ISO 27017 forthcoming note |
| 1.0 | [Date] | DPO/Legal/CISO | Initial approved release |

**Review Cycle**: Annual (or upon significant regulatory changes, new standard publications, or certification scope changes)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Data Protection Officer (DPO)
- Secondary: Chief Information Security Officer (CISO)
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**:

- PRIV-POL-01 — Privacy Governance and Decision-Making Framework
- ISMS-POL-00 — Regulatory Applicability Framework (ISMS base — mandatory co-reference)
- ISO/IEC 27701:2025 Clause 5.2 (Understanding the needs and expectations of interested parties)
- ISO/IEC 27701:2025 Clause 5.3 (Determining the scope of the PIMS)
- All PIMS policy documents (mandatory reference)

**Distribution**: All PIMS stakeholders, privacy officers, policy authors, system owners, auditors, processors
**Referenced By**: All PIMS policy documents (PRIV-POL-01, all 21 control group POLs)

**Language Strategy**: Where technical or regulatory terms are internationally established (e.g., GDPR, ISO/IEC, FADP, PII), English terminology is retained to preserve precision and facilitate cross-border regulatory reference.

---

## Executive Summary

This document provides the **authoritative reference** for interpreting privacy regulatory and framework applicability across the entire Privacy Information Management System (PIMS).

**Purpose**: Eliminate ambiguity and inconsistency in how privacy laws, regulations, and standards are referenced across PIMS policies, procedures, and controls.

**Scope**: All references to privacy laws, data protection regulations, and privacy frameworks within PIMS documentation.

**Relationship to ISMS**: This policy is a privacy-specific companion to **ISMS-POL-00** (Regulatory Applicability Framework). ISMS-POL-00 governs information security obligations. PRIV-POL-00 governs privacy and data protection obligations. Where obligations overlap (e.g., GDPR Article 32 — security of processing), ISMS-POL-00 takes precedence for the information security dimension; PRIV-POL-00 governs the data protection dimension.

**Key Principle**: **Privacy regulatory applicability must be explicit, not assumed.** References to privacy regulations and frameworks fall into three categories:

1. **Mandatory Compliance** — Legal obligations that apply to the organisation
2. **Conditional Applicability** — Requirements that apply only under specific circumstances
3. **Informational Reference** — Best practices and technical guidance

**Usage**: All PIMS policies SHALL include a "Regulatory Framework" section referencing this document, identifying which tier each cited regulation/standard belongs to.

**Key Terms**: Definitions for terms used throughout this policy (Mandatory, Conditional, Tier 1/2/3, Applicability Trigger, PII, PII Principal, Controller, Processor) are provided in the **Glossary** at the end of this document.

---

## Policy Authority and Boundaries

### Purpose and Scope of This Policy

This policy defines the **identification and applicability** of legal, statutory, regulatory, and contractual requirements for the organisation's Privacy Information Management System.

**This policy establishes:**

- Which privacy laws and standards apply to the organisation
- Categorisation of privacy obligations (Mandatory, Conditional, Informational)
- Assessment methodology for determining applicability
- Review and update processes for changes in the privacy regulatory landscape

**This policy does NOT establish:**

- Privacy risk treatment decisions (addressed in PIMS risk management)
- Control implementation requirements (addressed in control group POLs and IMPs)
- Compliance status or verification (addressed in compliance monitoring processes)
- Information security obligations (addressed in ISMS-POL-00)

The outcome of the privacy regulatory applicability assessment serves as **input** for:

- Control scoping decisions across all 21 PIMS control groups
- Privacy risk assessment and treatment prioritisation
- Proportionality decisions for control implementation (controller vs. processor obligations)
- Audit planning and compliance verification

**Boundary Principle**: This policy establishes privacy regulatory applicability. Implementation, enforcement, and verification are handled through separate PIMS processes and control group policies.

**Integration with ISO 27701:2025:**

- **Clause 5.2 (Interested Parties)**: Privacy regulatory requirements constitute the primary interested party obligations. This policy identifies them explicitly.
- **Clause 5.3 (Scope)**: Scope determination is informed by which Tier 1 regulations apply and whether the organisation acts as a controller, processor, or both.
- **Clause 6 (Risk Assessment)**: Regulatory obligations feed into the PIMS risk register. Tier 1 = High priority, Tier 2 conditional = Medium priority, Tier 3 = Informational input.

**Integration with ISMS-POL-00:**

This policy operates alongside and is subordinate to ISMS-POL-00 for all information security matters. Where a regulation has both privacy and security dimensions (e.g., GDPR Article 32, CH-nDSG Article 7), the obligations are addressed jointly. PRIV-POL-00 governs the privacy interpretation; ISMS-POL-00 governs the security interpretation.

---

**Regulatory Applicability Categories**

**Mandatory Compliance**
Legal or contractual privacy obligations that the organisation MUST comply with. Non-compliance results in legal liability, regulatory fines, supervisory authority investigations, or certification loss.

**Characteristics**:

- Enforceable by data protection authority (DPA) or court
- Non-compliance has legal/financial consequences (fines, enforcement orders)
- Requires documented evidence of compliance (records of processing, DPIAs, consent records)
- Subject to regulatory audits, inspections, and supervisory authority powers

**Conditional Applicability**
Privacy requirements that apply only when specific conditions are met (e.g., specific data types processed, geographic scope, certification sought, customer contracts, cloud service model).

**Characteristics**:

- Applicability depends on processing activities, data types, or geographic scope
- May become mandatory based on business activities or contractual requirements
- Requires periodic re-assessment as business and processing activities evolve

**Informational Reference / Best Practice Alignment**
Frameworks and standards used for technical and organisational guidance, benchmarking, or voluntary alignment. These inform privacy practices but do not constitute mandatory compliance requirements.

**Characteristics**:

- Voluntary adoption for best practices
- No direct legal enforcement mechanism
- Used for technical and organisational measure (TOM) implementation guidance
- May become mandatory if referenced in contracts or certification requirements

---

## Compliance Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│              PRIVACY COMPLIANCE HIERARCHY                       │
├─────────────────────────────────────────────────────────────────┤
│  TIER 1: MANDATORY (Legal/Contractual)                          │
│  • EU GDPR (where processing EU personal data)                  │
│  • Swiss Federal Data Protection Act (FADP/nDSG)               │
│  • ISO/IEC 27701:2025 (where certification sought)             │
│                                                                 │
│  TIER 2: CONDITIONAL (Context-Dependent)                        │
│  • ISO/IEC 27018:2025 (cloud PII processors)                   │
│  • UK GDPR (if processing UK personal data post-Brexit)         │
│  • LGPD (if processing Brazilian personal data)                 │
│  • PIPL (if processing Chinese personal data)                   │
│  • Other jurisdiction laws (trigger-based assessment)           │
│                                                                 │
│  TIER 3: INFORMATIONAL (Best Practice / Technical Guidance)     │
│  • ISO/IEC 27017:2019 (cloud security baseline for 27018)      │
│  • ISO/IEC 27002:2022 (security control implementation)        │
│  • NIST Privacy Framework 1.0 (privacy risk management)        │
│                                                                 │
│  FORTHCOMING (Monitor — Adopt on Publication)                   │
│  • ISO/IEC 27017:2025 (cloud security — not yet published)     │
└─────────────────────────────────────────────────────────────────┘
```

> *If box-drawing characters do not render correctly, refer to Sections below for tier definitions.*

---

# Mandatory Compliance (Tier 1)

## EU General Data Protection Regulation (GDPR)

**Applicability**: When processing personal data of EU/EEA residents, regardless of where the organisation is established.

**Key Requirements**:

- Article 5: Principles of processing (lawfulness, fairness, transparency, purpose limitation, data minimisation, accuracy, storage limitation, integrity and confidentiality, accountability)
- Article 6: Lawful basis for processing
- Article 7–9: Consent requirements and special category data
- Article 13–14: Information to be provided to PII principals (privacy notices)
- Article 15–22: Data subject rights (access, rectification, erasure, restriction, portability, objection, automated decision-making)
- Article 24: Controller responsibilities (accountability, policies, measures)
- Article 25: Data protection by design and by default
- Article 28: Processor obligations (written contract, security measures, sub-processor controls)
- Article 30: Records of processing activities (ROPA)
- Article 32: Security of processing (encryption, pseudonymisation, resilience, testing)
- Article 33–34: Breach notification (72 hours to DPA; without undue delay to affected individuals for high-risk breaches)
- Article 35–36: Data Protection Impact Assessment (DPIA) for high-risk processing; prior consultation with DPA where residual risk remains high
- Article 37–39: Data Protection Officer (DPO) obligations where applicable
- Article 44–49: Restrictions on international data transfers

**PIMS Impact**:

- Privacy by design and by default across all processing activities
- Records of processing activities (ROPA) maintained by controller and processor
- Lawful basis documented for each processing activity
- Data subject rights procedures implemented and tested
- Processor agreements compliant with Article 28 in place
- DPIA process for high-risk processing
- Breach notification procedure with 72-hour timeline
- International transfer safeguards (adequacy decisions, Standard Contractual Clauses, BCRs)

**Supervisory Authority**: Competent EU/EEA data protection authority (DPA) of the lead establishment or data subject's country.

**Reference**: Regulation (EU) 2016/679, effective 25 May 2018

---

## Swiss Federal Data Protection Act (FADP/nDSG)

**Applicability**: All processing of personal data by the organisation where subject to Swiss jurisdiction; and any processing of personal data of Swiss residents from outside Switzerland where effects occur in Switzerland.

**Key Requirements**:

- Article 6: Principles (lawfulness, good faith, proportionality, purpose limitation)
- Article 7: Data security (technical and organisational measures appropriate to risk)
- Article 8: Data processing by processors (written agreement, security, sub-processors)
- Article 9: Disclosure to foreign countries (adequacy or appropriate safeguards)
- Article 10: Representatives in Switzerland (if no establishment)
- Article 12: Register of processing activities (for controllers with >250 FTE or high-risk processing)
- Article 19–21: Duty to provide information (privacy notices to data subjects)
- Article 22: Data Protection Impact Assessment (DPIA) for high-risk processing
- Article 25: Data protection by design and by default
- Article 26: Data subject rights (access, rectification, erasure, restriction, portability, objection)
- Article 24: Breach notification to FDPIC where likely to result in high risk
- Article 328b CO: Employee monitoring and personality protection

**FADP / GDPR Alignment**: The revised FADP (in force 1 September 2023) is substantially aligned with GDPR in structure and principles. For organisations subject to both, a single GDPR-aligned programme generally satisfies FADP requirements. Key differences: FADP has no mandatory DPO requirement; Swiss adequacy list differs from EU; no administrative fine regime (criminal sanctions instead).

**PIMS Impact**:

- Processing register maintained (Art. 12)
- Processor agreements compliant with Art. 8 in place
- Privacy notices issued to data subjects (Art. 19–21)
- DPIA process for high-risk processing (Art. 22)
- Breach notification to FDPIC for high-risk breaches
- International transfer safeguards where data leaves Switzerland

**Supervisory Authority**: Federal Data Protection and Information Commissioner (FDPIC — Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter, EDÖB)

**Reference**: Federal Act on Data Protection (SR 235.1), effective 1 September 2023

---

## ISO/IEC 27701:2025 (Where Certification Sought)

**Applicability**: Where the organisation seeks ISO/IEC 27701:2025 certification, or where customers contractually require PIMS compliance with this standard.

**Key Requirements**:

- Clause 5: Context of the PIMS (understanding the organisation, interested parties, scope)
- Clause 6: Leadership (commitment, policy, roles, responsibilities)
- Clause 7: Planning (risks, objectives, privacy by design triggers)
- Clause 8: Support (resources, competence, awareness, communication, documented information)
- Clause 9: Operation (operational planning, risk treatment, DPIA process)
- Clause 10: Performance evaluation (monitoring, internal audit, management review)
- Clause 11: Improvement (nonconformity, corrective action, continual improvement)
- Annex A: Controller-specific controls (A.1.x — 31 controls)
- Annex A: Processor-specific controls (A.2.x — 18 controls)
- Annex A: Shared security controls (A.3.x — 29 controls)
- Annex B: Mapping of ISO/IEC 27001:2022 controls to PIMS (normative)

**PIMS Impact**:

- Full implementation of all 21 control groups in 51-isms-core-privacy/
- Role determination documented (controller, processor, or both per processing activity)
- PIMS integrated with or layered on top of ISO 27001 ISMS

**Note on Edition**: ISO/IEC 27701:2025 (Second Edition) is a standalone PIMS standard, not an extension clause set for ISO 27001. It can be implemented and certified independently. Where an organisation holds ISO 27001 certification, Annex B provides the normative mapping between 27001 controls and 27701 requirements.

**Reference**: ISO/IEC 27701:2025, Information security, cybersecurity and privacy protection — Privacy information management system

---

# Conditional Applicability (Tier 2)

These regulations and standards apply **only when specific conditions are met**.

## ISO/IEC 27018:2025 — Cloud PII Processors

**Standard**: ISO/IEC 27018:2025 (Third Edition) — Information technology — Security techniques — Code of practice for protection of personally identifiable information (PII) in public clouds acting as PII processors

**Applicability Triggers**:

- Organisation acts as a **PII processor operating public cloud services** (cloud service provider processing customer PII)
- Customer contracts **explicitly require** ISO/IEC 27018 compliance or certification
- Certification to ISO/IEC 27018:2025 is sought

**What ISO 27018:2025 Covers**:

ISO 27018:2025 comprises two distinct parts:

- **Body (Clauses 5–18)**: Implementation guidance for ISO/IEC 27002:2022 controls in public cloud environments. This guidance is informational in context and does not create additional mandatory requirements beyond ISO 27002.
- **Annex A (normative when certifying)**: 25 PII-specific controls not found in ISO 27002. These are the genuinely new cloud PII processor obligations (consent, transparency, purpose limitation, return/erasure, sub-processor disclosure, etc.).

**PIMS Delivery**: ISO 27018 Annex A controls (25 controls) are delivered as a crosswalk overlay on `priv-a.2.5.7-9-sub-processor-management` and adjacent processor packs. They are NOT standalone packs.

**Assessment**: If organisation provides public cloud services and processes customer PII → Assess ISO 27018:2025 Annex A for applicability.

**Reference**: ISO/IEC 27018:2025, Third Edition, 2025

---

## UK General Data Protection Regulation (UK GDPR)

**Regulation**: UK GDPR (retained EU law as amended by Data Protection, Privacy and Electronic Communications (Amendments etc) (EU Exit) Regulations 2019) + Data Protection Act 2018

**Applicability Triggers**:

- Organisation **processes personal data of UK residents** post-Brexit (1 January 2021)
- Organisation has an **establishment in the United Kingdom**
- Organisation **targets or monitors individuals** in the United Kingdom

**Key Differences from EU GDPR**:

- Supervisory authority: Information Commissioner's Office (ICO), not EU DPAs
- International transfers: UK adequacy regulations (not EU adequacy decisions); EU→UK transfer covered by EU adequacy decision for UK (current at time of writing — monitor for review)
- UK Standard Contractual Clauses (IDTA) or UK Addendum to EU SCCs required for transfers to third countries

**Assessment**: If organisation processes UK personal data → UK GDPR compliance required in parallel with EU GDPR. For most CH/EU organisations with UK operations or UK customers, this will be mandatory.

**Reference**: UK GDPR; Data Protection Act 2018 (UK)

---

## Lei Geral de Proteção de Dados (LGPD) — Brazil

**Regulation**: Lei n° 13.709/2018 — Lei Geral de Proteção de Dados Pessoais

**Applicability Triggers**:

- Organisation **processes personal data of individuals located in Brazil**
- Processing **occurs in Brazil** (regardless of establishment)
- Processing is **for the purpose of offering goods or services** in Brazil

**Key Requirements** (GDPR-aligned structure):

- Legal bases for processing (10 legal bases, including consent and legitimate interest)
- Data subject rights (access, correction, deletion, portability, opposition)
- Data Protection Officer (DPO/Encarregado) obligations
- Security incident notification to ANPD (Brazilian DPA) and data subjects
- International transfers: adequacy decision, contractual clauses, or consent

**Assessment**: If organisation serves Brazilian customers or processes Brazilian personal data → Assess LGPD applicability. Similar in structure to GDPR; existing GDPR-aligned programme covers most requirements.

**Supervisory Authority**: Autoridade Nacional de Proteção de Dados (ANPD)

**Reference**: Lei n° 13.709/2018, effective September 2020 (enforcement from August 2021)

---

## Personal Information Protection Law (PIPL) — China

**Regulation**: Personal Information Protection Law (个人信息保护法), effective 1 November 2021

**Applicability Triggers**:

- Organisation **processes personal information of individuals located in China**
- Organisation provides **products or services** targeting individuals in China
- Organisation **analyses behaviour** of individuals in China

**Key Requirements**:

- Consent as primary legal basis (narrower legitimate interest scope than GDPR)
- Data localisation: Personal information of Chinese individuals collected in China may require local storage
- Cross-border transfer: Security assessment by CAC required for transfers above volume thresholds; Standard Contract (SCC) for smaller volumes
- Data Protection Officer: Required if processing above thresholds
- Breach notification within 24 hours to regulator

**Assessment**: If organisation offers services to or collects personal data from individuals in China → PIPL applicability assessment required. Note: PIPL is stricter than GDPR in several respects (consent default, localisation, cross-border transfer controls).

**Supervisory Authority**: Cyberspace Administration of China (CAC — 国家互联网信息办公室)

**Reference**: PIPL 2021; CAC Provisions on Standard Contracts for Cross-border Transfer of Personal Information (2023)

---

## Additional Conditional Privacy Regulations

Organisations should assess and document additional conditional privacy regulations based on their specific processing activities and geographic scope:

| Regulation | Trigger | Supervisory Authority |
|-----------|---------|----------------------|
| **CCPA/CPRA** (California) | Serving California residents; revenue/data thresholds | California Privacy Protection Agency (CPPA) |
| **PIPEDA** (Canada) | Commercial processing of Canadian personal data | Office of the Privacy Commissioner of Canada (OPC) |
| **PDPA** (Singapore) | Processing personal data of Singapore individuals | Personal Data Protection Commission (PDPC) |
| **APPI** (Japan) | Processing personal information of Japan residents | Personal Information Protection Commission (PPC) |
| **POPIA** (South Africa) | Processing personal information of South Africa residents | Information Regulator |
| **Sector Regulations** | Healthcare (eHealth), financial data, children's data | Sector-specific authority |

**Assessment Approach**: For each new geographic market or processing activity, assess whether a privacy regulation applies using the triggers above. Document determination in the regulatory monitoring log (see Maintenance section).

---

# Informational Reference / Best Practice (Tier 3)

## ISO/IEC 27017:2019 — Cloud Security Controls

**Standard**: ISO/IEC 27017:2019 — Information technology — Security techniques — Code of practice for information security controls based on ISO/IEC 27002 for cloud services

**Role in PRIV-POL-00**: ISO 27017 is a **cloud security** standard (not a privacy standard). It is referenced here as a supporting technical baseline because ISO 27018:2025 (Annex A — cloud PII processor controls) builds directly on the security foundation established by ISO 27017. Organisations implementing ISO 27018 should treat ISO 27017 controls as the security bedrock for cloud PII processing environments.

**Primary Home**: ISO 27017 is referenced in **ISMS-POL-00** (Tier 3) as a cloud security best practice. Its presence in PRIV-POL-00 is as a privacy-supporting reference only.

**Key Guidance Areas** (relevant to cloud PII processing):

- Cloud customer and cloud service provider shared responsibility
- Virtual machine hardening and isolation
- Administrator operational security
- Monitoring of cloud services
- Network security in cloud environments

**Usage in PIMS**: Referenced in `priv-a.2.4.2-4-processor-lifecycle-controls` and `priv-a.2.5.7-9-sub-processor-management` (ISO 27018 overlay packs).

**Reference**: ISO/IEC 27017:2019, Information security controls for cloud services

---

## ISO/IEC 27017:2025 — Forthcoming (Monitor — Adopt on Publication)

**Status**: **Not yet published** as of the date of this policy.

ISO/IEC 27017:2025 is under development as the second edition of the cloud security controls standard. When published, this policy shall be updated to reference ISO/IEC 27017:2025 in place of (or alongside) ISO/IEC 27017:2019.

**Action on Publication**:

1. Review ISO/IEC 27017:2025 for structural changes vs. 2019 edition
2. Assess impact on `priv-a.2.4.2-4` and `priv-a.2.5.7-9` control packs
3. Update PRIV-POL-00 Tier 3 reference from 2019 to 2025 edition
4. Communicate changes to relevant control group owners
5. Update control pack IMPs where 27017 guidance is referenced

**Monitor**: ISO.org publications — SC 27 work programme — WG 4 (Security controls and services)

---

## ISO/IEC 27002:2022 — Security Control Implementation Guidance

**Standard**: ISO/IEC 27002:2022 — Information security, cybersecurity and privacy protection — Information security controls

**Role in PRIV-POL-00**: ISO 27002 provides implementation guidance for the A.3.x shared security controls (ISO 27701:2025 Annex A.3). The 29 A.3 shared controls are privacy-specific overlays on the information security control framework established by ISO 27002.

**Reference**: ISO/IEC 27002:2022

---

## NIST Privacy Framework 1.0

**Framework**: NIST Privacy Framework: A Tool for Improving Privacy Through Enterprise Risk Management, Version 1.0 (January 2020)

**Role in PRIV-POL-00**: Informational reference for privacy risk management methodology. Provides a function-based (Identify-P, Govern-P, Control-P, Communicate-P, Protect-P) vocabulary for privacy programme maturity assessment. May be used for gap analysis and privacy risk assessment benchmarking.

**Note**: NIST Privacy Framework 2.0 is anticipated. Monitor NIST publications and update reference when published.

**Reference**: NIST Privacy Framework v1.0, NIST, January 2020

---

# Determining Privacy Regulatory Applicability

## Assessment Process

When assessing whether a privacy regulation applies to the organisation, follow this decision process:

**Step 1: Identify Processing Activities**

Document each category of PII processing: what data, whose data (data subjects), in which territories, for what purpose, as controller or processor.

**Step 2: Apply Geographic Triggers**

For each regulation, evaluate the applicability trigger against the processing map:

| Trigger Type | Questions |
|-------------|-----------|
| **Establishment** | Is the organisation established in the jurisdiction? |
| **Data Subject Location** | Are individuals in the jurisdiction whose data is processed? |
| **Targeting / Monitoring** | Does the organisation target or monitor individuals in the jurisdiction? |
| **Service Delivery** | Is the organisation offering goods/services in the jurisdiction? |

**Step 3: Determine Controller vs. Processor Role**

Privacy obligations differ significantly based on role:

- **Controller**: Determines purposes and means of processing → Full Tier 1 obligations apply (GDPR Articles 5–39)
- **Processor**: Processes on behalf of a controller → Processor-specific obligations apply (GDPR Article 28; ISO 27701 Annex A.2)
- **Both**: Where the organisation acts as controller for some processing and processor for others → Obligations apply per processing activity

**Step 4: Classify and Document**

| Finding | Action |
|---------|--------|
| Regulation applies — no conditions | Classify Tier 1 (Mandatory) |
| Regulation applies only if condition met | Classify Tier 2 (Conditional) — document trigger |
| Standard provides guidance — not legally enforceable | Classify Tier 3 (Informational) |
| Regulation explicitly not applicable | Document as Not Applicable with rationale |

**Step 5: Update Records**

Update the Privacy Regulatory Register (maintained in PIMS documentation repository) with determination, rationale, and review date.

---

## Privacy Regulatory Applicability Matrix Template

Use this template to document applicability for each regulation:

| Regulation | Tier | Applies? | Trigger | Assessment Date | Reviewer | Next Review |
|-----------|------|----------|---------|-----------------|---------|-------------|
| EU GDPR | 1 | Yes/No | EU data subject processing | [Date] | DPO | Annually |
| CH FADP | 1 | Yes/No | Swiss operations | [Date] | DPO | Annually |
| ISO 27701:2025 | 1/2 | Yes/No | Certification sought | [Date] | CISO | Annually |
| ISO 27018:2025 | 2 | Yes/No | Cloud PII processor | [Date] | CISO | Annually |
| UK GDPR | 2 | Yes/No | UK data subjects | [Date] | DPO/Legal | Annually |
| LGPD | 2 | Yes/No | Brazilian data subjects | [Date] | Legal | Annually |
| PIPL | 2 | Yes/No | Chinese data subjects | [Date] | Legal | Annually |

---

## When to Re-Assess

| Trigger Event | Action Required |
|--------------|----------------|
| New geographic market entered | Full applicability assessment for that jurisdiction |
| New processing activity (new product, service, data type) | Controller/processor role + applicable regulations |
| Change from on-premise to cloud processing | ISO 27018:2025 assessment |
| Customer contract with explicit privacy requirements | Contract-specific tier update |
| New regulation published or enacted | Assess applicability, update register |
| Existing regulation substantially amended | Re-assess affected tier classification |
| ISO 27017:2025 published | Update Tier 3 reference; assess control pack impacts |
| Business change (acquisition, new entity, outsourcing) | Full applicability re-assessment for affected activities |

---

# Usage in PIMS Policies

## Standard Reference Language

All PIMS control group policies (PRIV-POL-01 through all 21 control group POLs) SHALL include a **Regulatory Framework** section using this standard reference:

```
## Regulatory Framework

This policy operates within the privacy regulatory framework established in PRIV-POL-00.
The following obligations are relevant to this control group:

**Mandatory (Tier 1):**
- EU GDPR: [specific articles relevant to this control group]
- CH FADP: [specific articles]
- ISO/IEC 27701:2025: [specific clauses/controls]

**Conditional (Tier 2):**
- ISO/IEC 27018:2025: [Annex A controls, if processor packs]

**Informational (Tier 3):**
- ISO/IEC 27017:2019: [if cloud-related controls]
```

## Role Labelling in Control Packs

Control group policies SHALL clearly state the organisational role addressed:

- `privacy-controller/` packs → **"This policy applies to the organisation acting as a PII Controller."**
- `privacy-processor/` packs → **"This policy applies to the organisation acting as a PII Processor."**
- `privacy-shared/` packs → **"This policy applies to the organisation acting as both PII Controller and PII Processor."**

---

# Regulatory Framework (This Policy)

## Mandatory Compliance

| Regulation | Version | Status | PIMS Control Relevance |
|-----------|---------|--------|------------------------|
| EU GDPR | 2016/679 | Active — Mandatory | All 21 control groups |
| CH FADP/nDSG | SR 235.1 (2023) | Active — Mandatory | All 21 control groups |
| ISO/IEC 27701:2025 | Ed. 2, 2025 | Mandatory (certification scope) | All 21 control groups |

## Conditional Applicability

| Regulation | Version | Status | Trigger |
|-----------|---------|--------|---------|
| ISO/IEC 27018:2025 | Ed. 3, 2025 | Conditional | Cloud PII processor services |
| UK GDPR | 2018/2021 | Conditional | UK data subjects |
| LGPD | 2018 | Conditional | Brazilian data subjects |
| PIPL | 2021 | Conditional | Chinese data subjects |

## Informational Reference

| Standard | Version | Status | Usage |
|---------|---------|--------|-------|
| ISO/IEC 27017:2019 | 2019 | Active — Tier 3 | Cloud security baseline (supports 27018 implementation) |
| ISO/IEC 27017:2025 | Not yet published | Forthcoming | Adopt on publication |
| ISO/IEC 27002:2022 | 2022 | Active — Tier 3 | Security control guidance for A.3 shared controls |
| NIST Privacy Framework | 1.0, 2020 | Active — Tier 3 | Privacy risk management methodology |

## Audit References

| Requirement | Evidence | Location |
|------------|---------|---------|
| Regulatory applicability documented | This policy + Privacy Regulatory Register | PIMS document repository |
| DPA registrations current | Registration certificates | Legal/Compliance file |
| ROPA maintained | Records of Processing Activities | [GRC Platform / ISMS system] |
| DPIA process documented | DPIA template + completed DPIAs | [GRC Platform] |
| Processor agreements in place | Signed DPAs per GDPR Art. 28 | Contracts repository |

---

# Current Regulatory Status

## Tier 1: Mandatory Compliance (Active)

| Regulation | Applicability Basis | Confirmed | Next Review |
|-----------|---------------------|-----------|-------------|
| EU GDPR | Processing EU personal data | [Date] | [Date + 12M] |
| CH FADP | Swiss-based operations | [Date] | [Date + 12M] |
| ISO 27701:2025 | Certification programme | [Date] | [Date + 12M] |

## Tier 2: Conditional Applicability

| Regulation | Current Status | Trigger Status | Action |
|-----------|---------------|---------------|--------|
| ISO 27018:2025 | [Applicable / Not Applicable] | [Cloud PII processor services in scope?] | [Implement Annex A overlay if applicable] |
| UK GDPR | [Applicable / Not Applicable] | [UK data subjects in scope?] | [Document if applicable] |
| LGPD | [Applicable / Not Applicable] | [Brazilian data subjects in scope?] | [Assess if applicable] |
| PIPL | [Applicable / Not Applicable] | [Chinese data subjects in scope?] | [Assess if applicable] |

## Tier 3: Informational Reference (Active Use)

| Standard | Usage | Referenced In |
|---------|-------|--------------|
| ISO/IEC 27017:2019 | Cloud security baseline | priv-a.2.4 and priv-a.2.5 processor packs |
| ISO/IEC 27002:2022 | Security control guidance | All A.3 shared control packs |
| NIST Privacy Framework | Risk methodology reference | PIMS risk assessment documentation |

---

# Maintenance & Updates

## Review Schedule

| Review Type | Frequency | Lead | Deliverable |
|------------|-----------|------|-------------|
| Annual comprehensive review | Annual (Q4) | DPO + CISO + Legal | Updated policy + Executive briefing |
| Quarterly monitoring | Quarterly | DPO + Legal | Regulatory monitoring log update |
| Triggered assessment | On trigger event | DPO (lead) | Triggered assessment report |
| ISO 27017:2025 watch | On publication | CISO | Control pack impact assessment |

## Regulatory Monitoring Sources

| Source | Monitoring Frequency | Responsible |
|--------|---------------------|-------------|
| EU Official Journal (eur-lex.europa.eu) | Monthly | Legal |
| EDPB Guidelines and Opinions (edpb.europa.eu) | Monthly | DPO |
| FDPIC publications (edoeb.admin.ch) | Quarterly | DPO |
| ISO.org — SC 27 publications | Quarterly | CISO |
| ICO (UK) guidance | Quarterly (if UK in scope) | Legal |
| National DPA guidance (member states) | Quarterly | DPO |

## Communication

Changes to this policy SHALL be communicated to:

- All PIMS control group policy owners
- Privacy champions / data owners
- Processors under contract with the organisation
- Internal audit

---

# Related Documents

| Document | Type | Relationship |
|---------|------|-------------|
| ISMS-POL-00 | ISMS Policy | Parent — information security regulatory framework |
| PRIV-POL-01 | PIMS Policy | Sibling — privacy governance and decision-making |
| priv-a.1.2.6-9 POL | Control Group Policy | Privacy Governance and Records (controller) |
| priv-a.3.13-16 POL | Control Group Policy | Privacy Compliance and Audit (shared) |
| ISO/IEC 27701:2025 | Standard | Primary governance standard |
| ISO/IEC 27018:2025 | Standard | Cloud PII processor supplementary standard |

---

# Glossary

| Term | Definition |
|------|------------|
| **PII** | Personally Identifiable Information — any information that can be used to identify a natural person directly or indirectly (equivalent to "personal data" under GDPR/FADP) |
| **PII Principal** | The natural person to whom PII relates (equivalent to "data subject") |
| **Controller** | The entity that determines the purposes and means of processing PII (GDPR: "data controller") |
| **Processor** | The entity that processes PII on behalf of a controller (GDPR: "data processor") |
| **Processing** | Any operation performed on PII: collection, recording, storage, adaptation, retrieval, use, disclosure, erasure |
| **PIMS** | Privacy Information Management System — the management system framework established under ISO/IEC 27701:2025 |
| **DPA** | Data Protection Authority — the supervisory authority responsible for enforcing privacy law in a jurisdiction |
| **DPIA** | Data Protection Impact Assessment — structured assessment of high-risk processing activities |
| **ROPA** | Records of Processing Activities — documentation required by GDPR Article 30 and FADP Article 12 |
| **Mandatory** | Legal obligation, enforceable by DPA or court, non-compliance has consequences |
| **Conditional** | Applies only if specific triggers are met (jurisdiction, data type, role, certification) |
| **Informational** | Reference for best practices, not legally enforceable, voluntary adoption |
| **Tier 1** | Mandatory compliance (legal, contractual) |
| **Tier 2** | Conditional compliance (context-dependent) |
| **Tier 3** | Informational reference (best practice, voluntary) |
| **Applicability Trigger** | Event or condition that causes a Tier 2 regulation to become applicable |
| **Regulatory Monitoring** | Systematic quarterly review of regulatory changes and organisational activities to detect applicability changes |

---

# Closing Statement

This policy establishes privacy regulatory applicability for the organisation's Privacy Information Management System.

**What this policy establishes:**

- Identification of applicable privacy regulations (mandatory, conditional, informational)
- Assessment methodology for determining privacy regulatory applicability
- Review and update processes for changes in the privacy regulatory landscape

**What this policy does NOT establish:**

- Privacy risk treatment decisions (addressed in PIMS risk management and control group IMPs)
- Control implementation requirements (addressed in 21 control group POLs and IMPs)
- Compliance status or verification (addressed in compliance monitoring processes)
- Information security obligations (addressed in ISMS-POL-00)

**Separation of Concerns:**

- **This Policy (PRIV-POL-00)**: Defines WHICH privacy regulations apply
- **PRIV-POL-01**: Defines HOW the PIMS is governed and decisions are made
- **Control Group POLs (21 packs)**: Define WHAT the organisation must do per control domain
- **Control Group IMPs**: Define HOW to implement the control requirements
- **Compliance Monitoring**: Verifies and tracks COMPLIANCE status

---

**END OF PRIV-POL-00**

*"Privacy regulatory applicability is the foundation. Implementation and compliance are the structure built upon it."*

<!-- QA_VERIFIED: [Date] -->
