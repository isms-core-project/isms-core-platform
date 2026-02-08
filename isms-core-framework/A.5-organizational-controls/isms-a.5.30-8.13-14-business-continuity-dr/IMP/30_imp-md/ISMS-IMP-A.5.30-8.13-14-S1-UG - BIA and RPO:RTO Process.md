**ISMS-IMP-A.5.30-8.13-14-S1-UG - BIA and RPO/RTO Process**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.13: Information Backup

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.30-8.13-14-S1-UG |
| **Version** | 1.0 |
| **Assessment Area** | Business Impact Analysis & Recovery Requirements Definition |
| **Related Policy** | ISMS-POL-A.5.30-8.13-14, Section 2.3.1 (Business Impact Analysis Requirements) |
| **Purpose** | Define systematic methodology for conducting BIA, determining system criticality, establishing RPO/RTO requirements, documenting recovery priorities |
| **Target Audience** | BC/DR Coordinator, Business Process Owners, System Owners, IT Management, Executive Management, Risk Management, Compliance Officers |
| **Assessment Type** | Business & Technical |
| **Review Cycle** | Annual or After Major Business/System Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial methodology for BIA and RPO/RTO determination | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.30-8.13-14-S1-TG.

---

# Assessment Overview

## What This Assessment Achieves

**Assessment Name:** ISMS-IMP-A.5.30-8.13-14-S1 - Business Impact Analysis and RPO/RTO Process

### The BIA Challenge

Business Impact Analysis answers the fundamental questions that drive ALL BC/DR investment:

- **Which systems are truly critical?** (Not "everything is critical")
- **How fast must they recover?** (RTO - Recovery Time Objective)
- **How much data loss is tolerable?** (RPO - Recovery Point Objective)
- **What are the dependencies?** (System interdependencies, recovery sequence)
- **What's the business justification?** (Financial impact, regulatory requirements, reputational risk)

**Without BIA:** BC/DR is guesswork. IT implements backup and redundancy based on convenience ("backup everything nightly, call it good"), not business requirements. When disaster strikes, you discover that your 24-hour RTO for the payment system doesn't meet the business requirement of 4 hours, and CHF 500K in revenue is lost.

**With BIA:** BC/DR is business-driven. Every backup schedule, every redundancy decision, every recovery priority is justified by documented business impact. When auditors ask "Why do you backup this database hourly?" the answer is "BIA determined RPO of 1 hour based on CHF 50K/hour revenue impact" - not "because we always have."

### BIA Process Outputs

Upon completion, [Organization] will have:

1. **Business Process Inventory** - All critical business processes documented
2. **System-Process Mapping** - Which ICT systems support which business processes
3. **Impact Assessment** - Quantified impact of disruption (financial, operational, regulatory, reputational)
4. **System Criticality Classification** - Tier 1-4 classification for every system
5. **RPO/RTO Requirements** - Business-justified recovery requirements per system
6. **Dependency Map** - System interdependencies and recovery sequence
7. **Gap Analysis** - Where current capabilities don't meet requirements
8. **Executive Approval** - Written sign-off from executive management
9. **BIA Report** - Comprehensive documentation for audit evidence

## Why This Matters - The Foundation of BC/DR

**Critical Principle:** All BC/DR technical decisions flow from BIA findings.

```
                    BIA DRIVES EVERYTHING
                            |
                +-----------+----------+
                |           |          |
        Backup Freq    Redundancy   Testing
        (RPO-driven)   (RTO-driven)  Priorities
                |           |          |
           IMP-S2      IMP-S3      IMP-S4
```

**Without BIA - The Cargo Cult BC/DR:**

- "We backup everything nightly" → Wastes backup storage on non-critical systems, fails to meet RPO for critical systems
- "Everything is Tier 1 critical" → Unsustainable redundancy costs, no prioritization
- "We'll restore whatever the business asks for first" → No documented recovery sequence, dependencies ignored
- "We haven't tested but backups are running" → False confidence, untested recovery

**With BIA - Evidence-Based BC/DR:**

- Payment database: RPO 1h (hourly backups) because CHF 50K/hour impact
- Dev environment: RPO 7 days (weekly backup) because CHF 500/day impact
- E-commerce site: RTO 1h (hot standby) because CHF 100K/hour revenue loss
- Internal wiki: RTO 7 days (restore from backup) because minimal business impact

**Regulatory Requirements for BIA:**

Per ISMS-POL-00 (Regulatory Applicability Framework):

**Tier 1 - Mandatory:**

- **ISO 27001:2022 A.5.30** - "ICT readiness shall be planned...based on business continuity objectives and ICT continuity requirements"
- **Swiss nDSG Art. 8** - "Appropriate technical and organizational measures" requires understanding of what's critical
- **EU GDPR Art. 32** - "Security of processing...taking into account...availability" requires knowing availability requirements

**Tier 2 - Conditional (if applicable):**

- **DORA (EU) Art. 12** - "Financial entities shall conduct business impact analysis to identify critical ICT systems"
- **NIS2 (EU) Art. 21** - "Essential entities shall identify critical ICT systems"
- **FINMA (Swiss Financial)** - "Financial institutions must ensure operational continuity" requires BIA
- **PCI DSS v4.0.1 Req. 12.10** - "Implement business continuity plan including impact analysis"

**Tier 3 - Informational:**

- **ISO 22301:2019** - Comprehensive BIA methodology for business continuity management
- **NIST SP 800-34** - Contingency Planning Guide for Federal Information Systems (BIA section)

## Connection to Three Controls (A.8.13, A.8.14, A.5.30)

This assessment implements the BIA requirements that drive all three BC/DR controls:

### To A.8.13 (Information Backup)

**Policy Section:** ISMS-POL-A.5.30-8.13-14, Section 2.1 (Information Backup Requirements)

**BIA Outputs Used:**

- **RPO requirements** → Backup frequency (RPO 1h = hourly incremental, RPO 24h = daily full)
- **System criticality tier** → Backup retention (Tier 1 = 30 days, Tier 4 = 7 days)
- **Data classification** → Backup encryption requirements

**Implementation Guide:** ISMS-IMP-A.5.30-8.13-14-S2 (Backup Implementation)

**Example Flow:**
```
BIA Result: Payment DB = Tier 1, RPO 1h, Confidential data
    ↓
Backup Implementation:

  - Hourly incremental backups (RPO requirement)
  - 30-day retention (Tier 1 requirement)
  - AES-256 encryption (Confidential data requirement)
  - Quarterly restore testing (Tier 1 requirement)

```

### To A.8.14 (Redundancy of Information Processing Facilities)

**Policy Section:** ISMS-POL-A.5.30-8.13-14, Section 2.2 (Redundancy Requirements)

**BIA Outputs Used:**

- **RTO requirements** → Redundancy architecture (RTO <1h = hot standby, RTO <24h = warm standby)
- **System criticality tier** → SPOF analysis priority (Tier 1 = mandatory, Tier 3 = optional)
- **Dependency map** → Infrastructure redundancy requirements

**Implementation Guide:** ISMS-IMP-A.5.30-8.13-14-S3 (Redundancy Implementation)

**Example Flow:**
```
BIA Result: E-commerce platform = Tier 1, RTO 1h, depends on Payment Gateway
    ↓
Redundancy Implementation:

  - Active-active load balanced (RTO requirement)
  - Multi-AZ deployment (geographic redundancy)
  - Payment Gateway also redundant (dependency requirement)
  - Automated failover (RTO <1h requirement)

```

### To A.5.30 (ICT Readiness for Business Continuity)

**Policy Section:** ISMS-POL-A.5.30-8.13-14, Section 2.3 (ICT BC Readiness Requirements)

**BIA Outputs Used:**

- **System criticality classification** → Recovery priorities and testing frequency
- **RPO/RTO requirements** → ICT continuity plan objectives
- **Dependency map** → Recovery sequence in DR scenarios
- **Gap analysis** → BC/DR program priorities and budget justification

**Implementation Guide:** ISMS-IMP-A.5.30-8.13-14-S4 (Recovery Testing) and S5 (BC/DR Assessment)

**Example Flow:**
```
BIA Result: Critical systems (Tier 1) identified, dependencies mapped
    ↓
ICT BC Readiness:

  - DR site requirements (must support Tier 1 systems)
  - Recovery runbooks (step-by-step procedures with dependencies)
  - Testing schedule (Tier 1 quarterly, Tier 2 semi-annually)
  - Crisis management (activation criteria, escalation procedures)

```

## Who Participates in BIA

**BIA is NOT an IT-only exercise.** Successful BIA requires cross-functional participation:

| Role | Responsibility in BIA | Time Commitment |
|------|----------------------|-----------------|
| **BC/DR Coordinator** | Process owner, coordinates all BIA activities, consolidates data, prepares documentation | 80-120 hours over 4-6 weeks |
| **Business Process Owners** | Define business processes, quantify impact of disruption, validate findings | 2-4 hours per process (interview + review) |
| **System Owners** | Document system dependencies, estimate recovery capabilities, validate technical feasibility | 2-3 hours per system |
| **IT Management** | Validate technical feasibility, resource availability, cost estimates | 8-12 hours (review sessions) |
| **Executive Management** | Approve criticality classifications, approve budget for gap remediation | 2-4 hours (final approval meeting) |
| **Finance/Accounting** | Provide revenue data, calculate financial impact, validate cost estimates | 4-6 hours (data provision + review) |
| **Legal/Compliance** | Identify regulatory requirements, contractual obligations, legal liabilities | 2-4 hours (regulatory impact assessment) |
| **Risk Management** | Interpret impact findings, risk scoring, integration with risk register | 4-6 hours (risk assessment integration) |

**Total Organizational Effort:** 100-150 person-hours for typical SME (50-100 systems)

## Time Estimate

**BIA Timeline:**

| Phase | Duration | Activities |
|-------|----------|-----------|
| **Week 1: Planning** | 5 days | Team assembly, scope definition, stakeholder scheduling |
| **Week 2-3: Data Collection** | 10 days | Business process interviews, system inventory, dependency mapping |
| **Week 4: Analysis** | 5 days | Impact scoring, RPO/RTO determination, criticality classification |
| **Week 5: Gap Analysis** | 3 days | Compare requirements vs. current capabilities, prioritize gaps |
| **Week 6: Approval** | 5 days | Executive presentation, feedback incorporation, final approval |

**Total Duration:** 4-6 weeks (first-time BIA)

**Recurring BIA:** 2-3 weeks annually (with established baseline and processes)

**Triggers for Interim BIA Updates:**

- New critical business service launch
- Major system changes (platform migration, technology refresh)
- Organizational changes (acquisition, divestiture, restructuring)
- Post-incident lessons learned (major outage revealed incorrect criticality)
- Regulatory changes affecting availability requirements

## Integration with Other ISMS Processes

**BIA Consumes Data From:**

- **A.5.9 (Asset Inventory)** - System inventory, asset classifications
- **Clause 6.1 (Risk Assessment)** - Existing risk assessments, threat landscape
- **A.5.19-23 (Supplier Management)** - Critical supplier dependencies, SLAs
- **Business Strategy Documents** - Revenue models, customer contracts, regulatory obligations

**BIA Produces Data For:**

- **A.8.13 (Backup Implementation)** - RPO requirements, retention policies
- **A.8.14 (Redundancy Implementation)** - RTO requirements, SPOF analysis
- **A.5.30 (ICT BC Plans)** - Recovery priorities, testing schedules
- **Clause 6.1 (Risk Assessment)** - BC/DR risks, impact ratings
- **Budget Planning** - Gap remediation costs, BC/DR investment justification

**BIA Updates Asset Inventory With:**

- System criticality classification (Tier 1-4)
- Business process dependencies
- RPO/RTO requirements
- Recovery priorities

**Example Integration:**
```
Asset Inventory (A.5.9):
  System: Payment Gateway
  Owner: IT Operations
  [After BIA:]
  Criticality: Tier 1
  RPO: 1 hour
  RTO: 1 hour
  Supports: Order Processing (Critical Business Process)
  
Risk Register (Clause 6.1):
  [After BIA:]
  Risk: Payment Gateway Failure
  Impact: CRITICAL (based on BIA - CHF 50K/hour revenue loss)
  Likelihood: Medium
  Mitigation: Hot standby redundancy (per A.8.14)
```

---

# Prerequisites

## Information Required

**Before Starting BIA, Gather:**

**Business Information:**

- [ ] Organizational chart with all business units and departments
- [ ] Business process inventory (even if informal - list what the business does)
- [ ] Revenue breakdown by product/service line
- [ ] Customer Service Level Agreements (SLAs) with availability commitments
- [ ] Regulatory compliance obligations (licenses, reporting requirements)
- [ ] Contractual penalties for service unavailability
- [ ] Operating hours (24/7, business hours only, regional variations)
- [ ] Peak periods and seasonal variations

**Financial Information:**

- [ ] Annual revenue (total and by business line)
- [ ] Revenue per hour/day (total and by revenue stream)
- [ ] Operating costs breakdown
- [ ] Penalty clauses in customer contracts (SLA breach costs)
- [ ] Insurance coverage for business interruption
- [ ] Regulatory fine schedules (GDPR, sector-specific)

**Technical Information:**

- [ ] Complete IT asset inventory (from A.5.9 if available)
  - Applications (custom, COTS, SaaS)
  - Databases (production, staging, dev)
  - Infrastructure (servers, storage, network)
  - Cloud services (IaaS, PaaS, SaaS)
- [ ] System architecture diagrams
- [ ] Network topology diagrams
- [ ] Data flow diagrams
- [ ] Integration/API dependencies
- [ ] Supplier/third-party dependencies
- [ ] Current backup configurations
- [ ] Current redundancy implementations

**Existing Documentation:**

- [ ] Previous BIA (if any)
- [ ] DR plans (if any)
- [ ] Incident history (past outages, impact, duration)
- [ ] Security risk assessments
- [ ] Business continuity plans

**Swiss/EU Context-Specific:**

- [ ] nDSG compliance obligations (Swiss data protection requirements)
- [ ] GDPR applicability (processing EU personal data?)
- [ ] DORA applicability (financial entity? ICT service provider to financial entities?)
- [ ] NIS2 applicability (essential or important entity in EU?)
- [ ] FINMA applicability (Swiss financial institution?)
- [ ] Sector-specific regulations

## Stakeholder Availability

**Schedule BIA Sessions With:**

**Executive Management:**

- Purpose: BIA kickoff (set expectations), final approval
- Duration: 1-2 hours each
- When: Week 1 (kickoff), Week 6 (approval)

**Business Unit Heads:**

- Purpose: Business process impact assessment
- Duration: 60-90 minutes per business unit
- When: Week 2-3
- Format: Structured interview using BIA worksheet

**System Owners (IT/Operations):**

- Purpose: System dependency mapping, technical capability assessment
- Duration: 30-45 minutes per system
- When: Week 2-4
- Format: Technical interview + diagram review

**Finance/Accounting:**

- Purpose: Validate revenue impacts, provide financial data
- Duration: 2 hours
- When: Week 2 (data provision), Week 4 (validation)

**Legal/Compliance:**

- Purpose: Regulatory requirements, contractual obligations
- Duration: 2 hours
- When: Week 2
- Format: Structured review of regulations and contracts

**Pro Tip:** Schedule all interviews in advance during planning week. No-shows delay entire BIA.

## Tools Needed

**BIA Assessment Workbook (Excel):**

- Provided in PART II of this document
- Template with 5 worksheets
- Pre-configured formulas, validations, conditional formatting
- **Location:** [Define location for your organization - SharePoint, shared drive, etc.]

**Dependency Mapping Tool:**

- Visual diagramming tool for system dependencies
- Options: Microsoft Visio, Lucidchart, draw.io (free), Miro
- Purpose: Create visual dependency maps showing system relationships

**Data Classification Scheme:**

- Use [Organization]'s existing data classification (typically):
  - **Restricted** - Highly confidential, significant impact if disclosed
  - **Confidential** - Internal use only, moderate impact if disclosed
  - **Internal** - Internal use, low impact if disclosed
  - **Public** - No confidentiality requirement

**Impact Scoring Framework:**

- Provided in Section 4 of this guide
- Swiss context-specific (CHF-based financial impacts)
- Calibrated for SME to mid-market enterprises

**Interview Templates:**

- Business Process Owner Interview Questions
- System Owner Technical Interview Questions
- Provided as part of BIA Workbook (documentation in PART II)

---

# BIA Methodology (10-Step Process)

## High-Level BIA Process

