<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.34.3-UG:framework:UG:a.5.34.3 -->
**ISMS-IMP-A.5.34.3-UG - Data Subject Rights Management Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.34: Privacy and Protection of PII

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Data Subject Rights Management Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.34.3-UG |
| **Related Policy** | ISMS-POL-A.5.34 (Privacy and Pii) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.34 (Privacy and Protection of PII) |
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

- ISMS-POL-A.5.34 (Privacy and Pii)
- ISMS-IMP-A.5.34.1 (PII Identification and Classification Assessment)
- ISMS-IMP-A.5.34.2 (Legal Basis and Lawful Processing Assessment)
- ISMS-IMP-A.5.34.4 (Technical and Organisational Measures (TOMs) Assessment)
- ISMS-IMP-A.5.34.5 (DPIA Assessment)
- ISMS-IMP-A.5.34.6 (Cross Border Transfer Assessment)

---

### Workbook at a Glance

This workbook contains the following 9 sheets:

| Sheet | Purpose |
|-------|---------|
| **Instructions & Legend** | Assessment guidance, rating definitions, and field descriptions |
| **2. DSR Request Inventory** | Comprehensive tracking of all data subject rights requests |
| **3. Request Process. Procedures** | Workflow, identity verification, and response generation procedures |
| **4. SLA Compliance Tracking** | 30-day response timeline adherence monitoring (GDPR/FADP Article 12) |
| **5. Exception & Reject. Tracking** | Tracking of refused or extended DSR requests with justifications |
| **6. Rights-Specific Analysis** | Detailed analysis by rights type (access, erasure, portability, etc.) |
| **7. Evidence Repository** | Evidence collected to support DSR management compliance |
| **Summary Dashboard** | Compliance overview auto-populated from your input data |
| **Approval Sign-Off** | Stakeholder sign-off and approval workflow |

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organisation]'s **data subject rights (DSR) management framework** to ensure compliance with GDPR Articles 15-22, Swiss FADP, and ISO 27001:2022 Control A.5.34.

**Core Assessment Components:**
1. **DSR Request Inventory** - Comprehensive tracking of all data subject rights requests
2. **Request Processing Procedures** - Workflow, identity verification, response generation
3. **SLA Compliance Monitoring** - 30-day response timeline adherence (GDPR/FADP)
4. **Exception and Rejection Tracking** - Documentation of refused requests with legal basis
5. **Rights-Specific Analysis** - Breakdown by right type (access, erasure, portability, etc.)
6. **Response Quality Assessment** - Completeness, clarity, legal accuracy
7. **Evidence Repository** - Supporting documentation for audit readiness

**Assessment Scope:** All data subject rights requests received across all channels (email, web portal, phone, mail) for the assessment period (typically quarterly).

**Assessment Output:** Excel workbook with comprehensive DSR metrics, SLA compliance rates, gap analysis, and remediation plans for ISO 27001 audits.

## Why This Matters

**ISO 27001:2022 Control A.5.34 Requirement:**
> *"Rules for the privacy and protection of PII should be established and implemented in accordance with applicable laws and regulations."*

**Regulatory Context - GDPR Articles 15-22:**

**Article 15 - Right of Access:**
> *"The data subject shall have the right to obtain from the controller confirmation as to whether or not personal data concerning him or her are being processed, and, where that is the case, access to the personal data and the following information: (a) the purposes of the processing; (b) the categories of personal data concerned..."*

**Article 16 - Right to Rectification:**
> *"The data subject shall have the right to obtain from the controller without undue delay the rectification of inaccurate personal data concerning him or her."*

**Article 17 - Right to Erasure ("Right to be Forgotten"):**
> *"The data subject shall have the right to obtain from the controller the erasure of personal data concerning him or her without undue delay... where one of the following grounds applies: (a) the personal data are no longer necessary..."*

**Article 18 - Right to Restriction of Processing:**
> *"The data subject shall have the right to obtain from the controller restriction of processing where one of the following applies: (a) the accuracy of the personal data is contested by the data subject..."*

**Article 20 - Right to Data Portability:**
> *"The data subject shall have the right to receive the personal data concerning him or her, which he or she has provided to a controller, in a structured, commonly used and machine-readable format and have the right to transmit those data to another controller..."*

**Article 21 - Right to Object:**
> *"The data subject shall have the right to object, on grounds relating to his or her particular situation, at any time to processing of personal data concerning him or her which is based on point (e) or (f) of Article 6(1)..."*

**Article 22 - Automated Individual Decision-Making:**
> *"The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her."*

**Swiss FADP - Articles 25-28:**

**Article 25 - Right of Access:**
> *"Every person may request information from the controller as to whether personal data concerning them is being processed."*

**Article 26 - Right to Data Portability:**
> *"The data subject may request that their personal data be handed over or transferred to another controller."*

**Article 27 - Right to Rectification:**
> *"The data subject may request that the controller rectify or destroy incorrect personal data."*

**Article 28 - Right to Object to Data Processing:**
> *"The data subject may object to the processing of their personal data."*

**Article 12(3) - Response Deadline (GDPR):**
> *"The controller shall provide information on action taken on a request under Articles 15 to 22 to the data subject without undue delay and in any event within one month of receipt of the request. That period may be extended by two further months where necessary, taking into account the complexity and number of the requests."*

**Business Impact:**

- **Regulatory Violations:** Failure to respond within 30 days = €10M or 2% annual turnover (GDPR Art. 12(3) violation)
- **Data Subject Complaints:** Unhandled DSRs trigger supervisory authority investigations
- **Audit Failures:** ISO 27001 auditors require documented DSR procedures and SLA evidence
- **Reputational Damage:** Ignoring data subject rights undermines trust and brand
- **Operational Risk:** Inefficient DSR handling consumes resources, increases legal exposure

## Who Should Complete This Assessment

**Primary Responsibility:** Data Protection Officer (DPO) or Privacy Officer

**Required Knowledge:**

- GDPR Articles 15-22 and Swiss FADP Articles 25-28 requirements
- Data subject rights request handling procedures
- Identity verification methods
- SLA tracking and compliance monitoring
- Exception and rejection legal bases (GDPR Art. 17(3), 21(1))

**Support Roles:**

- **Customer Service Team Lead:** Request receipt procedures, identity verification
- **IT Support:** Technical fulfillment (data extraction, system access, data portability)
- **Legal Counsel:** Exception review, rejection legal bases, complex requests
- **Compliance Team:** Evidence management, audit preparation
- **Business Process Owners:** Request scope assessment, data location identification

## Time Estimate

**Total Assessment Time:** 10-15 hours (depending on request volume)

**Breakdown:**

- **Request Data Collection:** 2-3 hours (gather requests from all channels)
- **DSR Request Inventory (Sheet 2):** 4-6 hours (document all requests, identity verification, SLA)
- **Request Processing Procedures (Sheet 3):** 1-2 hours (document workflows)
- **SLA Compliance Tracking (Sheet 4):** Auto-calculated (review metrics)
- **Exception & Rejection Tracking (Sheet 5):** 1-2 hours (document rejected requests)
- **Rights-Specific Analysis (Sheet 6):** Auto-calculated (review quality checks)
- **Evidence Repository (Sheet 7):** 1-2 hours (link supporting documentation)
- **Dashboard Review (Sheet 8):** 30 minutes (interpret metrics)
- **Approval & Sign-Off (Sheet 9):** 1 hour (stakeholder review)

**Pro Tip:** This assessment should be completed QUARTERLY to monitor DSR trends and identify process improvements. Annual assessment is minimum requirement.

## Connection to Policy

This assessment implements **ISMS-POL-A.5.34, Section 2.3 (Data Subject Rights)** which requires:

**Mandatory Policy Requirements:**

- All data subject rights SHALL be supported (access, rectification, erasure, portability, object, restriction, automated decision-making)
- Requests SHALL be logged within 24 hours of receipt
- Identity verification SHALL be performed before fulfilling requests
- Response SHALL be provided within 30 days (GDPR/FADP deadline)
- Exceptions SHALL be documented with legal basis (GDPR Article 17(3), 21(1), etc.)
- Response quality SHALL meet GDPR Article 12 requirements (clear, concise, transparent)
- Request fulfillment SHALL be tracked and evidence retained for audit
- SLA compliance rate target: ≥95%

