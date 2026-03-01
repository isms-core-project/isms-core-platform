<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.2-3-5.S4-UG:framework:UG:a.8.2-3-5 -->
**ISMS-IMP-A.8.2-3-5.S4-UG - Privileged Monitoring Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.2: Privileged Access Rights

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Privileged Monitoring |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.2-3-5.S4-UG |
| **Related Policy** | ISMS-POL-A.8.2-3-5 (Authentication Privileged Access) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.2 (Privileged Access Rights) |
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

- ISMS-POL-A.8.2-3-5 (Authentication Privileged Access)
- ISMS-IMP-A.8.2-3-5.S1 (Authentication Inventory)
- ISMS-IMP-A.8.2-3-5.S2 (MFA Coverage)
- ISMS-IMP-A.8.2-3-5.S3 (Privileged Accounts)
- ISMS-IMP-A.8.2-3-5.S5 (Access Restrictions)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.2-3-5.S4-TG.

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Session Recording Coverage | Track privileged session recording deployment |
| 3 | Privileged Command Logging | Document command logging for privileged activity |
| 4 | Anomaly Detection Rules | Define and assess anomaly detection rules for privileged access |
| 5 | Privileged Access Activity | Record privileged access activity for analysis |
| 6 | Alert Response Tracking | Track responses to privileged access alerts |
| 7 | Off Hours Access Log | Monitor and review out-of-hours privileged access |
| 8 | Failed Login Analysis | Analyse failed login attempts for privileged accounts |
| 9 | Tier Violation Incidents | Document and track tier isolation violation incidents |
| 10 | Evidence Register | Store and reference evidence supporting assessments |
| 11 | Summary Dashboard | Compliance status and key metrics overview |
| 12 | Approval Sign-Off | Management review sign-off and certification |

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.2-3-5.4 - Privileged Monitoring Assessment

**What This Assessment Does:**

- Monitors privileged access activity (privileged logins, commands executed, systems accessed)
- Detects anomalous privileged access behavior (off-hours access, unusual systems, failed attempts)
- Verifies tier isolation compliance (Tier 0 accounts accessing ONLY Tier 0 systems)
- Tracks session recording coverage and playback capability
- Measures privileged access review completion (quarterly reviews)
- Identifies suspicious privileged activity requiring investigation

**What This Assessment Does NOT Do:**

- Inventory privileged accounts (see IMP.3 - Privileged Account Inventory)
- Track MFA enrollment (see IMP.2 - MFA Coverage)
- Real-time incident response (SIEM/SOC handles real-time alerts)

**Primary ISO 27001 Control:** A.8.2 - Privileged Access Rights (Section 2.2.6 - Monitoring)

**Related Controls:**

- A.8.16 - Monitoring Activities (privileged access is high-priority monitoring)
- A.8.15 - Logging (privileged access events must be logged)
- A.5.24-27 - Incident Management (privileged access incidents)

**Why Privileged Monitoring Matters:**
Privileged accounts are high-value targets. Monitoring privileged activity enables early detection of:

- Credential compromise (unusual login times, locations, systems)
- Insider threats (privileged users accessing systems outside their role)
- Tier isolation violations (Tier 0 accounts accessing Tier 1/2 systems)
- Privilege escalation attempts (unauthorised privilege use)

## When to Use This Assessment

**Use this assessment when:**

- Conducting quarterly privileged access reviews (compliance requirement)
- Investigating privileged access security incidents
- Verifying tier isolation compliance
- Preparing for ISO 27001 certification audits
- Demonstrating privileged access monitoring to FINMA/DORA/NIS2 auditors
- Analyzing privileged access trends (usage patterns, anomalies)

**Assessment Frequency:**

- **Continuous**: Real-time monitoring via SIEM (alerts on suspicious activity)
- **Quarterly**: Comprehensive privileged access review, activity analysis, session recording verification
- **Annual**: Deep assessment, penetration testing, full compliance validation

## Who Completes This Assessment

**Primary Responsibility:** Security Team (SOC team lead, privileged access security analyst)

**Supporting Roles:**

