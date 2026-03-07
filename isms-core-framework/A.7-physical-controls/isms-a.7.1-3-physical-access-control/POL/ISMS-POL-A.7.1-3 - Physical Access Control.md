<!-- ISMS-CORE:POLICY:ISMS-POL-A.7.1-3:framework:POL:a.7.1-3 -->
**ISMS-POL-A.7.1-3 — Physical Access Control**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Physical Access Control |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.7.1-3 |
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
- Secondary: Facilities Manager
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.7.4-5-11 (Physical Infrastructure Security)
- ISMS-POL-A.6.7-8 (Remote Working and Reporting)
- ISMS-IMP-A.7.1-3.S1-UG/TG (Perimeter Security Assessment)
- ISMS-IMP-A.7.1-3.S2-UG/TG (Entry Control Assessment)
- ISMS-IMP-A.7.1-3.S3-UG/TG (Secure Areas Assessment)
- ISO/IEC 27001:2022 Controls A.7.1, A.7.2, A.7.3

---

## Executive Summary

This policy establishes [Organisation]'s requirements for physical access control, covering security perimeters, entry controls, and securing offices, rooms, and facilities.

**Scope**: This policy applies to all [Organisation] premises, facilities, and areas where information assets are processed, stored, or transmitted.

**Purpose**: Define requirements for protecting premises and information assets through physical security perimeters, controlled entry points, and secured internal spaces. This policy establishes WHAT physical access requirements apply and WHO is responsible. Implementation procedures (HOW) are documented in ISMS-IMP-A.7.1-3.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, PCI DSS v4.0.1, DORA, NIS2) apply where [Organisation]'s business activities trigger applicability.

**Combined Control Approach**: Controls A.7.1 (Physical Security Perimeters), A.7.2 (Physical Entry), and A.7.3 (Securing Offices, Rooms and Facilities) are implemented together because they form an integrated physical security framework where perimeters define boundaries, entry controls protect access points, and internal security measures protect specific areas.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Controls A.7.1, A.7.2, and A.7.3**

**ISO/IEC 27001:2022 Annex A.7.1 - Physical Security Perimeters**

> *Security perimeters should be defined and used to protect areas that contain information and other associated assets.*

**ISO/IEC 27001:2022 Annex A.7.2 - Physical Entry**

> *Secure areas should be protected by appropriate entry controls to ensure that only authorised personnel are allowed access.*

**ISO/IEC 27001:2022 Annex A.7.3 - Securing Offices, Rooms and Facilities**

> *Physical security for offices, rooms and facilities should be designed and implemented.*

**Control Objectives**:

- Prevent unauthorised physical access to organisational premises
- Define and enforce security boundaries for different asset classifications
- Ensure only authorised personnel can access secure areas
- Protect offices, rooms, and facilities containing information assets

**Control Type**: Preventive
**Control Category**: Physical

**This Policy Addresses**:

- Security perimeter definition and construction
- Physical entry controls and authentication
- Access control systems and visitor management
- Office, server room, and meeting room security
- Shared facility considerations

## What This Policy Does

This policy:

- **Defines** security zone classifications and perimeter requirements
- **Establishes** entry control and authentication requirements by zone
- **Specifies** visitor management and contractor access procedures
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Define physical monitoring and surveillance** (see ISMS-POL-A.7.4-5-11)
- **Specify environmental protection requirements** (see ISMS-POL-A.7.4-5-11)
- **Detail equipment siting and protection** (see ISMS-POL-A.7.8-9)
- **Provide access control system technical specifications** (see ISMS-IMP-A.7.1-3)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite technology or facility changes
- Flexibility for different physical security solutions
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- All owned, leased, or operated premises including offices, datacenters, and remote sites
- All areas: public areas, reception, offices, server rooms, datacenters, secure storage
- All entry points: main entrances, emergency exits, loading areas, windows, roof access
- All personnel: employees, contractors, visitors, maintenance personnel, delivery personnel

**Out of Scope**:

