**ISMS-OP-POL-A.7.12-13 — Cabling Security and Equipment Maintenance**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Cabling Security and Equipment Maintenance |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.7.12-13 |
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

- ISO/IEC 27001:2022 Controls A.7.12, A.7.13 — Cabling security, Equipment maintenance
- ISO/IEC 27002:2022 Sections 7.12, 7.13 — Implementation guidance
- NIST SP 800-53 Rev 5 PE-4 (Access Control for Transmission), PE-9 (Power Equipment and Cabling), MA-2 (Controlled Maintenance), MA-5 (Maintenance Personnel)
- IEC 11801 / EN 50173 / TIA-568 — Structured cabling standards
- Swiss NIN (Niederspannungs-Installationsnorm) — Low-voltage installation standards

**Related Annex A Controls**:

| Control | Relationship to Cabling Security and Equipment Maintenance |
|---------|-----------------------------------------------------------|
| A.5.9 Inventory of information and other associated assets | Asset inventory drives maintenance programme completeness |
| A.5.24–28 Incident management lifecycle | Infrastructure failures escalate to incident management |
| A.5.30 ICT readiness for business continuity | Equipment availability supports business continuity objectives |
| A.7.1–3 Physical security perimeters and entry | Access control to cable rooms and wiring closets |
| A.7.4 Physical security monitoring | Monitoring of infrastructure areas where cabling is routed |
| A.7.5 Protecting against physical and environmental threats | Environmental protection for cabling and equipment |
| A.7.8–9 Equipment siting and protection | Equipment placement considers cable routing and maintenance access |
| A.7.14 Secure disposal or re-use of equipment | Disposal procedures apply when equipment is retired after maintenance end-of-life |
| A.8.6 Capacity management | Capacity planning informs maintenance scheduling and cable infrastructure sizing |
| A.8.32 Change management | Infrastructure and cabling changes follow change management process |

**Related Internal Policies**:

- Physical Access Control Policy
- Physical Infrastructure Security Policy
- Equipment Siting and Protection Policy
- Asset Management Policy
- Change Management Policy
- Incident Management Policy
- Business Continuity and Disaster Recovery Policy

---

# Cabling Security and Equipment Maintenance Policy

## Purpose

The purpose of this policy is to protect the physical infrastructure that carries and processes information — specifically power and data cabling and the equipment connected to it. Cabling forms the nervous system of the organisation's information processing environment. Unprotected cables are vulnerable to interception, electromagnetic interference, and physical damage. Improperly maintained equipment degrades, fails, and creates security exposures. This policy establishes requirements for both.

Controls A.7.12 (Cabling Security) and A.7.13 (Equipment Maintenance) are combined because they address complementary aspects of infrastructure protection: cabling provides the connectivity foundation, and maintenance ensures ongoing reliability. They share common facilities, personnel, and assessment processes.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect the availability, integrity, and confidentiality of personal data through physical infrastructure controls. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 requirements for security of processing including physical measures also apply.

## Scope

All employees, contractors, and third-party maintenance personnel with access to cabling infrastructure or equipment requiring maintenance.

This includes:

- **Cabling**: Power cables, network cables (copper and fibre optic), telecommunications cables, structured cabling systems, patch panels, distribution frames, cable trays, conduits, and pathways.
- **Equipment**: Servers, network devices (switches, routers, firewalls), storage systems, UPS units, PDUs, HVAC systems supporting information processing, physical security systems (access control, CCTV), and telecommunications equipment.
- **Facilities**: Datacentres, server rooms, wiring closets, telecommunications rooms, cable risers, and underground cable routes.
- **Activities**: Cable installation, cable inspection, equipment servicing, preventive maintenance, corrective maintenance, remote maintenance, and equipment removal for repair.

**Out of scope**:

- Physical access control to infrastructure areas (covered by A.7.1–3).
- Environmental monitoring and protection systems (covered by A.7.4–5-11).
- Equipment disposal and secure destruction (covered by A.7.14 and A.7.10).
- Cloud-hosted infrastructure maintained entirely by the cloud provider (covered through supplier management, A.5.19–23). Where the organisation operates cloud-only with no on-premises equipment, Controls A.7.12 and A.7.13 may be marked "Not Applicable" in the Statement of Applicability with documented justification.

## Principle