- **SOC Team**: Real-time privileged access monitoring, alert investigation
- **IT Operations**: Provide privileged access logs from systems
- **System Owners**: Review privileged access to owned systems
- **SIEM Team**: Configure privileged access alerts, provide log analysis
- **Managers**: Conduct privileged access reviews for direct reports

**Approval Authority:** Chief Information Security Officer (CISO)

## Expected Time Investment

**Initial Setup** (first time):

- SIEM integration for privileged access logs: 4-8 hours
- Define privileged access monitoring rules: 2-4 hours
- Configure session recording: 2-4 hours (if not already configured)
- Initial workbook completion: 2-3 hours
- **Total**: 10-19 hours

**Quarterly Assessment**:

- Extract privileged access logs (3 months): 1-2 hours
- Analyze activity and identify anomalies: 2-3 hours
- Verify session recording coverage: 1-2 hours
- Conduct privileged access reviews: 3-4 hours (depends on number of privileged users)
- Workbook completion: 1-2 hours
- Evidence collection: 1-2 hours
- **Total**: 9-15 hours per quarter

**Continuous Monitoring** (ongoing):

- SOC team monitors privileged access alerts 24/7
- Investigate alerts as they occur (minutes to hours per alert)

---

# Prerequisites

## Required Information

Before starting the assessment, gather the following information:

**Privileged Access Logs:**

- [ ] Privileged login events (successful and failed)
- [ ] Privileged command execution logs (sudo, runas, PowerShell with admin rights)
- [ ] Privileged group membership changes (additions/removals from admin groups)
- [ ] Privileged access to sensitive systems (domain controllers, databases, security tools)
- [ ] Session recording logs (recorded sessions, playback capability)

**Reference Data:**

- [ ] Privileged account inventory (from IMP.3)
- [ ] Admin tier classifications (Tier 0, Tier 1, Tier 2)
- [ ] Expected privileged access patterns (business hours, authorised systems)
- [ ] Privileged user roles and responsibilities

**Session Recording:**

- [ ] Session recording platform details (CyberArk, BeyondTrust, native recording)
- [ ] Recorded sessions catalog (which accounts, which systems)
- [ ] Session playback capability verification

**Access Reviews:**

- [ ] Privileged access review schedule (quarterly)
- [ ] Previous review results
- [ ] Review completion status per privileged user

## Required Access

**System Access Needed:**

- [ ] SIEM read access (privileged access logs, alerts, dashboards)
- [ ] Session recording platform access (view recorded sessions, playback)
- [ ] Active Directory audit logs (privileged group changes, admin logins)
- [ ] Entra ID sign-in logs (privileged role activations, admin logins)
- [ ] Linux sudo logs (/var/log/auth.log, /var/log/secure)
- [ ] Windows Security Event Logs (Event IDs 4672, 4624, 4625 for privileged access)
- [ ] PAM solution logs (CyberArk, BeyondTrust activity logs)

**People Access Needed:**

- [ ] SOC team (alert investigation details)
- [ ] Privileged users (interview for access review)
- [ ] Managers (privileged access review approvals)

## Required Tools

**Software:**

- [ ] Microsoft Excel 2016 or later
- [ ] Python 3.8+ (if using automated workbook generation)
- [ ] SIEM access (Splunk, Microsoft Sentinel, Datadog, etc.)
- [ ] Session recording platform access
- [ ] Log analysis tools (PowerShell, Python scripts, grep/awk for Linux logs)

**Optional Tools:**

- [ ] SIEM API access (automated log extraction)
- [ ] PAM API access (session recording metadata)
- [ ] User Behavior Analytics (UBA) platform

---

# Assessment Workflow

## Assessment Process Overview