**Policy Authority:** Data Protection Officer (DPO) / Chief Privacy Officer (CPO)  
**Compliance Status:** Mandatory for all data subject interactions

## Critical: The 7 Data Subject Rights Framework

**⚠️ IMPORTANT - Complete DSR Coverage Required:**

Organisations must support ALL data subject rights under GDPR and Swiss FADP. Failure to implement even one right = compliance violation and regulatory risk.

**The 7 Core Data Subject Rights:**

| # | Right | GDPR/FADP Article | Description | Response Format | SLA |
|---|-------|-------------------|-------------|-----------------|-----|
| **1** | **Access** | GDPR Art. 15, FADP Art. 25 | Provide copy of personal data + processing transparency information | Data export (PDF/JSON) + transparency details | 30 days |
| **2** | **Rectification** | GDPR Art. 16, FADP Art. 27 | Correct inaccurate personal data | Confirmation of correction, updated data | 30 days |
| **3** | **Erasure ("Right to be Forgotten")** | GDPR Art. 17, FADP Art. 27 | Delete personal data when no longer necessary or unlawful | Confirmation of deletion | 30 days |
| **4** | **Restriction of Processing** | GDPR Art. 18 | Suspend processing temporarily while dispute resolved | Confirmation of restriction, lift notification | 30 days |
| **5** | **Data Portability** | GDPR Art. 20, FADP Art. 26 | Receive data in machine-readable format, transmit to another controller | Structured data file (JSON, CSV, XML) | 30 days |
| **6** | **Object to Processing** | GDPR Art. 21, FADP Art. 28 | Stop processing based on legitimate interest (Art. 6(1)(f)) or direct marketing | Confirmation of cessation or justified continuation | Immediate (direct marketing), 30 days (other) |
| **7** | **Automated Decision-Making** | GDPR Art. 22 | Challenge automated decisions, obtain human intervention, express point of view | Human review outcome, explanation of decision logic | 30 days |

**Key Distinctions - Critical for Correct Handling:**

**Access (Art. 15) vs. Portability (Art. 20):**

- **Access:** Comprehensive overview of ALL processing (purpose, categories, recipients, retention, rights, source). Includes data not provided by data subject. Format: Human-readable (PDF, letter).
- **Portability:** ONLY data "provided by data subject" (directly given or observed through use of service). Machine-readable format (JSON, CSV, XML). Subset of access right. May include right to transmit directly to another controller.

**Example:**

- Access request: Customer requests "all data you hold about me" → Provide: account info, purchase history, support tickets, marketing preferences, system logs, IP addresses, cookies.
- Portability request: Customer requests "my data in CSV format to transfer to competitor" → Provide: account info, purchase history (data customer gave you), NOT system logs, IP addresses (not provided by customer).

**Erasure (Art. 17) vs. Restriction (Art. 18):**

