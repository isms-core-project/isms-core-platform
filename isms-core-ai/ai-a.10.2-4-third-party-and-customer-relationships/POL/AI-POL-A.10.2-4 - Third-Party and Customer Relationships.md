<!-- ISMS-CORE:POLICY:AI-POL-A.10.2-4:ai:POL:a.10.2-4 -->
**AI-POL-A.10.2-4 — Third-Party and Customer Relationships**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Third-Party and Customer Relationships |
| **Document Type** | Policy |
| **Document ID** | AI-POL-A.10.2-4 |
| **Document Creator** | AI Governance Officer / Legal / Procurement Officer |
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
| 1.0 | [Date to be set] | AI Governance Officer / Legal | Initial policy for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual (or upon significant change to the AI third-party or customer landscape)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: AI Governance Officer
- Secondary: Legal / Procurement Officer
- Compliance: Chief Information Security Officer (CISO)
- Final Authority: Executive Management

**Related Documents**:

- AI-POL-00 (AIMS Regulatory Applicability Framework)
- AI-POL-01 (AIMS Governance and Decision-Making Framework)
- AI-POL-A.4.2-6 (AI System Resources — tooling and data resources from third parties)
- AI-POL-A.8.2-5 (Information for Interested Parties — customer and partner information)
- AI-POL-A.9.2-4 (Responsible Use of AI Systems — where third parties use AI on [Organisation]'s behalf)
- AI-IMP-A.10.2-4-UG (Third-Party and Customer Relationships — User Guide)
- AI-IMP-A.10.2-4-TG (Third-Party and Customer Relationships — Technical Guide)
- ISMS supplier management controls (where AI third parties are also ISMS suppliers)
- PRIV-POL-00 (Privacy Regulatory Applicability — where AI third parties process personal data)
- ISO/IEC 42001:2023 Controls A.10.2, A.10.3, A.10.4
- ISO/IEC 42001:2023 Annex B.10 (Implementation guidance — Third-party and customer relationships)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for managing AI-related obligations in relationships with third parties and customers — covering the allocation of AI-related responsibilities between parties (A.10.2), the management of AI suppliers and other third parties that provide AI components or services (A.10.3), and the communication and management of AI system information with customers (A.10.4) — in accordance with ISO/IEC 42001:2023 Controls A.10.2 through A.10.4.

**Scope**: All third-party relationships involving AI systems within the AIMS scope — including AI component suppliers, AI platform providers, AI service providers, AI co-developers, and customers receiving AI-enabled products or services.

**Purpose**: Define WHAT AI-related obligations must be managed in third-party and customer relationships, WHO is responsible for managing them, and WHAT minimum contractual provisions are required. Implementation detail in AI-IMP-A.10.2-4-UG and AI-IMP-A.10.2-4-TG.

**Combined Control Rationale**: A.10.2 addresses the cross-cutting question of responsibility allocation — when multiple parties are involved in an AI system, which party is accountable for which obligations? A.10.3 addresses the supply chain for AI — managing the AI components and services [Organisation] procures. A.10.4 addresses what [Organisation] owes to its customers when delivering AI-enabled products or services. These three controls form the contractual and relational governance framework for AI.

---

## Scope and Applicability

### ISO/IEC 42001:2023 Control Statements

**Control A.10.2 — Allocating responsibilities between parties**
The organisation shall determine and document which responsibilities related to the use or provision of AI systems are to be allocated between the parties involved.

**Control A.10.3 — Suppliers providing AI-related products or services**
The organisation shall implement appropriate measures to ensure that suppliers who provide AI-related products or services meet the organisation's requirements for responsible AI.

**Control A.10.4 — Customers**
The organisation shall communicate appropriate information about the AI system to customers as part of AI product or service delivery.

### What This Policy Covers

- Responsibility allocation framework for multi-party AI arrangements (A.10.2)
- Supplier management requirements for AI-related products and services (A.10.3)
- Customer information and obligation requirements for AI-enabled products and services (A.10.4)

### What This Policy Does NOT Cover

- Detailed information to be provided to customers (addressed in AI-POL-A.8.2-5)
- General ISMS supplier management (addressed in ISMS control A.5.19–A.5.23)
- AI incident communication (addressed in AI-POL-A.8.2-5 — A.8.4)

### Regulatory Framework

**Tier 1: Mandatory Compliance** (per AI-POL-00):

- **EU AI Act (Regulation 2024/1689)**: Article 25 — obligations of providers and deployers: where multiple parties are involved in bringing an AI system to market, the responsibilities of each must be clearly defined; Article 26 — deployer obligations including oversight and incident reporting; Article 28 — obligations of distributors; Article 55 — GPAI model providers' obligations to downstream providers and deployers
- **GDPR**: Article 28 — data processing agreements for third parties processing personal data; Article 44–49 — cross-border transfer requirements for personal data processed by AI third parties

**Tier 2: Conditional** (per AI-POL-00):

- **ISO/IEC 42001:2023**: Controls A.10.2–A.10.4 — applies where AIMS certification is in scope or contractually required
- **Sector-specific supply chain requirements**: NIS2 Article 21(2)(d) — supply chain security including AI component suppliers for in-scope entities; financial sector AI outsourcing requirements (EBA, FINMA) where AI services are materially outsourced

**Tier 3: Informational** (per AI-POL-00):

- NIST AI RMF: GOVERN 6.x — policies and processes for AI supply chain risk management; MAP 5.x — AI risk to third parties
- OECD AI Principles: Principle 1.5 — accountability across the AI value chain

---

## Policy Statements: Allocating Responsibilities Between Parties (A.10.2)

### Responsibility Allocation Requirement

Where [Organisation]'s AI systems involve more than one party — including joint development arrangements, third-party AI component integration, AI-as-a-service consumption, or AI-enabled service delivery to customers — [Organisation] SHALL determine and document which AI-related responsibilities are allocated to each party.

Ambiguity in AI responsibility allocation creates compliance gaps. This policy eliminates ambiguity by requiring explicit, documented allocation before any multi-party AI arrangement commences.

### Responsibility Allocation Framework

For each multi-party AI arrangement, the following responsibilities shall be explicitly allocated:

| Responsibility Domain | Allocation Consideration |
|----------------------|------------------------|
| **AI system specification** | Which party defines the requirements and performance criteria? |
| **Training data governance** | Which party is responsible for data quality, provenance, and compliance? |
| **Model development and validation** | Which party conducts V&V and to what standards? |
| **Impact assessment (AISIA)** | Which party conducts and maintains the AISIA? Is a joint assessment required? |
| **Regulatory compliance** | Which party holds the provider/deployer classification under EU AI Act? What obligations follow? |
| **Monitoring and incident response** | Which party monitors performance? Who is responsible for incident response and notification? |
| **User-facing transparency** | Which party provides transparency notices to affected individuals? |
| **Right to erasure / personal data obligations** | Which party responds to data subject requests relating to AI training data? |
| **Indemnity and liability** | What is each party's exposure for AI-related claims? How are losses allocated contractually? |

### EU AI Act Role Determination

For each third-party AI arrangement, [Organisation] SHALL determine:

- [Organisation]'s role: **provider**, **deployer**, or **both** (per AI-POL-00 role determination framework)
- Third party's role: provider, deployer, distributor, importer, or other
- Where the EU AI Act assigns obligations based on role, each party's obligations shall be documented and agreed contractually

Where a third party provides an AI system or component and [Organisation] modifies it materially for its own use, [Organisation] shall assess whether it assumes provider obligations under EU AI Act Article 25.

### Documentation Requirements

Responsibility allocation shall be documented in:

- The applicable contract or agreement between parties (as a schedule or exhibit)
- An internal **AI Third-Party Responsibility Matrix** maintained by the AI Governance Officer
- Referenced in the AI System Resource Register (AI-POL-A.4.2-6) for the relevant AI system

---

## Policy Statements: Suppliers of AI-Related Products and Services (A.10.3)

### AI Supplier Management Requirement

[Organisation] SHALL implement measures to ensure that suppliers providing AI-related products or services meet [Organisation]'s requirements for responsible AI. AI suppliers that cannot demonstrate adequate responsible AI practices represent a risk to [Organisation]'s AIMS compliance and AI system integrity.

### Scope of AI Supplier Management

This policy applies to third parties that provide:

- **AI foundation models or pre-trained models** used as a basis for [Organisation]'s AI systems
- **AI development platforms or tools** (MLOps, annotation tools, model registries)
- **AI-as-a-service** (AI APIs, AI SaaS platforms used operationally)
- **Training data** sourced from third parties
- **AI system components** embedded in [Organisation]'s AI systems
- **AI system auditing or assessment services**

### Pre-Procurement Assessment

Before engaging a new AI supplier, [Organisation] SHALL assess:

| Assessment Dimension | Minimum Assessment Required |
|---------------------|-----------------------------|
| **Responsible AI practices** | Does the supplier have documented AI governance practices? Certifications (ISO 42001, EU AI Act conformity)? Public AI ethics commitments? |
| **EU AI Act classification** | Is the AI product or service subject to EU AI Act obligations? If high-risk, has conformity been demonstrated (CE marking, notified body involvement)? |
| **Data governance** | Where the supplier's AI involves [Organisation]'s data: what data governance practices does the supplier apply? Where is data processed? |
| **Security** | What security controls govern the AI system and its data? CVE/vulnerability management for AI libraries? |
| **Incident response** | Does the supplier have AI incident response procedures? What are notification obligations to [Organisation]? |
| **Financial and operational resilience** | Is there single-vendor dependency risk? What is the supplier's continuity plan for AI services? |
| **Subprocessors / sub-suppliers** | What AI components does the supplier itself source from fourth parties? |

The depth of assessment shall be proportionate to the AI system's impact classification (AI-POL-A.5.2-5) and the degree of [Organisation]'s dependency on the supplier.

### Contractual Minimum Requirements for AI Suppliers

AI supplier contracts shall include, at minimum:

| Contractual Requirement | Rationale |
|------------------------|-----------|
| **Responsible AI obligations** | Supplier must maintain responsible AI practices consistent with [Organisation]'s requirements and applicable regulation |
| **Intended use limitations** | Supplier's AI system or component may only be used for documented intended purposes; restrictions on use apply downstream |
| **Incident notification** | Supplier must notify [Organisation] within 24 hours of any serious AI incident and within 72 hours of any other material AI incident affecting [Organisation]'s use; content requirements specified |
| **Audit rights** | [Organisation] (and where required, regulators) may audit supplier's AI governance practices upon reasonable notice |
| **Data governance** | Responsibilities for training data, operational data, output data clearly allocated; personal data processing under a GDPR-compliant data processing agreement where applicable |
| **EU AI Act compliance** | Where the supplier's product is subject to EU AI Act obligations, supplier must maintain and provide evidence of compliance; notify [Organisation] of any material change to compliance status |
| **Change notification** | Supplier must notify [Organisation] in advance of material changes to AI system (model updates, training data changes, performance changes) with sufficient lead time for [Organisation]'s re-assessment |
| **Exit and data portability** | Arrangements for transition off the supplier's AI service; data return or deletion; transition assistance |

### Ongoing AI Supplier Monitoring

AI suppliers shall be subject to periodic review, with minimum frequency determined by the impact classification of the supported AI system:

| AI System Impact Classification | Minimum Review Frequency |
|--------------------------------|--------------------------|
| High-impact (significant harm potential, high-risk AI under EU AI Act) | Annual |
| Medium-impact | Every 2 years |
| Low-impact | Every 3 years |

Reviews shall also be triggered by: material incident involving the supplier; EU AI Act compliance status change; significant model update; regulatory change affecting the supplier; change in [Organisation]'s dependency on the supplier; supplier ownership or structural change.

Records of supplier assessments and review outcomes shall be maintained by the Procurement Officer / AI Governance Officer.

---

## Policy Statements: Customers (A.10.4)

### Customer Information Requirement

Where [Organisation] delivers AI-enabled products or services to customers, [Organisation] SHALL communicate appropriate information about the AI system to those customers as part of the product or service relationship.

**Applicability**: This control applies to [Organisation] in the **AI provider** role — delivering AI-enabled products or services externally. Where [Organisation] acts solely as an internal AI deployer, A.10.4 applies to the extent that internal business units or subsidiaries are treated as internal customers.

### Minimum Customer Information Requirements

For each AI-enabled product or service delivered to customers, [Organisation] SHALL provide:

| Information Category | Content |
|--------------------|---------|
| **AI system description** | That the product or service incorporates an AI system; what the AI system does; how it contributes to the product or service output |
| **Intended use** | The uses for which the AI-enabled product or service is designed and validated; the conditions for valid and reliable outputs |
| **Limitations** | Known limitations of the AI system; conditions under which outputs may be less reliable; edge cases the customer should be aware of |
| **Customer responsibilities** | How the customer must use the AI-enabled product or service responsibly; what the customer must not use it for; human oversight obligations on the customer side |
| **Incident reporting** | How customers should report AI incidents, errors, or unexpected outputs to [Organisation]; response commitments |
| **Updates and changes** | How [Organisation] will communicate material changes to the AI system that may affect the customer's use or reliance |
| **Data handling** | How customer data is used in the AI system; whether customer data is used for training; opt-out options if applicable |

### Customer Contract Provisions

Customer contracts for AI-enabled products and services shall include:

| Contract Element | Requirement |
|-----------------|------------|
| **Intended use clause** | Customer's permitted uses defined; prohibition on use outside intended purpose |
| **Responsibility allocation** | Explicit allocation of AI-related responsibilities between [Organisation] and customer (per A.10.2) — including which party bears deployer obligations under EU AI Act |
| **Customer obligation to inform affected individuals** | Where the customer further deploys [Organisation]'s AI to affect third parties, customer's obligation to ensure appropriate transparency |
| **Incident notification (both directions)** | Customer notification to [Organisation] of AI incidents; [Organisation] notification to customer of AI system incidents |
| **Prohibition on harmful use** | Customer may not use [Organisation]'s AI-enabled product for prohibited uses listed in the intended use documentation |
| **Limitation of liability** | Liability for AI-related harm limited where harm arises from customer's use outside intended purpose or customer's failure to apply required human oversight |

### Customer Support for Responsible Use

[Organisation] SHALL provide customers with the resources necessary to use AI-enabled products responsibly:

- Accessible user documentation per AI-POL-A.8.2-5 (A.8.2)
- Contact point for AI-related questions, concerns, and incident reporting
- Training or guidance where the customer's responsible use of the AI-enabled product requires it
- Notification of material AI system changes with adequate lead time for the customer to adapt

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|----------------|
| **AI Governance Officer** | Own the A.10 framework; maintain AI Third-Party Responsibility Matrix; approve responsibility allocation decisions; oversee AI supplier governance |
| **Legal / Procurement Officer** | Draft and negotiate AI supplier and customer contracts; ensure contractual minimum requirements are included; manage AI-specific contract terms |
| **AI System Owner** | Maintain supplier relationships for AI components used in owned AI systems; trigger supplier reassessment when AI system changes |
| **CISO** | Review security dimensions of AI supplier assessments; manage supplier security incidents; maintain supplier security monitoring |
| **DPO / Privacy Officer** | Review third-party AI arrangements involving personal data; ensure GDPR-compliant data processing agreements are in place |
| **Account Management / Customer Success** | Manage customer information obligations; coordinate incident communication with customers; escalate customer AI concerns to AI System Owner |

---

## Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| AI Third-Party Responsibility Matrix | Documented responsibility allocation per multi-party AI arrangement | Current + 3 years |
| AI supplier pre-procurement assessments | Assessment records for AI-related suppliers | Duration of supplier relationship + 3 years |
| AI supplier contracts | Contracts with AI-specific provisions per A.10.3 | Duration of supplier relationship + 5 years |
| AI supplier monitoring records | Periodic review outcomes for AI suppliers | Duration of supplier relationship + 3 years |
| Customer-facing AI documentation | User documentation, transparency notices, intended use communications per A.10.4 | Duration of customer relationship + 5 years |
| Customer contracts | Contracts with AI-specific provisions per A.10.4 | Duration of customer relationship + 5 years |

---

## Audit Considerations

Auditors verifying compliance with A.10.2–A.10.4 should expect to find:

- An AI Third-Party Responsibility Matrix covering multi-party AI arrangements with documented allocation of each party's responsibilities
- EU AI Act role determinations documented for third-party AI arrangements
- Pre-procurement assessment records for AI suppliers, proportionate to dependency and impact classification
- AI supplier contracts with responsible AI, incident notification, audit rights, and change notification provisions
- Evidence of ongoing AI supplier monitoring
- Customer-facing documentation for AI-enabled products and services covering intended use, limitations, and customer responsibilities
- Customer contracts with AI-specific provisions including intended use, responsibility allocation, and incident notification

---

<!-- QA_VERIFIED: [2026-04-15] -->
