**ISMS-IMP-A.8.1-7-18-19-S5-TG - Privileged Utility Management**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.1: User Endpoint Devices

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Privileged Utility Programs Access and Usage Control |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19, Section 2.3 (Privileged Utility Management) |
| **Purpose** | Document privileged utilities, assess access controls, verify usage monitoring, track approval workflows |
| **Target Audience** | Security Engineers, IT Operations, System Administrators, Privileged Access Management Team, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Monthly (usage monitoring), Quarterly (full assessment) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guide for privileged utility assessment | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.1-7-18-19-S5-UG.

---

# Technical Specification

## Workbook Structure

**File Name:** `Privileged_Utilities_Assessment.xlsx`

**Sheets (11 total):**
1. Instructions & Legend
2. Utility_Inventory
3. Access_Controls
4. Approval_Workflow
5. Usage_Audit
6. MFA_Compliance
7. Quarterly_Reviews
8. Capability_Requirements
9. Evidence_Register
10. Gap_Analysis
11. Approval_Sign_Off

---

## Sheet 1: Instructions & Legend

### Header Section (Rows 1-2)
```
Row 1: "ISMS-IMP-A.8.1-7-18-19-S5 - Privileged Utility Management Assessment"
       (Dark blue #003366, white text, centered, merged A1:H1, height 40px)
Row 2: "ISO/IEC 27001:2022 - Controls A.8.1, A.8.7, A.8.18, A.8.19: Endpoint Security"
       (Medium blue #4472C4, white text, centered, merged A2:H2, height 30px)
```

### Document Information (Rows 4-12)
```
Document ID:           ISMS-IMP-A.8.1-7-18-19-S5
Assessment Area:       Privileged Utility Programs Access & Usage Control
Related Policy:        ISMS-POL-A.8.1-7-18-19, Section 2.3
Version:               1.0
Assessment Date:       [USER INPUT - yellow #FFEB9C]
Completed By:          [USER INPUT - yellow]
Organization:          [USER INPUT - yellow]
Review Cycle:          Monthly (usage monitoring), Quarterly (full)
Next Review Date:      [FORMULA: =B8+30]
```

### How to Use (Rows 14-23)
1. Identify privileged utilities (Sheet 2)
2. Document access controls (Sheet 3)
3. Assess approval workflows (Sheet 4)
4. Verify usage monitoring (Sheet 5)
5. Identify security bypass tools (Sheet 6)
6. Consolidate gaps (Sheet 7)
7. Register evidence (Sheet 8)
8. Review dashboard (Sheet 9)
9. Obtain three-level approval

### Status Legend (Rows 25-33)

| Symbol | Status | Description | Color |
|--------|--------|-------------|-------|
| ✅ | Controlled | Access restricted and monitored | Green #C6EFCE |
| ⚠️ | Partial Control | Some controls but gaps | Yellow #FFEB9C |
| ❌ | Uncontrolled | No access restrictions | Red #FFC7CE |
| 🔴 | Critical Risk | Security bypass tool uncontrolled | Dark Red #C00000 |
| 🟢 | Enforced | Access control actively blocking | Green #00B050 |
| 🟡 | Audit Mode | Logging only, not blocking | Yellow #FFFF00 |

### Control Thresholds (Rows 35-40)

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| Access Control Deployment | ≥95% | 85-94% | <85% |
| Logging/Monitoring | ≥95% | 85-94% | <85% |
| Approval Workflow | 100% | ≥90% | <90% |
| Recertification Current | ≤90 days | 90-180 days | >180 days |
| Security Bypass Tools | 0 uncontrolled | 1-2 controlled | >0 uncontrolled |

---

## Sheet 2: Utility_Inventory

### Purpose
Complete inventory of privileged utilities present on endpoints.

### Header (Rows 1-2)
```
Row 1: "PRIVILEGED UTILITY INVENTORY" (merged A1:O1, medium blue #4472C4)
Row 2: "Complete inventory of privileged utilities by category" (merged A2:O2)
```

