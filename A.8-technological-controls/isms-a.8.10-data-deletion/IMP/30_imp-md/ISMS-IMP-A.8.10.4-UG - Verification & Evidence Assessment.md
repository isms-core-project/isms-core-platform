**ISMS-IMP-A.8.10.4-UG - Verification & Evidence Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.10.4-UG |
| **Version** | 1.0 |
| **Assessment Area** | Deletion Verification Procedures & Evidence Quality |
| **Related Policy** | ISMS-POL-A.8.10, Section 2.4 (Verification & Evidence Requirements) |
| **Purpose** | Assess organizational capability to prove information deletion occurred while respecting data minimization principles |
| **Target Audience** | Information Security Officers, Compliance Officers, Audit Managers, IT Operations, Legal Counsel, Data Protection Officers, Internal/External Auditors |
| **Assessment Type** | Technical & Operational Compliance with Audit Focus |
| **Review Cycle** | Quarterly (minimum) or After Major Deletion Events |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Verification & Evidence assessment workbook | ISMS Implementation Team |

---

**Audience:** Information Security Officers, Compliance Officers, Audit Managers, IT Operations, Legal Counsel

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organization]'s **capability to prove information deletion occurred** through systematic verification procedures and evidence management, addressing the fundamental challenge: *How do you prove you deleted something without keeping the thing you deleted?*

**Scope:** Complete verification and evidence infrastructure across 5 critical areas:

1. **Deletion Logging Assessment** - Centralized audit trail infrastructure and completeness
2. **Verification Testing Program** - Forensic testing of deletion methods using test datasets
3. **Evidence Repository Assessment** - Secure storage, retention, and access control for deletion evidence
4. **Certificate Management** - Validation and quality assessment of third-party deletion certificates
5. **Audit Trail Completeness** - Reconstruction capability and chain of custody verification

**Assessment Output:** Excel workbook with ~200-300 data points documenting current verification capabilities, evidence quality, forensic testing effectiveness, and audit readiness status.

## Why This Matters

**ISO 27001:2022 Control A.8.10 Requirement:**
> *"Information stored in information systems, devices or in any other storage media should be deleted when no longer required."*

**The Verification Paradox:**

Organizations must prove deletion occurred **without retaining the deleted data itself**. This creates a fundamental challenge:

- ❌ **Wrong Approach:** Keep copies of deleted data to prove deletion → Violates data minimization
- ❌ **Wrong Approach:** Keep no evidence → Cannot prove compliance to auditors
- ✅ **Correct Approach:** Retain **metadata about deletion** (who/what/when/how) + test deletion **methods** (not actual data)

**Regulatory Context:**

- **EU GDPR (Article 5.1.f):** "Integrity and confidentiality" principle - organizations must demonstrate data processing security including deletion
- **EU GDPR (Article 17):** "Right to erasure" - organizations must provide evidence of deletion to data subjects on request
- **EU GDPR (Article 30):** "Records of processing activities" - deletion records are part of compliance documentation
- **Swiss FADP (Article 7):** Data security principle - deletion must be demonstrably effective
- **ISO 27001 Clause 9.1:** "Monitoring, measurement, analysis and evaluation" - deletion effectiveness must be measurable

**Business Impact:**

- **Audit Failures:** Without verifiable evidence, ISO 27001 certification audits may fail A.8.10 compliance
- **Regulatory Fines:** GDPR enforcement actions require proof of deletion - absence of evidence = €20M fines or 4% annual turnover
- **Legal Liability:** Data breach investigations examine whether "deleted" data was truly deleted - weak verification = extended liability
- **Operational Efficiency:** Systematic verification prevents "delete but not really deleted" scenarios (data in backups, archives, shadow IT)
- **Trust & Reputation:** Customers/partners increasingly require deletion certificates and audit evidence as part of due diligence

## Who Should Complete This Assessment

**Primary Responsibility:** Information Security Officer / Compliance Officer

**Required Knowledge:**

