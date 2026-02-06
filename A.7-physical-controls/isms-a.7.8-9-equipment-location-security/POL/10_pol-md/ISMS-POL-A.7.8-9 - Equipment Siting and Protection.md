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
- ISMS-IMP-A.7.8-9-S1-UG/TG (Equipment Siting Assessment)
- ISMS-IMP-A.7.8-9-S2-UG/TG (Off-Premises Asset Security)
- ISMS-IMP-A.7.8-9-S3-UG/TG (Equipment Protection Compliance Dashboard)
- ISO/IEC 27001:2022 Controls A.7.8, A.7.9

---

## Executive Summary

This policy establishes [Organisation]'s requirements for equipment siting and protection, addressing both on-premises equipment placement and security of assets when used off-premises.

**Scope**: This policy applies to all information processing equipment owned, leased, or operated by [Organisation], including servers, network equipment, workstations, laptops, mobile devices, and supporting infrastructure.

**Purpose**: Define requirements for secure equipment placement, environmental protection, and security measures for assets used outside organisational premises. This policy establishes WHAT equipment protection requirements apply and WHO is responsible. Implementation procedures (HOW) are documented in ISMS-IMP-A.7.8-9.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, DORA, NIS2) apply where [Organisation]'s business activities trigger applicability.

**Combined Control Approach**: Controls A.7.8 (Equipment Siting and Protection) and A.7.9 (Security of Assets Off-Premises) are implemented together because they address complementary aspects of equipment protection throughout its operational lifecycle, both on-premises and off-premises.

---

**Control Alignment & Scope**

**ISO/IEC 27001:2022 Controls A.7.8 and A.7.9**

**ISO/IEC 27001:2022 Annex A.7.8 - Equipment Siting and Protection**

> *Equipment should be sited securely and protected.*

**ISO/IEC 27001:2022 Annex A.7.9 - Security of Assets Off-Premises**

> *Off-site assets should be protected.*

**Control Objectives**:

- Prevent loss, damage, theft, or compromise of equipment through secure placement
- Protect equipment from physical and environmental threats
- Ensure off-premises equipment maintains appropriate security
- Maintain operational continuity through proper equipment protection

**Control Type**: Preventive
**Control Category**: Physical

**This Policy Addresses**:

- Equipment siting and secure placement requirements
- Environmental and power protection for equipment
- Off-premises asset security and tracking
- Remote working equipment requirements

## What This Policy Does

This policy:

- **Defines** secure equipment placement and siting requirements
- **Establishes** off-premises asset protection requirements
- **Specifies** equipment tracking and accountability requirements
- **References** applicable regulatory requirements per ISMS-POL-00

## What This Policy Does NOT Do

This policy does NOT:

- **Define physical access control to equipment areas** (see ISMS-POL-A.7.1-2-3)
- **Specify environmental monitoring systems** (see ISMS-POL-A.7.4-5-11)
- **Detail remote working security procedures** (see ISMS-POL-A.6.7-8)
- **Provide equipment procurement specifications** (see ISMS-IMP-A.7.8-9)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite technology or facility changes
- Flexibility for different equipment types and locations
- Clear distinction between governance (policy) and execution (implementation)

## Scope

**This policy applies to**:

- Equipment: servers, network devices, workstations, laptops, mobile devices, storage systems, telecommunications equipment
- Locations: on-premises facilities, datacenters, remote offices, employee homes, travel locations
- Personnel: all employees, contractors, and third parties using organisation equipment
- Lifecycle: equipment siting, operation, maintenance, transport, and off-premises use

**Out of Scope**:

- Physical access control to equipment areas (covered by A.7.1-2-3)
- Environmental monitoring and protection systems (covered by A.7.4-5-11)
- Equipment disposal (covered by A.7.14)

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG** | All personal data processing | Article 8 - Technical measures appropriate to risk |
| **ISO/IEC 27001:2022** | Certification scope | Controls A.7.8, A.7.9 |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Requirements |
|-----------|-------------------|--------------|
| **EU GDPR** | Processing EU personal data, EU establishment, or offering services to EU | Art. 32 security of processing |
| **FINMA** | Swiss regulated financial institution | Physical security of ICT infrastructure |
| **DORA** | EU financial services entity | ICT asset protection requirements |
| **NIS2** | Essential/important entity (EU) | Physical security measures |

**Tier 2 Applicability**: Applicability decisions are recorded in the Compliance Obligations Register per ISMS-POL-00.

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- NIST SP 800-53 PE (Physical and Environmental Protection)
- TIA-942 (Datacenter standards)
- ASHRAE thermal guidelines
- Industry best practices for equipment protection

**Compliance Determination**: [Organisation] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent requirements apply where multiple regulations overlap.

---

# Policy Statements

## Equipment Siting Requirements (A.7.8)

### Secure Placement

Equipment processing or storing sensitive information SHALL be sited to reduce risks from physical and environmental threats and unauthorised access:

**Location Selection**:

- Equipment SHALL be placed in areas with controlled access
- Critical equipment SHALL be located away from public areas
- Equipment SHALL be positioned to minimise risk of overlooking (shoulder surfing)
- Screens displaying sensitive information SHALL be positioned away from windows and high-traffic areas

**Environmental Considerations**:

- Equipment SHALL be protected from temperature extremes, humidity, dust, and vibration
- Adequate ventilation and cooling SHALL be provided; acceptance criteria (temperature ranges, UPS runtime targets by equipment tier) are defined in ISMS-IMP-A.7.8-9.1
- Equipment SHALL be elevated or protected where flood risk exists
- Smoking, eating, and drinking SHALL be prohibited near sensitive equipment

**Security Measures**:

- Equipment SHALL be in areas with appropriate physical access controls
- Cable routing SHALL be protected from unauthorised access or damage
- Equipment SHALL be clearly labelled with asset tags (except where this creates security risk)
- Clear segregation SHALL exist between [Organisation]-owned equipment and equipment not under organisational control

### Power and Cabling Protection

**Power Supply**:

- Equipment SHALL be protected from power failures using appropriate UPS systems
- Power cables SHALL be protected from interception or damage
- Emergency power-off switches SHALL be located near equipment rooms
- Power supplies SHALL be redundant for critical equipment

**Network Cabling**:

- Network cables SHALL be protected from interception or damage
- Cable runs SHALL be documented and reviewed at least annually and upon material changes
- Fibre optic cables SHALL be used for high-security transmissions where appropriate
- Cabling closets SHALL have appropriate access controls

### Colocation and Third-Party Datacenters

Where equipment is hosted in colocation or third-party datacenters:

- [Organisation] SHALL ensure siting, physical access, and environmental protections are implemented via contractual requirements and periodic assurance (e.g., SOC 2 reports, ISO 27001 certification, on-site inspections where justified)
- Evidence of third-party compliance SHALL be retained in the Supplier Assurance repository and linked to the relevant asset/location record
- Acceptance criteria for third-party environmental and physical controls are defined in ISMS-IMP-A.7.8-9.1

### Industrial and Hostile Environments

Where equipment is located in industrial environments:

- Additional protective measures SHALL be implemented (dust covers, sealed enclosures)
- Equipment ratings SHALL match environmental conditions (IP ratings)
- Maintenance frequency SHALL be increased
- Environmental monitoring SHALL be enhanced

## Security of Assets Off-Premises (A.7.9)

### Authorisation and Tracking

**Removal Authorisation**:

- Removal of equipment from premises SHALL be authorised by appropriate management
- Authorisation records SHALL document: equipment details, purpose, responsible person, expected return date
- High-value or sensitive equipment removal SHALL require line manager approval

**Asset Tracking**:

- Equipment removed from premises SHALL be logged in the asset management system
- Chain of custody SHALL be maintained when equipment transfers between individuals
- Return of equipment SHALL be verified and recorded

### Off-Premises Protection Requirements

**Physical Security**:

- Equipment SHALL not be left unattended in public places
- Equipment SHALL be carried in unmarked bags during transport
- Equipment SHALL be secured in hotel safes or locked storage when not in use
- Vehicle storage SHALL only be used when absolutely necessary (boot/trunk, not visible)

**Environmental Protection**:

- Equipment SHALL be protected from extreme temperatures during transport
- Equipment SHALL not be exposed to direct sunlight for extended periods
- Moisture and humidity protection SHALL be maintained

**Theft Prevention**:

- Equipment SHALL be physically secured where possible (cable locks, lockdown plates)
- GPS tracking or location services SHALL be enabled on supported devices where legally permitted, approved, and proportionate; configuration SHALL minimise employee monitoring and be documented in the internal privacy policy with appropriate transparency notice to users
- Remote wipe capability SHALL be configured on all supported mobile devices and SHALL be tested at least annually and after significant MDM changes; evidence of testing SHALL be retained
- Equipment serial numbers SHALL be recorded for police reports if stolen

### Working Remotely

**Home Office Requirements**:

- Equipment SHALL be stored securely when not in use
- Network connections SHALL be secured (encrypted WiFi, VPN)
- Family members and visitors SHALL not have access to organisation equipment
- Physical screen locks SHALL be used when stepping away

**Public Spaces**:

- Privacy screens SHALL be used when working with sensitive information
- Public WiFi SHALL only be used with VPN protection
- Bluetooth and wireless connections SHALL be disabled when not required
- Equipment SHALL never be left unattended

### Permanently Off-Site Equipment

Where [Organisation] deploys equipment permanently installed outside organisational premises (e.g., edge appliances at customer sites, remote sensors), enhanced protection is required:

- Physical tamper detection SHALL be implemented
- Environmental monitoring SHALL be continuous
- Regular physical inspection schedules SHALL be established
- Remote monitoring and management capabilities SHALL be enabled
- Incident response procedures SHALL account for remote locations

---

