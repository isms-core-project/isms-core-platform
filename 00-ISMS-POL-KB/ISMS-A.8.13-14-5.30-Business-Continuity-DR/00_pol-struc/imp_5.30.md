# ISMS Controls A.8.13/8.14/5.30 - BC/DR Framework Implementation Plan

**Date:** 2025-01-10  
**Version:** 1.0  
**Status:** APPROVED FOR AUTONOMOUS EXECUTION

---

## Executive Summary

This document provides the complete implementation plan for ISO 27001:2022 Controls A.8.13 (Information Backup), A.8.14 (Redundancy of Information Processing Facilities), and A.5.30 (ICT Readiness for Business Continuity) as a unified Business Continuity & Disaster Recovery Framework.

**Key Integration Points:**
- ✅ DORA Article 12 requirements (immutability, offsite, testing)
- ✅ NIS2 Directive requirements (3-2-1 rule, encryption, 24h reporting)
- ✅ Veeam 3-2-1-1-0 best practices (industry standard)
- ✅ A.8.23 script patterns (proven implementation approach)

---

## 1. Regulatory & Industry Standards Research

### 1.1 DORA (Digital Operational Resilience Act)
**Status:** Effective January 17, 2025  
**Applies to:** EU financial services entities

**Article 12 - Backup Requirements:**
- Regular backups with defined frequency
- **Restore to different locations** (physically AND logically separated)
- **Immutable backups** (protection from unauthorized changes/corruption)
- Secure offsite storage
- **Segregated backup systems**
- Regular testing of backup restoration processes
- ICT risk management framework integration
- Incident reporting within strict timeframes
- Mandatory resilience testing

### 1.2 NIS2 (Network and Information Security Directive 2)
**Status:** Transposition deadline October 17, 2024 (now effective)  
**Applies to:** Essential and important entities across 18 EU sectors

**Backup Requirements:**
- Business continuity/disaster recovery plans mandatory
- **3-2-1 rule** recommended (3 copies, 2 media types, 1 offsite)
- **Immutable backups** required
- **Offline and geographically distant** backup copies
- Encryption (at-rest and in-transit) mandatory
- Access control enforcement
- Regular testing required
- **24-hour early warning** incident reporting
- **72-hour detailed reporting**
- Supply chain security (vetting backup suppliers)
- Management accountability for cybersecurity

### 1.3 Veeam Best Practices
**3-2-1-1-0 Backup Rule** (Enhanced Industry Standard):

- **3** = Three copies of data (production + 2 backups)
- **2** = Two different media types (disk, cloud, tape)
- **1** = One copy offsite (geographic separation)
- **1** = One copy **offline/air-gapped/immutable** (ransomware protection)
- **0** = **Zero recovery errors** (verified recoverability)

**Key Veeam Guidance:**
- **Immutability** is critical (Object Lock on S3, WORM on tape, air-gapped)
- **SureBackup** technology for automated recovery verification
- GFS (Grandfather-Father-Son) retention schemes
- Scale-Out Backup Repository (SOBR) with capacity tier
- Object storage as preferred target for cloud backups
- **Recovery testing is non-negotiable** - backup without test = no backup

---

## 2. Document Structure

### 2.1 Directory Structure

```
ISMS-A.8.13-14-5.30-Business-Continuity-DR/
├── 00_pol-struc/
│   └── ISMS-POL-A.8.13-14-5.30-00-STRUCTURE-PLAN.md [this document]
│
├── 10_pol-md/
│   ├── ISMS-POL-A.8.13-14-5.30-S1-Executive-Control-Alignment.md
│   ├── ISMS-POL-A.8.13-14-5.30-S2-Backup-Requirements-A813.md
│   ├── ISMS-POL-A.8.13-14-5.30-S3-Redundancy-Requirements-A814.md
│   ├── ISMS-POL-A.8.13-14-5.30-S4-ICT-BC-Requirements-A530.md
│   ├── ISMS-POL-A.8.13-14-5.30-S5-Testing-Evidence-Framework.md
│   └── ISMS-POL-A.8.13-14-5.30-Annex-C-Integration-Mapping.md
│
├── 30_imp-md/
│   ├── ISMS-IMP-A.8.13-14-5.30-S1-BIA-RPO-RTO-Process.md
│   ├── ISMS-IMP-A.8.13-14-5.30-S2-Backup-Implementation.md
│   ├── ISMS-IMP-A.8.13-14-5.30-S3-Redundancy-Implementation.md
│   ├── ISMS-IMP-A.8.13-14-5.30-S4-Recovery-Testing-Process.md
│   └── ISMS-IMP-A.8.13-14-5.30-S5-BC-DR-Assessment.md
│
└── 50_scripts-excel/
    ├── generate_assessment_1_backup_inventory.py
    ├── generate_assessment_2_redundancy_analysis.py
    ├── generate_assessment_3_rpo_rto_compliance.py
    ├── generate_assessment_4_testing_results.py
    └── generate_dashboard_bcdr_readiness.py
```

---

## 3. Policy Documents Specification

### 3.1 S1: Executive Summary, Control Alignment, Scope
**File:** `ISMS-POL-A.8.13-14-5.30-S1-Executive-Control-Alignment.md`  
**Target Length:** 350-450 lines

**Content Requirements:**
1. **ISO 27001:2022 Control Text** (exact quotes from standard)
   - A.8.13 - Information Backup (full control text)
   - A.8.14 - Redundancy of Information Processing Facilities (full control text)
   - A.5.30 - ICT Readiness for Business Continuity (full control text)

2. **Executive Summary**
   - BC/DR business criticality (business survival depends on it)
   - Unified framework approach rationale
   - "Untested recovery = no recovery" principle (Feynman philosophy)
   - Systems Engineering methodology emphasis
   - DORA/NIS2 compliance support statement

3. **Scope and Applicability**
   - Framework applies to all ICT systems and data
   - Technology-agnostic (on-prem/cloud/hybrid/multi-cloud)
   - Business-requirement-driven (not prescriptive)
   - Scalable to organization size

4. **Integration Architecture**
   - How three controls form ecosystem
   - Recovery capability = Backup + Redundancy + Preparedness
   - RPO/RTO as unifying concept across all controls
   - Testing as verification mechanism (evidence-based)

5. **Regulatory Context**
   - DORA Article 12 alignment (financial services)
   - NIS2 Directive alignment (essential/important entities)
   - Industry best practices (Veeam 3-2-1-1-0)
   - Framework supports but does not mandate specific regulations

6. **Roles and Responsibilities**
   - Business owners (define RPO/RTO requirements)
   - BC/DR Coordinator (overall program management)
   - Technical teams (implement backup/redundancy)
   - Testing coordinators (recovery testing)
   - Auditors/assessors (compliance verification)

7. **Framework Overview**
   - Policy sections roadmap (S1-S5)
   - Implementation guidance structure (IMP S1-S5)
   - Assessment workbooks overview (WB1-4 + Dashboard)

### 3.2 S2: Information Backup Requirements (A.8.13)
**File:** `ISMS-POL-A.8.13-14-5.30-S2-Backup-Requirements-A813.md`  
**Target Length:** 450-550 lines

**Content Requirements:**

1. **Control Focus: A.8.13**
   - Full control text from ISO 27001:2022
   - Control purpose and objectives
   - Backup vs. archival distinction
   - Backup as recovery enabler

2. **Backup Scope Requirements**
   - What must be backed up (systems, databases, configurations, data)
   - Criticality-based prioritization
   - Exclusions (ephemeral data, truly non-critical systems)
   - Documentation requirements (backup inventory)

3. **Backup Schedule Requirements**
   - Frequency aligned with RPO requirements
   - Timing considerations (backup windows, business hours)
   - Full vs. incremental strategies
   - Retention policies (short-term, long-term, archival)

4. **RPO Requirements by Criticality**
   - Critical systems: RPO ≤ 4 hours (example, business-defined)
   - Important systems: RPO ≤ 24 hours (example, business-defined)
   - Standard systems: RPO ≤ 7 days (example, business-defined)
   - **Business-driven, not IT-driven** (BIA determines requirements)

5. **Backup Technology Requirements**
   - Technology-agnostic principles (no vendor mandates)
   - Backup integrity verification (checksums, validation)
   - Encryption requirements:
     - In-transit encryption (TLS/SSL)
     - At-rest encryption (AES-256 or equivalent)
     - Key management requirements
   - Backup solution capabilities needed (generic)

6. **3-2-1-1-0 Rule Implementation** (Industry Best Practice)
   - **3**: Three copies of data (production + 2 backups)
   - **2**: Two different media types (disk/tape/cloud)
   - **1**: One copy offsite (geographic separation)
   - **1**: One copy offline/air-gapped/immutable (ransomware protection)
   - **0**: Zero recovery errors (verified recoverability)
   - Reference Veeam best practices, but don't mandate specific vendors

7. **Offsite/Offline Backup Requirements**
   - Geographic separation requirements (minimum distance considerations)
   - Cloud backup considerations (multi-region, multi-provider)
   - Ransomware protection (offline/immutable/air-gapped)
   - **DORA compliance**: Backups restorable to different locations
   - **NIS2 compliance**: Geographically distant backup copies

8. **Immutability Requirements** (DORA/NIS2)
   - Immutable backup copies required for critical systems
   - Implementation approaches:
     - Object Lock (S3-compatible storage)
     - WORM media (tape)
     - Air-gapped systems (physically disconnected)
   - Protection from ransomware and malicious deletion

9. **Backup Testing Requirements**
   - Test frequency by system criticality:
     - Critical: Monthly restore testing minimum
     - Important: Quarterly restore testing minimum
     - Standard: Annual restore testing minimum
   - Test types:
     - File-level restore testing
     - System-level restore testing
     - Cross-platform restore testing
     - Full DR scenario testing (annual)
   - Test documentation requirements (results, issues, remediation)
   - Success criteria (RTO met, data integrity verified)

