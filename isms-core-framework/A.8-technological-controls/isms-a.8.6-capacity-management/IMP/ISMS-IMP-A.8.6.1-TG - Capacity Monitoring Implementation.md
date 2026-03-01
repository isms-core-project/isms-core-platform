<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.6.1-TG:framework:TG:a.8.6.1 -->
**ISMS-IMP-A.8.6.1-TG - Capacity Utilization Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.6: Capacity Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Capacity Monitoring Implementation |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.6.1-TG |
| **Related Policy** | ISMS-POL-A.8.6 (Capacity Management) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.6 (Capacity Management) |
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

- ISMS-POL-A.8.6 (Capacity Management)
- ISMS-IMP-A.8.6.2 (Capacity Forecasting Planning)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a86_1_capacity_utilisation.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.6-Assessment-1`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Compute Resources |
| 2 | Storage Resources |
| 3 | Network Resources |
| 4 | Application Resources |
| 5 | Cloud Resources |
| 6 | Threshold Summary |
| 7 | Coverage Analysis |
| 8 | Summary Dashboard |
| 9 | Evidence Register |
| 10 | Approval Sign-Off |
| 11 | Instructions & Legend |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
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
| 1 | COMPUTE CAPACITY UTILIZATION |
| 2 | STORAGE CAPACITY UTILIZATION |
| 3 | NETWORK CAPACITY UTILIZATION |
| 4 | APPLICATION CAPACITY UTILIZATION |
| 5 | CLOUD SERVICE CAPACITY UTILIZATION |
| 6 | CAPACITY THRESHOLD STATUS SUMMARY |
| 7 | MONITORING COVERAGE ANALYSIS |
| 8 | MONITORING GAPS - Resources Not Yet Monitored |
| 9 | Resource Name |
| 10 | Resource Type |
| 11 | Location/Cluster |
| 12 | Business Function |
| 13 | Total CPU (Cores) |
| 14 | Used CPU (Cores) |
| 15 | CPU Utilization (%) |
| 16 | Total Memory (GB) |
| 17 | Used Memory (GB) |
| 18 | Memory Utilization (%) |
| 19 | Peak CPU (%) |
| 20 | Peak Memory (%) |
| 21 | Threshold Status |
| 22 | Storage Type |
| 23 | Location/Server |
| 24 | Total Capacity (GB) |
| 25 | Used Capacity (GB) |
| 26 | Available Capacity (GB) |
| 27 | Utilization (%) |
| 28 | Peak Utilization (%) |
| 29 | Growth Rate (GB/month) |
| 30 | Network Type |
| 31 | Location |
| 32 | Link Capacity (Mbps) |
| 33 | Avg Inbound (Mbps) |
| 34 | Avg Outbound (Mbps) |
| 35 | Total Utilization (%) |
| 36 | Concurrent Connections |
| 37 | Connection Limit |
| 38 | Application Name |
| 39 | Application Type |
| 40 | Max Concurrent Users |
| 41 | Current Active Users |
| 42 | User Utilization (%) |
| 43 | Max Transactions/sec |
| 44 | Current Transactions/sec |
| 45 | Transaction Utilization (%) |
| 46 | Avg Response Time (ms) |
| 47 | Cloud Provider |
| 48 | Service/Resource Type |
| 49 | Region |
| 50 | Quota/Limit |
| 51 | Current Usage |
| 52 | Monthly Cost (CHF) |
| 53 | Reserved Capacity |
| 54 | Auto-Scaling Enabled |
| 55 | Resource Category |
| 56 | Total Resources |
| 57 | {CHECK} OK |
| 58 | {WARNING} Warning |
| 59 | {XMARK} Critical |
| 60 | Not Monitored |
| 61 | Coverage Metric |
| 62 | Target |
| 63 | Actual |
| 64 | Gap |
| 65 | Status |
| 66 | Reason Not Monitored |
| 67 | Planned Monitoring Date |
| 68 | Responsible Party |
| 69 | CPU Util (%) |
| 70 | Memory Util (%) |
| 71 | Evidence ID |
| 72 | Assessment Area |
| 73 | Evidence Type |
| 74 | Description |
| 75 | Location/Path |
| 76 | Date Collected |
| 77 | Collected By |
| 78 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, Physical Server, Virtual Machine, Container/Pod, Cloud Instance
Other, Prometheus, Datadog, New Relic, CloudWatch, Azure Monitor
GCP Monitoring, Zabbix, Nagios, PRTG, Filesystem, Database, Backup Repository
Archive, SAN/NAS, Object Storage, WAN/Internet, LAN, Inter-DC Link, VPN
Load Balancer, Firewall, Web Application, API Service, Message Queue
Batch Processing, SaaS Application, AWS, Azure, GCP, Oracle Cloud, IBM Cloud
Alibaba Cloud, Monitoring dashboard, Screenshot, Utilization report
Documentation, Capacity plan, Alert configuration, Audit log
Compliance report, Verified, Pending verification, Not verified
Requires update, Draft, Final, Requires remediation, Re-assessment required
Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 11 sheets, 78 columns, 59 validation values, 9 colors

---

**END OF SPECIFICATION**


---

*"Differential cryptanalysis taught us that even small biases can lead to complete breaks of cryptographic systems."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
