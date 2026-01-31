# ISMS-IMP-A.8.15.1 - Log Source Inventory Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.15 - Logging

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.15.1  
**Assessment Area:** Log Source Inventory and Completeness  
**Related Policy:** ISMS-POL-A.8.15-S2.1 (Event Logging Requirements)  
**Purpose:** Catalog all systems generating logs and assess logging completeness  
**Python Generator:** `generate_a815_1_log_source_inventory.py`  
**Target Audience:** System Owners, Log Administrators, SOC Team

---

## Workbook Structure Overview

**Total Sheets:** 13  
**Estimated Rows:** ~800 (varies by organization size)  
**Estimated Completion Time:** 4-8 hours (for 50-100 systems)  
**Review Cycle:** Annual (full assessment), Quarterly (updates)

### Sheet List
1. Instructions & Legend
2. System Inventory
3. Log Event Types by System
4. Authentication Logging Assessment
5. Authorization & Access Logging
6. Administrative Activity Logging
7. Security Event Logging
8. Application & Database Logging
9. Network Device Logging
10. Gap Analysis
11. Evidence Register
12. Summary Dashboard
13. Approval & Sign-Off

---

## Sheet 1: Instructions & Legend

### Header Section
**Main Title:** "Log Source Inventory Assessment"  
**Subtitle:** "ISO/IEC 27001:2022 - Control A.8.15: Logging"  
**Styling:** Dark blue header (003366), white text, 14pt bold, centered, 40px height

### Document Information Block (Rows 3-11)

| Field | Value | Cell Color |
|-------|-------|------------|
| Document ID | ISMS-IMP-A.8.15.1 | Gray (info) |
| Assessment Area | Log Source Inventory | Gray (info) |
| Related Policy | ISMS-POL-A.8.15-S2.1 | Gray (info) |
| Version | 1.0 | Gray (info) |
| Assessment Date | [USER INPUT] | Yellow (input) |
| Completed By | [USER INPUT] | Yellow (input) |
| Organization | [USER INPUT] | Yellow (input) |
| Review Cycle | Annual (full), Quarterly (updates) | Gray (info) |

### How to Use This Workbook (Rows 13-30)

**Instructions (numbered list):**
1. Complete the "System Inventory" sheet for all in-scope systems
2. For each system, document log sources and event types logged
3. Use dropdowns to ensure consistent data entry
4. Yellow cells require user input, gray cells are auto-calculated
5. Complete compliance checklist for each log source type
6. Review Summary Dashboard for overall compliance status
7. Document gaps in Gap Analysis sheet
8. Develop remediation plan for identified gaps
9. Obtain approvals in Approval & Sign-Off sheet

### Legend (Rows 32-42)

| Color | Hex | Meaning |
|-------|-----|---------|
| Yellow | FFFFCC | User input required |
| Green | C6EFCE | Compliant / Complete |
| Red | FFC7CE | Non-compliant / Missing |
| Gray | E7E6E6 | Auto-calculated / Reference |
| Blue | 4472C4 | Instructions / Headers |

### Key Definitions (Rows 44-60)

| Term | Definition |
|------|------------|
| **Log Source** | Any system, application, or device generating event logs |
| **Event Type** | Category of logged activity (authentication, authorization, etc.) |
| **SIEM** | Security Information and Event Management system |
| **Hot Storage** | Real-time searchable log storage (0-90 days typical) |
| **Warm Storage** | Compressed, slower-access storage (91-365 days typical) |
| **Cold Storage** | Archive storage (>1 year) |
| **WORM** | Write-Once-Read-Many (immutable storage) |
| **Syslog** | Standard logging protocol (RFC 5424) |
| **CEF** | Common Event Format |
| **EVTX** | Windows Event Log format |

---

## Sheet 2: System Inventory

### Purpose
Catalog all systems in scope for logging requirements.

### Column Structure (17 columns: A-Q)

