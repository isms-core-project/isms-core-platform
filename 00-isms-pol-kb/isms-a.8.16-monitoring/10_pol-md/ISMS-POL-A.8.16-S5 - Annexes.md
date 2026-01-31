# ISMS-POL-A.8.16-S5
## Monitoring Activities - Annexes

**Document ID**: ISMS-POL-A.8.16-S5
**Title**: Monitoring Activities - Annexes (Overview)  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]  | SOC Lead / Information Security Manager | Initial annex framework |

**Review Cycle**: Annual (individual annexes may have different cycles)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Operational Review: Security Operations Center (SOC) Lead
- Technical Review: Security Engineering Manager

**Distribution**: SOC, security team, IT operations (specific annexes distributed as needed)  
**Related Documents**: ISMS-POL-A.8.16-S5.A through S5.D (individual annexes)

---

## 5.1 Purpose and Scope

This section provides **supporting annexes** to the Monitoring Activities policy framework - practical tools, templates, and reference materials to facilitate policy implementation, SOC operations, and compliance.

**Annexes are operational documents** designed for day-to-day use by:
- SOC analysts triaging and investigating alerts
- Security engineers implementing monitoring infrastructure
- System owners establishing baselines
- Security team developing detection rules
- Management reviewing compliance and effectiveness
- Auditors verifying control implementation

**Key Principle**: Annexes translate policy requirements (S1-S4) into **actionable guidance** for security operations.

---

## 5.2 Annex Structure

The Monitoring Activities policy framework includes the following annexes:

### 5.2.1 Annex A: Monitoring Capability Standards

**Document**: ISMS-POL-A.8.16-S5.A  
**Purpose**: Define technical capability requirements for monitoring solutions (SIEM, IDS/IPS, EDR, etc.)

**Content**:
- Mandatory capabilities (MUST have)
- Recommended capabilities (SHOULD have)
- Optional capabilities (MAY have)
- Performance and scalability requirements
- Integration requirements (threat intel, SOAR, ticketing)
- Evaluation criteria for technology selection
- Capability maturity model

**Audience**: Security Engineering, Procurement, IT Management, Vendors

**Use Case**: Technology evaluation and selection, vendor RFP development, solution validation, architecture design

---

### 5.2.2 Annex B: Baseline Definition Template

**Document**: ISMS-POL-A.8.16-S5.B  
**Purpose**: Standardize baseline establishment process (implements S2.2)

**Content**:
- Baseline documentation template
- Baseline establishment methodology (step-by-step)
- Statistical metrics to collect (mean, median, std dev, percentiles)
- Time-aware baseline guidance (business hours, off-hours, weekends)
- Baseline review and update procedures
- Threshold derivation methodology
- Example baselines for common system types

**Audience**: SOC Analysts (Tier 2/3), Security Engineering, System Owners

**Use Case**: Establishing new baselines, reviewing existing baselines, documenting normal behavior, deriving alert thresholds

---

### 5.2.3 Annex C: Alert Response Procedures

**Document**: ISMS-POL-A.8.16-S5.C  
**Purpose**: Define SOC operational procedures for alert handling (implements S2.3)

**Content**:
- Alert triage procedures (step-by-step)
- Investigation playbooks by alert type
- Escalation procedures and criteria
- Evidence collection guidance
- Communication templates
- Severity classification decision trees
- Common false positive scenarios
- Tool-specific investigation guides

**Audience**: SOC Analysts (Tier 1, 2, 3), Incident Response Team, Security Operations

**Use Case**: Daily SOC operations, alert triage, incident investigation, new analyst training, shift handovers

---

### 5.2.4 Annex D: Quick Reference Guide

**Document**: ISMS-POL-A.8.16-S5.D  
**Purpose**: Provide at-a-glance reference for common scenarios and decisions

**Content**:
- Policy summary (key requirements)
- Severity classification quick reference
- SLA timeframes by severity
- Escalation paths (who to contact)
- Common alert types and responses
- Baseline establishment quick guide
- Responsibility quick reference (who does what)
- FAQ (Frequently Asked Questions)
- Contact information

**Audience**: All Personnel (especially SOC, System Owners, Security Team)

