<!-- ISMS-CORE:IMP:AI-IMP-A.5.2-5-TG:ai:TG:a.5.2-5 -->
**AI-IMP-A.5.2-5-TG — AI System Impact Assessment — AISIA Template**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI System Impact Assessment — AISIA Template |
| **Document Type** | Implementation Guide (Technical) — Fillable Template |
| **Document ID** | AI-IMP-A.5.2-5-TG |
| **Related Policy** | AI-POL-A.5.2-5 (AI System Impact Assessment) |
| **Document Creator** | AI Governance Officer |
| **Document Owner** | AI Governance Officer |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal — Restricted |
| **Status** | Draft |
| **AIMS Product Version** | 1.0 |
| **Methodology Basis** | ISO/IEC 42005:2025, Clause 6 and Annex E |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | AI Governance Officer | Initial AISIA template for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual (or upon publication of updated ISO 42005)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- AI-POL-A.5.2-5 (AI System Impact Assessment — governing policy)
- AI-IMP-A.5.2-5-UG (AI System Impact Assessment — User Guide — process instructions)
- ISO/IEC 42001:2023 Controls A.5.2–A.5.5 and Clause 6.1.4
- ISO/IEC 42005:2025 (AI system impact assessment methodology standard)

---

## How to Use This Template

This document is the **AISIA template** for [Organisation]. Each AI system within the AIMS scope requires a completed AISIA record. To create an AISIA for a specific AI system:

1. **Copy this template** — create a new document titled `AISIA — [AI System Name] — v[X.X] — [YYYY-MM-DD]`
2. **Complete all sections** — follow the guidance text in each section (shown in *italics*)
3. **Delete guidance text** from the completed AISIA before filing
4. **Obtain approval** — Section 9 must be signed by the AI Governance Officer before deployment

Refer to AI-IMP-A.5.2-5-UG for step-by-step process instructions, timing requirements, and worked examples.

**Methodology note**: This template is structured in accordance with ISO/IEC 42005:2025 Clause 6 (documentation requirements) and Annex E (example AISIA template). Field references in brackets [e.g., Ref. 6.2] indicate the ISO 42005:2025 clause that the field satisfies.

---

---

# AI SYSTEM IMPACT ASSESSMENT (AISIA)

## COMPLETED RECORD

*(Fill this header in every completed AISIA)*

| Field | Value |
|-------|-------|
| **AI System Name** | [Name of the AI system] |
| **AI System Identifier** | [Unique identifier from AI System Resource Register] |
| **AI System Version** | [Version number assessed, e.g., v1.0, v2.3] |
| **AISIA Document ID** | [AISIA-{SystemID}-v{X.X}] |
| **AISIA Version** | [1.0 for initial; increment for updates] |
| **Assessment Date** | [YYYY-MM-DD] |
| **Assessment Conducted By** | [Name, Role] |
| **AI System Owner** | [Name, Role] |
| **Classification Result** | [Low / Medium / High — completed in Section 8] |
| **Status** | [Draft / Under Review / Approved] |
| **Approved By** | [AI Governance Officer name — completed in Section 9] |
| **Approval Date** | [YYYY-MM-DD — completed in Section 9] |
| **Next Review Date** | [YYYY-MM-DD — based on classification: Low=3yr / Med=1yr / High=6mo] |

---

## Section 1 — AI System Identification [Ref. 6.2]

*Provide basic identification information about the AI system. This section establishes what system is being assessed.*

### 1.1 AI System Description

| Field | Content |
|-------|---------|
| **AI System Name** | |
| **AI System Purpose** | *What does this AI system do? What problem does it solve or what function does it perform?* |
| **AI System Type** | *Classification (e.g., ML-based / rule-based / hybrid / generative / discriminative / reinforcement learning)* |
| **Primary Output** | *What does the system produce? (prediction, recommendation, classification, generated content, decision, score, ranking, etc.)* |
| **Provider / Developer** | *Who developed this AI system? (Internal team / third-party vendor / open-source with customisation)* |
| **Deployer / Operator** | *Who deploys and operates this AI system? (Business unit, function, external customer)* |
| **Operational Status** | *Current status: Pre-deployment / In development / Deployed-operational / Decommissioning* |

