**ISMS-IMP-A.5.30-8.13-14-S5 - BC/DR Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.13: Information Backup

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.30-8.13-14-S5 |
| **Version** | 1.0 |
| **Assessment Area** | Overall BC/DR Capability Assessment |
| **Related Policy** | ISMS-POL-A.5.30-8.13-14 (All Sections) |
| **Related Assessments** | IMP-S1 (BIA), IMP-S2 (Backup), IMP-S3 (Redundancy), IMP-S4 (Testing) |
| **Purpose** | Consolidate BC/DR metrics, calculate maturity score, provide executive dashboard |
| **Target Audience** | Executive Management, CISO, BC/DR Coordinator, Internal Auditors, External Auditors |
| **Assessment Type** | Comprehensive Evaluation |
| **Review Cycle** | Quarterly (Dashboard Update) + Annual (Comprehensive Assessment) |
| **Date** | [Date] |

---

# PART I: USER COMPLETION GUIDE
**Audience:** Security assessors, Control owners, Compliance officers

---

# Assessment Overview

## Purpose

**IMP-S5 Consolidates ALL BC/DR Assessments:**

```
┌───────────────────────────────────────────────────────┐
│               BC/DR ASSESSMENT PYRAMID                │
│                                                       │
│                   ▲ IMP-S5                           │
│                  ╱│╲ (This Guide)                    │
│                 ╱ │ ╲                                │
│                ╱  │  ╲ Consolidates:                 │
│               ╱   │   ╲                              │
│              ╱    │    ╲                             │
│             ╱ IMP-S1-S4 ╲                            │
│            ╱   Individual  ╲                         │
│           ╱   Assessments   ╲                        │
│          ╱                   ╲                       │
│         ╱                     ╲                      │
│        ╱                       ╲                     │
│       ╱    IMP-S1: BIA (RPO/RTO) ╲                   │
│      ╱     IMP-S2: Backup         ╲                  │
│     ╱      IMP-S3: Redundancy      ╲                 │
│    ╱       IMP-S4: Testing          ╲                │
│   ╱─────────────────────────────────╲               │
└───────────────────────────────────────────────────────┘
```

**Outputs:**
1. **BC/DR Maturity Score** (0-100%)
2. **Executive Dashboard** (one-page summary)
3. **Gap Summary** (prioritized remediation list)
4. **Compliance Summary** (regulatory requirements met)
5. **Trend Analysis** (improvement over time)

## Assessment Dimensions

**IMP-S5 evaluates BC/DR across 5 dimensions:**

| Dimension | Source | Weight | Measurement |
|-----------|--------|--------|-------------|
| **1. Preparedness** | IMP-S1 (BIA) | 20% | BIA completeness, RPO/RTO documented |
| **2. Backup Capability** | IMP-S2 | 25% | Backup coverage, RPO compliance, restore success rate |
| **3. Redundancy Implementation** | IMP-S3 | 25% | SPOF elimination, RTO capability, failover success |
| **4. Testing Maturity** | IMP-S4 | 20% | Testing compliance, RTO/RPO validation, issues remediated |
| **5. Documentation** | All IMP guides | 10% | Procedures documented, evidence collected, approvals |

---

# Assessment Methodology

## Data Collection (from IMP-S1 through S4)

**From IMP-S1 (BIA):**
```
Metrics:

  - Total systems assessed: [Count]
  - Systems with RPO/RTO defined: [Count]
  - BIA approved by management: [Yes/No]
  - BIA age: [Months since last update]
  - Dependency maps complete: [Yes/No]

```

**From IMP-S2 (Backup):**
```
Metrics:

  - Total systems: [Count]
  - Systems backed up: [Count]
  - Backup coverage %: [Backed Up / Total]
  - Tier 1 backup coverage %: [Should be 100%]
  - Tier 2 backup coverage %: [Should be 100%]
  - RPO compliance %: [Systems meeting RPO / Total]
  - Offsite backup compliance: [Tier 1/2 with offsite / Total Tier 1/2]
  - Backup success rate (last 90 days): [Successful backups / Total attempts]
  - Restore testing compliance: [Tests current / Tests required]

```

**From IMP-S3 (Redundancy):**
```
Metrics:

  - Tier 1/2 systems requiring redundancy: [Count]
  - Systems with redundancy: [Count]
  - Redundancy coverage %: [With redundancy / Required]
  - P1 SPOFs open: [Count - should be 0]
  - P2 SPOFs open: [Count]
  - Failover testing compliance: [Tests current / Tests required]
  - Average failover time: [Minutes]
  - RTO compliance %: [Systems meeting RTO / Total]

```

**From IMP-S4 (Testing):**
```
Metrics:

  - Component tests completed (last 12 months): [Count]
  - Integration tests completed: [Count]
  - DR scenario tests completed (annual): [Count - should be 1]
  - Testing compliance %: [Actual tests / Required tests]
  - RTO validation success rate: [Tests meeting RTO / Total tests]
  - Issues identified in testing: [Count]
  - Issues remediated: [Count]
  - Open issues: [Count]

```

## Maturity Scoring Framework

**Dimension 1: Preparedness (20%)**

| Maturity Level | Score | Criteria |
|---------------|-------|----------|
| **Level 5: Optimized** | 90-100% | BIA current (<6 months), all systems assessed, executive approval, documented dependencies, regular updates |
| **Level 4: Managed** | 75-89% | BIA complete (<12 months), Tier 1/2 assessed, management approval, most dependencies documented |
| **Level 3: Defined** | 50-74% | BIA exists (>12 months), Tier 1 assessed, basic documentation |
| **Level 2: Repeatable** | 25-49% | Partial BIA, critical systems identified, informal documentation |
| **Level 1: Initial** | 0-24% | No BIA or very incomplete, ad-hoc approach |

**Dimension 2: Backup Capability (25%)**

