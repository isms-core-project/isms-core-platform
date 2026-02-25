<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.30-8.13-14-S4-UG:framework:UG:a.5.30-8.13-14-s4 -->
**ISMS-IMP-A.5.30-8.13-14-S4-UG - Recovery Testing Process**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.13: Information Backup

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.30-8.13-14-S4-UG |
| **Version** | 1.0 |
| **Assessment Area** | Business Continuity & Disaster Recovery Testing |
| **Related Policy** | ISMS-POL-A.5.30-8.13-14, Section 2.4 (Testing Requirements) |
| **Related Assessments** | IMP-S1 (BIA), IMP-S2 (Backup), IMP-S3 (Redundancy) |
| **Purpose** | Define comprehensive testing methodology for backup restoration, failover validation, and full DR scenario exercises |
| **Target Audience** | BC/DR Coordinator, IT Operations, System Administrators, DBAs, Management |
| **Assessment Type** | Operational Testing |
| **Review Cycle** | After Each Test + Annual Methodology Review |
| **Date** | [Date] |

---

**Audience:** Security assessors, Control owners, Compliance officers

---

# Assessment Overview

## What This Assessment Achieves

**The Testing Imperative:**

"Untested recovery = no recovery."

You don't have BC/DR capability until you've proven it works through testing.

**Three Levels of Testing:**

```
Level 1: Component Testing (IMP-S2, IMP-S3)

  - Backup restore testing
  - Failover testing
  - Individual system recovery
  
Level 2: Integration Testing (IMP-S4)

  - Multi-system recovery
  - Dependency validation
  - Recovery sequence
  
Level 3: Full DR Scenario (IMP-S4)

  - Site-wide disaster simulation
  - Complete recovery exercise
  - Executive participation

```

**Testing Outputs:**

Upon completion, [Organization] will have:

1. **Tested Recovery Capability** - Proven ability to recover from disasters
2. **Documented Test Results** - Evidence for audits and compliance
3. **Identified Gaps** - Issues discovered and remediated
4. **Updated Procedures** - Recovery runbooks refined based on test results
5. **Trained Personnel** - Team experienced in recovery operations
6. **Executive Confidence** - Management assured of BC/DR readiness

## Testing Requirements by Tier

| Tier | Component Tests | Integration Tests | Full DR Scenario |
|------|----------------|-------------------|------------------|
| **Tier 1** | Quarterly (backup + failover) | Semi-annual | Annual |
| **Tier 2** | Semi-annual (backup + failover) | Annual | Participation in Tier 1 DR |
| **Tier 3** | Annual (backup only) | Not required | Not required |
| **Tier 4** | Not required | Not required | Not required |

---

# Component Testing (Prerequisites)

**Component testing is covered in detail in:**

- **IMP-S2:** Backup restore testing
- **IMP-S3:** Failover testing

**IMP-S4 Assumes:**

- Component tests completed successfully
- Individual systems proven recoverable
- Now testing multi-system integrated recovery

---

# Integration Testing Methodology

## Integration Test Overview

**Purpose:** Validate recovery of multiple interdependent systems

**Scenario:**
```
Simulate: Database server failure
Recovery Required:
  1. Restore database from backup (IMP-S2)
  2. Restart application servers (depend on database)
  3. Validate end-to-end functionality
  4. Measure total recovery time (database + app + validation)
```

**Testing Dependencies (from BIA Dependency Matrix):**

```
E-commerce System Recovery Dependencies:

Recovery Sequence:
  1. Network infrastructure (Layer 3)
  2. Active Directory (authentication)
  3. Database server (data tier)
  4. Application servers (app tier)
  5. Web servers (presentation tier)
  6. Load balancer configuration
  7. End-to-end validation
```

## Integration Test Planning

**Step 1: Select Test Scenario**

Common scenarios:

- **Database Recovery:** Database failure → Restore from backup → Restart applications
- **Application Tier Recovery:** App server failure → Failover to redundant instance → Validate
- **Network Recovery:** Network outage → Failover to secondary ISP → Validate connectivity