### 1.2 Life Cycle Stage at Time of Assessment

*Select the life cycle stage(s) applicable to this assessment. An AISIA conducted before initial deployment covers all stages prospectively.*

| Life Cycle Stage | Applicable? | Notes |
|-----------------|-------------|-------|
| Design and specification | ☐ Yes ☐ No | |
| Development and training | ☐ Yes ☐ No | |
| Validation and testing | ☐ Yes ☐ No | |
| Deployment and integration | ☐ Yes ☐ No | |
| Operation and monitoring | ☐ Yes ☐ No | |
| Change / update | ☐ Yes ☐ No | *If update: describe what changed* |
| Decommissioning | ☐ Yes ☐ No | |

---

## Section 2 — Use Information [Ref. 6.3]

*Document the intended use, foreseeable misuse, and use constraints for this AI system.*

### 2.1 Intended Use

| Field | Content |
|-------|---------|
| **Intended use statement** | *Clear, specific description of what the AI system is for, by whom, in what context, and to what end* |
| **Intended user categories** | *Who is authorised to use the system? (Internal staff only / Customers / Partners / Public / etc.)* |
| **Intended operational context** | *The environments and conditions for which the system was designed and validated* |
| **Conditions for valid use** | *Prerequisites that must be met for outputs to be valid (input data requirements, operator qualifications, etc.)* |

### 2.2 Sensitive Uses

*Identify uses involving populations or contexts that warrant particular attention.*

| Sensitive Use Category | Applicable? | Description if applicable |
|-----------------------|-------------|--------------------------|
| Involves consequential decisions affecting individuals | ☐ Yes ☐ No | |
| Involves vulnerable populations (children, elderly, persons with disabilities, minority groups) | ☐ Yes ☐ No | |
| Involves power-asymmetric relationships (employer/employee, government/citizen, lender/borrower) | ☐ Yes ☐ No | |
| Involves personal data (especially special category data) | ☐ Yes ☐ No | |
| Involves autonomous or semi-autonomous decision-making | ☐ Yes ☐ No | |
| Involves public-facing or citizen-facing use | ☐ Yes ☐ No | |
| Involves safety-critical operations | ☐ Yes ☐ No | |

### 2.3 Out-of-Scope and Restricted Uses

| Field | Content |
|-------|---------|
| **Uses that are out of scope** | *Uses not designed or validated for — not necessarily prohibited, but not authorised* |
| **Uses that are prohibited** | *Uses explicitly forbidden — including uses that could cause harm, violate rights, or breach law* |

### 2.4 Reasonably Foreseeable Misuse

*Identify uses that could foreseeably occur even though unintended. These are addressed in detail in Section 8.2.*

*List 2–5 reasonably foreseeable misuse scenarios for this AI system:*

| # | Misuse Scenario Description |
|---|---------------------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |

---

## Section 3 — Technical Information [Ref. 6.4]

*Document technical characteristics of the AI system sufficient to support impact analysis.*

### 3.1 AI Technology Description

| Field | Content |
|-------|---------|
| **Algorithm / Model Type** | *e.g., Large language model (transformer), gradient boosting, CNN, random forest, rule-based + ML hybrid, etc.* |
| **Learning paradigm** | *Supervised / Unsupervised / Semi-supervised / Reinforcement learning / Foundation model / Fine-tuned foundation model* |
| **Key model components** | *Describe major components if applicable (e.g., retrieval system + LLM + re-ranker)* |
| **Human-in-the-loop design** | *Is human review integrated into the system design? Where and how?* |
| **Explainability mechanisms** | *What mechanisms exist to explain AI outputs? (SHAP, LIME, attention weights, natural language explanation, none, etc.)* |

