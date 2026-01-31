# ISMS-POL-A.8.13-14-5.30-S5: Testing Methodology and Evidence Framework

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
| 1.0 | [Date] | Security Operations Manager / CISO | Initial testing methodology and evidence framework for A.8.13/A.8.14/A.5.30 |

---

## Table of Contents

1. [Testing Philosophy](#1-testing-philosophy)
2. [Backup Testing Methodology (A.8.13)](#2-backup-testing-methodology-a813)
3. [Redundancy Testing Methodology (A.8.14)](#3-redundancy-testing-methodology-a814)
4. [ICT BC Testing Methodology (A.5.30)](#4-ict-bc-testing-methodology-a530)
5. [RPO/RTO Compliance Assessment](#5-rporto-compliance-assessment)
6. [Evidence Collection Requirements](#6-evidence-collection-requirements)
7. [Compliance Scoring Methodology](#7-compliance-scoring-methodology)
8. [Gap Analysis Methodology](#8-gap-analysis-methodology)
9. [Continuous Testing Approach](#9-continuous-testing-approach)
10. [Reporting and Dashboards](#10-reporting-and-dashboards)

---

## 1. Testing Philosophy

### 1.1 The Feynman Principle Applied to BC/DR

**"The first principle is that you must not fool yourself—and you are the easiest person to fool."** - Richard Feynman

This principle is the foundation of [Organization]'s BC/DR testing approach:

**Cargo Cult BC/DR (Self-Deception):**
- "We have backups configured." → Assumes backups work
- "We have redundant systems." → Assumes failover works
- "We have a BC/DR plan." → Assumes plan is executable

**Evidence-Based BC/DR (Feynman Approach):**
- "We restored the production database from backup in 2.3 hours last Tuesday." → Proved recovery works
- "We failed over to secondary datacenter in 11 minutes during last quarter's test." → Proved failover works
- "We executed full DR scenario last month with 23 participants and identified 6 gaps, all now remediated." → Proved plan works

### 1.2 The "Untested = Broken" Assumption

[Organization] operates under the principle: **Until proven otherwise through testing, assume it doesn't work.**

**Why This Assumption?**
- Configurations drift over time (systems change, backups break silently)
- Documentation becomes outdated (procedures written 2 years ago may not work today)
- Human knowledge decays (people forget, people leave, new people join)
- Dependencies change (system A now depends on system B, not documented)
- Assumptions are wrong (restore takes 8 hours, not 2 hours as assumed)

**Only testing reveals truth.**

### 1.3 Testing as Risk Reduction

Every test that reveals a gap is a **success**, not a failure:
- Gap found in test → Can be fixed before real disaster
- Gap not found in test, discovered in real disaster → Business impact, potential catastrophe

**Failed tests should be celebrated** for revealing issues when stakes are low.

### 1.4 Multi-Layered Testing Approach

[Organization] implements multiple types of tests, each with different risk/value profiles:

| Test Type | Risk to Production | Cost | Value | Frequency |
|-----------|-------------------|------|-------|-----------|
| **Component Testing** (restore single file) | Very Low | Low | Medium | Monthly |
| **System Testing** (restore full system) | Low | Medium | High | Quarterly |
| **Failover Testing** (test redundancy) | Low-Medium | Medium | High | Quarterly |
| **Tabletop Exercise** (discussion) | None | Very Low | Medium | Quarterly |
| **Full DR Simulation** (end-to-end) | Medium | High | Very High | Annual |

Layered approach balances thoroughness with practicality.

---

## 2. Backup Testing Methodology (A.8.13)

### 2.1 Backup Test Types

**2.1.1 File-Level Restore Test**

**Purpose:** Verify ability to restore individual files or small datasets

**Procedure:**
1. Select representative files from backup (vary file types, sizes, ages)
2. Initiate restore from backup solution
3. Compare restored files to originals (checksum validation)
4. Verify file integrity (can files be opened/used?)
5. Measure restore time
6. Document results

**Success Criteria:**
- Restored files match originals (byte-for-byte)
- Files are accessible and usable
- Restore completed within expected time

**Frequency:**
- Critical systems: Monthly minimum
- Important systems: Quarterly minimum
- Standard systems: Semi-annually

**2.1.2 System-Level Restore Test**

**Purpose:** Verify ability to restore complete systems

**Procedure:**
1. Select system for restore test (ideally in isolated test environment)
2. Document pre-restore state (as baseline)
3. Initiate full system restore from backup
4. Restore OS, applications, configurations, data
5. Verify system boots and operates
6. Verify application functionality (test core functions)
7. Verify data integrity (database consistency checks)
8. Measure total restore time
9. Document results and issues

**Success Criteria:**
- System fully operational after restore
- All applications functional
- Data integrity verified
- Restore time within RTO requirement

**Frequency:**
- Critical systems: Quarterly minimum
- Important systems: Semi-annually
- Standard systems: Annually

**2.1.3 Cross-Platform Restore Test**

**Purpose:** Verify ability to restore to different hardware/platform (DORA requirement: "restore to different locations")

**Procedure:**
1. Backup from production environment
2. Restore to different platform:
   - Physical to virtual (or vice versa)
   - On-premises to cloud
   - Different hardware generation
   - Different geographic location
3. Verify functionality on new platform
4. Document any compatibility issues

**Success Criteria:**
- System functional on alternate platform
- Data accessible and intact
- Documented procedure for alternate-platform restore

**Frequency:**
- Critical systems: Annually
- Required for DORA-regulated systems

**2.1.4 Application-Level Restore Test**

**Purpose:** Verify backup includes all application dependencies

**Procedure:**
1. Restore application and all dependencies (database, configs, integrations)
2. Test complete workflow (end-to-end transaction)
3. Verify integrations work (API calls, database connections)
4. Identify missing dependencies

**Success Criteria:**
- Application fully functional after restore
- All integrations operational
- No missing dependencies

**Frequency:** Quarterly for critical business applications

### 2.2 Restore Testing Without Production Impact

**2.2.1 Isolated Test Environment**

**Approach:** Restore to completely separate test environment
- Separate network (no connectivity to production)
- Separate storage
- Dedicated test servers/VMs

**Advantages:**
- Zero risk to production
- Can test destructively
- Can leave test environment running for extended validation

**Disadvantages:**
- Requires dedicated infrastructure
- May not exactly replicate production environment

**2.2.2 Cloud Restore Testing**

**Approach:** Restore production backups to cloud test environment
- Use cloud provider's isolated networks (VPCs)
- Spin up temporary infrastructure
- Run tests
- Destroy test environment after completion

**Advantages:**
- Cost-effective (pay only during test)
- Easy to replicate production scale
- Geographic diversity testing (restore to different region)

**Disadvantages:**
- Data transfer costs and time
- Requires cloud connectivity

**2.2.3 Snapshot-Based Testing**

**Approach:** Take production snapshot, restore backup over snapshot in isolated environment

**Advantages:**
- Production-identical environment
- Can compare restore to production snapshot (validate data integrity)

**Disadvantages:**
- Requires snapshot capability
- Snapshot may impact production performance

### 2.3 Backup Verification Beyond Restore Testing

**2.3.1 Automated Backup Validation**

Some backup solutions offer automated validation:
- Veeam SureBackup: Automatically boots restored VM and runs tests
- Synthetic full backup validation
- Backup chain integrity checks

**Automated validation complements but does not replace manual restore testing.**

**2.3.2 Backup Integrity Monitoring**

Continuous verification:
- Checksum validation during backup creation
- Periodic integrity scans of backup repository
- Automated alerts on corrupted backups
- Backup chain completeness checks (full + all incrementals present)

**2.3.3 Recovery Verification Testing**

Beyond restore, verify recovery:
- Can users access restored data?
- Are permissions correct?
- Are application functions working?
- Is performance acceptable?

**Recovery is not complete until business function is restored, not just data.**

### 2.4 Backup Test Documentation

Every backup restore test shall be documented with:

**Test Metadata:**
- Test ID (unique identifier)
- Test date and time
- Tester name
- System tested
- Test type (file/system/cross-platform/application)

**Test Details:**
- Backup date/time of backup being restored (RPO verification)
- Restore start time
- Restore completion time
- Actual restore duration (RTO verification)

**Test Results:**
- Result: Success / Partial Success / Failure
- Data integrity verification: Pass / Fail
- Application functionality verification: Pass / Fail
- Issues encountered (errors, warnings, unexpected behavior)

**Metrics:**
- Data volume restored (GB)
- Restore speed (GB/hour)
- RPO achieved (how old was restored data?)
- RTO achieved (how long did restore take?)

**Remediation (if test failed):**
- Root cause analysis
- Remediation plan
- Remediation owner
- Target remediation date
- Retest scheduled date

**Evidence:**
- Screenshots of restore process
- Log files
- Verification reports
- Test report signed by tester

Documentation stored in centralized repository for audit access.

---

## 3. Redundancy Testing Methodology (A.8.14)

### 3.1 Failover Test Types

**3.1.1 Planned Failover Test**

**Purpose:** Verify failover mechanism works in controlled scenario

**Procedure:**
1. Schedule maintenance window (announce to stakeholders)
2. Document pre-failover state (primary system status)
3. Initiate graceful shutdown of primary system
4. Monitor failover to secondary system
5. Verify secondary system operational
6. Test system functionality under secondary
7. Measure failover time
8. Fail back to primary (test failback)
9. Document results

**Success Criteria:**
- Failover completed successfully
- Failover time within RTO requirement
- No data loss (RPO = 0 for redundancy)
- Secondary system fully functional
- Failback successful

**Frequency:**
- Critical systems: Quarterly minimum
- Important systems: Semi-annually

**3.1.2 Unplanned Failover Simulation**

**Purpose:** Verify failover works when primary fails suddenly (worst-case scenario)

**Procedure:**
1. Schedule test (but simulate "unplanned" failure)
2. Suddenly terminate primary system (hard shutdown, network disconnect)
3. **Do not** gracefully shut down (simulates crash/failure)
4. Monitor automatic failover (if configured)
5. Verify detection time (how long until failure detected?)
6. Verify failover time (how long until secondary operational?)
7. Check for data loss or corruption
8. Document results

**Success Criteria:**
- Automatic failover triggered correctly
- Detection within expected time (health check frequency)
- Failover within RTO
- No data loss beyond acceptable RPO

**Frequency:**
- Critical systems with automatic failover: Annually minimum
- Recommended for all critical systems

**Risk Warning:** More disruptive than planned failover. Requires careful coordination.

**3.1.3 Component Failover Test**

**Purpose:** Test redundancy of individual components without full system failover

**Procedure:**
1. Identify redundant component (e.g., one server in cluster, one network path)
2. Disable component (shutdown, disconnect)
3. Verify system continues operating
4. Verify performance degradation acceptable (if any)
5. Re-enable component
6. Verify component rejoins cluster/pool

**Success Criteria:**
- System continues operating with component disabled
- No service interruption
- Component successfully rejoins

**Frequency:**
- Critical infrastructure: Quarterly
- Can often be done with minimal production impact

**3.1.4 Geographic Failover Test**

**Purpose:** Test ability to failover from primary site to secondary site

**Procedure:**
1. Coordinate with both sites (complex test requiring significant planning)
2. Simulate primary site unavailability
3. Failover all critical systems to secondary site
4. Verify systems operational at secondary site
5. Verify network connectivity from users to secondary site
6. Test business operations from secondary site
7. Measure failover time
8. Fail back to primary site
9. Document results

**Success Criteria:**
- All critical systems operational at secondary site
- Failover within RTO
- Business operations possible from secondary site
- Failback successful

**Frequency:**
- Annual minimum for systems with geographic redundancy
- Most complex and expensive test

### 3.2 Failover Testing Without Production Impact

**3.2.1 Blue-Green Testing**

**Approach:**
- Maintain two identical production environments (Blue = current, Green = standby)
- Failover traffic from Blue to Green
- Validate Green
- Either keep Green as new production or fail back to Blue

**Advantages:**
- Low risk (can fail back immediately if issues)
- Tests full failover including network routing

**3.2.2 Canary Testing**

**Approach:**
- Route small percentage of traffic (5-10%) to secondary system
- Monitor for issues
- Gradually increase traffic percentage
- If issues detected, route traffic back to primary

**Advantages:**
- Minimal impact if issues occur
- Suitable for Active-Active architectures

**3.2.3 Maintenance Window Testing**

**Approach:**
- Schedule failover test during planned maintenance window
- Accept brief service interruption (pre-announced)
- Most common approach for Active-Passive systems

### 3.3 Performance Testing Under Failover

Failover testing should include performance validation:

**Performance Metrics:**
- Response time (is it acceptable under failover?)
- Throughput (can secondary handle production load?)
- Concurrent users (capacity sufficient?)
- Database query performance

**Degraded Mode Acceptance:**
- Some performance degradation may be acceptable during failover
- Define acceptable degradation thresholds (e.g., 2x normal response time acceptable for 24 hours)
- Verify degradation is within acceptable bounds

### 3.4 Failover Test Documentation

Every failover test shall be documented with:

**Test Metadata:**
- Test ID, date, tester, system tested
- Test type (planned/unplanned/component/geographic)

**Test Details:**
- Failover trigger time
- Failure detection time (for automatic failover)
- Failover completion time
- Total failover duration (RTO verification)

**Test Results:**
- Result: Success / Partial Success / Failure
- Detection time (automatic failover)
- Failover time (within RTO?)
- Data loss (any data lost during failover?)
- Performance under failover (acceptable?)
- Issues encountered

**Failback Results:**
- Failback successful? (Yes/No)
- Failback time
- Data synchronization issues?

**Metrics:**
- Actual RTO achieved
- RPO verified (data loss measured)
- Performance degradation (if any)

**Remediation:**
- Issues identified
- Root cause analysis
- Remediation plan and owner
- Retest scheduled

Documentation stored for audit.

---

## 4. ICT BC Testing Methodology (A.5.30)

### 4.1 Scenario-Based DR Testing

**4.1.1 Tabletop Exercise**

**Format:** Discussion-based walkthrough (no actual recovery)

**Procedure:**
1. **Scenario Development:**
   - Create realistic disaster scenario (e.g., "Ransomware encrypts primary datacenter")
   - Provide scenario details to participants in advance
2. **Exercise Execution:**
   - Facilitator presents scenario
   - Participants walk through response step-by-step
   - Discuss decisions: "What would we do now?"
   - Identify actions, communication, resource needs
3. **Discussion Topics:**
   - Who would be notified?
   - What recovery procedures would be executed?
   - What resources would be needed?
   - What are potential issues or gaps?
4. **Documentation:**
   - Decisions made
   - Gaps identified
   - Action items for plan improvements

**Success Criteria:**
- All participants understand their roles
- Response procedures are clear
- Gaps identified and documented
- Action items created for improvements

**Advantages:**
- Very low risk (no actual systems affected)
- Low cost (2-4 hours of participant time)
- Builds familiarity with plans

**Frequency:** Quarterly

**4.1.2 Walkthrough**

**Format:** Step-through of procedures (semi-operational)

**Procedure:**
1. Select specific recovery procedure to test
2. Assemble technical team
3. Step through procedure line-by-line
4. Verify each step:
   - Do we have access to required tools?
   - Are credentials available?
   - Is documentation accurate?
   - Are commands correct?
5. Don't actually execute (just verify procedure completeness)

**Success Criteria:**
- Procedure is complete (no missing steps)
- All required resources are available
- Procedure is accurate and up-to-date

**Frequency:** Semi-annually for critical procedures

**4.1.3 Full Simulation / DR Exercise**

**Format:** Comprehensive test executing actual recovery

**Procedure:**
1. **Planning Phase (4-6 weeks before):**
   - Select scenario (site loss, prolonged outage, cyber incident)
   - Define scope (which systems to recover)
   - Coordinate participants (recovery teams, business, vendors)
   - Prepare test environment (DR site, cloud environment)
   - Communicate to stakeholders
2. **Execution Phase (4-8 hours or multi-day):**
   - Activate crisis management team
   - Execute recovery procedures
   - Recover systems per recovery plan
   - Test communications (internal, external)
   - Test business process recovery (can business operate?)
   - Measure recovery times
3. **Validation Phase:**
   - Verify systems operational
   - Test end-to-end workflows
   - Verify data integrity
   - Test user access
4. **Debrief Phase (within 1 week):**
   - Gather all participants
   - Review what worked and what didn't
   - Document lessons learned
   - Create improvement plan

**Success Criteria:**
- Critical systems recovered within RTO
- Data recovered within RPO
- Business processes can operate from DR environment
- Communications effective
- All participants executed their roles

**Frequency:** Annual minimum

**Cost:** High (infrastructure, participant time, potential service disruption)

**Value:** Highest (most realistic test, end-to-end validation)

### 4.2 Scenario Development Guidelines

**Realistic Scenarios:**
- Based on actual threats (ransomware is realistic, alien invasion is not)
- Appropriate scope (don't test recovering 200 systems in 4-hour exercise)
- Include complications (not everything works perfectly)

**Varied Scenarios Over Time:**
- Year 1: Site loss (fire/flood)
- Year 2: Cyber incident (ransomware)
- Year 3: Prolonged cloud provider outage
- Year 4: Multiple simultaneous failures
- Year 5: Supply chain disruption

**Scenario Complexity:**
- Start simple (single system recovery)
- Increase complexity over time (multi-system, multi-site)
- Challenge teams (inject complications during exercise)

**Example Scenarios:**

**Scenario 1: "Datacenter Fire"**
- Primary datacenter suffers fire, completely unavailable
- No advance warning
- Must recover to secondary datacenter or cloud
- RTO: 24 hours for critical systems

**Scenario 2: "Ransomware Attack"**
- Ransomware encrypts production systems and primary backups
- Offline/immutable backups remain available
- Must restore from offline backups
- RPO: 24 hours (last offline backup)
- RTO: 48 hours (restore is slow)

**Scenario 3: "Cloud Provider Regional Outage"**
- Primary cloud region unavailable for 8+ hours
- Must failover to secondary region
- RTO: 4 hours
- Test geographic redundancy

### 4.3 Participant Coordination

**Mandatory Participants:**
- BC/DR Coordinator (leads exercise)
- Technical Recovery Teams (execute procedures)
- Business Process Owners (validate business recovery)

**Optional but Recommended:**
- Executive management (observe, understand risks)
- Third-party vendors (if recovery depends on them)
- External auditors (if invited to observe)

**Observer Roles:**
- Facilitators (ensure exercise runs smoothly, inject scenario updates)
- Evaluators (assess performance, identify gaps)
- Note-takers (document exercise, capture issues)

### 4.4 DR Exercise Documentation

**Pre-Exercise:**
- Exercise plan (objectives, scenario, scope, schedule)
- Participant list (roles, contact info)
- Success criteria

**During Exercise:**
- Timeline (what happened when)
- Decisions made
- Issues encountered
- Recovery metrics (time to restore each system)

**Post-Exercise:**
- Executive summary (high-level results)
- Detailed findings (what worked, what didn't)
- Lessons learned
- Gaps identified
- Recommendations
- Improvement plan (action items with owners and deadlines)

---

## 5. RPO/RTO Compliance Assessment

### 5.1 RPO Compliance Measurement

**RPO Compliance Question:** Does backup frequency meet or exceed RPO requirement?

**Measurement:**
- **RPO Requirement:** (hours) - from BIA
- **Actual Backup Frequency:** (hours) - from backup configuration
- **Compliance Status:**
  - If Backup Frequency ≤ RPO Requirement → **Compliant** ✅
  - If Backup Frequency > RPO Requirement → **Non-Compliant** ❌

**Example:**
- System A: RPO Requirement = 4 hours, Backup Frequency = 2 hours → Compliant ✅
- System B: RPO Requirement = 4 hours, Backup Frequency = 24 hours → Non-Compliant ❌ (Gap = 20 hours)

**Gap Calculation:**
- RPO Gap = Backup Frequency - RPO Requirement
- Gap represents potential data loss beyond acceptable level

**Trending:**
- Track RPO compliance over time
- Target: 100% of Critical systems compliant, 90% overall

### 5.2 RTO Compliance Measurement

**RTO Compliance Question:** Can system be restored within RTO requirement?

**Measurement:**
- **RTO Requirement:** (hours) - from BIA
- **Actual Recovery Time:** (hours) - measured during testing
  - For systems with redundancy: Actual Failover Time
  - For systems without redundancy: Actual Restore Time from backup
- **Compliance Status:**
  - If Actual Recovery Time ≤ RTO Requirement → **Compliant** ✅
  - If Actual Recovery Time > RTO Requirement → **Non-Compliant** ❌

**Example:**
- System A: RTO Requirement = 4 hours, Failover Time = 0.5 hours → Compliant ✅
- System B: RTO Requirement = 4 hours, Restore Time = 8 hours → Non-Compliant ❌ (Gap = 4 hours)

**Gap Calculation:**
- RTO Gap = Actual Recovery Time - RTO Requirement
- Gap represents downtime beyond acceptable level

**Critical Note:** Actual recovery time must be **measured through testing**, not assumed.

### 5.3 Combined RPO/RTO Compliance

**Overall Compliance Status per System:**
- **Fully Compliant:** Both RPO and RTO met ✅✅
- **Partial Compliance:** Only RPO or only RTO met ⚠️
- **Non-Compliant:** Neither RPO nor RTO met ❌❌

**Organizational Metrics:**
- % systems fully compliant (both RPO and RTO)
- % systems partially compliant
- % systems non-compliant

**Target:** ≥90% overall fully compliant, 100% of Critical systems fully compliant

### 5.4 Compliance Trending

Track compliance over time:
- Quarter-over-quarter trends (improving/stable/degrading)
- Newly identified gaps (new systems, changed requirements)
- Remediated gaps (closed since last assessment)
- Open gaps (still requiring remediation)

Trend analysis helps identify:
- Systemic issues (are gaps increasing overall?)
- Successful remediation efforts (gaps closing)
- Need for additional investment

---

## 6. Evidence Collection Requirements

### 6.1 Evidence Types per Control

**6.1.1 Evidence for A.8.13 (Information Backup)**

**Configuration Evidence:**
- Backup policy documentation
- Backup schedules (documented configurations)
- Backup retention policies
- Backup scope documentation (what is backed up)
- Backup solution architecture diagrams

**Operational Evidence:**
- Backup job logs (success/failure for sample period - e.g., last 30 days)
- Backup monitoring dashboards (screenshots)
- Backup storage utilization reports
- Failed backup reports and remediation tracking

**Testing Evidence:**
- Restore test results (all tests conducted in last 12 months)
- Restore test documentation (procedure followed, results, issues)
- Evidence of successful restores (screenshots, verification reports)
- Remediation tracking for failed tests

**Compliance Evidence:**
- RPO compliance reports (from Assessment Workbook 1)
- Backup coverage reports (% systems backed up)
- Testing compliance reports (% systems tested on schedule)

**Regulatory Evidence (DORA/NIS2 if applicable):**
- Immutability implementation documentation
- Offsite backup verification
- Encryption implementation verification (at-rest and in-transit)
- Restore to different locations test results

**6.1.2 Evidence for A.8.14 (Redundancy)**

**Architecture Evidence:**
- Redundancy architecture diagrams
- SPOF analysis documentation
- Redundancy design decisions (why this architecture chosen)

**Implementation Evidence:**
- Failover configuration documentation
- Health check configurations
- Geographic redundancy verification (multi-site deployment evidence)

**Testing Evidence:**
- Failover test results (all tests conducted in last 12 months)
- Failover test documentation (procedure, results, issues)
- Evidence of successful failovers (logs, screenshots)
- Performance testing results (under failover)

**Compliance Evidence:**
- RTO compliance reports (from Assessment Workbook 2)
- SPOF mitigation status (from SPOF register)
- Testing compliance reports (% systems tested on schedule)

**6.1.3 Evidence for A.5.30 (ICT BC Readiness)**

**Planning Evidence:**
- Business Impact Analysis documentation
- BC/DR strategy document
- ICT Recovery Plans (current versions)
- Plan approval records (signed by stakeholders)

**Governance Evidence:**
- BC/DR Steering Committee meeting minutes
- Quarterly BC/DR status reports
- Budget allocation for BC/DR
- Risk acceptance documentation (for known gaps)

**Training Evidence:**
- Training materials (current versions)
- Training attendance records
- Knowledge assessment results (if conducted)

**Testing Evidence:**
- Tabletop exercise results
- Walkthrough results
- Full DR simulation results
- Lessons learned documentation
- Improvement action tracking

**Gap Management Evidence:**
- Gap register (all identified gaps)
- Remediation tracking (status, owner, timeline)
- Risk acceptance approvals (executive sign-off)

**Supplier Management Evidence:**
- Supplier BC assessment results
- Supplier SLA review
- Supplier testing participation records

### 6.2 Evidence Retention Requirements

All BC/DR evidence shall be retained:
- **Minimum:** 3 years (standard audit retention)
- **Regulatory:** As required by applicable regulations
  - DORA: May require longer retention
  - NIS2: Incident-related evidence per directive
- **Best Practice:** 5 years for critical evidence

**Evidence Storage:**
- Centralized evidence repository (document management system)
- Access controls (only authorized personnel)
- Version control (track changes over time)
- Backup of evidence (evidence itself should be backed up!)

### 6.3 Evidence Organization for Audit

Evidence should be organized for easy audit access:

**Folder Structure Example:**
```
BC_DR_Evidence/
├── A.8.13_Backup/
│   ├── Configuration/
│   ├── Operational_Logs/
│   ├── Testing/
│   └── Compliance_Reports/
├── A.8.14_Redundancy/
│   ├── Architecture/
│   ├── Testing/
│   └── Compliance_Reports/
├── A.5.30_ICT_BC/
│   ├── BIA/
│   ├── Plans/
│   ├── Governance/
│   ├── Training/
│   ├── Testing/
│   └── Gaps/
└── Assessment_Workbooks/
    ├── WB1_Backup_Inventory/
    ├── WB2_Redundancy_Analysis/
    ├── WB3_RPO_RTO_Compliance/
    ├── WB4_Testing_Results/
    └── Dashboard/
```

**Evidence Index:**
- Master evidence index (spreadsheet or database)
- Maps audit requirements to evidence location
- Facilitates rapid evidence retrieval during audit

### 6.4 Evidence Presentation to Auditors

When presenting evidence to auditors:

**Be Prepared:**
- Evidence pre-organized and easily accessible
- Evidence index ready (shows what evidence exists and where)
- Key stakeholders available (BC/DR Coordinator, technical leads)

**Present Systematically:**
- Start with overview (BC/DR strategy, framework)
- Show governance (BIA, plans, steering committee minutes)
- Show implementation (backup configs, redundancy architecture)
- Show testing (test results, lessons learned, remediation)
- Show compliance (assessment workbooks, dashboards, metrics)

**Be Honest:**
- If gaps exist, acknowledge them openly
- Show gap remediation plan
- Show progress on closing gaps
- Don't try to hide issues (auditors will find them anyway)

**Demonstrate Continuous Improvement:**
- Show how testing reveals gaps
- Show how gaps are remediated
- Show improvement trends over time

---

## 7. Compliance Scoring Methodology

### 7.1 Scoring Dimensions

[Organization] measures BC/DR compliance across multiple dimensions:

**Dimension 1: Coverage**
- **Question:** Are systems in scope actually backed up / have redundancy?
- **Measurement:** (Systems with backup/redundancy) / (Total in-scope systems) × 100%

**Dimension 2: Compliance with Requirements**
- **Question:** Do capabilities meet business requirements (RPO/RTO)?
- **Measurement:** (Systems meeting RPO/RTO) / (Total systems) × 100%

**Dimension 3: Testing**
- **Question:** Are systems tested on schedule?
- **Measurement:** (Systems tested within frequency) / (Systems requiring testing) × 100%

**Dimension 4: Gap Remediation**
- **Question:** Are identified gaps being closed?
- **Measurement:** (Gaps remediated or accepted) / (Total gaps) × 100%

### 7.2 Weighting by Criticality

Not all systems are equal. Scoring should weight by criticality:

**Criticality Weights:**
- Critical systems: 3× weight
- Important systems: 2× weight
- Standard systems: 1× weight
- Low-criticality systems: 0.5× weight (or excluded)

**Example Calculation:**
- 10 Critical systems, 8 compliant → Score = (8/10) × 3 = 2.4
- 20 Important systems, 16 compliant → Score = (16/20) × 2 = 1.6
- 30 Standard systems, 24 compliant → Score = (24/30) × 1 = 0.8
- **Total Weighted Score:** (2.4 + 1.6 + 0.8) / (3 + 2 + 1) = 4.8 / 6 = 80%

This ensures critical systems have more impact on overall score.

### 7.3 Overall BC/DR Maturity Score

**Overall Score Calculation:**

```
Overall BC/DR Maturity Score = 
  (Coverage Score × 30%) +
  (RPO/RTO Compliance Score × 30%) +
  (Testing Compliance Score × 20%) +
  (Gap Remediation Score × 10%) +
  (Documentation/Training Score × 10%)
```

**Maturity Levels:**
- **Level 1 - Initial** (0-60%): Ad hoc, reactive, significant gaps
- **Level 2 - Managed** (60-75%): Basic capabilities, gaps known and tracked
- **Level 3 - Defined** (75-90%): Comprehensive capabilities, regular testing, governance established
- **Level 4 - Optimized** (90-100%): Continuous improvement, automation, proactive

**Interpretation:**
- Below 60%: Significant risk, immediate action required
- 60-75%: Basic compliance, focus on closing gaps
- 75-90%: Good maturity, continue improvement
- Above 90%: Excellent maturity, maintain and optimize

### 7.4 Trend Scoring

In addition to absolute score, track **trends**:

**Trend Calculation:**
- Current Quarter Score - Previous Quarter Score = Trend
- Positive trend (improving): +5% or more
- Stable (maintaining): -5% to +5%
- Negative trend (degrading): -5% or more

**Trend Interpretation:**
- Improving trend: Remediation efforts working, continue
- Stable trend: Maintaining current level, ensure no complacency
- Degrading trend: Red flag, investigate why (new systems without BC/DR? tests failing? gaps increasing?)

---

## 8. Gap Analysis Methodology

### 8.1 Gap Identification

Gaps are identified through multiple sources:

**Source 1: Requirements vs. Capabilities Assessment**
- Compare BIA requirements to technical capabilities
- Gap = where capability < requirement
- Examples: RPO gap, RTO gap, coverage gap

**Source 2: Testing**
- Failed tests reveal gaps (backup doesn't restore, failover doesn't work)
- Longer-than-expected recovery times reveal gaps (RTO not achievable)

**Source 3: SPOF Analysis**
- Identified SPOFs without mitigation = gaps

**Source 4: Audit Findings**
- Internal or external audits may identify gaps (missing documentation, untested systems)

**Source 5: Incident Reviews**
- Actual incidents reveal gaps in real-world conditions

### 8.2 Gap Categorization

Gaps should be categorized for prioritization:

**Gap Type:**
- **Coverage Gap:** System has no backup/redundancy at all
- **RPO Gap:** Backup frequency doesn't meet RPO requirement
- **RTO Gap:** Recovery time exceeds RTO requirement
- **Testing Gap:** System not tested on schedule (or never tested)
- **Documentation Gap:** Plans/procedures missing or outdated
- **SPOF Gap:** Identified SPOF not mitigated
- **Regulatory Gap:** DORA/NIS2 requirement not met (immutability, offsite, etc.)

**Gap Severity:**
- **Critical:** Gap in Critical system, high business impact
- **High:** Gap in Important system or significant gap in Critical system
- **Medium:** Gap in Standard system or minor gap in Important system
- **Low:** Gap in Low-criticality system

### 8.3 Gap Prioritization Framework

**Prioritization Formula:**
```
Gap Risk Score = Criticality × Gap Severity × Likelihood of Incident
```

**Criticality:**
- Critical system = 10 points
- Important system = 5 points
- Standard system = 2 points
- Low-criticality system = 1 point

**Gap Severity:**
- No backup/redundancy = 10 points
- RPO/RTO gap > 50% of requirement = 7 points
- RPO/RTO gap 25-50% of requirement = 4 points
- RPO/RTO gap < 25% of requirement = 2 points
- Testing gap = 3 points
- Documentation gap = 1 point

**Likelihood:**
- High likelihood (frequent failures, high risk) = 3×
- Medium likelihood = 2×
- Low likelihood (rare failures, low risk) = 1×

**Priority Levels:**
- Risk Score > 200 → **Critical Priority** (remediate within 90 days)
- Risk Score 100-200 → **High Priority** (remediate within 6 months)
- Risk Score 50-100 → **Medium Priority** (remediate within 1 year)
- Risk Score < 50 → **Low Priority** (remediate as resources permit or accept risk)

### 8.4 Gap Remediation Tracking

All gaps shall be tracked in Gap Register:

**Gap Register Fields:**
- Gap ID (unique identifier)
- Gap description
- Gap type (coverage, RPO, RTO, testing, SPOF, etc.)
- System affected
- System criticality
- Gap severity
- Risk score (calculated)
- Priority level
- Business impact (if gap not remediated)
- Remediation plan (how gap will be closed)
- Remediation owner (responsible person)
- Target completion date
- Status (Open, In Progress, Complete, Risk Accepted, Deferred)
- Actual completion date
- Verification (how remediation will be verified - typically retest)

**Gap Review Cadence:**
- Monthly review by BC/DR Coordinator (track progress)
- Quarterly review by BC/DR Steering Committee (escalate blocked items)

### 8.5 Risk Acceptance Process

Some gaps may be accepted rather than remediated:

**Acceptable Reasons:**
- Cost of remediation exceeds cost of risk
- Technical infeasibility (no solution exists)
- Temporary gap (remediation in progress)
- Compensating controls reduce risk sufficiently

**Risk Acceptance Requirements:**
- Risk documented in enterprise risk register
- Business owner approves risk (not IT decision alone)
- Executive management approves for critical gaps
- Risk acceptance reviewed annually
- Risk acceptance expires if conditions change

**Unacceptable Gaps for Risk Acceptance:**
- Critical system with no backup (data loss catastrophic)
- Critical system RTO gap > 50% (downtime unacceptable)
- Regulatory compliance gap (DORA/NIS2 violation)

---

## 9. Continuous Testing Approach

### 9.1 Shift from Periodic to Continuous

**Traditional Approach:** Test once per year, forget about it until next year

**Continuous Approach:** Testing integrated into operations

**Benefits of Continuous Testing:**
- Catch issues earlier (don't wait 12 months to discover backup is broken)
- Smaller, more frequent tests are less risky than large annual tests
- Builds culture of preparedness (testing becomes normal, not special event)
- Automated testing reduces manual effort

### 9.2 Automated vs. Manual Testing

**Automated Testing:**
- Backup verification (automated integrity checks, synthetic restores)
- Health checks (continuous monitoring of redundancy)
- Automated failover testing (in test environments)

**Manual Testing:**
- Full restore tests (requires human validation of functionality)
- DR simulations (requires human decision-making)
- Tabletop exercises (inherently discussion-based)

**Balance:** Automate what can be automated, manually test what requires human judgment.

### 9.3 Testing Integration with Change Management

**Test After Changes:**
- New system deployed → Test backup and recovery before production
- Infrastructure change (network, storage) → Retest failover
- Application update → Verify backup includes new components

**Regression Testing:**
- After remediation of failed test → Retest to verify fix
- After plan updates → Walkthrough to verify changes correct

**Continuous Integration/Continuous Deployment (CI/CD) Integration:**
- Automated backup verification as part of deployment pipeline
- Infrastructure-as-Code changes trigger automated DR tests

### 9.4 Real-Time Compliance Monitoring

**Dashboard Approach:**
- Real-time backup success/failure monitoring
- Continuous RPO/RTO compliance calculation
- Automated alerts when compliance drops below threshold

**Example Alerts:**
- Alert when Critical system backup fails (immediate)
- Alert when RPO compliance for Critical systems < 95% (daily)
- Alert when test becomes overdue (weekly)

**Continuous Monitoring ≠ Continuous Testing** but monitoring informs testing priorities.

---

## 10. Reporting and Dashboards

### 10.1 Dashboard Requirements

**10.1.1 Operational Dashboard (Daily/Real-Time)**

**Audience:** IT Operations, BC/DR Coordinator

**Metrics:**
- Backup jobs (last 24 hours): Success count, Failure count
- Critical backup failures (require immediate action)
- Backup storage utilization (% full, trend)
- Redundancy status (systems operational, failover capable)
- Overdue tests (systems requiring testing)

**Refresh:** Real-time or hourly

**Purpose:** Day-to-day monitoring, rapid issue identification

**10.1.2 Management Dashboard (Monthly)**

**Audience:** IT Management, Business Unit Leaders

**Metrics:**
- Overall BC/DR maturity score
- RPO compliance (%)
- RTO compliance (%)
- Backup coverage (%)
- Testing compliance (%)
- Gap count (by priority: Critical, High, Medium, Low)
- Trend arrows (improving ↗, stable →, degrading ↘)

**Refresh:** Monthly

**Purpose:** Management oversight, trend identification, resource allocation decisions

**10.1.3 Executive Dashboard (Quarterly)**

**Audience:** CISO, CIO, Executive Management, Board

**Metrics:**
- Overall BC/DR readiness (single number/status: Green/Yellow/Red)
- Critical gaps count (gaps in Critical systems)
- Top 5 risks (highest-priority gaps)
- Compliance trends (quarter-over-quarter)
- Budget status (BC/DR spending vs. plan)
- Upcoming tests (next quarter)
- Regulatory compliance status (DORA, NIS2 if applicable)

**Refresh:** Quarterly (or more frequent during crisis)

**Purpose:** Executive visibility, strategic decisions, risk acceptance

### 10.2 Reporting Cadence

**Daily:**
- Automated backup success/failure summary (email to operations team)

**Weekly:**
- Failed backup summary (requiring remediation)
- Overdue test summary

**Monthly:**
- BC/DR compliance summary report (to management)
- Gap remediation status report
- Testing summary (tests conducted, results)

**Quarterly:**
- Comprehensive BC/DR status report (to BC/DR Steering Committee)
- Assessment workbooks updated (WB1-4, Dashboard)
- Executive presentation (to CISO, CIO)

**Annually:**
- Annual BC/DR program review (to executive management)
- BIA review results
- Strategy review and updates

### 10.3 Escalation Reporting

**Escalation Triggers:**
- Critical backup failure (Critical system backup failed)
- Failed recovery test (system cannot be recovered)
- RTO/RPO compliance drops below threshold (< 90% for Critical systems)
- Critical gap identified (new gap in Critical system)
- Test reveals major issue (DR simulation identifies multiple failures)

**Escalation Path:**
- **Level 1 (Operations):** BC/DR Coordinator, Operations Manager
- **Level 2 (Management):** IT Manager, CISO
- **Level 3 (Executive):** CIO, COO (if business impact significant)

**Escalation Timeframes:**
- Critical issues: Escalate immediately
- High priority issues: Escalate within 24 hours
- Medium priority: Escalate within weekly report

### 10.4 Reporting Best Practices

**Be Concise:**
- Executive reports: 1-2 pages maximum, focus on key metrics and decisions needed
- Management reports: 3-5 pages, more detail but still concise
- Operational reports: As detailed as needed for action

**Use Visualizations:**
- Charts and graphs convey trends better than tables
- Red/Yellow/Green status indicators for quick scanning
- Dashboards better than lengthy text reports

**Focus on Actionable Information:**
- Don't just report status, report what needs to be done
- Highlight gaps requiring decisions (resource allocation, risk acceptance)
- Provide recommendations, not just data

**Maintain Consistency:**
- Use same format report-to-report (allows comparison)
- Track same metrics over time (trend analysis)
- Don't change reporting methodology without good reason

---

## Conclusion

This Testing Methodology and Evidence Framework establishes the systematic approach [Organization] uses to verify BC/DR readiness and collect compliance evidence.

**Key Requirements Summary:**
✅ Testing is mandatory—untested capabilities are unreliable capabilities  
✅ Multiple test types balance risk, cost, and thoroughness  
✅ RPO/RTO compliance measured through actual testing, not assumptions  
✅ Comprehensive evidence collection supports audit readiness  
✅ Compliance scoring provides quantitative BC/DR maturity assessment  
✅ Gap analysis drives prioritized remediation  
✅ Continuous testing integrated into operations  
✅ Multi-level reporting provides visibility at all organizational levels  

**Testing Philosophy:**
This framework embraces the Feynman principle: "Don't fool yourself." Through systematic testing, evidence collection, and honest gap assessment, [Organization] ensures BC/DR readiness is real, not assumed.

**Integration Across Controls:**
- A.8.13: Backup testing proves recovery capability
- A.8.14: Failover testing proves redundancy works
- A.5.30: BC/DR scenario testing proves overall preparedness
- Combined: Evidence demonstrates complete BC/DR ecosystem functions

**Next Steps:**
1. Review and approve this testing and evidence framework
2. Implement testing schedules per this framework
3. Begin evidence collection per Section 6 requirements
4. Establish dashboards and reporting per Section 10
5. Conduct first round of testing per Sections 2-4
6. Complete assessment workbooks with test results

---

**Document End**

*"The first principle is that you must not fool yourself—and you are the easiest person to fool."* - Richard Feynman

*Test relentlessly. Collect evidence. Close gaps. Repeat.*

---

**APPROVAL SIGNATURES**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | | | |
| BC/DR Coordinator | | | |
| Quality Assurance Manager | | | |
| Compliance Officer | | | |

**Next Review Date:** [One year from approval date]