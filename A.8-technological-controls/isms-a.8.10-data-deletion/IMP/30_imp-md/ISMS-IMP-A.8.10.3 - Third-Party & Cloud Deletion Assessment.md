**ISMS-IMP-A.8.10.3 - Third-Party & Cloud Deletion Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.10.3 |
| **Version** | 1.0 |
| **Assessment Area** | Third-Party & Cloud Service Provider Deletion Capabilities |
| **Related Policy** | ISMS-POL-A.8.10, Section 2.3 (Third-Party & Cloud Deletion) |
| **Purpose** | Assess cloud provider and third-party vendor deletion capabilities, contractual obligations, and verification procedures to ensure data deletion extends beyond organization-controlled infrastructure |
| **Target Audience** | Cloud Administrators, Vendor Management, Legal Counsel, Procurement, Data Protection Officers, Compliance Officers, IT Operations, Auditors |
| **Assessment Type** | Contractual & Operational Compliance |
| **Review Cycle** | Annual or Upon Vendor Contract Renewal |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Third-Party & Cloud Deletion assessment workbook | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** Cloud Administrators, Vendor Management, Legal Counsel, Data Protection Officers

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organization]'s **third-party and cloud service provider deletion capabilities** to ensure data stored with external vendors is properly deleted when retention periods expire, in compliance with ISO/IEC 27001:2022 Control A.8.10, GDPR Article 28 processor obligations, and contractual deletion requirements.

**Scope:** External data deletion across 5 critical assessment areas:

1. **Cloud Provider Deletion Capabilities** - IaaS, PaaS, SaaS provider deletion policies and verification
2. **SaaS Application Data Deletion** - CRM, HR, Marketing, Collaboration tool deletion
3. **Vendor Contract Assessment** - Deletion clauses, SLAs, and contractual obligations
4. **Subprocessor Mapping** - Identify all subprocessors handling organizational data
5. **Shadow IT Assessment** - Unapproved cloud services with organizational data

**Assessment Output:** Excel workbook with ~100-200 data points documenting cloud provider deletion capabilities, vendor contract compliance, deletion certificates received, and remediation plans for vendors without adequate deletion procedures.

## Why This Matters

**ISO 27001:2022 Control A.8.10 Requirement:**
> *"Information stored in information systems, devices or in any other storage media should be deleted when no longer required."*

**Extension to Third Parties:** When [Organization] stores data with cloud providers or third-party vendors, deletion responsibility doesn't transfer entirely to the vendor. [Organization] remains accountable for ensuring deletion occurs.

**GDPR Article 28 - Processor Obligations:**

Under GDPR, cloud providers and SaaS vendors are typically "processors" of personal data. Article 28 requires:

- **Deletion Assistance:** Processors must assist controller in ensuring deletion of personal data
- **Return or Deletion:** Upon termination, processor must delete or return all personal data
- **Subprocessor Management:** Controllers must be informed of all subprocessors handling data

**Business Impact:**

- **Data Breach Risk:** Vendor retains "deleted" data = expanded attack surface, liability
- **GDPR Fines:** Controller responsible for processor deletion failures (up to €20M or 4% global turnover)
- **Vendor Lock-In:** Inability to delete data from SaaS = difficulty changing vendors
- **Shadow IT Risk:** Unapproved cloud services with organizational data = uncontrolled deletion
- **Compliance Audit Failures:** No deletion certificates from vendors = cannot prove compliance

**Real-World Scenarios:**

- SaaS vendor bankruptcy → Customer data sold to creditors (no deletion)
- Cloud provider "delete" delays months → Data accessible during delay period
- Subprocessor not disclosed → Data processed in unexpected jurisdiction, deletion unverified
- Free cloud service (Google Drive, Dropbox) → No enterprise deletion SLA, data persists indefinitely
- M&A activity → Acquired vendor changes data handling, deletion policies void

## Who Should Complete This Assessment

**Primary Responsibility:** Vendor Management / Procurement / Cloud Administrator

**Required Knowledge:**

- [Organization]'s cloud service inventory (AWS, Azure, GCP, SaaS applications)
- Vendor contract terms and data processing agreements (DPAs)
- GDPR Article 28 processor obligations
- Cloud provider deletion policies and capabilities
- Subprocessor disclosure requirements

**Support Roles:**

- **Legal Counsel:** For contract review and deletion clause sufficiency
- **Data Protection Officer (DPO):** For GDPR Article 28 compliance and subprocessor management
- **Cloud Administrators:** For cloud provider deletion verification and testing
- **IT Operations:** For SaaS application deletion procedures
- **Procurement:** For vendor contract negotiation and SLA management
- **Information Security:** For Shadow IT identification and risk assessment

## Time Estimate

**Total Assessment Time:** 8-12 hours (depending on vendor count and contract complexity)

**Breakdown:**

- **Cloud Provider Inventory (2-3 hours):** Identify all cloud services and providers
- **Vendor Contract Review (3-4 hours):** Review DPAs for deletion clauses and SLAs
- **Deletion Capability Assessment (2-3 hours):** Document provider deletion methods and verification
- **Subprocessor Mapping (1-2 hours):** Identify disclosed subprocessors
- **Shadow IT Assessment (1-2 hours):** Identify unapproved cloud services
- **Evidence Collection (1 hour):** Gather contracts, certificates, audit reports
- **Quality Review (1 hour):** Final validation and approval preparation

**Pro Tip:** If [Organization] has >50 cloud/SaaS vendors, consider prioritizing by data sensitivity (assess Confidential/Restricted data vendors first).

## Connection to Policy

This assessment implements **ISMS-POL-A.8.10, Section 2.3 (Third-Party & Cloud Deletion)** which defines mandatory requirements for:

- **Vendor Selection:** Deletion capabilities assessed during vendor evaluation
- **Contract Requirements:** All data processing agreements must include deletion clauses
- **Deletion SLAs:** Maximum deletion timelines defined (typically 30-90 days)
- **Verification Requirements:** Deletion certificates or audit logs required as proof
- **Subprocessor Disclosure:** All subprocessors identified and assessed for deletion capabilities
- **Shadow IT Prohibition:** Unapproved cloud services with organizational data not permitted

**Policy Authority:** Chief Information Security Officer (CISO) / Data Protection Officer (DPO) / Chief Procurement Officer (CPO)  
**Compliance Status:** Mandatory for all vendors processing Confidential or Restricted data, or personal data subject to GDPR

## Critical: GDPR Article 28 Processor Obligations

**⚠️ IMPORTANT - Controller vs. Processor Responsibilities:**

Under GDPR, [Organization] is typically the "controller" (determines purposes and means of processing). Cloud providers and SaaS vendors are typically "processors" (process data on behalf of controller).

**GDPR Article 28.3 - Processor Obligations Include:**

**(a) Data Processing Instructions:**
> "The processor shall process personal data only on documented instructions from the controller..."

**(e) Deletion Assistance:**
> "Taking into account the nature of the processing, the processor shall assist the controller by appropriate technical and organizational measures, insofar as this is possible, for the fulfillment of the controller's obligation to respond to requests for exercising the data subject's rights..."

**This includes:** Right to erasure (GDPR Article 17)

**(g) Deletion or Return:**
> "...the processor shall, at the choice of the controller, delete or return all the personal data to the controller after the end of the provision of services relating to processing, and delete existing copies unless Union or Member State law requires storage of the personal data."

**(h) Subprocessor Engagement:**
> "The processor shall not engage another processor without prior specific or general written authorization of the controller..."

**Critical Implication:**

- [Organization] cannot outsource GDPR compliance responsibility to vendors
- If vendor fails to delete data, [Organization] is liable under GDPR
- Vendor deletion capabilities MUST be verified, not assumed

---

# Prerequisites

## Access Required

Before starting this assessment, ensure you have access to:

**Documentation:**

- [ ] Cloud service inventory (all IaaS, PaaS, SaaS in use)
- [ ] Vendor contracts and data processing agreements (DPAs)
- [ ] Cloud provider deletion policies (AWS, Azure, GCP whitepapers)
- [ ] SaaS application deletion documentation
- [ ] Subprocessor disclosure notices from vendors
- [ ] ISMS-REF-A.5.23 Cloud Service Provider Registry (if available)
- [ ] Shadow IT detection reports (CASB, network logs, expense reports)

**Systems:**

- [ ] Cloud provider management consoles (AWS, Azure, GCP, etc.)
- [ ] SaaS application admin portals (Salesforce, Workday, HubSpot, etc.)
- [ ] Contract management system (for vendor agreements)
- [ ] Vendor management platform (if available)
- [ ] Cloud Access Security Broker (CASB) - if deployed

**Stakeholders:**

- [ ] Legal Counsel (for contract interpretation)
- [ ] Procurement team (for vendor contract access)
- [ ] Cloud administrators (for deletion testing)
- [ ] Business Unit Owners (for SaaS application inventory)

## Required Knowledge

**Regulatory & Legal:**

- Understanding of GDPR Article 28 (processor obligations)
- Understanding of GDPR Article 17 (right to erasure)
- Understanding of data processing agreement (DPA) structure
- Subprocessor disclosure requirements
- Cross-border data transfer implications on deletion

**Technical:**

- Cloud provider deletion mechanisms (IaaS, PaaS, SaaS)
- SaaS application data export and deletion capabilities
- API-based deletion vs. manual deletion processes
- Deletion verification methods (certificates, audit logs)

**Contractual:**

- Standard deletion clauses in DPAs
- Service Level Agreements (SLAs) for deletion timelines
- Data return vs. deletion options
- Vendor liability for deletion failures

## Pre-Assessment Checklist

Complete these tasks before beginning the assessment:

- [ ] **Create cloud service inventory** (or update existing inventory)
- [ ] **Gather all vendor contracts** with data processing agreements
- [ ] **Review ISMS-REF-A.5.23** Cloud Service Provider Registry (if available - provides deletion tier ratings)
- [ ] **Identify subprocessors** from vendor disclosure notices
- [ ] **Run Shadow IT scan** (CASB, expense reports, network traffic analysis)
- [ ] **Request deletion certificates** from major cloud providers (for past deletions)
- [ ] **Review vendor audit reports** (SOC 2 Type II, ISO 27001) for deletion procedures
- [ ] **Schedule vendor meetings** for providers without clear deletion documentation

**Critical:** If [Organization] lacks a complete cloud service inventory, allow additional time (20-30 hours) to conduct discovery before assessment.

---

# Assessment Workflow

## Workflow Overview

```
Step 1: Cloud Provider Deletion Assessment (Sheet 2)
   ↓
Step 2: SaaS Application Deletion (Sheet 3)
   ↓
Step 3: Vendor Contract Review (Sheet 4)
   ↓
Step 4: Subprocessor Mapping (Sheet 5)
   ↓
Step 5: Shadow IT Assessment (Sheet 6)
   ↓
Step 6: Evidence Collection (Sheet 8)
   ↓
Step 7: Review Summary Dashboard (Sheet 7)
   ↓
Step 8: Quality Check & Approval (Sheet 9)
```

## Step-by-Step Instructions

### Step 1: Cloud Provider Deletion Assessment (Sheet 2)

**Objective:** Document deletion capabilities for major cloud infrastructure providers (IaaS, PaaS)

**Instructions:**
1. List all cloud providers in Column A (e.g., "AWS - Production Environment", "Azure - DR Site")
2. Identify Provider Name and Service Tier in Column R (reference ISMS-REF-A.5.23 if available)
3. Document Deletion Method in Column S (API, lifecycle policy, manual)
4. Assess Deletion Verification Available in Column T
5. Evaluate Status based on contractual and technical deletion capabilities

**Major Cloud Providers to Consider:**

**Infrastructure as a Service (IaaS):**

- AWS (EC2, S3, EBS, RDS)
- Microsoft Azure (VMs, Blob Storage, SQL Database)
- Google Cloud Platform (Compute Engine, Cloud Storage, Cloud SQL)
- Alibaba Cloud
- Oracle Cloud Infrastructure

**Platform as a Service (PaaS):**

