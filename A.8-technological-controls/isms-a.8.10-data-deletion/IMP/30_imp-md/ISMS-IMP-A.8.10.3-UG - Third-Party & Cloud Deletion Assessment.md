**ISMS-IMP-A.8.10.3-UG - Third-Party & Cloud Deletion Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.10.3-UG |
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

**END OF USER GUIDE**

---

**Continue to PART II: TECHNICAL SPECIFICATION (Deliverable 2) for detailed Excel workbook structure, column definitions, validation rules, and Python script integration points.**

# ISMS-IMP-A.8.10.3 - Third-Party & Cloud Deletion Assessment
# DELIVERABLE 2: PART II - TECHNICAL SPECIFICATION

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
