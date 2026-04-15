<!-- ISMS-CORE:POLICY:AI-POL-A.9.2-4:ai:POL:a.9.2-4 -->
**AI-POL-A.9.2-4 — Responsible Use of AI Systems**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Responsible Use of AI Systems |
| **Document Type** | Policy |
| **Document ID** | AI-POL-A.9.2-4 |
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

**Review Cycle**: Annual (or upon significant change to AI system portfolio or applicable responsible use standards)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: AI Governance Officer
- Secondary: Chief Technology Officer (CTO) / Operations Lead
- Compliance: Legal / Chief Information Security Officer (CISO)
- Final Authority: Executive Management

**Related Documents**:

- AI-POL-00 (AIMS Regulatory Applicability Framework)
- AI-POL-01 (AIMS Governance and Decision-Making Framework)
- AI-POL-A.2.2-4 (AI Policy Framework — responsible AI principles)
- AI-POL-A.3.2-3 (AI Roles and Responsibilities — reporting concerns)
- AI-POL-A.5.2-5 (AI System Impact Assessment — intended use boundaries)
- AI-POL-A.6.2 (AI System Lifecycle — intended use specification A.6.2.2)
- AI-IMP-A.9.2-4-UG (Responsible Use of AI Systems — User Guide)
- AI-IMP-A.9.2-4-TG (Responsible Use of AI Systems — Technical Guide)
- ISO/IEC 42001:2023 Controls A.9.2, A.9.3, A.9.4
- ISO/IEC 42001:2023 Annex B.9 (Implementation guidance — Use of AI systems)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for the responsible use of AI systems in its operations — covering the processes that govern responsible use (A.9.2), the objectives that responsible use must achieve (A.9.3), and the enforcement of intended use boundaries (A.9.4) — in accordance with ISO/IEC 42001:2023 Controls A.9.2 through A.9.4.

**Scope**: All persons within [Organisation] who use, operate, oversee, or are responsible for AI systems within the AIMS scope; extends to third parties using AI systems operated by [Organisation] under contractual arrangements.

**Applicability Note**: A.9 controls apply to organisations in the **AI deployer** role — using AI systems in operations. They are also applicable to AI providers where the organisation itself uses the AI systems it develops.

**Purpose**: Define WHAT responsible use processes and objectives must be established and documented, and WHAT controls must be applied to enforce intended use. Implementation detail in AI-IMP-A.9.2-4-UG and AI-IMP-A.9.2-4-TG.

**Combined Control Rationale**: A.9.2 (processes), A.9.3 (objectives), and A.9.4 (intended use) are the operational counterpart to the development governance in A.6.1. Where A.6.1 governs how AI systems are built responsibly, A.9 governs how they are used responsibly once deployed. Objectives (A.9.3) set the principles; processes (A.9.2) operationalise them; intended use enforcement (A.9.4) provides the boundary control.

---

## Scope and Applicability

### ISO/IEC 42001:2023 Control Statements

**Control A.9.2 — Processes for responsible use of AI systems**
The organisation shall define and implement processes for the responsible use of AI systems.

**Control A.9.3 — Objectives for responsible use of AI systems**
The organisation shall define and document objectives for the responsible use of AI systems.

**Control A.9.4 — Intended use of AI systems**
The organisation shall define and document the intended use of AI systems and implement measures to ensure that AI systems are used for their intended purposes.

### What This Policy Covers

- Responsible use process requirements that must be in place before AI systems are used operationally
- Responsible use objectives that govern how AI is used within [Organisation]
- Intended use specification and the controls that prevent misuse or out-of-scope use

### What This Policy Does NOT Cover

- AI system development governance (addressed in AI-POL-A.6.1)
- AI system lifecycle management (addressed in AI-POL-A.6.2)
- Third-party relationships involving AI systems used by third parties on [Organisation]'s behalf (addressed in AI-POL-A.10.2-4)

### Regulatory Framework

**Tier 1: Mandatory Compliance** (per AI-POL-00):

- **EU AI Act (Regulation 2024/1689)**: Article 26 — deployer obligations, including use of high-risk AI systems only for intended purpose, human oversight, monitoring of operation, input data relevance, and log retention; Article 50 — transparency obligations when AI interacts with natural persons
- **GDPR**: Article 5(1)(b) — purpose limitation (AI systems processing personal data shall not be used for purposes incompatible with their documented purpose)

**Tier 2: Conditional** (per AI-POL-00):

- **ISO/IEC 42001:2023**: Controls A.9.2–A.9.4 — applies where AIMS certification is in scope or contractually required

**Tier 3: Informational** (per AI-POL-00):

