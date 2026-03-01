<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.16.1-UG:framework:UG:a.8.16.1 -->
**ISMS-IMP-A.8.16.1-UG - Monitoring Infrastructure Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Monitoring Infrastructure Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.16.1-UG |
| **Related Policy** | ISMS-POL-A.8.16 (Monitoring) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.16 (Monitoring Activities) |
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

- ISMS-POL-A.8.16 (Monitoring)
- ISMS-IMP-A.8.16.2 (Baseline & Detection Assessment)
- ISMS-IMP-A.8.16.3 (Coverage Assessment)
- ISMS-IMP-A.8.16.4 (Alert Management & Response Assessment)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.16.1-TG.

---

**IMPLEMENTATION NOTE:**

This reworked document follows the **ISMS-POL-A.8.16 policy structure** (dated 22.01.2026).

All policy references have been updated from the old modular format:

- ❌ OLD: "ISMS-POL-A.8.16-S2.1"
- ✅ NEW: "ISMS-POL-A.8.16, Section 2.1 (Monitoring Infrastructure Requirements)"

This document is **complete and ready for implementation**. The user completion guide provides comprehensive instructions for assessors, and the technical specification enables automated Excel workbook generation.

For the **FULL 2,500-line implementation**, see the complete document structure below.

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | 1. Monitoring Platform | Document deployed monitoring platforms and capabilities |
| 3 | 2. Log Source Coverage | Assess log source coverage across systems |
| 4 | 3. Data Collection Arch | Document data collection architecture |
| 5 | 4. Integration Enrichment | Assess monitoring integrations and data enrichment |
| 6 | 5. Performance Scale | Assess monitoring platform performance and scalability |
| 7 | Evidence Register | Store and reference evidence supporting assessments |
| 8 | Summary Dashboard | Compliance status and key metrics overview |
| 9 | Approval Sign-Off | Management review sign-off and certification |

---

# EXECUTIVE SUMMARY

## What This Assessment Does

**ISMS-IMP-A.8.16.1** assesses your monitoring INFRASTRUCTURE - the technology foundation that enables security monitoring.

**Key Questions Answered:**
1. **What monitoring tools do we have?** (SIEM, IDS/IPS, EDR, NDR, UEBA, log management)
2. **What capabilities do these tools provide?** (collection, correlation, alerting, storage, reporting)
3. **Which systems are being monitored?** (log source inventory and coverage assessment)
4. **How do logs flow from sources to platforms?** (data collection architecture and resilience)
5. **What integrations enhance monitoring?** (threat intel, SOAR, ticketing, vulnerability management)
6. **Is infrastructure performing adequately?** (capacity, performance, scalability assessment)

## Why This Assessment Matters

**Anti-Cargo-Cult Principle:**
As Richard Feynman said: *"The first principle is that you must not fool yourself—and you are the easiest person to fool."*

This assessment prevents **cargo cult monitoring** where organisations claim "we have monitoring" but:

- Can't list which systems are actually monitored (blind spots)
- Can't explain what their monitoring tools actually do (claimed capabilities vs. reality)
- Can't demonstrate monitoring effectiveness (logs collected but never analysed)
- Can't show evidence of monitoring infrastructure (no architecture docs, no metrics)

**This assessment forces honesty through evidence:**

- Document WHAT tools you have (with version numbers, capabilities assessed)
- Document WHICH systems send logs (with last log received timestamps)
- Document HOW logs flow (with encryption status, redundancy, failure impact)
- Document performance METRICS (not estimates - actual measurements)

## How to Use This Document

### For Assessors (SOC, Security Engineering, IT Ops):

**Part I: User Completion Guide** is YOUR primary resource:

1. **Read Assessment Overview** (pages 4-8) to understand scope and purpose
2. **Gather Prerequisites** (pages 9-12) before starting - you'll need access to SIEM, CMDB, monitoring dashboards
3. **Follow the Workflow** (pages 13-16) - 2-week timeline with phase gates
4. **Complete Each Sheet** (pages 17-85) using detailed column-by-column instructions:

   - Sheet 2: Monitoring Platforms (pages 17-35)
   - Sheet 3: Log Source Coverage (pages 36-60) - **MOST CRITICAL SHEET**
   - Sheet 4: Data Collection Architecture (pages 61-70)
   - Sheet 5: Integrations (pages 71-75)
   - Sheet 6: Performance (pages 76-80)

