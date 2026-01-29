# ISMS-IMP-A.8.16.1 - Monitoring Infrastructure Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.16.1  
**Assessment Area:** Monitoring Infrastructure (Log Sources, Tools, Integration)  
**Related Policy:** ISMS-POL-A.8.16-S2.1  
**Purpose:** Assess monitoring infrastructure capabilities, log source coverage, and tool deployment  
**Generator Script:** `generate_a816_1_monitoring_infrastructure.py`  
**Output Filename:** `ISMS-IMP-A.8.16.1_Monitoring_Infrastructure_YYYYMMDD.xlsx`

---

## Workbook Structure

**Total Sheets:** 9
1. Instructions & Legend
2. 1. Monitoring Platform Capabilities
3. 2. Log Source Coverage
4. 3. Data Collection Architecture
5. 4. Integration & Enrichment
6. 5. Performance & Scalability
7. Summary Dashboard
8. Evidence Register
9. Approval Sign-Off

---

## Sheet 1: Instructions & Legend

### Header Section
- **Title:** "MONITORING INFRASTRUCTURE ASSESSMENT"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.16: Monitoring Activities"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

### Document Information Block
```
Document ID:           ISMS-IMP-A.8.16.1
Assessment Area:       Monitoring Infrastructure
Related Policy:        ISMS-POL-A.8.16-S2.1
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Semi-annual
Next Review Date:      [Auto-calculated: Assessment Date + 6 months]
```

### How to Use This Workbook
1. Complete each worksheet tab in sequence (1-5)
2. Use dropdown menus where provided - do not type directly
3. Fill all yellow-highlighted cells with your organization's information
4. Refer to reference tables on each sheet for guidance
5. Complete compliance checklists on each assessment sheet
6. Document exceptions in the Exception/Deviation blocks
7. Gather evidence and list in Evidence Register
8. Review Summary Dashboard for compliance gaps
9. Obtain approvals via Approval Sign-Off sheet

### Legend Table
| Symbol | Meaning | When to Use |
|--------|---------|-------------|
| ✅ Compliant | Requirement fully met | All controls in place |
| ⚠️ Partial | Requirement partially met | Some controls missing |
| ❌ Non-Compliant | Requirement not met | No controls in place |
| N/A | Not applicable | Requirement doesn't apply |

---

## Sheet 2: 1. Monitoring Platform Capabilities

### Header
**Title:** "1. MONITORING PLATFORM CAPABILITIES ASSESSMENT"  
**Policy Reference:** "Assess SIEM/monitoring platform capabilities per ISMS-POL-A.8.16-S2.1.4"

### Assessment Question (Row 3)
"Does your organization have monitoring platforms (SIEM, IDS/IPS, EDR, NDR) with adequate capabilities?"

### Response Dropdown (Row 4)
- **Options:** Yes, No, Partial, Planned, N/A

### Column Headers (Row 6) - 21 Columns (A-U)

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | Platform/Tool Name | 28 | Text | Free text |
| B | Platform Type | 20 | Dropdown | SIEM, IDS/IPS, EDR, NDR, UEBA, Log Management, Other |
| C | Vendor/Solution | 22 | Text | Free text |
| D | Deployment Model | 18 | Dropdown | On-Premises, Cloud, Hybrid |
| E | Log Collection Methods | 24 | Text | Free text (agents, syslog, API) |
| F | Parsing Capabilities | 20 | Dropdown | Excellent, Good, Limited, Poor |
| G | Storage & Indexing | 20 | Dropdown | Hot/Warm/Cold Tiers, Hot Only, Minimal |
| H | Search Performance | 18 | Dropdown | <10 sec, 10-60 sec, >60 sec |
| I | Real-Time Alerting | 18 | Dropdown | Yes, No, Limited |
| J | Correlation Engine | 18 | Dropdown | Advanced, Basic, None |
| K | Threat Intel Integration | 22 | Dropdown | Yes, No, Planned |
| L | SOAR Integration | 18 | Dropdown | Yes, No, Planned |
| M | Visualization/Dashboards | 20 | Dropdown | Excellent, Good, Limited, Poor |
| N | High Availability | 18 | Dropdown | Yes, No, Planned |
| O | Disaster Recovery | 18 | Dropdown | Documented, Tested, None |
| P | Current EPS Capacity | 18 | Text | Free text (events/sec) |
| Q | Implementation Status | 20 | Dropdown | ✅ Deployed, ⚠️ Partial, ❌ Not Deployed, Planned |
| R | Last Upgrade Date | 16 | Text | DD.MM.YYYY format |
| S | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| T | Gaps/Issues | 30 | Text | Free text |
| U | Remediation Priority | 18 | Dropdown | Critical, High, Medium, Low, None |

### Data Entry Rows
- **Rows 8-20:** 13 data entry rows (yellow-highlighted)
- **Row 7:** Example row (gray italic): "Splunk Enterprise SIEM, Cloud, Agents+API, Excellent parsing..."

### Compliance Checklist (Starting Row 22)
**Title:** "MONITORING PLATFORM CAPABILITIES CHECKLIST"

| # | Requirement | Status Column |
|---|-------------|---------------|
| 1 | Primary monitoring platform (SIEM) deployed | Dropdown |
| 2 | Log collection supports multiple methods (agents, syslog, API) | Dropdown |
| 3 | Parsing capabilities for common log formats (Windows, Linux, network devices) | Dropdown |
| 4 | Storage includes hot/warm/cold tiers for cost optimization | Dropdown |
| 5 | Search performance meets requirements (<10 sec for typical queries) | Dropdown |
| 6 | Real-time alerting capability enabled | Dropdown |
| 7 | Correlation engine supports multi-event detection | Dropdown |
| 8 | Threat intelligence integration implemented | Dropdown |
| 9 | SOAR or ticketing integration functional | Dropdown |
| 10 | Dashboards configured for SOC operations | Dropdown |
| 11 | High availability architecture implemented | Dropdown |
| 12 | Disaster recovery plan documented and tested | Dropdown |
| 13 | Platform capacity adequate for current log volume | Dropdown |
| 14 | Platform upgraded within last 12 months | Dropdown |
| 15 | Platform security hardened (RBAC, MFA, encryption) | Dropdown |

**Auto-Score:** `=COUNTIF(C22:C36,"✅ Compliant")&" / 15"`

### Reference Tables (Starting Row 40)

**Table 1: Monitoring Platform Types**
| Platform Type | Primary Purpose | Example Capabilities |
|---------------|----------------|---------------------|
| SIEM | Centralized log aggregation & correlation | Search, alert, correlate, dashboards |
| IDS/IPS | Network intrusion detection | Signature matching, anomaly detection |
| EDR | Endpoint threat detection | Process monitoring, behavioral analysis |
| NDR | Network traffic analysis | Flow analysis, encrypted traffic analysis |
| UEBA | User behavior analytics | Baseline deviation, risk scoring |

**Table 2: Critical SIEM Capabilities (Per S2.1.4.1)**
| Capability | Requirement Level | Validation Method |
|------------|------------------|-------------------|
| Multi-format log parsing | MUST HAVE | Test with sample logs |
| Indexed storage | MUST HAVE | Verify search performance |
| Real-time alerting | MUST HAVE | Test alert generation |
| Multi-event correlation | MUST HAVE | Create test correlation rule |
| Threat intel integration | MUST HAVE | Verify IOC matching |
| Search < 10 sec | SHOULD HAVE | Benchmark queries |

**Table 3: Deployment Models**
| Model | Advantages | Considerations |
|-------|------------|----------------|
| On-Premises | Full control, data residency | CapEx, maintenance burden |
| Cloud | Scalability, no maintenance | Data residency, vendor dependency |
| Hybrid | Flexibility, staged migration | Complexity, integration challenges |

### Exception/Deviation Block (Starting Row 70)
- **Header (Red):** "EXCEPTION/DEVIATION MANAGEMENT"
- **Fields:** Exception ID, Risk ID, Business Justification, Compensating Controls, Approval Status, Review Date

---

## Sheet 3: 2. Log Source Coverage

### Header
**Title:** "2. LOG SOURCE COVERAGE ASSESSMENT"  
**Policy Reference:** "Assess log source coverage per ISMS-POL-A.8.16-S2.1.2"

### Assessment Question
"Does your organization collect logs from all critical systems and adequate coverage of standard systems?"

### Column Headers (Row 6) - 20 Columns (A-T)

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | System/Asset Name | 28 | Text | Free text |
| B | System Type | 22 | Dropdown | Server, Network Device, Security Appliance, Endpoint, Cloud Service, Database, Application |
| C | Criticality | 15 | Dropdown | Critical, High, Medium, Low |
| D | Location | 18 | Text | Free text |
| E | System Owner | 20 | Text | Free text |
| F | OS/Platform | 18 | Text | Free text |
| G | Log Types Collected | 30 | Text | Free text (auth, network, system, app) |
| H | Collection Method | 18 | Dropdown | Agent, Syslog, API, WMI, None |
| I | Forwarding Destination | 22 | Text | Free text (SIEM name) |
| J | Log Volume (GB/day) | 16 | Text | Free text |
| K | Monitoring Status | 18 | Dropdown | ✅ Monitored, ⚠️ Partial, ❌ Not Monitored, N/A |
| L | Baseline Established | 18 | Dropdown | Yes, No, In Progress |
| M | Detection Rules Active | 18 | Dropdown | Yes, No, Partial |
| N | Last Log Verified | 16 | Text | DD.MM.YYYY |
| O | Compliance Requirement | 22 | Dropdown | Mandatory (Critical), Required (High), Recommended, Optional |
| P | Coverage Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| Q | Gaps/Issues | 30 | Text | Free text |
| R | Remediation Target Date | 16 | Text | DD.MM.YYYY |
| S | Remediation Owner | 20 | Text | Free text |
| T | Budget Required | 15 | Dropdown | Yes, No, Unknown |

