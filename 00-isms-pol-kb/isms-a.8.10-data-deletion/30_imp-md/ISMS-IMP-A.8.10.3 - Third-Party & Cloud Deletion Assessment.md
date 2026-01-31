# ISMS-IMP-A.8.10.3 - Third-Party & Cloud Deletion Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.10.3  
**Assessment Area:** Third-Party and Cloud Provider Deletion Coordination  
**Related Policy:** ISMS-POL-A.8.10-S2.4 (Third-Party & Cloud Deletion)  
**Purpose:** Assess organization's ability to coordinate data deletion with cloud providers, SaaS vendors, and other third-party processors

**Key Principle:** This assessment is **vendor-neutral**. Organizations document THEIR specific cloud providers, SaaS applications, and third-party relationships. The workbook provides structure; customers document their reality.

---

## Assessment Context

### What This Assessment Covers

This assessment evaluates the organization's approach to:
1. **Cloud Provider Deletion** - IaaS, PaaS, SaaS provider deletion capabilities and contracts
2. **SaaS Application Deletion** - CRM, HR, marketing, collaboration platform deletion
3. **Vendor Contract Assessment** - Deletion clauses, SLAs, and contractual obligations
4. **Subprocessor Mapping** - Data flow through third-party supply chain
5. **Vendor Performance Tracking** - Certificate of Deletion, response times, incidents

### What This Assessment Does NOT Cover

- **Technical deletion methods** (see ISMS-IMP-A.8.10.2 - Deletion Methods)
- **WHEN to delete** data (see ISMS-IMP-A.8.10.1 - Retention Triggers)
- **Internal deletion verification** (see ISMS-IMP-A.8.10.4 - Verification & Evidence)

### Related ISMS Documents

- **ISMS-POL-A.8.10** - Information Deletion Policy (Master)
- **ISMS-POL-A.8.10-S2.4** - Third-Party & Cloud Deletion Requirements
- **ISMS-REF-A.5.23** - Cloud Service Provider Registry (68 providers, 10 tiers)
- **ISMS-IMP-A.8.10.2** - Deletion Methods Assessment (technical context)
- **GDPR Article 28** - Processor obligations (deletion requirements)

---

## Workbook Structure

This workbook contains **9 sheets** organized as follows:

### Core Sheets
1. **Instructions & Legend** - How to use this workbook, GDPR processor requirements, definitions
2. **2. Cloud Provider Assessment** - Major cloud providers (IaaS, PaaS) deletion capabilities
3. **3. SaaS Application Deletion** - SaaS platforms (CRM, HR, collaboration) deletion
4. **4. Vendor Contract Review** - Contractual deletion clauses and SLAs
5. **5. Subprocessor Mapping** - Data flow and subprocessor deletion coordination
6. **6. Vendor Performance Tracking** - Deletion certificates, response times, incidents

### Summary & Administration
7. **Summary Dashboard** - Compliance overview, vendor risk assessment, critical gaps
8. **Evidence Register** - Links to supporting documentation (100 rows)
9. **Approval Sign-Off** - Three-level approval workflow

---

## Assessment Sheets - Column Definitions

### Standard Column Layout (Columns A-Q, 17 columns)

These columns appear in **Sheets 2-6** with minor variations:

| Column | Header | Width | Type | Validation Options | Purpose |
|--------|--------|-------|------|-------------------|---------|
| A | Provider / Vendor Name | 30 | Text | Free text | Primary identifier |
| B | Service Type | 22 | Dropdown | IaaS, PaaS, SaaS, Data Processor, Other | Classification |
| C | Business Owner | 18 | Text | Free text | Internal owner |
| D | Data Categories Processed | 25 | Text | Free text | What data they hold |
| E | Provider Tier | 12 | Dropdown | Tier 1-10 (from ISMS-REF-A.5.23) | Criticality |
| F | Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Traffic light |
| G | Contract Start Date | 12 | Date | Date picker | When relationship began |
| H | Last Contract Review | 12 | Date | Date picker | Governance |
| I | Next Contract Review | 12 | Date | Date picker | Scheduled review |
| J | Gap Identified | 25 | Text | Free text | If not compliant |
| K | Remediation Plan | 25 | Text | Free text | How to fix |
| L | Target Completion | 12 | Date | Date picker | Remediation deadline |
| M | Risk Level | 12 | Dropdown | Critical, High, Medium, Low | If gap exists |
| N | Evidence Reference | 20 | Text | Free text | Link to Evidence Register |
| O | Notes / Comments | 25 | Text | Free text | Additional context |
| P | Remediation Owner | 18 | Text | Free text | Who will fix |
| Q | Budget Required | 15 | Dropdown | Yes, No, Unknown | Resource planning |

### Extended Columns (R-U) - Sheet-Specific

**Sheet 2 (Cloud Provider Assessment):**
- R: **Deletion Method** (Dropdown: API Delete, Console Delete, Support Ticket, Account Closure, Unknown)
- S: **Deletion SLA (Days)** (Number: e.g., 30)
- T: **Certificate Provided** (Dropdown: Yes - Automatic, Yes - On Request, No, Unknown)
- U: **Multi-Region Verified** (Dropdown: Yes, No, N/A, Unknown)

**Sheet 3 (SaaS Application Deletion):**
- R: **Admin Portal Access** (Dropdown: Yes - Full, Yes - Limited, No, Unknown)
- S: **Data Export Available** (Dropdown: Yes - API, Yes - Manual, No, Unknown)
- T: **Deletion Request Method** (Dropdown: Self-Service, Email Request, Support Ticket, Account Manager)
- U: **GDPR DPA Signed** (Dropdown: Yes, No, N/A, Pending)

**Sheet 4 (Vendor Contract Review):**
- R: **Deletion Clause Present** (Dropdown: Yes - Specific, Yes - Generic, No, Unknown)
- S: **Deletion Timeline Specified** (Dropdown: Yes - Days Specified, Yes - "Reasonable Time", No)
- T: **Certificate of Deletion** (Dropdown: Contractually Required, Available on Request, Not Mentioned)
- U: **Audit Rights** (Dropdown: Yes - Deletion Audit, Yes - General Audit, No, Unknown)

**Sheet 5 (Subprocessor Mapping):**
- R: **Subprocessor Count** (Number: known subprocessors)
- S: **Subprocessor List Current** (Dropdown: Yes - Updated, Yes - Outdated, No - Unknown, N/A)
- T: **Deletion Flow Documented** (Dropdown: Yes - Flowchart, Yes - Description, No, Unknown)
- U: **Subprocessor Deletion SLA** (Dropdown: Covered by Prime, Separate Agreement, Unknown, N/A)

