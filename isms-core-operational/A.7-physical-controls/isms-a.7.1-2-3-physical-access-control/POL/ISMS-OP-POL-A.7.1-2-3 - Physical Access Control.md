<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.1-2-3:operational:OP-POL:a.7.1-2-3 -->
**ISMS-OP-POL-A.7.1-2-3 — Physical Access Control**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Physical Access Control |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.7.1-2-3 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 0.1 |
| **Version Date** | [To Be Determined] |
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

- ISO/IEC 27001:2022 Controls A.7.1, A.7.2, A.7.3
- ISO/IEC 27002:2022 Sections 7.1, 7.2, 7.3 — Implementation guidance
- ISMS-OP-POL-A.7.4-5-11 — Physical Infrastructure Security
- ISMS-OP-POL-A.7.6-7-14 — Information and Media Handling
- ISMS-OP-POL-A.7.8-9 — Equipment Location Security
- ISMS-OP-POL-A.5.15-16-18 — Identity and Access Management
- ISMS-OP-POL-A.5.24-28 — Incident Management

**Related Annex A Controls**:

| Control | Relationship to Physical Access Control |
|---------|----------------------------------------|
| A.7.4 Physical security monitoring | Monitoring of perimeters and entry points defined in this policy |
| A.7.5 Protecting against physical and environmental threats | Environmental protection for areas secured by this policy |
| A.7.6 Working in secure areas | Behavioural requirements within zones defined here |
| A.7.8 Equipment siting and protection | Equipment placement within secured areas |
| A.5.15-16-18 Identity and access management | Logical access integration with physical access controls |
| A.5.24-28 Incident management lifecycle | Escalation path for physical security events |
| A.6.7 Remote working | Remote working reduces on-site access footprint |
| A.8.12 Data leakage prevention | Physical controls complement technical DLP measures |

---

# Physical Access Control Policy

## Purpose

This policy establishes the organisation's requirements for physical access control, covering security perimeters, physical entry controls, and securing offices, rooms, and facilities. It defines the security zones, authentication requirements, visitor management procedures, and facility protection measures necessary to prevent unauthorised physical access to organisational premises and information assets.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect personal data (including sensitive personal data) stored or processed on organisational premises. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 requirements for physical security of processing also apply.

Controls A.7.1 (Physical Security Perimeters), A.7.2 (Physical Entry), and A.7.3 (Securing Offices, Rooms and Facilities) are combined because they form an integrated physical security framework: perimeters define boundaries, entry controls protect the crossing of those boundaries, and internal security measures protect specific areas within them.

**Cloud-only organisations**: Organisations operating entirely from cloud infrastructure with no owned or leased server rooms or datacenters shall still apply this policy to office premises, co-working spaces, and any location where organisational information is accessed or stored physically. Server room and datacenter requirements apply only where the organisation controls such facilities; for third-party datacenters and colocation, supplier assurance requirements apply.

## Scope

This policy applies to:

- All owned, leased, or operated premises including offices, datacenters, and remote sites.
- All areas: public reception, general office space, server rooms, datacenters, secure storage, and archive rooms.
- All entry points: main entrances, secondary doors, emergency exits, loading and delivery areas, windows, and roof access points.
- All personnel: employees, contractors, visitors, maintenance personnel, and delivery personnel.

Out of scope:

- Physical security monitoring and surveillance systems (covered by A.7.4).
- Environmental protection — fire, water, temperature (covered by A.7.5).
- Equipment siting and off-premises security (covered by A.7.8-9).
- Supporting utilities (covered by A.7.11).

## Principle

Physical security shall be designed using a defence-in-depth approach with concentric security zones, where each successive zone requires stronger authentication and authorisation. Access shall be granted on the principle of least privilege — personnel receive access only to the zones required to perform their role. All physical access shall be logged, regularly reviewed, and promptly revoked when no longer needed. The organisation fosters a security-aware culture where all personnel are expected to challenge unrecognised persons in secured areas and report physical security concerns without fear of reprisal.

---

