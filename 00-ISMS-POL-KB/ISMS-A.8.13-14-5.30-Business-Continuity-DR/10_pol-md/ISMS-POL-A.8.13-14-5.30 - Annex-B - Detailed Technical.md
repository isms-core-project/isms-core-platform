# ISMS-POL-A.8.13-14-5.30-Annex-B: Detailed Technical Specifications

**Document Classification:** Internal - ISMS Policy  
**Version:** 1.0  
**Effective Date:** [To be defined]  
**Review Cycle:** Annual  
**Policy Owner:** Chief Information Security Officer (CISO)  
**Approved By:** [Approval Authority]

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Security Operations Manager / CISO | Initial technical specifications for BC/DR |

---

## Table of Contents

1. [Purpose of Technical Specifications](#1-purpose-of-technical-specifications)
2. [RPO/RTO Classification Matrix](#2-rporto-classification-matrix)
3. [BIA Detailed Worksheet Template](#3-bia-detailed-worksheet-template)
4. [Recovery Procedure Template](#4-recovery-procedure-template)
5. [Testing Checklists](#5-testing-checklists)
6. [Compliance Calculation Formulas](#6-compliance-calculation-formulas)
7. [Evidence Documentation Templates](#7-evidence-documentation-templates)
8. [Sample Recovery Playbook Structure](#8-sample-recovery-playbook-structure)

---

## 1. Purpose of Technical Specifications

### 1.1 Role of This Annex

This annex provides **detailed technical specifications, templates, and formulas** to support implementation of BC/DR controls. These are practical tools for:
- Conducting Business Impact Analysis
- Documenting recovery procedures
- Testing BC/DR capabilities
- Calculating compliance metrics
- Collecting evidence

### 1.2 How to Use These Specifications

**For Implementation:**
- Use templates as starting point (adapt to [Organization] context)
- Follow formulas for compliance calculations
- Use checklists to ensure completeness

**For Audits:**
- Reference specifications to demonstrate systematic approach
- Show evidence collected per templates
- Demonstrate compliance calculations per formulas

---

## 2. RPO/RTO Classification Matrix

### 2.1 System Criticality Classification Criteria

| Criticality Tier | Criteria | RPO Range | RTO Range | Backup Frequency | Redundancy |
|------------------|----------|-----------|-----------|------------------|------------|
| **Critical (Tier 1)** | Revenue-generating systems, customer-facing applications, regulatory-critical | ≤ 4 hours | ≤ 4 hours | Hourly or continuous | **Required** (Active-Passive minimum) |
| **Important (Tier 2)** | Internal business applications, supporting processes | ≤ 24 hours | ≤ 24 hours | Daily | **Recommended** (Warm standby or backup) |
| **Standard (Tier 3)** | Non-critical applications, internal tools | ≤ 7 days | ≤ 7 days | Weekly | Optional |
| **Low (Tier 4)** | Archived data, non-essential systems | > 7 days or Risk Accepted | > 7 days or Risk Accepted | Monthly or none | Not required |

### 2.2 Detailed RPO/RTO Matrix Template

**Template for Documenting RPO/RTO Requirements:**

| System Name | Business Process | Criticality Tier | Financial Impact ($/hour) | Operational Impact | MTPD | **RPO Requirement** | **RTO Requirement** | Justification |
|-------------|------------------|------------------|---------------------------|-------------------|------|---------------------|---------------------|---------------|
| E-Commerce Website | Online Sales | Critical (Tier 1) | $50,000/hour | Cannot process orders | 4 hours | 1 hour | 2 hours | Revenue loss catastrophic after 4 hours |
| ERP System | Finance, HR, Supply Chain | Important (Tier 2) | $5,000/hour | Degraded operations, manual workarounds | 24 hours | 4 hours | 8 hours | Can operate manually for 24 hours |
| Internal Wiki | Knowledge Management | Standard (Tier 3) | Negligible | Inconvenience only | 7 days | 24 hours | 48 hours | Non-critical, acceptable delay |
| Archive Server | Historical Records | Low (Tier 4) | None | None | 30 days | 7 days | 14 days | Rarely accessed, long recovery acceptable |

**Instructions for Completion:**
1. **System Name:** Exact system name (from asset inventory)
2. **Business Process:** Primary business function supported
3. **Criticality Tier:** Based on BIA (Tier 1-4)
4. **Financial Impact:** Revenue loss + recovery cost per hour of downtime
5. **Operational Impact:** Description of business impact during downtime
6. **MTPD (Maximum Tolerable Period of Disruption):** Longest acceptable downtime before severe consequences
7. **RPO Requirement:** Maximum acceptable data loss (in time)
8. **RTO Requirement:** Maximum acceptable downtime (typically 50-75% of MTPD)
9. **Justification:** Business reason for requirements

---

## 3. BIA Detailed Worksheet Template

### 3.1 BIA Interview Questions Template

**Section 1: System Identification**
1. System name and description
2. System owner / Business process owner
3. Primary business function(s) supported
4. User base (internal/external, count)
5. Dependencies (what does this system depend on?)
6. Dependents (what depends on this system?)

**Section 2: Impact Assessment**

**Financial Impact Questions:**
1. What is the estimated revenue loss per hour of system downtime?
2. What are the costs of manual workarounds during downtime?
3. Are there contractual penalties for service unavailability (SLA breaches)?
4. Are there regulatory fines for non-availability?
5. What are the recovery costs (labor, vendor support)?

**Operational Impact Questions:**
1. Can business functions continue without this system? If yes, for how long?
2. What manual workarounds exist during system downtime?
3. How many employees are impacted by system unavailability?
4. What is the impact on customers (internal/external)?
5. What is the impact on supply chain or partners?

**Reputational Impact Questions:**
1. Would system unavailability be visible to customers?
2. Would prolonged outage damage brand reputation?
3. Would media coverage of outage be likely?
4. Would competitors gain advantage during outage?
5. What is the risk of long-term customer loss?

**Regulatory/Legal Impact Questions:**
1. Are there regulatory requirements for system availability?
2. Would outage violate compliance obligations (DORA, NIS2, etc.)?
3. Are there contractual SLA commitments?
4. What is the potential legal liability from unavailability?

**Section 3: Time-Based Impact Assessment**

| Time Period | Financial Impact | Operational Impact | Reputational Impact | Overall Severity |
|-------------|------------------|-------------------|---------------------|------------------|
| **0-1 hours** | Minimal | Minor inconvenience, workarounds available | None | Low |
| **1-4 hours** | Moderate | Significant disruption, difficult workarounds | Minor (internal complaints) | Medium |
| **4-24 hours** | High | Major disruption, customer impact | Moderate (customer complaints, some media) | High |
| **1-3 days** | Very High | Critical business impact, unable to fulfill obligations | High (significant media, customer loss) | Very High |
| **> 3 days** | Catastrophic | Business failure risk, existential threat | Severe (major media, permanent customer loss) | Critical |

**MTPD Determination:** Identify the time period where impact becomes "Very High" or "Critical" → This is MTPD

**Section 4: RPO/RTO Determination**

**RPO Determination:**
- Question: "How much data loss is acceptable?"
- Consider: Financial impact of recreating lost data, regulatory requirements
- RPO = [Business owner decision based on data loss impact]

**RTO Determination:**
- Question: "How quickly must the system be restored?"
- Based on: MTPD and impact over time
- Formula: RTO = MTPD × 0.5 to 0.75 (buffer for safe recovery)
- RTO = [Business owner decision based on MTPD]

### 3.2 BIA Summary Template

**BIA Summary Report:**

**Executive Summary:**
- Total systems assessed: [count]
- Critical systems (Tier 1): [count]
- Important systems (Tier 2): [count]
- Standard systems (Tier 3): [count]
- Total estimated financial impact ($/hour across all critical systems): [$X]

**Key Findings:**
- Most critical system: [System name] (MTPD: [X hours], Financial impact: [$X/hour])
- Systems requiring immediate BC/DR investment: [List]
- Systems with inadequate current protection: [List]

**Recovery Priority Sequence:**
1. [System] - RTO: [X hours] - Justification: [X]
2. [System] - RTO: [X hours] - Justification: [X]
3. [System] - RTO: [X hours] - Justification: [X]

**Recommendations:**
- BC/DR investment priorities
- Gap remediation roadmap
- Testing priorities

---

## 4. Recovery Procedure Template

### 4.1 System Recovery Procedure Template

**SYSTEM RECOVERY PROCEDURE**

**System:** [System Name]  
**Version:** [Version Number]  
**Last Updated:** [Date]  
**Procedure Owner:** [Name/Role]  
**Estimated Recovery Time:** [X hours]

---

**1. PREREQUISITES**

**Access Required:**
- [ ] Backup administrator account
- [ ] System administrator account (restored system)
- [ ] Database administrator account (if applicable)
- [ ] Network access to restore location

**Tools/Resources Required:**
- [ ] Backup solution access (Veeam/Commvault/etc.)
- [ ] Restore target infrastructure (servers, storage)
- [ ] Software installation media/licenses
- [ ] Configuration files/documentation
- [ ] Contact information for escalation

**Pre-Restore Checklist:**
- [ ] Verify backup availability (backup exists and is not corrupted)
- [ ] Verify restore target is ready (servers provisioned, network configured)
- [ ] Verify sufficient storage space for restore
- [ ] Notify stakeholders of restore operation
- [ ] Document current state (for rollback if needed)

---

**2. DETECTION AND ASSESSMENT**

**Failure Detection:**
- How is failure typically detected? [Monitoring alert / User report / etc.]
- Who detects failure? [Operations team / Monitoring system]
- What are symptoms of failure? [Symptoms]

**Impact Assessment:**
- Assess severity: [Critical / High / Medium / Low]
- Assess scope: [Single server / Multiple servers / Complete system]
- Determine if recovery procedure should be activated: [Decision criteria]

**Decision Point:**
- If severity is Critical AND system is Tier 1 → Activate recovery immediately
- If severity is High → Assess if workaround available, activate if not
- If severity is Medium/Low → Attempt troubleshooting first

---

**3. RECOVERY STEPS**

**Step 1: Initiate Restore**
- Action: Log into backup solution [Backup Solution Name]
- Action: Navigate to [System Name] backup job
- Action: Select recovery point: 
  - Use most recent backup BEFORE failure (for data corruption)
  - Use most recent backup (for hardware failure)
- Action: Specify restore target: [Target server/location]
- Estimated time: [X minutes]

**Step 2: Execute Restore**
- Action: Start restore job
- Action: Monitor restore progress (check for errors)
- Action: If errors occur → Escalate to [Escalation Contact]
- Estimated time: [X hours] (depends on data size)

**Step 3: Verify Data Integrity**
- Action: Once restore completes, verify file integrity:
  - Check file count matches expected
  - Check critical files are accessible
  - Run database consistency check (if database):
    ```
    DBCC CHECKDB ([DatabaseName]) WITH NO_INFOMSGS
    ```
- Action: If integrity issues → Attempt restore from previous backup, escalate
- Estimated time: [X minutes]

**Step 4: Restore System Configuration**
- Action: Restore system configurations (if not included in backup):
  - Network configuration: [Procedure]
  - Application configuration: [Procedure]
  - Security settings: [Procedure]
- Action: Verify configurations match baseline (reference Configuration Management)
- Estimated time: [X minutes]

**Step 5: Start Services**
- Action: Start system services in correct order:
  1. [Service 1]
  2. [Service 2]
  3. [Service 3]
- Action: Verify each service starts successfully
- Action: If services fail to start → Check logs, escalate if needed
- Estimated time: [X minutes]

**Step 6: Verify System Functionality**
- Action: Perform functional tests:
  - [ ] Can log into system successfully
  - [ ] Can access application main page/interface
  - [ ] Can execute core transaction (e.g., create test record)
  - [ ] Can query database successfully
  - [ ] Integrations with other systems working
- Action: Perform performance check (acceptable response time?)
- Estimated time: [X minutes]

**Step 7: Restore User Access**
- Action: Verify user access controls are correct
- Action: Test user login (sample users)
- Action: If access issues → Review security group memberships, permissions
- Estimated time: [X minutes]

---

**4. VERIFICATION AND HANDOVER**

**Final Verification Checklist:**
- [ ] All services running and stable
- [ ] Data integrity verified (no corruption)
- [ ] Application functionality tested (core functions work)
- [ ] Performance acceptable (response time within normal range)
- [ ] User access working
- [ ] No error messages in logs
- [ ] Monitoring restored and operational

**Stakeholder Notification:**
- Action: Notify business owner: "System restored and operational"
- Action: Notify users: [Communication template]
- Action: Notify executive management (if Critical system)

**Documentation:**
- Action: Document restore in incident ticket
- Action: Complete recovery report (see Section 7.4)
- Action: Update asset inventory if hardware changed

**Post-Recovery Monitoring:**
- Monitor system closely for [24-48 hours] after recovery
- Watch for delayed issues (degraded performance, intermittent errors)

---

**5. ROLLBACK PLAN (If Recovery Fails)**

If recovery fails or causes additional issues:
- Action: Stop recovery immediately
- Action: Assess if previous state can be restored (if snapshot taken)
- Action: Escalate to [Senior Technical Lead]
- Action: Consider alternative recovery: [Alternative approach]

---

**6. ESCALATION CONTACTS**

| Level | Name | Role | Contact | When to Escalate |
|-------|------|------|---------|------------------|
| 1 | [Name] | Backup Administrator | [Phone/Email] | Backup restore issues |
| 2 | [Name] | System Owner | [Phone/Email] | System configuration issues |
| 3 | [Name] | Senior Technical Lead | [Phone/Email] | Recovery failing, multiple issues |
| 4 | [Name] | BC/DR Coordinator | [Phone/Email] | Need DR site activation |

---

**APPENDIX: Common Issues and Troubleshooting**

| Issue | Possible Cause | Resolution |
|-------|---------------|------------|
| Restore fails with "file not found" error | Backup incomplete or corrupted | Attempt restore from previous backup |
| Restored system won't boot | Configuration error | Review boot configuration, check logs |
| Database consistency errors | Corruption during failure | Restore from earlier backup |
| Services fail to start | Missing dependencies | Check prerequisite services, licenses |
| Poor performance after restore | Resource constraints | Check CPU/memory/disk utilization |

---

**Document End**

---

## 5. Testing Checklists

### 5.1 Backup Restore Test Checklist

**Pre-Test:**
- [ ] Backup restore test scheduled (date/time confirmed)
- [ ] Test environment prepared (isolated from production)
- [ ] Stakeholders notified (no disruption to production expected)
- [ ] Backup verified available (backup job successful, backup not corrupted)
- [ ] Test team assembled (tester, system owner, observer)

**During Test:**
- [ ] Test start time documented
- [ ] Backup recovery point documented (which backup being restored, date/time)
- [ ] Restore initiated (restore job started)
- [ ] Restore progress monitored (watching for errors)
- [ ] Any errors documented immediately
- [ ] Restore completion time documented
- [ ] Data integrity verified (file count, checksum, database consistency check)
- [ ] Application functionality tested (can access data, core functions work)
- [ ] Performance verified (acceptable response time)

**Post-Test:**
- [ ] Total restore time calculated (start to verified operational)
- [ ] RPO verified (how old was restored data? within requirement?)
- [ ] RTO verified (restore time within requirement?)
- [ ] Test result determined: Success / Partial Success / Failure
- [ ] Issues documented (any problems encountered)
- [ ] Screenshots/evidence captured
- [ ] Test report completed (see Section 7.3)
- [ ] Test environment cleaned up (destroyed or shut down)
- [ ] Stakeholders notified of results
- [ ] If test failed → Remediation plan created
- [ ] Next test scheduled

### 5.2 Failover Test Checklist

**Pre-Test:**
- [ ] Failover test scheduled (maintenance window confirmed)
- [ ] Stakeholders notified (brief service disruption possible)
- [ ] Primary and secondary systems status verified (both healthy before test)
- [ ] Failover procedure reviewed (team knows steps)
- [ ] Rollback plan ready (in case failover fails)
- [ ] Test team assembled (operators, system owner, observer)

**During Test:**
- [ ] Test start time documented
- [ ] Pre-failover state documented (primary system status)
- [ ] Failover initiated (graceful shutdown of primary OR unplanned simulation)
- [ ] Failure detection time documented (when was primary failure detected?)
- [ ] Failover decision time documented (automatic or manual decision)
- [ ] Failover execution started
- [ ] Secondary system takeover monitored
- [ ] Failover completion time documented
- [ ] Secondary system functionality verified (services running, accepting traffic)
- [ ] Data synchronization verified (no data loss)
- [ ] Performance verified (acceptable under failover)

**Failback:**
- [ ] Primary system restored and verified healthy
- [ ] Failback initiated
- [ ] Data synchronized back to primary (if needed)
- [ ] Traffic routed back to primary
- [ ] Failback successful, primary operational

**Post-Test:**
- [ ] Total failover time calculated (detection → secondary operational)
- [ ] RTO verified (failover time within requirement?)
- [ ] RPO verified (any data loss? within requirement?)
- [ ] Test result determined: Success / Partial Success / Failure
- [ ] Issues documented
- [ ] Evidence captured (logs, screenshots)
- [ ] Test report completed
- [ ] Stakeholders notified
- [ ] If test failed → Remediation plan created
- [ ] Next test scheduled

### 5.3 DR Simulation Checklist

**Pre-Simulation:**
- [ ] DR simulation scheduled (6+ weeks notice)
- [ ] Scenario developed and documented
- [ ] Participants identified and notified
- [ ] Test objectives defined (what are we testing?)
- [ ] Success criteria defined (how do we know if it worked?)
- [ ] DR site/environment prepared
- [ ] Facilitators/evaluators assigned
- [ ] Executive briefing conducted (management awareness)

**During Simulation:**
- [ ] Simulation kick-off (scenario presented to participants)
- [ ] Crisis management team activated
- [ ] Recovery procedures executed
- [ ] Communications tested (internal, external)
- [ ] Systems recovered per recovery plan
- [ ] Business processes tested (can business operate from DR?)
- [ ] Coordination observed (how well did teams work together?)
- [ ] Issues documented in real-time
- [ ] Timeline documented (what happened when)
- [ ] Recovery metrics captured (time to recover each system)

**Post-Simulation:**
- [ ] Debrief session conducted (within 1 week)
- [ ] Lessons learned documented
- [ ] Test report completed (comprehensive)
- [ ] Gaps identified and prioritized
- [ ] Improvement plan created (action items, owners, deadlines)
- [ ] Executive presentation (results, recommendations)
- [ ] Plans updated based on lessons learned
- [ ] Next simulation scheduled

---

## 6. Compliance Calculation Formulas

### 6.1 RPO Compliance Calculation

**Formula:**
```
RPO Compliance (per system) = 
  IF (Actual_Backup_Frequency ≤ RPO_Requirement) THEN "Compliant" 
  ELSE "Non-Compliant"

RPO Gap (per system) = 
  MAX(0, Actual_Backup_Frequency - RPO_Requirement)

Overall RPO Compliance (%) = 
  (Systems_Compliant_RPO / Total_Systems) × 100
```

**Example:**
- System A: RPO Requirement = 4 hours, Backup Frequency = 2 hours → Compliant ✅, Gap = 0
- System B: RPO Requirement = 4 hours, Backup Frequency = 24 hours → Non-Compliant ❌, Gap = 20 hours
- Overall: 1 compliant of 2 systems = 50% compliance

### 6.2 RTO Compliance Calculation

**Formula:**
```
RTO Compliance (per system) = 
  IF (Actual_Recovery_Time ≤ RTO_Requirement) THEN "Compliant" 
  ELSE "Non-Compliant"

RTO Gap (per system) = 
  MAX(0, Actual_Recovery_Time - RTO_Requirement)

Overall RTO Compliance (%) = 
  (Systems_Compliant_RTO / Total_Systems) × 100
```

**Note:** Actual_Recovery_Time must be **measured through testing**, not estimated.

### 6.3 Backup Coverage Calculation

**Formula:**
```
Backup Coverage (%) = 
  (Systems_With_Backup / Total_In_Scope_Systems) × 100

Critical System Backup Coverage (%) = 
  (Critical_Systems_With_Backup / Total_Critical_Systems) × 100
```

**Target:** ≥95% overall, 100% for Critical systems

### 6.4 Testing Compliance Calculation

**Formula:**
```
Testing Compliance (per system) = 
  IF (Days_Since_Last_Test ≤ Testing_Frequency_Required) THEN "Compliant" 
  ELSE "Overdue"

Overall Testing Compliance (%) = 
  (Systems_Tested_On_Schedule / Systems_Requiring_Testing) × 100
```

**Example:**
- Critical system requires quarterly testing (90 days)
- Last tested 75 days ago → Compliant ✅
- Last tested 120 days ago → Overdue ❌

**Target:** ≥80% overall, ≥95% for Critical systems

### 6.5 3-2-1-1-0 Compliance Scoring

**Scoring per System:**
```
3 Copies: IF (Copies ≥ 3) THEN 1 point ELSE 0
2 Media Types: IF (Media_Types ≥ 2) THEN 1 point ELSE 0
1 Offsite: IF (Offsite_Copy = TRUE) THEN 1 point ELSE 0
1 Immutable: IF (Immutable_Copy = TRUE) THEN 1 point ELSE 0
0 Errors: IF (Last_Restore_Test = "Success") THEN 1 point ELSE 0

Total Score (per system) = SUM(above) = 0 to 5 points

3-2-1-1-0 Compliance (per system) = 
  IF (Total_Score = 5) THEN "Full Compliance" 
  ELSE IF (Total_Score ≥ 3) THEN "Partial Compliance"
  ELSE "Non-Compliant"

Overall 3-2-1-1-0 Compliance (%) = 
  (Systems_Full_Compliance / Total_Systems) × 100
```

### 6.6 Overall BC/DR Maturity Score

**Weighted Formula:**
```
Overall Maturity Score = 
  (Backup_Coverage × 0.20) +
  (RPO_Compliance × 0.20) +
  (RTO_Compliance × 0.20) +
  (Testing_Compliance × 0.20) +
  (SPOF_Mitigation_Rate × 0.10) +
  (Gap_Remediation_Rate × 0.10)

Result: 0-100%
```

**Maturity Levels:**
- **0-60%:** Level 1 - Initial (significant risk)
- **60-75%:** Level 2 - Managed (basic compliance)
- **75-90%:** Level 3 - Defined (good maturity)
- **90-100%:** Level 4 - Optimized (excellent maturity)

---

## 7. Evidence Documentation Templates

### 7.1 Evidence Log Template

| Evidence ID | Evidence Type | Control(s) Supported | Date Created | Created By | Storage Location | Retention Period |
|-------------|---------------|---------------------|--------------|------------|------------------|------------------|
| BCDR-001 | Backup job logs | A.8.13, A.8.15 | 2024-10-15 | Operations Team | /evidence/backup/ | 3 years |
| BCDR-002 | Restore test report | A.8.13 | 2024-10-20 | Backup Admin | /evidence/testing/ | 3 years |
| BCDR-003 | Failover test report | A.8.14 | 2024-10-25 | Infrastructure | /evidence/testing/ | 3 years |
| BCDR-004 | BIA documentation | A.5.30 | 2024-09-01 | BC/DR Coord | /evidence/bia/ | 3 years |

### 7.2 Test Evidence Requirements

**Minimum Evidence per Test:**
1. **Test Plan** (before test)
   - Test objectives
   - Test scenario
   - Success criteria
   - Participants
   
2. **Test Execution Evidence** (during test)
   - Screenshots of key steps
   - Log files (backup/restore logs, system logs)
   - Timeline (start time, major milestones, completion time)
   
3. **Test Results** (after test)
   - Result summary (Success/Failure)
   - Metrics (RPO achieved, RTO achieved)
   - Issues encountered
   
4. **Test Report** (comprehensive documentation)
   - All of the above consolidated
   - Lessons learned
   - Recommendations
   - Sign-off by stakeholders

### 7.3 Test Report Template

**BC/DR TEST REPORT**

**Test ID:** [Unique ID]  
**Test Date:** [Date]  
**Test Type:** [Backup Restore / Failover / DR Simulation]  
**System Tested:** [System Name]  
**Test Result:** [Success / Partial Success / Failure]

---

**1. TEST OVERVIEW**

**Objectives:**
- [Objective 1: e.g., Verify backup restore works]
- [Objective 2: e.g., Measure actual RTO]

**Scope:**
- Systems: [List]
- Data: [Amount]
- Environment: [Production / Test / DR]

**Participants:**
- Test Lead: [Name]
- Technical Team: [Names]
- Observers: [Names]

---

**2. TEST EXECUTION**

**Timeline:**
- Test Start: [Date/Time]
- [Milestone 1]: [Date/Time]
- [Milestone 2]: [Date/Time]
- Test Complete: [Date/Time]
- Total Duration: [X hours]

**Procedure Followed:**
- [Reference to recovery procedure document]
- Any deviations from procedure: [List or "None"]

**Issues Encountered:**
- [Issue 1: Description, Impact, Resolution]
- [Issue 2: Description, Impact, Resolution]
- Or "None"

---

**3. TEST RESULTS**

**Success Criteria:**
- [Criterion 1]: ✅ Met / ❌ Not Met
- [Criterion 2]: ✅ Met / ❌ Not Met

**Metrics:**
- RPO Achieved: [X hours] (Requirement: [Y hours]) → ✅ / ❌
- RTO Achieved: [X hours] (Requirement: [Y hours]) → ✅ / ❌
- Data Integrity: ✅ Verified / ❌ Issues Found
- Functionality: ✅ All Functions Work / ⚠️ Some Issues / ❌ Non-Functional

**Overall Result:**
- ✅ **Success**: All objectives met, system fully recovered within requirements
- ⚠️ **Partial Success**: System recovered but with issues or outside requirements
- ❌ **Failure**: System could not be recovered

---

**4. LESSONS LEARNED**

**What Worked Well:**
- [Observation 1]
- [Observation 2]

**What Didn't Work:**
- [Issue 1]
- [Issue 2]

**Recommendations:**
- [Recommendation 1: Update procedure to include X]
- [Recommendation 2: Increase backup frequency]

---

**5. REMEDIATION PLAN** (if test failed or partial success)

| Issue | Priority | Remediation Action | Owner | Target Date | Status |
|-------|----------|-------------------|-------|-------------|--------|
| [Issue] | Critical | [Action] | [Name] | [Date] | Open |

---

**6. EVIDENCE ATTACHED**

- [ ] Test plan
- [ ] Screenshots of key steps
- [ ] Log files
- [ ] Verification reports

---

**APPROVALS**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Test Lead | | | |
| System Owner | | | |
| BC/DR Coordinator | | | |

---

### 7.4 Recovery Report Template

**Used for Actual Recovery Events (not tests)**

**SYSTEM RECOVERY REPORT**

**Incident ID:** [Incident Ticket Number]  
**Recovery Date:** [Date]  
**System:** [System Name]  
**Recovery Result:** [Success / Partial / Failed]

**1. INCIDENT SUMMARY**
- Failure detected: [Date/Time]
- Failure type: [Hardware / Software / Human Error / Disaster / Cyber]
- Scope: [What failed]
- Business impact: [Description]

**2. RECOVERY EXECUTION**
- Recovery started: [Date/Time]
- Recovery method: [Restore from backup / Failover / Other]
- Recovery completed: [Date/Time]
- Total downtime: [X hours]

**3. RECOVERY METRICS**
- RPO: [X hours] - Data loss from [Time] to [Time]
- RTO: [X hours] - System down from [Time] to [Time]
- Met requirements? RPO: ✅/❌ RTO: ✅/❌

**4. LESSONS LEARNED**
- What worked: [List]
- What didn't work: [List]
- Plan updates needed: [List]

**5. FOLLOW-UP ACTIONS**
- Root cause analysis: [Owner, Due Date]
- Plan updates: [Owner, Due Date]
- Preventive measures: [Owner, Due Date]

---

## 8. Sample Recovery Playbook Structure

### 8.1 Playbook Overview

A **Recovery Playbook** is a quick-reference guide for emergency recovery, designed for use during high-pressure situations.

**Characteristics:**
- **Concise:** 1-2 pages per scenario (laminated card or pocket guide)
- **Visual:** Flowcharts, decision trees, clear steps
- **Accessible:** Offline copies available (not just digital)
- **Tested:** Used during DR exercises to verify usability

### 8.2 Sample Playbook: Ransomware Recovery

**RANSOMWARE RECOVERY PLAYBOOK**

**SCENARIO:** Ransomware has encrypted production systems

---

**IMMEDIATE ACTIONS (First 15 minutes):**

1. **ISOLATE** infected systems (disconnect from network immediately)
2. **PRESERVE** evidence (don't power off, don't delete logs)
3. **ACTIVATE** Incident Response Team + BC/DR Coordinator
4. **ASSESS** scope: What is encrypted? What is still clean?
5. **VERIFY** backups are safe (check immutable/offline backups NOT encrypted)

---

**DECISION TREE:**

```
Are immutable/offline backups available and clean?
│
├─ YES → Proceed to Recovery
│
└─ NO → CRITICAL SITUATION
         - Do NOT pay ransom yet (preserve negotiation option)
         - Engage cyber insurance, legal counsel
         - Escalate to executive management immediately
         - Consider external incident response firm
```

---

**RECOVERY STEPS** (if clean backups available):

**Step 1: Verify Backup Integrity** (30 min)
- Mount immutable backup (read-only)
- Scan backup for malware (ensure ransomware not in backup)
- Verify backup date (ensure it's from before infection)

**Step 2: Prepare Clean Recovery Environment** (1-2 hours)
- Build isolated recovery environment (separate network)
- Ensure recovery environment is hardened (patched, secured)
- Do NOT connect to production network yet

**Step 3: Restore Systems to Clean Environment** (4-8 hours)
- Restore systems from clean backup
- Verify functionality in isolated environment
- Scan restored systems for any remaining malware

**Step 4: Harden Recovered Systems** (2-4 hours)
- Apply all security patches
- Change all passwords (assume compromised)
- Review and tighten security configurations
- Install/update EDR/antimalware

**Step 5: Return to Production** (1-2 hours)
- Verify recovered systems are clean (final scan)
- Carefully reconnect to production network (monitored)
- Monitor closely for 48-72 hours for reinfection

---

**TOTAL ESTIMATED RTO: 8-18 hours** (depending on data size and complexity)

---

**COMMUNICATIONS:**

- **Internal:** Notify all employees, explain situation, provide updates every 2 hours
- **External:** Notify customers if customer data affected (GDPR/privacy requirements)
- **Regulatory:** NIS2 requires 24-hour early warning, 72-hour detailed report

**Contacts:**
- Incident Response Lead: [Name, Phone]
- BC/DR Coordinator: [Name, Phone]
- Cyber Insurance: [Policy Number, Contact]
- Legal Counsel: [Name, Phone]
- Forensics Firm: [Company, Contact]

---

**CRITICAL: DO NOT:**
- ❌ Pay ransom without executive approval and legal counsel
- ❌ Power off systems (preserves forensics)
- ❌ Restore to infected production network (will be re-encrypted)
- ❌ Delete logs (needed for investigation)

---

**Document End**

---

## Conclusion

These detailed technical specifications provide practical tools for implementing BC/DR controls:

✅ **RPO/RTO Matrix:** Classify systems and document requirements systematically  
✅ **BIA Worksheet:** Conduct comprehensive impact analysis  
✅ **Recovery Procedures:** Document step-by-step recovery with checklists  
✅ **Testing Checklists:** Ensure complete testing coverage  
✅ **Compliance Formulas:** Calculate metrics consistently  
✅ **Evidence Templates:** Collect audit-ready evidence  
✅ **Recovery Playbooks:** Enable rapid response during emergencies  

**Usage:**
- Adapt templates to [Organization] context
- Use checklists to ensure completeness
- Follow formulas for consistent compliance measurement
- Reference playbooks during actual incidents

---

**APPROVAL SIGNATURES**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | | | |
| BC/DR Coordinator | | | |
| Quality Assurance Manager | | | |
| Documentation Manager | | | |

**Next Review Date:** [One year from approval date]