**Sheet 6 (Vendor Performance Tracking):**
- R: **Deletion Requests (Last 12M)** (Number: count of requests)
- S: **Average Response Time (Days)** (Number: actual performance)
- T: **Certificates Received** (Number: count)
- U: **Incidents / Failures** (Number: deletion failures)

---

## Validation Options - Dropdowns

### Service Type Options (Column B)
- IaaS (Infrastructure as a Service)
- PaaS (Platform as a Service)
- SaaS (Software as a Service)
- Data Processor (non-cloud)
- Subprocessor
- Other

### Provider Tier Options (Column E)
- Tier 1 (Hyperscaler - Critical Infrastructure)
- Tier 2 (Major Provider - High Dependency)
- Tier 3 (Significant Provider - Medium Dependency)
- Tier 4 (Standard Provider - Low Dependency)
- Tier 5 (Specialized Provider - Niche Service)
- Tier 6 (Regional Provider - Geographic Focus)
- Tier 7 (Emerging Provider - New/Startup)
- Tier 8 (Legacy Provider - Maintenance Mode)
- Tier 9 (Departmental - Shadow IT Risk)
- Tier 10 (Unknown/Unclassified)

*Reference ISMS-REF-A.5.23 for tier definitions and example providers*

### Data Classification Options (used in various contexts)
- Public
- Internal
- Confidential
- Restricted

### Status Options (Column F)
- ✅ Compliant
- ⚠️ Partial
- ❌ Non-Compliant
- N/A

### Risk Level Options (Column M)
- Critical
- High
- Medium
- Low

### Budget Required (Column Q)
- Yes
- No
- Unknown

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Legend

**Purpose:** Provide complete usage instructions, GDPR processor requirements, and definitions

**Content Structure:**

**Section 1: Document Information (Rows 1-8)**
- Workbook title and version
- Assessment date and assessor name
- Organization name
- Review period covered
- Related policy references

**Section 2: How to Use This Workbook (Rows 10-25)**
- Step-by-step instructions for completing assessment
- Integration with ISMS-REF-A.5.23 (Cloud Service Provider Registry)
- When to engage Legal/Procurement for contract review
- How to map data flows through subprocessors
- Evidence collection for deletion certificates
- Approval workflow instructions

**Section 3: GDPR Article 28 Processor Requirements (Rows 27-45)**

**Key GDPR Requirements for Processors:**

**Article 28(3)(e) - Deletion or Return:**
- Processor must delete or return all personal data after services end
- At the choice of the controller (organization)
- Unless EU/Member State law requires storage

**Article 28(3)(h) - Assistance with Data Subject Rights:**
- Processor must assist controller in responding to data subject requests
- Including deletion requests under Article 17 (Right to Erasure)

**Article 28(2) - Subprocessors:**
- Processor must not engage subprocessors without authorization
- Controller must be informed of subprocessor changes
- Same data protection obligations flow down to subprocessors

**Data Processing Agreement (DPA) Requirements:**
- Deletion obligations must be in writing (DPA/contract)
- Timeline for deletion should be specified
- Processor must provide means to verify deletion

**Section 4: Color Coding Legend (Rows 47-55)**
| Color | Meaning | Usage |
|-------|---------|-------|
| Blue header | Column headers | Do not edit |
| Yellow | Data entry cells | Complete these fields |
| Green | Compliant status | Contract has deletion clause + verified capability |
| Orange | Partial compliance | Clause exists but capability unverified |
| Red | Non-compliant | No deletion clause or capability |
| Gray | Reference information | Read-only guidance |
| White | Optional fields | Complete if relevant |

**Section 5: Key Definitions (Rows 57-75)**
- **Data Processor:** Third party processing personal data on behalf of organization (controller)
- **Data Controller:** Organization determining purposes and means of processing
- **Subprocessor:** Third party engaged by processor to process data
- **Data Processing Agreement (DPA):** Contract governing processor obligations (GDPR Art. 28)
- **Deletion SLA:** Service Level Agreement specifying deletion timeline
- **Certificate of Deletion:** Written confirmation that data has been deleted
- **Right to Erasure:** GDPR Article 17 right to request deletion
- **Return of Data:** Alternative to deletion - returning data to controller
- **Tier Classification:** Provider criticality ranking (ISMS-REF-A.5.23)
- **Shadow IT:** Unauthorized use of cloud/SaaS services

**Section 6: Provider Tier Quick Reference (Rows 77-90)**

*See ISMS-REF-A.5.23 for complete 68-provider registry*

| Tier | Description | Examples (Non-Exhaustive) | Deletion Risk |
|------|-------------|---------------------------|---------------|
| Tier 1 | Hyperscaler - Critical Infrastructure | AWS, Azure, GCP | Low (mature processes) |
| Tier 2 | Major Provider - High Dependency | Salesforce, Oracle Cloud, SAP | Low-Medium (established) |
| Tier 3 | Significant Provider - Medium Dependency | Dropbox, Box, Zendesk | Medium (varies by service) |
| Tier 4 | Standard Provider - Low Dependency | Regional cloud, niche SaaS | Medium-High (verify capability) |
| Tier 9 | Departmental - Shadow IT Risk | Unapproved SaaS, personal accounts | Very High (no contract) |
| Tier 10 | Unknown/Unclassified | Discovered via audit, unknown | Critical (no oversight) |

**Section 7: Important Notes (Rows 92-105)**
- Vendor-neutral approach explanation
- GDPR DPA requirement (mandatory for EU/EEA processors)
- Certificate of Deletion best practice (especially for Restricted data)
- Subprocessor notification requirements (GDPR Art. 28(2))
- Annual vendor contract review requirement
- Shadow IT discovery and remediation
- Link to related assessments (A.8.10.1, A.8.10.2, A.8.10.4)

---

### Sheet 2: Cloud Provider Assessment

**Purpose:** Assess deletion capabilities of major cloud providers (IaaS, PaaS)

**Assessment Question:**
*"Do we have documented deletion capabilities, contractual agreements, and performance metrics for all cloud infrastructure and platform providers?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.4, Section 2.4.1 (Cloud Provider Deletion)

**Column Structure:** A-U (21 columns total)
- Columns A-Q: Standard base columns
- Column R: Deletion Method
- Column S: Deletion SLA (Days)
- Column T: Certificate Provided
- Column U: Multi-Region Verified

**Data Entry Rows:** 13 rows (yellow-highlighted, Rows 10-22)

**Compliance Checklist (Rows 25-45):**