| Col | Header | Width | Type | Validation/Format |
|-----|--------|-------|------|-------------------|
| A | System ID | 15 | Text | Auto-generated: SYS-001, SYS-002, etc. |
| B | System Name | 30 | Text | Free text |
| C | System Type | 20 | Dropdown | Server, Network Device, Security Appliance, Application, Cloud Service, Database, Other |
| D | Operating System / Platform | 25 | Dropdown | Windows, Linux, Unix, Network OS, Cloud, Application Platform, Other |
| E | Environment | 15 | Dropdown | Production, Staging, Development, Test |
| F | Data Classification | 18 | Dropdown | Public, Internal, Confidential, Restricted |
| G | Business Criticality | 18 | Dropdown | Critical (T1), High (T2), Medium (T3), Low (T4) |
| H | Regulatory Scope | 20 | Multi-text | PCI DSS, HIPAA, GDPR, FADP, SOX, DORA, NIS2, None |
| I | Logging Priority | 15 | Dropdown | P1-Critical, P2-High, P3-Medium, P4-Low |
| J | System Owner | 25 | Text | Name |
| K | Owner Email | 30 | Text | Email format |
| L | Hostname / FQDN | 30 | Text | Free text |
| M | Primary IP | 15 | Text | IP format |
| N | Location | 20 | Text | Data center, cloud region |
| O | Logging Enabled | 15 | Dropdown | Yes, No, Partial, Unknown |
| P | Forwarding to SIEM | 18 | Dropdown | Yes, No, Planned, N/A |
| Q | Compliance Status | 18 | Formula | =IF(AND(O2="Yes",P2="Yes"),"Compliant","Non-Compliant") |

### Row Structure
- **Row 1:** Sheet title
- **Rows 3-6:** Header and instructions
- **Row 7:** Column headers (gray background, bold, borders)
- **Row 8:** Example row (gray, italic) with sample data
- **Rows 9-100:** Data entry rows (92 rows, yellow input cells)

### Example Data (Row 8 - Gray Italic)
```
SYS-001 | web-prod-01 | Server | Linux | Production | Confidential | Critical (T1) | 
PCI DSS, GDPR | P1-Critical | John Doe | jdoe@example.com | web-prod-01.example.com | 
10.0.1.50 | DC1 | Yes | Yes | Compliant
```

### Conditional Formatting
- **Column Q (Compliance Status):**
  - "Compliant" → Green fill (C6EFCE)
  - "Non-Compliant" → Red fill (FFC7CE)
  - "Partial" → Yellow fill (FFEB9C)

---

## Sheet 3: Log Event Types by System

### Purpose
Document what event types each system logs.

### Column Structure (19 columns: A-S)

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | System ID | 15 | Dropdown | Links to Sheet 2 System IDs |
| B | System Name | 30 | Formula | =VLOOKUP(A2,'System Inventory'!A:B,2,FALSE) |
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
| N | Est. Daily Volume (MB) | 20 | Number | Numeric validation, >0 |
| O | Retention Period (months) | 20 | Number | Numeric validation, >0 |
| P | Storage Tier | 15 | Dropdown | Hot, Warm, Cold, Unknown |
| Q | Protection Mechanisms | 20 | Text | Access Controls, Encryption, WORM, Hashing, None |
| R | Event Types Completeness | 20 | Formula | =COUNTIF(C2:J2,"Yes")/COUNTA(C2:J2) |
| S | Notes | 40 | Text | Free text |

### Row Structure
- **Rows 1-7:** Headers and instructions
- **Row 8:** Example data (gray italic)
- **Rows 9-100:** Data entry (92 rows)

### Formula Details
**Column R (Event Types Completeness):**
```excel
=COUNTIF(C2:J2,"Yes")/COUNTA(C2:J2)
```
Format as percentage. Conditional formatting:
- ≥90% → Green
- 70-89% → Yellow
- <70% → Red

---

## Sheet 4: Authentication Logging Assessment

### Purpose
Detailed assessment of authentication logging per ISMS-POL-A.8.15-S2.1.2

