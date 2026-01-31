# ISMS-IMP-A.8.15.2 - Log Collection & Centralization Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.15 - Logging

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.15.2  
**Assessment Area:** Log Collection Infrastructure and SIEM Integration  
**Related Policy:** ISMS-POL-A.8.15-S2.1 (Event Logging), S2.2 (Protection)  
**Purpose:** Assess centralized logging infrastructure and collection reliability  
**Python Generator:** `generate_a815_2_log_collection_centralization.py`  
**Target Audience:** Log Administrators, SOC Team, IT Operations, Infrastructure Team

---

## Workbook Structure Overview

**Total Sheets:** 12  
**Estimated Rows:** ~700 (varies by infrastructure size)  
**Estimated Completion Time:** 6-10 hours  
**Review Cycle:** Annual (full), Quarterly (metrics update)

### Sheet List
1. Instructions & Legend
2. SIEM Platform Details
3. Log Forwarder Inventory
4. Collection Reliability
5. Integration Architecture
6. SIEM Storage & Capacity
7. Log Parsing & Normalization
8. SIEM Performance Metrics
9. Data Quality Assessment
10. Gap Analysis & Remediation
11. Summary Dashboard
12. Approval & Sign-Off

---

## Sheet 1: Instructions & Legend

### Header Section
**Main Title:** "Log Collection & Centralization Assessment"  
**Subtitle:** "ISO/IEC 27001:2022 - Control A.8.15: Logging"  
**Styling:** Dark blue header (003366), white text, 14pt bold, centered, 40px height

### Document Information Block (Rows 3-11)

| Field | Value | Cell Color |
|-------|-------|------------|
| Document ID | ISMS-IMP-A.8.15.2 | Gray (info) |
| Assessment Area | Log Collection & Centralization | Gray (info) |
| Related Policy | ISMS-POL-A.8.15-S2.1, S2.2 | Gray (info) |
| Version | 1.0 | Gray (info) |
| Assessment Date | [USER INPUT] | Yellow (input) |
| Completed By | [USER INPUT] | Yellow (input) |
| Organization | [USER INPUT] | Yellow (input) |
| Review Cycle | Annual (full), Quarterly (metrics) | Gray (info) |

### How to Use This Workbook (Rows 13-25)

1. Document SIEM/log management platform details
2. Catalog all log forwarders and collectors
3. Assess collection reliability and performance
4. Document integration architecture
5. Review capacity and scalability
6. Identify collection gaps and failures
7. Review Summary Dashboard for overall health
8. Document gaps and remediation plans
9. Obtain approvals

### Legend (Rows 27-37)
Same as IMP-A.8.15.1 (Yellow=Input, Green=Compliant, Red=Non-Compliant, Gray=Calculated, Blue=Headers)

### Key Definitions (Rows 39-55)

| Term | Definition |
|------|------------|
| **SIEM** | Security Information and Event Management platform |
| **Log Forwarder** | Agent that collects and forwards logs (Splunk UF, Fluentd, etc.) |
| **Indexer** | SIEM component that processes and stores logs |
| **Search Head** | SIEM component for querying logs |
| **Collection Reliability** | % of expected logs successfully received |
| **Parse Success Rate** | % of logs successfully parsed into fields |
| **Indexing Lag** | Time delay between log generation and searchability |
| **Hot/Warm/Cold Storage** | Tiered storage based on age and access frequency |
| **Event Rate** | Logs received per second (EPS) |
| **Data Quality** | Completeness, accuracy, and consistency of log data |

---

## Sheet 2: SIEM Platform Details

### Purpose
Document centralized log management platform architecture and components.