Cabling carrying power or data should be protected from interception, interference, and damage. Equipment should be maintained correctly to ensure availability, integrity, and confidentiality of information. Protection and maintenance levels shall be proportionate to the criticality of the assets served, determined through risk assessment and the organisation's asset classification.

---

## Cable Protection Standards (A.7.12)

> *Cables carrying power, data or supporting information services should be protected from interception, interference and damage.*

### Physical Cable Protection

All cables carrying power, data, or supporting information services shall be physically protected:

- Cables shall be routed through protected pathways — conduits, cable trays, raised floors, or ceiling voids — not exposed across open areas.
- Underground cabling shall be protected against accidental damage using armoured conduits or duct systems. Route markers shall identify buried cable paths.
- Cables shall be protected from environmental hazards including water ingress, heat sources, chemical exposure, and physical impact. Cable routes shall avoid areas with high risk of damage.
- Where cables traverse between buildings, suitable protection shall be applied (armoured cable, sealed duct, or direct-buried conduit).
- Wiring closets, telecommunications rooms, and cable distribution frames shall be physically secured. These areas shall be locked when unoccupied and access restricted to authorised personnel.
- Manhole and duct access points shall be secured and access logged.

### Electromagnetic Protection

- Cables shall be protected from electromagnetic interference (EMI) through appropriate shielding, separation from interference sources, and selection of cable type suited to the environment.
- In environments with high electromagnetic interference (e.g., near heavy electrical equipment, industrial machinery, or radio transmission), shielded cable (STP/FTP) or fibre optic cable shall be used.
- Cable installations shall comply with the organisation's adopted structured cabling standard (IEC 11801 / EN 50173 / TIA-568 as applicable) for shielding and separation requirements.

---

## Cable Segregation

### Power and Data Separation

Power cables and communications cables shall be segregated to prevent electromagnetic interference:

- Minimum separation distances shall follow the structured cabling standard adopted by the organisation. As a baseline: minimum 200 mm separation between unshielded data cables and power cables running in parallel. Where crossing is unavoidable, cables shall cross at right angles.
- Power and data cables shall use separate conduits, cable trays, or pathways. Shared pathways are not permitted for unshielded data cables and power cables.
- Separation requirements shall be documented in the organisation's cabling standard and applied consistently across all installations.

### Network Classification Separation

- Cables carrying traffic of different security classifications shall be physically separated where feasible, or clearly identified using colour coding or labelling to prevent cross-connection.
- High-security network cables (e.g., management networks, financial systems, security systems) shall be identifiable through consistent colour coding or labelling convention defined by the organisation.

---

## Cable Documentation and Labelling

### Documentation Requirements

Cable infrastructure shall be documented and maintained:

- A cable register or cable management database shall record all structured cabling installations, including cable type, endpoints, route, installation date, and classification.
- As-built cabling diagrams shall be maintained for all facilities. Diagrams shall show cable routes, patch panel locations, distribution frames, and interconnections.
- Cable documentation shall be kept current. All cabling changes shall be reflected in documentation within 5 business days of completion.
- Cable documentation shall be secured and access-controlled. Only authorised personnel shall have access to detailed cabling diagrams (these reveal network topology and physical routes).

### Labelling Standards

- All cables shall be labelled at both ends with a unique identifier that maps to the cable register.
- Patch panels, distribution frames, and telecommunications outlets shall be clearly labelled.
- Labels shall be durable, legible, and enable identification without requiring reference to detailed documentation for routine operations.
- The organisation shall define and document a consistent labelling convention (e.g., building-floor-room-rack-port).

### Cabling Change Control

- All cabling installations, modifications, and removals shall follow the organisation's change management process (A.8.32).
- Unused cables shall be disconnected, documented, and either removed or clearly marked as inactive.
- Quarterly physical walkthroughs shall be conducted to identify unauthorised additions, modifications, or damage. Findings shall be reconciled against as-built diagrams and change records, with results documented and signed off by the Facilities Manager.

---

## Fibre Optic Requirements

Fibre optic cable shall be used in preference to copper for data transmission in the following circumstances:

- **High-security areas**: Server rooms, datacentres, and secure zones where interception risk is elevated. Fibre optic cable does not emit electromagnetic radiation and is significantly more difficult to tap without detection than copper cable.
- **Long-distance runs**: Between buildings, between floors (risers), and any horizontal runs exceeding 90 metres (copper Category 6A distance limit).
- **High-bandwidth requirements**: Where bandwidth demands exceed copper capabilities (e.g., 40 Gbps and above).
- **EMI-sensitive environments**: Areas with high electromagnetic interference where copper cable performance would be degraded.