## Physical Security Perimeters (A.7.1)

**ISO/IEC 27001:2022 Annex A.7.1 — Physical Security Perimeters**:

> *Security perimeters should be defined and used to protect areas that contain information and other associated assets.*

### Security Zone Model

The organisation shall define and document security zones using the following classification:

| Zone | Description | Example Areas | Access Population |
|------|-------------|---------------|-------------------|
| **Public Zone** | Accessible to the general public | Reception lobby, visitor waiting areas, external grounds | All persons |
| **Controlled Zone** | Authorised personnel only | General office areas, meeting rooms, break rooms | Employees, escorted visitors |
| **Restricted Zone** | Limited access, need-to-know basis | Executive offices, HR, finance, legal, records storage | Named personnel with business need |
| **High-Security Zone** | Strictly controlled access | Server rooms, datacenters, security operations, vault/safe rooms | Named personnel with explicit authorisation |

Each zone shall be documented on floor plans with clearly marked boundaries, entry points, and the access control mechanisms in use.

### Perimeter Construction Requirements

**Building perimeter (external)**:

- External walls, roofs, and floors shall be of solid construction appropriate to the risk.
- External doors shall be secured with locks and access control mechanisms (e.g., [Access Control System] badge readers, electronic locks).
- Windows shall be secured, particularly at ground level; ground-floor windows in proximity to Restricted or High-Security Zones shall be reinforced or fitted with security glazing.
- Emergency exits shall be alarmed and monitored; emergency exits shall not be usable for routine entry from outside.
- All fire doors on a security perimeter shall be alarmed, monitored, and tested in conjunction with the walls to establish the required level of resistance. Fire doors shall operate in accordance with Swiss fire safety regulations in a failsafe manner.
- Ventilation points and service openings shall not provide a bypass route into secured areas.
- Suitable intrusion detection systems shall be installed in accordance with applicable national or international standards (e.g., EN 50131).

**Internal perimeters (between zones)**:

- Partitions between Controlled, Restricted, and High-Security Zones shall extend floor-to-ceiling, including above suspended ceilings and below raised floors.
- Access points between zones shall have appropriate access controls matching the destination zone.
- Walls of Restricted and High-Security Zones shall prevent visual and audio eavesdropping where the risk assessment requires it.

**Perimeter inspections**:

- Building perimeter inspections shall be performed at minimum annually.
- Restricted and High-Security Zone perimeters shall be inspected at least quarterly and after any building modification or security incident.
- Inspection findings shall be documented and any gaps remediated within 30 days (or immediately if they present an imminent risk).

### Colocation and Shared Facilities

Where the organisation operates in colocation datacenters or shared office buildings:

- [Organisation]-controlled areas (cages, rooms, floors) shall be clearly delineated and documented.
- Contractual requirements for physical security, access logging, and incident notification shall be in place with the facility provider.
- Supplier assurance evidence (ISO 27001 certificate, SOC 2 Type II report, or equivalent attestation) shall be obtained and reviewed annually.
- Where the colocation provider's physical security does not meet this policy's requirements, documented risk acceptance with compensating controls shall be recorded.
- Shared infrastructure (lifts, corridors, common areas) shall not provide uncontrolled access to the organisation's secured areas.
- Key and card management for building access in shared facilities shall be coordinated with building management, with [Organisation] maintaining an independent record of all credentials issued.

**Information processing facilities separation**: Information processing facilities managed by the organisation shall be physically separated from those managed by external parties sharing the same building or floor.

---

## Physical Entry Controls (A.7.2)

**ISO/IEC 27001:2022 Annex A.7.2 — Physical Entry**:

> *Secure areas should be protected by appropriate entry controls to ensure that only authorised personnel are allowed access.*

### Entry Point Security

All entry points to secured areas shall be protected:

**Main entrances**:

- A staffed reception desk or equivalent control (intercom, video entry) shall operate during business hours.
- An access control system ([Access Control System] — e.g., Verkada, Genetec, Honeywell, Lenel, ASSA ABLOY/Salto, or equivalent RFID badge readers, mobile credentials, or biometric readers) shall authenticate all personnel entering beyond the Public Zone. Where systems are in selection, the interim approach and target deployment date shall be documented.
- Anti-tailgating measures shall be implemented at entry points to Restricted and High-Security Zones:

| Measure | Effectiveness | Zone Applicability |
|---------|--------------|-------------------|
| **Mantraps** (two-door interlocks) | High — physical prevention | High-Security Zones (servers, datacentres) |
| **Turnstiles with height sensors** | Medium-High — physical barrier + detection | Restricted Zones |
| **AI-enhanced CCTV** with tailgating detection | Medium — detection + alert | All secured zones |
| **Security awareness signage** + challenge culture | Low-Medium — behavioural | Minimum for all zones |

Current implementation: [Specify, e.g., "Turnstiles at main entrance; mantraps at datacentre; CCTV + awareness at secondary entries" or "Awareness + CCTV only; physical barriers planned for [quarter]"].
- After-hours access shall require additional authentication and shall generate alerts to security personnel or the on-call team.

### Emergency Access

**After-hours access** (outside business hours — [specify, e.g., 06:00–20:00 Mon–Fri]):
- Requires badge authentication + PIN (Controlled Zone minimum).
- Generates alert to on-call facilities / security monitoring.
- If challenge response not received within 15 minutes, escalation per incident procedure.

**Emergency lockdown**:
- Authority to initiate lockdown: CEO, COO, Facilities Manager, CISO, or on-site security.
- Lockdown triggers: Active threat on site, nearby incident affecting safety, natural disaster.
- Lockdown procedure: All external doors locked (badge access disabled); personnel shelter in place; emergency services notified; all-clear communicated via [PA system / SMS / email].

**Fire evacuation and security**:
- Fire doors unlock automatically on fire alarm (failsafe per Swiss fire code).
- Access control system restores after alarm reset and facilities inspection confirms safe.
- Evacuation assembly point outside secured perimeter; re-entry via controlled process after all-clear.

**Secondary and emergency entrances**:

- Side doors and secondary entrances shall have access controls equivalent to the main entrance for the corresponding zone.
- Fire doors and emergency exits shall be alarmed and monitored. Emergency exits shall open outward (per fire regulations) but shall not be openable from outside without authorisation.
- Roof access doors and service hatches shall be locked and alarmed.

### Authentication by Zone

| Security Zone | Minimum Authentication | Additional Requirements |
|---------------|----------------------|------------------------|
| **Controlled Zone** | Badge/card access (RFID, mobile credential) | — |
| **Restricted Zone** | Badge + PIN | Access logged with identity and timestamp |
| **High-Security Zone** | Badge + PIN + biometric, OR dual-person control | Access logged; CCTV at entry; after-hours access generates alert |

**Access control system requirements**:

- The access control system shall log all access events (granted and denied) with identity, timestamp, and entry point.
- Access rights shall be role-based and granted on a need-to-know/need-to-access basis.
- Access rights shall be reviewed quarterly (at minimum); Restricted and High-Security Zone access shall be re-confirmed by the authorising manager.

**Quarterly access review process**:

1. **Access report generation**: Facilities Manager generates access rights report from [Access Control System] showing all personnel with zone access, grouped by zone and department (due: 1st business day of review month).
2. **Manager attestation**: Line managers receive their team's access list; confirm each person's zone access is still required; identify access to remove (due: 14 days after report distribution).
3. **Revocation execution**: Facilities Manager revokes unnecessary access within 5 business days of manager attestation.
4. **Audit trail**: Attestation records (email confirmations, signed forms, or [GRC Tool] workflow records) retained for 3 years.

**Non-response handling**: Managers who do not respond within 14 days receive escalation to department head. Access for non-attested users in Restricted/High-Security Zones suspended pending attestation.

- Terminated employee physical access shall be revoked the same day as employment termination, coordinated with HR.
- Lost, stolen, or damaged badges shall be reported immediately and deactivated per the following timeline:

| Badge Type | Deactivation Timeline | Additional Actions |
|------------|----------------------|-------------------|
| **High-Security Zone badge** | **Immediate** (within 30 minutes of report) | CISO notification; access log review for 72 hours prior; reissue with new credential number |
| **Restricted Zone badge** | Within 2 hours | Access log review if suspicious circumstances |
| **Controlled Zone badge** | Within 4 hours | Standard replacement process |

**After-hours lost badge**: On-call facilities contact notified immediately for Restricted/High-Security badges; deactivation executed remotely.

- Badge sharing and lending shall be prohibited.
- Temporary access cards shall be time-limited and automatically expire.

### Employee Access

- Employee access shall be based on the principle of least privilege, providing access only to the zones required for the employee's role.
- Access control tokens (badges, cards, mobile credentials) shall be issued to each employee and shall identify the individual. Badges shall be worn visibly at all times while on premises (lanyard, clip, or badge holder). Covered or concealed badges may be challenged by security personnel.

**Badge requirements**:
- Employee badges shall include: photo, name, employee ID, zone access indicator (colour-coded or text).
- Visitor badges shall be clearly distinguishable from employee badges (distinct colour, "VISITOR" marking, no encoded zone access).
- Contractor badges shall be distinguishable and include expiry date.
- Temporary badges (replacement for lost permanent badge) shall be marked "TEMPORARY" and expire automatically after 7 days.
- Access control tokens shall not be shared, transferred, or loaned to other personnel.
- Access shall be revoked immediately upon employment termination; all physical access tokens shall be disabled and returned. HR shall notify Facilities of all terminations on or before the last working day.
- Role changes shall be assessed for physical access implications; access to zones no longer required for the new role shall be revoked within 5 business days.

**Access log retention**: Physical access control system logs shall be retained for at least 12 months (or longer where required by applicable regulation or contract), protected against unauthorised modification, and available within 2 business days for audit and incident response purposes.

### Visitor Management

**Visitor registration**:

- All visitors shall sign in at reception before proceeding beyond the Public Zone. Registration shall be recorded in [Visitor Management System] (or paper visitor log) and include: visitor name, company/organisation, host (employee being visited), date and time of arrival, and purpose of visit.
- Visitors shall present valid photographic identification.
- Visitor badges shall be clearly distinguishable from employee badges (distinct colour, marked "VISITOR", no zone access encoded).
- Visitors shall return badges at departure and sign out. Unreturned badges shall be deactivated by end of business day.

**Escort and supervision**:

- Visitors in Controlled Zones may move unescorted only if the host has confirmed the visit and the visitor badge restricts further zone access.
- Visitors in Restricted Zones shall be escorted at all times by an authorised employee.
- Visitors in High-Security Zones shall be escorted at all times by an authorised employee with explicit zone access, and the visit shall be pre-approved by the zone owner.
- Visitor access to High-Security Zones shall be pre-authorised in writing (email or [Visitor Management System] approval) before arrival.

**Visitor log retention**:

- Visitor logs shall be retained for a minimum of 12 months and protected against unauthorised modification.
- Logs shall be available within 2 business days for audit or incident investigation.

**Contractor and maintenance access**:

- Contractors and maintenance personnel shall be pre-authorised before arrival, with the scope of work and areas of access documented.
- Contractor access shall be time-limited and logged.
- Contractors accessing Restricted or High-Security Zones shall be escorted and their work supervised where sensitive systems or data are accessible.
- External maintenance on security systems (alarms, access control, CCTV) shall be performed under direct supervision by an authorised employee.

### Delivery and Loading Areas

- Access to delivery and loading areas from outside the building shall be restricted to identified and authorised delivery personnel.
- Delivery and loading areas shall be designed (or operationally managed) so that delivery personnel cannot gain access to other parts of the building.
- External doors of a delivery and loading area shall be secured when the internal doors to operational areas are opened; both shall not be open simultaneously where avoidable.
- Incoming materials shall be inspected for evidence of tampering before being moved from the delivery area.
- Incoming materials shall be registered in accordance with asset management procedures upon entry to the site.
- Incoming and outgoing shipments shall be physically segregated where feasible.
- Incoming materials shall be inspected for hazardous substances where the risk assessment warrants it (context-dependent: chemical, biological, or explosive risks).