### Compliance Checklist
1. All Tier 1 (Critical) systems monitored
2. >80% of Tier 2 (Standard) systems monitored
3. All perimeter firewalls monitored
4. All VPN gateways monitored
5. All domain controllers monitored
6. All database servers (production) monitored
7. All security appliances monitored
8. Cloud platform control plane logs collected
9. Network device logs collected
10. Authentication logs collected from all sources
11. Log collection verified within last 30 days
12. Log volume within platform capacity
13. No single points of failure in log collection
14. Log collection failures generate alerts
15. Documentation of monitoring coverage maintained

### Reference Tables
- **Table 1:** Mandatory Log Sources (Tier 1 - Critical Systems)
- **Table 2:** Standard Log Sources (Tier 2 - High Priority)
- **Table 3:** Log Types by System Category

---

## Sheet 4: 3. Data Collection Architecture

### Header
**Title:** "3. DATA COLLECTION ARCHITECTURE ASSESSMENT"  
**Policy Reference:** "Assess collection architecture per ISMS-POL-A.8.16-S2.1.5"

### Column Headers - 19 Columns (A-S)

| Col | Header | Width |
|-----|--------|-------|
| A | Network Segment/Zone | 28 |
| B | Number of Systems | 15 |
| C | Log Collector Deployed | 18 |
| D | Collector Type | 20 |
| E | Collector Capacity (EPS) | 18 |
| F | Current Load (EPS) | 16 |
| G | Utilization % | 12 |
| H | Redundancy | 15 |
| I | Bandwidth Impact | 18 |
| J | Encryption in Transit | 18 |
| K | Buffering Configured | 18 |
| L | Failover Tested | 16 |
| M | Health Monitoring | 18 |
| N | Last Health Check | 16 |
| O | Deployment Status | 18 |
| P | Compliance Status | 18 |
| Q | Issues/Gaps | 30 |
| R | Remediation Priority | 18 |
| S | Notes | 25 |

### Compliance Checklist
- Collection architecture documented
- Collectors deployed in each network segment
- Collector capacity adequate (utilization <70%)
- Redundancy for critical segments
- Encryption (TLS) for log transmission
- Buffering configured to handle spikes
- Failover tested within last 6 months
- Collector health monitored continuously
- Network bandwidth assessed and adequate
- Single points of failure identified and mitigated

---

## Sheet 5: 4. Integration & Enrichment

### Header
**Title:** "4. INTEGRATION & ENRICHMENT ASSESSMENT"  
**Policy Reference:** "Assess integrations per ISMS-POL-A.8.16-S2.1.4.3"

### Column Headers - 18 Columns (A-R)

| Col | Header | Width |
|-----|--------|-------|
| A | Integration Type | 25 |
| B | Integration Target | 25 |
| C | Integration Method | 20 |
| D | Data Flow Direction | 18 |
| E | Purpose/Use Case | 30 |
| F | Implementation Status | 20 |
| G | Data Quality | 15 |
| H | Latency | 12 |
| I | Error Rate | 12 |
| J | Last Tested | 14 |
| K | Automation Level | 18 |
| L | Business Value | 15 |
| M | Technical Complexity | 18 |
| N | Compliance Status | 18 |
| O | Issues/Limitations | 30 |
| P | Improvement Opportunities | 30 |
| Q | Priority | 15 |
| R | Notes | 25 |

**Integration Types:** Threat Intelligence, SOAR, Ticketing, Asset Management, Identity Management, Vulnerability Management, Email/Communication, Other

### Compliance Checklist
- Threat intelligence feeds integrated
- IOC matching automated
- Ticketing system integrated
- SOAR platform integrated (if available)
- Asset management enrichment configured
- Identity management enrichment configured
- Email notification configured
- All integrations documented
- Integration health monitored
- Data quality validated regularly

---

## Sheet 6: 5. Performance & Scalability

### Header
**Title:** "5. PERFORMANCE & SCALABILITY ASSESSMENT"  
**Policy Reference:** "Assess performance per ISMS-POL-A.8.16-S2.1.9"

### Column Headers - 17 Columns (A-Q)

| Col | Header | Width |
|-----|--------|-------|
| A | Metric Category | 25 |
| B | Metric Name | 28 |
| C | Current Value | 18 |
| D | Target/SLA | 18 |
| E | Status | 15 |
| F | Trend (Last 30 Days) | 18 |
| G | Peak Value | 15 |
| H | Measurement Method | 22 |
| I | Measurement Frequency | 18 |
| J | Last Measured | 14 |
| K | Alert Threshold | 16 |
| L | Alerting Configured | 16 |
| M | Issue Identified | 15 |
| N | Root Cause | 30 |
| O | Remediation Plan | 30 |
| P | Target Date | 14 |
| Q | Notes | 25 |

**Metrics to Assess:**
- Ingestion Rate (EPS)
- Search Query Time
- Dashboard Load Time
- Alert Generation Latency
- Indexing Lag Time
- Storage Utilization %
- CPU Utilization %
- Memory Utilization %
- Network Bandwidth Usage
- Disk I/O Performance

### Compliance Checklist
- Performance metrics tracked continuously
- Search performance <10 sec (hot storage)
- Alert latency <2 min (critical alerts)
- Indexing lag <5 min
- Storage utilization <80%
- CPU utilization <70% (sustained)
- Capacity planning conducted annually
- Performance issues generate alerts
- Performance trends analyzed monthly
- Scalability roadmap documented

---

## Sheet 7: Summary Dashboard

### Section 1: Compliance Summary (Rows 3-10)
| Assessment Area | Total | Compliant | Partial | Non-Compliant | N/A | % Compliant |
|-----------------|-------|-----------|---------|---------------|-----|-------------|
| 1. Platform Capabilities | Formula | Formula | Formula | Formula | Formula | Formula |
| 2. Log Source Coverage | Formula | Formula | Formula | Formula | Formula | Formula |
| 3. Collection Architecture | Formula | Formula | Formula | Formula | Formula | Formula |
| 4. Integration & Enrichment | Formula | Formula | Formula | Formula | Formula | Formula |
| 5. Performance & Scalability | Formula | Formula | Formula | Formula | Formula | Formula |
| **OVERALL** | Formula | Formula | Formula | Formula | Formula | Formula |

### Section 2: Critical Gaps (Rows 67-75)
- Priority | Gap Description | Risk Level | System/Area Affected | Target Date | Owner

### Section 3: Coverage Analysis (Rows 13-25)
- Critical systems monitored / total critical
- Standard systems monitored / total standard
- Log sources integrated / total sources
- Network segments covered / total segments
- Detection coverage %

### Section 4: Platform Health (Rows 28-40)
- Platform availability % (target: >99.5%)
- Search performance (target: <10 sec)
- Alert latency (target: <2 min)
- Storage utilization % (target: <80%)
- CPU utilization % (target: <70%)

### Section 5: Integration Status (Rows 43-55)
- Threat intel integration status
- SOAR integration status
- Ticketing integration status
- Enrichment quality score

### Section 6: Remediation Tracking (Rows 58-64)
- Open gaps by priority
- Remediation progress %
- Overdue remediations

---

## Sheet 8: Evidence Register

**100 rows for evidence tracking**

Columns:
- Evidence ID
- Evidence Type
- Description
- Related Requirement
- Date Collected
- Collected By
- Location/Link
- Verification Status
- Notes

---

## Sheet 9: Approval Sign-Off

3-level approval workflow:
1. Prepared By (Assessor)
2. Reviewed By (SOC Lead / Security Engineering)
3. Approved By (CISO)

Fields: Name, Title, Signature, Date, Comments

---

**END OF SPECIFICATION**

# ISMS-IMP-A.8.16.2 - Baseline & Detection Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.16.2  
**Assessment Area:** Baseline Establishment & Anomaly Detection  
**Related Policy:** ISMS-POL-A.8.16-S2.2  
**Purpose:** Assess baseline documentation, anomaly detection capabilities, and detection rule effectiveness  
**Generator Script:** `generate_a816_2_baseline_detection.py`  
**Output Filename:** `ISMS-IMP-A.8.16.2_Baseline_Detection_YYYYMMDD.xlsx`

---

## Workbook Structure

**Total Sheets:** 9
1. Instructions & Legend
2. 1. Baseline Documentation
3. 2. Detection Rule Inventory
4. 3. Anomaly Detection Capabilities
5. 4. Threshold Configuration
6. 5. Detection Effectiveness
7. Summary Dashboard
8. Evidence Register
9. Approval Sign-Off

---

## Sheet 2: 1. Baseline Documentation

### Header
**Title:** "1. BASELINE DOCUMENTATION ASSESSMENT"  
**Policy Reference:** "Assess baseline establishment per ISMS-POL-A.8.16-S2.2.2"

### Assessment Question
"Are baselines documented for all critical systems with measurable metrics?"