Where fibre optic is deployed, fusion splicing shall be used for permanent connections (not mechanical splicing) in secure areas. Fibre patch panels shall be housed in locked enclosures.

Where copper cable is used in areas with interception risk, shielded cable (STP/FTP) shall be specified and cable routes shall be physically secured.

---

## Inspection and Cable Maintenance

Regular inspection and maintenance of cabling infrastructure shall be performed:

- Cable infrastructure shall be included in the organisation's maintenance programme with defined inspection intervals.
- Visual inspections shall be conducted quarterly for accessible cable routes, checking for damage, unauthorised modifications, labelling integrity, and pathway obstructions.
- Formal cable testing (continuity, performance) shall be conducted annually or following any reported issues.
- Damaged cables shall be repaired or replaced promptly. Temporary repairs shall be documented and permanent repair scheduled within 30 calendar days.
- Inspection findings shall be documented and retained for a minimum of 3 years.

---

## Maintenance Programme (A.7.13)

> *Equipment should be maintained correctly to ensure availability, integrity and confidentiality of information.*

### Programme Establishment

The organisation shall establish and maintain a maintenance programme covering all equipment that processes, stores, or supports the processing of information:

- All in-scope equipment recorded in the asset inventory (per A.5.9) shall be included in the maintenance programme. The asset inventory is the authoritative source for programme completeness.
- Quarterly reconciliation shall verify that all inventoried equipment has maintenance coverage. Reconciliation results and sign-off shall be retained as evidence.
- Maintenance schedules shall follow manufacturer recommendations as minimums. Deviations require documented risk acceptance via the exception register.
- The maintenance programme shall be managed through [CMMS] or equivalent maintenance tracking system. Where a dedicated CMMS is not deployed, a controlled spreadsheet or register shall be used.

### Maintenance Schedule

The following minimum preventive maintenance frequencies apply:

| Equipment Category | Preventive Maintenance Frequency | Activities |
|-------------------|----------------------------------|------------|
| **Servers** | Annually | Firmware updates, cleaning, physical inspection, component health checks |
| **Network equipment** (switches, routers, firewalls) | Semi-annually | Firmware updates, fan cleaning, port inspection, log review |
| **UPS systems** | Quarterly battery checks; annual full capacity test | Battery condition, load testing, transfer testing, connection integrity |
| **PDUs** | Annually | Connection inspection, load balancing review, thermal imaging |
| **HVAC/Cooling** (serving IT areas) | Quarterly | Filter replacement, refrigerant checks, performance verification |
| **Fire detection and suppression** | Per cantonal fire regulations (minimum annually) | Detector testing, system inspection, suppression agent verification |
| **Physical security systems** (access control, CCTV) | Semi-annually | Camera health, reader testing, controller firmware, recording verification |
| **Structured cabling** | Annually (visual inspection quarterly) | Cable testing, pathway inspection, labelling verification |

Maintenance schedules shall be adjusted based on equipment age, environmental conditions, manufacturer advisories, and incident history. Equipment approaching end-of-life shall have maintenance frequency increased or be scheduled for replacement.

---

## Maintenance Personnel Authorisation

### Internal Personnel

- Only personnel with documented authorisation shall perform maintenance on information processing equipment.
- Maintenance authorisation shall specify which equipment categories and which maintenance activities the individual is qualified to perform.
- Authorisation records shall be maintained and reviewed annually.

### Third-Party Maintenance Personnel

- Third-party maintenance shall be performed only by contracted and approved providers. Maintenance contracts shall include confidentiality obligations and security requirements.
- Third-party maintenance personnel shall be identified and verified (government-issued identification) before being granted access to equipment.
- The organisation shall maintain a register of approved third-party maintenance providers, reviewed annually.

### Supervision Requirements

- Third-party maintenance personnel shall be supervised when accessing equipment that processes or stores sensitive or confidential information, unless a documented risk assessment concludes that unsupervised access is acceptable (e.g., dedicated maintenance contract with background-checked personnel, isolated equipment).
- Unsupervised third-party maintenance access shall be logged with individual identification, time in/out, and equipment accessed.
- Supervision records shall be maintained as evidence.

---

## Security During Maintenance

### Data Protection During Maintenance

