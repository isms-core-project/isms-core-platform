**ISMS-IMP-A.5.3.2-UG - Conflict Analysis**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.3: Policies for Segregation of Duties

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.3.2-UG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.3 Segregation of Duties |
| **Parent Policy** | ISMS-POL-A.5.3 - Segregation of Duties |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.3.2-TG.

---

## Assessment Overview

### Purpose

This workbook provides detailed analysis of segregation of duties conflicts identified in the SoD Matrix Assessment (ISMS-IMP-A.5.3.1). While the SoD Matrix identifies WHAT conflicts exist, this Conflict Analysis workbook examines WHY they are problematic and HOW they create risk.

The assessment serves multiple purposes:
- **Root Cause Analysis**: Understand why conflicts exist (process design, resource constraints, etc.)
- **Impact Assessment**: Quantify the potential damage from each conflict
- **Control Mapping**: Document which controls mitigate each conflict type
- **Trend Tracking**: Monitor conflict patterns over time
- **Prioritisation**: Enable risk-based remediation prioritisation

### Scope

The Conflict Analysis covers all conflicts identified in ISMS-IMP-A.5.3.1, categorised by:

| Conflict Category | Description | Examples |
|-------------------|-------------|----------|
| **Maker-Checker** | Same person creates and approves | Create payment + Approve payment |
| **Requestor-Approver** | Same person requests and approves | Request access + Approve access |
| **Developer-Deployer** | Same person writes and deploys code | Write code + Deploy to production |
| **Administrator-Auditor** | Same person manages and audits systems | Admin system + Review admin logs |
| **Creator-Reconciler** | Same person creates and reconciles records | Enter transactions + Reconcile accounts |
| **Custodian-Owner** | Same person has custody and ownership | Hold assets + Approve asset use |

**Analysis Depth:**
- Each conflict receives individual risk scoring
- Business process context documented
- Exploitation scenarios described
- Historical incidents referenced where applicable
- Control effectiveness evaluated

### Business Value

A thorough conflict analysis delivers:

| Value Area | Benefit |
|------------|---------|
| **Risk Prioritisation** | Focus remediation on highest-impact conflicts |
| **Resource Allocation** | Justify security investment with quantified risk |
| **Audit Defence** | Demonstrate thorough risk analysis to auditors |
| **Executive Communication** | Translate technical conflicts into business risk |
| **Control Design** | Inform design of compensating controls |
| **Trend Analysis** | Track improvement over time |

### Assessment Frequency

| Activity | Frequency | Trigger Events |
|----------|-----------|----------------|
| Full Conflict Analysis | Annual | New SoD Matrix Assessment |
| Impact Score Review | Quarterly | Business process changes |
| Control Effectiveness Check | Quarterly | Control modifications |
| Trend Analysis Update | Quarterly | Each analysis cycle |
| Scenario Library Update | Semi-annual | New threat intelligence |

---

## Control Requirements

### ISO 27001:2022 Control A.5.3

Per ISO/IEC 27001:2022 Control A.5.3:

> *"Conflicting duties and conflicting areas of responsibility should be segregated."*

**Control Type:** Preventive
**Security Properties:** Confidentiality, Integrity, Availability
**Cybersecurity Concepts:** Protect
**Operational Capabilities:** Governance, Identity and Access Management

This workbook operationalises the requirement by ensuring conflicts are not just identified but thoroughly analysed to enable informed risk decisions.

### What Auditors Look For

ISO 27001 auditors examining conflict analysis will verify:

| Audit Focus | Evidence Required |
|-------------|-------------------|
| **Risk Assessment** | Documented impact analysis for each conflict |
| **Prioritisation** | Risk-based ranking of conflicts |
| **Business Context** | Understanding of why conflicts exist |
| **Control Mapping** | Evidence of mitigating controls |
| **Trend Data** | Historical tracking showing improvement |
| **Management Attention** | Regular review and escalation evidence |

### Why This Matters

