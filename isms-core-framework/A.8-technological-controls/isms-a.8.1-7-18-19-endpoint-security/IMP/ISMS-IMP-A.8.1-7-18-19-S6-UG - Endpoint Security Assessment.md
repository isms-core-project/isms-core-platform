<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.1-7-18-19-S6-UG:framework:UG:a.8.1-7-18-19-s6 -->
**ISMS-IMP-A.8.1-7-18-19-S6-UG - Endpoint Security Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.1: User Endpoint Devices

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S6-UG |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Endpoint Security Compliance Assessment |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19 (All Sections) |
| **Purpose** | Consolidate endpoint security assessments (S1-S5), calculate overall compliance, provide executive dashboard |
| **Target Audience** | CISO, IT Director, Security Management, Compliance Officers, Auditors, Executive Leadership |
| **Assessment Type** | Consolidated Compliance & Governance |
| **Review Cycle** | Quarterly (full assessment) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial consolidated assessment framework | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.1-7-18-19-S6-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.1-7-18-19-S6 - Endpoint Security Assessment (Consolidated)

#### What This Assessment Covers

This is the **MASTER ASSESSMENT** that consolidates all endpoint security assessments (S1-S5) into a unified compliance view. This answers:

- What is the overall endpoint security posture?
- Are all four controls (A.8.1, A.8.7, A.8.18, A.8.19) compliant?
- What are the critical gaps across all endpoint security domains?
- What is the risk profile of the endpoint landscape?
- What actions are required to achieve compliance?
- Are we ready for ISO 27001 audit?

#### Key Principle

**This is the EXECUTIVE VIEW of endpoint security:**

- ❌ Component: "S3 shows 87% malware coverage"
- ✅ Integrated: "Overall endpoint security is Yellow: 87% malware coverage, 23 unprotected critical endpoints, remediation by Q2"

This assessment provides the **single source of truth** for endpoint security compliance status.

#### What You'll Consolidate

**From S1 (Endpoint Discovery):**

- Total endpoint inventory
- Endpoint classification and criticality
- Endpoint management coverage

**From S2 (Security Baselines):**

- Baseline compliance per endpoint type
- Configuration drift
- Encryption coverage

**From S3 (Malware Protection):**

- Anti-malware/EDR coverage
- Signature currency
- Scan compliance

**From S4 (Software Controls):**

- Approved software list completeness
- Unauthorized software count
- Application control deployment
- Patch compliance

**From S5 (Privileged Utilities):**

- Privileged utility access controls
- Usage monitoring
- Security bypass tool status

**Plus:**

- Cross-control gap analysis
- Risk prioritization
- Consolidated remediation roadmap
- Executive dashboard

#### How This Relates to Other Assessments

| Assessment | Focus | S6 Uses This Data |
|------------|-------|-------------------|
| **S1 - Endpoint Discovery** | Inventory | Endpoint counts, criticality distribution |
| **S2 - Security Baselines** | Configuration | Baseline compliance %, encryption % |
| **S3 - Malware Protection** | Protection | Coverage %, signature currency, scan compliance |
| **S4 - Software Controls** | Software Governance | Unauthorized software, app control %, patch compliance |
| **S5 - Privileged Utilities** | Access Control | Privileged access controls, usage monitoring |
| **S6 - Consolidated Assessment** | **Overall Compliance** | **Integrates all of the above into single view** |

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **CISO / Information Security Manager** - Overall accountability
2. **Security Engineering** - Data consolidation and analysis
3. **Compliance Officer** - Audit readiness verification
4. **IT Director** - Remediation commitment and resource allocation
5. **Executive Leadership** - Risk acceptance decisions

#### Time Commitment

- **Initial assessment:** 4-6 hours (data consolidation from S1-S5)
- **Quarterly updates:** 3-4 hours (refresh from updated S1-S5)
- **Annual audit prep:** 6-8 hours (comprehensive review with evidence)

### Expected Outputs

Upon completion, you will have:

1. ✅ Consolidated compliance dashboard
2. ✅ Overall compliance status per control (A.8.1, A.8.7, A.8.18, A.8.19)
3. ✅ Cross-control gap analysis
4. ✅ Risk-prioritized remediation roadmap
5. ✅ Executive summary and recommendations
6. ✅ Evidence package for audit
7. ✅ Approved assessment with management sign-off

---

## Prerequisites

### Information You'll Need

#### 1. Completed Assessments S1-S5

**CRITICAL:** S6 is a consolidation document. You **must** have completed:

- ✅ S1 - Endpoint Discovery Process
- ✅ S2 - Security Baseline Implementation
- ✅ S3 - Malware Protection Deployment
- ✅ S4 - Software Control Process
- ✅ S5 - Privileged Utility Management

**If any assessment is missing or outdated (>90 days), complete/update it first.**

#### 2. Access to Assessment Data

- S1 Dashboard metrics
- S2 Dashboard metrics
- S3 Dashboard metrics
- S4 Dashboard metrics
- S5 Dashboard metrics
- All gap registers (S1-S5 Sheet 6/7)
- All evidence registers (S1-S5 Sheet 7/8)

#### 3. Management Context

- Organizational risk appetite
- Budget constraints for remediation
- Timeline expectations
- Regulatory requirements
- Audit schedule

### Tools You'll Use

**Data Sources:**

- S1-S5 assessment workbooks
- ISMS policy documents
- Management dashboards

**Analysis Tools:**

- Excel (for consolidation)
- Risk assessment framework
- Gap analysis methodology

### Access Requirements

- Read access to all S1-S5 assessments
- Access to ISMS repository
- Access to management decision records
- Access to budget/resource planning documents

---

## Assessment Workflow

### High-Level Process

```
1. VERIFY S1-S5 COMPLETION (all current)
2. IMPORT DASHBOARD METRICS (from S1-S5)
3. CONSOLIDATE COMPLIANCE STATUS (Sheet 1)
4. CONSOLIDATE GAPS (Sheet 2)
5. ASSESS CROSS-CONTROL RISKS (Sheet 3)
6. PRIORITIZE REMEDIATION (Sheet 4)
7. REGISTER EVIDENCE (Sheet 5)
8. CREATE EXECUTIVE DASHBOARD (Sheet 6)
9. WRITE EXECUTIVE SUMMARY
10. REVIEW & APPROVE (CISO/Executive)
```