| Maturity Level | Score | Criteria |
|---------------|-------|----------|
| **Level 5: Optimized** | 90-100% | 100% Tier 1/2 coverage, RPO compliance 100%, offsite backups all critical, success rate >99%, quarterly restore testing |
| **Level 4: Managed** | 75-89% | >95% Tier 1/2 coverage, RPO compliance >90%, offsite backups most critical, success rate >95%, semi-annual testing |
| **Level 3: Defined** | 50-74% | >80% Tier 1/2 coverage, RPO compliance >75%, offsite backups some systems, success rate >90%, annual testing |
| **Level 2: Repeatable** | 25-49% | Partial coverage, inconsistent RPO, limited offsite, success rate >80%, sporadic testing |
| **Level 1: Initial** | 0-24% | Minimal coverage, no RPO alignment, no offsite, low success rate, no testing |

**Dimension 3: Redundancy Implementation (25%)**

| Maturity Level | Score | Criteria |
|---------------|-------|----------|
| **Level 5: Optimized** | 90-100% | 100% Tier 1 redundancy, 0 P1 SPOFs, RTO compliance 100%, automated failover, quarterly testing, geographic redundancy |
| **Level 4: Managed** | 75-89% | >90% Tier 1 redundancy, <3 P1 SPOFs, RTO compliance >90%, mostly automated, semi-annual testing |
| **Level 3: Defined** | 50-74% | >75% Tier 1 redundancy, some P1 SPOFs, RTO compliance >75%, manual failover, annual testing |
| **Level 2: Repeatable** | 25-49% | Partial redundancy, many SPOFs, inconsistent RTO, sporadic testing |
| **Level 1: Initial** | 0-24% | Minimal redundancy, extensive SPOFs, no RTO capability, no testing |

**Dimension 4: Testing Maturity (20%)**

| Maturity Level | Score | Criteria |
|---------------|-------|----------|
| **Level 5: Optimized** | 90-100% | All tests current, annual DR scenario, >95% RTO validation, all issues remediated, continuous improvement |
| **Level 4: Managed** | 75-89% | Most tests current, DR scenario within 18 months, >90% RTO validation, most issues remediated |
| **Level 3: Defined** | 50-74% | Critical tests current, DR scenario within 24 months, >80% RTO validation, some issues remediated |
| **Level 2: Repeatable** | 25-49% | Sporadic testing, no DR scenario or >3 years old, inconsistent RTO, limited remediation |
| **Level 1: Initial** | 0-24% | No testing or very limited, no DR scenario, unknown RTO capability |

**Dimension 5: Documentation (10%)**

| Maturity Level | Score | Criteria |
|---------------|-------|----------|
| **Level 5: Optimized** | 90-100% | All procedures documented, evidence complete, regular updates, version control, accessible to team |
| **Level 4: Managed** | 75-89% | Most procedures documented, good evidence, periodic updates, managed location |
| **Level 3: Defined** | 50-74% | Key procedures documented, basic evidence, some updates, stored centrally |
| **Level 2: Repeatable** | 25-49% | Limited procedures, minimal evidence, outdated, ad-hoc storage |
| **Level 1: Initial** | 0-24% | No procedures or very limited, no evidence, no updates |

## Overall BC/DR Maturity Calculation

```
BC/DR Maturity Score = 
  (Preparedness Score × 0.20) +
  (Backup Score × 0.25) +
  (Redundancy Score × 0.25) +
  (Testing Score × 0.20) +
  (Documentation Score × 0.10)

Example Calculation:
  Preparedness: 85% (Level 4)
  Backup: 92% (Level 5)
  Redundancy: 78% (Level 4)
  Testing: 70% (Level 3)
  Documentation: 80% (Level 4)
  
Overall Score = (85×0.20) + (92×0.25) + (78×0.25) + (70×0.20) + (80×0.10)
             = 17 + 23 + 19.5 + 14 + 8
             = 81.5% (Level 4 - Managed)
```

---

# Executive Dashboard

## Dashboard Components

**Page 1: BC/DR Readiness Summary**

