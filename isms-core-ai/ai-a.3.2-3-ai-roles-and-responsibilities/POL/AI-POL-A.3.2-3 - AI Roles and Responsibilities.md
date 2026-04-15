<!-- ISMS-CORE:POLICY:AI-POL-A.3.2-3:ai:POL:a.3.2-3 -->
**AI-POL-A.3.2-3 — AI Roles and Responsibilities**

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | AI Roles and Responsibilities |
| **Document Type** | Policy |
| **Document ID** | AI-POL-A.3.2-3 |
| **Document Creator** | AI Governance Officer / Chief Information Security Officer (CISO) |
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

**Review Cycle**: Annual (or upon significant organisational change affecting AI governance roles)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: AI Governance Officer
- Secondary: Chief Information Security Officer (CISO)
- Compliance: Legal / Compliance Officer
- Final Authority: Executive Management

**Related Documents**:

- AI-POL-00 (AIMS Regulatory Applicability Framework)
- AI-POL-01 (AIMS Governance and Decision-Making Framework)
- AI-IMP-A.3.2-3-UG (AI Roles and Responsibilities — User Guide)
- AI-IMP-A.3.2-3-TG (AI Roles and Responsibilities — Technical Guide)
- ISO/IEC 42001:2023 Controls A.3.2, A.3.3
- ISO/IEC 42001:2023 Clause 5.3 (Organisational roles, responsibilities and authorities)
- ISO/IEC 42001:2023 Annex B.3 (Implementation guidance — Internal organisation)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for defining AI governance roles and responsibilities, and for putting in place a process by which concerns about the organisation's AI activities can be reported — in accordance with ISO/IEC 42001:2023 Controls A.3.2 and A.3.3.

**Scope**: All AI systems within the AIMS scope; all roles with accountability for AI governance, development, operation, or oversight; all employees with the right and obligation to report AI-related concerns.

**Purpose**: Define WHAT AI roles must be established and documented, WHO holds accountability at each level of the AI governance hierarchy, and HOW concerns about AI systems can be raised and addressed. Implementation procedures are documented in AI-IMP-A.3.2-3-UG and AI-IMP-A.3.2-3-TG.

**Combined Control Rationale**: A.3.2 (roles and responsibilities) and A.3.3 (reporting of concerns) form the accountability foundation of the AIMS. Clear role definitions (A.3.2) create the governance structure; the concerns reporting process (A.3.3) provides the mechanism for any person to raise issues about AI system behaviour throughout its life cycle. These two controls are complementary and governed together.

---

## Scope and Applicability

### ISO/IEC 42001:2023 Control Statements

**Control A.3.2 — AI roles and responsibilities**
Roles and responsibilities for AI shall be defined and allocated according to the needs of the organisation.

**Control A.3.3 — Reporting of concerns**
The organisation shall define and put in place a process to report concerns about the organisation's role with respect to an AI system throughout its life cycle.

### What This Policy Covers

- Mandatory AIMS roles and their responsibilities
- RACI framework for AI governance
- Competence requirements per role
- Concerns reporting process — who can report, how, and what happens
- Escalation path for unresolved AI concerns

### What This Policy Does NOT Cover

- Human resource competence development actions (addressed in A.4.6 and training procedures)
- AI system-specific operational procedures (addressed in AI-POL-A.6.2)
- AIMS decision-making authority (addressed in AI-POL-01)

### Regulatory Framework

**Tier 1: Mandatory Compliance** (per AI-POL-00):

- **EU AI Act (Regulation 2024/1689)**: Article 26 (deployer obligations including human oversight designation); Article 16(l) and 25 (provider and deployer role responsibilities); Article 73 (serious incident reporting — operational responsibility)

**Tier 2: Conditional** (per AI-POL-00):

- **ISO/IEC 42001:2023**: Controls A.3.2, A.3.3 — applies where AIMS certification is in scope or contractually required

**Tier 3: Informational** (per AI-POL-00):

- NIST AI RMF: GOVERN 1.x — AI roles and responsibilities for risk management
- ISO/IEC 38507:2022: Governance of AI — governing body and management roles

---

## Policy Statements: AI Roles and Responsibilities (A.3.2)