1. All cloud providers in use are identified and documented
2. Provider tier assigned per ISMS-REF-A.5.23 classification
3. Data Processing Agreement (DPA) signed for all providers
4. DPA includes specific deletion obligations and timeline
5. Deletion method documented (API, console, support ticket)
6. API-based deletion implemented for Tier 1-3 providers
7. Deletion SLA documented and reasonable (≤30 days preferred)
8. Certificate of Deletion available (automatic or on request)
9. Multi-region/multi-zone deletion tested and verified
10. Snapshot and backup deletion procedures documented
11. Account closure deletion behavior documented
12. Provider notifications sent for subprocessor changes
13. Annual contract review conducted
14. Deletion requests successfully executed in last 12 months
15. Provider included in ISMS-REF-A.5.23 registry (or add if new)

**Reference Table 1: Major Cloud Provider Deletion Capabilities (Rows 47-65)**

*See ISMS-REF-A.5.23 for complete provider details*

| Provider | Tier | Deletion Method | Typical SLA | Certificate Available | Notes |
|----------|------|----------------|-------------|----------------------|-------|
| AWS | Tier 1 | API Delete, Console | Immediate | On request | Per-service deletion APIs |
| Microsoft Azure | Tier 1 | API Delete, Portal | Immediate | On request | Azure Resource Manager APIs |
| Google Cloud (GCP) | Tier 1 | API Delete, Console | Immediate | On request | Cloud APIs per service |
| Oracle Cloud | Tier 2 | API Delete, Console | Immediate | On request | OCI APIs available |
| IBM Cloud | Tier 2 | API Delete, Console | Immediate | On request | Resource Controller APIs |
| Alibaba Cloud | Tier 2 | API Delete, Console | Immediate | On request | Regional considerations |
| DigitalOcean | Tier 3 | API Delete, Console | Immediate | On request | Simpler API structure |
| Linode (Akamai) | Tier 3 | API Delete, Console | Immediate | On request | Compute-focused |
| Hetzner Cloud | Tier 4 | API Delete, Console | Immediate | Limited | European provider |
| OVHcloud | Tier 4 | API Delete, Console | Immediate | On request | European provider |

**Reference Table 2: Deletion SLA Best Practices (Rows 67-77)**

| Data Sensitivity | Recommended SLA | Rationale |
|------------------|----------------|-----------|
| Restricted (e.g., health, financial) | ≤7 days | High sensitivity, regulatory risk |
| Confidential | ≤30 days | GDPR default timeframe |
| Internal | ≤60 days | Business data, moderate sensitivity |
| Public | ≤90 days | Low sensitivity, operational flexibility |

**Reference Table 3: Cloud Provider Contract Checklist (Rows 79-92)**

| Contract Element | Description | Compliance Check |
|------------------|-------------|------------------|
| Deletion Obligation | Explicit requirement to delete data on request | ✅ or ❌ |
| Deletion Timeline | Specific number of days (e.g., 30 days) | Specify days |
| Deletion Method | How deletion is performed (API, manual, etc.) | Document method |
| Certificate of Deletion | Provider confirmation of deletion | Available? |
| Subprocessor Notification | Advance notice of subprocessor changes | Required? |
| Audit Rights | Right to audit deletion compliance | Yes/No |
| Data Return Option | Alternative to deletion - return data copy | Available? |
| Multi-Region Deletion | Deletion across all geographic regions | Verified? |
| Backup Deletion | Deletion from backup systems | Covered? |
| Breach Notification | Provider must notify of deletion failures | Required? |

**Exception/Deviation Block (Rows 95-100):**
- Providers without DPA (justify or remediate)
- Providers with >90 day deletion SLA (GDPR concern)
- Tier 9/10 providers (Shadow IT - urgent remediation)

---

### Sheet 3: SaaS Application Deletion

**Purpose:** Assess deletion procedures for SaaS applications (CRM, HR, marketing, collaboration)

**Assessment Question:**
*"Can we effectively delete data from all SaaS applications, including obtaining confirmation and managing data export if needed?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.4, Section 2.4.2 (SaaS Application Deletion)

**Column Structure:** A-U (21 columns total)
- Columns A-Q: Standard base columns
- Column R: Admin Portal Access
- Column S: Data Export Available
- Column T: Deletion Request Method
- Column U: GDPR DPA Signed

**Data Entry Rows:** 13 rows (yellow-highlighted)

**Compliance Checklist (Rows 25-45):**

1. All SaaS applications in use are identified and documented
2. Business owners assigned for each SaaS application
3. Data Processing Agreement (DPA) signed for SaaS handling personal data
4. DPA includes deletion obligations and timeline
5. Admin portal access verified (ability to manage data)
6. Data export capability tested (before deletion if needed)
7. Deletion request method documented (self-service, ticket, etc.)
8. Deletion confirmation process exists
9. User account deletion vs. data deletion distinguished
10. Shared account deletion procedures documented
11. Integration data deletion addressed (APIs, webhooks)
12. Backup/archive deletion coordinated
13. Shadow SaaS applications investigated and remediated
14. Annual SaaS inventory review conducted
15. GDPR data subject request procedures cover SaaS platforms

**Reference Table 1: Common SaaS Categories and Deletion Methods (Rows 47-68)**

| SaaS Category | Example Providers | Typical Deletion Method | Data Export | Notes |
|---------------|-------------------|------------------------|-------------|-------|
| CRM | Salesforce, HubSpot, Pipedrive | Admin portal delete | ✅ API/CSV | Record-level deletion |
| HR/Payroll | Workday, ADP, BambooHR | Admin portal + ticket | ✅ CSV/API | Retention requirements |
| Marketing Automation | Marketo, Mailchimp, Braze | Admin portal delete | ✅ API/CSV | List/contact deletion |
| Collaboration | Slack, Teams, Zoom | Admin console | ⚠️ Limited | Channel/meeting deletion |
| File Sharing | Dropbox, Box, Google Drive | Admin console delete | ✅ Download | File-level deletion |
| Project Management | Jira, Asana, Monday.com | Admin delete | ✅ Export | Project/task deletion |
| Analytics | Google Analytics, Mixpanel | Admin delete | ⚠️ Limited | Data retention settings |
| Customer Support | Zendesk, Intercom, Freshdesk | Admin delete | ✅ API/CSV | Ticket/conversation deletion |
| Identity/SSO | Okta, Auth0, Azure AD | Admin delete | ✅ API | User deletion |
| Accounting | QuickBooks, Xero, NetSuite | Admin + ticket | ✅ Export | Legal retention applies |

**Reference Table 2: SaaS Deletion Challenges (Rows 70-82)**