**Use Case**: Quick policy lookups, SOC desk reference, training reference, new hire onboarding

---

## 5.3 Annex Maintenance

### 5.3.1 Update Frequency

Annexes are **living documents** that may be updated more frequently than core policy sections (S1-S4):

**Annex A (Capability Standards)**: Updated when monitoring technology evolves (annually or as needed)  
**Annex B (Baseline Template)**: Updated when baseline methodology improves (semi-annually or as needed)  
**Annex C (Alert Response)**: Updated after incidents, process improvements, or new alert types (quarterly or as needed)  
**Annex D (Quick Reference)**: Updated when policies change or FAQs evolve (as needed)

### 5.3.2 Approval Authority

Annex updates require **lighter approval** than core policy sections:

- **Minor updates** (clarifications, playbook additions, FAQ updates): SOC Lead approval
- **Substantive updates** (new requirements, process changes, capability changes): CISO approval
- **Integration with core policy changes**: Follow core policy approval process (S4)

### 5.3.3 Version Control

Each annex is **independently versioned**:
- Changes to Annex C (procedures) do not trigger version changes in Annex A (capabilities)
- Annex version history tracked in each document
- Cross-references updated when related documents change
- Major updates communicated to all SOC shifts

---

## 5.4 Relationship to Core Policy

Annexes **support and implement** core policy requirements:

| Core Policy Section | Supporting Annex(es) | Relationship |
|---------------------|---------------------|--------------|
| S2.1 (Infrastructure) | Annex A | Capability standards for monitoring platforms |
| S2.2 (Baseline & Detection) | Annex B, Annex C | Baseline template + detection procedures |
| S2.3 (Alert Management) | Annex C, Annex D | Response procedures + quick reference |
| S2.4 (Retention) | Annex A | Storage capability requirements |
| S3 (Roles & Responsibilities) | Annex C, Annex D | Operational procedures + quick reference |
| S4 (Policy Governance) | All Annexes | Annexes support policy implementation |

**Hierarchy**: Core policy (S1-S4) sets **requirements**. Annexes provide **implementation guidance** and **operational procedures**.

**Conflict Resolution**: If conflict between core policy and annex, **core policy takes precedence**. Conflicts indicate annex needs updating.

---

## 5.5 Using the Annexes

### 5.5.1 For SOC Analysts

**Annex B**: Use when establishing or reviewing baselines  
**Annex C**: Use daily for alert triage and investigation (keep handy!)  
**Annex D**: Use for quick policy lookups during shift

### 5.5.2 For Security Engineering

**Annex A**: Use when evaluating, procuring, or deploying monitoring solutions  
**Annex B**: Use when helping system owners establish baselines  
**Annex C**: Use when creating investigation playbooks

### 5.5.3 For System Owners

**Annex B**: Use when collaborating with SOC on baseline establishment  
**Annex D**: Use for understanding monitoring responsibilities

### 5.5.4 For Incident Response

**Annex C**: Use during incident investigation (escalation procedures, evidence collection)  
**Annex D**: Use for escalation paths and contact information

### 5.5.5 For Management

**Annex A**: Use when making technology investment decisions  
**Annex D**: Use for high-level policy understanding and metrics overview

### 5.5.6 For Auditors

**All Annexes**: Demonstrate operational implementation of policy requirements  
**Annex B**: Verify baseline documentation exists  
**Annex C**: Verify operational procedures are documented and followed

---

## 5.6 Customization and Localization

Organizations **MAY** customize annexes to fit specific needs:

**Encouraged Customizations**:
- Add organization-specific playbooks to Annex C (custom alert types)
- Customize baseline template in Annex B for specific system types
- Add additional FAQs to Annex D based on SOC questions
- Add tool-specific investigation guides to Annex C (e.g., "How to investigate in Splunk")
- Translate annexes to local languages (while maintaining English master version)

**Discouraged Customizations**:
- Reducing capability requirements in Annex A (weakens monitoring)
- Oversimplifying triage procedures in Annex C (reduces investigation quality)
- Removing baseline statistical requirements from Annex B (creates cargo cult baselines)

**Change Control**: All customizations must be documented and approved per Section 5.3.

---

## 5.7 Training and Awareness