### Detailed Workflow

#### Phase 1: Verification (1 hour)

**Objective:** Ensure S1-S5 are complete and current

**Steps:**
1. Check S1-S5 completion status
2. Verify assessment dates (≤90 days for all)
3. Verify approval status (all approved)
4. If any missing/outdated: Stop, update those first

**Deliverable:** Confirmation that S1-S5 are complete and current

#### Phase 2: Data Import (1-2 hours)

**Objective:** Extract key metrics from S1-S5

**Steps:**
1. From S1 Dashboard: Endpoint counts, criticality distribution
2. From S2 Dashboard: Baseline compliance %, encryption %
3. From S3 Dashboard: Coverage %, signature currency, scan compliance
4. From S4 Dashboard: Unauthorized software, app control %, patch compliance
5. From S5 Dashboard: Privileged access controls, monitoring %

**Deliverable:** Sheet 1 populated with all metrics

#### Phase 3: Compliance Assessment (1 hour)

**Objective:** Calculate overall compliance per control

**Steps:**
1. For each control (A.8.1, A.8.7, A.8.18, A.8.19): Determine compliance status
2. Apply thresholds (Green/Yellow/Red)
3. Document compliance evidence
4. Identify compliance gaps

**Deliverable:** Sheet 1 with compliance status per control

#### Phase 4: Gap Consolidation (1-2 hours)

**Objective:** Consolidate all gaps from S1-S5

**Steps:**
1. Import gaps from S1 (inventory, management, baseline)
2. Import gaps from S2 (baseline, encryption)
3. Import gaps from S3 (coverage, signatures, scanning)
4. Import gaps from S4 (unauthorized software, app control, patches)
5. Import gaps from S5 (privileged access, monitoring, bypass tools)
6. Deduplicate (same gap may appear in multiple assessments)
7. Re-prioritize in consolidated view

**Deliverable:** Sheet 2 with master gap register

#### Phase 5: Cross-Control Risk Analysis (1 hour)

**Objective:** Identify risks from gap combinations

**Steps:**
1. Analyze gap intersections (e.g., unprotected + unpatched + unauthorized software = HIGH RISK)
2. Identify cumulative risks
3. Flag endpoints with multiple gaps
4. Assess overall risk profile

**Deliverable:** Sheet 3 with cross-control risk analysis

#### Phase 6: Remediation Roadmap (1-2 hours)

**Objective:** Develop prioritized remediation plan

**Steps:**
1. Group gaps by priority (P1/P2/P3/P4)
2. Sequence remediation (dependencies, quick wins)
3. Allocate to phases (Q1, Q2, Q3, Q4)
4. Assign ownership
5. Estimate resources
6. Get management commitment

**Deliverable:** Sheet 4 with remediation roadmap

#### Phase 7: Evidence Consolidation (30 minutes)

**Objective:** Aggregate evidence from S1-S5

**Steps:**
1. List all evidence from S1-S5
2. Organize by control
3. Verify audit readiness

**Deliverable:** Sheet 5 with evidence package

#### Phase 8: Executive Dashboard (1 hour)

**Objective:** Create executive-level summary

**Steps:**
1. Calculate overall endpoint security score
2. Summarize compliance status (4 controls)
3. Highlight critical gaps
4. Document recommended actions
5. Create visual dashboard

**Deliverable:** Sheet 6 with executive dashboard

#### Phase 9: Executive Summary (1 hour)

**Objective:** Write narrative summary

**Steps:**
1. Draft executive summary (1 page)
2. Document key findings
3. Recommend actions
4. Request decisions/approvals

**Deliverable:** Executive summary document

#### Phase 10: Review & Approval (2-3 hours)

**Steps:**
1. CISO review
2. Executive review (if required)
3. Approval and sign-off

**Deliverable:** Approved assessment

---

## Sheet-by-Sheet Completion Guide

### Sheet 1: Consolidated_Compliance

#### Purpose
Consolidate compliance metrics from S1-S5 into single view per control.

#### What to Document

**For EACH Control (A.8.1, A.8.7, A.8.18, A.8.19):**

- Key metrics from relevant assessments
- Compliance status (Green/Yellow/Red)
- Compliance percentage
- Critical gaps count
- Evidence references

#### How to Complete

**Step 1: Import S1 Metrics (A.8.1 - User Endpoint Devices)**

**From S1 Dashboard:**

- Total endpoints
- Endpoint classification distribution (corporate/BYOD/contractor)
- Criticality distribution (critical/high/medium/low)
- Management coverage % (MDM/agent enrollment)

**From S2 Dashboard (related to A.8.1):**

- Baseline compliance % by endpoint type
- Encryption coverage % (FDE, file-level)
- Secure disposal compliance %

**A.8.1 Compliance Calculation:**
```
A.8.1 Compliance = Weighted Average of:

  - Endpoint inventory completeness (10%)
  - Management coverage (20%)
  - Baseline compliance (40%)
  - Encryption coverage (30%)

Thresholds:
  Green: ≥95%
  Yellow: 85-94%
  Red: <85%
```

**Step 2: Import S3 Metrics (A.8.7 - Protection Against Malware)**

**From S3 Dashboard:**

- Overall malware protection coverage %
- Corporate coverage %, BYOD coverage %
- Signature currency %
- Scan compliance % (full scans, quick scans)
- Detection effectiveness metrics

**A.8.7 Compliance Calculation:**
```
A.8.7 Compliance = Weighted Average of:

  - Protection coverage (40%)
  - Signature currency (30%)
  - Scan compliance (20%)
  - Detection effectiveness (10%)

Thresholds:
  Green: ≥95% coverage, ≥95% signature currency, ≥90% scan compliance
  Yellow: ≥85% coverage, ≥85% signature, ≥75% scan
  Red: <85% coverage, <85% signature, <75% scan
```

**Step 3: Import S5 Metrics (A.8.18 - Use of Privileged Utility Programs)**

**From S5 Dashboard:**

- Total privileged utilities
- Access control deployment %
- Enforcement %
- Logging/monitoring %
- Approval workflow compliance %
- Security bypass tools (uncontrolled count)

