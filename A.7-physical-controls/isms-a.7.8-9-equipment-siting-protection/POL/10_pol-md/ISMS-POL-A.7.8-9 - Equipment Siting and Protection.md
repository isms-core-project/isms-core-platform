**ISMS-POL-A.7.8-9 — Equipment Siting and Protection**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Equipment Siting and Protection |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.7.8-9 |
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
- ISMS-POL-A.7.1-2-3 (Physical Access Control)
- ISMS-POL-A.7.4-5-11 (Physical Infrastructure Security)
- ISMS-IMP-A.7.8-9 (Implementation Guidance)
- ISO/IEC 27001:2022 Controls A.7.8, A.7.9

---

## Executive Summary

This policy establishes [Organisation]'s requirements for equipment siting and protection, addressing both on-premises equipment placement and security of assets when used off-premises.

**Purpose**: Define requirements for secure equipment placement, environmental protection, and security measures for assets used outside organisational premises. This policy establishes WHAT equipment protection requirements apply and WHO is responsible. Implementation procedures (HOW) are documented in ISMS-IMP-A.7.8-9.

**Scope**: All information processing equipment owned, leased, or operated by [Organisation], including servers, network equipment, workstations, laptops, mobile devices, and supporting infrastructure.

---

# Scope & Control Alignment

## ISO/IEC 27001:2022 Controls

### Control A.7.8 - Equipment Siting and Protection

> *Equipment should be sited securely and protected.*

**Control Objective**: Prevent loss, damage, theft, or compromise of assets and interruption to operations through secure equipment placement and protection measures.

### Control A.7.9 - Security of Assets Off-Premises

> *Off-site assets should be protected.*

**Control Objective**: Prevent loss, damage, theft, or compromise of off-site devices and interruption to operations.

**Control Type**: Preventive
**Control Category**: Physical

## Policy Scope

**This policy applies to**:

| Category | Scope |
|----------|-------|
| **Equipment** | Servers, network devices, workstations, laptops, mobile devices, storage systems, telecommunications equipment |
| **Locations** | On-premises facilities, datacenters, remote offices, employee homes, travel locations |
| **Personnel** | All employees, contractors, and third parties using organisation equipment |
| **Lifecycle** | Equipment siting, operation, maintenance, transport, and off-premises use |

## Regulatory Applicability

**Tier 1 - Mandatory Compliance** (All operations):

| Regulation | Key Requirements |
|------------|------------------|
| **Swiss nDSG** | Article 8 - Technical measures appropriate to risk |
| **EU GDPR** | Article 32 - Security of processing |
| **ISO/IEC 27001:2022** | Controls A.7.8, A.7.9 |

**Tier 2 - Conditional Applicability** (Triggered by business activities):

| Regulation | Trigger | Requirement |
|-----------|---------|-------------|
| **FINMA** | Swiss financial institution | Physical security of ICT infrastructure |
| **DORA** | EU financial services | ICT asset protection requirements |
| **NIS2** | Essential/important entity | Physical security measures |

---

# Policy Statements

## Equipment Siting Requirements

### Secure Placement

Equipment processing or storing sensitive information should be sited to reduce risks from physical and environmental threats and unauthorised access:

**Location Selection**:
- Equipment should be placed in areas with controlled access
- Critical equipment should be located away from public areas
- Equipment should be positioned to minimise risk of overlooking (shoulder surfing)
- Screens displaying sensitive information should be positioned away from windows and high-traffic areas

**Environmental Considerations**:
- Equipment should be protected from temperature extremes, humidity, dust, and vibration
- Adequate ventilation and cooling should be provided
- Equipment should be elevated or protected where flood risk exists
- Smoking, eating, and drinking should be prohibited near sensitive equipment

**Security Measures**:
- Equipment should be in areas with appropriate physical access controls
- Cable routing should be protected from unauthorised access or damage
- Equipment should be clearly labelled with asset tags (except where this creates security risk)
- Clear segregation should exist between [Organisation]-owned equipment and equipment not under organisational control

### Power and Cabling Protection

**Power Supply**:
- Equipment should be protected from power failures using appropriate UPS systems
- Power cables should be protected from interception or damage
- Emergency power-off switches should be located near equipment rooms
- Power supplies should be redundant for critical equipment

**Network Cabling**:
- Network cables should be protected from interception or damage
- Cable runs should be documented and regularly audited
- Fibre optic cables should be used for high-security transmissions where appropriate
- Cabling closets should have appropriate access controls

### Industrial and Hostile Environments

Where equipment is located in industrial environments:
- Additional protective measures should be implemented (dust covers, sealed enclosures)
- Equipment ratings should match environmental conditions (IP ratings)
- Maintenance frequency should be increased
- Environmental monitoring should be enhanced

## Security of Assets Off-Premises

### Authorisation and Tracking

**Removal Authorisation**:
- Removal of equipment from premises should be authorised by appropriate management
- Authorisation records should document: equipment details, purpose, responsible person, expected return date
- High-value or sensitive equipment removal should require line manager approval

**Asset Tracking**:
- Equipment removed from premises should be logged in the asset management system
- Chain of custody should be maintained when equipment transfers between individuals
- Return of equipment should be verified and recorded

### Off-Premises Protection Requirements

**Physical Security**:
- Equipment should not be left unattended in public places
- Equipment should be carried in unmarked bags during transport
- Equipment should be secured in hotel safes or locked storage when not in use
- Vehicle storage should only be used when absolutely necessary (boot/trunk, not visible)