- [Organization]'s deletion logging infrastructure (SIEM, audit logs, application logs)
- Forensic testing methodologies (NIST SP 800-88, data remanence analysis)
- Evidence repository systems (where deletion certificates, logs, test results are stored)
- Audit requirements for ISO 27001, GDPR, FADP, and industry-specific regulations
- Third-party vendor certificate validation procedures

**Support Roles:**

- **IT Operations:** For deletion logging system configuration and forensic test execution
- **Audit Manager:** For evidence quality standards and audit trail requirements
- **Legal Counsel:** For evidence retention periods and litigation hold implications
- **Data Protection Officer:** For GDPR Article 17 erasure evidence requirements
- **External Auditors:** For certification audit evidence acceptance criteria (if available)
- **Forensic Specialists:** For deletion method testing and verification procedures (if in-house capability exists)

## Time Estimate

**Total Assessment Time:** 10-15 hours (depending on verification infrastructure maturity)

**Breakdown:**

- **Deletion Logging Assessment (2-3 hours):** Review log infrastructure, completeness, retention
- **Verification Testing Program (3-4 hours):** Document forensic test procedures, results, coverage
- **Evidence Repository Assessment (2-3 hours):** Evaluate storage systems, access controls, retention policies
- **Certificate Management (2-3 hours):** Review third-party certificates, validation procedures
- **Audit Trail Completeness (1-2 hours):** Test reconstruction capability, chain of custody
- **Evidence Collection (1-2 hours):** Gather supporting documentation
- **Quality Review (1 hour):** Final validation and approval preparation

**Pro Tip:** If [Organization] has no formal verification testing program, the assessment will reveal this gap quickly (~2 hours). The remaining time should be spent documenting current ad-hoc verification practices and planning remediation.

## Connection to Policy

This assessment implements **ISMS-POL-A.8.10, Section 2.4 (Verification & Evidence Requirements)** which defines mandatory requirements for:

- **Deletion Logging:** All deletion events must generate audit log entries with required metadata
- **Verification Testing:** Deletion methods must be tested periodically using forensic analysis of test datasets
- **Evidence Repository:** Deletion evidence must be stored securely with access controls and retention schedules
- **Certificate Validation:** Third-party deletion certificates must be validated for completeness and authenticity
- **Audit Trail:** Complete reconstruction of "who deleted what, when, how, and with what result" must be possible

**Policy Authority:** Chief Information Security Officer (CISO) / Compliance Officer  
**Compliance Status:** Mandatory for all systems processing personal data, confidential data, or data subject to regulatory retention requirements

## Connection to Other A.8.10 Assessments

**Prerequisites (Must Complete First):**

- **A.8.10.1 (Retention & Deletion Triggers):** Defines evidence retention periods for deletion logs/certificates
- **A.8.10.2 (Deletion Methods):** Identifies which deletion methods require verification testing
- **A.8.10.3 (Third-Party & Cloud):** Identifies vendors from whom deletion certificates must be obtained

**Dependencies:**

- **From A.8.10.1:** Evidence retention schedules (typically 7 years for deletion logs per Swiss OR)
- **From A.8.10.2:** List of deletion methods requiring forensic verification (e.g., crypto-erasure, SSD sanitization)
- **From A.8.10.3:** Vendor list requiring certificate validation and deletion SLA monitoring

**Feeds Into:**

- **A.8.10.5 (Compliance Dashboard):** Verification metrics, audit readiness score, evidence quality ratings

---

# Prerequisites

## Access Required

Before starting this assessment, ensure you have access to:

**Systems:**

- [ ] Centralized logging system (SIEM, log aggregation platform)
- [ ] Evidence repository / document management system (where deletion certificates are stored)
- [ ] Forensic testing lab or test environment (if verification testing is performed)
- [ ] Backup and archive systems (to verify deletion from these systems as well)
- [ ] Third-party vendor portals (to retrieve deletion certificates)

**Documentation:**

