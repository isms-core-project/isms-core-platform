<!-- ISMS-CORE:IMP:AI-IMP-A.7.2-6-UG:ai:UG:a.7.2-6 -->
**AI-IMP-A.7.2-6-UG — Data for AI Systems — User Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Data for AI Systems — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | AI-IMP-A.7.2-6-UG |
| **Related Policy** | AI-POL-A.7.2-6 (Data for AI Systems) |
| **Document Creator** | AI Governance Officer / Data Governance Lead |
| **Document Owner** | Data Governance Lead |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **AIMS Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | Data Governance Lead | Initial user guide for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- AI-POL-A.7.2-6 (Data for AI Systems — governing policy)
- AI-IMP-A.7.2-6-TG (Data for AI Systems — Technical Guide)
- PRIV-POL-00 (Privacy Regulatory Applicability — personal data in AI)
- ISO/IEC 42001:2023 Controls A.7.2–A.7.6

---

## Purpose of This Guide

This guide explains **how to implement data governance for AI systems** — from acquiring a new dataset through quality assessment, provenance tracking, data preparation, and eventual deletion. It is the practical companion to AI-POL-A.7.2-6.

**Who this guide is for**: Data Scientists, ML Engineers, Data Governance Lead, DPO, and any person involved in sourcing, preparing, or managing data for AI systems.

---

## Part 1 — Before You Acquire Any Data

### 1.1 The Acquisition Approval Requirement

No dataset enters the AI pipeline without a documented acquisition record approved by the Data Governance Lead. This rule exists because data problems are the most common source of AI governance failures — bias, rights violations, and compliance breaches almost always start with inadequate data governance.

The acquisition record documents:
- Where the data came from
- What rights [Organisation] has to use it
- What personal data it contains
- What it will be used for

### 1.2 Dataset Source Categories and Key Risks

| Source Category | Key Risks | Minimum Actions |
|----------------|-----------|----------------|
| **Internal data** | Privacy scope creep; use beyond original purpose | Document intended use; assess GDPR purpose compatibility |
| **Licensed dataset** | Licence restrictions (commercial use, attribution, distribution); changes on renewal | Read the licence; Legal review for commercial or customer-facing AI |
| **Public dataset** | Unknown provenance; may contain personal data; web-scraped content may violate ToS | Check provenance; check licence; assess personal data risk |
| **Commissioned data collection** | Quality control; annotator bias; legal basis for data collection | Design collection protocol; include quality gates |
| **Web-scraped data** | Terms of Service compliance; copyright; personal data | Legal clearance required before use |
| **Synthetic data** | May introduce systematic bias; over-optimistic training signal | Document generation method; bias assessment |

### 1.3 Personal Data in AI Training — Key Rules

If the dataset contains or may contain personal data:
1. **Stop** and consult the DPO before proceeding
2. Document the legal basis under GDPR Article 6 (and Article 9 if special category)
3. Assess whether a DPIA is required (GDPR Article 35)
4. Data minimisation: can the same training objective be achieved with less personal data?
5. Purpose compatibility: is AI training compatible with the purpose for which data was originally collected?
6. Document right-to-erasure implications — which models were trained on which data subjects' records?

---

## Part 2 — Data Quality in Practice

### 2.1 Quality Gate Process

Every dataset used in an AI system must pass a quality gate before use. The quality gate is a documented assessment confirming that the dataset meets the quality criteria defined for the AI system.

**Who runs the quality gate**: Data Scientist / ML Engineer conducts the assessment; Data Governance Lead approves the result.

**When the gate is run**: Before the dataset is used in training, validation, or operation. Updating a dataset to a new version triggers a new gate assessment.

### 2.2 Quality Dimensions — What to Check

| Dimension | How to Assess | What Constitutes a Problem |
|-----------|--------------|--------------------------|
| **Completeness** | % of records with all required fields populated | Threshold set per dataset — e.g., <95% completeness flags for review |
| **Accuracy** | Sample-based validation against ground truth | Systematic errors in labelling or data collection |
| **Representativeness** | Distribution analysis across demographic dimensions | Under-representation of any affected demographic group that would cause bias |
| **Recency** | Temporal distribution of records | Significant concentration in historical periods that may not reflect current conditions |
| **Consistency** | Cross-source validation; duplicate check | Conflicting records from different sources; high duplicate rate |
| **Freedom from harmful bias** | Bias analysis across protected characteristics | Statistically significant outcome disparities correlated with protected characteristics |
| **Label quality** (supervised) | Inter-annotator agreement (IAA) measurement | IAA below acceptable threshold (typically κ < 0.6) |