### Role Definition Requirement

[Organisation] SHALL define, document, and communicate AI governance roles and responsibilities. All in-scope AI systems shall have named role holders. Vacancies in critical AI governance roles shall be escalated to Executive Management for timely resolution.

### Mandatory AI Governance Roles

The following roles SHALL be defined for every organisation implementing an AIMS under ISO 42001:2023:

#### AI Governance Officer

**Accountability**: Overall AIMS design, implementation, maintenance, and certification readiness

**Responsibilities**:
- Own and maintain AI-POL-00 and AI-POL-01
- Approve all AI regulatory applicability determinations
- Maintain the AIMS Statement of Applicability (SoA)
- Chair AIMS management reviews
- Coordinate internal and external AIMS audits
- Approve AISIA records before AI system deployment
- Monitor AI regulatory landscape and trigger policy updates

**Competence requirement**: ISO 42001 knowledge; AI governance experience; familiarity with EU AI Act; independence from AI operations; directly reports to CEO or equivalent

**Where role does not exist**: CISO assumes accountability with documented scope extension. The organisation shall document this arrangement in the AIMS SoA.

---

#### AI Risk Owner (per AI system)

**Accountability**: AI risk assessment and treatment decisions for a designated AI system

**Responsibilities**:
- Own and maintain the AI risk register entry for the designated AI system
- Approve residual AI risk acceptance decisions (subject to Executive Management sign-off above threshold)
- Commission and approve AISIA for the designated AI system
- Respond to AI incidents involving the designated AI system
- Ensure operational controls for the designated AI system are maintained

**Competence requirement**: Understanding of ISO 42001 risk management; business domain knowledge of the AI system's use case; authority to approve operational controls

---

#### AI System Owner

**Accountability**: Day-to-day management and documentation of a specific AI system in scope

**Responsibilities**:
- Maintain AI system inventory entry for the owned AI system
- Ensure lifecycle documentation (A.6.2 controls) is current
- Coordinate with development/engineering teams for verification and validation (A.6.2.4)
- Report AI incidents to AI Governance Officer and AI Risk Owner
- Maintain technical documentation for the AI system (A.6.2.7)
- Ensure intended use documentation is current (A.9.4)

**Competence requirement**: Technical familiarity with the AI system; business context understanding; access to AI system documentation

---

#### Data Governance Lead / Data Owner (per AI system)

**Accountability**: Data quality, provenance, and governance for data used in AI systems (A.7 controls)

**Responsibilities**:
- Approve data acquisition decisions for AI training and operation (A.7.3)
- Maintain data quality standards (A.7.4) for AI datasets
- Maintain data provenance records (A.7.5)
- Ensure data preparation processes are documented and controlled (A.7.6)
- Coordinate with Privacy Officer where AI data contains personal data

**Competence requirement**: Data governance expertise; familiarity with AI data lifecycle; understanding of data quality requirements for ML systems

---

#### AIMS Internal Auditor

**Accountability**: Independent verification of AIMS effectiveness

**Responsibilities**:
- Conduct internal AIMS audits per Clause 9.2 audit programme
- Report findings to AI Governance Officer and Executive Management
- Verify corrective action effectiveness
- Maintain audit records

**Competence requirement**: ISO 42001 auditor training; independence from audited functions (cannot audit own work); audit methodology skills

---

#### All Employees and Contractors

**Accountability**: Compliance with AI Policy and responsible use obligations

**Responsibilities**:
- Comply with the AI Policy and applicable AI-POL-A.9.x obligations
- Use AI systems only for documented intended purposes (A.9.4)
- Report AI-related concerns via the process defined in A.3.3 (below)
- Complete AI awareness training as assigned

---

### RACI Framework

The organisation shall maintain an AI RACI matrix in the AIMS documentation. At minimum it shall assign Responsible, Accountable, Consulted, and Informed designations for:

- AI risk assessment (per AI system)
- AISIA (per AI system)
- AI system deployment approval
- AI incident response
- AI policy review
- AIMS internal audit
- Management review
- SoA maintenance
- AI supplier assessment (A.10.3)

---

## Policy Statements: Reporting of Concerns (A.3.3)

