<!-- ISMS-CORE:IMP:AI-IMP-A.6.1-TG:ai:TG:a.6.1 -->
**AI-IMP-A.6.1-TG — AI Development Governance — Technical Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI Development Governance — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | AI-IMP-A.6.1-TG |
| **Related Policy** | AI-POL-A.6.1 (AI Development Governance) |
| **Document Creator** | AI Governance Officer / Chief Technology Officer |
| **Document Owner** | AI Governance Officer |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **AIMS Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | AI Governance Officer | Initial technical guide for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- AI-POL-A.6.1 (AI Development Governance — governing policy)
- AI-IMP-A.6.1-UG (AI Development Governance — User Guide)

---

## Purpose of This Guide

This guide provides the **technical structures, schemas, and reference configurations** for AI development governance — including the V&V record schema, model card template, development governance checklist, and fairness metric reference.

**Audience**: ML Engineers, Data Scientists, AI System Owners, Quality/Compliance.

---

## 1. V&V Record Schema

One V&V record per AI system version. Required before deployment gate clearance.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| V&V Record ID | Text | M | e.g., VVR-AI-SYS-001-v1.0 |
| AI System ID | Text | M | Reference to AI System Resource Register |
| AI System Version | Text | M | Version being validated |
| V&V Date(s) | Date | M | Date(s) validation was conducted |
| Lead Assessor | Text | M | Name and role |
| Independent Reviewer | Text | C | Required for High-impact systems |
| Evaluation Dataset | Text | M | Dataset name and version (must be held-out — not used in training) |
| Dataset Size | Text | M | Number of records/samples in evaluation set |
| Primary Metric | Text | M | e.g., F1-score, AUC-ROC, BLEU, Human evaluation score |
| Primary Metric — Pass Threshold | Text | M | Pre-defined threshold |
| Primary Metric — Result | Text | M | Actual result |
| Primary Metric — Pass? | Boolean | M | |
| Secondary Metrics | Text | R | Additional metrics with thresholds and results |
| Fairness Evaluation | Text | M | Summary of fairness evaluation (see section 3 for full schema) |
| Fairness Evaluation — Pass? | Boolean | M | |
| Adversarial Testing | Text | C | Required for Medium+ impact; summary of adversarial/edge case tests |
| Known Limitations | Text | M | Conditions under which performance degrades |
| Deployment Conditions | Text | C | Any conditions that must be met at deployment (e.g., specific input validation, human review threshold) |
| Overall Pass / Fail | Enum | M | Pass / Pass with conditions / Fail |
| Rationale | Text | M | Written justification for Pass/Fail decision |
| AI System Owner Sign-off | Text | M | Name and date |
| AI Governance Officer Reviewed? | Boolean | C | Required for High-impact systems |
| Version History | Text | R | Prior V&V record references for this system |

---

## 2. Model Card Template

A model card is a concise summary document for each AI system version — the technical record made available to operators, oversight teams, and (where appropriate) external parties. Based on Mitchell et al. (2019) model card concept, aligned to ISO 42001:2023 control A.6.2.7 (technical documentation).

---

```
MODEL CARD
AI System: [System Name] | Version: [X.X] | Date: [YYYY-MM-DD]

## System Overview
[2–3 sentences describing what the system does]

## Intended Uses
- Primary: [Intended use statement]
- Authorised users: [Who may use this system]
- Out of scope: [Uses for which the model was not designed]
- Prohibited: [Uses explicitly forbidden]

## Model Type and Architecture
- Algorithm family: [e.g., Gradient boosted trees / Transformer / CNN]
- Framework: [e.g., PyTorch 2.1 / scikit-learn 1.3 / TensorFlow 2.14]
- Model size: [Parameters / nodes — or "N/A" for rule-based components]
- Foundation model (if applicable): [Provider, model name, version]

## Training Data
- Datasets: [Names and versions]
- Size: [Approximate records/tokens]
- Date range: [Temporal coverage]
- Geographic coverage: [If relevant]
- Personal data: [Yes/No — legal basis if Yes]
- Known coverage limitations: [What populations or contexts are underrepresented]

## Performance
| Metric | Value | Dataset | Notes |
|--------|-------|---------|-------|
| [Primary metric] | [Value] | [Dataset name/version] | |
| [Metric by group: Group A] | [Value] | | |
| [Metric by group: Group B] | [Value] | | |

## Fairness Evaluation
[Summary of fairness testing — which groups evaluated; key findings; any known disparities]

## Limitations and Known Failure Modes
1. [Limitation 1 — condition and impact]
2. [Limitation 2]
3. [Edge case behaviour]

## Human Oversight Requirements
[How human review is required; what the human reviewer must do; when AI outputs must not be acted upon without review]

## Ethical Considerations
[Any ethical dimensions identified in the AISIA — concise summary]

## References
- AISIA: [Document ID and version]
- V&V Record: [Document ID]
- Data records: [Data governance record references]

Model Card Version: [X.X] | Prepared by: [AI System Owner] | Date: [YYYY-MM-DD]
```