- [ ] Deletion logging policy and configuration standards
- [ ] Forensic testing procedures (if documented)
- [ ] Evidence retention policy (from ISMS-POL-A.8.10, Section 2.4 (Verification & Evidence Requirements))
- [ ] List of third-party vendors with deletion SLAs (from A.8.10.3 assessment)
- [ ] Previous deletion verification test results (if available)
- [ ] Audit findings related to deletion verification (if any)

**Subject Matter Experts:**

- [ ] IT Operations (for logging system configuration)
- [ ] Security Operations (for log analysis and forensic testing)
- [ ] Compliance Team (for evidence quality standards)
- [ ] External Auditor (for audit trail acceptance criteria - if available)

## Required Knowledge

**Technical:**

- Understanding of audit log formats and centralized logging architectures
- Familiarity with forensic analysis concepts (data remanence, sanitization verification)
- Basic understanding of NIST SP 800-88 verification methodologies
- Knowledge of cryptographic deletion verification (if crypto-erasure is used)

**Regulatory & Compliance:**

- Understanding of GDPR Article 17 evidence requirements for erasure requests
- Familiarity with ISO 27001 Clause 9.1 monitoring and measurement requirements
- Knowledge of evidence retention requirements (Swiss OR, GDPR Article 30)
- Audit trail best practices for compliance audits

**Operational:**

- How [Organization] currently logs deletion events (if at all)
- Where deletion evidence is stored and who has access
- Whether forensic testing is performed and by whom
- How third-party deletion certificates are validated (if at all)

## Tools & Resources

**Assessment Tools:**

- Excel workbook: ISMS-IMP-A.8.10.4_Verification_Evidence_YYYYMMDD.xlsx (generated by Python script)
- NIST SP 800-88 Rev. 1: Guidelines for Media Sanitization (Appendix A - Verification)
- GDPR Article 17 guidance: Evidence of erasure requirements

**Reference Materials (Included in Workbook):**

- Log completeness checklist (20 required fields)
- Forensic testing effectiveness criteria
- Certificate quality scoring rubric
- Audit trail reconstruction test procedure

---

# Assessment Workflow

## Recommended Completion Sequence

**Phase 1: Information Gathering (2-3 hours)**

1. **Sheet 2 - Deletion Logging Assessment**

   - Identify centralized logging system(s) in use
   - Review log configuration for deletion events
   - Check log retention periods against policy requirements
   - Document tamper protection mechanisms (if any)
   - Assess log completeness using 20-item checklist

2. **Sheet 3 - Verification Testing Program**

   - Document whether forensic testing is performed
   - Review testing procedures and frequency
   - Analyze recent test results (pass/fail rates)
   - Identify which deletion methods are tested vs. untested
   - Assess testing coverage against NIST SP 800-88 requirements

**Phase 2: Evidence Quality Assessment (3-4 hours)**

3. **Sheet 4 - Evidence Repository Assessment**

   - Identify where deletion evidence is stored (document management system, file shares, etc.)
   - Review access controls (who can view/modify evidence)
   - Check evidence retention periods alignment with policy
   - Assess evidence integrity protection (versioning, audit trails)
   - Document backup and disaster recovery for evidence repository

4. **Sheet 5 - Certificate Management**

   - Review third-party deletion certificates received
   - Assess certificate quality using scoring rubric
   - Document certificate validation procedures (or lack thereof)
   - Check certificate retention and accessibility
   - Identify vendors with missing or low-quality certificates

**Phase 3: Audit Readiness Testing (2-3 hours)**

5. **Sheet 6 - Audit Trail Completeness**

   - Conduct sample audit trail reconstruction test
   - Verify chain of custody for deletion events
   - Test ability to answer: "Prove data X was deleted on date Y"
   - Assess time required to produce evidence for auditor
   - Document gaps in reconstruction capability

**Phase 4: Summary & Evidence (2-3 hours)**

6. **Sheet 7 - Verification Dashboard**

   - Review auto-calculated summary metrics
   - Validate scoring accuracy
   - Identify top 3 critical gaps
   - Document remediation priorities