### Column Headers (Row 6) - 22 Columns (A-V)

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | System/Asset Name | 28 | Text | Free text |
| B | System Type | 22 | Dropdown | Domain Controller, Database Server, Firewall, VPN Gateway, Web Server, Application Server, Endpoint, Other |
| C | Criticality Tier | 15 | Dropdown | Tier 1 (Critical), Tier 2 (Standard), Tier 3 (Low) |
| D | System Owner | 20 | Text | Free text |
| E | Baseline Established | 16 | Dropdown | Yes, No, In Progress |
| F | Baseline Date | 14 | Text | DD.MM.YYYY |
| G | Observation Period (Days) | 18 | Text | Free text |
| H | Metrics Documented | 30 | Text | Free text (auth, network, resources) |
| I | Statistical Profile | 22 | Dropdown | Complete (Mean/Median/StdDev/95th), Partial, Minimal, None |
| J | Time-Aware Baselines | 18 | Dropdown | Yes (Business/Off-Hours/Weekend), Partial, No |
| K | Baseline Review Frequency | 20 | Dropdown | Quarterly, Semi-Annually, Annually, Never |
| L | Last Review Date | 14 | Text | DD.MM.YYYY |
| M | Next Review Date | 14 | Text | DD.MM.YYYY |
| N | Thresholds Derived | 16 | Dropdown | Yes, No, Partial |
| O | Threshold Methodology | 22 | Dropdown | 95th %ile × Multiplier, Static, Expert Judgment, None |
| P | Baseline Accuracy | 16 | Dropdown | High, Medium, Low, Unknown |
| Q | False Positive Rate | 16 | Text | Free text (%) |
| R | Baseline Approved By | 20 | Text | Free text |
| S | Documentation Location | 25 | Text | Free text (file path, URL) |
| T | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| U | Issues/Gaps | 30 | Text | Free text |
| V | Remediation Priority | 18 | Dropdown | Critical, High, Medium, Low, None |

### Data Entry Rows
- **Rows 8-25:** 18 data entry rows (yellow-highlighted)
- **Row 7:** Example: "DC01-Primary, Domain Controller, Tier 1, IT Ops, Yes, 15.09.2025..."

### Compliance Checklist (Starting Row 27)
**Title:** "BASELINE DOCUMENTATION CHECKLIST"

1. 100% of Tier 1 (Critical) systems have documented baselines
2. >80% of Tier 2 (Standard) systems have documented baselines
3. Baselines include mean, median, std dev, 95th percentile
4. Time-aware baselines established (business hours, off-hours, weekend)
5. Observation period ≥30 days during known-good periods
6. Exclusions documented (incidents, maintenance windows)
7. Thresholds derived using documented methodology (95th × multiplier)
8. Baselines approved by system owner and SOC lead
9. Baseline review schedule defined (quarterly for Tier 1, semi-annually for Tier 2)
10. Reviews conducted on schedule
11. Baseline changes version controlled
12. False positive rates tracked (<25% target)
13. Baseline documentation stored in accessible location
14. Baseline templates used consistently
15. Baselines integrated with detection rules

**Auto-Score:** `=COUNTIF(C27:C41,"✅ Compliant")&" / 15"`

### Reference Tables (Starting Row 45)

**Table 1: Baseline Maturity Levels**
| Level | Description | Characteristics | Compliance |
|-------|-------------|-----------------|-----------|
| Level 0 | No Baselines | Subjective opinions, anecdotal | Non-Compliant |
| Level 1 | Basic Baselines | Critical systems, basic stats | Minimum Viable |
| Level 2 | Comprehensive | All systems, full stats, time-aware | Full Compliance |
| Level 3 | Automated | ML/AI, continuous adaptation | Excellence |

**Table 2: Required Metrics by System Type**
| System Type | Authentication Metrics | Network Metrics | System Metrics |
|-------------|----------------------|-----------------|----------------|
| Domain Controller | Logins/hour, failed auth, privileged access | Replication traffic, LDAP queries | CPU, memory, event logs |
| Database Server | Query count, connections, admin access | Data volume, connection sources | CPU, memory, disk I/O |
| Firewall | Connections/min, blocked attempts, rule hits | Throughput, session count | CPU, memory, interface utilization |

**Table 3: Threshold Derivation Methodology**
| Criticality | Risk Level | Multiplier | Example |
|-------------|-----------|------------|---------|
| Critical | High | 1.2x | 95th %ile = 150, threshold = 180 |
| Critical | Medium | 1.5x | 95th %ile = 150, threshold = 225 |
| Standard | Medium | 1.5x | 95th %ile = 100, threshold = 150 |
| Standard | Low | 2.0x | 95th %ile = 100, threshold = 200 |

---

## Sheet 3: 2. Detection Rule Inventory

### Header
**Title:** "2. DETECTION RULE INVENTORY"  
**Policy Reference:** "Assess detection rules per ISMS-POL-A.8.16-S2.2.5"

### Column Headers - 24 Columns (A-X)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Rule ID/Name | 28 | Text |
| B | Detection Type | 20 | Dropdown: Signature-Based, Threshold-Based, Anomaly-Based, Heuristic, Correlation |
| C | MITRE ATT&CK Technique | 22 | Text |
| D | Alert Severity | 15 | Dropdown: Critical, High, Medium, Low |
| E | Rule Description | 35 | Text |
| F | Data Sources Required | 30 | Text |
| G | Detection Logic | 35 | Text |
| H | Time Window | 15 | Text |
| I | Threshold Value | 15 | Text |
| J | Baseline-Derived | 16 | Dropdown: Yes, No, N/A |
| K | Rule Status | 16 | Dropdown: Active, Testing, Disabled, Retired |
| L | Created Date | 14 | Text: DD.MM.YYYY |
| M | Last Tuned | 14 | Text: DD.MM.YYYY |
| N | Tuning Frequency | 16 | Dropdown: Quarterly, Semi-Annually, Annually, As-Needed |
| O | Alert Volume (30d) | 16 | Text |
| P | False Positive Rate | 16 | Text: % |
| Q | True Positive Count | 16 | Text |
| R | Detection Rate (Testing) | 18 | Text: % |
| S | Last Tested | 14 | Text: DD.MM.YYYY |
| T | Rule Owner | 20 | Text |
| U | Playbook Reference | 22 | Text |
| V | Compliance Status | 18 | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| W | Issues/Gaps | 30 | Text |
| X | Tuning Priority | 16 | Dropdown: Critical, High, Medium, Low, None |

### Compliance Checklist
1. Detection rules documented in inventory
2. Each rule has unique ID
3. MITRE ATT&CK mapping documented
4. Severity classification assigned
5. Detection logic documented
6. Baseline-derived rules identified
7. Rules tested before production deployment
8. Testing results documented (detection rate >90% target)
9. False positive rate tracked (<25% overall, <10% critical)
10. High false positive rules tuned within 30 days
11. Rules reviewed quarterly (critical) / semi-annually (standard)
12. Tuning changes version controlled
13. Rule owner assigned
14. Playbook exists for each rule
15. Retired rules properly archived

---

## Sheet 4: 3. Anomaly Detection Capabilities

### Header
**Title:** "3. ANOMALY DETECTION CAPABILITIES"  
**Policy Reference:** "Assess anomaly detection per ISMS-POL-A.8.16-S2.2.4"

### Column Headers - 19 Columns (A-S)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Detection Method | 28 | Dropdown: Signature-Based, Threshold-Based, Anomaly-Based, Behavioral, Heuristic, Correlation |
| B | Use Cases | 30 | Text |
| C | Technology/Tool | 22 | Text |
| D | Implementation Status | 18 | Dropdown: ✅ Deployed, ⚠️ Partial, ❌ Not Deployed, Planned |
| E | Coverage (Systems) | 18 | Text: % or count |
| F | Baseline Dependency | 16 | Dropdown: High, Medium, Low, None |
| G | Machine Learning Used | 18 | Dropdown: Yes, No, Planned |
| H | Detection Accuracy | 16 | Text: % |
| I | False Positive Rate | 16 | Text: % |
| J | Alert Volume (30d) | 16 | Text |
| K | Mean Time to Detect | 16 | Text: minutes |
| L | Detection Rate | 16 | Text: % |
| M | Last Effectiveness Test | 16 | Text: DD.MM.YYYY |
| N | Strengths | 30 | Text |
| O | Limitations | 30 | Text |
| P | Integration Quality | 18 | Dropdown: Excellent, Good, Fair, Poor |
| Q | Compliance Status | 18 | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| R | Improvement Opportunities | 30 | Text |
| S | Priority | 16 | Dropdown: Critical, High, Medium, Low |

### Compliance Checklist
1. Multiple detection methodologies implemented
2. Signature-based detection deployed (mandatory)
3. Threshold-based detection deployed (mandatory for critical systems)
4. Anomaly-based detection deployed (recommended)
5. Correlation-based detection deployed (mandatory with SIEM)
6. Detection methods complement each other
7. Baseline-dependent methods have documented baselines
8. Detection accuracy measured (target >90%)
9. False positive rates acceptable (<25% overall)
10. Detection effectiveness tested quarterly

---

## Sheet 5: 4. Threshold Configuration

### Header
**Title:** "4. THRESHOLD CONFIGURATION ASSESSMENT"  
**Policy Reference:** "Assess thresholds per ISMS-POL-A.8.16-S2.2.3"

### Column Headers - 18 Columns (A-R)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | System/Metric | 28 | Text |
| B | Metric Type | 22 | Text |
| C | Baseline 95th Percentile | 18 | Text |
| D | Criticality | 15 | Dropdown: Critical, High, Medium, Low |
| E | Risk Level | 15 | Dropdown: High, Medium, Low |
| F | Multiplier Applied | 14 | Text: e.g., 1.2x |
| G | Warning Threshold | 16 | Text |
| H | Critical Threshold | 16 | Text |
| I | Threshold Rationale | 30 | Text |
| J | Last Validated | 14 | Text: DD.MM.YYYY |
| K | Validation Method | 22 | Text |
| L | Alerts Generated (30d) | 18 | Text |
| M | False Positive Rate | 16 | Text: % |
| N | True Positive Count | 16 | Text |
| O | Adjustment Needed | 16 | Dropdown: Yes, No, Under Review |
| P | Compliance Status | 18 | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| Q | Issues/Notes | 30 | Text |
| R | Tuning Priority | 16 | Dropdown: Critical, High, Medium, Low, None |

