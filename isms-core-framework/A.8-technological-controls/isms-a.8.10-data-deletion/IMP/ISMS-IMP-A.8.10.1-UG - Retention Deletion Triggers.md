<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.10.1-UG:framework:UG:a.8.10.1 -->
**ISMS-IMP-A.8.10.1-UG - Retention & Deletion Triggers Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Retention Deletion Triggers |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.10.1-UG |
| **Related Policy** | ISMS-POL-A.8.10 (Data Deletion) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.10 (Information Deletion) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.8.10 (Data Deletion)
- ISMS-IMP-A.8.10.2 (Deletion Methods Assessment)
- ISMS-IMP-A.8.10.3 (Third-Party & Cloud Deletion Assessment)
- ISMS-IMP-A.8.10.4 (Verification & Evidence Assessment)

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | 2. Data Category Registry | Catalogue all data categories and their retention requirements |
| 3 | 3. Retention Sched. Compliance | Assess compliance with retention schedule requirements |
| 4 | 4. Deletion Trigger Config. | Document and evaluate deletion trigger mechanisms |
| 5 | 5. Legal Hold Management | Manage legal holds that suspend deletion obligations |
| 6 | 6. Data Subject Requests | Track and manage data subject erasure requests |
| 7 | Evidence Register | Store and reference evidence supporting assessments |
| 8 | Summary Dashboard | Compliance status and key metrics overview |
| 9 | Approval Sign-Off | Management review sign-off and certification |

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organisation]'s implementation of **data retention schedules and deletion trigger mechanisms** to ensure compliance with ISO/IEC 27001:2022 Control A.8.10, applicable data protection regulations (GDPR, FADP), and industry-specific retention requirements.

**Scope:** Complete data lifecycle management across 5 critical areas:

1. **Data Category Registry** - Complete inventory of all data types processed by [Organisation]
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

- [Organisation]'s complete data inventory and classification scheme
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

**Total Assessment Time:** 8-12 hours (depending on data complexity and organisational size)

**Breakdown:**

- **Data Category Inventory (2-3 hours):** Identify and document all data types processed
- **Retention Schedule Review (2-3 hours):** Map legal/regulatory requirements to each category
- **Deletion Trigger Assessment (2-3 hours):** Document automated and manual deletion mechanisms
- **Legal Hold & Data Subject Rights (1-2 hours):** Review procedures and metrics
- **Evidence Collection (1-2 hours):** Gather supporting documentation
- **Quality Review (1 hour):** Final validation and approval preparation

**Pro Tip:** For complex organisations with >50 data categories, consider conducting assessment over multiple sessions (e.g., one session per business unit or system).

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

- Data classification scheme in use at [Organisation]
- Business processes that generate and consume data
- Records management principles
- Data subject rights request handling

## Pre-Assessment Checklist

Complete these tasks before beginning the assessment:

- [ ] **Gather existing retention schedules** (if any) from Legal, Compliance, or Records Management
- [ ] **Review GDPR Article 30 records** or equivalent data processing documentation
- [ ] **Identify all major data systems** (applications, databases, file shares, cloud storage)
- [ ] **Schedule meetings with Business Unit Owners** to validate data categories
- [ ] **Confirm regulatory requirements** applicable to [Organisation] with Legal Counsel
- [ ] **Review any active legal holds** or litigation requirements
- [ ] **Collect metrics** on data subject erasure requests (last 12 months)
- [ ] **Document backup retention policies** to ensure alignment with production retention

**Critical:** If [Organisation] has never conducted a formal data inventory or created retention schedules, allow additional time (20-30 hours) for foundational work before completing this assessment.

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

**Objective:** Document every type of data processed by [Organisation]

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

- Does overall compliance % reflect your understanding of [Organisation]'s posture?
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

Balance: Verification must be sufficient to prevent unauthorised deletion, but not so burdensome it obstructs legitimate requests.

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

- Access controls: Limited to ISMS team, auditors, authorised personnel
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

- [ ] Data classifications match [Organisation]'s classification scheme
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
3. **Gap Analysis:** Do identified gaps align with your understanding of [Organisation]'s posture?
4. **Evidence Check:** Can you locate all referenced evidence documents?
5. **Stakeholder Validation:** Share draft with 2-3 Business Unit Owners for feedback

## Approval Workflow (Sheet 9)

**Level 1: Technical/Operational Approval**

- **Approver:** Data Protection Officer / Privacy Officer / Information Security Manager
- **Validates:** Technical accuracy, completeness of data inventory, deletion trigger feasibility
- **Approval Criteria:** Assessment accurately reflects current state of [Organisation]'s retention posture

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

**END OF USER GUIDE**

---

*"Keeping data beyond its useful life is not preservation; it is accumulation of liability."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
