# ISMS-POL-A.8.9-S2.3
## Configuration Management - Configuration Monitoring Requirements

**Document ID**: ISMS-POL-A.8.9-S2.3  
**Title**: Configuration Monitoring Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Configuration Manager / Security Operations Manager | Initial configuration monitoring requirements |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Date + 1 year]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Operations Center (SOC) Manager / Configuration Manager
- Operations Review: IT Operations Manager / Infrastructure Lead

**Distribution**: SOC team, configuration management team, system administrators, security engineers, DevOps team  
**Related Documents**: ISMS-POL-A.8.9-S1 (Definitions), ISMS-POL-A.8.9-S2.1 (Baseline Requirements), ISMS-POL-A.8.9-S2.2 (Change Control), ISMS-IMP-A.8.9.3 (Monitoring Assessment)

---

## 2.3.1 Purpose

This document defines **mandatory and recommended requirements** for continuously monitoring IT configurations to detect deviations from approved baselines, unauthorized changes, and security drift. Configuration monitoring serves as the operational verification layer ensuring that:
- **Baselines remain accurate** - Documentation matches reality
- **Changes are tracked** - All modifications are detected and correlated with change records
- **Drift is detected** - Unauthorized or accidental deviations are identified rapidly
- **Security posture is maintained** - Hardening standards remain effective over time
- **Audit evidence is generated** - Compliance can be demonstrated continuously

**The Anti-Pattern**: Organizations that deploy configuration monitoring tools, generate 10,000 alerts per day, ignore 99.9% of them, and declare "monitoring is implemented." Monitoring without intelligent alerting and response is theater.

**The Feynman Standard**: *"If your monitoring system alerts on configuration drift but nobody looks at the alerts, you don't have monitoring—you have a log aggregator with delusions of grandeur. Real monitoring drives action."*

---

## 2.3.2 Configuration Monitoring Framework

### 2.3.2.1 Monitoring Objectives

**MUST Requirements**:
- [Organization] MUST implement configuration monitoring to achieve the following objectives:
  - **Drift Detection** - Identify deviations from approved configuration baselines
  - **Change Correlation** - Verify that detected changes correspond to approved change requests
  - **Security Compliance** - Confirm adherence to security hardening standards
  - **Incident Investigation** - Provide forensic evidence for security incidents
  - **Audit Support** - Generate compliance evidence for internal and external audits
- Monitoring objectives MUST be documented and aligned with organizational risk management

---

### 2.3.2.2 Monitoring Scope

**MUST Requirements**:
- Configuration monitoring MUST cover all asset types defined in ISMS-POL-A.8.9-S2.1 where technically feasible
- The scope MUST prioritize coverage based on:
  - **Asset criticality** - Critical and High criticality assets first
  - **Risk exposure** - Internet-facing, high-value targets
  - **Regulatory requirements** - Assets subject to compliance mandates
  - **Security sensitivity** - Systems processing sensitive data
- Assets excluded from monitoring MUST be documented with justification

**SHOULD Requirements**:
- Monitoring coverage SHOULD aim for ≥95% of Critical assets, ≥85% of High criticality assets
- Coverage gaps SHOULD be tracked and remediation plans established
- Monitoring scope SHOULD be reviewed quarterly and adjusted based on risk changes

**MAY Requirements**:
- [Organization] MAY implement differentiated monitoring intensity (e.g., hourly for critical, daily for medium)
- Monitoring MAY include both agent-based and agentless approaches

---

## 2.3.3 Drift Detection

### 2.3.3.1 Configuration Drift Definition

**Drift** is any deviation between the actual configuration state of an asset and its approved baseline configuration, whether intentional, accidental, or malicious.

**Categories of Drift**:
- **Authorized Drift** - Result of approved change, baseline not yet updated
- **Undocumented Drift** - Change made without following change control process
- **Malicious Drift** - Unauthorized modification (potential security incident)
- **Configuration Decay** - Gradual degradation over time (patches missed, accounts not removed)

---

### 2.3.3.2 Drift Detection Requirements