- AWS (Lambda, DynamoDB, Aurora)
- Azure (App Service, Cosmos DB, Functions)
- GCP (App Engine, Firestore, Cloud Run)
- Heroku
- DigitalOcean

**Provider-Specific Deletion Capabilities:**

**AWS:**

- **Deletion Method:** API (DeleteObject, TerminateInstances), Lifecycle Policies, Manual
- **Verification:** CloudTrail audit logs, S3 deletion markers, API responses
- **Crypto-Shred:** Customer Master Keys (CMK) deletion → data unrecoverable
- **SLA:** Immediate deletion intent, eventual consistency across regions

**Azure:**

- **Deletion Method:** API (Delete Blob, Delete VM), Lifecycle Management, Manual
- **Soft Delete:** BEWARE - Blob soft delete retains "deleted" data 1-365 days (default 7)
- **Verification:** Azure Monitor / Activity Logs, deletion confirmation
- **Crypto-Shred:** Customer-Managed Keys (CMK) deletion → data unrecoverable

**Google Cloud Platform:**

- **Deletion Method:** API (Delete Object, Delete Instance), Lifecycle Policies, Manual
- **Verification:** Cloud Audit Logs, deletion confirmation
- **Crypto-Shred:** Customer-Managed Encryption Keys (CMEK) destruction → data unrecoverable

**Quality Check:**

- Are soft delete features disabled or accounted for in retention calculations?
- Is crypto-shred capability documented and tested?
- Have deletion certificates been requested from providers?
- Is multi-region data deletion verified (not just single region)?

### Step 2: SaaS Application Deletion (Sheet 3)

**Objective:** Assess deletion capabilities for Software-as-a-Service applications

**Instructions:**
1. List all SaaS applications in Column A (e.g., "Salesforce CRM", "Workday HCM", "HubSpot Marketing")
2. Classify Application Type in Column R (CRM, HR, Marketing, Collaboration, etc.)
3. Document Deletion Procedure in Column S (API, Admin UI, Support Ticket, Unknown)
4. Assess Data Export Capability in Column T (required before deletion for verification)
5. Evaluate Status based on deletion accessibility and verification

**Common SaaS Categories:**

**Customer Relationship Management (CRM):**

- Salesforce, HubSpot, Microsoft Dynamics 365, Zoho CRM
- **Deletion:** Admin UI (bulk delete), API (programmatic), Support ticket (account closure)
- **Risk:** CRM data often has dependencies (contacts, opportunities, cases) - partial deletion risk

**Human Resources (HR):**

- Workday, SAP SuccessFactors, BambooHR, ADP
- **Deletion:** Typically requires support ticket (employee data sensitive)
- **Compliance:** GDPR Article 17 applies to employee data (ex-employees can request erasure)

**Marketing Automation:**

- HubSpot, Marketo, Mailchimp, Pardot
- **Deletion:** Admin UI (unsubscribe + delete), API
- **GDPR:** High risk - marketing lists often shared with third parties (subprocessors)

**Collaboration & Productivity:**

- Microsoft 365, Google Workspace, Slack, Zoom
- **Deletion:** Admin UI (user deletion), API
- **Risk:** Data scattered across multiple services (email, drive, chat, calendar)

**Finance & Accounting:**

- QuickBooks Online, Xero, NetSuite, Concur
- **Deletion:** Often restricted (legal retention requirements for financial records)
- **Compliance:** Financial data retention mandated by law (cannot delete per GDPR if legal obligation exists)

**SaaS Deletion Challenges:**

**Challenge 1: No Self-Service Deletion**

- Many SaaS apps require support ticket to delete data
- **Response Time:** 30-90 days typical (may exceed GDPR 30-day timeline)
- **Verification:** No deletion certificate, must trust vendor's confirmation email

**Challenge 2: Data Export Limitations**

- Some SaaS apps limit data export (preventing verification before deletion)
- **Example:** Zoom meeting recordings may not be fully exportable
- **Mitigation:** Test data export before committing to SaaS vendor

**Challenge 3: Soft Delete / Retention Periods**

- SaaS apps often have soft delete (30-90 day retention after "deletion")
- **Example:** Salesforce recycle bin (15 days), Office 365 deleted items (30 days)
- **Compliance:** Document retention periods in assessment

**Challenge 4: Third-Party Integrations**

- SaaS data synchronized to other services (Zapier, integrations)
- **Risk:** Deleting from primary SaaS doesn't delete from integrated services
- **Mitigation:** Map all integrations, delete from integrated services first

**Quality Check:**

- Have all SaaS applications been identified (check expense reports, SSO logs)?
- Is deletion procedure documented (not assumed)?
- Has data export been tested (required for GDPR data portability + verification)?
- Are soft delete / retention periods documented?
- Have integrations been mapped (data may exist in multiple SaaS)?

### Step 3: Vendor Contract Review (Sheet 4)

**Objective:** Assess vendor contracts for deletion clauses, SLAs, and compliance

**Instructions:**
1. List all vendors with data processing agreements in Column A
2. Document Contract Deletion Clause Strength in Column R
3. Assess Deletion SLA (Days) in Column S
4. Evaluate Certificate of Deletion Provision in Column T
5. Determine Status based on contractual adequacy

**Deletion Clause Assessment Criteria:**

**✅ Strong Deletion Clause:**

- Specifies deletion method (secure deletion, NIST standards)
- Includes deletion timeline SLA (typically 30-90 days)
- Requires deletion certificate or audit log evidence
- Covers all subprocessors
- Includes penalty for non-compliance

**Example Strong Clause:**
> "Upon termination or at Controller's request, Processor shall delete all personal data within 30 days using NIST SP 800-88 Purge or Destroy methods. Processor shall provide Controller with a signed Certificate of Deletion confirming deletion from all systems including backups and subprocessors. Failure to delete within SLA results in liquidated damages of [amount] per day."

**⚠️ Weak Deletion Clause:**

- Vague language ("reasonable efforts to delete")
- No deletion timeline specified
- No verification method (no certificate, no audit logs)
- Excludes backups or subprocessors
- No penalty for non-compliance

**Example Weak Clause:**
> "Processor will make reasonable efforts to delete data upon request, subject to legal and technical limitations. Deletion may take up to 180 days. Processor retains data in backups per retention policy."

**❌ Missing Deletion Clause:**

- Contract has no deletion language
- Standard terms & conditions only (no DPA)
- Free tier / consumer-grade service (no enterprise SLA)

**Deletion SLA Benchmarks:**

| Vendor Type | Typical Deletion SLA | Acceptable Range | GDPR Consideration |
|------------|---------------------|------------------|-------------------|
| **Enterprise Cloud (AWS, Azure, GCP)** | Immediate (API) | Immediate - 7 days | Acceptable |
| **Enterprise SaaS (Salesforce, Workday)** | 30 days | 30-60 days | Acceptable (aligns with GDPR) |
| **Mid-Market SaaS** | 60 days | 30-90 days | Borderline (document justification) |
| **Small Vendor / Niche SaaS** | 90 days or unknown | 60-120 days | Risky (may not meet GDPR if data subject requests erasure) |

**Certificate of Deletion:**

**Best Practice:** Vendor provides signed certificate confirming:

- Data deleted from production systems
- Data deleted from backups
- Data deleted from all subprocessors
- Deletion method used (NIST category)
- Deletion date and responsible person signature

**Alternative Verification:** If no certificate, vendor provides:

- Audit log exports showing deletion events
- SOC 2 Type II report describing deletion procedures
- ISO 27001 certification with deletion controls

**Quality Check:**

- All vendor contracts reviewed (not just major vendors - small vendors are high risk)?
- Deletion clauses assessed for strength (not just presence)?
- SLAs documented and reasonable for GDPR compliance?
- Certificate of deletion available or alternative verification method defined?
- Penalty clauses for non-compliance included in contracts?

### Step 4: Subprocessor Mapping (Sheet 5)

**Objective:** Identify all subprocessors handling organizational data

**Instructions:**
1. For each primary vendor, list disclosed subprocessors in Column A
2. Document Subprocessor Function in Column R (hosting, analytics, support, etc.)
3. Assess Subprocessor Deletion Capability in Column S
4. Evaluate Primary Vendor Control Over Subprocessor in Column T
5. Determine Status based on subprocessor deletion risk

**GDPR Article 28 Subprocessor Requirements:**

**What is a Subprocessor?**
A subprocessor is a third party engaged by the processor (your vendor) to process personal data on behalf of the controller (your organization).

**Examples:**

- **Primary Vendor:** Salesforce (CRM)
- **Subprocessors:** AWS (hosting), Heroku (platform), Tableau (analytics)

**GDPR Requirements:**
1. **Disclosure:** Processor must inform controller of all subprocessors (GDPR Article 28.2)
2. **Authorization:** Controller must authorize subprocessor engagement (general or specific)
3. **Obligations Flow Down:** Subprocessors must have same data protection obligations as primary processor
4. **Liability:** Primary processor remains liable for subprocessor failures

**Subprocessor Deletion Challenges:**

**Challenge 1: Undisclosed Subprocessors**

- Vendor uses subprocessors not disclosed in DPA
- **Risk:** Data in unknown locations, deletion unverified
- **Example:** SaaS vendor uses CDN for performance, CDN not disclosed

**Challenge 2: Multi-Tier Subprocessing**

- Subprocessor engages sub-subprocessor
- **Risk:** Data distributed across multiple tiers, deletion complexity
- **Example:** AWS (subprocessor) uses third-party data centers (sub-subprocessor)

**Challenge 3: No Direct Deletion Control**

- Primary vendor relies on subprocessor for deletion
- **Risk:** Deletion delay, no verification from subprocessor
- **Example:** SaaS vendor deletes from database, but AWS S3 lifecycle deletion delayed

**Challenge 4: Shared Infrastructure**

- Subprocessor hosts multiple tenants on shared infrastructure
- **Risk:** Data co-location, deletion verification difficult
- **Example:** Multi-tenant SaaS database - deletion must not affect other tenants

**Subprocessor Assessment Questions:**

For each subprocessor, ask:
1. **Disclosure:** Is subprocessor disclosed in vendor DPA?
2. **Function:** What data processing function does subprocessor perform?
3. **Location:** Where is subprocessor located (jurisdiction matters for GDPR)?
4. **Deletion:** Does primary vendor control subprocessor deletion, or is it independent?
5. **Verification:** Can primary vendor provide deletion evidence from subprocessor?

**Quality Check:**

- All subprocessors disclosed by vendors have been identified?
- Subprocessor functions documented (not just names)?
- Subprocessor deletion capabilities assessed (not assumed to match primary vendor)?
- Primary vendor liability for subprocessor deletion confirmed in contract?
- Multi-tier subprocessing identified and assessed?

### Step 5: Shadow IT Assessment (Sheet 6)

**Objective:** Identify unapproved cloud services containing organizational data

**Instructions:**
1. List all identified Shadow IT services in Column A
2. Document Discovery Method in Column R (CASB, expense reports, network logs)
3. Assess Data Sensitivity in Column S
4. Evaluate Deletion Risk in Column T
5. Determine remediation priority (migrate to approved service or delete data)

**What is Shadow IT?**

Shadow IT refers to cloud services and applications used by employees without IT department approval or knowledge. This creates uncontrolled data storage and deletion risk.

**Examples:**

- Employee uses personal Dropbox to share customer files
- Marketing team subscribes to unapproved analytics platform
- Developer uses free cloud database for testing (forgets to delete test data)
- Department purchases SaaS without IT review (no DPA, no deletion clause)

**Shadow IT Discovery Methods:**

**Method 1: Cloud Access Security Broker (CASB)**

- CASB monitors network traffic, identifies cloud service usage
- **Example Tools:** Netskope, McAfee MVISION Cloud, Palo Alto Prisma Access
- **Coverage:** High (detects most cloud services)

**Method 2: Expense Report Analysis**

- Review expense reports for SaaS subscriptions
- **Coverage:** Medium (misses free tier services, personal credit cards)

