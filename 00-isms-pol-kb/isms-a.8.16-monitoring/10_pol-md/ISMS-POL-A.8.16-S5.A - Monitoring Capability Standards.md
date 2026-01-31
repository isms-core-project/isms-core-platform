# ISMS-POL-A.8.16-S5.A
## Monitoring Capability Standards

**Document ID**: ISMS-POL-A.8.16-S5.A
**Title**: Monitoring Capability Standards  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]  | Security Engineering Manager | Initial capability standards |

**Review Cycle**: Annual (or when technology landscape changes significantly)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Engineering Manager
- Operational Review: SOC Lead

**Distribution**: Security Engineering, IT Management, Procurement, SOC Leadership  
**Related Documents**: ISMS-POL-A.8.16-S2.1 (Monitoring Infrastructure Requirements)

---

## 1. Purpose and Scope

### 1.1 Purpose

This annex defines **technical capability requirements** for monitoring solutions deployed within the organization's security monitoring infrastructure. These standards ensure monitoring platforms can:

- Collect and process security events at required scale
- Detect threats and anomalies effectively
- Support SOC operational workflows
- Meet compliance and retention requirements
- Integrate with broader security ecosystem

**Target Audience**: Security Engineering (primary), Procurement, IT Management, Solution Architects

### 1.2 Scope

Standards apply to **all monitoring technologies**, including but not limited to:

- **SIEM** (Security Information and Event Management)
- **IDS/IPS** (Intrusion Detection/Prevention Systems)
- **EDR/XDR** (Endpoint/Extended Detection and Response)
- **NDR** (Network Detection and Response)
- **UEBA** (User and Entity Behavior Analytics)
- **Log Management Platforms**
- **Threat Intelligence Platforms**

**Out of Scope**: Application-specific monitoring (APM), infrastructure monitoring (SNMP/Nagios), unless integrated into security monitoring.

### 1.3 Requirement Levels

This document uses RFC 2119 terminology:

- **MUST / SHALL / REQUIRED**: Mandatory capability, non-negotiable
- **SHOULD / RECOMMENDED**: Strongly recommended, waiver requires CISO approval
- **MAY / OPTIONAL**: Nice-to-have, competitive differentiator

**Rationale for Requirements**: Each requirement includes justification to prevent cargo cult implementation ("we need this because ISO 27001 says so" is not sufficient reasoning).

---

## 2. Core Capabilities

### 2.1 Log Collection

#### 2.1.1 Protocol Support

**MUST support**:
- **Syslog** (RFC 3164, RFC 5424) - Universal standard
- **Windows Event Logs** (via WMI, WEF, or agent) - Windows infrastructure
- **HTTPS API ingestion** - Modern application logs
- **File-based ingestion** - Batch processing, air-gapped systems

**SHOULD support**:
- **Kafka/streaming protocols** - High-volume environments
- **Cloud-native APIs** (AWS CloudWatch, Azure Monitor, GCP Logging) - Cloud infrastructure
- **SNMP traps** - Network device events

**Rationale**: Diverse infrastructure requires diverse collection methods. Syslog and Windows Event Logs are foundational; API and streaming support modern architectures.

#### 2.1.2 Collection Methods

**MUST support**:
- **Agent-based collection** - For endpoints, servers with local processing needs
- **Agentless collection** - For network devices, appliances, API sources

**SHOULD support**:
- **Proxy/forwarder architecture** - For distributed environments, DMZ collection

**Rationale**: No single collection method fits all scenarios. Endpoints benefit from agents (local filtering, buffering); network devices require agentless.

#### 2.1.3 Buffering and Reliability

**MUST provide**:
- **Local buffering** - Agents buffer during network outages (min 24 hours)
- **Guaranteed delivery** - Acknowledgments, retries, no log loss
- **Flow control** - Backpressure mechanisms to prevent collector overload

