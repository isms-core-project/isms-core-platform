<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.16:operational:OP-POL:a.8.16 -->
**ISMS-OP-POL-A.8.16 — Monitoring Activities**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Monitoring Activities |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.16 |
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

- ISO/IEC 27001:2022 Control A.8.16 — Monitoring activities

**Related Annex A Controls**:

| Control | Relationship to Monitoring Activities |
|---------|---------------------------------------|
| A.5.7 Threat intelligence | Threat intelligence informs monitoring rules and detection patterns |
| A.5.24–28 Incident management | Monitoring triggers incident detection and escalation |
| A.5.28 Collection of evidence | Monitoring data serves as forensic evidence |
| A.5.34 Privacy and protection of PII | Employee monitoring must comply with privacy requirements |
| A.8.7 Protection against malware | Malware detection events feed monitoring |
| A.8.15 Logging | Logs provide the raw data that monitoring analyses |
| A.8.17 Clock synchronisation | Accurate timestamps are essential for event correlation |
| A.8.20 Network security | Network traffic is a primary monitoring data source |

**Related Internal Policies**:

- Logging Policy (A.8.15)
- Incident Management Policy
- Network Security Policy
- Endpoint Security Policy
- Access Control Policy
- Privacy and Protection of PII Policy

---

# Monitoring Activities Policy

## Purpose

The purpose of this policy is to define the requirements for actively monitoring networks, systems, and applications to detect anomalous behaviour, security threats, and policy violations. Where logging (A.8.15) captures and preserves events, monitoring analyses those events in real-time or near-real-time to identify and respond to threats before they cause harm.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing monitoring as a technical and organisational measure appropriate to risk. Monitoring activities shall comply with Swiss employment law (CO Art. 328/328b) and the prohibition on behaviour surveillance (ArGV3 Art. 26). Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 requirements also apply.

## Scope

This policy applies to:

- All networks, systems, applications, and cloud services within the ISMS scope.
- All monitoring technologies: SIEM, EDR/XDR, NDR, IDS/IPS, UEBA, and equivalent tools.
- All employees and third-party users whose activities generate security-relevant events.
- All environments: production, staging, and externally-facing systems.

Monitoring of physical security systems (CCTV, badge readers) is covered under the Physical Access Control Policy. Logging configuration and log retention are covered under the Logging Policy (A.8.15).

## Principle

Monitoring is an active, detective control. Networks, systems, and applications shall be monitored for anomalous behaviour, and appropriate actions taken to evaluate potential information security incidents. Monitoring shall operate on the basis of established behavioural baselines, defined detection rules, and threat intelligence — not indiscriminate surveillance.

---

## What to Monitor

### Monitoring Scope

The following shall be monitored for anomalous behaviour and security events:

| # | Monitoring Domain | What to Monitor |
|---|-------------------|-----------------|
| 1 | **Network traffic** | Inbound and outbound traffic flows, east-west (lateral) traffic between segments, connections to known malicious IPs/domains |
| 2 | **Authentication and access** | Failed logon attempts, impossible travel, credential stuffing patterns, access from unexpected locations or devices |
| 3 | **Privileged activity** | Administrative actions, privilege escalations, service account usage, after-hours privileged access |
| 4 | **Endpoint behaviour** | Process execution anomalies, unsigned binaries, script execution, persistence mechanisms, memory injection |
| 5 | **Application activity** | Unusual transaction volumes, bulk data operations, API abuse patterns, application error spikes |
| 6 | **Configuration changes** | Modifications to security settings, firewall rules, group policies, DNS records, certificate configurations |
| 7 | **Security tool status** | Antivirus/EDR disablement, firewall rule changes, logging service interruptions, IDS/IPS bypass attempts |
| 8 | **Cloud services** | Administrative console access, tenant configuration changes, excessive API calls, data export operations |
| 9 | **Data movement** | Large file transfers, bulk downloads, USB device usage, cloud storage uploads, email attachments exceeding thresholds |
| 10 | **Resource utilisation** | CPU/memory/disk/bandwidth anomalies that may indicate cryptomining, DDoS participation, or system compromise |

### Critical Systems Priority

Systems shall be prioritised for monitoring based on risk:

| Priority | System Type | Monitoring Level |
|----------|-------------|-----------------|
| **Critical** | Authentication infrastructure, firewalls, VPN, domain controllers, payment systems | Real-time with automated alerting |
| **High** | Servers hosting confidential/personal data, email gateways, cloud admin consoles | Real-time or near-real-time (within 15 minutes) |
| **Medium** | Internal application servers, development infrastructure, internal file shares | Near-real-time (within 1 hour) |
| **Standard** | Workstations, printers, non-critical infrastructure | Periodic review (daily or weekly aggregation) |

