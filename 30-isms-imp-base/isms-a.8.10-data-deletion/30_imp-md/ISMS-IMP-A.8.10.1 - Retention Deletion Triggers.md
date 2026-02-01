**ISMS-IMP-A.8.10.1 - Retention & Deletion Triggers Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.10.1 |
| **Version** | 1.0 |
| **Assessment Area** | Data Retention Schedules & Deletion Triggers |
| **Related Policy** | ISMS-POL-A.8.10, Section 2.1 (Retention & Deletion Triggers) |
| **Purpose** | Assess organizational compliance with data retention requirements and deletion trigger mechanisms across all data categories |
| **Target Audience** | Data Protection Officers, Privacy Officers, Information Security Managers, Records Managers, Compliance Officers, IT Operations, Legal Counsel, Auditors |
| **Assessment Type** | Process & Operational Compliance |
| **Review Cycle** | Annual (minimum) or After Regulatory Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Retention & Deletion Triggers assessment workbook | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** Data Protection Officers, Privacy Officers, Legal Counsel, Records Managers, Compliance Officers

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organization]'s implementation of **data retention schedules and deletion trigger mechanisms** to ensure compliance with ISO/IEC 27001:2022 Control A.8.10, applicable data protection regulations (GDPR, FADP), and industry-specific retention requirements.

**Scope:** Complete data lifecycle management across 5 critical areas:

1. **Data Category Registry** - Complete inventory of all data types processed by [Organization]
2. **Retention Schedule Compliance** - Legal/regulatory alignment for each data category
3. **Deletion Trigger Configuration** - Automated and manual deletion mechanisms
4. **Legal Hold Management** - Procedures to suspend deletion when legally required
5. **Data Subject Rights** - GDPR Article 17 / FADP erasure request handling

**Assessment Output:** Excel workbook with ~150-250 data points documenting current retention posture, regulatory compliance status, deletion trigger effectiveness, and remediation plans for identified gaps.

## Why This Matters

**ISO 27001:2022 Control A.8.10 Requirement:**
> *"Information stored in information systems, devices or in any other storage media should be deleted when no longer required."*

**Regulatory Context:**

- **EU GDPR (Article 5.1.e):** "Storage limitation" principle - personal data must be kept only as long as necessary
- **EU GDPR (Article 17):** "Right to erasure" - data subjects can request deletion of their personal data
- **Swiss FADP (Article 6):** Purpose limitation and proportionality - data retention must be justified
- **Swiss Code of Obligations (OR):** Business records retention (typically 10 years for accounting documents)
- **Industry-Specific:** Financial services, healthcare, telecommunications often have sector-specific retention mandates


**Business Impact:**

- **Regulatory Fines:** GDPR violations can result in fines up to €20M or 4% of annual global turnover
- **Storage Costs:** Unnecessary data retention increases infrastructure costs (cloud storage, backup systems)
- **Data Breach Risk:** Retained data no longer needed = increased attack surface and breach liability
- **Operational Efficiency:** Clear retention schedules reduce ambiguity and enable systematic cleanup
- **Audit Readiness:** Documented retention schedules are fundamental to ISO 27001, GDPR, and financial audits


## Who Should Complete This Assessment

**Primary Responsibility:** Data Protection Officer (DPO) / Privacy Officer

**Required Knowledge:**

- [Organization]'s complete data inventory and classification scheme
- Applicable legal and regulatory retention requirements
- Data subject rights procedures (GDPR Article 17, FADP)
- IT systems and storage locations for each data category
- Business processes that generate, process, and retain data


**Support Roles:**

- **Legal Counsel:** For retention period justification and legal hold procedures
- **Records Managers:** For retention schedule design and implementation
- **IT Operations:** For technical deletion trigger implementation
- **Business Unit Owners:** For data category identification and business purpose validation
- **Compliance Team:** For regulatory requirement mapping
- **Information Security:** For deletion verification and evidence collection


## Time Estimate

**Total Assessment Time:** 8-12 hours (depending on data complexity and organizational size)

**Breakdown:**

- **Data Category Inventory (2-3 hours):** Identify and document all data types processed
- **Retention Schedule Review (2-3 hours):** Map legal/regulatory requirements to each category
- **Deletion Trigger Assessment (2-3 hours):** Document automated and manual deletion mechanisms
- **Legal Hold & Data Subject Rights (1-2 hours):** Review procedures and metrics
- **Evidence Collection (1-2 hours):** Gather supporting documentation
- **Quality Review (1 hour):** Final validation and approval preparation


**Pro Tip:** For complex organizations with >50 data categories, consider conducting assessment over multiple sessions (e.g., one session per business unit or system).

## Connection to Policy

This assessment implements **ISMS-POL-A.8.10, Section 2.1 (Retention & Deletion Triggers) (Retention & Deletion Triggers Requirements)** which defines mandatory requirements for:

- **Data Inventory:** All data categories must be identified and classified
- **Retention Schedules:** Every data category must have a documented retention period with legal/regulatory justification
- **Deletion Triggers:** Automated deletion mechanisms must be implemented where technically feasible
- **Legal Holds:** Procedures to suspend deletion when litigation, investigation, or audit requires data preservation
- **Data Subject Rights:** GDPR Article 17 / FADP erasure requests must be processed within regulatory timelines (typically 30 days)


**Policy Authority:** Chief Information Security Officer (CISO) / Data Protection Officer (DPO)  
**Compliance Status:** Mandatory for all data categories processing personal data or subject to regulatory retention requirements

---

# Prerequisites

## Access Required

Before starting this assessment, ensure you have access to:

**Documentation:**

- [ ] Data classification policy and current data inventory
- [ ] Existing retention schedules (if any)
- [ ] Data processing records (GDPR Article 30 / FADP Article 12)
- [ ] Data flow diagrams showing storage locations
- [ ] Legal and regulatory requirement register
- [ ] Privacy impact assessments (PIAs/DPIAs)


**Systems:**

- [ ] Data management systems (CRM, HR, ERP, etc.)
- [ ] Cloud storage administration consoles
- [ ] Backup and archive systems
- [ ] Data subject request tracking system (if implemented)
- [ ] Legal hold notification system (if implemented)


**Subject Matter Experts:**

- [ ] Legal Counsel (for retention period justification)
- [ ] Business Unit Owners (for data category identification)
- [ ] IT Operations (for deletion trigger implementation details)
- [ ] Records Manager (for retention schedule design)


## Required Knowledge

**Regulatory & Legal:**

- Understanding of GDPR Article 5.1.e (storage limitation)
- Understanding of GDPR Article 17 (right to erasure)
- Understanding of Swiss FADP Article 6 (purpose limitation)
- Familiarity with industry-specific retention requirements
- Legal hold concepts and litigation readiness


**Technical:**

- Basic understanding of database lifecycle management
- Familiarity with automated deletion mechanisms (cron jobs, lifecycle policies, retention policies)
- Understanding of backup retention vs. production data retention
- Cloud storage lifecycle management (if applicable)


**Process:**

- Data classification scheme in use at [Organization]
- Business processes that generate and consume data
- Records management principles
- Data subject rights request handling


## Pre-Assessment Checklist

Complete these tasks before beginning the assessment:

- [ ] **Gather existing retention schedules** (if any) from Legal, Compliance, or Records Management
- [ ] **Review GDPR Article 30 records** or equivalent data processing documentation
- [ ] **Identify all major data systems** (applications, databases, file shares, cloud storage)
- [ ] **Schedule meetings with Business Unit Owners** to validate data categories
- [ ] **Confirm regulatory requirements** applicable to [Organization] with Legal Counsel
- [ ] **Review any active legal holds** or litigation requirements
- [ ] **Collect metrics** on data subject erasure requests (last 12 months)
- [ ] **Document backup retention policies** to ensure alignment with production retention


**Critical:** If [Organization] has never conducted a formal data inventory or created retention schedules, allow additional time (20-30 hours) for foundational work before completing this assessment.

---

# Assessment Workflow

## Workflow Overview

```
Step 1: Data Category Inventory (Sheet 2)
   ↓
Step 2: Retention Schedule Review (Sheet 3)
   ↓
Step 3: Deletion Trigger Assessment (Sheet 4)
   ↓
Step 4: Legal Hold Procedures (Sheet 5)
   ↓
Step 5: Data Subject Rights (Sheet 6)
   ↓
Step 6: Evidence Collection (Sheet 8)
   ↓
Step 7: Review Summary Dashboard (Sheet 7)
   ↓
Step 8: Quality Check & Approval (Sheet 9)
```

## Step-by-Step Instructions

### Step 1: Data Category Inventory (Sheet 2)

**Objective:** Document every type of data processed by [Organization]

**Instructions:**
1. List all data categories in Column A (e.g., "Customer Contact Information", "Employee HR Records", "Application Logs")
2. Assign Data Classification in Column B using your classification scheme
3. Identify Business Owner in Column C (department or role responsible)
4. Document Primary Storage Location in Column R (On-Premise, Cloud, etc.)
5. Estimate Volume/Records in Column S (approximate count or size)
6. Indicate if Contains PII/SPI in Column T

**Common Data Categories to Consider:**

- Customer/Client data (CRM, sales, support tickets)
- Employee data (HR records, payroll, performance reviews)
- Financial data (invoices, contracts, accounting records)
- Operational data (application logs, monitoring data, backups)
- Marketing data (email lists, campaign analytics, website analytics)
- Legal data (contracts, NDAs, litigation files)
- Technical data (source code, documentation, system configurations)


**Quality Check:**

- Have you covered ALL systems where data is stored?
- Have you included cloud applications (SaaS)?
- Have you included backups and archives?
- Have you validated with Business Unit Owners?


### Step 2: Retention Schedule Compliance (Sheet 3)

**Objective:** Map legal/regulatory retention requirements to each data category

**Instructions:**
1. Copy data categories from Sheet 2 to Column A
2. Assign Retention Period in Column D based on legal/regulatory analysis
3. Document Legal/Regulatory Basis in Column E (e.g., "GDPR Article 6.1.c", "Swiss OR Article 958f")
4. Select Retention Calculation Method in Column R (Fixed Period, Event-Based, Hybrid)
5. If event-based, describe Event Trigger in Column S
6. Verify Backup Retention Aligned in Column T

**Common Retention Periods:**

- **30-90 days:** Application logs, temporary files, session data
- **1 year:** Marketing consent, routine business communications
- **3-7 years:** Tax-related documents, employment records (post-termination)
- **10 years:** Accounting records (Swiss OR), financial statements
- **Until Event Occurs:** Active customer accounts, ongoing contracts
- **Permanent:** Corporate governance documents, intellectual property


**Legal/Regulatory Basis Examples:**

