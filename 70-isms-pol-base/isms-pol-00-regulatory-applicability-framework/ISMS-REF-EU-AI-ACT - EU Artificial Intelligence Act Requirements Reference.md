# ISMS-REF-EU-AI-ACT — EU Artificial Intelligence Act Requirements Reference
## EU AI System Risk Management and Compliance Requirements (Non-ISMS Technical Reference)

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | EU AI Act Requirements Reference |
| **Document Type** | Internal - Technical Reference (Not ISMS) |
| **Document ID** | ISMS-REF-EU-AI-ACT |
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
| 1.0 | [Date] | CISO / AI Governance Team | Initial technical reference for EU AI Act (Regulation 2024/1689) |

**Review Cycle**: Semi-annual (AI Act implementation evolving rapidly)  
**Next Review Date**: [Date + 6 months]  
**Approvers**: CISO / Legal/Compliance / Data Protection Officer (technical reference, no ISMS approval required)

**Distribution**: AI/ML development teams, Product management, Legal, CISO, DPO (for organizations developing or deploying AI systems)

---

⚠️ **IMPORTANT – NON-ISMS TECHNICAL SUPPORT DOCUMENT**

This document is provided for informational and awareness purposes only.

- This document is NOT part of the Information Security Management System (ISMS).
- This document does NOT define mandatory requirements unless [Organization] develops or deploys AI systems affecting EU persons.
- This document does NOT establish binding requirements, deadlines, KPIs, or SLAs for non-AI organizations.
- This document does NOT mandate the adoption of EU AI Act requirements for organizations not subject to the regulation.
- This document does NOT override or extend any ISMS policy.

**Applicability Determination**:
EU AI Act requirements apply ONLY IF [Organization]:
- Is a provider (develops or places AI systems on EU market)
- Is a deployer (uses AI systems under own authority in the EU)
- Is an importer or distributor of AI systems in the EU
- Develops/deploys AI systems whose outputs affect persons located in the EU (extraterritorial application)

For all other organizations, this document serves solely as:
- Technical reference for potential AI Act requirements
- Context for business expansion into AI development/deployment
- Awareness of EU AI regulatory landscape
- **This document must not be used as audit evidence unless [Organization] is subject to AI Act**

Use of this document does not imply AI Act applicability, compliance obligations, or AI system development/deployment status.

**Critical Positioning Statement**:
This document intentionally provides regulatory detail beyond what applies to most organizations. Its purpose is awareness only for organizations that MAY become subject to the EU AI Act as they develop or deploy AI systems, or that provide services to AI system providers/deployers. No auditor conclusions shall be drawn from the presence, absence, or implementation status of any AI Act requirement listed herein unless [Organization] explicitly develops or deploys AI systems affecting EU persons.

---

## 1. Document Purpose and Scope

### 1.1 Purpose

This document provides a technical overview of the EU Artificial Intelligence Act (Regulation (EU) 2024/1689) requirements. It is intended to support:

- Awareness of EU AI Act requirements for AI system providers and deployers
- Understanding of risk-based classification (Unacceptable, High-Risk, Limited Risk, Minimal Risk)
- Context for organizations considering AI development or deployment
- Potential future applicability assessment
- Mapping AI Act requirements to ISO 27001:2022 controls

### 1.2 What This Document Is NOT

This document does NOT:
- Establish mandatory requirements for non-AI organizations
- Define [Organization]'s compliance obligations (see POL-00 for regulatory applicability)
- Create audit criteria unless [Organization] develops/deploys AI systems
- Replace legal or compliance counsel interpretation
- Constitute legal advice on EU AI Act compliance
- Cover all delegated acts and implementing acts (many still in development)
- Establish AI development or deployment procedures

### 1.3 Relationship to ISMS

This document is a **non-binding technical reference** UNLESS [Organization] develops or deploys AI systems affecting EU persons (as determined in ISMS-POL-00 Section 3.X - EU AI Act).

**If [Organization] DOES develop/deploy AI systems affecting EU:**
- AI Act requirements become Tier 1 (Mandatory Compliance) per POL-00
- This document provides implementation guidance
- ISMS controls must support AI Act compliance (risk management, data governance, logging, human oversight)
- Conformity assessment required for high-risk AI systems

**If [Organization] DOES NOT develop/deploy AI systems:**
- AI Act remains Tier 3 (Informational Reference) per POL-00
- This document is for awareness only
- No AI Act compliance obligations exist
- ISMS controls follow ISO 27001:2022 only

### 1.4 Content Organization

This reference organizes AI Act requirements by:
- Risk-based classification system (Unacceptable, High-Risk, Limited Risk, Minimal Risk)
- Provider obligations (developers, manufacturers)
- Deployer obligations (users of AI systems)
- Phased implementation timeline (2025-2027)
- General-purpose AI models (GPAI) requirements
- Mapping to ISO 27001:2022 and related standards
- Governance and organizational requirements

---

## 2. EU AI Act Overview and Applicability

### 2.1 What is the EU AI Act?

**Regulation (EU) 2024/1689** laying down harmonised rules on artificial intelligence (Artificial Intelligence Act).

**Key Dates**:
- **Adoption**: May 21, 2024 (European Parliament)
- **Entry into Force**: August 1, 2024 (20 days after publication in Official Journal)
- **Phased Implementation**: 2025-2027 (see Section 2.6)

**Purpose**:
- Establish harmonized rules for AI development and deployment in EU
- Risk-based regulatory approach (proportionate to AI system risks)
- Protect fundamental rights, health, safety, and democracy
- Foster trustworthy AI innovation
- Enhance EU's competitive position in AI

**Legal Basis**: EU Regulation (directly applicable in all member states, no national transposition required)

**Extraterritorial Application**: Applies to providers/deployers outside EU if AI systems affect persons in EU.

### 2.2 Key Definitions

**AI System** (Article 3(1)):
A machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments.

**Provider** (Article 3(3)):
A natural or legal person, public authority, agency or other body that develops an AI system or a general-purpose AI model or that has an AI system or a general-purpose AI model developed and places it on the market or puts it into service under its own name or trademark, whether for payment or free of charge.

**Deployer** (Article 3(4)):
A natural or legal person, public authority, agency or other body using an AI system under its authority except where the AI system is used in the course of a personal non-professional activity.

**General-Purpose AI Model (GPAI)** (Article 3(44)):
An AI model, including when trained with a large amount of data using self-supervision at scale, that displays significant generality and is capable of competently performing a wide range of distinct tasks regardless of the way the model is placed on the market and that can be integrated into a variety of downstream systems or applications, except AI models that are used for research, development or prototyping activities before being placed on the market.

### 2.3 Scope of Application (Article 2)

**The AI Act applies to**:

| Actor | Geographic Scope | Conditions |
|-------|------------------|------------|
| **Providers** | Placing AI systems on EU market OR putting into service in EU | Regardless of provider location |
| **Providers** | Located in third country | If AI system outputs used in EU |
| **Deployers** | Located in EU | Using AI systems |
| **Deployers** | Located in third country | If AI system outputs used in EU |
| **Importers and distributors** | In EU | Distributing AI systems |
| **Product manufacturers** | In EU | Placing AI-containing products on market |
| **Authorized representatives** | Of providers not in EU | Acting on behalf of non-EU providers |

**Exclusions** (Article 2(3)):
- AI systems developed or used exclusively for military, defense, or national security purposes
- AI systems developed or used exclusively for research, development, or prototyping activities before market placement
- Personal non-professional use

### 2.4 Risk-Based Classification

The AI Act employs a **four-tier risk pyramid**:

```
                   ┌──────────────────┐
                   │  UNACCEPTABLE    │
                   │    PROHIBITED    │
                   └──────────────────┘
                        (Article 5)
                            
              ┌────────────────────────────┐
              │       HIGH-RISK            │
              │  (Strict Requirements)     │
              └────────────────────────────┘
                   (Annex III + Article 6)
                            
        ┌────────────────────────────────────────┐
        │         LIMITED RISK                   │
        │   (Transparency Obligations)           │
        └────────────────────────────────────────┘
                     (Article 50)
                            
   ┌──────────────────────────────────────────────────┐
   │              MINIMAL RISK                        │
   │    (No Obligations - Voluntary Codes)            │
   └──────────────────────────────────────────────────┘
                     (Most AI systems)
```

### 2.5 Determining AI System Risk Classification

**Step 1**: Is the AI system prohibited? (Article 5 - Unacceptable Risk)

**Step 2**: Is the AI system in a high-risk category?
- Listed in Annex III? OR
- Safety component of product covered by EU harmonization legislation (Annex I)?

**Step 3**: Does the AI system have transparency requirements? (Article 50 - Limited Risk)

**Step 4**: If none of the above, it's Minimal Risk (no specific requirements)

### 2.6 Phased Implementation Timeline

| Requirement Category | Effective Date | Status |
|---------------------|----------------|--------|
| **Prohibited AI Practices** (Article 5) | February 2, 2025 | 6 months after entry into force |
| **General-Purpose AI Models** (Chapter V) | August 2, 2025 | 12 months after entry into force |
| **High-Risk AI Systems** (Chapter III, Section 2) | August 2, 2026 | 24 months after entry into force |
| **High-Risk AI in Regulated Products** | August 2, 2027 | 36 months after entry into force |
| **AI Office, Governance Structure** | Immediate | August 2024 |

**Grace Period for Existing Systems**:
AI systems already placed on market or put into service before August 2, 2026 may continue to be used until August 2, 2030 without compliance (unless substantial modifications made).

---

## 3. Unacceptable Risk AI Practices (Article 5) - PROHIBITED

### 3.1 Overview

Certain AI practices are **prohibited** due to unacceptable risks to fundamental rights, safety, or democracy.

**Effective Date**: February 2, 2025

**Penalty for Violation**: Up to €35 million or 7% of worldwide annual turnover (whichever higher)

### 3.2 Prohibited Practices

**Article 5(1)(a): Subliminal Manipulation**
- AI systems that deploy subliminal techniques beyond person's consciousness
- Purpose: Materially distorting behavior in manner that causes or likely to cause significant harm
- Examples: Hidden messaging, subliminal advertising targeting vulnerable populations

**Article 5(1)(b): Exploitation of Vulnerabilities**
- AI systems exploiting vulnerabilities of specific groups (age, disability, social/economic situation)
- Purpose: Materially distorting behavior causing significant harm
- Examples: Predatory targeting of children, elderly, or economically disadvantaged

**Article 5(1)(c): Social Scoring**
- AI systems evaluating or classifying natural persons based on social behavior or personal/personality characteristics
- Outcomes: Detrimental or unfavorable treatment in contexts unrelated to original data collection OR unjustified/disproportionate to social behavior
- Examples: Government social credit systems, employer broad-based social scoring

**Article 5(1)(d): Assessing Risk of Offending**
- AI systems assessing or predicting risk that natural person will commit criminal offense
- Based solely on profiling or personality traits
- Exception: Based on objective verifiable facts directly linked to criminal activity
- Examples: Predictive policing based solely on demographics

**Article 5(1)(e): Scraping for Facial Recognition Databases**
- Untargeted scraping of facial images from internet or CCTV
- Purpose: Creating or expanding facial recognition databases
- Examples: Mass scraping of social media photos

**Article 5(1)(f): Emotion Recognition in Workplace/Education**
- AI systems inferring emotions in workplace or educational institutions
- Exception: Medical or safety reasons
- Examples: Employee productivity monitoring via emotion detection (prohibited unless safety/medical)

**Article 5(1)(g): Biometric Categorisation**
- AI systems for biometric categorisation inferring sensitive attributes
- Sensitive attributes: Race, political opinions, trade union membership, religious/philosophical beliefs, sex life, sexual orientation
- Exception: Labelling/filtering lawfully acquired biometric datasets (law enforcement databases)

**Article 5(1)(h): Real-Time Remote Biometric Identification (RBI) in Public Spaces**
- Use of real-time RBI systems in publicly accessible spaces for law enforcement
- Exceptions (Article 5(2)): Strictly necessary and proportionate uses:
  - Targeted search for specific missing persons, abduction victims
  - Prevention of specific, substantial, imminent threat (terrorist attack)
  - Localization/identification of person suspected of serious criminal offense (defined in Annex II - serious crimes)
- Requires prior judicial or independent administrative authorization (except emergency)

**ISO 27001:2022 Mapping**:
- Article 5 prohibitions relate to organizational policies and ethical AI use
- No direct ISO 27001 control, but informed by:
  - A.5.1: Policies for information security (ethical use policies)
  - A.5.31: Legal, statutory, regulatory and contractual requirements
  - Clause 4.1: Understanding the organization and its context (societal expectations)

### 3.3 Compliance Requirements

**For All Organizations**:
1. **Inventory AI Systems**: Identify all AI systems in development or deployment
2. **Article 5 Assessment**: Assess whether any AI systems fall under prohibited practices
3. **Immediate Cessation**: Stop development/deployment of prohibited AI systems by February 2, 2025
4. **Documentation**: Document assessment and decisions
5. **Training**: Ensure development/procurement teams aware of Article 5 prohibitions

---

## 4. High-Risk AI Systems (Chapter III, Section 2)

### 4.1 Overview

High-risk AI systems face **strict requirements** due to potential significant risks to health, safety, or fundamental rights.

**Effective Date**: August 2, 2026 (24 months after entry into force)