### Column Structure (18 columns: A-R)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | System ID | 15 | Dropdown (from Sheet 2) |
| B | System Name | 30 | Formula (VLOOKUP) |
| C | Logs Successful Logins | 18 | Dropdown: Yes, No, Partial, N/A |
| D | Logs Failed Logins | 18 | Dropdown: Yes, No, Partial, N/A |
| E | Logs Account Lockouts | 18 | Dropdown: Yes, No, Partial, N/A |
| F | Logs Password Changes | 18 | Dropdown: Yes, No, Partial, N/A |
| G | Logs Session Start/End | 18 | Dropdown: Yes, No, Partial, N/A |
| H | Includes User ID | 15 | Dropdown: Yes, No |
| I | Includes Timestamp | 15 | Dropdown: Yes, No |
| J | Includes Source IP | 15 | Dropdown: Yes, No |
| K | Includes Auth Method | 15 | Dropdown: Yes, No |
| L | MFA Events Logged | 15 | Dropdown: Yes, No, N/A |
| M | SSO Events Logged | 15 | Dropdown: Yes, No, N/A |
| N | Service Account Auth Logged | 20 | Dropdown: Yes, No, N/A |
| O | Privileged Auth Logged | 18 | Dropdown: Yes, No, N/A |
| P | Compliance Score | 18 | Formula | =(COUNTIF(C2:O2,"Yes")/COUNTIF(C2:O2,"<>N/A"))*100 |
| Q | Gap Description | 40 | Text | If non-compliant, describe |
| R | Remediation Plan | 40 | Text | How to fix |

### Compliance Targets
- **Critical Systems (P1):** 100% compliance (all "Yes")
- **High Priority (P2):** ≥95% compliance
- **Medium Priority (P3):** ≥90% compliance
- **Low Priority (P4):** ≥80% compliance

---

## Sheet 5: Authorization & Access Logging

### Purpose
Assessment of access control event logging per ISMS-POL-A.8.15-S2.1.3

### Column Structure (18 columns: A-R)

| Col | Header | Assessment Criteria |
|-----|--------|-------------------|
| A-B | System ID/Name | (as previous sheets) |
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
| M | Includes Before/After State | Yes/No |
| N | Logs Group Membership Changes | Yes/No/N/A |
| O | Logs Role Assignment | Yes/No/N/A |
| P | Compliance Score | Formula (as Sheet 4) |
| Q | Gap Description | Text |
| R | Remediation Plan | Text |

---

## Sheet 6: Administrative Activity Logging

### Purpose
Assessment of administrative action logging per ISMS-POL-A.8.15-S2.1.4

### Column Structure (18 columns: A-R)

| Col | Header | Assessment Criteria |
|-----|--------|-------------------|
| A-B | System ID/Name | (as previous) |
| C | User Account Management | Yes/No/Partial/N/A |
| D | Group/Role Management | Yes/No/Partial/N/A |
| E | Configuration Changes | Yes/No/Partial/N/A |
| F | Security Policy Changes | Yes/No/Partial/N/A |
| G | Software Install/Uninstall | Yes/No/Partial/N/A |
| H | Service Start/Stop | Yes/No/Partial/N/A |
| I | Patch Application | Yes/No/Partial/N/A |
| J | Bulk Data Operations | Yes/No/Partial/N/A |
| K | Privileged Session Logging | Yes/No/Partial/N/A |
| L | Includes Administrator ID | Yes/No |
| M | Includes Before/After Values | Yes/No |
| N | Includes Timestamp | Yes/No |
| O | Includes Change Reason | Yes/No |
| P | Compliance Score | Formula |
| Q | Gap Description | Text |
| R | Remediation Plan | Text |

---

## Sheet 7: Security Event Logging

### Purpose
Assessment of security tool and event logging per ISMS-POL-A.8.15-S2.1.5

### Column Structure (18 columns: A-R)

| Col | Header | Assessment Criteria |
|-----|--------|-------------------|
| A-B | System ID/Name | (as previous) |
| C | Firewall Events | Yes/No/Partial/N/A |
| D | IDS/IPS Alerts | Yes/No/Partial/N/A |
| E | Anti-malware Events | Yes/No/Partial/N/A |
| F | DLP Events | Yes/No/Partial/N/A |
| G | Web Filtering Events | Yes/No/Partial/N/A |
| H | Email Gateway Events | Yes/No/Partial/N/A |
| I | EDR Events | Yes/No/Partial/N/A |
| J | Vulnerability Scan Results | Yes/No/Partial/N/A |
| K | Security Incident Events | Yes/No/Partial/N/A |
| L | Includes Severity Level | Yes/No |
| M | Includes Threat Indicators | Yes/No |
| N | Includes Response Actions | Yes/No |
| O | Automated Response Logged | Yes/No |
| P | Compliance Score | Formula |
| Q | Gap Description | Text |
| R | Remediation Plan | Text |

