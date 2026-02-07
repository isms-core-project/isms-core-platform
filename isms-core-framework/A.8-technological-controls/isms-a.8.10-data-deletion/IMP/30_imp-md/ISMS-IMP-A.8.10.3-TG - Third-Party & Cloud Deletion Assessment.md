**ISMS-IMP-A.8.10.3-TG - Third-Party & Cloud Deletion Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.10.3-TG |
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

# Technical Specification
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

<!-- QA_VERIFIED: 2026-02-06 -->