### 3.2 Training Data

| Field | Content |
|-------|---------|
| **Training data sources** | *Origin of training data (internal / licensed / public / synthetic / combination)* |
| **Training data volume** | *Approximate size (records, tokens, etc.)* |
| **Training data coverage** | *What populations, contexts, and time periods does the training data represent?* |
| **Known data limitations** | *Known gaps, biases, or coverage limitations in training data* |
| **Personal data in training** | ☐ Yes ☐ No — *If yes: categories of personal data; legal basis; reference to DPIA if applicable* |
| **Data governance reference** | *Reference to data acquisition and quality records (AI-POL-A.7.2-6)* |

### 3.3 Operational Data

| Field | Content |
|-------|---------|
| **Operational data inputs** | *What data does the system receive at inference/runtime?* |
| **Personal data at runtime** | ☐ Yes ☐ No — *If yes: categories; retention; processing basis* |
| **Data source validation** | *How is input data validated before the AI system processes it?* |
| **Data storage and logging** | *What data is stored during operation? For how long?* |

### 3.4 Performance and Validation

| Field | Content |
|-------|---------|
| **Primary performance metrics** | *Key metrics used to evaluate the system (accuracy, F1, AUC, precision/recall, BLEU, etc.) with current values* |
| **Validation approach** | *How was the model validated? (Held-out test set, k-fold CV, A/B test, adversarial testing, human evaluation, etc.)* |
| **Known performance limitations** | *Conditions under which performance degrades; edge cases; failure modes identified in testing* |
| **Fairness analysis results** | *Was the model tested for performance disparities across demographic groups? If yes: results and findings* |
| **Validation record reference** | *Reference to formal V&V documentation* |

### 3.5 Monitoring

| Field | Content |
|-------|---------|
| **Monitoring approach** | *What is monitored in operation? (Output quality, drift, error rates, usage patterns, etc.)* |
| **Alerting thresholds** | *What triggers a human review or system pause?* |
| **Incident detection** | *How are AI incidents or unexpected output patterns detected?* |
| **Logging** | *What is logged? Retention period?* |

---

## Section 4 — Deployment Environment [Ref. 6.5]

*Describe the context in which the AI system is deployed and operated.*

| Field | Content |
|-------|---------|
| **Deployment model** | *Internal tool / Customer-facing SaaS / API / Embedded in product / Third-party hosted / Edge deployment* |
| **Infrastructure** | *Where is the system hosted? (On-premises, cloud, hybrid — provider and region if applicable)* |
| **Integration points** | *What other systems does this AI system connect to or receive data from?* |
| **User interface** | *How do users interact with the AI system? (Web UI, API, chat interface, embedded in workflow, etc.)* |
| **Operational scale** | *How many users / how many AI-driven decisions / transactions per day, week, month?* |
| **Geographic deployment** | *Where is the system deployed? Which jurisdictions?* |
| **Third-party dependency** | *Is the system dependent on any third-party AI components (foundation models, APIs)? Identify them.* |
| **Operator training requirement** | *What training is required for staff who operate or use the AI system?* |

---

## Section 5 — EU AI Act Classification [Ref. AI-POL-00]

*Complete this section for all AI systems. Determines regulatory obligations that apply.*

| Field | Content |
|-------|---------|
| **[Organisation]'s role** | *Provider / Deployer / Both* |
| **AI Act risk category** | *Unacceptable risk (prohibited) / High-risk (Annex III) / Limited-risk / Minimal-risk / GPAI model / Not determined* |
| **Annex III category if high-risk** | *Specify which Annex III category applies, if applicable* |
| **Conformity assessment** | *If high-risk: is a conformity assessment required? Status?* |
| **FRIA required** | ☐ Yes ☐ No ☐ Not applicable — *EU AI Act Article 26 FRIA trigger: deployers of certain high-risk systems in specific sectors* |
| **FRIA reference** | *If FRIA required or conducted: reference to FRIA document* |
| **DPIA required** | ☐ Yes ☐ No ☐ Not applicable — *GDPR Article 35: AI processing personal data likely to result in high risk* |
| **DPIA reference** | *If DPIA required or conducted: reference to DPIA document* |