**A.8.18 Compliance Calculation:**
```
A.8.18 Compliance = Composite of:

  - Access control deployed ≥95%
  - Enforcement mode ≥95%
  - Logging/monitoring ≥95%
  - Approval workflow 100%
  - Security bypass tools: 0 uncontrolled

Thresholds:
  Green: All criteria met
  Yellow: Access control ≥85%, enforcement ≥85%, logging ≥85%, approval ≥90%, bypass ≤2 controlled
  Red: Any below yellow threshold OR uncontrolled bypass tools
```

**Step 4: Import S4 Metrics (A.8.19 - Installation of Software)**

**From S4 Dashboard:**

- Approved software list exists (Yes/No)
- Unauthorized software count
- Unauthorized software % of total
- Application control deployment %
- Application control enforcement %
- Critical patch compliance %
- High patch compliance %

**A.8.19 Compliance Calculation:**
```
A.8.19 Compliance = Composite of:

  - Approved list exists and current
  - Unauthorized software ≤5%
  - Application control deployed ≥95%
  - Application control enforced ≥90%
  - Critical patch compliance ≥95%

Thresholds:
  Green: All criteria met
  Yellow: Approved list exists, unauthorized 5-10%, app control ≥85%, enforcement ≥75%, critical patches ≥85%
  Red: No approved list OR unauthorized >10% OR app control <85% OR critical patches <85%
```

**Step 5: Calculate Overall Endpoint Security Compliance**

**Overall Compliance:**
```
Overall = Weighted Average of 4 Controls:
  A.8.1: 20%
  A.8.7: 30%
  A.8.18: 20%
  A.8.19: 30%

Overall Status = Worst of (A.8.1, A.8.7, A.8.18, A.8.19)
(Conservative approach - one Red control = Overall Red)
```

**Step 6: Document Compliance Evidence**

**For Each Control:**

- Evidence references (which assessments, which sheets)
- Date of evidence
- Evidence completeness (%)

#### Common Mistakes to Avoid

❌ **Using outdated data** - S1-S5 must be current (≤90 days)  
❌ **Cherry-picking metrics** - Use all required metrics, not just good ones  
❌ **Ignoring failed controls** - One Red doesn't mean overall is Yellow  
❌ **No evidence references** - Must trace back to source assessments  
❌ **Calculation errors** - Verify all formulas  

#### Quality Checklist

- [ ] All S1-S5 data imported
- [ ] Metrics verified against source assessments
- [ ] Compliance calculations correct
- [ ] Thresholds applied consistently
- [ ] Overall status reflects worst control (conservative)
- [ ] Evidence references documented
- [ ] No data >90 days old

---

### Sheet 2: Consolidated_Gaps

#### Purpose
Master gap register consolidating all gaps from S1-S5.

#### What to Document

All gaps from:

- S1 Sheet 6 (Discovery & Inventory gaps)
- S2 Sheet 6 (Baseline & Encryption gaps)
- S3 Sheet 6 (Protection Coverage gaps)
- S4 Sheet 7 (Software Control gaps)
- S5 Sheet 7 (Privileged Utility gaps)

Plus:

- Deduplication (same gap in multiple assessments)
- Re-prioritization in consolidated view
- Cross-control dependencies

#### How to Complete

**Step 1: Import All Gaps**

**From Each Assessment (S1-S5):**

- Gap ID
- Gap description
- Source assessment
- Risk level
- Remediation plan
- Owner
- Target date
- Status

**Step 2: Deduplicate Gaps**

**Common Duplicates:**

- Unmanaged endpoints (appears in S1, S2, S3)
- Missing encryption (appears in S2, but impacts S1 compliance)
- Application control gaps (appears in S4, S5)

**Deduplication Strategy:**

- Keep one entry per unique gap
- Reference all assessments where gap appears
- Use highest risk level if different across assessments

**Step 3: Re-Prioritize in Consolidated View**

**Priority Criteria (Consolidated):**

**P1 - Critical (Immediate, ≤30 days):**

- Uncontrolled security bypass tools
- Unprotected critical endpoints (no malware protection)
- Critical vulnerabilities >30 days overdue
- No application control on production endpoints
- Major compliance failures (audit blockers)

**P2 - High (≤90 days):**

- Yellow status controls (need to reach Green)
- High-risk gaps with workarounds
- Unauthorized software on critical endpoints
- Missing encryption on high-criticality endpoints

**P3 - Medium (≤180 days):**

- Process improvements (approval workflows, recertification)
- Medium-risk technical gaps
- Documentation updates

**P4 - Low (Backlog):**

- Nice-to-have improvements
- Low-risk gaps with strong compensating controls

**Step 4: Identify Cross-Control Dependencies**

**Example Dependencies:**

- Can't enforce application control (S4) until endpoints managed (S1)
- Can't monitor privileged utilities (S5) until logging centralized
- Baseline compliance (S2) depends on endpoint management (S1)

**Document:**

- Gap ID
- Depends on (other Gap IDs)
- Blocks (other Gap IDs)

**Step 5: Calculate Gap Metrics**

```
Total Gaps: [Count]

By Priority:
  P1 (Critical): [Count] ([%])
  P2 (High): [Count] ([%])
  P3 (Medium): [Count] ([%])
  P4 (Low): [Count] ([%])

By Source:
  S1 (Discovery): [Count]
  S2 (Baselines): [Count]
  S3 (Malware): [Count]
  S4 (Software): [Count]
  S5 (Privileged): [Count]

By Status:
  Open: [Count]
  In Progress: [Count]
  Blocked: [Count]
  Resolved: [Count]

Resolution Rate: [Resolved / Total × 100] %
```

#### Common Mistakes to Avoid

❌ **Not deduplicating** - Same gap counted 3 times  
❌ **Losing priority** - P1 in S3, becomes P3 in consolidated view  
❌ **Ignoring dependencies** - Starting S4 before S1 complete  
❌ **No cross-control view** - Treating gaps in isolation  

#### Quality Checklist

- [ ] All gaps from S1-S5 imported
- [ ] Duplicates identified and merged
- [ ] Priority re-assessed in consolidated context
- [ ] Dependencies documented
- [ ] Cross-control impacts analyzed
- [ ] Gap metrics calculated
- [ ] No gaps lost in consolidation