### Column Structure (14 columns: A-N)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Platform Component | 25 | Dropdown: SIEM Core, Indexer, Search Head, Forwarder Management, Storage, API Gateway, Other |
| B | Product/Vendor | 25 | Dropdown: Splunk, QRadar, Sentinel, LogRhythm, ELK Stack, Graylog, Custom, Other |
| C | Version | 15 | Text |
| D | Hostname/FQDN | 30 | Text |
| E | IP Address | 15 | Text |
| F | Role | 20 | Dropdown: Primary, Secondary, DR, Dev/Test |
| G | OS/Platform | 20 | Text |
| H | CPU Cores | 10 | Number |
| I | Memory (GB) | 15 | Number |
| J | Storage Capacity (TB) | 20 | Number |
| K | Storage Used (TB) | 20 | Number |
| L | Storage % Used | 15 | Formula: =K/J*100 |
| M | Availability | 15 | Dropdown: Active, Standby, Offline, Degraded |
| N | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers and instructions
- **Row 8:** Example data (gray italic)
- **Rows 9-30:** Data entry (22 rows for SIEM components)

### Example Data (Row 8)
```
SIEM Core | Splunk Enterprise | 9.1.3 | siem-core-01.example.com | 10.10.1.10 | Primary | 
Red Hat Linux | 32 | 256 | 50 | 32 | 64% | Active | Primary indexer cluster node
```

---

## Sheet 3: Log Forwarder Inventory

### Purpose
Catalog all log forwarders/collectors deployed across infrastructure.

### Column Structure (18 columns: A-R)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Forwarder ID | 15 | Auto: FWD-001, FWD-002 |
| B | Forwarder Type | 20 | Dropdown: Splunk UF, Fluentd, Logstash, rsyslog, syslog-ng, Filebeat, Winlogbeat, Windows Event Forwarder, Cloud Connector, Other |
| C | Version | 12 | Text |
| D | Installed On System | 30 | Text (links to IMP-1 System ID) |
| E | System Hostname | 30 | Text |
| F | Destination SIEM | 25 | Dropdown: Primary, Secondary, Both, Load Balanced |
| G | Transport Protocol | 18 | Dropdown: Syslog/TLS, Syslog/TCP, Syslog/UDP, HTTPS, gRPC, Proprietary |
| H | Port | 10 | Number |
| I | Encryption | 15 | Dropdown: Yes (TLS 1.3), Yes (TLS 1.2), No, N/A |
| J | Buffer Enabled | 15 | Dropdown: Yes, No |
| K | Buffer Size (MB) | 18 | Number |
| L | Install Date | 15 | Date: DD.MM.YYYY |
| M | Last Updated | 15 | Date: DD.MM.YYYY |
| N | Status | 15 | Dropdown: Running, Stopped, Error, Unknown |
| O | Events/Day | 20 | Number: Estimated forwarding rate |
| P | Data/Day (MB) | 20 | Number |
| Q | Last Health Check | 15 | Date: DD.MM.YYYY |
| R | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers and instructions
- **Row 8:** Example data
- **Rows 9-200:** Data entry (192 rows - one per system with forwarder)

### Formula
**Column A (Forwarder ID):**
```excel
=IF(B2<>"","FWD-"&TEXT(ROW()-8,"000"),"")
```

---

## Sheet 4: Collection Reliability

### Purpose
Track log collection reliability metrics over assessment period (last 30 days).

### Column Structure (16 columns: A-P)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Source System ID | 15 | Dropdown (from IMP-1) |
| B | Source System Name | 30 | Formula: VLOOKUP |
| C | Expected Events/Day | 20 | Number: Baseline |
| D | Actual Events/Day (Current) | 20 | Number: Current week avg |
| E | Collection Rate % | 18 | Formula: =D/C*100 |
| F | Status | 15 | Formula: >95%=Green, >80%=Yellow, <80%=Red |
| G | Last Event Received | 18 | Datetime: DD.MM.YYYY HH:MM |
| H | Gap Detected | 15 | Dropdown: Yes, No |
| I | Gap Start Time | 18 | Datetime (if gap) |
| J | Gap End Time | 18 | Datetime (if gap) |
| K | Gap Duration (hours) | 20 | Formula: =(J-I)*24 |
| L | Gap Reason | 30 | Dropdown: Network Issue, Forwarder Down, Source Down, SIEM Issue, Configuration Error, Unknown |
| M | Resolution Actions | 40 | Text |
| N | Resolved By | 20 | Text: Name |
| O | Resolved Date | 15 | Date: DD.MM.YYYY |
| P | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-200:** Data entry (monitoring period: last 30 days)