**Method 3: Network Traffic Analysis**

- Firewall logs, DNS queries to cloud service domains
- **Coverage:** Medium (encrypted traffic limits visibility)

**Method 4: SSO / Identity Provider Logs**

- Review SSO logs (Okta, Entra ID) for unapproved applications
- **Coverage:** Low (only detects services using SSO)

**Method 5: User Surveys / Interviews**

- Ask employees what cloud services they use
- **Coverage:** Low (relies on self-reporting)

**Shadow IT Deletion Risks:**

**Risk 1: No Deletion Control**

- Free tier / consumer services have no enterprise deletion SLA
- **Example:** Google Drive free account - no deletion certificate available

**Risk 2: Personal Accounts**

- Employee uses personal email for work
- **Risk:** Employee leaves, data remains in personal account indefinitely

**Risk 3: No Data Processing Agreement**

- Unapproved service = no DPA = no deletion obligations
- **GDPR Risk:** No contractual basis for vendor to delete data

**Risk 4: Data Co-Mingling**

- Work and personal data mixed in unapproved service
- **Risk:** Cannot delete work data without affecting personal data

**Shadow IT Remediation Options:**

**Option 1: Migrate to Approved Service**

- Export data from Shadow IT service
- Import to approved, DPA-compliant service
- Delete from Shadow IT service (verify if possible)

**Option 2: Formalize Usage**

- Upgrade to enterprise tier with DPA
- Add vendor to approved vendor list
- Document deletion capabilities

**Option 3: Prohibit and Delete**

- Policy: Immediate data deletion from unapproved service
- User training on approved alternatives
- Monitor for recurrence

**Quality Check:**

- Shadow IT discovery methods deployed (not relying on one method)?
- All discovered Shadow IT services documented (even low-risk ones)?
- Data sensitivity assessed for each Shadow IT service?
- Remediation plan defined (migrate, formalize, or delete)?
- User training planned to prevent future Shadow IT?

### Step 6: Evidence Collection (Sheet 8)

**Objective:** Link supporting documentation to third-party deletion assessments

**Instructions:**
1. For each cloud provider or vendor, create evidence entry
2. Evidence Register auto-generates Evidence ID (EV-001, EV-002, etc.)
3. Document Evidence Type, Location, Retention Period
4. Reference Evidence ID in Column N of assessment sheets

**Evidence Types:**

**Vendor Contracts:**

- Data Processing Agreements (DPAs) with deletion clauses
- Service Level Agreements (SLAs) for deletion timelines
- Master Service Agreements (MSAs)
- Subprocessor disclosure notices

**Deletion Certificates:**

- Vendor-signed certificates of deletion
- Cloud provider deletion confirmation emails
- Audit log exports showing deletion events

**Audit Reports:**

- SOC 2 Type II reports (deletion controls tested)
- ISO 27001 certificates (deletion procedures)
- Cloud provider compliance reports

**Technical Documentation:**

- Cloud provider deletion policy whitepapers (AWS, Azure, GCP)
- SaaS application deletion procedures (from vendor documentation)
- API documentation for programmatic deletion

**Verification Evidence:**

- Screenshots of deletion configurations (lifecycle policies)
- Crypto-shred key destruction logs
- CASB reports (Shadow IT discovery)

**Quality Check:**

- Every cloud provider / vendor has supporting evidence?
- Deletion certificates collected where available?
- Contracts reviewed and deletion clauses extracted?
- Subprocessor disclosures on file?
- Shadow IT discovery reports documented?

### Step 7: Review Summary Dashboard (Sheet 7)

**Objective:** Validate overall third-party deletion compliance and identify critical gaps

**The Summary Dashboard auto-calculates:**

- Overall third-party deletion compliance percentage
- Count of vendors with strong deletion clauses
- Count of vendors without deletion SLAs
- Subprocessor disclosure coverage
- Shadow IT count and data sensitivity
- Critical gaps requiring immediate remediation

**Review Questions:**

- Does overall compliance % reflect your understanding of vendor deletion capabilities?
- Are any vendors with Confidential/Restricted data missing deletion clauses? (High risk)
- Have all subprocessors been identified and assessed?
- Is Shadow IT count acceptable, or does it indicate policy enforcement gap?

### Step 8: Quality Check & Approval (Sheet 9)

**Objective:** Final validation and three-level approval workflow

**Self-Check Before Submitting for Approval:**

- [ ] All cloud providers and SaaS vendors documented (no major services omitted)
- [ ] Vendor contracts reviewed for deletion clauses and SLAs
- [ ] Deletion certificates requested from major providers
- [ ] Subprocessors identified and assessed
- [ ] Shadow IT discovery conducted and documented
- [ ] Evidence register populated with contracts and certificates
- [ ] Status indicators accurate (not aspirational)
- [ ] Gaps and remediation plans realistic and resourced

**Approval Workflow:**
1. **Level 1: Technical/Operational** - Cloud Administrator / Vendor Manager validates vendor inventory and deletion capabilities
2. **Level 2: Management** - CISO/DPO approves remediation plans and contract renegotiation priorities
3. **Level 3: Executive** - CRO/CEO acknowledges third-party deletion risk posture

---

# Question-by-Question Guidance

## Cloud Provider Deletion (Sheet 2)

**Q: How do I verify cloud provider deletion if I can't access their data centers?**
A: Multiple verification methods:
1. **Audit Logs:** AWS CloudTrail, Azure Monitor, GCP Cloud Audit Logs show deletion events
2. **Deletion Certificates:** Request from cloud provider (enterprise support)
3. **Crypto-Shred:** Use customer-managed keys (CMK), delete key, data cryptographically unrecoverable
4. **Compliance Reports:** SOC 2 Type II, ISO 27001 reports describe deletion procedures
5. **Contractual Confirmation:** Cloud provider confirms deletion in writing

**Best Practice:** Combine methods (audit logs + crypto-shred + compliance reports).

**Q: What's the difference between AWS "delete" and "crypto-shred"?**
A:

- **Standard Delete:** Removes object, but data may persist in backend systems until overwritten
- **Crypto-Shred:** Destroys encryption key (CMK), rendering encrypted data mathematically unrecoverable
- **Speed:** Crypto-shred instant (key deletion), standard delete gradual (eventual consistency)
- **Verification:** Crypto-shred easily verified (key status = PendingDeletion), standard delete requires audit logs

**Recommendation:** Use crypto-shred for Confidential/Restricted data in cloud storage.

**Q: What is "eventual consistency" in cloud deletion?**
A: Cloud storage replicates data across multiple regions/data centers. When you delete:
1. Deletion request accepted by one region
2. Deletion propagates to other regions over seconds/minutes
3. During propagation, data may still be accessible from some regions

**For GDPR compliance:** Document that deletion propagation typically completes within minutes, but may take up to 24 hours for globally distributed data.

**Q: Should I disable Azure Blob "soft delete" feature?**
A: Depends on use case:

- **Soft Delete Enabled (7-30 days):** Provides recovery window, but "deleted" data persists
- **GDPR Consideration:** If data subject requests erasure, soft delete retention adds to response time
- **Recommendation:** Disable soft delete for compliance-critical storage accounts, or document retention period in GDPR response timelines

## SaaS Application Deletion (Sheet 3)

**Q: Can I delete data from Salesforce myself, or do I need to contact support?**
A: Salesforce offers both:

- **Admin UI:** Bulk delete records, contacts, opportunities (limited to 200 at a time)
- **API:** Programmatic deletion (no limits, recommended for large-scale deletion)
- **Data Loader:** Desktop tool for bulk deletion (up to 5M records)
- **Support Ticket:** For account closure or deletion of system-level data

**For GDPR erasure requests:** API or Data Loader preferred (faster, verifiable via audit logs).

**Q: What if SaaS vendor says they "can't" delete data?**
A: Red flag - investigate further:

- **Legal Retention:** If vendor has legal obligation to retain (financial records, tax data), deletion may be legitimately restricted
- **Technical Limitation:** Vendor may lack deletion capability (legacy system) - this is a compliance risk
- **Policy Limitation:** Vendor policy may prohibit deletion during contract term - negotiate exception for GDPR

**Action:** If vendor cannot delete, consider:
1. Contract renegotiation (add deletion clause)
2. Vendor replacement (find vendor with deletion capability)
3. Risk acceptance (document gap, implement compensating controls like encryption)

**Q: How do I handle SaaS data in integrations (Zapier, APIs)?**
A: Multi-step deletion process:
1. **Identify all integrations:** Map where SaaS data is synchronized
2. **Delete from downstream systems first:** Delete from integrated services (e.g., data warehouse, analytics platform)
3. **Disable integrations:** Prevent re-synchronization
4. **Delete from primary SaaS:** Remove data from source system
5. **Verify:** Check all integrated systems confirm deletion

**Common Integration Deletion Gaps:**

- ❌ Delete from SaaS, but integrated data warehouse still has copy
- ❌ Delete records, but attachments/files remain in document storage
- ❌ Delete customer, but marketing platform still has email address

## Vendor Contract Assessment (Sheet 4)

**Q: What if vendor refuses to add deletion clause to contract?**
A: Assess vendor criticality and data sensitivity:

- **High-Risk Scenario:** Vendor processes Confidential/Restricted data, refuses deletion clause
  - **Action:** Replace vendor (find alternative with proper DPA)
  - **Justification:** GDPR Article 28 requires processor deletion assistance
- **Medium-Risk Scenario:** Vendor processes Internal data, weak deletion clause
  - **Action:** Document risk, implement compensating controls (client-side encryption)
- **Low-Risk Scenario:** Vendor processes Public data, no deletion clause
  - **Action:** Acceptable (Public data = no GDPR deletion requirement)

**Q: What's a reasonable deletion SLA?**
A: Depends on use case:

- **GDPR Data Subject Request:** 30 days maximum (GDPR Article 12.3)
- **Contract Termination:** 30-90 days acceptable
- **Routine Deletion (Retention Expiration):** 90 days acceptable
- **Cloud Infrastructure (API):** Immediate (within minutes/hours)

**Negotiation Tip:** If vendor proposes >90 day SLA, negotiate down or require interim deletion confirmation (e.g., production deletion in 30 days, backup deletion in 90 days).

**Q: Should deletion certificate be signed or is email confirmation sufficient?**
A: For audit purposes:

- **Ideal:** Signed certificate on vendor letterhead (legally binding)
- **Acceptable:** Email confirmation from authorized vendor representative (saved to evidence register)
- **Insufficient:** Automated system confirmation with no human verification

**Audit Readiness:** Auditors prefer signed certificates, but email from authorized person (CFO, CTO, Legal) is typically acceptable.

## Subprocessor Mapping (Sheet 5)

**Q: How do I find out who my vendor's subprocessors are?**
A: Multiple sources:
1. **Data Processing Agreement (DPA):** Should include subprocessor list or reference to published list
2. **Vendor Website:** Many vendors publish subprocessor lists (e.g., Salesforce Trust, AWS Compliance)
3. **Ask Vendor:** Request current subprocessor list (GDPR Article 28.2 requires disclosure)
4. **SOC 2 Report:** Type II reports often list subprocessors

**If vendor refuses to disclose:** GDPR violation - reconsider vendor relationship.

**Q: What if subprocessor list changes frequently?**
A: GDPR allows "general authorization" with notification:

- **General Authorization:** Controller authorizes vendor to use subprocessors, subject to notification
- **Notification:** Vendor must inform controller before engaging new subprocessor
- **Objection Period:** Controller has reasonable time to object (typically 30 days)

**Action:** Review vendor notification emails for subprocessor changes, assess deletion impact.

**Q: Am I responsible for subprocessor deletion, or is the primary vendor?**
A: Primary vendor is responsible (GDPR Article 28.4):
> "Where a processor engages another processor for carrying out specific processing activities on behalf of the controller, the same data protection obligations as set out in the contract or other legal act between the controller and the processor... shall be imposed on that other processor..."

**However:** Controller (you) should verify that:

- Primary vendor has contractual deletion obligations with subprocessors
- Primary vendor can demonstrate subprocessor deletion compliance