| Challenge | Description | Mitigation |
|-----------|-------------|------------|
| User Deletion ≠ Data Deletion | Deleting user account may not delete their data | Request data deletion explicitly |
| Shared Data | Data shared with other users/orgs | Coordinate with data owners |
| Integration Data | Data synced to other systems via API | Delete from all integrated systems |
| Backup Retention | SaaS backups may retain data longer | Confirm backup deletion timeline |
| No Self-Service Deletion | Must contact support/account manager | Document request process, SLA |
| No Data Export | Cannot export before deletion | Accept permanent loss or negotiate |
| Free/Freemium Accounts | No contract, limited support | Upgrade or migrate to contracted service |
| Shadow IT | Unknown SaaS usage | Discovery tools, policy enforcement |

**Reference Table 3: GDPR DPA Requirements for SaaS (Rows 84-95)**

| DPA Requirement | Why It Matters | Verification |
|-----------------|----------------|--------------|
| Processor Obligations (Art. 28) | SaaS is data processor, needs DPA | DPA signed? |
| Deletion on Request | Must delete when requested | Clause present? |
| Deletion Timeline | Should specify days (e.g., 30) | Timeline specified? |
| Assistance with DSR | Help with data subject deletion requests | Clause present? |
| Subprocessor Notification | SaaS may use sub-processors | Notification process? |
| Data Location | Where data is stored/processed | Documented? |
| Security Measures | Encryption, access controls | Documented? |
| Audit Rights | Right to audit deletion compliance | Clause present? |
| Breach Notification | Must notify of data breaches | Required timeline? |
| Data Return or Deletion | At end of service | Options documented? |

**Exception/Deviation Block (Rows 98-103):**
- SaaS without DPA (high risk - remediate or exit)
- SaaS without deletion capability (document risk, exit strategy)
- Shadow SaaS discovered (immediate remediation)

---

### Sheet 4: Vendor Contract Review

**Purpose:** Assess contractual deletion obligations across all third-party vendors

**Assessment Question:**
*"Do all vendor contracts include appropriate deletion clauses, SLAs, and audit rights to ensure data deletion compliance?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.4, Section 2.4.3 (Vendor Contract Requirements)

**Column Structure:** A-U (21 columns total)
- Columns A-Q: Standard base columns
- Column R: Deletion Clause Present
- Column S: Deletion Timeline Specified
- Column T: Certificate of Deletion
- Column U: Audit Rights

**Data Entry Rows:** 13 rows (yellow-highlighted)

**Compliance Checklist (Rows 25-45):**

1. All vendor contracts reviewed for deletion clauses
2. Deletion clause specificity assessed (specific vs. generic)
3. Deletion timeline explicitly stated (not just "reasonable time")
4. Certificate of Deletion either required or available on request
5. Audit rights include ability to verify deletion compliance
6. Subprocessor usage disclosed and governed
7. Data return option available as alternative to deletion
8. Contract renewal triggers deletion clause review
9. New vendor onboarding includes deletion clause requirement
10. Vendor contract template updated with deletion requirements
11. Legal/Procurement engaged for contract negotiations
12. High-risk vendors (Tier 1-3, Restricted data) have strongest clauses
13. Contract breach remedies include deletion failures
14. Vendor due diligence includes deletion capability assessment
15. Contracts reviewed at least every 3 years

**Reference Table 1: Deletion Clause Strength Assessment (Rows 47-60)**

| Clause Type | Example Language | Strength | Recommended For |
|-------------|------------------|----------|-----------------|
| **Strong (Specific)** | "Vendor shall delete all Customer Data within 30 days of termination or upon written request, and provide written certification of deletion within 5 business days." | ✅ Excellent | Tier 1-3, Restricted data |
| **Moderate (Generic with Timeline)** | "Upon termination, Vendor will delete Customer Data within a reasonable time not to exceed 90 days." | ⚠️ Acceptable | Tier 4-6, Confidential data |
| **Weak (Generic)** | "Vendor will handle data in accordance with applicable law." | ❌ Insufficient | Not recommended |
| **Absent** | No deletion clause | ❌ Non-Compliant | Requires amendment |

**Reference Table 2: Certificate of Deletion Best Practices (Rows 62-73)**

| Element | Description | Example |
|---------|-------------|---------|
| Date of Deletion | When deletion was executed | "Deleted on: 2025-12-15" |
| Scope of Deletion | What was deleted | "All customer records for Company X" |
| Deletion Method | How deletion was performed | "Secure deletion per NIST SP 800-88" |
| Systems Affected | Which systems/databases | "Production DB, backup servers, archives" |
| Verification | How deletion was verified | "Forensic verification completed" |
| Authorized Signatory | Who certifies deletion | "Signed by: Data Protection Officer" |
| Exceptions | Any data retained (with reason) | "Tax records retained per law" |
| Certificate Date | When certificate was issued | "Certified on: 2025-12-20" |

**Reference Table 3: Audit Rights Clauses (Rows 75-86)**

| Audit Right Type | Description | When to Require |
|------------------|-------------|-----------------|
| **Deletion Audit** | Right to verify deletion completion | High-value vendors, Restricted data |
| **General Audit** | Broader audit including deletion | All Tier 1-3 vendors |
| **Self-Certification** | Vendor certifies compliance | Tier 4-6 vendors, lower risk |
| **Third-Party Audit** | Independent auditor verifies | Critical vendors, regulatory requirement |
| **On-Demand Audit** | Can audit at any time | High-risk scenarios |
| **Scheduled Audit** | Annual or periodic audits | Standard vendors |
| **Audit Report Rights** | Right to receive SOC 2, ISO certs | All vendors handling personal data |

**Reference Table 4: Contract Amendment Triggers (Rows 88-98)**

| Trigger Event | Action Required | Timeline |
|---------------|-----------------|----------|
| New GDPR/FADP Requirement | Amend contract to include | Within 6 months |
| Vendor Subprocessor Change | Review subprocessor deletion obligations | Before change effective |
| Data Breach at Vendor | Review and strengthen deletion clauses | Within 3 months |
| Vendor Acquisition/Merger | Re-assess deletion capabilities | Before merger closes |
| Service Upgrade (More Sensitive Data) | Strengthen deletion requirements | Before upgrade |
| Contract Renewal | Full deletion clause review | During renewal process |
| Regulatory Audit Finding | Address gaps in contract | Per audit timeline |

**Exception/Deviation Block (Rows 101-106):**
- Contracts without deletion clauses (amendment required)
- Legacy contracts pre-dating GDPR (renewal or amendment needed)
- Vendors refusing deletion clause (risk acceptance or exit)

---

### Sheet 5: Subprocessor Mapping

**Purpose:** Map data flow through vendor subprocessor chains and assess deletion coordination

**Assessment Question:**
*"Do we know all subprocessors in our vendor supply chain, and can we coordinate deletion across the entire chain?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.4, Section 2.4.4 (Subprocessor Management)