Annexes support training programs:

**New SOC Analyst Onboarding**:
- Annex C (Alert Response) is core training material
- Annex D (Quick Reference) provided as desk reference
- Practice investigations using Annex C playbooks

**Role-Specific Training**:
- **SOC Analysts**: Deep dive on Annexes C, D (operational focus)
- **Security Engineering**: Focus on Annexes A, B (infrastructure and baseline focus)
- **System Owners**: Focus on Annex B (baseline establishment)
- **Incident Response**: Focus on Annex C (escalation and investigation)

**Ongoing Awareness**:
- Annex C updates communicated during shift handovers
- Quarterly SOC training sessions review updated playbooks
- Annual refresher on baseline methodology (Annex B)

---

## 5.8 Accessibility and Distribution

### 5.8.1 Publication

Annexes **SHALL** be published alongside core policy documents:

- Same repository (ISMS document management system)
- SOC internal wiki (for quick operational access)
- Linked from core policy sections for easy navigation
- Searchable and indexed

### 5.8.2 Formats

Annexes **SHOULD** be available in multiple formats:

- **PDF**: Official version for reference and printing
- **Markdown/DOCX**: Editable version for customization
- **HTML**: Web-based access via SOC wiki
- **Quick Reference Card** (Annex D): Laminated SOC desk card, poster, digital wallpaper
- **Annex C Playbooks**: Integrated into ticketing/SOAR systems for automated workflows

### 5.8.3 Access

**Public** (within organization):
- Annex D (Quick Reference) - all personnel
- Annex B (Baseline Template) - all technical personnel

**Restricted** (role-based):
- Annex A (Capability Standards) - Security, IT Management, Procurement
- Annex C (Alert Response) - SOC, Security Team, Incident Response (contains sensitive investigation techniques)

---

## 5.9 Continuous Improvement

Annexes evolve based on:

**Operational Feedback**:
- SOC analysts report unclear procedures → Update Annex C
- False positive patterns emerge → Update Annex C with new scenarios
- Baseline methodology proves inadequate → Update Annex B
- Frequent questions from system owners → Add to Annex D FAQ

**Technology Changes**:
- New SIEM capabilities available → Update Annex A
- New detection techniques discovered → Update Annex C
- New monitoring tools deployed → Update Annex A, C

**Incident Lessons Learned**:
- Investigation gaps identified → Add playbooks to Annex C
- Detection failures → Update Annex B (baseline methodology)
- Response delays → Streamline procedures in Annex C

**Metrics Analysis**:
- High false positive rates → Refine triage procedures in Annex C
- Slow investigation times → Add quick investigation shortcuts to Annex C
- Baseline staleness → Simplify Annex B process

---

## 5.10 Annex Documents

The following annexes are part of this policy framework:

- **ISMS-POL-A.8.16-S5.A** - Monitoring Capability Standards
- **ISMS-POL-A.8.16-S5.B** - Baseline Definition Template
- **ISMS-POL-A.8.16-S5.C** - Alert Response Procedures
- **ISMS-POL-A.8.16-S5.D** - Quick Reference Guide

Each annex is a standalone document, independently versioned and maintained.

---

## 5.11 INSTRUCTIONS FOR CREATING ANNEXES (Next Session)

**⚠️ IMPORTANT: The following annexes need to be created in the next session. Below are detailed specifications for each.**

---

### 5.11.1 Annex A: Monitoring Capability Standards

**Target Length**: ~350 lines  
**Structure**:

1. **Introduction** (~30 lines)
   - Purpose: Define what monitoring solutions MUST/SHOULD/MAY provide
   - Scope: All monitoring technologies (SIEM, IDS/IPS, EDR, NDR, UEBA, etc.)

2. **Core Capabilities** (~100 lines)
   - **Log Collection** (MUST): Syslog, Windows Event Logs, JSON, APIs, agents, agentless
   - **Log Parsing** (MUST): Common formats, custom parsers, field extraction, normalization
   - **Storage & Indexing** (MUST): Compressed storage, indexed search, hot/warm/cold tiers
   - **Search & Analysis** (MUST): Full-text search, field-based filtering, aggregation, time-series
   - **Alerting** (MUST): Real-time alerts, thresholds, correlation, suppression, enrichment
   - **Visualization** (MUST): Dashboards, charts, drill-down, customizable views