**MUST Requirements**:
- [Organization] MUST implement automated drift detection for:
  - Operating system configurations
  - Network device configurations
  - Security appliance configurations
  - Application configurations (where feasible)
  - Database configurations (where feasible)
  - Cloud service configurations
- Drift detection MUST compare current state against documented baselines
- Detected drift MUST be classified by severity:
  - **Critical** - Security control disabled, unauthorized administrative access created
  - **High** - Significant deviation from hardening standard, regulatory non-compliance
  - **Medium** - Moderate deviation, potential security impact
  - **Low** - Minor cosmetic changes, no security impact
- Critical and High severity drift MUST trigger immediate alerts

**SHOULD Requirements**:
- Drift detection SHOULD occur at frequencies appropriate to asset criticality:
  - Critical assets: Continuous or hourly
  - High criticality: Daily
  - Medium criticality: Weekly
  - Low criticality: Monthly
- Drift detection SHOULD identify specific configuration parameters that changed
- Drift alerts SHOULD include:
  - Asset identification
  - Parameter(s) changed
  - Expected vs. actual value
  - Detection timestamp
  - Change correlation (if linked to approved change)

**MAY Requirements**:
- [Organization] MAY implement real-time drift detection for critical security controls
- Drift detection MAY leverage file integrity monitoring (FIM) tools
- [Organization] MAY use configuration management tools (Ansible, Puppet, Chef, etc.) for drift detection

**Technology Examples** (vendor-agnostic capabilities):
- **File Integrity Monitoring**: OSSEC, Tripwire, AIDE, Samhain
- **Configuration Compliance Scanners**: Qualys Policy Compliance, Tenable.sc, CIS-CAT Pro
- **Cloud-Native Drift Detection**: AWS Config, Azure Policy, GCP Security Command Center
- **Configuration Management Platforms**: Ansible (Tower/AWX), Puppet, Chef, SaltStack
- **Custom Scripts**: PowerShell DSC, Python scripts, Bash comparison tools

---

### 2.3.3.3 Drift Remediation

**MUST Requirements**:
- All detected drift MUST be investigated to determine:
  - Root cause (authorized change, unauthorized change, system failure, malicious activity)
  - Impact (security, operational, compliance)
  - Required action (accept, remediate, update baseline)
- Critical and High severity drift MUST be remediated or escalated within defined SLAs:
  - **Critical drift**: 4 hours
  - **High drift**: 24 hours
  - **Medium drift**: 5 business days
  - **Low drift**: 30 days
- Drift that represents a security incident MUST be escalated to the Security Operations Center (SOC) or incident response team
- Remediation actions MUST be documented in the monitoring system or incident management system

**SHOULD Requirements**:
- Authorized drift (from approved changes) SHOULD trigger baseline updates
- Undocumented drift SHOULD trigger review of change control compliance
- Repeated drift on the same asset SHOULD trigger root cause analysis
- Remediation SHOULD be verified through re-scan or validation

**MAY Requirements**:
- [Organization] MAY implement automated remediation for specific drift types (e.g., re-apply baseline configuration)
- Automated remediation MAY include approval workflows for High and Critical changes

**The Cargo Cult Warning**: *Automatically remediating all drift sounds great until your automated system reverts a legitimate emergency change at 3 AM and takes down production. Automation requires intelligence.*

---

## 2.3.4 Continuous Monitoring

### 2.3.4.1 Real-Time vs. Scheduled Monitoring

**MUST Requirements**:
- [Organization] MUST define which monitoring activities are real-time vs. scheduled based on risk and feasibility
- The monitoring approach MUST balance security objectives with operational overhead
- Monitoring frequency MUST be documented in the monitoring strategy

**SHOULD Requirements**:
- Real-time monitoring SHOULD be implemented for:
  - Critical security controls (firewall rules, access controls, encryption settings)
  - Internet-facing systems
  - High-value targets (databases, identity systems, financial systems)
- Scheduled monitoring SHOULD be used for:
  - Comprehensive baseline comparisons
  - Low-criticality systems
  - Resource-intensive scans

**MAY Requirements**:
- [Organization] MAY adjust monitoring frequency dynamically based on threat intelligence or incident indicators

---

### 2.3.4.2 Monitoring Integration with SIEM and Logging