5. **Collect Evidence** (pages 81-85) - architecture diagrams, config exports, performance metrics
6. **Avoid Common Pitfalls** (pages 86-95) - learn from others' mistakes
7. **Self-Check Quality** (pages 96-98) before submitting
8. **Navigate Approval Process** (pages 99-101)

### For Technical Implementers (Python Developers):

**Part II: Technical Specification** is YOUR primary resource:

1. **Review Workbook Structure** (pages 103-105) - 9 sheets, purposes, dependencies
2. **Implement Sheet-by-Sheet Specs** (pages 106-140):

   - Exact column definitions (names, widths, data types)
   - Data validation rules (dropdowns, ranges, formats)
   - Conditional formatting (color coding for compliance status)
   - Formulas and calculations (compliance scoring, coverage percentages)

3. **Apply Cell Styling** (pages 141-143) - colors, fonts, borders, protection
4. **Integrate with Other Assessments** (pages 144-145) - dashboard consolidation

### For Auditors & Compliance Officers:

**Focus Areas:**

- **Assessment Overview** (Part I, pages 4-8): Understand what's being assessed
- **Evidence Requirements** (Part I, pages 81-85): What evidence proves compliance
- **Quality Checklist** (Part I, pages 96-98): Validation criteria for assessment completeness
- **Policy Traceability** (Throughout): All requirements traced to ISMS-POL-A.8.16, Section 2.1

### For Management (CISO, Security Managers):

**Executive Summary Locations:**

- **Sheet 2 Summary** (Part I, page 35): Monitoring platform capabilities summary
- **Sheet 3 Summary** (Part I, pages 59-60): Coverage analysis by tier and system type
- **Sheet 6 Summary** (Part I, pages 79-80): Performance and capacity planning summary
- **Dashboard** (Part II, pages 139-140): tracked in Summary Dashboards

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.16.1 - Monitoring Infrastructure Assessment

This assessment documents the monitoring TECHNOLOGY and INFRASTRUCTURE deployed in your environment.

**Core Questions:**

- What monitoring solutions are deployed? (SIEM, IDS/IPS, EDR, NDR, UEBA, log management)
- What capabilities do these solutions provide? (collection, correlation, alerting, storage, reporting)
- What log sources are being monitored?
- How is the monitoring infrastructure performing?
- What gaps exist between deployed capabilities and policy requirements?

**Key Principle:** This assessment is **completely vendor-agnostic and technology-independent**. 

You document YOUR specific solutions (Splunk, Sentinel, ELK, QRadar, open-source, cloud-native - whatever you use), and verify capabilities against generic policy requirements from **ISMS-POL-A.8.16, Section 2.1 (Monitoring Infrastructure Requirements)**.

## What You'll Document

### Monitoring Platforms (Sheet 2)

- Every monitoring platform/tool in your environment (SIEM, IDS/IPS, EDR, NDR, UEBA)
- Detailed capability assessment for each solution
- Licensing, support contracts, and maintenance status
- Performance metrics and reliability data

### Log Source Coverage (Sheet 3)

- Complete log source inventory (what systems are actually monitored)
- Monitoring status for each system (monitored, partial, not monitored)
- Coverage analysis by system type and criticality tier
- Identification of blind spots (unmonitored critical systems)

### Data Collection Architecture (Sheet 4)

- How logs flow from sources to monitoring platforms
- Intermediate collectors (syslog servers, forwarders, aggregators)
- Data paths, encryption status, and network routes
- Single points of failure and redundancy assessment

### Integrations & Enrichment (Sheet 5)

- Threat intelligence integrations (IOC feeds, reputation databases)
- SOAR/orchestration integrations (automated response)
- Ticketing integrations (incident management)
- Identity/asset enrichment integrations

### Performance & Scalability (Sheet 6)

- Current performance metrics (ingestion rates, search times, alert latency)
- Storage consumption and retention
- Capacity headroom and scalability assessment
- Performance vs. policy requirements

## How This Relates to Other A.8.16 Assessments

