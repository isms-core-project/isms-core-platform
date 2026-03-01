<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.15.2-UG:framework:UG:a.8.15.2 -->
**ISMS-IMP-A.8.15.2-UG - Log Collection & Centralization Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Log Collection & Centralization Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.15.2-UG |
| **Related Policy** | ISMS-POL-A.8.15 (Logging) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.15 (Logging) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.8.15 (Logging)
- ISMS-IMP-A.8.15.1 (Log Source Inventory Assessment)
- ISMS-IMP-A.8.15.3 (Log Protection & Retention Assessment)
- ISMS-IMP-A.8.15.4 (Log Analysis & Review Assessment)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.15.2-TG.

---

**Audience:** SOC Team, SIEM Administrators, IT Operations, Network Team

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | SIEM Platform Details | Document SIEM platform configuration and capabilities |
| 3 | Log Forwarder Inventory | Inventory of log forwarders and collection agents |
| 4 | Collection Reliability | Assess log collection reliability and coverage rates |
| 5 | Integration Architecture | Document log collection integration architecture |
| 6 | SIEM Storage & Capacity | Assess SIEM storage capacity and scaling |
| 7 | Log Parsing & Normalisation | Assess log parsing and normalisation quality |
| 8 | SIEM Performance Metrics | Track SIEM performance and ingestion metrics |
| 9 | Data Quality Assessment | Assess centralised log data quality |
| 10 | Encryption & Authentication | Verify log transmission encryption and authentication |
| 11 | Gap Analysis | Identify collection and centralisation gaps |
| 12 | Evidence Register | Store and reference evidence supporting assessments |
| 13 | Summary Dashboard | Compliance status and key metrics overview |
| 14 | Approval Sign-Off | Management review sign-off and certification |

---

# Assessment Overview

## What This Assessment Evaluates

This assessment evaluates the LOG COLLECTION INFRASTRUCTURE - how logs flow from source systems to centralized SIEM/log management, and whether this infrastructure is reliable, scalable, and properly configured.

**Key Questions Answered:**

- What SIEM or log management infrastructure exists?
- Are ALL identified log sources (from IMP-A.8.15.1) actually forwarding logs to SIEM?
- How reliable is log collection? (Are there gaps? Delays? Failures?)
- What storage architecture supports log retention requirements?
- Are logs protected during transmission?
- What integration methods are used? (Syslog, agents, APIs, cloud connectors)

**What This Assessment Is NOT:**

