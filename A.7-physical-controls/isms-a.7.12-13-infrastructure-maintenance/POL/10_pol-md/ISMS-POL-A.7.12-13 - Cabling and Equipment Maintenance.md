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
- ISMS-IMP-A.7.12-13 (Implementation Guidance)
- ISO/IEC 27001:2022 Controls A.7.12, A.7.13

---

## Executive Summary

This policy establishes [Organisation]'s requirements for cabling security and equipment maintenance, ensuring infrastructure integrity and operational continuity.

**Purpose**: Define requirements for protecting cabling infrastructure and maintaining equipment to ensure availability, integrity, and confidentiality of information. This policy establishes WHAT infrastructure requirements apply and WHO is responsible. Implementation procedures (HOW) are documented in ISMS-IMP-A.7.12-13.

**Scope**: All power and telecommunications cabling, and all equipment containing or supporting information processing.

---

# Scope & Control Alignment

## ISO/IEC 27001:2022 Controls

### Control A.7.12 - Cabling Security

> *Cables carrying power, data or supporting information services should be protected from interception, interference or damage.*

**Control Objective**: Protect power and communications cables from interception, interference, and damage.

### Control A.7.13 - Equipment Maintenance

> *Equipment should be maintained correctly to ensure availability, integrity and confidentiality of information.*

**Control Objective**: Prevent loss, damage, theft, or compromise of information due to lack of maintenance, and ensure operational continuity.

**Control Type**: Preventive
**Control Category**: Physical

## Policy Scope

**This policy applies to**:

| Category | Scope |
|----------|-------|
| **Cabling** | Power cables, network cables (copper and fibre), telecommunications cables |
| **Equipment** | Servers, network devices, storage systems, UPS, HVAC, security systems |
| **Facilities** | Datacenters, server rooms, wiring closets, office areas |
| **Activities** | Cable installation, maintenance, equipment servicing, repairs |

## Regulatory Applicability

**Tier 1 - Mandatory Compliance** (All operations):

| Regulation | Key Requirements |
|------------|------------------|
| **Swiss nDSG** | Article 8 - Technical measures appropriate to risk |
| **EU GDPR** | Article 32 - Security of processing |
| **ISO/IEC 27001:2022** | Controls A.7.12, A.7.13 |

**Tier 2 - Conditional Applicability** (Triggered by business activities):

| Regulation | Trigger | Requirement |
|-----------|---------|-------------|
| **FINMA** | Swiss financial institution | ICT infrastructure resilience |
| **DORA** | EU financial services | ICT operational resilience |
| **NIS2** | Essential/important entity | Infrastructure protection |

---

# Policy Statements

## Cabling Security

### Cable Protection

Cables carrying power, data, or supporting information services should be protected:

**Physical Protection**:
- Cables should be routed through protected pathways (conduits, cable trays, raised floors)
- Underground cabling should be protected against accidental damage (armoured conduits)
- Cables should be protected from electromagnetic interference
- Cable routes should avoid areas with high risk of damage (water, heat, physical impact)

**Access Control**:
- Cabling infrastructure (patch panels, distribution frames) should be in secured areas
- Wiring closets should have access controls and be locked when unoccupied
- Cable routes should not be accessible to unauthorised personnel
- Manhole and duct access should be controlled and logged

### Segregation Requirements

**Power and Data Separation**:
- Power cables should be segregated from communications cables to prevent interference
- Minimum separation distances should comply with industry standards
- Where crossing is unavoidable, cables should cross at right angles

**Network Segregation**:
- Cables carrying different security classifications should be physically separated where feasible
- High-security network cables should be clearly identified (colour coding or labelling)
- Fibre optic cables should be used for high-security transmissions where interception risk exists

### Cable Documentation and Management

**Documentation**:
- Cable infrastructure should be documented (cable schedules, diagrams)
- Documentation should be maintained as current
- Documentation should be secured and access-controlled

**Labelling**:
- Cables should be labelled at both ends
- Labels should enable identification without detailed documentation
- Patch panels and distribution frames should be clearly labelled

**Change Control**:
- Cabling changes should follow change management process
- Unused cables should be disconnected and documented
- Regular audits should identify unauthorised additions or changes

### Inspection and Maintenance

- Regular inspections should identify cable damage or deterioration
- Cable infrastructure should be included in maintenance schedules
- Damaged cables should be repaired or replaced promptly
- Inspection findings should be documented

## Equipment Maintenance

### Maintenance Programme

[Organisation] should establish and implement a maintenance programme for all equipment:

**Programme Requirements**:
- All equipment should be included in maintenance programme
- Maintenance schedules should follow manufacturer recommendations
- Critical equipment should have preventive maintenance schedules
- Maintenance records should be maintained

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
- Only authorised personnel should perform maintenance
- Maintenance personnel should be identified and verified
- Third-party maintenance should be contracted with approved providers