```
┌─────────────────────────────────────────────────────────────────────┐
│  BUSINESS CONTINUITY & DISASTER RECOVERY READINESS DASHBOARD        │
│  [Organization Name]                                                │
│  Period: Q1 2026                              Date: 2026-03-31      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────┐   ┌────────────────────────────┐ │
│  │   OVERALL BC/DR MATURITY     │   │    MATURITY LEVEL          │ │
│  │                              │   │                            │ │
│  │          81.5%               │   │     Level 4: MANAGED       │ │
│  │                              │   │                            │ │
│  │   ████████████████░░░░░░░░   │   │   Target: Level 5 (90%+)  │ │
│  │                              │   │   Gap: 8.5%                │ │
│  └──────────────────────────────┘   └────────────────────────────┘ │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┤
│  │ DIMENSION BREAKDOWN                                             │
│  ├──────────────────────────────┬──────────┬────────────┬─────────┤
│  │ Dimension                    │ Score    │ Level      │ Status  │
│  ├──────────────────────────────┼──────────┼────────────┼─────────┤
│  │ 1. Preparedness (20%)        │ 85%      │ Level 4    │ ● Good  │
│  │ 2. Backup Capability (25%)   │ 92%      │ Level 5    │ ✓ Excellent │
│  │ 3. Redundancy (25%)          │ 78%      │ Level 4    │ ● Good  │
│  │ 4. Testing Maturity (20%)    │ 70%      │ Level 3    │ ⚠ Fair  │
│  │ 5. Documentation (10%)       │ 80%      │ Level 4    │ ● Good  │
│  └──────────────────────────────┴──────────┴────────────┴─────────┘
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┤
│  │ CRITICAL METRICS                                                │
│  ├──────────────────────────────┬──────────────────────────────────┤
│  │ Backup Coverage (Tier 1/2)   │ 100% (18/18 systems) ✓          │
│  │ Redundancy Coverage (Tier 1) │ 90% (9/10 systems) ⚠            │
│  │ P1 SPOFs Open                │ 1 (Target: 0) ⚠                 │
│  │ Testing Compliance           │ 85% (11/13 tests current) ●     │
│  │ RTO Validation Success       │ 92% (11/12 tests met RTO) ●     │
│  │ Backup Success Rate (90d)    │ 98.5% ✓                          │
│  └──────────────────────────────┴──────────────────────────────────┘
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┤
│  │ TOP PRIORITIES (Next Quarter)                                   │
│  ├─────────────────────────────────────────────────────────────────┤
│  │ 1. Eliminate remaining P1 SPOF (CRM database - no redundancy)  │
│  │    Owner: DBA Team | Due: 2026-04-30 | Investment: CHF 12K     │
│  │                                                                 │
│  │ 2. Complete overdue integration tests (2 tests overdue)        │
│  │    Owner: BC/DR Coordinator | Due: 2026-04-15 | Cost: Internal│
│  │                                                                 │
│  │ 3. Update BIA (12 months old, approaching refresh)             │
│  │    Owner: BC/DR Coordinator | Due: 2026-06-30 | Cost: Internal│
│  └─────────────────────────────────────────────────────────────────┘
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┤
│  │ TREND (Last 4 Quarters)                                         │
│  ├─────────────────────────────────────────────────────────────────┤
│  │  90% ┤                                                   /✓     │
│  │  80% ┤                                          /──────●        │
│  │  70% ┤                                 /──────●                 │
│  │  60% ┤                        /──────●                          │
│  │  50% ┤               /──────●                                   │
│  │      └────┬────┬────┬────┬────┬────┬────┬────┬────┬────        │
│  │          Q2'25 Q3'25 Q4'25 Q1'26                               │
│  │                                                                 │
│  │  ↗ Improvement: +21.5% over 12 months                          │
│  └─────────────────────────────────────────────────────────────────┘
└─────────────────────────────────────────────────────────────────────┘

Legend: ✓ Excellent (90%+) | ● Good (75-89%) | ⚠ Fair (50-74%) | ✗ Poor (<50%)
```

---

# Gap Analysis & Remediation Roadmap

## Gap Summary

```
BC/DR GAP ANALYSIS
Assessment Date: 2026-03-31

═══════════════════════════════════════════════════════════════════════
CRITICAL GAPS (P1 - Immediate Action Required)
═══════════════════════════════════════════════════════════════════════
1. CRM Database - No Redundancy
   System: CRM (SYS-020)
   Tier: Tier 2
   Current State: Single instance, no failover
   Required State: Hot standby or database replication
   RTO Gap: Current 8h (restore), Required 4h
   Impact: Customer service degraded during outage
   Remediation: Implement SQL Always On (2-node cluster)
   Cost: CHF 12,000 (licensing + setup)
   Owner: DBA Team
   Due: 2026-04-30
   Status: IN PROGRESS (40% complete)

═══════════════════════════════════════════════════════════════════════
HIGH PRIORITY GAPS (P2 - Address Within 90 Days)
═══════════════════════════════════════════════════════════════════════
2. Integration Testing Overdue (2 tests)
   Systems: ERP System, Email
   Last Tested: ERP (2025-08-15 - 7 months ago), Email (2025-09-20 - 6 months)
   Required: Semi-annual (every 6 months)
   Impact: Unknown recovery capability, audit finding risk
   Remediation: Schedule and complete integration tests
   Cost: Internal (staff time)
   Owner: BC/DR Coordinator
   Due: 2026-04-15
   Status: SCHEDULED (test date: 2026-04-10)

3. BIA Approaching Refresh
   Current BIA Date: 2025-04-01 (12 months old)
   Policy Requirement: Annual refresh
   Impact: RPO/RTO requirements may be outdated, new systems not assessed
   Remediation: Conduct annual BIA refresh
   Cost: Internal (100-150 person-hours)
   Owner: BC/DR Coordinator
   Due: 2026-06-30
   Status: NOT STARTED (planned Q2 2026)

4. Geographic Redundancy for E-commerce (Recommended)
   System: E-commerce Platform (SYS-010)
   Tier: Tier 1
   Current: Multi-AZ (West Europe)
   Recommended: Multi-region (West Europe + North Europe)
   RTO Current: 1h (warm standby in same region)
   RTO Target: 15min (hot standby in secondary region)
   Justification: Customer-facing revenue system, high availability desired
   Cost: +CHF 8,000/year (secondary region resources)
   Owner: Infrastructure Team
   Due: 2026-09-30
   Status: BUDGETED (pending approval)

═══════════════════════════════════════════════════════════════════════
MEDIUM PRIORITY GAPS (P3 - Address Within 180 Days)
═══════════════════════════════════════════════════════════════════════
5. Backup Testing Automation
   Current: Manual restore testing (time-consuming)
   Proposed: Automated restore validation (Veeam SureBackup)
   Benefit: Increase testing frequency, reduce manual effort
   Cost: Included in Veeam license (configuration only)
   Owner: Backup Administrator
   Due: 2026-09-30
   Status: NOT STARTED

6. DR Scenario Test Frequency (Improvement)
   Current: Annual DR scenario
   Proposed: Semi-annual for critical systems
   Benefit: Higher confidence, more trained staff
   Cost: +100 person-hours/year (second scenario)
   Owner: BC/DR Coordinator
   Due: Decision by 2026-06-30
   Status: UNDER REVIEW

═══════════════════════════════════════════════════════════════════════
SUMMARY
═══════════════════════════════════════════════════════════════════════
Total Gaps: 6

  - P1 (Critical): 1
  - P2 (High): 3
  - P3 (Medium): 2

Remediation Investment:

  - One-time: CHF 12,000
  - Annual recurring: CHF 8,000
  - Internal effort: 250 person-hours

Expected Maturity Improvement: 81.5% → 87% (Level 4 → approaching Level 5)
```

---

# Compliance Summary