---

## Securing Offices, Rooms and Facilities (A.7.3)

**ISO/IEC 27001:2022 Annex A.7.3 — Securing Offices, Rooms and Facilities**:

> *Physical security for offices, rooms and facilities should be designed and implemented.*

### General Office Security

- Offices shall be locked when unoccupied outside business hours.
- The clean desk policy shall be enforced — sensitive documents secured in locked storage when not in active use.
- Screens shall be positioned to prevent shoulder surfing by visitors or passers-by.
- Storage facilities (cabinets, safes, locked drawers) shall be provided for securing classified documents and portable media.
- Critical facilities should be sited to avoid access by the public and should give minimum indication of their purpose, with no obvious external signage identifying the presence of information processing activities.
- Facilities should be configured to prevent confidential information or activities from being visible or audible from the outside.

### Sensitive Areas

Areas processing Confidential or Restricted information (e.g., HR, finance, legal, executive offices) shall have:

- Access controls appropriate to the zone classification (Restricted Zone minimum).
- Access logs maintained and reviewed.
- Windows into sensitive areas frosted, covered, or fitted with privacy film to prevent visual observation.
- Recording devices (cameras, phones with cameras) restricted or prohibited unless explicitly authorised.

### Server Rooms and Datacenters

**For [Organisation]-controlled server rooms and datacenters**:

**Access control**:

- Access shall be limited to authorised IT personnel only, with named access lists maintained.
- Multi-factor authentication shall be required (badge + PIN + biometric, or dual-person control).
- All access shall be logged with identity and timestamp.
- Visitors and contractors in server rooms shall be escorted at all times.

**Physical construction**:

- No external windows.
- Reinforced walls, floors, and ceilings.
- Full-height partitions (floor slab to ceiling slab, not suspended ceiling).
- Environmental monitoring (fire suppression, water detection, temperature and humidity sensors).
- CCTV coverage with recording (retention per ISMS-OP-POL-A.7.4-5-11).

**Access logging and monitoring** (server rooms and datacentres):
- All access logged with identity, timestamp, entry/exit time.
- Access logs reviewed **weekly** by IT Security Manager.
- Anomalies investigated (after-hours access, unusual access patterns, unexpected visitors).
- Access log retention: **3 years** (longer than standard 12 months due to critical asset protection).
- Real-time alerts for: unscheduled after-hours access, repeated failed authentication attempts, door held open >2 minutes.
- **Physical access–change correlation**: When server/infrastructure changes occur, physical access logs reviewed to verify authorised personnel performed the work.

**For third-party datacenters and colocation**:

- Equivalent protections shall be assured through supplier assurance (ISO 27001 certificate, SOC 2 Type II report) and contractual security requirements.
- Where exact equivalence is not feasible, documented risk treatment with compensating controls shall be recorded.

### Meeting Room Security

- Meeting rooms shall be checked for recording devices or materials left behind before sensitive discussions.
- Whiteboards and flip charts shall be erased or removed after meetings.
- Documents shall not be left in meeting rooms after meetings conclude.
- Video conferencing equipment shall be secured when not in use; cameras and microphones shall be in a known-off state between meetings.

### Network Access Points and Cabling

- Physical access to networking equipment (switches, routers, wireless access points, patch panels) shall be restricted to authorised IT personnel.
- Network jacks and ports in Public Zones shall be disabled or shall not provide access to the internal network.
- Network jacks and ports in Controlled Zones that provide access to the internal network shall be secured by physical access controls to the zone.
- Visitors shall not connect devices to internal network ports unless explicitly authorised and escorted.
- Power and telecommunications cabling carrying data shall be protected from interception, interference, and damage.
- Power cables shall be segregated from communications cables to prevent interference.
- Access to cable rooms and patch panels shall be restricted by physical access control (Restricted Zone minimum).
- Where underground cabling entry to the building is feasible, power and telecommunication lines into information processing facilities should be routed underground.

