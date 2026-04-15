<!-- ISMS-CORE:POLICY:AI-POL-01:ai:POL:01 -->
**AI-POL-01 — AIMS Governance and Decision-Making Framework**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AIMS Governance and Decision-Making Framework |
| **Document Type** | Policy |
| **Document ID** | AI-POL-01 |
| **Document Creator** | AI Governance Officer / Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |
| **AIMS Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date - 4 weeks] | AI Governance Officer | Initial draft — AIMS governance boundaries and decision-making framework |

**Review Cycle**: Annual (or upon significant AIMS or regulatory changes)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: AI Governance Officer (or designated CISO where no dedicated AI governance role exists)
- Secondary: Chief Information Security Officer (CISO)
- Compliance: Legal / Compliance Officer
- Final Authority: Executive Management

**Related Documents**:

- AI-POL-00 (AIMS Regulatory Applicability Framework — mandatory co-reference)
- ISMS-POL-01 (ISMS Governance and Decision-Making Framework — parent governance document)
- ISO/IEC 42001:2023 Clause 4.3 (Determining the scope of the AIMS)
- ISO/IEC 42001:2023 Clause 5.1 (Leadership and commitment)
- ISO/IEC 42001:2023 Clause 5.2 (AI policy)
- ISO/IEC 42001:2023 Clause 5.3 (Roles, responsibilities and authorities)
- ISO/IEC 42001:2023 Clause 9.2 (Internal audit)
- ISO/IEC 42001:2023 Clause 9.3 (Management review)
- ISO/IEC 42001:2023 Clause 10.2 (Nonconformity and corrective action)

**Distribution**: All AIMS stakeholders, AI system owners, AI risk owners, compliance officers, internal/external auditors
**Referenced By**: All AIMS policy documents, AIMS Statement of Applicability (SoA), AI Risk Treatment Plan

---

## Executive Summary

This policy establishes **where professional judgment is exercised** in the organisation's AI Management System (AIMS), ensuring that:

- **AIMS design decisions are documented and authorised** (control interpretation, regulatory applicability, AI risk acceptance)
- **Decision-making authority is clearly assigned** (AI Governance Officer, CISO, Legal, Executive Management — competence and scope)
- **AIMS criteria evolve through controlled processes** (regulatory changes, new standards, authority guidance, audit feedback)
- **Audit verification is objective and evidence-based** (auditors verify documented design, not reinterpret requirements)

**Purpose**: Enable **objective audit verification** by moving professional judgment to the **AIMS design phase** (documented policies, risk assessments, applicability decisions) rather than the **audit discussion phase** (subjective interpretation during certification).

**Scope**: All AIMS decision-making authority, AI regulatory applicability determinations, control exception handling, AI criteria evolution, and governance review processes.

**Key Principle**: **ISO/IEC 42001:2023 certification requires professional judgment at two stages:**

