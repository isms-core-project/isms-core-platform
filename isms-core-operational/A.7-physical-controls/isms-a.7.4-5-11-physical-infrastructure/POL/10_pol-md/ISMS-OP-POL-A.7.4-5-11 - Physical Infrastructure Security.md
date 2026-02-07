**ISMS-OP-POL-A.7.4-5-11 — Physical Infrastructure Security**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Physical Infrastructure Security |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.7.4-5-11 |
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
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Controls A.7.4, A.7.5, A.7.11 — Physical security monitoring, protecting against physical and environmental threats, supporting utilities
- ISO/IEC 27002:2022 Sections 7.4, 7.5, 7.11 — Implementation guidance

**Related Annex A Controls**:

| Control | Relationship to Physical Infrastructure Security |
|---------|--------------------------------------------------|
| A.7.1 Physical security perimeters | Perimeter boundaries define monitoring scope and environmental protection zones |
| A.7.2 Physical entry | Entry controls generate access events for monitoring and correlation |
| A.7.3 Securing offices, rooms, and facilities | Secure areas require environmental protection and utility resilience |
| A.7.8 Equipment siting and protection | Equipment placement considers environmental conditions and utility availability |
| A.7.12 Cabling security | Power and telecommunications cabling integrity supports utility resilience |
| A.7.13 Equipment maintenance | Maintenance schedules for environmental and utility systems |
| A.5.24–28 Incident management lifecycle | Physical security and environmental incidents escalate to incident management |
| A.5.30 ICT readiness for business continuity | Utility resilience supports business continuity objectives |
| A.8.16 Monitoring activities | Physical security events integrate with SIEM for correlated detection |

**Related Internal Policies**:

- Physical Access Control Policy
- Incident Management Policy
- Business Continuity and Disaster Recovery Policy
- Logging and Monitoring Policy
- Cloud Services and Supplier Security Policy
- Asset Management Policy

---

# Physical Infrastructure Security Policy

## Purpose

The purpose of this policy is to protect information processing facilities and associated infrastructure through physical security monitoring, environmental threat protection, and utility resilience. It establishes requirements for continuous surveillance, fire and water protection, climate control, and power and telecommunications continuity.

This policy addresses three related ISO 27001:2022 controls as a unified framework because they operate on the same physical infrastructure, create interdependencies, and share common assessment processes: monitoring detects threats (A.7.4), environmental controls prevent damage (A.7.5), and utility systems maintain operations (A.7.11). Each control maintains distinct requirements for Statement of Applicability purposes.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect the availability, integrity, and confidentiality of personal data through physical infrastructure security controls. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 requirements for security of processing including physical measures also apply.

## Scope

All employees and third-party users.

All organisation-owned, leased, or colocation premises, including:

- On-premises datacentres and disaster recovery sites
- Server rooms and telecommunications closets
- Corporate offices (headquarters, regional, branch)
- Colocation facilities (with shared responsibility model)
- Remote and temporary facilities where organisation-owned equipment is located

**Out of scope**:

- Physical security of portable devices (covered under A.7.9, A.8.1)
- Equipment transport security (covered under A.7.13)
- Offsite backup media storage (covered under A.8.13)
- Personnel security and background checks (covered under A.6.1–6.4)
- Third-party and supplier facility security (covered under A.5.19–23, except colocation as noted below)

### Cloud-Only Organisations

Organisations operating 100% in cloud environments with no on-premises information processing facilities may mark Controls A.7.4, A.7.5, and A.7.11 as "Not Applicable" in the Statement of Applicability.

The "Not Applicable" determination shall be documented with:

- Asset inventory reference confirming no on-premises information processing facilities.
- Cloud provider physical security verification through SOC 2 Type II report or ISO 27001 certification review.
- Annual review confirmation that cloud-only status remains accurate.

Cloud provider physical security shall be assessed through the supplier management process (A.5.19–23).

### Colocation Facilities

When utilising colocation datacentre space, physical infrastructure responsibilities are shared between the colocation provider and the organisation. The organisation shall:

- Maintain a formal responsibility matrix in the colocation contract documenting which party is responsible for each physical infrastructure control (monitoring, environmental, utility).
- Verify provider controls annually through SOC 2 Type II audit reports or ISO 27001 certification.
- Retain responsibility for monitoring and environmental controls within the organisation's allocated space (e.g., rack-level environmental monitoring, cage access controls).

## Principle

Physical and environmental security is built on the principle of protecting information processing facilities against unauthorised access, environmental threats, and utility failures — proportionate to the criticality of the assets they contain. Controls shall be selected based on documented risk assessment and the facility criticality tier classification defined in this policy.

---

## Physical Security Monitoring (A.7.4)

> *Premises should be continuously monitored for unauthorised physical access.*

Physical security monitoring shall detect and deter unauthorised physical access to facilities and restricted areas. Monitoring system design and implementation shall be proportionate to facility criticality.

### Physical Security Systems

The following physical security systems shall be implemented and maintained. Organisations shall specify the actual systems deployed (or document selection status) for each category:

| System Category | Purpose | Example Solutions | Status |
|----------------|---------|-------------------|--------|
| **Access control system** | Badge-based entry/exit with event logging | Verkada, Genetec, Honeywell, Lenel, ASSA ABLOY, Salto | [Specify or "Selection in progress"] |
| **CCTV / video surveillance** | Visual monitoring and recording | Verkada, Axis, Milestone, Genetec | [Specify or "Selection in progress"] |
| **Intrusion detection** | Perimeter and interior breach detection | Honeywell, Bosch, DSC, Texecom | [Specify or "Selection in progress"] |
| **Alarm monitoring service** | 24/7 alarm response and dispatch | Securitas, Protectas, local monitoring centre | [Specify or "Selection in progress"] |
| **Environmental monitoring** | Temperature, humidity, water detection sensors | Paessler PRTG, Raritan, APC NetBotz, Sensaphone | [Specify or "Selection in progress"] |
| **Building management system (BMS)** | Centralised building services control (HVAC, lighting, power) | Siemens Desigo, Honeywell Niagara, Schneider EcoStruxure | [Specify or "Selection in progress"] |
| **Fire detection and suppression** | Smoke/heat detection and clean agent suppression | Siemens, Minimax, Kidde, Wagner | [Specify or "Selection in progress"] |
| **UPS systems** | Uninterruptible power for critical equipment | Eaton, APC/Schneider, Vertiv/Liebert, Riello | [Specify or "Selection in progress"] |
| **Backup generator** | Extended power continuity | Caterpillar, Cummins, MTU, SDMO | [Specify or "Selection in progress"] |

**Integration requirements**: Where technically feasible, physical security systems should feed events to [SIEM] for correlation with logical security events. At minimum, access control events and intrusion detection alarms shall be forwarded.

### Electronic Access Control

- Electronic access control shall be implemented at all facility entry and exit points with authentication, event logging, and integration with identity management.
- Access events (granted, denied, forced door, door held open) shall be logged with timestamp, individual identity, and door identifier.
- Access logs shall be retained for a minimum of 12 months.
- Access rights shall be reviewed semi-annually and revoked when no longer required (e.g., role change, termination).
- Same-day access revocation shall be enforced upon employment termination.

#### Access Rights Review Process

Physical access rights shall be reviewed semi-annually using the following structured workflow:

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| 1 | Generate access rights report from [Access Control System] listing all personnel by zone and department | Facilities Manager | 1st business day of review month |
| 2 | Distribute zone-specific access lists to authorising managers for attestation | Facilities Manager | Within 2 business days |
| 3 | Managers review each person's access: confirm required, flag for removal, or escalate queries | Line Managers | Within 10 business days |
| 4 | Compile manager responses; generate revocation list for access no longer required | Facilities Manager | Within 2 business days of attestation deadline |
| 5 | Execute access revocations in [Access Control System] | Facilities Manager | Within 5 business days |
| 6 | Confirm revocations completed; file attestation records | Facilities Manager | Within 2 business days |

**Escalation for non-response**:
- Manager non-response at 10 business days → Reminder sent with 5-day extension
- Manager non-response at 15 business days → Escalation to department head
- Manager non-response at 20 business days → Access for non-attested personnel in Restricted zones suspended pending attestation

**Completion metrics**:
- Target: 100% of access rights reviewed per cycle
- Target: All revocations executed within 5 business days of attestation
- Non-compliance reported to CISO in quarterly compliance report

### Video Surveillance (CCTV)

- CCTV coverage shall be provided at facility entrances, restricted area access points, and critical infrastructure locations (server rooms, utility rooms).
- CCTV systems shall record continuously during operational hours at minimum; 24/7 recording is required for Tier 1 facilities.
- Recording retention: minimum 30 days for general areas, 90 days for restricted areas. Longer retention may be required for incident investigation.
- CCTV systems shall comply with applicable data protection requirements (Swiss nFADP, cantonal regulations). Signage indicating video surveillance shall be displayed at monitored areas.
- Camera health (connectivity, image quality, storage capacity) shall be verified weekly.

### Intrusion Detection

- Intrusion detection systems (IDS) shall be installed at Tier 1 facilities, covering perimeter doors, windows, and access points to restricted areas.
- Intrusion detection is recommended for Tier 2 facilities based on risk assessment.
- Alarms shall be connected to a monitored response point (security operations, alarm monitoring service, or [Alarm Monitoring Provider]).
- IDS shall be tested quarterly to confirm correct operation.

### Visitor Management

- All visitors shall register upon arrival, receive temporary identification, and be escorted in restricted areas.
- Visitor records (name, organisation, host, arrival/departure time) shall be retained for a minimum of 12 months.
- Visitor badges shall clearly identify visitor status, deny access to restricted areas, and expire at the end of the business day on which issued.

### Security Event Monitoring and Integration

- Physical security events (access denied, forced entry, intrusion alarm, door held open) should be forwarded to [SIEM] for correlation with logical security events where technically feasible.
- Repeated failed access attempts (3 or more within 30 minutes) shall trigger alert and investigation.

### Monitoring System Protection

- The design and configuration of monitoring systems shall be kept confidential.
- Monitoring systems shall be protected against tampering, unauthorised disabling, and remote interference.
- Monitoring equipment shall be on UPS-backed power to ensure continued operation during power interruptions.

---

## Environmental Protection (A.7.5)

> *Protection against physical and environmental threats should be designed and implemented.*