- NIST AI RMF: GOVERN 4.x — organisational policies for responsible AI use; MANAGE 1.x — managing AI risks in operation
- OECD AI Principles: Principle 1.4 — robustness, security, and safety; Principle 1.5 — accountability

---

## Policy Statements: Processes for Responsible Use (A.9.2)

### Process Definition Requirement

[Organisation] SHALL define and implement processes that govern how AI systems are used responsibly across operations. These processes shall be operational before an AI system is placed into use, and shall be reviewed when the AI system changes or when the operational context changes.

### Required Responsible Use Processes

**1. Pre-Use Verification Process**

Before any person or function begins using an in-scope AI system operationally, the following shall be verified and documented:

- The AI system has a current, approved AISIA (AI-POL-A.5.2-5)
- The intended use for this operational context is within the documented scope of the AI system
- Relevant users have received appropriate training on the AI system, its intended use, and its limitations
- Human oversight mechanisms are in place as required by the AI system's impact classification
- Logging is active (per AI-POL-A.6.2 — A.6.2.8)

**2. Ongoing Operational Oversight Process**

During the operational use of AI systems, [Organisation] SHALL maintain:

- Monitoring of AI system performance and outputs against defined KPIs and thresholds
- Human review processes where required by the impact classification and intended use specification
- Mechanism for users to escalate concerns, unexpected outputs, or potential misuse to the AI System Owner
- Regular review of whether the operational context remains consistent with the intended use specification

**3. Misuse Detection and Response Process**

[Organisation] SHALL implement a process to detect and respond to use of AI systems outside their intended purpose:

- Monitoring for use patterns inconsistent with intended use
- Mechanism for users to report observed or suspected misuse (links to A.3.3 concerns reporting)
- Escalation path: AI System Owner → AI Risk Owner → AI Governance Officer
- Documented response options: user guidance and retraining; access restriction; AI system operational suspension pending review

**4. User Training and Awareness Process**

[Organisation] SHALL ensure that users of AI systems receive training appropriate to their role:

| User Category | Minimum Training Required |
|--------------|--------------------------|
| Operational users (direct AI output users) | Intended use and limitations; how to apply human oversight; how to report concerns; what not to use the AI system for |
| Decision-makers relying on AI outputs | How to interpret AI outputs; limitations of AI-assisted decisions; when to override AI outputs; accountability for decisions made with AI input |
| AI System Owners | All of the above; plus monitoring obligations; incident reporting; intended use boundary enforcement |
| AIMS governance roles | AIMS framework; control requirements; audit readiness |

Training shall be documented and refreshed when the AI system changes materially or when regulatory requirements change.

**5. Access Control Process**

Access to AI systems shall be controlled:

- Access granted only to persons with a legitimate operational need
- Access rights reviewed when a person's role changes or they leave the organisation
- Privileged access (administrative, training data access, model modification) subject to enhanced access control per ISMS access management controls
- Access controls documented in the AI System Resource Register (AI-POL-A.4.2-6)

---

## Policy Statements: Objectives for Responsible Use (A.9.3)

### Responsible Use Objective Requirement

[Organisation] SHALL define and document objectives for the responsible use of its AI systems. These objectives shall be established per AI system (derived from the AISIA and the intended use specification) and shall guide operational governance.

### Core Responsible Use Objectives

The following responsible use properties shall form the basis of objectives for every AI system used by [Organisation]:

**Use Within Intended Purpose**

AI systems shall be used only for the purposes for which they were designed and validated. No AI system shall be applied to a use case for which it has not been assessed and approved.

**Preservation of Human Agency**

The use of AI systems shall not undermine the ability of human decision-makers to exercise meaningful judgment. Where AI systems inform consequential decisions, human review shall be exercised — not simply deferred to the AI output. Users shall understand that accountability for decisions remains with the human decision-maker, not the AI system.

**Fairness and Non-Discrimination in Use**

AI systems shall be used in ways that do not produce discriminatory outcomes in practice, even if the system was validated for fairness at deployment. Users shall be alert to outputs that appear inconsistent across groups and report them.

**Privacy Compliance in Use**

AI systems shall not be used to process personal data in ways that exceed the purpose for which consent was obtained or the legal basis documented. Users shall not feed personal data into AI systems that were not designed and assessed for personal data processing.

**Avoidance of Harmful Use**

AI systems shall not be used in ways that could cause harm to individuals, groups, or society — including uses that, while technically possible, fall outside the intended use and could produce harmful outputs or decisions.

**Transparency to Affected Parties**

Where AI systems are used in ways that affect individuals who are not direct users, those individuals shall be informed as required by AI-POL-A.8.2-5 and applicable regulation.

### Documenting Responsible Use Objectives

Responsible use objectives shall be documented in an **AI System Responsible Use Record** per AI system, covering:

- Specific responsible use objectives for this system
- How objectives are operationalised in the deployment context
- Monitoring approach for each objective
- Responsible party for each objective

---

## Policy Statements: Intended Use of AI Systems (A.9.4)

### Intended Use Specification Requirement

[Organisation] SHALL define and document the intended use for each in-scope AI system and implement measures to ensure the system is used for its intended purposes only.

The intended use specification is established as part of the AI system specification (AI-POL-A.6.2 — A.6.2.2) and shall be reviewed with each material change to the system or its operating context.

### Intended Use Documentation

For each AI system, the intended use shall document:

| Element | Content Required |
|---------|----------------|
| **Intended use statement** | Clear, specific description of what the AI system is for, by whom, in what context, and to what end |
| **Intended users** | Who is authorised to use the AI system; competence or qualification requirements |
| **Intended operational context** | The environments, conditions, and populations for which the system was designed and validated |
| **Uses that are out of scope** | Uses that are explicitly outside the designed purpose — neither validated nor authorised |
| **Uses that are prohibited** | Uses that are specifically forbidden, including uses that could cause harm, violate rights, or breach applicable law |
| **Conditions for valid use** | Prerequisites that must be met for outputs to be valid (e.g., input data within defined parameters; qualified human oversight in place) |

### Intended Use Enforcement Measures

[Organisation] SHALL implement measures to prevent use of AI systems outside their intended purpose:

**Technical measures**:
- Access controls limiting AI system availability to authorised users and use cases
- Input validation where technically feasible (rejecting inputs outside defined parameters)
- Output filtering or flagging where AI outputs could enable prohibited uses
- Logging of use patterns enabling review for out-of-scope use

**Administrative measures**:
- User training on intended and prohibited uses (per A.9.2 training process)
- Acceptable use policy for AI systems, communicated to all users
- Monitoring of use patterns against intended use specification
- Consequences for use outside intended purpose documented and communicated

**Governance measures**:
- AI System Owner accountable for intended use compliance
- Periodic intended use compliance review as part of operational monitoring (AI-POL-A.6.2 — A.6.2.6)
- AISIA review triggered where operational use patterns diverge from the intended use specification

### Material Change to Intended Use

If the operational use of an AI system materially diverges from the documented intended use — through scope creep, new use cases, or changed operational context — this constitutes a **material change** requiring:

1. Cessation of the out-of-scope use pending assessment (or documented risk acceptance by the AI Risk Owner)
2. Updated intended use specification if the expanded use is to be authorised
3. Updated AISIA reflecting the new or expanded use
4. Updated V&V confirming the system is valid for the new intended use
5. Updated user training and documentation

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|----------------|
| **AI Governance Officer** | Own responsible use policy; approve intended use specifications; review responsible use objective records; respond to material use boundary violations |
| **AI Risk Owner** | Accept residual responsible use risks; approve use boundary exceptions under defined criteria |
| **AI System Owner** | Maintain intended use documentation for owned systems; enforce use boundaries; monitor operational use against intended use; manage user training completion |
| **Operations / Business Function Leads** | Ensure staff using AI systems are trained; enforce responsible use requirements within their function; escalate misuse or out-of-scope use to AI System Owner |
| **Users** | Use AI systems only for their intended purpose; exercise required human oversight; report concerns, errors, or suspected misuse via A.3.3 channel |
| **DPO / Privacy Officer** | Advise where AI use involves personal data; review use for GDPR purpose limitation compliance |

---

## Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Responsible use process documentation | Documented processes per A.9.2 — pre-use verification, operational oversight, misuse response, training, access control | Current + 3 years |
| Responsible use objective records | Per-AI-system documentation of responsible use objectives | Duration of system + 3 years |
| Intended use specifications | Per-AI-system intended use documentation with scope boundaries | Duration of system + 3 years |
| Training records | Evidence of user training completion for each AI system | Current + 3 years |
| Access control records | Evidence of access controls implemented and reviewed | Current + 3 years |
| Misuse / out-of-scope use records | Records of detected out-of-scope use events and responses | Duration of system + 3 years |

---

## Audit Considerations

Auditors verifying compliance with A.9.2–A.9.4 should expect to find:

- Documented responsible use processes for AI systems in operational use
- Responsible use objective records per AI system, covering the key responsible use properties
- Intended use specifications for all in-scope AI systems with clear scope and prohibited use statements
- Evidence that users are trained on intended use and limitations
- Evidence that access controls limit AI system use to authorised users
- Evidence that use patterns are monitored against intended use
- Records of how out-of-scope use events were identified and addressed

---

<!-- QA_VERIFIED: [YYYY-MM-DD] -->