### Key Formulas
**Collection Rate % (Column E):**
```excel
=IF(C2=0,0,D2/C2*100)
```

**Status (Column F):**
```excel
=IF(E2>=95,"Compliant",IF(E2>=80,"Partial","Non-Compliant"))
```

**Gap Duration (Column K):**
```excel
=IF(AND(I2<>"",J2<>""),(J2-I2)*24,"")
```

### Auto-Alert Logic
Flag systems with:
- Collection rate <95%
- Gaps >4 hours
- No events received in last 24 hours

---

## Sheet 5: Integration Architecture

### Purpose
Document log flow architecture and integration points.

### Column Structure (14 columns: A-N)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Integration Point | 25 | Text: Source → Destination |
| B | Source Type | 20 | Dropdown: Server, Network Device, Application, Cloud Service, Security Tool, Container, Other |
| C | Source Count | 15 | Number: How many sources |
| D | Collection Method | 25 | Dropdown: Agent-based, Agentless/Syslog, API Pull, API Push, File Collection, Stream Processing |
| E | Intermediate Hops | 20 | Number: 0=direct, 1+=via concentrator |
| F | Network Path | 30 | Text: Describe routing |
| G | Bandwidth Required | 20 | Text: Mbps estimate |
| H | Latency Target | 15 | Text: <1 min, <5 min, etc. |
| I | Current Latency | 15 | Text: Actual measured |
| J | Redundancy | 15 | Dropdown: None, Active/Passive, Active/Active |
| K | Single Point of Failure | 20 | Dropdown: Yes, No, Mitigated |
| L | DR Capability | 15 | Dropdown: Yes, No, Partial |
| M | Bottleneck Risk | 15 | Dropdown: High, Medium, Low, None |
| N | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-50:** Data entry (integration patterns)

### Additional Content
**Architecture Diagram Placeholder** (Row 55+):
- Reserved space for architecture diagram
- Instructions to embed or link to Visio/draw.io diagram
- Shows complete log flow from sources → forwarders → SIEM → storage

---

## Sheet 6: SIEM Storage & Capacity

### Purpose
Assess storage capacity, growth trends, and capacity planning.

### Column Structure (15 columns: A-O)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Storage Component | 25 | Dropdown: Hot Storage, Warm Storage, Cold Storage, Archive, Backup |
| B | Technology | 20 | Dropdown: Local Disk/SSD, SAN, NAS, Object Storage (S3/Azure), Tape, Cloud, Other |
| C | Total Capacity (TB) | 20 | Number |
| D | Used Capacity (TB) | 20 | Number |
| E | Free Capacity (TB) | 20 | Formula: =C-D |
| F | % Used | 12 | Formula: =D/C*100 |
| G | Status | 15 | Formula: >85%=Red, >70%=Yellow, <70%=Green |
| H | Retention Period | 20 | Text: Days/months stored here |
| I | Avg Daily Ingest (GB) | 20 | Number |
| J | Growth Rate %/Month | 20 | Number: Historical trend |
| K | Days Until Full | 15 | Formula: =(E*1024)/I |
| L | Expansion Plan | 30 | Dropdown: Not Needed, Planned, In Progress, Urgent |
| M | Expansion Date | 15 | Date: When capacity added |
| N | Cost per TB/Month | 20 | Number: For budgeting |
| O | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-20:** Data entry (storage tiers)

### Capacity Planning Section (Rows 25-40)

**Summary Metrics:**
- Current total capacity across all tiers
- Projected capacity need (6 months, 12 months, 24 months)
- Budget required for expansion
- Optimization opportunities (compression, tiering, archival, retention tuning)

**Capacity Planning Table:**

