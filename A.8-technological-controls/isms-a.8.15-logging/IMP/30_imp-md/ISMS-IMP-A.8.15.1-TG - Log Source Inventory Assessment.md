**ISMS-IMP-A.8.15.1-TG - Log Source Inventory Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.15: Logging

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.15.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Log Source Inventory & Event Logging Completeness |
| **Related Policy** | ISMS-POL-A.8.15, Section 2.1 (Event Logging Requirements) |
| **Purpose** | Catalog all systems generating logs, verify logging completeness against policy requirements, and identify gaps in event logging coverage |
| **Target Audience** | IT Operations, System Owners, Application Owners, Security Team, Compliance Officers, Auditors, Workbook Developers (Python/Excel script maintainers) |
| **Assessment Type** | Inventory & Compliance Verification |
| **Review Cycle** | Annual (full inventory), Quarterly (new systems update) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|---------|
| 1.0 | [Date] | Initial technical specification for Log Source Inventory assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.15.1-UG.

---

# Technical Specification

**Audience:** Workbook Developers (Python/Excel Script Maintainers)

---

# Workbook Structure Overview

| Sheet # | Sheet Name | Purpose | Row Estimate |
|---------|------------|---------|--------------|
| 1 | Instructions_Legend | Usage guide, color codes, dropdown values, scoring methodology | ~60 |
| 2 | System_Inventory | Complete system catalog with attributes | ~300-1000+ |
| 3 | Event_Requirements_Summary | Required events per system based on policy | ~300-1000+ |
| 4 | Authentication_Events | Authentication event logging verification | ~300-1000+ |
| 5 | Authorization_Events | Authorization event logging verification | ~300-1000+ |
| 6 | Administrative_Actions | Administrative action logging verification | ~300-1000+ |
| 7 | Security_Events | Security event logging verification | ~300-1000+ |
| 8 | System_Events | System event logging verification | ~300-1000+ |
| 9 | Network_Events | Network event logging verification | ~300-1000+ |
| 10 | Application_Events | Application event logging verification | ~300-1000+ |
| 11 | Gap_Analysis | Consolidated gaps requiring remediation | ~50-200 |
| 12 | Evidence_Register | Evidence catalog and linkage | ~100-500 |
| 13 | Approval_Sign_Off | Three-level approval workflow | ~30 |

**Total Sheets**: 13  
**Estimated Total Rows**: ~2,500-8,000+ (depends on environment size)

**Workbook Filename Format**: `ISMS-IMP-A.8.15.1_Log_Source_Inventory_YYYYMMDD.xlsx`

---

# Sheet 1: Instructions_Legend

## Header Section

**Cells A1:O1** (Merged):

