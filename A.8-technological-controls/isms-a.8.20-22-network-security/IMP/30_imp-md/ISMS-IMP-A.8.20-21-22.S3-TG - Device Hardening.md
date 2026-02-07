**ISMS-IMP-A.8.20-21-22.S3-TG - Device Hardening Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.20-21-22-S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Network Device Security Hardening |
| **Related Policy** | ISMS-POL-A.8.20-21-22, Section 2.1 (Network Infrastructure Security - A.8.20) |
| **Purpose** | Establish systematic procedures for hardening network devices (routers, switches, firewalls, wireless APs) against security threats using industry-standard baselines and vendor best practices |
| **Target Audience** | Network Administrators, Security Engineers, System Administrators, Configuration Management Teams, Auditors |
| **Assessment Type** | Technical Configuration & Compliance Assessment |
| **Review Cycle** | Quarterly or After Major Firmware/Configuration Changes |
| **Total Sheets** | 11 |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guidance for network device hardening process | ISMS Implementation Team |

---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a820_3_services_catalog.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.20-21-22.S3` |
| **Output Filename** | `ISMS-IMP-A.8.20-21-22.S3_Network_Services_Catalog_YYYYMMDD.xlsx` |
| **Workbook Title** | Network Services Catalog & Security Assessment |
| **Total Sheets** | 12 (12 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls A.8.20, A.8.21, A.8.22: Network Security |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #002060 | 002060 | Custom |
| #003366 | 003366 | Dark Blue (Headers) |
| #006100 | 006100 | Dark Green (Pass) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #7F7F7F | 7F7F7F | Custom |
| #92D050 | 92D050 | Green (Complete) |
| #9C0006 | 9C0006 | Dark Red (Error) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFF00 | FFFF00 | Yellow (Warning) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Data_Validations

---

## Sheet 2: Instructions & Guide

---

## Sheet 3: Services_Catalog

**Data Rows:** 15 (rows 2–16) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Service ID |
| B | Service Type |
| C | Service Name |
| D | Purpose |
| E | Hosting Location |
| F | IP Address |
| G | Port(s) |
| H | Criticality |
| I | Redundancy Level |
| J | Monitoring Status |
| K | SLA Uptime % |
| L | Owner |
| M | Last Security Review |
| N | Status |
| O | Notes |
| P | Assessment Link |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| HN:HN | equal  |  |
| HN:HN | equal  |  |
| HN:HN | equal  |  |
| HN:HN | equal  |  |

---

## Sheet 4: DNS_Security_Assessment

**Data Rows:** 14 (rows 1–14)

### Columns

| Col | Header |
|-----|--------|
| A | Service ID |
| B | DNS Type |
| C | DNSSEC Enabled |
| D | Split DNS |
| E | Rate Limiting |
| F | Query Logging |
| G | RPZ/Filtering |
| H | Recursion Control |
| I | Cache Poisoning Protection |
| J | Zone Transfer Controls |
| K | TSIG/SIG(0) |
| L | Compliance Score % |
| M | Last Assessed |
| N | Notes |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| NN:NN | equal  |  |
| NN:NN | equal  |  |
| NN:NN | equal  |  |

---

## Sheet 5: DHCP_Security_Assessment

**Data Rows:** 12 (rows 1–12)

### Columns

| Col | Header |
|-----|--------|
| A | Service ID |
| B | DHCP Scope |
| C | DHCP Snooping |
| D | Rogue DHCP Detection |
| E | Server Hardening |
| F | Lease Time Appropriate |
| G | Utilization Monitoring |
| H | Reservation Management |
| I | Logging Enabled |
| J | Compliance Score % |
| K | Last Assessed |
| L | Notes |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| NN:NN | equal  |  |
| NN:NN | equal  |  |

---

## Sheet 6: NTP_Security_Assessment

**Data Rows:** 11 (rows 1–11)

### Columns

| Col | Header |
|-----|--------|
| A | Service ID |
| B | NTP Role |
| C | Authentication |
| D | Access Control |
| E | Stratum Appropriate |
| F | Source Validation |
| G | Monitoring |
| H | Compliance Score % |
| I | Stratum Level |
| J | Last Assessed |
| K | Notes |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| NN:NN | equal  |  |
| NN:NN | equal  |  |

---

## Sheet 7: Proxy_Security_Assessment

**Data Rows:** 13 (rows 1–13)

### Columns

| Col | Header |
|-----|--------|
| A | Service ID |
| B | Proxy Type |
| C | Authentication |
| D | SSL Inspection |
| E | Category Filtering |
| F | Malware Scanning |
| G | Logging |
| H | Bypass Prevention |
| I | Redundancy |
| J | Compliance Score % |
| K | Last Assessed |
| L | Filter Categories |
| M | Notes |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| NN:NN | equal  |  |
| NN:NN | equal  |  |

---

## Sheet 8: Additional_Services

**Data Rows:** 12 (rows 1–12)

### Columns

| Col | Header |
|-----|--------|
| A | Service ID |
| B | Service Type |
| C | Authentication |
| D | Encryption |
| E | Access Control |
| F | Logging |
| G | Monitoring |
| H | Hardening Applied |
| I | Compliance Score % |
| J | Last Assessed |
| K | Key Controls |
| L | Notes |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| NN:NN | equal  |  |
| NN:NN | equal  |  |

---

## Sheet 9: Service_Compliance_Summary

---

## Sheet 10: Service Distribution by Type

---

## Sheet 11: Gap_Analysis

**Data Rows:** 9 (rows 2–10) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | Service ID |
| C | Service Type |
| D | Security Gap |
| E | Current State |
| F | Severity |
| G | Remediation Plan |
| H | Owner |
| I | Status |
| J | Target Date |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| FN:FN | equal  |  |
| FN:FN | equal  |  |
| FN:FN | equal  |  |
| FN:FN | equal  |  |

---

## Sheet 12: Service_Dependencies

**Data Rows:** 6 (rows 1–6)

### Columns

| Col | Header |
|-----|--------|
| A | Service ID |
| B | Service Name |
| C | Depends On |
| D | Required By |
| E | Impact of Failure |
| F | Notes |

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `SERVICE_TYPES` | DNS, DHCP, NTP, Proxy/Web Filter, Load Balancer, RADIUS/TACACS+ (AAA), SNMP, Syslog, SMTP Relay, ... |

---

**END OF SPECIFICATION**

---

*"I would not dare to say that there is a direct relation between mathematics and madness, but there is no doubt that great mathematicians suffer from maniacal characteristics."*
— John Nash

<!-- QA_VERIFIED: 2026-02-06 -->