1. **AIMS Design** (Organisation's responsibility): Interpreting ISO 42001 for organisational context, determining AI provider/deployer roles, selecting risk-based controls, defining evidence sufficiency
2. **AIMS Verification** (Auditor's responsibility): Assessing whether organisational interpretation satisfies ISO 42001, verifying implementation matches documentation

This policy documents organisational professional judgment (Stage 1) to enable objective audit verification (Stage 2).

**Relationship to ISMS-POL-01**: This policy is the AI-specific companion to ISMS-POL-01. Where governance principles overlap (decision escalation, competence requirements, change control), ISMS-POL-01 takes precedence for information security governance. AI-POL-01 establishes AI-specific governance extensions and the AI Governance Officer's distinct authority.

---

## Policy Authority and Governance Boundaries

### Purpose and Scope

This policy defines **decision-making authority** for AIMS governance, ensuring:

- Clear assignment of responsibility for AI compliance interpretation
- Documented processes for applicability, exceptions, and evolution
- Competence requirements for AI governance decision-makers
- Objective criteria for audit verification

**This policy establishes:**

- Authority boundaries for AIMS decisions (Section 2: who decides what, with what competence)
- AI regulatory and control applicability authority (Section 3: who determines what applies)
- AI risk acceptance processes (Section 4: how AI risks that cannot be mitigated are handled)
- AIMS criteria change control (Section 5: how the AIMS evolves over time)
- Governance effectiveness monitoring (Section 6: how governance quality is assessed)

**This policy does NOT establish:**

- Specific AI control implementation requirements (addressed in AI-POL-A.x.x control group policies and IMPs)
- AI risk assessment methodology (addressed in AIMS Risk Assessment Procedure)
- Document control procedures (addressed in Document Control Procedure per Clause 7.5)
- Internal audit programme (addressed in Internal Audit Procedure per Clause 9.2)

**Boundary Principle**: This policy establishes **decision-making authority and processes**. The decisions themselves are documented in **AI-POL-00 (regulatory applicability), AIMS SoA (control applicability), and AI Risk Acceptance Register (risk treatment decisions)**.

**Integration with ISO/IEC 42001:2023**:

- **Clause 4.2 (Interested Parties)**: This policy formalises authority for interpreting AI regulatory requirements
- **Clause 4.3 (Scope)**: AI Governance Officer and CISO jointly recommend AIMS scope; Executive Management approves
- **Clause 5.1 (Leadership)**: Establishes decision escalation path ensuring top management commitment
- **Clause 5.2 (AI Policy)**: AI Governance Officer owns the AIMS policy suite; CISO co-owns where AI and security obligations overlap
- **Clause 5.3 (Roles)**: Defines authority assignment for all AIMS roles
- **Clause 9.3 (Management Review)**: Provides governance framework for annual AIMS review
- **Clause 10.1 (Continual Improvement)**: Enables governance process improvement through lessons learned

---

## Authority Boundaries and Competence

### Decision-Making Authority

| Authority Level | Role | Decision Scope | Competence Requirement |
|----------------|------|----------------|----------------------|
| **Primary** | AI Governance Officer | AI control design, ISO 42001/AI Act interpretation, AISIA authority, AI risk assessment process, regulatory applicability (AI-POL-00 Tier 1/2), day-to-day AIMS decisions | ISO 42001 knowledge, AI governance expertise (ISO 42001 Lead Implementer/Auditor, IAPP AI Governance Certificate or equivalent), 3+ years AI governance/risk experience, independence of AI operations |
| **Secondary** | Chief Information Security Officer (CISO) | Technical AI security measures, AI system security architecture, Annex A controls with security dimensions (A.6.2.4, A.6.2.6, A.7.4), integration with ISMS | Information security expertise (CISSP/CISM or equivalent), ISO 27001/42001 knowledge |
| **Tertiary** | Legal / Compliance Officer | Legal interpretation of AI obligations (EU AI Act, GDPR Art. 22), processor/supplier contract review, regulatory authority engagement, EU AI Act conformity assessment | Legal training, AI regulatory knowledge, access to external AI counsel |
| **Technical** | Chief Technology Officer (CTO) / AI Engineering Lead | AI system architecture decisions, lifecycle controls (A.6.x), data governance (A.7.x), technical documentation | Deep technical AI/ML expertise, responsible AI engineering practices |
| **Approval** | Executive Management (CEO/Board) | Strategic AI decisions, AIMS scope changes, resource allocation, AI risk acceptance, AI system portfolio decisions | Fiduciary responsibility for AI risk, understanding of ISO 42001 accountability obligations, budget authority |

**AI Governance Officer Independence**:

The AI Governance Officer SHALL operate with independence from AI development and deployment functions:

- Reports directly to CEO or equivalent top management
- Is not instructed by AI development teams or product management on AI governance determinations
- Has no conflict of interest — does not hold authority over AI system design decisions that would compromise governance objectivity
- Has access to all AI systems, documentation, and processes required to exercise governance duties

Where no dedicated AI Governance Officer role exists, the CISO assumes primary authority with the constraints that AI security and AI governance responsibilities are exercised independently.

**Decision Escalation Path**:

1. **Routine Decisions** (AI control design, evidence format, AIMS documentation):
   - **Authority**: AI Governance Officer
   - **Documentation**: AIMS POL/IMP documents, AISIA records
   - **Review**: Internal audit (Clause 9.2), annual management review (Clause 9.3)

2. **Regulatory Interpretation** (AI-POL-00 Tier assignments, EU AI Act classification, AI Act FRIA requirements):
   - **Authority**: AI Governance Officer determines AI applicability; CISO implements technical measures; Legal reviews legal dimensions
   - **Documentation**: AI-POL-00 Regulatory Applicability Matrix
   - **Review**: Quarterly monitoring, annual comprehensive review

3. **AI Risk Acceptance** (AI control exclusion or residual AI risk acceptance):
   - **Authority**: AI Governance Officer proposes (with AI risk assessment); Executive Management approves
   - **Documentation**: AI Risk Acceptance Register
   - **Review**: Annual management review (Clause 9.3)

4. **Strategic Changes** (AIMS scope change, AI role determination change, AI system portfolio expansion into high-risk categories):
   - **Authority**: Executive Management approval (AI Governance Officer + CISO recommend; CEO/Board decides)
   - **Documentation**: Management review records (Clause 9.3), board minutes where applicable
   - **Review**: As part of organisational strategic planning cycle

**Mandatory Requirements**:

1. The AI Governance Officer **shall** approve all AI control implementations before deployment.
2. The AI Governance Officer **shall** approve all regulatory applicability determinations (AI-POL-00 Tier assignments) before publication or update.
3. Executive Management **shall** approve all AI risk acceptance decisions per ISO 42001:2023 Clause 6.1.3.
4. The AI Governance Officer **shall** be consulted on any new AI system procurement, development, or material change — AI governance trigger. For the purpose of this policy, a **material change** is any change to an AI system's intended purpose, training methodology, data sources, output type, operating context, or deployment scope that was not foreseen in the original AISIA and risk assessment. This aligns with the EU AI Act's concept of **substantial modification** (Article 3(23)): a change that affects compliance with applicable requirements or results in a modification to the assessed intended purpose. Continuously learning system behaviour that was pre-determined by the provider at the time of the initial conformity assessment does not constitute a substantial modification.
5. Decision escalation **shall** follow the path defined above.

---

## Professional Judgment in ISO 42001:2023 Certification

### Stage 1: AIMS Design (Organisation's Responsibility)

Professional judgment exercised by the organisation includes:

1. **AI Role Determination** (provider, deployer, or both per AI system):
   - Identifying for each AI system whether the organisation acts as AI provider, deployer, or both
   - Documenting the determination per AI system in the AI System Inventory
   - Selecting applicable controls based on role — some controls apply primarily to providers (e.g., A.6.1.x, A.7.x), others to all roles
   - Documented in: AI System Inventory, AIMS SoA

2. **AIMS Scope Determination** (Clause 4.3):
   - Which AI systems are within AIMS scope
   - Whether AIMS is integrated with ISO 27001 ISMS or operated as standalone
   - Geographic and organisational boundaries
   - Documented in: AIMS Scope Document

3. **Control Selection and SoA** (Clause 6.1.3 / Annex A):
   - Selecting controls based on AI risk assessment and AISIA outcomes
   - Determining applicability of all 36 Annex A controls
   - Justifying exclusions — "not applicable to our role" or "risk does not apply" are valid exclusions; "not yet implemented" is not
   - Documented in: AIMS SoA, AI Risk Treatment Plan, AI-POL-A.x.x documents

4. **Evidence Sufficiency**:
   - Defining what evidence demonstrates control effectiveness (AISIA records, AI risk register entries, test reports, monitoring logs)
   - Determining evidence frequency and retention
   - Documented in: Control IMP documents (evidence section)

5. **AI Regulatory Applicability** (AI-POL-00):
   - Determining which AI laws apply (Tier 1/2/3 framework per AI-POL-00)
   - Assessing conditional regulation triggers (ISO 42001 certification, EU AI Act high-risk classification)
   - Documented in: AI-POL-00 Regulatory Applicability Matrix

### Stage 2: AIMS Verification (Auditor's Responsibility)

Professional judgment exercised by the auditor includes:

1. **Process Quality Assessment**:
   - Is AI risk assessment methodology sound and consistently applied?
   - Are AI role determinations (provider/deployer) reasonable given AI system portfolio?
   - Are decision-makers competent per authority table above?

2. **ISO 42001:2023 Alignment**:
   - Does organisational interpretation of Annex A controls satisfy control objectives?
   - Is the AIMS SoA complete and justified (all 36 Annex A controls documented)?
   - Are mandatory clauses (4–10) addressed?

3. **Implementation Effectiveness** (Stage 2):
   - Does actual implementation match documented design (POL → IMP → Evidence chain)?
   - Is evidence sufficient to demonstrate control operation?
   - Are nonconformities and corrective actions handled per Clause 10.2?

---

## Applicability Challenge Protocol

**Purpose**: Structured process for resolving disagreements on AI applicability determinations between organisation and auditor.

**When This Protocol Applies**:

- Auditor questions AI regulatory applicability (e.g., "Is EU AI Act high-risk classification justified?")
- Auditor challenges AI role determination for a specific AI system
- Auditor challenges control exclusion in the AIMS SoA
- Auditor believes alternative control does not achieve ISO 42001:2023 objective

**Protocol Steps**:

**Step 1 — Auditor Raises Concern**: Documents specific concern — which determination, what evidence conflicts, which ISO 42001 clause or control objective may not be satisfied.

**Step 2 — Organisation Provides Documentation**:

- For **regulatory applicability**: Assessment per AI-POL-00 methodology; trigger evaluation; AI Governance Officer + Legal approval record
- For **role determination**: AI system description; inventory entry; AI Governance Officer rationale for provider/deployer classification
- For **control exclusion**: AI risk assessment showing why risk does not apply or why control is outside organisational scope; SoA justification; organisational context

**Step 3 — Collaborative Assessment**: Organisation and auditor jointly assess whether documented rationale satisfies ISO 42001:2023 requirements. Discussion is fact-based.

**Step 4 — Resolution**:

| Outcome | Action |
|---------|--------|
| Organisation rationale accepted | Document in audit working papers; no change required |
| Gap confirmed | Organisation triggers corrective action (Clause 10.2); update SoA/AI-POL-00 as applicable |
| Disagreement unresolved | Escalate to certification body dispute resolution process |

---

## AIMS Scope Determination

### Scope Document Requirements

The AIMS Scope Document (per ISO 42001:2023 Clause 4.3) shall specify:

- **AI systems in scope**: Named AI systems with purpose, type, and deployment context
- **AI systems explicitly excluded**: With documented justification
- **Organisational units**: Which departments, functions, or legal entities are within scope
- **Geographic boundaries**: Which locations or jurisdictions are included
- **Integration with ISMS**: Whether AIMS and ISMS share processes (management review, internal audit, documented information control)

### AI System Inventory

The organisation shall maintain an AI System Inventory as a controlled document. The inventory shall include, for each AI system in scope:

| Field | Description |
|-------|-------------|
| AI System ID | Unique identifier |
| AI System Name | Common name and version |
| AI System Owner | Named responsible person |
| AI System Purpose | Intended use and deployment context |
| AI Role | Provider / Deployer / Both |
| EU AI Act Risk Classification | Prohibited / High-risk / Limited / Minimal / GPAI |
| AISIA Reference | Link to completed AISIA record |
| In AIMS Scope | Yes / No (with justification if No) |
| SoA Reference | Statement of Applicability entry |

The AI System Inventory shall be reviewed:

- At minimum annually at management review
- When a new AI system is procured or developed
- When an existing AI system is materially changed (new purpose, new population, new deployment context)
- When a change in EU AI Act classification is identified

---

## AIMS Statement of Applicability (SoA)

The organisation shall produce and maintain a Statement of Applicability per ISO 42001:2023 Clause 6.1.3. The SoA shall:

- List all 36 Annex A controls
- For each control: state whether it is applicable (Included) or not applicable (Excluded)
- For included controls: document implementation status and reference to AI-POL-A.x.x policy
- For excluded controls: document written justification — exclusion is only valid where the control genuinely does not apply given the organisation's AI role, scope, and risk assessment; "not yet implemented" does not constitute valid exclusion justification
- Be approved by the AI Governance Officer before first use
- Be reviewed annually and after material changes to AI system portfolio or regulatory requirements

---

## AIMS Change Control

**Triggers for controlled AIMS update**:

- New AI regulation enacted or significantly updated (EU AI Act delegated acts, Swiss AI law)
- New ISO standard published affecting AIMS (ISO 42006, ISO 42005 update)
- Material change to AI system portfolio (new high-risk AI system, retirement of in-scope system)
- Internal audit finding or corrective action that affects policy scope
- Management review decision

**Change process**:

1. AI Governance Officer proposes change with documented rationale
2. CISO and Legal review for security and legal dimensions
3. Executive Management approves if strategic decision (scope change, resource allocation)
4. Updated policy distributed and communicated per Clause 7.4
5. Training or awareness update triggered if change affects personnel obligations

---

## Management Review (Clause 9.3)

The AI Governance Officer shall convene or ensure an annual AIMS management review with participation from:

- Executive Management (sponsor)
- AI Governance Officer (chair)
- CISO
- Legal/Compliance Officer
- CTO / AI Engineering Lead (where AI development is in scope)
- AI System Owners (for in-scope systems)

**Mandatory agenda items** (per ISO 42001:2023 Clause 9.3.2):

1. Status of actions from previous management review
2. Changes in external/internal context affecting the AIMS
3. Changes in AI regulatory landscape (AI-POL-00 updates)
4. AI risk assessment and AISIA results
5. AIMS performance metrics (AI objectives progress, incident count/MTTR, SoA progress)
6. Internal audit results
7. Nonconformities and corrective actions
8. Resource adequacy review
9. Opportunities for continual improvement

**Management review output** (Clause 9.3.3):

Documented decisions and action items including:

- Continual improvement decisions
- AIMS scope changes
- Resource allocation decisions
- AI policy updates
- AI system portfolio decisions

Management review records shall be retained as documented evidence per Clause 7.5.

---

## Roles and Responsibilities

| Role | AIMS Governance Responsibilities |
|------|----------------------------------|
| **AI Governance Officer** | AIMS primary authority; SoA owner; AI-POL-00 owner; AISIA process owner; regulatory monitoring; management review chair; certification body liaison |
| **CISO** | Security dimensions of AI controls; ISMS/AIMS integration; technical measure oversight; A.6.2.4/A.6.2.6 security review |
| **Legal / Compliance** | AI regulatory monitoring; EU AI Act conformity assessment coordination; AI supplier contract AI clauses; supervisory authority engagement |
| **CTO / AI Engineering Lead** | A.6.x and A.7.x control implementation; AI system lifecycle documentation; technical evidence generation |
| **AI System Owners** | AI system inventory entries; AISIA completion for owned systems; operational controls; incident reporting |
| **Executive Management** | AI risk acceptance; resource allocation; AIMS scope approval; management review participation |
| **Internal Auditor** | Independent AIMS audit programme; findings reporting; corrective action verification |

---

<!-- QA_VERIFIED: [YYYY-MM-DD] -->