### Compliance Checklist
1. Thresholds derived from documented baselines
2. Derivation methodology documented (95th × multiplier)
3. Multipliers justified based on criticality and risk
4. Multi-threshold alerting implemented (warning + critical)
5. Thresholds validated quarterly
6. False positive rates tracked per threshold
7. High false positive thresholds adjusted within 30 days
8. Threshold changes documented and approved
9. Thresholds tested before production deployment
10. Threshold configuration backed up

---

## Sheet 6: 5. Detection Effectiveness

### Header
**Title:** "5. DETECTION EFFECTIVENESS ASSESSMENT"  
**Policy Reference:** "Assess effectiveness per ISMS-POL-A.8.16-S2.2.8"

### Column Headers - 20 Columns (A-T)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Test Scenario/Attack Type | 30 | Text |
| B | MITRE ATT&CK Technique | 22 | Text |
| C | Test Method | 22 | Dropdown: Purple Team, Red Team, Atomic Red Team, Caldera, Manual Simulation, Other |
| D | Test Date | 14 | Text: DD.MM.YYYY |
| E | Tester/Team | 20 | Text |
| F | Detection Expected | 16 | Dropdown: Yes, No |
| G | Alert Generated | 16 | Dropdown: Yes, No |
| H | Detection Time (MTTD) | 16 | Text: minutes |
| I | Alert Severity | 15 | Dropdown: Critical, High, Medium, Low |
| J | Detection Rule(s) Triggered | 30 | Text |
| K | Detection Accuracy | 16 | Dropdown: Accurate, Partial, Inaccurate, Missed |
| L | False Negative | 15 | Dropdown: Yes, No |
| M | Root Cause (if missed) | 30 | Text |
| N | Remediation Action | 30 | Text |
| O | Remediation Status | 18 | Dropdown: Complete, In Progress, Planned, Deferred |
| P | Retest Date | 14 | Text: DD.MM.YYYY |
| Q | Retest Result | 16 | Dropdown: Passed, Failed, Pending |
| R | Compliance Status | 18 | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| S | Notes | 30 | Text |
| T | Priority | 16 | Dropdown: Critical, High, Medium, Low |

### Compliance Checklist
1. Detection effectiveness testing conducted quarterly
2. Test scenarios cover MITRE ATT&CK techniques
3. Critical attack types tested (credential dumping, lateral movement, exfiltration)
4. Testing methodology documented
5. Detection rate measured (target >90%)
6. Mean Time to Detect (MTTD) measured (target <5 min for critical)
7. False negatives tracked and analyzed
8. Gaps remediated within 30 days (critical) / 90 days (high)
9. Retesting conducted after remediation
10. Results reported to CISO quarterly

---

## Sheet 7: Summary Dashboard

### Section 1: Baseline Coverage (Rows 3-15)
- Total systems requiring baselines
- Systems with complete baselines
- Systems with partial baselines
- Systems without baselines
- Baseline completeness % (target: 100% Tier 1, >80% Tier 2)
- Baselines reviewed on schedule %
- Baseline staleness (overdue reviews)

### Section 2: Detection Rule Health (Rows 18-30)
- Total active detection rules
- Rules by severity (Critical/High/Medium/Low)
- Rules by type (Signature/Threshold/Anomaly/Correlation)
- Average false positive rate (target: <25%)
- Rules requiring tuning
- Rules tested in last 6 months %

### Section 3: Detection Effectiveness (Rows 33-45)
- Overall detection rate % (target: >90%)
- MTTD average (target: <5 min for critical)
- MITRE ATT&CK coverage % (techniques with detection)
- False negative rate % (target: <5% for critical threats)
- Tests conducted (last quarter)
- Gaps remediated / total gaps

### Section 4: Compliance Summary (Rows 48-58)
| Assessment Area | Total | Compliant | Partial | Non-Compliant | % |
|-----------------|-------|-----------|---------|---------------|---|
| 1. Baseline Documentation | Formula | Formula | Formula | Formula | Formula |
| 2. Detection Rule Inventory | Formula | Formula | Formula | Formula | Formula |
| 3. Anomaly Detection | Formula | Formula | Formula | Formula | Formula |
| 4. Threshold Configuration | Formula | Formula | Formula | Formula | Formula |
| 5. Detection Effectiveness | Formula | Formula | Formula | Formula | Formula |
| **OVERALL** | Formula | Formula | Formula | Formula | Formula |

### Section 5: Critical Gaps (Rows 67-75)
- Priority | Gap Description | Impact | System/Rule Affected | Target Date | Owner

---

## Sheets 8-9: Evidence Register & Approval Sign-Off
(Standard format as per IMP-A.8.16.1)

---

**END OF SPECIFICATION**

# ISMS-IMP-A.8.16.3 - Coverage Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.16.3  
**Assessment Area:** Monitoring Coverage (Assets, Networks, Users, Applications)  
**Related Policy:** ISMS-POL-A.8.16-S2.1.1, S2.1.2  
**Purpose:** Assess completeness of monitoring coverage across organizational assets  
**Generator Script:** `generate_a816_3_coverage_assessment.py`  
**Output Filename:** `ISMS-IMP-A.8.16.3_Coverage_Assessment_YYYYMMDD.xlsx`

---

## Workbook Structure

**Total Sheets:** 9
1. Instructions & Legend
2. 1. Asset Inventory & Coverage
3. 2. Network Segment Coverage
4. 3. User & Identity Coverage
5. 4. Application & Service Coverage
6. 5. Coverage Gap Analysis
7. Summary Dashboard
8. Evidence Register
9. Approval Sign-Off

---

## Sheet 2: 1. Asset Inventory & Coverage

### Header
**Title:** "1. ASSET INVENTORY & MONITORING COVERAGE"  
**Policy Reference:** "Assess asset coverage per ISMS-POL-A.8.16-S2.1.1"

### Assessment Question
"Are all organizational assets inventoried and appropriate assets monitored?"

### Column Headers - 23 Columns (A-W)

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | Asset ID | 15 | Text | Free text |
| B | Asset Name | 28 | Text | Free text |
| C | Asset Type | 22 | Dropdown | Server, Network Device, Security Device, Endpoint, Cloud Resource, Database, Application, Container, IoT Device, Other |
| D | Operating System | 22 | Text | Free text |
| E | Location | 18 | Text | Free text |
| F | Business Unit | 20 | Text | Free text |
| G | Asset Owner | 20 | Text | Free text |
| H | Data Classification | 18 | Dropdown | Confidential, Internal, Public |
| I | Criticality | 15 | Dropdown | Critical, High, Medium, Low |
| J | Regulatory Scope | 22 | Dropdown | PCI-DSS, HIPAA, GDPR, SOX, Multiple, None |
| K | Monitoring Required | 16 | Dropdown | Mandatory, Recommended, Optional, N/A |
| L | Currently Monitored | 16 | Dropdown | Yes, No, Partial |
| M | Log Types Collected | 30 | Text | Free text |
| N | Monitoring Platform | 22 | Text | Free text |
| O | Baseline Established | 16 | Dropdown | Yes, No, N/A |
| P | Detection Rules Active | 18 | Text | Free text (count) |
| Q | Last Log Verified | 14 | Text | DD.MM.YYYY |
| R | Coverage Status | 18 | Dropdown | ✅ Full Coverage, ⚠️ Partial Coverage, ❌ No Coverage, N/A |
| S | Gap Reason | 30 | Text | Free text |
| T | Exception Approved | 16 | Dropdown | Yes, No, N/A |
| U | Target Coverage Date | 14 | Text | DD.MM.YYYY |
| V | Responsible Party | 20 | Text | Free text |
| W | Notes | 25 | Text | Free text |

### Data Entry Rows
- **Rows 8-50:** 43 data entry rows (comprehensive asset inventory)

### Compliance Checklist
1. Complete asset inventory maintained
2. Asset inventory updated at least quarterly
3. All assets classified by criticality
4. All Critical assets monitored (100%)
5. >80% of High priority assets monitored
6. >60% of Medium priority assets monitored
7. All PCI-DSS scope systems monitored
8. All HIPAA scope systems monitored
9. All systems handling confidential data monitored
10. Monitoring coverage gaps documented
11. Exceptions formally approved
12. Gap remediation plans exist
13. Coverage status reported monthly
14. Asset decommissioning process includes monitoring removal
15. New assets onboarded to monitoring within 30 days

### Reference Tables

**Table 1: Coverage Requirements by Criticality**
| Criticality | Coverage Requirement | Baseline Required | Detection Rules Required | Review Frequency |
|-------------|---------------------|-------------------|-------------------------|------------------|
| Critical | 100% mandatory | Yes | Yes (multiple) | Quarterly |
| High | >80% recommended | Yes | Yes | Semi-annually |
| Medium | >60% recommended | Recommended | Recommended | Annually |
| Low | Optional | No | No | As needed |

**Table 2: Coverage Requirements by Regulatory Scope**
| Regulation | Monitoring Requirement | Log Retention | Specific Controls |
|------------|----------------------|---------------|-------------------|
| PCI-DSS | Mandatory for CDE | 1 year minimum | File integrity, access control, network monitoring |
| HIPAA | Mandatory for PHI systems | 6 years | Access logs, audit trails, security events |
| GDPR | Recommended | Per data retention policy | Access logs, breach detection |
| SOX | Mandatory for financial systems | 7 years | Change management, access control |

---

## Sheet 3: 2. Network Segment Coverage

### Header
**Title:** "2. NETWORK SEGMENT COVERAGE ASSESSMENT"  
**Policy Reference:** "Assess network coverage per ISMS-POL-A.8.16-S2.1.1"

