<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.8-10:privacy:POL:a.3.8-10 -->
**PRIV-POL-A.3.8-10 — Identity, Access and Supplier Controls**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Identity, Access and Supplier Controls |
| **Document Type** | Policy |
| **Document ID** | PRIV-POL-A.3.8-10 |
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
- PRIV-IMP-A.3.8-10-UG (Identity, Access and Supplier Controls — User Guide)
- PRIV-IMP-A.3.8-10-TG (Identity, Access and Supplier Controls — Technical Guide)
- ISMS-POL-A.5.15-16-18 (Identity and Access Management — ISMS parallel)
- ISMS-POL-A.5.19-23 (Cloud Services and Supplier Relationships — ISMS parallel)
- ISO/IEC 27701:2025 Controls A.3.8, A.3.9, A.3.10
- ISO/IEC 27701:2025 Annex B (Implementation guidance B.3.8, B.3.9, B.3.10)
- GDPR Article 25 (Data protection by design and by default); Article 28 (Processor obligations); Article 32 (Security of processing)
- CH FADP Article 7 (Data security); Article 9 (Processor agreements)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for identity lifecycle management, access rights governance, and information security obligations in supplier agreements as they relate to the processing of Personally Identifiable Information (PII), in accordance with ISO/IEC 27701:2025 Controls A.3.8, A.3.9, and A.3.10.

**Scope**: All identities used to access PII or PII processing systems; all access rights to PII and associated assets; all supplier relationships where information security requirements for PII processing apply.

**Purpose**: Define organisational requirements for:

- Full lifecycle management of identities related to PII processing (A.3.8)
- Provisioning, review, modification, and removal of access rights to PII and associated assets (A.3.9)
- Establishing and agreeing information security requirements for PII processing with each supplier (A.3.10)

This policy establishes **WHAT** identity lifecycle, access rights, and supplier security requirements apply to PII, **WHO** holds accountability for these controls, and **WHEN** reviews and updates occur. Implementation procedures (**HOW**) are documented in PRIV-IMP-A.3.8-10-UG and PRIV-IMP-A.3.8-10-TG.

**Role Applicability**: This policy applies to the organisation acting as **both PII Controller and PII Processor**. Controls A.3.8, A.3.9, and A.3.10 are shared controls (Table A.3) and apply regardless of processing role.

**Combined Control Rationale**: A.3.8 (identity lifecycle), A.3.9 (access rights), and A.3.10 (supplier security) form the access governance triad for PII protection. Identities create the actors; access rights determine what they can reach; supplier agreements extend these controls to the supply chain. They are implemented together as an integrated access and supply chain governance layer over PII processing.

---

# Scope and Applicability

## ISO/IEC 27701:2025 Control Statements

**Control A.3.8 — Identity management**
Control A.3.8 requires [Organisation] to manage the full lifecycle of all identities that have a relationship to PII processing — covering provisioning, modification, suspension, and decommissioning of both human and non-human identities.

**Control A.3.9 — Access rights**
Control A.3.9 requires [Organisation] to provision, review, modify, and remove access rights to PII and other associated assets in accordance with its topic-specific access control policy and rules.

**Control A.3.10 — Addressing information security within supplier agreements**
Control A.3.10 requires [Organisation] to establish and agree relevant information security requirements for PII processing with each supplier, calibrated to the type of supplier relationship.

## What This Policy Covers

**Identities (A.3.8)**:

- All human identities (employee accounts, contractor accounts, temporary worker accounts) used to access PII or systems that process PII
- Non-human identities (service accounts, application accounts, automated processing accounts) used in PII processing pipelines
- Privileged identities with elevated access to PII processing environments or PII data stores
- Identity lifecycle stages: provisioning, modification, suspension, reactivation, and decommissioning

**Access Rights (A.3.9)**:

- Access rights to PII data stores, databases, and repositories
- Access rights to applications and systems that process PII
- Access rights to PII processing infrastructure (servers, cloud environments, processing platforms)
- Associated asset access rights where those assets support PII processing (e.g., backup systems, logging platforms, key management systems)

**Supplier Security (A.3.10)**:

- All suppliers who process PII on behalf of [Organisation] (PII processors)
- All suppliers who have access to PII or PII processing systems as part of their service delivery (e.g., IT support, managed services, SaaS providers)
- Information security requirements for PII processing that must be established and agreed in supplier agreements
- Supplier type differentiation for requirements proportionality

## What This Policy Does NOT Cover

- Identity provisioning workflows and tooling (see PRIV-IMP-A.3.8-10-TG)
- Access control technical configuration (see PRIV-IMP-A.3.8-10-TG)
- Supplier due diligence and selection procedures (see PRIV-POL-A.2.2.2-7 for processor-specific controls)
- Supplier monitoring and performance management (see ISMS-POL-A.5.19-23)
- Confidentiality and non-disclosure agreement requirements (see PRIV-POL-A.3.17-19)
- Authentication technology requirements (see PRIV-POL-A.3.23-31)

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 25 (access control as a data protection by design measure); Article 28 (processor contracts must include adequate security obligations); Article 32 (appropriate technical measures including access controls); Article 5(1)(f) (integrity and confidentiality principle)
- **CH FADP**: Article 7 (technical and organisational security measures); Article 9 (processor agreements must provide equivalent data protection)
- **ISO/IEC 27701:2025**: Controls A.3.8, A.3.9, A.3.10 (normative)

**Tier 2: Conditional Applicability** (per PRIV-POL-00):

- **ISO/IEC 27018:2025**: Annex A — supplier and sub-processor disclosure requirements (A.2.5.7–A.2.5.9) where cloud PII processing in scope

**Tier 3: Informational Reference** (per PRIV-POL-00):

- **ISO/IEC 27002:2022**: Implementation guidance for identity management (5.15–5.18), access control (5.15), and supplier relationships (5.19–5.21)
- **ISO/IEC 27701:2025 Annex B**: Implementation guidance B.3.8, B.3.9, B.3.10

For complete regulatory categorisation, refer to PRIV-POL-00.

---

# Policy Statements: Identity Lifecycle Management for PII Processing (A.3.8)

## Identity Lifecycle Requirements

[Organisation] SHALL manage the full lifecycle of all identities that have access to PII or PII processing systems. Identity lifecycle management for PII SHALL be consistent with and extend the ISMS identity management requirements (ISMS-POL-A.5.15-16-18) with the additional PII-specific requirements defined in this policy.

### Identity Provisioning for PII Access

Identities granted access to PII or PII processing systems SHALL be provisioned on the following basis:

- **Documented business purpose**: A documented and approved business justification for PII access must exist before provisioning
- **Role alignment**: Access SHALL be aligned to the role's documented PII processing responsibilities; access to PII not required for the role SHALL NOT be provisioned
- **Minimum privilege**: Identities SHALL be provisioned with the minimum level of access necessary for the documented purpose (principle of minimum necessary processing, consistent with GDPR Article 5(1)(c) data minimisation)
- **Approval authority**: PII access provisioning SHALL require approval from the Data Owner for the relevant PII dataset, or from the DPO where no Data Owner is assigned

### Identity Modification and Suspension

Where a role changes, an individual transfers to a different function, or circumstances change such that a previously justified PII access purpose no longer applies:

- PII access rights SHALL be modified or suspended within the timeframe specified in PRIV-IMP-A.3.8-10-TG
- Notification of role changes SHALL be provided by line management to the IT Security Team and documented
- Suspension (not immediate deletion) SHALL apply where a legal hold or investigation requires preservation of identity records

### Identity Decommissioning

When an individual's employment or engagement ends, or a service account's purpose is terminated:

- PII access rights SHALL be removed on or before the last day of access (employee departure, contract end)
- Identity decommissioning records SHALL be retained for 3 years from the date of decommissioning, to support audit and investigation
- Where decommissioning is delayed for technical reasons, access SHALL be suspended immediately and decommissioning completed within 5 business days
- To ensure timely decommissioning where HR notification is not received, IT Security SHALL perform a monthly reconciliation of active identities with PII access against current HR records; any identity without a current active employment or engagement record SHALL be suspended pending DPO confirmation

### Non-Human Identity Management

Service accounts, application accounts, and automated processing accounts used in PII processing pipelines SHALL be:

- Individually identified and registered in the Identity Register
- Assigned an accountable human owner (responsible for managing the service account lifecycle)
- Subject to periodic review (minimum annually) to confirm continued necessity
- Decommissioned when the processing purpose they support is discontinued

---

# Policy Statements: Access Rights to PII and Associated Assets (A.3.9)

## Access Rights Requirements

[Organisation] SHALL ensure that access rights to PII and associated assets are provisioned, reviewed, modified, and removed in accordance with the ISMS access control policy (ISMS-POL-A.5.15-16-18) and the PII-specific extensions defined in this policy.

### PII Access Rights Principles

Access rights to PII SHALL be governed by:

1. **Minimum necessary access**: Access granted shall be limited to the minimum PII and associated assets required to fulfil the documented processing purpose
2. **Need-to-process**: Access is only granted where there is a documented and current need to process the specific PII
3. **Segregation of duties**: Where PII processing involves high-risk operations (deletion, export, bulk access), segregation of duties controls SHALL be implemented to prevent single-actor abuse. The minimum standard is that no single identity may both initiate and approve a high-risk PII operation
4. **Time-limited access**: Where access is granted for a specific project, task, or temporary purpose, access rights SHALL be time-limited and automatically reviewed at expiry

### Access Rights Review for PII

Access rights to PII and PII processing systems SHALL be reviewed:

- **At minimum annually** for all access rights (formal certification)
- **Upon role change** for the affected individual
- **Upon organisational change** (restructuring, business unit changes) that affects processing purposes
- **Following a privacy incident** that involved unauthorised or inappropriate access to PII
- **Upon Data Owner request** for the relevant PII dataset

Access rights reviews SHALL be documented. Rights confirmed as no longer necessary SHALL be removed within 5 business days for standard access and immediately for privileged access. Review records SHALL be maintained as evidence.

### Privileged Access to PII

Privileged access to PII processing systems (administrative access, bulk data access, database administrator rights, backup and recovery access) requires:

- Explicit DPO notification and Data Owner approval before granting
- Separate privileged identity (not combined with standard user identity)
- Enhanced audit logging of privileged session activity involving PII
- More frequent periodic review (minimum every 6 months)
- Immediate revocation upon any indication of misuse

### Access Rights Register

[Organisation] SHALL maintain an Access Rights Register for PII that documents:

- Identities with access to PII, by dataset and system
- Access level and scope granted
- Approval basis and approver identity
- Date granted and date of last review
- Expiry date (where time-limited)

The Access Rights Register is maintained by the IT Security Team with DPO oversight. Structure and maintenance procedures are defined in PRIV-IMP-A.3.8-10-TG.

---

# Policy Statements: Information Security in Supplier Agreements (A.3.10)

## Supplier Security Requirements for PII

[Organisation] SHALL establish and agree relevant information security requirements related to PII processing with each supplier, proportionate to the type of supplier relationship.

### Supplier Categorisation for PII Requirements

Suppliers are categorised by their relationship to PII processing to determine applicable requirements:

| Supplier Category | Description | Minimum Requirements |
|------------------|-------------|---------------------|
| **PII Processor** | Processes PII directly on behalf of [Organisation] under instruction | Full processor agreement per GDPR Article 28 / CH FADP Article 9 + PII security schedule |
| **PII-Adjacent Supplier** | Has access to systems or environments containing PII as part of service delivery (e.g., IT managed services, cloud infrastructure, maintenance) | Confidentiality obligation + data handling restrictions + incident notification obligation |
| **No PII Access** | Provides services with no access to PII or PII processing systems | Standard supplier security terms (ISMS-POL-A.5.19-23) — no PII-specific addendum required |

### Mandatory PII Security Requirements in Supplier Agreements

For PII Processor and PII-Adjacent Supplier categories, the following information security requirements related to PII processing SHALL be established and agreed in the supplier agreement:

**Security obligations**:

- Commitment to implement and maintain appropriate technical and organisational security measures for PII, no less protective than [Organisation]'s own requirements
- Obligation to process PII only as instructed by [Organisation] (for processors)
- Prohibition on using PII for the supplier's own purposes

**Confidentiality**:

- Personnel of the supplier with access to PII are bound by confidentiality obligations
- Confidentiality obligations survive termination of the agreement

**Incident notification**:

- Obligation to notify [Organisation] of any actual or suspected PII security incident within the timeframe specified in the agreement (aligned to regulatory notification windows — maximum 24 hours where personal data breach risk exists)
- Cooperation in investigation and remediation

**Sub-processor / subcontractor control**:

- Prior written consent required before engaging sub-processors with access to [Organisation]'s PII
- Flow-down of equivalent security obligations to any sub-processor

**Audit rights**:

- [Organisation]'s right to audit or assess the supplier's PII security measures, or to receive third-party audit reports (e.g., ISO 27001 certification, SOC 2 Type II)

**Return and deletion**:

- Upon termination or on request, the supplier SHALL return or securely delete all PII, and confirm deletion in writing

**Regulatory compliance**:

- Supplier acknowledges the applicable regulatory framework (GDPR, CH FADP) and commits to compliance in their processing activities

### Supplier Agreement Review

PII-related supplier agreements SHALL be reviewed:

- At minimum annually, or upon contract renewal
- Upon material change to the nature of PII processed by the supplier
- Following a security incident involving the supplier
- Upon significant change to applicable regulatory requirements
- Upon notification of a change to the supplier's sub-processor arrangements

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Responsibilities for A.3.8–A.3.10 |
|------|-----------------------------------|
| **Data Protection Officer (DPO)** | Approves privileged PII access; maintains oversight of Access Rights Register; approves PII-relevant supplier agreements; reviews supplier categorisation decisions; maintains Processor Agreement Register |
| **Data Owner** | Approves PII access provisioning for their dataset; conducts or oversees periodic access rights reviews; escalates unauthorised access to DPO and CISO |
| **CISO** | Defines identity lifecycle and access control technical requirements; ensures ISMS identity management extends to PII per this policy; reviews supplier security schedules for technical adequacy |
| **IT Security Team** | Maintains the Identity Register and Access Rights Register; executes access provisioning and decommissioning; conducts access rights reviews; implements privileged access controls |
| **Legal/Compliance** | Reviews supplier agreement PII security clauses; advises on Article 28 processor contract requirements; maintains awareness of applicable regulatory changes |
| **Procurement / Supplier Management** | Ensures PII supplier categorisation is performed before agreement signature; engages Legal/DPO for PII-relevant agreements; maintains supplier agreement inventory |
| **Line Management** | Notifies IT Security Team of role changes and departures; approves PII access requests for their team members |

---

# Evidence Requirements

The following evidence demonstrates operation of this policy:

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Identity Register | All identities (human and non-human) with PII access, including lifecycle status | Current + 3 years |
| Access Rights Register | PII access rights by identity, dataset, and system; approval and review records | Current + 3 years |
| Access Rights Review Records | Documented evidence of periodic access rights certification, including removed rights | 3 years from the date of the review |
| Supplier Agreement Inventory | List of all supplier agreements with PII categorisation and PII security clause reference | Current + 3 years |
| Supplier Agreement Copies | Signed agreements (or agreement schedules) containing PII security obligations | Duration of agreement + 3 years |
| Privileged Access Approval Records | DPO notifications and Data Owner approvals for privileged PII access | 3 years from the date access was revoked |
| Identity Decommissioning Records | Evidence of timely access removal upon departure or role change | 3 years from the date of decommissioning |

---

# Audit Considerations

Auditors verifying compliance with A.3.8, A.3.9, and A.3.10 should expect to find:

**For A.3.8 (Identity management)**:
- Identity Register covering all human and non-human identities with PII access
- Evidence of documented approval for PII access provisioning
- Records of identity decommissioning on departure or role change
- Periodic review records for non-human identities

**For A.3.9 (Access rights)**:
- Access Rights Register for PII with current access rights documented
- Evidence of periodic access rights reviews (minimum annual)
- Records of access modification or removal following role changes
- Privileged access approval and review records
- Segregation of duties evidence for high-risk PII operations

**For A.3.10 (Supplier agreements)**:
- Supplier categorisation records (PII Processor / PII-Adjacent / No PII Access)
- Signed supplier agreements containing PII information security requirements
- Evidence of annual review or trigger-based review of PII supplier agreements
- Sub-processor approval records and flow-down confirmation

---

<!-- QA_VERIFIED: [Date] -->
