**ISMS-IMP-A.8.10.1-TG - Retention & Deletion Triggers Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.10.1-TG |
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

# Technical Specification
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

<!-- QA_VERIFIED: 2026-02-06 -->
