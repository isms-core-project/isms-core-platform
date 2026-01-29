# ISMS-POL-A.7.4-5-11 – Physical Infrastructure Security

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Physical Infrastructure Security |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.7.4-5-11 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Facilities Manager / Security Operations Manager | Initial consolidated policy for ISO 27001:2022 first certification - combines physical monitoring, environmental protection, and utility resilience |

**Review Cycle**: Annual (or upon significant facility changes, security incidents, or regulatory updates)  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Secondary: Facilities Manager
- Technical: Security Operations Manager
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.7.4-5-11 (Implementation Guidance Suite)
- ISO/IEC 27001:2022 Controls A.7.4, A.7.5, A.7.11
- ISMS-POL-A.7.1-3 (Physical Access Control)
- ISMS-POL-A.8.13-14-5.30 (Business Continuity and Disaster Recovery)
- ISMS-POL-A.5.19-23 (Cloud Services)

---

## Executive Summary

This policy establishes [Organization]'s requirements for physical infrastructure security controls to protect information assets through comprehensive monitoring, environmental protection, and utility resilience in accordance with ISO/IEC 27001:2022 Controls A.7.4, A.7.5, and A.7.11.

**Scope**: This policy applies to all facilities where [Organization] processes, stores, or transmits information assets, including on-premises datacenters, office facilities, colocation facilities, and remote locations. Cloud-only organizations operating without physical information processing facilities may mark these controls as "Not Applicable" (see Section 1.4.2).

**Purpose**: Define organizational requirements for physical infrastructure security control implementation and governance. This policy establishes WHAT physical security protection is required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.7.4-5-11.

**Combined Control Approach**: These three controls are implemented as a unified Physical Infrastructure Security Framework because they operate on the same physical infrastructure, create interdependencies (power failures affect environmental protection and monitoring systems), and share common assessment and evidence collection processes. Despite unified implementation, each control maintains distinct requirements for Statement of Applicability (SoA) purposes.

**Why Unified Framework**: Physical Security Monitoring (A.7.4) monitors WHO enters facilities and WHAT happens inside. Environmental Protection (A.7.5) protects facilities from ENVIRONMENTAL hazards (fire, flood, temperature). Utility Resilience (A.7.11) ensures UTILITIES supporting facilities remain available and resilient (power, HVAC, connectivity). Attempting to implement separately would result in disconnected monitoring, redundant risk assessments, fragmented utility management, and cascading failures (power outages disable monitoring and environmental protection systems).

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Controls A.7.4, A.7.5, A.7.11

**ISO/IEC 27001:2022 Annex A.7.4 - Physical Security Monitoring**

> *Premises shall be continuously monitored for unauthorized physical access.*

**Control Objective**: Detect and respond to unauthorized physical access to premises, facilities and information processing areas.

**ISO 27002:2022 Guidance Summary**:
- Physical access monitoring should be implemented to detect unauthorized access attempts
- Monitoring mechanisms can include security guards, video surveillance (CCTV), access control logs, and intrusion detection systems
- Monitoring should be continuous or at appropriate intervals based on risk assessment
- Access logs should be regularly reviewed to identify unauthorized or anomalous access patterns
- Visitor access should be monitored and supervised through sign-in procedures and escort requirements
- Physical security events should be recorded, analyzed, and integrated with logical security monitoring where appropriate
- Alarm systems should be implemented to alert security personnel of unauthorized access attempts
- Monitoring effectiveness should be periodically tested through security audits and penetration testing

**ISO/IEC 27001:2022 Annex A.7.5 - Protecting Against Physical and Environmental Threats**

> *Protection against physical and environmental threats, such as natural disasters, malicious attack or accidents shall be designed and implemented.*

**Control Objective**: Prevent physical and environmental damage to information processing facilities and information assets.

**ISO 27002:2022 Guidance Summary**:
- Protection should address natural disasters (floods, earthquakes, hurricanes, tornadoes), deliberate malicious acts (arson, vandalism, terrorism), and accidents (fires, water damage, equipment failure)
- Fire detection and suppression systems should be installed, tested, and maintained in accordance with local regulations
- Water damage protection should include flood risk assessment, water detection sensors, drainage systems, and equipment elevation
- Environmental monitoring should include temperature and humidity controls appropriate for information processing equipment
- Facilities should be constructed or reinforced to withstand identified environmental threats based on geographic location
- Physical access barriers (perimeter fencing, vehicle barriers, secure construction) should be implemented to protect against physical threats
- Emergency response procedures should be documented and regularly tested for various threat scenarios
- Equipment should be protected against power fluctuations, electromagnetic interference, and other environmental disruptions
- Insurance coverage should be considered to address financial impacts of physical and environmental incidents

**ISO/IEC 27001:2022 Annex A.7.11 - Supporting Utilities**

> *Information processing facilities shall be protected from power failures and other disruptions caused by failures in supporting utilities.*

**Control Objective**: Ensure the continued availability of information processing facilities in the event of utility disruptions.

**ISO 27002:2022 Guidance Summary**:
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

**Statement of Applicability Independence**: Despite unified implementation and documentation, Controls A.7.4, A.7.5, and A.7.11 are assessed independently in the Statement of Applicability. Each control maintains distinct requirements, evidence collection, and compliance scoring for audit purposes.

### 1.2 What This Policy Does

This policy:
- **Defines** physical infrastructure security control requirements aligned with organizational risk assessment
- **Establishes** governance framework for physical infrastructure security decision-making across monitoring, environmental protection, and utility resilience
- **Specifies** accountability for physical infrastructure security control implementation
- **References** applicable regulatory requirements per ISMS-POL-00
- **Integrates** three related controls into unified framework for implementation efficiency
- **Addresses** facility criticality tiers (critical datacenters vs. standard offices) with corresponding control requirements

### 1.3 What This Policy Does NOT Do