---

## Section 6 — Relevant Interested Parties [Ref. 6.6]

*Identify all categories of parties whose interests could be affected by this AI system. Complete all sub-sections.*

### 6.1 Internal Interested Parties

*Identify parties within [Organisation] whose interests are affected by the AI system.*

| # | Interested Party Category | Description | Their relationship to AI outputs |
|---|--------------------------|-------------|----------------------------------|
| 1 | *e.g., Operational users (staff directly using the system)* | | |
| 2 | *e.g., Decision-makers relying on AI outputs* | | |
| 3 | *e.g., Staff whose work or performance is assessed by AI* | | |
| 4 | *e.g., Management receiving AI-generated reports* | | |
| 5 | *Add rows as needed* | | |

### 6.2 External Users

*Identify external parties who directly use the AI system (e.g., customers, partners, public users).*

| # | Interested Party Category | Description | Their relationship to AI outputs |
|---|--------------------------|-------------|----------------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### 6.3 Affected Individuals

*Identify individuals who are NOT direct users but whose interests are affected by AI outputs. This is often the most critical section — the people subject to AI-driven decisions.*

| # | Affected Individual Category | Description | How AI affects them | Aware of AI use? | Recourse available? |
|---|-----------------------------|-----------|--------------------|-----------------|---------------------|
| 1 | | | | ☐ Yes ☐ No ☐ Partial | ☐ Yes ☐ No |
| 2 | | | | ☐ Yes ☐ No ☐ Partial | ☐ Yes ☐ No |
| 3 | | | | ☐ Yes ☐ No ☐ Partial | ☐ Yes ☐ No |

### 6.4 Vulnerable Groups

*Identify any affected parties in a vulnerable category. Vulnerability increases the potential severity of harm.*

| # | Vulnerable Group Category | Present in the affected population? | Additional considerations |
|---|--------------------------|-------------------------------------|--------------------------|
| 1 | Children (under 18) | ☐ Yes ☐ No ☐ Unknown | |
| 2 | Elderly individuals | ☐ Yes ☐ No ☐ Unknown | |
| 3 | Persons with disabilities | ☐ Yes ☐ No ☐ Unknown | |
| 4 | Minority ethnic or religious groups | ☐ Yes ☐ No ☐ Unknown | |
| 5 | Individuals in power-asymmetric relationships | ☐ Yes ☐ No ☐ Unknown | |
| 6 | Individuals with low digital literacy | ☐ Yes ☐ No ☐ Unknown | |
| 7 | Other vulnerable groups | ☐ Yes ☐ No ☐ Unknown | |

### 6.5 Regulatory and Oversight Bodies

*Identify regulatory authorities that may have oversight of this AI system.*

| # | Authority | Jurisdiction | Applicable obligations |
|---|-----------|-------------|----------------------|
| 1 | | | |
| 2 | | | |

### 6.6 Third-Party Suppliers

*Where third-party AI components are used, identify supplier obligations relevant to this AISIA.*

| # | Supplier | AI Component Provided | Responsibility allocation |
|---|----------|-----------------------|--------------------------|
| 1 | | | |
| 2 | | | |

---

## Section 7 — Benefits and Harms Analysis [Ref. 6.7]

*For each interested party category identified in Section 6, assess reasonably foreseeable benefits and harms across the eight impact dimensions. Complete one table per significant interested party category, or use a combined view where appropriate.*

