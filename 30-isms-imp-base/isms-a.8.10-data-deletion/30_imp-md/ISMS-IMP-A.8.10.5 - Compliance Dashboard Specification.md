**ISMS-IMP-A.8.10.5 - Compliance Dashboard Specification**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.10: Information Deletion

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.10.5 |
| **Version** | 1.0 |
| **Assessment Area** | Aggregate Deletion Compliance Metrics & Executive Dashboard |
| **Related Policy** | ISMS-POL-A.8.10 (Master Policy), ISMS-POL-A.8.10, Section 3.5 (Policy Governance) |
| **Purpose** | Provide executive visibility into A.8.10 compliance status by consolidating metrics from all four assessment workbooks into a single dashboard |
| **Target Audience** | Executives (CISO, CIO, CEO), Board of Directors, Audit Committee, Management, External Auditors, Compliance Officers, Regulators |
| **Assessment Type** | Reporting Dashboard & Trend Analysis (NOT data collection) |
| **Review Cycle** | Quarterly Updates (Minimum) or After Major Remediation Milestones |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Compliance Dashboard consolidation workbook | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** Executives, Board Members, Audit Committee, Compliance Officers, Management

---

# Dashboard Overview

## What This Dashboard Is (And Isn't)

**This is a DASHBOARD, not an assessment workbook.**

**What it IS:**

- ✅ **Executive summary** of A.8.10 compliance status across all four assessment areas
- ✅ **Single-page view** for board presentations and audit committee meetings
- ✅ **Trend analysis tool** showing quarterly progress over time
- ✅ **Gap prioritization** highlighting critical findings requiring management attention
- ✅ **Audit defense tool** demonstrating systematic compliance monitoring


**What it is NOT:**

- ❌ NOT a data collection tool (data comes from A.8.10.1-4 assessments)
- ❌ NOT a replacement for detailed assessments (it summarizes them)
- ❌ NOT automatically updated (requires manual quarterly updates)
- ❌ NOT a project management tool (tracks compliance status, not implementation tasks)


**Analogy:** If A.8.10.1-4 are detailed engineering reports, this dashboard is the executive summary presented to the board.

## Why This Matters

**ISO 27001:2022 Clause 9.1 Requirement:**
> *"The organization shall evaluate the information security performance and the effectiveness of the information security management system."*

**Dashboard Purpose:** Enable executives and auditors to answer the question:

> *"Is our organization effectively managing information deletion in compliance with ISO 27001:2022 Control A.8.10, GDPR, and FADP?"*

Without this dashboard:

- ❌ Executives must read 4 detailed assessment workbooks (300+ pages combined)
- ❌ Compliance trends invisible (no quarterly comparison)
- ❌ Critical gaps buried in technical details
- ❌ Board presentations require manual data extraction
- ❌ Auditors spend hours searching for summary metrics


With this dashboard:

- ✅ Executives see compliance status in 5 minutes
- ✅ Quarterly trends show improvement or decline
- ✅ Top 5 critical gaps visible immediately
- ✅ Board presentation ready without additional work
- ✅ Auditors validate compliance in <1 hour


**Regulatory Context:**

- **ISO 27001 Clause 9.3:** "Management review" requires aggregated performance metrics
- **GDPR Article 5.2:** "Accountability" principle requires demonstrable compliance
- **Swiss FADP Article 7:** Data security must be measurable and reportable
- **Board Governance:** Directors need summary metrics to fulfill oversight duties


**Business Impact:**

- **Audit Efficiency:** External auditors spend less time searching for evidence = lower audit costs
- **Risk Management:** Critical gaps visible to management = faster remediation decisions
- **Executive Confidence:** Data-driven compliance reporting = informed risk acceptance
- **Regulatory Defense:** Systematic monitoring demonstrates good faith compliance effort


## Dashboard Scope & Integration

**Source Assessments (What Gets Consolidated):**

| Assessment | Key Metrics Extracted | Update Frequency |
|------------|----------------------|------------------|
| **A.8.10.1** (Retention & Deletion Triggers) | • Retention schedule coverage %<br>• Overdue reviews count<br>• DSR response time<br>• Legal basis gaps | Quarterly |
| **A.8.10.2** (Deletion Methods) | • NIST compliance %<br>• Forensic test pass rate<br>• SSD-specific issues<br>• Method effectiveness | Quarterly |
| **A.8.10.3** (Third-Party & Cloud Deletion) | • Vendor SLA compliance %<br>• Shadow IT count (Tier 9/10)<br>• Certificate quality<br>• DPA coverage | Quarterly |
| **A.8.10.4** (Verification & Evidence) | • Audit readiness score<br>• Certificate quality avg<br>• Audit trail completeness %<br>• Forensic test coverage | Quarterly |

**Dashboard Output:**

- **9 Dashboard Sheets:** Overall compliance, retention health, deletion effectiveness, third-party performance, verification quality, critical gaps, trends, executive summary, approval
- **~40-60 Summary Metrics:** Consolidated from 200+ detailed assessment data points
- **Quarterly Snapshots:** Q1-Q4 trend analysis showing improvement/decline
- **Executive Narrative:** 1-2 page summary for board presentations


## Who Should Complete This Dashboard

**Primary Responsibility:** Compliance Officer / Information Security Officer

**Required Knowledge:**

- Familiarity with all four A.8.10 assessment workbooks (A.8.10.1-4)
- Understanding of which cells in source workbooks contain summary metrics
- Ability to interpret compliance metrics and identify trends
- Executive communication skills (for narrative summary in Sheet 9)


**Support Roles:**

- **Assessors from A.8.10.1-4:** Provide completed source workbooks and clarify metrics
- **Executive Sponsor (CISO/CIO):** Review dashboard before board presentation
- **External Auditor:** Validate dashboard accuracy during certification audits (if applicable)
- **Board Liaison:** Format dashboard for board meeting presentation


**Who USES the Dashboard (Consumers):**

- **Executives (CISO, CIO, CEO):** Overall compliance status and risk exposure
- **Board of Directors / Audit Committee:** Governance oversight and accountability
- **Management:** Remediation prioritization and resource allocation decisions
- **External Auditors:** ISO 27001 certification compliance validation
- **Regulators:** GDPR/FADP compliance demonstration (if requested)


## Time Estimate

**Initial Dashboard Creation:** 3-4 hours

**Breakdown:**

- **Prerequisites Check (30 min):** Ensure all 4 source assessments complete and approved
- **Sheet 2 - Overall Compliance (30 min):** Extract 5 summary metrics from source workbooks
- **Sheets 3-6 - Deep Dive Metrics (90 min):** Extract 10-15 metrics per assessment area (40-60 total)
- **Sheet 7 - Critical Gaps (30 min):** Identify top 5 gaps requiring management attention
- **Sheet 8 - Trend Analysis (15 min):** Document Q1 baseline (subsequent quarters: compare trends)
- **Sheet 9 - Executive Summary (30 min):** Write narrative summary for board presentation
- **Quality Review (15 min):** Validate formulas, check data accuracy, format for presentation


**Quarterly Updates:** 1-2 hours (once baseline established)

**Pro Tip:** First dashboard creation takes longer (3-4 hours). Subsequent quarterly updates are faster (1-2 hours) because formulas and structure are already established.

## Connection to Policy & Assessments

**Policy Authority:** ISMS-POL-A.8.10, Section 3.5 (Policy Governance) requires:

- Regular monitoring of A.8.10 compliance status
- Management review of deletion effectiveness
- Trend analysis to identify systemic issues
- Executive reporting for board oversight


**Assessment Dependencies (CRITICAL):**

**You CANNOT complete this dashboard without:**

- ✅ **A.8.10.1** (Retention & Deletion Triggers) - COMPLETE and APPROVED
- ✅ **A.8.10.2** (Deletion Methods) - COMPLETE and APPROVED
- ✅ **A.8.10.3** (Third-Party & Cloud Deletion) - COMPLETE and APPROVED
- ✅ **A.8.10.4** (Verification & Evidence) - COMPLETE and APPROVED


**If any source assessment is incomplete or not approved:** Dashboard metrics will be inaccurate. Complete source assessments first, then return to dashboard.

---

# Prerequisites

## Required Source Workbooks

Before starting dashboard completion, ensure you have:

**Assessment Workbooks (All 4 Required):**

- [ ] ISMS_A_8_10_1_Retention_Deletion_Triggers_YYYYMMDD.xlsx (APPROVED)
- [ ] ISMS_A_8_10_2_Deletion_Methods_YYYYMMDD.xlsx (APPROVED)
- [ ] ISMS_A_8_10_3_Third_Party_Cloud_YYYYMMDD.xlsx (APPROVED)
- [ ] ISMS_A_8_10_4_Verification_Evidence_YYYYMMDD.xlsx (APPROVED)


**Approval Status Check:**

- [ ] All source workbooks have completed three-level approval (Sheet 9 in each workbook)
- [ ] Approval dates within last 90 days (for quarterly dashboard update)
- [ ] No outstanding critical gaps without remediation plans


**Access to Source Workbooks:**

- [ ] Source workbooks stored in accessible location (not locked/archived)
- [ ] Permission to open and extract data from source workbooks
- [ ] Ability to verify data accuracy by cross-checking formulas


## Required Knowledge

**Technical:**

- Understanding of Excel formulas (AVERAGE, COUNTIF, basic arithmetic)
- Ability to locate specific cells in source workbooks using sheet/cell references
- Basic conditional formatting interpretation (RAG status colors)


**Compliance & Governance:**

- Understanding of ISO 27001 Clause 9.1 (monitoring and measurement)
- Familiarity with GDPR/FADP compliance reporting requirements
- Executive communication skills (translating metrics into narrative)
- Board presentation best practices


**Operational:**

- Knowledge of [Organization]'s A.8.10 implementation status
- Awareness of recent remediation efforts (for trend explanation)
- Understanding of which gaps are actively being addressed
- Familiarity with planned improvements for next quarter


## Tools & Resources

**Dashboard Workbook:**

- Excel workbook: ISMS_A_8_10_5_Compliance_Dashboard_YYYYMMDD.xlsx (generated by Python script)


**Reference Materials:**

- Data Source Mapping Table (in Dashboard Sheet 1 - Instructions)
- Maturity Scoring Model explanation (in Dashboard Sheet 1)
- Source workbook cell reference guide (in Dashboard Sheet 1)


**Optional (For Board Presentations):**

- PowerPoint template for executive summary
- Data visualization tools (if converting to charts/graphs)
- Previous quarter dashboards (for trend comparison)


---

# Dashboard Workflow

## Manual Entry Workflow (The Core Process)

**Design Decision:** This dashboard uses **manual entry** of summary metrics, NOT live formula links across workbooks.

**Why Manual Entry?**

**Advantages:**

- ✅ No broken links if source files renamed/moved
- ✅ Forces conscious review of data (not blind formula propagation)
- ✅ Enables quarterly snapshots without complex file versioning
- ✅ Dashboard remains functional even if source workbooks archived
- ✅ Simpler to maintain and troubleshoot


**Trade-offs:**

- ⚠️ Requires discipline to update quarterly (not automatic)
- ⚠️ Risk of manual entry errors (mitigated by validation formulas)
- ⚠️ Takes 1-2 hours per quarter vs. instant updates


**How It Works:**

1. **Open source workbook** (e.g., A.8.10.1)
2. **Navigate to summary sheet** (typically Sheet 7 - Dashboard in each source workbook)
3. **Locate specific cell** (e.g., "Retention Coverage %" in Cell B5)
4. **Copy value** (Ctrl+C)
5. **Switch to Dashboard workbook** (A.8.10.5)
6. **Navigate to correct destination sheet** (e.g., Sheet 3 - Retention Schedule Health)
7. **Paste value** (Ctrl+V into designated yellow-highlighted cell)
8. **Repeat** for all 40-60 metrics

**Validation:** Dashboard includes formulas that flag inconsistencies (e.g., "Sum of percentages ≠ 100%")

## Recommended Completion Sequence

