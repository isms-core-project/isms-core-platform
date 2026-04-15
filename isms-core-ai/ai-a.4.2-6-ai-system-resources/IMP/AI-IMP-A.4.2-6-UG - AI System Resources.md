<!-- ISMS-CORE:IMP:AI-IMP-A.4.2-6-UG:ai:UG:a.4.2-6 -->
**AI-IMP-A.4.2-6-UG — AI System Resources — User Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI System Resources — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | AI-IMP-A.4.2-6-UG |
| **Related Policy** | AI-POL-A.4.2-6 (AI System Resources) |
| **Document Creator** | AI Governance Officer |
| **Document Owner** | AI Governance Officer |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **AIMS Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | AI Governance Officer | Initial user guide for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- AI-POL-A.4.2-6 (AI System Resources — governing policy)
- AI-IMP-A.4.2-6-TG (AI System Resources — Technical Guide)
- AI-POL-A.5.2-5 (AISIA — references Resource Register)
- AI-POL-A.7.2-6 (Data for AI Systems — data resources)
- ISO/IEC 42001:2023 Controls A.4.2, A.4.3, A.4.4, A.4.5, A.4.6

---

## Purpose of This Guide

This guide explains **how to document, maintain, and manage the resources used in [Organisation]'s AI systems** — including computing infrastructure, data resources, tooling, and human competencies. It is the practical companion to AI-POL-A.4.2-6.

**Who this guide is for**: AI System Owners, AI Governance Officer, IT/infrastructure teams, ML Engineers, Data Governance Lead.

---

## Part 1 — The AI System Resource Register

### 1.1 Why the Register Matters

The AI System Resource Register (the Register) is the master record of all in-scope AI systems and their associated resources. It is the starting point for:
- AISIA assessments (who is affected by which system)
- Supplier management (which third parties provide AI components)
- Incident response (which systems are affected and how)
- Audit evidence (does [Organisation] know what AI systems it operates?)

Without a current Register, AI governance is blind. Keeping it current is a non-negotiable obligation for every AI System Owner.

### 1.2 What Goes Into the Register

The Register has five resource categories per AI system. The Technical Guide (AI-IMP-A.4.2-6-TG) provides the full field schema. At a minimum, each AI System Owner must document:

**The AI system itself**:
- System name, unique identifier, version
- Purpose and output type
- AI System Owner (named person)
- AI Risk Owner (named person)
- AISIA reference (document ID and current status)
- Impact classification (from AISIA)
- Operational status (pre-deployment / deployed / decommissioning)

**Computing resources**:
- Infrastructure where the system runs (on-premises server, cloud provider/region, third-party API)
- Significant compute dependencies (GPUs, TPUs, specialised hardware)

**Data resources**:
- Training datasets (name, source, version — link to full record in AI-POL-A.7.2-6 records)
- Operational data inputs (what data is fed to the system at inference time)

**Tooling**:
- Development tools (IDE, MLOps platforms, annotation tools, model registries)
- Third-party AI components used (foundation models, AI APIs, pre-trained models)
- ISMS-relevant tools (monitoring, logging, access management)

**Human resources**:
- Key competency requirements for operating this system
- Training status for current operators

### 1.3 Maintaining Register Currency

| Trigger | Required Action | Who Acts |
|---------|----------------|---------|
| New AI system entering AIMS scope | Add new Register entry before deployment gate | AI System Owner |
| Material change to existing AI system | Update relevant Register fields; flag AISIA review | AI System Owner |
| System decommissioned | Update status to Decommissioned; record decommission date; retain per retention policy | AI System Owner |
| Third-party component changes (new API version, foundation model update) | Update supplier/component fields; assess AISIA impact | AI System Owner |
| AI System Owner changes | Update named owner; AI Governance Officer verifies continuity | AI Governance Officer |
| Annual confirmation | Review all Register entries; confirm or update each field | AI System Owner + AI Governance Officer |

The AI Governance Officer conducts an annual Register validation — reviewing all entries against the actual deployed AI system portfolio to identify gaps, stale entries, or undocumented systems.