---

## Sheet 8: Application & Database Logging

### Purpose
Assessment of application and database logging per ISMS-POL-A.8.15-S2.1.7

### Column Structure (18 columns: A-R)

| Col | Header | Assessment Criteria |
|-----|--------|-------------------|
| A-B | System ID/Name | (as previous) |
| C | Web App Access Logging | Yes/No/Partial/N/A |
| D | API Call Logging | Yes/No/Partial/N/A |
| E | Transaction Logging | Yes/No/Partial/N/A |
| F | Application Errors | Yes/No/Partial/N/A |
| G | Database Connections | Yes/No/Partial/N/A |
| H | Database Queries (Sensitive) | Yes/No/Partial/N/A |
| I | Schema Changes (DDL) | Yes/No/Partial/N/A |
| J | Permission Grants | Yes/No/Partial/N/A |
| K | Backup/Restore Operations | Yes/No/Partial/N/A |
| L | Includes User/App Identity | Yes/No |
| M | Includes Data Modified | Yes/No |
| N | Includes Query Text | Yes/No |
| O | Includes Row Count | Yes/No |
| P | Compliance Score | Formula |
| Q | Gap Description | Text |
| R | Remediation Plan | Text |

---

## Sheet 9: Network Device Logging

### Purpose
Assessment of network infrastructure logging per ISMS-POL-A.8.15-S2.1.8

### Column Structure (18 columns: A-R)

| Col | Header | Assessment Criteria |
|-----|--------|-------------------|
| A-B | Device ID/Name | (as previous) |
| C | Connection Logging | Yes/No/Partial/N/A |
| D | Rule Match Logging | Yes/No/Partial/N/A |
| E | Configuration Changes | Yes/No/Partial/N/A |
| F | Interface Up/Down Events | Yes/No/Partial/N/A |
| G | Routing Changes | Yes/No/Partial/N/A |
| H | VPN Session Logging | Yes/No/Partial/N/A |
| I | DHCP/DNS Events | Yes/No/Partial/N/A |
| J | Wireless Events | Yes/No/Partial/N/A |
| K | NAT Translations | Yes/No/Partial/N/A |
| L | Includes Source/Dest IP | Yes/No |
| M | Includes Ports/Protocols | Yes/No |
| N | Includes Action (allow/deny) | Yes/No |
| O | Includes Bytes Transferred | Yes/No |
| P | Compliance Score | Formula |
| Q | Gap Description | Text |
| R | Remediation Plan | Text |

---

## Sheet 10: Gap Analysis

### Purpose
Consolidated list of all identified gaps across all assessments.

### Column Structure (12 columns: A-L)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Gap ID | 12 | Auto-generated: GAP-001, GAP-002, etc. |
| B | System ID | 15 | Dropdown (from Sheet 2) |
| C | System Name | 30 | Formula (VLOOKUP) |
| D | Gap Category | 25 | Dropdown: Log Source Missing, Event Type Not Logged, Incomplete Fields, Format Non-Standard, Protection Inadequate, Other |
| E | Gap Description | 50 | Text |
| F | Policy Requirement | 30 | Text (S2.1.x reference) |
| G | Impact / Risk | 20 | Dropdown: Critical, High, Medium, Low |
| H | Remediation Action | 50 | Text |
| I | Responsible Party | 25 | Text |
| J | Target Date | 15 | Date (DD.MM.YYYY format) |
| K | Status | 15 | Dropdown: Open, In Progress, Resolved, Deferred |
| L | Notes | 40 | Text |

### Auto-Population Logic
Gaps from Sheets 3-9 where Compliance Score <100% should auto-populate here using formulas or be manually entered.

### Conditional Formatting
- **Column G (Impact/Risk):**
  - Critical → Red
  - High → Orange
  - Medium → Yellow
  - Low → Green