7. **Sheet 8 - Evidence Register**

   - Document all evidence collected during assessment
   - Link evidence to specific findings
   - Ensure evidence is accessible for audit

8. **Sheet 9 - Approval Sign-Off**

   - Complete three-level approval workflow
   - Attach supporting evidence
   - Archive completed assessment

## Parallel vs. Sequential Approach

**Sequential (Recommended for First Assessment):**

- Complete Sheets 2-6 in order
- Easier to understand verification infrastructure holistically
- Allows learning from early sheets to inform later sheets

**Parallel (For Mature Organizations):**

- Assign different team members to different sheets
- Faster completion (5-7 hours total with 3+ people)
- Requires pre-coordination to avoid duplicate effort

---

# Question-by-Question Guidance

## Sheet 2: Deletion Logging Assessment (13 Assessment Rows)

**Purpose:** Evaluate whether [Organization] has comprehensive, tamper-evident deletion logs that can support audit trail reconstruction.

**Key Questions Assessors Struggle With:**

**Q: "What if we don't have a centralized logging system?"**

- A: Document current state as "Not Implemented" in Column B
- Note in Column Q: "Deletion logs scattered across applications/systems"
- Mark Gap Severity (Column D) as "High" or "Critical"
- This is a common finding for organizations starting A.8.10 implementation

**Q: "How complete do logs need to be to score 'Good' in Evidence Quality (Column F)?"**

- A: Use the 20-item checklist in the reference table below the assessment rows
- "Good" = 16-20 items captured (80%+)
- "Fair" = 11-15 items captured (55-79%)
- "Poor" = 6-10 items captured (30-54%)
- "None" = <6 items captured (<30%)

**Q: "What's the difference between 'Tamper Protection' values?"**

- A: Column U dropdown explained:
  - **None:** Logs stored in files/databases with no integrity protection
  - **Basic:** File permissions or database access controls only
  - **Advanced:** Cryptographic signing (e.g., syslog-ng crypto signatures)
  - **Immutable:** WORM storage, blockchain, or append-only systems
  - **N/A:** Not applicable (e.g., no logging system exists yet)

**Q: "Should we assess deletion logs from third-party vendors (e.g., cloud providers)?"**

- A: **No** - Third-party deletion logging is assessed in Sheet 5 (Certificate Management)
- Sheet 2 focuses on [Organization]'s own logging infrastructure
- However, if [Organization] ingests vendor logs into a centralized SIEM, assess that integration here

**Common Mistakes to Avoid:**

1. ❌ **Confusing deletion logs with general audit logs**

   - Deletion logs must specifically capture deletion events
   - General "data access" logs are not sufficient

2. ❌ **Assuming application-level logging is sufficient**

   - Application logs may not survive application deletion/decommissioning
   - Centralized logging ensures logs outlive the systems they monitor

3. ❌ **Forgetting to assess log retention periods**

   - Logs must be retained per ISMS-POL-A.8.10, Section 2.1 (Retention & Deletion Triggers) schedules (typically 7 years)
   - 30-day log retention = audit failure

## Sheet 3: Verification Testing Program (13 Assessment Rows)

**Purpose:** Evaluate whether [Organization] performs forensic testing to verify deletion methods actually work.

**The Core Concept:**

Instead of testing whether production data was deleted (which requires keeping the production data), test whether the **deletion method** works by:
1. Creating test datasets with known characteristics
2. Applying the deletion method to the test data
3. Using forensic tools to verify no data remnants remain
4. Documenting test results as evidence that the method is effective

**Key Questions Assessors Struggle With:**

**Q: "We've never done forensic testing. How do I complete this sheet?"**

- A: Document "Not Implemented" for all rows in Column B (Current State)
- This is a **critical gap** that many organizations have
- Mark Gap Severity (Column D) as "High" - forensic testing is mandatory per NIST SP 800-88
- Use Assessor Notes (Column Q) to propose testing program: "Recommend engaging third-party forensic lab or developing in-house capability"