### Secure Areas — Additional Requirements

In addition to the zone-based controls above, the following requirements apply to all designated secure areas (Restricted and High-Security Zones):

- Access rights to secure areas shall default to deny — access is granted only upon explicit authorisation.
- Photographic, video, audio, or other recording equipment (including cameras in mobile devices) shall not be permitted in secure areas unless specifically authorised by the zone owner.
- Personnel working in secure areas shall be informed of the specific security requirements and restrictions applicable to that area.
- Unsupervised working in High-Security Zones should be avoided both for safety reasons and to prevent opportunities for malicious activities.

### Training and Awareness

**Annual physical security awareness training** for all personnel covering:
- Badge usage (wear visibly, do not share, report lost immediately)
- Challenging unrecognised persons (polite inquiry: "May I help you?" or "Do you have an escort?")
- Tailgating prevention (do not hold doors, one person per badge tap)
- Clean desk policy (lock documents when leaving desk)
- Physical security incident reporting (what to report, how to report, to whom)
- Visitor escort responsibilities

**Role-specific training**:
- **Reception/Security**: Visitor management procedures, badge issuance/deactivation, emergency procedures.
- **Facilities**: Access control system operation, zone management, contractor escort requirements.
- **IT**: Network access point security, server room access procedures, equipment room security.

**New hire training**: Physical security training within **5 business days** of start date, before zone access granted.

Training completion tracked; target **95% completion** annually.

### Physical Security Walkthroughs

Compliance with office, meeting room, and facility security requirements shall be verified through documented physical security walkthroughs:

- **Frequency**: At least quarterly, and after any material security incident or facility change.
- **Scope**: All security zones, entry points, sensitive areas, server rooms, cable rooms, and meeting rooms.
- **Findings**: Documented as nonconformities or improvement actions with assigned owner, due date, and tracked to closure.
- **Checklist**: A standardised walkthrough checklist shall be maintained and used for all inspections.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|------------------|
| **Executive Management** | Approve policy; allocate budget for physical security infrastructure; receive reports on physical security posture |
| **CISO** | Policy ownership; define physical security standards; oversee compliance; approve exceptions; review physical security metrics |
| **Facilities Manager** | Implement and maintain physical security controls; manage access control systems; coordinate building security; manage contractors and maintenance |
| **IT Security** | Integrate physical and logical access controls; manage network access point security; review server room access; support incident response |
| **Reception / Security Personnel** | Operate visitor management; monitor entry points; respond to alarms and alerts; challenge unrecognised persons |
| **Line Managers** | Authorise physical access for team members; review and confirm access rights quarterly; report leavers and role changes for access revocation |
| **HR** | Notify Facilities of new hires, role changes, and terminations for access provisioning/revocation; manage contractor onboarding |
| **All Personnel** | Follow access procedures; wear badges visibly; challenge or report unrecognised persons; report lost badges and physical security events; comply with clean desk requirements |

**Escalation paths**:

### Physical Security Incident Reporting

All personnel shall immediately report physical security events to Reception, Facilities Manager, or Security Personnel. Reportable events include:

**Critical (immediate escalation to CISO)**:
- Unauthorised person discovered in Restricted or High-Security Zone
- Evidence of physical intrusion (forced doors, broken windows, tampered locks)
- Theft or suspected theft of equipment or documents
- Physical threats or confrontations on premises
- Badge cloning or tampering discovered

**High priority**:
- Successful tailgating into secured zone
- Unescorted visitor in Controlled Zone
- Propped-open security door (deliberate bypass)
- Lost badge with High-Security or Restricted Zone access

**Standard priority**:
- Lost badge with Controlled Zone only access
- Visitor without badge beyond reception
- Facility deficiency (broken lock, malfunctioning door sensor)
- Clean desk policy violation

