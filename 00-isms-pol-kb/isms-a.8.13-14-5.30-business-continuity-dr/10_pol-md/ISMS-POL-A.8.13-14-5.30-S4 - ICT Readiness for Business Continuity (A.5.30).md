# ISMS-POL-A.8.13-14-5.30-S4: ICT Readiness for Business Continuity (A.5.30)

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
| 1.0 | [Date] | Security Operations Manager / CISO | Initial ICT BC readiness requirements policy for A.5.30 |

---

## Table of Contents

1. [Control Focus: A.5.30](#1-control-focus-a530)
2. [Business Impact Analysis (BIA) Requirements](#2-business-impact-analysis-bia-requirements)
3. [BC/DR Strategy Requirements](#3-bcdr-strategy-requirements)
4. [ICT Recovery Plan Requirements](#4-ict-recovery-plan-requirements)
5. [Recovery Capability vs. Requirements Alignment](#5-recovery-capability-vs-requirements-alignment)
6. [BC/DR Awareness and Training](#6-bcdr-awareness-and-training)
7. [BC/DR Testing Requirements](#7-bcdr-testing-requirements)
8. [BC/DR Governance](#8-bcdr-governance)
9. [Supplier and Third-Party BC Requirements](#9-supplier-and-third-party-bc-requirements)
10. [Crisis Management Integration](#10-crisis-management-integration)
11. [Continuous Improvement](#11-continuous-improvement)
12. [Compliance Measurement](#12-compliance-measurement)

---

## 1. Control Focus: A.5.30

### 1.1 ISO 27001:2022 Control Text

**A.5.30 - ICT Readiness for Business Continuity**

> ICT readiness shall be planned, implemented, maintained and tested based on business continuity objectives and ICT continuity requirements.

**Purpose:**
To ensure that ICT systems are ready to support business continuity in the event of disruptions.

### 1.2 Control Objective

The objective of this control is to ensure that [Organization]'s Information and Communication Technology (ICT) infrastructure and services are prepared to support business continuity during disruptions through:
- Understanding business continuity requirements (Business Impact Analysis)
- Developing strategies and plans to meet those requirements
- Implementing technical capabilities (backup, redundancy) aligned with requirements
- Testing readiness through exercises and simulations
- Maintaining preparedness through governance and continuous improvement

### 1.3 Integration with A.8.13 and A.8.14

**A.5.30 is the overarching governance control** that ties together technical controls:

**A.5.30 (This Section):**
- **Defines requirements** through Business Impact Analysis (RPO/RTO)
- **Sets strategy** for how ICT will support business continuity
- **Governs implementation** of backup and redundancy
- **Tests overall readiness** through BC/DR exercises
- **Measures gaps** between requirements and capabilities

**A.8.13 (Backup):**
- **Implements capability** to recover data (meets RPO requirements defined by A.5.30)
- **Provides recovery mechanism** for data loss scenarios

**A.8.14 (Redundancy):**
- **Implements capability** for system availability (meets RTO requirements defined by A.5.30)
- **Provides recovery mechanism** for system failure scenarios

**Relationship:**
```
A.5.30 → Determines WHAT is needed (RPO/RTO requirements)
         ↓
A.8.13 + A.8.14 → Implements HOW to achieve it (backup + redundancy)
         ↓
A.5.30 → Verifies it works through testing and measures gaps
```

---

## 2. Business Impact Analysis (BIA) Requirements

### 2.1 BIA Purpose and Scope

**Business Impact Analysis (BIA)** is the foundational process that determines ICT continuity requirements. BIA identifies:
- Which business processes are most critical
- Impact of disruptions to those processes over time
- Maximum acceptable downtime (Maximum Tolerable Period of Disruption - MTPD)
- Recovery priorities and dependencies

**BIA Scope:**
- All business processes dependent on ICT
- All ICT systems and services
- Dependencies between systems and processes
- Third-party services and suppliers

### 2.2 BIA Methodology Requirements

[Organization] shall conduct BIA using a systematic methodology:

**2.2.1 Stakeholder Identification**
- Identify business process owners for all critical processes
- Identify IT system owners for all systems
- Identify key users and subject matter experts

**2.2.2 Impact Assessment**
BIA shall assess impact across multiple dimensions:

**Financial Impact:**
- Direct revenue loss ($/hour of downtime)
- Cost of recovery operations
- Penalties or fines (regulatory, contractual SLA breaches)
- Lost productivity costs

**Operational Impact:**
- Inability to perform critical business functions
- Degraded service quality
- Impact on customers (customer service, fulfillment)
- Impact on supply chain

**Reputational Impact:**
- Customer trust erosion
- Brand damage
- Media attention (negative publicity)
- Long-term customer loss

**Regulatory/Legal Impact:**
- Compliance violations
- Regulatory penalties
- Legal liability
- Contractual breaches

**Impact Over Time:**
BIA shall assess how impact **increases over time**:
- Hour 1-4: Minimal impact (operations can continue with workarounds)
- Hour 4-24: Moderate impact (significant disruption, customer complaints)
- Day 1-3: High impact (major revenue loss, regulatory concerns)
- Day 3+: Severe impact (existential threat, major customer loss)

This time-based assessment determines RTO requirements.

**2.2.3 Maximum Tolerable Period of Disruption (MTPD)**

MTPD is the **longest time** a business process can be disrupted before the organization faces severe consequences (business failure, irreversible damage).

**MTPD Determination:**
- Based on impact assessment over time
- Point where impact becomes unacceptable
- Sets upper bound for RTO (RTO must be < MTPD)

**Example:**
- E-commerce website MTPD = 4 hours (after 4 hours, customers abandon, competitors gain, reputation damaged)
- Internal reporting system MTPD = 7 days (can catch up on reporting after recovery)

**2.2.4 RPO and RTO Determination**

Based on impact assessment and MTPD:

**RPO (Recovery Point Objective):**
- Question: "How much data loss is acceptable?"
- Based on: Financial impact of recreating lost data, regulatory requirements, operational impact
- Example: Financial transactions RPO = 0 (no data loss acceptable); Daily report RPO = 24 hours

**RTO (Recovery Time Objective):**
- Question: "How quickly must system be restored?"
- Based on: MTPD, impact over time assessment
- RTO < MTPD (typically RTO = 50-75% of MTPD to provide buffer)
- Example: E-commerce MTPD = 4 hours → RTO = 2 hours

**2.2.5 Dependency Mapping**

BIA shall identify system interdependencies:
- **Upstream dependencies:** What does this system depend on? (databases, authentication, network)
- **Downstream dependencies:** What depends on this system? (applications, users, processes)
- **Hidden dependencies:** Often-overlooked dependencies (DNS, time servers, license servers)

**Dependency Considerations:**
- A system's RTO is constrained by its dependencies (can't restore system before dependencies are restored)
- Recovery sequence must account for dependencies (restore dependencies first)

### 2.3 BIA Documentation Requirements

BIA results shall be documented including:
- Executive summary (high-level findings, critical systems)
- Detailed impact assessment per business process/system
- MTPD, RPO, and RTO for each critical process/system
- Dependency maps
- Recovery priorities (sequence of recovery)

BIA documentation shall be approved by:
- Business process owners
- Executive management
- BC/DR Coordinator

### 2.4 BIA Update Frequency

BIA shall be reviewed and updated:
- **Annually** at minimum (scheduled review)
- **When significant business changes occur:**
  - New critical business processes
  - Major system implementations or retirements
  - Organizational restructuring
  - Mergers, acquisitions, divestitures
- **After major incidents** (lessons learned may change impact assessment)

Outdated BIA results in misaligned recovery capabilities.

---

## 3. BC/DR Strategy Requirements

### 3.1 Strategy Definition

**BC/DR Strategy** defines the high-level approach [Organization] will take to ensure ICT readiness for business continuity. Strategy translates BIA requirements into actionable plans.

**Strategy Components:**
- **Recovery strategies** for different system types (restore from backup, failover, manual workarounds)
- **Resource allocation** (budget, personnel, technology investments)
- **Organizational approach** (centralized BC/DR team, distributed responsibility)
- **Technology decisions** (cloud vs. on-premises, vendor selection)

### 3.2 Strategy Alignment with BIA

Strategy shall be **driven by BIA results**, not IT preferences:

**BIA → Strategy Examples:**

**Critical systems (RTO < 4 hours):**
- Strategy: Active-passive redundancy with automatic failover + hourly backups
- Rationale: RTO < 4 hours cannot be met with restore from backup alone (too slow)

**Important systems (RTO 4-24 hours):**
- Strategy: Daily backups + documented restore procedures + warm standby (optional)
- Rationale: RTO 4-24 hours achievable with efficient restore from backup

**Standard systems (RTO > 24 hours):**
- Strategy: Weekly backups + restore on-demand
- Rationale: RTO > 24 hours allows time for restore without redundancy investment

### 3.3 Cost-Benefit Considerations

BC/DR strategy shall balance **business requirements** with **cost constraints**:

**Cost of BC/DR Capabilities:**
- Redundancy is expensive (duplicate infrastructure, complexity)
- Offsite/cloud backups incur ongoing costs (storage, bandwidth)
- Testing requires time and resources

**Cost of Downtime:**
- Financial impact (from BIA)
- Reputational impact (from BIA)

**Decision Framework:**
- If Cost of Downtime > Cost of BC/DR → Invest in BC/DR
- If Cost of Downtime < Cost of BC/DR → Risk acceptance may be appropriate
- Business owner makes final decision (with full understanding of risks)

### 3.4 Multi-Strategy Approach

Different systems may require different strategies:
- Critical systems: High investment (redundancy, frequent backups, offsite, immutable)
- Important systems: Moderate investment (daily backups, documented procedures)
- Standard systems: Minimal investment (weekly backups, best effort recovery)

**This is appropriate and expected.** Not all systems warrant equal investment.

### 3.5 Strategy Approval and Communication

BC/DR strategy shall be:
- **Documented** in strategy document
- **Approved** by executive management (CISO, CIO, COO, CFO)
- **Communicated** to all stakeholders (IT, business owners, BC/DR team)
- **Reviewed annually** and updated as business requirements change

---

## 4. ICT Recovery Plan Requirements

### 4.1 Recovery Plan Purpose

**ICT Recovery Plans** (also called ICT Continuity Plans) document **how** [Organization] will recover ICT systems and services during a disruption.

Recovery plans translate strategy into **executable procedures**.

### 4.2 Plan Structure and Content

ICT Recovery Plans shall include:

**4.2.1 Plan Overview**
- Plan purpose and scope
- Plan activation triggers (when to invoke this plan)
- Plan owner and maintenance
- Relationship to overall Business Continuity Management

**4.2.2 Recovery Procedures**

For each critical system, document:
- **Detection:** How failure is detected (monitoring, user reports)
- **Assessment:** How to assess severity and decide on recovery action
- **Activation:** Who authorizes plan activation
- **Recovery Steps:** Detailed step-by-step procedures to restore system
  - Prerequisites (access, tools, resources needed)
  - Restore from backup procedure (with screenshots/examples)
  - Failover procedure (if redundancy exists)
  - Configuration restoration
  - Verification steps (how to confirm recovery success)
  - Estimated time for each step
- **Communication:** Who to notify during recovery
- **Fallback:** What to do if recovery fails

**4.2.3 Roles and Responsibilities**

Document roles during recovery:
- **Recovery Team Lead:** Coordinates recovery, makes decisions, manages communications
- **Technical Recovery Team:** Executes recovery procedures (restore, failover, configuration)
- **Business Liaison:** Coordinates with business stakeholders, provides updates
- **Communication Coordinator:** Manages internal and external communications
- **Logistics Coordinator:** Manages resources (workspace, equipment, supplies)

Each role should have:
- Primary assignee
- Backup assignee (if primary unavailable)
- Contact information (phone, email, alternate)

**4.2.4 Communication Plans**

Communication procedures for:
- **Internal communications:**
  - Employee notification (who, when, how)
  - Management escalation (reporting chain)
  - Recovery team coordination (status updates, issue resolution)
- **External communications:**
  - Customer notification (if service disruption affects customers)
  - Supplier/vendor notification (if their assistance needed)
  - Regulatory notification (24h/72h per NIS2 if applicable)
  - Media relations (if public statement needed)

Communication templates provided for common scenarios.

**4.2.5 Resource Requirements**

Document resources needed for recovery:
- **Personnel:** Who is needed, how many, what skills
- **Equipment:** Servers, storage, network devices, workstations
- **Software:** Licenses, installation media, configurations
- **Facilities:** Recovery workspace, datacenters, office space
- **Vendors:** External support (cloud providers, managed services, consultants)

**4.2.6 Recovery Priorities**

Document sequence of recovery:
1. First priority: Critical systems (Tier 1)
2. Second priority: Important systems (Tier 2)
3. Third priority: Standard systems (Tier 3)

Within each tier, order by dependencies (restore dependencies first).

### 4.3 Plan Formats

Recovery plans may exist in multiple formats for accessibility:

**Detailed Documentation:**
- Comprehensive written procedures
- Stored in document management system
- Version controlled

**Quick Reference Playbooks:**
- Condensed procedures for rapid reference during crisis
- Laminated cards or pocket guides
- Available offline (printable)

**Digital Runbooks:**
- Automated or semi-automated recovery scripts
- Executable procedures (reduces human error)

**Decision Trees:**
- Flowcharts for decision-making during crisis
- "If X, then Y" logic paths

### 4.4 Plan Maintenance Requirements

ICT Recovery Plans shall be maintained as **living documents**:

**Update Triggers:**
- Infrastructure changes (new systems, retired systems, architecture changes)
- Personnel changes (new recovery team members, role changes)
- BIA updates (changed RPO/RTO requirements)
- Failed tests (procedures didn't work, need revision)
- Actual incidents (lessons learned)
- Annual review (scheduled maintenance)

**Version Control:**
- Each plan version numbered and dated
- Change log documenting what changed and why
- Old versions archived (not deleted)

**Accessibility:**
- Plans stored in accessible location (not just on systems that may fail)
- Offline copies available (printed or stored on offline media)
- Recovery team members know where to find plans

---

## 5. Recovery Capability vs. Requirements Alignment

### 5.1 Gap Analysis Requirement

[Organization] shall regularly assess whether **actual recovery capabilities** meet **business requirements** defined in BIA.

**Gap Analysis Process:**
1. **Requirements (from BIA):** RPO/RTO requirements per system
2. **Capabilities (from A.8.13/A.8.14):** Actual backup frequency, actual failover time
3. **Comparison:** Does capability meet requirement?
4. **Gap Identification:** Where capability < requirement
5. **Risk Assessment:** What is business impact of gap?
6. **Remediation Planning:** How to close gap (or accept risk)

### 5.2 Common Gap Scenarios

**RPO Gaps:**
- Requirement: RPO 4 hours
- Capability: Daily backups (RPO 24 hours)
- Gap: 20 hours of potential data loss
- Remediation: Increase backup frequency to hourly

**RTO Gaps:**
- Requirement: RTO 2 hours
- Capability: Restore from backup takes 6 hours (measured in testing)
- Gap: 4 hours beyond acceptable downtime
- Remediation: Implement redundancy with automatic failover OR accept risk

**Coverage Gaps:**
- Requirement: System identified as Critical in BIA
- Capability: No backup exists
- Gap: Cannot recover system at all
- Remediation: Implement backup immediately (critical finding)

### 5.3 Gap Prioritization

Not all gaps can be remediated immediately (budget, resources). Prioritize based on:

**Risk Score = Criticality × Gap Severity × Likelihood**

**Criticality:**
- Critical system = 10 points
- Important system = 5 points
- Standard system = 2 points

**Gap Severity:**
- No backup/redundancy = 10 points
- RPO/RTO gap > 50% of requirement = 7 points
- RPO/RTO gap 25-50% of requirement = 4 points
- RPO/RTO gap < 25% of requirement = 2 points

**Likelihood:**
- High likelihood of disruption = 3x multiplier
- Medium likelihood = 2x multiplier
- Low likelihood = 1x multiplier

**Prioritization:**
- Risk Score > 200 → Critical priority (remediate within 90 days)
- Risk Score 100-200 → High priority (remediate within 6 months)
- Risk Score 50-100 → Medium priority (remediate within 1 year)
- Risk Score < 50 → Low priority (remediate as resources permit or accept risk)

### 5.4 Risk Acceptance Criteria

Some gaps may be accepted rather than remediated:

**Acceptable Reasons for Risk Acceptance:**
- Cost of remediation exceeds business impact of gap
- Technical infeasibility (no solution exists)
- Temporary gap (remediation in progress)
- Compensating controls reduce risk (manual workarounds, vendor support SLA)

**Risk Acceptance Process:**
- Risk documented in risk register
- Business owner reviews and accepts risk (not IT decision)
- Executive management approves risk acceptance (for critical gaps)
- Risk acceptance reviewed annually (conditions may change)

**Unacceptable Risk Acceptance:**
- Critical system with no backup (data loss would be catastrophic)
- Critical system with RTO gap > 50% (downtime unacceptable to business)
- Regulatory requirement not met (DORA/NIS2 compliance gaps)

### 5.5 Remediation Tracking

All gaps shall be tracked in **Gap Remediation Register:**
- Gap ID and description
- System affected
- Gap type (RPO, RTO, coverage)
- Risk score and priority
- Remediation plan
- Remediation owner
- Target completion date
- Status (Open, In Progress, Complete, Risk Accepted)

Remediation progress reviewed monthly by BC/DR Coordinator and reported quarterly to management.

---

## 6. BC/DR Awareness and Training

### 6.1 Training Purpose

Even the best BC/DR plans fail if people don't know they exist or how to execute them. Training ensures preparedness.

### 6.2 Training Requirements by Role

**6.2.1 Executive Awareness (Annual)**
- Audience: Executive management, board members
- Content:
  - BC/DR strategy overview
  - [Organization]'s BC/DR posture (compliance metrics)
  - Critical gaps and risks
  - Investment needs and priorities
- Format: Executive briefing (1 hour)
- Purpose: Ensure executives understand risks and support BC/DR program

**6.2.2 BC/DR Team Training (Quarterly)**
- Audience: BC/DR Coordinator, Recovery Team Leads, Technical Recovery Teams
- Content:
  - Detailed recovery procedures
  - Roles and responsibilities during crisis
  - Communication protocols
  - Recovery tools and systems
  - Hands-on practice (restore procedures, failover procedures)
- Format: Workshop and practical exercises (4-8 hours)
- Purpose: Ensure recovery team can execute plans effectively

**6.2.3 IT Staff Training (Semi-Annual)**
- Audience: All IT operations staff, system administrators
- Content:
  - BC/DR overview
  - Backup and restore procedures
  - Monitoring and alerting
  - Escalation procedures
- Format: Technical training (2-4 hours)
- Purpose: Ensure IT staff can support recovery operations

**6.2.4 General Staff Awareness (Annual)**
- Audience: All employees
- Content:
  - What is business continuity
  - Employee responsibilities during crisis
  - How to report incidents
  - Communication channels during disruptions
- Format: E-learning or briefing (30 minutes)
- Purpose: Ensure all employees understand basic BC/DR concepts

**6.2.5 New Employee Onboarding**
- Audience: New hires (especially in IT and critical business functions)
- Content: BC/DR overview relevant to their role
- Timing: Within first 30 days of employment

### 6.3 Training Effectiveness Measurement

Training effectiveness shall be measured through:
- **Attendance records** (who was trained, when)
- **Knowledge assessments** (tests after training, especially for BC/DR team)
- **Exercise performance** (do people execute procedures correctly during tests?)
- **Lessons learned** (identify training gaps from exercises)

### 6.4 Training Materials Maintenance

Training materials shall be:
- Updated annually or when plans change
- Consistent with current procedures (outdated training worse than no training)
- Available in accessible formats (online, printed)
- Version controlled

---

## 7. BC/DR Testing Requirements

### 7.1 Testing Philosophy

Testing is the **most critical element** of BC/DR preparedness:
- Plans that are never tested are plans that don't work
- Testing reveals gaps, errors, and unrealistic assumptions
- Testing builds muscle memory for recovery teams

**This section covers holistic BC/DR testing.** Individual backup restore testing (A.8.13) and failover testing (A.8.14) are covered in those respective sections. This section focuses on integrated, scenario-based testing.

### 7.2 Test Types and Frequency

[Organization] shall conduct multiple types of BC/DR tests:

**7.2.1 Tabletop Exercises (Quarterly)**
- **Format:** Discussion-based exercise (no actual recovery)
- **Participants:** BC/DR team, business stakeholders, IT leadership
- **Scenario:** Present hypothetical disaster scenario
- **Activities:**
  - Walk through response procedures step-by-step
  - Discuss decisions, communications, coordination
  - Identify gaps in plans or procedures
- **Duration:** 2-4 hours
- **Risk:** Low (no production impact)
- **Value:** Validates plans, builds team familiarity, low cost

**Example Scenario:** "Primary datacenter suffers power outage during business hours. Estimated restoration time is 8 hours. Walk through response."

**7.2.2 Walkthrough (Semi-Annual)**
- **Format:** Step-through of procedures (semi-operational)
- **Participants:** Technical recovery team
- **Scenario:** Specific system failure
- **Activities:**
  - Verbally step through each recovery procedure
  - Verify access to tools and systems
  - Check that documentation is current and accurate
  - Don't actually execute recovery (just verify procedures are complete)
- **Duration:** 1-2 hours per critical system
- **Risk:** Very low (no production changes)
- **Value:** Validates procedure completeness, identifies documentation gaps

**7.2.3 Functional Tests (Quarterly for Critical Systems)**
- **Format:** Actual execution of recovery procedures (non-production or non-critical systems)
- **Participants:** Technical recovery team
- **Scenario:** Recover specific system or component
- **Activities:**
  - Actually restore system from backup
  - Actually failover to redundant system
  - Verify recovery time
  - Document issues
- **Duration:** 2-4 hours
- **Risk:** Low (test environment or non-critical system)
- **Value:** Proves procedures actually work, measures actual recovery time

**7.2.4 Full Simulation / Disaster Recovery Exercise (Annual)**
- **Format:** Comprehensive test of entire BC/DR capability
- **Participants:** All recovery teams, business stakeholders, executive management
- **Scenario:** Major disaster (site loss, prolonged outage, cyber incident)
- **Activities:**
  - Execute full recovery of multiple critical systems
  - Test communications and coordination
  - Test decision-making under pressure
  - Test supplier/vendor coordination
  - Measure overall recovery time
- **Duration:** 4-8 hours (or multi-day for very complex scenarios)
- **Risk:** Moderate (may require maintenance window)
- **Value:** Most realistic test, validates end-to-end capability, executive visibility

**Example Scenario:** "Ransomware attack encrypts primary datacenter. Recovery from offsite backups to cloud DR environment required."

### 7.3 Scenario Development

Test scenarios should be:
- **Realistic:** Based on actual threats and historical incidents
- **Challenging:** Test systems under stress, not just "happy path"
- **Varied:** Different scenarios over time (don't test same scenario repeatedly)
- **Relevant:** Based on BIA (test critical systems, likely disasters)

**Scenario Categories:**
- Infrastructure failures (power, network, hardware)
- Natural disasters (fire, flood, earthquake)
- Cyber incidents (ransomware, data breach, DDoS)
- Prolonged outages (weeks of disruption)
- Third-party failures (cloud provider outage, supplier disruption)

### 7.4 Test Participant Requirements

**Mandatory Participants:**
- BC/DR Coordinator (leads exercise)
- Recovery Team Leads (coordinate their teams)
- Technical recovery teams (execute recovery procedures)

**Recommended Participants:**
- Business process owners (validate business function recovery)
- Executive management (observe, understand risks)
- Third-party vendors (if recovery depends on vendors)

**Observer Roles:**
- Facilitators (guide exercise, ensure objectives met)
- Evaluators (assess performance, identify gaps)
- Note-takers (document issues, lessons learned)

### 7.5 Test Documentation Requirements

Every BC/DR test shall be documented with:
- **Test Plan:**
  - Test date, time, duration
  - Test type and scenario
  - Objectives (what we're testing)
  - Participants
  - Success criteria
- **Test Results:**
  - What was tested
  - Test outcome (Success, Failure, Partial Success)
  - Systems recovered and recovery time
  - Issues encountered
  - Gaps identified
- **Lessons Learned:**
  - What worked well
  - What didn't work
  - Recommendations for improvement
- **Remediation Plan:**
  - Issues to be fixed
  - Owner and timeline for fixes
  - Retest plan (verify fixes worked)

Documentation stored in BC/DR evidence repository for audit.

### 7.6 Post-Test Review and Remediation

After every test:
1. **Debrief session** within 1 week (all participants)
2. **Document lessons learned**
3. **Create remediation plan** for identified issues
4. **Update plans and procedures** based on findings
5. **Retest** after significant changes (verify improvements)

**Critical:** Failed tests are not failures—they are opportunities to improve **before** an actual disaster. Test failures should be celebrated for revealing gaps.

### 7.7 Testing Compliance Tracking

[Organization] shall track testing compliance:
- Schedule of required tests (by type and system)
- Completed tests vs. scheduled tests
- Overdue tests (red flag)
- Test success rate
- Issue remediation rate

Assessment Workbook 4 (BC/DR Testing Results) tracks all testing activity and compliance.

---

## 8. BC/DR Governance

### 8.1 BC/DR Governance Structure

[Organization] shall establish a governance structure for BC/DR:

**8.1.1 BC/DR Steering Committee**
- **Members:** CISO, CIO, COO, CFO, Business Unit Leaders, BC/DR Coordinator
- **Frequency:** Quarterly meetings (more frequent during crisis)
- **Responsibilities:**
  - Approve BC/DR strategy and investment
  - Review BC/DR readiness metrics
  - Accept strategic risks
  - Allocate resources for BC/DR program

**8.1.2 BC/DR Working Group**
- **Members:** BC/DR Coordinator, IT Managers, Business Process Owners, Security Team
- **Frequency:** Monthly meetings
- **Responsibilities:**
  - Coordinate BC/DR activities
  - Track gap remediation
  - Plan and execute tests
  - Review incidents and lessons learned
  - Update plans and procedures

**8.1.3 BC/DR Coordinator Role**
- **Dedicated role** responsible for day-to-day BC/DR program management
- **Responsibilities:** (see Section 6, Roles and Responsibilities in S1)

### 8.2 Executive Oversight

**Executive management accountability:**
- Ensure adequate BC/DR budget and resources
- Approve BC/DR strategy
- Review quarterly BC/DR status reports
- Accept high-level risks (gaps in critical systems)

**NIS2 Note:** Under NIS2, management bodies are personally liable for cybersecurity and operational resilience, including BC/DR preparedness.

### 8.3 Review and Approval Processes

**BC/DR Plan Approval:**
- Plans reviewed and approved annually by BC/DR Steering Committee
- Major plan changes require executive approval
- Minor updates approved by BC/DR Coordinator

**BIA Approval:**
- BIA results reviewed by business process owners (validate impact assessment)
- BIA approved by executive management (endorse RPO/RTO requirements)

**Gap Remediation Approval:**
- Remediation requiring significant investment approved by BC/DR Steering Committee
- Risk acceptance for critical gaps approved by executive management

### 8.4 Integration with Risk Management

BC/DR shall be integrated with overall enterprise risk management:
- BC/DR risks documented in enterprise risk register
- BC/DR gaps escalated as risks
- Risk treatment plans include BC/DR remediation
- Risk reporting includes BC/DR metrics

### 8.5 Budget Allocation

BC/DR requires ongoing investment:
- Backup infrastructure and storage
- Redundancy infrastructure
- Testing resources
- Training
- BC/DR tools and software
- External services (cloud DR, consulting)

**Budget Process:**
- BC/DR Coordinator develops annual budget proposal
- Budget aligned with gap remediation priorities
- BC/DR Steering Committee approves budget
- Executive management allocates funds

**Adequate budget is essential for BC/DR preparedness.** Underfunded BC/DR programs fail.

---

## 9. Supplier and Third-Party BC Requirements

### 9.1 Supplier BC Risk

[Organization] depends on third-party suppliers and cloud providers. Their BC/DR capabilities directly impact [Organization]'s resilience.

**Supplier Risks:**
- Cloud provider outage (if [Organization] systems hosted in cloud)
- Managed service provider failure (if critical services outsourced)
- Software-as-a-Service (SaaS) provider downtime
- Supply chain disruption (if supplier provides critical components or data)

### 9.2 Supplier BC Assessment Requirements

**Before Engaging Supplier (Due Diligence):**
[Organization] shall assess supplier BC/DR capabilities:
- Request supplier's BC/DR documentation
- Review supplier's SLA commitments (uptime, RTO, RPO)
- Assess supplier's redundancy architecture (single datacenter or multi-region?)
- Review supplier's testing history (do they actually test BC/DR?)
- Assess supplier's incident history (past outages, response quality)

**Assessment Documentation:**
- Supplier BC/DR assessment checklist
- Supplier SLA review
- Risk assessment (what if supplier fails?)

### 9.3 SLA Requirements for Recovery

Contracts with critical suppliers shall include BC/DR provisions:

**Uptime SLA:**
- Minimum availability commitment (e.g., 99.9% uptime)
- Penalties for SLA breaches (service credits)

**RTO/RPO Commitments:**
- Supplier's RTO for service restoration
- Supplier's RPO for data recovery
- Must align with [Organization]'s requirements

**Incident Notification:**
- Supplier must notify [Organization] of outages within defined timeframe
- Escalation procedures if outage exceeds thresholds

**Testing Participation:**
- [Organization] may request participation in supplier's BC/DR tests
- Joint disaster recovery exercises for critical suppliers

**Right to Audit:**
- [Organization] may audit supplier's BC/DR controls
- Third-party audit reports acceptable (SOC 2, ISO 27001)

### 9.4 Cloud Provider BC Arrangements

For cloud-hosted systems, [Organization] shall:

**Understand Shared Responsibility:**
- Cloud provider responsible for infrastructure (datacenter, network, hardware)
- [Organization] responsible for data, configurations, applications
- Both parties must have BC/DR capabilities

**Multi-Region Deployment:**
- Critical systems should leverage multi-region capabilities (where available)
- Protects against regional cloud provider outages

**Cloud Provider SLA Review:**
- Understand cloud provider's availability commitments
- Understand cloud provider's backup and disaster recovery capabilities
- Supplement with [Organization]'s own backups (don't solely rely on provider)

**Cloud Provider Incident Response:**
- Understand cloud provider's incident notification process
- Monitor cloud provider status pages
- Have plan for cloud provider outages (failover to different region or provider)

### 9.5 Supplier Testing

[Organization] should participate in supplier BC/DR testing where feasible:
- Request notification when supplier conducts DR tests
- Verify [Organization]'s systems operate correctly during supplier test
- Joint exercises for critical dependencies

If supplier testing participation not feasible:
- Request supplier test results and evidence
- Conduct own tests of supplier failover (where possible)

---

## 10. Crisis Management Integration

### 10.1 BC/DR Activation Triggers

ICT Recovery Plans are activated during crises. Clear triggers must be defined:

**Automatic Activation Triggers:**
- Complete site loss (fire, flood, physical destruction)
- Prolonged outage (> 4 hours) of critical systems
- Cyber incident impacting critical systems (ransomware, breach)

**Management Decision Triggers:**
- Partial outage of critical systems (assess impact, decide whether to activate)
- Anticipated disruption (hurricane warning, planned major outage)

**Activation Authority:**
- BC/DR Coordinator can activate plans for operational level
- Executive management approval required for full DR activation (major resource commitment)

### 10.2 Crisis Management Team Structure

During major disruptions, [Organization] shall activate Crisis Management Team:

**Crisis Management Team Roles:**
- **Incident Commander** (CEO, COO, or delegate): Overall decision authority, resource allocation
- **BC/DR Coordinator:** Leads ICT recovery operations
- **Business Recovery Manager:** Leads business process recovery, workarounds
- **Communications Manager:** Manages all communications (internal, external, regulatory)
- **Logistics Manager:** Coordinates resources (facilities, supplies, equipment)

**ICT Recovery Team** reports to BC/DR Coordinator, who reports to Incident Commander.

### 10.3 Communication Protocols

**Internal Communications:**
- **Employee Notification:**
  - How employees will be notified of crisis (email, SMS, phone tree, mobile app)
  - Status updates frequency (hourly during crisis)
  - Return-to-normal-operations announcement
- **Management Escalation:**
  - Crisis severity levels (Level 1: Minor, Level 2: Moderate, Level 3: Severe)
  - Escalation path (who to notify at each level)
  - Reporting cadence (status updates to executives)

**External Communications:**
- **Customer Notification:**
  - When to notify customers (if service disruption affects them)
  - Communication channels (website status page, email, social media)
  - Message templates (pre-approved)
- **Regulatory Notification:**
  - **NIS2 Requirement:** 24-hour early warning, 72-hour detailed report
  - Notification triggers and thresholds
  - Regulatory contact information
- **Media Relations:**
  - Media spokesperson designated
  - Press release templates
  - Social media protocols

**Communication Plan should include:**
- Contact lists (kept updated)
- Message templates (for speed and consistency)
- Communication tools (and alternatives if primary tools fail)

### 10.4 Integration with Incident Management (A.5.24-27)

BC/DR activation often follows incident management escalation:

**Incident Management → BC/DR Activation:**
1. Incident detected (per A.5.24)
2. Incident assessed (severity, impact)
3. If incident impacts critical systems and exceeds RTO → BC/DR activation
4. BC/DR recovery procedures execute
5. System restored
6. Post-incident review (lessons learned)

**BC/DR Plans reference incident management procedures** (detection, classification, escalation).

### 10.5 Regulatory Incident Reporting (NIS2)

For organizations subject to NIS2:

**Early Warning (24 hours):**
- Significant incident must be reported within 24 hours of detection
- Early warning includes: Incident description, impact, preliminary assessment
- Reported to: National CSIRT and competent authority

**Detailed Report (72 hours):**
- Comprehensive incident report within 72 hours
- Includes: Root cause, impact assessment, mitigation actions, timeline
- Updates provided as investigation progresses

**Final Report (1 month):**
- Complete post-incident report within 1 month
- Includes: Lessons learned, preventive measures implemented

**BC/DR Plans must include:**
- Regulatory reporting procedures
- Reporting templates
- Contact information for regulatory authorities
- Escalation paths (who approves regulatory notifications)

---

## 11. Continuous Improvement

### 11.1 Continuous Improvement Principle

BC/DR is not a "set and forget" compliance exercise. It requires continuous improvement:
- Business requirements change → BIA updates → RPO/RTO changes
- Technology changes → New systems, architecture changes
- Threats evolve → New disaster scenarios to prepare for
- Tests reveal gaps → Plans and procedures updated
- Actual incidents provide lessons → Improvements implemented

### 11.2 Post-Incident Review Requirements

After any actual disruption or invocation of BC/DR plans:

**Post-Incident Review Process:**
1. **Assemble review team** (all participants in recovery, plus observers)
2. **Document timeline** (what happened, when, who did what)
3. **Assess performance:**
   - What worked well? (sustain these practices)
   - What didn't work? (needs improvement)
   - Were plans accurate and complete?
   - Was RTO/RPO achieved?
   - Were communications effective?
   - Were resources adequate?
4. **Identify lessons learned** (actionable improvements)
5. **Create improvement plan** (what will be changed, who, when)
6. **Update plans** based on lessons learned
7. **Communicate lessons learned** to organization
8. **Retest** updated procedures

**Post-Incident Review Timeline:**
- Initial debrief within 48 hours (while fresh in mind)
- Formal review within 2 weeks
- Improvement plan within 1 month
- Plan updates within 3 months

### 11.3 Lessons Learned Integration

Lessons learned from tests and incidents shall be:
- **Documented** in lessons learned repository
- **Analyzed** for trends (recurring issues)
- **Actioned** (improvement plans created and executed)
- **Verified** (improvements tested)

**Lessons Learned Repository includes:**
- Lesson description
- Source (test or incident)
- Category (process, technical, communication, training, documentation)
- Action required
- Action owner
- Action status
- Verification (how improvement will be tested)

### 11.4 Plan Update Triggers

ICT Recovery Plans shall be updated when:
- **Infrastructure changes:** New systems, retired systems, architecture changes
- **BIA updates:** Changed RPO/RTO requirements
- **Test failures:** Procedures didn't work
- **Actual incidents:** Lessons learned from real disasters
- **Personnel changes:** New recovery team members, role changes
- **Annual review:** Scheduled review even if no changes

**Update Process:**
- Draft updates
- Review with stakeholders
- Test updated procedures
- Approve updates
- Communicate changes
- Archive old version

### 11.5 Maturity Assessment

[Organization] should periodically assess BC/DR maturity:

**Maturity Levels:**
- **Level 1 - Initial:** Ad hoc, reactive, no formal plans
- **Level 2 - Managed:** Basic plans exist, some testing, gaps known
- **Level 3 - Defined:** Comprehensive plans, regular testing, governance established
- **Level 4 - Optimized:** Continuous improvement, automation, proactive

**Maturity Assessment:**
- Conducted annually
- Identifies improvement opportunities
- Sets maturity improvement goals
- Tracks progress over time

Assessment Workbook Dashboard includes overall BC/DR maturity score.

---

## 12. Compliance Measurement

### 12.1 Key BC/DR Readiness Metrics

[Organization] shall measure and report the following ICT BC readiness metrics:

**BIA Currency:**
- **Metric:** Months since last BIA update
- **Target:** ≤ 12 months (annual update)

**Plan Currency:**
- **Metric:** Percentage of ICT Recovery Plans updated within last 12 months
- **Target:** 100%

**Testing Compliance:**
- **Metric:** Percentage of required tests completed on schedule
- **Calculation:** (Tests completed) / (Tests required per schedule) × 100
- **Target:** ≥ 90%

**Training Compliance:**
- **Metric:** Percentage of BC/DR team trained within last 12 months
- **Calculation:** (Team members trained) / (Total team members) × 100
- **Target:** ≥ 95%

**Gap Remediation Progress:**
- **Metric:** Percentage of identified gaps remediated or risk-accepted
- **Calculation:** (Gaps remediated + Gaps accepted) / (Total gaps) × 100
- **Target:** ≥ 80%

**Overall RPO/RTO Compliance:**
- **Metric:** Percentage of systems meeting both RPO and RTO requirements
- **Calculation:** From Assessment Workbook 3
- **Target:** ≥ 90% overall; 100% for Critical systems

### 12.2 Assessment Workbook Integration

Assessment Workbook 4 (BC/DR Testing Results) tracks testing compliance. Assessment Workbook 3 (RPO/RTO Compliance) tracks requirement vs. capability alignment. Dashboard consolidates all metrics.

Organizations shall:
- Complete assessment workbooks quarterly
- Review metrics against targets
- Report to BC/DR Steering Committee quarterly
- Report to executive management semi-annually

### 12.3 Audit Evidence Requirements

For audit purposes (internal, ISO 27001, DORA, NIS2), [Organization] shall maintain:

**BIA Evidence:**
- BIA documentation (impact assessment, MTPD, RPO/RTO determination)
- BIA approval by business owners and executive management
- BIA update history

**Plan Evidence:**
- ICT Recovery Plans (current version)
- Plan update history (version control)
- Plan approval records

**Testing Evidence:**
- Test plans, results, and lessons learned (per Section 7.5)
- Test schedules and completion tracking
- Remediation plans and status

**Training Evidence:**
- Training materials
- Attendance records
- Knowledge assessment results

**Governance Evidence:**
- BC/DR Steering Committee meeting minutes
- Quarterly status reports
- Risk acceptance documentation

**Gap Management Evidence:**
- Gap register
- Remediation tracking
- Risk acceptance approvals

Evidence shall be retained for at least 3 years or as required by applicable regulations.

### 12.4 Continuous Monitoring

BC/DR readiness is not a snapshot but continuous:
- Real-time monitoring of backup and redundancy (A.8.13, A.8.14)
- Quarterly assessment of compliance metrics
- Annual BIA review
- Continuous gap identification and remediation tracking

Dashboards provide real-time visibility into BC/DR posture.

---

## Conclusion

This policy establishes comprehensive ICT readiness for business continuity requirements for [Organization] in accordance with ISO 27001:2022 Control A.5.30.

**Key Requirements Summary:**
✅ Business Impact Analysis shall be conducted to determine RPO/RTO requirements  
✅ BC/DR Strategy shall align technical capabilities with business requirements  
✅ ICT Recovery Plans shall document executable recovery procedures  
✅ Recovery capability vs. requirements alignment shall be continuously assessed  
✅ BC/DR awareness and training shall ensure preparedness  
✅ BC/DR testing shall be conducted regularly (tabletop, walkthrough, full simulation)  
✅ BC/DR governance shall provide executive oversight and resource allocation  
✅ Supplier BC/DR capabilities shall be assessed and managed  
✅ Crisis management integration shall enable effective response  
✅ Continuous improvement shall drive ongoing BC/DR maturity  

**Integration with A.8.13 and A.8.14:**
- A.5.30 defines WHAT is needed (requirements through BIA)
- A.8.13 and A.8.14 implement HOW to achieve it (technical capabilities)
- A.5.30 verifies it works (testing) and measures gaps (compliance)

**Next Steps:**
1. Review and approve this ICT BC readiness policy
2. Conduct or update Business Impact Analysis (IMP-S1)
3. Develop or update ICT Recovery Plans (per Section 4)
4. Assess gaps between requirements and capabilities (IMP-S5, Assessment Workbook 3)
5. Implement BC/DR testing schedule (per Section 7)
6. Establish BC/DR governance (per Section 8)

---

**Document End**

*"Plans are worthless, but planning is everything."* - Dwight D. Eisenhower

*This policy demands both planning AND testing to ensure ICT readiness.*

---

**APPROVAL SIGNATURES**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | | | |
| BC/DR Coordinator | | | |
| CIO / IT Director | | | |
| Business Continuity Manager | | | |

**Next Review Date:** [One year from approval date]