---

## Behavioural Baselines

### Establishing Baselines

Before anomaly detection is effective, the organisation shall establish baselines of normal behaviour. Initial baselines shall be established within 30 days of monitoring deployment for each system or system group. During the baseline establishment period, monitoring shall operate in "learning mode" — alerts shall be generated but reviewed with increased tolerance for false positives until baselines are validated.

Baselines shall document:

- System utilisation during standard and peak operating periods.
- Typical access patterns: timing, location, frequency, and volume by user group.
- Expected network traffic flows: source-destination pairs, protocols, data volumes.
- Standard application transaction rates and error levels.

Baselines shall be reviewed and updated:

- **Quarterly** for general systems.
- **After significant changes** (new systems, reorganisations, cloud migrations, seasonal business cycles).
- **Following incidents** where the incident revealed a gap in baseline definition.

### Deviation Detection

Monitoring systems shall be configured to detect deviations from established baselines, including:

- Traffic from or to known malicious sources (C2 servers, botnet infrastructure, threat-intelligence-flagged IPs/domains).
- Recognised attack signatures and patterns (brute force, DDoS, buffer overflow, SQL injection, credential stuffing).
- Unusual system behaviour: unexpected process terminations, unauthorised process execution, keystroke logging indicators, protocol deviations.
- User behaviour anomalies: access outside normal working hours, access to resources not previously accessed, impossible travel between geographic locations. **Impossible travel** is defined as authentication events from two geographic locations within a timeframe that makes physical travel between them implausible (e.g., logins from Zurich and Tokyo within 2 hours). The organisation shall define impossible travel parameters based on: maximum plausible travel speed, VPN/proxy exclusions for known corporate exit points, and tolerance for mobile device location inaccuracy.
- Network performance anomalies: unexpected latency, bandwidth saturation, unusual DNS query volumes.
- Resource consumption anomalies: CPU spikes, unexpected disk I/O, memory exhaustion without corresponding workload.

---

## Monitoring Architecture

### Monitoring Platform

The organisation shall deploy a centralised monitoring platform capable of:

| Capability | Requirement |
|------------|-------------|
| **Event correlation** | Correlate events from multiple sources (logs, network, endpoint, cloud, identity) into a unified view |
| **Automated alerting** | Generate alerts based on predefined rules, thresholds, and anomaly detection |
| **Threat intelligence integration** | Ingest external threat intelligence feeds to enrich detection rules and identify known indicators of compromise |
| **Dashboards** | Provide real-time visibility into security posture, alert volumes, and trends |
| **Investigation support** | Enable drill-down from alert to raw events for incident investigation |
| **Retention** | Retain monitoring data per the Logging Policy (A.8.15) retention schedule |

Platform examples: SIEM (e.g., Microsoft Sentinel, Splunk, Elastic SIEM, Wazuh), XDR, or equivalent.

### Detection Layers

A layered monitoring approach shall be implemented:

| Layer | Technology | Coverage |
|-------|-----------|----------|
| **Network** | NDR, IDS/IPS, firewall logs, DNS monitoring | North-south and east-west traffic visibility |
| **Endpoint** | EDR/XDR agents on all managed devices | Process execution, file operations, memory analysis |
| **Identity** | Identity provider monitoring, UEBA | Authentication anomalies, credential misuse, insider threat indicators |
| **Application** | Application logs forwarded to SIEM, WAF | Transaction anomalies, input validation failures, API abuse |
| **Cloud** | Cloud-native monitoring (e.g., AWS CloudTrail, Azure Monitor, GCP Cloud Audit Logs) | Administrative actions, configuration changes, data access |

Where the organisation lacks the resources for a full in-house Security Operations Centre (SOC), a Managed Detection and Response (MDR) service should be considered to provide 24/7 monitoring coverage.

### Cloud-Specific Monitoring

For cloud environments (IaaS, PaaS, SaaS), additional monitoring requirements apply:

- **Cloud audit logs** (AWS CloudTrail, Azure Activity Log, GCP Cloud Audit Logs) shall be forwarded to the centralised monitoring platform.
- **Cloud security posture** changes (e.g., public S3 bucket creation, security group modification, IAM policy changes) shall generate immediate alerts.
- **Cloud-native threat detection** services (AWS GuardDuty, Azure Defender, GCP Security Command Center) should be enabled and integrated with the centralised monitoring platform.
- **SaaS administrative actions** (M365 admin portal, Google Workspace admin, Salesforce setup changes) shall be monitored for unauthorised configuration changes.
- **Cloud API activity** shall be monitored for unusual volumes, access from unexpected locations, and use of deprecated or high-risk API endpoints.

### Monitoring System Health (SOC 2: CC4.1)

The monitoring infrastructure itself shall be monitored to ensure continuous availability:

- **Data ingestion**: Alert if log source ingestion stops or drops below baseline volume for more than 15 minutes.
- **Agent health**: Monitor EDR/monitoring agent status across all endpoints; alert on agent disconnection exceeding 1 hour.
- **Storage capacity**: Alert at 80% storage utilisation with capacity planning for minimum 30-day growth.
- **Platform availability**: Target 99.9% uptime for the monitoring platform; failover or redundancy for critical components.
- **Monthly health report**: IT Operations shall produce a monthly monitoring platform health report covering uptime, ingestion rates, agent coverage, and capacity projections.

### Phased Implementation Guidance

Organisations deploying monitoring capabilities for the first time or expanding scope should follow a phased approach:

| Phase | Duration | Scope | Objective |
|-------|----------|-------|-----------|
| **Phase 1 — Foundation** | Months 1-3 | Authentication logs, firewall logs, endpoint protection events forwarded to SIEM | Basic threat detection; log correlation capability |
| **Phase 2 — Expansion** | Months 4-6 | Add network traffic monitoring, cloud audit logs, application logs | Broader visibility; baseline establishment for additional systems |
| **Phase 3 — Maturation** | Months 7-12 | UEBA, automated response playbooks, MITRE ATT&CK coverage mapping, advanced analytics | Proactive threat hunting; reduced MTTD |
| **Phase 4 — Optimisation** | Ongoing | Continuous tuning, threat intelligence enrichment, red team/purple team exercises to validate detection | Sustained effectiveness; reduced false positives |

---

## Alert Management

### Alert Classification

Alerts shall be classified by severity to drive response timelines:

| Severity | Description | Response Time | Examples |
|----------|-------------|---------------|---------|
| **Critical** | Active compromise or imminent threat | **15 minutes** (business hours), **1 hour** (outside hours) | Confirmed malware execution, active data exfiltration, ransomware indicators |
| **High** | Probable security event requiring investigation | **1 hour** (business hours), **4 hours** (outside hours) | Multiple failed authentications from single source, disabling of security controls, bulk data download |
| **Medium** | Suspicious activity requiring analysis | **4 hours** (business hours), **next business day** (outside hours) | Single failed login from unusual location, minor policy violation, unexpected configuration change |
| **Low** | Informational or minor anomaly | **Next business day** | Port scan from external IP, blocked web request to suspicious category, minor threshold exceedance |

### Alert Triage Process

**Alert response staffing model**: The organisation shall define its alert response staffing approach:

| Model | Coverage | Suitable For |
|-------|----------|-------------|
| **In-house SOC** | Dedicated security analysts during business hours; on-call rotation for after-hours | Organisations with ≥3 security staff; high-risk environments |
| **Managed Detection and Response (MDR)** | 24/7 monitoring by external provider; escalation to internal team for confirmed events | Organisations with limited security staff; cost-effective 24/7 coverage |
| **Hybrid** | MDR for 24/7 first-line triage; in-house team for investigation and response | Balanced approach; most common for SMEs |
| **On-call rotation** | Business-hours monitoring with after-hours on-call for Critical/High alerts only | Minimum viable approach for small teams; requires well-tuned alerting |

The chosen model shall be documented and approved by the CISO. After-hours response capability shall be tested quarterly.

When an alert is generated:

1. **Receive**: Alert received by information security analyst (or MDR provider).
2. **Triage**: Analyst assesses whether the alert is a true positive, false positive, or requires further investigation.
3. **Enrich**: Gather additional context — asset criticality, user profile, threat intelligence, related events.
4. **Decide**: If true positive or probable security event, create an incident record per the Incident Management Policy.
5. **Escalate**: Critical and High severity incidents escalated to CISO immediately. Medium incidents escalated if not resolved within defined timeframes.
6. **Document**: All triage decisions documented — including false positives with justification.

### Alert Tuning

To maintain monitoring effectiveness and minimise alert fatigue:

- Detection rules shall be reviewed and tuned **monthly** to reduce false positive rates.
- Suppression rules shall be documented with justification and reviewed **quarterly**.
- New detection rules shall be added when: threat intelligence identifies new attack patterns, incidents reveal detection gaps, or new systems/applications are deployed.
- **Detection rule change control**: All changes to detection rules (new rules, modifications, suppressions, deletions) shall follow a documented process: change request with justification, peer review by a second analyst, testing in a non-production/staging environment where feasible, approval by the Information Security lead, and deployment with rollback capability. Emergency rule changes (e.g., in response to an active threat) may bypass peer review but shall be retrospectively reviewed within 48 hours.
- Alert volumes and false positive rates shall be tracked as key performance indicators.
- Target: false positive rate below **20%** for high-severity alerts.
- **False positive management process**: When a false positive is identified, the analyst shall: (a) document the root cause (misconfigured rule, legitimate business process, environmental noise), (b) determine the appropriate action (tune rule, add exception, suppress with expiry, accept), (c) implement the change through the detection rule change control process, and (d) verify the tuning does not suppress true positives. Persistent false positive sources (>10 occurrences per week from the same rule) shall be prioritised for tuning within 5 business days.

---

## Monitoring Review Schedule

| Review Type | Frequency | Owner | Scope |
|-------------|-----------|-------|-------|
| **Real-time alerting** | Continuous | Information Security / MDR | Critical and High severity events trigger immediate notification |
| **Alert queue review** | Daily | Information Security Analyst | Triage pending alerts; close false positives; escalate confirmed events |
| **Detection rule review** | Monthly | Information Security | Tune rules; add new detections; suppress validated false positives |
| **Monitoring coverage audit** | Quarterly | IT Operations / Information Security | Verify all in-scope systems are monitored; identify gaps; onboard new systems |
| **Baseline review** | Quarterly | Information Security | Update behavioural baselines for changes in systems, users, or business operations |
| **Effectiveness review** | Semi-annually | CISO | Review MTTD and MTTR metrics; assess detection coverage against MITRE ATT&CK; report to management. **Deliverables**: written effectiveness report including: coverage gap analysis, MITRE ATT&CK technique coverage heatmap (percentage of relevant techniques with active detection rules), trend analysis of MTTD/MTTR/false positive rates, and recommended improvements for next period |

---

## Key Performance Indicators

The following metrics shall be tracked to measure monitoring effectiveness:

| # | Metric | Target | Reporting |
|---|--------|--------|-----------|
| 1 | **Mean Time to Detect (MTTD)** | Critical events detected within 15 minutes of occurrence | Monthly to CISO |
| 2 | **Mean Time to Respond (MTTR)** | Critical alerts triaged within response SLA | Monthly to CISO |
| 3 | **Monitoring coverage** | 100% of critical systems, ≥95% of all in-scope systems. Coverage = (systems with active monitoring agent + systems with log forwarding to SIEM) / total in-scope systems from asset inventory. Systems marked out-of-scope require documented justification. | Quarterly |
| 4 | **False positive rate** | <20% for high-severity alerts | Monthly |
| 5 | **Detection rule currency** | All rules reviewed within last 90 days | Quarterly |
| 6 | **Alert backlog** | Critical: no untriaged alerts older than 1 hour; High: 4 hours; Medium: 24 hours; Low: 48 hours | Weekly |

---

## Employee Privacy and Monitoring

### Legal Requirements

Monitoring activities shall comply with Swiss employment law:

- **ArGV3 Art. 26**: Surveillance or control systems whose sole or primary purpose is to monitor employee behaviour are prohibited.
- **CO Art. 328b**: Employee data processing must be proportional and limited to what is necessary for the employment relationship or to verify the employee's suitability.
- **nFADP**: Processing of employee data through monitoring requires lawfulness, proportionality, purpose limitation, and transparency.

### Privacy Safeguards

The following safeguards shall be applied:

- Monitoring shall serve **legitimate security purposes** (threat detection, incident investigation, compliance verification) — not behavioural surveillance or performance management.
- Employees shall be **informed in advance** that monitoring takes place, what is monitored, and why, through the acceptable use policy and employment documentation.
- Only the **minimum necessary data** shall be collected and retained (data minimisation).
- Monitoring data shall **not be used** for HR performance evaluation, disciplinary action for non-security matters, or general behavioural profiling.
- **Personalised analysis** (identifying individual users) shall only occur when: (a) an alert indicates a potential security incident or policy violation, and (b) the investigation is documented with justification.
- Where monitoring data is shared with external parties (e.g., MDR providers, forensic investigators), personal identifiers shall be minimised or anonymised where feasible.
- A Data Protection Impact Assessment (DPIA) under nFADP Art. 22 shall be conducted before deployment of monitoring that meets any of the following criteria:
  - Monitoring of all employee network activity (full packet capture, URL logging).
  - Deployment of User and Entity Behaviour Analytics (UEBA) profiling individual employees.
  - Monitoring that captures employee location data (VPN connection geo-location, WiFi positioning).
  - Monitoring of personal device activity under BYOD arrangements.
  - Any monitoring activity where the DPO or Data Protection Advisor determines that the processing is likely to result in a high risk to employee personality rights.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; approval of monitoring scope and detection priorities; escalation point for critical alerts; semi-annual effectiveness review |
| **Information Security Analyst** | Daily alert triage; incident escalation; detection rule maintenance; false positive management; monthly tuning |
| **IT Operations / Platform Team** | Monitoring platform administration; agent deployment; log source onboarding; capacity management; system health monitoring |
| **System Administrators** | Ensuring monitoring agents are installed and operational on managed systems; reporting monitoring failures or gaps |
| **MDR Provider** (if applicable) | 24/7 alert monitoring; initial triage and enrichment; escalation of confirmed events per agreed runbooks |
| **Data Protection Advisor** | Guidance on privacy impact of monitoring activities; DPIA requirements; employee notification requirements |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Monitoring platform configuration** and system inventory (data sources, detection rules, alert routing) | IT Operations | *Configuration documented; data source inventory reviewed quarterly* |
| 2 | **Monitoring coverage metric** (percentage of in-scope systems with active monitoring) | IT Operations / Information Security | *Quarterly; target: 100% critical, ≥95% all in-scope* |
| 3 | **Behavioural baseline documentation** for critical systems and user groups | Information Security | *Documented; reviewed quarterly and after significant changes* |
| 4 | **Alert triage records** showing classification, triage decision, and response timeline | Information Security | *Retained 12 months; sampled during audit* |
| 5 | **Detection rule change log** (new rules, tuned rules, suppressed rules with justification) | Information Security | *Monthly; log retained 12 months* |
| 6 | **MTTD and MTTR metrics** reported to management | CISO | *Monthly to CISO; semi-annually to management review* |
| 7 | **False positive rate** and alert volume trends | Information Security | *Monthly; target <20% false positive rate for high-severity* |
| 8 | **Employee notification records** (acceptable use policy, privacy notice regarding monitoring) | HR / Information Security | *Updated per policy change; acknowledgment tracked annually* |
| 9 | **DPIA records** (if large-scale monitoring is implemented) | Data Protection Advisor | *Completed before deployment; reviewed annually* |
| 10 | **Monitoring platform health records** — uptime, data ingestion rates, agent health, storage capacity (SOC 2: CC4.1) | IT Operations | *Continuous monitoring; monthly summary report* |
| 11 | **Escalation records** — documented escalation path usage, escalation timeliness, resolution outcomes | Information Security | *Per escalation; reviewed monthly* |
| 12 | **MITRE ATT&CK coverage mapping** — techniques covered by detection rules, identified gaps, remediation plans | Information Security | *Semi-annually* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through monitoring coverage audits, alert response reviews, KPI tracking, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to monitoring technologies, threat landscape developments, regulatory requirements, and lessons learned from incidents and false positive analysis.

---

# Areas of the ISO 27001 Standard Addressed

Monitoring Activities Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 9.1 Monitoring, measurement, analysis, and evaluation | 5.37 Documented operating procedures |
| | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | **8.16 Monitoring activities** |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures; Art. 6 — Proportionality |
| Swiss CO (Code of Obligations) | Art. 328b — Employee data processing limitations |
| Swiss ArGV3 (Ordinance 3 to Employment Act) | Art. 26 — Prohibition on behaviour surveillance |
| EU GDPR (where applicable) | Art. 32 — Security of processing |
| ISO/IEC 27001:2022 | Annex A Control 8.16 |
| ISO/IEC 27002:2022 | Section 8.16 — Implementation guidance |
| NIST SP 800-53 Rev 5 | SI-4 (Information System Monitoring), AU-6 (Audit Record Review), CA-7 (Continuous Monitoring) |
| NIST CSF 2.0 | DE.CM (Continuous Monitoring), DE.AE (Adverse Event Analysis) |
| CIS Controls v8 | Control 8 (Audit Log Management), Control 13 (Network Monitoring and Defence) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
