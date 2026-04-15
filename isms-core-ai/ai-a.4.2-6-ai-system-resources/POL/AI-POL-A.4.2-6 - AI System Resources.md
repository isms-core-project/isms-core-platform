<!-- ISMS-CORE:POLICY:AI-POL-A.4.2-6:ai:POL:a.4.2-6 -->
**AI-POL-A.4.2-6 — AI System Resources**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI System Resources |
| **Document Type** | Policy |
| **Document ID** | AI-POL-A.4.2-6 |
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

**Review Cycle**: Annual (or upon significant change to AI system portfolio or resource infrastructure)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: AI Governance Officer
- Secondary: Chief Technology Officer (CTO) / AI Engineering Lead
- Compliance: Chief Information Security Officer (CISO)
- Final Authority: Executive Management

**Related Documents**:

- AI-POL-00 (AIMS Regulatory Applicability Framework)
- AI-POL-01 (AIMS Governance and Decision-Making Framework)
- AI-POL-A.3.2-3 (AI Roles and Responsibilities — human resources competence)
- AI-IMP-A.4.2-6-UG (AI System Resources — User Guide)
- AI-IMP-A.4.2-6-TG (AI System Resources — Technical Guide)
- ISO/IEC 42001:2023 Controls A.4.2, A.4.3, A.4.4, A.4.5, A.4.6
- ISO/IEC 42001:2023 Clause 7.1 (Resources)
- ISO/IEC 42001:2023 Annex B.4 (Implementation guidance — Resources for AI systems)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for identifying, documenting, and managing all resources associated with AI systems across their life cycles — in accordance with ISO/IEC 42001:2023 Controls A.4.2 through A.4.6.

**Scope**: All AI systems within the AIMS scope; all resource types used at any stage of the AI system life cycle (data, tooling, infrastructure, human resources).

**Purpose**: Define WHAT resource documentation must be maintained, WHO is responsible for keeping it current, and WHEN it must be reviewed and updated. Implementation procedures are in AI-IMP-A.4.2-6-UG and AI-IMP-A.4.2-6-TG.

**Combined Control Rationale**: A.4.2 through A.4.6 collectively form the resource identification and documentation requirement for the AIMS. Understanding what resources an AI system depends upon — across data, tooling, computing, and human capital — is foundational to accurate risk assessment and impact assessment. A.4.2 sets the overarching documentation obligation; A.4.3 through A.4.6 specify the resource categories that must be documented.

---

## Scope and Applicability

### ISO/IEC 42001:2023 Control Statements

**Control A.4.2 — Resource documentation**
The organisation shall identify and document relevant resources required for the activities at given AI system life cycle stages and other AI-related activities relevant for the organisation.

**Control A.4.3 — Data resources**
As part of resource identification, the organisation shall document information about the data resources utilised for the AI system.

**Control A.4.4 — Tooling resources**
As part of resource identification, the organisation shall document information about the tooling resources utilised for the AI system.

**Control A.4.5 — System and computing resources**
As part of resource identification, the organisation shall document information about the system and computing resources utilised for the AI system.

**Control A.4.6 — Human resources**
As part of resource identification, the organisation shall document information about the human resources and their competences utilised for the development, deployment, operation, change management, maintenance, transfer and decommissioning, as well as verification and integration of the AI system.

### What This Policy Covers

- Requirements for the AI System Resource Register
- Documentation standards for each resource category (data, tooling, computing, human)
- Resource review and update obligations
- Competence documentation and gap management for human resources

### What This Policy Does NOT Cover

- Detailed data quality and data management processes (addressed in AI-POL-A.7.2-6)
- Supplier management for AI resources (addressed in AI-POL-A.10.2-4)
- AI system lifecycle technical processes (addressed in AI-POL-A.6.2)

### Regulatory Framework

**Tier 1: Mandatory Compliance** (per AI-POL-00):