```
┌─────────────────────────────────────────────────────────┐
│              BIA PROCESS WORKFLOW                       │
│                                                         │
│  STEP 1: IDENTIFY Business Processes                   │
│     ↓                                                   │
│  STEP 2: MAP Processes to ICT Systems                  │
│     ↓                                                   │
│  STEP 3: ANALYZE Impact of Disruption                  │
│     ↓                                                   │
│  STEP 4: QUANTIFY Impact (Financial/Ops/Reg/Rep)       │
│     ↓                                                   │
│  STEP 5: DETERMINE Maximum Tolerable Downtime (MTD)    │
│     ↓                                                   │
│  STEP 6: ESTABLISH RPO & RTO Requirements              │
│     ↓                                                   │
│  STEP 7: CLASSIFY System Criticality (Tier 1-4)        │
│     ↓                                                   │
│  STEP 8: MAP Dependencies                              │
│     ↓                                                   │
│  STEP 9: IDENTIFY Gaps & Risks                         │
│     ↓                                                   │
│  STEP 10: APPROVE & DOCUMENT Findings                  │
└─────────────────────────────────────────────────────────┘
```

Each step builds on the previous. Do not skip steps.

## STEP 1: Identify Business Processes

**Objective:** Document ALL business processes and functions performed by [Organization].

**Duration:** Week 1 (planning) + Week 2 (data collection)

**Activities:**

1. **Review Organizational Structure**

   - Identify all business units, departments, functions
   - List each unit's primary responsibilities
   - Example for Swiss SME manufacturing company:
     - Sales & Marketing
     - Customer Service
     - Manufacturing/Production
     - Quality Assurance
     - Supply Chain/Procurement
     - Finance & Accounting
     - Human Resources
     - IT Operations

2. **Interview Business Unit Heads**

   - Use structured interview template
   - Key questions:
     - "What are the core processes your unit performs?"
     - "Which processes are critical to the organization's mission?"
     - "Which processes generate revenue directly?"
     - "Which processes support regulatory compliance?"
     - "What are the inputs and outputs of each process?"

3. **Categorize Business Processes**

   - **Revenue-Generating:** Directly generate revenue
     - Examples: Order processing, e-commerce sales, customer onboarding
   - **Operational:** Support day-to-day operations
     - Examples: Inventory management, production control, quality testing
   - **Support:** Enable other processes to function
     - Examples: Payroll, IT infrastructure, facilities management
   - **Compliance:** Required for regulatory/legal obligations
     - Examples: Financial reporting, safety audits, data protection

4. **Document in BIA Workbook - Sheet 1: Business Process Inventory**

   - Process ID (auto-generated: BP-001, BP-002...)
   - Process Name
   - Business Unit
   - Process Owner (Name + Title)
   - Process Description (brief - 1-2 sentences)
   - Process Category (Revenue/Operational/Support/Compliance)
   - Annual Revenue Impact (CHF - if applicable)

**Deliverable:** Complete list of business processes

**Example Output (Swiss Manufacturing SME):**

| Process ID | Process Name | Business Unit | Owner | Category | Annual Revenue Impact |
|-----------|-------------|---------------|-------|----------|---------------------|
| BP-001 | Customer Order Processing | Sales | Head of Sales | Revenue | CHF 25M |
| BP-002 | E-commerce Sales | Marketing | CMO | Revenue | CHF 15M |
| BP-003 | Production Planning | Manufacturing | Production Manager | Operational | N/A |
| BP-004 | Financial Reporting | Finance | CFO | Compliance | N/A |
| BP-005 | Payroll Processing | HR | HR Director | Support | N/A |

**Quality Check:**

- ✓ All business units represented
- ✓ Process owners identified and contactable
- ✓ Revenue totals match organizational revenue
- ✓ Compliance processes identified

## STEP 2: Map Processes to ICT Systems

**Objective:** Identify which ICT systems support each business process.

**Duration:** Week 2-3

**Critical Insight:** Most business processes depend on MULTIPLE ICT systems. E-commerce isn't just "the website" - it's web server + database + payment gateway + email + CRM + inventory system.

**Activities:**

1. **For Each Business Process, Identify Supporting ICT Systems**

   - Primary systems (process cannot function without them)
   - Supporting systems (process degraded without them)
   - Integration points (APIs, data feeds, file transfers)

2. **Classify System Relationship**

   - **Primary:** Process cannot function AT ALL without this system
   - **Supporting:** Process can limp along temporarily without this system
   - **Enhancement:** Process can function but with reduced efficiency/quality

3. **Document in BIA Workbook - Sheet 2: System-Process Mapping**

   - System ID (auto-generated: SYS-001, SYS-002...)
   - System Name
   - System Owner
   - System Type (Application/Database/Infrastructure/Cloud Service)
   - Deployment Model (On-Premises/Cloud/Hybrid)
   - Supporting Processes (list BP-IDs)
   - Relationship (Primary/Supporting/Enhancement)
   - Data Classification (Public/Internal/Confidential/Restricted)
   - Vendor/Provider (if applicable)

**Example Mapping (E-commerce Sales Process):**

**Business Process:** BP-002 (E-commerce Sales) - Annual Revenue CHF 15M

**Supporting ICT Systems:**

| System ID | System Name | Type | Deployment | Relationship | Data Classification |
|-----------|------------|------|------------|--------------|-------------------|
| SYS-010 | E-commerce Website | Application | Cloud (Azure App Service) | Primary | Public/Confidential |
| SYS-011 | E-commerce Database | Database | Cloud (Azure SQL) | Primary | Confidential |
| SYS-015 | Payment Gateway | SaaS | Cloud (Stripe) | Primary | Restricted |
| SYS-020 | CRM System | SaaS | Cloud (Salesforce) | Supporting | Confidential |
| SYS-025 | Email Service | SaaS | Cloud (Microsoft 365) | Supporting | Internal |
| SYS-030 | Inventory System | Application | On-Premises | Supporting | Internal |

**Analysis:**

- If SYS-010 (website) fails → E-commerce sales stop immediately (CHF 15M/year ÷ 8,760 hours = CHF 1,712/hour loss)
- If SYS-011 (database) fails → Website displays errors, no sales possible
- If SYS-015 (payment gateway) fails → Customers cannot complete purchase, no revenue
- If SYS-020 (CRM) fails → New leads not captured but existing orders can process (degraded)
- If SYS-030 (inventory) fails → Cannot verify stock availability but can take orders (degraded)

4. **Identify Cross-Process Dependencies**

   - Some systems support multiple business processes
   - Example: Email system supports sales, customer service, HR, operations
   - Failure of shared system impacts multiple processes simultaneously

**Example (Shared Infrastructure):**

| System ID | System Name | Supporting Processes | Impact if Failed |
|-----------|------------|---------------------|------------------|
| SYS-050 | Network Infrastructure | ALL PROCESSES | Complete operational shutdown |
| SYS-051 | Active Directory | Most IT-dependent processes | Authentication failure, no system access |
| SYS-025 | Email (Microsoft 365) | Sales, Customer Service, HR, Procurement | Communication breakdown across organization |

**Deliverable:** Complete system inventory with process mappings

**Quality Check:**

- ✓ All critical business processes have at least one supporting system identified
- ✓ System types classified (Application/Database/Infrastructure/Cloud)
- ✓ Data classification assigned (drives backup encryption requirements)
- ✓ Vendor/provider documented (for supplier BC/DR assessment per A.5.19-23)
- ✓ Primary vs. Supporting relationship clear

## STEP 3: Analyze Impact of Disruption

**Objective:** For each business process, determine "what happens if this is unavailable?"

**Duration:** Week 2-3 (concurrent with Step 2)

**Impact Dimensions:**

All disruptions affect the organization across FOUR dimensions:

### Financial Impact

**Revenue Loss:**

- Direct revenue loss (sales not made)
- Delayed revenue (sales delayed, eventually recovered)
- Lost customers (permanent customer defection)
- Contractual penalties (SLA breach penalties)

**Additional Costs:**

- Recovery costs (overtime, emergency procurement)
- Workaround costs (manual operations, temporary solutions)
- Opportunity costs (staff focused on recovery instead of normal work)

**Swiss Context - Financial Impact Questions:**

- "What is the hourly revenue for this process?" (Annual Revenue ÷ 8,760 hours)
- "Are there penalty clauses if we cannot deliver?" (Contractual SLAs)
- "What are the recovery costs?" (Staff overtime, emergency services)

**Example Calculation (E-commerce Sales):**
```
Annual E-commerce Revenue: CHF 15,000,000
Hourly Revenue = CHF 15,000,000 ÷ 8,760 hours = CHF 1,712/hour

Disruption Duration: 8 hours
Direct Revenue Loss: CHF 1,712 × 8 = CHF 13,696
Recovery Costs (overtime, emergency fixes): CHF 5,000
TOTAL FINANCIAL IMPACT (8 hours): CHF 18,696

Disruption Duration: 24 hours
Direct Revenue Loss: CHF 1,712 × 24 = CHF 41,088
Customer Defection (estimated 5% never return): CHF 750,000 (annual)
Recovery Costs: CHF 15,000
TOTAL FINANCIAL IMPACT (24 hours): CHF 806,088
```