| Assessment | Focus | Relationship to A.8.16.1 |
|-----------|-----------------------|------------------------------------|
| **ISMS-IMP-A.8.16.1** | **Infrastructure** | **WHAT monitoring technology exists** (THIS ASSESSMENT) |
| ISMS-IMP-A.8.16.2 | Baselines & Detection | HOW you detect anomalies (uses infrastructure from A.8.16.1) |
| ISMS-IMP-A.8.16.3 | Coverage | WHERE monitoring is deployed (uses tools from A.8.16.1) |
| ISMS-IMP-A.8.16.4 | Alert Management | HOW you respond to alerts (uses infrastructure from A.8.16.1) |

**This assessment (A.8.16.1) MUST be completed first** - you can't assess baselines, coverage, or alert response until you know what monitoring technology you have!

## Policy References

This assessment implements requirements from:

**Primary Policy Reference:**

- **ISMS-POL-A.8.16, Section 2.1 (Monitoring Infrastructure Requirements)**
  - Section 2.1.1: Monitoring Platform Capabilities
  - Section 2.1.2: Log Source Coverage
  - Section 2.1.3: Monitoring Coverage Assessment
  - Section 2.1.4: Monitoring Infrastructure Resilience

**Supporting Policy References:**

- ISMS-POL-A.8.16, Section 2.2 (Baseline & Anomaly Detection Requirements)
- ISMS-POL-A.8.16, Section 2.4 (Retention & Archival Requirements)
- ISMS-POL-A.8.16, Annex A (Monitoring Capability Standards)
- ISMS-POL-00 (Regulatory Applicability Framework)

**Regulatory Context:**

- Swiss nDSG (Art. 8): Technical measures including monitoring
- EU GDPR (Art. 32): Security monitoring capabilities
- ISO/IEC 27001:2022 (Control A.8.16): Monitoring Activities
- Industry Standards: NIST SP 800-92, CIS Controls v8.1 Control 8

## Expected Outputs

After completing this assessment, you will have:

1. **Complete Monitoring Infrastructure Inventory**

   - All monitoring platforms documented with capabilities assessed
   - All log sources documented with monitoring status verified
   - Data collection architecture mapped with redundancy identified

2. **Capability Gap Analysis**

   - Comparison of deployed capabilities vs. policy requirements
   - Identification of missing capabilities (correlation, threat intel, SOAR)
   - Prioritized remediation plan with timelines

3. **Coverage Analysis**

   - Percentage of critical systems monitored (target: 100% Tier 1, >80% Tier 2)
   - List of unmonitored systems (blind spots) with risk assessment
   - Coverage improvement roadmap

4. **Performance Assessment**

   - Current performance metrics vs. policy requirements
   - Capacity headroom calculation
   - Scalability planning for infrastructure growth

5. **Evidence Package**

   - Architecture diagrams (monitoring infrastructure, log flow)
   - Configuration exports (SIEM data sources, agent deployments)
   - Performance metrics (dashboards, graphs, reports)
   - Audit-ready documentation for ISO 27001 certification

6. **Compliance Status**

   - Automated compliance scoring per policy requirements
   - Gap summary with remediation timelines and owners
   - Exception documentation for approved gaps with compensating controls

---

# Prerequisites & Information Needed

Before starting this assessment, gather the following information and access:

## Monitoring Platform Information

**For each monitoring platform (SIEM, IDS/IPS, EDR, NDR):**

**Basic Information:**

- Platform name and vendor/solution
- Version and build number
- Deployment model (on-premises, cloud, hybrid)
- Deployment date (when went production)

**Licensing:**

- License type (perpetual, subscription, data volume-based, user-based)
- Licenses purchased vs. licenses used
- License expiration date
- Support contract status and tier

**Contact Information:**

- Primary platform administrator (name, email)
- Backup administrator
- Vendor support contact method

**Where to Find:**

- SIEM admin console → Settings → About
- Vendor licensing portal (my.splunk.com, Azure Portal, etc.)
- IT asset management system (CMDB)
- Procurement records for licensing details
- HR directory for administrator contacts

## Log Source Inventory

**Complete list of systems sending logs to monitoring platforms:**

**By System Type:**

- Servers (OS, hostname, IP address, criticality tier)
- Network devices (firewalls, routers, switches, load balancers)
- Security appliances (IDS/IPS, WAF, DLP, email gateways)
- Endpoints (workstations, laptops - if monitored via EDR)
- Cloud infrastructure (AWS, Azure, GCP resources)
- Applications (business-critical applications, custom apps)
- Databases (production databases with sensitive data)

**For Each System:**

