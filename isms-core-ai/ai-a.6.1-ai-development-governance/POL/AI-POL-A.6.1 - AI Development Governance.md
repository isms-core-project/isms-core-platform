<!-- ISMS-CORE:POLICY:AI-POL-A.6.1:ai:POL:a.6.1 -->
**AI-POL-A.6.1 — AI Development Governance**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI Development Governance |
| **Document Type** | Policy |
| **Document ID** | AI-POL-A.6.1 |
| **Document Creator** | AI Governance Officer / Chief Technology Officer (CTO) |
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
| 1.0 | [Date to be set] | AI Governance Officer / CTO | Initial policy for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual (or upon significant change in AI development methodology or responsible AI standards)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: AI Governance Officer
- Secondary: Chief Technology Officer (CTO) / AI Engineering Lead
- Compliance: Chief Information Security Officer (CISO)
- Final Authority: Executive Management

**Related Documents**:

- AI-POL-00 (AIMS Regulatory Applicability Framework)
- AI-POL-01 (AIMS Governance and Decision-Making Framework)
- AI-POL-A.5.2-5 (AI System Impact Assessment — AISIA drives control selection)
- AI-POL-A.6.2 (AI System Lifecycle — operational lifecycle controls)
- AI-IMP-A.6.1-UG (AI Development Governance — User Guide)
- AI-IMP-A.6.1-TG (AI Development Governance — Technical Guide)
- ISO/IEC 42001:2023 Controls A.6.1.2, A.6.1.3
- ISO/IEC 42001:2023 Annex B.6.1 (Implementation guidance — Management guidance for AI system development)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for identifying and integrating responsible development objectives, and for defining and documenting the processes by which AI systems are responsibly designed and developed — in accordance with ISO/IEC 42001:2023 Controls A.6.1.2 and A.6.1.3.

**Scope**: All AI systems developed by [Organisation] (AI provider role); the objectives, processes, and governance practices that guide the development life cycle from design to handover for deployment.

**Applicability Note**: A.6.1 controls apply primarily to organisations acting as **AI providers** — those that develop, train, or otherwise create AI systems. Organisations acting solely as AI deployers (using third-party AI without modification) should document this in the AIMS SoA and apply A.6.1 where they have material influence over AI system design or configuration.

**Purpose**: Define WHAT responsible development objectives must be established and documented (A.6.1.2), and WHAT processes for responsible design and development must be defined (A.6.1.3). Implementation in AI-IMP-A.6.1-UG and AI-IMP-A.6.1-TG.

**Combined Control Rationale**: A.6.1.2 and A.6.1.3 form the strategic and process governance layer for AI development. Objectives (A.6.1.2) establish the responsible AI principles that must be integrated into the development cycle; processes (A.6.1.3) define HOW those principles are implemented operationally. Both controls must be applied together to provide effective development governance.

---

## Scope and Applicability

### ISO/IEC 42001:2023 Control Statements

**Control A.6.1.2 — Objectives for responsible development of AI system**
The organisation shall identify and document objectives to guide the responsible development of AI systems, and take those objectives into account and integrate measures to achieve them in the development life cycle.

**Control A.6.1.3 — Processes for responsible AI system design and development**
The organisation shall define and document the specific processes for the responsible design and development of the AI system.

### What This Policy Covers

- Responsible AI development objectives that must be established per AI system
- Process requirements for responsible AI design and development
- Integration of AISIA outcomes into development governance
- Responsible AI checkpoints across the development life cycle

### What This Policy Does NOT Cover

- Operational lifecycle controls (requirements, V&V, deployment, monitoring — addressed in AI-POL-A.6.2)
- Data management processes (addressed in AI-POL-A.7.2-6)
- EU AI Act conformity assessment procedures (addressed in AI-POL-A.8.2-5 and AI-POL-00)

### Regulatory Framework

**Tier 1: Mandatory Compliance** (per AI-POL-00):

