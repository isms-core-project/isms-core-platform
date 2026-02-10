<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.30.4-UG:framework:UG:a.8.30.4 -->
**ISMS-IMP-A.8.30.4-UG - Monitoring and Exceptions Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.30: Outsourced Development

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.8.30.4-UG |
| **Document Title** | Monitoring and Exceptions Dashboard Specification |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.8.30: Outsourced Development |
| **Parent Policy** | ISMS-POL-A.8.30 (Outsourced Development) |
| **Version** | 1.0 |
| **Classification** | Internal |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO/ISO | Initial implementation specification for ISO 27001:2022 first certification |

---

This section provides step-by-step guidance for using and maintaining the Monitoring and Exceptions Dashboard. Follow this guide to ensure effective oversight of outsourced development security and proper exception management.

---

## Assessment Overview

### Purpose

The Monitoring and Exceptions Dashboard consolidates outsourced development security status, tracks policy exceptions, monitors vendor performance, and provides executive reporting on compliance posture. It serves as the central command centre for A.8.30 control effectiveness.

ISO/IEC 27001:2022 Control A.8.30 states:

> *"The organisation should direct, monitor and review the activities related to outsourced system development."*

This dashboard directly supports the "monitor and review" requirements by providing consolidated visibility into vendor security compliance and enabling evidence-based management decisions.

### Scope and Applicability

**This dashboard aggregates data from:**

| Source Workbook | Data Aggregated |
|-----------------|-----------------|
| ISMS-IMP-A.8.30.1 | Approved vendor count, assessment status, overdue reassessments |
| ISMS-IMP-A.8.30.2 | Contract count, clause compliance, SLA compliance |
| ISMS-IMP-A.8.30.3 | Deliverable count, testing status, SBOM compliance |

**This dashboard provides:**

| Function | Purpose |
|----------|---------|
| Executive Dashboard | High-level compliance status for leadership |
| Vendor Performance Tracking | Individual vendor security metrics |
| Exception Register | Policy exception management |
| Monitoring Log | Activity tracking and follow-up |
| Incident Log | Security incident documentation |
| Compliance Score Calculation | Weighted overall compliance metric |

### Business Context

**Why Monitoring Matters:**

Effective monitoring transforms outsourced development from a risk liability into a managed security function:

1. **Early Warning**: Identifies problems before they become incidents
2. **Trend Analysis**: Reveals patterns requiring strategic attention
3. **Accountability**: Creates transparency for vendor performance
4. **Compliance Evidence**: Demonstrates active control to auditors
5. **Decision Support**: Enables evidence-based vendor management
6. **Risk Visibility**: Quantifies residual risk from exceptions

**Stakeholder Value:**

| Stakeholder | Dashboard Value |
|-------------|-----------------|
| CISO | Risk visibility, exception oversight, audit readiness |
| Executive Management | Compliance status, trend analysis |
| IT Security Manager | Operational metrics, performance tracking |
| Procurement | Vendor performance data for renewals |
| Auditors | Compliance evidence, monitoring records |
| Risk Committee | Exception register, incident trends |

### Assessment Outputs

Upon completion and regular maintenance, this dashboard provides:

| Output | Purpose | Audience |
|--------|---------|----------|
| Executive Dashboard | Monthly compliance summary | CISO, Executive Management |
| Vendor Performance Report | Quarterly vendor scorecards | IT Security, Procurement |
| Exception Status Report | Monthly exception tracking | CISO, Risk Committee |
| Compliance Trend Analysis | Quarterly trend reporting | Audit Committee |
| Incident Summary | As-needed incident reporting | Executive Management |
| Audit Evidence Package | Annual compliance documentation | External Auditors |

---

## Prerequisites

### Required Inputs

Before using the dashboard, ensure:

| Input | Source | Required For |
|-------|--------|--------------|
| Vendor assessment data | ISMS-IMP-A.8.30.1 | Vendor metrics |
| Contract compliance data | ISMS-IMP-A.8.30.2 | Contract metrics |
| Testing and acceptance data | ISMS-IMP-A.8.30.3 | Testing metrics |
| Exception requests | Business units | Exception register |
| Monitoring activity records | IT Security | Monitoring log |
| Incident reports | Incident Management | Incident log |

### Required Approvals