**Q: "What's the minimum testing frequency to be compliant?"**

- A: Per NIST SP 800-88 and ISMS-POL-A.8.10, Section 2.4 (Verification & Evidence Requirements):
  - **Initial validation:** Test each deletion method before production use
  - **Periodic verification:** Re-test annually or after method/system changes
  - **Incident-driven:** Re-test if deletion failure suspected

**Q: "Who performs forensic testing - IT Operations or external labs?"**

- A: Either approach is acceptable:
  - **In-house:** Requires forensic tools (e.g., EnCase, FTK, dd, hdparm) and trained staff
  - **External:** Third-party forensic labs provide certificates of sanitization
  - Document approach in Column I (Responsible Party)

**Q: "What's considered a 'pass' for a forensic test?"**

- A: Per NIST SP 800-88:
  - **Hard Drives:** No data recoverable via hex editor/forensic tools after overwrite
  - **SSDs:** Verify crypto-erase completed (if using encryption) or physical destruction
  - **Cloud/VMs:** Verify no snapshots/backups remain post-deletion
  - Failure = ANY remnant data discoverable = method is ineffective

**Common Mistakes to Avoid:**

1. ❌ **Confusing vendor certification with forensic testing**

   - Vendor certificates (e.g., "AWS says they deleted it") ≠ forensic verification
   - Forensic testing requires [Organization] or third-party lab to verify

2. ❌ **Testing only hard drives, ignoring SSDs**

   - SSDs require different verification approaches (crypto-erasure validation or destruction)
   - Testing HDD methods on SSDs = false confidence

3. ❌ **One-time testing years ago**

   - Testing results expire (systems change, methods degrade)
   - Annual re-testing is minimum per NIST SP 800-88

## Sheet 4: Evidence Repository Assessment (13 Assessment Rows)

**Purpose:** Evaluate whether [Organization] securely stores deletion evidence with proper access controls and retention.

**Key Questions Assessors Struggle With:**

**Q: "What counts as 'deletion evidence' that needs to be stored?"**

- A: Evidence includes:
  - Deletion logs (from Sheet 2 assessment)
  - Forensic test reports (from Sheet 3 assessment)
  - Third-party deletion certificates (from Sheet 5 assessment)
  - Data subject erasure request records (GDPR Article 17)
  - Legal hold suspension records
  - Audit trail queries/reports

**Q: "Where should evidence be stored?"**

- A: Acceptable options (document actual approach in Column Q):
  - Document management system with access controls
  - Dedicated compliance evidence repository
  - Secure file share with versioning and audit trails
  - Records management system (RMS)
  - Unacceptable: Personal drives, email attachments, uncontrolled file shares

**Q: "How long must we retain deletion evidence?"**

- A: Per ISMS-POL-A.8.10, Section 2.1 (Retention & Deletion Triggers) and applicable regulations:
  - **Minimum:** Same as original data retention period (e.g., 7 years for accounting records per Swiss OR)
  - **GDPR compliance:** Evidence may be needed for 3+ years after deletion to defend against enforcement actions
  - **Best practice:** 7 years for most deletion evidence
  - Document retention period in Column S (Log Retention Period)

**Q: "Who should have access to the evidence repository?"**

- A: Access should be restricted to:
  - Compliance/Audit team (read/write)
  - Legal counsel (read)
  - External auditors (read, time-limited)
  - NOT general IT staff, NOT business users
  - Document in Column I (Responsible Party) and assess access controls

**Common Mistakes to Avoid:**

1. ❌ **Storing evidence in the same system as the deleted data**

   - If the system is decommissioned, evidence is lost
   - Evidence repository must be independent and long-lived

2. ❌ **No backups of the evidence repository**

   - Evidence loss = unable to prove compliance
   - Evidence repository must have backup/DR per Sheet 4 checklist

3. ❌ **Deleting deletion evidence too early**

   - "We deleted the logs about deletions" = audit failure
   - Evidence retention must match or exceed original data retention

