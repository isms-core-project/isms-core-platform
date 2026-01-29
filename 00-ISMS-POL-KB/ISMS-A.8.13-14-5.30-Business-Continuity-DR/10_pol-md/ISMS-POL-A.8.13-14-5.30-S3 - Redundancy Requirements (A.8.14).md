# ISMS-POL-A.8.13-14-5.30-S3: Redundancy Requirements (A.8.14)

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
| 1.0 | [Date] | Security Operations Manager / CISO | Initial redundancy requirements policy for A.8.14 |

---

## Table of Contents

1. [Control Focus: A.8.14](#1-control-focus-a814)
2. [Critical System Identification](#2-critical-system-identification)
3. [RTO Requirements by Criticality](#3-rto-requirements-by-criticality)
4. [Redundancy Architecture Requirements](#4-redundancy-architecture-requirements)
5. [Single Point of Failure (SPOF) Requirements](#5-single-point-of-failure-spof-requirements)
6. [Failover Capability Requirements](#6-failover-capability-requirements)
7. [Geographic Redundancy Requirements](#7-geographic-redundancy-requirements)
8. [Infrastructure Redundancy](#8-infrastructure-redundancy)
9. [Failover Testing Requirements](#9-failover-testing-requirements)
10. [Compliance Measurement](#10-compliance-measurement)

---

## 1. Control Focus: A.8.14

### 1.1 ISO 27001:2022 Control Text

**A.8.14 - Redundancy of Information Processing Facilities**

> Information processing facilities shall be implemented with sufficient redundancy to meet availability requirements.

**Purpose:**
To ensure the availability of information processing facilities in accordance with the organization's requirements.

### 1.2 Control Objective

The objective of this control is to ensure that [Organization] maintains information processing facilities with sufficient redundancy to meet business availability requirements, specifically to:
- Minimize unplanned downtime from component failures
- Enable rapid recovery from failures (within RTO requirements)
- Eliminate or mitigate Single Points of Failure (SPOFs)
- Provide continuous or near-continuous availability for critical systems
- Support business continuity objectives during disruptions

### 1.3 Key Principle: Redundancy vs. Backup

This policy addresses **redundancy** for availability, which is complementary to but distinct from **backup** for recovery:

**Redundancy (A.8.14):**
- Purpose: Maintain availability during failures (minimize downtime)
- Mechanism: Duplicate systems operating in parallel or standby
- Primary metric: Recovery Time Objective (RTO)
- Example: Database cluster with automatic failover - when primary fails, secondary takes over within minutes

**Backup (A.8.13):**
- Purpose: Recover data after loss or corruption
- Mechanism: Periodic copies of data stored separately
- Primary metric: Recovery Point Objective (RPO)
- Example: Nightly backups - when data is lost, restore from last night's backup (may take hours)

**Complementary Relationship:**
- Redundancy provides fast recovery (low RTO) but doesn't protect against data corruption or deletion
- Backup provides data recovery but may have longer recovery times
- Both are required for comprehensive BC/DR capability
- Critical systems typically require both redundancy AND backup

---

## 2. Critical System Identification

### 2.1 Determining Which Systems Require Redundancy

Not all systems require redundancy. Redundancy is costly (duplicate infrastructure, additional complexity) and should be applied based on **business-driven availability requirements**.

**Critical Systems (Tier 1) - Redundancy Mandatory:**
Systems where even brief outages cause significant business impact:
- Revenue-generating systems (e-commerce, payment processing, trading platforms)
- Customer-facing applications with high availability SLAs
- Real-time operational systems (manufacturing control, logistics, emergency services)
- Systems supporting critical business processes identified in BIA

**Important Systems (Tier 2) - Redundancy Recommended:**
Systems where outages cause moderate business impact:
- Internal business applications (ERP, CRM)
- Email and collaboration systems
- Key infrastructure services (Active Directory, DNS, authentication)

**Standard Systems (Tier 3) - Redundancy Optional:**
Systems where brief outages are acceptable:
- Internal tools and utilities
- Reporting and analytics systems
- Development and test environments

**Low-Criticality Systems (Tier 4) - Redundancy Not Required:**
Systems where extended outages are tolerable:
- Archived data access
- Non-critical internal applications
- Training environments

### 2.2 Criticality Classification Process

System criticality for redundancy purposes shall be determined through:

**Business Impact Analysis (BIA):**
- Assess financial impact of downtime ($/hour)
- Assess operational impact (inability to perform critical functions)
- Assess reputational impact (customer trust, brand damage)
- Determine Maximum Tolerable Period of Disruption (MTPD)

**RTO Determination:**
- Based on BIA, business owner defines acceptable downtime (RTO)
- Short RTO (< 4 hours) typically requires redundancy
- Long RTO (> 24 hours) may be achievable with backup/restore alone

**Dependency Analysis:**
- Systems that other critical systems depend on may require redundancy
- Example: Database server is critical if it supports critical applications, even if database alone is not customer-facing

**Regulatory Requirements:**
- Some regulations mandate high availability for certain systems
- Example: Payment systems may have regulatory uptime requirements

### 2.3 Criticality Documentation

System criticality shall be documented in:
- Asset Inventory (ISMS-POL-A.5.9)
- BIA Results (A.5.30)
- Redundancy Architecture Documentation

Criticality classification shall be reviewed:
- Annually (BIA review cycle)
- When business processes change significantly
- When new systems are deployed
- After major incidents (lessons learned)

---

## 3. RTO Requirements by Criticality

### 3.1 Recovery Time Objective Definition

**Recovery Time Objective (RTO)** is the maximum acceptable downtime for a system or service. It represents the target time within which the system must be restored to operation after a disruption.

**Example:**
- If RTO = 4 hours and system fails at 2:00 PM, system must be operational again by 6:00 PM
- RTO includes detection time, decision time, and recovery execution time

### 3.2 RTO Requirements by System Criticality

These are **baseline requirements**. Individual systems may have more stringent RTO requirements based on Business Impact Analysis:

| Criticality Tier | Maximum RTO | Redundancy Requirement | Typical Implementation |
|------------------|-------------|------------------------|------------------------|
| **Critical** (Tier 1) | ≤ 4 hours | Mandatory | Active-passive or active-active redundancy with automatic failover |
| **Important** (Tier 2) | ≤ 24 hours | Recommended | Hot or warm standby, or restore from backup |
| **Standard** (Tier 3) | ≤ 7 days | Optional | Cold standby or restore from backup |
| **Low** (Tier 4) | > 7 days or Risk Accepted | Not required | Restore from backup when needed |

**Note:** RTO ≤ 4 hours is difficult to achieve without redundancy. Backup restore typically takes hours to days depending on data size and complexity.

### 3.3 Business-Driven RTO Determination

**Critical Principle:** RTO requirements are **business-driven**, not IT-driven.

**Process for RTO Determination:**
1. Business Impact Analysis identifies impact of downtime over time
2. Business owner determines acceptable downtime based on impact assessment
3. RTO requirement is documented and approved by business owner
4. IT implements redundancy capabilities to meet approved RTO
5. Gap between business requirement and technical capability is identified, accepted, or remediated

**IT cannot unilaterally change RTO requirements.** If technical or cost limitations prevent meeting business requirements:
- Gap is documented
- Risk assessment is conducted (impact of not meeting RTO)
- Business owner either accepts risk or approves investment to close gap

### 3.4 RTO Components

RTO includes all time from failure to full restoration:

**Detection Time:**
- How long until failure is detected?
- Automated monitoring reduces detection time
- Manual detection may take minutes to hours

**Decision Time:**
- How long to decide on recovery action?
- Automated failover: Seconds to minutes
- Manual failover: Minutes to hours (requires human decision)

**Recovery Execution Time:**
- How long to execute recovery action?
- Automated failover: Minutes
- Manual failover: Hours
- Restore from backup: Hours to days

**Total RTO = Detection + Decision + Execution**

To meet short RTOs (< 1 hour), automation is typically required.

---

## 4. Redundancy Architecture Requirements

### 4.1 Technology-Agnostic Approach

This policy does not mandate specific redundancy technologies or vendors. [Organization] maintains flexibility to select redundancy solutions appropriate to its infrastructure, budget, and requirements.

**Technology Independence:**
- Any redundancy approach meeting these requirements is acceptable
- On-premises, cloud, or hybrid redundancy solutions are all viable
- Hardware redundancy, software redundancy, or both may be used
- Multiple redundancy approaches may be used for different systems

### 4.2 Redundancy Types

[Organization] shall implement redundancy appropriate to system criticality and RTO requirements:

**Active-Active (A-A):**
- Multiple systems operate simultaneously, all serving requests
- Load is distributed across all systems (load balancing)
- If one system fails, others continue without service interruption
- **Advantages:** No failover required (seamless), full capacity utilization
- **Disadvantages:** Higher complexity, data synchronization challenges, higher cost
- **Suitable for:** Critical systems requiring near-zero RTO (< 15 minutes)
- **Example:** Web servers behind load balancer, distributed databases

**Active-Passive (A-P):**
- Primary system serves all requests, secondary system on standby
- If primary fails, secondary takes over (failover)
- **Advantages:** Simpler than A-A, lower cost (standby not fully loaded)
- **Disadvantages:** Failover required (brief outage), standby capacity unused
- **Suitable for:** Critical systems with RTO 15 minutes - 4 hours
- **Example:** Database primary-replica with manual or automatic failover

**N+1 Redundancy:**
- N systems required for capacity, plus 1 spare
- If one system fails, spare takes over
- **Advantages:** Balances redundancy with cost
- **Disadvantages:** Reduced capacity during failure (running at N instead of N+1)
- **Suitable for:** Systems where brief performance degradation is acceptable
- **Example:** Cluster of 4 servers with 1 spare (any server can fail, cluster continues with 3)

**N+2 Redundancy:**
- N systems required, plus 2 spares
- Can tolerate 2 simultaneous failures
- **Advantages:** Higher resilience than N+1
- **Disadvantages:** Higher cost
- **Suitable for:** Critical systems where even redundant components may fail
- **Example:** Critical infrastructure with defense-in-depth redundancy

**Hot Standby:**
- Secondary system fully running, ready to take over immediately
- Similar to Active-Passive but standby is warmed up (application running, data synchronized)
- **Failover Time:** Seconds to minutes
- **Suitable for:** RTO < 1 hour

**Warm Standby:**
- Secondary system partially running (OS running, application stopped)
- Requires time to start application and synchronize data
- **Failover Time:** Minutes to hours
- **Suitable for:** RTO 1-4 hours

**Cold Standby:**
- Secondary system not running (may not even be powered on)
- Requires time to power on, configure, and synchronize data
- **Failover Time:** Hours to days
- **Suitable for:** RTO > 4 hours (may be adequate for Important systems with longer RTOs)

### 4.3 Redundancy Architecture Selection

Selection of redundancy architecture depends on:

**RTO Requirements:**
- RTO < 15 minutes → Active-Active or Hot Standby with automatic failover
- RTO 15 min - 4 hours → Active-Passive or Warm Standby
- RTO > 4 hours → Cold Standby or restore from backup may suffice

**Cost Constraints:**
- Active-Active most expensive (duplicate capacity fully utilized)
- N+1 more cost-effective (shared spare capacity)
- Cold Standby least expensive (standby not running)

**Complexity Tolerance:**
- Active-Active most complex (data synchronization, load balancing)
- Active-Passive simpler
- Cold Standby simplest

**Regulatory Requirements:**
- Some systems may have mandated availability requirements
- Financial trading systems may require near-zero downtime

### 4.4 Clustering and Load Balancing

**Clustering:**
- Multiple servers acting as a single system
- Provides both redundancy (high availability) and scalability (performance)
- Typically used for: Databases, application servers, web servers

**Load Balancing:**
- Distributes traffic across multiple systems
- Enables Active-Active redundancy
- Detects failed systems and routes traffic away from them
- Typically used for: Web applications, APIs, stateless services

**Required Capabilities:**
- Health checks (detect failed systems automatically)
- Session persistence (if stateful applications)
- Geographic load balancing (if multi-site redundancy)

---

## 5. Single Point of Failure (SPOF) Requirements

### 5.1 SPOF Definition

**Single Point of Failure (SPOF)** is a component whose failure would cause the entire system or service to fail, with no redundancy or alternative path.

**Examples of SPOFs:**
- Single database server (if database fails, application fails)
- Single network connection (if network fails, site is offline)
- Single power feed (if power fails, datacenter is offline)
- Single authentication server (if auth fails, all logins fail)

### 5.2 SPOF Identification Requirements

[Organization] shall systematically identify SPOFs through:

**Infrastructure Mapping:**
- Create architecture diagrams showing all components and their dependencies
- Identify components in the path from user to service
- Mark each component as redundant or single

**SPOF Discovery Methodology:**
- For each critical system, trace all dependencies
- Ask: "If this component fails, does the system fail?"
- If yes, and no alternative path exists, it's a SPOF

**Dependency Analysis:**
- Identify upstream dependencies (what this system depends on)
- Identify downstream dependencies (what depends on this system)
- A SPOF in a dependency is a SPOF for all dependent systems

**Systematic Review:**
- Hardware layer: Servers, storage, network devices
- Network layer: Network paths, ISP connections
- Infrastructure layer: Power, cooling, physical security
- Software layer: Application components, services, databases
- External dependencies: Cloud services, third-party APIs, vendors

### 5.3 SPOF Documentation

All identified SPOFs shall be documented in **SPOF Register** including:
- SPOF description (what component/service)
- Affected system(s) (what fails if SPOF fails)
- System criticality (is this SPOF in critical system?)
- Impact assessment (what is business impact of this SPOF failing?)
- Mitigation status (Mitigated / In Progress / Not Mitigated / Risk Accepted)
- Mitigation plan (how will SPOF be eliminated or mitigated?)
- Mitigation owner (who is responsible for remediation?)
- Target completion date (when will mitigation be complete?)

SPOF Register shall be reviewed quarterly and updated when infrastructure changes.

### 5.4 SPOF Mitigation Requirements

**Critical Systems (Tier 1):**
- **Zero tolerance for SPOFs**: All SPOFs in critical systems shall be mitigated or risk-accepted with executive approval
- SPOF mitigation must be prioritized
- Timeframe: Critical SPOFs shall be remediated within 90 days or escalated for risk acceptance

**Important Systems (Tier 2):**
- **Minimize SPOFs**: SPOFs should be mitigated where technically and economically feasible
- Risk assessment required for any accepted SPOFs
- Timeframe: SPOF remediation planned within annual budget cycle

**Standard Systems (Tier 3):**
- **Document SPOFs**: SPOFs shall be identified and documented
- Mitigation optional based on cost-benefit analysis
- Risk acceptance typical for Standard systems

### 5.5 SPOF Mitigation Strategies

**Hardware Redundancy:**
- Replace single server with clustered servers
- Replace single storage device with RAID or replicated storage
- Replace single network device with redundant pair

**Geographic Redundancy:**
- Deploy to multiple physical locations or availability zones
- Eliminates site-wide SPOFs (fire, power outage, natural disaster)

**Multiple Vendors/Providers:**
- Use multiple cloud providers or ISPs
- Eliminates vendor-specific SPOFs

**Failover Automation:**
- Implement automatic detection and failover
- Reduces recovery time when SPOF fails

**Graceful Degradation:**
- Design systems to degrade gracefully when components fail
- Example: Caching layer continues serving even if backend database fails (temporarily)

### 5.6 Acceptable Risk Thresholds

Some SPOFs may be accepted due to:
- Prohibitive cost of mitigation
- Technical infeasibility
- Very low likelihood of failure combined with acceptable RTO

**Risk Acceptance Criteria:**
- Risk assessment conducted (likelihood × impact)
- Business owner approves risk acceptance
- Compensating controls in place (rapid restore from backup, vendor support SLA, etc.)
- Risk acceptance documented and reviewed annually

---

## 6. Failover Capability Requirements

### 6.1 Automatic vs. Manual Failover

**Automatic Failover:**
- System detects failure and switches to redundant system without human intervention
- **Required for:** Critical systems with RTO < 1 hour
- **Advantages:** Fastest recovery, no human delay, works during off-hours
- **Disadvantages:** Risk of false positives (unnecessary failovers), higher complexity

**Manual Failover:**
- Human operator detects failure and manually initiates failover
- **Acceptable for:** Important systems with RTO 1-24 hours
- **Advantages:** Human oversight reduces false positives, simpler implementation
- **Disadvantages:** Slower recovery, requires on-call staff, human error risk

**Decision Criteria:**
- RTO < 1 hour → Automatic failover required
- RTO 1-4 hours → Automatic or manual acceptable (automatic preferred)
- RTO > 4 hours → Manual acceptable

### 6.2 Failover Trigger Conditions

Failover should be triggered when:

**System Failure:**
- Server crash, hang, or unresponsive
- Application crash or fatal error
- Database failure

**Performance Degradation:**
- Response time exceeds thresholds (system under stress)
- Error rate exceeds thresholds (system malfunctioning)

**Infrastructure Failure:**
- Network connectivity loss
- Storage failure
- Power failure

**Planned Maintenance:**
- Scheduled failover for maintenance of primary system

### 6.3 Health Check Requirements

For automatic failover, robust health checks are essential:

**Health Check Types:**
- **Liveness checks**: Is the system responding? (ping, TCP port check)
- **Readiness checks**: Is the system ready to serve traffic? (application startup complete?)
- **Functional checks**: Is the system working correctly? (test critical functions)

**Health Check Configuration:**
- Check frequency: Balance between detection speed and overhead (typically 5-30 seconds)
- Failure threshold: Multiple consecutive failures before triggering failover (avoid false positives)
- Timeout: How long to wait for response before considering check failed

**Best Practices:**
- Implement multiple levels of health checks (network, application, functionality)
- Test health checks in failover tests (verify they actually work)
- Monitor health check status (are health checks themselves working?)

### 6.4 Failover Time Alignment with RTO

Actual failover time (measured during testing) must align with RTO requirements:

**If Actual Failover Time > RTO:**
- Gap exists
- Options:
  - Improve failover speed (automation, faster health checks, pre-warmed standbys)
  - Implement different redundancy architecture (Active-Active instead of Active-Passive)
  - Business owner accepts longer RTO (adjust requirement)

**Failover Time Components:**
- Detection time (health checks detect failure)
- Decision time (automatic: milliseconds; manual: minutes-hours)
- Execution time (switch traffic, start services, synchronize data)
- Verification time (confirm failover successful)

**Measurement:**
- Failover time shall be measured during failover tests
- Recorded in Assessment Workbook 2 (Redundancy Analysis)
- Compared against RTO requirement

### 6.5 Failback Procedures

**Failback** is the process of returning to the primary system after it has been restored following a failure.

**Failback Requirements:**
- Documented failback procedure for each redundancy architecture
- Testing of failback (not just failover)
- Data synchronization considerations (ensure data changes on secondary are not lost during failback)
- Timing considerations (failback during maintenance window to avoid disruption)

**Automatic vs. Manual Failback:**
- **Automatic failback** can be risky (if primary failure reoccurs, may cause repeated failovers)
- **Manual failback** preferred for most scenarios (human verification that primary is truly stable)

---

## 7. Geographic Redundancy Requirements

### 7.1 When Geographic Redundancy is Required

**Geographic redundancy** (multi-site redundancy) protects against site-wide disasters affecting a single location.

**Required for:**
- Critical systems (Tier 1) where site-wide disaster would cause unacceptable business impact
- Systems subject to regulatory requirements for disaster recovery
- Systems with very short RTO (< 4 hours) where primary site recovery may not be fast enough

**Recommended for:**
- Important systems with moderate RTO requirements
- Systems where geographic diversity reduces risk significantly

**Not Required for:**
- Standard and Low-Criticality systems
- Systems where restore from backup within RTO is achievable

### 7.2 Geographic Separation Distance

Geographic separation should be sufficient to avoid single regional disasters:

**Minimum Separation:**
- **50 km** for basic geographic diversity (avoids localized disasters like building fire)
- **100-200 km** for regional disaster protection (avoids city-wide or regional events)
- **500+ km** for major disaster protection (avoids large-scale natural disasters, power grid failures)

**Cloud Multi-Region:**
- Different cloud availability zones within same region: Minimum protection (shared regional infrastructure)
- Different cloud regions: Better protection (separate power grids, networking, management)

**Considerations:**
- Greater distance may increase latency (impacts performance)
- Greater distance may increase complexity (data synchronization, management)
- Balance protection with operational requirements

### 7.3 Cross-Site Data Replication

Geographic redundancy requires data synchronization between sites:

**Synchronous Replication:**
- Primary site waits for secondary site to acknowledge write before completing
- **Advantages:** Zero data loss (RPO = 0), secondary always up-to-date
- **Disadvantages:** Performance impact (latency), requires low-latency connection
- **Suitable for:** Critical systems within same metro area (<50 km)

**Asynchronous Replication:**
- Primary site completes write immediately, replicates to secondary in background
- **Advantages:** No performance impact, works over longer distances
- **Disadvantages:** Some data loss possible (RPO = replication lag), secondary may be slightly behind
- **Suitable for:** Systems where small data loss acceptable, longer distances

**Replication Technology:**
- Database native replication (MySQL, PostgreSQL, SQL Server)
- Storage replication (SAN replication, cloud storage replication)
- Application-level replication
- File system replication

### 7.4 Multi-Region Considerations for Cloud Deployments

For cloud-based systems, geographic redundancy is achieved through multi-region deployment:

**Cloud Provider Regions:**
- Deploy to at least 2 separate regions (e.g., AWS us-east-1 and us-west-2)
- Consider regulatory requirements (data residency laws may limit region choices)
- Balance cost (cross-region data transfer costs) with resilience

**Multi-Region Architecture Options:**
- **Active-Passive Multi-Region**: Primary region serves traffic, secondary region on standby
- **Active-Active Multi-Region**: Both regions serve traffic (global load balancing)
- **Pilot Light**: Secondary region has minimal resources, scaled up during disaster

---

## 8. Infrastructure Redundancy

### 8.1 Network Redundancy

**Network Path Redundancy:**
- Multiple physical network paths from/to critical systems
- If one path fails, traffic routes through alternate path
- Implementation: Redundant switches, routers, cabling

**Internet Service Provider (ISP) Redundancy:**
- Multiple ISP connections to internet
- If one ISP fails, traffic routes through alternate ISP
- Particularly important for internet-facing services
- Implementation: Multi-homed BGP routing

**Network Device Redundancy:**
- Redundant routers, switches, firewalls, load balancers
- Typically in active-active or active-passive configuration
- Protocols: VRRP, HSRP, or vendor-specific high availability

**Monitoring:**
- Network path monitoring (detect outages)
- ISP connection monitoring
- Automatic failover to redundant paths

### 8.2 Power Redundancy

**Uninterruptible Power Supply (UPS):**
- Protects against brief power interruptions and provides time to failover or shut down gracefully
- Sizing: Must support load for sufficient time (typically 15-30 minutes minimum)
- Redundancy: N+1 UPS configuration (one UPS can fail, load continues on others)

**Generator Backup Power:**
- Provides extended power during prolonged outages
- Automatic transfer switch (ATS) switches to generator when utility power fails
- Fuel: Sufficient fuel for extended operation (24-72 hours typical)
- Testing: Regular generator testing (monthly load testing recommended)

**Dual Power Feeds:**
- Separate power feeds from utility (A feed and B feed from separate substations)
- Protects against single feed failure
- Servers connected to both feeds (power supplies draw from both)

**Power Distribution:**
- Redundant Power Distribution Units (PDUs)
- Dual-corded servers (connected to separate PDUs)
- Load balanced across power feeds

### 8.3 Cooling Redundancy

**Data Center Cooling:**
- Redundant HVAC systems (N+1 configuration typical)
- If one cooling unit fails, remaining units handle load
- Critical for on-premises datacenters

**Temperature Monitoring:**
- Real-time temperature monitoring in datacenter
- Automatic alerts if temperature exceeds thresholds
- Automatic shutdown of non-critical systems if overheating occurs (protect critical systems)

### 8.4 Utility Redundancy

**Water Supply:**
- Relevant for cooling systems using water
- Backup water supply or alternative cooling methods

**Network Connectivity:**
- Diverse network paths entering building (separate conduits)
- Protects against construction damage to network cables

---

## 9. Failover Testing Requirements

### 9.1 The Testing Imperative

**Critical Principle:** Untested failover is not failover. Redundancy you have never tested is redundancy you cannot trust.

**Common Failure Scenarios Revealed Only Through Testing:**
- Failover triggers don't work as expected (health checks misconfigured)
- Secondary system doesn't start correctly (configuration errors)
- Data synchronization failed (secondary has stale data)
- Failover takes much longer than expected (RTO not met)
- Failback breaks production (data loss during failback)

**Only testing reveals these issues.**

### 9.2 Test Frequency by System Criticality

Minimum failover test frequencies:

| Criticality Tier | Failover Test Frequency | Test Type |
|------------------|-------------------------|-----------|
| **Critical** | Quarterly | Planned failover and unplanned simulation |
| **Important** | Semi-annually | Planned failover |
| **Standard** | Annually | Planned failover (if redundancy exists) |

These are **minimum** frequencies. More frequent testing is encouraged.

### 9.3 Failover Test Types

**Planned Failover Test:**
- Scheduled failover during maintenance window
- Primary system gracefully shut down, secondary takes over
- Verifies: Failover mechanism works, RTO achievable
- Lowest risk (controlled, reversible)
- Recommended frequency: Quarterly for Critical, Semi-annually for Important

**Unplanned Failover Simulation:**
- Simulate sudden failure (hard shutdown, network disconnect)
- Tests: Automatic detection, failover under stress
- Verifies: Failover works in worst-case scenario, no data loss
- Higher risk (more disruptive)
- Recommended frequency: Annually for Critical systems

**Component Failover Test:**
- Test failover of individual components (one server in cluster, one ISP connection)
- Verifies: System continues operating with component failure
- Can often be done with minimal production impact
- Recommended frequency: Quarterly for critical infrastructure

**Geographic Failover Test:**
- Failover from primary site to secondary site
- Tests: Cross-site failover, data replication, geographic redundancy
- Most complex test (requires coordination across sites)
- Recommended frequency: Annually for systems with geographic redundancy

### 9.4 Test Documentation Requirements

Every failover test shall be documented with:
- Test date and duration
- System(s) tested
- Test type (planned, unplanned simulation, component, geographic)
- Test scope (what was failed over)
- Test result (Success, Failure, Partial Success)
- RTO achieved (how long did failover take?)
- Performance under failover (was performance acceptable?)
- Issues encountered (problems, errors, delays)
- Remediation actions (if issues found)
- Next test scheduled date

Test documentation shall be retained for audit purposes.

### 9.5 Testing Without Impacting Production

Failover tests should minimize production impact where possible:

**Test Environment Failover:**
- Test failover in non-production environment first
- Verifies mechanism works before testing production
- Limited value (production environment may differ)

**Maintenance Window Testing:**
- Schedule failover tests during maintenance windows
- Acceptable brief service interruption planned and communicated
- Most common approach for production systems

**Blue-Green Testing:**
- Maintain parallel production environment (blue)
- Failover to green environment
- Test green, then failover back to blue or keep green as new production

**Canary Testing:**
- Failover small percentage of traffic to secondary
- Verify secondary handles traffic correctly
- Gradually increase traffic percentage
- Suitable for Active-Active architectures with load balancing

### 9.6 Test Result Actions

**Successful Test:**
- Document success and metrics (RTO achieved, performance acceptable)
- Collect evidence for audit
- Schedule next test

**Failed Test:**
- Document failure details (what went wrong)
- Identify root cause (configuration, timing, data synchronization, etc.)
- Create remediation plan
- Implement remediation
- **Retest after remediation to verify fix**
- Failed failover test = critical gap requiring immediate attention

**Partial Success:**
- Document what worked and what didn't (e.g., failover worked but performance degraded)
- Assess whether partial success is acceptable for actual disaster
- Remediate if necessary

### 9.7 Failback Testing

Don't forget to test failback:
- After failing over to secondary, test returning to primary
- Verify no data loss during failback
- Document failback time (may be relevant if primary is repaired faster than RTO)
- Failure to test failback has caused production incidents (data loss during failback)

---

## 10. Compliance Measurement

### 10.1 Key Redundancy Metrics

[Organization] shall measure and report the following redundancy compliance metrics:

**Redundancy Coverage:**
- **Metric:** Percentage of critical systems with redundancy
- **Calculation:** (Critical systems with redundancy) / (Total critical systems) × 100
- **Target:** ≥ 90% for Critical systems

**SPOF Mitigation Rate:**
- **Metric:** Percentage of identified SPOFs that are mitigated
- **Calculation:** (SPOFs mitigated) / (Total SPOFs identified) × 100
- **Target:** ≥ 80% for Critical systems; ≥ 50% overall

**RTO Compliance:**
- **Metric:** Percentage of systems meeting RTO requirements
- **Calculation:** (Systems where failover time ≤ RTO requirement) / (Total systems) × 100
- **Target:** ≥ 90% overall; 100% for Critical systems

**Failover Testing Compliance:**
- **Metric:** Percentage of systems tested on schedule
- **Calculation:** (Systems tested within required frequency) / (Total systems requiring testing) × 100
- **Target:** ≥ 80% overall; ≥ 95% for Critical systems

**Geographic Redundancy Coverage:**
- **Metric:** Percentage of critical systems with geographic redundancy
- **Calculation:** (Critical systems with multi-site deployment) / (Total critical systems) × 100
- **Target:** Varies based on business requirements

### 10.2 Assessment Workbook Integration

Assessment Workbook 2 (Redundancy Analysis) automatically calculates these metrics based on data entered. Organizations shall:
- Complete Assessment Workbook 2 at least quarterly
- Review metrics against targets
- Identify gaps and prioritize remediation
- Track trends (improving, stable, degrading)

### 10.3 Audit Evidence Requirements

For audit purposes (internal, ISO 27001, regulatory), [Organization] shall maintain:

**Redundancy Architecture Evidence:**
- Redundancy policy documentation (this document)
- Architecture diagrams showing redundancy design
- Redundancy implementation documentation
- SPOF register and mitigation status

**Redundancy Testing Evidence:**
- Failover test results (documented per Section 9.4)
- Test schedules and completion records
- Evidence of remediation for failed tests
- RTO achievement evidence

**Compliance Evidence:**
- RTO compliance reports (from Assessment Workbook 2)
- SPOF mitigation tracking
- Testing compliance reports
- Quarterly/annual compliance summaries

Evidence shall be retained for at least 3 years or as required by applicable regulations.

### 10.4 Continuous Improvement

Redundancy compliance is not a one-time achievement but a continuous process:

**Quarterly Reviews:**
- Review Assessment Workbook 2 metrics
- Review SPOF register (new SPOFs identified? mitigation progress?)
- Identify new gaps or degrading trends
- Update remediation roadmap

**Annual Reviews:**
- Update BIA and RTO requirements
- Review redundancy architecture adequacy
- Assess need for additional redundancy (geographic, infrastructure)
- Update procedures based on lessons learned from failover tests

**Post-Incident Reviews:**
- After any actual system failure or disaster
- Review what worked and what didn't (did redundancy work as expected?)
- Update architecture or procedures based on lessons learned
- Test any changes to redundancy architecture

---

## Conclusion

This policy establishes comprehensive redundancy requirements for [Organization] in accordance with ISO 27001:2022 Control A.8.14.

**Key Requirements Summary:**
✅ Critical systems shall have redundancy architectures meeting RTO requirements  
✅ Single Points of Failure shall be systematically identified and mitigated  
✅ Failover capabilities shall be implemented with appropriate automation  
✅ Critical systems shall have geographic redundancy where site-wide disasters pose risk  
✅ Infrastructure redundancy (network, power, cooling) shall support critical systems  
✅ All redundancy shall be tested regularly (untested redundancy = unreliable redundancy)  
✅ RTO compliance shall be measured and reported  
✅ SPOF mitigation shall be tracked and prioritized  

**Next Steps:**
1. Review and approve this redundancy policy
2. Conduct or update Business Impact Analysis to determine RTO requirements (IMP-S1)
3. Assess current redundancy capabilities against these requirements (IMP-S5, Assessment Workbook 2)
4. Identify and prioritize SPOF mitigation
5. Implement regular failover testing cadence
6. Establish redundancy monitoring and reporting

---

**Document End**

*"Redundancy you have never tested is redundancy you cannot trust."*

*This policy demands evidence through testing, not assumptions.*

---

**APPROVAL SIGNATURES**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | | | |
| IT Operations Manager | | | |
| Infrastructure Architect | | | |
| Business Continuity Manager | | | |

**Next Review Date:** [One year from approval date]