**Penalty for Non-Compliance**: Up to €15 million or 3% of worldwide annual turnover (whichever higher)

### 4.2 High-Risk AI System Categories

**Annex III High-Risk Use Cases**:

| Category | Use Cases | Examples |
|----------|-----------|----------|
| **1. Biometric identification and categorisation** | Remote biometric identification, biometric categorisation (sensitive attributes exception), emotion recognition | Facial recognition access control, biometric categorisation systems |
| **2. Critical infrastructure** | Management and operation of critical digital infrastructure, road traffic, water, gas, heating, electricity supply | AI-controlled traffic management, power grid optimization |
| **3. Education and vocational training** | Determining access/admission, assessing students, detecting exam cheating | Automated university admissions, exam proctoring AI |
| **4. Employment** | Recruitment, screening, evaluation/promotion decisions, task allocation, monitoring/evaluation of work performance, termination | AI resume screening, performance evaluation systems |
| **5. Essential private/public services** | Credit scoring, assessing eligibility for public assistance, emergency response prioritization | Credit decision algorithms, benefit eligibility AI |
| **6. Law enforcement** | Individual risk assessment (victims, perpetrators, reoffending), polygraphs, emotion recognition, detecting deep fakes, evaluation of evidence reliability | Recidivism prediction, AI-assisted interrogation |
| **7. Migration, asylum, border control** | Examination of applications, detection of fraudulent documents, assessing security/health risks, polygraph/lie detection | Automated visa screening, document verification AI |
| **8. Administration of justice/democratic processes** | Assisting judicial authorities in legal research/interpretation, AI-influencing election outcomes | Legal research AI, electoral prediction systems |

**Article 6(1)**: AI systems that are safety components of products covered by EU harmonization legislation (Annex I) if those products undergo third-party conformity assessment.

**Examples from Annex I**:
- Medical devices (Regulation 2017/745, 2017/746)
- Machinery (Regulation 2023/1230)
- Toys (Directive 2009/48/EC)
- Radio equipment (Directive 2014/53/EU)
- Civil aviation (Regulations 2018/1139, 2019/945, 2018/1139)

### 4.3 Provider Obligations for High-Risk AI Systems

**Article 9: Risk Management System**

Requirements:
- Establish, implement, document, and maintain risk management system
- Continuous iterative process throughout AI system lifecycle
- Regular systematic updates

**Risk Management Process**:
1. **Identification and analysis** of known and reasonably foreseeable risks
2. **Estimation and evaluation** of risks arising during intended use and reasonably foreseeable misuse
3. **Evaluation of other risks** based on post-market monitoring data
4. **Adoption of suitable risk management measures** (Article 9(4))

**Risk Management Measures** (Article 9(4)):
- Elimination or reduction of risks (safeguards by design)
- Adequate mitigation and control measures (safeguards by deployment)
- Information to deployers (instructions for use, warnings)
- Appropriate training for deployers

**ISO 27001:2022 Mapping**:
- Clause 6.1.2: Information security risk assessment
- Clause 6.1.3: Information security risk treatment
- A.5.7: Threat intelligence
- ISO/IEC 23894:2023: Information technology — Artificial intelligence — Risk management (specific AI risk standard)

---

**Article 10: Data and Data Governance**

Requirements:
- Training, validation, testing datasets meet **quality criteria**
- Subject to **data governance** and management practices

**Data Quality Criteria** (Article 10(3)):
- **Relevant, sufficiently representative, and free from errors**
- **Complete** for intended purpose
- **Appropriate statistical properties** (e.g., balance, coverage)
- Consider characteristics/elements of specific geographical, contextual, functional setting
- Document design choices, data collection arrangements, data preparation operations

**Data Governance Practices** (Article 10(2)):
- Relevant design choices
- Data collection processes
- Data preparation processing operations (annotation, labeling, cleaning, enrichment, aggregation)
- Assumptions, especially regarding information completeness
- Assessment of data bias and appropriate mitigation measures
- Identification of data gaps or shortcomings affecting intended use

**Special Data Categories** (Article 10(5)):
Where AI system processes sensitive personal data categories (Article 9 GDPR: racial/ethnic origin, political opinions, religious beliefs, biometric data, health data, sex life/orientation):
- Appropriate measures for detecting, preventing, reducing bias
- Training on fundamental rights and non-discrimination

**ISO 27001:2022 Mapping**:
- A.5.12: Classification of information
- A.5.13: Labelling of information
- A.5.14: Information transfer (dataset sharing)
- A.8.11: Data masking
- GDPR Article 5(1)(d): Data accuracy principle

---

**Article 11: Technical Documentation**

Requirements:
- Draw up technical documentation **before placing on market**
- Keep technical documentation **up to date**
- Make available to national competent authorities upon request

**Technical Documentation Contents** (Annex IV):
1. General description of AI system (intended purpose, developer, versions, market placement dates)
2. Detailed description of system elements and development process
3. Detailed information about monitoring, functioning, control
4. Description of risk management system (Article 9)
5. Description of changes made through lifecycle
6. Compliance demonstration with high-risk requirements
7. Detailed description of conformity assessment procedure
8. Copy of EU declaration of conformity
9. Detailed description of post-market monitoring system

**ISO 27001:2022 Mapping**:
- A.5.37: Documented operating procedures
- Clause 7.5: Documented information (ISMS documentation requirements)

---

**Article 12: Record-Keeping (Logging)**

Requirements:
- Automatically generated logs throughout AI system's lifetime
- Enable **traceability** of system functioning
- Appropriate to intended purpose and risk level

**Logging Requirements** (Article 12(2)):
- **Duration of logging**: Appropriate for system's risk
- **Timestamp**: Date and time of each event
- **Input data**: Database/file causing action
- **Natural persons involved**: Identification where technically feasible

**Purpose**: Enable monitoring, investigation, post-market monitoring, and accountability.

**ISO 27001:2022 Mapping**:
- A.8.15: Logging
- A.8.16: Monitoring activities
- ISO/IEC 27018:2019: Protection of PII in public cloud (logging requirements)

---

**Article 13: Transparency and Information to Deployers**

Requirements:
- Design AI system for **transparency** enabling deployers to:
  - Interpret system output
  - Use system appropriately
  
**Instructions for Use** (Annex IV, Section 2):
- Identity and contact details of provider
- Characteristics, capabilities, limitations of performance
- Changes to AI system and performance
- Human oversight measures
- Computational and hardware resources needed
- Expected lifetime and maintenance needs

**ISO 27001:2022 Mapping**:
- A.5.37: Documented operating procedures (user documentation)

---

**Article 14: Human Oversight**

Requirements:
- Design AI system to enable **effective oversight by natural persons**
- Prevent or minimize risks to health, safety, fundamental rights

