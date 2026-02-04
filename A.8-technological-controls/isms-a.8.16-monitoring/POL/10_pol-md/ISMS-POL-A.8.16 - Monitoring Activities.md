**ISMS-POL-A.8.16 — Monitoring Activities**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Monitoring Activities |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.16 |
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
| 1.0 | [Date] | CISO | Initial consolidated policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- Operational Review: Security Operations Center (SOC) Lead
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.8.15 (Logging)
- ISMS-POL-A.5.24-5.28 (Incident Management)
- ISMS-IMP-A.8.16 (Implementation Guidance Suite)
- ISO/IEC 27001:2022 Control A.8.16
- ISO/IEC 27002:2022 Control 8.16

---

## Executive Summary

This policy establishes [Organization]'s requirements for monitoring activities to detect anomalous behavior and potential information security incidents in accordance with ISO/IEC 27001:2022 Control A.8.16.

**Scope**: This policy applies to all networks, systems, and applications where monitoring is technically feasible; all users (employees, contractors, service accounts); and all monitoring technologies regardless of vendor or deployment model.

**Purpose**: Define organizational requirements for monitoring activities control implementation and governance. This policy establishes WHAT monitoring is required, WHERE monitoring must be implemented, and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.8.16.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, and ISO/IEC 27001:2022. Conditional sector-specific requirements (FINMA, DORA, NIS2) apply where [Organization]'s business activities trigger applicability.

**Philosophy**: As Richard Feynman wisely noted: *"The first principle is that you must not fool yourself—and you are the easiest person to fool."* This framework prevents **cargo cult monitoring**—having SIEM dashboards that no one reads, alerts that everyone ignores, and "baselines" that are just guesses. True monitoring requires documented baselines, measurable thresholds, evidenced response procedures, and quantifiable effectiveness metrics.

---

# Control Alignment & Scope

## ISO/IEC 27001:2022 Control A.8.16

**ISO/IEC 27001:2022 Annex A.8.16 - Monitoring Activities**

> *Networks, systems and applications should be monitored for anomalous behavior and appropriate actions taken to evaluate potential information security incidents.*

**Control Objective**: Establish organizational policy for monitoring activities to detect abnormal behavior and potential information security incidents through systematic observation, baseline establishment, anomaly detection, and integration with incident management processes.

**This Policy Addresses**:

- Monitoring scope determination (what systems, networks, applications to monitor)
- Baseline establishment for normal behavior patterns
- Anomaly detection capabilities and methodologies
- Alert generation, classification, and response requirements
- Monitoring infrastructure requirements (tools, capabilities, integration)
- Log data retention and archival for compliance and forensics
- Organizational roles and responsibilities for monitoring governance
- Exception and incident management frameworks
- Integration with [Organization]'s risk assessment and incident response processes

## What This Policy Does

This policy:

- **Defines** monitoring control requirements aligned with data classification, system criticality, and regulatory obligations
- **Establishes** governance framework for monitoring decision-making and accountability
- **Specifies** mandatory monitoring scope based on risk assessment and business requirements
- **References** applicable regulatory requirements per ISMS-POL-00
- **Identifies** organizational roles and responsibilities for monitoring controls
- **Provides** framework for managing exceptions and monitoring gaps

## What This Policy Does NOT Do

This policy does NOT:

- **Specify technical monitoring procedures** (see ISMS-IMP-A.8.16 Implementation Guides)
- **Define specific SIEM configurations or detection rules** (see ISMS-IMP-A.8.16.2 Baseline & Detection Assessment)
- **List approved monitoring tools or vendors** (technology selection based on [Organization]'s risk assessment and technical environment)
- **Provide step-by-step alert response playbooks** (see ISMS-IMP-A.8.16 Alert Response Procedures)
- **Select specific monitoring technologies** (technology selection based on [Organization]'s architecture, risk profile, and operational needs)
- **Replace risk assessment** (monitoring controls selected based on [Organization]'s risk treatment decisions)
- **Define detailed incident response procedures** (see ISMS-POL-A.5.24-5.28 Incident Management)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite evolving threat landscape and technology changes
- Technical agility for tool updates and detection rule refinement without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Focused audit scope (auditors audit policy compliance, not technical implementation details)

## Scope

**This policy applies to**:

- All network segments where monitoring is technically feasible (on-premises, cloud, hybrid, remote access)
- All systems requiring monitoring per risk assessment (servers, workstations, network devices, security appliances)
- All applications assessed as business-critical or security-sensitive
- All users accessing organizational resources (employees, contractors, service accounts, automated systems)
- All monitoring technologies regardless of vendor or deployment model (SIEM, IDS/IPS, NDR, EDR, UEBA, log management)
- All third-party service providers with access to organizational systems or data

**Out of Scope**:

- Application performance monitoring for non-security purposes (covered under IT operations policies)
- Business intelligence and analytics unrelated to security (covered under data analytics policies)
- Network traffic optimization and capacity planning (covered under network management policies)
- User productivity monitoring (covered under HR policies, distinct from security monitoring)

**Critical Systems Requiring Mandatory Monitoring**:

- Domain controllers and authentication infrastructure
- Firewalls, VPN gateways, and network security devices
- Database servers containing Confidential or Restricted data
- Internet-facing web servers and applications
- Email servers and messaging infrastructure
- File servers containing business-critical or sensitive data
- Security monitoring infrastructure itself (SIEM, IDS/IPS, EDR)
- Cloud infrastructure and platform services (where [Organization] has monitoring visibility)

## Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**. 

**Tier 1: Mandatory Compliance**

| Regulation | Applicability | Key Monitoring Requirements |
|------------|---------------|----------------------------|
| **Swiss nDSG** | All Swiss operations | Art. 8 - Technical and organizational measures including monitoring for data protection |
| **EU GDPR** | When processing EU personal data | Art. 32 - Security measures including monitoring and detection capabilities |
| **ISO/IEC 27001:2022** | Certification scope | Control A.8.16 - Documented policy, implemented controls, evidence of effectiveness |

**Tier 2: Conditional Applicability**

Apply only when specific business conditions trigger applicability:

| Regulation | Trigger Condition | Monitoring Requirements |
|-----------|-------------------|------------------------|
| **FINMA Circular 2023/1** | Swiss regulated financial institution | Margin 63-72: Logging, monitoring, and incident detection for operational resilience |
| **DORA** | EU financial services entity | Art. 17: ICT-related incident detection, logging, and monitoring capabilities |
| **NIS2** | Essential/important entity (EU) | Art. 21: Security monitoring, incident detection, and response capabilities |
| **PCI DSS v4.0** | Processing payment card data | Req. 10: Logging and monitoring of access to cardholder data environments |
| **HIPAA** | Processing US healthcare data | §164.312(b): Audit controls and monitoring of ePHI access |

**Tier 3: Informational Guidance**

These frameworks inform implementation but do not constitute mandatory compliance unless contractually required:

- NIST SP 800-92 (Guide to Computer Security Log Management)
- NIST SP 800-137 (Information Security Continuous Monitoring)
- CIS Controls v8 (Control 8: Audit Log Management, Control 13: Network Monitoring and Defense)
- MITRE ATT&CK Framework (Detection tactics and techniques)
- SANS Critical Security Controls

**Compliance Determination**: [Organization] determines applicable Tier 2 regulations through periodic business activity assessment documented in ISMS-POL-00. The most stringent requirements apply where multiple regulations overlap.

## Integration with ISMS

**Risk Management Integration (ISO 27001 Clause 6)**:

- Monitoring controls implemented as detective measures in defense-in-depth strategy
- Monitoring gaps identified through risk assessment and documented in risk register
- Risk treatment decisions determine monitoring scope and priority
- Residual risks from monitoring limitations tracked and accepted by management

**Related ISMS Controls**:

| Control | Integration Point | Monitoring Role |
|---------|-------------------|----------------|
| **A.5.7** | Threat Intelligence | Monitoring generates intelligence from observed attacks; threat intel informs detection rules |
| **A.5.16** | Identity Management | User and entity behavior monitoring analyzes identity-based access patterns |
| **A.5.24-5.28** | Incident Management | Monitoring alerts trigger incident response workflow; incidents inform monitoring improvements |
| **A.8.7** | Malware Protection | Malware detection alerts feed monitoring; monitoring detects malware behavior patterns |
| **A.8.8** | Vulnerability Management | Monitoring identifies exploitation attempts; prioritizes patching based on observed attacks |
| **A.8.12** | Data Leakage Prevention | Monitoring detects data exfiltration patterns and unauthorized data transfers |
| **A.8.15** | Logging | Monitoring analyzes log data generated by logging controls; logging provides monitoring data |
| **A.8.17** | Clock Synchronization | Accurate timestamps essential for event correlation and timeline reconstruction |
| **A.8.20** | Network Security | Network security controls generate monitored events; monitoring validates control effectiveness |
| **A.8.23** | Web Filtering | Web filtering logs feed monitoring as log source; monitoring detects web-based threats |

---

# Monitoring Requirements Framework

## Monitoring Infrastructure Requirements

[Organization] SHALL implement monitoring infrastructure with adequate capabilities to collect, analyze, store, and act upon security-relevant events.

### Monitoring Platform Capabilities

Monitoring platforms (SIEM, IDS/IPS, EDR, NDR, UEBA, or equivalent) SHALL provide:

**Collection Capabilities**:

- Multi-source log ingestion (syslog, agents, APIs, file-based, cloud-native)
- Protocol support for common log formats (CEF, LEEF, JSON, XML, syslog RFC)
- Real-time and batch log collection methods
- Secure log transmission (encrypted channels, authenticated sources)
- Scalable collection supporting organizational growth

**Analysis Capabilities**:

- Real-time event correlation across multiple log sources
- Pattern matching and signature-based detection
- Statistical anomaly detection (deviation from baselines)
- User and entity behavior analytics (UEBA)
- Threat intelligence integration and enrichment
- Custom detection rule creation and tuning

**Storage and Retention**:

- Hot storage for active monitoring (minimum 90 days operational logs, 12 months security alerts)
- Warm/cold storage for compliance and forensics (retention aligned with regulatory requirements)
- Indexed search capabilities for rapid investigation
- Data integrity protection (tamper-evident logging)
- Backup and disaster recovery for monitoring data

**Alerting and Notification**:

- Configurable alert rules with severity classification
- Multi-channel notification (email, SMS, ticketing system integration, SOAR)
- Alert deduplication and correlation
- Escalation workflows based on severity and response time
- Integration with incident management systems

**Reporting and Dashboards**:

- Real-time security operations dashboards
- Executive summary reports (compliance, KPIs, trends)
- Compliance reporting aligned with regulatory requirements
- Forensic investigation capabilities (timeline reconstruction, evidence collection)
- Customizable reporting for stakeholder needs

### Log Source Coverage

[Organization] SHALL monitor log sources from:

**Network Infrastructure**:

- Firewalls (allowed/denied traffic, rule changes, VPN connections)
- Routers and switches (configuration changes, access control lists, network topology changes)
- Load balancers (traffic distribution, health checks, SSL termination)
- VPN gateways (connection attempts, authentication, data transfer)
- Wireless access points (client associations, authentication failures, rogue AP detection)
- Intrusion Detection/Prevention Systems (IDS/IPS signatures, blocked attacks)

**Security Appliances**:

- Web application firewalls (WAF) - HTTP/HTTPS traffic, attack attempts, rule violations
- Web filters - URL categories accessed, blocked attempts, policy violations
- Data Loss Prevention (DLP) - data transfer attempts, policy violations, content inspection
- Email security gateways - spam, phishing, malware, data leakage attempts
- Endpoint protection platforms (EPP/EDR) - malware detection, behavioral analysis, remediation actions
- Network Detection and Response (NDR) - lateral movement, anomalous traffic, C2 communication

**Systems and Servers**:

- Operating system logs (authentication, privilege escalation, system errors, configuration changes)
- Application logs (access, errors, transactions, security events)
- Database logs (queries, authentication, schema changes, sensitive data access)
- Web server logs (access logs, error logs, HTTP methods, response codes)
- Directory services (Active Directory, LDAP) - authentication, group changes, policy modifications
- Virtualization platforms (VM creation/deletion, resource allocation, migration events)

**Cloud Infrastructure**:

- Cloud platform logs (AWS CloudTrail, Azure Monitor, GCP Cloud Logging)
- Container orchestration (Kubernetes audit logs, pod events, RBAC changes)
- Serverless function executions (invocations, errors, resource consumption)
- Cloud storage access (bucket access, object downloads, permission changes)
- Identity and access management (IAM policy changes, role assignments, authentication events)

### Monitoring Coverage Assessment

[Organization] SHALL:

- Document all critical systems and their monitoring status (ISMS-IMP-A.8.16.3 Coverage Assessment)
- Calculate monitoring coverage percentage: (Monitored Critical Systems / Total Critical Systems) × 100
- Target coverage: 100% of Tier 1 (Critical) systems, >80% of Tier 2 (Standard) systems
- Identify and document monitoring gaps with risk assessment and remediation timelines
- Review coverage quarterly and after significant infrastructure changes

### Monitoring Infrastructure Resilience

Monitoring infrastructure SHALL be:

- **Redundant**: No single point of failure in log collection, storage, or alerting
- **Isolated**: Monitoring systems on separate network segments, protected from monitored systems
- **Secured**: Hardened configurations, restricted access, multi-factor authentication required
- **Monitored**: Monitoring infrastructure itself subject to health checks and alerting
- **Tested**: Regular testing of detection capabilities, failover procedures, backup restoration

## Baseline & Anomaly Detection Requirements

[Organization] SHALL establish baselines for normal behavior and configure anomaly detection capabilities.

### Baseline Philosophy

**The Feynman Principle Applied to Baselines:**
> *"If you cannot measure it with numbers, you don't have a baseline—you have an opinion."*

**Acceptable Baseline**:

- ✅ "User authentication rate during business hours (08:00-18:00 CET): Mean 145 logins/hour, Std Dev 23, 95th percentile 189"
- ✅ "Database query rate: Baseline 450 queries/minute ±50, alert threshold 600 queries/minute (95th percentile × 1.3)"

**Unacceptable "Baseline"**:

- ❌ "Normal authentication activity is around 100-200 logins per hour" (imprecise)
- ❌ "Database seems busy during the day" (subjective, unmeasurable)

### Baseline Establishment Requirements

Baselines SHALL be established for:

**System Utilization Baselines**:

- CPU utilization (mean, median, standard deviation, 95th percentile) during normal and peak times
- Memory consumption patterns
- Disk I/O and storage utilization
- Network bandwidth consumption (ingress/egress)
- Process and service resource consumption

**Access Pattern Baselines**:

- User authentication timing (time of day, day of week patterns)
- Geographic access patterns (normal locations, remote access patterns)
- Access frequency per user/system (daily logins, application access rates)
- Privileged access patterns (administrator logins, sudo usage, elevation requests)
- Failed authentication attempts baseline (normal failure rate vs. attack indicators)

**Application Behavior Baselines**:

- Transaction volumes and timing
- API call rates and patterns
- Database query patterns
- File access and modification patterns
- Network connection patterns (internal, external, protocols used)

### Baseline Documentation

Each baseline SHALL be documented with:

- **System/Asset Identified**: Specific system, user group, or application
- **Metric Definition**: Precise description of what is measured
- **Observation Period**: Duration of baseline establishment (minimum 30 days, including business cycles)
- **Statistical Profile**: Mean, median, standard deviation, 95th/99th percentiles
- **Time-Aware Baselines**: Separate baselines for business hours, off-hours, weekends, holidays if patterns differ
- **Exclusions**: Documented exclusions (known maintenance windows, incidents, anomalies)
- **Baseline Validity**: Effective date, review frequency (quarterly minimum), next review date
- **Peer Review** (mandatory for Tier 1 Critical system baselines): Independent validation by SOC Lead or Security Manager confirming observation period selection, exclusion justifications, and threshold derivation methodology
- **Threshold Derivation**: Methodology for deriving alert thresholds from baseline (e.g., 95th percentile × 1.5)
- **Owner**: Responsible party for baseline accuracy and updates

**Note**: For non-Tier 1 systems, peer review is recommended but optional to reduce administrative burden.

Baseline documentation template provided in **Annex B**.

### Anomaly Detection Scope

Monitoring systems SHALL be configured to detect anomalous behavior including:

**Unplanned System Behavior**:

- Unexpected process termination or service failures
- Unusual resource consumption (CPU spikes, memory exhaustion, disk space depletion)
- Configuration changes outside approved change windows
- Unauthorized software installation or execution
- Unusual network connections (new destinations, protocols, ports)

**Malicious Activity Indicators**:

- Known malware signatures and behavior patterns
- Traffic to/from known malicious IPs, domains, or botnets (C2 infrastructure)
- Exploit attempt signatures (buffer overflows, injection attacks, privilege escalation)
- Lateral movement patterns (internal reconnaissance, credential dumping, pass-the-hash)
- Data exfiltration indicators (large outbound transfers, unauthorized cloud uploads, DNS tunneling)

**Attack Signatures**:

- Denial-of-service attack patterns (SYN floods, UDP floods, application-layer attacks)
- Web application attacks (SQL injection, XSS, CSRF, directory traversal)
- Network scanning and reconnaissance (port scans, vulnerability scans, ping sweeps)
- Brute-force authentication attempts
- Protocol anomalies and malformed requests

**Unusual User/Entity Behavior**:

- Access attempts to resources outside normal scope (privilege creep detection)
- Unusual access timing (logins at 03:00 when user normally works 09:00-17:00)
- Geographic anomalies (login from Switzerland at 10:00, login from China at 10:05)
- Concurrent sessions from different locations (impossible travel)
- Unusual data access patterns (mass file downloads, database dumps, sensitive data queries)
- Privilege escalation outside normal workflows
- Disabled logging or monitoring on systems (anti-forensics indicators)

**Unauthorized Access**:

- Successful authentication with compromised credentials
- Unauthorized access attempts to protected resources
- Privilege escalation without approval
- Access to systems/data outside user's job function
- After-hours access to business-critical systems without approval

### Detection Effectiveness Requirements

[Organization] SHALL:

- Test detection rules quarterly using simulated attacks or purple team exercises
- Track detection effectiveness metrics: True Positives, False Positives, False Negatives
- Target detection rates: >90% True Positive rate for high-severity threats
- Target false positive rates: <20% for critical alerts, <30% for high-severity alerts
- Document detection gaps (what cannot be detected) and implement compensating controls
- Continuously tune detection rules to improve accuracy

## Alert Management & Response Requirements

[Organization] SHALL implement alert management and response capabilities ensuring timely and effective action on security events.

### Alert Classification

Alerts SHALL be classified by severity:

| Severity | Definition | Response Time SLA | Examples |
|----------|------------|-------------------|----------|
| **Critical** | Active attack in progress, imminent data loss, or complete service disruption | 15 minutes | Ransomware detected, active data exfiltration, root compromise, critical infrastructure failure |
| **High** | Significant security incident with potential for major impact | 1 hour | Malware infection, successful privilege escalation, sensitive data access by unauthorized user, brute force attack success |
| **Medium** | Security concern requiring investigation, potential incident | 4 hours | Failed privilege escalation attempts, anomalous behavior patterns, policy violations, suspicious authentication activity |
| **Low** | Informational event, minor policy violation, or low-impact anomaly | 24 hours | Minor configuration deviations, low-severity policy violations, informational security events |
| **Informational** | Logged for awareness, no immediate action required | Review during business hours | Routine administrative actions, expected security events, compliance logging |

### Alert Response SLAs

For each severity level, [Organization] defines:

- **Acknowledgment SLA**: Maximum time to acknowledge alert receipt (confirm SOC analyst awareness)
- **Triage SLA**: Maximum time to perform initial assessment (determine if incident)
- **Investigation SLA**: Maximum time to complete investigation and determine root cause
- **Containment SLA**: Maximum time to contain active threats (for Critical/High severity)
- **Resolution SLA**: Maximum time to fully resolve incident

**Minimum SLA Requirements**:

| Severity | Acknowledgment | Triage | Investigation | Containment | Resolution |
|----------|----------------|--------|---------------|-------------|------------|
| **Critical** | 5 min | 15 min | 2 hours | 1 hour | 24 hours |
| **High** | 15 min | 1 hour | 8 hours | 4 hours | 5 business days |
| **Medium** | 1 hour | 4 hours | 24 hours | 24 hours | 10 business days |
| **Low** | 4 hours | 24 hours | 5 business days | N/A | 20 business days |

[Organization] MAY define more aggressive SLAs based on risk appetite and operational capabilities.

### Alert Handling Procedures

**Alert Triage**:
1. **Validate**: Determine if alert is true positive or false positive
2. **Classify**: Assign correct severity based on actual vs. perceived risk
3. **Correlate**: Check for related events (same user, system, attack pattern)
4. **Document**: Record triage findings, evidence collected, initial assessment
5. **Escalate**: Escalate to Incident Response if confirmed security incident

**Escalation Criteria**:

- Alert meets Critical or High severity classification
- Multiple correlated alerts indicating coordinated attack
- Confirmed data breach or exfiltration
- Ransomware or destructive malware detected
- Compromise of critical infrastructure (domain controller, firewall, SIEM)
- Legal or regulatory reporting obligations triggered
- Executive management notification required per incident management policy

**False Positive Handling**:

- Document reason for false positive (baseline issue, detection rule overly sensitive, legitimate activity miscategorized)
- Submit detection rule tuning request to Security Engineering
- Track false positive rates per rule and overall
- Review high-FP rules quarterly for tuning or deactivation

### Alert Tuning and Optimization

[Organization] SHALL:

- Review alert volume and false positive rates monthly
- Tune detection rules to reduce false positives while maintaining detection coverage
- Deactivate or modify rules with >40% false positive rate after investigation
- Document tuning decisions with rationale and approval
- Validate tuning effectiveness through post-change monitoring
- Balance detection coverage (recall) vs. alert noise (precision)

**Tuning Methodology**:
1. Identify high-noise alerts (>10 instances/day with <50% true positive rate)
2. Analyze root cause (bad baseline, overly sensitive threshold, legitimate activity pattern)
3. Propose tuning (adjust threshold, refine detection logic, add whitelist exceptions)
4. Test tuning in monitoring-only mode (validate reduction in FPs without increasing FNs)
5. Implement tuning with documentation
6. Monitor post-tuning effectiveness (validate FP reduction, confirm no increase in missed detections)

## Retention & Archival Requirements

[Organization] SHALL retain monitoring data for compliance, forensics, and operational requirements.

### Retention Periods

**Operational Logs** (routine system activity, not security incidents):

- **Hot Storage** (indexed, searchable, real-time access): 90 days minimum
- **Warm/Cold Storage** (archived, slower retrieval): 12 months total retention

**Security Alerts and Incidents**:

- **Hot Storage**: 12 months minimum
- **Long-Term Archive**: Aligned with legal and regulatory requirements

**Compliance-Driven Retention**:

- **GDPR/nDSG**: Retention justified by legitimate interest, deleted when no longer needed (typically 12-24 months)
- **FINMA Circular 2023/1** (if applicable): 10 years for critical operational events
- **PCI DSS** (if applicable): 12 months hot storage, 3 months immediately available
- **HIPAA** (if applicable): 6 years minimum
- **Litigation Hold**: Indefinite retention until hold released

### Archival Process

Monitoring data archival SHALL:

- Transfer logs from hot to warm/cold storage automatically after retention period
- Maintain data integrity during transfer (checksums, tamper-evident logging)
- Compress archived data to optimize storage costs
- Encrypt archived data at rest
- Test archival restoration quarterly to validate recoverability
- Document archival locations, formats, and retrieval procedures

### Data Protection and Privacy

Monitoring data SHALL be:

- **Access Controlled**: Only authorized SOC, security team, CISO, and DPO have access
- **Encrypted**: At rest and in transit
- **Anonymized/Pseudonymized**: Where feasible for privacy protection (while maintaining forensic value)
- **Protected from Tampering**: Write-once-read-many (WORM) storage or equivalent integrity protection
- **Segregated**: Monitoring logs on separate infrastructure from monitored systems

**Employee Privacy Considerations** (Swiss nDSG Art. 328b CO, GDPR Art. 88):

- Monitoring scope limited to security and compliance objectives (no performance management, personal activity surveillance)
- Employees informed of monitoring through employment contracts, privacy notices, acceptable use policies
- Proportionality assessed: monitoring breadth and depth justified by security needs
- Data minimization: collect only security-relevant events, limit log verbosity to necessary fields
- Purpose limitation: monitoring data not used for HR performance evaluations without separate legal basis

---

# Governance & Compliance

## Roles & Responsibilities

Monitoring activities require clear accountability across organizational roles.

**Accountability Matrix (RACI)**:

| Role | Responsibility | Accountability |
|------|----------------|----------------|
| **Chief Information Security Officer (CISO)** | Strategic oversight, policy ownership, budget allocation, risk acceptance | Accountable for monitoring program effectiveness and compliance |
| **Security Operations Center (SOC) Lead** | Day-to-day monitoring operations, alert triage, escalation, team management | Responsible for 24/7 monitoring, initial incident response, SLA compliance |
| **Security Team** | Baseline definition, detection rule creation, tool management, tuning | Responsible for monitoring infrastructure, detection effectiveness, integration |
| **System Owners** | Ensure their systems log to monitoring platforms, provide domain expertise | Responsible for system-level monitoring configuration and evidence collection |
| **IT Operations** | Infrastructure support for monitoring platforms, log source onboarding | Responsible for operational support, capacity management, availability |
| **Network Team** | Network monitoring infrastructure, traffic analysis, firewall/IDS log collection | Responsible for network-level monitoring and traffic analysis |
| **Incident Response Team** | Escalated incident investigation, forensics, remediation, lessons learned | Responsible for incident handling post-SOC escalation |
| **Data Protection Officer (DPO)** | Privacy oversight, compliance with data protection regulations | Consulted on monitoring scope, data retention, employee privacy |
| **Legal/Compliance** | Regulatory interpretation, legal hold management, evidence preservation | Consulted on legal requirements, advised on compliance obligations |
| **Executive Management** | Resource allocation, strategic direction, risk acceptance | Informed through quarterly compliance reporting, approve monitoring budget |

## Policy Governance

### Policy Review and Updates

This policy SHALL be reviewed:

- **Annually** as part of ISMS policy review cycle
- **Upon significant changes** to organizational risk profile, IT infrastructure, or threat landscape
- **Following major security incidents** where monitoring gaps are identified
- **When new monitoring technologies** are deployed or existing tools are significantly upgraded
- **Upon regulatory changes** affecting monitoring requirements (new laws, updated standards, guidance publications)

Policy updates require:

- Proposal with business/security justification
- Risk assessment of proposed changes
- Review by affected stakeholders (SOC, Security Team, System Owners, Legal/Compliance)
- Approval by CISO
- Communication to relevant personnel
- Update to related implementation documentation (ISMS-IMP-A.8.16)

### Exception Management

Exceptions to monitoring requirements SHALL be:

- **Documented** with business/technical justification
- **Risk-Assessed** to quantify impact of monitoring gap
- **Compensating Controls** identified and implemented where feasible
- **Approved** by SOC Lead (operational exceptions) or CISO (policy exceptions)
- **Time-Limited**: Maximum 12 months, with shorter durations for high-severity gaps
- **Reviewed** quarterly to validate continued necessity and effectiveness of compensating controls
- **Tracked** in exception register with status, remediation plan, and responsible party

**Valid Exception Examples**:

- Legacy system without logging capability, scheduled for decommissioning in 6 months (compensating control: network monitoring of all traffic to/from system)
- Cloud service with limited logging visibility (compensating control: monitor API activity, configure maximum available logging)
- High-volume low-value alerts temporarily disabled for tuning (compensating control: enhanced manual review of related metrics)

**Invalid Exception Examples**:

- "Monitoring is too expensive" (cost is not a valid exception to security requirement)
- "We don't have time to configure logging" (resource constraints require escalation, not exception)
- "This system is not important" (criticality assessment required, not assumption-based exception)

### Compliance Verification

Compliance with monitoring requirements SHALL be verified through:

- **Quarterly Self-Assessments**: ISMS-IMP-A.8.16 assessment workbooks completed by responsible teams
- **Annual Internal Audit**: Verification of policy compliance, evidence review, control effectiveness testing
- **External Audits**: ISO 27001 certification audits, regulatory inspections (FINMA, DPA, etc.)
- **Detection Testing**: Quarterly purple team exercises or simulated attacks to validate detection capabilities
- **Metrics Review**: Monthly review of MTTD, MTTR, false positive rates, coverage percentages, SLA compliance

**Compliance Evidence**:

- Completed assessment workbooks with supporting evidence
- Monitoring infrastructure architecture diagrams
- Baseline documentation per Annex B template
- Detection rule inventory with effectiveness metrics
- Alert response logs demonstrating SLA compliance
- Exception register with approvals and compensating controls
- Incident response tickets showing monitoring-triggered investigations

## Integration with Risk Management

**Risk Assessment**:

- Monitoring scope determined through risk assessment (critical assets prioritized for monitoring)
- Monitoring gaps identified as risks in risk register
- Risk treatment decisions determine monitoring investment and priorities

**Risk Register**:

- Monitoring risks documented: blind spots, alert fatigue, insufficient coverage, detection gaps
- Risk scores drive remediation urgency (Critical gaps addressed within 30 days, High within 90 days)
- Quarterly risk reassessment based on monitoring effectiveness metrics and incident trends

**Risk Treatment**:

- Accept: Document monitoring limitations with executive risk acceptance (e.g., legacy systems unmonitorable)
- Mitigate: Implement monitoring controls, enhance detection coverage, reduce alert noise
- Transfer: Third-party SOC services, managed detection and response (MDR)
- Avoid: Decommission unmonitorable high-risk systems

---

# Implementation & References

## Implementation Resources

**Implementation Guidance (ISMS-IMP-A.8.16 Suite)**:

| Document | Purpose | Target Audience | Review Frequency |
|----------|---------|----------------|------------------|
| **ISMS-IMP-A.8.16.1** | Monitoring Infrastructure Assessment | Security Engineering, IT Operations | Semi-annual |
| **ISMS-IMP-A.8.16.2** | Baseline & Detection Assessment | SOC, Security Team, Threat Intelligence | Quarterly |
| **ISMS-IMP-A.8.16.3** | Coverage Assessment | System Owners, Network Team, Security Team | Quarterly |
| **ISMS-IMP-A.8.16.4** | Alert Management & Response Assessment | SOC, Incident Response, Security Team | Quarterly |
| **ISMS-IMP-A.8.16.5** | Compliance Dashboard | CISO, Security Managers, Auditors | Continuous |

**Assessment Tools**:

- Excel-based assessment workbooks generated via Python automation (5 workbooks)
- Evidence registers and gap analysis templates embedded in workbooks
- Remediation tracking and reporting capabilities
- Automated compliance calculations and status dashboards

**Supporting Materials** (ISMS-IMP-A.8.16 Annexes):

- Alert Response Procedures (operational incident handling playbooks, documented within ISMS-IMP-A.8.16.4 Alert Management & Response Assessment, Annex A)
- Detection Rule Library (organization-specific detection rules and use cases)
- Tuning Playbook (procedures for alert tuning and optimization)
- Baseline Review Template (structured baseline review process)

## Related ISMS Policies

This policy integrates with:

| Policy | Relationship |
|--------|--------------|
| **ISMS-POL-00** | Regulatory Applicability Framework - defines applicable regulations |
| **ISMS-POL-A.8.15** | Logging - provides log data for monitoring analysis |
| **ISMS-POL-A.5.24-5.28** | Incident Management - consumes monitoring alerts, incident response workflow |
| **ISMS-POL-A.5.7** | Threat Intelligence - threat intel informs detection rules, monitoring generates intelligence |
| **ISMS-POL-A.8.8** | Vulnerability Management - monitoring identifies exploitation, prioritizes patching |
| **ISMS-POL-A.8.20** | Network Security - network controls generate monitored events |
| **ISMS-POL-A.8.23** | Web Filtering - web filtering logs feed monitoring as log source |
| **ISMS-POL-A.8.12** | Data Leakage Prevention - monitoring detects data exfiltration patterns |

## External Standards & Regulations

**International Standards**:

- ISO/IEC 27001:2022 - Information Security Management Systems
- ISO/IEC 27002:2022 - Information Security Controls (Control 8.16 guidance)
- ISO/IEC 27035 - Incident Management (integration with monitoring)

**Technical Standards**:

- NIST SP 800-92 - Guide to Computer Security Log Management
- NIST SP 800-137 - Information Security Continuous Monitoring (ISCM)
- CIS Controls v8 - Control 8 (Audit Log Management), Control 13 (Network Monitoring)

**Regulatory**:

- Swiss Federal Act on Data Protection (FADP/nDSG)
- EU General Data Protection Regulation (GDPR) - where applicable
- FINMA Circular 2023/1 (Operational risks and resilience) - if applicable
- DORA (Digital Operational Resilience Act) - if applicable
- NIS2 Directive - if applicable
- Industry-specific regulations (PCI DSS, HIPAA, etc.) - as applicable

**Framework Alignment**:

- NIST Cybersecurity Framework (CSF) - Detect function
- MITRE ATT&CK Framework - Detection tactics and techniques
- SANS Critical Security Controls

---

# Definitions

**Monitoring**  
The continuous or periodic observation and analysis of networks, systems, and applications to identify anomalous behavior, security incidents, policy violations, or operational issues requiring attention.

**Baseline**  
A documented, measurable profile of normal behavior for a system, network segment, application, or user established during known-good operational periods. Baselines include statistical metrics (mean, median, standard deviation, percentiles) and are time-aware (business hours, off-hours, weekends).

**Anomalous Behavior**  
Activity that deviates significantly from established baselines or expected patterns. Anomalies may indicate security incidents, misconfigurations, policy violations, or legitimate but unusual business activities requiring investigation.

**Alert**  
A notification generated by monitoring systems when predefined thresholds are exceeded or specific security events occur. Alerts are classified by severity and trigger response procedures per SLA requirements.

**False Positive**  
An alert triggered by legitimate activity incorrectly identified as anomalous or malicious. High false positive rates lead to alert fatigue and require detection rule tuning.

**False Negative**  
A security incident or anomalous activity that should have triggered an alert but was not detected. False negatives represent detection gaps requiring rule enhancement or baseline adjustment.

**Mean Time to Detect (MTTD)**  
Average time elapsed between an incident occurring and detection by monitoring systems. Lower MTTD indicates more effective monitoring.

**Mean Time to Respond (MTTR)**  
Average time elapsed between alert generation and incident containment/resolution. Lower MTTR indicates more effective incident response.

**Security Information and Event Management (SIEM)**  
Centralized platform for collecting, correlating, analyzing, and storing security-relevant logs and events from multiple sources. SIEM provides real-time alerting, forensic investigation, and compliance reporting.

**Intrusion Detection System (IDS) / Intrusion Prevention System (IPS)**  
Network security technology that monitors traffic for malicious activity or policy violations. IDS alerts on detection, IPS actively blocks threats.

**Endpoint Detection and Response (EDR)**  
Security solution deployed on endpoints (workstations, servers) that monitors system behavior, detects threats, and enables response actions (isolation, remediation).

**Network Detection and Response (NDR)**  
Security solution that analyzes network traffic to detect threats, lateral movement, and anomalous communication patterns.

**User and Entity Behavior Analytics (UEBA)**  
Analytics technology that establishes behavioral baselines for users and entities (systems, applications), detecting deviations that may indicate compromised accounts or insider threats.

**Log Source**  
Any system, application, network device, or security control generating logs ingested by monitoring platforms. Log sources include operating systems, databases, firewalls, web servers, cloud platforms, security appliances.

**Correlation**  
The process of analyzing multiple events from different log sources to identify relationships and detect complex attack patterns not visible from individual events.

**Threat Intelligence**  
Curated information about current and emerging threats, attack techniques, and threat actor behaviors. Threat intelligence informs detection rules and enriches alert context.

**Incident**  
A confirmed security event requiring investigation and response. Incidents are classified by severity and handled per incident management procedures.

**Coverage**  
The percentage of systems, networks, and applications within monitoring scope that are actively monitored and generating logs to monitoring platforms. Coverage gaps represent blind spots.

**Retention**  
The duration for which monitoring data (logs, alerts, forensic evidence) is stored. Retention periods are determined by operational needs, regulatory requirements, and legal obligations.

**Hot Storage**  
High-performance, indexed storage for recent logs enabling real-time search, correlation, and alerting. Typically 90 days to 12 months.

**Warm/Cold Storage**  
Lower-cost archival storage for older logs with slower retrieval times. Used for compliance retention and forensic investigation of historical incidents.

**Escalation**  
The process of elevating an alert or incident to higher-tier analysts, incident response team, or management when initial response is insufficient or incident severity requires additional expertise.

**Tuning**  
The process of adjusting detection rules, baselines, and alert thresholds to reduce false positives while maintaining detection coverage. Tuning is an ongoing process based on operational feedback.

---

# Annex A: Monitoring Capability Standards (Decision Framework)

**Purpose**: This annex defines capability requirements and selection criteria for monitoring technologies. Organizations use this framework to evaluate monitoring solutions during procurement and validate existing tool capabilities.

## A.1 Monitoring Technology Categories

| Technology Category | Primary Function | Key Capabilities | Typical Deployment |
|---------------------|------------------|------------------|-------------------|
| **SIEM** | Centralized log management, correlation, alerting | Multi-source ingestion, real-time correlation, compliance reporting, forensics | Enterprise-wide, centralized |
| **IDS/IPS** | Network threat detection and prevention | Signature-based detection, protocol analysis, packet inspection | Network perimeter, critical segments |
| **EDR** | Endpoint threat detection and response | Behavioral analysis, malware detection, forensic investigation, remediation | Workstations, servers |
| **NDR** | Network behavior analysis and lateral movement detection | Traffic analysis, anomaly detection, east-west traffic monitoring | Data center, cloud environments |
| **UEBA** | User and entity behavior analytics | Machine learning baselines, anomaly detection, insider threat detection | Overlays SIEM/EDR data |
| **Log Management** | Log collection, storage, search | Scalable ingestion, long-term retention, search capabilities | Standalone or SIEM component |

## A.2 Mandatory Capabilities (All Monitoring Solutions)

Regardless of technology category, monitoring solutions SHALL provide:

**Collection**:

- Multi-protocol log ingestion (syslog, agent-based, API, file-based)
- Secure log transmission (TLS encryption, authenticated sources)
- Scalable collection (support organizational growth without architecture redesign)
- Reliable delivery (acknowledgment, retry mechanisms, queue management)

**Analysis**:

- Real-time event processing (sub-second latency for critical events)
- Search capabilities (indexed search across all collected logs)
- Filtering and querying (flexible query language for investigation)
- Correlation (ability to link related events across time and sources)

**Storage**:

- Data integrity protection (tamper-evident logging, checksums)
- Appropriate retention (hot storage ≥90 days, archival per compliance requirements)
- Backup and recovery (monitoring data included in backup strategy)

**Alerting**:

- Configurable rules (custom alert creation based on organizational needs)
- Severity classification (Critical, High, Medium, Low, Informational)
- Multi-channel notification (email, SMS, ticketing system, SOAR integration)
- Alert deduplication (prevent alert storms from single event)

**Reporting**:

- Compliance reporting (pre-built or customizable reports for regulatory requirements)
- Executive dashboards (high-level KPIs for management visibility)
- Forensic capabilities (timeline reconstruction, evidence export)

## A.3 Recommended Capabilities (Enhanced Monitoring)

Organizations SHOULD consider solutions providing:

**Advanced Correlation**:

- Multi-stage attack detection (link reconnaissance → exploitation → persistence → exfiltration)
- Behavioral analytics (UEBA for user and entity anomaly detection)
- Machine learning (adaptive baselines, automatic anomaly detection)

**Threat Intelligence Integration**:

- Automatic enrichment (correlate events with threat intel feeds)
- IOC matching (match logs against indicators of compromise)
- Threat hunting (proactive search for adversary TTPs)

**Orchestration and Automation**:

- Automated response actions (account lockout, network isolation, malware quarantine)
- Workflow automation (ticket creation, notification, escalation)
- Playbook execution (standardized response procedures)

**Cloud-Native Capabilities**:

- Cloud platform integration (AWS, Azure, GCP native log collection)
- Container monitoring (Kubernetes audit logs, pod events)
- Serverless monitoring (Lambda, Azure Functions, Cloud Functions)

## A.4 Technology Selection Criteria

When evaluating monitoring technologies, [Organization] SHALL assess:

**Technical Fit**:

- Compatibility with existing infrastructure (on-premises, cloud, hybrid)
- Log source coverage (supports organizational systems and applications)
- Scalability (handles current and projected log volumes)
- Integration capabilities (APIs, SIEM connectors, third-party tools)

**Operational Effectiveness**:

- Detection accuracy (low false positive rates, high true positive rates)
- Performance (real-time processing, acceptable search latency)
- Usability (intuitive interface, efficient workflows, minimal training required)
- Reliability (high availability, disaster recovery capabilities)

**Security**:

- Access controls (RBAC, MFA, audit logging of administrative actions)
- Data protection (encryption at rest and in transit, data masking)
- Isolation (monitoring infrastructure security hardening)

**Cost**:

- Total cost of ownership (licensing, infrastructure, staffing, training)
- Licensing model (per GB, per asset, per user, unlimited)
- Scalability cost (incremental costs as log volumes increase)

**Vendor Factors**:

- Vendor reputation and market presence
- Product maturity and roadmap
- Support quality and responsiveness
- Community and documentation
- Strategic alignment with organizational technology direction

## A.5 Capability Maturity Assessment

Organizations SHOULD assess monitoring capability maturity:

**Level 1 - Initial (Ad Hoc)**:

- Basic logging enabled, limited centralization
- Manual log review, reactive incident detection
- No baselines, detection rules, or alerting
- Minimal monitoring infrastructure

**Level 2 - Developing (Repeatable)**:

- Centralized log collection (SIEM or equivalent)
- Basic alerting rules configured
- Some baselines documented
- Incident response triggered by alerts (sometimes)

**Level 3 - Defined (Standardized)**:

- Comprehensive log source coverage (>80% critical systems)
- Documented baselines for critical systems
- Tuned detection rules with acceptable false positive rates (<30%)
- Defined response procedures and SLAs
- Quarterly detection testing

**Level 4 - Managed (Quantitatively Managed)**:

- Near-complete coverage (>95% critical systems, >80% standard systems)
- Baselines for all monitored systems
- Low false positive rates (<20% critical alerts)
- Metrics-driven optimization (MTTD, MTTR, detection rates tracked)
- Monthly tuning and continuous improvement

**Level 5 - Optimizing (Continuous Improvement)**:

- Complete coverage with minimal blind spots
- Automated baseline maintenance and anomaly detection
- Advanced correlation and threat intelligence integration
- Orchestrated response (SOAR)
- Proactive threat hunting
- Industry-leading metrics (MTTD <1 hour, MTTR <4 hours for critical incidents)

---

# Annex B: Baseline Definition Template

**Purpose**: Standardized template for documenting system, user, and application baselines per policy Section 2.2.

## B.1 Baseline Documentation Template

**Baseline ID**: [AUTO-GENERATED: BL-YYYYMMDD-NNN]  
**Creation Date**: [DD.MM.YYYY]  
**Created By**: [Name, Role]  
**Approved By**: [SOC Lead / Security Manager]  
**Review Date**: [Quarterly - Next Review: DD.MM.YYYY]  

---

## Baseline Scope

**System/Asset/User Group**:  
[Specific system hostname, IP, application name, or user group (e.g., "dc01.example.com", "Finance Department Users", "Customer Portal API")]

**Baseline Category**:  

- [ ] System Utilization (CPU, memory, disk, network)
- [ ] Access Patterns (authentication, logins, access frequency)
- [ ] Application Behavior (transactions, API calls, database queries)
- [ ] Network Traffic (protocols, destinations, bandwidth)
- [ ] Other: [Specify]

**Environment**:  

- [ ] Production
- [ ] Staging/QA
- [ ] Development
- [ ] Other: [Specify]

---

## Baseline Metric Definition

**Metric Name**: [Descriptive name - e.g., "SQL Query Rate", "User Authentication Count", "Outbound HTTPS Connections"]

**Metric Description**: [Precise definition of what is measured - e.g., "Number of SQL SELECT queries executed per minute against customer database", "Successful authentication attempts by Finance department users per hour"]

**Data Source**: [Where metric is collected - e.g., "SQL Server audit logs", "Active Directory security logs", "Firewall connection logs"]

**Collection Method**: [How metric is calculated - e.g., "SIEM aggregation of event ID 4624", "Database query: SELECT COUNT(*) FROM sys.dm_exec_requests WHERE statement_type='SELECT'"]

---

## Observation Period

**Start Date**: [DD.MM.YYYY]  
**End Date**: [DD.MM.YYYY]  
**Duration**: [X days - minimum 30 days recommended, include full business cycles]

**Business Cycle Coverage**:  

- [ ] Includes month-end processing (if applicable)
- [ ] Includes quarter-end processing (if applicable)
- [ ] Includes year-end processing (if applicable)
- [ ] Includes peak business periods (e.g., tax season, holiday shopping)
- [ ] Includes typical maintenance windows

**Exclusions**: [Document any periods excluded from baseline calculation]

- Scheduled maintenance windows: [List dates/times]
- Known incidents or anomalies: [Describe and justify exclusion]
- System downtime: [List dates/times]

---

## Statistical Profile

**Time Aggregation**: [Sample interval - e.g., "per minute", "per hour", "per day"]

**Overall Statistics**:

| Metric | Value | Notes |
|--------|-------|-------|
| **Mean (Average)** | [X.XX] | Average value across observation period |
| **Median** | [X.XX] | 50th percentile (middle value) |
| **Standard Deviation (σ)** | [X.XX] | Measure of variability |
| **Minimum** | [X.XX] | Lowest observed value (excluding outliers) |
| **Maximum** | [X.XX] | Highest observed value (excluding outliers) |
| **95th Percentile** | [X.XX] | 95% of observations below this value |
| **99th Percentile** | [X.XX] | 99% of observations below this value |

**Sample Size**: [N observations - e.g., "43,200 minutes (30 days × 24 hours × 60 minutes)"]

---

## Time-Aware Baselines (if applicable)

If behavior differs significantly by time period, document separate baselines:

**Business Hours** (Monday-Friday, 08:00-18:00 CET):

| Metric | Mean | Median | Std Dev | 95th %ile |
|--------|------|--------|---------|-----------|
| [Metric Name] | [Value] | [Value] | [Value] | [Value] |

**Off-Hours** (Monday-Friday, 18:00-08:00 CET):

| Metric | Mean | Median | Std Dev | 95th %ile |
|--------|------|--------|---------|-----------|
| [Metric Name] | [Value] | [Value] | [Value] | [Value] |

**Weekends** (Saturday-Sunday, all hours):

| Metric | Mean | Median | Std Dev | 95th %ile |
|--------|------|--------|---------|-----------|
| [Metric Name] | [Value] | [Value] | [Value] | [Value] |

---

## Threshold Derivation

**Alert Threshold Methodology**: [Describe how alert thresholds are derived from baseline]

**Example Methodologies**:

- **95th Percentile Multiplier**: Alert threshold = 95th percentile × [Multiplier - e.g., 1.5]
- **Standard Deviations**: Alert threshold = Mean + [N] × Standard Deviation
- **Absolute Value**: Alert threshold = [Fixed value] based on capacity limits or business rules
- **Rate of Change**: Alert when value increases/decreases by [X]% within [Y minutes]

**Calculated Thresholds**:

| Threshold Level | Methodology | Calculated Value | Justification |
|-----------------|-------------|------------------|---------------|
| **Warning** | [Method] | [Value] | [Why this level triggers warning] |
| **Critical** | [Method] | [Value] | [Why this level triggers critical alert] |

---

## Baseline Validation

**Known Good Period Verification**:  

- [ ] Observation period confirmed free of security incidents
- [ ] No major configuration changes during observation period
- [ ] No significant business process changes during observation period
- [ ] System performance within normal operational parameters

**Outlier Analysis**: [Describe any outliers identified and how they were handled]

**Peer Review**: [Name and role of reviewer who validated baseline accuracy]

---

## Baseline Maintenance

**Review Frequency**: Quarterly (or more frequently if business/technical changes occur)

**Update Triggers**:  

- [ ] System configuration changes (hardware, software, capacity upgrades)
- [ ] Business process changes (new workflows, organizational restructuring)
- [ ] Persistent deviations from baseline (sustained shift in normal behavior)
- [ ] Seasonal variations (adjust baselines for known seasonal patterns)

**Next Review Date**: [DD.MM.YYYY]

**Owner**: [Name and role of person responsible for baseline accuracy]

**Contact**: [Email/phone for questions about this baseline]

---

## Detection Rules Using This Baseline

**Alert Rules Configured**:

| Rule ID | Rule Name | Severity | Threshold | Status |
|---------|-----------|----------|-----------|--------|
| [RULE-001] | [Descriptive name] | [Critical/High/Medium] | [Value from Section 6] | [Active/Testing/Disabled] |

---

## Baseline Usage Notes

[Any additional context, caveats, or operational notes for SOC analysts and security team]

**Example Notes**:

- "This baseline excludes month-end batch processing (typically 28th-3rd). Separate baseline BL-20260115-002 covers month-end period."
- "Baseline reflects current 100-user organization. Re-baseline required if user count increases >20%."
- "Application version 2.5 deployed during observation period. Baseline may need adjustment if performance characteristics change in future versions."

---

**END OF BASELINE TEMPLATE**

**Baseline Status**: [ ] Draft [ ] Approved [ ] Active [ ] Expired [ ] Superseded

---

# Annex C: Quick Reference Guide

**Purpose**: One-page summary of monitoring activities for SOC analysts, system owners, and stakeholders.

## What is Monitoring?

Monitoring is the continuous observation of networks, systems, and applications to detect anomalous behavior and potential security incidents. Effective monitoring requires documented baselines, tuned detection rules, and timely response to alerts.

## Key Responsibilities

**If you are a...**

**SOC Analyst**:

- ✅ Monitor alerts 24/7, triage within SLA (5 min Critical, 15 min High)
- ✅ Investigate alerts, document findings, escalate confirmed incidents
- ✅ Report false positives for tuning

**System Owner**:

- ✅ Ensure your systems log to monitoring platforms
- ✅ Provide domain expertise during incident investigations
- ✅ Coordinate baseline establishment for your systems

**Security Engineer**:

- ✅ Establish baselines, create detection rules, tune alerts
- ✅ Manage monitoring infrastructure, integrate log sources
- ✅ Test detection effectiveness quarterly

**Executive/Management**:

- ✅ Review quarterly compliance dashboards
- ✅ Allocate resources for monitoring program
- ✅ Accept residual risks from monitoring gaps

## Alert Severity & Response Times

| Severity | Response Time | Examples |
|----------|---------------|----------|
| **Critical** | 15 minutes | Ransomware, active data exfiltration, root compromise |
| **High** | 1 hour | Malware infection, privilege escalation success |
| **Medium** | 4 hours | Anomalous behavior, policy violations |
| **Low** | 24 hours | Minor deviations, informational events |

## Monitoring Coverage Goals

- ✅ **100%** of Tier 1 (Critical) systems monitored
- ✅ **>80%** of Tier 2 (Standard) systems monitored
- ✅ **<20%** false positive rate for critical alerts
- ✅ **>90%** true positive rate for high-severity threats

## Common Monitoring Gaps (What to Watch For)

❌ **Blind Spots**: Legacy systems, cloud services with limited logging  
❌ **Alert Fatigue**: Too many false positives, analysts ignoring alerts  
❌ **Baseline Drift**: Baselines not updated, normal behavior triggers alerts  
❌ **Coverage Gaps**: Critical systems not sending logs to SIEM  
❌ **Retention Issues**: Logs purged too quickly for forensic investigation

## How to Report Issues

**False Positive**: Submit tuning request to Security Team (alert ID, reason it's FP, suggested fix)

**Monitoring Gap**: Document in quarterly coverage assessment, escalate to CISO if critical

**Incident**: Escalate to Incident Response per ISMS-POL-A.5.24-5.28

**Questions**: Contact SOC Lead or Security Manager

## Key Metrics (Track Monthly)

- **MTTD** (Mean Time to Detect): How quickly are incidents detected?
- **MTTR** (Mean Time to Respond): How quickly are incidents contained?
- **Coverage %**: What percentage of critical systems are monitored?
- **False Positive Rate**: What percentage of alerts are false positives?
- **Detection Rate**: What percentage of attacks are detected? (test quarterly)

## Quarterly Assessments

All stakeholders SHALL complete quarterly monitoring assessments:

- **ISMS-IMP-A.8.16.1**: Monitoring Infrastructure (Security Engineering)
- **ISMS-IMP-A.8.16.2**: Baselines & Detection (SOC, Security Team)
- **ISMS-IMP-A.8.16.3**: Coverage (System Owners, Network Team)
- **ISMS-IMP-A.8.16.4**: Alert Management & Response (SOC, Incident Response)
- **ISMS-IMP-A.8.16.5**: Compliance Dashboard (CISO, Management)

## Remember

> *"You can't manage what you don't measure. You can't measure what you don't monitor. You can't monitor what you don't baseline."*  
> *— Security Operations Wisdom*

**Monitoring without baselines is guessing. Alerts without response are noise. Detection without testing is hope.**

---

**For detailed information, refer to ISMS-POL-A.8.16 (Monitoring Activities Policy) and ISMS-IMP-A.8.16 (Implementation Guidance Suite).**

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Security Operations Center (SOC) Lead** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes requirements for monitoring activities. Implementation procedures, technical standards, and assessment workbooks are documented in ISMS-IMP-A.8.16.*

<!-- QA_VERIFIED: 2026-02-02 -->