**Best Practice:** In DPA with primary vendor, require clause: "Vendor is responsible for ensuring all subprocessors delete data per same SLA and verification requirements."

## Shadow IT Assessment (Sheet 6)

**Q: How do I prevent Shadow IT without blocking employee productivity?**
A: Balance security and usability:
1. **Approved Alternatives:** Provide approved cloud services that meet employee needs

   - Example: Approved file sharing (OneDrive, Box) so employees don't use Dropbox

2. **Easy Approval Process:** Make it easy for employees to request new cloud services

   - Fast-track approval for low-risk services

3. **User Training:** Explain risks of Shadow IT (data loss, compliance violations)
4. **CASB Monitoring:** Deploy CASB to detect Shadow IT without blocking (visibility first)
5. **Graduated Response:** Warn first, block if persistent violations

**Q: What if I discover Shadow IT with sensitive data already in it?**
A: Immediate action required:
1. **Assess Risk:** What data is in Shadow IT service? How sensitive?
2. **Contain:** Prevent additional data upload if possible (CASB block rule)
3. **Migrate or Delete:** 

   - If service useful: Upgrade to enterprise tier, add DPA, migrate to approved account
   - If service unnecessary: Export data, delete from Shadow IT service, delete Shadow IT account

4. **Document:** Record in assessment, track remediation completion
5. **User Training:** Retrain user on approved services and Shadow IT policy

**Q: Do I need to assess free tier / trial accounts?**
A: Yes - free tier accounts are high risk:

- **No DPA:** Consumer terms of service, no GDPR processor obligations
- **No Deletion SLA:** Vendor may retain data indefinitely
- **No Support:** Cannot request deletion certificate or escalate issues

**Action:** Identify all free tier usage, upgrade to enterprise tier or migrate to approved service.

---

# Evidence Collection

## What Evidence to Collect

For each assessment area, gather supporting documentation:

**Cloud Provider Deletion:**

- Cloud provider deletion policy documents (AWS, Azure, GCP whitepapers)
- Data Processing Agreements (DPAs) with deletion clauses
- Deletion certificates or confirmation emails
- Audit log exports (CloudTrail, Azure Monitor, Cloud Audit Logs)
- Crypto-shred key destruction logs
- SOC 2 Type II / ISO 27001 reports

**SaaS Application Deletion:**

- SaaS vendor DPAs with deletion clauses
- Deletion procedure documentation (from vendor support docs)
- Deletion confirmation emails (from past deletions)
- Data export capabilities test results
- Integration mapping (where SaaS data is synchronized)

**Vendor Contract Assessment:**

- All vendor contracts with data processing agreements
- Deletion clause excerpts (extracted and documented)
- SLA documentation (deletion timelines)
- Penalty clauses for non-compliance
- Amendment history (if deletion clauses added post-contract)

**Subprocessor Mapping:**

- Subprocessor disclosure notices from vendors
- Subprocessor list updates (email notifications)
- Subprocessor DPAs (if available)
- Vendor compliance reports documenting subprocessor management

**Shadow IT Assessment:**

- CASB reports (cloud service discovery)
- Expense report analysis results
- Network traffic analysis (cloud service domains)
- User survey results (self-reported cloud usage)
- Remediation tracking (migration or deletion completion)

## Evidence Storage & Retention

**Where to Store Evidence:**

- Centralized evidence repository (ISMS document management)
- Contract management system (for vendor agreements)
- Compliance management platform

**Evidence Retention Period:**

- Vendor contracts: Duration of contract + 7 years (for legal disputes)
- Deletion certificates: 7 years (to demonstrate historical compliance)
- Audit reports: 4 years (ISO 27001 certification cycle)

**Evidence Protection:**

- Access controls: Limited to ISMS team, Legal, Procurement, auditors
- Encryption: Contracts may contain sensitive commercial terms
- Integrity: Hash/checksum for contracts to detect tampering

## Audit-Readiness Tips

**What Auditors Will Look For:**
1. **Vendor Inventory Completeness:** All cloud/SaaS vendors identified?
2. **Contract Coverage:** Do all vendors have DPAs with deletion clauses?
3. **GDPR Article 28 Compliance:** Subprocessors disclosed, deletion obligations flow down?
4. **Verification Evidence:** Deletion certificates or audit logs available?
5. **Shadow IT Controls:** Shadow IT discovery process in place?
6. **High-Risk Vendors:** Confidential/Restricted data vendors have strong deletion clauses?

**Common Audit Findings (And How to Avoid Them):**

- ❌ **"Vendor contracts missing deletion clauses"** → Renegotiate contracts, prioritize high-risk vendors
- ❌ **"Subprocessors not disclosed"** → Request subprocessor lists from all vendors, document in assessment
- ❌ **"No deletion verification from vendors"** → Request deletion certificates or implement audit log verification
- ❌ **"Shadow IT with sensitive data"** → Deploy CASB, remediate discovered Shadow IT, user training
- ❌ **"Free tier / consumer services in use"** → Upgrade to enterprise tier or migrate to approved service
- ❌ **"No deletion SLAs"** → Negotiate SLAs in contract renewals, document acceptable timelines

---

# Common Pitfalls

## Assuming Cloud Provider Deletion = Immediate

**Pitfall:** Believing cloud "delete" instantly removes data from all systems

**Reality:**

- **Multi-Region Replication:** Data replicated across regions, deletion propagates gradually
- **Soft Delete:** Azure Blob soft delete, AWS S3 versioning - "deleted" data retained
- **Backup Systems:** Cloud provider backups may retain deleted data for days/weeks
- **Eventual Consistency:** Data accessible from some regions during deletion propagation

**Scenario:**

- Customer requests GDPR erasure
- Organization deletes from AWS S3 immediately
- Data still accessible from EU region for 30 minutes (multi-region replication lag)
- **Result:** Technical GDPR violation (data not immediately erased)

**Prevention:**

- Document deletion propagation timelines in GDPR response procedures
- Disable soft delete for compliance-critical accounts
- Use crypto-shred (key destruction) for immediate cryptographic erasure
- Verify deletion across all regions, not just primary region

## Not Reviewing Vendor Subprocessor Changes

**Pitfall:** Vendor engages new subprocessor, organization unaware

**Scenario:**

- SaaS vendor sends email: "We're adding Acme Analytics as subprocessor"
- Email goes to procurement inbox, ignored
- Acme Analytics processes customer data without organization's knowledge
- Acme Analytics has no deletion clause, data retained indefinitely
- **Result:** GDPR Article 28 violation (subprocessor not authorized, deletion unverified)

**Prevention:**

- Centralize subprocessor notification emails (route to DPO/vendor management)
- Review subprocessor changes quarterly
- Maintain subprocessor register (updated when notification received)
- Exercise objection right if subprocessor lacks adequate deletion procedures

## Shadow IT Data Leakage

**Pitfall:** Employees use unapproved cloud services, data persists after employee departure

**Scenario:**

- Employee uses personal Google Drive to collaborate on customer presentation
- Employee leaves company, personal Google Drive account remains active
- Customer data persists in ex-employee's personal account indefinitely
- **Result:** Data breach, GDPR violation, no deletion control

**Prevention:**

- CASB deployment (detect Shadow IT in real-time)
- Offboarding procedure: Require employees to confirm no work data in personal accounts
- User training: Explain Shadow IT risks and approved alternatives
- Technical controls: Block high-risk cloud services at firewall/proxy

## Free Tier / Trial SaaS Without DPA

**Pitfall:** Using free tier SaaS for production data without data processing agreement

**Scenario:**

- Marketing team uses HubSpot free tier for lead tracking
- No DPA (consumer terms of service apply)
- Company needs to delete leads per GDPR request
- HubSpot free tier: No deletion SLA, no support, no deletion certificate
- **Result:** Cannot prove deletion, GDPR compliance gap

**Prevention:**

- Prohibit free tier usage for business data (policy)
- Require enterprise tier with DPA for all SaaS
- CASB detection of free tier usage (alert IT/procurement)
- Quarterly review of SaaS subscriptions (expense reports)

## Vendor Lock-In Due to Deletion Restrictions

**Pitfall:** Vendor contract prohibits deletion during contract term, preventing vendor change

**Scenario:**

- Organization contracts with niche SaaS vendor
- Contract clause: "Data deletion only permitted after contract termination"
- SaaS vendor performance degrades, organization wants to switch vendors
- Cannot delete data to move to competitor (contract restriction)
- **Result:** Vendor lock-in, stuck with poor service

**Prevention:**

- Negotiate deletion rights during contract term (for GDPR compliance)
- Include data portability clause (export data in standard format)
- Avoid long-term contracts without exit clauses
- Review contract terms before signing (Legal + IT review)

## Subprocessor Deletion Gaps

**Pitfall:** Primary vendor deletes data, but subprocessor retains copy

**Scenario:**

- SaaS vendor uses AWS as subprocessor (hosting)
- Organization requests deletion, SaaS vendor deletes from application database
- SaaS vendor does NOT delete AWS S3 backups (outside application)
- Data persists in AWS S3 indefinitely
- **Result:** Incomplete deletion, GDPR violation

**Prevention:**

- In DPA, require clause: "Vendor responsible for deletion from ALL subprocessors"
- Request deletion certificate covering primary vendor + all subprocessors
- For critical data, require vendor to provide subprocessor deletion evidence
- Audit vendor deletion procedures (SOC 2 Type II should test subprocessor deletion)

---

# Quality Checklist

Before submitting assessment for approval, verify:

## Completeness

- [ ] All cloud providers documented (IaaS, PaaS)
- [ ] All SaaS applications documented (check SSO logs, expense reports)
- [ ] All vendor contracts reviewed (not just major vendors)
- [ ] Subprocessors identified for each vendor
- [ ] Shadow IT discovery conducted (CASB, expense reports, network logs)
- [ ] Evidence register populated with contracts and certificates

## Contractual Compliance

- [ ] All vendor DPAs include deletion clauses
- [ ] Deletion SLAs documented and reasonable (≤90 days typical)
- [ ] Certificate of deletion provision in contracts (or alternative verification)
- [ ] Subprocessor disclosure requirements met
- [ ] Penalty clauses for deletion non-compliance included

## Technical Verification

- [ ] Cloud provider deletion methods documented (API, lifecycle, crypto-shred)
- [ ] SaaS deletion procedures tested or documented
- [ ] Deletion verification methods identified (audit logs, certificates, crypto-shred)
- [ ] Multi-region deletion verified (not just single region)
- [ ] Soft delete features disabled or documented

## GDPR Compliance

- [ ] GDPR Article 28 processor obligations met (deletion assistance)
- [ ] Subprocessors authorized and disclosed
- [ ] Deletion timelines compatible with GDPR Article 17 (30-60 days)
- [ ] Data return vs. deletion options documented

## Risk Management

- [ ] High-risk vendors identified (Confidential/Restricted data, weak deletion clause)
- [ ] Shadow IT remediated or documented with mitigation plan
- [ ] Free tier / consumer services upgraded or replaced
- [ ] Vendor lock-in risks assessed (deletion restrictions in contracts)

## Audit Readiness

- [ ] Traceability: Control → Policy → Assessment → Evidence
- [ ] Evidence locations accessible to auditors
- [ ] Deletion certificates on file (or alternative verification documented)
- [ ] No obvious compliance gaps that would result in audit finding

---

# Review & Approval

## Self-Review

Before submitting for formal approval, conduct self-review:

1. **Vendor Inventory Validation:** Cross-check against expense reports, SSO logs, CASB reports
2. **Contract Review Completeness:** All vendors have DPA review documented
3. **Subprocessor Verification:** Subprocessor lists current (check for recent notifications)
4. **Shadow IT Remediation:** All discovered Shadow IT has remediation plan
5. **Evidence Check:** Can you locate all referenced contracts and certificates?
6. **Stakeholder Validation:** Share draft with Legal, Procurement, Cloud Administrators

## Approval Workflow (Sheet 9)

**Level 1: Technical/Operational Approval**

