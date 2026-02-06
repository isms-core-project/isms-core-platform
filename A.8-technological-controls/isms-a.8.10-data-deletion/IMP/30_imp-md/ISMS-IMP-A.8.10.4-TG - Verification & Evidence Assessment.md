**ISMS-IMP-A.8.10.4-TG - Verification & Evidence Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.10.4-TG |
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

# Technical Specification
**Audience:** ISMS Implementation Teams, Python Developers, Excel Power Users

---

# Excel Workbook Structure

## Overview

**Workbook Name:** `ISMS_A_8_10_4_Verification_Evidence_YYYYMMDD.xlsx`

**Sheet Count:** 9 sheets total

**Assessment Data Entry:** Sheets 2-6 (5 assessment sheets × 13 rows = 65 total assessments)

**Standard Pattern:** All assessment sheets (2-6) follow identical column structure A-Q, with sheet-specific extended columns R-U

## Sheet Organization

| Sheet # | Sheet Name | Purpose | Data Entry Rows | Protected? |
|---------|------------|---------|-----------------|------------|
| 1 | Instructions & Legend | User guidance and dropdown value definitions | N/A (read-only) | Yes |
| 2 | Deletion Logging Assessment | Centralized logging infrastructure evaluation | 13 | No (yellow cells) |
| 3 | Verification Testing Program | Forensic testing capability and effectiveness | 13 | No (yellow cells) |
| 4 | Evidence Repository Assessment | Storage, retention, access control evaluation | 13 | No (yellow cells) |
| 5 | Certificate Management | Third-party certificate validation and quality | 13 | No (yellow cells) |
| 6 | Audit Trail Completeness | Reconstruction capability and chain of custody | 13 | No (yellow cells) |
| 7 | Verification Dashboard | Summary metrics, gap analysis, scoring | N/A (formulas) | Yes (formulas) |
| 8 | Evidence Register | Documentation of assessment evidence | 20 | No |
| 9 | Approval Sign-Off | Three-level approval workflow | 3 | No |

---

# Sheet 1: Instructions & Legend

## Purpose
Provide comprehensive user guidance and dropdown value definitions to ensure consistent assessment completion.

## Content Sections

**Section 1: Assessment Overview (Rows 1-10)**

- Document ID, Version, Date
- Assessment scope and purpose
- Target audience and time estimate
- Connection to ISMS-POL-A.8.10, Section 2.4 (Verification & Evidence Requirements)

**Section 2: The Verification Paradox (Rows 12-20)**

- Explanation of verification challenge
- Metadata over data principle
- Method testing over data testing principle
- Time-bound evidence retention principle

**Section 3: How to Complete This Assessment (Rows 22-40)**

- Recommended completion sequence (Sheets 2-6)
- Evidence collection guidance
- Common pitfalls and how to avoid them
- Quality checklist before approval

**Section 4: Dropdown Value Definitions (Rows 42-120)**

- Standard columns (A-Q) dropdown values with explanations
- Extended columns (R-U) sheet-specific dropdown values
- When to use N/A vs. specific values
- Scoring impact of each dropdown choice

**Section 5: Integration with Other A.8.10 Assessments (Rows 122-135)**

- Prerequisites from A.8.10.1 (evidence retention periods)
- Prerequisites from A.8.10.2 (deletion methods requiring verification)
- Prerequisites from A.8.10.3 (vendor certificate requirements)
- How results feed A.8.10.5 dashboard

**Section 6: Reference Standards (Rows 137-150)**

- NIST SP 800-88 verification methodology overview
- GDPR Article 17 evidence requirements
- ISO 27001 Clause 9.1 monitoring requirements
- Swiss OR evidence retention periods

## Formatting

- Title: Bold, 16pt, Blue fill
- Section headers: Bold, 12pt, Light blue fill
- Dropdown definitions: Table format with alternating row colors
- All text cells: Wrap text enabled

---

# Sheet 2: Deletion Logging Assessment

## Purpose
Evaluate the completeness, centralization, and reliability of deletion logging infrastructure.

## Column Structure

**Standard Columns (A-Q):** Same as all A.8.10 assessments (see Section 12 below)

