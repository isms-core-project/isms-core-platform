# ISMS-IMP-A.8.10.1 - Retention & Deletion Triggers Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.10.1  
**Assessment Area:** Retention Schedules and Deletion Triggers  
**Related Policy:** ISMS-POL-A.8.10-S2.1 (Retention & Deletion Triggers)  
**Purpose:** Assess organizational compliance with retention requirements and deletion trigger mechanisms

**Key Principle:** This assessment is **vendor-neutral**. Organizations document THEIR specific data categories, retention periods, and deletion trigger implementations. The workbook provides the structure; customers provide their reality.

---

## Assessment Context

### What This Assessment Covers

This assessment evaluates the organization's approach to:
1. **Data Category Identification** - Complete inventory of data types processed
2. **Retention Schedule Compliance** - Legal and regulatory alignment
3. **Deletion Trigger Mechanisms** - Automated and manual deletion processes
4. **Legal Hold Procedures** - Suspension of deletion when required
5. **Data Subject Rights** - GDPR Article 17 / FADP compliance

### What This Assessment Does NOT Cover

- **HOW** data is deleted (see ISMS-IMP-A.8.10.2 - Deletion Methods)
- **WHERE** third-party data is stored (see ISMS-IMP-A.8.10.3 - Third-Party Deletion)
- **Verification** of deletion effectiveness (see ISMS-IMP-A.8.10.4 - Verification & Evidence)

### Related ISMS Documents

- **ISMS-POL-A.8.10** - Information Deletion Policy (Master)
- **ISMS-POL-A.8.10-S2.1** - Retention & Deletion Triggers Requirements
- **ISMS-POL-A.8.10-S5.B** - Annex B: Retention Schedule Template
- **ISMS-REF-A.5.23** - Cloud Service Provider Registry (for data location context)

---

## Workbook Structure

This workbook contains **9 sheets** organized as follows:

### Core Sheets
1. **Instructions & Legend** - How to use this workbook, color coding, definitions
2. **2. Data Category Registry** - Complete inventory of data categories
3. **3. Retention Schedule Compliance** - Retention periods and legal basis
4. **4. Deletion Trigger Configuration** - Automated and manual triggers
5. **5. Legal Hold Management** - Legal hold procedures and active holds
6. **6. Data Subject Requests** - GDPR Article 17 / FADP request handling

### Summary & Administration
7. **Summary Dashboard** - Compliance overview, KPIs, critical gaps
8. **Evidence Register** - Links to supporting documentation (100 rows)
9. **Approval Sign-Off** - Three-level approval workflow

---

## Assessment Sheets - Column Definitions

### Standard Column Layout (Columns A-Q, 17 columns)

These columns appear in **Sheets 2-6** with minor variations:

| Column | Header | Width | Type | Validation Options | Purpose |
|--------|--------|-------|------|-------------------|---------|
| A | Data Category / System Name | 30 | Text | Free text | Primary identifier for data type |
| B | Data Classification | 22 | Dropdown | Public, Internal, Confidential, Restricted | Sensitivity level |
| C | Business Owner | 18 | Text | Free text | Department/role responsible |
| D | Retention Period | 20 | Dropdown | See retention options below | How long to keep |
| E | Legal/Regulatory Basis | 20 | Dropdown | See legal basis options below | Why this retention period |
| F | Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Traffic light status |
| G | Implementation Date | 12 | Date | Date picker | When retention schedule deployed |
| H | Last Review Date | 12 | Date | Date picker | Most recent schedule review |
| I | Next Review Date | 12 | Date | Date picker | Scheduled next review |
| J | Gap Identified | 25 | Text | Free text | If not compliant, describe issue |
| K | Remediation Plan | 25 | Text | Free text | How gap will be addressed |
| L | Target Completion | 12 | Date | Date picker | Remediation deadline |
| M | Risk Level | 12 | Dropdown | Critical, High, Medium, Low | If gap exists |
| N | Evidence Reference | 20 | Text | Free text | Link to row in Evidence Register |
| O | Notes / Comments | 25 | Text | Free text | Additional context |
| P | Remediation Owner | 18 | Text | Free text | Person responsible for fix |
| Q | Budget Required | 15 | Dropdown | Yes, No, Unknown | Resource needs |

### Extended Columns (R-T) - Sheet-Specific

These additional columns appear in specific sheets:

**Sheet 2 (Data Category Registry):**
- R: **Primary Storage Location** (Dropdown: On-Premise, Cloud (IaaS), Cloud (PaaS), Cloud (SaaS), Hybrid, Third-Party)
- S: **Volume/Records** (Text: approximate count or size)
- T: **Contains PII/SPI** (Dropdown: Yes - PII, Yes - SPI, Yes - Both, No)

**Sheet 3 (Retention Schedule Compliance):**
- R: **Retention Calculation Method** (Dropdown: Fixed Period, Event-Based, Hybrid)
- S: **Event Trigger Description** (Text: if event-based, describe the event)
- T: **Backup Retention Aligned** (Dropdown: Yes, No, Partial, N/A)

**Sheet 4 (Deletion Trigger Configuration):**
- R: **Trigger Type** (Dropdown: Automatic, Manual, Semi-Automatic, Event-Based)
- S: **Trigger Frequency** (Dropdown: Real-time, Daily, Weekly, Monthly, Quarterly, Annual, Ad-hoc)
- T: **Legal Hold Check Integrated** (Dropdown: Yes - Automated, Yes - Manual, No, N/A)

