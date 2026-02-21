<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.5-6:framework:POL:a.5.5-6 -->
**ISMS-POL-A.5.5-6 — Contact with Authorities and Special Interest Groups**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Contact with Authorities and Special Interest Groups |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.5-6 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Legal Counsel
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle)
- ISMS-POL-A.5.7 (Threat Intelligence)
- ISMS-IMP-A.5.5-6.S1-UG/TG (Authority Contacts Register)
- ISMS-IMP-A.5.5-6.S2-UG/TG (Special Interest Groups Register)
- ISMS-IMP-A.5.5-6.S3-UG/TG (External Communication Procedures)
- ISMS-IMP-A.5.5-6.S4-UG/TG (Compliance Dashboard)
- ISMS-IMP-A.5.5-6.S5-UG/TG (Consolidation Dashboard)
- ISO/IEC 27001:2022 Controls A.5.5, A.5.6

---

## Executive Summary

This policy establishes [Organization]'s requirements for maintaining appropriate contacts with relevant authorities, regulatory bodies, and special interest groups to ensure timely exchange of information security intelligence, regulatory compliance, and effective incident response.

**Scope**: This policy applies to all communications with external authorities, law enforcement, regulatory bodies, and information security special interest groups regarding security matters.

**Purpose**: Define organizational requirements for external authority contacts and security community engagement. This policy establishes WHAT contacts are required and WHO is authorized to engage. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.5-6 (UG/TG variants).

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, NIS2, DORA) apply where [Organization]'s business activities trigger applicability.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Controls A.5.5 and A.5.6**

**ISO/IEC 27001:2022 Annex A.5.5 - Contact with Authorities**

> *Appropriate contacts with relevant authorities should be maintained.*

**ISO/IEC 27001:2022 Annex A.5.6 - Contact with Special Interest Groups**

> *Appropriate contacts with special interest groups or other specialist security forums and professional associations should be maintained.*

**Control Objectives**:

- Ensure compliance with mandatory reporting requirements
- Enable rapid response during security incidents
- Maintain current threat and vulnerability intelligence
- Participate in industry security improvement initiatives

**Control Type**: Preventive, Detective
**Control Category**: Organizational

**This Policy Addresses**:

- Required authority contacts and notification obligations
- Authorized communication channels and spokespersons
- Special interest group participation requirements
- Information sharing protocols and restrictions
- Response to authority inquiries

## What This Policy Does

This policy:

- **Defines** mandatory authority contacts and notification requirements
- **Establishes** authorized spokespersons for external communications
- **Specifies** special interest group participation expectations
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Specify contact procedures and scripts** (see ISMS-IMP-A.5.5-6 Implementation Guidance)
- **Provide communication templates** (see ISMS-IMP-A.5.5-6 Templates)
- **Define contact database maintenance procedures** (operational documentation)
- **Replace incident management** (see ISMS-POL-A.5.24-28)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite contact detail changes
- Flexibility for different communication methods
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- All communications with external authorities regarding [Organization] security matters
- All law enforcement and regulatory body interactions
- All special interest group and professional association participation
- All personnel authorized to communicate externally on security matters

**Out of Scope**:

- Routine business communications unrelated to security
- Personal professional memberships (unless representing [Organization])
- Internal security communications (covered by other policies)

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG Art. 24** | Personal data processing | Data breach notification to FDPIC |
| **ISO/IEC 27001:2022** | Certification scope | Controls A.5.5, A.5.6 - Authority and group contacts |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Contact Requirements |
|-----------|-------------------|----------------------|
| **EU GDPR Art. 33** | Processing EU personal data | Supervisory authority notification (72 hours) |
| **FINMA** | Swiss regulated financial institution | Incident reporting obligations |
| **NIS2** | Essential/important entity (EU) | Significant incident notification to CSIRT |
| **DORA** | EU financial services entity | ICT incident reporting to competent authority |
| **Swiss Critical Infrastructure** | Critical operator designation | NCSC mandatory reporting |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- ENISA Guidelines on Incident Reporting
- FIRST (Forum of Incident Response and Security Teams) best practices
- TLP (Traffic Light Protocol) for information sharing
- STIX/TAXII standards for threat intelligence exchange

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent notification requirements apply where multiple regulations overlap.

---

# Policy Statements

## Authority Contact Requirements

### Mandatory Authority Contacts

[Organization] SHALL maintain active contacts with the following authorities:

**Law Enforcement & Cyber Authorities**:

| Authority | Jurisdiction | Contact Purpose |
|-----------|--------------|-----------------|
| NCSC (National Cyber Security Centre) | Switzerland | Cyber threat reporting, advisories |
| Cantonal Police (Cybercrime Unit) | [Canton] | Criminal incident reporting |
| fedpol (Federal Police) | Switzerland | Serious cybercrime, terrorism |
| National cybersecurity coordination function | Switzerland | Critical incident reporting via NCSC channels |