- **EU AI Act (Regulation 2024/1689)**: Article 9 — high-risk AI providers must establish a quality management system addressing responsible AI objectives; Article 9(1)(b) — design and development methodology; Article 10 — training, validation, testing requirements for responsible development

**Tier 2: Conditional** (per AI-POL-00):

- **ISO/IEC 42001:2023**: Controls A.6.1.2, A.6.1.3 — applies where AIMS certification is in scope or contractually required

**Tier 3: Informational** (per AI-POL-00):

- NIST AI RMF: GOVERN 4.x — organisational AI development practices; MAP 2.x — impact identification in development
- ISO/IEC 23894:2023: Risk management considerations during AI development

---

## Policy Statements: Responsible Development Objectives (A.6.1.2)

### Responsible Development Objective Requirement

[Organisation] SHALL identify and document objectives for the responsible development of each AI system. These objectives shall:

- Be established before development begins (not retrospectively)
- Reflect the responsible AI principles in the AI Policy (AI-POL-A.2.2-4)
- Be informed by the AISIA outcomes for the AI system (AI-POL-A.5.2-5)
- Be integrated into the development life cycle as measurable design criteria, not aspirational statements
- Be approved by the AI Governance Officer before development commences

### Core Responsible Development Objectives

The following responsible AI properties shall be considered as objectives for every AI system developed by [Organisation]. Applicability and implementation level are determined by the AISIA impact classification (Low / Medium / High):

**Fairness and Non-Discrimination**

The AI system shall treat individuals and groups equitably. Objectives shall specify:

- Which demographic groups or protected characteristics are relevant for fairness evaluation
- Which fairness metric(s) are appropriate for the use case (e.g., demographic parity, equalised odds, predictive parity)
- Acceptable thresholds for fairness metrics before deployment — thresholds shall be defined by the AI Governance Officer in consultation with the CTO and relevant domain expertise, documented in the AISIA and approved before V&V begins
- Process for monitoring fairness in production (A.6.2.6)

**Transparency and Explainability**

The AI system's outputs shall be interpretable to the degree necessary for human oversight and affected individual communication. Objectives shall specify:

- Required level of explainability (feature importance, decision rationale, local explanations) based on use case and impact classification
- Audience for explanations (internal operators, affected individuals, regulators)
- Documentation of model limitations and conditions under which outputs may be unreliable

**Robustness and Safety**

The AI system shall perform reliably within its documented operating conditions and fail safely when conditions are outside the defined operating envelope. Objectives shall specify:

- Defined operating conditions and out-of-distribution detection requirements
- Adversarial robustness requirements (where the AI system could be a target)
- Acceptable failure modes and fail-safe behaviour
- Testing coverage for edge cases and adversarial inputs

**Privacy by Design**

The AI system shall process personal data minimally and by design, not as an afterthought. Objectives shall specify:

- Data minimisation requirements for training and operational data
- Anonymisation or pseudonymisation requirements
- GDPR Article 25 (data protection by design and by default) requirements where applicable
- Co-reference to PRIV-POL-00 obligations

**Human Oversight**

AI system design shall support, not undermine, meaningful human oversight. Objectives shall specify:

- Human review checkpoints required before AI-driven decisions affect individuals
- Override mechanisms — ability for humans to override AI outputs
- Logging and audit trail requirements to support human review
- Alert mechanisms for anomalous AI system behaviour

**Accountability**

Clear human accountability for AI system behaviour shall be maintained. Objectives shall specify:

- Named AI Risk Owner accountable for the AI system (AI-POL-A.3.2-3)
- Escalation path for AI incidents
- Audit trail requirements linking AI outputs to the system version that produced them

### Documenting Responsible Development Objectives

Responsible development objectives shall be documented in an **AI System Development Objectives Record** for each AI system, signed by:

- AI Governance Officer (responsible AI governance approval)
- AI Risk Owner (risk acceptance)
- CTO / AI Engineering Lead (technical feasibility confirmation)

The record shall be updated if the AISIA outcome changes materially.

---

## Policy Statements: Processes for Responsible AI Design and Development (A.6.1.3)