**Extended Columns (R-U):**

| Column | Field Name | Description | Data Type | Validation |
|--------|------------|-------------|-----------|------------|
| R | Log Completeness Score | Percentage of required log fields captured (0-100%) | Percentage | Range: 0-100 |
| S | Log Retention Period | How long deletion logs are retained | Text | Max 30 chars |
| T | Centralized System | Are logs aggregated centrally? | Dropdown | Yes/No/Partial |
| U | Tamper Protection | Log integrity protection mechanism | Dropdown | See values below |

**Column U - Tamper Protection Dropdown Values:**

- None (Logs can be modified)
- Basic (File permissions only)
- Advanced (Cryptographic signing)
- Immutable (WORM/blockchain)
- N/A

## Assessment Rows (13 Total)

**Pre-filled in Column A (Verification Area):**

1. Centralized log aggregation system implementation
2. Log retention period alignment with policy requirements
3. Tamper-evident logging mechanisms (integrity protection)
4. Log storage capacity planning
5. Backup and disaster recovery for log systems
6. Log content: User/system identity captured
7. Log content: Data classification and identifiers captured (not actual data)
8. Log content: Timestamp with timezone captured
9. Log content: Deletion method documented
10. Log content: Verification status/result captured
11. Log analysis and monitoring procedures
12. Log access controls and segregation of duties
13. Integration with SIEM or security monitoring

## Assessment Checklist (Below Assessment Rows)

**Logging Infrastructure (5 items):**

- [ ] Centralized log aggregation system implemented for all deletion operations
- [ ] Log retention periods align with ISMS-POL-A.8.10, Section 2.1 (Retention & Deletion Triggers) schedules (typically 7 years)
- [ ] Tamper-evident logging mechanisms protect log integrity
- [ ] Log storage capacity planning accounts for retention requirements
- [ ] Backup and disaster recovery procedures exist for log systems

**Log Content Completeness (5 items):**

- [ ] Logs capture: Who deleted (user/system identity)
- [ ] Logs capture: What was deleted (data classification, record identifiers - NOT actual data)
- [ ] Logs capture: When deletion occurred (timestamp with timezone)
- [ ] Logs capture: How deletion occurred (method: overwrite, crypto-erase, physical destruction)
- [ ] Logs capture: Verification result (success/failure, certificate ID if applicable)

**Log Management (5 items):**

- [ ] Log analysis procedures identify deletion anomalies
- [ ] Log access restricted to authorized personnel only
- [ ] Log modification tracked via audit trails (logs of logs)
- [ ] Logs integrated into SIEM or security monitoring platform
- [ ] Regular log review performed (quarterly minimum)

**Regulatory Compliance (5 items):**

- [ ] GDPR Article 30 compliance: Deletion activities documented
- [ ] FADP compliance: Data processing records include deletion
- [ ] ISO 27001 Clause 9.1 compliance: Deletion monitoring operational
- [ ] Logs support data subject erasure request evidence (GDPR Article 17)
- [ ] Logs retained per legal requirements (Swiss OR: 7 years minimum)

## Reference Table: Required Log Fields

| # | Field Name | Example Value | Purpose |
|---|------------|---------------|---------|
| 1 | Event ID | DEL-2024-001234 | Unique deletion event identifier |
| 2 | Timestamp | 2024-01-15T14:30:45+01:00 | When deletion occurred (ISO 8601 format) |
| 3 | User/System | jdoe@example.com / AutoCleanup-Job-Daily | Who/what initiated deletion |
| 4 | Data Classification | Confidential - Personal Data | Sensitivity level (NOT actual data) |
| 5 | Record Identifier | Customer-ID-45678 | Unique ID (NOT customer name/PII) |
| 6 | System/Application | CRM-Production-DB-01 | Source system |
| 7 | Deletion Method | NIST-Purge-3Pass-Overwrite | How deleted (reference to A.8.10.2) |
| 8 | Data Category | Customer Personal Data | Type per data inventory |
| 9 | Retention Basis | GDPR Article 17 Erasure Request | Why deletion occurred |
| 10 | Verification Status | Verified-Certificate-Issued | Success/failure of deletion |
| 11 | Certificate ID | CERT-DEL-2024-001234 | Link to deletion certificate (if issued) |
| 12 | Backup Deletion Status | Completed-2024-01-20 | Deletion from backups confirmed |
| 13 | Archive Deletion Status | Completed-2024-01-20 | Deletion from archives confirmed |
| 14 | Legal Hold Check | No-Active-Holds | Confirmed no litigation hold prevented deletion |
| 15 | Approver | compliance-officer@example.com | Who authorized deletion |
| 16 | Related Request ID | DSR-2024-00456 | Link to data subject request (if applicable) |
| 17 | Vendor/Processor | AWS-Account-123456 | Third-party involved (if applicable) |
| 18 | Geographic Location | EU-Ireland-DC-02 | Data location (for regulatory compliance) |
| 19 | Forensic Test ID | TEST-2024-Q1-HDD-01 | Link to verification test (if periodic testing) |
| 20 | Compliance Status | GDPR-Compliant / FADP-Compliant | Regulatory framework satisfied |