---

### Sheet 3: Cross_Control_Risk

#### Purpose
Identify amplified risks from gap combinations across multiple controls.

#### What to Document

**Risk Scenarios from Gap Combinations:**

- Unprotected + Unpatched + Unauthorized Software
- No Application Control + Privileged Access Uncontrolled
- Unmanaged + Unencrypted + Unprotected
- Missing Baseline + No Monitoring + No Software Controls

#### How to Complete

**Step 1: Identify High-Risk Endpoint Cohorts**

**Query Pattern:**
```
Endpoints WHERE:

  - A.8.7 Coverage = Unprotected AND
  - A.8.19 Patch Status = Critical Vulnerabilities AND
  - A.8.19 Unauthorized Software > 0

Result: Endpoints with TRIPLE RISK (no protection, vulnerable, unauthorized software)
```

**Common High-Risk Cohorts:**

**Cohort 1: Unmanaged + Unprotected**

- Not enrolled in MDM/endpoint management (S1)
- No malware protection (S3)
- Risk: Cannot deploy security controls, vulnerable to malware

**Cohort 2: Unencrypted + Unprotected + Mobile**

- Laptops without encryption (S2)
- No malware protection (S3)
- Mobile/remote workers
- Risk: Data loss if device lost/stolen + malware infection

**Cohort 3: Critical Endpoints + Multiple Gaps**

- Criticality = Critical (S1)
- Missing any protection (S3) OR missing app control (S4) OR privileged utilities uncontrolled (S5)
- Risk: High-value target with weak defenses

**Cohort 4: No Application Control + Privileged Access**

- Application control not deployed (S4)
- Users with privileged utility access (S5)
- Risk: Privileged users can install anything, including malicious tools

**Cohort 5: Stale Signatures + No Patching + Unauthorized Software**

- Anti-malware signatures >7 days (S3)
- Critical vulnerabilities unpatched >30 days (S4)
- Unauthorized software detected (S4)
- Risk: Outdated defenses + vulnerable software + potentially malicious software

**Step 2: Assess Cumulative Risk**

**For Each Cohort:**

- Endpoint count
- Business impact (what if all compromised)
- Attack likelihood
- Cumulative risk score

**Risk Scoring:**
```
Cumulative Risk = (Impact × Likelihood) + Gap Multiplier

Gap Multiplier:

  1 gap: ×1.0
  2 gaps: ×1.5
  3 gaps: ×2.0

  4+ gaps: ×3.0

Result:
  Critical: ≥20
  High: 15-19
  Medium: 10-14
  Low: <10
```

**Step 3: Document Cross-Control Scenarios**

**For Each Scenario:**

- Scenario ID
- Description (gap combination)
- Affected endpoints (count and list)
- Cumulative risk score
- Attack vectors enabled
- Business impact
- Recommended mitigation
- Owner
- Target date

**Step 4: Prioritize Remediation**

**Prioritization:**

- Start with scenarios affecting Critical endpoints
- Address scenarios with highest cumulative risk
- Quick wins (scenarios fixable with single remediation)

#### Common Mistakes to Avoid

❌ **Treating gaps independently** - Missing cumulative risk  
❌ **No endpoint-level analysis** - Not identifying which specific endpoints have multiple gaps  
❌ **Ignoring likelihood** - High impact but very unlikely scenarios over-prioritized  
❌ **No business context** - Technical risk without business impact assessment  

#### Quality Checklist

- [ ] High-risk cohorts identified
- [ ] Endpoint-level gap combinations analyzed
- [ ] Cumulative risk scored
- [ ] Business impact documented
- [ ] Attack scenarios described
- [ ] Mitigation strategies defined
- [ ] Prioritization based on risk + feasibility

---

### Sheet 4: Remediation_Roadmap

#### Purpose
Consolidated, sequenced remediation plan with phases, owners, resources.

#### What to Document

**Remediation organized by:**

- Priority (P1/P2/P3/P4)
- Phase (Q1/Q2/Q3/Q4 or Timeline)
- Control area (A.8.1/A.8.7/A.8.18/A.8.19)
- Dependencies
- Resource requirements
- Management commitments

#### How to Complete

**Step 1: Group Gaps by Remediation Project**

**Instead of 147 individual gaps, create remediation PROJECTS:**

**Project 1: Endpoint Management Enrollment**

- Addresses: S1 gaps (unmanaged endpoints)
- Enables: S2 (baseline deployment), S3 (protection deployment), S4 (app control)
- Priority: P1
- Timeline: Q1

**Project 2: Malware Protection Deployment**

- Addresses: S3 gaps (protection coverage)
- Dependencies: Project 1 (endpoints must be managed)
- Priority: P1
- Timeline: Q1-Q2

**Project 3: Application Control Rollout**

- Addresses: S4 gaps (application control)
- Dependencies: Project 1
- Priority: P2
- Timeline: Q2-Q3

**Project 4: Privileged Access Management (PAM)**

- Addresses: S5 gaps (privileged utility controls)
- Priority: P2
- Timeline: Q2-Q3

**Project 5: Encryption Deployment**

- Addresses: S2 gaps (encryption)
- Priority: P2
- Timeline: Q2-Q3

**Project 6: Patch Management Improvements**

- Addresses: S4 gaps (patch compliance)
- Priority: P2
- Timeline: Ongoing (process improvement)

**Project 7: Process & Documentation**

- Addresses: Approval workflows, recertification, documentation
- Priority: P3
- Timeline: Q3-Q4

**Step 2: Sequence Projects**

**Sequencing Considerations:**