**Reporting channels**: Reception (during hours), Facilities Manager, [emergency number] (after hours), CISO (for critical events).

**Escalation paths**:

- **Physical security incidents**: Employee/Security Personnel --> Facilities Manager --> CISO --> Executive Management
- **Access requests**: Employee --> Line Manager (approval) --> Facilities Manager (provisioning)
- **Visitor issues**: Reception --> Facilities Manager --> CISO
- **Lost/stolen badges**: Employee --> Reception/Facilities (immediate deactivation) --> IT Security (if system access implications)
- **Contractor non-compliance**: Escort/Supervisor --> Facilities Manager --> Procurement/Contract Owner

---

## Evidence for This Policy

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | **Security zone documentation and floor plans** showing zone boundaries, entry points, and access control mechanisms | Facilities Manager | Updated on facility change; reviewed annually | Current + previous version |
| 2 | **Access control system configuration** — zone assignments, authentication levels, role-based access rules | Facilities Manager / IT | Reviewed quarterly | Current configuration + change log |
| 3 | **Access control logs** — entry/exit events with identity, timestamp, entry point (granted and denied) | [Access Control System] | Continuous; reviewed monthly for anomalies | 12 months minimum |
| 4 | **Visitor logs** — registration records with name, company, host, date/time in/out, identification verified | Reception / [Visitor Management System] | Continuous | 12 months minimum |
| 5 | **Access rights review records** — quarterly review of personnel access rights with manager sign-off | Facilities Manager / Line Managers | Quarterly | 3 years |
| 6 | **Perimeter inspection reports** — documented findings from building and zone perimeter inspections | Facilities Manager | Annual (building); quarterly (Restricted/High-Security) | 3 years |
| 7 | **Physical security walkthrough reports** — checklist results, findings, and remediation tracking | Facilities Manager / CISO | Quarterly | 3 years |
| 8 | **Badge management records** — issuance, replacement, deactivation, lost/stolen reports | Facilities Manager | Per event; audited annually | Duration of employment + 1 year |
| 9 | **Contractor and maintenance access records** — pre-authorisation, scope, escort records | Facilities Manager | Per engagement | 3 years |
| 10 | **Supplier assurance records** for colocation/shared facilities — certificates, SOC reports, contract terms | CISO / Procurement | Reviewed annually | Duration of contract + 2 years |
| 11 | **Exception register** — approved exceptions with justification, compensating controls, expiry date | CISO | Updated per exception; reviewed quarterly | 3 years after exception closure |
| 12 | **Physical security incident reports** — unauthorised access attempts, badge losses, tailgating events, perimeter breaches | CISO / Facilities Manager | Per incident | 3 years |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to: access control system reports, visitor log audits, physical security walkthrough results, access rights review completion rates, badge management metrics, supplier assurance reviews, internal and external audits, and feedback to the policy owner.

**Key metrics**:

| Metric | Target | Review Frequency |
|--------|--------|------------------|
| Access control coverage (% of entry points with active controls) | 100% | Quarterly |
| Access rights reviews completed on time | 100% | Quarterly |
| Visitor escort compliance (Restricted/High-Security Zones) | 100% | Monthly |
| Terminated employee access revoked same day | 100% | Per event; audited monthly |
| Badge loss/theft incidents | < 5 per quarter | Quarterly |
| Unauthorised access attempts (successful) | 0 | Monthly |
| Physical security walkthrough completion | 100% on schedule | Quarterly |
| Supplier assurance reviews current | 100% | Annually |

**Reporting**:
- **Monthly dashboard** to CISO: Access revocation compliance, badge loss incidents, unauthorised access attempts, visitor escort compliance.
- **Quarterly report** to Executive Management: All metrics, trend analysis, walkthrough findings, exception status.
- **Annual report** to Management Review: Physical security programme effectiveness, capital investment recommendations, regulatory compliance status.

Metrics breaching targets shall be escalated to CISO immediately and include remediation plan with owner and target date.

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO in advance, with documented business justification, risk assessment, compensating controls, and a defined expiry date (maximum 6 months, renewable with re-assessment). Exceptions shall be reported to the Management Review Team.