```
1. PREPARE
   → Define assessment period (typically last quarter)
   → Extract privileged access logs from SIEM
   → Gather session recording metadata
   → Generate workbook (Python script or Excel template)

2. ANALYZE PRIVILEGED ACTIVITY
   → Sheet 1: Privileged Access Activity Log

      - Document privileged logins per account
      - Identify systems accessed
      - Flag off-hours access

   → Sheet 2: Privileged Command Execution

      - Track privileged commands (sudo, runas, admin PowerShell)
      - Identify unusual commands

   → Sheet 3: Tier Isolation Compliance

      - Verify Tier 0 accounts ONLY access Tier 0 systems
      - Flag tier isolation violations (CRITICAL)

3. VERIFY SESSION RECORDING
   → Sheet 4: Session Recording Coverage

      - Which privileged sessions were recorded?
      - Verify playback capability
      - Identify gaps (sessions NOT recorded)

4. CONDUCT ACCESS REVIEWS
   → Sheet 5: Privileged Access Review Status

      - Track quarterly review completion per privileged user
      - Document review outcomes (access confirmed, access removed)

5. IDENTIFY ANOMALIES
   → Off-hours privileged access
   → Unusual systems accessed
   → Failed privileged login attempts (potential attacks)
   → Tier isolation violations

6. COLLECT EVIDENCE
   → SIEM screenshots (privileged access dashboards)
   → Session recording examples
   → Access review completion records

7. REVIEW & APPROVE
   → SOC review (monitoring effectiveness)
   → Security Team review (anomaly investigation)
   → CISO approval (quarterly sign-off)

8. REMEDIATE ISSUES
   → Investigate suspicious activity
   → Enforce tier isolation
   → Address session recording gaps
   → Complete overdue access reviews
```

## Step-by-Step Completion Guide

**Step 1: Extract Privileged Access Logs**

**From SIEM (Splunk example):**
```splunk
index=windows EventCode IN (4672, 4624, 4625) 
| where PrivilegeList="*SeDebugPrivilege*" OR PrivilegeList="*SeBackupPrivilege*"
| stats count by user, src_ip, dest, EventCode, _time
| sort - _time
```

**From Entra ID (Microsoft Graph PowerShell):**
```powershell
# Connect to Microsoft Graph with required scopes
Connect-MgGraph -Scopes "AuditLog.Read.All"

# Get sign-in logs for privileged role activations
Get-MgAuditLogSignIn -Filter "createdDateTime ge 2025-10-01" |
  Where-Object {$_.ConditionalAccessStatus -ne 'notApplied'} |
  Select-Object UserPrincipalName, CreatedDateTime, IpAddress, ResourceDisplayName
```

**From Linux sudo logs:**
```bash
# Extract sudo commands from last quarter
grep "COMMAND" /var/log/auth.log | 
  awk '{print $1, $2, $3, $6, $9, $10, $11, $12}' |
  grep -E "2025-10|2025-11|2025-12"
```

**Step 2: Generate Workbook**

Option A - Automated (Recommended):
```bash
python3 generate_a8235_4_privileged_monitoring.py \
  --siem-export privileged_access_logs.csv \
  --period 2025-Q4
```
This creates: `ISMS-IMP-A.8.2-3-5.4_Privileged_Monitoring_YYYYMMDD.xlsx`

Option B - Manual:

- Use Excel template
- Import log data manually
- Save as: `ISMS-IMP-A.8.2-3-5.4_Privileged_Monitoring_[DATE].xlsx`

**Step 3: Complete Sheet 1 - Privileged Access Activity Log**

For each privileged access event:

1. **Event Identification** (Columns A-D):

   - Event ID: Unique identifier (log entry ID)
   - Timestamp: Date and time of privileged access
   - Privileged Account: Which admin account was used
   - Account Owner: Person who owns the account

2. **Access Details** (Columns E-H):

   - Source IP/System: Where access originated
   - Destination System: System accessed
   - Destination Tier: Tier 0, Tier 1, Tier 2 (from IMP.3)
   - Access Method: Interactive login, SSH, RDP, console, API

3. **Activity Classification** (Columns I-K):

   - Business Hours: Yes, No (normal business hours 08:00-18:00 weekdays)
   - Expected Activity: Yes, No (is this expected based on user role?)
   - Activity Type: Routine Maintenance, Change Implementation, Incident Response, Unknown