**MUST Requirements**:
- Configuration monitoring MUST generate logs for audit and forensic purposes
- Logs MUST include:
  - Configuration changes detected
  - Drift alerts generated
  - Remediation actions taken
  - Baseline updates
- Logs MUST be retained according to [Organization]'s log retention policy (minimum 90 days, 1 year recommended)

**SHOULD Requirements**:
- Configuration monitoring SHOULD integrate with the Security Information and Event Management (SIEM) system
- SIEM correlation SHOULD link configuration changes to:
  - Security events (failed logins, privilege escalations)
  - Change management records
  - Incident tickets
- Configuration drift SHOULD be treated as a security indicator in incident investigations

**MAY Requirements**:
- [Organization] MAY implement alerting rules in SIEM for specific drift patterns
- SIEM MAY automate ticket creation for detected drift

---

## 2.3.5 Configuration Auditing

### 2.3.5.1 Periodic Configuration Audits

**MUST Requirements**:
- [Organization] MUST conduct periodic configuration audits to verify:
  - Baselines are accurate and up-to-date
  - Monitoring systems are functioning correctly
  - Drift remediation is occurring within SLAs
  - Compliance with security hardening standards
- Audit frequency MUST be at least:
  - Critical assets: Quarterly
  - High criticality: Semi-annually
  - Medium/Low criticality: Annually
- Audit findings MUST be documented and tracked to resolution

**SHOULD Requirements**:
- Configuration audits SHOULD be performed by personnel independent of system administration (e.g., security team, internal audit)
- Audits SHOULD include both automated scans and manual sampling
- Audit reports SHOULD be reviewed by senior management (CISO, CTO)

**MAY Requirements**:
- [Organization] MAY engage external auditors for independent configuration assessments
- Audits MAY focus on specific areas (e.g., "firewall rule audit," "cloud configuration audit")

---

### 2.3.5.2 Automated Compliance Scanning

**SHOULD Requirements**:
- [Organization] SHOULD implement automated compliance scanning tools to verify adherence to:
  - CIS Benchmarks
  - DISA STIGs (if applicable)
  - Industry standards (PCI DSS, HIPAA, etc.)
  - Organizational security policies
- Compliance scans SHOULD generate reports showing:
  - Overall compliance percentage
  - Failed controls
  - Remediation recommendations
  - Trend analysis (compliance over time)
- Scan results SHOULD be integrated with vulnerability management programs

**MAY Requirements**:
- Compliance scanning MAY be integrated into CI/CD pipelines for Infrastructure as Code
- Scan failures MAY block deployments or trigger approval workflows

---

## 2.3.6 Monitoring Rules and Alerting

### 2.3.6.1 Alert Configuration

**MUST Requirements**:
- [Organization] MUST define monitoring rules that specify:
  - Configuration parameters to monitor
  - Expected values or acceptable ranges
  - Alert thresholds (when to generate alerts)
  - Alert severity levels
  - Notification recipients
  - Escalation procedures
- Monitoring rules MUST be documented and version-controlled
- Rule changes MUST follow change control procedures

**SHOULD Requirements**:
- Monitoring rules SHOULD be based on:
  - Security hardening standards
  - Regulatory requirements
  - Organizational risk assessment
  - Historical incident data
- Rules SHOULD be tuned to minimize false positives while ensuring critical drift is detected
- Rules SHOULD be reviewed and updated at least annually

**MAY Requirements**:
- [Organization] MAY implement dynamic thresholds based on historical baselines
- Rules MAY incorporate threat intelligence (e.g., alert on configurations matching known attack patterns)

---

### 2.3.6.2 Alert Severity Classification

**MUST Requirements**:
- All configuration monitoring alerts MUST be assigned a severity level:
  - **Critical** - Security control failure, imminent breach risk, regulatory violation
  - **High** - Significant deviation from security baseline, potential exploit vector
  - **Medium** - Moderate deviation, increased risk but not immediately exploitable
  - **Low** - Minor deviation, informational or optimization opportunity
- Severity classification MUST be consistent with [Organization]'s incident severity definitions

---

### 2.3.6.3 Alert Notification and Escalation

