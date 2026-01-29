# ISMS-POL-A.8.16-S2.1
## Monitoring Activities - Monitoring Infrastructure Requirements

**Document ID**: ISMS-POL-A.8.16-S2.1
**Title**: Monitoring Activities - Monitoring Infrastructure Requirements  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]  | Security Engineering / SOC Lead | Initial monitoring infrastructure requirements |

**Review Cycle**: Semi-annual (or upon major infrastructure changes)  
**Next Review Date**: [Approval Date + 6 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Operations Center (SOC) Lead
- Infrastructure Review: IT Operations Manager

**Distribution**: Security team, SOC analysts, security engineering, IT operations  
**Related Documents**: ISMS-IMP-A.8.16.1 (Infrastructure Assessment), ISMS-IMP-A.8.16.3 (Coverage Assessment)

---

## 2.1.1 Purpose and Scope

This section establishes **mandatory requirements** for monitoring infrastructure. These requirements ensure the organization has the technical foundation necessary to collect, analyze, store, and act upon security events.

**In Scope**: Technical infrastructure, log sources, tool capabilities, integration requirements  
**Primary Stakeholders**: Security Engineering, SOC, IT Operations  
**Implementation Evidence**: ISMS-IMP-A.8.16.1 (Infrastructure Assessment), ISMS-IMP-A.8.16.3 (Coverage Assessment)

**Feynman Reminder**: *"You can't monitor what you can't collect. You can't collect what you haven't instrumented. Instrumentation is infrastructure."*

---

## 2.1.2 Log Source Coverage

### 2.1.2.1 Mandatory Log Sources (Critical Systems)

Organizations **SHALL** collect and monitor logs from the following **critical** systems:

**Network Infrastructure:**
- Firewalls (all perimeter and internal segmentation firewalls)
- VPN concentrators and remote access gateways
- Intrusion Detection/Prevention Systems (IDS/IPS)
- Web Application Firewalls (WAF)
- DNS servers (queries, responses, anomalies)
- Network authentication services (RADIUS, TACACS+, 802.1X)
- Load balancers (where handling critical application traffic)

**Server Infrastructure:**
- Active Directory Domain Controllers (authentication, authorization, group policy changes)
- LDAP/Identity Provider servers
- Database servers (production databases containing sensitive data)
- Application servers (hosting business-critical applications)
- Web servers (externally facing or handling sensitive data)
- Email servers and gateways
- File servers (containing sensitive/regulated data)
- Backup servers and appliances

**Security Infrastructure:**
- SIEM/log management platforms themselves (meta-monitoring)
- Endpoint Detection and Response (EDR) platforms
- Antivirus/anti-malware management consoles
- Data Loss Prevention (DLP) systems
- Privileged Access Management (PAM) systems
- Web filtering solutions (per ISMS-POL-A.8.23)
- Email security gateways
- Multi-Factor Authentication (MFA) platforms

**Cloud Infrastructure:**
- Cloud platform control planes (AWS CloudTrail, Azure Activity Log, GCP Cloud Audit Logs)
- Cloud identity services (Azure AD, AWS IAM, GCP IAM)
- Cloud storage access logs (S3 access logs, Azure Blob, GCS)
- Cloud network logs (VPC Flow Logs, Network Security Group logs)
- Cloud-native security services (GuardDuty, Security Center, Security Command Center)

**Coverage Target**: 100% of critical systems MUST be monitored.

### 2.1.2.2 Standard Log Sources (Non-Critical Systems)

Organizations **SHOULD** collect and monitor logs from:

**Endpoint Systems:**
- Workstations (Windows Event Logs, macOS Unified Logs, Linux syslog)
- Laptops (especially for privileged users)
- Mobile devices (where MDM provides log access)
- Virtual desktop infrastructure (VDI) sessions

**Application Systems:**
- Custom business applications
- Third-party SaaS application logs (O365, Salesforce, etc.)
- Development/staging environments (reduced retention acceptable)
- Collaboration platforms (SharePoint, Teams, Slack)

**Coverage Target**: >80% of standard systems SHOULD be monitored.

### 2.1.2.3 Log Source Exclusions

Organizations **MAY** exclude from monitoring (with documented risk acceptance):

- Development/test environments (unless containing production-like data)
- Isolated lab environments (air-gapped networks)
- End-of-life systems scheduled for decommissioning within 90 days
- Systems with no network connectivity and no sensitive data
- Personal devices (BYOD) not accessing corporate resources

**All exclusions MUST be documented in ISMS-IMP-A.8.16.3 with risk justification.**

---

## 2.1.3 Event Types to Collect

### 2.1.3.1 Authentication and Authorization Events

Organizations **SHALL** collect:

- Successful authentication (login success)
- Failed authentication attempts (login failures)
- Account lockouts
- Password changes/resets
- Privileged access grants and use (sudo, runas, privilege escalation)
- Role/group membership changes
- Multi-factor authentication challenges and outcomes
- Single Sign-On (SSO) events
- Service account authentication
- API key/token usage

### 2.1.3.2 Network Events

Organizations **SHALL** collect:

- Firewall allow/deny decisions
- VPN connections (establish, disconnect)
- Network flow data (NetFlow, sFlow, IPFIX)
- DNS queries and responses (especially to external domains)
- IDS/IPS alerts and blocks
- Network connection establishments (especially from servers)
- Port scans detected
- Protocol violations

### 2.1.3.3 System Events

Organizations **SHALL** collect:

- System startups and shutdowns
- Service starts/stops (especially critical services)
- Process executions (especially from unusual locations)
- File integrity changes (critical system files, configuration files)
- Software installations and uninstallations
- System configuration changes
- Scheduled task creation/modification
- Registry changes (Windows critical paths)

### 2.1.3.4 Application Events

Organizations **SHALL** collect:

- Application errors and crashes
- Database query errors (especially SQL injection attempts)
- Access to sensitive data
- Data exports and bulk downloads
- Application configuration changes
- API calls (especially to sensitive endpoints)
- File uploads/downloads

### 2.1.3.5 Security Events

Organizations **SHALL** collect:

- Antivirus/anti-malware alerts and detections
- IDS/IPS signature matches
- EDR alerts (behavioral detections, threat hunting findings)
- DLP violations
- Web filtering blocks
- Email security events (spam, phishing, malware)
- Vulnerability scan findings
- Security policy violations

---

## 2.1.4 Monitoring Tool Capabilities

### 2.1.4.1 Core SIEM/Monitoring Platform Requirements

The organization's primary monitoring platform **SHALL** provide:

**Log Collection:**
- Support for common log formats (Syslog, Windows Event Logs, JSON, CEF)
- Agent-based and agentless collection methods
- Encrypted log transmission (TLS/SSL)
- Reliable delivery with acknowledgment mechanisms
- Buffering and retry logic for network disruptions

**Parsing and Normalization:**
- Parsing of common log formats without extensive custom development
- Normalization to common taxonomy (field mapping)
- Support for custom parsers when needed
- Regular expression and pattern matching capabilities

**Storage and Indexing:**
- Compressed storage to optimize capacity
- Indexed storage for fast search/retrieval
- Support for hot/warm/cold storage tiers (cost optimization)
- Retention policy enforcement

**Search and Analysis:**
- Full-text search capabilities
- Field-based filtering and aggregation
- Statistical analysis functions (count, sum, average, percentile)
- Time-series analysis
- Support for complex queries (Boolean logic, wildcards, regex)

**Alerting:**
- Real-time and scheduled alert generation
- Threshold-based alerting
- Anomaly-based alerting
- Alert suppression and deduplication
- Alert enrichment with context

**Visualization:**
- Dashboards with real-time updates
- Customizable charts and graphs
- Drill-down capabilities
- Time range selection
- Role-based dashboard access

### 2.1.4.2 Correlation and Detection Engine

The monitoring platform **SHALL** support:

- Multi-event correlation (e.g., "failed login followed by successful login from different IP")
- Time-window based correlation
- Field-based correlation (by user, IP, host, etc.)
- Threat intelligence integration (IOC matching)
- Behavioral baselining (where feasible)
- Use case/detection rule management
- Rule version control and change tracking

### 2.1.4.3 Integration Capabilities

The monitoring platform **SHALL** support integration with:

- Threat intelligence platforms (TAXII, STIX, custom feeds)
- Incident response platforms (ticketing, SOAR)
- Asset management systems (CMDB)
- Identity management systems (Active Directory, LDAP)
- Cloud platforms (native integrations or APIs)
- Third-party security tools (EDR, vulnerability scanners)

---

## 2.1.5 Data Collection Architecture

### 2.1.5.1 Log Collection Methods

Organizations **SHALL** implement appropriate collection methods:

**Agent-Based Collection:**
- For endpoints and servers where agents can be deployed
- Preferred for Windows/Linux servers and workstations
- Provides buffering, filtering, and pre-processing at source

**Agentless Collection:**
- For network devices and systems where agents cannot be deployed
- Syslog for network devices (routers, switches, firewalls)
- APIs for cloud services and SaaS applications
- WMI/WinRM for Windows systems (if agent not feasible)

**Network Tap/SPAN Collection:**
- For network flow data (NetFlow, IPFIX)
- For passive IDS/IPS monitoring
- For protocol analysis where in-line inspection isn't needed

### 2.1.5.2 Collection Infrastructure

Organizations **SHALL**:

- Deploy log collectors in each major network segment (avoid single points of failure)
- Size collectors appropriately for expected log volume (events per second - EPS)
- Implement buffering to handle temporary spikes in log volume
- Monitor collector health and alert on failures
- Secure collector communications (TLS, certificate validation)

### 2.1.5.3 Bandwidth and Network Considerations

Organizations **SHALL**:

- Assess network bandwidth impact of log collection
- Implement log filtering at source where appropriate (reduce noise before transmission)
- Schedule large log transfers during off-peak hours where feasible
- Monitor bandwidth usage by log sources

---

## 2.1.6 Log Storage and Retention

### 2.1.6.1 Storage Infrastructure

Organizations **SHALL**:

- Size storage to accommodate retention requirements (see ISMS-POL-A.8.16-S2.4)
- Implement storage tiering (hot/warm/cold) for cost optimization
- Protect stored logs from unauthorized modification (write-once-read-many where feasible)
- Implement access controls on log storage
- Encrypt logs at rest (especially for regulatory compliance)
- Plan for storage capacity growth (annual capacity planning)

### 2.1.6.2 Performance Requirements

Organizations **SHALL** ensure:

- Search performance: <10 seconds for typical queries on hot storage (last 30-90 days)
- Indexing performance: Lag time <5 minutes from log generation to searchability
- Dashboard load time: <5 seconds for standard dashboards
- Alert generation latency: <2 minutes from event to alert (real-time alerts)

---

## 2.1.7 High Availability and Resilience

### 2.1.7.1 Availability Requirements

Monitoring infrastructure **SHALL**:

- Achieve 99.5% uptime for critical monitoring functions (acceptable: ~3.6 hours downtime/month)
- Implement redundancy for critical components (no single points of failure)
- Survive failure of any single component without data loss
- Support maintenance windows with minimal service impact

### 2.1.7.2 Disaster Recovery

Organizations **SHALL**:

- Back up monitoring infrastructure configurations regularly (daily minimum)
- Document recovery procedures for monitoring infrastructure
- Test disaster recovery at least annually
- Define Recovery Time Objective (RTO): <24 hours for monitoring restoration
- Define Recovery Point Objective (RPO): <1 hour for log data loss

### 2.1.7.3 Fail-Safe Behaviors

Organizations **SHALL** define fail-safe behaviors:

**Log Collection Failure:**
- Log sources SHALL buffer logs locally when collector is unavailable
- Alert when buffer reaches 80% capacity
- Prioritize critical log sources during collection recovery

**SIEM/Platform Failure:**
- Define manual monitoring procedures for critical alerts
- Maintain secondary alerting capability (e.g., endpoint EDR alerts still function)
- Prioritize platform restoration in incident response procedures

---

## 2.1.8 Security of Monitoring Infrastructure

### 2.1.8.1 Access Controls

Organizations **SHALL**:

- Implement role-based access control (RBAC) on monitoring platforms
- Restrict privileged access (administrative rights) to authorized personnel
- Require multi-factor authentication (MFA) for monitoring platform access
- Log all administrative actions on monitoring platforms (meta-monitoring)
- Review access permissions quarterly

**Role Examples:**
- **SOC Analyst (Tier 1)**: View dashboards, search logs, create/update alerts (own assignments)
- **SOC Analyst (Tier 2/3)**: All Tier 1 + create detection rules, tune alerts, investigate incidents
- **Security Engineer**: All Tier 2/3 + modify infrastructure, install integrations, manage users
- **CISO/Manager**: View dashboards and reports, no day-to-day operational access unless needed

### 2.1.8.2 Log Integrity

Organizations **SHALL**:

- Protect logs from unauthorized modification or deletion
- Implement cryptographic hashing or digital signatures where feasible
- Restrict delete permissions (delete only for data retention compliance)
- Audit log access and exports
- Alert on suspicious log access patterns (bulk exports, unusual queries)

### 2.1.8.3 Segregation of Duties

Organizations **SHALL**:

- Separate monitoring platform administrative access from system administrative access where feasible
- Prevent administrators from deleting logs of their own activities
- Require dual approval for monitoring platform configuration changes (where feasible)
- Audit privileged actions independently

---

## 2.1.9 Performance and Scalability

### 2.1.9.1 Capacity Planning

Organizations **SHALL**:

- Measure current log volume (events per second - EPS, gigabytes per day)
- Project future growth based on business expansion and new log sources
- Conduct annual capacity planning exercises
- Monitor infrastructure utilization (CPU, memory, disk I/O, network)
- Alert when utilization exceeds 70% (warning) or 85% (critical)

### 2.1.9.2 Scalability Architecture

Organizations **SHOULD**:

- Design monitoring infrastructure for horizontal scalability (add nodes as volume grows)
- Implement distributed processing where supported by platform
- Separate search/query workloads from indexing workloads (where feasible)
- Use load balancing for log collection and user access

### 2.1.9.3 Performance Monitoring

Organizations **SHALL**:

- Monitor monitoring infrastructure performance (meta-monitoring)
- Track key performance indicators:
  - Indexing lag time
  - Search query response time
  - Alert generation latency
  - Dashboard load time
  - Log loss rate (should be 0%)
- Alert when performance degrades below acceptable thresholds

---

## 2.1.10 Integration with Security Ecosystem

### 2.1.10.1 Threat Intelligence Integration

Monitoring infrastructure **SHALL** integrate with:

- Commercial threat intelligence feeds (vendor-provided)
- Open-source threat intelligence (OSINT)
- Industry-specific threat sharing communities (ISACs)
- Internal threat intelligence (indicators from previous incidents)

Integration **SHALL** support:
- Automated IOC enrichment (IP reputation, domain categorization)
- IOC matching against logs (alerts when IOCs detected)
- Threat feed quality metrics (hit rate, false positive rate)

### 2.1.10.2 Incident Response Integration

Monitoring infrastructure **SHALL** integrate with:

- Ticketing systems (automatic ticket creation for confirmed incidents)
- Security Orchestration, Automation and Response (SOAR) platforms
- Case management systems
- Communication platforms (Slack, Teams, email) for alert notifications

### 2.1.10.3 Asset and Identity Context

Monitoring infrastructure **SHOULD** integrate with:

- Asset management (CMDB) for system owner, criticality, location context
- Identity management (Active Directory, HR systems) for user context
- Vulnerability management for risk scoring alerts based on exploitable vulnerabilities

**Benefit**: Enriched alerts with context reduce triage time and improve prioritization.

---

## 2.1.11 Monitoring Infrastructure Metrics

Organizations **SHALL** measure infrastructure effectiveness through:

**Availability Metrics:**
- Uptime percentage (target: >99.5%)
- Mean Time Between Failures (MTBF)
- Mean Time To Repair (MTTR)

**Performance Metrics:**
- Average indexing lag (target: <5 minutes)
- Average search query time (target: <10 seconds for hot data)
- Dashboard load time (target: <5 seconds)
- Alert generation latency (target: <2 minutes)

**Coverage Metrics:**
- Percentage of critical systems monitored (target: 100%)
- Percentage of all systems monitored (target: >80%)
- Number of log sources sending logs
- Log loss rate (target: 0%)

**Capacity Metrics:**
- Events per second (EPS) - current and peak
- Storage utilization percentage
- Storage days remaining at current growth rate
- Network bandwidth utilization for log collection

Metrics shall be reviewed **monthly** by Security Engineering and reported to CISO **quarterly**.

---

## 2.1.12 Continuous Improvement

Organizations **SHALL**:

- Review monitoring infrastructure coverage quarterly (identify gaps)
- Conduct annual capacity planning and infrastructure scaling
- Evaluate new monitoring technologies and capabilities annually
- Optimize detection rules and correlation logic to reduce false positives
- Review and update log source configurations when systems change
- Participate in industry forums for monitoring best practices

---

## 2.1.13 Exceptions to Infrastructure Requirements

**General Rule**: Exceptions to monitoring infrastructure requirements are **discouraged** as they create blind spots.

Where technical or business constraints prevent full compliance, organizations **SHALL**:

- Document exception with business/technical justification
- Identify compensating controls (e.g., if system cannot be monitored, increase physical security)
- Require Security Team approval for all monitoring exceptions
- Review exceptions quarterly for continued necessity
- Establish remediation timeline to achieve full compliance

**Example Valid Exception**: Legacy system that cannot generate logs in any standard format, scheduled for replacement in 6 months. Compensating control: Enhanced network monitoring of all traffic to/from legacy system.

**Example Invalid Exception**: "We don't want to monitor that system because logs are expensive." (Monitoring is a security control, not optional based on cost preference.)

---

## 2.1.14 Implementation Validation

Compliance with monitoring infrastructure requirements is validated through:

- **ISMS-IMP-A.8.16.1** (Infrastructure Assessment) - Documents monitoring tools, log sources, capabilities
- **ISMS-IMP-A.8.16.3** (Coverage Assessment) - Validates which systems are monitored, identifies gaps
- Annual architecture review by Security Team
- Quarterly coverage gap analysis
- External audit during ISO 27001 certification

**Evidence Required:**
- Monitoring infrastructure architecture diagram
- List of all log sources with collection status
- Monitoring platform configuration exports
- Integration documentation
- Performance metrics dashboard
- Capacity planning documentation
- Exception documentation with approvals

---

**END OF DOCUMENT**

---

## Related Documents in Framework

- **ISMS-POL-A.8.16-S1** (Purpose, Scope, Definitions) - Foundation and terminology
- **ISMS-POL-A.8.16-S2** (Requirements Overview) - Framework overview
- **ISMS-POL-A.8.16-S2.2** (Baseline & Detection) - How to detect anomalies on collected data
- **ISMS-POL-A.8.16-S2.3** (Alert Management) - What to do when monitoring detects something
- **ISMS-POL-A.8.16-S2.4** (Retention) - How long to keep monitoring data
- **ISMS-IMP-A.8.16.1** (Implementation Assessment) - Assessment workbook for this section
- **ISMS-IMP-A.8.16.3** (Coverage Assessment) - Gap analysis workbook

---

*"Infrastructure is not glamorous, but without it, everything else is theater."*  
*—Unknown Systems Engineer*