**Sheet 5 (Legal Hold Management):**
- R: **Active Legal Holds** (Number: count of active holds)
- S: **Legal Hold Notification Process** (Dropdown: Automated, Manual, Hybrid, None)
- T: **Hold Review Frequency** (Dropdown: Weekly, Monthly, Quarterly, Annual)

**Sheet 6 (Data Subject Requests):**
- R: **Average Response Time (Days)** (Number: actual performance)
- S: **GDPR/FADP Applicable** (Dropdown: GDPR Only, FADP Only, Both, Neither)
- T: **Request Volume (Last 12 Months)** (Number: count of requests)

---

## Validation Options - Dropdowns

### Retention Period Options (Column D)
- 30 days
- 60 days
- 90 days
- 6 months
- 1 year
- 2 years
- 3 years
- 5 years
- 7 years
- 10 years
- Permanent
- Until Event Occurs
- Other (specify in notes)

### Legal/Regulatory Basis Options (Column E)
- Swiss FADP
- EU GDPR
- Swiss Code of Obligations (OR)
- Swiss Tax Law
- EU ePrivacy Directive
- Industry Standard (specify)
- Contractual Obligation
- Legitimate Interest
- Consent
- Legal Obligation
- Multiple Bases (specify)
- Other (specify in notes)

### Data Classification Options (Column B)
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

**Purpose:** Provide complete usage instructions and definitions

**Content Structure:**

**Section 1: Document Information (Rows 1-8)**
- Workbook title and version
- Assessment date and assessor name
- Organization name
- Review period covered
- Related policy references

**Section 2: How to Use This Workbook (Rows 10-25)**
- Step-by-step instructions for completing assessment
- Navigation guidance between sheets
- When to use each assessment sheet
- How to link to Evidence Register
- Approval workflow instructions

**Section 3: Color Coding Legend (Rows 27-35)**
| Color | Meaning | Usage |
|-------|---------|-------|
| Blue header | Column headers | Do not edit |
| Yellow | Data entry cells | Complete these fields |
| Green | Compliant status | Automated/manual entry |
| Orange | Partial compliance | Automated/manual entry |
| Red | Non-compliant | Automated/manual entry |
| Gray | Reference information | Read-only |
| White | Optional fields | Complete if relevant |

**Section 4: Key Definitions (Rows 37-55)**
- **Data Category:** A classification of data based on content, purpose, or source
- **Retention Period:** The duration for which data must/should be retained
- **Deletion Trigger:** An event or condition that initiates data deletion
- **Legal Hold:** Suspension of normal deletion due to litigation or investigation
- **Data Subject Request:** Request from individual to delete their personal data
- **Event-Based Retention:** Retention calculated from a specific event (e.g., contract end)
- **PII:** Personally Identifiable Information
- **SPI:** Special category Personal Information (sensitive data)

**Section 5: Regulatory References (Rows 57-70)**
- GDPR Article 17 (Right to Erasure)
- Swiss FADP Article 6 (Data Processing Principles)
- GDPR Article 5(1)(e) (Storage Limitation)
- ISO 27002:2022 Control A.8.10
- NIST SP 800-88 (for deletion methods - reference only)

**Section 6: Important Notes (Rows 72-85)**
- Vendor-neutral approach explanation
- Link to related assessments (A.8.10.2-5)
- Annual review requirement
- Escalation procedures for critical gaps

---

### Sheet 2: Data Category Registry

**Purpose:** Complete inventory of all data categories processed by the organization

**Assessment Question:**
*"Have we identified and documented ALL data categories we process, including their characteristics, ownership, and storage locations?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.1, Section 2.1.1 (Data Category Identification)

**Column Structure:** A-T (20 columns total)
- Columns A-Q: Standard base columns
- Column R: Primary Storage Location
- Column S: Volume/Records
- Column T: Contains PII/SPI

**Data Entry Rows:** 13 rows (yellow-highlighted, Rows 10-22)

**Compliance Checklist (Rows 25-45):** ✅/❌ Assessment

1. All business units have been consulted for data categories
2. Data inventory includes operational, HR, financial, and customer data
3. Each data category has a designated Business Owner
4. Storage locations (on-premise, cloud, third-party) are documented
5. PII and SPI data categories are specifically identified
6. Volume/scale of data is estimated for each category
7. Data classification levels are assigned per organizational policy
8. Temporary/ephemeral data categories are included
9. Legacy systems and archived data are included in inventory
10. Cross-border data transfers are noted (if applicable)
11. Data category registry is reviewed at least annually
12. New business processes trigger data category reassessment
13. Shadow IT data categories have been investigated
14. M&A due diligence includes data category mapping
15. Data categories align with Records Retention Schedule

**Reference Table 1: Common Data Categories (Rows 47-62)**
| Category Example | Typical Retention | Common Legal Basis |
|------------------|-------------------|-------------------|
| Employee Personnel Files | 10 years post-employment | Swiss OR, Tax Law |
| Customer Contracts | 10 years post-termination | Swiss OR (Art. 127) |
| Financial Records | 10 years | Swiss Tax Law |
| Marketing Consent Records | Until consent withdrawn + 1 year | GDPR, FADP |
| Access Logs | 1 year | Security requirement |
| Email Communications | 1-7 years (varies) | Business need |
| Customer Support Tickets | 3 years post-resolution | Contractual |
| Product Telemetry | 90 days - 2 years | Legitimate interest |
| CCTV Footage | 30-90 days | Security/legal requirement |
| Website Analytics | 26 months (GDPR default) | Consent/Legitimate interest |
| Backup Data | Aligned with active retention | Same as source data |
| Development/Test Data | Until project end + 90 days | Business need |
| Audit Trails | 7-10 years | Regulatory requirement |
| HR Recruitment Records | 6 months post-decision | GDPR, FADP |
| Health & Safety Records | 10 years | Legal obligation |