```
REGULATORY COMPLIANCE SUMMARY

═══════════════════════════════════════════════════════════════════════
ISO 27001:2022 COMPLIANCE
═══════════════════════════════════════════════════════════════════════
Control A.8.13 - Information Backup: ✓ COMPLIANT
  Evidence:

    - 100% Tier 1/2 backup coverage
    - Quarterly restore testing (Tier 1)
    - Documented backup procedures
    - 98.5% backup success rate

Control A.8.14 - Redundancy: ● MOSTLY COMPLIANT
  Evidence:

    - 90% Tier 1 redundancy coverage
    - 1 P1 SPOF remaining (remediation in progress)
    - Failover testing completed

  Gap: 1 Tier 2 system without redundancy (CRM)
  Remediation: Due 2026-04-30

Control A.5.30 - ICT BC Readiness: ✓ COMPLIANT
  Evidence:

    - BIA current (<12 months)
    - BC/DR plans documented
    - Annual DR scenario completed (2025-06-15)
    - Testing program established

═══════════════════════════════════════════════════════════════════════
SWISS nDSG COMPLIANCE
═══════════════════════════════════════════════════════════════════════
Art. 8 - Data Security Measures: ✓ COMPLIANT
  Evidence:

    - Backup for all systems processing personal data
    - Encryption for Restricted/Confidential data
    - Tested restore capability

═══════════════════════════════════════════════════════════════════════
EU GDPR COMPLIANCE (if processing EU personal data)
═══════════════════════════════════════════════════════════════════════
Art. 32(1)(c) - Restore Availability: ✓ COMPLIANT
  Evidence:

    - Documented RPO/RTO for systems processing personal data
    - Quarterly restore testing
    - Proven recovery capability

═══════════════════════════════════════════════════════════════════════
DORA COMPLIANCE (if financial entity)
═══════════════════════════════════════════════════════════════════════
Art. 12 - Backup Policies: ✓ COMPLIANT
  Evidence:

    - Backup policy documented (ISMS-POL-A.5.30-8.13-14)
    - Backup procedures implemented (IMP-S2)
    - Regular testing
    - Restoration capability proven

Art. 11 - ICT Resilience: ✓ COMPLIANT
  Evidence:

    - Redundancy implemented for critical systems
    - RTO capability validated
    - Annual DR scenario

```

---

# Assessment Workbook (1 Consolidated Sheet)

## Consolidated_Dashboard

**Metrics (auto-calculated from IMP-S1 through S4):**

| Section | Metric | Value | Target | Status |
|---------|--------|-------|--------|--------|
| **BIA** | Systems Assessed | 85 | 85 | ✓ |
| **BIA** | BIA Age (months) | 12 | <12 | ⚠ |
| **Backup** | Tier 1/2 Coverage % | 100% | 100% | ✓ |
| **Backup** | RPO Compliance % | 95% | >90% | ✓ |
| **Backup** | Success Rate (90d) | 98.5% | >95% | ✓ |
| **Redundancy** | Tier 1 Coverage % | 90% | 100% | ⚠ |
| **Redundancy** | P1 SPOFs Open | 1 | 0 | ⚠ |
| **Redundancy** | RTO Compliance % | 92% | >90% | ✓ |
| **Testing** | Testing Compliance % | 85% | >90% | ● |
| **Testing** | DR Scenario (annual) | Yes (2025-06) | Yes | ✓ |
| **Overall** | **BC/DR Maturity** | **81.5%** | **90%+** | **●** |

**Charts:**

- Radar chart: 5 dimensions (Preparedness, Backup, Redundancy, Testing, Documentation)
- Trend line: Maturity score over last 4 quarters
- Gauge: Overall BC/DR readiness (0-100%)

---

# Continuous Improvement

**Quarterly Assessment Cycle:**
```
Q1 (January-March):

  - Update dashboard with Q4 data
  - Review gap remediation progress
  - Executive presentation

Q2 (April-June):

  - BIA refresh (annual)
  - Update BIA metrics
  - Schedule Q2 testing

Q3 (July-September):

  - Mid-year assessment
  - Trend analysis (H1 vs H2)
  - Budget planning for improvements

Q4 (October-December):

  - Annual DR scenario
  - Year-end comprehensive assessment
  - Set targets for next year

```

---

**END OF ISMS-IMP-A.5.30-8.13-14-S5**

**TOTAL: ~850 lines**

*"Measure, improve, repeat. BC/DR is a continuous journey."*

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

# Overview

## Purpose

This implementation guide provides step-by-step instructions for conducting comprehensive assessments of BC/DR compliance to identify gaps and track remediation.

**Critical Principle:** Assessment must be evidence-based, not self-reported. Verify claims through testing and documentation review.

## Relationship to Policy

This guide implements:

- **Policy S5:** Compliance Measurement and Gap Analysis
- **Annex-B** Section 6: Compliance Calculation Formulas
- All assessment workbooks (WB1-5)

## Expected Outcomes

Upon completion of assessment, [Organization] will have:

- Documented BC/DR compliance status (backup, redundancy, RPO/RTO, testing)
- Identified gaps (where capability < requirement)
- Prioritized gaps (risk-based prioritization)
- Remediation plans (with owners and timelines)
- Trend analysis (compliance improving/stable/degrading)
- Dashboard for executive visibility

---

# Assessment Planning

## Define Assessment Scope

**Step 1: Determine Assessment Frequency**

From Policy S5:

- **Quarterly:** Operational assessments (backup coverage, testing compliance)
- **Semi-Annual:** Detailed compliance review (RPO/RTO, gap analysis)
- **Annual:** Comprehensive assessment (full BC/DR maturity)

**Step 2: Identify Systems in Scope**

Assessment scope should include:

- All systems identified in BIA as Critical or Important (Tier 1-2)
- All systems with documented RPO/RTO requirements
- All production systems (even if not yet assessed in BIA)

**Out of Scope:**

