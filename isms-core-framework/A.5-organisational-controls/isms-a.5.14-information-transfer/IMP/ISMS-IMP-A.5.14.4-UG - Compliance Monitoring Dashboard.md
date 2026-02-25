<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.14.4-UG:framework:UG:a.5.14.4 -->
**ISMS-IMP-A.5.14.4-UG - Compliance Monitoring Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.14

---

## Document Control

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.14.4-UG |
| **Document Type** | Implementation Guide |
| **Parent Policy** | ISMS-POL-A.5.14 (Information Transfer) |
| **Control Reference** | ISO/IEC 27001:2022 Control A.5.14 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | Information Security Officer |
| **Last Updated** | [Date to be set] |

**Related Documents:**
- ISMS-POL-A.5.14 (Information Transfer Policy)
- ISMS-IMP-A.5.14.1 (Transfer Rules and Procedures)
- ISMS-IMP-A.5.14.2 (Channel Security Assessment)
- ISMS-IMP-A.5.14.3 (Transfer Agreements Register)
- ISMS-POL-A.5.24-28 (Incident Management)

---

## Assessment Overview

### Purpose

The **Compliance Monitoring Dashboard** (ISMS-IMP-A.5.14.4) provides ongoing visibility into information transfer security compliance. This dashboard tracks key performance indicators (KPIs), security incidents related to transfers, audit findings, and remediation progress. It serves as the central monitoring tool for A.5.14 control effectiveness.

### Scope

This dashboard covers:
- **Executive summary**: High-level compliance overview and key metrics
- **Compliance KPIs**: Key performance indicators for transfer security
- **Transfer incidents**: Security incident tracking specific to information transfer
- **Audit findings**: Internal and external audit findings related to A.5.14
- **Remediation tracking**: Gap and finding remediation progress

### Business Value

Maintaining this dashboard delivers:
- **Real-time compliance visibility** for management reporting
- **Incident trend analysis** to identify systemic issues
- **Audit preparation** with pre-compiled evidence
- **Continuous improvement** through KPI tracking
- **Risk-based prioritisation** of security investments

### Control Requirement

> *ISO/IEC 27001:2022 Annex A.5.14 — Information Transfer*
>
> "Information transfer rules, procedures, or agreements should be in place for all types of transfer facilities within the organization and between the organization and other parties."

This dashboard monitors ongoing compliance with established transfer rules and procedures.

---

## Prerequisites

Before starting this dashboard, ensure you have:

### Required Documents
- [ ] ISMS-IMP-A.5.14.1 (Transfer Rules) — defines compliance requirements
- [ ] ISMS-IMP-A.5.14.2 (Channel Assessment) — provides baseline status
- [ ] ISMS-IMP-A.5.14.3 (Agreements Register) — third-party compliance data
- [ ] Incident management records
- [ ] Audit reports (internal and external)
- [ ] Previous dashboard versions (if any)

### Required Access
- [ ] Security incident management system (SIEM, ServiceNow)
- [ ] DLP reporting tools
- [ ] Audit finding database
- [ ] Risk register
- [ ] Transfer system audit logs

### Required Personnel
- [ ] Information Security Officer (dashboard owner)
- [ ] IT Security Analyst (incident data)
- [ ] Internal Audit Representative
- [ ] Risk Management Officer
- [ ] Business Unit Security Champions

---

## Completion Walkthrough

### Sheet 1: Instructions

**Purpose**: Provides dashboard guidance and update frequency recommendations.

**Key Information**:
- Dashboard purpose and scope
- Sheet descriptions
- Recommended update frequencies
- Metric definitions

**Actions**:
1. Review the purpose statement
2. Note update frequency for each sheet
3. Understand metric definitions
4. Proceed to Executive_Summary

### Sheet 2: Executive_Summary

**Purpose**: Provide management with high-level compliance status.

**Key Metrics Section** (Row 5-10):
Document the following metrics in the metric boxes:

| Metric | Description | Source |
|--------|-------------|--------|
| Overall Compliance Score | Weighted average across all domains | Calculate from A.5.14.2 |
| Transfer Channels Assessed | Number of channels with assessment | From A.5.14.2 |
| Active Transfer Agreements | Current agreement count | From A.5.14.3 |
| Open Audit Findings | Unresolved findings count | From Audit_Findings sheet |
| Transfer Incidents (YTD) | Year-to-date incident count | From Transfer_Incidents |

**Domain Compliance Section**:
Complete status for each compliance domain:

| Domain | What to Report |
|--------|----------------|
| Policy Compliance | % of transfers following approved procedures |
| Technical Controls | % of channels with required controls |
| Third-Party Risk | % of third parties with current assessments |
| User Awareness | % of users completing transfer training |
| Incident Response | Average time to resolve transfer incidents |

**Compliance by Channel Type**:
Enter counts for each channel:

| Column | Description |
|--------|-------------|
| Assessed | Total items assessed |
| Compliant | Items meeting all requirements |
| Partial | Items with gaps |
| Non-Compliant | Items failing requirements |

**Key Actions Required**:
Document top 5 priority actions:
1. List critical actions first
2. Assign owner and due date
3. Track status to completion

### Sheet 3: Compliance_KPIs

**Purpose**: Track key performance indicators over time.

**For Each KPI, Document**:

| Column | Description | Example |
|--------|-------------|---------|
| KPI ID | Unique identifier | "KPI-TRF-001" |
| KPI Name | Short name | "Transfer Policy Compliance" |
| Description | What it measures | "% of transfers following approved procedures" |
| Target | Expected value | "≥95%" |
| Current Value | Actual measurement | "92%" |
| Status | Against target | "At Risk" |
| Trend | Direction of change | "↑ Improving" |
| Owner | Accountable person | "IT Security Manager" |
| Notes | Context or actions | "3% gap due to shadow IT" |

**Standard Transfer KPIs**:

| KPI ID | Name | Target |
|--------|------|--------|
| KPI-TRF-001 | Transfer Policy Compliance | ≥95% |
| KPI-TRF-002 | Channel Encryption Coverage | 100% |
| KPI-TRF-003 | Agreement Currency | 100% |
| KPI-TRF-004 | Third-Party Security Assessments | ≥90% |
| KPI-TRF-005 | Transfer Incident Rate | <0.5 per 1000 |
| KPI-TRF-006 | Mean Time to Detect (MTTD) | <4 hours |
| KPI-TRF-007 | DLP Policy Effectiveness | ≥98% |
| KPI-TRF-008 | User Awareness Training | 100% |
| KPI-TRF-009 | Audit Finding Closure Rate | ≥85% |
| KPI-TRF-010 | Configuration Compliance | ≥95% |
| KPI-TRF-011 | Classification Labeling Accuracy | ≥90% |
| KPI-TRF-012 | External Share Review Rate | 100% |

**Status Definitions**:
- **On Target**: Meeting or exceeding target
- **At Risk**: Within 10% of target
- **Below Target**: More than 10% from target
- **Not Measured**: Data not yet available

### Sheet 4: Transfer_Incidents

**Purpose**: Track security incidents related to information transfer.

**For Each Incident, Document**:

| Column | Description | Example |
|--------|-------------|---------|
| Incident ID | Unique identifier | "INC-TRF-001" |
| Date Detected | When discovered | "15.01.2026" |
| Channel Type | Transfer method involved | "Email", "Cloud Storage" |
| Incident Type | Category of incident | "Data Leakage" |
| Severity | Impact level | "High" |
| Classification Affected | Data classification | "CONFIDENTIAL" |
| Description | What happened | "Sensitive file sent to wrong recipient" |
| Root Cause | Why it happened | "Auto-complete selected wrong address" |
| Corrective Action | Fix applied | "Enabled external recipient warning" |
| Status | Current state | "Closed" |
| Closed Date | When resolved | "17.01.2026" |
| Lessons Learned | Improvement identified | "Update training on email verification" |

**Incident Types**:
- Data Leakage
- Unauthorised Sharing
- Lost Device
- Interception
- Policy Violation
- Malware
- Unauthorised Access
- Other

