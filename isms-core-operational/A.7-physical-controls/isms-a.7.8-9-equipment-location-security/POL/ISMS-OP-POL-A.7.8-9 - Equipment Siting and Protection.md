<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.8-9:operational:OP-POL:a.7.8-9 -->
**ISMS-OP-POL-A.7.8-9 — Equipment Siting and Protection**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Equipment Siting and Protection |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.7.8-9 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 0.1 |
| **Version Date** | [Date] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Controls A.7.8, A.7.9 — Equipment siting and protection, security of assets off-premises
- ISO/IEC 27002:2022 Sections 7.8, 7.9 — Implementation guidance
- ISMS-OP-POL-A.7.1-2-3 (Physical Access Control)
- ISMS-OP-POL-A.7.4-5-11 (Physical Infrastructure Security)
- ISMS-OP-POL-A.6.7-8 (Remote Working and Security Event Reporting)
- ISMS-OP-POL-A.5.9 (Asset Management)
- ISMS-OP-POL-A.8.1-7-18-19 (Endpoint Security)

**Related Annex A Controls**:

| Control | Relationship to Equipment Siting and Protection |
|---------|--------------------------------------------------|
| A.7.1 Physical security perimeters | Perimeter boundaries define zones where equipment may be sited |
| A.7.2 Physical entry | Entry controls protect areas containing equipment |
| A.7.3 Securing offices, rooms, and facilities | Secure areas house critical equipment |
| A.7.4 Physical security monitoring | Monitoring detects unauthorised access to equipment locations |
| A.7.5 Protecting against physical and environmental threats | Environmental controls protect equipment from hazards |
| A.7.11 Supporting utilities | Power, cooling, and telecommunications sustain equipment operation |
| A.7.12 Cabling security | Power and data cabling supports equipment connectivity |
| A.7.13 Equipment maintenance | Maintenance preserves equipment availability and integrity |
| A.7.14 Secure disposal or re-use of equipment | End-of-life handling follows secure disposal requirements |
| A.5.9 Inventory of information and other associated assets | Asset inventory records equipment location and custodian |
| A.6.7 Remote working | Remote working procedures address off-premises equipment use |
| A.8.1 User endpoint devices | Endpoint security policies cover portable equipment protection |

**Related Internal Policies**:

- Physical Access Control Policy
- Physical Infrastructure Security Policy
- Remote Working and Security Event Reporting Policy
- Asset Management Policy
- Endpoint Security Policy
- Incident Management Policy

---

# Equipment Siting and Protection Policy

## Purpose

The purpose of this policy is to reduce the risks of loss, damage, theft, or compromise of information processing equipment through secure placement, environmental protection, and appropriate safeguards for assets used both on-premises and off-premises. It establishes requirements for equipment siting, power and cabling protection, and the security of assets when taken outside organisational facilities.

This policy addresses two related ISO 27001:2022 controls as a unified framework because they represent complementary aspects of equipment protection throughout its operational lifecycle: A.7.8 governs secure placement and environmental protection of equipment at organisational facilities, while A.7.9 extends protection to equipment used off-premises — in transit, at employee homes, in public spaces, or permanently installed at remote locations.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect the availability, integrity, and confidentiality of personal data through physical equipment protection controls. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 requirements for security of processing including physical measures also apply.

## Scope

All employees, contractors, and third-party users who handle, operate, transport, or have custody of organisation equipment.

All information processing equipment owned, leased, or operated by the organisation, including:

- Servers, storage systems, and network infrastructure
- Workstations, laptops, and mobile devices
- Telecommunications equipment and cabling
- Printers, scanners, and multifunction devices
- Removable storage media (USB drives, external drives)
- Edge appliances, sensors, and permanently off-site equipment

All locations where organisation equipment is used:

- On-premises facilities (datacentres, server rooms, offices)
- Colocation and third-party datacentre facilities
- Employee home offices
- Travel locations, hotels, client sites
- Public spaces (airports, cafes, co-working spaces)
- Permanent off-site installations (remote sensors, edge devices)

**Out of scope**:

- Physical access control to equipment areas (covered under A.7.1-2-3)
- Environmental monitoring and protection systems (covered under A.7.4-5-11)
- Supporting utilities — power, cooling, telecommunications (covered under A.7.4-5-11)
- Equipment disposal and secure re-use (covered under A.7.14)
- Cabling infrastructure security (covered under A.7.12)
- Personnel security and background checks (covered under A.6.1-6.4)

