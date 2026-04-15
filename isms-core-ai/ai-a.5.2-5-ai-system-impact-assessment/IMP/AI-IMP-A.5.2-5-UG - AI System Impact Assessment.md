<!-- ISMS-CORE:IMP:AI-IMP-A.5.2-5-UG:ai:UG:a.5.2-5 -->
**AI-IMP-A.5.2-5-UG — AI System Impact Assessment — User Guide**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI System Impact Assessment — User Guide |
| **Document Type** | Implementation Guide (User) |
| **Document ID** | AI-IMP-A.5.2-5-UG |
| **Related Policy** | AI-POL-A.5.2-5 (AI System Impact Assessment) |
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

**Review Cycle**: Annual (or upon significant change to AISIA process or ISO 42005:2025 update)
**Next Review Date**: [Effective Date + 12 months]

**Related Documents**:

- AI-POL-A.5.2-5 (AI System Impact Assessment — governing policy)
- AI-IMP-A.5.2-5-TG (AI System Impact Assessment — AISIA Template)
- AI-POL-00 (AIMS Regulatory Applicability Framework)
- AI-POL-A.6.2 (AI System Lifecycle — deployment gate)
- ISO/IEC 42001:2023 Controls A.5.2–A.5.5 and Clause 6.1.4
- ISO/IEC 42005:2025 (AI system impact assessment — companion methodology standard)

---

## Purpose of This Guide

This guide explains **how to conduct an AI System Impact Assessment (AISIA)** at [Organisation] — who does it, when it is required, what the process steps are, and how to use the AISIA template. It is the practical companion to AI-POL-A.5.2-5 (the governing policy) and AI-IMP-A.5.2-5-TG (the fillable template).

**Who this guide is for**: AI System Owners, AI Governance Officer, Legal/DPO, AI development teams, and any person involved in deploying or significantly changing an AI system within the AIMS scope.

**Methodology basis**: [Organisation]'s AISIA process follows ISO/IEC 42005:2025 — the dedicated AI system impact assessment standard. The template in AI-IMP-A.5.2-5-TG is built against ISO 42005:2025 Annex E.

---

## Part 1 — What Is an AISIA?

### 1.1 Purpose of an AISIA

An AISIA is a structured assessment of the potential consequences — both positive and negative — that an AI system can have on individuals, groups of individuals, and society. It is not a risk assessment for the organisation (that is the AIMS Risk Assessment). The AISIA looks outward: who could be affected, how, and with what severity?

An AISIA answers three questions:
1. **Who is affected?** — Users, affected individuals, vulnerable groups, society
2. **What could happen to them?** — Benefits and harms across eight impact dimensions
3. **How significant is it?** — Severity, reversibility, breadth, duration

### 1.2 AISIA vs. DPIA vs. FRIA

These three assessments are complementary but distinct:

| Assessment | Lens | Standard/Law | When triggered |
|-----------|------|-------------|---------------|
| **AISIA** | Impacts on individuals and society from the AI system | ISO 42001:2023 / ISO 42005:2025 | All in-scope AI systems |
| **DPIA** | Risks to data subjects from personal data processing | GDPR Article 35 | When AI processing personal data is high-risk |
| **FRIA** | Fundamental rights of individuals affected by high-risk AI | EU AI Act Article 26 | Deployers of certain high-risk AI systems |

Where all three are required, the AISIA provides the analytical foundation — the DPIA and FRIA can reference the AISIA rather than repeating the same analysis. The AI Governance Officer and DPO shall coordinate to avoid duplication.

### 1.3 Impact Classification

Every AISIA results in one of three impact classifications:

| Classification | Description |
|---------------|-------------|
| **Low** | Limited impact; easily reversible; non-vulnerable populations; strong human oversight; minimal fundamental rights concerns |
| **Medium** | Moderate impact; partially reversible; some vulnerable individuals may be affected; AI has significant weight in decisions |
| **High** | Significant or irreversible impact; vulnerable populations affected; AI drives consequential decisions; affects fundamental rights |

