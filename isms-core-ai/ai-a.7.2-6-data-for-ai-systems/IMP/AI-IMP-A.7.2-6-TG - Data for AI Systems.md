<!-- ISMS-CORE:IMP:AI-IMP-A.7.2-6-TG:ai:TG:a.7.2-6 -->
**AI-IMP-A.7.2-6-TG — Data for AI Systems — Technical Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Data for AI Systems — Technical Guide |
| **Document Type** | Implementation Guide (Technical) |
| **Document ID** | AI-IMP-A.7.2-6-TG |
| **Related Policy** | AI-POL-A.7.2-6 (Data for AI Systems) |
| **Document Creator** | AI Governance Officer / Data Governance Lead |
| **Document Owner** | Data Governance Lead |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **AIMS Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | Data Governance Lead | Initial technical guide for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- AI-POL-A.7.2-6 (Data for AI Systems — governing policy)
- AI-IMP-A.7.2-6-UG (Data for AI Systems — User Guide)

---

## Purpose of This Guide

This guide provides the **schemas, templates, and technical reference structures** for AI data governance — including the data acquisition record schema, data quality record schema, data provenance record schema, and data preparation documentation template.

**Audience**: Data Scientists, ML Engineers, Data Governance Lead, DPO.

---

## 1. Data Acquisition Record Schema (A.7.3)

One record per dataset acquired for AI use. Approved by Data Governance Lead.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Dataset ID | Text | M | Unique identifier (e.g., DS-2026-001) |
| Dataset Name | Text | M | Human-readable name |
| Version | Text | M | Version at acquisition |
| AI System(s) | Text | M | Which AI system(s) this dataset will be used for |
| Life cycle stage | Enum | M | Training / Validation / Testing / Operational / Multiple |
| Source Category | Enum | M | Internal / Licensed / Public / Commissioned / Web-scraped / Synthetic |
| Source Description | Text | M | Specific source: name, URL, organisation, data collection method |
| Acquisition Method | Text | M | How data was obtained: download / API / database export / direct collection / purchase |
| Legal Basis / Licence | Text | M | Licence name and version (for licensed) or GDPR Article 6 basis (for personal data) |
| Licence Restrictions | Text | C | Any restrictions on use: commercial / non-commercial; attribution required; distribution restrictions |
| Intellectual Property Status | Enum | M | Owned / Licensed / Public domain / Creative Commons / Unknown |
| Legal Review Completed | Boolean | C | Required for licensed, web-scraped, and synthetic data |
| Legal Review Reference | Text | C | Reference to Legal review record |
| Personal Data | Boolean | M | Does dataset contain personal data? |
| Personal Data — Categories | Text | C | If Yes: categories of personal data (name, email, health, financial, etc.) |
| Special Category Data | Boolean | C | If Yes: which special categories (GDPR Art. 9) |
| GDPR Legal Basis | Text | C | If personal data: Article 6 basis; Article 9 basis if special category |
| DPIA Reference | Text | C | If DPIA required and conducted |
| Data Subject Awareness | Text | C | Are data subjects aware their data may be used for AI training? |
| Scope and Coverage | Text | M | What the data represents; geographic, temporal, demographic scope |
| Coverage Limitations | Text | M | Known gaps in representation |
| Approximate Size | Text | M | Record count, token count, or file size |
| Date Acquired | Date | M | |
| Approved By | Text | M | Data Governance Lead name and date |
| Notes | Text | R | |

---

## 2. Data Quality Record Schema (A.7.4)

One quality assessment record per dataset per AI system use. Approved by Data Governance Lead.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Quality Record ID | Text | M | Unique ID |
| Dataset ID | Text | M | Reference to acquisition record |
| Dataset Version | Text | M | Version assessed |
| AI System | Text | M | AI system this quality assessment supports |
| Assessment Date | Date | M | |
| Assessed By | Text | M | Name and role |
| **Completeness** | | | |
| Completeness Threshold | Text | M | Minimum acceptable % (e.g., 95%) |
| Completeness Result | Text | M | Actual % |
| Completeness Pass? | Boolean | M | |
| **Accuracy** | | | |
| Accuracy Assessment Method | Text | M | How accuracy was assessed |
| Accuracy Threshold | Text | M | |
| Accuracy Result | Text | M | |
| Accuracy Pass? | Boolean | M | |
| **Representativeness** | | | |
| Demographic Groups Assessed | Text | M | Which demographic dimensions were analysed |
| Representativeness Findings | Text | M | Summary of coverage analysis |
| Material Underrepresentation Found? | Boolean | M | |
| Representativeness Pass? | Boolean | M | |
| **Recency** | | | |
| Temporal Range | Text | M | Date range of records |
| Recency Assessment | Text | M | Whether recency is adequate for intended use |
| Recency Pass? | Boolean | M | |
| **Consistency** | | | |
| Consistency Check Method | Text | R | |
| Consistency Findings | Text | R | |
| Consistency Pass? | Boolean | M | |
| **Freedom from Harmful Bias** | | | |
| Bias Analysis Method | Text | M | |
| Protected Characteristics Assessed | Text | M | Which characteristics were tested |
| Bias Findings | Text | M | Summary of findings |
| Material Bias Found? | Boolean | M | |
| Bias Pass? | Boolean | M | |
| **Label Quality** (supervised learning only) | | | |
| IAA Measurement Method | Text | C | Cohen's kappa / Fleiss' kappa / % agreement |
| IAA Threshold | Text | C | Minimum acceptable IAA |
| IAA Result | Text | C | |
| Label Quality Pass? | Boolean | C | |
| **Overall Gate Decision** | | | |
| Overall Pass? | Enum | M | Pass / Pass with conditions / Fail |
| Conditions (if conditional pass) | Text | C | Document accepted limitations |
| Remediation Required? | Boolean | M | |
| Remediation Plan | Text | C | If Yes: what remediation, by whom, by when |
| Risk Acceptance (if applicable) | Text | C | AI Risk Owner name and date if used with known quality limitation |
| Approved By | Text | M | Data Governance Lead name and date |