## Conditional Formatting

**Column R (Log Completeness Score):**

- Green fill: ≥80% (16-20 fields captured)
- Yellow fill: 55-79% (11-15 fields)
- Orange fill: 30-54% (6-10 fields)
- Red fill: <30% (<6 fields)

**Column T (Centralized System):**

- Green text: "Yes"
- Yellow text: "Partial"
- Red text: "No"

**Column U (Tamper Protection):**

- Green text: "Immutable" or "Advanced"
- Yellow text: "Basic"
- Red text: "None"

---

# Sheet 3: Verification Testing Program

## Purpose
Evaluate whether [Organization] performs forensic testing to verify deletion methods are effective using test datasets (not production data).

## Extended Columns (R-U)

| Column | Field Name | Description | Data Type | Validation |
|--------|------------|-------------|-----------|------------|
| R | Testing Frequency | How often forensic tests are conducted | Dropdown | See values below |
| S | Last Test Date | Most recent forensic test for this method | Date | Date format |
| T | Test Pass Rate | Percentage of tests passed (0-100%) | Percentage | Range: 0-100 |
| U | NIST Verification Level | Level of verification per NIST SP 800-88 | Dropdown | See values below |

**Column R - Testing Frequency Dropdown:**

- Never (No testing performed)
- One-Time (Initial validation only)
- Annual (Once per year)
- Semi-Annual (Twice per year)
- Quarterly (4 times per year)
- After Each Use (Every deletion event)
- On-Demand (Ad-hoc testing)

**Column U - NIST Verification Level Dropdown:**

- None (No verification)
- Basic (Visual inspection only)
- Standard (Sector-level scan)
- Advanced (Full disk forensic scan)
- Laboratory (Third-party forensic lab)
- N/A

## Assessment Rows (13 Total)

**Pre-filled in Column A:**

1. Forensic testing program established and documented
2. Testing procedures based on NIST SP 800-88 methodology
3. Test datasets created with known characteristics
4. Testing frequency meets annual minimum requirement
5. Forensic tools and software inventory maintained
6. Hard drive overwrite method verification (if used)
7. SSD crypto-erasure verification (if used)
8. SSD physical destruction verification (if used)
9. Cloud/VM deletion verification (snapshot/backup removal)
10. Third-party forensic lab engagement (if outsourced)
11. Test result documentation and retention
12. Failed test remediation procedures
13. Testing coverage vs. deletion methods in use (from A.8.10.2)

## Assessment Checklist (20 items)

**Testing Program Governance (5 items):**

- [ ] Forensic testing program documented and approved
- [ ] Testing procedures reference NIST SP 800-88 verification standards
- [ ] Testing frequency defined (minimum annual per NIST)
- [ ] Responsible parties assigned (in-house or third-party lab)
- [ ] Testing budget allocated and approved

**Test Execution (5 items):**

- [ ] Test datasets created with known data patterns
- [ ] Deletion methods applied to test data (not production)
- [ ] Forensic analysis performed using industry-standard tools
- [ ] Test results documented with screenshots/reports
- [ ] Pass/fail criteria clearly defined per NIST

**Forensic Tools & Capabilities (5 items):**

