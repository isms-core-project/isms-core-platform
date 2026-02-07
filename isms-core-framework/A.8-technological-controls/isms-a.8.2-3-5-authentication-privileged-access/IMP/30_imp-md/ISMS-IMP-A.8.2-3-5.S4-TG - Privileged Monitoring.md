**ISMS-IMP-A.8.2-3-5.S4-TG - Privileged Monitoring Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.2-3-5.S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Privileged Access Monitoring & Activity Analysis |
| **Related Policy** | ISMS-POL-A.8.2-3-5 (Section 2.2.6 - Privileged Access Monitoring) |
| **Purpose** | Monitor and analyze privileged access activity to detect unauthorized use, anomalous behavior, and tier isolation violations; verify session recording coverage and privileged access review completion |
| **Target Audience** | Security Team, SOC Team, IT Operations, CISO |
| **Assessment Type** | Activity Monitoring & Behavioral Analysis |
| **Review Cycle** | Quarterly comprehensive assessment, Continuous monitoring via SIEM |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial assessment specification for privileged access monitoring | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.2-3-5.S4-UG.

---

# Technical Specification

# Excel Workbook Structure

## Workbook Overview

**Filename:** `ISMS-IMP-A.8.2-3-5.4_Privileged_Monitoring_YYYYMMDD.xlsx`

**Sheet Structure:**

| Sheet # | Sheet Name | Purpose | Rows | Completion Method |
|---------|-----------|---------|------|-------------------|
| 1 | Instructions & Legend | User guide and monitoring reference | ~60 | Pre-populated |
| 2 | Privileged Access Activity | Individual privileged access events | 1003 | User completes (log import) |
| 3 | Privileged Commands | Privileged command execution log | 503 | User completes (log import) |
| 4 | Tier Isolation Compliance | Tier violation summary and details | ~50 | Auto-calculated + manual |
| 5 | Session Recording Coverage | Session recording verification | 503 | User completes |
| 6 | Access Review Status | Quarterly access review tracking | 203 | User completes |
| 7 | Monitoring Summary | Overall metrics dashboard | ~30 | Auto-calculated |
| 8 | Evidence Register | Evidence tracking | 53 | User completes |
| 9 | Approval & Sign-Off | Three-level approval | ~25 | User completes |

**Total Workbook:** 9 sheets, ~2,400 rows of structured data collection

## Color Coding & Conditional Formatting

**Anomaly Status Colors:**

- 🔴 **Red (Anomaly - Investigate)**: RGB(255, 199, 206) - Unusual activity requiring investigation
- 🟡 **Yellow (Review Recommended)**: RGB(255, 235, 156) - Potentially unusual, review recommended
- 🟢 **Green (Normal)**: RGB(198, 239, 206) - Expected activity
- ⚫ **Gray (N/A)**: RGB(217, 217, 217) - Not applicable

**Tier Violation Colors:**

- 🔴 **Red (VIOLATION)**: RGB(255, 0, 0) - Tier isolation violation (CRITICAL)
- 🟢 **Green (Compliant)**: RGB(198, 239, 206) - Tier isolation maintained

**Review Status Colors:**

- 🔴 **Red (Overdue)**: RGB(255, 199, 206) - Access review overdue
- 🟡 **Yellow (Due Soon)**: RGB(255, 235, 156) - Review due within 30 days
- 🟢 **Green (Up to Date)**: RGB(198, 239, 206) - Review completed on time

---

# Sheet 2: Privileged Access Activity (Primary Data Collection)

## Purpose

Log of all privileged access events during assessment period.

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Event ID | 15 | Text | Free text | Unique log entry identifier |
| B | Timestamp | 18 | DateTime | DD.MM.YYYY HH:MM | Date and time of access |
| C | Privileged Account | 20 | Text | Free text | Admin account used |
| D | Account Owner | 20 | Text | Free text | Person who owns account |
| E | Source IP/System | 18 | Text | Free text | Where access originated |
| F | Destination System | 22 | Text | Free text | System accessed |
| G | Destination Tier | 12 | Dropdown | Tier 0, Tier 1, Tier 2, Unknown | Tier of destination system |
| H | Access Method | 15 | Dropdown | Interactive Login, SSH, RDP, Console, API, Other | How accessed |
| I | Business Hours | 12 | Formula | Auto: Yes, No | Within 08:00-18:00 weekdays? |
| J | Expected Activity | 15 | Dropdown | Yes, No, Unknown | Expected based on user role? |
| K | Activity Type | 18 | Dropdown | Routine Maintenance, Change, Incident Response, Unknown | Activity category |
| L | Account Tier | 12 | Dropdown | Tier 0, Tier 1, Tier 2 | Tier of privileged account |
| M | Tier Compliant | 15 | Formula | Auto: Yes, No, N/A | Tier isolation maintained? |
| N | Anomaly Detected | 15 | Dropdown | Yes, No | Unusual activity? |
| O | Investigation Status | 18 | Dropdown | Not Required, Pending, In Progress, Completed, Closed | Investigation state |