**Permitted exceptions** (with appropriate compensating controls):

- Temporary emergency access for urgent repairs (with enhanced monitoring and escort).
- Extended visitor access for auditors or regulatory inspectors (with documented approval and scope).
- Alternative authentication methods for personnel with accessibility requirements.

**Not permissible** as exceptions:

- Permanent bypass of zone authentication requirements.
- Exceptions without compensating controls.
- Exceptions to same-day access revocation for terminated employees.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Specific non-compliance scenarios and responses:

- **Tailgating or allowing tailgating**: Formal warning; repeated offence triggers disciplinary process.
- **Badge sharing or lending**: Immediate badge deactivation; disciplinary process.
- **Failure to challenge or report unrecognised persons**: Addressed through awareness training.
- **Propping open secured doors**: Immediate remediation; formal warning if deliberate.

Contractors found in non-compliance may have their access revoked and the contracting organisation notified.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider:

- Facility changes (office moves, renovations, new sites, lease changes).
- Physical security incidents and near-misses (unauthorised access, tailgating, perimeter breaches).
- Audit findings and walkthrough results.
- Advances in access control technology (mobile credentials, touchless biometrics, AI-enhanced anomaly detection).
- Regulatory changes (particularly nFADP, cantonal data protection requirements, and EU GDPR updates).
- Changes to the threat landscape (e.g., increased social engineering targeting physical access).
- Lessons learned from physical security events at the organisation or reported in the industry.

Improvement actions shall be tracked, assigned an owner, and reported to the CISO and Management Review Team.

---

# Areas of the ISO 27001 Standard Addressed

Physical Access Control Policy — ISO 27001:2022 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.1 Actions to address risks and opportunities | 5.36 Compliance with policies, rules, and standards |
| Clause 6.2 Information security objectives | 6.3 Information security awareness, education, and training |
| Clause 7.3 Awareness | 6.4 Disciplinary process |
| Clause 8.1 Operational planning and control | **7.1 Physical security perimeters** |
| Clause 9.1 Monitoring, measurement, analysis, evaluation | **7.2 Physical entry** |
| Clause 10.2 Nonconformity and corrective action | **7.3 Securing offices, rooms and facilities** |
| | 7.4 Physical security monitoring |
| | 7.6 Working in secure areas |
| | 7.8 Equipment siting and protection |

---

# Regulatory Framework

| Framework | Applicability | Relevance to Physical Access Control |
|-----------|---------------|--------------------------------------|
| **Swiss nFADP (revDSG)** | **Mandatory** — all personal data processing | Art. 8 — Technical and organisational measures appropriate to risk; physical security of premises where personal data is processed or stored |
| **Swiss DSV (Data Protection Ordinance)** | **Mandatory** — supplements nFADP | Art. 1-3 — Minimum requirements for data security, including physical access controls |
| **ISO/IEC 27001:2022** | **Mandatory** — certification scope | Annex A Controls 7.1, 7.2, 7.3 |
| **ISO/IEC 27002:2022** | **Guidance** | Sections 7.1, 7.2, 7.3 — Implementation guidance for physical controls |
| **EU GDPR** | **Conditional** — where processing EU/EEA personal data | Art. 32 — Security of processing, including physical security measures |
| **PCI DSS v4.0** | **Conditional** — where processing payment card data | Requirement 9 — Restrict physical access to cardholder data; requires badge-controlled access, visitor logs, media destruction procedures |
| **FINMA Circular 2023/1** | **Conditional** — Swiss regulated financial institutions | Operational risk management including physical security of critical infrastructure |
| **NIST SP 800-53 Rev 5** | **Guidance** | PE family — Physical and Environmental Protection controls |
| **CIS Controls v8** | **Guidance** | Control 3 (Data Protection), Control 6 (Access Control Management) — physical access dimensions |

---

<!-- QA_VERIFIED: 2026-02-07 -->