- Test/development systems (unless specifically included in BIA)
- Decommissioned systems

**Step 3: Assemble Assessment Team**

Assessment team should include:

- BC/DR Coordinator (leads assessment)
- Backup Administrator (backup compliance data)
- Infrastructure team (redundancy compliance data)
- System owners (validate findings)
- Internal Audit (optional, for independent verification)

## Prepare Assessment Tools

**Step 4: Prepare Assessment Workbooks**

Use assessment workbooks:

- **Workbook 1:** Backup Inventory & Coverage (assess backup compliance)
- **Workbook 2:** Redundancy Analysis & SPOF (assess redundancy compliance)
- **Workbook 3:** RPO/RTO Compliance Matrix (assess requirement vs capability)
- **Workbook 4:** Testing Results Tracker (assess testing compliance)
- **Workbook 5:** BC/DR Dashboard (consolidate all metrics)

**If First Assessment:**

- Generate workbooks using Python scripts (Phase 3)
- Populate with current data
- Establish baseline metrics

**If Subsequent Assessment:**

- Update existing workbooks
- Compare to previous quarter (trend analysis)

---

# Backup Coverage Assessment

## Inventory All Systems

**Step 5: Create System Inventory**

Starting from asset inventory (A.5.9), list all systems:

- System name
- System owner
- Criticality (from BIA)
- RPO requirement (from BIA)

**Step 6: Assess Backup Status per System**

For each system, verify:

| System | Criticality | Backup Status | Backup Solution | Frequency | Last Backup | Offsite | Immutable |
|--------|-------------|---------------|-----------------|-----------|-------------|---------|-----------|
| E-Commerce | Tier 1 | ✅ Backed up | Veeam | Hourly | 2 hours ago | ✅ Yes | ✅ Yes |
| ERP | Tier 2 | ✅ Backed up | Veeam | Daily | Last night | ✅ Yes | ❌ No |
| File Server | Tier 3 | ✅ Backed up | Windows Backup | Weekly | 2 days ago | ❌ No | ❌ No |
| Test DB | Tier 4 | ❌ Not backed up | N/A | N/A | N/A | N/A | N/A |

**Data Sources:**

- Backup solution reports (Veeam, Commvault, etc.)
- Backup job configurations
- Backup monitoring dashboards
- Cloud storage verification

**Step 7: Calculate Backup Coverage**

**Formula (from Annex-B Section 6.3):**
```
Backup Coverage (%) = (Systems With Backup / Total In-Scope Systems) × 100

Critical System Coverage (%) = (Critical Systems With Backup / Total Critical Systems) × 100
```

**Example:**

- Total systems: 50
- Systems with backup: 45
- Coverage: 45/50 = 90%
- Critical systems: 10
- Critical with backup: 10
- Critical coverage: 10/10 = 100% ✅

**Target:** ≥95% overall, 100% for Critical systems

**Step 8: Identify Coverage Gaps**

Systems without backup = Coverage Gaps:

- Test DB (Tier 4) - Not backed up
- Legacy Application (Tier 3) - Not backed up

**Assess:**

- Why not backed up? (Forgotten? Deliberately excluded?)
- Should it be backed up? (Check BIA)
- If yes → Gap, remediate

---

# Redundancy Coverage Assessment

## Assess Redundancy Status

**Step 9: Inventory Systems Requiring Redundancy**

From BIA, systems with RTO < 4 hours require redundancy:

- E-Commerce Website (RTO 2 hours)
- Email System (RTO 4 hours)
- Payment Gateway (RTO 1 hour)

**Step 10: Verify Redundancy Implementation**

For each system requiring redundancy:

| System | RTO Req | Redundancy Status | Architecture | Failover Type | Last Test | Result |
|--------|---------|-------------------|--------------|---------------|-----------|--------|
| E-Commerce | 2 hours | ✅ Implemented | Active-Passive | Automatic | Last quarter | ✅ Success |
| Email | 4 hours | ⚠️ Partial | Single server with daily backup | Manual restore | Never | ❌ N/A |
| Payment Gateway | 1 hour | ✅ Implemented | Active-Active | Automatic | Last month | ✅ Success |

**Data Sources:**

- Infrastructure documentation
- Load balancer configurations
- Clustering configurations
- Failover test results

**Step 11: SPOF Analysis Verification**

For systems with redundancy, verify SPOF analysis completed (from IMP-S3):

- SPOF register populated
- SPOFs identified and mitigated
- Open SPOFs tracked with remediation plans

**SPOF Metrics:**

- Total SPOFs identified
- SPOFs mitigated
- Open SPOFs (requiring remediation)
- Critical SPOFs (affecting Critical systems)

**Target:** Zero open SPOFs for Critical systems

**Step 12: Calculate Redundancy Coverage**

**Formula:**
```
Redundancy Coverage (%) = 
  (Systems with Redundancy / Systems Requiring Redundancy) × 100
```

**Example:**

- Systems requiring redundancy (RTO < 4 hours): 3
- Systems with redundancy implemented: 2 (E-Commerce, Payment Gateway)
- Coverage: 2/3 = 67% (Gap: Email system)

**Target:** 100% for Critical systems

---

# RPO/RTO Compliance Assessment

## Assess RPO Compliance

**Step 13: Compare RPO Requirement vs Capability**

For each system, compare:

- **RPO Requirement** (from BIA)
- **Actual Backup Frequency** (from backup configuration)

**Example:**

| System | RPO Req | Backup Frequency | RPO Compliant | Gap |
|--------|---------|------------------|---------------|-----|
| E-Commerce | 1 hour | Hourly (1 hour) | ✅ Yes | 0 hours |
| ERP | 4 hours | Daily (24 hours) | ❌ No | 20 hours |
| File Server | 24 hours | Weekly (168 hours) | ❌ No | 144 hours |