- **GDPR Article 6.1.c:** Legal obligation (e.g., tax authority requirements)
- **Swiss FADP Article 6:** Purpose limitation (retain only as long as needed)
- **Swiss OR Article 958f:** 10-year retention for accounting documents
- **Contractual Obligation:** Retention specified in customer/vendor agreements
- **Legitimate Interest:** Business need balanced against data subject rights


**Quality Check:**

- Every data category has a retention period assigned?
- Every retention period has a legal/regulatory justification?
- Retention periods align with applicable regulations (not excessive)?
- Backup retention ≤ production data retention (or justified exception)?


### Step 3: Deletion Trigger Configuration (Sheet 4)

**Objective:** Document how data is actually deleted when retention period expires

**Instructions:**
1. Copy data categories from Sheet 2 to Column A
2. Assign Status in Column F based on deletion trigger implementation:

   - ✅ Compliant: Automated deletion trigger implemented and verified
   - ⚠️ Partial: Manual deletion process documented but not automated
   - ❌ Non-Compliant: No deletion trigger or process exists

3. Document Trigger Type in Column R (Automatic, Manual, Semi-Automatic, Event-Based)
4. Select Trigger Frequency in Column S (Real-time, Daily, Weekly, Monthly, etc.)
5. Verify Legal Hold Check Integrated in Column T

**Deletion Trigger Types:**

**Automatic:**

- Cloud storage lifecycle policies (e.g., AWS S3 lifecycle, Azure Blob lifecycle)
- Database table partitioning with automatic purge
- Scheduled deletion jobs (cron, Task Scheduler, Azure Functions)
- Application-level retention enforcement


**Manual:**

- IT operations team performs quarterly cleanup
- Business unit reviews and deletes on schedule
- Ad-hoc deletion upon management approval


**Semi-Automatic:**

- System generates deletion candidates, human approves
- Automated flagging, manual execution


**Event-Based:**

- Customer account closure triggers data deletion
- Contract termination initiates retention countdown
- Employee departure starts HR record retention timer


**Quality Check:**

- High-risk data (Confidential/Restricted) has automated deletion?
- Manual processes have documented procedures?
- Legal hold checks prevent accidental deletion of preserved data?
- Deletion triggers verified through testing (see ISMS-IMP-A.8.10.4)?


### Step 4: Legal Hold Procedures (Sheet 5)

**Objective:** Document procedures to suspend deletion when legally required

**Instructions:**
1. Document each system/data category that could be subject to legal hold
2. Describe Legal Hold Notification Process (how stakeholders are notified)
3. Document Active Legal Holds count in Column R
4. Specify Legal Hold Notification Process type in Column S
5. Define Hold Review Frequency in Column T

**When Legal Holds Are Required:**

- Pending or anticipated litigation
- Government investigation or audit
- Internal investigation (fraud, misconduct)
- Regulatory examination
- Contractual obligation to preserve records


**Legal Hold Process Elements:**

- **Identification:** Who determines when legal hold is necessary?
- **Notification:** How are IT operations and data custodians notified?
- **Implementation:** Technical mechanism to prevent deletion (disable automation, flag records, move to hold area)
- **Monitoring:** How is compliance with hold verified?
- **Release:** Approval process to lift hold and resume normal deletion


**Quality Check:**

- Legal hold procedures documented and approved by Legal Counsel?
- Technical controls prevent accidental deletion of held data?
- Legal holds reviewed regularly (at least quarterly)?
- All data custodians trained on legal hold obligations?


### Step 5: Data Subject Rights (Sheet 6)

**Objective:** Assess GDPR Article 17 / FADP erasure request handling capabilities

**Instructions:**
1. Document each data category that contains personal data
2. Assess current response time in Column R (target: <30 days per GDPR)
3. Indicate GDPR/FADP Applicability in Column S
4. Record Request Volume (Last 12 Months) in Column T
5. Document Status in Column F based on compliance with timelines

**GDPR Article 17 - Right to Erasure ("Right to be Forgotten"):**

Data subjects can request deletion when:

- Personal data no longer necessary for original purpose
- Data subject withdraws consent (and no other legal basis)
- Data subject objects to processing (and no overriding legitimate grounds)
- Personal data unlawfully processed
- Legal obligation requires erasure
- Data collected from a child (special protections)


**Exceptions (When Deletion Can Be Refused):**

- Legal obligation to retain (e.g., tax records)
- Public interest (public health, scientific research)
- Legal claims (defense against litigation)
- Archiving in the public interest


**Process Requirements:**

- **Response Deadline:** 30 days (GDPR), can extend to 60 days if complex
- **Verification:** Confirm identity of requester
- **Scope:** Delete from all systems (production, backups, third-parties)
- **Confirmation:** Notify data subject of completion
- **Documentation:** Maintain log of all erasure requests and outcomes


**Quality Check:**

- Erasure request procedure documented and communicated to data subjects?
- Average response time ≤ 30 days?
- Process includes verification of requester identity?
- Third-party processors notified of erasure requests (GDPR Article 19)?
- Exceptions properly documented and legally justified?


### Step 6: Evidence Collection (Sheet 8)

**Objective:** Link supporting documentation to assessment findings

**Instructions:**
1. For each data category or finding, create evidence entry
2. Evidence Register auto-generates Evidence ID (EV-001, EV-002, etc.)
3. Document Evidence Type, Location, Retention Period
4. Reference Evidence ID in Column N of assessment sheets

**Evidence Types:**

- **Policy Documents:** Data retention policy, deletion policy
- **Technical Documentation:** Deletion trigger configuration, automation scripts
- **Regulatory Documents:** GDPR Article 30 records, FADP processing register
- **Audit Logs:** Deletion execution logs, data subject request logs
- **Contracts:** Third-party data processing agreements with deletion clauses
- **Legal Opinions:** Retention period justifications, legal hold procedures
- **Testing Results:** Deletion verification test reports (from ISMS-IMP-A.8.10.4)


**Quality Check:**

- Every assessment finding has supporting evidence?
- Evidence locations are accessible to auditors?
- Evidence retention periods defined?
- Sensitive evidence properly protected (access controls)?


### Step 7: Review Summary Dashboard (Sheet 7)

**Objective:** Validate overall compliance metrics and identify critical gaps

**The Summary Dashboard auto-calculates:**

- Overall compliance percentage across all assessment areas
- Count of compliant, partial, and non-compliant data categories
- Critical gaps requiring immediate attention
- Data categories without retention schedules
- Data categories without deletion triggers
- Average data subject request response time


**Review Questions:**

- Does overall compliance % reflect your understanding of [Organization]'s posture?
- Are critical gaps accurately identified?
- Do remediation priorities align with business risk?
- Are there anomalies requiring investigation?


### Step 8: Quality Check & Approval (Sheet 9)

**Objective:** Final validation and three-level approval workflow

**Self-Check Before Submitting for Approval:**

- [ ] All data categories documented (no major gaps)
- [ ] Every retention period has legal/regulatory justification
- [ ] Deletion triggers assessed for all categories
- [ ] Legal hold procedures documented
- [ ] Data subject rights metrics current (last 12 months)
- [ ] Evidence register populated with supporting documentation
- [ ] Status indicators accurate (not aspirational)
- [ ] Gaps and remediation plans realistic and resourced


**Approval Workflow:**
1. **Level 1: Technical/Operational** - DPO/Privacy Officer validates accuracy
2. **Level 2: Management** - CISO/CIO approves remediation resource allocation
3. **Level 3: Executive** - CEO/CRO acknowledges overall retention posture and risks

---

# Question-by-Question Guidance

## Data Category Registry (Sheet 2)

**Q: What exactly is a "data category"?**
A: A data category is a logical grouping of similar data with the same retention and deletion requirements. Examples:

- "Customer Contact Information" (names, emails, phone numbers)
- "Employee HR Records" (employment contracts, performance reviews)
- "Financial Transaction Records" (invoices, payments, receipts)


**Q: How granular should data categories be?**
A: Granular enough to assign meaningful retention periods. For example:

- ✅ Good: "Customer Account Data", "Customer Marketing Preferences", "Customer Support Tickets" (different retention needs)
- ❌ Too Broad: "All Customer Data" (mixing data with different legal requirements)
- ❌ Too Granular: "Customer First Name", "Customer Last Name" (same retention, unnecessarily fragmented)


**Q: Should backups be listed as separate data categories?**
A: Yes, if backup retention differs from production. For example:

- Production data: "Active Customer Accounts" (retained while account active)
- Backup data: "Customer Account Backups" (retained 90 days for disaster recovery)


**Q: What if data is stored in multiple locations?**
A: List as one data category but note all locations in Column R or Notes (Column O). Retention schedule applies uniformly across all locations.

## Retention Schedule Compliance (Sheet 3)

**Q: Where do I find legal retention requirements?**
A: Sources to consult:

- **Legal Counsel:** Primary source for legal obligations
- **Regulatory Authority Websites:** EDPB (GDPR), FDPIC (FADP), industry regulators
- **Industry Associations:** Often publish retention guidance
- **Professional Advisors:** Accountants, auditors, compliance consultants
- **Internal Compliance Team:** Regulatory requirement register


**Q: What if multiple regulations apply with different retention periods?**
A: Apply the LONGEST retention period required by any applicable regulation, then document all applicable bases in Column E. Example:

- Tax law: 7 years
- Contract: 5 years
- GDPR: No specific requirement (only "as long as necessary")
- **Decision:** Retain 7 years (tax law requirement), document "Swiss Tax Law, Contractual Obligation" in Column E


**Q: What if no specific retention requirement exists?**
A: Apply "business necessity" standard:

- Retain only as long as needed for original purpose (GDPR Article 5.1.e)
- Consider: operational needs, business value, storage costs, breach risk
- Document justification: "Retained 1 year for customer support quality, no longer needed after"
- **Avoid:** "Permanent" or "Just in case" retention without clear justification


**Q: How do I handle event-based retention?**
A: Define the triggering event and countdown clearly. Examples:

- "Customer account closure + 6 months" (retention starts when account closed)
- "Contract termination + 3 years" (retention starts when contract ends)
- "Employee departure + 7 years" (retention starts on last day of employment)


## Deletion Trigger Configuration (Sheet 4)

**Q: What's the difference between "Automatic" and "Semi-Automatic"?**
A:

- **Automatic:** System deletes without human intervention (e.g., AWS S3 lifecycle rule automatically deletes objects after 90 days)
- **Semi-Automatic:** System identifies deletion candidates, human approves execution (e.g., script generates list of expired records, DBA reviews and executes DELETE statement)


**Q: Is manual deletion acceptable?**
A: Yes, but with conditions:

- ✅ Acceptable: Low-volume data (<100 records/year), non-sensitive classification, documented procedure
- ❌ Not Acceptable: High-volume data, Confidential/Restricted classification, no documented procedure
- **Best Practice:** Automate deletion for any data category with >1,000 records or Confidential+ classification


**Q: How often should deletion triggers run?**
A: Depends on data volume and retention period:

- **Real-time/Daily:** High-volume transactional data (logs, sessions)
- **Weekly/Monthly:** Moderate-volume business data (closed tickets, completed projects)
- **Quarterly/Annual:** Low-volume or long-retention data (archived contracts, historical reports)


**Q: What about the "Backup Deletion Paradox"?**
A: Production data deleted per retention schedule, but persists in backups. Solutions:
1. **Backup Retention ≤ Production Retention:** Backups auto-expire before production deletion (safest, simplest)
2. **Backup Exclusion:** Exclude data category from backups (complex, risky)
3. **Backup Scrubbing:** Periodically remove expired data from backups (technically complex, verify GDPR compliance)

**Recommended:** Align backup retention to be SHORTER than production data retention to avoid paradox.

## Legal Hold Procedures (Sheet 5)

**Q: Who decides when to place legal hold?**
A: Typically:

- **Internal:** Legal Counsel, General Counsel, Chief Legal Officer
- **External:** Outside counsel in litigation matters
- **Coordination:** Legal Counsel notifies IT Operations/Records Management


**Q: How quickly must legal holds be implemented?**
A: Immediately upon notification. Delays can result in:

- Spoliation of evidence (destruction after hold notice)
- Adverse inference in litigation (court assumes destroyed evidence was unfavorable)
- Professional sanctions against counsel
- Financial penalties


**Q: Can we still delete data on legal hold after retention period expires?**
A: NO. Legal hold suspends normal retention/deletion. Data must be preserved until:

- Legal Counsel explicitly releases the hold
- Litigation/investigation concluded
- Regulatory examination completed


**Q: What if automated deletion runs before legal hold implemented?**
A: This is a critical failure. Prevention measures:

- Legal Counsel maintains list of systems potentially subject to hold
- IT Operations has emergency "kill switch" to disable deletion automation
- Regular legal hold training for IT staff
- Post-implementation verification that data preserved


## Data Subject Rights (Sheet 6)

**Q: Must we delete ALL data upon erasure request?**
A: No, exceptions apply under GDPR Article 17.3:

- **Legal Obligation:** Tax records, financial reporting (cannot delete)
- **Legal Claims:** Data needed to defend against litigation
- **Public Interest:** Public health data, scientific research (with safeguards)
- **Archiving:** Historical archives in the public interest


Document exception basis and communicate to data subject.

**Q: How do we verify identity of requester?**
A: GDPR requires "reasonable measures" to verify identity:

- **Low Risk:** Email confirmation (data subject emails from registered email address)
- **Medium Risk:** Multi-factor verification (security questions + email)
- **High Risk:** Government ID verification (for sensitive data like financial records)


Balance: Verification must be sufficient to prevent unauthorized deletion, but not so burdensome it obstructs legitimate requests.

**Q: What about data in backups?**
A: GDPR recognizes backup challenges. Options:
1. **Document exception:** Backups retained for technical reasons, data isolated and not used (GDPR Recital 39)
2. **Backup exclusion:** Exclude data subject's data from future backups
3. **Backup scrubbing:** Remove data from existing backups (complex, may not be technically feasible)

**Recommended:** Document that backup retention is solely for disaster recovery, data not accessed/used after deletion from production.

**Q: Must we notify third-party processors of deletion?**
A: Yes, per GDPR Article 19:

- Controller must inform processors of erasure request
- Processors must delete unless legal obligation requires retention
- Controller must obtain confirmation from processors


Document third-party notifications in Evidence Register.

---

# Evidence Collection

## What Evidence to Collect

For each assessment area, gather supporting documentation:

**Data Category Registry:**

- Data inventory documentation (existing or created during assessment)
- GDPR Article 30 / FADP Article 12 processing records
- Data flow diagrams
- System documentation showing storage locations


**Retention Schedule Compliance:**

- Legal retention requirement analysis (Legal Counsel memo)
- Regulatory guidance documents (EDPB, FDPIC opinions)
- Industry retention standards (if applicable)
- Board/Executive approval of retention schedule
- Retention schedule document (published version)


**Deletion Trigger Configuration:**

- Automation configuration screenshots (lifecycle policies, cron jobs)
- Deletion procedure documentation (for manual processes)
- Code/scripts implementing automated deletion
- Deletion execution logs (last 3-6 months)


**Legal Hold Procedures:**

- Legal hold policy document
- Legal hold notification template
- Active legal hold register
- Legal hold release approval records


**Data Subject Rights:**

- Data subject rights policy/procedure
- Erasure request form (template)
- Request tracking log (last 12 months, anonymized)
- Response time metrics
- Third-party notification confirmations


## Evidence Storage & Retention

**Where to Store Evidence:**

- Centralized evidence repository (ISMS document management)
- Access-controlled file share
- Compliance management platform


**Evidence Retention Period:**

- Minimum: Duration of ISO 27001 certification + 1 cycle (typically 4 years)
- Longer if litigation/investigation risk
- Personal data in evidence: Apply deletion triggers per retention schedule


**Evidence Protection:**

- Access controls: Limited to ISMS team, auditors, authorized personnel
- Encryption: If evidence contains sensitive data
- Integrity: Hash/checksum to detect tampering


## Audit-Readiness Tips

**What Auditors Will Look For:**
1. **Completeness:** All data categories documented? No obvious gaps?
2. **Justification:** Every retention period has legal/regulatory basis?
3. **Implementation:** Deletion triggers actually configured, not just aspirational?
4. **Verification:** Evidence that deletion triggers work (see ISMS-IMP-A.8.10.4)
5. **Data Subject Rights:** Erasure requests handled within regulatory timelines?
6. **Legal Holds:** Procedures prevent accidental deletion of preserved data?

**Common Audit Findings (And How to Avoid Them):**

- ❌ **"No retention schedule"** → Complete this assessment, get retention schedule approved
- ❌ **"Retention periods excessive with no justification"** → Document legal basis, consider reducing periods
- ❌ **"No deletion triggers implemented"** → Prioritize automation for high-risk data
- ❌ **"Backups retained longer than production data"** → Align backup retention ≤ production retention
- ❌ **"Data subject erasure requests not tracked"** → Implement request log, monitor response times
- ❌ **"No legal hold procedures"** → Document procedures, train IT staff


---

# Common Pitfalls

## Data Inventory Gaps

**Pitfall:** Forgetting to include certain data types or systems

**Common Omissions:**

- Cloud/SaaS applications (email, CRM, marketing tools)
- Backups and archives
- Log files and monitoring data
- Test/development environments
- Employee personal devices (if BYOD policy)
- Third-party systems where data is stored


**Prevention:**

- Conduct full IT asset inventory before assessment
- Interview Business Unit Owners systematically
- Review GDPR Article 30 records for data processing activities
- Check cloud billing for SaaS subscriptions


## Overly Broad Retention Periods

**Pitfall:** "Retain everything forever" or "10 years for everything just to be safe"

**Why This Is Problematic:**

- GDPR storage limitation principle (Article 5.1.e)
- Increased storage costs
- Increased data breach risk and liability
- Audit finding: Retention not proportionate to purpose


**Prevention:**

- Consult Legal Counsel for actual requirements (not assumptions)
- Apply "minimum necessary" principle
- Document specific legal basis for each retention period
- Review retention schedules annually


## Backup Retention Paradox

**Pitfall:** Production data deleted per schedule, but persists in 7-year backups

**Scenario:**

- Customer requests GDPR erasure
- Production database: Deleted immediately
- Backup tapes: Customer data still exists in monthly backups for next 7 years
- **Result:** Non-compliance with GDPR Article 17


**Prevention:**

- **Strategy 1:** Backup retention ≤ Production retention (safest)
- **Strategy 2:** Document backup exception per GDPR Recital 39 (backups for disaster recovery only, data not accessed)
- **Strategy 3:** Implement backup exclusion or scrubbing (complex, verify with GDPR counsel)


## No Deletion Trigger Implementation

**Pitfall:** Retention schedule documented, but no actual deletion occurring

**Scenario:**

- Policy says "Customer data retained 3 years after account closure"
- Reality: No deletion job configured, all data kept forever
- **Result:** Policy-implementation gap, audit finding


**Prevention:**

- For EVERY data category, document deletion trigger mechanism (Sheet 4)
- Verify deletion triggers actually work (see ISMS-IMP-A.8.10.4 for verification testing)
- Automate deletion for high-volume or high-risk data


## Legal Hold Process Failures

**Pitfall:** Automated deletion runs during legal hold, destroying evidence

**Scenario:**

- Litigation filed Friday afternoon
- Legal Counsel sends legal hold notice Monday morning
- Automated deletion job runs Saturday night, purges relevant data
- **Result:** Spoliation of evidence, sanctions, adverse inference


**Prevention:**

- Legal Counsel maintains list of systems potentially subject to hold
- IT Operations has emergency procedure to disable automation
- Legal hold notifications are URGENT (same-day implementation)
- Regular training on legal hold obligations


## Data Subject Rights Response Delays

**Pitfall:** Erasure requests take 60+ days, exceeding GDPR timeline

**Scenario:**

- Data subject submits erasure request
- Request sits in general customer support queue
- Eventually escalated to DPO after 45 days
- Investigation and execution takes another 30 days
- **Result:** GDPR violation (30-day deadline missed)


**Prevention:**

- Dedicated erasure request intake process (not general support email)
- Request tracking system with SLA alerts
- Monthly metrics review (average response time)
- Escalation procedure if approaching 30-day deadline


---

# Quality Checklist

Before submitting assessment for approval, verify:

## Completeness

- [ ] All data categories documented (no major systems omitted)
- [ ] All sheets completed (no "TBD" or blank sections)
- [ ] Evidence Register populated with supporting documentation
- [ ] Summary Dashboard reviewed and validated


## Accuracy

- [ ] Data classifications match [Organization]'s classification scheme
- [ ] Business Owners verified by actual department heads
- [ ] Retention periods validated by Legal Counsel
- [ ] Legal/regulatory bases accurately cited
- [ ] Status indicators reflect current reality (not aspirational)


## Compliance

- [ ] Every data category has retention period assigned
- [ ] Every retention period has legal/regulatory justification
- [ ] Deletion triggers documented for all categories
- [ ] Legal hold procedures cover all in-scope systems
- [ ] Data subject rights metrics current (last 12 months)


## Remediation Planning

- [ ] Gaps identified and described clearly
- [ ] Remediation plans actionable and realistic
- [ ] Target completion dates assigned
- [ ] Remediation owners identified
- [ ] Budget/resource needs flagged


## Audit Readiness

- [ ] Traceability: Control → Policy → Assessment → Evidence
- [ ] Evidence locations accessible to auditors
- [ ] Supporting documentation current (within last 12 months)
- [ ] No obvious compliance gaps that would result in audit finding


---

# Review & Approval

## Self-Review

Before submitting for formal approval, conduct self-review:

1. **Read-Through:** Review entire workbook for typos, inconsistencies, unclear entries
2. **Spot-Check Validation:** Select 5 random data categories, verify accuracy against source systems
3. **Gap Analysis:** Do identified gaps align with your understanding of [Organization]'s posture?
4. **Evidence Check:** Can you locate all referenced evidence documents?
5. **Stakeholder Validation:** Share draft with 2-3 Business Unit Owners for feedback

## Approval Workflow (Sheet 9)

**Level 1: Technical/Operational Approval**

- **Approver:** Data Protection Officer / Privacy Officer / Information Security Manager
- **Validates:** Technical accuracy, completeness of data inventory, deletion trigger feasibility
- **Approval Criteria:** Assessment accurately reflects current state of [Organization]'s retention posture


**Level 2: Management Approval**

- **Approver:** Chief Information Security Officer / Chief Information Officer / Chief Compliance Officer
- **Validates:** Remediation plans, resource allocation, budget requirements
- **Approval Criteria:** Remediation plans are realistic and adequately resourced


**Level 3: Executive Approval**

- **Approver:** Chief Executive Officer / Chief Risk Officer / Board Delegate
- **Validates:** Overall retention posture, risk acceptance for identified gaps
- **Approval Criteria:** Executive leadership acknowledges retention compliance status and commits to remediation


## Post-Approval Actions

Once all three levels approve:

1. **Communicate Results:** Share summary with stakeholders (Business Unit Owners, IT Operations, Legal)
2. **Initiate Remediation:** Begin addressing critical and high-risk gaps per approved timelines
3. **Schedule Follow-Up:** Quarterly progress review on remediation plans
4. **Plan Next Assessment:** Schedule annual re-assessment (or sooner if regulatory changes)
5. **Update ISMS Documentation:** If retention schedules changed, update ISMS-POL-A.8.10 and related documents

---

**END OF PART I: USER COMPLETION GUIDE**

---

**Continue to PART II: TECHNICAL SPECIFICATION (Deliverable 2) for detailed Excel workbook structure, column definitions, validation rules, and Python script integration points.**

# ISMS-IMP-A.8.10.1 - Retention & Deletion Triggers Assessment
# DELIVERABLE 2: PART II - TECHNICAL SPECIFICATION

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Python Developers, Excel Workbook Designers, ISMS Implementation Technical Teams

---

# Workbook Structure Overview

## Sheet Organization (9 Sheets Total)

| Sheet # | Sheet Name | Purpose | Rows | User Entry |
|---------|------------|---------|------|------------|
| 1 | Instructions & Legend | Assessment guidance, color coding, definitions | ~50 | Read-only |
| 2 | Data Category Registry | Complete inventory of all data types | ~25-50 | 13 data rows |
| 3 | Retention Schedule Compliance | Legal/regulatory alignment for retention periods | ~25-50 | 13 data rows |
| 4 | Deletion Trigger Configuration | Automated and manual deletion mechanisms | ~25-50 | 13 data rows |
| 5 | Legal Hold Management | Procedures to suspend deletion when required | ~25-50 | 13 data rows |
| 6 | Data Subject Rights | GDPR Article 17 / FADP erasure request handling | ~25-50 | 13 data rows |
| 7 | Summary Dashboard | Compliance overview, KPIs, critical gaps | ~60 | Formula-driven |
| 8 | Evidence Register | Links to supporting documentation | ~110 | 100 data rows |
| 9 | Approval Sign-Off | Three-level approval workflow | ~75 | Text entry |

**Total Data Entry Points:** ~150-250 (depending on data category count)

## Workbook Flow

```
Sheet 1 (Instructions) → Orientation
↓
Sheets 2-6 (Assessment Areas) → Data Collection
↓
Sheet 8 (Evidence Register) → Documentation
↓
Sheet 7 (Summary Dashboard) → Validation
↓
Sheet 9 (Approval Sign-Off) → Authorization
```

---

# Sheet 1: Instructions & Legend

## Purpose
Provide clear guidance on workbook usage, color coding scheme, and assessment context.

## Content Sections

**Section 1: Assessment Overview (Rows 3-12)**

- Document ID, version, related policy
- Purpose and scope
- Target audience
- Review cycle and date


**Section 2: How to Use This Workbook (Rows 14-25)**

- Step-by-step workflow
- Color coding explanation
- Validation rules
- Evidence linking


**Section 3: Assessment Context (Rows 27-40)**

- What this assessment covers
- What this assessment does NOT cover
- Connection to ISMS-POL-A.8.10, Section 2.1 (Retention & Deletion Triggers)
- Related ISMS documents


**Section 4: Color Legend (Rows 42-52)**

| Color | Purpose | When to Use |
|-------|---------|-------------|
| Blue Header | Column headers | All assessment sheets |
| Yellow Fill | Data entry cells | User input required |
| Gray Fill | Auto-calculated | Formula cells, no user entry |
| Green | ✅ Compliant | Status indicator |
| Yellow | ⚠️ Partial | Status indicator |
| Red | ❌ Non-Compliant | Status indicator |
| White | N/A | Not applicable |

**Section 5: Status Definitions (Rows 54-65)**

**✅ Compliant:**

- Data category has documented retention period with legal basis
- Deletion trigger implemented and verified
- Process meets policy requirements


**⚠️ Partial:**

- Retention period documented but not all requirements met
- Manual deletion process exists but not automated
- Minor gaps that don't pose immediate compliance risk


**❌ Non-Compliant:**

- No retention period defined
- No deletion trigger or process
- Significant gap requiring immediate remediation


**N/A:**

- Assessment area not applicable to this data category


---

# Sheet 2: Data Category Registry

## Purpose
Document complete inventory of all data types processed by [Organization].

## Sheet Layout

**Header Section (Rows 1-9):**

- Row 1: Sheet title "2. Data Category Registry"
- Row 2: Assessment objective
- Row 3: Instructions for completion
- Rows 4-6: Key guidance notes
- Row 7: Blank separator
- Row 8: Quality check reminders
- Row 9: Column headers (frozen)


**Data Entry Section (Rows 10-22):**

- 13 rows for data categories (yellow fill)
- Pre-populated example in Row 10 (editable)
- Rows 11-22 blank for user entry


**Reference Section (Rows 24-40):**

- Common data categories checklist (20 items)
- Examples: Customer data, Employee data, Financial records, Operational logs, etc.


## Column Definitions (17 standard + 3 extended = 20 total)

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Data Category | 35 | Text | Primary identifier (e.g., "Customer Contact Information") |
| B | Data Classification | 20 | Dropdown | Public / Internal / Confidential / Restricted |
| C | Business Owner | 20 | Text | Department or role responsible |
| D | Retention Period | 20 | Dropdown | See validation options below |
| E | Legal/Regulatory Basis | 25 | Dropdown | Justification for retention period |
| F | Status | 18 | Dropdown | ✅ / ⚠️ / ❌ / N/A |
| G | Implementation Date | 15 | Date | When retention schedule deployed |
| H | Last Review Date | 15 | Date | Most recent schedule review |
| I | Next Review Date | 15 | Date | Scheduled next review |
| J | Gap Identified | 30 | Text | If not compliant, describe issue |
| K | Remediation Plan | 30 | Text | How gap will be addressed |
| L | Target Completion | 15 | Date | Remediation deadline |
| M | Risk Level | 15 | Dropdown | Critical / High / Medium / Low |
| N | Evidence Reference | 20 | Text | Link to Evidence Register (EV-XXX) |
| O | Notes / Comments | 30 | Text | Additional context |
| P | Remediation Owner | 20 | Text | Person responsible for fix |
| Q | Budget Required | 15 | Dropdown | Yes / No / Unknown |
| R | Primary Storage Location | 25 | Dropdown | On-Premise / Cloud (IaaS/PaaS/SaaS) / Hybrid / Third-Party |
| S | Volume/Records | 20 | Text | Approximate count or size (e.g., "10,000 records", "500 GB") |
| T | Contains PII/SPI | 20 | Dropdown | Yes - PII / Yes - SPI / Yes - Both / No |

## Data Validation Rules

**Column B - Data Classification:**
```
Dropdown: Public, Internal, Confidential, Restricted
```

**Column D - Retention Period:**
```
Dropdown: 30 days, 60 days, 90 days, 6 months, 1 year, 2 years, 3 years, 5 years, 7 years, 10 years, Permanent, Until Event Occurs, Other (specify in notes)
```

**Column E - Legal/Regulatory Basis:**
```
Dropdown: Swiss FADP, EU GDPR, Swiss Code of Obligations (OR), Swiss Tax Law, EU ePrivacy Directive, Industry Standard (specify), Contractual Obligation, Legitimate Interest, Consent, Legal Obligation, Multiple Bases (specify), Other (specify in notes)
```

**Column F - Status:**
```
Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A
```

**Column M - Risk Level:**
```
Dropdown: Critical, High, Medium, Low
```

**Column Q - Budget Required:**
```
Dropdown: Yes, No, Unknown
```

**Column R - Primary Storage Location:**
```
Dropdown: On-Premise, Cloud (IaaS), Cloud (PaaS), Cloud (SaaS), Hybrid, Third-Party
```

**Column T - Contains PII/SPI:**
```
Dropdown: Yes - PII, Yes - SPI, Yes - Both, No
Note: PII = Personally Identifiable Information, SPI = Sensitive Personal Information
```

## Conditional Formatting

**Status Column (F):**

- ✅ Compliant: Green fill (RGB: 198, 239, 206)
- ⚠️ Partial: Yellow fill (RGB: 255, 235, 156)
- ❌ Non-Compliant: Red fill (RGB: 255, 199, 206)


**Risk Level Column (M):**

- Critical: Red fill (RGB: 255, 199, 206)
- High: Orange fill (RGB: 255, 230, 153)
- Medium: Yellow fill (RGB: 255, 242, 204)
- Low: No special formatting


## Reference Checklist (Rows 24-43)

**Common Data Categories to Consider:**

| # | Category | Example Systems |
|---|----------|----------------|
| 1 | Customer Contact Information | CRM, Sales systems |
| 2 | Customer Transaction History | E-commerce, Billing |
| 3 | Customer Support Tickets | Helpdesk, Support portal |
| 4 | Marketing Consent Records | Marketing automation |
| 5 | Employee HR Records | HRIS, Payroll |
| 6 | Employee Performance Reviews | Performance management |
| 7 | Employee IT Access Logs | IAM, SIEM |
| 8 | Financial Transaction Records | Accounting, ERP |
| 9 | Invoices and Receipts | Billing, Finance |
| 10 | Contracts and Agreements | Contract management |
| 11 | Application Logs | Servers, Applications |
| 12 | System Monitoring Data | SIEM, Monitoring tools |
| 13 | Backup Data | Backup systems |
| 14 | Email Archives | Email servers |
| 15 | Document Management | SharePoint, DMS |
| 16 | Source Code Repositories | Git, Version control |
| 17 | Test/Development Data | Dev environments |
| 18 | Website Analytics | Google Analytics, etc. |
| 19 | Security Incident Records | SIEM, Incident response |
| 20 | Audit Logs | Various systems |