4. **Tier Compliance** (Columns L-M):

   - Account Tier: Tier 0, Tier 1, Tier 2 (from IMP.3)
   - Tier Isolation Compliant: Yes, No, N/A
     - If Account Tier = Tier 0 AND Destination Tier ≠ Tier 0 → **No (VIOLATION)**
     - If Account Tier = Tier 1 AND Destination Tier = Tier 2 → **No (VIOLATION)**

5. **Alert Status** (Columns N-O):

   - Anomaly Detected: Yes, No (off-hours, unusual system, failed attempts)
   - Investigation Status: Not Required, Pending, In Progress, Completed, Closed

**Step 4: Complete Sheet 2 - Privileged Command Execution**

For privileged commands (sudo, runas, admin PowerShell):

1. **Command Details** (Columns A-F):

   - Timestamp
   - Privileged Account
   - System
   - Command Executed (e.g., "sudo systemctl restart apache2")
   - Command Category: Service Management, User Management, System Configuration, File Operations, Network Configuration, Security, Other

2. **Risk Assessment** (Columns G-H):

   - High-Risk Command: Yes, No
     - High-risk: user add/delete, privilege escalation, firewall changes, service disable
   - Review Required: Yes, No

**Step 5: Complete Sheet 3 - Tier Isolation Compliance**

Summary of tier isolation violations:

**Tier 0 Violations:**

- Total Tier 0 access events: [count]
- Tier 0 to Tier 0 (compliant): [count]
- Tier 0 to Tier 1 (VIOLATION): [count]
- Tier 0 to Tier 2 (VIOLATION): [count]

**Tier 1 Violations:**

- Total Tier 1 access events: [count]
- Tier 1 to Tier 1 (compliant): [count]
- Tier 1 to Tier 0 (N/A - Tier 1 cannot access Tier 0): [count]
- Tier 1 to Tier 2 (VIOLATION): [count]

**Violation Details:**
For each violation:

- Event ID (from Sheet 1)
- Timestamp
- Privileged Account
- Violation Type (Tier 0→1, Tier 0→2, Tier 1→2)
- Destination System
- Remediation Action (investigate, retrain user, enforce GPO, other)

**Step 6: Complete Sheet 4 - Session Recording Coverage**

For each privileged session:

1. **Session Details** (Columns A-F):

   - Session ID
   - Timestamp
   - Privileged Account
   - System Accessed
   - Session Duration (minutes)
   - Session Recorded: Yes, No

2. **Recording Quality** (Columns G-I):

   - Recording Type: Video, Keystroke Log, Both, None
   - Playback Verified: Yes, No (did we test playback?)
   - Recording Location: PAM solution path, file path

3. **Gap Analysis** (Columns J-K):

   - Recording Required: Yes, No (per policy - Tier 0 mandatory, Tier 1 recommended)
   - Recording Gap: Yes, No (required but not recorded)

**Step 7: Complete Sheet 5 - Privileged Access Review Status**

For each privileged user:

1. **User Details** (Columns A-D):

   - User Name
   - Privileged Accounts Owned (count)
   - Highest Tier Access (Tier 0, Tier 1, Tier 2)
   - Manager

2. **Review Status** (Columns E-I):

   - Last Review Date
   - Review Due Date (quarterly = last review + 90 days)
   - Review Status: Completed, Overdue, Upcoming
   - Review Outcome: Access Confirmed, Access Removed, Access Modified
   - Reviewer (manager or delegated reviewer)

3. **Compliance** (Columns J-K):

   - Review Overdue Days: [calculated: today - due date if overdue]
   - Compliance: Compliant, Overdue

**Step 8: Review Calculated Metrics**

The workbook automatically calculates:

- **Privileged Access Events (Quarter)**: Total count
- **Off-Hours Access Events**: Count and percentage
- **Tier Isolation Violations**: Count (target: 0)
- **Session Recording Coverage**: Percentage of sessions recorded
- **Access Review Completion**: Percentage of privileged users with up-to-date reviews

**Step 9: Collect Evidence**

Required evidence:

- **SIEM Privileged Access Dashboard**: Screenshot showing privileged activity summary
- **Tier Isolation Violation Report**: SIEM query results or log export
- **Session Recording Examples**: Screenshots of recorded sessions (redact sensitive commands)
- **Access Review Completion Records**: Manager sign-offs, review meeting minutes

Store evidence in: `/evidence/privileged-monitoring/[quarter]/`

**Step 10: Complete Evidence Register (Sheet 6)**

Document all collected evidence with links.

**Step 11: Approval & Sign-Off (Sheet 7)**

Three-level approval process.

---

# Evidence Collection Guidelines

## Required Evidence Types

**For Privileged Access Monitoring:**

1. **SIEM Privileged Access Dashboard**:

   - Screenshot of privileged access summary
   - Date range visible (quarter being assessed)
   - Metrics visible (event count, alerts, anomalies)

2. **Privileged Access Log Export**:

   - CSV or JSON export from SIEM
   - Columns: timestamp, user, source, destination, event type
   - At least quarterly data (3 months)

3. **Tier Isolation Violations**:

   - SIEM query showing cross-tier access
   - Alert notifications for tier violations
   - Investigation results (false positive, legitimate exception, actual violation)

4. **Session Recording Evidence**:

   - Screenshot of session recording catalog
   - Example recorded session (playback screenshot)
   - Session recording configuration (which accounts, which systems)

5. **Access Review Records**:

   - Quarterly review meeting minutes
   - Manager sign-offs for privileged users
   - Access review spreadsheet with outcomes

## Evidence Storage

**Structure:**
```
/evidence/privileged-monitoring/
├── 2025-Q4/
│   ├── siem-privileged-access-dashboard.png
│   ├── privileged-access-logs-2025-Q4.csv
│   ├── tier-isolation-violations.png
│   ├── session-recording-catalog.png
│   ├── session-recording-playback-example.png
│   └── access-review-completion-2025-Q4.xlsx
├── tier-violation-investigations/
│   ├── tier0-to-tier1-violation-2025-10-15.pdf
│   └── tier1-to-tier2-violation-2025-11-20.pdf
└── access-reviews/
    ├── 2025-Q3-access-review-results.xlsx
    └── 2025-Q4-access-review-results.xlsx
```

## Evidence Quality Checklist

For each piece of evidence:

- [ ] Date/time range clearly visible
- [ ] Source system identified (SIEM, PAM, logs)
- [ ] Data matches workbook entries
- [ ] Sensitive data redacted (passwords, PII)
- [ ] Linked in Evidence Register

---

# Common Pitfalls & How to Avoid Them

## Pitfall 1: Not Monitoring Service Account Privileged Access

**Problem**: Only monitoring interactive privileged access, missing service account activity

**Solution**:

- Monitor ALL privileged access (interactive + service accounts)
- Service accounts often have elevated privileges (SQL Server service account = DBA)
- Alert on unusual service account activity (unexpected time, unexpected system)

## Pitfall 2: Alert Fatigue

**Problem**: Too many privileged access alerts, SOC ignores them

**Solution**:

- Tune alerts (reduce false positives)
- Prioritize: Tier 0 access = HIGH priority, Tier 2 = LOW priority
- Use baseline: Alert on UNUSUAL privileged access, not ALL privileged access
- Use risk scoring: Off-hours + unusual system + failed attempts = HIGH RISK

## Pitfall 3: Not Testing Session Recording Playback

**Problem**: Assuming session recording works without testing playback

**Solution**:

- Quarterly: Test playback of recorded sessions
- Verify: Can we actually watch the recording?
- Check: Is audio included? Is video quality sufficient?
- Test: Can we search recordings by user, system, time?

## Pitfall 4: Access Reviews as Checkbox Exercise

**Problem**: Managers approve privileged access without actually reviewing

**Solution**:

- Provide context: "John Doe has Domain Admin access, last used: yesterday"
- Ask specific questions: "Does John still need this access? Has his role changed?"
- Require justification: "Why does John need Domain Admin?"
- Track outcomes: Access confirmed, access removed, access modified (not just "reviewed")

## Pitfall 5: Ignoring Failed Privileged Login Attempts