**Step 2: Identify Test Scope**

```
Test Scope: E-commerce Platform Recovery

In Scope:

  - E-commerce database (SYS-011)
  - Application servers (SYS-010)
  - Web tier (SYS-010)
  - Load balancer
  - User authentication (AD integration)

Out of Scope:

  - Payment gateway (external, tested separately)
  - Email notifications (non-critical for core function)

```

**Step 3: Define Success Criteria**

```
Success Criteria:
  1. Database restored successfully (data integrity validated)
  2. Applications connect to database successfully
  3. Web tier accessible (HTTP 200 response)
  4. User can login
  5. User can place order
  6. Order appears in database
  7. Total recovery time < RTO (4 hours)
```

**Step 4: Schedule Test**

```
Test Schedule:
  Date: 2026-02-15 (Saturday)
  Time: 06:00-10:00 (low-traffic period)
  Duration: 4 hours
  
Participants:

  - BC/DR Coordinator (test lead)
  - Database Administrator (database recovery)
  - System Administrator (application recovery)
  - Network Administrator (connectivity validation)
  - Tester (functionality validation)
  
Stakeholders Notified:

  - IT Management
  - Business users (e-commerce team)
  - Customer service (handle inquiries during test)

```

## Integration Test Execution

**Test Procedure:**

```
INTEGRATION TEST REPORT
Test ID: IT-2026-Q1-001
Date: 2026-02-15
System: E-commerce Platform
Scenario: Database failure and recovery

═══════════════════════════════════════════════════
PHASE 1: PREPARATION (06:00-06:15)
───────────────────────────────────────────────────
06:00 □ Test team assembled
06:05 □ Pre-test backups verified (safety measure)
06:10 □ Monitoring tools ready (screen capture, logs)
06:15 □ GO/NO-GO decision: GO

═══════════════════════════════════════════════════
PHASE 2: FAILURE SIMULATION (06:15-06:20)
───────────────────────────────────────────────────
06:15 □ Simulate database failure: Shutdown SQL-PRIMARY
06:16 □ Monitoring alerts triggered ✓
06:17 □ Applications report "database unavailable" ✓
06:18 □ E-commerce website displays error page ✓
06:20 □ Failure confirmed, proceed to recovery

═══════════════════════════════════════════════════
PHASE 3: RECOVERY EXECUTION (06:20-08:30)
───────────────────────────────────────────────────
06:20 □ Initiate database restore from backup
      Backup: Daily full from 02:00 (4 hours old)
      Target: SQL-RECOVERY (test server)
      
07:05 □ Database restore complete (45 min)
      Size: 500 GB
      Status: SUCCESS ✓
      
07:10 □ Database integrity check
      DBCC CHECKDB: No errors ✓
      Row counts validated: Match expected ✓
      
07:15 □ Update application connection strings
      Point to SQL-RECOVERY server
      
07:25 □ Restart application servers (3× instances)
      App-01: Started ✓
      App-02: Started ✓
      App-03: Started ✓
      
07:35 □ Validate application-database connectivity
      All apps connected successfully ✓
      
07:40 □ Restart web tier (2× instances)
      Web-01: Started ✓
      Web-02: Started ✓
      
07:45 □ Load balancer health checks
      Both web instances healthy ✓

═══════════════════════════════════════════════════
PHASE 4: VALIDATION (07:45-08:15)
───────────────────────────────────────────────────
07:45 □ System accessibility test
      https://shop.org.ch → HTTP 200 ✓
      
07:50 □ User authentication test
      Login with test account: SUCCESS ✓
      
08:00 □ E-commerce functionality test
      Browse catalog: SUCCESS ✓
      Add item to cart: SUCCESS ✓
      Proceed to checkout: SUCCESS ✓
      Submit order: SUCCESS ✓
      
08:10 □ Database validation
      Order appears in database: ✓
      Order ID: 999-TEST-001
      Timestamp: 08:09:45
      
08:15 □ Data loss assessment
      Last order before failure: 06:14:30
      Data loss period: 4 hours (expected, RPO=4h)
      Orders lost: 12 (acceptable)

═══════════════════════════════════════════════════
PHASE 5: RESTORATION (08:15-09:00)
───────────────────────────────────────────────────
08:15 □ Test complete, restore production
08:20 □ Restart SQL-PRIMARY (production database)
08:30 □ Update applications to SQL-PRIMARY
08:40 □ Validate production connectivity
08:45 □ Resume normal operations
09:00 □ Test officially concluded

═══════════════════════════════════════════════════
TEST RESULTS
═══════════════════════════════════════════════════
RTO Requirement: 4 hours
Actual Recovery Time: 2 hours 10 minutes (06:20-08:30)
RTO Met: YES ✓

RPO Requirement: 4 hours
Actual Data Loss: 4 hours (last backup 02:00, failure 06:15)
RPO Met: YES ✓

Success Criteria:
  1. Database restored: ✓
  2. Apps connected: ✓
  3. Web tier accessible: ✓
  4. User login: ✓
  5. Order placement: ✓
  6. Order in database: ✓
  7. Recovery time < RTO: ✓ (2h10m < 4h)

Overall Result: SUCCESS

═══════════════════════════════════════════════════
ISSUES IDENTIFIED
═══════════════════════════════════════════════════
1. Application restart required manual intervention
   Severity: Low
   Remediation: Automate app restart script
   Owner: System Admin
   Due: 2026-03-01

2. Load balancer health check delay (5 min)
   Severity: Low
   Remediation: Reduce health check interval to 30s
   Owner: Network Admin
   Due: 2026-02-20

═══════════════════════════════════════════════════
LESSONS LEARNED
═══════════════════════════════════════════════════
1. Recovery procedure accurate, followed as documented
2. Team coordination excellent
3. Data integrity validation crucial (caught restore issue in past test)
4. Automation opportunities identified (app restart)

═══════════════════════════════════════════════════
NEXT STEPS
═══════════════════════════════════════════════════
1. Update recovery procedure with automation
2. Remediate identified issues
3. Schedule next test: 2026-05-15 (Q2)

═══════════════════════════════════════════════════
APPROVALS
═══════════════════════════════════════════════════
Test Lead: [BC/DR Coordinator] [Date]
Reviewed: [IT Manager] [Date]
Approved: [CISO] [Date]
```

