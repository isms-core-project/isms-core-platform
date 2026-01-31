# ISMS-IMP-A.8.15.1
## Log Source Inventory Assessment
### Excel Workbook Layout Specification

**Document ID**: ISMS-IMP-A.8.15.1  
**Assessment Area**: Log Source Inventory and Completeness  
**Related Policy**: ISMS-POL-A.8.15-S2.1 (Event Logging Requirements)  
**Purpose**: Catalog all systems generating logs and assess logging completeness  
**Python Generator**: `generate_a815_1_log_source_inventory.py`

---

## Workbook Structure

### Sheet 1: Instructions & Legend

**Header**: "Log Source Inventory Assessment - ISO/IEC 27001:2022 Control A.8.15"

**Document Information Block**:
```
Document ID:           ISMS-IMP-A.8.15.1
Assessment Area:       Log Source Inventory
Related Policy:        ISMS-POL-A.8.15-S2.1
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Annual (full assessment), Quarterly (updates)
```

**How to Use This Workbook**:
1. Complete the "System Inventory" sheet for all in-scope systems
2. For each system, document log sources and event types logged
3. Use dropdowns to ensure consistent data entry
4. Yellow cells require user input, gray cells are auto-calculated
5. Complete compliance checklist for each log source type
6. Review Summary Dashboard for overall compliance status
7. Document gaps in Gap Analysis sheet
8. Develop remediation plan for identified gaps
9. Obtain approvals in Approval & Sign-Off sheet

**Legend** (color coding):
- Yellow: User input required
- Green: Compliant / Complete
- Red: Non-compliant / Missing
- Gray: Auto-calculated / Reference data
- Blue: Instructions / Headers

---

### Sheet 2: System Inventory

**Purpose**: Catalog all systems in scope for logging

**Column Structure** (17 columns A-Q):

| Column | Header | Width | Type | Validation/Format |
|--------|--------|-------|------|-------------------|
| A | System ID | 15 | Text | Auto-generated: SYS-001, SYS-002, etc. |
| B | System Name | 30 | Text | Free text |
| C | System Type | 20 | Dropdown | Server, Network Device, Security Appliance, Application, Cloud Service, Database, Other |
| D | Operating System / Platform | 25 | Dropdown | Windows, Linux, Unix, Network OS, Cloud, Application Platform, Other |
| E | Environment | 15 | Dropdown | Production, Staging, Development, Test |
| F | Data Classification | 18 | Dropdown | Public, Internal, Confidential, Restricted |
| G | Business Criticality | 18 | Dropdown | Critical (T1), High (T2), Medium (T3), Low (T4) |
| H | Regulatory Scope | 20 | Multi-select | PCI DSS, HIPAA, GDPR, FADP, SOX, DORA, NIS2, None |
| I | Logging Priority | 15 | Dropdown | P1-Critical, P2-High, P3-Medium, P4-Low |
| J | System Owner | 25 | Text | Name |
| K | Owner Email | 30 | Email | Email format validation |
| L | Hostname / FQDN | 30 | Text | Free text |
| M | Primary IP | 15 | Text | IP format validation |
| N | Location | 20 | Text | Data center, cloud region, etc. |
| O | Logging Enabled | 15 | Dropdown | Yes, No, Partial, Unknown |
| P | Forwarding to SIEM | 18 | Dropdown | Yes, No, Planned, N/A |
| Q | Compliance Status | 18 | Formula | =IF(AND(O2="Yes",P2="Yes"),"Compliant","Non-Compliant") |

**Data Entry Rows**: 8-100 (93 rows for systems)

**Example Row** (Row 7, gray, italic):
```
SYS-001 | web-prod-01 | Server | Linux | Production | Confidential | Critical (T1) | PCI DSS, GDPR | P1-Critical | John Doe | jdoe@example.com | web-prod-01.example.com | 10.0.1.50 | DC1 | Yes | Yes | Compliant
```

---

### Sheet 3: Log Event Types by System

**Purpose**: Document what event types each system logs

**Column Structure** (19 columns A-S):

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | System ID | 15 | Dropdown | Links to Sheet 2 System IDs |
| B | System Name | 30 | Formula | VLOOKUP from Sheet 2 |
| C | Authentication Events | 15 | Dropdown | Yes, No, Partial, N/A |
| D | Authorization Events | 15 | Dropdown | Yes, No, Partial, N/A |
| E | Administrative Actions | 15 | Dropdown | Yes, No, Partial, N/A |
| F | Security Events | 15 | Dropdown | Yes, No, Partial, N/A |
| G | Application Events | 15 | Dropdown | Yes, No, Partial, N/A |
| H | System Events | 15 | Dropdown | Yes, No, Partial, N/A |
| I | Network Events | 15 | Dropdown | Yes, No, Partial, N/A |
| J | Database Events | 15 | Dropdown | Yes, No, Partial, N/A |
| K | Log Format | 15 | Dropdown | Syslog, CEF, JSON, EVTX, Custom, Unknown |
| L | Timestamp Format | 18 | Dropdown | ISO 8601, RFC 3339, Unix Epoch, Custom, Unknown |
| M | Timezone | 15 | Dropdown | UTC, Local, Unknown |
| N | Est. Daily Volume (MB) | 20 | Number | Numeric validation |
| O | Retention Period (months) | 20 | Number | Numeric validation |
| P | Storage Tier | 15 | Dropdown | Hot, Warm, Cold, Unknown |
| Q | Protection Mechanisms | 20 | Multi-select | Access Controls, Encryption, WORM, Hashing, None |
| R | Event Types Completeness | 20 | Formula | Percentage of Yes across C-J |
| S | Notes | 40 | Text | Free text |

**Data Entry Rows**: 8-100

---

### Sheet 4: Authentication Logging Assessment

**Purpose**: Detailed assessment of authentication logging per S2.1.2