**Supervision**:
- Maintenance personnel should be supervised when accessing sensitive equipment
- Unsupervised maintenance access should be logged and monitored
- Remote maintenance should be subject to access controls

### Security During Maintenance

**Data Protection**:
- Sensitive data should be protected during maintenance activities
- Equipment containing data should not leave premises for maintenance where avoidable
- If off-site maintenance required, data should be securely erased first
- Maintenance personnel should not have access to data unless specifically required

**Access Controls**:
- Maintenance access should be time-limited
- Access should be logged (who, what, when, why)
- All tools and equipment should be accounted for after maintenance
- Physical inspection should verify no unauthorised modifications

### Remote Maintenance

**Remote Access Requirements**:
- Remote maintenance should be authorised and documented
- Remote access should use secure connections (VPN, encrypted)
- Remote sessions should be logged and monitored
- Remote access should be disabled when not actively required

### Equipment Removal for Maintenance

When equipment must be removed from premises for maintenance:
- Removal should be authorised by equipment owner
- Data should be securely erased before removal (per A.7.14)
- Chain of custody should be maintained
- Equipment should be inspected upon return
- Return should be logged in asset management system

### Maintenance Records

**Documentation Requirements**:
- All maintenance should be documented
- Records should include: date, equipment, work performed, personnel, findings
- Records should be retained per retention schedule (minimum 3 years)
- Records should be available for audit

---

# Roles & Responsibilities

| Role | Accountability |
|------|----------------|
| **Executive Management** | Approve policy, allocate resources |
| **CISO** | Policy ownership, security standards |
| **IT Operations Manager** | Equipment maintenance programme, vendor management |
| **Facilities Manager** | Cabling infrastructure, building maintenance |
| **System Owners** | Ensure owned equipment is maintained |
| **IT Operations** | Day-to-day maintenance, documentation |

**Escalation Path**:
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

**Governance Metrics (Quarterly Dashboard)**:

| Metric | Target | Measurement |
|--------|--------|-------------|
| Preventive maintenance completion | 100% on schedule | Maintenance records |
| Equipment failures due to maintenance gaps | 0 | Incident analysis |
| Cabling documentation accuracy | >95% | Audit findings |
| Unauthorised cabling changes detected | 0 | Audit findings |
| Maintenance-related security incidents | 0 | Incident reports |

## Exception Management

Policy exceptions require:
- Documented business justification
- Risk assessment
- Compensating controls
- IT Operations Manager + CISO approval
- Time-limited approval (maximum 6 months)

---

# ISMS Integration

## Statement of Applicability

| Control | Status | Implementation Reference |
|---------|--------|-------------------------|
| **A.7.12 - Cabling Security** | Applicable | This policy, ISMS-IMP-A.7.12-13 |
| **A.7.13 - Equipment Maintenance** | Applicable | This policy, ISMS-IMP-A.7.12-13 |

## Related Controls

| Control | Relationship |
|---------|--------------|
| **A.7.4-5-11** | Physical monitoring, environmental protection, utilities |
| **A.7.8-9** | Equipment siting and off-premises security |
| **A.7.14** | Secure disposal when equipment retired |
| **A.8.6** | Capacity management informs maintenance planning |
| **A.8.32** | Change management for infrastructure changes |

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

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

- ✅ This policy document (ISMS-POL-A.7.12-13 v1.0)
- ✅ Approval signatures from CISO, IT Operations Manager, Executive Management
- ✅ Cabling security requirements documented (Section 2.1)
- ✅ Equipment maintenance requirements documented (Section 2.2)
- ✅ Roles and responsibilities assigned (Section 3)

**Stage 2 (Operational Effectiveness) Evidence:**

**Evidence Repository and Generation**:

| Evidence Type | Repository Location | Generation Method | Owner | Retention |
|---------------|-------------------|-------------------|-------|-----------|
| Cable documentation | [Network Documentation System] | Network diagrams, cable schedules | Facilities/IT | Active + updates |
| Cabling inspection reports | [GRC Platform] - Physical Security | Annual inspections | Facilities Manager | 3 years |
| Maintenance schedules | [CMMS/ITSM System] | Preventive maintenance planning | IT Operations | Active |
| Maintenance records | [CMMS/ITSM System] | Per maintenance event | IT Operations | 5 years |
| Vendor maintenance reports | [Vendor Portal/GRC Platform] | Per vendor visit | IT Operations | 3 years |
| Remote maintenance logs | [Remote Access System] | Automated logging | IT Security | 12 months |

**Evidence Accessibility**: All evidence SHALL be accessible to auditors upon request within 2 business days.

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

*This policy establishes [Organisation]'s requirements for cabling security and equipment maintenance. Implementation procedures are documented in ISMS-IMP-A.7.12-13.*

<!-- QA_VERIFIED: [Date] -->