**Reference Table 2: Storage Location Implications (Rows 64-72)**
| Location Type | Deletion Complexity | Key Considerations |
|---------------|---------------------|-------------------|
| On-Premise | Medium | Full control, hardware lifecycle |
| Cloud (IaaS) | Medium-High | Snapshot management, API deletion |
| Cloud (PaaS) | High | Platform-specific deletion methods |
| Cloud (SaaS) | Very High | Vendor-dependent, see A.8.10.3 |
| Hybrid | Very High | Coordination across environments |
| Third-Party | Very High | Contractual deletion, see A.8.10.3 |

**Exception/Deviation Block (Rows 75-80):**
- Data categories excluded from inventory (with justification)
- Categories pending Business Owner assignment
- Categories with disputed retention periods

---

### Sheet 3: Retention Schedule Compliance

**Purpose:** Verify that retention periods are defined and comply with legal/regulatory requirements

**Assessment Question:**
*"Does each data category have a documented retention period with a valid legal or business justification?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.1, Section 2.1.2 (Retention Schedule Requirements)

**Column Structure:** A-T (20 columns total)
- Columns A-Q: Standard base columns
- Column R: Retention Calculation Method
- Column S: Event Trigger Description
- Column T: Backup Retention Aligned

**Data Entry Rows:** 13 rows (yellow-highlighted)

**Compliance Checklist (Rows 25-45):**

1. Every data category has a defined retention period
2. Retention periods have documented legal/regulatory basis
3. Swiss FADP compliance verified for all PII categories
4. GDPR compliance verified where applicable
5. Retention periods do not exceed legal maximums
6. Retention periods meet legal minimums (e.g., tax records)
7. Event-based retention triggers are clearly defined
8. Business justification documented for non-regulatory retention
9. Conflicting retention requirements are resolved and documented
10. Retention schedule approved by Legal/Compliance team
11. Backup retention aligns with active data retention
12. "Permanent" retention is justified and approved
13. Retention periods reviewed annually
14. Changes to retention periods follow change management process
15. Data subjects are informed of retention periods (GDPR/FADP)

**Reference Table 1: Swiss Legal Retention Requirements (Rows 47-58)**
| Data Type | Minimum Retention | Legal Basis | Maximum Deletion |
|-----------|-------------------|-------------|------------------|
| Accounting Records | 10 years | Swiss OR Art. 958f | After 10 years |
| Tax Records | 10 years | Swiss Tax Law | After 10 years |
| Employee Records | 10 years | Swiss OR Art. 127 | After 10 years (FADP) |
| Contracts | 10 years | Swiss OR Art. 127 | After 10 years |
| Payroll Records | 10 years | Swiss Tax/Social Law | After 10 years |
| Corporate Minutes | Permanent | Swiss OR Art. 695 | N/A |
| Share Register | Permanent | Swiss OR Art. 686 | N/A |
| Correspondence | No minimum | Business need | FADP: when no longer needed |
| Marketing Data | No minimum | Consent-based | FADP: consent withdrawal |
| CCTV Footage | No minimum | Proportionality | FADP: typically 30-90 days |
| Health Data | 10 years (recommended) | Best practice | FADP: when no longer needed |

**Reference Table 2: GDPR Storage Limitation Principle (Rows 60-68)**
| GDPR Requirement | Implication for Retention |
|------------------|---------------------------|
| Article 5(1)(e) | Data kept no longer than necessary |
| Article 17 | Right to erasure (with exceptions) |
| Article 6 Legal Bases | Retention tied to lawful basis duration |
| Recital 39 | Periodic review of data necessity |
| Art. 13/14 | Inform data subjects of retention periods |
| Art. 30 | Document retention periods in ROPA |

**Reference Table 3: Retention Calculation Methods (Rows 70-77)**
| Method | Definition | Example |
|--------|------------|---------|
| Fixed Period | Set duration from creation/collection | 7 years from date of invoice |
| Event-Based | Duration starts at specific event | 10 years from contract termination |
| Hybrid | Combination of fixed + event | 3 years OR until litigation resolved |
| Indefinite (Permanent) | No planned deletion | Corporate charter documents |
| Until Consent Withdrawn | Active until user action | Marketing email list |

**Exception/Deviation Block (Rows 80-85):**
- Data categories with conflicting retention requirements
- Categories pending Legal/Compliance review
- Categories where retention exceeds legal minimum (justify)

---

### Sheet 4: Deletion Trigger Configuration

**Purpose:** Assess mechanisms that initiate data deletion (automated, manual, event-based)

**Assessment Question:**
*"Do we have effective and reliable deletion triggers that ensure data is deleted when retention periods expire?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.1, Section 2.1.3 (Deletion Trigger Implementation)

**Column Structure:** A-T (20 columns total)
- Columns A-Q: Standard base columns
- Column R: Trigger Type
- Column S: Trigger Frequency
- Column T: Legal Hold Check Integrated

**Data Entry Rows:** 13 rows (yellow-highlighted)

**Compliance Checklist (Rows 25-45):**