- [ ] Forensic software tools licensed and current (e.g., EnCase, FTK, X-Ways)
- [ ] Hard drive imaging tools available (e.g., dd, FTK Imager)
- [ ] Hex editors for data remnant analysis
- [ ] SSD-specific tools for crypto-erase verification
- [ ] Test lab environment isolated from production

**Coverage & Completeness (5 items):**

- [ ] All deletion methods in use tested (per A.8.10.2 inventory)
- [ ] HDD overwrite methods tested (if used)
- [ ] SSD crypto-erase methods tested (if used)
- [ ] Cloud/VM deletion methods tested (snapshot verification)
- [ ] Physical destruction methods verified (if used)

## Reference Table: NIST SP 800-88 Verification Methods

| Media Type | Deletion Method (from A.8.10.2) | NIST Verification Level | Verification Procedure |
|------------|--------------------------------|------------------------|------------------------|
| HDD (magnetic) | Clear (1-pass overwrite) | Standard | Sector-level scan for data remnants |
| HDD (magnetic) | Purge (3-pass overwrite) | Advanced | Full disk forensic scan, hex analysis |
| HDD (magnetic) | Destroy (physical) | Laboratory | Third-party certificate of destruction |
| SSD (flash) | Clear (TRIM/Secure Erase) | Standard | Verify command completion via ATA logs |
| SSD (flash) | Purge (Crypto Erase) | Advanced | Verify unique encryption keys, test data recovery |
| SSD (flash) | Destroy (physical) | Laboratory | Visual inspection + certificate |
| Cloud/VM | Delete (API call) | Standard | Verify no snapshots/backups remain |
| Cloud/VM | Crypto Erase (key deletion) | Advanced | Verify keys deleted, data unrecoverable |
| Paper | Shred (cross-cut) | Basic | Visual inspection of shred size |
| Paper | Pulverize | Laboratory | Third-party certificate |

## Reference Table: Test Pass/Fail Criteria

| Test Result | Criteria | Action Required |
|-------------|----------|-----------------|
| **Pass** | Zero data remnants recoverable via forensic tools | Document test results, update testing log, continue using method |
| **Partial Pass** | <1% of test data recoverable, not sensitive fields | Review method effectiveness, consider upgrade to Purge method |
| **Fail** | >1% of test data recoverable OR any sensitive fields recoverable | **Immediately suspend method use**, investigate root cause, remediate before resuming |
| **Unable to Test** | Technical limitations prevent testing | Document limitation, engage third-party lab, or implement alternative method |

## Conditional Formatting

**Column R (Testing Frequency):**

- Green: "Quarterly", "Semi-Annual", "Annual"
- Yellow: "One-Time" (needs ongoing testing)
- Red: "Never" (critical gap)

**Column T (Test Pass Rate):**

- Green: ≥95% pass rate
- Yellow: 80-94% pass rate
- Red: <80% pass rate

**Column U (NIST Verification Level):**

- Green: "Advanced" or "Laboratory"
- Yellow: "Standard"
- Red: "Basic" or "None"

---

# Sheet 4: Evidence Repository Assessment

## Purpose
Evaluate secure storage, retention, and access control for deletion evidence (logs, certificates, test reports).

## Extended Columns (R-U)

| Column | Field Name | Description | Data Type | Validation |
|--------|------------|-------------|-----------|------------|
| R | Storage System Type | Type of evidence repository | Dropdown | See values below |
| S | Access Control Level | Strength of access restrictions | Dropdown | See values below |
| T | Backup Status | Evidence repository backup/DR status | Dropdown | Yes/No/Partial |
| U | Evidence Retention (Years) | How long evidence is retained | Number | Range: 1-99 |

**Column R - Storage System Type Dropdown:**

- None (No formal repository)
- File Share (Network drive)
- SharePoint / Document Management System
- Dedicated Records Management System (RMS)
- Compliance Evidence Platform
- SIEM / Log Management System
- Multiple Systems (Fragmented)

**Column S - Access Control Level Dropdown:**

- None (Open access)
- Basic (File permissions only)
- Role-Based (RBAC implemented)
- Privileged (Restricted to compliance/audit team)
- Time-Limited (External auditor access only)

