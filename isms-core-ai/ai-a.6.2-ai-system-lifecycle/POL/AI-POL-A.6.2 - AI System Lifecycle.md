<!-- ISMS-CORE:POLICY:AI-POL-A.6.2:ai:POL:a.6.2 -->
**AI-POL-A.6.2 — AI System Lifecycle**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI System Lifecycle |
| **Document Type** | Policy |
| **Document ID** | AI-POL-A.6.2 |
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

**Review Cycle**: Annual (or upon significant change to AI development and operations practices)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: AI Governance Officer
- Secondary: Chief Technology Officer (CTO) / AI Engineering Lead
- Compliance: Chief Information Security Officer (CISO)
- Final Authority: Executive Management

**Related Documents**:

- AI-POL-00 (AIMS Regulatory Applicability Framework)
- AI-POL-A.6.1 (AI Development Governance — pre-lifecycle objectives and processes)
- AI-POL-A.7.2-6 (Data for AI Systems)
- AI-POL-A.5.2-5 (AI System Impact Assessment — AISIA must precede deployment)
- AI-IMP-A.6.2-UG (AI System Lifecycle — User Guide)
- AI-IMP-A.6.2-TG (AI System Lifecycle — Technical Guide)
- ISO/IEC 42001:2023 Controls A.6.2.2, A.6.2.3, A.6.2.4, A.6.2.5, A.6.2.6, A.6.2.7, A.6.2.8
- ISO/IEC 42001:2023 Annex B.6.2 (Implementation guidance — AI system life cycle)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for the AI system life cycle — covering specification, design and development documentation, verification and validation, deployment, operation and monitoring, technical documentation, and event logging — in accordance with ISO/IEC 42001:2023 Controls A.6.2.2 through A.6.2.8.

**Scope**: All AI systems within the AIMS scope across all life cycle stages from specification through decommissioning. Controls apply to AI providers (primary) and AI deployers where they have significant influence over lifecycle management.

**Purpose**: Define WHAT must be documented and controlled at each life cycle stage, WHO is responsible, and WHEN controls apply. Implementation detail in AI-IMP-A.6.2-UG and AI-IMP-A.6.2-TG.

**Combined Control Rationale**: A.6.2.2 through A.6.2.8 map directly to the stages of the AI system life cycle. Each control governs a distinct stage: specification → design/development documentation → verification/validation → deployment → operation/monitoring → technical documentation → event logging. These seven controls are interdependent — each stage produces outputs that the next depends upon.

---

## Scope and Applicability

### ISO/IEC 42001:2023 Control Statements

**Control A.6.2.2 — AI system requirements and specification**
The organisation shall specify and document requirements for new AI systems or material enhancements to existing systems.

**Control A.6.2.3 — Documentation of AI system design and development**
The organisation shall document the AI system design and development based on organisational objectives, documented requirements and specification criteria.

**Control A.6.2.4 — AI system verification and validation**
The organisation shall define and document verification and validation measures for the AI system and specify criteria for their use.

**Control A.6.2.5 — AI system deployment**
The organisation shall document a deployment plan and ensure that appropriate requirements are met prior to deployment.

**Control A.6.2.6 — AI system operation and monitoring**
The organisation shall define and document the necessary elements for the ongoing operation of the AI system. At the minimum, this should include system and performance monitoring, repairs, updates and support.

**Control A.6.2.7 — AI system technical documentation**
The organisation shall determine what AI system technical documentation is needed for each relevant category of interested parties, such as users, partners, supervisory authorities, and provide the technical documentation to them in the appropriate form.

**Control A.6.2.8 — AI system recording of event logs**
The organisation shall determine at which phases of the AI system life cycle, record keeping of event logs should be enabled, but at the minimum when the AI system is in use.

### Regulatory Framework

**Tier 1: Mandatory Compliance** (per AI-POL-00):

- **EU AI Act (Regulation 2024/1689)**: Article 11 (technical documentation), Article 12 (record-keeping and logging), Article 13 (transparency and information provision), Article 14 (human oversight), Article 15 (accuracy, robustness, cybersecurity), Article 17 (QMS — all lifecycle stages)

**Tier 2: Conditional** (per AI-POL-00):