3. **Detection Capabilities** (~80 lines)
   - **Correlation Engine** (MUST): Multi-event correlation, time-windows, field-based correlation
   - **Threat Intelligence Integration** (MUST): IOC matching, STIX/TAXII support, custom feeds
   - **Baseline Support** (SHOULD): Statistical baselining, anomaly detection, UEBA
   - **Rule Management** (MUST): Version control, testing, tuning, retirement

4. **Integration Capabilities** (~60 lines)
   - **Threat Intelligence** (MUST): Automated feed ingestion, IOC enrichment
   - **Incident Response** (MUST): Ticketing integration, SOAR, case management
   - **Asset Management** (SHOULD): CMDB integration, asset context enrichment
   - **Identity Management** (SHOULD): AD/LDAP integration, user context

5. **Performance & Scalability** (~40 lines)
   - **Ingestion Rate** (MUST): Support expected EPS (events per second)
   - **Search Performance** (MUST): <10 sec for typical queries on hot storage
   - **Alert Latency** (MUST): <2 min for critical alerts
   - **Scalability** (MUST): Horizontal scaling capability

6. **Operational Requirements** (~40 lines)
   - **High Availability** (SHOULD): 99.5% uptime, redundancy, failover
   - **Disaster Recovery** (MUST): Backup, RTO <24h, RPO <24h
   - **Security** (MUST): RBAC, MFA, encrypted transmission, audit logging

**Style**: Use SHALL/SHOULD/MAY consistently. Provide rationale for each requirement. Include examples.

**Reference**: Similar to ISMS-POL-A.8.23-S5.A but for monitoring tools instead of web filtering.

---

### 5.11.2 Annex B: Baseline Definition Template

**Target Length**: ~250 lines  
**Structure**:

1. **Introduction** (~20 lines)
   - Purpose: Provide step-by-step baseline establishment methodology
   - When to use: New system monitoring, baseline review, threshold derivation

2. **Baseline Establishment Steps** (~100 lines)
   - **Step 1: Identify System** (name, type, criticality, owner, business function)
   - **Step 2: Define Metrics** (what to measure - authentication, network, resource usage)
   - **Step 3: Collect Data** (observation period, 30-90 days, exclude anomalies)
   - **Step 4: Calculate Statistics** (mean, median, std dev, min/max, 95th percentile)
   - **Step 5: Create Time-Aware Baselines** (business hours, off-hours, weekends)
   - **Step 6: Document Baseline** (using template below)
   - **Step 7: Derive Thresholds** (baseline × multiplier based on risk)
   - **Step 8: Approve Baseline** (system owner, SOC lead)

3. **Baseline Documentation Template** (~80 lines)
```
   System: [Name]
   Type: [Server/Workstation/Network Device]
   Owner: [Name/Team]
   Criticality: [Critical/High/Medium/Low]
   
   Metric: [Specific metric, e.g., "Successful Login Events"]
   Observation Period: [DD.MM.YYYY - DD.MM.YYYY]
   Exclusions: [Incidents, maintenance windows excluded]
   
   Business Hours Baseline (Mon-Fri 08:00-18:00):
   - Mean: X events/hour
   - Median: X events/hour
   - Std Dev: X events/hour
   - 95th Percentile: X events/hour
   - Min/Max: X-X events/hour
   
   Off-Hours Baseline (Mon-Fri 18:00-08:00):
   - Mean: X events/hour
   - Median: X events/hour
   - 95th Percentile: X events/hour
   
   Weekend Baseline (Sat-Sun):
   - Mean: X events/hour
   - 95th Percentile: X events/hour
   
   Alert Threshold: X events/hour (95th %ile × 1.2 multiplier)
   Warning Threshold: X events/hour (optional)
   
   Established By: [Name]
   Established Date: DD.MM.YYYY
   Approved By: [SOC Lead]
   Next Review Date: DD.MM.YYYY (quarterly for critical systems)
```

4. **Example Baselines** (~50 lines)
   - Domain Controller authentication baseline (example)
   - Database server query baseline (example)
   - Firewall connection baseline (example)