---

# Sheet 3: Retention Schedule Compliance

## Purpose
Map legal/regulatory retention requirements to each data category.

## Sheet Layout

**Header Section (Rows 1-9):**

- Row 1: Sheet title "3. Retention Schedule Compliance"
- Row 2: Assessment objective
- Row 3: Instructions for completion
- Rows 4-6: Key guidance notes on retention period justification
- Row 7: Blank separator
- Row 8: Reminder: "Every retention period MUST have legal/regulatory basis"
- Row 9: Column headers (frozen)


**Data Entry Section (Rows 10-22):**

- 13 rows for data categories (yellow fill)
- Columns A-Q same as Sheet 2
- Columns R-T: Extended columns specific to retention


**Reference Section (Rows 24-50):**

- Common retention periods table
- Legal/regulatory basis examples
- Retention calculation methods guidance


## Column Definitions (Standard A-Q + Extended R-T)

**Columns A-Q:** Same as Sheet 2 (standard columns)

**Extended Columns (R-T) - Retention-Specific:**

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| R | Retention Calculation Method | 25 | Dropdown | Fixed Period / Event-Based / Hybrid |
| S | Event Trigger Description | 30 | Text | If event-based, describe the event (e.g., "Account closure", "Contract termination") |
| T | Backup Retention Aligned | 20 | Dropdown | Yes / No / Partial / N/A |

## Data Validation Rules (Extended Columns)

**Column R - Retention Calculation Method:**
```
Dropdown: Fixed Period, Event-Based, Hybrid
```

**Fixed Period Example:** "Retain 3 years from date of creation"
**Event-Based Example:** "Retain until account closure + 6 months"
**Hybrid Example:** "Retain 5 years OR until contract termination, whichever is longer"

**Column T - Backup Retention Aligned:**
```
Dropdown: Yes, No, Partial, N/A
```

**Alignment Rules:**

- **Yes:** Backup retention period ≤ Production retention period
- **No:** Backup retention > Production retention (Backup Deletion Paradox risk)
- **Partial:** Some backups aligned, others not
- **N/A:** Data category not included in backups


## Reference Tables (Rows 24-50)

**Table 1: Common Retention Periods (Rows 26-38)**

| Data Type | Typical Retention | Legal Basis |
|-----------|------------------|-------------|
| Application logs | 30-90 days | Operational need |
| Session data | 30 days | GDPR necessity |
| Marketing consent | 1-2 years | GDPR Article 6.1.a |
| Customer accounts | Until closure + 6 months | GDPR Article 17 exceptions |
| Employment records | 7 years post-termination | Swiss OR, Tax law |
| Accounting records | 10 years | Swiss OR Article 958f |
| Tax documents | 10 years | Swiss Tax Law |
| Contracts | Duration + 3-10 years | Statute of limitations |
| Legal hold data | Until hold released | Litigation requirements |
| Audit trails | 7 years | ISO 27001 requirement |
| GDPR deletion requests | 3-7 years | Proof of compliance |
| Security incidents | 7 years | Forensic/investigation |

**Table 2: Retention Calculation Examples (Rows 40-50)**

**Fixed Period:**

- "Retain application logs 90 days from date of creation"
- Implementation: Automated deletion after 90 days


**Event-Based:**

- "Retain customer data until account closure + 6 months"
- Implementation: Deletion trigger = Account closure date + 180 days


**Hybrid:**

- "Retain employment records 7 years OR until litigation resolved, whichever is longer"
- Implementation: Check both conditions before deletion


---

# Sheet 4: Deletion Trigger Configuration

## Purpose
Document how data is actually deleted when retention period expires.

## Sheet Layout

**Header Section (Rows 1-9):**

- Row 1: Sheet title "4. Deletion Trigger Configuration"
- Row 2: Assessment objective
- Row 3: Instructions for completion
- Rows 4-6: Deletion trigger type explanations
- Row 7: Blank separator
- Row 8: Critical reminder: "Automated deletion REQUIRED for Confidential/Restricted data"
- Row 9: Column headers (frozen)


**Data Entry Section (Rows 10-22):**

- 13 rows for data categories (yellow fill)
- Focus: How is deletion actually executed?


**Reference Section (Rows 24-55):**

- Deletion trigger types and examples
- Automation options by technology
- Legal hold integration requirements


## Column Definitions (Standard A-Q + Extended R-T)

**Columns A-Q:** Same as Sheet 2 (standard columns)

**Extended Columns (R-T) - Deletion-Specific:**

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| R | Trigger Type | 25 | Dropdown | Automatic / Manual / Semi-Automatic / Event-Based |
| S | Trigger Frequency | 25 | Dropdown | Real-time / Daily / Weekly / Monthly / Quarterly / Annual / Ad-hoc |
| T | Legal Hold Check Integrated | 25 | Dropdown | Yes - Automated / Yes - Manual / No / N/A |

## Data Validation Rules (Extended Columns)

**Column R - Trigger Type:**
```
Dropdown: Automatic, Manual, Semi-Automatic, Event-Based
```

**Automatic:** System deletes without human intervention
**Manual:** Human executes deletion on schedule
**Semi-Automatic:** System identifies candidates, human approves
**Event-Based:** System deletes upon specific event (account closure, etc.)

**Column S - Trigger Frequency:**
```
Dropdown: Real-time, Daily, Weekly, Monthly, Quarterly, Annual, Ad-hoc
```

**Column T - Legal Hold Check Integrated:**
```
Dropdown: Yes - Automated, Yes - Manual, No, N/A
```

**Yes - Automated:** System automatically checks legal hold status before deletion
**Yes - Manual:** Human verifies no legal hold before approving deletion
**No:** No legal hold check (HIGH RISK - could delete evidence)
**N/A:** Data category not subject to legal holds

## Reference Tables (Rows 24-55)

**Table 1: Deletion Trigger Types - Detailed Examples (Rows 26-40)**

**Automatic Examples:**

- AWS S3 Lifecycle Policy: Delete objects after 90 days
- Azure Blob Lifecycle Management: Transition to cold storage, then delete
- Database partitioning: Drop old partitions on schedule
- Application-level: Soft delete after retention period, hard delete after grace period
- Scheduled jobs: Cron job runs daily, purges expired records


**Manual Examples:**

- IT operations team quarterly cleanup
- DBA runs DELETE query monthly
- Business unit reviews and archives annually
- Ad-hoc deletion upon management approval


**Semi-Automatic Examples:**

- Script generates list of expired records → DBA reviews → DBA executes
- System flags for deletion → Privacy Officer approves → Automation executes
- Quarterly report of deletable data → Management approves → IT executes


**Event-Based Examples:**

- Customer account closure → Wait 180 days → Automatic deletion
- Contract termination → Wait 3 years → Automatic deletion
- Employee departure → Wait 7 years → Automatic deletion


**Table 2: Automation Options by Technology (Rows 42-55)**

| Technology | Automation Method | Effort |
|------------|------------------|--------|
| AWS S3 | Lifecycle Policy | Low |
| Azure Blob | Lifecycle Management | Low |
| Google Cloud Storage | Object Lifecycle Management | Low |
| Databases (SQL) | Partitioning + DROP | Medium |
| Databases (NoSQL) | TTL (Time-To-Live) | Low |
| SaaS Applications | Native retention policies | Low-Medium |
| File Shares | PowerShell/Bash scripts | Medium |
| Email Systems | Retention tags/policies | Low-Medium |
| Backup Systems | Backup retention policies | Low |

---

# Sheet 5: Legal Hold Management

## Purpose
Document procedures to suspend deletion when legally required (litigation, investigation, audit).

## Sheet Layout

**Header Section (Rows 1-9):**

- Row 1: Sheet title "5. Legal Hold Management"
- Row 2: Assessment objective
- Row 3: Instructions for completion
- Rows 4-6: Legal hold scenarios and requirements
- Row 7: Blank separator
- Row 8: Critical warning: "Legal hold violations = Spoliation of evidence"
- Row 9: Column headers (frozen)


**Data Entry Section (Rows 10-22):**

- 13 rows for systems/data categories subject to legal hold
- Focus: Procedures and controls


**Reference Section (Rows 24-50):**

- When legal holds are required
- Legal hold process elements
- Consequences of failures


## Column Definitions (Standard A-Q + Extended R-T)

**Columns A-Q:** Same as Sheet 2 (standard columns)

**Extended Columns (R-T) - Legal Hold-Specific:**

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| R | Active Legal Holds | 20 | Number | Count of currently active holds on this system/data |
| S | Legal Hold Notification Process | 30 | Dropdown | Automated / Manual / Hybrid / None |
| T | Hold Review Frequency | 25 | Dropdown | Weekly / Monthly / Quarterly / Annual |

## Data Validation Rules (Extended Columns)

**Column R - Active Legal Holds:**
```
Number (integer): 0, 1, 2, 3, etc.
```

**Column S - Legal Hold Notification Process:**
```
Dropdown: Automated, Manual, Hybrid, None
```

**Automated:** System-generated email to IT/data custodians when hold placed
**Manual:** Legal Counsel sends email/memo to stakeholders
**Hybrid:** Automated notification + Manual follow-up confirmation
**None:** No formal notification process (HIGH RISK)

**Column T - Hold Review Frequency:**
```
Dropdown: Weekly, Monthly, Quarterly, Annual
```

Frequency should match litigation risk and volume of legal holds.

## Reference Tables (Rows 24-50)

**Table 1: When Legal Holds Are Required (Rows 26-34)**

| Scenario | Hold Timing | Hold Scope |
|----------|-------------|------------|
| Litigation filed | Immediately upon notice | All relevant data |
| Litigation anticipated | Upon reasonable anticipation | Potentially relevant data |
| Government investigation | Upon notification/subpoena | Requested data + related |
| Internal investigation | Upon investigation launch | Subject employee data |
| Regulatory examination | Upon notification | In-scope systems/records |
| Contractual obligation | Per contract terms | Specified data |

**Table 2: Legal Hold Process Elements (Rows 36-50)**

**1. Identification (Who decides hold is needed):**

- Legal Counsel / General Counsel
- External counsel (in litigation)
- Compliance Officer (regulatory exam)


**2. Notification (How custodians are informed):**

- Email from Legal Counsel to IT Operations
- Legal hold notice to all data custodians
- Emergency escalation for immediate holds


**3. Implementation (Technical controls):**

- Disable automated deletion jobs
- Flag records in system ("Legal Hold" tag)
- Move data to isolated hold area
- Document hold placement in Evidence Register


**4. Monitoring (Verification):**

- IT confirms hold implementation
- Periodic audits that hold data not deleted
- Legal Counsel maintains active hold register