**Environmental Protection**:
- Equipment should be protected from extreme temperatures during transport
- Equipment should not be exposed to direct sunlight for extended periods
- Moisture and humidity protection should be maintained

**Theft Prevention**:
- Equipment should be physically secured where possible (cable locks, lockdown plates)
- GPS tracking or location services should be enabled on supported devices
- Remote wipe capability should be configured and tested
- Equipment serial numbers should be recorded for police reports if stolen

### Working Remotely

**Home Office Requirements**:
- Equipment should be stored securely when not in use
- Network connections should be secured (encrypted WiFi, VPN)
- Family members and visitors should not have access to organisation equipment
- Physical screen locks should be used when stepping away

**Public Spaces**:
- Privacy screens should be used when working with sensitive information
- Public WiFi should only be used with VPN protection
- Bluetooth and wireless connections should be disabled when not required
- Equipment should never be left unattended

### Permanently Off-Site Equipment

Equipment permanently installed outside organisational premises (ATMs, remote sensors, edge devices) requires enhanced protection:

- Physical tamper detection should be implemented
- Environmental monitoring should be continuous
- Regular physical inspection schedules should be established
- Remote monitoring and management capabilities should be enabled
- Incident response procedures should account for remote locations

---

# Roles & Responsibilities

| Role | Accountability |
|------|----------------|
| **Executive Management** | Approve policy, allocate resources for equipment protection |
| **CISO** | Policy ownership, security standards for equipment protection |
| **Facilities Manager** | On-premises equipment siting, environmental controls |
| **IT Operations** | Equipment deployment, asset tracking, remote management |
| **Line Managers** | Authorise equipment removal, ensure team compliance |
| **All Personnel** | Protect equipment in their custody, report security incidents |

**Escalation Path**:
- Equipment security concerns: Employee → Line Manager → IT Operations → CISO
- Equipment loss/theft: Employee → IT Operations (immediate) → CISO → Executive Management

---

# Governance & Compliance

## Assessment Framework

| Assessment | Frequency | Owner | Evidence |
|------------|-----------|-------|----------|
| Equipment siting review | Annual | Facilities Manager | Siting assessments |
| Off-premises equipment audit | Semi-annual | IT Operations | Asset tracking records |
| Remote work security review | Annual | CISO | Compliance checks |
| Equipment removal log review | Quarterly | IT Operations | Authorisation records |

**Governance Metrics (Quarterly Dashboard)**:

| Metric | Target | Measurement |
|--------|--------|-------------|
| Equipment with compliant siting | 100% | Siting assessment results |
| Off-premises equipment with tracking | 100% | Asset management records |
| Equipment losses/thefts | 0 | Incident records |
| Overdue equipment returns | <5 | Asset tracking system |
| Remote wipe capability enabled | 100% (mobile devices) | MDM compliance reports |

## Exception Management

Equipment protection policy exceptions require:
- Documented business justification
- Risk assessment of deviation impact
- Compensating controls specification
- CISO approval
- Time-limited approval (maximum 6 months)
- Quarterly review for continued necessity

---

# ISMS Integration

## Statement of Applicability

| Control | Status | Implementation Reference |
|---------|--------|-------------------------|
| **A.7.8 - Equipment Siting and Protection** | Applicable | This policy, ISMS-IMP-A.7.8-9 |
| **A.7.9 - Security of Assets Off-Premises** | Applicable | This policy, ISMS-IMP-A.7.8-9 |

## Related Controls

| Control | Relationship |
|---------|--------------|
| **A.7.1-2-3** | Physical access control for areas where equipment is sited |
| **A.7.4-5-11** | Physical monitoring and environmental protection for equipment |
| **A.8.1** | User endpoint device security policies |
| **A.6.7** | Remote working security requirements |
| **A.5.9** | Asset inventory including equipment location tracking |

---

# Definitions

| Term | Definition |
|------|------------|
| **Equipment Siting** | The secure placement and positioning of information processing equipment |
| **Off-Premises Assets** | Organisation equipment used outside organisational facilities |
| **Chain of Custody** | Documented transfer of equipment responsibility between individuals |
| **Remote Wipe** | Capability to erase data from a device remotely |
| **Tamper Detection** | Mechanisms to detect unauthorised physical access to equipment |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

- ✅ This policy document (ISMS-POL-A.7.8-9 v1.0)
- ✅ Approval signatures from CISO, Facilities Manager, Executive Management
- ✅ Equipment siting requirements documented (Section 2.1)
- ✅ Off-premises security requirements documented (Section 2.2)
- ✅ Roles and responsibilities assigned (Section 3)

**Stage 2 (Operational Effectiveness) Evidence:**

**Evidence Repository and Generation**:

| Evidence Type | Repository Location | Generation Method | Owner | Retention |
|---------------|-------------------|-------------------|-------|-----------|
| Equipment siting assessments | [GRC Platform] - Physical Security Module | Annual facility reviews | Facilities Manager | 3 years |
| Asset removal authorisations | [Asset Management System] | Per removal request | IT Operations | 3 years |
| Off-premises equipment tracking | [Asset Management System] | Continuous tracking | IT Operations | Active + 1 year |
| Equipment incident reports | [GRC Platform] - Incident Module | Per incident | CISO | 5 years |
| Remote wipe capability reports | [MDM Platform] | Monthly compliance reports | IT Operations | 3 years |

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

*This policy establishes [Organisation]'s requirements for equipment siting and protection. Implementation procedures are documented in ISMS-IMP-A.7.8-9.*

<!-- QA_VERIFIED: [Date] -->