- **Text**: "ISMS-IMP-A.8.15.1 - Log Source Inventory Assessment"
- **Font**: Calibri 20pt, Bold, White
- **Fill**: Dark Blue (#003366)
- **Alignment**: Center, Middle
- **Row Height**: 40px

**Cells A2:O2** (Merged):

- **Text**: "ISO/IEC 27001:2022 - Control A.8.15: Logging"
- **Font**: Calibri 14pt, White
- **Fill**: Dark Blue (#003366)
- **Alignment**: Center, Middle
- **Row Height**: 25px

## Document Information Block (Rows 4-14)

```
| Field (Col A) | Value (Col B-D, merged) | Styling |
|---------------|-------------------------|---------|
| Document ID | ISMS-IMP-A.8.15.1 | Bold label, normal value |
| Assessment Area | Log Source Inventory & Event Logging Completeness | Normal |
| Related Policy | ISMS-POL-A.8.15, Section 2.1 (Event Logging Requirements) | Blue hyperlink style |
| Version | 2.0 | Normal |
| Assessment Date | [USER INPUT - Yellow fill #FFEB9C] | Input cell |
| Completed By | [USER INPUT - Yellow fill #FFEB9C] | Input cell |
| Organization | [USER INPUT - Yellow fill #FFEB9C] | Input cell |
| Review Cycle | Annual (full), Quarterly (updates) | Normal |
```

## Status Dropdown Values (Rows 16-23)

**Table Headers** (Row 16): Status Value | Color | Meaning

- **Font**: Bold, Dark Blue (#003366)
- **Fill**: Light Blue (#BDD7EE)

**Data Rows** (17-22):
| Status | Fill Color | Text | Meaning |
|--------|------------|------|---------|
| Implemented | Green (#C6EFCE) | Dark Green (#006100) | Fully configured and verified |
| Partial | Yellow (#FFEB9C) | Dark Yellow (#9C5700) | Partially configured, gaps exist |
| Planned | Blue (#BDD7EE) | Dark Blue (#003366) | Scheduled, not yet implemented |
| Not Implemented | Red (#FFC7CE) | Dark Red (#9C0006) | Not configured or no capability |
| N/A | Gray (#D9D9D9) | Black | Not applicable to this system |

## Compliance Status Values (Rows 25-29)

| Status | Fill Color | Meaning |
|--------|------------|---------|
| Compliant | Green (#C6EFCE) | Meets all policy requirements |
| Partial Compliance | Yellow (#FFEB9C) | Meets some requirements, gaps exist |
| Non-Compliant | Red (#FFC7CE) | Does not meet requirements |

## Priority Values (for Gap Analysis) (Rows 31-35)

| Priority | Fill Color | Meaning |
|----------|------------|---------|
| Critical | Dark Red (#9C0006) white text | Immediate risk, address within 30 days |
| High | Red (#FF0000) | Significant risk, address within 90 days |
| Medium | Yellow (#FFEB9C) | Moderate risk, address within 180 days |
| Low | Blue (#BDD7EE) | Minor risk, address within 12 months |

## Instructions Summary (Rows 37-55)

**Title** (Row 37): "How to Use This Workbook"

- **Font**: Calibri 14pt, Bold, Dark Blue

**Steps** (Rows 38-55):
1. Start with Sheet 2 (System Inventory): Document all systems in environment
2. Complete Sheet 3 (Event Requirements): Determine what each system must log
3. Verify logging for each event category (Sheets 4-9)
4. Identify gaps in Sheet 10 (Gap_Analysis)
5. Collect evidence in Sheet 11 (Evidence_Register)
6. Review Summary Dashboard (Sheet 12)
7. Obtain approvals in Sheet 13 (Approval_Sign_Off)

**Key Points**:

- Use dropdown menus for consistent data entry
- Yellow-highlighted cells require user input
- Gray-shaded cells auto-calculate (do not edit formulas)
- Link evidence files for all non-compliant findings
- Review quality checklist before submission

## Scoring Methodology (Rows 57-60)

**Compliance Score Calculation**:

- **Compliant systems**: 100% weight
- **Partial compliance**: 50% weight
- **Non-compliant**: 0% weight
- **Formula**: `(Compliant_Count + 0.5 * Partial_Count) / Total_Applicable_Systems * 100`

---

# Sheet 2: System_Inventory

## Purpose
Complete catalog of all systems that should be logging per ISMS-POL-A.8.15, Section 1.4 (Scope).

## Column Specifications

| Col | Column Name | Width | Data Type | Data Validation | Conditional Formatting |
|-----|-------------|-------|-----------|-----------------|------------------------|
| A | System ID | 12 | Text | None (auto-increment SYS-001) | None |
| B | System Name | 25 | Text | None | None |
| C | System Type | 20 | Dropdown | Server, Application, Network Device, Security Tool, Database, Cloud Service, Authentication System, Other | None |
| D | System Owner | 20 | Text | Email format validation (optional) | None |
| E | Business Function | 25 | Text | None | None |
| F | Data Classification | 18 | Dropdown | Public, Internal, Confidential, Restricted | Color: Public=Green, Internal=Yellow, Confidential=Orange, Restricted=Red |
| G | System Criticality | 15 | Dropdown | Critical, High, Standard, Low | Color: Critical=Red, High=Orange, Standard=Yellow, Low=Green |
| H | Deployment Model | 18 | Dropdown | On-Premises, Cloud (IaaS), Cloud (PaaS), Cloud (SaaS), Hybrid, Third-Party Hosted | None |
| I | OS / Platform | 20 | Text | None | None |
| J | Vendor / Manufacturer | 20 | Text | None | None |
| K | Logging Capability | 15 | Dropdown | Yes, Partial, No, Unknown | Color: Yes=Green, Partial=Yellow, No/Unknown=Red |
| L | Log Forwarding Status | 18 | Dropdown | Implemented, Partial, Planned, Not Implemented, N/A | Status color scheme |
| M | SIEM Integration | 15 | Dropdown | Yes, No, Planned, N/A | Yes=Green, No=Red, Planned=Yellow |
| N | Notes | 30 | Text | None | None |

**Header Row** (Row 1):

- **Font**: Bold, White
- **Fill**: Dark Blue (#003366)
- **Alignment**: Center, Middle, Wrap Text
- **Row Height**: 45px
- **Freeze Panes**: Row 2 (header always visible)

**Data Rows** (Starting Row 2):

- **Row Height**: Auto (minimum 20px)
- **Borders**: Light gray (#D9D9D9) grid lines
- **Alternating Row Colors**: White / Light Gray (#F2F2F2) for readability

**Auto-Increment Formula** (Column A, starting A2):
```excel
="SYS-" & TEXT(ROW()-1, "000")
```

**Data Validation Examples**:

Column C (System Type):

- List: `Server, Application, Network Device, Security Tool, Database, Cloud Service, Authentication System, Other`
- Input Message: "Select the primary system type"
- Error Alert: "Please select a valid system type from the list"

Column F (Data Classification):

- List: `Public, Internal, Confidential, Restricted`
- Input Message: "Per organizational data classification policy"

Column G (System Criticality):

- List: `Critical, High, Standard, Low`
- Input Message: "Critical = Major business disruption if unavailable; High = Significant impact; Standard = Manageable impact; Low = Minimal impact"

**Conditional Formatting Rules**:

Data Classification (Column F):
```excel
Rule 1: If F2="Public" then Fill=Green (#C6EFCE)
Rule 2: If F2="Internal" then Fill=Yellow (#FFEB9C)
Rule 3: If F2="Confidential" then Fill=Orange (#FFC000)
Rule 4: If F2="Restricted" then Fill=Red (#FFC7CE)
```

System Criticality (Column G):
```excel
Rule 1: If G2="Critical" then Fill=Red (#FFC7CE)
Rule 2: If G2="High" then Fill=Orange (#FFC000)
Rule 3: If G2="Standard" then Fill=Yellow (#FFEB9C)
Rule 4: If G2="Low" then Fill=Green (#C6EFCE)
```

Logging Capability (Column K):
```excel
Rule 1: If K2="Yes" then Fill=Green (#C6EFCE)
Rule 2: If K2="Partial" then Fill=Yellow (#FFEB9C)
Rule 3: If K2 IN ("No","Unknown") then Fill=Red (#FFC7CE)
```

---

# Sheet 3: Event_Requirements_Summary

## Purpose
Determines WHAT events each system must log based on system attributes and policy requirements (ISMS-POL-A.8.15, Section 2.1 + Annex A).

## Column Specifications

| Col | Column Name | Width | Data Type | Formula / Validation | Notes |
|-----|-------------|-------|-----------|---------------------|-------|
| A | System ID | 12 | Reference | `='System_Inventory'!A2` | External reference to Sheet 2 |
| B | System Name | 25 | Reference | `='System_Inventory'!B2` | External reference |
| C | System Type | 20 | Reference | `='System_Inventory'!C2` | External reference |
| D | Data Classification | 18 | Reference | `='System_Inventory'!F2` | External reference |
| E | System Criticality | 15 | Reference | `='System_Inventory'!G2` | External reference |
| F | Required Event Categories | 30 | Calculated | See formula below | Comma-separated list |
| G | Authentication Events? | 15 | Calculated | See formula | Yes (All), Yes (Failures Only), No |
| H | Authorization Events? | 15 | Calculated | See formula | Yes, No |
| I | Administrative Actions? | 15 | Calculated | Yes always | Yes, No |
| J | Security Events? | 15 | Calculated | Yes always | Yes, No |
| K | System Events? | 15 | Calculated | See formula | Yes, No |
| L | Network Events? | 15 | Calculated | See formula | Yes, No, N/A |
| M | Application Events? | 15 | Calculated | See formula | Yes, No, N/A |
| N | Retention (Online) | 12 | Calculated | See formula | Months |
| O | Retention (Archive) | 12 | Calculated | See formula | Years |
| P | Special Regulatory? | 18 | Manual Input | Dropdown | None, PCI DSS, HIPAA, SOX, GDPR/nDSG, Multiple |
| Q | Rationale | 40 | Calculated | See formula | Auto-generated explanation |

**Formula Examples**:

Column F (Required Event Categories):
```excel
=IF(OR(E2="Critical", D2="Restricted"), 
  "Authentication, Authorization, Administrative, Security, System, Network, Application",
  IF(OR(E2="High", D2="Confidential"),
    "Authentication, Authorization, Administrative, Security, System, Application",
    IF(E2="Standard",
      "Authentication, Administrative, Security",
      "Authentication (Failures), Administrative, Critical Security Events"
    )
  )
)
```

Column G (Authentication Events Required):
```excel
=IF(OR(E2="Critical", E2="High", E2="Standard", D2<>"Public"), 
  "Yes (All)", 
  "Yes (Failures Only)"
)
```

Column H (Authorization Events Required):
```excel
=IF(OR(E2="Critical", E2="High", D2="Restricted", D2="Confidential"), "Yes", "No")
```

Column N (Retention Online - Months):
```excel
=IF(OR(E2="Critical", D2="Restricted", D2="Confidential"), 12,
  IF(E2="High", 6, 3)
)
```

Column O (Retention Archive - Years):
```excel
=IF(OR(E2="Critical", D2="Restricted", D2="Confidential", P2<>"None"), 7,
  IF(E2="High", 1, 0.5)
)
```

Column Q (Rationale):
```excel
=IF(E2="Critical",
  "Critical system requires comprehensive logging per ISMS-POL-A.8.15, Annex A.1",
  IF(D2="Restricted",
    "Restricted data requires comprehensive logging per ISMS-POL-A.8.15, Annex A.1",
    IF(OR(E2="High", D2="Confidential"),
      "High-value system/Confidential data requires detailed logging per ISMS-POL-A.8.15, Section 2.1",
      "Standard logging requirements per ISMS-POL-A.8.15, Section 2.1"
    )
  )
)
```

**Cell Protection**:

- Columns A-O: **LOCKED** (formulas protected)
- Column P: **UNLOCKED** (user input allowed)
- Column Q: **LOCKED** (calculated)

---

# Sheets 4-9: Event Category Verification

These sheets follow identical structure. Only column names and specific event checklists differ.

## Common Column Structure

| Col | Column Name | Width | Data Type | Source / Validation |
|-----|-------------|-------|-----------|---------------------|
| A | System ID | 12 | Reference | From Sheet 2 |
| B | System Name | 25 | Reference | From Sheet 2 |
| C | Logging Required? | 15 | Reference | From Sheet 3 (appropriate column) |
| D | Logging Status | 15 | Dropdown | Implemented, Partial, Not Implemented, N/A |
| E | Log Format | 18 | Dropdown | Syslog, CEF, JSON, Windows Event Log, Proprietary, Other |
| F | Log Location | 18 | Dropdown | Local Only, SIEM, Cloud Service, Both (Local+SIEM) |
| G | Specific Events Logged | 40 | Checklist Text | Multi-line text with checkbox ASCII: [X] or [ ] |
| H | Sample Log Entry | 40 | Text | Copy/paste of actual log entry |
| I | Verification Method | 20 | Dropdown | Configuration Review, Log Sample, Owner Confirmation, Documentation Review |
| J | Verification Date | 12 | Date | Date picker |
| K | Verified By | 18 | Text | Name or email |
| L | Compliance Status | 15 | Dropdown | Compliant, Non-Compliant, Partial Compliance |
| M | Gap Description | 30 | Text | Required if L="Non-Compliant" or "Partial" |
| N | Evidence Reference | 15 | Text | Link to Sheet 11 (e.g., "EVD-045") |
| O | Notes | 25 | Text | Additional context |

**Conditional Formatting** (Column L - Compliance Status):
```excel
Rule 1: If L2="Compliant" then Fill=Green (#C6EFCE)
Rule 2: If L2="Partial Compliance" then Fill=Yellow (#FFEB9C)
Rule 3: If L2="Non-Compliant" then Fill=Red (#FFC7CE)
```

**Data Validation** (Column G - Specific Events):

- Type: Text (multi-line allowed)
- Input Message: "Check all events that are logged. Use [X] for yes, [ ] for no. See ISMS-POL-A.8.15, Section 2.1 for required events."

**Formula for Column C (Example - Sheet 4 Authentication Events)**:
```excel
='Event_Requirements_Summary'!G2
```
(References appropriate column from Sheet 3 depending on event category)

---

## Sheet 4: Authentication_Events - Specific Details

**Column G Sample Content** (Specific Events Logged):
```
Per ISMS-POL-A.8.15, Section 2.1:
[X] Successful login attempts (user ID, timestamp, source IP, method)
[X] Failed login attempts (user ID, timestamp, source IP, failure reason)
[X] Logout events (user ID, session duration, timestamp)
[ ] Account lockouts (user ID, lockout reason, timestamp)
[X] Password changes/resets (user ID, timestamp, initiated by)
[ ] Multi-factor authentication events (MFA success/failure, method, timestamp)
```

---

## Sheet 5: Authorization_Events - Specific Details

**Column G Sample Content**:
```
Per ISMS-POL-A.8.15, Section 2.1:
[X] Access to sensitive data (user, classification, action, timestamp)
[X] Privilege escalation (user, escalated privileges, justification, timestamp)
[ ] Access control changes (modified permissions, affected resources, initiator)
[X] File/object access for classified data (user, resource, action, outcome)
[X] Denied access attempts (user, attempted resource, denial reason, timestamp)
```

---

## Sheet 6: Administrative_Actions - Specific Details

**Column G Sample Content**:
```
Per ISMS-POL-A.8.15, Section 2.1:
[X] System configuration changes (parameters, previous/new values, admin, timestamp)
[X] User account creation/modification/deletion (affected user, changes, admin)
[X] Privilege grants/revocations (affected user, privilege type, admin, timestamp)
[ ] Security policy changes (policy modified, details, admin, approval ref)
[X] Installation/removal of software/services (package, version, admin, timestamp)
[ ] Firmware/system updates (system ID, update applied, admin, timestamp)
```

---

## Sheet 7: Security_Events - Specific Details

**Column G Sample Content**:
```
Per ISMS-POL-A.8.15, Section 2.1:
[X] Malware detection/prevention (malware type, system, action, timestamp)
[X] Intrusion detection/prevention alerts (alert type, source/dest, action)
[X] Firewall blocks/rule violations (source/dest, protocol/port, rule violated)
[ ] Data loss prevention (DLP) events (data type, egress channel, action)
[ ] Encryption/decryption operations (user, operation type, data classification)
[X] Certificate validation failures (certificate subject, validation error)
[ ] Security tool configuration changes (tool name, config modified, admin)
```

---

## Sheet 8: Application_Database - Specific Details

**Column G Sample Content**:
```
Per ISMS-POL-A.8.15, Section 2.1:
[X] Application errors/exceptions (app name, error type, error details, timestamp)
[X] Database transactions with sensitive data (user, table/record, operation)
[X] API authentication/authorization (API endpoint, user/service account, outcome)
[ ] Data export operations (user, data scope, export format, destination)
[X] Application-level access control decisions (user, requested resource, decision)
```

---

## Sheet 9: Network_Device_Logging - Specific Details

**Column G Sample Content**:
```
Per ISMS-POL-A.8.15, Section 2.1:
[X] Firewall rule matches for security traffic (source/dest, rule, action)
[X] VPN connections/disconnections (user ID, VPN gateway, connection duration)
[ ] Network segmentation traversals (source/dest segment, protocol, user context)
[ ] DNS query anomalies (queried domain, source system, response, timestamp)
[X] Network device configuration changes (device ID, config modified, admin)
```

---

# Sheet 10: Gap_Analysis

## Purpose
Consolidated list of all logging gaps requiring remediation.

## Column Specifications

| Col | Column Name | Width | Data Type | Data Validation |
|-----|-------------|-------|-----------|-----------------|
| A | Gap ID | 10 | Text | Auto-increment (GAP-001) |
| B | System ID | 12 | Reference | From System_Inventory |
| C | System Name | 25 | Reference | From System_Inventory |
| D | Gap Category | 20 | Dropdown | Missing Log Source, Incomplete Events, No Log Forwarding, Retention Non-Compliance, Format Issues, Other |
| E | Gap Description | 40 | Text | Detailed description of the gap |
| F | Policy Reference | 25 | Text | E.g., "ISMS-POL-A.8.15, Section 2.1 - Authentication Events" |
| G | Risk Severity | 12 | Dropdown | Critical, High, Medium, Low |
| H | Business Impact | 30 | Text | What is the impact if not remediated? |
| I | Proposed Remediation | 35 | Text | Actionable remediation steps |
| J | Responsible Owner | 18 | Text | Name or email of person responsible |
| K | Target Date | 12 | Date | Remediation deadline |
| L | Status | 15 | Dropdown | Open, In Progress, Resolved, Accepted Risk |
| M | Evidence Reference | 15 | Text | Link to Sheet 11 (e.g., "EVD-087") |
| N | Notes | 25 | Text | Additional context |

**Auto-Increment Formula** (Column A):
```excel
="GAP-" & TEXT(ROW()-1, "000")
```

**Conditional Formatting** (Column G - Risk Severity):
```excel
Rule 1: If G2="Critical" then Fill=Dark Red (#9C0006), Font=White
Rule 2: If G2="High" then Fill=Red (#FF0000)
Rule 3: If G2="Medium" then Fill=Yellow (#FFEB9C)
Rule 4: If G2="Low" then Fill=Blue (#BDD7EE)
```

**Conditional Formatting** (Column L - Status):
```excel
Rule 1: If L2="Resolved" then Fill=Green (#C6EFCE)
Rule 2: If L2="In Progress" then Fill=Yellow (#FFEB9C)
Rule 3: If L2="Open" then Fill=Red (#FFC7CE)
Rule 4: If L2="Accepted Risk" then Fill=Gray (#D9D9D9)
```

**Data Validation** (Column G - Risk Severity):

- List: `Critical, High, Medium, Low`
- Input Message: "Critical = Immediate risk (30 days); High = Significant risk (90 days); Medium = Moderate risk (180 days); Low = Minor risk (12 months)"

**Target Date Auto-Suggestion** (Column K - based on severity):
```excel
=IF(G2="Critical", TODAY()+30,
  IF(G2="High", TODAY()+90,
    IF(G2="Medium", TODAY()+180,
      IF(G2="Low", TODAY()+365, ""))))
```
(User can override this suggested date)

---

# Sheet 11: Evidence_Register

## Purpose
Catalog all evidence files supporting assessment findings.

## Column Specifications

| Col | Column Name | Width | Data Type | Notes |
|-----|-------------|-------|-----------|-------|
| A | Evidence ID | 12 | Text | Auto-increment (EVD-001) |
| B | Related System ID(s) | 20 | Text | Comma-separated list if evidence covers multiple systems |
| C | Evidence Type | 20 | Dropdown | Configuration Screenshot, Sample Log, Owner Confirmation, Vendor Doc, SIEM Screenshot, Other |
| D | Description | 40 | Text | What does this evidence show? |
| E | File Location | 50 | Hyperlink | Network path, SharePoint link, or "Email dated DD.MM.YYYY" |
| F | Collection Date | 12 | Date | When was evidence collected? |
| G | Collected By | 18 | Text | Who collected this evidence? |
| H | Notes | 25 | Text | Additional context |

**Auto-Increment Formula** (Column A):
```excel
="EVD-" & TEXT(ROW()-1, "000")
```

**Hyperlink Format** (Column E):
```excel
=HYPERLINK("\\fileserver\share\A.8.15.1\Evidence\" & A2 & "_filename.png", "Link to Evidence")
```

**Conditional Formatting** (Column F - highlight old evidence):
```excel
Rule 1: If F2 < TODAY()-90 then Fill=Orange (#FFC000)
```
(Evidence older than 90 days may be stale)

---

# Sheet 12: Summary_Dashboard

## Purpose
Overall compliance metrics and summary view for management review.

## Structure

**Title Block** (Rows 1-3):
- **Row 1**: "Log Source Inventory - Summary Dashboard"
- **Row 2**: "ISMS-IMP-A.8.15.1"
- **Row 3**: Assessment Date: [Auto-populated]

**Compliance Summary** (Rows 5-12):

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Systems Assessed | [Count from Sheet 2] | - | - |
| Fully Compliant Systems | [Count] | 100% | [%] |
| Partially Compliant | [Count] | 0% | [%] |
| Non-Compliant | [Count] | 0% | [%] |
| Open Gaps | [Count from Sheet 10] | 0 | - |
| Critical Gaps | [Count] | 0 | - |

**By Event Category** (Rows 14-22):

| Event Category | Compliant | Partial | Non-Compliant |
|----------------|-----------|---------|---------------|
| Authentication (Sheet 4) | [Count] | [Count] | [Count] |
| Authorization (Sheet 5) | [Count] | [Count] | [Count] |
| Administrative (Sheet 6) | [Count] | [Count] | [Count] |
| Security (Sheet 7) | [Count] | [Count] | [Count] |
| Application/Database (Sheet 8) | [Count] | [Count] | [Count] |
| Network (Sheet 9) | [Count] | [Count] | [Count] |

**Formulas**:
```excel
Total Systems: =COUNTA('System_Inventory'!A:A)-1
Fully Compliant: =COUNTIF('Gap_Analysis'!L:L,"Compliant")
Open Gaps: =COUNTA('Gap_Analysis'!A:A)-1
Critical Gaps: =COUNTIF('Gap_Analysis'!G:G,"Critical")
```

**Conditional Formatting**:
- Overall compliance >= 90%: Green
- Overall compliance 70-89%: Yellow
- Overall compliance < 70%: Red

---

# Sheet 13: Approval_Sign_Off

## Purpose
Three-level approval workflow for assessment validation.

## Structure

**Title Block** (Rows 1-3):

- **Row 1**: "Assessment Approval & Sign-Off"
- **Row 2**: "ISMS-IMP-A.8.15.1 - Log Source Inventory Assessment"
- **Row 3**: "Version 1.0"

**Approval Table** (Rows 5-15):

| Col A | Col B | Col C | Col D | Col E |
|-------|-------|-------|-------|-------|
| **Approval Level** | **Role** | **Name** | **Signature / Date** | **Comments** |
| Level 1 | System Owners | [Multiple rows] | [Date] | [Optional feedback] |
| Level 2 | IT Operations Manager | [Name] | [Date] | Inventory completeness certified |
| Level 3 | Information Security Manager / CISO | [Name] | [Date] | Assessment approved, remediation authorized |

**System Owner Approval Rows** (Rows 6-10, expandable):

- One row per System Owner
- Column B: System Owner Name
- Column C: Systems Owned (list)
- Column D: Signature/Date
- Column E: Confirmation statement: "I confirm the logging assessment for my systems is accurate"

**IT Operations Manager Approval** (Row 12):

- Column B: IT Operations Manager
- Column C: [Name]
- Column D: [Date]
- Column E: "I certify the system inventory is complete and logging configurations are technically accurate"

**InfoSec Manager / CISO Approval** (Row 14):

- Column B: Information Security Manager / CISO
- Column C: [Name]
- Column D: [Date]
- Column E: "I approve this assessment and authorize the remediation plan per Sheet 10 (Gap_Analysis)"

**Conditional Formatting** (Approval status):
```excel
If signature/date cell is blank: Fill=Red (pending approval)
If signature/date cell has content: Fill=Green (approved)
```

---

# Python Script Usage Notes

## Script Name
`generate_a815_1_log_source_inventory.py`

## Purpose
Generates the ISMS-IMP-A.8.15.1 Excel workbook with all 13 sheets, data validation, conditional formatting, formulas, and cell protection.

## Key Customization Points (marked with `# CUSTOMIZE:` in script)

1. **Sheet Names**: If organizational naming conventions differ
2. **Dropdown Options**: If additional status values needed beyond standard set
3. **Data Validation Rules**: If custom compliance criteria required
4. **Conditional Formatting Thresholds**: If different risk color coding desired
5. **Formula Logic**: If organizational policy has different criticality/classification definitions
6. **Cell Protection**: If different cells need to be unlocked for user input

## Quality Assurance

**Validation Script**: `excel_sanity_check_a815_1.py`

- Validates sheet structure matches this specification
- Checks all data validation rules applied correctly
- Verifies conditional formatting ranges accurate
- Tests formula calculations
- Reports discrepancies between generated workbook and specification

## Version Control

**Workbook Versioning**:

- Filename format: `ISMS-IMP-A.8.15.1_Log_Source_Inventory_YYYYMMDD.xlsx`
- Version tracking in Instructions_Legend sheet (Document Control block)
- Document Control section updated with each revision

**Change Log**:

- v1.0: Initial workbook structure with consolidated policy references to ISMS-POL-A.8.15

**Compatibility**:

- Workbooks can be opened in Excel 2016+
- Requires openpyxl 3.0+ for Python generation

---

# Integration Points

## External References

**From Other Assessment Workbooks**:

- ISMS-IMP-A.8.15.2 (Log Collection & Centralization) references this workbook's System_Inventory sheet for log source list
- ISMS-IMP-A.8.15.5 (Compliance Dashboard) references this workbook's compliance scores and gap counts

**To Policy Documents**:

- All "Related Policy" references point to consolidated ISMS-POL-A.8.15-Logging.md
- Specific section references: Section 2.1 (Event Logging Requirements), Annex A (Logging Decision Matrix)

**To Technical Reference**:

- ISMS-REF-A.8.15 (Logging Standards Reference) provides detailed log format specifications referenced in this assessment

## Data Flow

```
System Inventory (Sheet 2)
  |
  v
Event Requirements (Sheet 3) - Determines what to log based on system attributes
  |
  v
Event Category Verification (Sheets 4-9) - Verifies actual configuration
  |
  v
Gap_Analysis (Sheet 10) - Consolidates non-compliance findings
  |
  v
Evidence_Register (Sheet 11) - Links supporting evidence
  |
  v
Summary_Dashboard (Sheet 12) - Overall compliance metrics
  |
  v
Approval_Sign_Off (Sheet 13) - Three-level sign-off
  |
  v
External: Dashboard Consolidation (IMP-A.8.15.5) - Aggregates this + other assessments
```

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

**Document Assembly Complete**: ISMS-IMP-A.8.15.1 consists of Part I (User Completion Guide) + Part II (Technical Specification)

**Total Document Length**: ~1,600 lines (Part I: ~600 lines, Part II: ~1,000 lines)

**Quality Review**: All policy references updated to consolidated ISMS-POL-A.8.15-Logging.md (v1.0)

---

**END OF SPECIFICATION**

---

*"Once you stop learning, you start dying."*
- Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