**5. Release (Approval to resume deletion):**

- Legal Counsel explicit release authorization
- IT removes hold flags/re-enables automation
- Document hold release in Evidence Register


---

# Sheet 6: Data Subject Rights

## Purpose
Assess GDPR Article 17 / FADP erasure request handling capabilities and performance.

## Sheet Layout

**Header Section (Rows 1-9):**

- Row 1: Sheet title "6. Data Subject Rights (GDPR Article 17 / FADP Erasure)"
- Row 2: Assessment objective
- Row 3: Instructions for completion
- Rows 4-6: GDPR Article 17 requirements summary
- Row 7: Blank separator
- Row 8: Compliance target: "Response time ≤ 30 days (GDPR), extendable to 60 if complex"
- Row 9: Column headers (frozen)


**Data Entry Section (Rows 10-22):**

- 13 rows for data categories containing personal data
- Focus: Response time performance and process compliance


**Reference Section (Rows 24-60):**

- GDPR Article 17 conditions for erasure
- Exceptions where erasure can be refused
- Process requirements and best practices


## Column Definitions (Standard A-Q + Extended R-T)

**Columns A-Q:** Same as Sheet 2 (standard columns)

**Extended Columns (R-T) - Data Subject Rights-Specific:**

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| R | Average Response Time (Days) | 25 | Number | Actual performance (last 12 months) |
| S | GDPR/FADP Applicable | 25 | Dropdown | GDPR Only / FADP Only / Both / Neither |
| T | Request Volume (Last 12 Months) | 25 | Number | Count of erasure requests received |

## Data Validation Rules (Extended Columns)

**Column R - Average Response Time (Days):**
```
Number (integer): 0-90
Conditional Formatting:

- ≤30 days: Green fill (compliant)
- 31-60 days: Yellow fill (acceptable if complex)
- >60 days: Red fill (non-compliant)

```

**Column S - GDPR/FADP Applicable:**
```
Dropdown: GDPR Only, FADP Only, Both, Neither
```

**GDPR Only:** EU data subjects
**FADP Only:** Swiss data subjects (not in EU)
**Both:** Mixed EU and Swiss data subjects
**Neither:** Non-EU/non-Swiss data (other privacy laws may apply)

**Column T - Request Volume (Last 12 Months):**
```
Number (integer): 0, 1, 2, 3, ... 100+
```

## Reference Tables (Rows 24-60)

**Table 1: GDPR Article 17 - When Erasure Must Be Granted (Rows 26-35)**

Data subjects have the right to erasure when:

1. Personal data no longer necessary for original purpose
2. Data subject withdraws consent (and no other legal basis exists)
3. Data subject objects to processing (and no overriding legitimate grounds)
4. Personal data has been unlawfully processed
5. Legal obligation requires erasure
6. Data concerns a child (special protections apply)

**Table 2: GDPR Article 17.3 - When Erasure Can Be Refused (Rows 37-47)**

Erasure can be refused when necessary for:

1. **Legal Obligation:** Tax records, financial reporting, statutory retention
2. **Legal Claims:** Defense, establishment, or exercise of legal claims
3. **Public Interest:** Public health, scientific/historical research (with safeguards)
4. **Archiving:** Archives in the public interest
5. **Freedom of Expression:** Journalism, academic freedom

**Table 3: Process Requirements (Rows 49-60)**

**Response Timeline:**

- Standard: 30 days (GDPR Article 12.3)
- Complex cases: 60 days (with justification to data subject within 30 days)


**Verification:**

- Confirm identity of requester (reasonable measures)
- Methods: Email confirmation, security questions, government ID (for sensitive data)


**Scope of Deletion:**

- Production systems: Immediate deletion
- Backups: Document exception per GDPR Recital 39 (disaster recovery only)
- Third-party processors: Notify per GDPR Article 19, obtain confirmation


**Documentation:**

- Log all erasure requests (date, requester, data categories, outcome)
- Maintain for 3-7 years as proof of compliance
- Reference in Evidence Register


**Communication:**

- Acknowledge receipt within 5 days
- Confirm completion or explain exception
- If refused, explain reason and right to appeal to supervisory authority


---

# Sheet 7: Summary Dashboard

## Purpose
Aggregate compliance metrics from all assessment areas and identify critical gaps.

## Sheet Layout

**Header Section (Rows 1-5):**

- Row 1: Sheet title "7. Summary Dashboard - Retention & Deletion Triggers Compliance"
- Row 2: Assessment period and version
- Row 3: Generated date (auto-populated)
- Row 5: Overall compliance status indicator (colored)


**Section 1: Overall Compliance Summary (Rows 7-15)**

| Metric | Value | Status |
|--------|-------|--------|
| Total Data Categories Assessed | =COUNTA(Sheet2!A10:A22) | N/A |
| Data Categories Compliant | =COUNTIF(Sheet2!F10:F22,"✅ Compliant") | Formula |
| Data Categories Partial Compliance | =COUNTIF(Sheet2!F10:F22,"⚠️ Partial") | Formula |
| Data Categories Non-Compliant | =COUNTIF(Sheet2!F10:F22,"❌ Non-Compliant") | Formula |
| Overall Compliance % | =Compliant/(Total-N/A)*100 | Conditional format |

**Compliance Percentage Color Coding:**

- ≥90%: Green fill (excellent)
- 80-89%: Yellow fill (acceptable)
- 70-79%: Orange fill (needs improvement)
- <70%: Red fill (unacceptable)


**Section 2: Assessment Area Breakdown (Rows 17-30)**

| Assessment Area | Compliant | Partial | Non-Compliant | Compliance % |
|----------------|-----------|---------|---------------|--------------|
| Data Category Registry (Sheet 2) | Formula | Formula | Formula | Formula |
| Retention Schedule Compliance (Sheet 3) | Formula | Formula | Formula | Formula |
| Deletion Trigger Configuration (Sheet 4) | Formula | Formula | Formula | Formula |
| Legal Hold Management (Sheet 5) | Formula | Formula | Formula | Formula |
| Data Subject Rights (Sheet 6) | Formula | Formula | Formula | Formula |

**Section 3: Critical Gaps Requiring Immediate Attention (Rows 32-45)**

Auto-populated table pulling rows where:

- Status = "❌ Non-Compliant" AND Risk Level = "Critical" OR "High"


| Data Category | Assessment Area | Gap Description | Risk Level | Target Completion |
|---------------|----------------|-----------------|------------|-------------------|
| [Auto-pull from assessment sheets] | | | | |

**Section 4: Data Categories Without Retention Schedules (Rows 47-55)**

List of data categories where Column D (Retention Period) is blank.

**Section 5: Data Categories Without Deletion Triggers (Rows 57-65)**

List of data categories where Sheet 4 Column F = "❌ Non-Compliant" (no deletion trigger).

**Section 6: Data Subject Rights Performance (Rows 67-75)**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Average Response Time (Days) | =AVERAGE(Sheet6!R10:R22) | ≤30 days | Conditional |
| Requests Exceeding 30 Days | =COUNTIF(Sheet6!R10:R22,">30") | 0 | Conditional |
| Total Requests (Last 12 Months) | =SUM(Sheet6!T10:T22) | N/A | N/A |

**Section 7: Key Recommendations (Rows 77-85)**

Text section for assessor to provide top 3-5 recommendations based on findings.

---

# Sheet 8: Evidence Register

## Purpose
Centralized tracking of all supporting documentation for assessment findings.

## Sheet Layout

**Header Section (Rows 1-9):**

- Row 1: Sheet title "8. Evidence Register"
- Row 2: Purpose and usage instructions
- Row 3: Reminder: "Reference Evidence ID (EV-XXX) in Column N of assessment sheets"
- Rows 4-8: Guidance on evidence types and retention
- Row 9: Column headers (frozen)


**Data Entry Section (Rows 10-109):**

- 100 rows for evidence entries (yellow fill)
- Auto-numbered Evidence ID


**Total Rows:** ~115

## Column Definitions

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Evidence ID | 15 | Formula | Auto-generated (EV-001, EV-002, etc.) |
| B | Evidence Type | 25 | Dropdown | Policy / Technical / Regulatory / Audit Log / Contract / Legal Opinion / Testing Result / Other |
| C | Evidence Description | 40 | Text | Brief description of the evidence |
| D | Related Assessment Area | 25 | Dropdown | Data Category Registry / Retention Schedule / Deletion Triggers / Legal Hold / Data Subject Rights / Multiple |
| E | Related Data Category | 30 | Text | Link to specific data category (or "General") |
| F | Evidence Location | 40 | Text | File path, URL, document management ID |
| G | Document Date | 15 | Date | Date of evidence creation |
| H | Evidence Retention Period | 20 | Dropdown | 3 years / 5 years / 7 years / 10 years / Permanent |
| I | Access Restrictions | 25 | Dropdown | Public / Internal / Confidential / Restricted |
| J | Verified By | 20 | Text | Person who verified evidence exists |
| K | Verification Date | 15 | Date | Date evidence verified |
| L | Notes | 35 | Text | Additional context |

## Evidence ID Auto-Generation

**Formula for Column A:**
```excel
="EV-"&TEXT(ROW()-9,"000")
```

Row 10 generates: EV-001
Row 11 generates: EV-002
...
Row 109 generates: EV-100

## Data Validation Rules

**Column B - Evidence Type:**
```
Dropdown: Policy, Technical Documentation, Regulatory Document, Audit Log, Contract, Legal Opinion, Testing Result, Other
```

**Column D - Related Assessment Area:**
```
Dropdown: Data Category Registry, Retention Schedule, Deletion Triggers, Legal Hold, Data Subject Rights, Multiple
```

**Column H - Evidence Retention Period:**
```
Dropdown: 3 years, 5 years, 7 years, 10 years, Permanent
```

**Column I - Access Restrictions:**
```
Dropdown: Public, Internal, Confidential, Restricted
```

## Evidence Type Examples

**Policy:**

- ISMS-POL-A.8.10 Information Deletion Policy
- Data Retention Policy
- Data Subject Rights Procedure


**Technical Documentation:**

- Deletion trigger configuration screenshots
- Automation scripts (cron jobs, lifecycle policies)
- System architecture diagrams


**Regulatory Document:**

- GDPR Article 30 Records of Processing Activities
- FADP Article 12 Register
- Legal retention requirement analysis memo


**Audit Log:**

- Deletion execution logs (last 6 months)
- Data subject request tracking log
- Legal hold register


**Contract:**

- Data Processing Agreements with deletion clauses
- Cloud provider contracts (deletion SLAs)
- Vendor agreements


**Legal Opinion:**

- Legal Counsel memo on retention periods
- Legal hold procedure approval
- GDPR Article 17 exception analysis


**Testing Result:**

- Deletion verification test reports (from ISMS-IMP-A.8.10.4)
- Backup deletion testing results


---