**The Analysis Gap:**
Many organisations identify conflicts but fail to analyse them properly. This leads to:
- Treating all conflicts equally (wasting resources on low-risk issues)
- Missing high-impact conflicts that don't look obvious
- Implementing controls that don't address actual risks
- Audit findings for "inadequate analysis"

**Stage 2 Audit Requirements:**
Auditors expect to see evidence that conflicts have been analysed, not just listed. This workbook provides:
- Risk-based prioritisation rationale
- Impact quantification for each conflict
- Control mapping showing mitigation
- Trend data demonstrating management attention

---

## Prerequisites

### Required Documents

- [ ] Completed ISMS-IMP-A.5.3.1 SoD Matrix Assessment
- [ ] Gap Analysis from SoD Matrix (list of actual conflicts)
- [ ] Business process documentation for affected processes
- [ ] Historical incident data related to SoD failures
- [ ] Control catalogue for available mitigations
- [ ] Risk assessment methodology documentation
- [ ] Prior conflict analysis (if available)

### Required Personnel

| Role | Responsibility | Time Commitment |
|------|----------------|-----------------|
| **Conflict Analyst** | Conduct analysis, document findings | 4-8 hours per 10 conflicts |
| **Process Owners** | Explain business context, validate impact | 1-2 hours per process |
| **Risk Manager** | Validate risk scoring, approve ratings | 2-4 hours total |
| **Control Owners** | Confirm control effectiveness | 1-2 hours per control type |
| **Internal Audit** | Independent validation of analysis | 4-8 hours total |

### Required Access

| System | Purpose | Access Level Needed |
|--------|---------|---------------------|
| Risk Register | Risk methodology reference | Read access |
| Incident Management | Historical incident data | Report access |
| Control Library | Available control documentation | Read access |
| ISMS-IMP-A.5.3.1 | Source conflict data | Full access |

### Prerequisite Checklist

Before proceeding, verify:

- [ ] ISMS-IMP-A.5.3.1 completed and approved
- [ ] Gap Analysis data exported
- [ ] Process owner availability confirmed
- [ ] Risk methodology documentation available
- [ ] Historical incident data accessible
- [ ] Control catalogue current

---

## Completion Walkthrough

### Step 1: Populate Conflict Register

**Time allocation:** 1-2 hours

**Purpose:** Import all conflicts from ISMS-IMP-A.5.3.1 for detailed analysis.

**Fields to Complete:**

| Field | Description | Example |
|-------|-------------|---------|
| Conflict_ID | Unique identifier | CON-2026-001 |
| Gap_ID | Reference to SoD Matrix | GAP-2026-001 |
| Conflict_Category | Type classification | Maker-Checker |
| Role_A | First conflicting role | AP Clerk |
| Role_B | Second conflicting role | Treasurer |
| Process | Affected business process | Accounts Payable |
| Conflict_Type | From matrix (X, C, M) | X |
| Persons_Affected | Count of people with conflict | 2 |
| Analysis_Status | Current state | Pending / In Progress / Complete |

**Worked Example - Conflict Register:**

| Conflict_ID | Gap_ID | Conflict_Category | Role_A | Role_B | Process | Conflict_Type | Persons_Affected |
|-------------|--------|-------------------|--------|--------|---------|:-------------:|:----------------:|
| CON-2026-001 | GAP-2026-001 | Maker-Checker | AP Clerk | Payment Approver | Accounts Payable | X | 1 |
| CON-2026-002 | GAP-2026-002 | Creator-Reconciler | GL Accountant | Bank Reconciler | Financial Close | C | 2 |
| CON-2026-003 | GAP-2026-003 | Developer-Deployer | Developer | Production Deployer | Software Release | X | 3 |
| CON-2026-004 | GAP-2026-004 | Admin-Auditor | System Admin | Audit Analyst | IT Operations | X | 1 |
| CON-2026-005 | GAP-2026-005 | Requestor-Approver | Access Requester | Access Approver | Identity Mgmt | X | 2 |

### Step 2: Complete Impact Assessment

**Time allocation:** 2-4 hours

**Purpose:** Quantify the potential impact of each conflict if exploited.

**Impact Dimensions:**