1. Automated deletion triggers implemented for high-volume data
2. Manual deletion procedures documented for low-volume data
3. Trigger execution is logged and auditable
4. Failed deletion attempts are alerted and investigated
5. Legal hold checks are integrated into trigger logic
6. Backup deletion triggers aligned with active data triggers
7. Cloud/SaaS deletion triggers verified (see A.8.10.3)
8. Event-based triggers are monitored for event occurrence
9. Deletion triggers tested at least annually
10. Trigger failures have defined escalation procedures
11. Business Owner approval required for manual triggers (if policy requires)
12. Deletion triggers respect data dependencies (referential integrity)
13. Triggers account for data in transit (queues, caches)
14. Deletion trigger schedule published and communicated
15. Trigger configuration changes follow change management

**Reference Table 1: Trigger Types and Use Cases (Rows 47-58)**
| Trigger Type | Best For | Advantages | Disadvantages |
|--------------|----------|------------|---------------|
| Automatic | High-volume, structured data | Consistent, no human error | Requires robust testing |
| Manual | Low-volume, sensitive data | Controlled, deliberate | Human error risk, slower |
| Semi-Automatic | Medium volume, needs approval | Balance control and efficiency | Workflow complexity |
| Event-Based | Contract-dependent data | Precise, legally aligned | Requires event tracking |

**Reference Table 2: Common Deletion Trigger Patterns (Rows 60-70)**
| Pattern | Description | Example Implementation |
|---------|-------------|------------------------|
| Time-Based Cron | Scheduled deletion job | Daily at 02:00 UTC, delete records > 7 years |
| Database TTL | Built-in expiration | MongoDB TTL index, Redis EXPIRE |
| Lifecycle Policy | Cloud-native deletion | AWS S3 Lifecycle, Azure Blob Lifecycle |
| Workflow Approval | Human-in-the-loop | Jira ticket → approval → script execution |
| Event Listener | Reactive deletion | Contract.status = "terminated" → 90-day timer → delete |
| Batch Processing | Periodic bulk deletion | Monthly job: identify + delete expired records |

**Reference Table 3: Legal Hold Integration Methods (Rows 72-80)**
| Integration Type | How It Works | Reliability |
|------------------|--------------|-------------|
| Pre-Deletion Check | Query legal hold DB before deletion | High (recommended) |
| Exclusion Flag | Legal hold sets "do_not_delete" flag | High |
| Separate Quarantine | Move to legal hold storage | High (best for litigation) |
| Manual Review List | Daily review of pending deletions | Medium (human dependency) |
| None (Manual Hold) | Rely on manual halt of deletion | Low (not recommended) |

**Exception/Deviation Block (Rows 83-88):**
- Data categories without automated triggers (justify)
- Trigger failures in last 12 months
- Categories pending trigger implementation

---

### Sheet 5: Legal Hold Management

**Purpose:** Assess procedures for suspending deletion when legal or regulatory holds are in effect

**Assessment Question:**
*"Do we have robust processes to identify, communicate, and manage legal holds to prevent premature deletion of data under hold?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.1, Section 2.1.4 (Legal Hold Procedures)

**Column Structure:** A-T (20 columns total)
- Columns A-Q: Standard base columns
- Column R: Active Legal Holds
- Column S: Legal Hold Notification Process
- Column T: Hold Review Frequency

**Data Entry Rows:** 13 rows (yellow-highlighted)

**Compliance Checklist (Rows 25-45):**

1. Legal hold procedures are documented and approved
2. Legal/Compliance team has authority to initiate holds
3. IT/Data teams receive timely notification of holds
4. Hold notification includes specific data categories and date ranges
5. Automated deletion triggers check for active holds
6. Legal hold data is segregated or flagged in systems
7. Legal hold registry is maintained (who, what, when, why)
8. Business Owners are notified when their data is under hold
9. Periodic review of active holds (at least quarterly)
10. Hold release procedures are documented
11. Post-hold deletion is executed per normal retention schedule
12. Legal hold training provided to relevant staff
13. Legal hold breaches (accidental deletion) are reported and investigated
14. Legal hold scope is clearly defined (not overly broad)
15. Legal hold process tested at least annually

**Reference Table 1: Legal Hold Triggers (Rows 47-56)**
| Trigger Event | Typical Response Time | Hold Scope |
|---------------|----------------------|------------|
| Litigation Notice | Within 24 hours | All relevant data for case |
| Regulatory Investigation | Within 48 hours | Specified data types/periods |
| Internal Investigation | Within 72 hours | Specific employees/systems |
| M&A Due Diligence | Within 1 week | All corporate records |
| Employment Dispute | Within 48 hours | Employee records + communications |
| IP Dispute | Within 72 hours | Development records, communications |
| Data Breach Investigation | Immediate | Affected systems/logs |
| Audit Notification | Within 1 week | Records relevant to audit scope |
| Freedom of Information Request | Within 5 days (varies) | Specific requested records |

**Reference Table 2: Legal Hold Communication Matrix (Rows 58-66)**
| Stakeholder | Notification Method | Content Includes |
|-------------|---------------------|------------------|
| IT/Data Team | Email + Ticket | Systems, date ranges, search terms |
| Business Owners | Email + Meeting | Why, what, duration estimate |
| Legal/Compliance | Formal memo | Case details, scope, authority |
| Records Management | System flag | Categories under hold |
| External Counsel | Secure communication | Full case details |
| Executives | Executive summary | Business impact, compliance status |