**SHOULD provide**:
- **Compression in transit** - Reduce bandwidth consumption (gzip, lz4)
- **Persistent queues** - Disk-backed queues survive collector restarts

**Rationale**: Log loss = blind spots. Buffering ensures continuity during outages. Flow control prevents cascading failures.

---

### 2.2 Log Parsing and Normalization

#### 2.2.1 Format Support

**MUST support parsing**:
- **Common formats**: Syslog, Windows Event Logs, JSON, CEF, LEEF
- **Custom parsers**: Regex-based, field extraction, delimiter parsing

**SHOULD support**:
- **Pre-built parsers**: For common sources (Cisco, Palo Alto, Microsoft, Linux)
- **Parser marketplace**: Vendor-provided or community parsers

**Rationale**: Out-of-box parsers accelerate deployment. Custom parsers handle unique applications. Poor parsing = unusable data.

#### 2.2.2 Field Normalization

**MUST provide**:
- **Common schema mapping** - Map vendor fields to standard fields (src_ip, dest_ip, user, action)
- **Field enrichment** - Add calculated fields, lookups, categorization
- **Data type enforcement** - IP addresses as IPs, timestamps as timestamps (not strings)

**Rationale**: Normalization enables cross-source correlation. "User=admin" vs "Username=admin" vs "account=admin" must map to same field for analytics.

#### 2.2.3 Parsing Performance

**MUST achieve**:
- **Parsing latency <1 second** - From ingestion to searchable
- **Error handling** - Failed parsing documented, sample logs retained for troubleshooting

**SHOULD achieve**:
- **Parsing latency <100ms** - For real-time alerting use cases

**Rationale**: Slow parsing delays detection. Parse errors create blind spots. 1 second is acceptable for batch; <100ms needed for real-time threats.

---

### 2.3 Storage and Indexing

#### 2.3.1 Storage Architecture

**MUST provide**:
- **Compressed storage** - Min 5:1 compression ratio (industry standard)
- **Indexed search** - Full-text and field-based indexing
- **Tiered storage** - Hot (fast SSD), warm (slower disks), cold (archive)

**SHOULD provide**:
- **Data retention automation** - Automatic tier migration based on age
- **Immutable storage** - Write-once for compliance/forensics (optional tier)

**Rationale**: 90 days of uncompressed logs = massive storage costs. Compression is non-negotiable. Tiering balances cost vs. performance. Hot tier for recent investigations; cold for compliance.

#### 2.3.2 Storage Capacity

**MUST support**:
- **Expected EPS × 90 days** - With compression applied
- **20% growth buffer** - Accommodate log volume increases

**Example Calculation**:
```
Org ingests 10,000 EPS average
90 days = 10,000 EPS × 86,400 sec/day × 90 days = 77.76 billion events
Average event size = 1KB uncompressed
With 5:1 compression = 200 bytes/event
Storage needed = 77.76B events × 200 bytes = 15.55 TB
With 20% buffer = 18.66 TB required capacity
```

**Rationale**: Under-provisioning = data loss when storage fills. Growth buffer prevents emergency expansions.

#### 2.3.3 Indexing Performance

**MUST achieve**:
- **Indexing rate ≥ ingestion rate** - No backlog accumulation
- **Search latency <10 seconds** - For typical queries on hot storage (last 30 days)

**SHOULD achieve**:
- **Search latency <3 seconds** - For common dashboards and alerts

**Rationale**: Indexing slower than ingestion = ever-growing backlog. Slow search = frustrated analysts, delayed investigations.

---

### 2.4 Search and Analysis

#### 2.4.1 Query Capabilities

**MUST support**:
- **Full-text search** - Keyword search across all fields
- **Field-based filtering** - WHERE clauses (src_ip=X, user=Y, action=Z)
- **Boolean logic** - AND, OR, NOT operators
- **Time-range filtering** - Essential for all queries
- **Aggregation** - COUNT, SUM, AVG, GROUP BY
- **Sorting** - By any field, ascending/descending

