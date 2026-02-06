**ISMS-IMP-A.5.23.S1-UG - Cloud Service Inventory & Classification**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S1-UG |
| **Version** | 1.0 |
| **Assessment Area** | Cloud Service Inventory & Classification |
| **Related Policy** | ISMS-POL-A.5.19-23-S5 (Cloud Services Security), ISMS-POL-A.5.19-23-S1 (Supplier Relationships) |
| **Purpose** | Maintain authoritative inventory of all cloud services with data classification, criticality assessment, and exit feasibility analysis |
| **Target Audience** | IT Operations, Procurement, Finance, Security Teams, Compliance Officers, Auditors |
| **Assessment Type** | Inventory & Classification |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.23.S1-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.23.S1 - Cloud Service Inventory & Classification

#### What This Assessment Covers

This assessment creates and maintains the **authoritative inventory** of ALL cloud services used by [Organization]. This is the foundation of your cloud security program - you cannot secure, configure, monitor, or audit cloud services you don't know about.

This assessment answers:

- **What cloud services exist?** (Complete inventory: SaaS, IaaS, PaaS, security services, storage)
- **Who provides them?** (Vendor identification)
- **What data do they process?** (Data classification)
- **How critical are they?** (Business impact assessment)
- **What's the financial commitment?** (Costs, contract terms)
- **How do we exit if needed?** (Exit strategy assessment)

#### Key Principle

**"If it touches organizational data or infrastructure, it must be in this inventory."**

This includes:

- ✅ Officially procured cloud services (sanctioned IT)
- ✅ Shadow IT discovered through monitoring
- ✅ Free/trial services used by business units
- ✅ Cloud-based security tools
- ✅ Cloud storage and collaboration platforms
- ✅ Infrastructure services (AWS, Azure, GCP)
- ✅ Development/test cloud environments

This is a **zero-tolerance inventory** - no cloud service is too small to track.

#### What You'll Document

For EACH cloud service:

**Basic Information:**

- Service name (what YOU call it)
- Vendor/provider name
- Service type (SaaS, IaaS, PaaS, etc.)
- Deployment status (production, dev, trial, decommissioned)
- Service owner (internal person responsible)

**Classification:**