| Activity | Approver | Purpose |
|----------|----------|---------|
| Exception approval | Per exception type matrix | Formalise policy deviations |
| Report distribution | CISO | Control report audience |
| Dashboard modifications | IT Security Manager | Maintain integrity |
| Incident classification | CISO | Ensure appropriate handling |

### Required Knowledge

Dashboard users should understand:

- ISO 27001:2022 A.8.30 control requirements
- Organisation's risk appetite and tolerance
- Exception approval authority matrix
- Vendor performance expectations
- Incident classification criteria
- Reporting cadences and audiences

### Access Requirements

| Role | Access Level | Capabilities |
|------|--------------|--------------|
| Dashboard Administrator | Full | All sheets, configuration |
| IT Security Team | Full | All sheets, data entry |
| CISO | Read + Approve | View all, approve exceptions |
| Executive Management | Read | Dashboard and reports only |
| Auditors | Read | All sheets for audit purposes |
| Procurement | Read | Vendor performance only |

---

## Completion Walkthrough

### Sheet 1: Executive Dashboard – Completion Guide

**Purpose**: Provide leadership with at-a-glance visibility into outsourced development security status.

**Step-by-Step Completion:**

**Step 1: Update Source Metrics**

Pull current values from source workbooks:

| Metric | Source | Update Method |
|--------|--------|---------------|
| Approved Vendors | Workbook 1, Sheet 1 | COUNT where Status=Approved |
| Active Contracts | Workbook 2, Sheet 1 | COUNT where Status=Active |
| Pending Assessments | Workbook 1, Sheet 1 | COUNT where Status=Pending |
| Overdue Reassessments | Workbook 1, Sheet 1 | COUNT where Next_Due < TODAY |
| Contract Clause Compliance | Workbook 2, Sheet 2 | Yes / (Yes + No + Modified) |
| SLA Compliance (Critical) | Workbook 2, Sheet 3 | Met / Total Critical |
| SLA Compliance (High) | Workbook 2, Sheet 3 | Met / Total High |
| Security Testing Completion | Workbook 3, Sheet 1 | Complete / Total |
| SBOM Compliance | Workbook 3, Sheet 1 | Yes / Total |
| Active Exceptions | Sheet 3 | COUNT where Status=Approved |
| Overdue Exceptions | Sheet 3 | COUNT where Expiry < TODAY |
| Overall Compliance Score | Sheet 6 | Calculated value |

**Step 2: Calculate Trends**

For each metric, compare to previous period:

| Trend | Symbol | Definition |
|-------|--------|------------|
| Improving | ↑ | Better than previous period |
| Stable | → | Within 5% of previous period |
| Declining | ↓ | Worse than previous period |

**Step 3: Apply RAG Status**

| Status | Criteria |
|--------|----------|
| Green | Metric meets or exceeds target |
| Amber | Metric within 10% of target |
| Red | Metric more than 10% below target |

**Step 4: Document Commentary**

Add brief commentary for:
- Any Red status metrics
- Significant trend changes
- Notable events or exceptions