| Dimension | Description | Scale |
|-----------|-------------|-------|
| **Financial** | Potential monetary loss | 1-5 (1 = <10K, 5 = >1M) |
| **Operational** | Business disruption severity | 1-5 (1 = Minor, 5 = Critical) |
| **Reputational** | Brand/trust damage | 1-5 (1 = Internal only, 5 = Public crisis) |
| **Compliance** | Regulatory penalty risk | 1-5 (1 = Warning, 5 = License revocation) |
| **Data** | Information compromise scale | 1-5 (1 = <100 records, 5 = >100K records) |

**Impact Scale Definitions:**

**Financial Impact:**
| Score | Range | Description |
|:-----:|-------|-------------|
| 1 | <CHF 10,000 | Minor financial impact, recoverable |
| 2 | CHF 10,000 - 50,000 | Moderate impact, affects budget |
| 3 | CHF 50,000 - 250,000 | Significant impact, executive attention |
| 4 | CHF 250,000 - 1,000,000 | Major impact, board notification |
| 5 | >CHF 1,000,000 | Severe impact, existential threat |

**Operational Impact:**
| Score | Description |
|:-----:|-------------|
| 1 | Minor inconvenience, no service disruption |
| 2 | Some process delays, workarounds available |
| 3 | Significant delays, limited service impact |
| 4 | Major service disruption, customer impact |
| 5 | Critical business failure, extended outage |

**Reputational Impact:**
| Score | Description |
|:-----:|-------------|
| 1 | Internal awareness only |
| 2 | Limited external awareness, no media |
| 3 | Local media coverage, customer inquiries |
| 4 | National media coverage, regulatory attention |
| 5 | International coverage, brand damage |

**Compliance Impact:**
| Score | Description |
|:-----:|-------------|
| 1 | Minor non-conformity, internal correction |
| 2 | Documented non-conformity, audit finding |
| 3 | Regulatory inquiry, formal response required |
| 4 | Regulatory investigation, potential fine |
| 5 | Enforcement action, license risk |

**Data Impact:**
| Score | Records at Risk | Description |
|:-----:|-----------------|-------------|
| 1 | <100 | Limited personal data exposure |
| 2 | 100-1,000 | Moderate data exposure |
| 3 | 1,000-10,000 | Significant data exposure |
| 4 | 10,000-100,000 | Major data breach |
| 5 | >100,000 | Mass data breach, notification required |

**Overall Impact Formula:**
```
Overall_Impact = MAX(Financial, Operational, Reputational, Compliance, Data)
```

**Worked Example - Impact Assessment:**

| Conflict_ID | Financial | Operational | Reputational | Compliance | Data | Overall |
|-------------|:---------:|:-----------:|:------------:|:----------:|:----:|:-------:|
| CON-2026-001 | 4 | 2 | 3 | 4 | 1 | **4** |
| CON-2026-002 | 3 | 2 | 2 | 3 | 1 | **3** |
| CON-2026-003 | 3 | 5 | 4 | 3 | 4 | **5** |
| CON-2026-004 | 2 | 4 | 3 | 3 | 3 | **4** |
| CON-2026-005 | 2 | 3 | 2 | 3 | 3 | **3** |

### Step 3: Document Exploitation Scenarios

**Time allocation:** 2-4 hours

**Purpose:** Describe how each conflict could realistically be exploited.

**Scenario Components:**

| Component | Description | Example |
|-----------|-------------|---------|
| **Threat Actor** | Who could exploit | Disgruntled employee, external attacker |
| **Motivation** | Why they would exploit | Financial gain, sabotage, espionage |
| **Method** | How they would exploit | Create fake vendor, approve own payment |
| **Detection Difficulty** | How hard to detect | High - no independent verification |
| **Historical Precedent** | Similar incidents known | Yes - 2019 AP fraud at [Company] |