### Operational Impact

**Process Degradation:**

- Complete shutdown (process cannot function at all)
- Significant degradation (>50% capacity loss)
- Moderate degradation (25-50% capacity loss)
- Minor degradation (<25% capacity loss)

**Cascade Effects:**

- Upstream processes blocked (cannot receive input from failed process)
- Downstream processes blocked (cannot provide output to failed process)
- Staff idle time (employees cannot perform duties)

**Manual Workarounds:**

- Can process continue manually? (Paper forms, phone calls, spreadsheets)
- How long is manual operation sustainable? (Hours, days, weeks)
- What is the efficiency loss? (Manual = 10% of normal capacity)

**Example Analysis (Order Processing System Failure):**
```
Normal Capacity: 500 orders/day
With System Down:

  - Manual Order Entry (phone + fax): 50 orders/day (10% capacity)
  - Manual operation sustainable: 2-3 days maximum
  - After 3 days: Order backlog unmanageable, customers cancel

Operational Impact: SIGNIFICANT (90% capacity loss)
```

### Regulatory/Legal Impact

**Regulatory Violations:**

- Reporting deadlines missed (financial reporting, tax filings)
- Compliance requirements breached (data protection, safety reporting)
- License requirements not met (regulatory licenses require system availability)

**Legal Liabilities:**

- Contract breach (SLA violations, delivery failures)
- Statutory obligations (employment law, labor reporting)
- Legal discovery obligations (inability to produce required records)

**Fines and Penalties:**

**Swiss nDSG:**

- Data breach notification: 72 hours to FDPIC (Federal Data Protection and Information Commissioner)
- Failure to implement appropriate technical measures: Up to CHF 250,000 fine (individuals)

**EU GDPR (if processing EU personal data):**

- Data breach notification: 72 hours to supervisory authority
- Security of processing violation: Up to €20M or 4% of global annual turnover (whichever is higher)
- Example: CHF 50M revenue company → Maximum fine €2M (~CHF 1.9M)

**DORA (if EU financial entity):**

- ICT operational resilience failure: Penalties up to €10M or 2% of total annual worldwide turnover
- Major incident reporting failure: 4 hours initial, 72 hours intermediate report

**NIS2 (if essential/important entity in EU):**

- Cybersecurity risk management failure: Up to €10M or 2% of global turnover (essential), €7M or 1.4% (important)
- Incident reporting failure (24h/72h deadlines)

**PCI DSS v4.0.1 (if processing payment cards):**

- Non-compliance: Loss of ability to process card payments
- Data breach: Card brand fines ($5,000-$100,000 per month), card reissuance costs
- Merchant account termination

**Example Regulatory Impact Assessment:**
```
Process: Customer Data Management System
Disruption Impact:

  - GDPR Art. 15 (Right of Access): Cannot respond to subject access requests
  - Deadline: 30 days (per GDPR)
  - Impact if >30 days: Potential supervisory authority complaint
  - Swiss nDSG equivalent: Right to information (Art. 25)
  
  - GDPR Art. 17 (Right to Erasure): Cannot process deletion requests
  - Deadline: 30 days (in most cases)
  - Impact: Ongoing processing of data subject requested for deletion
  
Regulatory Impact: HIGH (compliance violation, potential supervisory action)
```

### Reputational Impact

**Brand Damage:**

- Negative media coverage
- Social media backlash
- Customer trust erosion
- Competitive disadvantage ("Company X can't even keep their website up")

**Customer Defection:**

- Immediate (during outage - customers go to competitor)
- Delayed (customers lose confidence, switch over time)
- Permanent (brand association with unreliability)

**Stakeholder Confidence:**

- Investor confidence (especially for public companies or those seeking investment)
- Partner/supplier confidence (business relationships affected)
- Employee morale (reputational damage affects recruitment/retention)

**Reputational Impact Scale:**

| Impact Level | Description | Example |
|--------------|-------------|---------|
| **Critical** | National/international media coverage, viral social media, mass customer defection | Major bank's online banking down for 24+ hours |
| **High** | Regional media coverage, significant social media discussion, notable customer complaints | E-commerce site down during Black Friday |
| **Medium** | Limited media coverage, moderate customer complaints, internal only | Internal HR system down for 1 day |
| **Low** | Minimal visibility, internal impact only | Development environment down |

**Example Reputational Assessment (E-commerce Platform):**
```
Scenario: E-commerce platform down for 12 hours during business hours

Immediate Impact:

  - Customers cannot place orders → Frustration, social media complaints
  - Competitor websites available → Direct customer loss
  - "Company X website is always broken" sentiment

24-Hour Impact:

  - Regional news coverage (if significant company)
  - Twitter/LinkedIn discussion
  - Customer service overwhelmed with complaints

Long-Term Impact:

  - Brand association with unreliability
  - Estimated 2-5% customer defection to competitors
  - Recruitment impact (talented employees prefer reliable companies)

Reputational Impact: HIGH
```

---

## STEP 4: QUANTIFY Impact (Financial/Ops/Reg/Rep)

**Objective:** Score each impact dimension on a 1-5 scale to enable prioritization.

**Duration:** Week 3-4

**Using the Impact Scoring Framework:**

Reference **Section 4: Impact Scoring Methodology** for complete scoring criteria.

**Quick Reference - Impact Scoring (Calibrated for Swiss Context):**

| Score | Financial (CHF/day) | Operational | Regulatory | Reputational |
|-------|-------------------|-------------|------------|--------------|
| **5** | >CHF 500K/day | Complete shutdown | Major fines/license loss | Severe brand damage |
| **4** | CHF 100K-500K/day | Significant degradation (>50%) | Compliance violation, supervisory action | Major negative publicity |
| **3** | CHF 25K-100K/day | Moderate degradation (25-50%) | Minor compliance issue | Moderate publicity |
| **2** | CHF 5K-25K/day | Minor degradation (<25%) | Potential compliance issue | Limited publicity |
| **1** | <CHF 5K/day | Negligible impact | No compliance issue | No publicity |

**Process:**

1. **For Each System, Score All Four Dimensions**

   - Financial Impact: 1-5
   - Operational Impact: 1-5
   - Regulatory Impact: 1-5
   - Reputational Impact: 1-5

2. **Calculate Composite Impact Score**
   ```
   Composite Impact Score = MAX(Financial, Operational, Regulatory, Reputational)
   ```
   
   **Rationale:** Single high-impact dimension makes system critical. Example: Dev environment might have low financial/operational/reputational impact (1-2), but if it processes production data subject to GDPR, regulatory impact could be 4-5, making overall criticality HIGH.

3. **Document in BIA Workbook - Sheet 3: Impact Assessment**

   - System Name (from Sheet 2)
   - Financial Score (1-5)
   - Financial Impact (CHF/day - calculated)
   - Operational Score (1-5)
   - Operational Impact (description)
   - Regulatory Score (1-5)
   - Regulatory Impact (specific regulations affected)
   - Reputational Score (1-5)
   - Reputational Impact (description)
   - **Composite Score (calculated = MAX)**
   - Impact Rationale (justification for scores)

**Example Impact Assessment:**

**System:** SYS-010 (E-commerce Website)

| Dimension | Score | Impact Description | Rationale |
|-----------|-------|-------------------|-----------|
| **Financial** | **5** | CHF 41,088/day (CHF 1,712/hour × 24h) | Direct revenue loss, e-commerce contributes CHF 15M/year |
| **Operational** | **5** | Complete shutdown of e-commerce sales | Cannot take orders at all, no workaround available |
| **Regulatory** | **4** | GDPR data processing interruption, customer complaint risk | Customer data in database, inability to process subject rights requests |
| **Reputational** | **4** | High social media visibility, customer complaints, competitor advantage | Brand known for e-commerce, downtime highly visible |
| **COMPOSITE** | **5** | MAX(5,5,4,4) = 5 | CRITICAL system |

**Quality Check:**

- ✓ All systems scored on all four dimensions
- ✓ Financial impact calculated based on actual revenue data
- ✓ Regulatory impact considers [Organization]'s specific regulatory obligations
- ✓ Rationale documented for audit trail
- ✓ Cross-validation: Revenue totals across systems don't exceed organizational revenue

## STEP 5: DETERMINE Maximum Tolerable Downtime (MTD)

**Objective:** Establish the absolute maximum time a system can be unavailable before causing irreparable harm.