10. **Backup Monitoring Requirements**
    - Backup success/failure monitoring (automated)
    - Alert thresholds (failed backups, capacity issues)
    - Dashboard requirements (real-time status visibility)
    - Reporting cadence (daily operations, monthly management)

11. **Recovery Procedures**
    - Documented recovery procedures for each system type
    - Recovery playbooks (step-by-step instructions)
    - Escalation paths (when recovery fails)
    - Recovery verification (integrity checks post-restore)

12. **Compliance Measurement**
    - Backup coverage metrics (% systems backed up)
    - RPO compliance metrics (actual backup frequency vs. required)
    - Testing compliance metrics (% systems tested on schedule)
    - Audit evidence requirements (logs, test results, procedures)

### 3.3 S3: Redundancy Requirements (A.8.14)
**File:** `ISMS-POL-A.8.13-14-5.30-S3-Redundancy-Requirements-A814.md`  
**Target Length:** 450-550 lines

**Content Requirements:**

1. **Control Focus: A.8.14**
   - Full control text from ISO 27001:2022
   - Control purpose and objectives
   - Redundancy vs. backup distinction (availability vs. recoverability)
   - High availability concepts

2. **Critical System Identification**
   - Criticality classification criteria (BIA-driven)
   - Business impact considerations (financial, operational, reputational)
   - Dependency mapping requirements (system interdependencies)
   - Documentation requirements (critical system register)

3. **RTO Requirements by Criticality**
   - Critical systems: RTO ≤ 4 hours (example, business-defined)
   - Important systems: RTO ≤ 24 hours (example, business-defined)
   - Standard systems: RTO ≤ 7 days (example, business-defined)
   - Acceptable downtime parameters (MTPD alignment)

4. **Redundancy Architecture Requirements**
   - Redundancy types:
     - Active-Active (simultaneous operation, load distribution)
     - Active-Passive (hot standby, automatic failover)
     - N+1 (one spare component/system)
     - N+2 (two spare components/systems)
   - Hot/Warm/Cold standby definitions
   - Clustering and load balancing considerations
   - Technology-agnostic approach (no vendor mandates)

5. **Single Point of Failure (SPOF) Requirements**
   - SPOF identification methodology (systematic analysis)
   - SPOF mitigation requirements (by criticality)
   - Acceptable risk thresholds (risk acceptance framework)
   - Continuous SPOF monitoring (architecture changes)

6. **Failover Capability Requirements**
   - Automatic vs. manual failover (based on RTO)
   - Failover trigger conditions (health checks, thresholds)
   - Failover time alignment with RTO requirements
   - Failback procedures (return to primary after recovery)

7. **Geographic Redundancy Requirements**
   - When required (critical systems, regulatory requirements)
   - Geographic separation distance (minimum thresholds)
   - Cross-site data replication (synchronous vs. asynchronous)
   - Multi-region considerations (cloud deployments)

8. **Infrastructure Redundancy**
   - Network redundancy:
     - Multiple network paths
     - Multiple ISP connections
     - Redundant routing protocols
   - Power redundancy:
     - UPS (uninterruptible power supply)
     - Generators (backup power)
     - Dual power feeds
   - Cooling redundancy (data center environments)
   - Utility redundancy (water, HVAC)

9. **Failover Testing Requirements**
   - Test frequency by system criticality:
     - Critical: Quarterly failover testing minimum
     - Important: Semi-annual failover testing minimum
     - Standard: Annual failover testing minimum
   - Test types:
     - Planned failover (scheduled maintenance simulation)
     - Unplanned failover simulation (disaster scenario)
     - Performance testing under failover
   - Test documentation requirements
   - Success criteria (RTO achieved, no data loss)

10. **Compliance Measurement**
    - Redundancy coverage metrics (% critical systems with redundancy)
    - SPOF count and mitigation status
    - RTO compliance metrics (actual failover time vs. required)
    - Audit evidence requirements (architecture docs, test results)

### 3.4 S4: ICT BC Readiness Requirements (A.5.30)
**File:** `ISMS-POL-A.8.13-14-5.30-S4-ICT-BC-Requirements-A530.md`  
**Target Length:** 450-550 lines

**Content Requirements:**

1. **Control Focus: A.5.30**
   - Full control text from ISO 27001:2022
   - Control purpose and objectives
   - ICT BC within overall Business Continuity Management
   - Preparedness vs. response distinction

2. **Business Impact Analysis (BIA) Requirements**
   - BIA methodology (impact assessment approach)
   - Impact categories:
     - Financial impact (revenue loss, cost per hour)
     - Operational impact (service disruption, productivity)
     - Reputational impact (customer trust, brand damage)
     - Regulatory impact (compliance penalties)
   - Maximum Tolerable Period of Disruption (MTPD) determination
   - BIA documentation and update frequency (annual minimum)

3. **BC/DR Strategy Requirements**
   - Strategy aligned with BIA results
   - Technical capabilities mapped to business requirements
   - Cost-benefit considerations (redundancy costs vs. impact)
   - Strategy approval and communication requirements
   - Multi-strategy approach (different strategies for different systems)

4. **ICT Recovery Plan Requirements**
   - Plan structure and content requirements:
     - Recovery procedures per system type
     - Roles and responsibilities in recovery
     - Communication plans (internal, external)
     - Resource requirements (personnel, equipment)
   - Plan maintenance and versioning (change control)
   - Plan accessibility (online, offline copies)

5. **Recovery Capability vs. Requirements Alignment**
   - Gap analysis requirements (systematic comparison)
   - Actual RPO/RTO vs. required RPO/RTO
   - Gap remediation planning (prioritization, timelines)
   - Risk acceptance for gaps (documented, approved)

6. **BC/DR Awareness and Training**
   - Training requirements by role:
     - Executive awareness (strategic level)
     - BC/DR team training (operational level)
     - General staff awareness (basic procedures)
   - Training frequency (annual minimum, more for BC/DR team)
   - Training effectiveness measurement (tests, exercises)
   - Awareness campaigns (regular communications)

7. **BC/DR Testing Requirements**
   - Test types:
     - Tabletop exercises (discussion-based, low risk)
     - Walkthroughs (step-through of procedures)
     - Functional tests (actual recovery of non-critical systems)
     - Full simulations (comprehensive DR scenario)
   - Test frequency by scenario:
     - Tabletop: Quarterly minimum
     - Walkthroughs: Semi-annual minimum
     - Full simulation: Annual minimum
   - Test participant requirements (cross-functional teams)
   - Lessons learned process (post-test review, plan updates)

8. **BC/DR Governance**
   - BC/DR governance structure (steering committee)
   - Executive oversight (management accountability)
   - Review and approval processes (plan updates, strategy changes)
   - Integration with risk management (risk register updates)
   - Budget allocation (BC/DR investment decisions)

9. **Supplier/Third-Party BC Requirements**
   - Supplier BC capability assessment (due diligence)
   - SLA requirements for recovery:
     - Supplier RPO/RTO commitments
     - Supplier testing participation
     - Supplier incident notification
   - Cloud provider BC arrangements:
     - Multi-region deployments
     - Provider SLA understanding
     - Shared responsibility model
   - Supplier testing participation (joint exercises)

10. **Crisis Management Integration**
    - BC/DR activation triggers (when to invoke plans)
    - Crisis management team structure (roles, authority)
    - Communication protocols:
      - Internal communications (employee notification)
      - External communications (customer notification, media)
      - Regulatory notifications (24h/72h per NIS2)
    - Integration with incident management (A.5.24-27)

11. **Continuous Improvement**
    - Post-incident review requirements (after real incidents)
    - Lessons learned integration (plan updates)
    - Plan update triggers:
      - After significant infrastructure changes
      - After BIA updates
      - After failed tests
      - Annual minimum
    - Maturity assessment (BC/DR program maturity model)

12. **Compliance Measurement**
    - BC/DR plan currency (last update date)
    - Testing compliance (tests completed vs. scheduled)
    - Training compliance (staff trained vs. required)
    - Gap remediation progress (gaps closed vs. identified)
    - Audit evidence requirements (plans, test results, training records)

### 3.5 S5: Testing Methodology and Evidence Framework
**File:** `ISMS-POL-A.8.13-14-5.30-S5-Testing-Evidence-Framework.md`  
**Target Length:** 350-450 lines

**Content Requirements:**

1. **Testing Philosophy**
   - "Untested recovery = no recovery" principle
   - Feynman principle application ("don't fool yourself")
   - Evidence-based assurance (test results over assumptions)
   - Continuous verification (not one-time compliance)

2. **Backup Testing Methodology**
   - Test types:
     - File-level restore (granular recovery)
     - System-level restore (full system recovery)
     - Cross-platform restore (restore to different hardware)
     - Application-level restore (database, application data)
   - Test frequency requirements (by system criticality)
   - Test scope determination (what to test, how much)
   - Success criteria (data integrity, RTO met, application functional)
   - Production impact mitigation (test environments, timing)

3. **Redundancy Testing Methodology**
   - Failover test types:
     - Planned failover (scheduled, controlled)
     - Unplanned failover simulation (chaos engineering)
     - Geographic failover (cross-site)
     - Component failover (individual SPOF testing)
   - SPOF validation testing (verify SPOF analysis accuracy)
   - Performance testing under failover (degraded mode performance)
   - Success criteria (RTO achievement, no data loss, performance acceptable)
   - Production impact mitigation (blue/green testing, canary deployments)

4. **ICT BC Testing Methodology**
   - Scenario-based testing:
     - Site loss scenarios (primary datacenter unavailable)
     - Prolonged outage scenarios (extended recovery)
     - Cyber incident scenarios (ransomware, breach)
   - Tabletop exercises:
     - Discussion-based (low risk, high learning)
     - Participant roles (executives, BC team, technical)
     - Scenario walkthroughs (step-by-step discussion)
   - Walkthroughs:
     - Procedure verification (are procedures complete?)
     - Dependency validation (are dependencies documented?)
   - Full simulations:
     - Actual system recovery (real systems, test environment)
     - Cross-functional coordination (all teams involved)
     - Time-bound (measure actual recovery times)
   - Participant requirements (who must be involved)