- **Approver:** Cloud Administrator / Vendor Management / IT Operations Manager
- **Validates:** Vendor inventory completeness, deletion capability accuracy
- **Approval Criteria:** Assessment accurately reflects current cloud/vendor deletion posture

**Level 2: Management Approval**

- **Approver:** Chief Information Security Officer / Data Protection Officer / Chief Procurement Officer
- **Validates:** Contract adequacy, GDPR Article 28 compliance, remediation plans
- **Approval Criteria:** Vendor contracts meet deletion requirements, remediation adequately resourced

**Level 3: Executive Approval**

- **Approver:** Chief Executive Officer / Chief Risk Officer / General Counsel
- **Validates:** Overall third-party deletion risk, vendor lock-in risks
- **Approval Criteria:** Executive leadership acknowledges vendor deletion compliance status and commits to contract renegotiation where needed

## Post-Approval Actions

Once all three levels approve:

1. **Contract Renegotiation:** Initiate contract amendments for vendors with weak/missing deletion clauses
2. **Vendor Meetings:** Schedule meetings with high-risk vendors to discuss deletion capabilities
3. **Shadow IT Remediation:** Execute remediation plans (migrate, formalize, or delete)
4. **Request Deletion Certificates:** For vendors without certificates, initiate request process
5. **CASB Deployment:** If not deployed, initiate CASB project for ongoing Shadow IT monitoring
6. **Update ISMS Documentation:** If vendor list changed, update ISMS-POL-A.8.10, Section 2.3 (Third-Party & Cloud Deletion) and related documents
7. **Plan Next Assessment:** Schedule annual re-assessment or upon major vendor changes

---

**END OF PART I: USER COMPLETION GUIDE**

---

**Continue to PART II: TECHNICAL SPECIFICATION (Deliverable 2) for detailed Excel workbook structure, column definitions, validation rules, and Python script integration points.**

# ISMS-IMP-A.8.10.3 - Third-Party & Cloud Deletion Assessment
# DELIVERABLE 2: PART II - TECHNICAL SPECIFICATION

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Python Developers, Excel Workbook Designers, ISMS Implementation Technical Teams

---

# Workbook Structure Overview

## Sheet Organization (9 Sheets Total)

| Sheet # | Sheet Name | Purpose | Rows | User Entry |
|---------|------------|---------|------|------------|
| 1 | Instructions & Legend | Assessment guidance, GDPR Article 28 overview, color coding | ~65 | Read-only |
| 2 | Cloud Provider Deletion | IaaS/PaaS provider deletion capabilities and verification | ~25-50 | 13 data rows |
| 3 | SaaS Application Deletion | Software-as-a-Service deletion procedures | ~25-50 | 13 data rows |
| 4 | Vendor Contract Assessment | DPA deletion clauses and SLA compliance | ~25-50 | 13 data rows |
| 5 | Subprocessor Mapping | Third-party subprocessor identification and deletion | ~25-50 | 13 data rows |
| 6 | Shadow IT Assessment | Unapproved cloud services discovery and remediation | ~25-50 | 13 data rows |
| 7 | Summary Dashboard | Compliance overview, vendor risk analysis, gaps | ~75 | Formula-driven |
| 8 | Evidence Register | Links to supporting documentation | ~110 | 100 data rows |
| 9 | Approval Sign-Off | Three-level approval workflow | ~75 | Text entry |

**Total Data Entry Points:** ~100-200 (depending on vendor count)

## Workbook Flow

```
Sheet 1 (Instructions) → Orientation
↓
Sheets 2-6 (Assessment Areas) → Vendor Deletion Capability Documentation
↓
Sheet 8 (Evidence Register) → Contract and Certificate Evidence
↓
Sheet 7 (Summary Dashboard) → Vendor Risk Validation
↓
Sheet 9 (Approval Sign-Off) → Authorization
```

## Integration with ISMS-REF-A.5.23 Cloud Service Provider Registry

**CRITICAL:** This assessment integrates with **ISMS-REF-A.5.23 - Cloud Service Provider Registry** which provides:

- Cloud provider tier ratings (Tier 1: Enterprise, Tier 2: Mid-Market, Tier 3: Small/Niche)
- Deletion capability ratings by provider
- Standard DPA templates by provider
- Recommended deletion verification methods

**If ISMS-REF-A.5.23 available:** Reference provider tiers in Column R (Sheet 2)
**If ISMS-REF-A.5.23 not available:** Manually assess provider deletion capabilities

---

# Sheet 1: Instructions & Legend

## Purpose
Provide clear guidance on workbook usage, GDPR Article 28 processor obligations, and third-party deletion requirements.

## Content Sections

**Section 1: Assessment Overview (Rows 3-12)**

- Document ID, version, related policy
- Purpose and scope
- Target audience
- Review cycle and date

**Section 2: GDPR Article 28 - Processor Obligations (Rows 14-40)**

**Key Requirements for Data Processors:**

| Obligation | GDPR Article | Relevance to Deletion |
|-----------|--------------|---------------------|
| **Deletion Assistance** | Article 28.3(e) | Processor must assist controller in deleting data upon request |
| **Deletion or Return** | Article 28.3(g) | Upon termination, processor deletes or returns all data |
| **Subprocessor Management** | Article 28.2, 28.4 | Controller must authorize subprocessors, deletion obligations flow down |
| **Processor Liability** | Article 28.3 | Processor liable for subprocessor deletion failures |

**Section 3: Vendor Deletion Capability Assessment Framework (Rows 42-58)**

**Deletion Capability Levels:**

| Level | Criteria | Examples | Risk |
|-------|----------|----------|------|
| **High** | - API-based deletion<br>- Deletion certificates available<br>- SOC 2 Type II certified<br>- SLA ≤30 days | AWS, Azure, GCP, Salesforce Enterprise | Low |
| **Medium** | - Admin UI deletion<br>- Email confirmation<br>- SLA 30-90 days<br>- DPA includes deletion clause | Mid-market SaaS, regional cloud providers | Medium |
| **Low** | - Support ticket required<br>- No deletion SLA<br>- Weak or missing deletion clause<br>- No verification method | Small SaaS vendors, free tier services | High |
| **Unknown** | - Deletion capability not assessed<br>- No DPA | Shadow IT, unapproved services | Critical |

**Section 4: How to Use This Workbook (Rows 60-72)**

- Step-by-step workflow
- Color coding explanation
- Validation rules
- Evidence linking
- ISMS-REF-A.5.23 integration (if available)

**Section 5: Color Legend (Rows 74-85)**

| Color | Purpose | When to Use |
|-------|---------|-------------|
| Blue Header | Column headers | All assessment sheets |
| Yellow Fill | Data entry cells | User input required |
| Gray Fill | Auto-calculated | Formula cells, no user entry |
| Green | ✅ Compliant / High Deletion Capability | Status indicator |
| Yellow | ⚠️ Partial / Medium Deletion Capability | Status indicator |
| Red | ❌ Non-Compliant / Low/Unknown Deletion Capability | Status indicator |
| White | N/A | Not applicable |

---

# Sheet 2: Cloud Provider Deletion

## Purpose
Document deletion capabilities for cloud infrastructure providers (IaaS, PaaS).

## Sheet Layout

**Header Section (Rows 1-9):**

- Row 1: Sheet title "2. Cloud Provider Deletion Capabilities"
- Row 2: Assessment objective
- Row 3: Instructions for completion
- Rows 4-6: Cloud deletion verification methods
- Row 7: Blank separator
- Row 8: Reminder: "Verify multi-region deletion propagation"
- Row 9: Column headers (frozen)

**Data Entry Section (Rows 10-22):**

- 13 rows for cloud providers (yellow fill)
- Pre-populated example in Row 10 (editable)
- Rows 11-22 blank for user entry

**Reference Section (Rows 24-75):**

- Cloud provider deletion policies (AWS, Azure, GCP)
- Crypto-shred implementation guide
- Deletion verification methods
- ISMS-REF-A.5.23 integration notes (if available)

## Column Definitions (17 standard + 3 extended = 20 total)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Cloud Provider / Service | 35 | Text | Primary identifier (e.g., "AWS - Production Environment") |
| B | Data Classification | 20 | Dropdown | Public / Internal / Confidential / Restricted |
| C | Responsible Role | 20 | Text | Cloud Administrator, DevOps, etc. |
| D | Deletion Method Available | 30 | Dropdown | API / Lifecycle Policy / Manual / Crypto-Shred / Support Ticket |
| E | Deletion Verification Method | 30 | Dropdown | Audit Logs / Certificate / Crypto-Shred / Testing / None |
| F | Status | 18 | Dropdown | ✅ / ⚠️ / ❌ / N/A |
| G | Contract Start Date | 15 | Date | When service contract began |
| H | Last Deletion Verification | 15 | Date | Most recent deletion test or certificate |
| I | Next Verification Date | 15 | Date | Scheduled next verification |
| J | Gap Identified | 30 | Text | If not compliant, describe issue |
| K | Remediation Plan | 30 | Text | How gap will be addressed |
| L | Target Completion | 15 | Date | Remediation deadline |
| M | Risk Level | 15 | Dropdown | Critical / High / Medium / Low |
| N | Evidence Reference | 20 | Text | Link to Evidence Register (EV-XXX) |
| O | Notes / Comments | 30 | Text | Additional context |
| P | Remediation Owner | 20 | Text | Person responsible for fix |
| Q | Budget Required | 15 | Dropdown | Yes / No / Unknown |
| R | Provider Tier | 25 | Dropdown | Tier 1 (Enterprise) / Tier 2 (Mid-Market) / Tier 3 (Small) / Unknown / See ISMS-REF-A.5.23 |
| S | Deletion SLA (Days) | 20 | Number | Contractual deletion timeline (0 for immediate) |
| T | Multi-Region Verified | 20 | Dropdown | Yes / No / Single Region Only / N/A |

## Data Validation Rules

**Column D - Deletion Method Available:**
```
Dropdown: API, Lifecycle Policy, Manual, Crypto-Shred, Support Ticket, Unknown
```

**Column E - Deletion Verification Method:**
```
Dropdown: Audit Logs, Deletion Certificate, Crypto-Shred (Key Destruction), Testing (Recovery Attempt), None
```

**Column F - Status:**
```
Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A
```

**Compliance Logic:**

- ✅ Compliant: API or Crypto-Shred available + Verification method implemented + SLA ≤90 days
- ⚠️ Partial: Manual deletion available + Some verification + SLA 90-180 days
- ❌ Non-Compliant: Support ticket only OR no verification OR SLA >180 days

**Column M - Risk Level:**
```
Dropdown: Critical, High, Medium, Low
```

**Column Q - Budget Required:**
```
Dropdown: Yes, No, Unknown
```

**Column R - Provider Tier:**
```
Dropdown: Tier 1 (Enterprise), Tier 2 (Mid-Market), Tier 3 (Small/Niche), Unknown, See ISMS-REF-A.5.23
```

**If ISMS-REF-A.5.23 available:** Select "See ISMS-REF-A.5.23" and reference registry for tier
**If not available:** Manually assess tier based on provider size and capabilities

**Column S - Deletion SLA (Days):**
```
Number (integer): 0 (immediate), 1-365
```

**Benchmarks:**

- 0: Immediate (API deletion, crypto-shred)
- 1-30: Excellent (enterprise cloud providers)
- 31-90: Acceptable (mid-market providers)
- 91-180: Borderline (requires justification)
- >180: Non-compliant (unless legal retention requirement)

**Column T - Multi-Region Verified:**
```
Dropdown: Yes, No, Single Region Only, N/A
```

**Purpose:** Ensure deletion propagates across all geographic regions where data is replicated.

## Conditional Formatting

**Status Column (F):**

- ✅ Compliant: Green fill (RGB: 198, 239, 206)
- ⚠️ Partial: Yellow fill (RGB: 255, 235, 156)
- ❌ Non-Compliant: Red fill (RGB: 255, 199, 206)

**Deletion SLA Exceeds Thresholds:**

