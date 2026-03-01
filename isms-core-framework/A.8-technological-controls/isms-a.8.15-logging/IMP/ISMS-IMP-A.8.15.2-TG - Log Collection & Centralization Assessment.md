<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.15.2-TG:framework:TG:a.8.15.2 -->
**ISMS-IMP-A.8.15.2-TG - Log Collection & Centralization Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Log Collection & Centralization Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.15.2-TG |
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

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a815_2_log_collection_centralization.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.15.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | SIEM Platform Details |
| 3 | Log Forwarder Inventory |
| 4 | Collection Reliability |
| 5 | Integration Architecture |
| 6 | SIEM Storage & Capacity |
| 7 | Log Parsing & Normalisation |
| 8 | SIEM Performance Metrics |
| 9 | Data Quality Assessment |
| 10 | Encryption & Authentication |
| 11 | Gap Analysis |
| 12 | Evidence Register |
| 13 | Summary Dashboard |
| 14 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #808080 | Gray (Disabled) |
| #C00000 | Dark Red (Blocked) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | Platform Component |
| 2 | Product/Vendor |
| 3 | Version |
| 4 | Hostname/FQDN |
| 5 | IP Address |
| 6 | Role |
| 7 | OS/Platform |
| 8 | CPU Cores |
| 9 | Memory (GB) |
| 10 | Storage Capacity (TB) |
| 11 | Storage Used (TB) |
| 12 | Storage % Used |
| 13 | Availability |
| 14 | Notes |
| 15 | Forwarder ID |
| 16 | Forwarder Type |
| 17 | Installed On System |
| 18 | System Hostname |
| 19 | Destination SIEM |
| 20 | Transport Protocol |
| 21 | Port |
| 22 | Encryption |
| 23 | Buffer Enabled |
| 24 | Buffer Size (MB) |
| 25 | Install Date |
| 26 | Last Updated |
| 27 | Status |
| 28 | Events/Day |
| 29 | Data/Day (MB) |
| 30 | Last Health Check |
| 31 | Source System ID |
| 32 | Source System Name |
| 33 | Expected Events/Day |
| 34 | Actual Events/Day |
| 35 | Collection Rate % |
| 36 | Last Event Received |
| 37 | Gap Detected |
| 38 | Gap Start Time |
| 39 | Gap End Time |
| 40 | Gap Duration (hours) |
| 41 | Gap Reason |
| 42 | Resolution Actions |
| 43 | Resolved By |
| 44 | Resolved Date |
| 45 | Integration Point |
| 46 | Source Type |
| 47 | Source Count |
| 48 | Collection Method |
| 49 | Intermediate Hops |
| 50 | Network Path |
| 51 | Bandwidth Required |
| 52 | Latency Target |
| 53 | Current Latency |
| 54 | Redundancy |
| 55 | Single Point of Failure |
| 56 | DR Capability |
| 57 | Bottleneck Risk |
| 58 | Storage Component |
| 59 | Technology |
| 60 | Total Capacity (TB) |
| 61 | Used Capacity (TB) |
| 62 | Free Capacity (TB) |
| 63 | % Used |
| 64 | Retention Period |
| 65 | Avg Daily Ingest (GB) |
| 66 | Growth Rate %/Month |
| 67 | Days Until Full |
| 68 | Expansion Plan |
| 69 | Expansion Date |
| 70 | Cost per TB/Month |
| 71 | Log Source Type |
| 72 | Log Format |
| 73 | Parsing Method |
| 74 | Parser Status |
| 75 | Parse Success Rate % |
| 76 | Unparsed Events/Day |
| 77 | Fields Extracted |
| 78 | Required Fields Present |
| 79 | Timestamp Parsing |
| 80 | Timezone Handling |
| 81 | Last Parser Update |
| 82 | Issues Identified |
| 83 | Tuning Required |
| 84 | Owner |
| 85 | Metric Date |
| 86 | Daily Events Indexed |
| 87 | Peak Events/Second |
| 88 | Indexing Lag (minutes) |
| 89 | Search Performance (sec) |
| 90 | Dashboard Load Time (sec) |
| 91 | CPU Utilization % |
| 92 | Memory Utilization % |
| 93 | Disk I/O % |
| 94 | Network Throughput (Gbps) |
| 95 | Uptime % |
| 96 | Incidents |
| 97 | Performance Status |
| 98 | Quality Dimension |
| 99 | Assessment Method |
| 100 | Sample Size |
| 101 | Pass Count |
| 102 | Fail Count |
| 103 | Quality Score % |
| 104 | Common Issues |
| 105 | Impact |
| 106 | Remediation Action |
| 107 | Responsible Party |
| 108 | Target Date |
| 109 | Gap ID |
| 110 | Gap Category |
| 111 | Description |
| 112 | Affected Systems |
| 113 | Current State |
| 114 | Target State |
| 115 | Timeframe |
| 116 | Projected Ingest (TB) |
| 117 | Capacity Needed (TB) |
| 118 | Gap (TB) |
| 119 | Estimated Cost |
| 120 | Log Source/Path |
| 121 | Protocol |
| 122 | TLS Version |
| 123 | Cipher Suite |
| 124 | Certificate Valid |
| 125 | Certificate Expiry |
| 126 | Mutual TLS |
| 127 | Compliance Status |
| 128 | Last Verified |
| 129 | Evidence Ref |
| 130 | Auth Type |
| 131 | Credential Storage |
| 132 | Rotation Frequency |
| 133 | Last Rotated |
| 134 | Service Account |
| 135 | MFA Enabled |
| 136 | Compliance |
| 137 | Evidence ID |
| 138 | Assessment Area |
| 139 | Evidence Type |
| 140 | Location/Path |
| 141 | Date Collected |
| 142 | Collected By |
| 143 | Verification Status |
| 144 | Total Items |
| 145 | Compliant |
| 146 | Partial |
| 147 | Non-Compliant |
| 148 | N/A |
| 149 | Compliance % |
| 150 | Metric |
| 151 | Value |
| 152 | Target |
| 153 | Finding Type |
| 154 | Risk Level |
| 155 | Associated Sheet |
| 156 | Recommended Action |
| 157 | ISO Clause |