**Scenario Template:**
```
Conflict: AP Clerk + Treasurer
Scenario: Fictitious Vendor Fraud

A person holding both roles could:
1. Create a new vendor record using a fictitious company name
2. Submit invoices from the fictitious vendor
3. Approve their own invoices without management review
4. Process payments to a bank account they control
5. Reconcile the payments to hide the discrepancy

Detection: Unlikely without independent audit
Historical: Similar scheme caused $2.4M loss at comparable organisation
```

**Worked Example - Exploitation Scenarios:**

| Scenario_ID | Conflict_ID | Scenario_Name | Threat_Actor | Method | Detection_Difficulty |
|-------------|-------------|---------------|--------------|--------|:--------------------:|
| SCN-001 | CON-2026-001 | Fictitious Vendor Fraud | Insider-Malicious | Create fake vendor, approve own invoices | Very High |
| SCN-002 | CON-2026-002 | Financial Statement Manipulation | Insider-Malicious | Enter false entries, reconcile to hide | High |
| SCN-003 | CON-2026-003 | Malicious Code Deployment | Insider-Malicious | Write backdoor, deploy without review | Very High |
| SCN-004 | CON-2026-003 | Accidental Production Error | Insider-Negligent | Deploy untested code to production | Medium |
| SCN-005 | CON-2026-004 | Audit Trail Manipulation | Insider-Malicious | Perform action, delete/modify logs | Very High |
| SCN-006 | CON-2026-005 | Privilege Escalation | Insider-Malicious | Request elevated access, self-approve | High |

**Detection Difficulty Scale:**

| Rating | Description | Detection Method |
|--------|-------------|------------------|
| Very Low | Easily detected automatically | Real-time monitoring with alerts |
| Low | Detected with routine monitoring | Regular automated reports |
| Medium | Detected with periodic review | Quarterly access reviews |
| High | Requires targeted investigation | Internal audit procedures |
| Very High | Likely undetected without tip-off | Whistleblower or external audit |

### Step 4: Map Mitigating Controls

**Time allocation:** 2-4 hours

**Purpose:** Document which controls reduce risk for each conflict.

**Control Categories:**

| Category | Examples | Effectiveness |
|----------|----------|---------------|
| **Preventive** | RBAC, workflow approval | High - stops before occurrence |
| **Detective** | Log review, reconciliation | Medium - identifies after occurrence |
| **Corrective** | Incident response, recovery | Low - addresses after damage |
| **Compensating** | Enhanced monitoring | Variable - depends on implementation |

**Control Mapping Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| Mapping_ID | Unique identifier | MAP-2026-001 |
| Conflict_ID | Related conflict | CON-2026-001 |
| Control_ID | Reference to control | CTL-FIN-001 |
| Control_Name | Descriptive name | Dual Approval Workflow |
| Control_Type | Preventive/Detective/etc. | Preventive |
| Effectiveness | Rating | High / Medium / Low |
| Implementation_Status | Current state | Implemented / Partial / Planned |
| Gap_Notes | What's missing | Email approval; system-enforced needed |

**Worked Example - Control Mapping:**

| Mapping_ID | Conflict_ID | Control_Name | Control_Type | Effectiveness | Implementation_Status |
|------------|-------------|--------------|--------------|:-------------:|:---------------------:|
| MAP-001 | CON-2026-001 | Dual Approval Workflow | Preventive | High | Partial |
| MAP-002 | CON-2026-001 | Daily Transaction Review | Detective | Medium | Implemented |
| MAP-003 | CON-2026-002 | Independent Reconciliation | Preventive | High | Not Implemented |
| MAP-004 | CON-2026-003 | Code Review Requirement | Preventive | High | Implemented |
| MAP-005 | CON-2026-003 | Deployment Approval Gate | Preventive | High | Partial |
| MAP-006 | CON-2026-004 | Immutable Logging | Preventive | High | Implemented |
| MAP-007 | CON-2026-004 | Independent Log Review | Detective | Medium | Partial |

**Control Effectiveness Criteria:**

| Rating | Criteria |
|--------|----------|
| **High** | Control is automated, consistently applied, and regularly tested |
| **Medium** | Control is documented, generally applied, but has manual elements |
| **Low** | Control exists but is inconsistently applied or not enforced |