- **ISO/IEC 42001:2023**: Controls A.6.2.2–A.6.2.8 — applies where AIMS certification is in scope or contractually required

---

## Policy Statements: Requirements and Specification (A.6.2.2)

### AI System Specification Requirement

[Organisation] SHALL specify and document requirements for every new AI system and for material enhancements to existing systems before development or enhancement begins.

### Specification Document Requirements

The AI system specification shall document:

| Element | Content Required |
|---------|----------------|
| **Intended purpose** | Clear statement of what the AI system is designed to do, for whom, and in what context |
| **Functional requirements** | What the system must do (inputs, outputs, decision types, performance expectations) |
| **Non-functional requirements** | Reliability, availability, response time, scalability, security |
| **Responsible AI requirements** | Fairness metrics and thresholds; explainability level; human oversight mechanisms; derived from AISIA and AI-POL-A.6.1 objectives |
| **Operating conditions** | Conditions under which the AI system is expected to operate correctly (data distribution assumptions, environmental conditions) |
| **Out-of-scope uses** | Explicitly documented uses for which the system is NOT designed or validated |
| **Stakeholders** | Internal and external parties who will interact with or be affected by the system |
| **Regulatory constraints** | EU AI Act risk classification; GDPR Article 22 triggers; other applicable obligations |
| **Integration requirements** | How the AI system integrates with existing systems and processes |

**Material enhancement** is defined as any change that: modifies AI system outputs in a material way; introduces the system to a new population; changes the operating context or intended purpose; or changes the model architecture, training data, or key hyperparameters.

---

## Policy Statements: Design and Development Documentation (A.6.2.3)

### Design and Development Documentation Requirement

[Organisation] SHALL document the AI system design and development, ensuring the documentation is traceable to the specification and responsible AI objectives.

### Required Documentation

| Documentation | Content |
|--------------|---------|
| **Architecture documentation** | High-level system architecture; component diagram; data flow; integration points |
| **Model documentation** | Algorithm selection rationale; model architecture; training approach; hyperparameter choices |
| **Training data documentation** | Datasets used; pre-processing steps; data split methodology; link to A.7 data records |
| **Design decisions log** | Key design decisions with rationale; trade-offs made; alternatives considered |
| **Responsible AI design decisions** | How fairness, transparency, and safety requirements were addressed in design |
| **Version history** | All model versions with changes documented; reproducibility information |

Documentation shall be version-controlled and linked to the AI system version it describes.

---

## Policy Statements: Verification and Validation (A.6.2.4)

### V&V Requirement

[Organisation] SHALL define and document verification and validation measures for each AI system before deployment, and specify criteria that must be met for deployment authorisation.

### Verification

Verification confirms that the AI system was built correctly per specifications:

- Functional testing against specification requirements
- Performance testing (accuracy, precision/recall, or task-specific metrics) against defined thresholds
- Security testing — adversarial input testing, model robustness assessment
- Integration testing in staging environment

### Validation

Validation confirms that the AI system solves the right problem and is suitable for its intended use:

- Responsible AI validation — fairness metrics evaluated against approved thresholds; explainability validated for target audience
- Intended use validation — testing with real-world conditions and edge cases
- Out-of-distribution testing — behaviour documented when inputs fall outside training distribution
- Human oversight validation — override mechanisms function correctly; alert thresholds calibrated

### Deployment Criteria

Each AI system shall have documented criteria that must be met before deployment authorisation. The AI Governance Officer shall sign off V&V completion against criteria. A system that does not meet V&V criteria shall not be deployed.

---

## Policy Statements: Deployment (A.6.2.5)

### Deployment Plan Requirement

[Organisation] SHALL document a deployment plan for each AI system and ensure all pre-deployment requirements are satisfied before operational deployment.

### Deployment Plan Content

| Element | Content Required |
|---------|----------------|
| **Deployment scope** | Which environments, user populations, and use cases are covered in this deployment |
| **Pre-deployment checklist** | All requirements that must be confirmed before deployment (AISIA approved, V&V passed, technical documentation ready, human oversight implemented, logging enabled) |
| **Rollout approach** | Staged rollout / shadow mode / full deployment — with rationale |
| **Rollback procedure** | How to revert to previous state if deployment causes unexpected issues |
| **Monitoring activation** | How operational monitoring (A.6.2.6) is activated at deployment |
| **Stakeholder communication** | Who must be informed of the deployment and how |
| **Deployment authorisation** | Named authoriser (AI Governance Officer must approve) and authorisation date |