**SHOULD support**:
- **Statistical functions** - STDDEV, PERCENTILE, MEDIAN
- **Regex search** - Pattern matching within fields
- **Subsearches** - Use one query result as input to another
- **Geolocation** - IP-to-geo enrichment, map visualizations

**Rationale**: Basic filtering/aggregation handles 90% of SOC queries. Statistical functions enable baseline analysis. Regex enables pattern hunting.

#### 2.4.2 Query Performance

**MUST achieve**:
- **<10 seconds for 80% of queries** - On hot storage (last 30 days)
- **<60 seconds for complex queries** - Multi-stage aggregations, large time ranges

**SHOULD provide**:
- **Query optimization** - Automatic index selection, query rewriting
- **Query caching** - Frequently-run queries return instantly

**Rationale**: 10 seconds is SOC analyst attention span. Longer searches slow investigations. Complex queries (baseline calculations) can be slower but <60 sec prevents frustration.

#### 2.4.3 Concurrent Users

**MUST support**:
- **≥10 concurrent analysts** - Searching without performance degradation

**SHOULD support**:
- **≥50 concurrent users** - Including dashboard viewers, automated queries

**Rationale**: Typical SOC has 3-10 analysts per shift. Peak usage during incidents can spike. Under-provisioning = "system slow during incident" (worst timing).

---

### 2.5 Alerting

#### 2.5.1 Alert Types

**MUST support**:
- **Threshold alerts** - Value exceeds/falls below threshold (e.g., failed logins > 10)
- **Correlation alerts** - Multiple events across time window (e.g., failed login + successful login within 5 min)
- **Baseline deviation alerts** - Statistical anomaly detection
- **Threat intelligence matches** - IOC matches (IP, domain, hash)

**SHOULD support**:
- **Machine learning alerts** - UEBA, unsupervised anomaly detection
- **Aggregation alerts** - GROUP BY before threshold (e.g., per-user failed logins)

**Rationale**: Thresholds handle known-bad scenarios. Correlation detects attack patterns. Baseline deviation catches anomalies. TI matches known threats.

#### 2.5.2 Alert Enrichment

**MUST provide**:
- **Field extraction** - Include relevant fields in alert (user, IP, hostname)
- **Contextual lookups** - Add asset info, user info, threat intel

**SHOULD provide**:
- **Automatic response** - Trigger SOAR workflows, containment actions
- **Dynamic severity** - Adjust severity based on context (e.g., admin account = higher severity)

**Rationale**: Analysts need context immediately. "Alert: Brute force detected" (useless). "Alert: Brute force on admin@dc01 from 1.2.3.4 (known botnet)" (actionable).

#### 2.5.3 Alert Management

**MUST provide**:
- **Alert suppression** - Suppress duplicate alerts within time window (avoid spam)
- **Alert tuning** - Adjust thresholds without rule rewrite
- **Alert lifecycle** - NEW → INVESTIGATING → RESOLVED/FALSE_POSITIVE states

**SHOULD provide**:
- **Alert escalation** - Automatic escalation if no response within SLA
- **Alert grouping** - Related alerts grouped into single incident

**Rationale**: Unsuppressed duplicate alerts = alert fatigue. Tuning must be easy or analysts create tickets instead of tuning. Lifecycle tracking = accountability.

#### 2.5.4 Alert Performance

**MUST achieve**:
- **Alert latency <2 minutes** - From event ingestion to alert trigger (critical alerts)
- **Alert latency <15 minutes** - For non-critical alerts

**Rationale**: 2 minutes allows real-time response to critical threats. 15 minutes acceptable for lower-severity issues. Longer delays = missed containment windows.

---

### 2.6 Visualization

#### 2.6.1 Dashboard Capabilities

**MUST provide**:
- **Pre-built dashboards** - Common use cases (failed logins, network traffic, threat intel matches)
- **Custom dashboards** - Analyst-created, saved, shared
- **Chart types** - Time series, bar, pie, table, single value
- **Drill-down** - Click chart element → underlying logs