### Step 5: Analyse Trends

**Time allocation:** 1-2 hours

**Purpose:** Track conflict patterns over time to identify systemic issues.

**Trend Metrics:**

| Metric | Description | Target |
|--------|-------------|--------|
| Total Conflicts | Count of identified conflicts | Decreasing |
| Critical Conflicts | Count of X-type conflicts | Zero |
| Resolution Rate | % resolved within target | >90% |
| New Conflicts | Net new per quarter | Decreasing |
| Recurrence Rate | Previously resolved, returned | <5% |
| Mean Time to Resolution | Average days to resolve | <30 days |

**Trend Analysis Questions:**
- Are conflicts concentrated in specific departments?
- Do conflicts increase after reorganisations?
- Are certain conflict types persistent?
- Are compensating controls working?
- Is the organisation improving over time?

**Worked Example - Trend Analysis:**

| Period | Total_Conflicts | Critical_Conflicts | Resolved | New | MTTR | Resolution_Rate |
|--------|:---------------:|:------------------:|:--------:|:---:|:----:|:---------------:|
| 2025-Q1 | 25 | 5 | 10 | 8 | 45 | 40% |
| 2025-Q2 | 23 | 4 | 12 | 10 | 38 | 52% |
| 2025-Q3 | 21 | 3 | 14 | 12 | 32 | 67% |
| 2025-Q4 | 19 | 2 | 16 | 14 | 28 | 84% |
| 2026-Q1 | 17 | 1 | 15 | 13 | 25 | 88% |

### Step 6: Create Prioritisation Matrix

**Time allocation:** 1-2 hours

**Purpose:** Rank conflicts for remediation based on risk.

**Prioritisation Formula:**
```
Priority_Score = Impact_Score x Likelihood_Score x (1 - Control_Effectiveness)
```

Where:
- Impact_Score: 1-5 from Impact_Assessment
- Likelihood_Score: 1-5 based on exploitation difficulty
- Control_Effectiveness: 0.0-1.0 (High=0.8, Medium=0.5, Low=0.2)

**Priority Levels:**

| Score Range | Priority | Action Timeline |
|:-----------:|:--------:|-----------------|
| 15-25 | Critical | Immediate (< 7 days) |
| 10-14 | High | Short-term (< 30 days) |
| 5-9 | Medium | Medium-term (< 90 days) |
| 1-4 | Low | Long-term (< 180 days) |

**Likelihood Scoring:**

| Score | Likelihood | Criteria |
|:-----:|------------|----------|
| 1 | Rare | Highly unlikely, requires extraordinary circumstances |
| 2 | Unlikely | Could occur but no history or clear motivation |
| 3 | Possible | Has occurred elsewhere, could happen here |
| 4 | Likely | Has occurred here before, conditions favourable |
| 5 | Almost Certain | Expected to occur without intervention |

**Worked Example - Prioritisation Matrix:**

| Conflict_ID | Impact | Likelihood | Control_Eff | Priority_Score | Priority | Timeline |
|-------------|:------:|:----------:|:-----------:|:--------------:|:--------:|----------|
| CON-2026-001 | 4 | 4 | 0.5 | 8.0 | Medium | <90 days |
| CON-2026-002 | 3 | 3 | 0.2 | 7.2 | Medium | <90 days |
| CON-2026-003 | 5 | 4 | 0.6 | 8.0 | Medium | <90 days |
| CON-2026-004 | 4 | 3 | 0.8 | 2.4 | Low | <180 days |
| CON-2026-005 | 3 | 4 | 0.5 | 6.0 | Medium | <90 days |

---

## Exploitation Scenario Library

### Financial Process Conflicts

**Scenario: Fictitious Vendor Fraud**
- **Conflict**: Vendor creation + Payment approval
- **Method**: Create fake vendor, submit/approve own invoices
- **Impact**: Direct financial loss
- **Detection**: Vendor validation, payment pattern analysis
- **Controls**: Independent vendor approval, payment limits, matching

