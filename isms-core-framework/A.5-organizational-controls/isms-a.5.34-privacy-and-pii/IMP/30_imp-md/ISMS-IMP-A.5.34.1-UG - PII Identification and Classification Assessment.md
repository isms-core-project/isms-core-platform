**ISMS-IMP-A.5.34.1-UG - PII Identification and Classification Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.34.1-UG |
| **Version** | 1.0 |
| **Assessment Area** | PII Identification, Classification, Data Flow Mapping, and ROPA Maintenance |
| **Related Policy** | ISMS-POL-A.5.34, Section 2.1 (PII Classification and Identification) |
| **Purpose** | Guide users through systematic PII discovery, classification, data mapping, and GDPR Article 30 compliant Record of Processing Activities (ROPA) maintenance |
| **Target Audience** | DPO/Privacy Officers, Data Owners, System Owners, IT Teams, Compliance Officers, Auditors, Workbook Developers |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major System Changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for PII Identification assessment workbook | ISMS Implementation Team |

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.34.1-TG.

---

**Audience:** DPO/Privacy Officers, Data Owners, System Owners, IT Teams, Compliance Officers

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.34.1 - PII Identification and Classification Assessment

### What This Assessment Covers

This assessment documents the **WHAT** and **WHERE** of PII processing - the foundational inventory that answers:

- What personal data / PII does [Organization] process?
- Where is this PII located (systems, databases, applications, files)?
- How is PII classified (Basic, Sensitive, Criminal Offense Data)?
- How does PII flow through organizational boundaries?
- What processing activities are conducted (collection, storage, sharing, deletion)?
- What legal basis justifies each processing activity?
- What safeguards protect PII during cross-border transfers?

### Key Principle

This assessment is **completely vendor-agnostic and technology-independent**. You document YOUR specific systems (whatever you use - Salesforce, SAP, custom databases, spreadsheets, email, paper files) and verify compliance against generic GDPR/FADP requirements.

### What You'll Document

- ✅ **Complete PII system inventory** listing all systems containing personal data
- ✅ **PII classification** for each system (Basic/Sensitive/Criminal Offense)
- ✅ **Data flow diagrams** showing PII movement across organizational boundaries
- ✅ **Cross-border transfer identification** with safeguard documentation
- ✅ **Record of Processing Activities (ROPA)** compliant with GDPR Article 30
- ✅ **Legal basis documentation** for all processing activities
- ✅ **Gap analysis** identifying non-compliant processing
- ✅ **Evidence register** linking documentation to audit artifacts
- ✅ **Approved assessment** with DPO and stakeholder sign-offs

### How This Relates to Other A.5.34 Assessments

| Assessment | Focus | Relationship to A.5.34.1 |
|------------|-------|--------------------------|
| **ISMS-IMP-A.5.34.1** | **PII Identification & ROPA** | **Foundation - WHAT and WHERE** |
| ISMS-IMP-A.5.34.2 | Legal Basis & Lawful Processing | Requires ROPA from A.5.34.1 for legal basis mapping |
| ISMS-IMP-A.5.34.3 | Data Subject Rights Management | Requires PII inventory to fulfill access/erasure requests |
| ISMS-IMP-A.5.34.4 | Technical & Organizational Measures | Requires PII classification to determine appropriate controls |
| ISMS-IMP-A.5.34.5 | Data Protection Impact Assessment | Triggered by high-risk processing identified in ROPA |
| ISMS-IMP-A.5.34.6 | Cross-Border Transfer Assessment | Requires transfer flows from A.5.34.1 data flow mapping |

**Context Note:** This assessment (A.5.34.1) MUST be completed first - it provides the foundational PII inventory and ROPA that all other privacy assessments depend on.

## Who Should Complete This Assessment

### Primary Stakeholders

1. **Data Protection Officer (DPO) / Privacy Officer** - Leads assessment, ensures GDPR Article 30 compliance, validates ROPA completeness
2. **Chief Information Security Officer (CISO) / Security Team** - Provides technical PII discovery support (DLP scans, database queries, system documentation)
3. **System Owners / IT Operations** - Document PII in systems they manage, provide technical architecture details
4. **Data Owners / Business Process Owners** - Define data processing purposes, legal bases, retention requirements
5. **Legal / Compliance Officer** - Validate legal basis accuracy, confirm cross-border transfer mechanisms

### Required Skills

- Understanding of GDPR Article 30 and Swiss FADP requirements
- Knowledge of [Organization]'s IT infrastructure and system landscape
- Familiarity with data protection principles (purpose limitation, data minimization, storage limitation)
- Ability to interview system owners and business stakeholders
- Technical understanding to read system documentation and data flow diagrams

### Time Commitment

- **Initial assessment:** 20-40 hours (depending on organization size and system complexity)
  - Small organization (1-10 systems, 1-50 employees): 10-20 hours
  - Medium organization (10-50 systems, 50-250 employees): 20-40 hours
  - Large organization (50+ systems, 250+ employees): 40-80+ hours
- **Quarterly updates:** 2-4 hours (verify no changes, update for new systems)

## Expected Outputs

Upon completion, you will have:

1. ✅ **Complete PII System Inventory** - All systems processing PII with classifications
2. ✅ **PII Data Flow Map** - Visual representation of data movement including cross-border transfers
3. ✅ **GDPR Article 30 Compliant ROPA** - Record of Processing Activities with all required elements
4. ✅ **Legal Basis Documentation** - Identified and validated for each processing activity
5. ✅ **Cross-Border Transfer Register** - All international data transfers with safeguard mechanisms
6. ✅ **PII Discovery Gap Analysis** - Identified gaps with risk ratings and remediation plans
7. ✅ **Evidence Register** - Supporting documentation linked to audit artifacts
8. ✅ **Compliance Dashboard** - Executive summary with metrics and KPIs
9. ✅ **Approved Assessment** - DPO and stakeholder sign-offs confirming accuracy

---

# Prerequisites

## Information You'll Need

Before starting this assessment, gather:

### System Documentation

- IT asset inventory (from ISMS-POL-A.5.9 if available)
- System architecture diagrams
- Application portfolio / software inventory
- Database documentation
- Cloud service subscriptions (SaaS platforms)
- Third-party processor list

### Data Flow Documentation

- Network diagrams showing system interconnections
- API integrations and data exchange protocols
- Data lineage documentation (where data originates, how it flows)
- Cross-border data transfer records
- Vendor/processor contracts (for data sharing agreements)

### Business Process Information

- Business process documentation (what activities use PII)
- HR processes (employee data lifecycle)
- Customer/client processes (CRM, sales, support)
- Marketing processes (campaigns, analytics, advertising)
- Vendor management processes (procurement, payments)

### Legal/Compliance Documentation

- Privacy notices and policies
- Data Processing Agreements (DPA) with processors
- Standard Contractual Clauses (SCCs) for international transfers
- Binding Corporate Rules (BCRs) if applicable
- GDPR Article 30 ROPA (if existing - for validation/update)
- Legal obligations register (employment law, tax law, sector regulations)

### Technical Discovery Tools

- Data Loss Prevention (DLP) scan results
- Database discovery tool outputs
- File system scans for PII (structured data, documents, emails)
- Cloud access security broker (CASB) reports
- Identity and Access Management (IAM) logs

## Access Required

You will need access to:

**Systems:**

- [ ] Administrative access to key systems (or coordination with system administrators)
- [ ] Database query access for PII column identification
- [ ] Cloud platform admin consoles (AWS, Azure, GCP, SaaS applications)
- [ ] File share and document management systems
- [ ] Email system (for correspondence records, mailing lists)

**Documents:**

- [ ] IT architecture documentation repository
- [ ] Vendor contracts and DPAs
- [ ] Privacy notice templates and published versions
- [ ] Legal obligations register
- [ ] Previous ROPA (if exists)

**People:**

- [ ] Ability to interview system owners and data owners
- [ ] Access to HR, Sales, Marketing, Finance directors for process understanding
- [ ] Coordination with Legal/Compliance for regulatory interpretation
- [ ] Support from IT/Security for technical discovery

## Tools and Resources

**Assessment Workbook:** Excel workbook (generated by `generate_a5341_pii_identification_assessment.py`) containing:

- Sheet 1: Instructions & Legend
- Sheet 2: PII System Inventory
- Sheet 3: PII Data Flow Mapping
- Sheet 4: Record of Processing Activities (ROPA)
- Sheet 5: PII Discovery Gaps
- Sheet 6: Evidence Register
- Sheet 7: Dashboard
- Sheet 8: Approval & Sign-Off

**Supporting Tools** (optional but highly recommended):