**Reference Table 3: Hold Management Best Practices (Rows 68-76)**
| Practice | Purpose | Implementation |
|----------|---------|----------------|
| Centralized Hold Registry | Single source of truth | Legal hold database/system |
| Automated Flagging | Prevent accidental deletion | System flags or separate storage |
| Regular Hold Reviews | Release unnecessary holds | Quarterly review meetings |
| Clear Release Process | Controlled return to normal deletion | Legal approval required |
| Documentation Requirements | Audit trail | Who, what, when, why, how long |
| Scope Definition | Avoid over-preservation | Specific data types, date ranges |
| Cost Tracking | Understand hold impact | Storage costs, resource time |

**Exception/Deviation Block (Rows 79-84):**
- Systems without legal hold capability (risk assessment required)
- Historical hold breaches (lessons learned)
- Categories exempt from legal hold (justify)

---

### Sheet 6: Data Subject Requests (GDPR/FADP)

**Purpose:** Assess organization's ability to respond to data subject deletion requests (Right to Erasure)

**Assessment Question:**
*"Can we effectively identify, validate, and execute deletion requests from data subjects within required timeframes?"*

**Policy Reference:** ISMS-POL-A.8.10-S2.1, Section 2.1.5 (Data Subject Request Handling)

**Column Structure:** A-T (20 columns total)
- Columns A-Q: Standard base columns
- Column R: Average Response Time (Days)
- Column S: GDPR/FADP Applicable
- Column T: Request Volume (Last 12 Months)

**Data Entry Rows:** 13 rows (yellow-highlighted) - by data category or system

**Compliance Checklist (Rows 25-45):**

1. Data subject request procedure is documented
2. Request intake channel is clearly communicated (e.g., privacy@company.ch)
3. Identity verification process prevents fraudulent requests
4. Request acknowledgment within 5 business days (GDPR/FADP)
5. Requests fulfilled within 30 days (extendable to 60 days with justification)
6. Search capability across all systems holding personal data
7. Ability to distinguish between deletion obligations and exceptions
8. Third-party/cloud systems included in deletion scope (see A.8.10.3)
9. Backup deletion addressed in response (or timeline communicated)
10. Request tracking system in place (ticket system, CRM, etc.)
11. Responses documented (what was deleted, what was retained, why)
12. Data subjects informed of retention exceptions (e.g., legal obligations)
13. Escalation procedure for complex requests
14. Staff training on data subject request handling
15. Request metrics tracked and reported to DPO/Privacy Officer

**Reference Table 1: GDPR Article 17 Deletion Obligations (Rows 47-59)**
| Condition for Deletion | Organization Must Delete If... | Example |
|------------------------|-------------------------------|---------|
| No longer necessary | Data no longer needed for original purpose | Marketing data after consent withdrawn |
| Consent withdrawn | Individual withdraws consent (no other legal basis) | Newsletter subscription cancellation |
| Objection to processing | Individual objects + no overriding legitimate grounds | Profiling/direct marketing objection |
| Unlawful processing | Data was processed illegally | Processing without valid legal basis |
| Legal obligation | Law requires deletion | Court order, regulatory requirement |
| Child's data | Data collected from child w/o proper consent | Social media account created under age 13 |

**Reference Table 2: GDPR Article 17 Deletion Exceptions (Rows 61-72)**
| Exception | Organization Can Retain If... | Example |
|-----------|------------------------------|---------|
| Freedom of expression | Exercise of freedom of expression/information | Journalistic/academic/artistic purposes |
| Legal obligation | Processing necessary for legal compliance | Tax records (10-year retention) |
| Public interest | Public health, scientific research (safeguarded) | Anonymized medical research data |
| Legal claims | Establishment, exercise, defense of legal claims | Litigation hold, contract disputes |
| Archiving in public interest | Historical, statistical, scientific research (safeguarded) | National archives, public health studies |

**Reference Table 3: FADP (Swiss) Specific Considerations (Rows 74-82)**
| FADP Requirement | Implication for Deletion | Notes |
|------------------|--------------------------|-------|
| Article 6 | Data must be deleted when no longer necessary | Similar to GDPR storage limitation |
| Article 25 | Right to request deletion (with exceptions) | Narrower than GDPR in some cases |
| Article 32 | Right to object to processing | May trigger deletion if no other basis |
| Retention for legal purposes | Swiss OR, Tax Law retention supersedes FADP | 10-year retention often required |
| No explicit timeframe | FADP doesn't specify 30-day deadline | Best practice: align with GDPR (30 days) |
| Cross-border data | Extra-territorial application where applicable | Deletion may involve foreign systems |

**Reference Table 4: Request Response Workflow (Rows 84-94)**
| Step | Action | Timeframe | Responsible Role |
|------|--------|-----------|------------------|
| 1. Receive | Log request in tracking system | Day 0 | Privacy Team |
| 2. Acknowledge | Send acknowledgment to data subject | Within 5 business days | Privacy Team |
| 3. Verify Identity | Validate requestor identity | Within 7 days | Privacy Team |
| 4. Assess Scope | Identify all systems with data subject's data | Within 10 days | IT + Business Owners |
| 5. Check Exceptions | Determine if deletion exceptions apply | Within 15 days | Legal/Compliance |
| 6. Execute Deletion | Delete data across all systems | Within 25 days | IT + Third-Parties |
| 7. Document | Record what was deleted and retained | Day 28 | Privacy Team |
| 8. Respond | Inform data subject of outcome | Day 30 | Privacy Team |
| 9. Follow-Up | Backup deletion (if applicable) | Within 90 days | IT |