**Scenario: Payroll Ghost Employees**
- **Conflict**: Employee creation + Payroll processing
- **Method**: Create fictitious employees, process payments
- **Impact**: Ongoing financial drain
- **Detection**: Headcount reconciliation, manager attestation
- **Controls**: HR verification, manager sign-off, address validation

**Scenario: Expense Report Fraud**
- **Conflict**: Submit expenses + Approve expenses
- **Method**: Submit inflated or personal expenses, self-approve
- **Impact**: Financial loss, policy violation
- **Detection**: Receipt verification, expense analytics
- **Controls**: Manager approval, receipt requirements, spending limits

**Scenario: Bank Reconciliation Fraud**
- **Conflict**: Cash handling + Bank reconciliation
- **Method**: Embezzle cash, falsify reconciliation
- **Impact**: Financial loss, hidden theft
- **Detection**: Independent reconciliation, surprise audits
- **Controls**: Dual custody, independent verification, rotation

### IT Operations Conflicts

**Scenario: Malicious Code Deployment**
- **Conflict**: Code development + Production deployment
- **Method**: Write backdoor, deploy without review
- **Impact**: System compromise, data breach
- **Detection**: Code review process, deployment logs
- **Controls**: Mandatory code review, deployment approval, CI/CD controls

**Scenario: Privileged Access Abuse**
- **Conflict**: Account creation + Access approval
- **Method**: Create elevated account, approve own access
- **Impact**: Unauthorised system access
- **Detection**: Access certification, privilege monitoring
- **Controls**: Separation of duties, access reviews, PAM

**Scenario: Evidence Destruction**
- **Conflict**: System administration + Log management
- **Method**: Perform malicious action, delete logs
- **Impact**: Destroyed audit trail, undetected breach
- **Detection**: Immutable logging, SIEM correlation
- **Controls**: Log forwarding, WORM storage, integrity monitoring

**Scenario: Configuration Manipulation**
- **Conflict**: Configuration change + Configuration approval
- **Method**: Modify security controls, self-approve
- **Impact**: Weakened security posture
- **Detection**: Configuration monitoring, change tracking
- **Controls**: Change management, configuration baselines

### Procurement Conflicts

**Scenario: Kickback Scheme**
- **Conflict**: Vendor selection + Contract approval
- **Method**: Select vendor offering kickbacks, approve contract
- **Impact**: Inflated costs, corruption
- **Detection**: Bid analysis, vendor relationship review
- **Controls**: Competitive bidding, rotation of buyers, relationship disclosure

**Scenario: Goods Receipt Fraud**
- **Conflict**: Order goods + Receive goods
- **Method**: Order excess, divert upon receipt
- **Impact**: Inventory loss, financial loss
- **Detection**: Three-way matching, inventory audits
- **Controls**: Independent receiving, matching, cycle counts

**Scenario: Invoice Manipulation**
- **Conflict**: Invoice entry + Invoice approval
- **Method**: Enter inflated invoice, approve payment
- **Impact**: Overpayment to vendors
- **Detection**: Invoice analytics, vendor statement reconciliation
- **Controls**: Three-way match, approval limits, vendor confirmations

### HR Conflicts

**Scenario: Salary Manipulation**
- **Conflict**: Salary entry + Payroll approval
- **Method**: Increase own salary, approve payroll
- **Impact**: Excess compensation, budget impact
- **Detection**: Compensation benchmarking, budget variance analysis
- **Controls**: HR approval, compensation committee, budget controls

**Scenario: Benefits Fraud**
- **Conflict**: Benefits enrolment + Benefits approval
- **Method**: Enrol ineligible dependents, approve coverage
- **Impact**: Excess benefit costs
- **Detection**: Dependent verification, claims analysis
- **Controls**: Dependent audit, verification requirements

---

## Evidence Collection

### Evidence Requirements

| Evidence Type | Source | Retention |
|---------------|--------|-----------|
| Conflict Analysis Workbook | Generated | 7 years |
| Impact Assessment Documentation | Analysis process | 7 years |
| Exploitation Scenarios | Security team | 7 years |
| Control Effectiveness Testing | Internal audit | 3 years |
| Trend Analysis Reports | Periodic updates | 7 years |
| Historical Incident Data | Incident management | 7 years |

