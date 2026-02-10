<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.15.2-TG:framework:TG:a.8.15.2 -->
**ISMS-IMP-A.8.15.2-TG - Log Collection & Centralization Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Log Collection Infrastructure & SIEM Integration |
| **Related Policy** | ISMS-POL-A.8.15, Section 2.2 (Log Protection & Integrity Requirements), Section 2.3 (Log Retention & Storage Requirements) |
| **Purpose** | Assess SIEM/log management infrastructure, verify log collection coverage and reliability, validate centralized logging implementation |
| **Target Audience** | Security Operations Center (SOC), SIEM Administrators, IT Operations, Network Team, Security Engineers, Compliance Officers, Auditors, Workbook Developers |
| **Assessment Type** | Infrastructure & Operational |
| **Review Cycle** | Annual (full assessment), Quarterly (reliability metrics) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial technical specification for Log Collection assessment workbook | ISMS Implementation Team |


---
# Technical Specification
**Audience:** Workbook Developers (Python/Excel script maintainers)


> Auto-generated from `generate_a815_2_log_collection_centralization.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.15.2` |
| **Output Filename** | `ISMS-IMP-A.8.15.2_Log_Collection_Centralization_YYYYMMDD.xlsx` |
| **Total Sheets** | 28 (28 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.15: Logging |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #4472C4 | end_color | Medium Blue (Sub-headers) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: SIEM Platform Details

---

## Sheet 3: Log Forwarder Inventory

---

## Sheet 4: Collection Reliability

---

## Sheet 5: Integration Architecture

---

## Sheet 6: SIEM Storage & Capacity

---

## Sheet 7: Log Parsing & Normalization

---

## Sheet 8: SIEM Performance Metrics

---

## Sheet 9: Data Quality Assessment

---

## Sheet 10: Encryption & Authentication

---

## Sheet 11: Gap Analysis & Remediation

---

## Sheet 12: Evidence Register

---

## Sheet 13: Summary Dashboard

---

## Sheet 14: Approval & Sign-Off

---

## Sheet 15: Instructions

**Frozen Panes:** A3

---

## Sheet 16: Siem_Platform

**Data Rows:** 22 (rows 9–30) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Platform Component | 25 |
| B | Product/Vendor | 25 |
| C | Version | 15 |
| D | Hostname/FQDN | 30 |
| E | IP Address | 15 |
| F | Role | 20 |
| G | OS/Platform | 20 |
| H | CPU Cores | 10 |
| I | Memory (GB) | 15 |
| J | Storage Capacity (TB) | 20 |
| K | Storage Used (TB) | 20 |
| L | Storage % Used | 15 |
| M | Availability | 15 |
| N | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| A | A9:A30 | `component_dv` |
| B | B9:B30 | `vendor_dv` |
| F | F9:F30 | `role_dv` |
| M | M9:M30 | `availability_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| LN | `=IF(J{data_row}=0,0,K{data_row}/J{data_row})` |  |

---

## Sheet 17: Log_Forwarder_Inventory

**Data Rows:** 192 (rows 9–200) | **Frozen Panes:** C8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Forwarder ID | 15 |
| B | Forwarder Type | 20 |
| C | Version | 12 |
| D | Installed On System | 30 |
| E | System Hostname | 30 |
| F | Destination SIEM | 25 |
| G | Transport Protocol | 18 |
| H | Port | 10 |
| I | Encryption | 15 |
| J | Buffer Enabled | 15 |
| K | Buffer Size (MB) | 18 |
| L | Install Date | 15 |
| M | Last Updated | 15 |
| N | Status | 15 |
| O | Events/Day | 20 |
| P | Data/Day (MB) | 20 |
| Q | Last Health Check | 15 |
| R | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B9:B200 | `forwarder_type_dv` |
| F | F9:F200 | `destination_dv` |
| G | G9:G200 | `protocol_dv` |
| I | I9:I200 | `encryption_dv` |
| J | J9:J200 | `buffer_dv` |
| N | N9:N200 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{data_row}<>` |  |

---

## Sheet 18: Collection_Reliability

**Data Rows:** 192 (rows 9–200) | **Frozen Panes:** C8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Source System ID | 15 |
| B | Source System Name | 30 |
| C | Expected Events/Day | 20 |
| D | Actual Events/Day | 20 |
| E | Collection Rate % | 18 |
| F | Status | 15 |
| G | Last Event Received | 18 |
| H | Gap Detected | 15 |
| I | Gap Start Time | 18 |
| J | Gap End Time | 18 |
| K | Gap Duration (hours) | 20 |
| L | Gap Reason | 30 |
| M | Resolution Actions | 40 |
| N | Resolved By | 20 |
| O | Resolved Date | 15 |
| P | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| H | H9:H200 | `gap_detected_dv` |
| L | L9:L200 | `gap_reason_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| BN | `=IF(A{data_row}=` |  |
| EN | `=IF(C{data_row}=0,0,D{data_row}/C{data_row})` |  |
| KN | `=IF(AND(I{data_row}<>` |  |

---

## Sheet 19: Integration_Architecture

**Purpose:** "Architecture is politics" - Mitch Kapor

**Data Rows:** 42 (rows 9–50) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Integration Point | 25 |
| B | Source Type | 20 |
| C | Source Count | 15 |
| D | Collection Method | 25 |
| E | Intermediate Hops | 20 |
| F | Network Path | 30 |
| G | Bandwidth Required | 20 |
| H | Latency Target | 15 |
| I | Current Latency | 15 |
| J | Redundancy | 15 |
| K | Single Point of Failure | 20 |
| L | DR Capability | 15 |
| M | Bottleneck Risk | 15 |
| N | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B9:B50 | `source_type_dv` |
| D | D9:D50 | `method_dv` |
| J | J9:J50 | `redundancy_dv` |
| K | K9:K50 | `spof_dv` |
| L | L9:L50 | `dr_dv` |
| M | M9:M50 | `bottleneck_dv` |

---

## Sheet 20: Siem_Storage_Capacity

**Data Rows:** 12 (rows 9–20) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Storage Component | 25 |
| B | Technology | 20 |
| C | Total Capacity (TB) | 20 |
| D | Used Capacity (TB) | 20 |
| E | Free Capacity (TB) | 20 |
| F | % Used | 12 |
| G | Status | 15 |
| H | Retention Period | 20 |
| I | Avg Daily Ingest (GB) | 20 |
| J | Growth Rate %/Month | 20 |
| K | Days Until Full | 15 |
| L | Expansion Plan | 30 |
| M | Expansion Date | 15 |
| N | Cost per TB/Month | 20 |
| O | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| A | A9:A20 | `storage_component_dv` |
| B | B9:B20 | `technology_dv` |
| L | L9:L20 | `expansion_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| EN | `=IF(C{data_row}=` |  |
| FN | `=IF(C{data_row}=0,0,D{data_row}/C{data_row})` |  |
| GN | `=IF(A{data_row}=` |  |
| KN | `=IF(OR(I{data_row}=0,E{data_row}=` |  |
| — | `=SUM(D9:D20)` | Current |
| — | `=SUM(I9:I20)*180/1024` | 6 months |
| — | `=SUM(I9:I20)*365/1024` | 12 months |
| — | `=SUM(I9:I20)*730/1024` | 24 months |

---

## Sheet 21: Log_Parsing_Normalization

**Data Rows:** 92 (rows 9–100) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Log Source Type | 25 |
| B | Log Format | 20 |
| C | Parsing Method | 20 |
| D | Parser Status | 15 |
| E | Parse Success Rate % | 20 |
| F | Unparsed Events/Day | 20 |
| G | Fields Extracted | 20 |
| H | Required Fields Present | 20 |
| I | Timestamp Parsing | 18 |
| J | Timezone Handling | 18 |
| K | Last Parser Update | 15 |
| L | Issues Identified | 40 |
| M | Tuning Required | 15 |
| N | Owner | 20 |
| O | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B9:B100 | `log_format_dv` |
| C | C9:C100 | `parsing_method_dv` |
| D | D9:D100 | `parser_status_dv` |
| H | H9:H100 | `required_fields_dv` |
| I | I9:I100 | `timestamp_dv` |
| J | J9:J100 | `timezone_dv` |
| M | M9:M100 | `tuning_dv` |

---

## Sheet 22: Siem_Performance_Metrics

**Data Rows:** 82 (rows 9–90) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Metric Date | 15 |
| B | Daily Events Indexed | 20 |
| C | Peak Events/Second | 20 |
| D | Indexing Lag (minutes) | 20 |
| E | Search Performance (sec) | 20 |
| F | Dashboard Load Time (sec) | 20 |
| G | CPU Utilization % | 18 |
| H | Memory Utilization % | 18 |
| I | Disk I/O % | 15 |
| J | Network Throughput (Gbps) | 20 |
| K | Uptime % | 12 |
| L | Incidents | 15 |
| M | Performance Status | 18 |
| N | Notes | 40 |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| MN | `=IF(A{data_row}=` |  |
| — | `=SUM(L9:L38)` | Total Incidents: |
| — | `=COUNTIF(M9:M38,\` | Days with Healthy Status: |

---

## Sheet 23: Data_Quality_Assessment

**Data Rows:** 42 (rows 9–50) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Quality Dimension | 25 |
| B | Log Source Type | 25 |
| C | Assessment Method | 30 |
| D | Sample Size | 15 |
| E | Pass Count | 15 |
| F | Fail Count | 15 |
| G | Quality Score % | 18 |
| H | Status | 15 |
| I | Common Issues | 40 |
| J | Impact | 20 |
| K | Remediation Action | 40 |
| L | Responsible Party | 25 |
| M | Target Date | 15 |
| N | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| A | A9:A50 | `quality_dimension_dv` |
| J | J9:J50 | `impact_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| GN | `=IF(AND(D{data_row}<>` |  |
| HN | `=IF(G{data_row}=` |  |

---

## Sheet 24: Encryption_Authentication

**Frozen Panes:** A6

### Columns

| Col | Header |
|-----|--------|
| A | Log Source/Path |
| B | Protocol |
| C | TLS Version |
| D | Cipher Suite |
| E | Certificate Valid |
| F | Certificate Expiry |
| G | Mutual TLS |
| H | Compliance Status |
| I | Last Verified |
| J | Evidence Ref |
| K | Notes |

---

## Sheet 25: Gap_Analysis

**Data Rows:** 92 (rows 9–100) | **Frozen Panes:** A8

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Gap ID | 12 |
| B | Gap Category | 25 |
| C | Description | 50 |
| D | Affected Systems | 30 |
| E | Impact | 20 |
| F | Current State | 40 |
| G | Target State | 40 |
| H | Remediation Action | 50 |
| I | Owner | 25 |
| J | Target Date | 15 |
| K | Status | 15 |
| L | Notes | 40 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| B | B9:B100 | `gap_category_dv` |
| E | E9:E100 | `impact_dv` |
| K | K9:K100 | `status_dv` |

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| AN | `=IF(B{data_row}<>` |  |

---

## Sheet 26: Evidence_Register

**Data Rows:** 95 (rows 6–100) | **Frozen Panes:** A6

### Columns

| Col | Header | Width |
|-----|--------|-------|
| A | Evidence ID | 12 |
| B | Assessment Sheet | 22 |
| C | Evidence Type | 20 |
| D | Evidence Title | 35 |
| E | Description | 40 |
| F | File Location/Link | 35 |
| G | Date Collected | 14 |
| H | Collected By | 18 |
| I | Retention Period | 15 |
| J | Review Date | 14 |
| K | Status | 12 |
| L | Notes | 30 |

### Data Validations

| Column | Range | Validation Variable |
|--------|-------|---------------------|
| C | C6:C100 | `type_dv` |
| B | B6:B100 | `sheet_dv` |
| K | K6:K100 | `status_dv` |

---

## Sheet 27: Summary_Dashboard

**Purpose:** "Simplicity is the ultimate sophistication." - Leonardo da Vinci

**Data Rows:** 192 (rows 9–200)

### Formulas

| Cell | Formula | Purpose |
|------|---------|---------|
| — | `=COUNTA(` | Total Systems Monitored |
| — | `=COUNTIF(` | Systems Collecting >95% |
| DN | `=IF(B{row}>0,\` |  |
| BN | `=COUNTIF(\` |  |
| CN | `=COUNTIFS(\` |  |
| DN | `=AVERAGEIF(\` |  |
| EN | `=SUMPRODUCT((\` |  |

---

## Sheet 28: Approval_Signoff

---

**END OF SPECIFICATION**

---

*"Make everything as simple as possible, but not simpler."*
- Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