5. **RPO/RTO Compliance Assessment**
   - Measurement approach:
     - Backup frequency → actual RPO
     - Failover time → actual RTO
     - Compare actual vs. required
   - Actual vs. required comparison methodology
   - Gap identification methodology (where capability < requirement)
   - Trend analysis (improving, stable, degrading)

6. **Evidence Collection Requirements**
   - Evidence types per control:
     - **A.8.13 (Backup)**: 
       - Backup logs (success/failure)
       - Restore test results (documented outcomes)
       - RPO compliance reports (frequency analysis)
       - Backup configuration documentation
       - Encryption verification
       - Offsite/immutable copy verification
     - **A.8.14 (Redundancy)**: 
       - Failover test results (documented outcomes)
       - SPOF analysis documentation
       - RTO compliance reports (failover time analysis)
       - Redundancy architecture diagrams
       - Geographic redundancy verification
     - **A.5.30 (ICT BC)**: 
       - BIA documentation (impact analysis)
       - BC/DR plans (documented procedures)
       - Testing results (all test types)
       - Training records (who trained, when)
       - Supplier BC assessments
       - Gap analysis and remediation tracking
   - Evidence retention requirements (7 years typical)
   - Evidence presentation to auditors (organized, accessible)

7. **Compliance Scoring Methodology**
   - Scoring dimensions:
     - **Coverage**: % systems with backup/redundancy
     - **Testing**: % required tests completed
     - **Compliance**: % systems meeting RPO/RTO
   - Weighting by criticality:
     - Critical systems: 50% of score
     - Important systems: 30% of score
     - Standard systems: 20% of score
   - Overall maturity score calculation (0-100 scale)
   - Benchmark targets:
     - Level 1 (Initial): <60%
     - Level 2 (Managed): 60-75%
     - Level 3 (Defined): 75-90%
     - Level 4 (Optimized): >90%

8. **Gap Analysis Methodology**
   - Gap identification:
     - Systems without backup
     - Systems without redundancy (critical only)
     - RPO/RTO compliance gaps
     - Testing compliance gaps
     - Documentation gaps
   - Gap criticality assessment:
     - Critical: System criticality × gap severity
     - High, Medium, Low categorization
   - Remediation prioritization (risk-based)
   - Risk acceptance criteria (documented, approved)

9. **Continuous Testing Approach**
   - Ongoing vs. periodic testing:
     - Continuous: Automated backup verification
     - Periodic: Scheduled restore tests, failover tests
   - Automated testing where possible:
     - Backup verification (automated)
     - Synthetic monitoring (health checks)
   - Testing integration with change management:
     - Test after infrastructure changes
     - Regression testing
   - Real-time compliance monitoring (dashboards)

10. **Reporting and Dashboards**
    - Executive dashboard requirements:
      - Overall BC/DR maturity score
      - Critical gaps summary
      - Compliance trend (improving/stable/degrading)
    - Operational dashboards:
      - Backup success rates (real-time)
      - Testing compliance (by system)
      - Gap remediation status
    - Reporting frequency:
      - Daily: Operations team (backup status)
      - Monthly: Management (compliance summary)
      - Quarterly: Executive (strategic overview)
    - Escalation triggers:
      - Critical backup failures
      - Failed recovery tests
      - Missed RTO in actual incident

### 3.6 Annex-C: Integration Mapping
**File:** `ISMS-POL-A.8.13-14-5.30-Annex-C-Integration-Mapping.md`  
**Target Length:** 200-300 lines

**Content Requirements:**

1. **BC/DR Controls → Other ISMS Controls Mapping**
   - A.5.9 (Asset Inventory) ← BC/DR requires complete asset inventory
   - A.8.6 (Capacity Management) ← Backup storage, redundant capacity
   - A.8.9 (Configuration Management) ← Redundancy configs managed
   - A.8.15 (Logging) ← Backup/failover events logged
   - A.8.16 (Monitoring) ← Backup/redundancy monitored
   - A.5.19-23 (Supplier/Cloud) ← Cloud provider BC/DR capabilities
   - A.5.24-27 (Incident Management) ← BC/DR invoked during incidents
   - A.6.8 (Change Management) ← Changes tested for BC/DR impact

2. **Evidence Flow Between Controls**
   - Asset inventory → Systems requiring backup/redundancy
   - Change management → BC/DR plan updates
   - Incident management → BC/DR activation evidence
   - Monitoring logs → Backup/failover event verification

3. **Integration Testing Considerations**
   - Test BC/DR in context of other controls
   - Verify logging during recovery tests
   - Verify monitoring alerts during failover tests
   - Verify incident management integration during simulations

4. **Unified Compliance Approach**
   - Single evidence repository (cross-control)
   - Consolidated testing (multi-control scenarios)
   - Integrated reporting (BC/DR + other controls)

---

## 4. Implementation Documents Specification

### 4.1 IMP-S1: BIA and RPO/RTO Process
**File:** `ISMS-IMP-A.8.13-14-5.30-S1-BIA-RPO-RTO-Process.md`  
**Target Length:** 400-500 lines

**Content Structure:**
1. Purpose and Scope
2. Business Impact Analysis Process
   - Stakeholder identification and engagement
   - Impact assessment methodology (templates, interviews)
   - MTPD determination process
   - BIA workshop facilitation guidance
   - BIA documentation templates
3. System Criticality Classification
   - Classification criteria (objective, measurable)
   - Criticality levels (Critical/Important/Standard/Low)
   - Classification decision tree (flowchart logic)
   - Example classifications
4. RPO/RTO Determination
   - RPO calculation from BIA (data loss tolerance)
   - RTO calculation from BIA (downtime tolerance)
   - Balancing business needs with cost (trade-offs)
   - Example calculations
5. Dependency Mapping
   - System interdependency analysis (upstream/downstream)
   - Dependency documentation (dependency matrix)
   - Hidden dependencies (often overlooked)
6. Aligning Technical Capabilities with Business Requirements
   - Gap identification process
   - Cost-benefit analysis (investment justification)
   - Risk acceptance workflow (when gaps remain)
7. Common Pitfalls
   - IT-driven vs. business-driven requirements (wrong approach)
   - Unrealistic RTO expectations (minutes for all systems)
   - Ignoring dependencies (cascade failures)

### 4.2 IMP-S2: Backup Implementation
**File:** `ISMS-IMP-A.8.13-14-5.30-S2-Backup-Implementation.md`  
**Target Length:** 450-550 lines

**Content Structure:**
1. Purpose and Scope
2. Backup Solution Selection
   - Requirements gathering (RFP preparation)
   - Solution evaluation criteria (checklist)
   - Vendor/technology selection process
   - Proof of concept (PoC) guidance
3. Backup Architecture Design
   - Full vs. incremental strategies (trade-offs)
   - Backup retention design (GFS schemes)
   - Storage capacity planning (growth projections)
   - Network considerations (bandwidth, timing)
4. 3-2-1-1-0 Implementation Guidance
   - **3 copies**: Production + 2 backups (how to achieve)
   - **2 media**: Disk + Cloud/Tape (examples)
   - **1 offsite**: Geographic separation (how far?)
   - **1 immutable**: Object Lock, WORM, air-gap (how to implement)
   - **0 errors**: Verification testing (how to achieve)
   - Veeam-style implementation examples (technology-agnostic)
5. Backup Scheduling
   - RPO-driven schedule design (alignment process)
   - Backup window optimization (minimize impact)
   - Conflict resolution (multiple systems competing)
   - Example schedules
6. Offsite/Cloud Backup Implementation
   - Offsite location selection criteria
   - Cloud provider selection (AWS, Azure, GCP, others)
   - Data transfer mechanisms (initial seed, incremental)
   - Cost optimization (storage tiers, lifecycle policies)
7. Backup Encryption
   - In-transit encryption (TLS/SSL configuration)
   - At-rest encryption (AES-256 implementation)
   - Key management (KMS, vault, escrow)
   - DORA/NIS2 compliance verification
8. Backup Monitoring Setup
   - Monitoring tool integration (SIEM, dashboards)
   - Alert configuration (failure thresholds)
   - Dashboard creation (real-time visibility)
   - Automated reporting
9. Recovery Procedure Documentation
   - Procedure templates (step-by-step)
   - Step-by-step documentation (screenshots)
   - Recovery playbook creation (runbooks)
   - Version control
10. Backup Testing Procedures
    - File-level restore testing (granular)
    - System-level restore testing (full)
    - Full DR restore testing (comprehensive)
    - Test scheduling (calendar integration)
11. Common Pitfalls
    - Backup without testing (cargo cult compliance)
    - Insufficient retention (data loss)
    - Single backup copy (no redundancy)
    - Backup monitoring gaps (silent failures)

### 4.3 IMP-S3: Redundancy Implementation
**File:** `ISMS-IMP-A.8.13-14-5.30-S3-Redundancy-Implementation.md`  
**Target Length:** 450-550 lines

**Content Structure:**
1. Purpose and Scope
2. SPOF Identification
   - Infrastructure mapping (architecture diagrams)
   - SPOF discovery methodology (systematic analysis)
   - Dependency tracing (follow the chain)
   - SPOF documentation (register)
3. Redundancy Architecture Design
   - Active-active design patterns (examples)
   - Active-passive design patterns (examples)
   - Load balancing architecture (algorithms)
   - Clustering approaches (HA clusters)
4. Failover Mechanism Implementation
   - Automatic failover configuration (health checks)
   - Manual failover procedures (runbooks)
   - Health check configuration (thresholds)
   - Failover triggers (what causes failover)
5. Geographic Redundancy
   - Multi-site architecture (2+ locations)
   - Data replication setup (sync vs. async)
   - Site selection criteria (distance, risk)
   - Cross-site networking (VPN, direct connect)
6. Network Redundancy
   - Dual path design (redundant routes)
   - Multiple ISP configuration (BGP routing)
   - Network failover automation (routing protocols)