- Physical monitoring systems (covered by A.7.4)
- Environmental protection (covered by A.7.5)
- Equipment protection and siting (covered by A.7.8-9)

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG** | All personal data processing | Article 8 - Technical measures appropriate to risk |
| **ISO/IEC 27001:2022** | Certification scope | Controls A.7.1, A.7.2, A.7.3 |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Requirements |
|-----------|-------------------|--------------|
| **EU GDPR Art. 32** | Processing personal data of EU/EEA individuals as determined in ISMS-POL-00 | Security of processing including physical security |
| **PCI DSS v4.0.1** | Payment card processing | Requirement 9 - Physical access restrictions |
| **FINMA** | Swiss regulated financial institution | Physical security of premises |
| **DORA** | EU financial services entity | ICT physical security requirements |
| **NIS2** | Essential/important entity (EU) | Physical security measures |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- ASIS Physical Security Professional guidelines
- NIST SP 800-116 (PIV Card physical access)
- EN 50131 (Intrusion detection standards)
- Industry best practices for access control systems

**Compliance Determination**: [Organisation] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent requirements apply where multiple regulations overlap.

---

# Policy Statements

## Physical Security Perimeters (A.7.1)

### Perimeter Definition

[Organisation] SHALL define and document physical security perimeters to protect areas containing information and associated assets:

**Security Zones**:

| Zone | Description | Example Areas |
|------|-------------|---------------|
| **Public Zone** | Accessible to general public | Reception lobby, visitor waiting areas |
| **Controlled Zone** | Accessible to authorised personnel | General office areas, meeting rooms |
| **Restricted Zone** | Limited access, need-to-know | Executive offices, HR, finance |
| **High-Security Zone** | Strictly controlled access | Server rooms, datacenters, security operations |

**Perimeter Requirements**:

- Perimeters SHALL be clearly defined and documented
- Physical barriers SHALL be appropriate to the zone classification
- There SHALL be no gaps in perimeters where unauthorised entry could occur
- Perimeters SHALL extend from floor to ceiling (including raised floors and suspended ceilings)

### Perimeter Construction

**Building Perimeter**:

- External walls, roofs, and floors SHALL be of solid construction
- External doors SHALL be secured with appropriate locks and access controls
- Windows SHALL be secured, especially at ground level
- Emergency exits SHALL be alarmed and monitored

**Internal Perimeters**:

- Partitions between security zones SHALL extend floor-to-ceiling
- Access points between zones SHALL have appropriate controls
- Walls SHALL prevent visual and audio eavesdropping where required

### Perimeter Monitoring

- CCTV coverage SHALL be provided at perimeter entry points
- Intrusion detection SHALL be implemented for high-security perimeters
- Perimeter breaches SHALL trigger alerts to security personnel
- Perimeter inspections SHALL be performed at minimum annually for Controlled zones and at least quarterly for Restricted and High-Security zones; evidence retained in the Evidence Register
- Technical specifications, retention, and monitoring operations are defined in ISMS-POL-A.7.4-5-11 and related IMPs

### Colocation and Shared Facilities

Where [Organisation] operates in colocation or shared facilities, physical perimeter controls SHALL be assured via:

- Documented delineation of [Organisation]-controlled areas (cages/rooms) and entry points
- Contractual requirements for physical security and access logging
- Supplier assurance evidence (e.g., ISO 27001 certificate, SOC reports, or equivalent attestations) reviewed per ISMS-POL-A.5.19-23
- Periodic review records per supplier management requirements
- Evidence linked in the Evidence Register

## Physical Entry Controls (A.7.2)

### Entry Point Security

All entry points to secure areas SHALL be protected:

**Main Entrances**:

- Reception desk SHALL be staffed during business hours
- Access control systems (badge readers, biometrics) SHALL be implemented
- Tailgating/piggybacking prevention measures SHALL be in place
- After-hours access SHALL require additional authentication

**Secondary Entrances**:

- Side doors SHALL have equivalent access controls to main entrance
- Fire doors and emergency exits SHALL be alarmed
- Emergency exits SHALL not be used for routine entry/exit
- Loading areas SHALL have separate access controls

### Access Control Systems

**Authentication Methods**:

| Security Zone | Minimum Authentication |
|---------------|----------------------|
| **Controlled Zone** | Badge/card access |
| **Restricted Zone** | Badge + PIN |
| **High-Security Zone** | Badge + PIN + biometric OR dual-person control |

**Access Control Requirements**:

- Access rights SHALL be based on job role and need-to-know
- Access rights SHALL be reviewed quarterly
- Terminated employee access SHALL be revoked immediately
- Lost badges SHALL be reported and deactivated immediately
- Badge sharing SHALL be prohibited