---

## 3. Fairness Metric Reference

The following metrics are used in fairness evaluations. Not all metrics apply to all system types — selection should be based on the system's output type and the impact classification.

| Metric | Definition | System Type | When to Use |
|--------|-----------|-------------|-------------|
| **Demographic parity** | P(Ŷ=1\|A=a) = P(Ŷ=1\|A=b) — positive outcome rate is equal across groups | Binary classification | When equal treatment (not equal accuracy) is the fairness goal |
| **Equalised odds** | Equal TPR and FPR across groups | Binary classification | When both false positives and false negatives have significant consequences |
| **Equal opportunity** | Equal TPR (true positive rate) across groups | Binary classification | When false negatives are the primary harm (e.g., screening systems where false rejection is harmful) |
| **Predictive parity** | Equal PPV (precision) across groups | Binary classification | When positive predictions should be equally reliable regardless of group |
| **Individual fairness** | Similar individuals receive similar outputs | Any | Spot-check: sample comparable individuals from different groups; compare outputs |
| **Counterfactual fairness** | Would the outcome change if the individual belonged to a different group? | Any | For high-impact systems; typically requires feature sensitivity analysis |
| **Group calibration** | Calibration curves are consistent across groups | Probabilistic output | When the system outputs probabilities used for decision-making |

**Practical guidance**: For most systems, start with demographic parity and equal opportunity. Document which metrics were used and why others were not applicable.

---

## 4. Development Governance Checklist

Complete at each major development milestone. Different sections are triggered at different lifecycle stages.

### At Design Stage
| Item | Complete |
|------|----------|
| Intended use statement drafted | ☐ |
| Affected populations identified | ☐ |
| Preliminary AISIA initiated | ☐ |
| Fairness requirements defined | ☐ |
| Privacy requirements assessed (DPO consulted if personal data) | ☐ |
| Explainability approach selected | ☐ |
| Human oversight mechanism designed | ☐ |
| Fail-safe and fallback behaviour defined | ☐ |

### At Data Stage
| Item | Complete |
|------|----------|
| Data acquisition records created (AI-POL-A.7.2-6) | ☐ |
| Data quality criteria defined | ☐ |
| Data quality assessment completed | ☐ |
| Demographic coverage assessment completed | ☐ |
| Bias in training data assessed | ☐ |
| DPO consulted (if personal data) | ☐ |
| Data provenance records created | ☐ |
| Training / validation / test split documented (no leakage) | ☐ |

### At Model Development Stage
| Item | Complete |
|------|----------|
| Proxy variable audit completed | ☐ |
| Fairness constraints implemented | ☐ |
| Model version controlled in model registry | ☐ |
| Experiment tracking active | ☐ |

### At V&V Stage
| Item | Complete |
|------|----------|
| V&V pass/fail criteria defined before evaluation | ☐ |
| Evaluation on held-out dataset (not training data) | ☐ |
| Stratified evaluation by demographic group | ☐ |
| Adversarial / edge case testing completed | ☐ |
| V&V record completed and signed | ☐ |
| Model card drafted | ☐ |

### At Deployment Gate
| Item | Complete |
|------|----------|
| Final AISIA completed and approved | ☐ |
| V&V passed | ☐ |
| User documentation prepared | ☐ |
| User training completed | ☐ |
| Access controls configured | ☐ |
| Monitoring and logging active | ☐ |
| AI System Resource Register updated | ☐ |
| AI Governance Officer deployment approval | ☐ |

---

<!-- QA_VERIFIED: 2026-04-15 -->