## Assessment Rows (13 Total)

**Pre-filled in Column A:**

1. Evidence repository system implemented
2. Access controls restrict evidence to authorized personnel
3. Evidence retention periods align with policy (typically 7 years)
4. Evidence organized and indexed for retrieval
5. Backup and disaster recovery for evidence repository
6. Deletion log storage and retention
7. Forensic test report storage and retention
8. Third-party certificate storage and retention
9. Data subject request (DSR) evidence storage
10. Legal hold documentation storage
11. Evidence integrity protection (versioning, audit trails)
12. Evidence retrieval time meets audit requirements (<2 hours)
13. Evidence repository capacity planning

## Assessment Checklist (20 items)

**Repository Infrastructure (5 items):**

- [ ] Dedicated evidence repository system implemented
- [ ] Repository separate from operational systems (independence)
- [ ] Evidence organized by category (logs, certificates, test reports, DSR records)
- [ ] Evidence indexed for rapid retrieval (searchable)
- [ ] Repository capacity planning accounts for 7+ year retention

**Access Controls (5 items):**

- [ ] Access restricted to compliance/audit/legal personnel only
- [ ] Role-based access control (RBAC) implemented
- [ ] Access logging tracks who accessed which evidence
- [ ] External auditor access time-limited (e.g., 30-day audit window)
- [ ] Evidence modification prevented (read-only or version-controlled)

**Evidence Retention (5 items):**

- [ ] Retention periods documented per evidence type
- [ ] Deletion logs retained minimum 7 years (per Swiss OR)
- [ ] Forensic test reports retained for method lifecycle
- [ ] Certificates retained per vendor SLA + 3 years
- [ ] DSR evidence retained minimum 3 years (GDPR enforcement window)

**Backup & Disaster Recovery (5 items):**

- [ ] Evidence repository backed up daily/weekly
- [ ] Backups stored offsite or in separate availability zone
- [ ] Backup retention matches evidence retention requirements
- [ ] Disaster recovery tested annually
- [ ] Recovery Time Objective (RTO) <24 hours for audit support

## Reference Table: Evidence Types & Retention

| Evidence Type | Source Assessment | Minimum Retention Period | Retention Basis |
|---------------|------------------|--------------------------|-----------------|
| Deletion Logs | A.8.10.4 Sheet 2 | 7 years | Swiss OR (business records) |
| Forensic Test Reports | A.8.10.4 Sheet 3 | Method lifecycle + 1 year | NIST SP 800-88 (ongoing validation) |
| Third-Party Certificates | A.8.10.4 Sheet 5 | Vendor SLA period + 3 years | GDPR enforcement window |
| DSR Erasure Records | A.8.10.1 (Data Subject Rights) | 3 years | GDPR Article 17 enforcement window |
| Legal Hold Records | A.8.10.1 (Legal Holds) | 7 years after hold release | Litigation risk period |
| Audit Trail Queries | A.8.10.4 Sheet 6 | 3 years | ISO 27001 certification cycle |

## Conditional Formatting

**Column R (Storage System Type):**

- Green: "Dedicated Records Management System" or "Compliance Evidence Platform"
- Yellow: "SharePoint / Document Management System"
- Red: "File Share" or "None" or "Multiple Systems (Fragmented)"

**Column S (Access Control Level):**

- Green: "Privileged" or "Time-Limited"
- Yellow: "Role-Based"
- Red: "Basic" or "None"

**Column U (Evidence Retention Years):**

- Green: ≥7 years
- Yellow: 3-6 years
- Red: <3 years

---

# Sheet 5: Certificate Management

## Purpose
Evaluate quality and validation procedures for third-party deletion certificates (from cloud providers, SaaS vendors, managed service providers).

## Extended Columns (R-U)

| Column | Field Name | Description | Data Type | Validation |
|--------|------------|-------------|-----------|------------|
| R | Certificate Quality Score | Average quality score (1-5 scale) | Number | Range: 1-5 |
| S | Certificates Received Count | Number of certificates received this period | Number | Range: 0-999 |
| T | Validation Procedure Exists | Is certificate validation documented? | Dropdown | Yes/No/Partial |
| U | Missing Certificates Count | Vendors with no certificate | Number | Range: 0-999 |

