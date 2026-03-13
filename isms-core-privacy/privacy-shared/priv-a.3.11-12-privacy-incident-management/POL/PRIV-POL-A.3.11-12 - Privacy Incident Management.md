<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.11-12:privacy:POL:a.3.11-12 -->
**PRIV-POL-A.3.11-12 — Privacy Incident Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Privacy Incident Management |
| **Document Type** | Policy |
| **Document ID** | PRIV-POL-A.3.11-12 |
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
- PRIV-IMP-A.3.11-12-UG (Privacy Incident Management — User Guide)
- PRIV-IMP-A.3.11-12-TG (Privacy Incident Management — Technical Guide)
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle — ISMS parallel)
- ISMS-POL-A.6.8 (Information Security Event Reporting — ISMS parallel)
- ISO/IEC 27701:2025 Controls A.3.11, A.3.12
- ISO/IEC 27701:2025 Annex B (Implementation guidance B.3.11, B.3.12)
- GDPR Article 33 (Notification to supervisory authority); Article 34 (Communication to data subject)
- CH FADP Article 24 (Notification of data security breaches)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for planning, preparing, and responding to information security incidents related to PII processing, in accordance with ISO/IEC 27701:2025 Controls A.3.11 and A.3.12.

**Scope**: All information security incidents that involve, affect, or could affect the confidentiality, integrity, or availability of PII processed by [Organisation]; all personnel with roles in privacy incident detection, escalation, management, or notification.

**Purpose**: Define organisational requirements for:

- Planning and preparation for PII-related information security incidents (A.3.11)
- Responding to information security incidents related to PII processing (A.3.12)

This policy establishes **WHAT** privacy incident management structures and notification obligations apply, **WHO** holds accountability for privacy incidents, and **WHEN** key actions and notifications must occur. Implementation procedures (**HOW**) are documented in PRIV-IMP-A.3.11-12-UG and PRIV-IMP-A.3.11-12-TG.

**Role Applicability**: This policy applies to the organisation acting as **both PII Controller and PII Processor**. Controls A.3.11 and A.3.12 are shared controls (Table A.3) and apply regardless of processing role. However, notification obligations differ materially between controller and processor roles and are addressed separately within this policy.

**Combined Control Rationale**: A.3.11 (planning and preparation) and A.3.12 (response) are the two phases of the same capability. Effective response is impossible without prior planning; planning without tested response procedures is theoretical. They are implemented together as an integrated privacy incident management programme that extends and specialises the ISMS incident management framework (ISMS-POL-A.5.24-28) for PII processing contexts.

---

# Scope and Applicability

## ISO/IEC 27701:2025 Control Statements

**Control A.3.11 — Information security incident management planning and preparation**
> *The organization shall plan and prepare for managing information security incidents related to PII processing by defining, establishing, and communicating incident management processes, roles and responsibilities.*

**Control A.3.12 — Response to information security incidents**
> *Responses to information security incidents related to PII processing shall be according to the documented procedures.*

## What This Policy Covers

**Incident Planning and Preparation**:

- Privacy incident management processes, roles, and responsibilities
- The Privacy Incident Response Plan (PIRP) structure and governance
- Escalation and communication paths specific to PII incidents
- Preparation activities: tabletop exercises, awareness, response tooling

**Incident Response**:

- Assessment of whether an information security incident constitutes a personal data breach
- Response procedures for personal data breaches, including containment and recovery
- Internal reporting and escalation chains for PII incidents
- Regulatory notification obligations (supervisory authorities)
- Data subject notification obligations
- Processor notification obligations (when acting as processor or when using processors)
- Post-incident learning specific to PII incidents

**Scope of PII Incidents**:

All of the following constitute PII-related incidents requiring management under this policy:

- Unauthorised access to PII (confirmed or suspected)
- Accidental disclosure of PII to an unauthorised recipient
- Loss or theft of a device, media, or document containing PII
- Ransomware, malware, or system compromise affecting PII processing systems
- Accidental deletion or corruption of PII
- Unlawful processing of PII (processing without legal basis, purpose limitation breach)
- Supplier/processor notification of an incident affecting [Organisation]'s PII

## What This Policy Does NOT Cover

- General information security incident management (see ISMS-POL-A.5.24-28)
- Forensic evidence collection procedures (see ISMS-POL-A.5.24-28)
- Information security event reporting by personnel (see ISMS-POL-A.6.8)
- Business continuity and disaster recovery (see ISMS-POL-A.5.29-30)
- Data subject rights response procedures for access and erasure requests (see PRIV-POL-A.1.3.5-10)

## Regulatory Framework

**Tier 1: Mandatory Compliance** (per PRIV-POL-00):

- **EU GDPR**: Article 33 (notification to supervisory authority within 72 hours of becoming aware of a personal data breach); Article 34 (communication to data subjects where breach is likely to result in high risk); Article 5(1)(f) (integrity and confidentiality principle)
- **CH FADP**: Article 24 (notification to the FDPIC of data security breaches likely to result in high risk to data subjects, without undue delay)
- **ISO/IEC 27701:2025**: Controls A.3.11, A.3.12 (normative)

**Tier 2: Conditional Applicability** (per PRIV-POL-00):

- **ISO/IEC 27018:2025**: Annex A — processor notification obligations to customers (A.2.5.5) where cloud PII processing in scope

**Tier 3: Informational Reference** (per PRIV-POL-00):

- **ISO/IEC 27002:2022**: Implementation guidance for incident management (5.24–5.28)
- **ISO/IEC 27701:2025 Annex B**: B.3.11 (incident planning), B.3.12 (incident response)

For complete regulatory categorisation, refer to PRIV-POL-00.

---

# Policy Statements: Privacy Incident Planning and Preparation (A.3.11)

## Privacy Incident Management Programme

[Organisation] SHALL plan and prepare for managing information security incidents related to PII processing as a defined, established, and communicated programme. This programme extends the ISMS incident management framework (ISMS-POL-A.5.24-28) with PII-specific processes, roles, and obligations.

### Privacy Incident Response Plan

[Organisation] SHALL maintain a Privacy Incident Response Plan (PIRP) that defines:

- PII incident classification criteria and severity tiers
- Roles and responsibilities for privacy incident management (see Roles and Responsibilities section)
- Escalation and communication chains for each severity tier
- Regulatory notification decision logic (whether, when, and to whom notifications are required)
- Data subject notification decision criteria and process
- Processor notification obligations (when [Organisation] acts as processor)
- Evidence preservation requirements for PII incidents
- Post-incident review and lessons learned process

The PIRP is a controlled document maintained by the DPO. Structure and content requirements are defined in PRIV-IMP-A.3.11-12-UG.

### Privacy Incident Severity Classification

PII incidents SHALL be classified by severity to determine escalation and response urgency:

| Severity | Criteria | Response Urgency |
|----------|----------|-----------------|
| **Critical** | Large-scale breach; special category PII affected; high likelihood of significant harm to data subjects; systemic compromise of PII processing systems | Immediate — incident response team activated within 2 hours |
| **High** | Confirmed personal data breach; regulatory notification likely; meaningful risk of harm to data subjects; significant volume of PII affected | Same day — DPO engaged within 4 hours |
| **Medium** | Suspected breach under investigation; limited PII affected; risk of harm low but not negligible; containment achieved | 24-hour response — DPO engaged within 24 hours |
| **Low** | Near-miss or potential event; no confirmed PII access; procedural violation with no actual breach | Standard — assessed within 5 business days |

Severity classification is performed by the Privacy Incident Lead and may be escalated upon discovery of additional information during investigation.

### Preparedness Requirements

[Organisation] SHALL maintain readiness for privacy incidents through:

- **Roles assigned and communicated**: All privacy incident roles (Privacy Incident Lead, DPO, Legal/Compliance, CISO, Communications) shall be defined, documented, and personnel shall be aware of their responsibilities
- **Training**: Personnel with privacy incident roles shall receive role-specific training; all personnel shall receive general awareness on how to recognise and report a potential PII incident
- **Testing**: The PIRP shall be tested at minimum annually through tabletop exercises; testing records shall be maintained
- **Contact maintenance**: Regulatory contact information (CNIL/AEPD/EDPB/ICO contact details for GDPR; FDPIC for CH FADP) and supervisory authority notification portal access shall be maintained and current
- **Notification templates**: Draft notification templates for supervisory authorities and data subjects shall be prepared, reviewed by Legal/DPO, and maintained ready for rapid deployment

---

# Policy Statements: Response to Privacy Incidents (A.3.12)

## Response Requirements

Responses to information security incidents related to PII processing SHALL be carried out according to the documented procedures in the PIRP and PRIV-IMP-A.3.11-12-UG. The following requirements govern the response:

### Personal Data Breach Assessment

When a PII-related incident is detected, [Organisation] SHALL promptly assess whether the incident constitutes a **personal data breach** — defined as a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data.

The personal data breach assessment SHALL consider:

- Whether PII was, or may have been, accessed, disclosed, lost, or destroyed without authorisation
- The categories and approximate volume of PII involved
- The likely consequences for data subjects (risk of financial harm, discrimination, identity theft, distress, or other significant adverse effects)
- Whether the breach is likely to result in a risk (or high risk) to the rights and freedoms of natural persons

The assessment and its outcome SHALL be documented regardless of conclusion.

### Regulatory Notification: Acting as PII Controller

When [Organisation] acts as PII Controller and a personal data breach is confirmed or reasonably suspected:

**GDPR — Notification to Supervisory Authority (Article 33)**:

- WHERE the breach is likely to result in a risk to the rights and freedoms of natural persons: notify the competent supervisory authority **without undue delay and, where feasible, no later than 72 hours** after becoming aware
- WHERE notification is made after 72 hours: include a reasoned justification for the delay
- WHERE the breach is unlikely to result in a risk: notification to the supervisory authority is not required, but the breach SHALL be documented internally (breach register)
- Notification content: nature of breach; categories and approximate number of data subjects; categories and approximate number of records; name/contact of DPO; likely consequences; measures taken or proposed to address the breach

**CH FADP — Notification to FDPIC (Article 24)**:

- WHERE the breach is likely to result in a high risk to the personality or fundamental rights of data subjects: notify the FDPIC **as soon as possible**
- Notification to the FDPIC shall follow the format specified by the FDPIC

**GDPR — Communication to Data Subjects (Article 34)**:

- WHERE the breach is likely to result in a **high risk** to the rights and freedoms of data subjects: communicate to affected data subjects **without undue delay**
- Communication content: nature of the breach (in plain language); name/contact of DPO; likely consequences; measures taken or proposed
- Communication may be delayed where law enforcement considerations apply (coordination with Legal required)

### Regulatory Notification: Acting as PII Processor

When [Organisation] acts as PII Processor and a personal data breach (or potential breach) affecting a customer's PII is detected:

- Notify the PII Controller (customer) **without undue delay** (timeframes per processor agreement, maximum 24 hours from confirmed awareness)
- Provide all available information to enable the Controller to fulfil its Article 33 notification obligations
- Do NOT notify the supervisory authority or data subjects directly unless explicitly authorised by the Controller (except where legally required)
- Cooperate fully with the Controller's investigation

### Incident Response Actions

Privacy incident response SHALL include, in order of priority:

1. **Contain**: Stop the ongoing breach or prevent further PII exposure
2. **Assess**: Determine scope, affected PII categories, volume, and affected data subjects
3. **Preserve**: Secure evidence (logs, records, affected systems) — coordinate with CISO per ISMS-POL-A.5.24-28
4. **Notify**: Execute regulatory and data subject notifications per the applicable thresholds above
5. **Recover**: Restore PII processing to normal operation with appropriate safeguards
6. **Review**: Conduct post-incident review; update PIRP and controls as needed