- If Column S > 180 days: Red fill (non-compliant)
- If Column S 91-180 days: Yellow fill (borderline)
- If Column S ≤90 days: No special formatting (acceptable)

**No Verification Method:**

- If Column E = "None": Orange fill on entire row (high risk - cannot verify deletion)

**Risk Level Column (M):**

- Critical: Red fill (RGB: 255, 199, 206)
- High: Orange fill (RGB: 255, 230, 153)
- Medium: Yellow fill (RGB: 255, 242, 204)
- Low: No special formatting

## Reference Tables (Rows 24-75)

**Table 1: Cloud Provider Deletion Policies (Rows 26-50)**

| Provider | Service | Deletion Method | Verification Available | Soft Delete Default | Crypto-Shred Support |
|----------|---------|----------------|----------------------|-------------------|-------------------|
| **AWS** | S3 | API (DeleteObject) | CloudTrail audit logs | Disabled (versioning opt-in) | Yes (CMK deletion) |
| **AWS** | EC2 | API (TerminateInstances) | CloudTrail audit logs | N/A | Yes (encrypted EBS) |
| **AWS** | RDS | API (DeleteDBInstance) | CloudTrail audit logs | Retention period configurable | Yes (encryption at rest) |
| **Azure** | Blob Storage | API (Delete Blob) | Azure Monitor logs | **Enabled (7 days default)** | Yes (CMK deletion) |
| **Azure** | VMs | API (Delete VM) | Activity logs | N/A | Yes (disk encryption) |
| **Azure** | SQL Database | API (Delete Database) | Activity logs | Retention period configurable | Yes (TDE with CMK) |
| **GCP** | Cloud Storage | API (Delete Object) | Cloud Audit Logs | Disabled | Yes (CMEK destruction) |
| **GCP** | Compute Engine | API (Delete Instance) | Cloud Audit Logs | N/A | Yes (encrypted disks) |
| **GCP** | Cloud SQL | API (Delete Instance) | Cloud Audit Logs | Retention period configurable | Yes (CMEK) |

**Table 2: Crypto-Shred Implementation by Provider (Rows 52-68)**

**AWS Crypto-Shred (S3, EBS, RDS):**
```
1. Enable encryption with Customer Master Key (CMK) - NOT default aws/s3 key
2. Use unique CMK per data set (bucket, volume, database)
3. When retention expires: Delete data via API → Schedule CMK deletion
4. CMK enters "PendingDeletion" state (7-30 day waiting period)
5. After waiting period: CMK destroyed, data cryptographically unrecoverable
6. Verify: CMK status = "PendingDeletion" or "Deleted" in KMS console
```

**Azure Crypto-Shred (Blob, Disk, SQL):**
```
1. Enable encryption with Customer-Managed Key (CMK) in Azure Key Vault
2. Use unique key per storage account / disk / database
3. When retention expires: Delete data via API → Delete key in Key Vault
4. Key marked as "deleted", soft delete period applies (configurable 7-90 days)
5. Purge key after soft delete period
6. Verify: Key status = "deleted" or "purged" in Key Vault
```

**GCP Crypto-Shred (Cloud Storage, Disk, Cloud SQL):**
```
1. Enable encryption with Customer-Managed Encryption Key (CMEK)
2. Use unique key per bucket / disk / database
3. When retention expires: Delete data via API → Destroy key in Cloud KMS
4. Key marked for destruction (24 hour minimum before actual destruction)
5. After destruction period: Key permanently destroyed
6. Verify: Key state = "DESTROY_SCHEDULED" or "DESTROYED" in Cloud KMS
```

**Table 3: Deletion Verification Methods (Rows 70-75)**

| Verification Method | Implementation | Audit Evidence | Pros | Cons |
|---------------------|----------------|---------------|------|------|
| **Audit Logs** | Review CloudTrail/Azure Monitor/Cloud Audit Logs | Log export or screenshot | Real-time, automated | Only confirms API call, not data overwrite |
| **Deletion Certificate** | Request from cloud provider support | Signed certificate PDF | Legally binding | Enterprise support required, manual process |
| **Crypto-Shred** | Delete encryption key (CMK/CMEK) | Key deletion event in logs | Immediate cryptographic erasure | Requires unique keys per data set |
| **Testing** | Attempt data access after deletion | 404/403 error screenshots | Direct verification | Only confirms inaccessibility, not overwrite |

---

# Sheet 3: SaaS Application Deletion

## Purpose
Assess deletion capabilities for Software-as-a-Service applications.

## Sheet Layout

**Header Section (Rows 1-9):**

- Row 1: Sheet title "3. SaaS Application Deletion Capabilities"
- Row 2: Assessment objective
- Row 3: Instructions for completion
- Rows 4-6: SaaS deletion procedure guidance
- Row 7: Blank separator
- Row 8: Warning: "Check for data in integrations (Zapier, APIs) before deletion"
- Row 9: Column headers (frozen)

**Data Entry Section (Rows 10-22):**

- 13 rows for SaaS applications (yellow fill)
- Focus: Deletion accessibility and verification

**Reference Section (Rows 24-70):**

- SaaS category deletion challenges
- Common SaaS deletion procedures
- Integration mapping guidance

## Column Definitions (Standard A-Q + Extended R-T)

**Columns A-Q:** Same as Sheet 2 (standard columns)

**Extended Columns (R-T) - SaaS-Specific:**

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| R | Application Category | 25 | Dropdown | CRM / HR / Marketing / Collaboration / Finance / DevOps / Other |
| S | Deletion Procedure | 35 | Dropdown | API / Admin UI / Support Ticket / Unknown |
| T | Data Export Capability | 25 | Dropdown | Full Export Available / Partial Export / No Export / Unknown |

## Data Validation Rules (Extended Columns)

**Column R - Application Category:**
```
Dropdown: CRM, HR, Marketing, Collaboration, Finance, DevOps, Analytics, Security, Other
```

**Column S - Deletion Procedure:**
```
Dropdown: API (Programmatic), Admin UI (Self-Service), Support Ticket (Vendor Assisted), Unknown
```

**Compliance Preference:**

- **Best:** API (automated, verifiable via logs)
- **Acceptable:** Admin UI (self-service, but manual)
- **Problematic:** Support Ticket (slow, no direct control)
- **Critical:** Unknown (high risk - deletion capability not verified)

**Column T - Data Export Capability:**
```
Dropdown: Full Export Available, Partial Export, No Export, Unknown
```

**GDPR Relevance:** Data export required for GDPR Article 20 (data portability) and enables deletion verification (export before delete, verify export complete, then delete).

## Reference Tables (Rows 24-70)

**Table 1: SaaS Deletion Challenges by Category (Rows 26-48)**

| Category | Common SaaS | Deletion Challenge | Mitigation |
|----------|------------|-------------------|------------|
| **CRM** | Salesforce, HubSpot | Data dependencies (contacts, opportunities, cases linked) | Cascade delete or export dependencies first |
| **HR** | Workday, BambooHR | Legal retention (employee records retained per law) | Document retention exceptions, delete post-retention |
| **Marketing** | Marketo, Mailchimp | Data shared with third parties (email service providers) | Map all integrations, delete from subprocessors |
| **Collaboration** | Slack, Microsoft Teams | Data scattered (messages, files, shared channels) | Full workspace export before deletion |
| **Finance** | QuickBooks, NetSuite | Financial retention mandates (cannot delete per GDPR if legal retention) | Document legal retention basis |
| **DevOps** | GitHub, GitLab | Source code retention (IP protection) | Separate personal data from code, delete personal only |

**Table 2: Common SaaS Deletion Procedures (Rows 50-65)**

**Salesforce:**

- **Bulk Delete:** Admin UI (200 records max), Data Loader (5M records)
- **API:** REST/SOAP API (DELETE method)
- **Account Closure:** Support ticket (complete org deletion)
- **Verification:** Audit logs (setup audit trail), recycle bin check

**Microsoft 365:**

- **User Deletion:** Admin Center (soft delete 30 days, then hard delete)
- **Mailbox Deletion:** Exchange Admin Center
- **OneDrive Deletion:** SharePoint Admin Center (files retained 30 days in recycle bin)
- **Verification:** Compliance Center audit logs

**Google Workspace:**

- **User Deletion:** Admin Console (soft delete 20 days, then hard delete)
- **Drive Deletion:** User deletion includes Drive files
- **Shared Drive:** Manual deletion required (not automatically deleted with user)
- **Verification:** Admin audit logs

**HubSpot:**

- **Contact Deletion:** Contacts menu (bulk delete)
- **Engagement Deletion:** Manual or API
- **Account Closure:** Support ticket
- **Verification:** Email confirmation from support

**Table 3: SaaS Integration Mapping (Rows 67-70)**

**Common Integration Points:**

- Zapier automations (data synchronized to other services)
- Native integrations (CRM ↔ Marketing, HR ↔ Payroll)
- API connections (custom integrations, data warehouse)
- Single Sign-On (SSO) - not data sync, but access audit trail

**Deletion Order:** Delete from downstream integrations FIRST, then delete from source SaaS (prevents re-synchronization).

---

# Sheet 4: Vendor Contract Assessment

## Purpose
Assess vendor contracts for deletion clauses, SLAs, and GDPR Article 28 compliance.

## Sheet Layout

**Header Section (Rows 1-9):**

- Row 1: Sheet title "4. Vendor Contract & DPA Assessment"
- Row 2: Assessment objective
- Row 3: Instructions for completion
- Rows 4-6: Strong deletion clause criteria
- Row 7: Blank separator
- Row 8: Requirement: "All vendors processing personal data must have DPA with deletion clause"
- Row 9: Column headers (frozen)

**Data Entry Section (Rows 10-22):**

- 13 rows for vendor contracts (yellow fill)
- Focus: Contractual adequacy

**Reference Section (Rows 24-80):**

- Strong vs. weak deletion clause examples
- GDPR Article 28 DPA requirements
- Deletion SLA benchmarks
- Contract negotiation tips

## Column Definitions (Standard A-Q + Extended R-T)

**Columns A-Q:** Same as Sheet 2 (standard columns)

**Extended Columns (R-T) - Contract-Specific:**

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| R | DPA Deletion Clause Strength | 30 | Dropdown | Strong / Weak / Missing / N/A (No Personal Data) |
| S | Deletion SLA (Days) | 20 | Number | Contractual deletion timeline (blank if not specified) |
| T | Certificate of Deletion Provision | 30 | Dropdown | Required / Optional / Not Provided / Unknown |

## Data Validation Rules (Extended Columns)

**Column R - DPA Deletion Clause Strength:**
```
Dropdown: Strong, Weak, Missing, N/A (No Personal Data)
```

**Strength Criteria:**

**Strong:**

- Specifies deletion method (NIST standards, secure deletion)
- Includes deletion SLA (≤90 days typical)
- Requires deletion certificate or audit log evidence
- Covers all subprocessors
- Includes penalty for non-compliance

**Weak:**

- Vague language ("reasonable efforts")
- No specific deletion timeline
- No verification method
- Excludes backups or subprocessors

**Missing:**

- Contract has no deletion clause
- Consumer terms of service (no DPA)

**Column S - Deletion SLA (Days):**
```
Number (integer): 0-365 (blank if not specified in contract)
```

**Column T - Certificate of Deletion Provision:**
```
Dropdown: Required (contractually mandated), Optional (available upon request), Not Provided, Unknown
```

## Reference Tables (Rows 24-80)

**Table 1: Strong Deletion Clause Example (Rows 26-40)**