**Duration:** Week 3

**Key Concept - MTD vs. RTO:**

- **MTD (Maximum Tolerable Downtime):** The absolute survival limit. Beyond this point, the organization suffers irreparable harm (e.g., contract termination, regulatory license loss, bankruptcy).
- **RTO (Recovery Time Objective):** The target recovery time with a safety margin. RTO should be 30-50% of MTD to provide buffer.

**Example:**
```
Payment Processing System:
  MTD = 8 hours (Beyond 8h: Regulatory reporting deadline missed, banking license implications)
  RTO = 4 hours (50% of MTD - provides 4h safety margin)
```

**MTD Determination Questions:**

1. **"At what point does this disruption cause permanent damage?"**

   - Contract termination (SLA breach so severe customer terminates)
   - Regulatory action (license suspension, mandatory reporting failure)
   - Market share loss (customers permanently switch to competitors)
   - Business failure (cannot continue operations)

2. **"What are the external deadlines driving recovery?"**

   - Regulatory reporting deadlines
   - Customer contract SLA commitments
   - Payment processing windows (payroll, vendor payments)
   - Market events (stock exchange trading, critical business periods)

3. **"How long can manual workarounds sustain the process?"**

   - If manual operation possible: MTD = Longer (days to weeks)
   - If no manual operation: MTD = Shorter (hours to days)

**MTD Examples (Swiss Business Context):**

**Tier 1 Systems (Critical) - MTD ≤ 8 hours:**

| System | MTD | Justification |
|--------|-----|---------------|
| **Payment Processing** | 4 hours | Beyond 4h: Daily settlement deadlines missed, regulatory reporting late, banking partner issues |
| **E-commerce Platform** | 8 hours | Beyond 8h: Customer SLA breaches (99.9% uptime = 8.76h/year max downtime), significant revenue loss, brand damage |
| **Manufacturing Control System** | 6 hours | Beyond 6h: Production lines cold, restart costs CHF 50K, delivery commitments missed |

**Tier 2 Systems (Important) - MTD ≤ 48 hours:**

| System | MTD | Justification |
|--------|-----|---------------|
| **CRM System** | 24 hours | Beyond 24h: Sales team cannot function, lead response SLA breached, manual workarounds exhausted |
| **ERP System** | 48 hours | Beyond 48h: Order processing backlog unmanageable, inventory visibility lost, accounting delayed |
| **Email (Microsoft 365)** | 24 hours | Beyond 24h: Business communication severely impaired, customer response impossible |

**Document in BIA Workbook - Sheet 4: MTD, RPO, RTO**

- System Name
- MTD (dropdown: 1h / 4h / 8h / 24h / 48h / 7 days / 30 days)
- MTD Justification (business rationale)
- [RPO and RTO covered in Step 6]

**Quality Check:**

- ✓ MTD reflects actual business tolerance, not IT convenience
- ✓ MTD justified with specific business consequences
- ✓ MTD considers regulatory deadlines, contractual SLAs
- ✓ MTD reviewed with business process owners, not determined by IT alone

## STEP 6: ESTABLISH RPO & RTO Requirements

**Objective:** Define business-justified Recovery Point Objective (data loss tolerance) and Recovery Time Objective (recovery time target).

**Duration:** Week 3-4

**Critical Principle:** RPO and RTO are **business-driven, not IT-driven**. The business defines how much data loss and downtime is tolerable based on impact. IT then implements solutions to meet those requirements.

### RPO (Recovery Point Objective) - "How much data loss is tolerable?"

**RPO Determination Questions:**

1. **"Can lost data be recreated?"**

   - Yes, easily → Longer RPO acceptable (backup less frequently)
   - Yes, with effort → Moderate RPO (balance effort vs. backup cost)
   - No, cannot recreate → Short RPO (backup frequently)

2. **"What is the cost of data re-creation?"**

   - Example: Lost customer orders
     - Each order = 15 minutes manual re-entry
     - 100 orders/hour during business hours
     - Re-creation cost for 4 hours lost data = 100 orders/hr × 4hr × 15min/order = 100 person-hours
     - Cost: CHF 5,000 (at CHF 50/hour labor)
   - If re-creation cost > backup cost → Shorter RPO

3. **"What are regulatory requirements for data integrity?"**

   - Financial transactions: Near-zero data loss (regulatory requirement)
   - Healthcare records: Minimal data loss (patient safety)
   - Manufacturing quality data: Low data loss (traceability requirements)

4. **"What is the transaction frequency?"**

   - High transaction volume (payment processing: 1000s/hour) → Short RPO
   - Low transaction volume (monthly reports) → Longer RPO

**RPO Framework (Business-Driven):**

| Data Loss Tolerance | RPO Target | Typical Business Drivers | Technical Implementation (A.8.13) |
|---------------------|------------|-------------------------|----------------------------------|
| **Zero Tolerance** | **Near-zero** (continuous replication) | Financial transactions, healthcare records, safety-critical | Synchronous replication, transaction log backups every 15min |
| **Minimal Tolerance** | **≤ 1 hour** | E-commerce, real-time processing, payment systems | Hourly incremental backup + transaction logs |
| **Limited Tolerance** | **≤ 4 hours** | CRM, operational databases, customer service | 4-hourly incremental backups |
| **Moderate Tolerance** | **≤ 24 hours** | Document management, collaboration, non-critical databases | Daily full backup + incremental |
| **High Tolerance** | **≤ 7 days** | Archived data, development environments, test systems | Weekly full backups |

**RPO Examples (Swiss Business Context):**

| System | RPO | Justification |
|--------|-----|---------------|
| **Payment Database** | **1 hour** | High transaction volume (500/hour peak), each transaction ~CHF 100 average, 1h data loss = CHF 50K revenue impact, cannot recreate payment authorizations |
| **E-commerce Database** | **4 hours** | Moderate transaction volume (100 orders/hour), 4h data loss = 400 orders to manually re-enter (100 person-hours = CHF 5K cost), acceptable vs. hourly backup cost |
| **CRM System** | **24 hours** | Low update frequency (updates throughout day but not time-critical), 24h data loss = ~50 customer interactions to re-enter (5 person-hours = CHF 250 cost) |
| **File Server (Internal Docs)** | **24 hours** | Document changes throughout day, most documents version-controlled elsewhere (SharePoint, Git), 24h acceptable |
| **Development Environment** | **7 days** | Code committed to Git (external), database schema changes infrequent, dev work can be recreated, 7 days acceptable |

### RTO (Recovery Time Objective) - "How fast must the system be recovered?"

**RTO Determination - Business-Driven:**

**Formula:** RTO = MTD × Safety Factor (typically 0.3 to 0.5)

**Rationale:** RTO provides safety margin below MTD. If MTD = 8 hours (absolute limit), RTO = 4 hours (50% safety margin) provides 4 hours of buffer for unexpected complications.

**RTO Framework (Business-Driven):**

| Downtime Tolerance | RTO Target | Typical Business Drivers | Technical Implementation (A.8.14) |
|--------------------|------------|-------------------------|----------------------------------|
| **Near-Zero** | **≤ 15 minutes** | Critical revenue systems, customer transactions, safety-critical | Active-active load balanced, automated failover |
| **Minimal** | **≤ 1 hour** | Payment processing, e-commerce, real-time operations | Hot standby, automatic failover, synchronized data |
| **Limited** | **≤ 4 hours** | CRM, ERP, customer support, operational systems | Warm standby, manual failover, recent data sync |
| **Moderate** | **≤ 24 hours** | Email, collaboration, internal applications | Cold standby or restore from backup |
| **Relaxed** | **≤ 7 days** | Supporting systems, development tools, non-critical infrastructure | Rebuild from backup, no redundancy |

**RTO Examples (Aligned with RPO Above):**

| System | MTD | RTO | RTO Justification | Technical Implementation |
|--------|-----|-----|------------------|-------------------------|
| **Payment Database** | 4h | **1 hour** | MTD 4h × 50% safety = 2h, but customer SLA requires 1h RTO | Hot standby (Azure SQL Always On), automated failover |
| **E-commerce Platform** | 8h | **4 hours** | MTD 8h × 50% safety = 4h, provides buffer for complications | Warm standby (pre-provisioned Azure VMs, manual failover) |
| **CRM System** | 24h | **8 hours** | MTD 24h × 30% safety = 7.2h, rounded to 8h for practicality | Restore from backup (daily backup, restore tested at 6h) |
| **File Server** | 7 days | **24 hours** | MTD 7 days × 14% = 24h, minimal impact if takes full day | Restore from backup (daily backup) |
| **Dev Environment** | 30 days | **7 days** | MTD 30 days × 23% = 7 days, acceptable for non-production | Rebuild from backup (weekly backup) |