Environmental protection controls shall prevent or mitigate damage from fire, water, climate extremes, and other physical threats. Protection levels shall be proportionate to facility criticality.

### Environmental Threat Assessment

- An environmental threat risk assessment shall be conducted for each facility, considering geographic location, building characteristics, historical events, and surrounding hazards.
- The assessment shall be reviewed annually and updated following incidents or significant facility changes.
- Threats to consider include: fire, flood, water ingress, temperature extremes, humidity, lightning, seismic activity, structural failure, civil unrest, and industrial hazards.

### Fire Detection and Suppression

Fire detection shall be implemented in all facilities containing information processing equipment.

| Requirement | Tier 1 — Critical Facilities | Tier 2 — Standard Facilities |
|-------------|-------------------------------|------------------------------|
| **Detection** | Smoke detection (VESDA/aspirating or conventional) in all zones; heat detection in utility areas | Conventional smoke detection in server/equipment areas |
| **Suppression** | Clean agent fire suppression (inert gas, e.g., IG-541/Inergen, IG-55/Argonite, or equivalent) in server rooms and datacentre floors | Suppression required where equipment value exceeds CHF 500,000 or where data criticality warrants; portable extinguishers elsewhere |
| **Alarm integration** | Connected to building management system (BMS), fire brigade, and security monitoring | Connected to building fire alarm panel |
| **Inspection** | Semi-annual inspection and annual full test per cantonal fire regulations | Annual inspection per cantonal fire regulations |

**Notes on suppression agents**: Clean agent systems compliant with NFPA 2001 and ISO 14520 are required for occupied spaces containing electronic equipment. Water-based sprinkler systems shall not be used in server rooms or datacentres. Organisations should consider the long-term availability and environmental profile of selected agents when specifying suppression systems.

#### Fire Suppression Agent Selection Guidance

Organisations selecting clean agent fire suppression systems for server rooms and datacentres should evaluate options based on effectiveness, safety, environmental profile, and long-term regulatory availability:

| Agent | Type | Ozone Depletion | Global Warming Potential | Safety (Occupied Spaces) | Availability Outlook | Recommendation |
|-------|------|-----------------|-------------------------|--------------------------|---------------------|----------------|
| **IG-541 (Inergen)** | Inert gas blend (N₂, Ar, CO₂) | Zero | Zero | Safe — breathable at design concentration | Long-term stable | **Recommended** for new installations |
| **IG-55 (Argonite)** | Inert gas blend (N₂, Ar) | Zero | Zero | Safe — breathable at design concentration | Long-term stable | Recommended alternative |
| **IG-100 (Nitrogen)** | Pure nitrogen | Zero | Zero | Safe — breathable at design concentration | Long-term stable | Suitable for large volumes |
| **FK-5-1-12 (Novec 1230)** | Fluoroketone | Zero | 1 | Safe — low toxicity | Stable (3M production continues) | Acceptable for space-constrained installations |
| **HFC-227ea (FM-200)** | Hydrofluorocarbon | Zero | 3,220 | Safe — low toxicity at design concentration | **Phase-down** under EU F-gas Regulation and Kigali Amendment | **Not recommended** for new installations |

**Selection criteria for new installations**:
1. Inert gas systems (IG-541, IG-55) preferred due to zero environmental impact and long-term regulatory certainty
2. FK-5-1-12 (Novec 1230) acceptable where cylinder storage space is limited (lower volume requirement than inert gases)
3. HFC-227ea (FM-200) not recommended for new installations due to regulatory phase-down trajectory

**Existing FM-200 systems**: No immediate replacement required. Maintain per manufacturer schedule. Plan budget for replacement with inert gas system at next major refurbishment or within 10 years (whichever comes first). Document replacement timeline in facilities capital plan.

- Fire doors on security perimeters shall be alarmed, monitored, and tested in accordance with applicable fire codes.
- Emergency lighting and evacuation routes shall be maintained and tested semi-annually.

### Water Detection and Protection

- Water detection sensors shall be installed in Tier 1 facilities — below raised floors, above suspended ceilings, near cooling infrastructure, and in all zones where water ingress is possible.
- Tier 2 facilities shall have water detection in high-risk areas (near plumbing, HVAC systems, ground-level rooms).
- Water alarms shall trigger immediate alert to facilities management.
- Facilities shall implement drainage, waterproofing, and physical barriers appropriate to identified flood risk.

### Climate Control

Information processing equipment shall be maintained within controlled temperature and humidity ranges to prevent damage and ensure reliable operation.

| Parameter | Recommended Range (ASHRAE A1–A4 Class) | Alert Threshold | Critical Threshold |
|-----------|----------------------------------------|-----------------|--------------------|
| **Temperature** | 18–27 °C (64–81 °F) | Outside 18–27 °C | Below 15 °C or above 32 °C |
| **Humidity** | 20–80% relative humidity (RH) | Outside 20–80% RH | Below 10% RH or above 90% RH |
| **Temperature rate of change** | < 5 °C per hour | Exceeds 5 °C/hr | Exceeds 10 °C/hr |

**Tier 1 facilities**: Temperature shall be maintained within 18–27 °C with tolerance of +/- 2 °C. Continuous environmental monitoring with real-time alerting is required.