**Exception/Deviation Block (Rows 97-102):**
- Systems unable to delete data subject data (document risk)
- Categories with high exception rate (e.g., financial records)
- Requests that exceeded 30-day deadline (root cause analysis)

---

### Sheet 7: Summary Dashboard

**Purpose:** Provide executive-level overview of retention and deletion trigger compliance

**Dashboard Structure:**

**Section 1: Overall Compliance Summary (Rows 3-12)**

| Assessment Area | Total Items | Compliant | Partial | Non-Compliant | Compliance % |
|-----------------|-------------|-----------|---------|---------------|--------------|
| Data Category Registry | =COUNT(Sheet2!F:F)-1 | =COUNTIF(Sheet2!F:F,"✅ Compliant") | =COUNTIF(Sheet2!F:F,"⚠️ Partial") | =COUNTIF(Sheet2!F:F,"❌ Non-Compliant") | =Compliant/Total |
| Retention Schedule Compliance | [Similar formulas] | | | | |
| Deletion Trigger Configuration | [Similar formulas] | | | | |
| Legal Hold Management | [Similar formulas] | | | | |
| Data Subject Requests | [Similar formulas] | | | | |
| **OVERALL A.8.10.1** | =SUM(Total) | =SUM(Compliant) | =SUM(Partial) | =SUM(Non-Compliant) | =SUM(Compliant)/SUM(Total) |

**Compliance Thresholds:**
- ≥ 90% Compliant = 🟢 Green (Excellent)
- 70-89% Compliant = 🟡 Yellow (Needs Improvement)
- < 70% Compliant = 🔴 Red (Critical Attention Required)

**Section 2: Critical Gaps Requiring Immediate Attention (Rows 15-25)**

Auto-populated from all assessment sheets where:
- Status = "❌ Non-Compliant" AND Risk Level = "Critical" OR "High"

| Data Category/Item | Gap Description | Risk Level | Target Completion | Owner |
|-------------------|-----------------|------------|-------------------|-------|
| [Auto-populated from Sheets 2-6] | | | | |

**Section 3: Retention Schedule Coverage (Rows 28-36)**

| Metric | Count/Percentage | Target | Status |
|--------|------------------|--------|--------|
| Total Data Categories Identified | =COUNTA(Sheet2!A:A)-9 | N/A | ℹ️ Info |
| Data Categories with Defined Retention | =COUNTIF(Sheet3!D:D,"<>") | 100% | [Green/Yellow/Red] |
| Data Categories with Legal Basis | =COUNTIF(Sheet3!E:E,"<>") | 100% | [Green/Yellow/Red] |
| Event-Based Retention Categories | =COUNTIF(Sheet3!R:R,"Event-Based") | N/A | ℹ️ Info |
| Categories with PII/SPI | =COUNTIF(Sheet2!T:T,"Yes*") | N/A | ℹ️ Info |
| Categories Pending Review | =COUNTIF(Sheet3!I:I,"<"&TODAY()) | 0 | [Green/Yellow/Red] |

**Section 4: Deletion Trigger Effectiveness (Rows 39-48)**

| Metric | Count/Percentage | Target | Status |
|--------|------------------|--------|--------|
| Categories with Automated Triggers | =COUNTIF(Sheet4!R:R,"Automatic") | ≥ 70% | [Green/Yellow/Red] |
| Categories with Manual Triggers Only | =COUNTIF(Sheet4!R:R,"Manual") | ≤ 30% | [Green/Yellow/Red] |
| Triggers with Legal Hold Integration | =COUNTIF(Sheet4!T:T,"Yes*") | 100% | [Green/Yellow/Red] |
| Trigger Test Failures (Last 12 Months) | [Manual entry] | 0 | [Green/Yellow/Red] |
| Average Trigger Execution Success Rate | [Manual entry or calculated] | ≥ 99% | [Green/Yellow/Red] |

**Section 5: Legal Hold Management Metrics (Rows 51-59)**

| Metric | Count/Value | Notes |
|--------|-------------|-------|
| Active Legal Holds | =SUM(Sheet5!R:R) | Current snapshot |
| Average Hold Duration (Days) | [Manual calculation] | Monitor for stale holds |
| Legal Hold Breaches (Last 12 Months) | [Manual entry] | Target: 0 |
| Systems Without Legal Hold Capability | =COUNTIF(Sheet5!F:F,"❌ Non-Compliant") | Risk assessment required |
| Last Legal Hold Process Test | [Date entry] | Annual testing required |

**Section 6: Data Subject Request Performance (Rows 62-72)**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Requests (Last 12 Months) | =SUM(Sheet6!T:T) | N/A | ℹ️ Info |
| Average Response Time (Days) | =AVERAGE(Sheet6!R:R) | ≤ 30 days | [Green/Yellow/Red] |
| Requests Exceeding 30 Days | =COUNTIF(Sheet6!R:R,">30") | 0 | [Green/Yellow/Red] |
| Systems Unable to Delete Data Subject Data | =COUNTIF(Sheet6!F:F,"❌ Non-Compliant") | 0 | [Green/Yellow/Red] |
| Exception Rate (% requests not fully deleted) | [Manual calculation] | < 20% | [Green/Yellow/Red] |
| GDPR/FADP Applicable Systems | =COUNTIF(Sheet6!S:S,"*GDPR*")+COUNTIF(Sheet6!S:S,"*FADP*") | N/A | ℹ️ Info |

**Section 7: Risk Summary (Rows 75-85)**