**Deployment gate**: No AI system shall be deployed without documented AI Governance Officer approval confirming that all pre-deployment requirements are met, including a current AISIA.

---

## Policy Statements: Operation and Monitoring (A.6.2.6)

### Operational Monitoring Requirement

[Organisation] SHALL define and document the elements required for the ongoing operation and monitoring of each in-scope AI system.

### Mandatory Monitoring Elements

**Performance monitoring**:

- Key performance indicators (KPIs) defined at specification stage (A.6.2.2)
- Monitoring frequency appropriate to use case (continuous / daily / weekly)
- Performance degradation thresholds — when performance drops below threshold, alert is triggered
- Model drift detection — statistical monitoring of input data distribution and output distribution

**Responsible AI monitoring**:

- Fairness monitoring — fairness metrics measured in production on a defined schedule
- Bias detection — monitoring for emergence of bias in production that was not present at V&V
- Human oversight effectiveness — are override mechanisms being used appropriately?
- Scope adherence — is the AI system being used for documented intended purposes only?

**Operational monitoring**:

- System availability and uptime
- Response time and throughput
- Error rates and failure modes
- Infrastructure health (linked to A.4.5)

**Incident alerting**:

- Defined alert conditions for each monitoring dimension
- Escalation path from automated alert to AI System Owner to AI Risk Owner
- Integration with AI incident response process (AI-POL-A.8.2-5)

### Monitoring Documentation

The monitoring plan for each AI system shall be documented before deployment, covering all mandatory monitoring elements with:

- What is monitored
- How it is monitored (tool, method)
- Frequency
- Alert thresholds
- Escalation path for threshold breaches

---

## Policy Statements: Technical Documentation (A.6.2.7)

### Technical Documentation Requirement

[Organisation] SHALL determine what technical documentation is needed for each relevant category of interested parties and provide it in the appropriate form.

### Interested Party Categories and Documentation Requirements

| Interested Party | Documentation Required |
|-----------------|----------------------|
| **Internal operators / users** | User guide; intended use specification; limitations; operating procedures; override mechanisms |
| **AI System Owner / Governance** | Full technical specification; model card; V&V report; AISIA summary; monitoring plan |
| **IT / Infrastructure** | System architecture; integration documentation; infrastructure requirements; deployment runbook |
| **Regulatory authorities** | EU AI Act technical documentation (Article 11 for high-risk AI); AISIA summary; conformity assessment documentation |
| **Customers / partners** | Capability description; limitations; transparency notice (A.8.2); incident reporting mechanism (A.8.3) |
| **Auditors (internal/external)** | Full documentation set; evidence of V&V; AISIA; SoA reference |

Technical documentation shall be version-controlled, linked to the AI system version it describes, and reviewed at each material change.

---

## Policy Statements: Event Logging (A.6.2.8)

### Event Logging Requirement

[Organisation] SHALL determine at which phases of the AI system life cycle event logging shall be enabled. At minimum, event logging shall be active when the AI system is in operational use.

### Mandatory Logging Phases

| Life Cycle Phase | Logging Requirement |
|----------------|-------------------|
| **Operational use** | MANDATORY — all AI system interactions, inputs, outputs, and decisions shall be logged |
| **Validation and testing** | Required — test inputs, outputs, and evaluation results logged for traceability |
| **Deployment** | Required — deployment event, version, authoriser, timestamp |
| **Monitoring alerts** | Required — all threshold breaches and alert events |
| **Incidents** | Required — all AI incident events for post-incident review |
| **Development** | Best practice — model training runs, hyperparameter sets, evaluation metrics |

### Log Content Requirements

For operational AI system logs, each event record shall include at minimum:

- Timestamp (UTC)
- AI system identifier and version
- Input summary (or input hash where logging full inputs is prohibited by data protection obligations)
- Output or decision produced
- Any human override applied
- User or session identifier (where applicable and permissible)

### Log Retention

AI system event logs shall be retained for:

- Duration of AI system operational life, PLUS
- 3 years after decommissioning minimum (extend where EU AI Act or sector regulations require longer periods)