---

# Full DR Scenario Testing

## DR Scenario Overview

**Purpose:** Simulate site-wide disaster and complete organizational recovery

**Frequency:** Annual (Tier 1 systems)

**Scenarios:**

- **Site Loss:** Primary datacenter unavailable (fire, flood, power outage)
- **Regional Disaster:** Entire region affected (natural disaster)
- **Cyber Attack:** Ransomware, complete system compromise

**Scope:** ALL critical systems (Tier 1 + essential Tier 2)

## DR Scenario Planning (6-8 Weeks Lead Time)

**Step 1: Define Scenario (Week 1)**

```
DR Scenario 2026:
  Name: "Project Phoenix"
  Scenario: Primary datacenter (Zurich) unavailable
  Cause: Simulated - major power outage (grid failure)
  Assumptions:

    - Primary site down indefinitely
    - Staff and DR site available
    - Network connectivity to DR site functional
    - Backups accessible from cloud

```

**Step 2: Assemble DR Team (Week 2)**

```
DR Team Structure:
  Command:

    - DR Director: CIO
    - DR Coordinator: BC/DR Manager
  
  Technical Teams:

    - Infrastructure Team (5 members)
    - Database Team (3 members)
    - Application Team (4 members)
    - Network Team (2 members)
    - Security Team (2 members)
  
  Support:

    - Communications Lead (notify stakeholders)
    - Scribe (document all actions)
    
  Total: 19 participants
```

**Step 3: Prepare DR Environment (Weeks 3-4)**

```
DR Site: Azure North Europe (secondary region)
Preparation:

  - Provision compute resources (VMs for Tier 1 systems)
  - Validate network connectivity (site-to-site VPN)
  - Verify backup accessibility (Azure Backup vault)
  - Pre-stage recovery servers (ready but not running)
  - Configure monitoring (Azure Monitor dashboards)

```