### Column Structure (Row 3 - headers, Rows 4-203 - data, 200 rows)

| Col | Header | Type | Width | Validation |
|-----|--------|------|-------|------------|
| A | Utility ID | Auto | 10 | UTIL-001... |
| B | Utility Name | Text | 30 | Official name (yellow #FFEB9C) |
| C | Category | Dropdown | 20 | System Admin / Remote Access / Debug/Dev / Password/Cred / Network Analysis / Security Bypass |
| D | OS Type | Dropdown | 12 | Windows / macOS / Linux / Cross-Platform |
| E | Installation | Dropdown | 15 | Pre-installed / Centrally Deployed / User Installed |
| F | Endpoints with Utility | Number | 12 | Count |
| G | % of Total Endpoints | Formula | 10 | =(F4/TotalEndpoints)*100 |
| H | Risk Level | Dropdown | 10 | Critical / High / Medium / Low |
| I | Risk Justification | Text | 40 | Why this risk level |
| J | Business Justification | Text | 40 | Why needed |
| K | Primary Users | Text | 30 | Who needs it (role/team) |
| L | Usage Frequency | Dropdown | 15 | Daily / Weekly / Monthly / Rarely |
| M | Alternative Available | Dropdown | 10 | Yes / No |
| N | Alternative Tool | Text | 30 | If yes, what alternative |
| O | Notes | Text | 40 | Additional info |

### Utility Summary (Rows 205-220)
```
Total Privileged Utilities:  [=COUNT(A4:A203 where not blank)]

By Category:
  System Admin:              [=COUNTIF(C4:C203,"System Admin")]
  Remote Access:             [=COUNTIF(C4:C203,"Remote Access")]
  Debug/Dev:                 [=COUNTIF(C4:C203,"Debug/Dev")]
  Password/Cred:             [=COUNTIF(C4:C203,"Password/Cred")]
  Network Analysis:          [=COUNTIF(C4:C203,"Network Analysis")]
  Security Bypass:           [=COUNTIF(C4:C203,"Security Bypass")]

By Risk Level:
  Critical:                  [=COUNTIF(H4:H203,"Critical")]
  High:                      [=COUNTIF(H4:H203,"High")]
  Medium:                    [=COUNTIF(H4:H203,"Medium")]
  Low:                       [=COUNTIF(H4:H203,"Low")]

By Installation:
  Pre-installed:             [=COUNTIF(E4:E203,"Pre-installed")]
  Centrally Deployed:        [=COUNTIF(E4:E203,"Centrally Deployed")]
  User Installed:            [=COUNTIF(E4:E203,"User Installed")]
```

### Conditional Formatting

**Risk Level Column (H):**

- If "Critical" → Dark red #C00000, white text
- If "High" → Red #FFC7CE
- If "Medium" → Yellow #FFEB9C
- If "Low" → Green #C6EFCE

**Category Column (C):**

- If "Security Bypass" → Red #FFC7CE
- Else → Light blue #D9E1F2

---

## Sheet 3: Access_Control

### Purpose
Per-endpoint and per-utility access control assessment.

### Header (Rows 1-2)
```
Row 1: "ACCESS CONTROL ASSESSMENT"
Row 2: "Who can access privileged utilities and how access is enforced"
```

### Column Structure (Row 3 - headers, Rows 4-203 - data, 200 rows)

| Col | Header | Type | Width | Formula/Validation |
|-----|--------|------|-------|-------------------|
| A | Utility Name | Text | 30 | From Sheet 2 col B |
| B | Access Control Mechanism | Dropdown | 20 | AppLocker / WDAC / PAM / sudo / SELinux / MDM / GPO / None |
| C | Deployment Status | Dropdown | 12 | 🟢 Deployed / 🟡 Partial / 🔴 Not Deployed |
| D | Enforcement Mode | Dropdown | 12 | Enforce / Audit / Disabled |
| E | Access Granted To | Text | 40 | RBAC groups or individuals |
| F | User Count | Number | 10 | Total users with access |
| G | Access Type | Dropdown | 15 | Standing / Temporary / Emergency |
| H | Standing Access Users | Number | 10 | Count with permanent access |
| I | Temporary Access Users | Number | 10 | Count with time-limited |
| J | Emergency Access Accounts | Number | 10 | Break-glass count |
| K | Access Test Date | Date | 12 | When tested |
| L | Access Test Result | Dropdown | 12 | ✅ Pass / ❌ Fail / Not Tested |
| M | Test Details | Text | 40 | What was tested |
| N | Control Status | Formula | 12 | =IF(AND(C4="🟢",D4="Enforce"),"✅ Controlled",IF(D4="Audit","⚠️ Audit","❌ Uncontrolled")) |
| O | Remediation Required | Formula | 10 | =IF(N4="❌ Uncontrolled","Yes","No") |
| P | Notes | Text | 40 | Additional |

### Access Control Metrics (Rows 205-220)
```
Total Utilities Assessed:    [=COUNT(A4:A203 where not blank)]

Deployment Status:
  Deployed:                  [=COUNTIF(C4:C203,"🟢 Deployed")]
  Partial:                   [=COUNTIF(C4:C203,"🟡 Partial")]
  Not Deployed:              [=COUNTIF(C4:C203,"🔴 Not Deployed")]
  Deployment %:              [=Deployed/Total*100]

Enforcement Mode:
  Enforce:                   [=COUNTIF(D4:D203,"Enforce")]
  Audit:                     [=COUNTIF(D4:D203,"Audit")]
  Disabled:                  [=COUNTIF(D4:D203,"Disabled")]
  Enforcement %:             [=Enforce/(Enforce+Audit)*100]

Access Testing:
  Pass:                      [=COUNTIF(L4:L203,"✅ Pass")]
  Fail:                      [=COUNTIF(L4:L203,"❌ Fail")]
  Not Tested:                [=COUNTIF(L4:L203,"Not Tested")]

Control Status:
  Controlled:                [=COUNTIF(N4:N203,"✅ Controlled")]
  Audit Mode:                [=COUNTIF(N4:N203,"⚠️ Audit")]
  Uncontrolled:              [=COUNTIF(N4:N203,"❌ Uncontrolled")]
  Control %:                 [=Controlled/Total*100]

Targets:
  Deployment: ≥95%
  Enforcement: ≥95%
  Testing: 100%
```

### Conditional Formatting

**Deployment Status Column (C):**

- If "🟢 Deployed" → Green #C6EFCE
- If "🟡 Partial" → Yellow #FFEB9C
- If "🔴 Not Deployed" → Red #FFC7CE

**Enforcement Mode Column (D):**

- If "Enforce" → Green #C6EFCE
- If "Audit" → Yellow #FFEB9C
- If "Disabled" → Red #FFC7CE

**Control Status Column (N):**

- If "✅ Controlled" → Green #C6EFCE
- If "⚠️ Audit" → Yellow #FFEB9C
- If "❌ Uncontrolled" → Red #FFC7CE

**Test Result Column (L):**

- If "✅ Pass" → Green #C6EFCE
- If "❌ Fail" → Red #FFC7CE
- If "Not Tested" → Light gray #D9D9D9

---

## Sheet 4: Approval_Workflow

### Purpose
Document approval process for privileged utility access.

### Header (Rows 1-2)
```
Row 1: "APPROVAL WORKFLOW ASSESSMENT"
Row 2: "Approval process for privileged utility access requests"
```

### Column Structure (Row 3 - headers, Rows 4-103 - data, 100 rows for recent approvals)

| Col | Header | Type | Width | Validation |
|-----|--------|------|-------|------------|
| A | Request ID | Text | 12 | Ticket number |
| B | Request Date | Date | 12 | When requested |
| C | Requestor | Text | 20 | Who requested |
| D | Utility Requested | Text | 30 | Which utility |
| E | Access Type | Dropdown | 12 | Standing / Temporary / Emergency |
| F | Duration | Text | 15 | If temporary, how long |
| G | Business Justification | Text | 40 | Why needed |
| H | Manager Approval | Dropdown | 12 | Approved / Denied / Pending |
| I | Manager Approver | Text | 20 | Who approved |
| J | Security Review | Dropdown | 12 | Approved / Denied / Pending |
| K | Security Reviewer | Text | 20 | Who reviewed |
| L | Final Approval | Dropdown | 12 | Approved / Denied / Pending |
| M | Final Approver | Text | 20 | Who approved |
| N | Approval Date | Date | 12 | When granted |
| O | Days to Approve | Formula | 10 | =INT(N4-B4) |
| P | Access Granted Date | Date | 12 | When provisioned |
| Q | Expiration Date | Date | 12 | If temporary |
| R | Recertification Date | Date | 12 | Next review |
| S | Status | Dropdown | 12 | Active / Expired / Revoked |
| T | Notes | Text | 40 | Additional |

### Approval Workflow Metrics (Rows 105-125)
```
Total Requests (Period):     [=COUNT(A4:A103 where not blank)]

Request Status:
  Approved:                  [=COUNTIF(H4:H103,"Approved")] ([%])
  Denied:                    [=COUNTIF(H4:H103,"Denied")] ([%])
  Pending:                   [=COUNTIF(H4:H103,"Pending")] ([%])

By Access Type:
  Standing:                  [=COUNTIF(E4:E103,"Standing")]
  Temporary:                 [=COUNTIF(E4:E103,"Temporary")]
  Emergency:                 [=COUNTIF(E4:E103,"Emergency")]

Approval Quality:
  All Levels Complete:       [Count where H,J,L all "Approved"]
  Missing Levels:            [Count where any H,J,L "Pending" but granted]
  
Approval Time:
  Average Days to Approve:   [=AVERAGE(O4:O103 where approved)]
  Median Days:               [=MEDIAN(O4:O103 where approved)]
  >7 Days (slow):            [=COUNTIF(O4:O103,">7")]

Current Status:
  Active:                    [=COUNTIF(S4:S103,"Active")]
  Expired:                   [=COUNTIF(S4:S103,"Expired")]
  Revoked:                   [=COUNTIF(S4:S103,"Revoked")]

Recertification:
  Due Within 30 Days:        [=COUNTIFS(R:R,"<="&TODAY()+30,S:S,"Active")]
  Overdue:                   [=COUNTIFS(R:R,"<"&TODAY(),S:S,"Active")]
```

### Conditional Formatting

**Approval Columns (H, J, L):**

- If "Approved" → Green #C6EFCE
- If "Denied" → Red #FFC7CE
- If "Pending" → Yellow #FFEB9C

**Days to Approve Column (O):**

- If ≤3 → Green #C6EFCE
- If 4-7 → Yellow #FFEB9C
- If >7 → Red #FFC7CE

**Status Column (S):**

- If "Active" → Green #C6EFCE
- If "Expired" or "Revoked" → Light gray #D9D9D9

**Recertification Date Column (R):**

- If ≤30 days → Yellow #FFEB9C (due soon)
- If <TODAY → Red #FFC7CE (overdue)
- Else → Green #C6EFCE

---

## Sheet 5: Usage_Monitoring

### Purpose
Verify privileged utility usage is logged, monitored, and reviewed.

### Header (Rows 1-2)
```
Row 1: "USAGE MONITORING ASSESSMENT"
Row 2: "Logging, SIEM integration, and usage review for privileged utilities"
```

### Column Structure (Row 3 - headers, Rows 4-203 - data, 200 rows)

| Col | Header | Type | Width | Validation |
|-----|--------|------|-------|------------|
| A | Utility Name | Text | 30 | From Sheet 2 |
| B | Logging Configured | Dropdown | 12 | Yes / No / Partial |
| C | Logging Mechanism | Text | 30 | Event Log / auditd / PAM / EDR |
| D | Events Logged | Text | 40 | What's logged (user, time, endpoint, etc.) |
| E | SIEM Integration | Dropdown | 12 | Yes / No / In Progress |
| F | SIEM Verified | Dropdown | 12 | Yes / No / Not Tested |
| G | SIEM Test Date | Date | 12 | When verified |
| H | Log Retention (Days) | Number | 10 | How long stored |
| I | Alerting Configured | Dropdown | 12 | Yes / No |
| J | Alert Triggers | Text | 40 | What triggers alert |
| K | Usage Period (Days) | Number | 10 | Sample period (e.g., 30) |
| L | Total Executions | Number | 12 | Count in period |
| M | Unique Users | Number | 10 | How many users |
| N | Unique Endpoints | Number | 10 | How many endpoints |
| O | Anomalies Detected | Number | 10 | Count of anomalies |
| P | Review Frequency | Dropdown | 15 | Real-time / Daily / Weekly / Monthly |
| Q | Last Review Date | Date | 12 | When last reviewed |
| R | Review Findings | Text | 40 | Summary of findings |
| S | Monitoring Status | Formula | 12 | =IF(AND(B4="Yes",E4="Yes",F4="Yes"),"✅ Complete","⚠️ Partial") |
| T | Notes | Text | 40 | Additional |

### Usage Monitoring Metrics (Rows 205-225)
```
Total Utilities Assessed:    [=COUNT(A4:A203 where not blank)]

Logging Status:
  Logging Configured:        [=COUNTIF(B4:B203,"Yes")]
  Partial Logging:           [=COUNTIF(B4:B203,"Partial")]
  No Logging:                [=COUNTIF(B4:B203,"No")]
  Logging %:                 [=Logging Configured/Total*100]

SIEM Integration:
  SIEM Integrated:           [=COUNTIF(E4:E203,"Yes")]
  SIEM Verified:             [=COUNTIF(F4:F203,"Yes")]
  SIEM Integration %:        [=SIEM Integrated/Total*100]

Alerting:
  Alerting Configured:       [=COUNTIF(I4:I203,"Yes")]
  Alerting %:                [=Alerting/Total*100]

Log Retention:
  Average Retention (Days):  [=AVERAGE(H4:H203)]
  Min Retention:             [=MIN(H4:H203)]
  Below 90 Days:             [=COUNTIF(H4:H203,"<90")]

Review Process:
  Real-time Review:          [=COUNTIF(P4:P203,"Real-time")]
  Daily Review:              [=COUNTIF(P4:P203,"Daily")]
  Weekly Review:             [=COUNTIF(P4:P203,"Weekly")]
  Monthly Review:            [=COUNTIF(P4:P203,"Monthly")]

Recent Reviews:
  Reviewed ≤30 Days:         [=COUNTIF(Q4:Q203,">="&TODAY()-30)]
  Review Compliance %:       [=Reviewed/Total*100]

Overall Monitoring:
  Complete:                  [=COUNTIF(S4:S203,"✅ Complete")]
  Partial:                   [=COUNTIF(S4:S203,"⚠️ Partial")]
  Monitoring %:              [=Complete/Total*100]

Targets:
  Logging: 100%
  SIEM: ≥95%
  Alerting: ≥90% (high-risk utilities)
  Retention: ≥90 days
  Review: 100% compliance
```

### Conditional Formatting

**Logging Configured Column (B):**

- If "Yes" → Green #C6EFCE
- If "Partial" → Yellow #FFEB9C
- If "No" → Red #FFC7CE

**SIEM Integration Column (E):**

- If "Yes" → Green #C6EFCE
- If "In Progress" → Yellow #FFEB9C
- If "No" → Red #FFC7CE

**SIEM Verified Column (F):**

- If "Yes" → Green #C6EFCE
- If "No" or "Not Tested" → Red #FFC7CE

**Monitoring Status Column (S):**

- If "✅ Complete" → Green #C6EFCE
- If "⚠️ Partial" → Yellow #FFEB9C

**Log Retention Column (H):**

- If ≥90 → Green #C6EFCE
- If 30-89 → Yellow #FFEB9C
- If <30 → Red #FFC7CE

---

## Sheet 6: Security_Bypass_Tools

### Purpose
Specifically identify and assess security bypass tools - CRITICAL RISK.

### Header (Rows 1-2)
```
Row 1: "SECURITY BYPASS TOOLS"
Row 2: "Tools that can disable security controls or bypass protections"
```

### Column Structure (Row 3 - headers, Rows 4-53 - data, 50 rows)

| Col | Header | Type | Width | Validation |
|-----|--------|------|-------|------------|
| A | Tool ID | Auto | 10 | BYPASS-001... |
| B | Tool Name | Text | 30 | Tool name (yellow #FFEB9C) |
| C | Bypass Type | Dropdown | 20 | AV Disabler / Log Editor / Cred Dump / Rootkit / Kernel Manipulation |
| D | Found on Endpoints | Dropdown | 12 | Yes / No |
| E | Endpoint Count | Number | 10 | If yes, how many |
| F | Authorized Use | Dropdown | 12 | Security Team Only / Prohibited / Conditional |
| G | Use Case | Text | 40 | If authorized, why |
| H | Access Control | Dropdown | 15 | PAM / Blocklisted / No Control |
| I | Detection Configured | Dropdown | 12 | Yes / No |
| J | Detection Mechanism | Text | 30 | EDR alert, SIEM rule |
| K | Session Recording | Dropdown | 12 | Yes / No / N/A |
| L | Authorized Endpoints | Text | 30 | Where allowed (e.g., security lab) |
| M | Risk Level | Dropdown | 10 | Critical / High |
| N | Compensating Controls | Text | 40 | Mitigations |
| O | Control Status | Formula | 12 | =IF(F4="Prohibited",IF(H4="Blocklisted","✅ Blocked","🔴 Critical"),IF(H4="PAM","✅ Controlled","⚠️ Partial")) |
| P | Notes | Text | 40 | Additional |

### Security Bypass Tool Metrics (Rows 55-70)
```
Total Bypass Tools Identified: [=COUNT(A4:A53 where not blank)]

By Bypass Type:
  AV Disabler:               [=COUNTIF(C4:C53,"AV Disabler")]
  Log Editor:                [=COUNTIF(C4:C53,"Log Editor")]
  Cred Dump:                 [=COUNTIF(C4:C53,"Cred Dump")]
  Rootkit:                   [=COUNTIF(C4:C53,"Rootkit")]
  Kernel Manipulation:       [=COUNTIF(C4:C53,"Kernel Manipulation")]

Presence:
  Found on Endpoints:        [=COUNTIF(D4:D53,"Yes")]
  Total Affected Endpoints:  [=SUM(E4:E53)]

Authorization:
  Security Team Only:        [=COUNTIF(F4:F53,"Security Team Only")]
  Prohibited:                [=COUNTIF(F4:F53,"Prohibited")]
  Conditional:               [=COUNTIF(F4:F53,"Conditional")]

Controls:
  PAM Controlled:            [=COUNTIF(H4:H53,"PAM")]
  Blocklisted:               [=COUNTIF(H4:H53,"Blocklisted")]
  No Control:                [=COUNTIF(H4:H53,"No Control")]

Detection:
  Detection Configured:      [=COUNTIF(I4:I53,"Yes")]
  No Detection:              [=COUNTIF(I4:I53,"No")]

Session Recording:
  Recording Enabled:         [=COUNTIF(K4:K53,"Yes")]

Control Status:
  Blocked:                   [=COUNTIF(O4:O53,"✅ Blocked")]
  Controlled:                [=COUNTIF(O4:O53,"✅ Controlled")]
  Partial:                   [=COUNTIF(O4:O53,"⚠️ Partial")]
  Critical (Uncontrolled):   [=COUNTIF(O4:O53,"🔴 Critical")]

TARGET: 0 uncontrolled security bypass tools
```

### Conditional Formatting

**Found on Endpoints Column (D):**

- If "Yes" → Yellow #FFEB9C (requires investigation)
- If "No" → Green #C6EFCE

**Access Control Column (H):**

- If "PAM" or "Blocklisted" → Green #C6EFCE
- If "No Control" → Red #FFC7CE

**Detection Configured Column (I):**

- If "Yes" → Green #C6EFCE
- If "No" → Red #FFC7CE

**Control Status Column (O):**

- If "✅ Blocked" or "✅ Controlled" → Green #C6EFCE
- If "⚠️ Partial" → Yellow #FFEB9C
- If "🔴 Critical" → Dark red #C00000, white text

---

## Sheet 7: Privileged_Utility_Gaps

### Purpose
Consolidated gap register.

### Header (Rows 1-2)
```
Row 1: "PRIVILEGED UTILITY GAPS & REMEDIATION"
Row 2: "Consolidated gap register with risk-based prioritization"
```

### Column Structure

Same as S3/S4 Sheet 7 (100 rows)

Gap Categories: No Access Control / Not Enforced / Over-Privileged / No Approval / No Monitoring / No Recertification / Security Bypass Uncontrolled

---

## Sheet 8: Evidence_Register

### Purpose
Evidence repository.

### Header (Rows 1-2)
```
Row 1: "EVIDENCE REGISTER"
Row 2: "Document all evidence supporting this assessment"
```

### Column Structure

Same as S3/S4 Sheet 8 (100 rows)

---

## Sheet 9: Privileged_Utility_Dashboard

### Purpose
Executive summary dashboard.

### Header (Rows 1-3)
```
Row 1: "PRIVILEGED UTILITY COMPLIANCE DASHBOARD"
Row 2: "ISO/IEC 27001:2022 Control A.8.18 - Use of Privileged Utility Programs"
Row 3: "Executive Summary - [=Instructions!B8]"
```

### Dashboard Layout

**Section 1: Overall Status (Rows 5-18)**

```
┌─────────────────────────────────────────┐
│  PRIVILEGED UTILITY CONTROL STATUS      │
├─────────────────────────────────────────┤
│  Total Utilities:         [XXX]         │
│  High/Critical Risk:      [XX]          │
│                                          │
│  Access Control:                        │
│    Deployment:            [XX.X%]       │
│    Enforcement:           [XX.X%]       │
│                                          │
│  Monitoring:                            │
│    Logging:               [XX.X%]       │
│    SIEM Integration:      [XX.X%]       │
│                                          │
│  Approval Workflow:       [XX.X%]       │
│  Recertification:         [XX.X%]       │
│                                          │
│  Security Bypass Tools:   [X] Uncontrolled  │
│                                          │
│  Overall Status:          [🟢 GREEN / 🟡 YELLOW / 🔴 RED]  │
└─────────────────────────────────────────┘
```

**Formulas:**

- From Sheet 2: Total utilities, risk counts
- From Sheet 3: Access control %
- From Sheet 5: Logging %, SIEM %
- From Sheet 4: Approval workflow %
- From Sheet 6: Security bypass tool status

**Overall Status Logic:**
```
=IF(AND(AccessControl>=95%,Enforcement>=95%,Logging>=95%,SIEM>=95%,BypassTools=0),"🟢 GREEN",
   IF(AND(AccessControl>=85%,Enforcement>=85%,Logging>=85%,BypassTools<=2),"🟡 YELLOW",
   "🔴 RED"))
```

**Section 2: Utility Breakdown (Rows 20-30)**

By category, by risk level

**Section 3: Access Control Summary (Rows 32-42)**

Deployment, enforcement, testing results

**Section 4: Usage Monitoring Summary (Rows 44-54)**

Logging, SIEM, alerting, review compliance

**Section 5: Security Bypass Tools (Rows 56-66)**

Count, control status, critical gaps

**Section 6: Critical Gaps (Rows 68-82)**

Top 10 from Sheet 7

**Section 7: Executive Summary (Rows 84-92)**

Narrative

**Section 8: Recommended Actions (Rows 94-112)**

Immediate, short-term, long-term

### Conditional Formatting

Same as S3/S4 Dashboard sheets

---

## Cell Styling Reference

Same as S3/S4

---

## Appendix: Python Developer Notes

### Generating This Workbook

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule

# Initialize
wb = Workbook()

# Standard styles (same as S3/S4)
# ... (styles defined)

# Create sheets
ws1 = wb.active
ws1.title = "Instructions"
ws2 = wb.create_sheet("Utility_Inventory")
ws3 = wb.create_sheet("Access_Control")
ws4 = wb.create_sheet("Approval_Workflow")
ws5 = wb.create_sheet("Usage_Monitoring")
ws6 = wb.create_sheet("Security_Bypass_Tools")
ws7 = wb.create_sheet("Privileged_Utility_Gaps")
ws8 = wb.create_sheet("Evidence_Register")
ws9 = wb.create_sheet("Privileged_Utility_Dashboard")

# Data Validations
dv_category = DataValidation(type="list",
    formula1='"System Admin,Remote Access,Debug/Dev,Password/Cred,Network Analysis,Security Bypass"')
ws2.add_data_validation(dv_category)
for row in range(4, 204):
    dv_category.add(ws2[f"C{row}"])

dv_control = DataValidation(type="list",
    formula1='"AppLocker,WDAC,PAM,sudo,SELinux,MDM,GPO,None"')
ws3.add_data_validation(dv_control)
for row in range(4, 204):
    dv_control.add(ws3[f"B{row}"])

# Conditional Formatting
ws3.conditional_formatting.add(
    "N4:N203",
    CellIsRule(operator="equal", formula=['"✅ Controlled"'], fill=green_fill)
)
ws3.conditional_formatting.add(
    "N4:N203",
    CellIsRule(operator="equal", formula=['"❌ Uncontrolled"'], fill=red_fill)
)

# Formulas
ws3["N4"] = '=IF(AND(C4="🟢 Deployed",D4="Enforce"),"✅ Controlled",IF(D4="Audit","⚠️ Audit","❌ Uncontrolled"))'
ws4["O4"] = '=INT(N4-B4)'
ws5["S4"] = '=IF(AND(B4="Yes",E4="Yes",F4="Yes"),"✅ Complete","⚠️ Partial")'
ws6["O4"] = '=IF(F4="Prohibited",IF(H4="Blocklisted","✅ Blocked","🔴 Critical"),IF(H4="PAM","✅ Controlled","⚠️ Partial"))'

# Save
wb.save("Privileged_Utilities_Assessment.xlsx")
```

### Identifying Privileged Utilities

```python
import subprocess
import platform

def identify_privileged_utilities_windows():
    """Identify common privileged utilities on Windows"""
    utilities = {
        'System Admin': [
            'regedit.exe', 'services.msc', 'gpedit.msc', 
            'compmgmt.msc', 'eventvwr.msc'
        ],
        'Remote Access': [
            'mstsc.exe', 'teamviewer.exe'
        ],
        'Debug/Dev': [
            'windbg.exe', 'procexp.exe', 'procmon.exe'
        ],
        'Network Analysis': [
            'wireshark.exe', 'nmap.exe'
        ],
        'Security Bypass': [
            'mimikatz.exe', 'pwdump.exe'  # Should be prohibited
        ]
    }
    
    found = {}
    for category, tools in utilities.items():
        found[category] = []
        for tool in tools:
            # Check if exists (simplified - actual would query all endpoints)
            path = f"C:\\Windows\\System32\\{tool}"
            if os.path.exists(path):
                found[category].append(tool)
    
    return found

def check_access_control_windows(utility_path):
    """Check if access control is configured for utility"""
    # Check AppLocker policy (simplified)
    # In reality, query GPO and local AppLocker rules
    
    result = subprocess.run(
        ['powershell', '-Command', 
         f'Get-AppLockerPolicy -Effective | Select-Object -ExpandProperty RuleCollections'],
        capture_output=True, text=True
    )
    
    # Parse result to see if utility_path is in allowlist
    # Return access control status
    pass
```

---

**END OF SPECIFICATION**

---

*"It is perfectly obvious that the whole world is going to hell. The only possible chance that it might not is that we do not attempt to prevent it from doing so."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->