## Assessment Rows (13 Total)

**Pre-filled in Column A:**

1. Third-party deletion certificate requirements documented
2. Vendor contracts require formal deletion certificates
3. Certificate request procedures established
4. Certificate quality scoring rubric implemented
5. Certificate validation procedures documented
6. Certificates stored in evidence repository
7. Certificate authenticity verification (signature, ID)
8. High-quality certificates received (score 4-5)
9. Medium-quality certificates received (score 3)
10. Low-quality certificates received (score 1-2)
11. Missing certificates from vendors requiring them
12. Certificate follow-up procedures for non-compliance
13. Integration with A.8.10.3 vendor management

## Reference Table: Certificate Quality Scoring Rubric

| Score | Quality Level | Certificate Characteristics | Example |
|-------|---------------|---------------------------|---------|
| **5** | Excellent | • Vendor letterhead with signature<br>• Certificate ID number<br>• Deletion date and method<br>• NIST category (Clear/Purge/Destroy)<br>• Data type deleted<br>• Verification statement<br>• Contact for questions | Formal certificate from AWS/Azure with all fields |
| **4** | Good | Missing 1-2 elements (e.g., NIST category or certificate ID) | Professional certificate with most fields |
| **3** | Fair | Generic template with minimal detail | "Data deleted per your request on [date]" |
| **2** | Poor | Email confirmation only, no formal certificate | Email: "We've processed your deletion request" |
| **1** | None | No certificate provided despite request | Vendor ignored certificate request |

## Conditional Formatting

**Column R (Certificate Quality Score):**

- Green: ≥4.0 (Excellent/Good average)
- Yellow: 3.0-3.9 (Fair average)
- Red: <3.0 (Poor average)

**Column U (Missing Certificates Count):**

- Green: 0 missing
- Yellow: 1-5 missing
- Red: >5 missing

---

# Sheet 6: Audit Trail Completeness

## Purpose
Test ability to reconstruct complete deletion audit trail for external auditor: "Prove data X was deleted on date Y."

## Extended Columns (R-U)

| Column | Field Name | Description | Data Type | Validation |
|--------|------------|-------------|-----------|------------|
| R | Reconstruction Time (Hours) | Time to gather complete evidence | Number | Range: 0-24 |
| S | Evidence Completeness (%) | % of required evidence gathered | Percentage | Range: 0-100 |
| T | Chain of Custody | Is chain of custody documented? | Dropdown | Yes/No/Partial |
| U | Audit Readiness | Can defend to external auditor? | Dropdown | See values below |

**Column U - Audit Readiness Dropdown:**

- Fully Ready (Evidence complete, <1 hour retrieval)
- Mostly Ready (Evidence complete, 1-4 hours retrieval)
- Partially Ready (Evidence incomplete or >4 hours retrieval)
- Not Ready (Cannot reconstruct audit trail)

## Assessment Rows (13 Total)

**Pre-filled in Column A:**

1. Audit trail reconstruction procedure documented
2. Sample reconstruction test conducted (3-5 deletion events)
3. Evidence retrieval time meets audit requirements (<2 hours)
4. Chain of custody documentation maintained
5. Deletion logs accessible and complete
6. Forensic test results linked to deletion events
7. Third-party certificates linked to deletion events
8. Data subject request (DSR) evidence linked
9. Legal hold check evidence available
10. Backup/archive deletion evidence accessible
11. Evidence gaps identified and documented
12. Remediation plan for evidence gaps
13. Quarterly audit readiness testing scheduled

## Reference Table: Audit Trail Reconstruction Test Procedure