**Tier 2 facilities**: Temperature shall be maintained within 18–27 °C with tolerance of +/- 5 °C. Environmental monitoring with alerting during staffed hours is required.

Environmental monitoring data (temperature, humidity) shall be logged and retained for a minimum of 12 months.

#### Environmental Monitoring Alert Configuration

Environmental monitoring systems shall be configured with the following alert thresholds, response requirements, and escalation paths:

| Parameter | Warning Alert | Critical Alert | Response Time (Tier 1) | Response Time (Tier 2) |
|-----------|--------------|----------------|----------------------|----------------------|
| **Temperature** | Outside 18–27°C | Below 15°C or above 32°C | 15 minutes | Next business day |
| **Humidity** | Outside 20–80% RH | Below 10% or above 90% RH | 15 minutes | Next business day |
| **Temperature rate of change** | Exceeds 5°C/hour | Exceeds 10°C/hour | 15 minutes | 1 hour |
| **Water detection** | Any sensor activation | Multiple sensors or rising water | Immediate | 30 minutes |
| **Power (UPS on battery)** | UPS transfers to battery | Battery below 50% capacity | Immediate | 15 minutes |
| **Cooling system** | Single unit failure (redundant unit active) | All cooling units failed | 30 minutes | 1 hour |

**Alert routing**:
- Warning alerts → Facilities Manager + IT Operations (email + dashboard)
- Critical alerts → Facilities Manager + IT Operations + CISO (email + SMS + dashboard)
- After-hours critical alerts → On-call Facilities contact + IT Operations on-call

**Escalation**:
- Warning alert unacknowledged after 30 minutes → Escalate to critical
- Critical alert unacknowledged after 15 minutes → Escalate to CISO + executive management

**Alert testing**: Environmental monitoring alert paths shall be tested quarterly (simulate threshold excursion; verify alert delivery to all configured recipients within target timeframes).

### Structural and Physical Protection

- Building exterior (roof, walls, flooring) shall be of solid construction appropriate to identified threats.
- Lightning protection shall be applied to buildings housing information processing facilities. Surge protection shall be fitted to incoming power and telecommunications lines.
- Equipment siting shall minimise risk from identified environmental threats (e.g., avoid basement locations in flood-prone areas, avoid locations adjacent to hazardous processes).
- Guidelines for eating, drinking, and smoking in proximity to information processing facilities shall be established and communicated.

### Emergency Response

Emergency response procedures shall be documented for environmental incidents and tested regularly. Emergency contact information shall be posted at facility entrances and within server rooms.

#### Fire Emergency Response

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| 1 | Fire alarm activates (automatic detection or manual pull station) | Automatic / any personnel | Immediate |
| 2 | Evacuate affected zone; assembly at designated muster point | All personnel | Within 3 minutes |
| 3 | Fire brigade notified (automatic via BMS or manual call) | Facilities Manager / Reception | Within 2 minutes |
| 4 | Confirm all personnel evacuated (headcount at muster point) | Floor wardens | Within 5 minutes |
| 5 | If clean agent suppression activated: Do NOT re-enter until gas concentration verified safe | Facilities Manager | Post-suppression |
| 6 | Fire brigade clears premises; damage assessment initiated | Facilities Manager + CISO | Post all-clear |

**Post-fire actions**: Equipment damage assessment within 24 hours; data integrity verification for affected systems; incident report filed within 48 hours; insurance notification if applicable.

#### Water Ingress / Flood Emergency Response

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| 1 | Water alarm triggers or water detected visually | Automatic / any personnel | Immediate |
| 2 | Identify water source (plumbing, external ingress, HVAC condensation) | Facilities Manager | Within 15 minutes |
| 3 | If source controllable: Isolate (shut off valve, redirect flow) | Facilities Manager | Immediate |
| 4 | Move equipment and media above water level or to dry area | IT Operations + Facilities | Immediate |
| 5 | Disconnect power to at-risk equipment (if safe to do so) | IT Operations | As required |
| 6 | Deploy water extraction (pumps, wet vacuums); engage emergency restoration contractor if extensive | Facilities Manager | Within 1 hour |

#### Cooling Failure Emergency Response

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| 1 | Temperature alert received (warning threshold exceeded) | Automatic alert to IT Ops | Immediate |
| 2 | Verify cooling system status; attempt restart or failover to redundant unit | Facilities Manager | Within 15 minutes |
| 3 | If temperature approaching critical threshold (32°C): Begin orderly shutdown of non-essential systems to reduce heat load | IT Operations | Within 30 minutes |
| 4 | Deploy temporary cooling (portable AC units) if available | Facilities Manager | Within 1 hour |
| 5 | If temperature exceeds critical threshold: Orderly shutdown of all systems; notify stakeholders | IT Operations + CISO | As required |
| 6 | HVAC contractor engaged for emergency repair | Facilities Manager | Within 2 hours |

#### Total Power Failure Emergency Response

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| 1 | Mains power failure detected; UPS activates automatically | Automatic | Immediate |
| 2 | Verify generator start (Tier 1) or confirm UPS sustaining load | Facilities Manager | Within 2 minutes |
| 3 | If generator fails to start: Begin orderly shutdown of non-essential systems | IT Operations | Within 10 minutes |
| 4 | Notify utility provider; request estimated restoration time | Facilities Manager | Within 15 minutes |
| 5 | If UPS runtime approaching limit and generator unavailable: Complete orderly shutdown of all systems | IT Operations | Before UPS depletion |
| 6 | Post-restoration: Verify all systems restarted correctly; check for data integrity | IT Operations | Post-power restoration |

