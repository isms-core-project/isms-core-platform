<!-- ISMS-CORE:POLICY:ISMS-POL-A.7.12-13:framework:POL:a.7.12-13 -->
**ISMS-POL-A.7.12-13 — Cabling Security and Equipment Maintenance**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Cabling Security and Equipment Maintenance |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.7.12-13 |
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
- Secondary: IT Operations Manager / Facilities Manager
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.7.4-5-11 (Physical Infrastructure Security)
- ISMS-POL-A.7.8-9 (Equipment Siting and Protection)
- ISMS-POL-A.8.6 (Capacity Management)
- ISMS-IMP-A.7.12-13.S1-UG/TG (Cabling Security Assessment)
- ISMS-IMP-A.7.12-13.S2-UG/TG (Equipment Maintenance Assessment)
- ISMS-IMP-A.7.12-13.S3-UG/TG (Maintenance Schedule Tracking)
- ISMS-IMP-A.7.12-13.S4-UG/TG (Infrastructure Compliance Dashboard)
- ISO/IEC 27001:2022 Controls A.7.12, A.7.13

---

## Executive Summary

This policy establishes [Organisation]'s requirements for cabling security and equipment maintenance, ensuring infrastructure integrity and operational continuity.

**Scope**: This policy applies to all power and telecommunications cabling, and all equipment containing or supporting information processing.

**Purpose**: Define requirements for protecting cabling infrastructure and maintaining equipment to ensure availability, integrity, and confidentiality of information. This policy establishes WHAT infrastructure requirements apply and WHO is responsible. Implementation procedures (HOW) are documented in ISMS-IMP-A.7.12-13.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, DORA, NIS2) apply where [Organisation]'s business activities trigger applicability.

**Combined Control Approach**: Controls A.7.12 (Cabling Security) and A.7.13 (Equipment Maintenance) are implemented together because they address complementary aspects of infrastructure protection and operational continuity, with cabling forming the foundation for equipment connectivity and maintenance ensuring ongoing reliability.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Controls A.7.12 and A.7.13**

**ISO/IEC 27001:2022 Annex A.7.12 - Cabling Security**

> *Cables carrying power, data or supporting information services should be protected from interception, interference or damage.*

**ISO/IEC 27001:2022 Annex A.7.13 - Equipment Maintenance**

> *Equipment should be maintained correctly to ensure availability, integrity and confidentiality of information.*

**Control Objectives**:

- Protect power and communications cables from interception, interference, and damage
- Ensure equipment availability through proper maintenance
- Maintain information integrity and confidentiality during maintenance activities
- Prevent operational disruptions through proactive maintenance

**Control Type**: Preventive
**Control Category**: Physical

**This Policy Addresses**:

- Cable protection and segregation requirements
- Cable documentation and change control
- Equipment maintenance programmes and schedules
- Maintenance personnel authorisation and supervision
- Security during maintenance activities

## What This Policy Does

This policy:

- **Defines** cabling security and protection requirements
- **Establishes** equipment maintenance programme requirements
- **Specifies** security requirements during maintenance activities
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Define physical access control to infrastructure areas** (see ISMS-POL-A.7.1-2-3)
- **Specify environmental monitoring requirements** (see ISMS-POL-A.7.4-5-11)
- **Detail equipment siting requirements** (see ISMS-POL-A.7.8-9)
- **Provide maintenance schedules and checklists** (see ISMS-IMP-A.7.12-13)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite technology or vendor changes
- Flexibility for different equipment types and maintenance providers
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- Cabling: power cables, network cables (copper and fibre), telecommunications cables
- Equipment: servers, network devices, storage systems, UPS, HVAC, security systems
- Facilities: datacenters, server rooms, wiring closets, office areas
- Activities: cable installation, maintenance, equipment servicing, repairs

**Out of Scope**:

- Physical access control to infrastructure (covered by A.7.1-2-3)
- Environmental monitoring systems (covered by A.7.4-5-11)
- Equipment disposal (covered by A.7.14)

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG** | All personal data processing | Appropriate technical and organisational measures to protect personal data |
| **ISO/IEC 27001:2022** | Certification scope | Controls A.7.12, A.7.13 |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Requirements |
|-----------|-------------------|--------------|
| **EU GDPR** | Processing EU personal data, EU establishment, or offering services to EU | Art. 32 security of processing |
| **FINMA** | Swiss regulated financial institution | ICT infrastructure resilience |
| **DORA** | EU financial services entity | ICT operational resilience |
| **NIS2** | Essential/important entity (EU) | Infrastructure protection |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- TIA/EIA-568 (Structured cabling standards)
- BICSI (Building Industry Consulting Service International) guidelines
- ISO/IEC 11801 (Generic cabling standards)
- ITIL Service Management (maintenance practices)

**Compliance Determination**: [Organisation] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent requirements apply where multiple regulations overlap.

---

# Policy Statements

## Cabling Security (A.7.12)

### Cable Protection

Cables carrying power, data, or supporting information services SHALL be protected:

**Physical Protection**:

- Cables SHALL be routed through protected pathways (conduits, cable trays, raised floors)
- Underground cabling SHALL be protected against accidental damage (armoured conduits)
- Cables SHALL be protected from electromagnetic interference
- Cable routes SHALL avoid areas with high risk of damage (water, heat, physical impact)

**Access Control**:

- Cabling infrastructure (patch panels, distribution frames) SHALL be in secured areas
- Wiring closets SHALL have access controls and be locked when unoccupied
- Cable routes SHALL not be accessible to unauthorised personnel
- Manhole and duct access SHALL be controlled and logged

### Segregation Requirements

**Power and Data Separation**:

- Power cables SHALL be segregated from communications cables to prevent interference
- Minimum separation and shielding requirements SHALL follow the [Organisation] Cabling Security Baseline defined in ISMS-IMP-A.7.12-13.1, which specifies minimum criteria per site type (on-premises, colocation, office)
- Where crossing is unavoidable, cables SHALL cross at right angles

**Network Segregation**:

- Cables carrying different security classifications SHALL be physically separated where feasible
- High-security network cables SHALL be clearly identified (colour coding or labelling)
- Fibre optic cables SHALL be used for high-security transmissions where interception risk exists

### Cable Documentation and Management

**Documentation**:

- Cable infrastructure SHALL be documented (cable schedules, diagrams)
- Documentation SHALL be maintained as current
- Documentation SHALL be secured and access-controlled

**Labelling**:

- Cables SHALL be labelled at both ends
- Labels SHALL enable identification without detailed documentation
- Patch panels and distribution frames SHALL be clearly labelled

**Change Control**:

- Cabling changes SHALL follow change management process (ISMS-POL-A.8.32)
- Unused cables SHALL be disconnected and documented
- Quarterly physical walkthroughs SHALL be conducted to identify unauthorised additions or changes; findings SHALL be reconciled against as-built diagrams and change tickets, with results documented and signed off in the cabling inspection workbook

### Inspection and Maintenance

- Regular inspections SHALL identify cable damage or deterioration
- Cable infrastructure SHALL be included in maintenance schedules
- Damaged cables SHALL be repaired or replaced promptly
- Inspection findings SHALL be documented

## Equipment Maintenance (A.7.13)

### Maintenance Programme

[Organisation] SHALL establish and implement a maintenance programme for all equipment:

**Programme Requirements**:

- All in-scope equipment recorded in the asset inventory (ISMS-POL-A.5.9) SHALL be included in the maintenance programme; the asset inventory is the authoritative source for programme completeness
- Quarterly reconciliation SHALL verify that all inventoried equipment has maintenance coverage; reconciliation results and sign-off SHALL be retained as evidence
- Maintenance schedules SHALL follow manufacturer recommendations as minimums; deviations require documented approval via the exception register
- Critical equipment SHALL have preventive maintenance schedules
- Maintenance records SHALL be maintained