The classification determines the control requirements applied (AI-POL-A.5.2-5), review frequency, and whether Executive Management approval is required for deployment.

---

## Part 2 — When to Conduct an AISIA

### 2.1 Mandatory Triggers

An AISIA must be completed **before** the following events occur:

| Trigger | Who initiates |
|---------|--------------|
| **Initial deployment** of any in-scope AI system | AI System Owner |
| **Material change** to an AI system (new version, new use case, changed population, new deployment context) | AI System Owner |
| **New jurisdiction** of deployment | AI System Owner / Legal |
| **Post-incident review** following any AI incident with material impact on individuals | AI Governance Officer |
| **Scheduled review** — Low: 3 years / Medium: 1 year / High: 6 months | AI Governance Officer |

### 2.2 The Deployment Gate

No AI system shall be deployed operationally without a completed and **approved** AISIA. The AI Governance Officer approves the AISIA before deployment authorisation is issued. This gate applies even for internal tools and low-volume systems.

**What "approved" means**: The AI Governance Officer has reviewed the completed AISIA template, confirmed all sections are complete, and signed the approval record in Section 9 of the template.

### 2.3 Scoping — Does This AI System Need an AISIA?

An AISIA is required for any AI system that:
- Processes data about individuals (even indirectly)
- Produces outputs that could affect individuals (decisions, recommendations, classifications, content)
- Is used by staff whose behaviour is influenced by AI outputs
- Could generate content that reaches or affects the public

If uncertain, the default is: **conduct an AISIA**. The AI Governance Officer may classify a system as out-of-scope only where the system clearly produces no impact on any individual or group.

---

## Part 3 — AISIA Process Steps

The AISIA process has six phases. Each phase has a responsible role and a completion criterion.

### Phase 1: Initiation and Scoping

**Responsible**: AI System Owner (with AI Governance Officer support)

**Outputs**: Completed Sections 1–2 of the AISIA template

**Steps**:

1. AI System Owner notifies AI Governance Officer that a new AISIA is required (trigger: new system, material change, or review schedule)
2. AI System Owner and AI Governance Officer confirm the scope:
   - Which AI system? Which version?
   - What is the intended use?
   - What is the deployment context?
   - Who are the users? Who are the affected individuals?
3. AI System Owner is confirmed as the responsible person for completing Sections 1–6 of the template
4. AI Governance Officer is confirmed as the approver (Section 9)
5. Legal/DPO is notified where personal data is involved (DPIA trigger assessment)

**Time allocation**: 1–2 hours for standard systems; longer for complex multi-use cases

---

### Phase 2: AI System Information Gathering

**Responsible**: AI System Owner (with input from ML Engineers / Data Governance Lead)

**Outputs**: Completed Sections 3–5 of the AISIA template

**Steps**:

1. Document the AI system's technical profile:
   - Algorithm type and model architecture
   - Training data sources and coverage
   - Operational data used at runtime
   - Performance metrics and validation results
   - Monitoring arrangements
2. Document the deployment environment:
   - Where the system is deployed (internal tool, customer-facing, public-facing)
   - Who operates it; who the end-users are
   - What happens to AI outputs (advisory, automated, hybrid)
3. Confirm the intended use statement is current and accurately documented

**Practical tip**: Use the AI System Resource Register (AI-POL-A.4.2-6) as a starting point — much of this information should already be documented there.

---

### Phase 3: Interested Party Identification

**Responsible**: AI System Owner (with Legal/DPO for external party identification)

**Outputs**: Completed Section 6 of the AISIA template

**Steps**:

1. Identify all categories of interested parties:
   - **Internal**: Staff who use the system, staff whose work is affected, management relying on AI outputs
   - **External users**: Customers, partners, or third parties directly using the system
   - **Affected individuals**: Persons who are not direct users but whose interests are affected by AI outputs (e.g., job applicants assessed by AI, individuals subject to AI-driven decisions)
   - **Vulnerable groups**: Children, elderly, persons with disabilities, minority groups, power-asymmetric relationships
   - **Society**: Communities, sectors, or the public at large that could be affected at scale