### Column Headers - 20 Columns (A-T)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Network Segment/Zone | 28 | Text |
| B | Segment Type | 22 | Dropdown: Production, DMZ, Internal, Management, Guest, Partner, Development, Test, Cloud VPC, Other |
| C | IP Range/CIDR | 20 | Text |
| D | VLAN ID | 12 | Text |
| E | Number of Assets | 15 | Text |
| F | Criticality | 15 | Dropdown: Critical, High, Medium, Low |
| G | Data Classification | 18 | Dropdown: Confidential, Internal, Public |
| H | Perimeter Monitoring | 18 | Dropdown: Firewall, IDS/IPS, Both, None |
| I | Flow Monitoring | 16 | Dropdown: Yes, No, Planned |
| J | DNS Monitoring | 16 | Dropdown: Yes, No, Planned |
| K | Endpoint Monitoring | 18 | Dropdown: Yes (EDR), Partial, No |
| L | Log Collection Active | 18 | Dropdown: Yes, Partial, No |
| M | Network Tap/SPAN | 16 | Dropdown: Yes, No, Planned |
| N | Isolation Status | 16 | Dropdown: Isolated, Semi-Isolated, Open |
| O | Coverage Status | 18 | Dropdown: ✅ Full, ⚠️ Partial, ❌ None, N/A |
| P | Gaps Identified | 30 | Text |
| Q | Exception Approved | 16 | Dropdown: Yes, No, N/A |
| R | Target Date | 14 | Text: DD.MM.YYYY |
| S | Responsible Party | 20 | Text |
| T | Notes | 25 | Text |

### Compliance Checklist
1. All network segments inventoried
2. All production segments monitored
3. All DMZ segments monitored
4. Critical segments have redundant monitoring
5. Perimeter traffic monitored (firewall + IDS/IPS)
6. Internal traffic monitored (flow data)
7. DNS queries monitored
8. Endpoints monitored (EDR/AV integration)
9. East-west traffic visibility (lateral movement detection)
10. Cloud network segments included

---

## Sheet 4: 3. User & Identity Coverage

### Header
**Title:** "3. USER & IDENTITY MONITORING COVERAGE"  
**Policy Reference:** "Assess user monitoring per ISMS-POL-A.8.16-S2.1.2"

### Column Headers - 19 Columns (A-S)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Identity System | 25 | Text |
| B | System Type | 22 | Dropdown: Active Directory, Azure AD, LDAP, SAML IdP, OAuth Provider, Database Auth, Application-Specific, Other |
| C | User Count | 15 | Text |
| D | Privileged Account Count | 20 | Text |
| E | Service Account Count | 20 | Text |
| F | Authentication Logs Collected | 22 | Dropdown: Yes, Partial, No |
| G | Authorization Logs Collected | 22 | Dropdown: Yes, Partial, No |
| H | Password Change Logs | 20 | Dropdown: Yes, No |
| I | Privilege Escalation Logs | 22 | Dropdown: Yes, No |
| J | MFA Events Logged | 18 | Dropdown: Yes, No, N/A |
| K | SSO Events Logged | 18 | Dropdown: Yes, No, N/A |
| L | Failed Login Monitoring | 20 | Dropdown: Yes, No |
| M | After-Hours Access Monitoring | 22 | Dropdown: Yes, No |
| N | Geographic Anomaly Detection | 22 | Dropdown: Yes, No, Planned |
| O | User Behavior Analytics | 22 | Dropdown: Yes (UEBA), Planned, No |
| P | Privileged Access Monitoring | 22 | Dropdown: Yes (PAM integrated), Partial, No |
| Q | Coverage Status | 18 | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| R | Gaps/Issues | 30 | Text |
| S | Priority | 16 | Dropdown: Critical, High, Medium, Low |

### Compliance Checklist
1. Primary identity system (AD/Azure AD) monitored
2. All authentication events logged
3. Failed login attempts monitored and alerted
4. Privileged account usage monitored
5. Service account usage monitored
6. Password changes logged
7. Privilege escalation logged
8. MFA events logged (if MFA deployed)
9. SSO events logged (if SSO deployed)
10. After-hours access monitored
11. Geographic anomalies detected
12. User behavior baselines established
13. Dormant accounts identified
14. Privileged access sessions recorded (PAM)
15. Identity correlation across systems

---

## Sheet 5: 4. Application & Service Coverage

### Header
**Title:** "4. APPLICATION & SERVICE MONITORING COVERAGE"  
**Policy Reference:** "Assess application coverage per ISMS-POL-A.8.16-S2.1.2"

### Column Headers - 21 Columns (A-U)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Application/Service Name | 28 | Text |
| B | Application Type | 22 | Dropdown: Web Application, Database, API, Microservice, SaaS, Mobile App, Desktop App, Other |
| C | Business Unit | 20 | Text |
| D | Application Owner | 20 | Text |
| E | Data Classification | 18 | Dropdown: Confidential, Internal, Public |
| F | Criticality | 15 | Dropdown: Critical, High, Medium, Low |
| G | User Base | 18 | Text |
| H | Application Logs Collected | 22 | Dropdown: Yes, Partial, No |
| I | API Logs Collected | 18 | Dropdown: Yes, No, N/A |
| J | Database Logs Collected | 22 | Dropdown: Yes, Partial, No |
| K | Error/Exception Logging | 20 | Dropdown: Yes, Partial, No |
| L | Transaction Logging | 18 | Dropdown: Yes, No |
| M | Access Control Logs | 20 | Dropdown: Yes, No |
| N | Data Export Monitoring | 20 | Dropdown: Yes, No |
| O | Performance Monitoring | 20 | Dropdown: Yes, No |
| P | WAF Integration | 16 | Dropdown: Yes, No, N/A |
| Q | APM Integration | 16 | Dropdown: Yes, No |
| R | Coverage Status | 18 | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| S | Gaps | 30 | Text |
| T | Target Date | 14 | Text: DD.MM.YYYY |
| U | Priority | 16 | Dropdown: Critical, High, Medium, Low |

### Compliance Checklist
1. All critical applications monitored
2. >80% of high-priority applications monitored
3. Application error/exception logs collected
4. API calls logged (if API-based)
5. Database queries logged (if database-backed)
6. User access logged
7. Data exports/downloads monitored
8. File uploads monitored
9. Configuration changes logged
10. WAF deployed for internet-facing apps
11. APM integrated for performance visibility
12. Cloud application logs collected (SaaS)
13. Mobile app backend logs collected
14. Third-party integrations monitored
15. Application security events forwarded to SIEM

---

## Sheet 6: 5. Coverage Gap Analysis

### Header
**Title:** "5. COVERAGE GAP ANALYSIS"  
**Policy Reference:** "Assess gaps per ISMS-POL-A.8.16-S2.1"

### Column Headers - 18 Columns (A-R)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Gap ID | 12 | Text |
| B | Gap Category | 22 | Dropdown: Asset Not Monitored, Log Source Missing, Network Segment Gap, User/Identity Gap, Application Gap, Detection Gap, Other |
| C | Affected Asset/System | 28 | Text |
| D | Gap Description | 35 | Text |
| E | Business Impact | 30 | Text |
| F | Risk Level | 15 | Dropdown: Critical, High, Medium, Low |
| G | Root Cause | 30 | Text |
| H | Exception Approved | 16 | Dropdown: Yes, No, Pending |
| I | Exception ID | 15 | Text |
| J | Compensating Controls | 30 | Text |
| K | Remediation Plan | 35 | Text |
| L | Remediation Owner | 20 | Text |
| M | Target Date | 14 | Text: DD.MM.YYYY |
| N | Budget Required | 15 | Dropdown: Yes, No, Unknown |
| O | Status | 18 | Dropdown: Open, In Progress, Resolved, Deferred, Accepted |
| P | Status Date | 14 | Text: DD.MM.YYYY |
| Q | Verification Method | 25 | Text |
| R | Notes | 30 | Text |

### Compliance Checklist
1. All coverage gaps identified
2. Gaps categorized by type
3. Risk level assessed for each gap
4. Root cause analysis conducted
5. Critical gaps remediated within 30 days
6. High gaps remediated within 90 days
7. Exceptions formally approved
8. Compensating controls documented
9. Remediation plans documented
10. Gap remediation tracked
11. Verification conducted post-remediation
12. Trends analyzed (recurring gaps?)
13. Gaps reported to CISO monthly
14. Improvement actions implemented
15. Coverage metrics improving over time

---

## Sheet 7: Summary Dashboard

### Section 1: Overall Coverage Summary (Rows 3-18)
- Total assets in inventory
- Assets monitored / total assets
- % Coverage by criticality (Critical/High/Medium/Low)
- % Coverage by asset type
- Assets without monitoring (count and %)

### Section 2: Network Coverage (Rows 21-30)
- Network segments total
- Segments fully monitored
- Segments partially monitored
- Segments not monitored
- % Coverage by segment type

### Section 3: User/Identity Coverage (Rows 33-42)
- Identity systems total
- Identity systems monitored
- Users covered
- Privileged accounts monitored %

### Section 4: Application Coverage (Rows 45-54)
- Applications total
- Applications monitored
- % Coverage by criticality
- % Coverage by type

### Section 5: Gap Analysis (Rows 57-69)
- Total gaps identified
- Gaps by severity (Critical/High/Medium/Low)
- Open gaps
- In-progress remediations
- Resolved gaps
- Accepted risks
- Overdue remediations

### Section 6: Compliance Summary (Rows 72-82)
| Assessment Area | Compliant | Partial | Non-Compliant | % Compliant |
|-----------------|-----------|---------|---------------|-------------|
| 1. Asset Coverage | Formula | Formula | Formula | Formula |
| 2. Network Coverage | Formula | Formula | Formula | Formula |
| 3. User/Identity Coverage | Formula | Formula | Formula | Formula |
| 4. Application Coverage | Formula | Formula | Formula | Formula |
| 5. Gap Remediation | Formula | Formula | Formula | Formula |
| **OVERALL** | Formula | Formula | Formula | Formula |