**Column Structure:** A-U (21 columns total)
- Columns A-Q: Standard base columns (Vendor Name in Column A)
- Column R: Subprocessor Count
- Column S: Subprocessor List Current
- Column T: Deletion Flow Documented
- Column U: Subprocessor Deletion SLA

**Data Entry Rows:** 13 rows (yellow-highlighted)

**Compliance Checklist (Rows 25-45):**

1. All primary vendors (processors) identified
2. Subprocessor disclosure obtained from each vendor
3. Subprocessor count documented and current
4. Subprocessor list reviewed at least annually
5. Vendor contractually obligated to notify of subprocessor changes
6. Data flow diagram created for critical data categories
7. Deletion flow documented (prime vendor → subprocessor deletion)
8. Subprocessor deletion SLA understood (covered by prime or separate)
9. Subprocessor DPAs flow down from prime vendor
10. High-risk subprocessors identified (non-EU, Tier 9/10)
11. Subprocessor changes trigger risk assessment
12. Deletion requests explicitly include subprocessor deletion
13. Certificate of Deletion covers subprocessor deletion
14. Multi-tier subprocessing mapped (sub-subprocessors)
15. Shadow subprocessors investigated (undisclosed usage)

**Reference Table 1: Common Subprocessor Categories (Rows 47-62)**

| Primary Vendor Type | Common Subprocessors | Deletion Coordination |
|---------------------|---------------------|----------------------|
| **Cloud Provider** | CDN (Cloudflare, Akamai), Monitoring (Datadog), Logging (Splunk) | Via prime vendor APIs |
| **SaaS CRM** | Email delivery (SendGrid), Analytics (Segment), Payment (Stripe) | Prime vendor coordinates |
| **HR/Payroll** | Background check vendors, Benefits administrators, Tax filing services | Often manual coordination |
| **Marketing Platform** | Email providers, SMS gateways, Ad networks | API or dashboard deletion |
| **File Sharing** | Preview generation, Virus scanning, OCR services | Automatic via prime vendor |
| **Customer Support** | Chatbots (Intercom), Knowledge base, Voice transcription | Prime vendor deletion |
| **Analytics** | Data warehouses, BI tools, ML platforms | Manual export-delete workflow |

**Reference Table 2: Deletion Flow Documentation Methods (Rows 64-75)**

| Method | Description | Best For |
|--------|-------------|----------|
| **Flowchart** | Visual diagram of deletion propagation | Complex multi-tier relationships |
| **Table/Matrix** | Prime vendor → Subprocessors → Deletion method | Simple linear relationships |
| **Narrative Description** | Text explanation of deletion process | Simple single-tier relationships |
| **API Documentation** | Technical specs for deletion APIs | Developer-focused documentation |
| **Runbook** | Step-by-step deletion procedure | Operational teams |

**Reference Table 3: Subprocessor Risk Assessment (Rows 77-88)**

| Risk Factor | High Risk | Medium Risk | Low Risk |
|-------------|-----------|-------------|----------|
| **Data Sensitivity** | Restricted (health, financial) | Confidential | Internal, Public |
| **Subprocessor Location** | Non-EU, sanctioned countries | US (Privacy Shield concerns) | EU/EEA, Switzerland |
| **Deletion Capability** | Unknown, no deletion API | Manual process only | Automated deletion API |
| **Subprocessor Tier** | Tier 9-10 (unknown, shadow) | Tier 4-8 (verified but lower tier) | Tier 1-3 (established) |
| **DPA Coverage** | Not covered by prime DPA | Generic coverage | Specific DPA for subprocessor |
| **Notification Process** | No notification of changes | Notification after fact | Advance notification + approval |

**Reference Table 4: GDPR Article 28(2) - Subprocessor Requirements (Rows 90-100)**

| Requirement | Description | Verification |
|-------------|-------------|--------------|
| Prior Authorization | Controller must authorize subprocessors | Authorized in contract? |
| General or Specific | General authorization or case-by-case | Type documented? |
| Notification of Changes | Processor must inform of subprocessor changes | Notification process? |
| Objection Rights | Controller can object to new subprocessors | Objection clause present? |
| Same Obligations | Subprocessors bound by same DPA obligations | Flow-down confirmed? |
| Prime Liability | Prime processor liable for subprocessor | Liability clause present? |

**Exception/Deviation Block (Rows 103-108):**
- Vendors with unknown subprocessor count (discovery required)
- Vendors with >10 subprocessors (detailed mapping needed)
- Subprocessors in high-risk jurisdictions (risk assessment + exit strategy)

---

### Sheet 6: Vendor Performance Tracking

**Purpose:** Track actual deletion performance, certificates received, and incidents

**Assessment Question:**
*"Are vendors meeting their deletion SLAs, providing certificates when required, and is performance monitored over time?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.4, Section 2.4.5 (Vendor Performance Monitoring)

**Column Structure:** A-U (21 columns total)
- Columns A-Q: Standard base columns
- Column R: Deletion Requests (Last 12M)
- Column S: Average Response Time (Days)
- Column T: Certificates Received
- Column U: Incidents / Failures

**Data Entry Rows:** 13 rows (yellow-highlighted)

**Compliance Checklist (Rows 25-45):**

1. Deletion request log maintained for all vendors
2. Response time tracked per vendor
3. SLA compliance calculated (actual vs. contracted)
4. Certificate of Deletion requested for high-value deletions
5. Certificate completeness reviewed (includes scope, date, method)
6. Deletion incidents documented and investigated
7. Root cause analysis performed for failed deletions
8. Vendor escalation procedures exist for SLA breaches
9. Quarterly vendor performance review conducted
10. Underperforming vendors identified and remediated
11. Performance metrics reported to management
12. Vendor scorecard includes deletion performance
13. Contract renewal considers deletion performance history
14. Best-performing vendors identified for benchmarking
15. Performance data feeds into vendor risk assessment

**Reference Table 1: Deletion Performance Metrics (Rows 47-58)**

| Metric | Calculation | Target | Use Case |
|--------|-------------|--------|----------|
| **High-Risk Vendor Response Time** | Avg days for Tier 1/critical vendors | ≤ 50% of standard SLA | Prioritization effectiveness |
| **Verification Rate** | (Deletions verified / Total deletions) × 100% | 100% | Actual deletion confirmation |
| **Backlog Age** | Oldest unresolved request in days | ≤ 30 days | Process blockage detection |
| **Vendor Non-Response Rate** | (No response after X days / Total) × 100% | < 2% | Vendor relationship quality |
| **Certificate Quality Score** | Manual audit of certificate completeness | ≥ 90% valid | Vendor compliance rigor |