**Critical Validation: RPO ≤ RTO Always**

**Why:** You cannot recover to a point in time (RPO) that's after the recovery completes (RTO). If RTO = 4 hours but RPO = 8 hours, you're saying "We'll recover the system in 4 hours, but the data will be 8 hours old" - which means the system was actually unavailable for 12 hours total (4h recovery + 8h of missing data).

**Correct Relationship:** RPO ≤ RTO

**Example Validation:**
```
Payment Database:
  RPO: 1 hour (backup every hour)
  RTO: 1 hour (recover in 1 hour)
  Validation: RPO (1h) ≤ RTO (1h) ✓ PASS

Incorrect Example:
  RPO: 8 hours
  RTO: 4 hours
  Validation: RPO (8h) > RTO (4h) ✗ FAIL
  Problem: System recovered in 4h but data 8h old = effective 12h outage
```

**Document in BIA Workbook - Sheet 4: MTD, RPO, RTO**

- System Name
- MTD (from Step 5)
- **RPO** (dropdown: near-zero / 1h / 4h / 24h / 7 days)
- **RPO Rationale** (business justification)
- **RTO** (dropdown: 15min / 1h / 4h / 24h / 7 days)
- **RTO Rationale** (business justification)
- **Safety Margin %** (calculated: (MTD - RTO) / MTD × 100%)
- **Validation: RPO ≤ RTO** (formula: IF(RPO_hours <= RTO_hours, "PASS", "FAIL"))

**Conditional Formatting:**

- Safety Margin < 30%: Red (insufficient buffer)
- Safety Margin 30-50%: Green (good buffer)
- RPO > RTO: Red cell + "FAIL" (invalid configuration)

**Quality Check:**

- ✓ All systems have RPO and RTO defined
- ✓ RPO ≤ RTO validation passes for all systems
- ✓ Safety margin (MTD - RTO) is adequate (30%+ preferred)
- ✓ Business rationale documented for each RPO/RTO
- ✓ RPO/RTO reviewed with business process owners

## STEP 7: CLASSIFY System Criticality (Tier 1-4)

**Objective:** Assign each system to a criticality tier based on impact scores and RPO/RTO requirements.

**Duration:** Week 4

**Criticality Tier Framework:**

Per ISMS-POL-A.5.30-8.13-14, [Organization] classifies all ICT systems into four criticality tiers. Each tier has distinct BC/DR requirements.

### Tier 1: Critical Systems

**Criteria (ANY ONE triggers Tier 1):**

- RTO ≤ 4 hours
- RPO ≤ 4 hours
- Composite Impact Score = 5
- Financial impact > CHF 100K/day
- Regulatory compliance-critical (failure = major fines or license loss)
- Direct customer-facing revenue system
- Safety-critical (if applicable to [Organization])

**BC/DR Requirements:**

- **Backup:** Mandatory backup, frequency aligned with RPO (hourly minimum for RPO ≤ 4h)
- **Redundancy:** Mandatory redundancy (hot standby or active-active)
- **Geographic Redundancy:** Required for disaster scenarios (multi-AZ, multi-region, or hybrid cloud-on-prem)
- **Testing:** Quarterly recovery testing (backup restore + failover)
- **Monitoring:** 24/7 monitoring, automated alerts
- **Approval:** Executive management approval required for criticality classification and any exceptions

**Typical Examples:**

- Payment processing systems
- E-commerce platforms
- Core banking systems (if financial institution)
- Manufacturing control systems (if manufacturing)

### Tier 2: Important Systems

**Criteria:**

- RTO ≤ 24 hours
- RPO ≤ 24 hours
- Composite Impact Score = 4
- Financial impact CHF 25K-100K/day
- Significant operational impact (business degraded without system)
- Customer service systems (non-revenue but customer-facing)

**BC/DR Requirements:**

- **Backup:** Mandatory backup, frequency aligned with RPO (daily minimum for RPO ≤ 24h)
- **Redundancy:** Required (warm standby or N+1 clustering acceptable)
- **Geographic Redundancy:** Recommended but not mandatory
- **Testing:** Semi-annual recovery testing (backup restore + failover where applicable)
- **Monitoring:** Business hours monitoring with on-call escalation
- **Approval:** CISO approval required for exceptions

**Typical Examples:**

- CRM systems
- ERP systems
- HR systems (payroll, benefits)
- Email and collaboration platforms (Microsoft 365, Google Workspace)

### Tier 3: Standard Systems

**Criteria:**

- RTO ≤ 7 days
- RPO ≤ 7 days
- Composite Impact Score = 3
- Financial impact < CHF 25K/day
- Supporting systems (not directly operational-critical)
- Internal-facing systems with moderate impact

**BC/DR Requirements:**

- **Backup:** Required (weekly backup acceptable for RPO ≤ 7 days)
- **Redundancy:** Recommended but not mandatory (risk-based decision)
- **Geographic Redundancy:** Not required
- **Testing:** Annual recovery testing (backup restore)
- **Monitoring:** Business hours monitoring
- **Approval:** IT Management approval for exceptions

**Typical Examples:**

- Intranet portals
- Document management systems
- Non-critical file servers

### Tier 4: Low-Criticality Systems

**Criteria:**

- RTO > 7 days
- RPO > 7 days
- Composite Impact Score ≤ 2
- Negligible business impact
- Easily rebuildable systems
- Non-production systems with no business dependency

**BC/DR Requirements:**

- **Backup:** Optional (monthly or on-demand backup acceptable)
- **Redundancy:** Not required
- **Geographic Redundancy:** Not required
- **Testing:** No recovery testing requirement (rebuild acceptable)
- **Monitoring:** Best-effort monitoring
- **Approval:** Risk acceptance documented by system owner

**Typical Examples:**

- Test environments (isolated from production)
- Training systems
- Archived data (no active use)

## Tier Classification Formula (Auto-Calculated in Workbook)

**Excel Formula (in Sheet 5 - System Criticality, Column: Auto_Tier):**

```excel
=IF(OR(RTO_Hours<=4, RPO_Hours<=4, Composite_Impact=5, Financial_Impact_Per_Day>100000), "Tier 1",
  IF(OR(RTO_Hours<=24, RPO_Hours<=24, Composite_Impact=4, AND(Financial_Impact_Per_Day>=25000, Financial_Impact_Per_Day<=100000)), "Tier 2",
    IF(OR(RTO_Hours<=168, RPO_Hours<=168, Composite_Impact=3), "Tier 3", "Tier 4")))
```

**Manual Override:**

- Workbook allows manual tier override with justification
- Final_Tier = Manual_Override (if provided) ELSE Auto_Tier
- All overrides require documented justification and approval

**Example Tier Classifications:**

| System | Composite Impact | RTO | RPO | Financial/Day | Auto Tier | Manual Override | Final Tier | Override Justification |
|--------|-----------------|-----|-----|--------------|-----------|----------------|-----------|---------------------|
| Payment DB | 5 | 1h | 1h | CHF 1.2M | Tier 1 | - | **Tier 1** | - |
| E-commerce | 5 | 4h | 4h | CHF 1.0M | Tier 1 | - | **Tier 1** | - |
| CRM | 4 | 8h | 24h | CHF 50K | Tier 2 | - | **Tier 2** | - |
| Email | 4 | 24h | 24h | CHF 30K | Tier 2 | - | **Tier 2** | - |
| Intranet | 3 | 7 days | 7 days | CHF 5K | Tier 3 | - | **Tier 3** | - |
| Dev Environment | 2 | 7 days | 7 days | CHF 500 | Tier 3 | Tier 4 | **Tier 4** | No production dependency, code in Git, acceptable to rebuild |

**Document in BIA Workbook - Sheet 5: System Criticality**

- System Name (from previous sheets)
- Composite Impact Score (from Sheet 3)
- RTO Requirement (from Sheet 4)
- RPO Requirement (from Sheet 4)
- Financial Impact per Day (from Sheet 3)
- **Auto-Calculated Tier** (formula)
- **Manual Override Tier** (dropdown: Tier 1/2/3/4 or blank)
- **Final Tier** (calculated: IF manual override exists, use it, else use auto tier)
- **Override Justification** (mandatory if manual override)
- **Approved By** (name + title if override)
- **Approval Date** (if override)

**Quality Check:**