---

**END OF SPECIFICATION**

# ISMS-IMP-A.8.16.4 - Alert Management & Response Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.16.4  
**Assessment Area:** Alert Management, Triage, Investigation, Response  
**Related Policy:** ISMS-POL-A.8.16-S2.3  
**Purpose:** Assess alert management processes, response procedures, and SOC operational effectiveness  
**Generator Script:** `generate_a816_4_alert_management.py`  
**Output Filename:** `ISMS-IMP-A.8.16.4_Alert_Management_YYYYMMDD.xlsx`

---

## Workbook Structure

**Total Sheets:** 9
1. Instructions & Legend
2. 1. Alert Generation & Classification
3. 2. Triage & Investigation Processes
4. 3. Escalation & Response Procedures
5. 4. Alert Performance Metrics
6. 5. SOC Operational Readiness
7. Summary Dashboard
8. Evidence Register
9. Approval Sign-Off

---

## Sheet 2: 1. Alert Generation & Classification

### Header
**Title:** "1. ALERT GENERATION & CLASSIFICATION ASSESSMENT"  
**Policy Reference:** "Assess alert generation per ISMS-POL-A.8.16-S2.3.3"

### Column Headers - 22 Columns (A-V)

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | Alert Type/Name | 30 | Text | Free text |
| B | Alert Source | 22 | Dropdown | SIEM, IDS/IPS, EDR, NDR, Firewall, WAF, AV, DLP, Cloud Security, Other |
| C | Detection Rule ID | 20 | Text | Free text |
| D | Alert Severity | 15 | Dropdown | Critical (P1), High (P2), Medium (P3), Low (P4) |
| E | MITRE ATT&CK Technique | 22 | Text | Free text |
| F | Alert Description | 35 | Text | Free text |
| G | Trigger Criteria | 30 | Text | Free text |
| H | Enrichment Data | 30 | Text | Free text (threat intel, asset, user) |
| I | Expected FP Rate | 15 | Text | % |
| J | Actual FP Rate (30d) | 15 | Text | % |
| K | Alert Volume (30d) | 15 | Text | Count |
| L | True Positives (30d) | 15 | Text | Count |
| M | Response Playbook | 22 | Text | Free text (playbook reference) |
| N | SLA Timeframe | 18 | Dropdown | <15 min, <1 hr, <4 hrs, <1 day, <3 days |
| O | Auto-Enrichment | 16 | Dropdown | Yes, Partial, No |
| P | Auto-Containment | 16 | Dropdown | Yes, No, N/A |
| Q | Deduplication Enabled | 18 | Dropdown | Yes, No |
| R | Alert Status | 16 | Dropdown | Active, Testing, Tuning Needed, Retired |
| S | Last Tuned | 14 | Text | DD.MM.YYYY |
| T | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| U | Issues/Gaps | 30 | Text | Free text |
| V | Tuning Priority | 16 | Dropdown | Critical, High, Medium, Low, None |

### Compliance Checklist
1. All alert types documented in inventory
2. Alert severity classification defined and consistent
3. MITRE ATT&CK mapping documented
4. Trigger criteria clearly documented
5. Alert enrichment configured (asset, user, threat intel)
6. Response playbook exists for each alert type
7. SLA timeframes defined per severity
8. False positive rates tracked (<25% overall, <10% critical)
9. High FP alerts tuned within 30 days
10. Alert deduplication configured
11. Auto-containment configured for high-confidence alerts
12. Alert generation tested before production
13. Alert volume monitored for spikes
14. Noisy alerts identified and tuned
15. Retired alerts properly archived

---

## Sheet 3: 2. Triage & Investigation Processes

### Header
**Title:** "2. TRIAGE & INVESTIGATION PROCESS ASSESSMENT"  
**Policy Reference:** "Assess triage per ISMS-POL-A.8.16-S2.3.5"

### Column Headers - 21 Columns (A-U)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Process Step | 28 | Dropdown | Alert Acknowledgment, Initial Assessment, Context Gathering, Disposition Decision, Investigation, Documentation, Escalation, Closure |
| B | Process Owner | 20 | Text |
| C | Procedure Documented | 18 | Dropdown | Yes, No, Partial |
| D | Documentation Location | 25 | Text |
| E | Training Provided | 16 | Dropdown | Yes, No, Planned |
| F | Tools/Systems Used | 25 | Text |
| G | Automation Level | 18 | Dropdown | Fully Automated, Partially Automated, Manual |
| H | Average Time (Minutes) | 18 | Text |
| I | SLA Target (Minutes) | 18 | Text |
| J | SLA Compliance % | 16 | Text |
| K | Bottlenecks Identified | 30 | Text |
| L | Quality Metrics | 25 | Text |
| M | Error Rate % | 12 | Text |
| N | Analyst Workload | 18 | Text | (alerts/shift) |
| O | Shift Coverage | 18 | Dropdown | 24/7, Business Hours, On-Call |
| P | Escalation Criteria | 30 | Text |
| Q | Escalation Rate % | 15 | Text |
| R | Process Status | 16 | Dropdown | ✅ Defined, ⚠️ Partial, ❌ Undefined |
| S | Last Process Review | 14 | Text | DD.MM.YYYY |
| T | Improvement Opportunities | 30 | Text |
| U | Priority | 16 | Dropdown | Critical, High, Medium, Low |

### Compliance Checklist
1. Triage procedure documented
2. Triage steps clearly defined
3. Disposition criteria documented (TP/FP/Benign/Investigation)
4. Triage timeframes defined per severity
5. SOC analysts trained on triage procedures
6. Triage tools accessible to all analysts
7. Context enrichment automated where possible
8. Common false positive scenarios documented
9. Investigation playbooks exist
10. Evidence collection guidance provided
11. Documentation requirements defined
12. Escalation criteria clearly defined
13. Escalation paths documented
14. Process reviewed quarterly
15. Continuous improvement implemented

---

## Sheet 4: 3. Escalation & Response Procedures

### Header
**Title:** "3. ESCALATION & RESPONSE PROCEDURES"  
**Policy Reference:** "Assess escalation per ISMS-POL-A.8.16-S2.3.7"

### Column Headers - 19 Columns (A-S)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Escalation Scenario | 30 | Text |
| B | Trigger Criteria | 30 | Text |
| C | Escalation Level | 20 | Dropdown | Tier 1→Tier 2, Tier 2→Tier 3, SOC→IR, IR→CISO, CISO→Exec, Exec→Board, External |
| D | Target Person/Team | 22 | Text |
| E | Primary Contact | 22 | Text |
| F | Backup Contact | 22 | Text |
| G | Contact Method | 18 | Dropdown | Phone, Email, Ticketing System, Secure Chat, Multiple |
| H | Escalation Timeframe | 16 | Text | e.g., "Within 15 min" |
| I | Information to Provide | 35 | Text |
| J | Expected Response Time | 18 | Text |
| K | Procedure Documented | 18 | Dropdown | Yes, No, Partial |
| L | Tested Frequency | 18 | Dropdown | Quarterly, Semi-Annually, Annually, Never |
| M | Last Tested | 14 | Text | DD.MM.YYYY |
| N | Test Result | 16 | Dropdown | Successful, Issues Found, Not Tested |
| O | After-Hours Procedure | 20 | Dropdown | On-Call, 24/7 SOC, Automated, None |
| P | Escalation Rate (30d) | 16 | Text | % or count |
| Q | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| R | Gaps/Issues | 30 | Text |
| S | Priority | 16 | Dropdown | Critical, High, Medium, Low |

### Compliance Checklist
1. Escalation paths documented for all severity levels
2. Escalation criteria clearly defined
3. Contact information current (verified quarterly)
4. Backup contacts identified
5. After-hours escalation procedures defined
6. On-call rotation established
7. Escalation timeframes defined
8. Information requirements documented (what to escalate)
9. Communication templates available
10. Escalation tracking in place
11. Escalation procedures tested (tabletop exercises)
12. External escalation procedures defined (law enforcement, regulators)
13. Executive escalation criteria defined
14. Escalation metrics tracked
15. False escalations analyzed and reduced

---

## Sheet 5: 4. Alert Performance Metrics

### Header
**Title:** "4. ALERT PERFORMANCE METRICS"  
**Policy Reference:** "Assess metrics per ISMS-POL-A.8.16-S2.3.9"

### Column Headers - 18 Columns (A-R)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Metric Name | 30 | Text |
| B | Metric Category | 22 | Dropdown | Volume, Response Time, Quality, Effectiveness, Workload |
| C | Measurement Method | 25 | Text |
| D | Data Source | 22 | Text |
| E | Current Value | 15 | Text |
| F | Target/SLA | 15 | Text |
| G | Status | 16 | Dropdown | ✅ Meeting Target, ⚠️ Below Target, ❌ Critical |
| H | Trend (30d) | 16 | Dropdown | Improving, Stable, Declining |
| I | Measurement Frequency | 18 | Dropdown | Real-Time, Daily, Weekly, Monthly |
| J | Reporting Frequency | 18 | Dropdown | Daily, Weekly, Monthly, Quarterly |
| K | Reported To | 20 | Text |
| L | Automated Tracking | 18 | Dropdown | Yes, Partial, No |
| M | Dashboard Available | 18 | Dropdown | Yes, No |
| N | Alert on Threshold | 18 | Dropdown | Yes, No |
| O | Last Review | 14 | Text | DD.MM.YYYY |
| P | Action Items | 30 | Text |
| Q | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |
| R | Notes | 25 | Text |