**Dashboard Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│ OUTSOURCED DEVELOPMENT SECURITY DASHBOARD                    │
│ Report Period: [Month Year]                                  │
├─────────────────────────────────────────────────────────────┤
│ OVERALL COMPLIANCE SCORE: [XX%] [↑↓→]                       │
├─────────────────────────────────────────────────────────────┤
│ VENDOR MANAGEMENT          │ CONTRACT COMPLIANCE            │
│ • Approved Vendors: XX     │ • Active Contracts: XX         │
│ • Pending: XX              │ • Clause Compliance: XX%       │
│ • Overdue Reviews: XX      │ • SLA Compliance: XX%          │
├─────────────────────────────────────────────────────────────┤
│ SECURITY TESTING           │ EXCEPTION MANAGEMENT           │
│ • Testing Complete: XX%    │ • Active Exceptions: XX        │
│ • SBOM Compliance: XX%     │ • Overdue: XX                  │
├─────────────────────────────────────────────────────────────┤
│ COMMENTARY:                                                  │
│ [Key observations, risks, and actions]                      │
└─────────────────────────────────────────────────────────────┘
```

### Sheet 2: Vendor Performance – Completion Guide

**Purpose**: Track individual vendor security performance for management and renewal decisions.

**Step-by-Step Completion:**

**Step 1: Identify Vendors to Track**

Include all vendors with:
- Approved status in registry
- Active contracts in past 12 months
- Delivered code in review period

**Step 2: Collect Performance Data**

For each vendor, gather:

| Metric | Source | Collection Method |
|--------|--------|-------------------|
| Active Contracts | Workbook 2, Sheet 1 | COUNT per vendor |
| Total Deliverables | Workbook 3, Sheet 1 | COUNT per vendor (12 months) |
| Security Findings | Workbook 3, Sheet 3 | SUM findings per vendor |
| Critical Findings | Workbook 3, Sheet 3 | SUM Critical per vendor |
| High Findings | Workbook 3, Sheet 3 | SUM High per vendor |
| SLA Compliance Rate | Workbook 2, Sheet 3 | Met / Total per vendor |
| Avg Remediation Days | Workbook 2, Sheet 3 | AVG days per vendor |
| Security Incidents | Sheet 5 | COUNT per vendor (12 months) |
| Last Assessment Date | Workbook 1, Sheet 1 | Date per vendor |

**Step 3: Calculate Performance Score**

Performance score is weighted calculation:

| Component | Weight | Calculation |
|-----------|--------|-------------|
| SLA Compliance | 40% | (SLA_Met / Total) × 100 |
| Findings Severity | 30% | 100 - (Critical×20 + High×10 + Medium×5) |
| Assessment Currency | 15% | 100 if current, -5 per month overdue |
| Incident History | 15% | 100 - (Incidents × 25) |

**Formula:**
```
Performance_Score = (SLA × 0.40) + (Findings × 0.30) + (Assessment × 0.15) + (Incident × 0.15)
```

**Score Interpretation:**

| Score Range | Rating | Action |
|-------------|--------|--------|
| 90-100 | Excellent | Continue engagement |
| 80-89 | Good | Monitor standard |
| 70-79 | Acceptable | Enhanced monitoring |
| 60-69 | Concerning | Performance improvement plan |
| <60 | Unacceptable | Contract review, potential termination |

**Step 4: Determine Performance Trend**

Compare to previous quarter:

| Trend | Definition | Indicator |
|-------|------------|-----------|
| Improving | Score increased >5 points | ↑ |
| Stable | Score within ±5 points | → |
| Declining | Score decreased >5 points | ↓ |

**Step 5: Document Notes**

For each vendor, record:
- Notable achievements
- Areas of concern
- Planned actions
- Relationship status

### Sheet 3: Exception Register – Completion Guide

**Purpose**: Track all approved exceptions to A.8.30 requirements with proper governance.

**Step-by-Step Completion:**

**Step 1: Generate Exception ID**

Create unique identifier using format `EXC-XXXX`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | EXC- | EXC- |
| Sequential Number | 4 digits | 0023 |
| Full ID | EXC-XXXX | EXC-0023 |

**Step 2: Classify Exception Type**

| Exception Type | Examples | Typical Duration |
|----------------|----------|------------------|
| Vendor Assessment | Deferred assessment, reduced scope | 90 days max |
| Contract Clause | Missing clause, modified SLA | Contract duration |
| SLA | Extended remediation timeline | 30-90 days |
| Testing | Reduced testing scope, deferred test | 90 days max |
| Training | Deferred training completion | 60 days max |

**Step 3: Document Exception Details**

| Field | Guidance |
|-------|----------|
| Related_Entity | Vendor_ID, Contract_ID, or Deliverable_ID |
| Requirement_Reference | Specific policy section being excepted |
| Exception_Description | Clear description of what is being excepted |
| Risk_Level | Risk of the exception itself |
| Business_Justification | Why exception is necessary |
| Compensating_Controls | Controls reducing exception risk |

**Step 4: Risk Assessment**

Classify exception risk:

| Risk Level | Definition | Approval Level |
|------------|------------|----------------|
| Critical | Direct impact on security posture | CISO + Executive |
| High | Significant security implication | CISO |
| Medium | Moderate security implication | IT Security Manager |
| Low | Minor deviation, well-compensated | IT Security Lead |

**Step 5: Submit for Approval**

Complete approval workflow:

1. **Requestor** submits exception request
2. **IT Security** reviews and assesses risk
3. **Approver** (per matrix) approves or rejects
4. **Exception** recorded in register with expiry date

**Step 6: Set Review and Expiry Dates**

| Exception Type | Maximum Duration | Review Frequency |
|----------------|------------------|------------------|
| Vendor Assessment | 90 days | 30 days |
| Contract Clause | Contract duration | Quarterly |
| SLA Extension | Per severity | At extension end |
| Testing Deferral | 90 days | Monthly |
| Training | 60 days | Monthly |

**Step 7: Manage Exception Lifecycle**

| Status | Definition | Actions |
|--------|------------|---------|
| Pending | Awaiting approval | Complete approval workflow |
| Approved | Active exception | Monitor, schedule reviews |
| Rejected | Not approved | Document rationale, notify requestor |
| Expired | Past expiry date | Close or renew |
| Renewed | Extended beyond original | Requires re-approval |
| Remediated | Root cause resolved | Close exception |

**Renewal Process:**

If exception needs renewal:
1. Review necessity (can root cause be addressed?)
2. Document updated justification
3. Verify compensating controls still effective
4. Obtain fresh approval
5. Increment renewal counter

**Maximum Renewals:**

| Risk Level | Maximum Renewals | After Maximum |
|------------|------------------|---------------|
| Critical | 1 | Executive escalation required |
| High | 2 | CISO escalation required |
| Medium | 3 | Risk acceptance required |
| Low | 4 | Management review required |

### Sheet 4: Monitoring Log – Completion Guide

**Purpose**: Track all monitoring activities for outsourced development relationships.

**Step-by-Step Completion:**

**Step 1: Generate Log ID**

Create unique identifier using format `LOG-XXXX`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | LOG- | LOG- |
| Sequential Number | 4 digits | 0156 |
| Full ID | LOG-XXXX | LOG-0156 |

**Step 2: Select Activity Type**

| Activity Type | Description | Frequency |
|---------------|-------------|-----------|
| Status Meeting | Regular vendor status review | Weekly/Bi-weekly |
| Security Review | Focused security assessment | Monthly/Quarterly |
| Audit | Formal audit activity | Annual |
| Incident Review | Post-incident review | Per incident |
| Ad-hoc | Unscheduled review or check | As needed |

**Step 3: Document Activity**

| Field | Guidance |
|-------|----------|
| Log_Date | Date of activity |
| Vendor_ID | Vendor being monitored |
| Contract_ID | Related contract |
| Activity_Type | Per type list |
| Activity_Description | What was done |
| Participants | Who participated |
| Findings | Key findings or observations |

**Step 4: Record Actions Required**

For findings requiring follow-up:

| Field | Guidance |
|-------|----------|
| Actions_Required | Specific action items |
| Action_Owner | Person responsible |
| Action_Due_Date | When action must complete |
| Action_Status | Open, In Progress, Complete, Overdue |

**Step 5: Link Evidence**

Document evidence location for all monitoring activities:
- Meeting minutes
- Review reports
- Audit findings
- Email correspondence

**Monitoring Cadence Requirements:**

| Vendor Risk Tier | Minimum Monitoring |
|------------------|-------------------|
| Critical | Monthly security review, weekly status |
| High | Quarterly security review, bi-weekly status |
| Standard | Annual security review, monthly status |

### Sheet 5: Incident Log – Completion Guide

**Purpose**: Track security incidents involving outsourced development vendors.

**Step-by-Step Completion:**

**Step 1: Generate Incident ID**

Create unique identifier using format `INC-XXXX`:

| Component | Format | Example |
|-----------|--------|---------|
| Prefix | INC- | INC- |
| Sequential Number | 4 digits | 0012 |
| Full ID | INC-XXXX | INC-0012 |

**Step 2: Record Incident Details**

| Field | Guidance |
|-------|----------|
| Incident_Date | Date incident occurred |
| Vendor_ID | Vendor involved |
| Contract_ID | Related contract |
| Incident_Type | Classification category |
| Severity | Critical, High, Medium, Low |
| Description | Detailed incident description |

**Step 3: Classify Incident Type**

| Type | Definition | Examples |
|------|------------|----------|
| Data Breach | Unauthorised data access/disclosure | Customer data exposed |
| Vulnerability Exploited | Security flaw actively exploited | Zero-day in vendor code |
| Unauthorised Access | Access beyond authorised scope | Vendor accessed production |
| Policy Violation | Breach of security requirements | Failed to notify incident |
| Other | Other security events | Malware in development env |

**Step 4: Assess Severity**

| Severity | Definition | Response Time |
|----------|------------|---------------|
| Critical | Immediate business impact, data breach | Immediate |
| High | Significant security impact | Same day |
| Medium | Limited impact, contained | 24 hours |
| Low | Minimal impact | 72 hours |

**Step 5: Verify Notification SLA**

Contract requires 24-hour notification:

| Notification_SLA_Met | Definition |
|----------------------|------------|
| Yes | Organisation notified within 24 hours |
| No | Notification delayed beyond 24 hours |

Document notification timeline:
- When incident occurred
- When vendor discovered it
- When organisation was notified
- Gap analysis if SLA missed

**Step 6: Track Remediation**

| Field | Guidance |
|-------|----------|
| Root_Cause | Root cause analysis findings |
| Impact_Assessment | Impact on organisation |
| Remediation_Actions | Actions taken/planned |
| Remediation_Date | Date remediation complete |
| Lessons_Learned | What can prevent recurrence |

**Step 7: Determine Contract Impact**

| Impact Level | Criteria | Action |
|--------------|----------|--------|
| None | Minor, well-handled | Document only |
| Warning | First offense, proper response | Formal warning |
| Review | Pattern or significant event | Contract review |
| Suspension | Serious breach | Suspend new work |
| Termination | Egregious or repeated | Contract termination |

### Sheet 6: Compliance Score Calculation – Completion Guide

**Purpose**: Calculate weighted overall compliance score for outsourced development security.

**Step-by-Step Completion:**

**Step 1: Collect Component Scores**

| Component | Weight | Data Source | Calculation |
|-----------|--------|-------------|-------------|
| Vendor Assessment | 20% | Workbook 1 | (Current assessments / Total approved) × 100 |
| Contract Compliance | 25% | Workbook 2 | (Contracts with all clauses / Total) × 100 |
| SLA Compliance | 25% | Workbook 2 | (Critical_SLA×0.4 + High_SLA×0.6) |
| Security Testing | 20% | Workbook 3 | (Complete testing / Total deliverables) × 100 |
| Exception Management | 10% | Sheet 3 | 100 - (Overdue_exceptions × 10) |

**Step 2: Calculate Overall Score**

```
Overall_Score = (Vendor × 0.20) + (Contract × 0.25) + (SLA × 0.25) + (Testing × 0.20) + (Exception × 0.10)
```

**Step 3: Apply Score Interpretation**

| Score | Status | Colour | Action |
|-------|--------|--------|--------|
| ≥90% | Compliant | Green | Maintain current practices |
| 70-89% | Needs Improvement | Amber | Address gaps, increase monitoring |
| <70% | Non-Compliant | Red | Immediate escalation, remediation plan |

**Step 4: Document Score Breakdown**

For transparency and actionability, document:
- Individual component scores
- Specific items affecting each score
- Actions to improve low-scoring areas
- Comparison to previous period

---

## Evidence Collection

### Evidence Requirements

Evidence must be maintained for all dashboard activities:

| Evidence Category | Retention Period | Storage Location |
|-------------------|------------------|------------------|
| Dashboard snapshots | 7 years | ISMS Evidence Library |
| Vendor performance reports | 7 years | ISMS Evidence Library |
| Exception approvals | 7 years | ISMS Evidence Library |
| Monitoring logs | 7 years | ISMS Evidence Library |
| Incident records | 10 years | ISMS Evidence Library |
| Compliance score history | 7 years | ISMS Evidence Library |

### Evidence Folder Structure

```
ISMS-Evidence-Library/
└── Monitoring-Dashboard/
    └── A.8.30-Outsourced-Development/
        ├── Dashboard-Snapshots/
        │   └── [YYYY-MM]-Dashboard.pdf
        ├── Vendor-Performance/
        │   └── [Quarter]-Performance-Report.pdf
        ├── Exceptions/
        │   └── [EXC-ID]/
        │       ├── Request.pdf
        │       └── Approval.pdf
        ├── Monitoring-Activities/
        │   └── [YYYY]/
        │       └── [LOG-ID]-Activity.pdf
        ├── Incidents/
        │   └── [INC-ID]/
        │       ├── Report.pdf
        │       └── Closure.pdf
        └── Compliance-Scores/
            └── [YYYY-MM]-Score.xlsx