- **Column J (Target Date):**
  - Overdue (past today) → Red fill
- **Column K (Status):**
  - Open → Red
  - In Progress → Yellow
  - Resolved → Green

---

## Sheet 11: Evidence Register

### Purpose
Track evidence artifacts for audit and compliance verification.

### Column Structure (10 columns: A-J)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Evidence ID | 15 | Auto-generated: EVD-001, EVD-002 |
| B | Evidence Type | 25 | Dropdown: Log Sample, Configuration Screenshot, SIEM Query Result, Documentation, Other |
| C | Description | 40 | Text |
| D | Related System(s) | 30 | Text |
| E | Related Policy Req | 25 | Text (S2.1.x reference) |
| F | File Name / Location | 40 | Text |
| G | Collected By | 25 | Text |
| H | Collection Date | 15 | Date (DD.MM.YYYY) |
| I | Retention Period | 20 | Text |
| J | Notes | 40 | Text |

### Row Structure
- **Rows 1-7:** Headers and instructions
- **Rows 8-107:** Data entry (100 rows for evidence tracking)

---

## Sheet 12: Summary Dashboard

### Purpose
Executive summary of assessment results with KPIs and visualizations.

### Section 1: Overall Compliance Summary (Rows 3-10)

| Metric | Formula | Target | Display |
|--------|---------|--------|---------|
| Total Systems Assessed | =COUNTA('System Inventory'!A9:A100)-COUNTBLANK(...) | N/A | Number |
| Systems with Logging Enabled | =COUNTIF('System Inventory'!O:O,"Yes") | 100% | Number + % |
| Systems Forwarding to SIEM | =COUNTIF('System Inventory'!P:P,"Yes") | 100% | Number + % |
| Overall Compliance Rate | =Average of all compliance scores from Sheets 4-9 | >95% | % with status color |
| Critical Systems Compliant | =% of P1 systems with compliance >95% | 100% | % with status |
| Medium Systems Compliant | =% of P3 systems with compliance >90% | >90% | % with status |
| Low Systems Compliant | =% of P4 systems with compliance >80% | >80% | % with status |

**Status Color Coding:**
- Green: Meets/exceeds target
- Yellow: Within 10% of target
- Red: Below target by >10%

### Section 2: Event Type Coverage (Rows 12-22)

| Event Type | Systems Logging | % Coverage | Target | Status |
|------------|-----------------|------------|--------|--------|
| Authentication | =COUNTIF('Log Event Types'!C:C,"Yes") | Formula | >95% | Color |
| Authorization | =COUNTIF('Log Event Types'!D:D,"Yes") | Formula | >95% | Color |
| Administrative | =COUNTIF('Log Event Types'!E:E,"Yes") | Formula | >95% | Color |
| Security Events | =COUNTIF('Log Event Types'!F:F,"Yes") | Formula | 100% | Color |
| Application | =COUNTIF('Log Event Types'!G:G,"Yes") | Formula | >90% | Color |
| System | =COUNTIF('Log Event Types'!H:H,"Yes") | Formula | >85% | Color |
| Network | =COUNTIF('Log Event Types'!I:I,"Yes") | Formula | >85% | Color |
| Database | =COUNTIF('Log Event Types'!J:J,"Yes") | Formula | >90% | Color |

### Section 3: Gap Summary by Priority (Rows 24-30)

| Priority | Open Gaps | In Progress | Resolved | Overdue | % Complete |
|----------|-----------|-------------|----------|---------|------------|
| Critical | =COUNTIFS('Gap Analysis'!G:G,"Critical",K:K,"Open") | Formula | Formula | Formula | Formula |
| High | =COUNTIFS('Gap Analysis'!G:G,"High",K:K,"Open") | Formula | Formula | Formula | Formula |
| Medium | Formula | Formula | Formula | Formula | Formula |
| Low | Formula | Formula | Formula | Formula | Formula |
| **Total** | =SUM | =SUM | =SUM | =SUM | Formula |

### Section 4: Visualizations (Rows 32-60)

**Chart 1: Compliance Status Pie Chart**
- Data: Compliant, Partial, Non-Compliant counts
- Colors: Green, Yellow, Red

