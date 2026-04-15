<!-- ISMS-CORE:POLICY:AI-POL-A.5.2-5:ai:POL:a.5.2-5 -->
**AI-POL-A.5.2-5 — AI System Impact Assessment**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI System Impact Assessment |
| **Document Type** | Policy |
| **Document ID** | AI-POL-A.5.2-5 |
| **Document Creator** | AI Governance Officer |
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
| 1.0 | [Date to be set] | AI Governance Officer | Initial policy for ISO/IEC 42001:2023 first certification |

**Review Cycle**: Annual (or upon publication of updated ISO 42005 or significant change in AI portfolio)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: AI Governance Officer
- Secondary: Legal / Compliance Officer
- Compliance: Chief Information Security Officer (CISO)
- Final Authority: Executive Management

**Related Documents**:

- AI-POL-00 (AIMS Regulatory Applicability Framework)
- AI-POL-01 (AIMS Governance and Decision-Making Framework)
- AI-IMP-A.5.2-5-UG (AI System Impact Assessment — User Guide)
- AI-IMP-A.5.2-5-TG (AI System Impact Assessment — Technical Guide)
- ISO/IEC 42001:2023 Controls A.5.2, A.5.3, A.5.4, A.5.5
- ISO/IEC 42001:2023 Clause 6.1.4 (AI system impact assessment)
- ISO/IEC 42005:2025 — AI system impact assessment (companion methodology standard)
- ISO/IEC 42001:2023 Annex B.5 (Implementation guidance — Assessing impacts of AI systems)
- PRIV-POL-00 (Privacy Regulatory Applicability — for AI processing personal data)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for assessing, documenting, and maintaining AI System Impact Assessments (AISIA) — in accordance with ISO/IEC 42001:2023 Controls A.5.2 through A.5.5 and the detailed methodology standard ISO/IEC 42005:2025.

**Scope**: All AI systems within the AIMS scope; all AISIA processes from establishment through documentation, individual impact assessment, and societal impact assessment.

**Purpose**: Define WHAT the AISIA process must cover, WHO is responsible for conducting and approving assessments, WHEN assessments must be performed and reviewed. Implementation methodology is in AI-IMP-A.5.2-5-UG (process guide) and AI-IMP-A.5.2-5-TG (template guide, built against ISO 42005:2025).

**AISIA and FRIA alignment note**: For AI systems classified as high-risk under the EU AI Act, the AISIA provides the analytical foundation for the Fundamental Rights Impact Assessment (FRIA) required under Article 26. Organisations subject to both ISO 42001:2023 and EU AI Act obligations shall document the cross-reference between AISIA records and FRIA outputs.

**Combined Control Rationale**: A.5.2 (AISIA process), A.5.3 (documentation), A.5.4 (individual impacts), and A.5.5 (societal impacts) form the impact assessment system. The process (A.5.2) comes first; documentation obligations (A.5.3) govern retention; individual impact assessment (A.5.4) and societal impact assessment (A.5.5) are the two lenses of the assessment itself. These four controls are inseparable in practice.

---

## Scope and Applicability

### ISO/IEC 42001:2023 Control Statements

**Control A.5.2 — AI system impact assessment process**
The organisation shall establish a process to assess the potential consequences for individuals or groups of individuals, or both, and societies that can result from the AI system throughout its life cycle.

**Control A.5.3 — Documentation of AI system impact assessments**
The organisation shall document the results of AI system impact assessments and retain results for a defined period.

**Control A.5.4 — Assessing AI system impact on individuals or groups of individuals**
The organisation shall assess and document the potential impacts of AI systems to individuals or groups of individuals throughout the system's life cycle.

**Control A.5.5 — Assessing societal impacts of AI systems**
The organisation shall assess and document the potential societal impacts of their AI systems throughout their life cycle.

### What This Policy Covers

- Mandatory AISIA process requirements
- Scope definition for each AISIA (which systems, which populations)
- When AISIAs must be performed and reviewed
- Individual impact assessment requirements (A.5.4)
- Societal impact assessment requirements (A.5.5)
- Documentation, retention, and access requirements (A.5.3)
- AISIA approval process

### What This Policy Does NOT Cover

- Detailed AISIA methodology and template (addressed in AI-IMP-A.5.2-5-TG, built against ISO 42005:2025)
- AI risk assessment (risk-to-organisation lens — addressed separately in AIMS Risk Assessment Procedure)
- GDPR Data Protection Impact Assessment (DPIA) — linked but separate obligation under PRIV-POL-00

### Regulatory Framework

**Tier 1: Mandatory Compliance** (per AI-POL-00):

- **EU AI Act (Regulation 2024/1689)**: Article 26 — deployers of certain high-risk AI systems shall conduct a Fundamental Rights Impact Assessment (FRIA) before putting the system into use; AISIA is the ISO 42001 instrument that provides the analytical foundation for FRIA
- **GDPR Article 35**: Where AI processing personal data is likely to result in high risk to individuals, a DPIA is required — AISIA and DPIA are complementary (see Privacy note below)