## Sheet 5: Certificate Management (13 Assessment Rows)

**Purpose:** Evaluate quality and validation of third-party deletion certificates.

**Key Questions Assessors Struggle With:**

**Q: "What's a 'good' deletion certificate vs. a 'bad' one?"**

- A: Certificate quality scoring rubric (in reference table):
  - **Excellent (5 points):** Certificate includes: vendor name, date, data type, deletion method, NIST category, authorized signature, unique certificate ID
  - **Good (4 points):** Missing 1-2 minor elements (e.g., certificate ID)
  - **Fair (3 points):** Generic certificate with minimal detail
  - **Poor (2 points):** Email confirmation only ("we deleted it")
  - **None (1 point):** No certificate provided

**Q: "How do we validate certificates are authentic?"**

- A: Validation procedures should include:
  - Verify certificate signature matches vendor contact
  - Check certificate ID against vendor portal (if available)
  - Confirm deletion date aligns with contract SLA
  - Store original certificate (not just screenshot/summary)
  - Document validation in Column Q (Assessor Notes)

**Common Mistakes to Avoid:**

1. ❌ **Accepting email confirmations as sufficient**

   - "Data deleted per your request" email ≠ formal certificate
   - Formal certificates are signed, dated, with method details

2. ❌ **Not requesting certificates from vendors**

   - Assumption: "They deleted it per contract" without evidence
   - Always request formal deletion certificate

## Sheet 6: Audit Trail Completeness (13 Assessment Rows)

**Purpose:** Test ability to reconstruct "who deleted what, when, how" for audit purposes.

**Key Questions Assessors Struggle With:**

**Q: "How do we test audit trail reconstruction?"**

- A: Conduct a sample test:

  1. Select 3-5 recent deletion events from logs
  2. Attempt to reconstruct: Who deleted? What was deleted? When? How (method)? Was it verified?
  3. Measure time required to gather complete evidence
  4. Document results in Column Q

**Q: "What's considered 'good' reconstruction capability?"**

- A: Benchmarks:
  - **Excellent:** Complete evidence gathered in <1 hour
  - **Good:** Complete evidence in 1-4 hours
  - **Fair:** Complete evidence in 4-8 hours (requires manual searching)
  - **Poor:** Evidence incomplete even after 8+ hours
  - **None:** Cannot reconstruct (logs missing, not retained)

---

# Evidence Collection

## Required Evidence

For each sheet, collect and document in Sheet 8 (Evidence Register):

**Sheet 2 (Deletion Logging):**

- [ ] Screenshot of centralized logging system configuration
- [ ] Sample deletion log entries (redact sensitive data)
- [ ] Log retention policy document
- [ ] Access control list for logging system

**Sheet 3 (Verification Testing):**

- [ ] Forensic test reports (most recent 3)
- [ ] Testing procedure document
- [ ] Test schedule showing annual/periodic testing
- [ ] Forensic tool inventory (if in-house testing)

**Sheet 4 (Evidence Repository):**

- [ ] Evidence repository access control policy
- [ ] Sample evidence retention records
- [ ] Backup/DR procedures for evidence repository
- [ ] Evidence repository system documentation

**Sheet 5 (Certificate Management):**

- [ ] Sample deletion certificates from 3 vendors (high/medium/low quality)
- [ ] Certificate validation procedure document
- [ ] Vendor contract clauses requiring certificates
- [ ] Certificate request template

**Sheet 6 (Audit Trail):**

- [ ] Sample audit trail reconstruction test results
- [ ] Time log for reconstruction exercise
- [ ] Evidence chain of custody documentation
- [ ] Gap analysis for incomplete reconstructions

## Evidence Quality Standards

**Acceptable Evidence:**

- Current (within last 12 months)
- Attributed to responsible party (signed/dated)
- Complete (not partial/draft)
- Traceable to source system
- Stored in evidence repository (not just email)

**Unacceptable Evidence:**