- Sensitive data shall be protected during all maintenance activities. Maintenance personnel shall not have access to data stored on equipment unless specifically required and authorised.
- Equipment containing data shall not be removed from premises for maintenance where on-site repair is feasible.
- If off-site maintenance is required, data shall be securely erased from the equipment before removal (per A.7.14 secure disposal procedures), or the storage media shall be removed and retained by the organisation.
- For equipment where data erasure is not feasible before removal (e.g., fault prevents access), a documented risk assessment shall be completed and the maintenance provider's data handling obligations confirmed in writing.

### Physical Verification After Maintenance

- After maintenance, equipment shall be physically inspected before being returned to service to verify that no unauthorised modifications have been made.
- All tools and equipment brought on-site by maintenance personnel shall be accounted for before and after maintenance.
- Firmware and software versions shall be verified after maintenance to confirm no unauthorised changes.

### Maintenance Access Controls

- Maintenance access shall be time-limited. Access windows shall be agreed in advance and documented.
- All maintenance access shall be logged: who performed the work, when, what equipment was accessed, and what work was performed.
- Maintenance personnel shall be issued temporary access credentials (badges, system access) that expire at the end of the maintenance window.

---

## Remote Maintenance

Remote maintenance introduces additional risk. The following controls shall apply:

- Remote maintenance shall be explicitly authorised before each session. Standing authorisation for remote access is not permitted.
- Remote maintenance sessions shall use encrypted connections (VPN, SSH, or equivalent secure protocol). Unencrypted remote access is not permitted.
- Remote maintenance sessions shall be logged, including session start/end times, individual identity, and actions performed. Session recording is recommended for critical equipment.
- Remote access shall be disabled when not actively in use. Persistent remote access connections for maintenance purposes shall not remain open.
- Remote maintenance of equipment containing sensitive data shall require the same authorisation as physical access to that equipment.
- Where the maintenance provider requires remote access to internal systems, a dedicated jump host or bastion server with multi-factor authentication shall be used.

---

## Equipment Removal and Return

When equipment must be removed from premises for off-site maintenance:

1. **Authorisation**: Removal shall be authorised in writing by the equipment owner or designated delegate.
2. **Data protection**: Data shall be securely erased before removal. If erasure is not possible, storage media shall be removed and retained by the organisation. The data protection approach shall be documented.
3. **Chain of custody**: A chain of custody record shall be created documenting: equipment identification, condition at removal, removal date/time, authorised by, carrier/transporter, destination, expected return date.
4. **Equipment return inspection**: Upon return, the equipment shall be inspected for tampering, unauthorised modifications, and correct configuration. Firmware and software versions shall be verified.
5. **Asset register update**: Equipment return shall be logged in [Asset Management System] with maintenance summary and inspection results.

---

## Maintenance Records

### Documentation Requirements

All maintenance — preventive and corrective — shall be documented:

- **Preventive maintenance**: Date, equipment identifier, maintenance activities performed, findings, parts replaced, next scheduled maintenance date, personnel who performed the work.
- **Corrective maintenance**: Date, equipment identifier, fault description, root cause (where determined), repair actions taken, parts replaced, post-repair verification results, personnel who performed the work.
- **Remote maintenance**: Session date/time, equipment accessed, individual identity, actions performed, session duration.

### Record Retention

- Maintenance records shall be retained for a minimum of 3 years or the lifecycle of the equipment, whichever is longer.
- Records shall be available for audit at all times.
- Records shall be stored in [CMMS] or equivalent controlled register.

### Maintenance Trend Analysis

- Maintenance records shall be reviewed quarterly for trends: recurring faults, equipment approaching end-of-life, increasing failure frequency, or maintenance SLA breaches.
- Trend analysis shall inform equipment replacement planning and maintenance programme adjustments.
- Quarterly trend reports shall be provided to the IT Operations Manager and CISO.

---

## Definitions