### Log Protection

AI system event logs are audit evidence. They shall be:

- Protected against modification or deletion (immutable or append-only where feasible)
- Access-controlled (read-only for auditors; restricted write access for log management)
- Backed up per ISMS backup requirements

---

## Policy Statements: Decommissioning

### Decommissioning Requirement

[Organisation] SHALL manage the planned end-of-life of AI systems in a controlled manner that preserves evidence, protects data subjects, and ensures no residual harm arises from discontinued systems.

### Decommissioning Trigger Conditions

An AI system decommissioning process shall be initiated when:

- The AI system is being permanently withdrawn from operational use
- A replacement system is being deployed and the existing system retired
- The AI system's AISIA identifies risks that cannot be adequately mitigated
- The intended use case is discontinued
- A material change would require full re-assessment that the system cannot meet

### Decommissioning Process

The AI System Owner shall execute a documented decommissioning plan approved by the AI Governance Officer covering:

| Step | Requirement |
|------|------------|
| **User notification** | Notify all users and affected parties of the planned decommission date with adequate notice (minimum 30 days for operational systems; as required by contractual obligations for customer-facing systems) |
| **Data disposition** | Define the fate of all training data, operational data, and output data: delete, archive, or transfer — documented per the GDPR data lifecycle requirements |
| **Model disposal** | Confirm deletion of model weights and associated artefacts from all environments (production, staging, backups), or document justification for retention |
| **Access revocation** | Revoke all user and API access to the system before or at decommission |
| **Log preservation** | Retain event logs for a minimum of 3 years post-decommission, or as required by applicable regulation |
| **AISIA closure** | Close the AISIA with a decommission record, noting the disposal method and confirming outstanding risks are resolved |
| **EU AI Act registry** | Where the system was registered in the EU AI Act database, update registration status to decommissioned |
| **Third-party notification** | Notify relevant third parties (AI component suppliers, data processors) of the decommission and obtain confirmation of data deletion where required |

### Evidence Requirements for Decommissioning

The AI Governance Officer shall retain a **Decommission Record** per system including: system identity, decommission date, disposal method for data and model artefacts, user notification confirmation, and AISIA closure.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|----------------|
| **AI Governance Officer** | Approve deployment (all stages); own lifecycle policy; review monitoring reports; approve technical documentation for regulatory audiences; approve decommissioning plans |
| **CTO / AI Engineering Lead** | Own A.6.2.2 specification, A.6.2.3 documentation, A.6.2.4 V&V processes; ensure engineering practices meet policy |
| **AI System Owner** | Maintain all lifecycle documentation for owned systems; own monitoring plan; respond to monitoring alerts |
| **CISO** | Review security dimensions of V&V (A.6.2.4), monitoring (A.6.2.6), and logging (A.6.2.8) |
| **AI Risk Owner** | Accept residual risks identified at V&V; approve deployment risk acceptance |

---

## Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| AI system specification | Documented requirements per AI system version | Duration of system + 3 years |
| Design and development documentation | Architecture, model, training, decision log | Duration of system + 3 years |
| V&V records | Test plans, test results, deployment criteria pass/fail | Duration of system + 3 years |
| Deployment plan and authorisation | Deployment plan with AI Governance Officer approval | Duration of system + 3 years |
| Monitoring plan | Documented monitoring plan with thresholds | Duration of system + 3 years |
| Technical documentation | Version-controlled documentation per interested party category | Duration of system + 3 years |
| Event logs | AI system operational logs | Duration of system + 3 years post-decommission |
| Decommission records | Disposal method, data deletion confirmation, AISIA closure, user notification | 5 years post-decommission |

---

## Audit Considerations

Auditors verifying compliance with A.6.2.2–A.6.2.8 should expect to find:

- Specification documents for all in-scope AI systems predating development
- Design and development documentation traceable to specifications
- V&V reports with documented deployment criteria and pass/fail outcomes
- Deployment authorisation records with AI Governance Officer sign-off
- Active monitoring plans with alert configurations
- Technical documentation available for each interested party category
- Active event logging in operational use, with retention policy documented
- Decommission records for retired AI systems, including data/model disposal confirmation and AISIA closure

---

<!-- QA_VERIFIED: 2026-04-15 -->