| Timeframe | Projected Ingest (TB) | Capacity Needed (TB) | Gap (TB) | Estimated Cost |
|-----------|-----------------------|----------------------|----------|----------------|
| Current | [Calculated] | [Current] | N/A | N/A |
| 6 months | [Formula] | [Formula] | [Formula] | [Input] |
| 12 months | [Formula] | [Formula] | [Formula] | [Input] |
| 24 months | [Formula] | [Formula] | [Formula] | [Input] |

---

## Sheet 7: Log Parsing & Normalization

### Purpose
Assess parsing accuracy, field extraction, and data normalization.

### Column Structure (15 columns: A-O)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Log Source Type | 25 | Text: Windows, Linux, Firewall, etc. |
| B | Log Format | 20 | Dropdown: Syslog, CEF, JSON, EVTX, LEEF, Custom |
| C | Parsing Method | 20 | Dropdown: Built-in, Custom Regex, Grok, Logstash Filter, Custom Script, ML-based |
| D | Parser Status | 15 | Dropdown: Working, Needs Tuning, Broken, Not Configured |
| E | Parse Success Rate % | 20 | Number: 0-100 |
| F | Unparsed Events/Day | 20 | Number |
| G | Fields Extracted | 20 | Number: How many fields |
| H | Required Fields Present | 20 | Dropdown: All, Most, Some, Few, None |
| I | Timestamp Parsing | 18 | Dropdown: Correct, Incorrect, Missing |
| J | Timezone Handling | 18 | Dropdown: Correct, Incorrect, Unknown |
| K | Last Parser Update | 15 | Date: DD.MM.YYYY |
| L | Issues Identified | 40 | Text |
| M | Tuning Required | 15 | Dropdown: Yes, No |
| N | Owner | 20 | Text: Responsible for parser |
| O | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-100:** Data entry (log source types)

### Target Metrics
- Parse success rate: >95% for all sources
- Required fields: "All" or "Most"
- Timestamp parsing: "Correct"
- Unparsed events: Minimize (ideally <5% of daily volume)

---

## Sheet 8: SIEM Performance Metrics

### Purpose
Track SIEM platform performance over assessment period.

### Column Structure (14 columns: A-N)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Metric Date | 15 | Date: DD.MM.YYYY |
| B | Daily Events Indexed | 20 | Number: Total events |
| C | Peak Events/Second | 20 | Number: EPS |
| D | Indexing Lag (minutes) | 20 | Number: Real-time vs. indexed |
| E | Search Performance (sec) | 20 | Number: Avg query time |
| F | Dashboard Load Time (sec) | 20 | Number |
| G | CPU Utilization % | 18 | Number: 0-100 |
| H | Memory Utilization % | 18 | Number: 0-100 |
| I | Disk I/O % | 15 | Number: 0-100 |
| J | Network Throughput (Gbps) | 20 | Number |
| K | Uptime % | 12 | Number: 99.9+ target |
| L | Incidents | 15 | Number: Outages/issues |
| M | Performance Status | 18 | Formula: Green if all healthy |
| N | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-90:** Data entry (daily metrics for 30-90 days)

### Performance Targets

| Metric | Target | Status Condition |
|--------|--------|------------------|
| Indexing lag | <5 minutes | Green: ≤5, Yellow: 5-15, Red: >15 |
| Search performance | <10 seconds | Green: ≤10, Yellow: 10-30, Red: >30 |
| CPU/Memory utilization | <80% | Green: <80%, Yellow: 80-90%, Red: >90% |
| Uptime | >99.9% | Green: ≥99.9%, Yellow: 99-99.9%, Red: <99% |

### Summary Section (Rows 95-105)

**Average Performance (Last 30 Days):**
- Avg daily events indexed
- Avg peak EPS
- Avg indexing lag
- Avg search performance
- Avg uptime %
- Total incidents

---

## Sheet 9: Data Quality Assessment

### Purpose
Assess quality of log data in SIEM (completeness, accuracy, consistency).