### Evidence Storage

**Primary Location:** `[SharePoint/Evidence Library]/A.5.3/Conflict-Analysis/[Year]/`

**Folder Structure:**
```
A.5.3/
|-- Conflict-Analysis/
|   |-- 2026/
|   |   |-- Assessment-Workbooks/
|   |   |   |-- ISMS-IMP-A.5.3.2_Conflict_Analysis_20260203.xlsx
|   |   |-- Impact-Assessment/
|   |   |   |-- Impact-Scoring-Methodology.pdf
|   |   |   |-- Impact-Assessment-Working-Papers.xlsx
|   |   |-- Exploitation-Scenarios/
|   |   |   |-- Financial-Scenarios.pdf
|   |   |   |-- IT-Operations-Scenarios.pdf
|   |   |-- Control-Mapping/
|   |   |   |-- Control-Effectiveness-Testing.xlsx
|   |   |   |-- Control-Gap-Analysis.pdf
|   |   |-- Trend-Analysis/
|   |   |   |-- Quarterly-Trend-Report-Q1-2026.pdf
|   |   |   |-- Historical-Data.xlsx
```

**Naming Convention:**
```
EVD-A.5.3.2_[EvidenceType]_[Reference]_[YYYYMMDD].[ext]
```

---

## Common Pitfalls

Avoid these common mistakes when completing the Conflict Analysis:

### Impact Assessment Pitfalls

❌ **MISTAKE**: Treating all conflicts with equal urgency
✅ **CORRECT**: Use risk-based prioritisation to focus on highest-impact conflicts first; not all conflicts pose equal risk

❌ **MISTAKE**: Using subjective impact scores without methodology
✅ **CORRECT**: Apply consistent scoring methodology with defined criteria; document rationale for each score

❌ **MISTAKE**: Ignoring compounding effects of multiple conflicts
✅ **CORRECT**: Consider scenarios where multiple conflicts combine to create greater risk; a person with three low-risk conflicts may create high aggregate risk

❌ **MISTAKE**: Scoring impact based on current controls rather than inherent risk
✅ **CORRECT**: Score impact assuming no controls exist; control effectiveness is factored separately in prioritisation

### Scenario Development Pitfalls

❌ **MISTAKE**: Analysing conflicts without business context
✅ **CORRECT**: Always document the process context - why the conflict exists, how it arose, what business need it serves

❌ **MISTAKE**: Documenting exploitation scenarios too generically
✅ **CORRECT**: Make scenarios specific to your organisation's systems and processes; generic scenarios don't enable targeted controls

❌ **MISTAKE**: Focusing only on intentional exploitation
✅ **CORRECT**: Include accidental error scenarios - many SoD failures are not fraud but honest mistakes that cause harm

❌ **MISTAKE**: Not considering collusion scenarios
✅ **CORRECT**: Some conflicts are only exploitable through collusion; document this and assess likelihood of collusion

### Control Mapping Pitfalls

❌ **MISTAKE**: Mapping controls without assessing effectiveness
✅ **CORRECT**: Evaluate whether controls are actually working, not just present; a control that exists on paper but isn't followed provides no protection

❌ **MISTAKE**: Assuming automated controls are always effective
✅ **CORRECT**: Verify automated controls are properly configured and monitored; automation can fail or be bypassed

❌ **MISTAKE**: Not identifying control gaps
✅ **CORRECT**: Explicitly document where controls are missing or insufficient; this drives remediation planning

❌ **MISTAKE**: Counting compensating controls as full mitigation
✅ **CORRECT**: Compensating controls reduce but don't eliminate risk; factor residual risk into prioritisation

### Trend Analysis Pitfalls

❌ **MISTAKE**: Not tracking trends over time
✅ **CORRECT**: Maintain historical data to identify patterns and measure progress; single-point-in-time analysis misses trends

❌ **MISTAKE**: Treating new conflicts as failures
✅ **CORRECT**: New conflict identification is a sign of improving detection; track net change, not just new conflicts

