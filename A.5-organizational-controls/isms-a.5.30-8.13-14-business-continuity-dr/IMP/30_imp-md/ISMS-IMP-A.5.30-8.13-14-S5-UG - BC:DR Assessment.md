**ISMS-IMP-A.5.30-8.13-14-S5-UG - BC/DR Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.13: Information Backup

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.30-8.13-14-S5-UG |
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


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