### Column Structure (14 columns: A-N)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Quality Dimension | 25 | Dropdown: Completeness, Accuracy, Consistency, Timeliness, Validity |
| B | Log Source Type | 25 | Text |
| C | Assessment Method | 30 | Text: How measured |
| D | Sample Size | 15 | Number: Events checked |
| E | Pass Count | 15 | Number |
| F | Fail Count | 15 | Number |
| G | Quality Score % | 18 | Formula: =E/(E+F)*100 |
| H | Status | 15 | Formula: >95%=Green, >80%=Yellow, <80%=Red |
| I | Common Issues | 40 | Text: What problems found |
| J | Impact | 20 | Dropdown: Critical, High, Medium, Low |
| K | Remediation Action | 40 | Text |
| L | Responsible Party | 25 | Text |
| M | Target Date | 15 | Date: DD.MM.YYYY |
| N | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-50:** Data entry (quality checks)

### Quality Dimensions Explained

**Completeness:** All required fields present in logs
- Example check: Do all authentication logs have user_id, timestamp, source_ip?

**Accuracy:** Data values correct and meaningful
- Example check: Are timestamps within reasonable range? Are IP addresses valid?

**Consistency:** Same events logged same way across sources
- Example check: Do all Windows servers log authentication the same way?

**Timeliness:** Logs indexed within target timeframe
- Example check: Are logs searchable within 5 minutes of generation?

**Validity:** Data conforms to expected formats
- Example check: Do email addresses match format? Are status codes valid?

---

## Sheet 10: Gap Analysis & Remediation

### Purpose
Track collection infrastructure gaps and remediation.

### Column Structure (12 columns: A-L)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Gap ID | 12 | Auto: GAP-001 |
| B | Gap Category | 25 | Dropdown: Coverage Gap, Reliability Issue, Performance Issue, Parsing Error, Capacity Constraint, Redundancy Gap, DR Gap, Data Quality Issue |
| C | Description | 50 | Text |
| D | Affected Systems | 30 | Text: Count or list |
| E | Impact | 20 | Dropdown: Critical, High, Medium, Low |
| F | Current State | 40 | Text |
| G | Target State | 40 | Text |
| H | Remediation Action | 50 | Text |
| I | Owner | 25 | Text |
| J | Target Date | 15 | Date: DD.MM.YYYY |
| K | Status | 15 | Dropdown: Open, In Progress, Resolved, Deferred |
| L | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers
- **Row 8:** Example
- **Rows 9-100:** Data entry (gaps)

### Gap Categories Defined

- **Coverage Gap:** Systems not sending logs to SIEM
- **Reliability Issue:** Collection rate <95%
- **Performance Issue:** Indexing lag, slow searches
- **Parsing Error:** High unparsed event rate
- **Capacity Constraint:** Storage running out
- **Redundancy Gap:** Single points of failure
- **DR Gap:** No disaster recovery capability
- **Data Quality Issue:** Incomplete, inaccurate, or inconsistent data

---

## Sheet 11: Summary Dashboard

### Purpose
Executive summary of log collection health and compliance.

### Section 1: Collection Health Summary (Rows 3-12)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Systems Monitored | =COUNT formula | N/A | Info |
| Systems Collecting >95% | =COUNTIF formula | 100% | Green/Yellow/Red |
| Avg Collection Rate % | =AVERAGE formula | >98% | Status |
| Systems with Gaps >4hr | =COUNT formula | 0 | Status |
| Parse Success Rate % | =AVERAGE formula | >95% | Status |
| SIEM Uptime % | From Sheet 8 | >99.9% | Status |
| Storage Used % | From Sheet 6 | <70% | Status |
| Days Until Storage Full | =MIN formula | >90 days | Status |

### Section 2: Collection by System Type (Rows 14-24)
Bar chart showing collection rates by system type (Server, Network, Security, Application, Cloud)