2. For each interested party category, document:
   - Who they are
   - How they interact with or are affected by the AI system
   - What they know about the AI system's use (transparency status)
   - Their capacity to exercise oversight or recourse

3. Flag any party category where vulnerability, power asymmetry, or limited recourse applies — these require additional scrutiny in Phase 4.

---

### Phase 4: Harms and Benefits Analysis

**Responsible**: AI System Owner (primary), with AI Governance Officer review; Legal for regulatory dimensions; DPO for privacy dimensions

**Outputs**: Completed Sections 7–8 of the AISIA template

This is the analytical core of the AISIA. For each interested party category identified in Phase 3, assess both harms and benefits across eight impact dimensions:

| Dimension | What to assess |
|-----------|---------------|
| **Accountability** | Harms/benefits relating to who is responsible for AI-driven outcomes; appeals and redress availability |
| **Transparency** | Harms/benefits from how well the AI system's operation and outputs can be understood by affected parties |
| **Fairness and discrimination** | Harms/benefits relating to whether AI outputs treat individuals or groups equitably across protected characteristics |
| **Privacy** | Harms/benefits relating to personal data processing, surveillance potential, or inference of sensitive attributes |
| **Reliability** | Harms/benefits from the AI system's consistency and robustness; impacts of errors or performance variability |
| **Safety** | Harms/benefits affecting physical or psychological safety of users, affected individuals, or third parties |
| **Explainability** | Harms/benefits relating to whether AI reasoning can be explained to users and affected individuals |
| **Environmental impact** | Harms/benefits from the AI system's energy consumption, carbon footprint, and resource use |

**Completing the analysis**:

For each dimension, document:
- **Benefits**: What reasonably foreseeable positive impacts does this dimension produce for each interested party?
- **Harms**: What reasonably foreseeable negative impacts does this dimension produce for each interested party?
- **Severity**: How serious is the potential harm? (negligible / minor / moderate / serious / critical)
- **Breadth**: How many individuals could be affected?
- **Reversibility**: Can the harm be undone?
- **Existing controls**: What controls already in place mitigate the harm?

**AI system failures** (Section 8.1):
For each interested party, document:
- What failures could occur in the AI system?
- What are the impacts of those failures on that interested party?

**Reasonably foreseeable misuse** (Section 8.2):
Document:
- What misuse of the AI system is reasonably foreseeable (even if unintended)?
- What are the impacts of that misuse on interested parties?

---

### Phase 5: Classification, Measures, and Conclusions

**Responsible**: AI Governance Officer (with AI System Owner input)

**Outputs**: Completed Sections 8 (classification) and 9 (measures + approval) of the AISIA template

**Steps**:

1. **Assign overall impact classification** (Low / Medium / High) based on the harm analysis:
   - The classification reflects the **highest-severity dimension** after considering breadth and reversibility
   - High-impact classification cannot be overridden except by Executive Management with documented rationale

2. **Identify measures**:
   - For each significant harm identified, determine what additional control measure reduces or eliminates it
   - Record the measure, responsible party, and target completion date
   - Note where a measure is already in place vs. where a new measure is needed

3. **Residual impact**:
   - After all planned measures are applied, what is the residual impact level?
   - Where residual harm is assessed as acceptable, document the rationale and who accepted it (AI Governance Officer or AI Risk Owner)

4. **AISIA conclusions**:
   - Document overall findings: is the AI system safe to deploy? With what conditions?
   - Flag any conditions on deployment (e.g., "may only be deployed with human review of all outputs above threshold X")

---

### Phase 6: Approval and Record Filing

**Responsible**: AI Governance Officer (approval); AI System Owner (filing)

**Outputs**: Signed AISIA record, filed in AISIA register

**Steps**:

1. AI Governance Officer reviews the completed AISIA template in full
2. Any gaps or insufficient analysis are returned to the AI System Owner for completion
3. For **High-impact** AI systems: Legal/DPO review before AI Governance Officer approval; Executive Management notified before deployment authorisation
4. AI Governance Officer signs Section 9 (Approval Record) with date
5. AI System Owner files the completed AISIA in the AISIA Register (maintained by AI Governance Officer)
6. Next review date is set per impact classification:
   - Low: 3 years from approval date
   - Medium: 12 months from approval date
   - High: 6 months from approval date

---

## Part 4 — Maintaining the AISIA

### 4.1 Review Process

On each scheduled review:
1. AI System Owner reviews the current AISIA against the current system state
2. If the system has not materially changed: confirm currency with a short review note; update the next review date
3. If the system has changed materially: conduct a full updated AISIA (new document version)
4. AI Governance Officer approves the review outcome (confirmation or updated AISIA)

### 4.2 Material Change Triggers

Treat the following as material changes requiring a new or updated AISIA:

- New use case not covered by the current AISIA scope
- New population of affected individuals
- Changed AI model (new training data, architectural change, fine-tuning that could affect outputs)
- New deployment context (different jurisdiction, different operator, different access channel)
- New regulation or legal requirement affecting the AI system's use

When in doubt: **ask the AI Governance Officer** before deploying a changed system without an updated AISIA.

### 4.3 Post-Incident AISIA Review

Following any AI incident:
1. AI Governance Officer determines whether the incident reveals new or underestimated harms
2. If yes: immediate AISIA review; deployment may be suspended pending updated AISIA
3. If no: incident findings are noted in the AISIA record; next scheduled review date is confirmed

### 4.4 AISIA Register

The AI Governance Officer maintains an AISIA Register containing:
- One entry per AI system with current AISIA version, classification, approval date, and next review date
- Links to the filed AISIA document records
- Flag for overdue reviews

---

## Part 5 — Worked Examples

### Example A: Internal AI-Assisted Recruitment Screening Tool

**System**: AI system that screens CVs and ranks candidates for human review

**Key AISIA findings**:
- Affected individuals: Job applicants (not direct users) — high concern; power asymmetry; potentially life-affecting decisions
- Fairness dimension: High risk of discriminatory bias in training data; ranking could disadvantage protected groups
- Accountability dimension: Human reviewer may over-rely on AI ranking without independent judgment
- Transparency dimension: Applicants unaware AI is used; no recourse mechanism

**Classification**: **High**

**Measures required**: Bias audit of training data and outputs before deployment; transparency notice to applicants; human reviewer mandatory for all shortlisting decisions; appeals process for rejected applicants

---

### Example B: Internal AI Content Summarisation Tool for Staff

**System**: AI tool that summarises internal documents for staff use; no external data; advisory only

**Key AISIA findings**:
- Affected individuals: Internal staff (direct users); no external individuals affected
- Reliability dimension: Summaries may miss nuance; staff may rely on them without reading source
- Privacy dimension: Documents may contain staff personal data; summaries should not be shared externally
- Fairness, safety, environmental: Low concern

**Classification**: **Low**

**Measures required**: Training on limitations; acceptable use guidance; logging of use; prohibition on sharing AI-generated summaries externally without review

---

## Part 6 — Common Mistakes to Avoid

| Mistake | Consequence | How to avoid |
|---------|------------|--------------|
| Treating AISIA as a formality to unlock deployment | Genuine harms missed; audit failure; regulatory exposure | The AI Governance Officer must verify substantive analysis, not just form completion |
| Only assessing harms, not benefits | Incomplete AISIA; misses the proportionality assessment | Benefits columns in Section 7 are mandatory |
| Forgetting affected individuals (non-users) | Most serious AISIA gap; often the highest-risk population | Always ask: "Who is affected by AI outputs who never interacted with the system?" |
| Setting review dates too late | Stale AISIA after system changes | Follow classification-based review frequency strictly |
| Completing AISIA after deployment | Deployment gate breach; no evidence for audit | AISIA approval before any operational use — no exceptions |

---

<!-- QA_VERIFIED: [2026-04-15] -->