**Phase 1: Data Extraction (60-90 minutes)**

**Step 1: Sheet 2 - Overall A.8.10 Compliance**

- Extract 5 high-level metrics from each source workbook's summary sheet
- Document overall maturity score, retention coverage, NIST compliance, vendor SLA compliance, audit readiness
- Validate: All 5 metrics populated, no #REF! errors


**Step 2: Sheet 3 - Retention Schedule Health**

- Extract 8-10 retention-specific metrics from A.8.10.1
- Focus on: schedule coverage, overdue reviews, DSR performance, legal basis gaps
- Validate: Metrics align with A.8.10.1 Sheet 7 summary


**Step 3: Sheet 4 - Deletion Method Effectiveness**

- Extract 10 deletion method metrics from A.8.10.2
- Focus on: NIST compliance, forensic test pass rate, SSD-specific issues, method coverage
- Validate: NIST category percentages sum to 100%


**Step 4: Sheet 5 - Third-Party Deletion Performance**

- Extract 8-10 vendor metrics from A.8.10.3
- Focus on: vendor count, SLA compliance, Shadow IT exposure, DPA coverage, certificate quality
- Validate: Shadow IT count matches A.8.10.3 Tier 9/10 total


**Step 5: Sheet 6 - Verification & Evidence Quality**

- Extract 8-10 verification metrics from A.8.10.4
- Focus on: audit readiness, certificate quality, audit trail completeness, forensic coverage
- Validate: Audit readiness aligns with A.8.10.4 Sheet 6 assessment


**Phase 2: Gap Analysis & Trends (30-45 minutes)**

**Step 6: Sheet 7 - Critical Gaps Dashboard**

- Review all source workbooks for Critical/High severity gaps (Column D in Sheets 2-6)
- Identify top 5 gaps requiring management attention
- Document gap description, responsible party, target completion date
- Prioritize by: regulatory risk > operational risk > efficiency gains


**Step 7: Sheet 8 - Trend Analysis**

- If Q1 (first dashboard): Document baseline values, leave Q2-Q4 blank
- If Q2-Q4: Compare current metrics vs. previous quarter(s)
- Calculate trend direction: ↑ (improving), → (stable), ↓ (declining)
- Document significant changes in "Trend Explanation" column


**Phase 3: Executive Communication (30-45 minutes)**

**Step 8: Sheet 9 - Executive Summary**

- Write 1-2 paragraph narrative summary (see Section 4.4 below for guidance)
- Highlight: overall compliance status, top 3 achievements, top 3 concerns, next quarter priorities
- Include: maturity score, critical gaps count, trend direction (improving/stable/declining)
- Target audience: Board members with no technical background


**Step 9: Approval & Publication**

- Complete three-level approval workflow (same as source assessments)
- Export Sheet 9 (Executive Summary) to PDF for board presentation
- Archive completed dashboard in compliance evidence repository
- Schedule next quarterly update (90 days from current)


## Quarterly Update Cadence

**Recommended Schedule:**

| Quarter | Month | Dashboard Completion | Source Assessments Due | Board Presentation |
|---------|-------|---------------------|----------------------|-------------------|
| Q1 | January | End of January | Mid-January | February board meeting |
| Q2 | April | End of April | Mid-April | May board meeting |
| Q3 | July | End of July | Mid-July | August board meeting |
| Q4 | October | End of October | Mid-October | November board meeting |

**Workflow Timeline (Typical Quarter):**

- **Week 1-2:** Complete all 4 source assessments (A.8.10.1-4)
- **Week 3:** Extract metrics into dashboard (A.8.10.5)
- **Week 4:** Review, approve, present to board


**Pro Tip:** Schedule dashboard completion 1 week before board meeting to allow time for questions and revisions.

---

# Question-by-Question Guidance

## Sheet 2: Overall A.8.10 Compliance

**Purpose:** Provide highest-level view for executives who want the "bottom line" in 30 seconds.

**Key Questions Dashboard Users Struggle With:**

**Q: "What's the 'Overall A.8.10 Maturity Score' and how is it calculated?"**

- A: Weighted average of 4 assessment area scores:
  - Retention Schedule Health (25% weight)
  - Deletion Method Effectiveness (25% weight)
  - Third-Party Deletion Performance (25% weight)
  - Verification & Evidence Quality (25% weight)
- **Target:** ≥80/100 (demonstrates effective compliance program)
- **Calculation:** See Section 5.1 (Maturity Scoring Model) for detailed formula


**Q: "What does 'RAG status' mean?"**

- A: Red-Amber-Green traffic light visualization:
  - **Green:** ≥90% compliance / Score ≥80 / "Fully Ready" → Low risk
  - **Amber:** 70-89% compliance / Score 60-79 / "Mostly Ready" → Moderate risk, monitor closely
  - **Red:** <70% compliance / Score <60 / "Partially/Not Ready" → High risk, immediate action required


**Q: "How do I explain 'trend' arrows to the board?"**

- A: Simple comparison vs. last quarter:
  - **↑ (Green up arrow):** Metric improved vs. last quarter → Positive trend
  - **→ (Amber horizontal):** No significant change vs. last quarter → Stable
  - **↓ (Red down arrow):** Metric declined vs. last quarter → Negative trend requiring explanation


**Common Mistakes to Avoid:**

1. ❌ **Confusing "maturity score" with "compliance percentage"**

   - Maturity score = holistic program effectiveness (0-100 scale)
   - Compliance percentage = specific metric achievement (0-100%)
   - They're related but measured differently


2. ❌ **Ignoring amber (yellow) statuses**

   - Amber = "we're functional but not great" → Often overlooked until it becomes red
   - Amber should trigger preventive action, not just monitoring


3. ❌ **Not explaining trends**

   - Red down arrow without explanation = looks like lack of management attention
   - Always document WHY trends changed in Sheet 8 (Trend Analysis)


## Sheet 3: Retention Schedule Health (from A.8.10.1)

**Purpose:** Deep dive into retention schedule coverage and data subject rights performance.

**Key Metrics to Extract:**

| Metric | Source Workbook | Source Sheet | Source Cell | Dashboard Cell |
|--------|-----------------|--------------|-------------|----------------|
| Total Data Categories | A.8.10.1 | Sheet 7 (Dashboard) | B5 | Sheet 3, B5 |
| Categories with Retention Schedules | A.8.10.1 | Sheet 7 | B6 | Sheet 3, B6 |
| Retention Coverage % | A.8.10.1 | Sheet 7 | B7 (formula) | Sheet 3, B7 |
| Overdue Schedule Reviews | A.8.10.1 | Sheet 7 | B8 | Sheet 3, B8 |
| Average DSR Response Time (days) | A.8.10.1 | Sheet 7 | B12 | Sheet 3, B12 |
| DSR Requests On Time % | A.8.10.1 | Sheet 7 | B13 | Sheet 3, B13 |
| Data Categories Without Legal Basis | A.8.10.1 | Sheet 7 | B11 | Sheet 3, B11 |

**Key Questions:**

**Q: "What's considered 'good' retention coverage?"**

- A: **100% is the only acceptable target** for organizations processing personal data
- GDPR Article 5.1(e) requires ALL personal data categories to have defined retention periods
- Anything <100% = non-compliance with storage limitation principle


**Q: "How many overdue reviews are acceptable?"**

- A: **Zero is the target**
- Overdue reviews indicate retention schedules may be outdated → retention periods may be incorrect
- Typical threshold: >5 overdue reviews = Critical gap requiring immediate action


**Q: "What's the GDPR requirement for DSR response time?"**

- A: **30 days maximum** (extendable to 60 days in complex cases with notification)
- Average >30 days = systematic non-compliance
- Acceptable targets: <20 days average (buffer for complex cases)


**Common Mistakes:**

1. ❌ **Accepting <100% retention coverage as "good enough"**

   - "We have 95% coverage" = 5% of data categories have no legal retention basis = GDPR violation
   - Always target 100% for personal data


2. ❌ **Not distinguishing between "no retention schedule" vs. "overdue review"**

   - No schedule = critical gap (data may be kept indefinitely)
   - Overdue review = medium gap (schedule exists but may be outdated)


## Sheet 4: Deletion Method Effectiveness (from A.8.10.2)

**Purpose:** Evaluate whether [Organization]'s deletion methods meet NIST SP 800-88 standards.

**Key Metrics to Extract:**

| Metric | Source | Dashboard Cell | Target |
|--------|--------|----------------|--------|
| Total Deletion Methods in Use | A.8.10.2 Sheet 7 | B5 | Documented |
| NIST-Compliant Methods Count | A.8.10.2 Sheet 7 | B6 | 100% |
| NIST Compliance % | A.8.10.2 Sheet 7 | B7 | 100% |
| Forensic Test Pass Rate % | A.8.10.2 Sheet 7 | B8 | ≥95% |
| Clear Methods % (NIST Category) | A.8.10.2 Sheet 7 | B10 | Documented |
| Purge Methods % (NIST Category) | A.8.10.2 Sheet 7 | B11 | Documented |
| Destroy Methods % (NIST Category) | A.8.10.2 Sheet 7 | B12 | Documented |
| SSD-Specific Issues Count | A.8.10.2 Sheet 7 | B14 | 0 |
| Crypto-Erasure Implemented? | A.8.10.2 Sheet 7 | Text field | Yes/No |

**Key Questions:**

**Q: "What does 'NIST compliance %' actually measure?"**

- A: Percentage of deletion methods that align with NIST SP 800-88 categories (Clear/Purge/Destroy)
- Non-compliant methods = custom approaches not validated per NIST standards
- **Target:** 100% (all methods must be NIST-validated for audit readiness)


**Q: "What's an acceptable forensic test pass rate?"**

- A: **≥95% is industry standard**
- <95% = systematic issues with deletion methods or testing procedures
- <80% = critical gap requiring immediate investigation


**Q: "Why do SSD-specific issues matter?"**