**Reference Table 2: Certificate of Deletion Quality Checklist (Rows 60-72)**

| Quality Element | Check | Pass/Fail |
|-----------------|-------|-----------|
| Date of Deletion | Specific date provided (not date range) | ✅ / ❌ |
| Scope Clarity | Exactly what data was deleted | ✅ / ❌ |
| Deletion Method | Method documented (e.g., "Secure erase") | ✅ / ❌ |
| Systems Listed | All affected systems identified | ✅ / ❌ |
| Verification Method | How deletion was verified | ✅ / ❌ |
| Authorized Signature | Signed by DPO or authorized person | ✅ / ❌ |
| Company Letterhead | Official vendor document | ✅ / ❌ |
| Reference Number | Traceable certificate ID | ✅ / ❌ |
| Exceptions Noted | Any retained data explained | ✅ / ❌ |
| Contact Information | For follow-up questions | ✅ / ❌ |

**Reference Table 3: Deletion Incident Categories (Rows 74-85)**

| Incident Type | Description | Severity | Remediation |
|---------------|-------------|----------|-------------|
| **SLA Breach** | Deletion exceeded contracted timeline | Medium-High | Escalate, track for pattern |
| **Incomplete Deletion** | Some data retained unintentionally | High | Re-request, verify completion |
| **No Certificate** | Certificate not provided when required | Medium | Request, document for scorecard |
| **Subprocessor Failure** | Prime deleted, subprocessor did not | Critical | Escalate to prime, audit |
| **Multi-Region Miss** | Deleted in one region, not all | Critical | Re-request, verify all regions |
| **Backup Retention** | Active data deleted, backup retained | Medium-High | Request backup purge |
| **Failed Verification** | Forensic test shows data still present | Critical | Escalate, re-delete, audit |
| **Vendor Refusal** | Vendor refuses deletion request | Critical | Legal escalation, exit strategy |

**Reference Table 4: Vendor Performance Scorecard Example (Rows 87-98)**

| Vendor Name | Tier | Requests (12M) | Avg Response (Days) | SLA | SLA Compliance | Incidents | Score |
|-------------|------|----------------|---------------------|-----|----------------|-----------|-------|
| AWS | Tier 1 | 15 | 1.2 | ≤3 | 100% | 0 | 🟢 Excellent |
| Salesforce | Tier 2 | 8 | 5.5 | ≤7 | 100% | 0 | 🟢 Excellent |
| VendorX | Tier 3 | 3 | 45 | ≤30 | 67% | 1 | 🟡 Needs Improvement |
| VendorY | Tier 4 | 2 | 95 | ≤60 | 50% | 2 | 🔴 Critical |

**Scoring:** 🟢 = 90-100%, 🟡 = 70-89%, 🔴 = <70% SLA compliance

**Exception/Deviation Block (Rows 101-106):**
- Vendors with 0 deletion requests in 12 months (may be inactive - review)
- Vendors with >3 incidents (high risk - remediation or exit)
- Vendors with <80% SLA compliance (contract breach - escalate)

---

### Sheet 7: Summary Dashboard

**Purpose:** Provide executive-level overview of third-party deletion compliance and vendor risk

**Dashboard Structure:**

**Section 1: Overall Compliance Summary (Rows 3-12)**

| Assessment Area | Total Items | Compliant | Partial | Non-Compliant | Compliance % |
|-----------------|-------------|-----------|---------|---------------|--------------|
| Cloud Provider Assessment | [COUNT] | [COUNTIF] | [COUNTIF] | [COUNTIF] | [%] |
| SaaS Application Deletion | [COUNT] | [COUNTIF] | [COUNTIF] | [COUNTIF] | [%] |
| Vendor Contract Review | [COUNT] | [COUNTIF] | [COUNTIF] | [COUNTIF] | [%] |
| Subprocessor Mapping | [COUNT] | [COUNTIF] | [COUNTIF] | [COUNTIF] | [%] |
| Vendor Performance Tracking | [COUNT] | [COUNTIF] | [COUNTIF] | [COUNTIF] | [%] |
| **OVERALL A.8.10.3** | [SUM] | [SUM] | [SUM] | [SUM] | [Overall %] |

**Compliance Thresholds:**
- ≥ 90% Compliant = 🟢 Excellent
- 70-89% Compliant = 🟡 Needs Improvement
- < 70% Compliant = 🔴 Critical Attention Required

**Section 2: Critical Vendor Risks (Rows 15-25)**

Auto-populated from all assessment sheets where:
- Status = "❌ Non-Compliant" AND (Risk Level = "Critical" OR Provider Tier = "Tier 1-3")

| Vendor Name | Tier | Gap Description | Risk Level | Remediation Plan |
|-------------|------|-----------------|------------|------------------|
| [Auto-populated from Sheets 2-6] | | | | |

**Section 3: Vendor Tier Distribution (Rows 28-38)**

| Provider Tier | Count | % of Total | Avg Compliance % | Status |
|---------------|-------|-----------|------------------|--------|
| Tier 1 (Hyperscaler) | [COUNT] | [%] | [AVG compliance] | [Status] |
| Tier 2 (Major Provider) | [COUNT] | [%] | [AVG compliance] | [Status] |
| Tier 3 (Significant) | [COUNT] | [%] | [AVG compliance] | [Status] |
| Tier 4-8 (Standard-Legacy) | [COUNT] | [%] | [AVG compliance] | [Status] |
| Tier 9 (Shadow IT) | [COUNT] | [%] | [AVG compliance] | 🔴 Critical! |
| Tier 10 (Unknown) | [COUNT] | [%] | [AVG compliance] | 🔴 Critical! |

**Section 4: Contract Compliance Metrics (Rows 41-49)**

| Metric | Count/Percentage | Target | Status |
|--------|------------------|--------|--------|
| Vendors with DPA Signed | [COUNT] | 100% (personal data) | [Status] |
| Vendors with Deletion Clause | [COUNT] | 100% | [Status] |
| Vendors with Specific SLA | [COUNT] | ≥80% | [Status] |
| Vendors with Certificate Provision | [COUNT] | 100% (Tier 1-3) | [Status] |
| Vendors with Audit Rights | [COUNT] | ≥70% | [Status] |
| Contracts Reviewed (Last 12M) | [COUNT] | 100% (annual) | [Status] |

**Section 5: Subprocessor Risk Assessment (Rows 52-60)**

