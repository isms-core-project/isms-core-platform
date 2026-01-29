# ISMS-IMP-A.8.13-14-5.30-S1: BIA and RPO/RTO Process

**Document Classification:** Internal - ISMS Implementation Guide  
**Version:** 1.0  
**Target Audience:** BC/DR Coordinator, Business Process Owners, IT Management  
**Prerequisites:** Policy S4 (A.5.30) approved, stakeholder list prepared  
**Estimated Effort:** 3-6 weeks (depending on organization size)

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | BC/DR Coordinator | Initial BIA and RPO/RTO process implementation guide |

---

## Table of Contents

1. [Overview](#1-overview)
2. [BIA Preparation and Planning](#2-bia-preparation-and-planning)
3. [Stakeholder Engagement](#3-stakeholder-engagement)
4. [Impact Assessment Process](#4-impact-assessment-process)
5. [MTPD Determination](#5-mtpd-determination)
6. [RPO and RTO Calculation](#6-rpo-and-rto-calculation)
7. [Dependency Mapping](#7-dependency-mapping)
8. [BIA Documentation and Approval](#8-bia-documentation-and-approval)
9. [BIA Review and Update Process](#9-bia-review-and-update-process)
10. [Common Pitfalls and How to Avoid](#10-common-pitfalls-and-how-to-avoid)
11. [Verification and Sign-Off](#11-verification-and-sign-off)

---

## 1. Overview

### 1.1 Purpose

This implementation guide provides step-by-step instructions for conducting a Business Impact Analysis (BIA) and determining Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO) for ICT systems.

**Critical Principle:** RPO and RTO must be **business-driven, not IT-driven**. The business determines acceptable data loss and downtime based on impact, not IT based on technical capability.

### 1.2 Relationship to Policy

This guide implements:
- **Policy S4 (A.5.30)** Section 2: Business Impact Analysis Requirements
- **Annex-B** Section 2: RPO/RTO Classification Matrix
- **Annex-B** Section 3: BIA Detailed Worksheet Template

### 1.3 Expected Outcomes

Upon completion of this BIA process, [Organization] will have:
- Documented impact assessment for all critical ICT systems
- Defined RPO and RTO requirements for each system
- Criticality tier classification (Tier 1-4)
- System dependency map
- Approved BIA documentation
- Recovery priority sequence

---

## 2. BIA Preparation and Planning

### 2.1 Establish BIA Project Team

**Step 1: Assign BIA Project Lead**

The BIA Project Lead is typically the BC/DR Coordinator. Responsibilities:
- Coordinate all BIA activities
- Schedule interviews and workshops
- Collect and consolidate BIA data
- Prepare BIA documentation
- Present findings to executive management

**Step 2: Assemble BIA Team**

Include representatives from:
- IT (system owners, infrastructure team)
- Business units (process owners from each critical function)
- Finance (cost impact assessment)
- Legal/Compliance (regulatory requirements)
- Risk management

**Team Size:** Typically 5-8 people for core team, with additional subject matter experts as needed.

### 2.2 Define BIA Scope

**Step 3: Identify Systems in Scope**

BIA scope should include:
- All production ICT systems
- Systems supporting critical business processes
- Infrastructure systems (network, storage, identity management)
- Third-party/cloud services critical to operations

**Out of Scope:**
- Test/development systems (unless they support production)
- Archived/decommissioned systems
- Systems with no business dependency

**Action:** Create initial system inventory from asset inventory (A.5.9). Validate with IT and business stakeholders.

**Step 4: Define BIA Timeline**

Typical BIA timeline:
- Week 1-2: Preparation and stakeholder engagement
- Week 3-6: Impact assessment interviews/workshops
- Week 7-8: Data consolidation and analysis
- Week 9: BIA documentation and review
- Week 10: Executive presentation and approval

**Action:** Create BIA project plan with milestones, owners, and deadlines.

### 2.3 Prepare BIA Materials

**Step 5: Customize BIA Templates**

Use templates from Annex-B Section 3:
- BIA Interview Questions Template
- Impact Assessment Worksheet
- RPO/RTO Matrix Template

**Customization:**
- Add [Organization]-specific business processes
- Include relevant regulatory requirements
- Adjust impact categories (financial, operational, reputational, regulatory)

**Step 6: Prepare Communication Materials**

Create:
- Executive briefing (why BIA is important, what's expected)
- Stakeholder communication (timeline, interview schedule)
- BIA training materials (how to assess impact, how to determine RPO/RTO)

---

## 3. Stakeholder Engagement

### 3.1 Identify Key Stakeholders

**Step 7: Create Stakeholder Matrix**

For each system in scope, identify:
- **System Owner:** IT person responsible for system operation
- **Business Process Owner:** Business leader whose process depends on system
- **Key Users:** People who use system daily (subject matter experts)
- **Financial Stakeholder:** Person who can assess financial impact

**Example:**

| System | IT System Owner | Business Process Owner | Key Users | Financial Stakeholder |
|--------|----------------|----------------------|-----------|---------------------|
| ERP System | IT Manager | CFO, COO | Finance team, HR team | CFO |
| E-Commerce Website | Web Team Lead | VP Sales | Marketing, Customer Service | VP Sales |
| Email System | Infrastructure Manager | All departments | All employees | CIO |

### 3.2 Conduct Stakeholder Kickoff

**Step 8: Executive Briefing**

Present BIA project to executive management:
- BIA purpose and objectives
- Timeline and resource requirements
- Expected deliverables (RPO/RTO requirements, recovery priorities)
- Executive role (approval of BIA results, resource allocation)

**Duration:** 30-60 minutes

**Outcome:** Executive buy-in and commitment

**Step 9: Stakeholder Workshops**

Conduct kickoff workshop with business process owners and IT:
- Explain BIA process and methodology
- Define impact categories and how to assess
- Explain RPO and RTO concepts (with examples)
- Review BIA timeline and interview schedule

**Duration:** 2-3 hours

**Outcome:** Common understanding of BIA approach

---

## 4. Impact Assessment Process

### 4.1 Conduct BIA Interviews

**Step 10: Schedule and Conduct Interviews**

For each critical system:
- Schedule 1-2 hour interview with business process owner and IT system owner
- Use BIA Interview Questions Template (Annex-B Section 3.1)
- Document responses in Impact Assessment Worksheet

**Interview Approach:**
- Ask open-ended questions: "What happens if this system is unavailable?"
- Probe for quantitative data: "How much revenue loss per hour?"
- Explore time dimension: "What impact after 1 hour? 4 hours? 1 day? 3 days?"
- Discuss workarounds: "Can you operate manually? For how long?"

**Best Practices:**
- Record session (with permission) for later review
- Have note-taker in addition to interviewer
- Send summary to interviewee for validation
- Be empathetic (business owners may not understand technical constraints)

### 4.2 Assess Financial Impact

**Step 11: Calculate Revenue Loss**

For revenue-generating systems:
- **Direct Revenue Loss:** Revenue not generated during downtime
  - Formula: (Annual Revenue / 8760 hours) × Downtime Hours
  - Example: E-commerce site generating $50M/year → $5,707/hour revenue loss
- **Opportunity Cost:** Lost customers who move to competitors
- **Penalties:** SLA breach penalties, late fees, contractual penalties

For non-revenue systems:
- **Recovery Costs:** Cost to restore operations (labor, vendor support)
- **Productivity Loss:** Employee time wasted during downtime
  - Formula: (# Affected Employees × Hourly Rate) × Downtime Hours

**Step 12: Assess Operational Impact**

Evaluate operational disruption:
- **Critical Business Functions:** Can they continue without this system?
- **Workarounds:** Are manual workarounds available? How long sustainable?
- **Customer Impact:** Are customers unable to be served?
- **Supply Chain Impact:** Are suppliers or partners affected?
- **Cascading Failures:** Do other systems depend on this one?

**Rating Scale:**
- **Minimal:** Inconvenience only, full workarounds available
- **Moderate:** Significant disruption, difficult workarounds
- **High:** Cannot perform critical functions, no effective workarounds
- **Severe:** Complete business stoppage, existential threat

### 4.3 Assess Reputational Impact

**Step 13: Evaluate Reputational Risk**

Consider:
- **Customer Trust:** Would outage damage customer confidence?
- **Brand Reputation:** Would media coverage harm brand?
- **Competitive Position:** Would competitors gain permanent advantage?
- **Long-Term Customer Loss:** Would customers permanently leave?

**Examples:**
- Bank online banking down for 8 hours → High reputational impact (trust in bank)
- Internal HR system down for 8 hours → Low reputational impact (not customer-facing)

### 4.4 Assess Regulatory/Legal Impact

**Step 14: Identify Compliance Requirements**

Review regulatory obligations:
- **DORA (if applicable):** ICT systems supporting financial services must meet resilience requirements
- **NIS2 (if applicable):** Essential services must meet availability requirements
- **Industry-specific:** HIPAA (healthcare), PCI DSS (payment cards), etc.
- **Contractual SLAs:** Service level agreements with customers

**Compliance Impact:**
- **Regulatory Fines:** Potential penalties for non-compliance
- **Legal Liability:** Lawsuits from customers or partners
- **Audit Findings:** Non-compliance discovered in audit

---

## 5. MTPD Determination

### 5.1 Time-Based Impact Analysis

**Step 15: Map Impact Over Time**

For each system, assess impact at multiple time intervals:

**Template:**

| Time Period | Financial Impact | Operational Impact | Reputational Impact | Regulatory Impact | Overall Severity |
|-------------|------------------|-------------------|---------------------|-------------------|------------------|
| 0-1 hours | $5K | Minimal - workarounds work | None | None | **Low** |
| 1-4 hours | $20K | Moderate - workarounds difficult | Minor complaints | None | **Medium** |
| 4-24 hours | $120K | High - cannot fulfill orders | Customer complaints, some media | Possible SLA breach | **High** |
| 1-3 days | $500K | Severe - major revenue loss | Significant media, customer exodus | Regulatory investigation | **Very High** |
| 3+ days | $2M+ | Catastrophic - business failure risk | Permanent reputation damage | Major fines, legal action | **Critical** |

**Step 16: Determine MTPD**

MTPD (Maximum Tolerable Period of Disruption) is the time point where impact becomes **"Very High" or "Critical"**.

In example above:
- MTPD = 24 hours (point where impact escalates from High to Very High)

**Business Owner Decision:** MTPD is determined by business owner, not IT. IT cannot override business assessment of acceptable downtime.

### 5.2 MTPD Validation

**Step 17: Validate MTPD with Executive Management**

For critical systems with short MTPD (< 4 hours):
- Present impact analysis to executive management
- Confirm MTPD assessment is accurate
- Discuss cost implications (short MTPD requires expensive redundancy)
- Obtain executive approval of MTPD

**Why Validation Matters:**
- Short MTPD drives high BC/DR costs (redundancy, testing)
- Executive must understand cost-benefit trade-off
- Prevents unrealistic MTPD expectations

---

## 6. RPO and RTO Calculation

### 6.1 RPO Determination

**Step 18: Assess Data Loss Impact**

**RPO Question:** "How much data loss is acceptable?"

**Consider:**
- **Financial Impact of Recreating Data:** Cost to manually re-enter lost transactions
- **Regulatory Requirements:** Some data loss may be unacceptable (financial transactions)
- **Data Volatility:** How frequently does data change?

**Examples:**

**E-Commerce System:**
- Data: Customer orders, payment transactions
- Volatility: High (orders every minute)
- Regulatory: PCI DSS requires transaction integrity
- Financial Impact: Lost orders = lost revenue, cannot be recreated
- **RPO Decision: 0 hours** (no data loss acceptable)

**Internal Document Repository:**
- Data: Shared documents, wikis
- Volatility: Low (documents updated occasionally)
- Regulatory: None
- Financial Impact: Low (can recreate documents)
- **RPO Decision: 24 hours** (acceptable to lose 1 day of document edits)

**Step 19: Map RPO to Backup Frequency**

RPO drives backup frequency:
- RPO 0 (no data loss) → Continuous replication or very frequent backups (every 15-30 min)
- RPO 1 hour → Hourly backups
- RPO 4 hours → Every 4 hours
- RPO 24 hours → Daily backups
- RPO 7 days → Weekly backups

**Formula:** Backup Frequency ≤ RPO Requirement

### 6.2 RTO Determination

**Step 20: Calculate RTO from MTPD**

**RTO Question:** "How quickly must system be restored?"

**RTO is derived from MTPD:**
- RTO should be 50-75% of MTPD (provides buffer for unexpected delays)
- Formula: RTO = MTPD × 0.5 to 0.75

**Examples:**
- MTPD = 4 hours → RTO = 2-3 hours
- MTPD = 24 hours → RTO = 12-18 hours
- MTPD = 1 week → RTO = 3-5 days

**Why Buffer Needed:**
- Recovery rarely goes perfectly (issues, delays)
- Need time for validation and testing after recovery
- Want to recover well before MTPD is reached

**Step 21: Validate RTO is Achievable**

**Critical Reality Check:**
- Can system actually be restored within RTO?
- If RTO < 4 hours → Requires redundancy (restore from backup too slow)
- If RTO 4-24 hours → Daily backup may be sufficient
- If RTO > 24 hours → Weekly backup acceptable

**If RTO Not Achievable with Current Capability:**
- Document gap (Assessment Workbook 3)
- Determine remediation (implement redundancy, increase backup frequency)
- OR negotiate with business to accept longer RTO (risk acceptance)

### 6.3 RPO/RTO Documentation

**Step 22: Complete RPO/RTO Matrix**

Use template from Annex-B Section 2.2. For each system document:
- System name and description
- Business process supported
- Criticality tier (based on MTPD and impact)
- MTPD (Maximum Tolerable Period of Disruption)
- RPO Requirement
- RTO Requirement
- Justification (business rationale)

**Example:**

| System | Business Process | Criticality | MTPD | RPO | RTO | Justification |
|--------|-----------------|-------------|------|-----|-----|---------------|
| E-Commerce Website | Online Sales | Critical (Tier 1) | 4 hours | 0 hours | 2 hours | Revenue loss $5K/hour, customer exodus after 4 hours |
| ERP System | Finance, HR, Procurement | Important (Tier 2) | 24 hours | 4 hours | 12 hours | Can operate manually for 1 day, critical for month-end close |
| Document Repository | Knowledge Sharing | Standard (Tier 3) | 1 week | 24 hours | 3 days | Inconvenience only, no critical business impact |

---

## 7. Dependency Mapping

### 7.1 Identify System Dependencies

**Step 23: Map Upstream Dependencies**

For each system, identify what it depends on:
- **Infrastructure:** Network, storage, servers
- **Authentication:** Active Directory, SSO, MFA
- **Databases:** SQL servers, NoSQL databases
- **External Services:** Cloud services, APIs, third-party integrations
- **Utilities:** Power, internet connectivity
- **Hidden Dependencies:** DNS, NTP (time servers), licensing servers

**Tool:** Dependency mapping worksheet or diagram

**Example (E-Commerce Website):**
```
E-Commerce Website depends on:
  ├─ Web Servers (Infrastructure)
  ├─ Database Server (SQL)
  ├─ Authentication Service (SSO)
  ├─ Payment Gateway (Third-Party API)
  ├─ CDN (Third-Party Service)
  └─ Internet Connectivity (Network)
```

**Step 24: Map Downstream Dependencies**

Identify what depends on this system:
- **Other Systems:** Systems that integrate with this one
- **Business Processes:** Processes that cannot function without this system
- **Users:** Who cannot work without this system?

### 7.2 Dependency Impact on RPO/RTO

**Step 25: Adjust RPO/RTO for Dependencies**

**Critical Rule:** A system's RTO is constrained by its dependencies.

**Example:**
- E-Commerce Website RTO = 2 hours
- Payment Gateway (dependency) RTO = 8 hours
- **Problem:** Cannot restore E-Commerce Website in 2 hours if Payment Gateway takes 8 hours
- **Solution:** Either (a) improve Payment Gateway RTO to ≤ 2 hours, or (b) accept E-Commerce RTO = 8 hours

**Step 26: Define Recovery Sequence**

Based on dependencies, determine recovery order:
1. Recover foundational infrastructure (network, storage, authentication)
2. Recover databases
3. Recover applications
4. Recover integrations

**Recovery Priority List:**

| Priority | System | Dependencies | Reason |
|----------|--------|--------------|--------|
| 1 | Network Infrastructure | None | All systems depend on network |
| 2 | Authentication (AD) | Network | All systems depend on authentication |
| 3 | Database Server | Network, Storage | E-Commerce and ERP depend on database |
| 4 | E-Commerce Website | Network, AD, Database, Payment Gateway | Revenue-critical |
| 5 | ERP System | Network, AD, Database | Important but can wait until after E-Commerce |

---

## 8. BIA Documentation and Approval

### 8.1 Prepare BIA Report

**Step 27: Consolidate BIA Findings**

Create comprehensive BIA report including:

**Executive Summary** (1-2 pages):
- Total systems assessed
- Critical systems identified (Tier 1 count)
- Total estimated financial impact ($/hour across all critical systems)
- Key findings and recommendations

**Detailed Findings** (per system):
- Impact assessment (financial, operational, reputational, regulatory)
- MTPD determination
- RPO and RTO requirements
- Criticality tier classification
- Dependencies

**Recovery Priorities:**
- Recovery sequence (order of restoration)
- Rationale for priorities

**Gap Analysis** (preliminary):
- Systems where current BC/DR capability does not meet requirements
- Estimated cost to close gaps
- Risk if gaps not closed

**Appendices:**
- Interview summaries
- Impact assessment worksheets
- RPO/RTO matrix (complete)
- Dependency maps

**Step 28: Prepare Executive Presentation**

Create concise presentation (10-15 slides) covering:
- BIA methodology
- Key findings (critical systems, impact summary)
- RPO/RTO requirements summary
- Recovery priorities
- Gap analysis highlights
- Recommendations (investment needed, risk acceptance decisions)
- Next steps

### 8.2 BIA Review and Approval

**Step 29: Business Owner Review**

Before executive presentation:
- Circulate BIA report to all business process owners
- Request validation: "Does impact assessment accurately reflect your business?"
- Incorporate feedback and corrections
- Obtain written sign-off from business owners

**Step 30: Executive Approval**

Present BIA to executive management (CISO, CIO, COO, CFO):
- Walk through findings
- Highlight critical systems and RPO/RTO requirements
- Present gap analysis and cost implications
- Request approval of BIA results
- Request budget allocation for gap remediation

**Outcome:** Executive approval of BIA, including RPO/RTO requirements

**Documentation:** Meeting minutes, approval signatures on BIA report

---

## 9. BIA Review and Update Process

### 9.1 BIA Update Triggers

**Step 31: Define BIA Update Triggers**

BIA shall be updated when:
- **Annual Review:** Scheduled review every 12 months minimum
- **New Critical Systems:** New system deployed supporting critical business process
- **Retired Systems:** System decommissioned
- **Business Changes:**
  - Organizational restructuring
  - New business processes or products
  - Mergers, acquisitions, divestitures
  - Significant revenue model changes
- **Major Incidents:** Actual disruption revealed BIA assumptions incorrect
- **Regulatory Changes:** New compliance obligations affecting RPO/RTO

**Step 32: Establish Review Schedule**

Create annual BIA review calendar:
- Q1: Review and update BIA for Tier 1 (Critical) systems
- Q2: Review Tier 2 (Important) systems
- Q3: Review Tier 3 (Standard) systems
- Q4: Update BIA documentation, executive presentation

**Step 33: BIA Change Management**

When BIA is updated:
- Document what changed and why
- Update RPO/RTO matrix
- Assess impact on BC/DR capabilities (do gaps increase or decrease?)
- Update recovery priorities if needed
- Communicate changes to stakeholders
- Obtain approval for significant changes

---

## 10. Common Pitfalls and How to Avoid

### 10.1 IT-Driven RPO/RTO (Not Business-Driven)

**Pitfall:** IT determines RPO/RTO based on technical capability rather than business need.

**Example:**
- IT: "We do daily backups, so RPO is 24 hours."
- Reality: Business needs RPO of 4 hours for this system.
- **Problem:** Misalignment, business requirements not met.

**How to Avoid:**
- Always ask business: "How much data loss is acceptable?"
- Don't lead with technical capability ("we can do daily backups")
- If business requirement exceeds technical capability → Document as gap, remediate

### 10.2 Overly Optimistic RTO

**Pitfall:** Assuming RTO without testing actual recovery time.

**Example:**
- BIA documents RTO = 4 hours
- Assumption: "Restore from backup takes 4 hours"
- Reality: Restore actually takes 12 hours (discovered during testing)
- **Problem:** Business expects 4-hour recovery, IT cannot deliver

**How to Avoid:**
- RTO must be based on **tested** recovery time, not assumptions
- If not yet tested, document RTO as "target" pending verification
- After testing, update RTO to reflect actual capability
- If actual > requirement → Gap, implement redundancy or faster backup solution

### 10.3 Ignoring Dependencies

**Pitfall:** System RTO documented without considering dependencies.

**Example:**
- E-Commerce RTO = 2 hours
- Payment Gateway (dependency) RTO = 8 hours
- **Problem:** Cannot meet E-Commerce RTO because dependency takes longer

**How to Avoid:**
- Always map dependencies before finalizing RTO
- Adjust RTO for dependent systems (must be ≥ longest dependency RTO)
- Escalate conflicts to business owners for decision (accept longer RTO or invest in dependency)

### 10.4 Outdated BIA

**Pitfall:** BIA conducted once, never updated.

**Example:**
- BIA from 2020 documents System A as "Important"
- In 2024, System A now supports critical revenue-generating process (but BIA not updated)
- **Problem:** System A still backed up weekly (Tier 2 standard), should be hourly (Tier 1)

**How to Avoid:**
- Annual BIA review mandatory
- Trigger BIA updates when business changes occur
- Include BIA status in quarterly BC/DR reporting ("Last BIA update: 6 months ago")

### 10.5 No Executive Engagement

**Pitfall:** BIA conducted without executive involvement or approval.

**Example:**
- BC/DR Coordinator completes BIA, documents RPO/RTO requirements
- Executive management never sees BIA results
- When budget requested for BC/DR investment, executives question need ("Why so expensive?")
- **Problem:** No executive buy-in, no budget allocation

**How to Avoid:**
- Executive briefing at start of BIA (set expectations)
- Executive presentation at end of BIA (approval of requirements)
- Highlight cost implications clearly (short RTO = expensive redundancy)
- Obtain written approval of BIA results

---

## 11. Verification and Sign-Off

### 11.1 Completion Checklist

**Before considering BIA complete, verify:**

- [ ] All in-scope systems assessed (from Step 3)
- [ ] Impact assessment documented for each system (financial, operational, reputational, regulatory)
- [ ] MTPD determined for each critical system
- [ ] RPO and RTO documented for each system
- [ ] Criticality tier assigned (Tier 1-4)
- [ ] Dependencies mapped (upstream and downstream)
- [ ] Recovery priority sequence defined
- [ ] BIA report completed (executive summary, detailed findings, appendices)
- [ ] Business process owners reviewed and approved impact assessments
- [ ] Executive management presentation delivered
- [ ] Executive approval obtained (written sign-off on BIA report)
- [ ] BIA results entered into Assessment Workbook 3 (RPO/RTO Compliance Matrix)
- [ ] BIA documentation stored in evidence repository

### 11.2 Evidence to Collect

**BIA Evidence for Audit:**
- Interview notes and recordings (with permission)
- Impact assessment worksheets (completed for each system)
- RPO/RTO matrix (complete, approved)
- Dependency maps
- BIA report (final version with executive approval)
- Executive presentation slides
- Approval meeting minutes
- Business owner sign-offs

**Storage:** Centralized evidence repository, retained for 3+ years

### 11.3 Stakeholder Approval

**Required Approvals:**

| Stakeholder | Approval For | Format |
|-------------|-------------|--------|
| Business Process Owners | Impact assessment accuracy for their systems | Written sign-off on BIA worksheets |
| BC/DR Coordinator | BIA methodology and completeness | Signature on BIA report |
| CISO / CIO | BIA results and RPO/RTO requirements | Signature on BIA report |
| Executive Management | BIA results, budget allocation for gaps | Meeting minutes, signature on BIA report |

---

## 12. Next Steps

### 12.1 After BIA Completion

**Immediate Actions:**
1. **Gap Assessment** (IMP-S5): Compare BIA requirements to current BC/DR capabilities
2. **Backup Implementation** (IMP-S2): Implement backups aligned with RPO requirements
3. **Redundancy Implementation** (IMP-S3): Implement redundancy for systems requiring short RTO
4. **Testing** (IMP-S4): Test recovery capabilities to verify RTO is achievable

### 12.2 Ongoing BIA Maintenance

- **Quarterly:** Review BIA update triggers, assess if BIA update needed
- **Annually:** Conduct scheduled BIA review and update
- **As Needed:** Update BIA when significant business changes occur

### 12.3 Integration with BC/DR Program

BIA results feed into:
- **Backup planning:** RPO requirements drive backup frequency
- **Redundancy planning:** RTO requirements drive redundancy decisions
- **Testing priorities:** Critical systems (Tier 1) tested most frequently
- **Budget planning:** Gap remediation costs included in annual BC/DR budget

---

**Document End**

*"The business defines what's critical, IT determines how to protect it."*

*BIA is the foundation of effective BC/DR - invest time to get it right.*

---

**APPROVAL SIGNATURES**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| BC/DR Coordinator | | | |
| CISO / CIO | | | |
| CFO (Financial Impact Validation) | | | |
| COO (Operational Impact Validation) | | | |

**Next Review Date:** [One year from approval date]