**Chart 2: Event Type Coverage Bar Chart**
- X-axis: Event types (Auth, Admin, Security, etc.)
- Y-axis: % coverage
- Target line at 95%

**Chart 3: Compliance by System Type**
- Bar chart showing compliance % by system type (Server, Network Device, Application, etc.)

**Chart 4: Gap Status Distribution**
- Stacked bar by priority showing Open/In Progress/Resolved

### Section 5: Top Gaps Requiring Attention (Rows 62-75)

Table showing top 10 gaps sorted by:
1. Critical gaps first
2. Then by target date (most overdue first)

| Gap ID | System | Description | Priority | Target Date | Days Overdue | Status |
|--------|--------|-------------|----------|-------------|--------------|--------|
| (Auto-populated from Gap Analysis sheet, sorted by priority and date) |

### Section 6: Recommendations (Rows 77-90)

**Pre-populated recommendations based on common gaps:**
1. If <95% authentication logging → "Implement authentication logging on all systems"
2. If <90% SIEM forwarding → "Configure centralized log forwarding"
3. If critical gaps exist → "Prioritize remediation of critical gaps within 30 days"
4. If >20% systems missing logging → "Conduct log source discovery exercise"

**Text box for assessor custom recommendations** (5 rows, merged cells)

### Section 7: Assessment Metadata (Rows 92-100)

| Field | Value |
|-------|-------|
| Assessment Completed By | (from Instructions sheet) |
| Assessment Date | (from Instructions sheet) |
| Review Date | (Today + 90 days) |
| Approval Status | (from Approval sheet) |
| Next Assessment Due | (Today + 365 days) |

---

## Sheet 13: Approval & Sign-Off

### Purpose
Document multi-level approval workflow.

### Approval Table (Rows 3-12)

| Role | Name | Date | Signature | Status |
|------|------|------|-----------|--------|
| System Owners (collective) | [List] | DD.MM.YYYY | _____ | ☐ Reviewed |
| Log Administrator | [Name] | DD.MM.YYYY | _____ | ☐ Reviewed |
| SOC Lead | [Name] | DD.MM.YYYY | _____ | ☐ Reviewed |
| Information Security Manager | [Name] | DD.MM.YYYY | _____ | ☐ Approved |
| CISO | [Name] | DD.MM.YYYY | _____ | ☐ Approved |

### Acknowledgments Checklist (Rows 14-25)

- ☐ Assessment completed per ISMS-POL-A.8.15-S2.1
- ☐ All in-scope systems documented in System Inventory
- ☐ Event type logging assessed for all systems
- ☐ Gaps identified and prioritized
- ☐ Remediation plan established with target dates
- ☐ Resources committed for gap remediation
- ☐ Evidence artifacts collected and registered
- ☐ Next assessment date scheduled
- ☐ Stakeholders informed of findings
- ☐ Dashboard reviewed with management

### Comments Section (Rows 27-35)

Large text box (merged cells) for approval comments, conditions, or concerns.

---

## Cell Styling Reference

### Header Styles
- **Main Header (Sheet titles):**
  - Font: Calibri 14pt bold white
  - Fill: 003366 (dark blue)
  - Height: 40px, centered
  
- **Subheader (Section titles):**
  - Font: Calibri 11pt bold white
  - Fill: 4472C4 (medium blue)
  - Height: 30px, centered
  
- **Column Headers:**
  - Font: Calibri 10pt bold black
  - Fill: D9D9D9 (light gray)
  - Borders: All sides, thin black

### Input Cell Styles
- **User Input:**
  - Fill: FFFFCC (light yellow)
  - Alignment: Left/center, text wrap enabled
  - Border: Thin black all sides
  
- **Example Data (Row 8):**
  - Fill: E7E6E6 (light gray)
  - Font: Italic
  - Border: Thin gray

### Status/Compliance Fills
- **Compliant:** C6EFCE (light green)
- **Partial:** FFEB9C (light yellow)
- **Non-Compliant:** FFC7CE (light red)
- **N/A:** D9D9D9 (gray)