- **Data Loss Prevention (DLP)** - Automated PII scanning (e.g., Microsoft Purview, Symantec DLP, Digital Guardian)
- **Database discovery tools** - Identify PII columns in databases (e.g., BigID, OneTrust Discovery, IBM Guardium)
- **Data mapping software** - Visualize data flows (e.g., OneTrust DataGuidance, TrustArc, Collibra)
- **Collaboration tools** - Document findings (SharePoint, Confluence, Notion)

**Reference Materials:**

- ISMS-POL-A.5.34 Section 2.1 (PII classification framework)
- ISMS-CTX-A.5.34 (Privacy regulatory landscape - GDPR/FADP guidance)
- GDPR Article 30 text (ROPA requirements)
- [Organization]'s data classification policy (ISMS-POL-A.5.12)
- ICO Guidance: ["Guide to the GDPR - Documentation"](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/documentation/)
- EDPB Guidelines 07/2020 on Article 30 ROPA

---

# Assessment Workflow

## High-Level Process

```
1. PREPARE (Gather prerequisites, set up assessment team)
   ↓
2. DISCOVER PII SYSTEMS (Automated scans + manual inventory)
   ↓
3. CLASSIFY PII (Basic / Sensitive / Criminal Offense Data)
   ↓
4. MAP DATA FLOWS (Internal + cross-border transfers)
   ↓
5. CREATE/UPDATE ROPA (GDPR Article 30 compliance)
   ↓
6. IDENTIFY GAPS (Missing systems, unlawful processing)
   ↓
7. COLLECT EVIDENCE (Link to supporting documentation)
   ↓
8. REVIEW & APPROVE (DPO validation, stakeholder sign-off)
```

## Detailed Workflow

### Phase 1: Preparation (1-2 hours)

**Objective:** Set up assessment foundation

**Steps:**
1. Read this entire User Guide (PART I)
2. Gather all prerequisites (Section 2.1 above)
3. Review ISMS-POL-A.5.34 Section 2.1 for PII classification framework
4. Identify all system owners and schedule interviews
5. Set up DLP scans or database discovery tools (if available)
6. Create working folder for evidence collection

**Deliverable:** Assessment plan with system owner interview schedule

### Phase 2: PII System Discovery (5-15 hours)

**Objective:** Identify ALL systems processing PII

**Steps:**
1. **Automated Discovery:**

   - Run DLP scans across file shares, email, databases
   - Execute database discovery tools to identify PII columns
   - Review CASB reports for cloud application usage
   - Analyze IAM logs for system access patterns

2. **Manual Discovery:**

   - Review IT asset inventory (ISMS-POL-A.5.9)
   - Interview system owners using discovery questionnaire
   - Review vendor contracts for processor relationships
   - Walk through business processes (HR, Sales, Marketing, Finance)