# Roles and Responsibilities

## Accountability Matrix

| Role | Equipment Siting and Protection Responsibilities |
|------|--------------------------------------------------|
| **Executive Management** | Approve policy, allocate resources for equipment protection |
| **CISO** | Policy ownership, security standards for equipment protection |
| **Facilities Manager** | On-premises equipment siting, environmental controls |
| **IT Operations** | Equipment deployment, asset tracking, remote management |
| **Line Managers** | Authorise equipment removal, ensure team compliance |
| **All Personnel** | Protect equipment in their custody, report security incidents |

## Escalation Path

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

**Governance Metrics**:

- Equipment with compliant siting (target: 100%)
- Off-premises equipment with tracking (target: 100%)
- Equipment losses/thefts (target: 0)
- Overdue equipment returns (target: <5)
- Remote wipe capability enabled (target: 100% for mobile devices)

## Policy Review

- **Frequency**: Annual minimum
- **Triggers**: Equipment incidents, technology changes, facility changes, regulatory updates
- **Reviewers**: CISO, Facilities Manager, IT Operations
- **Approval**: Executive Management

## Exception Management

**Permitted Exceptions**:

- Equipment placement in non-standard locations for operational requirements (with enhanced monitoring)
- Extended off-premises periods for specific projects (with documented approval)
- Alternative protection measures for legacy equipment (with compensating controls)

**Exception Process**:

1. Document business justification
2. Risk assessment of deviation impact
3. CISO approval with compensating controls
4. Time-limited approval (maximum 6 months)
5. Documentation in exception register

**Not Permissible**:

- Equipment in uncontrolled areas without compensating controls
- Off-premises equipment without tracking capability
- Permanent exceptions to theft prevention requirements

All exceptions SHALL be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

## Corrective Action Linkage

Nonconformities related to this policy (e.g., improper equipment siting, lost equipment, missing tracking, unprotected off-premises assets) SHALL be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organisation]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- Equipment theft and damage risks inform siting requirements
- Off-premises risks addressed through protection requirements
- Risk treatment plans document equipment protection controls

**Statement of Applicability** (ISO 27001 Clause 6.1.3):

- Controls A.7.8 and A.7.9 applicability justified in [Organisation]'s SoA
- Implementation status tracked and reported

**Related Controls**:

| Control | Relationship |
|---------|--------------|
| **A.7.1-2-3** | Physical access control for areas where equipment is sited |
| **A.7.4-5-11** | Physical monitoring and environmental protection for equipment |
| **A.8.1** | User endpoint device security policies |
| **A.6.7** | Remote working security requirements |
| **A.5.9** | Asset inventory including equipment location tracking |

**Stacked Control Integration**:

A.7.8-9 (Equipment Siting and Protection) stacks with related controls:

| Stacked Control | Integration Point | A.7.8-9 Contribution |
|-----------------|-------------------|----------------------|
| **A.7.1-2-3** (Physical Access) | Equipment areas | A.7.1-2-3 controls area access; A.7.8-9 defines siting requirements |
| **A.7.4-5-11** (Infrastructure) | Environmental protection | A.7.4-5-11 provides monitoring; A.7.8-9 specifies equipment needs |
| **A.6.7** (Remote Working) | Off-premises equipment | A.6.7 defines working procedures; A.7.9 specifies equipment protection |

Assessment of A.7.8-9 should reference stacked control assessments for complete coverage.

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.7.8-9 Suite):

| Document ID | Title | Purpose |
|-------------|-------|---------|
| **ISMS-IMP-A.7.8-9.1-UG/TG** | Equipment Siting Assessment | Siting requirements verification |
| **ISMS-IMP-A.7.8-9.2-UG/TG** | Off-Premises Asset Management | Tracking and protection procedures |
| **ISMS-IMP-A.7.8-9.3-UG/TG** | Remote Equipment Security | Home and travel security procedures |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

Required Stage 1 evidence includes:

- This policy document (ISMS-POL-A.7.8-9 v1.0)
- Recorded approval by CISO, Facilities Manager, Executive Management
- Evidence of communication to relevant roles
- Equipment siting requirements documented (Equipment Siting Requirements)
- Off-premises security requirements documented (Security of Assets Off-Premises)
- Roles and responsibilities assigned (Roles and Responsibilities)

Evidence presence and status is tracked in the ISMS Evidence Register.

**Stage 2 (Operational Effectiveness) Evidence:**

Evidence required to demonstrate this policy is operationally effective:

- Equipment siting assessments with compliance verification
- Asset removal authorisations and return records
- Off-premises equipment tracking records
- Equipment incident reports (loss, theft, damage)
- Remote wipe capability verification reports
- MDM compliance reports for mobile devices
- Remote work security acknowledgments

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

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Facilities Manager** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for equipment siting and protection. Implementation procedures are documented in ISMS-IMP-A.7.8-9 (UG/TG).*

<!-- QA_VERIFIED: 2026-02-04 -->