| Risk Level | Count of Open Gaps | % of Total Gaps | Priority Action |
|------------|-------------------|-----------------|-----------------|
| Critical | =COUNTIF(Sheets!M:M,"Critical") | [Calculate %] | Immediate escalation |
| High | =COUNTIF(Sheets!M:M,"High") | [Calculate %] | Executive attention |
| Medium | =COUNTIF(Sheets!M:M,"Medium") | [Calculate %] | Planned remediation |
| Low | =COUNTIF(Sheets!M:M,"Low") | [Calculate %] | Monitor |

**Section 8: Remediation Timeline (Rows 88-95)**

| Timeframe | Count of Remediations Due | % Complete | On Track? |
|-----------|---------------------------|------------|-----------|
| Overdue | =COUNTIF(Sheets!L:L,"<"&TODAY()) | [Calculate] | 🔴 Red |
| Next 30 Days | =COUNTIF(Sheets!L:L,">="&TODAY(),"<="&TODAY()+30) | [Calculate] | Status |
| Next 90 Days | =COUNTIF(Sheets!L:L,">="&TODAY()+30,"<="&TODAY()+90) | [Calculate] | Status |
| Beyond 90 Days | =COUNTIF(Sheets!L:L,">"&TODAY()+90) | [Calculate] | Status |

**Section 9: Executive Summary & Recommendations (Rows 98-110)**

**Text block (manually updated by assessor):**

**Overall A.8.10.1 Maturity Level:** [Emerging / Developing / Established / Optimized]

**Key Strengths:**
1. [Example: 95% of data categories have documented retention periods]
2. [Example: Automated deletion triggers implemented for all high-volume systems]
3. [Example: Zero legal hold breaches in the past 12 months]

**Critical Improvement Areas:**
1. [Example: 15% of data categories lack defined legal basis for retention]
2. [Example: Manual deletion processes for 40% of SaaS applications]
3. [Example: Data subject request response time averaging 45 days]

**Top 3 Recommendations:**
1. [Priority 1 action with timeline]
2. [Priority 2 action with timeline]
3. [Priority 3 action with timeline]

**Next Review Date:** [Date, typically annual]

---

### Sheet 8: Evidence Register

**Purpose:** Central repository for linking evidence to assessment findings

**Structure:** 100 pre-formatted rows for evidence tracking

**Column Layout:**

| Column | Header | Width | Type | Purpose |
|--------|--------|-------|------|---------|
| A | Evidence ID | 12 | Text | Unique identifier (e.g., A810.1-001) |
| B | Assessment Sheet | 20 | Dropdown | Which sheet references this evidence |
| C | Related Data Category/Item | 30 | Text | What this evidence supports |
| D | Evidence Type | 20 | Dropdown | Document, Screenshot, Log, Certificate, Email, Report, Other |
| E | Evidence Title/Description | 35 | Text | Brief description of evidence |
| F | File Location/Link | 40 | Text | Network path, URL, or physical location |
| G | Date Created/Collected | 12 | Date | When evidence was generated |
| H | Retention Period | 15 | Dropdown | How long to keep evidence (align with data retention) |
| I | Next Review Date | 12 | Date | When to re-validate evidence |
| J | Owner/Custodian | 20 | Text | Person responsible for evidence |
| K | Notes | 30 | Text | Additional context |

**Evidence Type Dropdown Options:**
- Policy Document
- Procedure Document
- Screenshot/Print Screen
- System Log Export
- Configuration File
- Email Communication
- Meeting Minutes
- Audit Report
- Certificate (Deletion, Compliance)
- Contract/Agreement
- Training Record
- Test Result
- Other

**Assessment Sheet Dropdown Options:**
- Sheet 2: Data Category Registry
- Sheet 3: Retention Schedule Compliance
- Sheet 4: Deletion Trigger Configuration
- Sheet 5: Legal Hold Management
- Sheet 6: Data Subject Requests

**Retention Period Options (for evidence itself):**
- 1 year
- 3 years
- 5 years
- 7 years
- 10 years
- Duration of related data retention + 1 year
- Permanent

**Pre-populated Examples (Rows 10-15):**

| Evidence ID | Sheet | Item | Type | Description |
|-------------|-------|------|------|-------------|
| A810.1-001 | Sheet 3 | Employee Records | Policy Document | HR Data Retention Policy v2.1 |
| A810.1-002 | Sheet 4 | Customer Data | Configuration File | AWS S3 Lifecycle Policy - 7yr deletion |
| A810.1-003 | Sheet 5 | Litigation XYZ | Email | Legal hold notification from General Counsel |
| A810.1-004 | Sheet 6 | GDPR Request #42 | Certificate | Deletion Certificate from Salesforce |
| A810.1-005 | Sheet 3 | Financial Records | Document | Swiss Tax Law Retention Requirements Memo |

**Instructions (Top of sheet):**
*"Use this register to document all evidence supporting your retention and deletion trigger assessments. Reference evidence by ID (Column A) in the 'Evidence Reference' column (Column N) of assessment sheets. Maintain evidence per the retention period specified to support audits."*

---

### Sheet 9: Approval Sign-Off

**Purpose:** Three-level approval workflow for assessment completion

**Structure:**

**Section 1: Document Control (Rows 3-10)**
- Assessment Period: [Date Range]
- Workbook Version: [e.g., 1.0]
- Total Assessment Sheets Completed: [5]
- Overall Compliance %: [Link to Summary Dashboard]
- Critical Gaps Identified: [Count from Summary]
- Assessment Completed By: [Name, Date]