### Cloud-Only Organisations

Organisations operating 100% in cloud environments with no on-premises information processing facilities may mark Control A.7.8 as "Not Applicable" in the Statement of Applicability. However, A.7.9 remains applicable wherever employees use laptops, mobile devices, or other portable equipment off-premises.

The "Not Applicable" determination for A.7.8 shall be documented with:

- Asset inventory reference confirming no on-premises information processing facilities.
- Cloud provider physical security verification through SOC 2 Type II report or ISO 27001 certification review.
- Annual review confirmation that cloud-only status remains accurate.

## Principle

Equipment siting and protection is built on the principle that information processing equipment requires physical safeguards proportionate to the sensitivity of data it processes and the criticality of services it supports — regardless of whether that equipment is on organisational premises or in the field. Controls shall be selected based on documented risk assessment.

---

## Equipment Classification for Protection

Equipment shall be classified into protection categories to determine appropriate siting requirements and off-premises protection levels:

| Category | Examples | Siting Requirement | Off-Premises |
|----------|----------|--------------------|--------------|
| **Category A — Critical Infrastructure** | Servers, core network switches, SAN/NAS storage, firewalls, domain controllers | Dedicated access-controlled room; environmental monitoring; redundant power | Removal requires CISO approval; limited to: (1) datacentre migration or relocation, (2) hardware repair/replacement where on-site service is not possible, (3) disaster recovery relocation to pre-approved alternate site |
| **Category B — Business Equipment** | Workstations, printers, VoIP phones, meeting room displays | Controlled office environment; standard environmental conditions | Line manager authorisation; asset tracking required |
| **Category C — Portable Equipment** | Laptops, tablets, mobile phones, portable projectors | Secured when unattended; cable locks in shared spaces | Line manager authorisation; full-disk encryption; remote wipe; GPS tracking where supported |
| **Category D — Removable Media** | USB drives, external hard drives, backup tapes | Locked storage when not in use; classified media in safes | Encrypted media only; authorisation required; chain of custody |
| **Category E — Permanently Off-Site** | Edge appliances, remote sensors, ATMs, kiosk terminals, digital signage | Tamper-resistant enclosure; IP-rated housing; remote monitoring | N/A (always off-site); physical inspection schedule; tamper detection |

Category assignment shall be recorded in [Asset Management System] or [CMDB] as part of asset registration.

---

## Equipment Siting Requirements (A.7.8)

> *Equipment should be sited securely and protected.*

Equipment processing or storing information shall be sited to reduce risks from physical and environmental threats, unauthorised access, and damage.

### Location Selection

- Equipment shall be placed in areas with controlled physical access, appropriate to the classification of information it processes.
- Critical equipment (servers, network infrastructure, storage systems) shall be located in dedicated, access-controlled rooms — not in general office areas, reception zones, or publicly accessible spaces.
- Equipment shall be positioned to minimise risk of overlooking (shoulder surfing). Screens displaying sensitive or confidential information shall be positioned away from windows, corridors, and high-traffic areas.
- Information processing facilities handling classified data should be positioned carefully so that unauthorised persons cannot view information displayed on screens during use. Where repositioning is not feasible, privacy screens shall be used.
- Organisation-managed equipment shall be clearly segregated from equipment not under organisational control (e.g., personal devices, visitor equipment, shared-tenancy infrastructure).
- Storage facilities (server racks, storage cabinets, safe rooms) shall be secured to prevent unauthorised access.

### Environmental Considerations

- Equipment shall be protected from temperature extremes, humidity, dust, vibration, and corrosive atmospheres. Acceptable environmental conditions for equipment operation shall be defined based on manufacturer specifications.
- Adequate ventilation and cooling shall be provided for equipment rooms. Server rooms and datacentres shall maintain temperature within 18-27 degrees C and humidity within 20-80% relative humidity, consistent with ASHRAE thermal guidelines.
- Equipment shall be elevated or protected where flood risk exists (e.g., raised floors, ground-level barriers, avoidance of basement locations in flood-prone areas).
- Smoking, eating, and drinking shall be prohibited in server rooms, datacentres, and equipment closets. Guidelines for eating and drinking near workstations shall be communicated to all personnel.
- Environmental conditions that may disrupt operations (temperature, humidity, airborne particulates) shall be continuously monitored in rooms housing Category A (critical infrastructure) equipment, with automated alerting within 15 minutes when thresholds are exceeded. For rooms housing Category B equipment, continuous monitoring should be implemented where technically feasible.