**Formula (from Annex-B Section 6.1):**
```
RPO Compliant = IF (Backup Frequency ≤ RPO Requirement) THEN "Yes" ELSE "No"

RPO Gap = MAX(0, Backup Frequency - RPO Requirement)
```

**Step 14: Calculate RPO Compliance**

**Formula:**
```
RPO Compliance (%) = (Systems Meeting RPO / Total Systems) × 100
```

**Example:**

- Total systems: 3
- Meeting RPO: 1 (E-Commerce)
- Compliance: 1/3 = 33% (Low - remediation needed)

**Target:** ≥90% overall, 100% for Critical systems

## Assess RTO Compliance

**Step 15: Compare RTO Requirement vs Capability**

**RTO Capability = Actual Recovery Time (from testing)**

**Critical:** RTO capability MUST be based on tested recovery time, not assumptions.

**Example:**

| System | RTO Req | Actual Recovery Time (Tested) | RTO Compliant | Gap |
|--------|---------|-------------------------------|---------------|-----|
| E-Commerce | 2 hours | 0.5 hours (failover tested) | ✅ Yes | 0 |
| ERP | 12 hours | 8 hours (restore tested) | ✅ Yes | 0 |
| File Server | 48 hours | Not tested (assumed 24 hours) | ❓ Unknown | N/A |

**If Not Tested:**

- Cannot determine RTO compliance
- Mark as "Unknown" or "Non-Compliant" (conservative approach)
- Require testing before claiming compliance

**Formula (from Annex-B Section 6.2):**
```
RTO Compliant = IF (Actual Recovery Time ≤ RTO Requirement) THEN "Yes" ELSE "No"

RTO Gap = MAX(0, Actual Recovery Time - RTO Requirement)
```

**Step 16: Calculate RTO Compliance**

**Formula:**
```
RTO Compliance (%) = (Systems Meeting RTO / Total Systems) × 100
```

**Example:**

- Total systems: 3
- Meeting RTO: 2 (E-Commerce, ERP)
- Compliance: 2/3 = 67%
- Note: File Server not tested, cannot confirm compliance

**Target:** ≥90% overall, 100% for Critical systems

---

# Testing Compliance Assessment

## Assess Testing Status

**Step 17: Verify Testing Schedule Compliance**

From Policy S2, S3, S5:

- **Critical systems:** Quarterly restore/failover testing
- **Important systems:** Semi-annual testing
- **Standard systems:** Annual testing

**For each system, assess:**

| System | Criticality | Required Frequency | Last Test Date | Status |
|--------|-------------|-------------------|----------------|--------|
| E-Commerce | Tier 1 | Quarterly (90 days) | 45 days ago | ✅ On Time |
| Email | Tier 2 | Semi-Annual (180 days) | 200 days ago | ❌ Overdue (20 days) |
| File Server | Tier 3 | Annual (365 days) | 320 days ago | ✅ On Time |
| Payment Gateway | Tier 1 | Quarterly (90 days) | Never tested | ❌ Overdue |

**Data Sources:**

- Assessment Workbook 4 (Testing Results Tracker)
- Test reports and evidence
- Testing calendar

**Step 18: Calculate Testing Compliance**

**Formula (from Annex-B Section 6.4):**
```
Testing Compliant = 
  IF (Days Since Last Test ≤ Required Frequency) THEN "Compliant" ELSE "Overdue"

Testing Compliance (%) = 
  (Systems Tested On Schedule / Systems Requiring Testing) × 100
```

**Example:**

- Systems requiring testing: 4
- Tested on schedule: 2 (E-Commerce, File Server)
- Compliance: 2/4 = 50% (Low - testing gaps)

**Target:** ≥80% overall, ≥95% for Critical systems

## Assess Test Success Rate

**Step 19: Analyze Test Results**

Of tests conducted, how many were successful?

| Test Type | Tests Conducted | Successful | Failed | Partial | Success Rate |
|-----------|----------------|------------|--------|---------|--------------|
| Backup Restore | 25 | 22 | 2 | 1 | 88% |
| Failover | 8 | 6 | 1 | 1 | 75% |
| DR Simulation | 1 | 0 | 1 | 0 | 0% (Failed) |

**Low success rate indicates:**

- Procedures don't work as documented
- Infrastructure issues
- Training gaps

**Target:** ≥90% success rate for backup restore, ≥85% for failover

---

# Gap Identification and Analysis

## Consolidate All Gaps

**Step 20: Create Master Gap List**

Consolidate gaps from all assessments:

**Coverage Gaps:**

- Systems without backup (should be backed up per BIA)
- Systems without redundancy (RTO < 4 hours, no redundancy)

**RPO/RTO Compliance Gaps:**

- Systems where backup frequency < RPO requirement
- Systems where recovery time > RTO requirement

**Testing Gaps:**

- Systems overdue for testing
- Systems never tested

**SPOF Gaps:**

- Open SPOFs (not yet mitigated)

**Example Gap List:**

| Gap ID | Gap Type | System | Description | Impact |
|--------|----------|--------|-------------|--------|
| GAP-001 | Coverage | Legacy App | No backup | Cannot recover if failure |
| GAP-002 | RPO | ERP System | Daily backup, RPO 4 hours | 20 hours data loss possible |
| GAP-003 | RTO | Email | No redundancy, RTO 4 hours | Cannot meet RTO (restore takes 12 hours) |
| GAP-004 | Testing | Payment Gateway | Never tested failover | Unknown if failover works |
| GAP-005 | SPOF | E-Commerce | Single ISP | Internet outage = website down |

**Step 21: Categorize Gaps**

**Gap Types:**

- **Critical:** Tier 1 system not protected OR regulatory compliance gap
- **High:** Tier 2 system not meeting requirements OR significant gap in Tier 1
- **Medium:** Tier 3 system gap OR minor gap in Tier 2
- **Low:** Tier 4 system gap OR optimization opportunity

---

# Gap Prioritization

## Calculate Gap Risk Scores

**Step 22: Apply Risk Scoring Formula**