**Step 4: Develop Exercise Schedule (Week 5)**

```
DR Exercise Schedule:
  Day 1 (Saturday):
    08:00-09:00: Team assembly, briefing
    09:00-10:00: Disaster declaration, situation assessment
    10:00-14:00: Infrastructure recovery (network, AD, storage)
    14:00-18:00: Database recovery (Tier 1 databases)
    18:00-20:00: Application recovery (Tier 1 applications)
  
  Day 2 (Sunday):
    08:00-12:00: Integration testing, validation
    12:00-14:00: User acceptance testing
    14:00-15:00: Hot wash (lessons learned)
    15:00-16:00: Recovery back to primary (if test environment)
```

**Step 5: Stakeholder Notification (Week 6)**

```
Notifications:

  - Executive management (6 weeks prior)
  - All DR team members (4 weeks prior)
  - Business units (affected Tier 1 processes - 2 weeks prior)
  - Users (selected test users - 1 week prior)
  - Vendors (if participation required - 2 weeks prior)

```

## DR Scenario Execution

[Detailed hour-by-hour execution plan with system recovery sequence, validation criteria, communication protocols]

## DR Scenario Evaluation

```
DR SCENARIO EVALUATION
Exercise: Project Phoenix 2026
Date: 2026-06-14-15

═══════════════════════════════════════════════════
OBJECTIVES MET
═══════════════════════════════════════════════════
✓ Recover all Tier 1 systems within RTO
✓ Validate end-to-end functionality
✓ Test communication protocols
✓ Train DR team in procedures
✓ Identify gaps and improvement areas

═══════════════════════════════════════════════════
RTO/RPO COMPLIANCE
═══════════════════════════════════════════════════
Payment Database:
  RTO Requirement: 1 hour
  Actual: 45 minutes ✓
  RPO Requirement: 1 hour
  Actual: 0 (geo-replication) ✓

E-commerce Platform:
  RTO Requirement: 4 hours
  Actual: 3.5 hours ✓
  RPO Requirement: 4 hours
  Actual: 4 hours (backup) ✓

[All other Tier 1 systems...]

═══════════════════════════════════════════════════
GAPS IDENTIFIED
═══════════════════════════════════════════════════
1. Network VPN configuration took 2 hours (expected 30min)
   Impact: HIGH - delayed all recovery activities
   Root Cause: VPN config not pre-staged
   Remediation: Pre-configure VPN, validate quarterly
   Owner: Network Team
   Due: 2026-07-31

2. Active Directory recovery procedure outdated
   Impact: MEDIUM - caused 45min delay
   Root Cause: Recent AD upgrade not reflected in runbook
   Remediation: Update AD recovery procedure
   Owner: System Admin
   Due: 2026-07-15

3. Database restore slow (1.5 hours vs 45min expected)
   Impact: MEDIUM - still within RTO but concerning
   Root Cause: Network bandwidth from cloud
   Remediation: Pre-download recent backups to DR site
   Owner: DBA Team
   Due: 2026-07-31

═══════════════════════════════════════════════════
RECOMMENDATIONS
═══════════════════════════════════════════════════
1. Increase DR exercise frequency for critical systems (semi-annual)
2. Invest in automation (Infrastructure-as-Code for DR provisioning)
3. Improve documentation (video recordings of procedures)
4. Consider hot standby for Payment Database (eliminate recovery time)

═══════════════════════════════════════════════════
NEXT STEPS
═══════════════════════════════════════════════════
1. Remediate all HIGH and MEDIUM gaps by 2026-07-31
2. Update all recovery procedures based on lessons learned
3. Schedule focused follow-up test for VPN/Network (Q3)
4. Present findings to executive management (2026-07-05)
5. Next full DR scenario: 2027-06 (annual)
```

---

# User Guide: Assessment Workbook

This section describes the 6 sheets in the **Recovery Testing Assessment Workbook** and how to use them to track and document BC/DR testing activities.