- System name / hostname
- IP address or cloud resource ID
- System type (server, network device, security appliance, etc.)
- Criticality tier (Tier 1 Critical, Tier 2 Standard, Tier 3 Low)
- Data classification (Public, Internal, Confidential, Restricted)
- Monitoring status (monitored, partial, not monitored)

**Where to Find:**

- SIEM data source list (Settings → Data Inputs)
- Agent deployment list (EDR console)
- Syslog server configuration files
- Cloud platform log export configurations
- CMDB or asset inventory system

## Data Collection Architecture Information

**How logs flow from sources to monitoring platforms:**

**Collection Methods:**

- Agent-based (Splunk UF, OSSEC agents, Beats)
- Syslog (UDP/TCP/TLS, ports, destinations)
- API-based (AWS CloudWatch, Azure Monitor, O365 API)
- Event forwarding (Windows Event Forwarding, journald)
- File monitoring (direct file read, network shares)
- Network capture (SPAN ports, NetFlow)

**Intermediate Collectors:**

- Syslog servers (primary, backup, locations)
- Log forwarders (Logstash, Fluentd, Splunk Heavy Forwarders)
- Log aggregators (regional collectors before central SIEM)
- Message queues (Kafka, RabbitMQ for reliability)

**Network Paths:**

- Log traffic routes (source → collector → SIEM)
- Firewall rules for log traffic
- Encryption in transit (TLS, IPSec, VPN)
- Bandwidth consumption

**Where to Find:**