Emergency procedures shall be tested at least annually through drills or tabletop exercises.

### Physical Security Awareness Training

All personnel with facility access shall complete physical security awareness training. Training is delivered annually with new-hire completion required within 10 business days of facility access being granted.

#### Training Curriculum

| Module | Content | Duration | Audience |
|--------|---------|----------|----------|
| **Module 1: Facility Security Fundamentals** | Facility criticality tiers; security zone model; badge usage and responsibilities; visitor management obligations; tailgating prevention | 10 minutes | All personnel |
| **Module 2: Environmental Awareness** | Fire safety and evacuation routes; water detection awareness; climate control importance; reporting environmental anomalies; emergency contact numbers | 10 minutes | All personnel |
| **Module 3: Incident Recognition and Reporting** | Recognising physical security events (unauthorised persons, propped doors, environmental anomalies); reporting channels and expectations; evidence preservation (do not touch/move) | 5 minutes | All personnel |
| **Module 4: Role-Specific Responsibilities** | Visitor escort procedures; server room access protocols; emergency warden duties; utility system awareness | 5 minutes | Personnel with Tier 1 facility access or escort responsibilities |

**Total duration**: 30 minutes (all modules).

**Assessment**: Short quiz (5 questions, 80% pass rate required). Failed assessment: retake within 5 business days.

**Tier 1 facility orientation** (additional, in-person):
- Physical walkthrough of emergency exits, fire extinguisher locations, and muster points
- Demonstration of badge reader and access procedures
- Introduction to environmental monitoring displays (where applicable)
- Duration: 15 minutes, conducted by Facilities Manager or delegate

**Training completion target**: 95% of facility-access personnel annually. Completion tracked via [LMS or training register]. Non-completion escalated to line manager at 30 days overdue; facility access suspended at 60 days overdue.

---

## Supporting Utilities (A.7.11)

> *Information processing facilities should be protected from power failures and other disruptions caused by failures in supporting utilities.*

Utility systems shall be implemented with capacity and redundancy proportionate to facility criticality, and tested regularly to ensure reliability.

### Power Protection — Uninterruptible Power Supply (UPS)

| Requirement | Tier 1 — Critical Facilities | Tier 2 — Standard Facilities |
|-------------|-------------------------------|------------------------------|
| **Configuration** | N+1 redundancy (dual UPS units) | Single UPS |
| **Runtime** | Minimum 30 minutes per unit (sufficient for generator start and stabilisation, or orderly shutdown) | Minimum 15 minutes (sufficient for orderly shutdown) |
| **Monitoring** | Real-time monitoring with automated alerting on battery status, load, and transfer events | Monitored during staffed hours |
| **Maintenance** | Battery replacement per manufacturer schedule; annual capacity test | Battery replacement per manufacturer schedule |

- UPS systems shall protect all critical information processing equipment, network infrastructure, and security systems (access control, CCTV, fire detection).
- UPS systems shall be configured to support orderly shutdown of equipment that supports critical business operations if extended outage exceeds UPS runtime.

#### UPS Sizing Methodology

UPS capacity shall be calculated using the following four-step process to ensure adequate runtime for protected equipment:

**Step 1 — Load calculation**:
- Inventory all equipment to be protected (servers, network switches, storage, security systems)
- Sum total power draw in watts (W) or volt-amperes (VA) from equipment nameplates or measured power consumption
- Apply power factor correction if using VA ratings (typical IT load power factor: 0.9)

**Step 2 — Growth factor**:
- Apply 20–30% growth margin above current load to accommodate planned equipment additions
- Tier 1 facilities: 30% growth margin (3-year planning horizon)
- Tier 2 facilities: 20% growth margin

**Step 3 — UPS capacity selection**:
- Select UPS unit(s) with rated capacity exceeding Step 2 total
- Tier 1: N+1 redundancy (two UPS units, each capable of supporting full load independently)
- Tier 2: Single UPS with capacity exceeding Step 2 total
- Verify battery runtime at calculated load meets minimum requirements (30 minutes Tier 1, 15 minutes Tier 2)

**Step 4 — Runtime verification**:
- After installation, perform full-load discharge test to verify actual runtime
- Document actual runtime vs. calculated runtime
- If actual runtime < minimum requirement: Add battery modules or reduce protected load
- Re-verify annually during capacity test (battery degradation reduces runtime over time)

**UPS sizing record**: Documented in facilities asset register with load calculation, selected UPS model, rated capacity, measured load, calculated runtime, and actual tested runtime.

### Backup Power Generation

| Requirement | Tier 1 — Critical Facilities | Tier 2 — Standard Facilities |
|-------------|-------------------------------|------------------------------|
| **Generator** | Backup generator required | Not required (risk-based decision) |
| **Fuel capacity** | Minimum 48 hours at full load | N/A unless generator installed |
| **Start time** | Automatic start within 30 seconds of mains failure; automatic transfer switch (ATS) | Manual or automatic as appropriate |
| **Fuel management** | Fuel quality tested annually; refuelling contracts in place | Per manufacturer requirements |