3. **Inventory Creation (Sheet 2):**

   - List EVERY system containing PII (don't miss any!)
   - Document system owner, type, purpose
   - Estimate data volume (approximate record counts)
   - Note hosting location (on-premises, cloud provider, geographic region)
   - Identify access levels (who can access, how many users)

**Deliverable:** Complete Sheet 2 (PII System Inventory) with all systems listed

**Quality Check:**

- ✓ All obvious systems captured (CRM, HRIS, email, file shares)
- ✓ Cloud services documented (SaaS subscriptions)
- ✓ Shadow IT identified (unapproved cloud usage)
- ✓ Paper records included (physical files, access logs)
- ✓ Backup systems documented (backups contain PII too!)
- ✓ Development/test environments captured (may contain production PII copies)

### Phase 3: PII Classification (3-6 hours)

**Objective:** Classify PII sensitivity for each system

**Steps:**
1. Review PII classification framework (ISMS-POL-A.5.34 Section 2.1):

   - **Basic PII:** Name, email, phone, address, account numbers
   - **Sensitive PII (GDPR Art. 9):** Health data, biometrics, genetic data, racial/ethnic origin, political opinions, religious beliefs, trade union membership, sex life/orientation, private sphere (FADP-specific)
   - **Criminal Offense Data (GDPR Art. 10):** Criminal convictions, criminal charges, criminal history

2. For EACH system in Sheet 2, determine:

   - What PII categories does this system contain?
   - What is the highest PII classification? (If system contains both Basic and Sensitive, classify as Sensitive)
   - If Sensitive PII, what specific types? (e.g., health data, biometric authentication)

3. Apply classification decision tree:
```
Does system contain Special Category Data (GDPR Art. 9)?
  YES → Classification: SENSITIVE PII
  NO → Continue...

Does system contain Criminal Offense Data (GDPR Art. 10)?
  YES → Classification: CRIMINAL OFFENSE DATA
  NO → Continue...

Does system contain financial data, government IDs, detailed location, or communications content?
  YES → Classification: BASIC PII (high sensitivity subset)
  NO → Continue...

Does system contain names, contact details, generic user data?
  YES → Classification: BASIC PII
  NO → System may not contain PII (verify it's truly anonymous)
```

**Deliverable:** Sheet 2 complete with PII Classification column populated

**Common Mistakes to Avoid:**

- ❌ Under-classifying: "Employee birthdates are just Basic PII" → Wrong if combined with health insurance data
- ❌ Over-classifying: "All customer data is Sensitive" → No, unless it contains GDPR Art. 9 categories
- ❌ Forgetting backups: Backups inherit classification of source system
- ❌ Ignoring aggregation: Multiple Basic PII fields together can create profiling risk

### Phase 4: Data Flow Mapping (4-8 hours)

**Objective:** Document how PII moves through and across organizational boundaries

**Steps:**
1. For EACH system in Sheet 2, identify:

   - **Inbound flows:** Where does PII come from?
     - Data subject (directly from individual via form, registration)
     - Other internal systems (API, database sync, file transfer)
     - Third-party sources (vendor provides data, data enrichment services)
   
   - **Internal flows:** Where does PII move within [Organization]?
     - System-to-system integrations
     - Database replication
     - Backup processes
     - Reporting/analytics extracts
   
   - **Outbound flows:** Where does PII go outside [Organization]?
     - Processors (cloud services, vendors performing work on behalf)
     - Third parties (marketing partners, analytics providers)
     - Cross-border transfers (data leaving CH/EU)
     - Data subject (portability requests, account exports)

2. For CROSS-BORDER transfers, document:

   - Source country (where data originates)
   - Destination country (where data is transferred to)
   - Transfer mechanism (SCCs, BCRs, Adequacy Decision, Derogation)
   - Processor name and contract reference

3. Complete Sheet 3 (PII Data Flow Mapping):

   - One row per data flow
   - Link to source/destination systems (use System Names from Sheet 2)
   - Document transfer mechanism, frequency, volume
   - Flag cross-border transfers for TIA (Transfer Impact Assessment) in A.5.34.6

**Deliverable:** Sheet 3 complete with all significant data flows mapped

**Quality Check:**

- ✓ All systems have at least one inbound flow (where does data come from?)
- ✓ Cross-border transfers identified (look for cloud providers with global infrastructure)
- ✓ Processor relationships documented (cloud SaaS, outsourced functions)
- ✓ API integrations captured (check application logs, API gateways)
- ✓ Manual data exports noted (spreadsheet downloads, report generation)

### Phase 5: ROPA Creation (6-12 hours)

**Objective:** Create GDPR Article 30 compliant Record of Processing Activities

**GDPR Article 30 Requirements:**
The ROPA must document:

- Name and contact details of controller (and DPO if applicable)
- Purposes of processing
- Categories of data subjects
- Categories of personal data
- Categories of recipients (internal departments, external processors, third parties)
- Transfers to third countries (if applicable)
- Retention periods (or criteria to determine)
- Technical and organizational measures (general description)

**Steps:**
1. **Group systems into processing activities:**

   - One processing activity may span multiple systems
   - Example: "Employee Management" activity includes HRIS, payroll, time tracking, email
   - Example: "Customer Relationship Management" activity includes CRM, marketing automation, support tickets

2. **For EACH processing activity, document in Sheet 4:**

   - Activity name and purpose (why are we processing this data?)
   - Data subjects (employees, customers, vendors, job applicants, website visitors)
   - PII categories processed (from Sheet 2 system inventory)
   - Legal basis (consent, contract, legal obligation, legitimate interest, vital interest, public task)
   - Recipients (who receives this data - internal departments, processors, third parties)
   - Cross-border transfers (from Sheet 3 data flows)
   - Retention period (how long data is kept, or criteria for deletion)
   - Security measures (reference to TOMs assessment A.5.34.4)

3. **Validate legal basis:**

   - Every processing activity MUST have a valid legal basis under GDPR Article 6
   - For Sensitive PII, additional legal basis required under GDPR Article 9
   - If legal basis unclear, flag for Legal/Compliance review

4. **Cross-reference with existing ROPA (if applicable):**

   - Compare new ROPA against previous version
   - Identify new processing activities (flag for review)
   - Identify ceased processing (mark as inactive)
   - Update changed processing purposes or PII categories

**Deliverable:** Sheet 4 (ROPA) complete with all processing activities documented

**Quality Check:**

- ✓ Every system from Sheet 2 is included in at least one ROPA entry
- ✓ Every processing activity has a documented legal basis
- ✓ Sensitive PII has GDPR Article 9 legal basis (not just Article 6)
- ✓ Recipients clearly identified (don't use vague terms like "business partners")
- ✓ Cross-border transfers reference Sheet 3 data flows
- ✓ Retention periods are specific (not "as long as necessary")

### Phase 6: Gap Analysis (2-4 hours)

**Objective:** Identify non-compliant processing and prioritize remediation

**Steps:**
1. **Review Sheet 2, 3, 4 for gaps:**

   - Systems without clear PII classification
   - Processing activities without valid legal basis
   - Cross-border transfers without adequate safeguards
   - Data flows with no documented purpose
   - Systems with "unknown" hosting location or owner

2. **For EACH gap, document in Sheet 5:**

   - Gap description (what's missing or non-compliant?)
   - System or activity affected
   - Risk level (Critical / High / Medium / Low based on impact and likelihood)
   - Remediation action (what needs to be done?)
   - Owner (who will fix it?)
   - Target completion date (risk-based prioritization)

3. **Risk Rating Guidelines:**

   - **Critical:** Unlawful processing (no legal basis, inadequate safeguards for Sensitive PII)
   - **High:** Significant compliance gap (cross-border transfers without SCCs, inaccurate ROPA)
   - **Medium:** Process improvement needed (incomplete documentation, missing evidence)
   - **Low:** Minor deficiency (formatting inconsistencies, unclear descriptions)

**Deliverable:** Sheet 5 (PII Discovery Gaps) with all identified gaps and remediation plans

**Common Gaps:**

- "We collect PII but don't have a legal basis documented"
- "We transfer data to US-based cloud provider but don't have SCCs in place"
- "We keep customer data indefinitely without defined retention period"
- "Shadow IT discovered - unapproved SaaS application with customer data"
- "Development environment contains production PII without proper access controls"

### Phase 7: Evidence Collection (2-4 hours)

**Objective:** Link assessment to supporting audit documentation

**Steps:**
1. For key assertions in Sheets 2-5, collect evidence:

   - **System inventory:** Screenshots of system admin consoles, architecture diagrams
   - **PII classification:** DLP scan reports, database schema documentation
   - **Data flows:** API integration documentation, network diagrams, processor contracts
   - **ROPA entries:** Privacy notices, consent forms, DPAs with processors
   - **Cross-border transfers:** SCCs signed with vendors, adequacy decision documentation
   - **Legal basis:** Legitimate Interest Assessments (LIAs), consent records, legal obligations register

2. Store evidence in organized structure:
   ```
   Evidence Repository/
   ├── System_Inventory/
   │   ├── CRM_Screenshot_AdminConsole.png
   │   ├── HRIS_Architecture_Diagram.pdf
   │   └── Cloud_Services_Subscription_List.xlsx
   ├── Data_Flows/
   │   ├── API_Integration_Documentation.pdf
   │   ├── Processor_DPA_Vendor_ABC.pdf
   │   └── SCC_Cloud_Provider_XYZ.pdf
   ├── Legal_Basis/
   │   ├── Privacy_Notice_Customers_v2.1.pdf
   │   ├── Consent_Form_Marketing.pdf
   │   └── LIA_Customer_Profiling.docx
   └── [etc.]
   ```

3. Register evidence in Sheet 6:

   - Evidence ID (unique identifier)
   - Related sheet/row (link evidence to specific assertion)
   - Evidence type (screenshot, document, report, contract)
   - File location (path to evidence file)
   - Evidence date (when evidence was created/captured)

**Deliverable:** Sheet 6 (Evidence Register) populated with links to all supporting documentation

**Quality Check:**

- ✓ Every "Critical" system has supporting evidence
- ✓ Cross-border transfers have SCC or BCR documentation
- ✓ Sensitive PII processing has GDPR Article 9 legal basis evidence
- ✓ Evidence is recent (<90 days old) or clearly dated
- ✓ File paths are accessible to auditors

### Phase 8: Review & Approval (2-3 hours)

**Objective:** Validate assessment completeness and obtain stakeholder sign-off

**Steps:**
1. **Self-Review:** Complete quality checklist (Section 6 below)

2. **DPO Review:** 

   - Schedule review meeting with DPO
   - Walk through ROPA (Sheet 4) for GDPR Article 30 compliance
   - Discuss critical gaps and remediation timeline
   - Validate legal basis for all processing activities

3. **Stakeholder Review:**

   - **CISO / Security Team:** Validate system inventory completeness
   - **Legal / Compliance:** Confirm legal basis and cross-border transfer mechanisms
   - **Executive Sponsor:** Approve gap remediation budget and timeline

4. **Sign-Off (Sheet 8):**

   - Assessment Lead (DPO): Methodology, completeness, ROPA compliance
   - CISO: Technical accuracy, system inventory validation
   - Legal/Compliance: Legal basis validity, regulatory compliance
   - Executive Sponsor: Final approval, gap remediation support

**Deliverable:** Sheet 8 complete with all required sign-offs

---

# Sheet-by-Sheet Completion Guidance

## Sheet 1: Instructions & Legend

**Purpose:** Reference guide (read-only, no data entry required)

**What to Do:**
1. Read this sheet first to understand assessment methodology
2. Review PII classification framework
3. Review status legend (Not Started / In Progress / Complete / Validated)
4. Note acceptable evidence types

**No action required** - proceed to Sheet 2.

---

## Sheet 2: PII System Inventory

**Purpose:** Document ALL systems processing PII with classifications

**Step 1: List ALL Systems**

Systematically identify systems by category:

- **CRM / Sales:** Salesforce, HubSpot, Microsoft Dynamics, custom CRM
- **HR / Payroll:** Workday, BambooHR, ADP, SAP SuccessFactors
- **Email / Communication:** Microsoft 365, Google Workspace, Slack, Teams
- **File Storage:** SharePoint, Google Drive, Dropbox, on-premises file shares
- **Marketing Automation:** Mailchimp, Marketo, Pardot, ActiveCampaign
- **Analytics:** Google Analytics, Mixpanel, Amplitude, Adobe Analytics
- **E-Commerce / Shopping Cart:** Shopify, WooCommerce, Magento, custom
- **Payment Processing:** Stripe, PayPal, Authorize.Net, Square
- **Customer Support:** Zendesk, Freshdesk, Intercom, custom ticketing
- **Backup Systems:** Veeam, Acronis, cloud backup services
- **Databases:** PostgreSQL, MySQL, SQL Server, MongoDB, etc.
- **Websites / Web Applications:** Public websites with contact forms, portals
- **Mobile Applications:** iOS/Android apps collecting user data
- **CCTV / Physical Security:** Video surveillance systems, access control logs
- **Other:** Anything else that collects, processes, or stores PII

**Step 2: Complete Required Fields**

For EACH system, enter:

- **System Name:** Clear, recognizable name (e.g., "Salesforce CRM", "Employee File Share")
- **System Owner:** Person responsible for system (name or role)
- **System Type:** Select from dropdown (CRM, HRIS, Email, Database, etc.)
- **PII Processing Role:** Controller (we decide purpose/means) or Processor (vendor processes on our behalf)
- **PII Data Subjects:** Who does this data relate to? (Employees, Customers, Vendors, Job Applicants, Website Visitors)
- **PII Categories:** What personal data fields? (Name, Email, Phone, Address, SSN, Health Data, Payment Info, etc.)
- **PII Classification:** Select from dropdown based on GDPR sensitivity:
  - **Basic PII:** Standard personal data (name, contact info, account numbers)
  - **Sensitive PII:** GDPR Article 9 Special Categories (health, biometric, racial origin, etc.)
  - **Criminal Offense Data:** GDPR Article 10 (criminal convictions, charges)
- **Sensitive PII Types:** If Sensitive, specify type (Health Data, Biometric Data, etc.)
- **Data Volume:** Approximate number of records (order of magnitude is fine: ~100, ~10K, ~1M)
- **Hosting Location:** Where is data physically stored? (On-premises, AWS US-East, Azure West Europe, Switzerland, etc.)
- **Access Level:** Who can access and how many users? (All employees, HR team only, External vendors)
- **Discovery Method:** How was this system identified? (IT Asset Inventory, DLP Scan, System Owner Interview, etc.)
- **Status:** Not Started / In Progress / Complete / Validated

**Step 3: Mark Status**

As you complete each system row, update status:

- **Not Started:** System identified but not yet assessed
- **In Progress:** Assessment started, missing some information
- **Complete:** All information documented, pending validation
- **Validated:** DPO reviewed and approved

**Tips:**

- Start with obvious systems (CRM, HRIS, email) then expand
- Don't forget backups - they contain PII copies!
- Include shadow IT (unapproved cloud services)
- Document physical records (paper files, archived documents)
- Check for PII in unexpected places (logs, caches, temporary files)

**Common Mistakes to Avoid:**

- ❌ **Incomplete inventory:** Missing shadow IT, development environments, backups
- ❌ **Vague descriptions:** "Database" → Should be "Customer Order Database (PostgreSQL)"
- ❌ **Under-classification:** Not identifying Sensitive PII in employee health records
- ❌ **Unknown hosting:** "Cloud" → Should specify provider and region
- ❌ **Missing system owners:** Every system needs an accountable owner

---

## Sheet 3: PII Data Flow Mapping

**Purpose:** Document how PII moves between systems and across borders

**Step 1: Identify Data Flows**

For EACH system in Sheet 2, trace:
1. **Where does PII come from?** (Inbound flows)

   - Data subject directly (web form, mobile app, in-person)
   - Other internal systems (API integration, database sync)
   - Third-party sources (vendor provides data, enrichment services)

2. **Where does PII go within [Organization]?** (Internal flows)

   - System-to-system transfers (CRM → Marketing Automation)
   - Reporting/analytics (production DB → data warehouse)
   - Backup processes (live system → backup storage)

3. **Where does PII go outside [Organization]?** (Outbound flows)

   - Processors (cloud SaaS, vendors performing services)
   - Third parties (marketing partners, analytics providers)
   - Cross-border (data leaving CH/EU jurisdiction)
   - Data subjects (portability exports, account deletion)

**Step 2: Document Each Flow**

For EACH data flow, enter:

- **Flow ID:** Auto-generated (FLOW-001, FLOW-002, etc.)
- **Source System:** Where PII originates (from Sheet 2 System Name)
- **Destination System:** Where PII is sent (from Sheet 2 System Name)
- **PII Categories:** What personal data moves in this flow?
- **Transfer Mechanism:** How is data transferred? (API, SFTP, Manual Export, Database Replication, etc.)
- **Transfer Frequency:** How often? (Real-time, Hourly, Daily, Weekly, On-demand)
- **Transfer Volume:** Approximate records per transfer
- **Cross-Border?:** Yes if data leaves CH/EU jurisdiction, No otherwise
- **Source Country:** Where data originates (Switzerland, Germany, US, etc.)
- **Destination Country:** Where data is transferred to
- **Transfer Safeguard:** If cross-border, what mechanism? (SCCs, BCRs, Adequacy Decision, Derogation)
- **Purpose:** Why is data transferred? (Service delivery, Analytics, Backup, etc.)
- **Data Minimization:** Is transfer limited to necessary data? (Yes / No / Needs Review)
- **Evidence Reference:** Link to DPA, SCC, architecture diagram

**Step 3: Flag Cross-Border Transfers**

For ANY flow where **Cross-Border? = Yes**:

- ✅ Verify transfer safeguard is documented (SCCs, BCRs, Adequacy)
- ✅ Link to evidence (DPA with SCC appendix, BCR approval, adequacy decision)
- ✅ Note for detailed Transfer Impact Assessment (TIA) in A.5.34.6

**Tips:**

- Use network diagrams and API documentation to identify flows
- Check integration logs and middleware (API gateways, message queues)
- Don't forget manual flows (spreadsheet downloads, report emails)
- Cloud providers often have global infrastructure (check data residency settings)

**Common Pitfalls:**

- ❌ **Missing flows:** Forgetting backups, logs, crash reports sent to vendors
- ❌ **Vague mechanisms:** "Cloud sync" → Should specify "Salesforce API REST POST /contacts"
- ❌ **Assuming adequacy:** "US cloud provider" → Check if data residency in EU/CH or needs SCCs
- ❌ **No minimization check:** Transferring entire customer database when only email needed

---

## Sheet 4: Record of Processing Activities (ROPA)

**Purpose:** GDPR Article 30 compliant documentation of all processing activities

**Step 1: Group Systems into Processing Activities**

Don't document every system separately - group related systems into logical processing activities:

**Example Grouping:**

- **Employee Management** = HRIS + Payroll + Time Tracking + Employee File Share
- **Customer Relationship Management** = CRM + Marketing Automation + Support Tickets
- **Website Operations** = Public Website + Analytics + Contact Forms + Newsletter

**Step 2: Create ROPA Entry**

For EACH processing activity, document:

**Activity Identification:**

- **Activity ID:** Auto-generated (ROPA-001, ROPA-002, etc.)
- **Activity Name:** Clear, business-oriented name (e.g., "Employee Onboarding and Management")
- **Processing Purpose:** Why do we process this data? (Employment relationship, Legal compliance, Service delivery, etc.)
- **Systems Involved:** List all systems from Sheet 2 included in this activity

**Data Subject and Data Categories:**

- **Data Subjects:** Who does this data relate to? (Employees, Customers, Job Applicants, Vendors, Website Visitors)
- **PII Categories:** What personal data? (Name, Contact Info, SSN, Health Data, Payment Info, Browsing History, etc.)
- **PII Classification:** Highest classification of any PII in this activity (Basic / Sensitive / Criminal Offense)
- **Special Categories (Art. 9)?:** Yes if Sensitive PII, No otherwise

**Legal Basis:**

- **Legal Basis (GDPR Art. 6):** Consent / Contract / Legal Obligation / Vital Interests / Public Task / Legitimate Interest
- **Legal Basis (GDPR Art. 9, if Sensitive):** Explicit Consent / Employment Law / Vital Interests / Healthcare / Legal Claims / Substantial Public Interest / Research / etc.
- **Legal Basis Description:** Specific justification (e.g., "Employment contract requires payroll processing")

**Recipients:**

- **Internal Recipients:** Which departments access this data? (HR, Finance, IT, Management)
- **External Recipients:** Processors and third parties who receive data
  - Processors: Cloud providers, payroll vendors, marketing platforms
  - Third parties: Banks (for payments), tax authorities (for compliance), marketing partners

**Cross-Border Transfers:**

- **International Transfers?:** Yes if data goes outside CH/EU, No otherwise
- **Transfer Destinations:** Countries where data is transferred (from Sheet 3)
- **Transfer Safeguards:** SCCs, BCRs, Adequacy Decision, Derogation
- **Evidence Reference:** Link to Sheet 3 data flows and Sheet 6 evidence

**Retention:**

- **Retention Period:** How long is data kept? (Be specific: "7 years after termination", not "as long as necessary")
- **Retention Rationale:** Why this period? (Legal requirement, Business need, Consent duration)
- **Deletion Process:** How is data deleted? (Automated purge, Manual deletion request, End-of-life system decommissioning)

**Technical and Organizational Measures:**

- **Security Measures Summary:** High-level description (NOT detailed technical specs)
  - Example: "Encryption in transit (TLS 1.3) and at rest (AES-256), role-based access control, audit logging, annual security audits"
  - Reference: "See ISMS-IMP-A.5.34.4 (TOMs Assessment) for detailed control implementation"

**Step 3: Validate Completeness**

GDPR Article 30 mandates these elements - ensure ALL are documented:

- ✅ Controller identity and contact details (in assessment header)
- ✅ Purposes of processing (Processing Purpose field)
- ✅ Categories of data subjects (Data Subjects field)
- ✅ Categories of personal data (PII Categories field)
- ✅ Categories of recipients (Internal/External Recipients fields)
- ✅ Transfers to third countries (International Transfers section)
- ✅ Retention periods (Retention Period field)
- ✅ General description of security measures (Security Measures Summary)

**Tips:**

- One ROPA entry can cover multiple systems if they serve the same purpose
- Be specific about legal basis - "Legitimate Interest" requires balancing test (LIA)
- Retention periods should be defensible (legal requirement or business need)
- List processors by name (not "cloud vendors" - say "AWS, Microsoft Azure, Salesforce")

**Common Pitfalls:**

- ❌ **Vague purpose:** "Business operations" → Should be specific like "Customer service delivery"
- ❌ **Missing Art. 9 basis:** Sensitive PII needs BOTH Art. 6 AND Art. 9 legal basis
- ❌ **Generic retention:** "As long as needed" → Must specify period or criteria
- ❌ **Incomplete recipients:** Only listing processors, forgetting internal departments
- ❌ **No transfer safeguards:** International transfers without documented SCCs/BCRs

---

## Sheet 5: PII Discovery Gaps

**Purpose:** Identify non-compliant processing and plan remediation

**Step 1: Review Sheets 2-4 for Gaps**

Common gap categories:

- **Missing Legal Basis:** Processing activity has no documented legal basis
- **Inadequate Safeguards:** Cross-border transfers without SCCs or BCRs
- **Classification Issues:** PII sensitivity not properly identified
- **Retention Violations:** Data kept longer than legally permitted or without justification
- **Undocumented Processing:** Shadow IT discovered, not in ROPA
- **Access Control Deficiencies:** Unauthorized access to PII systems
- **Missing Processor Agreements:** Third parties processing PII without DPA

**Step 2: Document Each Gap**

For EACH gap identified, enter:

- **Gap ID:** Auto-generated (2024-GAP-001, etc.)
- **Status:** Open / In Progress / Resolved / Accepted (risk accepted)
- **Gap Type:** Select from dropdown (Legal Basis Missing, Inadequate Safeguards, etc.)
- **Gap Description:** Clear explanation of what's wrong
- **System/Activity Affected:** Which systems or ROPA entries are impacted?
- **Risk Level:** Critical / High / Medium / Low (based on GDPR violation severity)
- **Risk Justification:** Why this risk rating?
- **Remediation Action:** What needs to be done to close the gap?
- **Remediation Owner:** Person responsible for fixing
- **Target Completion Date:** Deadline (risk-based prioritization)
- **Actual Completion Date:** When gap was actually closed (if Status = Resolved)

**Risk Rating Guidelines:**

**Critical Risk (Immediate action required):**

- Unlawful processing (no valid legal basis under GDPR Art. 6)
- Sensitive PII without Art. 9 legal basis
- Cross-border transfers to non-adequate countries without SCCs/BCRs
- Data breach imminent (no security controls)

**High Risk (Action within 30 days):**

- Inaccurate ROPA (missing processing activities)
- Retention violations (data kept beyond legal/business justification)
- Missing processor DPAs (processors without contracts)
- Inadequate consent (not meeting GDPR Art. 7 requirements)

**Medium Risk (Action within 90 days):**

- Incomplete documentation (missing evidence)
- Access control issues (too broad access permissions)
- Data minimization failures (collecting more than necessary)
- Shadow IT without risk assessment

**Low Risk (Action within 180 days):**

- Process improvements (documentation formatting, ROPA descriptions)
- Training needs (staff unaware of policies)
- Tool enhancements (better PII discovery automation)

**Step 3: Prioritize Remediation**

- **Sort by Risk Level** (Critical → High → Medium → Low)
- **Consider effort** (quick wins for low-effort high-risk items)
- **Bundle related gaps** (e.g., all missing DPAs in one procurement project)

**Tips:**

- Be honest about gaps - hiding them only increases risk
- Involve Legal/Compliance for risk rating validation
- Set realistic target dates (consider resource availability)
- Track remediation progress (update Status regularly)

**Common Gaps:**
1. "Shadow IT: Marketing team using unapproved cloud survey tool with customer data, no DPA, no legal basis documented"
2. "Cross-border transfer: Customer data hosted on US-based AWS instances, no SCCs in place"
3. "Retention violation: Employee records kept indefinitely, Swiss law requires deletion 10 years after termination"
4. "Missing Art. 9 basis: Health insurance data processed for employee benefits without valid Art. 9 legal basis"
5. "Development environment: Production PII copied to dev/test systems without proper access controls or data masking"

---

## Sheet 6: Evidence Register

**Purpose:** Link assessment assertions to supporting documentation

**Step 1: Identify Evidence Needs**

For key assertions requiring proof:

- **System inventory:** Architecture diagrams, admin console screenshots
- **PII classification:** DLP scan reports, database schemas
- **Data flows:** API documentation, integration diagrams, network topology
- **Legal basis:** Privacy notices, consent forms, LIAs (Legitimate Interest Assessments)
- **Cross-border transfers:** SCCs with processors, BCRs, adequacy decisions
- **Retention:** Retention schedules, deletion procedures, policy documents
- **Security measures:** TOMs assessment (A.5.34.4), security audit reports

**Step 2: Register Evidence**

For EACH evidence artifact, enter:

- **Evidence ID:** Unique identifier (EV-SYS-001, EV-FLOW-001, EV-ROPA-001)
- **Related Sheet/Row:** Which assertion does this support? (e.g., "Sheet 2, Row 5: Salesforce CRM")
- **Evidence Type:** Screenshot / Document / Report / Contract / Policy / Audit / Other
- **Evidence Description:** Brief summary (e.g., "Salesforce admin console showing PII fields configured")
- **File Location:** Path to evidence file (SharePoint URL, file share path, physical location)
- **Evidence Date:** When was evidence created or captured?
- **Collected By:** Who gathered this evidence?
- **Verification Status:** Verified / Pending / Expired
- **Verified By:** Who validated evidence adequacy?
- **Notes:** Any additional context

**Step 3: Organize Evidence**

Suggested folder structure:
```
ISMS-A.5.34.1-PII-Assessment-Evidence/
├── 01-System-Inventory/
│   ├── CRM_Salesforce_Screenshot_20240115.png
│   ├── HRIS_Architecture_Diagram_v2.1.pdf
│   └── Cloud_Services_Inventory_20240115.xlsx
├── 02-Data-Flows/
│   ├── API_Integration_CRM-to-Marketing.pdf
│   ├── DPA_AWS_with_SCC.pdf
│   └── Network_Diagram_Data_Flows.vsdx
├── 03-ROPA/
│   ├── Privacy_Notice_Customers_v3.0.pdf
│   ├── Privacy_Notice_Employees_v2.1.pdf
│   ├── Consent_Form_Marketing_Email.pdf
│   └── LIA_Customer_Profiling.docx
├── 04-Cross-Border-Transfers/
│   ├── SCC_AWS_EU_Standard_Clauses.pdf
│   ├── SCC_Salesforce_Signed_20230601.pdf
│   └── Adequacy_Decision_Switzerland_EU.pdf
└── 05-Security-Measures/
    ├── TOMs_Assessment_A.5.34.4_Summary.pdf
    ├── ISO_27001_Certificate_Valid_2024-2027.pdf
    └── Penetration_Test_Report_2023.pdf
```

**Tips:**

- Collect evidence as you complete assessment (don't wait until the end)
- Sanitize sensitive data in screenshots (redact account numbers, passwords)
- Include metadata (creation date, version, author)
- Store evidence in access-controlled location (not public file share)
- Keep evidence for audit cycle (typically 1+ years)

**Common Evidence Gaps:**

- ❌ "We have SCCs but can't find the signed copies"
- ❌ "DLP scan was 2 years ago, need fresh evidence"
- ❌ "Privacy notice is outdated, doesn't reflect current processing"
- ❌ "Evidence files on personal laptop, not accessible to auditors"
- ❌ "Screenshots don't show date/timestamp - can't prove currency"

---

## Sheet 7: Dashboard

**Purpose:** Executive summary with compliance metrics (auto-calculated, read-only)

**What This Shows:**

**Section 1: PII System Inventory Summary**

- Total systems identified
- Systems by PII classification (Basic / Sensitive / Criminal Offense)
- Systems by hosting location (On-premises / Cloud CH / Cloud EU / Cloud Non-EU)
- Systems by status (Validated / Complete / In Progress / Not Started)

**Section 2: Data Flow Summary**

- Total data flows documented
- Internal flows vs. cross-border transfers
- Cross-border transfers by safeguard mechanism (SCCs / BCRs / Adequacy / None)
- Flows by transfer frequency (Real-time / Daily / Weekly / On-demand)

**Section 3: ROPA Summary**

- Total processing activities documented
- Activities by legal basis (Consent / Contract / Legal Obligation / Legitimate Interest)
- Activities involving Sensitive PII (requiring Art. 9 basis)
- Activities with cross-border transfers

**Section 4: Gap Analysis**

- Total gaps identified
- Gaps by risk level (Critical / High / Medium / Low)
- Gap remediation status (Open / In Progress / Resolved / Accepted)
- Overdue gaps (past target completion date)

**Section 5: Evidence Status**

- Total evidence artifacts collected
- Evidence by type (Screenshot / Document / Report / Contract)
- Evidence verification status (Verified / Pending / Expired)

**Section 6: Overall Compliance Score**

Formula:
```
Compliance Score = (
  System_Inventory_Completeness * 0.25 +
  Data_Flow_Documentation * 0.20 +
  ROPA_Completeness * 0.30 +
  Gap_Remediation_Progress * 0.15 +
  Evidence_Coverage * 0.10
) * 100
```

**Interpretation:**

- **90-100%:** Excellent - Audit-ready
- **70-89%:** Good - Minor gaps to address
- **50-69%:** Fair - Significant work needed
- **<50%:** Poor - Major compliance issues

**What You Do:**

- Review dashboard metrics to validate completeness
- Use for executive briefings and management reporting
- Identify areas needing more work (low scores indicate gaps)
- Track progress over time (quarterly updates)

**No action required on this sheet** - all metrics auto-calculate from Sheets 2-6.

---

## Sheet 8: Approval & Sign-Off

**Purpose:** Stakeholder validation and formal approval

**Step 1: Complete Assessment**

Before seeking approvals:

- ✅ All systems documented (Sheet 2 Status = Complete or Validated)
- ✅ All data flows mapped (Sheet 3)
- ✅ ROPA complete with all processing activities (Sheet 4)
- ✅ Gaps identified and remediation plans documented (Sheet 5)
- ✅ Evidence collected and registered (Sheet 6)
- ✅ Dashboard metrics reviewed and reasonable (Sheet 7)
- ✅ Quality checklist passed (Section 6 below)

**Step 2: Obtain Sign-Offs**

**Required Approvers:**

1. **Assessment Lead (DPO / Privacy Officer)**

   - **Approval Scope:** Assessment methodology, completeness, ROPA GDPR Article 30 compliance
   - **What They Check:** Are all processing activities documented? Is legal basis valid? Are cross-border transfers properly safeguarded?

2. **Chief Information Security Officer (CISO)**

   - **Approval Scope:** Technical accuracy, system inventory completeness, data flow validation
   - **What They Check:** Are all PII systems identified? Are data flows technically accurate? Is hosting location correct?

3. **Legal / Compliance Officer**

   - **Approval Scope:** Legal basis validity, regulatory compliance, cross-border transfer mechanisms
   - **What They Check:** Are legal bases defensible? Are SCCs in place for international transfers? Is retention legally compliant?

4. **Executive Sponsor (e.g., CFO, COO)**

   - **Approval Scope:** Final approval, gap remediation resource allocation, accountability
   - **What They Check:** Are critical gaps being addressed? Is remediation timeline realistic? Is budget allocated?

**Step 3: Schedule Review Meetings**

Don't just send workbook via email - schedule review sessions:
1. **DPO Review (1-2 hours):** Walk through ROPA, discuss legal basis, prioritize gaps
2. **CISO Review (30-60 min):** Validate system inventory, verify data flow accuracy
3. **Legal Review (30-60 min):** Confirm transfer mechanisms, review sensitive PII processing
4. **Executive Briefing (15-30 min):** Present dashboard, highlight critical gaps, request approval

**Step 4: Document Approvals**

For EACH approver, record:

- **Signatory Role:** (pre-populated from required roles)
- **Signatory Name:** Person who approved
- **Signature / Electronic Approval:** E-signature, email confirmation, or meeting notes reference
- **Signature Date:** When approval was given
- **Approval Scope:** What they approved (pre-populated)
- **Comments:** Any conditions, concerns, or notes from approver
- **Contact Email:** For follow-up if needed

**Next Steps After Approval:**
1. Distribute final assessment to stakeholders
2. Begin gap remediation (execute plans from Sheet 5)
3. Schedule quarterly review (update Sheets 2-4 for changes)
4. Link to downstream assessments (A.5.34.2 Legal Basis uses this ROPA)

---

# Evidence Collection

## What Evidence to Collect

**For System Inventory (Sheet 2):**

- ✓ IT asset inventory exports (from CMDB or asset management tool)
- ✓ Screenshots of system admin consoles showing PII fields configured
- ✓ Architecture diagrams showing system interconnections
- ✓ DLP scan reports identifying PII locations
- ✓ Database schemas with PII columns highlighted
- ✓ Cloud service subscription lists and configurations

**For Data Flows (Sheet 3):**

- ✓ API integration documentation (endpoints, data payloads)
- ✓ Network diagrams showing data movement
- ✓ Data Processing Agreements (DPAs) with processors
- ✓ Standard Contractual Clauses (SCCs) for cross-border transfers
- ✓ Binding Corporate Rules (BCRs) approval documentation
- ✓ Adequacy decision references (for transfers to adequate countries)

**For ROPA (Sheet 4):**

- ✓ Privacy notices (customer-facing, employee-facing)
- ✓ Consent forms and consent management platform records
- ✓ Legitimate Interest Assessments (LIAs) for Art. 6(1)(f) processing
- ✓ Contracts establishing processing necessity (for Art. 6(1)(b))
- ✓ Legal obligation register (employment law, tax law, sector regulations)
- ✓ Retention schedules and deletion procedures

**For Security Measures:**

- ✓ TOMs Assessment (ISMS-IMP-A.5.34.4) summary
- ✓ ISO 27001 certificate (if certified)
- ✓ SOC 2 reports (if applicable)
- ✓ Penetration test reports
- ✓ Security audit findings
- ✓ Encryption configuration evidence (TLS, at-rest encryption)

## Evidence Storage Best Practices

**Access Control:**

- Store in secure, access-controlled location (not public file share)
- Limit access to assessment team, DPO, auditors, management
- Use document management system with audit trails (SharePoint, Confluence)
- Don't email evidence - use secure file sharing links

**Organization:**

- Use consistent folder structure (see Sheet 6 guidance)
- Name files descriptively (System_EvidenceType_Date.ext)
- Include metadata (creation date, version, author)
- Maintain index (Sheet 6 Evidence Register serves this purpose)

**Retention:**

- Keep evidence for full audit cycle (typically 1+ years minimum)
- After audit, archive but don't delete (useful for trend analysis)
- Update evidence when it expires (e.g., certificate renewals, updated policies)

**Sanitization:**

- Redact sensitive data in screenshots (account numbers, passwords, personal details)
- Remove confidential business information (financial data, strategy)
- Ensure evidence is appropriate for external auditor review

## Common Evidence Gaps

**Gap 1: "We do this but have no evidence"**

- **Problem:** Claiming PII is encrypted but no configuration screenshot or audit report
- **Solution:** Generate evidence retroactively (take screenshots, export configurations)
- **Fallback:** Acknowledge gap, document remediation plan

**Gap 2: Evidence exists but not collected**

- **Problem:** SCCs signed with vendor but not in evidence folder
- **Solution:** Request copies from Legal/Procurement, add to Sheet 6

**Gap 3: Evidence too old**

- **Problem:** DLP scan from 2 years ago doesn't reflect current state
- **Solution:** Re-run scan, collect fresh evidence within 90 days of assessment

**Gap 4: Evidence not sanitized**

- **Problem:** Screenshot shows employee SSNs or customer payment data
- **Solution:** Re-capture with sensitive data masked/redacted

**Gap 5: Evidence not organized**

- **Problem:** Random files scattered across email, personal folders
- **Solution:** Centralize in structured repository, register in Sheet 6

---

# Common Pitfalls

## Pitfall 1: Incomplete System Inventory

**Mistake:** Not identifying all PII-containing systems

**Example:** Forgetting about:

- Backup systems (backups contain PII copies!)
- Development/test environments (often contain production PII copies)
- Shadow IT (unapproved SaaS services employees are using)
- Legacy systems (old applications still running with historical data)
- Physical records (paper files, archived documents)
- Vendor-managed systems (processors with direct access to PII)

**Why It Happens:**

- Focusing only on "obvious" systems (CRM, HRIS)
- Not asking employees about tools they use
- Assuming IT has complete visibility (they don't know about shadow IT)
- Forgetting offline/physical data storage

**How to Avoid:**

- Use discovery questionnaire with all departments
- Run cloud access security broker (CASB) scans for shadow IT
- Check procurement records for SaaS subscriptions
- Review backup job listings
- Ask: "What tools do you use to do your job?" (not just "What PII systems exist?")

**Assessment Impact:** Incomplete inventory = ROPA non-compliance = GDPR violation

## Pitfall 2: Under-Classifying Sensitive PII

**Mistake:** Classifying Sensitive PII as Basic PII

**Example:**

- Employee birthdates combined with health insurance enrollment → Contains health data (Sensitive PII)
- Customer profiles with inferred ethnicity from name/address → Racial/ethnic origin data (Sensitive PII)
- Biometric authentication (fingerprint, face recognition) → Biometric data (Sensitive PII)
- Political party membership in donor database → Political opinions (Sensitive PII)

**Why It Happens:**

- Not recognizing indirect Sensitive PII (inferred or derived data)
- Treating aggregated data as non-sensitive (aggregation doesn't remove special category status)
- Assuming "business data" isn't personal data (job title = personal data if identifiable)

**How to Avoid:**

- Review GDPR Article 9 list carefully (health, genetic, biometric, racial origin, political opinions, religious beliefs, trade union membership, sex life/sexual orientation)
- Check for derived Sensitive PII (profiling, inference, enrichment)
- When in doubt, classify as Sensitive (over-classification is safer than under)

**Assessment Impact:** Incorrect classification = Inadequate safeguards = Data breach risk

## Pitfall 3: Ignoring Cross-Border Transfers

**Mistake:** Not identifying data transfers outside CH/EU

**Example:**

- "We use Microsoft 365" → Data may be processed in US datacenters (cross-border transfer)
- "Our website analytics" → Google Analytics sends data to US servers (cross-border transfer)
- "Customer support ticketing" → Zendesk data stored in US (cross-border transfer)
- "Email service" → Mail routing through non-EU servers (cross-border transfer)

**Why It Happens:**

- Assuming cloud providers only use local datacenters (they often don't)
- Not checking data residency settings in SaaS configurations
- Thinking "adequacy decision" means no safeguards needed (Switzerland-EU adequacy doesn't cover CH-US!)
- Relying on vendor claims without verification

**How to Avoid:**

- **Check vendor contracts:** Where is data stored? Where is data processed?
- **Review service configurations:** Data residency settings, region selection
- **Map actual data routes:** Use network monitoring, API logs
- **Verify adequacy:** Only EU member states + handful of others have adequacy decisions
- **Assume transfer if unsure:** Better to document unnecessary SCC than miss required one

**Assessment Impact:** Undocumented cross-border transfers = GDPR Article 46 violation = Supervisory authority enforcement

## Pitfall 4: Vague or Missing Legal Basis

**Mistake:** Not documenting valid legal basis for processing

**Example:**

- "We need this data for our business" → Not a legal basis (need specific Art. 6 basis)
- "We have legitimate interest" → Without documented LIA (Legitimate Interest Assessment), this is non-compliant
- "Customers gave consent" → But no proof of consent (no timestamp, no record, not freely given)
- "It's in our privacy policy" → Privacy notice doesn't establish legal basis, only informs about it

**Why It Happens:**

- Confusing business justification with legal basis
- Thinking "legitimate interest" is a catch-all (it requires balancing test)
- Assuming implied consent (consent must be explicit, freely given, specific)
- Not involving Legal/Compliance in legal basis determination

**How to Avoid:**

- **Review GDPR Article 6 options:** Consent, Contract, Legal Obligation, Vital Interests, Public Task, Legitimate Interest
- **Document specific basis:** Not just "consent" but "explicit opt-in consent via registration form on 2024-01-15"
- **Complete LIA if using legitimate interest:** Must document necessity, balancing test, safeguards
- **Validate with Legal/Compliance:** Don't self-determine legal basis for Sensitive PII

**Assessment Impact:** No legal basis = Unlawful processing = GDPR Article 6 violation = Up to €20M or 4% revenue fine

## Pitfall 5: Indefinite Retention

**Mistake:** Keeping PII forever without justification

**Example:**

- "We keep customer data indefinitely" → No retention limit violates storage limitation principle
- "We might need it someday" → Not a valid retention justification
- "Retention period: As long as necessary" → Too vague, must specify period or criteria
- "We delete data when customer requests" → Reactive deletion doesn't satisfy proactive retention limits

**Why It Happens:**

- Fear of deleting data that might be useful
- No clear business justification for retention
- Technical difficulty of implementing automated deletion
- Not considering legal retention requirements (may require longer retention for some data)

**How to Avoid:**

- **Define retention period for EACH ROPA entry:** Based on legal requirement or business need
- **Be specific:** "7 years after contract termination" not "as long as needed"
- **Balance requirements:** Legal retention (tax law) vs. data minimization (delete when no longer needed)
- **Implement deletion processes:** Automated purging, manual review cycles, system decommissioning
- **Document exceptions:** If legal hold or litigation prevents deletion, document why

**Assessment Impact:** Indefinite retention = GDPR Article 5(1)(e) violation = Storage limitation breach

## Pitfall 6: Aspirational Assessment

**Mistake:** Documenting what SHOULD be true, not what IS true

**Example:**

- "All PII is encrypted" → But dev/test environments use plaintext databases
- "We have SCCs with all processors" → But several vendors still need to sign updated SCCs
- "Consent is properly documented" → But consent records were lost in system migration
- "Access controls are role-based" → But many users have admin rights "just in case"

**Why It Happens:**

- Pressure to show compliance
- Confusion between policy requirements and actual implementation
- Optimism bias ("we're doing this right")
- Not verifying claims (assuming controls are working without testing)

**How to Avoid:**

- **Verify everything:** Don't assume - check actual configurations, run tests
- **Document current state:** What exists today, not what's planned
- **Use evidence to validate:** If you can't prove it, don't claim it
- **Mark gaps honestly:** Better to document gap with remediation plan than false compliance
- **Test controls:** For critical claims (encryption, access controls), perform spot checks

**Assessment Impact:** False claims = Auditor distrust = Re-assessment required = Delayed certification

## Pitfall 7: No System Owner Accountability

**Mistake:** Systems without designated owners

**Example:**

- "System Owner: IT Department" → Too generic (who in IT specifically?)
- "System Owner: Unknown" → Unacceptable for audit
- "System Owner: Former employee" → Owner left 2 years ago, not updated
- "System Owner: [blank]" → Assessment incomplete

**Why It Happens:**

- Treating system ownership as administrative detail
- Not establishing clear accountability in organization
- Legacy systems where original owner is long gone
- Shadow IT discovered with no clear owner

**How to Avoid:**

- **Assign specific person:** Name and email, not department or role title
- **Establish ownership as part of system lifecycle:** New systems require owner before deployment
- **Maintain ownership registry:** Update when people change roles or leave
- **Escalate ownership gaps:** If system has no owner, assign one or decommission system

**Assessment Impact:** No ownership = No accountability = Controls not maintained = Security/privacy risk

## Pitfall 8: Confusing Processors and Controllers

**Mistake:** Misidentifying PII processing role

**Example:**

- **Controller vs. Processor confusion:**
  - Salesforce is a **Processor** (we control purpose, Salesforce processes on our behalf)
  - Marketing partner is a **Controller** (they decide what to do with shared data)
  - Cloud backup service is a **Processor** (we control what's backed up)

- **Joint Controller mistake:**
  - Data sharing with business partner where BOTH decide processing purposes = Joint Controllers
  - Requires joint controller agreement (GDPR Article 26)

**Why It Happens:**

- Not understanding controller vs. processor distinction
- Assuming all vendors are processors (some are independent controllers)
- Not reading vendor contracts carefully (DPA may specify role)

**How to Avoid:**

- **Ask:** Who determines WHY and HOW PII is processed?
  - **We decide:** Vendor is Processor → Need DPA with GDPR Article 28 clauses
  - **Vendor decides:** Vendor is Controller → No DPA, but need data sharing agreement
  - **Both decide:** Joint Controllers → Need Article 26 agreement
- **Review contracts:** Vendor contract should specify role
- **When in doubt:** Consult Legal/DPO

**Assessment Impact:** Incorrect role = Missing DPA = GDPR Article 28 violation = Processor liability

---

# Quality Checklist

Complete this checklist before seeking approvals:

## Sheet 2: PII System Inventory

- [ ] All PII-containing systems identified (including backups, dev/test, shadow IT)
- [ ] System Owner specified for every system (specific person, not "IT Department")
- [ ] PII Classification determined for all systems (Basic / Sensitive / Criminal Offense)
- [ ] Hosting Location documented (specific cloud region or on-premises location)
- [ ] Data Volume estimated (order of magnitude sufficient)
- [ ] Status = "Complete" or "Validated" for all critical systems
- [ ] No systems with "Unknown" or "TBD" values remaining

## Sheet 3: PII Data Flow Mapping

- [ ] All significant data flows documented (internal + cross-border)
- [ ] Cross-border transfers identified with "Cross-Border? = Yes"
- [ ] Transfer Safeguards documented for ALL cross-border flows (SCCs / BCRs / Adequacy)
- [ ] Source/Destination systems match Sheet 2 System Names (dropdown validation)
- [ ] Data Minimization assessed (transfer only necessary data)
- [ ] Evidence Reference links to Sheet 6 for critical flows (SCCs, DPAs)

## Sheet 4: ROPA (Record of Processing Activities)

- [ ] All processing activities documented (every system appears in at least one ROPA entry)
- [ ] GDPR Article 6 legal basis documented for ALL activities
- [ ] GDPR Article 9 legal basis documented for Sensitive PII processing
- [ ] Retention Period specified (not "as long as necessary" - must be specific)
- [ ] Recipients identified (internal departments + external processors + third parties)
- [ ] Cross-border transfers referenced (link to Sheet 3)
- [ ] Security Measures summary provided (reference to A.5.34.4 TOMs assessment)

## Sheet 5: PII Discovery Gaps

- [ ] All compliance gaps identified and documented
- [ ] Risk Level assigned for each gap (Critical / High / Medium / Low)
- [ ] Remediation Action defined (clear, specific, actionable)
- [ ] Remediation Owner assigned (specific person responsible)
- [ ] Target Completion Date set (risk-based prioritization)
- [ ] Critical gaps have immediate action plans (no Critical gaps without remediation)

## Sheet 6: Evidence Register

- [ ] Evidence collected for all critical assertions (see Section 5)
- [ ] Evidence Register populated with links to supporting documentation
- [ ] Cross-border transfer evidence available (SCCs, BCRs, adequacy decisions)
- [ ] Legal basis evidence documented (privacy notices, consent forms, LIAs)
- [ ] Evidence is recent (<90 days old) or clearly dated
- [ ] Evidence stored in access-controlled location (not personal folders)

## Sheet 7: Dashboard

- [ ] Dashboard metrics reviewed and reasonable
- [ ] Overall Compliance Score calculated (target ≥70% for audit readiness)
- [ ] No unexpected anomalies (e.g., 0 cross-border transfers when using cloud services)

## Sheet 8: Approval & Sign-Off

- [ ] All required approvers identified (DPO, CISO, Legal, Executive Sponsor)
- [ ] Review meetings scheduled
- [ ] Approvers have access to complete assessment (all sheets + evidence)

## Cross-Sheet Validation

- [ ] System Names in Sheet 3 Data Flows match Sheet 2 System Inventory
- [ ] ROPA entries (Sheet 4) cover all systems from Sheet 2
- [ ] Evidence References (Sheets 2-5) link to Sheet 6 Evidence Register
- [ ] Gap remediation (Sheet 5) addresses deficiencies identified in Sheets 2-4

## Overall Assessment Quality

- [ ] Assessment completed by qualified personnel (DPO involvement)
- [ ] No placeholder text or dummy data remaining
- [ ] All dropdown fields use valid options (no free-text where dropdown expected)
- [ ] Dates in consistent format (DD.MM.YYYY or YYYY-MM-DD)
- [ ] Assessment internally consistent (no contradictory statements)
- [ ] Assessment language clear and professional (suitable for external audit)

---

# Review & Approval

## Self-Review

Before presenting to stakeholders:
1. Complete Quality Checklist (Section 7 above) - all items checked
2. Run spell-check and grammar review
3. Validate formulas in Dashboard (Sheet 7) are calculating correctly
4. Spot-check evidence links (open a few to verify they work)
5. Read assessment from auditor perspective: "Would this satisfy GDPR Article 30 requirements?"

## DPO Review (Mandatory)

**Schedule:** 1-2 hour review meeting with DPO / Privacy Officer

**DPO Reviews:**

- **ROPA Compliance:** Does Sheet 4 meet GDPR Article 30 requirements?
- **Legal Basis Validity:** Are legal bases defensible? Do Sensitive PII activities have Article 9 basis?
- **Cross-Border Transfers:** Are SCCs/BCRs in place for all international transfers?
- **Gap Severity:** Are Critical/High gaps accurately rated? Is remediation timeline realistic?
- **Overall Completeness:** Has assessment covered all processing activities?

**Outcome:** DPO approval or list of required corrections

## CISO / Security Review

**Schedule:** 30-60 minute review with CISO or Security Team Lead

**CISO Reviews:**

- **System Inventory Completeness:** Are all PII systems identified? Any shadow IT missed?
- **Data Flow Accuracy:** Do data flows match network architecture?
- **Security Classification:** Is PII sensitivity correctly identified?
- **Technical Controls:** Are security measures (Sheet 4, ROPA) accurately described?

**Outcome:** CISO approval or required corrections

## Legal / Compliance Review

**Schedule:** 30-60 minute review with Legal Counsel / Compliance Officer

**Legal Reviews:**

- **Legal Basis Validity:** Are legal bases legally defensible?
- **Cross-Border Transfer Mechanisms:** Are SCCs/BCRs sufficient for all transfers?
- **Retention Compliance:** Do retention periods comply with legal requirements?
- **Regulatory Alignment:** Does assessment satisfy Swiss FADP and GDPR requirements?

**Outcome:** Legal approval or required corrections

## Executive Briefing

**Schedule:** 15-30 minute presentation to Executive Sponsor (CFO, COO, or CEO)

**Executive Briefing Contents:**
1. **Dashboard Summary (Sheet 7):** Overall compliance score, key metrics
2. **Critical Gaps (Sheet 5):** What's broken and needs immediate fix?
3. **Remediation Plan:** Timeline, budget requirements, resource needs
4. **Regulatory Risk:** What happens if gaps aren't addressed?
5. **Next Steps:** Downstream assessments (A.5.34.2-6), quarterly updates

**Outcome:** Executive approval to proceed with remediation and downstream assessments

## Final Sign-Off (Sheet 8)

After all reviews complete and corrections made:
1. **Update Sheet 8** with approver names and dates
2. **Collect signatures** (electronic or physical)
3. **Version workbook** as FINAL (e.g., `ISMS_A_5_34_1_PII_Assessment_20240115_v1.0_FINAL.xlsx`)
4. **Distribute** to stakeholders (DPO, CISO, Legal, Management, Auditors)
5. **Archive** in secure document repository with access controls

---

# Next Steps After Completion

## Immediate Actions

1. **Share Assessment Results**

   - Executive summary to management (Dashboard + critical gaps)
   - Detailed findings to DPO, Legal, CISO
   - Gap assignments to system owners and remediation teams

2. **Begin Gap Remediation**

   - Prioritize Critical and High risk gaps
   - Allocate resources (budget, personnel, time)
   - Track progress weekly (update Sheet 5 Status column)

3. **Publish Approved ROPA**

   - Make available to authorized personnel (DPO, Legal, Compliance, Audit)
   - Restrict access (ROPA contains sensitive processing details)
   - Establish update process (how to add new processing activities)

## Integration with Downstream Assessments

This assessment (A.5.34.1) provides foundational data for:

- **ISMS-IMP-A.5.34.2 (Legal Basis):** Uses ROPA (Sheet 4) as input for detailed legal basis validation and Legitimate Interest Assessments
- **ISMS-IMP-A.5.34.3 (Data Subject Rights):** Uses PII inventory (Sheet 2) to identify systems for access/erasure request fulfillment
- **ISMS-IMP-A.5.34.4 (TOMs):** Uses PII classification (Sheet 2) to determine appropriate technical and organizational security measures
- **ISMS-IMP-A.5.34.5 (DPIA):** Uses ROPA (Sheet 4) to identify high-risk processing requiring Data Protection Impact Assessment
- **ISMS-IMP-A.5.34.6 (Cross-Border Transfers):** Uses data flows (Sheet 3) for detailed Transfer Impact Assessments (TIAs)

**Sequence:** Complete A.5.34.1 first, then proceed with other assessments in parallel or sequence.

## Ongoing Maintenance

**Quarterly Updates (2-4 hours):**

- Review Sheet 2 for new systems or decommissioned systems
- Update Sheet 3 for changed data flows (new integrations, terminated vendors)
- Refresh Sheet 4 ROPA for new processing activities or changed purposes
- Update Sheet 5 gap status (mark resolved, add new gaps)
- Re-run Dashboard (Sheet 7) to track compliance trends

**Triggered Updates:**

- **New system deployment:** Assess PII before production (add to Sheet 2)
- **M&A activity:** Assess acquired company's PII processing (merge into ROPA)
- **New vendor/processor:** Ensure DPA in place, add to data flows (Sheet 3)
- **Material processing change:** Update ROPA within 30 days (GDPR requirement)
- **Regulatory change:** Re-assess legal basis if law changes (e.g., new FADP requirements)

**Annual Validation (Full Re-Assessment):**

- Comprehensive review of all ROPA entries
- Re-interview system owners
- Re-run automated PII discovery tools (DLP scans)
- Validate evidence still current (refresh expired evidence)
- Obtain fresh sign-offs (Sheet 8)

## Using Assessment for Audits

**ISO 27001 Certification Audits:**

- Provide Sheets 2-4 as evidence for Control A.5.34
- Dashboard (Sheet 7) gives auditor compliance summary
- Gap remediation (Sheet 5) demonstrates continual improvement
- Evidence register (Sheet 6) provides audit trail

**Data Protection Authority (DPA) Audits:**

- Sheet 4 (ROPA) satisfies GDPR Article 30 requirement
- Sheet 3 (Data Flows) supports Article 46 transfer compliance
- Legal basis documentation demonstrates Article 6/9 compliance
- Gap remediation shows accountability and risk management

**Internal Audits:**

- Use Dashboard (Sheet 7) for quarterly compliance reporting
- Track gap closure progress (Sheet 5) for management reviews
- Evidence register (Sheet 6) supports internal control testing

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