*Instructions*:
- Assess **benefits first** — the AISIA is a balanced assessment, not only a harm register
- For each harm: rate **Severity** (Negligible / Minor / Moderate / Serious / Critical), **Breadth** (Individual / Small group / Large group / Population / Societal), and **Reversibility** (Easily reversible / Partially reversible / Difficult to reverse / Irreversible)
- Note existing controls that already mitigate identified harms
- Proposed additional measures are recorded in Section 8.3

---

### 7.1 Accountability

*Harms and benefits relating to responsibility, governance, auditability, and recourse.*

| | Benefits | Harms |
|-|---------|-------|
| **Description** | *What reasonably foreseeable benefits does this AI system produce regarding accountability?* | *What reasonably foreseeable harms could arise regarding accountability?* |
| **Affected parties** | | |
| **Severity** | N/A | *Negligible / Minor / Moderate / Serious / Critical* |
| **Breadth** | N/A | *Individual / Small group / Large group / Population* |
| **Reversibility** | N/A | *Easily reversible / Partially / Difficult / Irreversible* |
| **Existing controls** | | |
| **Residual concern** | ☐ None ☐ Low ☐ Medium ☐ High | ☐ None ☐ Low ☐ Medium ☐ High |

---

### 7.2 Transparency

*Harms and benefits relating to how well the AI system's operation and outputs can be understood.*

| | Benefits | Harms |
|-|---------|-------|
| **Description** | | |
| **Affected parties** | | |
| **Severity** | N/A | |
| **Breadth** | N/A | |
| **Reversibility** | N/A | |
| **Existing controls** | | |
| **Residual concern** | ☐ None ☐ Low ☐ Medium ☐ High | ☐ None ☐ Low ☐ Medium ☐ High |

---

### 7.3 Fairness and Discrimination

*Harms and benefits relating to equitable treatment across individuals, groups, and protected characteristics.*

| | Benefits | Harms |
|-|---------|-------|
| **Description** | | |
| **Affected parties** | | |
| **Protected characteristics at risk** | N/A | *List any (gender, race, age, disability, religion, nationality, etc.)* |
| **Fairness analysis result** | | |
| **Severity** | N/A | |
| **Breadth** | N/A | |
| **Reversibility** | N/A | |
| **Existing controls** | | |
| **Residual concern** | ☐ None ☐ Low ☐ Medium ☐ High | ☐ None ☐ Low ☐ Medium ☐ High |

---

### 7.4 Privacy

*Harms and benefits relating to personal data, surveillance, inference of sensitive attributes.*

| | Benefits | Harms |
|-|---------|-------|
| **Description** | | |
| **Personal data categories involved** | | |
| **Privacy-specific risks** | N/A | *e.g., re-identification, inference, surveillance, data breach via AI output, etc.* |
| **Severity** | N/A | |
| **Breadth** | N/A | |
| **Reversibility** | N/A | |
| **DPIA cross-reference** | N/A | *If a DPIA has been / will be conducted: reference here* |
| **Existing controls** | | |
| **Residual concern** | ☐ None ☐ Low ☐ Medium ☐ High | ☐ None ☐ Low ☐ Medium ☐ High |

---

### 7.5 Reliability

*Harms and benefits relating to AI system consistency, robustness, and performance variability.*

| | Benefits | Harms |
|-|---------|-------|
| **Description** | | |
| **Error rates / performance variability** | | |
| **Conditions causing degraded performance** | | |
| **Severity** | N/A | |
| **Breadth** | N/A | |
| **Reversibility** | N/A | |
| **Existing controls** | | |
| **Residual concern** | ☐ None ☐ Low ☐ Medium ☐ High | ☐ None ☐ Low ☐ Medium ☐ High |

---

### 7.6 Safety

*Harms and benefits relating to physical or psychological safety of users and affected individuals.*