This policy does NOT:
- **Specify technical implementation details** (see ISMS-IMP-A.7.4-5-11 Implementation Guides)
- **Define specific access control hardware or CCTV models** (see ISMS-IMP-A.7.4-5-11-S1 Physical Monitoring Assessment)
- **Provide fire suppression system designs or UPS sizing calculations** (see ISMS-IMP-A.7.4-5-11-S2 Environmental Protection and S3 Utility Resilience Assessments)
- **Define facility-specific deployment procedures** (see ISMS-IMP-A.7.4-5-11 Implementation Guides)
- **Select physical security technologies or vendors** (technology selection based on [Organization]'s risk assessment)
- **Replace risk assessment** (physical security controls selected based on [Organization]'s risk treatment)
- **Replace building codes or life safety regulations** (compliance with local building codes, fire codes, and safety regulations remains mandatory)

**Rationale**: Separating policy requirements from implementation guidance enables:
- Policy stability despite evolving security technologies (access control, CCTV, environmental sensors)
- Technical agility for technology updates without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Location-agnostic approach applicable to any facility type (datacenter, office, colocation)
- Risk-based implementation adapted to facility criticality and geographic threats

### 1.4 Scope

#### 1.4.1 Physical Environment Scope

**This policy applies to**:

**On-Premises Datacenters**:
- Primary datacenter facilities
- Disaster recovery sites
- Server rooms within office buildings
- Telecommunications closets
- Equipment cages

**Office Facilities**:
- Corporate headquarters
- Regional offices
- Branch offices
- Remote offices
- Home offices (where organization-owned equipment is located)

**Colocation Facilities**:
- Leased datacenter space (cages, suites, cabinets)
- Managed hosting environments
- Shared infrastructure facilities
- Responsibility matrix applies (see Section 1.4.3)

**Remote and Temporary Facilities**:
- Pop-up offices
- Temporary workspaces
- Mobile command centers (if applicable)

**Geographic Scope**:
- All facilities globally where [Organization] operates
- Geographic-specific threat considerations apply (see Section 1.4.4)

**Personnel Scope**:
- Facilities Management, Security Operations, IT Operations
- System Owners, Security Personnel
- All employees (physical access policies)
- Contractors, vendors, visitors (when accessing facilities)

#### 1.4.2 Cloud-Only Organizations - Critical Applicability Note

**IMPORTANT: If [Organization] operates 100% in cloud environments (AWS, Azure, GCP, etc.) with NO on-premises datacenters, server rooms, or information processing facilities, these controls may be marked as "Not Applicable" in the Statement of Applicability (SoA).**

**Rationale**:
- Cloud providers are responsible for physical infrastructure security (datacenters, power, cooling, physical access)
- [Organization's] responsibility is to assess cloud provider physical security controls through supplier management (ISO 27001:2022 Control A.5.19-23: Information Security for Use of Cloud Services)
- Cloud provider physical security is verified through audit reports (SOC 2 Type II, ISO 27001 certification) rather than direct implementation

**Statement of Applicability Language (if applicable)**:
```
Control A.7.4 - Physical Security Monitoring: Not Applicable - Cloud Environment
Control A.7.5 - Protecting Against Physical and Environmental Threats: Not Applicable - Cloud Environment  
Control A.7.11 - Supporting Utilities: Not Applicable - Cloud Environment

Justification: [Organization] operates 100% in cloud infrastructure (AWS/Azure/GCP) with no on-premises datacenters, server rooms, or information processing facilities. Physical infrastructure security is the cloud provider's responsibility. [Organization] assesses cloud provider physical security controls through supplier management (Control A.5.19-23) including review of SOC 2 Type II and ISO 27001 audit reports covering physical security, environmental protection, and utility resilience.

Office physical security is addressed through Control A.7.1-3 (Physical Access Control) for office premises only.
```

**Hybrid Cloud Organizations**:
- If [Organization] operates BOTH cloud and on-premises infrastructure, these controls apply to on-premises facilities only
- Cloud portion assessed via A.5.19-23 (supplier management)
- Clear documentation of which facilities are in scope vs. out of scope

**Office Physical Security**:
- Even cloud-only organizations typically have office premises
- Office physical security (building access, visitor management, basic environmental protection) is still required
- Apply Control A.7.1-3 (Physical Access Control) for office security
- These controls (A.7.4/5/11) focus on information processing facilities, not general office security

#### 1.4.3 Colocation Facilities - Shared Responsibility Model

When [Organization] utilizes colocation datacenter space, physical infrastructure responsibilities are shared between the colocation provider and [Organization]:

**Colocation Provider Responsibilities (Typical)**:
- Perimeter physical security (fencing, vehicle barriers, building access control)
- Building-wide CCTV and intrusion detection
- Fire detection and suppression (facility-wide)
- HVAC and environmental controls (facility-wide)
- Primary power (utility), UPS, backup generators (facility-wide)
- Building structure and seismic/wind protection
- 24/7 security personnel and monitoring

**[Organization] Customer Responsibilities (Typical)**:
- Cage/suite access control (secondary access layer)
- Internal CCTV within cage/suite (optional but recommended)
- Equipment-level environmental monitoring (temperature sensors within cage)
- Equipment-level UPS (optional, for network equipment)
- Physical security of equipment (rack locks, cable locks)
- Visitor escort within cage/suite area

**Responsibility Matrix Documentation**:
- Maintain formal responsibility matrix in colocation contract
- Document which controls are provider-managed vs. customer-managed
- Verify provider controls through audit reports (SOC 2 Type II, ISO 27001, Uptime Institute Tier Certification)
- Review provider SLAs for physical security, environmental protection, and utility uptime
- Conduct periodic verification (annual review of provider audit reports)

**Evidence Collection for Colocation**:
- Provider audit reports (SOC 2 Type II, ISO 27001)
- Provider SLA reports (power uptime, HVAC uptime, physical security incidents)
- Provider datacenter tier certification (Uptime Institute)
- Customer-implemented controls evidence (cage access logs, equipment-level monitoring)
- Incident reports (provider incidents affecting customer, customer incidents)

#### 1.4.4 Geographic Applicability and Threat Diversity

This framework is **location-agnostic** and adapts to geographic-specific threats:

**Earthquake Zones (e.g., California, Japan, New Zealand)**:
- Enhanced structural protection requirements
- Equipment anchoring and seismic mounts mandatory
- Seismic-resistant building design verification
- Post-earthquake inspection procedures

**Hurricane/Typhoon Zones (e.g., Florida, Caribbean, Southeast Asia)**:
- Wind-resistant construction verification
- Generator fuel supply for extended outages (3-7 days)
- Emergency generator testing before hurricane season
- Roof and window protection measures

**Flood Zones (e.g., Netherlands, Bangladesh, coastal areas)**:
- Equipment elevation requirements (raised floors, elevated racks)
- Flood barrier systems (sandbags, temporary barriers)
- Water detection sensors mandatory
- Drainage system verification

**Extreme Temperature Zones (e.g., Arctic, desert regions)**:
- Enhanced HVAC capacity for extreme temperatures
- Equipment cold-start procedures (Arctic)
- Heat mitigation for extreme heat (desert)
- Temperature monitoring with wider alert thresholds

**Implementation Approach**:
- Perform location-specific environmental threat assessment (see Section 3.1)
- Apply threat-specific mitigation controls based on assessment
- Document geographic considerations in facilities risk register
- Review threat landscape annually or when opening new facilities

#### 1.4.5 Facility Criticality Tiers

Facilities are classified into two criticality tiers with corresponding control requirements:

**Tier 1 - Critical Facilities**:
- **Definition**: Datacenters, primary server rooms, critical infrastructure hosting
- **Characteristics**: 24/7 operations, high availability requirements, significant business impact if unavailable
- **Examples**: Production datacenters, disaster recovery sites, core network infrastructure rooms

**Control Requirements**:
- Physical monitoring: 24/7 access control, CCTV, intrusion detection, security personnel
- Environmental protection: Pre-action sprinklers or gas suppression, continuous temperature monitoring, comprehensive threat protection
- Utility resilience: UPS 15+ min runtime, backup generator 24+ hours, N+1 redundancy (power, HVAC), dual ISP with diverse paths

**Tier 2 - Standard Facilities**:
- **Definition**: Office buildings, branch offices, non-critical server rooms
- **Characteristics**: Business hours operations, standard availability requirements, moderate business impact if unavailable
- **Examples**: Corporate offices, regional offices, small server rooms supporting local operations

**Control Requirements**:
- Physical monitoring: Business hours access control with after-hours alarms, CCTV (business hours or motion-triggered), basic intrusion detection
- Environmental protection: Standard sprinklers, temperature monitoring (business hours or threshold alerts), basic threat protection
- Utility resilience: UPS 5+ min runtime, backup generator (risk-based, optional), N configuration (no redundancy), single ISP with SLA

**Tier Assignment**:
- Facilities classified based on Business Impact Analysis (BIA)
- Tier assignment reviewed annually or upon significant facility changes
- Documented in facilities risk register

#### 1.4.6 Out of Scope

**This policy does NOT apply to**:
- Physical security of portable devices and laptops (covered under A.7.7 Clear Desk and Clear Screen, A.8.1 User Endpoint Devices)
- Physical security of network cables and equipment during transport (covered under A.7.13 Equipment Maintenance)
- Physical security of backup media storage offsite (covered under A.8.13 Information Backup)
- Personnel security and background checks (covered under A.6.1-6.4 People Controls)
- Information destruction procedures (covered under A.8.10 Information Deletion)

### 1.5 Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**.

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Requirements |
|------------|---------------|------------------|
| **Swiss nDSG (Federal Data Protection Act)** | All Swiss operations | Art. 8 - Appropriate technical and organizational measures for physical security |
| **EU GDPR** | When processing EU personal data | Art. 32 - Security of processing including physical security measures |
| **ISO/IEC 27001:2022** | Certification scope | Controls A.7.4, A.7.5, A.7.11 - Documented policy and implementation evidence |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Physical Infrastructure Requirements |
|-----------|-------------------|-------------------------------------|
| **FINMA Circular 2023/1** | Swiss regulated financial institution | Margin 50-62: Physical security, environmental protection, utility resilience for operational risk management |
| **DORA (EU) 2022/2554** | EU financial services entity | Art. 12: Physical security and environmental controls for ICT infrastructure |
| **NIS2 Directive (EU) 2022/2555** | Essential/important entity (EU) | Art. 21(2)(d): Physical security, environmental controls, unauthorized access protection |

**Tier 3: Informational Guidance**

Best practice frameworks referenced but not mandatory compliance requirements:

- **Uptime Institute Tier Standards**: Datacenter classification (Tier I-IV) based on availability and redundancy
- **TIA-942**: Telecommunications Infrastructure Standard for Data Centers
- **EN 50600**: European standard for datacenter facilities and infrastructures
- **NIST SP 800-53 Rev 5**: Physical and Environmental Protection (PE) controls
- **ISO/IEC 27033**: Network Security (physical security for network infrastructure)

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment. The most stringent requirements apply where multiple regulations overlap. For complete regulatory categorization and applicability determination, refer to ISMS-POL-00 - Regulatory Applicability Framework.

---

## 2. Physical Security Monitoring Requirements (A.7.4)

### 2.1 Access Control and Monitoring

[Organization] SHALL implement access control systems that:

**System Capabilities**:
- Provide electronic access control at all facility entry/exit points
- Support badge/card reader systems with appropriate authentication technology (proximity, smart card, or biometric)
- Implement multi-factor authentication for highly sensitive areas in critical facilities
- Integrate with identity management system for automated badge provisioning and revocation
- Maintain comprehensive access logs with user identity, location, timestamp, and result

**Access Authorization**:
- Assign access rights based on role and business need (principle of least privilege)
- Define access levels: Public areas, general office, restricted areas, highly sensitive
- Implement temporary access for contractors and visitors with time limitations
- Provide emergency access override with complete audit trail
- Configure anti-passback where appropriate to prevent badge sharing

**Access Log Requirements**:
- Retention: 365 days minimum (critical facilities), 90 days minimum (standard facilities)
- Review frequency: Weekly (critical facilities high-privilege access), Monthly (standard facilities after-hours access)
- Automated anomaly detection: Failed access attempts, after-hours access, unusual patterns
- Secure storage with access controls and off-site backup

**Visitor Management**:
- All visitors SHALL sign in at reception or security desk with required information (name, company, purpose, host, duration)
- Issue temporary visitor badges clearly marked and differentiated from employee badges
- Verify visitor identity through government-issued photo ID
- Require escort for visitors accessing restricted areas
- Record visitor exit and badge return upon departure
- Monthly review of contractor badges with expiration and revocation of expired access

**Access Review and Recertification**:
- Quarterly access review: Identify stale accounts (no activity 90 days), orphaned accounts (terminated employees)
- Annual access recertification by system owners and managers
- Automated provisioning/deprovisioning integrated with HR system (immediate badge revocation upon termination)

### 2.2 Physical Intrusion Detection

[Organization] SHALL implement intrusion detection systems that:

**Sensor Types and Coverage**:
- Motion sensors (PIR) in server rooms, telecom closets, storage rooms, sensitive areas
- Door and window sensors on all perimeter entry points and ground-floor windows
- Glass break detectors for ground floor windows, large glass panels, skylights
- Perimeter intrusion detection for critical facilities (fence-mounted sensors, infrared beams, video analytics)

**Coverage Requirements**:
- Critical facilities (Tier 1): 100% of interior restricted areas, 100% of perimeter entry points, perimeter intrusion detection, no blind spots
- Standard facilities (Tier 2): All entry points, accessible windows, sensitive areas (risk-based)

**Arming and Monitoring**:
- Define independent arming zones (building perimeter, server room, office areas)
- Critical facilities: Armed 24/7 (perimeter and restricted areas)
- Standard facilities: Armed after business hours (perimeter), restricted areas armed when unoccupied
- Authentication required for arming/disarming with complete audit trail

**Testing and Maintenance**:
- Monthly walk testing: Activate each sensor, verify alarm notifications
- Quarterly end-to-end testing: Trigger alarm, verify response procedure
- Annual professional inspection by certified technician
- False alarm management: Target <5 false alarms per month, investigate root cause if exceeding

### 2.3 Video Surveillance (CCTV)

[Organization] SHALL provide CCTV coverage for:

**Mandatory Coverage Areas**:
- All building entrances and exits (exterior and interior views)
- All facility perimeter entry points (vehicle gates, pedestrian gates)
- Reception areas and visitor waiting areas
- Server rooms (interior view of racks and access door)
- Telecom closets and equipment rooms
- Parking areas (vehicular access points)
- Critical facilities additional: Building perimeter, loading docks, sensitive storage, emergency exits, roof access

**Camera Requirements**:
- Elimination of blind spots through overlapping coverage
- Appropriate camera types: Fixed cameras (continuous monitoring), PTZ cameras (operator-controlled), IP cameras (network-based)
- Resolution: Minimum 1080p (2 megapixel) for critical areas, 720p acceptable for general monitoring
- Low-light capability: IR illuminators or camera low-light sensitivity (0.1 lux or better)
- Weatherproofing: IP66 or IP67 rated for outdoor cameras

**Recording and Retention**:
- Continuous recording for critical areas (entrances, server rooms, restricted areas)
- Motion-triggered recording acceptable for low-traffic areas
- Frame rate: Minimum 10 fps for monitoring, 15-30 fps for identification purposes
- Retention period: 90 days (critical facilities), 30 days (standard facilities)
- Secure storage with access controls and backup

**System Management**:
- Network Video Recorder (NVR) or Video Management System (VMS) with adequate storage capacity
- Redundant storage (RAID, cloud backup) for critical footage
- User access controls (view-only for security personnel, full access for security manager)
- Monthly camera functionality testing and annual professional maintenance

### 2.4 Security Personnel and Operations

[Organization] SHALL (where security personnel deployed):

**Security Personnel Duties**:
- Reception duties: Greet visitors, verify ID, issue badges, log information, notify hosts, escort where required
- Patrol duties: Conduct patrols per defined schedule, document checkpoints, report observations
- Monitoring duties: Monitor CCTV live feeds, respond to alarms, document events in security log
- Incident response: Respond to physical security incidents per defined response procedures

**Daily Security Log**:
- Record: Date, shift, personnel on duty, patrol completion times, visitor log, alarm events, incidents, observations
- Retention: 12 months minimum
- Review: Security manager weekly review, CISO monthly summary

**Response Time Targets**:
- Critical facilities (Tier 1): Security personnel on-site within 5 minutes of alarm
- Standard facilities (Tier 2): Security personnel or contracted security within 15 minutes of alarm

### 2.5 Integration with Security Operations

[Organization] SHALL integrate physical security systems with security operations:

**SIEM Integration**:
- Forward physical security events to SIEM: Access denied events, forced door events, after-hours access, intrusion alarms, camera offline events
- Event correlation: Physical access + logical access (same user, verify authorized), physical intrusion + network anomaly (investigate data exfiltration)
- Alert rules: After-hours restricted area access, unusual access patterns, terminated employee access attempts

**Physical Security Dashboard**:
- Real-time metrics: Access events, failed attempts, after-hours access, active visitors, alarm events, camera status, storage capacity, open incidents
- Access: SOC (real-time monitoring), Security Operations Manager (daily), CISO (weekly), Executive Management (monthly)
- Update frequency: Real-time (30-60 second refresh)

**Incident Management Integration**:
- Classify physical security incidents per severity (Critical, High, Medium, Low)
- Manage through incident management process (ISMS-POL-A.5.24-27)
- Collect forensic evidence: Access logs, CCTV footage, alarm logs, security guard logs, physical evidence
- Maintain chain of custody and evidence retention (incident duration + 12 months, indefinite if litigation)

---

## 3. Environmental Protection Requirements (A.7.5)

### 3.1 Environmental Threat Assessment

[Organization] SHALL conduct environmental threat risk assessment that:

**Threat Categories**:
- Natural disasters: Floods, earthquakes, hurricanes/typhoons, tornadoes, extreme weather
- Fire risks: Electrical faults, equipment overheating, external fire spread, arson
- Water damage: Flooding, plumbing failures, roof leaks, sprinkler activation
- Temperature extremes: Overheating, freezing conditions
- Humidity risks: Condensation, corrosion, static electricity
- Physical intrusion: Theft, vandalism, terrorism, sabotage

**Risk Assessment Process**:
- Identify location-specific threats based on geography and facility characteristics
- Assess likelihood and impact for each threat category
- Document in facilities risk register
- Review annually or upon opening new facilities
- Implement risk-based mitigation controls per assessment results

### 3.2 Fire Detection and Suppression

[Organization] SHALL implement fire protection systems that:

**Fire Detection**:
- Smoke detectors providing early warning, installed per fire code requirements
- Heat detectors in areas where smoke detectors inappropriate (kitchens, mechanical rooms)
- Fire alarm system with audible and visual alarms, manual pull stations
- Alarm monitoring: Local alarm (critical facilities), central station monitoring (optional based on risk)
- Testing: Monthly fire alarm system test, annual inspection by certified technician

**Fire Suppression**:
- Sprinkler systems: Wet pipe sprinklers (standard), pre-action sprinklers or gas suppression (datacenters, server rooms)
- Gas suppression: FM-200, Novec 1230, or Inergen for datacenters (protects electronic equipment, minimizes water damage)
- Fire extinguishers: Appropriate type and placement per fire code, annual inspection
- Emergency evacuation plan with documented procedures, designated assembly points, annual fire drills

**Fire Response Procedures**:
- Immediate evacuation upon fire alarm activation
- Emergency services notification (automatic or manual based on system)
- Equipment shutdown procedures (if safe, where applicable)
- Post-incident inspection and restoration procedures

### 3.3 Flood and Water Damage Protection

[Organization] SHALL implement water damage protection that:

**Flood Risk Management**:
- Conduct flood risk assessment based on facility location (flood zones, below-grade areas, plumbing systems)
- Install water detection sensors in at-risk areas: Below-grade facilities, server rooms, under raised floors, near plumbing
- Implement drainage systems adequate for location and threat level
- Apply waterproofing to walls, floors, ceilings in vulnerable areas
- Elevate equipment off floor in flood-prone areas (raised floors, elevated racks minimum 6 inches)

**Water Detection and Response**:
- Water detection sensors with immediate alerting (email, SMS, alarm panel)
- Sensor placement: Server room perimeter, under raised floors, near HVAC equipment, near water supply lines
- Response procedures: Isolate water source, protect equipment, engage facilities emergency response
- Testing: Monthly sensor functionality test, annual professional inspection

### 3.4 Temperature and Humidity Control

[Organization] SHALL maintain environmental controls that:

**HVAC Monitoring**:
- Continuous temperature and humidity monitoring in server rooms and datacenters
- Temperature set points: 18-27°C (64-80°F) operating range, alerts for excursions
- Humidity set points: 40-60% RH operating range, alerts for excursions
- Temperature/humidity sensor placement: Server room intake, hot aisle, cold aisle (if applicable)

**Cooling Requirements**:
- Critical facilities (Tier 1): N+1 redundant cooling units, hot aisle/cold aisle containment recommended
- Standard facilities (Tier 2): Single cooling unit adequate, temperature monitoring with alerts
- Cooling capacity: Adequate for current and projected heat load (BTU/kW calculation per equipment density)

**Alert and Response**:
- Temperature exceeds upper threshold: Alert facilities immediately, investigate cooling failure
- Temperature exceeds critical threshold: Initiate emergency cooling procedures, consider equipment shutdown
- Humidity exceeds thresholds: Investigate HVAC malfunction, implement temporary humidity control
- Response time: <30 minutes for critical facilities, <2 hours for standard facilities

### 3.5 Structural Protection

[Organization] SHALL implement structural protection that:

**Building Integrity**:
- Verify building structural integrity appropriate for information processing equipment weight and seismic requirements
- Seismic protection (earthquake zones): Seismic-resistant building design, equipment anchoring, seismic mounts for racks
- Wind resistance (hurricane zones): Building wind rating adequate for location, roof and window protection measures
- Equipment anchoring: Secure racks to floor, secure equipment within racks

**Physical Access Barriers**:
- Perimeter fencing for critical facilities (chain-link or solid barrier minimum 2 meters height)
- Vehicle barriers: Bollards or gates at vehicle entry points to prevent unauthorized vehicle access
- Secure construction: Solid walls for server rooms, reinforced doors, limited window access
- Physical security integration: Barriers complement access control and intrusion detection

### 3.6 Environmental Protection Plan

[Organization] SHALL maintain environmental protection plan that:

**Plan Components**:
- Threat-specific response procedures (fire, flood, temperature excursion, structural damage)
- Emergency contact list (facilities personnel, emergency services, equipment vendors, insurance)
- Equipment relocation procedures (if environmental threat imminent and relocation feasible)
- Business continuity integration (link to BC/DR plan for facility unavailability scenarios)
- Insurance coverage considerations for physical and environmental incidents

**Plan Maintenance**:
- Review and update annually or upon facility changes
- Test procedures through annual exercises or actual incident response
- Document lessons learned and implement improvements

---

## 4. Utility Resilience Requirements (A.7.11)

### 4.1 Power Supply Resilience

[Organization] SHALL implement power protection that:

**Uninterruptible Power Supply (UPS)**:
- Install UPS systems to provide short-term power during utility failures
- UPS capacity requirements:
  - Critical facilities (Tier 1): Minimum 15 minutes runtime at full load
  - Standard facilities (Tier 2): Minimum 5 minutes runtime at full load
- UPS configuration: Online/double conversion UPS for critical equipment, line-interactive acceptable for less critical
- Testing: Monthly UPS self-test, quarterly load test (verify runtime), annual battery replacement based on age

**Backup Generator**:
- Critical facilities (Tier 1): Backup generator required, minimum 24 hours runtime at full load
- Standard facilities (Tier 2): Backup generator risk-based (optional but recommended)
- Generator capacity: Adequate for essential systems (HVAC, lighting, IT equipment, security systems)
- Fuel supply: On-site fuel tank with capacity for required runtime, refueling plan for extended outages
- Automatic transfer switch (ATS): Seamless transfer from utility power to generator (transfer time <10 seconds)
- Testing: Monthly no-load test (verify operation), quarterly load test (verify capacity under load)

**Power Redundancy**:
- Critical facilities (Tier 1): N+1 redundancy minimum (utility power + UPS + generator, redundant power distribution)
- Standard facilities (Tier 2): N configuration (utility power + UPS, generator optional)
- Dual power supply equipment: Servers and network equipment with dual power supplies connected to separate power sources
- Power quality monitoring: Monitor voltage, frequency, power factor, alerts for anomalies

**Power Failure Procedures**:
- Utility power loss: UPS provides immediate power, generator starts automatically within 10-30 seconds
- Generator failure: UPS runtime exhausted, initiate graceful shutdown procedures (save data, shutdown non-critical systems)
- Extended outage: Monitor fuel levels, arrange refueling, assess business continuity activation

### 4.2 HVAC and Cooling Resilience

[Organization] SHALL implement cooling protection that:

**Cooling Capacity**:
- Calculate cooling capacity requirements based on equipment heat load (watts to BTU/kW conversion)
- Critical facilities (Tier 1): N+1 redundant cooling units (minimum two units, one failure does not impact cooling)
- Standard facilities (Tier 2): Single cooling unit adequate with rapid replacement capability
- Hot aisle/cold aisle containment: Recommended for datacenters to improve cooling efficiency

**HVAC Monitoring**:
- Continuous HVAC monitoring: Temperature sensors, humidity sensors, HVAC unit status
- Alerts: HVAC unit failure, temperature excursion, filter clogging, refrigerant leak
- Dashboard: Real-time HVAC status, temperature trends, humidity trends
- Integration: HVAC alerts forwarded to facilities and security operations

**HVAC Failure Response**:
- HVAC failure detected: Alert facilities immediately, assess cooling capacity remaining
- Temperature rising: Open doors for temporary airflow (if secure), deploy portable cooling units (if available)
- Critical threshold reached: Initiate equipment shutdown to prevent heat damage
- Response time: <30 minutes investigation, <2 hours resolution or mitigation

**HVAC Maintenance**:
- Preventive maintenance: Quarterly filter replacement, annual professional servicing
- Testing: Annual cooling capacity test, verify redundant units functional

### 4.3 Telecommunications Resilience

[Organization] SHALL implement telecommunications protection that:

**ISP Redundancy**:
- Critical facilities (Tier 1): Dual ISP with diverse paths (different physical routes, different providers)
- Standard facilities (Tier 2): Single ISP with documented SLA (typical 99.9% uptime)
- ISP failover: Automatic failover to backup ISP (BGP routing or SD-WAN)
- ISP monitoring: Monitor connectivity, packet loss, latency, alerts for degradation or failure

**Network Equipment Protection**:
- UPS protection for all network equipment (routers, switches, firewalls)
- Redundant network equipment where feasible (dual routers, dual switches with failover)
- Remote management: Out-of-band management access for network equipment (console server, management network)

**Telecommunications Failure Response**:
- ISP failure detected: Verify automatic failover to backup ISP (critical facilities)
- Single ISP outage: Engage ISP support, assess impact, communicate to users, activate backup connectivity (mobile hotspot if available)
- Extended outage: Assess business continuity activation, consider alternative work locations

### 4.4 Water Supply (If Applicable)

[Organization] SHALL (where water-cooled systems used):

**Water Supply Resilience**:
- Primary water supply for cooling systems (municipal water, well water)
- Backup water supply or water storage tank (risk-based for critical facilities with water-cooled HVAC)
- Water quality monitoring (prevent scale, corrosion in cooling systems)

### 4.5 Utility Monitoring

[Organization] SHALL implement utility monitoring that:

**Real-Time Monitoring**:
- Power monitoring: Voltage, current, frequency, power quality, UPS status, generator status, fuel level
- HVAC monitoring: Temperature, humidity, HVAC unit status, airflow
- Telecommunications monitoring: ISP connectivity, bandwidth utilization, latency, packet loss
- Water supply monitoring: Water pressure, flow rate (if water-cooled systems)

**Alerting**:
- Immediate alerts for utility failures or critical thresholds
- Alert recipients: Facilities personnel, security operations, on-call engineers
- Alert methods: Email, SMS, dashboard alerts, alarm panel

**Utility Performance Dashboard**:
- Real-time utility status and metrics
- Historical trends and performance data
- Incident tracking and resolution time
- Compliance scoring and reporting

### 4.6 Utility Failure Testing

[Organization] SHALL conduct utility failure testing:

**UPS Testing**:
- Monthly: UPS self-test (automated)
- Quarterly: UPS load test (verify runtime under load)
- Battery replacement: Based on manufacturer recommendation (typical 3-5 years)

**Generator Testing**:
- Monthly: No-load test (generator starts, runs 15-30 minutes, verify operation)
- Quarterly: Load test (generator powers facility, verify capacity and automatic transfer switch)
- Annual: Full load test at nameplate capacity

**HVAC Testing**:
- Annual: Cooling capacity test (verify adequate cooling for current load)
- Annual: Redundant unit failover test (simulate primary unit failure, verify secondary unit sufficient)

**ISP Failover Testing**:
- Quarterly: Disconnect primary ISP, verify automatic failover to backup ISP (critical facilities)
- Annual: Extended failover test (operate on backup ISP for 24 hours, verify performance)

---

## 5. Governance & Compliance

### 5.1 Roles and Responsibilities

**Chief Information Security Officer (CISO)**:
- Overall accountability for physical infrastructure security framework
- Policy approval and major change authorization
- Budget allocation for physical security investments
- Executive management and board reporting on physical security posture
- Escalation point for significant physical security incidents

**Facilities Manager**:
- Day-to-day responsibility for physical infrastructure operations
- Environmental protection systems maintenance and testing
- Utility resilience testing and maintenance (UPS, generator, HVAC)
- Coordination with building management (if applicable)
- Vendor management (security, HVAC, generator, ISP vendors)

**Security Operations Manager**:
- Physical security monitoring implementation and operations
- Access control system management and access review
- CCTV system operation and footage review
- Intrusion detection system management
- Physical security incident response coordination
- Security personnel supervision (if internal security team)

**System Owners**:
- Identify physical security requirements for owned systems
- Coordinate equipment placement with facilities constraints
- Participate in physical security incident response for owned systems
- Provide input to capacity planning (power, cooling, space requirements)

**IT Operations**:
- Integration of physical security systems with logical security (SIEM integration)
- Network infrastructure for physical security systems (access control, CCTV network)
- Monitoring dashboard configuration and maintenance
- Incident escalation from physical to logical security

**Security Personnel** (if applicable):
- Physical patrols and continuous monitoring
- Access control verification (badge checks, visitor escort)
- First response to physical security incidents
- Daily security log maintenance and reporting

**Facilities Technicians**:
- Physical security system maintenance (access control, CCTV, intrusion detection)
- Environmental protection system maintenance (fire alarm, HVAC, water sensors)
- Utility system maintenance (UPS, generator, ISP equipment)
- Testing execution (monthly generator test, quarterly UPS test)

**Internal Audit**:
- Annual physical security compliance audit
- Physical access control testing (badge testing, failed access attempt verification)
- Environmental protection system verification (fire alarm test, water sensor test)
- Utility resilience testing verification (UPS test records, generator test records)
- Evidence review and compliance reporting

**Risk Management**:
- Physical security risk assessment (annual or event-triggered)
- Environmental threat risk assessment
- Risk register maintenance (physical security risks)
- Risk treatment planning (mitigation, transfer, acceptance)

**Compliance Officer**:
- Regulatory compliance tracking (FINMA, DORA, NIS2 if applicable)
- Evidence collection for regulatory audits
- Liaison with regulatory authorities
- Compliance reporting to executive management

### 5.2 Assessment and Verification

**Assessment Framework**:

[Organization] SHALL conduct regular assessments per ISMS-IMP-A.7.4-5-11 assessment methodology:

**Assessment Domains**:
- Domain 1: Physical Access Monitoring (A.7.4) - Access control systems, CCTV, intrusion detection, visitor management
- Domain 2: Environmental Protection (A.7.5) - Fire detection/suppression, water detection, temperature/humidity monitoring
- Domain 3: Utility Resilience (A.7.11) - Power infrastructure, HVAC, telecommunications, utility monitoring
- Domain 4: Compliance Dashboard - Consolidated physical infrastructure health score

**Assessment Frequency**:
- Continuous monitoring: Real-time alerts for utility failures, access violations, environmental excursions
- Monthly assessments: Automated data collection from physical security systems
- Quarterly assessments: Manual verification and testing compliance review
- Annual assessments: Comprehensive audit with external verification

**Compliance Scoring**:
- Overall compliance score calculation based on domain scores with risk-based weighting
- Thresholds: >90% (excellent), 75-89% (good), 60-74% (acceptable), <60% (non-compliant)
- Remediation plans required for scores <75% with executive approval for acceptance below thresholds

**Evidence Requirements**:
- Configuration evidence: System documentation, network diagrams, integration specifications
- Operational evidence: Access logs, CCTV footage samples, environmental monitoring data, utility performance reports
- Testing evidence: Test records (monthly, quarterly, annual), professional inspection reports
- Incident evidence: Physical security incident reports, forensic investigation records, corrective actions

### 5.3 Exception Management

**Exception Request Process**:

Physical infrastructure security requirements may be waived through formal exception process:

**Valid Exception Scenarios**:
- Technical infeasibility (technology limitations prevent requirement implementation)
- Business constraint (requirement creates unacceptable business impact)
- Cost disproportionate to risk (requirement cost exceeds risk mitigation value)
- Temporary exception (short-term variance during facility transition, renovation, or migration)

**Exception Approval Authority**:
- Low-risk exceptions (Tier 2 facilities, non-critical controls): Security Operations Manager
- Medium-risk exceptions (Tier 1 facilities, important controls): CISO
- High-risk exceptions (critical controls, extended duration): Executive Management

**Compensating Controls**:
- Exceptions SHALL include compensating controls where feasible
- Compensating controls documented with effectiveness assessment
- Compensating controls monitored for continued effectiveness

**Exception Documentation**:
- Exception request SHALL document: Requirement being waived, justification, risk assessment, compensating controls, duration
- Exception review: Re-evaluate upon expiration, facility changes, or incident occurrence
- Exception register: Maintain central register of all active exceptions with review status

### 5.4 Incident Response

**Physical Security Incident Classification**:

**Critical Incidents**:
- Unauthorized access to restricted areas (server rooms, datacenters)
- Physical breach or forced entry
- Theft of equipment or information assets
- Violence or threat of violence on premises
- Major environmental event (fire, flood, structural damage)
- Extended utility failure affecting operations

**High Incidents**:
- Repeated failed access attempts suggesting attack
- Tailgating or badge sharing
- Lost or stolen badges
- Visitor policy violation in restricted areas
- Environmental alert requiring immediate response

**Medium Incidents**:
- Door held open beyond timeout
- Frequent false alarms indicating system issue
- Visitor policy violation in non-restricted areas
- Temperature/humidity excursion within acceptable range
- Brief utility interruption with successful failover

**Low Incidents**:
- Single failed access (user error)
- Minor visitor policy violation (forgot to sign out)
- Single false alarm
- Minor temperature/humidity fluctuation

**Incident Response Procedures**:
- Immediate response: Critical/High incidents per incident management plan (ISMS-POL-A.5.24-27)
- Investigation: All incidents documented and investigated, root cause analysis for Critical/High
- Corrective action: Implement corrective and preventive actions to prevent recurrence
- Evidence preservation: Maintain chain of custody for forensic evidence (access logs, CCTV footage)

**Incident Integration**:
- Physical security incidents managed through organizational incident management process
- Physical-logical correlation: Investigate potential connection between physical and logical security incidents
- Business continuity: Critical physical incidents may trigger BC/DR activation

### 5.5 Policy Governance

**Policy Review**:
- Review frequency: Annual or upon significant trigger event
- Trigger events: Facility changes, security incidents, regulatory updates, technology changes
- Review participants: CISO, Facilities Manager, Security Operations Manager, Compliance Officer
- Review scope: Policy effectiveness, requirement appropriateness, technology updates, regulatory changes

**Policy Approval**:
- Policy changes require CISO approval (minor changes, clarifications)
- Material policy changes require Executive Management approval (scope changes, requirement relaxation, budget impact)
- Regulatory changes require Compliance Officer review before approval

**Version Control**:
- Maintain version history with change log
- Archive previous policy versions
- Communicate policy changes to all stakeholders
- Update related documents (IMP guides, assessment tools) when policy changes

**Training and Awareness**:
- Annual physical security awareness training for all employees
- Role-specific training: Security personnel, facilities technicians, system owners
- New hire training includes physical security policies and procedures
- Update training materials when policy changes

---

## 6. Implementation & References

### 6.1 Integration with ISMS

**Risk Assessment Linkage**:
- Physical infrastructure security controls selected based on facilities risk assessment
- Environmental threat assessment informs risk treatment decisions
- Utility resilience requirements aligned with availability risk appetite
- Physical security risks documented in organizational risk register

**Statement of Applicability**:
- Controls A.7.4, A.7.5, A.7.11 addressed independently in SoA despite unified implementation
- Cloud-only organizations may mark controls "Not Applicable" with documented justification
- Colocation environments document shared responsibility model in SoA
- Control exclusions require documented justification and executive approval

**Related Controls Integration**:
- A.7.1-3 (Physical Access Control): Prerequisite baseline for physical monitoring
- A.8.13-14-5.30 (BC/DR): Physical disaster scenarios feed BC/DR planning
- A.5.19-23 (Cloud Services): Cloud provider physical security assessment via supplier management
- A.8.6 (Capacity Management): Physical infrastructure capacity planning coordinates with IT capacity
- A.5.24-27 (Incident Management): Physical security incidents managed through incident process

### 6.2 Implementation Resources

**Policy Framework (This Document)**:
- ISMS-POL-A.7.4-5-11: Physical Infrastructure Security (this consolidated policy)

**Implementation Guidance Suite**:
- ISMS-IMP-A.7.4-5-11-S1: Physical Monitoring Assessment (access control, CCTV, intrusion detection assessment methodology)
- ISMS-IMP-A.7.4-5-11-S2: Environmental Protection Assessment (fire, water, temperature protection assessment methodology)
- ISMS-IMP-A.7.4-5-11-S3: Utility Resilience Assessment (power, HVAC, telecommunications assessment methodology)
- ISMS-IMP-A.7.4-5-11-S4: Facilities Compliance Dashboard (consolidated physical infrastructure health assessment)

**Assessment Tools**:
- Excel Assessment Workbook 1: Physical Access Monitoring (A.7.4)
- Excel Assessment Workbook 2: Environmental Protection (A.7.5)
- Excel Assessment Workbook 3: Utility Resilience (A.7.11)
- Excel Dashboard Workbook: Physical Infrastructure Health (consolidated)
- Python generation scripts for automated assessment workbook creation

**Supporting Documentation**:
- Facilities risk register
- Environmental threat assessment reports
- Physical security system configuration documentation
- Testing and maintenance schedules
- Incident response procedures
- Vendor contracts and SLAs

### 6.3 Regulatory Mapping

**ISO/IEC 27001:2022 Annex A Requirements**:

| Control | Policy Section | IMP Assessment | Evidence Type |
|---------|----------------|----------------|---------------|
| A.7.4 Physical Security Monitoring | Section 2 | IMP-S1, Workbook 1 | Access logs, CCTV footage, test records |
| A.7.5 Environmental Protection | Section 3 | IMP-S2, Workbook 2 | Fire system tests, environmental monitoring data |
| A.7.11 Supporting Utilities | Section 4 | IMP-S3, Workbook 3 | UPS tests, generator tests, utility uptime reports |

**Conditional Regulatory Requirements**:

**FINMA Circular 2023/1** (if applicable):
- Margin 52 (Physical Security): Addressed in Section 2 (Physical Security Monitoring)
- Margin 53 (Environmental Protection): Addressed in Section 3 (Environmental Protection)
- Margin 54 (Utility Resilience): Addressed in Section 4 (Utility Resilience)
- Margin 57 (Business Continuity): Physical infrastructure integration with BC/DR planning
- Evidence: Physical security documentation, environmental risk assessments, utility resilience testing records

**DORA (EU) 2022/2554** (if applicable):
- Article 12(6) (ICT Security): Physical security and environmental controls for ICT infrastructure
- Article 11(1) (Business Continuity): ICT business continuity considering physical infrastructure
- Evidence: Physical security policies, environmental protection measures, utility resilience documentation

**NIS2 Directive (EU) 2022/2555** (if applicable):
- Article 21(2)(d) (Cybersecurity Risk Management): Physical security and environmental controls
- Evidence: Physical security policies, risk assessments, incident reports

**Informational Framework References**:
- Uptime Institute Tier Standards: Referenced for datacenter design and redundancy levels (Tier I-IV classification)
- TIA-942: Referenced for telecommunications infrastructure design (Rated-1 through Rated-4)
- EN 50600: Referenced for European datacenter facility standards (Class 1-4)
- NIST SP 800-53 Rev 5: Referenced for technical control implementation guidance (PE family)

---

## Related Documents

**Internal ISMS References**:
- ISMS-POL-00: Regulatory Applicability Framework
- ISMS-POL-A.7.1-3: Physical Access Control
- ISMS-POL-A.8.13-14-5.30: Business Continuity and Disaster Recovery
- ISMS-POL-A.5.19-23: Information Security for Use of Cloud Services
- ISMS-POL-A.8.6: Capacity Management
- ISMS-POL-A.5.24-27: Incident Management

**Implementation Guidance**:
- ISMS-IMP-A.7.4-5-11-S1: Physical Monitoring Assessment
- ISMS-IMP-A.7.4-5-11-S2: Environmental Protection Assessment
- ISMS-IMP-A.7.4-5-11-S3: Utility Resilience Assessment
- ISMS-IMP-A.7.4-5-11-S4: Facilities Compliance Dashboard

**External Standards**:
- ISO/IEC 27001:2022: Information Security Management Systems - Requirements
- ISO/IEC 27002:2022: Information Security Controls - Reference
- FINMA Circular 2023/1: Operational Risks and Resilience (if applicable)
- DORA (EU) 2022/2554: Digital Operational Resilience Act (if applicable)
- NIS2 (EU) 2022/2555: Network and Information Systems Directive (if applicable)
- Uptime Institute Tier Standards: Datacenter Infrastructure Tier Classification
- TIA-942: Telecommunications Infrastructure Standard for Data Centers
- EN 50600: Information Technology - Data Centre Facilities and Infrastructures
- NIST SP 800-53 Rev 5: Security and Privacy Controls

---

**Document Approval Signatures**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Author | [Name] | | |
| Facilities Manager | [Name] | | |
| Security Operations Manager | [Name] | | |
| CISO | [Name] | | |
| Executive Management | [Name] | | |

---

**END OF ISMS-POL-A.7.4-5-11 - Physical Infrastructure Security**

---

*Physical infrastructure security is not just about having badge readers, fire alarms, and backup generators. It's about systematic monitoring, comprehensive environmental protection, and resilient utility infrastructure—all working together as an integrated system to protect information assets from physical threats.*