**Style**: Step-by-step instructions. Concrete examples. Emphasize measurability.

**Reference**: Implements ISMS-POL-A.8.16-S2.2 (Baseline & Anomaly Detection Requirements).

---

### 5.11.3 Annex C: Alert Response Procedures

**Target Length**: ~350 lines  
**Structure**:

1. **Introduction** (~20 lines)
   - Purpose: SOC operational procedures for alert handling
   - Scope: All alert types, all severity levels
   - When to use: Every alert received

2. **Alert Triage Procedure** (~60 lines)
   - **Step 1: Acknowledge Alert** (claim ownership, update status)
   - **Step 2: Read Alert** (understand what triggered, review enrichment)
   - **Step 3: Gather Context** (user info, asset info, recent activity)
   - **Step 4: Determine Disposition**:
     - True Positive → Escalate to investigation
     - False Positive → Document and close
     - Benign True Positive → Document and close
     - Requires Investigation → Proceed to investigation
   - **Step 5: Document Triage** (findings, rationale, disposition)
   - **Triage Timeframes**: Critical <15min, High <1hr, Medium <4hr, Low <1day

3. **Investigation Playbooks by Alert Type** (~150 lines)
   
   **Playbook: Brute Force Authentication** (~30 lines)
   - Symptoms: Failed logins > threshold
   - Investigation steps: Check source IP, check user account, check if successful login followed, check geographic patterns
   - Evidence to collect: Authentication logs, network connection logs
   - Escalation criteria: If successful login occurred OR source is known attack infrastructure
   
   **Playbook: Lateral Movement** (~30 lines)
   - Symptoms: Admin login to multiple systems in short time
   - Investigation steps: Check user normal behavior, check systems accessed, check process execution
   - Evidence to collect: RDP/SSH logs, process execution logs, network connections
   - Escalation criteria: If user should not have admin access OR systems unrelated to user role
   
   **Playbook: Data Exfiltration** (~30 lines)
   - Symptoms: Large data transfer to external destination
   - Investigation steps: Check destination IP/domain, check data type, check user authorization, check business justification
   - Evidence to collect: Network flow logs, file access logs, email logs
   - Escalation criteria: If destination unknown OR data is sensitive
   
   **Playbook: Malware Detection** (~30 lines)
   - Symptoms: EDR/AV alert for malware
   - Investigation steps: Check malware type, check affected system criticality, check if contained, check for lateral movement
   - Evidence to collect: Malware sample, process logs, network connections
   - Escalation criteria: ALWAYS escalate malware detections
   
   **Playbook: Baseline Deviation** (~30 lines)
   - Symptoms: Metric exceeds baseline threshold
   - Investigation steps: Check if legitimate activity (business cycle, planned event), compare to historical patterns, check for anomalies
   - Evidence to collect: Relevant logs for deviated metric
   - Escalation criteria: If no legitimate explanation found

4. **Escalation Procedures** (~40 lines)
   - When to escalate: True positive confirmed, user confirmation needed, containment needed
   - How to escalate: Create incident ticket, notify on-call (if after hours), brief Tier 2/IR
   - What to provide: Alert details, triage findings, evidence collected, recommended actions
   - Escalation paths: Tier 1 → Tier 2 → IR → CISO

5. **Evidence Collection Guide** (~30 lines)
   - What to collect: Relevant logs (±2 hours around event), screenshots, network captures
   - How to collect: SIEM exports, log file downloads, packet captures
   - Where to store: Incident case management system, secure evidence storage
   - Chain of custody: Log access, maintain integrity

6. **Common False Positive Scenarios** (~50 lines)
   - **Failed logins after password reset** - Expected, close as benign
   - **Maintenance window activities** - Expected, verify maintenance window, close as benign
   - **Backup jobs triggering data transfer alerts** - Expected, verify backup schedule, tune threshold
   - **Security scanner triggering attack signatures** - Expected, verify authorized scanner, whitelist
   - **Business cycle events** - Expected (e.g., month-end processing), update baseline

**Style**: Concise, actionable, step-by-step. Use checkboxes/bullet points. Tool-agnostic where possible.