- ✓ Auto-tier calculation formula correct
- ✓ All manual overrides have documented justification
- ✓ All Tier 1 overrides approved by executive management
- ✓ All Tier 2 overrides approved by CISO
- ✓ Distribution of tiers is realistic (not "everything is Tier 1")

## STEP 8: MAP Dependencies

**Objective:** Document system interdependencies to determine recovery sequence and identify infrastructure requiring redundancy.

**Duration:** Week 3-4 (concurrent with Steps 6-7)

**Critical Insight:** Systems don't operate in isolation. A Tier 1 application depends on Tier 2 database, Tier 2 infrastructure, Tier 3 network - ALL dependencies must recover BEFORE the primary system.

### Dependency Categories

**1. Application Dependencies**

- Upstream applications (this system consumes data/services from)
- Downstream applications (this system provides data/services to)
- Integration points (APIs, file transfers, message queues)

**Example (E-commerce Platform):**
```
E-commerce Website (SYS-010)
  ↓ Depends on ↓

  - E-commerce Database (SYS-011) - stores product catalog, orders
  - Payment Gateway (SYS-015) - processes payments
  - Inventory System (SYS-030) - checks stock availability
  - CRM System (SYS-020) - customer information
  - Email Service (SYS-025) - order confirmations

```

**2. Infrastructure Dependencies**

- Compute (physical servers, VMs, containers)
- Storage (SAN, NAS, object storage)
- Network (routers, switches, firewalls, load balancers)
- Identity (Active Directory, LDAP, SSO)
- DNS
- Power/Utilities (UPS, generators)

**Example (Any Application):**
```
Any Application
  ↓ Depends on ↓

  - Compute Platform (Azure VMs, AWS EC2, on-prem servers)
  - Network Connectivity (Internet, VPN, internal network)
  - DNS (name resolution)
  - Active Directory (authentication)
  - Storage (database storage, file storage)
  - Power (datacenter power, UPS, generators if on-prem)

```

**3. External Dependencies**

- Cloud providers (AWS, Azure, GCP)
- SaaS platforms (Salesforce, Microsoft 365, etc.)
- Third-party APIs (payment gateways, shipping APIs, etc.)
- ISP/Network providers
- Managed service providers

**Example (Cloud-Dependent Application):**
```
Application Hosted in Azure
  ↓ Depends on ↓

  - Azure Region (West Europe datacenter)
  - Microsoft Entra ID (formerly Azure Active Directory) (authentication)
  - Azure SQL Database (data storage)
  - Internet Connectivity (ISP)
  - Microsoft 365 (email for notifications)

```

### Dependency Mapping Process

**Step 1: For Each Tier 1 and Tier 2 System, Interview System Owner**

Questions:

- "What systems does this system connect to?" (upstream/downstream)
- "What infrastructure is required for this system to function?" (network, storage, compute)
- "What external services does this system use?" (cloud, SaaS, APIs)
- "Who is required to recover this system?" (personnel)

**Step 2: Create Dependency Diagram**

Use Visio, Lucidchart, draw.io, or similar:

- Boxes for systems
- Arrows showing dependencies (A → B means "A depends on B")
- Color-code by criticality tier
- Include infrastructure and external dependencies

**Step 3: Determine Recovery Sequence**

**Rule:** Dependencies must recover BEFORE dependent systems.

**Example Recovery Sequence (E-commerce):**
```
Recovery Order (Sequential):
1. Active Directory (authentication for everything)
2. Network Infrastructure (connectivity)
3. Azure Infrastructure (platform)
4. Azure SQL Database (data)
5. On-premises Database (inventory data)
6. VPN (connect cloud to on-prem)
7. Payment Gateway API (external - verify operational)
8. E-commerce Website (application)
9. Validate end-to-end (customer can place order and payment processes)
```

**Estimated Recovery Time:**
```
Active Directory: 30 min
Network Infrastructure: 15 min
Azure Infrastructure: 15 min (already up, validate connectivity)
Azure SQL: 45 min (restore from backup or failover)
On-prem Database: 60 min (restore from backup)
VPN: 15 min
Payment Gateway: 0 min (external, verify only)
E-commerce Website: 30 min (deploy application, configure)
Validation: 15 min
───────────────────
TOTAL: 225 min = 3.75 hours

RTO Requirement: 4 hours ✓ ACHIEVABLE (with 15 min buffer)
```

**Step 4: Identify Infrastructure Requiring Redundancy**

If a Tier 1 system depends on infrastructure, that infrastructure must ALSO be redundant (otherwise single point of failure).

**Example Analysis:**
```
E-commerce Website (Tier 1) → Requires Active Directory
Question: Is Active Directory redundant?

  - If NO: SPOF - Active Directory failure = E-commerce down
  - Action: Implement AD redundancy (multiple domain controllers)

E-commerce Website (Tier 1) → Requires Network
Question: Is network redundant?

  - If NO: SPOF - Network failure = E-commerce down
  - Action: Implement network redundancy (dual ISP, redundant switches)

```

**Document in BIA Workbook - Sheet 6: Dependency Matrix**

- System Name (primary system)
- Dependency Type (dropdown: Application/Database/Infrastructure/External)
- Dependent System (name of dependency)
- Dependency Criticality (dropdown: Required/Optional)
- Dependency RTO (must be ≤ primary system RTO)
- Recovery Sequence (number: 1, 2, 3... indicating order)
- Notes (additional context)

**Quality Check:**

- ✓ All Tier 1 and Tier 2 systems have dependencies documented
- ✓ Dependency RTO ≤ Primary System RTO (dependencies must recover first)
- ✓ Recovery sequence logical (infrastructure before applications)
- ✓ Required vs. Optional dependencies identified
- ✓ Dependency diagrams created and saved as evidence
- ✓ SPOF identified (single dependencies with no redundancy)

## STEP 9: IDENTIFY Gaps & Risks

**Objective:** Compare BIA requirements (RPO/RTO) with current BC/DR capabilities to identify gaps.

**Duration:** Week 4-5

**Gap Analysis Process:**

**Step 1: For Each System, Assess Current BC/DR Capabilities**

**Current Backup Capability:**

- Is backup configured? (Yes/No)
- Backup frequency? (Hourly/Daily/Weekly/None)
- Last successful backup? (Date/Time)
- Last restore test? (Date/Result)
- Achievable RPO based on current backup = Backup frequency

**Current Redundancy Capability:**

- Is redundancy implemented? (Yes/No)
- Redundancy type? (Active-Active/Hot Standby/Warm Standby/Cold Standby/None)
- Last failover test? (Date/Result)
- Achievable RTO based on current redundancy = Estimated recovery time

**Step 2: Compare Required vs. Actual**

**RPO Gap:**
```
RPO Gap = Required RPO - Actual RPO

Example:
  Required RPO: 4 hours (from BIA)
  Actual RPO: 24 hours (daily backup)
  RPO Gap: -20 hours (WORSE than required - GAP EXISTS)
```

**RTO Gap:**
```
RTO Gap = Required RTO - Actual RTO

Example:
  Required RTO: 4 hours (from BIA)
  Actual RTO: 24 hours (restore from backup, no redundancy)
  RTO Gap: -20 hours (WORSE than required - GAP EXISTS)
```

**Step 3: Classify Gap Severity**

**Gap Priority Framework:**

| Priority | Criteria | Response Time |
|----------|----------|--------------|
| **P1 - Critical** | Tier 1 system gap, severe non-compliance (cannot meet RTO/RPO at all) | Remediate within 30 days |
| **P2 - High** | Tier 2 system gap, significant non-compliance | Remediate within 90 days |
| **P3 - Medium** | Tier 3 system gap, moderate non-compliance | Remediate within 180 days |
| **P4 - Low** | Tier 4 system gap, or risk accepted | Risk acceptance documented |

**Gap Priority Formula (Excel):**
```excel
=IF(AND(Final_Tier="Tier 1", OR(RPO_Gap<0, RTO_Gap<0)), "P1 - Critical",
  IF(AND(Final_Tier="Tier 2", OR(RPO_Gap<0, RTO_Gap<0)), "P2 - High",
    IF(AND(Final_Tier="Tier 3", OR(RPO_Gap<0, RTO_Gap<0)), "P3 - Medium", "P4 - Low")))
```

**Step 4: Develop Remediation Plan**

For each P1 and P2 gap:

- **Remediation Action:** Specific steps to close gap (e.g., "Implement hourly backup", "Deploy hot standby in Azure West Europe")
- **Remediation Owner:** Person accountable for remediation
- **Target Date:** Deadline based on priority
- **Estimated Cost:** Budget required (labor + technology)
- **Approval Required:** Budget approval from executive management