---

## Part 2 — Computing Resources

### 2.1 Documenting Computing Infrastructure

For each AI system, the AI System Owner documents:
- Where the system runs (infrastructure classification)
- What the compute requirements are (approximate — enabling BIA and continuity planning)
- What the single-vendor dependencies are

**Infrastructure classification**:

| Classification | Examples |
|---------------|---------|
| On-premises | Company-owned server, internal data centre |
| Private cloud | Dedicated cloud environment managed by [Organisation] |
| Public cloud | AWS, Azure, GCP — note: provider, region, service type |
| Third-party hosted | Vendor-managed SaaS AI platform (e.g., OpenAI API, AWS Bedrock, Azure OpenAI) |
| Hybrid | Combination of the above |

### 2.2 Third-Party AI API Dependencies

Where an AI system relies on a third-party AI API (e.g., a foundation model API), this creates a supply chain dependency:
- Document the dependency in the Register (vendor, service name, version/model, tier)
- Assess single-vendor risk: what happens if the API is unavailable?
- Ensure the supplier is assessed per AI-POL-A.10.2-4 (A.10.3 supplier management)
- Ensure the contract includes incident notification obligations

---

## Part 3 — Data Resources

### 3.1 Linking to Data Governance Records

The Register contains a summary reference to data resources. The full data governance records are maintained per AI-POL-A.7.2-6 (Data for AI Systems). For each AI system, document in the Register:
- Dataset name and version (training data)
- Source category (internal / licensed / public / synthetic)
- Data governance record reference (full record in A.7.2-6 records)
- Personal data flag (Yes / No / Partial)
- Applicable legal basis if personal data (GDPR Article 6 / Article 9)

### 3.2 What AI System Owners Must Not Do

- Do not allow new datasets to be used in an AI system without a documented acquisition record (AI-POL-A.7.2-6)
- Do not allow personal data to be fed into an AI system without documented legal basis
- Do not allow third-party data with unknown provenance or disputed IP rights

---

## Part 4 — Tooling

### 4.1 AI-Specific Tooling Categories

Document the following tooling categories in the Register:

| Tooling Category | What to Record | Why It Matters |
|-----------------|---------------|---------------|
| **Development environment** | IDEs, Jupyter/notebook platforms, version control system | Code provenance and reproducibility |
| **MLOps platform** | Training orchestration, experiment tracking, model registry | Model lineage and deployment control |
| **Data annotation tools** | Platform and version used for labelling | Label quality and annotator governance |
| **Foundation model access** | Which foundation model(s), provider, API version | Supply chain dependency |
| **Monitoring tools** | Platform monitoring AI system performance in production | Incident detection capability |
| **Logging infrastructure** | What logs are collected, stored where, retention | Audit trail and incident response |

### 4.2 Open-Source Components

Where AI systems use open-source models or libraries:
- Record the name, version, and licence
- Note: open-source components may have their own usage restrictions (e.g., AGPL, CC BY-NC)
- Ensure Legal has reviewed licence implications before use in commercial or customer-facing AI systems

---

## Part 5 — Human Resources and Competencies

### 5.1 Documenting Competency Requirements

For each AI system, the AI System Owner documents what competencies are required to operate the system responsibly. This is not a training tracker — it is the competency specification that feeds the training process.

| Competency Dimension | What to Document |
|--------------------|-----------------|
| AI domain knowledge | What understanding of the AI system's technology does an operator need? |
| Domain expertise | What subject matter expertise is required to validate AI outputs? |
| AIMS governance | What AIMS policies does the operator need to know? |
| Tool access | What tools must the operator be trained on? |
| Human oversight | What specific oversight actions must the operator perform? |

### 5.2 Competency Gaps

If a material competency gap is identified (e.g., operators using the system lack required training), the AI System Owner escalates to the AI Governance Officer. A competency gap does not require suspension of the AI system unless the gap poses a safety or compliance risk — but it does require a remediation plan.

---

<!-- QA_VERIFIED: [2026-04-15] -->