**Key Metrics to Track:**
- Total alerts per day/week/month
- Alerts by severity (Critical/High/Medium/Low)
- True Positive rate (%)
- False Positive rate (%)
- Mean Time To Acknowledge (MTTA)
- Mean Time To Triage (MTTT)
- Mean Time To Investigate (MTTI)
- Mean Time To Resolve (MTTR)
- SLA compliance rate (%)
- Escalation rate (%)
- Alert-to-Incident ratio
- SOC analyst workload (alerts/shift)
- Detection rate (from testing)

### Compliance Checklist
1. Alert volume metrics tracked
2. Response time metrics tracked (MTTA, MTTT, MTTI, MTTR)
3. Quality metrics tracked (TP rate, FP rate)
4. Effectiveness metrics tracked (detection rate)
5. Metrics targets defined
6. Metrics measured consistently
7. Metrics reported to SOC Lead (weekly)
8. Metrics reported to CISO (monthly)
9. Metrics dashboard available
10. Trends analyzed
11. Performance issues identified
12. Improvement actions taken
13. SLA compliance tracked
14. Metrics drive tuning decisions
15. Metrics included in management reporting

---

## Sheet 6: 5. SOC Operational Readiness

### Header
**Title:** "5. SOC OPERATIONAL READINESS ASSESSMENT"  
**Policy Reference:** "Assess SOC operations per ISMS-POL-A.8.16-S3"

### Column Headers - 17 Columns (A-Q)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Readiness Area | 28 | Dropdown | Staffing, Training, Tools, Procedures, Communication, Facilities, Testing, Documentation |
| B | Requirement | 35 | Text |
| C | Current State | 35 | Text |
| D | Status | 18 | Dropdown | ✅ Adequate, ⚠️ Needs Improvement, ❌ Inadequate |
| E | Evidence | 30 | Text |
| F | Gap Description | 30 | Text |
| G | Business Impact | 25 | Text |
| H | Risk Level | 15 | Dropdown | Critical, High, Medium, Low |
| I | Remediation Plan | 30 | Text |
| J | Target Date | 14 | Text | DD.MM.YYYY |
| K | Owner | 20 | Text |
| L | Budget Required | 15 | Dropdown | Yes, No, Unknown |
| M | Dependencies | 25 | Text |
| N | Status | 16 | Dropdown | Complete, In Progress, Planned, Not Started |
| O | Last Updated | 14 | Text | DD.MM.YYYY |
| P | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |
| Q | Notes | 25 | Text |

### Compliance Checklist
**Staffing:**
1. SOC staffing adequate for 24/7 coverage (if required)
2. SOC analyst to alert ratio acceptable (<50 alerts/shift)
3. SOC tiers defined (Tier 1, 2, 3)
4. On-call rotation established
5. Shift handover procedures defined

**Training:**
6. SOC analysts trained on triage procedures
7. SOC analysts trained on investigation playbooks
8. SOC analysts trained on tools (SIEM, EDR, etc.)
9. Training records maintained
10. Quarterly training refreshers conducted

**Tools & Systems:**
11. All required tools accessible to SOC
12. Tool access tested and functional
13. Tool documentation available
14. Tool integrations working
15. Communication systems functional (ticketing, chat, email)

**Procedures:**
16. SOC procedures documented
17. Playbooks available for common alert types
18. Escalation procedures documented
19. Shift handover checklists available
20. Standard operating procedures (SOPs) updated

**Testing:**
21. Tabletop exercises conducted quarterly
22. Alert response tested (red team, purple team)
23. Escalation procedures tested
24. Communication systems tested
25. Disaster recovery procedures tested

---

## Sheet 7: Summary Dashboard

### Section 1: Alert Management Summary (Rows 3-18)
- Total alerts (last 30 days)
- Alerts by severity breakdown
- True Positive rate % (target >20%)
- False Positive rate % (target <25%)
- Alert-to-Incident ratio
- Noisy alerts requiring tuning (count)

### Section 2: Response Time Performance (Rows 21-35)
- MTTA (Mean Time To Acknowledge)
  - Critical: Current vs. Target (<15 min)
  - High: Current vs. Target (<1 hr)
- MTTT (Mean Time To Triage)
  - Critical: Current vs. Target (<1 hr)
  - High: Current vs. Target (<4 hrs)
- MTTI (Mean Time To Investigate)
- MTTR (Mean Time To Resolve)
- SLA compliance rate % (target >95%)

### Section 3: Escalation Metrics (Rows 38-48)
- Escalations to Tier 2 (count, %)
- Escalations to IR (count, %)
- Escalations to CISO (count)
- Escalation rate by severity
- False escalation rate %

### Section 4: SOC Operational Health (Rows 51-63)
- SOC analyst count (current/required)
- Coverage model (24/7, business hours, hybrid)
- Average alerts per shift
- Analyst workload status
- Training completion %
- Tool availability %
- Procedure documentation complete %

### Section 5: Compliance Summary (Rows 66-76)
| Assessment Area | Total | Compliant | Partial | Non-Compliant | % |
|-----------------|-------|-----------|---------|---------------|---|
| 1. Alert Generation | Formula | Formula | Formula | Formula | Formula |
| 2. Triage & Investigation | Formula | Formula | Formula | Formula | Formula |
| 3. Escalation & Response | Formula | Formula | Formula | Formula | Formula |
| 4. Performance Metrics | Formula | Formula | Formula | Formula | Formula |
| 5. SOC Readiness | Formula | Formula | Formula | Formula | Formula |
| **OVERALL** | Formula | Formula | Formula | Formula | Formula |

### Section 6: Critical Issues (Rows 79-87)
- Priority | Issue | Impact | Target Date | Owner | Status

---

**END OF SPECIFICATION**

# ISMS-IMP-A.8.16.5 - Compliance Dashboard Specification
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.16.5  
**Assessment Area:** Overall Compliance Dashboard & Master Metrics  
**Related Policy:** All ISMS-POL-A.8.16 sections  
**Purpose:** Consolidated compliance dashboard aggregating all monitoring activity assessments  
**Generator Script:** `generate_a816_5_compliance_dashboard.py`  
**Output Filename:** `ISMS-IMP-A.8.16.5_Compliance_Dashboard_YYYYMMDD.xlsx`

---

## Workbook Structure

**Total Sheets:** 7
1. Instructions & Legend
2. Executive Summary
3. Detailed Compliance Matrix
4. Key Performance Indicators (KPIs)
5. Gap Analysis & Remediation Tracker
6. Trend Analysis
7. Evidence Register & Approvals

---

## Sheet 2: Executive Summary

### Header
**Title:** "MONITORING ACTIVITIES - EXECUTIVE SUMMARY"  
**Subtitle:** "ISO/IEC 27001:2022 Control A.8.16 Compliance Status"

### Section 1: Overall Compliance Score (Rows 3-12)

**Visual Compliance Gauge:**
```
Overall Compliance:  [XX%] ■■■■■■■■□□ 
Status:              [✅ Compliant / ⚠️ Partial / ❌ Non-Compliant]
Assessment Date:     DD.MM.YYYY
Next Review:         DD.MM.YYYY
```

**Compliance by Assessment Area:**
| Assessment | Domain | Compliance % | Status | Trend |
|------------|--------|--------------|--------|-------|
| IMP-A.8.16.1 | Infrastructure | Formula | Formula | ↑/→/↓ |
| IMP-A.8.16.2 | Baseline & Detection | Formula | Formula | ↑/→/↓ |
| IMP-A.8.16.3 | Coverage | Formula | Formula | ↑/→/↓ |
| IMP-A.8.16.4 | Alert Management | Formula | Formula | ↑/→/↓ |
| **OVERALL** | **All Domains** | **Formula** | **Formula** | **↑/→/↓** |

### Section 2: Critical Metrics Summary (Rows 16-30)

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| **Coverage Metrics** |
| Critical Systems Monitored | Formula | 100% | Formula |
| Overall System Coverage | Formula | >80% | Formula |
| Network Segment Coverage | Formula | 100% | Formula |
| **Detection Metrics** |
| Baseline Coverage (Critical) | Formula | 100% | Formula |
| Detection Rate | Formula | >90% | Formula |
| False Positive Rate | Formula | <25% | Formula |
| **Response Metrics** |
| MTTD (Critical Alerts) | Formula | <5 min | Formula |
| MTTR (Critical Incidents) | Formula | <8 hrs | Formula |
| SLA Compliance | Formula | >95% | Formula |
| **Operational Metrics** |
| Log Sources Integrated | Formula | Target | Formula |
| Active Detection Rules | Formula | Target | Formula |
| SOC Analyst Coverage | Formula | 24/7 | Formula |

### Section 3: Top 5 Strengths (Rows 34-42)
| Rank | Strength | Evidence |
|------|----------|----------|
| 1 | [Auto-populated from assessments] | [Link to evidence] |
| 2 | ... | ... |

### Section 4: Top 5 Gaps (Rows 45-53)
| Priority | Gap | Risk | Remediation Target |
|----------|-----|------|-------------------|
| Critical | [Auto-populated] | High | DD.MM.YYYY |

### Section 5: Management Recommendations (Rows 56-68)
- Investment priorities
- Resource needs
- Strategic improvements
- Compliance actions

---

## Sheet 3: Detailed Compliance Matrix

### Header
**Title:** "DETAILED COMPLIANCE MATRIX"

### Matrix Structure (Rows 3-150)

**Column Headers:**
| Col | Header | Width |
|-----|--------|-------|
| A | Policy Reference | 25 |
| B | Requirement | 40 |
| C | Control Type | 18 |
| D | Assessment Sheet | 22 |
| E | Evidence Location | 30 |
| F | Implementation Status | 20 |
| G | Compliance Status | 20 |
| H | Gap Description | 35 |
| I | Risk Level | 15 |
| J | Remediation Owner | 20 |
| K | Target Date | 14 |
| L | Notes | 25 |