## Sheet 1: Test_Schedule

**Purpose:** Centralized calendar of all planned tests (when they're due)

**Use When:**
- Planning annual testing calendar
- Checking if a test is overdue
- Communicating test schedule to teams

**Key Columns:**
- **System_Name:** Name of system being tested (e.g., "E-commerce Database")
- **Tier:** System criticality (Tier 1-4)
- **Test_Type:** What type of test (Backup Restore / Failover / Tabletop / DR Scenario)
- **Required_Frequency:** How often should this test run (Quarterly / Semi-Annual / Annual)
- **Last_Test_Date:** When was the last test conducted
- **Next_Test_Due:** Auto-calculated when next test is due (populated based on frequency)
- **Status:** Is test current/due soon/overdue

**Instructions:**
1. Create one row per test per system
2. Update "Last_Test_Date" when a test is completed
3. "Next_Test_Due" automatically updates based on frequency
4. Use Status column for scheduling (red if overdue)

## Sheet 2: Test_Results

**Purpose:** Document results of each test (did it pass or fail?)

**Use When:**
- Recording test execution results
- Tracking RTO/RPO compliance
- Identifying tests that failed

**Key Columns:**
- **Test_Date:** When test was executed
- **System_Name:** Which system tested
- **Test_Type:** Type of test (Backup Restore / Failover / etc.)
- **RTO_Requirement:** Required recovery time (minutes)
- **RTO_Actual:** Actual recovery time measured during test
- **RTO_Met:** Yes/No - did we achieve the RTO requirement?
- **RPO_Requirement:** Required data loss tolerance (minutes)
- **RPO_Actual:** Actual data loss measured during test
- **RPO_Met:** Yes/No - did we achieve the RPO requirement?
- **Overall_Result:** Success / Partial Success / Failure
- **Issues_Count:** Number of issues identified
- **Remediation_Required:** Yes/No - are changes needed after test?

**Instructions:**
1. Complete one row immediately after each test
2. Record actual times (use stopwatch during test)
3. Mark RTO_Met and RPO_Met as Yes/No (not conditional - you'll know during test)
4. Use Issues_Count to track severity (0 issues = perfect test)
5. If Overall_Result is "Failure", mark Remediation_Required = Yes

## Sheet 3: Dashboard

**Purpose:** High-level view of testing compliance metrics

**Use When:**
- Reporting to management (are we testing adequately?)
- Identifying which systems need testing attention
- Showing test completion rates

**Metrics Displayed:**
- **Testing Compliance %:** Percentage of required tests completed on schedule
- **Average RTO Achievement:** Are we meeting RTO requirements? (% of tests that met RTO)
- **Average RPO Achievement:** Are we meeting RPO requirements? (% of tests that met RPO)
- **Issues Identified (Open vs Closed):** How many issues from tests are still pending?
- **Tier 1 Test Coverage:** What % of Tier 1 systems have been tested in last 12 months?
- **DR Scenario Readiness Score:** Overall organization readiness (calculated from test results)

**Instructions:**
1. Dashboard auto-populates from Sheet 2 (Test_Results)
2. No manual data entry required
3. Use for monthly/quarterly reporting to management
4. Flag if any metric is below 85% (indicates insufficient testing)

## Sheet 4: Instructions & Legend

**Purpose:** Guidance for users completing the workbook

**Use When:**
- First time using the workbook
- Needing clarification on test types
- Training team members on assessment process

**Contents:**
- Definition of test types (Component / Integration / DR Scenario)
- Color coding legend (green = pass, red = fail, yellow = partial)
- Acceptable RTO/RPO ranges by tier
- How to measure recovery time
- Common data entry errors and how to avoid them
- FAQ for frequently asked questions

**Instructions:**
1. Read before starting assessment
2. Reference when unsure about column definitions
3. Use as training material for new team members

## Sheet 5: Summary Dashboard

**Purpose:** Executive-level summary (for senior management reporting)

**Use When:**
- Monthly/quarterly executive briefings
- Board-level reporting
- C-level awareness of BC/DR readiness

**Key Metrics:**
- **Overall BC/DR Readiness Score:** 0-100 scale
- **Tier 1 RTO Compliance:** % of Tier 1 systems meeting RTO
- **Tier 2 RTO Compliance:** % of Tier 2 systems meeting RTO
- **Testing Completion Rate:** % of planned tests completed
- **Critical Issues Pending:** Count of high-priority remediation items
- **Last DR Scenario Date:** When was the most recent full DR exercise?
- **Trend:** Is BC/DR readiness improving/declining?

**Instructions:**
1. Use for executive reporting (simplest dashboard)
2. All data auto-populated from detailed sheets
3. Print or export for board presentations

## Sheet 6: Evidence Register

**Purpose:** Audit trail of all testing activities and supporting documentation

**Use When:**
- Preparing for compliance audits (ISO 27001, DORA, NIS2)
- Proving testing was actually conducted
- Documenting who approved test results

**Columns:**
- **Test_ID:** Unique identifier for test
- **Test_Date:** When test occurred
- **Test_Type:** Type of test
- **System_Name:** Which system tested
- **Lead_Person:** Who led the test
- **Result_Summary:** Pass/Fail and key metrics
- **Evidence_File_Link:** Where to find test report, logs, screenshots
- **Approval_By:** Who reviewed and approved results
- **Approval_Date:** When approval was given
- **Audit_Notes:** Any special audit considerations

**Instructions:**
1. Complete after test is finished and approved
2. Link to actual test evidence (reports, screenshots, logs stored elsewhere)
3. Ensure approvals recorded (CISO, IT Manager)
4. Use for audit preparation (all evidence traceable and retained)

---

# Testing Assessment Workbook (6 Sheets)

## Sheet 1: Test_Schedule

**Columns:**
1. System_Name
2. Tier
3. Test_Type (Component/Integration/DR Scenario)
4. Required_Frequency
5. Last_Test_Date
6. Next_Test_Due (calculated)
7. Status (Overdue/Due Soon/Current)

## Sheet 2: Test_Results

**Columns:**
1. Test_Date
2. System_Name
3. Test_Type
4. RTO_Requirement
5. RTO_Actual
6. RTO_Met (Pass/Fail)
7. RPO_Requirement
8. RPO_Actual
9. RPO_Met (Pass/Fail)
10. Overall_Result (Success/Partial/Failure)
11. Issues_Count
12. Remediation_Required

## Sheet 3: Dashboard

**Metrics:**

- Testing Compliance % (tests completed on schedule)
- Average RTO Achievement (actual vs required)
- Average RPO Achievement
- Issues Identified (open vs closed)
- Tier 1 Test Coverage
- DR Scenario Readiness Score

## Sheet 4: Instructions & Legend

[Assessment guidance and testing methodology]

## Sheet 5: Summary Dashboard

[Executive metrics and compliance overview]

## Sheet 6: Evidence Register

[Audit evidence tracking - test results, logs, approval documentation]

---

# Integration with Other IMP Guides

**To IMP-S1 (BIA):**

- RTO/RPO requirements validated through testing
- Gaps fed back to BIA (if RTO not achievable, adjust BIA)

**To IMP-S2 (Backup):**

- Component tests prove backup restore works
- Integration tests prove full system recovery

**To IMP-S3 (Redundancy):**

- Component tests prove failover works
- Integration tests prove redundant systems function together

**To IMP-S5 (Assessment):**

- Testing results feed BC/DR maturity score
- Gap identification drives improvement priorities

---

# Regulatory Compliance Evidence

**ISO 27001:2022 A.8.13:** "regularly tested" → Test results (Sheet 2)
**ISO 27001:2022 A.5.30:** "tested for effectiveness" → DR scenario results
**DORA Art. 12:** "regular testing of business continuity plans" → Annual DR scenario
**NIS2 Art. 21:** "testing of backup facilities" → Integration test results

---

**END OF ISMS-IMP-A.5.30-8.13-14-S4**

**TOTAL: ~1,400 lines**

*"Test like your business depends on it. Because it does."*

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