| | Benefits | Harms |
|-|---------|-------|
| **Description** | | |
| **Safety-critical use?** | ☐ Yes ☐ No | ☐ Yes ☐ No |
| **Psychological safety concerns** | N/A | *e.g., distress from AI-driven decisions, manipulation potential, etc.* |
| **Physical safety concerns** | N/A | *e.g., AI controlling physical systems; AI-driven medical or infrastructure decisions* |
| **Severity** | N/A | |
| **Breadth** | N/A | |
| **Reversibility** | N/A | |
| **Existing controls** | | |
| **Residual concern** | ☐ None ☐ Low ☐ Medium ☐ High | ☐ None ☐ Low ☐ Medium ☐ High |

---

### 7.7 Explainability

*Harms and benefits relating to the ability to understand and explain AI reasoning and outputs.*

| | Benefits | Harms |
|-|---------|-------|
| **Description** | | |
| **Explainability mechanism available?** | ☐ Yes ☐ Partial ☐ No | |
| **Audiences requiring explanation** | | *e.g., affected individuals, auditors, operators, regulators* |
| **Severity** | N/A | |
| **Breadth** | N/A | |
| **Reversibility** | N/A | |
| **Existing controls** | | |
| **Residual concern** | ☐ None ☐ Low ☐ Medium ☐ High | ☐ None ☐ Low ☐ Medium ☐ High |

---

### 7.8 Environmental Impact

*Harms and benefits relating to energy consumption, carbon footprint, and resource use.*

| | Benefits | Harms |
|-|---------|-------|
| **Description** | | |
| **Energy / carbon footprint estimate** | N/A | *Approximate (high / medium / low / negligible) — or documented measurement if available* |
| **Proportionality assessment** | | *Is the environmental cost proportionate to the value delivered?* |
| **Severity** | N/A | |
| **Breadth** | N/A | |
| **Existing controls / optimisations** | | |
| **Residual concern** | ☐ None ☐ Low ☐ Medium ☐ High | ☐ None ☐ Low ☐ Medium ☐ High |

---

### 7.9 Societal Impact Summary [Ref. 6.7 + A.5.5]

*This section addresses macro-level societal impacts beyond individual harm — required by ISO 42001:2023 Control A.5.5.*

| Societal Dimension | Assessment |
|-------------------|-----------|
| **Systemic bias / societal inequality** | *At scale, could this AI system reinforce or amplify existing inequalities?* |
| **Labour and employment** | *Could this AI system displace workers or materially change employment patterns?* |
| **Misinformation risk** | *Could this AI system generate or amplify false or misleading content?* |
| **Democratic and civic processes** | *Could this AI system affect democratic participation, elections, or civic discourse?* |
| **Concentration of power** | *Does this AI system concentrate decision-making in ways that reduce accountability?* |
| **Dependency and resilience** | *Does societal reliance on this AI system create vulnerability if it fails or is compromised?* |
| **Cross-border / global impact** | *Where relevant: does the AI system have impacts across jurisdictions or internationally?* |

**Societal impact assessment summary**:
*[Write 2–4 sentences summarising the overall societal impact picture and whether it warrants additional measures.]*

---

## Section 8 — AI System Failures and Foreseeable Misuse [Ref. 6.8]

### 8.1 Impact of AI System Failures [Ref. 6.8.2]

*For each interested party category identified in Section 6, document the impact of potential AI system failures.*

| # | Failure Description | Affected Interested Party | Impacts Resulting from Potential Failure |
|---|--------------------|--------------------------|-----------------------------------------|
| 1 | *Description of potential failure (technical, data, operational, adversarial)* | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

### 8.2 Impact of Reasonably Foreseeable Misuse [Ref. 6.8.3]

*For each reasonably foreseeable misuse scenario identified in Section 2.4, document the impacts on interested parties.*

| # | Reasonably Foreseeable Misuse Description | Affected Interested Party | Impacts Caused by Misuse (Benefit or Harm) |
|---|------------------------------------------|--------------------------|--------------------------------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