- **Erasure:** Permanent deletion. Data cannot be recovered. Typically irreversible.
- **Restriction:** Temporary suspension. Data retained but NOT processed (except storage and with data subject's consent for specific purposes). Used when: accuracy disputed, processing unlawful but data subject opposes erasure, data no longer needed for controller's purposes but data subject needs it for legal claims, data subject objects to processing pending verification of controller's legitimate grounds.

**When to Use Restriction Instead of Erasure:**

- Data subject disputes accuracy → Restrict while verifying accuracy
- Processing potentially unlawful but data subject wants restriction not deletion
- Data subject needs data for legal claims but controller doesn't need it anymore
- Data subject objects to legitimate interest processing → Restrict while assessing objection

**Object (Art. 21) vs. Withdrawal of Consent:**

- **Object:** Used for legitimate interest processing (Art. 6(1)(f)) or public task (Art. 6(1)(e)). Data subject must provide "grounds relating to their particular situation" EXCEPT for direct marketing (unconditional right to object).
- **Withdrawal of Consent:** Used for consent-based processing (Art. 6(1)(a)). Data subject can withdraw consent at any time without providing reasons. Withdrawal does NOT affect lawfulness of past processing.

**Direct Marketing Special Rule (GDPR Art. 21(2-3)):**
> *"Where personal data are processed for direct marketing purposes, the data subject shall have the right to object at any time to processing of personal data concerning him or her for such marketing, which includes profiling to the extent that it is related to such direct marketing."*

**Unconditional right to object to direct marketing:** Must be processed IMMEDIATELY (not subject to 30-day SLA). No balancing test. Data subject does NOT need to provide grounds.

---

# Prerequisites

## Required Inputs

Before starting this assessment, you must have:

1. **DSR Request Data**

   - Email inbox (e.g., privacy@organisation.com, dpo@organisation.com)
   - Web portal submissions
   - Customer service tickets (if DSRs logged as tickets)
   - Phone call logs (if requests received verbally)
   - Postal mail (if physical letters received)

2. **Request Correspondence**

   - Original request emails/letters
   - Response emails/letters sent to data subjects
   - Identity verification correspondence
   - Extension notifications (if 30-day deadline extended)
   - Rejection notifications (if requests refused)

3. **Identity Verification Records**

   - Verification method used (account login, email confirmation, ID document)
   - Verification outcome (verified, failed, escalated)
   - Verification date

4. **Exception Documentation** (if applicable)

   - Rejected requests with legal basis (GDPR Art. 17(3), Art. 21(1))
   - Extended timelines with justification (Art. 12(3) - complexity, high volume)
   - Fee charges with calculation (Art. 12(5) - manifestly unfounded/excessive)

5. **Communication Templates**

   - Standard response templates for each right type
   - Rejection notification templates
   - Extension notification templates (Art. 12(3) - 2-month extension notice)

## Access Required

You will need access to:

**Systems:**

- [ ] DSR management system (if applicable - e.g., OneTrust, TrustArc, custom CRM module)
- [ ] Email system (to retrieve DSR correspondence)
- [ ] Customer support ticketing system (if DSRs logged as tickets)
- [ ] Data extraction tools (for fulfilling access/portability requests)
- [ ] Identity verification system (e.g., ID verification service, secure portal)

**Documents:**

- [ ] DSR request logs (spreadsheet or database export)
- [ ] Response correspondence (emails, letters, portal messages)
- [ ] Identity verification logs
- [ ] Exception documentation (rejection letters, legal analysis)
- [ ] SLA tracking reports (if available)

**People:**

- [ ] Customer Service Team Lead (for request receipt procedures)
- [ ] IT Support (for technical fulfillment processes, data extraction, system access)
- [ ] Legal Counsel (for exception review, rejection legal bases)
- [ ] DPO (for oversight, approval, escalation)

## Tools and Resources

**Recommended Resources:**

- **ICO (UK) Guidance:** ["Individual rights guide"](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/individual-rights/)
- **EDPB Guidelines:** Guidelines 01/2022 on data subject rights - Right of access
- **EDPB Guidelines:** Guidelines 2/2019 on Article 6(1)(b) (contractual necessity - relevant for portability scope)
- **Swiss FDPIC:** Guidance on data subject rights under FADP
- **Art. 29 Working Party:** Opinion on automated individual decision-making and profiling (relevant for Art. 22)
- **CNIL (France):** Guidance on data portability (machine-readable formats)

**Assessment Workbook Sheets:**
1. **Instructions & Legend** - This guide, assessment methodology, legal framework
2. **DSR Request Inventory** - Complete list of all requests received (main data entry sheet)
3. **Request Processing Procedures** - Workflow documentation and quality checks
4. **SLA Compliance Tracking** - 30-day timeline monitoring (auto-calculated)
5. **Exception & Rejection Tracking** - Refused requests with legal basis
6. **Rights-Specific Analysis** - Breakdown by right type (access, erasure, etc.) with quality metrics
7. **Evidence Repository** - Supporting documentation for audit
8. **Dashboard** - Compliance metrics and KPIs (executive summary)
9. **Approval & Sign-Off** - Stakeholder review and approval

---

# Assessment Workflow

## High-Level Process

**Phase 1: Preparation (2-3 hours)**
→ Read User Guide
→ Gather all DSR requests from channels
→ Collect correspondence and identity verification records
→ Review ISMS-POL-A.5.34 Section 2.3

**Phase 2: DSR Request Inventory (4-6 hours)**
→ Document all requests in Sheet 2
→ Track identity verification for each request
→ Record response dates and SLA compliance
→ Link to evidence in Sheet 7

**Phase 3: Request Processing Procedures (1-2 hours)**
→ Document workflows in Sheet 3
→ Quality checks for each right type
→ Exception handling procedures

**Phase 4: SLA Compliance Review (30 minutes)**
→ Review auto-calculated metrics in Sheet 4
→ Identify SLA breaches and root causes
→ Document corrective actions

**Phase 5: Exception & Rejection Tracking (1-2 hours)**
→ Document all rejected/restricted requests in Sheet 5
→ Verify legal basis for each exception
→ Confirm data subject notification and appeal rights communicated

**Phase 6: Rights-Specific Analysis (30 minutes)**
→ Review auto-calculated metrics in Sheet 6
→ Quality checks for each of the 7 rights
→ Identify common issues and process improvements

**Phase 7: Evidence Collection (1-2 hours)**
→ Register all supporting documentation in Sheet 7
→ Link evidence to specific requests in Sheet 2

**Phase 8: Dashboard Review (30 minutes)**
→ Interpret executive metrics in Sheet 8
→ Prepare management presentation

**Phase 9: Approval & Sign-Off (1 hour)**
→ Stakeholder review (DPO, Legal Counsel, Customer Service Lead)
→ Obtain sign-offs in Sheet 9
→ Finalize and archive assessment

---

# Step-by-Step Completion Instructions

## SHEET 1: Instructions & Legend

**Purpose:** Reference guide for assessment completion

**What to Do:**
1. Read this sheet first to understand DSR framework and the 7 rights
2. Review SLA requirements (30-day deadline, extension rules)
3. Understand dropdown options and validation rules
4. Note any organisation-specific customizations

**No data entry required on this sheet.**

---

## SHEET 2: DSR Request Inventory

**Purpose:** Document ALL data subject rights requests received during assessment period

**Step 1: Import Request Data**

Gather all DSR requests from:

- Email inbox (e.g., privacy@organisation.com, dpo@organisation.com)
- Web portal submissions (if online DSR form available)
- Customer service tickets (if DSRs logged in ticketing system)
- Phone call logs (if requests received verbally - GDPR allows oral requests)
- Postal mail (if physical letters received)

**For EACH request, record:**

**Column A - Request ID:** Unique identifier

- Format: DSR-YYYY-####
- Example: DSR-2026-0001, DSR-2026-0002
- Sequential numbering ensures auditability

**Column B - Receipt Date:** When request was received

- Format: YYYY-MM-DD (ISO date format)
- **Critical for SLA calculation:** 30-day clock starts from receipt date
- If request received via multiple channels, use earliest receipt date

**Column C - Request Channel:** How request was received

- Dropdown: Email, Web Portal, Phone, Postal Mail, In-Person
- Helps identify channel trends (e.g., most requests via email → improve email handling)

**Column D - Right Type:** Which right was exercised

- Dropdown: Access (Art. 15), Rectification (Art. 16), Erasure (Art. 17), Restriction (Art. 18), Data Portability (Art. 20), Object (Art. 21), Automated Decision-Making (Art. 22)
- **If multiple rights in single request:** Create separate rows for each right (e.g., DSR-2026-0001a for access, DSR-2026-0001b for erasure)

**Column E - Requester Name:** Data subject's name

- Use name as provided in request
- If anonymous request (rare), enter "Anonymous - Identity Verification Pending"

**Column F - Requester Contact:** Email or phone

- Primary contact method for response
- Used for identity verification and response delivery

**Column G - Request Description:** Brief summary of request (2-3 sentences)

**Examples:**

- "Request for copy of all personal data held, including account information, purchase history, and support tickets."
- "Request to delete account and all associated data. Reason: No longer using service."
- "Object to processing for direct marketing purposes. Wants email/SMS marketing stopped immediately."
- "Request data in CSV format for account portability to competitor service."

**Column H - Request Scope:** Systems/data categories involved

- Helps determine complexity and effort required

**Examples:**

- "Customer account data (CRM), purchase history (e-commerce platform), support tickets (Zendesk)"
- "Employee HR records (BambooHR), payroll data (ADP), time tracking (Toggl)"
- "Marketing preferences (Mailchimp), website analytics (Google Analytics cookies)"

---

## Step 2: Track Identity Verification (Columns I-K)

**GDPR Article 12(6) Requirement:**
> *"Without prejudice to Article 11, where the controller has reasonable doubts concerning the identity of the natural person making the request referred to in Articles 15 to 21, the controller may request the provision of additional information necessary to confirm the identity of the data subject."*

**Purpose:** Prevent unauthorised disclosure of personal data to wrong person.

**Column I - Identity Verification Method:**

- Dropdown: Account Login, Email Confirmation, ID Document, Phone Verification, In-Person, Not Required

**When to Use Each Method:**

- **Account Login:** Data subject logs into account → Identity verified through existing authentication
- **Email Confirmation:** Send verification link/code to email on file → Data subject confirms
- **ID Document:** Request copy of government-issued ID (passport, driver's license) → Verify against account details
- **Phone Verification:** Call data subject at phone number on file → Ask security questions
- **In-Person:** Data subject visits office in person → Present ID
- **Not Required:** Request from authenticated account with no reasonable doubts

**Column J - Verification Status:**

- Dropdown: Verified, Verification Failed, Verification Pending, Not Required

**Column K - Verification Date:**

- Format: YYYY-MM-DD
- Date when identity verification completed

**⚠️ CRITICAL:** Do NOT fulfill request until identity verified. Unauthorised disclosure = GDPR Art. 5(1)(f) violation (integrity and confidentiality principle).

---

## Step 3: Document Response and Fulfillment (Columns L-P)

**Column L - Assigned To:** Who is handling the request?

- Name of person responsible for fulfilling request
- Enables accountability and workload tracking

**Column M - Response Date:** When was response sent to data subject?

- Format: YYYY-MM-DD
- **Used for SLA compliance calculation**

**Column N - Days to Respond:** Auto-calculated

- Formula: `=M2-B2` (Response Date - Receipt Date)
- Shows number of days taken to respond

**Column O - SLA Status:** Auto-calculated

- Formula: `=IF(M2="", "Pending", IF(N2<=30, "Met", "Breached"))`
- Dropdown: Met, Breached, Pending, Extended (if 2-month extension granted per Art. 12(3))

**Column P - Response Method:** How was response delivered?

- Dropdown: Email, Secure Portal, Postal Mail, In-Person, Download Link
- **Best practice:** Secure portal or encrypted email for access/portability responses (data security)

---

## Step 4: Document Request Outcome (Columns Q-S)

**Column Q - Request Outcome:**

- Dropdown: Fulfilled, Partially Fulfilled, Rejected, Extended, Withdrawn

**When to Use Each:**

- **Fulfilled:** Request fully satisfied. All requested actions completed.
- **Partially Fulfilled:** Only part of request satisfied. Example: Access to some systems provided, but others excluded due to third-party personal data.
- **Rejected:** Request refused with legal basis. Example: Erasure rejected due to legal obligation (GDPR Art. 17(3)(b)).
- **Extended:** 2-month extension granted due to complexity/high volume (GDPR Art. 12(3)). Data subject notified.
- **Withdrawn:** Data subject withdrew request before fulfillment.

**Column R - Fulfillment Details:** What was provided/done?

**Examples:**

- "Provided PDF export of account data, purchase history, and support tickets. Sent via secure download link."
- "Deleted account, purchase history, and marketing preferences. Retained transaction records for 7 years per tax law."
- "Corrected shipping address from '123 Old St' to '456 New Ave' in CRM and billing system."
- "Provided CSV file with account info, purchase history. Excluded system logs per GDPR Art. 20(3) (not data provided by data subject)."

**Column S - Rejection Reason:** If rejected, what is legal basis?

**GDPR Article 17(3) - Exceptions to Right to Erasure:**

- (a) Exercise of right to freedom of expression and information
- (b) Compliance with legal obligation (e.g., tax records, employment law)
- (c) Public interest in public health
- (d) Archiving purposes in public interest, scientific/historical research, statistics
- (e) Establishment, exercise, defense of legal claims

**GDPR Article 21(1) - Objection to Legitimate Interest:**
> *"Where personal data are processed for direct marketing purposes, the data subject shall have the right to object at any time..."*

Controller can refuse objection to legitimate interest processing (NOT direct marketing) if:
> *"...the controller demonstrates compelling legitimate grounds for the processing which override the interests, rights and freedoms of the data subject or for the establishment, exercise or defence of legal claims."*

**Dropdown: Legal Obligation (Art. 17(3)(b) - Tax, Employment Law), Legal Claims (Art. 17(3)(e) - Litigation, Defense), Public Interest (Art. 17(3)(d) - Research, Statistics), Freedom of Expression (Art. 17(3)(a)), Vital Interests (Art. 17(1)(d)), Manifestly Unfounded/Excessive (Art. 12(5)), Other**

**Example Rejection Justification:**
> "Erasure request rejected. Requester is current employee. Swiss Code of Obligations Art. 328b requires retention of personnel records during employment and for 10 years after termination for potential legal claims. Legal basis: GDPR Art. 17(3)(b) (legal obligation) and 17(3)(e) (defense of legal claims). Data subject informed of rejection, reason, and right to complain to FDPIC."

---

## Step 5: Track Effort and Complexity (Columns T-U)

**Column T - Estimated Effort (Hours):** How much time required?

- Used for resource planning and process improvement

**Typical Effort by Right Type:**

- Access: 2-4 hours (data extraction from multiple systems)
- Rectification: 0.5-1 hour (update single field)
- Erasure: 1-3 hours (delete from multiple systems, notify third parties per Art. 19)
- Restriction: 1-2 hours (flag account, configure processing restrictions)
- Data Portability: 3-5 hours (extract, transform to machine-readable format)
- Object: 0.5-2 hours (stop processing, assess compelling legitimate grounds)
- Automated Decision-Making: 2-4 hours (human review, explain decision logic)

**Column U - Complexity:**

- Dropdown: Low, Medium, High, Very High

**Factors Affecting Complexity:**

- Number of systems involved (1 system = Low, 5+ systems = High)
- Data volume (100 records = Low, 10,000+ records = High)
- Special category data involved (Yes = +1 complexity level)
- Third-party data sharing (requires Art. 19 notifications = +1 level)
- Legal uncertainty (novel request, unclear legal basis = High)

---

## Step 6: Link to Evidence and Notes (Columns V-W)

**Column V - Evidence Reference:** Link to supporting documentation

- Format: "EV-A533-###" (matches Evidence ID in Sheet 7)
- Example: "EV-A533-001, EV-A533-005"

**Column W - Notes:** Any additional context

**Examples:**

- "Requester initially provided insufficient ID. Requested passport copy. Verified on 2026-01-15."
- "Extended deadline by 2 months due to high volume (50+ requests in January). Data subject notified on 2026-01-20."
- "Consulted Legal Counsel on erasure rejection. Confirmed legal obligation applies per employment law."

---

## SHEET 3: Request Processing Procedures

**Purpose:** Document standardized workflow for each right type to ensure consistency

**For EACH of the 7 Rights:**

## Right 1: Access (GDPR Art. 15) - Procedure Documentation

**Procedure Steps:**
1. Verify identity (Column I-K in Sheet 2)
2. Identify all systems holding data subject's personal data (consult ROPA from A.5.34.1)
3. Extract data from each system (CRM, HRIS, e-commerce, marketing automation, etc.)
4. Compile transparency information (GDPR Art. 15(1)):

   - Processing purposes
   - Categories of personal data
   - Recipients or categories of recipients
   - Retention periods
   - Data subject rights (rectification, erasure, restriction, object, complain)
   - Source of data (if not collected from data subject)
   - Existence of automated decision-making (Art. 22)
   - Appropriate safeguards for transfers to third countries (Art. 46)

5. Redact third-party personal data (GDPR Art. 15(4))
6. Provide copy in "intelligible form" (PDF, readable format)
7. Send response via secure method (encrypted email, secure portal)

**Quality Checks:**

- [ ] All required transparency information included (Art. 15(1)(a)-(h))?
- [ ] Data provided in intelligible form (human-readable)?
- [ ] Third-party personal data redacted?
- [ ] All systems checked (no data sources missed)?
- [ ] Response sent within 30 days of receipt?

**Common Issues:**

- Incomplete data exports (missed systems) → Use ROPA to ensure all systems checked
- Lack of transparency information (just data dump) → Include all Art. 15(1) information
- Excessive response time (complex data architecture) → Automate data extraction where possible

**Tools Used:**

- Data extraction scripts/tools
- ROPA (from A.5.34.1) to identify all data locations
- Secure file transfer (encrypted email, secure portal)

---

## Right 2: Rectification (GDPR Art. 16) - Procedure Documentation

**Procedure Steps:**
1. Verify identity
2. Identify data to be corrected (which field, which system)
3. Verify data subject's claim (is current data actually inaccurate?)
4. If accuracy disputed: Consider restriction (Art. 18) while verifying
5. Update data in all systems holding the information
6. Notify third parties of correction per GDPR Art. 19 (if data was disclosed)
7. Confirm correction to data subject

**Quality Checks:**

- [ ] Correction propagated to ALL systems holding the data?
- [ ] Third parties notified of correction (Art. 19)?
- [ ] Data subject informed of correction completion?
- [ ] If correction disputed: Was restriction applied during verification?

**Common Issues:**

- Correction in one system but not others (data inconsistency) → Use centralized data management or sync processes
- Failure to notify third parties (Art. 19 violation) → Maintain recipient list in ROPA

**Art. 19 Requirement:**
> *"The controller shall communicate any rectification or erasure of personal data or restriction of processing carried out in accordance with Article 16, Article 17(1) and Article 18 to each recipient to whom the personal data have been disclosed, unless this proves impossible or involves disproportionate effort."*

---

## Right 3: Erasure (GDPR Art. 17) - Procedure Documentation

**Procedure Steps:**
1. Verify identity
2. Check if any Art. 17(3) exceptions apply (legal obligation, legal claims, etc.)
3. If exception applies: Reject request with documented legal basis (see Sheet 5)
4. If no exception: Delete data from all systems
5. Notify third parties of erasure per Art. 19 (if data was disclosed)
6. Confirm deletion to data subject
7. Retain record of deletion for audit trail (NOT the personal data itself)

**Quality Checks:**

- [ ] All Art. 17(3) exceptions considered?
- [ ] Data deleted from ALL systems (production, backups, archives)?
- [ ] Third parties notified (Art. 19)?
- [ ] Deletion audit trail retained (for compliance evidence)?
- [ ] If rejected: Legal basis documented, data subject informed of rejection and appeal rights?

**Common Issues:**

- Data retained in backups (GDPR allows reasonable time for backup deletion but active restoration prohibited)
- Failure to assess Art. 17(3) exceptions (arbitrary deletion may violate legal obligations)
- No audit trail of deletion (cannot prove compliance)

**Backup Restoration Prohibition:**
Even if data remains in backups, controller MUST NOT actively restore it for processing purposes. Data is considered "deleted" if no longer accessible for processing.

---

## Right 4: Restriction (GDPR Art. 18) - Procedure Documentation

**Procedure Steps:**
1. Verify identity
2. Determine reason for restriction (Art. 18(1)):

   - (a) Accuracy contested by data subject → Restrict while verifying
   - (b) Processing unlawful but data subject opposes erasure → Restrict instead of delete
   - (c) Controller no longer needs data but data subject needs it for legal claims → Restrict
   - (d) Data subject objected to processing → Restrict pending verification of controller's legitimate grounds

3. Configure systems to prevent processing (except storage)
4. Inform data subject when restriction will be lifted (Art. 18(3))
5. Obtain data subject's consent before lifting restriction (Art. 18(2))

**Quality Checks:**

- [ ] Processing fully restricted (only storage allowed)?
- [ ] Data subject informed of restriction in place?
- [ ] Data subject informed when restriction will be lifted?
- [ ] Consent obtained before lifting restriction?

**Art. 18(2) - Permitted Processing During Restriction:**
> *"Where processing has been restricted under paragraph 1, such personal data shall, with the exception of storage, only be processed with the data subject's consent or for the establishment, exercise or defence of legal claims or for the protection of the rights of another natural person or legal person or for reasons of important public interest of the Union or of a Member State."*

---

## Right 5: Data Portability (GDPR Art. 20) - Procedure Documentation

**Procedure Steps:**
1. Verify identity
2. Determine scope: ONLY data "provided by data subject" (Art. 20(1))

   - Includes: Data directly given (registration info, profile data) + data observed through use (search history, location data)
   - Excludes: Inferred/derived data (analytics, scores, predictions), system-generated logs

3. Extract data in machine-readable format (JSON, CSV, XML)
4. If requested: Transmit directly to another controller (Art. 20(2))
5. Provide to data subject via secure download link

**Quality Checks:**

- [ ] Only "provided" data included (not inferred/derived data)?
- [ ] Machine-readable format (JSON, CSV, XML)?
- [ ] Structured and commonly used format?
- [ ] If direct transmission requested: Technical feasibility assessed?
- [ ] Third-party personal data excluded (Art. 20(4))?

**Art. 20(3) - Scope Limitation:**
> *"The right to data portability shall not adversely affect the rights and freedoms of others."*

Excludes third-party personal data (e.g., email threads with other people, shared documents).

**Common Formats:**

- JSON (preferred for complex nested data)
- CSV (preferred for tabular data)
- XML (structured data, less common)

---

## Right 6: Object (GDPR Art. 21) - Procedure Documentation

**Procedure Steps:**
1. Verify identity
2. Determine processing legal basis:

   - If **direct marketing (Art. 21(2)):** Stop processing IMMEDIATELY (no balancing test)
   - If **legitimate interest (Art. 6(1)(f)) or public task (Art. 6(1)(e)):** Assess objection grounds

3. If legitimate interest: Conduct balancing test

   - Can controller demonstrate "compelling legitimate grounds that override data subject's interests, rights, freedoms"?
   - Example: Fraud prevention may override objection

4. If no compelling grounds: Stop processing
5. If compelling grounds: Document justification, reject objection, inform data subject

**Quality Checks:**

- [ ] Direct marketing objections processed immediately?
- [ ] Balancing test conducted for legitimate interest objections?
- [ ] If objection refused: Compelling legitimate grounds documented?
- [ ] Data subject informed of outcome and appeal rights?

**Art. 21(1) - Objection Right:**
> *"The data subject shall have the right to object, on grounds relating to his or her particular situation, at any time to processing of personal data concerning him or her which is based on point (e) or (f) of Article 6(1), including profiling based on those provisions."*

**Art. 21(3) - Absolute Right for Direct Marketing:**
> *"Where the data subject objects to processing for direct marketing purposes, the personal data shall no longer be processed for such purposes."*

---

## Right 7: Automated Decision-Making (GDPR Art. 22) - Procedure Documentation

**Procedure Steps:**
1. Verify identity
2. Determine if decision was "solely" automated (no human involvement)
3. Determine if decision produces "legal effects" or "similarly significant effects"
4. If yes to both: Data subject has right to:

   - (a) Obtain human intervention
   - (b) Express their point of view
   - (c) Contest the decision

5. Conduct human review of automated decision
6. Explain decision logic (Art. 13(2)(f), 14(2)(g))
7. Provide outcome of human review

**Quality Checks:**

- [ ] Decision was "solely" automated (no human involvement)?
- [ ] Decision produces legal/significant effects?
- [ ] Human intervention provided?
- [ ] Data subject allowed to express point of view?
- [ ] Decision logic explained?

**Art. 22(1):**
> *"The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her."*

**Examples of Art. 22 Decisions:**

- Automatic loan/credit denial
- Automated recruitment screening (reject without human review)
- Algorithmic performance evaluation (firing decision)
- Automated insurance premium calculation with significant price impact

**NOT Art. 22:**

- Automated decision with human review (human can override)
- Decision without significant effects (product recommendations, non-binding risk scores)

---

## SHEET 4: SLA Compliance Tracking

**Purpose:** Monitor 30-day response deadline adherence (auto-calculated metrics)

**This sheet is FULLY AUTO-CALCULATED. No manual data entry required.**

**Section 1: Overall SLA Compliance (Rows 5-10)**

| Row | Metric | Formula | Cell |
|-----|--------|---------|------|
| 5 | Total Requests | `=COUNTA('2. DSR Request Inventory'!A2:A10000)` | B5 |
| 6 | Requests Met SLA | `=COUNTIF('2. DSR Request Inventory'!O2:O10000, "Met")` | B6 |
| 7 | Requests Breached SLA | `=COUNTIF('2. DSR Request Inventory'!O2:O10000, "Breached")` | B7 |
| 8 | Requests Pending | `=COUNTIF('2. DSR Request Inventory'!O2:O10000, "Pending")` | B8 |
| 9 | SLA Compliance Rate | `=IF(B5-B8=0, 0, B6/(B5-B8))` | B9 |
| 10 | Average Response Time (Days) | `=AVERAGE('2. DSR Request Inventory'!N2:N10000)` | B10 |

**Interpretation:**

- **SLA Compliance Rate Target:** ≥95%
- If <95%: Investigate root causes in Section 3 (SLA Breach Root Cause)
- **Average Response Time Target:** ≤20 days (buffer before 30-day deadline)

**Section 2: Breakdown by Right Type (Rows 12-20)**

For each of the 7 rights, calculate:

- Total requests
- SLA met count
- SLA breached count
- Average response time

**Example Formulas (Access Requests):**

- Total Access Requests: `=COUNTIF('2. DSR Request Inventory'!D2:D10000, "Access*")`
- SLA Met (Access): `=COUNTIFS('2. DSR Request Inventory'!D2:D10000, "Access*", '2. DSR Request Inventory'!O2:O10000, "Met")`
- SLA Breached (Access): `=COUNTIFS('2. DSR Request Inventory'!D2:D10000, "Access*", '2. DSR Request Inventory'!O2:O10000, "Breached")`
- Avg Response Time (Access): `=AVERAGEIF('2. DSR Request Inventory'!D2:D10000, "Access*", '2. DSR Request Inventory'!N2:N10000)`

**Repeat for:** Rectification, Erasure, Restriction, Data Portability, Object, Automated Decision-Making

**Section 3: SLA Breach Root Cause (Rows 22-30)**

**Manual Data Entry Required:**

For each SLA breach, document:

- Request ID (from Sheet 2)
- Right Type
- Days Overdue (how many days past 30-day deadline?)
- Breach Reason (why did breach occur?)
  - Examples: "Complex data extraction from 10+ systems", "Identity verification delayed (requester didn't respond to verification request)", "High request volume (50+ requests in month)", "Technical issue with data extraction tool", "Staff shortage (2 team members on leave)"
- Corrective Action Taken
  - Examples: "Automated data extraction script deployed", "Hired additional DSR coordinator", "Implemented priority queue for urgent requests", "Improved identity verification process (faster turnaround)"

**Purpose:** Root cause analysis enables process improvement and prevents future breaches.

---

## SHEET 5: Exception & Rejection Tracking

**Purpose:** Document rejected/restricted requests with legal basis (GDPR Art. 17(3), 21(1))

**⚠️ CRITICAL:** Arbitrary rejections without legal basis = GDPR violation. Every rejection MUST have documented legal justification.

**For EACH Rejected/Restricted Request, Document:**

**Column A - Request ID:** Link to Sheet 2 (e.g., DSR-2026-0015)

**Column B - Right Type:** Which right was exercised (e.g., Erasure)

**Column C - Exception Legal Basis:**

- Dropdown with GDPR/FADP exception provisions

**Complete Dropdown List:**

- Legal Obligation (Art. 17(3)(b) - Tax, Employment Law)
- Legal Claims (Art. 17(3)(e) - Litigation, Defense)
- Public Interest (Art. 17(3)(d) - Research, Statistics)
- Freedom of Expression (Art. 17(3)(a))
- Vital Interests (Art. 17(1)(d))
- Manifestly Unfounded/Excessive (Art. 12(5))
- Compelling Legitimate Grounds (Art. 21(1) - Override Objection)
- No Direct Transfer (Art. 20(3) - Technical Infeasibility)
- Consent Exception (Art. 17(3) - Processing Based on Consent, Data No Longer Needed)
- Other (specify)

**Column D - Detailed Justification:**

- Specific facts justifying rejection (2-3 sentences minimum)

**Example (Erasure Rejection - Employment Law):**
> "Requester is current employee. Swiss Code of Obligations Art. 328b requires retention of personnel records (employment contract, payroll data, performance reviews) during employment and for 10 years after termination for potential legal claims (wrongful termination, discrimination). Retention necessary to defend against potential employment-related litigation. Legal basis: GDPR Art. 17(3)(b) (legal obligation) and Art. 17(3)(e) (defense of legal claims)."

**Example (Erasure Rejection - Tax Law):**
> "Transaction records (invoices, payment data) must be retained for 7 years per Swiss VAT Act (SR 641.20, Art. 70). Deletion would violate legal obligation. Financial authorities may audit transactions within 7-year period. Legal basis: GDPR Art. 17(3)(b) (compliance with legal obligation)."

**Example (Objection Rejection - Fraud Prevention):**
> "Data subject objected to fraud prevention processing. Controller has compelling legitimate grounds: Fraud prevention protects controller and other customers from financial crime. Without fraud monitoring, controller cannot detect fraudulent transactions, leading to financial losses and security risks. Safeguards in place: Data minimised to transaction patterns only, automated review with human oversight, data retention limited to 90 days. Legal basis: GDPR Art. 21(1) (compelling legitimate grounds override data subject's interests)."

**Column E - Data Subject Notification:**

- Was data subject informed of rejection and reason?
- Dropdown: Yes, No, Pending

**GDPR Art. 12(4) Requirement:**
> *"If the controller does not take action on the request of the data subject, the controller shall inform the data subject without delay and at the latest within one month of receipt of the request of the reasons for not taking action and on the possibility of lodging a complaint with a supervisory authority and seeking a judicial remedy."*

**Column F - Appeal Rights Communicated:**

- Did you inform data subject of right to complain to supervisory authority and seek judicial remedy?
- Dropdown: Yes, No

**⚠️ CRITICAL:** GDPR Art. 12(4) requires informing data subject of appeal rights when rejecting requests. Failure to do so = procedural violation.

**Column G - Alternative Measures Offered:**

- What alternatives were provided (if any)?

**Examples:**

- "Offered restriction of processing instead of erasure (GDPR Art. 18). Data subject accepted."
- "Could not provide full erasure due to legal obligation, but offered to restrict processing for non-essential purposes. Marketing preferences deleted."
- "Portability request rejected (data not 'provided by data subject'), but offered access request (GDPR Art. 15) as alternative. Data subject accepted."

**Column H - DPO Review:**

- Was rejection reviewed by DPO before sending to data subject?
- Dropdown: Yes, No, N/A

**Best Practice:** All rejections should have DPO approval before communication to data subject. Reduces risk of erroneous rejections.

**Column I - Legal Counsel Review:**

- For complex exceptions, was Legal Counsel consulted?
- Dropdown: Yes, No, N/A

**When to Involve Legal Counsel:**

- Novel/untested legal basis
- High-value data subject (litigation risk)
- Ambiguous legal obligation (e.g., conflicting laws)
- Potential regulatory scrutiny

**Column J - Requester Response:**

- Did data subject appeal or accept rejection?
- Dropdown: Accepted, Appealed to Supervisory Authority, Disputed, No Response

**If "Appealed to Supervisory Authority":**

- Escalate to DPO/Legal immediately
- Prepare comprehensive case file for supervisory authority
- May need to reconsider rejection if authority disagrees

---

## SHEET 6: Rights-Specific Analysis

**Purpose:** Deep-dive metrics for each of the 7 rights to identify patterns and quality issues

**This sheet is AUTO-CALCULATED. No manual data entry required.**

**For EACH of the 7 Rights, Calculate:**

## Right 1: Access Requests (GDPR Art. 15) - Metrics

**Section Rows 5-15:**

| Metric | Formula | Purpose |
|--------|---------|---------|
| Total Access Requests | `=COUNTIF('2. DSR Request Inventory'!D2:D10000, "Access*")` | Volume tracking |
| Avg Response Time | `=AVERAGEIF('2. DSR Request Inventory'!D2:D10000, "Access*", '2. DSR Request Inventory'!N2:N10000)` | Identify delays |
| % Requiring Manual Data Extraction | (User input in separate column) | Process improvement opportunity |
| Common Data Categories Requested | (User analysis based on Request Scope) | Identify frequently accessed data |

**Quality Checks (User Assessment):**

- [ ] Did response include all required transparency information (Art. 15(1)(a)-(h))?
  - Processing purposes
  - Data categories
  - Recipients or categories of recipients
  - Retention periods
  - Data subject rights (rectification, erasure, restriction, object, complain)
  - Source of data (if not collected from data subject)
  - Automated decision-making details (if applicable)
  - Appropriate safeguards for cross-border transfers (Art. 46)
- [ ] Was data provided in "intelligible form" (Art. 15(1))?
- [ ] Were third-party personal data redacted (Art. 15(4))?
- [ ] Were all systems checked (no data sources missed)?

**Common Issues Identified:**

- Incomplete data exports (missed systems) → Solution: Use ROPA to systematically check all data locations
- Lack of transparency information (just data dump) → Solution: Create standard transparency template
- Excessive response time (complex data architecture) → Solution: Automate data extraction where possible

---

## Right 2-7: Repeat Similar Analysis

**For each remaining right, calculate:**

- Total requests
- Average response time
- SLA compliance rate
- Common issues identified
- Quality checks specific to that right

**Rectification (Art. 16) Quality Checks:**

- [ ] Correction propagated to all systems holding the data?
- [ ] Third parties notified of correction (Art. 19)?
- [ ] Data subject informed of correction completion?

**Erasure (Art. 17) Quality Checks:**

- [ ] All Art. 17(3) exceptions considered?
- [ ] Data deleted from all systems (production, backups, archives)?
- [ ] Third parties notified (Art. 19)?
- [ ] Deletion audit trail retained?

**Restriction (Art. 18) Quality Checks:**

- [ ] Processing fully restricted (only storage allowed)?
- [ ] Data subject informed when restriction will be lifted?
- [ ] Consent obtained before lifting restriction?

**Data Portability (Art. 20) Quality Checks:**

- [ ] Only "provided" data included (not inferred/derived)?
- [ ] Machine-readable format (JSON, CSV, XML)?
- [ ] Third-party personal data excluded (Art. 20(4))?

**Object (Art. 21) Quality Checks:**

- [ ] Direct marketing objections processed immediately?
- [ ] Balancing test conducted for legitimate interest objections?
- [ ] If objection refused: Compelling legitimate grounds documented?

**Automated Decision-Making (Art. 22) Quality Checks:**

- [ ] Decision was "solely" automated (no human involvement)?
- [ ] Human intervention provided?
- [ ] Data subject allowed to express point of view?
- [ ] Decision logic explained?

---

## SHEET 7: Evidence Repository

**Purpose:** Centralized evidence tracking for DSR audit readiness

**For EACH piece of supporting documentation, record:**

**Column A - Evidence ID:** Unique identifier

- Auto-generated: `="EVID-A533-"&TEXT(ROW()-3,"000")`
- Example: EVID-A533-001, EVID-A533-002

**Column B - Evidence Type:**

- Dropdown: Request Email/Letter, Response Email/Letter, Identity Verification Record, Rejection Notification, Extension Notification, Data Export File, Deletion Confirmation, Correction Confirmation, Restriction Notification, Legal Counsel Opinion, DPO Approval, Other

**Column C - Evidence Description:**

- Brief summary of evidence (2-3 sentences)

**Examples:**

- "Original access request email from john.doe@example.com received 2026-01-10. Requested copy of all personal data."
- "Identity verification: Copy of requester's passport submitted 2026-01-12, verified against account details."
- "Response email with PDF data export sent 2026-01-25 via secure download link."
- "Rejection notification for erasure request (DSR-2026-0023). Legal basis: Employment law retention requirement per Swiss CO Art. 328b."

**Column D - File Location:**

- Full path or URL to evidence file
- Examples:
  - "SharePoint: /Privacy/DSR Requests/2026/Q1/DSR-2026-0001_Request.pdf"
  - "Email: privacy@organisation.com, subject 'DSR Request - John Doe', dated 2026-01-10"
  - "Secure Portal: https://privacy.organisation.com/requests/DSR-2026-0001"

**Column E - Related Request IDs:**

- Comma-separated list of Request IDs from Sheet 2
- Example: "DSR-2026-0001, DSR-2026-0005"

**Column F - Evidence Date:**

- Date of evidence creation/receipt
- Format: YYYY-MM-DD

**Column G - Uploaded By:**

- Name of person who registered evidence
- Accountability and contact for questions

**Column H - Verification Status:**

- Dropdown: Verified, Pending Verification, Expired, Requires Update

**Column I - Verified By:**

- Name of DPO or Privacy Officer who verified evidence
- Ensures evidence quality

**Column J - Verification Date:**

- Date when evidence was verified
- Format: YYYY-MM-DD

**Purpose of Evidence Repository:**
1. **Audit Trail:** Demonstrates compliance to ISO 27001 auditors
2. **Supervisory Authority Inquiries:** Quick response to FDPIC/DPA requests
3. **Legal Defense:** Evidence of proper DSR handling in case of litigation
4. **Process Improvement:** Analyze evidence to identify bottlenecks

---

## SHEET 8: Dashboard

**Purpose:** Executive summary with auto-calculated compliance metrics

**This sheet is FULLY AUTO-CALCULATED. No manual data entry required.**

**Section 1: Executive Summary (Rows 5-12)**

| Metric | Formula | Cell | Target |
|--------|---------|------|--------|
| Total DSR Requests (Quarter) | `=COUNTA('2. DSR Request Inventory'!A2:A10000)` | B5 | N/A |
| SLA Compliance Rate | `=IF(B5-B8=0, 0, B6/(B5-B8))` | B6 | ≥95% |
| Average Response Time (Days) | `=AVERAGE('2. DSR Request Inventory'!N2:N10000)` | B7 | ≤20 days |
| Requests Pending | `=COUNTIF('2. DSR Request Inventory'!O2:O10000, "Pending")` | B8 | N/A |
| Requests Rejected | `=COUNTA('5. Exception & Rejection Tracking'!A2:A1000)` | B9 | N/A |
| Rejection Rate | `=IF(B5=0, 0, B9/B5)` | B10 | ≤5% |
| Critical SLA Breaches (>45 days) | `=COUNTIFS('2. DSR Request Inventory'!N2:N10000, ">45")` | B11 | 0 |
| Evidence Documents Uploaded | `=COUNTA('7. Evidence Repository'!A2:A1000)` | B12 | N/A |

**Section 2: Breakdown by Right Type (Rows 14-22)**

Pie chart or bar chart showing:

- Access: X requests (Y%)
- Rectification: X requests (Y%)
- Erasure: X requests (Y%)
- Restriction: X requests (Y%)
- Data Portability: X requests (Y%)
- Object: X requests (Y%)
- Automated Decision-Making: X requests (Y%)

**Section 3: SLA Compliance Trend (Rows 24-30)**

If multiple quarters assessed, show trend:

- Q1 2026: 92% SLA compliance
- Q2 2026: 94% SLA compliance
- Q3 2026: 97% SLA compliance → Improving trend

**Section 4: Top DSR Channels (Rows 32-36)**

- Email: X% of requests
- Web Portal: Y% of requests
- Phone: Z% of requests
- Postal Mail: A% of requests
- In-Person: B% of requests

**Interpretation:** If 80% of requests via email, prioritize email response process optimization.

**Section 5: Rejection Analysis (Rows 38-44)**

Breakdown of rejection reasons:

- Legal Obligation (Art. 17(3)(b)): X rejections
- Legal Claims (Art. 17(3)(e)): Y rejections
- Manifestly Unfounded/Excessive (Art. 12(5)): Z rejections
- Compelling Legitimate Grounds (Art. 21(1)): A rejections

**Interpretation:** If high rejection rate (>10%), review if legitimate or process improvement needed.

**Section 6: Effort Analysis (Rows 46-50)**

- Average effort per request type (hours)
- Total effort spent on DSR requests (quarter)
- Cost implications (if hourly rate available)

**Interpretation:** If erasure requests consistently high effort (5+ hours), consider automation of deletion process.

---

## SHEET 9: Approval & Sign-Off

**Purpose:** Stakeholder validation and formal approval documentation

**Pre-Populated Required Approvals:**

| Row | Signatory Role | Approval Scope | Signature | Date |
|-----|----------------|----------------|-----------|------|
| 4 | Data Protection Officer (DPO) | DSR procedures, SLA compliance, rejection legal bases, GDPR Art. 12-22 compliance | [User input] | [User input] |
| 5 | Legal Counsel | Exception legal bases, rejection justifications, regulatory compliance | [User input] | [User input] |
| 6 | Customer Service Team Lead | Request handling procedures, identity verification, response quality | [User input] | [User input] |
| 7 | IT Support Lead | Technical fulfillment, data extraction processes, system access | [User input] | [User input] |
| 8 | Executive Sponsor (CPO/CISO) | Final approval, resource allocation, gap remediation commitment | [User input] | [User input] |

**Additional Approvers (Rows 9-15):**

- Add as needed (e.g., Head of Compliance, General Counsel, Business Unit Leads)

**Approval Process:**
1. Complete Sheets 2-7 (data entry and analysis)
2. Review Dashboard (Sheet 8) - prepare executive briefing
3. Schedule approval meetings with stakeholders
4. Present findings, SLA compliance, gaps, recommendations
5. Collect signatures and dates in Sheet 9
6. Finalize and archive assessment

---

# Common Pitfalls

## Identity Verification Issues

**Pitfall:** Skipping identity verification for "low-risk" requests
**Impact:** Unauthorised disclosure = GDPR Art. 5(1)(f) violation (integrity and confidentiality)
**Solution:** Always verify identity unless request from authenticated account with no reasonable doubts

**Pitfall:** Requesting excessive identity verification documents
**Impact:** GDPR Art. 12(6) prohibits "excessive" ID requests. Data subject may complain.
**Solution:** Request only what's necessary to confirm identity (e.g., passport copy if email verification insufficient)

## SLA Compliance Issues

**Pitfall:** Counting 30 days from when request was assigned (not received)
**Impact:** SLA breach. 30-day clock starts from receipt date, not assignment date.
**Solution:** Log requests within 24 hours of receipt. Track receipt date in Column B.

**Pitfall:** Not notifying data subject of extension
**Impact:** GDPR Art. 12(3) requires notifying data subject within 1 month if extending by 2 months.
**Solution:** If extending, send extension notification within 30 days of receipt. Document in Sheet 2.

## Access Request Quality Issues

**Pitfall:** Providing only data export without transparency information
**Impact:** Incomplete access request response. GDPR Art. 15(1) requires transparency info (a)-(h).
**Solution:** Use standard template with all Art. 15(1) information (purposes, categories, recipients, retention, rights, source, automated decisions, safeguards).

**Pitfall:** Including third-party personal data in access response
**Impact:** GDPR Art. 15(4) prohibits adversely affecting rights of others. Disclosing third-party data = violation.
**Solution:** Redact names, contact info, and identifiable information of third parties (e.g., in email threads, shared documents).

## Erasure Request Issues

**Pitfall:** Deleting data without checking Art. 17(3) exceptions
**Impact:** Violating legal obligations (e.g., tax law, employment law). Cannot recover deleted data.
**Solution:** Always check Art. 17(3) exceptions BEFORE deletion. Document in Sheet 5 if rejection applies.

**Pitfall:** Not notifying third parties of erasure (Art. 19)
**Impact:** GDPR Art. 19 violation. Third parties continue processing data that should be erased.
**Solution:** Maintain recipient list in ROPA (A.5.34.1). Notify all recipients when erasure fulfilled.

**Pitfall:** No audit trail of deletion
**Impact:** Cannot prove compliance to auditors. No evidence of deletion.
**Solution:** Retain deletion confirmation, logs, and audit trail (NOT the personal data itself).

## Data Portability Scope Issues

**Pitfall:** Including inferred/derived data in portability export
**Impact:** Exceeds Art. 20 scope. Portability only applies to "provided" data.
**Solution:** Exclude analytics, scores, predictions, system-generated logs. Include only data directly given or observed through use.

**Pitfall:** Providing data in non-machine-readable format (PDF)
**Impact:** GDPR Art. 20(1) requires "structured, commonly used and machine-readable format".
**Solution:** Use JSON, CSV, or XML. NOT PDF (human-readable but not machine-readable).

## Objection Handling Issues

**Pitfall:** Treating direct marketing objections same as legitimate interest objections
**Impact:** Direct marketing objections must be processed IMMEDIATELY (Art. 21(3)). No 30-day SLA.
**Solution:** Flag direct marketing objections for immediate processing. Stop marketing within 24-48 hours.

**Pitfall:** Rejecting legitimate interest objections without balancing test
**Impact:** Arbitrary rejection. Must demonstrate "compelling legitimate grounds" (Art. 21(1)).
**Solution:** Document balancing test in Sheet 5. Show controller's interests override data subject's interests.

## Exception Documentation Issues

**Pitfall:** Generic rejection reasons without specific legal basis
**Impact:** Insufficient justification. Data subject may successfully appeal to supervisory authority.
**Solution:** Cite specific legal provision (e.g., "Swiss Code of Obligations Art. 328b" not just "employment law").

**Pitfall:** Not informing data subject of appeal rights
**Impact:** GDPR Art. 12(4) procedural violation. Data subject may complain to supervisory authority.
**Solution:** Always inform data subject of right to complain to supervisory authority and seek judicial remedy when rejecting requests.

---

# Quality Checklist

## Completeness Checks

**Sheet 2 (DSR Request Inventory):**

- [ ] All requests from assessment period included (email, web portal, phone, mail)
- [ ] Identity verification documented for all requests
- [ ] Response dates and SLA status recorded
- [ ] Request outcomes documented (fulfilled, rejected, extended, withdrawn)
- [ ] Fulfillment details provided for all fulfilled requests
- [ ] Rejection reasons documented for all rejected requests
- [ ] Effort and complexity assessed
- [ ] Evidence references link to Sheet 7

**Sheet 3 (Request Processing Procedures):**

- [ ] Procedures documented for all 7 rights
- [ ] Quality checks specified for each right
- [ ] Common issues identified
- [ ] Tools and resources listed

**Sheet 4 (SLA Compliance Tracking):**

- [ ] Overall SLA compliance rate calculated
- [ ] Breakdown by right type complete
- [ ] SLA breach root causes documented

**Sheet 5 (Exception & Rejection Tracking):**

- [ ] All rejected requests documented
- [ ] Legal basis specified for each rejection
- [ ] Detailed justification provided (2-3 sentences minimum)
- [ ] Data subject notification confirmed
- [ ] Appeal rights communicated
- [ ] DPO review obtained

**Sheet 6 (Rights-Specific Analysis):**

- [ ] Metrics calculated for all 7 rights
- [ ] Quality checks completed
- [ ] Common issues identified

**Sheet 7 (Evidence Repository):**

- [ ] All supporting documentation registered
- [ ] File locations accurate
- [ ] Evidence linked to related requests
- [ ] Verification status updated

**Sheet 8 (Dashboard):**

- [ ] Executive summary metrics reviewed
- [ ] Trends analysed
- [ ] Recommendations documented

**Sheet 9 (Approval & Sign-Off):**

- [ ] DPO approval obtained (mandatory)
- [ ] Legal Counsel approval obtained (mandatory)
- [ ] Customer Service Lead approval obtained
- [ ] IT Support Lead approval obtained
- [ ] Executive Sponsor approval obtained

## Regulatory Compliance Checks

**GDPR Articles 15-22:**

- [ ] All 7 data subject rights supported
- [ ] 30-day response deadline met for ≥95% of requests
- [ ] Identity verification performed (Art. 12(6))
- [ ] Access requests include all Art. 15(1) transparency information
- [ ] Rectification propagated to all systems, third parties notified (Art. 19)
- [ ] Erasure exceptions assessed per Art. 17(3)
- [ ] Restriction only allows storage (Art. 18(2))
- [ ] Data portability provided in machine-readable format (Art. 20(1))
- [ ] Direct marketing objections processed immediately (Art. 21(3))
- [ ] Automated decision-making requests include human intervention (Art. 22(1))
- [ ] Rejected requests include legal basis, data subject informed of appeal rights (Art. 12(4))
- [ ] Extensions justified and data subject notified within 1 month (Art. 12(3))

**Swiss FADP Articles 25-28:**

- [ ] Access requests fulfilled per Art. 25
- [ ] Rectification/deletion fulfilled per Art. 27
- [ ] Objection rights honored per Art. 28
- [ ] Data portability supported per Art. 26

**ISO 27001:2022 Control A.5.34:**

- [ ] DSR procedures documented and implemented
- [ ] Evidence retained for audit
- [ ] SLA compliance monitored and reported

## Quality Assurance Checks

**Access Requests:**

- [ ] All required transparency information included (Art. 15(1)(a)-(h))
- [ ] Data provided in intelligible form (human-readable)
- [ ] Third-party personal data redacted (Art. 15(4))
- [ ] All systems checked (ROPA used to ensure completeness)

**Rectification Requests:**

- [ ] Correction propagated to all systems
- [ ] Third parties notified (Art. 19)
- [ ] Data subject informed of completion

**Erasure Requests:**

- [ ] Art. 17(3) exceptions assessed
- [ ] Data deleted from all systems (production, backups, archives)
- [ ] Third parties notified (Art. 19)
- [ ] Deletion audit trail retained

**Restriction Requests:**

- [ ] Processing fully restricted (only storage allowed)
- [ ] Data subject informed when restriction will be lifted
- [ ] Consent obtained before lifting restriction

**Data Portability Requests:**

- [ ] Only "provided" data included (not inferred/derived)
- [ ] Machine-readable format (JSON, CSV, XML)
- [ ] Third-party personal data excluded (Art. 20(4))

**Objection Requests:**

- [ ] Direct marketing objections processed immediately
- [ ] Balancing test conducted for legitimate interest objections
- [ ] If objection refused: Compelling legitimate grounds documented

**Automated Decision-Making Requests:**

- [ ] Decision was "solely" automated
- [ ] Human intervention provided
- [ ] Data subject allowed to express point of view
- [ ] Decision logic explained

---

# Next Steps After Completion

## Immediate Actions

1. **Review Dashboard (Sheet 8)** - Present executive summary to senior management
2. **Address Critical SLA Breaches** - Investigate and remediate any requests >45 days overdue
3. **Implement Corrective Actions** - Based on SLA breach root causes (Sheet 4)
4. **Update DSR Procedures** - Based on common issues identified (Sheet 6)
5. **Update Communication Templates** - Response letters, rejection notifications based on lessons learned

## Process Improvements

1. **Automate Data Extraction** - If access requests consistently high effort (5+ hours)
2. **Improve Identity Verification** - If verification delays are common SLA breach cause
3. **Enhance ROPA** - Add recipient lists to enable Art. 19 third-party notifications
4. **Train Staff** - Customer Service and IT Support on DSR procedures
5. **Implement DSR Management System** - If manual tracking becoming unmanageable (>20 requests/quarter)

## Quarterly Monitoring

1. **Repeat Assessment Quarterly** - Track SLA compliance trends
2. **Monitor Request Volume** - Increasing requests may indicate data minimisation opportunity or process improvement needed
3. **Track Rejection Rate** - High rejection rate (>10%) may indicate overly broad data collection
4. **Review Effort Trends** - Increasing effort may indicate need for automation

## Integration with Other Assessments

**Feeds Into:**


**Depends On:**

- **ISMS-IMP-A.5.34.1 (PII Identification):** ROPA shows what data exists → enables access/portability fulfillment
- **ISMS-IMP-A.5.34.2 (Legal Basis):** Legal basis determines rejection eligibility (e.g., legal obligation prevents erasure)

## Prepare for Audits

1. **Evidence Ready** - Sheet 7 (Evidence Repository) organised and accessible
2. **Dashboard Metrics Current** - Sheet 8 updated with latest data
3. **Approval Sign-Offs Complete** - Sheet 9 fully executed
4. **Gap Remediation Progress** - Track corrective actions from SLA breaches

---

**END OF USER GUIDE**

---

*"The right to be forgotten is the right to move forward."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