**Total Columns:** 15 (A-O)

## Business Hours Calculation (Column I)

**Formula Logic:**
```excel
=IF(AND(WEEKDAY(B5,2)<=5, HOUR(B5)>=8, HOUR(B5)<18), "Yes", "No")
```

- Weekdays (Monday-Friday) AND 08:00-17:59 = Business Hours

## Tier Compliance Calculation (Column M)

**Formula Logic:**
```excel
=IF(L5="Tier 0",
    IF(G5="Tier 0", "Yes", "No - VIOLATION"),
    IF(L5="Tier 1",
        IF(OR(G5="Tier 0", G5="Tier 1"), "Yes",
            IF(G5="Tier 2", "No - VIOLATION", "N/A")),
        "N/A"))
```

**Tier Isolation Rules:**

- Tier 0 account → Tier 0 system = Compliant
- Tier 0 account → Tier 1/2 system = **VIOLATION**
- Tier 1 account → Tier 0/1 system = Compliant (Tier 1 cannot access Tier 0 anyway)
- Tier 1 account → Tier 2 system = **VIOLATION**

**Conditional Formatting:**

- "No - VIOLATION" → Red background, bold text
- "Yes" → Green background

---

# Sheet 3: Privileged Commands

## Purpose

Track privileged command execution (sudo, runas, admin PowerShell).

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Timestamp | 18 | DateTime | DD.MM.YYYY HH:MM | When command executed |
| B | Privileged Account | 20 | Text | Free text | Admin account |
| C | System | 20 | Text | Free text | System where command executed |
| D | Command Executed | 40 | Text | Free text | Full command (e.g., "sudo systemctl restart apache2") |
| E | Command Category | 20 | Dropdown | Service Management, User Management, System Configuration, File Operations, Network Configuration, Security, Other | Command type |
| F | High-Risk Command | 12 | Dropdown | Yes, No | Requires review? |
| G | Review Required | 15 | Dropdown | Yes, No | Should this be reviewed? |
| H | Review Notes | 30 | Text | Free text | Reviewer comments |

**Total Columns:** 8 (A-H)

## High-Risk Commands

**High-Risk = Yes:**

- User add/delete/modify commands (useradd, userdel, net user)
- Privilege escalation (chmod +s, visudo, net localgroup administrators)
- Firewall changes (iptables, ufw, netsh advfirewall)
- Service disable (systemctl disable, sc config start=disabled)
- Security tool disable (setenforce 0, AppArmor=shutdown)

---

# Sheet 4: Tier Isolation Compliance

## Purpose

Summary of tier isolation violations with remediation tracking.

## Metrics Section

```
Tier 0 Access Events:

- Total: [count from Sheet 2 where Account Tier = Tier 0]
- To Tier 0 (Compliant): [count]
- To Tier 1 (VIOLATION): [count]
- To Tier 2 (VIOLATION): [count]

Tier 1 Access Events:

- Total: [count from Sheet 2 where Account Tier = Tier 1]
- To Tier 1 (Compliant): [count]
- To Tier 2 (VIOLATION): [count]

Overall Tier Isolation Compliance: [%]
```

## Violation Detail Table

| Col | Header | Width | Type | Description |
|-----|--------|-------|------|-------------|
| A | Event ID | 15 | Text | Reference to Sheet 2 |
| B | Timestamp | 18 | DateTime | When violation occurred |
| C | Privileged Account | 20 | Text | Which account |
| D | Violation Type | 15 | Text | Tier 0→1, Tier 0→2, Tier 1→2 |
| E | Destination System | 22 | Text | System accessed |
| F | Investigation Status | 18 | Dropdown | Pending, In Progress, Completed |
| G | Investigation Outcome | 30 | Text | Legitimate exception, User error, Security incident, etc. |
| H | Remediation Action | 30 | Text | GPO enforcement, User retraining, Account disabled, etc. |

---

# Sheet 5: Session Recording Coverage

## Purpose