# Sheet 9: Approval Sign-Off

## Purpose
Three-level approval workflow ensuring accountability for assessment findings and remediation commitments.

## Sheet Layout

**Header Section (Rows 1-10):**

- Row 1: Sheet title "9. Approval Sign-Off"
- Row 2: Purpose
- Row 3: Assessment completion summary
- Rows 5-10: Document Control metadata


**Document Control (Rows 5-10):**

- Assessment Period: [Date Range]
- Workbook Version: [e.g., 1.0]
- Total Assessment Sheets Completed: 5
- Overall Compliance %: [Link to Sheet 7]
- Critical Gaps Identified: [Count from Sheet 7]
- Assessment Completed By: [Name, Date]


**Section 1: Level 1 Approval - Technical/Operational (Rows 12-25)**

**Approver Role:** Data Protection Officer / Privacy Officer / Information Security Manager

**Approval Statement:**
*"I confirm that this assessment accurately reflects our current retention schedules and deletion trigger implementations as of [Date]. All data categories have been reviewed, gaps have been identified, and remediation plans are in place."*

| Field | Input Type |
|-------|-----------|
| Approver Name | Text entry |
| Title/Role | Text entry |
| Email | Text entry |
| Review Date | Date picker |
| Approval Status | Dropdown: ✅ Approved / ⚠️ Approved with Conditions / ❌ Rejected |
| Conditions/Comments | Text area (if applicable) |
| Signature | Text: "Electronically signed" OR physical signature space if printed |

**Section 2: Level 2 Approval - Management (Rows 27-40)**

**Approver Role:** Chief Information Security Officer / Chief Information Officer / Chief Compliance Officer

**Approval Statement:**
*"I acknowledge the findings of this A.8.10.1 assessment and approve the proposed remediation plans. Resources will be allocated to address critical and high-risk gaps within the specified timelines."*

| Field | Input Type |
|-------|-----------|
| Approver Name | Text entry |
| Title/Role | Text entry |
| Email | Text entry |
| Review Date | Date picker |
| Approval Status | Dropdown: ✅ Approved / ⚠️ Approved with Conditions / ❌ Rejected |
| Conditions/Comments | Text area |
| Signature | Text: "Electronically signed" |

**Section 3: Level 3 Approval - Executive (Rows 42-55)**

**Approver Role:** Chief Executive Officer / Chief Risk Officer / Board Delegate

**Approval Statement:**
*"This assessment has been reviewed at the executive level. The organization's retention and deletion trigger posture is [Acceptable/Needs Improvement/Unacceptable]. The Board/Executive Team has been briefed on critical gaps and remediation commitments."*

| Field | Input Type |
|-------|-----------|
| Approver Name | Text entry |
| Title/Role | Text entry |
| Email | Text entry |
| Review Date | Date picker |
| Approval Status | Dropdown: ✅ Approved / ⚠️ Approved with Conditions / ❌ Rejected |
| Executive Summary | Text area for key points communicated to Board |
| Signature | Text: "Electronically signed" |

**Section 4: Next Steps (Rows 57-68)**

| Action Item | Responsible Party | Due Date | Status |
|-------------|------------------|----------|--------|
| Implement remediation plans for critical gaps | [Name] | [Date] | Pending/In Progress/Complete |
| Quarterly progress review on remediation | [Name] | [Date] | Pending |
| Annual re-assessment of A.8.10.1 | [Name] | [Date + 1 year] | Scheduled |
| Update ISMS-POL-A.8.10 if needed | [Name] | [Date] | Pending/Not Required |
| Communicate changes to stakeholders | [Name] | [Date] | Pending |

**Section 5: Audit Trail (Rows 70-80)**

| Date | Version | Change Description | Changed By |
|------|---------|-------------------|------------|
| [Auto] | 1.0 | Initial assessment completed | [Auto-populate from Section 1] |
| [Entry] | 1.1 | [Example: Updated Sheet 3 with new retention periods] | [Name] |
| [Entry] | 1.2 | [Example: Added 5 new data categories to Sheet 2] | [Name] |

---

# Conditional Formatting Rules

## Status Column (Column F) - All Assessment Sheets

**Rule 1: Compliant Status**

- Condition: Cell value = "✅ Compliant"
- Format: Fill color RGB(198, 239, 206) - Light green
- Font: Bold, dark green


**Rule 2: Partial Status**

- Condition: Cell value = "⚠️ Partial"
- Format: Fill color RGB(255, 235, 156) - Light yellow
- Font: Bold, dark orange


**Rule 3: Non-Compliant Status**

- Condition: Cell value = "❌ Non-Compliant"
- Format: Fill color RGB(255, 199, 206) - Light red
- Font: Bold, dark red


## Risk Level Column (Column M) - All Assessment Sheets

**Rule 1: Critical Risk**

- Condition: Cell value = "Critical"
- Format: Fill color RGB(255, 199, 206) - Light red
- Font: Bold, white


**Rule 2: High Risk**

- Condition: Cell value = "High"
- Format: Fill color RGB(255, 230, 153) - Light orange
- Font: Bold, dark red


**Rule 3: Medium Risk**

- Condition: Cell value = "Medium"
- Format: Fill color RGB(255, 242, 204) - Very light yellow
- Font: Regular, black


## Summary Dashboard - Compliance Percentage

**Rule 1: Excellent (≥90%)**

- Condition: Cell value ≥ 90
- Format: Fill color RGB(198, 239, 206) - Green
- Font: Bold, dark green


**Rule 2: Acceptable (80-89%)**

- Condition: Cell value ≥ 80 AND < 90
- Format: Fill color RGB(255, 235, 156) - Yellow
- Font: Bold, dark orange


**Rule 3: Needs Improvement (70-79%)**

- Condition: Cell value ≥ 70 AND < 80
- Format: Fill color RGB(255, 230, 153) - Orange
- Font: Bold, dark red


**Rule 4: Unacceptable (<70%)**

- Condition: Cell value < 70
- Format: Fill color RGB(255, 199, 206) - Red
- Font: Bold, white


## Data Subject Rights - Average Response Time (Sheet 6, Column R)

**Rule 1: Compliant (≤30 days)**

- Condition: Cell value ≤ 30
- Format: Fill color RGB(198, 239, 206) - Green
- Font: Bold, dark green


**Rule 2: Acceptable if Complex (31-60 days)**

- Condition: Cell value > 30 AND ≤ 60
- Format: Fill color RGB(255, 235, 156) - Yellow
- Font: Bold, dark orange


**Rule 3: Non-Compliant (>60 days)**

- Condition: Cell value > 60
- Format: Fill color RGB(255, 199, 206) - Red
- Font: Bold, dark red


---

# Cell Protection & Sheet Security

## Protected Cells (Formula/Static Content)

**Applies to all sheets:**

- Column headers (Row 9)
- Instructions text (Rows 1-8)
- Reference tables and checklists
- Formula cells in Summary Dashboard
- Evidence Register ID auto-generation (Column A)


**Protection Settings:**

- Locked: Yes
- Hidden formulas: No (allow users to see calculation logic)


## Unprotected Cells (User Input Areas)

**Applies to all sheets:**

- Data entry rows (Rows 10-22 in Sheets 2-6) - Yellow fill
- Evidence Register data fields (Rows 10-109, Columns B-L)
- Approval Sign-Off fields (All approval sections)
- Notes/Comments columns (Column O, Column J, etc.)


**Protection Settings:**

- Locked: No
- Allow: Formatting, Insert rows (within data range), Delete content


## Sheet Protection Configuration

**Enable Protection on All Sheets with:**

- Password: [To be set by workbook generator]
- Allow users to:
  - [ ] Select locked cells (YES)
  - [ ] Select unlocked cells (YES)
  - [ ] Format cells (YES)
  - [ ] Format columns (NO)
  - [ ] Format rows (NO)
  - [ ] Insert columns (NO)
  - [ ] Insert rows (YES - within data entry range only)
  - [ ] Delete columns (NO)
  - [ ] Delete rows (YES - within data entry range only)
  - [ ] Sort (YES)
  - [ ] Use AutoFilter (YES)
  - [ ] Edit objects (NO)
  - [ ] Edit scenarios (NO)


---

# Summary Dashboard Formulas

## Overall Compliance Calculation

**Total Data Categories Assessed:**
```excel
=COUNTA(Sheet2!A10:A22)
```

**Data Categories Compliant:**
```excel
=COUNTIF(Sheet2!F10:F22,"✅ Compliant")
```

**Data Categories Partial:**
```excel
=COUNTIF(Sheet2!F10:F22,"⚠️ Partial")
```

**Data Categories Non-Compliant:**
```excel
=COUNTIF(Sheet2!F10:F22,"❌ Non-Compliant")
```

**Overall Compliance %:**
```excel
=IF((COUNTA(Sheet2!F10:F22)-COUNTIF(Sheet2!F10:F22,"N/A"))=0,0,
   COUNTIF(Sheet2!F10:F22,"✅ Compliant")/
   (COUNTA(Sheet2!F10:F22)-COUNTIF(Sheet2!F10:F22,"N/A"))*100)
```

## Critical Gaps Count

**Critical and High Risk Non-Compliant Items:**
```excel
=COUNTIFS(Sheet2!F10:F22,"❌ Non-Compliant",Sheet2!M10:M22,"Critical")+
 COUNTIFS(Sheet2!F10:F22,"❌ Non-Compliant",Sheet2!M10:M22,"High")
```

## Data Categories Without Retention Schedules

**Count of Missing Retention Periods:**
```excel
=COUNTBLANK(Sheet3!D10:D22)
```

## Data Categories Without Deletion Triggers

**Count from Sheet 4 Non-Compliant:**
```excel
=COUNTIF(Sheet4!F10:F22,"❌ Non-Compliant")
```

## Data Subject Rights Performance

**Average Response Time:**
```excel
=AVERAGE(Sheet6!R10:R22)
```

**Requests Exceeding 30 Days:**
```excel
=COUNTIF(Sheet6!R10:R22,">30")
```

**Total Requests (Last 12 Months):**
```excel
=SUM(Sheet6!T10:T22)
```

---

# Python Script Integration

## Script Purpose

The Python script `generate_a810_1_retention_triggers.py` generates the complete Excel workbook based on this specification.

## Key Script Functions

**Function: `create_workbook()`**

- Initialize openpyxl Workbook object
- Create all 9 sheets
- Set default font (Calibri 11)
- Return workbook object


**Function: `setup_styles()`**

- Define cell styles: header, subheader, input_cell, status_compliant, status_partial, status_noncompliant
- Define fills: green, yellow, red, gray, blue
- Define borders: thin, medium
- Return style dictionary


**Function: `create_instructions_sheet(wb, styles)`**

- Add Instructions & Legend content
- Format headers, color legend, status definitions
- Freeze panes at Row 9


**Function: `create_assessment_sheet(wb, styles, sheet_name, sheet_number)`**