- Dependencies (must complete A before starting B)
- Quick wins (high impact, low effort - do early)
- Resource constraints (can't do everything at once)
- Business cycles (avoid during busy seasons)

**Example Sequence:**
```
Q1 (Immediate):

  - Project 1: Endpoint Management (foundation)
  - Project 2: Malware Protection (start after Project 1 phase 1)

Q2 (Short-term):

  - Project 2: Malware Protection (complete)
  - Project 3: Application Control (pilot)
  - Project 4: PAM (design)
  - Project 5: Encryption (pilot)

Q3 (Medium-term):

  - Project 3: Application Control (rollout)
  - Project 4: PAM (deploy)
  - Project 5: Encryption (rollout)
  - Project 6: Patch Management (improve process)

Q4 (Long-term):

  - Project 7: Process improvements
  - Project 3/4/5: Complete and optimize

```

**Step 3: Assign Ownership & Resources**

**For Each Project:**

- **Owner:** IT Operations Manager, Security Engineering Lead, etc.
- **Team:** Who works on it (FTEs, contractors)
- **Budget:** Licensing, consulting, hardware, training
- **Timeline:** Start date, milestones, completion date
- **Success Metrics:** How to measure success

**Example:**
```
Project 2: Malware Protection Deployment
Owner: Security Engineering Manager
Team: 2 security engineers, 1 endpoint engineer, help desk support
Budget: $150K (EDR licensing 500 endpoints × $50/yr × 3 years)
Timeline: 

  - Q1 W1-2: Pilot (50 endpoints)
  - Q1 W3-8: Rollout phase 1 (250 endpoints)
  - Q2 W1-8: Rollout phase 2 (200 endpoints)
  - Q2 W9: Complete

Success Metrics: 

  - Coverage ≥98%
  - Signature currency ≥95%
  - User satisfaction ≥4/5

```

**Step 4: Get Management Commitment**

**For Budget/Resources:**

- Total budget required across all projects
- Resource allocation (people, time)
- Expected ROI or risk reduction
- Management approval

**For Timeline:**

- Realistic given resources
- Accounts for other initiatives
- Includes contingency (10-20%)
- Management sign-off

**Step 5: Define Milestones & Tracking**

**Milestone Examples:**

- Project 1: 100 endpoints enrolled in MDM (Q1 W4)
- Project 2: EDR deployed to 50% of endpoints (Q1 end)
- Project 3: Application control enforced on pilot group (Q2 W6)

**Tracking:**

- Monthly status updates
- Risk/issue escalation
- Budget tracking
- Milestone completion

#### Common Mistakes to Avoid

❌ **147 individual remediation plans** - Need projects, not line items  
❌ **No dependencies** - Starting projects that require others first  
❌ **Unrealistic timelines** - Aggressive schedules with no contingency  
❌ **No resources allocated** - Plan without budget/people  
❌ **No management buy-in** - Plan without executive commitment  
❌ **No tracking** - Plan without progress monitoring  

#### Quality Checklist

- [ ] Gaps grouped into remediation projects
- [ ] Projects sequenced logically (dependencies)
- [ ] Ownership assigned (named individuals)
- [ ] Resources estimated (budget, people, time)
- [ ] Timeline realistic (accounts for constraints)
- [ ] Milestones defined (measurable progress)
- [ ] Management commitment obtained
- [ ] Tracking mechanism established

---

### Sheet 5: Evidence_Package

#### Purpose
Consolidated evidence from S1-S5 organized for audit.

#### What to Document

All evidence from S1-S5 Evidence Registers, organized by control (A.8.1, A.8.7, A.8.18, A.8.19).

#### How to Complete

**Step 1: Import Evidence from S1-S5**

**From Each Assessment:**

- Evidence ID
- Evidence type
- Description
- Source assessment
- Storage location
- Collection date
- Verification status

**Step 2: Organize by Control**

**A.8.1 Evidence:**

- From S1 (endpoint inventory, management coverage)
- From S2 (baseline configs, encryption evidence)

**A.8.7 Evidence:**

- From S3 (protection coverage reports, signature status, scan compliance)

**A.8.18 Evidence:**

- From S5 (privileged utility inventory, access controls, usage logs, approval records)

**A.8.19 Evidence:**

- From S4 (approved software list, unauthorized software reports, app control configs, patch compliance)

**Step 3: Verify Audit Readiness**

**For Each Evidence Item:**

- Recent (≤90 days for operational data, ≤1 year for policies)
- Complete (not redacted beyond sanitization)
- Accessible (auditor can retrieve)
- Verified (spot-checked for accuracy)

**Step 4: Create Evidence Index**

**Evidence Index:**

- Control → Requirement → Evidence Item(s) → Storage Location

**Example:**
```
A.8.7 - Protection Against Malware
  → Requirement: ≥98% corporate endpoint coverage
    → Evidence: S3-EVD-012 (EDR coverage report, 2026-01-15)
    → Location: SharePoint/ISMS/Evidence/S3/
```

#### Quality Checklist

- [ ] All evidence from S1-S5 included
- [ ] Organized by control
- [ ] Audit readiness verified
- [ ] Evidence index created
- [ ] Storage locations documented
- [ ] No missing evidence

---

### Sheet 6: Executive_Dashboard

#### Purpose
One-page executive summary with overall status, metrics, critical gaps, and recommendations.

#### What to Document

- Overall endpoint security status (Green/Yellow/Red)
- Compliance status per control (A.8.1, A.8.7, A.8.18, A.8.19)
- Key metrics summary
- Top 10 critical gaps
- Recommended actions (immediate, short-term, long-term)
- Management decisions required

#### How to Complete

**Step 1: Overall Status**

```
┌─────────────────────────────────────────────────┐
│  ENDPOINT SECURITY COMPLIANCE DASHBOARD         │
│  ISO/IEC 27001:2022 Controls A.8.1/8.7/8.18/8.19│
├─────────────────────────────────────────────────┤
│                                                  │
│  OVERALL STATUS:  [🟢 GREEN / 🟡 YELLOW / 🔴 RED] │
│                                                  │
│  A.8.1 - User Endpoint Devices:      [🟢/🟡/🔴]  │
│  A.8.7 - Protection Against Malware: [🟢/🟡/🔴]  │
│  A.8.18 - Privileged Utilities:      [🟢/🟡/🔴]  │
│  A.8.19 - Software Installation:     [🟢/🟡/🔴]  │
│                                                  │
└─────────────────────────────────────────────────┘
```

**Step 2: Key Metrics Summary**

- Total endpoints: [X]
- Critical endpoints: [X]
- Malware protection coverage: [XX%]
- Application control deployment: [XX%]
- Critical vulnerabilities overdue: [X]
- Uncontrolled security bypass tools: [X]
- P1 gaps: [X]

**Step 3: Top 10 Critical Gaps**

From Sheet 2 (Consolidated Gaps), list top 10 P1/P2 gaps with:

- Gap description
- Risk level
- Owner
- Target date

**Step 4: Executive Summary (Narrative)**

**Template:**
```
[Organization]'s endpoint security posture is [GREEN/YELLOW/RED] as of [Date].

Controls Status:

- A.8.1 (Endpoint Devices): [Status] - [brief summary]
- A.8.7 (Malware Protection): [Status] - [brief summary]
- A.8.18 (Privileged Utilities): [Status] - [brief summary]
- A.8.19 (Software Controls): [Status] - [brief summary]

Critical Issues:
1. [Top issue]
2. [Second issue]
3. [Third issue]

Remediation Plan:
[X] projects planned over [timeline] requiring $[budget] and [FTEs].
Q1 focus: [priorities]
Expected outcome: [Green status by Q3 2026]

Management Actions Required:
1. [Decision needed]
2. [Approval needed]
3. [Resource allocation needed]
```

**Step 5: Recommended Actions**

**IMMEDIATE (7-30 days):**
1. [Action]
2. [Action]
3. [Action]

**SHORT-TERM (90 days):**
1. [Action]
2. [Action]
3. [Action]

**LONG-TERM (180 days):**
1. [Action]
2. [Action]
3. [Action]

#### Quality Checklist

- [ ] Overall status reflects worst control (conservative)
- [ ] All 4 controls represented
- [ ] Key metrics accurate
- [ ] Top gaps prioritized correctly
- [ ] Executive summary concise (1 page)
- [ ] Recommended actions specific and actionable
- [ ] Management decisions clearly stated

---

### Sheet 7: Risk_Prioritization

#### Purpose
Prioritize identified gaps and risks across all endpoint security controls (S1-S5).

#### What to Document

**Risk Ranking:**

- Gap ID
- Control area (S1/S2/S3/S4/S5)
- Risk description
- Risk severity (Critical/High/Medium/Low)
- Business impact
- Affected endpoints
- Exploitability
- Priority score

**Prioritization Rationale:**

- Risk factors considered
- Weighting methodology
- Tie-breaker criteria
- Alignment with organizational risk tolerance

#### How to Complete

**Step 1: Consolidate All Gaps**

From S1-S5:

- S1 gaps: [list with risk]
- S3 gaps: [list with risk]
- S4 gaps: [list with risk]
- S5 gaps: [list with risk]
- Total gap count: [count]

**Step 2: Define Risk Criteria**

**Critical:**

- Security bypass possible
- Widespread vulnerability exploitation risk
- Affects >25% of endpoints
- Known active exploits

**High:**

- Significant control weakness
- Affects 10-25% of endpoints
- Potential for exploitation
- Compensating controls insufficient

**Medium:**

- Control gap with limited impact
- Affects 5-10% of endpoints
- Exploitation requires specific conditions
- Workarounds available

**Low:**

- Minor gap or configuration issue
- Affects <5% of endpoints
- Difficult to exploit
- Minimal business impact

**Step 3: Calculate Priority Scores**

```
Priority Score = (Severity × 5) + (Impact × 3) + (Exploitability × 2)

Severity: Critical=5, High=4, Medium=3, Low=2, Informational=1
Impact: High=5, Medium=3, Low=1
Exploitability: High=5, Medium=3, Low=1

Sort by Score (descending)
```

**Step 4: Create Risk Heat Map**

- X-axis: Likelihood (Low/Medium/High)
- Y-axis: Impact (Low/Medium/High)
- Plot each gap by position
- Identify critical quadrant gaps

**Step 5: Map to Remediation Timeline**

- Tier 1 (Critical): Immediate (7 days)
- Tier 2 (High): 30 days
- Tier 3 (Medium): 90 days
- Tier 4 (Low): 180 days

#### Common Mistakes to Avoid

❌ Treating all gaps equally
❌ No documented prioritization criteria
❌ Risk criteria too vague
❌ No business impact assessment
❌ Prioritization not aligned with risk appetite

#### Quality Checklist

- [ ] All gaps included
- [ ] Risk criteria clearly defined
- [ ] Severity assigned to all gaps
- [ ] Business impact documented
- [ ] Priority scores calculated
- [ ] Heat map visualized
- [ ] Management alignment obtained

---

### Sheet 8: Remediation_Tracking

#### Purpose
Track remediation progress across all identified gaps and maintain accountability.

#### What to Document

**Remediation Status:**

- Gap ID and description
- Priority tier
- Owner/responsible party
- Target completion date
- Current status (Not Started/In Progress/Blocked/Completed)
- % Complete
- Actual completion date

**Progress Metrics:**

- Total gaps: [count]
- On schedule: [count] ([%])
- At risk: [count] ([%])
- Blocked: [count] ([%])
- Completed: [count] ([%])

**Issue Tracking:**

- Blockers
- Resource constraints
- Escalations needed
- Change requests

#### How to Complete

**Step 1: Create Remediation Plan**

For each gap:

- Remediation action: [specific task]
- Owner: [team/person]
- Target date: [date]
- Resource needs: [budget/staff/tools]
- Success criteria: [measurable outcome]
- Dependencies: [other gaps/projects]

**Step 2: Baseline Planning**

- Tier 1 (Critical) target: [date - 7 days from approval]
- Tier 2 (High) target: [date - 30 days]
- Tier 3 (Medium) target: [date - 90 days]
- Tier 4 (Low) target: [date - 180 days]

**Step 3: Track Progress**

Weekly updates:

- Status: Not Started/In Progress/Blocked/Completed
- % Complete: [0-100%]
- Next steps: [by date]
- Blockers/issues: [if any]
- Updated completion date: [if changed]

**Step 4: Escalate Blockers**

If blocked or off-track:

- Issue description: [what's blocking]
- Impact: Delay of [X days]
- Escalation: [name/date]
- Resolution required: [what's needed]

**Step 5: Track Completion**

When remediation complete:

- Actual completion date: [date]
- Verification method: [how verified]
- Verification date: [date]
- Verification evidence: [document/screenshot]
- Sign-off: [owner/manager]

#### Common Mistakes to Avoid

❌ Plans created but never tracked
❌ Status not updated regularly
❌ Blockers escalated too late
❌ No accountability assigned
❌ No evidence of completion

#### Quality Checklist

- [ ] All gaps have remediation plans
- [ ] Owners assigned
- [ ] Target dates realistic
- [ ] Status updated weekly
- [ ] Blockers tracked and escalated
- [ ] Completion verified
- [ ] Overall progress measured

---

### Sheet 9: Trend_Analysis

#### Purpose
Track key metrics trends over time to measure improvement and identify emerging patterns.

#### What to Document

**Trend Metrics:**

- Metric name
- Measurement period (monthly/quarterly)
- Current value
- Previous value
- Change (absolute and %)
- Trend direction (improving/stable/declining)
- Threshold/target
- Status vs. target

**Key Trend Lines:**

- Overall compliance status
- Gap closure rate
- Endpoint protection coverage
- Vulnerability remediation time
- Incident rate

**Seasonal/Cyclical Patterns:**

- Peak risk periods
- Resource availability patterns
- Patch deployment cycles

#### How to Complete

**Step 1: Define Key Metrics**

**Control S1 - Endpoint Discovery:**

- Endpoint inventory accuracy: [%]
- Inventory update frequency: [days]
- Inventory completeness: [%]

**Control S3 - Malware Protection:**

- Protection coverage: [%]
- Signature currency: [%]
- Scan compliance: [%]
- Detection rate: [per 1000 endpoints]

**Control S4 - Software Control:**

- Approved software list: [count items]
- Unauthorized software rate: [per 1000 endpoints]
- Patch compliance: [%]

**Control S5 - Privileged Utility:**

- Controlled utilities: [count]
- Access certification currency: [% current]
- Unauthorized access attempts: [per month]

**Control S6 - Overall:**

- Compliance status: [%]
- Gap closure rate: [gaps/month]
- Remediation average time: [days]

**Step 2: Collect Historical Data**

- Period 1 (baseline): [date] - [values]
- Period 2: [date] - [values]
- Period 3: [date] - [values]
- Current: [date] - [values]

**Step 3: Calculate Trends**

For each metric:

- Change from previous: [+/-X%]
- Change from baseline: [+/-X%]
- Trend: Improving/Stable/Declining
- Trend rate: [X% per period]

**Step 4: Create Visualizations**

- Line graph: Metric over time
- Identify inflection points
- Mark major events (deployments, incidents)
- Forecast based on trend

**Step 5: Analyze Patterns**

- Improvement drivers: [what caused positive trend]
- Risk factors: [what caused negative trend]
- Seasonal patterns: [if any]
- Emerging issues: [early warning signs]

#### Common Mistakes to Avoid

❌ Insufficient historical data
❌ Inconsistent measurement methodology
❌ No context for metric changes
❌ Seasonal variation not considered
❌ Trends not linked to actions

#### Quality Checklist

- [ ] Key metrics identified
- [ ] Historical data available (3+ periods)
- [ ] Measurement methodology consistent
- [ ] Current values accurate
- [ ] Trends calculated correctly
- [ ] Visualizations clear
- [ ] Pattern analysis complete

---

### Sheet 10: Evidence_Register

#### Purpose
Centralized registry of all evidence collected across S1-S6 assessments for audit traceability.

#### What to Document

**Evidence Inventory:**

- Evidence ID
- Evidence type
- Control reference (S1-S6)
- Description
- Source system/document
- Collection date
- Collector
- Location (storage path)
- Verification date
- Verification status (Verified/Unverified)
- Expires/Refresh date

**Evidence Status:**

- Total evidence items: [count]
- Verified: [count] ([%])
- Current (within 30 days): [count] ([%])
- Expiring soon (30-60 days): [count]
- Expired: [count]

#### How to Complete

**Step 1: Consolidate Evidence**

From S1-S5 evidence registers and this assessment:

- S1 evidence: [count] items
- S3 evidence: [count] items
- S4 evidence: [count] items
- S5 evidence: [count] items
- S6 evidence: [count] items
- Total: [count] items

**Step 2: Register Each Item**

For every piece of evidence:

- Evidence type: [Screenshot/Report/Log/Configuration/Documentation]
- Control: [S1/S3/S4/S5/S6]
- Description: [What does it prove]
- Location: [File path/URL/System]
- Collection date: [date]
- Collector: [name/team]
- Sanitization: [Redacted items (if any)]

**Step 3: Verify Evidence**

- Evidence still exists: Yes/No
- Evidence current: Yes/No (if >30 days, refresh needed)
- Evidence accessible: Yes/No
- Evidence complete: Yes/No

**Step 4: Set Refresh Schedule**

- Operational data (logs, reports): Refresh every 30 days
- Configuration data: Refresh every 90 days
- Documentation: Refresh when changed
- Screenshots: Refresh every 60 days

**Step 5: Organize Evidence**

```
Evidence Storage Structure:

/Audit Evidence/
├── S1 - Endpoint Discovery/
│   ├── Inventory Exports/
│   ├── Scan Reports/
│   └── Asset Count/
├── S3 - Malware Protection/
│   ├── Coverage Reports/
│   ├── Scan History/
│   └── Detection Logs/
├── S4 - Software Control/
│   ├── Approved List/
│   ├── Patch Reports/
│   └── Scan Results/
├── S5 - Privileged Utility/
│   ├── Policies/
│   ├── Access Reviews/
│   └── Usage Logs/
└── S6 - Assessment/
    ├── Consolidated Findings/
    ├── Remediation Plans/
    └── Management Approvals/
```

**Step 6: Document Sanitization**

Evidence sanitization tracking:

- Original location: [path]
- Redacted items: [IPs, usernames, secrets]
- Retained items: [timestamps, versions, metrics]
- Sanitized location: [path]
- Sanitization date: [date]

#### Common Mistakes to Avoid

❌ Evidence scattered across systems
❌ Collection dates unknown
❌ Outdated evidence used
❌ Evidence not sanitized
❌ No traceability chain
❌ Evidence expiration not tracked

#### Quality Checklist

- [ ] All evidence consolidated
- [ ] Evidence locations documented
- [ ] Collection dates recorded
- [ ] Verification status tracked
- [ ] Refresh schedule defined
- [ ] Evidence properly organized
- [ ] Sanitization documented
- [ ] Traceability verified

---

## Evidence Collection

### Required Evidence Types

**Consolidated Evidence:**

- All evidence from S1-S5 (organized by control)
- This assessment (S6) itself
- Management approval records
- Remediation project plans
- Budget approvals

---

## Common Pitfalls

### Pitfall 1: Outdated Source Data

**Mistake:** Using S3 from 6 months ago

**Why It Fails:** Compliance status may have changed, data not current

**How to Avoid:** Verify all S1-S5 ≤90 days, refresh if needed

### Pitfall 2: Cherry-Picking Metrics

**Mistake:** Showing only good metrics, hiding bad ones

**Why It Fails:** Audit will find gaps, credibility lost

**How to Avoid:** Report all required metrics, honest assessment

### Pitfall 3: Overly Optimistic Status

**Mistake:** Calling overall status Green when A.8.7 is Red

**Why It Fails:** Auditor will fail the control, overall must be honest

**How to Avoid:** Overall = worst control (conservative approach)

### Pitfall 4: No Remediation Plan

**Mistake:** Identifying gaps but no plan to fix

**Why It Fails:** Audit requires corrective action plans

**How to Avoid:** Sheet 4 remediation roadmap is mandatory

### Pitfall 5: Unrealistic Remediation Timelines

**Mistake:** "Fix all 87 gaps in 30 days"

**Why It Fails:** Not achievable, plan will fail

**How to Avoid:** Realistic timelines with management commitment

### Pitfall 6: No Management Buy-In

**Mistake:** Creating plan without budget/resource approval

**Why It Fails:** Plan won't execute, gaps remain

**How to Avoid:** Get management sign-off on remediation roadmap

### Pitfall 7: Losing Gap Details

**Mistake:** Consolidating gaps loses specificity

**Why It Fails:** Can't remediate generic gap

**How to Avoid:** Maintain traceability to source assessments

### Pitfall 8: Ignoring Cross-Control Risks

**Mistake:** Treating controls independently

**Why It Fails:** Missing amplified risks from gap combinations

**How to Avoid:** Sheet 3 cross-control risk analysis

### Pitfall 9: No Executive Summary

**Mistake:** Handing executives a 50-sheet workbook

**Why It Fails:** Executives won't read it, won't approve

**How to Avoid:** Sheet 6 one-page dashboard + executive summary

### Pitfall 10: Static Assessment

**Mistake:** Complete S6 once, never update

**Why It Fails:** Compliance changes, gaps remediated, new gaps emerge

**How to Avoid:** Quarterly updates, tied to S1-S5 refresh cycle

---

## Quality Checklist

### Completeness (10 items)

- [ ] All 6 sheets completed
- [ ] All S1-S5 data imported
- [ ] All 4 controls assessed
- [ ] All gaps consolidated
- [ ] Cross-control risks analyzed
- [ ] Remediation roadmap developed
- [ ] Evidence package complete
- [ ] Executive dashboard created
- [ ] Executive summary written
- [ ] Management approval obtained

### Accuracy (10 items)

- [ ] S1-S5 data current (≤90 days)
- [ ] Compliance calculations correct
- [ ] Thresholds applied consistently
- [ ] Gap counts accurate
- [ ] Risk scores justified
- [ ] Metrics verified against sources
- [ ] No calculation errors
- [ ] Evidence references accurate
- [ ] Timeline realistic
- [ ] Budget estimates reasonable

### Honesty (8 items)

- [ ] Overall status reflects worst control
- [ ] No cherry-picking metrics
- [ ] Gaps not hidden
- [ ] Red controls not called Yellow
- [ ] Remediation challenges acknowledged
- [ ] Resource constraints documented
- [ ] Limitations stated clearly
- [ ] Management decisions required identified

### Evidence (5 items)

- [ ] All S1-S5 evidence consolidated
- [ ] Evidence organized by control
- [ ] Evidence audit-ready
- [ ] Evidence index created
- [ ] Storage locations accessible

### Remediation (8 items)

- [ ] All gaps have remediation plans
- [ ] Plans grouped into projects
- [ ] Projects sequenced (dependencies)
- [ ] Ownership assigned
- [ ] Resources estimated
- [ ] Timeline realistic
- [ ] Milestones defined
- [ ] Management committed

### Executive Communication (6 items)

- [ ] Executive dashboard one-page
- [ ] Executive summary concise (≤2 pages)
- [ ] Status clear (Green/Yellow/Red)
- [ ] Top gaps highlighted
- [ ] Recommended actions specific
- [ ] Decisions required stated

### Integration (5 items)

- [ ] All 4 controls integrated
- [ ] Cross-control risks identified
- [ ] Dependencies documented
- [ ] No contradictions between sources
- [ ] Holistic view achieved

### Auditability (5 items)

- [ ] Traceability to source assessments
- [ ] Evidence complete and organized
- [ ] Compliance claims supported
- [ ] Gap remediation tracked
- [ ] Approval records documented

---

## Review & Approval

### Two-Level Approval Process

#### Level 1: CISO Review

**Reviewer:** CISO or Information Security Manager

**Focus:**

- Compliance status accurate
- Risk assessment appropriate
- Remediation plan feasible
- Evidence package complete

**Checklist:**

- [ ] All 4 controls assessed
- [ ] Overall status justified
- [ ] Critical gaps identified
- [ ] Remediation roadmap realistic
- [ ] Budget requirements documented
- [ ] Evidence audit-ready

**Outcome:**

- Approve → Level 2
- Request Changes → Return

#### Level 2: Executive Approval

**Reviewer:** CIO, IT Director, or Executive Committee

**Focus:**

- Strategic alignment
- Resource commitment
- Risk acceptance
- Compliance timeline

**Checklist:**

- [ ] Remediation plan approved
- [ ] Budget allocated
- [ ] Resources committed
- [ ] Timeline acceptable
- [ ] Risk acceptance decisions documented
- [ ] Audit readiness confirmed

**Outcome:**

- Approve → Assessment Complete
- Request Changes → Return
- Escalate → Board/CEO (if major issues)

### Post-Approval Actions

1. Lock assessment (read-only)
2. Store in ISMS repository
3. Notify internal audit
4. Notify external auditors (if scheduled)
5. Begin remediation execution
6. Schedule quarterly reassessment

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