7. Power/Utility Redundancy
   - UPS sizing and configuration (capacity)
   - Generator integration (backup power)
   - Dual power feed setup (A+B feeds)
   - Cooling redundancy (HVAC)
8. Cost vs. Availability Trade-offs
   - Cost modeling (TCO analysis)
   - Availability calculation (nine's of uptime)
   - Trade-off decision framework (matrix)
9. Failover Automation vs. Manual
   - When to automate (criteria)
   - Automation risks (cascading failures)
   - Manual procedure documentation (when automation fails)
10. Common Pitfalls
    - Ignoring network as SPOF (overlooked)
    - Insufficient testing of failover (untested = broken)
    - Overly complex architectures (maintainability issues)
    - Shared dependencies between redundant systems (pseudo-redundancy)

### 4.4 IMP-S4: Recovery Testing Process
**File:** `ISMS-IMP-A.8.13-14-5.30-S4-Recovery-Testing-Process.md`  
**Target Length:** 450-550 lines

**Content Structure:**
1. Purpose and Scope
2. Backup Restore Testing
   - Test planning (scope, schedule, resources)
   - File-level restore procedure (step-by-step)
   - System-level restore procedure (step-by-step)
   - Cross-platform restore testing (different hardware)
   - Test environment setup (isolated, safe)
   - Production impact mitigation (timing, isolation)
3. Failover Testing
   - Planned failover test procedure (scheduled)
   - Unplanned failover simulation (chaos engineering)
   - Failback testing (return to primary)
   - Performance validation (under failover)
   - Production impact mitigation (blue/green, canary)
4. Full DR Scenario Testing
   - Scenario definition (site loss, prolonged outage)
   - Tabletop exercise facilitation (agenda, roles)
   - Walkthrough procedure (step-through)
   - Full simulation planning (logistics)
   - Participant coordination (cross-functional)
5. Testing Without Impacting Production
   - Isolated test environments (separate from production)
   - Production snapshot testing (clone, test, dispose)
   - Partial failover testing (subset of systems)
   - Risk mitigation strategies (rollback plans)
6. Test Result Documentation
   - Documentation templates (standardized)
   - Metrics capture (RPO/RTO achieved, issues)
   - Issue logging (what went wrong)
   - Evidence collection (logs, screenshots)
7. Remediation of Identified Gaps
   - Gap analysis from test results
   - Remediation prioritization (risk-based)
   - Remediation tracking (status, ownership)
   - Retest requirements (verify fixes)
8. Testing Frequency Recommendations
   - Critical systems: Monthly restore, Quarterly failover
   - Important systems: Quarterly restore, Semi-annual failover
   - Standard systems: Annual restore, Annual failover
   - Regulatory considerations (DORA, NIS2 may require more)
9. Common Pitfalls
   - Testing only ideal scenarios (happy path bias)
   - Insufficient documentation (can't prove compliance)
   - Not testing failback (one-way recovery)
   - Ignoring test lessons learned (repeat mistakes)

### 4.5 IMP-S5: BC/DR Assessment
**File:** `ISMS-IMP-A.8.13-14-5.30-S5-BC-DR-Assessment.md`  
**Target Length:** 400-500 lines

**Content Structure:**
1. Purpose and Scope
2. Assessment Preparation
   - Data collection planning (what data, from where)
   - Stakeholder coordination (who to involve)
   - Tool preparation (workbooks, scripts)
3. Backup Coverage Assessment
   - Inventory all systems (complete list)
   - Identify backup status (backed up or not)
   - Calculate coverage percentage (metrics)
   - Gap identification (systems without backup)
4. Redundancy Effectiveness Assessment
   - Critical system inventory (criticality classification)
   - SPOF analysis (identify SPOFs)
   - Redundancy verification (architecture review)
   - Gap identification (SPOFs without mitigation)
5. RPO/RTO Compliance Assessment
   - Compare required vs. actual RPO (backup frequency)
   - Compare required vs. actual RTO (failover time)
   - Calculate compliance percentage (metrics)
   - Risk scoring (criticality × gap = risk)
6. Testing Compliance Assessment
   - Verify backup testing frequency (on schedule?)
   - Verify failover testing frequency (on schedule?)
   - Verify BC scenario testing frequency (on schedule?)
   - Identify overdue tests (red flags)
7. Gap Prioritization
   - Criticality scoring (impact assessment)
   - Risk assessment (likelihood × impact)
   - Remediation effort estimation (resources, time)
   - Prioritization matrix (risk vs. effort)
8. Continuous Monitoring Approach
   - Real-time backup monitoring (automated)
   - Automated compliance checking (scripts)
   - Dashboard maintenance (keep current)
   - Trend analysis (improving, stable, degrading)
9. Reporting
   - Executive summary generation (high-level)
   - Detailed findings (technical)
   - Remediation recommendations (prioritized)
   - Follow-up scheduling (next review)
10. Common Pitfalls
    - Assessment without remediation (pointless exercise)
    - Ignoring non-technical gaps (training, documentation)
    - One-time assessment vs. continuous (compliance drift)

---

## 5. Assessment Scripts Specification

### 5.1 Common Script Features (from A.8.23 Analysis)

**All scripts must include:**

1. **Comprehensive Console Output**
```python
print("=" * 78)
print("ISMS-IMP-A.8.13-14-5.30.X - [Workbook Name]")
print("ISO/IEC 27001:2022 - Controls A.8.13, A.8.14, A.5.30")
print("=" * 78)
print("\n🎯 Systems Engineering Approach: Evidence-Based BC/DR")
print("📊 Technology-Agnostic: Works with ANY backup/DR solution")
print("🔒 Regulatory Compliance: DORA Article 12, NIS2 Directive")
```

2. **Exception Handling**
```python
try:
    wb.save(filename)
    print(f"✅ SUCCESS: {filename}")
except Exception as e:
    print(f"❌ ERROR saving workbook: {e}")
    return 1
```

3. **Workbook Validation**
```python
def validate_workbook(filename):
    """Validate generated workbook structure."""
    expected_sheets = [...]
    # Check sheet count, names, row counts
    return True/False
```

4. **Style Definitions**
```python
styles = {
    "header": {...},
    "subheader": {...},
    "column_header": {...},
    "input_cell": {"fill": PatternFill(start_color="FFFFCC", ...)},
    "formula_cell": {"fill": PatternFill(start_color="E7E6E6", ...), 
                     "font": Font(color="0000FF", italic=True)},
    "status_green": {"fill": PatternFill(start_color="C6EFCE", ...)},
    "status_yellow": {"fill": PatternFill(start_color="FFEB9C", ...)},
    "status_red": {"fill": PatternFill(start_color="FFC7CE", ...)},
}
```

5. **Instructions & Legend Sheet**
   - Document information block (ID, version, date, assessor)
   - How to use this workbook (numbered steps)
   - Status legend (symbols, colors, meanings)
   - DORA/NIS2 compliance notes
   - Feynman quote: "Don't fool yourself"

6. **Evidence Register Sheet** (100 rows)
   - Evidence ID, Type, Description, Location, Date, Owner
   - Pre-populated with example evidence types
   - Dropdowns for evidence type

7. **Approval Sign-Off Sheet** (3-level)
   - Completed By (Assessor)
   - Reviewed By (Security Manager)
   - Approved By (CISO)
   - Name, Date, Signature fields
   - Certification statement
   - Next review date

8. **Data Validation Dropdowns**
   - Extensive dropdowns for consistency
   - Pre-defined options (no free text where avoidable)

9. **Conditional Formatting**
   - Red/Yellow/Green for compliance status
   - Based on formulas (e.g., RPO met = green)

10. **Number Formatting**
```python
cell.number_format = "0.00"  # Hours
cell.number_format = "0.0%"  # Percentages
cell.number_format = "YYYY-MM-DD"  # Dates
```

11. **Column Width Optimization**
```python
ws.column_dimensions["A"].width = 25
ws.column_dimensions["B"].width = 15
```

12. **Freeze Panes**
```python
ws.freeze_panes = "A5"  # Freeze header rows
```

13. **Pre-populated Example Data**
   - 50+ rows of realistic sample data
   - Mix of compliant/non-compliant scenarios
   - Various criticality levels
   - Demonstrates how to use workbook

### 5.2 Script 1: Backup Inventory & Coverage
**File:** `generate_assessment_1_backup_inventory.py`  
**Target Length:** 800-1000 lines

**Sheet Structure:**
1. **Instructions_Legend** (standard format)
2. **System_Inventory** (50+ pre-populated rows)
   - System ID, System Name, Description, Owner, Business Function
   - Criticality (Critical/Important/Standard/Low) - dropdown
   - RPO Requirement (hours) - input
   - RTO Requirement (hours) - input
   - Data Size (GB) - input
   - Dependencies - input
3. **Backup_Status** (50+ pre-populated rows)
   - System ID (lookup from System_Inventory)
   - Backup Status (Yes/No/Partial/Planned) - dropdown
   - Backup Solution (vendor/product) - input
   - Backup Schedule Frequency (hours) - input
   - Retention Period (days) - input
   - Last Backup Date/Time - input
   - Backup Size (GB) - input
   - Offsite/Offline Backup (Yes/No) - dropdown
   - Immutable Backup (Yes/No) - dropdown (DORA/NIS2)
4. **3-2-1-1-0_Compliance** (50+ pre-populated rows)
   - System ID (lookup)
   - 3 Copies (Yes/No/Partial) - dropdown
   - 2 Media Types (Yes/No) - dropdown
   - 1 Offsite (Yes/No) - dropdown
   - 1 Immutable (Yes/No) - dropdown (DORA/NIS2)
   - 0 Errors (Yes/No) - dropdown (verified recovery)
   - Compliance Score (%) - **FORMULA**: `=COUNTIF(C10:G10,"Yes")/5`
   - Compliance Status - **FORMULA**: `=IF(H10>=0.8,"✅ Compliant",IF(H10>=0.6,"⚠️ Partial","❌ Non-Compliant"))`
5. **Restore_Testing** (50+ pre-populated rows)
   - System ID (lookup)
   - Last Restore Test Date - input
   - Test Type (File/System/Full DR/Not Tested) - dropdown
   - Test Result (Success/Failure/Partial/Not Tested) - dropdown
   - Actual Recovery Time (hours) - input
   - Issues Identified - input
   - Next Test Scheduled - input
   - Testing Frequency Required (days) - input (based on criticality)
   - Days Since Last Test - **FORMULA**: `=IF(B10="","N/A",TODAY()-B10)`
   - Testing Status - **FORMULA**: `=IF(J10="N/A","❌ Never Tested",IF(J10>I10,"❌ Overdue","✅ Current"))`
6. **RPO_Compliance** (50+ pre-populated rows)
   - System ID (lookup)
   - System Name (lookup)
   - Criticality (lookup)
   - RPO Requirement (hours) (lookup from System_Inventory)
   - Actual Backup Frequency (hours) (lookup from Backup_Status)
   - RPO Met (Yes/No) - **FORMULA**: `=IF(E10<="","""",IF(E10<=D10,"✅ Yes","❌ No"))`
   - RPO Gap (hours) - **FORMULA**: `=IF(F10="✅ Yes",0,MAX(0,E10-D10))`
   - Compliance Status (Compliant/At Risk/Non-Compliant) - **FORMULA**: `=IF(F10="✅ Yes","Compliant",IF(G10<=D10*0.25,"At Risk","Non-Compliant"))`
7. **Gap_Summary** (40 gap rows)
   - Gap ID (auto-numbered)
   - System ID (lookup)
   - System Name (lookup)
   - Criticality (lookup)
   - Gap Type (No Backup/No Testing/RPO Gap/No Offsite/No Immutable/No 3-2-1-1-0) - dropdown
   - Gap Description - input
   - Risk Level (Critical/High/Medium/Low) - **FORMULA**: Based on criticality + gap type
   - Remediation Required - input
   - Remediation Owner - input
   - Target Completion Date - input
   - Status (Open/In Progress/Closed) - dropdown
   - Priority - **FORMULA**: Risk-based prioritization
8. **Evidence_Register** (100 rows - standard)
9. **Approval_Sign_Off** (standard 3-level)

**Data Validation:**
- Criticality: `"Critical,Important,Standard,Low"`
- Backup Status: `"Yes,No,Partial,Planned"`
- Yes/No dropdowns: `"Yes,No"`
- Test Type: `"File-Level Restore,System-Level Restore,Full DR Scenario,Not Tested"`
- Test Result: `"Success,Failure,Partial Success,Not Tested"`
- Gap Type: `"No Backup,No Testing,RPO Gap,No Offsite Copy,No Immutable Copy,No 3-2-1-1-0 Compliance"`
- Risk Level: `"Critical,High,Medium,Low"`
- Status: `"Open,In Progress,Closed"`

**Conditional Formatting:**
- RPO Compliance: Green (met), Yellow (within 25%), Red (not met)
- Testing Status: Green (current), Red (overdue or never tested)
- Backup Status: Green (Yes), Yellow (Partial), Red (No), Blue (Planned)
- 3-2-1-1-0 Compliance: Green (≥80%), Yellow (60-80%), Red (<60%)
- Gap Risk Level: Red (Critical), Orange (High), Yellow (Medium), Green (Low)

**Pre-populated Examples (50 systems):**
- Mix of criticality levels (10 Critical, 15 Important, 20 Standard, 5 Low)
- 5 systems with no backup (gaps)
- 10 systems with RPO gaps (backup frequency > RPO requirement)
- 15 systems with overdue testing
- 20 systems without immutable backups (DORA/NIS2 gap)
- 10 systems without offsite copies
- 15 systems not meeting 3-2-1-1-0

### 5.3 Script 2: Redundancy Analysis
**File:** `generate_assessment_2_redundancy_analysis.py`  
**Target Length:** 800-1000 lines

**Sheet Structure:**
1. **Instructions_Legend** (standard format)
2. **Critical_Systems** (40+ pre-populated rows)
   - System ID, System Name, Description, Owner, Business Function
   - Criticality (Critical/Important/Standard) - dropdown
   - RTO Requirement (hours) - input
   - Current Availability (%) - input
   - Business Impact of Outage ($/hour or High/Medium/Low) - input
   - Redundancy Required (Yes/No/N/A) - dropdown
3. **Redundancy_Architecture** (40+ pre-populated rows)
   - System ID (lookup)
   - Redundancy Type (Active-Active/Active-Passive/N+1/N+2/None) - dropdown
   - Failover Capability (Automatic/Manual/None) - dropdown
   - Failover Time (minutes) - input
   - Geographic Redundancy (Yes/No/N/A) - dropdown
   - Geographic Distance (km) - input (if Yes)
   - Network Redundancy (Yes/No) - dropdown
   - Power Redundancy (Yes/No) - dropdown
   - Cooling Redundancy (Yes/No/N/A) - dropdown
4. **SPOF_Analysis** (40+ pre-populated rows)
   - System ID (lookup)
   - SPOF Identified (Yes/No) - dropdown
   - SPOF Description - input
   - SPOF Component Type (Server/Network/Power/Storage/Application/Other) - dropdown
   - SPOF Impact (Critical/High/Medium/Low) - dropdown
   - Mitigation Status (Mitigated/In Progress/Not Mitigated/Accepted) - dropdown
   - Mitigation Plan - input
   - Mitigation Owner - input
   - Target Completion Date - input
5. **Failover_Testing** (40+ pre-populated rows)
   - System ID (lookup)
   - Last Failover Test Date - input
   - Test Type (Planned Failover/Unplanned Simulation/Component Test/Not Tested) - dropdown
   - Test Result (Success/Failure/Partial Success/Not Tested) - dropdown
   - Actual Failover Time (minutes) - input
   - Performance Degradation (%) - input
   - Issues Identified - input
   - Next Test Scheduled - input
   - Testing Frequency Required (days) - input
   - Days Since Last Test - **FORMULA**: `=IF(B10="","N/A",TODAY()-B10)`
   - Testing Status - **FORMULA**: `=IF(J10="N/A","❌ Never Tested",IF(J10>I10,"❌ Overdue","✅ Current"))`
6. **RTO_Compliance** (40+ pre-populated rows)
   - System ID (lookup)
   - System Name (lookup)
   - Criticality (lookup)
   - RTO Requirement (hours) (lookup from Critical_Systems)
   - Actual Failover Time (hours) - **FORMULA**: Convert minutes to hours from Failover_Testing
   - RTO Met (Yes/No) - **FORMULA**: `=IF(E10<="","""",IF(E10<=D10,"✅ Yes","❌ No"))`
   - RTO Gap (hours) - **FORMULA**: `=IF(F10="✅ Yes",0,MAX(0,E10-D10))`
   - Compliance Status (Compliant/At Risk/Non-Compliant) - **FORMULA**
7. **SPOF_Summary** (dashboard section)
   - By Criticality:
     - Total Systems
     - Systems with SPOF
     - SPOFs Mitigated
     - SPOFs In Progress
     - SPOFs Not Mitigated
     - SPOFs Accepted
     - SPOF Rate (%)
   - By Component Type:
     - Server SPOFs
     - Network SPOFs
     - Power SPOFs
     - Storage SPOFs
     - Application SPOFs
   - **FORMULAS**: `=COUNTIFS(...)`
8. **Gap_Summary** (40 gap rows)
   - Gap ID, System ID, System Name, Criticality
   - Gap Type (No Redundancy/SPOF Not Mitigated/RTO Gap/No Failover Testing/No Geographic Redundancy) - dropdown
   - Risk Level (Critical/High/Medium/Low) - **FORMULA**
   - Remediation Required, Owner, Target Date, Status
9. **Evidence_Register** (100 rows - standard)
10. **Approval_Sign_Off** (standard 3-level)

**Data Validation:**
- Criticality: `"Critical,Important,Standard"`
- Redundancy Required: `"Yes,No,N/A"`
- Redundancy Type: `"Active-Active,Active-Passive,N+1,N+2,Hot Standby,Warm Standby,Cold Standby,None"`
- Failover Capability: `"Automatic,Manual,None"`
- Yes/No dropdowns: `"Yes,No"`
- Yes/No/N/A dropdowns: `"Yes,No,N/A"`
- SPOF Component Type: `"Server,Network,Power,Storage,Application,Database,Security,Other"`
- SPOF Impact: `"Critical,High,Medium,Low"`
- Mitigation Status: `"Mitigated,In Progress,Not Mitigated,Risk Accepted"`
- Test Type: `"Planned Failover,Unplanned Simulation,Component Test,Geographic Failover,Not Tested"`
- Test Result: `"Success,Failure,Partial Success,Not Tested"`

**Conditional Formatting:**
- RTO Compliance: Green (met), Yellow (within 25%), Red (not met)
- Testing Status: Green (current), Red (overdue or never tested)
- SPOF Status: Red (Not Mitigated), Yellow (In Progress), Green (Mitigated), Blue (Accepted)
- Redundancy Type: Green (Active-Active/N+2), Yellow (Active-Passive/N+1), Red (None)
- Failover Capability: Green (Automatic), Yellow (Manual), Red (None)

**Pre-populated Examples (40 systems):**
- Mix of criticality (15 Critical, 15 Important, 10 Standard)
- 5 systems with no redundancy (Critical = gap)
- 10 systems with SPOF not mitigated
- 8 systems with RTO gaps (failover time > RTO requirement)
- 12 systems with overdue failover testing
- 5 systems without geographic redundancy (Critical systems)

### 5.4 Script 3: RPO/RTO Compliance Matrix
**File:** `generate_assessment_3_rpo_rto_compliance.py`  
**Target Length:** 700-900 lines

**Sheet Structure:**
1. **Instructions_Legend** (standard format)
2. **System_Inventory** (60+ pre-populated rows)
   - System ID, System Name, Business Function
   - Criticality (Critical/Important/Standard/Low) - dropdown
   - Business Owner, Technical Owner
3. **Business_Requirements** (60+ pre-populated rows)
   - System ID (lookup)
   - RPO Requirement (hours) - input
   - RTO Requirement (hours) - input
   - Requirement Source (BIA/Regulation/Policy/SLA) - dropdown
   - MTPD (hours) - input
   - Financial Impact ($/hour) - input
   - BIA Date - input
4. **Technical_Capabilities** (60+ pre-populated rows)
   - System ID (lookup)
   - Backup Frequency (hours) - input (achievable RPO)
   - Failover Time (hours) - input (achievable RTO)
   - Capability Last Verified (date) - input
   - Verification Method (Backup Test/Failover Test/Calculation/Estimation) - dropdown
5. **Compliance_Matrix** (60+ pre-populated rows)
   - System ID (lookup), System Name (lookup), Criticality (lookup)
   - **RPO Section:**
     - RPO Required (lookup from Business_Requirements)
     - RPO Actual (lookup from Technical_Capabilities)
     - RPO Met (Yes/No) - **FORMULA**: `=IF(E10<=D10,"✅ Yes","❌ No")`
     - RPO Gap (hours) - **FORMULA**: `=IF(F10="✅ Yes",0,E10-D10)`
   - **RTO Section:**
     - RTO Required (lookup)
     - RTO Actual (lookup)
     - RTO Met (Yes/No) - **FORMULA**: `=IF(I10<=H10,"✅ Yes","❌ No")`
     - RTO Gap (hours) - **FORMULA**: `=IF(J10="✅ Yes",0,I10-H10)`
   - **Overall:**
     - Overall Compliance (Both Met/RPO Only/RTO Only/Neither Met) - **FORMULA**: `=IF(AND(F10="✅ Yes",J10="✅ Yes"),"✅ Both Met",IF(F10="✅ Yes","⚠️ RPO Only",IF(J10="✅ Yes","⚠️ RTO Only","❌ Neither Met")))`
     - Risk Level (Critical/High/Medium/Low) - **FORMULA**: Based on criticality + gaps
6. **Gap_Analysis** (60+ gap rows)
   - System ID (lookup), System Name (lookup), Criticality (lookup)
   - Gap Type (RPO Gap/RTO Gap/Both) - **FORMULA**: Auto-detect from Compliance_Matrix
   - RPO Gap Severity (hours) - **FORMULA**: From Compliance_Matrix
   - RTO Gap Severity (hours) - **FORMULA**: From Compliance_Matrix
   - Business Impact (if gap not closed) - lookup from Business_Requirements
   - Remediation Plan - input
   - Remediation Type (Improve Backup Frequency/Add Redundancy/Accept Risk/Other) - dropdown
   - Remediation Status (Planned/In Progress/Complete/Risk Accepted) - dropdown
   - Remediation Owner - input
   - Target Close Date - input
   - Estimated Cost - input
7. **Compliance_Summary** (dashboard section)
   - **By Criticality:**
     - Total Systems
     - RPO Compliant Count - **FORMULA**: `=COUNTIFS(...)`
     - RPO Compliant Percentage - **FORMULA**: `=Count/Total`
     - RTO Compliant Count - **FORMULA**
     - RTO Compliant Percentage - **FORMULA**
     - Both Compliant Count - **FORMULA**
     - Both Compliant Percentage - **FORMULA**
   - **Overall Metrics:**
     - Overall RPO Compliance: XX%
     - Overall RTO Compliance: XX%
     - Overall Both Compliance: XX%
   - **Trend** (if historical data available):
     - Previous Quarter
     - Current Quarter
     - Trend (Improving/Stable/Degrading)
8. **Risk_Prioritization** (top 20 risks)
   - System ID, System Name, Criticality
   - Gap Type, RPO Gap, RTO Gap
   - Financial Impact ($/hour)
   - Risk Score - **FORMULA**: `=(Criticality Weight) × (Gap Severity) × (Financial Impact)`
   - Ranked by Risk Score (highest first)
9. **Evidence_Register** (100 rows - standard)
10. **Approval_Sign_Off** (standard 3-level)

**Data Validation:**
- Criticality: `"Critical,Important,Standard,Low"`
- Requirement Source: `"BIA,Regulation,Policy,SLA,Contract"`
- Verification Method: `"Backup Test,Failover Test,Full DR Test,Calculation,Estimation"`
- Remediation Type: `"Improve Backup Frequency,Add Redundancy,Upgrade Infrastructure,Accept Risk,Other"`
- Remediation Status: `"Planned,In Progress,Complete,Risk Accepted"`

**Conditional Formatting:**
- Compliance Status: Green (met), Yellow (gap <25%), Red (gap ≥25%)
- Risk Level: Red (Critical), Orange (High), Yellow (Medium), Green (Low)
- Overall Compliance: Green (Both Met), Yellow (One Met), Red (Neither Met)
- Gap Severity: Color scale (green → yellow → red based on gap size)

**Pre-populated Examples (60 systems):**
- Mix of criticality (10 Critical, 20 Important, 25 Standard, 5 Low)
- 15 systems with RPO gaps (various severities)
- 12 systems with RTO gaps (various severities)
- 8 systems with both RPO and RTO gaps (high risk)
- 25 systems fully compliant (both RPO and RTO met)
- Realistic business impact values ($1000-$50,000/hour)

### 5.5 Script 4: BC/DR Testing Results
**File:** `generate_assessment_4_testing_results.py`  
**Target Length:** 700-900 lines

**Sheet Structure:**
1. **Instructions_Legend** (standard format)
2. **Test_Inventory** (30+ pre-populated test records)
   - Test ID, Test Name, Test Description
   - Test Type (Backup Restore/Failover/Tabletop/Walkthrough/Full Simulation) - dropdown
   - Test Scope (systems/components covered) - input
   - Test Frequency Required (days) - input
   - Last Test Date - input
   - Next Test Scheduled - input
   - Test Owner - input
   - Days Since Last Test - **FORMULA**: `=IF(E10="","N/A",TODAY()-E10)`
   - Test Status - **FORMULA**: `=IF(H10="N/A","❌ Never Tested",IF(H10>D10,"❌ Overdue","✅ Current"))`
3. **Test_Results** (30+ pre-populated test results)
   - Test ID (lookup from Test_Inventory)
   - Test Date, Test Duration (hours) - input
   - Test Result (Success/Failure/Partial Success) - dropdown
   - Systems Tested (count) - input
   - Systems Successful (count) - input
   - Systems Failed (count) - input
   - Success Rate (%) - **FORMULA**: `=IF(D10=0,0,E10/D10)`
   - Metrics Achieved:
     - RPO Met (Yes/No/N/A) - dropdown
     - RTO Met (Yes/No/N/A) - dropdown
     - Performance Acceptable (Yes/No/N/A) - dropdown
   - Test Notes - input
4. **Issues_Identified** (50+ issue rows)
   - Test ID (lookup)
   - Issue ID (auto-numbered)
   - Issue Description - input
   - Issue Severity (Critical/High/Medium/Low) - dropdown
   - Affected System - input
   - Root Cause - input
   - Remediation Required - input
   - Remediation Status (Open/In Progress/Closed) - dropdown
   - Remediation Owner - input
   - Target Close Date - input
   - Actual Close Date - input
5. **Testing_Compliance** (by test type)
   - Test Type
   - Tests Required (count) - input
   - Tests Completed On Time (count) - **FORMULA**: Count from Test_Inventory where not overdue
   - Tests Overdue (count) - **FORMULA**: Count from Test_Inventory where overdue
   - Compliance Rate (%) - **FORMULA**: `=Completed/Required`
   - Next Test Due Date - **FORMULA**: MIN(Next Test Scheduled) for this type
6. **Lessons_Learned** (30+ lessons)
   - Test ID (lookup)
   - Lesson ID (auto-numbered)
   - Lesson Description - input
   - Lesson Category (Process/Technical/Communication/Documentation/Training/Other) - dropdown
   - Action Required - input
   - Action Status (Planned/In Progress/Complete) - dropdown
   - Action Owner - input
   - Action Due Date - input
7. **Testing_Summary** (dashboard section)
   - **Overall Metrics:**
     - Overall Testing Compliance (%) - **FORMULA**: Average across test types
     - Tests Conducted (count) - **FORMULA**: Count from Test_Results
     - Tests Passed (count) - **FORMULA**: Count where result = Success
     - Tests Failed (count) - **FORMULA**: Count where result = Failure
     - Tests Partial (count) - **FORMULA**: Count where result = Partial
     - Overall Success Rate (%) - **FORMULA**: Passed/(Passed+Failed+Partial)
   - **By Test Type:**
     - Backup Restore: Count, Success Rate
     - Failover: Count, Success Rate
     - Tabletop: Count, Success Rate
     - Walkthrough: Count, Success Rate
     - Full Simulation: Count, Success Rate
   - **Issue Summary:**
     - Open Critical Issues - **FORMULA**: `=COUNTIFS(Issues!Severity,"Critical",Issues!Status,"Open")`
     - Open High Issues - **FORMULA**
     - Total Open Issues - **FORMULA**
     - Issues Closed This Period - **FORMULA**
   - **Trend Analysis** (if historical data):
     - Previous Quarter: Success Rate, Issues
     - Current Quarter: Success Rate, Issues
     - Trend (Improving/Stable/Degrading)
8. **Evidence_Register** (100 rows - standard)
9. **Approval_Sign_Off** (standard 3-level)

**Data Validation:**
- Test Type: `"Backup Restore,Failover,Tabletop Exercise,Walkthrough,Full Simulation,Component Test"`
- Test Result: `"Success,Failure,Partial Success,Cancelled,Postponed"`
- Issue Severity: `"Critical,High,Medium,Low"`
- Status (Issues/Lessons): `"Open,In Progress,Closed"`
- Lesson Category: `"Process,Technical,Communication,Documentation,Training,Other"`
- Action Status: `"Planned,In Progress,Complete,Cancelled"`
- Yes/No/N/A dropdowns: `"Yes,No,N/A"`

**Conditional Formatting:**
- Test Result: Green (Success), Yellow (Partial), Red (Failure)
- Testing Compliance: Green (>90%), Yellow (70-90%), Red (<70%)
- Issue Status: Red (Open Critical), Yellow (Open High), Green (Closed)
- Test Status: Red (Overdue), Green (Current), Gray (Never Tested)
- Success Rate: Green (>95%), Yellow (80-95%), Red (<80%)

**Pre-populated Examples (30 tests):**
- 10 Backup Restore tests (8 success, 2 partial)
- 8 Failover tests (6 success, 1 failure, 1 partial)
- 5 Tabletop exercises (all success - discussion-based)
- 4 Walkthroughs (all success - procedure review)
- 3 Full Simulations (2 success, 1 partial)
- 5 tests overdue (mixed types)
- 15 issues identified (mix of severities, some closed, some open)
- 20 lessons learned (mix of categories)

### 5.6 Script 5: BC/DR Readiness Dashboard
**File:** `generate_dashboard_bcdr_readiness.py`  
**Target Length:** 1000-1200 lines

**Sheet Structure:**
1. **Executive_Dashboard** (primary view)
   - **Document Information**
     - Document ID: ISMS-IMP-A.8.13-14-5.30-Dashboard
     - Report Date: =TODAY()
     - Reporting Period: [USER INPUT]
     - Organization: [USER INPUT]
   - **Overall BC/DR Maturity Score** (0-100)
     - **FORMULA**: Weighted average of:
       - Backup Compliance (30%)
       - Redundancy Compliance (30%)
       - Testing Compliance (20%)
       - Gap Remediation (10%)
       - Documentation/Training (10%)
     - Score displayed as large number with conditional formatting
     - Maturity Level: Initial/Managed/Defined/Optimized
   - **Compliance by Control** (scorecard)
     - A.8.13 Backup Score - **EXTERNAL LINK**: `='[WB1]Gap_Summary'!Overall_Score`
     - A.8.14 Redundancy Score - **EXTERNAL LINK**: `='[WB2]Gap_Summary'!Overall_Score`
     - A.5.30 ICT BC Score - **EXTERNAL LINK**: `='[WB4]Testing_Summary'!Compliance_Rate`
   - **Key Metrics Summary** (KPI cards)
     - Backup Coverage (%) - **EXTERNAL LINK**: From WB1
     - Backup Testing Compliance (%) - **EXTERNAL LINK**: From WB1
     - Critical Systems with Redundancy (%) - **EXTERNAL LINK**: From WB2
     - SPOF Count (Open) - **EXTERNAL LINK**: From WB2
     - RPO Compliance (%) - **EXTERNAL LINK**: From WB3
     - RTO Compliance (%) - **EXTERNAL LINK**: From WB3
     - Testing Compliance (%) - **EXTERNAL LINK**: From WB4
     - Open Critical Issues - **EXTERNAL LINK**: From WB4
   - **Critical Gaps Count** (top priority items)
     - Critical systems without backup
     - Critical systems without redundancy
     - Critical RPO/RTO gaps
     - Overdue critical tests
     - Total Critical Gaps
   - **Trend Analysis** (month-over-month)
     - Overall Score: Current, Previous, Trend
     - Backup Coverage: Current, Previous, Trend
     - Testing Compliance: Current, Previous, Trend
     - Open Gaps: Current, Previous, Trend

2. **Backup_Metrics** (consolidated from WB1)
   - **From Workbook 1 (Backup Inventory):**
     - Total Systems: **EXTERNAL LINK**: `=COUNTA('[WB1]System_Inventory'!A10:A100)`
     - Systems Backed Up: **EXTERNAL LINK**: `=COUNTIF('[WB1]Backup_Status'!B10:B100,"Yes")`
     - Backup Coverage %: **FORMULA**: `=B5/B4`
   - **RPO Compliance by Criticality:**
     - Critical: X/Y systems compliant (XX%)
     - Important: X/Y systems compliant (XX%)
     - Standard: X/Y systems compliant (XX%)
   - **Testing Compliance by Criticality:**
     - Critical: X/Y systems tested on schedule (XX%)
     - Important: X/Y systems tested on schedule (XX%)
     - Standard: X/Y systems tested on schedule (XX%)
   - **3-2-1-1-0 Compliance:**
     - Systems meeting all 5 criteria (%)
     - Systems with immutable backups (%) - DORA/NIS2
     - Systems with offsite backups (%)
   - **Issues:**
     - Systems Without Backup (count)
     - Systems Without Offsite Backup (count)
     - Systems Without Immutable Backup (count) - DORA/NIS2
     - Overdue Backup Tests (count)

3. **Redundancy_Metrics** (consolidated from WB2)
   - **From Workbook 2 (Redundancy Analysis):**
     - Critical Systems Count: **EXTERNAL LINK**
     - Systems with Redundancy (%): **EXTERNAL LINK**
   - **SPOF Summary:**
     - Total SPOFs Identified: **EXTERNAL LINK**
     - SPOFs Mitigated: **EXTERNAL LINK**
     - SPOFs In Progress: **EXTERNAL LINK**
     - SPOFs Not Mitigated: **EXTERNAL LINK**
     - SPOFs Risk Accepted: **EXTERNAL LINK**
     - SPOF Mitigation Rate (%): **FORMULA**
   - **RTO Compliance by Criticality:**
     - Critical: X/Y systems compliant (XX%)
     - Important: X/Y systems compliant (XX%)
     - Standard: X/Y systems compliant (XX%)
   - **Failover Testing Compliance:**
     - Critical: X/Y systems tested on schedule (XX%)
     - Important: X/Y systems tested on schedule (XX%)
     - Standard: X/Y systems tested on schedule (XX%)
   - **Geographic Redundancy:**
     - Critical Systems with Geographic Redundancy (%)

4. **RPO_RTO_Compliance** (consolidated from WB3)
   - **From Workbook 3 (RPO/RTO Compliance):**
     - **Overall Compliance:**
       - RPO Compliance (%): **EXTERNAL LINK**
       - RTO Compliance (%): **EXTERNAL LINK**
       - Both Compliance (%): **EXTERNAL LINK**
     - **By Criticality:**
       - Critical: RPO X%, RTO Y%, Both Z%
       - Important: RPO X%, RTO Y%, Both Z%
       - Standard: RPO X%, RTO Y%, Both Z%
     - **Gap Count:**
       - Systems with RPO Gaps: **EXTERNAL LINK**
       - Systems with RTO Gaps: **EXTERNAL LINK**
       - Systems with Both Gaps: **EXTERNAL LINK**
     - **Gap Remediation Status:**
       - Planned: XX gaps
       - In Progress: XX gaps
       - Complete: XX gaps
       - Risk Accepted: XX gaps

5. **Testing_Summary** (consolidated from WB4)
   - **From Workbook 4 (Testing Results):**
     - **Overall Testing Compliance:**
       - Overall Compliance (%): **EXTERNAL LINK**
       - Tests Conducted: **EXTERNAL LINK**
       - Overall Success Rate (%): **EXTERNAL LINK**
     - **By Test Type:**
       - Backup Restore: Count, Success Rate
       - Failover: Count, Success Rate
       - Tabletop: Count, Success Rate
       - Walkthrough: Count, Success Rate
       - Full Simulation: Count, Success Rate
     - **Open Issues:**
       - Open Critical Issues: **EXTERNAL LINK**
       - Open High Issues: **EXTERNAL LINK**
       - Total Open Issues: **EXTERNAL LINK**
     - **Overdue Tests:**
       - Overdue Backup Tests: **EXTERNAL LINK**
       - Overdue Failover Tests: **EXTERNAL LINK**
       - Overdue BC Scenario Tests: **EXTERNAL LINK**

6. **Gap_Prioritization** (consolidated gaps from all workbooks)
   - **All Gaps Consolidated:**
     - Gap ID, Source (WB1/WB2/WB3/WB4), System, Criticality
     - Gap Type, Gap Description
     - Risk Score - **FORMULA**: `=(Criticality Weight) × (Gap Type Weight) × (Age Weight)`
     - Remediation Status, Owner, Target Date
     - Days Open - **FORMULA**: `=TODAY()-Gap_Identified_Date`
   - **Sorted by Risk Score** (highest first)
   - **Top 20 Gaps** displayed prominently
   - **EXTERNAL LINKS** to pull gaps from:
     - WB1: Gap_Summary sheet
     - WB2: Gap_Summary sheet
     - WB3: Gap_Analysis sheet
     - WB4: Issues_Identified sheet

7. **Evidence_Summary** (evidence tracking across all workbooks)
   - **Evidence Required per Control:**
     - A.8.13 (Backup): Types of evidence needed
     - A.8.14 (Redundancy): Types of evidence needed
     - A.5.30 (ICT BC): Types of evidence needed
   - **Evidence Available:**
     - Evidence Type, Count Available, Source (WB1/WB2/WB3/WB4)
     - Evidence Status (Complete/Incomplete) - checkbox style
   - **Evidence Currency:**
     - Evidence Type, Last Updated, Age (days), Status (Current/Outdated)
   - **Missing Evidence Highlighted** (conditional formatting - red)
   - **EXTERNAL LINKS** to pull evidence counts from:
     - WB1: Evidence_Register (count rows)
     - WB2: Evidence_Register (count rows)
     - WB3: Evidence_Register (count rows)
     - WB4: Evidence_Register (count rows)

8. **Regulatory_Compliance** (DORA/NIS2 specific)
   - **DORA Article 12 Compliance:**
     - Immutable Backups (%) - **EXTERNAL LINK**: From WB1
     - Restore to Different Locations Tested (%) - **EXTERNAL LINK**: From WB1
     - Segregated Backup Systems (%) - **EXTERNAL LINK**: From WB1
     - Regular Testing (%) - **EXTERNAL LINK**: From WB1
   - **NIS2 Directive Compliance:**
     - 3-2-1-1-0 Compliance (%) - **EXTERNAL LINK**: From WB1
     - Geographically Distant Backups (%) - **EXTERNAL LINK**: From WB1
     - Encryption (At-Rest and In-Transit) (%) - Manual input or **EXTERNAL LINK**
     - 24h Incident Reporting Capability (Yes/No) - Manual input
   - **Compliance Status** (Compliant/Partially Compliant/Non-Compliant)
   - **Regulatory Gaps** (items preventing full compliance)

9. **Approval_Sign_Off** (standard 3-level)

**Dashboard Features:**
- **External Workbook Links** (formulas):
  ```
  ='[ISMS-IMP-A.8.13-14-5.30.1_Backup_Inventory_YYYYMMDD.xlsx]Gap_Summary'!B5
  ```
- **Consolidated KPIs** (all metrics in one view)
- **Overall Maturity Score** (weighted calculation)
- **Risk Register** (consolidated, prioritized gaps)
- **Evidence Summary** (completeness tracking)
- **Trend Analysis** (if historical data available)
- **Executive Summary** (high-level for management)
- **Remediation Roadmap** (planned fixes, timelines)

**Data Validation:**
- Maturity Level: `"Initial,Managed,Defined,Optimized"`
- Compliance Status: `"Compliant,Partially Compliant,Non-Compliant"`
- Trend: `"Improving,Stable,Degrading"`

**Conditional Formatting:**
- Maturity Score: Red (<60%), Yellow (60-80%), Green (>80%)
- Compliance Rates: Red (<70%), Yellow (70-90%), Green (>90%)
- SPOF Count: Red (>10 open), Yellow (5-10 open), Green (<5 open)
- Gap Risk: Red (Critical), Orange (High), Yellow (Medium), Green (Low)

**Pre-populated:**
- Dashboard is primarily formulas (pulls from other workbooks)
- Example calculations shown (with placeholder data)
- Instructions on placing dashboard in same folder as source workbooks
- "Update Links" reminder

---

## 6. Implementation Roadmap

### Phase 1: Policy Sections (Autonomous Execution)
**Duration:** Immediate execution

1. S1: Executive Control Alignment (350-450 lines)
2. S2: Backup Requirements - A.8.13 (450-550 lines)
3. S3: Redundancy Requirements - A.8.14 (450-550 lines)
4. S4: ICT BC Requirements - A.5.30 (450-550 lines)
5. S5: Testing Evidence Framework (350-450 lines)
6. Annex-C: Integration Mapping (200-300 lines)

**Deliverable:** Complete policy framework ready for review

### Phase 2: Implementation Sections (Autonomous Execution)
**Duration:** Immediate execution after Phase 1

1. IMP-S1: BIA RPO/RTO Process (400-500 lines)
2. IMP-S2: Backup Implementation (450-550 lines)
3. IMP-S3: Redundancy Implementation (450-550 lines)
4. IMP-S4: Recovery Testing Process (450-550 lines)
5. IMP-S5: BC/DR Assessment (400-500 lines)

**Deliverable:** Complete implementation guidance ready for use

### Phase 3: Assessment Scripts (Autonomous Execution)
**Duration:** Immediate execution after Phase 2

1. generate_assessment_1_backup_inventory.py (800-1000 lines)
2. generate_assessment_2_redundancy_analysis.py (800-1000 lines)
3. generate_assessment_3_rpo_rto_compliance.py (700-900 lines)
4. generate_assessment_4_testing_results.py (700-900 lines)
5. generate_dashboard_bcdr_readiness.py (1000-1200 lines)

**Deliverable:** Working assessment scripts generating Excel workbooks

### Phase 4: Quality Verification (Autonomous Execution)
**Duration:** Continuous during Phases 1-3

- UTF-8 encoding verification (proactive)
- Formula logic testing (RPO/RTO comparisons)
- Conditional formatting testing (sample data)
- Script execution testing (dry runs)
- Workbook structure validation (automated checks)

**Deliverable:** Self-assessment checklist completed

---

## 7. Quality Assurance Checklist

### Policy Documents (S1-S5, Annex-C)
- [ ] All THREE control texts quoted correctly (A.8.13, A.8.14, A.5.30)
- [ ] Each control's requirements distinctly addressed (separate sections)
- [ ] Integration between controls is clear
- [ ] Technology-agnostic (no vendor/product mandates)
- [ ] DORA Article 12 requirements integrated
- [ ] NIS2 Directive requirements integrated
- [ ] Veeam 3-2-1-1-0 best practices referenced
- [ ] Testing requirements prominent throughout
- [ ] Measurable compliance criteria provided
- [ ] UTF-8 encoding correct (no garbled characters)
- [ ] Length appropriate (not too short, not too long)

### Implementation Documents (IMP-S1-S5)
- [ ] Practical, step-by-step guidance
- [ ] Common pitfalls documented
- [ ] References to policy sections (not duplicating)
- [ ] UTF-8 encoding correct
- [ ] Examples included where helpful
- [ ] Length appropriate for topic

### Assessment Scripts (5 scripts)
- [ ] Workbook schema accurate and complete
- [ ] Formulas tested (RPO/RTO compliance logic correct)
- [ ] Conditional formatting verified (red/yellow/green working)
- [ ] Sample data realistic and diverse (includes gaps)
- [ ] Data validation dropdowns included (extensive)
- [ ] Error handling robust (try/except blocks)
- [ ] UTF-8 encoding for output (emojis work in Excel)
- [ ] Evidence Register (100 rows) included
- [ ] Approval Sign-Off (3-level) included
- [ ] Instructions & Legend sheet complete
- [ ] Dashboard consolidation logic matches workbook structures
- [ ] External workbook links correct (formula syntax)
- [ ] Number formatting correct (hours, percentages, dates)
- [ ] Column widths optimized
- [ ] Freeze panes configured
- [ ] Pre-populated examples comprehensive (50+ rows)

---

## 8. Key Success Criteria

### For Policy Framework:
✅ Completely generic (works for any organization, any infrastructure)  
✅ Three controls distinctly addressed (separate SoA entries possible)  
✅ DORA/NIS2 compliance support built-in  
✅ Industry best practices (Veeam 3-2-1-1-0) referenced  
✅ Testing emphasis clear ("Untested recovery = no recovery")  
✅ Evidence-based approach throughout  

### For Implementation Guidance:
✅ Practical and actionable (not theoretical)  
✅ Technology-agnostic (adaptable to any solution)  
✅ Step-by-step procedures clear  
✅ Common pitfalls documented  
✅ Examples provided  

### For Assessment Scripts:
✅ Working scripts (execute without errors)  
✅ Comprehensive workbooks (all sheets, all formulas)  
✅ Pre-populated examples (demonstrates usage)  
✅ RPO/RTO comparison logic correct (critical formulas)  
✅ 3-2-1-1-0 compliance scoring accurate  
✅ Dashboard consolidation working (external links)  
✅ UTF-8 encoding correct (emojis render properly)  
✅ Conditional formatting working (visual clarity)  

---

## 9. Autonomous Work Protocol

**I will work autonomously following this protocol:**

### READ Phase:
- ✅ Reviewed A.8.20-22 reference implementation
- ✅ Reviewed A.8.23 script patterns
- ✅ Researched DORA Article 12 requirements
- ✅ Researched NIS2 Directive requirements
- ✅ Researched Veeam 3-2-1-1-0 best practices
- ✅ Analyzed A.8.23 scripts for patterns

### UPDATE Phase:
- Adapt A.8.20-22 structure to BC/DR context
- Incorporate DORA/NIS2/Veeam requirements
- Ensure all three controls distinctly addressed
- Emphasize testing and evidence throughout
- Apply A.8.23 script patterns to BC/DR scripts

### TEST Phase:
- Fix UTF-8 encoding proactively (before delivery)
- Test formula logic carefully (RPO/RTO comparisons)
- Verify conditional formatting (with sample data)
- Mentally execute scripts (check logic)
- Validate workbook structures (automated checks)

### PRESENT Phase:
- Deliver COMPLETE sections ready for use
- Include self-assessment against quality checklist
- Flag any uncertainties or assumptions
- No broken UTF-8, no untested formulas, no conditional formatting issues

### DO NOT:
- ❌ Ask for approval to test (just test proactively)
- ❌ Deliver broken UTF-8 that needs fixing
- ❌ Deliver untested formulas
- ❌ Deliver conditional formatting that doesn't work
- ❌ Present incomplete work

### DO:
- ✅ Fix issues proactively before delivery
- ✅ Test logic carefully (especially RPO/RTO gap analysis)
- ✅ Verify everything works as intended
- ✅ Present polished, complete deliverables
- ✅ Learn from past mistakes (UTF-8, formulas)

---

## 10. Next Steps (Autonomous Execution)

**I will now proceed with autonomous execution:**

1. **Phase 1: Policy Sections** (S1 → S2 → S3 → S4 → S5 → Annex-C)
   - Work through each section systematically
   - Fix UTF-8 proactively
   - Present complete, polished sections

2. **Phase 2: Implementation Sections** (IMP S1 → S2 → S3 → S4 → S5)
   - Work through each section systematically
   - Fix UTF-8 proactively
   - Present complete, polished sections

3. **Phase 3: Assessment Scripts** (1 → 2 → 3 → 4 → Dashboard)
   - Test formulas carefully (RPO/RTO logic)
   - Verify conditional formatting
   - Define accurate workbook schemas before dashboard
   - Present complete working scripts

4. **Phase 4: Quality Review**
   - Self-assessment against checklist
   - Final verification

---

**END OF IMPLEMENTATION PLAN**

**Status: APPROVED FOR AUTONOMOUS EXECUTION**  
**Execution Begins: Immediately**  
**Expected Completion: All phases executed sequentially**

---

*"The first principle is that you must not fool yourself — and you are the easiest person to fool."* - Richard Feynman

*This is not cargo cult ISMS. This is evidence-based BC/DR compliance.*