| Step | Action | Expected Result | Pass/Fail Criteria |
|------|--------|-----------------|-------------------|
| 1 | Select 3 recent deletion events from logs | 3 events identified with dates, record IDs | **Pass:** Events identified <15 min<br>**Fail:** Cannot identify events |
| 2 | Gather deletion log entries for each event | Complete log entries retrieved | **Pass:** All 20 log fields present<br>**Fail:** Missing critical fields |
| 3 | Retrieve forensic test results (if applicable) | Test reports show method verification | **Pass:** Test reports accessible<br>**Fail:** No test reports or >1 year old |
| 4 | Retrieve certificates (if third-party) | Certificates for vendor deletions | **Pass:** Certificates quality score ≥4<br>**Fail:** No certificate or score <3 |
| 5 | Verify chain of custody | Evidence traceable to source | **Pass:** All evidence attributed<br>**Fail:** Gaps in attribution |
| 6 | Measure total time elapsed | Time from request to complete evidence | **Pass:** <2 hours<br>**Fail:** >2 hours |

## Conditional Formatting

**Column R (Reconstruction Time):**

- Green: <1 hour
- Yellow: 1-4 hours
- Red: >4 hours

**Column S (Evidence Completeness):**

- Green: 100%
- Yellow: 80-99%
- Red: <80%

**Column U (Audit Readiness):**

- Green: "Fully Ready"
- Yellow: "Mostly Ready"
- Red: "Partially Ready" or "Not Ready"

---

# Sheet 7: Verification Dashboard

## Purpose
Aggregate summary metrics from Sheets 2-6 for executive visibility and gap prioritization.

## Dashboard Sections

**Section 1: Overall Verification Maturity (5 metrics)**

| Metric | Formula | Target | Status |
|--------|---------|--------|--------|
| Deletion Logging Maturity | =AVERAGE(Sheet2!E5:E17) | ≥4.0 ("Effective") | RAG |
| Verification Testing Coverage | =COUNTIF(Sheet3!B5:B17,"Fully Implemented")/13*100 | 100% | RAG |
| Evidence Repository Security | =AVERAGE(Sheet4!F5:F17) | ≥4.0 ("Good") | RAG |
| Certificate Quality Average | =AVERAGE(Sheet5!R5:R17) | ≥4.0 | RAG |
| Audit Trail Readiness | =COUNTIF(Sheet6!U5:U17,"Fully Ready")/13*100 | 100% | RAG |

**Section 2: Critical Gaps Summary**

| Assessment Area | Critical Gaps | Highest Priority | Target Date |
|-----------------|---------------|------------------|-------------|
| Deletion Logging | =COUNTIF(Sheet2!D5:D17,"Critical") | [Manual entry from Sheet 2] | [Manual] |
| Verification Testing | =COUNTIF(Sheet3!D5:D17,"Critical") | [Manual entry from Sheet 3] | [Manual] |
| Evidence Repository | =COUNTIF(Sheet4!D5:D17,"Critical") | [Manual entry from Sheet 4] | [Manual] |
| Certificate Management | =COUNTIF(Sheet5!D5:D17,"Critical") | [Manual entry from Sheet 5] | [Manual] |
| Audit Trail | =COUNTIF(Sheet6!D5:D17,"Critical") | [Manual entry from Sheet 6] | [Manual] |

**Section 3: Verification Evidence Statistics**

| Metric | Value | Benchmark |
|--------|-------|-----------|
| Average Log Completeness Score | =AVERAGE(Sheet2!R5:R17) | ≥80% |
| Forensic Test Pass Rate | =AVERAGE(Sheet3!T5:T17) | ≥95% |
| Evidence Repository Retention (Years) | =AVERAGE(Sheet4!U5:U17) | ≥7 years |
| Certificate Quality Score | =AVERAGE(Sheet5!R5:R17) | ≥4.0 |
| Audit Reconstruction Time (Hours) | =AVERAGE(Sheet6!R5:R17) | <2 hours |

---

# Sheet 8: Evidence Register

## Purpose
Document all evidence collected during assessment to support audit defense.

## Column Structure (20 evidence rows)

| Column | Field Name | Description |
|--------|------------|-------------|
| A | Evidence ID | Unique identifier (e.g., A.8.10.4-E001) |
| B | Evidence Type | Dropdown: Screenshot / Document / Report / Certificate / Log / Email / Other |
| C | Description | What this evidence shows |
| D | Related Assessment | Which sheet/row this supports (e.g., "Sheet 2, Row 5") |
| E | Source System | Where evidence was obtained |
| F | Collection Date | When evidence was collected |
| G | Collected By | Person who collected evidence |
| H | Storage Location | Path to evidence file in repository |
| I | Retention Period | How long to retain (years) |
| J | Notes | Additional context |