| Metric | Value | Notes |
|--------|-------|-------|
| Total Vendors with Subprocessors | [COUNT] | From Sheet 5 |
| Total Subprocessor Count | [SUM] | Across all vendors |
| Vendors with Unknown Subprocessor Count | [COUNT] | High risk |
| Vendors with >10 Subprocessors | [COUNT] | Complex data flow |
| High-Risk Subprocessors (Non-EU) | [COUNT] | GDPR concern |
| Deletion Flow Documented | [COUNT/Total %] | Target: 100% Tier 1-3 |

**Section 6: Deletion Performance Summary (Rows 63-72)**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Deletion Requests (12M) | [SUM from Sheet 6] | N/A | ℹ️ Info |
| Average Response Time (All Vendors) | [AVERAGE] | ≤30 days | [Status] |
| SLA Compliance Rate | [Calculate %] | ≥95% | [Status] |
| Certificates Received | [SUM] | 100% (required) | [Status] |
| Deletion Incidents | [SUM] | 0 | [Status] |
| Vendors with >3 Incidents | [COUNT] | 0 | [Status] |

**Section 7: Shadow IT & Discovery (Rows 75-82)**

| Metric | Count | Risk Level | Action Required |
|--------|-------|------------|-----------------|
| Tier 9 Vendors (Departmental/Shadow) | [COUNT] | High | Immediate review |
| Tier 10 Vendors (Unknown) | [COUNT] | Critical | Urgent discovery |
| Vendors without DPA | [COUNT] | High | Contract amendment |
| Vendors Discovered in Last Quarter | [COUNT] | N/A | Onboarding process |

**Section 8: Executive Summary & Recommendations (Rows 85-105)**

**Text block (manually updated by assessor):**

**Overall A.8.10.3 Maturity Level:** [Emerging / Developing / Established / Optimized]

**Key Strengths:**
1. [Example: All Tier 1-3 cloud providers have DPAs with specific deletion SLAs]
2. [Example: 95% SLA compliance rate across all vendors]
3. [Example: Comprehensive subprocessor mapping for critical data flows]

**Critical Improvement Areas:**
1. [Example: 5 Tier 9/10 vendors discovered (Shadow IT) - no deletion clauses]
2. [Example: 30% of SaaS vendors lack Certificate of Deletion provision]
3. [Example: 3 vendors with >10 subprocessors - deletion flow not documented]

**Top 3 Recommendations:**
1. [Priority 1: Remediate Tier 9/10 Shadow IT vendors within 60 days]
2. [Priority 2: Amend contracts to require Certificate of Deletion for Tier 1-3]
3. [Priority 3: Map deletion flows for all vendors with >5 subprocessors]

**Next Review Date:** [Date, typically annual]

---

### Sheet 8: Evidence Register

**Purpose:** Central repository for linking evidence to assessment findings

**Structure:** 100 pre-formatted rows for evidence tracking

**Column Layout:**

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Evidence ID | 12 | Text | Unique identifier (e.g., A810.3-001) |
| B | Assessment Sheet | 20 | Dropdown | Which sheet references this evidence |
| C | Related Vendor/Provider | 30 | Text | What this evidence supports |
| D | Evidence Type | 20 | Dropdown | Type of evidence |
| E | Evidence Title/Description | 35 | Text | Brief description |
| F | File Location/Link | 40 | Text | Network path, URL, or physical location |
| G | Date Created/Collected | 12 | Date | When evidence was generated |
| H | Retention Period | 15 | Dropdown | How long to keep evidence |
| I | Next Review Date | 12 | Date | When to re-validate |
| J | Owner/Custodian | 20 | Text | Person responsible |
| K | Notes | 30 | Text | Additional context |

**Evidence Type Dropdown Options:**
- Data Processing Agreement (DPA)
- Vendor Contract
- Deletion Clause Extract
- Certificate of Deletion
- Email Correspondence
- Subprocessor List
- Deletion Request Log
- Performance Report
- Audit Report
- Meeting Minutes
- Other

**Assessment Sheet Dropdown Options:**
- Sheet 2: Cloud Provider Assessment
- Sheet 3: SaaS Application Deletion
- Sheet 4: Vendor Contract Review
- Sheet 5: Subprocessor Mapping
- Sheet 6: Vendor Performance Tracking

**Retention Period Options:**
- Duration of vendor relationship + 7 years
- 7 years (standard contract retention)
- 10 years (critical vendors)
- Permanent (ongoing relationship)

**Pre-populated Examples (Rows 10-15):**

| Evidence ID | Sheet | Vendor | Type | Description |
|-------------|-------|--------|------|-------------|
| A810.3-001 | Sheet 2 | AWS | DPA | AWS Data Processing Addendum v4.0 signed 2024-03-15 |
| A810.3-002 | Sheet 3 | Salesforce | Certificate of Deletion | Certificate for customer data deletion - Case #12345 |
| A810.3-003 | Sheet 4 | VendorX | Contract | Master Services Agreement with deletion clause (Section 8.3) |
| A810.3-004 | Sheet 5 | Azure | Subprocessor List | Azure subprocessor list as of 2025-Q1 |
| A810.3-005 | Sheet 6 | Google Cloud | Performance Report | Q4 2025 deletion request tracking log |

---

### Sheet 9: Approval Sign-Off

**Purpose:** Three-level approval workflow for assessment completion

**Structure:**

**Section 1: Document Control (Rows 3-10)**
- Assessment Period: [Date Range]
- Workbook Version: [e.g., 1.0]
- Total Assessment Sheets Completed: [5]
- Overall Compliance %: [Link to Summary Dashboard]
- Critical Vendor Risks Identified: [Count from Summary]
- Shadow IT Vendors Discovered: [Count Tier 9/10]
- Assessment Completed By: [Name, Date]

**Section 2: Level 1 Approval - Operational (Rows 13-22)**
**Role:** Vendor Management / Procurement / IT Compliance Officer

**Approval Statement:**
*"I confirm that this assessment accurately reflects our current third-party vendor relationships, cloud provider deletion capabilities, and subprocessor mappings as of [Date]. All vendors have been reviewed, gaps identified, and remediation plans are in place."*

| Field | Value |
|-------|-------|
| Approver Name | [Text entry] |
| Title/Role | [Text entry] |
| Email | [Text entry] |
| Review Date | [Date picker] |
| Approval Status | [Dropdown: ✅ Approved, ⚠️ Approved with Conditions, ❌ Rejected] |
| Conditions/Comments | [Text area] |
| Signature | [Text: "Electronically signed"] |

**Section 3: Level 2 Approval - Legal/Compliance (Rows 25-34)**
**Role:** Data Protection Officer / General Counsel / Chief Compliance Officer

**Approval Statement:**
*"I acknowledge the findings of this A.8.10.3 assessment from a legal and compliance perspective. Vendor contracts meet GDPR Article 28 requirements (or remediation is planned). Critical vendor risks, particularly Shadow IT (Tier 9/10), require immediate executive attention."*