| Term | Definition |
|------|------------|
| **Structured Cabling** | A standardised cabling infrastructure (copper and fibre optic) following industry standards (IEC 11801, EN 50173, TIA-568) that provides a flexible, reliable framework for voice, data, and video communications |
| **Cabling Infrastructure** | All power and communications cables, conduits, pathways, patch panels, distribution frames, and termination points |
| **Fibre Optic Cable** | A cable containing one or more optical fibres that transmit data as light pulses, offering higher bandwidth, longer distance, EMI immunity, and greater resistance to interception than copper cable |
| **Preventive Maintenance** | Scheduled maintenance performed at defined intervals to prevent equipment failure and maintain performance within specifications |
| **Corrective Maintenance** | Unplanned maintenance performed to restore equipment to operational condition following a fault or failure |
| **Remote Maintenance** | Maintenance performed via remote network access without physical presence at the equipment location |
| **Chain of Custody** | A documented chronological record of the transfer of responsibility for equipment, tracking possession from removal through maintenance to return |
| **CMMS** | Computerised Maintenance Management System — software used to schedule, track, and document maintenance activities |
| **EMI** | Electromagnetic Interference — unwanted electrical noise from external sources that can degrade signal quality in data cables |

---

## Roles and Responsibilities

| Role | Cabling and Maintenance Responsibilities |
|------|------------------------------------------|
| **Executive Management** | Approve policy; allocate budget for infrastructure maintenance and cable plant upgrades |
| **CISO** | Policy ownership; security standards for maintenance activities; risk acceptance for exceptions; quarterly reporting on infrastructure compliance |
| **IT Operations Manager** | Equipment maintenance programme ownership; maintenance vendor management; maintenance schedule oversight; trend analysis review |
| **Facilities Manager** | Cabling infrastructure ownership; cable plant maintenance and inspection; building services coordination; physical pathway management |
| **System Owners** | Ensure owned equipment is included in maintenance programme; authorise equipment removal; define data protection requirements for maintenance |
| **IT Operations** | Day-to-day maintenance execution and coordination; maintenance record keeping; remote maintenance session management |
| **Internal Audit** | Annual verification of maintenance programme compliance; cable infrastructure audit; evidence review |
| **All Employees** | Report suspected cable damage, equipment faults, or unauthorised infrastructure changes promptly |

### Escalation Path

- Cable damage or unauthorised changes discovered: Reporting individual notifies Facilities Manager. Facilities Manager assesses impact and notifies CISO if security-relevant.
- Equipment maintenance failures: IT Operations notifies IT Operations Manager. Critical equipment failures escalate to CISO.
- Security concerns during maintenance: Any staff member notifies CISO directly.

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Cable register / cable management database** documenting all structured cabling with type, endpoints, route, and classification | Facilities Manager | *Maintained continuously; reviewed annually* |
| 2 | **As-built cabling diagrams** for all facilities, current and version-controlled | Facilities Manager | *Updated within 5 business days of changes; reviewed annually* |
| 3 | **Quarterly cable walkthrough reports** with findings, reconciliation against diagrams, and sign-off | Facilities Manager | *Quarterly; retained 3 years* |
| 4 | **Cable testing records** (continuity, performance) for new installations and annual verification | Facilities Manager | *Annually and per installation; retained 3 years* |
| 5 | **Maintenance programme** showing all in-scope equipment with schedules aligned to manufacturer recommendations | IT Operations Manager | *Reviewed quarterly; retained 3 years* |
| 6 | **Quarterly reconciliation** of asset inventory against maintenance programme coverage | IT Operations Manager | *Quarterly; retained 3 years* |
| 7 | **Preventive maintenance records** documenting completed maintenance with findings and next scheduled date | IT Operations | *Per maintenance event; retained 3 years minimum* |
| 8 | **Corrective maintenance records** documenting faults, root cause, repair actions, and post-repair verification | IT Operations | *Per event; retained 3 years minimum* |
| 9 | **Maintenance personnel authorisation records** (internal and third-party) | IT Operations Manager | *Reviewed annually; retained 3 years* |
| 10 | **Third-party maintenance provider register** with contract details and annual review | IT Operations Manager | *Reviewed annually; retained active + 2 years* |
| 11 | **Remote maintenance session logs** with individual identification, times, and actions | IT Operations | *Per session; retained 3 years* |
| 12 | **Equipment removal and return records** with chain of custody, data protection evidence, and return inspection | IT Operations | *Per event; retained 3 years* |
| 13 | **Maintenance trend analysis reports** identifying recurring issues and equipment lifecycle recommendations | IT Operations Manager | *Quarterly; retained 3 years* |
| 14 | **Exception register** for approved deviations from maintenance schedules or cabling standards | CISO | *Per event; reviewed quarterly; retained active + 2 years* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, cable infrastructure audits, maintenance programme reviews, maintenance record audits, physical inspections, vendor compliance assessments, internal and external audits, and feedback to the policy owner.