**Section 2: Level 1 Approval - Technical/Operational (Rows 13-22)**
**Role:** Data Protection Officer / Privacy Officer / IT Security Manager

**Approval Statement:**
*"I confirm that this assessment accurately reflects our current retention schedules and deletion trigger implementations as of [Date]. All data categories have been reviewed, gaps have been identified, and remediation plans are in place."*

| Field | Value |
|-------|-------|
| Approver Name | [Text entry] |
| Title/Role | [Text entry] |
| Email | [Text entry] |
| Review Date | [Date picker] |
| Approval Status | [Dropdown: ✅ Approved, ⚠️ Approved with Conditions, ❌ Rejected] |
| Conditions/Comments | [Text area for conditions if applicable] |
| Signature | [Text: "Electronically signed" or physical signature if printed] |

**Section 3: Level 2 Approval - Management (Rows 25-34)**
**Role:** Chief Information Officer / Head of Compliance / Legal Counsel

**Approval Statement:**
*"I acknowledge the findings of this A.8.10.1 assessment and approve the proposed remediation plans. Resources will be allocated to address critical and high-risk gaps within the specified timelines."*

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
**Role:** Chief Executive Officer / Chief Risk Officer / Board Delegate

**Approval Statement:**
*"This assessment has been reviewed at the executive level. The organization's retention and deletion trigger posture is [Acceptable/Needs Improvement/Unacceptable]. The Board/Executive Team has been briefed on critical gaps and remediation commitments."*

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
| Implement remediation plans for critical gaps | [Name] | [Date] | [Pending/In Progress/Complete] |
| Quarterly progress review on remediation | [Name] | [Date] | [Pending] |
| Annual re-assessment of A.8.10.1 | [Name] | [Date + 1 year] | [Scheduled] |
| Update ISMS-POL-A.8.10 if needed | [Name] | [Date] | [Pending/Not Required] |
| Communicate changes to stakeholders | [Name] | [Date] | [Pending] |

**Section 6: Audit Trail (Rows 61-70)**

| Date | Version | Change Description | Changed By |
|------|---------|-------------------|------------|
| [Auto] | 1.0 | Initial assessment completed | [Auto-populate from Section 1] |
| [Entry] | 1.1 | [Example: Updated Sheet 3 with new retention periods] | [Name] |
| [Entry] | 1.2 | [Example: Added 5 new data categories to Sheet 2] | [Name] |

---

## Summary Dashboard - Calculation Notes

### Formula Guidelines

**Compliance Percentage Calculation:**
```
= COUNTIF(SheetX!F:F,"✅ Compliant") / (COUNTA(SheetX!F:F) - 9)
```
*(Subtracting 9 to exclude header and checklist rows)*

**Conditional Formatting for Status Indicators:**
- Green (🟢): Cell value ≥ 90%
- Yellow (🟡): Cell value 70-89%
- Red (🔴): Cell value < 70%

**Auto-Population of Critical Gaps:**
Use array formula or filter function to pull rows where:
- `F = "❌ Non-Compliant"` AND `M = "Critical"` OR `M = "High"`

---

## Workbook Metadata

**File Naming Convention:**
`ISMS-IMP-A.8.10.1_Retention_Deletion_Triggers_YYYYMMDD.xlsx`

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

**Print Settings:**
- Orientation: Landscape for assessment sheets, Portrait for Summary/Evidence
- Print Area: Defined to exclude empty rows beyond data
- Header/Footer: Include Document ID, Page X of Y, Date Printed

---

## Implementation Notes

### For Script Generator (generate_a810_1_retention_triggers.py)

**Key Parameters:**
- Total Sheets: 9
- Data Entry Rows per Assessment Sheet: 13 (yellow-highlighted)
- Evidence Register Rows: 100
- Base Columns: A-Q (17 columns)
- Extended Columns: Varies by sheet (R-T, 3 additional)

**Reusable Components from A.8.23:**
- Style definitions (header, subheader, input_cell, status colors)
- Data validation creator
- Evidence Register generator (identical structure)
- Approval Sign-Off generator (identical structure)
- Freeze panes logic

**A.8.10.1-Specific Components:**
- Retention period dropdown options
- Legal basis dropdown options
- GDPR/FADP reference tables
- Data subject request workflow table
- Trigger type and frequency dropdowns

**Reference Data to Hard-Code:**
- Swiss legal retention requirements (10 years for most business records)
- GDPR Article 17 conditions and exceptions
- Common data categories and retention periods
- Trigger types and patterns

---

## Quality Assurance Checklist

**Before Delivery:**
- [ ] All 9 sheets present and correctly named
- [ ] Column widths optimized for readability
- [ ] Data validations working (test dropdowns)
- [ ] Formulas in Summary Dashboard calculating correctly
- [ ] Yellow highlighting on all data entry cells
- [ ] Freeze panes active on assessment sheets
- [ ] Evidence Register has 100 rows
- [ ] Approval Sign-Off has 3-level workflow
- [ ] Print settings configured
- [ ] File size < 5 MB
- [ ] No vendor-specific references (vendor-neutral confirmed)
- [ ] Instructions sheet complete and clear

---

**END OF SPECIFICATION**

**Related Documents:**
- ISMS-POL-A.8.10-S2.1 (Retention & Deletion Triggers Policy)
- ISMS-IMP-A.8.10.2 (Deletion Methods Assessment) - Next in sequence
- ISMS-REF-A.5.23 (Cloud Service Provider Registry)

**Version:** 1.0  
**Date:** [Approval Date] 
**Status:** Ready for Python Generator Implementation