### Data Validation Values

All dropdown/list values used across sheets:

```
SIEM Core, Indexer, Search Head, Forwarder Management, Storage, API Gateway
Other, Splunk, QRadar, Sentinel, LogRhythm, ELK Stack, Graylog, Custom
Primary, Secondary, DR, Dev/Test, Active, Standby, Offline, Degraded
Splunk UF, Fluentd, Logstash, rsyslog, syslog-ng, Filebeat, Winlogbeat
Windows Event Forwarder, Cloud Connector, Both, Load Balanced, Syslog/TLS
Syslog/TCP, Syslog/UDP, HTTPS, gRPC, Proprietary, Yes (TLS 1.3), Yes (TLS 1.2)
No, N/A, Yes, Running, Stopped, Error, Unknown, Network Issue, Forwarder Down
Source Down, SIEM Issue, Configuration Error, Server, Network Device
Application, Cloud Service, Security Tool, Container, Agent-based
Agentless/Syslog, API Pull, API Push, File Collection, Stream Processing, None
Active/Passive, Active/Active, Mitigated, Partial, High, Medium, Low
Hot Storage, Warm Storage, Cold Storage, Archive, Backup, Local Disk/SSD, SAN
NAS, Object Storage (S3/Azure), Tape, Cloud, Not Needed, Planned, In Progress
Urgent, Syslog, CEF, JSON, EVTX, LEEF, Built-in, Custom Regex, Grok
Logstash Filter, Custom Script, ML-based, Working, Needs Tuning, Broken
Not Configured, All, Most, Some, Few, Correct, Incorrect, Missing
Completeness, Accuracy, Consistency, Timeliness, Validity, Critical
Coverage Gap, Reliability Issue, Performance Issue, Parsing Error
Capacity Constraint, Redundancy Gap, DR Gap, Data Quality Issue, Open
Resolved, Deferred, Configuration file, Screenshot, Network scan
Documentation, Vendor spec, Certificate inventory, Audit log
Compliance report, Verified, Pending verification, Not verified
Requires update, Draft, Final, Requires remediation, Re-assessment required
Approved, Approved with Conditions, Rejected
```

**Extracted:** 14 sheets, 157 columns, 146 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Make everything as simple as possible, but not simpler."*
- Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