- Verbal confirmations with no documentation
- Undated or unsigned documents
- Screenshots with no context
- Draft policies "under development"
- Evidence older than retention period

---

# Common Pitfalls & How to Avoid Them

## "We Don't Have Verification Testing" Paralysis

**Pitfall:** Organization freezes assessment because verification testing doesn't exist.

**Solution:**

- Complete the assessment anyway - documenting gaps IS the purpose
- Mark "Not Implemented" in Current State
- Use this assessment to build business case for testing program
- Reference A.8.10.2 assessment to identify which methods need testing
- Propose remediation timeline in Columns M-O

## Cargo Cult Compliance

**Pitfall:** Assuming vendor certificates = sufficient proof without validation.

**Solution:**

- Always validate certificate quality using rubric
- Request formal certificates (not email confirmations)
- Sample-test vendor claims (e.g., request proof of snapshot deletion)
- Document validation procedures in Sheet 5

## Evidence Repository = File Share Dump

**Pitfall:** Treating evidence storage as "save everything to a folder" without structure.

**Solution:**

- Evidence must be organized, indexed, and accessible
- Retention periods must be enforced
- Access controls must exist (not open to all staff)
- Backups must protect evidence long-term

## One-Time Assessment Never Updated

**Pitfall:** Complete assessment once, file it away, never revisit.

**Solution:**

- Schedule quarterly reviews (minimum)
- Trigger updates after major deletion events
- Feed results into A.8.10.5 dashboard for trend analysis
- Include in annual ISMS management review

---

# Quality Checklist

Before submitting assessment for approval (Sheet 9), verify:

**Completeness:**

- [ ] All 13 rows completed in Sheets 2-6 (65 total assessments)
- [ ] All dropdown values selected (no blank cells in Columns B-P)
- [ ] Assessor Notes (Column Q) provided for Critical/High gaps
- [ ] Evidence Register (Sheet 8) documents all supporting evidence

**Accuracy:**

- [ ] Current State reflects actual implementation (not aspirational)
- [ ] Gap Severity aligned with risk level (High risk = Critical/High severity)
- [ ] Remediation timelines realistic (Columns M-O)
- [ ] Evidence linked correctly to findings

**Audit Readiness:**

- [ ] Can demonstrate completion to external auditor within 2 hours
- [ ] Evidence accessible and traceable
- [ ] Gaps documented with remediation plans
- [ ] Summary Dashboard (Sheet 7) accurately reflects detailed findings

---

# Review & Approval Process

## Three-Level Approval Workflow

| Level | Role | Responsibility | Timeline |
|-------|------|----------------|----------|
| Level 1 | Assessor/Preparer | Complete assessment, collect evidence, document findings | Week 1-2 |
| Level 2 | Information Security Officer / Compliance Officer | Review completeness, validate findings, approve remediation priorities | Week 3 |
| Level 3 | CISO / Audit Committee | Final approval, commit resources for remediation, authorize dashboard publication | Week 4 |

## Approval Criteria

**Level 1 → Level 2:**

- All sheets completed with no blank mandatory fields
- Evidence collected and registered
- Findings supported by evidence
- Remediation plans documented

**Level 2 → Level 3:**

- Assessment findings validated against policy requirements
- Gap severity ratings confirmed
- Remediation priorities aligned with risk appetite
- Evidence quality acceptable for external audit

**Level 3 (Final):**

- Critical gaps have approved remediation plans with budgets
- Overall compliance status acceptable or improvement plan approved
- Results ready for publication to A.8.10.5 dashboard

## Rejection Scenarios

Assessment may be rejected if:

- ❌ Critical gaps identified with no remediation plan
- ❌ Evidence quality insufficient for audit defense
- ❌ Current State assessments appear inaccurate (too optimistic)
- ❌ Verification testing coverage <50% of deletion methods (per A.8.10.2)
- ❌ Deletion logs not retained per policy (typically 7 years)

---

**End of PART I: User Completion Guide**

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