### Formula Cells
- **Calculated Fields:**
  - Fill: E7E6E6 (light gray)
  - Font: Regular black
  - Border: Thin black
  - Protection: Locked (prevent editing)

---

## Formulas & Validation

### Key Formulas

**System Inventory - Compliance Status (Sheet 2, Column Q):**
```excel
=IF(AND(O2="Yes",P2="Yes"),"Compliant",IF(OR(O2="Partial",P2="Planned"),"Partial","Non-Compliant"))
```

**Log Event Types - Event Type Completeness (Sheet 3, Column R):**
```excel
=COUNTIF(C2:J2,"Yes")/COUNTA(C2:J2)
```
Format: Percentage, 0 decimals

**Assessment Sheets - Compliance Score (Sheets 4-9, Column P):**
```excel
=(COUNTIF(C2:O2,"Yes")/COUNTIF(C2:O2,"<>N/A"))*100
```
Format: Number, 1 decimal, append "%"

**Summary Dashboard - Total Systems:**
```excel
=COUNTA('System Inventory'!A9:A100)-COUNTBLANK('System Inventory'!A9:A100)
```

**Summary Dashboard - Overall Compliance Rate:**
```excel
=AVERAGE('Authentication Logging'!P:P,'Authorization & Access'!P:P,'Administrative Activity'!P:P,'Security Event'!P:P,'Application & Database'!P:P,'Network Device'!P:P)
```

**Gap Analysis - Days Overdue:**
```excel
=IF(AND(J2<TODAY(),K2<>"Resolved"),TODAY()-J2,0)
```

### Data Validations

**Dropdown Lists:**
- All dropdowns: List validation with error alert on invalid entry
- Error message: "Please select from dropdown list"

**Email Validation (Sheet 2, Column K):**
```excel
=AND(ISNUMBER(FIND("@",K2)),ISNUMBER(FIND(".",K2)),LEN(K2)>5)
```

**Date Validation:**
- Format: DD.MM.YYYY
- Allow dates only (no text)
- Min date: 01.01.2020, Max date: 31.12.2030

**Numeric Validation:**
- Greater than 0
- Whole numbers only (where applicable)

---

## Conditional Formatting Rules

### Apply Across All Assessment Sheets (4-9)

**Compliance Score (Column P):**
- Green (C6EFCE): ≥95
- Yellow (FFEB9C): 80-94
- Red (FFC7CE): <80

**Status Columns:**
- "Yes" / "Compliant" → Green
- "Partial" / "In Progress" → Yellow
- "No" / "Non-Compliant" / "Open" → Red
- "N/A" / "Unknown" → Gray

### Gap Analysis Sheet

**Priority Column (G):**
- "Critical" → Red fill
- "High" → Orange (FFC000)
- "Medium" → Yellow
- "Low" → Green

**Target Date Column (J):**
- If date < TODAY() AND Status ≠ "Resolved" → Red fill

**Status Column (K):**
- "Open" → Red
- "In Progress" → Yellow
- "Resolved" → Green
- "Deferred" → Gray

### Summary Dashboard

**Compliance metrics:**
- ≥Target → Green
- ≥90% of target → Yellow
- <90% of target → Red

---

## File Naming Convention

**Generated Filename Format:**
```
ISMS-IMP-A_8_15_1_Log_Source_Inventory_YYYYMMDD.xlsx
```

**Example:**
```
ISMS-IMP-A_8_15_1_Log_Source_Inventory_20260106.xlsx
```

**Date Component:**
- Use generation date (today)
- Format: YYYYMMDD (for filename sorting)
- Excel internal dates: DD.MM.YYYY

---

## Document Metadata

| Attribute | Value |
|-----------|-------|
| **Control** | ISO/IEC 27001:2022 A.8.15 |
| **Policy** | ISMS-POL-A.8.15-S2.1 |
| **Version** | 1.0 |
| **Sheet Count** | 13 |
| **Est. File Size** | 800 KB - 1.5 MB |
| **Est. Completion Time** | 4-8 hours |
| **Review Cycle** | Annual (full), Quarterly (updates) |
| **Target Audience** | System Owners, Log Admins, SOC Team, Auditors |

---

**END OF ISMS-IMP-A.8.15.1 SPECIFICATION**