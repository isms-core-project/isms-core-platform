<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.15-16-18.S5-UG:framework:UG:a.5.15-16-18 -->
**ISMS-IMP-A.5.15-16-18.S5-UG - Lifecycle Compliance Detailed Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.16: Identity Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S5-UG |
| **Version** | 1.0 |
| **Assessment Area** | Lifecycle Compliance Detailed Assessment - Joiner/Mover/Leaver Analysis |
| **Related Policy** | ISMS-POL-A.5.15-16-18 (All Sections) |
| **Purpose** | Detailed analysis of identity lifecycle compliance across joiner/mover/leaver events with SLA tracking and HR integration status |
| **Target Audience** | IAM Team, HR Operations, IT Operations, Security Operations, Internal Audit |
| **Assessment Type** | Lifecycle Event Analysis |
| **Review Cycle** | Monthly (Lifecycle Review), Quarterly (Process Review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Lifecycle Compliance Detailed Assessment | ISMS Implementation Team |

---

## Assessment Overview

### Purpose & Scope

This workbook provides detailed analysis of identity lifecycle compliance across all joiner/mover/leaver events, enabling:

- **Joiner Event Analysis**: Track new hire provisioning against SLA (days to provision)
- **Mover Event Analysis**: Track role changes and transfers with access modification timeliness
- **Leaver Event Analysis**: Track termination deprovisioning (critical security - hours to disable)
- **Contractor Lifecycle**: Track time-bound contractor access and contract expiration
- **Orphaned Account Remediation**: Track detection and remediation of orphaned accounts
- **HR Integration Status**: Document automation level of lifecycle processes

### Assessment Scope

This workbook tracks detailed lifecycle events from:

| Event Type | Data Source | Key Metrics |
|------------|-------------|-------------|
| **Joiners** | HR hire data + Identity system logs | Days to provision, SLA compliance |
| **Movers** | HR transfer data + Access change logs | Days to update access, change type |
| **Leavers** | HR termination data + Account disable logs | Hours to disable, security risk |
| **Contractors** | Contractor management system | Contract dates, expiration status |
| **Orphaned Accounts** | Identity system scans | Detection date, remediation status |

### Key Outputs

Upon completion, you will have:

1. **Joiner Events Log**: Complete provisioning compliance for new hires
2. **Mover Events Log**: Role change and transfer processing timeliness
3. **Leaver Events Log**: Termination deprovisioning compliance (security-critical)
4. **Contractor Lifecycle**: Time-bound access tracking and expiration management
5. **Orphaned Account Tracking**: Detection and remediation status
6. **Timeliness Metrics**: SLA compliance summary across all lifecycle events
7. **HR Integration Status**: Automation coverage and integration health
8. **Gap Analysis**: Process gaps with remediation plans
9. **Evidence Register**: Audit-ready evidence for A.5.16 compliance

---

## Prerequisites

### Data Sources Required

Before starting this assessment, you must have access to:

1. **HR System Data**

   - Employee hire dates (start dates)
   - Employee termination dates (last day)
   - Role changes and department transfers (effective dates)
   - Contractor contract start and end dates

2. **Identity Management System Logs**

   - Account creation timestamps
   - Account modification timestamps
   - Account disable/delete timestamps
   - Last login dates

3. **Service Desk / Ticketing System** (Optional)

   - Provisioning request tickets
   - Access change request tickets
   - Deprovisioning request tickets

4. **Contractor Management System**

   - Active contractor list
   - Contract dates and sponsor information

### File Organization

**Recommended folder structure**:
```
SharePoint/IAM_Assessments/2025-10/
├── ISMS-IMP-A.5.15-16-18.S5_Lifecycle_Compliance_Detailed_20251015.xlsx (this file)
├── HR_Export_Joiners_202510.csv
├── HR_Export_Leavers_202510.csv
├── Identity_System_Provisioning_Log_202510.csv
└── Contractor_Active_List_202510.xlsx
```

Store source data exports alongside the completed workbook for audit traceability.

### Time Commitment

- **Initial data collection**: 2-3 hours (export HR data, identity logs)
- **Joiner/Mover/Leaver analysis**: 3-4 hours (correlate events, calculate timeliness)
- **Contractor and orphaned account review**: 1-2 hours
- **Gap analysis and evidence collection**: 1-2 hours
- **Monthly refresh**: 2-3 hours (new events, updated metrics)

---

## Workflow

### Assessment Flow

```
1. COLLECT HR DATA (Joiners, Movers, Leavers)
   ↓
2. COLLECT IDENTITY SYSTEM LOGS (Account events)
   ↓
3. CORRELATE EVENTS (Match HR dates to identity events)
   ↓
4. POPULATE JOINER EVENTS (Sheet 2)
   ↓
5. POPULATE MOVER EVENTS (Sheet 3)
   ↓
6. POPULATE LEAVER EVENTS (Sheet 4)
   ↓
7. REVIEW CONTRACTOR LIFECYCLE (Sheet 5)
   ↓
8. TRACK ORPHANED ACCOUNTS (Sheet 6)
   ↓
9. CALCULATE METRICS (Sheet 7)
   ↓
10. DOCUMENT HR INTEGRATION (Sheet 8)
   ↓
11. ANALYZE GAPS (Sheet 9)
   ↓
12. COLLECT EVIDENCE (Sheet 10)
```

### Phase 1: Data Collection (2-3 hours)

**Objective**: Gather lifecycle event data from HR and identity systems

**Steps**:
1. Export new hire data from HR system (assessment period)
   - Fields: Employee ID, Name, Department, Hire Date, Job Title
2. Export termination data from HR system
   - Fields: Employee ID, Name, Termination Date, Last Day
3. Export role changes and transfers from HR system
   - Fields: Employee ID, Change Type, Effective Date, From/To Department
4. Export account provisioning logs from identity system
   - Fields: User ID, Username, Account Created Date
5. Export account disable/delete logs from identity system
   - Fields: User ID, Username, Account Disabled Date/Time
6. Export contractor list with contract dates
7. Export orphaned account scan results (if available)

**Deliverable**: Source data files ready for analysis

**Quality Check**:
- All exports cover the assessment period
- Data formats are consistent (dates, IDs)
- No missing critical fields

### Phase 2: Joiner Event Analysis (1-2 hours)

**Objective**: Document provisioning timeliness for new hires

**Steps**:
1. Open **Sheet 2** (Joiner_Events)
2. For each new hire in HR export:
   - Create Event ID (JOIN-XXXX)
   - Enter User ID, Username, Full Name, Department, Job Title
   - Enter Hire Date (from HR)
   - Find corresponding account creation in identity logs
   - Enter Provision Date (account created date)
   - Calculate Days to Provision (Provision Date - Hire Date)
   - Compare against SLA (typically 0-2 days before hire)
   - Mark Compliance status
3. Add notes for any non-compliant events

**Deliverable**: Complete joiner events log with compliance status

**Quality Check**:
- All new hires in period are documented
- Each event matched to identity system record
- Compliance calculated correctly

### Phase 3: Mover Event Analysis (1-2 hours)

**Objective**: Document access modification timeliness for role changes

**Steps**:
1. Open **Sheet 3** (Mover_Events)
2. For each role change/transfer in HR export:
   - Create Event ID (MOVE-XXXX)
   - Enter User ID, Username, Full Name
   - Enter Change Type (Department Transfer, Promotion, Role Change)
   - Enter From/To Department
   - Enter Effective Date (from HR)
   - Find corresponding access change in logs
   - Enter Access Updated Date
   - Calculate Days to Update
   - Compare against SLA (typically 3 days)
   - Mark Compliance status
3. Add notes for delayed events

**Deliverable**: Complete mover events log with compliance status

**Quality Check**:
- All role changes in period are documented
- Access modifications matched to HR events
- Delayed events explained in notes

### Phase 4: Leaver Event Analysis (1-2 hours)

**Objective**: Document deprovisioning timeliness (critical security)

**Steps**:
1. Open **Sheet 4** (Leaver_Events)
2. For each termination in HR export:
   - Create Event ID (LEAVE-XXXX)
   - Enter User ID, Username, Full Name, Department
   - Enter Termination Date (from HR)
   - Find corresponding account disable in identity logs
   - Enter Account Disabled Date/Time
   - Calculate Hours to Disable
   - Compare against SLA (typically 24 hours)
   - Mark Compliance status
   - Flag Security Risk if non-compliant
3. Add detailed notes for non-compliant events (security exposure)

**Deliverable**: Complete leaver events log with security risk flags

**Quality Check**:
- All terminations in period are documented
- Account disable matched to termination date
- **CRITICAL**: Any security risks flagged and escalated

### Phase 5: Contractor Lifecycle Review (30-60 minutes)

**Objective**: Track contractor access against contract dates

**Steps**:
1. Open **Sheet 5** (Contractor_Lifecycle)
2. Import active contractor list
3. For each contractor:
   - Verify contract start and end dates
   - Calculate Days Remaining
   - Determine Expiration Status (Active, Expiring Soon, EXPIRED)
   - Check for extension approval if expiring
   - Mark Compliance status
4. Flag any expired contractors still with active access

**Deliverable**: Complete contractor lifecycle tracking

**Quality Check**:
- All active contractors documented
- Expired contractors flagged
- Extensions tracked where applicable

### Phase 6: Orphaned Account Remediation (30-60 minutes)

**Objective**: Track detection and remediation of orphaned accounts

**Steps**:
1. Open **Sheet 6** (Orphaned_Remediation)
2. Import orphaned account scan results
3. For each orphaned account:
   - Document detection date and reason
   - Assign to responsible team
   - Determine remediation action
   - Track completion status
4. Update status for previously identified accounts

**Deliverable**: Complete orphaned account tracking

**Quality Check**:
- All detected orphaned accounts documented
- Remediation assigned and tracked
- Pending accounts have clear action plans

### Phase 7: Calculate Timeliness Metrics (15 minutes)

**Objective**: Summarize SLA compliance across lifecycle events

**Steps**:
1. Open **Sheet 7** (Timeliness_Metrics)
2. Calculate from event sheets:
   - Joiner On-Time Provisioning % (from Sheet 2)
   - Leaver On-Time Deprovisioning % (from Sheet 4)
   - Mover Access Update % (from Sheet 3)
   - Contractor Expiration Compliance % (from Sheet 5)
   - Orphaned Account Remediation % (from Sheet 6)
3. Compare against targets
4. Document gaps and comments

**Deliverable**: Metrics summary with target comparison

### Phase 8: Document HR Integration (15 minutes)

**Objective**: Document automation status of lifecycle processes

**Steps**:
1. Open **Sheet 8** (HR_Integration)
2. For each integration component:
   - Document current status (Active, Partial, Not Implemented)
   - Record integration method (API, CSV, Manual)
   - Note frequency and last sync
   - Identify any issues or gaps

**Deliverable**: HR integration status documentation

### Phase 9: Gap Analysis (30 minutes)

**Objective**: Document process gaps and remediation plans

**Steps**:
1. Open **Sheet 9** (Gap_Analysis)
2. Review findings from all sheets
3. For each identified gap:
   - Create Gap ID
   - Categorize (Provisioning, Deprovisioning, etc.)
   - Describe the gap and root cause
   - Assign risk level
   - Define remediation plan
   - Assign owner and due date
4. Update status for existing gaps

**Deliverable**: Gap analysis with remediation tracking

### Phase 10: Evidence Collection (30 minutes)

**Objective**: Document evidence for A.5.16 compliance

**Steps**:
1. Open **Sheet 10** (Evidence_Register)
2. For each lifecycle process area:
   - Reference evidence (this workbook sheets, source exports)
   - Record collection date
   - Verify completeness
   - Note reviewer
3. Ensure all A.5.16 requirements have supporting evidence

**Deliverable**: Complete evidence register for audit

---

## Completing Each Sheet

### Sheet 1: Instructions and Legend

**Purpose**: Document control, how to use workbook, SLA definitions

**Key Sections**:
1. **Document Control**: Workbook ID, version, assessment period, prepared by
2. **Workbook Overview**: Purpose, scope, how to use
3. **SLA Definitions**: Provisioning SLA (days), Deprovisioning SLA (hours), Mover SLA (days)
4. **Status Legends**: Compliant, Non-Compliant, Warning indicators
5. **Evidence Collection**: How to link evidence for audit

### Sheet 2: Joiner_Events

**Purpose**: Track new hire provisioning compliance against SLA

**How to Complete**:
1. Export new hire data from HR system for assessment period
2. For each new hire, create a row:
   - **Event ID**: Sequential identifier (JOIN-1001, JOIN-1002, ...)
   - **User ID**: From identity system
   - **Username**: Account login name
   - **Full Name**: Employee name
   - **Department**: Assigned department
   - **Job Title**: Position
   - **Hire Date**: From HR (official start date)
   - **Provision Date**: From identity system (account created date)
   - **Days to Provision**: Calculate (Provision Date - Hire Date)
   - **SLA**: Your provisioning SLA (e.g., 0 = same day)
   - **Compliance**: Compliant if Days to Provision ≤ SLA
   - **Notes**: Explain any non-compliant events

**Quality Check**:
- ✓ All new hires in assessment period documented
- ✓ Each hire matched to identity system record
- ✓ Days to Provision calculated correctly
- ✓ Non-compliant events have notes explaining delay

### Sheet 3: Mover_Events

**Purpose**: Track role change and transfer processing timeliness

**How to Complete**:
1. Export role changes and transfers from HR system
2. For each change, create a row:
   - **Event ID**: Sequential identifier (MOVE-1001, MOVE-1002, ...)
   - **User ID**: User account identifier
   - **Username**: Account login name
   - **Full Name**: Employee name
   - **Change Type**: Department Transfer, Promotion, Role Change, Team Reassignment
   - **From Dept**: Previous department
   - **To Dept**: New department
   - **Effective Date**: From HR (when change took effect)
   - **Access Updated**: From identity system (when access was modified)
   - **Days to Update**: Calculate (Access Updated - Effective Date)
   - **Compliance**: Compliant if Days to Update ≤ SLA (typically 3 days)
   - **Notes**: Explain any delayed events

**Quality Check**:
- ✓ All role changes in assessment period documented
- ✓ Access modifications matched to HR events
- ✓ Delayed events have explanation

### Sheet 4: Leaver_Events

**Purpose**: Track termination deprovisioning compliance (critical security)

**How to Complete**:
1. Export termination data from HR system
2. For each termination, create a row:
   - **Event ID**: Sequential identifier (LEAVE-1001, LEAVE-1002, ...)
   - **User ID**: User account identifier
   - **Username**: Account login name
   - **Full Name**: Employee name
   - **Department**: Employee's department
   - **Termination Date**: From HR (last day of employment)
   - **Account Disabled**: From identity system (date/time account was disabled)
   - **Hours to Disable**: Calculate in hours
   - **SLA**: Your deprovisioning SLA (typically 24 hours)
   - **Compliance**: Compliant if Hours to Disable ≤ SLA
   - **Security Risk**: YES if non-compliant (terminated user retained access)
   - **Notes**: **CRITICAL** - Document security exposure for non-compliant events

**Quality Check**:
- ✓ All terminations in assessment period documented
- ✓ Account disable matched to termination date
- ✓ **Security risks flagged and escalated immediately**
- ✓ Non-compliant events have detailed notes

**Security Note**: Late deprovisioning is a critical security risk. Any terminated employee with active access can cause data exfiltration, sabotage, or compliance violations. Non-compliant events should be escalated immediately.

### Sheet 5: Contractor_Lifecycle

**Purpose**: Track time-bound contractor access and contract expiration

**How to Complete**:
1. Export active contractor list
2. For each contractor, create a row:
   - **Contractor ID**: Unique identifier
   - **Username**: Contractor login name
   - **Full Name**: Contractor name
   - **Sponsor**: Business sponsor (manager responsible)
   - **Department**: Department contractor works with
   - **Contract Start**: Contract start date
   - **Contract End**: Contract end date
   - **Days Remaining**: Calculate (Contract End - Today)
   - **Expiration Status**: Active (>30 days), Expiring Soon (1-30 days), EXPIRED (<0)
   - **Extension Approved**: Approved, Pending, Not Requested, N/A
   - **Compliance**: Based on status and extension

**Quality Check**:
- ✓ All active contractors documented
- ✓ Contract dates verified
- ✓ Expired contractors flagged
- ✓ Expiring contractors have extension status

### Sheet 6: Orphaned_Remediation

**Purpose**: Track orphaned account detection and remediation

**How to Complete**:
1. Import orphaned account scan results
2. For each orphaned account, create a row:
   - **Account ID**: User account identifier
   - **Username**: Account login name
   - **Account Type**: Employee, Contractor, Service Account
   - **Last Login**: Last successful login date
   - **Detection Date**: When orphaned status was detected
   - **Orphan Reason**: Why account is orphaned
   - **Assigned To**: Team responsible for remediation
   - **Remediation Action**: Disable, Delete, Reassign owner, Document exception
   - **Completion Date**: When remediation completed (if done)
   - **Days to Remediate**: Calculate if completed
   - **Status**: Remediated, Pending

**Orphan Reasons**:
- No login for 120+ days
- User terminated but account not disabled
- No valid business owner
- Contractor contract ended, account still active

**Quality Check**:
- ✓ All detected orphaned accounts documented
- ✓ Remediation action assigned
- ✓ Pending accounts have clear timeline

### Sheet 7: Timeliness_Metrics

**Purpose**: Summary of lifecycle SLA compliance metrics

**How to Complete**:
1. Calculate metrics from event sheets:
   - **Joiner On-Time Provisioning**: COUNTIF(Joiner Compliance = "Compliant") / Total Joiners
   - **Leaver On-Time Deprovisioning**: COUNTIF(Leaver Compliance = "Compliant") / Total Leavers
   - **Mover Access Update**: COUNTIF(Mover Compliance = "Compliant") / Total Movers
   - **Contractor Expiration Compliance**: COUNTIF(Contractor Status ≠ "EXPIRED") / Total Contractors
   - **Orphaned Account Remediation**: COUNTIF(Orphan Status = "Remediated") / Total Orphaned
2. Compare against targets
3. Determine status (Compliant, Warning, Non-Compliant)
4. Document gap and comments

**Quality Check**:
- ✓ Metrics calculated correctly
- ✓ Targets reflect organizational policy
- ✓ Gaps identified with context

### Sheet 8: HR_Integration

**Purpose**: Document HR system integration status

**How to Complete**:
1. For each integration component:
   - **Component**: Employee Data Feed, Termination Feed, Transfer Feed, Contractor Feed, etc.
   - **Status**: Active, Partial, Not Implemented
   - **Integration Method**: API, CSV Import, Manual, N/A
   - **Frequency**: Real-time, Daily, Weekly, N/A
   - **Last Sync**: Last successful synchronization
   - **Issues**: Current issues or blockers
   - **Notes**: Additional context

**Quality Check**:
- ✓ All integration components documented
- ✓ Status reflects current state
- ✓ Issues identified for improvement planning

### Sheet 9: Gap_Analysis

**Purpose**: Document lifecycle process gaps and remediation plans

**How to Complete**:
1. Review findings from all sheets
2. For each gap, create a row:
   - **Gap ID**: Sequential identifier (GAP-001, GAP-002, ...)
   - **Category**: Provisioning, Deprovisioning, Orphaned Accounts, Contractor Management
   - **Description**: What is the gap?
   - **Risk Level**: High, Medium, Low
   - **Affected Items**: Count or scope of impact
   - **Root Cause**: Why did this happen?
   - **Remediation Plan**: What action will fix this?
   - **Owner**: Who is responsible?
   - **Due Date**: Target resolution date
   - **Status**: Open, In Progress, Planned, Closed

**Quality Check**:
- ✓ All significant gaps documented
- ✓ Root causes identified (not just symptoms)
- ✓ Remediation plans are actionable
- ✓ Owners assigned and accountable

### Sheet 10: Evidence_Register

**Purpose**: Evidence collection for A.5.16 Identity Management compliance

**How to Complete**:
1. For each lifecycle process area, document evidence:
   - **Evidence ID**: Sequential identifier (EV-001, EV-002, ...)
   - **Requirement**: A.5.16 requirement area (Joiner Process, Leaver Process, etc.)
   - **Evidence Type**: Event Log, Report, Configuration, Screenshot
   - **Evidence Location**: Sheet reference, file path, URL
   - **Collection Date**: When evidence was collected
   - **Completeness**: Complete, Partial, Missing
   - **Reviewed By**: Who verified the evidence
   - **Notes**: Additional context

**Standard Evidence Items**:
- Joiner events log (Sheet 2)
- Mover events log (Sheet 3)
- Leaver events log (Sheet 4)
- Contractor lifecycle tracking (Sheet 5)
- Orphaned account remediation (Sheet 6)
- Timeliness metrics (Sheet 7)
- HR integration status (Sheet 8)
- Source data exports (HR, identity system)

**Quality Check**:
- ✓ All A.5.16 requirements have supporting evidence
- ✓ Evidence is current (within assessment period)
- ✓ Evidence locations are accessible for audit

---

## Common Pitfalls & Solutions

### Pitfall 1: Missing HR Data

**Problem**: Cannot correlate identity events to HR events because HR data is incomplete or unavailable.

**Solution**:
1. Establish data sharing agreement with HR
2. Define minimum required fields (Employee ID, dates, department)
3. Schedule regular exports (weekly or monthly)
4. Create mapping table for HR ID to identity system ID

### Pitfall 2: Timestamp Mismatches

**Problem**: HR dates and identity system dates don't align due to timezone or format differences.

**Solution**:
1. Standardize on UTC or local timezone
2. Document date format in Instructions sheet
3. When correlating events, allow 1-day tolerance for date matching
4. For leavers, use hour-level precision

### Pitfall 3: Orphaned Accounts Undetected

**Problem**: Orphaned accounts not found because no regular scanning process exists.

**Solution**:
1. Implement monthly orphaned account scan
2. Define orphan criteria (no login 90+ days, no owner, terminated employee)
3. Automate scan reports from identity system
4. Add scan schedule to evidence register

### Pitfall 4: Manual Processes Causing Delays

**Problem**: High non-compliance rate because lifecycle processes are manual.

**Solution**:
1. Document manual processes in HR_Integration sheet
2. Identify automation opportunities
3. Create gap with remediation plan to automate
4. Track automation progress month-over-month

### Pitfall 5: Contractor Contract Dates Not Maintained

**Problem**: Contractor accounts show as "expired" but contract was extended, just not updated.

**Solution**:
1. Implement contract extension workflow
2. Require documented approval for extensions
3. Update contractor system before contract end date
4. Send automated reminders 30 days before expiration

### Pitfall 6: Security Risks Not Escalated

**Problem**: Late deprovisioning events documented but not escalated as security incidents.

**Solution**:
1. Any leaver with account active 24+ hours post-termination = Security Incident
2. Escalate to Security Operations immediately
3. Document in incident management system
4. Add to Gap Analysis as critical priority

### Pitfall 7: Incomplete Evidence

**Problem**: Audit requests evidence but source data exports are not retained.

**Solution**:
1. Retain all source data exports (HR, identity logs) with assessment
2. Store in same folder as completed workbook
3. Include file names in Evidence Register
4. Define retention period (3 years typical)

---

## Quality Checklist

### Prerequisites

- [ ] HR system data export obtained (joiners, movers, leavers)
- [ ] Identity system logs exported (account events)
- [ ] Contractor list with contract dates available
- [ ] Orphaned account scan results available (if scan exists)
- [ ] Data formats documented and consistent

### Sheet 2: Joiner_Events

- [ ] All new hires in assessment period documented
- [ ] Each hire matched to identity system record
- [ ] Days to Provision calculated correctly
- [ ] SLA threshold documented
- [ ] Compliance status assigned
- [ ] Non-compliant events have explanatory notes

### Sheet 3: Mover_Events

- [ ] All role changes in assessment period documented
- [ ] Change type categorized correctly
- [ ] From/To departments recorded
- [ ] Days to Update calculated correctly
- [ ] Compliance status assigned
- [ ] Delayed events have explanation

### Sheet 4: Leaver_Events

- [ ] All terminations in assessment period documented
- [ ] Hours to Disable calculated correctly (not days)
- [ ] SLA threshold documented (hours)
- [ ] Compliance status assigned
- [ ] **Security Risk flagged for non-compliant events**
- [ ] Non-compliant events have detailed notes
- [ ] Security risks escalated appropriately

### Sheet 5: Contractor_Lifecycle

- [ ] All active contractors documented
- [ ] Contract dates verified
- [ ] Days Remaining calculated
- [ ] Expiration Status assigned
- [ ] Extension status tracked where applicable
- [ ] Expired contractors flagged for remediation

### Sheet 6: Orphaned_Remediation

- [ ] All detected orphaned accounts documented
- [ ] Orphan reason documented
- [ ] Remediation action assigned
- [ ] Responsible team assigned
- [ ] Completion tracked for remediated accounts
- [ ] Pending accounts have timeline

### Sheet 7: Timeliness_Metrics

- [ ] All metrics calculated from event sheets
- [ ] Targets reflect organizational policy
- [ ] Status (Compliant/Warning/Non-Compliant) assigned
- [ ] Gaps identified with context

### Sheet 8: HR_Integration

- [ ] All integration components documented
- [ ] Status reflects current state
- [ ] Integration method documented
- [ ] Issues identified for improvement

### Sheet 9: Gap_Analysis

- [ ] All significant gaps documented
- [ ] Risk level assigned
- [ ] Root cause identified
- [ ] Remediation plan defined
- [ ] Owner assigned
- [ ] Due date set
- [ ] Status tracked

### Sheet 10: Evidence_Register

- [ ] All A.5.16 requirements have supporting evidence
- [ ] Evidence locations are specific and accessible
- [ ] Collection dates are current
- [ ] Completeness assessed (Complete/Partial/Missing)
- [ ] Reviewer documented

### General Quality

- [ ] All data from assessment period (not stale)
- [ ] Calculations verified (spot check)
- [ ] Conditional formatting displays correctly
- [ ] File naming follows standard (ISMS-IMP-A.5.15-16-18.5_Lifecycle_Compliance_Detailed_YYYYMMDD.xlsx)
- [ ] Source data exports retained with assessment

---

## Continuous Improvement

### Monthly Assessment Refresh

**Frequency**: Monthly (or after significant lifecycle events)

**Tasks**:
1. Export latest HR data (joiners, movers, leavers for period)
2. Export latest identity system logs
3. Add new events to appropriate sheets
4. Update metrics calculations
5. Review and update gap status
6. Collect new evidence
7. Save workbook with date suffix

**Output**: Updated lifecycle compliance assessment

---

### Quarterly Process Review

**Frequency**: Quarterly

**Tasks**:
1. Analyze trends in lifecycle compliance
2. Review HR integration effectiveness
3. Assess automation progress
4. Update gap remediation plans
5. Present findings to IAM governance committee

---

## Integration with Other ISMS Controls

### Upstream Dependencies

**This assessment relies on data from**:

- **HR System**: Authoritative source for employee lifecycle data
- **Identity Management System**: Account provisioning and deprovisioning logs
- **Contractor Management**: Contract dates and sponsor information

### Downstream Dependencies

**This assessment feeds into**:

- **S1 (User Inventory)**: Validates user lifecycle compliance metrics
- **S3 (Access Review)**: Identifies users requiring review due to role changes
- **IAM Governance**: Lifecycle compliance contributes to overall IAM maturity

### Integration Benefits

This lifecycle compliance assessment provides:

- **Internal Audit**: Evidence of A.5.16 compliance
- **Risk Management**: Identification of security risks (late deprovisioning)
- **Process Improvement**: Data for HR integration automation decisions
- **Compliance**: Evidence for regulatory requirements

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
