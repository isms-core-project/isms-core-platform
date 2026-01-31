# ISMS-POL-A.7.4-5-11-S1: Executive Summary, Control Alignment & Scope

**Document Classification:** Internal - ISMS Policy  
**Version:** 1.0  
**Effective Date:** [To be defined]  
**Review Cycle:** Annual  
**Policy Owner:** Chief Information Security Officer (CISO)  
**Approved By:** [Approval Authority]

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Operations Manager / Facilities Manager / CISO | Initial policy framework for unified physical infrastructure security controls |

**Review Schedule:** Annual review or upon significant facility changes, security incidents, or regulatory updates  
**Next Review Date:** [Approval Date + 12 months]  
**Distribution:** CISO, Security Operations, Facilities Management, System Owners, Auditors

---

## Table of Contents

1. [ISO 27001:2022 Control Text](#1-iso-270012022-control-text)
2. [Executive Summary](#2-executive-summary)
3. [Scope and Applicability](#3-scope-and-applicability)
4. [Integration Architecture](#4-integration-architecture)
5. [Regulatory and Compliance Context](#5-regulatory-and-compliance-context)
6. [Roles and Responsibilities](#6-roles-and-responsibilities)
7. [Framework Overview](#7-framework-overview)
8. [Related Documents](#8-related-documents)

---

## 1. ISO 27001:2022 Control Text

This section provides the complete control text from ISO/IEC 27001:2022 for all three controls addressed by this unified Physical Infrastructure Security Framework.

### 1.1 Control A.7.4 - Physical Security Monitoring

**Control Type:** Technical  
**Information Security Properties:** Availability, Confidentiality, Integrity  
**Cybersecurity Concepts:** Detect, Respond  
**Operational Capabilities:** Physical Security  
**Security Domains:** Protection

**Control Text:**
> Premises shall be continuously monitored for unauthorized physical access.

**Purpose:**
To detect and respond to unauthorized physical access to premises, facilities and information processing areas.

**ISO 27002:2022 Guidance Summary:**
- Physical access monitoring should be implemented to detect unauthorized access attempts
- Monitoring mechanisms can include security guards, video surveillance (CCTV), access control logs, and intrusion detection systems
- Monitoring should be continuous or at appropriate intervals based on risk assessment
- Access logs should be regularly reviewed to identify unauthorized or anomalous access patterns
- Visitor access should be monitored and supervised through sign-in procedures and escort requirements
- Physical security events should be recorded, analyzed, and integrated with logical security monitoring where appropriate
- Alarm systems should be implemented to alert security personnel of unauthorized access attempts
- Monitoring effectiveness should be periodically tested through security audits and penetration testing

### 1.2 Control A.7.5 - Protecting Against Physical and Environmental Threats

**Control Type:** Technical  
**Information Security Properties:** Availability, Integrity  
**Cybersecurity Concepts:** Protect  
**Operational Capabilities:** Physical Security, Business Continuity  
**Security Domains:** Protection

**Control Text:**
> Protection against physical and environmental threats, such as natural disasters, malicious attack or accidents shall be designed and implemented.

**Purpose:**
To prevent physical and environmental damage to information processing facilities and information assets.

**ISO 27002:2022 Guidance Summary:**
- Protection should address natural disasters (floods, earthquakes, hurricanes, tornadoes), deliberate malicious acts (arson, vandalism, terrorism), and accidents (fires, water damage, equipment failure)
- Fire detection and suppression systems should be installed, tested, and maintained in accordance with local regulations
- Water damage protection should include flood risk assessment, water detection sensors, drainage systems, and equipment elevation
- Environmental monitoring should include temperature and humidity controls appropriate for information processing equipment
- Facilities should be constructed or reinforced to withstand identified environmental threats based on geographic location
- Physical access barriers (perimeter fencing, vehicle barriers, secure construction) should be implemented to protect against physical threats
- Emergency response procedures should be documented and regularly tested for various threat scenarios
- Equipment should be protected against power fluctuations, electromagnetic interference, and other environmental disruptions
- Insurance coverage should be considered to address financial impacts of physical and environmental incidents

### 1.3 Control A.7.11 - Supporting Utilities

**Control Type:** Technical  
**Information Security Properties:** Availability  
**Cybersecurity Concepts:** Protect  
**Operational Capabilities:** Physical Security, Business Continuity  
**Security Domains:** Protection

**Control Text:**
> Information processing facilities shall be protected from power failures and other disruptions caused by failures in supporting utilities.

**Purpose:**
To ensure the continued availability of information processing facilities in the event of utility disruptions.

**ISO 27002:2022 Guidance Summary:**
- Supporting utilities include power supply, telecommunications, water supply (if used for cooling), heating/ventilation/air conditioning (HVAC), and other essential infrastructure
- Uninterruptible Power Supply (UPS) systems should be installed to provide short-term power during utility failures and allow graceful system shutdown
- Backup generators should be considered for critical facilities requiring extended operation during power outages
- Power supply systems should be tested regularly to verify functionality and capacity
- Telecommunications infrastructure should include redundancy through diverse carrier paths and backup connectivity methods
- HVAC systems should maintain appropriate temperature and humidity levels for information processing equipment
- Cooling redundancy should be implemented for critical facilities to prevent equipment overheating
- Utility monitoring systems should provide real-time visibility into power, cooling, and connectivity status
- Utility failure procedures should be documented and tested to ensure orderly shutdown or failover to backup systems
- Fuel supply for backup generators should be monitored and maintained with sufficient capacity for extended outages

---

## 2. Executive Summary

### 2.1 Why Unified Framework?

This Physical Infrastructure Security Framework addresses three ISO 27001:2022 Annex A controls as an integrated system rather than separate implementations. These controls are fundamentally interconnected and require coordinated implementation to achieve genuine physical security:

**A.7.4 (Physical Security Monitoring)** monitors WHO enters physical facilities and WHAT happens inside through access control systems, video surveillance, intrusion detection, and security personnel. Without monitoring, physical access controls (A.7.1-3) cannot detect violations or unauthorized access.

**A.7.5 (Protecting Against Physical and Environmental Threats)** protects facilities from ENVIRONMENTAL hazards including fire, flood, temperature extremes, and structural threats. Environmental protection systems require monitoring integration (A.7.4) and depend on reliable utilities (A.7.11) to function.

**A.7.11 (Supporting Utilities)** ensures UTILITY infrastructure (power, cooling, telecommunications) remains available and resilient. Utility failures directly impact environmental protection systems (fire suppression, HVAC) and physical monitoring systems (access control, CCTV), creating cascading failures.

**Attempting to implement these controls separately would result in:**
- Disconnected physical security and environmental monitoring (no integrated alerting)
- Redundant facilities risk assessments (separate assessments for physical, environmental, utility risks)
- Fragmented utility management (UPS protects access control but not HVAC)
- Inefficient evidence collection (separate logs, separate audits, separate compliance reporting)
- Single points of failure (environmental protection depends on power, but power is managed separately)

**Unified framework benefits:**
- Integrated threat assessment (natural disasters affect physical access, environment, and utilities simultaneously)
- Coordinated monitoring and alerting (single dashboard for physical, environmental, and utility events)
- Efficient resource allocation (shared infrastructure: UPS protects access control AND environmental sensors)
- Streamlined evidence collection (unified assessment approach, single compliance dashboard)
- Holistic risk management (dependencies between controls explicitly addressed)

### 2.2 Framework Overview

This Physical Infrastructure Security Framework provides comprehensive guidance across three security domains:

**Physical Monitoring Domain (A.7.4):**
- Access control systems (badge readers, logs, visitor management)
- Video surveillance (CCTV coverage, retention, review procedures)
- Intrusion detection (motion sensors, door/window sensors, glass break detectors)
- Security personnel (guards, patrols, Security Operations Center)
- Alarm systems (types, monitoring, response procedures)
- Integration with security operations (SIEM, incident management)

**Environmental Protection Domain (A.7.5):**
- Environmental threat risk assessment (natural disasters, fire, flood, temperature)
- Fire detection and suppression (smoke detectors, sprinklers, gas suppression)
- Flood and water damage protection (sensors, drainage, equipment elevation)
- Temperature and humidity control (HVAC monitoring, environmental sensors)
- Structural protection (seismic, wind resistance, equipment anchoring)
- Physical access barriers (perimeter fencing, vehicle barriers, secure construction)
- Environmental protection plan (threat response procedures, equipment relocation)

**Utility Resilience Domain (A.7.11):**
- Power supply resilience (UPS, backup generators, redundancy levels)
- HVAC and cooling (capacity planning, redundancy, monitoring)
- Telecommunications infrastructure (ISP redundancy, diverse paths, failover)
- Water supply (if applicable for cooling systems)
- Utility failure procedures (power loss response, HVAC failure response, telecommunications outage response)
- Utility monitoring (real-time status, alerting, performance dashboards)

### 2.3 Target Audience

This framework is designed for multiple stakeholders:

**Implementers:**
- Chief Information Security Officer (CISO) - overall accountability
- Security Operations Manager - physical security monitoring implementation
- Facilities Manager - environmental protection and utility management
- System Owners - equipment-level physical security requirements
- IT Operations - integration with logical security controls

**Auditors and Compliance:**
- Internal Auditors - annual compliance verification
- External Auditors - ISO 27001 certification audits
- Regulatory Authorities - industry-specific compliance (FINMA, DORA, NIS2)
- Management - risk oversight and resource allocation

**Daily Operations:**
- Security Personnel - monitoring, patrol, incident response
- Facilities Technicians - maintenance, testing, incident response
- Help Desk / NOC - escalation, coordination
- Vendors and Contractors - maintenance service providers

---

## 3. Scope and Applicability

### 3.1 Physical Environment Scope

This framework applies to all facilities where [Organization] processes, stores, or transmits information assets:

**On-Premises Datacenters:**
- Primary datacenter facilities
- Disaster recovery sites
- Server rooms within office buildings
- Telecommunications closets
- Equipment cages

**Office Facilities:**
- Corporate headquarters
- Regional offices
- Branch offices
- Remote offices
- Home offices (where organization-owned equipment is located)

**Colocation Facilities:**
- Leased datacenter space (cages, suites, cabinets)
- Managed hosting environments
- Shared infrastructure facilities
- Responsibility matrix applies (see Section 3.4)

**Remote and Temporary Facilities:**
- Pop-up offices
- Temporary workspaces
- Mobile command centers (if applicable)

**Geographic Scope:**
- All facilities globally where [Organization] operates
- Geographic-specific threat considerations apply (see Section 3.3)

### 3.2 Cloud-Only Organizations

**CRITICAL APPLICABILITY NOTE:**

If [Organization] operates **100% in cloud environments** (AWS, Azure, GCP, etc.) with **no on-premises datacenters, server rooms, or information processing facilities**, these controls may be marked as **"Not Applicable"** in the Statement of Applicability (SoA).

**Rationale:**
- Cloud providers are responsible for physical infrastructure security (datacenters, power, cooling, physical access)
- [Organization's] responsibility is to assess cloud provider physical security controls through supplier management (ISO 27001:2022 Control A.5.19-23: Information Security for Use of Cloud Services)
- Cloud provider physical security is verified through audit reports (SOC 2 Type II, ISO 27001 certification) rather than direct implementation

**Statement of Applicability Language (if applicable):**
```
Control A.7.4 - Physical Security Monitoring: Not Applicable - Cloud Environment
Control A.7.5 - Protecting Against Physical and Environmental Threats: Not Applicable - Cloud Environment  
Control A.7.11 - Supporting Utilities: Not Applicable - Cloud Environment

Justification: [Organization] operates 100% in cloud infrastructure (AWS/Azure/GCP) with no on-premises datacenters, server rooms, or information processing facilities. Physical infrastructure security is the cloud provider's responsibility. [Organization] assesses cloud provider physical security controls through supplier management (Control A.5.19-23) including review of SOC 2 Type II and ISO 27001 audit reports covering physical security, environmental protection, and utility resilience.

Office physical security is addressed through Control A.7.1-3 (Physical Access Control) for office premises only.
```

**Hybrid Cloud Organizations:**
- If [Organization] operates BOTH cloud and on-premises infrastructure, these controls apply to on-premises facilities only
- Cloud portion assessed via A.5.19-23 (supplier management)
- Clear documentation of which facilities are in scope vs. out of scope

**Office Physical Security:**
- Even cloud-only organizations typically have office premises
- Office physical security (building access, visitor management, basic environmental protection) is still required
- Apply Control A.7.1-3 (Physical Access Control) for office security
- These controls (A.7.4/5/11) focus on information processing facilities, not general office security

### 3.3 Geographic Applicability and Threat Diversity

This framework is **location-agnostic** and adapts to geographic-specific threats:

**Environmental Threat Variation by Geography:**

**Earthquake Zones (e.g., California, Japan, New Zealand):**
- Enhanced structural protection requirements
- Equipment anchoring and seismic mounts mandatory
- Seismic-resistant building design verification
- Post-earthquake inspection procedures

**Hurricane/Typhoon Zones (e.g., Florida, Caribbean, Southeast Asia):**
- Wind-resistant construction verification
- Generator fuel supply for extended outages (3-7 days)
- Emergency generator testing before hurricane season
- Roof and window protection measures

**Flood Zones (e.g., Netherlands, Bangladesh, coastal areas):**
- Equipment elevation requirements (raised floors, elevated racks)
- Flood barrier systems (sandbags, temporary barriers)
- Water detection sensors mandatory
- Drainage system verification

**Extreme Temperature Zones (e.g., Arctic, desert regions):**
- Enhanced HVAC capacity for extreme temperatures
- Equipment cold-start procedures (Arctic)
- Heat mitigation for extreme heat (desert)
- Temperature monitoring with wider alert thresholds

**Implementation Approach:**
- Perform location-specific environmental threat assessment (see POL-S3, Section 2)
- Apply threat-specific mitigation controls based on assessment
- Document geographic considerations in facilities risk register
- Review threat landscape annually or when opening new facilities

### 3.4 Colocation Facilities - Shared Responsibility Model

When [Organization] utilizes colocation datacenter space, physical infrastructure responsibilities are shared between the colocation provider and [Organization]:

**Colocation Provider Responsibilities (Typical):**
- Perimeter physical security (fencing, vehicle barriers, building access control)
- Building-wide CCTV and intrusion detection
- Fire detection and suppression (facility-wide)
- HVAC and environmental controls (facility-wide)
- Primary power (utility), UPS, backup generators (facility-wide)
- Building structure and seismic/wind protection
- 24/7 security personnel and monitoring

**[Organization] Customer Responsibilities (Typical):**
- Cage/suite access control (secondary access layer)
- Internal CCTV within cage/suite (optional but recommended)
- Equipment-level environmental monitoring (temperature sensors within cage)
- Equipment-level UPS (optional, for network equipment)
- Physical security of equipment (rack locks, cable locks)
- Visitor escort within cage/suite area

**Responsibility Matrix Documentation:**
- Maintain formal responsibility matrix in colocation contract
- Document which controls are provider-managed vs. customer-managed
- Verify provider controls through audit reports (SOC 2 Type II, ISO 27001, Uptime Institute Tier Certification)
- Review provider SLAs for physical security, environmental protection, and utility uptime
- Conduct periodic verification (annual review of provider audit reports)

**Evidence Collection for Colocation:**
- Provider audit reports (SOC 2 Type II, ISO 27001)
- Provider SLA reports (power uptime, HVAC uptime, physical security incidents)
- Provider datacenter tier certification (Uptime Institute)
- Customer-implemented controls evidence (cage access logs, equipment-level monitoring)
- Incident reports (provider incidents affecting customer, customer incidents)

### 3.5 Facility Criticality Tiers

Facilities are classified into two criticality tiers with corresponding control requirements:

**Tier 1 - Critical Facilities:**
- **Definition:** Datacenters, primary server rooms, critical infrastructure hosting
- **Characteristics:** 24/7 operations, high availability requirements, significant business impact if unavailable
- **Examples:** Production datacenters, disaster recovery sites, core network infrastructure rooms

**Control Requirements:**
- Physical monitoring: 24/7 access control, CCTV, intrusion detection, security personnel
- Environmental protection: Pre-action sprinklers or gas suppression, continuous temperature monitoring, comprehensive threat protection
- Utility resilience: UPS 15+ min runtime, backup generator 24+ hours, N+1 redundancy (power, HVAC), dual ISP with diverse paths

**Tier 2 - Standard Facilities:**
- **Definition:** Office buildings, branch offices, non-critical server rooms
- **Characteristics:** Business hours operations, standard availability requirements, moderate business impact if unavailable
- **Examples:** Corporate offices, regional offices, small server rooms supporting local operations

**Control Requirements:**
- Physical monitoring: Business hours access control with after-hours alarms, CCTV (business hours or motion-triggered), basic intrusion detection
- Environmental protection: Standard sprinklers, temperature monitoring (business hours or threshold alerts), basic threat protection
- Utility resilience: UPS 5+ min runtime, backup generator (risk-based, optional), N configuration (no redundancy), single ISP with SLA

**Tier Assignment:**
- Facilities classified based on Business Impact Analysis (BIA)
- Tier assignment reviewed annually or upon significant facility changes
- Documented in facilities risk register

---

## 4. Integration Architecture

### 4.1 Integration with Other ISO 27001:2022 Controls

This Physical Infrastructure Security Framework integrates with multiple other controls:

**A.7.1, A.7.2, A.7.3 - Physical Access Control (Entry/Exit Baseline):**
- A.7.1-3 establishes baseline physical access controls (perimeter security, entry controls, secure areas)
- A.7.4 (this framework) extends with monitoring and detection capabilities
- Integration point: Access control logs from A.7.1-3 feed monitoring systems in A.7.4
- Dependency: Physical access control (A.7.1-3) is prerequisite for physical security monitoring (A.7.4)

**A.8.13, A.8.14, A.5.30 - Business Continuity and Disaster Recovery:**
- Environmental threats (A.7.5) directly inform BC/DR planning
- Utility resilience (A.7.11) determines Recovery Time Objectives (RTO) achievability
- Backup power capacity (A.7.11) must support backup/recovery operations (A.8.13)
- Integration point: Physical disaster scenarios feed BC/DR plan, BC/DR testing validates physical controls
- Dependency: Physical infrastructure resilience enables information backup and continuity

**A.5.19-23 - Information Security for Use of Cloud Services:**
- Cloud provider physical security assessed via supplier management (A.5.19-23)
- Physical infrastructure controls (A.7.4/5/11) apply to on-premises only
- Integration point: Cloud provider SOC 2/ISO 27001 reports evaluated for physical security
- Dependency: Cloud-only organizations substitute supplier assessment for direct implementation

**A.8.6 - Capacity Management:**
- Utility capacity planning (A.7.11) informs overall capacity management
- Power, cooling, and network capacity must align with IT capacity growth
- Integration point: Facilities capacity planning coordinates with IT capacity planning
- Dependency: Physical infrastructure capacity enables information processing capacity

**A.5.24, A.5.25, A.5.26, A.5.27 - Incident Management:**
- Physical security incidents (breaches, environmental events, utility failures) managed via incident management process
- Physical security monitoring (A.7.4) detects and escalates incidents
- Integration point: Physical security events feed incident management system, incident response procedures coordinate physical and logical response
- Dependency: Incident management process handles physical security incidents

**A.8.7 - Protection Against Malware:**
- Physical access control prevents unauthorized installation of malicious hardware
- Environmental protection (temperature, humidity) prevents equipment failure that could bypass malware protection
- Integration point: Physical security log correlation with malware detection events
- Dependency: Physical security prevents physical attack vectors for malware

### 4.2 Three-Control Integration Model

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PHYSICAL INFRASTRUCTURE SECURITY                  │
│                         Unified Framework                            │
└─────────────────────────────────────────────────────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────────┐    ┌───────────────────┐    ┌───────────────────┐
│   A.7.4 MONITOR   │    │   A.7.5 PROTECT   │    │ A.7.11 RESILIENCE │
│                   │    │                   │    │                   │
│ • Access Control  │    │ • Fire Detection  │    │ • UPS / Generator │
│ • CCTV Surveil.   │    │ • Fire Suppress.  │    │ • HVAC / Cooling  │
│ • Intrusion Det.  │    │ • Water Detect.   │    │ • ISP Redundancy  │
│ • Security Guard  │    │ • Temp/Humidity   │    │ • Utility Monitor │
│ • Alarm Systems   │    │ • Structural Prot.│    │ • Failure Proced. │
└─────────┬─────────┘    └─────────┬─────────┘    └─────────┬─────────┘
          │                        │                        │
          │                        │                        │
          └────────────────────────┼────────────────────────┘
                                   │
                                   ▼
                        ┌────────────────────┐
                        │  UNIFIED EVIDENCE  │
                        │                    │
                        │ • Access Logs      │
                        │ • CCTV Footage     │
                        │ • Env. Monitoring  │
                        │ • Utility Uptime   │
                        │ • Incident Reports │
                        │ • Test Records     │
                        └────────────────────┘
                                   │
                                   ▼
                        ┌────────────────────┐
                        │ COMPLIANCE DASHBOARD│
                        │                    │
                        │ • A.7.4 Score: 92% │
                        │ • A.7.5 Score: 88% │
                        │ • A.7.11 Score: 95%│
                        │ • Overall: 91%     │
                        └────────────────────┘
```

**Integration Points:**

1. **Monitoring → Environmental:** CCTV detects fire/flood, environmental sensors trigger physical security alarms
2. **Environmental → Utilities:** Fire suppression requires power (UPS), HVAC depends on power and monitoring
3. **Utilities → Monitoring:** Power failures disable access control and CCTV unless UPS-protected
4. **All Three → Evidence:** Unified logging, monitoring, and compliance reporting

**Dependency Chain:**
```
Power (A.7.11) → Environmental Protection (A.7.5) → Physical Monitoring (A.7.4)
```
Without reliable power, environmental protection systems (fire suppression, HVAC) fail.
Without environmental protection, facilities become uninhabitable (fire, temperature).
Without physical monitoring, unauthorized access and environmental threats go undetected.

---

## 5. Regulatory and Compliance Context

This Physical Infrastructure Security Framework implements requirements from regulations categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

### 5.1 Mandatory Compliance (Tier 1)

**ISO/IEC 27001:2022:**
- Control A.7.4 - Physical Security Monitoring (mandatory)
- Control A.7.5 - Protecting Against Physical and Environmental Threats (mandatory)
- Control A.7.11 - Supporting Utilities (mandatory)
- Evidence: Documented controls, implementation evidence, test records, incident reports
- Audit: Annual ISO 27001 surveillance or recertification audit

**Implementation Obligation:**
- All organizations with ISO 27001 certification MUST implement these controls
- Controls cannot be excluded unless genuinely not applicable (e.g., 100% cloud with no physical facilities)
- Statement of Applicability must document implementation or justify exclusion

### 5.2 Conditional Compliance (Tier 2)

The following regulations apply IF specific triggers are met:

**FINMA Circular 2023/1 (Switzerland) - Operational Risks and Resilience:**
- **Trigger:** [Organization] is a financial institution supervised by FINMA (banks, insurance, asset managers, securities dealers)
- **Relevant Margins:** Margin 50-62 (Operational Risks and Resilience)
- **Key Requirements:**
  - Margin 52: Physical security of premises and datacenters
  - Margin 53: Protection against environmental threats
  - Margin 54: Utility resilience and backup systems
  - Margin 57: Business continuity planning including physical infrastructure
- **Evidence:** Physical security documentation, environmental risk assessments, utility resilience testing records
- **Audit:** FINMA may inspect during prudential supervision

**Digital Operational Resilience Act (DORA) - Regulation (EU) 2022/2554:**
- **Trigger:** [Organization] is a financial entity operating in EU (credit institutions, investment firms, insurance, payment institutions)
- **Relevant Articles:** Article 12 (ICT and Security Risk Management), Article 11 (Business Continuity)
- **Key Requirements:**
  - Article 12(6): Physical security and environmental controls for ICT infrastructure
  - Article 11(1): ICT business continuity plans considering physical infrastructure
  - Physical security controls protecting critical ICT systems
- **Evidence:** Physical security policies, environmental protection measures, utility resilience documentation
- **Audit:** National competent authorities (NCAs) may inspect

**Network and Information Systems Directive (NIS2) - Directive (EU) 2022/2555:**
- **Trigger:** [Organization] is essential entity or important entity under NIS2 (energy, transport, banking, health, digital infrastructure, etc.)
- **Relevant Articles:** Article 21 (Cybersecurity Risk Management Measures)
- **Key Requirements:**
  - Article 21(2)(d): Physical security and environmental controls
  - Security of premises and facilities
  - Protection against unauthorized physical access
  - Environmental threat mitigation
- **Evidence:** Physical security policies, risk assessments, incident reports
- **Audit:** National CSIRT or supervisory authority may inspect

### 5.3 Informational Reference (Tier 3)

The following standards provide best practices but are NOT mandatory unless contractually required:

**Uptime Institute Tier Standards:**
- **Description:** Datacenter classification system (Tier I - IV) based on infrastructure availability and redundancy
- **Tiers:**
  - Tier I: Basic (N) - 99.671% availability, no redundancy
  - Tier II: Redundant Components (N+1) - 99.741% availability
  - Tier III: Concurrently Maintainable (N+1) - 99.982% availability
  - Tier IV: Fault Tolerant (2N or 2N+1) - 99.995% availability
- **Use:** Inform datacenter design, benchmark against industry standards, communicate capabilities to stakeholders
- **Reference:** [Uptime Institute](https://uptimeinstitute.com/)

**TIA-942 - Telecommunications Infrastructure Standard for Data Centers:**
- **Description:** ANSI/TIA standard for datacenter telecommunications infrastructure
- **Scope:** Structured cabling, pathways, spaces, redundancy, environmental controls
- **Rating System:** Rated-1 through Rated-4 (similar to Uptime Institute tiers)
- **Use:** Guide datacenter cabling infrastructure, environmental design, redundancy planning
- **Reference:** Telecommunications Industry Association (TIA)

**EN 50600 - Information Technology - Data Centre Facilities and Infrastructures:**
- **Description:** European standard series for datacenter facilities (EN 50600-1 through EN 50600-4-6)
- **Scope:** Building construction, power distribution, environmental control, telecommunications cabling, security systems
- **Availability Classes:** Class 1 (Basic) through Class 4 (Fault Tolerant)
- **Use:** European datacenter design and operation (aligns with TIA-942 and Uptime Institute)
- **Reference:** European Committee for Electrotechnical Standardization (CENELEC)

**NIST Special Publications:**
- **SP 800-53 Rev 5:** Physical and Environmental Protection (PE) controls
- **SP 800-160 Vol 1:** Systems Security Engineering (includes physical security)
- **SP 800-34 Rev 1:** Contingency Planning (includes physical disaster recovery)
- **Use:** Technical guidance, control implementation details, testing procedures
- **Reference:** [NIST Computer Security Resource Center](https://csrc.nist.gov/)

### 5.4 Regulatory Determination Process

To determine which regulations apply to [Organization]:

1. **ISO 27001:2022:** Always applies if seeking/maintaining certification → Mandatory (Tier 1)

2. **FINMA Circular 2023/1:** Does [Organization] operate as financial institution in Switzerland?
   - YES → FINMA applies → Conditional Mandatory (Tier 2)
   - NO → Informational reference only

3. **DORA:** Does [Organization] operate as financial entity in EU?
   - YES → DORA applies → Conditional Mandatory (Tier 2)
   - NO → Informational reference only

4. **NIS2:** Is [Organization] essential or important entity under NIS2?
   - YES → NIS2 applies → Conditional Mandatory (Tier 2)
   - NO → Informational reference only

5. **Uptime Institute / TIA-942 / EN 50600:** Industry best practices
   - Use as design guidance → Informational (Tier 3)
   - May become mandatory if contractually required by customers

**For complete regulatory categorization and applicability determination, refer to ISMS-POL-00 - Regulatory Applicability Framework.**

---

## 6. Roles and Responsibilities

### 6.1 Governance and Accountability

**Chief Information Security Officer (CISO):**
- Overall accountability for physical infrastructure security framework
- Approval of physical security policies and major changes
- Budget allocation for physical security investments
- Reporting to executive management and board on physical security posture
- Escalation point for significant physical security incidents

**Facilities Manager:**
- Day-to-day responsibility for physical infrastructure operations
- Environmental protection systems maintenance
- Utility resilience testing and maintenance
- Coordination with building management (if applicable)
- Vendor management (security, HVAC, generator, ISP vendors)

**Security Operations Manager:**
- Physical security monitoring implementation and operations
- Access control system management
- CCTV system operation and footage review
- Intrusion detection system management
- Security incident response coordination
- Security personnel supervision (if internal security team)

### 6.2 Implementation and Operations

**System Owners:**
- Identify physical security requirements for owned systems
- Coordinate equipment placement with facilities constraints
- Participate in physical security incident response for owned systems
- Provide input to capacity planning (power, cooling, space)

**IT Operations:**
- Integration of physical security systems with logical security (SIEM)
- Network infrastructure for physical security systems (access control, CCTV, sensors)
- Monitoring dashboard configuration and maintenance
- Incident escalation from physical to logical security

**Security Personnel (if applicable):**
- Physical patrols and monitoring
- Access control verification (badge checks, visitor escort)
- First response to physical security incidents
- Daily security log maintenance

**Facilities Technicians:**
- Physical security system maintenance (access control, CCTV, sensors)
- Environmental protection system maintenance (fire alarm, HVAC, water sensors)
- Utility system maintenance (UPS, generator, ISP equipment)
- Testing execution (monthly generator test, quarterly UPS test, etc.)

### 6.3 Oversight and Assurance

**Internal Audit:**
- Annual physical security compliance audit
- Physical access control testing (badge testing, failed access attempts)
- Environmental protection system verification (fire alarm test, water sensor test)
- Utility resilience testing verification (UPS test records, generator test records)
- Evidence review (logs, monitoring data, test records)

**Risk Management:**
- Physical security risk assessment (annual or triggered)
- Environmental threat risk assessment
- Risk register maintenance (physical security risks)
- Risk treatment planning (mitigation, transfer, acceptance)

**Compliance Officer:**
- Regulatory compliance tracking (FINMA, DORA, NIS2 if applicable)
- Evidence collection for regulatory audits
- Liaison with regulatory authorities
- Compliance reporting to executive management

### 6.4 RACI Matrix

| Activity | CISO | Facilities Mgr | Security Ops Mgr | System Owners | IT Ops | Internal Audit |
|----------|------|----------------|------------------|---------------|--------|----------------|
| Policy Approval | A | C | C | I | I | I |
| Access Control Implementation | I | R | A | C | C | I |
| CCTV System Operation | I | C | A/R | I | C | I |
| Environmental Protection | C | A/R | I | I | C | I |
| Utility Maintenance | C | A/R | I | I | C | I |
| Physical Security Incidents | A | C | R | C | C | I |
| Annual Compliance Audit | I | C | C | C | C | A/R |
| Risk Assessment | A | C | C | C | I | C |

**Legend:** A = Accountable, R = Responsible, C = Consulted, I = Informed

---

## 7. Framework Overview

### 7.1 Control Sections and Implementation Guides

This Physical Infrastructure Security Framework consists of five policy sections and four implementation guides:

**Policy Documents (POL):**
- **POL-S1 (This Document):** Executive Summary, Control Alignment, Scope - foundation and context
- **POL-S2:** Physical Security Monitoring (A.7.4) - access control, CCTV, intrusion detection, security personnel
- **POL-S3:** Environmental Protection (A.7.5) - fire, flood, temperature, structural threats
- **POL-S4:** Utility Resilience (A.7.11) - power, HVAC, telecommunications
- **POL-S5:** Assessment Methodology and Evidence Framework - compliance measurement and audit evidence

**Implementation Guides (IMP):**
- **IMP-S1:** Physical Monitoring Implementation - access control, CCTV, intrusion detection deployment
- **IMP-S2:** Environmental Protection Implementation - fire detection/suppression, water detection, temperature monitoring
- **IMP-S3:** Utility Resilience Implementation - UPS, generator, HVAC, ISP redundancy deployment
- **IMP-S4:** Facilities Assessment - ongoing compliance monitoring and testing procedures

**Assessment Tools:**
- **Assessment 1:** Access Monitoring (A.7.4) - access logs, CCTV coverage, intrusion detection
- **Assessment 2:** Environmental Protection (A.7.5) - fire detection, water detection, temperature monitoring
- **Assessment 3:** Utility Resilience (A.7.11) - power infrastructure, HVAC, telecommunications
- **Dashboard:** Physical Infrastructure Health - unified compliance dashboard

### 7.2 Implementation Sequence

**Phase 1: Assessment and Planning (Months 1-2)**
- Conduct environmental threat risk assessment (POL-S3, Section 2)
- Identify facility criticality tiers (Section 3.5)
- Perform gap analysis against requirements
- Develop implementation roadmap and budget

**Phase 2: Physical Monitoring (Months 2-4)**
- Deploy access control system (IMP-S1, Section 2)
- Install CCTV system (IMP-S1, Section 3)
- Implement intrusion detection (IMP-S1, Section 4)
- Integrate monitoring systems (IMP-S1, Section 5)

**Phase 3: Environmental Protection (Months 3-6)**
- Install/verify fire detection system (IMP-S2, Section 2)
- Deploy water detection system (IMP-S2, Section 3)
- Implement temperature/humidity monitoring (IMP-S2, Section 4)
- Develop environmental protection plan (IMP-S2, Section 5)

**Phase 4: Utility Resilience (Months 4-7)**
- Size and install UPS (IMP-S3, Section 2)
- Size and install backup generator (IMP-S3, Section 3)
- Implement HVAC redundancy (IMP-S3, Section 4)
- Configure ISP redundancy (IMP-S3, Section 5)

**Phase 5: Monitoring and Testing (Months 6-8)**
- Deploy utility monitoring system (IMP-S3, Section 6)
- Conduct end-to-end testing (IMP-S4, Section 4)
- Establish continuous monitoring (IMP-S4, Section 5)
- Complete initial compliance assessment (IMP-S4, Section 2)

**Phase 6: Continuous Improvement (Ongoing)**
- Monthly automated assessments
- Quarterly manual assessments and testing
- Annual comprehensive audit
- Continuous monitoring and alerting

### 7.3 Success Metrics

**Physical Security Monitoring (A.7.4):**
- Access control coverage: 100% of entry/exit points
- CCTV coverage: 100% of required areas (entrances, server rooms, parking)
- Failed access attempts: <5 per month (legitimate failures, not attacks)
- Incident response time: <5 minutes (critical facilities), <15 minutes (standard)
- Physical security incidents: <2 per year (excluding false alarms)

**Environmental Protection (A.7.5):**
- Fire detection coverage: 100% of facility area
- Fire suppression coverage: 100% of facility area
- Water detection coverage: 100% of at-risk areas
- Temperature excursions: <5 per month
- Environmental incidents: 0 major incidents per year (fire, flood causing damage)

**Utility Resilience (A.7.11):**
- Power uptime: 99.99% (critical facilities), 99.9% (standard)
- UPS runtime: Meets requirement (15 min critical, 5 min standard)
- Generator test compliance: 100% (monthly, quarterly, annual tests completed)
- HVAC uptime: 99.9% (critical facilities), 99% (standard)
- ISP uptime: Meets SLA (99.9% typical)

**Overall Framework:**
- Compliance score: >90% (excellent), 75-89% (good), 60-74% (acceptable), <60% (non-compliant)
- Audit findings: 0 major findings, <3 minor findings
- Testing compliance: 100% of required tests completed on schedule

---

## 8. Related Documents

**Internal ISMS References:**
- **ISMS-POL-00:** Regulatory Applicability Framework (regulatory categorization, applicability determination)
- **ISMS-POL-A.7.1-3:** Physical Access Control (entry/exit security baseline, prerequisite for A.7.4 monitoring)
- **ISMS-POL-A.8.13-14-5.30:** Business Continuity and Disaster Recovery (physical disaster scenarios, recovery procedures)
- **ISMS-POL-A.5.19-23:** Information Security for Use of Cloud Services (cloud provider physical security assessment)
- **ISMS-POL-A.8.6:** Capacity Management (physical infrastructure capacity planning)
- **ISMS-POL-A.5.24-27:** Incident Management (physical security incident handling)

**Framework Sections (This Control Stack):**
- **ISMS-POL-A.7.4-5-11-S2:** Physical Security Monitoring (A.7.4)
- **ISMS-POL-A.7.4-5-11-S3:** Environmental Protection (A.7.5)
- **ISMS-POL-A.7.4-5-11-S4:** Utility Resilience (A.7.11)
- **ISMS-POL-A.7.4-5-11-S5:** Assessment Methodology and Evidence Framework
- **ISMS-IMP-A.7.4-5-11-S1:** Physical Monitoring Implementation
- **ISMS-IMP-A.7.4-5-11-S2:** Environmental Protection Implementation
- **ISMS-IMP-A.7.4-5-11-S3:** Utility Resilience Implementation
- **ISMS-IMP-A.7.4-5-11-S4:** Facilities Assessment

**External Standards and Regulations:**
- **ISO/IEC 27001:2022:** Information Security Management Systems - Requirements (Controls A.7.4, A.7.5, A.7.11)
- **ISO/IEC 27002:2022:** Information Security Controls - Reference (Detailed guidance for A.7.4, A.7.5, A.7.11)
- **FINMA Circular 2023/1:** Operational Risks and Resilience (if applicable to Swiss financial institutions)
- **DORA (EU) 2022/2554:** Digital Operational Resilience Act (if applicable to EU financial entities)
- **NIS2 (EU) 2022/2555:** Network and Information Systems Directive (if applicable to essential/important entities)
- **Uptime Institute Tier Standards:** Datacenter classification (informational reference)
- **TIA-942:** Telecommunications Infrastructure Standard for Data Centers (informational reference)
- **EN 50600:** Data Centre Facilities and Infrastructures (informational reference)
- **NIST SP 800-53 Rev 5:** Security and Privacy Controls (Physical and Environmental Protection family)

---

**END OF ISMS-POL-A.7.4-5-11-S1**

---

**Document Approval Signatures:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Author | [Name] | | |
| Facilities Manager | [Name] | | |
| Security Operations Manager | [Name] | | |
| CISO | [Name] | | |
| Executive Management | [Name] | | |

---

*"Physical infrastructure security is not just about having badge readers, fire alarms, and backup generators. It's about systematic monitoring, comprehensive environmental protection, and resilient utility infrastructure—all working together as an integrated system to protect information assets from physical threats."*