**Human Oversight Measures** (Article 14(4)):
- **Understand** AI system capabilities and limitations
- Remain **aware** of automation bias tendency
- Correctly **interpret** system output
- **Decide not to use** or override output
- **Intervene or interrupt** system operation (stop button)

**Oversight Assignees** (Article 14(5)):
- Natural persons to whom oversight assigned must have:
  - Necessary competence, training, authority
  - Adequate understanding of high-risk AI system

**ISO 27001:2022 Mapping**:
- A.5.37: Documented operating procedures (human oversight procedures)
- A.6.3: Information security awareness, education and training (oversight training)

---

**Article 15: Accuracy, Robustness, Cybersecurity**

Requirements:
- **Accuracy**: Appropriate level of accuracy throughout lifecycle
- **Robustness**: Technical and cybersecurity measures appropriate to risks
- **Resilience**: Against attempts to alter use/performance by third parties

**Robustness Measures**:
- Technical solutions against adversarial attacks
- Model poisoning attacks
- Data poisoning attacks
- Privacy attacks (model inversion, membership inference)
- Confidentiality attacks

**ISO 27001:2022 Mapping**:
- A.8.7: Protection against malware
- A.8.8: Management of technical vulnerabilities
- A.8.16: Monitoring activities (anomaly detection)
- A.8.24: Use of cryptography (model protection)
- ISO/IEC 24029-1: Artificial intelligence — Assessment of robustness of neural networks

---

**Article 16: Quality Management System**

Requirements:
- Put in place quality management system ensuring:
  - Compliance with AI Act
  - Implementation of Articles 9-15
  - Post-market monitoring (Article 72)

**Quality Management Contents**:
- Strategy for regulatory compliance (policies, procedures)
- Techniques, procedures, systematic actions (design, design control, verification, validation, testing)
- Examination, test, validation procedures before, during, after development
- Technical specifications (quality standards, coding guidelines)
- Systems and procedures for data management
- Risk management system
- Post-market monitoring system
- Reporting of serious incidents and malfunctions
- Communication with authorities, deployers
- Systems and procedures for record-keeping
- Resource management (skills, training plans)
- Accountability framework (roles and responsibilities)

**ISO 27001:2022 Mapping**:
- Entire Clause 4-10 ISMS framework
- ISO 9001:2015 Quality Management System (complementary standard)

---

**Article 43-51: Conformity Assessment**

**Before placing high-risk AI system on market**, provider must undergo conformity assessment.

**Conformity Assessment Options**:

**Option 1: Internal Control** (Article 43 + Annex VI):
- Provider's own assessment (self-assessment)
- Applicable to most Annex III high-risk systems

**Option 2: Notified Body Assessment** (Article 43 + Annex VII):
- Third-party assessment by notified body
- Required for:
  - Biometric identification/categorisation (Annex III(1))
  - Certain critical infrastructure (if not self-certified)

**Conformity Assessment Process** (Annex VI):
1. Technical documentation prepared (Article 11, Annex IV)
2. Implement quality management system (Article 16)
3. Implement risk management system (Article 9)
4. Self-assessment or third-party assessment
5. Draw up EU declaration of conformity (Annex V)
6. Affix CE marking (Article 48)

**CE Marking** (Article 48):
- High-risk AI systems bear CE marking
- Indicates conformity with AI Act
- Affixed visibly, legibly, indelibly

**ISO 27001:2022 Mapping**:
- Clause 9.2: Internal audit (similar to self-assessment)
- Clause 9.3: Management review

---

**Article 72: Post-Market Monitoring**

Requirements:
- Establish and document post-market monitoring system
- Collect, document, analyze data on performance throughout lifetime

**Post-Market Monitoring Plan**:
- Strategy for collecting data on performance in real-world use
- Methods for analyzing serious incidents, malfunctions, inaccuracies
- Mechanisms for reporting to authorities
- Feedback loop to risk management system

**ISO 27001:2022 Mapping**:
- Clause 9.1: Monitoring, measurement, analysis and evaluation
- A.8.16: Monitoring activities

---

### 4.4 Deployer Obligations for High-Risk AI Systems

**Article 26: Deployer Obligations**

Deployers (users) of high-risk AI systems must:

1. **Use in accordance with instructions** (Article 26(1))
2. **Assign human oversight** to competent natural persons (Article 26(2))
3. **Monitor operation** based on instructions for use (Article 26(3))
4. **Suspend use** if serious incident or malfunction suspected (Article 26(4))
5. **Keep logs** automatically generated by system (Article 26(5))
6. **Use input data** relevant and representative for intended purpose (Article 26(6))
7. **Conduct fundamental rights impact assessment** (FRIA) before putting into service (Article 27) - for deployers in specific sectors or uses

**Fundamental Rights Impact Assessment (FRIA)** - Article 27:
Required for deployers who are:
- Public authorities OR
- EU institutions/bodies/agencies OR
- Deploying high-risk AI in certain sensitive areas (defined in Article 27(1))

**FRIA Contents**:
- Description of deployer's processes where AI will be used
- Description of period and frequency of use
- Categories of natural persons and groups likely to be affected
- Specific risks of harm likely to impact affected persons
- Description of human oversight measures
- Measures in case of materialization of risks

**ISO 27001:2022 Mapping**:
- A.5.37: Documented operating procedures (deployer procedures)
- Clause 6.1.2: Information security risk assessment (FRIA similar to risk assessment)
- GDPR Article 35: Data Protection Impact Assessment (similar to FRIA)

---

## 5. Limited Risk AI Systems (Article 50) - Transparency Obligations

### 5.1 Overview

Certain AI systems pose **limited risks** but require transparency to enable informed decisions.

**Effective Date**: August 2, 2026 (same as high-risk systems)

**Penalty for Non-Compliance**: Up to €7.5 million or 1.5% of worldwide annual turnover (whichever higher)

### 5.2 Transparency Requirements

**Article 50(1): AI Systems Interacting with Natural Persons**

When AI system intended to interact directly with natural persons:
- **Inform natural persons** they are interacting with AI system
- **Exceptions**: 
  - Obvious from circumstances and context
  - Authorized by law for law enforcement (detecting, preventing, investigating crimes)