| System Type | Total | Collecting >95% | Avg Collection Rate % |
|-------------|-------|-----------------|----------------------|
| Server | COUNT | COUNTIF | AVERAGE |
| Network Device | COUNT | COUNTIF | AVERAGE |
| Security Appliance | COUNT | COUNTIF | AVERAGE |
| Application | COUNT | COUNTIF | AVERAGE |
| Cloud Service | COUNT | COUNTIF | AVERAGE |

### Section 3: Performance Trends (Rows 26-40)
Line chart: Daily events indexed over time (last 30 days)

### Section 4: Top Issues (Rows 42-55)
- Top 10 systems with lowest collection rates
- Top 10 parsing errors by volume
- Top 5 capacity constraints

### Section 5: Gap Summary (Rows 57-65)

| Priority | Open | In Progress | Resolved | Overdue |
|----------|------|-------------|----------|---------|
| Critical | COUNT | COUNT | COUNT | COUNT |
| High | COUNT | COUNT | COUNT | COUNT |
| Medium | COUNT | COUNT | COUNT | COUNT |
| Low | COUNT | COUNT | COUNT | COUNT |

### Section 6: Recommendations (Rows 67-80)

Pre-populated based on assessment findings:
1. If collection rate <98% → "Investigate and resolve collection gaps"
2. If storage >70% → "Plan storage expansion within 90 days"
3. If parse rate <95% → "Tune parsers for improved field extraction"
4. If uptime <99.9% → "Implement SIEM redundancy/HA"
5. If critical gaps exist → "Prioritize critical gap remediation within 30 days"

---

## Sheet 12: Approval & Sign-Off

### Purpose
Document assessment approval workflow.

### Approval Table (Rows 3-12)

| Role | Name | Date | Signature | Status |
|------|------|------|-----------|--------|
| Log Administrator | [Name] | DD.MM.YYYY | _____ | ☐ Reviewed |
| SOC Lead | [Name] | DD.MM.YYYY | _____ | ☐ Reviewed |
| IT Operations Manager | [Name] | DD.MM.YYYY | _____ | ☐ Reviewed |
| Information Security Manager | [Name] | DD.MM.YYYY | _____ | ☐ Approved |

### Acknowledgments (Rows 14-25)

- ☐ SIEM platform architecture documented
- ☐ Log forwarders inventoried
- ☐ Collection reliability assessed
- ☐ Performance metrics tracked
- ☐ Storage capacity reviewed
- ☐ Gaps identified and prioritized
- ☐ Remediation plan established
- ☐ Next review scheduled

---

## Cell Styling Reference
(Same as IMP-A.8.15.1)

## Formulas & Validation

**Key Formulas:**

**Forwarder ID (Sheet 3, Column A):**
```excel
=IF(B2<>"","FWD-"&TEXT(ROW()-8,"000"),"")
```

**Collection Rate % (Sheet 4, Column E):**
```excel
=IF(C2=0,0,D2/C2*100)
```

**Storage % Used (Sheet 6, Column F):**
```excel
=IF(C2=0,0,D2/C2*100)
```

**Days Until Full (Sheet 6, Column K):**
```excel
=IF(I2=0,"N/A",(E2*1024)/I2)
```

**Quality Score (Sheet 9, Column G):**
```excel
=IF((E2+F2)=0,0,E2/(E2+F2)*100)
```

## Conditional Formatting

**Collection Rate (Sheet 4, Column E):**
- Green: ≥95%
- Yellow: 80-94%
- Red: <80%

**Storage % Used (Sheet 6, Column F):**
- Green: <70%
- Yellow: 70-85%
- Red: >85%

**Parse Success Rate (Sheet 7, Column E):**
- Green: ≥95%
- Yellow: 80-94%
- Red: <80%

**Performance Status (Sheet 8, Column M):**
- Green: All metrics within target
- Yellow: 1-2 metrics outside target
- Red: 3+ metrics outside target

## File Naming Convention

**Filename:** `ISMS-IMP-A_8_15_2_Log_Collection_Centralization_YYYYMMDD.xlsx`

---

**END OF ISMS-IMP-A.8.15.2 SPECIFICATION**