### 2.3 When Quality Gates Fail

If a dataset fails a quality gate:
1. **Reject**: Do not use the dataset. Document the failure and reason.
2. **Remediate**: Apply defined remediation (additional collection, cleaning, re-labelling) and re-run the quality gate.
3. **Accept with risk**: If the Data Governance Lead and AI Risk Owner accept the known quality limitation, document the accepted limitation explicitly in the quality gate record and the model card.

Do not silently proceed with a failed gate. The quality gate outcome must be documented either way.

---

## Part 3 — Data Provenance in Practice

### 3.1 Why Provenance Matters

Provenance tells you: for any deployed model, exactly which data was used to train it. You need this for:
- **Audit**: An auditor asks "what data was used to train this model?" — you can answer in minutes
- **Incident investigation**: A bias incident occurs — you can trace which dataset contributed to it
- **Right to erasure (GDPR)**: A data subject requests erasure — you need to know which models were trained on their data
- **Supplier change**: Your licensed dataset provider changes terms — you need to know which models are affected

### 3.2 Maintaining Provenance Records

Provenance records are maintained by the Data Governance Lead. For each dataset:

1. **At acquisition**: Create a provenance record (see AI-IMP-A.7.2-6-TG for schema) with source, licence, and initial characteristics
2. **At each transformation**: Log the transformation (cleaning step, normalisation, augmentation, sampling) with date and responsible person
3. **At training**: Link the model version to the dataset version used — this is the critical version-linking step
4. **At deletion**: Record deletion date, authority, and method

The version-linking requirement is absolute: given any deployed model version, you must be able to identify the exact dataset version(s) used.

---

## Part 4 — Data Preparation

### 4.1 Documentation Requirements

Every data preparation pipeline must be documented before it is used in training. The pipeline documentation is a governance artefact — not just technical documentation.

**What to document**:
- Each pre-processing step with rationale
- Feature engineering decisions — what was included, what was excluded, and why
- Filtering criteria — what records were excluded and why
- Augmentation methods and parameters
- Sampling strategy

**Key principle**: A pipeline decision that cannot be explained in writing should prompt re-examination of whether it is defensible from a bias and fairness perspective.

### 4.2 Bias-Aware Data Preparation

Some common data preparation decisions that can introduce or amplify bias:

| Preparation Decision | Potential Bias Effect | Mitigation |
|---------------------|----------------------|-----------|
| **Under-sampling majority class** | May disproportionately remove records from already underrepresented groups | Stratified sampling; monitor impact by demographic group |
| **Imputation of missing values** | Imputed values may differ systematically by demographic group | Group-aware imputation; document imputation strategy |
| **Filtering records by quality threshold** | Quality issues may be correlated with demographic group | Check demographic distribution before and after filtering |
| **Feature selection** | May inadvertently remove features that enable fairness analysis later | Retain demographic variables for evaluation even if not used in model |
| **Normalisation** | Different normalisation effects for different sub-populations | Document normalisation parameters; check robustness |

---

## Part 5 — Data Lifecycle to Deletion

### 5.1 Data Retention and Deletion

Data is not retained indefinitely just because it might be useful for future training. Retention must have a documented basis:

| Data Category | Default Retention | Notes |
|--------------|------------------|-------|
| Training datasets — active system | Duration of AI system operational life | May be extended for ongoing re-training |
| Training datasets — decommissioned system | 5 years post-decommission (align with AISIA retention) | Legal hold may override |
| Operational input logs (containing personal data) | Per AI-IMP-A.6.2-TG log retention schedule | GDPR minimum — not longer than necessary |
| Data provenance records | Duration of AI system + 5 years | Required for audit and incident investigation |
| Quality gate records | Duration of AI system + 3 years | Required for audit |

### 5.2 Right to Erasure (GDPR Article 17)

When a data subject requests erasure of their personal data:
1. DPO receives the request and determines scope
2. Data Governance Lead uses provenance records to identify which datasets contain the data subject's records
3. Data Governance Lead identifies which AI models were trained on those datasets
4. Data Governance Lead and AI Governance Officer assess whether the trained models need to be retrained without the data subject's records (usually not required for well-generalised models, but documented assessment is required)
5. Source data is deleted; provenance record is updated to note the erasure
6. DPO documents the erasure response

---

<!-- QA_VERIFIED: [YYYY-MM-DD] -->