**MUST Requirements**:
- Alerts MUST be delivered through appropriate channels:
  - **Critical alerts**: Immediate notification via multiple channels (email, SMS, SIEM, ticketing)
  - **High alerts**: Real-time notification via email and SIEM
  - **Medium alerts**: Email and daily summary reports
  - **Low alerts**: Weekly summary reports
- Alert recipients MUST be defined based on:
  - Asset ownership
  - On-call rotations
  - Escalation hierarchy
- Unresolved Critical alerts MUST escalate after defined timeframes (e.g., 1 hour to SOC manager, 4 hours to CISO)

**SHOULD Requirements**:
- Alert notifications SHOULD include actionable information:
  - Asset identification and location
  - Specific configuration drift detected
  - Business impact assessment
  - Recommended remediation steps
  - Links to relevant runbooks or procedures
- Alert fatigue SHOULD be actively managed through tuning and consolidation
- [Organization] SHOULD track alert response metrics (time to acknowledgment, time to resolution)

**MAY Requirements**:
- [Organization] MAY implement intelligent alerting (e.g., suppress low-priority alerts during change windows)
- Alerts MAY integrate with collaboration tools (Slack, Microsoft Teams) for rapid response

**The Reality Check**: *If your monitoring system sends 500 alerts per day and the team ignores 499 of them, you have trained your team to ignore alerts. Quality > Quantity.*

---

## 2.3.7 Response Procedures

### 2.3.7.1 Alert Triage and Investigation

**MUST Requirements**:
- All configuration monitoring alerts MUST be triaged to determine:
  - Validity (true positive vs. false positive)
  - Root cause (authorized change, unauthorized change, system failure, attack)
  - Impact (security, compliance, operational)
  - Urgency (immediate remediation required or can be scheduled)
- Triage MUST occur within defined timeframes:
  - Critical alerts: 30 minutes
  - High alerts: 2 hours
  - Medium alerts: 24 hours
  - Low alerts: 5 business days
- Triage results MUST be documented in the monitoring or ticketing system

**SHOULD Requirements**:
- Triage SHOULD be performed by qualified personnel (SOC analysts, system administrators, security engineers)
- Triage SHOULD leverage automation where possible (e.g., automatic correlation with change management records)
- Repeated false positives SHOULD trigger monitoring rule tuning

---

### 2.3.7.2 Incident Escalation

**MUST Requirements**:
- Configuration drift that indicates a security incident MUST be escalated to the Security Incident Response Team
- Escalation criteria MUST include:
  - Unauthorized administrative access created
  - Security controls disabled
  - Malware or backdoor indicators
  - Data exfiltration indicators
  - Indicators of Compromise (IOCs) from threat intelligence
- Escalated incidents MUST follow [Organization]'s incident response procedures

**SHOULD Requirements**:
- Incident escalation SHOULD include all relevant context:
  - Timeline of configuration changes
  - Related alerts or events
  - Affected systems and data
  - Potential indicators of lateral movement

---

## 2.3.8 Reporting Requirements

### 2.3.8.1 Operational Reporting

**MUST Requirements**:
- [Organization] MUST generate operational reports on configuration monitoring including:
  - **Drift Summary** - Count and severity of drift detected
  - **Coverage Report** - Percentage of assets monitored
  - **Alert Statistics** - Alerts generated, acknowledged, resolved
  - **SLA Compliance** - Remediation within defined timeframes
  - **Trend Analysis** - Drift patterns over time
- Reports MUST be generated at least monthly
- Reports MUST be reviewed by the Configuration Manager and Security Operations Manager

**SHOULD Requirements**:
- Operational reports SHOULD be automated
- Reports SHOULD include visualizations (charts, graphs) for trend identification
- Reports SHOULD highlight anomalies or emerging issues

---

### 2.3.8.2 Compliance Reporting

**MUST Requirements**:
- [Organization] MUST generate compliance reports for:
  - Internal audits
  - External audits (ISO 27001, SOC 2, industry regulations)
  - Regulatory inquiries
- Compliance reports MUST demonstrate:
  - Baseline adherence across asset inventory
  - Configuration hardening compliance (CIS, STIG, vendor standards)
  - Change correlation (detected changes match approved changes)
  - Remediation effectiveness (drift resolved within SLAs)
