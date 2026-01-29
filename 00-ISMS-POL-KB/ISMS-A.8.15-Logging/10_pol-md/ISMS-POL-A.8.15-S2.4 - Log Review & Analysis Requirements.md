# ISMS-POL-A.8.15-S2.4
## Logging - Log Review & Analysis Requirements

**Document ID**: ISMS-POL-A.8.15-S2.4  
**Title**: Logging - Log Review & Analysis Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | SOC Lead / Information Security Manager | Initial review and analysis requirements |

**Review Cycle**: Semi-annual (or upon changes to threat landscape or detection capabilities)  
**Next Review Date**: [Approval Date + 6 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Operational Review: Security Operations Center (SOC) Lead
- Technical Review: Information Security Manager / Security Architect
- Process Review: Incident Response Manager

**Distribution**: SOC analysts, security team, incident responders, IT operations  
**Related Documents**: ISMS-IMP-A.8.15.4 (Log Analysis & Review Assessment), ISMS-POL-A.5.24 (Incident Management), ISMS-POL-A.8.16 (Monitoring Activities)

---

## 2.4.1 Purpose and Scope

This section establishes requirements for **reviewing and analyzing logs** to detect security incidents, policy violations, and operational issues. As the principle states: *"Logs aren't write-only storage."*

**Core Principle**: Logging without review is security theater. Logs must be actively analyzed to provide value.

**In Scope**: Review frequency, automated analysis, alerting, investigation procedures, reporting, KPIs  
**Primary Stakeholders**: SOC Analysts, Security Engineers, Incident Responders, Management  
**Implementation Evidence**: ISMS-IMP-A.8.15.2 (Log Collection Assessment), ISMS-IMP-A.8.15.4 (Log Analysis & Review Assessment)

**Key Objectives**:
- Early detection of security incidents
- Identification of policy violations
- Detection of system anomalies and errors
- Support for forensic investigations
- Compliance verification
- Continuous improvement of detection capabilities

---

## 2.4.2 Manual Log Review Requirements

### 2.4.2.1 Daily Review

Security personnel **SHALL** conduct daily review of:

**Critical Security Logs**:
- Authentication failures (especially for administrative accounts)
- Privileged access activities
- Security tool alerts (IDS/IPS, anti-malware, DLP)
- Firewall blocks of unusual or high-severity traffic
- Failed access attempts to sensitive resources
- Configuration changes to security systems

**Review Procedures**:
- Designated SOC analyst reviews logs each business day
- Focus on anomalies, trends, and high-severity events
- Document findings (incident tickets, log review reports)
- Escalate suspicious activities per incident response procedures
- Review time: Minimum 30 minutes for small environments, 2-4 hours for large environments

### 2.4.2.2 Weekly Review

Security personnel **SHOULD** conduct weekly review of:

**Trend Analysis**:
- Authentication patterns (login times, locations, devices)
- Failed authentication trends (potential brute-force attacks)
- Resource access patterns (unusual access to sensitive data)
- Network traffic trends (bandwidth usage, unusual protocols)
- Security alert volumes (increasing alerts may indicate emerging threats)

**Administrative Activities**:
- User account creations, modifications, deletions
- Permission and role changes
- Configuration changes across infrastructure
- Privileged access usage patterns

**Review Procedures**:
- Security engineer or SOC lead reviews weekly
- Generate reports comparing current week to previous weeks
- Identify trends requiring investigation or policy adjustment
- Document findings and recommendations
- Review time: 1-2 hours

### 2.4.2.3 Monthly Review

Management and security leadership **SHOULD** conduct monthly review of:

**Strategic Analysis**:
- Overall security posture (incidents detected, response times)
- Compliance with logging policy (are all systems logging properly?)
- False positive/negative rates (quality of detection)
- Top threats detected (what attacks are being attempted?)
- Top security policy violations (user behavior issues)

**Capacity and Performance**:
- Log volume trends (planning for storage growth)
- Query performance (is log analysis responsive?)
- Missing or failing log sources (remediation needed?)

**Review Procedures**:
- CISO or Security Manager reviews monthly reports
- Present findings to management (Security Steering Committee)
- Identify process improvements or policy changes needed
- Allocate resources for remediation activities
- Review time: 1-2 hours preparation, 30-60 minute management review

### 2.4.2.4 Documentation of Manual Reviews

All manual log reviews **SHALL** be documented:

- Date and time of review
- Reviewer name
- Logs reviewed (sources, date ranges)
- Findings summary (incidents identified, trends observed)
- Actions taken (investigations initiated, escalations made)
- Sign-off (reviewer approval)

Documentation **SHALL** be retained per records retention policy (minimum 1 year).

---

## 2.4.3 Automated Log Analysis Requirements

### 2.4.3.1 SIEM/Log Management Platform

Organizations **SHOULD** implement Security Information and Event Management (SIEM) or log management platform for:

**Automated Analysis Capabilities**:
- Real-time log ingestion and parsing
- Correlation of events across multiple log sources
- Pattern detection and anomaly identification
- Alerting on suspicious activities
- Dashboard and visualization capabilities
- Search and query functionality
- Report generation

**Platform Requirements**:
- Support for standard log formats (syslog, CEF, JSON)
- Scalability to handle organizational log volume
- Integration with ticketing/incident management systems
- User authentication and role-based access control
- API for integration with other security tools

Organizations **MAY** use simpler log aggregation tools (e.g., Graylog, ELK Stack) if SIEM capabilities are not required or affordable.

### 2.4.3.2 Correlation Rules

Organizations **SHALL** implement correlation rules to detect:

**Authentication Attacks**:
- Brute force attempts (multiple failed logins from same source)
- Password spraying (attempts against many accounts with common passwords)
- Impossible travel (same user logging in from distant locations in short time)
- After-hours access (privileged access outside normal business hours)

**Privilege Abuse**:
- Unauthorized privilege escalation
- Privileged account used for non-administrative activities
- Excessive failed access attempts by authorized user

**Data Exfiltration**:
- Large data transfers to external destinations
- Unusual access patterns to sensitive data
- Database dumps or bulk exports
- Use of unauthorized file transfer methods

**Malware Indicators**:
- C2 communication attempts (outbound connections to known C2 infrastructure)
- Malware execution detected by anti-malware tools
- Unusual process execution patterns
- Registry or file system modifications typical of malware

**Policy Violations**:
- Access to prohibited website categories
- Unauthorized software installation
- Policy exception abuse
- Violation of acceptable use policy

### 2.4.3.3 Use Case Development

Organizations **SHALL** develop and maintain detection use cases:

**Use Case Components**:
- Use case name and identifier
- Threat scenario being detected (what attack or violation)
- Data sources required (which logs are needed)
- Detection logic (correlation rule, query, or analysis method)
- Expected false positive rate
- Severity/priority for alerting
- Response procedures (what to do when detected)

**Use Case Management**:
- Document all use cases in use case library
- Review use cases quarterly for effectiveness
- Update use cases based on threat intelligence
- Retire use cases that generate excessive false positives without value
- Develop new use cases for emerging threats

**Recommended Minimum Use Cases** (Organizations SHALL implement at least):
- Failed authentication threshold (10+ failures in 1 hour)
- Privileged account usage outside business hours
- New user account creation (administrative action requiring review)
- Unusual data access volume (potential exfiltration)
- Malware detection (anti-malware alerts)
- Critical system configuration changes

---

## 2.4.4 Anomaly Detection

### 2.4.4.1 Baseline Establishment

Organizations **SHOULD** establish behavioral baselines for:

**User Behavior**:
- Normal login times and locations
- Typical applications and resources accessed
- Normal data access volumes
- Usual source IP addresses/devices

**System Behavior**:
- Normal traffic volumes and patterns
- Typical resource utilization (CPU, memory, disk)
- Expected service availability
- Standard configuration states

**Baseline Process**:
- Collect data over minimum 30-day period (90 days preferred)
- Identify patterns and establish "normal" ranges
- Update baselines periodically (quarterly) to reflect legitimate changes
- Document baseline assumptions and limitations

### 2.4.4.2 Anomaly Detection Methods

Organizations **SHOULD** implement anomaly detection using:

**Statistical Methods**:
- Threshold-based detection (exceeding normal ranges)
- Standard deviation analysis (events outside 2-3 sigma)
- Time-series analysis (unusual patterns over time)

**Machine Learning**:
- Behavioral analytics (user and entity behavior analytics - UEBA)
- Clustering algorithms (identifying outliers)
- Supervised learning (trained on known good/bad patterns)

**Heuristic Analysis**:
- Rule-based detection (known patterns of suspicious behavior)
- Reputation scoring (users/systems/IPs with risk scores)

### 2.4.4.3 False Positive Management

Organizations **SHALL** manage false positives:

- Track false positive rate per use case/rule (target: <10%)
- Tune detection rules to reduce false positives
- Implement allow lists for known-good activities
- Document legitimate activities triggering false positives
- Balance false positives vs. false negatives (prefer false positives for critical threats)
- Review high false-positive alerts monthly for tuning opportunities

---

## 2.4.5 Alerting Requirements

### 2.4.5.1 Alert Generation

Automated analysis systems **SHALL** generate alerts for:

- Security incidents (malware, intrusions, policy violations)
- Suspicious activities requiring investigation
- System anomalies or failures
- Configuration changes to critical systems
- Compliance violations

### 2.4.5.2 Alert Prioritization

Alerts **SHALL** be prioritized by severity:

**Critical (P1)**: Immediate response required
- Active malware outbreak
- C2 communication detected
- Data breach in progress
- System compromise confirmed
- **Response Time**: <15 minutes

**High (P2)**: Urgent response required
- Multiple failed authentication attempts
- Privilege escalation detected
- Unusual data access patterns
- Critical system configuration change
- **Response Time**: <1 hour

**Medium (P3)**: Prompt response required
- Policy violation detected
- System anomaly detected
- Failed access attempts
- **Response Time**: <4 hours

**Low (P4)**: Routine review
- Informational events
- Low-severity policy violations
- **Response Time**: Next business day

### 2.4.5.3 Alert Delivery

Alerts **SHALL** be delivered via:

- SIEM console/dashboard (always)
- Email (for P2-P4, optional for P1)
- SMS/phone (for P1 critical alerts, optional for P2)
- Ticketing system (for tracking and assignment)
- Security orchestration platform (for automated response)

**Alert Content** SHALL include:
- Alert severity and priority
- Event description (what was detected)
- Source system and affected entities
- Timestamp of detected event
- Recommended response actions
- Link to detailed logs or investigation tools

### 2.4.5.4 Alert Escalation

Organizations **SHALL** define escalation procedures:

- **No response within SLA**: Escalate to next tier (analyst → senior analyst → manager)
- **After-hours critical alerts**: Page on-call security personnel
- **Incidents beyond SOC capability**: Escalate to Incident Response Team
- **Business-impacting incidents**: Notify management immediately

---

## 2.4.6 Investigation Procedures

### 2.4.6.1 Investigation Initiation

Investigations **SHALL** be initiated for:

- All critical (P1) and high (P2) severity alerts
- Medium (P3) alerts indicating potential security incidents
- Low (P4) alerts showing concerning patterns or trends
- User reports of suspicious activities
- External notifications (threat intelligence, vendor alerts)

### 2.4.6.2 Investigation Process

Investigators **SHALL** follow structured investigation process:

**Initial Assessment** (5-15 minutes):
1. Review alert details and supporting logs
2. Determine if alert is true positive or false positive
3. Assess initial severity and scope
4. Decide to escalate or close

**Detailed Investigation** (varies by incident):
1. Gather additional logs and evidence
2. Correlate events across multiple log sources
3. Identify timeline of events (when did it start, is it ongoing?)
4. Identify affected systems and users
5. Determine attack vector or root cause
6. Assess impact (data compromised, systems affected)
7. Document findings in incident ticket

**Response Actions**:
1. Contain threat (isolate systems, block IPs, disable accounts)
2. Eradicate threat (remove malware, close vulnerabilities)
3. Recover systems (restore from backup, rebuild)
4. Document actions taken
5. Update detection rules to catch similar incidents

### 2.4.6.3 Investigation Documentation

All investigations **SHALL** be documented:

- Incident ticket number
- Alert or trigger that initiated investigation
- Timeline of investigative actions
- Logs and evidence reviewed
- Findings and conclusions
- Response actions taken
- Lessons learned and recommendations

Documentation **SHALL** be retained per incident response policy (minimum 7 years).

---

## 2.4.7 Reporting Requirements

### 2.4.7.1 Operational Reports

SOC **SHALL** generate operational reports:

**Daily Reports** (optional, for mature SOCs):
- Alerts processed (count by severity)
- Incidents detected and investigated
- Top alert sources
- Analyst workload

**Weekly Reports**:
- Incidents summary (count, types, resolution status)
- Top threats detected
- False positive rates
- Pending investigations

**Monthly Reports**:
- Incident trends (month-over-month comparison)
- Detection effectiveness (incidents detected vs. missed)
- Response metrics (time to detect, time to respond)
- Top security risks identified
- Recommendations for improvement

### 2.4.7.2 Management Reports

Security management **SHALL** receive management reports:

**Quarterly Reports to CISO**:
- Security posture summary (incidents, trends, improvements)
- Compliance status (logging coverage, retention compliance)
- Detection capability maturity
- Resource requirements (staffing, tools, training)
- Budget requests for improvements

**Annual Reports to Executive Management**:
- Year-over-year security trends
- Major incidents and lessons learned
- ROI of logging and monitoring investments
- Regulatory compliance status
- Strategic recommendations

### 2.4.7.3 Audit Reports

For auditors, organizations **SHALL** provide:

- Evidence of regular log review (review documentation)
- Sample investigation reports
- Metrics demonstrating detection capability
- Compliance with logging policy requirements
- Gap remediation plans and progress

---

## 2.4.8 Key Performance Indicators (KPIs)

Organizations **SHALL** track KPIs to measure logging effectiveness:

**Detection Metrics**:
- **Mean Time to Detect (MTTD)**: Time from incident occurrence to detection (target: <1 hour for critical, <24 hours for high)
- **Incidents detected per month**: Volume of security incidents identified
- **False positive rate**: Percentage of alerts that are false positives (target: <10%)
- **Detection coverage**: Percentage of attack scenarios with detection capability (target: >90% for MITRE ATT&CK techniques)

**Response Metrics**:
- **Mean Time to Respond (MTTR)**: Time from detection to containment (target: <4 hours for critical)
- **Alert response rate**: Percentage of alerts investigated within SLA (target: 100%)
- **Incident closure time**: Time from detection to incident resolution (varies by incident)

**Compliance Metrics**:
- **Log source coverage**: Percentage of in-scope systems logging properly (target: 100%)
- **Log review compliance**: Percentage of required reviews completed on schedule (target: 100%)
- **Retention compliance**: Percentage of logs meeting retention requirements (target: 100%)

**Quality Metrics**:
- **Use case effectiveness**: Percentage of use cases generating valuable alerts (target: >70%)
- **Alert quality score**: Ratio of true positives to total alerts (target: >50%)
- **Log completeness**: Percentage of logs with all required fields (target: >95%)

KPIs **SHALL** be reviewed monthly by SOC Lead and reported to CISO quarterly.

---

## 2.4.9 Continuous Improvement

### 2.4.9.1 Process Improvement

Organizations **SHALL** continuously improve log review and analysis:

**Post-Incident Reviews**:
- Conduct after each significant incident
- Identify what detection worked and what didn't
- Update use cases and correlation rules
- Document lessons learned

**Quarterly Process Reviews**:
- Review detection effectiveness
- Analyze false positive trends
- Identify gaps in detection coverage
- Prioritize improvements

**Annual Capability Assessment**:
- Assess SOC maturity (people, process, technology)
- Benchmark against industry standards
- Identify capability gaps
- Develop roadmap for improvements

### 2.4.9.2 Threat Intelligence Integration

Organizations **SHOULD** integrate threat intelligence:

- Subscribe to threat intelligence feeds (commercial, government, open-source)
- Incorporate indicators of compromise (IOCs) into detection rules
- Share threat intelligence with industry peers (ISACs, sharing communities)
- Update use cases based on emerging threats
- Conduct threat hunting based on intelligence

### 2.4.9.3 Training and Exercises

Organizations **SHALL** train security personnel:

**Analyst Training**:
- Initial training for new SOC analysts (2-4 weeks)
- Ongoing training on new tools and techniques (quarterly)
- Certifications (GCIA, GCIH, Security+, vendor certifications)

**Tabletop Exercises**:
- Conduct incident response exercises using log data (semi-annual)
- Simulate various attack scenarios
- Test detection and response procedures
- Identify gaps and training needs

---

## 2.4.10 Integration with Incident Response

Organizations **SHALL** integrate log analysis with incident response:

**Incident Response Integration Points**:
- Detection triggers incident response (automated or manual escalation)
- Log analysis supports investigation (evidence gathering)
- Logs provide timeline reconstruction (what happened when)
- Logs identify scope (affected systems and users)
- Logs guide containment (what to block, isolate, or disable)
- Logs support post-incident analysis (lessons learned)

**Cross-Reference**: ISMS-POL-A.5.24 (Information Security Incident Management)

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-POL-A.8.15-S2.4 |
| **ISO 27001:2022 Control** | Annex A Control 8.15 (Logging) |
| **ISO 27002:2022 Section** | 8.15 (Event logging) |
| **Document Type** | Policy Section - Detailed Requirements |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Page Count** | [Auto-generated] |
| **Word Count** | ~3,200 words |
| **Line Count** | ~390 lines |
| **Parent Policy** | ISMS-POL-A.8.15 (Master) |
| **Related Sections** | S1, S2, S2.1, S2.2, S2.3 |
| **Implementation Evidence** | ISMS-IMP-A.8.15.2, ISMS-IMP-A.8.15.4 |

---

**END OF SECTION S2.4**

---

*"Logs aren't write-only storage. If nobody's reading them, you're just collecting expensive data."*  
— SOC Manager Wisdom

*"The best time to review logs is yesterday. The second best time is now."*  
— Incident Response Proverb

*"You can't defend what you can't see. You can't see what you don't log. You can't investigate what you don't review."*  
— ISMS Implementation Truth