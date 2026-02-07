**ISMS-OP-POL-A.5.30-8.13-14 — Business Continuity and Disaster Recovery**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Business Continuity and Disaster Recovery |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.30-8.13-14 |
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

- ISO/IEC 27001:2022 Control A.5.30 — ICT readiness for business continuity
- ISO/IEC 27001:2022 Control A.8.13 — Information backup
- ISO/IEC 27001:2022 Control A.8.14 — Redundancy of information processing facilities
- ISO/IEC 22301 — Business continuity management systems (informational reference)
- NIST SP 800-34 Rev 1 — Contingency Planning Guide for Federal Information Systems (informational reference)

**Related Annex A Controls**:

| Control | Relationship to Business Continuity and Disaster Recovery |
|---------|----------------------------------------------------------|
| A.5.9 Inventory of information and other associated assets | Asset inventory drives BIA and backup scope identification |
| A.5.19–23 Supplier relationships and cloud services | Supplier BC/DR commitments and shared responsibility model |
| A.5.24–28 Incident management lifecycle | Major incidents may trigger BC/DR plan activation |
| A.5.29 Information security during disruption | Security continuity during BC/DR events |
| A.8.6 Capacity management | Capacity planning supports redundancy and DR infrastructure |
| A.8.9 Configuration management | Configuration baselines required for system rebuild and recovery |
| A.8.15 Logging | Backup and recovery operations shall be logged |
| A.8.16 Monitoring activities | Backup monitoring and redundancy health checks |

**Related Internal Policies**:

- Asset Management Policy
- Incident Management Policy
- Cloud Services and Supplier Security Policy
- Logging and Monitoring Policy
- Change Management Policy

---

# Business Continuity and Disaster Recovery Policy

## Purpose

The purpose of this policy is to ensure the organisation can continue or recover its critical business operations and information processing facilities following a disruptive incident. It establishes requirements for business impact analysis, information backup, system redundancy, and ICT continuity planning.

This policy addresses three related ISO 27001:2022 controls as a unified framework because they operate as an integrated BC/DR ecosystem: backup provides data recovery capability (A.8.13), redundancy provides system availability capability (A.8.14), and ICT readiness provides overall preparedness and governance (A.5.30). Each control maintains distinct requirements for Statement of Applicability purposes.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect the availability and integrity of personal data and information processing systems. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32(1)(c) requirements for the ability to restore the availability and access to personal data in a timely manner also apply.

## Scope

All employees and third-party users.

All information systems, applications, infrastructure, and services deemed in scope by the ISO 27001 scope statement, including:

- Servers, databases, and code repositories
- Cloud infrastructure and SaaS applications
- Network infrastructure and security systems
- Business-critical applications and data
- System configurations and infrastructure-as-code

**Out of scope for backup** (unless specifically risk-assessed):

- Desktop and laptop local storage (data shall reside on backed-up servers, cloud services, or repositories; local-only data is at risk of permanent loss and is not protected by this policy)
- Mobile device local storage

**Out of scope for this policy**:

- Non-ICT business continuity (organisational BCM framework)
- Physical records and non-digital information (covered under physical security controls)

## Principle

**People's safety shall be our first priority. Always.**

Business continuity management and information security continuity shall address threats, risks, and incidents that impact the continuity of operations. The framework is based on industry best practice and aligns with ISO 22301 Business Continuity Management.

The organisation shall:

- Conduct business impact analysis to identify critical systems and determine recovery requirements.
- Maintain backup copies of information, software, and systems, tested regularly to confirm recoverability.
- Implement redundancy for critical information processing facilities to meet availability requirements.
- Plan, implement, maintain, and test ICT continuity based on business continuity objectives.

**Critical Principle — "Untested Recovery = No Recovery"**: Backup success without restore testing, redundancy without failover testing, and BC plans without scenario testing provide false confidence. Evidence-based verification through systematic testing is required.

---

## Business Impact Analysis and System Criticality