**Problem**: Only monitoring successful privileged access, missing attack attempts

**Solution**:

- Track failed privileged logins (Event ID 4625 with elevated privileges)
- Multiple failed attempts = potential brute force attack
- Failed login + successful login shortly after = potential credential compromise
- Alert threshold: 5+ failed attempts within 15 minutes = INVESTIGATE

## Pitfall 6: Not Correlating with User Context

**Problem**: Flagging legitimate off-hours access as suspicious

**Solution**:

- Know your users: DBA on-call rotation expects off-hours access
- Know your systems: Scheduled maintenance windows are expected
- Document exceptions: "John Doe is on-call, off-hours access expected this week"
- Use UBA: Learn normal behavior, alert on deviations from normal

## Pitfall 7: Missing Cross-Platform Privileged Access

**Problem**: Monitoring Active Directory privileged access but missing Azure, AWS, GCP

**Solution**:

- Monitor ALL platforms (AD, Entra ID, AWS IAM, GCP IAM, Okta, applications)
- Correlate: Same user with admin rights in AD AND AWS (multiple attack surfaces)
- Cloud privileged access is JUST AS CRITICAL as on-prem

## Pitfall 8: Not Investigating Tier Violations

**Problem**: Detecting tier isolation violations but not investigating WHY

**Solution**:

- Every tier violation requires investigation
- Ask: "Why did Domain Admin log into file server?"
- Answer might be: Legitimate break-glass scenario, mistake (user used wrong account), malicious activity
- Document: Legitimate exception, retraining required, security incident

## Pitfall 9: Session Recordings Not Retained

**Problem**: Recording sessions but deleting recordings after 30 days

**Solution**:

- Retention requirements: FINMA requires privileged session logs retained per data retention policy
- Typical retention: 90 days online, 1-7 years archived
- Critical sessions: Retain indefinitely (incident investigations, compliance audits)

## Pitfall 10: Not Sharing Monitoring Results

**Problem**: Security team has great privileged access monitoring, but nobody else knows

**Solution**:

- Quarterly report to CISO: Privileged access metrics, anomalies detected, investigations
- Share with privileged users: "Your off-hours access was flagged, here's why"
- Executive dashboard: Tier isolation compliance, session recording coverage, access review completion
- Celebrate: "Zero tier violations this quarter!"

---

# Quality Checklist

Before submitting assessment for approval, verify:

## Completeness

- [ ] All privileged access events documented (or representative sample if volume is high)
- [ ] Privileged commands tracked (sudo, runas, admin PowerShell)
- [ ] Tier isolation violations identified (all violations documented)
- [ ] Session recording coverage assessed
- [ ] Access reviews tracked for all privileged users

## Accuracy

- [ ] Log data validated against SIEM
- [ ] Tier classifications match IMP.3 (Privileged Account Inventory)
- [ ] Timestamps in correct timezone
- [ ] Anomaly detections reviewed (not just auto-flagged)
- [ ] Access review status validated with managers

## Evidence Quality

- [ ] SIEM dashboard screenshots collected
- [ ] Session recording playback verified
- [ ] Access review completion records collected
- [ ] Tier violation investigation results documented
- [ ] Evidence dated and linked

## Compliance

- [ ] Tier isolation violations flagged as CRITICAL
- [ ] Session recording gaps for Tier 0 flagged as HIGH priority
- [ ] Overdue access reviews flagged
- [ ] Off-hours anomalies investigated

## Professional Presentation

- [ ] No spelling errors
- [ ] Consistent date formatting (DD.MM.YYYY HH:MM)
- [ ] Clear and concise investigation notes
- [ ] Executive summary suitable for CISO review

---

# Interpreting Results

## Understanding Monitoring Metrics

**Privileged Access Event Volume:**

- **Baseline Established**: Compare quarter-over-quarter (is volume increasing/decreasing?)
- **Spike Detection**: Sudden increase = potential attack, new system deployment, policy change
- **Trend Analysis**: Gradual increase = normal growth, gradual decrease = automation/consolidation

**Off-Hours Access Percentage:**

