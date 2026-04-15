<!-- ISMS-CORE:POLICY:AI-POL-A.7.2-6:ai:POL:a.7.2-6 -->
**AI-POL-A.7.2-6 — Data for AI Systems**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Data for AI Systems |
| **Document Type** | Policy |
| **Document ID** | AI-POL-A.7.2-6 |
| **Document Creator** | AI Governance Officer / Data Governance Lead |
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
| 1.0 | [Date to be set] | AI Governance Officer / Data Governance Lead | Initial policy for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual (or upon significant change to AI data practices or applicable data regulations)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: AI Governance Officer
- Secondary: Data Governance Lead / Chief Data Officer
- Compliance: Legal / Data Protection Officer (DPO)
- Final Authority: Executive Management

**Related Documents**:

- AI-POL-00 (AIMS Regulatory Applicability Framework)
- AI-POL-A.4.2-6 (AI System Resources — data resource documentation)
- AI-POL-A.6.2 (AI System Lifecycle — data used in development and operation)
- AI-IMP-A.7.2-6-UG (Data for AI Systems — User Guide)
- AI-IMP-A.7.2-6-TG (Data for AI Systems — Technical Guide)
- PRIV-POL-00 (Privacy Regulatory Applicability — for AI data containing personal data)
- ISO/IEC 42001:2023 Controls A.7.2, A.7.3, A.7.4, A.7.5, A.7.6
- ISO/IEC 42001:2023 Annex B.7 (Implementation guidance — Data for AI systems)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for managing data throughout the AI system life cycle — covering data management processes, data acquisition and selection, data quality, data provenance, and data preparation — in accordance with ISO/IEC 42001:2023 Controls A.7.2 through A.7.6.

**Scope**: All data used in the development, training, validation, testing, and operation of AI systems within the AIMS scope.

**Privacy note**: Where AI data contains or is derived from personal data, this policy operates in conjunction with PRIV-POL-00 and the PIMS control suite. GDPR Article 5 (data minimisation, purpose limitation) and Article 25 (data protection by design) apply in addition to the requirements in this policy.

**Purpose**: Define WHAT data governance requirements apply to AI systems, WHO is responsible, and WHEN data governance processes must be applied. Implementation in AI-IMP-A.7.2-6-UG and AI-IMP-A.7.2-6-TG.

**Combined Control Rationale**: A.7.2 through A.7.6 form the data governance framework for AI. Data management (A.7.2) sets the overarching process requirements; acquisition (A.7.3) governs how data enters the AI pipeline; quality (A.7.4) sets the standards data must meet; provenance (A.7.5) ensures the origin and rights of data are tracked; preparation (A.7.6) governs how raw data is processed into model-ready form.

---

## Scope and Applicability

### ISO/IEC 42001:2023 Control Statements

**Control A.7.2 — Data for development and enhancement of AI system**
The organisation shall define, document and implement data management processes related to the development of AI systems.

**Control A.7.3 — Acquisition of data**
The organisation shall determine and document details about the acquisition and selection of the data used in AI systems.

**Control A.7.4 — Quality of data for AI systems**
The organisation shall define and document requirements for data quality and ensure that data used to develop and operate the AI system meet those requirements.

**Control A.7.5 — Data provenance**
The organisation shall define and document a process for recording the provenance of data used in its AI systems over the life cycles of the data and the AI system.

**Control A.7.6 — Data preparation**
The organisation shall define and document its criteria for selecting data preparations and the data preparation methods to be used.

### Regulatory Framework

**Tier 1: Mandatory Compliance** (per AI-POL-00):

- **EU AI Act (Regulation 2024/1689)**: Article 10 — data governance requirements for high-risk AI training data (quality criteria, representativeness, freedom from errors and biases, data governance practices); Article 11 — technical documentation must include training data description
- **GDPR**: Article 5 (purpose limitation, data minimisation for AI training data containing personal data); Article 25 (data protection by design); Article 35 (DPIA where AI data processing poses high risk)

**Tier 2: Conditional** (per AI-POL-00):

- **ISO/IEC 42001:2023**: Controls A.7.2–A.7.6 — applies where AIMS certification is in scope or contractually required

---

## Policy Statements: Data Management Processes (A.7.2)

### Data Management Framework Requirement

[Organisation] SHALL define, document, and implement data management processes that govern all data used in AI system development and enhancement. These processes shall be integrated into the AI development life cycle (AI-POL-A.6.2) and shall address the full data lifecycle from acquisition through deletion.

### AI Data Lifecycle Governance

Data management processes shall address each stage of the data lifecycle:

| Stage | Governance Requirement |
|-------|----------------------|
| **Acquisition** | Documented acquisition criteria and approval process (A.7.3) |
| **Ingestion** | Version-controlled intake with provenance recording (A.7.5) |
| **Quality assessment** | Quality criteria applied before use (A.7.4) |
| **Preparation** | Documented preparation methodology (A.7.6) |
| **Storage** | Access controls, encryption, backup per ISMS |
| **Use in training / validation / operation** | Version linking — which dataset version was used in which model version |
| **Update / re-training** | Trigger criteria for dataset updates and re-training |
| **Archival** | What to retain, for how long, and in what format |
| **Deletion** | Secure deletion criteria and process; link to PRIV-POL-00 where personal data involved |

---

## Policy Statements: Data Acquisition and Selection (A.7.3)

### Data Acquisition Requirement

[Organisation] SHALL determine and document the details of data acquisition and selection for each AI system. No data shall enter the AI development pipeline without documented acquisition approval.

### Data Acquisition Documentation

For each dataset acquired for AI use:

| Field | Content Required |
|-------|----------------|
| Dataset identifier | Unique name and version |
| Source | Origin of data (internal system, public dataset, licensed dataset, commissioned collection, web scrape, other) |
| Acquisition method | How data was obtained |
| Legal basis / licence | Licence under which data is used; ownership confirmation; for personal data: legal basis under GDPR |
| Intended use | Which AI system(s) and life cycle stage(s) the data is intended for |
| Scope and coverage | What the data represents; what it does not represent |
| Date acquired | When data was obtained |
| Responsible approver | Data Governance Lead approval for acquisition |

### Prohibited Data Sources

The following shall NOT be used as AI training or operational data without explicit documented approval from the AI Governance Officer and Legal:

- Data obtained through web scraping where the website terms of service prohibit such use
- Data containing personal data without a documented legal basis under GDPR
- Synthetic data where the generation method introduces systematic bias without documented mitigation
- Data where intellectual property rights are unclear or disputed
- Data where the provenance cannot be established

---

## Policy Statements: Data Quality (A.7.4)

### Data Quality Requirement

[Organisation] SHALL define and document data quality requirements for each AI system and shall verify that data meets those requirements before use in training, validation, or operation.

### Data Quality Dimensions

Quality criteria shall be defined along the following dimensions for each dataset:

| Dimension | Definition | Assessment Method |
|-----------|-----------|------------------|
| **Completeness** | What proportion of required fields or records are present | Statistical completeness check |
| **Accuracy** | Degree to which data correctly represents the real-world entity it describes | Sampling and validation against ground truth |
| **Representativeness** | Degree to which data represents the deployment population across relevant demographic dimensions | Distribution analysis; demographic coverage assessment |
| **Recency** | Data is sufficiently recent for the use case; temporal drift is assessed | Temporal distribution analysis |
| **Consistency** | Data is consistent across sources and over time | Cross-source validation; consistency checks |
| **Freedom from harmful bias** | Data does not contain systematic biases that would produce unfair AI outputs | Bias analysis across protected characteristics |
| **Label quality** (for supervised learning) | Labels are accurate, consistent, and produced by qualified annotators | Inter-annotator agreement; label audit |

### Quality Gate

Each dataset shall be assessed against its defined quality criteria before use. Datasets that do not meet minimum quality thresholds shall:

1. Be rejected for use, OR
2. Be remediated (additional data collection, cleaning, augmentation) with the remediation documented, OR
3. Be used with documented risk acceptance from the AI Risk Owner, with known quality limitations noted in the model card

No dataset shall be used in an AI system without documented quality assessment results.

---

## Policy Statements: Data Provenance (A.7.5)

### Data Provenance Requirement

[Organisation] SHALL define and implement a process for recording and maintaining the provenance of all data used in AI systems throughout the life cycles of both the data and the AI system.

### Provenance Record Requirements

A data provenance record shall be maintained for each dataset, tracking:

| Element | Content |
|---------|---------|
| Dataset identifier and version | Unique reference |
| Original source | Where data originated (with reference to acquisition record) |
| Transformation history | All cleaning, normalisation, augmentation, or other transformations applied — with dates and responsible party |
| Derived datasets | If this dataset was derived from another, link to parent provenance record |
| AI systems using this dataset | Which AI systems (and model versions) have used this dataset |
| Retention and deletion log | When data was archived or deleted, and under what authority |

### Version Linking

The provenance system shall enable traceability: given any deployed AI model version, it shall be possible to identify the exact dataset version(s) used in training and validation. This traceability is required for:

- Audit and certification evidence
- Incident investigation (determining if a data issue contributed to an AI incident)
- Regulatory compliance (EU AI Act Article 11 technical documentation)
- Right to erasure compliance (GDPR Article 17 — identifying which models were trained on data subject to an erasure request)

### GDPR Article 17 — Right to Erasure for AI Training Data

Where a data subject submits a valid erasure request under GDPR Article 17, [Organisation] SHALL:

1. **Delete the source training data record immediately** — remove the individual's data from all training datasets, validation sets, and associated data stores without undue delay.
2. **Assess residual risk in model weights** — using provenance traceability, identify all AI model versions trained on the data. Document a technical assessment of whether the individual's data is recoverable from or attributable to trained model weights. For standard neural network architectures, full erasure from weights is generally technically infeasible; this infeasibility shall be documented.
3. **Respond to the data subject** — acknowledge the erasure request, confirm deletion of source data, and where full erasure from model weights is technically infeasible, document this limitation and the residual risk assessment per applicable DPA guidance.
4. **Trigger model retraining or retirement** — where the residual risk assessment identifies significant likelihood of individual identifiability from model outputs (e.g., the model was trained on a small dataset, or the individual is a distinctive data point), the AI System Owner shall assess whether model retraining or retirement is required. The DPO shall advise on the risk threshold for this determination.
5. **Log all erasure actions** — record the request, the source data deletion confirmation, the model assessment, and any retraining decision in the AI Data Governance Register. Retain records for 5 years.

Where [Organisation] uses differential privacy techniques at training time, this shall be documented in the AISIA and referenced in erasure responses as a risk mitigant.

---

## Policy Statements: Data Preparation (A.7.6)

### Data Preparation Requirement

[Organisation] SHALL define and document criteria for selecting data preparation approaches and the methods to be used. Data preparation decisions shall be documented and reproducible.

### Data Preparation Governance

Data preparation — the process of transforming raw data into a form suitable for AI model training or operation — shall be:

**Documented**: Each preparation pipeline shall be documented including:
- Pre-processing steps applied (normalisation, encoding, imputation, tokenisation, etc.)
- Feature engineering decisions with rationale
- Filtering criteria (records excluded and why)
- Augmentation methods applied (and their parameters)
- Sampling strategy where data volumes require sampling

**Version controlled**: Data preparation scripts and pipelines shall be version-controlled alongside model code, enabling reproduction of the exact prepared dataset from the raw source.

**Bias-aware**: Data preparation decisions shall be reviewed for their potential to introduce or amplify bias. Steps that could disproportionately affect underrepresented groups (e.g., under-sampling, imputation strategies) shall be documented with rationale and bias impact assessment.

**Annotator governance** (for labelled data):

- Annotation guidelines shall be documented
- Annotator qualifications documented
- Inter-annotator agreement measured and documented
- Label quality below acceptable thresholds triggers re-annotation

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|----------------|
| **AI Governance Officer** | Own the AI data governance policy; approve data acquisition for high-sensitivity datasets; review data quality issues escalated by Data Governance Lead |
| **Data Governance Lead** | Own and operate A.7.x processes day-to-day; approve standard data acquisitions; maintain provenance records; chair data quality gates |
| **DPO / Privacy Officer** | Review AI data involving personal data; ensure GDPR compliance for training data; advise on right-to-erasure implications |
| **Data Scientists / ML Engineers** | Conduct data quality assessments; document preparation pipelines; flag quality issues to Data Governance Lead |
| **AI System Owner** | Ensure data governance records are current for owned AI systems |

---

## Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Data acquisition records | Per-dataset acquisition documentation with legal basis and approval | Duration of dataset use + 5 years |
| Data quality assessment records | Per-dataset quality assessment results against defined criteria | Duration of dataset use + 3 years |
| Data provenance records | Transformation history and version-linking records | Duration of AI system + 5 years post-decommission |
| Data preparation documentation | Pipeline documentation with version-controlled code reference | Duration of AI system + 3 years |
| Quality gate outcomes | Records of quality gate pass/fail decisions with approval | Duration of AI system + 3 years |

---

## Audit Considerations

Auditors verifying compliance with A.7.2–A.7.6 should expect to find:

- Documented data management processes covering the full data lifecycle
- Acquisition records for all datasets used in in-scope AI systems
- Data quality criteria defined per AI system and quality assessment records confirming criteria are met
- Data provenance records enabling traceability from deployed model to training dataset
- Data preparation pipelines documented and version-controlled
- Evidence that data quality gates are applied before datasets enter production use

---

<!-- QA_VERIFIED: [2026-04-15] -->
