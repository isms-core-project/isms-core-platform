**ISMS-POL-A.7.1-2-3 — Physical Access Control**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Physical Access Control |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.7.1-2-3 |
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
- ISMS-IMP-A.7.1-2-3 (Implementation Guidance)
- ISO/IEC 27001:2022 Controls A.7.1, A.7.2, A.7.3

---

## Executive Summary

This policy establishes [Organisation]'s requirements for physical access control, covering security perimeters, entry controls, and securing offices, rooms, and facilities.

**Purpose**: Define requirements for protecting premises and information assets through physical security perimeters, controlled entry points, and secured internal spaces. This policy establishes WHAT physical access requirements apply and WHO is responsible. Implementation procedures (HOW) are documented in ISMS-IMP-A.7.1-2-3.

**Scope**: All [Organisation] premises, facilities, and areas where information assets are processed, stored, or transmitted.

---

# Scope & Control Alignment

## ISO/IEC 27001:2022 Controls

### Control A.7.1 - Physical Security Perimeters

> *Security perimeters should be defined and used to protect areas that contain information and other associated assets.*

**Control Objective**: Prevent unauthorised physical access, damage, and interference to organisation information and assets.

### Control A.7.2 - Physical Entry

> *Secure areas should be protected by appropriate entry controls to ensure that only authorised personnel are allowed access.*

**Control Objective**: Ensure only authorised persons can access secure areas.

### Control A.7.3 - Securing Offices, Rooms and Facilities

> *Physical security for offices, rooms and facilities should be designed and implemented.*

**Control Objective**: Prevent unauthorised access to offices, rooms, and facilities containing information assets.

**Control Type**: Preventive
**Control Category**: Physical

## Policy Scope

**This policy applies to**:

| Category | Scope |
|----------|-------|
| **Facilities** | All owned, leased, or operated premises including offices, datacenters, and remote sites |
| **Areas** | Public areas, reception, offices, server rooms, datacenters, secure storage |
| **Entry Points** | Main entrances, emergency exits, loading areas, windows, roof access |
| **Personnel** | Employees, contractors, visitors, maintenance personnel, delivery personnel |

## Regulatory Applicability

**Tier 1 - Mandatory Compliance** (All operations):

| Regulation | Key Requirements |
|------------|------------------|
| **Swiss nDSG** | Article 8 - Technical measures appropriate to risk |
| **EU GDPR** | Article 32 - Security of processing including physical security |
| **ISO/IEC 27001:2022** | Controls A.7.1, A.7.2, A.7.3 |

**Tier 2 - Conditional Applicability** (Triggered by business activities):

| Regulation | Trigger | Requirement |
|-----------|---------|-------------|
| **PCI DSS v4.0** | Payment card processing | Requirement 9 - Physical access restrictions |
| **FINMA** | Swiss financial institution | Physical security of premises |
| **DORA** | EU financial services | ICT physical security |
| **NIS2** | Essential/important entity | Physical security measures |

---

# Policy Statements

## Physical Security Perimeters

### Perimeter Definition

[Organisation] should define and document physical security perimeters to protect areas containing information and associated assets:

**Security Zones**:

| Zone | Description | Example Areas |
|------|-------------|---------------|
| **Public Zone** | Accessible to general public | Reception lobby, visitor waiting areas |
| **Controlled Zone** | Accessible to authorised personnel | General office areas, meeting rooms |
| **Restricted Zone** | Limited access, need-to-know | Executive offices, HR, finance |
| **High-Security Zone** | Strictly controlled access | Server rooms, datacenters, security operations |

**Perimeter Requirements**:
- Perimeters should be clearly defined and documented
- Physical barriers should be appropriate to the zone classification
- There should be no gaps in perimeters where unauthorised entry could occur
- Perimeters should extend from floor to ceiling (including raised floors and suspended ceilings)

### Perimeter Construction

**Building Perimeter**:
- External walls, roofs, and floors should be of solid construction
- External doors should be secured with appropriate locks and access controls
- Windows should be secured, especially at ground level
- Emergency exits should be alarmed and monitored

**Internal Perimeters**:
- Partitions between security zones should extend floor-to-ceiling
- Access points between zones should have appropriate controls
- Walls should prevent visual and audio eavesdropping where required

### Perimeter Monitoring

- CCTV coverage should be provided at perimeter entry points
- Intrusion detection should be implemented for high-security perimeters
- Perimeter breaches should trigger alerts to security personnel
- Regular perimeter inspections should be conducted

## Physical Entry Controls

### Entry Point Security

All entry points to secure areas should be protected:

**Main Entrances**:
- Reception desk should be staffed during business hours
- Access control systems (badge readers, biometrics) should be implemented
- Tailgating/piggybacking prevention measures should be in place
- After-hours access should require additional authentication

**Secondary Entrances**:
- Side doors should have equivalent access controls to main entrance
- Fire doors and emergency exits should be alarmed
- Emergency exits should not be used for routine entry/exit
- Loading areas should have separate access controls

### Access Control Systems

**Authentication Methods**:

| Security Zone | Minimum Authentication |
|---------------|----------------------|
| **Controlled Zone** | Badge/card access |
| **Restricted Zone** | Badge + PIN |
| **High-Security Zone** | Badge + PIN + biometric OR dual-person control |

**Access Control Requirements**:
- Access rights should be based on job role and need-to-know
- Access rights should be reviewed quarterly
- Terminated employee access should be revoked immediately
- Lost badges should be reported and deactivated immediately
- Badge sharing should be prohibited