- Where generators are installed, they shall be inspected weekly and load-tested according to the testing schedule below.

#### Generator Fuel Selection and Management

The fuel type shall be selected based on facility requirements, local infrastructure, and environmental considerations:

| Fuel Type | Advantages | Disadvantages | Recommended Use |
|-----------|-----------|---------------|-----------------|
| **Diesel** | High energy density; long storage life (12–18 months with treatment); widely available; reliable cold start | Requires on-site fuel storage; fuel quality degrades over time; environmental regulations for tank storage | Tier 1 facilities requiring extended autonomous runtime (48+ hours) |
| **Natural gas** | No on-site fuel storage; unlimited runtime (utility supply); lower emissions; reduced maintenance | Dependent on utility gas supply (may fail during regional disaster); lower energy density; requires gas-rated genset | Tier 1 facilities with reliable gas infrastructure and separate utility path from electrical supply |
| **Propane (LPG)** | Long shelf life (indefinite); clean burning; reliable in cold climates | Requires pressurised tank storage; lower energy density than diesel; tank refuelling logistics | Tier 2 facilities; backup for natural gas generators |

**Fuel capacity calculation** (diesel generators):
1. Determine generator fuel consumption rate at full load (litres/hour, from manufacturer data)
2. Multiply by required runtime (48 hours for Tier 1)
3. Add 20% safety margin
4. Result = minimum fuel tank capacity

**Fuel management requirements** (diesel):
- Fuel quality tested annually (water content, microbial contamination, oxidation stability)
- Fuel treatment (biocide, stabiliser) applied per manufacturer schedule
- Tank inspection annually (internal corrosion, water accumulation, structural integrity)
- Refuelling contract in place with guaranteed delivery within 24 hours of request
- Minimum fuel level maintained at 75% capacity (automatic monitoring where feasible)

### Cooling Systems

| Requirement | Tier 1 — Critical Facilities | Tier 2 — Standard Facilities |
|-------------|-------------------------------|------------------------------|
| **Redundancy** | Dual cooling paths (N+1 minimum) | Single cooling system |
| **Monitoring** | Continuous temperature monitoring with automated alerting | Monitored during staffed hours |
| **Failure response** | Automatic failover to redundant unit; alert to facilities management | Alert to facilities management; manual response |

- Cooling capacity shall be sufficient for the current heat load plus planned growth.
- Cooling systems shall be maintained per manufacturer service schedules, with air filters replaced at recommended intervals.

### Telecommunications Redundancy

| Requirement | Tier 1 — Critical Facilities | Tier 2 — Standard Facilities |
|-------------|-------------------------------|------------------------------|
| **Internet connectivity** | Dual ISP with automatic failover | Single ISP (secondary recommended based on risk assessment) |
| **Path diversity** | Diverse physical entry points where feasible | Single entry acceptable |
| **Monitoring** | Continuous with automated failover and alerting | Monitored during staffed hours |

- Power and telecommunications cabling carrying data or supporting information services shall be protected from interception, interference, or damage.
- Power cables shall be segregated from communications cables to prevent interference.
- Access to cable rooms and patch panels shall be restricted by physical access control.

#### Telecommunications Failover Procedures

Automated and manual failover procedures shall be documented and tested to ensure connectivity continuity:

**Automatic failover** (Tier 1 facilities with dual ISP):

| Step | Action | Target Time |
|------|--------|------------|
| 1 | Primary ISP failure detected (link down, packet loss >5%, latency >200ms) | Detection within 30 seconds |
| 2 | Automatic failover to secondary ISP initiated by routing equipment | Failover within 60 seconds |
| 3 | Alert generated to IT Operations (email + monitoring dashboard) | Immediate |
| 4 | IT Operations verifies service restoration and investigates primary ISP failure | Within 15 minutes |
| 5 | Primary ISP restored → automatic failback (or manual failback if configured) | Per ISP restoration |

**Manual failover** (Tier 2 facilities or single-ISP with backup):

| Step | Action | Owner |
|------|--------|-------|
| 1 | ISP outage reported or detected via monitoring | IT Operations |
| 2 | Verify outage is ISP-side (not internal equipment failure) | IT Operations |
| 3 | Activate backup connectivity (4G/5G failover, mobile hotspot, or alternate ISP) | IT Operations |
| 4 | Notify affected users of degraded connectivity and estimated restoration | IT Operations |
| 5 | Monitor primary ISP restoration; restore normal routing when available | IT Operations |

**Single-ISP backup for Tier 2 facilities**: Where a single ISP is deployed, a 4G/5G mobile broadband failover device (e.g., Cradlepoint, Peplink, or equivalent) shall be available as backup. Failover device shall be tested quarterly to confirm SIM activation and bandwidth sufficiency for critical services.

### Utility Testing Schedule

All utility resilience systems shall be tested at regular intervals to verify operational readiness:

| System | Test Type | Frequency | Pass Criteria | Owner |
|--------|-----------|-----------|---------------|-------|
| **UPS** | Failover test (simulate mains failure, verify transfer to battery) | Quarterly | Clean transfer within rated time; load sustained for rated runtime | Facilities Manager |
| **UPS** | Battery capacity test (full discharge under load) | Annually | Battery capacity >= 80% of rated capacity | Facilities Manager |
| **Backup generator** | No-load start test | Monthly | Start within 30 seconds; stable voltage and frequency within 60 seconds | Facilities Manager |
| **Backup generator** | Load bank test (minimum 30% nameplate rating, 30 minutes) | Semi-annually | Sustains rated load; exhaust temperature within limits | Facilities Manager |
| **Backup generator** | Full-load transfer test (end-to-end with ATS) | Annually | Automatic transfer and retransfer without interruption to protected load | Facilities Manager |
| **Cooling** | Redundancy failover verification | Quarterly | Standby unit activates; temperature remains within thresholds | Facilities Manager |
| **Telecommunications** | ISP failover test | Annually | Automatic or manual failover within documented target time; services restored | IT Operations |

Test results shall be documented with: test date, system tested, test procedure, pass/fail result, issues identified, and corrective actions. Test records shall be retained for 5 years.

**Failed test response**: Any test failure shall trigger immediate investigation, interim compensating controls (e.g., restrict facility use, increase monitoring), and remediation within 30 days. Repeat failures shall be escalated to the CISO.

### Utility Monitoring

- Utility systems (power, cooling, telecommunications) shall be monitored in real-time with alerting for failures, threshold excursions, and degraded conditions.
- Utility monitoring systems should be integrated with [BMS] or [Environmental Monitoring System] for centralised visibility.
- Utility incidents shall be logged and reported per the incident management process.

---

## Facility Criticality Tiers

Facilities shall be classified into criticality tiers based on business impact analysis. The tier classification drives monitoring intensity, environmental protection requirements, and utility resilience levels throughout this policy.

| Attribute | Tier 1 — Critical | Tier 2 — Standard |
|-----------|-------------------|-------------------|
| **Definition** | Datacentres, primary server rooms, disaster recovery sites | Corporate offices, branch offices, non-critical server rooms |
| **Classification criteria** | Hosts Tier 1/2 business systems; processes CONFIDENTIAL data; RTO < 4 hours | Hosts Tier 3/4 systems; processes INTERNAL data; RTO > 4 hours |
| **Monitoring** | 24/7 monitoring (SOC or alarm monitoring service); < 15-minute response SLA; intrusion detection required | Business-hours monitoring (8/5); next-business-day response acceptable; intrusion detection based on risk |
| **Environmental** | Fire suppression + detection; water detection all zones; temperature 18–27 °C +/- 2 °C; continuous monitoring | Fire detection mandatory (suppression if equipment > CHF 500k); water detection high-risk areas; temperature 18–27 °C +/- 5 °C |
| **Utility — Power** | N+1 UPS (dual units, 30-min runtime each); backup generator (48-hr fuel); ATS | Single UPS (15-min runtime minimum); generator optional |
| **Utility — Cooling** | Dual cooling paths (N+1); continuous monitoring | Single cooling system; monitoring during staffed hours |
| **Utility — Telecom** | Dual ISP with automatic failover; diverse path entry | Single ISP; secondary recommended |
| **Review frequency** | Monthly manual verification of all systems | Quarterly manual verification of all systems |

**Tier assignment process**: System owners, in consultation with the Facilities Manager and CISO, shall determine the appropriate tier for each facility based on business impact analysis results. Tier assignments shall be reviewed annually.

---

## Incident Classification

Physical infrastructure security events shall be classified and responded to based on severity:

| Severity | Examples | Required Response |
|----------|----------|-------------------|
| **Critical** | Unauthorised access to restricted areas; physical breach; theft of equipment; major fire or flood; total power or cooling failure | Immediate response; activate incident management process; notify CISO and executive management within 1 hour |
| **High** | Repeated failed access attempts; tailgating detected; lost access badges; environmental alerts approaching critical thresholds; partial utility failure | Same-day investigation and response; notify CISO within 4 hours |
| **Medium** | Door held open alerts; frequent false alarms; minor environmental excursions (within alert but not critical thresholds); single utility test failure | Documented and investigated within 5 business days; trend analysis |
| **Low** | Single failed access attempt; minor policy violations; scheduled maintenance notifications | Logged for trend analysis; reviewed monthly |

Physical security incidents shall be reported and managed through the organisation's incident management process (A.5.24–28).

---

## Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| **Chief Information Security Officer (CISO)** | Overall accountability for physical infrastructure security policy; risk acceptance for exceptions; budget approval; executive reporting on physical security posture |
| **Facilities Manager** | Day-to-day physical infrastructure operations; environmental and utility system maintenance; vendor management for building services; utility testing programme execution |
| **Security Operations Manager** | Physical security monitoring implementation; access control system management; CCTV operations; intrusion detection management; physical security incident coordination |
| **IT Operations** | Physical-logical security integration (SIEM); network infrastructure supporting security systems; telecommunications redundancy management |
| **System Owners** | Define physical security requirements for owned systems; participate in facility tier classification; report physical security incidents |
| **Internal Audit** | Annual physical security compliance verification; evidence review; control testing |
| **All Employees** | Report physical security incidents and suspicious activity; comply with access control and visitor management procedures; follow environmental emergency procedures |