### Privacy Breach Register

[Organisation] SHALL maintain a Privacy Breach Register that records all personal data breaches, regardless of whether regulatory notification was required. The register SHALL include:

- Incident reference and date of discovery
- Nature of the breach and PII categories affected
- Approximate number of data subjects and records involved
- Risk assessment outcome (risk / high risk / no risk to data subjects)
- Notification decisions (supervisory authority, data subjects) and dates
- Remediation actions taken
- Post-incident review reference

The DPO maintains the Privacy Breach Register. It is a confidential document and evidence of regulatory compliance. Retention: minimum 5 years.

---

# Roles and Responsibilities

## Privacy Incident Management Roles

| Role | Responsibilities |
|------|-----------------|
| **Data Protection Officer (DPO)** | Privacy Incident Lead — activates PIRP; makes regulatory notification decisions; communicates with supervisory authorities; approves data subject communications; maintains Privacy Breach Register; leads post-incident review |
| **CISO** | Technical Incident Lead — coordinates containment and recovery; preserves forensic evidence; manages technical investigation; interfaces with IT Security Team and external responders |
| **Legal/Compliance Officer** | Legal guidance on notification obligations, data subject rights, and law enforcement considerations; reviews supervisory authority notifications before submission; advises on processor obligations |
| **Privacy Champions** | First escalation point for staff reporting PII incidents in their business unit; initial triage and escalation to DPO |
| **IT Security Team** | Technical investigation and containment; log analysis; system isolation and recovery; evidence preservation per ISMS-POL-A.5.24-28 |
| **Executive Management** | Informed of all High and Critical incidents; approve crisis communications; support regulatory engagement at senior level where required |
| **Communications** | Data subject notification drafting (with DPO approval); media/public relations management for large-scale breaches |
| **All Personnel** | Report suspected PII incidents immediately to their Privacy Champion or directly to the DPO; preserve evidence; cooperate with investigation |

---

# Evidence Requirements

The following evidence demonstrates operation of this policy:

| Evidence | Description | Retention |
|---------|-------------|-----------|
| Privacy Incident Response Plan (PIRP) | Current approved version with roles, processes, notification decision logic | Current + 3 years |
| Privacy Breach Register | Record of all personal data breaches and near-misses with risk assessment and notification decisions | 5 years |
| Supervisory Authority Notifications | Copies of all Article 33 / FADP Article 24 notifications submitted | 5 years |
| Data Subject Communications | Copies of Article 34 communications to data subjects | 5 years |
| PIRP Test Records | Evidence of annual tabletop exercises including findings and improvements | 3 years |
| Incident Response Timeline Records | Evidence of compliance with 72-hour notification window (or documented justification for delay) | 5 years |
| Post-Incident Review Reports | Lessons learned and PIRP/control improvement actions | 3 years |

---

# Audit Considerations

Auditors verifying compliance with A.3.11 and A.3.12 should expect to find:

**For A.3.11 (Planning and preparation)**:
- A documented Privacy Incident Response Plan with PII-specific processes and roles
- Evidence that roles are assigned and personnel are aware of responsibilities
- Annual PIRP test records (tabletop exercise or equivalent)
- Maintained supervisory authority contact information and notification portal access
- Prepared notification templates reviewed by Legal/DPO

**For A.3.12 (Response)**:
- Privacy Breach Register with all incidents recorded including no-notification determinations
- For notified breaches: supervisory authority notifications within 72-hour window (or justified delay documentation)
- Personal data breach assessment documentation for all High/Critical incidents
- Post-incident review reports with improvement actions tracked to completion
- Evidence that processor notification obligations were met (timely customer notification where acting as processor)

---

<!-- QA_VERIFIED: [Date] -->