### Visitor Management

**Visitor Procedures**:

- All visitors SHALL sign in at reception
- Visitors SHALL present identification
- Visitor badges SHALL be clearly distinguishable from employee badges
- Visitors SHALL be escorted in restricted and high-security zones
- Visitor logs SHALL be retained for minimum 12 months

**Contractor and Maintenance Access**:

- Contractors SHALL be pre-authorised before arrival
- Contractor access SHALL be time-limited and logged
- Contractors in high-security zones SHALL be escorted
- Contractor work SHALL be supervised where sensitive systems accessed

## Securing Offices, Rooms and Facilities (A.7.3)

### Office Security

**General Offices**:

- Offices SHALL be locked when unoccupied (after hours)
- Clean desk policy SHALL be enforced
- Sensitive documents SHALL be secured in locked storage
- Screens SHALL be positioned to prevent shoulder surfing

**Sensitive Areas**:

- Areas processing CONFIDENTIAL information SHALL have additional access controls; sensitive areas are determined based on classification per ISMS-POL-A.5.12-13
- Access logs SHALL be maintained
- Windows into sensitive areas SHALL be frosted or covered

**Access Log Retention**: Physical access control system logs SHALL be retained for at least 12 months (or longer if required by applicable regulation/contract), protected against unauthorised modification, and available within 2 business days for audit and incident response. Technical log retention requirements are defined in ISMS-POL-A.8.15.

### Server Rooms and Datacenters

**Access Control**:

- Access SHALL be limited to authorised IT personnel only
- Multi-factor authentication SHALL be required
- All access SHALL be logged with identity and timestamp
- Dual-person control SHALL be implemented for highest-security areas

**Physical Security**:

**For [Organisation]-controlled server rooms**, the following requirements SHALL apply:

- No external windows
- Reinforced walls, floors, and ceilings
- Environmental monitoring (fire, water, temperature)
- CCTV coverage with recording

**For third-party datacenters/colocation**, [Organisation] SHALL ensure equivalent protections through supplier assurance (ISO 27001, SOC reports) and contractual requirements, documented exceptions, and risk treatment where exact equivalence is not feasible. Evidence linked in the Evidence Register per ISMS-POL-A.5.19-23.

### Meeting Rooms

- Meeting rooms SHALL be checked for recording devices before sensitive discussions
- Whiteboards SHALL be erased after meetings
- Documents SHALL not be left in meeting rooms
- Video conferencing equipment SHALL be secured when not in use

### Verification of Office and Meeting Room Controls

Compliance with office, meeting room, and sensitive area requirements SHALL be verified through documented physical security walkthroughs/spot checks at least quarterly (and after material incidents). Findings SHALL be recorded as nonconformities or improvement actions and tracked to closure per Clause 10.2. Walkthrough checklist and evidence stored in Evidence Register.

### Shared Facilities

For organisations in shared buildings:

- [Organisation]'s perimeter SHALL be clearly defined within the building
- Building management access SHALL be controlled and logged
- Shared infrastructure (lifts, corridors) SHALL not provide direct access to secure areas
- Key/card management for building access SHALL be coordinated with building management

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Physical Access Responsibilities |
|------|----------------------------------|
| **Executive Management** | Approve policy, allocate resources for physical security |
| **CISO** | Policy ownership, physical security standards, compliance oversight |
| **Facilities Manager** | Physical security implementation, access control operations |
| **Reception/Security** | Visitor management, monitoring, incident response |
| **Line Managers** | Authorise access for team members, ensure compliance |
| **All Personnel** | Follow access procedures, report security incidents, challenge unknown persons |

## Escalation Path

- Physical security incidents: Employee → Security/Reception → Facilities Manager → CISO
- Access requests: Employee → Line Manager → Facilities Manager (approval)
- Visitor issues: Reception → Facilities Manager → CISO

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| Perimeter security audit | Annual | Facilities Manager | Inspection reports |
| Access control system review | Quarterly | IT Security | System configuration, logs |
| Access rights review | Quarterly | Facilities Manager | Access lists, approvals |
| Visitor log audit | Monthly | Security Team | Visitor registers |
| Physical security testing | Annual | Internal Audit | Penetration test results |

**Governance Metrics**:

- Access control coverage (target: 100% of entry points)
- Unauthorised access attempts (target: 0 successful)
- Visitor escort compliance (target: 100%)
- Access reviews completed on time (target: 100%)
- Badge loss/theft incidents (target: <5 per quarter)

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Facility changes, security incidents, audit findings, regulatory updates
- **Reviewers**: CISO, Facilities Manager, Security Team
- **Approval**: Executive Management

## Exception Management

**Permitted Exceptions**:

- Temporary access for emergency repairs (with enhanced monitoring)
- Extended visitor access for auditors (with documented approval)
- Alternative authentication methods for accessibility requirements

**Exception Process**:

1. Document business justification
2. Risk assessment of exception impact
3. CISO + Facilities Manager approval
4. Time-limited approval (maximum 6 months)
5. Documentation in exception register

**Not Permissible**:

- Permanent exceptions to access revocation timelines
- Exceptions without compensating controls
- Bypass of high-security zone authentication requirements

All exceptions SHALL be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

## Corrective Action Linkage

Nonconformities related to this policy (e.g., unauthorised access, incomplete visitor logs, access not revoked, perimeter gaps) SHALL be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organisation]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Physical security risks identified in risk assessment
- Threat scenarios include unauthorised access, theft, damage
- Risk treatment plans document physical security controls

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Controls A.7.1, A.7.2, A.7.3 applicability justified in [Organisation]'s SoA
- Implementation status tracked and reported

**Related Controls**:

| Control | Relationship |
|---------|--------------|
| **A.7.4-5-11** | Physical monitoring, environmental protection, utilities |
| **A.7.6-7-14** | Secure areas working, clear desk, secure disposal |
| **A.5.15-16-18** | Logical access control integration |
| **A.5.24-28** | Physical security incident management |
| **A.6.7** | Remote working reduces on-site access requirements |

**Stacked Control Integration**:

A.7.1-3 (Physical Access Control) stacks with related controls:

| Stacked Control | Integration Point | A.7.1-3 Contribution |
|-----------------|-------------------|------------------------|
| **A.7.4-5-11** (Infrastructure Security) | Monitoring and environment | A.7.1-3 defines access; A.7.4-5-11 monitors and protects |
| **A.5.15-16-18** (IAM) | Logical-physical integration | A.7.1-3 physical access; IAM logical access |
| **A.5.24-28** (Incident Management) | Physical incidents | A.7.1-3 prevents; A.5.24-28 responds to physical security incidents |

Assessment of A.7.1-3 should reference stacked control assessments for complete coverage.

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.7.1-3 Suite):

| Document ID | Title | Purpose |
|-------------|-------|---------|
| **ISMS-IMP-A.7.1-3.1-UG/TG** | Physical Security Assessment | Zone assessment and perimeter verification |
| **ISMS-IMP-A.7.1-3.2-UG/TG** | Access Control Configuration | Access system setup and management |
| **ISMS-IMP-A.7.1-3.3-UG/TG** | Visitor Management Procedures | Visitor processing and escort procedures |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Required Stage 1 evidence includes:

- This policy document (ISMS-POL-A.7.1-3 v1.0)
- Recorded approval by CISO, Facilities Manager, Executive Management
- Evidence of communication to relevant roles
- Security perimeter requirements documented (Physical Security Perimeters)
- Entry control requirements documented (Physical Entry Controls)
- Office/room security requirements documented (Securing Offices, Rooms and Facilities)
- Roles and responsibilities assigned (Roles and Responsibilities)

Evidence presence and status is tracked in the ISMS Evidence Register.

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Security zone documentation and floor plans
- Access control system configuration and logs
- Visitor registers and escort records
- Access rights review records and approvals
- Perimeter inspection reports
- Physical security test results
- Badge management records (issuance, revocation, lost badges)
- Training records for security personnel

---

# Definitions

| Term | Definition |
|------|------------|
| **Security Perimeter** | A defined boundary protecting a secure area from unauthorised access |
| **Secure Area** | A location where access is controlled and restricted to authorised personnel |
| **Tailgating** | Following an authorised person through an access point without authentication |
| **Dual-Person Control** | Requirement for two authorised persons to be present for access |
| **Visitor** | Any person who is not an employee or regular contractor |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Facilities Manager** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for physical access control. Implementation procedures are documented in ISMS-IMP-A.7.1-3 (UG/TG).*

<!-- QA_VERIFIED: 2026-03-01 -->
