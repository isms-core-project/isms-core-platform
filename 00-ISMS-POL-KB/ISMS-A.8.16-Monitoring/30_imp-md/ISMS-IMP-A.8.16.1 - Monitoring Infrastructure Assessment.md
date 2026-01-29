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