| Field | Value |
|-------|-------|
| Approver Name | [Text entry] |
| Title/Role | [Text entry] |
| Email | [Text entry] |
| Review Date | [Date picker] |
| Approval Status | [Dropdown: ✅ Approved, ⚠️ Approved with Conditions, ❌ Rejected] |
| Conditions/Comments | [Text area] |
| Signature | [Text: "Electronically signed"] |

**Section 4: Level 3 Approval - Executive (Rows 37-46)**
**Role:** Chief Information Officer / Chief Risk Officer / Chief Procurement Officer

**Approval Statement:**
*"This assessment has been reviewed at the executive level. The organization's third-party deletion posture is [Acceptable/Needs Improvement/Unacceptable]. The Board/Executive Team has been briefed on vendor risks, particularly: (1) Shadow IT vendors, (2) Vendors without deletion clauses, (3) Subprocessor complexity."*

| Field | Value |
|-------|-------|
| Approver Name | [Text entry] |
| Title/Role | [Text entry] |
| Email | [Text entry] |
| Review Date | [Date picker] |
| Approval Status | [Dropdown: ✅ Approved, ⚠️ Approved with Conditions, ❌ Rejected] |
| Executive Summary | [Text area for key points communicated to Board] |
| Signature | [Text: "Electronically signed"] |

**Section 5: Next Steps (Rows 49-58)**

| Action Item | Responsible Party | Due Date | Status |
|-------------|-------------------|----------|--------|
| Remediate Tier 9/10 Shadow IT vendors | [Name] | [Date] | [Pending/In Progress/Complete] |
| Amend contracts for vendors without deletion clauses | [Name] | [Date] | [Pending] |
| Map deletion flows for complex subprocessor chains | [Name] | [Date] | [Pending] |
| Implement vendor deletion performance dashboard | [Name] | [Date] | [Pending] |
| Annual re-assessment of A.8.10.3 | [Name] | [Date + 1 year] | [Scheduled] |

**Section 6: Audit Trail (Rows 61-70)**

| Date | Version | Change Description | Changed By |
|------|---------|-------------------|------------|
| [Auto] | 1.0 | Initial assessment completed | [Auto-populate] |
| [Entry] | 1.1 | [Example: Added 3 newly discovered SaaS vendors] | [Name] |
| [Entry] | 1.2 | [Example: Updated AWS DPA to version 5.0] | [Name] |

---

## Summary Dashboard - Calculation Notes

### Formula Guidelines

**Compliance Percentage Calculation:**
```
= COUNTIF(SheetX!F:F,"✅ Compliant") / (COUNTA(SheetX!F:F) - 9)
```

**Vendor Tier Distribution:**
```
= COUNTIF(Sheet2!E:E,"Tier 1")
```

**Shadow IT Detection (Critical!):**
```
= COUNTIF(Sheet2!E:E,"Tier 9") + COUNTIF(Sheet2!E:E,"Tier 10")
```
*If count > 0, flag as CRITICAL GAP requiring immediate remediation*

**Average SLA Compliance:**
```
= (Vendors meeting SLA / Total vendors) × 100%
```

---

## Workbook Metadata

**File Naming Convention:**
`ISMS-IMP-A.8.10.3_Third_Party_Cloud_Deletion_{YYYYMMDD}.xlsx`

**Sheet Tab Colors:**
- Instructions: Blue (#4472C4)
- Assessment Sheets (2-6): Green (#70AD47)
- Summary Dashboard: Orange (#FFC000)
- Evidence Register: Gray (#A6A6A6)
- Approval Sign-Off: Purple (#7030A0)

**Default Sheet Protections:**
- Headers (Rows 1-9): Protected, locked
- Data entry cells (Yellow): Unprotected, editable
- Formula cells: Protected, locked
- Evidence Register: Fully editable
- Approval Sign-Off: Fully editable

---

## Implementation Notes

### For Script Generator (generate_a810_3_third_party_cloud.py)

**Key Parameters:**
- Total Sheets: 9
- Data Entry Rows per Assessment Sheet: 13 (yellow-highlighted)
- Evidence Register Rows: 100
- Base Columns: A-Q (17 columns)
- Extended Columns: R-U (4 additional columns per sheet)

**Reusable Components from A.8.10.1 and A.8.10.2:**
- Style definitions (header, subheader, input_cell, status colors)
- Data validation creator
- Evidence Register generator (identical structure)
- Approval Sign-Off generator (identical structure)
- Freeze panes logic

**A.8.10.3-Specific Components:**
- Provider Tier dropdown (Tier 1-10 from ISMS-REF-A.5.23)
- GDPR DPA requirement tracking
- Subprocessor count and mapping
- Certificate of Deletion tracking
- Vendor performance metrics (requests, response time, incidents)
- Shadow IT detection (Tier 9/10 flagging)

**Critical Integration:**
- Provider Tier dropdown MUST reference ISMS-REF-A.5.23 classifications
- Instructions sheet MUST explain tier system and reference full registry
- Dashboard MUST flag Tier 9/10 (Shadow IT) as critical

---

## Quality Assurance Checklist

**Before Delivery:**
- [ ] All 9 sheets present and correctly named
- [ ] GDPR Article 28 requirements explained in Instructions
- [ ] Provider Tier dropdown (Tier 1-10) working correctly
- [ ] Shadow IT detection formula working (Tier 9/10 count)
- [ ] Cloud provider examples reference ISMS-REF-A.5.23
- [ ] Data validations working (test all dropdowns)
- [ ] Formulas in Summary Dashboard calculating correctly
- [ ] Yellow highlighting on all data entry cells
- [ ] Freeze panes active on assessment sheets
- [ ] Evidence Register has 100 rows
- [ ] Approval Sign-Off has 3-level workflow
- [ ] File size < 5 MB
- [ ] Vendor-neutral language (no locked-in vendors)

---

**END OF SPECIFICATION**

**Related Documents:**
- ISMS-POL-A.8.10-S2.4 (Third-Party & Cloud Deletion Policy)
- ISMS-REF-A.5.23 (Cloud Service Provider Registry - 68 providers, 10 tiers)
- ISMS-IMP-A.8.10.1 (Retention Triggers) - Completed
- ISMS-IMP-A.8.10.2 (Deletion Methods) - Completed
- ISMS-IMP-A.8.10.4 (Verification & Evidence) - Next in sequence
- GDPR Article 28 (Processor Obligations)

**Version:** 1.0  
**Date:** [Approval Date] 
**Status:** Ready for Python Generator Implementation