### Process Definition Requirement

[Organisation] SHALL define and document the specific processes for the responsible design and development of each AI system. These processes shall operationalise the responsible development objectives defined under A.6.1.2.

### Required Responsible Development Processes

**1. Responsible AI Design Review**

Before development commences, a design review process shall validate that:

- The proposed AI system architecture supports the documented responsible AI objectives
- Fairness, explainability, and privacy considerations are embedded in the design, not added post-hoc
- The intended use is clearly specified and scope-limiting controls are designed in

The design review shall be documented, with approval from the AI Governance Officer.

**2. Bias and Fairness Assessment Process**

For AI systems with Medium or High impact classification (per AI-POL-A.5.2-5), the development process shall include:

- Pre-development: Dataset representativeness assessment — does the training data represent the deployment population?
- Development: Fairness-aware model selection and training — which fairness constraints or objectives are integrated?
- Pre-deployment: Fairness evaluation against approved metrics and thresholds
- Post-deployment: Ongoing fairness monitoring (A.6.2.6)

The bias assessment process shall be documented per AI system with evidence retained.

**3. Responsible AI Development Checkpoints**

The development process shall include defined checkpoints at which responsible AI criteria are evaluated before proceeding to the next stage:

| Checkpoint | Stage | What is Verified |
|-----------|-------|-----------------|
| Design approval | Before development begins | Responsible AI objectives documented; AISIA completed; data sources approved |
| Data quality gate | Before model training | Data representativeness, quality criteria met; provenance documented |
| Development review | During active development | Fairness, explainability, and privacy controls implemented as designed |
| Pre-validation review | Before V&V (A.6.2.4) | Model documentation complete; testing criteria defined including responsible AI criteria |
| Pre-deployment approval | Before deployment (A.6.2.5) | All responsible AI objectives assessed; AISIA current; human oversight mechanisms implemented |

Each checkpoint shall produce a documented outcome. A system that does not pass a responsible AI checkpoint shall not progress to the next stage until issues are resolved.

**4. Responsible AI Documentation Process**

Throughout development, the following documentation shall be maintained:

- **Model card**: Intended use, training data description, evaluation results including fairness metrics, known limitations, out-of-scope uses
- **Data card**: Dataset description, collection methodology, representativeness assessment, bias analysis
- **Responsible AI criteria record**: How each responsible AI objective was addressed in the design and development

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|----------------|
| **AI Governance Officer** | Approve responsible development objectives; approve design review; conduct or commission responsible AI checkpoint reviews; maintain objective records |
| **CTO / AI Engineering Lead** | Lead responsible AI design reviews; ensure development process includes checkpoints; ensure engineering teams are trained in responsible AI practices |
| **AI System Owner** | Maintain responsible development objectives record; ensure checkpoint documentation is complete |
| **Data Scientists / ML Engineers** | Apply fairness-aware techniques; complete data representativeness assessments; document model cards and data cards |
| **AI Risk Owner** | Accept residual responsible AI risk; escalate where objectives cannot be met |

---

## Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Responsible development objectives record | Per-AI-system document of responsible AI objectives with approval | Duration of system + 3 years |
| Design review records | Documentation of responsible AI design reviews with outcomes | Duration of system + 3 years |
| Checkpoint records | Evidence of each responsible AI checkpoint with pass/fail outcome | Duration of system + 3 years |
| Model cards | Model documentation including fairness evaluation and limitations | Duration of system + 3 years |
| Data cards | Dataset documentation including representativeness and bias analysis | Duration of dataset use + 3 years |

---

## Audit Considerations

Auditors verifying compliance with A.6.1.2–A.6.1.3 should expect to find:

- Documented responsible development objectives per AI system, predating development
- Evidence that objectives were informed by AISIA outcomes
- Defined development process with responsible AI checkpoints
- Checkpoint records demonstrating that responsible AI criteria were evaluated before stage transitions
- Model cards and data cards as output artefacts of the development process

---

<!-- QA_VERIFIED: [2026-04-15] -->