### 8.3 Measures Register

*For each significant harm identified in Sections 7 and 8.1–8.2, record the measure selected to address it.*

| # | Harm / Risk Addressed | Measure Description | Measure Type | Responsible | Target Date | Status |
|---|----------------------|---------------------|-------------|-------------|-------------|--------|
| 1 | | | *Technical / Administrative / Governance* | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |

---

## Section 9 — Impact Classification and Conclusions [Ref. 6.9]

### 9.1 Overall Impact Classification

*Assign the overall AISIA impact classification. The classification reflects the highest-severity harm dimension after considering breadth and reversibility. Refer to AI-POL-A.5.2-5 for classification criteria.*

| Dimension | Residual Concern Level (from Sections 7.1–7.8) |
|-----------|------------------------------------------------|
| Accountability | ☐ None ☐ Low ☐ Medium ☐ High |
| Transparency | ☐ None ☐ Low ☐ Medium ☐ High |
| Fairness and Discrimination | ☐ None ☐ Low ☐ Medium ☐ High |
| Privacy | ☐ None ☐ Low ☐ Medium ☐ High |
| Reliability | ☐ None ☐ Low ☐ Medium ☐ High |
| Safety | ☐ None ☐ Low ☐ Medium ☐ High |
| Explainability | ☐ None ☐ Low ☐ Medium ☐ High |
| Environmental Impact | ☐ None ☐ Low ☐ Medium ☐ High |
| Societal Impact | ☐ None ☐ Low ☐ Medium ☐ High |
| AI System Failures | ☐ None ☐ Low ☐ Medium ☐ High |
| Reasonably Foreseeable Misuse | ☐ None ☐ Low ☐ Medium ☐ High |

**Overall Impact Classification (pre-measures)**:
☐ **Low** ☐ **Medium** ☐ **High**

*Rationale for classification*:
*[Write 2–4 sentences explaining the basis for the classification, referencing the highest-concern dimensions.]*

**Overall Impact Classification (post-measures / residual)**:
☐ **Low** ☐ **Medium** ☐ **High**

*Residual impact rationale*:
*[Explain how measures reduce the classification, or note where classification remains unchanged.]*

### 9.2 Deployment Recommendation

| Field | Content |
|-------|---------|
| **Recommendation** | ☐ Approved for deployment ☐ Approved for deployment with conditions ☐ Not recommended — further measures required |
| **Deployment conditions** | *If conditional: list specific conditions that must be met before or during deployment* |
| **Open measures** | *List any measures in Section 8.3 not yet completed at time of approval, with planned completion dates* |
| **Residual risks accepted** | *List any harms not fully mitigated, with rationale for acceptance* |
| **Accepted by** | *[Name, Role — AI Governance Officer or AI Risk Owner if applicable]* |

### 9.3 Assessment Conclusions

*[Write a brief narrative summary (5–10 sentences) of the overall AISIA findings, including: the nature of the AI system, the most significant impact areas, the measures recommended, the classification result, and any conditions on deployment.]*

---

## Section 10 — Approval Record [Ref. A.5.3 — AI-POL-A.5.2-5]

*This section must be completed by the AI Governance Officer before deployment authorisation is issued. Do not deploy without a signed approval record.*

| Field | Value |
|-------|-------|
| **AISIA Document ID** | |
| **AI System Name and Version** | |
| **AISIA Version** | |
| **Assessment Date** | |
| **Assessment Conducted By** | |
| **Impact Classification (Residual)** | ☐ Low ☐ Medium ☐ High |
| **Approval Status** | ☐ Approved ☐ Approved with conditions ☐ Rejected — further work required |
| **Conditions / Open items** | |
| **AI Governance Officer Name** | |
| **AI Governance Officer Approval** | [Signature or digital approval reference] |
| **Approval Date** | |
| **Next Review Date** | *Low: [Approval date + 3 years] / Medium: [+1 year] / High: [+6 months]* |
| **Executive Management notified?** | ☐ Yes ☐ No ☐ Not required — *Required for High-impact AI systems* |
| **Legal / DPO reviewed?** | ☐ Yes ☐ No ☐ Not required — *Required where personal data involved or FRIA trigger exists* |