---

## 3. Data Provenance Record Schema (A.7.5)

One provenance record per dataset. Updated throughout the dataset lifecycle.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| Dataset ID | Text | M | Links to acquisition record |
| Dataset Name | Text | M | |
| Current Version | Text | M | |
| Acquisition Record Reference | Text | M | |
| **Transformation History** | | | |
| Transformation # | Integer | M | Sequential entry per transformation |
| Transformation Date | Date | M | |
| Transformation Type | Enum | M | Cleaning / Normalisation / Augmentation / Filtering / Sampling / Feature engineering / Label update / Schema change / Other |
| Transformation Description | Text | M | What was done |
| Transformation Rationale | Text | M | Why it was done |
| Applied By | Text | M | Name |
| Pipeline Reference | Text | M | Version-controlled script/pipeline reference |
| Output Dataset Version | Text | M | Version after this transformation |
| Bias Impact Assessment | Text | C | If transformation could affect fairness: assessment |
| **AI System Usage** | | | |
| AI System ID | Text | M | Per system that uses this dataset |
| AI System Version | Text | M | Specific model version |
| Usage Stage | Enum | M | Training / Validation / Testing |
| Date First Used | Date | M | |
| **Deletion Log** | | | |
| Deletion Date | Date | C | When applicable |
| Deletion Authority | Text | C | Who authorised deletion |
| Deletion Method | Text | C | Secure deletion; confirmation of completion |
| GDPR Erasure Reference | Text | C | If deletion triggered by data subject request |
| Retention Override | Text | C | If retained beyond standard period: legal hold or regulatory basis |

---

## 4. Data Preparation Documentation Template (A.7.6)

Complete one document per data preparation pipeline version. Version-controlled alongside the pipeline code.

---

```
DATA PREPARATION DOCUMENTATION
Pipeline ID: [DP-System-ID-v.X.X] | Date: [YYYY-MM-DD]
AI System: [System name and version]
Input Dataset: [Dataset ID and version]
Output Dataset (prepared): [Dataset ID and version]
Author: [ML Engineer / Data Scientist]
Reviewed By: [Data Governance Lead]

1. PRE-PROCESSING STEPS
   [For each step: name, description, parameters, rationale]
   
   Step 1: [Name]
   - Action: [What is done to the data]
   - Parameters: [Settings, thresholds, rules applied]
   - Rationale: [Why this step is needed]
   - Records affected: [Approximate count / proportion]
   - Bias consideration: [Any effect on demographic representativeness]
   
   [Repeat for each step]

2. FEATURE ENGINEERING
   [For each feature created or transformed]
   
   Feature: [Feature name]
   - Derivation: [How it is calculated from source data]
   - Rationale: [Why this feature is included]
   - Proxy variable risk: [Could this be a proxy for a protected characteristic? Assessment]
   - Excluded features: [Features considered but excluded, with rationale]

3. FILTERING CRITERIA
   [Records or samples removed from the dataset]
   
   Filter: [Description of filtering rule]
   - Criterion: [Exact rule]
   - Records removed: [Count / proportion]
   - Demographic impact: [Was the removed subset demographically unbiased?]

4. AUGMENTATION (if applicable)
   - Method: [Augmentation technique]
   - Parameters: [Settings]
   - Synthetic samples added: [Count / proportion]
   - Bias consideration: [Does augmentation maintain demographic balance?]

5. SAMPLING STRATEGY (if applicable)
   - Strategy: [e.g., stratified random sampling]
   - Stratification variables: [What variables define strata]
   - Sample sizes per stratum: [Counts]
   - Bias consideration: [Does sampling maintain representativeness?]

6. ANNOTATION GOVERNANCE (for labelled data)
   - Annotation guidelines version: [Reference]
   - Annotator count: [Number]
   - Annotator qualifications: [Relevant expertise]
   - IAA result: [κ or % agreement]
   - Label quality issues found: [Any systematic labelling problems]
   - Remediation applied: [If labels were corrected]

7. PIPELINE VERSION REFERENCE
   - Git repository: [URL/path]
   - Commit hash: [Full commit hash of pipeline code]
   - Docker image (if applicable): [Image name and digest]

8. KNOWN LIMITATIONS
   [Any preparation decisions that introduce limitations to be noted in the model card]
```

---

<!-- QA_VERIFIED: [2026-04-15] -->