**Formula (from Annex-B Section 8.3):**
```
Gap Risk Score = Criticality × Gap Severity × Likelihood

Criticality:

- Critical system (Tier 1) = 10 points
- Important system (Tier 2) = 5 points
- Standard system (Tier 3) = 2 points
- Low criticality (Tier 4) = 1 point

Gap Severity:

- No backup/redundancy = 10 points
- RPO/RTO gap > 50% of requirement = 7 points
- RPO/RTO gap 25-50% = 4 points
- RPO/RTO gap < 25% = 2 points
- Testing gap = 3 points
- Documentation gap = 1 point

Likelihood:

- High (frequent failures) = 3×
- Medium = 2×
- Low (rare failures) = 1×

```

**Example:**

| Gap | Criticality | Severity | Likelihood | Risk Score | Priority |
|-----|-------------|----------|------------|------------|----------|
| GAP-003 (Email RTO) | 5 (Tier 2) | 7 (>50% gap) | 2× (Medium) | 5 × 7 × 2 = 70 | Medium |
| GAP-004 (Payment Gtw Testing) | 10 (Tier 1) | 3 (Testing) | 3× (High) | 10 × 3 × 3 = 90 | High |
| GAP-005 (E-Commerce ISP SPOF) | 10 (Tier 1) | 7 (SPOF) | 2× (Medium) | 10 × 7 × 2 = 140 | High |

**Step 23: Prioritize Gaps**

**Priority Levels (from Policy S5 Section 8.3):**

- **Risk Score > 200:** Critical Priority (remediate within 90 days)
- **Risk Score 100-200:** High Priority (remediate within 6 months)
- **Risk Score 50-100:** Medium Priority (remediate within 1 year)
- **Risk Score < 50:** Low Priority (remediate as resources permit or accept risk)

**Sort gaps by risk score (highest first) for remediation planning.**

---

# Remediation Planning and Tracking

## Develop Remediation Plans

**Step 24: Create Remediation Plan per Gap**

For each gap:

**Remediation Plan Template:**
```
Gap ID: GAP-003
Gap Description: Email system RTO gap (RTO 4 hours, actual recovery 12 hours)
Impact: Cannot meet business requirement for email recovery
Priority: High (Risk Score 70)

Remediation Options:
Option 1: Implement Active-Passive redundancy with automatic failover

  - Cost: $25K (infrastructure)
  - Time: 3 months
  - Result: RTO < 1 hour (exceeds requirement)

Option 2: Improve restore procedure and increase backup frequency

  - Cost: $5K (faster backup storage)
  - Time: 1 month
  - Result: RTO 6 hours (still above requirement, partial improvement)

Option 3: Accept Risk

  - Cost: $0
  - Risk: Email unavailable for 12 hours during failure
  - Approval Required: Business owner + Executive

Recommended: Option 1 (meets requirement, provides buffer)

Remediation Plan:
1. Design Active-Passive architecture (Week 1-2)
2. Procure infrastructure (Week 3-4)
3. Deploy and configure redundancy (Week 5-8)
4. Test failover (Week 9-10)
5. Document and train (Week 11-12)

Owner: Infrastructure Manager
Target Completion: 90 days from approval
Budget: $25K
Status: Awaiting approval
```

**Step 25: Track Remediation Progress**

**Gap Remediation Register (Assessment Workbook 3):**

| Gap ID | Description | Priority | Remediation Plan | Owner | Target Date | Status | % Complete |
|--------|-------------|----------|------------------|-------|-------------|--------|------------|
| GAP-003 | Email RTO gap | High | Implement redundancy | Infra Mgr | 90 days | In Progress | 40% |
| GAP-004 | Payment Gtw testing | High | Conduct failover test | BC/DR Coord | 30 days | Open | 0% |
| GAP-005 | E-Commerce ISP SPOF | High | Add second ISP | Network Eng | 6 months | Open | 0% |

**Review Frequency:**

- Monthly: BC/DR Coordinator reviews progress, updates status
- Quarterly: Report to BC/DR Steering Committee

## Risk Acceptance Process

**Step 26: Document Risk Acceptance (If Applicable)**

Some gaps may be accepted rather than remediated:

**Acceptable Risk Acceptance Reasons:**

- Cost of remediation > cost of risk
- Technical infeasibility
- Temporary gap (remediation in progress)
- Compensating controls

**Risk Acceptance Requirements (from Policy S4 Section 5.4):**

- Risk documented in risk register
- Business owner approves (not IT alone)
- Executive approval for Critical system gaps
- Risk reviewed annually (conditions may change)

**Risk Acceptance Documentation:**
```
Gap ID: GAP-001 (Legacy App - No Backup)
Risk: Data loss if system fails
Impact: Low (system rarely used, data can be recreated)
Cost to Remediate: $10K (backup solution licensing + storage)
Cost of Risk: $2K (estimated cost to recreate data)
Decision: Accept Risk (cost of remediation > cost of risk)
Approved By: Business Owner (Signature) + CFO (Signature)
Review Date: Annual (next review: 1 year from acceptance)
```

---

# Assessment Reporting and Dashboards

## Prepare Assessment Report

**Step 27: Create Quarterly Assessment Report**

**Report Structure:**

**1. Executive Summary** (1 page):

- Overall BC/DR maturity score (0-100%)
- Key findings (critical gaps, compliance status)
- Trends (improving/stable/degrading)
- Recommendations

**2. Compliance Metrics:**

- Backup coverage: X% (target ≥95%)
- RPO compliance: X% (target ≥90%)
- RTO compliance: X% (target ≥90%)
- Testing compliance: X% (target ≥80%)
- Redundancy coverage: X% (Critical systems, target 100%)

**3. Gap Summary:**

- Total gaps: X
- By priority: Critical (X), High (X), Medium (X), Low (X)
- Top 5 gaps (by risk score)
- Remediation progress: X% gaps closed since last quarter

**4. Testing Summary:**