- **<5%**: Excellent - Most privileged access during business hours
- **5-15%**: Acceptable - Some on-call/maintenance activity
- **15-30%**: Review Required - High off-hours activity (is this expected?)
- **>30%**: CONCERN - Unusual pattern (investigate)

**Tier Isolation Compliance:**

- **Zero violations**: Excellent - Tier isolation enforced
- **1-5 violations/quarter**: Acceptable - Investigate each violation
- **>5 violations/quarter**: CRITICAL - Architectural enforcement failure (GPO, Conditional Access not working)

**Session Recording Coverage:**

- **100% Tier 0 sessions recorded**: Target state (MANDATORY)
- **90-100% Tier 1 sessions recorded**: Good (RECOMMENDED)
- **<90% Tier 1 sessions recorded**: Gap - Expand session recording
- **Any Tier 0 session NOT recorded**: CRITICAL GAP

**Access Review Completion:**

- **100% reviews completed on time**: Excellent
- **90-99% completed**: Good - Follow up on overdue reviews
- **<90% completed**: POOR - Access review process not enforced

## Anomaly Prioritization

**Priority 1 - CRITICAL (Immediate Investigation - Within 4 Hours):**

- Tier 0 account accessing Tier 1 or Tier 2 system
- Multiple failed privileged login attempts (>5 within 15 minutes)
- Privileged access from unexpected geography (impossible travel)
- Privileged access to Tier 0 systems from non-PAW workstation

**Priority 2 - HIGH (Investigation Within 24 Hours):**

- Off-hours privileged access without on-call schedule justification
- Privileged account accessing systems outside typical scope
- Unusual privileged commands (user account creation, privilege escalation)
- Tier 1 account accessing Tier 2 system

**Priority 3 - MEDIUM (Investigation Within 1 Week):**

- Single failed privileged login attempt
- Off-hours access with on-call justification (confirm legitimacy)
- Session recording missing for Tier 1 account

**Priority 4 - LOW (Track for Trends):**

- Normal privileged access patterns (business hours, expected systems)
- Scheduled maintenance window privileged access

## Regulatory Compliance Interpretation

**FINMA Compliance** (if Swiss financial institution):

- Margin 63-72: Logging and monitoring requirements
- Privileged access monitoring demonstrates compliance
- Session recordings = evidence of privileged access monitoring
- Target: Continuous monitoring, quarterly reviews documented

**DORA Compliance** (if EU financial entity):

- Article 10: Monitoring and logging of privileged access
- Target: Real-time monitoring, alerting on anomalies, quarterly reporting

---

# Review & Approval Process

## Approval Workflow

**Level 1 - Preparer (SOC Team / Security Analyst)**:

- Extract privileged access logs
- Analyze activity and identify anomalies
- Investigate alerts
- Complete assessment workbook
- Collect evidence
- Submit for review

**Level 2 - Reviewer (Security Team Lead / Senior SOC Analyst)**:

- Validate log analysis accuracy
- Review anomaly investigations
- Verify tier isolation compliance
- Confirm session recording coverage
- Approve and forward to CISO

**Level 3 - Approver (CISO)**:

- Review privileged access metrics
- Validate critical anomalies investigated
- Approve access review completion
- Sign off on quarterly assessment
- Present to Executive Management (if required)

## Approval Criteria

Assessment is approved when:

- [ ] Privileged access activity documented for assessment period
- [ ] Tier isolation violations investigated
- [ ] Session recording coverage assessed
- [ ] Access reviews completed (or overdue reviews escalated)
- [ ] Anomalies investigated
- [ ] Evidence collected and linked

## Post-Approval Actions

After CISO approval:
1. **Communicate Results**: Share privileged access metrics with privileged users, IT Ops, Executive Management
2. **Escalate Critical Issues**: Tier violations, compromised accounts escalated immediately
3. **Track Remediation**: Session recording gaps, access review overdue → Dashboard (IMP.6)
4. **Schedule Next Review**: Set calendar reminder for next quarterly assessment

---

**END OF USER GUIDE**

---

*"Power unchecked is a vulnerability waiting to be exploited."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