The following metrics shall be tracked and reported to the CISO quarterly:

| Metric | Target | Red Threshold |
|--------|--------|---------------|
| Preventive maintenance completed on schedule | 100% | < 85% |
| Equipment failures attributable to missed or inadequate maintenance | 0 | Any occurrence |
| Cable documentation accuracy (walkthrough findings vs. diagrams) | > 95% | < 85% |
| Unauthorised cabling changes detected | 0 | Any occurrence |
| Maintenance-related security incidents | 0 | Any occurrence |
| Asset inventory to maintenance programme reconciliation | 100% coverage | < 90% coverage |
| Third-party maintenance personnel properly authorised and supervised | 100% | < 95% |

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO in advance, with documented risk assessment, compensating controls, and a defined review date (maximum 6 months, renewable). Valid exception scenarios include:

- Deferred maintenance for critical systems where maintenance window cannot be scheduled without unacceptable business impact (with compensating monitoring).
- Extended maintenance intervals for low-criticality equipment (with documented justification and manufacturer consultation where applicable).
- Copper cable use in locations where fibre optic is specified but installation is not feasible (with shielding and physical protection compensating controls).
- Third-party maintenance without full supervision (with enhanced logging and post-maintenance inspection).

Exceptions shall be recorded in the Exception Register and reported to the Management Review Team.

**Not permissible**:

- Skipping security-critical maintenance (UPS, fire systems, security systems) without compensating controls.
- Undocumented cabling changes.
- Unsupervised and unlogged third-party maintenance on equipment containing sensitive data.
- Permanent exceptions to maintenance programme coverage.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Cabling changes made without authorisation or documentation shall be treated as a security incident and investigated accordingly. Equipment maintenance bypassed without approval shall be reported to the CISO for risk assessment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to facility operations, infrastructure technology, cabling standards, manufacturer maintenance recommendations, equipment lifecycle status, regulatory requirements, audit findings, incident trends, and lessons learned from equipment failures. Nonconformities related to this policy shall be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Areas of the ISO 27001 Standard Addressed

Cabling Security and Equipment Maintenance Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.9 Inventory of information and other associated assets |
| Clause 6.1 Actions to address risks and opportunities | 5.30 ICT readiness for business continuity |
| Clause 7.3 Awareness | 7.4 Physical security monitoring |
| Clause 8.1 Operational planning and control | 7.5 Protecting against physical and environmental threats |
| Clause 9.1 Monitoring, measurement, analysis and evaluation | 7.8 Equipment siting and protection |
| Clause 10.2 Nonconformity and corrective action | **7.12 Cabling security** |
| | **7.13 Equipment maintenance** |
| | 7.14 Secure disposal or re-use of equipment |
| | 8.32 Change management |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures for physical security of data processing infrastructure |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security including physical measures |
| Swiss NIN (Niederspannungs-Installationsnorm) | Low-voltage electrical installation standards applicable to power cabling in buildings |
| Swiss Federal Ordinance on Low-Voltage Installations (SR 734.27) | Prerequisites and inspection requirements for electrical installations |
| EU GDPR (where applicable) | Art. 32 — Security of processing including physical infrastructure measures |
| ISO/IEC 27001:2022 | Annex A Controls 7.12 (Cabling Security), 7.13 (Equipment Maintenance) |
| ISO/IEC 27002:2022 | Sections 7.12, 7.13 — Implementation guidance for cabling security and equipment maintenance |
| IEC 11801 / EN 50173 | International and European structured cabling standards for generic cabling in customer premises |
| TIA-568 / TIA-942 | North American structured cabling and datacentre cabling standards |
| NIST SP 800-53 Rev 5 | PE-4 (Access Control for Transmission), PE-9 (Power Equipment and Cabling), MA-2 (Controlled Maintenance), MA-5 (Maintenance Personnel) |
| CIS Controls v8 | Control 1 (Inventory and Control of Enterprise Assets), Control 12 (Network Infrastructure Management) |
| **Conditional**: FINMA Circular 2023/1 | Swiss regulated financial institution — enhanced infrastructure resilience requirements |
| **Conditional**: DORA (EU) 2022/2554 | EU financial services entity — ICT operational resilience for infrastructure |
| **Conditional**: NIS2 (EU) 2022/2555 | Essential/important entity in EU — infrastructure protection requirements |

---

<!-- QA_VERIFIED: 2026-02-07 -->