**Example Gap Analysis:**

| System | Required RPO | Actual RPO | RPO Gap | Required RTO | Actual RTO | RTO Gap | Gap Priority | Remediation Plan |
|--------|-------------|-----------|---------|-------------|-----------|---------|-------------|----------------|
| **Payment DB** | 1h | 24h | -23h | 1h | 24h | -23h | **P1 - Critical** | Implement hourly incremental backup + transaction log backups; Deploy Azure SQL Always On (hot standby); Cost: CHF 15K/year; Owner: DBA Team; Target: 30 days |
| **E-commerce Platform** | 4h | 24h | -20h | 4h | 24h | -20h | **P1 - Critical** | Implement 4-hourly backup; Deploy warm standby in Azure (pre-provisioned VMs); Cost: CHF 8K/year; Owner: Platform Team; Target: 30 days |
| **CRM (Salesforce)** | 24h | 24h | 0 | 8h | 8h | 0 | **No Gap** | Salesforce native backup sufficient; Native HA meets RTO |

**Step 5: Calculate Total Remediation Cost**

Sum estimated costs for all P1 and P2 gaps → Budget request for executive approval.

**Example:**
```
P1 Gaps: CHF 23K/year (Payment DB + E-commerce)
P2 Gaps: CHF 5K/year (Inventory + 2 other systems)
────────────────────
Total BC/DR Gap Remediation Budget: CHF 28K/year recurring + CHF 15K one-time implementation
```

**Document in BIA Workbook - Sheet 7: Gap Analysis**

- System Name
- Final Tier (from Sheet 5)
- Required RPO (from Sheet 4)
- Actual RPO (manual entry - current backup frequency)
- RPO Gap (calculated: Required - Actual, in hours)
- Required RTO (from Sheet 4)
- Actual RTO (manual entry - current recovery capability)
- RTO Gap (calculated: Required - Actual, in hours)
- Gap Priority (calculated formula: P1/P2/P3/P4)
- Remediation Plan (text description)
- Remediation Owner (name)
- Target Date (date)
- Estimated Cost (CHF)
- Status (dropdown: Not Started/In Progress/Complete)

**Conditional Formatting:**

- RPO Gap < 0 (negative = gap exists): Red cell
- RTO Gap < 0 (negative = gap exists): Red cell
- Gap Priority "P1 - Critical": Red row
- Gap Priority "P2 - High": Orange row
- Status "Complete": Green cell

**Quality Check:**

- ✓ All systems assessed for current backup/redundancy capability
- ✓ Gaps calculated correctly (negative = gap exists)
- ✓ Gap priority aligns with criticality tier
- ✓ Remediation plans specific and actionable
- ✓ Remediation owners assigned
- ✓ Target dates realistic based on priority
- ✓ Costs estimated (for budget approval)
- ✓ Total remediation cost calculated

## STEP 10: APPROVE & DOCUMENT Findings

**Objective:** Obtain executive approval for BIA results, criticality classifications, and gap remediation budget.

**Duration:** Week 5-6

**Approval Requirements:**

| Item Requiring Approval | Approver | Format |
|------------------------|----------|--------|
| **Tier 1 System Classifications** | Executive Management (CEO/CIO/CISO) | BIA Approval Meeting + Written Sign-Off |
| **Tier 2 System Classifications** | CISO + IT Director | Written Sign-Off on BIA Report |
| **Gap Remediation Budget (P1/P2)** | Executive Management + CFO | Budget Approval Meeting + Financial Approval |
| **Risk Acceptance (P3/P4 gaps)** | System Owner + Risk Committee | Risk Acceptance Form |
| **Overall BIA Methodology** | BC/DR Coordinator + CISO | Sign-Off on BIA Report |

**Step 1: Prepare BIA Report**

**BIA Report Structure:**

1. **Executive Summary** (2-3 pages)

   - BIA purpose and scope
   - Methodology overview
   - Key findings summary
   - Total systems assessed, breakdown by tier
   - Critical gaps requiring immediate remediation (P1)
   - Budget request summary

2. **Detailed Findings** (10-20 pages)

   - Business process inventory
   - System criticality classifications
   - RPO/RTO requirements by tier
   - Dependency analysis
   - Gap analysis (detailed)
   - Remediation roadmap

3. **Appendices**

   - BIA Assessment Workbook (Excel - all 5 sheets)
   - Dependency diagrams
   - Interview notes
   - Regulatory requirements mapping
   - Risk register integration

**Step 2: Schedule Executive Approval Meeting**

**Agenda (90 minutes):**

| Time | Topic | Presenter |
|------|-------|-----------|
| **0-10 min** | BIA Methodology Overview | BC/DR Coordinator |
| **10-30 min** | Findings Presentation | BC/DR Coordinator |
| **30-50 min** | Gap Analysis & Budget Request | BC/DR Coordinator + CFO |
| **50-70 min** | Tier 1 System Review & Approval | BC/DR Coordinator + System Owners |
| **70-85 min** | Discussion & Questions | All |
| **85-90 min** | Formal Approval & Next Steps | CEO/CIO |

**Step 3: Address Executive Feedback**

**Common Executive Questions (Be Prepared):**

- "Why is [System X] classified as Tier 1?" → Reference financial impact, regulatory requirement, customer SLA
- "Can we downgrade [System Y] to save costs?" → Explain risk (if Tier 1 downgraded, cannot meet SLA/regulatory obligation)
- "CHF 28K seems expensive for BC/DR, can we reduce?" → Explain cost of NOT having BC/DR (CHF 50K/hour revenue loss vs. CHF 28K/year investment)
- "What if we don't remediate the P1 gaps?" → Quantify risk (revenue loss + regulatory fines + reputational damage)

**Step 4: Obtain Written Approval**

**BIA Approval Sign-Off Sheet (Include in BIA Report):**

```
BIA APPROVAL SIGN-OFF

I approve the following Business Impact Analysis findings and commit to supporting the recommended remediation activities:

Tier 1 Critical Systems: [List]
Tier 2 Important Systems: [List]
Gap Remediation Budget: CHF [Amount] (annual recurring) + CHF [Amount] (one-time)
Risk Acceptance: [List of P3/P4 gaps accepted]

Signatures:

___________________________  Date: __________
[CEO Name], Chief Executive Officer

___________________________  Date: __________
[CIO Name], Chief Information Officer

___________________________  Date: __________
[CISO Name], Chief Information Security Officer

___________________________  Date: __________
[CFO Name], Chief Financial Officer

___________________________  Date: __________
[BC/DR Coordinator Name], BC/DR Coordinator
```

**Step 5: Document and Archive**

**BIA Evidence Repository:**

Create centralized folder structure:
```
BIA_2026/
  ├── 01_Planning/
  │     ├── BIA_Project_Charter.docx
  │     └── Stakeholder_List.xlsx
  ├── 02_Data_Collection/
  │     ├── Interview_Notes/
  │     └── System_Documentation/
  ├── 03_Analysis/
  │     ├── BIA_Assessment_Workbook_2026.xlsx (MASTER)
  │     └── Dependency_Diagrams/
  ├── 04_Approval/
  │     ├── BIA_Report_2026_FINAL.pdf
  │     ├── Executive_Presentation_2026-01-25.pptx
  │     └── Signed_Approval_Sheet.pdf
  └── 05_Implementation/
        └── Gap_Remediation_Project_Plan.xlsx
```

**Retention:** 3+ years (for audit)

**Annual Review:** Next BIA scheduled for [Current Date + 12 months]

---

[Sections 4-6 continue with Impact Scoring, RPO/RTO Framework, Common Pitfalls]
[Sections 7-12 continue with Workbook Guide, Evidence, Quality, Approval, Integration, Compliance]
[PART II contains complete Excel technical specifications]

**DOCUMENT CONTINUES...**

---

# Impact Scoring Methodology

[Complete section with Swiss CHF-calibrated scoring framework...]

# RPO/RTO Determination Framework

[Complete section with business-driven determination methodology...]

# Common Pitfalls & How to Avoid Them

[Complete section covering 9 major pitfalls...]

# BIA Workbook Completion Guide

[Complete guide for all 9 Excel sheets...]

# Evidence Collection

[Complete evidence requirements and best practices...]

# Quality Checklist

[Complete pre-submission checklist...]

# Review & Approval Process

[Complete approval workflow...]

# Integration with BC/DR Implementation

[Complete integration with IMP-S2, S3, S4, S5...]

# Regulatory Compliance Mapping

[Complete compliance mapping for ISO/DORA/NIS2/PCI DSS v4.0.1/FINMA...]

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