### Business Impact Analysis

Business continuity shall be based on a documented business impact analysis (BIA) and risk assessment. The BIA shall:

- Identify critical business processes and their ICT dependencies.
- Quantify the impact of ICT disruptions (financial, operational, reputational, regulatory).
- Establish Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO) for each critical system.
- Identify interdependencies between systems.

**BIA frequency**: The BIA shall be conducted initially during ISMS implementation, reviewed annually, and updated upon significant business changes (new services, acquisitions, major system changes) or after major incidents.

### System Criticality Tiers

Systems shall be classified into criticality tiers based on BIA results. These tiers drive backup frequency, redundancy requirements, and testing schedules:

| Tier | Classification | Maximum RPO | Maximum RTO | Examples |
|------|---------------|-------------|-------------|----------|
| **Tier 1** | Critical | 1 hour | 4 hours | Core business application, primary database, authentication system |
| **Tier 2** | High | 6 hours | 24 hours | Email, collaboration platform, secondary business applications |
| **Tier 3** | Medium | 24 hours | 72 hours | Internal tools, development environments, reporting systems |
| **Tier 4** | Low | 7 days | > 72 hours | Archives, non-critical internal services |

System owners, in consultation with the BC/DR Coordinator, shall determine the appropriate tier for each system based on the BIA results.

**Role assignment**: Where the organisation does not have a dedicated BC/DR Coordinator, the IT Operations Manager shall assume BC/DR coordination responsibilities. This assignment shall be formally documented in the role description.

### RPO and RTO

**Recovery Point Objective (RPO)** defines the maximum acceptable data loss measured in time. RPO drives backup frequency. Example: An RPO of 6 hours means up to 6 hours of data loss is acceptable, so backups must occur at least every 6 hours.

**Recovery Time Objective (RTO)** defines the maximum acceptable time to restore a system after disruption. RTO drives redundancy and recovery strategy. Example: An RTO of 4 hours means the system must be operational within 4 hours of failure.

Systems unable to meet their defined RPO or RTO shall follow the exception management process (see Policy Compliance — Exceptions).

---

## Information Backup

### Backup Scope

The following categories of information shall be backed up:

| Category | Backup Requirement |
|----------|-------------------|
| Critical business data (customer, financial, operational) | Mandatory |
| Production system data and configurations | Mandatory |
| Application software and dependencies | Mandatory |
| Security configurations and access control data | Mandatory |
| Important business data | Mandatory |
| Development/test environments | Risk-based (backup if recreation cost exceeds backup cost) |
| Ephemeral data (caches, temporary logs) | Not required |

### Backup Schedule and Retention

A backup schedule, retention schedule, and testing schedule shall be maintained and made available. Backup frequency shall align with the RPO for each system tier:

| System Tier | Backup Frequency | Minimum Retention |
|-------------|-----------------|-------------------|
| **Tier 1 (Critical)** | Continuous replication or hourly | Daily: 30 days; Weekly: 90 days; Monthly: 12 months |
| **Tier 2 (High)** | Every 4–6 hours | Daily: 30 days; Weekly: 90 days; Monthly: 12 months |
| **Tier 3 (Medium)** | Daily | Daily: 7 days; Weekly: 28 days; Monthly: 12 months |
| **Tier 4 (Low)** | Weekly or on-change | Weekly: 28 days; Monthly: 12 months |

**Extended retention**: Longer retention periods may be required by regulation (e.g., financial records 7–10 years), legal hold requests, or contractual obligations. Extended retention shall be justified (regulatory requirement, legal hold, or contractual obligation) to prevent unnecessary data accumulation. Shorter retention periods require CISO approval with documented risk acceptance.

### Backup Types

The organisation shall select appropriate backup strategies based on system requirements:

| Backup Type | Description | Use Case |
|-------------|-------------|----------|
| **Full** | Complete copy of all data | Baseline backup; weekly or monthly |
| **Incremental** | Changed data since last backup (any type) | Daily backups; fast, storage-efficient |
| **Differential** | Changed data since last full backup | Daily backups; faster recovery than incremental |
| **Snapshot** | Point-in-time copy at storage level | Frequent backups; VMs and cloud workloads |
| **Continuous Data Protection** | Real-time or near-real-time replication | Tier 1 systems requiring RPO < 1 hour |

### 3-2-1 Backup Rule

The organisation shall implement the 3-2-1 backup rule as a minimum for Tier 1 and Tier 2 systems:

| Element | Requirement |
|---------|------------|
| **3 copies** | Original data plus at least 2 backup copies |
| **2 media types** | Different storage technologies (e.g., disk + cloud, disk + tape) |
| **1 offsite copy** | Geographically separated location (different building, region, or cloud region) |

**Immutable backups**: For Tier 1 and Tier 2 systems, at least one backup copy shall be immutable (write-once-read-many) or air-gapped to protect against ransomware and accidental deletion. Technologies include object storage with object lock (e.g., AWS S3 Object Lock, Azure Immutable Blob Storage, or equivalent), WORM tape, or air-gapped offline media.

**Conditional**: Organisations subject to DORA (EU financial entities) shall implement immutable backup copies where technically feasible (Art. 12(4)) and offsite backup storage at sufficient geographic distance.

### Backup Security

- Backups shall be encrypted both in transit and at rest using AES-256 or equivalent, per the Use of Cryptography Policy (A.8.24). The backup solution (e.g., Veeam, Commvault, AWS Backup, Azure Backup, or equivalent) shall support built-in encryption.
- Backups stored in cloud-based solutions shall as a minimum be hosted with an ISO 27001 certified provider.
- Where backup is to physical media:
  - The media shall be encrypted.
  - The media shall be labelled and stored securely with restricted, authorisation-required access control.
  - Offsite transfer shall use an approved secure courier or encrypted electronic transfer.
- Backups shall be protected to at least the same security level as the original data.
- **Backup encryption key management**: Encryption keys shall be managed separately from backup data. Key recovery procedures shall be documented and tested (keys must be accessible when primary systems are unavailable). Keys shall be rotated annually or upon suspected compromise. Key escrow or split-key custody is recommended for critical system backups. Key management shall comply with the Use of Cryptography Policy (A.8.24).

### Backup Portability

To avoid vendor lock-in, backup implementations should ensure:

- Backups are exportable to industry-standard formats where feasible.
- Cloud backups are restorable to alternative environments (different cloud provider or on-premises).
- Recovery procedures address provider exit scenarios.

### Backup Monitoring

Backup operations shall be monitored:

| Element | Requirement |
|---------|------------|
| Backup success/failure | Real-time monitoring; immediate alert on failure for Tier 1–2 systems |
| Backup duration | Alert if duration exceeds backup window |
| Storage capacity | Warning at 70% utilisation; alert at 80%; critical at 90% |
| Offsite replication | Alert on replication failure |

Backup logs shall be produced and checked for errors and performance at least weekly. Where errors are found, corrective action shall be taken and recorded.

Monthly backup status reports shall be provided to the CISO, including backup coverage, success rates, and outstanding issues.

### Backup Testing and Verification

Backups shall be regularly tested to ensure they can be relied upon in an emergency and meet the needs of the business continuity plans:

| System Tier | Restore Test Frequency | Test Scope |
|-------------|----------------------|-----------|
| **Tier 1 (Critical)** | Quarterly | Full system restore to alternate environment |
| **Tier 2 (High)** | Semi-annually | Representative data sets; full system annually |
| **Tier 3 (Medium)** | Annually | Sample restore verification |
| **Tier 4 (Low)** | Upon significant change | Sample restore or documented risk acceptance |

Each restore test shall document: test date, systems tested, backup source, expected vs. actual recovery time, data integrity verification, issues encountered, and sign-off by the test owner.

**Failed test response**: Restore tests revealing recovery failures shall trigger escalation based on system tier:

| Tier | Notification | Remediation Plan | Status Updates | Escalation |
|------|-------------|-----------------|----------------|------------|
| **Tier 1** | Executive notification within 4 hours | Within 24 hours | Daily | Reported at next Management Review; recurring failures (same system twice in 12 months) trigger architectural review |
| **Tier 2** | CISO notification within 24 hours | Within 5 business days | Weekly | Reported at next Management Review |
| **Tier 3–4** | Risk register update within 10 business days | Next maintenance window | Monthly | Quarterly review |

Retest shall occur within 30 days of remediation for Tier 1–2 systems.

**Conditional**: Organisations subject to DORA shall test backup recovery at least annually (Art. 12(6)).

### Recovery Procedures

Backup and restoration procedures shall be documented, maintained, and kept accessible (including when primary systems are unavailable). Recovery procedures for each critical system shall include:

- Step-by-step restore process.
- Required access credentials and authorisation.
- Recovery time estimate vs. RTO target (include a 25% buffer for unforeseen complications).
- Validation steps to confirm successful recovery.
- Escalation contacts.

### Cloud Backup Responsibilities

For cloud-hosted systems, the organisation shall:

- Understand the provider's shared responsibility model (what the provider backs up vs. what the customer must back up).
- Implement customer-managed backups where provider capabilities do not meet RPO requirements.
- Test SaaS data export and restoration procedures.
- Document cloud-to-on-premises recovery procedures for extended cloud outage scenarios.

### Cloud Provider SLA Alignment

- Cloud provider SLA guarantees shall be verified against organisational RTO requirements for each system tier.
- Provider historical uptime and incident response performance shall be documented during vendor assessment (per A.5.19–23).
- Where provider SLA is insufficient for Tier 1 or Tier 2 systems, customer-managed redundancy shall be implemented.
- Provider BC/DR capabilities (multi-AZ, backup/restore, failover) shall be documented.
- Cloud provider BC/DR commitments shall be included in the vendor risk assessment.
- Providers should maintain ISO 22301 certification or equivalent where available.

---

## Redundancy of Information Processing Facilities

### Redundancy Requirements by Tier

Information processing facilities shall be implemented with redundancy sufficient to meet availability requirements:

| System Tier | Minimum Redundancy | Failover Type | Target RTO |
|-------------|-------------------|---------------|-----------|
| **Tier 1 (Critical)** | Active-active or active-passive with automated failover | Automatic | Minutes |
| **Tier 2 (High)** | Warm standby or documented manual failover | Manual with runbook | Hours |
| **Tier 3 (Medium)** | Cold standby or rebuild from backup | Rebuild | Days |
| **Tier 4 (Low)** | Backup-based recovery | Restore | Per RTO |

**Redundancy architecture options**:

- **Active-active**: Multiple systems serving traffic simultaneously; failure handled by remaining systems.
- **Active-passive**: Primary system serves traffic; standby system ready for immediate activation on failure.
- **Warm standby**: Standby environment partially provisioned; requires data synchronisation before becoming operational.
- **Cold standby**: Infrastructure available but not provisioned; requires provisioning and data restoration.

### Single Point of Failure (SPOF) Analysis

System owners shall conduct SPOF analysis for Tier 1 and Tier 2 systems to identify components whose failure would cause complete system unavailability. Common SPOFs include:

- Single server with no clustering or failover.
- Single network path with no redundant connectivity.
- Single storage controller, power supply, or UPS.
- Single cloud availability zone or data centre.
- Single DNS or authentication server.

**SPOF remediation**: Identified SPOFs for Tier 1 systems shall be remediated within 90 days or have documented risk acceptance from the CISO. Tier 2 system SPOFs shall be remediated within 180 days or have documented risk acceptance.

### Failover Testing

Systems with redundancy shall have their failover mechanisms tested:

| System Tier | Failover Test Frequency |
|-------------|------------------------|
| **Tier 1 (Critical)** | Quarterly (full failover in production or production-like environment) |
| **Tier 2 (High)** | Semi-annually (documented failover test or tabletop exercise) |
| **Tier 3 (Medium)** | Annually (tabletop exercise or procedure validation) |

Each failover test shall document: systems tested, failover trigger mechanism, actual failover time vs. RTO target, issues identified, and sign-off.

**Failback testing**: Failover tests shall also validate the failback process (returning to primary infrastructure after recovery). Failback procedures shall be documented and tested alongside failover to ensure full recovery cycle capability.

**Failed failover response**: Tests revealing inability to meet RTO shall trigger immediate remediation and risk assessment per the escalation table in Backup Testing and Verification.

### Geographic and Network Redundancy

**Geographic redundancy**: For Tier 1 systems, redundancy shall be implemented at sufficient geographic distance to protect against site-wide disasters:

| Distance Tier | Separation | Protection Against |
|---------------|-----------|-------------------|
| **Minimum** | Different building or campus | Localised incidents (fire, flood, power) |
| **Recommended** | Different city or region (>100 km) | Regional disasters |
| **Best practice** | Different geographic or seismic zone | Large-scale natural disasters |

Cloud-specific guidance: Multi-AZ deployment (tens of kilometres separation) meets the minimum tier. Multi-region deployment (hundreds to thousands of kilometres) meets the recommended tier.

**Network redundancy**: Critical systems should implement network redundancy including dual ISPs or providers, redundant switches/routers, and redundant firewalls where the organisation's infrastructure supports it.

**Cost-benefit analysis**: Redundancy decisions shall balance the cost of redundant infrastructure against the business impact of extended outages and regulatory requirements. For many SMEs, cloud-native redundancy (multi-AZ deployment) provides cost-effective geographic redundancy without maintaining separate physical infrastructure.

**Conditional**: Organisations subject to DORA or NIS2 should implement geographic redundancy for critical systems to meet operational resilience requirements.

---

## ICT Continuity Planning

### Business Continuity Plans

The organisation shall maintain documented procedures for responding to a disruptive incident and for continuing or recovering its activities within predetermined timeframes. Business continuity plans shall address the requirements of those who will use them.

**Business continuity plans shall cover**:

- Roles and responsibilities for people and teams with authority during and following an incident.
- A process for activating the response.
- Details to manage the immediate consequences of a disruptive incident, giving due regard to the welfare of individuals.
- Strategic, tactical, and operational options for responding to disruption.
- Prevention of further loss or unavailability of prioritised activities.
- How and under what circumstances the organisation will communicate with employees and their relatives, key interested parties, and emergency contacts.
- How the organisation will continue or recover its prioritised activities within predetermined timeframes.
- Details of the organisation's media response following an incident, including a communications strategy, preferred interface with the media, and guidelines for drafting media statements.
- A process for standing down once the incident is over.

**Each plan shall define**: purpose and scope, objectives, activation criteria and procedures, implementation procedures, roles and authorities, communication requirements, internal and external interdependencies, resource requirements, and information flow and documentation processes.

### ICT Recovery Plans

For each Tier 1 and Tier 2 system, the organisation shall maintain ICT recovery plans documenting:

1. **Activation criteria** — When to activate the plan (disaster declaration process).
2. **Recovery team** — Roles, responsibilities, and escalation procedures.
3. **Emergency contacts** — Recovery team, vendors, stakeholders.
4. **Recovery procedures** — Step-by-step system recovery instructions in priority sequence.
5. **Communication procedures** — Internal and external communication templates.
6. **Recovery priorities** — System recovery sequence based on dependencies and tier classification.
7. **Validation procedures** — How to verify systems are operational after recovery.
8. **Rollback procedures** — Actions if recovery fails.

Recovery plans shall be version-controlled, reviewed annually, and updated after testing exercises, major incidents, or significant system changes.

### Disaster Declaration Process

A disaster shall be declared when:

- A Tier 1 system outage exceeds 50% of its defined RTO.
- Multiple systems fail simultaneously.
- Extended infrastructure outage (data centre, cloud region, network) is confirmed.
- A cyber incident (ransomware, data breach) prevents normal operations.
- Physical site loss or inaccessibility occurs.

**Declaration authority hierarchy**: On-call engineer assesses → escalates to IT Operations Manager → CISO evaluates within 30 minutes → CEO/Executive Management authorises declaration if required → BC/DR plans activated and recovery teams notified.

**Activation notification**: Pre-approved notification templates shall be maintained in the BC/DR plan. Notification shall be issued via primary channel (email, collaboration platform) and backup channel (SMS, phone) simultaneously.

**Incident-to-disaster escalation**: Not every incident is a disaster. The Incident Management Policy (A.5.24–28) governs initial incident response. Escalation to disaster declaration occurs when incident response determines that normal recovery within RTO is not achievable.

### BC/DR Testing Programme

Business continuity plans and technical recovery plans shall be tested at least annually and when significant change occurs.

**Testing types**:

| Test Type | Description | Frequency |
|-----------|-------------|-----------|
| **Tabletop exercise** | Discussion-based walkthrough of a scenario with key personnel | Annually (all critical processes) |
| **Component test** | Test individual system recovery (backup restore, failover) | Quarterly for Tier 1; semi-annually for Tier 2 |
| **Full DR test** | Complete failover to DR site or alternate environment | Annually for Tier 1 systems |

**Annual integrated test**: At least one annual BC/DR test should exercise backup restoration, redundancy activation, business process validation, and communication procedures together to verify end-to-end recovery capability.

**Test documentation**: Each test shall document: test date, scope, objectives, participants, scenario, results (success/partial/failure), actual vs. target RTO/RPO, issues identified, lessons learned, action items, and sign-off.

**Failed test response**: Tests revealing inability to meet RTO/RPO shall trigger immediate investigation, gap remediation plan, interim compensating controls, and executive notification for Tier 1 systems.

**Conditional**: Organisations subject to DORA shall test BC arrangements at least annually (Art. 11(9)) and test ICT backup and restoration at least annually (Art. 12(6)).

### BC/DR Training and Awareness

| Audience | Training Content | Frequency |
|----------|-----------------|-----------|
| **All employees** | BC/DR awareness (individual responsibilities, reporting procedures, communication channels, basic concepts) | Annually |
| **Recovery team members** | Role-specific training (recovery procedures, communication protocols, tool usage) | Annually; new members trained within 30 days of assignment |
| **Executive Management** | Crisis decision-making, disaster declaration process, media handling | Annually (tabletop exercise) |

Post-test training: BC/DR test results and lessons learned shall be communicated to all participants within 30 days of each test.

**Training targets**: 100% of recovery team trained; 95% of all employees completed BC/DR awareness.

### Crisis Communication

BC/DR plans shall include communication procedures for:

**Internal communication**:

- Activation notification within 30 minutes of disaster declaration (who is notified, through what channels).
- Status updates during recovery at defined intervals (hourly for Tier 1, every 4 hours for Tier 2).
- All-clear notification when recovery is complete and systems validated.

**External communication**:

- Customer notification (proactive for known outages affecting service).
- Supplier/partner coordination (if needed for recovery).
- Regulatory notification (if required — e.g., data breach notification per nFADP Art. 24 or GDPR Art. 33).

**Communication channels**: Primary channels (email, [Collaboration Platform]); backup channels (SMS, phone) if primary channels are unavailable. Contact lists shall be maintained, accessible offline (printed or on mobile devices), and reviewed quarterly.

### Recovery Procedures

The organisation shall maintain documented procedures to restore and return business activities from temporary measures adopted during an incident to normal business operations.

**Recovery validation checklist**: Before declaring a system recovered and returning to normal operations, the following shall be verified:

- Data integrity confirmed (checksums, record counts, application-level validation).
- All dependent systems and integrations operational.
- User access restored and tested.
- Security controls re-enabled and verified (EDR, firewall rules, logging).
- Performance within acceptable parameters.
- Sign-off from system owner.

### Ransomware Recovery

Given the prevalence of ransomware threats, the following specific recovery considerations supplement the general BC/DR framework:

**Immediate actions upon ransomware detection**:

1. Isolate infected systems from the network (do not power off — preserve forensic evidence).
2. Activate incident response team per the Incident Management Policy (A.5.24–28).
3. Assess backup integrity — verify that backup copies are not compromised before initiating restoration.

**Recovery considerations**:

- Rebuild from known-clean backups verified as pre-dating the infection.
- Patch the exploited vulnerability before restoring systems to production.
- Reset all credentials (user, service account, administrative) before restoring access.
- Implement extended monitoring for 30–90 days post-recovery to detect persistence mechanisms.

**Immutable backup importance**: WORM storage, object lock, or air-gapped media ensures at least one recovery point is immune to ransomware encryption.

**Ransom payment**: The organisation shall not make ransom payments without explicit Executive Management approval and prior consultation with legal counsel and cyber insurance provider (if applicable).

### Incident and Business Continuity Reporting

An incident management process shall be in place and followed. Business continuity incidents shall additionally be:

- Recorded and tracked in a register.
- Reported to the Management Review Team.
- Subject to post-incident review to capture lessons learned.

---

## Roles and Responsibilities

| Role | BC/DR Responsibilities |
|------|----------------------|
| **CEO / Executive Management** | Ultimate accountability for business continuity; approve BC/DR strategy and budget; declare disasters requiring plan activation |
| **CISO** | BC/DR policy owner; approve requirements and risk acceptances; ensure adequate resources; report BC/DR status to executive management quarterly |
| **BC/DR Coordinator** | Day-to-day BC/DR programme management; coordinate BIA process; maintain recovery plans; schedule and facilitate testing; track compliance with backup and redundancy requirements; manage BC/DR training programme; assess change impact on BC/DR plans |
| **System Administrators / Cloud Administrators** | Implement and manage backup solutions; configure redundancy and failover mechanisms; monitor backup jobs; participate in BC/DR testing; maintain recovery documentation |
| **System Owners / Application Owners** | Define RTO/RPO requirements; provide input to BIA; approve system recovery priorities; validate recovered systems; participate in BC/DR testing |
| **All Employees** | Report business continuity incidents; follow BC plans during disruptions; participate in BC/DR awareness training |

---

## BC/DR Metrics and Reporting

The following metrics shall be tracked to measure BC/DR programme effectiveness:

| # | Metric | Target | Monitoring | Reporting |
|---|--------|--------|-----------|-----------|
| 1 | **Backup success rate** | ≥99% Tier 1; ≥98% Tier 2–3 | Daily | Monthly to CISO |
| 2 | **Restore test completion** | 100% per schedule | Per test | Quarterly |
| 3 | **RTO/RPO test results** | 100% Tier 1 within target; ≥95% Tier 2 | Per test | Quarterly trend |
| 4 | **Failover test completion** | 100% per schedule | Per test | Quarterly |
| 5 | **BC/DR plan currency** | 100% reviewed within annual cycle | Quarterly | Quarterly |
| 6 | **SPOF remediation** | ≥90% remediated or risk-accepted within timeline | Quarterly | Quarterly |
| 7 | **Recovery team training** | 100% trained | Annually | Annually |