- Tests conducted: X
- Success rate: X%
- Failed tests and remediation status

**5. Recommendations:**

- Priority gaps requiring immediate attention
- Resource needs (budget, personnel)
- Strategic initiatives (redundancy projects, etc.)

**Step 28: Create Executive Dashboard**

**Dashboard Metrics (from Policy S5 Section 10.1):**

**Overall BC/DR Maturity Score:**

- Single number 0-100% (weighted composite of all metrics)
- Color: Green (>85%), Yellow (70-85%), Red (<70%)

**Coverage Metrics:**

- Backup Coverage (overall and by criticality)
- Redundancy Coverage (Critical systems)

**Compliance Metrics:**

- RPO Compliance (%)
- RTO Compliance (%)
- Testing Compliance (%)

**Gap Metrics:**

- Total open gaps
- Critical/High priority gaps (requiring immediate attention)
- Gap trend (↗ increasing, → stable, ↘ decreasing)

**Trend Indicators:**

- Quarter-over-quarter change (improving/degrading)
- Arrows showing direction

**Step 29: Distribute Reports**

**Report Distribution:**

- **Detailed Assessment Report:** BC/DR Coordinator, IT Management, Internal Audit
- **Executive Dashboard:** CISO, CIO, Executive Management, Board
- **Gap Remediation Status:** Gap owners, BC/DR Steering Committee

**Cadence:**

- Quarterly assessment reports
- Monthly gap remediation status updates

---

# Common Pitfalls and How to Avoid

## Self-Reported Data (Not Verified)

**Pitfall:** Assessment based on what people claim, not verified evidence.

**Example:** System owner says "Yes, we're backed up" but no backup actually exists.

**How to Avoid:**

- **Verify claims through evidence:**
  - Backup status → Check backup solution reports
  - Testing status → Review test documentation
  - Redundancy → Review infrastructure configs and test results
- Don't rely solely on questionnaires or self-assessment

## Assuming Compliance (Not Measured)

**Pitfall:** Assume systems are compliant without actually measuring.

**Example:** "We implemented backups 2 years ago, so we're compliant." Reality: Many backup jobs failing, nobody noticed.

**How to Avoid:**

- Regular measurement (quarterly minimum)
- Use assessment workbooks to systematically evaluate
- Track metrics over time

## Gaps Identified But Not Tracked

**Pitfall:** Gaps identified in assessment, documented, then forgotten.

**Example:** Assessment identifies 15 gaps. 6 months later, same 15 gaps still open.

**How to Avoid:**

- Gap Remediation Register mandatory (Step 25)
- Monthly progress reviews
- Gap owners accountable for remediation
- Escalate stalled gaps to management

## No Remediation Accountability

**Pitfall:** Gaps assigned to owners, but no follow-up or consequences for not completing remediation.

**How to Avoid:**

- Clear ownership (one person accountable per gap)
- Target dates committed
- Monthly status reviews
- Escalation for overdue remediation
- Include gap remediation in performance objectives

## Stale Assessments (Not Updated)

**Pitfall:** Assessment done once, never updated. Compliance status unknown.

**How to Avoid:**

- Quarterly assessment cadence (minimum)
- Assessment integrated into operational processes
- Assessment Workbooks continuously updated (not just during formal assessment)

---

# Verification and Sign-Off

## Completion Checklist

**Assessment program established when:**

- [ ] Assessment scope defined (which systems, which controls)
- [ ] Assessment workbooks prepared (WB1-5)
- [ ] First assessment completed:
  - [ ] Backup coverage assessed
  - [ ] Redundancy coverage assessed
  - [ ] RPO/RTO compliance assessed
  - [ ] Testing compliance assessed
- [ ] Gaps identified and documented (Gap Register)
- [ ] Gaps prioritized (risk scoring applied)
- [ ] Remediation plans created (for high/critical gaps)
- [ ] Assessment report prepared (findings, metrics, recommendations)
- [ ] Executive dashboard created (visual summary)
- [ ] Reports distributed to stakeholders
- [ ] Quarterly assessment schedule established
- [ ] Gap remediation tracking process established

## Evidence to Collect

**Assessment Evidence:**

- Assessment workbooks (WB1-5, completed)
- Data sources (backup reports, infrastructure configs, test results)
- Gap register (all identified gaps)
- Remediation plans (per gap)
- Risk acceptance documentation (if applicable)
- Assessment reports (quarterly)
- Executive dashboards
- Trend analysis (comparison to previous quarters)

**Storage:** Evidence repository, retained 3+ years

## Stakeholder Approval

**Required Approvals:**

| Stakeholder | Approval For | Evidence |
|-------------|-------------|----------|
| BC/DR Coordinator | Assessment methodology and findings | Signature on assessment report |
| IT Management | Acceptance of findings and commitment to remediation | Signature on assessment report |
| CISO | Assessment meets compliance requirements | Approval of executive dashboard |
| BC/DR Steering Committee | Approval of remediation priorities and resource allocation | Meeting minutes approving assessment findings |

---

# Next Steps

## Ongoing Assessment Operations

**Quarterly:**

- Update assessment workbooks (WB1-5)
- Calculate compliance metrics
- Identify new gaps
- Update gap register
- Prepare quarterly assessment report
- Review with BC/DR Steering Committee

**Monthly:**

- Review gap remediation progress
- Update remediation status
- Escalate stalled remediations

**Annually:**

- Comprehensive BC/DR maturity assessment
- Review and update assessment methodology
- Benchmark against industry standards (if available)

## Integration with BC/DR Program

- **Continuous Improvement:** Assessment findings drive plan updates
- **Budget Planning:** Gap remediation costs inform BC/DR budget
- **Audit Readiness:** Assessment evidence supports audit compliance
- **Executive Visibility:** Dashboard provides transparency into BC/DR posture

---

**END OF SPECIFICATION**

---

*"The only source of knowledge is experience."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-01-31 -->