```
"Deletion of Personal Data"

1. Timeline: Upon termination or upon Controller's written request, Processor shall delete 
   all Personal Data within thirty (30) days.

2. Scope: Deletion shall include all Personal Data in Processor's possession or control, 
   including: (a) production systems, (b) backup systems, (c) disaster recovery systems, 
   (d) logs and archives, (e) all subprocessor systems.

3. Method: Processor shall use secure deletion methods compliant with NIST SP 800-88 
   "Purge" or "Destroy" categories for data classified as Confidential or Restricted.

4. Verification: Processor shall provide Controller with a signed Certificate of Deletion 
   confirming: (a) deletion completion date, (b) systems from which data deleted, 
   (c) deletion method used, (d) subprocessor deletion confirmations.

5. Penalties: Failure to delete within SLA results in liquidated damages of $1,000 USD 
   per day until deletion completed and verified.

6. Exceptions: Processor may retain Personal Data to the extent required by applicable 
   law, provided Processor: (a) notifies Controller of legal retention requirement, 
   (b) isolates retained data, (c) deletes upon expiration of legal retention period.
```

**Table 2: Weak Deletion Clause Example (Rows 42-50)**

```
"Data Retention"

Vendor will make reasonable commercial efforts to delete Customer Data upon request, 
subject to technical and legal limitations. Deletion may take up to one hundred eighty 
(180) days. Vendor retains data in backup systems per its standard retention policy. 
Vendor is not liable for data retained in backups or by third-party subcontractors.
```

**Issues:**

- ❌ Vague language ("reasonable commercial efforts")
- ❌ Long SLA (180 days - exceeds GDPR 30-day recommendation)
- ❌ Excludes backups (GDPR violation if personal data persists)
- ❌ Excludes subprocessors (GDPR Article 28 violation)
- ❌ No verification method
- ❌ No liability for failure

**Table 3: GDPR Article 28 DPA Requirements (Rows 52-70)**

**Required DPA Clauses (Beyond Deletion):**

- Processing instructions (controller specifies purposes and means)
- Confidentiality obligations (processor employees bound by confidentiality)
- Security measures (appropriate technical and organizational measures)
- Subprocessor engagement (prior authorization required)
- Data subject rights assistance (help controller respond to GDPR requests)
- **Deletion or return** (upon termination)
- Audit rights (controller can audit processor compliance)
- International transfers (if applicable, safeguards required)

**Table 4: Deletion SLA Benchmarks (Rows 72-80)**

| Vendor Tier | Typical SLA | Acceptable Range | GDPR Consideration |
|------------|-------------|------------------|-------------------|
| **Tier 1 (Enterprise)** | 30 days | 15-60 days | Compliant |
| **Tier 2 (Mid-Market)** | 60 days | 30-90 days | Compliant if justified |
| **Tier 3 (Small)** | 90 days | 60-120 days | Borderline (may not meet GDPR data subject requests) |
| **Consumer / Free Tier** | Not specified | N/A | Non-compliant (no SLA = unacceptable risk) |

---

# Sheet 5: Subprocessor Mapping

## Purpose
Identify all subprocessors handling organizational data and assess deletion risk.

## Sheet Layout

**Header Section (Rows 1-9):**

- Row 1: Sheet title "5. Subprocessor Mapping & Deletion Assessment"
- Row 2: Assessment objective
- Row 3: Instructions for completion
- Rows 4-6: GDPR Article 28 subprocessor requirements
- Row 7: Blank separator
- Row 8: Reminder: "Primary vendor liable for subprocessor deletion failures"
- Row 9: Column headers (frozen)

**Data Entry Section (Rows 10-22):**

- 13 rows for subprocessors (yellow fill)
- Focus: Subprocessor identification and control

**Reference Section (Rows 24-65):**

- Subprocessor disclosure sources
- Multi-tier subprocessing risks
- Primary vendor liability framework

## Column Definitions (Standard A-Q + Extended R-T)

**Columns A-Q:** Same as Sheet 2 (standard columns)

**Extended Columns (R-T) - Subprocessor-Specific:**

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| R | Primary Vendor | 30 | Text | Which vendor disclosed this subprocessor |
| S | Subprocessor Function | 30 | Dropdown | Hosting / Analytics / Support / Payment Processing / Other |
| T | Primary Vendor Control Over Deletion | 35 | Dropdown | Direct Control / Coordinates Deletion / No Control / Unknown |

## Data Validation Rules (Extended Columns)

**Column R - Primary Vendor:**
```
Text (free entry): Name of vendor who disclosed this subprocessor
```

**Column S - Subprocessor Function:**
```
Dropdown: Hosting, Analytics, Support, Payment Processing, Email Delivery, CDN, Backup, Other
```

**Column T - Primary Vendor Control Over Deletion:**
```
Dropdown: Direct Control (Primary vendor can delete from subprocessor), Coordinates Deletion (Primary vendor instructs subprocessor), No Control (Subprocessor independent), Unknown
```

**Compliance:**

- **Direct Control:** Ideal - primary vendor deletes from subprocessor directly
- **Coordinates Deletion:** Acceptable - primary vendor instructs subprocessor, receives confirmation
- **No Control:** High Risk - subprocessor deletion independent, may not occur
- **Unknown:** Critical Risk - deletion process not documented

## Reference Tables (Rows 24-65)

**Table 1: Subprocessor Disclosure Sources (Rows 26-38)**

| Source | How to Access | Update Frequency | Reliability |
|--------|---------------|------------------|-------------|
| **Data Processing Agreement (DPA)** | Contract appendix or schedule | Annual (or upon change) | High |
| **Vendor Website** | Trust center, compliance page | Monthly (varies by vendor) | Medium |
| **Subprocessor Change Notifications** | Email from vendor | As changes occur | High |
| **SOC 2 Type II Report** | Request from vendor or auditor | Annual | High |
| **Direct Request to Vendor** | Email legal/compliance contact | On request | High |

**Examples:**

- **Salesforce:** https://www.salesforce.com/company/legal/third-party-subprocessors/
- **AWS:** https://aws.amazon.com/compliance/sub-processors/
- **Microsoft:** https://aka.ms/Online_Services_Subprocessor_List

**Table 2: Multi-Tier Subprocessing Example (Rows 40-52)**

```
Tier 0: [Organization] (Controller)
   ↓
Tier 1: Salesforce (Processor)
   ↓
Tier 2: AWS (Subprocessor - hosting)
   ↓
Tier 3: Equinix (Sub-subprocessor - data center)

Deletion Flow:
1. [Organization] requests deletion from Salesforce
2. Salesforce deletes from application database
3. Salesforce instructs AWS to delete S3 backups
4. AWS deletion propagates to Equinix data centers
5. Salesforce provides deletion certificate covering all tiers
```

**Risk:** Each additional tier increases deletion complexity and verification difficulty.

**Mitigation:** DPA with Tier 1 vendor must flow deletion obligations down to all subprocessor tiers.

**Table 3: Undisclosed Subprocessor Risks (Rows 54-65)**

**Scenario: Vendor Uses Undisclosed Subprocessor**

- Vendor contracts with new subprocessor without notifying controller
- Controller requests deletion, unaware of new subprocessor
- Vendor deletes from known systems, but data persists in undisclosed subprocessor
- **Result:** Incomplete deletion, GDPR violation

**Prevention:**

- DPA clause: "Vendor must notify controller 30 days before engaging new subprocessor"
- Regular subprocessor list review (quarterly)
- Exercise objection right if subprocessor lacks adequate deletion capabilities
- Audit vendor compliance (SOC 2 Type II should test subprocessor management)

---

# Sheet 6: Shadow IT Assessment

## Purpose
Identify unapproved cloud services containing organizational data and assess remediation priority.

## Sheet Layout

**Header Section (Rows 1-9):**

- Row 1: Sheet title "6. Shadow IT Discovery & Remediation"
- Row 2: Assessment objective
- Row 3: Instructions for completion
- Rows 4-6: Shadow IT definition and risks
- Row 7: Blank separator
- Row 8: Warning: "Shadow IT = No deletion control, high GDPR risk"
- Row 9: Column headers (frozen)

**Data Entry Section (Rows 10-22):**

- 13 rows for Shadow IT services (yellow fill)
- Focus: Discovery and remediation planning

**Reference Section (Rows 24-70):**

- Shadow IT discovery methods
- Remediation options
- User training recommendations

## Column Definitions (Standard A-Q + Extended R-T)

**Columns A-Q:** Same as Sheet 2 (standard columns)

**Extended Columns (R-T) - Shadow IT-Specific:**

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| R | Discovery Method | 30 | Dropdown | CASB / Expense Reports / Network Logs / User Survey / Other |
| S | Data Sensitivity Assessment | 25 | Dropdown | Confidential/Restricted / Internal / Public / Unknown |
| T | Remediation Option | 30 | Dropdown | Migrate to Approved Service / Formalize (Add DPA) / Prohibit & Delete / Under Review |

## Data Validation Rules (Extended Columns)

**Column R - Discovery Method:**
```
Dropdown: CASB, Expense Reports, Network Traffic Analysis, SSO Logs, User Survey, Other
```

**Column S - Data Sensitivity Assessment:**
```
Dropdown: Confidential/Restricted, Internal, Public, Unknown (requires investigation)
```

**Risk Priority:**

- **Confidential/Restricted:** Critical priority (immediate remediation)
- **Internal:** High priority (remediate within 90 days)
- **Public:** Medium priority (formalize or accept risk)
- **Unknown:** High priority (assess data sensitivity first, then remediate)

**Column T - Remediation Option:**
```
Dropdown: Migrate to Approved Service, Formalize (Upgrade to Enterprise + DPA), Prohibit & Delete, Under Review
```

**Remediation Decision Matrix:**

| Data Sensitivity | Service Tier | Recommended Remediation |
|-----------------|--------------|------------------------|
| **Confidential/Restricted** | Free / Consumer | **Prohibit & Delete** (immediate) |
| **Confidential/Restricted** | Paid / No DPA | **Migrate** or **Formalize** (add DPA) |
| **Internal** | Free / Consumer | **Migrate** or **Formalize** |
| **Internal** | Paid / No DPA | **Formalize** (add DPA) |
| **Public** | Any | **Accept Risk** or **Formalize** |

## Reference Tables (Rows 24-70)

**Table 1: Shadow IT Discovery Methods Comparison (Rows 26-45)**

| Method | Coverage | Cost | Ease | Real-Time Detection |
|--------|----------|------|------|-------------------|
| **CASB** | High (80-90%) | High ($) | Medium | Yes |
| **Expense Reports** | Medium (50-70%) | Low | Easy | No (monthly lag) |
| **Network Logs** | Medium (60-80%) | Low | Hard (technical) | Yes |
| **SSO Logs** | Low (30-50%) | Low | Easy | Yes (if SSO used) |
| **User Surveys** | Low (20-40%) | Low | Easy | No |

**Recommendation:** Combine methods (CASB + Expense Reports) for best coverage.

**Table 2: Shadow IT Remediation Process (Rows 47-60)**

**Step 1: Discovery**

- Deploy CASB or run expense report analysis
- Identify all unapproved cloud services
- Document in assessment (Sheet 6)

**Step 2: Data Sensitivity Assessment**

- For each Shadow IT service, determine: What data is stored?
- Classify data (Confidential, Internal, Public)
- Prioritize remediation (Confidential = highest priority)

**Step 3: Remediation Planning**

- **Option A: Migrate to Approved Service**
  - Export data from Shadow IT service
  - Import to approved, DPA-compliant service
  - Delete from Shadow IT service
  - Verify deletion (if possible)

- **Option B: Formalize Usage**
  - Upgrade to enterprise tier
  - Negotiate DPA with vendor
  - Add vendor to approved vendor list
  - Document deletion capabilities (add to Sheet 2 or 3)

- **Option C: Prohibit & Delete**
  - Policy: Immediate data deletion
  - User training on approved alternatives
  - Monitor for recurrence (CASB alerts)

**Step 4: User Training**

- Explain Shadow IT risks (data loss, compliance violations, no deletion control)
- Provide approved alternatives (list of approved cloud services)
- Simplify approval process (reduce temptation to bypass)

**Step 5: Ongoing Monitoring**

- CASB continuous monitoring
- Quarterly expense report review
- Annual user surveys

**Table 3: Common Shadow IT Services (Rows 62-70)**