- Compliance reports MUST be retained according to regulatory and audit requirements

**SHOULD Requirements**:
- Compliance reports SHOULD be generated on-demand (not only during audit periods)
- Reports SHOULD provide evidence at multiple levels (summary and detailed)
- [Organization] SHOULD maintain a "compliance evidence repository" for audit readiness

---

### 2.3.8.3 Executive Reporting

**SHOULD Requirements**:
- [Organization] SHOULD provide executive-level reporting on configuration monitoring including:
  - **Overall Configuration Health** - Percentage of assets in compliance
  - **Top Risk Areas** - Assets or configurations with highest drift or non-compliance
  - **Improvement Trends** - Reduction in drift over time, improved remediation SLAs
  - **Resource Allocation** - Monitoring coverage gaps and recommended investments
- Executive reports SHOULD be presented quarterly to senior leadership (CISO, CTO, CIO)

---

## 2.3.9 Monitoring Tool Requirements

### 2.3.9.1 Capabilities

**MUST Requirements**:
- Configuration monitoring tools MUST provide the following capabilities:
  - **Baseline Comparison** - Compare current state to documented baselines
  - **Change Detection** - Identify what changed, when, and (if possible) by whom
  - **Alerting** - Generate alerts based on configurable rules
  - **Reporting** - Produce operational and compliance reports
  - **Audit Logging** - Maintain tamper-evident logs of monitoring activities
- Tools MUST support the asset types in [Organization]'s environment

**SHOULD Requirements**:
- Monitoring tools SHOULD provide:
  - API integration for automation and orchestration
  - Role-based access control (RBAC) for tool administration
  - Dashboard visualizations for real-time status
  - Integration with CMDB, SIEM, and ticketing systems
  - Scalability to support asset growth
- Tools SHOULD support both agent-based and agentless monitoring approaches

**MAY Requirements**:
- Tools MAY include automated remediation capabilities
- Tools MAY support multi-cloud and hybrid environments

**Technology Neutrality Note**: 
Common configuration monitoring capabilities are provided by: ServiceNow CMDB, BMC Helix Discovery, Device42, Lansweeper, Ansible Tower/AWX, Puppet Enterprise, Chef Automate, SaltStack, Tripwire Enterprise, Qualys Policy Compliance, Tenable.sc, AWS Config, Azure Policy, GCP Security Command Center, CIS-CAT Pro, OpenSCAP, Microsoft SCCM/Intune, and custom scripts. The requirement is for CAPABILITY, not specific vendor tools.

---

### 2.3.9.2 Tool Management

**MUST Requirements**:
- Configuration monitoring tools MUST be maintained and updated regularly
- Tools MUST be configured securely (hardened, least privilege access)
- Tool credentials MUST be protected according to privileged access management policies
- Tool configuration changes MUST follow change control procedures

**SHOULD Requirements**:
- Monitoring tools SHOULD be monitored themselves (monitoring the monitors)
- Tool availability and performance SHOULD be tracked
- Tool failures SHOULD trigger alerts to administrators

---

## 2.3.10 Monitoring for Cloud and IaC Environments

### 2.3.10.1 Cloud Configuration Monitoring

**MUST Requirements**:
- [Organization] MUST monitor cloud service configurations including:
  - Identity and access management (IAM) policies
  - Network security groups and firewall rules
  - Storage bucket permissions and encryption
  - Compute instance configurations
  - Logging and monitoring settings
- Cloud monitoring MUST detect:
  - Public exposure of private resources
  - Weak authentication or authorization
  - Encryption disabled
  - Logging disabled
  - Deviations from cloud security benchmarks (CIS AWS, CIS Azure, CIS GCP)

**SHOULD Requirements**:
- Cloud monitoring SHOULD leverage cloud-native tools (AWS Config, Azure Policy, GCP Security Command Center)
- Cloud monitoring SHOULD be supplemented with third-party Cloud Security Posture Management (CSPM) tools
- Multi-cloud environments SHOULD use unified monitoring platforms

---

### 2.3.10.2 Infrastructure as Code (IaC) Monitoring