**SHOULD provide**:
- **Real-time dashboards** - Auto-refresh, live data
- **Dashboard templating** - Parameterized dashboards (select time range, filter)

**Rationale**: Pre-built dashboards accelerate onboarding. Custom dashboards support diverse use cases. Drill-down bridges metrics to raw logs (essential for investigations).

#### 2.6.2 Reporting

**MUST provide**:
- **Scheduled reports** - Daily/weekly/monthly, email/export
- **On-demand reports** - Generate report for any time range
- **Export formats** - PDF, CSV, JSON

**SHOULD provide**:
- **Report templates** - Compliance reports (PCI, ISO, SOC2)
- **Executive dashboards** - High-level KPIs, no technical jargon

**Rationale**: Compliance requires regular reports. Investigations require on-demand reports. Executives need simplified views.

---

## 3. Detection Capabilities

### 3.1 Correlation Engine

#### 3.1.1 Correlation Types

**MUST support**:
- **Temporal correlation** - Events within time window (e.g., A then B within 5 minutes)
- **Field-based correlation** - Events sharing common field (e.g., same src_ip)
- **Threshold correlation** - Event count across multiple sources

**SHOULD support**:
- **Sequence correlation** - Events in specific order (A → B → C)
- **Absence correlation** - Expected event did NOT occur (e.g., user logged in but no logout for 24h)

**Rationale**: Attacks span multiple events, sources, time. Simple threshold alerts miss multi-stage attacks. Correlation connects dots.

#### 3.1.2 Correlation Performance

**MUST achieve**:
- **Correlation latency <5 minutes** - For standard rules (2-3 event correlation)
- **Memory efficiency** - No unbounded state growth (prevent memory exhaustion)

**SHOULD achieve**:
- **Correlation latency <1 minute** - For real-time attack detection

**Rationale**: 5 minutes allows detection of rapid attacks (brute force → lateral movement). Longer delays = attacker establishes foothold. Memory leaks crash systems.

---

### 3.2 Threat Intelligence Integration

#### 3.2.1 Feed Support

**MUST support**:
- **IOC ingestion** - IPs, domains, URLs, file hashes (MD5, SHA1, SHA256)
- **Feed formats** - STIX/TAXII, CSV, JSON, custom APIs
- **Automatic updates** - Feeds refresh on schedule (hourly/daily)

**SHOULD support**:
- **Commercial feeds** - Integration with threat intel platforms (MISP, ThreatConnect, Anomali)
- **Confidence scoring** - Weight matches by IOC confidence level

**Rationale**: Threat intel identifies known-bad. Manual updates are cargo cult (stale intel). Confidence scoring reduces false positives (not all IOCs are equal).

#### 3.2.2 Matching Performance

**MUST achieve**:
- **Real-time IOC matching** - Check all logs against IOC database
- **Match latency <1 minute** - From IOC match to alert

**SHOULD achieve**:
- **Bidirectional matching** - Historical logs re-scanned when new IOCs added (retrohunting)

**Rationale**: Real-time matching catches threats immediately. Retrohunting discovers past compromises when new intel emerges.

---

### 3.3 Baseline and Anomaly Detection

#### 3.3.1 Baseline Support

**SHOULD provide**:
- **Statistical baselining** - Calculate mean, stddev, percentiles per metric
- **Time-aware baselines** - Separate baselines for business hours, off-hours, weekends
- **Automated threshold derivation** - Suggest thresholds based on baseline

**MAY provide**:
- **UEBA** - User/entity behavior profiling, peer group comparison
- **Machine learning** - Unsupervised anomaly detection

**Rationale**: Manual baselines are time-consuming (SHOULD automate). Time-aware baselines reduce false positives (weekend activity ≠ weekday). UEBA and ML are advanced, not required for basic monitoring.

#### 3.3.2 Anomaly Detection