### Power and Cabling Protection

**Power Supply**:

- Equipment shall be protected from power failures using uninterruptible power supply (UPS) systems appropriate to equipment criticality.
- Power cables shall be protected from interception or damage through conduit, trunking, or enclosed cable trays.
- Emergency power-off (EPO) switches shall be located near server room and datacentre exits for use in emergencies. EPO switches shall be clearly labelled, protected against accidental activation (e.g., hinged cover, break-glass enclosure), and tested annually as part of the electrical safety programme.
- Power supplies shall be redundant for critical equipment (N+1 configuration recommended).
- Lightning protection shall be applied to buildings housing information processing facilities. Surge protection filters shall be fitted to all incoming power and telecommunications lines.

**Network Cabling**:

- Network cables carrying data or supporting information services shall be protected from interception, interference, or damage.
- Power cables shall be segregated from communications cables to prevent electromagnetic interference.
- Cable runs shall be documented in the asset register and reviewed at least annually and upon material changes.
- Fibre optic cables should be used for high-security data transmissions where the risk of interception warrants it.
- Cabling closets and patch panels shall have appropriate physical access controls.
- Network jacks in public areas shall not provide access to the internal network unless explicitly authorised and monitored.

### Colocation and Third-Party Datacentres

Where equipment is hosted in colocation or third-party datacentre facilities:

- The organisation shall ensure that siting, physical access, environmental protection, and power resilience meet the requirements of this policy, verified through contractual obligations and periodic assurance.
- Third-party facility assurance shall be obtained through one or more of: SOC 2 Type II audit report (reviewing PE-related controls specifically), ISO 27001 certification (confirming Annex A physical controls in scope), or documented on-site inspection using the organisation's physical security checklist. Where SOC 2 or ISO 27001 reports are relied upon, the organisation shall verify:
  - The report covers the specific facility where organisation equipment is hosted (not just the provider's headquarters).
  - The report period is current (issued within the last 12 months).
  - Any qualifications, exceptions, or complementary user entity controls (CUECs) are reviewed and addressed.
- A formal responsibility matrix shall be maintained in the colocation contract, documenting which party is responsible for each physical security and environmental control.
- Evidence of third-party compliance shall be retained and reviewed annually. Material changes to third-party facility security shall be reported to the organisation under contractual notification clauses.
- **Vendor risk management (SOC 2: CC9.2)**: Colocation and datacentre providers shall be included in the organisation's vendor risk management programme. Equipment-related vendor risks (physical security, environmental resilience, staffing, financial stability) shall be assessed at onboarding and reviewed annually. SLA compliance for uptime, incident response, and physical access notification shall be monitored against contractual thresholds.

### Visitor Equipment on Premises (SOC 2: CC6.4)

Where visitors (clients, vendors, contractors, auditors) bring personal or employer-owned equipment on-premises:

- Visitor devices shall not connect to the organisation's internal network. A segregated guest WiFi network shall be provided where visitor Internet access is required.
- Visitors bringing equipment into access-controlled areas (server rooms, secure areas) shall declare the equipment at reception and confirm its removal upon departure.
- Where visitor equipment must interface with organisation systems (e.g., vendor diagnostic tools, auditor equipment), IT Operations shall inspect the device, confirm current endpoint protection, and provide a time-limited, scope-restricted network connection.
- Visitor equipment use shall be documented in the visitor log, recording: device type, purpose, areas accessed, and time on-premises.

### Industrial and Hostile Environments

Where equipment is located in industrial, manufacturing, or otherwise harsh environments:

- Additional protective measures shall be implemented, including dust covers, sealed enclosures, and protective housings rated to appropriate IP (Ingress Protection) standards.
- Equipment ratings shall match or exceed environmental conditions. IP65 or higher should be used for environments with significant dust or water exposure.
- Special protection methods shall be considered, such as keyboard membranes in industrial settings to prevent contamination.
- Maintenance frequency shall be increased for equipment in hostile environments, with inspection intervals defined in the maintenance schedule.
- Equipment processing classified information in exposed locations shall be protected against information leakage due to electromagnetic emanation, where risk assessment warrants it.

---

## Security of Assets Off-Premises (A.7.9)

> *Off-site assets should be protected.*

Off-site assets shall be protected to prevent loss, damage, theft, or compromise of devices and to prevent interruption to the organisation's information processing activities.

### Authorisation and Tracking

**Removal Authorisation**:

- Removal of equipment from organisational premises shall be authorised by the appropriate line manager prior to removal.
- Authorisation records shall document: equipment details (asset tag, serial number, type), purpose of removal, responsible person, expected return date, and any special handling requirements.
- High-value equipment (value exceeding [CHF threshold]) or equipment containing classified data shall require additional approval from [IT Operations Manager] or equivalent.
- Bulk equipment moves (e.g., office relocation, project deployment) shall be authorised through a formal equipment movement request.

**Asset Tracking**:

- Equipment removed from premises shall be logged in [Asset Management System] or [CMDB] with current location, custodian, and expected return date.
- Chain of custody shall be maintained when equipment transfers between individuals. Transfer records shall include both the releasing and receiving party, date, and equipment condition.
- Return of equipment shall be verified and recorded. Equipment shall be inspected upon return for damage, tampering, or missing components.
- Equipment not returned by the expected date shall trigger follow-up by the asset owner. Equipment overdue by more than 30 days shall be escalated to the line manager and IT Operations.

### Physical Security Off-Premises

**General Requirements**:

- Equipment shall not be left unattended in public places (airports, cafes, conference venues, public transport, vehicles).
- Equipment shall be carried in unmarked, nondescript bags during transport — not in manufacturer-branded bags or cases that advertise high-value contents.
- When not in active use, equipment shall be secured in hotel safes (noting size limitations — laptops may not fit standard hotel safes), locked storage, or other secured areas. Where hotel safe capacity is insufficient, equipment shall be kept in locked luggage or the employee shall take equipment with them. Equipment shall not be left visible in hotel rooms.
- Vehicle storage shall only be used when absolutely necessary, and equipment shall be placed in the boot (trunk) out of sight — never on seats or visible through windows.

**Environmental Protection During Transport**:

- Equipment shall be protected from extreme temperatures during transport and storage. Manufacturer guidelines for safe operating and storage temperature ranges shall be observed.
- Equipment shall not be exposed to direct sunlight for extended periods.
- Moisture and humidity protection shall be maintained during transport (padded bags, weatherproof cases for outdoor transport).
- Equipment shall be transported in padded carrying cases to protect against physical shock and vibration.

**Theft Prevention Measures**:

- Equipment shall be physically secured where possible using cable locks, lockdown plates, or equivalent physical tethering in shared or semi-public environments.
- GPS tracking or location services shall be enabled on supported devices where technically feasible and legally permitted. GPS tracking configuration shall:
  - Minimise employee location monitoring (device location only, not continuous personal tracking).
  - Be documented in the organisation's internal privacy policy with appropriate transparency notice to users.
  - Comply with Swiss nFADP proportionality requirements and any applicable cantonal employee monitoring restrictions.
  - Account for technical constraints: GPS/location services require OS-level support (iOS Find My, Android Device Manager, or equivalent MDM location feature); devices without network connectivity may not report location until reconnected; battery-saving modes may limit location accuracy.
  - Where GPS tracking is not technically feasible or legally permitted, compensating controls shall be documented (e.g., enhanced physical security awareness, encrypted full-disk protection, reduced data residency on device).
- Remote wipe capability shall be configured on all supported mobile devices through [MDM] and shall be:
  - Tested at least annually and after significant MDM platform changes.
  - Executable within 4 hours of a confirmed loss or theft report during business hours; within 12 hours for after-hours reports.
  - For after-hours incidents: an emergency contact procedure shall be documented and communicated to all personnel, enabling out-of-hours remote wipe initiation through [on-call IT Operations contact / MDM self-service portal].
  - Evidence of test results retained for audit purposes.
- Equipment serial numbers, asset tags, and descriptions shall be recorded in [Asset Management System] to support police reports and insurance claims in case of theft.
- Organisation equipment labels (company name, asset tags) should be discreet — sufficient for internal identification but not advertising theft targets:
  - **Good practice**: Small asset tag with barcode/QR code; engraved serial number on underside; internal-only RFID tag.
  - **Avoid**: Large company logo stickers on laptop lids; "Property of [Company Name]" labels visible during transport; branded laptop bags or sleeves.

### Home Office Requirements

Where employees work from home with organisation equipment:

- Equipment shall be stored securely when not in use — in a locked room, cabinet, or desk drawer where feasible.
- Network connections shall be secured with encrypted WiFi (WPA3 preferred, WPA2 minimum). VPN shall be used for all access to organisation systems, except where the organisation has implemented a zero-trust network architecture or where access is exclusively to SaaS applications over HTTPS with enforced SSO and device certificate validation.
- Family members, visitors, and other household members shall not have access to organisation equipment. Screen lock shall be activated when the employee steps away.
- The home office environment should provide adequate environmental conditions (temperature, humidity, ventilation) to prevent equipment damage.
- Employees shall acknowledge home office security requirements as a condition of remote working authorisation.

### Public Spaces

When working with organisation equipment in public or shared spaces:

- Privacy screens shall be used when working with sensitive or confidential information in environments where shoulder surfing is possible (public transport, cafes, airport lounges, co-working spaces).
- Public WiFi shall only be used with VPN protection, except where the organisation has implemented zero-trust network architecture or where access is limited to SaaS applications over HTTPS with enforced SSO and device certificate validation. Direct connection to public WiFi without VPN or equivalent protection for accessing organisation systems or data is prohibited.
- Bluetooth, AirDrop, and other wireless sharing protocols shall be disabled when not actively required.
- Equipment shall never be left unattended in public spaces, even briefly.
- Screen pop-ups and notifications (messaging alerts, email previews, calendar entries) should be disabled during presentations, screen sharing, or when working in public areas to prevent inadvertent disclosure.

### Permanently Off-Site Equipment

Where the organisation deploys equipment permanently installed outside organisational premises, the following scenarios are in scope:

- **Customer-hosted appliances**: Network devices, monitoring sensors, or processing equipment installed at customer premises under managed service agreements.
- **Remote infrastructure**: Telecommunications equipment at cell towers, utility substations, or remote offices without permanent staff.
- **Public-facing terminals**: ATMs, self-service kiosks, payment terminals, or digital signage in retail or public locations.
- **Environmental sensors**: IoT devices for building management, environmental monitoring, or industrial process control.
- **Edge computing nodes**: Edge servers or gateways deployed at branch offices, warehouses, or manufacturing facilities.

Requirements for permanently off-site equipment:

- Physical tamper detection shall be implemented (tamper-evident seals, chassis intrusion detection, tamper alarms) appropriate to asset criticality.
- Environmental monitoring shall be continuous where technically feasible, with remote alerting for threshold excursions.
- Regular physical inspection schedules shall be established, with frequency based on risk assessment and equipment criticality.
- Remote monitoring and management capabilities shall be enabled to maintain visibility of equipment health, security status, and configuration integrity.
- Logical access restrictions (encrypted communications, strong authentication, certificate-based access) shall compensate for reduced physical security.
- Incident response procedures shall account for remote locations, including response time expectations and local contact arrangements.
- **Environmental failure failover (SOC 2: A1.2)**: For permanently off-site equipment supporting critical services, failover procedures shall be documented for environmental failure scenarios (power loss, cooling failure, network outage). Failover may include: automatic switchover to redundant equipment at alternate location, graceful degradation with reduced service, or manual relocation to a pre-approved recovery site. Failover procedures shall be tested annually as part of business continuity testing.
- Manufacturer protection instructions (electromagnetic fields, moisture, temperature, dust) shall be followed for permanently installed equipment.

### Travel Security

When transporting organisation equipment during business travel:

- Equipment shall be kept in hand luggage during air travel — never checked into hold baggage.
- Equipment shall not be left in vehicles overnight or for extended periods, even in locked vehicles.
- In high-risk travel destinations, additional precautions should be taken: use of travel-specific devices with minimal data, encrypted containers for sensitive data, and heightened physical awareness. High-risk destinations are determined by the organisation's travel risk assessment based on:
  - Government travel advisory level (Swiss FDFA, equivalent national advisory) at elevated or restricted status.
  - Known state-sponsored cyber-espionage activity targeting the organisation's industry sector.
  - Customs/border enforcement practices that routinely require device inspection or password disclosure.
  - History of equipment theft or seizure affecting business travellers in that jurisdiction.
- International travel with encrypted devices shall comply with destination country import/export regulations for cryptographic equipment.
- Lost or stolen equipment during travel shall be reported immediately to IT Operations (for remote wipe initiation) and to the local police. The employee shall document the circumstances and report through the incident management process upon return.

---

## Definitions

| Term | Definition |
|------|------------|
| **Equipment Siting** | The secure placement and positioning of information processing equipment to minimise physical, environmental, and access risks |
| **Off-Premises Assets** | Organisation equipment used outside organisational facilities, including at employee homes, client sites, and during travel |
| **Chain of Custody** | Documented transfer of equipment responsibility between individuals, recording releasing party, receiving party, date, and equipment condition |
| **Remote Wipe** | The capability to erase data from a device remotely through [MDM] or equivalent management platform |
| **Tamper Detection** | Physical or electronic mechanisms to detect unauthorised access to or modification of equipment (tamper-evident seals, chassis intrusion sensors) |
| **IP Rating (Ingress Protection)** | IEC 60529 classification system indicating equipment resistance to dust and water ingress (e.g., IP65 = dust-tight, protected against water jets) |
| **UPS (Uninterruptible Power Supply)** | Battery-backed power system providing short-term power during mains failure, allowing orderly shutdown or generator transfer |
| **EPO (Emergency Power-Off)** | Emergency shutdown mechanism for rapid de-energisation of equipment in server rooms or datacentres |

---

## Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| **Chief Information Security Officer (CISO)** | Overall accountability for equipment siting and protection policy; risk acceptance for exceptions; review and approval of siting standards; executive reporting on equipment security posture |
| **Facilities Manager** | On-premises equipment siting decisions; environmental conditions management; coordination with landlords and colocation providers; physical infrastructure supporting equipment |
| **IT Operations** | Equipment deployment and configuration; asset tracking in [Asset Management System]; MDM management; remote wipe capability; monitoring of off-site equipment |
| **Line Managers** | Authorise equipment removal from premises; ensure team compliance with off-premises security requirements; follow up on overdue equipment returns |
| **System Owners** | Define siting requirements for owned systems; participate in risk assessment for equipment placement; report equipment security concerns |
| **Data Protection Officer (where appointed)** | Advise on privacy implications of GPS tracking and remote wipe; review employee monitoring transparency notices |
| **All Personnel** | Protect equipment in their custody; comply with off-premises security requirements; report equipment loss, theft, damage, or security incidents immediately; follow transport and storage guidelines |

### Escalation Path

- Equipment siting concerns: Employee --> Facilities Manager --> CISO
- Equipment security concerns (off-premises): Employee --> Line Manager --> IT Operations --> CISO
- Equipment loss or theft: Employee --> IT Operations (immediate, for remote wipe) --> CISO --> Executive Management
- Equipment damage (environmental): Employee --> Facilities Manager --> IT Operations --> CISO

---

## Incident Classification

Equipment-related security events shall be classified and responded to based on severity:

| Severity | Examples | Required Response |
|----------|----------|-------------------|
| **Critical** | Equipment theft (Category A or B); loss of device containing classified data; physical breach of server room; confirmed data exposure from stolen equipment | Immediate response; initiate remote wipe; activate incident management process; notify CISO and executive management within 1 hour; file police report |
| **High** | Loss of portable device (Category C); equipment found unattended in public area; tamper evidence on off-site equipment; unauthorised equipment removal detected | Same-day investigation and response; initiate remote wipe if loss confirmed; notify CISO within 4 hours |
| **Medium** | Equipment siting non-compliance identified; overdue equipment return (> 30 days); environmental excursion in equipment room; colocation provider audit finding | Documented and investigated within 5 business days; remediation plan required |
| **Low** | Minor siting adjustment needed; single overdue equipment return (< 30 days); equipment label missing; cable routing discrepancy | Logged for trend analysis; corrected within next scheduled review |

Equipment security incidents shall be reported and managed through the organisation's incident management process (A.5.24-28).

---

## Implementation Checklist

The following checklist summarises key implementation actions by responsible role:

**IT Operations:**

- [ ] Configure remote wipe capability on all supported mobile devices via [MDM]
- [ ] Enable GPS tracking on supported devices (with DPO-reviewed privacy notice)
- [ ] Register all equipment in [Asset Management System] / [CMDB] with location and custodian
- [ ] Establish annual remote wipe testing schedule and retain test records
- [ ] Configure environmental monitoring alerts for equipment rooms (15-minute threshold for Category A)
- [ ] Verify colocation/third-party assurance reports are current (within 12 months)
- [ ] Establish permanently off-site equipment inspection schedules

**Facilities Manager:**

- [ ] Complete equipment siting assessment for all on-premises information processing equipment
- [ ] Verify environmental conditions (temperature, humidity) in equipment rooms meet ASHRAE guidelines
- [ ] Confirm EPO switches are functional and locations are clearly marked
- [ ] Maintain cable run documentation and review annually
- [ ] Establish visitor equipment inspection and isolation procedures
- [ ] Coordinate colocation physical security reviews

**Line Managers:**

- [ ] Communicate off-premises equipment security requirements to team members
- [ ] Establish equipment removal authorisation process for team
- [ ] Monitor overdue equipment returns and escalate as required
- [ ] Ensure home office security acknowledgements are current for all remote workers
- [ ] Brief team on travel security requirements including high-risk destination procedures

---

## Evidence for This Policy

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | **Equipment siting register** (equipment location, siting assessment, environmental compliance) | Facilities Manager | *Annual assessment; updated on material changes* | 3 years |
| 2 | **Equipment removal authorisation records** (approval, equipment details, purpose, expected return) | IT Operations | *Per event* | 3 years |
| 3 | **Asset tracking records** (off-premises equipment log from [Asset Management System] / [CMDB]) | IT Operations | *Continuous; reviewed quarterly* | 3 years |
| 4 | **Chain of custody records** (equipment transfer documentation between individuals) | IT Operations | *Per transfer event* | 3 years |
| 5 | **Equipment return verification records** (return inspection, condition, completeness) | IT Operations | *Per return event* | 3 years |
| 6 | **Remote wipe capability test records** (annual MDM test results, wipe execution logs) | IT Operations | *Annually; after MDM changes* | 3 years |
| 7 | **Equipment loss/theft incident reports** (incident details, response actions, police reports if applicable) | CISO / IT Operations | *Per incident* | 5 years |
| 8 | **Colocation/third-party assurance records** (SOC 2 reports, ISO 27001 certificates, inspection reports) | IT Operations / Facilities Manager | *Annually* | Active contract + 2 years |
| 9 | **GPS tracking privacy notice** (employee notification, policy documentation, consent/transparency records) | DPO / CISO | *Annual review; updated on changes* | Active + 2 years |
| 10 | **Home office security acknowledgements** (employee sign-off on remote working security requirements) | Line Managers / HR | *Upon remote working authorisation; annual renewal* | Employment + 2 years |
| 11 | **Environmental monitoring records for equipment rooms** (temperature, humidity logs, alert records) | Facilities Manager | *Continuous logging; retained 12 months minimum* | 12 months |
| 12 | **Equipment siting exception register** (approved deviations with risk acceptance and compensating controls) | CISO | *Per exception; reviewed quarterly* | Active + 2 years |
| 13 | **Permanently off-site equipment inspection records** (physical inspection results, tamper seal verification) | IT Operations | *Per inspection schedule* | 3 years |
| 14 | **Cable run documentation** (cable routes, annual review records) | Facilities Manager / IT Operations | *Annual review* | Current + 1 year |
| 15 | **Visitor equipment access records** (visitor devices brought on-premises, inspection, network isolation confirmation) | Facilities Manager / IT Operations | *Per visit* | 3 years |
| 16 | **Vendor risk assessment records** (equipment-related vendor risk evaluations, SLA compliance, physical security verification) | CISO / Procurement | *Annual; upon vendor onboarding* | Active contract + 2 years |
| 17 | **Environmental failure failover records** (failover activation logs, equipment relocation documentation, recovery testing results) | IT Operations / Facilities Manager | *Per event; recovery testing annually* | 3 years |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, equipment siting inspections, asset tracking system reports, MDM compliance reports, off-premises equipment audits, incident records, internal and external audits, and feedback to the policy owner.

Compliance shall be assessed using the following metrics:

| Metric | Target | Measurement Source |
|--------|--------|-------------------|
| Equipment with compliant siting (assessed against this policy) | 100% | Equipment siting register |
| Off-premises equipment with current tracking in [Asset Management System] | 100% | [Asset Management System] / [CMDB] |
| Mobile devices with remote wipe capability enabled | 100% | [MDM] compliance reports |
| Equipment losses/thefts per year | 0 | Incident records |
| Overdue equipment returns (> 30 days past expected date) | < 5 at any time | [Asset Management System] |
| Remote wipe test passed on schedule | 100% | Test records |
| Colocation/third-party assurance reports current (within 12 months) | 100% | Supplier assurance records |
| Home office security acknowledgements current | 100% for remote workers | HR / line manager records |

| Score | Rating | Action |
|-------|--------|--------|
| > 90% | Excellent | Maintain current controls |
| 75-89% | Good | Address gaps in next review cycle |
| 60-74% | Acceptable | Develop remediation plan within 30 days |
| < 60% | Non-Compliant | Immediate remediation required; CISO escalation |

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk assessment, compensating controls, and a defined review date (maximum 6 months, renewable). Valid exception scenarios include:

- Equipment placement in non-standard locations for operational requirements (with enhanced monitoring).
- Extended off-premises periods beyond standard authorisation (with documented justification).
- Alternative protection measures for legacy equipment that cannot support remote wipe or tracking (with compensating controls such as full-disk encryption and enhanced physical security).
- GPS tracking opt-out where privacy or legal constraints prevent enabling (with alternative loss prevention measures).

Exceptions shall be reported to the Management Review Team. Permanent exceptions to theft prevention or asset tracking requirements are not permitted.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Equipment loss or theft resulting from negligent failure to follow this policy may result in financial liability where permitted by applicable employment law.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to facility operations, equipment technology, remote working patterns, regulatory requirements, lessons learned from equipment incidents (loss, theft, environmental damage), and audit findings.

---

# Areas of the ISO 27001 Standard Addressed

Equipment Siting and Protection Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | **7.8 Equipment siting and protection** |
| | **7.9 Security of assets off-premises** |
| | 7.1 Physical security perimeters |
| | 7.4 Physical security monitoring |
| | 7.5 Protecting against physical and environmental threats |
| | 7.11 Supporting utilities |
| | 7.12 Cabling security |

# Regulatory Framework

| Framework | Relevance |
|-----------|-----------|
| **Swiss nFADP (revDSG)** | Art. 8 — Technical and organisational measures for physical security of data processing equipment |
| **Swiss DSV (Data Protection Ordinance)** | Art. 1-3 — Minimum requirements for data security including physical protection measures |
| **EU GDPR (where applicable)** | Art. 32 — Security of processing including physical measures for equipment protection |
| **ISO/IEC 27001:2022** | Annex A Controls 7.8 (Equipment Siting and Protection), 7.9 (Security of Assets Off-Premises) |
| **ISO/IEC 27002:2022** | Sections 7.8, 7.9 — Implementation guidance |
| **NIST SP 800-53 Rev 5** | PE-14 (Environmental Controls), PE-18 (Location of System Components), PE-17 (Alternate Work Site) |
| **CIS Controls v8** | Control 1 (Inventory and Control of Enterprise Assets), Control 12 (Network Infrastructure Management) |
| **ASHRAE** | Thermal guidelines for data processing environments (temperature and humidity ranges) |
| **IEC 60529** | IP (Ingress Protection) rating standard for equipment enclosure protection |
| **Conditional: FINMA Circular 2023/1** | Swiss regulated financial institution — enhanced physical security of ICT infrastructure |
| **Conditional: DORA (EU) 2022/2554** | EU financial services entity — ICT asset protection including off-premises |
| **Conditional: NIS 2 Directive (EU) 2022/2555** | Essential/important entity in EU — physical security measures for critical infrastructure |

---

<!-- QA_VERIFIED: 2026-02-07 -->