Verify session recording implementation and playback capability.

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | Session ID | 15 | Text | Free text | Unique session identifier |
| B | Timestamp | 18 | DateTime | DD.MM.YYYY HH:MM | Session start time |
| C | Privileged Account | 20 | Text | Free text | Admin account used |
| D | System Accessed | 22 | Text | Free text | Destination system |
| E | Session Duration (min) | 15 | Number | ≥0 | Minutes |
| F | Session Recorded | 12 | Dropdown | Yes, No | Was session recorded? |
| G | Recording Type | 15 | Dropdown | Video, Keystroke Log, Both, None | Type of recording |
| H | Playback Verified | 15 | Dropdown | Yes, No, N/A | Did we test playback? |
| I | Recording Location | 30 | Text | Free text | PAM path or file location |
| J | Recording Required | 15 | Formula | Auto: Yes, No | Per policy (Tier 0 mandatory) |
| K | Recording Gap | 12 | Formula | Auto: Yes, No | Required but not recorded? |

**Total Columns:** 11 (A-K)

## Recording Required Calculation (Column J)

**Formula Logic:**
```excel
=IF(VLOOKUP(C5, 'Privileged Account Inventory'!A:I, 9, FALSE)="Tier 0", 
    "Yes", "No")
```

- Look up account in IMP.3, check tier
- Tier 0 = Recording MANDATORY
- Tier 1 = Recording RECOMMENDED (policy may require)
- Tier 2 = Optional

## Recording Gap Calculation (Column K)

**Formula Logic:**
```excel
=IF(AND(J5="Yes", F5="No"), "Yes - GAP", "No")
```

**Conditional Formatting:**

- "Yes - GAP" → Red background

---

# Sheet 6: Access Review Status

## Purpose

Track quarterly privileged access review completion.

## Column Structure

| Col | Header | Width | Type | Validation | Description |
|-----|--------|-------|------|------------|-------------|
| A | User Name | 20 | Text | Free text | Privileged user |
| B | Privileged Accounts | 15 | Number | ≥1 | Number of admin accounts owned |
| C | Highest Tier | 12 | Text | Tier 0, Tier 1, Tier 2 | Highest privilege level |
| D | Manager | 20 | Text | Free text | User's manager |
| E | Last Review Date | 15 | Date | DD.MM.YYYY | Date of last completed review |
| F | Review Due Date | 15 | Formula | Auto: Last + 90 days | Quarterly review deadline |
| G | Review Status | 15 | Formula | Auto: Completed, Overdue, Due Soon | Status |
| H | Review Outcome | 18 | Dropdown | Access Confirmed, Access Removed, Access Modified, Pending | Result |
| I | Reviewer | 18 | Text | Free text | Who conducted review |
| J | Review Overdue (Days) | 15 | Formula | Auto: Days overdue if overdue | How many days past due |
| K | Compliance | 12 | Formula | Auto: Compliant, Overdue | Compliance status |

**Total Columns:** 11 (A-K)

## Review Due Date Calculation (Column F)

**Formula Logic:**
```excel
=E5+90
```

- Quarterly review = every 90 days

## Review Status Calculation (Column G)

**Formula Logic:**
```excel
=IF(TODAY()>F5, "Overdue",
    IF(TODAY()>F5-30, "Due Soon",
        "Completed"))
```

## Review Overdue Days (Column J)

**Formula Logic:**
```excel
=IF(TODAY()>F5, TODAY()-F5, 0)
```

## Compliance Status (Column K)

**Formula Logic:**
```excel
=IF(G5="Overdue", "Overdue", "Compliant")
```

**Conditional Formatting:**

- Overdue → Red background
- Due Soon → Yellow background
- Completed → Green background

---

# Sheet 7: Monitoring Summary (Dashboard)

## Purpose

Executive summary of privileged access monitoring metrics.

## Metrics Calculated

**Privileged Access Activity:**
```excel
Total Privileged Access Events: 
  =COUNTA('Privileged Access Activity'!A5:A1003)

Off-Hours Access Events: 
  =COUNTIF('Privileged Access Activity'!I:I, "No")

Off-Hours Percentage: 
  =Off_Hours / Total_Events * 100
```

**Tier Isolation:**
```excel
Tier Isolation Violations: 
  =COUNTIF('Privileged Access Activity'!M:M, "No - VIOLATION")

Tier Isolation Compliance %: 
  =(Total_Events - Violations) / Total_Events * 100
```

**Session Recording:**
```excel
Total Sessions: 
  =COUNTA('Session Recording Coverage'!A5:A503)

Sessions Recorded: 
  =COUNTIF('Session Recording Coverage'!F:F, "Yes")

Recording Coverage %: 
  =Sessions_Recorded / Total_Sessions * 100

Recording Gaps (Tier 0): 
  =COUNTIF('Session Recording Coverage'!K:K, "Yes - GAP")
```