**Requirements Mapped:**
- All requirements from S2.1 (Infrastructure) - ~25 requirements
- All requirements from S2.2 (Baseline & Detection) - ~30 requirements
- All requirements from S2.3 (Alert Management) - ~25 requirements
- All requirements from S2.4 (Retention) - ~15 requirements
- All requirements from S3 (Roles) - ~10 requirements
- **Total: ~105 requirement rows**

**Auto-Population from Assessment Workbooks:**
- Import compliance status from IMP-A.8.16.1 through IMP-A.8.16.4
- Aggregate to policy requirement level
- Flag gaps and non-compliance

### Compliance Scoring (Formula-driven)
```
Compliant Count: =COUNTIF(G:G,"✅ Compliant")
Partial Count: =COUNTIF(G:G,"⚠️ Partial")
Non-Compliant Count: =COUNTIF(G:G,"❌ Non-Compliant")
Overall %: =Compliant/(Compliant+Partial+Non-Compliant)*100
```

---

## Sheet 4: Key Performance Indicators (KPIs)

### Section 1: Coverage KPIs (Rows 3-20)

| KPI | Current | Target | Baseline | Trend (3mo) | Status |
|-----|---------|--------|----------|-------------|--------|
| **Asset Coverage** |
| Critical Systems Monitored % | [Input] | 100% | [Historical] | Chart | Status |
| High Priority Systems % | [Input] | >80% | [Historical] | Chart | Status |
| Overall Asset Coverage % | [Input] | >80% | [Historical] | Chart | Status |
| Network Segments Covered % | [Input] | 100% | [Historical] | Chart | Status |
| **Log Source Integration** |
| Log Sources Integrated (Count) | [Input] | Target | [Historical] | Chart | Status |
| Log Volume (GB/day) | [Input] | Capacity | [Historical] | Chart | Status |
| Log Collection Reliability % | [Input] | >99% | [Historical] | Chart | Status |

### Section 2: Detection KPIs (Rows 23-42)

| KPI | Current | Target | Baseline | Trend | Status |
|-----|---------|--------|----------|-------|--------|
| **Baseline Metrics** |
| Tier 1 Systems with Baselines % | [Input] | 100% | [Historical] | Chart | Status |
| Tier 2 Systems with Baselines % | [Input] | >80% | [Historical] | Chart | Status |
| Baseline Staleness (Avg Days Since Review) | [Input] | <90 | [Historical] | Chart | Status |
| **Detection Rule Health** |
| Active Detection Rules (Count) | [Input] | Target | [Historical] | Chart | Status |
| MITRE ATT&CK Coverage % | [Input] | >60% | [Historical] | Chart | Status |
| Detection Rate (Testing) % | [Input] | >90% | [Historical] | Chart | Status |
| False Positive Rate % | [Input] | <25% | [Historical] | Chart | Status |
| Rules Requiring Tuning (Count) | [Input] | <10 | [Historical] | Chart | Status |

### Section 3: Response KPIs (Rows 45-65)

| KPI | Current | Target | Baseline | Trend | Status |
|-----|---------|--------|----------|-------|--------|
| **Alert Metrics** |
| Total Alerts (30d) | [Input] | Target | [Historical] | Chart | Status |
| Alerts by Severity (Critical/High/Med/Low) | [Input] | Profile | [Historical] | Chart | Status |
| True Positive Rate % | [Input] | >20% | [Historical] | Chart | Status |
| Alert-to-Incident Ratio | [Input] | Target | [Historical] | Chart | Status |
| **Response Time Metrics** |
| MTTA - Critical (minutes) | [Input] | <15 | [Historical] | Chart | Status |
| MTTT - Critical (minutes) | [Input] | <60 | [Historical] | Chart | Status |
| MTTI - Critical (hours) | [Input] | <4 | [Historical] | Chart | Status |
| MTTR - Critical (hours) | [Input] | <8 | [Historical] | Chart | Status |
| SLA Compliance Rate % | [Input] | >95% | [Historical] | Chart | Status |
| **Escalation Metrics** |
| Escalation Rate % | [Input] | Target | [Historical] | Chart | Status |
| False Escalation Rate % | [Input] | <10% | [Historical] | Chart | Status |

### Section 4: Operational KPIs (Rows 68-85)

| KPI | Current | Target | Baseline | Trend | Status |
|-----|---------|--------|----------|-------|--------|
| **SOC Operations** |
| SOC Analyst Count | [Input] | Target | [Historical] | Chart | Status |
| Alerts per Analyst per Shift | [Input] | <50 | [Historical] | Chart | Status |
| SOC Coverage Model | [Input] | 24/7 | N/A | N/A | Status |
| Training Completion % | [Input] | 100% | [Historical] | Chart | Status |
| **Infrastructure Health** |
| SIEM Availability % | [Input] | >99.5% | [Historical] | Chart | Status |
| Search Performance (seconds) | [Input] | <10 | [Historical] | Chart | Status |
| Storage Utilization % | [Input] | <80% | [Historical] | Chart | Status |
| Indexing Lag (minutes) | [Input] | <5 | [Historical] | Chart | Status |

---

## Sheet 5: Gap Analysis & Remediation Tracker

### Section 1: Gap Inventory (Rows 3-60)

| Gap ID | Source Assessment | Gap Category | Description | Risk | Impact | Remediation Plan | Owner | Target Date | Budget | Status | % Complete | Last Updated |
|--------|-------------------|--------------|-------------|------|--------|------------------|-------|-------------|--------|--------|------------|--------------|
| [Auto-populated from IMP-A.8.16.1-4] | | | | | | | | | | | | |

**Gap Categories:**
- Infrastructure Gap
- Baseline Gap
- Coverage Gap
- Detection Gap
- Alert Management Gap
- Process Gap
- Resource Gap

### Section 2: Gap Summary by Category (Rows 63-75)
| Category | Total | Critical | High | Medium | Low | Open | In Progress | Resolved |
|----------|-------|----------|------|--------|-----|------|-------------|----------|
| Infrastructure | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| Baseline & Detection | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| Coverage | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| Alert Management | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| **TOTAL** | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |

### Section 3: Remediation Timeline (Rows 78-95)
- Gantt chart style timeline
- Gaps by month
- Critical path items highlighted
- Resource allocation

### Section 4: Risk Heat Map (Rows 98-110)
```
                Impact
            Low  Med  High
Likelihood:
High        [Count gaps by quadrant]
Med         
Low         
```

---

## Sheet 6: Trend Analysis

### Section 1: Compliance Trend (Rows 3-18)
**Monthly compliance % over 12 months**
| Month | Overall % | Infrastructure % | Baseline % | Coverage % | Alert Mgmt % |
|-------|-----------|------------------|------------|-----------|--------------|
| Jan 2025 | [Historical] | ... | ... | ... | ... |
| ... | | | | | |
| Dec 2025 | [Current] | ... | ... | ... | ... |

**Line chart showing trends**

### Section 2: KPI Trends (Rows 21-45)
**Key metrics over time (12 months):**
- Critical system coverage %
- Detection rate %
- False positive rate %
- MTTD (Critical)
- MTTR (Critical)
- SLA compliance %

### Section 3: Gap Closure Rate (Rows 48-60)
**Monthly gap remediation tracking:**
| Month | New Gaps | Closed Gaps | Net Change | Total Open |
|-------|----------|-------------|------------|------------|
| ... | | | | |

### Section 4: Incident Detection Effectiveness (Rows 63-75)
**Quarterly analysis:**
| Quarter | Incidents Detected by Monitoring | Incidents Missed | Detection Rate % | Lessons Learned |
|---------|----------------------------------|------------------|------------------|-----------------|
| ... | | | | |

---

## Sheet 7: Evidence Register & Approvals

### Section 1: Evidence Register (Rows 3-102)
**100 rows for evidence tracking**

| Evidence ID | Evidence Type | Description | Related Requirement | Source Assessment | Date Collected | Collected By | Location/Link | Verification Status | Verified By | Verification Date | Notes |
|-------------|---------------|-------------|-------------------|-------------------|----------------|--------------|---------------|-------------------|-------------|------------------|-------|

### Section 2: Approval Workflow (Rows 105-130)

**Assessment Prepared By:**
- Name: [Input]
- Title: [Input]
- Date: [Input]
- Signature: [Space for signature]

**Reviewed By (SOC Lead):**
- Name: [Input]
- Title: [Input]
- Review Comments: [Multi-line text]
- Date: [Input]
- Signature: [Space]

**Reviewed By (Security Engineering):**
- Name: [Input]
- Title: [Input]
- Review Comments: [Multi-line text]
- Date: [Input]
- Signature: [Space]

**Approved By (CISO):**
- Name: [Input]
- Title: [Input]
- Approval Decision: [Dropdown: Approved, Approved with Conditions, Rejected]
- Conditions/Comments: [Multi-line text]
- Date: [Input]
- Signature: [Space]

**Executive Acknowledgment (Optional):**
- Name: [Input]
- Title: [Input]
- Date: [Input]
- Signature: [Space]

---

## Data Import Instructions

**This workbook is designed to aggregate data from:**
- ISMS-IMP-A.8.16.1_Monitoring_Infrastructure_YYYYMMDD.xlsx
- ISMS-IMP-A.8.16.2_Baseline_Detection_YYYYMMDD.xlsx
- ISMS-IMP-A.8.16.3_Coverage_Assessment_YYYYMMDD.xlsx
- ISMS-IMP-A.8.16.4_Alert_Management_YYYYMMDD.xlsx

**Import Method:**
1. Manual copy-paste from Summary Dashboards
2. Excel Power Query (recommended for automation)
3. Python script to aggregate (advanced)

**Formula References:**
- Use INDIRECT() for dynamic workbook references
- Use INDEX/MATCH for lookups across workbooks
- Implement data validation to prevent manual errors

---

**END OF SPECIFICATION**