**SHOULD provide**:
- **Deviation alerts** - Metric exceeds baseline by X stddev or X%
- **Anomaly scoring** - Quantify "how anomalous" (e.g., 3 stddev vs 10 stddev)

**MAY provide**:
- **Explainable ML** - ML alerts include rationale (why flagged as anomaly)

**Rationale**: Baselines without alerts = wasted effort. Scoring helps prioritization (10 stddev = more urgent). Explainable ML builds analyst trust.

---

### 3.4 Rule Management

#### 3.4.1 Rule Lifecycle

**MUST support**:
- **Version control** - Track rule changes, rollback capability
- **Testing environment** - Test rules on historical data before production
- **Rule disabling** - Temporary disable without deletion (maintenance windows)
- **Rule retirement** - Archive obsolete rules, maintain history

**SHOULD support**:
- **A/B testing** - Run two rule versions in parallel, compare results
- **Rule metrics** - Track true positive rate, false positive rate, alert volume per rule

**Rationale**: Unversioned rules = "who changed this and why?" Version control = accountability. Testing prevents production fires. Metrics drive tuning.

#### 3.4.2 Rule Documentation

**MUST require**:
- **Rule purpose** - What attack/behavior does this detect?
- **MITRE ATT&CK mapping** - Which technique(s)?
- **Thresholds/logic** - Documented rationale for values
- **Known false positives** - Document expected FP scenarios

**SHOULD include**:
- **Investigation playbook** - Link to response procedure (Annex C)
- **Last tuning date** - When last reviewed/updated

**Rationale**: Undocumented rules = tribal knowledge. MITRE mapping enables coverage analysis. Documented FPs speed triage. Playbook links operationalize detection.

---

## 4. Integration Capabilities

### 4.1 Threat Intelligence Platforms

**MUST support**:
- **Automated feed ingestion** - From TIP to SIEM
- **IOC enrichment** - Alerts include TIP context (threat actor, campaign)

**SHOULD support**:
- **Bidirectional integration** - SIEM findings pushed back to TIP

**Rationale**: Manual threat intel = stale intel. Enrichment provides context. Bidirectional sharing improves organizational threat intel.

---

### 4.2 Incident Response and SOAR

**MUST support**:
- **Ticketing integration** - Auto-create tickets from alerts (ServiceNow, Jira)
- **Case management** - Link alerts to investigations/incidents

**SHOULD support**:
- **SOAR integration** - Trigger automated response workflows
- **API access** - Programmatic alert management, query execution

**Rationale**: Manual ticket creation = wasted time. SOAR enables automated containment (isolate host, block IP). APIs enable automation beyond vendor-provided integrations.

---

### 4.3 Asset Management

**SHOULD support**:
- **CMDB integration** - Enrich alerts with asset info (owner, criticality, location)
- **Automatic asset discovery** - Populate asset database from logs

**Rationale**: "Alert on 10.1.2.3" (useless). "Alert on PROD-DB-01 (critical, owner=DBTeam)" (actionable). Automatic discovery reduces manual asset management.

---

### 4.4 Identity Management

**SHOULD support**:
- **AD/LDAP integration** - Enrich alerts with user info (department, manager, title)
- **Identity context** - Differentiate human vs service account

**Rationale**: "Alert on jsmith" (ambiguous). "Alert on John Smith (Finance, high-privileged)" (context). Service account logins have different baselines than human logins.

---

## 5. Performance and Scalability

### 5.1 Ingestion Rate

**MUST support**:
- **Current EPS + 50% growth** - Accommodate log volume increases without upgrade

**Example**: Current 10,000 EPS → System must handle 15,000 EPS peak

**Rationale**: Immediate capacity for growth. 50% buffer prevents emergency upgrades when new systems onboarded.

---

### 5.2 Search Performance

Already covered in Section 2.4.2 (Query Performance).

---

### 5.3 Alert Latency

Already covered in Section 2.5.4 (Alert Performance).