---

# Sheet 9: Approval Sign-Off

## Three-Level Approval

| Level | Role | Name | Signature | Date | Comments |
|-------|------|------|-----------|------|----------|
| 1 | Assessor/Preparer | [Manual] | [Manual] | [Auto: =TODAY()] | [Manual] |
| 2 | Info Security Officer | [Manual] | [Manual] | [Manual] | [Manual] |
| 3 | CISO / Audit Committee | [Manual] | [Manual] | [Manual] | [Manual] |

---

# Conditional Formatting Summary

## Global Rules (All Sheets 2-6)

**Column B (Current State):**

- Green: "Fully Implemented" or "Continuously Improving"
- Yellow: "Substantially Implemented"
- Orange: "Partially Implemented"
- Red: "Not Implemented"

**Column D (Gap Severity):**

- Red bold: "High" or "Critical"
- Orange: "Medium"
- Green: "None (No Gap)"

**Column F (Evidence Quality):**

- Green: "Excellent" or "Good"
- Yellow: "Fair"
- Red: "Poor" or "None"

**Column G (Compliance Status):**

- Green: "Fully Compliant"
- Yellow: "Substantially Compliant"
- Red: "Non-Compliant" or "Partially Compliant"

---

# Python Script Integration Notes

## Script: `generate_a810_4_verification_evidence.py`

**Purpose:** Generate ISMS_A_8_10_4_Verification_Evidence_YYYYMMDD.xlsx with all specifications above.

**Key Customization Areas for A.8.10.4:**

1. **Sheet-Specific Extended Columns (R-U):**

   - Sheet 2: Log Completeness %, Retention Period, Centralized, Tamper Protection
   - Sheet 3: Testing Frequency, Last Test Date, Pass Rate %, NIST Level
   - Sheet 4: Storage Type, Access Control, Backup Status, Retention Years
   - Sheet 5: Quality Score, Certificates Count, Validation Exists, Missing Count
   - Sheet 6: Reconstruction Time, Completeness %, Chain of Custody, Readiness

2. **Reference Tables:**

   - Sheet 2: 20 Required Log Fields table
   - Sheet 3: NIST Verification Methods by Media Type table
   - Sheet 3: Test Pass/Fail Criteria table
   - Sheet 4: Evidence Types & Retention table
   - Sheet 5: Certificate Quality Scoring Rubric table
   - Sheet 6: Reconstruction Test Procedure table

3. **Assessment Row Pre-fills:**

   - Each sheet has specific 13 verification areas in Column A
   - Do NOT copy generic assessment rows from other controls

4. **Dashboard Formulas (Sheet 7):**

   - Calculate from Sheets 2-6 specific columns
   - Use AVERAGE, COUNTIF, conditional logic
   - No external workbook links (self-contained)

5. **Conditional Formatting:**

   - Sheet-specific rules for extended columns R-U
   - Global rules for standard columns A-Q (consistent across all A.8.10 assessments)

## Integration with A.8.10.5 Dashboard

**Metrics to Export to Compliance Dashboard:**

| Metric | Source Cell | Dashboard Destination |
|--------|-------------|----------------------|
| Audit Readiness Score | Sheet7!B5 (formula result) | A.8.10.5 Sheet 6, Cell B8 |
| Certificate Quality Average | Sheet7!B11 | A.8.10.5 Sheet 6, Cell B5 |
| Audit Trail Completeness % | Sheet6 average of Column S | A.8.10.5 Sheet 6, Cell B6 |
| Forensic Test Coverage % | Sheet3 average of Column T | A.8.10.5 Sheet 6, Cell B7 |

**Manual Entry Required:** Assessment completer must copy these values from A.8.10.4 Sheet 7 into A.8.10.5 dashboard after approval.

---

**END OF SPECIFICATION**

---

*"The violation of Bell's inequalities shows that quantum mechanics cannot be explained by any local hidden variable theory."*
— Alain Aspect

<!-- QA_VERIFIED: 2026-02-06 -->