- **EU AI Act (Regulation 2024/1689)**: Article 11 (technical documentation for high-risk AI must include information on training data, computational resources, and human oversight infrastructure); Article 9 (QMS must address resource management)

**Tier 2: Conditional** (per AI-POL-00):

- **ISO/IEC 42001:2023**: Controls A.4.2–A.4.6 — applies where AIMS certification is in scope or contractually required

**Tier 3: Informational** (per AI-POL-00):

- NIST AI RMF: GOVERN 4.x — organisational team AI risk responsibilities; MAP 1.x — AI context establishment including resource identification

---

## Policy Statements: Resource Documentation (A.4.2)

### AI System Resource Register

[Organisation] SHALL maintain an **AI System Resource Register** documenting all significant resources associated with each in-scope AI system. The register shall be maintained as a controlled document per ISO 42001:2023 Clause 7.5 and updated at each life cycle stage.

The register shall identify resources by:

- Life cycle stage (development / training / validation / deployment / operation / decommissioning)
- Resource category (data / tooling / computing / human)
- Resource status (in use / archived / decommissioned)
- Owner or responsible party

The AI System Owner is responsible for maintaining the resource register entries for their AI system. The AI Governance Officer is responsible for the completeness and integrity of the consolidated register.

---

## Policy Statements: Data Resources (A.4.3)

### Data Resource Documentation Requirement

For each AI system, [Organisation] SHALL document the data resources used across all life cycle stages.

### Required Data Resource Documentation

| Field | Content Required |
|-------|----------------|
| Dataset name / identifier | Name or reference for each dataset used |
| Life cycle stage | Training / validation / testing / operation |
| Data source | Origin of data (internal system, licensed dataset, public dataset, collected data) |
| Data type | Structured / unstructured / image / text / tabular / time series / other |
| Volume | Approximate scale (records, GB, tokens) |
| Update frequency | Static / periodic update / real-time stream |
| Licensing / rights | Ownership or licence under which data is used |
| Personal data | Yes / No — if yes, link to PRIV-POL-00 and relevant DPIA |
| Sensitivity classification | Per ISMS data classification scheme |
| Data quality assessment reference | Link to quality assessment record (A.7.4) |
| Provenance record reference | Link to data provenance record (A.7.5) |
| Retention period | How long data is retained after use |

Detailed data management requirements are governed by AI-POL-A.7.2-6.

---

## Policy Statements: Tooling Resources (A.4.4)

### Tooling Resource Documentation Requirement

For each AI system, [Organisation] SHALL document the tooling resources used across all life cycle stages.

### Required Tooling Resource Documentation

| Field | Content Required |
|-------|----------------|
| Tool name and version | Name and version of each AI tool, framework, or library |
| Tool category | ML framework / IDE / annotation tool / evaluation tool / MLOps platform / model registry / other |
| Life cycle stage(s) | Where in the lifecycle the tool is used |
| Licence type | Open source (with licence identifier) / commercial / proprietary |
| Supplier / maintainer | Organisation or project maintaining the tool |
| Version pinning | Whether tool version is pinned; rationale if not |
| Security assessment | Reference to vulnerability assessment or CVE monitoring status |
| Replacement / deprecation risk | Known EOL date or migration risk |

---

## Policy Statements: System and Computing Resources (A.4.5)

### System and Computing Resource Documentation Requirement

For each AI system, [Organisation] SHALL document the system and computing infrastructure resources used.

### Required System and Computing Documentation

| Field | Content Required |
|-------|----------------|
| Infrastructure component | Name / identifier of each infrastructure component |
| Component type | GPU / CPU cluster / cloud service / on-premise server / edge device / other |
| Provider | Internal IT / cloud provider (AWS, Azure, GCP, etc.) / third-party service |
| Capacity | Compute, memory, and storage specifications relevant to AI workload |
| Life cycle stage(s) | Where in the lifecycle the resource is used |
| Availability requirements | Uptime / SLA requirements for operational AI |
| Security controls | Link to relevant ISMS-POL controls governing the infrastructure |
| Environmental footprint | Energy consumption or carbon data where applicable (supports societal impact awareness per A.5.5) |
| Single points of failure | Identified SPOF and mitigation status |