---

### 5.4 Scalability Architecture

**MUST support**:
- **Horizontal scaling** - Add nodes/collectors to increase capacity
- **No single point of failure** - Distributed architecture

**SHOULD support**:
- **Auto-scaling** - Cloud environments dynamically scale based on load
- **Multi-tenancy** - Logically separate data per business unit (if needed)

**Rationale**: Vertical scaling has limits (biggest server still has ceiling). Horizontal scaling = limitless growth. SPOF = entire SOC blind during outages.

---

## 6. Operational Requirements

### 6.1 High Availability

**SHOULD provide**:
- **99.5% uptime** - ≤43.8 hours downtime per year (reasonable for internal systems)
- **Redundancy** - Redundant collectors, indexers, search heads
- **Failover** - Automatic failover to standby components

**MAY provide**:
- **99.9% uptime** - ≤8.76 hours downtime per year (for mission-critical environments)

**Rationale**: Monitoring downtime = blind spots. 99.5% balances cost vs. availability. Mission-critical orgs may require 99.9% (higher cost).

---

### 6.2 Disaster Recovery

**MUST provide**:
- **Backup capability** - Configuration, rules, dashboards backed up
- **RTO <24 hours** - Restore monitoring within 24h after disaster
- **RPO <24 hours** - Accept up to 24h log loss in disaster scenario (not ideal but acceptable)

**SHOULD provide**:
- **Geo-redundancy** - DR site in different geographic location
- **RTO <4 hours** - Faster recovery for critical environments

**Rationale**: Disasters happen (datacenter fire, ransomware). 24h RTO/RPO acceptable for logs (not transaction data). 4h RTO ideal but costly.

---

### 6.3 Security

#### 6.3.1 Access Control

**MUST provide**:
- **RBAC** (Role-Based Access Control) - Separate roles (admin, analyst, viewer)
- **MFA** (Multi-Factor Authentication) - For all access
- **Audit logging** - Log all user actions (searches, config changes)

**SHOULD provide**:
- **SSO integration** - SAML, OIDC (reduce password fatigue)
- **Data-level access control** - Restrict access to sensitive logs per role

**Rationale**: Logs contain sensitive data. RBAC prevents unauthorized access. MFA prevents credential compromise. Audit logs = accountability. Data-level control enables least privilege.

#### 6.3.2 Data Protection

**MUST provide**:
- **Encryption in transit** - TLS 1.2+ for all communications
- **Encrypted storage** - Logs encrypted at rest

**SHOULD provide**:
- **Tokenization/masking** - Redact sensitive fields (PCI, PII) from logs

**Rationale**: Logs traverse networks (encrypt in transit). Logs stored on disk (encrypt at rest). PCI/PII in logs = compliance risk (mask/tokenize).

---

## 7. Capability Evaluation Criteria

When evaluating monitoring solutions, use this checklist:

### 7.1 Must-Have Capabilities (Go/No-Go)

- [ ] Syslog and Windows Event Log collection
- [ ] Agent and agentless collection methods
- [ ] JSON, CEF, LEEF parsing
- [ ] Compressed tiered storage (hot/warm/cold)
- [ ] Full-text and field-based search
- [ ] Threshold and correlation alerting
- [ ] Alert suppression and lifecycle management
- [ ] Dashboard creation and reporting
- [ ] IOC matching (IP, domain, hash)
- [ ] Ticketing integration (ServiceNow, Jira, etc.)
- [ ] RBAC and MFA
- [ ] Encryption in transit and at rest
- [ ] Expected EPS + 50% capacity
- [ ] <10 sec search performance (hot storage)
- [ ] <2 min alert latency (critical alerts)

**Scoring**: All Must-Haves required to proceed. Any "No" = disqualified.

### 7.2 Should-Have Capabilities (Weighted Scoring)

Assign points (0-5 each, 5=excellent, 0=absent):