---

## Section 11 — AISIA Review Log

*Record all subsequent reviews of this AISIA here. Create a new AISIA version document for any review that identifies material changes to the assessment.*

| Review Date | Review Type | Conducted By | Outcome | Changes from Previous | New AISIA Version Required? | Next Review Date |
|------------|-------------|-------------|---------|----------------------|----------------------------|-----------------|
| | ☐ Scheduled ☐ Post-incident ☐ Material change | | ☐ No change ☐ Updated | | ☐ Yes ☐ No | |
| | ☐ Scheduled ☐ Post-incident ☐ Material change | | ☐ No change ☐ Updated | | ☐ Yes ☐ No | |
| | ☐ Scheduled ☐ Post-incident ☐ Material change | | ☐ No change ☐ Updated | | ☐ Yes ☐ No | |

---

## Annex A — Harms Taxonomy Quick Reference (ISO 42005:2025 Annex C)

*Reference table for use when completing Section 7. These are the categories of foreseeable AI-related harms per ISO 42005:2025 Annex C.*

| Dimension | Typical Harm Examples |
|-----------|----------------------|
| **Accountability** | Unclear responsibility for AI-driven decisions; no appeals mechanism; inability to attribute errors; AI system used to evade accountability |
| **Transparency** | Affected individuals unaware AI is used; AI reasoning opaque; inability to understand or challenge AI outputs; misleading explanations |
| **Fairness and discrimination** | Biased outputs across protected characteristics; reinforcement of historical discrimination; disparate impact on minority groups; proxy discrimination |
| **Privacy** | Processing personal data beyond scope; re-identification of anonymised data; inference of sensitive attributes; surveillance; data breach via AI output |
| **Reliability** | High error rates; inconsistent outputs; performance degradation in edge cases; over-reliance on AI despite known limitations |
| **Safety** | Physical harm from AI-controlled systems; psychological harm from AI interactions; manipulation; deception; AI-generated harmful content |
| **Explainability** | No explanation available for consequential AI decisions; technical explanations inaccessible to non-expert users; post-hoc explanations that are inaccurate or misleading |
| **Environmental impact** | Disproportionate energy consumption; excessive carbon footprint; rare earth material consumption; e-waste from AI infrastructure |

---

## Annex B — ISO 42001:2023 Control Mapping

*Cross-reference between this AISIA template and the ISO 42001:2023 controls and clauses it satisfies.*

| AISIA Section | ISO 42001:2023 Reference | Control / Clause |
|--------------|--------------------------|-----------------|
| Sections 1–5 (AI system documentation) | Clause 6.1.4, Control A.5.2, A.5.3 | AISIA process and documentation |
| Section 6 (Interested parties) | Clause 4.2, Control A.5.4 | Individual impact — identifying affected parties |
| Section 7.1–7.8 (Benefits and harms) | Controls A.5.4, A.5.5 | Individual and societal impact assessment |
| Section 7.9 (Societal impact) | Control A.5.5 | Assessing societal impacts |
| Section 8.1 (AI system failures) | Clause 6.1.4, Control A.5.4 | Impact of failures on individuals |
| Section 8.2 (Foreseeable misuse) | Control A.5.4, A.9.4 | Intended use and misuse controls |
| Section 8.3 (Measures) | Clause 6.1.3, Clause 6.1.4 | AI risk treatment |
| Section 9 (Classification) | Clause 6.1.4, Control A.5.2 | Impact classification and conclusions |
| Section 10 (Approval) | Control A.5.3 | Documentation and approval |

---

<!-- QA_VERIFIED: 2026-04-15 -->