- Data classification (what data types it processes)
- Service criticality (business impact if unavailable)
- User count (how many people use it)
- Geographic scope (where it's used)

**Financial:**

- Annual cost
- Contract status (active, expiring, trial)
- Procurement method (enterprise agreement, credit card, etc.)

**Risk & Compliance:**

- Data residency (where data is stored/processed)
- Regulatory requirements (GDPR, FADP, sector-specific)
- Vendor risk rating
- Exit strategy status

#### How This Relates to Other A.5.23 Assessments

| Assessment | Focus | Relationship to A.5.23.1 |
|------------|-------|--------------------------|
| **ISMS-IMP-A.5.23.S1** | **Inventory & Classification** | **WHAT services exist** (START HERE) |
| ISMS-IMP-A.5.23.S2 | Vendor Due Diligence | WHO provides services (uses this inventory) |
| ISMS-IMP-A.5.23.S3 | Secure Configuration | HOW services are configured (uses this inventory) |
| ISMS-IMP-A.5.23.S4 | Ongoing Governance | HOW services are managed (uses this inventory) |
| ISMS-IMP-A.5.23.S5 | Compliance Dashboard | Consolidated compliance view (aggregates all) |

**Critical Dependency:** This assessment (A.5.23.1) MUST be completed FIRST and kept current. All other A.5.23 assessments depend on having an accurate, complete cloud service inventory.

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **IT Operations** - Service ownership, infrastructure knowledge
2. **Procurement** - Contract details, costs, vendor relationships
3. **Finance** - Budget tracking, cost allocation
4. **Security** - Risk assessment, data classification
5. **Compliance** - Regulatory requirements, audit support

#### Required Skills

- Broad knowledge of organizational IT landscape
- Understanding of cloud service models (SaaS, IaaS, PaaS)
- Familiarity with data classification schemes
- Access to procurement and financial systems
- Ability to interview service owners across departments

#### Time Commitment

- **Initial inventory (from scratch):** 20-40 hours
  - Discovery: 8-12 hours
  - Documentation: 8-16 hours
  - Classification: 4-8 hours
  - Validation: 2-4 hours

- **Quarterly updates:** 4-8 hours
  - New services: 1-2 hours
  - Changes to existing: 2-3 hours
  - Decommissions: 1 hour
  - Validation: 1-2 hours

#### Collaboration Model

**This is a TEAM effort, not a solo activity.**

Recommended approach:
1. **Coordinator** (IT Ops or Security) - Owns the assessment, coordinates input
2. **Contributors** - Department representatives provide service details
3. **Reviewers** - Finance validates costs, Security validates classifications
4. **Approvers** - CIO/CISO final approval

### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete cloud service inventory** - Every cloud service documented
2. ✅ **Data classification mapping** - What data each service processes
3. ✅ **Criticality assessment** - Business impact understanding
4. ✅ **Financial tracking** - Total cloud spend, contract visibility
5. ✅ **Vendor landscape** - Understanding of cloud provider dependencies
6. ✅ **Exit strategy assessment** - Exit feasibility for each service
7. ✅ **Compliance mapping** - Regulatory requirements per service
8. ✅ **Risk visibility** - Concentrated risks, shadow IT, gaps
9. ✅ **Evidence register** - Supporting documentation for audit
10. ✅ **Approved assessment** - Management sign-off and audit readiness

### Assessment Success Criteria

You'll know this assessment is successful when:

- ✅ **Completeness:** No undocumented cloud services (verified through multiple discovery methods)
- ✅ **Accuracy:** All data verified with service owners and financial systems
- ✅ **Currency:** Updated within last 90 days
- ✅ **Usability:** Other teams can use this as authoritative source
- ✅ **Auditability:** Evidence supports all classifications and ratings
- ✅ **Actionability:** Gaps and risks have remediation plans

### Common Use Cases

**Use Case 1: Budget Planning**

- Finance needs total cloud spend
- Filter by department/cost center
- Identify renewal dates
- Project next year's costs

**Use Case 2: Audit Support**

- Auditor asks: "What cloud services process customer PII?"
- Filter by data classification = Confidential/Restricted
- Filter by data type = Personal Data
- Generate report with evidence

**Use Case 3: Vendor Risk Assessment**

- Security needs to assess concentration risk
- Group services by vendor
- Identify critical dependencies on single vendor
- Assess exit feasibility

**Use Case 4: Shadow IT Discovery**

- Discover services not in official procurement
- Compare credit card statements vs. inventory
- Engage with departments using unapproved services
- Regularize or sunset shadow IT

**Use Case 5: Contract Renewals**

- Procurement needs to know what's expiring in Q3
- Filter by contract expiration date
- Review usage and criticality
- Decide: renew, renegotiate, or terminate

---

## Assessment Methodology

### Discovery Methods

To build a complete inventory, use MULTIPLE discovery methods:

#### Method 1: Procurement Records

**Source:** Purchase orders, invoices, contracts
**Covers:** Officially procured services
**Limitations:** Misses shadow IT, free trials, credit card purchases

**How to Execute:**
1. Export all cloud-related purchases (last 24 months)
2. Filter by vendor type (software, cloud, SaaS)
3. Identify recurring subscriptions
4. Cross-reference with current usage

#### Method 2: Financial System Analysis

**Source:** Expense reports, credit card statements, budgets
**Covers:** Credit card purchases, expense reimbursements
**Limitations:** May not identify service names clearly

**How to Execute:**
1. Review credit card transactions (IT, department cards)
2. Look for recurring charges to known cloud vendors
3. Investigate unfamiliar cloud-related charges
4. Correlate with service owners

#### Method 3: Network Traffic Analysis

**Source:** Firewall logs, web proxy logs, DNS queries
**Covers:** Actually used services (not just purchased)
**Limitations:** May miss encrypted traffic, requires log analysis skills

**How to Execute:**
1. Export top 1000 destination domains (last 30 days)
2. Identify cloud service domains (*.amazonaws.com, *.office365.com, etc.)
3. Correlate with known cloud providers
4. Investigate unknown domains

#### Method 4: SSO/Identity Provider Analysis

**Source:** Single Sign-On applications, Entra ID app registrations, Okta apps
**Covers:** Services integrated with corporate identity
**Limitations:** Misses services without SSO

**How to Execute:**
1. Export all applications from SSO provider
2. Identify cloud services
3. Document user counts and access patterns
4. Verify active usage

#### Method 5: Department Surveys

**Source:** Direct inquiry with department heads
**Covers:** Department-specific tools, business unit services
**Limitations:** Depends on honest reporting, may miss individual tools

**How to Execute:**
1. Send survey to all department heads
2. Ask: "What cloud services does your team use?"
3. Include examples (collaboration, storage, business apps)
4. Follow up on responses

#### Method 6: IT Asset Inventory

**Source:** CMDB, asset management systems
**Covers:** Services registered in official inventory
**Limitations:** Often outdated or incomplete

**How to Execute:**
1. Export all "cloud" or "SaaS" assets from CMDB
2. Verify current status
3. Add missing services
4. Update outdated entries

**Recommended Approach:** Use ALL methods and triangulate results. Services found by multiple methods have higher confidence.

---

## Assessment Lifecycle

### Initial Inventory (Year 1)

**Phase 1: Discovery (Weeks 1-2)**

- Execute all 6 discovery methods
- Compile raw list of potential cloud services
- Deduplicate and consolidate
- Identify service owners

**Phase 2: Documentation (Weeks 3-4)**

- Interview service owners
- Collect service details
- Gather evidence (contracts, screenshots)
- Document in assessment workbook

**Phase 3: Classification (Week 5)**

- Assess data classification
- Determine service criticality
- Evaluate exit feasibility
- Calculate risk ratings

**Phase 4: Validation (Week 6)**

- Cross-check with finance
- Verify with department heads
- Reconcile discrepancies
- Quality review

**Phase 5: Approval (Week 7)**

- Technical review
- Compliance review
- Management approval
- Publish as authoritative source

### Quarterly Updates (Ongoing)

**Week 1: Discovery Refresh**

- Run automated discovery (network, SSO, financial)
- Identify new services since last assessment
- Identify decommissioned services
- Update service details

**Week 2: Classification Review**

- Re-assess criticality (business changes?)
- Update data classification (new data types?)
- Review exit strategies (tested recently?)
- Update risk ratings

**Week 3: Validation & Approval**

- Finance validates costs
- Security validates classifications
- Management approves changes
- Update version history

**Week 4: Reporting**

- Publish updated inventory
- Notify dependent teams
- Update compliance dashboard
- Archive previous version

### Triggered Updates

Update inventory immediately when:

- ✅ New cloud service deployed
- ✅ Major service change (new use case, new data type)
- ✅ Service decommissioned
- ✅ Vendor acquisition or merger
- ✅ Security incident involving cloud service
- ✅ Before audits

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Organizational Access

- **Financial Systems:** Access to procurement, accounts payable, expense management
- **Asset Management:** Access to CMDB, IT asset inventory
- **Network Monitoring:** Access to firewall logs, web proxy logs, DNS logs
- **Identity Systems:** Access to SSO provider (Entra ID, Okta, etc.)
- **Contracts Repository:** Access to vendor contracts and agreements

#### 2. Discovery Data Sources

**Procurement Data:**

- Purchase orders (last 24 months)
- Vendor invoices (recurring subscriptions)
- Software licenses and cloud service contracts
- Trial and proof-of-concept agreements

**Financial Data:**

- Credit card statements (IT department cards)
- Expense reports with cloud service charges
- Budget allocations for cloud services
- Cost center allocations

**Technical Data:**

- Network traffic logs (top destinations, last 30 days)
- SSO application list with user counts
- DNS query logs (identify cloud domains)
- Email gateway logs (cloud service signups)

**Organizational Data:**

- Department directory (service owners)
- Organizational chart (approval hierarchy)
- Business unit structure (cost allocation)
- Geographic locations (data residency)

#### 3. Policy Documents

- **ISMS-POL-A.5.19-23:** Supplier & Cloud Services Security Policy
- **ISMS-POL-A.5.19-23-S5:** Cloud Services Security (specific requirements)
- **Data Classification Policy:** Data handling requirements
- **Business Continuity Policy:** Criticality assessment criteria

#### 4. Reference Data

- **Cloud Service Provider Registry:** Pre-populated vendor list (if available)
- **Data Classification Scheme:** Classification levels and definitions
- **Criticality Assessment Matrix:** Business impact criteria
- **Exit Strategy Templates:** Exit planning frameworks

### Required Tools

- **Microsoft Excel 2016 or later:** For workbook completion
- **Network analysis tools:** To review traffic logs (optional: SIEM, log analytics)
- **SSO admin console:** To export application list and usage data
- **Financial reporting tools:** To extract cloud spending data
- **Screen capture tools:** For evidence collection
- **File organization:** Folder structure for evidence storage

### Required Permissions

Ensure you have appropriate access:

- [ ] Read access to procurement system
- [ ] Read access to financial/accounting system
- [ ] Admin access to SSO provider (or permission to request exports)
- [ ] Read access to network monitoring/SIEM
- [ ] Access to contract repository
- [ ] Ability to contact service owners across departments
- [ ] Permission to view budget allocations (finance approval may be needed)

### Dependencies

**No prerequisites from other assessments** - This is the foundational assessment.

**This assessment is INPUT to:**

- ISMS-IMP-A.5.23.S2 (Vendor Due Diligence) - Uses service/vendor list
- ISMS-IMP-A.5.23.S3 (Secure Configuration) - Uses service list and criticality
- ISMS-IMP-A.5.23.S4 (Ongoing Governance) - Uses service list and ownership
- ISMS-IMP-A.5.23.S5 (Compliance Dashboard) - Aggregates all assessment data

**External Dependencies:**

- Stakeholder availability (service owners for interviews)
- Finance cooperation (cost validation)
- Procurement cooperation (contract details)

---

## Workflow

### High-Level Process

```
1. PREPARE
   ↓
2. DISCOVER SERVICES (Multi-method discovery)
   ↓
3. CONSOLIDATE & DEDUPLICATE
   ↓
4. DOCUMENT SERVICES (Interview owners, collect evidence)
   ↓
5. CLASSIFY DATA
   ↓
6. ASSESS CRITICALITY
   ↓
7. EVALUATE EXIT FEASIBILITY
   ↓
8. CALCULATE FINANCIAL IMPACT
   ↓
9. IDENTIFY GAPS & RISKS
   ↓
10. REVIEW & APPROVE
```

---

### Detailed Workflow

#### Phase 1: Preparation (4-8 hours)

**Objective:** Set up assessment infrastructure and gather data sources

**Steps:**
1. **Read this entire User Guide** (1 hour)
2. **Review related policies** (1 hour)

   - ISMS-POL-A.5.19-23-S5 (Cloud Services Security)
   - Data Classification Policy
   - Business Continuity Policy

3. **Set up working folders** (30 minutes)

   - Create folder structure for evidence
   - Set up naming conventions
   - Create evidence log template

4. **Identify stakeholders** (1 hour)

   - List all department heads
   - Identify known service owners
   - Schedule discovery interviews

5. **Gather access permissions** (1-2 hours)

   - Request SSO admin access (if needed)
   - Request financial system access
   - Request procurement system access

6. **Extract initial discovery data** (2-3 hours)

   - Export procurement data
   - Export SSO application list
   - Export financial data (if available)
   - Export network logs (if available)

**Deliverable:** 

- Working folders created
- Discovery data files collected
- Stakeholder list with contact info
- Assessment timeline with milestones

**Quality Check:**

- ✓ All required access permissions obtained
- ✓ Discovery data sources identified and accessible
- ✓ Stakeholders identified and scheduled
- ✓ Working folders organized

---

#### Phase 2: Multi-Method Discovery (8-12 hours)

**Objective:** Identify ALL cloud services through 6 discovery methods

**Method 1: Procurement Discovery (2 hours)**

Steps:
1. Export all purchase orders tagged "software" or "cloud" (last 24 months)
2. Filter for recurring subscriptions
3. Identify cloud service vendors
4. Create list of services with: Vendor, Service Name, Annual Cost, Contract End Date

Expected Output: 30-100 services (depending on org size)

**Method 2: Financial Discovery (2 hours)**

Steps:
1. Export credit card transactions for IT department cards (last 12 months)
2. Filter for known cloud vendors (AWS, Microsoft, Google, Salesforce, etc.)
3. Identify recurring charges
4. Cross-reference with procurement list

Expected Output: 10-30 additional services (shadow IT)

**Method 3: Network Traffic Discovery (2-3 hours)**

Steps:
1. Export top 1000 destination domains from firewall/proxy (last 30 days)
2. Filter for known cloud service domains:

   - *.amazonaws.com
   - *.azure.com, *.microsoft.com
   - *.google.com, *.googleapis.com
   - *.salesforce.com
   - *.zoom.us, *.webex.com
   - *.slack.com, *.dropbox.com
   - (Add others as needed)

3. Investigate unknown domains (whois lookup, web search)
4. Create list of active cloud services

Expected Output: Verification of active usage + 5-15 undocumented services

**Method 4: SSO/Identity Discovery (1 hour)**

Steps:
1. Log into SSO admin console (Entra ID, Okta, etc.)
2. Export all registered applications
3. Filter for cloud services (exclude internal apps)
4. Document: Service Name, User Count, Last Login Date
5. Identify inactive apps (no logins in 90 days)

Expected Output: 20-80 services + user count data

**Method 5: Department Survey (2-3 hours)**

Steps:
1. Create survey email template:
   ```
   Subject: Cloud Services Inventory - Your Input Needed
   
   Hi [Department Head],
   
   We're conducting an inventory of cloud services used across [Organization].
   Please list all cloud-based tools and services your team uses, including:
   
   - Collaboration tools (Slack, Teams, Zoom, etc.)
   - Business applications (Salesforce, HubSpot, etc.)
   - File storage (Dropbox, Box, Google Drive, etc.)
   - Development tools (GitHub, AWS, Azure, etc.)
   - Any other cloud services
   
   For each service, please provide:
   1. Service name
   2. Vendor
   3. Primary use case
   4. Approximate number of users in your team
   5. Service owner name (if known)
   
   Please respond by [date].
   
   Thank you!
   ```

2. Send to all department heads
3. Follow up after 3 days
4. Consolidate responses

Expected Output: 10-40 services + ownership information

**Method 6: Asset Inventory Review (1 hour)**

Steps:
1. Export all assets from CMDB tagged as "Cloud" or "SaaS"
2. Verify current status (still in use?)
3. Cross-reference with other discovery methods
4. Identify services in CMDB but not found elsewhere (decommissioned?)

Expected Output: Verification + gap identification

**Discovery Consolidation:**

After all 6 methods:
1. Consolidate all findings into single master list
2. Deduplicate (same service found by multiple methods)
3. Flag confidence level:

   - **High:** Found by 3+ methods
   - **Medium:** Found by 2 methods
   - **Low:** Found by 1 method only

4. Create initial inventory spreadsheet

**Deliverable:**

- Master list of all discovered services (100-300 services typical for ~300 staff org)
- Confidence ratings per service
- Initial ownership assignment (where known)
- Discovery method attribution (which method found each service)

**Quality Check:**

- ✓ All 6 discovery methods executed
- ✓ Results consolidated and deduplicated
- ✓ No obvious gaps (compare to industry benchmarks)
- ✓ Confidence ratings assigned

---

#### Phase 3: Service Documentation (8-16 hours)

**Objective:** Complete detailed documentation for EACH service in inventory

**For each service:**

**Step 1: Identify Service Owner (15 minutes per service)**

- Who requested/purchased the service?
- Who uses it day-to-day?
- Who is accountable for it?
- Document in Sheet 1: Service Owner field

**Step 2: Verify Basic Details (15 minutes per service)**

- Official service name (as vendor calls it)
- Vendor name (legal entity, not brand)
- Service type (SaaS, IaaS, PaaS, etc.)
- Deployment model (public cloud, private, hybrid)
- Primary use case
- User count (active users)

**Step 3: Financial Details (10 minutes per service)**

Cross-reference with procurement/finance:

- Annual cost (verify with invoice)
- Contract start/end dates
- Renewal status (auto-renew, manual, trial)
- Payment method (enterprise agreement, credit card, invoice)
- Cost allocation (department, cost center)

**Step 4: Technical Details (10 minutes per service)**

- Service URL/endpoint
- Integration points (SSO, API, data feeds)
- Data location/residency
- Deployment region (EU, US, Global)

**Step 5: Collect Evidence (10 minutes per service)**

For each service, collect:

- Contract or purchase order (PDF)
- Invoice showing annual cost
- Screenshot of admin console (sanitized)
- User list export (sanitized)
- SSO configuration screenshot (if integrated)

**Deliverable:**

- Sheet 1 (Service Inventory) - Complete for all services
- Evidence folder with organized files
- Contact list of all service owners

**Quality Check:**

- ✓ Every service has basic details complete
- ✓ No "Unknown" or "TBD" without justification
- ✓ Service owners identified (or escalated if unknown)
- ✓ Financial data verified with procurement/finance
- ✓ Evidence collected for high-value/critical services

**Time Estimate:**

- Small org (50 services): 8 hours
- Medium org (150 services): 16 hours  
- Large org (300+ services): 24+ hours (consider team approach)

---

#### Phase 4: Data Classification (4-8 hours)

**Objective:** Classify what data each service processes

**For each service:**

**Step 1: Review Data Types**

Ask service owner:

- What data does this service process?
- Personal data (names, emails, addresses)?
- Financial data (credit cards, bank accounts)?
- Health data (HIPAA/medical records)?
- Intellectual property (trade secrets, R&D)?
- Customer data (CRM, support tickets)?
- Employee data (HR, payroll)?
- Public data only?

**Step 2: Apply Classification Level**

Using organizational data classification policy:

| Classification | Examples | Protection Requirements |
|----------------|----------|------------------------|
| **Restricted** | Personal health info, credit card numbers, trade secrets | Highest protection, encryption, audit logging |
| **Confidential** | Customer contracts, financial reports, employee data | Strong protection, access controls |
| **Internal** | Internal documents, project plans, non-public info | Standard protection |
| **Public** | Marketing materials, public website content | Minimal protection |

Assign highest classification level that applies.

**Special Cases:**

- **Mixed Data:** If service processes both Confidential and Public data → classify as Confidential (highest applies)
- **No Data:** Services that don't process organizational data (rare) → classify as N/A
- **Unknown:** If service owner unsure → classify as Confidential until verified (conservative approach)

**Step 3: Document Data Residency**

- Where is data stored? (geographic location: EU, US, Switzerland, Global)
- Where is data processed? (may differ from storage)
- Is data encrypted at rest?
- Is data encrypted in transit?

**Step 4: Identify Regulatory Requirements**

Based on data classification and residency:

- **GDPR:** If EU personal data
- **Swiss FADP:** If Swiss personal data
- **HIPAA:** If US healthcare data
- **PCI-DSS:** If credit card data
- **SOX:** If financial reporting data
- **Sector-specific:** Banking, insurance, etc.

**Deliverable:**

- Sheet 2 (Data Classification) - Complete for all services
- Data flow diagrams (for critical services)
- Regulatory requirements matrix

**Quality Check:**

- ✓ Every service has data classification assigned
- ✓ Classification level justified (not guessed)
- ✓ Data residency documented
- ✓ Regulatory requirements identified
- ✓ Mixed data services flagged for further review

---

#### Phase 5: Criticality Assessment (4-6 hours)

**Objective:** Determine business impact if service becomes unavailable

**Criticality Criteria:**

Use these definitions (aligned with Business Continuity Policy):

| Criticality | RTO | Business Impact | Examples |
|-------------|-----|-----------------|----------|
| **Critical** | < 4 hours | Organization cannot operate without this service. Revenue loss, customer impact, regulatory breach. | Email, CRM, payment processing, core production systems |
| **High** | 4-24 hours | Significant business impact. Major workflow disruption, but workarounds exist. | Collaboration tools, HR systems, project management |
| **Medium** | 1-3 days | Moderate impact. Can operate with temporary workarounds for limited time. | Reporting tools, analytics, non-critical integrations |
| **Low** | > 3 days | Minimal impact. Nice to have but not essential for operations. | Training platforms, internal wikis, test environments |

**Assessment Questions:**

For each service, ask:
1. **What happens if this service goes down for 1 hour?**

   - No impact → Low
   - Minor inconvenience → Medium
   - Workflow disruption → High
   - Revenue/customer impact → Critical

2. **Can we operate without this service for a day?**

   - Yes, no problem → Low/Medium
   - Yes, but difficult → High
   - No, absolutely not → Critical

3. **How many users are affected?**

   - < 10 users → Lower criticality
   - 10-50 users → Medium/High
   - 50+ users or customer-facing → High/Critical

4. **Is this service customer-facing or revenue-generating?**

   - Yes → High or Critical
   - No → Medium or lower

**Special Considerations:**

- **Dependency chains:** Service may be low criticality itself but supports critical service → increase rating
- **Seasonal criticality:** Tax software critical only during tax season → document in notes
- **Redundancy:** If backup/failover exists → may reduce criticality rating

**Deliverable:**

- Sheet 3 (Criticality Assessment) - Complete for all services
- Business impact analysis (BIA) summaries for Critical/High services
- Dependency mapping (for critical services)

**Quality Check:**

- ✓ Every service has criticality rating
- ✓ Critical services have BIA documentation
- ✓ Service owners agree with criticality rating
- ✓ Criticality ratings consistent with RTO/RPO values
- ✓ No obvious misclassifications (critical service rated low)

---

#### Phase 6: Exit Feasibility Assessment (4-6 hours)

**Objective:** Assess how easily organization could exit each cloud service

**For each service, assess:**

**Exit Strategy Type:**

- Cloud-to-Cloud (migrate to alternative cloud provider)
- Hybrid (partial on-premises repatriation)
- On-Premises (full build-back to internal infrastructure)
- Not Determined

**Data Portability:**

- Export format available? (Standard CSV/JSON, Proprietary, API Only, None)
- Export tested? (Yes, No, Partial)
- Data volume (GB)
- Migration complexity (Low, Medium, High, Very High)

**Alternative Providers:**

- Alternative identified? (Yes, No, Multiple Options)
- Alternative assessed? (Capability comparison done?)
- Migration estimate (time in days)
- Migration cost estimate

**Vendor Lock-In Risk:**

- Lock-in risk rating (Low, Medium, High, Critical)
- Lock-in factors:
  - Proprietary data formats
  - Proprietary APIs
  - Deep integrations
  - Custom development
  - Training investment
  - Contract terms

**Exit Plan Status:**

- Documented (full exit plan exists)
- Draft (plan in progress)
- Not Started
- N/A (service not critical enough to require exit plan)

**Rating Guidelines:**

| Exit Feasibility | Characteristics |
|------------------|-----------------|
| **Easy Exit** | Standard export formats, multiple alternatives available, no custom development, contract allows termination |
| **Moderate Exit** | Some proprietary formats, limited alternatives, some custom integrations, contract has notice period |
| **Difficult Exit** | Proprietary formats, few alternatives, deep integrations, significant custom development, long contract |
| **Locked-In** | No viable alternatives, completely proprietary, mission-critical custom development, multi-year contract with penalties |

**For Critical/High services:**

Must have documented exit plans including:

- Exit triggers (when would we exit?)
- Alternative providers identified
- Data export procedures tested
- Migration cost estimated
- Timeline estimated
- Resource requirements identified

**Deliverable:**

- Sheet 4 (Exit Feasibility) - Complete for all services
- Exit plans documented for Critical/High services
- Vendor lock-in risk register

**Quality Check:**

- ✓ All services assessed for exit feasibility
- ✓ Critical/High services have exit plans
- ✓ Data export capabilities verified (not assumed)
- ✓ Lock-in risks identified and documented
- ✓ Alternative providers researched

---

#### Phase 7: Financial Impact Analysis (2-4 hours)

**Objective:** Calculate total cloud spend and identify cost optimization opportunities

**Activities:**

**Total Cost Calculation:**
1. Sum all annual costs (from Sheet 1)
2. Break down by:

   - Service type (SaaS, IaaS, PaaS)
   - Department
   - Vendor
   - Criticality

**Spend Analysis:**

- Top 10 most expensive services (80/20 rule - these are likely 80% of spend)
- Services with cost increases (compare to prior year)
- Unused/underutilized services (low user count vs. cost)
- Duplicate services (same function, different vendor)

**Contract Review:**

- Services expiring in next 90 days
- Services with auto-renewal (can we negotiate better terms?)
- Trial services that converted to paid (was this authorized?)
- Services without contracts (credit card purchases - negotiate volume discount?)

**Cost Optimization Opportunities:**
1. Consolidation (eliminate duplicates)
2. Right-sizing (reduce licenses for underutilized services)
3. Renegotiation (volume discounts, multi-year commits)
4. Elimination (sunset unused services)

**Deliverable:**

- Sheet 5 (Financial Summary) - Complete with totals and breakdowns
- Cost optimization recommendations
- Contract renewal calendar

**Quality Check:**

- ✓ All costs verified with finance
- ✓ Totals reconcile with budget
- ✓ Optimization opportunities identified
- ✓ Renewal dates tracked
- ✓ Savings potential estimated

---

#### Phase 8: Gap & Risk Identification (2-3 hours)

**Objective:** Identify security, compliance, and operational gaps

**Gap Categories:**

**1. Inventory Gaps:**

- Services discovered through network/financial but not known to IT
- Shadow IT services
- Services without identified owners
- Services without contracts

**2. Classification Gaps:**

- Services with unknown data classification
- Services processing Restricted data without adequate controls
- Services with unclear data residency

**3. Criticality Gaps:**

- Critical services without exit plans
- Critical services with single vendor dependency
- Critical services without BC/DR plans

**4. Compliance Gaps:**

- Services processing GDPR data without DPA
- Services in non-compliant regions
- Services without required certifications (SOC 2, ISO 27001)

**5. Financial Gaps:**

- Services without contracts (compliance risk)
- Services with expired contracts
- Duplicate services (cost inefficiency)

**6. Exit Strategy Gaps:**

- Critical services with high lock-in risk
- Services without exit plans
- Services without tested data export

**Risk Register:**

For each gap, assess:

- **Risk:** What could go wrong?
- **Impact:** What's the consequence? (Low/Medium/High/Critical)
- **Likelihood:** How likely? (Low/Medium/High)
- **Risk Rating:** Impact × Likelihood
- **Remediation:** What needs to be done?
- **Owner:** Who's responsible?
- **Target Date:** When will it be fixed?

**Deliverable:**

- Gap analysis report
- Risk register with prioritized remediation plan
- Management escalation for critical gaps

**Quality Check:**

- ✓ All gap categories reviewed
- ✓ Risks assessed realistically (not downplayed)
- ✓ Remediation plans actionable
- ✓ Owners assigned
- ✓ Target dates set
- ✓ High/critical risks escalated to management

---

#### Phase 9: Evidence Registry (1-2 hours)

**Objective:** Organize all evidence for audit readiness

**Evidence Organization:**

Create structured evidence folders:
```
/Evidence/ISMS-IMP-A.5.23.S1/
  /Contracts/
    vendor_service_contract_YYYYMMDD.pdf
  /Invoices/
    vendor_service_invoice_YYYYMMDD.pdf
  /Screenshots/
    service_admin_console_YYYYMMDD.png
  /Exports/
    sso_user_list_YYYYMMDD.csv
  /Reports/
    discovery_network_traffic_YYYYMMDD.pdf
```

**Evidence Types:**

For each service category:

- **Procurement:** Contracts, POs, invoices
- **Financial:** Budget allocation, cost reports
- **Technical:** Screenshots, configuration exports, architecture diagrams
- **Compliance:** DPAs, certifications, audit reports
- **Operational:** User lists, usage reports, incident logs

**Evidence Registry (Sheet 10):**

Document each evidence item:

- Evidence ID (sequential: EV-INV-001, EV-INV-002, etc.)
- Service Name
- Evidence Type
- Description
- File Location
- Date Collected
- Collected By
- Verification Status

**Quality Check:**

- ✓ All evidence organized in standard folders
- ✓ Evidence registry complete
- ✓ File naming consistent
- ✓ Sensitive data redacted
- ✓ Evidence accessible to auditors

---

#### Phase 10: Review & Approval (2-4 hours)

**Objective:** Three-level approval process

See "Review & Approval" section (Part I, Section 7) for detailed process.

**Quick Summary:**

**Level 1: Technical Review** (IT Operations, Security)

- Verify inventory completeness
- Validate classifications
- Check technical accuracy

**Level 2: Compliance Review** (Compliance, Legal)

- Verify regulatory requirements
- Validate evidence quality
- Check gap analysis

**Level 3: Management Approval** (CIO, CISO, CFO)

- Review financial impact
- Approve gap remediation plans
- Accept residual risks

**Deliverable:**

- Approved assessment ready for compliance dashboard
- Signed approval form with all three levels
- Published inventory as authoritative source

---

## Completing Each Sheet

This section provides detailed guidance for completing each sheet in the workbook.

---

## Sheet 1: Service Inventory (Primary)

### Purpose

Create the master inventory of ALL cloud services. This is your "single source of truth" - every cloud service must be documented here.

### What to Document

For EACH cloud service:

- Service identification (name, vendor, type)
- Deployment details (status, model, region)
- Ownership (service owner, department, cost center)
- User metrics (total users, active users)
- Contract details (status, dates, procurement method)
- Initial classification (criticality, data type)

### Common Mistakes to Avoid

❌ **Incomplete discovery** - Missing shadow IT, free trials, or department-specific tools  
❌ **Vague service names** - "Cloud Storage" instead of "Dropbox Business for Marketing Department"  
❌ **Missing ownership** - No identified service owner  
❌ **Duplicate entries** - Same service listed multiple times under different names  
❌ **Ignoring decommissioned services** - Not tracking services being sunset  
❌ **No user counts** - Leaving user fields blank or using "Unknown"  

### How to Complete

**Step 1: List Every Service Discovered**

From your multi-method discovery (Phase 2), add each service to Sheet 1.

For each service, start with basics:

**Column A: Cloud Service Name**

- Use the name YOUR organization calls it (may differ from vendor's name)
- Be specific: "Microsoft 365 E5 for Enterprise" not just "Office 365"
- Include environment if applicable: "AWS Production Account" vs. "AWS Dev/Test Account"

**Good Examples:**

- ✅ "Salesforce Sales Cloud - EMEA Instance"
- ✅ "Zoom Enterprise Video - Global License"
- ✅ "Azure Production Subscription (West Europe)"

**Poor Examples:**

- ❌ "CRM" (too vague - which CRM?)
- ❌ "Cloud" (completely meaningless)
- ❌ "That thing Marketing uses" (not a service name)

**Column B: Service Type**

Classify the service (use dropdown):

| Type | Description | Examples |
|------|-------------|----------|
| **SaaS** | Software as a Service - complete applications | Salesforce, Office 365, Zoom, Slack, Workday |
| **IaaS** | Infrastructure as a Service - compute, storage, networking | AWS EC2/S3, Azure VMs, Google Compute Engine |
| **PaaS** | Platform as a Service - development platforms | Heroku, Azure App Service, Google App Engine |
| **Security Service** | Cloud-based security tools | CrowdStrike, Zscaler, Cloudflare, Okta |
| **Cloud Storage** | File storage and collaboration | Dropbox, Box, Google Drive, OneDrive |
| **Collaboration** | Communication and teamwork | Slack, Teams, Zoom, Webex, Miro |
| **Other** | Doesn't fit above categories (document in notes) | Specialized industry tools |

**If unsure:** Most business applications are SaaS. Most infrastructure is IaaS.

**Column C: Vendor Name**

Legal entity name, not brand name.

- ✅ "Salesforce, Inc." not "Salesforce.com"
- ✅ "Amazon Web Services, Inc." not "AWS"
- ✅ "Microsoft Corporation" not "MSFT"

Check the contract to get the legal entity name correct.

**Column D: Service Criticality**

Initial criticality rating (detailed assessment in Sheet 3):

| Criticality | Quick Test | Examples |
|-------------|-----------|----------|
| **Critical** | Organization stops if this fails within 4 hours | Email, CRM, payment processing, production infrastructure |
| **High** | Major disruption within 24 hours | Collaboration tools, HR systems, development platforms |
| **Medium** | Can work around for 1-3 days | Reporting tools, analytics, training platforms |
| **Low** | Minimal impact beyond 3 days | Test environments, archived data, optional tools |

**When in doubt:** Ask "Can we operate without this for a day?" If no, it's Critical or High.

**Column E: Data Classification**

Highest classification level of data processed (detailed assessment in Sheet 2):

| Classification | Quick Test | Examples |
|----------------|-----------|----------|
| **Restricted** | Personal health info, payment card data, trade secrets | HIPAA data, PCI data, R&D secrets |
| **Confidential** | Customer data, employee data, financial data | CRM, HR systems, accounting |
| **Internal** | Non-public business information | Internal wikis, project plans |
| **Public** | Publicly available information | Marketing sites, public docs |
| **N/A** | No organizational data | Pure infrastructure (empty VMs) |

**Conservative approach:** If unsure, classify as Confidential until verified.

**Column F: Data Residency Region**

Where is data stored/processed?

Use dropdown:

- Switzerland
- EU (specify country if known: Germany, Ireland, Netherlands, etc.)
- USA (specify region if known: us-east-1, us-west-2, etc.)
- Global / Multi-Region (data in multiple locations)
- Unknown (must investigate)

**Why this matters:** GDPR, Swiss FADP, and other regulations restrict where personal data can be stored.

**Column G: Contract Status**

Current contract state:

| Status | Meaning | Action Required |
|--------|---------|-----------------|
| **Active** | Under contract, fully licensed | Normal operations |
| **Renewal Due (≤90 days)** | Contract expiring soon | Start renewal process |
| **Expired** | Contract lapsed | Urgent: Renew or terminate |
| **Under Negotiation** | New contract being negotiated | Track to completion |
| **Trial** | Evaluation/POC, not production | Convert or cancel decision needed |
| **Decommissioning** | Being phased out | Track sunset timeline |

**Column H: Status**

Compliance assessment status (how well documented is this service?):

| Status | Meaning |
|--------|---------|
| ✅ **Compliant** | Fully documented, all required info collected, evidence available |
| ⚠️ **Partial** | Basic info present, but gaps exist (missing cost, owner, classification, etc.) |
| ❌ **Non-Compliant** | Major gaps - service discovered but minimal documentation |
| **N/A** | Not applicable (decommissioned, planned but not deployed) |

**Start with Partial for all services during initial inventory, update to Compliant as you collect details.**

**Columns I-Q: Standard Assessment Columns**

See "Base Columns" section in Part II for detailed specs. Key fields:

- **I: Evidence Location** - Path to contracts, invoices, screenshots
- **J: Gap Description** - What's missing? (if Status = Partial/Non-Compliant)
- **K: Remediation Needed** - Yes if gaps must be addressed
- **L: Exception ID** - Link to exception register if gap accepted
- **M: Risk ID** - Link to risk register if risk identified
- **N: Compensating Controls** - Mitigations if gaps exist
- **O: Service Owner** - Person accountable (name and email)
- **P: Target Remediation Date** - When gaps will be closed
- **Q: Last Review Date** - When this entry was last validated

**Extended Columns R-X (Inventory-Specific):**

See Sheet 1 specification in Part II for:

- R: Primary Use Case
- S: User Count (Total)
- T: User Count (Active - last 30 days)
- U: Annual Cost (CHF)
- V: Contract Start Date
- W: Contract End Date
- X: Procurement Method

**Step 2: Validate Completeness**

After entering all services:

1. **Cross-check discovery methods:**

   - All services from procurement → in inventory?
   - All services from SSO → in inventory?
   - All services from network traffic → in inventory?
   - All services from department surveys → in inventory?

2. **Check for common gaps:**

   - Development/test environments included?
   - Security tools included (EDR, SIEM, etc.)?
   - Backup/DR services included?
   - Infrastructure monitoring tools?
   - Identity providers (SSO, MFA)?

3. **Verify no duplicates:**

   - Same service listed under different names?
   - Same vendor appearing multiple times (consolidate?)

**Step 3: Identify Service Owners**

For every service, you MUST identify an owner:

**Owner Definition:**

- Person accountable for the service
- Makes decisions about service usage, renewal, decommissioning
- Budget authority (or influences budget)
- Escalation point for issues

**If owner unknown:**
1. Check who requested/purchased the service (procurement records)
2. Check who uses it most (SSO login data, license assignments)
3. Check department using the service (survey responses)
4. Escalate to department head to assign owner
5. As last resort: Default to IT Operations (but document that owner should be assigned)

**NEVER leave owner field blank.** If truly unknown, put "UNASSIGNED - ESCALATED TO [Department Head]"

**Step 4: Collect Financial Data**

For each service, obtain:

**Annual Cost:**

- Check most recent invoice
- Annualize if monthly/quarterly (monthly × 12)
- Include all licenses/seats
- Include support/maintenance if separate line item

**Contract Dates:**

- Contract Start Date: When did we first sign with vendor?
- Contract End Date: When does current commitment end?
- Renewal Date: If auto-renewal, when does it renew?

**Procurement Method:**

- Enterprise Agreement (multi-year, volume discount)
- Subscription (monthly/annual recurring)
- Pay-As-You-Go (usage-based, variable cost)
- Credit Card (ad-hoc purchase, no contract)
- Trial/Free (no payment)
- Bundled (part of larger agreement)

**Step 5: Initial User Count Estimate**

You need two numbers:

**Total Licensed Users:**

- How many licenses purchased?
- Check license agreement or invoice

**Active Users (Last 30 Days):**

- How many actually used the service recently?
- Check SSO login data
- Check service admin console usage reports
- If unknown, estimate conservatively (50% of licensed as a starting point)

**Why this matters:** Reveals over-licensing (wasted money) or under-licensing (compliance risk)

**Example:**

- Service: Zoom Enterprise
- Licensed Users: 500
- Active Users (30 days): 280
- **Finding:** Paying for 220 unused licenses → potential cost optimization

**Step 6: Document Evidence**

For each service (or at minimum, for Critical/High services):

Collect and store:

- **Contract:** MSA, DPA, SLA (if available)
- **Invoice:** Most recent invoice showing cost
- **Screenshot:** Admin console showing license count, active users, version
- **Purchase Order:** Original PO (if available)
- **Business Case:** Why was this service purchased? (if available)

Store in structured folders:
```
/Evidence/ISMS-IMP-A.5.23.S1/Services/[Vendor_Service_Name]/
  Contract_YYYYMMDD.pdf
  Invoice_YYYYMMDD.pdf
  Admin_Console_Screenshot_YYYYMMDD.png
  Purchase_Order_YYYYMMDD.pdf
```

Document evidence location in Column I: Evidence Location

Example: `/Evidence/A.5.23.1/Services/Salesforce_Sales_Cloud/`

### Common Scenarios

**Scenario 1: Shadow IT Discovered via Credit Card**

Discovery: Marketing Manager's credit card shows $299/month to "Canva Pro Teams"

**Assessment:**
1. Service Name: "Canva Pro Teams - Marketing Department"
2. Service Type: SaaS
3. Vendor: Canva Pty Ltd
4. Criticality: Low (design tool, not mission-critical)
5. Data Classification: Internal (marketing materials)
6. Contract Status: Subscription (monthly, no contract)
7. Service Owner: Marketing Manager
8. Annual Cost: CHF 3,588 ($299 × 12)
9. **Gap:** No IT approval, no data processing agreement
10. **Action:** Engage with Marketing - regularize or move to approved tool

**Scenario 2: Critical Service Without Owner**

Discovery: "Oracle Database Cloud" found in network traffic, critical production database

**Assessment:**
1. Service identified but no obvious owner
2. **Action Steps:**

   - Check who has admin access (database team)
   - Check who pays the bill (finance → trace to department)
   - Check application owners (who uses the database?)
   - Escalate to CTO if truly orphaned
   - **Temporary:** Assign to Database Manager pending clarification

**Scenario 3: Duplicate Services**

Discovery: Three different file sharing services found:

- Dropbox Business (IT-approved, 300 users)
- Box Enterprise (Engineering, 50 users)
- Google Drive Business (Marketing, 20 users)

**Assessment:**
1. Document all three separately in inventory
2. Flag in notes: "DUPLICATE CAPABILITY - CONSOLIDATION OPPORTUNITY"
3. Calculate total cost: Dropbox + Box + Google Drive = CHF 45,000/year
4. **Remediation:** Consolidate to single platform, potential savings CHF 20,000/year
5. Assign owner: IT Operations to lead consolidation project

**Scenario 4: Service in Decommissioning**

Discovery: "Lotus Notes" still showing in SSO, but migration to Office 365 underway

**Assessment:**
1. Service Name: "Lotus Notes (DECOMMISSIONING)"
2. Contract Status: Decommissioning
3. Status: Partial (still in use but being phased out)
4. **Document:**

   - Decommission target date
   - Migration plan reference
   - Remaining user count
   - When decommissioned, update Status to N/A but keep in inventory for historical record

### Evidence Examples

**Good Evidence:**

- Current contract with signatures and dates visible
- Invoice dated within last 90 days showing annual cost
- Admin console screenshot with service name, license count, active users visible
- SSO integration showing user list and last login dates
- Purchase order with budget approval

**Poor Evidence:**

- Unsigned contracts or drafts
- Invoices from 2+ years ago
- Generic marketing materials
- "I think we pay $X" without verification
- No evidence, just assumptions

### Quality Checklist

Before moving to Sheet 2, verify:

- [ ] All discovered services documented (100% coverage from discovery phase)
- [ ] No "Unknown" in Service Type or Vendor Name
- [ ] Every service has an owner (or escalated if unassigned)
- [ ] Financial data verified for Critical/High services (cross-checked with finance)
- [ ] User counts are reasonable estimates (not just "TBD")
- [ ] Contract status accurate (not assumed)
- [ ] Data residency documented (even if "Unknown" with plan to investigate)
- [ ] Evidence collected for top 20 highest-cost services
- [ ] No obvious duplicates (or duplicates flagged for remediation)
- [ ] Decommissioned services noted but still tracked

---

## Sheet 2: Data Classification Mapping

### Purpose

Document what data each cloud service processes. This is critical for regulatory compliance (GDPR, FADP), risk assessment, and incident response.

### What to Document

For EACH cloud service:

- Data types processed (personal, financial, health, etc.)
- Classification level (Restricted, Confidential, Internal, Public)
- Data residency details (storage location, processing location)
- Regulatory requirements applicable
- Data protection controls in place

### Common Mistakes to Avoid

❌ **Guessing classification** - "Probably Confidential" instead of verifying with service owner  
❌ **Underclassifying** - Marking CRM as "Internal" when it has customer PII (should be Confidential)  
❌ **Assuming no data** - "It's just infrastructure" (but what does it host?)  
❌ **Ignoring mixed data** - Service has both Public and Confidential data, but only documenting Public  
❌ **Not checking data residency** - Assuming data is in EU when it's actually in US  
❌ **Missing regulatory requirements** - Processing health data without noting HIPAA/privacy laws  

### How to Complete

**Step 1: Review Service Purpose**

For each service, understand:

- What is this service used for?
- What business process does it support?
- What data inputs does it receive?
- What data outputs does it produce?
- Where does data come from / go to?

**Interview service owner with these questions:**

**Step 2: Identify Data Types**

Check all that apply (multiple selections possible):

| Data Type | Description | Examples in Service |
|-----------|-------------|---------------------|
| **Personal Data** | Information about identifiable individuals | Names, emails, addresses, phone numbers, IP addresses |
| **Financial Data** | Payment and financial information | Credit cards, bank accounts, invoices, salaries |
| **Health Data** | Medical or health-related information | Medical records, health insurance, fitness data |
| **Intellectual Property** | Proprietary business information | Trade secrets, patents, R&D data, source code |
| **Customer Data** | Information about customers | CRM records, support tickets, purchase history |
| **Employee Data** | Information about employees | HR records, performance reviews, payroll |
| **Public Data** | Publicly available information | Marketing materials, public website content |
| **System/Logs** | Technical operational data | System logs, audit logs, performance metrics |

**Special Cases:**

**Mixed Data Services:**

- CRM with both customer data (Confidential) and marketing materials (Public)
- HR system with employee data (Confidential) and org chart (Internal)

→ Classify at HIGHEST level: Confidential

**No Organizational Data:**

- Empty cloud infrastructure (provisioned but not yet used)
- Development/test with synthetic data only

→ Classify as N/A, but document plan for production use

**Step 3: Apply Classification Level**

Based on identified data types, assign classification:

| Classification | Data Types Present | Protection Requirements |
|----------------|-------------------|-------------------------|
| **Restricted** | Health data, payment cards, trade secrets | Encryption required, strict access controls, audit logging, DLP |
| **Confidential** | Personal data, customer data, employee data, financial data | Encryption recommended, access controls, logging |
| **Internal** | Non-public business information | Access controls, basic logging |
| **Public** | Publicly available information only | Minimal protection |
| **Mixed** | Multiple classification levels | Treat as highest level present |

**Conservative Principle:** When in doubt, classify higher rather than lower.

**Step 4: Document Data Residency**

**Data Storage Location:**

- Primary: Where is data stored at rest? (geographic region)
- Backup: Where are backups stored?
- Disaster Recovery: Where are DR copies?

**Data Processing Location:**

- Where is data processed/computed? (may differ from storage)
- Are there cross-border data transfers?

**How to Verify:**
1. Check vendor documentation
2. Review contract (data processing addendum)
3. Check service admin console (region settings)
4. Ask vendor support if unclear

**Common Scenarios:**

**Example 1: Salesforce**

- Primary Storage: Germany (eu-central-1)
- Backup: Netherlands (eu-west-1)
- Processing: Germany
- Cross-Border: No (all within EU)
- **GDPR Compliant:** Yes

**Example 2: AWS S3**

- Primary Storage: us-east-1 (Virginia, USA)
- Backup: us-west-2 (Oregon, USA)
- Processing: USA
- Cross-Border: EU → USA transfer
- **GDPR Compliant:** Only if Standard Contractual Clauses (SCCs) in place

**Example 3: Global CDN**

- Storage: Global (replicated worldwide)
- Processing: Edge locations globally
- Cross-Border: Yes (everywhere)
- **Assessment:** Only suitable for Public data OR must review data processing agreement

**Step 5: Identify Regulatory Requirements**

Based on data types and residency, identify applicable regulations:

| Regulation | Applies If... | Key Requirements |
|------------|---------------|------------------|
| **GDPR** | EU personal data | Lawful basis, data minimization, breach notification, DPA required |
| **Swiss FADP** | Swiss personal data | Similar to GDPR, data export restrictions |
| **HIPAA** | US healthcare data | BAA required, encryption, audit logs, breach notification |
| **PCI-DSS** | Payment card data | No storage of CVV, encryption, tokenization, SAQ compliance |
| **SOX** | Financial reporting data (public companies) | Access controls, audit trails, change management |
| **Sector-Specific** | Banking, insurance, etc. | FINMA (CH banking), BaFin (DE banking), etc. |

**For each applicable regulation, verify:**

- ✅ Required vendor certifications (SOC 2, ISO 27001, etc.)
- ✅ Data processing agreement (DPA) in place
- ✅ Breach notification procedures defined
- ✅ Data retention policies compliant
- ✅ Data subject rights supported (GDPR: access, deletion, portability)

**Step 6: Assess Data Protection Controls**

For each service, verify:

**Encryption:**

- [ ] Data encrypted at rest (AES-256 or equivalent)
- [ ] Data encrypted in transit (TLS 1.2+ or equivalent)
- [ ] Key management documented

**Access Controls:**

- [ ] Multi-Factor Authentication (MFA) enforced
- [ ] Role-Based Access Control (RBAC) implemented
- [ ] Least privilege principle applied
- [ ] Access reviews conducted quarterly

**Logging & Monitoring:**

- [ ] Access logs retained ≥90 days
- [ ] Administrative actions logged
- [ ] Logs integrated with SIEM (if Critical/High)
- [ ] Alerts configured for anomalous activity

**Data Protection:**

- [ ] Data Loss Prevention (DLP) configured
- [ ] Data classification labels applied
- [ ] Backup/recovery tested
- [ ] Data deletion procedures defined

**Step 7: Document Gaps**

If data protection controls are missing:

**Identify:**

- What control is missing?
- Why is it missing? (technical limitation, cost, not implemented)
- What's the risk?

**Remediate:**

- What needs to be done?
- Who's responsible?
- What's the target date?
- Compensating controls in place?

**Example Gap:**

Service: Box Business (file sharing)

- **Gap:** No DLP configured
- **Risk:** Confidential documents could be shared externally without approval
- **Remediation:** Implement Box Shield (DLP add-on) or deploy third-party DLP
- **Owner:** IT Security
- **Target:** Q2 2026
- **Compensating Control:** User training on data handling policies

### Evidence Examples

**Good Evidence:**

- Data processing agreement (DPA) signed with vendor
- Admin console screenshot showing data residency settings
- Data flow diagram showing data sources and destinations
- Vendor certification (SOC 2 Type II showing controls)
- Export of data classification labels applied in service
- SIEM integration showing logs flowing

**Poor Evidence:**

- Vendor marketing claiming "we're GDPR compliant"
- Assumed data residency without verification
- Old DPA from 2019 (not current)
- No evidence, just "service owner says it's fine"

### Quality Checklist

- [ ] Every service from Sheet 1 has data classification assessed
- [ ] Data types identified (not assumed)
- [ ] Classification level justified (not guessed)
- [ ] Data residency verified (not assumed)
- [ ] Regulatory requirements identified
- [ ] Required agreements in place (DPAs, BAAs, etc.)
- [ ] Data protection controls assessed
- [ ] Gaps documented with remediation plans
- [ ] Evidence collected for Restricted/Confidential services

---

## Sheet 3: Service Criticality Assessment

### Purpose

Determine business impact if each service becomes unavailable. This drives BC/DR planning, SLA requirements, and resource allocation for incident response.

### What to Document

For EACH cloud service:

- Criticality rating (Critical, High, Medium, Low)
- Business impact description
- RTO (Recovery Time Objective) - how quickly must it recover?
- RPO (Recovery Point Objective) - how much data loss is acceptable?
- User impact (who is affected, how many users)
- Revenue impact (direct or indirect)
- Dependencies (what other services depend on this)

### Common Mistakes to Avoid

❌ **Over-rating criticality** - Everything marked "Critical" (dilutes the meaning)  
❌ **Under-rating criticality** - Customer-facing service marked "Low" because only 5 employees use it directly  
❌ **Ignoring dependencies** - Service rated Low but Critical service depends on it  
❌ **Confusing criticality with importance** - CEO's calendar tool marked Critical (it's important to CEO, but not Critical to organization)  
❌ **No RTO/RPO defined** - Just criticality rating without recovery targets  
❌ **Not considering customer impact** - Internal systems rated by employee convenience, not customer experience  

### How to Complete

**Step 1: Review Criticality Definitions**

Use consistent definitions across all services:

| Criticality | RTO | Business Impact | Protection Level |
|-------------|-----|-----------------|------------------|
| **Critical** | < 4 hours | Organization cannot operate. Revenue loss, customer SLA breach, regulatory violation, safety risk. | Maximum: 24/7 monitoring, automated failover, tested BC/DR plans |
| **High** | 4-24 hours | Significant disruption. Major workflow interruption, customer impact possible, but temporary workarounds exist. | High: Business hours monitoring, documented recovery procedures, tested annually |
| **Medium** | 1-3 days | Moderate impact. Workflow slowdowns, internal delays, but business continues. | Standard: Standard monitoring, recovery procedures documented |
| **Low** | > 3 days | Minimal impact. Convenience features, "nice to have" but not essential. | Basic: Best-effort recovery |

**Step 2: Assessment Questions**

For each service, ask service owner:

**Impact Questions:**

1. **What happens if this service goes down for 1 hour?**

   - No impact → Low
   - Minor inconvenience → Medium
   - Workflow disruption → High
   - Revenue/customer/safety impact → Critical

2. **Can we operate the business without this service for 1 day?**

   - Yes, no problem → Low/Medium
   - Yes, but with significant manual workarounds → High
   - No, business stops → Critical

3. **Is this service customer-facing or directly revenue-generating?**

   - Yes, customers directly affected → High or Critical
   - No, internal only → Medium or lower (unless dependencies exist)

4. **How many people are affected if this service is down?**

   - < 10 users, low impact → Typically Medium or lower
   - 10-50 users, moderate impact → Medium to High
   - 50+ users or entire departments → High or Critical
   - Customers affected → Critical (regardless of internal user count)

5. **Are there dependencies?**

   - Do Critical services depend on this service? → Increase rating
   - Does this service depend on Low-priority services? → Note risk

**Impact Categories:**

Assess impact across multiple dimensions:

| Dimension | Critical Impact | High Impact | Medium Impact | Low Impact |
|-----------|----------------|-------------|---------------|------------|
| **Revenue** | Direct revenue loss > CHF 10K/day | Revenue impact CHF 1K-10K/day | Indirect/future revenue risk | No revenue impact |
| **Customers** | Customer SLA breach, service unavailable | Customer inconvenience, degraded service | Internal inefficiency | No customer impact |
| **Operations** | Business stops | Major process disruption | Workflow slowdown | Minor inconvenience |
| **Reputation** | Public incident, media coverage | Customer complaints | Internal frustration | No reputation impact |
| **Compliance** | Regulatory violation, fines | Audit finding potential | Documentation gap | No compliance impact |
| **Safety** | Safety risk to people | Property damage potential | Equipment risk | No safety impact |

**If ANY dimension shows Critical impact → service is Critical overall.**

**Step 3: Define RTO and RPO**

**RTO (Recovery Time Objective):** How quickly must service be restored?

| Criticality | Typical RTO | Example |
|-------------|-------------|---------|
| Critical | 1-4 hours | Email service: Must be up within 4 hours |
| High | 4-24 hours | HR system: Can wait until next business day |
| Medium | 1-3 days | Reporting tool: Can wait a few days |
| Low | > 3 days | Training platform: Restore when possible |

**RPO (Recovery Point Objective):** How much data loss is acceptable?

| Criticality | Typical RPO | Example |
|-------------|-------------|---------|
| Critical | Near-zero (continuous backup) | CRM: Can't lose customer transactions |
| High | < 24 hours | Project management: Yesterday's work acceptable loss |
| Medium | < 7 days | Analytics: Last week's data acceptable |
| Low | Best effort | Test environments: Rebuild from scratch acceptable |

**Document both RTO and RPO for each service.**

**Step 4: Map Dependencies**

Identify:

**Upstream Dependencies** (services this service depends on):

- Identity/SSO (Entra ID, Okta)
- Network connectivity
- Database backends
- Integration platforms
- Payment gateways

**Downstream Dependencies** (services that depend on this service):

- Applications using this as data source
- Automated workflows triggered by this service
- Reporting dashboards pulling data from this service

**Dependency Risk:**

If a Low-criticality service is a dependency for a Critical service, the Low service effectively becomes High or Critical.

**Example:**

- Service: PostgreSQL Database (hosts CRM data)
- Direct Criticality: Medium (database alone, no users)
- Downstream Dependency: Salesforce CRM (Critical)
- **Effective Criticality: Critical** (because CRM depends on it)

**Step 5: Assess BC/DR Readiness**

For Critical and High services, verify:

**Backup:**

- [ ] Automated backups configured
- [ ] Backup frequency meets RPO
- [ ] Backups tested (restore test in last 90 days)
- [ ] Backups stored in geographically separate location

**Disaster Recovery:**

- [ ] DR plan documented
- [ ] Failover procedures tested
- [ ] DR environment exists (if applicable)
- [ ] DR RTO tested and validated

**High Availability:**

- [ ] Redundant components (no single points of failure)
- [ ] Multi-region deployment (for Critical services)
- [ ] Load balancing configured
- [ ] Automated health checks and failover

**Incident Response:**

- [ ] Incident response procedures documented
- [ ] On-call rotation defined (for Critical services)
- [ ] Escalation paths clear
- [ ] Communication plan defined (who to notify, how)

**Gap Identification:**

If BC/DR requirements not met:

- **Gap:** What's missing?
- **Risk:** What could happen?
- **Remediation:** What needs to be done?
- **Owner:** Who's responsible?
- **Target Date:** When will it be addressed?

**Example Gap:**

Service: Salesforce CRM (Critical)

- **Gap:** No tested DR failover in last 12 months
- **Risk:** If primary instance fails, uncertain if DR will work, could exceed 4-hour RTO
- **Remediation:** Schedule DR test for Q1 2026, document results
- **Owner:** IT Operations Manager
- **Target:** 31.03.2026
- **Compensating Control:** Vendor (Salesforce) has 99.9% uptime SLA, multi-AZ by default

### Common Scenarios

**Scenario 1: Customer-Facing Service**

Service: E-commerce Website (hosted on AWS)

**Assessment:**

- **Criticality:** Critical
- **Why:** Direct revenue impact, customers cannot purchase if down
- **RTO:** 1 hour (revenue loss CHF 5K/hour)
- **RPO:** Near-zero (cannot lose customer orders)
- **Users Affected:** All customers (B2C, thousands daily)
- **Revenue Impact:** Direct - CHF 120K/day
- **Dependencies:** Payment gateway (Critical), Product database (Critical), CDN (High)
- **BC/DR:** Multi-region deployment, automated failover, tested quarterly
- **Status:** ✅ Compliant

**Scenario 2: Internal Tool with Critical Dependencies**

Service: Shared File Server (Windows File Server on Azure)

**Initial Assessment:**

- **Direct Criticality:** Medium (file storage, mostly convenience)
- **Users:** 200 employees

**Dependency Analysis:**

- Engineering uses this for build artifacts → CI/CD pipeline depends on it
- Finance uses this for invoice processing → Accounts Payable depends on it
- **Critical Workflow Impact:** Software releases blocked, invoices can't be paid

**Revised Assessment:**

- **Effective Criticality:** High (upgraded due to critical dependencies)
- **RTO:** 8 hours (can work around for half a day, but not longer)
- **RPO:** 24 hours (yesterday's files acceptable)
- **Remediation:** Migrate critical workflows off file server OR upgrade to HA configuration

**Scenario 3: Overrated Service**

Service: CEO Calendar (Outlook Calendar)

**Initial Assessment (by Executive Assistant):**

- **Criticality:** Critical (CEO needs calendar!)

**Objective Assessment:**

- **Business Impact Test:** If CEO's calendar is down for 4 hours, does business stop?
  - Answer: No. CEO inconvenienced, but organization continues.
- **Customer Impact:** No customer impact
- **Revenue Impact:** No direct revenue impact
- **Regulatory Impact:** No compliance issues

**Correct Assessment:**

- **Criticality:** High (important person, but not Critical to organization operations)
- **RTO:** 8 hours (within business day)
- **RPO:** 1 hour (recent appointments critical)

**Scenario 4: Seasonal Criticality**

Service: Tax Reporting Software

**Assessment:**

- **Baseline Criticality:** Low (used 2 months/year)
- **Seasonal Criticality (Jan-Feb):** Critical (must file taxes by deadline)
- **RTO (Seasonal):** 24 hours (filing deadline cannot be missed)
- **RTO (Off-Season):** > 7 days (can wait)

**Documentation:**

- Mark as: Medium (average criticality across year)
- Note: "SEASONAL CRITICAL: Jan-Feb tax filing season, RTO 24 hours during this period"
- Ensure BC/DR tested before tax season begins

### Evidence Examples

**Good Evidence:**

- Business impact analysis (BIA) document
- RTO/RPO documented in service catalog
- BC/DR test results (last 12 months)
- Incident response procedures
- SLA agreement showing uptime requirements
- Dependency map/diagram
- Interview notes with service owner confirming impact assessment

**Poor Evidence:**

- "Everyone knows this is critical" (no documentation)
- Criticality assigned without impact assessment
- No RTO/RPO defined
- BC/DR plan exists but never tested
- Generic "very important" descriptions

### Quality Checklist

- [ ] Every service has criticality rating assigned
- [ ] Criticality justified with business impact description
- [ ] RTO and RPO defined for all Critical/High services
- [ ] User impact quantified (number of users, customer-facing yes/no)
- [ ] Revenue impact assessed (direct or indirect)
- [ ] Dependencies mapped (upstream and downstream)
- [ ] BC/DR readiness assessed for Critical/High services
- [ ] Gaps documented with remediation plans
- [ ] Service owners agree with criticality ratings
- [ ] No inflation (not everything is Critical)
- [ ] Evidence collected for Critical services

---

## Sheet 4: Exit Feasibility & Strategy Assessment

### Purpose

Assess how easily [Organization] could exit each cloud service if needed. This is CRITICAL for avoiding vendor lock-in, maintaining negotiation leverage, and ensuring business continuity if vendor fails or terms become unacceptable.

Per **ISMS-POL-A.5.19-23-S5 Section 8.1.1**, every cloud service must have an assessed exit strategy following one of three paths:
1. **Cloud-to-Cloud** (migrate to alternative provider) - 90%+ of services
2. **Hybrid** (partial on-premises repatriation) - 5-10% of services
3. **On-Premises** (full build-back) - <5% of services (only when justified)

### What to Document

For EACH cloud service:

- Exit strategy type (Cloud-to-Cloud, Hybrid, On-Premises, Not Yet Determined)
- Data portability assessment
- Alternative providers identified
- Vendor lock-in risks
- Exit plan status
- Migration complexity and cost estimates
- **For Hybrid exits:** Workload segmentation, data sync requirements
- **For On-Premises exits:** TCO analysis, infrastructure requirements, staffing needs

### Common Mistakes to Avoid

❌ **Assuming on-premises is default** - Reality: On-prem economically justified in <5% of cases  
❌ **Not testing data export** - Assuming export works without actually trying it  
❌ **Ignoring vendor lock-in** - Deep proprietary integrations not documented  
❌ **No exit plans for Critical services** - Policy requires exit plans for Critical/High services  
❌ **Underestimating exit costs** - "Just export the data" (ignoring reconfiguration, testing, training)  
❌ **Missing hybrid complexity** - Assuming hybrid is "easy middle ground" (it's often more complex than full cloud)  

### How to Complete

**Step 1: Determine Exit Strategy Type**

For each service, select the most appropriate exit strategy using the decision framework from **Policy Section 8.1.1.4**:

```
DECISION TREE:

1. Is there a regulatory mandate for on-premises infrastructure?
   YES → On-Premises or Hybrid
   NO → Continue to Q2

2. Is cloud cost > CHF 500K/year AND workload stable/predictable?
   NO → Cloud-to-Cloud (default)
   YES → Continue to Q3

3. Would on-premises TCO be < 70% of cloud cost over 5 years?
   YES → Consider On-Premises (run full TCO analysis)
   NO → Cloud-to-Cloud

4. If considering Hybrid: Can workload be cleanly segmented?
   YES → Hybrid viable
   NO → Cloud-to-Cloud or On-Premises only
```

**Exit Strategy Profiles:**

| Exit Type | When to Use | Typical Timeline | Cost Range (5-year TCO) |
|-----------|-------------|------------------|------------------------|
| **Cloud-to-Cloud** | 90%+ of services, DEFAULT for most scenarios | 3-6 months | CHF 50K-500K+ OPEX/year |
| **Hybrid** | Data sovereignty for some data, latency-sensitive workloads, staged migration | 6-12 months | CHF 95K-700K CAPEX + CHF 80K-300K/year OPEX |
| **On-Premises** | Regulatory mandate, cost inversion (cloud > CHF 500K/year AND on-prem TCO < 70%), strategic independence | 9-18 months | CHF 390K-990K CAPEX + CHF 470K-1.11M/year OPEX |

**⚠️ CRITICAL PRINCIPLE:** On-premises repatriation is economically justified in **<5% of scenarios**. Do not default to on-premises without rigorous TCO analysis.

**Step 2: Assess Data Portability**

For each service, evaluate how easily data can be extracted:

**Export Format Available:**

| Format | Portability | Examples |
|--------|-------------|----------|
| **Standard (CSV/JSON/XML)** | ✅ High | Easy to import into alternative systems |
| **Proprietary** | ⚠️ Medium | Vendor-specific format, conversion needed |
| **API Only** | ⚠️ Medium | Programmatic extraction, development needed |
| **None** | ❌ Low | No export capability, vendor lock-in |

**Export Testing:**

Don't assume - ACTUALLY TEST data export:

1. **Locate export function** in admin console
2. **Export sample data** (10-20% of dataset for large services)
3. **Verify completeness:**

   - All fields included?
   - Metadata preserved?
   - Relationships intact?
   - Audit trails included?

4. **Test import** into alternative system (if alternative identified)
5. **Document:**

   - Export procedure
   - File format
   - Data completeness
   - Any limitations

**Data Volume:**

Document:

- Current data volume (GB or TB)
- Growth rate (per month/year)
- Estimated volume at exit time (project forward)

**Why this matters:** Export time and migration complexity scale with data volume.

**Migration Complexity:**

Rate the overall difficulty of migrating data:

| Complexity | Characteristics | Examples |
|------------|----------------|----------|
| **Low** | Standard formats, clean data, simple schema | Email (IMAP export), file storage (download folders) |
| **Medium** | Some custom fields, moderate transformations needed | CRM with custom objects, project management tools |
| **High** | Complex schema, many custom fields, significant transformations | ERP systems, custom-developed applications |
| **Very High** | Deeply integrated, proprietary formats, no clear migration path | Highly customized platforms, embedded workflows |

**Step 3: Cloud-to-Cloud Exit Assessment**

For services with **Cloud-to-Cloud** exit strategy (90%+ of services):

**Alternative Providers Identified:**

Minimum requirement: Identify **2+ alternative providers** that could provide similar functionality.

**Example:**

Current Service: Salesforce Sales Cloud

Alternative Options:
1. Microsoft Dynamics 365 Sales
2. HubSpot Enterprise CRM
3. Zoho CRM Plus

**Assessment Criteria:**

For each alternative:

- ✅ **Service Parity:** Provides comparable features?
- ✅ **Data Portability:** Can import from current service?
- ✅ **Integration Compatibility:** Supports required integrations?
- ✅ **Cost Comparison:** Comparable or lower TCO?
- ✅ **Certification Alignment:** Has required certifications (SOC 2, ISO 27001)?

**Migration Estimate:**

Document estimated:

- **Timeline:** 3-6 months typical for cloud-to-cloud
  - Assessment & Planning: 2-4 weeks
  - Data Migration & Testing: 4-12 weeks
  - Cutover & Validation: 2-4 weeks
- **Cost:** CHF 50K-500K+ depending on service complexity
  - New service setup and licensing
  - Data migration tools/services
  - Integration reconfiguration
  - User training
  - Parallel running costs (during migration)

**Step 4: Hybrid Exit Assessment**

For services with **Hybrid** exit strategy (5-10% of services):

**When Hybrid Makes Sense:**

✅ Data sovereignty requirement (some data must be on-premises)  
✅ Extreme latency sensitivity (real-time processing needs local compute)  
✅ Existing on-premises capacity available  
✅ Workload can be cleanly segmented (app in cloud, database on-prem OR vice versa)  

**Workload Segmentation:**

Document which components go where:

**Example: Hybrid CRM Deployment**

| Component | Location | Rationale |
|-----------|----------|-----------|
| **Application Layer** | Cloud (SaaS CRM) | Low latency requirement, benefits from cloud updates |
| **Customer Database** | On-Premises | Data sovereignty requirement (FADP compliance) |
| **Reporting/Analytics** | Cloud | Compute-intensive, benefits from cloud elasticity |
| **Integration Layer** | Hybrid (VPN/Direct Connect) | Bridges cloud app to on-prem database |

**Data Synchronization Requirements:**

For hybrid deployments, assess:

**Latency Requirements:**

- < 100ms: Excellent (real-time sync possible)
- 100-500ms: Acceptable (near real-time)
- > 500ms: Concern (may require async sync, potential consistency issues)

**Synchronization Mechanism:**

- Real-Time Replication (database mirroring)
- Batch Sync (hourly, daily)
- Manual Transfer (not recommended for production)

**Hybrid Connectivity:**

Required infrastructure:

- **VPN:** Basic connectivity (typically 100-500 Mbps)
- **Direct Connect / ExpressRoute:** High-speed dedicated link (1-10 Gbps)
- **SD-WAN:** Software-defined networking for optimized routing

**Cost:** CHF 1K-10K/month for dedicated connectivity

**Hybrid TCO (3-5 year):**

| Component | CAPEX | OPEX (Annual) | 5-Year TCO |
|-----------|-------|---------------|------------|
| **Infrastructure** | CHF 95K-700K | - | CHF 95K-700K |
| **Connectivity** | CHF 0 | CHF 12K-120K | CHF 60K-600K |
| **Cloud Components** | CHF 0 | CHF 50K-150K | CHF 250K-750K |
| **Staffing (3-5 FTE)** | CHF 0 | CHF 180K-450K | CHF 900K-2.25M |
| **TOTAL** | CHF 95K-700K | CHF 242K-720K | CHF 1.31M-4.30M |

**Hybrid Complexity Factors:**

⚠️ Increased management overhead (two environments to maintain)  
⚠️ Data consistency challenges (sync delays, conflict resolution)  
⚠️ Security boundaries (cloud-to-on-prem trust relationships)  
⚠️ Disaster recovery complexity (must protect both environments)  

**Step 5: On-Premises Exit Assessment**

For services with **On-Premises** exit strategy (<5% of services):

**⚠️ WARNING:** On-premises repatriation is **RARELY** economically justified. Complete rigorous TCO analysis before proceeding.

**Justification Required:**

On-premises exit only justified if:

✅ **Regulatory Mandate:** Air-gapped infrastructure legally required (defense, critical infrastructure)  
✅ **Cost Inversion:** Cloud cost > CHF 500K/year AND on-prem 5-year TCO < 70% of cloud  
✅ **Strategic Independence:** National security or critical infrastructure concerns  
✅ **Concentration Risk:** DORA Article 28.9 concentration risk that cannot be mitigated through multi-cloud  

**On-Premises TCO Analysis:**

**CAPEX (Initial Investment):**

| Component | Range | Notes |
|-----------|-------|-------|
| **Compute** | CHF 150K-300K | ~50 VMs worth of server hardware |
| **Storage** | CHF 50K-150K | ~100TB usable storage (SAN/NAS) |
| **Network** | CHF 40K-80K | Switches, firewalls, load balancers |
| **Facilities** | CHF 0-100K | If new datacenter space needed |
| **Software Licenses** | CHF 20K-50K | Virtualization, management tools |
| **Professional Services** | CHF 50K-100K | Migration, configuration, testing |
| **Security Tools** | CHF 30K-60K | Firewalls, IDS/IPS, backup systems |
| **Contingency (20%)** | CHF 80K-200K | Buffer for unexpected costs |
| **TOTAL CAPEX** | **CHF 420K-1.04M** | One-time investment |

**OPEX (Annual Recurring):**

| Component | Annual Cost | Notes |
|-----------|-------------|-------|
| **Staffing (4.5-7.0 FTE)** | CHF 450K-790K | Sys admin, network, security, DBA roles |
| **Power & Cooling** | CHF 15K-40K | Datacenter operating costs |
| **Facilities/Colocation** | CHF 20K-60K | If not owned datacenter |
| **Software Maintenance** | CHF 40K-100K | Support contracts (15-20% of license cost) |
| **Hardware Refresh (3-5 year)** | CHF 60K-120K | Amortized replacement costs |
| **Backup/DR** | CHF 20K-50K | Off-site backup, DR testing |
| **Security Services** | CHF 30K-80K | Security monitoring, pen testing |
| **Network Connectivity** | CHF 10K-30K | Internet, WAN links |
| **Training** | CHF 10K-30K | Staff skill development |
| **Contingency (10%)** | CHF 50K-130K | Unexpected operational costs |
| **TOTAL OPEX** | **CHF 705K-1.43M/year** | Ongoing annual costs |

**5-Year TCO Comparison:**

| Scenario | CAPEX | OPEX (5 years) | Total 5-Year TCO |
|----------|-------|----------------|------------------|
| **Cloud (baseline)** | CHF 0 | CHF 2.5M-5.0M | CHF 2.5M-5.0M |
| **On-Premises** | CHF 420K-1.04M | CHF 3.53M-7.15M | CHF 3.95M-8.19M |
| **Difference** | - | - | +CHF 1.45M-3.19M (58-64% MORE expensive) |

**Conclusion:** On-premises is typically **60-200% MORE expensive** than cloud over 5 years.

**On-premises only cheaper if:**

- Cloud cost > CHF 1M/year (very large deployments)
- AND workload extremely stable (no elasticity benefit from cloud)
- AND staff already exist (not incremental hires)
- AND datacenter space already exists (no new CAPEX)

**Infrastructure Requirements:**

If proceeding with on-premises:

**Compute:**

- vCPU requirements: _____ cores
- Memory requirements: _____ GB RAM
- Storage IOPS: _____ IOPS
- Virtualization platform: VMware ESXi / Hyper-V / KVM / Other

**Storage:**

- Capacity: _____ TB usable
- Performance tier: SSD / HDD / Hybrid
- Redundancy: RAID 10 / RAID 6 / Erasure Coding
- Backup: On-site + off-site

**Network:**

- Bandwidth: _____ Gbps
- Redundancy: Dual uplinks, diverse paths
- Security: Firewalls, IDS/IPS, segmentation

**Staffing Requirements:**

| Role | FTE | Annual Cost (CHF) | Responsibilities |
|------|-----|-------------------|------------------|
| **System Administrator** | 2.0 | 180K-220K | Server management, OS patching, monitoring |
| **Network Engineer** | 1.0 | 100K-130K | Network config, troubleshooting, security |
| **Security Specialist** | 1.0 | 110K-150K | Security monitoring, incident response |
| **Database Administrator** | 0.5 | 60K-90K | Database tuning, backup, recovery |
| **Storage Administrator** | 0.5 | 50K-80K | SAN/NAS management, capacity planning |
| **Manager/Lead** | 0.5 | 60K-120K | Team leadership, vendor management |
| **TOTAL** | **5.5 FTE** | **CHF 560K-790K/year** | Full operational team |

**⚠️ Staffing is the LARGEST cost component** (70-80% of OPEX).

**Technology Refresh:**

On-premises infrastructure requires refresh every 3-5 years:

- Servers: 3-4 years
- Storage: 4-5 years
- Network: 5-7 years

Budget CHF 60K-120K/year for ongoing refresh (amortized).

**Risks of On-Premises:**

⚠️ **Technology Debt:** Infrastructure ages, falls behind cloud capabilities  
⚠️ **Capacity Planning:** Must over-provision (can't scale elastically)  
⚠️ **Elasticity Loss:** Can't handle traffic spikes without over-investment  
⚠️ **Skills Retention:** Staff turnover risk, knowledge concentration  
⚠️ **Single Points of Failure:** Unless significant investment in redundancy  
⚠️ **Compliance Burden:** Must maintain certifications internally (SOC 2, ISO 27001 for datacenter)  

**Step 6: Exit Plan Status**

For **Critical and High** criticality services, document exit plan status:

| Status | Meaning | Required Actions |
|--------|---------|------------------|
| **Documented** | Full exit plan exists, tested, ready to execute | Annual review and update |
| **Draft** | Exit plan in progress | Complete within 90 days |
| **Not Started** | No exit plan (NON-COMPLIANT for Critical/High) | URGENT: Create exit plan |
| **N/A** | Service criticality Low/Medium, exit plan not required | Optional: Create if concentration risk exists |

**Exit Plan Contents (for Documented status):**

Must include:
1. Exit triggers (when would we execute exit?)
2. Alternative providers identified (2+ options assessed)
3. Data export procedures documented and tested
4. Migration timeline estimated (with milestones)
5. Resource requirements identified (staff, budget, tools)
6. Communication plan (stakeholder notification)
7. Rollback plan (if migration fails)
8. Post-migration validation criteria

**Step 7: Vendor Lock-In Risk Assessment**

Assess factors that could prevent or complicate exit:

**Lock-In Factors:**

| Factor | High Risk | Medium Risk | Low Risk |
|--------|-----------|-------------|----------|
| **Data Format** | Proprietary, no export | Proprietary with conversion tools | Standard formats (CSV, JSON) |
| **APIs** | Proprietary, no alternatives | REST API but vendor-specific | Standard protocols (IMAP, CalDAV) |
| **Integrations** | Deep custom integrations, hundreds of connections | Moderate integrations, documented | Minimal integrations, standard connectors |
| **Custom Development** | Significant custom code on platform | Some customizations | Out-of-box configuration only |
| **Training Investment** | Extensive specialized training, certifications | Moderate training | Minimal training, intuitive |
| **Contract Terms** | Multi-year lock-in, high exit penalties | 1-year terms, moderate penalties | Monthly/annual, no penalties |
| **Data Volume** | > 10TB | 1-10TB | < 1TB |
| **User Count** | > 500 users | 100-500 users | < 100 users |

**Lock-In Risk Rating:**

- **Low:** 0-2 high-risk factors → Exit feasible within 3-6 months
- **Medium:** 3-4 high-risk factors → Exit difficult, 6-12 months
- **High:** 5-6 high-risk factors → Exit very difficult, 12-18 months
- **Critical:** 7+ high-risk factors → Effectively locked in, >18 months or rebuild required

**Mitigation Strategies:**

For high lock-in risks:

- ✅ Negotiate contract exit clauses (termination for convenience, data portability guaranteed)
- ✅ Maintain integration abstraction layer (don't integrate directly, use middleware)
- ✅ Export data regularly (quarterly backups to standard formats)
- ✅ Document all customizations (version control, architecture diagrams)
- ✅ Cross-train staff (reduce vendor-specific skill dependency)
- ✅ Evaluate alternatives annually (maintain awareness of exit options)

**Step 8: Annual Exit Strategy Review**

**Policy Requirement:** Exit strategies must be reviewed annually.

For each service:

- [ ] Alternative providers re-evaluated (are there better options now?)
- [ ] Data export tested (verify export still works)
- [ ] Cost comparison updated (cloud vs. alternatives vs. on-prem)
- [ ] Regulatory changes assessed (new data residency requirements?)
- [ ] Technology changes considered (new migration tools available?)
- [ ] Contract terms reviewed (approaching renewal? renegotiate exit terms?)
- [ ] Organizational changes (business strategy shift affecting cloud usage?)

**Testing Requirements (by Service Criticality):**

| Criticality | Testing Scope | Frequency |
|-------------|---------------|-----------|
| **Critical** | Full simulation: Export 100% data, deploy on alternative provider (test environment) | Annual |
| **High** | Sample test: Export 50% data, verify import on alternative | Annual |
| **Medium** | Sample test: Export 10-20% data, verify completeness | Annual |
| **Low** | Documentation review only | Biennial |

**Evidence:** Document test results, store export files, screenshot alternative provider import.

### Common Scenarios

**Scenario 1: SaaS with Good Exit Path (Cloud-to-Cloud)**

Service: Zoom Video Communications

**Assessment:**

- **Exit Strategy Type:** Cloud-to-Cloud
- **Alternative Providers:** Microsoft Teams, Cisco Webex, Google Meet
- **Data Portability:** High (recordings can be downloaded, user lists exported to CSV)
- **Export Tested:** Yes (exported 100 sample recordings, all metadata intact)
- **Data Volume:** 500GB recordings
- **Migration Complexity:** Low (users can use alternative immediately)
- **Lock-In Risk:** Low (minimal custom integrations, monthly billing, standard features)
- **Migration Estimate:** 1-2 months, CHF 20K (reconfiguration, user training)
- **Exit Plan Status:** Documented (alternatives identified, tested exports)
- **Status:** ✅ Compliant

**Scenario 2: IaaS with Hybrid Strategy (Cloud + On-Prem)**

Service: Azure VM Workloads (Development Environments)

**Assessment:**

- **Exit Strategy Type:** Hybrid
- **Rationale:** Dev/test in cloud (elasticity), production database on-premises (data sovereignty)
- **Workload Segmentation:**
  - Cloud: Application servers, test databases, CI/CD pipelines
  - On-Premises: Production database, sensitive data processing
- **Data Sync:** Batch (nightly database refresh from prod to dev)
- **Connectivity:** Azure ExpressRoute (1 Gbps dedicated link)
- **Hybrid TCO (5-year):** CHF 1.8M (vs. CHF 2.2M all-cloud, CHF 3.5M all on-prem)
- **Migration Estimate:** 6-9 months, CHF 150K
- **Status:** Draft (plan in progress, connectivity being provisioned)

**Scenario 3: On-Premises Repatriation - REJECTED (TCO Analysis)**

Service: AWS EC2 Production Workloads (100 VMs)

**Initial Request:** "Cloud is too expensive, let's build back on-prem"

**TCO Analysis:**

Current Cloud Cost: CHF 480K/year

On-Premises Cost Estimate:

- CAPEX: CHF 650K (servers, storage, network)
- OPEX: CHF 720K/year (5.5 FTE staff + facilities + maintenance)
- 5-Year TCO: CHF 4.25M

Cloud 5-Year TCO: CHF 2.4M

**Result:** On-premises is **77% MORE expensive** (CHF 1.85M additional cost)

**Decision:** REJECT on-premises repatriation, maintain cloud deployment

**Alternative Actions:**

- ✅ Right-size VMs (identified 30% over-provisioned → save CHF 144K/year)
- ✅ Use reserved instances (3-year commit → save 40% = CHF 192K/year)
- ✅ Implement auto-scaling (reduce off-peak capacity → save CHF 60K/year)
- **Total Savings:** CHF 396K/year (82% of current cost)

**Revised Cloud TCO (optimized):** CHF 1.01M (5-year)

**Conclusion:** Cloud-to-cloud optimization vastly superior to on-prem repatriation.

**Scenario 4: Lock-In with Remediation**

Service: Salesforce Sales Cloud (Highly Customized)

**Assessment:**

- **Exit Strategy Type:** Cloud-to-Cloud (but difficult)
- **Lock-In Factors:**
  - Proprietary Apex code (500+ custom classes)
  - Deep integrations (15 systems connected)
  - Custom Lightning components
  - 5-year enterprise agreement (2 years remaining)
- **Lock-In Risk:** High
- **Data Portability:** Medium (standard export available, but complex schema)
- **Migration Estimate:** 12-18 months, CHF 500K-800K
- **Alternative:** Microsoft Dynamics 365, HubSpot Enterprise (both require significant customization)

**Remediation Plan:**

- ✅ Document all customizations (architecture diagrams, code repository)
- ✅ Reduce custom code (replace with standard features where possible)
- ✅ Quarterly data exports (maintain export capability)
- ✅ Integration abstraction layer (use middleware, not direct SFDC→System connections)
- ✅ Negotiate contract: Add "termination for convenience" clause at next renewal
- ✅ Annual alternative provider review
- **Target:** Reduce lock-in risk from High to Medium by next renewal (2027)

### Evidence Examples

**Good Evidence:**

- Data export test results (screenshots of export process, file samples)
- Alternative provider evaluation matrix (side-by-side comparison)
- TCO analysis spreadsheet (5-year comparison: cloud vs. hybrid vs. on-prem)
- Exit plan document (trigger events, migration timeline, resource requirements)
- Hybrid architecture diagram (workload segmentation, data flows)
- Contract clauses guaranteeing data portability
- Annual exit test reports

**Poor Evidence:**

- "We could probably export if we needed to" (no actual test)
- Vendor marketing claiming "easy migration"
- Exit plan from 3 years ago never updated
- TCO analysis missing staffing costs (largest OPEX component)
- No hybrid connectivity assessment (ignoring sync latency)
- Assuming on-prem cheaper without doing math

### Quality Checklist

- [ ] All services have exit strategy type assigned (Cloud-to-Cloud/Hybrid/On-Prem)
- [ ] Data export capabilities TESTED (not assumed)
- [ ] Alternative providers identified (2+ for Critical/High services)
- [ ] Lock-in risks assessed honestly (not downplayed)
- [ ] TCO analysis completed for any On-Premises exit (prove it's cheaper)
- [ ] Hybrid workload segmentation documented (clear boundaries)
- [ ] Exit plans documented for Critical/High services
- [ ] Annual testing schedule established
- [ ] Gaps documented with remediation plans
- [ ] Evidence collected (export tests, alternative evaluations, TCO analysis)

---

## Sheet 5: Financial Summary & Cost Optimization

### Purpose

Consolidate financial data for all cloud services, analyze spending patterns, identify cost optimization opportunities, and track contract renewals.

### What to Document

- Total cloud spend (by category, department, vendor)
- Top 10 most expensive services
- Contract renewal calendar
- Cost trends (year-over-year comparison)
- Optimization opportunities
- Budget variance

### How to Complete

1. Export billing data from each cloud provider console (monthly or quarterly)
2. Categorize spend by service type (IaaS, PaaS, SaaS), department, and cost centre
3. Identify top 10 services by spend and flag any with >10% quarter-over-quarter increase
4. Cross-reference contract renewal dates and flag renewals within 90 days
5. Document optimization opportunities (right-sizing, reserved instances, unused resources)
6. Calculate budget variance and report to finance/management

---

## Sheet 6: Compliance & Regulatory Mapping

### Purpose

Map regulatory requirements to cloud services, track compliance status, identify gaps.

### What to Document

- Applicable regulations per service (GDPR, FADP, HIPAA, PCI-DSS, etc.)
- Required vendor certifications
- Data processing agreements (DPAs) status
- Compliance gaps
- Audit readiness

### How to Complete

---

## Section 5: Completing Sheets 7-9

### Sheet 7: Summary Dashboard

**Purpose:** Auto-calculated metrics consolidating data from all assessment sheets.

**Key Metrics:**

- Total services inventoried
- Services by type (SaaS, IaaS, PaaS breakdown)
- Services by criticality (Critical/High/Medium/Low counts)
- Total cloud spend (annual)
- Compliance status distribution (Compliant/Partial/Non-Compliant counts)

**How It Works:** Formula-driven, automatically populated from Sheets 1-6.

**Your Role:** Verify calculations are correct, interpret results, identify trends.

---

### Sheet 8: Evidence Register

**Purpose:** Central registry of all evidence collected during assessment.

**What to Document:**

- Evidence ID (EV-INV-001, EV-INV-002, etc.)
- Service Name
- Evidence Type (Contract, Invoice, Screenshot, Export, Report)
- Description
- File Location (path to evidence file)
- Date Collected
- Collected By
- Verification Status

**Organization:**
```
/Evidence/ISMS-IMP-A.5.23.S1/
  /Contracts/
  /Invoices/
  /Screenshots/
  /Exports/
  /Reports/
```

**Quality Check:**

- [ ] All evidence organized in standard folders
- [ ] Evidence registry matches actual files
- [ ] Sensitive data redacted from screenshots
- [ ] Evidence accessible to auditors

---

### Sheet 9: Approval Sign-Off

**Purpose:** Document three-level approval process.

**Workflow:**
1. **IT Operations Review** → Verify inventory completeness, technical accuracy
2. **Finance/Compliance Review** → Verify costs, regulatory requirements
3. **CISO/CIO Approval** → Final approval, gap remediation authorization

**Completion:** All three signatures required before assessment considered complete.

---

## Section 6: Evidence Collection & Common Pitfalls

### Evidence Collection Best Practices

**Types of Evidence:**

| Evidence Type | Examples | When to Collect |
|---------------|----------|-----------------|
| **Contracts** | MSA, DPA, SLA | For all services > CHF 10K/year |
| **Financial** | Invoices, POs, budget allocations | For all services |
| **Technical** | Screenshots, config exports, architecture diagrams | For Critical/High services |
| **Compliance** | Vendor certifications (SOC 2, ISO 27001), audit reports | For Restricted/Confidential data services |
| **Operational** | User lists, usage reports, incident logs | For Critical services |

**Evidence Quality Standards:**

✅ **Good Evidence:**

- Recent (< 90 days old)
- Complete (all required information visible)
- Sanitized (passwords/secrets redacted)
- Timestamped (date clearly visible)
- Attributed (source identified)

❌ **Poor Evidence:**

- Outdated (> 1 year old)
- Incomplete (key information missing)
- Unsanitized (contains sensitive data)
- No date (can't verify currency)
- Generic (vendor marketing, not actual config)

---

### Common Pitfalls

**Pitfall 1: Incomplete Discovery**

**Mistake:** Missing shadow IT, department-specific tools, or free trials.

**Example:** IT discovers services only through procurement. Marketing has 15 SaaS tools purchased via credit card - all undocumented.

**Why It Happens:**

- Siloed discovery (only checking one source)
- Not engaging with departments
- Assuming procurement has complete record

**How to Avoid:**

- Use all 6 discovery methods (procurement, financial, network, SSO, surveys, asset inventory)
- Cross-check results
- Engage department heads
- Check credit card statements

---

**Pitfall 2: Aspirational Classification**

**Mistake:** Rating services based on what SHOULD be, not what IS.

**Example:** 

- Service rated "Confidential" because policy says it should only process Confidential data
- Reality: Users upload Restricted data (personal health info)
- Correct rating: Restricted (based on actual use, not policy)

**Why It Happens:**

- Optimism bias
- Pressure to show compliance
- Not verifying actual usage

**How to Avoid:**

- Interview actual users (not just service owners)
- Review sample data
- Check logs/audit trails
- Rate based on REALITY, not policy

---

**Pitfall 3: Over-Rating Criticality**

**Mistake:** Everything marked "Critical."

**Example:** Email (Critical), CRM (Critical), HR System (Critical), Training Platform (Critical)...

**Reality:** Only 5-15% of services should be truly Critical.

**Why It Happens:**

- Service owners want priority treatment
- "Everything is important to someone"
- Fear of undervaluing services

**How to Avoid:**

- Use objective criteria (RTO < 4 hours, revenue impact)
- Apply business impact test ("Can we operate for a day without this?")
- Push back on inflation
- Get management validation

---

**Pitfall 4: Assuming On-Prem Is Cheaper**

**Mistake:** "Cloud is expensive, let's move back on-prem."

**Example:** 

- Cloud cost: CHF 400K/year
- Assumed on-prem cost: CHF 200K/year (hardware only)
- Actual on-prem cost: CHF 900K/year (hardware + staff + facilities + maintenance)

**Why It Happens:**

- Only counting CAPEX, ignoring OPEX
- Not counting staff time (largest cost)
- Not counting facilities, power, cooling
- Not counting ongoing maintenance/refresh

**How to Avoid:**

- **ALWAYS** run full TCO analysis
- Include ALL costs (staff, facilities, refresh, training)
- Use 5-year comparison
- Be honest about staffing requirements (4-7 FTE typical)
- Remember: On-prem cheaper in <5% of cases

---

**Pitfall 5: Untested Exit Plans**

**Mistake:** Exit plan documented but never tested.

**Example:**

- Exit plan says: "Export data via API, import to Alternative Provider"
- Reality when tested: API rate-limited to 100 records/hour, full export would take 6 months
- Export format not compatible with Alternative Provider

**Why It Happens:**

- Assuming vendor documentation is accurate
- Not validating assumptions
- "Set it and forget it" mentality

**How to Avoid:**

- **ACTUALLY TEST** data export (even sample)
- Import test data into alternative provider
- Time the export (how long does it really take?)
- Document any issues found
- Re-test annually

---

**Pitfall 6: Ignoring Hybrid Complexity**

**Mistake:** "Hybrid is the easy middle ground between cloud and on-prem."

**Reality:** Hybrid is often MORE complex than pure cloud OR pure on-prem.

**Why:**

- Two environments to manage (cloud + on-prem)
- Data synchronization challenges (latency, consistency)
- Security boundaries (cross-environment trust)
- Skills required for both environments
- More failure modes (connectivity, sync, inconsistency)

**When Hybrid Makes Sense:**

- Data sovereignty mandate (some data MUST be on-prem)
- Extreme latency requirements (< 10ms)
- Existing on-prem infrastructure with spare capacity
- Staged migration path

**When to Avoid Hybrid:**

- "Cloud and on-prem both sound good" (lack of clear requirement)
- Cost optimization (usually not cheaper than pure cloud)
- "Hedge our bets" (increases risk, doesn't reduce it)

---

**Pitfall 7: No Service Owners**

**Mistake:** Services in inventory with "Owner: TBD" or "IT Operations."

**Example:** 47 services in inventory, 23 have no identified owner.

**Why It's a Problem:**

- No one accountable for the service
- Can't make decisions (renew? sunset? upgrade?)
- Can't assess business impact
- Can't get data classification info

**How to Avoid:**

- **NEVER** leave owner field blank
- Escalate to department head if owner unknown
- Default to "Unassigned - Escalated to [Name]" (make escalation visible)
- Track unassigned services as HIGH PRIORITY gap

---

**Pitfall 8: Stale Inventory**

**Mistake:** Inventory created once, never updated.

**Example:**

- Inventory from January 2025 still being used in January 2026
- Contains 15 decommissioned services
- Missing 30 new services deployed in last year

**Why It Happens:**

- No process for updates
- No ownership of inventory maintenance
- Quarterly updates not scheduled
- Drift between reality and documentation

**How to Avoid:**

- **Schedule quarterly updates** (calendar invites)
- Assign inventory owner (IT Ops Manager, Cloud Architect)
- Trigger updates: new service deployment, service sunset, contract renewal
- Continuous discovery (automated network/SSO/financial monitoring)

---

## Section 7: Quality Checklist + Review & Approval

### Master Quality Checklist

Before submitting for review, verify:

#### Completeness

- [ ] All discovered services documented (100% from discovery phase)
- [ ] All sheets completed (1-9)
- [ ] No blank mandatory fields
- [ ] Evidence collected for Critical/High services
- [ ] Gap analysis complete

#### Accuracy

- [ ] All data verified with authoritative sources (not assumed)
- [ ] Service owners confirmed (not guessed)
- [ ] Costs verified with finance
- [ ] Classifications verified with data owners
- [ ] Exit strategies realistic (not aspirational)

#### Honesty

- [ ] Criticality ratings honest (not inflated)
- [ ] Gaps documented (not hidden)
- [ ] Lock-in risks acknowledged (not downplayed)
- [ ] TCO analysis realistic (all costs included)

#### Evidence Quality

- [ ] Evidence recent (< 90 days)
- [ ] Evidence complete (required information present)
- [ ] Evidence sanitized (sensitive data redacted)
- [ ] Evidence organized (follows standard structure)
- [ ] Evidence accessible (paths correct, files exist)

#### Compliance

- [ ] Regulatory requirements identified
- [ ] DPAs in place for personal data
- [ ] Data residency verified
- [ ] Vendor certifications confirmed
- [ ] Exit plans documented for Critical/High

#### Financial

- [ ] Costs reconcile with budget
- [ ] Contract dates accurate
- [ ] Renewal calendar complete
- [ ] Cost optimizations identified
- [ ] ROI calculated for optimizations

---

### Review & Approval Process

#### Level 1: Technical Review

**Reviewer:** IT Operations Manager, Cloud Architect, or Security Engineer

**Focus:**

- Inventory completeness (all services found?)
- Technical accuracy (service types correct?)
- Architecture understanding (dependencies mapped?)
- Exit feasibility (realistic assessments?)

**Checklist:**

- [ ] Discovery methods all executed
- [ ] Service inventory complete
- [ ] Technical details accurate
- [ ] Dependencies identified
- [ ] Exit strategies technically sound

**Timeline:** 2-3 days

**Outcome:**

- ✅ Approved → Move to Level 2
- ⚠️ Changes Requested → Return to completer with feedback

---

#### Level 2: Compliance & Financial Review

**Reviewer:** Compliance Officer, Finance Manager, or Legal Counsel

**Focus:**

- Regulatory compliance (requirements identified?)
- Financial accuracy (costs verified?)
- Contract status (renewals tracked?)
- Risk assessment (gaps documented?)

**Checklist:**

- [ ] Data classifications correct
- [ ] Regulatory requirements identified
- [ ] Financial data verified
- [ ] Contracts documented
- [ ] Compliance gaps have remediation plans

**Timeline:** 2-3 days

**Outcome:**

- ✅ Approved → Move to Level 3
- ⚠️ Changes Requested → Return with feedback

---

#### Level 3: Management Approval

**Reviewer:** CISO, CIO, or CFO

**Focus:**

- Strategic alignment (supports business strategy?)
- Risk acceptance (gaps acceptable?)
- Budget impact (costs within budget?)
- Resource allocation (remediation plans funded?)

**Checklist:**

- [ ] Overall assessment credible
- [ ] Gap priorities align with business risk
- [ ] Remediation plans resourced
- [ ] Budget implications understood
- [ ] Risks formally accepted or mitigated

**Timeline:** 3-5 days

**Outcome:**

- ✅ Approved → Assessment complete, ready for audit
- ⚠️ Changes Requested → Return with feedback
- ⚠️ Escalate → Executive leadership review (for major issues)

---

### Post-Approval Actions

Once all three levels approve:

1. **Lock Assessment**

   - No further edits without change control
   - Version as "APPROVED v1.0"
   - Archive in ISMS documentation repository

2. **Publish Inventory**

   - Make available to other teams (read-only)
   - Update CMDB with cloud service data
   - Share with procurement (contract tracking)
   - Share with finance (budget planning)

3. **Notify Stakeholders**

   - Auditors: Assessment available for review
   - Department heads: Service ownership confirmed
   - Finance: Cost optimizations identified
   - Security: Risk gaps requiring remediation

4. **Execute Remediation**

   - Assign owners to all gaps
   - Set milestones and target dates
   - Allocate budget/resources
   - Track progress monthly

5. **Schedule Quarterly Update**

   - Calendar invite for Q2, Q3, Q4 updates
   - Assign responsibility for updates
   - Define update process

---

## Section 8: Next Steps After Completion

### Proceed to Other A.5.23 Assessments

This inventory (A.5.23.1) is complete. Use it as INPUT for:

**A.5.23.2 - Vendor Due Diligence:**

- Use service/vendor list from Sheet 1
- Assess vendor security posture
- Review contracts and SLAs
- Evaluate vendor risk

**A.5.23.3 - Secure Configuration:**

- Use service list and criticality ratings
- Assess security configurations
- Verify baseline compliance
- Identify configuration gaps

**A.5.23.4 - Ongoing Governance:**

- Use service ownership from Sheet 1
- Assess access reviews
- Evaluate change management
- Review incident procedures

**A.5.23.5 - Compliance Dashboard:**

- Consolidate all assessment data
- Generate executive summary
- Track compliance metrics
- Report to management

---

### Execute Remediation Plans

From gap analysis:
1. **Review prioritized gaps** with management
2. **Allocate resources** (budget, people, time)
3. **Assign ownership** to each gap
4. **Set milestones** (30/60/90-day targets)
5. **Track progress** (monthly status reviews)
6. **Update assessment** as gaps close

---

### Establish Continuous Discovery

Move beyond periodic assessments:

**Automated Discovery:**

- Network traffic monitoring (flag new cloud domains)
- SSO integration monitoring (new app registrations)
- Financial system monitoring (new cloud vendors)
- Cloud access broker (CASB) deployment

**Process Integration:**

- New service deployment → Add to inventory
- Service decommission → Update inventory status
- Contract renewal → Update contract dates
- Vendor acquisition → Assess vendor risk impact

**Ownership:**

- Assign "Cloud Services Inventory Owner" role
- Define responsibilities (maintenance, updates, accuracy)
- Establish SLA (new services added within X days)

---

### Quarterly Updates

**Update Schedule:** Q2, Q3, Q4 (and annually for comprehensive review)

**What to Update:**

- **Sheet 1:** New services, decommissioned services, status changes
- **Sheet 2:** Data classification changes (new data types)
- **Sheet 3:** Criticality re-assessment (business impact changes)
- **Sheet 4:** Exit strategy review, export testing results
- **Sheet 5:** Cost updates, renewal dates, optimization progress
- **Sheet 6:** Regulatory changes, compliance status
- **Sheet 10:** New evidence collected

**Update Process:**
1. Run discovery methods (focus on deltas since last assessment)
2. Interview service owners (any changes?)
3. Update sheets
4. Collect new evidence
5. Re-run approval process (may be expedited if minor changes)

---

### Metrics & Reporting

**Track KPIs:**

- Total cloud spend (trend over time)
- Number of cloud services (growth rate)
- Shadow IT discovery rate (services found outside procurement)
- Exit plan coverage (% of Critical/High with documented plans)
- Compliance rate (% services fully compliant)
- Cost optimization savings realized

**Monthly Reporting to Management:**

- New services added
- Services decommissioned
- Contract renewals upcoming
- Cost variance vs. budget
- Compliance gaps (open/closed)
- Optimization savings

---

## Section 9: Appendix & Glossary

### Terminology

**Assessment Terms:**

- **Inventory:** Complete list of all cloud services
- **Classification:** Categorization by data type, criticality, etc.
- **Criticality:** Business impact rating if service unavailable
- **Exit Strategy:** Plan for migrating away from cloud service
- **Lock-In:** Factors preventing easy migration
- **TCO:** Total Cost of Ownership (5-year comparison)

**Cloud Service Types:**

- **SaaS:** Software as a Service (complete applications)
- **IaaS:** Infrastructure as a Service (compute, storage, network)
- **PaaS:** Platform as a Service (development platforms)

**Exit Strategies:**

- **Cloud-to-Cloud:** Migrate to alternative cloud provider (DEFAULT, 90%+)
- **Hybrid:** Partial on-premises repatriation (5-10%)
- **On-Premises:** Full build-back to internal infrastructure (<5%, rarely justified)

**Financial Terms:**

- **CAPEX:** Capital Expenditure (upfront hardware investment)
- **OPEX:** Operating Expenditure (annual recurring costs, includes staffing)
- **TCO:** Total Cost of Ownership (CAPEX + 5 years OPEX)

**Compliance Terms:**

- **DPA:** Data Processing Agreement (GDPR requirement)
- **BAA:** Business Associate Agreement (HIPAA requirement)
- **SCC:** Standard Contractual Clauses (EU data transfer mechanism)

---

### References

**Policy Documents:**

- ISMS-POL-A.5.19-23: Supplier & Cloud Services Security Policy (Master)
- ISMS-POL-A.5.19-23-S5: Cloud Services Security (Detailed requirements)
- ISMS-POL-A.5.19-23-S5 Section 8.1.1: Exit Strategy Framework (Cloud/Hybrid/On-Prem)

**Related Assessments:**

- ISMS-IMP-A.5.23.S2: Vendor Due Diligence & Contracts
- ISMS-IMP-A.5.23.S3: Secure Configuration & Deployment
- ISMS-IMP-A.5.23.S4: Ongoing Governance & Risk Management
- ISMS-IMP-A.5.23.S5: Compliance Monitoring Dashboard

**External Standards:**

- ISO/IEC 27001:2022 Annex A.5.19-23: Supplier Controls
- DORA (Digital Operational Resilience Act) Article 28.6: Exit Strategies
- GDPR Article 28: Data Processing Agreements
- Swiss FADP: Data Protection Requirements

---

### Contact Information

**For Questions on This Assessment:**

- **Assessment Owner:** [IT Operations Manager / Cloud Architect]
- **Technical Questions:** [Security Team / Cloud Team]
- **Compliance Questions:** [Compliance Officer / Legal]
- **Financial Questions:** [Finance Manager / Procurement]

**Escalation:**

- **CISO:** For risk acceptance, major gaps
- **CIO:** For strategic decisions, major investments
- **CFO:** For budget implications, cost optimizations

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