**Tier 2: Conditional** (per AI-POL-00):

- **ISO/IEC 42001:2023**: Controls A.5.2–A.5.5 — applies where AIMS certification is in scope or contractually required
- **ISO/IEC 42005:2025**: AISIA methodology standard — applies where ISO 42001:2023 certification is in scope; all AISIA templates shall be built against ISO 42005:2025 Clause 6

**Tier 3: Informational** (per AI-POL-00):

- NIST AI RMF: MAP 1.x and MEASURE 2.x — impact measurement and documentation

---

## Policy Statements: AISIA Process (A.5.2)

### Mandatory AISIA Process

[Organisation] SHALL establish, implement, and maintain an AISIA process that:

- Is applied to every in-scope AI system before initial deployment
- Is documented as a procedure, not left to ad hoc judgment
- Produces a structured, documented AISIA record for each AI system
- Is repeatable — consistent application across different AI systems and assessors
- Is integrated into the AI system life cycle (deployment gate at minimum; review cycle thereafter)

The AISIA methodology shall follow ISO/IEC 42005:2025 — the dedicated AI system impact assessment standard. AISIA templates are maintained in AI-IMP-A.5.2-5-TG.

### AISIA Scope Definition

For each AI system, the AISIA shall define its scope including:

- **AI system description**: Name, version, purpose, output type, deployment context
- **Intended uses**: Documented uses for which the system was designed and validated
- **Foreseeable misuses**: Uses that could foreseeably occur even if unintended
- **Sensitive uses**: Any use involving vulnerable populations, consequential decisions, or sensitive personal data
- **Restricted uses**: Uses that are explicitly prohibited

### When AISIA Must Be Performed

An AISIA is mandatory:

| Trigger | Requirement |
|---------|------------|
| **Before initial deployment** | AISIA must be completed and approved before the AI system is deployed in any operational context |
| **Material change to AI system** | New version with changed outputs, new use case, new population affected, new deployment context |
| **Change in operating context** | New regulation affecting the AI system's use; new jurisdiction of deployment |
| **Scheduled review** | Low-impact AI systems: every 3 years; Medium-impact: annually; High-impact: every 6 months |
| **AI incident involving the system** | Following any AI incident where the system's impact on individuals was material |

**Deployment gate**: No AI system shall be deployed in an operational context without a completed and approved AISIA. The AI Governance Officer shall approve the AISIA before deployment authorisation.

### AISIA Review Depth

Two levels of review apply depending on the trigger:

| Review Type | When Required | What Is Required |
|-------------|---------------|-----------------|
| **Currency check** | Scheduled review (Low: 3yr; Medium: annual; High: 6mo) where no material change has occurred | Confirm the AI system's purpose, population, and deployment context are unchanged; confirm identified measures are still in place; update "Next review date"; AI System Owner sign-off, AI Governance Officer approval |
| **Full re-assessment** | Material change to the AI system or operating context (new use case, new affected population, significant model update, new regulation, AI incident involving the system) | Full re-run of the AISIA process per ISO 42005:2025 Clause 6; all sections re-evaluated; new impact classification assigned; AI Governance Officer approval required before continued or expanded operation |

Where a currency check reveals changes that were not identified as material at the time they occurred, the AI System Owner shall escalate to a full re-assessment and document the oversight in the AISIA record.

---

## Policy Statements: Individual Impact Assessment (A.5.4)

### Individual Impact Assessment Requirement

[Organisation] SHALL assess and document, for each AI system, the potential impacts on **individuals or groups of individuals** throughout the AI system's life cycle.

### Assessment Dimensions for Individual Impact

For each affected population identified in the AISIA scope, the following dimensions shall be assessed:

| Dimension | Assessment Questions |
|-----------|---------------------|
| **Nature of impact** | What type of harm could the AI system cause? (financial, physical, psychological, reputational, loss of rights, discrimination, loss of opportunity) |
| **Severity** | How serious is the worst-case impact on an individual? |
| **Breadth** | How many individuals could be affected? (individual, group, large population) |
| **Reversibility** | Can the harm be corrected if the AI system makes an error? Is there an appeals process? |
| **Duration** | Is the impact short-term, medium-term, or long-lasting / permanent? |
| **Consent and awareness** | Are affected individuals aware that an AI system is being used? Did they consent where required? |
| **Human oversight** | Is there meaningful human review of AI outputs before they affect individuals? |
| **Recourse** | Can individuals challenge AI-driven decisions? Is a human decision-maker available? |
| **Vulnerable populations** | Are any affected individuals in a vulnerable category? (children, elderly, persons with disabilities, minority groups, power-asymmetric relationships such as employer/employee or government/citizen) |

### Impact Classification

Based on the above dimensions, each AI system shall be assigned an impact classification:

| Classification | Criteria |
|---------------|---------|
| **Low** | Limited impact; easily reversible; non-vulnerable individuals; AI is advisory with strong human oversight; minimal consent or transparency concerns |
| **Medium** | Moderate impact; partially reversible; some vulnerable individuals may be affected; AI has significant weight in decisions; structured human oversight |
| **High** | Significant or irreversible impact; vulnerable individuals affected; AI drives consequential decisions with limited human review; affects fundamental rights |

