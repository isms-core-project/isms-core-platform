**ISMS-IMP-A.5.17.4-UG - Compliance and Audit Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.17

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.17.4-UG |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.17 (Authentication Information) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.17 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.17 (Authentication Information Policy)
- ISMS-IMP-A.5.17.1 (Password Policy Implementation Guide)
- ISMS-IMP-A.5.17.2 (MFA Deployment Assessment)
- ISMS-IMP-A.5.17.3 (Authentication Management Procedures)
- ISMS-POL-A.5.24-28 (Incident Management)

---

## Assessment Overview

### Purpose

The **Compliance and Audit Dashboard** (ISMS-IMP-A.5.17.4) provides ongoing visibility into authentication security compliance. This dashboard tracks key performance indicators (KPIs), authentication events, audit findings, and remediation progress. It serves as the central monitoring tool for A.5.17 control effectiveness.

### Scope

This dashboard covers:
- **Executive summary**: High-level compliance metrics and status
- **Compliance KPIs**: Key performance indicators for authentication security
- **Authentication events**: Event monitoring and anomaly tracking
- **Audit findings**: Internal and external audit finding management
- **Remediation tracking**: Gap and finding remediation progress

### Business Value

Maintaining this dashboard delivers:
- **Real-time compliance visibility** for management reporting
- **Event trend analysis** to identify security issues
- **Audit preparation** with pre-compiled evidence
- **Continuous improvement** through KPI tracking
- **Risk-based prioritisation** of security investments

### Control Requirement

> *ISO/IEC 27001:2022 Annex A.5.17 — Authentication Information*
>
> "The allocation and management of authentication information should be controlled by a management process, including advising personnel on appropriate handling of authentication information."

This dashboard monitors ongoing compliance with authentication information management requirements.

---

## Prerequisites

Before starting this dashboard, ensure you have:

### Required Documents
- [ ] ISMS-IMP-A.5.17.1 (Password Policy) — policy compliance baseline
- [ ] ISMS-IMP-A.5.17.2 (MFA Deployment) — MFA coverage baseline
- [ ] ISMS-IMP-A.5.17.3 (Authentication Management) — process compliance
- [ ] Incident management records
- [ ] Audit reports (internal and external)

### Required Access
- [ ] SIEM/security monitoring dashboards
- [ ] Identity provider admin console (Azure AD, Okta)
- [ ] Authentication log data
- [ ] Audit finding database
- [ ] Risk register

### Required Personnel
- [ ] Information Security Officer (dashboard owner)
- [ ] IT Security Analyst (event data)
- [ ] Identity & Access Management Team
- [ ] Internal Audit Representative
- [ ] Risk Management Officer

---

## Completion Walkthrough

### Sheet 1: Instructions

**Purpose**: Provides dashboard guidance and update frequency recommendations.

**Actions**:
1. Review the dashboard purpose
2. Note update frequencies for each sheet
3. Understand metric definitions
4. Proceed to Executive_Summary

### Sheet 2: Executive_Summary

**Purpose**: Provide management with high-level authentication compliance status.

**Key Metrics Section** (Rows 5-10):

| Metric Box | Description | Target |
|------------|-------------|--------|
| Overall Compliance | Weighted average across all areas | ≥90% |
| MFA Adoption Rate | % of users enrolled in MFA | ≥95% |
| Password Policy Compliance | % of accounts meeting policy | 100% |
| Failed Login Rate | % of failed vs total logins | <5% |
| Open Findings | Count of unresolved audit findings | Minimise |

**Compliance by Area Table**:

| Area | What to Track |
|------|---------------|
| Password Policy | Compliance with length, complexity, history |
| MFA Implementation | Enrollment rate, usage rate, coverage |
| Credential Lifecycle | Proper allocation, change, revocation |
| System Security | Storage security, integration compliance |
| User Responsibilities | Training completion, policy acknowledgment |
| Audit Logging | Log coverage, retention, monitoring |

**Key Actions Section**:
Document top 5 priority actions with owner, due date, and status.

### Sheet 3: Compliance_KPIs

**Purpose**: Track key performance indicators over time.

**For Each KPI, Document**:

| Column | Description | Example |
|--------|-------------|---------|
| KPI ID | Unique identifier | "KPI-AUTH-001" |
| KPI Name | Short name | "MFA Enrollment Rate" |
| Description | What it measures | "% of users enrolled in MFA" |
| Target | Expected value | "100%" |
| Current Value | Actual measurement | "94%" |
| Status | Against target | "At Risk" |
| Trend | Direction of change | "↑ Improving" |
| Owner | Accountable person | "IAM Manager" |
| Notes | Context or actions | "5 new users pending enrollment" |