**Column Structure** (18 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | System ID | 15 | Dropdown |
| B | System Name | 30 | Formula (VLOOKUP) |
| C | Logs Successful Logins | 18 | Dropdown: Yes / No / Partial / N/A |
| D | Logs Failed Logins | 18 | Dropdown: Yes / No / Partial / N/A |
| E | Logs Account Lockouts | 18 | Dropdown: Yes / No / Partial / N/A |
| F | Logs Password Changes | 18 | Dropdown: Yes / No / Partial / N/A |
| G | Logs Session Start/End | 18 | Dropdown: Yes / No / Partial / N/A |
| H | Includes User ID | 15 | Dropdown: Yes / No |
| I | Includes Timestamp | 15 | Dropdown: Yes / No |
| J | Includes Source IP | 15 | Dropdown: Yes / No |
| K | Includes Auth Method | 15 | Dropdown: Yes / No |
| L | MFA Events Logged | 15 | Dropdown: Yes / No / N/A |
| M | SSO Events Logged | 15 | Dropdown: Yes / No / N/A |
| N | Service Account Auth Logged | 20 | Dropdown: Yes / No / N/A |
| O | Privileged Auth Logged | 18 | Dropdown: Yes / No / N/A |
| P | Compliance Score | 18 | Formula | Percentage compliant |
| Q | Gap Description | 40 | Text | If non-compliant, describe |
| R | Remediation Plan | 40 | Text | How to fix |

---

### Sheet 5: Authorization & Access Logging

**Purpose**: Assessment of access control event logging per S2.1.3

**Column Structure** (similar to Sheet 4, 18 columns):

| Column | Header | Assessment Of |
|--------|--------|---------------|
| A-B | System ID/Name | |
| C | Logs Access Grants | Yes/No/Partial/N/A |
| D | Logs Access Denials | Yes/No/Partial/N/A |
| E | Logs Permission Changes | Yes/No/Partial/N/A |
| F | Logs Privilege Escalation | Yes/No/Partial/N/A |
| G | Logs Data Access (Sensitive) | Yes/No/Partial/N/A |
| H | Includes User ID | Yes/No |
| I | Includes Resource Accessed | Yes/No |
| J | Includes Action Type | Yes/No |
| K | Includes Outcome | Yes/No |
| L | Includes Reason (if denied) | Yes/No |
| M-R | Compliance score, gaps, remediation |

---

### Sheet 6: Administrative Activity Logging

**Purpose**: Assessment of administrative action logging per S2.1.4

**Column Structure** (18 columns):

| Column | Header | Assessment Of |
|--------|--------|---------------|
| A-B | System ID/Name | |
| C | User Account Management | Yes/No/Partial/N/A |
| D | Group/Role Management | Yes/No/Partial/N/A |
| E | Configuration Changes | Yes/No/Partial/N/A |
| F | Security Policy Changes | Yes/No/Partial/N/A |
| G | Software Install/Uninstall | Yes/No/Partial/N/A |
| H | Service Start/Stop | Yes/No/Partial/N/A |
| I | Patch Application | Yes/No/Partial/N/A |
| J | Bulk Data Operations | Yes/No/Partial/N/A |
| K | Privileged Session Logging | Yes/No/Partial/N/A |
| L-R | Includes fields, compliance score, gaps |

---

### Sheet 7: Security Event Logging

**Purpose**: Assessment of security tool and event logging per S2.1.5

**Column Structure** (18 columns):

| Column | Header | Assessment Of |
|--------|--------|---------------|
| A-B | System ID/Name | |
| C | Firewall Events | Yes/No/Partial/N/A |
| D | IDS/IPS Alerts | Yes/No/Partial/N/A |
| E | Anti-malware Events | Yes/No/Partial/N/A |
| F | DLP Events | Yes/No/Partial/N/A |
| G | Web Filtering Events | Yes/No/Partial/N/A |
| H | Email Gateway Events | Yes/No/Partial/N/A |
| I | EDR Events | Yes/No/Partial/N/A |
| J | Vulnerability Scan Results | Yes/No/Partial/N/A |
| K | Security Incident Events | Yes/No/Partial/N/A |
| L-R | Includes severity, compliance score, gaps |

---

### Sheet 8: Application & Database Logging

**Purpose**: Assessment of application and database logging per S2.1.7

**Column Structure** (18 columns):

| Column | Header | Assessment Of |
|--------|--------|---------------|
| A-B | System ID/Name | |
| C | Web App Access Logging | Yes/No/Partial/N/A |
| D | API Call Logging | Yes/No/Partial/N/A |
| E | Transaction Logging | Yes/No/Partial/N/A |
| F | Application Errors | Yes/No/Partial/N/A |
| G | Database Connections | Yes/No/Partial/N/A |
| H | Database Queries (Sensitive) | Yes/No/Partial/N/A |
| I | Schema Changes (DDL) | Yes/No/Partial/N/A |
| J | Permission Grants | Yes/No/Partial/N/A |
| K | Backup/Restore Operations | Yes/No/Partial/N/A |
| L-R | Includes fields, compliance score, gaps |

---

### Sheet 9: Network Device Logging

**Purpose**: Assessment of network infrastructure logging per S2.1.8

**Column Structure** (18 columns):

| Column | Header | Assessment Of |
|--------|--------|---------------|
| A-B | Device ID/Name | |
| C | Connection Logging | Yes/No/Partial/N/A |
| D | Rule Match Logging | Yes/No/Partial/N/A |
| E | Configuration Changes | Yes/No/Partial/N/A |
| F | Interface Up/Down Events | Yes/No/Partial/N/A |
| G | Routing Changes | Yes/No/Partial/N/A |
| H | VPN Session Logging | Yes/No/Partial/N/A |
| I | DHCP/DNS Events | Yes/No/Partial/N/A |
| J | Wireless Events | Yes/No/Partial/N/A |
| K | NAT Translations | Yes/No/Partial/N/A |
| L-R | Includes fields, compliance score, gaps |

---

### Sheet 10: Gap Analysis

**Purpose**: Consolidated list of all identified gaps

**Column Structure** (12 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Gap ID | 12 | Auto-generated: GAP-001, GAP-002 |
| B | System ID | 15 | Dropdown (from Sheet 2) |
| C | System Name | 30 | Formula (VLOOKUP) |
| D | Gap Category | 25 | Dropdown: Log Source Missing, Event Type Not Logged, Incomplete Fields, Format Non-Standard, Protection Inadequate, Other |
| E | Gap Description | 50 | Text |
| F | Policy Requirement | 30 | Text | Reference to S2.1.x |
| G | Impact / Risk | 20 | Dropdown: Critical, High, Medium, Low |
| H | Remediation Action | 50 | Text |
| I | Responsible Party | 25 | Text |
| J | Target Date | 15 | Date | DD.MM.YYYY format |
| K | Status | 15 | Dropdown: Open, In Progress, Resolved, Deferred |
| L | Notes | 40 | Text |

**Auto-population**: Gaps identified in Sheets 3-9 should auto-populate here based on "Non-Compliant" statuses

---

### Sheet 11: Evidence Register

**Purpose**: Track evidence artifacts for audit

**Column Structure** (10 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Evidence ID | 15 | Auto-generated: EVD-001 |
| B | Evidence Type | 25 | Dropdown: Log Sample, Configuration Screenshot, SIEM Query Result, Documentation, Other |
| C | Description | 40 | Text |
| D | Related System(s) | 30 | Text |
| E | Related Policy Req | 25 | Text | S2.1.x reference |
| F | File Name / Location | 40 | Text |
| G | Collected By | 25 | Text |
| H | Collection Date | 15 | Date | DD.MM.YYYY |
| I | Retention Period | 20 | Text | How long to keep |
| J | Notes | 40 | Text |

---

### Sheet 12: Summary Dashboard

**Purpose**: Executive summary of assessment results

**Section 1: Overall Compliance Summary** (Rows 3-10):

| Metric | Formula | Target |
|--------|---------|--------|
| Total Systems Assessed | COUNT(Sheet2!A:A)-1 | N/A |
| Systems with Logging Enabled | COUNTIF(Sheet2!O:O,"Yes") | 100% |
| Systems Forwarding to SIEM | COUNTIF(Sheet2!P:P,"Yes") | 100% |
| Overall Compliance Rate | Avg compliance across sheets | >95% |
| Critical Systems Compliant | % of P1/P2 systems compliant | 100% |
| Medium Systems Compliant | % of P3 systems compliant | >90% |
| Low Systems Compliant | % of P4 systems compliant | >80% |

**Section 2: Event Type Coverage** (Rows 12-22):

| Event Type | Systems Logging | % Coverage | Target |
|------------|-----------------|------------|--------|
| Authentication | COUNTIF(Sheet3!C:C,"Yes") | Formula | >95% |
| Authorization | COUNTIF(Sheet3!D:D,"Yes") | Formula | >95% |
| Administrative | COUNTIF(Sheet3!E:E,"Yes") | Formula | >95% |
| Security Events | COUNTIF(Sheet3!F:F,"Yes") | Formula | 100% (Critical) |
| Application | COUNTIF(Sheet3!G:G,"Yes") | Formula | >90% |
| System | COUNTIF(Sheet3!H:H,"Yes") | Formula | >85% |
| Network | COUNTIF(Sheet3!I:I,"Yes") | Formula | >85% |
| Database | COUNTIF(Sheet3!J:J,"Yes") | Formula | >90% |

**Section 3: Gap Summary by Priority** (Rows 24-30):

| Priority | Open Gaps | In Progress | Resolved | Target Date Risk |
|----------|-----------|-------------|----------|------------------|
| Critical | COUNTIFS formula | COUNTIFS | COUNTIFS | COUNT overdue |
| High | COUNTIFS formula | COUNTIFS | COUNTIFS | COUNT overdue |
| Medium | COUNTIFS formula | COUNTIFS | COUNTIFS | COUNT overdue |
| Low | COUNTIFS formula | COUNTIFS | COUNTIFS | COUNT overdue |

**Section 4: Charts** (Rows 32-50):
- Pie chart: Compliance Status (Compliant, Partial, Non-Compliant)
- Bar chart: Event Type Coverage by System Type
- Trend chart: Gap remediation progress over time (if historical data)
- Heat map: Compliance by System and Event Type

**Section 5: Top Gaps Requiring Attention** (Rows 52-65):
Top 10 gaps from Sheet 10 sorted by Impact/Risk

**Section 6: Recommendations** (Rows 67-80):
- Pre-populated recommendations based on common gaps
- Text box for assessor recommendations

**Section 7: Assessment Metadata** (Rows 82-92):
- Assessment date
- Completed by
- Review date
- Approval status
- Next assessment date

---

### Sheet 13: Approval & Sign-Off

**Purpose**: Document assessment approval

**Approval Table**:

| Role | Name | Date | Signature | Status |
|------|------|------|-----------|--------|
| System Owners (collective) | [List] | DD.MM.YYYY | _____ | [ ] Reviewed |
| Log Administrator | [Name] | DD.MM.YYYY | _____ | [ ] Reviewed |
| SOC Lead | [Name] | DD.MM.YYYY | _____ | [ ] Reviewed |
| Information Security Manager | [Name] | DD.MM.YYYY | _____ | [ ] Approved |
| CISO | [Name] | DD.MM.YYYY | _____ | [ ] Approved |

**Acknowledgments**:
- [ ] Assessment completed per ISMS-POL-A.8.15-S2.1
- [ ] All in-scope systems documented
- [ ] Gaps identified and prioritized
- [ ] Remediation plan established
- [ ] Resources committed for gap remediation
- [ ] Next assessment scheduled

---

## Cell Styling Reference

**Header Styles**:
- Main Header: Calibri 14pt bold white, Fill: 003366 (dark blue), Height: 40px
- Subheader: Calibri 11pt bold white, Fill: 4472C4 (blue), Height: 30px
- Column Header: Calibri 10pt bold black, Fill: D9D9D9 (gray), Borders: All

**Input Cells**:
- Fill: FFFFCC (light yellow)
- Alignment: Left/center, wrapped
- Border: Thin black on all sides

**Status Fills**:
- Compliant: C6EFCE (green)
- Partial: FFEB9C (yellow)
- Non-Compliant: FFC7CE (red)
- N/A: D9D9D9 (gray)

**Formula Cells**:
- Fill: E7E6E6 (light gray)
- Font: Regular black
- Border: Thin

---

## Formulas & Validation

**Key Formulas**:
```excel
// System Compliance Status (Sheet 2, Column Q)
=IF(AND(O2="Yes",P2="Yes"),"Compliant",IF(OR(O2="Partial",P2="Planned"),"Partial","Non-Compliant"))

// Event Type Completeness (Sheet 3, Column R)
=COUNTIF(C2:J2,"Yes")/COUNTA(C2:J2)

// Compliance Score (various sheets, Column P)
=(COUNTIF(C2:O2,"Yes")/COUNTIF(C2:O2,"<>N/A"))*100

// Total Systems (Dashboard)
=COUNTA(Sheet2!A8:A100)

// Compliance Rate (Dashboard)
=COUNTIF(Sheet2!Q:Q,"Compliant")/COUNTA(Sheet2!A8:A100)
```

**Data Validations**:
- All dropdowns: List validation, error alert on invalid entry
- Email fields: Custom formula validation for email format
- IP addresses: Custom formula for IP format (optional)
- Dates: Date format DD.MM.YYYY
- Numbers: Numeric validation, >0

---

## Auto-population Logic

1. **Sheet 3-9 System Names**: VLOOKUP from Sheet 2 based on System ID
2. **Gap Analysis**: Auto-populate from sheets 3-9 where compliance score <100%
3. **Dashboard Metrics**: COUNT/COUNTIF/SUMIF across all data sheets
4. **Charts**: Auto-update based on data ranges

---

## Conditional Formatting

**Apply to all data sheets**:
- Compliance Status column: Green if "Compliant", Red if "Non-Compliant", Yellow if "Partial"
- Compliance Score column: Color scale (Red <70%, Yellow 70-90%, Green >90%)
- Status column (Gap Analysis): Red if "Open", Yellow if "In Progress", Green if "Resolved"
- Target Date column (Gap Analysis): Red if overdue (past today)

---

## File Naming Convention

**Generated Filename**: `ISMS-IMP-A_8_15_1_Log_Source_Inventory_YYYYMMDD.xlsx`

Example: `ISMS-IMP-A_8_15_1_Log_Source_Inventory_20260106.xlsx`

---

## Document Metadata (embedded in Instructions sheet)

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.1 |
| **Version** | 1.0 |
| **ISO 27001 Control** | A.8.15 (Logging) |
| **Related Policy** | ISMS-POL-A.8.15-S2.1 |
| **Sheet Count** | 13 |
| **Estimated Rows** | ~800 (varies by org size) |
| **Estimated Completion Time** | 4-8 hours (for 50-100 systems) |

---

**END OF IMP SPECIFICATION A.8.15.1**

# ISMS-IMP-A.8.15.2
## Log Collection & Centralization Assessment
### Excel Workbook Layout Specification

**Document ID**: ISMS-IMP-A.8.15.2  
**Assessment Area**: Log Collection Infrastructure and SIEM Integration  
**Related Policy**: ISMS-POL-A.8.15-S2.1 (Event Logging), S2.2 (Protection)  
**Purpose**: Assess centralized logging infrastructure and collection reliability  
**Python Generator**: `generate_a815_2_log_collection_centralization.py`

---

## Workbook Structure

### Sheet 1: Instructions & Legend

**Header**: "Log Collection & Centralization Assessment - ISO/IEC 27001:2022 Control A.8.15"

**Document Information Block**:
```
Document ID:           ISMS-IMP-A.8.15.2
Assessment Area:       Log Collection & Centralization
Related Policy:        ISMS-POL-A.8.15-S2.1, S2.2
Version:               1.0
Assessment Date:       [USER INPUT]
Completed By:          [USER INPUT]
Organization:          [USER INPUT]
Review Cycle:          Annual (full), Quarterly (metrics)
```

**How to Use**:
1. Document SIEM/log management platform details
2. Catalog all log forwarders and collectors
3. Assess collection reliability and performance
4. Document integration architecture
5. Review capacity and scalability
6. Identify collection gaps and failures
7. Review dashboard for overall health

---

### Sheet 2: SIEM Platform Details

**Purpose**: Document centralized log management platform

**Column Structure** (14 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Platform Component | 25 | Dropdown: SIEM Core, Indexer, Search Head, Forwarder Management, Storage, Other |
| B | Product/Vendor | 25 | Text: Splunk, QRadar, Sentinel, LogRhythm, ELK, Graylog, Other |
| C | Version | 15 | Text |
| D | Hostname/FQDN | 30 | Text |
| E | IP Address | 15 | Text |
| F | Role | 20 | Dropdown: Primary, Secondary, DR, Dev/Test |
| G | OS/Platform | 20 | Text |
| H | CPU Cores | 10 | Number |
| I | Memory (GB) | 15 | Number |
| J | Storage Capacity (TB) | 20 | Number |
| K | Storage Used (TB) | 20 | Number |
| L | Storage % Used | 15 | Formula: =K/J |
| M | Availability | 15 | Dropdown: Active, Standby, Offline, Degraded |
| N | Notes | 40 | Text |

**Data Rows**: 8-30 (SIEM components)

---

### Sheet 3: Log Forwarder Inventory

**Purpose**: Catalog all log forwarders/collectors deployed

**Column Structure** (18 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Forwarder ID | 15 | Auto: FWD-001, FWD-002 |
| B | Forwarder Type | 20 | Dropdown: Splunk UF, Fluentd, Logstash, rsyslog, syslog-ng, Beats, Windows Event Forwarder, Cloud Connector, Other |
| C | Version | 12 | Text |
| D | Installed On System | 30 | Text (links to IMP 1 System ID) |
| E | System Hostname | 30 | Text |
| F | Destination SIEM | 25 | Dropdown: Primary, Secondary, Both |
| G | Transport Protocol | 18 | Dropdown: Syslog/TLS, Syslog/TCP, Syslog/UDP, HTTPS, Proprietary |
| H | Port | 10 | Number |
| I | Encryption | 15 | Dropdown: Yes (TLS), No, N/A |
| J | Buffer Enabled | 15 | Dropdown: Yes, No |
| K | Buffer Size (MB) | 18 | Number |
| L | Install Date | 15 | Date: DD.MM.YYYY |
| M | Last Updated | 15 | Date: DD.MM.YYYY |
| N | Status | 15 | Dropdown: Running, Stopped, Error, Unknown |
| O | Events/Day | 20 | Number: Estimated forwarding rate |
| P | Data/Day (MB) | 20 | Number |
| Q | Last Health Check | 15 | Date: DD.MM.YYYY |
| R | Notes | 40 | Text |

**Data Rows**: 8-200 (one per system with forwarder)

---

### Sheet 4: Collection Reliability

**Purpose**: Track log collection reliability metrics

**Column Structure** (16 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Source System ID | 15 | Dropdown (from IMP 1) |
| B | Source System Name | 30 | Formula: VLOOKUP |
| C | Expected Events/Day | 20 | Number: Baseline |
| D | Actual Events/Day (Current) | 20 | Number: Current week avg |
| E | Collection Rate % | 18 | Formula: =D/C |
| F | Status | 15 | Formula: If >95% Green, >80% Yellow, <80% Red |
| G | Last Event Received | 18 | Datetime: DD.MM.YYYY HH:MM |
| H | Gap Detected | 15 | Dropdown: Yes, No |
| I | Gap Start Time | 18 | Datetime (if gap) |
| J | Gap End Time | 18 | Datetime (if gap) |
| K | Gap Duration (hours) | 20 | Formula: =J-I |
| L | Gap Reason | 30 | Dropdown: Network Issue, Forwarder Down, Source Down, SIEM Issue, Configuration Error, Unknown |
| M | Resolution Actions | 40 | Text |
| N | Resolved By | 20 | Text: Name |
| O | Resolved Date | 15 | Date |
| P | Notes | 40 | Text |

**Data Rows**: 8-200 (monitoring period: last 30 days)

**Auto-alert logic**: Flag systems with <95% collection rate or gaps >4 hours

---

### Sheet 5: Integration Architecture

**Purpose**: Document log flow architecture

**Column Structure** (14 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Integration Point | 25 | Text: Source → Destination |
| B | Source Type | 20 | Dropdown: Server, Network Device, Application, Cloud Service, Security Tool |
| C | Source Count | 15 | Number: How many sources |
| D | Collection Method | 25 | Dropdown: Agent-based, Agentless/Syslog, API Pull, API Push, File Collection |
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

**Data Rows**: 10-50 (integration patterns)

**Include**: Architecture diagram placeholder (insert image or link to Visio/draw.io)

---

### Sheet 6: SIEM Storage & Capacity

**Purpose**: Assess storage capacity and growth

**Column Structure** (15 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Storage Component | 25 | Dropdown: Hot Storage, Warm Storage, Cold Storage, Archive, Backup |
| B | Technology | 20 | Dropdown: Local Disk, SAN, NAS, Object Storage (S3/Azure), Tape, Other |
| C | Total Capacity (TB) | 20 | Number |
| D | Used Capacity (TB) | 20 | Number |
| E | Free Capacity (TB) | 20 | Formula: =C-D |
| F | % Used | 12 | Formula: =D/C |
| G | Status | 15 | Formula: >85% Red, >70% Yellow, <70% Green |
| H | Retention Period | 20 | Text: Days/months stored here |
| I | Avg Daily Ingest (GB) | 20 | Number |
| J | Growth Rate %/Month | 20 | Number: Historical trend |
| K | Days Until Full | 15 | Formula: Based on growth rate |
| L | Expansion Plan | 30 | Dropdown: Not Needed, Planned, In Progress, Urgent |
| M | Expansion Date | 15 | Date: When capacity added |
| N | Cost per TB/Month | 20 | Number: For budgeting |
| O | Notes | 40 | Text |

**Data Rows**: 5-15 (storage tiers)

**Capacity Planning Section** (below data, rows 30-40):
- Current total capacity
- Projected capacity need (6 months, 12 months, 24 months)
- Budget required for expansion
- Optimization opportunities (compression, tiering, archival)

---

### Sheet 7: Log Parsing & Normalization

**Purpose**: Assess parsing accuracy and completeness

**Column Structure** (15 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Log Source Type | 25 | Text: Windows, Linux, Firewall, etc. |
| B | Log Format | 20 | Dropdown: Syslog, CEF, JSON, EVTX, Custom |
| C | Parsing Method | 20 | Dropdown: Built-in, Custom Regex, Grok, Logstash Filter, Custom Script |
| D | Parser Status | 15 | Dropdown: Working, Needs Tuning, Broken, Not Configured |
| E | Parse Success Rate % | 20 | Number: 0-100 |
| F | Unparsed Events/Day | 20 | Number |
| G | Fields Extracted | 20 | Number: How many fields |
| H | Required Fields Present | 20 | Dropdown: All, Most, Some, Few |
| I | Timestamp Parsing | 18 | Dropdown: Correct, Incorrect, Missing |
| J | Timezone Handling | 18 | Dropdown: Correct, Incorrect, Unknown |
| K | Last Parser Update | 15 | Date |
| L | Issues Identified | 40 | Text |
| M | Tuning Required | 15 | Dropdown: Yes, No |
| N | Owner | 20 | Text: Responsible for parser |
| O | Notes | 40 | Text |

**Data Rows**: 20-100 (log source types)

**Target**: >95% parse success rate for all sources

---

### Sheet 8: SIEM Performance Metrics

**Purpose**: Track SIEM platform performance

**Column Structure** (14 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Metric Date | 15 | Date: DD.MM.YYYY |
| B | Daily Events Indexed | 20 | Number: Millions |
| C | Peak Events/Second | 20 | Number |
| D | Indexing Lag (minutes) | 20 | Number: Real-time vs. indexed |
| E | Search Performance (sec) | 20 | Number: Avg query time |
| F | Dashboard Load Time (sec) | 20 | Number |
| G | CPU Utilization % | 18 | Number: 0-100 |
| H | Memory Utilization % | 18 | Number: 0-100 |
| I | Disk I/O % | 15 | Number: 0-100 |
| J | Network Throughput (Gbps) | 20 | Number |
| K | Uptime % | 12 | Number: 99.9+ target |
| L | Incidents | 15 | Number: Outages/issues |
| M | Performance Status | 18 | Formula: Green if all metrics healthy |
| N | Notes | 40 | Text |

**Data Rows**: 30-90 (daily metrics for monitoring period)

**Performance Targets**:
- Indexing lag: <5 minutes
- Search performance: <10 seconds for typical query
- CPU/Memory: <80% average utilization
- Uptime: >99.9%

---

### Sheet 9: Data Quality Assessment

**Purpose**: Assess quality of log data in SIEM

**Column Structure** (14 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Quality Dimension | 25 | Dropdown: Completeness, Accuracy, Consistency, Timeliness, Validity |
| B | Log Source Type | 25 | Text |
| C | Assessment Method | 30 | Text: How measured |
| D | Sample Size | 15 | Number: Events checked |
| E | Pass Count | 15 | Number |
| F | Fail Count | 15 | Number |
| G | Quality Score % | 18 | Formula: =E/(E+F) |
| H | Status | 15 | Formula: >95% Green, >80% Yellow, <80% Red |
| I | Common Issues | 40 | Text: What problems found |
| J | Impact | 20 | Dropdown: Critical, High, Medium, Low |
| K | Remediation Action | 40 | Text |
| L | Responsible Party | 25 | Text |
| M | Target Date | 15 | Date |
| N | Notes | 40 | Text |

**Data Rows**: 20-50 (quality checks)

**Quality Dimensions**:
- **Completeness**: All required fields present
- **Accuracy**: Data values correct and meaningful
- **Consistency**: Same events logged same way across sources
- **Timeliness**: Logs indexed within target timeframe
- **Validity**: Data conforms to expected formats

---

### Sheet 10: Gap Analysis & Remediation

**Purpose**: Track collection infrastructure gaps

**Column Structure** (12 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Gap ID | 12 | Auto: GAP-001 |
| B | Gap Category | 25 | Dropdown: Coverage Gap, Reliability Issue, Performance Issue, Parsing Error, Capacity Constraint, Redundancy Gap, DR Gap |
| C | Description | 50 | Text |
| D | Affected Systems | 30 | Text: Count or list |
| E | Impact | 20 | Dropdown: Critical, High, Medium, Low |
| F | Current State | 40 | Text |
| G | Target State | 40 | Text |
| H | Remediation Action | 50 | Text |
| I | Owner | 25 | Text |
| J | Target Date | 15 | Date |
| K | Status | 15 | Dropdown: Open, In Progress, Resolved |
| L | Notes | 40 | Text |

**Data Rows**: Variable (all identified gaps)

---

### Sheet 11: Summary Dashboard

**Section 1: Collection Health Summary** (Rows 3-12):

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Systems Monitored | COUNT formula | N/A | Info |
| Systems Collecting >95% | COUNTIF formula | 100% | Green/Yellow/Red |
| Avg Collection Rate % | AVERAGE formula | >98% | Status |
| Systems with Gaps >4hr | COUNT formula | 0 | Status |
| Parse Success Rate % | AVERAGE formula | >95% | Status |
| SIEM Uptime % | From Sheet 8 | >99.9% | Status |
| Storage Used % | From Sheet 6 | <70% | Status |
| Days Until Storage Full | MIN formula | >90 days | Status |

**Section 2: Collection by System Type** (Rows 14-24):
Bar chart showing collection rates by system type (Server, Network, Security, Application, Cloud)

**Section 3: Performance Trends** (Rows 26-40):
Line chart: Daily events indexed over time (last 30 days)

**Section 4: Top Issues** (Rows 42-55):
- Top 10 systems with lowest collection rates
- Top 10 parsing errors by volume
- Top 5 capacity constraints

**Section 5: Gap Summary** (Rows 57-65):

| Priority | Open | In Progress | Resolved | Overdue |
|----------|------|-------------|----------|---------|
| Critical | COUNT | COUNT | COUNT | COUNT |
| High | COUNT | COUNT | COUNT | COUNT |
| Medium | COUNT | COUNT | COUNT | COUNT |
| Low | COUNT | COUNT | COUNT | COUNT |

**Section 6: Recommendations** (Rows 67-80):
Pre-populated based on assessment findings

---

### Sheet 12: Approval & Sign-Off

**Approval Table**:

| Role | Name | Date | Signature | Status |
|------|------|------|-----------|--------|
| Log Administrator | [Name] | DD.MM.YYYY | _____ | [ ] Reviewed |
| SOC Lead | [Name] | DD.MM.YYYY | _____ | [ ] Reviewed |
| IT Operations Manager | [Name] | DD.MM.YYYY | _____ | [ ] Reviewed |
| Information Security Manager | [Name] | DD.MM.YYYY | _____ | [ ] Approved |

---

## File Naming Convention

**Filename**: `ISMS-IMP-A_8_15_2_Log_Collection_Centralization_YYYYMMDD.xlsx`

---

**END OF IMP SPECIFICATION A.8.15.2**

# ISMS-IMP-A.8.15.3
## Log Protection & Retention Assessment
### Excel Workbook Layout Specification

**Document ID**: ISMS-IMP-A.8.15.3  
**Assessment Area**: Log Protection, Integrity, and Retention Compliance  
**Related Policy**: ISMS-POL-A.8.15-S2.2 (Protection), S2.3 (Retention)  
**Purpose**: Assess log protection mechanisms and retention compliance  
**Python Generator**: `generate_a815_3_log_protection_retention.py`

---

## Workbook Structure

### Sheet 1: Instructions & Legend

**Header**: "Log Protection & Retention Assessment - ISO/IEC 27001:2022 Control A.8.15"

**Document Information Block**:
```
Document ID:           ISMS-IMP-A.8.15.3
Assessment Area:       Log Protection & Retention
Related Policy:        ISMS-POL-A.8.15-S2.2, S2.3
Version:               1.0
Assessment Date:       [USER INPUT]
Completed By:          [USER INPUT]
Organization:          [USER INPUT]
Review Cycle:          Semi-annual
```

---

### Sheet 2: Access Control Assessment

**Purpose**: Assess log access controls per S2.2.2

**Column Structure** (16 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Log Source / SIEM Component | 30 | Text |
| B | Access Control Type | 20 | Dropdown: RBAC, ACL, None, Other |
| C | Authentication Required | 18 | Dropdown: Yes, No |
| D | Authorization Model | 20 | Dropdown: Role-Based, User-Based, Group-Based, None |
| E | Read Access Controlled | 18 | Dropdown: Yes, No, Partial |
| F | Write Access Prevented | 20 | Dropdown: Yes (read-only), No, Partial |
| G | Delete Access Controlled | 20 | Dropdown: Yes (restricted), No |
| H | Admin Separation | 20 | Dropdown: Yes (separated), No, N/A |
| I | Access Logged (Meta-logging) | 20 | Dropdown: Yes, No |
| J | MFA Required for Admin | 20 | Dropdown: Yes, No, N/A |
| K | Last Access Review Date | 18 | Date: DD.MM.YYYY |
| L | Access Review Frequency | 20 | Dropdown: Quarterly, Semi-annual, Annual, None |
| M | Non-Compliance Issues | 40 | Text |
| N | Compliance Score | 15 | Formula: Based on Yes/No answers |
| O | Remediation Required | 18 | Dropdown: Yes, No |
| P | Notes | 40 | Text |

**Data Rows**: 20-100

**Target**: 100% compliance for critical logs (P1/P2 systems)

---

### Sheet 3: Integrity Protection Mechanisms

**Purpose**: Assess integrity protection per S2.2.4

**Column Structure** (17 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Log Source / Storage | 30 | Text |
| B | Log Criticality | 18 | Dropdown: Critical, High, Medium, Low |
| C | Write-Once Storage (WORM) | 20 | Dropdown: Yes, No, N/A |
| D | WORM Technology | 25 | Dropdown: Hardware WORM, Software WORM, Cloud Object Lock, None |
| E | Cryptographic Hashing | 20 | Dropdown: Yes, No |
| F | Hash Algorithm | 18 | Dropdown: SHA-256, SHA-512, MD5 (weak), None |
| G | Hash Storage Location | 25 | Text: Separate from logs? |
| H | Digital Signatures | 18 | Dropdown: Yes, No |
| I | File Sealing | 18 | Dropdown: Yes, No, N/A |
| J | Integrity Check Frequency | 20 | Dropdown: Daily, Weekly, Monthly, None |
| K | Last Integrity Check | 18 | Date: DD.MM.YYYY |
| L | Tampering Detected | 18 | Dropdown: Never, Historical, Recent |
| M | Backup Protected | 18 | Dropdown: Yes, No |
| N | Compliance with Policy | 20 | Formula: Based on requirements |
| O | Gap Description | 40 | Text |
| P | Remediation Plan | 40 | Text |
| Q | Notes | 40 | Text |

**Data Rows**: 20-100

**Minimum Requirements by Criticality**:
- **Critical**: WORM + Hashing + Daily integrity checks
- **High**: Hashing + Weekly integrity checks  
- **Medium**: Access controls + Monthly integrity checks
- **Low**: Basic access controls

---

### Sheet 4: Secure Transmission Assessment

**Purpose**: Assess log transmission security per S2.2.3

**Column Structure** (14 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Source System | 30 | Text |
| B | Destination (SIEM) | 25 | Text |
| C | Transport Protocol | 20 | Dropdown: TLS, TCP, UDP, HTTPS, Other |
| D | Encryption in Transit | 18 | Dropdown: Yes (TLS), No |
| E | TLS Version | 15 | Dropdown: TLS 1.3, TLS 1.2, TLS 1.1 (weak), TLS 1.0 (weak), None |
| F | Certificate Validation | 20 | Dropdown: Yes, No, N/A |
| G | Network Segment | 20 | Dropdown: Isolated Mgmt Network, Internal Network, Internet, DMZ |
| H | Firewall Protection | 18 | Dropdown: Yes, No |
| I | Source Authentication | 20 | Dropdown: Yes (mutual TLS/certs), No |
| J | Vulnerability Risk | 18 | Dropdown: None, Low, Medium, High |
| K | Compliance Status | 18 | Formula: TLS 1.2+ on untrusted = compliant |
| L | Remediation Required | 18 | Dropdown: Yes, No |
| M | Target Date | 15 | Date: If remediation needed |
| N | Notes | 40 | Text |

**Data Rows**: 50-200

**Policy Requirement**: TLS for transmission across untrusted networks

---

### Sheet 5: Retention Period Compliance

**Purpose**: Assess retention period compliance per S2.3.2

**Column Structure** (18 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Log Source / Type | 30 | Text |
| B | Log Category | 20 | Dropdown: Security, Authentication, Admin, Application, System, Network, Database |
| C | Regulatory Requirement | 25 | Dropdown: PCI DSS, HIPAA, SOX, GDPR, ISO 27001, None |
| D | Policy Retention (months) | 20 | Number: Per S2.3 |
| E | Hot Storage Period (months) | 22 | Number: Actual current |
| F | Warm Storage Period (months) | 22 | Number: Actual |
| G | Cold Storage Period (years) | 20 | Number: Actual |
| H | Total Retention (months) | 20 | Formula: Sum of periods |
| I | Meets Policy Requirement | 20 | Formula: Total >= Policy |
| J | Retention Gap (months) | 20 | Formula: Policy - Total (if negative) |
| K | Over-Retention (months) | 20 | Formula: Total - Policy (if excessive) |
| L | Automated Disposal | 18 | Dropdown: Yes, No |
| M | Last Disposal Date | 18 | Date: DD.MM.YYYY |
| N | Legal Hold Capability | 18 | Dropdown: Yes, No |
| O | Compliance Status | 18 | Formula: Green if meets requirement |
| P | Remediation Action | 40 | Text: If non-compliant |
| Q | Target Date | 15 | Date |
| R | Notes | 40 | Text |

**Data Rows**: 30-100 (log types)

**Quick Reference Table** (below data):
Standard retention periods by log type (from S2.3.2.3)

---

### Sheet 6: Storage Tier Implementation

**Purpose**: Assess tiered storage implementation per S2.3.3

**Column Structure** (15 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Storage Tier | 20 | Dropdown: Hot, Warm, Cold |
| B | Technology | 25 | Dropdown: Local Disk/SSD, SAN, NAS, Object Storage, Tape, Other |
| C | Capacity (TB) | 15 | Number |
| D | Used (TB) | 15 | Number |
| E | % Used | 12 | Formula |
| F | Retention Period | 20 | Text: What's stored here |
| G | Access Performance | 20 | Dropdown: Real-time (<1 min), Fast (<15 min), Slow (hours), Very Slow (days) |
| H | Encryption at Rest | 18 | Dropdown: Yes, No |
| I | Encryption Method | 20 | Dropdown: AES-256, AES-128, None |
| J | Geographic Location | 25 | Text: Data center, cloud region |
| K | Redundancy | 20 | Dropdown: None, Local (RAID), Remote (Replication), Both |
| L | Backup Implemented | 18 | Dropdown: Yes, No |
| M | Meets Policy Requirements | 20 | Formula: Based on tier expectations |
| N | Issues | 40 | Text |
| O | Notes | 40 | Text |

**Data Rows**: 3-10 (storage tiers per system)

**Tiering Assessment**:
- Is 3-tier model implemented (hot/warm/cold)?
- Are transitions automated?
- Are retention periods matched to tiers?

---

### Sheet 7: Log Backup & Recovery

**Purpose**: Assess backup and recovery capabilities per S2.2.7

**Column Structure** (16 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Backup Scope | 30 | Dropdown: All Logs, Hot Storage Only, Critical Logs Only, None |
| B | Backup Frequency | 20 | Dropdown: Daily, Weekly, Monthly |
| C | Backup Technology | 25 | Text: Product/solution |
| D | Backup Location | 30 | Dropdown: Same Site, Offsite, Cloud, Multiple |
| E | Backup Encrypted | 18 | Dropdown: Yes, No |
| F | Encryption Algorithm | 20 | Dropdown: AES-256, AES-128, None |
| G | Backup Integrity Verified | 20 | Dropdown: Yes (periodic), Yes (always), No |
| H | Last Backup Date | 18 | Date: DD.MM.YYYY |
| I | Last Restore Test Date | 18 | Date: DD.MM.YYYY |
| J | Restore Test Frequency | 20 | Dropdown: Quarterly, Semi-annual, Annual, Never |
| K | Last Restore Success | 18 | Dropdown: Yes, No, Not Tested |
| L | RTO (Recovery Time Objective) | 20 | Text: Hours/days |
| M | RPO (Recovery Point Objective) | 20 | Text: Hours/days of data loss acceptable |
| N | Backup Retention Period | 20 | Text: How long backups kept |
| O | Compliance Status | 18 | Formula |
| P | Notes | 40 | Text |

**Data Rows**: 5-20 (backup configurations)

**Minimum Requirements**:
- Daily backups for critical logs
- Offsite/separate location storage
- Quarterly restore testing

---

### Sheet 8: Disposal Procedures

**Purpose**: Assess secure disposal practices per S2.3.5

**Column Structure** (14 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Log Type / Source | 30 | Text |
| B | Retention Period Expired | 20 | Date: When eligible for disposal |
| C | Automated Disposal | 18 | Dropdown: Yes, No |
| D | Disposal Method | 25 | Dropdown: Cryptographic Erasure, Multi-pass Overwrite, Physical Destruction, Deletion |
| E | Disposal Approval Required | 22 | Dropdown: Yes (manual), No (automated), N/A |
| F | Legal Hold Check | 18 | Dropdown: Yes (checked), No, N/A |
| G | Disposal Logged | 18 | Dropdown: Yes, No |
| H | Last Disposal Date | 18 | Date: DD.MM.YYYY |
| I | Volume Disposed (GB) | 20 | Number |
| J | Disposal Verification | 20 | Dropdown: Verified, Not Verified |
| K | Compliance with Policy | 20 | Formula |
| L | Issues | 40 | Text |
| M | Remediation | 40 | Text |
| N | Notes | 40 | Text |

**Data Rows**: 20-50

**Key Checks**:
- No premature disposal (before retention period)
- Legal hold respected
- Disposal logged (meta-logging)
- Secure disposal methods used

---

### Sheet 9: Separation of Duties

**Purpose**: Assess separation of duties per S2.2.6

**Column Structure** (14 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | System / Component | 30 | Text |
| B | System Administrator(s) | 30 | Text: Names/roles |
| C | Log Administrator(s) | 30 | Text: Names/roles |
| D | Roles Separated | 18 | Dropdown: Yes (different people), No (same people), Partial |
| E | Sys Admin Can Modify Logs | 25 | Dropdown: No (compliant), Yes (violation), Limited |
| F | Compensating Controls | 40 | Text: If separation not feasible |
| G | Break-Glass Procedure | 20 | Dropdown: Yes (documented), No |
| H | Break-Glass Usage Logged | 22 | Dropdown: Yes, No, N/A |
| I | Independent Review | 20 | Dropdown: Yes, No, Frequency |
| J | Last Review Date | 18 | Date |
| K | Violations Detected | 18 | Dropdown: None, Historical, Recent |
| L | Compliance Status | 18 | Formula |
| M | Remediation Plan | 40 | Text |
| N | Notes | 40 | Text |

**Data Rows**: 20-50

**Critical Assessment**: Systems with poor separation are HIGH RISK

---

### Sheet 10: Legal Hold Management

**Purpose**: Track legal holds per S2.3.6

**Column Structure** (13 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Hold ID | 15 | Auto: HOLD-001 |
| B | Hold Name / Matter | 30 | Text: Case name |
| C | Initiation Date | 15 | Date: DD.MM.YYYY |
| D | Initiated By | 25 | Text: Legal counsel name |
| E | Scope Description | 40 | Text: What logs covered |
| F | Systems/Sources Affected | 30 | Text |
| G | Date Range | 20 | Text: From date to date |
| H | Hold Status | 15 | Dropdown: Active, Released, Suspended |
| I | Review Date | 15 | Date: Quarterly review |
| J | Disposal Prevented | 18 | Dropdown: Yes (verified), No |
| K | Release Date | 15 | Date: If released |
| L | Release Authorized By | 25 | Text |
| M | Notes | 40 | Text |

**Data Rows**: Variable (active legal holds)

**Compliance Check**: Verify no logs under hold have been disposed

---

### Sheet 11: Gap Analysis

**Purpose**: Consolidated protection & retention gaps

**Column Structure** (12 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Gap ID | 12 | Auto: GAP-001 |
| B | Gap Category | 25 | Dropdown: Access Control, Integrity Protection, Transmission Security, Retention Non-Compliance, Backup, Disposal, Separation of Duties, Other |
| C | Description | 50 | Text |
| D | Affected Systems | 30 | Text |
| E | Policy Requirement | 30 | Text: S2.2.x or S2.3.x reference |
| F | Risk Level | 15 | Dropdown: Critical, High, Medium, Low |
| G | Remediation Action | 50 | Text |
| H | Owner | 25 | Text |
| I | Target Date | 15 | Date |
| J | Budget Required | 15 | Dropdown: Yes, No |
| K | Status | 15 | Dropdown: Open, In Progress, Resolved |
| L | Notes | 40 | Text |

---

### Sheet 12: Summary Dashboard

**Section 1: Protection Compliance Summary** (Rows 3-15):

| Protection Measure | Compliant Count | Non-Compliant | % Compliant | Target |
|-------------------|-----------------|---------------|-------------|--------|
| Access Controls | COUNTIF | COUNTIF | Formula | 100% |
| Integrity Protection | COUNTIF | COUNTIF | Formula | >95% |
| Secure Transmission | COUNTIF | COUNTIF | Formula | 100% (critical) |
| Backup Implemented | COUNTIF | COUNTIF | Formula | >95% |
| Separation of Duties | COUNTIF | COUNTIF | Formula | >90% |

**Section 2: Retention Compliance Summary** (Rows 17-25):

| Log Category | Compliant | Under-Retained | Over-Retained | % Compliant |
|--------------|-----------|----------------|---------------|-------------|
| Security | COUNT | COUNT | COUNT | Formula |
| Authentication | COUNT | COUNT | COUNT | Formula |
| Administrative | COUNT | COUNT | COUNT | Formula |
| Application | COUNT | COUNT | COUNT | Formula |
| Overall | TOTAL | TOTAL | TOTAL | Formula |

**Section 3: Gap Summary by Risk** (Rows 27-35):

| Risk Level | Open Gaps | In Progress | Resolved | Overdue |
|------------|-----------|-------------|----------|---------|
| Critical | COUNT | COUNT | COUNT | COUNT |
| High | COUNT | COUNT | COUNT | COUNT |
| Medium | COUNT | COUNT | COUNT | COUNT |
| Low | COUNT | COUNT | COUNT | COUNT |

**Section 4: Charts** (Rows 37-60):
- Compliance status pie chart (Compliant, Partial, Non-Compliant)
- Retention period distribution (How many logs in each retention bucket)
- Protection mechanisms in use (WORM, Hashing, etc.)

**Section 5: Key Findings & Recommendations** (Rows 62-80)

---

### Sheet 13: Approval & Sign-Off

**Approval Table**:

| Role | Name | Date | Signature | Status |
|------|------|------|-----------|--------|
| Log Administrator | [Name] | DD.MM.YYYY | _____ | [ ] Reviewed |
| IT Operations Manager | [Name] | DD.MM.YYYY | _____ | [ ] Reviewed |
| Information Security Manager | [Name] | DD.MM.YYYY | _____ | [ ] Approved |
| Legal/Compliance Officer | [Name] | DD.MM.YYYY | _____ | [ ] Reviewed |

---

## File Naming Convention

**Filename**: `ISMS-IMP-A_8_15_3_Log_Protection_Retention_YYYYMMDD.xlsx`

---

**END OF IMP SPECIFICATION A.8.15.3**

# ISMS-IMP-A.8.15.4
## Log Analysis & Review Assessment
### Excel Workbook Layout Specification

**Document ID**: ISMS-IMP-A.8.15.4  
**Assessment Area**: Log Review, Analysis, and Detection Effectiveness  
**Related Policy**: ISMS-POL-A.8.15-S2.4 (Log Review & Analysis)  
**Purpose**: Assess log analysis capabilities and review process effectiveness  
**Python Generator**: `generate_a815_4_log_analysis_review.py`

---

## Workbook Structure

### Sheet 1: Instructions & Legend

**Header**: "Log Analysis & Review Assessment - ISO/IEC 27001:2022 Control A.8.15"

**Document Information Block**:
```
Document ID:           ISMS-IMP-A.8.15.4
Assessment Area:       Log Analysis & Review
Related Policy:        ISMS-POL-A.8.15-S2.4
Version:               1.0
Assessment Date:       [USER INPUT]
Assessment Period:     [USER INPUT - e.g., Q4 2025]
Completed By:          [USER INPUT]
Organization:          [USER INPUT]
Review Cycle:          Quarterly
```

**How to Use**:
1. Document review schedule compliance (daily/weekly/monthly)
2. Track detection use cases and effectiveness
3. Assess alert quality and false positive rates
4. Record incident detection metrics
5. Evaluate SOC analyst performance
6. Track investigation completeness
7. Review dashboard for effectiveness summary

---

### Sheet 2: Review Schedule Compliance

**Purpose**: Track compliance with required review schedule per S2.4.1-2

**Column Structure** (15 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Review Period | 20 | Date Range: Week of DD.MM.YYYY |
| B | Review Type | 18 | Dropdown: Daily, Weekly, Monthly |
| C | Scheduled Date | 15 | Date: DD.MM.YYYY |
| D | Actual Date | 15 | Date: DD.MM.YYYY |
| E | Completed On Time | 18 | Formula: =IF(D<=C,"Yes","Late") |
| F | Reviewer Name | 25 | Dropdown: List of authorized reviewers |
| G | Time Spent (minutes) | 20 | Number |
| H | Logs Reviewed | 30 | Text: Which log sources |
| I | Findings Count | 18 | Number: Issues identified |
| J | Incidents Created | 18 | Number: Tickets opened |
| K | False Positives | 18 | Number |
| L | Documentation Complete | 20 | Dropdown: Yes, Partial, No |
| M | Escalations Made | 18 | Number |
| N | Review Quality Score | 20 | Formula: Based on completeness |
| O | Notes | 40 | Text |

**Data Rows**: 60-180 (quarterly = ~90 daily reviews + 12 weekly + 3 monthly)

**Compliance Targets**:
- Daily reviews: 100% completion (Mon-Fri or 7 days/week)
- Weekly reviews: 100% completion
- Monthly reviews: 100% completion

**Metrics to Calculate**:
- % reviews completed on time
- Average time per review type
- Average findings per review

---

### Sheet 3: Detection Use Cases Inventory

**Purpose**: Document all detection use cases per S2.4.3.3

**Column Structure** (18 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Use Case ID | 15 | Auto: UC-001, UC-002 |
| B | Use Case Name | 30 | Text |
| C | Threat Category | 25 | Dropdown: Authentication Attack, Privilege Abuse, Data Exfiltration, Malware, Policy Violation, System Anomaly, Other |
| D | MITRE ATT&CK Technique | 25 | Text: T1078, T1566, etc. |
| E | Data Sources Required | 30 | Text: Log types needed |
| F | Detection Logic | 50 | Text: How it detects |
| G | Detection Method | 25 | Dropdown: Correlation Rule, Threshold, Anomaly Detection, Signature, ML/AI, Manual Query |
| H | Alert Severity | 15 | Dropdown: Critical, High, Medium, Low, Info |
| I | Status | 15 | Dropdown: Active, Testing, Disabled, Retired |
| J | Implemented Date | 15 | Date: DD.MM.YYYY |
| K | Last Tuned Date | 15 | Date: DD.MM.YYYY |
| L | True Positives (30d) | 20 | Number |
| M | False Positives (30d) | 20 | Number |
| N | False Positive Rate % | 20 | Formula: =M/(L+M) |
| O | Effectiveness Rating | 20 | Dropdown: Excellent, Good, Fair, Poor |
| P | Owner | 25 | Text: Who maintains this |
| Q | Next Review Date | 15 | Date |
| R | Notes | 40 | Text |

**Data Rows**: 50-200 (use cases)

**Recommended Minimum Use Cases** (from S2.4.3.3):
- Failed authentication threshold (10+ failures in 1 hour)
- Privileged account usage outside business hours
- New user account creation
- Unusual data access volume
- Malware detection
- Critical system configuration changes

---

### Sheet 4: Alert Quality Analysis

**Purpose**: Analyze alert effectiveness and false positive rates

**Column Structure** (16 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Alert Source / Rule Name | 30 | Text |
| B | Alert Type | 25 | Dropdown: Security, Operational, Compliance, Performance |
| C | Severity | 15 | Dropdown: Critical, High, Medium, Low |
| D | Total Alerts (30d) | 20 | Number |
| E | True Positives | 18 | Number |
| F | False Positives | 18 | Number |
| G | Unreviewed | 15 | Number |
| H | True Positive Rate % | 20 | Formula: =E/D |
| I | False Positive Rate % | 20 | Formula: =F/D |
| J | Alert Quality Score | 20 | Formula: TP/(TP+FP) - target >50% |
| K | Status | 15 | Formula: Green if >50%, Yellow 20-50%, Red <20% |
| L | Average Investigation Time | 22 | Number: Minutes |
| M | Tuning Required | 18 | Dropdown: Yes (urgent), Yes, No |
| N | Tuning Action | 40 | Text: How to improve |
| O | Last Tuned | 15 | Date |
| P | Notes | 40 | Text |

**Data Rows**: 50-200 (alert sources)

**Analysis Section** (below data):
- Top 10 worst performers (highest false positive rate)
- Top 10 by volume (most alerts generated)
- Alerts requiring immediate tuning (FP rate >50%)

**Target Alert Quality**:
- Critical alerts: >80% true positive rate
- High alerts: >60% true positive rate
- Medium alerts: >50% true positive rate
- Overall: <10% false positive rate

---

### Sheet 5: Incident Detection Metrics

**Purpose**: Track security incident detection effectiveness

**Column Structure** (17 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Incident ID | 15 | Text: INC-2025-001 |
| B | Detection Date | 15 | Date: DD.MM.YYYY |
| C | Incident Type | 25 | Dropdown: Malware, Intrusion, Data Breach, Policy Violation, Unauthorized Access, Other |
| D | Severity | 15 | Dropdown: Critical, High, Medium, Low |
| E | Detected By | 25 | Dropdown: Automated Alert, Manual Review, User Report, External Notification |
| F | Detection Method | 25 | Dropdown: SIEM Rule, Anomaly Detection, Threat Intelligence, Manual Query |
| G | Incident Occurred Date | 18 | Date: When attack happened |
| H | Time to Detect (hours) | 20 | Formula: =A-G (MTTD) |
| I | Response Start Time | 18 | Datetime |
| J | Time to Respond (hours) | 20 | Formula: =I-A (MTTR) |
| K | Containment Time | 18 | Datetime |
| L | Time to Contain (hours) | 20 | Formula: =K-I |
| M | Resolution Date | 15 | Date |
| N | Total Resolution Time | 20 | Formula: =M-A |
| O | Investigation Complete | 18 | Dropdown: Yes, No, In Progress |
| P | Lessons Learned Captured | 22 | Dropdown: Yes, No |
| Q | Notes | 40 | Text |

**Data Rows**: Variable (all incidents in assessment period)

**Metrics to Calculate**:
- **Mean Time to Detect (MTTD)**: Average of column H
- **Mean Time to Respond (MTTR)**: Average of column J
- **Mean Time to Contain**: Average of column L
- **Detection by Method**: COUNT by detection method

**Targets** (from S2.4.8):
- MTTD: <1 hour (critical), <24 hours (high)
- MTTR: <4 hours (critical), <24 hours (high)

---

### Sheet 6: Investigation Quality Assessment

**Purpose**: Assess investigation thoroughness per S2.4.6

**Column Structure** (16 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Incident ID | 15 | Text (links to Sheet 5) |
| B | Investigator | 25 | Text: Name |
| C | Timeline Documented | 18 | Dropdown: Yes, No, Partial |
| D | Root Cause Identified | 20 | Dropdown: Yes, No, Unknown |
| E | Scope Assessed | 18 | Dropdown: Complete, Partial, None |
| F | Evidence Collected | 18 | Dropdown: Complete, Partial, None |
| G | Logs Analyzed | 30 | Text: Which sources reviewed |
| H | IOCs Documented | 18 | Dropdown: Yes, No, N/A |
| I | Actions Documented | 18 | Dropdown: Complete, Partial, None |
| J | Report Completeness | 20 | Dropdown: Complete, Partial, Incomplete |
| K | Lessons Learned | 18 | Dropdown: Yes, No |
| L | Post-Incident Review Done | 22 | Dropdown: Yes, No, Scheduled |
| M | Investigation Quality Score | 22 | Formula: % of Yes answers |
| N | Status | 15 | Formula: Green >80%, Yellow >60%, Red <60% |
| O | Improvement Areas | 40 | Text |
| P | Notes | 40 | Text |

**Data Rows**: Variable (matches incidents from Sheet 5)

**Quality Targets**:
- Investigation completeness: >90% for Critical/High incidents
- Root cause identification: >80% overall
- Documentation completeness: 100% for all incidents

---

### Sheet 7: SOC Analyst Performance

**Purpose**: Track SOC analyst workload and effectiveness

**Column Structure** (16 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Analyst Name | 25 | Text |
| B | Role | 20 | Dropdown: Tier 1, Tier 2, Tier 3, Lead |
| C | Assessment Period | 20 | Text: Month/Quarter |
| D | Shifts Worked | 15 | Number |
| E | Alerts Reviewed | 18 | Number |
| F | Alerts per Shift | 18 | Formula: =E/D |
| G | Incidents Investigated | 20 | Number |
| H | Incidents Escalated | 20 | Number |
| I | True Positives Identified | 22 | Number |
| J | False Positives Flagged | 22 | Number |
| K | Accuracy Rate % | 18 | Formula: =I/(I+J) |
| L | Avg Investigation Time (min) | 25 | Number |
| M | Reviews Completed On Time | 22 | Number / Total |
| N | Training Hours | 18 | Number |
| O | Performance Rating | 20 | Dropdown: Exceeds, Meets, Needs Improvement |
| P | Notes | 40 | Text |

**Data Rows**: 5-20 (SOC analysts)

**Performance Benchmarks**:
- Alerts per shift: 20-50 (depends on alert quality)
- Accuracy rate: >85%
- On-time reviews: >95%
- Training: Minimum 8 hours per quarter

---

### Sheet 8: Anomaly Detection Assessment

**Purpose**: Assess behavioral analytics and anomaly detection per S2.4.4

**Column Structure** (15 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Anomaly Detection Type | 30 | Dropdown: User Behavior, System Behavior, Network Behavior, Data Access Patterns |
| B | Implementation Status | 20 | Dropdown: Implemented, Testing, Planned, Not Implemented |
| C | Technology Used | 25 | Dropdown: SIEM Native, UEBA Tool, Custom Script, ML/AI Platform, None |
| D | Baseline Established | 18 | Dropdown: Yes, No, In Progress |
| E | Baseline Period (days) | 20 | Number: 30-90 days typical |
| F | Last Baseline Update | 18 | Date: DD.MM.YYYY |
| G | Anomalies Detected (30d) | 22 | Number |
| H | True Anomalies | 18 | Number: Actual issues |
| I | False Positives | 18 | Number |
| J | Detection Accuracy % | 20 | Formula: =H/G |
| K | Actionable Alerts | 18 | Number: Led to investigation |
| L | Value Rating | 15 | Dropdown: High, Medium, Low, None |
| M | Tuning Required | 18 | Dropdown: Yes, No |
| N | Next Review Date | 15 | Date |
| O | Notes | 40 | Text |

**Data Rows**: 10-30 (anomaly detection methods)

**Assessment Questions**:
- Are behavioral baselines established?
- Are baselines updated regularly?
- Is anomaly detection providing value?
- What's the false positive rate?

---

### Sheet 9: Threat Intelligence Integration

**Purpose**: Assess threat intelligence usage per S2.4.9.2

**Column Structure** (14 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Threat Feed Name | 30 | Text |
| B | Feed Type | 25 | Dropdown: Commercial, Government, Open Source, Industry ISAC, Internal |
| C | Feed Category | 25 | Dropdown: IOC (IP/Domain/Hash), Vulnerability, Threat Actor, Campaign, General |
| D | Integration Method | 25 | Dropdown: SIEM Native, API, Manual Import, TAXII/STIX, Other |
| E | Update Frequency | 20 | Dropdown: Real-time, Hourly, Daily, Weekly |
| F | Last Update | 15 | Date: DD.MM.YYYY |
| G | IOCs Active | 18 | Number: Currently in SIEM |
| H | Matches (30d) | 18 | Number: Hits on IOCs |
| I | True Positives | 18 | Number |
| J | False Positives | 18 | Number |
| K | Feed Quality Score | 20 | Formula: TP/(TP+FP) |
| L | Status | 15 | Dropdown: Active, Inactive, Evaluating |
| M | Value Assessment | 20 | Dropdown: High, Medium, Low, None |
| N | Notes | 40 | Text |

**Data Rows**: 5-20 (threat feeds)

**Key Questions**:
- Are threat feeds integrated into detection?
- Are IOCs being matched against logs?
- Which feeds provide most value?
- Are false positives from feeds managed?

---

### Sheet 10: Detection Coverage Matrix

**Purpose**: Map detection coverage to MITRE ATT&CK framework

**Column Structure** (14 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | ATT&CK Tactic | 25 | Dropdown: Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Exfiltration, C2, Impact |
| B | ATT&CK Technique | 30 | Text: T#### - Technique name |
| C | Technique Relevance | 20 | Dropdown: High, Medium, Low, N/A |
| D | Detection Implemented | 20 | Dropdown: Yes, Partial, No |
| E | Detection Method | 25 | Dropdown: SIEM Rule, Anomaly, Signature, Manual, None |
| F | Use Case ID | 15 | Text: Links to Sheet 3 |
| G | Log Sources Required | 30 | Text |
| H | Log Sources Available | 30 | Text |
| I | Coverage Gap | 18 | Dropdown: None, Partial, Complete |
| J | Detection Tested | 18 | Dropdown: Yes, No |
| K | Last Test Date | 15 | Date |
| L | Priority | 15 | Dropdown: Critical, High, Medium, Low |
| M | Remediation Plan | 40 | Text: If gap exists |
| N | Notes | 40 | Text |

**Data Rows**: 100-200 (MITRE techniques)

**Coverage Analysis**:
- % of high-relevance techniques with detection
- % of techniques with complete coverage
- Priority gaps requiring detection development

---

### Sheet 11: Review Process Effectiveness

**Purpose**: Assess overall review process quality

**Column Structure** (13 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Process Element | 30 | Dropdown: Daily Review, Weekly Review, Monthly Review, Alert Triage, Investigation, Documentation, Escalation, Training, Tools |
| B | Process Owner | 25 | Text: Role responsible |
| C | Process Documented | 18 | Dropdown: Yes, No, Partial |
| D | Staff Trained | 18 | Dropdown: All, Most, Some, None |
| E | Tools Adequate | 18 | Dropdown: Yes, No, Partial |
| F | Process Followed | 18 | Dropdown: Always, Usually, Sometimes, Rarely |
| G | Quality Score | 15 | Number: 1-5 rating |
| H | Effectiveness Rating | 20 | Dropdown: Excellent, Good, Fair, Poor |
| I | Issues Identified | 40 | Text |
| J | Improvement Actions | 40 | Text |
| K | Action Owner | 25 | Text |
| L | Target Date | 15 | Date |
| M | Notes | 40 | Text |

**Data Rows**: 10-20 (process elements)

---

### Sheet 12: Gap Analysis

**Purpose**: Consolidated gaps in analysis and review

**Column Structure** (12 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Gap ID | 12 | Auto: GAP-001 |
| B | Gap Category | 25 | Dropdown: Review Process, Detection Coverage, Alert Quality, Investigation Quality, Tools/Technology, Staffing, Training, Documentation |
| C | Description | 50 | Text |
| D | Impact | 20 | Dropdown: Critical, High, Medium, Low |
| E | Current State | 40 | Text |
| F | Target State | 40 | Text |
| G | Remediation Action | 50 | Text |
| H | Owner | 25 | Text |
| I | Target Date | 15 | Date |
| J | Budget Required | 18 | Dropdown: Yes, No |
| K | Status | 15 | Dropdown: Open, In Progress, Resolved |
| L | Notes | 40 | Text |

---

### Sheet 13: Summary Dashboard

**Section 1: Review Compliance Summary** (Rows 3-12):

| Review Type | Required Count | Completed | On Time % | Avg Time | Target |
|-------------|----------------|-----------|-----------|----------|--------|
| Daily | Formula (business days) | COUNT | Formula | AVG | 100% |
| Weekly | Formula (weeks in period) | COUNT | Formula | AVG | 100% |
| Monthly | Formula (months) | COUNT | Formula | AVG | 100% |
| Overall | SUM | SUM | Formula | N/A | 100% |

**Section 2: Detection Effectiveness** (Rows 14-25):

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Use Cases | COUNT(Sheet3) | N/A | Info |
| Active Use Cases | COUNTIF(Sheet3, "Active") | N/A | Info |
| Avg False Positive Rate | AVERAGE(Sheet3) | <10% | Status |
| True Positive Rate | Formula | >50% | Status |
| Use Cases Needing Tuning | COUNT | 0 | Status |
| Detection Coverage % | From Sheet 10 | >90% | Status |
| MTTD - Critical (hours) | AVG(Sheet5) | <1 | Status |
| MTTR - Critical (hours) | AVG(Sheet5) | <4 | Status |

**Section 3: Alert Quality Summary** (Rows 27-38):

| Severity | Total Alerts | True Pos | False Pos | FP Rate % | Quality Score |
|----------|--------------|----------|-----------|-----------|---------------|
| Critical | SUM | SUM | SUM | Formula | Formula |
| High | SUM | SUM | SUM | Formula | Formula |
| Medium | SUM | SUM | SUM | Formula | Formula |
| Low | SUM | SUM | SUM | Formula | Formula |
| Total | SUM | SUM | SUM | Formula | Formula |

**Section 4: Incident Metrics** (Rows 40-50):

| Incident Type | Count | Avg MTTD | Avg MTTR | Detection Method (most common) |
|---------------|-------|----------|----------|-------------------------------|
| Malware | COUNT | AVG | AVG | MODE |
| Intrusion | COUNT | AVG | AVG | MODE |
| Data Breach | COUNT | AVG | AVG | MODE |
| Policy Violation | COUNT | AVG | AVG | MODE |
| Other | COUNT | AVG | AVG | MODE |

**Section 5: Charts** (Rows 52-75):
- Alert volume trend (last 90 days)
- False positive rate trend
- Detection coverage heat map (MITRE ATT&CK)
- Incident detection time distribution

**Section 6: Top Gaps** (Rows 77-90):
Top 10 gaps from Sheet 12 by impact

**Section 7: Recommendations** (Rows 92-105):
Key improvement recommendations

---

### Sheet 14: Approval & Sign-Off

**Approval Table**:

| Role | Name | Date | Signature | Status |
|------|------|------|-----------|--------|
| SOC Lead | [Name] | DD.MM.YYYY | _____ | [ ] Reviewed |
| Security Engineers | [Names] | DD.MM.YYYY | _____ | [ ] Reviewed |
| Information Security Manager | [Name] | DD.MM.YYYY | _____ | [ ] Approved |

---

## File Naming Convention

**Filename**: `ISMS-IMP-A_8_15_4_Log_Analysis_Review_YYYYMMDD.xlsx`

---

**END OF IMP SPECIFICATION A.8.15.4**

# ISMS-IMP-A.8.15.5
## Logging Compliance Dashboard
### Excel Workbook Layout Specification

**Document ID**: ISMS-IMP-A.8.15.5  
**Assessment Area**: Overall Logging Program Compliance Dashboard  
**Related Policy**: All ISMS-POL-A.8.15 sections  
**Purpose**: Executive summary dashboard consolidating all logging assessments  
**Python Generator**: `generate_a815_5_compliance_dashboard.py`

---

## Workbook Structure

### Sheet 1: Executive Dashboard

**Purpose**: Single-page executive view of entire logging program

**Header**: "Logging Program Compliance Dashboard - ISO/IEC 27001:2022 Control A.8.15"

**Document Information Block** (Rows 1-7):
```
Organization:          [USER INPUT]
Reporting Period:      [USER INPUT - Q4 2025]
Dashboard Date:        [AUTO - Today's date]
Program Owner:         CISO
Program Manager:       Information Security Manager
Last Full Assessment:  [Date of last IMP 1-4 completion]
Next Assessment Due:   [Calculated: Last + Review Cycle]
```

---

**Section 1: Overall Compliance Summary** (Rows 9-18, prominent display):

Large KPI boxes with conditional formatting:

| Metric | Value | Status | Target |
|--------|-------|--------|--------|
| **Overall Compliance Score** | Formula: Weighted avg of all assessments | Color: Green >95%, Yellow 85-95%, Red <85% | >95% |
| **Log Source Coverage** | From IMP 1: % systems logging | Color coded | 100% |
| **Collection Reliability** | From IMP 2: % uptime | Color coded | >99% |
| **Protection Compliance** | From IMP 3: % protected | Color coded | >95% |
| **Retention Compliance** | From IMP 3: % meeting retention | Color coded | 100% |
| **Review Compliance** | From IMP 4: % reviews completed | Color coded | 100% |
| **Detection Effectiveness** | From IMP 4: MTTD + alert quality | Color coded | >90% |
| **Critical Gaps Open** | From all IMPs: Critical priority gaps | Red if >0 | 0 |

---

**Section 2: Compliance by Assessment Area** (Rows 20-32):

Bar chart with data table:

| Assessment Area | Document ID | Completion Date | Compliance % | Status | Next Due |
|-----------------|-------------|-----------------|--------------|--------|----------|
| Log Source Inventory | IMP-A.8.15.1 | DD.MM.YYYY | Formula | Status | Date |
| Log Collection | IMP-A.8.15.2 | DD.MM.YYYY | Formula | Status | Date |
| Protection & Retention | IMP-A.8.15.3 | DD.MM.YYYY | Formula | Status | Date |
| Analysis & Review | IMP-A.8.15.4 | DD.MM.YYYY | Formula | Status | Date |

---

**Section 3: Compliance Trend** (Rows 34-48):

Line chart showing compliance over time (if historical data available):
- X-axis: Assessment periods (Q1 2025, Q2 2025, etc.)
- Y-axis: Compliance percentage
- Multiple lines: Overall, Log Sources, Collection, Protection, Analysis

---

**Section 4: Risk Heat Map** (Rows 50-65):

Matrix view:

|  | Log Sources | Collection | Protection | Retention | Review |
|--|-------------|------------|------------|-----------|--------|
| **Critical Systems** | Status | Status | Status | Status | Status |
| **High Systems** | Status | Status | Status | Status | Status |
| **Medium Systems** | Status | Status | Status | Status | Status |
| **Low Systems** | Status | Status | Status | Status | Status |

Color coding: Green = compliant, Yellow = partial, Red = non-compliant

---

**Section 5: Top 10 Gaps Requiring Attention** (Rows 67-82):

| Gap ID | Category | Description | Priority | Impact | Owner | Target Date | Status | Days Overdue |
|--------|----------|-------------|----------|--------|-------|-------------|--------|--------------|
| [From IMP gap sheets, sorted by priority] ||||||||

---

**Section 6: Key Metrics Summary** (Rows 84-100):

Three-column layout:

**Log Sources** | **Collection & Protection** | **Analysis & Detection**
- Total systems: ### | - Events/day: ### | - Use cases active: ###
- Logging enabled: ##% | - Storage used: ##% | - Alerts/day: ###
- SIEM integrated: ##% | - Collection uptime: ##% | - True positive rate: ##%
- Missing sources: ### | - Parse success rate: ##% | - MTTD: ## hours
- Priority 1 compliant: ##% | - Backup success: ##% | - MTTR: ## hours

---

**Section 7: Regulatory Compliance Summary** (Rows 102-115):

| Regulation | Applicable Systems | Compliance Status | Key Requirements Met | Gaps |
|------------|-------------------|-------------------|---------------------|------|
| ISO 27001 | All | Status % | List | Count |
| PCI DSS | Payment systems | Status % | List | Count |
| GDPR | EU data systems | Status % | List | Count |
| HIPAA | Healthcare systems | Status % | List | Count |
| SOX | Financial systems | Status % | List | Count |
| DORA | Financial ICT | Status % | List | Count |
| NIS2 | Critical infra | Status % | List | Count |

---

**Section 8: Resource Utilization** (Rows 117-128):

| Resource Type | Allocated | Used | % Used | Status | Forecast Need (+12m) |
|---------------|-----------|------|--------|--------|---------------------|
| Storage (TB) | ## | ## | Formula | Status | ## |
| SIEM Licenses | ## | ## | Formula | Status | ## |
| SOC FTE | ## | ## | Formula | Status | ## |
| Budget (Annual) | $### | $### | Formula | Status | $### |

---

**Section 9: Program Maturity Assessment** (Rows 130-145):

Maturity scorecard (1-5 scale):

| Capability | Maturity Level | Description | Target | Gap |
|------------|----------------|-------------|--------|-----|
| Log Coverage | 1-5 | Ad-hoc / Defined / Managed / Optimized | 4-5 | +/- |
| Collection Reliability | 1-5 | "" | 4-5 | +/- |
| Protection & Integrity | 1-5 | "" | 4-5 | +/- |
| Analysis & Detection | 1-5 | "" | 4-5 | +/- |
| Incident Response | 1-5 | "" | 4-5 | +/- |
| Process Documentation | 1-5 | "" | 4-5 | +/- |
| Staff Training | 1-5 | "" | 4-5 | +/- |
| Continuous Improvement | 1-5 | "" | 4-5 | +/- |

Radar chart visualization of maturity levels

---

**Section 10: Action Items Summary** (Rows 147-160):

| Priority | Open | This Month | Next Month | Next Quarter | Overdue |
|----------|------|------------|------------|--------------|---------|
| Critical | COUNT | COUNT | COUNT | COUNT | COUNT |
| High | COUNT | COUNT | COUNT | COUNT | COUNT |
| Medium | COUNT | COUNT | COUNT | COUNT | COUNT |
| Total | SUM | SUM | SUM | SUM | SUM |

---

### Sheet 2: Detailed Metrics

**Purpose**: Detailed breakdown of all compliance metrics

**Section 1: Log Source Metrics** (from IMP 1):
- Total systems assessed
- Systems by type breakdown
- Systems by environment breakdown
- Logging enabled rate
- Event type coverage percentages
- Compliance by system criticality

**Section 2: Collection Metrics** (from IMP 2):
- Daily event volume
- Parse success rates
- Collection reliability by source
- Storage capacity metrics
- SIEM performance metrics
- Integration health

**Section 3: Protection Metrics** (from IMP 3):
- Access control implementation rate
- Integrity protection implementation rate
- Encryption in transit rate
- Backup success rate
- Separation of duties compliance
- Legal holds active

**Section 4: Retention Metrics** (from IMP 3):
- Retention compliance by log type
- Storage tier utilization
- Disposal process compliance
- Over/under retention issues

**Section 5: Analysis Metrics** (from IMP 4):
- Review schedule compliance
- Alert volumes and quality
- Detection effectiveness
- Investigation quality scores
- SOC analyst performance
- Detection coverage percentages

---

### Sheet 3: Gap Register (Consolidated)

**Purpose**: All gaps from all assessments in one place

**Column Structure** (15 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Gap ID | 15 | Text: Source-###  (e.g., IMP1-001) |
| B | Source Assessment | 20 | Dropdown: IMP 1, IMP 2, IMP 3, IMP 4 |
| C | Gap Category | 25 | Text |
| D | Description | 50 | Text |
| E | Policy Requirement | 25 | Text: S2.x.x reference |
| F | Priority | 15 | Dropdown: Critical, High, Medium, Low |
| G | Business Impact | 20 | Dropdown: Critical, High, Medium, Low |
| H | Affected Systems Count | 20 | Number |
| I | Remediation Action | 50 | Text |
| J | Owner | 25 | Text |
| K | Target Date | 15 | Date: DD.MM.YYYY |
| L | Budget Required | 15 | Number: $ amount |
| M | Status | 15 | Dropdown: Open, In Progress, Resolved, Deferred |
| N | Days Open | 12 | Formula: TODAY() - First identified |
| O | Notes | 40 | Text |

**Data Import**: Pull gaps from IMP 1-4 gap sheets

**Auto-Calculations**:
- Days overdue (if past target date and not resolved)
- Total budget required
- Gaps by priority/status

---

### Sheet 4: Trend Analysis

**Purpose**: Historical trend tracking (populated over multiple assessment cycles)

**Column Structure** (Variable columns based on quarters):

| Assessment Period | Q1 2025 | Q2 2025 | Q3 2025 | Q4 2025 | Target |
|-------------------|---------|---------|---------|---------|--------|
| Overall Compliance % | ## | ## | ## | ## | >95% |
| Log Source Coverage % | ## | ## | ## | ## | 100% |
| Collection Reliability % | ## | ## | ## | ## | >99% |
| Protection Compliance % | ## | ## | ## | ## | >95% |
| Retention Compliance % | ## | ## | ## | ## | 100% |
| Review Compliance % | ## | ## | ## | ## | 100% |
| Alert True Positive % | ## | ## | ## | ## | >50% |
| MTTD (hours) | ## | ## | ## | ## | <1 |
| MTTR (hours) | ## | ## | ## | ## | <4 |
| Open Critical Gaps | ## | ## | ## | ## | 0 |

**Charts**:
- Trend lines for each metric
- Gap closure velocity
- Improvement trajectory

---

### Sheet 5: Regulatory Mapping

**Purpose**: Map logging requirements to regulatory obligations

**Column Structure** (12 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Regulation / Standard | 25 | Dropdown: ISO 27001, PCI DSS, HIPAA, GDPR, SOX, DORA, NIS2 |
| B | Requirement ID | 20 | Text: Specific clause |
| C | Requirement Description | 50 | Text |
| D | Policy Section | 20 | Text: S2.x.x |
| E | Implementation Assessment | 25 | Text: Which IMP covers this |
| F | Applicable Systems | 30 | Text: Which systems must comply |
| G | Compliance Status | 18 | Dropdown: Compliant, Partial, Non-Compliant |
| H | Evidence Location | 40 | Text: Where evidence is |
| I | Last Verified | 15 | Date: DD.MM.YYYY |
| J | Next Verification | 15 | Date |
| K | Gaps | 40 | Text |
| L | Notes | 40 | Text |

**Data Rows**: 50-150 (regulatory requirements)

**Key Regulatory Requirements Mapped**:
- ISO 27001:2022 A.8.15
- PCI DSS 4.0 Requirement 10
- HIPAA § 164.312(b)
- GDPR Article 32
- SOX Section 404
- DORA Article 17
- NIS2 Article 21

---

### Sheet 6: Action Plan & Roadmap

**Purpose**: Strategic roadmap for logging program improvements

**Column Structure** (13 columns):

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Initiative ID | 15 | Auto: INIT-001 |
| B | Initiative Name | 30 | Text |
| C | Description | 50 | Text |
| D | Strategic Goal | 30 | Dropdown: Improve Coverage, Enhance Detection, Reduce Gaps, Compliance, Optimization, Other |
| E | Related Gaps | 25 | Text: Gap IDs addressed |
| F | Priority | 15 | Dropdown: Critical, High, Medium, Low |
| G | Start Date | 15 | Date |
| H | Target End Date | 15 | Date |
| I | Status | 15 | Dropdown: Not Started, Planning, In Progress, Completed, On Hold |
| J | % Complete | 12 | Number: 0-100 |
| K | Budget | 15 | Number: $ |
| L | Owner | 25 | Text |
| M | Notes | 40 | Text |

**Roadmap Visualization** (Gantt chart style):
Timeline showing initiatives across quarters

---

### Sheet 7: Management Report Template

**Purpose**: Pre-formatted report for management presentation

**Report Structure**:

**Page 1: Executive Summary** (Rows 1-40)
- Overall compliance status (Green/Yellow/Red)
- Key achievements this period
- Critical issues requiring attention
- Resource requirements
- Recommended actions

**Page 2: Detailed Findings** (Rows 42-80)
- Compliance by assessment area
- Gap summary by priority
- Regulatory compliance status
- Metric trends

**Page 3: Action Plan** (Rows 82-120)
- Priority gaps and remediation plans
- Resource requests (budget, personnel, tools)
- Timeline for improvements
- Expected outcomes

**Formatting**: Professional report layout with:
- Headers/footers
- Page numbers
- Print-friendly formatting
- Charts embedded
- Executive-appropriate language

---

### Sheet 8: Instructions & Data Sources

**Purpose**: Explain how to use and update the dashboard

**Content**:

**Data Sources**:
- IMP-A.8.15.1: Log Source Inventory (Sheet 2 pulls from IMP 1)
- IMP-A.8.15.2: Log Collection (Sheet 2 pulls from IMP 2)
- IMP-A.8.15.3: Protection & Retention (Sheet 2 pulls from IMP 3)
- IMP-A.8.15.4: Analysis & Review (Sheet 2 pulls from IMP 4)

**Update Frequency**:
- Quarterly: Full dashboard refresh with new IMP assessments
- Monthly: Update metrics that change monthly (events/day, storage, etc.)
- Weekly: Update action item status
- Daily: Update if real-time SIEM metrics integrated

**How to Update**:
1. Complete IMP assessments (1-4) for the period
2. Export summary data from each IMP
3. Paste into "Data Import" section (hidden sheet)
4. Dashboard auto-refreshes with formulas
5. Review calculated metrics for accuracy
6. Update status of gaps/actions manually
7. Generate management report (Sheet 7)
8. Present to CISO/management

**Customization Notes**:
- Adjust targets based on organizational risk appetite
- Add/remove regulatory sections as applicable
- Customize maturity model definitions
- Add organization-specific KPIs

---

## Formulas & Logic

**Overall Compliance Score**:
```excel
= (IMP1_Score * 0.25) + (IMP2_Score * 0.25) + (IMP3_Score * 0.25) + (IMP4_Score * 0.25)
```

**Status Color Coding**:
```excel
Green: >=95%
Yellow: >=85% AND <95%
Red: <85%
```

**Days Overdue** (Gap Register):
```excel
=IF(AND(K2<TODAY(), M2<>"Resolved"), TODAY()-K2, 0)
```

**Trend Calculation**:
```excel
=IF(Current_Period > Previous_Period, "Improving", IF(Current_Period < Previous_Period, "Declining", "Stable"))
```

---

## Conditional Formatting Rules

**Apply across dashboard**:
- Compliance percentages: Red <85%, Yellow 85-95%, Green >95%
- Status indicators: Red = Non-Compliant, Yellow = Partial, Green = Compliant
- Days overdue: Red if >0
- Priority: Red = Critical, Orange = High, Yellow = Medium, Green = Low
- Trend indicators: Up arrow (green) = improving, Down arrow (red) = declining

---

## File Naming Convention

**Filename**: `ISMS-IMP-A_8_15_5_Compliance_Dashboard_YYYYMMDD.xlsx`

Example: `ISMS-IMP-A_8_15_5_Compliance_Dashboard_20260106.xlsx`

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.5 |
| **Version** | 1.0 |
| **ISO 27001 Control** | A.8.15 (Logging) |
| **Related Policy** | All ISMS-POL-A.8.15 sections |
| **Sheet Count** | 8 |
| **Update Frequency** | Quarterly (full), Monthly (metrics) |
| **Target Audience** | Executive Management, CISO, Audit |

---

**END OF IMP SPECIFICATION A.8.15.5**