### Concerns Reporting Requirement

[Organisation] SHALL establish and communicate a process by which any person — employee, contractor, partner, or customer — can report concerns about the organisation's role with respect to an AI system throughout its life cycle.

### What Can Be Reported

Concerns reportable under this process include, but are not limited to:

- Observed or suspected AI system behaviour inconsistent with its documented intended purpose
- Potential bias, unfairness, or discriminatory outputs from an AI system
- AI system outputs that may harm individuals or specific groups
- Suspected privacy violations involving AI processing of personal data
- AI system decisions that lack adequate human oversight
- Concerns about AI supply chain integrity (e.g., undisclosed AI components in third-party services)
- Concerns about the adequacy of transparency disclosures to AI-affected individuals
- Violations of the AI Policy or applicable AI-POL-A.x.x policies
- Misuse of AI systems outside their intended purpose

### Who Can Report

Any person with knowledge of a concern related to an AI system shall be entitled and encouraged to use this process:

- All employees (permanent, temporary, contract)
- Third-party contractors and consultants with access to AI systems
- Customers and partners who interact with the organisation's AI systems
- Members of the public affected by AI-driven decisions

### How to Report

Reports may be submitted through:

- **Direct escalation**: To the AI Governance Officer, AI System Owner, or AI Risk Owner
- **CISO / Information Security team**: Where the concern involves security dimensions of AI systems
- **Ethics / Compliance hotline**: Where the organisation operates one, AI concerns are within scope
- **Anonymous channel**: The organisation shall ensure at minimum one anonymous reporting pathway is available for AI concerns

### What Happens After Reporting

1. **Acknowledgement**: Reports shall be acknowledged within [Organisation-specific timeframe, e.g., 5 business days]
2. **Initial triage**: AI Governance Officer or designated deputy assesses severity and route
3. **Investigation**: AI System Owner and AI Risk Owner investigate; CISO involved where security dimension exists
4. **Response**: Outcome communicated to reporter (where identity is known) within [Organisation-specific timeframe]
5. **Escalation**: Concerns involving potential EU AI Act serious incidents (Article 73) are escalated to Legal/Compliance for regulatory reporting assessment
6. **Non-retaliation**: No person shall be penalised, dismissed, or disadvantaged for making a good-faith report of an AI concern

### Tracking and Review

All concerns received shall be logged in the AI Concerns Register maintained by the AI Governance Officer. The register shall be reviewed at each AIMS management review for patterns, systemic issues, and corrective action outcomes.

---

## Roles and Responsibilities

| Role | Responsibilities for A.3.2–A.3.3 |
|------|----------------------------------|
| **AI Governance Officer** | Maintain role definitions; ensure all in-scope AI systems have named role holders; own and operate the concerns reporting process; review Concerns Register quarterly |
| **Executive Management** | Approve RACI framework; ensure adequate resourcing of AI governance roles; receive escalated concerns |
| **HR** | Reflect AI governance roles in job descriptions; support annual competence assessment |
| **CISO** | Ensure AI security roles are aligned with ISMS role structure |
| **All Managers** | Ensure their teams are aware of AI governance roles and the concerns reporting process |

---

## Evidence Requirements

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Role definitions document | Formal descriptions of all AIMS roles with responsibilities and competence requirements | Current + 3 years |
| Role assignment records | Named individuals assigned to each AIMS role per AI system | Current + 3 years |
| RACI matrix | Current RACI for AIMS activities | Current + 3 years |
| AI Concerns Register | Log of all concerns received, triage outcome, investigation, resolution | Current + 5 years |
| Non-retaliation acknowledgement | Evidence that reporters are protected from retaliation | Current + 3 years |

---

## Audit Considerations

Auditors verifying compliance with A.3.2–A.3.3 should expect to find:

- Documented AIMS roles with named holders for each in-scope AI system
- RACI matrix covering key AIMS activities
- Evidence of competence assessment for AI governance role holders
- Documented concerns reporting process communicated to employees
- AI Concerns Register with logged entries (or documented evidence of no concerns received) and outcomes
- Evidence that concerns reporters are protected from retaliation

---

<!-- QA_VERIFIED: [YYYY-MM-DD] -->