- NOT about what systems exist (that's IMP-A.8.15.1 - Log Source Inventory)
- NOT about what's in the logs or how they're reviewed (that's IMP-A.8.15.4 - Log Analysis)
- NOT about retention compliance (that's IMP-A.8.15.3 - Log Protection & Retention)

This is purely about the **INFRASTRUCTURE** and **DATA FLOW** - getting logs from sources to centralized storage.

## Why This Matters

This assessment verifies [Organisation]'s compliance with:

- **ISO/IEC 27001:2022 Control A.8.15**: Logs must be "kept" - centralized collection ensures logs aren't lost when systems fail or are compromised
- **ISMS-POL-A.8.15, Section 2.2 (Log Protection)**: Immediate forwarding to centralized SIEM prevents local log deletion/tampering
- **ISMS-POL-A.8.15, Section 2.3 (Log Retention)**: Storage architecture must support minimum retention periods
- **PCI DSS v4.0.1 Requirement 10.5.1** (if applicable): Centralized log management required for payment card systems
- **DORA/NIS2** (if applicable): ICT system monitoring requires centralized logging infrastructure

**Security Impact**: 

- **Attackers delete local logs** - centralized collection preserves evidence even if source system compromised
- **Log gaps create blind spots** - unreliable collection means missed security events
- **Investigation failures** - without centralized logs, incident investigation is impossible

**Compliance Impact**: 

- **Major non-conformity** if centralized logging not implemented for critical systems
- **Auditors verify** log collection reliability and coverage in ISO 27001 audits

**Audit Evidence**: This assessment workbook provides **objective evidence** of centralized logging implementation.

## Assessment Outputs

**Primary Deliverable**: Excel workbook with 11 sheets containing:

1. **SIEM Infrastructure Inventory**: Centralized log management platforms documented
2. **Log Collection Coverage**: % of identified log sources actually forwarding to SIEM
3. **Collection Reliability Metrics**: Gaps, failures, delays quantified
4. **Integration Methods**: How each log source connects to SIEM (protocol, agent, API)
5. **Storage Architecture**: Tiered storage design (hot/warm/cold) supporting retention
6. **Network Infrastructure**: Bandwidth, connectivity, firewall rules supporting log forwarding
7. **Encryption & Security**: TLS encryption, authentication methods for log transmission
8. **Gap Analysis**: Missing collection, unreliable sources, infrastructure weaknesses
9. **Compliance Scoring**: % compliance with policy requirements

**Typical Assessment Results**:

- **SIEM Infrastructure**: 1-3 SIEM platforms (primary + DR/backup)
- **Collection Coverage**: 85-98% (target: >=95%)
- **Collection Reliability**: 95-99% uptime (target: >=98%)
- **Gaps Identified**: 5-20 log sources not yet integrated, network bottlenecks, authentication issues

## Relationship to Other Assessments

**Sequential Dependencies**:

```
IMP-A.8.15.1 (Log Source Inventory)
    |
    v
    Identifies WHAT systems should log
    |
    v
IMP-A.8.15.2 (Log Collection) <-- YOU ARE HERE
    |
    v
    Verifies logs actually FLOWING to SIEM
    |
    v
IMP-A.8.15.3 (Protection & Retention)
    |
    v
    Verifies logs PROTECTED and RETAINED
    |
    v
IMP-A.8.15.4 (Analysis & Review)
    |
    v
    Verifies logs ANALYZED and REVIEWED
    |
    v
Summary Dashboards (per workbook)
    |
    v
    Findings tracked in Summary Dashboards
```

**Recommended Order**: Complete IMP-A.8.15.1 FIRST (know what log sources exist), then complete this assessment (verify they're forwarding logs).

---

# Prerequisites

**Before Starting This Assessment:**

## Required Completed Work

**CRITICAL**: You MUST have completed **ISMS-IMP-A.8.15.1 (Log Source Inventory Assessment)** first.

**Why?** This assessment checks whether log sources identified in IMP-A.8.15.1 are forwarding logs. You need to know WHAT sources exist before verifying they're connected.

**If IMP-A.8.15.1 not complete:**

- STOP - complete IMP-A.8.15.1 first
- This assessment will reference the IMP-A.8.15.1 workbook for log source list

## Required Access

**SIEM Platform Access**:

- Read access to SIEM administration console
- Ability to view log source configurations
- Access to collection statistics/metrics
- Permission to export SIEM configuration (for evidence)

**Infrastructure Access**:

- Network diagrams showing log forwarding paths
- Firewall rules documentation for log traffic
- Storage system access (capacity reports, retention configuration)
- Cloud logging configuration (if applicable - CloudTrail, Azure Monitor, GCP Cloud Logging)

**Operational Metrics**:

- SIEM uptime/availability reports (last 3-6 months)
- Log collection failure alerts/incidents
- Storage capacity utilization trends
- Network bandwidth monitoring data

## Required Personnel

**Who Should Complete This Assessment**:

**Primary Responsibility**:

- **SIEM Administrator**: Knows SIEM configuration, log source integrations
- **SOC Lead**: Understands operational requirements, collection reliability

**Supporting Input Required From**:

- **IT Operations**: Storage infrastructure, network connectivity
- **Network Team**: Firewall rules, bandwidth, routing
- **System Administrators**: Log forwarding configuration on source systems
- **Cloud Team**: Cloud logging services configuration (if applicable)

**Estimated Time**: 8-12 hours (distributed across multiple personnel over 1-2 weeks)

## Required Tools & Documentation

**Tools**:

- SIEM administration interface access
- Network monitoring/mapping tools
- Storage management console
- Previous IMP-A.8.15.1 workbook (log source inventory)

**Documentation**:

- SIEM architecture diagrams
- Network topology diagrams
- Log forwarding configuration standards
- Storage architecture documentation
- Previous assessment results (if repeat assessment)

---

# Assessment Workflow

## Recommended Completion Sequence

**Phase 1: Infrastructure Documentation (Sheets 1-4)**

- Sheet 1: Instructions (read thoroughly)
- Sheet 2: SIEM Infrastructure Inventory (document all SIEM platforms)
- Sheet 3: Storage Architecture (document tiered storage design)
- Sheet 4: Network Infrastructure (document connectivity and bandwidth)

**Phase 2: Collection Verification (Sheets 5-7)**

- Sheet 5: Log Source Coverage (import from IMP-A.8.15.1, verify forwarding status)
- Sheet 6: Integration Methods (document how each source connects)
- Sheet 7: Collection Reliability Metrics (analyse gaps, delays, failures)

**Phase 3: Security & Compliance (Sheets 8-9)**

- Sheet 8: Encryption & Authentication (verify TLS, verify authentication methods)
- Sheet 9: Gap Analysis (identify missing sources, reliability issues, security gaps)

**Phase 4: Review & Approval (Sheets 10-11)**

- Sheet 10: Evidence Register (document all supporting evidence)
- Sheet 11: Approval Sign-Off (three-level approval process)

**Estimated Timeline**:

- Phase 1: 3-4 hours (infrastructure documentation)
- Phase 2: 4-6 hours (collection verification - most time-consuming)
- Phase 3: 2-3 hours (security verification and gap analysis)
- Phase 4: 1-2 hours (evidence collection and approvals)

**Total**: 10-15 hours (spread over 1-2 weeks to gather inputs from multiple teams)

## Iterative Approach

**Don't try to complete everything in one sitting.** This is a collaborative assessment:

**Week 1**:

- SIEM Administrator completes infrastructure sheets (1-4)
- IT Operations provides storage architecture input
- Network Team provides network infrastructure input

**Week 2**:

- SIEM Administrator completes collection coverage verification (Sheet 5)
- System Administrators verify log forwarding configurations
- SOC reviews collection reliability metrics (Sheet 7)

**Week 3**:

- Security Team verifies encryption and authentication (Sheet 8)
- Gap analysis workshop with SIEM Admin + IT Ops + SOC (Sheet 9)
- Evidence collection and approval process (Sheets 10-11)

## Data Collection Methods

**SIEM Configuration Export**:

- Export log source list from SIEM (provides current collection status)
- Export collection statistics (log volume per source, collection failures)
- Screenshot SIEM dashboard showing active log sources

**Infrastructure Verification**:

- Network diagrams (visually verify log forwarding paths)
- Firewall rule exports (verify log traffic allowed)
- Storage capacity reports (verify adequate capacity)
- Cloud service console screenshots (CloudTrail, Azure Monitor, etc.)

**Operational Metrics**:

- SIEM uptime reports (prove availability meets policy requirement)
- Collection failure alerts (quantify reliability issues)
- Bandwidth utilization graphs (verify network capacity adequate)

---

# Completing Each Sheet

## Sheet 1: Instructions & Legend

**Purpose**: Understand assessment methodology and scoring criteria.

**Completion**:
1. Read instructions thoroughly
2. Review scoring methodology (0-100% compliance scale)
3. Note color coding (Red = Critical Gap, Yellow = Improvement Needed, Green = Compliant)
4. Understand what "compliance %" means for this assessment

**Time**: 15-20 minutes (first-time users), 5 minutes (returning users)

## Sheet 2: SIEM Infrastructure Inventory

**Purpose**: Document all centralized log management platforms.

**What to Document**:

**For Each SIEM Platform**:

- SIEM Name (e.g., Splunk, ELK Stack, QRadar, Microsoft Sentinel, Chronicle, LogRhythm)
- Deployment Type (On-premises, Cloud-hosted, Hybrid, SaaS)
- Version/Build
- Primary Use Case (Security events, Compliance, Operations, All logs)
- Capacity (Events Per Second - EPS rating)
- Current Utilization (% of capacity used)
- Licensing (Licensed EPS, license expiration, license type)
- Geographic Location (Region, datacenter, availability zone)
- High Availability (Clustered? DR/backup? RPO/RTO?)
- Maintenance Window (scheduled downtime, maintenance frequency)

**Evidence Required**:

- SIEM platform dashboard screenshot showing version and capacity
- Architecture diagram showing SIEM deployment
- License documentation (redact sensitive details, show capacity and expiration)

**Common Scenarios**:

**Single SIEM Deployment**:

- Document primary SIEM
- Note if backup/DR exists or is missing (Gap!)

**Multiple SIEM Platforms**:

- Document each platform
- Note purpose (Security SIEM vs. Operations SIEM vs. Compliance SIEM)
- Verify no gaps in coverage (all log sources feeding to appropriate SIEM)

**Cloud-Native Logging**:

- Document cloud provider logging (CloudTrail, Azure Monitor, GCP Cloud Logging)
- Note if forwarded to centralized SIEM or standalone
- If standalone, assess coverage completeness

**Time**: 1-2 hours

## Sheet 3: Storage Architecture

**Purpose**: Document tiered storage design supporting retention requirements.

**What to Document**:

**For Each Storage Tier**:

**Hot/Online Storage**:

- Storage System (SIEM internal, SAN, NAS, Object Storage, Cloud Storage)
- Total Capacity (TB)
- Current Utilization (TB used, % utilization)
- Retention Period (Days/Months logs kept online)
- Performance (IOPS, latency, search speed)
- Redundancy (RAID level, replication, backup)
- Geographic Location

**Warm/Nearline Storage**:

- Storage System (compressed storage, secondary storage tier)
- Total Capacity (TB)
- Current Utilization
- Retention Period
- Access Time (how long to retrieve logs)
- Compression Ratio (if applicable)

**Cold/Archive Storage**:

- Storage System (tape, object storage, write-once media, cloud archive)
- Total Capacity (TB)
- Current Utilization
- Retention Period (matches policy requirement - typically 7 years total)
- Access Time (hours/days to retrieve)
- Write-Once Capability (WORM storage for compliance)

**Capacity Planning**:

- Current log ingestion rate (GB/day, TB/month)
- Historical growth trend (% growth year-over-year)
- Projected capacity needs (12 months forward projection)
- Capacity alerts (threshold for warnings, currently alerting?)

**Evidence Required**:

- Storage capacity reports from storage management console
- SIEM storage utilization dashboard screenshot
- Capacity planning spreadsheet or forecast
- Storage architecture diagram showing tiers

**Compliance Check**:

- Does total retention (hot + warm + cold) meet policy requirements?
- Is capacity adequate for next 12 months + 20% buffer?
- Are alerts configured for 80% capacity threshold?

**Time**: 1-2 hours

## Sheet 4: Network Infrastructure

**Purpose**: Verify network connectivity supports reliable log forwarding.

**What to Document**:

**For Each Network Path (Source Systems -> SIEM)**:

**Network Connectivity**:

- Source Network Segment (e.g., Production LAN, DMZ, Management Network)
- Destination (SIEM IP address, cloud endpoint, collector IP)
- Protocol Used (Syslog UDP/TCP, HTTPS, proprietary protocol)
- Port Number
- Bandwidth Available (Mbps/Gbps)
- Current Utilization (% of bandwidth used for logs)
- Latency (milliseconds average)
- Packet Loss (% packet loss observed)

**Firewall Rules**:

- Firewall Name/Location
- Rule ID/Number
- Source IP Range
- Destination IP/Port
- Action (Allow/Deny)
- Last Review Date

**Routing & Segmentation**:

- VLAN/Subnet Information
- Routing Protocol (static routes, dynamic routing)
- Network Segmentation Boundaries (logs crossing security zones?)
- NAT/PAT (Network Address Translation affecting source IPs?)

**Redundancy & Resilience**:

- Redundant Network Paths (multiple routes to SIEM?)
- Load Balancing (multiple SIEM collectors?)
- Failover Configuration (what happens if primary path fails?)

**Evidence Required**:

- Network diagram showing log forwarding paths
- Firewall rule exports (sanitized for sensitivity)
- Bandwidth utilization graphs
- Network monitoring data showing connectivity uptime

**Common Issues to Identify**:

- Insufficient bandwidth (log forwarding saturating network link)
- Firewall rules missing or incorrect (blocking log traffic)
- Single point of failure (no redundant paths)
- High latency or packet loss (indicating network congestion)

**Time**: 2-3 hours (requires coordination with Network Team)

## Sheet 5: Log Source Coverage

**Purpose**: Verify identified log sources (from IMP-A.8.15.1) are actually forwarding logs to SIEM.

**CRITICAL**: This sheet IMPORTS data from **IMP-A.8.15.1 Sheet 2 (System Inventory)**.

**How It Works**:

1. **Automatic Import**: Python script generates this sheet with log source list from IMP-A.8.15.1
2. **Verification**: For EACH log source, verify if logs are arriving in SIEM
3. **Status Assignment**: Mark as "Forwarding", "Partial", "Not Forwarding", "Planned"

**For Each Log Source**:

**From IMP-A.8.15.1 (Auto-Populated)**:

- System Name
- System Type (Server, Network Device, Security Tool, Application, Cloud Service)
- Data Classification (Restricted, Confidential, Internal, Public)
- System Criticality (Critical, High, Medium, Low)
- System Owner

**To Be Completed (Manual)**:

- **Collection Status**: Dropdown (Forwarding, Partial, Not Forwarding, Planned, N/A)
- **SIEM Destination**: Which SIEM receives logs (if multiple SIEMs)
- **Collection Method**: Agent-based, Syslog, API, Cloud Connector, Manual Upload, None
- **Last Log Received**: Timestamp of most recent log (verify current)
- **Daily Log Volume**: GB/day or Events/day
- **Verification Method**: How verified (SIEM search, dashboard, agent status, API check)
- **Gap Reason** (if not forwarding): Technical limitation, Planned but not implemented, Not required per risk assessment, Under investigation
- **Remediation Plan** (if gap): Target date, responsible party, estimated effort

**Status Definitions**:

- **Forwarding**: Logs actively arriving, verified within last 24 hours, no gaps
- **Partial**: Some logs arriving but incomplete (missing event types, intermittent, delays)
- **Not Forwarding**: No logs arriving, or last log >7 days old
- **Planned**: Integration approved and scheduled but not yet implemented
- **N/A**: Explicitly excluded per approved exception (reference exception ID from policy Section 3.3)

**Verification Methods**:

- **SIEM Search**: Search for recent logs from this source (most reliable method)
- **Dashboard Check**: SIEM dashboard shows source as "active" or "connected"
- **Agent Status**: Logging agent reports "healthy" and "connected" status
- **API Check**: API query confirms logs flowing (for cloud services)
- **Manual Inspection**: Check SIEM raw log viewer for source system logs

**Evidence Per Source**:

- SIEM search result screenshot (showing recent logs from this source)
- Agent status screenshot (if agent-based collection)
- Cloud service logging configuration screenshot (if cloud service)

**Time**: 4-6 hours (most time-consuming sheet - verify EACH log source individually)

**Pro Tip**: Filter by criticality first. Verify all "Critical" and "High" systems before "Medium" and "Low". Prioritize effort.

## Sheet 6: Integration Methods

**Purpose**: Document HOW each log source connects to SIEM (technical integration details).

**What to Document**:

**For Each Integration Method**:

**Agent-Based Collection**:

- Agent Software (Splunk Universal Forwarder, Elastic Beats, proprietary agent)
- Agent Version
- Installation Date
- Auto-Update Enabled? (Yes/No - security consideration)
- Configuration Source (centralized management, local config file)
- Health Monitoring (agent reports health status to SIEM?)
- SSL/TLS Encryption (Yes/No)
- Authentication Method (certificate, API key, username/password)

**Syslog (Network Protocol)**:

- Protocol Variant (RFC 3164 legacy, RFC 5424 modern, BSD Syslog, CEF over Syslog)
- Transport (UDP port 514, TCP port 514/6514, TLS port 6514)
- Encryption (None, TLS 1.2, TLS 1.3)
- Reliability (UDP = fire-and-forget, TCP = acknowledged delivery, TLS = encrypted + authenticated)
- Message Format (plain text, structured, JSON embedded)
- Timestamp Format (timezone handling, ISO 8601 compliance)

**API-Based Collection**:

- API Type (REST API, GraphQL, proprietary API)
- Authentication (OAuth 2.0, API key, certificate, bearer token)
- Collection Frequency (real-time webhook, polling every X minutes)
- Rate Limiting (API calls per hour limit, current utilization)
- Error Handling (retry logic, exponential backoff, dead-letter queue)

**Cloud Connectors**:

- Cloud Provider (AWS CloudTrail, Azure Monitor, GCP Cloud Logging, Microsoft 365, Google Workspace)
- Connector Type (native SIEM integration, third-party connector, custom script)
- Service Account/Credentials (permissions granted, credential rotation schedule)
- Scope (which cloud resources logged - all, specific services, specific regions)
- Latency (typical delay from event occurrence to SIEM ingestion)

**File-Based Collection**:

- Collection Method (agent reads local files, network file share, FTP/SFTP)
- File Location (log file paths)
- File Rotation Handling (rotate detection, multi-part file handling)
- File Format (plain text, JSON, XML, CSV)
- Parsing Configuration (custom parser, built-in parser, regex-based)

**Database/JDBC Collection**:

- Database Type (SQL Server, Oracle, PostgreSQL, MySQL, MongoDB)
- Connection Method (JDBC, ODBC, native driver)
- Query Schedule (real-time triggers, scheduled queries)
- Credentials (service account, read-only access verified)
- Data Volume (rows per day, GB per day)

**For Each Integration**:

- **Configuration Documentation**: Where is config documented? (config file path, configuration management system, runbook)
- **Change Management**: How are changes tracked? (change tickets, version control, approval process)
- **Troubleshooting Contact**: Who to contact if collection fails? (team, person, escalation path)

**Evidence Required**:

- Configuration screenshots from SIEM showing integration settings
- Agent configuration files (sample, sanitized for credentials)
- Cloud connector permission/role documentation
- Network protocol packet captures (if troubleshooting Syslog issues)

**Compliance Check**:

- Are all integrations using TLS 1.2 or higher for encryption? (per policy Section 2.2)
- Are authentication credentials securely managed? (not hardcoded, rotated regularly)
- Are integrations documented sufficiently for continuity if personnel changes?

**Time**: 2-3 hours

## Sheet 7: Collection Reliability Metrics

**Purpose**: Quantify how reliable log collection is (gaps, delays, failures).

**What to Measure**:

**Overall SIEM Availability**:

- SIEM Uptime % (last 30 days, last 90 days, last 12 months)
- Target: >=99.5% per ISMS-POL-A.8.15 Section 2.4
- Downtime Incidents (count, total duration, root causes)
- Planned vs. Unplanned Downtime (maintenance windows vs. failures)

**Log Source Connectivity**:

- Total Log Sources Expected (from IMP-A.8.15.1)
- Log Sources Currently Forwarding (from Sheet 5)
- Collection Coverage % = (Forwarding / Expected) x 100%
- Target: >=98% per ISMS-POL-A.8.15 Section 2.4

**Collection Gaps & Delays**:

- Log Sources with Gaps (count, list)
- Average Gap Duration (hours/days between expected logs and actual arrival)
- Maximum Gap Duration (longest period without logs from any source)
- Delayed Forwarding (logs arriving but delayed >1 hour from generation)

**Collection Failures**:

- Failed Collection Attempts (count in last 30 days)
- Failure Categories:
  - Network connectivity issues (firewall blocks, routing failures, DNS resolution)
  - Authentication failures (expired credentials, insufficient permissions)
  - Agent failures (agent crash, agent offline, agent misconfigured)
  - API rate limiting (exceeded API quotas, throttled requests)
  - Storage capacity (SIEM storage full, unable to write logs)
  - Unknown/Other
- Mean Time to Detect Failure (how quickly was failure identified?)
- Mean Time to Restore Collection (how quickly was collection restored?)

**Data Quality Issues**:

- Unparsed Logs (logs arriving but SIEM can't parse - count, %)
- Parsing Errors (count, common error patterns)
- Missing Required Fields (logs missing timestamps, source IPs, user IDs)
- Character Encoding Issues (UTF-8 corruption, special characters mangled)

**Alerting Effectiveness**:

- Collection Failure Alerts Configured? (Yes/No for each log source category)
- Alert Threshold (e.g., no logs for >2 hours triggers alert)
- False Positive Rate (alerts fired where collection was actually OK)
- False Negative Rate (collection failures NOT detected by alerts)

**Trending Data**:

- Log Volume Trend (GB/day over last 3-6 months - growing? stable? declining?)
- Collection Reliability Trend (improving? degrading? stable?)
- Incident Frequency Trend (collection failures increasing or decreasing?)

**Evidence Required**:

- SIEM uptime report (from SIEM vendor dashboard or monitoring system)
- Collection failure alert history (SIEM alert logs or ticketing system)
- Log volume graphs (SIEM dashboard showing ingestion rates over time)
- Incident reports for significant collection failures

**Automated Data Collection**:

- Many SIEMs provide APIs or reports for these metrics
- Python script can query SIEM API and populate this sheet automatically
- Manual review still required for qualitative assessment (root causes, trends)

**Time**: 2-3 hours (including SIEM data extraction and analysis)

## Sheet 8: Encryption & Authentication

**Purpose**: Verify log transmission is encrypted and authenticated per policy Section 2.2.

**What to Verify**:

**For Each Log Forwarding Path**:

**Encryption Status**:

- **Encryption Enabled?** (Yes/No)
- **Encryption Protocol**: None, TLS 1.0 (deprecated), TLS 1.1 (deprecated), TLS 1.2 (acceptable), TLS 1.3 (preferred)
- **Cipher Suite**: Strong (AEAD ciphers), Weak (CBC mode, RC4), Unknown
- **Certificate Validation**: Certificate verified? Self-signed? CA-signed? Expired?
- **Perfect Forward Secrecy**: Supported? (Ephemeral key exchange - DHE/ECDHE)

**Policy Compliance**:

- **ISMS-POL-A.8.15 Section 2.2 Requirement**: "Logs SHALL be transmitted over encrypted channels (TLS 1.2 or higher)"
- **Compliant**: TLS 1.2 or TLS 1.3 with strong cipher suites
- **Non-Compliant**: No encryption, TLS 1.0/1.1, weak ciphers
- **Exception Approved?**: If non-compliant, is there an approved exception per policy Section 3.3? (Reference exception ID)

**Authentication Methods**:

- **Authentication Type**:
  - Certificate-based (mutual TLS, client certificate)
  - API Key/Token (bearer token, API key in header)
  - Username/Password (basic auth - discouraged, shared secrets)
  - Pre-shared Key (PSK for Syslog-TLS)
  - IP Whitelisting (not authentication, but access control)
  - None (unauthenticated - HIGH RISK)
- **Credential Strength**:
  - Strong: Certificate-based, long random API keys (>128-bit entropy)
  - Medium: Complex passwords, shorter API keys
  - Weak: Simple passwords, default credentials, hardcoded secrets
- **Credential Rotation**:
  - Rotation Schedule: Not rotated, Annual, Quarterly, On-demand only
  - Last Rotation Date
  - Automated Rotation? (Yes/No)

**Risk Assessment**:

**For Unencrypted or Weakly Authenticated Paths**:

- **Network Exposure**: Is log traffic traversing untrusted networks? (Internet, DMZ, cross-datacenter WAN)
- **Data Sensitivity**: What classification of data is in these logs? (Restricted, Confidential, Internal)
- **Compensating Controls**: Are there mitigating factors? (physically secured network, VPN encapsulation, network segmentation)
- **Risk Level**: Critical (unencrypted restricted data over Internet), High (unencrypted confidential data over LAN), Medium (unauthenticated internal data over trusted network), Low (internal data over physically secured network)

**Remediation Priorities**:

**Critical Priority** (fix immediately):

- No encryption for restricted/confidential data logs
- Logs transmitted over Internet without encryption
- Default or hardcoded credentials in use
- Expired or invalid certificates

**High Priority** (fix within 30 days):

- TLS 1.0 or TLS 1.1 (deprecated protocols)
- Weak cipher suites (CBC mode, non-AEAD)
- No authentication for security-critical log sources
- Credentials not rotated in >12 months

**Medium Priority** (fix within 90 days):

- IP whitelisting as sole authentication (add certificate or API key)
- Self-signed certificates without proper trust chain
- Manual credential rotation (automate)

**Evidence Required**:

- TLS certificate details (from SIEM, from log forwarder configuration)
- Cipher suite configuration screenshots
- Authentication configuration documentation
- Network diagrams showing encrypted vs. unencrypted paths

**Time**: 1-2 hours

## Sheet 9: Gap Analysis

**Purpose**: Consolidate all identified gaps, prioritize by risk, and create remediation plan.

**Gap Categories**:

**Category 1: Missing Log Source Coverage**

- Log sources identified in IMP-A.8.15.1 but NOT forwarding to SIEM
- Gap Impact: Blind spots - no visibility into these systems
- Priority: Critical (if critical system), High (if high-value data), Medium (standard systems)

**Category 2: Collection Reliability Issues**

- Log sources forwarding intermittently, with gaps or delays
- Gap Impact: Incomplete evidence, missed security events
- Priority: High (if critical systems), Medium (if standard systems)

**Category 3: Encryption Not Implemented**

- Log transmission without TLS encryption (policy Section 2.2 violation)
- Gap Impact: Confidentiality risk - logs readable in transit, potential data exposure
- Priority: Critical (if restricted/confidential data), High (if internal data over untrusted networks)

**Category 4: Weak or No Authentication**

- Log sources sending unauthenticated logs, weak passwords, expired credentials
- Gap Impact: Integrity risk - unauthorised log injection possible, log spoofing
- Priority: High (security-critical logs), Medium (operational logs)

**Category 5: Insufficient Storage Capacity**

- Storage projected to run out before next capacity expansion
- Gap Impact: Log loss, retention non-compliance
- Priority: Critical (if <30 days to capacity exhaustion), High (if <90 days)

**Category 6: Network Infrastructure Weaknesses**

- Single point of failure, insufficient bandwidth, no redundancy
- Gap Impact: Availability risk - log collection failures during outages
- Priority: Medium (if redundancy missing), Low (if adequate current capacity but no growth buffer)

**For Each Gap**:

- **Gap ID**: Unique identifier (e.g., COLL-001, COLL-002)
- **Gap Category**: From categories above
- **Gap Description**: Clear description of what's missing or inadequate
- **Affected System(s)**: Which log sources or infrastructure affected
- **Policy Reference**: Which policy requirement violated (e.g., "ISMS-POL-A.8.15 Section 2.2 - TLS Encryption Required")
- **Risk Rating**: Critical, High, Medium, Low (use risk matrix below)
- **Business Impact**: What could go wrong? (missed breach, compliance failure, investigation impairment)
- **Remediation Plan**:
  - Proposed Solution (what needs to be done)
  - Responsible Party (who will fix it)
  - Target Completion Date
  - Estimated Effort (hours/days)
  - Budget Required (if additional hardware/software needed)
- **Compensating Controls** (if any): Temporary mitigations while gap remains open
- **Exception Status**: Approved exception exists? (Reference exception ID from policy Section 3.3)

**Risk Rating Matrix**:

| Impact | Likelihood | Risk Rating |
|--------|-----------|-------------|
| High | Likely | **Critical** |
| High | Possible | **High** |
| Medium | Likely | **High** |
| Medium | Possible | **Medium** |
| Low | Likely | **Medium** |
| Low | Possible | **Low** |

**Impact Factors**:

- **High Impact**: Restricted/Confidential data, Critical systems, Compliance-critical logs (PCI DSS v4.0.1, HIPAA, SOX)
- **Medium Impact**: Internal data, High-value systems, Security monitoring impact
- **Low Impact**: Public data, Low-value systems, Operational convenience only

**Likelihood Factors**:

- **Likely**: Known vulnerabilities, past incidents, inadequate controls
- **Possible**: Some controls exist but gaps, no incidents yet but conditions present
- **Unlikely**: Strong compensating controls, low exposure, no threat vectors identified

**Remediation Tracking**:

- Gaps should be tracked in organisation's issue tracking system (Jira, ServiceNow, etc.)
- Reference tracking ticket ID in this sheet
- Update status quarterly during assessment refreshes

**Time**: 2-3 hours (gap identification and remediation planning requires cross-functional input)

---

# Evidence Collection

## Evidence Types

**For SIEM Infrastructure (Sheet 2)**:

- SIEM platform version and license information (screenshot from admin console)
- Architecture diagram (showing SIEM components, collectors, indexers, storage)
- Capacity report (current EPS utilization, storage consumption)
- High availability configuration (clustering documentation, DR procedures)

**For Storage Architecture (Sheet 3)**:

- Storage capacity reports (from storage management system)
- Retention configuration (screenshot of retention policy settings)
- Capacity trend graphs (6-12 months historical data)
- Capacity planning projections (forecasting spreadsheet or tool output)

**For Network Infrastructure (Sheet 4)**:

- Network diagram (showing log forwarding paths)
- Firewall rules (exports or screenshots - sanitize sensitive IPs)
- Bandwidth utilization graphs (from network monitoring system)
- Routing table excerpts (showing SIEM reachability)

**For Log Source Coverage (Sheet 5)**:

- SIEM search results (screenshot showing recent logs from each source)
- Log source status dashboard (SIEM internal view of connected sources)
- Agent health reports (if agent-based collection)
- Cloud service logging configuration screenshots

**For Integration Methods (Sheet 6)**:

- Configuration file samples (agent configs, syslog configs - redact credentials)
- SIEM input configuration screenshots
- API permission documentation (cloud service accounts, API key permissions)
- Integration test results (proof that logs flowing correctly)

**For Collection Reliability (Sheet 7)**:

- SIEM uptime report (last 90 days minimum)
- Collection failure alert history (alert logs or ticketing system exports)
- Log volume graphs (trend analysis over 3-6 months)
- Incident reports (major collection outages with root cause analysis)

**For Encryption & Authentication (Sheet 8)**:

- TLS certificate details (certificate chain, expiration dates, cipher suites)
- Configuration screenshots (showing TLS/encryption enabled)
- Authentication configuration documentation
- Security assessment reports (if encryption/auth recently audited)

**For Gap Analysis (Sheet 9)**:

- Gap descriptions (sufficient detail to understand issue)
- Remediation plans (documented proposals with timelines)
- Exception approvals (if gaps have approved exceptions per policy Section 3.3)

## Evidence Collection Best Practices

**Screenshots**:

- Include date/time stamps in screenshots
- Show sufficient context (don't crop too tightly)
- Redact sensitive information (IP addresses, credentials, internal hostnames if necessary)
- Name files clearly (e.g., "SIEM_Dashboard_Capacity_2026-01-21.png")

**Exports & Reports**:

- Export in readable formats (PDF, Excel, CSV)
- Include metadata (date generated, who ran report, system/tool used)
- Sanitize for sensitivity before storing in assessment workbook folder

**Documentation References**:

- If evidence exists in other documentation, reference it (don't duplicate)
- Provide document name, version, location (network path, SharePoint, document management system)
- Verify document is current (not outdated)

**Evidence Organisation**:

- Create evidence folder structure matching assessment sheets:

  ```
  ISMS-IMP-A.8.15.2_Evidence/
  |-- Sheet02_SIEM_Infrastructure/
  |-- Sheet03_Storage_Architecture/
  |-- Sheet04_Network_Infrastructure/
  |-- Sheet05_Log_Source_Coverage/
  |-- Sheet06_Integration_Methods/
  |-- Sheet07_Collection_Reliability/
  |-- Sheet08_Encryption_Authentication/
  `-- Sheet09_Gap_Analysis/
  ```

**Evidence Retention**:

- Retain evidence for minimum 7 years (matches log retention policy)
- Evidence = audit trail proving assessment was evidence-based, not theoretical
- Store securely (evidence may contain sensitive configuration details)

---

# Common Pitfalls

## Pitfall: "We think logs are forwarding but haven't verified"

**Problem**: Assuming log collection works without verification.

**Why This Happens**:

- Logs configured to forward but network/firewall issue prevents delivery
- Log forwarder agent installed but not started or misconfigured
- Cloud logging enabled but permissions insufficient to read logs

**How to Avoid**:

- **ALWAYS verify logs arriving in SIEM** with actual search/query (Sheet 5)
- Don't trust agent status "green" - verify logs with your own eyes
- Search for logs from each source with timestamp in last 24 hours

**Evidence of Proper Verification**:

- SIEM search screenshot showing recent logs from EACH source
- Query syntax documented (so verification can be repeated)

## Pitfall: "All logs go to SIEM" (without checking WHICH SIEM)

**Problem**: Multiple SIEM platforms exist, log sources split across platforms, gaps in coverage not identified.

**Why This Happens**:

- Organisation has Security SIEM (Splunk), Operations SIEM (ELK), Compliance SIEM (LogRhythm)
- Assumption that "logging is enabled" means "goes to security SIEM"
- Reality: logs going to operations SIEM, security team has no visibility

**How to Avoid**:

- Document WHICH SIEM receives logs for EACH source (Sheet 5 - "SIEM Destination" column)
- Verify security-relevant logs going to security SIEM (not just any logging system)
- Map log sources to SIEM purposes (Sheet 2 - "Primary Use Case")

## Pitfall: "Encryption is on because we use Syslog over TCP"

**Problem**: TCP Syslog != Encrypted Syslog. TCP provides reliability, not encryption.

**Misconception**:

- Syslog over TCP (port 514) = unencrypted but reliable delivery
- Syslog over TLS (port 6514) = encrypted AND reliable

**How to Avoid**:

- Verify TLS explicitly (Sheet 8 - check protocol is "TLS 1.2" or "TLS 1.3", NOT just "TCP")
- Packet capture verification if uncertain (capture log traffic, verify encrypted or plaintext)
- Don't assume encryption based on port number or TCP transport

## Pitfall: "Collection is 100% reliable" (ignoring gaps/delays)

**Problem**: Overconfidence in collection reliability without metrics.

**Reality**:

- Network outages cause temporary log loss
- Agent crashes cause gaps until detection/restart
- API rate limiting causes delays
- Storage capacity issues cause log drops

**How to Avoid**:

- Quantify reliability with actual metrics (Sheet 7 - uptime %, gap duration, failure count)
- Review SIEM alerts for collection failures (don't just assume it works)
- Trending analysis over 3-6 months (catches intermittent issues)

## Pitfall: "We'll fix gaps later" (without documenting gaps)

**Problem**: Gaps identified but not tracked, forgotten, never remediated.

**Why This Happens**:

- No formal gap tracking process
- Gaps seem minor at assessment time
- Responsibility unclear (whose job to fix?)

**How to Avoid**:

- **Document EVERY gap in Sheet 9** (even if "minor")
- Assign clear ownership (responsible party column)
- Set target dates (creates accountability)
- Track in issue tracking system (Jira, ServiceNow)
- Review gap closure progress in quarterly assessment updates

## Pitfall: "Evidence collection can wait until audit"

**Problem**: Audit announced, scramble to collect evidence, missing evidence for historical configurations.

**Why This Happens**:

- Evidence collection seen as "extra work"
- Screenshots not taken at time of assessment
- Configurations changed since assessment, historical evidence lost

**How to Avoid**:

- Collect evidence **DURING assessment** (Sheet 10 - Evidence Register)
- Take screenshots at time of verification (later screenshots may not match assessment date)
- Store evidence securely (organised folder structure per section 5.2)
- Evidence retention = audit readiness

---

# Quality Checklist

**Before Submitting Assessment for Approval:**

## Completeness Checks

- [ ] All sheets completed (no sheets left blank unless explicitly N/A with justification)
- [ ] All yellow cells filled in (yellow = user input required)
- [ ] All dropdown selections made (no cells left on "Select..." placeholder)
- [ ] All log sources from IMP-A.8.15.1 verified in Sheet 5 (none skipped)
- [ ] Evidence collected for all critical assertions (Sheet 10 - Evidence Register complete)
- [ ] Gap analysis complete with remediation plans (Sheet 9 - no gaps left without plan)

## Accuracy Checks

- [ ] SIEM infrastructure information verified (Sheet 2 - version numbers, capacity, licensing accurate)
- [ ] Storage capacity calculations correct (Sheet 3 - current utilization + projected growth reasonable)
- [ ] Network infrastructure documentation current (Sheet 4 - firewall rules reflect current state, not historical)
- [ ] Log source coverage verified with recent search results (Sheet 5 - verification timestamps within last week)
- [ ] Collection reliability metrics from recent data (Sheet 7 - not outdated metrics from 6+ months ago)
- [ ] Encryption/authentication status verified (Sheet 8 - TLS versions confirmed, not assumed)

## Compliance Alignment

- [ ] Policy references correct (all references point to ISMS-POL-A.8.15 v1.0 consolidated policy)
- [ ] Regulatory requirements identified (PCI DSS v4.0.1, HIPAA, DORA/NIS2 applicability determined per ISMS-POL-00)
- [ ] Exception approvals documented (any non-compliance has exception reference or remediation plan)
- [ ] Retention requirements met (storage architecture supports minimum retention periods per policy Section 2.3)

## Evidence Quality

- [ ] Evidence file naming clear and consistent
- [ ] Evidence contains date/time metadata (to prove currency)
- [ ] Sensitive information redacted (no exposed credentials, excessive internal details)
- [ ] Evidence organised in folder structure (per section 5.2)
- [ ] Evidence Register (Sheet 10) references match actual files (no broken references)

## Approval Readiness

- [ ] Assessment completed by qualified personnel (SIEM Admin, SOC Lead - not delegated to unqualified staff)
- [ ] Cross-functional input obtained (IT Ops, Network Team, System Admins provided input where needed)
- [ ] Review by InfoSec Manager scheduled (before final CISO approval)
- [ ] Gaps socialized with stakeholders (no surprises in approval meeting)
- [ ] Remediation plans have stakeholder buy-in (responsible parties aware and agree to timelines)

**If ANY checkbox is unchecked**: Assessment is NOT ready for approval. Complete missing items before proceeding to approval.

---

# Review & Approval

## Three-Level Approval Process

**Level 1: Technical Review**

- **Reviewer**: SIEM Administrator (primary completer) + SOC Lead
- **Focus**: Technical accuracy, completeness of coverage verification, realistic remediation plans
- **Timeline**: 2-3 business days for review and corrections
- **Outcome**: Assessment technically accurate and complete

**Level 2: Management Review**

- **Reviewer**: Information Security Manager
- **Focus**: Gap prioritization correct, remediation plans aligned with organisational priorities, resource requirements reasonable
- **Timeline**: 3-5 business days for review and discussion
- **Outcome**: Remediation plans approved, resources committed, timelines realistic

**Level 3: Executive Approval**

- **Reviewer**: CISO
- **Focus**: Strategic alignment, risk acceptance for unfixed gaps, budget approval for significant investments
- **Timeline**: 1-2 weeks for review and final sign-off
- **Outcome**: Assessment officially approved, gaps formally tracked, execution authorised

## Approval Workflow

**Step 1: Assessment Completion**

- SIEM Administrator completes all sheets with SOC Lead input
- Quality checklist (Section 7) fully checked
- Evidence collected and organised

**Step 2: Level 1 Technical Review**

- SIEM Administrator self-reviews
- SOC Lead peer-reviews
- Corrections made, clarifications added
- Both sign Sheet 11 (Approval Sign-Off)

**Step 3: Level 2 Management Review**

- InfoSec Manager reviews assessment
- Gap prioritization discussion (are priorities correct?)
- Remediation feasibility discussion (are timelines realistic?)
- Resource requirements clarification (budget, personnel, vendor support)
- InfoSec Manager signs Sheet 11 after satisfactory review

**Step 4: Level 3 Executive Approval**

- CISO reviews executive summary (Sheet 11 - Summary Dashboard)
- CISO reviews critical/high-priority gaps
- CISO reviews remediation budgets and resource requests
- CISO approves or requests modifications
- CISO signs Sheet 11 as final approval

**Step 5: Post-Approval Actions**

- Assessment workbook marked as "Approved" (Sheet 11 - Status field updated)
- Gaps entered into issue tracking system (Jira, ServiceNow) for remediation tracking
- Assessment results included in quarterly compliance reporting
- Assessment stored in ISMS document repository for audit evidence

## Approval Timeline

**Typical Timeline from Start to Final Approval**:

- **Week 1-2**: Assessment completion (SIEM Admin, SOC Lead, cross-functional input)
- **Week 3**: Level 1 Technical Review (corrections, evidence supplementation)
- **Week 3-4**: Level 2 Management Review (InfoSec Manager review and discussion)
- **Week 4-5**: Level 3 Executive Approval (CISO review and sign-off)

**Total**: 4-5 weeks from initiation to final approval (for well-executed assessments with minimal corrections)

**Expedited Process** (if needed for audit or compliance deadline):

- Concurrent reviews (InfoSec Manager review while Level 1 happening)
- Focused review on critical findings only (defer detailed review of non-critical items)
- Timeline: 2-3 weeks (minimum realistic timeline)

---

**END OF USER GUIDE**

---

*"Centralised logging is the nervous system of security operations."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