---

## Evidence for This Policy

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Physical access control logs** (access granted/denied events with individual identification) | Security Operations Manager | *Continuous logging; reviewed monthly; retained 12 months* |
| 2 | **CCTV system operational records** (uptime reports, camera health checks, recording verification) | Security Operations Manager | *Weekly health checks; retained 12 months* |
| 3 | **Intrusion detection test records** (quarterly test results, alarm response verification) | Security Operations Manager | *Quarterly; retained 3 years* |
| 4 | **Visitor management logs** (visitor register with name, organisation, host, escort compliance) | Security Operations Manager | *Continuous; retained 12 months* |
| 5 | **Access rights review records** (semi-annual review results, revocation actions) | Security Operations Manager | *Semi-annually; retained 3 years* |
| 6 | **Fire system inspection and test records** (detection and suppression system certificates, fire door tests) | Facilities Manager | *Semi-annual / annual per tier; retained 5 years* |
| 7 | **Environmental monitoring data** (temperature, humidity logs; threshold excursion records) | Facilities Manager | *Continuous logging; retained 12 months* |
| 8 | **Water detection system maintenance and test records** | Facilities Manager | *Quarterly verification; retained 3 years* |
| 9 | **UPS test records** (quarterly failover tests, annual capacity tests) | Facilities Manager | *Per testing schedule; retained 5 years* |
| 10 | **Generator test records** (monthly start tests, semi-annual load tests, annual transfer tests) | Facilities Manager | *Per testing schedule; retained 5 years* |
| 11 | **Cooling redundancy verification records** (quarterly failover tests) | Facilities Manager | *Quarterly; retained 3 years* |
| 12 | **Telecommunications failover test records** | IT Operations | *Annually; retained 3 years* |
| 13 | **Environmental threat risk assessment** (facility-specific risk assessment with review history) | Facilities Manager / CISO | *Annual review; retained 5 years* |
| 14 | **Emergency response drill records** (drill date, scenario, participants, findings, actions) | Facilities Manager | *Annually; retained 3 years* |
| 15 | **Exception register** (approved deviations from policy with risk acceptance and compensating controls) | CISO | *Per event; reviewed quarterly; retained active + 2 years* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, physical security system reports, utility test records, environmental monitoring data, facility inspections, internal and external audits, and feedback to the policy owner.

Compliance shall be assessed using the following weighted metrics:

| Metric | Weight | Measurement Source |
|--------|--------|-------------------|
| Access control system availability and log completeness | 20% | [Access Control System] logs |
| Environmental parameter compliance (temperature/humidity within thresholds) | 20% | [Environmental Monitoring System] / [BMS] |
| Utility resilience test success rate (all tests passed on schedule) | 15% | Test records |
| Fire and water detection system operational status | 15% | Inspection records |
| Physical security incident response time adherence | 15% | Incident records |
| Visitor management compliance (registration, escort, badge return) | 10% | Visitor logs |
| Physical security awareness training completion | 5% | Training records |

| Score | Rating | Action |
|-------|--------|--------|
| > 90% | Excellent | Maintain current controls |
| 75–89% | Good | Address gaps in next review cycle |
| 60–74% | Acceptable | Develop remediation plan within 30 days |
| < 60% | Non-Compliant | Immediate remediation required; CISO escalation |

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk assessment, compensating controls, and a defined review date (maximum 6 months, renewable). Valid exception scenarios include technical infeasibility, disproportionate cost relative to risk, and temporary variance during facility transitions. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to facility operations, environmental risk profiles, regulatory requirements, technology advancements in physical security systems, lessons learned from incidents and utility test failures, and audit findings.

---

# Areas of the ISO 27001 Standard Addressed

Physical Infrastructure Security Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | **7.4 Physical security monitoring** |
| | **7.5 Protecting against physical and environmental threats** |
| | 7.8 Equipment siting and protection |
| | **7.11 Supporting utilities** |
| | 7.12 Cabling security |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures for physical security of data processing facilities |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security including physical measures |
| EU GDPR (where applicable) | Art. 32 — Security of processing including physical measures |
| ISO/IEC 27001:2022 | Annex A Controls 7.4 (Physical Security Monitoring), 7.5 (Environmental Protection), 7.11 (Supporting Utilities) |
| ISO/IEC 27002:2022 | Sections 7.4, 7.5, 7.11 — Implementation guidance |
| ASHRAE | Thermal guidelines for data processing environments (temperature/humidity) |
| NFPA 2001 / ISO 14520 | Clean agent fire suppression systems for occupied spaces |
| NFPA 110 | Emergency and standby power systems testing requirements |
| NIST SP 800-53 Rev 5 | PE-1 through PE-20 — Physical and Environmental Protection family |
| CIS Controls v8 | Control 1 (Inventory), Control 12 (Network Infrastructure — physical cabling) |
| **Conditional**: FINMA Circular 2023/1 | Swiss regulated financial institution — enhanced physical security requirements |
| **Conditional**: DORA (EU) 2022/2554 | EU financial services entity — operational resilience for ICT infrastructure |
| **Conditional**: NIS2 (EU) 2022/2555 | Essential/important entity in EU — physical security for critical infrastructure |

---

<!-- QA_VERIFIED: 2026-02-07 -->
