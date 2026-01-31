# ISMS-POL-A.8.16-S2.2
## Monitoring Activities - Baseline & Anomaly Detection Requirements

**Document ID**: ISMS-POL-A.8.16-S2.2
**Title**: Monitoring Activities - Baseline & Anomaly Detection Requirements  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]  | SOC Lead / Security Engineering / Threat Intelligence | Initial baseline and detection requirements |

**Review Cycle**: Quarterly (baselines evolve as business operations change)  
**Next Review Date**: [Approval Date + 3 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Operations Center (SOC) Lead
- Analytics Review: Threat Intelligence Lead / Security Architect

**Distribution**: Security team, SOC analysts, security engineering, threat intelligence  
**Related Documents**: ISMS-IMP-A.8.16.2 (Baseline & Detection Assessment), ISMS-POL-A.8.16-S5.B (Baseline Template)

---

## 2.2.1 Purpose and Scope

This section establishes **mandatory requirements** for baseline establishment and anomaly detection. These requirements ensure the organization can differentiate between normal and abnormal behavior—the fundamental capability that makes monitoring effective.

**In Scope**: Baseline establishment, anomaly detection methodologies, correlation logic, detection effectiveness  
**Primary Stakeholders**: SOC, Security Engineering, Threat Intelligence  
**Implementation Evidence**: ISMS-IMP-A.8.16.2 (Baseline & Detection Assessment)

**The Feynman Principle:**
> *"If you cannot explain your baseline with measurable metrics, you don't have a baseline—you have a guess. If you cannot explain why something is anomalous, you have noise—not detection."*

**This section prevents cargo cult monitoring** where organizations claim "we monitor everything" but cannot demonstrate:
- What "normal" looks like (documented baselines)
- How deviations are detected (detection logic)
- That detection actually works (effectiveness metrics)

---

## 2.2.2 Baseline Establishment Philosophy

### 2.2.2.1 What is a Baseline?

A **baseline** is a documented, measurable profile of normal behavior for a system, network segment, application, or user during known-good operational periods.

**Baselines are NOT:**
- ❌ Subjective opinions ("that seems high")
- ❌ Rough estimates ("usually around 100")
- ❌ Anecdotal observations ("I've never seen that before")
- ❌ Vendor default thresholds without validation

**Baselines ARE:**
- ✅ Quantifiable metrics with units (e.g., "50-100 logins/hour")
- ✅ Statistical profiles (mean, median, standard deviation, percentiles)
- ✅ Time-aware patterns (business hours vs. off-hours, weekday vs. weekend)
- ✅ Context-enriched (system type, criticality, user role)
- ✅ Documented and version-controlled

### 2.2.2.2 Fundamental Question

Organizations must answer:

> **"What does normal look like for each monitored asset, and how do we know?"**

This question requires actual measurement, not assumption.

### 2.2.2.3 Baseline Maturity Levels

Organizations progress through maturity levels:

**Level 0: No Baselines (Cargo Cult Monitoring)**
- Alerts configured with arbitrary thresholds
- No documented normal behavior
- Alert fatigue and ignored alarms
- **Status**: Non-compliant with this policy

**Level 1: Basic Baselines (Minimum Viable)**
- Critical systems have documented baselines
- Simple metrics (login count, connection count, error rate)
- Manual observation and documentation
- **Status**: Acceptable for initial implementation

**Level 2: Comprehensive Baselines (Target)**
- All monitored systems have documented baselines
- Multiple metrics per system (authentication, network, resource usage)
- Time-aware baselines (hourly, daily, weekly patterns)
- **Status**: Full compliance

**Level 3: Advanced Baselines (Aspirational)**
- Automated baseline maintenance
- Statistical anomaly detection (ML/AI)
- User and Entity Behavior Analytics (UEBA)
- **Status**: Excellence

Organizations **SHALL** achieve Level 1 within 6 months and Level 2 within 18 months of policy adoption.

---

## 2.2.3 Baseline Establishment Requirements

### 2.2.3.1 Mandatory Baseline Coverage

Organizations **SHALL** establish documented baselines for:

**Critical Infrastructure (Tier 1 - Priority 1):**
- Domain Controllers (authentication patterns, group policy changes, privileged access)
- Database servers (query patterns, connection counts, unusual queries)
- Externally-facing web servers (traffic volume, geographic patterns, error rates)
- VPN gateways (connection patterns, authentication failures, unusual sources)
- Firewalls (traffic volume, blocked connection patterns, rule change frequency)

**Security Infrastructure (Tier 1 - Priority 2):**
- SIEM/monitoring platforms (log ingestion rates, storage utilization)
- EDR platforms (endpoint behavior patterns, alert volumes)
- Privileged Access Management (PAM) systems (privileged session frequency, duration)
- Email security gateways (spam rates, malware detection rates, phishing attempts)

**Business-Critical Systems (Tier 2):**
- ERP systems (transaction patterns, user activity)
- CRM systems (data access patterns, export activities)
- File servers (access patterns, large file transfers, permission changes)
- Application servers (resource utilization, error rates, API call patterns)

**Coverage Target:** 100% of Tier 1 systems MUST have documented baselines. 80% of Tier 2 systems SHOULD have baselines.

### 2.2.3.2 Baseline Observation Period

Organizations **SHALL**:

- Establish baselines using **minimum 30 days** of observation during known-good periods
- Exclude incident periods, outages, or major changes from baseline establishment
- Include sufficient operational diversity (business cycles, seasonal patterns where applicable)
- Document observation period start/end dates and exclusions

Organizations **SHOULD**:
- Use 60-90 days observation for more accurate baselines
- Capture multiple business cycles if relevant (month-end processing, quarter-end, year-end)
- Account for seasonal variations (retail holiday season, academic year patterns)

### 2.2.3.3 Baseline Metrics

For each baselined system, organizations **SHALL** establish metrics in these categories:

**Authentication Metrics:**
- Successful login count (total, per hour, per user)
- Failed login attempts (total, per user, per source IP)
- Privileged access sessions (frequency, duration, accounts used)
- After-hours authentication (outside business hours)
- Geographic login patterns (countries, cities, unusual locations)

**Network Metrics:**
- Inbound connection count (total, per protocol, per source)
- Outbound connection count (especially from servers to internet)
- Data transfer volume (inbound, outbound, per protocol)
- Connection duration patterns
- Port usage patterns

**System Behavior Metrics:**
- Process execution patterns (which processes run, how often)
- System resource usage (CPU, memory, disk I/O - average and peak)
- Service restarts (frequency, which services)
- Configuration file modifications (frequency, which files)
- Error rates (system errors, application errors)

**Application Metrics:**
- Transaction volume (per hour, per day)
- Database query patterns (types, frequencies, execution times)
- API call patterns (endpoints, request rates)
- Data access patterns (which data, how often, by whom)
- Export/download activities (frequency, volume)

**User Behavior Metrics:**
- Normal working hours patterns
- System access patterns (which systems, when)
- Data access patterns (which data, read vs. write)
- Email patterns (volume sent/received, external recipients)

### 2.2.3.4 Statistical Baseline Documentation

Organizations **SHALL** document baselines using statistical measures:

**Required Metrics:**
- **Mean (Average)**: Central tendency
- **Median**: Middle value (less affected by outliers)
- **Standard Deviation**: Measure of variability
- **Minimum/Maximum**: Range boundaries
- **95th Percentile**: Upper normal bound (excludes outlier spikes)

**Example Baseline Documentation:**
```
System: DC01-Primary (Domain Controller)
Metric: Successful Login Events
Observation Period: 01.11.2025 - 30.11.2025 (30 days, excluding 15.11 incident)
Business Hours (08:00-18:00 Mon-Fri):
  - Mean: 245 logins/hour
  - Median: 238 logins/hour
  - Std Dev: 42 logins/hour
  - 95th Percentile: 315 logins/hour
  - Range: 180-350 logins/hour
Off-Hours (all other times):
  - Mean: 12 logins/hour
  - Median: 8 logins/hour
  - 95th Percentile: 25 logins/hour
Threshold: Alert if >350 logins/hour during business hours OR >30 logins/hour off-hours
```

### 2.2.3.5 Time-Aware Baselines

Organizations **SHALL** establish time-aware baselines recognizing that "normal" varies by:

**Time of Day:**
- Business hours (08:00-18:00): Higher activity expected
- Off-hours (18:00-08:00): Lower activity expected
- Overnight (00:00-06:00): Minimal activity expected (except batch jobs)

**Day of Week:**
- Monday-Friday: Business activity
- Saturday-Sunday: Minimal activity (except retail, healthcare, 24/7 operations)

**Special Periods:**
- Month-end/quarter-end: Financial processing spikes
- Maintenance windows: Expected service restarts, configuration changes
- Business cycles: Payroll processing, invoice runs, reporting periods

Organizations **SHOULD** establish separate baselines for each time context rather than single "average" baseline.

---

## 2.2.4 Baseline Maintenance and Updates

### 2.2.4.1 Baseline Review Frequency

Organizations **SHALL** review baselines:

**Scheduled Reviews:**
- **Critical systems (Tier 1)**: Quarterly
- **Standard systems (Tier 2)**: Semi-annually
- **All baselines**: Annually (comprehensive review)

**Triggered Reviews:**
- After major infrastructure changes (migrations, upgrades)
- After significant business process changes
- Following security incidents (if baseline gaps identified)
- When monitoring generates excessive false positives

### 2.2.4.2 Baseline Update Triggers

Baselines **SHALL** be updated when:

- Business operations change significantly (new applications, process changes)
- System role changes (e.g., file server becomes database server)
- User population changes significantly (growth, reorganization)
- Detection consistently identifies new "normal" patterns
- False positive rate exceeds acceptable threshold (>25% for that detection rule)

### 2.2.4.3 Baseline Change Control

Baseline updates **SHALL** follow change control:

- **Document reason** for baseline update
- **Compare old vs. new** baselines (what changed)
- **Approve changes** by SOC Lead or Security Manager
- **Version control** baselines (retain historical versions)
- **Communicate changes** to SOC analysts (updated thresholds)

**Example Change Log:**
```
Baseline Update Log:
System: SQLPROD01
Date: 15.12.2025
Updated By: SOC Analyst T2 (Jane Doe)
Approved By: SOC Lead (John Smith)
Change: Increased database query baseline from 1,000/hour to 2,500/hour
Reason: New business reporting application deployed 01.12.2025
Evidence: 2 weeks observation shows consistent 2,400-2,600 queries/hour
Old Alert Threshold: >1,500/hour
New Alert Threshold: >3,500/hour (140% of new baseline)
```

---

## 2.2.5 Anomaly Detection Methodologies

### 2.2.5.1 Detection Approaches

Organizations **SHALL** implement multiple detection approaches:

**Signature-Based Detection (Rule-Based):**
- Detects known attack patterns using predefined rules
- Example: "Failed login >5 times in 10 minutes from same IP"
- **Strength**: Low false positives for known threats
- **Weakness**: Cannot detect novel attacks (zero-days)
- **Usage**: Mandatory for all organizations

**Threshold-Based Detection (Statistical):**
- Detects when metrics exceed baseline thresholds
- Example: "Network traffic >200% of baseline"
- **Strength**: Detects unusual volume/frequency
- **Weakness**: Requires accurate baselines
- **Usage**: Mandatory for critical systems

**Anomaly-Based Detection (Behavioral):**
- Detects deviations from established behavior patterns
- Example: "User accessing systems never previously accessed"
- **Strength**: Can detect novel attacks
- **Weakness**: Higher false positive rate
- **Usage**: Recommended where supported by tools

**Heuristic Detection (Pattern-Based):**
- Uses rules of thumb to identify suspicious patterns
- Example: "PowerShell execution from browser process"
- **Strength**: Flexible, catches variations
- **Weakness**: Requires security expertise to develop
- **Usage**: Recommended for mature SOCs

**Correlation-Based Detection (Multi-Event):**
- Correlates multiple events to identify attack chains
- Example: "Failed login followed by successful login from different country within 1 minute"
- **Strength**: Reduces false positives, identifies complex attacks
- **Weakness**: Requires SIEM/correlation engine
- **Usage**: Mandatory where SIEM is deployed

Organizations **MUST** use at minimum signature-based and threshold-based detection. Advanced methods are recommended as SOC matures.

### 2.2.5.2 Threshold Derivation from Baselines

Organizations **SHALL** derive alert thresholds from documented baselines using this methodology:

**Standard Threshold Formula:**
```
Alert Threshold = Baseline_95th_Percentile × Multiplier

Where Multiplier depends on risk tolerance:
- Critical systems, high-risk events: 1.2x (20% above baseline)
- Standard systems, medium-risk events: 1.5x (50% above baseline)
- Low-priority systems, low-risk events: 2.0x (100% above baseline)
```

**Example:**
```
System: VPN Gateway
Baseline (Business Hours): 95th percentile = 150 connections/hour
Risk Level: High (external access)
Multiplier: 1.2x
Alert Threshold: 150 × 1.2 = 180 connections/hour
```

Organizations **MAY** adjust multipliers based on operational experience but **SHALL** document justification.

### 2.2.5.3 Multi-Threshold Alerting

Organizations **SHOULD** implement multi-level thresholds:

**Warning Threshold:**
- Moderate deviation from baseline (e.g., 1.5x)
- Lower severity alert
- Investigation within 24 hours

**Critical Threshold:**
- Significant deviation from baseline (e.g., 2.0x)
- High severity alert
- Immediate investigation required

**Example:**
```
Metric: Failed Login Attempts
Baseline: 5 failures/hour (95th percentile)
Warning Threshold: 8 failures/hour (1.5x)
Critical Threshold: 15 failures/hour (3x)
```

---

## 2.2.6 Detection Rule Development and Management

### 2.2.6.1 Detection Content Strategy

Organizations **SHALL** develop detection rules from multiple sources:

**Threat Intelligence Feeds:**
- IOC matching rules (malicious IPs, domains, file hashes)
- TTP-based detection (MITRE ATT&CK techniques)
- Industry-specific threat patterns

**Security Frameworks:**
- MITRE ATT&CK Framework (detection per technique)
- CIS Controls (detection rules aligned to controls)
- NIST SP 800-53 (monitoring requirements)

**Vendor-Provided Rules:**
- SIEM/EDR vendor default rule sets
- Security appliance signature updates

**Custom Organizational Rules:**
- Baseline-derived threshold rules
- Business-specific detection logic
- Post-incident detection rules (prevent recurrence)

**Community Sources:**
- Open-source detection rules (Sigma, YARA)
- Industry sharing communities (ISACs)

### 2.2.6.2 Detection Rule Requirements

Each detection rule **SHALL** include:

**Rule Identification:**
- Unique rule ID/name
- Rule version and creation date
- Rule owner/author
- Last modified date

**Rule Logic:**
- Detection conditions (what triggers the rule)
- Timeframe/window (if applicable)
- Correlation logic (if multi-event)
- Severity level (Critical/High/Medium/Low)

**Rule Metadata:**
- MITRE ATT&CK mapping (technique ID)
- Asset scope (which systems this rule applies to)
- False positive expected rate
- Tuning history (changes made)

**Response Guidance:**
- Initial triage steps
- Expected false positive scenarios
- Escalation criteria
- Investigation playbook reference

### 2.2.6.3 Rule Lifecycle Management

Organizations **SHALL** manage detection rules through lifecycle:

**Development:**
- Test rules in dev/staging environment first
- Validate rule logic with sample data
- Estimate false positive rate
- Document rule purpose and logic

**Deployment:**
- Deploy to production with "monitor mode" first (log but don't alert)
- Observe for 7-14 days to calibrate
- Enable alerting after tuning

**Tuning:**
- Analyze false positives and adjust conditions
- Refine thresholds based on operational experience
- Document tuning changes and rationale
- Re-test after major changes

**Retirement:**
- Disable rules no longer relevant (obsolete threats, decommissioned systems)
- Document retirement reason
- Retain rule documentation for audit trail

### 2.2.6.4 Rule Testing and Validation

Organizations **SHALL** validate detection effectiveness:

**Testing Methods:**
- **Purple Team Exercises**: Red team attacks tested against blue team detection
- **Attack Simulations**: Tools like Atomic Red Team, Caldera
- **Injected Test Events**: Synthetic security events injected into production monitoring
- **Historical Incident Analysis**: Replay past incident data to verify detection would trigger

**Testing Frequency:**
- Critical detection rules: Quarterly
- Standard detection rules: Semi-annually
- New rules: Within 30 days of deployment
- Post-incident: Rules modified after incidents

**Success Criteria:**
- Detection rate >90% for tested attack techniques
- False positive rate <10% for critical alerts, <25% for all alerts
- Alert generation latency <5 minutes

---

## 2.2.7 Correlation and Multi-Event Detection

### 2.2.7.1 Correlation Requirements

Organizations with SIEM capabilities **SHALL** implement correlation to:

- Reduce false positives (require multiple conditions before alerting)
- Detect complex attack patterns (attack chains, lateral movement)
- Enrich alerts with context (asset info, user info, threat intelligence)
- Prioritize alerts based on risk scoring

**Example Correlation Rules:**

**Suspicious Login Chain:**
```
IF failed_login_count > 5 within 10 minutes
  AND successful_login occurs from same username
  AND source_IP is different from normal user locations
THEN generate HIGH severity alert: "Suspicious login after brute force"
```

**Lateral Movement Detection:**
```
IF administrative_login to Server_A
  AND network_connection from Server_A to Server_B within 5 minutes
  AND administrative_login to Server_B within 10 minutes
  AND user_account not normally accessing Server_B
THEN generate CRITICAL alert: "Possible lateral movement"
```

### 2.2.7.2 Context Enrichment

Organizations **SHOULD** enrich alerts with context from:

- **Asset Management**: System owner, criticality, location
- **Identity Management**: User role, department, manager
- **Threat Intelligence**: IP reputation, domain categorization, known IOCs
- **Vulnerability Management**: Known vulnerabilities on affected systems
- **Historical Data**: Past incidents involving same user/system

**Benefit**: Context reduces triage time and improves prioritization.

---

## 2.2.8 Threat Intelligence Integration

### 2.2.8.1 Threat Intelligence Sources

Organizations **SHALL** integrate threat intelligence from:

**External Sources (Mandatory):**
- SIEM/security tool vendor threat feeds
- Industry-specific threat sharing communities (ISACs)
- Open-source threat intelligence (OSINT)

**External Sources (Recommended):**
- Commercial threat intelligence platforms
- Government threat intelligence (NCSC, CISA, etc.)
- Peer organization sharing (where trust relationships exist)

**Internal Sources (Mandatory):**
- IOCs from past security incidents
- Indicators from threat hunting activities
- Custom detection logic based on organizational threats

### 2.2.8.2 IOC Matching and Alerting

Organizations **SHALL**:

- Automatically match threat intelligence IOCs against logs (IP addresses, domains, file hashes, URLs)
- Generate alerts when IOC matches are detected
- Enrich IOC matches with threat context (threat actor, campaign, severity)
- Track IOC hit rates (how often feeds provide actionable matches)

### 2.2.8.3 Threat Intelligence Quality Management

Organizations **SHALL**:

- Evaluate threat feed quality (hit rate, false positives, timeliness)
- Disable or deprioritize low-quality feeds
- Tune alert severity based on threat intelligence confidence levels
- Document which threat feeds are consumed and why

---

## 2.2.9 False Positive and False Negative Management

### 2.2.9.1 False Positive Handling

Organizations **SHALL** implement process for false positive management:

**Identification:**
- SOC analysts identify false positives during triage
- Track false positives by detection rule

**Analysis:**
- Investigate root cause (baseline outdated? Rule too broad? Legitimate exception?)
- Document false positive patterns

**Resolution:**
- **Tune rule** if logic is too broad
- **Update baseline** if normal behavior changed
- **Add exception** if legitimate but unusual activity
- **Retire rule** if consistently unusable

**Tracking:**
- Measure false positive rate per rule (target: <25% for all rules, <10% for critical)
- Report high false positive rules to SOC management monthly
- Prioritize tuning for worst offenders

### 2.2.9.2 False Negative Management

Organizations **SHALL** address false negatives through:

**Detection:**
- Post-incident analysis (did monitoring detect the incident? If not, why not?)
- Red team exercises revealing detection gaps
- Threat hunting discovering undetected threats

**Root Cause Analysis:**
- Was log source missing? (coverage gap)
- Was baseline too permissive? (threshold too high)
- Was detection rule missing? (capability gap)
- Was alert suppressed? (tuning error)

**Remediation:**
- Add missing log sources
- Adjust baselines/thresholds
- Develop new detection rules
- Review and improve tuning decisions

**Continuous Improvement:**
- Track detection rate from testing (target: >90%)
- Measure dwell time for incidents (lower is better)
- Analyze missed detections in incident reports

### 2.2.9.3 Acceptable Error Rates

Organizations **SHALL** establish acceptable error rates:

**False Positive Targets:**
- Critical severity alerts: <10% false positive rate
- High severity alerts: <15% false positive rate
- Medium severity alerts: <25% false positive rate
- Low severity alerts: <40% false positive rate

**False Negative Targets:**
- Critical threats (APT, ransomware, data exfiltration): <5% miss rate
- Standard threats: <10% miss rate

**Note**: Perfect detection (0% false positives, 0% false negatives) is impossible. Organizations must balance detection completeness with operational workload.

---

## 2.2.10 Detection Effectiveness Metrics

Organizations **SHALL** measure detection effectiveness through:

### 2.2.10.1 Detection Rate Metrics

**Primary Metric: Detection Rate**
- Percentage of test attacks successfully detected
- Measured through red team exercises, simulations
- **Target: >90% detection rate for tested techniques**

**Secondary Metrics:**
- Mean Time To Detect (MTTD): Time from event to alert
- Alert Volume: Total alerts per day (indicates tuning effectiveness)
- Alert-to-Incident Ratio: Percentage of alerts that become incidents

### 2.2.10.2 Baseline Quality Metrics

- **Baseline Coverage**: Percentage of critical systems with documented baselines (target: 100%)
- **Baseline Staleness**: Days since last baseline review (target: <90 days for critical systems)
- **Baseline-Derived Alerts**: Percentage of alerts using baseline thresholds (indicates baseline utilization)

### 2.2.10.3 Rule Performance Metrics

- **False Positive Rate by Rule**: Percentage of alerts that are false positives
- **Alert Volume by Rule**: Number of alerts generated (identifies noisy rules)
- **Rule Coverage**: Percentage of MITRE ATT&CK techniques with detection coverage
- **Rule Testing Status**: Percentage of rules tested in last 6 months

### 2.2.10.4 Reporting

Detection effectiveness metrics **SHALL** be:
- Reviewed **monthly** by SOC management
- Reported **quarterly** to CISO
- Included in **annual** ISMS review

---

## 2.2.11 Continuous Improvement

Organizations **SHALL**:

- Conduct **quarterly** baseline reviews and updates
- Conduct **quarterly** detection rule tuning exercises
- Conduct **annual** comprehensive detection coverage assessment (MITRE ATT&CK mapping)
- Participate in industry threat intelligence sharing communities
- Analyze all security incidents for detection gaps
- Incorporate lessons learned into detection improvements

Organizations **SHOULD**:
- Implement threat hunting program to discover detection gaps proactively
- Conduct regular purple team exercises
- Benchmark detection capabilities against peer organizations
- Invest in SOC analyst training on detection techniques

---

## 2.2.12 Exceptions to Detection Requirements

**General Rule**: Exceptions to baseline and detection requirements create blind spots and are strongly discouraged.

Where technical or business constraints prevent full compliance, organizations **SHALL**:

- Document exception with technical justification
- Identify compensating controls
- Require SOC Lead and CISO approval
- Review exceptions quarterly
- Establish timeline to achieve compliance

**Example Valid Exception**: Legacy system with no logging capability, scheduled for replacement in 4 months. Compensating control: Enhanced network monitoring of all traffic to/from legacy system.

**Example Invalid Exception**: "Establishing baselines is too much work." (Monitoring without baselines is cargo cult security—the work must be done.)

---

**END OF DOCUMENT**

---

## Related Documents in Framework

- **ISMS-POL-A.8.16-S1** (Purpose, Scope, Definitions) - Foundation and terminology
- **ISMS-POL-A.8.16-S2** (Requirements Overview) - Framework overview
- **ISMS-POL-A.8.16-S2.1** (Infrastructure) - Log collection and monitoring platforms
- **ISMS-POL-A.8.16-S2.3** (Alert Management) - What to do when detection triggers
- **ISMS-POL-A.8.16-S2.4** (Retention) - How long to keep monitoring data
- **ISMS-POL-A.8.16-S5.B** (Baseline Template) - Template for baseline documentation
- **ISMS-IMP-A.8.16.2** (Implementation Assessment) - Assessment workbook for baselines and detection

---

*"A baseline without measurement is an opinion. An alert without a baseline is noise. Detection without testing is hope."*  
*—Security Operations Wisdom*