**SHOULD Requirements**:
- [Organization] SHOULD monitor IaC repositories for:
  - Security misconfigurations in templates (Terraform, CloudFormation, ARM templates)
  - Hardcoded secrets or credentials
  - Policy violations (e.g., allowing public access by default)
- IaC scanning SHOULD occur:
  - Pre-commit (developer workstation)
  - Pre-merge (pull request validation)
  - Pre-deployment (CI/CD pipeline gates)
  - Post-deployment (runtime verification)
- IaC monitoring SHOULD integrate with developer workflows (IDE plugins, Git hooks)

**MAY Requirements**:
- [Organization] MAY block deployments that fail IaC security scans
- IaC scan results MAY be aggregated in dashboards for security and DevOps teams

---

## 2.3.11 Monitoring Performance and Optimization

**SHOULD Requirements**:
- [Organization] SHOULD periodically assess monitoring system performance:
  - Detection effectiveness (percentage of changes detected)
  - False positive rate (percentage of alerts that are not actionable)
  - Mean time to detect (MTTD) configuration drift
  - Mean time to remediate (MTTR) configuration drift
- Monitoring performance SHOULD be optimized through:
  - Rule tuning to reduce false positives
  - Alert consolidation to reduce alert fatigue
  - Automation to accelerate remediation
- Optimization efforts SHOULD be documented and reviewed quarterly

---

## 2.3.12 Integration with Configuration Baselines and Change Control

### 2.3.12.1 Baseline Accuracy Validation

**MUST Requirements**:
- Configuration monitoring MUST validate that documented baselines reflect actual production state
- Discrepancies between baselines and production MUST be investigated and resolved:
  - If production is correct: Update baseline documentation
  - If baseline is correct: Remediate production drift
  - If both are incorrect: Conduct root cause analysis
- Baseline accuracy MUST be reviewed during configuration audits

---

### 2.3.12.2 Change Control Correlation

**MUST Requirements**:
- Configuration monitoring systems MUST correlate detected changes with approved change requests
- Changes detected without corresponding change records MUST be flagged as unauthorized
- Change success MUST be validated through monitoring (did the change achieve its intended configuration state?)

**SHOULD Requirements**:
- Monitoring systems SHOULD integrate with change management systems for automatic correlation
- Change approvers SHOULD have access to monitoring data to inform risk assessments

---

## 2.3.13 Exception Handling

**MUST Requirements**:
- Configuration drift that cannot be immediately remediated MUST be documented as an exception
- Exceptions MUST include:
  - Business or technical justification
  - Risk assessment and compensating controls
  - Expiration date or review schedule
  - Approval by CISO or delegated authority
- Exceptions MUST be tracked and reviewed regularly (at least quarterly)

**SHOULD Requirements**:
- Long-standing exceptions SHOULD trigger investigation (why can't this be remediated?)
- Exceptions SHOULD be minimized through proper change control and baseline management

---

## 2.3.14 The Reality of Configuration Monitoring

**Feynman's Final Word**: 

*"Configuration monitoring is not about achieving perfection—it's about knowing where you stand. You will have drift. Systems will deviate from baselines. Administrators will make emergency changes. Monitoring tells you this is happening so you can decide whether to accept it, fix it, or escalate it.*

*The organizations that succeed aren't the ones with zero drift (impossible). They're the ones that detect drift quickly, triage it intelligently, and remediate it systematically. Aim for a 95% configuration compliance rate, not 100%—the last 5% might be justified exceptions or acceptable risk."*

---

**END OF DOCUMENT**

**Cross-References**:
- ISMS-POL-A.8.9-S1: Purpose, Scope, Definitions
- ISMS-POL-A.8.9-S2: Requirements Overview
- ISMS-POL-A.8.9-S2.1: Baseline Configuration Requirements
- ISMS-POL-A.8.9-S2.2: Change Control Requirements
- ISMS-POL-A.8.9-S2.4: Security Hardening Requirements (next)
- ISMS-POL-A.8.9-S5.C: Configuration Deviation Procedures
- ISMS-IMP-A.8.9.3: Configuration Monitoring Assessment Specification

---