❌ **MISTAKE**: Not investigating recurring conflicts
✅ **CORRECT**: Conflicts that recur indicate systemic issues; investigate root cause and address process design

❌ **MISTAKE**: Ignoring resolution time trends
✅ **CORRECT**: Track mean time to resolution; increasing MTTR indicates remediation bottlenecks

### Documentation Pitfalls

❌ **MISTAKE**: Completing analysis once and never updating
✅ **CORRECT**: Refresh analysis quarterly or when significant changes occur; business processes and threats evolve

❌ **MISTAKE**: Accepting "we've always done it this way" as justification
✅ **CORRECT**: Challenge historical practices that create unnecessary conflicts; legacy processes often predate security awareness

❌ **MISTAKE**: Documenting scenarios without remediation recommendations
✅ **CORRECT**: Each scenario should include recommended controls to prevent exploitation; analysis without action is incomplete

❌ **MISTAKE**: Not linking analysis to source conflicts
✅ **CORRECT**: Maintain clear traceability from A.5.3.1 Gap_Analysis to this analysis; auditors expect clear linkage

---

## Quality Checklist

Before submitting the completed workbook, verify all items:

### Completeness Checks

- [ ] All conflicts from ISMS-IMP-A.5.3.1 imported
- [ ] Every conflict has impact assessment completed
- [ ] Exploitation scenarios documented for high/critical conflicts
- [ ] Control mapping completed for all conflicts
- [ ] Trend analysis includes minimum 2 data points (or baseline documented)
- [ ] Prioritisation matrix calculated for all conflicts

### Methodology Checks

- [ ] Impact scoring methodology documented
- [ ] All impact scores have documented rationale
- [ ] Likelihood scores based on defined criteria
- [ ] Control effectiveness ratings verified
- [ ] Priority calculations correct

### Coverage Checks

- [ ] Financial process conflicts analysed
- [ ] IT operations conflicts analysed
- [ ] Procurement conflicts analysed
- [ ] HR conflicts analysed
- [ ] All conflict categories represented

### Accuracy Checks

- [ ] Impact scores validated by process owners
- [ ] Exploitation scenarios reviewed by risk manager
- [ ] Control effectiveness ratings verified by control owners
- [ ] Prioritisation scores calculated correctly

### Documentation Checks

- [ ] Evidence references linked
- [ ] Historical incidents cited where applicable
- [ ] Compensating control details sufficient
- [ ] Analysis methodology documented
- [ ] All required attachments present

### Process Checks

- [ ] Process owners signed off on their areas
- [ ] Risk manager approved overall analysis
- [ ] CISO reviewed prioritisation
- [ ] Workbook saved with correct naming convention
- [ ] Evidence stored in ISMS Evidence Library

---

## Review and Approval

### Review Workflow

| Step | Role | Responsibility | Timeline |
|------|------|----------------|----------|
| 1 | Conflict Analyst | Complete all sheets | By deadline |
| 2 | Process Owners | Validate impact, scenarios | 5 business days |
| 3 | Risk Manager | Approve risk ratings | 3 business days |
| 4 | Internal Audit | Independent validation | 5 business days |
| 5 | CISO | Approve prioritisation | 3 business days |

### Approval Workflow

```
Conflict Analyst Completes
        │
        ▼
Self-Review (Quality Checklist)
        │
        ▼
Process Owners Validate ────────► Return for Corrections
        │                                │
        ▼                                │
Risk Manager Review ────────────► Return for Corrections
        │                                │
        ▼                                │
Internal Audit Validation ──────► Return for Corrections
        │                                │
        ▼                                │
CISO Final Approval ─────────────────────┘
        │
        ▼
   Analysis Complete
        │
        ▼
   Upload to ISMS Evidence Library
```

### Post-Approval Actions

Upon approval:

1. Upload completed workbook to ISMS Evidence Library
2. Update ISMS control status
3. Communicate prioritisation to remediation owners
4. Schedule next analysis cycle
5. Update A.5.3.4 Dashboard with new data

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