**Standard Authentication KPIs**:

| KPI ID | Name | Target |
|--------|------|--------|
| KPI-AUTH-001 | MFA Enrollment Rate | 100% |
| KPI-AUTH-002 | MFA Usage Rate | ≥95% |
| KPI-AUTH-003 | Password Policy Compliance | 100% |
| KPI-AUTH-004 | Failed Login Rate | <5% |
| KPI-AUTH-005 | Account Lockout Rate | <2 per 1000 users/day |
| KPI-AUTH-006 | Password Reset Volume | <50 per 1000 users/month |
| KPI-AUTH-007 | Credential Exposure | 0 |
| KPI-AUTH-008 | Service Account Rotation | 100% on schedule |
| KPI-AUTH-009 | SSO Coverage | ≥90% |
| KPI-AUTH-010 | Privileged Account MFA | 100% |
| KPI-AUTH-011 | Training Completion | ≥95% |
| KPI-AUTH-012 | Audit Finding Closure | ≥85% within SLA |

### Sheet 4: Authentication_Events

**Purpose**: Track and monitor authentication-related security events.

**For Each Event Category**:

| Column | Description | Example |
|--------|-------------|---------|
| Event Category | Type of event | "Failed Logins" |
| This Period | Current period count | "1,234" |
| Previous Period | Last period count | "1,456" |
| Change | Trend direction/amount | "-15%" |
| Threshold | Alert threshold | "<5% of total" |
| Alert Status | Current status | "Normal" |
| Investigation | Action taken | "None Required" |
| Notes | Context | "Expected decrease after MFA rollout" |

**Event Categories to Monitor**:
- Total Login Attempts (baseline)
- Successful Logins
- Failed Logins
- Account Lockouts
- Password Resets (Self-Service and Admin)
- MFA Failures
- MFA Bypass Events
- Impossible Travel Alerts
- Unknown Device Logins
- After Hours Logins
- Service Account Logins
- Privilege Escalation
- Emergency Access (Break-Glass)

**Alert Status Options**:
- **Normal**: Within expected thresholds
- **Warning**: Approaching threshold
- **Alert**: Threshold exceeded
- **Critical**: Requires immediate attention

### Sheet 5: Audit_Findings

**Purpose**: Track audit findings related to authentication controls.

**For Each Finding**:

| Column | Description | Example |
|--------|-------------|---------|
| Finding ID | Unique identifier | "AUD-AUTH-001" |
| Audit Type | Source of finding | "ISO 27001 Audit" |
| Audit Date | When discovered | "10.01.2026" |
| Finding Description | What was found | "Password complexity not enforced on legacy system" |
| Affected Area | Control area impacted | "Password Policy" |
| Severity | Finding severity | "High" |
| Recommendation | Auditor's suggestion | "Implement password filter or migrate to AD" |
| Owner | Accountable person | "Infrastructure Lead" |
| Due Date | Target remediation | "28.02.2026" |
| Status | Current state | "In Progress" |
| Notes | Progress updates | "Migration scheduled for Feb" |

**Audit Types**:
- Internal Audit
- ISO 27001 Audit
- Penetration Test
- SOC 2 Audit
- Customer Audit
- Self-Assessment

**Finding Status**:
- Open
- In Progress
- Remediated
- Verified (closed)
- Risk Accepted
- Overdue

### Sheet 6: Remediation_Tracker

**Purpose**: Track all remediation activities to closure.

**For Each Remediation Item**:

| Column | Description | Example |
|--------|-------------|---------|
| Item ID | Unique identifier | "REM-AUTH-001" |
| Source | Where gap identified | "Audit Finding" |
| Description | What needs fixing | "Enable MFA for VPN access" |
| Priority | Urgency level | "High" |
| Remediation Plan | How to fix | "Configure MFA on VPN gateway" |
| Owner | Accountable person | "Network Team Lead" |
| Start Date | When started | "15.01.2026" |
| Target Date | Expected completion | "15.02.2026" |
| Status | Current state | "In Progress" |
| Notes | Progress updates | "Testing in non-prod" |

**Source Types**:
- Audit Finding
- Assessment Gap
- Incident RCA (Root Cause Analysis)
- Risk Assessment
- Management Review
- Other

### Sheet 7: Evidence_Register

**Purpose**: Track all dashboard supporting evidence.

**For Each Evidence Item**:

| Column | Description | Example |
|--------|-------------|---------|
| Evidence ID | Unique identifier | "EV-517-CD-001" |
| Evidence Type | Document category | "Report" |
| Description | What it demonstrates | "Monthly compliance dashboard" |
| Related Section | Dashboard component | "Executive_Summary" |
| Location/Link | Where stored | "SharePoint/ISMS/Reports" |
| Date | When collected | "01.02.2026" |
| Collected By | Who gathered | "Security Analyst" |
| Status | Current status | "Verified" |

### Sheet 8: Approval_SignOff

**Purpose**: Monthly approval of dashboard accuracy.

**Complete**:
1. Document Information (verify dates)
2. Reporting Period (specify month covered)
3. Approval Signatures:

| Role | Responsibility |
|------|----------------|
| Dashboard Owner | Accuracy and completeness |
| IT Security Manager | Technical validation |
| Information Security Officer | Overall approval |
| CISO | Executive oversight |

---

## Evidence Collection

### Evidence by Sheet

| Sheet | Required Evidence |
|-------|-------------------|
| Executive_Summary | Monthly dashboard PDF export |
| Compliance_KPIs | KPI source data, calculation methodology |
| Authentication_Events | SIEM reports, log extracts |
| Audit_Findings | Audit reports, finding documentation |
| Remediation_Tracker | Remediation evidence, completion proof |

### Evidence Storage

Store all evidence in:
```
/ISMS/Evidence/A.5.17-Authentication/
├── A.5.17.4-Compliance-Dashboard/
│   ├── Dashboard-Reports/
│   ├── KPI-Data/
│   ├── Event-Analysis/
│   ├── Audit-Findings/
│   └── Remediation-Evidence/
```

---

## Common Pitfalls

### ❌ MISTAKE: Updating dashboard only before audits
✅ CORRECT: Maintain continuous updates per recommended frequency

### ❌ MISTAKE: Calculating KPIs without documented methodology
✅ CORRECT: Document how each KPI is calculated and data sources

### ❌ MISTAKE: Not investigating authentication anomalies
✅ CORRECT: Review all Warning/Alert status events and document investigation

### ❌ MISTAKE: Closing findings without verification evidence
✅ CORRECT: Require proof of remediation before marking "Verified"

### ❌ MISTAKE: Not correlating failed logins with account lockouts
✅ CORRECT: Analyse relationships between event categories

### ❌ MISTAKE: Missing MFA bypass events monitoring
✅ CORRECT: Alert on ANY MFA bypass - these should be rare/zero

### ❌ MISTAKE: Not tracking service account authentication separately
✅ CORRECT: Service accounts have different risk profiles; track separately

### ❌ MISTAKE: KPIs set to unachievable targets
✅ CORRECT: Set realistic targets based on baseline measurements

### ❌ MISTAKE: Not escalating overdue remediation items
✅ CORRECT: Implement automatic escalation for items past due

### ❌ MISTAKE: Dashboard metrics not aligned with business risk
✅ CORRECT: Focus KPIs on metrics that indicate actual security posture

---

## Quality Checklist

Before submitting the dashboard, verify:

### Executive Summary
- [ ] Reporting period clearly stated
- [ ] All key metrics populated
- [ ] Compliance scores calculated correctly
- [ ] Key actions identified and assigned

### Compliance KPIs
- [ ] All KPIs have current values
- [ ] Status reflects actual vs target
- [ ] Trend direction documented
- [ ] Owners assigned
- [ ] Calculation methodology documented

### Authentication Events
- [ ] All event categories tracked
- [ ] Thresholds defined and appropriate
- [ ] Alert status reflects actual state
- [ ] Investigations documented for anomalies

### Audit Findings
- [ ] All findings have owners
- [ ] Due dates are realistic
- [ ] Overdue items flagged
- [ ] Closure evidence documented

### Remediation Tracker
- [ ] All gaps/findings tracked
- [ ] Priority reflects risk
- [ ] Progress notes current
- [ ] Completed items have evidence

### Approval
- [ ] All approvals obtained
- [ ] Dashboard archived for records

---

## Review and Approval

### Update Schedule
- **Executive Summary**: Monthly
- **KPIs**: Monthly (end of month)
- **Authentication Events**: Weekly minimum, real-time preferred
- **Audit Findings**: After each audit
- **Remediation**: Weekly

### Approval Workflow
1. **Dashboard Owner** updates all sheets
2. **IT Security Manager** validates technical accuracy
3. **ISO** reviews and approves
4. **CISO** signs off for executive reporting

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