**Access Reviews:**
```excel
Total Privileged Users: 
  =COUNTA('Access Review Status'!A5:A203)

Reviews Completed: 
  =COUNTIF('Access Review Status'!G:G, "Completed")

Reviews Overdue: 
  =COUNTIF('Access Review Status'!G:G, "Overdue")

Review Completion %: 
  =Reviews_Completed / Total_Users * 100
```

---

# Sheet 8: Evidence Register

## Column Structure

| Col | Header | Width | Type | Description |
|-----|--------|-------|------|-------------|
| A | Evidence ID | 15 | Text | EV-A8235-4-001 |
| B | Evidence Type | 20 | Dropdown | SIEM Dashboard, Log Export, Session Recording, Review Record, Investigation Report |
| C | Description | 30 | Text | Brief description |
| D | File Location | 30 | Text | Path to evidence file |
| E | Collection Date | 15 | Date | When collected |
| F | Collected By | 18 | Text | Person who collected |

---

# Sheet 9: Approval & Sign-Off

## Three-Level Approval

**Level 1 - Preparer (SOC Team / Security Analyst):**

- Name, Title, Date, Signature

**Level 2 - Reviewer (Security Team Lead):**

- Name, Title, Date, Signature

**Level 3 - Approver (CISO):**

- Name, Title, Date, Signature

---

# Python Script Integration

## Script Purpose

Automated generation of privileged monitoring workbook with log import.

**Script:** `generate_a8235_4_privileged_monitoring.py`

## Script Features

- Imports privileged access logs from SIEM export (CSV, JSON)
- Creates all 9 sheets with proper structure
- Applies data validation rules (dropdowns)
- Implements conditional formatting (anomaly colors, tier violations)
- Adds formulas for tier compliance calculations
- Generates monitoring summary dashboard
- Sets column widths and freeze panes

## Running the Script

```bash
# With SIEM log import
python3 generate_a8235_4_privileged_monitoring.py \
  --siem-export privileged_logs.csv \
  --period 2025-Q4

# With custom output
python3 generate_a8235_4_privileged_monitoring.py \
  --siem-export logs.csv \
  --output /path/to/file.xlsx \
  --date 2026-01-22
```

## Input CSV Format

Expected columns in SIEM export:

- Timestamp (required: YYYY-MM-DD HH:MM:SS)
- User (required: privileged account name)
- SourceIP (optional)
- DestinationSystem (required)
- EventType (optional: login, command, privilege_escalation)
- Command (optional: for privileged command tracking)

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Document Assembly & Quality Checks

**Complete Document Structure:**
```
ISMS-IMP-A.8.2-3-5.4 - Privileged Monitoring Assessment v1.0

├── Document Control (Metadata, Version History)
│
├── PART I: USER COMPLETION GUIDE (~600 lines)
│   ├── 1. Assessment Overview
│   ├── 2. Prerequisites
│   ├── 3. Assessment Workflow
│   ├── 4. Evidence Collection
│   ├── 5. Common Pitfalls (10 pitfalls)
│   ├── 6. Quality Checklist
│   ├── 7. Interpreting Results
│   └── 8. Review & Approval
│
└── PART II: TECHNICAL SPECIFICATION (~400 lines)
    ├── 1. Workbook Structure
    ├── 2. Sheet 2: Privileged Access Activity
    ├── 3. Sheet 3: Privileged Commands
    ├── 4. Sheet 4: Tier Isolation Compliance
    ├── 5. Sheet 5: Session Recording Coverage
    ├── 6. Sheet 6: Access Review Status
    ├── 7. Sheet 7: Monitoring Summary
    ├── 8. Sheet 8: Evidence Register
    ├── 9. Sheet 9: Approval & Sign-Off
    └── 10. Python Script Integration
```

**Quality Checks Before Finalizing:**

- [ ] All sections complete and accurate
- [ ] Tier isolation monitoring prominently featured
- [ ] Session recording verification clearly documented
- [ ] Access review tracking integrated
- [ ] SIEM integration guidance provided
- [ ] Cross-references correct (IMP.3 for tier data)
- [ ] No placeholder text
- [ ] Technical specification matches Python script

---

**END OF ISMS-IMP-A.8.2-3-5.4**

*Privileged access monitoring is not optional. It's your early warning system.*

*Tier violations = CRITICAL alerts. Investigate every one.*

*Session recordings = your evidence. Test playback quarterly.*

---

**END OF SPECIFICATION**

---

*"We may hope that machines will eventually compete with men in all purely intellectual fields."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