The impact classification determines the control requirements applied under A.5.2 and feeds directly into the AI risk treatment plan (ISO 42001:2023 Clause 6.1.3).

---

## Policy Statements: Societal Impact Assessment (A.5.5)

### Societal Impact Assessment Requirement

[Organisation] SHALL assess and document, for each AI system, the potential **societal impacts** throughout the AI system's life cycle.

The societal impact assessment is a separate and additional lens from the individual impact assessment. An AI system with low individual impact may have significant societal impact at scale.

### Societal Impact Dimensions

| Dimension | What to Assess |
|-----------|---------------|
| **Scale of deployment** | If deployed at scale, what are the cumulative societal effects of many individual AI-driven decisions? |
| **Misinformation risk** | Could the AI system generate or amplify false or misleading content? What is the potential scale of spread? |
| **Systemic bias** | Could the AI system reinforce or amplify existing societal inequalities at scale? |
| **Labour and employment** | Could the AI system displace workers or change employment patterns in ways that are socially significant? |
| **Environmental impact** | What is the energy/carbon footprint of operating this AI system? Is it proportionate to the value delivered? |
| **Democratic and civic processes** | Could the AI system be used in ways that affect democratic participation, electoral processes, or civic discourse? |
| **Concentration of power** | Does the AI system concentrate decision-making power in ways that reduce accountability or oversight? |
| **Dependency and resilience** | Does reliance on this AI system create societal vulnerability if the system fails or is compromised? |

Societal impacts that are beyond the organisation's direct control shall be documented with the assessment of what measures the organisation can take to mitigate its contribution to those impacts.

---

## Policy Statements: Documentation and Retention (A.5.3)

### AISIA Record Requirements

Each completed AISIA shall be documented as a structured record including (per ISO 42005:2025 Clause 6):

1. AI system identification (name, version, owner)
2. Assessment date and assessor identity
3. AI system description, functionalities, and purpose
4. Intended uses, sensitive uses, restricted uses, foreseeable misuse
5. Data information and quality summary
6. Algorithm and model information summary
7. Deployment environment description
8. Affected populations (direct and indirect)
9. Individual impact assessment per affected population (A.5.4)
10. Societal impact assessment (A.5.5)
11. Benefits and positive impacts (not only harms)
12. Measures selected to address identified harms
13. Residual impact assessment after measures applied
14. Impact classification (Low / Medium / High)
15. Approval: AI Governance Officer signature and date
16. Next review date

### Retention

AISIA records shall be retained for:

- Duration of the AI system's operational life, PLUS
- 5 years after decommissioning

Retention ensures auditability and supports any regulatory investigation or litigation involving AI system impacts.

### Access

AISIA records shall be:

- Accessible to the AI Governance Officer at all times
- Available to internal auditors on request
- Made available to regulatory authorities on request (EU AI Act Article 26 FRIA disclosure obligations)
- Shared with affected individuals or civil society to the extent determined appropriate by the AI Governance Officer and Legal, proportionate to the AI system's impact level

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|----------------|
| **AI Governance Officer** | Own the AISIA process; approve all AISIAs before deployment; maintain AISIA records; ensure review schedule is followed |
| **AI Risk Owner** | Commission AISIA for owned AI systems; provide AI system context to assessors; accept residual impact classification |
| **AI System Owner** | Provide AI system documentation for AISIA; implement measures identified in AISIA; maintain AISIA currency as system changes |
| **Legal / DPO** | Advise on regulatory dimensions (EU AI Act FRIA, GDPR DPIA triggers); review high-impact AISIAs for compliance |
| **CISO** | Review security dimensions of AI impact (adversarial manipulation potential, incident response readiness) |
| **Executive Management** | Approve high-impact AI system deployments; receive AISIA summaries at management review |

---

## Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| AISIA records | Completed AISIA per AI system per version | Duration of system life + 5 years |
| AISIA approval records | Documented approval by AI Governance Officer | Same as AISIA |
| Review records | Evidence of scheduled AISIA reviews with outcomes | Same as AISIA |
| AISIA process documentation | Procedure for how AISIAs are conducted | Current + 3 years |
| Deployment gate records | Evidence that AISIA approval was obtained before deployment | Same as AISIA |

---

## Audit Considerations

Auditors verifying compliance with A.5.2–A.5.5 should expect to find:

- A documented AISIA process (not ad hoc assessments)
- Completed AISIA records for all in-scope AI systems prior to deployment
- AISIA records covering both individual (A.5.4) and societal (A.5.5) impact dimensions
- Impact classification (Low/Medium/High) documented with supporting rationale
- Evidence that AISIAs are reviewed on schedule and when AI systems change
- AISIA approval by AI Governance Officer documented before deployment
- AISIA records retained for the required period

---

<!-- QA_VERIFIED: [2026-04-15] -->