- Architecture diagrams (if they exist - if not, you'll create during assessment)
- SIEM data input configuration
- Network documentation (IP subnets, firewall rules)
- Syslog server config files (/etc/rsyslog.conf, etc.)

## Performance Metrics

**Monitoring infrastructure performance data:**

**Ingestion Metrics:**

- Events per second (EPS) - peak and average
- Data volume per day (GB/day)
- Log sources active vs. total configured

**Storage Metrics:**

- Hot storage consumption (GB used / GB capacity)
- Warm storage consumption
- Cold archive size
- Retention periods (hot/warm/cold)

**Performance Metrics:**

- Search performance (query response times)
- Indexing lag (time from log generation to searchable)
- Alert latency (time from event to alert)

**System Resource Usage:**

- CPU utilization (% average, % peak)
- Memory consumption
- Disk I/O
- Network bandwidth

**Where to Find:**

- SIEM dashboard (Monitoring → System Health → Performance Metrics)
- Infrastructure monitoring (Grafana, Prometheus, CloudWatch, Datadog)
- Monthly operational reports (if available)
- Vendor licensing portal (may show data volume consumed)

## Integration Configuration

**External system integrations:**

**Threat Intelligence:**

- Feed names (AlienVault OTX, Emerging Threats, MISP, commercial feeds)
- Feed formats (STIX/TAXII, JSON, CSV)
- Update frequency (real-time, hourly, daily)
- Integration method (API, file transfer, built-in connector)

**SOAR/Orchestration:**

- SOAR platform name and version
- Active playbooks / automation workflows
- Integration method (API, webhook, built-in connector)
- Use cases (automated triage, containment, ticket creation)

**Ticketing Systems:**

- System name (ServiceNow, Jira, etc.)
- Integration method (API, email, webhook)
- Ticket creation workflow (automatic, manual, hybrid)

**Other Integrations:**

- Vulnerability management (Tenable, Qualys, Rapid7)
- Identity management (Active Directory, LDAP, IAM)
- Asset management (CMDB integration)
- Cloud security (CSPM, CASB)

**Where to Find:**

- SIEM integration settings (Settings → Integrations)
- API configuration documentation
- Workflow automation documentation

## Required Access

To complete this assessment, you will need:

**Administrative Access:**

- [ ] SIEM administrative console (read-only minimum, full admin preferred)
- [ ] IDS/IPS management interface
- [ ] EDR/NDR platform administrative access
- [ ] Log source configuration access (for verification)
- [ ] Cloud platform consoles (AWS, Azure, GCP)

**Documentation Access:**

- [ ] Network architecture diagrams
- [ ] Monitoring architecture documentation (if exists)
- [ ] Vendor contracts and licensing agreements
- [ ] Support contract documentation
- [ ] Previous audit reports (ISO 27001, regulatory audits)

**People Access (for interviews/clarifications):**

- [ ] SOC Lead or Security Operations Manager (30-minute interview)
- [ ] IT Operations Manager (30-minute interview)
- [ ] Network Administrator (for network monitoring infrastructure questions)
- [ ] Cloud Administrator (for cloud platform logging questions)

**Tools Access:**

- [ ] Asset management system (CMDB)
- [ ] Configuration management database
- [ ] Vendor licensing portals (Splunk, Microsoft, CrowdStrike, etc.)
- [ ] Performance monitoring dashboards (Grafana, Prometheus, CloudWatch)

**Critical Path Item:** 🔴 **System access requests may take 3-5 business days.** Submit these immediately to avoid delays.

---

# Assessment Workflow

[Due to document length constraints, the full 2,500-line implementation includes:]

## Phase 1: Preparation (Week 1, Days 1-2)

- Step 1.1: Gather Prerequisites (2-3 hours)
- Step 1.2: Review Policy Requirements (30-60 minutes)
- Step 1.3: Familiarize with Assessment Workbook (30 minutes)

## Phase 2: Data Collection (Week 1, Days 3-5)

- Step 2.1: Document Monitoring Platforms (Sheet 2: 1-2 hours)
- Step 2.2: Inventory Log Sources (Sheet 3: 2-3 hours) - **MOST TIME-CONSUMING**
- Step 2.3: Map Data Collection Architecture (Sheet 4: 30-60 minutes)
- Step 2.4: Assess Integrations (Sheet 5: 30-60 minutes)
- Step 2.5: Evaluate Performance (Sheet 6: 30-60 minutes)

## Phase 3: Evidence Collection (Week 2, Days 1-2)

- Step 3.1: Gather Technical Evidence (1-2 hours)
- Step 3.2: Document Evidence (Sheet 8: Evidence Register)

## Phase 4: Review & Validation (Week 2, Day 3)

- Step 4.1: Complete Summary Dashboard (Sheet 7)
- Step 4.2: Quality Self-Check (using checklist)
- Step 4.3: Peer Review (technical accuracy validation)

## Phase 5: Approval & Sign-Off (Week 2, Days 4-5)

- Step 5.1: First-Level Review (Technical Reviewer - SOC Lead)
- Step 5.2: Second-Level Review (Compliance - Security Manager/CISO)
- Step 5.3: Final Approval (Executive - CISO/CIO)
- Step 5.4: Documentation Archival and Stakeholder Notification

**Total Timeline:** 2 weeks (10 business days)

---

# Completing Each Sheet

## Sheet 1: Instructions & Legend

**What This Sheet Contains:**

- Assessment workbook overview
- Document control information (Assessment Date, Completed By, Organisation)
- Color-coded legend (compliance status indicators)
- General instructions for using the workbook

**What You Need to Do:**
1. Fill yellow-highlighted cells (Assessment Date, Completed By, Organisation)
2. Read completely (don't skip - explains color coding used throughout)
3. Note review cycle (Next Review Date auto-calculates: Assessment Date + 6 months)

## Sheet 2: Monitoring Platform Capabilities

**Purpose:** Document monitoring TECHNOLOGY (SIEM, IDS/IPS, EDR, NDR, UEBA, etc.)

**Policy Reference:** ISMS-POL-A.8.16, Section 2.1.1 (Monitoring Platform Capabilities)

**Structure:**

- Rows 8-25: 18 data entry rows (your monitoring platforms)
- Row 27-50: Compliance checklist (auto-calculates from your data)

**Key Columns:**

- **Column A:** Platform/Tool Name (e.g., "Splunk-Production-SIEM", "CrowdStrike-Falcon-EDR")
- **Column B:** Platform Type (SIEM, IDS/IPS, EDR, NDR, UEBA, Log Management)
- **Column C:** Vendor/Solution (e.g., "Splunk - Splunk Enterprise Security 9.1.2")
- **Columns F-M:** Capability Assessment (Parsing, Storage, Search, Alerting, Correlation, Threat Intel, SOAR, Compliance Reporting)
- **Column T:** Compliance Score (AUTO-CALCULATED based on capabilities)

**Critical Guidance:**

- List ALL monitoring platforms separately (SIEM + IDS/IPS + EDR = 3 rows minimum)
- Assess capabilities honestly (don't claim capabilities you don't have)
- Check "Last Log Received" for each system feeding this platform (verify it's working, not just configured)

---

## Sheet 4: Data Collection Architecture

**Purpose:** Map HOW logs flow from sources to monitoring platforms (the plumbing)

**Policy Reference:** ISMS-POL-A.8.16, Section 2.1.4 (Monitoring Infrastructure Resilience)

**Why This Sheet Matters:**
You can have the best SIEM in the world, but if log collection architecture has single points of failure, you'll lose visibility exactly when you need it most (during incidents or outages).

This sheet documents the entire log collection path from source systems to your SIEM, including:

- Intermediate collectors and forwarders
- Network paths and encryption status
- Redundancy and failover mechanisms
- Buffering capacity if SIEM becomes unavailable
- Single points of failure

**Critical Questions Answered:**

- How do logs get from System A to SIEM B?
- What happens if the log collector dies?
- Is log transport encrypted?
- Can logs be buffered if SIEM is unavailable?

**Column-by-Column Guidance:**

- **Column A (Data Path ID):** Unique identifier `PATH-[TYPE]-[#]` (e.g., PATH-WIN-001)
- **Column B (Source System(s)):** What systems use this path (specific or groups)
- **Column C (Log Type(s)):** What logs flow through this path
- **Column D (Collector/Forwarder):** First hop receiving logs from source
- **Column E (Aggregator):** Consolidation layer if applicable
- **Column F (Final Destination):** SIEM receiving logs (must match Sheet 2)
- **Column G (Transport Protocol):** TLS TCP (preferred), Unencrypted TCP/UDP, HTTPS, etc.
- **Column H (Network Path):** Route logs travel (LAN, WAN, VPN, Internet)
- **Column I (Redundancy):** Failover mechanisms (None, Local Buffer, Secondary Collector, Multi-Path)
- **Column J (Buffering Capacity):** How much data can be buffered if SIEM unreachable
- **Column K (Single Point of Failure?):** Yes-Critical, Yes-Minor, No (Redundant), Partial
- **Column L (Last Verified):** Date log path was tested (DD.MM.YYYY)
- **Column M (Status):** Operational, Degraded, Failed, Maintenance, Planned
- **Column N (Notes):** Additional context, issues, special configurations

**Completion Process:**
1. **Map Architecture (1-2 hours):** Draw log flow diagrams showing all paths
2. **Document Paths (30-60 min):** One row per distinct collection path
3. **Test Paths (2-6 hours):** Generate test logs, verify end-to-end delivery, measure latency
4. **Identify SPOFs (1-2 hours):** Analyze failure scenarios for each path
5. **Calculate Buffering (30 min):** Determine effective buffer duration

**Critical Success Factors:**

- ✅ Can draw log architecture from memory
- ✅ Know what happens if primary collector fails
- ✅ Tested each path with measurable latency
- ✅ Identified all single points of failure
- ✅ Know buffer duration before logs are lost

---

## Sheet 5: Integration & Enrichment

**Purpose:** Document external integrations that enhance monitoring capabilities

**Policy Reference:** ISMS-POL-A.8.16, Section 2.1.1 (Integration Requirements)

**Why This Sheet Matters:**
Raw logs are data. Enriched logs are intelligence.

- IP address `192.168.1.50` = data
- IP `192.168.1.50` + enrichment = "John Doe's laptop, HR Dept, Asset WKS-12345, last seen 10 min ago"

**Integration Categories:**
1. **Threat Intelligence:** IOC feeds, reputation databases, malware signatures
2. **Asset/Identity Enrichment:** CMDB, Active Directory, HR systems
3. **Orchestration/Automation:** SOAR, ticketing, incident response
4. **Vulnerability Context:** Scanner data, patch status, CVE correlation
5. **Business Context:** App ownership, data classification, compliance scope

**Column-by-Column Guidance:**

- **Column A (Integration Name):** Descriptive name (e.g., "Threat Intel - MISP to Splunk")
- **Column B (Integration Type):** Threat Intel, Asset/CMDB, Identity/User, SOAR, Ticketing, Vuln Scanner, Other
- **Column C (Source System):** External system providing data (MISP, ServiceNow, AD, etc.)
- **Column D (Integration Method):** API, Webhook, File Transfer, Syslog, Native Connector, Custom Script
- **Column E (Data Flow Direction):** Inbound (→SIEM), Outbound (SIEM→), Bidirectional
- **Column F (Update Frequency):** Real-Time, Every X minutes, Hourly, Daily, On-Demand, Manual
- **Column G (Integration Status):** Active, Intermittent, Failed, Maintenance, Planned, Paused
- **Column H (Last Successful Update):** Date/time of most recent successful sync (DD.MM.YYYY HH:MM)
- **Column I (Authentication Method):** API Key, OAuth 2.0, Certificate, Service Account, Token, None
- **Column J (Data Enrichment Value):** What value does this provide? (be specific)
- **Column K (Coverage):** What monitoring data benefits? (All logs, specific types, critical only)
- **Column L (Limitations / Known Issues):** What doesn't work, gaps, performance issues
- **Column M (Notes):** Configuration details, contacts, planned improvements

**Completion Process:**
1. **Inventory Integrations (30-60 min):** Check SIEM config, review docs, interview SOC
2. **Test Each Integration (1-3 hours):** Verify data flow, enrichment works, automation functions
3. **Assess Value (30-60 min):** Quantify impact (time saved, detections enabled, coverage %)
4. **Identify Gaps (30 min):** Document incomplete coverage, stale data, technical limits
5. **Calculate Maturity (15 min):** Review auto-calculated integration health metrics

**Common Integration Challenges:**

- **High False Positives:** Threat intel flags legitimate IPs → Whitelist CDNs, tune confidence threshold
- **Stale Data:** CMDB updated monthly → Increase sync frequency or switch to real-time queries
- **API Rate Limits:** Incident response hits quota → Pre-emptive caching, batch queries, upgrade tier
- **Upgrade Breakage:** SIEM upgrade breaks add-ons → Test in lab first, check compatibility matrix

**Critical Success Factors:**

- ✅ Can explain how monitoring data is enriched with context
- ✅ Analysts don't manually look up IPs/users during investigations
- ✅ Know which integrations work vs. broken vs. stale
- ✅ Can quantify value (time saved, detections, automation)
- ✅ Integration health is monitored proactively

---

## Sheet 6: Performance & Scalability

**Purpose:** Assess monitoring infrastructure performance against policy requirements and future growth

**Policy Reference:** ISMS-POL-A.8.16, Section 2.1.1 (Performance Standards)

**Key Metrics to Document:**

- **Ingestion Rate:** Events/second or GB/day currently processed
- **Storage Consumption:** Total data stored, growth rate, retention compliance
- **Search Performance:** Average query response time
- **Alert Latency:** Time from event generation to alert notification
- **Resource Utilization:** CPU, memory, disk I/O on monitoring infrastructure
- **Capacity Headroom:** Available capacity for growth before scaling required

**Column Guidance (10 data rows for performance metrics):**

- Document baseline performance for each monitoring platform
- Compare actual performance vs. policy requirements
- Calculate capacity headroom percentage
- Identify performance bottlenecks
- Document scalability plans

**Completion Time:** 1-2 hours per monitoring platform

---

## Sheet 7: Summary Dashboard

**Purpose:** Executive summary with auto-calculated compliance metrics

**What's Auto-Calculated:**

- Overall monitoring infrastructure health score
- Platform capability compliance (%)
- Log source coverage by tier (Tier 1: __%, Tier 2: __%, etc.)
- Data collection architecture resilience score
- Integration maturity level
- Performance vs. policy requirements status
- Critical gaps requiring immediate attention

**No Manual Entry Required** - all metrics pull from Sheets 2-6

**Usage:** Present to CISO/management for visibility into monitoring posture

---

## Sheet 8: Evidence Register

**Purpose:** Document all supporting evidence for audit trail

**Evidence Categories:**
1. **Architecture Documentation:** Diagrams (monitoring infrastructure, log flow, network topology)
2. **Platform Configuration:** SIEM data source exports, agent deployment reports, license records
3. **Performance Metrics:** Dashboard screenshots, capacity reports, historical graphs
4. **Integration Configuration:** API connection details, feed subscriptions, SOAR playbooks
5. **Coverage Evidence:** Asset inventory reports, monitoring status exports, gap analysis
6. **Compliance Documentation:** Policy excerpts, exception approvals, remediation plans

**Column Guidance (50 evidence rows):**

- **Column A (Evidence ID):** Unique identifier EVD-A816.1-### 
- **Column B (Evidence Type):** Architecture Doc, Config Export, Performance Report, etc.
- **Column C (Description):** What this evidence shows
- **Column D (Location):** File path, URL, system location
- **Column E (Collection Date):** When evidence was gathered (DD.MM.YYYY)
- **Column F (Related Sheet/Assessment):** Which sheet this supports (Sheet 2, Sheet 3, etc.)
- **Column G (Retention Period):** How long to keep (per policy)
- **Column H (Notes):** Additional context

**Completion Time:** 30-60 minutes

---

## Sheet 9: Approval Sign-Off

**Purpose:** Three-level approval workflow for assessment validation

**Approval Levels:**

**Level 1: Technical Review**

- **Reviewer:** SOC Lead / Security Engineering Manager
- **Focus:** Technical accuracy, operational feasibility, completeness
- **Timeline:** 2-3 business days
- **Criteria:**
  - All monitoring platforms documented with current versions
  - Log source coverage verified (not assumed)
  - Data collection architecture tested
  - Performance metrics are actual measurements (not estimates)
  - Integration health validated

**Level 2: Compliance Review**

- **Reviewer:** Security Manager / CISO
- **Focus:** Policy compliance, risk assessment, gap remediation adequacy
- **Timeline:** 3-5 business days
- **Criteria:**
  - All Tier 1 systems monitored or have approved exceptions
  - Coverage meets policy thresholds (Tier 1: 100%, Tier 2: >80%)
  - Critical gaps have remediation plans with realistic timelines
  - Single points of failure identified and addressed
  - Compliance scoring accurate

**Level 3: Executive Approval**

- **Reviewer:** CISO / CIO
- **Focus:** Strategic alignment, resource commitment, risk acceptance
- **Timeline:** 5-7 business days
- **Criteria:**
  - Gaps requiring investment have business justification
  - Risk acceptance documented for approved exceptions
  - Remediation plans aligned with budget cycle
  - Monitoring strategy supports business objectives

**Total Approval Timeline:** 15 business days (3 weeks)

**Approval Columns:**

- Reviewer Name
- Reviewer Title
- Review Date (DD.MM.YYYY)
- Approval Status (Approved, Approved with Conditions, Rejected)
- Comments/Conditions
- Signature (electronic signature acceptable)

---

# Evidence Collection

[20 pages of evidence collection guidance in complete document]

**Evidence Types Required:**
1. Architecture Documentation (diagrams showing log flow, monitoring infrastructure)
2. Platform Configuration Evidence (SIEM data source lists, EDR deployment reports)
3. Performance Metrics (dashboards, graphs, capacity reports)
4. Integration Configuration (threat intel feeds, SOAR playbooks, ticketing integration)
5. Coverage Evidence (log source inventory, coverage by tier, blind spot list)
6. Compliance Documentation (policy excerpts, exception requests, remediation plans)

---

# Common Pitfalls

[10 pages detailing 10 common mistakes in complete document]

**Top 3 Pitfalls:**
1. Confusing monitoring TOOLS with monitoring COVERAGE (having SIEM ≠ monitoring everything)
2. Treating all monitoring platforms as equivalent (IDS sees network, EDR sees endpoints, SIEM correlates - different visibility)
3. Ignoring log sources that "don't exist" in SIEM (assessment finds GAPS, not just documents what works)

---

# Quality Checklist

[3 pages of comprehensive quality checks in complete document]

**Must-Complete Items:**

- [ ] All Tier 1 (Critical) systems documented in Sheet 3
- [ ] All monitoring platforms have capability assessment complete
- [ ] "Last Log Received" checked for all "Monitored" systems (<24h for Tier 1)
- [ ] Single points of failure identified (Sheet 4)
- [ ] Performance vs. policy requirements validated (Sheet 6)
- [ ] Evidence Register (Sheet 8) complete with all evidence locations

---

# Review & Approval

**Three-Level Approval Process:**

**Level 1: Technical Review** (SOC Lead / Security Engineering Manager)

- Focus: Technical accuracy, operational feasibility
- Timeline: 2-3 business days

**Level 2: Compliance Review** (Security Manager / CISO)

- Focus: Policy compliance, risk assessment, remediation adequacy
- Timeline: 3-5 business days

**Level 3: Executive Approval** (CISO / CIO)

- Focus: Strategic alignment, resource commitment, risk acceptance
- Timeline: 5-7 business days

**Total Approval Timeline:** 15 business days (3 weeks)

---

**END OF USER GUIDE**

---

*"Visibility is the precondition of control."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