**Incident Workflow**:
1. **Open**: Incident detected, investigation starting
2. **Investigating**: Root cause analysis in progress
3. **Remediation**: Fix being implemented
4. **Closed**: Resolved and documented
5. **Accepted**: Risk accepted (rare)

### Sheet 5: Audit_Findings

**Purpose**: Track audit findings related to transfer controls.

**For Each Finding, Document**:

| Column | Description | Example |
|--------|-------------|---------|
| Finding ID | Unique identifier | "AUD-TRF-001" |
| Audit Type | Source of finding | "Internal Audit", "ISO 27001" |
| Audit Date | When audit occurred | "10.01.2026" |
| Finding Description | What was found | "Email encryption not enforced for external" |
| Affected Control | Control area | "Electronic_Transfer" |
| Severity | Finding severity | "High" |
| Recommendation | Auditor's suggestion | "Enable mandatory TLS for external mail" |
| Owner | Accountable person | "Email Administrator" |
| Due Date | Target remediation date | "15.02.2026" |
| Status | Current state | "In Progress" |
| Closure Notes | Resolution details | "TLS enforcement enabled 01.02.2026" |

**Audit Types**:
- Internal Audit
- ISO 27001 Audit
- Penetration Test
- Vulnerability Assessment
- SOC 2 Audit
- GDPR Audit
- Customer Audit
- Other

**Finding Status**:
- **Open**: Not yet addressed
- **In Progress**: Remediation underway
- **Remediated**: Fix implemented
- **Verified Closed**: Fix tested and validated
- **Risk Accepted**: Management accepted residual risk
- **Overdue**: Past due date, not resolved

### Sheet 6: Remediation_Tracker

**Purpose**: Track all remediation activities to closure.

**For Each Remediation Item**:

| Column | Description | Example |
|--------|-------------|---------|
| Item ID | Unique identifier | "REM-001" |
| Source | Where gap identified | "Channel Assessment", "Audit Finding" |
| Gap/Finding Description | What needs fixing | "Missing MFA on SFTP accounts" |
| Priority | Urgency level | "High" |
| Remediation Plan | How to fix | "Enable MFA, migrate legacy accounts" |
| Owner | Accountable person | "Infrastructure Lead" |
| Start Date | When work began | "20.01.2026" |
| Target Date | Expected completion | "15.02.2026" |
| Status | Current state | "In Progress" |
| Progress Notes | Updates on work | "3 of 5 accounts migrated" |

**Source Types**:
- Channel Assessment
- Audit Finding
- Incident RCA (Root Cause Analysis)
- Risk Assessment
- Management Review
- Self-Assessment
- Other

**Status Options**:
- Not Started
- Planning
- In Progress
- Testing
- Completed
- On Hold
- Cancelled

### Sheet 7: Evidence_Register

**Purpose**: Track all dashboard supporting evidence.

**For Each Evidence Item**:

| Column | Action | Example |
|--------|--------|---------|
| Evidence ID | Unique identifier | "EV-514-CMD-001" |
| Evidence Type | Document category | "Report", "Metrics Export" |
| Description | What it demonstrates | "Monthly compliance dashboard report" |
| Related Item | Link to dashboard content | "Executive_Summary" |
| Location/Link | Where stored | "SharePoint/ISMS/Reports" |
| Date Collected | When gathered | "01.02.2026" |
| Collected By | Who gathered | "Security Analyst" |
| Status | Current status | "Verified" |

### Sheet 8: Approval_SignOff

**Purpose**: Monthly approval of dashboard accuracy.

**Complete**:
1. **Document Information**: Verify and update dates
2. **Reporting Period**: Specify month/quarter covered
3. **Approval Signatures**: Obtain monthly sign-offs

| Role | Responsibility |
|------|----------------|
| Dashboard Owner | Accuracy and completeness |
| IT Security Manager | Technical validation |
| Information Security Officer | Overall approval |
| CISO/Executive Sponsor | Management oversight |

4. **Distribution List**: Document who receives the dashboard

---

## Evidence Collection

### Evidence by Sheet