- A: SSDs cannot be reliably deleted using HDD methods (overwriting doesn't work due to wear-leveling)
- SSD-specific issues count = number of SSDs being deleted with HDD methods
- **Target:** 0 issues (all SSDs use crypto-erase or physical destruction)


**Common Mistakes:**

1. ❌ **Assuming "we delete data" = NIST compliant**

   - Deletion method must be specifically validated against NIST SP 800-88
   - "Empty recycle bin" ≠ NIST Clear/Purge/Destroy


2. ❌ **Not tracking NIST category distribution**

   - Different data classifications require different NIST categories
   - Public data: Clear (OK), Confidential data: Purge/Destroy (required)


## Sheet 5: Third-Party Deletion Performance (from A.8.10.3)

**Purpose:** Monitor vendor compliance with deletion SLAs and identify Shadow IT exposure.

**Key Metrics to Extract:**

| Metric | Source | Dashboard Cell | Target |
|--------|--------|----------------|--------|
| Total Vendors with Data | A.8.10.3 Sheet 7 | B5 | Documented |
| Vendors with Deletion SLAs | A.8.10.3 Sheet 7 | B6 | 100% |
| Vendor SLA Compliance % | A.8.10.3 Sheet 7 | B7 | ≥95% |
| Shadow IT Instances (Tier 9/10) | A.8.10.3 Sheet 7 | B8 | 0 |
| DPA Coverage % | A.8.10.3 Sheet 7 | B10 | 100% |
| Strong Deletion Clauses % | A.8.10.3 Sheet 7 | B11 | ≥80% |
| Certificate Quality Score | A.8.10.3 Sheet 7 | B12 | ≥4.0 |

**Key Questions:**

**Q: "What's the difference between 'vendors with SLAs' and 'SLA compliance'?"**

- A: 
  - **Vendors with SLAs:** Percentage of vendors who have contractual deletion timelines (target: 100%)
  - **SLA Compliance:** Percentage of vendors who actually meet their SLAs (target: ≥95%)
  - Example: 100% have SLAs, but only 80% comply → 20% vendors breach timelines


**Q: "Why is Shadow IT (Tier 9/10) such a big deal?"**

- A: Tier 9/10 = Unauthorized systems processing sensitive/confidential data
  - [Organization] has NO contractual control over deletion
  - May violate GDPR Article 28 (processor agreements required)
  - Deletion requests may be impossible to enforce
  - **Target:** 0 Shadow IT instances with sensitive data


**Q: "What's a 'strong deletion clause'?"**

- A: Contract language that includes:
  - Specific deletion timeline (e.g., "30 days after termination")
  - Deletion method specification (NIST Purge or Destroy)
  - Certificate of deletion required
  - Audit rights to verify deletion
  - See A.8.10.3 assessment for scoring rubric


**Common Mistakes:**

1. ❌ **Ignoring Shadow IT because "users will always find workarounds"**

   - Shadow IT with sensitive data = GDPR processor violation
   - Must be discovered, assessed, and either formalized or shut down


2. ❌ **Accepting weak deletion clauses as "good enough"**

   - "Vendor will delete data per their policies" = weak clause (no enforceability)
   - Strong clause specifies timeline, method, and verification


## Sheet 6: Verification & Evidence Quality (from A.8.10.4)

**Purpose:** Assess audit readiness and evidence quality for proving deletion occurred.

**Key Metrics to Extract:**

| Metric | Source | Dashboard Cell | Target |
|--------|--------|----------------|--------|
| Audit Readiness Score | A.8.10.4 Sheet 7 | B8 | Fully Ready |
| Certificate Quality Average | A.8.10.4 Sheet 7 | B11 | ≥4.0 |
| Audit Trail Completeness % | A.8.10.4 Sheet 6 (average Column S) | B6 | 100% |
| Forensic Test Coverage % | A.8.10.4 Sheet 3 (average Column T) | B7 | ≥95% |
| Deletion Logging Maturity | A.8.10.4 Sheet 7 | B5 | ≥4.0 |
| Evidence Repository Security | A.8.10.4 Sheet 7 | B9 | ≥4.0 |

**Key Questions:**

**Q: "What does 'Audit Readiness' actually mean?"**

- A: Ability to demonstrate deletion compliance to external auditor within 2 hours:
  - **Fully Ready:** Complete evidence available in <1 hour
  - **Mostly Ready:** Complete evidence available in 1-4 hours
  - **Partially Ready:** Evidence incomplete or requires >4 hours to gather
  - **Not Ready:** Cannot reconstruct audit trail


**Q: "Why is 'Certificate Quality Average' important?"**

- A: Low-quality certificates (score <3.0) may not be accepted by auditors or regulators
  - Score 5: Excellent formal certificate with all fields
  - Score 3: Fair generic certificate
  - Score 1: Email confirmation only
  - **Target:** ≥4.0 (Good to Excellent average)


**Q: "What's the difference between 'Audit Trail Completeness' and 'Forensic Test Coverage'?"**

- A:
  - **Audit Trail Completeness:** Can reconstruct "who deleted what, when" from logs (evidence exists)
  - **Forensic Test Coverage:** Have tested deletion methods work correctly (methods are effective)
  - Both needed: Evidence exists (audit trail) + Methods work (forensic testing)


**Common Mistakes:**

1. ❌ **Assuming logs = audit readiness**

   - Logs must be complete, retained, accessible, and organized
   - "We have logs somewhere" ≠ Fully Ready for audit


2. ❌ **Accepting email confirmations as certificates**

   - Email: "Data deleted per your request" = score 2 (Poor)
   - Formal signed certificate with details = score 5 (Excellent)


## Sheet 7: Critical Gaps Dashboard

**Purpose:** Highlight top 5 gaps requiring immediate management attention.

**How to Identify Critical Gaps:**

**Step 1: Review all 4 source assessments**

- Open A.8.10.1-4 workbooks
- In each, scan Sheets 2-6, Column D (Gap Severity)
- List all rows marked "Critical" or "High"


**Step 2: Prioritize by regulatory/operational risk**

- **Regulatory Risk:** GDPR/FADP violations, ISO 27001 non-conformities
- **Operational Risk:** Data breach exposure, audit failures
- **Efficiency:** Cost savings, process improvements


**Step 3: Select top 5 for dashboard**

- Document in Sheet 7: Gap description, assessment source, responsible party, target date


**Example Critical Gaps:**

| Priority | Gap Description | Source | Risk Level | Target Date |
|----------|----------------|--------|------------|-------------|
| 1 | Shadow IT: 12 instances processing confidential data (Tier 9/10) | A.8.10.3 | Regulatory (GDPR Art. 28) | 30 days |
| 2 | No forensic testing program for deletion methods | A.8.10.4 | Operational (Cannot verify deletion) | 60 days |
| 3 | 15% of data categories lack retention schedules | A.8.10.1 | Regulatory (GDPR Art. 5.1.e) | 30 days |
| 4 | SSD deletion using HDD overwrite methods (8 systems) | A.8.10.2 | Operational (Ineffective deletion) | 90 days |
| 5 | Deletion logs retained only 90 days (vs. 7 years required) | A.8.10.4 | Audit (Evidence loss) | 45 days |

**Pro Tip:** Include target completion dates and responsible parties to demonstrate management accountability.

## Sheet 8: Trend Analysis

**Purpose:** Show quarterly progress (or decline) to identify systemic issues.

**First Quarter (Q1 Baseline):**

- Document all current metrics in Q1 column
- Leave Q2, Q3, Q4 blank
- No trend arrows (no comparison data yet)


**Subsequent Quarters (Q2-Q4):**

- Document current metrics in appropriate column
- Calculate trend vs. previous quarter:
  - ↑ (Green): Metric improved by ≥5%
  - → (Amber): Metric changed by <5% (stable)
  - ↓ (Red): Metric declined by ≥5%
- Document "Trend Explanation" for significant changes


**Example Trend Explanations:**

| Metric | Q1 | Q2 | Trend | Explanation |
|--------|----|----|-------|-------------|
| Retention Coverage % | 85% | 100% | ↑ | Completed retention schedule project for remaining 15 data categories |
| Forensic Test Pass Rate | 88% | 95% | ↑ | Replaced HDD overwrite method on SSDs with crypto-erase (7 systems) |
| Shadow IT Count | 12 | 5 | ↑ | Formalized 4 instances with DPAs, decommissioned 3 unauthorized systems |
| DSR Response Time | 35 days | 22 days | ↑ | Implemented automated DSR workflow reducing manual processing time |

**Red Flag Trends (Require Immediate Explanation):**

- ↓ Retention coverage declining (data categories added without schedules)
- ↓ NIST compliance declining (new deletion methods not validated)
- ↓ SLA compliance declining (vendors breaching deadlines more frequently)


## Sheet 9: Executive Summary (Narrative)

**Purpose:** Translate technical metrics into executive communication for board presentation.

**Structure (1-2 pages maximum):**

**Section 1: Overall Compliance Status (2-3 sentences)**

- Overall A.8.10 Maturity Score: [Score]/100 → [Green/Amber/Red]
- Headline summary: "Fully compliant" / "Substantially compliant" / "Partially compliant"
- Trend: "Improving" / "Stable" / "Declining" vs. last quarter


**Section 2: Key Achievements (3-5 bullets)**

- What improved this quarter
- Major remediation milestones completed
- Positive regulatory developments


**Section 3: Key Concerns (3-5 bullets)**

- Top 3 critical gaps (from Sheet 7)
- Any declining trends (from Sheet 8)
- Regulatory risks requiring board awareness


**Section 4: Next Quarter Priorities (3-5 bullets)**

- Planned remediation efforts
- Resource requirements (budget, staff)
- Expected completion dates


**Example Executive Summary:**
```
EXECUTIVE SUMMARY - Q2 2024 A.8.10 COMPLIANCE DASHBOARD

Overall Status: [Organization] achieved a maturity score of 78/100 (Amber) for ISO 27001:2022 
Control A.8.10 (Information Deletion), representing substantial compliance with a positive 
trend (+8 points vs. Q1). While foundational controls are in place, three critical gaps 
require board attention and resource allocation.

Key Achievements:

- Completed retention schedule implementation - now 100% coverage (up from 85% in Q1)
- Reduced data subject request (DSR) response time to 22 days average (vs. 35 days Q1), 

  exceeding GDPR 30-day requirement

- Formalized 4 Shadow IT instances with proper Data Processing Agreements (DPAs)
- Implemented crypto-erasure for SSD deletion (7 systems transitioned from ineffective 

  overwrite methods)

Key Concerns Requiring Board Attention:

- Shadow IT: 5 remaining unauthorized systems process confidential data without contractual 

  deletion controls (GDPR Article 28 violation risk - €20M fine exposure)

- Forensic Testing: No systematic program to verify deletion methods are effective (cannot 

  defend "we actually deleted it" claims to regulators/auditors)

- Evidence Retention: Deletion logs retained only 90 days vs. 7-year requirement per Swiss 

  Code of Obligations (audit evidence gap)

Next Quarter Priorities (Q3 2024):

- Establish forensic testing program (budget request: CHF 45,000 for third-party lab 

  engagement or in-house tools)

- Remediate remaining 5 Shadow IT instances (formalize 3, decommission 2)
- Extend deletion log retention to 7 years (storage expansion: CHF 12,000)
- Target maturity score: 85/100 (Green threshold: ≥80)


Board Action Requested:

- Approve CHF 57,000 budget for Q3 remediation initiatives
- Authorize CISO to engage third-party forensic lab for deletion method validation
- Mandate business unit leaders to eliminate Shadow IT processing of confidential data by Q3 end

```

**Writing Tips:**

- ✅ **Use business language, not technical jargon**
  - Good: "Cannot prove we deleted data to regulators"
  - Bad: "Forensic verification testing program not NIST SP 800-88 compliant"

- ✅ **Quantify risks in financial terms**
  - Good: "GDPR violation risk = €20M fine or 4% annual revenue"
  - Bad: "Non-compliant with GDPR Article 28"

- ✅ **Be specific about resource needs**
  - Good: "CHF 45,000 for forensic testing lab engagement"
  - Bad: "Additional budget needed"

- ✅ **Frame gaps as fixable with clear timelines**
  - Good: "Remediate by Q3 end with approved budget"
  - Bad: "Critical gap exists with no resolution plan"


---

# Maturity Scoring Model

## How the Overall A.8.10 Maturity Score is Calculated

**Scoring Formula (Weighted Average):**
```
Overall Score = (Retention Health × 25%) 

              + (Deletion Effectiveness × 25%) 
              + (Third-Party Performance × 25%) 
              + (Verification Quality × 25%)

```

**Component Scores (0-100 scale):**

Each component score is calculated from its source assessment:

**1. Retention Health (from A.8.10.1):**

- Retention Coverage % (40% weight)
- DSR Response Time Performance (30% weight)
- Legal Basis Gaps (30% weight)


**2. Deletion Effectiveness (from A.8.10.2):**

- NIST Compliance % (50% weight)
- Forensic Test Pass Rate (30% weight)
- SSD-Specific Issues (20% weight)


**3. Third-Party Performance (from A.8.10.3):**

- Vendor SLA Compliance % (40% weight)
- Shadow IT Exposure (30% weight)
- DPA Coverage % (30% weight)


**4. Verification Quality (from A.8.10.4):**

- Audit Readiness Score (40% weight)
- Certificate Quality Average (30% weight)
- Audit Trail Completeness (30% weight)


**Example Calculation:**
```
Component Scores:

- Retention Health: 85/100
- Deletion Effectiveness: 72/100
- Third-Party Performance: 68/100
- Verification Quality: 75/100


Overall Score = (85 × 0.25) + (72 × 0.25) + (68 × 0.25) + (75 × 0.25)
              = 21.25 + 18 + 17 + 18.75
              = 75/100 (Amber)
```

**Interpretation:**

- **≥80 (Green):** Mature compliance program, audit-ready, minimal regulatory risk
- **60-79 (Amber):** Functional but gaps exist, remediation in progress, moderate risk
- **<60 (Red):** Significant compliance gaps, high regulatory risk, immediate action required


## Why Weighted Scoring vs. Simple Average?

**Simple Average Problem:**

- Treats all metrics equally (DSR response time = SSD deletion method)
- Doesn't reflect regulatory priorities (GDPR compliance ≠ operational efficiency)
- One excellent area can mask critical gaps elsewhere


**Weighted Scoring Benefits:**

- ✅ Reflects regulatory importance (retention schedules weighted higher than log formatting)
- ✅ Balances technical and operational aspects
- ✅ Prevents "gaming" the score by excelling in low-impact areas


---

# Common Pitfalls & How to Avoid Them

## "Set It and Forget It" Syndrome

**Pitfall:** Create dashboard once in Q1, never update it again.

**Consequences:**

- Q2-Q4 metrics stale and inaccurate
- Board receives outdated compliance status
- Remediation efforts not tracked
- Trend analysis impossible


**Solution:**

- Schedule recurring calendar reminder (every 90 days)
- Link dashboard update to board meeting preparation
- Include dashboard update in quarterly ISMS management review
- Assign accountability (Compliance Officer owns quarterly updates)


## Copy-Paste Errors in Manual Entry

**Pitfall:** Copy wrong cell from source workbook into dashboard.

**Example Error:**

- Dashboard Cell B5 should have "Retention Coverage %" (95%)
- Accidentally paste "Overdue Reviews Count" (8) instead
- Dashboard now shows 8% retention coverage (appears catastrophic)


**Solution:**

- **Double-check source cell references** using Data Source Mapping Table (Sheet 1)
- **Validate totals:** If percentages should sum to 100%, verify the math
- **Cross-reference:** Compare dashboard summary to source workbook summary (should match exactly)
- **Peer review:** Have second person validate 10-20% of manual entries (sampling)


## Ignoring Trend Explanations

**Pitfall:** Document trends (↑↓→) without explaining WHY changes occurred.

**Problem:**

- Board sees "↓ NIST Compliance declined 10%" with no context
- Appears as lack of management control or care
- Missed opportunity to highlight remediation efforts


**Solution:**

- Always document "Trend Explanation" in Sheet 8 for significant changes (>5%)
- Explain both positive and negative trends:
  - Positive: "Implemented new forensic testing program"
  - Negative: "Discovered 3 new data categories without retention schedules during system inventory"
- Use trends to request resources: "Declining SLA compliance due to vendor underperformance → renegotiate contracts"


## Dashboard Data Conflicts with Source Assessments

**Pitfall:** Dashboard shows 95% retention coverage, but A.8.10.1 source shows 87%.

**Causes:**

- Source assessments updated after dashboard creation
- Dashboard populated from draft versions of source assessments
- Manual entry errors


**Solution:**

- **ALWAYS use approved versions** of source assessments (Sheet 9 approval completed)
- **Lock source assessments** after approval (prevent post-dashboard changes)
- **Version control:** Document which version of each source assessment fed the dashboard
  - Example: "Dashboard Q2 2024 based on: A.8.10.1 v2.0 approved 15.04.2024"
- If source assessments must be revised post-dashboard, regenerate dashboard


## Executive Summary Too Technical

**Pitfall:** Executive summary reads like an engineering report, not board communication.

**Bad Example:**
```
"The NIST SP 800-88 Rev. 1 compliance percentage for Clear/Purge/Destroy categorization 
is 72% due to insufficient forensic verification testing per Appendix A methodology."
```

**Good Example:**
```
"72% of deletion methods are validated per industry standards. Gap: We cannot prove to 
regulators that deletion actually occurred (no forensic testing program). Risk: €20M 
GDPR fine if challenged. Solution: CHF 45K budget for third-party testing lab."
```

**Solution:**

- Write for audience with NO technical background
- Translate jargon: "NIST SP 800-88" → "industry deletion standards"
- Quantify risks: Always include financial/regulatory exposure
- Be action-oriented: Every gap = proposed solution + cost + timeline


---

# Quality Checklist

Before submitting dashboard for approval (Sheet 9), verify:

**Data Accuracy:**

- [ ] All metrics extracted from approved source assessments (not draft versions)
- [ ] Manual entry validated by cross-checking 20% of values (sampling)
- [ ] Formulas calculate correctly (no #REF!, #DIV/0!, #VALUE! errors)
- [ ] Percentages sum to 100% where applicable (e.g., NIST category distribution)
- [ ] Trend arrows match actual metric changes (↑ = improving, not declining)


**Completeness:**

- [ ] All 40-60 metrics populated (no blank cells in yellow-highlighted fields)
- [ ] Critical Gaps Dashboard (Sheet 7) documents top 5 gaps with timelines
- [ ] Trend Analysis (Sheet 8) includes explanations for significant changes
- [ ] Executive Summary (Sheet 9) includes narrative for board presentation
- [ ] Evidence documentation (link to source assessment approval records)


**Executive Communication:**

- [ ] Executive Summary uses business language (not technical jargon)
- [ ] Risks quantified in financial terms (€20M GDPR fines, audit costs)
- [ ] Resource requests specific (budget amounts, timelines, responsible parties)
- [ ] Both achievements and concerns balanced (not only negative gaps)
- [ ] Next quarter priorities actionable and measurable


**Audit Readiness:**

- [ ] Dashboard demonstrates systematic compliance monitoring (quarterly cadence)
- [ ] Trend analysis shows management oversight and continuous improvement
- [ ] Critical gaps have documented remediation plans
- [ ] Source assessments traceable (version numbers, approval dates documented)
- [ ] Dashboard can be presented to external auditor with <1 hour preparation


---

# Review & Approval Process

## Three-Level Approval Workflow

| Level | Role | Responsibility | Timeline |
|-------|------|----------------|----------|
| Level 1 | Compliance Officer / Preparer | Extract metrics from source assessments, populate dashboard, write executive summary | Week 1 |
| Level 2 | Information Security Officer / CISO | Validate metric accuracy, review trends, approve gap priorities | Week 2 |
| Level 3 | Executive Sponsor / Audit Committee | Final approval, authorize board presentation, commit remediation resources | Week 3 |

## Approval Criteria

**Level 1 → Level 2:**

- All sheets populated with no blank mandatory fields
- Source assessments approved and version-controlled
- Trend explanations documented for significant changes
- Executive summary written for board audience


**Level 2 → Level 3:**

- Metric accuracy validated by cross-checking source assessments
- Critical gaps aligned with organizational risk appetite
- Remediation budgets and timelines realistic
- Dashboard ready for board presentation (formatting, clarity)


**Level 3 (Final):**

- Executive sponsor approves board presentation
- Remediation budget requests authorized (or revised)
- Quarterly update schedule confirmed for next 3 quarters
- Dashboard archived in compliance evidence repository


## Rejection Scenarios

Dashboard may be rejected if:

- ❌ Metrics conflict with source assessments (data accuracy issues)
- ❌ Critical gaps have no remediation plans or timelines
- ❌ Trend analysis shows declining compliance without explanation
- ❌ Executive summary too technical for board audience
- ❌ Source assessments not approved (using draft versions)
- ❌ Manual entry errors discovered during validation sampling


---

**End of PART I: User Completion Guide**

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** ISMS Implementation Teams, Python Developers, Excel Power Users

---

# Excel Workbook Structure

## Overview

**Workbook Name:** `ISMS_A_8_10_5_Compliance_Dashboard_YYYYMMDD.xlsx`

**Sheet Count:** 9 sheets total

**Design Philosophy:** REPORTING DASHBOARD (not data collection tool)

- Manual entry of summary metrics from source workbooks (no external file links)
- Heavy use of formulas for calculations and aggregations
- Visual indicators (RAG status, trend arrows) for executive consumption
- Quarterly snapshot capability (Q1-Q4 columns in Sheet 8)


## Sheet Organization

| Sheet # | Sheet Name | Purpose | Data Entry Type | Protected? |
|---------|------------|---------|-----------------|------------|
| 1 | Instructions & Data Mapping | User guidance and source cell references | N/A (read-only) | Yes |
| 2 | Overall A.8.10 Compliance | Highest-level summary (5 metrics) | Manual entry (5 cells) | Formulas protected |
| 3 | Retention Schedule Health | A.8.10.1 deep dive (8-10 metrics) | Manual entry (10 cells) | Formulas protected |
| 4 | Deletion Method Effectiveness | A.8.10.2 deep dive (10 metrics) | Manual entry (10 cells) | Formulas protected |
| 5 | Third-Party Deletion Performance | A.8.10.3 deep dive (8-10 metrics) | Manual entry (10 cells) | Formulas protected |
| 6 | Verification & Evidence Quality | A.8.10.4 deep dive (8-10 metrics) | Manual entry (10 cells) | Formulas protected |
| 7 | Critical Gaps Dashboard | Top 5 gaps from all assessments | Manual entry (15 cells) | No |
| 8 | Trend Analysis | Quarterly comparison Q1-Q4 | Manual entry (40 cells/quarter) | Formulas protected |
| 9 | Executive Summary & Approval | Narrative summary and sign-off | Manual entry (text + 3 approvals) | No |

**Total Manual Entry Cells:** ~100-120 cells (vs. 260+ cells in assessment workbooks)

**Total Formula Cells:** ~200-300 cells (calculations, aggregations, RAG status)

---

# Sheet 1: Instructions & Data Mapping

## Purpose
Provide comprehensive guidance on dashboard completion and exact source cell references for manual data entry.

## Content Sections

**Section 1: Dashboard Overview (Rows 1-15)**

- Document ID, Version, Date
- Dashboard purpose and scope
- Target audience (executives, board, auditors)
- Update frequency (quarterly)
- Manual entry workflow explanation


**Section 2: Data Source Mapping Table (Rows 17-80)**

This is the CRITICAL table that prevents manual entry errors. For each dashboard cell, document:

- Dashboard Sheet Name
- Dashboard Cell Reference
- Source Workbook Filename
- Source Sheet Name
- Source Cell Reference
- Metric Description
- Expected Data Type (%, count, score, text)


**Example Data Source Mapping Table:**

| Dashboard Sheet | Dashboard Cell | Source Workbook | Source Sheet | Source Cell | Metric Description | Data Type |
|-----------------|----------------|-----------------|--------------|-------------|-------------------|-----------|
| Sheet 2 (Overall) | B5 | A.8.10.1_Retention_[Date].xlsx | Sheet 7 (Dashboard) | B7 | Retention Schedule Coverage % | Percentage |
| Sheet 2 (Overall) | B6 | A.8.10.2_Deletion_Methods_[Date].xlsx | Sheet 7 (Dashboard) | B7 | NIST Compliance % | Percentage |
| Sheet 2 (Overall) | B7 | A.8.10.3_Third_Party_[Date].xlsx | Sheet 7 (Dashboard) | B7 | Vendor SLA Compliance % | Percentage |
| Sheet 2 (Overall) | B8 | A.8.10.4_Verification_[Date].xlsx | Sheet 7 (Dashboard) | B18 | Audit Readiness Score | Text |
| Sheet 3 (Retention) | B5 | A.8.10.1_Retention_[Date].xlsx | Sheet 7 (Dashboard) | B5 | Total Data Categories | Count |
| Sheet 3 (Retention) | B6 | A.8.10.1_Retention_[Date].xlsx | Sheet 7 (Dashboard) | B6 | Categories with Schedules | Count |
| Sheet 3 (Retention) | B8 | A.8.10.1_Retention_[Date].xlsx | Sheet 7 (Dashboard) | B8 | Overdue Reviews Count | Count |
| Sheet 3 (Retention) | B12 | A.8.10.1_Retention_[Date].xlsx | Sheet 7 (Dashboard) | B12 | Avg DSR Response Time (days) | Number |
| Sheet 4 (Methods) | B5 | A.8.10.2_Deletion_Methods_[Date].xlsx | Sheet 7 (Dashboard) | B5 | Total Deletion Methods | Count |
| Sheet 4 (Methods) | B6 | A.8.10.2_Deletion_Methods_[Date].xlsx | Sheet 7 (Dashboard) | B6 | NIST-Compliant Methods | Count |
| Sheet 4 (Methods) | B8 | A.8.10.2_Deletion_Methods_[Date].xlsx | Sheet 7 (Dashboard) | B8 | Forensic Test Pass Rate % | Percentage |
| Sheet 5 (Third-Party) | B5 | A.8.10.3_Third_Party_[Date].xlsx | Sheet 7 (Dashboard) | B5 | Total Vendors with Data | Count |
| Sheet 5 (Third-Party) | B8 | A.8.10.3_Third_Party_[Date].xlsx | Sheet 7 (Dashboard) | B8 | Shadow IT Tier 9/10 Count | Count |
| Sheet 6 (Verification) | B5 | A.8.10.4_Verification_[Date].xlsx | Sheet 7 (Dashboard) | B5 | Deletion Logging Maturity | Score 1-5 |
| Sheet 6 (Verification) | B11 | A.8.10.4_Verification_[Date].xlsx | Sheet 7 (Dashboard) | B11 | Certificate Quality Avg | Score 1-5 |

**Section 3: Maturity Scoring Model (Rows 82-110)**

Explanation of how Overall A.8.10 Maturity Score is calculated:
```
Overall Score = (Retention Health × 25%) 

              + (Deletion Effectiveness × 25%) 
              + (Third-Party Performance × 25%) 
              + (Verification Quality × 25%)


Where:
  Retention Health = Based on A.8.10.1 metrics (coverage, DSR, legal basis)
  Deletion Effectiveness = Based on A.8.10.2 metrics (NIST, testing, SSD)
  Third-Party Performance = Based on A.8.10.3 metrics (SLA, Shadow IT, DPA)
  Verification Quality = Based on A.8.10.4 metrics (audit readiness, certificates, logs)
```

**Section 4: RAG Status Color Coding (Rows 112-125)**

| Color | Threshold | Meaning | Action |
|-------|-----------|---------|--------|
| **Green** | ≥90% / Score ≥80 / "Fully Ready" | Low risk, compliant | Maintain current controls |
| **Amber** | 70-89% / Score 60-79 / "Mostly Ready" | Moderate risk, gaps exist | Monitor and plan improvements |
| **Red** | <70% / Score <60 / "Partially/Not Ready" | High risk, non-compliant | Immediate remediation required |

**Section 5: Quarterly Update Workflow (Rows 127-145)**

Step-by-step guide to quarterly dashboard updates:
1. Ensure all 4 source assessments (A.8.10.1-4) completed and approved
2. Open this dashboard workbook
3. Open Data Source Mapping Table (Section 2)
4. For each row in mapping table:

   - Open source workbook specified
   - Navigate to source sheet specified
   - Copy value from source cell specified
   - Paste into dashboard cell specified

5. Validate formulas calculate correctly (no errors)
6. Complete Sheet 7 (Critical Gaps) - manual entry
7. Complete Sheet 8 (Trend Analysis) - manual entry + formulas
8. Complete Sheet 9 (Executive Summary) - narrative text
9. Three-level approval workflow
10. Archive completed dashboard

## Formatting

- Mapping table: Alternating row colors, borders, wrapped text
- Manual entry cells: Yellow fill (same as assessment workbooks)
- Formula cells: Light blue fill, locked
- Source cell references: Monospace font for clarity


---

# Sheet 2: Overall A.8.10 Compliance

## Purpose
Provide the 30-second executive summary - highest-level compliance status across all 4 assessment areas.

## Layout Structure

**Section 1: Summary Metrics (Rows 3-12, Columns A-F)**

| Row | Column A (Metric) | Column B (Value) | Column C (Target) | Column D (Status) | Column E (Trend) | Column F (Notes) |
|-----|-------------------|------------------|-------------------|-------------------|------------------|------------------|
| 5 | Overall A.8.10 Maturity Score | =Formula | ≥80/100 | =RAG Formula | =Trend Formula | Auto-text |
| 6 | Retention Schedule Coverage | [Manual] | 100% | =RAG Formula | =Trend Formula | From A.8.10.1 |
| 7 | Deletion Method NIST Compliance | [Manual] | 100% | =RAG Formula | =Trend Formula | From A.8.10.2 |
| 8 | Vendor SLA Compliance | [Manual] | ≥95% | =RAG Formula | =Trend Formula | From A.8.10.3 |
| 9 | Audit Readiness Score | [Manual] | Fully Ready | =RAG Formula | =Trend Formula | From A.8.10.4 |

**Column B Formula Examples:**

**Row 5 (Overall Maturity Score):**
```excel
=ROUND(
  ('Retention Health'!B20 * 0.25) +
  ('Deletion Effectiveness'!B20 * 0.25) +
  ('Third-Party Performance'!B20 * 0.25) +
  ('Verification Quality'!B20 * 0.25),
  0
)
```
*Note: B20 in each sheet contains that area's component score (0-100)*

**Column D (RAG Status) Formulas:**

**For Percentages (Rows 6-8):**
```excel
=IF(B6>=90,"Green",IF(B6>=70,"Amber","Red"))
```

**For Scores (Row 5):**
```excel
=IF(B5>=80,"Green",IF(B5>=60,"Amber","Red"))
```

**For Text Values (Row 9 - Audit Readiness):**
```excel
=IF(B9="Fully Ready","Green",IF(B9="Mostly Ready","Amber","Red"))
```

**Column E (Trend) Formulas:**

*Compares current value (Column B) vs. previous quarter value (Sheet 8 Trend Analysis)*
```excel
=IF(ISBLANK('Trend Analysis'!B5),"→",
   IF(B5>='Trend Analysis'!B5*1.05,"↑",
      IF(B5<='Trend Analysis'!B5*0.95,"↓","→")))
```

**Section 2: Critical Gaps Summary (Rows 14-22, Columns A-E)**

| Row | Column A (Area) | Column B (Critical Gaps Count) | Column C (Highest Priority Gap) | Column D (Target Date) |
|-----|-----------------|-------------------------------|--------------------------------|----------------------|
| 16 | A.8.10.1 Retention | =Formula | [Manual from Sheet 7] | [Manual] |
| 17 | A.8.10.2 Methods | =Formula | [Manual from Sheet 7] | [Manual] |
| 18 | A.8.10.3 Third-Party | =Formula | [Manual from Sheet 7] | [Manual] |
| 19 | A.8.10.4 Verification | =Formula | [Manual from Sheet 7] | [Manual] |

**Column B Formula (Critical Gaps Count):**
```excel
='Critical Gaps'!B5
```
*Where Critical Gaps Sheet B5 = count of A.8.10.1 critical gaps*

**Section 3: Compliance Readiness by Standard (Rows 24-31, Columns A-D)**

| Row | Column A (Standard) | Column B (Compliance Status) | Column C (Evidence Gaps) | Column D (Next Action) |
|-----|-------------------|----------------------------|------------------------|----------------------|
| 26 | ISO 27001:2022 A.8.10 | =Formula | =Formula | [Manual] |
| 27 | GDPR Article 17 | =Formula | =Formula | [Manual] |
| 28 | FADP Article 6 | =Formula | =Formula | [Manual] |
| 29 | NIST SP 800-88 | =Formula | =Formula | [Manual] |

**Column B Formula (Compliance Status):**
```excel
=IF(B5>=90,"Fully Compliant",
   IF(B5>=70,"Substantially Compliant",
      IF(B5>=50,"Partially Compliant","Non-Compliant")))
```

**Column C Formula (Evidence Gaps Count):**
```excel
=SUMIF('Critical Gaps'!C5:C9,"Evidence*")
```
*Counts gaps in Critical Gaps sheet where gap description contains "Evidence"*

## Conditional Formatting

**Column D (Status) - Text Color Based on Value:**

- Green text for cells containing "Green"
- Orange text for cells containing "Amber"
- Red bold text for cells containing "Red"


**Column E (Trend) - Icon Sets:**

- Green up arrow (↑) for "↑"
- Orange right arrow (→) for "→"
- Red down arrow (↓) for "↓"


**Row 5 (Overall Maturity Score) - Cell Fill:**

- Green fill if B5 ≥ 80
- Orange fill if B5 60-79
- Red fill if B5 < 60


---

# Sheet 3: Retention Schedule Health

## Purpose
Deep dive into retention schedule coverage and data subject rights performance from A.8.10.1 assessment.

## Layout Structure

**Section 1: Retention Schedule Coverage Metrics (Rows 3-13, Columns A-E)**

| Row | Column A (Metric) | Column B (Current Value) | Column C (Target) | Column D (Status) | Column E (Notes) |
|-----|-------------------|------------------------|-------------------|-------------------|------------------|
| 5 | Total Data Categories Identified | [Manual from A.8.10.1] | Baseline | Info | [Auto] |
| 6 | Categories with Retention Schedules | [Manual from A.8.10.1] | 100% | =RAG | [Auto] |
| 7 | Retention Schedule Coverage % | =B6/B5*100 | 100% | =RAG | Calculated |
| 8 | Overdue Schedule Reviews | [Manual from A.8.10.1] | 0 | =RAG | [Auto] |
| 9 | Schedules Aligned with FADP | [Manual from A.8.10.1] | All | =RAG | [Auto] |
| 10 | Schedules Aligned with GDPR | [Manual from A.8.10.1] | All | =RAG | [Auto] |
| 11 | Avg Schedule Review Age (months) | [Manual from A.8.10.1] | <12 | =RAG | [Auto] |
| 12 | Categories Without Legal Basis | [Manual from A.8.10.1] | 0 | =RAG | [Auto] |

**Row 7 Formula (Retention Coverage %):**
```excel
=IF(B5=0,0,ROUND(B6/B5*100,1))
```

**Column D (Status) Formulas:**

**Row 7 (Coverage %):**
```excel
=IF(B7=100,"Green",IF(B7>=95,"Amber","Red"))
```

**Row 8 (Overdue Reviews):**
```excel
=IF(B8=0,"Green",IF(B8<=5,"Amber","Red"))
```

**Row 11 (Review Age):**
```excel
=IF(B11<12,"Green",IF(B11<18,"Amber","Red"))
```

**Row 12 (No Legal Basis):**
```excel
=IF(B12=0,"Green",IF(B12<=3,"Amber","Red"))
```

**Section 2: GDPR DSR Response Performance (Rows 15-20, Columns A-E)**

| Row | Column A (Metric) | Column B (Performance) | Column C (GDPR Requirement) | Column D (Status) |
|-----|-------------------|----------------------|---------------------------|-------------------|
| 17 | Average DSR Response Time (days) | [Manual from A.8.10.1] | <30 days | =RAG |
| 18 | DSR Requests Completed On Time % | [Manual from A.8.10.1] | 100% | =RAG |
| 19 | DSR Backlog Count | [Manual from A.8.10.1] | 0 | =RAG |

**Column D Formulas:**

**Row 17 (DSR Response Time):**
```excel
=IF(B17<20,"Green",IF(B17<30,"Amber","Red"))
```

**Row 18 (On Time %):**
```excel
=IF(B18=100,"Green",IF(B18>=90,"Amber","Red"))
```

**Row 19 (Backlog):**
```excel
=IF(B19=0,"Green",IF(B19<=3,"Amber","Red"))
```

**Section 3: Component Score Calculation (Row 20, Column B)**

*This feeds into Sheet 2 Overall Maturity Score*

**Formula:**
```excel
=ROUND(
  (B7*0.4) +                    /* Retention Coverage 40% weight */
  ((30-MIN(B17,30))/30*100*0.3) + /* DSR Response 30% weight (inverse - lower is better) */
  ((B5-B12)/B5*100*0.3),           /* Legal Basis 30% weight */
  0
)
```

**Section 4: Reference - Retention Compliance Benchmarks (Rows 22-28, Table)**

| Benchmark | Value | Source |
|-----------|-------|--------|
| Industry Average Retention Coverage | 85% | ISO 27001 Survey 2024 |
| Regulatory Minimum (GDPR) | 100% | Article 5.1(e) Storage Limitation |
| Best Practice Target | 100% | NIST SP 800-88 R1 |
| GDPR DSR Response Deadline | 30 days | Article 17 |
| Swiss OR Business Records Retention | 7 years | Article 958f |

---

# Sheet 4: Deletion Method Effectiveness

## Purpose
Evaluate deletion method compliance and effectiveness from A.8.10.2 assessment.

## Layout Structure

**Section 1: NIST SP 800-88 Compliance Metrics (Rows 3-17, Columns A-E)**

| Row | Column A (Metric) | Column B (Current) | Column C (Target) | Column D (Status) |
|-----|-------------------|-------------------|-------------------|-------------------|
| 5 | Total Deletion Methods in Use | [Manual from A.8.10.2] | Documented | Info |
| 6 | NIST-Compliant Methods Count | [Manual from A.8.10.2] | 100% of total | =RAG |
| 7 | NIST Compliance % | =B6/B5*100 | 100% | =RAG |
| 8 | Forensic Test Pass Rate % | [Manual from A.8.10.2] | ≥95% | =RAG |
| 9 | Methods Tested vs. Untested | [Manual] / [Manual] | All tested | =RAG |
| 10 | Clear Methods % | [Manual from A.8.10.2] | Per classification | Info |
| 11 | Purge Methods % | [Manual from A.8.10.2] | Per classification | Info |
| 12 | Destroy Methods % | [Manual from A.8.10.2] | Per classification | Info |
| 13 | NIST Category Sum Check | =B10+B11+B12 | 100% | Validation |
| 14 | SSD-Specific Issues Count | [Manual from A.8.10.2] | 0 | =RAG |
| 15 | Crypto-Erasure Implemented | [Manual from A.8.10.2] | Yes/No | Info |

**Row 7 Formula:**
```excel
=IF(B5=0,0,ROUND(B6/B5*100,1))
```

**Row 13 Formula (Validation):**
```excel
=IF(ABS(B10+B11+B12-100)<0.1,"✓ Valid","⚠ Check percentages")
```

**Column D Formulas:**

**Row 7 (NIST Compliance):**
```excel
=IF(B7=100,"Green",IF(B7>=90,"Amber","Red"))
```

**Row 8 (Test Pass Rate):**
```excel
=IF(B8>=95,"Green",IF(B8>=80,"Amber","Red"))
```

**Row 14 (SSD Issues):**
```excel
=IF(B14=0,"Green",IF(B14<=3,"Amber","Red"))
```

**Section 2: Deletion Method Testing Coverage (Rows 19-25)**

| Row | Column A (Metric) | Column B (Count) | Column C (Target) | Column D (Status) |
|-----|-------------------|------------------|-------------------|-------------------|
| 21 | Methods with Annual Testing | [Manual] | All methods | =RAG |
| 22 | Methods Tested in Last 12 Months | [Manual] | 100% | =RAG |
| 23 | Methods Never Tested | =B5-B22 | 0 | =RAG |
| 24 | Test Failures Requiring Remediation | [Manual] | 0 | =RAG |

**Section 3: Component Score Calculation (Row 20, Column B)**
```excel
=ROUND(
  (B7*0.5) +          /* NIST Compliance 50% */
  (B8*0.3) +          /* Test Pass Rate 30% */
  ((B5-B14)/B5*100*0.2), /* SSD Issues 20% (inverse) */
  0
)
```

**Section 4: Reference - NIST Media Categories (Rows 27-35, Table)**

| Media Type | Clear | Purge | Destroy |
|------------|-------|-------|---------|
| HDD (magnetic) | 1-pass overwrite | 3-pass overwrite | Degauss or shred |
| SSD (flash) | TRIM/Secure Erase | Crypto Erase | Physical destruction |
| Cloud/VM | API delete | Crypto Erase | N/A (provider-managed) |
| Paper | Shred (strip) | Cross-cut shred | Pulverize/incinerate |
| Optical (CD/DVD) | Not possible | Not possible | Physical destruction |

---

# Sheet 5: Third-Party Deletion Performance

## Purpose
Monitor vendor compliance with deletion SLAs and identify Shadow IT exposure from A.8.10.3 assessment.

## Layout Structure

**Section 1: Vendor Deletion Management Metrics (Rows 3-15, Columns A-E)**

| Row | Column A (Metric) | Column B (Current) | Column C (Target) | Column D (Status) |
|-----|-------------------|-------------------|-------------------|-------------------|
| 5 | Total Vendors with Data | [Manual from A.8.10.3] | Documented | Info |
| 6 | Vendors with Deletion SLAs | [Manual from A.8.10.3] | 100% | =RAG |
| 7 | Vendor SLA Coverage % | =B6/B5*100 | 100% | =RAG |
| 8 | Vendor SLA Compliance % | [Manual from A.8.10.3] | ≥95% | =RAG |
| 9 | Vendors Breaching SLAs | [Manual from A.8.10.3] | 0 | =RAG |
| 10 | DPA Coverage % | [Manual from A.8.10.3] | 100% | =RAG |
| 11 | Strong Deletion Clauses % | [Manual from A.8.10.3] | ≥80% | =RAG |
| 12 | Certificate Quality Score (Avg) | [Manual from A.8.10.3] | ≥4.0 | =RAG |

**Section 2: Shadow IT Exposure (Rows 17-23)**

| Row | Column A (Metric) | Column B (Count) | Column C (Target) | Column D (Status) |
|-----|-------------------|------------------|-------------------|-------------------|
| 19 | Total Shadow IT Instances | [Manual from A.8.10.3] | Documented | Info |
| 20 | Shadow IT Tier 9/10 (High Risk) | [Manual from A.8.10.3] | 0 | =RAG |
| 21 | Shadow IT with Sensitive Data | [Manual from A.8.10.3] | 0 | =RAG |
| 22 | Shadow IT Remediation in Progress | [Manual from A.8.10.3] | All high-risk | Info |

**Column D Formulas:**

**Row 7 (SLA Coverage):**
```excel
=IF(B7=100,"Green",IF(B7>=90,"Amber","Red"))
```

**Row 8 (SLA Compliance):**
```excel
=IF(B8>=95,"Green",IF(B8>=85,"Amber","Red"))
```

**Row 10 (DPA Coverage):**
```excel
=IF(B10=100,"Green",IF(B10>=90,"Amber","Red"))
```

**Row 11 (Strong Clauses):**
```excel
=IF(B11>=80,"Green",IF(B11>=60,"Amber","Red"))
```

**Row 12 (Certificate Quality):**
```excel
=IF(B12>=4,"Green",IF(B12>=3,"Amber","Red"))
```

**Row 20 (Shadow IT Tier 9/10):**
```excel
=IF(B20=0,"Green",IF(B20<=3,"Amber","Red"))
```

**Section 3: Component Score Calculation (Row 20, Column B)**
```excel
=ROUND(
  (B8*0.4) +              /* SLA Compliance 40% */
  ((B5-B20)/B5*100*0.3) + /* Shadow IT 30% (inverse) */
  (B10*0.3),              /* DPA Coverage 30% */
  0
)
```

**Section 4: Reference - Cloud Provider Deletion SLAs (Rows 25-32, Table)**

| Provider | Standard Deletion SLA | Verification Method | Certificate Provided |
|----------|---------------------|-------------------|-------------------|
| AWS | 30 days after termination | API logs, support ticket | On request |
| Azure | 90 days after termination | Compliance Manager | On request |
| Google Cloud | 30 days after deletion request | Admin Console logs | On request |
| Salesforce | Immediate + 90-day recycle bin | Data Export API | On request |
| Microsoft 365 | 30 days after deletion | Admin Center logs | On request |

---

# Sheet 6: Verification & Evidence Quality

## Purpose
Assess audit readiness and evidence quality for proving deletion occurred (from A.8.10.4 assessment).

## Layout Structure

**Section 1: Verification Infrastructure Metrics (Rows 3-15, Columns A-E)**

| Row | Column A (Metric) | Column B (Current) | Column C (Target) | Column D (Status) |
|-----|-------------------|-------------------|-------------------|-------------------|
| 5 | Deletion Logging Maturity (1-5) | [Manual from A.8.10.4] | ≥4.0 | =RAG |
| 6 | Log Completeness Score (%) | [Manual from A.8.10.4] | ≥80% | =RAG |
| 7 | Log Retention Period (years) | [Manual from A.8.10.4] | ≥7 years | =RAG |
| 8 | Centralized Logging Implemented | [Manual from A.8.10.4] | Yes/No | =RAG |
| 9 | Tamper Protection Implemented | [Manual from A.8.10.4] | Advanced/Immutable | =RAG |

**Section 2: Forensic Testing & Verification (Rows 17-23)**

| Row | Column A (Metric) | Column B (Current) | Column C (Target) | Column D (Status) |
|-----|-------------------|-------------------|-------------------|-------------------|
| 19 | Forensic Testing Program Exists | [Manual from A.8.10.4] | Yes/No | =RAG |
| 20 | Testing Frequency | [Manual from A.8.10.4] | Annual minimum | =RAG |
| 21 | Test Pass Rate (%) | [Manual from A.8.10.4] | ≥95% | =RAG |
| 22 | Methods Tested vs. Total | [Manual] / [Manual] | 100% | =RAG |

**Section 3: Evidence Repository & Audit Readiness (Rows 25-32)**

| Row | Column A (Metric) | Column B (Current) | Column C (Target) | Column D (Status) |
|-----|-------------------|-------------------|-------------------|-------------------|
| 27 | Evidence Repository Security (1-5) | [Manual from A.8.10.4] | ≥4.0 | =RAG |
| 28 | Evidence Retention Compliance | [Manual from A.8.10.4] | 100% | =RAG |
| 29 | Certificate Quality Average (1-5) | [Manual from A.8.10.4] | ≥4.0 | =RAG |
| 30 | Audit Trail Completeness (%) | [Manual from A.8.10.4] | 100% | =RAG |
| 31 | Audit Trail Reconstruction Time (hrs) | [Manual from A.8.10.4] | <2 hours | =RAG |
| 32 | Audit Readiness Status | [Manual from A.8.10.4] | Fully Ready | =RAG |

**Column D Formulas:**

**Row 5, 27, 29 (1-5 Scores):**
```excel
=IF(B5>=4,"Green",IF(B5>=3,"Amber","Red"))
```

**Row 6, 30 (Percentages):**
```excel
=IF(B6>=90,"Green",IF(B6>=70,"Amber","Red"))
```

**Row 7 (Retention Years):**
```excel
=IF(B7>=7,"Green",IF(B7>=3,"Amber","Red"))
```

**Row 8 (Yes/No - Centralized):**
```excel
=IF(B8="Yes","Green",IF(B8="Partial","Amber","Red"))
```

**Row 9 (Tamper Protection):**
```excel
=IF(OR(B9="Advanced",B9="Immutable"),"Green",IF(B9="Basic","Amber","Red"))
```

**Row 19 (Testing Program Exists):**
```excel
=IF(B19="Yes","Green","Red")
```

**Row 31 (Reconstruction Time):**
```excel
=IF(B31<1,"Green",IF(B31<4,"Amber","Red"))
```

**Row 32 (Audit Readiness):**
```excel
=IF(B32="Fully Ready","Green",IF(B32="Mostly Ready","Amber","Red"))
```

**Section 4: Component Score Calculation (Row 20, Column B)**
```excel
=ROUND(
  (IF(B32="Fully Ready",100,IF(B32="Mostly Ready",75,IF(B32="Partially Ready",50,25)))*0.4) + /* Audit Readiness 40% */
  (B29*20*0.3) +  /* Certificate Quality 30% (convert 1-5 to 0-100) */
  (B30*0.3),      /* Audit Trail Completeness 30% */
  0
)
```

---

# Sheet 7: Critical Gaps Dashboard

## Purpose
Highlight top 5 gaps requiring immediate management attention from all four assessments.

## Layout Structure

**Critical Gaps Summary Table (Rows 3-12, Columns A-F)**

| Row | Column A (Priority) | Column B (Gap Description) | Column C (Source Assessment) | Column D (Risk Level) | Column E (Responsible Party) | Column F (Target Date) |
|-----|-------------------|--------------------------|---------------------------|--------------------|----------------------------|---------------------|
| 5 | 1 (Highest) | [Manual entry] | Dropdown: A.8.10.1/2/3/4 | Dropdown: Critical/High | [Manual] | [Date] |
| 6 | 2 | [Manual entry] | Dropdown | Dropdown | [Manual] | [Date] |
| 7 | 3 | [Manual entry] | Dropdown | Dropdown | [Manual] | [Date] |
| 8 | 4 | [Manual entry] | Dropdown | Dropdown | [Manual] | [Date] |
| 9 | 5 (Lowest) | [Manual entry] | Dropdown | Dropdown | [Manual] | [Date] |

**Column C Dropdown Values:**

- A.8.10.1 - Retention & Deletion Triggers
- A.8.10.2 - Deletion Methods
- A.8.10.3 - Third-Party & Cloud Deletion
- A.8.10.4 - Verification & Evidence


**Column D Dropdown Values:**

- Critical (Regulatory violation risk)
- High (Operational risk, audit failure)
- Medium (Efficiency gap)


**Section 2: Gap Statistics by Assessment Area (Rows 14-22, Formulas)**

| Row | Column A (Assessment) | Column B (Critical Gaps) | Column C (High Gaps) | Column D (Total) |
|-----|---------------------|------------------------|-------------------|----------------|
| 16 | A.8.10.1 Retention | =COUNTIF(C5:C9,"A.8.10.1*") | [Manual if needed] | =B16+C16 |
| 17 | A.8.10.2 Methods | =COUNTIF(C5:C9,"A.8.10.2*") | [Manual] | =B17+C17 |
| 18 | A.8.10.3 Third-Party | =COUNTIF(C5:C9,"A.8.10.3*") | [Manual] | =B18+C18 |
| 19 | A.8.10.4 Verification | =COUNTIF(C5:C9,"A.8.10.4*") | [Manual] | =B19+C19 |
| 20 | **TOTAL** | =SUM(B16:B19) | =SUM(C16:C19) | =SUM(D16:D19) |

## Conditional Formatting

**Column D (Risk Level):**

- Red bold text for "Critical"
- Orange text for "High"


**Column F (Target Date):**

- Red fill if date < TODAY() (overdue)
- Orange fill if date < TODAY()+30 (due within 30 days)
- Green fill if date >= TODAY()+30


---

# Sheet 8: Trend Analysis

## Purpose
Show quarterly progress or decline to identify systemic issues requiring management attention.

## Layout Structure

**Quarterly Metrics Tracking (Rows 3-50, Columns A-F)**

**Column Structure:**

- Column A: Metric Name
- Column B: Q1 Value (Baseline)
- Column C: Q2 Value
- Column D: Q3 Value
- Column E: Q4 Value
- Column F: Trend Explanation


**Key Metrics Tracked (40 total):**

**From Sheet 2 (Overall):**
1. Overall A.8.10 Maturity Score
2. Retention Coverage %
3. NIST Compliance %
4. Vendor SLA Compliance %
5. Audit Readiness Score

**From Sheet 3 (Retention):**
6. Total Data Categories
7. Categories with Schedules
8. Overdue Reviews Count
9. Avg DSR Response Time (days)
10. DSR On-Time %

**From Sheet 4 (Methods):**
11. Total Deletion Methods
12. NIST-Compliant Methods
13. Forensic Test Pass Rate %
14. SSD Issues Count
15. Clear/Purge/Destroy Distribution

**From Sheet 5 (Third-Party):**
16. Total Vendors
17. Vendors with SLAs
18. SLA Compliance %
19. Shadow IT Count (Tier 9/10)
20. DPA Coverage %

**From Sheet 6 (Verification):**
21. Logging Maturity Score
22. Log Completeness %
23. Forensic Testing Exists
24. Certificate Quality Avg
25. Audit Readiness Status

## Trend Calculation Formulas

**For each metric row, add a calculated column G (Trend Arrow):**

**Formula (assuming metric in row 5):**
```excel
=IF(ISBLANK(B5),"N/A",
   IF(ISBLANK(C5),"→",
      IF(C5>=B5*1.05,"↑ +"&TEXT((C5-B5)/B5,"0%"),
         IF(C5<=B5*0.95,"↓ "&TEXT((C5-B5)/B5,"0%"),"→ "&TEXT((C5-B5)/B5,"0%")))))
```

*This shows both arrow and percentage change*

**Column F (Trend Explanation) - Manual Entry Examples:**

| Metric | Q1 | Q2 | Trend | Explanation |
|--------|----|----|-------|-------------|
| Retention Coverage % | 85% | 100% | ↑ +18% | Completed retention schedule project for 15 remaining data categories (Mar-Apr 2024) |
| Shadow IT Count | 12 | 5 | ↑ -58% | Formalized 4 instances with DPAs, decommissioned 3 unauthorized systems |
| Forensic Test Pass Rate | 88% | 95% | ↑ +8% | Replaced HDD overwrite on SSDs with crypto-erase (7 systems) |
| Vendor SLA Compliance | 92% | 87% | ↓ -5% | AWS delayed deletion by 15 days (incident #INC-2024-045), escalated to account manager |

## Conditional Formatting

**Columns B-E (Quarterly Values):**

- Green fill if value improves vs. previous quarter (for metrics where higher is better)
- Red fill if value declines >5% vs. previous quarter
- Yellow fill if value stable (±5%)


**Column G (Trend Arrows):**

- Green text for ↑
- Red text for ↓
- Gray text for →


---

# Sheet 9: Executive Summary & Approval

## Purpose
Provide narrative summary for board presentation and capture three-level approval.

## Section 1: Executive Summary Narrative (Rows 3-40, Merged Cells)

**Structure (Text Entry Field, ~500-750 words):**
```
EXECUTIVE SUMMARY - [Quarter] [Year] A.8.10 COMPLIANCE DASHBOARD

[Organization]: [Organization Name]
Reporting Period: [Q1/Q2/Q3/Q4] [Year]
Prepared by: [Name, Title]
Date: [DD.MM.YYYY]

---

OVERALL STATUS:
[2-3 sentences: Maturity score, overall compliance status, trend vs. previous quarter]

KEY ACHIEVEMENTS:

- [Achievement 1 - quantified improvement]
- [Achievement 2 - milestone completed]
- [Achievement 3 - positive metric change]
- [Achievement 4 - regulatory compliance milestone]


KEY CONCERNS REQUIRING BOARD ATTENTION:

- [Concern 1 - critical gap with regulatory risk quantification]
- [Concern 2 - declining metric with impact analysis]
- [Concern 3 - resource constraint impeding progress]


NEXT QUARTER PRIORITIES:

- [Priority 1 - remediation initiative with timeline]
- [Priority 2 - resource requirement with budget]
- [Priority 3 - expected improvement target]


BOARD ACTION REQUESTED:

- [Action 1 - budget approval / resource allocation]
- [Action 2 - policy decision / strategic direction]
- [Action 3 - escalation support / vendor management]


---

DETAILED METRICS SUMMARY:
[Reference to Sheets 2-6 for detailed breakdowns]

REGULATORY COMPLIANCE STATUS:

- ISO 27001:2022 A.8.10: [Fully/Substantially/Partially Compliant]
- GDPR Article 17: [Compliant/Non-Compliant + evidence]
- Swiss FADP Article 6: [Compliant/Non-Compliant + evidence]


AUDIT READINESS:
[Organization] can demonstrate A.8.10 compliance to external auditors within [X] hours
with [complete/partial] evidence. [Gaps if any].

---

Prepared by: [Compliance Officer Name]
Reviewed by: [CISO Name]
Approved by: [Executive Sponsor Name]
```

**Formatting:**

- Font: Arial 11pt
- Line spacing: 1.5
- Bold headers for sections
- Bullet points for lists
- Merged cells for easy reading


## Section 2: Three-Level Approval (Rows 42-52, Table)

| Row | Column A (Level) | Column B (Role) | Column C (Name) | Column D (Signature) | Column E (Date) | Column F (Comments) |
|-----|------------------|----------------|----------------|---------------------|----------------|-------------------|
| 44 | Level 1 | Compliance Officer / Preparer | [Manual] | [Manual/Digital] | =TODAY() | [Manual] |
| 45 | Level 2 | Information Security Officer / CISO | [Manual] | [Manual/Digital] | [Manual] | [Manual] |
| 46 | Level 3 | Executive Sponsor / Audit Committee | [Manual] | [Manual/Digital] | [Manual] | [Manual] |

**Column E (Date) Validation:**

- Must be chronological: Level 2 date >= Level 1 date, Level 3 date >= Level 2 date
- Cannot be future dated
- Warning if >30 days between levels (delays)


## Section 3: Board Presentation Export (Rows 54-58)

**Instructions for exporting to PowerPoint:**

1. Copy Executive Summary (Rows 3-40)
2. Paste into PowerPoint slide (Blank layout)
3. Add charts/visuals from Sheets 2-6 if desired
4. Include data source reference: "Source: ISMS A.8.10 Compliance Dashboard Q[X] 2024"
5. Archive PDF of completed dashboard with board presentation materials

---

# Conditional Formatting Summary

## Global Rules (All Dashboard Sheets)

**RAG Status Cells (Column D in Sheets 2-6):**

- Green text + light green fill for "Green"
- Orange text + light orange fill for "Amber"
- Red bold text + light red fill for "Red"


**Percentage Metrics (Various cells):**

- Green fill if ≥90%
- Yellow fill if 70-89%
- Red fill if <70%


**Score Metrics (1-5 scale):**

- Green fill if ≥4.0
- Yellow fill if 3.0-3.9
- Red fill if <3.0


**Count Metrics (Gap counts, Shadow IT counts):**

- Green fill if 0
- Yellow fill if 1-5
- Red fill if >5


## Sheet-Specific Rules

**Sheet 2 (Overall Compliance):**

- Overall Maturity Score cell (B5): Large font (20pt), bold, colored fill based on RAG


**Sheet 7 (Critical Gaps):**

- Target Date column: Red fill if overdue, orange if <30 days, green if >30 days


**Sheet 8 (Trend Analysis):**

- Trend arrow cells: Icon sets (up/right/down arrows with colors)
- Quarterly value cells: Color scale (green = improvement, red = decline)


---

# Python Script Integration Notes

## Script: `generate_a810_5_compliance_dashboard.py`

**CRITICAL DIFFERENCE from A.8.10.1-4 Scripts:**

This workbook is a **DASHBOARD**, not an assessment workbook. Key differences:

1. **Fewer Data Entry Cells:** ~100-120 manual entry cells (vs. 260+ in assessments)
2. **More Formula Cells:** ~200-300 formulas for calculations, aggregations, RAG status
3. **No External File Links:** All data entry is manual (no `=VLOOKUP('[OtherFile.xlsx]Sheet'!A1)`)
4. **Quarterly Snapshot Structure:** Sheet 8 has Q1-Q4 columns (not just current state)

**Key Customization Areas for A.8.10.5:**

**1. Data Source Mapping Table (Sheet 1):**

- **DO NOT** hardcode source cell references in formulas
- **DO** create reference table showing manual entry instructions
- Table structure (in Sheet 1, Rows 17-80):

```
  Dashboard Sheet | Dashboard Cell | Source Workbook | Source Sheet | Source Cell | Metric | Data Type
```

**2. Manual Entry Cells (Yellow Fill):**

- Sheets 2-6: ~40-60 cells total (not 260+ like assessments)
- All cells UNPROTECTED (allow user entry)
- Data validation where applicable (percentages 0-100, scores 1-5)


**3. Formula Cells (Light Blue Fill, Protected):**

- RAG status formulas (IF statements based on thresholds)
- Aggregation formulas (AVERAGE, SUM, COUNTIF)
- Trend calculation formulas (comparing current vs. previous quarter)
- Component score calculations (weighted averages)
- **PROTECT** all formula cells to prevent accidental overwrites


**4. Maturity Scoring Formulas:**

- Overall Score (Sheet 2, B5):

```python
  formula = "=ROUND(('Sheet3'!B20*0.25)+('Sheet4'!B20*0.25)+('Sheet5'!B20*0.25)+('Sheet6'!B20*0.25),0)"
```

- Component Scores (Each sheet, Row 20, Column B): Weighted average per assessment area


**5. Trend Analysis Structure (Sheet 8):**

- Columns B-E: Q1, Q2, Q3, Q4 (manual entry)
- Column G: Trend formula comparing current vs. previous quarter

```python
  trend_formula = '=IF(ISBLANK(B5),"→",IF(C5>=B5*1.05,"↑",IF(C5<=B5*0.95,"↓","→")))'
```

**6. Conditional Formatting:**

- More extensive than assessments (RAG visualization critical for executive audience)
- Use `openpyxl` conditional formatting for:
  - Color scales (green-yellow-red)
  - Icon sets (arrows for trends)
  - Data bars (optional for percentages)


**7. Sheet Protection:**

- Sheet 1: Fully protected (instructions, read-only)
- Sheets 2-6: Protect formulas, leave manual entry cells unlocked
- Sheet 7: Fully unprotected (critical gaps manual entry)
- Sheet 8: Protect trend formulas, leave quarterly values unlocked
- Sheet 9: Fully unprotected (narrative text, approval)


## Script Validation Checks

**Before generating workbook, validate:**
```python
# Check 1: Data source mapping table has all required metrics
required_metrics = [
    'Retention Coverage %',
    'NIST Compliance %',
    'Vendor SLA Compliance %',
    'Audit Readiness Score',
    # ... (40-60 total)
]
assert len(data_source_mapping) >= 40, "Missing metrics in mapping table"

# Check 2: Formula cells are protected, manual entry cells are not
for sheet in [sheet2, sheet3, sheet4, sheet5, sheet6]:
    for row in sheet.iter_rows():
        for cell in row:
            if cell.fill.fgColor.rgb == 'FFFFFF00':  # Yellow = manual entry
                assert cell.protection.locked == False
            elif 'FORMULA' in str(cell.value):
                assert cell.protection.locked == True

# Check 3: RAG status formulas use correct thresholds
rag_formula_pattern = r'IF\(.*>=90.*Green.*IF\(.*>=70.*Amber.*Red'
assert re.search(rag_formula_pattern, sheet2['D5'].value)

# Check 4: Maturity score formula references all 4 component scores
maturity_formula = sheet2['B5'].value
assert "'Sheet3'!B20" in maturity_formula
assert "'Sheet4'!B20" in maturity_formula
assert "'Sheet5'!B20" in maturity_formula
assert "'Sheet6'!B20" in maturity_formula
assert "*0.25" in maturity_formula  # 25% weight each

# Check 5: Trend analysis has Q1-Q4 columns
assert sheet8['B4'].value == "Q1 [Year]"
assert sheet8['C4'].value == "Q2 [Year]"
assert sheet8['D4'].value == "Q3 [Year]"
assert sheet8['E4'].value == "Q4 [Year]"
```

## Common Mistakes to Avoid in Script

**1. ❌ CRITICAL ERROR: Creating External File Links**
```python
# WRONG - creates external file link (breaks if source file moved)
cell.value = "='[A_8_10_1_Retention.xlsx]Sheet7'!B5"

# CORRECT - manual entry instruction in mapping table
mapping_table.append([
    'Sheet 3', 'B5', 
    'A.8.10.1_Retention_[Date].xlsx', 'Sheet 7', 'B5',
    'Total Data Categories', 'Count'
])
cell.fill = yellow_fill  # Mark for manual entry
```

**2. ❌ Forgetting to Protect Formula Cells**
```python
# WRONG - formulas unprotected, user can accidentally overwrite
formula_cell.value = "=B5/B6*100"

# CORRECT - formulas protected
formula_cell.value = "=B5/B6*100"
formula_cell.protection = Protection(locked=True)
ws.protection.sheet = True
ws.protection.password = None  # Allow unlocking yellow cells
```

**3. ❌ Hardcoding Year in Trend Analysis**
```python
# WRONG - hardcoded 2024
sheet8['B4'].value = "Q1 2024"

# CORRECT - placeholder for user to fill
sheet8['B4'].value = "Q1 [Year]"
```

**4. ❌ Incorrect RAG Threshold Formulas**
```python
# WRONG - backwards logic (green for <70%)
formula = "=IF(B5<70,'Green',IF(B5<90,'Amber','Red'))"

# CORRECT - green for ≥90%
formula = "=IF(B5>=90,'Green',IF(B5>=70,'Amber','Red'))"
```

## Integration with Source Assessment Generators

**A.8.10.5 Dashboard is DEPENDENT on A.8.10.1-4:**

When developing/testing `generate_a810_5_compliance_dashboard.py`:

1. **First generate sample source workbooks:**
```python
   # Generate source assessments with test data
   exec(open('generate_a810_1_retention_triggers.py').read())
   exec(open('generate_a810_2_deletion_methods.py').read())
   exec(open('generate_a810_3_third_party_cloud.py').read())
   exec(open('generate_a810_4_verification_evidence.py').read())
```

2. **Manually populate sample data in source workbooks** (or use test data generator)

3. **Then generate dashboard workbook:**
```python
   exec(open('generate_a810_5_compliance_dashboard.py').read())
```

4. **Test manual entry workflow:**

   - Open dashboard workbook
   - Follow Data Source Mapping Table instructions
   - Manually copy values from source workbooks
   - Verify formulas calculate correctly


**Test Scenario:**
```
Source A.8.10.1 Sheet 7, B7 = 95% (Retention Coverage)
→ Copy to Dashboard Sheet 3, B7
→ Dashboard Sheet 3, D7 formula should show "Amber" (95% is 90-100 range but target is 100%)
→ Dashboard Sheet 2, B6 should show 95%
→ Overall Maturity Score should incorporate this value
```

---

# Version Control & Change Management

## Workbook Versioning

**Filename Format:**
```
ISMS_A_8_10_5_Compliance_Dashboard_YYYYMMDD_Qn.xlsx
```

**Example:** `ISMS_A_8_10_5_Compliance_Dashboard_20260130_Q1.xlsx`

**Quarterly Snapshots:**

- Keep separate file for each quarter (Q1, Q2, Q3, Q4)
- Archive previous quarters (read-only)
- Current quarter = working copy


**Version Tracking in Sheet 1:**

- Document ID: ISMS-IMP-A.8.10.5
- Version: 1.0
- Quarter: Q1/Q2/Q3/Q4 [Year]
- Date: DD.MM.YYYY


## Change Log

**Version 1.0 → 2.0 Changes:**

- Added PART I: USER COMPLETION GUIDE (comprehensive user documentation)
- Enhanced PART II: TECHNICAL SPECIFICATION (detailed Excel structure)
- Added Data Source Mapping Table (prevents manual entry errors)
- Strengthened Maturity Scoring Model (weighted component scoring)
- Added Quarterly Trend Analysis (Q1-Q4 comparison)
- Improved Executive Summary guidance (board presentation focus)
- Enhanced conditional formatting (RAG visualization)
- Updated approval workflow (three-level sign-off)


## Backward Compatibility

**v2.0 Workbooks:**

- Compatible with Excel 2016+
- Compatible with LibreOffice Calc 6.0+ (minor formatting differences)
- Not compatible with Google Sheets (use Excel Online for cloud access)


**v1.0 to v2.0 Migration:**

- No automated migration (different structure)
- Manually transfer Q1 baseline from v1.0 to v2.0 Sheet 8 if upgrading mid-year
- Recommend starting v2.0 at beginning of new fiscal year or quarter


---

# Quality Assurance Checklist

## Pre-Deployment Validation

Before using generated dashboard workbook, verify:

**Data Source Mapping (Sheet 1):**

- [ ] All 40-60 metrics documented in mapping table
- [ ] Source cell references match actual source workbook structure
- [ ] No broken references or TBD placeholders


**Formula Accuracy (Sheets 2-6):**

- [ ] RAG status formulas use correct thresholds (≥90% green, 70-89% amber, <70% red)
- [ ] Component score formulas use correct weightings (sum to 100%)
- [ ] Overall Maturity Score formula references all 4 component scores
- [ ] No #REF!, #DIV/0!, #VALUE! errors in any formula cells


**Manual Entry Cells:**

- [ ] All manual entry cells have yellow fill
- [ ] Manual entry cells are UNLOCKED (not protected)
- [ ] Data validation applied where appropriate (percentages 0-100, dates)


**Protection:**

- [ ] Formula cells are LOCKED (protected)
- [ ] Instructions sheet fully protected
- [ ] Manual entry cells remain editable when sheet protection enabled


**Conditional Formatting:**

- [ ] RAG status colors apply correctly
- [ ] Trend arrows display correctly (↑↓→)
- [ ] Overdue dates highlighted in red


## Post-Completion Validation

After manual data entry, verify:

- [ ] All yellow cells populated (no blanks)
- [ ] NIST category percentages sum to 100% (Sheet 4, B10+B11+B12=100)
- [ ] Component scores calculate correctly (Sheets 3-6, Row 20)
- [ ] Overall Maturity Score matches manual calculation
- [ ] Trend Analysis shows realistic quarter-over-quarter changes
- [ ] Critical Gaps Dashboard has remediation dates for all gaps
- [ ] Executive Summary narrative matches quantitative data
- [ ] Three-level approval completed with dates


---

# Integration with ISMS Management Review

## ISO 27001 Clause 9.3 Requirement

**ISO 27001:2022 Clause 9.3.2:**
> *"The management review shall include consideration of... the results of monitoring and measurement."*

**A.8.10.5 Dashboard fulfills this requirement** by providing:

- Systematic monitoring results (quarterly assessments)
- Measurable compliance metrics (percentages, scores, counts)
- Trend analysis (improvement or decline identification)
- Performance evaluation (maturity scoring model)


## Dashboard Integration into Management Review

**Recommended Agenda Item:**
```
ISMS MANAGEMENT REVIEW - Control A.8.10 (Information Deletion)

1. Overall Compliance Status

   - Present Sheet 2 (Overall A.8.10 Compliance)
   - Highlight maturity score and trend vs. previous quarter


2. Assessment Area Deep Dives (if significant changes)

   - Retention Schedule Health (Sheet 3) - if coverage changed ±5%
   - Deletion Method Effectiveness (Sheet 4) - if NIST compliance changed ±5%
   - Third-Party Performance (Sheet 5) - if Shadow IT or SLA issues
   - Verification Quality (Sheet 6) - if audit readiness changed


3. Critical Gaps Requiring Management Decision

   - Present Sheet 7 (Critical Gaps Dashboard)
   - Request budget approval for remediation
   - Assign accountability for high-priority gaps


4. Regulatory Compliance Status

   - GDPR Article 17: [Compliant/Non-Compliant + evidence]
   - Swiss FADP Article 6: [Compliant/Non-Compliant + evidence]
   - ISO 27001 A.8.10: [Conformity statement]


5. Management Decisions & Actions

   - Approve remediation budgets
   - Set target maturity score for next quarter
   - Escalate vendor performance issues (if applicable)

```

## Documentation Requirements

**Archive with Management Review Minutes:**

- PDF export of completed dashboard (Sheets 2-6 summary + Executive Summary)
- Quarter designation (Q1/Q2/Q3/Q4 [Year])
- Management decisions and action items
- Link to source assessment workbooks (A.8.10.1-4) for detailed evidence


---

**END OF SPECIFICATION**

---

*"We have to accept that nature behaves in a way that seems strange to us, because we evolved to understand the macroscopic world."*
— Alain Aspect

*Where bamboo antennas actually work.* 🎋