**Regulatory Authorities** (as applicable per ISMS-POL-00):

| Authority | Trigger | Contact Purpose |
|-----------|---------|-----------------|
| FDPIC | Personal data processing | Data breach notification, inquiries |
| FINMA | Financial services | Regulatory reporting, inspections |
| Relevant EU DPAs | EU operations/data subjects | GDPR compliance, breach notification |

**Emergency Services**:

| Service | Contact Trigger |
|---------|-----------------|
| Fire Services | Physical security emergency |
| Medical Services | Personnel safety emergency |
| Utility Providers | Infrastructure disruption |

### Notification Obligations

Notification obligations, deadlines, and thresholds are determined by applicable legal/regulatory and contractual requirements as recorded in ISMS-POL-00 and the legal obligations register. The timeframes below are internal targets intended to enable compliance unless a stricter legal/contractual deadline applies.

**Mandatory Notifications**:

| Event Type | Authority | Timeframe | Threshold |
|------------|-----------|-----------|-----------|
| Personal data breach (CH) | FDPIC | "As soon as possible" | High risk to data subjects |
| Personal data breach (EU) | Lead Supervisory Authority | 72 hours | Except if unlikely to result in risk |
| Major cyber incident | NCSC | 24 hours | Critical systems affected |
| Criminal activity | Police | Immediate | Evidence of crime |
| Financial services incident | FINMA | Per FINMA requirements | Material incident |

**Notification Authority**: Only designated personnel may submit mandatory notifications:

- CISO or Deputy CISO
- Legal Counsel
- Data Protection Officer (for data breach notifications)
- CEO/CFO (for regulatory filings)

### Communication Protocols

**Authorized Spokespersons**:

| Topic | Primary Spokesperson | Backup |
|-------|---------------------|--------|
| Security incidents | CISO | Deputy CISO |
| Data protection matters | DPO | Legal Counsel |
| Regulatory inquiries | Legal Counsel | CFO |
| Media inquiries | Communications Director | CEO |

**Communication Restrictions**:

- No employee shall contact authorities regarding [Organization] security matters without authorization
- All authority communications SHALL be documented
- Legal Counsel SHALL review communications involving potential legal liability
- Classified or confidential information requires approval before disclosure

**Response to Authority Inquiries**:

- Acknowledge receipt within 24 hours or next business day, whichever is sooner; critical inquiries follow the incident on-call process
- Engage Legal Counsel for formal requests or investigations
- Document all requests and responses
- Escalate to Executive Management for significant matters

## Special Interest Group Participation

### Required Memberships

[Organization] SHALL maintain active participation in relevant security communities:

**Industry-Specific Groups**:

| Group Type | Examples | Participation Level |
|------------|----------|---------------------|
| Sector ISAC/ISAO | FS-ISAC, H-ISAC, or equivalent | Active membership |
| National CERT community | FIRST, national CERT network | Information sharing |
| Industry associations | ISACA, (ISC)², CISO councils | Professional development |

**Vendor/Technology Groups**:

- Security advisory mailing lists for deployed technologies
- Vendor security notification programmes
- Open source security communities (where applicable)

### Participation Requirements

**Active Participation Includes**:

- Receiving and acting on threat intelligence
- Contributing anonymized incident data (where permitted)
- Attending relevant conferences and meetings
- Sharing best practices and lessons learned
- Participating in joint exercises when appropriate

At minimum, "active participation" means: (1) membership/subscription is current, (2) a monitored intake channel exists, (3) relevant advisories are reviewed at least weekly (or on receipt), and (4) actions/decisions are recorded in the ticketing or risk system where applicable (including "no action required" with rationale).

**Information Sharing Controls**:

- Pre-disclosure review for sensitive information
- Use of Traffic Light Protocol (TLP) for intelligence sharing
- Legal review for any information that could create liability
- No disclosure of customer data without consent/legal basis

### Participation Boundaries

**Permitted Activities**:

- Receiving threat intelligence and advisories
- Sharing technical indicators of compromise (IoCs)
- Participating in industry benchmarking (anonymized)
- Contributing to standards development
- Attending educational events

**Requires Additional Approval**:

- Disclosing [Organization] incident details
- Participating in joint operations
- Public speaking on [Organization] security practices
- Media interviews regarding security matters

---

# Roles and Responsibilities

## Accountability Matrix

