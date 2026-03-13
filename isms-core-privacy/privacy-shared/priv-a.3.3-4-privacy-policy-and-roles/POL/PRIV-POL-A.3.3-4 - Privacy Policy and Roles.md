<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.3-4:privacy:POL:a.3.3-4 -->
**PRIV-POL-A.3.3-4 — Privacy Policy and Roles**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Privacy Policy and Roles |
| **Document Type** | Policy |
| **Document ID** | PRIV-POL-A.3.3-4 |
| **Document Creator** | Data Protection Officer (DPO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |
| **Privacy Product Version** | 1.0 |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | DPO | Initial policy for ISO/IEC 27701:2025 first certification |

**Review Cycle**: Annual (or upon significant regulatory or organisational change)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Data Protection Officer (DPO)
- Secondary: Chief Information Security Officer (CISO)
- Legal: Legal/Compliance Officer
- Final Authority: Executive Management

**Related Documents**:

- PRIV-POL-00 (Privacy Regulatory Applicability Framework)
- PRIV-POL-01 (Privacy Governance and Decision-Making Framework)
- PRIV-IMP-A.3.3-4-UG (Privacy Policy and Roles — User Guide)
- PRIV-IMP-A.3.3-4-TG (Privacy Policy and Roles — Technical Guide)
- ISMS-POL-A.5.1-2-6.1-2 (Secure Employment and Roles — ISMS parallel)
- ISO/IEC 27701:2025 Controls A.3.3, A.3.4
- ISO/IEC 27701:2025 Annex B (Implementation guidance B.3.3, B.3.4)
- GDPR Article 24 (Controller responsibilities), Article 28 (Processor obligations)
- CH FADP Article 7 (Data security)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for information security policies and role definitions as they relate to the processing of Personally Identifiable Information (PII), in accordance with ISO/IEC 27701:2025 Controls A.3.3 and A.3.4.

**Scope**: All personnel and relevant interested parties involved in PII processing; all information security policies that govern PII processing; all organisational roles with responsibilities for PII processing security.

**Purpose**: Define organisational requirements for:

- PII-scoped information security policy governance (A.3.3)
- Privacy and security role definition and accountability for PII processing (A.3.4)

This policy establishes **WHAT** policy governance structures are required, **WHO** holds privacy and security responsibilities for PII processing, and **WHEN** reviews and updates occur. Implementation procedures (**HOW**) are documented in PRIV-IMP-A.3.3-4-UG and PRIV-IMP-A.3.3-4-TG.

**Role Applicability**: This policy applies to the organisation acting as **both PII Controller and PII Processor**. Controls A.3.3 and A.3.4 are shared controls (Table A.3) and apply regardless of processing role.

**Combined Control Rationale**: A.3.3 (policies) and A.3.4 (roles) form the foundational governance pair for PII processing security. Policies without role accountability are unenforceable; roles without governing policies are undefined. They are implemented together as a unified governance layer.

---

# Scope and Applicability

## ISO/IEC 27701:2025 Control Statements

**Control A.3.3 — Policies for information security**
> *Information security policies related to PII processing shall be defined, approved by management, published, communicated to and acknowledged by relevant personnel and relevant interested parties, and reviewed at planned intervals and if significant changes occur.*

**Control A.3.4 — Information security roles and responsibilities**
> *Information security roles and responsibilities related to PII processing shall be defined and allocated according to the organisational needs.*

## What This Policy Covers

**Personnel and Interested Parties**:

- All employees, contractors, and third parties with access to PII or PII processing systems
- PII processors engaged by the organisation (as relevant interested parties)
- Executive Management and Board members with oversight of PII processing

**Policies**:

- All information security policies that govern, directly or indirectly, the security of PII processing
- Topic-specific policies addressing PII processing controls (this policy series: PRIV-POL-A.x.x)
- The PIMS policy framework (PRIV-POL-00, PRIV-POL-01, and all 21 control group POLs)

**Roles**:

- Roles with explicit privacy responsibility (DPO, Privacy Champions, Data Owners)
- Roles with PII processing security responsibility (CISO, Security Team, System Owners)
- All personnel roles (general awareness obligations for PII processing)

## What This Policy Does NOT Cover

- Policy templates and authoring procedures (see PRIV-IMP-A.3.3-4-UG)
- Role description templates and assignment procedures (see PRIV-IMP-A.3.3-4-TG)
- Detailed training and awareness procedures (see PRIV-POL-A.3.17-19)
- Personnel screening and employment terms (see ISMS-POL-A.5.1-2-6.1-2)
- Privacy risk assessment procedures (see PRIV-POL-01 and PRIV-IMP risk documentation)

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 24 (controller accountability for TOMs); Article 32 (security of processing); Article 37–39 (DPO obligations); Article 28 (processor security obligations)
- **CH FADP**: Article 7 (technical and organisational security measures); Article 8 (processor agreements including role clarity)
- **ISO/IEC 27701:2025**: Controls A.3.3, A.3.4 (normative)

**Tier 2: Conditional Applicability** (per PRIV-POL-00):

- **ISO/IEC 27018:2025**: Annex A — processor role requirements where cloud PII processing in scope

**Tier 3: Informational Reference** (per PRIV-POL-00):

- **ISO/IEC 27002:2022**: Implementation guidance for policy governance and role definitions
- **ISO/IEC 27701:2025 Annex B**: Implementation guidance B.3.3 (policy governance), B.3.4 (role definitions)

For complete regulatory categorisation, refer to PRIV-POL-00.

---

# Policy Statements: PII-Scoped Information Security Policies (A.3.3)

## Policy Governance Requirements

[Organisation] SHALL maintain an information security policy framework that explicitly addresses the security of PII processing.

### Policy Scope Requirement

All information security policies that govern systems, processes, or personnel involved in PII processing SHALL include explicit reference to PII processing obligations. Where an existing information security policy (from the ISMS framework) does not address PII-specific requirements, a supplementary PIMS policy SHALL be established to address the gap.

### Policy Lifecycle Requirements

PII-scoped information security policies SHALL be managed through the following lifecycle stages:

**Definition**: Policies defined using the PIMS policy framework established in PRIV-POL-01. Each policy SHALL address at minimum: purpose, scope, policy statements (WHAT), responsible roles (WHO), and reference documents (WITH WHAT).

**Approval**: Policies approved by the Data Protection Officer (DPO) as primary authority, with co-approval by CISO for technical policies. Final authority: Executive Management.

**Publication**: Policies published to the organisational PIMS document repository with version control. Published versions SHALL be accessible to all relevant personnel and interested parties.

**Communication**: PII-scoped policies SHALL be communicated to:
- All personnel with access to PII or PII processing systems
- Relevant PII processors (as applicable under processor agreements)
- Relevant interested parties (supervisory authorities and certification bodies — made available upon request)

**Acknowledgment**: Personnel with access to PII or PII processing systems SHALL acknowledge receipt and understanding of applicable PIMS policies. Acknowledgment records SHALL be maintained in the Personnel Privacy Training and Acknowledgment Register.

**Review**: PII-scoped policies SHALL be reviewed:
- At planned intervals (minimum annually)
- Upon significant regulatory change affecting PII processing obligations
- Following a material privacy incident (including personal data breach)
- Upon significant change to PII processing activities (new processing, new system, new data category)
- Upon publication of new DPA guidance materially affecting policy content
- Upon publication of a new edition of ISO/IEC 27701 or applicable regulatory standard

**Retirement**: Retired policies SHALL be archived with full audit trail for minimum 3 years.

### Policy Hierarchy

| Tier | Type | Approval Authority | Review Frequency |
|------|------|-------------------|------------------|
| 1 | PIMS Foundation (PRIV-POL-00, PRIV-POL-01) | Executive Management | Annual |
| 2 | Control Group Policies (21 PRIV-POL-A.x.x) | DPO | Annual |
| 3 | Implementation Guides (UG/TG per control group) | DPO + CISO | Annual or on change |
| 4 | Operational Procedures and Work Instructions | Process Owner (DPO oversight) | Semi-annual or on change |

Lower-tier documents SHALL NOT contradict higher-tier policies. All tiers SHALL be accessible to relevant personnel.

---

# Policy Statements: Privacy and Security Roles for PII Processing (A.3.4)

## Role Definition Requirements

[Organisation] SHALL define and allocate information security roles and responsibilities as they relate to PII processing, covering privacy-specific roles and security roles with PII processing relevance.

### Mandatory Privacy Roles

The following roles SHALL be defined and assigned:

| Role | Responsibility | Appointment Basis |
|------|---------------|------------------|
| **Data Protection Officer (DPO)** | Primary accountability for PIMS; regulatory interface; DPIA authority; data subject rights oversight; privacy policy ownership | GDPR Article 37 (mandatory where applicable); FADP (recommended); appointed in writing with independence per GDPR Article 38 |
| **Privacy Champion** (per business unit or processing domain) | First-line privacy support; escalation to DPO; privacy awareness facilitation within their domain | Appointed by DPO in consultation with business unit management |
| **Data Owner** (per processing activity or data category) | Accountable for the PII within their domain; approves access; participates in DPIA; ensures accuracy | Appointed by Executive Management on recommendation of DPO |
| **PIMS Internal Auditor** | Independent audit of PIMS effectiveness; reports to Executive Management | Appointed per Clause 9.2; must be independent from audited activities |

### Security Roles with PII Processing Responsibility

The following information security roles SHALL have explicitly documented PII processing responsibilities within their role definition:

| Role | PII Processing Responsibility |
|------|------------------------------|
| **Chief Information Security Officer (CISO)** | Technical and organisational security measures (TOMs) for PII processing; A.3 shared security controls; security architecture decisions affecting PII |
| **System Owner** (for systems processing PII) | Ensuring technical controls for PII are implemented and maintained on their systems; participating in DPIAs for their systems |
| **IT Security Team** | Implementation of technical security controls for PII processing environments; security monitoring covering PII systems |
| **Development / DevOps Teams** | Privacy by design in system development; security controls in PII processing code and infrastructure |

### Role Allocation Principles

Roles SHALL be allocated according to organisational needs with the following principles:

1. **No role conflicts**: The DPO SHALL NOT hold a role that determines purposes and means of PII processing (per GDPR Article 38.6)
2. **Clear accountability**: Each PII processing activity SHALL have an identified Data Owner
3. **Proportionality**: Role scope and depth of responsibility SHALL be proportionate to the volume, sensitivity, and risk of PII processing activities
4. **Documentation**: All role assignments SHALL be documented and maintained in the Privacy Roles Register
5. **Currency**: Role assignments SHALL be reviewed at least annually and upon organisational change

### Role Documentation Requirements

For each defined privacy and security role, the following SHALL be documented:

- Role title and unique identifier
- Responsibilities related to PII processing (specific, not generic)
- Authority scope (what decisions the role can make)
- Reporting line and escalation path
- Competence requirements (qualifications, training, experience)
- Incumbent name and appointment date
- Review date

Role documentation is maintained in the Privacy Roles Register (see PRIV-IMP-A.3.3-4-TG for register structure and maintenance procedures).

---

# Evidence Requirements

The following evidence demonstrates operation of this policy:

| Evidence | Description | Retention |
|---------|-------------|-----------|
| PIMS Policy Register | List of all current PIMS policies with version, approval date, next review date, and owner | 3 years |
| Policy Approval Records | DPO + Executive Management approval signatures per policy | 3 years |
| Policy Acknowledgment Register | Personnel acknowledgment records per policy per person | Duration of employment + 3 years |
| Privacy Roles Register | Documented role assignments with incumbent, responsibilities, appointment date | Duration of role + 3 years |
| DPO Appointment Record | Written DPO appointment with independence statement | Duration of appointment + 3 years |
| DPO Role Conflict Assessment | Annual documented assessment confirming no DPO role conflicts per GDPR Article 38.6 | Duration of appointment + 3 years |
| Policy Review Records | Evidence of annual review (or trigger-based review) per policy | 3 years |
| Communication Records | Evidence of policy communication to relevant personnel and interested parties | 3 years |

---

# Audit Considerations

Auditors verifying compliance with A.3.3 and A.3.4 should expect to find:

**For A.3.3 (Policies)**:
- A complete and current PIMS policy register
- Policies covering all in-scope PII processing activities
- Evidence of management approval for current policy versions
- Evidence of communication and acknowledgment by relevant personnel
- Records of policy review at planned intervals or upon trigger events

**For A.3.4 (Roles)**:
- A documented Privacy Roles Register with all mandatory roles assigned
- DPO appointment letter with independence confirmation
- Role descriptions including PII processing responsibilities
- No role conflicts for DPO (documented assessment)
- Evidence of role review and currency

---

<!-- QA_VERIFIED: [Date] -->