- Generic function to create Sheets 2-6
- Apply column definitions (A-Q standard, R-T extended)
- Add data validation dropdowns
- Apply conditional formatting
- Add reference tables/checklists
- Freeze panes at Row 9


**Function: `create_summary_dashboard(wb, styles)`**

- Create Sheet 7 structure
- Add formulas for compliance calculations
- Apply conditional formatting to compliance %
- Add critical gaps table (formula-driven)


**Function: `create_evidence_register(wb, styles)`**

- Create Sheet 8 with 100 data rows
- Add Evidence ID auto-generation formula
- Apply data validation for dropdowns
- Freeze panes at Row 9


**Function: `create_approval_signoff(wb, styles)`**

- Create Sheet 9 with 3-level approval workflow
- Add Document Control section
- Add Next Steps and Audit Trail sections
- Format approval tables


**Function: `apply_data_validation(sheet, cell_range, dropdown_values)`**

- Generic function to apply dropdown validation
- Used for all dropdown columns


**Function: `apply_conditional_formatting(sheet, cell_range, rules)`**- Generic function to apply conditional formatting

- Used for status columns, risk level, compliance %


## Customization Points (Marked with `# CUSTOMIZE:` in Script)

**Dropdown Options:**

- Data Classification values (if organization uses different scheme)
- Retention Period options (if additional periods needed)
- Legal/Regulatory Basis values (if industry-specific regulations)


**Conditional Formatting Thresholds:**

- Compliance % thresholds (currently 90%, 80%, 70%)
- Response time thresholds (currently 30, 60 days)


**Sheet Names:**

- If organizational naming conventions differ from standard


**Column Widths:**

- Adjust if organization prefers different layout


**Data Entry Row Count:**

- Currently 13 rows, increase if needed (but recommend pagination to new workbook)


## Script Execution

**Command:**
```bash
python generate_a810_1_retention_triggers.py
```

**Output:**

- Filename: `ISMS-IMP-A.8.10.1_Retention_Triggers_YYYYMMDD.xlsx`
- Location: Current working directory
- Success message with workbook structure summary


**Validation:**

- Open workbook in Excel
- Verify all 9 sheets present
- Test dropdowns in assessment sheets
- Verify formulas calculate correctly in Summary Dashboard
- Check conditional formatting applies properly


---

# Quality Assurance

## Pre-Delivery Checklist

Before delivering workbook to users, verify:

**Structure:**

- [ ] All 9 sheets present and correctly named
- [ ] Sheet tab colors applied (per specification)
- [ ] Freeze panes configured (Row 9 on all assessment sheets)


**Content:**

- [ ] Instructions sheet complete with color legend
- [ ] All reference tables populated
- [ ] Column headers match specification
- [ ] Evidence Register has 100 rows


**Functionality:**

- [ ] All dropdowns working (test each column)
- [ ] Conditional formatting applies correctly (enter test values)
- [ ] Summary Dashboard formulas calculate (no #REF! errors)
- [ ] Evidence ID auto-generates (EV-001, EV-002, etc.)


**Protection:**

- [ ] Formula cells protected
- [ ] Data entry cells unlocked (yellow fill)
- [ ] Sheet protection enabled with correct permissions
- [ ] Password set (if required)


**Formatting:**

- [ ] Column widths appropriate (no truncated headers)
- [ ] Status indicators visible (✅ ⚠️ ❌)
- [ ] Print areas defined
- [ ] Page breaks logical


## User Acceptance Testing

**Test Scenarios:**

**Scenario 1: Complete Data Category Assessment**
1. User enters 5 data categories in Sheet 2
2. User copies to Sheet 3, assigns retention periods
3. User documents deletion triggers in Sheet 4
4. Summary Dashboard updates automatically
5. User links evidence in Sheet 8
6. User completes approval workflow in Sheet 9

**Expected Outcome:** All formulas work, conditional formatting applies, no errors.

**Scenario 2: Identify Critical Gaps**
1. User marks 2 data categories as ❌ Non-Compliant with Risk Level = Critical
2. Summary Dashboard Critical Gaps section auto-populates
3. Overall Compliance % reflects non-compliance

**Expected Outcome:** Dashboard accurately reflects findings.

**Scenario 3: Data Subject Rights Performance**
1. User enters response times in Sheet 6 (mix of <30, 30-60, >60 days)
2. Conditional formatting colors cells appropriately
3. Summary Dashboard calculates average response time

**Expected Outcome:** Performance metrics accurate, color coding correct.

---

# Integration with Other A.8.10 Assessments

## Assessment Dependencies

**ISMS-IMP-A.8.10.1 (This Assessment) Feeds Into:**

- **ISMS-IMP-A.8.10.2 (Deletion Methods):** Retention schedules defined here → Deletion methods assessed there
- **ISMS-IMP-A.8.10.3 (Third-Party Deletion):** Data categories identified here → Third-party deletion assessed there
- **ISMS-IMP-A.8.10.4 (Verification & Evidence):** Deletion triggers defined here → Verification testing there
- **ISMS-IMP-A.8.10.5 (Compliance Dashboard):** All findings aggregated into overall A.8.10 compliance posture


## Data Flow Between Assessments

```
A.8.10.1 Retention Triggers
    ↓ (Data categories, retention periods)
A.8.10.2 Deletion Methods
    ↓ (Deletion methods by media type)
A.8.10.3 Third-Party Deletion
    ↓ (Cloud provider deletion capabilities)
A.8.10.4 Verification & Evidence
    ↓ (Verification test results)
A.8.10.5 Compliance Dashboard
    ↓ (Overall A.8.10 compliance status)
```

## Cross-Reference Requirements

**Evidence Register (Sheet 8) Should Link:**

- Retention schedule approvals → Referenced in A.8.10.1
- Deletion method testing → Referenced in A.8.10.2
- Cloud provider contracts → Referenced in A.8.10.3
- Verification test reports → Referenced in A.8.10.4


---

# Version Control & Change Management

## Workbook Versioning

**Filename Format:**
```
ISMS-IMP-A.8.10.1_Retention_Triggers_YYYYMMDD.xlsx
```

**Example:** `ISMS-IMP-A.8.10.1_Retention_Triggers_20260119.xlsx`

**Version Tracking in Instructions Sheet:**

- Document ID: ISMS-IMP-A.8.10.1
- Version: 1.0
- Date: [Date]


## Change Log

**Version 1.0 → 2.0 Changes:**

- Added PART I: USER COMPLETION GUIDE (comprehensive user documentation)
- Enhanced PART II: TECHNICAL SPECIFICATION (detailed Excel structure)
- Improved GDPR Article 17 / FADP alignment in Sheet 6
- Added Legal Hold Management as separate assessment area (Sheet 5)
- Enhanced Evidence Register with 100 rows (previously 50)
- Strengthened Approval Sign-Off with Executive-level summary
- Updated compliance calculation formulas for accuracy
- Added conditional formatting for response time performance


## Backward Compatibility

**v2.0 Workbooks:**

- Can be opened in Excel 2016+
- Compatible with LibreOffice Calc 6.0+ (with minor formatting differences)
- Not compatible with Google Sheets (use Excel Online for cloud access)


**v1.0 to v2.0 Migration:**

- Manual data transfer required (no automated migration script)
- Copy data categories from v1.0 Sheet 2 → v2.0 Sheet 2
- Re-assess additional columns (R, S, T) in v2.0 format
- Update Evidence Register with new entries


---

# Support & Troubleshooting

## Common Issues

**Issue 1: Formulas Show #REF! Error**

- Cause: Sheet names changed or rows deleted
- Solution: Check formula references point to correct sheets/ranges
- Prevention: Don't rename sheets or delete header rows


**Issue 2: Dropdowns Not Working**

- Cause: Data validation not applied or sheet protection blocks editing
- Solution: Verify data validation rules, check cell is unlocked
- Prevention: Use script-generated workbook, don't manually recreate


**Issue 3: Conditional Formatting Not Applying**

- Cause: Rule range incorrect or conflicting rules
- Solution: Review conditional formatting rules, ensure range covers data rows
- Prevention: Test with sample data before distribution


**Issue 4: Summary Dashboard Shows 0% Compliance**

- Cause: No data entered in assessment sheets OR formulas reference wrong range
- Solution: Enter at least one data category, verify formulas reference Rows 10-22
- Prevention: Complete at least Sheet 2 before reviewing dashboard


## Technical Support

**For Python Script Issues:**

- Review error messages in console output
- Verify openpyxl library installed (`pip install openpyxl`)
- Check Python version (requires 3.7+)
- Contact: ISMS Implementation Team


**For Excel Workbook Issues:**

- Verify Excel version (2016+ required)
- Check file not corrupted (re-generate from script)
- Review cell protection settings
- Contact: ISMS Implementation Team


---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Document Assembly Instructions

**To create the complete ISMS-IMP-A.8.10.1 v1.0 document:**

1. **Document Control + PART I: USER COMPLETION GUIDE** (Deliverable 1)
2. **PART II: TECHNICAL SPECIFICATION** (Deliverable 2, this file)

**Final Document Structure:**
```
ISMS-IMP-A.8.10.1 - Retention & Deletion Triggers Assessment v1.0

├── Document Control (Metadata, Version History)
│
├── PART I: USER COMPLETION GUIDE (~2,200 lines)
│   ├── 1. Assessment Overview
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
    ├── 2. Sheet 1: Instructions & Legend
    ├── 3. Sheet 2: Data Category Registry
    ├── 4. Sheet 3: Retention Schedule Compliance
    ├── 5. Sheet 4: Deletion Trigger Configuration
    ├── 6. Sheet 5: Legal Hold Management
    ├── 7. Sheet 6: Data Subject Rights
    ├── 8. Sheet 7: Summary Dashboard
    ├── 9. Sheet 8: Evidence Register
    ├── 10. Sheet 9: Approval Sign-Off
    ├── 11. Conditional Formatting Rules
    ├── 12. Cell Protection & Sheet Security
    ├── 13. Summary Dashboard Formulas
    ├── 14. Python Script Integration
    ├── 15. Quality Assurance
    ├── 16. Integration with Other A.8.10 Assessments
    ├── 17. Version Control & Change Management
    └── 18. Support & Troubleshooting
```

**Quality Checks Before Finalizing:**

- [ ] All section references accurate (no broken cross-references)
- [ ] Document Control version shows 2.0
- [ ] Version History documents v1.0 → v2.0 changes
- [ ] All dates in DD.MM.YYYY format
- [ ] Consistent use of [Organization] placeholder
- [ ] No placeholder text remains incomplete
- [ ] Technical specification matches Python script capability


---

**END OF SPECIFICATION**

---

*"Bell's theorem and the experiments it inspired have taught us that nature is not locally realistic in the way Einstein hoped."*
— Alain Aspect

*Where bamboo antennas actually work.* 🎋