Metrics breaching targets for two consecutive reporting periods shall be escalated to the CISO and reported at the next Management Review.

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Business Impact Analysis** with system criticality tiers, RPO/RTO, and dependency mapping | BC/DR Coordinator / CISO | *Annual review; updated upon significant changes; retained 5 years* |
| 2 | **Backup inventory** (systems backed up, backup type, frequency, retention, offsite status) | System Administrators | *Maintained continuously; reviewed quarterly; retained 3 years* |
| 3 | **Backup monitoring logs and reports** (success/failure rates, error resolution records) | System Administrators | *Weekly log checks; monthly reports to CISO; retained 12 months* |
| 4 | **Backup restore test results** (test date, systems, actual vs. target RTO/RPO, data integrity verification) | BC/DR Coordinator | *Per schedule (quarterly to annually by tier); retained 3 years* |
| 5 | **SPOF analysis** for Tier 1 and Tier 2 systems with remediation status | System Owners | *Annual review; updated upon infrastructure changes; retained 3 years* |
| 6 | **Failover test results** (failover time, issues, sign-off) | BC/DR Coordinator | *Per schedule (quarterly to annually by tier); retained 3 years* |
| 7 | **BC/DR plans** (business continuity plans and ICT recovery plans, current versions) | BC/DR Coordinator / CISO | *Annual review; updated after tests and incidents; retained current + 2 prior versions* |
| 8 | **BC/DR test records** (tabletop exercises, component tests, full DR tests with scenarios and results) | BC/DR Coordinator | *Annual minimum; retained 3 years* |
| 9 | **Exception register** (systems not meeting RPO/RTO, risk acceptances, compensating controls) | CISO | *Per event; reviewed quarterly; retained 5 years* |
| 10 | **Crisis communication contact lists** (internal team, external contacts, supplier contacts, available offline) | BC/DR Coordinator | *Reviewed quarterly; updated upon any change* |
| 11 | **BC/DR training records** (recovery team training completion, annual awareness completion rates) | BC/DR Coordinator | *Annually; retained 3 years* |
| 12 | **BC/DR metrics reports** (backup success rates, test completion, plan currency trends) | BC/DR Coordinator | *Monthly to CISO; quarterly trend reports; retained 3 years* |
| 13 | **Cloud provider SLA and BC/DR capability documentation** (SLA guarantees, shared responsibility model, BC/DR alignment verification) | System Owners / Cloud Administrators | *Reviewed annually and upon contract renewal; retained 3 years* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, backup monitoring reports, restore test records, BC/DR test results, SPOF analysis reports, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy (e.g., system excluded from backup, redundancy not implemented, RPO/RTO not met) shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date (maximum 12 months, renewable). Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to business operations, technology infrastructure, regulatory requirements, lessons learned from BC/DR tests and actual incidents, audit findings, emerging threats (e.g., ransomware, supply chain disruptions), environmental threat assessments, and capacity forecasting for backup and DR infrastructure.

The organisation is committed to the development and continual improvement of the business continuity process, plans, and system.

---

# Areas of the ISO 27001 Standard Addressed

Business Continuity and Disaster Recovery Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.29 Information security during disruption |
| Clause 7.3 Awareness | **5.30 ICT readiness for business continuity** |
| Clause 8.1 Operational planning and control | 5.36 Compliance with policies, rules, and standards |
| | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | **8.13 Information backup** |
| | **8.14 Redundancy of information processing facilities** |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures including availability protection and data recovery capability |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 32(1)(c) — Ability to restore availability and access to personal data in a timely manner |
| ISO/IEC 27001:2022 | Annex A Controls 5.30 (ICT Readiness), 8.13 (Information Backup), 8.14 (Redundancy) |
| ISO/IEC 27002:2022 | Sections 5.30, 8.13, 8.14 — Implementation guidance |
| ISO/IEC 22301 | Business continuity management systems (informational reference) |
| NIST SP 800-34 Rev 1 | Contingency Planning Guide (informational reference) |
| CIS Controls v8 | Control 11 (Data Recovery) |
| DORA (conditional) | Art. 11–12 — ICT business continuity, backup policies, disaster recovery plans, annual testing |
| NIS2 (conditional) | Art. 21 — Business continuity and crisis management, backup management |
| FINMA (conditional) | Business continuity management for Swiss financial institutions |

---

<!-- QA_VERIFIED: 2026-02-07 -->