### Visitor Management

**Visitor Procedures**:
- All visitors should sign in at reception
- Visitors should present identification
- Visitor badges should be clearly distinguishable from employee badges
- Visitors should be escorted in restricted and high-security zones
- Visitor logs should be retained for minimum 12 months

**Contractor and Maintenance Access**:
- Contractors should be pre-authorised before arrival
- Contractor access should be time-limited and logged
- Contractors in high-security zones should be escorted
- Contractor work should be supervised where sensitive systems accessed

## Securing Offices, Rooms and Facilities

### Office Security

**General Offices**:
- Offices should be locked when unoccupied (after hours)
- Clean desk policy should be enforced
- Sensitive documents should be secured in locked storage
- Screens should be positioned to prevent shoulder surfing

**Sensitive Areas**:
- Areas processing CONFIDENTIAL information should have additional access controls
- Access logs should be maintained
- Windows into sensitive areas should be frosted or covered

### Server Rooms and Datacenters

**Access Control**:
- Access limited to authorised IT personnel only
- Multi-factor authentication required
- All access logged with identity and timestamp
- Dual-person control for highest-security areas

**Physical Security**:
- No external windows
- Reinforced walls, floors, and ceilings
- Environmental monitoring (fire, water, temperature)
- CCTV coverage with recording

### Meeting Rooms

- Meeting rooms should be checked for recording devices before sensitive discussions
- Whiteboards should be erased after meetings
- Documents should not be left in meeting rooms
- Video conferencing equipment should be secured when not in use

### Shared Facilities

For organisations in shared buildings:
- [Organisation]'s perimeter should be clearly defined within the building
- Building management access should be controlled and logged
- Shared infrastructure (lifts, corridors) should not provide direct access to secure areas
- Key/card management for building access should be coordinated with building management

---

# Roles & Responsibilities

| Role | Accountability |
|------|----------------|
| **Executive Management** | Approve policy, allocate resources for physical security |
| **CISO** | Policy ownership, physical security standards |
| **Facilities Manager** | Physical security implementation, access control operations |
| **Reception/Security** | Visitor management, monitoring, incident response |
| **Line Managers** | Authorise access for team members, ensure compliance |
| **All Personnel** | Follow access procedures, report security incidents, challenge unknown persons |

**Escalation Path**:
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

**Governance Metrics (Quarterly Dashboard)**:

| Metric | Target | Measurement |
|--------|--------|-------------|
| Access control coverage | 100% of entry points | Access system inventory |
| Unauthorised access attempts | 0 successful | Access logs, incident reports |
| Visitor escort compliance | 100% | Visitor log review, spot checks |
| Access reviews completed on time | 100% | Review records |
| Badge loss/theft incidents | <5 per quarter | Incident reports |

## Exception Management

Physical access policy exceptions require:
- Documented business justification
- Risk assessment including compensating controls
- Facilities Manager recommendation
- CISO approval
- Time-limited approval (maximum 6 months)
- Quarterly review

---

# ISMS Integration

## Statement of Applicability

| Control | Status | Implementation Reference |
|---------|--------|-------------------------|
| **A.7.1 - Physical Security Perimeters** | Applicable | This policy, ISMS-IMP-A.7.1-2-3 |
| **A.7.2 - Physical Entry** | Applicable | This policy, ISMS-IMP-A.7.1-2-3 |
| **A.7.3 - Securing Offices, Rooms and Facilities** | Applicable | This policy, ISMS-IMP-A.7.1-2-3 |

## Related Controls

| Control | Relationship |
|---------|--------------|
| **A.7.4-5-11** | Physical monitoring, environmental protection, utilities |
| **A.7.6-7-14** | Secure areas working, clear desk, secure disposal |
| **A.5.15-16-18** | Logical access control integration |
| **A.5.24-28** | Physical security incident management |
| **A.6.7** | Remote working reduces on-site access requirements |

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

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

- ✅ This policy document (ISMS-POL-A.7.1-2-3 v1.0)
- ✅ Approval signatures from CISO, Facilities Manager, Executive Management
- ✅ Security perimeter requirements documented (Section 2.1)
- ✅ Entry control requirements documented (Section 2.2)
- ✅ Office/room security requirements documented (Section 2.3)
- ✅ Roles and responsibilities assigned (Section 3)

**Stage 2 (Operational Effectiveness) Evidence:**

**Evidence Repository and Generation**:

| Evidence Type | Repository Location | Generation Method | Owner | Retention |
|---------------|-------------------|-------------------|-------|-----------|
| Security zone documentation | [GRC Platform] - Physical Security | Facility security plans | Facilities Manager | Active + review |
| Access control logs | [Access Control System] | Automated logging | Security Team | 12 months |
| Visitor registers | [Reception System] or physical logs | Daily logging | Reception | 12 months |
| Access rights reviews | [GRC Platform] - Compliance Module | Quarterly reviews | Facilities Manager | 3 years |
| Perimeter inspection reports | [GRC Platform] - Physical Security | Annual inspections | Facilities Manager | 3 years |
| Physical security test results | [GRC Platform] - Audit Module | Annual testing | Internal Audit | 5 years |

**Evidence Accessibility**: All evidence SHALL be accessible to auditors upon request within 2 business days.

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

*This policy establishes [Organisation]'s requirements for physical access control. Implementation procedures are documented in ISMS-IMP-A.7.1-2-3.*

<!-- QA_VERIFIED: [Date] -->