```

### Evidence for Audit

During ISO 27001 audit, be prepared to demonstrate:

| Auditor Request | Evidence to Provide |
|-----------------|---------------------|
| "How do you monitor outsourced development?" | Monitoring log, dashboard history |
| "Show me vendor performance tracking" | Sheet 2 reports, trend analysis |
| "How are exceptions managed?" | Sheet 3, approval records |
| "What incidents have occurred?" | Sheet 5, incident reports |
| "How is compliance measured?" | Sheet 6, score history |
| "Show me governance activities" | Meeting minutes, review records |

---

## Common Pitfalls

### Dashboard Management Errors

❌ **MISTAKE: Infrequent dashboard updates**
Dashboard must be updated at least weekly. Stale data leads to missed risks and poor decisions.

❌ **MISTAKE: Not validating source data**
Garbage in, garbage out. Verify source workbooks are current before updating dashboard.

❌ **MISTAKE: Ignoring trend analysis**
Absolute numbers without trends miss important patterns. Always track direction of change.

❌ **MISTAKE: Dashboard manipulation**
Never adjust metrics to look better. Accurate reporting is essential for risk management.

### Exception Management Errors

❌ **MISTAKE: Exceptions without compensating controls**
Every exception must have compensating controls. Exceptions without controls are unmanaged risk.

❌ **MISTAKE: Not tracking exception expiry**
Expired exceptions must be closed or renewed. Zombie exceptions create compliance gaps.

❌ **MISTAKE: Excessive renewals without remediation**
Repeated renewals indicate permanent exceptions. Require root cause remediation or risk acceptance.

❌ **MISTAKE: Approving without proper authority**
Exception approval must follow authority matrix. Unauthorised approvals are invalid.

### Monitoring Errors

❌ **MISTAKE: Monitoring without documentation**
Undocumented monitoring has limited audit value. Always record activities and findings.

❌ **MISTAKE: Not following up on actions**
Identified actions must be tracked to completion. Untracked actions may never complete.

❌ **MISTAKE: Inconsistent monitoring cadence**
Monitoring frequency must match risk tier. Critical vendors need more attention.

### Incident Management Errors

❌ **MISTAKE: Delayed incident recording**
Incidents must be recorded immediately. Delayed recording loses details and delays response.

❌ **MISTAKE: Not assessing contract impact**
Every incident should evaluate contract impact. Patterns of incidents may warrant termination.

❌ **MISTAKE: Skipping lessons learned**
Every incident is a learning opportunity. Document and implement improvements.

---

## Quality Checklist

### Weekly Dashboard Checklist

Before publishing weekly dashboard:

- [ ] Source workbooks reviewed and current
- [ ] All metrics calculated correctly
- [ ] Trends compared to previous week
- [ ] RAG status applied appropriately
- [ ] Commentary updated for Red items
- [ ] Dashboard snapshot saved to evidence

### Monthly Activities Checklist

Monthly governance activities:

- [ ] Vendor performance scores updated
- [ ] Exception register reviewed
- [ ] Overdue exceptions addressed
- [ ] Monitoring activities completed per cadence
- [ ] Monthly report generated and distributed
- [ ] Actions from previous month verified complete

### Quarterly Review Checklist

Quarterly governance activities:

- [ ] Vendor performance trends analysed
- [ ] Compliance score trend reviewed
- [ ] Exception patterns analysed
- [ ] Quarterly report to management
- [ ] Process improvements identified
- [ ] Audit evidence organised

---

## Review and Approval

### Dashboard Approval

| Report | Approver | Distribution |
|--------|----------|--------------|
| Weekly Dashboard | IT Security Manager | IT Security Team |
| Monthly Executive Dashboard | CISO | Executive Management |
| Quarterly Vendor Performance | CISO | Procurement, Management |
| Annual Compliance Report | CISO + Executive | Audit Committee |

### Exception Approval Authority

| Exception Risk | Approver | Documentation |
|----------------|----------|---------------|
| Critical | CISO + Executive | Formal approval record |
| High | CISO | Email approval minimum |
| Medium | IT Security Manager | Email approval |
| Low | IT Security Lead | Documented approval |

### Reporting Cadence

| Report | Frequency | Audience | Due Date |
|--------|-----------|----------|----------|
| Executive Dashboard | Monthly | CISO, Executive | 5th business day |
| Vendor Performance | Quarterly | IT Security, Procurement | 10th of quarter |
| Exception Status | Monthly | CISO, Risk Committee | 5th business day |
| Compliance Score Trend | Quarterly | Audit Committee | 15th of quarter |
| Incident Summary | As needed | Executive Management | Within 48 hours |

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