- [ ] Kafka/streaming protocol support (5 pts)
- [ ] Cloud-native API support (AWS/Azure/GCP) (5 pts)
- [ ] Pre-built parsers for common sources (4 pts)
- [ ] Statistical functions (STDDEV, PERCENTILE) (4 pts)
- [ ] Regex search (3 pts)
- [ ] Machine learning anomaly detection (5 pts)
- [ ] UEBA capabilities (5 pts)
- [ ] A/B rule testing (3 pts)
- [ ] Rule performance metrics (4 pts)
- [ ] SOAR integration (4 pts)
- [ ] CMDB integration (3 pts)
- [ ] AD/LDAP integration (3 pts)
- [ ] Auto-scaling (cloud environments) (4 pts)
- [ ] 99.5%+ uptime SLA (4 pts)
- [ ] Geo-redundant DR (4 pts)
- [ ] SSO integration (3 pts)
- [ ] Data-level access control (4 pts)
- [ ] PII masking/tokenization (4 pts)

**Scoring**: Sum points. >50 pts = strong solution. <30 pts = gaps in capabilities.

### 7.3 Nice-to-Have Capabilities (Differentiators)

- [ ] 99.9% uptime SLA
- [ ] Explainable machine learning
- [ ] Absence correlation (expected event did not occur)
- [ ] Bidirectional threat intel sharing
- [ ] Automatic asset discovery

**Scoring**: Use as tiebreakers between equivalent solutions.

---

## 8. Capability Maturity Model

Organizations should assess current monitoring maturity and plan improvements:

**Level 1 - Basic**: Syslog collection, keyword search, manual alerting (Excel spreadsheets)  
**Level 2 - Managed**: SIEM deployed, threshold alerts, manual correlation, basic dashboards  
**Level 3 - Defined**: Correlation rules, threat intel integration, automated ticketing, baselines documented  
**Level 4 - Quantitative**: Statistical baselines, UEBA, rule performance metrics, tuning cycles  
**Level 5 - Optimizing**: Machine learning, auto-tuning, predictive alerting, continuous improvement

**Target Maturity**: Level 3 minimum for compliance. Level 4+ for mature security programs.

---

## 9. Maintenance and Review

### 9.1 Annual Review

Review this document annually:

- **Technology evolution**: New SIEM capabilities, cloud-native tools, ML advances
- **Threat landscape**: New attack patterns requiring new detection capabilities
- **Operational feedback**: SOC reports capability gaps or pain points

### 9.2 Capability Gaps

When gaps identified:

1. **Document gap** - What capability is missing?
2. **Assess impact** - Is this MUST/SHOULD/MAY requirement?
3. **Plan remediation** - Upgrade current solution, add complementary tool, accept risk
4. **Update standards** - Revise requirements if needed (e.g., new mandatory capability)

---

## 10. Vendor Engagement

### 10.1 RFP Guidance

Use this document to create RFP requirements:

- MUST requirements → Mandatory RFP line items
- SHOULD requirements → Scored RFP criteria
- MAY requirements → Bonus points

**Include in RFP**:
- Request proof of capability (not just "yes we support X")
- Request performance benchmarks (EPS, search latency, alert latency)
- Request customer references at similar scale

### 10.2 Proof of Concept (POC)

Before procurement, conduct POC:

1. **Ingest real logs** (not vendor sample data)
2. **Test critical use cases** (correlation, baseline, threat intel)
3. **Measure performance** (ingestion, search, alert latency)
4. **Involve SOC analysts** (usability matters as much as features)
5. **Validate integrations** (ticketing, SOAR, TIP)

**POC Failure = Disqualify Vendor** (no matter how impressive the sales demo).

---

**END OF DOCUMENT**

---

*"If your SIEM can't do it, your SOC can't do it. Choose wisely."*  
*—Security Engineering Wisdom*

*"Perfect is the enemy of good, but good is the enemy of 'we have no logs because storage filled up'."*  
*—Feynman (probably)*