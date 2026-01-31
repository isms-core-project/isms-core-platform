# ISMS-IMP-A.8.13-14-5.30-S4: Recovery Testing Process

**Document Classification:** Internal - ISMS Implementation Guide  
**Version:** 1.0  
**Target Audience:** BC/DR Coordinator, Test Coordinators, IT Operations, Business Process Owners  
**Prerequisites:** Backup implemented (IMP-S2), Redundancy implemented (IMP-S3 if applicable)  
**Estimated Effort:** Ongoing (testing is continuous, not one-time)

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | BC/DR Coordinator | Initial recovery testing process guide |

---

## Table of Contents

1. [Overview](#1-overview)
2. [Testing Strategy Development](#2-testing-strategy-development)
3. [Test Planning and Scheduling](#3-test-planning-and-scheduling)
4. [Backup Restore Testing Procedures](#4-backup-restore-testing-procedures)
5. [Failover Testing Procedures](#5-failover-testing-procedures)
6. [DR Scenario Testing](#6-dr-scenario-testing)
7. [Testing Without Production Impact](#7-testing-without-production-impact)
8. [Test Documentation and Evidence](#8-test-documentation-and-evidence)
9. [Post-Test Review and Remediation](#9-post-test-review-and-remediation)
10. [Continuous Testing Integration](#10-continuous-testing-integration)
11. [Common Pitfalls and How to Avoid](#11-common-pitfalls-and-how-to-avoid)
12. [Verification and Sign-Off](#12-verification-and-sign-off)

---

## 1. Overview

### 1.1 Purpose

This implementation guide provides step-by-step instructions for planning, executing, and documenting BC/DR testing to verify that backup, redundancy, and recovery capabilities actually work.

**Critical Principle:** "Plans are worthless, but planning is everything." Testing transforms plans from theory into proven capability.

### 1.2 Relationship to Policy

This guide implements:
- **Policy S5:** Testing Methodology and Evidence Framework
- **Annex-B** Section 5: Testing Checklists
- **Policy S2:** Backup testing requirements (A.8.13)
- **Policy S3:** Failover testing requirements (A.8.14)
- **Policy S4:** ICT BC testing requirements (A.5.30)

### 1.3 Expected Outcomes

Upon completion of testing program, [Organization] will have:
- Documented testing strategy (types, frequency, scope)
- Testing schedule (annual calendar of all tests)
- Tested recovery procedures (verified they work)
- Measured actual RTO/RPO (not assumptions)
- Documented test results (evidence for audit)
- Remediated test failures (gaps closed)
- Continuous testing culture (testing is normal, not exceptional)

---

## 2. Testing Strategy Development

### 2.1 Define Testing Approach

**Step 1: Establish Testing Philosophy**

[Organization]'s testing philosophy (from Policy S5):
- **Untested recovery = No recovery**
- Failed tests are successes (reveal gaps before real disaster)
- Testing is mandatory, not optional
- Multiple test types balance risk, cost, and thoroughness

**Step 2: Define Test Types and Purposes**

| Test Type | Purpose | Risk to Production | Cost | Value | Frequency |
|-----------|---------|-------------------|------|-------|-----------|
| **File Restore Test** | Verify can restore individual files | Very Low | Low | Medium | Monthly |
| **System Restore Test** | Verify can restore complete system | Low | Medium | High | Quarterly |
| **Failover Test** | Verify redundancy works | Low-Medium | Medium | High | Quarterly |
| **Tabletop Exercise** | Walkthrough of DR procedures (discussion) | None | Very Low | Medium | Quarterly |
| **DR Simulation** | Full scenario test (end-to-end) | Medium | High | Very High | Annual |

**Step 3: Map Tests to Systems by Criticality**

| System Criticality | File Restore | System Restore | Failover | Tabletop | DR Simulation |
|-------------------|--------------|----------------|----------|----------|---------------|
| **Critical (Tier 1)** | Monthly | Quarterly | Quarterly | Quarterly | Annual |
| **Important (Tier 2)** | Quarterly | Semi-Annual | Semi-Annual | Semi-Annual | Biennial |
| **Standard (Tier 3)** | Semi-Annual | Annual | N/A | Annual | N/A |

More critical = more frequent testing.

### 2.2 Create Annual Testing Calendar

**Step 4: Build Testing Schedule**

Create calendar with all tests for year:

**Example Calendar (Critical System - E-Commerce Website):**

| Month | Test Type | System | Participants | Duration |
|-------|-----------|--------|--------------|----------|
| January | Tabletop Exercise | E-Commerce | BC/DR team, Business | 2 hours |
| February | File Restore Test | E-Commerce Database | Backup admin | 1 hour |
| March | Failover Test | E-Commerce (Active-Passive) | Infrastructure team | 4 hours |
| April | System Restore Test | E-Commerce Web Servers | Infrastructure, QA | 6 hours |
| May | File Restore Test | E-Commerce Database | Backup admin | 1 hour |
| June | Tabletop Exercise | All Critical Systems | BC/DR team, Executives | 3 hours |
| July | Failover Test | E-Commerce | Infrastructure team | 4 hours |
| August | File Restore Test | E-Commerce | Backup admin | 1 hour |
| September | System Restore Test | E-Commerce | Infrastructure, QA | 6 hours |
| October | Tabletop Exercise | E-Commerce | BC/DR team, Business | 2 hours |
| November | File Restore Test | E-Commerce | Backup admin | 1 hour |
| December | **DR Simulation** | **All Critical Systems** | **All teams, Executives** | **8 hours** |

**Calendar Distribution:**
- Publish testing calendar to all stakeholders (beginning of year)
- Include in project planning (reserve time for testing)
- Adjust as needed but maintain minimum frequencies

---

## 3. Test Planning and Scheduling

### 3.1 Plan Individual Tests

**Step 5: Create Test Plan per Test**

For each scheduled test, create test plan document:

**Test Plan Template:**
```
TEST PLAN

Test ID: [Unique ID, e.g., BCDR-TEST-2024-Q1-01]
Test Date: [Date and time]
Test Type: [File Restore / System Restore / Failover / Tabletop / DR Simulation]
System Under Test: [System name]
Test Objectives:
- [Objective 1: e.g., Verify can restore database from last night's backup]
- [Objective 2: e.g., Measure actual restore time, compare to RTO requirement]

Test Scope:
- What will be tested: [Specific components, data, etc.]
- What will NOT be tested: [Out of scope]

Success Criteria:
- [ ] System/data restored successfully
- [ ] Data integrity verified (no corruption)
- [ ] Application functionality verified
- [ ] Restore time within RTO requirement
- [ ] No data loss exceeding RPO

Test Environment:
- [Production / Test / DR Site / Isolated Environment]
- [If test environment, how does it differ from production?]

Participants:
- Test Lead: [Name]
- Technical Team: [Names]
- Business Validation: [Name - validates business function works]
- Observers: [Names - audit, management]

Test Procedure:
- [Step-by-step procedure - reference recovery procedure document]

Rollback Plan:
- [If test fails or causes issues, how to revert]

Evidence to Collect:
- Screenshots of key steps
- Log files
- Test result documentation
- Timing measurements

Risk Mitigation:
- [How minimizing impact on production]
- [Communication plan if issues arise]
```

### 3.2 Coordinate Test Scheduling

**Step 6: Coordinate with Stakeholders**

**Schedule Considerations:**
- **Business Impact:** When can test occur without disrupting business? (maintenance windows, off-hours)
- **Resource Availability:** Are test participants available?
- **Dependencies:** Does test depend on other activities?

**Notification Timeline:**
- **4 weeks before:** Notify all participants, reserve time on calendars
- **1 week before:** Send test plan, reminder
- **1 day before:** Final confirmation, pre-test checklist

**Step 7: Obtain Approvals**

For tests with production risk (failover tests, DR simulations):
- Test plan approved by IT Operations Manager
- Business stakeholder approval (awareness of potential brief disruption)
- Executive approval for major DR simulations (high visibility, resource intensive)

---

## 4. Backup Restore Testing Procedures

### 4.1 File-Level Restore Test

**Step 8: Plan File Restore Test**

**Purpose:** Verify can restore individual files from backup.

**Frequency:** Monthly (Critical systems), Quarterly (Important systems)

**Procedure:**
1. Select files to restore (representative sample: documents, databases, configs)
2. Document file checksums before test (for integrity verification)
3. Initiate restore from backup
4. Compare restored files to originals (checksum match?)
5. Verify files are accessible and usable
6. Measure restore time
7. Document results

**Success Criteria:**
- Files restored successfully
- Checksums match (no corruption)
- Files accessible
- Restore time acceptable

### 4.2 System-Level Restore Test

**Step 9: Plan System Restore Test**

**Purpose:** Verify can restore entire system from backup.

**Frequency:** Quarterly (Critical), Semi-Annual (Important), Annual (Standard)

**Procedure:**
1. **Preparation:**
   - Prepare isolated test environment (separate from production)
   - Verify backup available (backup job successful, not corrupted)
   - Document pre-test state
2. **Execution:**
   - Initiate full system restore (OS, applications, data, configs)
   - Monitor restore progress (watch for errors)
   - Measure restore time (start to operational)
3. **Verification:**
   - System boots successfully
   - Services start correctly
   - Application accessible
   - Data integrity verified (database consistency check)
   - Core functionality tested (execute sample transactions)
   - Performance acceptable
4. **Documentation:**
   - Restore time vs RTO requirement
   - Issues encountered
   - Test result (Success / Partial / Failure)

**Use Checklist:** Annex-B Section 5.1 (Backup Restore Test Checklist)

### 4.3 Cross-Platform Restore Test

**Step 10: Test Restore to Different Platform**

**Purpose:** Verify can restore to different hardware/location (DORA requirement).

**Frequency:** Annual (for DORA-regulated systems)

**Scenarios:**
- Physical to virtual (or vice versa)
- On-premises to cloud
- Different hardware generation

**Why Important:** Proves backup is portable, not locked to specific hardware.

---

## 5. Failover Testing Procedures

### 5.1 Planned Failover Test

**Step 11: Plan Planned Failover**

**Purpose:** Verify failover mechanism works in controlled scenario.

**Frequency:** Quarterly (Critical systems with redundancy)

**Procedure:**
1. **Pre-Test:**
   - Schedule maintenance window
   - Notify stakeholders (brief service disruption possible)
   - Document pre-test state (primary active, secondary standby)
   - Verify data synchronized (primary and secondary in sync)
2. **Execution:**
   - Gracefully shut down primary (controlled shutdown)
   - Monitor failover process (health check detects failure)
   - Measure failover time (detection → secondary operational)
   - Verify secondary operational (services running, traffic flowing)
3. **Validation:**
   - Application functionality verified
   - Data accessible
   - No data loss (verify synchronization)
   - Performance acceptable
4. **Failback:**
   - Restore primary system
   - Synchronize data back to primary
   - Failback to primary (reverse failover)
   - Verify primary operational
5. **Documentation:**
   - Total failover time vs RTO requirement
   - Issues encountered
   - Test result

**Use Checklist:** Annex-B Section 5.2 (Failover Test Checklist)

### 5.2 Unplanned Failover Simulation

**Step 12: Simulate Unplanned Failure**

**Purpose:** Verify failover works when primary fails suddenly (worst-case).

**Frequency:** Annual (Critical systems)

**Difference from Planned:**
- **Sudden failure:** Hard shutdown, network disconnect (not graceful)
- **Automatic detection:** Health checks must detect failure automatically
- **Realistic scenario:** Simulates actual disaster

**Procedure:**
1. Suddenly terminate primary (hard shutdown, pull network cable)
2. Do NOT manually trigger failover (test automatic detection)
3. Monitor automatic failover (health check → failover decision → secondary takeover)
4. Measure detection time and failover time separately
5. Verify no data loss (replication may lag during sudden failure)

**Higher Risk:** More realistic but riskier. Requires careful planning.

---

## 6. DR Scenario Testing

### 6.1 Tabletop Exercise

**Step 13: Conduct Tabletop Exercise**

**Purpose:** Discussion-based walkthrough of DR procedures.

**Frequency:** Quarterly

**Format:** Discussion, no actual recovery

**Procedure:**
1. **Preparation (2-4 weeks before):**
   - Develop scenario (e.g., "Ransomware encrypts primary datacenter")
   - Prepare scenario details (what failed, when, impact)
   - Invite participants (BC/DR team, business stakeholders, IT)
2. **Execution (2-4 hours):**
   - Facilitator presents scenario
   - Participants walk through response step-by-step:
     - Who would you notify?
     - What recovery procedures would you execute?
     - What resources would you need?
     - What are potential issues?
   - Document discussion, decisions, gaps identified
3. **Post-Exercise:**
   - Document lessons learned
   - Identify plan improvements
   - Create action items

**Benefits:**
- Very low risk (no actual systems affected)
- Low cost (just participant time)
- Builds familiarity with plans
- Identifies gaps in procedures or communication

### 6.2 Full DR Simulation

**Step 14: Conduct DR Simulation**

**Purpose:** Comprehensive end-to-end test of BC/DR capability.

**Frequency:** Annual

**Format:** Actual execution of recovery (full scenario)

**Planning Timeline:** 6-8 weeks minimum

**Phases:**

**Phase 1: Planning (6-8 weeks before)**
- Develop scenario (realistic disaster: site loss, cyber attack, prolonged outage)
- Define scope (which systems will be recovered)
- Assemble team (all recovery teams, business stakeholders, executives)
- Prepare DR site/environment
- Communicate to organization (minimize surprise)
- Create detailed test plan and schedule

**Phase 2: Execution (4-8 hours or multi-day)**
- Kick-off (scenario presented, test begins)
- Activate crisis management team
- Execute recovery procedures:
  - Assess situation
  - Activate BC/DR plans
  - Recover systems per priority sequence
  - Test communications (internal, external)
  - Validate business processes (can business operate?)
- Document timeline (what happened when)
- Measure recovery times per system

**Phase 3: Validation**
- Verify systems operational
- Test end-to-end workflows (can complete business transactions?)
- Verify data integrity
- Test user access
- Measure overall recovery time

**Phase 4: Debrief (within 1 week)**
- Gather all participants
- Review what worked / what didn't
- Document lessons learned
- Create improvement plan

**Use Checklist:** Annex-B Section 5.3 (DR Simulation Checklist)

**Step 15: Develop Realistic Scenarios**

**Scenario Variety (rotate annually):**
- Year 1: Site loss (fire, flood, building evacuation)
- Year 2: Cyber incident (ransomware attack)
- Year 3: Prolonged cloud provider outage
- Year 4: Multiple simultaneous failures
- Year 5: Supply chain disruption (critical vendor failure)

**Scenario Realism:**
- Based on actual threats (ransomware is realistic, alien invasion is not)
- Include complications ("Cloud provider says recovery will take 12 hours, not 4")
- Challenge teams (inject unexpected issues during exercise)

---

## 7. Testing Without Production Impact

### 7.1 Isolated Test Environments

**Step 16: Use Test Environments**

**Option 1: Dedicated Test Infrastructure**
- Separate servers, storage, network (isolated from production)
- Restore production backups to test environment
- Test recovery without affecting production

**Pros:**
- Zero risk to production
- Can test destructively
- Can leave test environment running for extended validation

**Cons:**
- Requires dedicated infrastructure (cost)
- Test environment may not perfectly replicate production

**Option 2: Cloud Test Environment**
- Restore production backups to cloud (temporary)
- Test recovery in cloud
- Destroy cloud resources after test (cost-effective)

**Pros:**
- Pay only during test (cost-effective)
- Easy to scale to production size
- Geographic diversity testing

**Cons:**
- Data transfer time and cost
- Requires cloud connectivity

### 7.2 Production Testing Strategies

**Step 17: Minimize Production Impact**

When testing must involve production:

**Maintenance Windows:**
- Schedule tests during low-usage periods (nights, weekends)
- Announce in advance (give users warning)
- Have rollback plan ready

**Blue-Green Testing:**
- Maintain two production environments (Blue = current, Green = standby)
- Test failover from Blue to Green
- If issues, failback to Blue immediately

**Canary Testing:**
- Route small percentage of traffic (5-10%) to secondary system
- Monitor for issues
- If successful, gradually increase percentage

---

## 8. Test Documentation and Evidence

### 8.1 Document Test Execution

**Step 18: Collect Evidence During Test**

**Real-Time Documentation:**
- Timeline (what happened when - timestamp each major event)
- Screenshots of key steps
- Log files (backup logs, system logs, application logs)
- Metrics (restore time, failover time, data transferred)
- Issues encountered (errors, unexpected behavior)

**Step 19: Complete Test Report**

Use template from Annex-B Section 7.3 (Test Report Template).

**Test Report Includes:**
1. **Test Overview:** Objectives, scope, participants, date
2. **Test Execution:** Timeline, procedure followed, deviations
3. **Test Results:** 
   - Success criteria met? (Yes/No per criterion)
   - Metrics (RPO achieved, RTO achieved)
   - Overall result (Success / Partial Success / Failure)
4. **Lessons Learned:** What worked, what didn't, recommendations
5. **Remediation Plan:** (if test failed) Issues to fix, owner, timeline
6. **Evidence:** Attach screenshots, logs

**Step 20: Store Test Evidence**

**Evidence Repository:**
- Centralized storage (document management system)
- Organized by control (A.8.13, A.8.14, A.5.30)
- Organized by test type and date
- Retained for 3+ years (audit retention)

**Evidence Includes:**
- Test plans
- Test reports
- Screenshots
- Log files
- Approval records

---

## 9. Post-Test Review and Remediation

### 9.1 Conduct Post-Test Debrief

**Step 21: Debrief Session**

**Within 1 week of test:**
- Assemble all test participants
- Review test results
- Discuss what worked well
- Discuss what didn't work
- Identify improvement opportunities

**Debrief Agenda:**
- Test results summary (Did we meet objectives?)
- Issues encountered (technical, procedural, communication)
- Lessons learned (actionable insights)
- Recommendations (what should we change?)

**Step 22: Document Lessons Learned**

**Lessons Learned Categories:**
- **Process:** Recovery procedures incomplete or inaccurate
- **Technical:** System configurations caused issues
- **Communication:** Stakeholders not notified, unclear messaging
- **Training:** Team members didn't know procedures
- **Documentation:** Procedures outdated or unclear

**For Each Lesson:**
- Description (what happened)
- Root cause (why did it happen)
- Impact (how did it affect test)
- Recommendation (how to prevent in future)

### 9.2 Remediate Test Failures

**Step 23: Create Remediation Plan**

For each issue identified:

| Issue | Priority | Remediation Action | Owner | Target Date | Status |
|-------|----------|-------------------|-------|-------------|--------|
| Restore took 8 hours (RTO = 4 hours) | Critical | Implement redundancy or faster backup solution | Infrastructure | 90 days | Open |
| Backup procedure incomplete (missing step 5) | High | Update procedure documentation | Backup Admin | 30 days | Open |
| Team didn't know where to find DR plans | Medium | Add DR plan location to training | BC/DR Coord | 60 days | Open |

**Remediation Workflow:**
1. Issue identified in test
2. Prioritized (Critical / High / Medium / Low)
3. Assigned to owner
4. Target date set
5. Tracked to completion
6. Retest to verify fix

**Step 24: Update Plans and Procedures**

Based on lessons learned:
- Update recovery procedures (fix errors, add missing steps)
- Update training materials (address knowledge gaps)
- Update communication plans (fix notification issues)

**Version Control:**
- Increment version number
- Document what changed and why
- Archive old version
- Distribute updated version to all stakeholders

---

## 10. Continuous Testing Integration

### 10.1 Shift from Periodic to Continuous

**Step 25: Integrate Testing into Operations**

**Traditional Approach:** Test once per year, forget until next year.

**Continuous Approach:** Testing integrated into regular operations.

**Integration Opportunities:**

**After Infrastructure Changes:**
- New system deployed → Test backup before production
- Network change → Retest failover
- Application update → Verify backup includes new components

**After Plan Updates:**
- Recovery procedure changed → Walkthrough to verify changes correct
- New system added to DR scope → Initial restore test

**After Gap Remediation:**
- Issue fixed from previous test → Retest to verify fix worked

### 10.2 Automated Testing

**Step 26: Implement Automated Tests**

**What Can Be Automated:**
- Backup integrity verification (checksum validation)
- Automated restore tests (Veeam SureBackup, synthetic restores)
- Health check monitoring (continuous)
- Synthetic transactions (monitor application availability)

**What Cannot Be Automated:**
- Full DR scenarios (require human decision-making)
- Business process validation (requires human judgment)
- Communication testing

**Balance:** Automate what can be automated, manually test what requires human judgment.

---

## 11. Common Pitfalls and How to Avoid

### 11.1 Testing in Production (Risk of Outage)

**Pitfall:** Restore test in production environment causes production outage.

**Example:** Test restore of database to production server, accidentally overwrites production database.

**How to Avoid:**
- **Always test in isolated environment** (unless specifically testing production failover)
- Use dedicated test infrastructure
- Verify restore target before initiating restore

### 11.2 Not Documenting Test Results

**Pitfall:** Test conducted, results not documented. No evidence for audit.

**How to Avoid:**
- Test report template mandatory (Annex-B Section 7.3)
- Test report completed before test considered complete
- Test evidence stored in evidence repository

### 11.3 Failed Tests Ignored (Not Remediated)

**Pitfall:** Test fails, issues identified, nothing happens. Same issues appear in next test.

**How to Avoid:**
- Remediation plan required for all failed tests (Step 23)
- Remediation tracked in Assessment Workbook 4
- Retest required to verify remediation worked

### 11.4 Testing Same Scenario Repeatedly

**Pitfall:** Test restore of same system using same procedure every time. False sense of security.

**How to Avoid:**
- Vary test scenarios (Step 15)
- Test different systems (rotate through all critical systems)
- Test different failure modes (hardware, network, cyber, disaster)

### 11.5 No Post-Test Review (Lessons Not Learned)

**Pitfall:** Test conducted, no debrief, lessons not documented or actioned.

**How to Avoid:**
- Post-test debrief mandatory (Step 21)
- Lessons learned documented (Step 22)
- Plans updated based on lessons (Step 24)

---

## 12. Verification and Sign-Off

### 12.1 Completion Checklist

**Testing program established when:**

- [ ] Testing strategy defined (types, frequency, scope)
- [ ] Annual testing calendar created and published
- [ ] Test procedures documented (backup restore, failover, DR scenarios)
- [ ] Test plan template available
- [ ] Test report template available
- [ ] First round of tests completed:
  - [ ] At least one file restore test (per Critical system)
  - [ ] At least one system restore test (per Critical system)
  - [ ] At least one failover test (per redundant Critical system)
  - [ ] At least one tabletop exercise
- [ ] Test results documented
- [ ] Test evidence stored in repository
- [ ] Remediation plans created for failed tests
- [ ] Assessment Workbook 4 (Testing Results) populated
- [ ] Testing integrated into operational processes

### 12.2 Evidence to Collect

**Testing Program Evidence:**
- Testing strategy document
- Annual testing calendar
- Test procedures (backup, failover, DR scenarios)
- Test plans (for each test conducted)
- Test reports (for each test conducted)
- Screenshots and logs (test evidence)
- Lessons learned documentation
- Remediation tracking (for failed tests)
- Updated recovery procedures (based on test feedback)

**Storage:** Evidence repository, retained 3+ years

### 12.3 Stakeholder Approval

**Required Approvals:**

| Stakeholder | Approval For | Evidence |
|-------------|-------------|----------|
| BC/DR Coordinator | Testing program established and operational | Signature on testing strategy document |
| IT Operations Manager | Testing procedures appropriate and feasible | Signature on testing calendar |
| CISO | Testing meets compliance requirements | Verification that testing compliance metrics acceptable |
| Business Process Owners | Awareness of testing schedule and participation | Acknowledgment of testing calendar |

---

## 13. Next Steps

### 13.1 Ongoing Testing Operations

**Monthly:**
- Execute scheduled tests (per testing calendar)
- Document test results
- Track remediation progress

**Quarterly:**
- Review testing compliance (tests completed on schedule?)
- Update testing calendar (adjust for new systems, changed priorities)
- Report testing metrics to BC/DR Steering Committee

**Annually:**
- Conduct DR simulation (comprehensive test)
- Review and update testing strategy (still appropriate?)
- Publish next year's testing calendar

### 13.2 Integration with BC/DR Program

- **BC/DR Assessment** (IMP-S5): Testing compliance assessed
- **Continuous Improvement:** Test feedback improves plans and procedures
- **Audit Readiness:** Test evidence supports audit compliance

---

**Document End**

*"Test like you mean it. Test like failure is inevitable. Test until you're confident."*

*Testing is not overhead - it's the only way to prove BC/DR works.*

---

**APPROVAL SIGNATURES**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| BC/DR Coordinator | | | |
| IT Operations Manager | | | |
| Quality Assurance Manager | | | |
| CISO | | | |

**Next Review Date:** [One year from approval date]