| Role | External Communication Responsibilities |
|------|----------------------------------------|
| **CEO** | Ultimate authority for external communications, regulatory attestations |
| **CISO** | Primary security authority contact, special interest group lead |
| **Legal Counsel** | Regulatory inquiry response, disclosure review, notification compliance |
| **DPO** | Data protection authority communications, breach notifications |
| **Communications** | Media relations, public statements coordination |
| **Department Heads** | Domain-specific authority liaisons (with CISO coordination) |

## Contact Management

- **Contact Register Owner**: CISO
- **Update Frequency**: Quarterly verification of contact details
- **Access**: Restricted to authorized personnel
- **Backup**: Offline contact list maintained for emergencies

## Escalation Path

- Authority inquiry received: Recipient → CISO → Legal Counsel → Executive Management
- Notification required: CISO → Legal Counsel → CEO (for significant events)
- Media inquiry: Recipient → Communications Director → CEO

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| Authority contact verification | Quarterly | CISO | Updated contact register |
| Notification obligation review | Annual | Legal Counsel | Regulatory review |
| Special interest group assessment | Annual | CISO | Membership records |
| Communication log audit | Semi-annual | Internal Audit | Log review |

**Governance Metrics**:

- Contact register accuracy (target: 100% verified quarterly)
- Notification compliance rate (target: 100%)
- Special interest group participation (target: active in relevant groups)
- Authority inquiry response time (target: <24 hours acknowledgment)

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Regulatory changes, organisational changes, incident lessons learned
- **Reviewers**: CISO, Legal Counsel, DPO
- **Approval**: Executive Management

## Exception Management

**Limited Exceptions**:

- Alternative contact during personnel unavailability (documented delegation)
- Modified notification timelines only where legally permitted

**Not Permissible**:

- Failure to maintain required authority contacts
- Non-compliance with mandatory notification obligations
- Unauthorized disclosure of security information

All exceptions SHALL be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

## Corrective Action Linkage

Nonconformities related to this policy (e.g., missed notifications, unauthorized communications, contact register gaps) SHALL be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organization]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Authority contact requirements informed by regulatory risk assessment
- Threat intelligence sharing supports risk identification
- Risk treatment plans document external communication controls

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Controls A.5.5 and A.5.6 applicability justified in [Organization]'s SoA
- Implementation status tracked and reported

**Related Controls**:

| Control | Relationship |
|---------|--------------|
| **A.5.7** | Threat Intelligence - Intelligence received from special interest groups |
| **A.5.24-28** | Incident Management - Authority notification during incidents |
| **A.5.34** | Privacy and PII Protection - Data protection authority communications |

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.5.5-6):

| Document ID | Title | Purpose |
|-------------|-------|---------|
| **ISMS-IMP-A.5.5-6-UG/TG** | External Communications Implementation Guide | Contact procedures, templates, register maintenance |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Required Stage 1 evidence includes:

- ✅ This policy document (ISMS-POL-A.5.5-6 v1.0)
- ✅ Recorded approval by CISO, Legal Counsel, Executive Management
- ✅ Evidence of communication to relevant roles
- ✅ Mandatory authority contacts defined (Authority Contact Requirements)
- ✅ Notification obligations specified with timeframes (Notification Obligations)
- ✅ Authorized spokesperson matrix documented (Communication Protocols)
- ✅ Special interest group participation requirements defined (Special Interest Group Participation)
- ✅ Roles and responsibilities assigned (Roles and Responsibilities)

Evidence status is tracked in the ISMS Evidence Register.

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Authority contact register with quarterly verification records
- Sample notification submissions and responses
- Special interest group membership and participation records
- Communication logs with authorities (anonymised as needed)
- Threat intelligence received and actions taken
- Training records for authorised spokespersons
- Incident cases where authorities were contacted
- Evidence of acting on received advisories

Where no notifiable incidents occurred in the audit period, evidence may include tabletop exercises, simulations, and draft notification packs demonstrating readiness.

---

# Definitions

| Term | Definition |
|------|------------|
| **Relevant Authority** | Any government body, law enforcement agency, or regulatory authority with jurisdiction over [Organization]'s operations or data processing activities |
| **Special Interest Group** | Professional associations, industry forums, information sharing organizations, and security communities focused on cybersecurity topics |
| **Traffic Light Protocol (TLP)** | A standardized system for classifying sensitive information and controlling its distribution |
| **ISAC/ISAO** | Information Sharing and Analysis Center/Organization - sector-specific groups for sharing threat intelligence |
| **Mandatory Notification** | A legally required report to authorities triggered by specific events (e.g., data breach, cyber incident) |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Legal Counsel** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for external communications with authorities and special interest groups. Implementation procedures are documented in ISMS-IMP-A.5.5-6 (UG/TG).*

<!-- QA_VERIFIED: 2026-02-04 -->