---

## Policy Statements: Human Resources (A.4.6)

### Human Resource and Competence Documentation Requirement

[Organisation] SHALL document the human resources and their competences involved in the AI system across all life cycle stages, from development through decommissioning.

### Competence Matrix

For each AI system, a competence matrix shall be maintained identifying:

| Life Cycle Activity | Required Competences | Current Role(s) | Competence Status |
|---------------------|---------------------|----------------|-------------------|
| AI system development | ML/AI engineering, responsible AI design, data science | AI Engineer / Data Scientist | Assessed / Gap identified |
| Data management | Data engineering, data quality, data governance | Data Engineer / Data Governance Lead | Assessed / Gap identified |
| Verification and validation | AI testing, fairness evaluation, adversarial testing | QA Engineer / AI Evaluator | Assessed / Gap identified |
| Deployment | MLOps, deployment security, monitoring setup | MLOps Engineer / DevOps | Assessed / Gap identified |
| Operation and monitoring | AI performance monitoring, drift detection, incident response | AI Operations / Platform Team | Assessed / Gap identified |
| Change management | AI change impact assessment, re-assessment triggers | AI System Owner / AI Risk Owner | Assessed / Gap identified |
| Transfer and integration | AI integration architecture, API management | Solution Architect / Engineering Lead | Assessed / Gap identified |
| Decommissioning | Data disposal, model retirement, documentation archival | AI System Owner / Data Governance Lead | Assessed / Gap identified |
| Governance oversight | ISO 42001, EU AI Act, AIMS governance | AI Governance Officer | Assessed / Gap identified |

### Competence Gap Management

Where a competence gap is identified in the matrix:

1. AI Governance Officer is notified
2. HR and the relevant function agree a resolution plan: training, hiring, or external advisory engagement
3. Resolution plan is documented in the Resource Register with target date
4. Gaps are reported to management review as open items until resolved

### Awareness

All persons working on or with AI systems shall receive AI awareness training covering:

- The organisation's AI Policy and responsible AI principles
- Their specific role in the AIMS and its objectives
- How to report AI concerns (A.3.3)
- Applicable responsible use requirements (AI-POL-A.9.2-4)

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|----------------|
| **AI Governance Officer** | Own the consolidated AI System Resource Register; review for completeness at management review; identify systemic resource gaps |
| **AI System Owners** | Maintain resource register entries for their AI systems; keep documentation current at each lifecycle transition |
| **CTO / AI Engineering Lead** | Ensure tooling and computing resource documentation is technically accurate; manage tooling security and deprecation risk |
| **Data Governance Lead** | Maintain data resource documentation; ensure data licensing and provenance entries are accurate |
| **HR** | Support human resource competence assessments; coordinate training for competence gaps |

---

## Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| AI System Resource Register | Consolidated register covering all resource categories per AI system | Current + 3 years |
| Competence matrices | Per-AI-system competence assessments with gap status | Current + 3 years |
| Competence gap resolution plans | Documented plans for addressing identified gaps | Until gap closed + 2 years |
| Awareness training records | Evidence of AI awareness training completion | Current + 3 years |
| Tooling security assessments | CVE/vulnerability assessments for AI tooling | Current + 2 years |

---

## Audit Considerations

Auditors verifying compliance with A.4.2–A.4.6 should expect to find:

- An AI System Resource Register covering all four resource categories (data, tooling, computing, human) for each in-scope AI system
- Data resource entries with licensing, sensitivity, and provenance references
- Tooling entries with version and licence information
- Computing resource documentation with availability and security references
- Competence matrices with named individuals and assessed competence status
- Evidence of gap management where competence gaps were identified

---

<!-- QA_VERIFIED: [2026-04-15] -->