**Reference**: Implements ISMS-POL-A.8.16-S2.3 (Alert Management & Response Requirements).

---

### 5.11.4 Annex D: Quick Reference Guide

**Target Length**: ~200 lines  
**Structure**:

1. **Policy Summary** (~30 lines)
   - Purpose of monitoring
   - Scope (what's monitored)
   - Key requirements (baselines, alert response, retention)

2. **Severity Classification Quick Reference** (~40 lines)
   - **Critical (P1)**: Definition, examples, response time (<15 min)
   - **High (P2)**: Definition, examples, response time (<1 hr)
   - **Medium (P3)**: Definition, examples, response time (<4 hrs)
   - **Low (P4)**: Definition, examples, response time (<1 day)

3. **SLA Quick Reference** (~20 lines)
   - MTTA targets: Critical <15min, High <1hr
   - MTTT targets: Critical <1hr, High <4hrs
   - MTTI targets: Critical <4hrs, High <24hrs

4. **Responsibility Quick Reference** (~30 lines)
   - Who triages alerts? SOC Tier 1
   - Who investigates complex alerts? SOC Tier 2/3
   - Who responds to incidents? Incident Response Team
   - Who establishes baselines? SOC Tier 2/3 + System Owners
   - Who approves baselines? SOC Lead + System Owner

5. **Escalation Paths** (~20 lines)
   - Technical: Tier 1 → Tier 2 → Tier 3 → Security Engineering
   - Incident: SOC → IR → CISO → Exec Management
   - Critical (after hours): Call on-call number

6. **Common Scenarios & Responses** (~30 lines)
   - Alert fires → Triage within SLA → Investigate or close
   - False positive → Document scenario, tune if repeated
   - True positive → Escalate to IR immediately
   - Baseline outdated → Review and update quarterly

7. **FAQ** (~30 lines)
   - Q: What is a baseline? A: Documented normal behavior...
   - Q: How long are logs retained? A: 90 days hot, 1 year total...
   - Q: Who do I contact for alert questions? A: SOC Lead...
   - Q: What if I can't triage in time? A: Escalate to Tier 2 immediately...
   - Q: Can I suppress noisy alerts? A: No, must tune detection rule instead...

**Style**: Ultra-concise, skimmable, visual (use tables, bullet points). One-pagers where possible.

**Reference**: Summarizes entire ISMS-POL-A.8.16 framework.

---

## 5.12 Implementation Notes for Next Session

When creating annexes:

1. **Read all policy sections first** (S1 through S4) to understand requirements
2. **Check Control 8.23 annexes** for structural examples (but adapt for monitoring)
3. **Keep practical** - these are operational documents, not policy documents
4. **Use examples liberally** - concrete examples make procedures clear
5. **Format consistently** - use code blocks for templates, tables for quick reference
6. **Cross-reference policies** - link back to policy sections that establish requirements
7. **Stay under line limits** - split if needed, but aim for single documents
8. **Test usability** - would a new SOC analyst understand this? Would system owner know what to do?

**Priority Order (if time limited)**:
1. **Annex C** (Alert Response) - Most critical for SOC operations
2. **Annex D** (Quick Reference) - High value, easy to create
3. **Annex B** (Baseline Template) - Critical for S2.2 implementation
4. **Annex A** (Capability Standards) - Can be deferred if time short

---

**END OF DOCUMENT**

---

## Related Documents in Framework

- **ISMS-POL-A.8.16-S1** (Purpose, Scope, Definitions) - Foundation
- **ISMS-POL-A.8.16-S2.x** (Requirements) - What annexes implement
- **ISMS-POL-A.8.16-S3** (Roles) - Who uses annexes
- **ISMS-POL-A.8.16-S4** (Governance) - How annexes are maintained
- **ISMS-POL-A.8.16-S5.A** (Capability Standards) - To be created
- **ISMS-POL-A.8.16-S5.B** (Baseline Template) - To be created
- **ISMS-POL-A.8.16-S5.C** (Alert Response) - To be created
- **ISMS-POL-A.8.16-S5.D** (Quick Reference) - To be created

---

*"Annexes are where policy meets reality. Make them practical, or they'll gather dust."*  
*—Security Operations Wisdom*