| Category | Common Services | Risk Level | Recommended Action |
|----------|----------------|------------|-------------------|
| **File Sharing** | Personal Dropbox, Google Drive, WeTransfer | High | Migrate to approved (OneDrive, Box) |
| **Collaboration** | Personal Slack, Discord, WhatsApp | Medium | Migrate to approved (Teams, Enterprise Slack) |
| **Project Management** | Personal Trello, Asana, Monday.com | Medium | Formalize (add DPA) or migrate |
| **Development** | Personal GitHub, GitLab, Bitbucket | High | Migrate to organization account |
| **Analytics** | Free Google Analytics, Mixpanel | Low | Formalize (upgrade to paid tier) |

---

# Sheet 7: Summary Dashboard

## Purpose
Aggregate third-party deletion compliance metrics and identify critical vendor risks.

## Sheet Layout

**Header Section (Rows 1-5):**

- Row 1: Sheet title "7. Summary Dashboard - Third-Party Deletion Compliance"
- Row 2: Assessment period and version
- Row 3: Generated date (auto-populated)
- Row 5: Overall compliance status indicator (colored)

**Section 1: Overall Compliance Summary (Rows 7-20)**

| Metric | Value | Status |
|--------|-------|--------|
| Total Vendors Assessed | =COUNTA(Sheet2!A10:A22)+COUNTA(Sheet3!A10:A22)+... | N/A |
| Vendors with Strong Deletion Clauses | =COUNTIF(Sheet4!R10:R22,"Strong") | Formula |
| Vendors with Weak/Missing Deletion Clauses | =COUNTIF(Sheet4!R10:R22,"Weak")+COUNTIF(Sheet4!R10:R22,"Missing") | Formula |
| Vendors with Deletion Certificates | =COUNTIF(Sheet2!T10:T22,"Yes")+... | Formula |
| Overall Compliance % | =Compliant/(Total-N/A)*100 | Conditional format |
| Shadow IT Services Identified | =COUNTA(Sheet6!A10:A22) | Formula |

**Compliance Percentage Color Coding:**

- ≥90%: Green fill (excellent)
- 80-89%: Yellow fill (acceptable)
- 70-79%: Orange fill (needs improvement)
- <70%: Red fill (unacceptable)

**Section 2: Vendor Risk by Category (Rows 22-38)**

| Category | Vendor Count | Strong DPA | Weak/Missing DPA | Deletion Certificate | Compliance % |
|----------|-------------|-----------|-----------------|---------------------|--------------|
| Cloud Providers (IaaS/PaaS) | Formula | Formula | Formula | Formula | Formula |
| SaaS Applications | Formula | Formula | Formula | Formula | Formula |
| Total | Formula | Formula | Formula | Formula | Formula |

**Section 3: Critical Gaps Requiring Immediate Attention (Rows 40-55)**

Auto-populated table pulling rows where:

- (Data Classification = "Confidential" OR "Restricted") AND (DPA Deletion Clause = "Weak" OR "Missing") OR
- (Deletion SLA > 90 days) OR
- (Status = "❌ Non-Compliant" AND Risk Level = "Critical" OR "High")

| Vendor | Classification | DPA Strength | Deletion SLA | Gap | Target Completion |
|--------|---------------|--------------|--------------|-----|-------------------|
| [Auto-pull from assessment sheets] | | | | | |

**Section 4: Subprocessor Disclosure Status (Rows 57-68)**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Vendors with Disclosed Subprocessors | =COUNTIF(Sheet5!A10:A22,"<>") | 100% of vendors | Conditional |
| Subprocessors with Deletion Assessment | =COUNTIFS(Sheet5!T10:T22,"<>Unknown") | 100% | Conditional |
| Multi-Tier Subprocessing Identified | =COUNTIF(Sheet5!Notes,"multi-tier") | Document all | N/A |

**Section 5: Shadow IT Status (Rows 70-80)**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Shadow IT Services Identified | =COUNTA(Sheet6!A10:A22) | 0 (ideal) | Conditional |
| Shadow IT with Confidential/Restricted Data | =COUNTIF(Sheet6!S10:S22,"Confidential/Restricted") | 0 (mandatory) | Conditional |
| Shadow IT Remediated | =COUNTIF(Sheet6!T10:T22,"Migrate*")+COUNTIF(Sheet6!T10:T22,"Prohibit*") | =Total Shadow IT | Conditional |
| Shadow IT Remediation % | =Remediated/Total*100 | 100% | Conditional |

---

# Sheet 8: Evidence Register

(Same structure as previous assessments - 100 rows, auto-numbered EV-001 through EV-100)

**Evidence Types Specific to Third-Party Assessment:**

- Vendor contracts (DPAs)
- Deletion clause excerpts
- Deletion certificates
- Subprocessor disclosure notices
- Cloud provider compliance reports (SOC 2, ISO 27001)
- CASB Shadow IT reports
- Vendor email confirmations
- Audit log exports

---

# Sheet 9: Approval Sign-Off

(Same three-level approval structure as previous assessments)

**Approval Focus for Third-Party Assessment:**

- Level 1: Vendor inventory completeness, deletion capability accuracy
- Level 2: Contract adequacy, GDPR Article 28 compliance, remediation resourcing
- Level 3: Overall vendor deletion risk, contract renegotiation commitments

---

# Conditional Formatting Rules

(Standard status column formatting + assessment-specific rules)

**Additional Rules for Third-Party Assessment:**

## Weak/Missing DPA Deletion Clause (Sheet 4)

**Rule: Confidential/Restricted Data + Weak/Missing DPA**

- Condition: Column B = "Confidential" OR "Restricted" AND Column R = "Weak" OR "Missing"
- Format: Fill color RGB(255, 150, 150) - Bright red, Bold
- Applies to: Entire row
- Reason: High GDPR risk - sensitive data with inadequate contractual deletion protection

## Deletion SLA Exceeds GDPR Timeline (Sheet 2, Sheet 3, Sheet 4)

**Rule: Deletion SLA > 90 Days**

- Condition: Column S > 90
- Format: Fill color RGB(255, 199, 206) - Light red
- Applies to: Column S
- Reason: May not meet GDPR Article 17 data subject request timeline (30 days)

## Shadow IT with Sensitive Data (Sheet 6)

**Rule: Shadow IT Confidential/Restricted**

- Condition: Column S = "Confidential/Restricted"
- Format: Fill color RGB(255, 150, 150) - Bright red, Bold, White text
- Applies to: Entire row
- Reason: Critical priority - immediate remediation required

## No Deletion Verification Method (Sheet 2, Sheet 3)

**Rule: Verification Method = None**

- Condition: Column E = "None"
- Format: Fill color RGB(255, 230, 153) - Orange
- Applies to: Entire row
- Reason: Cannot verify deletion occurred - high audit risk

---

# Summary Dashboard Formulas

## Overall Compliance Calculation

**Total Vendors Assessed:**
```excel
=COUNTA(Sheet2!A10:A22) + COUNTA(Sheet3!A10:A22)
```

**Vendors with Strong Deletion Clauses:**
```excel
=COUNTIF(Sheet4!R10:R22,"Strong")
```

**Vendors with Weak/Missing Deletion Clauses:**
```excel
=COUNTIF(Sheet4!R10:R22,"Weak") + COUNTIF(Sheet4!R10:R22,"Missing")
```

**Overall Compliance %:**
```excel
=IF((COUNTA(Sheet4!F10:F22)-COUNTIF(Sheet4!F10:F22,"N/A"))=0,0,
   COUNTIF(Sheet4!F10:F22,"✅ Compliant")/
   (COUNTA(Sheet4!F10:F22)-COUNTIF(Sheet4!F10:F22,"N/A"))*100)
```

## Shadow IT Metrics

**Shadow IT Services Identified:**
```excel
=COUNTA(Sheet6!A10:A22)
```

**Shadow IT with Confidential/Restricted Data:**
```excel
=COUNTIF(Sheet6!S10:S22,"Confidential/Restricted")
```

**Shadow IT Remediation %:**
```excel
=IF(Shadow_IT_Total=0,100,
   (COUNTIF(Sheet6!T10:T22,"Migrate*")+COUNTIF(Sheet6!T10:T22,"Prohibit*"))/Shadow_IT_Total*100)
```

## Subprocessor Coverage

**Vendors with Disclosed Subprocessors:**
```excel
=COUNTA(Sheet5!A10:A22)
```

**Subprocessors Assessed for Deletion:**
```excel
=COUNTIFS(Sheet5!T10:T22,"<>Unknown")
```

---

# Python Script Integration

**Script:** `generate_a810_3_third_party_cloud.py`

**Key Customization Points:**

- ISMS-REF-A.5.23 integration (if available - populate Provider Tier dropdown)
- Vendor-specific deletion clause examples in reference tables
- CASB integration (if organization uses specific CASB, add vendor-specific guidance)
- Shadow IT service list (update common services table per organization patterns)

---

# Integration with ISMS-REF-A.5.23

**If Cloud Service Provider Registry Available:**

**Column R (Sheet 2) - Provider Tier:**

- Option: "See ISMS-REF-A.5.23" (dropdown value)
- On selection, user cross-references cloud provider registry for tier rating
- Registry provides: Deletion capability rating, recommended verification methods, standard DPA templates

**Benefits:**

- Consistency across assessments (same provider rated consistently)
- Pre-vetted deletion capabilities (reduce assessment time)
- Reference architecture (standard deletion patterns by provider)

**If Registry Not Available:**

- Manual tier assessment per this workbook's criteria
- Document assessment in Notes column
- Consider creating ISMS-REF-A.5.23 for future assessments

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Document Assembly Instructions

**To create the complete ISMS-IMP-A.8.10.3 v1.0 document:**

1. **Document Control + PART I: USER COMPLETION GUIDE** (Deliverable 1)
2. **PART II: TECHNICAL SPECIFICATION** (Deliverable 2, this file)

**Final Document Structure:**
```
ISMS-IMP-A.8.10.3 - Third-Party & Cloud Deletion Assessment v1.0

├── Document Control (Metadata, Version History)
│
├── PART I: USER COMPLETION GUIDE (~2,600 lines)
│   ├── 1. Assessment Overview (with GDPR Article 28 context)
│   ├── 2. Prerequisites
│   ├── 3. Assessment Workflow
│   ├── 4. Question-by-Question Guidance
│   ├── 5. Evidence Collection
│   ├── 6. Common Pitfalls
│   ├── 7. Quality Checklist
│   └── 8. Review & Approval
│
└── PART II: TECHNICAL SPECIFICATION (~1,800 lines)
    ├── 1. Workbook Structure Overview
    ├── 2. Sheet 1: Instructions & Legend (GDPR Article 28 overview)
    ├── 3. Sheet 2: Cloud Provider Deletion
    ├── 4. Sheet 3: SaaS Application Deletion
    ├── 5. Sheet 4: Vendor Contract Assessment
    ├── 6. Sheet 5: Subprocessor Mapping
    ├── 7. Sheet 6: Shadow IT Assessment
    ├── 8. Sheet 7: Summary Dashboard (Vendor risk breakdown)
    ├── 9. Sheet 8: Evidence Register
    ├── 10. Sheet 9: Approval Sign-Off
    ├── 11. Conditional Formatting Rules (including DPA strength, Shadow IT sensitive data)
    ├── 12. Summary Dashboard Formulas
    ├── 13. Python Script Integration
    └── 14. Integration with ISMS-REF-A.5.23
```

**Quality Checks Before Finalizing:**

- [ ] All GDPR Article 28 references accurate
- [ ] Cloud provider deletion policies current (AWS, Azure, GCP)
- [ ] Strong vs. weak deletion clause examples clear
- [ ] Shadow IT discovery methods comprehensive
- [ ] ISMS-REF-A.5.23 integration documented (conditional on registry availability)
- [ ] Document Control version shows 2.0
- [ ] All dates in DD.MM.YYYY format
- [ ] Consistent use of [Organization] placeholder

---

**END OF SPECIFICATION**

---

*"Entanglement is not just a theoretical curiosity; it is the key resource for quantum information processing."*
— Alain Aspect

<!-- QA_VERIFIED: 2026-01-31 -->