**Examples**:
- Chatbots (must inform user they're interacting with AI)
- Virtual assistants
- Automated phone systems

---

**Article 50(2): Emotion Recognition and Biometric Categorisation Systems**

When using emotion recognition or biometric categorisation systems:
- **Inform natural persons** exposed to system
- **Exception**: Authorized by law for law enforcement

**Examples**:
- Retail emotion recognition (must inform customers)
- Interview emotion analysis tools
- Airport biometric categorisation

---

**Article 50(3): AI-Generated Content (Deep Fakes)**

When generating or manipulating image/audio/video content (deep fakes):
- **Disclose** content artificially generated or manipulated

**Disclosure Requirements**:
- Machine-readable format (technical standards being developed)
- Human-readable disclosure for average person

**Exceptions**:
- Content necessary for exercise of right to freedom of expression and arts/literary/artistic/satirical freedom
- Authorized by law for law enforcement
- Necessary for detecting/exposing crimes

**Specific Types**:

**Article 50(4): AI-Generated Text (ChatGPT-like systems)**
- Disclose outputs are artificially generated or manipulated
- Applies to systems producing text for public information purposes
- **Exception**: Text undergone human review/editorial control with editorial responsibility

---

**ISO 27001:2022 Mapping**:
- A.5.1: Policies for information security (transparency policies)
- A.5.9: Inventory of information and other associated assets (AI system inventory)

---

## 6. Minimal Risk AI Systems - Voluntary Measures

### 6.1 Overview

Most AI systems pose **minimal or no risk** and face **no mandatory requirements** under the AI Act.

**Examples**:
- Spam filters
- AI-enabled video games
- Inventory management systems
- Recommendation engines (e-commerce)
- Internal business analytics
- AI development tools

### 6.2 Voluntary Codes of Conduct (Article 95)

Providers of minimal risk AI systems are **encouraged** to voluntarily apply:
- Requirements for high-risk AI systems (Articles 9-15)
- Transparency requirements (Article 50)
- Codes of conduct developed by industry

**Benefits of Voluntary Compliance**:
- Demonstrate trustworthiness
- Competitive advantage
- Preparation for potential future regulation
- Alignment with ethical AI principles

---

## 7. General-Purpose AI Models (GPAI) - Chapter V

### 7.1 Overview

**General-Purpose AI Models** (GPAI) are foundation models capable of wide range of tasks.

**Examples**:
- Large Language Models (GPT-4, Claude, Gemini, LLaMA)
- Multimodal models (GPT-4V, Gemini)
- Foundation models for image generation (DALL-E, Stable Diffusion, Midjourney)

**Effective Date**: August 2, 2025 (12 months after entry into force)

### 7.2 GPAI Provider Obligations

**Article 53: Obligations for All GPAI Providers**

All GPAI providers must:

1. **Technical Documentation** (Article 53(1)(a) + Annex XI):
   - General description of model (capabilities, limitations)
   - Description of data used for training (sources, curation)
   - Information on compute resources (training time, hardware)
   - Description of evaluation process and results

2. **Information for Downstream Providers** (Article 53(1)(b)):
   - Documentation to enable downstream providers (integrating GPAI into their AI systems) to comply with AI Act
   - Instructions for use

3. **Copyright Policy** (Article 53(1)(c)):
   - Publicly available policy to identify and comply with Directive (EU) 2019/790 (Copyright Directive)
   - Summary of copyrighted content used for training (if available)

4. **Transparency** (Article 53(1)(d)):
   - Publicly available summary of content used for training
   - EU AI Office template (to be developed)

**Article 54: Systemic Risk GPAI Models - Additional Obligations**

For GPAI models with **systemic risk** (see Section 7.3):

5. **Model Evaluation** (Article 54(1)(a)):
   - Adversarial testing (red teaming)
   - Assessing and mitigating systemic risks

6. **Serious Incidents Tracking** (Article 54(1)(b)):
   - Track, document, report serious incidents to AI Office

7. **Cybersecurity** (Article 54(1)(c)):
   - Ensure adequate level of cybersecurity protection
   - Protect model weights and other parameters from unauthorized access

8. **Energy Efficiency** (Article 54(1)(d)):
   - Report on energy consumption during training
   - Optimize energy efficiency where feasible

### 7.3 Systemic Risk GPAI Models

**Definition** (Article 51):
GPAI model with systemic risk if:
- High-impact capabilities (evaluated by state-of-the-art) OR
- Significant impact on EU market (assessed via model reach) OR
- Cumulative amount of compute used ≥ 10^25 FLOPs (floating point operations)

**10^25 FLOPs threshold** (Article 51(1)(a)):
- Presumed systemic risk if training compute ≥ 10^25 FLOPs
- Example: GPT-4 estimated ~2-5 × 10^25 FLOPs (would qualify)

**Designation**:
- EU AI Office can designate models as systemic risk
- Providers can request Commission decision if compute < 10^25 FLOPs

**Penalty for Non-Compliance**: Up to €15 million or 3% of worldwide annual turnover (whichever higher)

### 7.4 ISO 27001:2022 Mapping for GPAI

| AI Act Requirement | ISO 27001:2022 Control | Notes |
|--------------------|------------------------|-------|
| Technical documentation (Article 53) | A.5.37, Clause 7.5 | Documentation practices |
| Copyright policy (Article 53(1)(c)) | A.5.31 Legal requirements | Copyright compliance |
| Model evaluation (Article 54(1)(a)) | A.8.8 Vulnerability management | Adversarial testing similar to pentesting |
| Serious incidents tracking (Article 54(1)(b)) | A.5.24-5.28 Incident management | Incident tracking and reporting |
| Cybersecurity (Article 54(1)(c)) | A.8.24 Cryptography, A.8.3 Access restriction | Model weight protection |

---

## 8. Organizational Requirements and Governance

### 8.1 AI Literacy (Article 4)

**Requirement**: Providers and deployers ensure **staff operating AI systems** have sufficient level of AI literacy.

**AI Literacy Definition**: Skills and knowledge to:
- Understand AI system capabilities and limitations
- Interpret system output correctly
- Make informed decisions on appropriate use

**Implementation**:
- Training programs for AI system users
- Role-specific training (developers, deployers, oversight personnel)
- Awareness of bias, ethics, fundamental rights

**ISO 27001:2022 Mapping**:
- A.6.3: Information security awareness, education and training

---

### 8.2 Roles and Responsibilities

**Recommended Governance Structure**:

| Role | Responsibilities |
|------|------------------|
| **AI Governance Board** | Strategic AI oversight, policy approval, risk appetite |
| **Chief AI Officer (CAIO)** or equivalent | AI program leadership, compliance coordination |
| **CISO** | Cybersecurity aspects of AI systems (Article 15) |
| **DPO** | GDPR compliance for AI processing personal data |
| **Legal/Compliance** | AI Act compliance, risk assessments, external reporting |
| **Product Owners** | Responsible for specific AI systems (risk management, documentation) |
| **AI Development Teams** | Implementation of technical requirements (Articles 9-15) |
| **Human Oversight Personnel** | Assigned per Article 14 for high-risk systems |

**ISO 27001:2022 Mapping**:
- Clause 5.3: Organizational roles, responsibilities and authorities
- A.5.2: Information security roles and responsibilities

---

### 8.3 AI System Inventory

**Requirement**: Maintain inventory of all AI systems developed or deployed.

**Inventory Contents**:
- AI system name and version
- Provider (internal development or external)
- Intended purpose and use cases
- Risk classification (Unacceptable, High-Risk, Limited Risk, Minimal Risk)
- Deployment status (development, testing, production, retired)
- Regulatory obligations (conformity assessment status)
- Deployer responsibilities assigned

**ISO 27001:2022 Mapping**:
- A.5.9: Inventory of information and other associated assets

---

## 9. ISO 27001:2022 to EU AI Act Mapping

### 9.1 Control Mapping Matrix

| AI Act Requirement | AI Act Article | ISO 27001:2022 Control | Gap Analysis |
|--------------------|----------------|------------------------|--------------|
| Prohibited practices assessment | Art. 5 | A.5.1, A.5.31 | AI Act-specific prohibitions |
| Risk management system | Art. 9 | Clause 6.1.2-6.1.3 | AI Act: More detailed AI-specific risk process |
| Data governance | Art. 10 | A.5.12-5.14 | **AI Act-specific**: Data quality, bias mitigation |
| Technical documentation | Art. 11 | A.5.37, Clause 7.5 | AI Act: Extensive AI system documentation |
| Logging (record-keeping) | Art. 12 | A.8.15-8.16 | Aligned |
| Transparency to deployers | Art. 13 | A.5.37 | AI Act: Detailed instructions for use |
| Human oversight | Art. 14 | A.5.37 | **AI Act-specific**: Human-in-the-loop requirements |
| Accuracy, robustness, cybersecurity | Art. 15 | A.8.7-8.8, A.8.16 | AI Act: AI-specific adversarial attack protection |
| Quality management system | Art. 16 | Clause 4-10 (entire ISMS) | Complementary: ISO 9001 + ISO 27001 |
| Conformity assessment | Art. 43-51 | Clause 9.2-9.3 | **AI Act-specific**: CE marking, notified bodies |
| Post-market monitoring | Art. 72 | Clause 9.1, A.8.16 | AI Act: Continuous real-world performance monitoring |
| Deployer obligations | Art. 26 | A.5.37 | AI Act: Deployer-specific responsibilities |
| Transparency (limited risk) | Art. 50 | A.5.1 | **AI Act-specific**: User disclosure requirements |
| AI literacy | Art. 4 | A.6.3 | AI Act: AI-specific training |

### 9.2 Key Gaps Between ISO 27001:2022 and EU AI Act

**Gap 1: AI-Specific Risk Assessment**
- ISO 27001: General information security risk assessment
- AI Act: Detailed AI system risk management (bias, discrimination, safety, fundamental rights)

**Gap 2: Data Governance for AI**
- ISO 27001: Data classification, protection
- AI Act: Training/validation/test data quality, representativeness, bias mitigation

**Gap 3: Human Oversight Requirements**
- ISO 27001: No specific human oversight requirements
- AI Act: Mandatory human oversight for high-risk AI (Article 14)

**Gap 4: Conformity Assessment and CE Marking**
- ISO 27001: Certification by accredited body
- AI Act: Conformity assessment (self-assessment or notified body), CE marking

**Gap 5: Transparency and Explainability**
- ISO 27001: No explainability requirements
- AI Act: Transparency to deployers (Article 13), transparency to end users (Article 50)

**Gap 6: Fundamental Rights Impact**
- ISO 27001: No fundamental rights assessment
- AI Act: Fundamental Rights Impact Assessment (FRIA) for certain deployers (Article 27)

**Gap 7: Post-Market Monitoring Specific to AI**
- ISO 27001: General monitoring and measurement
- AI Act: AI system performance monitoring in real-world use, incident reporting

### 9.3 AI Act Compliance with ISO 27001 Foundation

**Key Insight**:
ISO 27001:2022 provides strong foundational controls for AI Act compliance, particularly for cybersecurity aspects (Article 15). However, AI Act introduces **AI-specific requirements** not covered by ISO 27001:

**Additional Standards to Consider**:
- **ISO/IEC 42001:2023**: AI Management System (AIMS) - specifically designed for AI governance
- **ISO/IEC 23894:2023**: AI Risk Management
- **ISO/IEC 24029-1:2021**: Assessment of robustness of neural networks
- **ISO/IEC TR 24028:2020**: Overview of trustworthiness in AI
- **ISO/IEC 38507:2022**: Governance of IT - Governance implications of AI

Organizations with ISO 27001 typically require **40-60% additional effort** to achieve EU AI Act compliance for high-risk systems, primarily in:
- AI-specific risk management
- Data governance for training/validation data
- Human oversight procedures
- Conformity assessment and CE marking
- Fundamental rights considerations

---

## 10. Implementation Considerations

### 10.1 AI Act Compliance Roadmap

**If [Organization] develops or deploys AI systems affecting EU**:

**Phase 1: Inventory and Classification (Months 1-3)**
- Identify all AI systems (current and planned)
- Classify each AI system (Unacceptable, High-Risk, Limited Risk, Minimal Risk)
- Assess Article 5 prohibitions (immediate action if violations)
- Determine provider vs. deployer role for each system
- Identify GPAI models (if applicable)

**Phase 2: Gap Assessment (Months 3-6)**
- Assess current AI governance and documentation
- Identify gaps against AI Act requirements
- Prioritize remediation (prohibited practices first, then high-risk)
- Estimate budget and resources
- Engage legal counsel for complex classification decisions

**Phase 3: Governance and Policies (Months 6-9)**
- Establish AI governance structure (roles, responsibilities)
- Develop AI risk management framework (Article 9)
- Create data governance policies (Article 10)
- Establish human oversight procedures (Article 14)
- AI literacy training programs (Article 4)

**Phase 4: High-Risk System Compliance (Months 9-18)**
- Implement technical requirements (Articles 11-15)
- Prepare technical documentation (Annex IV)
- Implement quality management system (Article 16)
- Conduct conformity assessment preparation
- Establish post-market monitoring

**Phase 5: Conformity Assessment (Months 18-24)**
- Finalize technical documentation
- Conduct internal assessment or engage notified body
- Address any non-conformities identified
- Prepare EU declaration of conformity
- Affix CE marking (if high-risk system)

**Phase 6: Deployment and Monitoring (Month 24+)**
- Deploy high-risk AI systems with conformity
- Implement post-market monitoring (Article 72)
- Continuous compliance monitoring
- Annual review and updates
- Incident reporting procedures

**Timeline Notes**:
- Prohibited practices: Immediate action required (February 2, 2025)
- GPAI: August 2, 2025
- High-risk systems: August 2, 2026
- Existing systems grace period: Until August 2, 2030 (unless substantial modification)

### 10.2 Resource Requirements

**Personnel**:
- Chief AI Officer or equivalent
- AI governance team (cross-functional)
- Data scientists/ML engineers (AI development)
- Legal counsel with AI Act expertise
- Data governance specialists
- Human oversight personnel (for each high-risk system)
- Compliance/audit team

**External Resources**:
- Legal counsel (AI Act interpretation)
- Notified bodies (if required for conformity assessment)
- AI ethics consultants
- External auditors (quality management system)

**Technology**:
- AI system documentation platform
- Model governance tools (MLOps, model registry)
- Data governance platforms (data quality, lineage)
- Logging and monitoring infrastructure
- Adversarial testing tools (for GPAI with systemic risk)

### 10.3 Cost Implications

AI Act compliance costs vary significantly by:
- Number and risk level of AI systems
- Provider vs. deployer role
- Internal AI development vs. third-party AI

**Estimated Compliance Costs**:

**High-Risk AI System (Provider)**:
- Technical documentation and quality management: €50,000 - €200,000
- Conformity assessment (notified body if required): €10,000 - €50,000
- Annual post-market monitoring: €20,000 - €100,000
- Legal and consulting: €30,000 - €100,000
- **Total initial cost**: €110,000 - €450,000 per high-risk system
- **Annual ongoing**: €50,000 - €150,000 per system

**High-Risk AI System (Deployer)**:
- Fundamental Rights Impact Assessment: €10,000 - €30,000
- Human oversight implementation: €20,000 - €50,000
- Training and procedures: €10,000 - €30,000
- **Total initial cost**: €40,000 - €110,000 per system
- **Annual ongoing**: €20,000 - €50,000

**GPAI Model with Systemic Risk**:
- Technical documentation: €100,000 - €300,000
- Adversarial testing (red teaming): €50,000 - €200,000
- Cybersecurity measures (model protection): €50,000 - €150,000
- Energy efficiency reporting: €10,000 - €30,000
- **Total initial cost**: €210,000 - €680,000
- **Annual ongoing**: €100,000 - €300,000

**Non-Compliance Penalties**:
- Prohibited practices: Up to €35M or 7% turnover
- High-risk violations: Up to €15M or 3% turnover
- Limited risk violations: Up to €7.5M or 1.5% turnover
- Supplying incorrect information: Up to €7.5M or 1.5% turnover

---

## 11. Common Pitfalls and Lessons Learned

### 11.1 Common AI Act Compliance Challenges

**Challenge 1: AI System Identification**
- Organizations underestimate number of AI systems in use
- "AI" definition broad - includes rule-based systems, statistical models
- AI embedded in third-party software often overlooked

**Challenge 2: Risk Classification Uncertainty**
- Boundary between high-risk and limited risk not always clear
- Use case matters more than technology (same model, different use = different risk)
- Annex III categories subject to interpretation

**Challenge 3: Provider vs. Deployer Role Confusion**
- Same organization can be both provider and deployer
- Customization of third-party AI may make organization a provider
- "Substantial modification" triggers provider obligations

**Challenge 4: Data Governance for AI**
- Training data quality and bias mitigation require significant effort
- Legacy AI systems may lack data lineage documentation
- Data representativeness difficult to assess and validate

**Challenge 5: Human Oversight Implementation**
- Identifying appropriate oversight personnel with competence
- Balancing oversight with operational efficiency
- "Stop button" not always technically feasible in real-time systems

**Challenge 6: Conformity Assessment Preparation**
- Technical documentation is extensive (Annex IV)
- Quality management system requires organizational maturity
- Notified body capacity may be limited initially

**Challenge 7: GPAI Model Obligations**
- Copyright compliance for training data difficult to verify
- Transparency summaries require standardized formats (still being developed)
- Systemic risk threshold (10^25 FLOPs) may capture many foundation models

### 11.2 Best Practices

**Practice 1**: Conduct comprehensive AI system inventory early (don't wait for deadlines)
**Practice 2**: Engage legal counsel for risk classification (documented decisions)
**Practice 3**: Implement AI governance structure before technical requirements
**Practice 4**: Leverage ISO 27001 + ISO 42001 (AI Management System) together
**Practice 5**: Document everything (AI Act emphasizes documentation heavily)
**Practice 6**: Establish human oversight from AI system design phase (not retrofit)
**Practice 7**: For GPAI providers, engage with EU AI Office early (guidance evolving)
**Practice 8**: Consider voluntary compliance for minimal risk AI (future-proofing)
**Practice 9**: Integrate AI Act compliance into SDLC and procurement processes
**Practice 10**: Monitor AI Act delegated acts and implementing acts (many still being developed)

---

## 12. References and Resources

### 12.1 EU AI Act Official Resources

**Primary Regulation**:
- Regulation (EU) 2024/1689 (AI Act) - Official Journal of the EU

**EU AI Office**:
- Website: https://digital-strategy.ec.europa.eu/en/policies/ai-office
- Guidance documents (being developed)
- Templates for technical documentation and transparency summaries

**European Commission**:
- AI Act dedicated pages: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

### 12.2 Related Standards and Frameworks

**ISO AI Standards**:
- **ISO/IEC 42001:2023**: AI Management System (AIMS) - recommended for AI Act compliance
- **ISO/IEC 23894:2023**: AI Risk Management
- **ISO/IEC 24029-1:2021**: Assessment of robustness of neural networks
- **ISO/IEC TR 24028:2020**: Overview of trustworthiness in AI
- **ISO/IEC 38507:2022**: Governance of IT - Governance implications of AI
- **ISO/IEC 23053:2022**: Framework for AI systems using machine learning

**Information Security Standards**:
- ISO/IEC 27001:2022: Information Security Management
- ISO/IEC 27002:2022: Information Security Controls
- ISO/IEC 27701:2019: Privacy Information Management

**NIST AI Standards** (informational reference):
- NIST AI Risk Management Framework (AI RMF)
- NIST SP 1270: Towards a Standard for Identifying and Managing Bias in AI

### 12.3 Industry Guidance and Resources

**European AI Alliance**:
- Stakeholder forum for AI policy
- Website: https://futurium.ec.europa.eu/en/european-ai-alliance

**AI Standards Hub**:
- CEN-CENELEC AI standardization activities
- Website: https://www.cencenelec.eu/areas-of-work/cen-cenelec-topics/artificial-intelligence/

**Legal and Consulting Resources**:
- Engage legal counsel with EU AI Act expertise
- AI ethics consultants for fundamental rights assessments
- Notified bodies (list to be published by Commission)

---

## Appendix A: EU AI Act Compliance Self-Assessment Checklist

### AI System Inventory

| Question | Status | Notes |
|----------|--------|-------|
| Have we identified all AI systems in use or development? | ⬜ Yes ⬜ No ⬜ In Progress | [List systems] |
| Have we classified each AI system's risk level? | ⬜ Yes ⬜ No ⬜ Partial | [Classification documentation] |
| Have we determined provider vs. deployer role for each system? | ⬜ Yes ⬜ No ⬜ Partial | [Role documentation] |
| Do we develop or use any GPAI models? | ⬜ Yes ⬜ No ⬜ Uncertain | [GPAI list if applicable] |

### Prohibited Practices (Article 5)

| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| Assessed all AI systems against Article 5 prohibitions | ⬜ Yes ⬜ No | | |
| Confirmed no subliminal manipulation AI | ⬜ Yes ⬜ No ⬜ N/A | | |
| Confirmed no social scoring AI | ⬜ Yes ⬜ No ⬜ N/A | | |
| Confirmed no real-time RBI (unless law enforcement exception) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Confirmed no emotion recognition in workplace/education (unless safety/medical) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Documented Article 5 assessment | ⬜ Yes ⬜ No | | |

### High-Risk AI Systems - Provider Obligations

| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| Risk management system established (Article 9) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Data governance and quality measures (Article 10) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Technical documentation prepared (Article 11, Annex IV) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Automatic logging implemented (Article 12) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Instructions for use provided (Article 13) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Human oversight measures designed (Article 14) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Accuracy, robustness, cybersecurity addressed (Article 15) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Quality management system implemented (Article 16) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Conformity assessment conducted | ⬜ Yes ⬜ No ⬜ Planned | | |
| CE marking affixed (if applicable) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Post-market monitoring system established (Article 72) | ⬜ Yes ⬜ No ⬜ N/A | | |

### High-Risk AI Systems - Deployer Obligations

| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| Use in accordance with instructions (Article 26(1)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Human oversight assigned (Article 26(2)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Monitoring operation per instructions (Article 26(3)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Suspend use procedures if serious incident (Article 26(4)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Logs retained (Article 26(5)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Input data relevant and representative (Article 26(6)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| FRIA conducted (Article 27, if applicable) | ⬜ Yes ⬜ No ⬜ N/A | | |

### Limited Risk AI Systems

| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| Chatbot/virtual assistant discloses AI interaction (Article 50(1)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Emotion recognition/biometric categorisation informs users (Article 50(2)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Deep fake content disclosed (Article 50(3)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| AI-generated text disclosed (Article 50(4)) | ⬜ Yes ⬜ No ⬜ N/A | | |

### General-Purpose AI Models

| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| Technical documentation prepared (Article 53, Annex XI) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Information for downstream providers (Article 53(1)(b)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Copyright policy documented (Article 53(1)(c)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Training content summary published (Article 53(1)(d)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| Assessed if systemic risk (≥10^25 FLOPs or other criteria) | ⬜ Yes ⬜ No ⬜ N/A | | |
| **If Systemic Risk**: Model evaluation / red teaming (Article 54(1)(a)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| **If Systemic Risk**: Serious incidents tracking (Article 54(1)(b)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| **If Systemic Risk**: Cybersecurity / model protection (Article 54(1)(c)) | ⬜ Yes ⬜ No ⬜ N/A | | |
| **If Systemic Risk**: Energy efficiency reporting (Article 54(1)(d)) | ⬜ Yes ⬜ No ⬜ N/A | | |

### Organizational Requirements

| Requirement | Status | Evidence | Notes |
|-------------|--------|----------|-------|
| AI governance structure established | ⬜ Yes ⬜ No ⬜ In Progress | | |
| AI literacy training for staff (Article 4) | ⬜ Yes ⬜ No ⬜ Planned | | |
| AI system inventory maintained | ⬜ Yes ⬜ No ⬜ In Progress | | |
| Roles and responsibilities assigned | ⬜ Yes ⬜ No ⬜ Partial | | |

---

## Appendix B: High-Risk AI System Classification Flowchart

```
┌─────────────────────────────────────────┐
│   Is this system an AI system?          │
│   (Article 3(1) definition)             │
└──────────────┬──────────────────────────┘
               │ YES
               ↓
┌─────────────────────────────────────────┐
│   Is it prohibited under Article 5?     │
│   (Social scoring, subliminal manip.,   │
│    RBI in public, etc.)                 │
└──────────────┬──────────────────────────┘
               │ NO (If YES → STOP, prohibited)
               ↓
┌─────────────────────────────────────────┐
│   Is it listed in Annex III?            │
│   (Biometric ID, critical infra,        │
│    employment, education, law enf.,     │
│    credit scoring, etc.)                │
└──────────────┬──────────────────────────┘
         YES   │   NO
               ↓
┌─────────────────────────────────────────┐
│   OR: Is it a safety component of       │
│   product under Annex I legislation?    │
└──────────────┬──────────────────────────┘
         YES   │   NO
               ↓
┌─────────────────────────────────────────┐
│   HIGH-RISK AI SYSTEM                   │
│                                          │
│   Requirements:                          │
│   - Risk management (Art. 9)            │
│   - Data governance (Art. 10)           │
│   - Technical documentation (Art. 11)   │
│   - Logging (Art. 12)                   │
│   - Transparency (Art. 13)              │
│   - Human oversight (Art. 14)           │
│   - Accuracy/robustness (Art. 15)       │
│   - QMS (Art. 16)                       │
│   - Conformity assessment (Art. 43-51)  │
│   - Post-market monitoring (Art. 72)    │
└──────────────┬──────────────────────────┘
               │
          (End - High-Risk)
               
        (NO from Annex III/I check)
               ↓
┌─────────────────────────────────────────┐
│   Does it require transparency?         │
│   - Chatbot/interaction with humans?    │
│   - Emotion recognition/biometric cat.? │
│   - Generates deep fakes/synthetic      │
│     content?                            │
│   - Generates text for public info?     │
└──────────────┬──────────────────────────┘
         YES   │   NO
               ↓
┌─────────────────────────────────────────┐
│   LIMITED RISK AI SYSTEM                │
│                                          │
│   Requirements:                          │
│   - Transparency obligations (Art. 50)  │
│   - Disclose AI interaction/content     │
└──────────────┬──────────────────────────┘
               │
          (End - Limited Risk)
               
        (NO from transparency check)
               ↓
┌─────────────────────────────────────────┐
│   MINIMAL RISK AI SYSTEM                │
│                                          │
│   Requirements:                          │
│   - None mandatory                       │
│   - Voluntary codes of conduct (Art. 95)│
└─────────────────────────────────────────┘
```

---

**END OF TECHNICAL REFERENCE**

---

*This technical reference supports potential EU AI Act compliance requirements as determined in ISMS-POL-00. All regulatory applicability determinations and binding requirements are defined in ISMS-POL-00 and approved ISMS policy documents.*

*For organizations NOT developing or deploying AI systems affecting EU persons, this document is for informational awareness only and does NOT create compliance obligations.*