**Maintenance Schedule**:

| Equipment Type | Preventive Maintenance Frequency |
|----------------|----------------------------------|
| Servers | Annually (firmware, cleaning, inspection) |
| Network equipment | Semi-annually |
| UPS systems | Quarterly battery checks, annual full test |
| HVAC/Cooling | Quarterly |
| Fire suppression | Per regulatory requirements |
| Security systems | Semi-annually |

### Maintenance Personnel

**Authorisation**:

- Only authorised personnel SHALL perform maintenance
- Maintenance personnel SHALL be identified and verified
- Third-party maintenance SHALL be contracted with approved providers

**Supervision**:

- Maintenance personnel SHALL be supervised when accessing sensitive equipment
- Unsupervised maintenance access SHALL be logged and monitored
- Remote maintenance SHALL be subject to access controls

### Security During Maintenance

**Data Protection**:

- Sensitive data SHALL be protected during maintenance activities
- Equipment containing data SHALL not leave premises for maintenance where avoidable
- If off-site maintenance required, data SHALL be securely erased first
- Maintenance personnel SHALL not have access to data unless specifically required

**Access Controls**:

- Maintenance access SHALL be time-limited
- Access SHALL be logged (who, what, when, why)
- All tools and equipment SHALL be accounted for after maintenance
- Physical inspection SHALL verify no unauthorised modifications

### Remote Maintenance

**Remote Access Requirements**:

- Remote maintenance SHALL be authorised and documented
- Remote access SHALL use secure connections (VPN, encrypted)
- Remote sessions SHALL be logged and monitored
- Remote access SHALL be disabled when not actively required

### Equipment Removal for Maintenance

When equipment must be removed from premises for maintenance:

- Removal SHALL be authorised by equipment owner
- Data SHALL be securely erased before removal (per A.7.14)
- Chain of custody SHALL be maintained
- Equipment SHALL be inspected upon return
- Return SHALL be logged in asset management system

### Maintenance Records

**Documentation Requirements**:

- All maintenance SHALL be documented
- Records SHALL include: date, equipment, work performed, personnel, findings
- Records SHALL be retained per retention schedule (minimum 3 years)
- Records SHALL be available for audit

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Cabling and Maintenance Responsibilities |
|------|------------------------------------------|
| **Executive Management** | Approve policy, allocate resources for infrastructure maintenance |
| **CISO** | Policy ownership, security standards for maintenance |
| **IT Operations Manager** | Equipment maintenance programme, vendor management |
| **Facilities Manager** | Cabling infrastructure, building maintenance |
| **System Owners** | Ensure owned equipment is maintained |
| **IT Operations** | Day-to-day maintenance execution, documentation |

## Escalation Path

- Maintenance issues: IT Operations → IT Operations Manager → CISO
- Cabling issues: Facilities → Facilities Manager → IT Operations Manager
- Security concerns: Any staff → CISO

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| Cabling infrastructure audit | Annual | Facilities Manager | Inspection reports |
| Maintenance programme review | Annual | IT Operations Manager | Programme documentation |
| Maintenance record audit | Quarterly | IT Operations | Maintenance logs |
| Vendor compliance review | Annual | IT Operations Manager | Contract compliance |

**Governance Metrics**:

- Preventive maintenance completion (target: 100% on schedule)
- Equipment failures due to maintenance gaps (target: 0)
- Cabling documentation accuracy (target: >95%)
- Unauthorised cabling changes detected (target: 0)
- Maintenance-related security incidents (target: 0)

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Infrastructure incidents, technology changes, audit findings, regulatory updates
- **Reviewers**: CISO, IT Operations Manager, Facilities Manager
- **Approval**: Executive Management

## Exception Management

**Permitted Exceptions**:

- Deferred maintenance for critical systems (with risk acceptance and scheduling)
- Extended maintenance intervals for low-criticality equipment (with documented justification)
- Third-party maintenance without full supervision (with enhanced monitoring)

**Exception Process**:

1. Document business justification
2. Risk assessment of exception impact
3. IT Operations Manager + CISO approval
4. Time-limited approval (maximum 6 months)
5. Documentation in exception register

**Not Permissible**:

- Skipping security-critical maintenance without compensating controls
- Undocumented cabling changes
- Unsupervised maintenance on systems containing sensitive data

All exceptions SHALL be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

## Corrective Action Linkage

Nonconformities related to this policy (e.g., missed maintenance, undocumented cabling, unauthorised changes, equipment failures) SHALL be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organisation]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Infrastructure failure risks inform maintenance requirements
- Cable interception risks addressed through protection measures
- Risk treatment plans document infrastructure protection controls

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Controls A.7.12 and A.7.13 applicability justified in [Organisation]'s SoA
- Implementation status tracked and reported

**Related Controls**:

| Control | Relationship |
|---------|--------------|
| **A.7.4-5-11** | Physical monitoring, environmental protection, utilities |
| **A.7.8-9** | Equipment siting and off-premises security |
| **A.7.14** | Secure disposal when equipment retired |
| **A.8.6** | Capacity management informs maintenance planning |
| **A.8.32** | Change management for infrastructure changes |

**Stacked Control Integration**:

A.7.12-13 (Cabling and Equipment Maintenance) stacks with related controls:

| Stacked Control | Integration Point | A.7.12-13 Contribution |
|-----------------|-------------------|------------------------|
| **A.7.4-5-11** (Infrastructure) | Environmental protection | A.7.4-5-11 monitors environment; A.7.12-13 maintains equipment |
| **A.7.8-9** (Equipment Siting) | Equipment protection | A.7.8-9 defines siting; A.7.13 ensures ongoing reliability |
| **A.8.32** (Change Management) | Infrastructure changes | A.7.12-13 maintains; A.8.32 controls changes |

Assessment of A.7.12-13 should reference stacked control assessments for complete coverage.

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.7.12-13 Suite):

| Document ID | Title | Purpose |
|-------------|-------|---------|
| **ISMS-IMP-A.7.12-13.1-UG/TG** | Cabling Standards and Procedures | Cable installation and protection procedures |
| **ISMS-IMP-A.7.12-13.2-UG/TG** | Maintenance Programme Management | Maintenance scheduling and tracking |
| **ISMS-IMP-A.7.12-13.3-UG/TG** | Vendor Maintenance Procedures | Third-party maintenance management |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Required Stage 1 evidence includes:

- This policy document (ISMS-POL-A.7.12-13 v1.0)
- Recorded approval by CISO, IT Operations Manager, Executive Management
- Evidence of communication to relevant roles
- Cabling security requirements documented (Cabling Security)
- Equipment maintenance requirements documented (Equipment Maintenance)
- Roles and responsibilities assigned (Roles and Responsibilities)

Evidence presence and status is tracked in the ISMS Evidence Register.

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Cable documentation including diagrams and schedules
- Cabling inspection reports
- Maintenance schedules showing equipment coverage
- Maintenance records with work performed
- Vendor maintenance reports
- Remote maintenance access logs
- Equipment return inspection records

---

# Definitions

| Term | Definition |
|------|------------|
| **Cabling Infrastructure** | All power and communications cables, conduits, pathways, and termination points |
| **Preventive Maintenance** | Scheduled maintenance to prevent equipment failure |
| **Corrective Maintenance** | Maintenance performed to repair a fault |
| **Remote Maintenance** | Maintenance performed via remote access without physical presence |
| **Chain of Custody** | Documented transfer of equipment responsibility |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **IT Operations Manager** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for cabling security and equipment maintenance. Implementation procedures are documented in ISMS-IMP-A.7.12-13 (UG/TG).*

<!-- QA_VERIFIED: 2026-02-04 -->