| Sheet | Required Evidence |
|-------|-------------------|
| Executive_Summary | Monthly dashboard PDF export |
| Compliance_KPIs | KPI calculation methodology, source data |
| Transfer_Incidents | Incident tickets, investigation reports |
| Audit_Findings | Audit reports, finding documentation |
| Remediation_Tracker | Remediation evidence, test results |

### Evidence Storage

Store all evidence in:
```
/ISMS/Evidence/A.5.14-Information-Transfer/
├── A.5.14.4-Monitoring/
│   ├── Dashboard-Reports/
│   ├── KPI-Data/
│   ├── Incident-Records/
│   ├── Audit-Findings/
│   └── Remediation-Evidence/
```

### Evidence Naming

Format: `EV-514-CMD-[Type]-[Period]-[YYYYMMDD].[ext]`

Examples:
- `EV-514-CMD-Dashboard-Jan2026-20260201.pdf`
- `EV-514-CMD-KPI-Export-Q1-20260331.xlsx`
- `EV-514-CMD-Incident-INC001-20260115.pdf`

---

## Common Pitfalls

### ❌ MISTAKE: Updating dashboard only before audits
✅ CORRECT: Maintain continuous updates per recommended frequency

### ❌ MISTAKE: Calculating KPIs without documented methodology
✅ CORRECT: Document how each KPI is calculated and where data comes from

### ❌ MISTAKE: Closing incidents without root cause analysis
✅ CORRECT: Always document root cause and lessons learned

### ❌ MISTAKE: Marking findings "Closed" without verification
✅ CORRECT: Require evidence of remediation before moving to "Verified Closed"

### ❌ MISTAKE: Not linking incidents to policy gaps
✅ CORRECT: Analyse incidents to identify rule or procedure improvements

### ❌ MISTAKE: Reporting raw numbers without context
✅ CORRECT: Include trend data and comparison to targets

### ❌ MISTAKE: Overdue remediation items not escalated
✅ CORRECT: Implement automatic escalation for items past due date

### ❌ MISTAKE: Missing executive summary for management
✅ CORRECT: Always complete Executive_Summary for reporting

### ❌ MISTAKE: Not tracking recurring incident patterns
✅ CORRECT: Analyse incidents for systemic issues requiring broader fixes

### ❌ MISTAKE: KPIs set to unachievable targets
✅ CORRECT: Set realistic targets, adjust based on baseline measurements

---

## Quality Checklist

Before submitting the dashboard, verify:

### Executive Summary
- [ ] Reporting period clearly stated
- [ ] All key metrics populated
- [ ] Domain compliance scores current
- [ ] Channel compliance counts accurate
- [ ] Key actions identified and assigned

### Compliance KPIs
- [ ] All KPIs have current values
- [ ] Status reflects actual vs target
- [ ] Trend direction documented
- [ ] Owners assigned
- [ ] Calculation methodology documented

### Incidents
- [ ] All open incidents have status
- [ ] Severity ratings appropriate
- [ ] Root cause documented for closed incidents
- [ ] Lessons learned captured
- [ ] Linked to remediation if needed

### Audit Findings
- [ ] All findings have owners
- [ ] Due dates are realistic
- [ ] Overdue items flagged
- [ ] Closure notes document evidence
- [ ] Status reflects actual state

### Remediation
- [ ] All gaps/findings tracked
- [ ] Priority reflects business impact
- [ ] Progress notes current
- [ ] Blocked items escalated
- [ ] Completed items have evidence

### Approval
- [ ] All approvals obtained
- [ ] Distribution list current
- [ ] Dashboard archived for records

---

## Review and Approval

### Update Schedule
- **Executive Summary**: Monthly (first week)
- **KPIs**: Monthly (end of month)
- **Incidents**: Real-time (within 24 hours)
- **Audit Findings**: After each audit
- **Remediation**: Weekly

### Approval Workflow
1. **Dashboard Owner** updates all sheets
2. **IT Security Manager** validates data
3. **ISO** reviews and approves
4. **Executive distribution** after approval

### Post-Approval Actions
- Distribute to stakeholder list
- Archive copy for audit trail
- Update risk register if needed
- Schedule next update cycle

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
